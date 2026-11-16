// Landing page gate: runs the polish and ship checks against a running page.
// Usage: node check.mjs <url> [--chromium <path>]
// Run from a directory where `playwright` is installed (the product repo).
// Prints PASS / WARN / FAIL / ERROR per check. Exits 0 clean, 1 on any FAIL, 2 when a check
// couldn't run (ERROR), which is a failure too, never a pass; 2 wins over 1.
// Elements inside a `data-ui` root (the live product) are exempt from the page rules, except the
// inert-input tell, since the fake input is usually in the product fragment.
// Local dev servers make the LCP number meaningless; judge it on a preview deploy.

import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

// Playwright resolves from beside this script, then from the current directory (the product repo).
const load = async () => {
  try { return await import('playwright'); } catch {}
  const require = createRequire(pathToFileURL(process.cwd() + '/').href);
  return import(pathToFileURL(require.resolve('playwright')).href);
};
const pw = await load().catch(() => null);
const chromium = pw?.chromium ?? pw?.default?.chromium;
if (!chromium) {
  console.log('ERROR  playwright  (not found beside the script or in the current directory; run from the product repo with playwright installed)');
  process.exit(2);
}

const args = process.argv.slice(2);
const url = args.find((a) => /^https?:\/\//.test(a));
if (!url) {
  console.error('usage: node check.mjs <url> [--chromium <path>]');
  process.exit(2);
}
const ci = args.indexOf('--chromium');
const executablePath = ci >= 0 ? args[ci + 1] : process.env.CHROMIUM_PATH;

const results = [];
const report = (status, name, detail = '') => results.push({ status, name, detail });
const pass = (n, d) => report('PASS', n, d);
const warn = (n, d) => report('WARN', n, d);
const fail = (n, d) => report('FAIL', n, d);
const error = (n, d) => report('ERROR', n, d);
const check = (ok, n, d, soft = false) => (ok ? pass(n, d) : soft ? warn(n, d) : fail(n, d));

const browser = await chromium.launch(executablePath ? { executablePath } : {}).catch((e) => {
  console.log(`ERROR  browser launch  (${String(e).split('\n')[0].slice(0, 200)})`);
  process.exit(2);
});

// Runs one group of checks; a crash is reported as ERROR and the other groups still run.
let loaded = false;
const step = async (name, fn) => {
  try { await fn(); } catch (e) { error(name, String(e).split('\n')[0].slice(0, 200)); }
};

// Counts every animation the page starts (CSS, transitions, WAAPI and Motion) and the LCP entry.
const instrument = () => {
  window.__anims = 0;
  const bump = (el) => { if (!el?.closest?.('[data-ui]')) window.__anims++; };
  document.addEventListener('animationstart', (e) => bump(e.target), true);
  document.addEventListener('transitionstart', (e) => bump(e.target), true);
  const orig = Element.prototype.animate;
  Element.prototype.animate = function (...a) { bump(this); return orig.apply(this, a); };
  window.__lcp = null;
  window.__lcpEl = null;
  try {
    new PerformanceObserver((l) => {
      const e = l.getEntries().at(-1);
      if (e) { window.__lcp = { t: Math.round(e.startTime), tag: e.element?.tagName ?? null }; window.__lcpEl = e.element ?? null; }
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  } catch {}
};

async function desktop() {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  await ctx.addInitScript(instrument);
  const page = await ctx.newPage();
  const res = await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  if (!res || !res.ok()) throw new Error(`page didn't load (status ${res?.status()}); no check below means anything`);
  pass('page loads', `status ${res.status()}`);
  loaded = true;
  await page.waitForTimeout(2500);

  // Dev server: minifiers change what ships, so the last pass runs on the production build.
  const dev = await page.evaluate(() => !!document.querySelector('script[src*="@vite/client"], script[src*="react-refresh"], script[src*="webpack-hmr"], nextjs-portal') || window.__NEXT_DATA__?.buildId === 'development');
  check(!dev, 'production build, not a dev server', dev ? 'dev server detected; rerun on the build before shipping' : '', true);

  // Head and meta
  const head = await page.evaluate(() => {
    const m = (s) => document.querySelector(s);
    const c = (s) => m(s)?.getAttribute('content') ?? null;
    return {
      title: document.title,
      lang: document.documentElement.lang,
      description: c('meta[name="description"]'),
      ogTitle: c('meta[property="og:title"]'),
      ogImage: c('meta[property="og:image"]'),
      twitterCard: c('meta[name="twitter:card"]'),
      svgIcon: !!m('link[rel~="icon"][type="image/svg+xml"], link[rel~="icon"][href$=".svg"]'),
      appleIcon: !!m('link[rel="apple-touch-icon"]'),
      themeColor: !!m('meta[name="theme-color"]'),
      h1s: document.querySelectorAll('h1').length,
      imgsNoAlt: [...document.images].filter((i) => !i.hasAttribute('alt')).length,
      hasInput: !!document.querySelector('input:not([type="hidden"]), textarea'),
      skip: (() => { const a = document.querySelector('a[href^="#"]'); return a ? a.textContent.trim() : null; })(),
    };
  });
  check(head.title, 'title', head.title);
  check(head.lang, 'html lang', head.lang);
  check(head.description, 'meta description');
  check(head.ogTitle, 'og:title');
  check(head.twitterCard === 'summary_large_image', 'twitter:card summary_large_image', head.twitterCard ?? 'missing');
  if (head.ogImage) {
    // Crawlers need an absolute URL they can reach, an image under 5 MB, and 1200x630.
    check(/^https?:\/\//.test(head.ogImage), 'og:image is an absolute URL', head.ogImage);
    const src = new URL(head.ogImage, url).href;
    if (/\/\/(localhost|127\.0\.0\.1|0\.0\.0\.0)[:/]/.test(src)) warn('og:image reachable by crawlers', 'points at localhost; X and others can\'t fetch it, recheck on the deploy');
    const r = await ctx.request.get(src).catch(() => null);
    check(r && r.ok(), 'og:image fetches', `${r?.status()} ${head.ogImage}`);
    if (r && r.ok()) {
      const type = r.headers()['content-type'] || '';
      const bytes = (await r.body()).length;
      check(type.startsWith('image/'), 'og:image is an image', type || 'no content-type');
      check(bytes <= 5 * 1024 * 1024, 'og:image under 5 MB', `${Math.round(bytes / 1024)} KB`);
      const dim = await page.evaluate((u) => new Promise((done) => {
        const i = new Image();
        i.onload = () => done({ w: i.naturalWidth, h: i.naturalHeight });
        i.onerror = () => done(null);
        i.src = u;
      }), src);
      if (!dim) fail('og:image decodes', src);
      else if (dim.w === 1200 && dim.h === 630) pass('og:image 1200x630');
      else if (dim.w > 1200 && Math.abs(dim.w / dim.h - 1200 / 630) < 0.01) warn('og:image 1200x630', `${dim.w}x${dim.h}: right ratio, heavier than it needs to be`);
      else fail('og:image 1200x630', `${dim.w}x${dim.h}`);
    }
  } else fail('og:image', 'missing');
  check(head.svgIcon, 'svg favicon', '', true);
  check(head.appleIcon, 'apple-touch-icon');
  check(head.themeColor, 'theme-color meta', '', true);
  check(head.h1s === 1, 'one h1', `${head.h1s}`);
  check(head.imgsNoAlt === 0, 'alt on every img', `${head.imgsNoAlt} missing`);

  // Stylesheet text, same-origin and cross-origin, parsed in the page.
  const hrefs = await page.evaluate(() => [...document.styleSheets].map((s) => s.href).filter(Boolean));
  const inline = await page.evaluate(() => [...document.querySelectorAll('style')].map((s) => s.textContent));
  const fetched = [];
  const unfetched = [];
  for (const h of hrefs) {
    const r = await ctx.request.get(h).catch(() => null);
    if (r && r.ok()) fetched.push(await r.text());
    else unfetched.push(h);
  }
  if (unfetched.length) warn('stylesheets fetched', `${unfetched.length} couldn't be read, so the CSS checks didn't see them: ${unfetched.join(' ').slice(0, 160)}`);
  const css = await page.evaluate((texts) => {
    const out = { selection: false, focusVisible: false, scrollbar: false, caret: false, fallbackFace: false, hoverUnguarded: 0, hoverGuarded: 0, transitionAll: 0, vw100: [] };
    const walk = (rules, guarded) => {
      for (const r of rules) {
        if (r instanceof CSSMediaRule) walk(r.cssRules, guarded || /hover\s*:\s*hover/.test(r.conditionText || r.media.mediaText));
        else if (r.cssRules && r.cssRules.length && !(r instanceof CSSStyleRule)) walk(r.cssRules, guarded);
        else if (r instanceof CSSFontFaceRule) { if (/size-adjust|ascent-override/.test(r.cssText)) out.fallbackFace = true; }
        else if (r instanceof CSSStyleRule) {
          const s = r.selectorText || '';
          if (s.includes('[data-ui]')) continue; // the live product keeps its own conventions
          if (s.includes('::selection')) out.selection = true;
          if (r.style.caretColor) out.caret = true;
          if ([r.style.width, r.style.minWidth].includes('100vw')) out.vw100.push(s.slice(0, 40));
          if (s.includes(':focus-visible')) out.focusVisible = true;
          if (s.includes('::-webkit-scrollbar') || /scrollbar-(color|width)/.test(r.style.cssText)) out.scrollbar = true;
          if (/transition(-property)?\s*:\s*all\b/.test(r.style.cssText)) out.transitionAll++;
          if (s.includes(':hover')) guarded ? out.hoverGuarded++ : out.hoverUnguarded++;
          if (r.cssRules && r.cssRules.length) walk(r.cssRules, guarded);
        }
      }
    };
    for (const t of texts) {
      try { const sh = new CSSStyleSheet(); sh.replaceSync(t); walk(sh.cssRules, false); } catch {}
    }
    out.colorScheme = getComputedStyle(document.documentElement).colorScheme;
    out.overflowX = [document.documentElement, document.body].map((e) => getComputedStyle(e).overflowX);
    return out;
  }, [...inline, ...fetched]);
  check(css.selection, '::selection styled');
  check(css.focusVisible, ':focus-visible styled');
  check(css.scrollbar, 'scrollbar styled', '', true);
  check(css.colorScheme && css.colorScheme !== 'normal', 'color-scheme set', css.colorScheme);
  check(css.fallbackFace, 'metric-matched fallback font face', '', true);
  check(css.transitionAll === 0, 'no transition: all', `${css.transitionAll} rules`, true);
  check(css.hoverUnguarded === 0 || css.hoverGuarded > 0, 'hover rules guarded by (hover: hover)', `${css.hoverGuarded} guarded, ${css.hoverUnguarded} not`, true);
  if (head.hasInput) check(css.caret, 'caret-color set', '', true);
  // hidden on html or body makes a scroll container, which breaks position: sticky; clip doesn't.
  check(!css.overflowX.includes('hidden'), 'overflow-x: clip, not hidden, on html and body', `html ${css.overflowX[0]}, body ${css.overflowX[1]}`, true);
  check(css.vw100.length === 0, 'no 100vw widths (they include the scrollbar)', css.vw100.join(', '), true);

  // Font preloads
  const preloads = await page.evaluate(() => [...document.querySelectorAll('link[rel="preload"][as="font"]')].map((l) => ({ href: l.href, co: l.hasAttribute('crossorigin') })));
  check(preloads.length > 0, 'fonts preloaded', `${preloads.length}`, true);
  const badPreload = preloads.filter((p) => !/\.woff2(\?|$)/.test(p.href) || !p.co);
  check(badPreload.length === 0, 'preloads are woff2 with crossorigin', badPreload.map((p) => p.href).join(' '));

  // Skip link and focus ring
  await page.keyboard.press('Tab');
  const first = await page.evaluate(() => {
    const e = document.activeElement;
    const r = e?.getBoundingClientRect();
    return e && e !== document.body ? { text: (e.textContent || '').trim().slice(0, 40), visible: r.width > 0 && r.top >= 0 && r.top < innerHeight } : null;
  });
  check(first && /skip/i.test(first.text) && first.visible, 'skip link is first Tab stop', first?.text ?? 'nothing focused');
  const rings = [];
  for (let i = 0; i < 10; i++) {
    rings.push(await page.evaluate(() => {
      const e = document.activeElement;
      if (!e || e === document.body) return null;
      const cs = getComputedStyle(e);
      return { fv: e.matches(':focus-visible'), outline: cs.outlineStyle, ring: cs.outlineStyle !== 'none' && cs.outlineStyle !== 'auto' ? 'outline' : cs.boxShadow !== 'none' ? 'shadow' : cs.outlineStyle };
    }));
    await page.keyboard.press('Tab');
  }
  const seen = rings.filter(Boolean);
  const uaRings = seen.filter((r) => r.ring === 'auto' || r.ring === 'none');
  check(seen.length && uaRings.length === 0, 'custom focus ring on Tab stops', `${uaRings.length}/${seen.length} use UA auto or none`);

  // Nav scroll state
  const navAt = () => page.evaluate(() => {
    const h = document.querySelector('header, [role="banner"]');
    if (!h) return null;
    const cs = getComputedStyle(h);
    return { pos: cs.position, bg: cs.backgroundColor, sh: cs.boxShadow, bb: cs.borderBottomColor + cs.borderBottomWidth, bf: cs.backdropFilter };
  });
  const top = await navAt();
  await page.evaluate(() => window.scrollTo(0, 700));
  await page.waitForTimeout(800);
  const scrolled = await navAt();
  if (!top) fail('header element', 'no <header>');
  else if (!/sticky|fixed/.test(top.pos)) warn('nav scroll state', `header is ${top.pos}; fine if deliberate`);
  else {
    const changed = top.bg !== scrolled.bg || top.sh !== scrolled.sh || top.bb !== scrolled.bb;
    const alwaysGlass = top.bf && top.bf !== 'none';
    check(changed || alwaysGlass, 'nav has a scrolled state', changed ? 'changes on scroll' : alwaysGlass ? 'permanent blur' : 'header looks the same at 0 and 700px');
  }

  // Animation budget over a full scroll
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(300);
  const before = await page.evaluate(() => window.__anims);
  const height = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < height; y += 600) {
    await page.evaluate((v) => window.scrollTo(0, v), y);
    await page.waitForTimeout(250);
  }
  const scrollAnims = (await page.evaluate(() => window.__anims)) - before;
  const per10k = Math.round((scrollAnims / Math.max(height, 1)) * 10000);
  check(per10k <= 40, 'scroll animations under 40 per 10,000px', `${scrollAnims} over ${height}px (${per10k} per 10k)`, true);

  const lcp = await page.evaluate(() => window.__lcp);
  check(lcp && lcp.t <= 2500, 'LCP under 2.5s (judge on a deploy, not localhost)', lcp ? `${lcp.t}ms on ${lcp.tag}` : 'no entry', true);
  const lcpImg = await page.evaluate(() => {
    const e = window.__lcpEl;
    return e && e.tagName === 'IMG' ? { lazy: e.loading === 'lazy', fp: e.getAttribute('fetchpriority'), src: (e.currentSrc || e.src).slice(-60) } : null;
  });
  if (lcpImg) {
    check(!lcpImg.lazy, 'LCP image not lazy-loaded', lcpImg.src);
    check(lcpImg.fp === 'high', 'LCP image has fetchpriority="high"', lcpImg.src, true);
  }
  const heads = await page.evaluate(() => [...document.querySelectorAll('h1, h2')].filter((e) => !e.closest('[data-ui]') && e.getClientRects().length)
    .filter((e) => { const cs = getComputedStyle(e); return cs.overflowWrap === 'normal' && cs.wordBreak === 'normal'; }).length);
  check(heads === 0, 'display heads set overflow-wrap: break-word', `${heads} h1/h2 without it`, true);

  // Agent tells (rubric.md): a "scroll" cue, bold runs in body copy, an input that takes focus but not typing
  const tells = await page.evaluate(() => {
    const shown = (e) => e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden';
    const cue = [...document.querySelectorAll('body *')].filter((e) => [...e.children].every((c) => !c.textContent.trim()) && shown(e) && /^\s*(↓\s*)?scroll(\s+(down|to explore|for more))?\s*(↓)?\s*$/i.test(e.textContent)).length;
    const bold = [...document.querySelectorAll('p strong, p b')].filter((e) => shown(e) && !e.closest('[data-ui], footer, nav')).map((e) => e.textContent.trim().slice(0, 30));
    const inert = [...document.querySelectorAll('input[readonly], textarea[readonly]')].filter((e) => shown(e) && e.tabIndex >= 0 && e.type !== 'hidden').length;
    return { cue, bold, inert };
  });
  check(tells.cue === 0, 'no "scroll" cue', `${tells.cue} element(s) telling the visitor to scroll`, true);
  check(tells.bold.length < 3, 'no bold runs in body copy', `${tells.bold.length} in paragraphs: ${tells.bold.slice(0, 4).join(' | ')}`, true);
  check(tells.inert === 0, 'no input that takes focus but not typing', `${tells.inert} focusable readonly field(s); wire them or set them as a still`, true);

  // Forms
  const forms = await page.evaluate(() => [...document.querySelectorAll('input[type="email"]')].filter((i) => !i.closest('[data-ui]')).map((i) => {
    const f = i.closest('form');
    return { ac: i.getAttribute('autocomplete'), im: i.getAttribute('inputmode'), nv: f?.noValidate ?? false, live: !!f?.querySelector('[aria-live], [role="status"], [role="alert"]') };
  }));
  forms.forEach((f, n) => check(f.ac && f.nv && f.live, `email form ${n + 1}: autocomplete, novalidate, live region`, JSON.stringify(f)));

  await ctx.close();
}

async function theme(scheme) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: scheme });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  const at = await page.evaluate(() => ({ cls: document.documentElement.className, data: document.documentElement.dataset.theme ?? null, cs: getComputedStyle(document.documentElement).colorScheme }));
  await ctx.close();
  return at;
}

async function reducedMotion() {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(2500);
  const r = await page.evaluate(() => {
    const all = document.getAnimations().filter((a) => a.playState === 'running');
    const inf = all.filter((a) => a.effect?.getTiming?.().iterations === Infinity);
    const hidden = [...document.querySelectorAll('main h1, main h2, main p')].filter((e) => parseFloat(getComputedStyle(e).opacity) < 0.1).length;
    return { inf: inf.length, hidden };
  });
  check(r.inf === 0, 'reduced motion stops infinite loops', `${r.inf} running`);
  check(r.hidden === 0, 'reduced motion leaves no content invisible', `${r.hidden} text elements at opacity < 0.1`);
  await ctx.close();
}

async function mobile(width) {
  const ctx = await browser.newContext({ viewport: { width, height: 760 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(2000);
  const m = await page.evaluate((w) => {
    const h = document.querySelector('h1');
    const lh = h ? parseFloat(getComputedStyle(h).lineHeight) || parseFloat(getComputedStyle(h).fontSize) * 1.1 : 0;
    const small = [...document.querySelectorAll('header a, header button')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && (r.width < 24 || r.height < 24);
    }).map((e) => { const r = e.getBoundingClientRect(); return `${(e.getAttribute('aria-label') || e.textContent.trim() || e.tagName).slice(0, 20)} ${Math.round(r.width)}x${Math.round(r.height)}`; });
    return { sw: document.documentElement.scrollWidth, lines: h ? Math.round(h.getBoundingClientRect().height / lh) : null, small };
  }, width);
  if (width === 320) {
    check(m.sw <= 320, 'no horizontal overflow at 320', `scrollWidth ${m.sw}`);
    check(m.lines !== null && m.lines <= 3, 'h1 three lines or fewer at 320', `${m.lines}`, true);
  }
  if (width === 375) {
    check(m.small.length === 0, 'header targets 24px or larger at 375', m.small.join(', '));
    const btn = page.locator('header button[aria-expanded]').first();
    if (await btn.count()) {
      await btn.click({ timeout: 3000 }).catch(() => {});
      await page.waitForTimeout(600);
      const s = await page.evaluate(() => {
        const d = document.querySelector('[role="dialog"], [aria-modal="true"]');
        const lock = [document.body, document.documentElement].some((e) => getComputedStyle(e).overflow === 'hidden');
        return { dialog: !!d, lock, focusIn: d ? d.contains(document.activeElement) : false };
      });
      check(s.dialog, 'mobile menu is a dialog');
      check(s.lock, 'mobile menu locks scroll');
      check(s.focusIn, 'mobile menu moves focus in', '', true);
      await page.keyboard.press('Escape');
      await page.waitForTimeout(400);
      check((await btn.getAttribute('aria-expanded')) !== 'true', 'Escape closes mobile menu');
    } else warn('mobile menu', 'no header button[aria-expanded] found; check by hand');
  }
  await ctx.close();
}

// One page resized through the widths: overflow, wrapping buttons, the first screen at 1280x800,
// the container at 1920, sticky elements under the nav, and words the phone never gets.
const SWEEP = [320, 375, 768, 1024, 1280, 1440, 1920];
const measure = () => {
  const free = (e) => !e.closest('[data-ui]');
  const shown = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && e.checkVisibility({ visibilityProperty: true, checkVisibilityCSS: true }); };
  const label = (e) => (e.getAttribute('aria-label') || e.textContent || e.value || e.tagName).trim().replace(/\s+/g, ' ').slice(0, 24);
  const buttonish = (e) => {
    if (e.matches('button, [role="button"], input[type="submit"], input[type="button"], header a, nav a')) return true;
    const cs = getComputedStyle(e);
    const bg = cs.backgroundColor !== 'transparent' && !/rgba\(.*,\s*0\)$/.test(cs.backgroundColor);
    const border = parseFloat(cs.borderTopWidth) > 0 && cs.borderTopStyle !== 'none';
    return cs.display !== 'inline' && (bg || border);
  };
  // Lines of text in an element, from its text nodes' line boxes (icons and padding don't count).
  const lines = (e) => {
    const tops = [];
    const walk = document.createTreeWalker(e, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    for (let n = walk.nextNode(); n; n = walk.nextNode()) {
      if (!n.textContent.trim()) continue;
      range.selectNodeContents(n);
      for (const r of range.getClientRects()) if (r.width > 1) tops.push({ mid: (r.top + r.bottom) / 2, h: r.height });
    }
    tops.sort((a, b) => a.mid - b.mid);
    let count = 0, last = -Infinity;
    for (const t of tops) { if (t.mid - last > t.h * 0.5) { count++; last = t.mid; } }
    return count;
  };
  const buttons = [...document.querySelectorAll('button, [role="button"], input[type="submit"], input[type="button"], a')]
    .filter((e) => free(e) && shown(e) && buttonish(e) && (e.textContent.trim() || e.value));
  const wrapped = buttons.filter((e) => lines(e) > 1).map(label);

  // The first screen: h1, the first sentence after it, the first button-like action after it.
  const h = document.querySelector('h1');
  const after = (sel, ok) => h && [...document.querySelectorAll(sel)].find((e) => (h.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) && !h.contains(e) && free(e) && shown(e) && ok(e));
  const lede = after('p', (e) => e.textContent.trim().split(/\s+/).length >= 5);
  const cta = after('a, button', (e) => buttonish(e) && !e.closest('header, nav'));
  const inView = (e) => { if (!e) return null; const r = e.getBoundingClientRect(); return r.top >= 0 && r.bottom <= innerHeight; };

  // Container: the horizontal extent of text blocks outside the live product.
  const blocks = [...document.querySelectorAll('main h1, main h2, main h3, main p, main li')].filter((e) => free(e) && shown(e) && e.textContent.trim());
  const rects = blocks.map((e) => e.getBoundingClientRect());
  const extent = rects.length ? { left: Math.round(Math.min(...rects.map((r) => r.left))), right: Math.round(Math.max(...rects.map((r) => r.right))) } : null;

  // Sticky elements outside the header that would slide under a pinned header, or each other.
  const header = document.querySelector('header, [role="banner"]');
  const hcs = header && getComputedStyle(header);
  const pinned = hcs && /sticky|fixed/.test(hcs.position) ? header.getBoundingClientRect().height : 0;
  const stickies = [...document.querySelectorAll('body *')].filter((e) => free(e) && !(header && (header === e || header.contains(e))) && getComputedStyle(e).position === 'sticky')
    .map((e) => ({ top: parseFloat(getComputedStyle(e).top), name: e.tagName.toLowerCase() + (e.id ? '#' + e.id : e.classList[0] ? '.' + e.classList[0] : '') }))
    .filter((x) => !Number.isNaN(x.top) && x.top < Math.max(pinned, 1));

  // Visible words outside the nav, header, dialogs, and the live product.
  let words = 0;
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = tw.nextNode(); n; n = tw.nextNode()) {
    const p = n.parentElement;
    if (!p || p.closest('header, nav, [role="dialog"], [data-ui], script, style, noscript, template')) continue;
    if (!p.checkVisibility({ visibilityProperty: true, checkVisibilityCSS: true })) continue;
    words += n.textContent.trim().split(/\s+/).filter(Boolean).length;
  }

  return {
    sw: document.documentElement.scrollWidth, wrapped,
    hero: { h1: inView(h), lede: inView(lede), cta: inView(cta), found: { h1: !!h, lede: !!lede, cta: !!cta } },
    extent, pinned: Math.round(pinned), stickies, words,
  };
};

async function sweep() {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(2000);
  const at = {};
  for (const w of SWEEP) {
    await page.setViewportSize({ width: w, height: w === 1280 ? 800 : w === 1920 ? 1080 : 900 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(500);
    at[w] = await page.evaluate(measure);
  }
  const over = SWEEP.filter((w) => w > 320 && at[w].sw > w).map((w) => `${w}: ${at[w].sw}`);
  check(over.length === 0, 'no horizontal overflow 375 to 1920', over.join(', '));
  const wraps = SWEEP.filter((w) => at[w].wrapped.length).map((w) => `${w}: ${[...new Set(at[w].wrapped)].slice(0, 4).join(' | ')}`);
  check(wraps.length === 0, 'button and nav labels never wrap, 320 to 1920', wraps.join('; '));

  const hero = at[1280].hero;
  if (!hero.found.h1) fail('first screen at 1280x800', 'no h1');
  else {
    const missing = ['h1', 'lede', 'cta'].filter((k) => hero.found[k] && !hero[k]);
    check(missing.length === 0, 'headline, lede, and CTA visible at 1280x800', missing.length ? `${missing.join(', ')} below the fold` : '');
    if (!hero.found.cta) fail('primary action after the h1', 'no button or button-like link found');
    if (!hero.found.lede) warn('supporting sentence after the h1', 'none found');
  }

  const e = at[1920].extent;
  check(!e || (e.left >= 120 && e.right <= 1920 - 120), 'container capped at 1920', e ? `text spans ${e.left} to ${e.right}px` : 'no text in main', true);

  const st = at[1440];
  if (st.pinned) check(st.stickies.length === 0, 'nothing sticky slides under the pinned nav', st.stickies.map((x) => `${x.name} top:${x.top}`).join(', '));
  else check(st.stickies.length < 2, 'at most one sticky top:0', st.stickies.map((x) => x.name).join(', '), true);

  const lost = at[1440].words - at[375].words;
  check(lost < 40, 'phone gets the same content (under 40 words hidden at 375)', `${at[1440].words} words at 1440, ${at[375].words} at 375`, true);
  await ctx.close();
}

// With scripting off, a reveal that waits on JavaScript leaves the page blank.
async function noScript() {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, javaScriptEnabled: false });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  const r = await page.evaluate(() => {
    const text = [...document.querySelectorAll('h1, h2, h3, p, li, a, button')].filter((e) => !e.closest('[data-ui], noscript') && e.textContent.trim());
    const hidden = text.filter((e) => { const cs = getComputedStyle(e); return parseFloat(cs.opacity) < 0.1 || cs.visibility === 'hidden'; });
    return { h1: !!document.querySelector('h1'), hidden: hidden.length, sample: hidden.slice(0, 3).map((e) => e.textContent.trim().slice(0, 30)) };
  });
  if (!r.h1) warn('page renders without JavaScript', 'no h1 without scripting; prerender the page');
  else check(r.hidden === 0, 'reveals visible with JavaScript off', r.hidden ? `${r.hidden} hidden: ${r.sample.join(' | ')}` : '');
  await ctx.close();
}

async function notFound() {
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const res = await page.goto(new URL('/zz-not-a-page-' + Date.now(), url).href, { waitUntil: 'domcontentloaded' });
  const title = await page.title().catch(() => '');
  check(res?.status() === 404, '404 returns status 404', `${res?.status()}`);
  check(/404|not found/i.test(title + (await page.textContent('body').catch(() => ''))), '404 page is branded', title, true);
  await ctx.close();
}

await step('desktop checks', desktop);
// The first group proves the page loads; without it the rest would only repeat the same error.
if (loaded) {
  await step('theme at first paint', async () => {
    const dark = await theme('dark');
    const light = await theme('light');
    check(dark.cs.includes('dark') || /dark/.test(dark.cls + dark.data), 'theme set before paint (dark)', JSON.stringify(dark), true);
    check(light.cs.includes('light') || /light/.test(light.cls + light.data) || !dark.cs.includes('dark'), 'theme set before paint (light)', JSON.stringify(light), true);
  });
  await step('reduced motion', reducedMotion);
  await step('JavaScript off', noScript);
  await step('width sweep', sweep);
  await step('mobile 320', () => mobile(320));
  await step('mobile 375', () => mobile(375));
  await step('404', notFound);
}
await browser.close();

for (const r of results) console.log(`${r.status.padEnd(5)}  ${r.name}${r.detail ? `  (${r.detail})` : ''}`);
const count = (s) => results.filter((r) => r.status === s).length;
const [fails, warns, errors] = [count('FAIL'), count('WARN'), count('ERROR')];
console.log(`\n${count('PASS')} pass, ${warns} warn, ${fails} fail, ${errors} couldn't run`);
if (errors) console.log('A check that couldn\'t run is a failure, not a pass: fix the setup and rerun.');
process.exit(errors ? 2 : fails ? 1 : 0);

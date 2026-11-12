// Brand gate: the measurable checks before any critic sees the work.
// Usage (run from a directory where `playwright` is installed, the product repo):
//   node check.mjs tokens <tokens.css> [--pairs fg:bg,fg:bg] [--ui fg:bg,...]
//   node check.mjs page <url> [--fonts "Face A,Face B"] [--out board.png]
//   node check.mjs mark <mark.svg> [--out strip.png]
// tokens: tells lint on color and font tokens; WCAG contrast (4.5:1 text pairs, 3:1 --ui pairs) with APCA Lc beside it.
// page:   every named face loads (document.fonts.check), font family count, distinct text colors, 1440 screenshot.
// mark:   vector-only checks, then a strip at 16/32/64/512 on light and dark plus a one-color render.
// Prints PASS / WARN / FAIL per check; exits 1 on any FAIL.

import fs from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';

const [mode, target, ...rest] = process.argv.slice(2);
const opt = (k) => { const i = rest.indexOf(k); return i >= 0 ? rest[i + 1] : undefined; };
if (!mode || !target) {
  console.error('usage: node check.mjs tokens|page|mark <target> [options]');
  process.exit(2);
}

const results = [];
const report = (status, name, detail = '') => results.push({ status, name, detail });
const check = (ok, n, d, soft = false) => report(ok ? 'PASS' : soft ? 'WARN' : 'FAIL', n, d);

// Color maths: hex to linear sRGB, WCAG ratio, APCA Lc (apca-w3 0.1.9 constants).
const hexRgb = (h) => {
  h = h.replace('#', '');
  if (h.length === 3) h = [...h].map((c) => c + c).join('');
  return [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16) / 255);
};
const lin = (c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
const lum = (h) => { const [r, g, b] = hexRgb(h).map(lin); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const wcag = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };
const apca = (txt, bg) => {
  const y = (h) => { const [r, g, b] = hexRgb(h).map((c) => c ** 2.4); return 0.2126729 * r + 0.7151522 * g + 0.072175 * b; };
  const clamp = (v) => (v > 0.022 ? v : v + (0.022 - v) ** 1.414);
  const t = clamp(y(txt)), b = clamp(y(bg));
  const s = b > t ? (b ** 0.56 - t ** 0.57) * 1.14 : (b ** 0.65 - t ** 0.62) * 1.14;
  return Math.abs(s) < 0.1 ? 0 : Math.round((s > 0 ? s - 0.027 : s + 0.027) * 100);
};
const hueOf = (h) => {
  const [r, g, b] = hexRgb(h), mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn;
  if (!d) return { h: 0, s: 0, l: (mx + mn) / 2, c: 0 };
  const hh = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4;
  const l = (mx + mn) / 2;
  return { h: (hh * 60 + 360) % 360, s: d / (1 - Math.abs(2 * l - 1)), l, c: d };
};

// The measured tells (references/tells.md). A hit is a WARN: keep it only with a written reason.
const TELL_HEX = { '#6366F1': 'Tailwind indigo-500', '#8B5CF6': 'Tailwind violet-500', '#D97757': "Claude's terracotta", '#3B82F6': 'Tailwind blue-500' };
const TELL_FONTS = ['Inter', 'Geist', 'Space Grotesk', 'Roboto', 'DM Sans', 'Fraunces', 'Playfair', 'Instrument Serif'];
const near = (a, b) => hexRgb(a).reduce((s, v, i) => s + (v - hexRgb(b)[i]) ** 2, 0) ** 0.5 < 0.06;

if (mode === 'tokens') {
  const css = fs.readFileSync(target, 'utf8');
  const colors = Object.fromEntries([...css.matchAll(/--([\w-]+):\s*(#[0-9a-fA-F]{3,8})\b/g)].map((m) => [m[1], m[2].slice(0, 7)]));
  const fonts = [...css.matchAll(/--font[\w-]*:\s*([^;]+);/g)].map((m) => m[1]);
  check(Object.keys(colors).length > 0, 'color tokens found', `${Object.keys(colors).length} hex tokens`);

  for (const [name, hex] of Object.entries(colors)) {
    for (const [t, label] of Object.entries(TELL_HEX)) if (near(hex, t)) check(false, `tell: ${name}`, `${hex} is near ${label}`, true);
    const { h, s, l, c } = hueOf(hex);
    if (/accent|primary|brand/.test(name) && s > 0.35 && h >= 250 && h <= 300) check(false, `tell: ${name}`, `${hex} sits in the indigo-purple band`, true);
    if (/paper|bg|background|canvas/.test(name) && l > 0.9 && h >= 30 && h <= 60 && c > 0.03) check(false, `tell: ${name}`, `${hex} reads as cream; keep only with a reason`, true);
  }
  for (const f of fonts) for (const t of TELL_FONTS) if (new RegExp(`["']?${t}["']?\\s*(,|$)`).test(f.trim())) check(false, 'tell: font', `${t} in ${f.trim()}`, true);

  const pairs = (s) => (s ? s.split(',').map((p) => p.split(':')) : []);
  const text = pairs(opt('--pairs')), ui = pairs(opt('--ui'));
  if (!text.length) check(false, 'contrast pairs', 'pass --pairs ink:paper,... to gate text contrast', true);
  for (const [[fg, bg], floor] of [...text.map((p) => [p, 4.5]), ...ui.map((p) => [p, 3])]) {
    const [f, b] = [fg, bg].map((n) => colors[n] || colors[`color-${n}`]);
    if (!f || !b) { check(false, `contrast ${fg} on ${bg}`, 'token missing'); continue; }
    const r = wcag(f, b);
    check(r >= floor, `contrast ${fg} on ${bg}`, `${r.toFixed(2)}:1 (floor ${floor}), APCA Lc ${apca(f, b)}`);
  }
} else {
  // Resolve playwright from the working directory (the product repo), not from this script's folder.
  const req = createRequire(path.join(process.cwd(), 'noop.js'));
  let chromium;
  for (const m of ['playwright', '@playwright/test']) { try { ({ chromium } = req(m)); break; } catch {} }
  if (!chromium) { console.error('playwright not found from the working directory; run from the product repo'); process.exit(2); }
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});

  if (mode === 'page') {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
    await page.goto(/^https?:|^file:/.test(target) ? target : `file://${fs.realpathSync(target)}`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const faces = (opt('--fonts') || '').split(',').map((s) => s.trim()).filter(Boolean);
    const info = await page.evaluate((faces) => {
      const fams = new Set(), cols = new Set();
      for (const el of document.querySelectorAll('body *')) {
        if (![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
        const cs = getComputedStyle(el);
        fams.add(cs.fontFamily.split(',')[0].replace(/["']/g, '').trim());
        cols.add(cs.color);
      }
      return { fams: [...fams], cols: cols.size, loaded: faces.map((f) => [f, document.fonts.check(`16px "${f}"`)]) };
    }, faces);
    if (!faces.length) check(false, 'fonts loaded', 'pass --fonts "Display,Text" to assert the faces load', true);
    for (const [f, ok] of info.loaded) check(ok, `font loads: ${f}`, ok ? '' : 'fell back; the render is not the design');
    check(info.fams.length <= 3, 'font family count', info.fams.join(', '), true);
    for (const t of TELL_FONTS) if (info.fams.includes(t)) check(false, 'tell: font in use', t, true);
    check(info.cols <= 8, 'distinct text colors', `${info.cols}; more than the token set suggests a leak`, true);
    const out = opt('--out') || 'board.png';
    await page.screenshot({ path: out, fullPage: true });
    check(true, 'screenshot', out);
  }

  if (mode === 'mark') {
    const svg = fs.readFileSync(target, 'utf8');
    check(!/<text[\s>]/.test(svg), 'no live text', 'wordmarks are outlines, never <text>');
    check(!/<image[\s>]/.test(svg), 'no embedded raster');
    check(!/Gradient/.test(svg), 'no gradient', 'gradients go to mud at 16px', true);
    check(!/fill="#|fill:\s*#/.test(svg.replace(/<mask[\s\S]*?<\/mask>/g, '')), 'fill is currentColor', 'hex fills found outside masks', true);
    const mono = svg.replace(/(fill|stroke)="(?!none)[^"]*"/g, '$1="currentColor"');
    const cell = (s, bg, fg, src) => `<div style="display:flex;align-items:center;justify-content:center;width:${Math.max(s, 64) + 24}px;height:${Math.max(s, 64) + 24}px;background:${bg};color:${fg}">${src.replace('<svg', `<svg width="${s}" height="${s}" style="width:${s}px;height:${s}px"`)}</div>`;
    const row = (bg, fg, src) => `<div style="display:flex;gap:8px">${[16, 32, 64, 512].map((s) => cell(s, bg, fg, src)).join('')}</div>`;
    const html = `<body style="margin:16px;font:12px system-ui;display:grid;gap:8px">${row('#fff', '#111', svg)}${row('#111', '#f5f5f5', svg)}${row('#fff', '#111', mono)}</body>`;
    const page = await browser.newPage({ viewport: { width: 900, height: 600 }, deviceScaleFactor: 1 });
    await page.setContent(html);
    const out = opt('--out') || 'mark-strip.png';
    await page.screenshot({ path: out, fullPage: true });
    check(true, 'strip rendered', `${out}: read the 16 and 32 cells first; a blob there is a reject`);
  }
  await browser.close();
}

for (const r of results) console.log(`${r.status.padEnd(4)}  ${r.name}${r.detail ? `  (${r.detail})` : ''}`);
const fails = results.filter((r) => r.status === 'FAIL').length;
console.log(`\n${fails} FAIL, ${results.filter((r) => r.status === 'WARN').length} WARN`);
process.exit(fails ? 1 : 0);

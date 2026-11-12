# Polish and ship

The finish is about a dozen one-line details the tier sets and templates skip, all checked live in October 2026. `scripts/check.mjs` tests most of them; the rest are marked (by hand). General UI polish (press scale, concentric radius, `transition: all`) lives in better-ui, hit areas in better-accessibility; stress testing (long names, 200% zoom, non-Latin copy) lives in break-it.

- [The one-line details](#the-one-line-details)
- [Nav](#nav)
- [Buttons and links](#buttons-and-links)
- [Forms, pricing, FAQ, honest gaps](#forms-pricing-faq-honest-gaps)
- [Ship list](#ship-list)
- [Running the gate](#running-the-gate)

## The one-line details

- `::selection` in the brand color (Linear `lch(43 53 288)` with white text; Raycast `rgb(255,99,99)`).
- `:focus-visible` ring in the brand color, 1 to 3px, offset 2 to 4px (Stripe `3px solid rgba(84,82,251,.75)` offset 3px). Never the browser's default `auto` outline, never on `:focus` alone.
- Scrollbar: `scrollbar-width: thin; scrollbar-color: <alpha gray> transparent`; `scrollbar-gutter: stable` where overlays open.
- `color-scheme` on `<html>` so native controls and scrollbars match the theme.
- `text-wrap: balance` on headings, `pretty` on body.
- `overscroll-behavior: none` on body, so the rubber band doesn't flash white behind a dark page.
- `scroll-padding-top` equal to the header height, so anchor jumps clear it.
- Theme set by an inline script in `<head>` before paint (stored choice, then `prefers-color-scheme`), writing the class and `style.colorScheme`; `theme-color` meta per scheme with `media=`.
- Fonts self-hosted as woff2, only the above-the-fold files preloaded with `crossorigin`, and a metric-matched fallback face (`size-adjust`, `ascent-override`, `descent-override`; next/font generates it) so text doesn't jump on load.
- Hover-only effects wrapped in `@media (hover: hover)` so they don't stick on touch.

## Nav

- A full-width fixed or sticky bar, 56 to 76px, not a floating pill (none of the tier floats one). Sticky is a choice; Stripe's isn't.
- A real scrolled state: transparent to solid plus a hairline (Vercel adds `0 1px 0 rgba(255,255,255,.14)` after scrolling), or a permanent blur with a hairline (Linear, `blur(20px)` and 8% white). Detect it with a sentinel or `top: -1px` sticky and an IntersectionObserver.
- One primary CTA at the right end beside a quieter log in.
- Mega menus open on hover in 120 to 170ms from a `button[aria-expanded]` and close when the pointer leaves.
- Mobile menu: `role="dialog"`, body scroll locked, focus moved in, Escape closes, trigger `aria-expanded` and at least 42px square.
- A skip link as the first Tab stop, visible on focus.
- Right-click on the nav logo opens a small menu: copy the mark as SVG, copy the wordmark as SVG, download the brand assets (by hand; Interfere, Vercel). Keyboard users still reach the home link.

## Buttons and links

- 36 to 48px tall, 14px text, medium or semibold. One radius across the page, concentric inside pills.
- Hover changes background or border in 150 to 200ms; press scales to about 0.97 or shifts tone.
- Disabled is `aria-disabled` plus reduced opacity; loading holds the button's width (by hand).
- Copy-to-clipboard for install commands: an `aria-label`, the icon swaps to a check for about 1.5s, the label stays (by hand).

## Forms, pricing, FAQ, honest gaps

- Email capture: `autocomplete="email"`, `inputmode="email"`, `novalidate` on the form so the page's own messages show, validation on blur not on keystroke, a live region for messages. Submitting swaps the label and holds the width; success replaces the form inline and names the address; "already signed up" is a success variant, not an error; errors sit under the input in `role="alert"`. None of the tier has an email field on its homepage, so these are built from first principles.
- A form with no endpoint yet carries an empty `data-endpoint`, and submitting a valid address says "Nothing was sent: this form isn't connected yet." in the live region. It never prints a success state ("You're on the list") with no request behind it; the ship report names the endpoint it needs. (From Hallmark's `patterns.md`.)
- A fact nobody gave (a price, a date, a venue) is a slot, never an invented value: `<span class="fill" data-fill="price">Price to be announced</span>`, muted, inside a 1px dashed outline (`box-decoration-break: clone`) so it reads as a blank to fill, not a link or a selection. Two a page at most, the two a visitor needs to act, each named in the ship report. A row or line that would hold nothing but a missing fact is cut, not announced. (From Hallmark's `craft.md` §8.)
- Pricing toggle: `role="switch"` between monthly and annual, the saving on the annual label (Maze), the crossed-out monthly price inside each card (Melius), prices in `tabular-nums` so cards don't reflow.
- FAQ: native `<details>` or `button[aria-expanded]`; the chevron rotates rather than swaps.
- Cookie banner only when a tracker fires before consent; no tracker, no banner.

## Ship list

Table stakes: `<title>`, meta description, `og:title`, `og:image` at 1200x630 that fetches from an absolute URL, `twitter:card` `summary_large_image`, the X card previewed on the deploy (paste the URL into a draft post: image, title, nothing cropped through the headline; X caches cards, so add `?v=2` to see a change), svg favicon plus `apple-touch-icon`, `html[lang]`, one `h1`, alt on every image, semantic landmarks, a skip link, privacy and terms links in the footer, a branded 404 that returns status 404 (Linear's returns 200), no overflow at 320px, form validation, no dead links, a way back from every page, index or noindex as decided at intake. Lighthouse accessibility 95 or above.

Differentiators: everything in the one-line details, reduced motion that actually stops loops, a generated OG image, `theme-color` and favicon per scheme.

## Running the gate

From the product repo with Playwright installed, against the running page. Run the last pass on the production build (`next build && next start`, `vite build && vite preview`), not only the dev server: minifiers change what ships (one dropped a `backdrop-filter` the dev server showed; taste-skill). The script warns when it's looking at a dev server.

```
node ~/.claude/skills/landing-page/scripts/check.mjs http://localhost:3000/
```

It checks head and meta, the og:image (absolute, fetches, 1200x630, under 5 MB, not on localhost), the CSS details above (by parsing every stylesheet), `overflow-x: clip` rather than `hidden` or `100vw`, font preloads, the skip link and focus rings across ten Tab stops, the nav's scrolled state, sticky elements sliding under the nav, the animation count over a full scroll, LCP and whether its image is lazy-loaded, email forms, theme at first paint in both schemes, reduced motion (no infinite loops, no text left invisible), reveals with JavaScript off, the headline, lede, and CTA visible at 1280x800, overflow and button labels wrapping at every width from 320 to 1920, the container capped at 1920, words a phone never gets at 375, header targets and the mobile menu at 375, and the 404 status. Anything inside a `data-ui` root (the live product) is exempt from the page rules. Exit 0 is clean, 1 is a FAIL, 2 means a check couldn't run, which is a failure too, never a pass: fix the setup and rerun. WARN needs a fix or a reason. Add `--chromium <path>` if the installed browser build doesn't match Playwright's.

For performance on a preview deploy (local LCP means little): `npx lighthouse <url> --preset=desktop --output=json`, targets LCP 2.5s, CLS 0.1, INP 200ms at p75.

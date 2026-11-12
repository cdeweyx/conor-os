# Recipes per motion

Technique, library, code size, budget, and the review artifact for each motion that tends to earn its place on a data product. Default to the CSS version; reach for a library only when the row says so.

| Motion | Worth it when | Technique | Library | Size | Budget and reduced motion | Review artifact |
|---|---|---|---|---|---|---|
| Hero reveal | Every surface, once | Opacity plus translateY(8px), stagger 60ms in element order | CSS keyframes or WAAPI | 15 lines | Under 1s total; final frame under reduced motion | Four-frame strip |
| Chart or line draw-in | A line that means "in the order it happened" | `stroke-dasharray` and `stroke-dashoffset`, or Motion `pathLength` 0 to 1; 600 to 900ms ease-out; labels fade 150ms after | CSS or Motion `motion.path` | 15 lines | Runs once on first paint; static path after; final frame under reduced motion | Four frames: empty axes, 30%, 100%, labels landed |
| Number roll | Hero stats on entry and on change; never table cells | Digit roll, 500 to 700ms ease-out, tabular figures | NumberFlow (MIT, WAAPI, reduced-motion default); @kitlangton/rolling-number (MIT, no deps) when rolls must be interruptible on rapid re-runs | One component | Entry and value change only | Three frames: zeros, mid-roll, settled |
| Ticker or marquee | Breadth in fixed space | Duplicate the set (each with its trailing gap, so -50% is exactly one period), `translateX(-50%)`, linear, speed in px/s (about 30) so the loop follows the content; paused on hover, focus-within, hidden tab, offscreen, and a visible Pause inside the strip (hover alone doesn't meet WCAG 2.2.2); focus seeks the loop to the card instead of scrolling; hard clip unless the product allows gradients | CSS | 20 lines | Compositor-only; pause offscreen; single set and no motion under reduced motion | One still with the seam visible plus a 15s clip |
| Ambient backdrop drift | A generative field that should feel alive | Shader with slow speed, or a CSS mask sliding over a static SVG field; period 20s or longer, low amplitude | Paper Shaders, or CSS | One component | DPR cap 1.5; pause offscreen; one frame under reduced motion | Two stills (t=0, t=10s) plus a 10s clip; the drift must be invisible mid-sentence |
| Micro-feedback | Press, toggle, hover on interactive elements | Scale 0.96 to 0.98 on press, 120ms, ease-out | CSS | 5 lines | Interactive elements only | One before-and-after pair |
| Editor open (overlay anchored to a field) | A control opens from the thing that was clicked | Opacity plus scale 0.98 to 1 with transform-origin at the trigger, 200ms ease-out; exit 160ms | CSS or Motion AnimatePresence | 15 lines | Interruptible; final state under reduced motion | Three frames |
| State change (result updates) | A number or chart changes after a re-run | Number roll plus a 200ms crossfade of the chart; no re-draw-in | NumberFlow plus CSS | 20 lines | On change only | Three frames |
| Icon morph (menu to close, play to pause, sort direction) | A control whose two states are one glyph | morphicons `smooth` preset (stiffness 170, damping 26, no overshoot); set `reducedMotion="user"`, the default is never | morphicons (MIT, about 7KB, no deps) | One component | Interactive elements only; final glyph under reduced motion | One before-and-after pair |
| Section fade-ups, parallax, cursor trails, page transitions, spinners | Never on a data product | | | | | |

## Code shapes

Ticker (CSS):

```css
.track { display: flex; gap: 12px; width: max-content; animation: ticker 75s linear infinite; }
.track:hover, .track:focus-within { animation-play-state: paused; }
@keyframes ticker { to { transform: translateX(-50%); } }
.viewport { overflow: hidden; mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); }
@media (prefers-reduced-motion: reduce) { .track { animation: none; } .track > .dup { display: none; } }
```

Line draw-in (CSS):

```css
.hero-path { stroke-dasharray: var(--len); stroke-dashoffset: var(--len); animation: draw 800ms cubic-bezier(.2,.7,.2,1) forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) { .hero-path { animation: none; stroke-dashoffset: 0; } }
```

Set `--len` from `path.getTotalLength()` once, or use Motion's `pathLength` in React to skip the measurement.

Reveal (WAAPI, one function):

```js
const seq = [["h1", 0], [".helper", 60], [".input", 120], [".cta", 180]];
if (!matchMedia("(prefers-reduced-motion: reduce)").matches)
  seq.forEach(([sel, delay]) => document.querySelector(sel).animate(
    [{ opacity: 0, transform: "translateY(8px)" }, { opacity: 1, transform: "none" }],
    { duration: 200, delay, easing: "cubic-bezier(.2,.7,.2,1)", fill: "both" }));
```

## Library notes

- Motion (motion.dev): MIT core; `AnimatePresence`, layout animations, `pathLength`, springs. Motion+ is a one-time license for Ticker, AnimateNumber, and an AI kit; not needed for the recipes above.
- NumberFlow: dependency-free, WAAPI, respects reduced motion by default, about 2.5kb.
- morphicons: closed-form rotation between two paths, no Flubber; Motion can't morph paths on its own.
- Paper Shaders: `@paper-design/shaders-react`, Apache 2.0, hex-array colors, `speed` and `pause` props, the same shaders as the Paper canvas.
- GSAP is free for commercial use since 2025; use only for a timeline CSS can't express (rare on a data product).
- Lottie and Rive are for illustrated, stateful characters; wrong register here. Video loops read as stock on a data product.

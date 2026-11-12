# Type rendering

How text actually renders in the browser, which a canvas can't show. DESIGN.md decides the faces, sizes, and tracking. This covers what happens to them in code. Read it before writing the `ui/` spec, and on every polish pass. From jakubkrehel/skills `better-typography` (MIT).

## Wrapping

- `text-wrap: balance` for headings and short descriptions. Never on paragraphs, and Chromium ignores it past six lines.
- `text-wrap: pretty` on paragraphs, to keep a lone word off the last line.
- `overflow-wrap: break-word` wherever long words, URLs, or IDs can land.
- `white-space: nowrap` on labels and badges.
- Cap long-form text at 60 to 75 characters a line.

## Truncation

A truncated value needs a way back to the full text (a tooltip, a detail view, an expand). Without one it's a floor failure in build's `references/interface-floor.md`.

- One line: `overflow: hidden`, `text-overflow: ellipsis`, `white-space: nowrap`.
- Several lines: `display: -webkit-box`, `-webkit-box-orient: vertical`, `-webkit-line-clamp: 3`, `overflow: hidden`.

## Numbers

`font-variant-numeric: tabular-nums` on anything that changes or lines up: timers, counters, prices, table columns. Use the property rather than `font-feature-settings: "tnum"`, since properties keep working when a fallback face loads.

## Faces and weights

- Load every face the design uses. A browser synthesizes a weight or style the family doesn't ship, and the result distorts the face.
- `font-synthesis: none` only on a treatment you've checked across the fallback stack, never on body or interface text. Set the one unwanted longhand instead.
- Use `font-weight: 650`, not `font-variation-settings: "wght" 650`. Raw tags are for custom axes only.
- Leave `font-optical-sizing` at `auto`.
- A family's `Display` cut is for large sizes and its `Text` cut for small ones. Match the cut to the size.
- `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` go once, on the root, never per component.

## Small details

- **Buttons and badges:** `text-box: trim-both cap alphabetic` trims the space a font reserves above and below its letters, so text sits centered. It's a progressive enhancement.
- **Underlines:** `text-underline-position: from-font` and `text-decoration-thickness: from-font`. A dotted underline hints at a defined term.
- **Case:** store natural case and use `text-transform`, so copy and screen readers get the real words.
- **Punctuation:** curly quotes, en dashes in ranges, the `…` character, and `&nbsp;` in values like `10 km`. Code keeps straight quotes.
- **Selection:** `user-select: none` only on drag or gesture surfaces.
- **Decorative text:** CSS, not images, so it stays selectable.

## Inputs on iOS

iOS zooms when input text is under 16px. Either size up on mobile (`text-base sm:text-sm`) or keep `font-size: 16px` and render smaller with a transform on a transparent input, with a wrapper drawing the field. Pick one per product.

## Where our rules win

The source's numbers came in without these, because ours are measured or chosen:

- **Sizes:** it floors body at 16px, inputs and menus at 14px, and captions at 13px. DESIGN.md sets ours, including 13px tables and 12px meta.
- **Tracking and line height:** it keeps body at 0 and headings at -0.01 to -0.02em. DESIGN.md decides, and landing-page's `references/craft.md` holds the values measured from the tier.
- **Fallbacks:** its `system-ui` stacks are fallbacks only. Those faces stay on the deny list as design choices.
- **Em dashes:** it asks for them in rendered text. Product copy doesn't use them.

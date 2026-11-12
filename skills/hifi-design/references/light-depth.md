# Light depth

Read at the expressive-moments step. Contents: The three surface tones · Shadow-as-border and layered shadow stacks · Inset top highlight · Accent edge · Sunken well · Halo ring · What Paper drops · The don'ts · Expressive moments checklist

Depth and light on a light theme, rendered as stills on the Paper canvas. Every recipe here is inline CSS: flex, `box-shadow` (stacked, inset included), `color-mix`, layered `background` gradients, `border` with alpha. None needs `filter`, `backdrop-filter`, `mask`, or a pseudo-element. Token names follow the product's DESIGN.md; `--color-ink`, `--color-line`, `--color-accent`, and `--color-paper` below are placeholders for whatever it calls them. The recipes are written with `color-mix()`, but Paper drops it silently even though its guide documents it: on the canvas, compute each mix to a literal hex (rgba for alpha) and pixel-check the export. Build CSS keeps the `color-mix()`, with `in oklch` added.

The people who do light mode well say the same three things. Linear rebuilt its themes in LCH to "deal with different elevations for our surfaces (e.g. background, foreground, panels, dialogs, and modals)" and made light-mode neutrals darker, not lighter ([Linear, 2024](https://linear.app/now/how-we-redesigned-the-linear-ui)). Vercel's Geist is border-first, with real shadows "reserved for interactive states (like hover) or for elements that need to appear visually above the main content plane" ([Geist materials](https://vercel.com/geist/materials)). Comeau stacks shadows, keeps one light source, and tints them, because gray shadows look "washed-out" ([Designing Shadows](https://www.joshwcomeau.com/css/designing-shadows/)). Depth on light paper is surface steps plus a hairline plus one honest shadow on the thing that floats. Nothing glows.

## The three surface tones

Depth starts with tone, not shadow. Three fills: the page ground, a raised surface one step lighter, and a sunken tone one step darker, pre-blended at full opacity so it doesn't shift over whatever sits under it.

```css
background: var(--color-paper);   /* ground */          background: #FFFFFF;   /* raised: a card, a hovered row */
background: color-mix(var(--color-paper) 96%, var(--color-ink));   /* sunken: a well, an input, the nav */
```

Earns its place on every surface, before any other recipe; a selected or hovered row is a tone step to white plus an alpha hairline, no shadow. Don't add a fourth step. Past three the eye can't rank them and you're back to borders. Source: Linear's elevation model above and visual-assets' "depth by pre-blended lightness at full opacity" (visual-assets' `references/techniques.md`).

## Shadow-as-border and layered shadow stacks

Shadow-as-border replaces the hairline on the one card that's raised or active. better-ui's rule: "Shadows for elevation, borders for structure. Where a border exists only to create depth, prefer layered transparent `box-shadow` values. Keep borders that communicate structure or state." Its exact light-mode values, three layers, "The first acts as a 1px border ring, the second adds subtle lift, the third ambient depth" ([better-ui surfaces.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-ui/surfaces.md)):

```css
box-shadow: 0 0 0 1px oklch(0 0 0 / 0.06), 0 1px 2px -1px oklch(0 0 0 / 0.06), 0 2px 4px 0 oklch(0 0 0 / 0.04);            /* rest */
box-shadow: 0 0 0 1px oklch(0 0 0 / 0.08), 0 1px 2px -1px oklch(0 0 0 / 0.08), 0 2px 4px 0 oklch(0 0 0 / 0.06);            /* hover */
```

On a warm ground, swap the black for the ink so the shadow takes the surface's tint: `0 0 0 1px color-mix(var(--color-ink) 6%, transparent)` and so on down the stack. Vercel's raised card is the same shape, `0 0 0 1px #00000014` plus `0px 2px 2px #0000000a, 0px 8px 8px -8px #0000000a` ([design-bites, Vercel DESIGN.md](https://github.com/educlopez/design-bites/blob/main/design-mds/vercel.com/DESIGN.md)). Earns its place on the active or hovered card in a grid of hairlined ones, or a bordered button. Don't: "Never apply this to dividers" (better-ui), and never on every card; a shadow under everything is on the deny list and stays there.

The layered stack is for the one thing that floats: a popover, a menu, a dialog. Comeau's rules are that every shadow on the page shares one ratio, the vertical offset is about twice the horizontal, offset grows with blur, and the shadow is tinted toward the surface ([Designing Shadows](https://www.joshwcomeau.com/css/designing-shadows/); Looijesteijn, "the color of the shadow should be based on the color of the surface on which it's rendered", [Shadows have colors](https://www.kooslooijesteijn.net/blog/shadows-have-colors)). When the ink token is warm, the tint comes free.

```css
box-shadow: 0 1px 1px color-mix(var(--color-ink) 4%, transparent), 0 2px 2px color-mix(var(--color-ink) 4%, transparent), 0 4px 4px color-mix(var(--color-ink) 4%, transparent),
            0 8px 8px color-mix(var(--color-ink) 4%, transparent), 0 0 0 1px color-mix(var(--color-ink) 8%, transparent);
```

Earns its place on overlays only, which is DESIGN.md's elevation rule already. Don't: black at 0.2 with a 20px blur (the 2019 Material card), or blur with no offset. Run Comeau's [Shadow Palette Generator](https://www.joshwcomeau.com/css/introducing-shadow-palette-generator/) once with the product's ground color and paste the three results into DESIGN.md's elevation section.

## Inset top highlight and top-lit edge on filled controls

Light comes from above, so a filled control gets a 1px lighter edge at the top and its contact shadow below. apple-design writes the material form for a translucent bar as `border-top: 1px solid rgba(255, 255, 255, 0.4); /* bright top edge = light catching the material */` ([apple-design](https://raw.githubusercontent.com/emilkowalski/skills/main/skills/apple-design/SKILL.md)). On a flat button the inset shadow does the same job without changing the box; Refactoring UI's version of the rule is top lighter than bottom, shadow only below ([summary](https://www.sglavoie.com/posts/2023/09/09/book-summary-refactoring-ui/)).

```css
background: var(--color-accent); color: var(--color-paper);
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.18), 0 1px 2px color-mix(var(--color-ink) 12%, transparent);
```

An ink-filled chip takes the same at `0.12`. Earns its place on the one primary action on the page: the only filled control gets the only light. Don't put it on a paper-white surface (white on paper catches nothing), and don't let the inset grow past 1px or gain blur, which is a bevel and reads as 2010.

## Accent edge that fades to the surface

One edge lit from one side, for the card that's live. A solid accent `border-top` is a colored rail, which the deny list names; an accent that fades into the surface tone reads as light on an edge. Paint it with two background layers and a transparent border, the standard no-pseudo-element method ([Build UI](https://buildui.com/recipes/gradient-border), [CodyHouse](https://codyhouse.co/nuggets/css-gradient-borders)).

```css
border: 1px solid transparent;
background: linear-gradient(var(--color-paper), var(--color-paper)) padding-box, linear-gradient(180deg, color-mix(var(--color-accent) 45%, transparent), color-mix(var(--color-accent) 6%, transparent)) border-box;
```

Earns its place on the one live or selected card in a grid, one per view. Don't: a conic or hue-to-hue border (that's Border beam frozen mid-frame), or accent edges on more than one card. This is a named exception to the deny list's "gradients", so it goes on a duplicate and gets asked about, never woven in by default.

## Sunken well for a waiting element

An element that's waiting for content sits below the surface, not on it. Refactoring UI: an inset element gets its shadow at the top, since the light is above ([summary](https://www.sglavoie.com/posts/2023/09/09/book-summary-refactoring-ui/)).

```css
background: color-mix(var(--color-paper) 96%, var(--color-ink));
box-shadow: inset 0 1px 2px color-mix(var(--color-ink) 6%, transparent), inset 0 0 0 1px color-mix(var(--color-ink) 4%, transparent);
```

Earns its place on a content area while it loads, an input, a progress track, an empty slot; the skeleton inside it matches the final layout. Don't pair it with a matching light inset on the opposite edge. That pair is neumorphism.

## Halo ring on a live indicator

A status dot says "live" with a spread ring and no blur. It's a focus ring's geometry doing a status job, so it reads as system state rather than decoration.

```css
width: 6px; height: 6px; border-radius: 999px; background: var(--color-accent);
box-shadow: 0 0 0 3px color-mix(var(--color-accent) 14%, transparent);
```

Earns its place on one dot per card footer, or a selected row's marker. Don't add blur. A blurred halo is a glow, and glows are on the deny list for the reason Linear gives: "don't compete for attention you haven't earned" (motion-design's `references/inspiration.md`).

## What Paper drops

Paper renders inline CSS only. "Classes, style blocks, and pseudo-elements are dropped", and a dropped property comes back in `ignoredStyles` on the write response (`references/paper-loop.md`), so every recipe above is inline and none uses `::before` or `::after`. `filter`, `backdrop-filter`, `mask`, and SVG `feTurbulence` in a data URI are unverified and probably dropped; visual-assets already found Paper ignores SVG `clipPath` and `stroke-opacity`. The padding-box / border-box trick is plain CSS but untested on the canvas: write it once and read `ignoredStyles` before the screenshot. Anything that comes back in `ignoredStyles` gets a fallback (a solid pre-blended tint for glass, a 6% dot grid for grain) or leaves the strip.

## The don'ts

Each technique above has a 2019 version. The line between them is whether every value is a token or derived from one, and whether it's visible at a glance.

- Glow: a halo with blur, or a colored shadow larger than its element. The ring above is spread only. Paper's own guide says "Avoid outdated design trends from the late 2010s like excessive gradients and shadows".
- Glass: `backdrop-filter` plus a white-alpha fill. Paper can't render it, a still has nothing behind it to blur, and Superdesign's own caveat names "data-dense screens (tables and code develop blur halos; keep glass on chrome only)" and "flat, single-color backgrounds (blur has nothing to process)" ([Superdesign](https://www.superdesign.dev/styles/glassmorphism)). apple-design adds "Never stack a light translucent surface on another". Fake it with a solid pre-blended tint and an alpha hairline, or leave it out.
- Grain: SVG noise at 5% works on a dark marketing hero; on light paper anything past about 8% reads as a dirty screen, and Paper drops the filter anyway ([ibelick](https://ibelick.com/blog/create-grainy-backgrounds-with-css)). Never under a table or over text.
- Gradients on text: `background-clip: text` with a hue sweep is the deny list's "gradient text" and stays banned. The only gradients that survive are the accent edge above (one hue to transparent) and a 1 to 2% top-lit surface (`linear-gradient(180deg, #FFFFFF, var(--color-paper))` on a raised card), both proposed as named exceptions or not at all.
- Tinted image outlines: better-ui's rule is pure black at 0.1 on images, `outline: 1px solid oklch(0 0 0 / 0.1)`, "never a tinted neutral. A tinted outline picks up the surface underneath and reads as dirt" ([better-ui](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-ui/SKILL.md)).

## Expressive moments checklist

- Name two or three moments per surface that earn a treatment, and no more: a live indicator, an upload in progress, a loading state, the primary action, a selected or hovered row, a stale banner. The rest of the surface stays as it is.
- One technique per moment. Never two on one element or on neighbors; Libraries.dev's rule holds for stills too: "never two effects on the same element or on elements right next to each other" ([libraries-dev](https://raw.githubusercontent.com/Jakubantalik/Libraries.dev/main/skills/libraries-dev/SKILL.md)).
- Every value is a token or derived from one: a `color-mix` in build CSS, its literal hex on the canvas. No hex that isn't a token or a mix of tokens.
- Each moment is one still on a duplicate beside the base, at its settled frame, with the assumption it tests in the layer name. Read `ignoredStyles` and pixel-check the export for the fill you meant.
- Nothing the deny list names unless the still proposes a named exception. A 1px accent edge is one; a glow isn't.
- Present the strip as a decision, not a gallery: one line per still with a recommendation and a second pick, and say which stills change the base and which only change a state, or the user won't know what he's being asked.
- The user picks per moment. A pick is woven into the base, its recipe goes into DESIGN.md's elevation section with its don't, and the choice goes into `references/preferences.md` so the next surface starts from it. A moment left plain is recorded too.
- Whether a picked moment also moves is motion-design's call at the prototype. The still fixes the settled frame.

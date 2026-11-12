# Levers and plumbing

How a brand gets into a working product without hurting it, and how it rides on tokens. Sources: Linear's 2024 and 2026 redesign write-ups, Radix Colors, Stripe's accessible color post, Rauno Freiberg, Family, Raycast, Wise and Ragged Edge.

## Levers, by weight

Spend on the top four first. In a data-dense app the brand is mostly here, not in color.

| Lever | Weight | What to decide |
|---|---|---|
| Neutral tint and warmth | High | The gray's hue and chroma. Linear's 2026 refresh mostly changed its gray (cool to warm), with the warning that too warm "looks muddy". Pair the gray's hue with the accent's; keep app grounds low chroma, lower in dark mode. |
| Numerals | High for data | `lining-nums tabular-nums`, slashed zero where the face has it, the minus sign, how a signed number looks. A column that doesn't align is a fail. |
| Typeface and a display cut | High | One family for the app, a display cut or second face for headings only (Linear: Inter Display for headings). Stylistic sets as a token so they're one edit. |
| Accent reach | High | A written list of where the accent may appear (primary action, one chart mark, focus ring). Everything else is gray. Accent text is marketing, not app. |
| Icons | Medium | One set, shared corner radius, no tinted icon tiles. Stroke matches the text beside it in rendered pixels: 1.5px next to 400, 2px next to 500 to 600, 2.5px next to 700 (Lucide's `absoluteStrokeWidth`, or `vector-effect: non-scaling-stroke`, since a 24-grid icon at 16px otherwise paints 2 as 1.33). Use the set's 16, 20, or 24 grid that matches the render size; a 24 drawing scaled to 16 lands off the pixel grid and goes soft. (From jakubkrehel better-ui `icons.md`.) |
| Radius, dividers, focus ring | Medium | The radius scale as personality; divider contrast; focus ring as a box-shadow that follows radius. |
| Density and chrome | Medium | How much chrome recedes; the sidebar dimmer than content. |
| One signature interaction | Medium | One named moment that carries the brand; motion removed from anything used hundreds of times a day. |
| Chart tone | Medium | Mark weight, the one highlighted series, gridline contrast, label face. dataviz rules still hold. |
| Voice in microcopy | Low to medium | Empty states, errors, confirmations. Clear before clever. |
| Sound and haptics | Low | At most one, named (Family has one sound in the whole app). |

## Token plumbing

- **Three tiers.** Core (raw values, ramps), semantic (jobs: background, border, text-1, text-2, accent, positive), component (only where a component truly differs). A rebrand edits core and a few semantic aliases. It never touches component usage or layout.
- **Generate ramps, don't hand-pick them.** Linear generates every theme from three inputs (base, accent, contrast) in LCH, replacing 98 hand-set variables. Build ramps in OKLCH so equal lightness looks equally light; store hex, since canvases and renderers take hex.
- **Contrast is a property of the ramp.** Stripe's rule: every hue follows one lightness curve, so any two colors five steps apart pass small text and four apart pass icons. Radix guarantees its steps 11 and 12 at APCA Lc 60 and 90 over step 2. Check WCAG 4.5:1 text and 3:1 UI as the floor; report APCA beside it.
- **Tools.** Leonardo (`@adobe/leonardo-contrast-colors`, `formula: 'wcag3'` for APCA) builds ramps for both modes from one key set. Rampa CLI for a single hue. Huemint for palette seeds only (non-commercial). Palette from a reference image: k-means in OKLab, never raw RGB.

## Change and leave alone

Write both lists before the swap.
- **Change:** values behind tokens, type and its features, icon set rules, radius scale, divider contrast, empty-state and error copy, one signature interaction, the mark and wordmark.
- **Leave:** layout, navigation, component APIs, chart form, where any number sits, what any number says.

## Testing the swap

- A flag or toggle that flips old and new tokens in one click on the running app.
- Name the stress views up front: the densest table, the chart page, an empty state, an error, the front door. Check each in light and dark.
- Screenshot every surface per mode before and after through the project's existing baselines; accept changed ones by name with a reason.
- Theme switches never animate.

## Type facts that bite

- Judge type only on a rendered page after `document.fonts.check` passes; a fallback looks like a decision.
- Judge a candidate face by what its cuts say: sharp cuts read techy and unapproachable, round forms read friendly and can date it. The character has to match the brand and stay out of the way: a loud brand wants a quieter face, and a minimal brand needs the face to do more. Set it in the wordmark and one composition before the pick (Primary Studio's brand sprint).
- Fontshare's FFL v2.0 (August 2026) allows self-hosting and trademarked wordmarks, and bans subsetting, format conversion, and glyph edits. Wordmark outlines in an SVG are fine; a tweaked font file isn't.
- OFL fonts allow modification, but a Reserved Font Name forces a rename of any rebuilt font.
- Paid foundries (Pangram Pangram, Klim) are a user call with a per-domain or pageview license.

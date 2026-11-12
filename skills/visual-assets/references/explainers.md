# Explainer diagrams and the SVG part contract

How-it-works visuals: a concept or an object drawn as separate parts, with markup that keeps each part editable. Condensed from jakubkrehel/skills `teardown`; its mesh pipeline and viewer are for hardware and stay out. Read this when the visual's job is to explain, not to set a mood.

## Explainer diagrams

- **One part per idea.** A concept with no physical form (how a sync works, what a score is built from, the layers of a screen) becomes a stack of thin plates, one per idea, exploded along one axis so each lifts off the one below. Leave about a tenth of a plate's thickness between layers; faces that share a plane fight and break both lines and fills.
- **Color only where it carries meaning.** Default to one ink plus the accent on the part the explainer is about; a part gets a hue of its own only when it's a different kind of thing and the hue is the point (red, green, and blue subpixels). Hierarchy comes from line width before opacity.
- **The assembled view is one toggle away**, from the same source and the same camera. Zero explosion rebuilds the assembly; if it doesn't, a part is misplaced.
- **The smallest set of views that answers the question.** An exploded view for how parts fit, a section for an inside passage, one pictorial view for a shape.
- **Label invented construction as concept.** For a real object, the evidence ledger from the frame step decides what's drawn.

## The SVG part contract

- One `<g id data-item data-name>` per part with a `<title>`, so a part can be selected, recolored, hidden, or labeled without touching its paths.
- Every path carries `data-line-role` (`outline`, `edge`, `detail`, `texture`, `axis`), and widths are set once per role in a `<style>`, never per path. A weight change is one edit.
- Fills sit in their own group, apart from the linework. `fill="none"` on every open path, or a bent leader closes into a black triangle.
- No nested scale transforms: they multiply stroke widths along with the geometry. Generate coordinates in final units; to inset a view smaller, divide its stroke widths by the scale.
- Self-contained: styles inside the SVG, fonts embedded as woff2 data URLs, no linked images or remote fonts.
- Print export: `px = mm / 25.4 x dpi` (A3 landscape at 300 dpi is 4961 by 3508).

## The technical stroke preset

A fourth preset beside the field, envelope, and hero weights in `techniques.md`: **outline 4 : edge 2.5 : detail 1.5 : texture 1**, with `axis` at detail weight, dashed, butt caps (round caps would close the dashes). Round caps and joins everywhere else. Teardown's values on paper are 0.35, 0.22, 0.13, and 0.09mm. One hue per part, and a part's fill is an 18% tint of its own line color (each channel `255 - (255 - c) x 0.18`), so fill and line always agree.

The mechanical checks for any SVG are in `scorecard.md`.

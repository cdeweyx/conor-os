# Techniques by visual type

Rules an agent can apply, condensed from the design research. Numbers are starting points; the research lane for a specific visual may refine them.

## Contents

1. Generative fields
2. Contour maps and dot fields
3. Illustration
4. Objects and collages
5. Texture and atmosphere
6. Raster pipeline
7. Type as the visual
8. What the premium sites actually ship
9. Custom glyphs

Explainer diagrams, the SVG part contract, and the technical stroke preset are in `explainers.md`.

## 1. Generative fields (random walks, flow fields)

- Generate, don't draw. Seeded numpy or plain-Python walks; the seed is part of the asset.
- Simplify then smooth: Ramer-Douglas-Peucker at about 0.5 to 1.5px, then Catmull-Rom to cubic Bezier so every point stays on the line. One path per walk, coordinates rounded to integers or one decimal. Chaikin is the cheap alternative.
- Three weights, no more: field 0.6px, envelope 0.8px, hero 2px. The hero at three times the field reads as intent; 1.5 times reads as noise. Round caps and joins.
- Depth by pre-blended lightness at full opacity. Blend three grays against the ground (on #FBFAF7: #ECEAE4, #DEDBD3, #CFCBC1) and assign by rank. Stacked transparency makes false darker colors at every crossing.
- Taper only the hero: a filled polygon from a width profile, or three stroked segments of rising width when a polygon is too heavy.
- One terminal marker: a dot with a ground-colored ring on the hero tip, a hairline baseline, nothing on field lines.
- Structure plus randomness: two faint envelope curves at plus and minus k times sqrt(t) frame the band (Hobbs).
- Density and edge: 24 to 36 walks, start 10% past the artboard edge, cap the fan angle so the band stays a band.
- Reserve the text zone by masking, not fading. Paper Desktop ignores SVG clipPath and stroke-opacity, so bend the walks away from the form zone in the generator (scale the overshoot above a guard line to a quarter); dropping segments or laying a ground-colored rectangle over the field both show as a hard cut and a box behind the input. On the web, a clipPath with an even-odd path works.
- Twenty seeds, pick one. The hero should leave the band cleanly with air around its exit: cut it at a `tip_x` about 100px short of the edge instead of letting it run off. Smooth the hero with Chaikin twice and draw it as a polyline; cubic control points on already-smoothed points produce cusps at tight turns.
- A scorecard line can lose to the user's pick. When the field weight the user chose on the canvas is under the 1px floor, keep the pick and log the miss as deliberate in the hand-back note.
- Flow fields (Hobbs): grid at 0.5% of width, extend 50% past the canvas, Perlin angles or quantized to multiples of pi/4 for a sculpted look, minimum distance between curves; short curves read as fur, long as fluid. https://www.tylerxhobbs.com/words/flow-fields
- Python: opensimplex or noise for fields, shapely.simplify for RDP, drawsvg for emission (svgwrite is unmaintained), vpype linesimplify and linemerge as a post-pass. `scripts/linefield.py` shows the walk version with no dependencies.

## 2. Contour maps and dot fields

- Contours: a noise grid, then skimage.measure.find_contours at 8 to 12 levels, each contour one polyline. Topographic at a few KB. One contour in the accent, the rest in the line gray. Label one value in the product's units. https://scikit-image.org/docs/stable/auto_examples/edges/plot_contours.html
- Dot fields: a grid of circles with radius or presence driven by noise or distance from a focus; or real data points (every order as a dot, columns by month) with a handful in the positive color. Compact SVG: one path of `M x y h0.01` segments with round caps.
- Halftone: same grid, radius from a source image's luminance. https://github.com/abhishek-sehgal954/SVG_Digital_Halftoning

## 3. Illustration

- Primitives, not paths: circles, rects, ellipses, polygons, short paths. Dense coordinate data fails in every model. https://chat2svg.github.io/
- Three named groups (background, midground, foreground), five hues max, opacity variants before new colors, one stroke width. https://0xdoublemoon.github.io/tools/2026/06/04/svg-skills.html
- Palette as role slots: each part takes a role (main, highlight, tint, positive, alert, deep), never a hex, and the roles map to DESIGN.md tokens, so a brand swap repaints a whole set in one edit (from kelvinkn17 fun-isometric).
- Render, look, critique, revise, with a stop. The agentic-pelican lesson: know when to stop adding detail.
- People and hands: don't draw them. Open Peeps, Open Doodles, Humaaans (all CC0) recolored to ink and accent; unDraw sparingly (softer, SaaS-looking). Lucide at 96 to 240px for big iconography.
- Line-drawn objects (a field, a course map, a scorecard): single-weight line, one accent, the domain's own drawing tradition. The Masters course map is the benchmark.
- Cartoon figures read low-brow. If the brief wants a character, source it.

## 4. Objects and collages (tickets, stubs, cards)

- Real content: the product's actual items, names, dates. Fake content reads as a template.
- Ticket silhouette as one SVG path (notches included) plus one dashed line for the perforation. CSS masks work on the web; on the canvas use the path.
- Tilt sparingly (2 to 7 degrees), never every item the same way, never a shadow stack.
- Monospace and middle-dot meta strings are template chrome now; a ticket has to earn monospace through the receipt metaphor, and probably shouldn't.

## 5. Texture and atmosphere

- Paper Shaders (@paper-design/shaders-react, Apache 2.0, zero deps): mesh gradient, grain gradient, paper texture, dots, halftone, dithering. Hex-array colors, tuned on the Paper canvas and shipped as props. Texture, not hero. https://github.com/paper-design/shaders
- Grain: feTurbulence at 3 to 6% opacity on the web; test once on the canvas and fall back to a 6% dot grid if filters don't render.
- Lit grain: feTurbulence plus feSpecularLighting gives paper with a light on it. Tune it on fffuel's nnnoise (output free for commercial use), export the SVG, and move the parameters into the script.
- Gradients are on the deny list for a reason. One intense color moment beats five.

## 6. Raster pipeline (only when approved)

- Style anchor: one fixed paragraph reused verbatim (FIXED: ground hex, accent hex, linework, one light source; FLUID: the subject). Models can't invent and remember at once.
- Palette lock: FLUX.2 binds hex codes and takes a JSON palette field; Ideogram 4 has a first-class palette parameter; Recraft palettes enforce. Everything else: generate near-monochrome and recolor.
- Recolor: `magick in.png -colorspace gray +level-colors "#1C1B18","#FBFAF7" out.png` for a duotone onto paper; `magick in.png -remap palette.png out.png` for a hard snap.
- Negative constraints: state the positive invariant ("flat matte surfaces") rather than naming what you don't want; naming it puts it in the image.
- References: index them and say what each does ("style of image 1, object from image 2"); three to five refs, weighted.
- Upscaling: Topaz or Real-ESRGAN at 2x and stop. Magnific adds pores and texture, which is the slop.
- Alpha: native from Recraft, Ideogram's API, GPT Image; otherwise render on white and on black and recover alpha from the pair.
- Vectorize only flat art: Recraft native SVG, then Vectorizer.ai, then vtracer locally.
- Ten candidates, a vision critique pass, regenerate the losers. Script over MCP so the anchor and palette live in version control.
- Asset gate for generated raster (from Appllama's image-assets): an icon set or any repeated element is one sheet from one prompt, then sliced, so the set shares a style. Check every edge at 400% for halos and matte fringes. On a two-theme product, generate theme twins or place the asset on a surface that doesn't change with the theme. App icon at 1024, no alpha, no rounded corners (the OS masks it), judged at 60px; a concept that dies small gets simplified.

## 7. Type as the visual

- The question or headline at display size (48 to 64px), tight leading, one accent word at most.
- A cycling line of real examples under the field beats an illustration for a monochrome product.
- Custom or lesser-known faces are the differentiator; Inter and Geist signal that nobody chose. Velvetyne (OFL, credit the designer) has the experimental display faces for this; never as the UI family.

## 8. What the premium sites actually ship

Stripe's hero is a WebGL shader over 150 inline SVGs. Vercel stacks six layers, vector first paint, shader last. Linear has 219 SVGs and no canvas; depth from a surface ladder and hairlines. Nobody ships a pure generative SVG hero. The premium feel is a small vector layer under CSS with strict weight and lightness discipline, one confident decorative move, and typography doing the heavy lifting. https://rauno.me/craft/vercel

Explainer diagrams, the SVG part contract, and the technical stroke preset are in `explainers.md`.

## 9. Custom glyphs: construct, render, check

Professionals construct line icons from numbers, not freehand: a keyline grid, a centered stroke, padding, radius by element size, a minimum gap tested with a rolling circle, one cap and join style, a blur test against a reference circle (Lucide, Octicons, Material, Phosphor, IBM, Atlassian guides). An agent typing path coordinates from memory drifts off grid, leaves tangents, and mixes stroke weights; the fix is mechanical, not taste.

Recipe, when nothing exists to source:
1. One-line brief naming one object cue and one state cue ("soufflé; it fell in the middle").
2. Pull proportions from a real reference (a photo, a rulebook diagram, a sourced icon's geometry). Tracing (potrace, vtracer) and generative vector give filled silhouettes, never centerline strokes; take proportions only.
3. Construct in a script (drawsvg, MIT) from named anchors on a 4px grid using lines, rects, circles, and computed arcs inside one keyshape, at a fixed 1.5px round-capped stroke. Spot glyphs at 140px run 1.2% stroke to height (illustration weight); icons run 6 to 9%.
4. Render with resvg (MIT) at 1x and 50% beside a reference circle. Gaps stay at 6px or more so the 50% render survives.
5. Check: reads at 50%, stroke count under twelve, one hue, one cue that names the object, no tangents, consistent stroke, optically centered, balanced negative space, no scene. Adjust anchors until it passes; three passes, then stop.
6. Family-check against the product's existing glyphs; keep the script as the source and name the layer with it.

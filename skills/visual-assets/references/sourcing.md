# Sourcing: models, open sets, servers, licenses

Facts rot; check the link before relying on a price or a plan. Ranked for a palette-locked, monochrome-plus-accent product.

## Vector, in order of preference

1. Your own Python (walks, fields, contours, halftone) emitting compact SVG. Exact hex, deterministic seeds, edits in code. The only route that holds a strict palette and data-shaped structure at once.
2. The agent writing SVG directly, for composition, placement, masks, labels. Not for thirty smooth paths.
3. Recraft V4.1 Vector: true SVG, palette controls, a line-art substyle, V4 Styles from one to ten references. Paid plan assigns copyright; the free tier is non-commercial. Illustration bias, excess anchor points. Remote MCP at https://mcp.recraft.ai/mcp (OAuth), about $0.08 per vector image. Use for an illustration spot, never for a data-shaped backdrop.
4. Quiver Arrow 2.0 (powers Paper's SVG generation): SVG-native, no documented palette lock or license terms.
5. Adobe Firefly Text to Vector: editable SVG, indemnified, Illustrator-bound, illustration bias.

## Raster, when approved

- FLUX.2 (pro, flex, klein): documented hex binding and a JSON palette field, 4MP, open weights for klein. Best for palette-locked abstract heroes. Built into Paper. https://docs.bfl.ai/guides/prompting_guide_flux2
- Nano Banana 2 and Pro (Gemini image models): best value, conversational edits, 4K, three style refs; no transparent output. Nano Banana Pro is built into Paper.
- GPT Image 2.5: best editing and text, transparent output, obedient to strict prompts, glossy by default. Around $0.05 per medium image.
- Ideogram 4.0: first-class palette parameter (16 hex), best typography; open weights are non-commercial.
- Seedream 5.0 Pro: layered transparent PNG output for compositing.
- Midjourney V8.2: still the aesthetic leader, style references lock a look; no API and automation is banned, so hand-run only.
- Cheapest via API: FLUX.2 klein, then Recraft Utility, then Seedream Lite. Best license: Adobe Firefly (indemnified), then the OpenAI API.
- Paper's built-in generation (Pro plan) covers Flux 2, Nano Banana Pro, OpenAI Image Edit, Seedream, Recraft V4.1, and Quiver; it counts against the user's usage, so it stays off until they say on.

## Icons and glyphs

- Iconify aggregates about 200 sets behind one API; search it first: `https://api.iconify.design/search?query=<object>&limit=64`, fetch `https://api.iconify.design/<prefix>/<name>.svg`. When it rate-limits (it does), fall back to the jsDelivr `@iconify-json/<prefix>` package. `scripts/fetch-glyph.py search <q>` and `fetch-glyph.py get <prefix:name> --height 140 --stroke 1.75` do both, write a `.raw.svg` and a tokenized copy with `stroke="var(--color-control, #8E8A81)"`.
- Only stroke-based sets survive scaling to a 140px glyph: Lucide and Lucide Lab (ISC), Tabler (MIT), Hugeicons free (MIT), Iconoir (MIT), Mingcute, IconMind. Re-weight with `stroke-width = target_px * grid / height` (0.3 on a 24 grid for 1.75px at 140). The `?width=` parameter alone leaves the stroke at 2 grid units, an 11px cartoon line.
- Baked outlines (Phosphor, Material Symbols, MDI, Font Awesome, game-icons, Streamline Freehand) can't be re-weighted: use them at 32px or retrace the proportions.
- License tiers: ISC, MIT, Apache, CC0 need nothing. CC BY (Streamline free, game-icons, Solar, Font Awesome free, Flaticon) needs one visible credit line. CC BY-SA (OpenMoji) and non-commercial free tiers (Noun Project, Absurd, Storyset) are out. Keep an ATTRIBUTIONS.md beside the assets, written when the asset is pulled.

## Open illustration sets that recolor to tokens

- Open Peeps and Open Doodles: CC0, black-and-white hand-drawn, modular. Best style match for a monochrome product. https://www.openpeeps.com/ , https://www.opendoodles.com/about
- Humaaans: CC0, flat two-tone layered figures. https://www.humaaans.com/
- unDraw: free, recolor allowed, softer SaaS look; sparingly. https://undraw.co/license
- Lucide (ISC) and Phosphor (MIT): icons at 96 to 240px for big iconography; Phosphor at one weight reads more chosen than Lucide.
- Skip Absurd Design and Streamline Free (attribution required on free tiers).

## Open-collection pictures (from taste-skill `references/imagery.md`)

When a visual needs a real picture the product doesn't have (its place, old maps, materials, the trade's history, museum objects), search the open collections, under the raster rule: off until the user says on.
- Openverse (one index over Flickr, Wikimedia Commons, museums, and libraries), Wikimedia Commons (archival photos, old maps, scans of prints), the Art Institute of Chicago and the Met (public-domain works, open APIs).
- Commercial-use licenses only: CC0, public domain, CC BY. CC BY-SA is out, since our recoloring makes a derivative. Write source, creator, license, and page into ATTRIBUTIONS.md when it's pulled, and credit it in the footer.
- Search the inventory, not the category, in the place's own words: "azulejo", not "blue tile"; "ghent postcard", not "city".
- A found picture is never the client's own. It can show the city, the materials, the history; it never stands in for the product, a room, a person, or the team, and its caption never ties it to them.
- Twice the shown width for anything full-bleed; recolor through the raster pipeline's duotone.

## MCP servers and skills worth having

- Recraft remote MCP for vector spots; fal.ai MCP for everything else through one key (FLUX, Recraft, Ideogram, video, 3D). Skip Midjourney bridges (ToS), svgo and ImageMagick MCPs (Bash does it).
- Prompting references: replicate/skills prompt-images (Apache 2.0) is the best general image-prompting doc; wuyoscar/GPT-Image2-Skill has 163 gallery prompts including data visualization and brand systems.
- 3D only if a product needs it: Spline V2 with its MCP and pre-rendered WebP, blender-mcp as the free route. Not for a data tool.

## Front-door materials

Logos (svgl), background removal (remove.bg), gradient libraries, AI stock, and mockup tools are in the design-sources skill under Materials.

## Licensing rules of thumb

- Prompt-only output isn't registrable in the US; compositing and editing strengthens the claim.
- Free tiers of generators usually forbid commercial use or keep the copyright (Recraft, Unicorn Studio).
- Check the LICENSE file of any vendored skill or asset before copying; several popular design skills ship without one.

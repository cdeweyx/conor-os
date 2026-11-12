# Craft: layout, type, surfaces, imagery

Values measured from the live CSS and markup of Linear, Vercel, Stripe, Raycast, Resend, Clerk, and Framer in October 2026. They're ranges the tier sits in, not a house style; DESIGN.md decides inside them. Arc is gone (a farewell page) and isn't a reference anymore.

- [Hero](#hero)
- [Type system](#type-system)
- [Layout and rhythm](#layout-and-rhythm)
- [Surfaces](#surfaces)
- [Product shots](#product-shots)
- [Bento and feature sections](#bento-and-feature-sections)
- [Video, logos, testimonials, OG](#video-logos-testimonials-og)
- [Pipelines](#pipelines)
- [What to steal](#what-to-steal)

## Hero

- Layout: pick before writing copy. Split (text left, product right), product-first (short headline, the product directly below), or type-only (left-aligned, full-bleed visual below). Five of seven tier sites left-align the headline on desktop. Centered with a badge is the fallback, not the default.
- Headline: 56 to 72px desktop, 36 to 40px mobile; line-height 1.0 to 1.1; tracking -0.02em at 48px, -0.03em at 64px, down to -0.06em only on tight grotesks (Vercel); weight 450 to 600 (700 only with -0.035em or tighter); `text-wrap: balance`; measure about 16 to 36ch; two lines.
- Character budget: characters per line ≈ line width ÷ (font size × 0.5) for most grotesks and serifs at display size (0.4 condensed, 0.58 wide or caps). A 44px headline in a 350px phone column holds about 16 a line, so about 32 characters (four to six words) survives two lines everywhere; up to 42 if the phone size drops to the mid-30s. Write the copy deck to the budget and move the rest into the subhead. Never fix a long headline only by shrinking it: five words at 64px beat nine at 28px. (From taste-skill's `copy.md`.)
- Subhead: 18 to 20px, line-height about 1.4, -0.01em, max 600 to 640px, muted.
- CTAs: primary filled plus a ghost or plain-link secondary, under three words each. Proof (a stat, a logo row, a named quote) within 48px of them.
- Text gradient on the headline is off by default; it suits a serif or a dark hero (Resend's white to 50% white).
- Kill test for the hero visual: delete every decorative node, line, dot, glow, and gradient in your head. If what's left still says the idea, the concept is real; if it's a headline on an empty ground, the visual was wallpaper. (From LangChain's design-agent.)

## Type system

- A grotesk plus a mono is the floor; a display face (a serif or a pixel face used only above 48px) is how the differentiators stand out (Resend's Domaine, Raycast's Instrument Serif, Vercel's Geist Pixel). Three families at most, each with one job.
- Inter is fine when tuned: Linear runs InterVariable at weights 510, 590, 680 with per-step tracking; Raycast turns on `ss02`, `ss08`. Inter at default settings and weight 700 is the tell, not Inter.
- Every step of the scale declares size, line-height, tracking, and weight; nobody in the tier uses a framework's default scale. Body 15 to 16px at -0.011em; small 13 to 14px at -0.013em; an eyebrow, where one earns its place, 12 to 13px mono or caps at +0.04 to +0.08em.
- Tabular figures on every number that changes or lines up (Clerk ships a separate numbers face; Linear sets the slashed zero).
- Variable fonts let weights sit between steps (450, 510); that's part of the finish.

## Layout and rhythm

- Three container widths: a reading column (600 to 640px), a product column (960 to 1024px), a full container (1200 to 1280px). Adjacent sections differ in width or alignment; two card grids never sit back to back.
- Section padding from 64, 96, 128, 160px; the hero and final CTA get the most.
- Density varies on purpose: a dense bento after an airy statement, a hairline-divided list after a grid.
- A statement section is optional: 48 to 72px, weight 300 to 500, asymmetric (Instrument's oversized gray serif beside two small columns). No per-word scroll animation on it.
- Opening a section: a tracked label above every heading is the tell; ask what the reader doesn't know yet. If nothing, open with nothing. Twelve ways in, one per section (two can share; three is noise): nothing, air above and the heading flush; the heading announces itself in its first two words (usually best); a lead-in in a heavier weight inside the first paragraph; a drop cap, once a page; a rule that does more than rule (hairline, color edge, pure gap), one divider language varied seam to seam; a numeral at graphic scale, once a page, only when the number is real and is the point; a real `<ol>` when the sequence is genuine; a caption below the content instead of a label above; marginalia beside the body; a change of paper, the band's edge as the break; a running head that persists at the page edge; a heading that stays in view while its content scrolls. An eyebrow is fine when it names something present (a plan name, a `<time>`, a real filename), not a name for what comes next. (From Hallmark's `craft.md` §7.)

## Surfaces

- Hairlines are alpha, not gray hex: `rgba(255,255,255,.06)` to `.12` on dark (Raycast `#ffffff0f`), `rgba(0,0,0,.06)` to `.1` on light. One-sided dividers are fine.
- Gradients are monochrome fades of the surface or glows under 20% opacity (Linear's CSS has 74 radial gradients, Clerk's 219). The tell is a saturated two-hue blob behind centered text, not gradients as such.
- Depth comes from layered low-alpha shadows (Clerk, below) and tone steps, not one heavy drop shadow.
- Glass and noise are differentiators used once, not defaults.

## Product shots

- Order of preference: the product rebuilt as live markup (Linear's hero has no `<img>`; real issue IDs and statuses are in the HTML), then a cropped real screenshot, then a stylized abstraction. Never a full app window in a browser or laptop frame.
- Crop to one task, 600 to 720px wide, no window chrome, states frozen (one hover, one selection).
- Fade the crop into the card: `mask-image: linear-gradient(45deg, #000 50%, transparent 100%)` (Resend). Mask in CSS, not in the file, so light and dark reuse one asset.
- Clerk's shadow stack, each layer the same color `rgb(19 19 22 / .025)`: `0 0 0 1px, 0 1px 1px -.5px, 0 3px 3px -1.5px, 0 6px 6px -3px, 0 12px 12px -6px, 0 24px 24px -12px`. Radius in percent so it scales with the image.
- No tilt on the hero shot; a secondary card can tilt under 6 degrees on one axis.
- Ship light and dark variants and toggle by theme class (Vercel).
- Raster: WebP at q90 to 95 with 1x and 2x `srcset`, AVIF for glows (Clerk's bento glow is 22.7 KB), `loading="lazy" decoding="async"` below the fold, `fetchpriority="high"` on a hero image.

## Bento and feature sections

- A bento earns its place when tile size encodes priority: one lead tile at twice the width holding a real crop, two to five supporting tiles, each with a miniature UI drawing in one stroke color (Attio), one glow behind the whole grid. Equal tiles of icon plus sentence is the generic version.
- At least one feature section isn't a card grid: a numbered mono-eyebrow list with no icons (Lemon Squeezy), or hairline rows with a small image left and text right (Square).
- Photography only for a physical product or a people-led brand, and then lit, not stock. Developer tools in the tier ship none.

## Video, logos, testimonials, OG

- Video: `autoplay loop muted playsinline preload="none" poster`, WebM then MP4, 5 to 10 seconds, under 500 KB in a card, under 4 MB in a hero; poster only under reduced motion. Encode: `ffmpeg -i in.mov -b:v 0 -crf 25 -vcodec libx264 -pix_fmt yuv420p out.mp4`.
- Hero video: the page background equals the footage's edge color, so it needs no overlay and never flashes. Check frames at 0, 50, and 100%: the text zone is empty in all three, and the loop seam is invisible. Against a white flash, set `html, body { background }` as the first CSS rule and fade the video in on `loadeddata`. Re-aim `object-position` on mobile or move the video below the copy; `max-height` breakpoints (850, 720px) keep a one-screen hero whole on short laptops. Fix a busy text zone with `object-position` or a new clip, never a dark wash. (From MotionSites' `assets.md` and `craft.md`.)
- Logos: monochrome SVG from svgl (`https://api.svgl.app?search=<name>`), `fill="currentColor"`, 24 to 32px tall, six to eight in a static row. Check each brand's usage terms; svgl carries none.
- Testimonials: a real face, name, role, and company on every one, or don't ship it.
- OG image: generated from the hero's fragment at 1200x630 with `ImageResponse` (Next's `opengraph-image` or a route like Linear's `/api/og?title=`), with a committed static fallback.

## Pipelines

Live-markup hero (the default):
1. Pick the one screen that proves the headline and write its data as a fixture (real names, real numbers, from the product's seed; break-it's Demo fixture works).
2. Build it as a component with the product's own tokens, 720px max, no chrome, states frozen, by the loop in `product-ui.md` (copy the closest gold, budget the words, poster frame first, compare).
3. Shadow stack and percentage radius; one glow or shader behind it through visual-assets.
4. Theme both variants; screenshot at 1x and 2x to check.

Real screenshot, when the screen can't be rebuilt:
1. Seed the app with the fixture.
2. `page.locator('[data-shot=hero]').screenshot()` at `deviceScaleFactor: 2`, cursor and scrollbars hidden by an injected stylesheet.
3. Crop and export with sharp (WebP q90 plus AVIF), write the `srcset`.
4. Commit the fixture and the script so the shot regenerates when the UI changes.

Run `npx playwright install chromium` first if Playwright complains about a browser build mismatch.

## What to steal

- linear.app: the type scale (title steps 17 to 72px, -0.012em under 24px and -0.022em above, body 15px/1.6), the hero as live DOM, the dynamic OG route.
- vercel.com: the heading tracking table (-0.06em at every step from 40 to 72px) at weight 450; paired light and dark hero images.
- stripe.com: the light-weight hero (300 to 400) at line-height 1.03 and `max-width: 36ch`; the hero sized in `lvh` to fit the fold.
- resend.com: serif display over a sans body; the 45-degree mask fade on cropped shots; sub-500 KB 3D loops with posters.
- clerk.com: the six-layer shadow stack; a live component as the hero; one AVIF glow behind the bento.
- raycast.com: the responsive hero (36, 48, 64px with max-width 440 to 540px) and the translucent card borders.
- Mobbin sections worth opening: Antimetal's type-only hero with the editor beneath, ElevenLabs developers' left eyebrow and full-bleed visual, Lemon Squeezy's numbered feature list, FLORA's lead-tile bento, Cursor's testimonial wall.

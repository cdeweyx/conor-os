# Product UI on the page

How to build the product as interface for the hero, a feature card, or a bento tile: what fails, and the loop that fixes it. The method is Stageshow's (github.com/benjitaylor/skills, Benji Taylor, MIT). It ships a React kit, gold examples, and film scripts; clone it into a scratch folder and copy from it, since its examples are the bar, not inspiration. `craft.md` holds the measured values (crop, mask, shadow stack) and the fixture pipeline; this is the method on top.

## Five ways it fails

- **Too much.** Real text at full weight in every row, numbers everywhere, every pixel packed. The more detail, the more it looks generated.
- **Wireframe.** Two gray blobs and a button: built too small, or stripped of what made the product recognizable.
- **Boxed.** A whole window shrunk into a card with even margins. A screenshot pasted in, not a product shot.
- **Flat.** Every object the same weight in the same bordered card, so the eye has nowhere to land.
- **Bland.** A gray window with a cursor whatever the idea was. The page's idea and the product's own look are the point.

The fix for all five: a full, structured screen in quiet tones, real words only on what the claim is about, room to breathe, and a crop that puts the eye on the story. Simplify the words, not the context.

## The loop

1. **Size it at the width it's shown.** About 720x340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400x300 for a card, viewed at 1:1. A demo never goes under about 320 wide. Anything that sits in a phone column gets a second design at 358, cropped closer with the action and result kept whole, not the wide one squeezed. Small formats crop harder: a 400px card holds a third of a dashboard at full size, not all of it at a third.
2. **Copy the closest gold example.** Stageshow's `examples/` has a gold table in its SKILL.md; pick by need (`static-card` for a still card, `dark-hero` and `hero-demo` for heroes, `bento` and `dark-bento` for grids, `chart-scrub`, `table-edit`, `ai-chat`, `form-error`, `loading` for one interaction). Copy its structure (stage size, crop and bleed, row and type sizes, spacing), then swap in the product's tokens, icons, chrome, and words. A copy that only changes the name isn't done. Don't rewrite from a glance; the gold's proportions are what you can't eyeball.
3. **Spend the words.** Count the real strings: the title, the thing acted on, what's typed, the result, usually 3 to 7. Everything else is quiet filler (bars of varying width, 60, 45, 70, 52). A word budget isn't an element budget: a calendar still needs a populated week. Filler sits at the edges; bars where the eye lands read unfinished, which is the gray-bar fake UI the rubric caps. The hero's live product is the exception to filler: every visible row holds the fixture's real content, since at hero scale it's the proof, but only the claim's strings sit at full weight and the rest stay quiet, which is how it avoids Too much.
4. **Frame it.** One gutter, a full one or well past it. Only filler bleeds; actions read whole or not at all. The page is the ground: no plate behind the window on a white or dark page, and never a window whole with air on four sides. The window fills at least two thirds of the stage and runs off an edge. One number gets to be big; the heaviest marks sit on what the claim is about. No dead corners, no empty band mid-window while the result is pushed into the crop.
5. **Set the poster frame first.** Most people see one frame: the still, the thumbnail, the reduced-motion state. It's the beat that tells the story alone, never one caught mid-change, with the result left on screen. In the still build that frame is the whole job; motion-design animates it later, if at all.
6. **Film it and compare.** Screenshot it at the shown width and at 390, beside the gold's at the same size. If yours is emptier, flatter, or more boxed, that's the first fix, before any motion. Ask what the eye lands on first and whether it's the result. When it animates, Stageshow's `scripts/film.mjs` makes a contact sheet of the loop (copy `scripts/` beside the kit and install `playwright-core`; read them before running). Fix the largest fault first: framing, then hierarchy, then motion, then polish.

## Faults that come back

- Gray bars where the eye lands; filler belongs at the edges.
- A plate behind the window, or a window floating with air on four sides.
- Empty bands, controls cut by the crop, shadows clipped.
- Stock AI marks and made-up logos: sparkles, purple, a letter in a colored square.
- Busy rows and uneven insets: words under 8px from a card's edge (12px is right).
- Content that swaps instead of moving, and a loop that resets with no cause.
- A control that looks live and isn't: an input that takes focus but not typing. Wire it to the fixture, or set it as a still with no focus, caret, or pointer cursor.

Mark the fragment's root with `data-ui` and write its CSS under `[data-ui]`, so `check.mjs` holds the page around it to the page rules and leaves the product's own radii, borders, and labels alone. It's for cropped fragments only, never a heading or a whole section.

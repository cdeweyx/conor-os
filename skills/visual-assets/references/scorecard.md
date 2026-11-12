# Scorecard for a decorative visual

## Mechanical checks, before the score

Run these on every exported SVG first; a fail is a defect to fix, not a judgment (from jakubkrehel teardown's `verification.md`).
- Parse it as XML. Fail on duplicate ids, a `url(#...)` that resolves to nothing, invalid numbers, and any external asset (a linked image, a remote font).
- Crop the densest junction at 4x and look: faceting, doubled edges, lines running through solid faces, leaders ending in empty space.
- For an exploded explainer, a part that shows under half its own linework is hidden behind another; change its path or the camera.

## The score

Score a 2x screenshot on each line, yes or no. Fix the noes, re-render, score again. Three passes, then pick. Anything still failing after three is a direction problem, not a polish problem.

1. Says one thing. A viewer can name what the visual means in five words (proof, breadth, the domain, the data, the payoff). If it needs a caption to mean anything, it's decoration.
2. Speaks the product's vocabulary. The forms, objects, or numbers come from the product or its domain, not from a generic aesthetic family.
3. The job of the screen still wins. Eyes land on the question, the input, or the number first; the visual reads second. Cover the visual with your hand and the screen still works.
4. One confident move. A single decorative decision (a field, a strip, a drawing), not a scene. Two moves need a reason; three is noise.
5. Weight discipline. At most three line weights, the hero at about three times the field, round caps and joins, nothing hairline-thin at 1x.
6. Lightness, not opacity. Depth comes from pre-blended tones at full opacity; no crossing is darker than the darkest tone.
7. Structure plus randomness. The eye can find an axis, an envelope, a baseline, or a grid under the variation.
8. Negative space is a shape. The empty area around the form is deliberate, and the visual never fades to nothing under text; it's clipped or ends.
9. Every color is a token. No hex the system doesn't know; the accent appears once with a job (the hero, the marker), never as a wash.
10. None of the tells. No gradient wash, glow, glass, 3D blob, identical card row, ALL-CAPS eyebrow, middle-dot meta, appended arrow, stock face, text or interface inside a generated image, or a generated device that isn't a real one. Cream plus serif plus terracotta counts.

Bonus, for generated visuals: the seed was chosen from twenty, and the exit of the hero (or the focal element) has air around it.

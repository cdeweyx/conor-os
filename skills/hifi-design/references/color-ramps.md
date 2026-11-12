# Color ramps

better-colors' rules for building and using a color system, with where each one extends or contradicts the DESIGN.md template's rules (design in monochrome; hue only for sign, action, and the one highlighted mark; grays derived in OKLCH with a measured contrast ratio beside each step). Source: [better-colors SKILL.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/SKILL.md) and its references, linked per rule.

## Ramp shape

"A system is ramps, not colors." One neutral ramp, one accent ramp, "and only the status ramps the product actually renders. A `warning` ramp nothing imports is maintenance for zero pixels." Every step has a job: "Do not generate a step no role consumes." ([SKILL.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/SKILL.md))

A well-formed ramp has four properties ([palette-generation.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/palette-generation.md)):

- "Steps step evenly in *perceived* lightness, not in whatever the format calls lightness."
- "Hue is constant end to end."
- "Vividness peaks in the middle and falls off at both ends."
- "Steps are denser at the light end. Light backgrounds need finer distinctions than dark ones. Keep `50` to `200` close together and `800` to `950` further apart."

Both ends "stop short of pure black and white, which cannot carry hue at all." Never compute a ramp by eye; culori, colorjs.io, or chroma.js interpolate in a perceptual space and emit the project's notation. "Neutrals carry the most roles, so they need the most steps. Never generate fewer neutral steps than accent steps." ([palette-structure.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/palette-structure.md))

Against DESIGN.md: agrees on OKLCH derivation and one job per step (paper, line, ink-3, ink-2, ink). It extends it in one place. DESIGN.md says "even lightness steps"; better-colors says the light end is denser, because that's where surfaces live. The three surface tones in `light-depth.md` (ground, raised, sunken) sit within a few percent of lightness while the text steps sit far apart, so the ramp is dense at the top and sparse below. Write it that way in the Ramps section rather than as one even scale.

## Gradient interpolation

"The space is a look, not a correctness setting." For a ramp the space isn't a choice: "the steps have to land evenly in perceived lightness and sRGB interpolation produces muddy mid-steps." For a decorative gradient ([color-usage.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/color-usage.md)):

- "`in oklab` is the best default: even brightness, no hue surprises."
- "`in oklch` travels around the hue wheel rather than through the middle, staying vivid and sweeping every hue between the stops. Reach for it when a two-hue gradient goes gray in the middle."
- "The sRGB default darkens and mutes the midpoint. It is what most interfaces already have, because it is what you get without asking."

Against DESIGN.md: gradients are on the deny list, so this rule reaches only two places. The accent edge in `light-depth.md` is one hue to transparent, and a dataviz sequential or diverging palette is a ramp, so both take a perceptual space and never the sRGB default. Write `in oklab` (or `in oklch` for a single hue) on any gradient that survives, and never a two-hue sweep, which oklch would route through hues nobody asked for.

## Tinted neutrals

"A pure gray ramp is a perfectly good default." Tinting it "is a stylistic option, not a correction. A trace of the accent, a few percent of its vividness, puts the grays in the same family as the accent rather than merely coexisting with it. Enough to measure, not enough to name." "Warm neutrals, hue toward orange, read approachable and editorial; cool ones, toward blue, read technical and precise. Whichever you pick, including none, hold it across the whole ramp. A warm gray border on a cool gray background is visible even when neither color is nameable alone." ([palette-structure.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/palette-structure.md))

Against DESIGN.md: DESIGN.md is stricter. Its grays sit at 3 to 6% saturation in one hue family, and "pure grays read unfinished" is a check in `checks.md`, so the tint isn't optional here. The one contradiction is the accent: better-colors tints toward the accent hue, while the taste interview picks warm or cool grays on their own, so warm grays can sit under a cool blue accent. That's a taste call already made; keep it, and keep the whole ramp in the same family. The exception both agree on is images: better-ui's outline is pure black at 0.1, never a tinted neutral.

## Semantic color derivation

"Name primitives by hue, semantics by role." Primitives (`--blue-500`) "are never applied in a component"; semantic tokens (`--color-text-secondary`) "name a job, point at a primitive and are the only tier components reference." "Use a token only in its role. Never borrow a token because its value is right today." "One color, one meaning": anything within 15° of hue is the same color, and "if the accent means interactive, that hue on static text tells users to click something that is not clickable." "Fill exactly one action per view... Put the color on the background, not the label." "Keep every status hue distinct from the accent." ([SKILL.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/SKILL.md), [palette-structure.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/palette-structure.md))

Against DESIGN.md: agrees on one filled action per view and on status hues (the template defines none; lifecycle is shape plus word in gray, and green and red carry sign only). It extends the token layer: DESIGN.md's tokens are already role-named (ink, ink-2, line, accent), but the Paper canvas holds them as one flat tier. Add the primitive tier only if a second theme ever ships. The one tension is "one color, one meaning": the accent here is the primary action and also the one highlighted mark on a chart, which better-colors would read as a static mark asking to be clicked. DESIGN.md decided it (the mark is paired with a word and an outline), so record it as a known exception rather than fixing it.

## What to avoid

From the Before-you-finish table ([SKILL.md](https://raw.githubusercontent.com/jakubkrehel/skills/main/skills/better-colors/SKILL.md)), the rows that bite a light monochrome system:

- "Ramp built by varying HSL lightness" → "Rebuild against perceived lightness with a constant hue."
- "Ramp spaced evenly across the full range" → "Tighten the light end until `50` and `100` read as two surfaces."
- "Same saturation number reused across hues" → "Match the proportion of each hue's own maximum, not the raw value." Sign colors (positive, negative) and the accent each get their own vividness, matched by proportion.
- "Contrast fixed by changing hue" → "Change lightness, the channel contrast responds to."
- "An isolated `oklch()` value dropped into a hex codebase" → keep one notation. DESIGN.md stores hex derived in OKLCH; the canvas tokens stay hex and `color-mix` runs off them.
- "Semantic token used outside its role (separator as text)" → add a token for the missing role. `--line` is a hairline, never a text color, even at the meta size.
- "Never report a contrast value you did not measure." Agrees with DESIGN.md's ratio beside each step and hifi-design's a11y MCP check on every text-on-background pair; a failing pair is reported and left for the user, not repainted.

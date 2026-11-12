# DESIGN.md template

Read before the taste interview. Contents: Taste interview · Drafting notes · The template (front matter, Overview, Colors, Typography, Layout, Elevation and Depth, Shapes, Components, Do's and Don'ts, Charts, States)

A specimen page example is in `specimen-example.html`: one HTML file, tokens as CSS variables, the sections in the order of the DESIGN.md. Copy it, swap the tokens and the real copy, render it, open it.

About fifty lines. Fill every value; a blank line is a default the agent will supply. Paste it into the first prompt and upload it as the design system. Tokens live here; a CSS variables file is generated from them, never hand-edited.

The shape follows the open DESIGN.md spec (google-labs-code/design.md, Apache-2.0): YAML front matter for the tokens, the known sections in its order, then our own. Consumers keep sections they don't know, so Charts and States ride along, and `npx @google/design.md lint` checks contrast on the component pairs and flags tokens nothing uses. Run it beside the specimen; at a brand pass, `diff` v0 against v1.

A value nobody has decided yet is written as `OPEN: <the question>`, never a placeholder. An agent copies a placeholder into the product and the guess becomes the design; an `OPEN` it has to ask about.

Two rules for writing rules. A rule is observable or it isn't a rule ("table numbers are right-aligned in tabular figures", not "tables feel tidy"). When rules conflict, the order is: supplied facts, locked structure, contrast floors, tokens, taste.

## Taste interview

One question at a time, before drafting anything: the mechanics of a design system come from research and the wireframes, but taste has to come from the user.

1. Two words for how it should feel and two for what it must not. Never clean, modern, sleek, minimal, or premium, which describe every template.
2. The world it belongs to: the place or material it would sit near (instruments on a night shift, a ledger). It tints the grays, picks the accent, and feeds any visual.
3. One signature detail only this product would have, used the same way everywhere.
4. One product they'd want it mistaken for, and the single trait to take. When they name it, read its Refero style page for trait candidates and its Similar Brands, then confirm the one trait; that file informs the interview and never reaches the build agent.
5. Warm or cool grays.
6. An accent hue they'd accept on every primary action, or "you pick".
7. A typeface they already like, or "you pick from the shortlist".
8. Anything they never want to see beyond the standard deny list.

## Drafting notes

- **What it's drafted from:** the taste interview's answers, the product doc's tone, the converged wireframes' density and hierarchy, and this template. Four to six colors with one job each, a gray ramp with contrast floors, one typeface with a size scale and three weights, tabular figures on every column, density in numbers, three spacing values and one radius, the grammar's layer stack (each layer's shadow, hairline, and spring, so height reads the same everywhere), what earns a border, chart mark rules, state rules, and a deny list.
- **Every token carries its rule and its don't.** Tokens without rationale get the right colors and the wrong decisions.
- **The gray ramp comes from Ramps** (ramps.studio, free, an API an agent can call): an OKLCH neutral ramp with the measured contrast ratio on every step. Take the neutrals and the ratios and discard its status ramps. Hex stays the stored value, since the canvas, the recolor commands, and the renderers all take hex. `color-ramps.md` holds the ramp rules.
- **Color has jobs, not moods.** Design in monochrome and let hue in only for sign, action, or data, always paired with a non-color cue. Green and red carry sign only, never lifecycle, errors, or emphasis; the accent is for action and the one highlighted mark. Graded states are a diverging scale with gray at the middle, and uncertainty fades toward gray instead of changing hue.
- **One typeface, not the defaults** (Inter, Roboto, Geist, Space Grotesk, Instrument Serif are all tells now), with tabular figures and a distinct 1, l, and I. Prove it before compiling tokens: drop the font file on Wakamai Fondue and read tabular figures, the weights, and the 1, l, I glyphs off the report. The Typography section names a shortlist with the license trap per source.
- **The specimen** renders the real tokens in both themes: swatches with hex and contrast, the graded scale, the type scale with real copy, a table at the density rule, a card, controls, each chart form drawn in the palette, the states.
- **Brand v0.** Form (a chart, a field, a strip of the product's own objects) is product vocabulary and survives a rebrand; a brand pass changes the values behind the tokens and the canvas re-renders.

## The template

```markdown
---
version: alpha
name: <product>
description: <one line: what it is and who reads it>
colors:               # dark, the default theme; light reuses every name with its own value (Colors)
  paper: "#______"
  ink: "#______"
  ink-2: "#______"
  ink-3: "#______"
  line: "#______"
  control: "#______"
  accent: "#______"
  positive: "#______"
  negative: "#______"
typography:            # one level per size in the scale; every level names the family, size, weight, line height, and tnum
  meta:      { fontFamily: <family>, fontSize: 12px, fontWeight: 400, lineHeight: 1.5, fontFeature: "'tnum'" }
  table:     { fontFamily: <family>, fontSize: 13px, fontWeight: 400, lineHeight: 1.5, fontFeature: "'tnum'" }
  body:      { fontFamily: <family>, fontSize: 14px, fontWeight: 400, lineHeight: 1.5, fontFeature: "'tnum'" }
  section-title: { fontFamily: <family>, fontSize: 16px, fontWeight: 600, lineHeight: 1.3 }
  lead:      { fontFamily: <family>, fontSize: 20px, fontWeight: 500, lineHeight: 1.3, fontFeature: "'tnum'" }
  hero-number: { fontFamily: <family>, fontSize: 28px, fontWeight: 500, lineHeight: 1.1, fontFeature: "'pnum'" }
spacing: { sm: 8px, md: 16px, lg: 32px, section: 48px, row: 32px, cell-y: 6px, cell-x: 12px }
rounded: { control: 3px, card: 3px, overlay: 6px, full: 9999px }
components:            # token references only; the lint checks contrast on each backgroundColor and textColor pair
  table-row:      { height: "{spacing.row}", typography: "{typography.table}", textColor: "{colors.ink}", backgroundColor: "{colors.paper}" }
  card:           { backgroundColor: "{colors.paper}", textColor: "{colors.ink}", rounded: "{rounded.card}", padding: "{spacing.md}" }
  input:          { backgroundColor: "{colors.paper}", textColor: "{colors.ink}", rounded: "{rounded.control}", padding: "{spacing.cell-y}" }
  button-primary: { backgroundColor: "{colors.accent}", textColor: "{colors.paper}", rounded: "{rounded.control}", padding: "{spacing.cell-y}" }
  overlay:        { backgroundColor: "{colors.paper}", textColor: "{colors.ink}", rounded: "{rounded.overlay}", padding: "{spacing.md}" }
---

# DESIGN.md: <product> (v1, dark and light)

## Overview
Not in v1, on purpose: breakpoints, motion (added at build handoff). Say what's out so no agent fills it; the spec's `omitted` key only takes its own section names.
Tone: <two sentences: what it is, what it isn't. Open on the data; there is no hero.> Feel: <two concrete words; never clean, modern, sleek, minimal, or premium>.
World: <the place or material it belongs to>. It tints the gray ramp, picks the accent, and feeds any visual; surfaces stay near neutral on a working screen.
Signature: <one detail only this product would have>, used the same way everywhere it appears and nowhere else.
Terminology: <the words the surface uses, verbatim from Solution Details: the object's name, its states, each metric's name>. One word per thing, everywhere.

## Colors (each value has one job; nothing else gets color; each job holds a dark and a light value)
--paper    #______  page and panel ground: black in dark, near-white in light, never a brand color
--ink      #______  primary text, table numbers, the primary data line
--ink-2    #______  secondary text, labels (>= 6:1)
--ink-3    #______  meta, timestamps, axis text (>= 4.5:1, the floor; never lighter for text)
--line     #______  hairlines: table rows, card edges, gridlines
--control  #______  input and control borders (>= 3:1)
--accent   #______  primary action and the one highlighted mark per chart. Never a background, never a border, never decoration, never a sign.
--positive #______  the positive pole only: a gain, a win, a bar above zero. Always with a sign, shape, or word.
--negative #______  the negative pole only: a loss, a bar below zero. Never for errors.
Ramp derived in OKLCH at even lightness steps (Ramps), one per theme; hex is the stored value, repeated here so the prose reads without the front matter, with the measured ratio beside each step in both themes.
Semantic: disabled is --ink-3 text with no border change; selected is --ink text plus a 1px --control border; positive and negative values carry the sign and the word.
Graded states = diverging: negative, negative 40%, ink-3, positive 40%, positive. Always with the word and a count beside it.
Lifecycle states = shape + word in gray. No hue.
Uncertain marks fade toward gray (40% alpha) rather than changing hue. Green and red carry sign only (a signed number, a win or a loss, a bar above or below zero), never lifecycle, errors, or emphasis. No amber warnings.

## Typography
Family: <one family with tabular figures and a distinct 1, l, I, proven in Wakamai Fondue>. Substitute: <named fallback>. Mono only for identifiers, if at all.
Shortlist and the trap per source: Untitled Sans (Klim; tabular in all styles; a web app needs the App license, priced by MAU, test fonts free for mockups). Public Sans and IBM Plex Sans (OFL, tabular). Switzer or Supreme (Fontshare; free commercial, no subsetting or conversion). Satoshi and General Sans don't list tabular figures.
Weights: 400, 500, 600 only.
Sizes: 12 meta / 13 table / 14 body (1.5) / 16 section title (600) / 20 lead sentence (500, 1.3) / 28 hero number (500).
font-variant-numeric: tabular-nums on every column and every updating number; proportional on the hero number.
Sentence case everywhere. Numbers right-aligned, headers aligned like their column.

## Layout
Table rows 32px, cell padding 6px 12px (16px at row ends), 13px text in --ink.
Horizontal hairlines only. No zebra, no vertical rules, no borders around tables.
Density comes from row height and padding, never from smaller or lighter text.
Spacing: 8 / 16 / 32. More space around a group than inside it. No one-off margins. Max line 60ch.

## Elevation and Depth
The layer stack, copied from the grammar; a thing is only as high as it is temporary.
ground: the page. No shadow, no hairline.
card: rests on the ground. No shadow at rest; hairline only when selected.
panel: anchored to an edge, one at a time. --shadow-panel, hairline at ink 8%.
popover: grows from its trigger, seconds long. --shadow-overlay (two layers, low alpha), semi-transparent border.
dialog: blocks, one decision. --shadow-overlay over --scrim.
A border is earned by: a table row, an input, a selected card, an overlay. Nothing else.

## Shapes
Radius: 3px controls and cards, 6px overlays, full on dots. Concentric when nested.

## Components
Only what exists; a documented variant nobody built gets used anyway. Each entry: when to use it and when to reach for something else, one bad use from the product's own code (plus the default variant when it has several), then every state it has (rest, hover, pressed, focus, disabled, loading, empty, error).
Blocks (a card plus its rows, a panel, a hero) are derived from built screens after the fact, once a part has been rebuilt on two screens, never designed up front. Once two exist, add a `## Blocks` section: each block named with its file, the components it's made of and its states, and each surface written as a stack of named blocks. The two-copy test is tech-planning's `libraries.md`. The section is for whoever writes the brief; the brief's line naming the block's file is what an implementer follows.
table-row: 32px, --line hairline below, numbers right-aligned tabular, comparison in the same cell group. Use for any list a user compares down a column; not for one object's details.
card: --paper, 3px, border only when selected, one link, the whole card clickable. Use for an object opened from a collection; not for a single fact. States: rest, hover, selected, thin.
input: --control border, 3px, accepts every common form of the value.
button-primary: --accent fill, --paper text, sentence case, says what happens.
overlay: 6px, two-layer shadow, semi-transparent border, grows from its trigger.

## Do's and Don'ts
Do: design in monochrome and let hue in for sign, action, or data only. Pair every color with a word or a shape. Put the decisive number first and its comparison beside it. Say stale and thin in words.
Don't: Inter, Roboto, Arial, Geist, Space Grotesk, Instrument Serif. Gradients, glows, glass, colored rails, icon tiles,
emoji, sparkles, eyebrows, ALL-CAPS labels, badges without a state machine, cards in cards, red/green for anything but sign,
hero sections, three-card rows, bento grids, cream + serif + terracotta, near-black + neon.
Don't compensate with a sterile anti-design template either; distinctiveness comes from the subject.

## Charts
Lines 2px, markers 8px, bars <= 24px with rounded data-ends and 2px gaps. No gridlines beyond the zero or reference hairline.
One accent per chart on exactly one mark. Bands very light, no stroked edge, no mean line, labeled once in words.
Text never wears a series color. Sparklines under 2px; below ~20 points, countable marks instead of a line.

## States
Empty: a small glyph in the product's own vocabulary (line-drawn, one hue, on a ground line), one sentence naming the cause in --ink-2, one accent link, centered as a block. Thin: outline marks, "Not enough yet", what's missing.
Callouts: one pattern, placed directly under the page's title block: a --line fill, a 14px icon, one sentence. Info is a circle-i with --ink-2 text; warning is a yield triangle with --ink text at 500; stale adds a Refresh link. Never a hue, never two stacked.
Loading: a skeleton in the final layout, or nothing under 400ms. Stale: "as of" moves to the top, marks drop to 40%. Error: ink sentence, bold lead, retry link. No amber.
```

Add a `## Motion` section at build handoff, from `final-and-handoff.md`'s default motion block. Leave for a brand skill: wordmark, illustration, the final typeface if it changes, voice beyond the tone line.

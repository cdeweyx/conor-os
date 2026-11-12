# Hi-fi constraints

Read end to end before every surface's token plan, so the user never has to say these. Revision checks are in `checks.md`; the cases and sources behind the rules are in `learnings.md`.

Contents: Deny · AI-look clusters · Data surfaces · Copy and controls · Cards and lists

## Deny (paste into the brief and the design system, with the clusters below)

Inter, Roboto, Arial, system sans, Geist, Space Grotesk, Instrument Serif, IBM Plex Mono with Archivo (the vibe-coded dashboard pairing); italic or colored single words in headings; purple or indigo anywhere; gradients, gradient text, glows, blobs, glass, grid backgrounds, colored side rails; one radius on everything; a soft shadow under every element; cards inside cards; three-card rows; bento; eyebrows, kickers, overlines; ALL-CAPS labels; arrows on links; 01/02/03 markers on non-sequences; emoji or sparkle icons; status pills without a state model; repeated metric boxes; invented or uncheckable stats, claims, or copy ("loved by 10,000+ teams", "10x faster"); greeting headlines ("Welcome back"; the title names the page or the period); hype words (supercharge, seamless, unlock, magic, revolutionize, game-changing, AI-powered); fade-up on every section; hover effects on non-interactive elements; transition: all; dark mode with no light theme; neon accents; rainbow chart palettes; page-load animation.

## AI-look clusters

Generated design lands in one of five looks. Each is a default rather than a choice, so it needs a reason from the subject; the collision test checks the plan against them and critics name the cluster a screen falls into.

1. A warm cream ground (near #F4F1EA), a high-contrast serif display, and a terracotta or clay accent (near #D97757, Claude's own accent, so on anyone else's product it reads as a tell).
2. A near-black ground with one bright acid-green or vermilion accent.
3. Broadsheet: hairline rules, zero radius, dense newspaper columns.
4. The SaaS-card kit: content chopped into identical rounded cards, one radius on everything, the same soft gray shadow (rgba(0,0,0,.1)) under each, gradient washes as decoration.
5. Template chrome whatever the subject: a tracked ALL-CAPS eyebrow over every heading, meta joined with middle dots ("A · B · C"), labels built as a capitalized word, a spaced dash, and a fragment, tinted near-black (#0B0B0B, #111) standing in for black, a monospace face for small data labels, an arrow after link and button text.

A user pick inside a cluster stays; the test is whether someone chose it.

## Data surfaces

- Sign colors: green and red only as sign (a gain or a loss, a bar above or below zero), each paired with a sign, shape, or word; never for lifecycle, errors, or emphasis, and never blue and green on one chart. Every number that reads good or bad wears its sign color; a count stays ink. The color follows good or bad, not up or down: churn rising wears negative.
- A chart labels at most three numbers; the rest is hover. Labels lead with the number ("+5 tasks"), percentages carry %, and no sentence sits inside a chart. No how-to-read caption: one info marker per section, on the title.
- The chart's hero number is the section heading: 28px in sign color at the chart's top-left, one subcopy line under it, no title row.
- Two or more marks get a legend, not direct labels, which read as sentences in the built product. Labels in one chart share one size and treatment, each starting with a capital.
- Draw a distribution once; a dot strip beside a range bar of the same data reads as two facts. A range is a visual, never a clause of numbers.
- A KPI is type: a label, a number, its change in words. No icon tile, no sparkline. A zero change is gray ("+0"); from a zero prior write "+4 (new)", never "+100%"; nothing to compare is a gray dash.
- A hero number reads one window and never swaps it silently; the recent trend goes on its own line.
- Every axis names what it counts, in the heading's word. Wide time axes show full years. A caption and its marks share an x range.
- The lead sentence is one clause with its key number in sign color, and nothing above it is louder; history and caveats live below.
- The header is identity only (the object's name and its tags). Text that describes the object sits beside its name, not as a section.
- No internal vocabulary: copy is for the person using the app, never the builder (no commands, field names, milestone names, engine terms). A fix that's a command becomes an action ("Load last year's data"); a check that can't run says why in the user's words.
- Thin data keeps the chart forms, drawn as outlines with what's missing in words. Stale is said in words (a banner with the as-of time and a refresh action); faded numbers read as disabled.
- Cut a section that repeats the one above, and a column empty for most rows. No narrow column at the top of a wide page. Leave 4px under the last SVG baseline.

## Copy and controls

- A helper under a heading is one line or nothing. A placeholder is a real example in the product's voice, never "Try:" or "e.g.".
- No copy that explains what the element already shows, and a number is said once: sub-copy doesn't repeat what the chart draws, and no word repeats what the color says. Decorative elements carry no exact copy from the data.
- Paired facts use parallel copy ("since January", "since March 3"). Text the user wrote carries no date.
- A primary action names the act ("Save report"); naming and confirming happen in the dialog after the click. Dialogs hold fields and one meta line at most, no helper sentences.
- An empty state names the cause and offers one plain action ("Adjust filters"), never a conditional one.
- A warning sits directly under the thing it's about.
- Callouts follow one pattern, decided before the second one exists: one placement (under the title block), one shape (a filled strip, an icon, one sentence), the kind setting the treatment. Never a hue, never two stacked.
- A secondary line under a title gets the lightest treatment that still differentiates: a mark beside the text, not a box around it.
- Icons denote the thing in the user's frame: a magnifier for what you're looking into, a lightbulb for the tool's own read, a yield triangle for a warning.
- 20px between a title and its subordinate line, not 12.
- A long user string truncates with an ellipsis and keeps its action visible.
- Actions sit where the sibling surface puts them. One primary action on a front door; the secondary is a ghost button or an icon beside it.

## Cards and lists

- Weight before presentation: name the job of every number (trust, act, or leave) and its size tier. A card carries one hero, one supporting line, and one action; the rest lives on the detail view.
- One control language per product: a filled pill at full radius means selected or a tag; everything else is borderless text. No outlined chips, no segmented control in an outer box. The nav's active tab never shares a shape with the filters.
- Non-text marks use full-strength tokens only; the 40% tints sit under 3:1. A legend never draws a gradient for a stepped encoding, and hides when a column header names the number.
- Peer cards share the row's height by stretch. A variable band sits at the bottom edge; cards with the band and cards without never share a grid, so the quiet ones become rows under the cards.
- A line that says "nothing" on every card is absence: remove it. A state that adds no new fact isn't a state.
- A state never changes an item's height; it changes the item's copy ("3 tasks due, 1 blocked") and explains itself in the detail view.
- Error state is nav plus the block, a bold lead and the action. Summary lines: facts in ink at 600, the connective in ink-2.
- Hover belongs to the whole card and a click opens the detail view; the cue is a small chevron after the label. No per-mark tooltips on a card.
- A mark on a card gets a short name, and one legend for the list sits by the view toggle. A tag every card carries sits in the same place on each, markers to its left.
- A card that can't support its action yet (thin data) doesn't invite it: the action line drops to ink-2, the mark goes, the number is gray.
- Standard controls (tabs, menus, dialogs, toggles, comboboxes, tooltips) start from the project's primitive library and two or three products that draw them well; name the primitive in the brief.

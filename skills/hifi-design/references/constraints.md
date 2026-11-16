# Hi-fi constraints

Read end to end before every surface's token plan, so the user never has to say these. Revision checks are in `checks.md`; the cases behind the rules, in `learnings.md`.

Contents: Deny · AI-look clusters · Data surfaces · Copy and controls · Cards and lists

## Deny (paste into the brief and the design system, with the clusters below)

Inter, Roboto, Arial, system sans, Geist, Space Grotesk, Instrument Serif, IBM Plex Mono with Archivo; italic or colored single words in headings; purple or indigo anywhere; gradients, gradient text, glows, blobs, glass, grid backgrounds, colored side rails; one radius on everything; a soft shadow under every element; cards inside cards; three-card rows; bento; eyebrows, kickers, overlines; ALL-CAPS labels; arrows on links; 01/02/03 markers on non-sequences; emoji or sparkle icons; status pills without a state model; repeated metric boxes; invented or uncheckable stats, claims, or copy; greeting headlines ("Welcome back"; the title names the page or the period); hype words (supercharge, seamless, unlock, magic, revolutionize, game-changing, AI-powered); fade-up on every section; hover effects on non-interactive elements; transition: all; dark mode with no light theme; neon accents; rainbow chart palettes; page-load animation.

## AI-look clusters

Generated design lands in one of five looks, each a default rather than a choice, so it needs a reason from the subject. The collision test checks the plan against them; critics name a screen's cluster.

1. A warm cream ground (near #F4F1EA), a high-contrast serif display, and a terracotta or clay accent (near #D97757, Claude's own).
2. A near-black ground with one bright acid-green or vermilion accent.
3. Broadsheet: hairline rules, zero radius, dense newspaper columns.
4. The SaaS-card kit: content chopped into identical rounded cards, one radius on everything, the same soft gray shadow under each, gradient washes as decoration.
5. Template chrome whatever the subject: a tracked ALL-CAPS eyebrow over every heading, meta joined with middle dots ("A · B · C"), labels built as a capitalized word, a spaced dash, and a fragment, a tinted near-black standing in for black, a monospace face for small data labels, an arrow after link and button text.

A user pick inside a cluster stays; the test is whether someone chose it.

## Data surfaces

- Sign colors: green and red only as sign, each paired with a sign, shape, or word; never for lifecycle, errors, or emphasis, and never blue and green on one chart. Every number that reads good or bad wears its sign color; a count stays ink. The color follows good or bad, not up or down.
- A chart labels at most three numbers; the rest is hover. Labels lead with the number, percentages carry %, and no sentence sits inside a chart. No how-to-read caption: one info marker per section, on the title.
- The chart's hero number is the section heading: 28px in sign color at the chart's top-left, one subcopy line under it, no title row.
- Two or more marks get a legend, not direct labels. Labels in one chart share one size and treatment, each starting with a capital.
- Draw a distribution once. A range is a visual, never a clause of numbers.
- A KPI is type: a label, a number, its change in words. No icon tile, no sparkline. A zero change is gray ("+0"); from a zero prior write "+4 (new)", never "+100%"; nothing to compare is a gray dash.
- A hero number reads one window and never swaps it silently; the recent trend goes on its own line.
- Every axis names what it counts, in the heading's word. Wide time axes show full years. A caption and its marks share an x range.
- The lead sentence is one clause with its key number in sign color, and nothing above it is louder; history and caveats live below.
- The header is identity only (the object's name and its tags); text describing the object sits beside its name, not as a section.
- No internal vocabulary: copy is for the person using the app, never the builder (no commands, field names or engine terms). A fix that's a command becomes an action; a check that can't run says why in the user's words.
- Thin data keeps the chart forms, drawn as outlines with what's missing in words. Stale is said in words (an as-of banner with a refresh action); faded numbers read as disabled.
- Cut a section that repeats the one above, and a column empty for most rows. No narrow column at the top of a wide page. Leave 4px under the last SVG baseline.

## Copy and controls

- Design the best form or flow, not the one the current backend makes easy: a service (the email provider, the auth vendor) is plumbing that may change, so states and copy never borrow its wording or limits.
- A helper under a heading is one line or nothing. A placeholder is a real example in the product's voice, never "Try:" or "e.g.". Exception: a lone capture field with no heading and no button at rest (an email signup) may name the action in its placeholder ("Subscribe via email"), with a visually hidden label.
- No copy that explains what the element already shows, and a number is said once (sub-copy doesn't repeat the chart, no word repeats the color). Decorative elements carry no exact copy from the data.
- Paired facts use parallel copy ("since January", "since March 3"). Text the user wrote carries no date.
- A primary action names the act ("Save report"); naming and confirming happen in the dialog it opens. Dialogs hold fields and one meta line at most, no helper sentences.
- An empty state names the cause and offers one plain action, never a conditional one.
- A warning sits directly under the thing it's about.
- Callouts follow one pattern, set before the second exists: one placement (under the title block), one shape (a filled strip, an icon, one sentence), the kind setting the treatment. Never a hue, never two stacked.
- A secondary line under a title gets the lightest treatment that differentiates it: a mark beside, not a box around.
- Icons denote the thing in the user's frame, not the app's.
- 20px between a title and its subordinate line, not 12.
- A long user string truncates with an ellipsis and keeps its action visible.
- Actions sit where the sibling surface puts them. One primary action on a front door; the secondary is a ghost button or an icon beside it.

## Cards and lists

- A list grouped under a shared stamp (a day, a month) gives every row its own rule and date; a stamp and rule only on a group's first row reads as broken.
- When the user picks a layout and asks for a marker that tells items apart (a favicon, a cue), the marker goes on that layout; a new row shape answers a question he didn't ask.
- Weight before presentation: name the job of every number (trust, act, or leave) and its size tier. A card carries one hero, one supporting line, and one action; the rest lives on the detail view.
- One control language per product: a filled pill at full radius means selected or a tag; everything else is borderless text. No outlined chips, no segmented control in an outer box. The nav's active tab never shares a shape with the filters.
- Non-text marks use full-strength tokens only; the 40% tints sit under 3:1. A legend never draws a gradient for a stepped encoding, and hides when a column header names the number.
- Peer cards share the row's height by stretch. A variable band sits at the bottom edge; cards with and without the band never share a grid; the quiet ones become rows under the cards.
- A line that says "nothing" on every card is absence: remove it. A state that adds no new fact isn't a state.
- A state never changes an item's height; it changes the item's copy and explains itself in the detail view.
- Error state is nav plus the block, a bold lead and the action. Summary lines: facts in ink at 600, the connective in ink-2.
- Hover belongs to the whole card and a click opens the detail view; the cue is a small chevron after the label. No per-mark tooltips on a card.
- A mark on a card gets a short name, and one legend for the list sits by the view toggle. A tag every card carries sits in the same place on each, markers to its left.
- A card that can't support its action yet (thin data) doesn't invite it: the action line drops to ink-2, the mark goes, the number is gray.
- Standard controls (tabs, menus, dialogs) start from the project's primitive library and two or three products that draw them well; name the primitive in the brief.

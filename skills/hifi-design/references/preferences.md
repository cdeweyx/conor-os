# Preferences going in

What the user has picked on the canvas so far, so the first pass on a new surface starts from his choices instead of the agent's defaults. These are the biases to try first, not locks: build the first pass with them, and put an alternative in the directions round only when the surface has a reason to differ. Update this file at every skill pause with the picks from that surface. The dated, product-specific picks these lines came from are in `preferences-archive.md`; when this file nears 1,500 words, move the narrowest lines there with their dates.

## Register

- Polished and crafted, never low-brow or unintentional, toward Linear (calm density, typographic discipline).
- Every product: a black or near-white ground, dark and light built from one set of color jobs, dark the default. Monochrome plus one accent for actions; brand color in the mark and signals, never the page ground. Sign colors follow `constraints.md`; a count has no sign and stays ink.
- "Striking" means a clear story in the marks (color by meaning, a hero number, a direct annotation), not decoration added on top.
- The lightest treatment that still differentiates wins. An icon plus one line beat a rule callout and a quote card; a mark beside text beats a box around it.

## Layout

- Open on the data. No hero on a working screen; the sentence is the title and the key number leads.
- Sections read at a glance: hairline above, 48px of air, 16px/600 title with a 16px stroke icon that denotes.
- Two-column rhythm for paired sections; never a narrow column at the top of a wide page.
- Actions last, where the sibling surface puts them. Consistency across surfaces beats a reorder.
- Callouts directly under the page's title block, one pattern, kind sets the treatment.
- A front door puts the form in the upper middle, the decorative field in the lower third, and a strip along the bottom edge.
- Overlays anchored to the thing they edit (a date editor under the date), not sheets from the side, not inline expansion that pushes the page.

## Copy

- A plain question as the heading, one line under it that says what happens, in the user's words, not the niche's slogans.
- Actions name the act: "Build report", "Save report", "Adjust filters". Naming and confirming happen in the dialog after.
- No copy explaining the obvious, no exact copy on decoration, no helper sentences in dialogs, no "Try:" on placeholders.
- No intro label over content that explains itself (a "Recent invoices" label over a list of recent invoices).

## Components

- The tool's own read gets a lightbulb; what the user is looking into gets a magnifier.
- Cards chunky, number-first (the count before the percentage), one meta line. Tables with hairlines only, tabular numerals.
- Empty states get a glyph from the product's domain, centered with one sentence and one link.
- Controls: secondary actions are text buttons (no border, ink-2 at 500, a 28px hit area); destructive ones confirm inline in the row. The primary is the only filled control, top-lit (an inset 1px white highlight and a 1px contact shadow). Radius 4 / 6 / 8 plus full for controls, surfaces, overlays; interactive resting borders at about 20% ink.
- Surfaces: callouts and the stale banner sit in a sunken well a step off paper with a faint ring; overlays are white on the layered stack; a hovered card uses the shadow as its border; a hovered row is a tone step with a faint ring.
- Notices: one pattern anchored to its cause, and every status line (info, assumed, warning, error) uses the callout component, with an icon and a surface, never a bare line of text. Kind shows in the icon and the text's tone, never hue: a warning is a yield triangle with ink text at 500, never amber. Info is a circle-i in ink-2. With no cause on the page, one line under the title block.
- Prevent, don't warn: an input that would make something invalid can't be entered; the control offers only valid choices.
- An edit mark (a pencil) sits at the end of what it edits and turns on edit mode; a labeled action far from its object loses. Editing a field the user owns opens a modal in the save dialog's pattern, with an info popover on why the field matters.
- Context that can't exist in a state never appears in it.
- A tabbed page has no visible page title (the tab names it; keep a visually hidden h1); object pages keep theirs. Tabs are short and plain, one or two words; a single-user product has no "My"; the tab and the page's primary action share the verb. The nav carries at most one live fact, reusing a mark the product already taught.
- Generic moments (first-run empty, error) take generic sourced glyphs; a product-specific glyph is for the product-specific moment. A rebuild of a picked glyph keeps its composition and fixes the craft.

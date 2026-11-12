# Hi-fi checks

The mechanical checks a surface passes before the user sees it: after each revision (screenshot first), the table lens at refine and polish, the cross-surface pass after the last surface, and the done checklist. A `worker` can run the revision checks in a fresh context on the 2x export (Model: worker role). The rules they check are in `constraints.md`; the cases behind them are in `learnings.md`.

Contents: After each revision · Table lens · Cross-surface pass · Done checklist

## After each revision

- Containers: list every border or shadow; remove any that isn't selection, overlay, or a grouping spacing can't express.
- Sign colors: every signed number wears its sign color and a sign, shape, or word (`constraints.md`, Data surfaces).
- Numbers: every numeric column has tabular-nums and right alignment; units attached with a non-breaking space; one format per quantity across the screen ($48,210 never beside $124,860.40).
- Spacing: every padding, gap, and fixed size is a step on DESIGN.md's scale; a one-off value (13px, 7px) is a decision nobody made.
- Alignment: draw the guides on the 2x export, don't eyeball it. At each level of a list, every row starts its icon on one x and its text on another; panes side by side share one header line; controls in one row share one height. A guide that misses by a few px is a finding.
- Grid: write the sum before placing cards (3 × 372 + 2 × 16 = 1148, the content width); pick the column count from the number of items, and let a lone card span rather than orphan it.
- Type: count distinct font sizes; more than six, or any weight outside the named set, fails.
- Radii: count distinct corner radii; any value outside DESIGN.md's set fails. Nested shapes are concentric: inner radius = outer minus the inset, or the gap is over 24px. A full-round pill inside a 4px box fails; check DESIGN.md's own rules against each other too.
- Chrome: grep uppercase plus letter-spacing; sentence case everywhere except identifiers. No negative letter-spacing below display size.
- Squint at 50% zoom: the lead sentence and the key number read first; nav is a step dimmer.
- States: empty, thin, dense, error, stale each render; the skeleton matches the final layout.
- Grays: sample three; each has 3 to 8% saturation in the same hue family. Pure grays read unfinished.
- Shadows: only on overlays, two layers plus a semi-transparent border.
- Modals: every modal dialog (and destructive confirm) gets a scrim, ink at about 24% on a light theme, no blur, fading in on the base motion and out on the fast one. Popovers, menus, tooltips and toasts get none. The dialog's edge comes from its shadow and border, never the scrim; a copied dialog keeps its backdrop.
- Hover: every interactive word or control has a visible hover state on every surface and in every state it appears, overlays and panels included.
- Icons: one set, one stroke, no background tiles, each optically centered on its text's x-height.
- Copy: no "great," "strong," or exclamation marks on results; every error names the fix. Labels, buttons, headings, and captions end without a period; a line of two or more sentences keeps them.
- Data: diff every number and name against the pasted rows, then against each other. A heading that says 1,112 invoices over a sentence that says 1,140 is the first thing a skeptic finds. Then count repeats: each fact appears once per screen.

## Table lens (usability laws, paraphrased; run at refine and polish)

- Fitts: sort headers and row actions have a hit area of the whole cell, not the glyph.
- Common region and proximity: a number's comparison sits inside the same cell group; column groups read as groups without vertical rules.
- Serial position: the decisive metric is the first data column, the action the last.
- Von Restorff: one highlighted thing per view; a second highlight cancels the first.
- Doherty: a response over 400ms shows a skeleton in the final layout; under it, nothing.
- Jakob: sorting, filtering, and expanding work the way every other table does; novelty goes in the data, not the controls.
- Postel: inputs accept every common form of the value (0.5 and 50%, 7 and +7).
- Aesthetic-usability: a screen that looks finished hides broken states; check the states after the ideal looks good, not instead.

## Cross-surface pass (after the last surface)

- Change a radius or a border weight through the token in one pass across every artboard, never surface by surface; cards at 3 beside buttons at 4 look worse than either. Cards and text areas get their own surface token.
- A pass that touches a chart touches its clones on every surface that shares the data; list the sibling artboards before the first replace, and give the ones with their own data their own edit.
- A number that changes on one artboard changes everywhere it's echoed on that artboard (the lead sentence, the chart subline, "Showing 6 of N").
- Secondary actions are text buttons; the primary is the only filled control on a page and the only one that catches light.
- Carry a picked expressive recipe to every surface with the same moment before proposing new ones.
- One control language, carried to every surface.

## Done checklist (all pass, per surface)

1. Every product-doc goal this surface serves points at a visible element.
2. Six states rendered; each empty and error state has a message and an action; the loading frame is a skeleton in the ideal layout, or there's a reason it isn't.
3. Copy is final, verbatim from the brief, sentence case, actions say what happens.
4. Threshold and sample-size language matches Solution Details.
5. Numbers tabular and right-aligned; peers share size and weight.
6. Text 4.5:1 (3:1 large), chart marks 3:1, every color paired with a non-color cue.
7. Every color and font resolves to a DESIGN.md token, and a node search for the system font family returns nothing. The resting state is drawn in dark, the default, and again in light from the same tokens.
8. No open comment thread: resolved once the fix is on the canvas, tagged taste, or moved to Open Questions. Picks stay open until the user picks.
9. Locked artboards on the Final page named by surface and state, reviewed there once; the state the user would show someone exported at 2x and embedded once under the surface's numbered heading in Solution Details, with the states linked.
10. Every element maps to a noun, verb, or attribute in the product's grammar (an orphan is cut, or the grammar amended first); every overlay names its layer and its lifetime fits it; every verb has a visible signifier.
11. Prototype decision recorded: yes with the interaction it must carry, or no with the reason.
12. The world and the signature from DESIGN.md's Overview are visible: point at where each shows on the surface, or say why this surface carries neither.

Not required: breakpoints, motion, hover and focus polish beyond a visible hover state, pixel-exact spacing. Interaction states (disabled, selected, focus ring, skeleton shape) are token rows in DESIGN.md, not frames.

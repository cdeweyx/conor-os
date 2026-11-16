# Brief and review

The brief and reference templates, the steer-yourself list, the revision templates, and what goes wrong, read at every surface's prep. The critic prompts are in `critics.md`, the done checklist in `checks.md`.

Contents: Hi-fi brief · Reference report (and Mobbin) · Steer yourself before showing · Revision lock · Review batch · Things that go wrong

## Hi-fi brief (one per surface)

```
Surface: <name>
Decision this screen supports: <one sentence from the lo-fi review page>
Product-doc goals it serves: <numbers>
Locked (what lo-fi or the issue settled): <layout | reading order | element inventory | copy>. Do not change these.
Open: <the axis the takes differ on>, then type, color, spacing, borders, chart styling, per DESIGN.md below.
DESIGN.md overrides Paper's style guide. Tokens are on the canvas; reference them, never a raw value.
Ownership: touch only nodes you create this run. Artboard name: <Surface> - v<N> @ <date>.
Converged wireframe: <path to the lo-fi HTML file and its screenshot; do not paste the HTML, rewrite it in Paper's dialect>
Why it won: <two lines from converged directions>
Losers, do not reintroduce: <name, one-line reason each>
Standing rulings: <the latest review's fixes for this surface, one line each; a designer who duplicates an older artboard otherwise revives reversed calls>
Metric hierarchy: <1st, 2nd, 3rd, footnote>
States to render, each its own frame: ideal, empty, thin, loading, error, stale
Copy (final, verbatim): <block, including empty and error messages>
Data: <real rows attached; no invented numbers; "n/a" labeled where unknown>
Audience: <who this surface must perform for, one line from the reference pass>
References: <the annotated technique list from mockups/hifi/references-<surface>.md, pasted as text; no screenshots, no mood words>
Not this: <the anti-reference and the look it names>
Before building (the lead has already run it on the token plan; a designer agent reruns it on its own direction): run the collision test. Plan the palette, type, and layout for a similar brief (same job, another product); wherever it lands close to this plan or in one of the five AI-look clusters, change direction on that axis with a choice from this product's world and say why.
World: <the place or material from the taste interview>. Signature: <the one detail, and where it appears>.
Takes: <two or more, from the planner's plan>, differing dramatically in <the axis the planner named>, never in color alone. Same data, same tokens. Each carries one concrete aesthetic sentence and the assumption it tests; never "unique" or "clean".
Feedback I want: <hierarchy | state coverage | chart styling>
Feedback I don't want: new layouts, new variants, alternative structures.
DESIGN.md: <paste>
```

## Reference report (one per surface, `mockups/hifi/references-<surface>.md`)

Text is what the build agent reads; the HTML report with the images beside these notes is for the user.

```
# References: <surface>
Date: <date>. Source: Mobbin (search_screens "<query>", search_flows <competitors>) | Playwright.
Audience: <who this surface must perform for, one line>
Not this: <one anti-reference, the product or screen, and the look it names>

- Product: <name>
  Screen: <what it is, twelve words>
  Link: <Mobbin or public URL>
  Technique: <line weights, hue count, density, structure, what carries meaning>
  Take: <the transferable principle>
  Avoid: <the part that's theirs, or the mistake>
```

Five to eight entries. Design-shaping's competitive look writes the flows entries; add only what's new for this surface.

Searching: `search_screens` for the surface's job (a list of records, a dashboard, a settings form), `search_flows` for the named competitors, `search_sections` for marketing and front-door pieces. Run the two or three references the surface will lean on hardest through explain-interface, along with the product named in the taste interview and anything the user drops in along the way, and put what it measures in their Technique lines. For the dark theme, the default, add two or three from Dark Mode Design for how layers separate on near-black. The audience line matters because a sharp expert comparing options reads a card differently from a friend being shown one.

Mobbin: OAuth, Pro plan, 60 calls a minute; install with `claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp`, then `/mcp`. Without it, or when its results come back mostly off-domain, screenshot public screens with Playwright in one pass (galleries by job in design-sources), annotate them the same way, and say in the report which was primary.

## Steer yourself before showing

Run before any round reaches the user, on the real 2x exports, and add each new steer he gives.

- At least one bold swing beside the safe set, from an outside reference (Mobbin, another tool)?
- Every element where its kind belongs: metadata with metadata, actions with their object, evidence with the claim it supports?
- Any number or word said twice: sub-copy repeating the chart, a word the color already says, a label repeating a heading?
- One label treatment per chart, full years on wide axes, sign color on every signed number?
- Every icon centered on its text, checked at 8x, every right edge flush?
- Every gap reads as intended at 1x, inside a card (object to its edge) and outside it? On the scale but accidental-looking is still a miss.
- The interaction matches an existing pattern (modal or inline, the save dialog), with an info popover where a field's purpose isn't obvious?
- Each surface between too loud and invisible, checked on the pixel-checked export?
- A critic pick contradicts one of his named likes? The like stays and the fix is softened.
- Every decision in the ask still open? Check the tracker and the last Decisions card; re-asking a settled call costs trust.
- Stacked blocks share their left and right edges, or the label names why not? Count the distinct widths in one view.
- A part of a page also shown inside the whole page? One full-page example at 1440 light is enough.
- The hand-off names the loop's step (direction round, polish, ready review), and shows critic scores only when critics ran.

## Revision lock (prefix every revision turn)

```
Keep the tokens and the current layout. Work only the open comment threads and the selected node.
Do not touch any node not named. Keep all data values as they are. Revise on the duplicate, not the reviewed artboard.
```

## Review batch (one per revision)

```
Rev <n>, <surface>. Feedback wanted: <topic>.
Keep: <what survives, so it isn't undone>
Blocking (goal <n>, <state>): <element>: <observation, impact, request>
Should change (goal <n>, <state>): <element>: <...>
Taste, not blocking: <note>. Leave it.
What would change my mind about calling this done: <one line>
```

Refuse to discuss: structure (point at converged directions), new variants, anything that can't be tagged with a goal.

Comment scope during hi-fi, agreed once with the user: hierarchy, charts, copy, missing states, system violations. Colors, brand, nav, hover, motion, breakpoints, and pixel nudges wait for brand or build. Say so when the user asks whether to comment on every detail.

## Things that go wrong

Read with the rest of this file before the first artboard. Each one has happened; the ones with a home elsewhere name it.

- Screenshots in the brief. The agent copies the pixels and drops the system; technique notes carry.
- Paper's house taste leaking in: mood palettes, asymmetry, a warm human touch. The brief says DESIGN.md wins.
- Fonts substituting silently. Check the family before the first text is written, with the file as the active tab. The canvas falls back to the system face on HTML text while SVG text uses the named one, so only a node check catches it (`paper-loop.md`, font check).
- Icons as text glyphs. SVG or nothing.
- Rewriting a whole artboard for a small change. Update the node.
- Editing inside an SVG. SVG text isn't a Text node: `set_text_content` refuses it and `write_html replace` on one element never renders. Rewrite the whole SVG on the master and clone it into each instance (`paper-loop.md`).
- Trusting undo. Nothing documents undo after an agent write; the duplicate you didn't touch is the history.
- A carry that stops at the base. When a decision changes a number or a word, sweep for the old one: `find_nodes` on the Final page (plus `get_jsx` on chart masters, since SVG text is invisible to search), grep the repo, and grep the fetched product doc. A renamed heading once reached five states and missed two, and dead words outlived their decisions in DESIGN.md.
- Fake data drawn per surface. Generators that each invented rows contradicted each other across surfaces (a client with six open invoices here, one there). Keep one fixture file every generator and artboard reads, check numbers across surfaces at each Final row, and pull real rows through the product's API before inventing one.
- Critics that add. An uncapped critic proposes one more element every round; the removal preference and the round cap are what keep the surface from growing back.

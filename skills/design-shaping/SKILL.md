---
name: design-shaping
description: >
  Runs the design step between a locked product doc and tech planning, from
  dramatically different explorations through hi-fi to written Solution
  Details. Use when the product doc's Overall Shape is locked and the user
  says "let's design", "mockups", "design step", "explore approaches", "what
  should this look like", or wants Solution Details written. Do NOT use to
  write or reshape the product doc (product-shaping, product-doc), for a
  one-off visual of an existing shape (hifi-design), or for polishing a
  built UI (better-ui).
---

# Design shaping

Turn a locked product doc into a converged design and a behavioral spec. The process diverges before it converges, because with an agent variants are nearly free and the biggest risk is anchoring on the first thing that renders. Every step writes something back to the product doc so the design work is a record, not a conversation.

Read the product doc first. The Overall Shape names the surfaces (tabs, pages, panels, views, whatever the product has). Everything below runs per surface.

## Your role

- Same posture as product-shaping: thinking partner, one draft plus one question per turn, a recommendation you defend, a progress map at every gate.
- Ugly on purpose until hi-fi. Agent output looks finished by default, and polish invites polish feedback when the question is still structure. Say so in the prompt every time: gray boxes, one system font, no color, real data.
- Real data, always. The content is the design. Lorem ipsum and fake numbers hide the layout problems that matter.
- Never ask for "more distinctive." Name the constraint (type, density, color meaning) or the agent redraws the same default.
- Every step closes the same way: write the full output, drop it in chat, ask before pushing it to the product doc, and wait for the user to say the step is done before starting the next. The gate is their review, not your sense that it's complete.
- Before any research (the spike, the competitive look), post the lanes and wait for a go. Screens come from Mobbin over its MCP when it's connected and from Playwright screenshots of public screens otherwise, in one pass after the text research lands; open only the images that change a decision.
- Keep a running list of open questions through every step. At each step close, refresh the product doc's Open Questions: share new ones with a proposed answer, then add them. Frame each as the goal or tension behind it, not the feature; when something is punted, record what's out and which part of the goal still matters. When the user answers one, it moves to the doc's Resolved section with the answer as their line and its number kept, so the sequence stays readable.
- Everything written for the user (specs, summaries, open questions) goes through writing-style first. No framing sentence that restates the structure, no method labels on sections, the plain name of the thing instead.
- Answer the question asked, at its size (zero-to-one, Working with the user). A rundown for a new context window here also carries the canvas positions.

## The steps

1. Interview. Read the product doc and ask the hard questions per surface, one at a time: what the key object looks like, what happens with no data, what a time window means, what "done" looks like on this screen. Wherever the user authors something (a rule, a note, a name), ask what fixed set of structures it offers, typed clauses or a few semantic styles, the way Notes has no font menu; free text is the exception and needs a reason, since presets keep meaning and most people format badly. Write answers back into the product doc as decisions, or into Open Questions if they're still open.

Research spike, optional, after the interview. Ask once: is there anything the interview surfaced that design can't proceed without knowing? A statistics question, a domain convention, a regulatory constraint. If yes, run it through product-research (lanes proposed, confirmed, run in parallel, synthesized to the project's research page) before the user journey. If no, say so and move on. The point is to not design a display for something nobody understands yet.

2. User journey. For each surface, a table: the places (screens, panels, states), what the user can do in each, and what each action leads to. No pictures yet. Mockups bias everything that comes after them, and a table keeps the abstraction honest. This becomes the skeleton of Solution Details. Close it by naming the one or two crux surfaces, the ones the product fails without, with a line on why. They get the exploration budget (wildcards, bold swings, a second round); every other surface gets a single pass: one round of lo-fi explorations, then hi-fi with no wildcards or bold swing. This overrides the round and wildcard defaults in wireframe-explorations and hifi-design for those surfaces.

Grammar, after the journey, once for the whole product. The journey is organized by place; the grammar is organized by object, so it catches what the journey hides: a noun with one verb, a verb with no home, a dialog that should be a popover. Write posture, nouns, and the object-action matrix in the product doc's design page, and draw the layer stack and a numbered beats strip on one gray-box "Grammar" artboard in Paper; read `references/grammar.md` once before drafting, it holds the five sections and a worked example. Every sparse row in the matrix gets a decision, and an empty cell that should be full goes to Open Questions. A contested verb, and every destructive one, gets a citation from Interface Lineage (the reference has the curl lines). Explorations, hi-fi's done checklist, and the prototype's step list all read from it, and DESIGN.md's terminology line copies its nouns.

3. Competitive look. Now that the surfaces and their jobs are named, look at what the incumbents do for each, with specific questions. Scope it to the seams: what they do well enough to steal, what they do badly that the explorations should attack. Not a teardown, though what's worth stealing gets an explain-interface read when the screen is public, so the entry says how it's built as well as how it looks. Pull the screens with Mobbin's `search_flows` per named competitor when the MCP is connected (hifi-design's reference pass has the install line), Playwright on their public screens otherwise. The output per surface is an annotated text list, each entry with its link and the technique it uses (line weights, hue count, density, structure, what carries meaning), plus a report with the images for the user; hi-fi's reference pass reuses that list rather than searching again, so write it in the report format from hifi-design's `references/brief-and-review.md`. For a kind of surface with an entry in `references/flow-references.md` (onboarding so far), read that entry beside the incumbents: it's a format worth borrowing on any product, not a competitor. Name one anti-reference per surface ("not this", the product and the look it stands for) and one line on the audience the surface must perform for; both travel to the brief. An optional token lane, when the user says yes: Fudge over MCP on each incumbent's core working screen, five numbers each (body size, row height, cell padding, palette count, where the accent goes), handed to the hi-fi interview. Hyperbrowser's DESIGN.md extractor is the manual fallback. Raw reports go to the research page by product-research's same-day rule; the synthesis goes in an appendix toggle. Feed it straight into the next step.

4. Explorations. Run wireframe-explorations per place from the place inventory. It posts a brief per place (the job, why it's worth exploring, each option's assumption) and waits for a yes before drawing, then builds three to five options that differ in approach, ugly on purpose with real data, and returns one contact sheet per place plus a review page. Put the sheets in a design explorations toggle in the product doc. Present without a recommendation.

5. Feedback and convergence. The user reacts to each exploration. Keep the format light but structured, because critique tied to goals converges and reactions don't: each note is a like, a wish, or a what-if, and names the goal it serves. Merge the best elements into one direction per surface rather than picking a winner; the planner role does the merge from the user's notes and the references (build's `references/design-loop.md`, "The planner frames every round"). Two rounds is the target. On the second round the question is "what would change your mind," not "what else could we try." The thinking, what was tried and why it lost, goes in a scratch toggle in the product doc.

6. Hi-fi. Run hifi-design per surface. It interviews for taste, writes DESIGN.md with a rendered specimen, puts the tokens and a system artboard on the Paper canvas, briefs with structure locked (wireframe file, states, final copy, metric hierarchy, losers), builds three directions as artboards once, then iterates on canvas comments and selection until the user says the surface is good. Front-door surfaces (home, empty, onboarding) get a treatment axis through visual-assets after the structure pass, and so do empty and error states inside a working surface, at a smaller scale. Per surface it runs hifi-design's per-surface loop in its order (the reference pass reuses step 3's list), then the spec for that surface written in chat and pushed as the next numbered heading under Solution Details (one inline frame, links to the Final page for the states), Open Questions refreshed, then the skill pause (authoring-skills' Closing a skill update) on hifi-design and this skill before the next surface. Steps 7 and 8 run per surface inside that loop, not once at the end; step 9 runs once, after the last surface.

7. Prototype. The test is whether a static frame can answer the question you'd ask a user. A loop, more than two states, or a control whose feel is the question means yes. Build it in code with fake data in a PR; a coded prototype keeps most of its structure through build. A prototype is small: one per motion or control, with only enough of the screen around it to judge the interaction. It never prototypes the whole app. A control whose feel is the question gets live knobs (DialKit) bounded to the motion rulebook, and the tuned values go into the spec. Anything that moves goes through motion-design first (jobs, spec, keyframe strip, prototype, recording), which calls review-animations on the code. Static reads get a frame and a states table. Stack: what's in the repo, otherwise a pragmatic default confirmed with the user first.

8. Solution Details. Per surface: the reading order, per-element rules, a states table (ideal, thin, empty, loading, error, stale), event-to-state transitions, and edge cases written as scenarios ("when X, then Y"), never as categories. Include the rules the user reads (thresholds, limits, what a number means), rabbit holes, no-gos, and the prototype decision. Written into the product doc as a numbered heading per surface under Solution Details, no toggles, per product-doc's Solution Details reference. There's no journey rewrite at the end: Overall Shape already carries the journey, and each numbered spec lands in journey order as its surface closes, shared chrome (the nav) last. Every transition that lands on another surface ("opens the habit view", "the week, filtered to that habit", "Done returns to the list") is checked against that surface's artboards when the spec is written, and anything undrawn is drawn or cut then. Surfaces designed one at a time leave their seams unowned: one run's final review found an edit flow, a date picker, a share sheet, and a "due this week" line that every spec pointed at and nobody drew.

9. Revisit open questions. One last pass through every open question after the last surface, polish, and motion. Each one is resolved by the design (moved to Resolved with the user's answer), resolved now with a design call the user makes, or left open and labeled for tech planning. Anything that surfaced but the user can't see from the UI (data shape, jobs, caching, where numbers come from) goes in the tech toggle, the product doc's toggle of what tech planning needs. Show the sort in chat and push on a yes; after that, the user's answer to each design call is the push, so push it the moment it's settled. Build the sort from the freshly fetched doc and account for every number: a sort written from memory dropped a question that had been settled at polish. Fetch again before each edit, because every move renumbers the open list, and name the calls by topic in chat, not by doc number. A question that turns on a number gets its math checked before any display is proposed (see hifi-design's metric sidebar). The pass also sweeps the synced copies: the DESIGN.md toggle, tab and surface names in Overall Shape, and any spec line an answer touches.

10. Final review. A fresh context reviews: worker subagents from this session, read-only, each handed the exported doc and the Final page's PNGs (Model: worker role; the critic role only scores one screenshot against a rubric and refuses a doc-to-screens audit). Split it three ways: two workers by surface, and one for goals-to-screens and state completeness. Each checks Solution Details against the product doc and the Final page and flags only gaps that change behavior: every product-doc goal points at something visible, and the Final page is complete. Then the skill pause folds the whole run into this skill, hifi-design, and zero-to-one. The design step closes there, and tech planning gets its inputs from the open list and the tech toggle.

## Tooling

- Explorations: wireframe-explorations owns the stylesheet, the constraint block, the scanner, and the contact sheet pipeline (Playwright). Keep PNGs under 5 MB so the doc tool renders them inline.
- Treatment and motion: visual-assets for front-door surfaces; motion-design at the prototype step. Both optional, both called from hifi-design.
- Hi-fi: Paper Desktop over MCP, with hifi-design owning the DESIGN.md template, the specimen, the Paper dialect and loop, the brief, the review intake, the done checklist, and the handoff shape. dataviz for chart form; better-ui at build, not here.
- Mockups folder in the project repo, gitignored or not per the project. Dated filenames that say which surface and which exploration.
- Design research (technique lanes, reference lanes, empty-state patterns) goes to the project's design-process page as numbered sub-pages the same day it lands, and to the repo. The product research page holds product research; the two don't mix.

## Things that go wrong

- Five layouts of the same idea presented as five explorations.
- Hi-fi with no done signal, drifting into taste and burning usage.
- Correcting the same default three times in one session. Clear and rewrite the prompt with the constraint named.
- Putting rules the user reads (a limit, an empty-state message) in the tech toggle. If it changes what they see, it's Solution Details.
- A decision on a later surface that changes an earlier one. On one run, a later surface's metric sidebar made the amount owed the headline number and demoted the status word, which forced a revisit of an earlier surface and a sweep of every state. Before the first surface's hi-fi, run the metric sidebar once across every surface that shows the same object (an invoice on a card, a row, a panel, a popover), so the weights are set product-wide.

## Checklist

- Every step wrote something back to the product doc, after the user reviewed it in chat and said push.
- Research lanes were previewed before launch.
- Open Questions in the product doc are current at every step close, framed as goals not features.
- The research spike question was asked after the interview, and answered either way.
- The journey named the one or two crux surfaces, and only they got a second round or wildcards.
- Competitive look left an annotated text list with links per surface, an anti-reference, and an audience line, in the format hi-fi's reference pass reads.
- The grammar was written after the journey: posture, nouns with an if/then each, the object-action matrix with every sparse row decided, the layer stack and beats on the Grammar artboard.
- Explorations differ in approach, not just layout, and one is the incumbent baseline.
- Feedback notes name the goal they serve.
- Hi-fi hit the done signal per surface, with every state shown, and the skills were updated after each surface from every comment on the surface, not once at the end.
- Prototype decision was made against the interaction test, not skipped by default.
- Solution Details are scenarios and tables, landed per surface in journey order; no end-of-step rewrite.
- The open-questions pass sorted every question into resolved, resolved now, or open for tech planning.
- The final review ran in fresh-context worker agents and the skill pause updated the skills.

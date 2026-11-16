---
name: product-doc
description: >
  Writes and shapes product docs: opportunity briefs, feature specs,
  initiative proposals, and problem / solution framing. Use when the user
  says "write a product doc", "spec this out", "draft a brief", or wants a
  section of an existing doc written or reworked. Do NOT use for the full
  frame, research, and shape process (product-shaping, which hands off
  here), for technical design docs or engineering RFCs, or for research or
  meeting notes (research-notes, meeting-notes).
---

# Product docs

A product doc is the thinking tool before the PRD. It defines the why, the shape, the open questions, and just enough of the solution that design and eng can react. It's not a complete spec on day one; Solution Details fills in later.

Read `references/example.md` once before drafting. One full example carries more than the section guidance below.

## Your role

You're a thinking partner, not a scribe.

- Push for simplicity. If the shape takes more than two sentences to explain, ask "do we actually need this?"
- Have a recommendation and defend it. Don't present options neutrally.
- Question scope. Every requirement should trace to evidence. If it can't, say so.
- Ask whether this is a local fix for a broader problem. "Add a setting for X" is often a symptom of a missing model or a bad default. Before jumping to a feature, ask whether a cleaner abstraction makes it unnecessary.
- Ask whether it's unique thinking or table stakes. Table stakes is fine, but name it. If nobody else in the market does it, that's either differentiated or wrong; ask "why does nobody else do this?" before converging.
- Don't over-simplify. If the user's longer version was better, keep it.
- Verify current behavior before asserting it. Docs describe intent, not what shipped. If you can look (code, live app, a screenshot from the user), look. If you can't, say what you couldn't verify instead of writing around it.

## Before you write: frame the problem

This is a conversation, not a questionnaire. Inside a product-shaping run, its numbered order wins; on its own, start with whichever question matters most given what the user brought and follow the thread, but every one of these should have an answer before the doc gets drafted. Track them as you go and ask directly for any that didn't come up.

1. **What's the customer job to be done?** Not a feature. "New users can't get from signup to a useful result without help" is a job; "better onboarding" isn't.
2. **Why now?** What changed? Flip it: what happens if we do nothing? If the honest answer is "not much," that's the signal.
3. **What does success look like?** Concrete and testable. "Twice as many new users reach their first saved artifact," not "more users activate."
4. **Who's the first customer?** The persona or segment we design for first.
5. **What's the business impact?** Activation, retention, expansion, revenue, and the mechanism. Don't accept "it's important." For a personal tool it's the payoff (time saved, money made) and whether it seeds something bigger.
6. **What does this unlock beyond the feature?** Positioning, new segments, future work.

Appetite isn't a framing question; push for the smallest shape anyway.

Then present a framing check-in: one line per question, under 20 words each, and ask if it looks right before drafting. Give a confidence number ("I'd put this at roughly 70%, the signal is consistent but thin") so the user knows how much evidence the doc rests on.

**Starting from an existing doc:** read it first, then treat it as one input, not the foundation. The framing might be wrong or anchored on an old hypothesis. Ask what prompted the rework. Preserve what's still valid and move superseded content to the Appendix with a note on what changed and why.

## Structure

Sections appear in this order. Not every doc needs every section, but the order holds because each one frames the next.

1. **Title.** Names the job, not the feature. "Help clients read invoices without the sender's context" is a job; "Offer custom logo uploads" is a feature. A good title survives the solution changing. Verb-led, under 60 characters, no "add / build / implement / support."
2. **Why this? Why now?** Two to three bullets, each a self-contained argument. Lead with the user's pain, not the business metric. At least one bullet grounded in real behavior (a quote, a session observation, a number with a link). Include the "why now": timing, competitive pressure, cost of inaction, an unlocked dependency.
3. **Hypothesis.** One sentence, set apart from the body. "If we [change], then [outcome], because [reason]." It has to be falsifiable: if we ship it and it doesn't work, would we know?
4. **Goals / Non-goals.** Goals: 2 to 4, verb-led, specific enough to check post-ship. "Eat better" isn't a goal; "show which saved recipes fit tonight's pantry before dinner" is. Non-goals: what we're deliberately excluding and why. Each one preempts a real "but what about X?" and does work; if nobody would expect it in scope, cut it. Non-goals are for scope, not dependencies. "Won't ship until X lands" belongs in Overall Shape or Open Questions. Plain lists, no bold labels, and vary the phrasing: a list where every line starts with "Not" reads as a template.
5. **Success Metrics.** Framed as questions ("Are more new users reaching their first saved artifact?"), not KPI definitions. Order: the broad outcome metric the team already tracks, then discovery (are people finding it), then adoption (are they using it repeatedly). Each metric traces to a step this project actually changes. Guardrails only when there's a plausible way this hurts an adjacent metric. Be honest about what can't be measured yet. Optional for a personal or single-user tool: nobody's tracking a dashboard, and retention already lives in the hypothesis.
6. **Overall Shape.** The core of the doc. One sentence of setup, then structure: numbered steps for flows, bold-labeled bullets for non-sequential features. What ships and how the pieces fit, not how it's built. Stay at product altitude: what the user sees and does, and what has to be true underneath, in plain words. Data formats, schemas, build order, and stack choices belong in the tech plan; if you write "JSON," "ships first," or a library name, cut it. Follow-on milestones stay in the same list ("data model supports it from day one, UI ships as its own milestone") so the whole shape is visible in one place. Prerequisites go in a short separate list below, only ones not already in flight.
7. **Designs.** Only if design links exist. An empty section with placeholder text is worse than no section.
8. **Solution Details.** The behavioral spec, filled in during design and eng, not at shaping time. Stub it with "..." and nothing else; the reader knows. When it's time to fill it, see `references/solution-details.md`.
9. **Analytics.** An events table, four columns: Event, Trigger, Properties, Notes. No narrative. Fewer events, not more: cut anything derivable from another event, any always-true property, any property that doesn't create a cohort you'd actually segment on. Event names are readable with a shared prefix so they group ("Guided Tour Step Shown"). Properties are snake_case in inline code; enums as `property_name: [a, b, c]`. Analysis ideas go in the Appendix.
10. **Open Questions.** Real decisions that would change the shape, scoped to this project. Numbered. Bookmark them throughout the conversation (deferred decisions, feasibility unknowns, non-goals with tension), then review: cut what got resolved before the doc existed, add what the conversation missed. Frame each as the goal or tension behind it, not the feature ("how does a user know a habit is still on track?", not "add an alerts page"), so the answer can be something other than the feature. When one gets answered, it moves to a Resolved toggle at the top of Open Questions with its number kept and the answer as an indented sub-bullet ("your initials (YYYY-MM-DD): ..."), so the numbering other pages cite still resolves. When one is punted, record what's out and which part of the goal still matters, so the punt doesn't read as the goal dropped.
11. **Appendix.** Separated by a divider. Collapsed blocks for prior iterations of the shape, evidence detail with links, analysis ideas for later, parked product ideas ("Could be cool later"), related work. Keeps the body clean without losing anything.

## Writing the sections

- Write Why this? Why now? first. It forces you to understand the problem before proposing solutions.
- Write the title after the hypothesis is locked, since the job becomes clear then.
- In Overall Shape, propose two or three meaningfully different approaches in conversation before converging. For each: what it optimizes for and what it trades away. Ground every element in something from the framing or research. Push for the smallest thing that solves the problem.
- Hyperlink evidence with 1 to 3 words on the specific claim. Don't re-link something already linked earlier in the doc.
- Cross-reference related projects with real links or backlinks, not plain text.
- Match the doc's weight to the change. A one-line code change gets a one-bullet shape. Resisting growth is part of the job.
- Keep people out of critical context. "Existing broken flow," not "flow built by [name]."
- Flag uncertainty in the doc itself. "Not confirmed, but this looks like the cause" beats stating a guess as fact.

## When to compress

- Strong evidence and a clear problem: skip straight to the shape. Still check for related or prior work.
- Problem understood, solution unclear: a light framing pass, then spend the time in Overall Shape.
- Small bet or quality-of-life fix: the whole thing is one conversation, and the doc might be Overall Shape plus Solution Details (still stubbed at shaping; design fills them in).

## Rendering notes

Apply these when writing into a specific tool; otherwise ignore.

- Headings are flat: every major section is H1, sub-topics inside a section are H3, Solution Details topics are H4. Never H2. The doc scans as a list of sections, not a tree.
- Notion: Hypothesis in a default gray callout, no icon, no color override, with a bold "Hypothesis:" prefix and no heading. Goals / Non-goals side by side in columns with the heading inside each column. Appendix items as toggles with plain-text summaries. No page icons. Verify every write landed by re-fetching; batch updates can silently skip an operation.

## Quality check before delivering

- Title names the job and survives the solution changing
- Why this? Why now? leads with user pain and cites at least one real observation with a link
- Hypothesis is one falsifiable sentence
- Goals are verifiable; every non-goal preempts a real question
- Success metrics are questions, ordered outcome → discovery → adoption, and trace to a step this project changes
- Overall Shape is one sentence of setup then structure, at product altitude, with no formats, build order, or stack
- Open Questions would each change the shape if answered
- Voice matches writing-style: direct, specific, no hedging, no LLM tells
- Length fits the problem: roughly 400 to 700 words for a focused problem, up to 1000 for a broad one

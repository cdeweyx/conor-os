---
name: product-shaping
description: >
  Three-phase product shaping: frame the problem, research it, and shape the
  solution into a validated spec, then hand off to product-doc for the
  writeup. Use when scoping a new product investment, turning a vague idea
  into a concrete opportunity, gathering evidence for a product decision, or
  reworking an existing doc, or when the user says "shape this", "let's
  shape", "scope this", "new feature". Do NOT use to just write or edit a
  doc (product-doc) or to log research or notes (research-notes,
  meeting-notes).
---

# Product shaping

Turn an idea into a validated spec through three phases: Frame, Research, Shape. Each phase ends with an explicit opt-in before the next starts, because research nobody agreed to is wasted and a shape built on an unconfirmed frame is wrong. The output is a product doc written per the product-doc skill. Load product-doc at the start: shaping uses its role, its six framing questions, and its section guidance throughout.

## Your role

Take product-doc's Your role (a thinking partner with a recommendation you defend, who pushes for simplicity, questions scope, and gut-checks the novel) through every phase. Shaping adds:

- Keep things tight. No artifacts "for completeness."
- Keep each turn small: one draft plus one question. A wall of options reads as a questionnaire and the user stops collaborating. Bold only section labels, never words inside a list or a sentence.
- Ask for a call the way build's Asking the user says: what to review, where to look, the word you want back.
- Keep zero-to-one's progress map at every gate, one line naming the phase and section ("Phase 3, Goals and Non-goals locked, next is Overall Shape"), and answer "where are we" with it.
- Apply the writing-style skill to anything written: framing summaries, spec sections, the doc.

## Starting from an existing doc

Start the way product-doc says (read it first, treat it as one input, ask what prompted the rework, move superseded content to the Appendix), then adapt the phases. Solid frame but weak shape: skip Phase 1, light Phase 2 for new evidence, go deep on shaping. New evidence challenges the hypothesis: revisit Phase 1, targeted research, reshape. Bare stub: start from scratch but update the existing entry.

## zero-to-one's two modes

**Personal mode** shapes a product the user will build for themselves first. Shape it as a public product (who it's for, why it wins, the rivals), because that decides what gets built. Accounts, pricing, marketing, and the front door go in as non-goals marked "(Go live)" so Launch shaping can find them, and so do Success Metrics: skip them here and let Launch shaping write them, unless the user wants a draft now. Step 2's front-door and pricing rules don't fire here. Phase 2 reuses zero-to-one's research synthesis and adds only what shaping still lacks.

**Launch shaping** is the mode for zero-to-one's Go live step 1: the same three phases on a product the user already uses, to take it public. Start from the existing doc (above), Personal's closing handoff, its "(Go live)" non-goals, and what real use showed; that use is evidence the first shaping didn't have.

- **Frame.** The frame stays locked unless use broke it, so skip the six questions, Other framings, and the keywords. The check-in asks only who the public user is, what they need that the user didn't, and what launch means here (a waitlist, open sign-up, paid from day one), then gives the confidence number.
- **Research.** The launch lanes in Phase 2 (comparable paywalls, metering, an open-source angle, funnel and landing references, growth fit), plus pricing. They run here, not through product-research, even with no company behind the idea.
- **Shape.** The front door (Step 2's landing-page rule), pricing and the paywall (Step 2's pricing rule), accounts and sign-in, the legal pages, and the Success Metrics the personal tool skipped.
- **Write.** The launch shape goes into the product doc as its own section, and the "(Go live)" non-goals move into it as goals or stay parked. Step 4's cold read runs on that section. Design Needed issues are filed as the split is agreed, as always, but in the Go live project's "Launch design" milestone with no blocker, since zero-to-one files no shaping issue; tech planning moves each into the milestone that ships its surface.

## Phase 1: Frame

*Goal: define the problem clearly enough to know what research to run.*

Ask product-doc's six framing questions one at a time, numbered ("Question 2 of 6, why now"). For each: write your own answer first to a scratch file the user doesn't see, then ask the question bare (no take, no options, no lean), then once they've answered, draft the answer in the user's voice from what they said, show your pre-written take beside it with where it differs and what you'd push on, confirm, move on. Your take stays unbiased because it's written before theirs, and theirs stays unbiased because yours isn't shown until they've answered. The same holds for every interview question in any shaping or design interview. One question per turn, because bundling three produces long answers to none of them and the user loses track of what's settled. If the user's opening message already answers some, say which and skip them. A feature inside a product that's already shaped (its doc names the customer, the why now, the metrics) asks only the questions that doc doesn't answer for this feature, usually the job alone, and cites the doc for the rest. Push past the first answer on the job; it does the most work downstream. On question 6, offer a brainstorm if the user wants one: five to seven candidates, one line each with a take, ranked.

Weave in throughout: is this unique thinking or table stakes (table stakes is fine, name it), why are we building this (make the user defend it), and is this a local fix for a broader problem (an "add a setting" request is often a symptom of a missing model or bad default).

**Framing check-in.** Once all six are answered, run product-doc's check-in (one line per question, what the user said, not your analysis), ending "Does this framing look right? If so, I'll propose a research plan.", and iterate on pushback until it's confirmed.

**Other framings.** When the idea arrived as a solution ("build X", "add Y"), the user's framing is one of several, and research only asks what its framing points at. With the check-in, offer three problem framings the same idea could answer, one line each with the build it leads to ("users don't see what changed": state indicators; "users don't trust it's working": status and an audit trail; "users want it watched for them": digests and alerts), and say which you'd pick and why. The user keeps theirs, picks one, or merges, and the research plan asks that framing's questions. An idea that arrived as a problem skips this.

**Confidence check.** Give product-doc's confidence number with its reason. Here it sizes the research: high confidence means narrow, targeted research to close specific gaps; below 50% means broader research and a readiness to kill it.

**Propose the research plan.** Be specific about what each track investigates and why:

- **Context and prior-work scan** (always runs first): strategy docs, related initiatives in any state (shipped, in progress, parked, killed), and existing research or analysis that already covers this.
- **Customer research**: specific questions to answer from customer voice (calls, feedback, support), not "research customers." Each question is its own investigation.
- **Analytics research**: specific metric questions to size the problem.

Also recommend tracks you think would be valuable based on the framing ("this touches the AI flow, I'd look at current AI adoption and drop-off first"; "there are three related initiatives already, read those before designing").

When the shaping touches launch, pricing, or a paywall, customer and analytics are too narrow. Propose these lanes by default: comparable paywalls in the category, how products meter a paid feature, what an open-source angle could do, funnel and landing references outside the category (tasteful tools that handle the same moment well), and growth fit (do the pricing, the funnel, and the growth plan mesh). They run beside Tracks 2 and 3, the same way. Tell each of these researchers to pull on interesting threads it finds rather than stop at the brief, and to name the ones it followed.

**Agree on search keywords.** The same problem has multiple names; customers, engineers, and support describe it differently. Build the list, let the user refine it. It drives every search downstream.

Present plan and keywords together, then wait for the opt-in before running anything.

## Phase 2: Research

*Goal: gather the evidence the shape will rest on.*

If there's no company behind the idea (no strategy docs, no customer calls, no analytics), Phase 2 is the product-research skill instead of the tracks below. Run it, then come back here for Phase 3.

### Track 1: context and prior work (first)

This is the foundation everything else gets interpreted against.

- Load the project's strategy context (whatever the project defines: strategy, current-quarter goals, named assumptions, personas). Selectively load what the problem touches.
- Scan for related initiatives by keyword, in any state. Surface what you find with the context that matters: what overlaps, what was killed and why, what's in flight.
- **Verify the current shipped state.** Docs describe intent, not what landed. Check the live app or the code, note deltas between docs and reality, ask the user to confirm anything ambiguous. A screenshot from the user is primary over any doc. This catches the most common shaping failure: citing a feature from an old doc as if it shipped.
- **Verify every cost or constraint premise in the code before it shapes anything.** A premise from the kickoff ("each call costs us, so every tier needs a cap") gets measured from real usage, since a wrong one sets caps, tiers, and metrics. One measured at a fraction of a cent turned caps from cost control into a value gate and an abuse guard, killed a success metric built on it, and showed the real costs were fixed licenses.
- Scan existing research and analysis broadly. If something recent already covers this, surface it, flag how current it is, and don't duplicate it.

Output: a synthesis of how this connects to strategy, related work, existing evidence, and the gaps. This decides whether the other tracks are still needed and what they should ask.

### Tracks 2 and 3: customer and analytics research (after Track 1, in parallel)

For each agreed question, run a separate investigation with the question, the keywords, and the strategic framing. Use the project's research skills or sources; if sub-agents are available, one `researcher` agent per question (Model: researcher role), and if a research agent fails twice, run that question in the main conversation. Skip or narrow a track when Track 1 surfaced recent research that already answers it.

Customer research synthesizes existing signal; it shouldn't be written back as new signal, because derivatives of derivatives pollute future searches. Analytics research produces genuinely new artifacts (dashboards, findings) and can be saved.

### Present findings as they come in

Track 1 inline as it's gathered. Each research investigation in full as it completes, not condensed to a few bullets. The user needs to see the evidence. **Preserve source links** on every claim so anything can be verified in one click.

Close the phase with three writes, because research that lives only in chat is gone next session: the raw reports saved in the repo (product-research's same-day rule), one appendix line in the doc pointing at them, and Open Questions refreshed after the user has reviewed them.

Then the phase gate: "Ready to start shaping, or is there more research to do first?"

## Phase 3: Shape

*Goal: make the design decisions, then capture them.*

### Step 1: Lock the frame

The research either confirmed the Phase 1 framing or shifted it. Either way, lock each element before designing, one at a time:

1. Present a draft based on the framing plus the research.
2. Challenge your own draft first. Is the hypothesis actually testable? Are the goals specific enough to evaluate? Do the non-goals preempt the right questions? If something's weak, say so before the user has to.
3. Challenge the user's thinking. If their framing doesn't hold against the research, push: "The research shows X, but the hypothesis assumes Y. Which is it?"
4. Ask for holes. "What am I missing?"
5. Iterate until both sides are satisfied, then move on.

The elements, in order: Why this? Why now? (push: is the "why now" real? If this could've been built six months ago and wasn't, what changed?), Hypothesis (push: is it falsifiable?), Goals and Non-goals (push: could we remove this non-goal and nothing changes? Is it scope or a dependency?), Success Metrics (push: can we measure it? Does it trace to a step this project changes?). Section-level guidance for each lives in product-doc.

For a feature inside a product that's already shaped, Success Metrics are skipped unless the user asks for them; the hypothesis names what to measure. For a single-user or personal tool, offer to skip Success Metrics (product-doc's Success Metrics says why); don't invent discovery and adoption metrics for an audience of one.

Confirm before moving on: "The frame is set. Ready to shape the solution?"

### Step 2: Shape the solution

A back-and-forth, constrained by the locked frame and grounded in the research.

1. Propose two or three meaningfully different approaches, not variations. For each: what it is, what it optimizes for, what it trades away. Recommend one and defend it. Before feature-level solutions, ask whether a cleaner abstraction (a model, a primitive, a default) makes the feature unnecessary. "Add a toggle" is a feature; "change the default so nobody needs the toggle" is an abstraction.
2. The user reacts, gravitates, combines. Follow the thread.
3. Narrow through pointed questions that force decisions: replace the existing flow or live alongside it? All users or new users only? New surface or inside something that exists?
4. Ground every element in evidence. If it can't be traced, challenge it.
5. Push for the smallest thing that solves the problem.
6. Once a direction is picked, brainstorm. Five to seven ideas that could live inside the shape, one line each with a question attached ("is this a view or a filter?"). The user keeps, kills, or parks each. Killed ideas go nowhere. Parked ideas, here or anywhere in the session, go to the doc's "Could be cool later" list in the Appendix, never to the tracker unless the user asks for a ticket. This is where the shape gets its texture, and it's cheap.

Keep the shape at product altitude (product-doc, Overall Shape): what the user sees and does, never formats, sequencing, or stack.

**The landing page can be part of the shape.** When the product's signed-out app could be its front door, offer one front door (the signed-out app is the landing page) against a separate marketing site. If the user picks one front door, shaping that app is shaping the landing page: set its sections and their order here, at product altitude, with the page's idea sentence (landing-page step 3), since the review checks it. Before proposing the final structure, run landing-page's cold structure review (its step 4) and bring its proposal with your verdict on each change; the user still overrides it. The page's design then runs through landing-page as a Design Needed issue in the build milestone that ships the signed-out app, not after Quality.

**File design issues as soon as the split is agreed.** When the shape splits off a surface or page that needs its own design, file its Design Needed issue right then, in the shaping issue's project and milestone, blocked by the shaping issue (Launch shaping says where they go when there's none), with its contents to come from the doc section that shapes it. Don't wait for the doc.

**Pricing and paywall calls.** Lead with the simplest option; the user has picked it every time so far. A one-time free allowance over a monthly reset, no trial at launch (adding one later is easy, taking one away is hard), two plans (monthly and annual) over a third, and sign-up with no password (Google plus an email code). It's a tendency to lead with, not a rule: still give the runner-up. Keep a free allowance's remaining count out of the way: no counter sitting beside the action, only a quiet line after a run and in settings, because a standing "2 left" discourages using it. The wall itself can be a modal.

Feasibility questions come up mid-conversation. When they do, investigate the codebase (existing flows, data models, what's reusable) right then; it's a tool you pull out, not a separate step. If there's no code access, ask the user to describe the architecture and flag the assumptions.

Research questions come up too ("what do the competitors show on this screen?"). Check what Phase 2 already found first and surface it. If it's not there, offer a targeted look with a time estimate, and ask before running it. Often the right answer is "work from what we have now, run it at the start of design."

When multiple shapes survive, capture them in a lightweight comparison table (trade-offs, complexity, which segments each serves) with a recommendation. The user decides.

Once the Overall Shape is locked, offer a quick mockup if the feature is UI-heavy (a new surface, a redesign, a flow). Not every shape needs one.

### Step 3: Stub the rest and write

Fill the doc per product-doc: the locked frame, the Overall Shape, Solution Details and Analytics stubbed with "...", Designs only if links exist, Open Questions from the bookmarks you kept throughout (deferred decisions, feasibility unknowns, non-goals with tension) plus a first-principles pass, and an Appendix with the research summarized and every source linked.

Run product-doc's quality check, then the cold read (Step 4), then present the draft for a final pass with the cold read's paraphrase and verdicts beside it, then write it where the project keeps docs. Update an existing entry rather than creating a new one when there is one. The same three writes close this phase: any raw research from shaping saved in the repo, one appendix line pointing at it, and Open Questions refreshed after the user's review.

### Step 4: Cold read

Everything above is the author checking their own draft, and the author can't see what the doc doesn't say. So before the user's final pass, three fresh `critic` agents read the exported doc and nothing else: no chat, no research, no reasoning (Model: critic role). They run in parallel and never see each other.

- **Paraphrase.** "Read this doc. Before anything else, write two sections of three to five sentences: 'What this proposes' and 'What's true today, per this doc.' No score, no findings." The lead diffs it against what was meant. A wrong paraphrase is a finding against the doc, never against the reader: it catches the doc whose terms are all defined but whose parts don't connect.
- **Premortem.** "It's six months after launch and this failed. Name the three most likely causes and the assumption in this doc behind each."
- **Design readiness.** "You're starting the design step from this doc alone. List every question you'd have to ask before drawing the first surface, and every place you'd have to guess." A question the doc should answer is a finding. One that belongs to design goes to Open Questions.

A wrong paraphrase is never rejected; the doc gets fixed, by rewording or cutting before adding. For the premortem and readiness findings, the lead writes a verdict per finding before revising: accepted with the change, or rejected with a reason the user could check (a call the user made, or a question that belongs to design). "That was intentional" isn't a reason; if the doc needed explaining, that's the finding. One round. Re-run the paraphrase alone if the revision touched the frame or the shape, and show the user the latest one.

## When to compress

Compress as product-doc's When to compress says, in phase terms: skipping the research tracks still runs Track 1, and a small bet does all three phases in one conversation with a cold read of the paraphrase alone.

## After the doc: resolving open questions

Offer this as a next step, in the same session or later. Walk the open questions one at a time:

1. Ask for the user's unbiased take first. Don't lead.
2. Propose a research plan for this question from the toolkit: codebase investigation, customer research, analytics, strategy docs, web research (10 to 15 examples of how others solve it), or first-principles reasoning when it's a judgment call and needs no data. Propose only what's useful.
3. Get approval. They'll cut sources, add some, or say "just reason through it."
4. Run it.
5. Present your take with evidence.
6. Compare the two takes. Where you agree, where you don't, and why. Push back if theirs doesn't hold up; be open to being wrong.
7. Draft a one-to-two sentence answer.
8. On confirmation, add it as an indented "your initials (date):" sub-bullet and move the question, number kept, to the Resolved toggle at the top of Open Questions (product-doc has the convention).

If neither that nor a mockup is wanted, name the recommended next step explicitly: build a prototype (validate the shape before committing eng), design (run design-shaping once the Overall Shape is locked; it fills Solution Details), instrument and measure (no baseline yet), or start building (validated, questions resolved).

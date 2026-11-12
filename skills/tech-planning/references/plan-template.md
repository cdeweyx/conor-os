# The tech plan: sections, records, milestones, the epic, the close

What each section must contain and must not become, the decision-record format, the effort scale, the round log, the product-doc summary, the epic, and the close checklist. Read once before drafting. Sourced from real design docs measured on their raw files (Rust RFCs, Oxide RFDs, KEPs, ADRs, Spolsky specs) and from what agent builds need.

Contents: sections · decision records · effort scale · risks · appendix and round log · the product doc's tech planning section · the epic · close checklist

## Sections, in order

Body under 2,500 words. Reasoning next to the decision it belongs to; trade-off mass lives inside the design, never in a trailing alternatives section (RFC 1522 spends 44% of its words on rationale nested in the design and 69 words on the mandated Alternatives section). Tables only where every row shares the same columns: option comparisons, the data model, the milestone list.

1. Problem and link. Two sentences and the product doc link. Not a restatement of the doc.
2. Constraints. The cost line, single or multi user, agent-built, design fixed, the interview answers. No time appetite: the whole design gets built and the milestones carry the effort. Not principles or values.
3. Scenarios. Three or four concrete runs through the system, one of them a failure ("Saturday morning, the daily import failed, what does the summary job do"). Not personas.
4. System context and data flow. One context diagram placing the external systems (sources, cron, notifier, host, app) and one flow from capture to result. Not a diagram set.
5. Components and what each requires. Each component, its inputs, outputs, and the technology it needs. This is the map for the reader and the layout for the epic. Not a tour of internal functions.
6. Data model. Tables, keys, grain, and the one-way-door reasoning with prior art, ADR-style. Not a schema dump.
7. Decisions. One-way doors first, each as a full record in the format below with rejected options inline in three lines each. Two-way doors as one line each (the decision sentence, what it serves, the door), with their full records in the appendix toggle "Decision records, two-way doors". Not an alternatives essay.
8. Risks. Each risk with a mitigation and a signal (how we'd notice), including the five ways this plan bites, each pinned to a component or a check. Not a list of worries.
9. Open questions. Quoted by the product doc's number and topic, each with the milestone or spike that resolves it. Not a parking lot.
10. Milestones. In order: milestone 0 is the walking skeleton, as two waves of one milestone: every shared contract first (schema, types, API shape, tokens, the `ui/` layer from hi-fi's spec with its `/dev/ui` route, the test harness, the workspace scripts), then the whole loop rough (every permanent table, adapter, and function the loop needs, the scariest computation included, with throwaway screens, so the user can feel the product and the ledger starts recording). Nothing else starts until it merges. Then by risk. This is the one definition of milestone 0; the skill and the epic point here. Each with a one-line done state, an effort tag with its risk driver, and a check. Not a Gantt, not hours.
11. Public later (zero-to-one's Personal mode only). The seams built in so Go live isn't a rewrite, one line each with the value it holds until accounts exist (tech-planning, Public later). Not Go live's features.
12. Deliberately left out. What could reasonably be in scope and isn't, and why. Not negated goals.
13. How we'll know. One observable per milestone. Not KPIs for a single-user tool.
14. Appendix. Toggles: the two-way decision records in full, the criteria and the three approaches compared, spike results, rejected candidates with the specific failure case, a "Round logs" toggle holding one nested toggle per critic round and one for the user's review, and after the epic is filed, the epic snapshot. Not required reading. Toggle shape for Notion: `<details>` on its own line, `<summary>` on the next, a blank line, the content, `</details>` on its own line; a one-line `<details><summary>` becomes literal text.

## Decision records

One per decision point, `D-n` in creation order, never renumbered, never deleted, only superseded.

- D-n, title as a verb phrase ("Choose the app layer").
- Serves: the open question number or the surface it serves.
- Context: the design constraint and the technical fact, two lines.
- Options: one line each, the neglected ones included.
- Decision, as one sentence: "Facing c, we chose o over p, to get q, accepting d."
- Why, inline, as long as it needs to be. This is where the trade-off lives.
- Rejected options, three lines each: what it optimized for, what it cost here, what would reopen it.
- Door: one-way or two-way.
- Confirm by: the milestone or spike that proves it (blank for two-way doors).
- Status, dated: proposed (round n) / decided (the user, date) / superseded by D-m. Old lines stay.

## Effort scale

Sized by what it costs the user, not the agent, and marked as the agent's read. No source gives a validated way to estimate agent work; wall clock breaks when the human multitasks.

- S: one session, one layer, the check exists. Review under 15 minutes.
- M: one session, two layers or a new check to write. Review 15 to 45 minutes.
- L: two or more sessions with a handoff, or a one-way door inside it. Review an hour plus, and a critic pass.
- Spike: unknown, timeboxed to one session, output is a decision not code.

Risk drivers, one per milestone: ambiguity, no runnable check, cross-layer integration, external API with limits, visual fidelity, numeric correctness. Anything L with a numeric driver gets golden fixtures written before it starts. A milestone that touches more than two layers or can't finish in one clean context is two milestones.

## Risks

Rank by chance it's real, cost if real, and how late you'd find out. The top risk gets action, not a table row: a spike before the plan is final, a place in the first milestone, or a line in deliberately left out. The five ways this bites (from Superpowers' Review Focus): the five input classes or failure modes the plan implies but no check exercises, each pinned to a component or a check. Greenfield failure classes to check against: premature done (a fresh evaluator, not the author), integration (skeleton first, features as user actions), data plumbing (exact commands named in the epic), numeric correctness (fixtures and a look-ahead test), design fidelity (tokens as the only source of values, a screenshot check per surface), drift (a unit fits one window), stubbing (the reviewer greps for placeholders).

## Appendix and round log

One toggle per critic round: `Round N, <date>, median <score>`. Inside: each finding as `[seat] [blocking | should | note] <finding> → accepted: <what changed, D-n, before and after lines> | rejected: <why>`, the debate verdicts if any, the score line. Nothing edited after the round closes; the next round is a new toggle. The before-and-after lines are the supersede chain: the record gets a new dated line, the old one stays, the round log points at it.

## The product doc's tech planning section

- A link to the plan.
- A decisions toggle: one line per decision point, the decision sentence, linked to its D-n.
- A milestones toggle: the order with the check per milestone.
- Open questions stay in Open Questions. Each plan record names the question it serves; each doc summary line carries the record ID, so a superseded decision stays findable from either side.

## The epic

Written after the user's review as a Linear project, for the build skill's milestone lead, which dispatches a fresh implementer per issue with the brief as its only memory. Linear is the only todo list; the repo keeps no feature list of its own, because two lists drift and nobody knows which is true. Issue status replaces a `passes` flag and a progress file: Done on merge (a PR with `Fixes <ID>`) is automatic, and the build lead moves the rest.

- Project: a short description (Linear caps it at 255 characters) and the long text in the project content: links to the tech plan and the product doc, the branch and PR conventions, the standing rules. The user may rename the project; query it by id afterwards.
- Milestones: one per plan milestone, in order, each with its check in the description. Names capitalized and terse, no "the": "M1: Results Panel and Tokens", "M2: Saving and Library". A milestone added after the first filing sits in plan order, right after the one it follows: set its `sortOrder` between its neighbors' values in the same turn it's created. The MCP's `save_milestone` can't set `sortOrder`, so use Linear's GraphQL `projectMilestoneUpdate` with a personal key, or ask the user to drag it, and list it in the filing summary until it's in place (user: "whenever you create new milestones in Linear, make sure you put them in the right order"). No sub-milestones: a phase inside a milestone is a wave of issues, not a milestone, as milestone 0's two waves are (Milestones, above). Parallel agents that each invent a contract conflict about twice as often. The scaffold issue creates a stub for every module a later wave calls, with its final signature and return shape (a router calling `health()` before anyone owned it, a lookup with no return type), so a fan-out wave fills bodies and never invents a seam; one seam read found four blockers, all of this kind.
- Issues: one PR each. Titles capitalized, terse, no "the", the outcome in a few words ("Dashboard shows this week's invoices with due dates"); the brief carries the detail. Every issue assigned to the user, with a priority from the agent's read on build's scale (build SKILL, Keeping the tracker true), in the team's Todo state by default (the user moves things to Backlog as it makes sense). The project's ordering is manual, so set each issue's sort order to the plan's order within its milestone. Blocked-by relations set the waves: three to five issues per wave that share no files and don't depend on each other; serial waves chain issue to issue.
- A surface that spans milestones (the page in one, the behavior behind its main action in a later one): the earlier milestone's issue names the interim state and owes its design, what the control does until the later work lands, never a dead button. One home screen's main button had no job between its page in one milestone and the parsing behind it in the next.
- Guardrails follow the build's phases (build's `references/project-setup.md`, Guardrails, says what milestone 0 gets); hard locks (protected goldens, unlock notes, deny rules) are their own issue in the milestone where the numbers are confirmed or the product goes live.

Each issue's body is the brief:

- Context: links to the D-n records it implements, the product doc section, and the artboard. Link, don't restate; the reasoning has one home.
- Owns: the files or directories it may change. Doesn't touch: its neighbors in the same wave.
- Interfaces: what it consumes from milestone 0 or an earlier issue, and what it must expose.
- Done: three to seven checkable criteria as the end state, the check the build runs (the exact command, or the screenshot check), and the constraints that mustn't change on the way.
- Out of scope, one line.
- Labels: one type, one effort label, and a risk label where one applies, as build's Filing defines them (build SKILL, Keeping the tracker true). Bias toward small: when an issue could ship as two PRs that each work on their own, file two. It's a lean, not a rule; work that can't split cleanly stays one issue, since a forced split leaves seams that cost a close issue. Big issues are where implementers' context runs long, and long runs cost the most and needed the most review rounds. Calibrate against built line counts, not feel: on one build, eleven issues planned as Small came in at 434 to 2,039 changed lines, so a surface issue is Medium at least. `Chore` is a type for miscellaneous work, not a size: a chore still carries an effort label, usually Small.

File through the Linear MCP, or through Linear's GraphQL API with a personal key when the connector isn't loaded in the session (connectors load at session start; a key goes in a gitignored file, never a commit). Parse the epic document into milestones, waves, and issues, create labels, project, milestones, issues, then relations from the wave lines; keep the draft-key-to-Linear map in the repo. If something can't be set, list it for the user rather than folding it into the body. The user's review is this step's gate; once filed, every issue is ready to build, and build doesn't wait on a per-issue read.

Around the issues, in the repo: fixtures with hand-computed answers for every formula and a look-ahead test, written before the engine milestone; a screenshot check per surface against the canvas export with an agreed match threshold; a Stop hook that blocks the session until typecheck and lint pass, never the tests (the build runs the full check once per merge batch), with the rest of build's hooks (build's `references/project-setup.md`, Guardrails); boundaries in three tiers (always, ask first, never); and a CLAUDE.md under 4k tokens where every line traces to a mistake. CLAUDE.md carries the standing rules so every session gets them: build's machine rules and not-evidence list (build's `references/project-setup.md`); the library mismatches in `libraries.md` (no hand-rolled toasts or dialogs, no 1,000-row list rendered whole, primitives only through `src/ui/`); one issue per implementer; the PR body carries evidence (the command and its output, or a screenshot) and `Fixes <ID>`; a brief that turns out wrong gets a comment on its issue, and new work becomes a new issue (assigned to the user, in Todo), never an extra change in this PR; two corrections on one issue means clear and rewrite the brief; plan and build never share a window.

Snapshot the milestones and issue titles into the plan's appendix as "what we thought the epic would be"; Linear is live.

## Close checklist

- Every D-n is decided or superseded; none left proposed.
- Every open question is resolved with a dated answer, parked with the surviving goal and a revisit condition, or named in a milestone. Nothing left as "explore in tech planning."
- The "for tech planning" toggle is empty; its items became D-n records.
- The tech planning summary matches the plan's current decisions (re-read both).
- Old names swept from overall shape, the appendix, and any spec line an answer touched.
- Every round log closed with a verdict; no change without a D-n.
- Plan linked from the doc, doc linked from the plan.
- Checkpoint done: what the rounds changed about the process, into SKILL.md.

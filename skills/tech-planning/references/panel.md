# Lint, the critic panel, and the debate

Read before the lint pass and the critic rounds. The evidence: self-review is close to worthless, copies don't help but differences do, and judges are anchored by prior scores and biased toward length and their own text. So every critic is a fresh context with inputs the author didn't use, sees no prior findings, and reports in a fixed shape.

Contents: lint · paraphrase gate · seats · critic prompt · author verdicts · rounds and convergence · debate on forks · biased planners · seam read · rules learned

## Lint, before any critic

Mechanical, fix what fails:

- Reasoning sits next to every decision; no trailing alternatives section.
- Every risk has a mitigation and a signal.
- Every milestone has a done state, a check, an effort tag, and a risk driver.
- Every product goal maps to a milestone; no milestone serves a non-goal.
- Every "for tech planning" item became a D-n.
- No file names in the body.
- No open decision inside a milestone.
- Body under 2,500 words.

## Paraphrase gate, after lint and before round one

A plan can pass lint and every seat while its parts don't connect, because each seat reads for its own question. One fresh `critic` gets the plan file alone (Model: critic role):

> Read this tech plan at [plan path] and nothing else. Before anything else, write two sections of three to five sentences each: "What this builds and how the pieces connect" and "What exists today, per this plan." No score, no findings, no gaps filled with a guess.

The lead diffs it against the plan's intent. A wrong paraphrase is a finding against the plan: fix the plan, not the reader, then re-run the gate with a fresh critic. Only a right paraphrase goes to round one. Wrong twice means the plan's structure is the problem: show the user both paraphrases before any more rounds. (From the Elephant-Goldfish model's comprehension reviewer.)

## Seats

| Seat | Sees | The question it answers |
|---|---|---|
| Complexity skeptic, also the estimator | Plan only | What can be cut or deferred without losing a goal; where the effort is dishonest |
| Engine reviewer | Plan plus the engine research | Is the engine right: its math, its edge cases, the data it needs |
| Design-fidelity reviewer | Plan plus DESIGN.md and the surface specs | Does the stack honor the handoff; which surface, state, or motion can't be built as specified |
| Product reader | Plan plus the product doc | Does every goal have a milestone; does any milestone serve a non-goal; which open question is silently answered |
| Premortem | Plan only, framed as "it's month three and this failed" | The three most likely causes and the assumption behind each |

Model: critic role for every seat, so the critics run on a different model from the author on the planner role.

## Critic prompt

Give the critic the artifact and its inputs for that seat, nothing else, and this shape:

- A readiness score 0 to 10, used only by the orchestrator, never shown to another critic.
- At most three findings, ranked, each tagged blocking, should, or note, each pointing at a section, each naming the goal or assumption it serves.
- One line: what would change my mind.
- A declined-to-judge list, so nothing is dropped silently.
- Flag only gaps that affect correctness or the stated requirements; a reviewer asked to find gaps will find some regardless. A finding that names an ambiguity a build agent would trip on ("which table does scoring write to") outranks taste. Prefer removing over adding; an addition counts against the finding.

## Author verdicts

The lead writes a verdict per finding before anyone revises: accepted, with the change and the D-n it touches; accepted in part, with the rejected half and the criterion it lost to; or rejected, with the reason. The lead checks facts against the lane reports (a critic without the lanes can be wrong on a fact) and reads each critic's declined-to-judge list, which is a second source of findings. Then the planner applies the verdicts. Critics on the critic role can't write files; the lead assembles the round log from their replies. A stated rationale never downgrades a finding on its own; a rejection needs a fact the critic didn't have or a user call it contradicts. Rejected findings stay in the round log so the user can see what was refused, not just what changed.

## Rounds and convergence

- Round one: five independent critics on the draft.
- Round two: five fresh critics on the revised plan, plus one scoped re-review that verdicts round one's blocking findings addressed or not addressed.
- Round three: only for decision points still open after round two, as a debate (below).
- Cap three. Stop early when no blocking finding is unanswered and the median score is 8 or better, or when a round moves the median under a point without producing a blocker. A round that holds the median but finds new blockers isn't done: one round's fixes expose the next round's gaps.
- Forks that are the user's value calls (cost, a licensing stance) aren't debated; they go to the review with both cases. Round three is for forks critics can settle on facts.
- The scoped re-reviewer may add one line beyond its scope when it sees a contradiction the fixes left behind.
- A round-two critic re-flagging a round-one rejection is the stop signal, not a reopen; the rejection stands unless it brings new information.
- A finding that contradicts a call the user made wins for the user; log the finding and the call it lost to.

## Debate on forks

Independent review by default, because critics who read each other anchor and collapse toward the majority. Debate wins only where a judge picks between two argued answers, which is the shape of a fork, not of "is this plan good." For each fork still open after round two: two critics assigned opposite sides with the same inputs, one exchange each, a fresh judge who never saw the plan's recommendation writes the verdict. The verdict goes into the plan's D-n, or the fork goes to the user with both cases attached. One exchange, not a loop.

## Biased planners

For the approaches step, three planner agents with the same inputs and criteria and one bias each, set in the prompt:

- Minimal: the fewest moving parts that meet every given; cut anything no given or constraint forces.
- Clean: the shape that's easiest to change in month three; seams at every swap point.
- Pragmatic: the most boring choice at every two-way door, novelty spent only where the product is novel.

Each returns one whole-system approach argued on the criteria, with its own weakest point named. The lead compares, picks, and writes the loser lines.

## Seam read, before the epic is filed

The panel judges the plan; nobody reads the briefs as a set. One `critic` does (Model: critic role), once, after the epic draft is written and before anything goes to Linear. Critics can only Read named files, so dump the plan to a file and give both exact paths. No score and no second round: the lead writes a verdict per finding, fixes the briefs, and files.

> You're reading an epic before it's filed, in a fresh context. Inputs: the tech plan at [plan path] and the epic draft at [epic path]. A fresh implementer will build each issue with its brief as its only memory. Find where issues meet and the briefs disagree or go silent: an interface one issue exposes that another consumes under a different name or shape; a seam with no failure contract (what raises, who catches, what the user sees); two issues in one wave owning the same file; an issue consuming something no earlier issue exposes; a decision record no issue implements, or an issue making a decision no record made; a done criterion with no runnable check. At most seven findings, each tagged blocking or should, each quoting both briefs or the record. Don't judge the plan's decisions; the panel did. End with a declined-to-judge list.

## Rules learned

Rejected and recurring findings become rules here, one line each with the plan that produced them.

- One failure, one answer. A fix that adds a second answer for the same failure (a redraw from the last pull, a fallback source that also renders) gets caught the next round. Name the one artboard or state a failure renders.
- A seam with one implementation isn't a seam. Every adapter interface ships with a recorded fixture and, where a real second source exists, a second implementation; otherwise name the fallback and don't build it.
- Re-read the data model after any formula or sequencing change. A scoring-formula fix revealed a missing column on a flag; a sequencing fix revealed a missing component for items with no result yet.
- The premortem earns its seat: both rounds it found the gap the partitioned seats couldn't see (a broken data source reading as no new activity; no feature row for items with no result yet). Keep it plan-only.
- A "fail visibly" call has to survive every client's success test. One client showed "Saved ✓" whenever `error` was missing, so a 404 or an HTML error read as success; the fix was success only on an explicit `ok: true` and JSON on every status. Ask the premortem to check each client's success condition.
- A user's "no retry" applies to every path unless they scope it. Round 1 removed a retry from the response path; round 2 found one still in the background task.
- Lighter panel for a small tool: one planner and three seats (skeptic, product reader, premortem), two rounds, found three blockers a round. Worth it even at this size.

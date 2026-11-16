---
name: build
description: >
  Runs one milestone of a filed epic as a lead that never writes code:
  a fresh implementer and an agent review per issue, each issue PR merged
  into main on Ready, stopping only for what needs the user. zero-to-one's
  build step in either mode and Go live's Quality hardening close. Use when the user says "rip M0", "run M3", "run
  the milestone", "start the build", "build the epic", "next milestone",
  "harden it", or asks where the build stands. Do NOT use to plan or file the epic
  (tech-planning), for a one-off fix outside an epic, or for the
  post-build stress test (break-it).
---

# Build

One lead per milestone, one fresh implementer per issue, agents reviewing every issue PR, and every issue merged into `main` on Ready. Milestones are planning only: grouping, order, waves. The user's judgment goes to the few calls where a wrong one compounds (When to stop) and to the running product whenever he looks, which never blocks. Everything per-issue goes to agents, behind checks they can't fake. The ledger and `git log` are the lead's memory, over recollection.

Read `references/learnings.md` every run, `references/loop.md` before the first dispatch, `references/brief.md` when writing a brief, `references/prompts.md` at the step that sends each prompt, `references/gates.md` at a gate or an unlock, `references/ledger-template.md` before writing the ledger, and every other reference at the step that names it. `references/learnings-archive.md` holds run history and the dated stories and quotes behind these rules; read it only when diagnosing a repeat. Before a project's first milestone, run `references/project-setup.md`.

## Process weight

The project's `docs/build/README.md` sets the weight. Get it running and right first; production checks wait for launch:

- **Pre-launch weight,** the default for every build until the hardening close: no readiness read or approach review, except one cold read on an `Effort: Large` issue; one combined reviewer per PR, with a validator only for a P0; P2s logged, not fixed; issues that share no files built in parallel; the lead's own run of the check on the head counts as the stamp; the light close at each milestone (`references/close.md`).
- **Full weight,** from the hardening close on (zero-to-one's Quality step, which flips the README), or from the start on a product with real users: the readiness read and Approach review, pr-review's sized reviewer set and validators, P2s fixed, a hardening close at each milestone.

At either weight, an issue on a one-way door or the user's data and secrets gets pr-review's full reviewer set and validators (the project's README names those guards). Start light and add a step back only when a real miss shows it would have caught something, logged as a ruling with the miss that earned it. At pre-launch weight, skill learnings fold in as they come (a small edit to the owning skill the same session, logged under the ledger's "For the skill"), and the full skill pause runs once at the end of the build, filed as a tracker issue in the last milestone.

## Roles

- **Lead:** the main session (Model: main chat). It doesn't write, read or paste product code, since that fills its context and spends the fresh read the reviewers give. Two exceptions: its docs (`docs/build/`, and the CLAUDE.md and review-rules edits the skill pause makes), and a reviewed patch it applies under an unlock (`references/gates.md`). Its doc and ledger edits land on `main` through the merge script's docs-only path (`references/project-setup.md`), one docs PR per merge batch, between merges or with the close issue, never into a tree an agent is using. It holds the issue order, the ledger path, the base sha and open findings, and uses git, gh, the project's scripts, and the Linear, Agentation and Paper MCPs.
- **Implementer:** a fresh `worker` per issue (Model: worker role) with the brief as a file, CLAUDE.md and the loop's prompt.
- **Reviewers and validators:** whatever `pr-review` dispatches (Model: worker role).

## The run

1. **Progress map.** Milestone, issues done and left, the next gate. Answer "where's the build" the same way.
2. **Load.** This skill's learnings, the project's `docs/build/README.md` (process weight, gates, owed inputs, merge script, review rules), CLAUDE.md, the previous milestone's ledger ("For the skill"), `git log`. List the rules that apply before the first dispatch.
3. **Preflight.** Every check in `references/preflight.md`. A missing input blocks only the issues that need it: ask for it and go on with the rest, without asking. Issues on the same screen are grouped by surface (one branch, PR and review); two branches never accept the same baseline in one milestone.
4. **Work the issues.** The loop in `references/loop.md`: brief to file, a pool worktree, the readiness read and approach review where they apply, implementer, `pr-review` on the pushed head alongside its one stamped check, the PR into `main`, the fix rounds (Standing rules), the merge script on Ready, a ledger line, and the full check on `main` once per merge batch. Until the merge script exists, squash-merge on Ready and say so in the ledger.
5. **Gates.** When an issue hits a When to stop item, or the README names a gate after the issue that just merged, post the gate note (`references/gates.md`) in chat and on the issue, move the issues behind it to Needs Review (a merged issue stays Done), and go on with the rest. No objection to a gate note's questions counts as go; it never stands in for a yes the unlock needs (`references/gates.md`). During a gate he runs live, hold merges that change the surface under test until its steps finish, since a merge mid-run changes what he's testing. A ruling that changes a protected golden gets its unlock note the same turn. A spike's gate note asks the user about every product call its rubric grades as right.
6. **Close.** `references/close.md`, once the milestone's issues have landed: the light close before Quality, the hardening close at Quality and after. Pinned at the last issue's squash commit, over this milestone's work only, blocking nothing. Findings go into **one close issue**, fixed there or killed with a reason, never parked forward. It ends with the digest and the where-to-look post.
7. **The user's look.** `references/review.md`. He looks when he wants, from the where-to-look post, and nothing waits on it. Take a position in chat on each of his notes and file the agreed ones the same turn as ordinary issues the run picks up.
8. **Skill pause.** Fold each "For the skill" line into its conor-os skill in the session it's logged, at any weight. Every handoff to another session is a skill pause too: run the pause before writing the handoff, and end the handoff message with the next session's opening prompt as one copyable fenced Markdown block. So is the end of a thread a session owns (a design loop's lock, a side quest's last step): fold its learnings in that turn and list them, unasked. Then, at milestone close: `references/pause.md`, at each milestone's close without holding the next one (pre-launch weight: once, at the end of the build): fold the "For the skill" lines that hold, sort his corrections, prune, cold-read, show edits with cuts beside additions, push on his yes.

## When to stop

The user's gate is tech planning; once the epic is filed, the build advances every issue it can. These wait on him, each with its ask in Needs Review, and the lead flags them at filing or dispatch so the ask goes out before the work arrives. A flagged issue still builds and gets reviewed; only its merge, and the issues behind it, wait for his answer:

- **A one-way door:** a schema change once real data sits on it (before launch, additive schema is a standing approval), auth and secrets, deleting stored data, anything that spends money, a public name.
- **The first look or product rule** later issues build on: a new surface's direction, a rule about what the product counts or shows.
- **A stuck issue:** a `needs-human` PR, a wrong brief, a missing input, a golden change with no allowance from him in so many words, an irreversible or outside-the-worktree action, a plan where every path is a guess.

Everything that doesn't depend on him goes on, and a gate the README names holds only the issues behind it. An open ask never idles the run. The run ends at a stop he named (a milestone or an issue) or when nothing left can move. Everything else is a ledger ruling (decision, why, cost if wrong), and the run goes on without him. One exception: a reviewed fix to a protected harness file waits for his yes, then lands by the unlock (`references/gates.md`).

## Standing rules

- **Never ask the user to unblock the build by hand** (a git chore, a command, a restart), except a resource only root frees (leaked POSIX semaphores): ask once with the exact command and file the harness fix the same turn. Take the machine as it is; when it's loaded, serialize (one check at a time, every test run in the lock) and tell him once.
- **The machine rules bind the lead too.** The project's CLAUDE.md carries them (no clones or temp copies, worktrees under `.claude/worktrees/`, kill by PID, the lock, one blocking wait; `references/project-setup.md`). A broken environment (moved repo, broken worktree links, "* 2" sync copies, a dead skills or agents symlink) is the lead's to repair in place and log, without asking.
- **A second opinion is a reviewer agent,** never the user.
- **Never run under `/goal`;** it pushes past a gate that ends on a question.
- **Fix rounds:** this is the one home for the count. Two fix rounds, then `needs-human`; a third, targeted one only as a logged ruling when findings converge and he wants the result by a deadline, and never a fourth. Past about 250k tokens of implementer context, or on a Small issue, the next round goes to a fresh one from a handoff (`references/loop.md`, step 9).
- **A standing golden allowance** goes into the unlock note word for word; every moved golden is explained in the PR, and the before-and-after table opens the digest.
- **Research inside a milestone,** when a question undermines its data: preview the lanes, run them, file issues (in this milestone if he asks), and re-check his earlier approvals against the result before merging them.
- **A wrong brief** gets a comment on its issue; the new work is a new issue, never extra change in the PR, parked if nothing depends on it. Two corrections on one issue means rewrite the brief.

## Asking the user

He reads asks in Linear and GitHub, away from the chat. Every ask (gate note, Needs Review comment, `needs-human`) opens "Decision needed from you: …", then "My take: …", then evidence; a note needing nothing opens "FYI, nothing needed". A question stands alone: the proposal in the message, a screen claim with its shot, and a direct link to the exact place (Paper page, PR, local URL) every time something is mentioned.

**Options in plain words.** Each option is one plain sentence of what the user sees or does; shorthand ("call 1") gets "what are you saying".

**Answer his questions first.** A turn that also reports status opens with direct answers to every question he asked since the last reply, before status and tables; an answer buried mid-message reads as no answer.

**The answer goes last.** In Conductor the user sees only the turn's last message, and a decision or answer written before more tool calls is collapsed and lost, so every decision, answer and gate goes in the turn's final message.

**A question isn't an instruction.** When he questions a call, answer with the position and its reasoning first, and change the call only if the reasoning breaks, never to fold to his lean.

Decisions use the global CLAUDE.md's "Decisions for you" table, opening the message when there are two or more, its lean column the lead's take. Build adds: the where-it-lands column is a direct link; options are lettered with the lean marked, so one reply code answers ("1A 2 yes 3 no"); options he must see are drawn first on a page made for the decision, one labeled frame each, differing only in what's decided and named as the message names them (rough HTML is fine). Decided and coming go below the table, apart. Right above the table, one line names where to look: the file and the page by name, each a direct link, plus which row or board is which.

Every open decision also sits in the tracker's waiting-on-the-user status (the waiting status: Needs Review in a build project's lifecycle, Waiting on Me in an improvements project), since one asked only in chat gets lost: a comment @-mentioning him on the existing issue whose work it changes, that issue moved to waiting, linked from chat. Never file an issue just to hold one. When he answers, reply in that decision's own comment thread the same turn, quoting his words, the decision, and what it changed (the issue, PR or rescope), so the issue reads as decided without the chat. Waiting is only for an issue blocked on the answer; a shipped issue goes to Done and its leftover decision moves to the issue that acts on it, or the digest. Say it plainly: the problem in one example, the fix and what it changes, the alternative, what parking it costs. No internal labels ("b2", lens names).

## Keeping the tracker true

**Filing.** This is the home for the build's priority scale and label set (global CLAUDE.md says which fields every issue needs, and a hook blocks a create missing one); tech-planning files the epic by it too. Every issue gets a priority (High for anything other work waits on: the walking skeleton, one-way doors, close, review and blocking fixes; Medium for surfaces, features and bugs nothing waits on; Low for backfill, parked niceties, and setup nothing needs yet, such as hosting before launch; never blank), one effort label, one type label, a risk label where one applies (`Touches Data`, `One Way Door`, or the team's equivalent), so the risk shows at filing (pr-review gives a one-way door its full reviewer set), and starts in Todo, Design Needed issues included: an issue moves to In Design only when its design loop actually starts. `Effort: Small` is one layer, a copy or config fix, a one-line engine change, most chores (under ~300 changed lines); `Effort: Medium` one component, endpoint or feature across one or two layers with tests (300 to 1,500); `Effort: Large` a surface or subsystem across layers, several seams, or a data build. Type by intent: `Feature` (new capability), `Improvement` (works, should be better: polish, copy, UX, design revisions), `Bug` (not what the spec or data says), `Chore` (upkeep), `Spike` (research to pick an approach). Every issue has a milestone, never none: work no current milestone will pick up goes to a later milestone or the project's catch-all one (an improvements project's "Later"), never a milestone-less Backlog. A dev-loop or harness fix found mid-run (a flaky spec, a slow check, a script bug) goes into the current milestone and gets worked there, not parked in the improvements project, which holds only what the user chose to punt, new features not being built now, and other work that can wait. A problem he reports outside a build (a bad row, a missing image, "worth looking into why") gets an issue the same turn in the project's improvements project, filed by these rules, and moves across the board as the work goes: In Progress while investigating, the waiting status with a decision comment when the fix is his call, then the normal PR lifecycle.

**The Design Needed test** is the lead's call at filing, from any source, never left to the user. A new element, one moved or resized enough to change what reads first, a new layout or hierarchy, or a change to what a page says at a glance gets the Design Needed loop in Paper first, however small. Another row in a designed pattern, a tweak inside the scale, a swap between tokens, a copy fix, or a bug back to spec builds from code, which wins over Final until the hardening close's Final pass draws it in. Neither waits on his review. An issue that still asks what to build, not how it looks (a first-run experience, a magic moment, a new flow whose steps aren't settled), is shaped before its loop: the design lead proposes a shaping process (product-shaping's phases, research lanes, the gates) and he okays it before any framing ask or round.

**Scope changes** (a ruling, a folded finding, a corrected number) update the title, description and effort label the same turn; re-size at dispatch and at merge against real changed lines. The title says what the issue does now, and a dated line atop the description says what changed and why. He reads the tracker, not the ledger, merged issues included.

**Designs drift too.** When a ruling or fix changes a surface's layout, or he sets a rule for surfaces, sweep the same turn: every Final artboard, motion strip or spec and unbuilt brief it touches or breaks gets a dated line and the Design Needed label (a Done issue gets a new Design Needed issue in this milestone).

**Final is the source of truth** for how a surface looks and moves, except a code tweak until the hardening close's Final pass. A cited motion spec is read against Final at dispatch, and a moving element is pinned by frame-sampling tests, never one still. One element, one look: a pick moving to Final updates every artboard that draws it, and the hardening close repeats it as the element sweep (`references/design-loop.md`).

## Approach review

The brief says what, where and how to tell it's done; the implementer picks how. Where how is a real choice, a wrong pick costs a review round or a close issue, so at full weight it gets a tech-lead review before code. The lead flags it at dispatch, whoever filed the issue, when any of these holds:

- It touches the schema, a shared contract (API shape, store, a type other issues read), or a decision record.
- It changes how two issues or modules meet: what raises and who catches, which side computes a number.
- It adds a dependency.
- It's `Effort: Large`.
- The lead can name two plausible builds.

The approach is the first look at an issue's real size, so the ruling carries tech-planning's lean toward small issues. When the accepted approach reads as more than one PR's worth and each part can ship on its own, lean toward splitting it as a ruling: the approach implementer builds the first part, and the rest become new issues in the same milestone, each built by a fresh implementer from the parent brief's "Approach (accepted)" section. They get no second approach review, even when a part hits a trigger, since the accepted approach already ruled on it. A lean, not a rule: keep it whole when a split would leave half-built seams. Every part one implementer builds stays in its context, and long contexts are the costliest runs.

An issue above Small that changes no screen first gets a researcher lane on the repo's own evidence: is it worth building at that size (Model: researcher role)? A Large implementation issue added after tech planning (from shaping, a review, a spike, or re-sized at dispatch) goes to the planner role first: a tech plan scoped to that issue, one cold critic, then the split into sub-issues as necessary, filed under it, before any dispatch (Model: planner role). A Large design issue gets the same pass once its design locks and it moves to implementation. The approach-step split stays as the backstop for anything that grows mid-build. A Large issue that still reaches dispatch whole gets a cold readiness read; Small and Medium get the lead's own check; no trigger means straight to code. A flagged issue's implementer returns an approach for a fresh tech-lead review, then builds the accepted one, which the issue review judges against. Unsettled after two rounds means the brief is wrong. Steps: `references/loop.md` 3a and 4a.

## The lead's own calls

**Ask-first means the user,** given anywhere: on the issue, relayed by another lead, or standing for the milestone. A standing approval covers in-scope items the branch can undo (fixtures re-recorded from scripts, tokens via DESIGN.md, additive schema, harness chores, a test the issue retires), never a golden, a one-way door or a dependency: a golden moves only under an allowance he gave in so many words (Standing rules). Anything else gets a one-line ask at dispatch (item, reason, your take) while work goes on. Log each approval in his words, list standing ones in the digest under "Ask-first items I approved without you", never re-ask, and carry approved actions out yourself; a hook that blocks the usual command for an approved action gets the plain equivalent, said in the PR (the lead's one exception to the machine rules' blocked-command rule), except the machine rules' own denies (kill by name, rebase, force-push, clone), which each name the command to use instead, and a merge: the merge script is the one path into `main`, and no agent merges around it.

**Short-term calls are the lead's:** which issue a change lands in, wave order, shipping what only works once a later issue lands. Decide, log, put it in the digest. Ask only for what When to stop lists; a conventional control isn't a product rule.

**Risky rulings get a reviewer.** A ruling that moves a decision record, changes a shared contract, or predicts the data goes to a fresh reviewer (Model: worker role) with the record and the code or data that could prove it wrong, before any brief; its findings get verdicts like any other.

## What counts as proof

A claim is never proof, whoever makes it. The project's CLAUDE.md carries the not-evidence list (`references/project-setup.md`); a gate note, ledger line, digest or ruling whose only support is on it says "unverified" until the lead has the proof.

## Design loop

A Design Needed issue runs hifi-design's loop in its own design-lead session (nudge the user to open it): Full for a surface whose new direction later issues build on, whose direction pick and ready review wait on the user; Quick for the rest, which locks on the lead's pick and rides with the milestone's look. The built surface scores at least as well as Final before merge. It carries the Design Needed label, waits in Todo, and moves to In Design when its loop starts. Read `references/design-loop.md` when a loop starts and when a pick moves to Final.

Every PR that builds or changes a designed surface carries a side-by-side for each state: the Final frame exported from Paper on the left, the built page at the same size on the right, one image per state, in the PR body and in the message that shows the user the work. The brief asks for it, and a difference kept on purpose gets one line under its image.

Mid-build design feedback outside an issue's gate becomes an issue when it changes a constraint, otherwise a line in `docs/build/papercuts.md`, never a fix in an open PR (`references/design-loop.md`). His notes after a look follow `references/review.md`.

## Parallel work

Always go as fast as the work allows: dispatch every unblocked issue that shares no files with running work, grow the pool to fit, and plan the next wave (planner passes, briefs, research) beside the build. Issues sharing files stay serial; review and merge stay serial through the lead. Milestones may overlap, since everything lands on `main`. Read `references/parallel.md` first.

## Checklist

- Preflight ran; the demo script exists and was posted.
- Every merged issue has a Ready verdict on its stamped head and a ledger line; every merge batch, a green full check.
- Every Large issue had a readiness read and, at full weight, every flagged issue an approach review before code, kept on the issue, every risky ruling a reviewer.
- The lead never edited a product file; every stop was a named reason.
- At the hardening close, the Final pass caught Final up with every code tweak, then one pixel sweep.
- The where-to-look post went out with the digest, and at a hardening close the demo script ran clean first.

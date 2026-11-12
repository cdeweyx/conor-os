# Agent prompts

The prompts the loop dispatches (`references/loop.md`), plus the PR body. Read at the step that sends each one. Fill the brackets; keep the rest. Machine rules (processes, checkouts, merging, ports, the check lock, waiting, output) live once, in the project's CLAUDE.md (`references/project-setup.md`, "The machine rules in CLAUDE.md"); the prompts point there instead of restating them.

## Implementer prompt

Step 4, and every resume that builds.

> You're implementing [one issue, or the issues of one surface group] in [repo] on branch [branch], which is based on `main`, in the worktree at [pool worktree path]. One rule first: stop only processes you started, by PID (capture `$!` at launch, then plain `kill <pid>`), never `pkill`, `killall`, a kill by pattern, or `kill -9`. Then read `CLAUDE.md`: its machine rules apply to you, with their reasons (no clones, extra checkouts as worktrees under `.claude/worktrees/`, merge never rebase, your own port, the check lock, one blocking wait and never a monitor, quiet output). Then read the brief at [brief path, or one per key], then the files it names. Build exactly what the brief asks, in the files it says you own. A section the brief names comes from the file it names; a section you need that has no component or block there is a question for the lead, not a rebuild, and so is new state or a mechanism the brief doesn't name (a flag, a stash, a round trip): name the existing pattern you'd use instead. Write the tests its done criteria name, and make them check real results, not that a mock was called. Never edit a golden, a baseline, or a protected file to make a check pass; if one looks wrong, stop and say why. Don't widen a tolerance, skip a test, or touch files outside the brief unless the brief says so; if you have to, say which and why. Numbers in the brief are the spec: if the data gives a different number, report it and why, never tune the code to hit it. Pin an edge state (a popover, hover, error, thin data, loading) with a behavior test that asserts what's on screen and where (DOM, computed style, positions in page coordinates, frame sampling for a transition), never a new screenshot; a new baseline is only for a new surface's main state, which joins the project's key-screen list. While you work, run type checks, unit tests and the browser specs for your own surface, nothing wider, and never the gate-0 target (the milestone close runs it). Run a new browser spec once with the dev server's cache cleared, since a test that passes warm and fails cold is a bug, and repeated three times only when it touches timing or a route in flight. Break the code to prove a test only when the test asserts something doesn't happen or nothing moves, and say in your report that it failed. Commit and push as you go; a branch with no pushed commit counts as no work. When the work is done, commit the test-count ratchet, push, and report with "Check: pending"; the lead starts the review then and resumes you. On that resume, run the project's lint target first (a stamp that goes red on one lint line wastes a lock slot), then the affected check, or the full check when the brief says the PR stands alone, once on the head you handed back; that run stamps the head the lead merges. Paste its tail.
>
> Report in at most fifteen lines:
> Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED
> What you built (one line per done criterion, with the test or output that shows it)
> Files changed outside the brief's Owns list, and why
> Decisions the brief didn't make, each with the reason
> Concerns or questions
> Check: pending, then the last lines of its output after the resume
>
> You don't open the PR or merge; the lead does.

## Handoff prompt

Sent to an implementer past about 250k tokens of context, or to a Small issue's medium-effort implementer, before its next fix round goes to a fresh one (loop step 9).

> Before a fresh implementer takes the next fix round, write a handoff of at most one page to [handoff path] and stop. What's built: one line per done criterion, with its test. The confirmed findings to fix, each as given. Where things are: the worktree path, the branch, the head sha (pushed), the test files and how to run them. Decisions you made that the brief didn't, each with its reason. Don't fix anything in this turn.

## Readiness prompt

Loop step 3a, `Effort: Large` only.

> You're about to implement one issue with its brief as your only memory, in a fresh context. You're read-only: don't edit, stage, or commit anything. Read the brief at [brief path], `CLAUDE.md`, the decision records the brief links, and the files the brief names, nothing else. Don't plan the build. Return two lists. Choices: every decision you'd have to make that the brief doesn't make, each tagged with the trigger it touches (schema, a shared contract, a decision record, how two modules meet, a new dependency, or two plausible builds that differ beyond this issue) or "none". Unresolved: every name, file, record, artboard, or field the brief cites that you couldn't find or that means two things. Each item quotes the brief line. Nothing else.

## Approach prompt

For a flagged issue, sent before the implementer prompt (loop step 4a).

> You're planning one issue in [repo] on branch [branch] before anyone writes code. Read `CLAUDE.md`, the brief at [brief path], the decision records it links, and the code it touches and the code around it. Don't edit anything yet. Return the approach in at most 25 lines:
> Files: each one that changes or is new, with a line on why
> Data flow: the path from input to the table or the screen, naming the functions and fields
> Reuse: the existing code, component in the project's UI layer (CLAUDE.md names it), or library this builds on, and what you checked so it doesn't duplicate something; a style block another feature already has gets extracted into the UI layer first
> Contracts: what it consumes and exposes, and the failure contract (what raises, who catches, what the user sees)
> Tests: what the done criteria's tests will check, against real results
> Runner-up: the approach you'd pick second, and why it lost
> Open questions the brief doesn't answer, each with your proposed answer
> Status: APPROACH. Stay in this session; you'll build once the approach is ruled on.

## Tech-lead reviewer prompt

Loop step 4a.

> You're the tech lead reviewing an approach before any code is written, in a fresh context. You're read-only: don't edit, stage, or commit anything. Inputs: the brief at [brief path], the approach at [approach path], the tech plan at [plan path], `CLAUDE.md`, and the repo at [worktree]. Read the code the approach names and the code around it. Judge: whether it meets every done criterion; whether it honors the decision records and the contracts other issues read; whether there's a simpler path or existing code it should reuse; whether the failure contract and the seams with other issues are right; whether a later issue or milestone will have to undo it. Flag only what would cost a review round, a close issue, or a rewrite later. Don't judge style or naming. Prefer removing over adding; an addition counts against a finding. Return: a verdict (sound, sound with changes, or rethink); at most five findings, each tagged blocking or should, each quoting the brief line, record, or code that proves it, with the change you'd make; and a declined-to-judge list.

## PR body

```
Fixes [KEY, and every other key for a surface group]

[Status report from the implementer, verbatim]

Check (the implementer's stamped run at [sha]):
[tail of the check output]
```

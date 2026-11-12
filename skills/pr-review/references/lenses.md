# Lenses, validator, and the finding schema

Prompts for the reviewers and validators. Each goes to a fresh `worker` with paths, not pasted content (Model: worker role). Fill the brackets; keep the rest. The milestone-mode lenses (bug hunt, drift, structure) are in `lenses-milestone.md`.

## Contents
- Shared preamble
- Finding schema
- Correctness
- Brief conformance (with the test-diff section)
- Numbers (conditional)
- Interface (conditional)
- Copy (conditional)
- Validator

## Shared preamble

> You're reviewing a change you didn't write, in a fresh context. You're read-only: don't edit, stage, or commit anything. Inputs: the diff at [diff path], the brief at [brief path], `CLAUDE.md`, and the rules at [rules paths]. Read the repo around the diff as needed; the diff alone hides most false positives. Flag only what breaks: code that won't run, will produce wrong results, violates a quotable rule, or fails the brief. Don't flag style, naming, anything a linter or type checker catches, pre-existing issues the diff didn't touch, or "might be a problem if" without a concrete trigger. If the diff is over about 400 lines, review in passes and say so. Don't read the PR body, the implementer's report, or the issue's comments: they're the author's framing, and a description that says a change is safe walks real bugs past reviewers. The brief (which carries any accepted approach), the code, and the check output are your only account of the change. The machine rules in `CLAUDE.md` apply to you, with their reasons (no clones, extra checkouts as worktrees under `.claude/worktrees/`, kill by PID, one blocking wait and never a monitor). Read only the code, tests and docs you judge. The bar is wrong results or an agent faking green in normal use, not a determined attacker. End with a "Declined to judge" list: what you saw and chose not to rule on, and why.

## Finding schema

Return a JSON array, then the declined list.

```json
{
  "lens": "correctness | conformance | numbers | interface | copy | bug-hunt | drift | structure",
  "severity": "P0 | P1 | P2",
  "confidence": 0 | 25 | 50 | 75 | 100,
  "file": "path",
  "line": 123,
  "quote": "the verbatim line that proves it",
  "claim": "one sentence: what's wrong",
  "trigger": "the concrete input or state that makes it fail",
  "fix_hint": "optional, one line"
}
```

- P0: wrong results, data corruption, an invariant bypassed, a done criterion not met, a protected file changed without the unlock. P1: a real bug with a narrower trigger, or a brief requirement met in a way that'll break the next issue. P2: worth knowing, not worth blocking.
- Confidence anchors: 100 is verifiable from the code itself; 75 means you checked the diff and the surrounding code and it will bite in normal use; 50 is plausible but unconfirmed; 25 and 0 aren't reported.
- A 75 or 100 without a verbatim `quote` and `file:line` is demoted to 50. A 50 survives only as a P0.
- Don't propose rewrites. A detailed "explain and propose a fix" raises misjudgment; the claim and the trigger are enough.

## Correctness

> Mentally execute the change. Hunt logic errors, boundaries and off-by-ones, state that outlives its scope, errors swallowed or turned into defaults, ordering and idempotency, anything reading data it shouldn't yet have (look-ahead). Check the project's named one-way doors as listed in its review rules (ID schemes, data formats, counting and grading rules, schema invariants): a change that bends one is a P0 even when the tests pass.

## Brief conformance

> The brief is the spec, and a spec's silence isn't permission: judge behavior the brief didn't mention by what a reasonable user of this product would expect. Behavior the brief names as out of scope, or that predates the change, isn't this PR's finding: list it under declined for the lead to file.
>
> **First, the test diff.** Before anything else, list every one of these in the diff: an assertion removed or weakened (`toBeTruthy` where there was a value, a range widened), a test deleted or renamed, a skip, xfail, `.only`, or disabled test, a tolerance or threshold changed, a mock introduced where the real thing was tested, a golden, snapshot, or baseline changed, a test that only checks a mock was called, a hardcoded value that matches a test input, and any change justified as "backward compatibility" or "flaky". Each is a P0 finding unless the brief asks for it by name. This section exists because agents fake green in exactly these ways, and model reviewers catch about half of the subtle cases (a seed figure, from before Opus 5.5); the scripts catch the rest.
>
> **Then the conformance table.** One row per done criterion in the brief: the criterion, the evidence (a test name, a line of check output, a screenshot path), and met / not met / no evidence. No evidence counts as not met, and so does anything on CLAUDE.md's not-evidence list. Then three lists: required but missing or partial; present but not asked for (scope creep, including files outside the brief's Owns list, using the scope script's output); and present but wrong. Quote the brief line for each.
>
> Check the "easy half" trap: an interface plus a test suite that tests nothing, a placeholder or TODO behind a passing check, fixtures invented rather than recorded, numbers typed in rather than computed.

## Numbers (conditional)

Run when the diff touches calculation, counting, grading, statistics, or golden data.

> Re-derive one case by hand from the spec the brief cites, and compare it to what the code computes. Check: denominators (what's excluded, such as canceled orders), sign conventions, the side a number is computed from, units, rounding and the precision the goldens use, and that no row reads information dated after the event it describes. Check that any golden or expected value came from an independent source (an oracle script, the spec's worked numbers), never from the code under test. A formula and its expected value moving in the same diff is a P0.

## Interface (conditional)

Runs only when `scripts/removed-signals.sh` printed hits. Reads the hits, not the whole diff.

> Regressions don't show in the finished code, only in what a diff deleted. The hits at `.build/review/[n]/interface-hits.txt` are deleted lines that carried an interface signal. For each one, read `references/removed-signals.md`, then the diff around it and the code that replaced it. Drop every hit an equivalent replacement explains, or that the brief asked to remove. Report a hit only when the user lost something and nothing in the change gives it back, with the severity the table sets. Quote the deleted line, and give the surface and what someone can no longer do as the trigger. Report nothing for code the change didn't touch.

## Copy (conditional)

Runs when the diff rewrites user-facing words.

> Read every user-facing string the diff adds or changes (labels, buttons, errors, empty states, notifications) against the writing-style skill at [writing-style path] and its `references/ui-copy.md`. Report a string that breaks one of those rules, contradicts the state it names, or moves a number, unit or meaning from what the brief or the design says; quote the line. Don't rewrite copy you'd merely word differently.

## Validator

> You're checking one finding from a code review. Inputs: the finding (below), the diff at [diff path], and read access to the repo. Decide whether it's real. Read the cited line and enough around it to know. Return exactly one of: **confirmed** (cite the line that proves it), **rejected** (cite the line or test that refutes it), or **unresolved** (say what you'd need to know). A rejection without a cited line counts as unresolved. For a visual or screenshot claim, measure through the same capture path the gate uses (the screenshot call with its mask stylesheet), never computed styles read outside a capture. Don't look for other problems. The machine rules in `CLAUDE.md` apply to you (kill by PID, one blocking wait and never a monitor).

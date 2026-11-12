# Ledger template

One file per milestone, `docs/build/ledger-M<n>.md` (`docs/build/go-live/ledger-M<n>.md` for zero-to-one's Go live project, which numbers its milestones afresh), landed on `main` between merges or with the close issue (SKILL, Roles). It's the lead's memory across compaction, the source of the digest, and the skill's input at the pause. Its Squash sha column is what the close reviews.

```markdown
# Ledger: M<n> [name]

Started [date]. Demo script `docs/build/demo-M<n>.md`.

## Issues

| Keys | Title | Squash sha | Lines | Check time | Approach | Review rounds | Peak ctx | Notes |
|---|---|---|---|---|---|---|---|---|

Peak ctx is the largest context any implementer on the issue reached, across every round: the max of `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` over its transcript's calls (`subagents/agent-<id>.jsonl`). It's how the pause sees whether issues are sized small enough; past 400k, say why in Notes.

## Batch checks

- [date] full check at [sha] after [KEYs]: [green | red, culprit KEY reopened or reverted], [time].

## Escaped

- [date] [the bug], found by [milestone review | break-it | the user | a later issue], traced to [KEY, KEY] (M<n>, squash [sha]); its review [skipped it: which lens | couldn't see it: where issues meet].

One line per bug that merged past its issue's review, with every issue it traces to. One found after the close goes in the current ledger, or the last one's once the run is over, and keeps the milestone it came from.

## Rulings

- [date] [KEY] Ruling: [decision], because [why]; cost if wrong: [cost].

## Parked

- [KEY or finding]: [why it's parked], [what reopens it].

## Gates

- [gate name], after [KEY], [date]: [the user's answer].

## Digest (written at close; becomes the close issue's summary and the where-to-look post)

**FYI, nothing needed** for the look itself. Open decisions only the user can make: each as a question, linked to the Needs Review issue it sits on.
**My take:** the lead's recommendation on each, with the fact that settles it.

**Landed:** [KEY], [KEY], ..., squash commits [first sha] to [last sha]; the close pinned at [sha].
**Where to look:** [local url], the screens and side-by-sides, what changed.

**What's runnable:** the milestone's done state in one or two lines.
**Demo script:** ran clean at [sha]; output and screenshots in [path].
**Per issue:** the check line that proves its done criteria.
**Decisions made outside the briefs:** from the rulings.
**Review:** findings rejected and why; findings parked; findings already gone on current `main`.
**Drift:** the milestone-mode drift lens, in a few lines.
**Look here first:** the two or three things most likely to be wrong.

## For the skill

What would make the next milestone run better: a dispatch prompt that needed changing, a hook or script fix, a check that ran slow and where its time went (the lock, the machine, a re-run), where the lead wasted context, what the user's notes caught that the agents missed.
```

# Milestone-mode lenses

The bug hunt, drift, and structure prompts, read only in milestone mode. Each reviewer gets the shared preamble and the finding schema from `lenses.md` with its lens below; same rules for paths and brackets.

## Bug hunt (milestone mode)

One or two hunters, each a fresh `worker` with the shared preamble from `lenses.md` (Model: worker role). Inputs and report shape only; the hunt stays open.

> Run the app built from the milestone's squash commits (the diff at [diff path], the worktree pinned at the last one at [worktree path]) on your own port, with the demo script at [demo path] and the briefs at [brief paths], and use it across the routes and data shapes those commits touched, where one issue's work meets another's. Each bug is a finding in the schema: `trigger` is the steps that make it happen, and `quote` is the code line you traced it to; trace each one, since an untraced finding is demoted to 50 and survives only as a P0. The lead sends an untraced P1 back to its hunter once to trace; still untraced, it's dropped. Report only what you made happen, not what reading the diff suggests.

## Drift (milestone mode)

> Read the milestone's squash commits (the diff at [diff path], in the worktree pinned at the last one) against the tech plan's decision records and the milestone's done state. Report: decisions made in code that no brief or record made; one-way doors as built versus as recorded; shared contracts that changed shape between issues; test health across the milestone (skips, mocks, coverage of the done criteria, the test count over time); and anything a later milestone will have to undo. Then the other direction, with the product doc's Solution Details at [doc path] and DESIGN.md: every line there or in a decision record that the built code now contradicts, quoting both sides, with the side you'd expect to win. This lens reports to the digest; it doesn't block on its own unless a one-way door moved.

## Structure (milestone mode)

> The shared preamble's "flag only what breaks" reads here as "flag only what makes a named future change break or cost more". Read pr-review's `references/structure.md` at [structure path] first, then the milestone's squash commits at [diff path], in the worktree pinned at the last one. Start with the hot spots: the files those commits touched, ranked by the hot-spot and co-change commands there, then widen to the rest of the milestone's changes. Ask of every piece the milestone added or changed whether it should change together with what it's linked to, and report the hidden links, needless links, surplus, and special cases the milestone introduced or leaned on. Code the milestone didn't touch isn't a finding. Each finding's `trigger` is the concrete next change that becomes fragile, and its `quote` is the line that shows the link. Severity is P2 by default; P1 only when that change would break silently (no check fails, no test catches it, wrong behavior ships); never P0. Run the guardrails in `structure.md` before each finding, counter-evidence included, and report nothing rather than a cue you couldn't tie to a change. When one fix would dissolve several findings, give each the same one-line `fix_hint` so the caller can group them; otherwise propose nothing. You don't fix, and this lens doesn't block on its own.

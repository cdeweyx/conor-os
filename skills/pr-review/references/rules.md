# Rules: exclusions and precedents

Rules that hold in any repo. Read every run. Each line carries a source (`seed`, `fp`, `miss`, `user`). Project-specific rules with path globs live in the project's `docs/build/review-rules.md`. Keep this file under 60 lines; prune at each milestone close.

## Exclusions (never a finding)

- Pre-existing issues on lines the diff didn't change. (seed)
- Anything the linter, formatter, or type checker owns, and anything silenced by an explicit ignore with a reason. (seed)
- Nitpicks a senior engineer wouldn't raise in review: naming, ordering, comment wording. (seed)
- General quality asks (more tests, more logging, "consider security") unless the brief or CLAUDE.md requires them. (seed)
- Performance on paths the product doesn't run hot, without a measured or concrete trigger. (seed)
- A PR with no gate-0 run (screenshot baselines at zero pixel tolerance), CSS, token or layout changes included: the 1% gate (the per-PR screenshot tolerance) holds per PR, and drift under it is the hardening close's pixel sweep (build's `references/close.md`). Nor one stamped by the affected check in a milestone run: the full check runs per merge batch. (user)
- A missing proof beyond what each test owes: a mutation proof only when it asserts something doesn't happen (Always a finding), a cold run only for a new browser spec, a three-repeat run only for a new spec touching timing or a route in flight. (user)

## Precedents (facts that settle common false positives)

- A value read from a committed config or an environment variable is trusted input. (seed)
- Generated files (types, tokens, lockfiles) are judged by their generator, not line by line. (seed)
- A new file under a protected path is allowed; a modified or deleted one isn't, unless the project's unlock note covers that change and the review quotes it. A note the branch got by merging its base covers only what the note names. (seed; user)

- An expected value that moves by exactly a change the user ruled on (cited in the PR) isn't a moved golden.
- Two reviewers reproducing the same trigger independently is verification; the validator can be skipped and the verdict says so.
- A test that writes and deletes in a shared store under a parallel runner and fails intermittently has found a race in the code; the fix goes in the code, not in serializing the test. (miss)

- An oracle that re-implements the build's own rule isn't independent on that rule; a rule the oracle mirrors needs a cross-check against an outside source (a sign bug sat in both build and oracle). (miss)

- A re-review that finds the same class of hole one step over (an allowlist that leaks another item) marks the earlier finding not addressed for the class, and the fix hint is narrowing the class, not another entry.

## Always a finding

- A test that asserts a mock was called instead of checking the result. (seed: the most common fake from the models before Opus 5.5)
- A golden or expected value that moved in the same diff as the code that computes it. (seed)
- A test that reads the wall clock. It passes today and fails in ninety days. (seed)
- A catch, fallback, or default that turns a failure into a plausible-looking value. (seed)
- A schema or invariants diff whose tests try only plain UPDATE and INSERT. List REPLACE, UPSERT, and delete-then-insert attempts.
- A catch around a step that already committed, if anything it doesn't catch can turn that committed step into an error response.

- A UI primitive imported outside `src/ui/`, a style block that restates one another feature already has, or a section rebuilt where a block DESIGN.md names already exists, when the project has a `ui/` layer. (user) So is an inline style or utility class that overrides a shared `ui/` component's look at the call site (a button resized by hand); the fix is a new variant on the component; P1 at least, since a linter flagging the same line doesn't excuse it. (seed: Matt Dailey's gardening sweep)
- A baseline changes only through the project's accept command with a logged reason, and a logged change matching the brief isn't a finding; but one re-accepted under the pixel gate can still carry a change its logged reason doesn't name (a loading state, a stale glyph, a hover that used to win). Compare every re-accepted PNG with its old one; an unlogged change is a P1. (seed)
- A design-tool export can be a test input (the browser window sized from the export's height): a taller export fails its baselines on size. Re-accept them in the same PR.
- An eval's prompt or context holding its own expected answers (a catalog, a few-shot, a system note quoting the graded thresholds) makes the score measure lookup. Diff the prompt against the expected values.
- A test that asserts something doesn't happen, or a state stays (no request, no lift, no CDN host), is shown failing by breaking the code before it counts. A position is measured in page coordinates across the load, never relative to an element that can move with it.
- A stubbed API answer in a client test must be one the real route can send, with a server test on the same case.
- A client cache's invalidation and freshness are proven by interleaving tests (a forget before, during and after the look and the read), not one ordering.
- A color, length, radius, shadow, or duration that's neither a token value nor arithmetic over token values is a design value. A value lifted from a signed-off design that no token holds isn't a finding; the verdict names the token to add. (seed: heyrico's review-screen)
- A block that renders fetched data missing any one of a loading, empty, or error state, or with one the code can never reach; P1 at least, P0 when a done criterion names the state. (seed: heyrico's review-screen)
- Status text that can disagree with the state it names (a card still reading "Needs approval" after the approval): trace the string to the state it's derived from; a hard-coded or separately cached status is a finding. (seed: heyrico's review-screen)
- A rule the client mirrors from the engine (a classifier, a validity check, a reason) is tested against one table both sides read; a client-only copy drifts.
- A test that moves with its code leaves the old home's behavior untested; check the old entry point still has a test.
- A ruling that flips a test covers the ruled assertion only; diff the test so nothing beside it moved.


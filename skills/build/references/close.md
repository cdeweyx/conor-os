# Milestone close and the hardening close

Step 6 of the run, in full. The lead reads this when a close starts, and again when later scope reopens it.

## Which close

- **The light close** runs at every milestone while the project's README is at pre-launch weight (SKILL, Process weight): the check on `main`, the UI sweep, a cross-issue bug hunt, and the where-to-look post. Pre-launch, the job is to get the product running and right; the user's look catches the taste, copy and product calls, and the bug hunt catches the seams that compound.
- **The hardening close** is where the production checks live: accessibility, critics, drift and structure, the demo walk, the Final pass, the gate-0 pixel sweep and the time audit. It runs once, over the whole product, at zero-to-one's Quality step (after branding, on the same pinned sha as break-it), and flips the README to full weight. From then on, every milestone close is a hardening close scoped to that milestone. A project that starts at full weight (real users) has no first hardening close: each milestone close is a scoped one.

## Rules for both

- **Run it once,** when the milestone's issues have landed on `main` (the hardening close: when the build and branding have). One still waiting on the user doesn't hold it; it gets a scoped re-run when it lands.
- **Pinned, and blocking nothing.** The passes run in a detached worktree pinned at the squash commit of the last issue in scope, so later merges don't move what they read. The first hardening close pins at `main`'s head once branding has landed, so it reads the styled product. The next milestone doesn't wait for them, and nothing waits on the user's look.
- **Scoped to its commits.** A milestone close reads only the milestone's squash commits (the ledger's Squash sha column), never everything since a date, and its sweeps and walks cover only the surfaces its issues touched. A seam between this milestone and a later one is the later milestone's close to catch, since it sees both on `main`. The first hardening close reads every commit on `main` from the epic's first issue up to its pin, branding included, and every surface.
- **The passes run together,** in parallel where the lock allows.
- **Checked against current `main`.** Before a finding is filed, check it on current `main`: later work may have changed or fixed it. One that's gone is logged in the digest, not filed.
- **One close issue.** Everything the passes confirm goes into one close issue, worked like any other issue: its own branch off `main`, PR, review, and merge.
- **Later scope reopens it.** An issue that lands after the close has started (it was waiting on the user) reopens the same close issue rather than filing another, and the passes re-run only on what changed, pinned at its squash commit.
- **Findings stay in the close.** A finding about the work in scope is fixed in the close issue or killed with its reason, never parked in the next milestone to clear the board. The one exception is a structure-lens finding bigger than Small (Drift and structure findings), since it's upkeep rather than a fault in the work.

## The light close

1. **Every issue landed.** Pin the close worktree at the last issue's squash commit.
2. **The UI sweep** (a milestone that ships a surface), as in the hardening close below. The lead skims the sheets for a bug the sweep hit, a screen that doesn't match its Final artboard (a tweak the build made on purpose aside), or one that shouldn't exist, and files each into the close issue. The close issue also drains `docs/build/papercuts.md` (SKILL, Design loop).
3. **The bug hunt.** `pr-review` in milestone mode with its bug hunts only, on the milestone's squash commits in the pinned worktree, while the lead works on. Its confirmed product findings go into the close issue, each through the approach review before code, since hunts produce false positives the approach catches. Expect them: the hunt finds the cross-issue seams the issue reviews can't, by running the app across routes and data shapes, not by reading diffs.
4. **Clear the board** (hardening close, step 12).
5. **The digest and where to look.** Run the batch check on the pinned sha (`references/loop.md`, step 10a), write a short digest into the ledger and the close issue, and post where to look (below). A milestone with no surface posts the digest alone.

## The hardening close

1. **Every issue landed.** Pin the close worktree at the last issue's squash commit (the first hardening close: `main`'s head once branding has landed).
2. **The UI sweep** (a milestone that ships a surface). A fresh worker clicks every ordinary state of every surface in scope (loaded, loading, empty, error, each tab, open menus and dialogs, focus on the main actions) and returns a contact sheet per surface plus the bugs it hit on the way, including any label whose words contradict its state ("Needs approval" on an approved card) (Model: worker role).
3. **The accessibility pass.** A second fresh worker runs better-accessibility read-only on those surfaces, with `references/judge-siblings.md`, and checks them against `references/interface-floor.md` and the detection table in writing-style's `references/ui-copy.md` (Model: worker role).
4. **The lead skims the sheets** for any screen that doesn't match its Final artboard (a tweak the build made on purpose aside) or shouldn't exist. A mismatch, a bug the sweep hit, a floor failure, or a better-accessibility `HIGH` goes into the close issue; a minor one, or a better-accessibility `MEDIUM` or `LOW`, goes in as a papercut. The close issue also drains `docs/build/papercuts.md` (SKILL, Design loop), taking the cheapest fix on the floor's ladder.
5. **`pr-review` in milestone mode,** with its bug hunts, drift lens and structure lens, on the squash commits in scope in the pinned worktree, while the lead works on. Its confirmed product findings go into the close issue. Harness findings go to a backlog issue until the project's `docs/build/README.md` marks the harness hardened, and go into the close issue after.
6. **Drift and structure findings.**
   - The drift lens's doc-versus-code findings get the lead's ruling on which side is wrong (Final wins on how a surface looks, except a tweak the build made on purpose, which the Final pass below draws in). Wrong code goes into the close issue. A stale doc goes in the digest as a proposed edit (decision records and DESIGN.md fixed on `main` with the close issue, the product doc on the user's yes).
   - Findings from the structure lens (pr-review's `references/structure.md`, findings only) go the same way: a confirmed Small one goes into the close issue; anything bigger is filed as a `Chore` in the next milestone (the catch-all one at the first hardening close, or one the user names), with its effort label set at filing like any issue, and gets the researcher gut check (SKILL, Approach review) at dispatch.
7. **The demo walk.** A fresh demo walker runs the demo script end to end, with the closed product calls, and keeps the output and screenshots (Model: worker role).
8. **The critic pass** (a surface in scope). Critics score screenshots of the built surface with real data (hifi-design's critic loop; Model: critic role), because the issue reviews judge against the spec and can't see a spec choice that reads badly in use.
9. **Delete the project's unlock note** if one exists.
10. **The Final pass,** in the close issue's last PR. Bring the design's Final page up to date with every tweak the build made (the Design Needed test, SKILL, Keeping the tracker true) and run the element sweep (`references/design-loop.md`). Then one re-export and one token sync (the project's tokens-against-canvas comparison), with the moved baselines in the same PR. Gate 0 and Final re-exports run here, not on every PR.
11. **The pixel sweep,** the only gate-0 run. Every baseline at the pixel gate of 0 (the project's gate-0 target), each moved capture re-accepted with a reason or named, since a small change passes the per-PR 1% gate and goes stale silently.
12. **Clear the board.** Move anything parked into the tracker, and every open issue out of this milestone into the one that picks it up (the tracker is the only todo list; a date-gated issue carries its date).
13. **The time and token audit.** From the ledgers and the agents' reports, one table per issue: dispatch to merge, split into building, waiting on the lock, checks, review rounds and fix rounds, plus each agent's token total. Name the three biggest sinks with their cause (a queue, a full-suite selection, a thin brief, a fix round a better brief would have saved) and one change for each, filed as a harness issue or written into this skill the same turn. Tokens come second: flag only an agent or step that cost several times its peers. The table and the changes go in the digest.
14. **The digest.** Run the batch check on the pinned sha first (`references/loop.md`, step 10a), then write the digest into the ledger and as the close issue's summary.
15. **Full weight.** At the first hardening close, set the README's process weight to full, in the close issue's docs PR.
16. **Where to look,** as below.

A close with no surface in scope posts the digest alone as its where-to-look, carrying the proof (test lines, before-and-after numbers); there's no UI sweep, critic pass, localhost walk or Agentation pass.

## Where to look

The same post in chat and on the close issue, once the close's passes have run. It asks for nothing; open decisions sit on their own Needs Review issues and are only linked here.

> **FYI, nothing needed.** [Milestone] is on `main` and its close passes have run. Look when you want; nothing waits on it.
> **Where:** `[run command]` in [worktree], then [local url]. Follow `docs/build/demo-M<n>.md`.
> **What changed:** each surface or rule this milestone set, one line each, with its side-by-side (Final left, built right) or screen.
> **Look at first:** the two or three things most likely to be wrong, or the calls you'd most likely overrule, each with the lead's position.
> **Waiting on you elsewhere:** a link to each Needs Review issue, if any.
> Annotate on localhost with Agentation, or comment on the close issue; each agreed note becomes an issue the run picks up.

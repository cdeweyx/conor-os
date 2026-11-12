# Project setup, before the first milestone

What a repo needs before the orchestrator can run unattended. Most of it is the first milestone's first two issues; the rest is a README and a couple of account settings. Split what's owed into what only the user can do (account integrations, design work) and what the agent can do (installs, MCP config, exports over an MCP); a mixed list makes agent work look like a blocker.

## `docs/build/README.md` in the repo

The project's plumbing for this skill, so the skill stays generic:

- Branch names: every issue branch comes off `main` under Linear's branch name. There's no milestone branch.
- Process weight: pre-launch (the default until the hardening close flips it), or full from setup for a product with real users (SKILL, Process weight).
- The key-screen list: about 20 to 30 screenshot baselines per mode, the main state of each surface, kept as a drift check. Edge states (popovers, hovers, errors, thin data, loading) are pinned by behavior tests that assert what's on screen and where (DOM, computed style, positions in page coordinates, frame sampling for transitions), because a screenshot is taken after the page settles and misses what moves on the way.
- A target that runs the browser captures with the per-pixel threshold and the pixel gate both at 0, so nobody hand-edits the harness to get one. Only the hardening close's pixel sweep runs it; issue PRs hold the normal 1% gate.
- A target that compares the design tokens against the canvas (the token sync). It runs once, in the hardening close's Final pass, not per token change.
- The affected target (e.g. `make check-affected`: type checks, unit tests, and the browser specs for the surfaces a PR touches), which a milestone run's issue PRs stamp with, and a merge script that accepts its stamp. Until both exist, issue PRs run the full check (`references/loop.md`, step 6).
- The worktree pool script: it keeps a few worktrees under `.claude/worktrees/` with deps installed, and at dispatch takes a free one and resets it to `main`'s head on the issue's branch, re-installing only when a lockfile changed.
- The bookkeeping script: it opens the issue PR from the loop's body template with the stamp's tail, and appends the issue's ledger line. Tracker moves stay on the tracker's MCP.
- The check command and how it takes the base branch. Once the product has a surface, it runs `npx impeccable detect <ui source>` (impeccable 4.8.0 or later), and a repo with a GitHub Actions job runs it there with `--github` too, so each finding lands as an annotation on its line in the issue PRs. A PostToolUse hook that lints the file an implementer just edited (ai-design-check's `hook` command is the pattern) hands findings back before review; consider it once the lint's false alarms are known. (From impeccable's 4.8.0 release notes and ai-design-check's README.)
- The merge script and what it refuses (Guardrails).
- Guards: the paths that write or delete stored user data, auth, and secrets. Their PRs get pr-review's full set at either weight.
- Gates: one line per gate, naming the issue it follows and what the user is confirming.
- Owed inputs per milestone: artboard exports, canvas revisions, keys. Tie each one to the issue that first needs it, so a later milestone's export doesn't read as a blocker for the first issue.
- Where the demo scripts, ledgers, review rules, and review misses live.

## A README for a cold reader

The repo's `README.md` exists from the first milestone and follows brand-design's `references/readme.md` (a cold reader's sections, the branded top fold once the brand exists, the product-shot hero). CLAUDE.md and the PR rules carry its one standing line: a PR that changes setup, usage, configuration or a command a user runs updates the README in the same PR.

## Guardrails (deterministic, not prompts)

Sequence them by phase. At M0 of a zero-to-one build, the check, the tamper lint, soft CLAUDE.md rules, and the machine-rule hooks below (they lock no number, so they cost nothing to keep) are enough; the numbers and definitions still move with the user's calls, and a lock that needs the user's hand on every change costs more than it protects. Hard locks (protected goldens, unlock notes, deny rules, the merge script's stamp) arrive once the numbers are confirmed or the product is live. Whatever's in place, the lead can apply a reviewed change to it on the user's say-so; the user never does manual git chores to unblock the build.

The cheapest defenses against an agent faking a green check are scripts and hooks, because model reviewers catch about half the subtle cases (an October 2026 measurement, from before Opus 5.5; pr-review's tallies recheck it):

- A protected list (goldens, oracle scripts, screenshot baselines, test config, the hook and merge scripts themselves). New files under a protected path pass; modified or deleted ones block, unless an unlock note quoting the user's yes exists (`references/gates.md`).
- `permissions.deny` on Edit for the protected files the agent should never write, plus a PreToolUse hook for the Bash paths a deny rule misses (snapshot-update flags, deleting tests, `--no-verify`, merges outside the script, pushes to main). A hook that blocks merges into `main` lets the merge script through: it's the one path into `main`, and no agent merges around it.
- The same PreToolUse hook denies the machine rules' commands, each with its reason in the deny message, since text alone hasn't held them (agents ran `pkill -f` three times against the prompt's rule): `pkill`, `killall` and any kill by pattern (other sessions run the same commands on this machine, so a pattern kill takes theirs); `kill -9` (a killed worker never unlinks its POSIX semaphores, and once leaked only sudo frees them); `git rebase` and `git push --force` or `-f`, `--force-with-lease` included (branches are pushed as they go, and a rewrite moves the sha the stamp and the verdict name; `git merge` and `git revert` cover every case); `git clone` (a clone sits outside the workspace, see the machine rules).
- A check step that diffs protected paths against the merge base, which catches subprocess writes the hook can't see.
- A no-skip gate and a test-count ratchet in the test runner.
- A scope report: files changed outside the brief's Owns list, fed to the reviewer.
- A Stop hook (it fires only when the main session ends a turn) that runs typecheck and lint, never the tests or the full check: the full check runs once per merge batch in a pinned worktree (`references/loop.md`, step 10a), and a Stop hook that ran it went unlocked on a dirty tree and turned turns red.
- A second Stop-hook check that lists every issue in the waiting-on-the-user status whose last comment is the user's, as the hook's block reason, so the lead moves each out before the turn ends: an answered issue left waiting reads as still blocked, and it happened twice on one project. It reads the tracker's API with a key from a gitignored file.
- A merge script that refuses unless the base is `main`, a check stamp (affected or full) for the head sha exists, there's no `needs-human` label, the review's verdict line says Ready for that sha, and `docs/build/review-misses.md` has a tally line for the PR (pr-review's log lines went missing for seven PRs in one milestone and about fifteen in another while the rule was prose). One exception: a PR whose every changed path is under `docs/build/` (the lead's ledger, briefs and notes) merges without a stamp or verdict. No other merge path.

## The machine rules in CLAUDE.md

Copy this into the project's CLAUDE.md, beside the not-evidence list. Every agent on the machine shares them (the lead, implementers, reviewers, validators), and none of those prompts restates them; each prompt points here. The hooks above back the ones a command can break.

> **Machine rules.** Many sessions share this machine and this repo.
> - **Stop only processes you started, by PID.** Capture it from `$!` at launch and `kill <pid>` with plain SIGTERM. Never `pkill`, `killall`, or a kill by pattern, since other sessions run the same commands and a pattern kill takes theirs; never `kill -9`, since a killed worker never unlinks its POSIX semaphores and only sudo frees them.
> - **No clones, temp copies or side folders.** Never clone the repo, copy it to a temp folder, create folders beside the repos, or re-clone to repair (fix in place from the remote). A clone or temp copy sits outside the workspace, which means permission prompts that stop an autonomous run, and it skips the repo's hooks and shared git objects. A worktree has neither problem: add one under the repo's `.claude/worktrees/`, address it with `git -C`, and remove it when done.
> - **Leave the repo's own state alone.** From a script, never `cd` into the repo (the hooks judge a command by its target checkout), never symlink data into a worktree (`git check-ignore` fails past the link), and never move branches or refs another worktree may have checked out.
> - **Merge, never rebase or force-push.** When `main` moves, bring it in with `git merge`; a branch is pushed as you go, and a rewrite moves the sha the check stamp and the review verdict name.
> - **A blocked command is a report, not a puzzle.** If a hook or permission rule blocks something you need, say so instead of working around it; the hooks are what keeps a green check honest.
> - **Your own port, inside the lock.** Run checks on your own port (the project's port variable), since two checks on one port kill each other at startup. Run every check, browser run and test run inside the machine's check lock, since overlapping runs time out under load (two lanes once the machine is shared: an engine lane for unit tests, type checks and lint, capped below the core count, and a browser lane for the browser runs alone, each with its own lock, the browser lock always taken first; the full check runs both lanes at once and stamps only when both are green, and a change no browser spec reaches takes no browser lock), with a 2-hour limit on anything you background (background commands stop at two hours, and the limit counts the lock wait).
> - **One blocking wait.** Wait on a long run (a full check, a browser batch, an accept loop) with one command that returns when it finishes: a foreground call when it finishes inside the tool's 10-minute cap, otherwise one background run whose single completion notice you act on. Never a monitor, never a re-armed one, and never a shell poll loop (`for`, `until` or `while` around `sleep`): each wake-up re-sends your whole context to say nothing.
> - **Quiet output.** Run checks so they print a summary and the failures only (the project's quiet mode, or output to a log you `tail` or `grep`), and never read a whole log: you re-read everything you've seen on every step after.

## The not-evidence list in CLAUDE.md

Copy this into the project's CLAUDE.md. Implementers and reviewers never load this skill, and an agent that can't tell proof from a claim reports the claim.

> **This is not evidence.** A claim in a PR body, commit message, or agent report ("green", "tested", "works", "should work", "verified"). A summary of output in place of the output. A check run on any sha but the head. A test that passes because this change touched it (a loosened assertion, an edited golden, a new mock of the thing under test). Type-checks or lint passing, offered as proof of behavior. No console errors, offered as proof a surface renders right. A screenshot of demo or seeded data when the criterion is about real data, or at a width or state the criterion didn't name.
>
> **This is.** The command and the tail of its output on the head sha. A named test that exercises the criterion (and for a bug fix, failed before the fix). A before-and-after number with the command that produced both. A screenshot or recording of the named state at the named width, with real data.

## Accounts and settings

- The tracker's GitHub integration installed with access to the repo, with PR automations. The lifecycle: Todo, In Progress (the lead, at dispatch), In Review (the lead moves it the turn it dispatches the first reviewer, `references/loop.md` step 6; set the integration's PR-opened automation to In Review as the fallback), Done (merged into `main`), Needs Review (waiting on the user: an ask from the SKILL's When to stop, a gate, or a `needs-human` PR; never a merged issue, a fix from the user's notes included, which stays Done). The integration's default, Done on merge, is right; set no branch rule.
- The review MCP (Agentation) registered at user scope so every workspace has it; its server binds one port, so one review at a time.

# Learnings

Standing mechanics from real runs, read every run. The story behind each line is in `learnings-archive.md`, read only when diagnosing a repeat. The pause adds mechanics here, history there and process to SKILL.md, and keeps this file under 1,500 words by moving its narrowest lines to the archive.

## Tracker

- Linear's default automation moves In Review only on a GitHub review request, which agent reviews never make; that's why the lead moves it (loop step 6).
- When the user answers a gate or decision, the next tool call after the answer arrives (the turn's first, or mid-turn) moves the issue out of the waiting status (to In Progress), before running what the answer unlocks; the project's Stop hook lists any left behind.

## Briefs, reviews and merges

- The correctness prompt for a schema or invariants diff lists the write variants to attack: UPDATE, INSERT OR REPLACE, REPLACE INTO, UPSERT, DELETE then INSERT, a connection without foreign keys.
- Give guardrail reviewers the bar up front ("an agent faking green in normal use, not a determined attacker"), or the review becomes an arms race.
- Rule on an implementer's concerns before the PR opens; it saves a review round each time.
- Give each bug-hunt finding to the approach review, not straight to code: hunts produce false positives the approach catches.
- A finding that contradicts Final is checked against Final before it goes to the implementer.
- A visual claim is validated through the gate's own capture path: Playwright injects the capture stylesheet only during the screenshot, so computed styles read outside a capture mislead.
- Batch one-way-door confirmations into one gate per phase rather than one per PR; the risk is later issues building on a wrong door, caught at the phase boundary.
- The merge script refuses a short sha in the verdict line, and the verdict sha comes from `git rev-parse` on the stamped head, since a hand-typed one got its tail wrong and the verdict was reposted.
- Gate cleanup on the merge script's exit code (`if bash scripts/merge.sh N; then <remove worktree, delete branches>; fi`): a `;` once removed the worktree after a failed merge, and the implementer couldn't be resumed.
- A lead ruling that widens a pattern gets one counterexample checked before it goes out.
- Write a brief's counts and keys from the code, not memory.
- When a re-review finds the same hole one step over in an allowlist or coverage rule, stop plugging: take "narrow the class" or "one more plug" to the user, leaning narrow.

## Critics and the demo walker

- Critics can only Read named files: give every path (every PNG) by name, never a folder, and give every visual reviewer the full capture list.
- Built-surface critics get viewport shots from one real engine, dev overlays hidden, plus the capture's mask list (`still.css`); compare a failing pair with the current baseline before calling it a regression.

## Git, worktrees and hooks

- Each implementer's pool worktree sits under the main checkout's `.claude/worktrees/`, not the lead's checkout, and holds its own check stamp; run the check and the merge script from it.
- A project hook scopes itself to its own repo and fails closed on an unclear target. It judges the command's target checkout (`git -C`, the command's cwd), never the session's branch.
- Once the hook is live, the lead edits docs with Edit/Write or splices from a gitignored file. The hook reads any command text that names a protected file (a heredoc, a commit message, a ledger note) as a write to it, so write around the name.
- A guardrails issue's own deny rules lock its implementer out of its fix rounds; the lead applies the reviewed patch (`references/gates.md`).
- The lead runs from a checkout of `main`, since a hook that judges a push by the session's own branch blocks the lead's pushes from anywhere else. Its scratch files (briefs, approach notes, review logs) live where a workspace archive won't take them, or get restored from the archive before an agent reads them again.
- A `main` merge into a branch trips the protected gate when both lines carry approved protected changes; it's clean when every protected path equals one parent's blob (`git rev-parse <parent>:<f>`).
- A settings Stop hook fires only when the main session ends a turn, never per subagent, so per-issue checks are run explicitly. Commit and push every ledger and doc edit before a turn ends: the hook runs on whatever tree is there, and an uncommitted lead doc once made it run a full check under load, which flaked twice.
- The hook judges a compound command on the branch it starts on: switch branches in one call, push in the next.
- `worktree-pool.sh take` leaves the issue branch tracking the milestone; implementers set their own upstream until the pool sets none.
- Return a pool worktree only after every agent reading it has reported: `return` cleans ignored files, and it once wiped data a running reviewer was reading.
- The batch check runs in its own worktree outside the pool (`.claude/worktrees/batch`): a returned pool worktree pinned for it got handed to the next issue mid-run.

## Checks and the machine

- Diagnose the harness before the machine: every browser and test run behind the lock, one check run alone, fewer workers.
- Run nothing beside `make check`, the demo walker included; a heavy neighbor turns it red on timeouts.
- A stopped check can orphan the web server its test runner started, and the next check on that port dies at startup; after a stop, list what still listens on the port and stop it if its cwd is the check's worktree.
- The lead stops only what it started: check a process's command and working directory (`ps -o command= -p <pid>`, `lsof -a -d cwd -p <pid>`) before stopping it. A port near another agent's port isn't evidence it's yours.
- Check a harness change's files against the protected-paths list before routing it through a patch and unlock.
- A harness issue whose proof is full checks gets a run budget in its brief (at most two, when the lock is quiet); an open-ended proof once ran 2.5 hours behind four agents on one lock.
- One browser spec red in a full check: re-run it `--repeat-each=3` in the lock before bisecting; a repeat flake becomes an issue in the current milestone.

## Agents

- Address an agent by its own launch id, checked against its description.
- A `worker` can't spawn agents, so a pr-review handed to one runs every lens in one context. For the fresh-context lenses (a one-way door's full set), the lead dispatches each lens and validator itself.
- A handoff written while the outgoing session's agents still run leaves their completion notices in that session; the outgoing lead names a relay in the handoff (it forwards each final report verbatim and acts on nothing), or the new lead asks for one before re-dispatching.

- A handoff names one owner for every long-running job. "Let it finish in the old session" had both sessions resume the same backfill at once.
- Spend limits kill agents mid-run. Resume each with SendMessage after the reset (their worktrees and commits survive), and repeat in the resume message any correction queued before the stop.
- A spike a decision waits on runs as a researcher lane from the lead right away, beside shaping; its result goes on its issue and on the shaping issue.

## Fixtures and data

- Tests that compare to goldens build from a committed pinned copy of the source data; the live cache a refresh rewrites breaks a sha pin within hours.
- When data moves a number, grep every fixture for the old value, not only the ones whose tests go red.
- A lead's live test or one-off data script touches only rows it creates: query that a test record isn't already in the user's data (saving over an existing one changes it), and create before you delete.

## The user's look

- Embed images from the lead's own `.context/`; another workspace's path shows broken.

- For a live review of unmerged fixes, a detached local preview that merges the open fix branches (baseline conflicts resolved either way, never pushed) lets the user review before the merges land.

# Learnings

Standing mechanics from real runs, read every run. The story behind each line is in `learnings-archive.md`, read only when diagnosing a repeat. The pause adds mechanics here, history there and process to SKILL.md, and keeps this file under 1,500 words by moving its narrowest lines to the archive.

## Tracker

- When the user answers a gate or decision, the next tool call after the answer arrives (the turn's first, or mid-turn) moves the issue out of the waiting status (to In Progress), before running what the answer unlocks; the project's Stop hook lists any left behind.
- Before reporting what's blocked, the lead reads the tracker: each issue's state, and the reply threads under every open ask (the user often answers there, not in chat). A handoff once called an issue design-owned hours after its design locked, and a later "what's blocked" listed asks the user had already answered in Linear.
- A blanket yes ("I trust your leans") covers the asks it answers, never a lean that reverses a call the user made earlier; that one needs his word on the item. One such yes once deferred motion he had approved, and he reversed it.
- When the user decides text the lead drafted (legal copy, a brief), the lead edits the source file in the same turn, before any build reads it; an implementer once published the pre-decision draft as told, and only the conformance lens caught it.

## Briefs, reviews and merges

- The correctness prompt for a schema or invariants diff lists the write variants to attack: UPDATE, INSERT OR REPLACE, REPLACE INTO, UPSERT, DELETE then INSERT, a connection without foreign keys.
- A finding that contradicts Final is checked against Final before it goes to the implementer.
- Batch one-way-door confirmations into one gate per phase rather than one per PR; the risk is later issues building on a wrong door, caught at the phase boundary.
- Rule on an implementer's concerns before the PR opens; it saves a review round each time.
- A lead ruling that widens a pattern gets one counterexample checked before it goes out.
- Write a brief's counts and keys from the code, not memory.
- When a re-review finds the same hole one step over in an allowlist or coverage rule, stop plugging: take "narrow the class" or "one more plug" to the user, leaning narrow.
- Before ruling a concern out of scope, trace every caller of the component the ruling protects; a scope note once let the same leak through another caller.
- When main moved under a stamped PR, `git merge-tree --write-tree origin/main HEAD` says if it merges clean; a conflict means merge main, scoped re-review, fresh stamp.
- A harness rule implementers trip twice goes into every later brief that touches those files (a test naming rule, a lint rule, an allowlist): each cost a stamp.
- A surface brief says "if Final, DESIGN.md or the data disagree, stop with a decisions table". The lead appends its rulings and the first implementer's reads to the brief, and a fresh implementer builds from it; one milestone had four such stops and threw away no code.

## Critics and the demo walker

- Critics can only Read named files: give every path (every PNG) by name, never a folder, and give every visual reviewer the full capture list.

## Git, worktrees and hooks

- Each implementer's pool worktree sits under the main checkout's `.claude/worktrees/`, not the lead's checkout, and holds its own check stamp; run the check and the merge script from it.
- A project hook scopes itself to its own repo and fails closed on an unclear target. It judges the command's target checkout (`git -C`, the command's cwd), never the session's branch.
- Once the hook is live, the lead edits docs with Edit/Write or splices from a gitignored file. The hook reads any command text that names a protected file (a heredoc, a commit message, a ledger note) as a write to it, so write around the name.
- The lead runs from a checkout of `main`, since a hook that judges a push by the session's own branch blocks the lead's pushes from anywhere else. Its scratch (briefs, reviews, research, logs) lives in the main checkout's ignored `.build/lead/`, never a Conductor workspace: an archive keeps only `.context`, and archiving the lead's workspace once took every brief mid-run. Lost files come back from the sessions' transcripts (`~/.claude/projects/<workspace>/*.jsonl` outlives an archive) by replaying each Write and Edit; one recovery restored 520 files that way.
- A lead docs PR's title names no issue key: Linear closes any issue a merged PR title names, and that once closed two open epics.
- A settings Stop hook fires only when the main session ends a turn, never per subagent, so per-issue checks run explicitly. Commit and push every ledger and doc edit before a turn ends, since the hook runs on whatever tree is there.
- Run a multi-step docs command under `set -e`, since a newline ends an `&&` chain; a failed merge once still reached `git add -A` and landed conflict markers on main.
- Return a pool worktree only after every agent reading it has reported: `return` cleans ignored files, and it once wiped data a running reviewer was reading.
- The batch check runs in its own worktree outside the pool (`.claude/worktrees/batch`): a returned pool worktree pinned for it got handed to the next issue mid-run.

## Checks and the machine

- Run nothing beside `make check`, the demo walker included; a heavy neighbor turns it red on timeouts.
- The lead stops only what it started: check a process's command and working directory (`ps -o command= -p <pid>`, `lsof -a -d cwd -p <pid>`) before stopping it. A port near another agent's port isn't evidence it's yours.
- Check a harness change's files against the protected-paths list before routing it through a patch and unlock.
- Unit tests passing don't prove the artifact boots. A change to a deployed entry module (a Worker's main module, a server's startup) runs a boot check before review; a Worker once passed 188 unit tests and couldn't start (its runtime rejects a non-handler export).
- One browser spec red in a full check: re-run it `--repeat-each=3` in the lock before bisecting; a repeat flake becomes an issue in the current milestone.
- After a flake fix merges, every open branch merges main before its next stamp; branches cut earlier keep failing on the old flake.

## Agents

- A reviewer's prompt says the stamp covers the suite, so it runs only a targeted probe; reviewers once sat up to 45 minutes in the lock queue rerunning stamped suites.
- A `worker` can't spawn agents, so a pr-review handed to one runs every lens in one context. For the fresh-context lenses (a one-way door's full set), the lead dispatches each lens and validator itself.
- A handoff written while the outgoing session's agents still run leaves their completion notices in that session; the outgoing lead names a relay in the handoff (it forwards each final report verbatim and acts on nothing), or the new lead asks for one before re-dispatching.
- The pause runs through its push before the handoff, and the handoff names the pushed commit or what's left; one lead handed off mid-pause.
- An agent waiting on its own background run ("I'll resume on its notice") resumes itself when the run ends; leave it be. A lead's SendMessage then interrupts it: four resumes once stopped work mid-check.
- A fix round makes a running stamp moot: the old implementer stops it by PID before writing its handoff.

## Fixtures and data

- Tests that compare to goldens build from a committed pinned copy of the source data; the live cache a refresh rewrites breaks a sha pin within hours.
- When an issue's test data doesn't exist yet, split it by what builds on today's data.
- A recorded data file can predate the build Final was drawn from. Before briefing a surface whose copy states numbers, compare the file's numbers to Final's; a mismatch is the user's call on a re-record, asked at dispatch. Two landing sections once stopped on it after dispatch.

## The user's look

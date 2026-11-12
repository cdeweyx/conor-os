---
name: untangle
description: >
  Finds where a codebase's structure makes ordinary changes fragile by
  asking one question of every piece, "should these change together?":
  hidden links, needless links, surplus, and special cases, in an area
  the user names or the git hot spots. Proves a baseline can fail,
  writes a decision log with each fix above the problems it dissolves,
  reports the top five, the calls for the user, and what held up, then
  stops. Fixes only on request, on one ticket and one reviewed PR. Use
  when the user says "untangle", "clean up this codebase", "it's a
  mess", "AI slop", "refactor this repo", "this code is spaghetti". Do
  NOT use to review one PR (pr-review), for bugs in a diff
  (/code-review), for the structure pass at a build's hardening close
  (pr-review's structure lens runs there), or for UI edge cases
  (break-it).
disable-model-invocation: true
argument-hint: "[optional area or concern to focus on]"
metadata:
  adapted-from: https://github.com/caldoai/skills/tree/main/skills/untangle-codebase
  also-from: https://github.com/LordGhostX/agents-skills/tree/main/skills/untangle-codebase
  author: caldoai (untangle-codebase, MIT) and LordGhostX (its rewrite, MIT); adapted to stop at a report and fix through one reviewed PR
  commit: 442c299 (caldoai), 610ee7f (LordGhostX)
---

# Untangle

Agents write better code, and break less without noticing, where pieces that change together live together. A messy repo (vibe-coded, inherited, grown without a plan) usually gets that wrong in a few places that cost on every change and in a lot of places that look bad and cost nothing. This skill finds the first kind, proves it, and stops at a report. It never fixes everything in one pass: a whole-repo refactor is a diff nobody can review, and it trades known behavior for tidier files.

Inside a zero-to-one build, pr-review's structure lens already asks this question at the hardening close. This is for repos outside that arc.

Invoking it doesn't authorize edits. Steps 1 to 5 change nothing in the user's tree.

**Size it to the ask.** "Clean it up a bit" is the light pass, not an audit: a short report and every low-to-medium-risk cleanup it finds (dead code, copied constants, a rule kept in two places, needless indirection, misleading names, consolidation inside a module). The bound is risk, not count: no significant architecture change (new layers, moved seams between the system's parts, data-format or schema changes, a new abstraction across many modules). Each of those is filed as its own tracker issue in the product's improvements project, Backlog status, its catch-all milestone. No behavior change, and no calls for the user unless one is truly one-way; whoever runs it makes the rest, says which in the PR, and goes straight to step 6 without waiting for "fix all". The full pass is for "it's a mess", "refactor this repo", or a repo outside a build. The quotes behind this are in `references/learnings.md`.

## Steps

1. **Scope.** The area the user named. Otherwise the git hot spots, using the commands in `../pr-review/references/structure.md`, since structure only costs where code keeps changing. Read CLAUDE.md, the README, and any architecture or decision docs first; a recorded decision isn't reopened unless the friction is real. State the scope in one line. For an area too big to hold, a fresh `worker` summarizes each part, or a script strips function bodies to a skeleton written outside the repo (Model: worker role).

2. **Baseline.** Write down the checks that must stay green (the project's check command, typecheck, lint, the suite) and the two or three things that must keep working in use, each as a command or a click path with the result you expect. Run them and save the output. Then prove the baseline can fail: in a throwaway git worktree, break one thing in scope on purpose (flip a condition, return early), confirm something goes red, and remove the worktree. A baseline that never goes red can't protect a refactor; say so in the report, and the first fix becomes tests that pin current behavior.

3. **List every problem.** Read `../pr-review/references/structure.md` and ask its question of every piece in scope. Write down every hidden link, needless link, surplus piece, and special case with its `file:line`, the concrete change it makes fragile, and the counter-evidence you checked. Run its guardrails on each one. Change nothing.

4. **Redesign.** Work out the fixes as if the system had known today's requirements from the start, in the decision log format, each fix above the problems it dissolves. Look for the one fix behind several problems; never fix special cases one by one. Rank by how many problems a fix dissolves and how hot the code is, and keep the top five. The rest stays a plain list.

5. **Report and stop.** Written through writing-style, in three parts:
   - **Fixes.** The top five, each as its decision-log entry plus an effort (Small, Medium, Large), the behavior at risk, and the baseline check that guards it.
   - **Calls for you.** Problems whose fix changes what the product does or picks a direction: dropping a flag nobody sets, one of two flows that do the same job, an endpoint something outside the repo might call. One line each with a lean, the runner-up, and why.
   - **What held up.** What looked tangled and wasn't, with the counter-evidence. No findings is a valid result.

   Close with the baseline (what it runs, the break that proved it) and the word to send back: "fix all" or "fix 1, 3".

6. **Fix on request.** Everything chosen goes on one ticket in the project's tracker ("Untangle: <scope>") with the chosen log entries as its brief, and one PR on one branch. Each fix lands as its own batch in log order, and the baseline runs after every batch; a red baseline stops the work until the refactor, never the check, is fixed. A new bug, a product call, or a bigger redesign found mid-fix goes to the user before the scope grows. A test is deleted, loosened, or rewritten only when the brief names that change. Review the PR with pr-review in issue mode, the ticket as the brief and the last baseline run as the check stamp.

7. **Close.** Gate: every chosen fix landed or dropped with its reason, the baseline green after the last batch and matching step 2's output on what must keep working, and the PR reviewed.

## Things that go wrong

- Fixing as you go. Calls get made by the agent, and the report can't show what held up.
- Counting wins in files deleted. A merged wrapper isn't progress unless the named change got easier.
- A framework to unify code that only looks alike.
- A test cleanup pass. Removing tests that "wouldn't catch a real bug" mid-refactor is how a refactor fakes green, so test changes only come through the brief.
- Trusting a baseline that never went red.

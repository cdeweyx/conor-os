# The research spike before the plan

How to turn the givens and gaps into lanes, what counts as verified, and when to stop. Read before proposing lanes.

## Lane generator

Inputs: the givens and gaps, the interview answers, the product doc (goals, non-goals, overall shape), the designs (surfaces, states, motion), prior research, any candidate stack.

The walk:

1. Shape rows. For each numbered step of the overall shape: the component needed, what a platform, source, or library imposes, the worst plausible failure, scheduled or interactive.
2. Design rows. For each surface and state (empty, thin, loading, error, the run state): the rendering component, the data and its freshness, the seam crossed. A row needing a data shape the core table lacks is a plan decision.
3. Stack rings. Frontend jobs (primitives, toasts, command menu, virtualization, drag and drop, numbers, charts) start from their pick in `libraries.md`; another choice needs a reason. Every named technology gets a ring: Adopt (used before, or a survived reference repo uses it this way), Trial (docs say yes), Assess (unknown). Trial or Assess under a one-way door becomes a lane.
4. Cross-cutting checklist, always: scheduled jobs and their timing guarantees, free-tier cliffs and idle pauses, secrets, rebuild of the canonical store from scratch, the agent's per-milestone check, the review channel.
5. Merge rows that share a question; drop rows prior research already answered; add the three "why this fails in a month" questions, each with a lane.

Output: four to seven lanes, each with the question, the decision it feeds and that decision's reversibility, the rung required, the time budget, and the report shape. Show the list, get a yes, run. Write one shared brief file (the product, the givens, the constraints, the report shape) that every lane reads, so each prompt is the lane's question and nothing else. Number the reports in the project's one research sequence, continuing across pages.

Always a lane: the domain's hard problems, prior art that survived, operational surface and cliffs, the build tooling. Depends on the product: scale and performance (only near a boundary), library maturity (only for the two or three load-bearing libraries, plus whether the agent can read their docs), integration seams (when the design is fixed first). A dimension earns a lane only if a plan decision changes with the answer and nothing already answers it.

## Verification ladder

Each rung is enough for a different decision; climb from the top for anything runnable.

- Doc: a fetched page, quoted, dated. Enough for two-way doors and vendor-stated limits.
- Repo: a raw file read from a project that did the same job at the same scale for a season. Enough for patterns.
- Probe: a script under 50 lines that produces a number or a pass, run locally, script path in the report. Required for any number the plan will repeat and any platform behavior a doc states vaguely. Twenty minutes usually retires a dimension.
- Prototype: a thin end-to-end line across two or more components in an unnamed worktree, the pass criterion written by the user first, timeboxed, reported as a number and a screenshot, then discarded. Required under a one-way door when the risk is fit, not any one piece. If it wants to be kept, it becomes the first milestone and gets rebuilt from the plan.

Every plan claim carries its rung. Below the required rung at budget's end becomes an open question tagged with the rung it needs. Probes produce tests: a probe's verified table is the fixture's first draft, and a probe can retire a constraint outright (data recoverable after the fact removed the cron). Reports cite file paths in backticks, never as links; Notion turns local links into dead URLs. Probes stay headless: verify with a CLI, a file header or an exit code, never by opening a GUI app on the user's screen (a signed-Shortcut check popped an import dialog mid-session). Lanes don't read the user's personal accounts (mail, calendar, docs) for sample data without the lead's yes; ask for a sample or use a public one.

## Lane report additions

Beyond the product-research report shape: a verified table with one row per claim the plan will repeat (claim, rung, result, source, the decision fed), and a recommendation per decision with a reversibility tag. Synthesis is then a union: the plan's decision points are the lanes' decision columns with their best rung attached, and any decision no lane covered is visibly naked.

## Stopping rule

Every decision has its rung and the scariest unknown has a probe result. Then draft. Three guards against research as procrastination: lanes confirmed before they run, each naming its decision; a time budget per lane and probe, set first; anything unverified at budget's end goes into the plan as an open question, and the first milestone can be the probe.

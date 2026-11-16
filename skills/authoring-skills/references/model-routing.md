# Model routing

Which model does which job, and how the skills act on it. Last revised against Fable 5.2 and Opus 5.5. Revisit when a new model ships, when credit pricing changes, or when a step keeps failing in a way the table doesn't predict.

Sweep filed for: claude-fable-5-2, claude-opus-5-5

## The rule

Opus 5.5 is the default for everything. Fable 5.2 runs two kinds of agent: research and tech planning. Sessions and subagents don't run Sonnet or Haiku to save money; a product's own API calls are a separate choice.

| Role | Model | Effort | Used for |
|---|---|---|---|
| Main chat | Opus 5.5 | high; medium while iterating, low in a tight loop | Shaping, design, copy, build, every conversation with the user |
| `researcher` agent | Fable 5.2 | medium | One research lane: a big or vague corpus, many calls, a report back |
| `planner` agent | Fable 5.2 | high | Tech planning and architecture: a biased approach, the tech plan draft, the revisions between critic rounds. A design round's plan, at hifi-design's direction rounds only (a direction not yet picked; never polish or feedback inside a picked one): the lead's packet and live inspiration turned into the designers' direction, resumed across rounds |
| `critic` agent | Opus 5.5 | medium | Fresh-context critique of one artifact: a screenshot against a scorecard or DESIGN.md, or a tech plan from one panel seat |
| `worker` agent | Opus 5.5 | high (build's Small-issue implementers start at medium; their fix rounds run at high) | Any other delegated task: checks, generation, a bounded edit |

## How the skills use it

- Skills name roles, never models. "Spawn three critic agents", not "spawn Opus". The role definitions live in `agents/` at the repo root and are symlinked into `~/.claude/agents/`. A model change is an edit to the legend and the agent files; the skills don't move.
- Every role pins the full model ID (`claude-fable-5-2`, `claude-opus-5-5`), never an alias. An alias moves on its own, so a new model would arrive unnoticed, and it can also lag: on launch day `fable` still resolved to 5.1 (Claude Code 2.1.319). After any pin change, spawn the role, or run `claude --model <id> -p "Reply with your exact model ID only."`, and check the answer. A pin that no sweep covers fails `skill-budget.py` (authoring-skills, When a model ships).
- Every subagent pins a role. An unpinned subagent inherits the session model and effort, which is how a Fable session quietly spends Fable credits on critics.
- The main chat model is set by the human in the chat's model picker, so a step that wants a different main model says so in a `Model:` line. Grep `Model:` across skills to find every routing instruction.
- Tech planning is the one step that wants Fable doing the main work. The chat stays on Opus and the `planner` agent drafts the doc, which keeps the conversation in one place.

## Effort facts

- When a step falls short, escalate in this order: add a check that verifies the work, then raise effort one level, then move up a model at a lower effort. Anthropic's model guide calls the check "more cost effective and adds less latency than changing effort levels," and starts everyday engineering on Opus at medium, then high.
- The researcher runs medium (many lanes in parallel, breadth over depth); the planner runs high (few runs, one-way doors that compound into the build).
- Opus defaults to medium. The main chat runs it at high, lowered while iterating, set in the chat's effort control. Don't push Opus to xhigh or max as a stand-in for Fable; at max it costs more than Fable and scored lower on agentic coding than at medium (undated, source not recorded; retest at the next sweep).
- Fable's delegation follows the harness more than the effort level. With a minimal tool for starting subagents it rarely starts one; in a harness whose prompts invite delegation, like Claude Code, it delegates readily, and at xhigh and max 5.2 also spawns self-review subagents, which 5.1 didn't ([Fable 5.2 guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents)). Pinning sets a subagent's model, not how many get spawned, so the planner and researcher files say not to spawn.
- Watch item (from a roundup measured on 5.1; the 5.2 guide says nothing either way): Fable at high argued with feedback. The planner applies the critic panel's verdicts, so at the next tech plan, count applied vs reargued verdicts in the round log, then keep or cut this line.

- Cost is mostly context re-read, not thinking: every call re-reads the whole context, so a session's cost grows with roughly the square of its length. Build keeps implementers small by chunking issues. Main sessions get a nudge instead: `scripts/context-nudge.py`, a PostToolUse hook in `~/.claude/settings.json`, tells a main session past 400k (then each further 100k) to hand off at its next clean break. Subagents are skipped.

## Evidence behind the rule

From a research pass across Anthropic docs, X, HN, Reddit, blogs, and YouTube in September 2026:

- Anthropic's own guidance: most workloads start with Opus 5.5. On their SWE-bench Pro run, Opus at default effort matched Fable 5.1 at a fifth of the cost per solved task (5.1-era; see Prices below for 5.2).
- "Plan with Fable, execute with Opus" is the most repeated pattern. Fable earns its credits on architecture and on vague research over a large corpus, where it reads more and goes deeper.
- Incorporating feedback is Opus's clearest win. It takes notes without a fight; Fable 5.1 at high effort argued.
- Design and screenshot reading favor Opus. Copy favors Opus for clarity; Fable is fine for long exec-audience drafts. Neither is a good editor.
- Pixel-art stamps are the one place a run found Fable drawing better: two Opus rounds on a pixel-art footer scene came out "clean but plain" next to the Fable-drawn hero art at 8x, and the scores went flat; Conor put Fable on the last round, which drew specific buildings and lifted the gold comparison from 5 to 6. One case, a watch item: retest when either model ships.

## Prices and the 5.2 update

From the launch post and a second-source check in November 2026:

- Per token, Fable costs twice what Opus does. Fable 5.2 is $8 in / $40 out per MTok, a 20% cut from 5.1's $10 / $50 ([TNW](https://thenextweb.com/news/claude-fable-5-2-mythos-5-2-anthropic-launch-price)). Opus 5.5 is $4 / $20 ([Finout](https://www.finout.io/blog/claude-opus-5.5-pricing-2026-what-anthropics-new-flagship-actually-costs)).
- Anthropic's [launch post](https://www.anthropic.com/claude-fable-and-mythos-5-2) claims Fable 5.2 at high matches Opus 5.5 on agentic coding at about half the cost per task. That comparison runs Opus at its highest effort, which we never use. Against Opus at high there's no data, so a model swap on cost grounds needs our own token counts first.
- Fable 5.2 leads Opus 5.5 on every benchmark in the post except the preference-judged one (AA-Briefcase Elo, Opus 1800 to 1785). That fits the rule: Fable where depth and search pay, Opus for judgment, feedback, and anything the user reads.
- Never call a model cheaper from a vendor's per-task chart. Check list prices from a second source and the effort the chart compared.

## Revision log

- First version. Default flipped from Fable to Opus. Four roles defined.
- Critic widened to documents for tech-planning's panel; the author (planner, Fable) and the critics (Opus) run on different models on purpose, since homogeneous review can't improve a plan.
- Fable 5.2. Researcher and planner pin `claude-fable-5-2`; planner moves to high. Added prices; the 5.1-era claim that Opus matched Fable at a fifth of the cost is history, not current evidence.
- Anthropic's model-choice guide reviewed by a three-advisor panel. Models and the never-Sonnet-or-Haiku rule kept; build's Small-issue implementers start at medium; the escalation order added; the two main-chat rows merged.
- Researcher told to finish its lane through ordinary failures. Anthropic's Fable 5.2 guide: at medium effort the model ends turns early with a list of what's left, and the researcher runs at medium with nobody to say continue.
- Critic and worker pin `claude-opus-5-5` instead of the `opus` alias, so an Opus release is an edit too. `skill-budget.py` fails any pin missing from the "Sweep filed for" line.
- Model notes retested against the Fable 5.2 guide in the model sweep. Dropped the three with no 5.2 source (the 11x effort dial, Claude Code defaulting Fable to medium, Fable overshooting limits); reworded the spawning note to the harness cause the guide gives; dated the arguing note as a watch item; dropped the Fable-window option for tech planning. The per-token price check dates from when a vendor's per-task chart (Opus at max effort) was read as Fable 5.2 being cheaper.
- The design planner runs at direction rounds only, by Conor's preference. In six days, 60 design-planner runs cost $548 on Fable, 20 of them framing polish or feedback inside a picked direction.

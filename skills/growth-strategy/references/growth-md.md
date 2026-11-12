# GROWTH.md template

GROWTH.md lives in the product's repo beside DESIGN.md. growth-strategy writes it; every tactic skill reads it before doing anything, stops if it's missing, and appends to the results log after. Only growth-strategy changes the techniques; tactic skills write to the results log and nothing else. Keep it under two screens: it's a decision record, not the research (the teardowns sit in `growth/teardowns/`).

```markdown
# Growth: <product>

Updated <date> · Stage: <pre-launch | live, no revenue | revenue> · Goal: <number> by <date>

## Buyer
Who buys, in one line. Where they already gather (named communities, newsletters, feeds, searches). The words they use for the problem, quoted from a source (copied from MESSAGE.md's Their words when it exists, so the two don't drift).

## Frame and rivals
Frame: <the category we claim, one line>.

| Rival | How it grows (Observed / Inferred) | Weakness we can use | Snapshot |
|---|---|---|---|
| <name> | <the one or two channels that carry it, with links> | <…> | `growth/teardowns/<rival>/`, <date> |

Adjacent options buyers use instead: <by hand, a spreadsheet, an agency>.

## AI answers
Models and date: <model ids, date>. The ten questions stay fixed; re-runs compare against this table.

| Question | Named most (share of runs) | Us (share of runs) |
|---|---|---|

## Where we win
Three or four lines the user agreed to in the discussion.

## Techniques
### 1. <technique>
- Why: <fit, with the evidence and its link>
- First action: <this week>
- Metric: <one number>, threshold <x> by <check date>
- Kill rule: <below what, by when, then what>
- Runs with: <skill, or "brief below">
- Runner-up: <technique>, lost because <reason>

(two or three of these, never more)

Stage coverage: before they know they need you <technique | empty> · while they compare options <…> · through tools and people they trust <…> · after they buy <…>. Each empty stage is a Skip row with the trigger that would fill it.

## Skip
| Play | Why not |
|---|---|

## Measurement
Signup asks "where did you hear about us?" (<tracked | build issue link>). Each technique's metric: <where it's read>.

## Results log
| Date | Technique | Metric | Value | What we learned |
|---|---|---|---|---|

## Briefs for unbuilt skills
### <skill name>
The job, the inputs it reads from this file, what done looks like, the evidence to start from.
```

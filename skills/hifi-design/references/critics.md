# Critics

The subtract pass, the scored critic loop's prompt, and the comparison pass, read at refine and polish. visual-assets and landing-page run the same loop on their layer or page. The cases behind these rules are in `learnings.md`.

Contents: Subtract pass · Critic prompt · Comparison pass

## Subtract pass (before the critics)

One row per element on the surface. Show the cuts as a duplicate beside the base before they land.

```
| Element | Job (trust, act, leave, orient) | Keep or cut | Why |
| Due-this-week line | act | keep | the one action on the card |
| "Nothing this week" line | none | cut | absence on every card; drop the line, not the fact |
```

## Critic prompt (one per critic, fresh context, screenshot only)

```
You're one of three critics reviewing a product screen from a 2x screenshot. You have no code, no brief, no earlier scores, and no reference images; judge only what you see.
Audience: <one line, from the reference pass>
Settled by the user, don't raise: <the user's standing calls on this surface, one line each>
Score two things, 0 to 10, separately.
Taste: hierarchy, clarity, restraint, whether the subject carries the design, per the attached scorecard. Name it if the screen falls into an AI-look cluster: cream, serif, and a terracotta accent near #D97757; near-black with one acid-green or vermilion accent; broadsheet hairlines at zero radius; the SaaS-card kit (identical rounded cards, one shadow under each); template chrome (tracked caps eyebrows, middle-dot meta, mono data labels, arrows on links), as a finding.
Compliance: every visible value against the attached DESIGN.md (tokens, type scale, density, color jobs, deny list), plus four checks every round: nested radii concentric (a pill inside a square box fails), a hover state drawn for every interactive element in every state, standard controls that look like the library's primitive rather than a one-off, and every raised thing carrying its layer's shadow and hairline from the stack in DESIGN.md (an overlay drawn flat, or a card lifted like a popover, fails).
Prefer removing over adding. Any addition you propose counts as a cost against your own score.
Return: taste score, compliance score, then the three findings that would move each score most, each tagged with the goal or state it serves and marked structural (moves an element) or local. No praise, no rewrite.
```

Attach `visual-assets/references/scorecard.md` and DESIGN.md to the two scoring critics. When a Final artboard is re-exported for a build, the export is a test input (the browser window takes its height), so the export and its baselines ship in one PR. Cap polish at three rounds per design (the comparison pass and its one rerun sit outside this); past that the built-surface critic pass is the gate. Give every critic exact file paths, one per screenshot (and for a built-versus-design pass, a table pairing each built screenshot with its Final artboard): the critic agent can only Read a named file and can't list a folder, so a folder path wastes the round. The third critic is `/impeccable critique` on the same screenshot with the audience line and the removal preference prepended; ask it for the two scores at the end so the median has three values. Log per round in `mockups/hifi/critique-<surface>.md`: the three score pairs, the medians, the findings applied, the ones asked about, the ones that lost to a user call and the thread they lost to.

## Comparison pass (after the critic loop, per state that got a loop)

Running it: three fresh `critic` agents (Model: critic role) rank the ideal state against two or three gold screens for the same job. Gold means the best screen for that job, the user's named favorites first, then the reference pass, never just the nearest rival, so the surface isn't pulled toward the category look. Each state that got its own loop gets its own pass. Ours ranking first closes it. Otherwise fix ours from the findings under the loop's rules (structural on a duplicate and asked, the user's calls win), carry any fix to the states cloned from the base, and once the user has answered the duplicates, rerun once with every screen rescored (skip it if no fix landed); the rerun sits outside the three-round cap. If ours still isn't first, the user gets the table and decides whether that place is good enough, since a critic never locks a surface; if it isn't, the findings become the next comment round's agenda. Gold screens never reach the agent drawing the surface, and a finding names the goal ours misses, never a look to copy.

Setup, because anything that identifies ours breaks the blind:
- A `worker` prepares the set (Model: worker role), so the gold images stay out of the context that draws the surface.
- Ours and two or three gold screens, same state, same size. Crop logos and product names so the critic judges design, not recognition.
- Neutral paths (`compare/screen-a.png`), a fresh shuffle per critic, the key in the critique log only. A file called `ours.png` ends the test.
- No settled calls in this prompt, since they point at ours. Treat a finding that contradicts one as the loop does: the call wins, the fix is softened or dropped, and it's logged.

```
You're one of three critics comparing screens that do the same job, each from a screenshot. You have no code, no brief, and no earlier scores, and you don't know who made any of them.
Audience: <one line, from the reference pass>
The job: <one line, what a user comes to this screen to do>
Score every screen 0 to 10 on how well it does that job and how well it's made: hierarchy, clarity, restraint, craft. Then rank them best to worst, no ties.
For every screen below first, the three things most holding it back from the first, each pointing at a spot on that screen, tagged with the goal it serves and marked structural or local. Name the gap, never "make it like screen B". Prefer removing over adding.
Return: the scores, the rank, then the findings per screen. No praise, no rewrite.
```

Read it by rank and gap. Ours' rank is the median of the three ranks; the gap is ours' median score minus the best other screen's. Only numbers from one pass compare with each other: scores drift between passes even on unchanged screens, so compare gap to gap, never score to score. Use only the findings on ours. Log the key, the table (screen, median, rank), the gap, and what changed to `mockups/hifi/critique-<surface>.md`.

For a round with several options, the three critics carry different weights (the base, scanability or meaning, restraint or craft), rank every option, and name three changes for their top pick, each marked structural or local. They converge on compliance (off-token fills, unearned borders, side rails, eyebrows, labels repeating a heading, how-to-read captions); where they split on character, build both variants rather than choosing. They also catch real data bugs (a goal marker that sits off the bar it labels): explain the mark on the surface, don't hide it.

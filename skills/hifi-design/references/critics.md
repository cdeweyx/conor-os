# Critics

The subtract pass, the scored critic loop's prompt, and the comparison pass, read in the polish loop. visual-assets and landing-page run the same loop on their layer or page. The cases behind these rules are in `learnings.md`.

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

Write the direction pick into DESIGN.md before the first critic round, since critics score compliance against the doc: a nav's first two rounds scored 6.5 against a doc that still described the old bar. Attach `visual-assets/references/scorecard.md` and DESIGN.md to the two scoring critics. When a Final artboard is re-exported for a build, the export is a test input (the browser window takes its height), so the export and its baselines ship in one PR. The bar and the cap are in SKILL.md's polish loop (the comparison pass and its one rerun sit outside the cap); in a build, past them the built-surface critic pass is the gate. Give every critic exact file paths, one per screenshot (and for a built-versus-design pass, a table pairing each built screenshot with its Final artboard): the critic agent can only Read a named file and can't list a folder, so a folder path wastes the round. The third critic is `/impeccable critique` on the same screenshot with the audience line and the removal preference prepended; ask it for the two scores at the end so the median has three values. For a pixel-art layer, swap the template's "product screen" for the layer and its Compliance line for pixel craft: the panel is two pixel-craft critics (against the "Pixel-art scenes" section of visual-assets' `references/techniques.md`) and one taste critic (the scorecard); a palette-role script replaces the compliance critic, the prompt drops the removal preference, and the comparison pass against gold pixel scenes runs every round. The pixel-craft critic caught the banded glow, the tiled stamps and the value collisions that the taste critics only named as a cluster. Log per round in `mockups/hifi/critique-<surface>.md`: the three score pairs, the medians, the findings applied, the ones asked about, the ones that lost to a user call and the thread they lost to.

Stills and the brief: Paper's export writes to the Downloads folder: move the stills into the loop's scratch and slice any taller than about 1,400 top-down (ffmpeg's crop; sips crops from the center), since Read shrinks a tall still past legible. All three critics read one brief file (the screen, the stills by name, the settled list, the rubric), so they stay blind and identical. Slice a states sheet at a gap between cells, never through a fragment, and name in the brief what a still can't show (a 44 hit area drawn by spec), or critics mark down what they can't see. Check every still's height before the brief goes out: an export can come back as a 1-pixel strip, and all three critics then score the moment as missing.

A component the user approved by name is settled for critics too. When a critic fix shrinks it (a band of pictures cut to one to match a narrower board after the user praised it), the lead reverts it and adds it to the brief's settled list.

The lock message names what the critics scored and what they didn't: the scored set (such as dark 1440 and 390, three passes), the duplicates checked only mechanically (light by the recolor check, 768 by the fold rules), and any step of the loop that was skipped or cut short by the cap. The user asked after lock whether the critic process had run on everything.

Every round's stills include the state boards (hover, focus, every state the surface draws), not only the ideal pages: a round that sees no hover board fails compliance on hover it can't see, and the next round spends itself on a non-finding. When rounds are drawn in light, the loop scores light, and the other theme gets one scored pass of its own before the ready review, since a theme no critic saw is unscored even when it's drawn.

A frame that can hold still must read whole. Settled motion doesn't excuse a frozen frame that looks cut off or broken: when a frame can sit on screen (a wait's hold, reduced motion, a slow network), a critic's "cut off" finding on it is a still finding, not a reopened motion call. One lead dropped two critics' finding on a hard-edged frame as "settled motion", and the user flagged the same frame as weird and cut off.

Before acting on a finding about a small mark (a 16px logo, a favicon), crop it at 4x from the still and check the spec against what was locked. Critics misread marks at 2x, and a spec rewritten to match a misreading spreads to every frame.

A phone version of a locked desktop surface gets a bar test, not an absolute score. One blind pass ranks the phone frame, the desktop frame and two controls (the same phone type over plain crops of the desktop art). Each critic scores taste and craft (pixel craft for art, DESIGN.md compliance otherwise). It passes when its median taste and craft each match the desktop's and it outranks both controls. Scores drift between passes, so compare only the gap within one pass. When the gap stops closing, the worker rounds stop, and the phone round's last step in `rounds.md` takes over.

## Comparison pass (after the critic loop, per state that got a loop)

Running it: three fresh `critic` agents (Model: critic role) rank the ideal state against two or three gold screens for the same job. Gold means the best screen for that job, the user's named favorites first, then the reference pass, never just the nearest rival, so the surface isn't pulled toward the category look. Each state that got its own loop gets its own pass. Ours ranking first closes it. Otherwise fix ours from the findings under the loop's rules (structural on a duplicate and asked, the user's calls win), carry any fix to the states cloned from the base, and once the user has answered the duplicates, rerun once with every screen rescored (skip it if no fix landed); the rerun sits outside the cap. If ours still isn't first, the table goes to the ready review and the user decides whether that place is good enough, since a critic never locks a surface; if it isn't, the findings go into the planner's next packet. Gold screens never reach the agent drawing the surface, and a finding names the goal ours misses, never a look to copy.

Setup, because anything that identifies ours breaks the blind:
- A `worker` prepares the set (Model: worker role), so the gold images stay out of the context that draws the surface.
- Ours and two or three gold screens, same state, same size. Crop logos and product names so the critic judges design, not recognition.
- Neutral paths (`compare/screen-a.png`), a fresh shuffle per critic, the key in the critique log only. A file called `ours.png` ends the test.
- Mask identity the same way on every screen, ours included: one visible flat box over the name and face, never a box in the page color. A mask that disappears on ours reads as a page with no owner, and every critic files it as ours' top finding.
- No settled calls in this prompt, since they point at ours. Treat a finding that contradicts one as the loop does: the call wins, the fix is softened or dropped, and it's logged.

```
You're one of three critics comparing screens that do the same job, each from a screenshot. You have no code, no brief, and no earlier scores, and you don't know who made any of them.
Audience: <one line, from the reference pass>
The job: <one line, what a user comes to this screen to do>
Score every screen 0 to 10 on how well it does that job and how well it's made: hierarchy, clarity, restraint, craft. Then rank them best to worst, no ties.
For every screen below first, the three things most holding it back from the first, each pointing at a spot on that screen, tagged with the goal it serves and marked structural or local. Name the gap, never "make it like screen B". Prefer removing over adding.
Return: the scores, the rank, then the findings per screen. No praise, no rewrite.
```

Read it by rank and gap. Ours' rank is the median of the three ranks; the gap is ours' median score minus the best other screen's. Only numbers from one pass compare with each other: scores drift between passes even on unchanged screens, so compare gap to gap, never score to score. Use only the findings on ours. Under the cap, a pass also closes the polish loop when every critic ranks the pick above the gold set and the median rose, and what's left is findings all three name: the lead rules them into one fix pass (with 768 and the second theme when those are owed) and moves to Final without another critic round. Log the key, the table (screen, median, rank), the gap, and what changed to `mockups/hifi/critique-<surface>.md`.

For a round with several options, the three critics carry different weights (the base, scanability or meaning, restraint or craft), rank every option, and name three changes for their top pick, each marked structural or local. They converge on compliance (off-token fills, unearned borders, side rails, eyebrows, labels repeating a heading, how-to-read captions); where they split on character, build both variants rather than choosing. They also catch real data bugs (a goal marker that sits off the bar it labels): explain the mark on the surface, don't hide it.

**A structural finding that keeps coming back.** When all three critics name the same structural finding in two or more rounds, and the fix only brings one width to a structure the user already approved at the other width (a 1440 card taking the 390 card's order), merge it into the base and number it as a change at the ready review, rather than parking it on a duplicate. Left parked, it pins that place's score round after round. When a later round's critics ask to undo a fix an earlier round's critics asked for (the legend to the column edge, then back), that's the reversal stop: rule the open findings into one fix pass and close the loop.

# Review loop for motion

Paper has no playback, so motion is reviewed as stills before code and as recordings after. The user approves the strip; the critics review the clip before the user tests it; the clip proves the code matches the strip.

## 1. Keyframe strip on the canvas

On the surface's explorations page, duplicate the approved artboard three to five times across a row and edit each into a moment: t=0 (before the reveal), first element landed, mid-stagger, settled, and for a loop, one frame with the seam visible. Under each, a 12px label with the milliseconds and the easing token, and the artboard name says which motion ("Home · reveal · t=120ms"). Onion-skin variant when a start and end state need comparing: both states in one frame, the previous at 30% in gray, the next in the accent.

Post the row, get a yes. That yes is what the spec table refers to.

## 2. HTML prototype

One file per motion, `mockups/motion/<motion>/index.html`, with the real assets (the exported SVG layer, the real copy, the tokens as CSS variables) and the spec table implemented per `recipes.md`. No framework. Open it in the browser; iterate by editing the spec, then the file, never the other way around. A control whose feel is the question gets one round of DialKit knobs (MIT, vanilla adapter) with min and max set to the rulebook range; copy the values into the spec table before touching the file, and strip the panel after.

## 3. Record and tile

```bash
# record 12s at 1440x900 with Playwright (Python or Node), then tile with ffmpeg
npx playwright screenshot --viewport-size=1440,900 file://$PWD/mockups/motion/home.html /tmp/still.png
# for a clip, use a small Playwright script with recordVideo, then:
ffmpeg -i /tmp/home.webm -vf "fps=10,scale=480:-1,tile=8x3" /tmp/home-sheet.png
```

Capture stills from `render(t)` (`?t=ms`) rather than a recording where you can: exact, repeatable, and no dropped frames. Each still gets a fresh browser session: state the motion keeps ("played once this session" in sessionStorage) otherwise poisons every capture after the first, and in one run two critics judged a draw that the frames never showed. Before any critic sees a sheet, look at it and confirm the motion is visible across the frames. `scripts/contact_sheet.sh` wraps the ffmpeg step; with no ffmpeg, tile stills with Pillow. Sample dense through each transition (several frames inside every handoff) and sparse through the holds, and keep the first and last frames (a clip's title and end cards): an even strip hides a broken handoff between two frames (from LangChain design-agent). One look at the sheet covers the timeline; the clip goes to the user. To freeze a specific instant without recording, set a negative `animation-delay` on the elements and screenshot. If the Playwright clip drops frames, render with HyperFrames (`npx hyperframes render`, Apache-2.0, seeks every frame) rather than re-recording; it needs a seekable timeline, so it's a fallback, not the pipeline.

A check that couldn't run and has no fallback above (no Playwright, a page that wouldn't load, a crashed Lighthouse run) is a failure to report, never a pass. (from LangChain design-agent)

## 4. Critic loop (before the user sees it)

By the first recording the agent has stopped seeing the motion, so three critics in fresh contexts see it first. They get frames, never the conversation.

The user's pick is the anchor. The loop refines it; it never replaces it. Critics grading against the restraint rulebook alone pull every round toward less, and in one run that turned the user's pick into something they didn't want in three rounds ("I like A back on every point... how did we end up here?"). So every critic gets the moment's brief (for a signature moment, what it must make the viewer feel, e.g. rich, interactive, wow) and scores fit to the brief next to the rulebook, and any finding that would change the pick's character (cut a motion, reorder, change the pacing by a third or more) comes back to the user as a before and after beside the pick, one at a time, never folded into a new version.

Every critic prompt also lists the user's standing calls ("don't raise these again"). Without the list, critics re-raise settled decisions each round; with it, round 2 reopened none of them.

The code critic runs as a `worker` agent (Model: worker role): the `critic` role reads screenshots only and declines code. Ask it to verify behavior in a browser (keyboard paths, loops after focus, interruption), not just read; in one run it caught three regressions that round 1's own fixes had introduced.

Inputs per round: the contact sheet (10fps, tiled), four to six stills at named timestamps (t=0, first mark, mid, landing beat, settled, plus a repeat-run still for a signature moment), and the spec table. Only the first critic gets the code.

1. **review-animations** on the code and the spec table: rulebook compliance and craft. It defaults to flagging, so a pass means something.
2. **Taste critic**: the contact sheet and stills, scored against `scorecard.md`. Prefer removing over adding; any addition counts as a cost.
3. **First-time viewer**: the stills and contact sheet with one line of product context and nothing else. Asked: what just happened, what did it tell you, where did your eye go in each still, what felt slow, what felt fake. It never sees the scorecard.

Each returns a 0 to 10 score in its lane, a 0 to 10 score for fit to the brief and the three findings that would move it most, each marked structural (a phase reordered, added, or cut; a duration changed by a third or more) or local. No praise, no rewrite. The round's score is the median.

Rounds: two to three. Stop at a 9, or when a round gains under a point; a fourth round is taste drift. Expect round two to re-flag the user's calls from the approved strip; that's the stop signal, not a reason to reopen them, and it ends the loop even when the score would allow a third round.

Between rounds:
- After applying fixes, run a quick scripted check of every behavior you touched (Playwright: keyboard open and close, a run interrupted mid-replay, a loop after focus) before the next round. Fixes break things.
- Start by re-reading the whole spec and the last round's log and asking of each row whether you'd make that call again. Old work gets revisited, not just nudged.
- Every fix goes into the spec table first, then the file, then a fresh recording.
- Structural findings are allowed. Apply them and keep the before clip, so the user sees both with the reason. A finding that contradicts something the user approved on the strip becomes a variant beside it, not a replacement.
- After a round that added anything, one line of subtract check.

Log every round to `mockups/motion/critique-<motion>.md`: the three scores, the median, findings applied, structural changes with before and after clips, and findings that lost to a user call with the call they lost to.

**Ranking pass for directions.** For a signature moment's rough directions, run the same three critics once on each direction's frames. They rank rather than score, with one line on why and the one change that would most improve each. The user picks from the clips and the ranking.

## 5. The user tests it

Post the clip, the prototype link, the last round's median, and anything structural the critics changed (before and after). The user tests in the browser; their calls win over any critic. Iterate on their notes through the spec, re-record, and re-run one critic round only if the change was structural.

Budget, checked before handing over: throttled Lighthouse, INP, layout shift, idle CPU with everything running. Done when the strip, the spec, and the clip agree, the critics are past the stop, and the user has said yes.

## 6. Record the decision

The spec table into DESIGN.md as the motion spec at handoff. The clip linked from the surface's Solution Details. The strip stays on the explorations page. The prototype ships in a PR with fake data.

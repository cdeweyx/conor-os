---
name: motion-design
description: >
  Designs purposeful motion for a product surface, from deciding what should
  move at all to a reviewed prototype and a motion spec in DESIGN.md. Use at
  hi-fi's prototype step, or when the user says "animate", "motion", "should
  this move", "reveal", "ticker", "draw in", "make it feel alive", "page
  load", "loading state", "magic moment". Do NOT use to judge finished
  motion code (review-animations, which this skill calls), for polish of an
  existing UI (better-ui), or for the visual itself (visual-assets).
---

# Motion design

The bar is Linear's: if most people don't notice what changed, that's a good sign. Motion on a product surface exists to establish hierarchy once, to show a value being measured rather than typed, to keep a backdrop alive without asking for attention, and to answer a user's action. Everything else is a fade-in on scroll, which is now the named tell of generated work. The skill runs the same loop as visual-assets: frame, research the specific motion, directions for a signature moment, spec, make, critic loop, the user's test, hand back, fold the run into the skill. The spec comes before the code because a motion nobody wrote down gets tuned by feel until it's mush, and the critics come before the user because by the first cut the agent has stopped seeing it.

Read `references/rulebook.md` before writing a spec, and before building read `references/recipes.md` (data motion) and, for UI components (dropdown, tooltip, modal, drawer, toast, accordion, gestures), `references/recipes-ui.md`. `references/review-loop.md` has the keyframe strip, the prototype, the recording pipeline, and the critic loop; `references/scorecard.md` is what the critics score against. `references/inspiration.md` has where to look and how to annotate a reference clip. `references/transitions-dev.md` has the Transitions.dev and Libraries.dev catalog, the token mapping, and the install lines. Read `references/preferences.md` every run, before framing; it holds the user's picks from past runs. `references/vocabulary.md` names every motion; use its terms in the candidate list, the spec rows, and the reference notes so a motion is called the same thing everywhere.

## Frame what earns its place

Go wide before cutting. Generate at least fifteen candidates across the categories where products put their best motion: the wait on the core computation, arrivals and departures (save lands, discard, retire), overlays and disclosures, data that changes while the user watches (a re-run, a refresh, a count), numbers changing, the front door, empty and success moments, hovers and tooltips, and the handoff from one screen to the next. For each, ask what a product people love would do there. In parallel, have one fresh-context `worker` agent brainstorm its own list from the specs alone, and merge (Model: worker role). Cutting is cheap; a moment nobody listed never gets designed.

Then give each candidate a job or cut it. Build the list from every spec's States and Transitions tables and the grammar's beats, not from the artboards, because the moments that matter most are often between screens: a computation the user waits on (a run, a search, an analysis) is the signature-moment candidate for the product and usually outranks everything else on the list. A spec that says "skeleton after 150ms" for a computation hasn't decided the moment yet. Jobs that survive: the one reveal on first paint, a chart or line drawing itself in the order it happened, a number rolling to its value, a ticker showing breadth in fixed space, a slow ambient drift on a backdrop, and micro-feedback on user actions. Jobs that don't: section fade-ups, parallax, cursor effects, page transitions, anything on a keyboard-initiated or high-frequency action (a hold's progress fill is the exception). Write the surviving list with one line each on what the motion is for and what it must not do (compete with reading, run while the user types, play forever), then the cut list with the reason each one died (no job, too frequent, keyboard-initiated, data the user is reading). The cuts show the restraint was real, and they stop the same candidate coming back next run. A cut that's already in code goes with what it leaves behind (`references/rulebook.md`, Cutting built motion). Where hi-fi's expressive-moments step already picked a settled frame for a moment, the motion serves that frame; it doesn't redesign it. Run `transitions review` from the Transitions.dev skill on the prototype's markup as a second opinion on the list (install line in `references/transitions-dev.md`); take its adds only where they name a job. When a motion breaks the rulebook for a reason (a draw-in on first paint, a rolling number), name it as an exception in the spec rather than loosening the rule. Get a yes.

## Research the specific motion

A path draw-in, a marquee, a digit roll, and a field drift each have a canon and a set of reference implementations. Two lanes, previewed and confirmed, each a `researcher` agent (Model: researcher role):

- Technique: the property to animate, the library that does it with the least code, the duration and easing that practitioners converge on, the performance trap, the reduced-motion outcome. Ask for numbers.
- References: products that do this exact motion well, with a clip or a frame sequence. On a live page, read the timing off it with explain-interface instead of estimating from a recording. Screen-record or fetch, then annotate each with what moves, what stays still, duration, easing shape, stagger, and the moment it stops. The stillness is usually the insight.

When the two lanes disagree (technique said scroll the ticker and references said product tickers don't scroll), don't pick in chat: build both as versions behind hifi-design's switcher (`references/picker.md` there) and let the user choose from the running thing, with your lean. Log each lane's report by product-research's same-day rule. Distill to a timing and a shape per motion, and one principle for the surface (for a data product, usually: the data draws, the chrome doesn't).

## Directions for a signature moment

A signature moment (the product's one wow, usually the wait on its core computation) gets directions before a spec; the other motions have one obvious shape and skip this. Write an exploration brief: the moment's job in one sentence, the honesty rule, the frequency split, and two or three directions that differ in what the viewer watches (the result forming, the volume of work, the method), each with its bet. Get a yes on the brief, then build each direction as a rough prototype from the research, record them, and run one ranking pass with the critics in `references/review-loop.md` before the user picks. The user picks from the clips and the ranking; the pick goes to the strip.

The honesty rule for a working state: it shows real work (the actual counts, steps, and partial results as they're computed), never a fake progress bar. A short minimum duration is fine when the backend is instant, because visible real work builds trust; replaying real results at a paced tempo is honest, inventing them isn't. It's skippable by click or key, it plays in full on the first run and in about a second on a repeat, and it hands off to the result rather than cutting to it.

## Spec before code

Before the spec, pull the locked frames from the canvas (screenshot and JSX of the artboards the motion lives on), not from exports or memory. Hi-fi polish moves things after the specs are written: in one run the chart's heading had changed and the editor's table had different rows, and the first prototypes animated a layout that no longer existed. If the canvas is unreachable, build from the spec text, say so, and check against the canvas the moment it's back.

Write the motion tokens if the product doesn't have them: three durations (fast, base, slow), three easings (out, in-out, linear when data or progress sets the pace), a stagger step, and a spring preset, as CSS variables in DESIGN.md so the canvas and the app agree. Then one table per surface, one row per motion: element, property, from and to, delay, duration, easing token, trigger, reduced-motion outcome. The load sequence is one orchestrated reveal in element order, nothing else moves on load. The whole table fits the ten-line prompt in the rulebook; if it doesn't, cut motions. A motion that can fail, be canceled, or fire twice gets one more row per path: what the user sees on an error, how a cancel unwinds, and whether a repeat restarts or is ignored while the work is pending. A result from an abandoned run never lands. These rows sit outside the ten lines, which count what plays, not what can go wrong.

## Make it

Write every frame as `render(t)`, a pure function of the timeline's milliseconds: stills (`?t=`), skip, replay, and reduced motion are then the same code, and critics get exact frames. Prototype every data motion with a strong case and a weak one, at the same tempo; the weak case is where honesty shows. Keep picked-against options as URL toggles in the same file (`?x=hold`, `?chart=still`) so the record stays runnable.

CSS and the Web Animations API first; Motion for React when layout, presence, or path length is involved; NumberFlow for digits; morphicons for a glyph that morphs between two states; Paper Shaders for an ambient backdrop, tuned on the canvas and shipped as props. Not GSAP, Lottie, Rive, or video unless the research named a reason. Libraries.dev's effects are tuned for a theme: judge each against the product's ground and register, not in the abstract (on a light warm theme only Border beam and Thinking orbs survived). Transitions.dev's catalog and its asymmetry rules are in `references/transitions-dev.md`; install both at the build, not before. Transform and opacity only, transform-origin where the motion physically starts, a reduced-motion branch (rulebook rule 7), loops that pause offscreen and on hover. `references/recipes.md` has the code shape and budget per motion, `references/recipes-ui.md` the UI component recipes.

## Review before and after code

Paper has no playback, so motion is reviewed in a prototype, not on the canvas. Paper holds only what stills show well: a states sheet for every interactive element (rest, hover, focus, pressed, selected, disabled, busy) and three key frames per signature moment's lead direction (start, peak, settled), each annotated with the milliseconds and easing token. Timing pairs and competing directions never go on the canvas; they're toggles in the prototype (a 140-artboard strip round was cut to about 20). Then the agent writes a single HTML prototype from the spec with the real assets, records it with Playwright, and tiles the frames into a contact sheet so one look covers the timeline.

Before the user sees it, run the scored critic loop in `references/review-loop.md`: three critics in fresh contexts (review-animations on the code, run by a `worker`; a taste `critic` on the contact sheet against `references/scorecard.md`; and a first-time-viewer `critic` who sees only the frames and says what just happened) (Model: worker role for the code lane, critic role for the other two), two to three rounds, stopping at a 9 or when a round gains under a point. Each round starts by re-reading the whole spec and asking whether you'd make each call again, so old work gets revisited, not just nudged; structural findings (a phase reordered, added, or cut) are fair game and get shown to the user as a before and after. Every fix edits the spec first, then the file. Log each round. Check the budget: one load sequence under a second (a signature moment has its own cap in the spec), idle CPU under five percent on a mid-range phone, no layout shift.

Then the user tests the prototype in the browser, with the clip, the last round's scores, and anything structural the critics changed. Their calls win over any critic; iterate on their notes.

## Hand back

The motion table goes into DESIGN.md at handoff as the motion spec, with the tokens. Before it goes, check every row against the surface's Final artboards: a rule that changes what a still frame shows (an item hiding at an edge, an element held back) is drawn on Final too, or it's cut. A spec that quietly contradicts Final gets built as the spec, and the user sees a surface that doesn't match the design they signed off (a ticker once hid any item cut by the window's edge, which Final never drew, and left a hole at the tape's start). The prototype ships in a PR with fake data; a coded prototype keeps most of its structure through build. The keyframe strip stays on the explorations page as the record, and the clip goes into the product doc's Solution Details for the surface, linked, not embedded.

## Skill pause

Run authoring-skills' Closing a skill update (the skill pause) at the end of every run. What goes where in this skill: a process gap into the steps or "Things that go wrong", a timing or property rule into `references/rulebook.md`, a scoring gap into `references/scorecard.md`, a technique into `references/recipes.md`, the user's taste picks into `references/preferences.md`. Read the critique logs end to end too: each finding that lost to a user call, and each pattern the critics got wrong (drifting toward less on a moment the user wanted rich), is a lesson as much as an applied fix.

## Things that go wrong

- Critics replacing the pick. Scored only against restraint, every round pulls toward less; in one run three rounds turned the user's pick into something they rejected. The pick is the anchor, the brief is scored, character changes come back as toggles.
- Labels that aren't true yet, or that borrow another concept's numbers. "Paid on time, 2011 to 2017" can't appear in 2012; "best of 37 clients" on a chart of one client mixed up two ideas and read as "this client beat the rest". A label on a moving chart names what the marks are, and appears when it becomes true.
- A live number that isn't the number it lands on. One run counted a total into a heading the Final page had changed to a percentage. Everything that moves lands where it lives, the largest number on the page included.
- Asking for a call in shorthand. Ask the way build's Asking the user says, each option one plain sentence of what the user sees or does.
- Trusting contact sheets for live bugs. Two things the user felt in seconds never showed on a sheet: a one-frame flash of the finished screen before a staged wait's first beat (an asset loading), and a color-parse bug that blacked out a nav's siblings in dark. Before any critic, drive the prototype live in both themes with a real pointer and log the opening frames one by one.
- Critics talking the user out of a pick, again. A critic asked to cut the half-opacity section settle and the staged wait's highlighted walk; the user kept both. Log such findings as "not taken: the user's pick" rather than applying them.
- A late agent overwriting the frame. A framing agent from an earlier session finished after the lead had rewritten the frame and replaced it. Check a shared file's mtime before relying on it, keep the late output beside yours, and re-brief any agent that read the wrong one.
- A fresh builder per fix round. The worker that built the prototype holds its structure; resume it for each fix round instead of spawning one that re-reads everything.
- Tuning by feel. No spec, so every round moves a number and nothing converges. Knobs (DialKit) only for one round with the rulebook's range as the bounds, then the values go into the table.
- A ticker at reading speed. Sixty to ninety seconds per loop, linear, paused on hover.
- Reviewing motion from a single screenshot. Use the strip and the clip.
- Reaching for a library before CSS. Most of this is twenty lines.

- Sending the code lane to a worker. review-animations is user-invoked only (disable-model-invocation), so a worker can't load it and shouldn't rebuild its workflow. Ask the user to run `/review-animations` on the prototype and the spec, and run the other two critics meanwhile.

## Checklist

- Locked frames pulled from the canvas before the spec; prototype matches the canvas (heading, rows, copy).
- Lane disagreements shown as toggles, not decided in chat.
- Every critic prompt carried the brief and the user's standing calls; the code lane ran on `worker` (the `critic` role reads screenshots only).
- Stills captured in a fresh session each, and a timeline checked for visible motion before any critic saw it.
- Candidate motions listed, each with a job or cut, the cut list kept with its reasons; user said yes.
- Fifteen or more candidates generated across the categories, merged with the brainstorm worker's list, then cut; swept from every spec's States and Transitions tables; the signature moment named; rulebook exceptions named in the spec.
- Technique and reference lanes previewed and run; references annotated with what moves, what stays, duration, easing, stagger, stop.
- Signature moment: exploration brief approved, rough directions recorded, one critic ranking pass, the user picked.
- Motion tokens in DESIGN.md; one table per surface, one row per motion plus its failure and cancel paths, reduced-motion column filled; one orchestrated reveal.
- Built with CSS, Motion, NumberFlow, or Paper Shaders; transform and opacity only; loops pause offscreen.
- States sheet and key frames on the explorations page; directions and timing pairs as prototype toggles; HTML prototype recorded and tiled; budget checked.
- Critic loop run before the user saw it: three critics, two to three rounds, each round revisiting the spec, fixes through the spec, logged to `critique-<motion>.md`.
- The user tested the prototype; their notes applied.
- The skill pause ran.
- Motion spec in DESIGN.md at handoff; prototype in a PR; clip linked from Solution Details.

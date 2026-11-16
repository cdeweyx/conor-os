---
name: hifi-design
description: >
  Takes converged lo-fi wireframes into high-fidelity surfaces on the Paper
  canvas over MCP, from DESIGN.md through a per-surface loop to the build
  handoff. Use when wireframes have converged and the user says "hi-fi",
  "high fidelity", "take it into Paper", "make it look real", "design
  system", "DESIGN.md", or when design-shaping reaches its hi-fi step. Do
  NOT use for lo-fi options (wireframe-explorations), for polishing a built
  UI (better-ui), for chart form and palette on their own (dataviz), or for
  brand identity (brand-design).
---

# Hi-fi design

Hi-fi polishes a solution that already works. The risk is the opposite of lo-fi's: not anchoring too early, but drifting into taste and clobbering what the user already approved. Every rule below is about locking what's decided, replacing the agent's defaults with the user's, and stopping on a signal instead of a feeling.

This is the one hi-fi loop. design-shaping calls it per surface, and build calls it for every Design Needed issue (build's `references/design-loop.md` adds only the session, tracker and built-surface rules). Both run it in the same order at one of two weights.

The canvas is Paper Desktop over its MCP server: real HTML with inline CSS, so what Claude writes is what the user sees, and what the user edits Claude reads back. Load dataviz for chart form and palette validation.

Read each reference at its step:
- `references/paper-loop.md` before the first Paper call (dialect, tool sequences, etiquette).
- `references/design-md-template.md` before the taste interview.
- `references/brief-and-review.md` every surface, at its prep: the brief and reference templates, the steer-yourself list, the revision templates, and the things that go wrong.
- `references/preferences.md` every surface, before its first pass. The first pass starts from the user's picks, and takes vary only what the surface gives a reason to vary. `references/preferences-archive.md` holds the dated product picks behind it; read it only when a surface repeats one of those objects.
- `references/constraints.md` every surface, end to end, before the first write.
- `references/checks.md` every surface, at each round's steer pass and at Lock: the revision checks, the table lens, the cross-surface pass, and the done checklist.
- `references/rounds.md` at the direction round, the polish loop and the ready review: the planner's packet, the designer brief, the review page, long pages.
- `references/critics.md` in the polish loop: the subtract pass, the critic prompt, and the comparison pass.
- writing-style's `references/ui-copy.md` before writing a surface's copy.
- `references/treatment.md` at the treatment step; `references/light-depth.md` at expressive moments.
- `references/final-and-handoff.md` at Lock, the shared chrome, and the prototype decision; `references/type-rendering.md` before the `ui/` spec.
- `references/learnings.md` and `references/failed-prompts.md` at the skill pause.

## Weights

The lead names the weight when the surface opens, in one line with the reason, and the user can bump it.

- **Full:** a crux surface (design-shaping step 2), a front door, a product's first hi-fi surface (it sets the visual system, whatever its kind), or, inside a build, a surface whose new direction later issues build on. It runs every step below.
- **Quick:** a surface built from patterns already on Final (the system artboard alone doesn't count), a small new element, or a side asset (an OG card, a README hero), even when it's a new page. It skips the ideas ask, the direction round, wildcards and the comparison pass, and reuses the reference report that exists. One designer, the planner framing it once from the brief, at most two critic rounds, and the user's first look is the ready review.

## Roles

- **The lead** (the session running this skill) does prep, writes the planner's packet, sends takes to designers, runs the critics, turns critic findings into fixes between rounds, picks, and talks to the user. It doesn't draw and doesn't write a direction.
- **The planner** (Model: planner role) frames direction rounds only: any round whose takes explore a direction not yet picked (the first round, a new direction the user asks for, a long page's next section pair), a small side asset included. Polish and feedback inside a picked direction are the lead's; it holds their context. The lead hands the planner a packet rather than letting it explore, and resumes the same planner for the surface's later direction rounds with only what changed (`references/rounds.md`). The user's notes are one strong input, not orders: the plan says follow, go further, or push back for each, with the reason.
- **Designers** (Model: worker role): two on Full, one on Quick, one take per artboard on the explorations page, resumed across rounds so they keep their canvas context.
- **Critics** (Model: critic role): three per round, screenshot only, run by the lead since designers can't spawn them.
- **The user:** the ideas ask, the direction pick, the ready review, and the done signal.

## Before the canvas

Interview the user before drafting anything, one question at a time, with the eight questions in `references/design-md-template.md`: feel and must-not words, the world it belongs to, one signature detail, a product to be mistaken for and its one trait, grays, accent, typeface, and a never-see list. Mechanics come from research and the wireframes; taste has to come from the user.

Draft DESIGN.md in the template's shape and present it as the system artboard in Paper (Setting up the canvas), dark and light side by side, with the spec's lint (`npx @google/design.md lint`) beside it, rerun on every change; a contrast claim in prose isn't proof. The user never reviews a design system as an HTML specimen or a PNG in chat. Iterate until approved, then push it to the product doc as an appendix toggle.

DESIGN.md is brand v0: brand-design comes after design-shaping's gate (zero-to-one's Branding step), since every canvas value is a token and the swap is cheap before any code.

## Setting up the canvas

Once per product, in its own session, by the setup section of `references/paper-loop.md`: Paper Pro, the three files, the Final and explorations pages, DESIGN.md compiled into Paper tokens, and a system artboard (swatches, type scale, a table row, a card, the controls, each chart form) that is the clone source for every surface, approved by the user before any screen exists.

## The per-surface loop

Every surface runs the same order, and the order is most of the skill:

1. **Prep** (silent): metric sidebar, reference pass, brief.
2. **Ideas ask** (Full): "Any ideas before I draw?", one question the user can skip.
3. **Direction round** (Full): the planner frames the takes, the designers draw them, and the user picks and gives feedback.
4. **Polish loop** (silent): the lead frames the pick and feedback once, then treatment, states, subtract, expressive moments, critic rounds to the bar, the comparison pass, contrast and the table lens.
5. **Ready review:** the user sees it all at once. A comment asking for a new direction goes back to the planner; other comments go to the polish loop; "good" is the done signal.
6. **Lock:** done checklist, Final, spec, PR, skill pause.

The user sees the work twice per pass, at the direction pick and the ready review; a front door adds a third, the treatment pick. Everything between is silent: never share a draft, one take, or a critic's interim score as it lands. Detail calls (a token, a copy line, a rest state) wait for the ready review. Skipping ahead costs a round.

## Prep

**Metric sidebar.** On any surface built from cards, rows, or panels, the lead weights the set before anything is drawn, because a direction round on an unweighted set is wasted. List every number and mark, its job for the user (trust, act, or leave), and its size tier (hero, supporting, action, off the face). One hero, one supporting line, one action is the shape of a card. Start from the order lo-fi or the product doc settled. Then a stats check on every number kept: a comparison shares its sample, null, and unit with what it's compared to, and a measure that fails comes off (offer the matched version), as does one that assumes a user action the app never sees. Then the name test: "62% [name]" read aloud has to name the thing it's a share of. It reaches the user only when it contradicts something already decided or drops a measure they like. Before the first surface, run it once across every surface that shows the same object, so the weights are set product-wide.

**Reference pass.** Gather references as text, by the reference report section of `references/brief-and-review.md`. When design-shaping's competitive look has a report, reuse it and search only for what's new. Five to eight references, each annotated by technique rather than feeling (line weights, hue count, density, structure, what carries meaning), link kept. Save it as `mockups/hifi/references-<surface>.md` with a small HTML report of the images for the user. Close with one "not this" anti-reference and one line naming the audience the surface must perform for. Designers get the annotated text list only, never images or taste words; technique notes hold a design system without drift.

**The brief.** Hand the designers artifacts that fix the answer, not adjectives that invite one, in the brief template: the converged wireframe file and screenshot (or the issue's spec in a build), the decision the screen supports, the goals it serves, the metric hierarchy and tiers, the references as text, the final copy verbatim, real data rows, the states, the losers and why they lost, the surface's standing rulings (or an older duplicate revives reversed calls), and DESIGN.md.

- Say what's locked: whatever lo-fi converged or the issue settled. The takes differ on what's left open.
- Say that DESIGN.md overrides Paper's style guide, or the designer drifts toward the canvas's house taste.
- Withhold the other explorations, every competitive screenshot, and taste words.
- When the brief reuses a pattern, name its node and say "match it exactly"; where the brief and an existing pattern disagree, the pattern wins.
- Don't paste the wireframe's HTML; its classes would be dropped. Point at the file and rewrite it in Paper's dialect.

Post the brief in chat and start drawing the same turn; the direction pick catches a bad brief. When the project keeps a running direction page (a Notion page for the agent's findings), write the brief there in the same turn, beside the repo copy. That page takes briefs and big structural decisions only; round picks go to the tracker.

Before the first artboard, write a token plan and check it four ways, in order:
1. The collision test: plan a similar brief (same job, another product); wherever the two land close, change direction on that axis and say why.
2. The five AI-look clusters in `references/constraints.md`. Bans relocate the default; colliding and moving off doesn't.
3. `references/preferences.md`: use the user's picks; where there are none, the direction round earns its place.
4. `references/constraints.md` end to end, every rule against the plan, before the first write, not at polish.

## Direction round

Ask for ideas first, then hand the planner the packet with the answer in it. The planner frames two or more takes that differ dramatically on the axis that matters most for this surface, and names that axis: often layout, sometimes density, the treatment, or what the screen leads with, never color alone. When lo-fi already settled the layout, the takes differ on something else. Each take carries one concrete aesthetic sentence and the assumption it tests ("hairline table, the monthly change at 28px in sign color, everything else at 13px gray; assumes the number is what earns trust"), never "unique" or "clean"; a take without its sentence is a layout shuffle. Crux surfaces get one or two wildcards when the user asks for range (usually), and when the user says a round is too incremental, the next adds four or five bold swings from outside references beside the safe set.

- Draw at 1440 and 390 only (or the surface's own frame), in the picked theme; other widths and the second theme follow, since six versions of a losing take are waste.
- A picked direction's 390 is finished in its own pass, art included, never stubbed for later. One that isn't a straight fold (a hero, art) runs the phone round in `references/rounds.md`.
- An object (a glyph, an icon) is sourced or constructed before it appears, never freehand. When takes differ mostly in where a visual that doesn't exist yet sits, rough the visual into each first; a gray box can't be judged.
- Walk the steer-yourself list, then lay the takes out on a review page (`references/rounds.md`) with a label card per row: the name, what it is, how it differs, the assumption, the weak spot, and the lead's lean. No critics yet: they polish a direction, and four rounds once polished a split layout the user didn't want.
- A taste call (a ground, a color, a texture, a layout) goes to the user drawn both ways, even when the critics agree; their vote and the lead's lean are inputs, not the pick.
- When the round is handed over, the surface's tracker issue moves to the waiting-on-the-user status in the same turn with a comment naming the call; it goes back to In Design the turn the reply arrives, with a comment saying what unblocked it, and so does every sub-issue parked with it.

The user picks on the canvas and gives feedback; no more variants unless asked.

## Steer yourself before showing

Before anything reaches the user (the direction round, the ready review), walk the steer-yourself checklist in `references/brief-and-review.md` against the real exports and fix what fails. Every steer the user gives is one they shouldn't have needed, so it joins the checklist the same turn.

## Polish loop

Silent, in this order, because each pass changes what the next one sees. It opens with the lead framing the pick and the user's feedback into one plan (on Quick, the planner's brief framing); after that the lead runs it. On a second surface onward, designers start from the approved surface's tree or a duplicate, and the first critic round adds a drift check against the approved screenshot and the token set (an oversized first pass, a new font treatment, glyph icons).

**Treatment.** A front door (a home screen, an empty state, an onboarding step) gets one, unasked, since "boring" is the first reaction to a plain one: read `references/treatment.md` and call visual-assets as a round inside the loop; its direction strip is the one look the polish loop shows the user, before any critic runs, and it hands back one named layer with its seed, parameters, and any new tokens. Empty and error states get it shrunk down; working screens skip it.

**States.** Clone the states from the base as their own artboards: empty, thin, loading, error, stale, each with a message and an action where it needs one. A state that adds no new fact isn't a state; drop it and note the idea. Loading never is that state: every surface that fetches gets one, front doors included. Every name and number on a state is real data, a front door's showcase included.

**Subtract pass.** Every element with its job, in the subtract template in `references/critics.md`; cut what doesn't earn its place, on a duplicate beside the base, before any critic is asked, because a critic can't see what should be gone.

**Expressive moments.** A flat working screen lacks depth or light, not motion. Name the two or three moments that earn a treatment (a live indicator, the primary action, a selected row) and run the checklist in `references/light-depth.md`: one still per moment on a duplicate, one technique each. The strip goes to the ready review as a decision; motion waits for the prototype.

**Critic rounds.**
- **Run.** Duplicate the base first, for the before and after. Export the ideal state at 2x and run three critics (`/impeccable critique` and two more), each scoring taste against visual-assets' `references/scorecard.md` and compliance against DESIGN.md, 0 to 10; the median of each is the round's score. Critics never see the code, the brief, prior scores, or references; every rubric carries the settled list (the user's calls and the lead's rulings) as do-not-raise. They prefer removing over adding (prompt in `references/critics.md`).
- **The bar.** Another round while median taste is under 8 or the critics split (taste scores more than two points apart). Stop at the bar, when median taste doesn't rise from one round to the next, when critics start reversing each other's fixes, or at the cap: five rounds on Full, two on Quick. Any of these stops the loop even below the bar, and the lead rules on the open findings.
- **Fix.** Between rounds the lead turns the goal-tagged findings into a fix list and the designer whose take won applies it. A finding that would move an element is structural even when the brief agrees, so it goes on a duplicate for the ready review; the user reads a reorder as a regression. Copy findings that make the page's numbers agree with each other are applied. After any round that added something, one line of subtract check.
- **The user's calls win.** A finding that reverses a settled call is logged and dropped, along with that critic's scores when it was the critic's top finding (the median of the two left is their mean). The user's named likes count as calls: a finding that would remove one is dropped, and one that only adjusts it is softened. A falling compliance score while the canvas follows the user's picks usually means DESIGN.md is behind: diff the doc against the picks and fix the doc first.
- **Log and scope.** Log every round (scores, findings, what changed and why) to `mockups/hifi/critique-<surface>.md`. A surface's front-door and working-screen states each get a loop; visual-assets runs this loop on its layer; motion isn't reviewed here. `/impeccable audit` runs once, after round one, for its AI-default detectors and build notes.

**Comparison pass** (Full), because a screen scored alone can reach the bar and still lose side by side: three fresh critics rank the ideal state against two or three gold screens for the same job, the user's favorites first. Ours first closes it; otherwise fix under the loop's rules and rerun once, outside the cap, and if ours still isn't first the table goes to the ready review. The procedure is in `references/critics.md`; gold screens never reach a designer.

**Contrast and the table lens.** The a11y MCP's contrast check on every new text-on-background token pair (all of them on the first surface), and the table lens in `references/checks.md` against the surface's tables and panels. Fix what names a goal, log taste.

## Ready review

One review page (`references/rounds.md`): the base with every state, the lead's pick first, a numbered callout per change the critics made (one line each on what moved and why, since the user can't overrule what they can't see), and the open decisions on duplicates beside it (structural findings, taste calls, the expressive strip). Show it as links to its artboards, never PNGs in chat; exports are for critics and the build. Before showing, read every open thread on every artboard of the surface, losers included, since the user comments mid-round.

- **"Good" is the done signal,** and the surface goes to Lock. A pick that comes with comments ("couple comments, otherwise good") is a go: the lead applies them without the planner, runs a polish pass and the critics, and locks with no second review.
- **Other comments:** one asking for a direction not yet drawn goes to the resumed planner as a direction round; the lead frames the rest into the next polish loop; the ready review comes back. These rounds have no cap; the user's done signal ends a surface, a critic's never does.
- **Read every thread** by the review intake in `references/paper-loop.md`. When a pin could mean two elements, name both and fix or show both.
- **Learn per thread.** When a thread generalizes past this surface, write the rule into `references/constraints.md` or the pick into `references/preferences.md` in the same turn, before the next thread. A pick already in the file means the pass missed it: sharpen the line only if it's scoped too narrowly, and log the miss for the pause's "we covered this" trace.
- **What a comment is.** It names the goal, the state, and the element; anything that can't be tagged with a goal is taste, noted and left. A question about a call ("do we need X?") is a prompt, not an instruction: take a position in chat and change nothing on the canvas until the user answers. A pin that names a defect ("weird gap here?") is a comment to fix. A note asking for exploration gets two or three variants on duplicates that differ in one thing. When the user is torn, render the failure case too (the sparsest data, the longest name).
- **One base, one axis.** Keep one base artboard per surface, the current answer, and give each open question its own strip of duplicates beside it. Weave each pick back into the base before the next opens, so two open questions never interact on one frame.
- **Ownership is the clobber rule** (`references/paper-loop.md`, Etiquette): a commented artboard is frozen and revised on a duplicate, and a user-made node is never deleted. Explore only on the surface's explorations page; Final holds picked designs only.

When a layout question keeps coming back, stop arguing on the canvas and propose a short research lane (on the user's yes) whose principle lands in DESIGN.md and constraints.md.

## Lock

Run the twelve checks in the done checklist in `references/checks.md` against each surface on its own; the step closes when every surface passes.

Then read `references/final-and-handoff.md` and lock the surface: artboards to the Final page in its fixed structure, renamed by surface and state, the Paper file size checked before every write, one last review there. Then the spec under Solution Details, in the user's voice, pushed on a yes with Open Questions refreshed. Then push the branch and open the PR; a step close that stays local isn't closed.

## Skill pause

Then authoring-skills' Closing a skill update, after every checkpoint the user reviews (the direction pick and each ready review), not only per surface, and never batched to the end, since learnings decay if they wait; it reads every thread on the surface, resolved ones included. What goes where in this skill: picks into `references/preferences.md`, rules into `references/constraints.md` (a recurring critic finding becomes one), a check into `references/checks.md`, a steer into the steer-yourself list in `references/brief-and-review.md`, a round mechanic into `references/rounds.md`, and prompts behind a bad first pass into `references/failed-prompts.md`, to rerun on newer models.

## Shared chrome

Any bar every surface shares is its own small surface, designed once: right after the first surface when the tab set is fixed, otherwise after the main ones (shared chrome, `references/final-and-handoff.md`).

## After the last surface

Once every surface and the shared chrome are on Final: a cross-surface polish pass (`references/checks.md`: control language, radius, and expressive moments carried everywhere, plus every open polish comment), then motion-design for anything that moves, then design-shaping's open-questions pass and final review. No journey rewrite; the specs already read in journey order.

## Prototype and handoff

At the prototype decision, read the prototype and handoff sections of `references/final-and-handoff.md`. Prototype only when a static artboard can't answer the question; call motion-design first when anything should move. Hi-fi ships still, and the motion spec joins DESIGN.md at handoff.

## Checklist

Only the steps that have actually been missed.

- Round plans, critique logs and reference reads committed the turn they're written; a workspace archive keeps only `.context`.
- The weight named in one line when the surface opened.
- Metric sidebar set before the direction round on any card, row, or panel surface.
- `references/constraints.md` read end to end and checked against the token plan before the first write.
- Every thread on every artboard read before showing; rounds shown as canvas links on the explorations page, never PNGs.
- A loading state on every surface that fetches; real data on every state.
- DESIGN.md diffed against the picks before acting on a falling compliance score; contrast proven by the lint and the a11y check.
- Carries swept across Final, the repo, and the doc; one fixture file; one element, one look.
- The branch pushed and the PR opened at the step close.

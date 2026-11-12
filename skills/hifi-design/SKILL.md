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

Hi-fi polishes a solution that already works. Structure was settled in lo-fi, so this step turns one dial, the visuals, and holds everything else fixed. The risk is the opposite of lo-fi's: not anchoring too early, but drifting into taste and clobbering what the user already approved. Every rule below is about locking what's decided, replacing the agent's defaults with the user's, and stopping on a signal instead of a feeling.

The canvas is Paper Desktop over its MCP server: real HTML with inline CSS, so what Claude writes is what the user sees, and what the user edits Claude reads back. Load dataviz for chart form and palette validation; better-ui is for build time.

Read each reference at its step:
- `references/paper-loop.md` before the first Paper call (dialect, tool sequences, etiquette).
- `references/design-md-template.md` before the taste interview.
- `references/brief-and-review.md` every surface, at its reference pass: the brief and reference templates, the steer-yourself list, the comment-round templates, and the things that go wrong.
- `references/preferences.md` every surface, before its first pass. The first pass starts from the user's picks, and directions vary only what the surface gives a reason to vary. `references/preferences-archive.md` holds the dated product picks behind it; read it only when a surface repeats one of those objects.
- `references/constraints.md` every surface, end to end, before the first write.
- `references/checks.md` every surface, at each round's steer pass and at Done: the revision checks, the table lens, the cross-surface pass, and the done checklist.
- `references/critics.md` at refine and polish: the subtract pass, the critic prompt, and the comparison pass.
- writing-style's `references/ui-copy.md` before writing a surface's copy.
- `references/treatment.md` at the treatment step; `references/light-depth.md` at expressive moments.
- `references/final-and-handoff.md` at Done, the shared chrome, and the prototype decision; `references/type-rendering.md` before the `ui/` spec.
- `references/inside-a-build.md` when a build's Design Needed issue calls this loop.
- `references/learnings.md` and `references/failed-prompts.md` at the skill pause.

## Before the canvas

Interview the user before drafting anything, one question at a time, with the eight questions in `references/design-md-template.md`: feel and must-not words, the world it belongs to, one signature detail, a product to be mistaken for and its one trait, grays, accent, typeface, and a never-see list. Mechanics come from research and the wireframes; taste has to come from the user.

Draft DESIGN.md in the template's shape, following its drafting notes. Present it as a text summary and as the system artboard on the Paper canvas (Setting up the canvas), dark and light side by side, with the spec's lint (`npx @google/design.md lint`) beside it, rerun whenever DESIGN.md changes; a contrast claim in prose isn't proof. The user reviews a design system in Paper, never as an HTML specimen or a PNG in chat; a rendered specimen page is the agent's own check before the canvas. Iterate until approved, then push it to the product doc as an appendix toggle.

DESIGN.md is brand v0: brand-design comes after design-shaping's gate (zero-to-one's Branding step), since every canvas value is a token and the swap is cheap before any code.

## Setting up the canvas

Once per product, in its own session. Go Pro first; the free tier's weekly call cap dies mid-write. Confirm the files (a Final file, an Explorations file and an Archive file; `references/final-and-handoff.md`, "Three kinds of Paper file") and make the pages: "🏁 Final" in the Final file for locked artboards only, and one "🚧 <Surface> · Explorations" per surface in the Explorations file (emoji, surface, middle dot, Explorations in title case). Check the typeface is available and compile DESIGN.md into Paper tokens (palette, then the semantic aliases). Then build a system artboard (swatches, type scale, a table row, a card, the controls, each chart form): the clone source for every surface, approved by the user before any screen exists.

## The per-surface loop

Every surface runs the same order, and the order is most of the skill: metric sidebar, reference pass, brief with the user's yes, one directions round, comment rounds to the done signal (each round steered by the agent before the user sees it), treatment for front doors, states, refine and polish (open comments, subtract pass, expressive moments, scored critic loop, comparison pass, critic changes shown, a11y and the table lens, done checklist, Final row, spec), then the skill pause. The sections below are those steps in sequence. Skipping ahead costs a round.

## Metric sidebar

First, on any surface built from cards, rows, or panels, run the metric sidebar with the user, because a directions round on an unweighted set is wasted. List every number and mark, its job for the user (trust, act, or leave), and its size tier (hero, supporting, action, off the face). One hero, one supporting line, one action is the shape of a card. The fixed metric order from research says what comes first; the sidebar says what's big.

Then a stats check on every number kept: a comparison shares its sample, null, and unit with what it's compared to, and copy that paraphrases a number says what the number says. A measure that fails comes off even when the user likes it (offer the matched version), and so does any measure that assumes a user action the app never sees. Then the metric-name test: say "62% [name]" out loud; a percentage needs the thing it's a share of, and a name that doesn't finish that sentence gets renamed. Get the user's yes on the table; directions then vary presentation of the weighted set only.

## Reference pass

Then gather references, as text, following the reference report section of `references/brief-and-review.md` (Mobbin searches, explain-interface on the two or three that matter most, the Playwright fallback). When design-shaping's competitive look has a report, reuse it and search only for what's new. Five to eight references, each annotated by technique rather than feeling (line weights, hue count, density, structure, what carries meaning), link kept. Save it as `mockups/hifi/references-<surface>.md` with a small HTML report of the images for the user. Close with one "not this" anti-reference and one line naming the audience the surface must perform for.

The build agent gets the annotated text list only, never images or taste words; technique notes hold a design system without drift.

## The brief

Hand the agent artifacts that fix the answer, not adjectives that invite one, in the brief template: the converged wireframe file and screenshot, the decision the screen supports, the goals it serves, the metric hierarchy and tiers, the references as text, the final copy verbatim, real data rows, the states, the losers and why they lost, the surface's standing rulings (or an older duplicate revives reversed calls), and DESIGN.md.

- Say that layout, reading order, element inventory, and copy are locked; only type, color, spacing, borders, and chart styling change.
- Say that DESIGN.md overrides Paper's style guide, or the agent drifts toward the canvas's house taste.
- Withhold the other explorations, every competitive screenshot, and taste words.
- When the brief reuses a pattern, name its node and say "match it exactly"; where the brief and an existing pattern disagree, the pattern wins.
- Every direction carries one concrete aesthetic sentence and the assumption it tests ("hairline table, the monthly change at 28px in sign color, everything else at 13px gray; assumes the number is what earns trust"), never "unique" or "clean". A direction without its sentence is a layout shuffle.
- Don't paste the wireframe's HTML; its classes would be dropped. Point at the file and rewrite it in Paper's dialect.

Post the brief in chat and get the user's yes before the first write. When the project keeps a running direction page (a Notion page for the agent's findings), write the brief there in the same turn, beside the repo copy.

Before the first artboard, write a token plan and check it four ways, in order:
1. The collision test: plan a similar brief (same job, another product); wherever the two land close, change direction on that axis and say why.
2. The five AI-look clusters in `references/constraints.md`. Bans relocate the default; colliding and moving off doesn't.
3. `references/preferences.md`: use the user's picks; where there are none, the directions round earns its place.
4. `references/constraints.md` end to end, every rule against the plan, before the first write, not at polish.

## Directions

One artboard per surface per turn, named with the surface and a version, built to `references/paper-loop.md`'s etiquette: small writes, a 2x screenshot after each, style updates over rewrites, the working indicator released, no node IDs in chat.

Three artboards side by side, differing in density or reading order, never in color, plus one or two wildcards when the user asks for range (usually), on crux surfaces only (design-shaping step 2). When the user says a round is too incremental, the next adds four or five bold swings from outside references beside the safe set. Layout ideas can be sketched; an object (a glyph, an icon) is sourced or constructed before it appears in a round, never freehand. The user picks one on the canvas; no more variants unless asked. When a decision needs the user's call, put it on the canvas as a duplicate before asking ("show me" answers every described option). That's for options you propose; a question the user asks gets a position in chat and no canvas change (Comment rounds).

## Steer yourself before showing

Before any round reaches the user (directions, comment rounds, a Design Needed round inside a build), walk the steer-yourself checklist in `references/brief-and-review.md` against the real exports and fix what fails. Every steer the user gives is one they shouldn't have needed, so it joins the checklist the same turn.

## Comment rounds

Review happens on the canvas: the user pins comments, selects a node and describes the change, or hand-edits. When a round's inputs need weighing (several comments, critic findings, a reference to chase), the planner role turns them into the round's plan first, by build's `references/design-loop.md` ("The planner frames every round"); a single concrete edit just gets made.

- **Where work lives.** Explore only on the surface's explorations page; Final holds picked designs only, and a round reaches it after the user picks. Show every round as links to its artboards (the page URL with the artboard's node parameter), beside a copy of what they replace, never as PNGs in chat. Exports are for critics and the build.
- **Read every thread.** At the start of every round and again before showing anything, read every open thread on every artboard of the surface, losers included (their notes usually apply to the winner), not only those mentioned in chat; the user comments mid-round. Map each comment's x/y offset on its container frame to an element on the screenshot before acting. Work each, screenshot, resolve, and report per thread in chat (there's no reply tool) as done, partial, or needs a call.
- **Learn per thread.** When a thread generalizes past this surface, write the rule into `references/constraints.md` or the pick into `references/preferences.md` in the same turn, before the next thread. A pick already in the file means the pass missed it: sharpen the line only if it's scoped too narrowly, and log the miss for the pause's "we covered this" trace. Learning starts here, not at the pause.
- **What a comment is.** It names the goal, the state, and the element; anything that can't be tagged with a goal is taste, noted and left. A question ("do we need X?") is a prompt, not an instruction: check references, take a position in chat, and change nothing on the canvas until the user answers. A note asking for exploration gets two or three variants on duplicates that differ in one thing, each naming its assumption, and the user picks. When the user is torn, render the failure case too (the sparsest data, the longest name), not just the options.
- **One base, one axis.** Keep one base artboard per surface, the current answer, and give each open thread its own strip of duplicates beside it. Weave each pick back into the base before the next thread opens, one axis at a time, so two open questions never interact on one frame. Fixes that need no decision land in the same pass.
- **Ownership is the clobber rule.** Touch only nodes created this run. Before editing an artboard, list its threads; one comment means it's frozen, and revisions go on a duplicate beside it, never parented into it. Never delete a node the user made. The user doesn't edit an artboard while the working indicator is on.

When a layout question keeps coming back, stop arguing on the canvas and propose a short research lane (launched on the user's yes): what the field does, what the design-system literature says, three to five principles, a recommendation, with the principle written into DESIGN.md and constraints.md. There's no revision cap; rounds run until the user says the surface is good, which is the done signal. Second surface onward, start from the approved surface's tree or a duplicate, then run a fresh-context drift critique against the approved screenshot and the token set; drift (an oversized first pass, a new font treatment, glyph icons) is the common failure.

## Treatment

Once the structure-locked pass is approved, ask whether this surface is a front door (a home screen, an empty state, an onboarding step) or a working screen (a results panel). Expect "boring" as the first reaction to a plain front door, and open the treatment axis before the user has to say it. For a front door, read `references/treatment.md` and call visual-assets as a round inside the loop, not a pass after it; it hands back one named layer with its seed, parameters, and any new tokens. Empty and error states get the same loop shrunk down. Working screens skip this.

## States

Once the user is happy with the ideal state (and the treatment, on a front door, since it decides what empty, thin, and error show), clone the states from the base as their own artboards: empty, thin, loading, error, stale, each with a message and an action where it needs one. A state that adds no new fact isn't a state; drop it and note the idea. Loading never is that state: every surface that fetches gets one, front doors included. Every name and number on a state is real data, a front door's showcase included.

## Refine and polish

Before the done checklist, in this order, because each pass changes what the next one sees.

Open comments first. Gather the user's open comments on the base: they're the polish agenda, and every later pass proposes against them rather than around them.

Then the subtract pass: every element with its job, in the subtract template in `references/critics.md`; cut what doesn't earn its place and show the cuts as a duplicate beside the base before they land. A line that says "nothing" on every card, a helper that restates its field, a legend for a self-naming column all go before any critic is asked, because a critic can't see what should be gone.

Then expressive moments, before any critic scores the base. A working screen on light paper reads flat because nothing has depth or light, not because it needs motion. Name the two or three moments that earn a treatment (a live indicator, the primary action, a selected row) and run the checklist in `references/light-depth.md`: one still per moment on a duplicate, one technique each, the strip shown as a decision. Picks go into DESIGN.md's elevation section and `references/preferences.md`; motion waits for the prototype.

Then the scored critic loop, because by the last round the agent and the user have both stopped seeing the surface.
- **Run.** Duplicate the base first, for the before and after. Export the ideal state at 2x and run three `critic` agents in fresh contexts, screenshot only (Model: critic role): `/impeccable critique`, and two scoring taste against visual-assets' `references/scorecard.md` and compliance against DESIGN.md, 0 to 10 each, separately; the median of each is the round's score. Critics never see the code, the brief, prior scores, or references; each prompt lists the user's standing calls as do-not-raise (authoring-skills, Harness principles). They prefer removing over adding, scoring any addition as a cost (prompt in `references/critics.md`).
- **Stop.** Cap three rounds; stop early when both scores reach 9 or when neither gains a full point, since the fourth round is taste drift. A finding that re-raises one of the user's calls anyway is logged and dropped, never an argument to reopen it; a round whose findings are all re-raised calls is done.
- **Fix.** Between rounds apply the goal-tagged fixes. A finding that would move an element is structural even when the brief agrees, so it goes on a duplicate and gets asked about; the user reads a reorder as a regression. Copy findings that make the page's numbers agree with each other are applied without asking. After any round that added something, one line of subtract check.
- **The user's calls win.** When a finding contradicts a call the user made on the canvas (a removed label, a chosen metric order), the call wins; log the finding and the thread it lost to. The user's named likes (a bold label, a callout box) count as calls: the like stays and the fix is softened.
- **A falling compliance score** while the canvas follows the user's picks usually means DESIGN.md is behind the decisions: diff the doc against the picks and fix the doc first.
- **Log and scope.** Log every round (scores, findings, what changed and why) to `mockups/hifi/critique-<surface>.md`. A surface's front-door and working-screen states each get a loop; visual-assets runs this loop on its layer; motion isn't reviewed here. `/impeccable audit` runs once, after round one, for its AI-default detectors and build notes; its contrast concern is the token check below.

Then the comparison pass, because a screen scored alone can reach a 9 and still lose side by side: three fresh `critic` agents (Model: critic role) rank the ideal state against two or three gold screens for the same job, the user's favorites first. Ours first closes it; otherwise fix under the loop's rules and rerun once, outside the cap, and if ours still isn't first the user decides. The procedure is in `references/critics.md`; gold screens never reach the agent drawing.

Then show the user what the critics changed: the pre-loop base beside the current one on the explorations page, a numbered callout per change, one line each on what moved and why. The user can't overrule what they can't see.

Then the a11y MCP's contrast check on every new text-on-background token pair (all of them on the first surface), and the table lens in `references/checks.md` against the surface's tables and panels. Treat it all as comments: fix what names a goal, log taste.

## Done

Run the twelve checks in the done checklist in `references/checks.md` against each surface on its own; the step closes when every surface passes.

Then read `references/final-and-handoff.md` and lock the surface: artboards to the Final page in its fixed structure, renamed by surface and state, the Paper file size checked before every write, one last review there. Then the spec under Solution Details, in the user's voice, pushed on a yes with Open Questions refreshed. Then push the branch and open the PR; a step close that stays local isn't closed.

## Skill pause

Then authoring-skills' Closing a skill update, after every surface rather than at the end, since learnings decay if they wait; it reads every thread on the surface, resolved ones included. What goes where in this skill: picks into `references/preferences.md`, rules into `references/constraints.md` (a recurring critic finding becomes one), a check into `references/checks.md`, a steer into the steer-yourself list in `references/brief-and-review.md`, and prompts behind a bad first pass into `references/failed-prompts.md`, to rerun on newer models. Taste is the half that stops the next surface repeating the mistake.

## Shared chrome

Any bar every surface shares is its own small surface, designed once after the main surfaces, since it can't be settled before it knows them. Until then each artboard carries a placeholder for its own tab, and tab renames reach every artboard the same day. When its turn comes, read the shared chrome section of `references/final-and-handoff.md`.

## After the last surface

Once every surface and the shared chrome are on Final: a cross-surface polish pass (`references/checks.md`: control language, radius, and expressive moments carried everywhere, plus every open polish comment), then motion-design for anything that moves, then design-shaping's open-questions pass and final review. No journey rewrite; the specs already read in journey order.

## Prototype and handoff

At the prototype decision, read the prototype and handoff sections of `references/final-and-handoff.md`. Prototype only when a static artboard can't answer the question; call motion-design first when anything should move. Hi-fi ships still, and the motion spec joins DESIGN.md at handoff.

## Inside a build

When a build's Design Needed issue calls this loop, read `references/inside-a-build.md` before the exploration brief: it runs in chat, drawing starts the same turn, and feedback on a built surface becomes a rule change or a papercut.

## Things that go wrong

The list is at the end of `references/brief-and-review.md`, read with the rest of that file at each surface's reference pass.

## Checklist

Only the steps that have actually been missed.

- Metric sidebar approved before the first directions round on any card, row, or panel surface.
- `references/constraints.md` read end to end and checked against the token plan before the first write.
- Every thread on every artboard read at each round's start and before showing; rounds shown as canvas links on the explorations page, never PNGs.
- A loading state on every surface that fetches; real data on every state.
- The expressive strip shown as a decision.
- DESIGN.md diffed against the picks before acting on a falling compliance score; contrast proven by the lint and the a11y check.
- Carries swept across Final, the repo, and the doc; one fixture file; one element, one look.
- The Paper file size checked before every write.
- The branch pushed and the PR opened at the step close.

# Final page, shared chrome, prototype, and handoff

Read the Final page and spec sections at Done, before moving a surface's artboards; the shared chrome section when its turn comes after the main surfaces; the prototype and handoff sections at the prototype decision. The dated cases behind these rules are in `learnings.md`.

Contents: The Final page · Three kinds of Paper file · The spec (and lists of model-written text) · Shared chrome · Prototype · Handoff (the README, the default motion block)

## The Final page

Move the locked artboards to the Final page, renamed by surface and state ("Invoices · ideal", "Invoices · thin data"), and ask for one last review there before the spec. The user reads the row differently from the explorations page. The Final page always has the same structure:

- One row per surface in journey order (nav first, then each surface in the order a user meets it, then a last row for dialogs and overlays), with a text label at each row's left.
- The ideal state first in each row, then the other states in a fixed order (opened or expanded, thin, empty, stale, error, plus each surface's own), 1600 apart.
- Every case the fixtures define is present, and gaps are listed rather than invented.
- Superseded artboards move to the explorations page, marked "(superseded)", and are never deleted.
- One element, one look across Final: when an element changes, every Final artboard that draws it is updated in the same move (search the Final page by node name and text, then duplicate the new version into place). Two artboards that disagree confuse the user and the build alike.
- Every pick lands here in the same session, and so does a build's redesign (a new element, a moved one, a new hierarchy), drawn here before it's built. A build tweak (copy, spacing, color, a bug fix) is built from code and lands here in the build's hardening close, in its one Final pass, with one re-export and one token sync; until then the code wins. Final is the design's source of truth, and the design exports the browser tests read come from it.
- When a cross-cutting pattern changes (number format, icons, label treatment, colors), a consistency pass runs across every surface on the page, not just the one where it changed.

## Three kinds of Paper file

A Final file, an Explorations file, and an Archive file. Paper's size limit is per file, so pages inside one file don't help.

A small product (a personal site, a few surfaces) starts as one file named for the product, with a page for each body of work: the system, "🚧 <Surface> · Explorations" for each surface, and "🏁 Final". Split it into the three kinds only when the size warning appears.

- **When each gets too big:** Final splits into several Final files by surface. Explorations sends its abandoned explorations (losers, superseded rounds) to Archive. Archive spins out a new Archive file.
- **When to check:** look for the "file is too large" warning before every write, and split before editing, never after. The warning goes stale until the app reloads, so check again after a reload before acting on it.

## The spec

Export the ideal state at 2x into the mockups folder. The spec goes under the product doc's Solution Details as a numbered heading per surface ("1. Invoices"), never a toggle: the surface in order, per-element rules, a states table, transitions, the rules the user reads, rabbit holes, the prototype decision.

- Write it in the user's voice through writing-style before it reaches chat: no framing sentence that restates the structure ("Two screens. The list shows..."), and section labels that name the thing ("The list", "One invoice"), not the method ("Reading order, the list").
- The image is the state the user would show someone. One inline frame, the ideal state, right after the reading order; the states table links to the Final page instead of embedding every state.
- Image blocks can't be edited or removed through the API afterwards, so be sure before inserting one.
- Show the spec, push it on a yes, and refresh Open Questions in the same push. Then push the branch and open the PR; a step close that stays local isn't closed.

### Lists of model-written text

A surface that renders model-generated text in bulk (summary lines, generated titles, theme cards, a digest) is read two words per item, so the rules go into the generation prompt the spec hands the build, and the fixtures carry a realistic batch rather than one hand-polished line.

- Start each item with its subject or its verb. When every item shares the subject, drop it and lead with the verb, in one tense.
- Put the words that tell this item apart from the others first ("Shipped: order 1001", not "Your order 1001 has shipped").
- One structure and one word per concept across every item.
- Vary length, structure, or an extra detail only to mark a real difference; a version number on one card reads as meaning the others don't have one.
- Pick verbs whose connotation matches the surface's job ("users complain", "users love").

## Shared chrome

The nav, header, or any bar every surface shares is its own small surface, designed once after the main surfaces because it can't be settled until it knows all of them: the tab set, the active states, and whatever is global (a product name, search, an account mark). Until then every artboard carries a placeholder that reflects its own tab, and tab renames propagate to every artboard the same day.

When its turn comes it gets a short loop: a brief, two or three directions, a pick, then it's cloned into every Final artboard and the spec gets a short section of its own.

- References: Navbar Gallery is worth one pass (about 550 navs, filtered by type: sticky, sidebar, search bar, breadcrumbs), filtered to monochromatic and typographic; navbar.design adds about twenty more. Both are marketing-site navs, so Mobbin's app shells carry the app patterns and the galleries top up with an idea or two.
- Draw the directions over the real top of two surfaces (a collection page with its filters and an object page), not a bar alone, since a nav is judged against what sits under it.
- Tab copy gets its own short round after the pick: a bunch of ideas per tab, a proposal with fallback sets, tested by saying them aloud and against the page's primary button.

## Prototype

A prototype is small, one per motion or control with only enough screen to judge it, never the whole app. Prototype when a static artboard can't answer the question you'd ask a user: a loop, more than two states, a control whose feel is the question. Static reads get an artboard and a states table. Record the decision either way, with the reason.

- Build it in code with fake data; a coded prototype keeps most of its structure through build.
- When a control's feel is the question, expose its motion tokens as DialKit knobs (MIT, a vanilla adapter) with min and max set to the rulebook's range. The user tunes, the values are copied into the spec table before the file changes, and the panel never ships.
- When the question is which version (two or three ways a control could work, or two research lanes that disagree), put the versions behind one switcher, not in separate files or a strip of thumbnails: one version at a time, full size, in the real screen around it, flipped with number keys or arrows, R to replay its motion, the pick in the URL (`?v=2`) so a reload or a shared link lands on the same one, and the swap itself instant.
- Each version diverges on a named axis and fully works on the product's fixture data; two that differ only in color or copy are one version, so cut one and say so.
- The switcher is chrome, not a contestant: copy `picker.md` verbatim and never theme it with the product's tokens.
- Present each version with one line on when it wins and one on what it costs, with your lean and runner-up. After the pick, a riff round can diverge around the winner; the losers stay reachable in the file as the record, and only the winner moves into the spec.
- When anything on the surface should move, call motion-design before writing the prototype: it lists which motions earn a job, researches the specific ones, writes the tokens and a spec table, lays a keyframe strip on the explorations page for approval, then builds the HTML prototype, records it, and runs the vendored review-animations skill on the code. Motion never enters the canvas artboards themselves; hi-fi ships still.

## Handoff

Handoff comes off the canvas, not from screenshots.

- The tokens as CSS.
- The JSX per artboard with inline styles. No Tailwind theme: it rounds a 13px table to the nearest utility, so runtime styling is plain CSS against the token variables.
- Computed styles for exact values, and a mapping file of artboard IDs and frame links.
- The `ui/` spec: one entry per component DESIGN.md names, with the primitive it wraps, its token-resolved styles per state, and the Final node it matches. The build's first milestone writes `src/ui/` from it, and tech-planning's `references/libraries.md` holds the rules. Read `type-rendering.md` before writing it.
- A "Specimen · ui" artboard in the Final page's last row drawing every entry in every state, which the build's `/dev/ui` route mirrors.
- A states and transitions table per surface (this is Solution Details).
- A README with the stack, file layout, and the done checklist.

Write the motion spec into DESIGN.md at handoff, not before; hi-fi ships without motion.

### The README

Stack and file layout; the tokens as CSS from the canvas and that CSS variables are generated from DESIGN.md; the JSX per artboard (inline styles) and computed styles; a mapping file of artboard IDs, frame links, and fidelity notes; the `ui/` spec (primitive, styles per state, Final node per component) and the Specimen · ui artboard; the screens per state at 2x; the transitions table (pointer to Solution Details); the done checklist; open questions.

Two contracts for the build. Tables ship as real tables: a caption, `th scope="col"`, first-column row headers with `scope="row"`, a horizontal-scroll wrapper with `tabindex="0"`, and never restyled with `display`, which strips the semantics. Components are named by their majority name on component.gallery with the product's alias in parentheses, and each lists its named parts.

### The default motion block (DESIGN.md, at handoff)

```
## Motion
Durations: 100ms press and toggle; 150ms hover, color, opacity, exit; 200ms enter, collapse, panel; 250ms same-series chart update. Nothing above 300ms.
Easings: cubic-bezier(0.23, 1, 0.32, 1) for enter, exit, collapse; cubic-bezier(0.4, 0, 0.2, 1) for on-screen movement and chart paths; ease for color and opacity. Never ease-in. Linear only on progress.
Springs: none. Properties: transform, opacity, clip-path only. Never height, width, padding, margin, transition: all.
Enter: opacity 0 to 1, translateY 4px to 0, 200ms. No scale under 0.95. No stagger.
Exit: opacity to 0, 150ms, leaves the way it came.
Charts: no draw-in on load. Same-series update interpolates 250ms. Different series or domain: 150ms cross-fade. No pulsing points.
Numbers: no ticking. Cross-fade 150ms with tabular-nums; color changes with the value.
Frequency rule: anything used more than a few times per session gets no motion (view toggles, filters, keyboard actions). Nothing animates on first render.
Reduced motion: transforms off, fades stay. Theme switch: no transitions. Every animated change has a static cue.
```

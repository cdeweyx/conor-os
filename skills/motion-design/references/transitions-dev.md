# Transitions.dev and Libraries.dev

Two build-step tools by Jakub Antalik. Neither renders on a Paper still; both go to the prototype and the build. [Transitions.dev](https://github.com/Jakubantalik/transitions.dev) is thirty-two copy-paste CSS transitions "each namespaced under `t-*` selectors with semantic CSS custom properties", no framework dependencies, and "every snippet ships a `prefers-reduced-motion` guard". [Libraries.dev](https://github.com/Jakubantalik/Libraries.dev) is seven React effect packages with a placement skill. Sources: [transitions-dev SKILL.md](https://raw.githubusercontent.com/Jakubantalik/transitions.dev/main/skills/transitions-dev/SKILL.md), [transitions-polish SKILL.md](https://raw.githubusercontent.com/Jakubantalik/transitions.dev/main/skills/transitions-polish/SKILL.md), [`_root.css`](https://raw.githubusercontent.com/Jakubantalik/transitions.dev/main/skills/transitions-dev/_root.css), [libraries-dev SKILL.md](https://raw.githubusercontent.com/Jakubantalik/Libraries.dev/main/skills/libraries-dev/SKILL.md). Fetched September 2026.

## The catalog

The skill's own decision rule: "match against the visible UI element first, then the verb", and "If two transitions could fit, prefer the lower-overhead one (card resize over panel reveal, dropdown over modal, success check over a full modal celebration)." "No clear match → fall back to `transitions reveal` and let the user pick. Don't guess." Sixteen need a small JS orchestration snippet; shimmer text is pure CSS. Grouped by the moment each serves:

- A surface opens or changes shape: menu dropdown (grows from its trigger, origin-aware), modal open / close, panel reveal (slides into a region with a cross-blur), page side-by-side (list to detail), plus to menu morph, accordion expand, card resize (tween a container's width or height).
- A value changes in place: number pop-in ("Re-enter each digit with a blurred slide when a number updates"), spinning counter (slot-machine reels), text states swap (blurred up-and-down), icon swap (cross-fade in the same slot).
- Something is waiting: skeleton loader and reveal ("Pulse a placeholder, then cross-fade + cross-blur to the loaded content"), shimmer text, thinking states ("Shimmer a status line while it holds, then swap it to the next state"), reasoning stream, streaming text, matrix dot loader.
- Feedback on an action: success check, error state shake, checkbox check, toggle, like button, input clear with dissolve.
- Hints and hover: tooltip open / close (delayed in, instant out), avatar group hover, learn more hover, card hover tilt.
- Notices and navigation: notification badge, toast open / close, banner stacking, tabs sliding ("Slide the active pill between tabs in a segmented control"), texts reveal (staggered blurred rise for stacked lines).

For a data product, by the skill's own rules: number pop-in or spinning counter when a total refreshes, text states swap for a run's status line, thinking states for a run in progress ("Scanning 1,140 records"), skeleton loader and reveal for results, tabs sliding for a segmented control, tooltip, toast. Not a data product: like button, card hover tilt, avatar group hover, plus to menu morph, success check as a celebration, reasoning stream, streaming text, matrix loader. They're the wrong register for a data tool, or the rulebook's frequency gate cuts them.

Common mistakes the skill names, worth reading before the build: "Replacing `transition: …` with `transition: all`", "Animating a single container instead of the inner pieces", and "Morphing the accordion chevron's `d` path" because "CSS `d:` path interpolation is Chromium-only".

## The token table, mapped onto ours

Transitions.dev's scale carries a usage per row, and usage is what its polish add-on matches on: "match on usage, never on the nearest number". "A `300ms` modal close maps to `--duration-quick` (150ms) because both are 'modal close', even though the numbers differ." This system keeps three durations and one out curve; the rest of the scale maps onto them or has no equivalent.

| Their token | Value | Their usage (verbatim) | Ours |
| --- | --- | --- | --- |
| `--duration-stagger` | 40ms | per-item stagger offset | `--stagger` (rulebook: 40 to 80ms) |
| `--duration-micro` | 80ms | tooltip/path delay, shake segment, large stagger | none; the rulebook's 80ms hover-open wait is the same number |
| `--duration-quick` | 150ms | modal/dropdown close, text swap, tooltip appear | `--duration-quick` 150 |
| `--duration-fast` | 250ms | icon swap, dropdown/modal open, tabs sliding, page slide | `--duration-fast` 250 |
| `--duration-medium` | 350ms | panel close, toast close | none; use `--duration-fast` |
| `--duration-slow` | 400ms | panel open, skeleton content reveal, input clear | `--duration-slow` 400 |
| `--duration-very-slow` | 500ms | emphasis moments, badge appear, text reveal, success check | none; cut the moment or use `--duration-slow` |
| `--ease-smooth-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | modal/dropdown/panel open + close, page slide, resize, position change | `--ease-smooth-out`, our out curve; Emil's `cubic-bezier(0.23, 1, 0.32, 1)` is the same family |
| `--ease-in-out` | `ease-in-out` | icon swap, text swap, text reveal, skeleton reveal | in-out |
| `--ease-linear` | `linear` | shimmer, skeleton pulse, spinner | linear, tickers and loops only |
| `--ease-bounce`, `--ease-bounce-strong` | `cubic-bezier(0.34, 1.36, 0.64, 1)`, `(0.34, 3.85, 0.64, 1)` | badge pop open, bouncy hover-out | none; the spring preset with damping near 1, and only on a spatial entrance |
| `--scale-large` to `--scale-tiny` | 0.96, 0.97, 0.98, 0.99 | modal open, dropdown open, tooltip open, dropdown close | none as tokens; the rulebook floor is no scale under 0.95, so all four pass |
| `--blur-small` to `--blur-large` | 2px, 3px, 8px | swaps and reveals, page slide, success check | none as tokens; blur stays under 20px and off plain fades |

`--duration-slow` at 400ms sits above the rulebook's 300ms ceiling for UI. It's reserved for a panel open and a skeleton reveal, review-animations will flag it, and each use needs its reason in the spec table. Transitions.dev's own `_root.css` ships literal values per snippet, so `transitions refine` is what maps them back to these names.

## transitions-polish: the asymmetry rules

The add-on audits motion that already exists against the same scale. Its rules, quoted ([transitions-polish](https://raw.githubusercontent.com/Jakubantalik/transitions.dev/main/skills/transitions-polish/SKILL.md)):

- "Opening is an invitation; closing should get out of the way. Closes are faster and quieter than opens." "dropdown/modal **open 250ms → close 150ms**"; "panel **open 400ms → close 350ms**".
- "Symmetric exceptions", same duration and easing both ways: "page side-by-side (250ms), tabs sliding (250ms), accordion (250ms), icon swap (250ms), text swap (150ms). These read as a single reversible motion, not an open/close pair."
- "the enter phase carries the distance and blur; the exit can drop or shrink them so a close doesn't fling content across the screen."
- "Overshoot curves belong to *entrances only* (badge pop, number pop-in)" and "never bounce a close."
- "Keep the **total** stagger (offset × item count) under ~300ms so the last item doesn't feel late", and for long lists "cap the number of staggered items or shrink the offset."
- "A delay is right when you want to *filter accidental triggers* or *sequence* two things", "not to pad a slow animation." "if motion feels late, prefer trimming the **duration** over adding delay."
- "Never delay a close or a hover-out", because "dismissal must feel instant."
- Hover: "In: quick and direct... Out: softer and springier". This is the one rule we don't take; the rulebook keeps hover-out at the same curve, and a bouncy return on a data table is noise.

## transitions review at the frame step

`transitions review` is read-only. It scans "`transition:` declarations, `@keyframes`, hardcoded `ms` / `s` durations in style files, components matching the decision-rule patterns", matches each hit against the decision rules, and prints a numbered list grouped by file with the single best-fit transition per hit, then "Do not edit anything." The polish version of the same verb also checks open/close asymmetry, hover in/out, stagger totals, and delays, and lists off-token values as `usage: value → var(--token)` with a one-line reason.

At motion-design's frame step, after the candidate list has a job or a cut for every motion, run it on the prototype's markup (or on the built surface at the build) as a second opinion. Take its adds only where they name a job the list missed; its suggestions are matched on element shape, not on whether the motion earns its place, so the frequency gate and the reveal rule still apply. Run the polish `transitions review` again on the prototype's CSS before the review-animations pass, and fix asymmetry and stagger totals there.

## Libraries.dev on a light warm theme

Two of seven survive on light paper without paying for Pro, and both are the "light" tier in the author's own cost ranking ("Thinking orbs and Border beam are light; Voice, Bot avatars and Gooey are moderate; Liquid metal and Image run WebGL"). The wait rule is taken as written: "Under 2 s: Nothing. No orb, no beam." "2 s or more: Thinking orbs, usually beside a text label." "More than 3 s: Also Border beam on the element doing the work (`active` from the loading flag)."

- Border beam (`border-beam`): `<BorderBeam size="pulse-inner" colorVariant="mono" theme="light" strength={0.7}>` on the card doing the work, after a three-second wait. The reference's own note: default is `theme="dark"`, and "On a white card, set `theme="light"`. The dark tuning looks washed out there." Pulse only; the Rotate types "do not handle `prefers-reduced-motion`".
- Thinking orbs (`thinking-orbs`): a 20px orb beside the status label after two seconds, `theme="light"` (draws dark dots) or `auto`. Plain 2D canvas, "no WebGL, no `ctx.filter`".

The other five don't: Gooey is dark-first with light themes behind Pro and needs transparent items; Voice is dark-only in the free tier and needs voice input; Bot avatars has no theme prop and is the wrong register for a data tool; Liquid metal runs WebGL2 and "Reflections do no work in light theme"; Image is a generation placeholder, for products with generated images. The skill's own density rule still binds the two survivors: "never two effects on the same element or on elements right next to each other", and "never leave a dark-tuned effect on a light page".

## Install, at the build, not before

```
npx skills add Jakubantalik/transitions.dev
npx skills add Jakubantalik/transitions.dev -s transitions-polish
npx skills add Jakubantalik/Libraries.dev
npm install border-beam thinking-orbs
```

Per transition, `npx transitions-dev add <name>` (for example `card-resize`). The skills ask before installing a package; let them. review-animations still judges the result; these skills don't review their own output, and an approval from it's what closes the motion step.

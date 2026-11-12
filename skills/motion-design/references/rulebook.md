# Motion rulebook

The numbers practitioners converge on (Emil Kowalski, Rauno Freiberg, Vercel's guidelines, Material 3, Apple HIG), condensed for a data product.

## Tokens

- Durations: fast 120ms (micro feedback), base 200ms (standard UI, reveals), slow 280ms (modals, larger moves). Nothing over 300ms except a chart draw-in (600 to 900ms), ambient loops, and a hold's progress fill. Exits about 20% faster than entrances.
- Easings: out (entering, user-triggered), in-out (moving on screen), linear (when data or progress sets the pace: tickers, a draw on a time axis, a hold's fill). Never ease-in for UI. The out curves the tier ships (measured in Linear, Stripe, Clerk, and Raycast bundles, October 2026): easeOutCubic `cubic-bezier(.33,1,.68,1)` as the base, easeOutExpo `cubic-bezier(.16,1,.3,1)` for one large move. Springs with damping near 1 for spatial moves; no overshoot on opacity or color. The spring preset is one CSS `linear()` string generated once from Easing Wizard (its MCP server or the web app), with mass, stiffness, and damping recorded beside it, so a spatial move can spring without a library.
- Stagger: 40 to 80ms between siblings, and step times count stays under 300ms, so cap the items or shrink the step. Follow-through: labels and icons land 100 to 200ms after their container.
- As CSS variables: `--motion-fast`, `--motion-base`, `--motion-slow`, `--ease-out`, `--ease-in-out`, `--spring`, `--stagger`.

## Rules

1. One orchestrated reveal on load, in element order; nothing else animates on load.
2. Motion answers a user action or shows a value being measured. Frequent, low-novelty actions get less motion, not more.
3. Never animate keyboard-initiated actions. When a control takes both inputs, track which one fired, so arrow keys jump and clicks animate. A progress fill isn't decoration: a keyboard hold still fills. (from Subframe's motion library)
4. Transform and opacity only. Never `transition: all`. Never layout properties (width, height, top, left).
5. Transform-origin where the motion physically starts (a menu grows from its trigger).
6. Blur under 20px; no glow.
7. Every animation has a `prefers-reduced-motion` branch. It's a column in the spec table, not a fix. Decorative motion paints the final frame. Motion that does a job keeps the job and drops the travel: a hold still takes its full time and a countdown still counts, with progress in text and the bar or fill changing only at the end; a spinner holds still beside its status label. (from Subframe's motion library)
8. Loops pause when offscreen and on hover or focus-within; anything autoplaying over five seconds needs a pause control. A countdown the user may act on (an undo window) pauses its timer the same way, which counts as its pause control, then resumes from the time left. On touch, with no hover, the window runs at least eight seconds. (from Subframe's motion library)
9. Paired elements share easing and duration.
10. Interruptible: a second action mid-animation doesn't wait for the first. Work still pending follows the spec's repeat row, which may ignore the press.
11. Hover-opened surfaces (tooltips, previews) wait 80ms before opening, so a pass-through doesn't fire them.
12. Curves come from the tokens and the spring preset. Don't hand-write a bezier or a sine wobble for one element; tune amplitude, delay, and direction, never the curve. (from kelvinkn17 fun-isometric)
13. An illustrated loop (an icon, a sticker, a mascot) is the action, then a still hold about as long; the hold is the feel, so never fill it with idle wobble. Tickers and ambient fields stay continuous. A layered illustration pops in and out with scale, not opacity, since alpha shows the layers through each other. (from kelvinkn17 fun-isometric)
14. Screen readers get the landing, not the motion. Hide the moving digits with `aria-hidden` and keep the value, with its label, in visually hidden text from first paint. Make that text a polite live region only where the value changes after load, so a roll on entry stays silent and a change announces once, where it lands; announcing every frame or tick is noise. A countdown announces what's on offer and for how long when it starts, then once when it ends. (from Subframe's motion library)

## The ten-line reveal prompt

Fill this in per surface and hand it to the agent that writes the code:

```
Surface: <name>. One reveal on first paint; nothing else animates on load.
Order and timing (delay, duration, easing token):
1. <element> 0ms, --motion-base, --ease-out, opacity 0 to 1 and translateY(8px) to 0
2. <element> 60ms, ...
3. <element> 120ms, ...
Chart line: pathLength 0 to 1, 700ms, --ease-out, labels fade 150ms after the line lands.
Numbers: roll to value, 600ms, --ease-out, tabular figures, on entry and on change only.
Ticker: translateX(-50%) over 75s, linear, paused on hover and focus-within, mask-image edge fades.
Reduced motion: paint the final frame; ticker static and single set.
Forbidden: transition: all, layout properties, ease-in, bounce, anything on scroll.
```

## Flag on sight (from review-animations)

`transition: all`, `scale(0)` entrances, `ease-in`, anything over 300ms in UI, motion on hover for non-interactive elements, a missing reduced-motion branch, animated `height`, stacked fade-ups, a spinner where a skeleton belongs. Also the component-library effects that read as a generated page: meteors, border beam, shine border, spotlight card, cursor follower, retro grid, globe, orbiting circles, sparkles text, typing animation, word rotate, scroll word reveal.

## Budget

- One load sequence under one second total.
- Idle CPU under five percent on a mid-range phone with the backdrop, the ticker, and one chart draw.
- No layout shift from motion; check INP and a throttled Lighthouse run.
- The LCP element (the headline or hero product on a front door) never starts below opacity 0.1 and never moves. Chrome doesn't count an opacity-0 paint, so a fade from zero pushes LCP to the end of the animation.
- Backdrop shaders: cap device pixel ratio at 1.5, pause offscreen with IntersectionObserver, two or three noise octaves at most on mobile.

When a motion drops frames, name the cause before changing code, and confirm on a mid-range phone recording, not a laptop (from emilkowalski animation-performance):

| Symptom | Cause and fix |
|---|---|
| Stutters | Layout property; animate `transform` or `opacity` |
| Choppy shadow | `box-shadow` repaints every frame; animate `filter: drop-shadow()` |
| Janks only during navigation or loading | Main thread busy; move it to CSS or WAAPI |
| Motion `x`/`y`/`scale` drops frames | Before `motion` 14.2 they run on the main thread; upgrade or use the full `transform` string. `layout` and `layoutId` stay on the main thread in every version |
| Hand-rolled animation drops frames in React | `setState` per frame; write `ref.current.style` or a motion value |
| Gets laggier as content grows (a drag, a long list) | A CSS variable set on a parent recalculates every descendant each frame, even though only `transform` reads it; set `transform` on the element itself |
| Blur lags, Safari worst | Animated `blur()` over 20px; 2 to 5px softens a crossfade |
| Shifts 1px as it starts or ends | GPU handoff; `will-change: transform` on that element, only once you've seen it |

## Cutting built motion

A cut motion that's already in code takes its dependents with it (from emilkowalski remove-animations):

- Delete the start state with the animation: an `opacity: 0` keyframe start, `initial={{ opacity: 0 }}`, or a reveal class waiting on an observer leaves the element invisible forever.
- Delete what waits for it: `transitionend` and `onAnimationEnd` listeners, timeouts sized to a duration, focus moved in a callback.
- Move `onExitComplete` work to where the component closes; without the exit, `AnimatePresence` unmounts at once.
- Check a removed `layout` prop or FLIP wasn't masking a layout jump. If the jump appears, keep the animation and log the shift.

## Front doors, loops, and repeats

- A front door may play once and hold: one draw on first paint within the one-second load budget, never again in the session, never redrawn by the next step. Typing snaps it to the final frame.
- An ambient loop (a ticker) starts with the page. A loop that starts late reads as something loading late.
- "Nothing moves under the cursor" is scoped to what's under or behind the cursor. A ticker at the bottom keeps moving while the user types; no product pauses a marquee on input.
- A data draw on a time axis is linear, every period the same time, and the same tempo whether the result is good or bad.
- An action that costs the user something never fires from browsing. Picking a value fills it in; the explicit button runs.
- A repeat of a signature moment is a different, shorter shape (about 1s), and a third within 10s is a cross-fade. Interruptible: once the result is in, a new run snaps the one in flight to its end; while the work is pending, the spec's repeat row decides.
- Numbers in one summary change together, in one beat, and the page never shows two different sample sizes for one result at once.


# UI motion recipes

Vendored from [emilkowalski/skills `animate/RECIPES.md`](https://github.com/emilkowalski/skills/blob/main/skills/animate/RECIPES.md) (MIT, Emil Kowalski) at commit f1090be. Verbatim below the rule except em dashes, swapped for house punctuation. `recipes.md` covers data motion; this covers the UI components around it. Start from the recipe and adapt rather than rebuilding.

- **Tokens.** The recipes name `--ease-out`, `--ease-in-out`, and `--ease-drawer`. Use the product's tokens where they exist (`rulebook.md` Tokens). For a product with none, upstream's values: `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`, `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)`, `--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1)` (iOS-like, from Ionic).
- **The rulebook wins where they meet.** The drawer (500ms) and toast (400ms) run past the 300ms cap, the accordion animates `height`, and the scroll reveal is motion on scroll. Cap them at the rulebook's values by default; keep the recipe's value only with a reason, named as an exception in the spec row, and scroll reveal stays off a data product.
- **Hold to confirm needs more than `:active`.** The CSS is the fill. A shipped hold drives that fill from a small state machine (idle, holding, releasing, committed), because `:active` can't cover the rest: Space or Enter holds, ignoring key repeat, and keyup releases; Escape resets; moving more than 10px, pointer cancel, window blur, and a hidden tab all release; the fill drains from where it reached at about 2.5x its fill speed, which replaces the recipe's fixed 200ms. Fill and drain are both linear, since they're progress. Under reduced motion the hold keeps its full time, text reports progress, and the fill changes only at completion. Offer another way to confirm for anyone who can't sustain a press. This is the exception to "the rulebook wins": `clip-path`, `linear`, and a fill or drain past 300ms are right for progress, so name them in the spec row rather than capping them. `clip-path` in the tab indicator recipe is the same kind of exception. (from interior.dev)

Contents: [Button press](#button-press), [Dropdown, popover, menu, select](#dropdown-popover-menu-select), [Tooltip](#tooltip), [Modal](#modal), [Drawer / sheet](#drawer--sheet), [Toast](#toast), [Accordion / collapse](#accordion--collapse), [Stagger a group entrance](#stagger-a-group-entrance), [Hold to confirm](#hold-to-confirm), [Tab indicator with a color transition](#tab-indicator-with-a-color-transition), [Scroll reveal](#scroll-reveal), [Gestures](#gestures), [Masking a crossfade that won't settle](#masking-a-crossfade-that-wont-settle), [Programmatic, without a library](#programmatic-without-a-library)

---

## Button press

Any pressable element. Instant feedback that the interface heard the user.

```css
.button {
  transition: transform 160ms var(--ease-out);
}

.button:active {
  transform: scale(0.97);
}
```

`scale()` scales children too: the label and icons come along, which is what makes it read as a physical press.

No hover gating needed here: `:active` is a real press on touch. Gate any `:hover` styling separately.

---

## Dropdown, popover, menu, select

Scales out of its trigger, not out of thin air.

```css
.popover {
  transform-origin: var(--transform-origin); /* Base UI supplies this */
  transition:
    opacity 200ms var(--ease-out),
    transform 200ms var(--ease-out);
}

.popover[data-starting-style],
.popover[data-ending-style] {
  opacity: 0;
  transform: scale(0.95);
}
```

The `transform-origin` is the whole point: the panel should look like it came out of the thing you clicked.

---

## Tooltip

Same shape as a popover, faster, plus the detail most implementations miss.

```css
.tooltip {
  transform-origin: var(--transform-origin);
  transition:
    transform 125ms var(--ease-out),
    opacity 125ms var(--ease-out);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* Once one tooltip is open, neighbors open instantly */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

The initial delay prevents accidental activation. After that, skipping both the delay and the animation makes the whole toolbar feel faster.

---

## Modal

The one popover that stays centered.

```css
.modal {
  transform-origin: center; /* exempt: not anchored to a trigger */
  transition:
    opacity 250ms var(--ease-out),
    transform 250ms var(--ease-out);
}

.modal[data-starting-style],
.modal[data-ending-style] {
  opacity: 0;
  transform: scale(0.96);
}

.backdrop {
  transition: opacity 250ms var(--ease-out);
}
```

Animate the backdrop's opacity alongside it so they read as one surface.

---

## Drawer / sheet

```css
.drawer {
  transform: translateY(0);
  transition: transform 500ms var(--ease-drawer);
}

.drawer[data-closed] {
  transform: translateY(100%);
}
```

This is how Vaul hides a drawer before animating it in.

Add drag and it becomes a gesture problem; see **Gestures** below.

---

## Toast

```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity 400ms ease,
    transform 400ms ease;

  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
}
```

- `ease` rather than `ease-out`, slightly slower than typical UI: Sonner reads as elegant partly because its motion is tuned to the component's personality rather than to the generic UI budget.
- If `@starting-style` isn't available, fall back to the mount flag:

```jsx
useEffect(() => { setMounted(true); }, []);
// <div data-mounted={mounted}>
```

When toasts stack and the list reflows, the opacity change has to work against the height change. There's no formula for that pair; adjust until it feels right, then check it again the next day.

---

## Accordion / collapse

```css
.content {
  overflow: hidden;
  transition:
    height 200ms var(--ease-out),
    opacity 200ms var(--ease-out);
}
```

Keep it short: this is one of the few animations that costs layout on every frame, so a long duration is expensive as well as sluggish. Measure the content height in JS (or use a headless primitive that supplies it) rather than animating to `auto`.

---

## Stagger a group entrance

For a list or grid the user sees occasionally, not for a list they scroll past all day.

```css
.item {
  opacity: 0;
  transform: translateY(8px);
  animation: fadeIn 300ms var(--ease-out) forwards;
}

.item:nth-child(2) { animation-delay: 50ms; }
.item:nth-child(3) { animation-delay: 100ms; }
.item:nth-child(4) { animation-delay: 150ms; }

@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

Stagger is decorative: it must never block interaction while it plays.

---

## Hold to confirm

For destructive actions where a plain click is too easy to fire by accident.

```css
.overlay {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms var(--ease-out); /* release: snappy */
}

.button:active .overlay {
  clip-path: inset(0 0 0 0);
  transition: clip-path 2s linear;             /* press: slow and deliberate */
}

.button:active {
  transform: scale(0.97);
}
```

`linear` is correct here: the fill is a progress indicator, and progress shouldn't ease.

---

## Tab indicator with a color transition

Timing individual color transitions across a tab list never quite lands. Clip instead.

Duplicate the tab list. Style the copy as the active state: different background, different text color. Clip the copy so only the active tab shows, and animate the clip on change:

```css
.tabs-active-copy {
  clip-path: inset(0 60% 0 20%); /* driven by the active tab's position */
  transition: clip-path 250ms var(--ease-in-out);
}
```

The text and background change together, in perfect sync, because they're one element being revealed rather than two colors being interpolated.

---

## Scroll reveal

Marketing surfaces only. Don't do this to functional UI a user visits daily.

```css
.reveal {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 600ms var(--ease-in-out);
}

.reveal[data-visible] {
  clip-path: inset(0 0 0 0);
}
```

Trigger with `IntersectionObserver`, or Motion's `useInView` with `{ once: true, margin: "-100px" }`. Fire it once: re-animating on every scroll-by is an interface fighting its reader.

---

## Gestures

Drag, swipe, fling, and sheet interactions. Springs, not durations, because the user can reverse mid-motion.

The rules the code below doesn't spell out, from Emil Kowalski's [`gestures`](https://github.com/emilkowalski/skills/tree/main/skills/gestures) skill (MIT):

- **Library first.** A drawer or bottom sheet is Vaul. Hand-roll only what no library covers (swipe cards, a custom drag).
- **Two phases.** While the pointer is down, position maps 1:1 to it: a motion value or a direct `transform` write, with no spring, no easing, and no React state per move. After release, a spring seeded with the release velocity finishes the motion, never a keyframe.
- **Linked values come from the drag.** An overlay's opacity or the page's scale is derived from drag position (Motion's `useTransform`), not animated on its own, so it stays in step when the user reverses.
- **Bounce only after a drag.** A released drag gets a little; the same element closed by a button gets none. Snap-back under the threshold is fast.
- **Dismiss along the entry axis.** A toast that slides up dismisses with a swipe down.
- **A floating drawer** (not touching a screen edge) runs about 200ms. The 500ms drawer curve reads right only on a full-width sheet attached to an edge.
- **Reduced motion keeps the tracking**, since the user makes that motion, and drops fling, bounce, and momentum: release settles with a short fade or position change.
- **`touch-action`** for the drag axis, so native scroll doesn't fight the gesture. Test on a phone over the local IP; a trackpad lies about touch.

```js
// Dismiss on a flick, not just on distance
const timeTaken = Date.now() - dragStartTime.current;
const velocity = Math.abs(swipeAmount) / timeTaken;

if (Math.abs(swipeAmount) >= SWIPE_THRESHOLD || velocity > 0.11) {
  dismiss();
}
```

```js
// Set transform on the dragged element directly.
// Driving it through a CSS variable on the parent recalcs styles for every child.
element.style.transform = `translateY(${distance}px)`;
```

Four details that separate a good drag from a bad one:

- **Pointer capture** once the drag starts, so it continues when the pointer leaves the element's bounds.
- **Multi-touch protection**: `if (isDragging) return` on new touch points, or switching fingers mid-drag makes the element jump.
- **Damping past boundaries**: dragging beyond a natural edge moves the element less the further it goes. Real things slow before they stop.
- **Friction, not a wall**: allow the over-drag with rising resistance rather than refusing it.

Settle with a spring so an interrupted drag keeps its velocity:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }
```

---

## Masking a crossfade that won't settle

When two states overlap visibly during a transition and no amount of easing or duration tuning fixes it, blur the seam:

```css
.content {
  transition:
    filter 200ms ease,
    opacity 200ms ease;
}

.content.transitioning {
  filter: blur(2px);
  opacity: 0.7;
}
```

Without blur the eye reads two distinct objects swapping. Blur blends them into one perceived transformation. Keep it under 20px; heavy blur is expensive, especially in Safari.

---

## Programmatic, without a library

When the motion needs JS control but not a dependency, WAAPI gives you CSS-grade performance:

```js
element.animate(
  [{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
  { duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)' }
);
```

Hardware-accelerated, interruptible, no bundle cost.

## Gliding nav pill
- One pill behind the links, a soft hover tint (the product's hover overlay, about 6%), never an opaque block. Siblings keep their rest ink; nothing dims.
- Move it with `clip-path: inset()` on a fixed-width layer, not `width`. Drive each edge with a critically damped spring so it stretches on a cross, carries speed on a reversal, and never passes its target word.
- Grow from the hovered word's width on enter; leave in about 200. Hold the last anchor (`data-last`) so leaving the nav doesn't collapse it to zero.
- A weight step on hover needs the hidden bold copy to reserve width, or the row shifts.
- References: Cal.com (glide), Attio (fast in, slow out), Stripe (sibling dim, which reads as disabled on dark; avoid).

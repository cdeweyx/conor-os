# Interface floor

What the UI sweep holds every surface to, and how the polish pass picks a fix. From jakubkrehel/skills `better-interface` (MIT).

## The floor

Evidence, not taste. A density, radius, or voice you merely disagree with isn't a finding, and DESIGN.md settles those. These are failures whatever the style guide says, and they count on a minor surface too. One is a close issue, never a papercut.

- A control with no accessible name.
- A keyboard-reachable control with no visible focus.
- A path a pointer can take and a keyboard can't.
- Motion or autoplay that ignores `prefers-reduced-motion`.
- Content or a control clipped, overlapped, or unreachable at 320px or 200% zoom.
- Content that moves once drawn: a load, a late notice, or a skeleton that pushes what's on screen, measured in page coordinates over the load.
- Body or control text failing its contrast ratio, measured on the rendered pair.
- State or meaning carried by color alone.
- A state change carried by motion alone, with nothing left behind when the animation doesn't run.
- A destructive action with no confirmation, undo, or distinct treatment.
- Truncated content with no way to reach the full value.
- Content or a control past a scroll edge or behind a disclosure with no visible cue.
- An error that names no way to recover.
- A semantic color used against its meaning, like the danger hue on a harmless action.

Every finding cites `file:line` and shows what's there. A rendering claim needs the rendered state, and a check that couldn't run is `Not verified`, never a pass.

## Cheapest fix first

When more than one fix would work, take the earliest that does:

1. **Delete.** A separator that space would carry, an animation on a high-frequency interaction, an ARIA attribute a native element makes redundant.
2. **Use the platform.** The native element or the browser's own focus ring, instead of a custom rebuild.
3. **Reuse what the project has.** An existing token, spacing step, or component, before any new value.
4. **Correct the value.** The wrong easing, radius, gap, or contrast pair.
5. **Add.** A new token, wrapper, media query, or attribute, only when nothing above works.

When the code under review adds what step 1 would fix, that's a finding, and the fix is the deletion.

## One root cause, one finding

Report a shared token or component once, with every location in the same row. It outranks the same symptom in one leaf, because one fix buys more.

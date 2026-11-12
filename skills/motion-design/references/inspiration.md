# Inspiration: where to look for motion and how to read a reference

Motion references are read for what stays still as much as what moves. Gather ten, annotate the choreography, extract three principles, commit to one reveal.

## Sources

The motion galleries, craft writing, and the people worth studying live in the design-sources skill, under Motion and interaction and Craft writing. Start with 60fps.design for choreography, uilabs.dev and interior.dev for product-register feedback, and emilkowal.ski and Rauno's interfaces for the rules.

## Lane plan for a specific motion

For a line draw-in, a ticker, a number roll, or an ambient drift, two lanes previewed and confirmed:

- Technique: the property, the library with the least code, the duration and easing practitioners converge on, the performance trap, the reduced-motion outcome. Ask for numbers, not moods.
- References: three to five products doing this exact motion well. Record a three-second clip or fetch the frame sequence. Include one anti-reference (stagger spam, a bouncing hero) to name what's out.

Capture with Playwright `recordVideo` or a screen recording; tile with `scripts/contact_sheet.sh` so one look covers each clip's timeline.

## Annotate each clip

```
ref: M-02   source:   captured: 3s clip, contact sheet   lane:
what moves:            what stays still:
trigger: load / scroll / hover / idle loop / user action
duration per element:  total reveal:
easing shape: named curve or spring (duration, bounce)
choreography: what moves first, overlap, follow-through, the moment it stops
budget: share of the screen moving at once; pauses off-screen?
why it works: one sentence, the principle
take:                  leave:
```

Synthesis: three principles with the clip that proves each, one reveal for the surface, and the timing and shape per motion that feed the spec table.

## Method notes

- Emil's judgment drill: two versions of the same animation side by side, pick one, write the reason, then read the breakdown. Run it on the keyframe strip before asking the user to.
- Rauno skips wireframes for motion and goes to code with a concrete visual in mind, sharing tiny clips for feedback. The HTML prototype is that clip.
- Vercel's polish definition: no dropped frames, no cross-browser inconsistency, accessible. Some animations are unnecessary because they aren't the focus.
- Josh Comeau: novelty is the ingredient of whimsy, so ration it; natural variation over robotic repetition; springs slow to a stop the way CSS curves can't.
- Linear: structure should be felt, not seen. If most people don't notice what changed, that's a good sign.

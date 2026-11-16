# Motion budget for a landing page

Measured with `document.getAnimations()` across a full scroll of the tier's homepages (October 2026): Vercel runs nothing at load and one 200ms fade over the whole page; Linear one hero reveal, one ambient loop, and 11 reveals over 10,000px; Resend 3 over 12,300px. None splits a headline by word or character, uses parallax or pinned storytelling, or ships GSAP, Lenis, Lottie, or Rive. Restraint is the tier marker. Conor's named favorites (roma.app, generalintelligencecompany.com) run a slower register, with blur clearing on entry and a tuned reveal per block, and both registers are allowed. motion-design owns the tokens, the spec, and the review loop; this is the page-level budget it designs inside. The hero reveal and the in-view reveals are front-door exceptions to the rulebook's 300ms UI cap, since they play once and answer no action; hovers, presses, and other feedback keep the rulebook's numbers.

## Budget

- One hero reveal in element order (headline, subhead, CTA, product, background last), in one of two registers. Quick, the tier's: under 1s total, delays 0, 80, 160, 240ms, 500 to 700ms each, 12 to 20px of rise or opacity only. Slow, the favorites': about 2s total, the headline 1000 to 1300ms clearing a 6 to 12px blur, supporting lines rising 6px with no blur, the product last at about +600ms, a long ease-out such as `cubic-bezier(.22,.65,.25,1)`. Blur goes on the headline only. When the headline is the LCP element, it clears blur and fades in place, with no rise (the next line).
- The LCP element (usually the headline or the hero product) never starts below opacity 0.1 and never moves. Chrome doesn't count an opacity-0 paint, so a fade from zero pushes LCP to the end of the animation.
- Below the hero, either still with at most one in-view reveal per screen (400 to 500ms, once, 12 to 16px), or one tuned reveal reused on each section as it enters (roma.app: 800ms, a 6px blur clearing with a 14px rise, `cubic-bezier(.22,.61,.36,1)`, once). Tuned means a blur clearing with the rise, 700 to 900ms, on a long ease-out; a stock fade-up (opacity and rise at a library's defaults) isn't. Build it as one `@keyframes` animation per section, since the gate counts a transition once per property. Either register of hero pairs with either choice below it, but below the hero it's one recipe, never a mix, and every revealed block is visible with JavaScript off and under reduced motion (roma fails both). `check.mjs` warns past 40 animations per 10,000px.
- Text animates by line, 30 to 80ms apart. Word-by-word reveals (on load or on scroll), character splits, typewriters, and word rotators are off, except as the page's one named signature moment.
- Numbers roll rather than count: digit columns translate, 300 to 600ms, 50ms per digit, tabular figures (Stripe uses 325ms with `cubic-bezier(.33,1,.68,1)`; NumberFlow does it).
- Logos sit in a static row. A marquee only when there's more than one row of them: 150s or slower, linear, paused on hover, static under reduced motion.
- One ambient layer at most (a shader, canvas, or video), loaded after LCP, device pixel ratio capped at 1.5, paused offscreen, skipped on weak hardware.
- Tabs or a carousel that advance on a timer: assume nobody sees past the first panel, so the lead claim sits there. The timer starts when the set is in view, pauses on hover and focus, and stops under reduced motion.
- A product demo prefers a live component, then a self-running sequence that plays when in view, then video. A scrubbed or pinned scroll section needs a named reason and stays under three viewports.
- A self-running sequence over about 3s plays once per visitor (a `localStorage` flag), then shows its poster frame on return visits. (Interfere's timeline hero.)

## Mechanics

- Easings found in the tier's bundles: easeOutCubic `cubic-bezier(.33,1,.68,1)` as the base, easeOutExpo `cubic-bezier(.16,1,.3,1)` for the one large move.
- Scroll-linked effects use CSS `animation-timeline: view()` or `scroll()` inside `@supports` with a static fallback (cross-browser since Firefox 159, October 2026, about 88% global), Motion's `useScroll` or `whileInView` as the fallback. Never a raw scroll listener.
- Reduced motion: transforms go to zero, blur clears at once, opacity fades stay, loops pause with `animation-play-state: paused`, video shows its poster. Raycast and Clerk ignore it and Linear keeps 75 infinite animations running under it, so getting it right is an easy place to beat them.

## Blocklist

The component-library effects that read as a generated page, by name: meteors, border beam, shine border, spotlight card, cursor follower, retro grid, globe, orbiting circles, sparkles text, aurora text, typing animation, word rotate, scroll word reveal (a word reveal or typewriter written as the page's one named signature moment, per the budget above, is the exception). Magic UI and React Bits are where they come from; motion-primitives (In View, Text Effect per line, Sliding Number) is the library that reads at the tier's level.

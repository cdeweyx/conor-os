# Inspiration: where to look and how to turn a reference into technique

The front of the loop. Gather ten, extract three principles, commit to one move that's ours. Stealing the thinking behind a reference is the method; stealing the pixels is the failure.

## Sources

The galleries, by job, live in the design-sources skill. For a decorative visual start with recent.design, Sections.wtf, and Mobbin `search_sections`; add Dark Mode Design for a dark-first product and 404s for an empty or error state.

Sport and editorial: the Masters app (data depth, the course map), The Athletic (Metalab and STRV case studies show the reasoning), ESPN (a documented blueprint with exact values). FiveThirtyEight's archive is gone; use the Wayback Machine and the data repo.

## Lane plan for a specific visual

Post the lanes, get a go, then run them in parallel. For an abstract backdrop on a data product's home screen:

- A, technique canon: the essays and notebooks for this visual type (Hobbs on flow fields, Observable field notebooks, Codrops line and particle demos). Queries name the technique, not the feeling.
- B, shipped backdrops: recent.design, Siteinspire, Land-book, Lapa, Awwwards websites; Dark Mode Design when the product is dark-first; 404s for an empty or error state. Screenshot the hero at 1440x900 and 390x844.
- C, data-product peers: Linear, Vercel, Stripe, Raycast, Ramp, Mercury by URL; Refero style search; SaaSFrame dashboards.
- D, adjacent editorial and the domain's own tradition: its maps, scorecards, tickets; the data-viz galleries.
- E, anti-references: two Dribbble shots and one gradient-mesh template, to name what we won't do.

Capture with Playwright in one pass: still per viewport, a three-second clip for anything that moves, stored as `refs/<lane>/<slug>.png` with a `refs.json` of URL, viewport, timestamp. Cull thirty to sixty down to twelve to eighteen, crop each to the part that matters, tile into one contact sheet with a one-line caption each, grouped by lane. Open only the images that change a decision.

## Annotate each reference by technique

Writing the annotation is the analysis. One block per reference:

```
ref: B-03   source:   captured: 1440 still | 390 still | 3s clip   lane:
one line: what it is, in twelve words
job it does: sells / orients / rewards / fills silence
composition: where the mass sits, the anchor, the reading path
palette: N colors incl. neutrals; the accent's role
weights: stroke min and max; how many tiers
density: where it's dense, where it thins, where text sits
negative space: share of the frame that rests
texture and depth: grain, blur, none; how layers separate
type relation: how the visual yields to copy
motion, if any: trigger, duration, easing, what stays still
why it works: one sentence, the principle not the pixels
take: the transferable principle     leave: the part that's theirs
```

Then the synthesis: three principles, each with the reference that proves it, and one move. The brief gets the principles, the move, the hard constraints (palette count, weight tiers, density, negative space), the anti-references, and the technique stack chosen. Raw sheets and annotations go to the project's research page.

## Method notes from practitioners

- Kleon: imitate, then emulate. Emil: surround yourself with the best work, think hard about why you like it, get critiqued; "almost every taste decision has a logical reason," so write the reasons as rules.
- Dan Mall's visual inventory: pair each reference with a question ("could a monochrome approach work here?") and get answers in a day. Brad Frost's gut test: twenty sites, twenty seconds each, score, discuss the outliers.
- Style tiles before layout: extract color, type, texture into a tile first.
- Linear's maxims: don't compete for attention you haven't earned; structure should be felt, not seen.
- Vercel Ship: a ferrofluid reference, fifteen thousand generated images, an accessibility pivot, then a metallic liquid system. A real reference-to-technique arc, and a reminder that the research lane can change the answer.
- The Pudding: keep a running doc of screenshots, what worked, and the link; mock statically before code.

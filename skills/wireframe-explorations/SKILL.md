---
name: wireframe-explorations
description: >
  Builds three to five lo-fi HTML wireframe options for a product surface
  that differ in approach rather than styling, with real data and a contact
  sheet to compare them. Use when a product doc and user journey exist and
  the user says "explore approaches", "wireframes", "lo-fi options",
  "contact sheet", "show me three ways this could work", or at
  design-shaping's explorations step. Do NOT use for hi-fi or styled mockups
  (hifi-design), polishing a built UI (better-ui), or charts on their own
  (dataviz).
---

# Wireframe explorations

Gray boxes that argue. The point of an exploration is to make a real alternative visible before anyone picks, because the biggest design risk with an agent is that the first plausible layout gets locked in. Every option in a set changes an assumption, not a layout, and every option is deliberately unfinished so feedback lands on structure instead of fonts.

Read `references/constraints.md` every run, before building. It holds the deny list and the requirements. `references/wireframe.css` is the shared stylesheet; link it, don't restyle.

## Before drawing

Settle what matters before naming options. When the options would differ in what matters (which metric leads, which fact is on the card face), settle that ranking with the user first, from the research, and then explore how to present it. Priority is a decision; presentation is what exploration is for. Settle weight too, not just order: for each number, the job it does for the user (trust, act, or leave) and its size tier. A card is one hero, one supporting line, one action; the rest goes to the detail view. An ordered list at one size still reads as noise, and a round drawn on an unweighted set gets redrawn.

Then the brief, before any drawing, because a list of variant names isn't enough to approve. Post it and wait for a yes. Per surface:

- The job. One sentence on what the user is trying to do here, from the user journey.
- Why it's worth exploring instead of defaulting. What's contested, what the research said, what the incumbents get wrong.
- Each option: a two-word name, one concrete sentence on what it is (structural here, since lo-fi has no look: "a ledger of rows, the record first, one row per invoice", never "unique" or "clean"), the assumption it changes, and what it would prove or disprove. One option is the incumbent pattern done right, so the creative ones have a baseline to beat; when Interface Lineage has the pattern, the option names its slug (found in `https://interfacelineage.com/llms.txt`, read with `curl -s https://interfacelineage.com/<slug>.md`), so the baseline is a mechanism with known limits, not a layout.

Options differ in approach when they change one of: what the user starts from, the atomic unit (card, row, message, page), whether this is the right place for the thing at all, the reading order, or an assumption the product doc takes for granted. Five layouts of the same idea is one option.

## Rounds

Round 1 is approaches: three to five per surface. A surface design-shaping didn't name as a crux stops after round 1. Round 2 is one direction per surface with the contested detail varied (the headline visual, the arrangement, the default view), and the question is "what would change your mind," not "what else could we try." A round 3 is a single surface if one is still open. Each round gets its own brief and its own yes.

## Content before layout

Inventory the content before placing anything, tagging each item fixed or variable in length: the primary content, the actions (one primary, the rest secondary), the navigation, the chrome, the empty, thin, and error states, and which action is disabled in each and why. Layout follows the inventory; wireframes that skip this step are structurally hollow.

Every string on screen names real information from the product: real object names, real records, real sample sizes, real prices, real date ranges. No lorem ipsum, no "Image" boxes, no invented numbers, no filler labels that remove nothing when deleted. If a number isn't known yet, print a labeled placeholder ("metric to confirm"). The content is the design; fake content hides the layout problems that matter. Where the product has rules for deriving a number (a total from its line items, a percentage from its counts), derive the illustrative values from those rules so the options agree with each other and with the doc.

Build a small generator, not hand-written files: one script with a shared data module and component functions (stats block, table, card, states). Every option and every round reads the same data, so a change to a number or a label propagates, and round 2 reuses round 1's parts.

Declare the surface's mode: Operate (the user completes a task; scanability and consistency win) or Read (the user absorbs a result; hierarchy and reading order win). Expression loses to both.

Every screen supports two reading speeds. The executive path is the title, the decisive numbers, and the one sentence that states the decision this screen supports. The audit path is the tables, the assumptions, and the caveats. Label each number by kind when it matters: observation, derivation, or projection.

## Building

Gray and hairline on purpose: the constraints file lists what's allowed. Size, weight, gray value, and position are the only tools, which is the point. Polish invites polish feedback, and reviewers assume a finished-looking thing means the thinking is finished.

Start with the feature, not the shell. Draw the one screen that does the job, and let the navigation chrome emerge only if the surfaces need it.

Tables are the primary data surface. Numbers right-aligned in tabular figures, headers aligned like their columns, one hairline between rows, no verticals, no stripes. Under about twenty numbers, a table beats a chart.

Every number sits next to its comparison: baseline, break-even, prior period. A stat with no comparison is decoration.

Section height follows content. Dense where the data is, air around the one decision. If every block is the same height, the layout is wrong.

Each option renders its states further down the same page: empty, thin data, and any error the journey named. A thin-data state is its own state, not an empty one.

Number the elements worth discussing with small markers and tie them to notes at the bottom of the option. Mark unknowns explicitly ("copy to decide", "modal or page, open").

Before coding each option, write a four-line plan (surfaces, primary table, the one highlighted thing, states), then ask "would I produce this for any similar prompt?" and change what fails. After building, run the scanner in the constraints file over the HTML; it catches most of the slop catalog before anyone looks.

## Output

- One HTML file per option in the project's mockups folder, dated, named by surface and option: `YYYY-MM-DD-checkout-summary-first.html`. All link the shared stylesheet.
- Two Playwright screenshots per option: the viewport for thumbnails and the full page for click-through. Contact sheets built from full-page shots are unreadable.
- One contact sheet per surface: an HTML page lining the options up side by side with the two-word name and the assumption under each, exported to a PNG under 5 MB so the doc tool renders it inline.
- A review page: one HTML file with a section per surface, thumbnails that open the real wireframe in a new tab, and a compare toggle that puts two options side by side in iframes. Open it in the user's browser for them.
- After the round closes: the sheets go into the product doc in a design explorations toggle, the converged direction per surface in its own toggle, and what was tried and why it lost in a scratch toggle. One push per round, after review.

Bring the sheets to the user with a one-line pitch per option and no recommendation. A first reaction shaped by yours is the anchoring the step exists to avoid. Let them react in their own words; sort the reactions into keep, change, and kill, and name the goal each serves. Give your own pick only when asked, after their first read, and defend it.

## Things that go wrong

- Styled output on round one. Any color, shadow, radius, icon, or second typeface means the constraints weren't read.
- A landing-page skeleton for a tool. Hero, three boxes, call to action, even in gray. Open on the data.
- Correcting the same default three times. Clear and rewrite the prompt with the constraint named.

## Skill pause

Run authoring-skills' Closing a skill update (the skill pause) at the end of every run. What goes where in this skill: a process rule into the body, a deny or a requirement into `references/constraints.md`.

## Checklist

- Order and weight (job and size tier per number) settled before the options were named.
- Brief posted per surface and approved before anything was drawn, for every round; every option carried its one concrete sentence and its assumption.
- Options generated from one script and one data module.
- One option per surface is the incumbent done right, with its Interface Lineage slug when one exists.
- Every string is real product content or a labeled placeholder.
- Every number has its comparison beside it; tables use tabular figures and right-aligned numbers.
- States rendered on every option.
- Scanner run clean on every file.
- Contact sheet per surface under 5 MB, review page opens, sheets in the product doc.
- Presented without a recommendation; the pick offered only when asked.
- Converged direction and the losers written to the doc after the user's yes, and handed to the hi-fi brief unchanged: the metric hierarchy, the reading order, the final copy, the losers with why they lost.

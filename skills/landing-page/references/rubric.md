# Rubric, tells, and evidence

What the critics score, the collision test before the build, the tells the gate scans for, and which conversion claims have evidence behind them. The rubric and caps draw on taste-skill's critique method (github.com/Leonxlnx/taste-skill, MIT) and its 247-site study; the clusters and the collision test are Anthropic's frontend-design skill (github.com/anthropics/skills).

## Rubric

Each axis 0 to 10, weighted, screenshot only.

- **Strategy, 20%.** Five-second test: what it is, who it's for, what to do next. The idea fails for the competitor. One primary action, with a real button on the first screen. One live thing: the first screen's product is also operable (set a value and read the real result, pick an option and see it applied), made from the idea, works with a thumb, has a plain fallback without script, never blocks reading. In taste-skill's blind tests every winning page had one and the jurors named it first.
- **Copy, 20%.** Headline literal and two lines or fewer at 1440 and 390. Every section a claim with its proof beside it, and for each proof, can you point at it (the number, the screen, the named quote), not just a sentence saying it's so? Plain reading level. No banned phrases, no invented proof, no orphan words. Written to the buyer about their problem, never to investors about the company: a "who we serve" band of segments or a picker that makes the visitor classify themselves before they learn what it does is pitch-deck copy. Proof comes from people who look like the buyer; two investor quotes on a product for anyone reads as "for VCs".
- **Visual, 30%.** Squint and the screen resolves into two or three masses. Headline at least three times body size. Two or three text edges per screen. No two adjacent sections share a layout. Every desktop screen reads as a composed poster. Holes vs rests: every large void is a rest only if something closes it (the picture, type big enough to span it, a step in ground tone); otherwise it's a hole. Holes come from text in one half with nothing in the other, unequal outer margins, a gap between sections over about 40% of a screen, a short block stretched to a full screen, or a reveal that hasn't fired. No stretch over half a screen holds nothing. The fix is a bigger main element or less space, almost never more stuff. The product is visible, as live interface or a real crop.
- **Motion, 10%.** One signature move, named. One tuned reveal reused per block is fine (`motion.md`); a stock fade-up on every section isn't. Reduced motion keeps all content. Nothing hidden by a reveal that didn't fire.
- **Polish, 20%.** Clean at 1440, 768, and 390; the phone layout is its own composition, not a squeezed desktop. Hover, focus, and press states; contrast proven on the tokens; nothing colliding; ship list complete.

Caps override the arithmetic:
- Fails the five-second test, or the idea works for the competitor: overall 6.5 at most.
- A three-line headline, placeholder content, gray-bar fake UI (bars where the eye lands; filler at the edges is fine, see `product-ui.md`), or any `check.mjs` FAIL: overall 6 at most.
- No live thing on the first screen: strategy 7.5 at most.
- Two or more holes or near-empty screens: visual 6.5 at most.
- Three or more tells from the list below: visual 6 at most.

## Critic prompt shape

Each critic gets the page's screenshots at three widths and two gold pages at the same widths, the user's named favorites first, then the reference pass's tier-one pages, never the anti-reference, logos and product names cropped, shuffled and unlabeled with neutral file names, and nothing else. A `worker` prepares the set (Model: worker role). It answers in this order: what it saw in one second; which of the three pages it thinks is generated and why; the idea in one sentence if it can find one; the layout of each screen in a word or two; the five scores with the caps applied, for each page; the pages ranked best to worst, no ties; the top three fixes for each page, each pointing at its screenshot. Prefer removing to adding. Leave the user's settled calls out of the prompt, since they point at ours; a fix that contradicts one is softened or dropped and logged.

Read each round by rank and gap: ours' rank is the median of the three ranks, the gap is ours' median overall minus the best gold page's. Scores drift between rounds even on unchanged pages, so compare gap to gap, never score to score. Use only the fixes for ours.

## Collision test

A gate between the direction step and the first line of markup. Write the token plan (four to six named hex values, the faces and their jobs, the layout in a sentence and an ASCII sketch, the one place boldness goes), then work through a similar prompt for another product in the same category. Every part of the plan you'd also arrive at there is a default, not a choice: revise it and say what changed and why. Check the plan against the five clusters below in the same pass. Where DESIGN.md or the user pins one of these looks, follow it; the test only governs axes left free.

## Tells

The five AI-look clusters, each counted as one tell (frontend-design's calibration list, verified November 2026):
1. **Cream and terracotta.** A warm cream ground (near `#F4F1EA`), a high-contrast serif display, a terracotta or clay accent (near `#D97757`, Claude's own accent, so on anyone else's page it reads as a tell).
2. **Near-black and acid.** A near-black ground with one bright acid-green or vermilion accent.
3. **Broadsheet.** Hairline rules, zero radius, dense newspaper columns.
4. **The SaaS-card kit.** Content chopped into identical rounded cards, one radius on everything, the same soft gray shadow under each, gradient washes as decoration.
5. **Template chrome.** A tracked all-caps eyebrow above every heading (16% of top sites, 57% of weak ones in taste-skill's study; `craft.md` has twelve ways to open a section instead), meta strings joined with middle dots, labels built as a word, a spaced em dash, and a fragment, tinted near-black standing in for black, a mono face for small data labels, "→" on every link and button.

The template look, from taste-skill's measured gap between strong and weak sites:
- Centered headline over a framed screenshot (7% of top sites, 24% of weak ones).
- A row of icon-plus-sentence feature cards (1% vs 28%).
- A saturated gradient blob or glow behind centered text (gradients overall 22% vs 52%).
- A pill badge above the headline; one word of the headline accented in italic, bold, color, or a gradient.
- Every section a centered title, centered subhead, and a card grid at the same width.
- A stock fade-up on every section (a tuned reveal per `motion.md` is fine); word-by-word reveals outside the signature moment; the blocklisted effects in `motion.md`.
- Logo wall in brand colors, or padded with a marquee to hide that there are four.
- Initials-only avatars, or a quote with no company.

What agents add unasked, from YC's Design Review of AI startup sites. As with the clusters, a look the user pins wins over any tell here: keep it, tell them once that blind critics will still count it toward the cap, and give its `check.mjs` WARN that reason.
- A control that looks live and isn't: an input that takes focus but no typing, a button that does nothing. It pulls attention off the real action.
- Auto-advancing tabs or a carousel whose timer starts before it's in view (`motion.md`).
- A "scroll" cue, or any nudge to do what the visitor would do anyway.
- Random words bolded in body copy.

Banned phrases: revolutionize, supercharge, seamless, effortless, unlock, unleash, elevate, empower, harness the power, cutting-edge, next-generation, world-class, game-changer, transform your workflow, take it to the next level, all-in-one platform, built for the future.

## Conversion evidence

Treat everything but the first row as practice, not law.

| Claim | Status | Source |
|---|---|---|
| Key message and primary action in the first screen | Backed | NN/g eyetracking, 120 users: 57% of viewing time above the fold, 74% within two screens |
| Simpler copy converts better | Correlation | Unbounce benchmark, 41k pages: word count correlates -18.6% with conversion; controlled tests split both ways |
| One CTA beats several | Correlation | Unbounce 2018, self-reported; a Bath University test found more CTAs didn't cut clicks. One goal, repeated, is safe |
| Specific headlines beat vague ones | Practice | No isolated test found |
| Proof beside the CTA beats proof at the bottom | Practice | Vendor claims only |
| An FAQ helps | Contested | AssessmentDay: removing the FAQ lifted sales 62%, no significance reported |
| Risk reversal (trial, guarantee) is required | Practice | No test found |
| Match the message to the ad | Practice | No test found; sensible |
| A typed action (email, prompt) left open on the page beats one behind a click | Practice | Two founder reports, no numbers: Magic Patterns removed its hero prompt box and conversion dropped; Creative Market's tests favored the visible field (YC Design Review, 2026) |

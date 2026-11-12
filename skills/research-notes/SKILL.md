---
name: research-notes
description: >
  Turns raw user research notes, customer interview notes, and call
  transcripts into structured, scannable research notes. Use when given
  messy notes or a transcript from a user interview, customer
  conversation, usability test, or research session, or when the user
  says "clean up these notes", "format this interview", "write up this
  call", or "here are notes from a call". Do NOT use for internal
  meeting notes or recaps (use meeting-notes). Do NOT use to interpret
  what a call means (use call-debrief after this).
---

# Research notes

Clean up raw notes from a customer or user conversation into a short, insight-first record that someone who wasn't on the call can read and use. This records what happened. What it means is a separate step (call-debrief).

## Inputs

- **Raw notes** (always). The interviewer's messy notes: bolding, caps, shorthand, half-formed bullets. This is the primary source. Index heavily on what they chose to write down, because it's the signal for what mattered.
- **Transcript** (sometimes). For filling gaps, exact quotes, and context the notes reference but don't capture. Don't fish for new themes the interviewer didn't flag. If it's not in the notes, they probably left it out on purpose.
- **Who and where** (sometimes). Name, role, company, what they use. Ask if missing.

When notes and transcript disagree, the transcript wins on facts (exact quotes, numbers) and the notes win on emphasis (what the interviewer thought mattered).

## Process

1. Read the raw notes first and understand what the interviewer thought was important.
2. Reference the transcript second to fill gaps and correct quotes.
3. Group by theme, not chronology. The conversation bounced around; the notes shouldn't.
4. Rewrite every bullet. Complete the thought, add just enough context for someone who wasn't there.
5. Trim. Point made, move on.
6. **Preview in chat before saving anywhere.** Show the full cleaned notes, let the user react and revise, and only write to a destination once they've signed off. Where notes get saved (which database, which properties) is defined by the project, not by this skill.

## Output

### Length

Less than a page, and shorter than the raw input. If you're producing more text than you received, you're over-extracting or padding.

### Sections

Four to six sections, each a heading with bullets underneath. Common ones, in the order they usually make sense:

- **Summary** (optional, 2 to 3 bullets). Only when the call had several distinct insights and a TL;DR helps. If it won't fit in three bullets, the takeaways aren't sharp enough.
- **Background.** The use case and team context, not the person's bio. For a repeat customer, mostly what's net-new since last time. One or two bullets.
- **Current workflow.** How they do it today. Neutral.
- **Pain points.** What's broken, frustrating, or missing.
- **Ideal workflow.** What they wish they could do.
- **Usage patterns.** Features they rely on, workarounds they've built, how often they engage.
- **Other notes.** Orphan observations worth keeping.

Let the raw notes decide which exist. Then rename them: a section header should say what the finding is, not what category it belongs to. "Lack of integration with their docs tool," not "Pain points." "Editor experience," not "Usage patterns." Generic labels are placeholders, not final output.

Principles for sectioning:

- Fewer, denser sections beat many thin ones. Seven or more means over-segmented. Thin sections with two generic bullets are worse than one dense section with six specific ones.
- Collapse overlapping themes. If two sections are different angles on the same insight, merge them.
- Workflow and pain collapse when the workflow exists only to illustrate the pain. Keep them separate when they're genuinely different observations.
- Classify bullets by theme, not by when they came up. Put each bullet where a reader would look for it.
- Every section uses bullets, including Background.

### Usability tests are a subtype

When the call was a hands-on test of a prototype or feature, not a discovery conversation:

- Order sections by the discovery arc, not by theme. What they noticed first, tried next, found later. For a usability test, the journey is the data.
- Capture interviewer-side context. "Pointed her to X and asked Y." "Right on cue, he discovered Z." Whether we set up the breadcrumb and whether they found it matters.
- Cut low-priority nits. If a bug doesn't change a product decision, it doesn't earn a bullet. Fold meaningful ones into the section where they emerged.

### Bullets

- **Top-level bullets are full sentences**, one to three each. Standalone observations, not fragments. No artificial cap per section; add as many as the material supports.
- **Sub-bullets carry supporting detail**: a quote, a specific example, a clarification. Not a continuation of the parent thought.
- **Specificity carries weight.** "Had trouble editing" is weak. "Wanted to add a line item, went to Insert in the top bar, and the new line dropped to the bottom of the invoice, outside the section it belonged to" is useful.
- **Consolidate bullets that share an insight.** "Tested the AI live" and "validation was hard" are one thought, not two.
- **Report what was observed, not what it proves.** "Dashboard served its purpose during alignment, then got abandoned" is what happened. "Editing friction turns dashboards into static deliverables" is spin. Three patterns to cut specifically:
  - Cross-call meta-patterns ("same thing X said on their call"). These notes describe this call.
  - Narration framings ("this was the moment it clicked"). If the bullet above shows the moment, naming it is restatement.
  - The customer's own diagnosis ("awareness is the issue, not functionality"). Their theory of their problem isn't the evidence.
  Synthesis is fine when it crystallizes a punchy framing ("their ideal is X") that adds structure.
- **Quotes do real work.** Include one when the exact words carry meaning that paraphrase would lose. Stitch quotes from different parts of the conversation when they reinforce one point. Default to putting the quote in a sub-bullet under the observation it supports, so what happened stays separate from what they said. A quote goes in a top-level bullet only when the quote is the observation, and never in a blockquote, which pulls it out of the observation it supports. Don't write "Ben said" before every quote; the whole doc is about this person.
- **Verb-led where possible.** "Automate reporting for the ops team," not "Reporting for the ops team."
- **Every bullet passes the "so what?" test.** If it doesn't change how a reader would interpret the call or inform a product decision, cut it. Social pleasantries, jokes, and invitations to visit go unless they reveal something about the relationship with the product.
- **Hyperlink tools, packages, competitors, and products** when they have a URL.

### Product framing

- Frame gaps against what we currently offer, specifically. "We have one-off and recurring invoices; installment plans are the gap" beats "their needs don't align."
- Distinguish discoverability gaps from product gaps. "Didn't know the feature existed" is a docs / onboarding problem. "Needs a capability we don't have" is engineering work. Say which.
- Reframe complaints in terms of what we offer where it's true ("automatic bank matching is the more effective path for unreconciled payments than a better import screen").
- Don't overclaim. "Something we don't offer," not "something we don't offer at all." Hedge when unsure about current capabilities.

## Voice

Apply the writing-style skill, notes register. Sounds like Conor, not a transcription service. Research notes are functional, so clarity and scannability over personality. Contractions always, no corporate speak, no filler.

## Checklist

- Less than a page and shorter than the raw input
- 4 to 6 sections, each named for the insight
- Background leads with the use case, not the bio
- Every top-level bullet is a standalone observation someone who wasn't there could follow
- Observations, not conclusions; no cross-call patterns, no narration, no customer self-diagnosis
- Quotes exact (checked against the transcript), earning their place, in sub-bullets
- No pleasantries or color commentary
- Previewed in chat before saving

---
name: product-research
description: >
  Landscape research for a new product or greenfield idea: parallel research
  lanes synthesized into one view with decisions for the next step. Use when
  starting a product from scratch or when the user says "research this", "is
  this buildable", "what's out there", "what do the competitors do", "what
  data exists". Do NOT use for research inside an existing company context
  (product-shaping Phase 2), to log interview notes (research-notes), or for
  a single open question mid-shaping (product-shaping's open-questions
  loop).
---

# Product research

Turn an idea into evidence the next step can act on. The output is a synthesis the user reads in five minutes, backed by lane reports they can verify in one click. Research nobody asked for is wasted, so lanes get confirmed before they run.

## Take context first

Ask for, or pull from what the user brought:

- The idea in a sentence, and anything already written down (a list, a doc, a sketch).
- What the next step is. Shaping needs feasibility and a wedge. Design needs what competitors show. Tech planning needs sources, costs, and a stack. The next step decides what the research has to answer, so name it before proposing lanes.
- Constraints that shape the search: budget, single user or many, markets, platforms, whatever bounds the space.

## Propose lanes

Four to seven lanes. Each one is a question the next step can't proceed without, and each runs on its own without waiting on another. For a new product the usual set is:

- Market: who does this today, what they charge, what they do badly, what nobody does. The evidence: the leaders' 3-star reviews for what's missing, proof people pay (sales rank, public revenue, paid tiers) rather than interest alone, a five-year trend line so a lasting problem isn't mistaken for a fad, and who entered in the last year or two: small, recent entrants winning fast means demand is open, while only big, old leaders means it's saturated.
- Data or inputs: what exists, how far back, what it costs, what's verified live.
- Method: what's known to work, what's known to be noise, what standard separates the two.
- Stack: what a single builder would use, what reference projects survived, what they'd change.
- Plus whatever the idea specifically hinges on (live feeds, legal exposure, a hard-to-get input).

Present the lanes with one line each on what it answers and why the next step needs it, plus two to four acceptance criteria per lane: what a report you'd trust has to contain. Write them as a skeptical fact-checker who gets one shot at a researcher they've never worked with ("the free-tier limit, quoted from the provider's own pricing page, dated"), and write them before any report exists, so the output can't anchor them. Ask before running anything. The user cuts, adds, or reorders.

## Run the lanes

One `researcher` agent per lane, in parallel (Model: researcher role). Each lane gets the idea, the constraints, its question, its acceptance criteria, and the shape of the report it should return. Before a report goes into the synthesis, a fresh `critic` grades it against its lane's criteria and the report contract below, nothing else: each criterion met or not, with the line that shows it (Model: critic role). A missed criterion goes back to the lane once, by resuming it; still missing, the synthesis marks that claim unverified. If agents aren't available, run the lanes sequentially in the main conversation and say so.

Every lane report carries:

- A research date and a scope line.
- Claims marked verified (checked live: a probe, a download, a fetched page) or unverified (docs, writeups, prior knowledge). Verified is the default expectation for anything the next step will build on.
- Source links on every claim, short link text on the specific number or fact.
- Dead ends, named, so nobody re-runs them.
- A closing section on what this means for the next step.

Present each report in full as it lands, not condensed. The user needs to see the evidence. Save each raw report the same day it lands, in the repo (the project's research folder, or a design lead's ignored scratch), never only in chat, since a report that waits for the write-up step gets lost when the session ends. Notion isn't a research archive: it holds the product doc, and only big structural decisions go back there; a report goes to Notion only when the user asks.

After the text lanes land, screenshot the public screens they named (competitors, data sources, tools) with Playwright in one pass, since text reports describe a screen worse than a glance does. Open only the images that change a decision; the rest stay on disk as reference.

## Synthesize

One document that pulls the lanes into a view:

1. The one-paragraph answer. Is it buildable, what's the wedge, what does it cost.
2. Cross-cutting findings. Three to five, each a self-contained argument that draws on more than one lane.
3. Feasibility table, when there's a list to grade (saved ideas, candidate features). One row each: can it be done, from when, with what, and the catch.
4. Gaps ranked by how much they hurt, each with its workaround.
5. Risks worth naming.
6. Decisions handed to the next step. Number them, give a recommendation on each, and mark it as a recommendation. The next step makes the call.
7. Reading order. Which lane to read if you only read one, and why.

Insight over description. Hedge single-source findings ("supports," "is consistent with"). Write it in the user's voice per writing-style.

## Write it up

Where the project keeps docs: the synthesis and the full lane reports in the repo; in Notion only the decisions the product doc takes from them, unless the user asks for a research page. If the destination is Notion, convert tables and verify every write by re-fetching. Record the decisions the next step actually made back on the synthesis page once they're made, with the date, so the research page stays the record.

## Checklist

- Lanes were confirmed before running, each with acceptance criteria written before any report existed.
- Every report was graded against its criteria before the synthesis used it.
- Every claim the next step will build on is verified or flagged as not.
- The synthesis opens with the answer, not the method.
- Decisions for the next step are numbered, with a recommendation, and marked as recommendations.
- The user can get from any number in the synthesis to its source in one click.

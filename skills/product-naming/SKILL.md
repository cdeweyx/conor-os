---
name: product-naming
description: >
  Names a product, app, or feature, from a naming brief through hundreds of
  candidates and scripted availability checks to a final name plus a backup.
  Use when the user says "name this", "name the app", "what should we call
  it", "naming", "rename", "we need a name", "is this name taken", or at
  brand-design's naming step. Do NOT use for taglines or copy (landing-page,
  writing-style), the visual identity (brand-design), or legal clearance
  (the checks are a first look, never legal advice).
---

# Product naming

A name is the brand idea compressed into a word, and it's chosen after the idea, never before: a name out of step with the positioning is, in the words of Igor (a naming firm), "an ugly mess." Left alone, a model in 2026 doesn't produce -ly and -ify names anymore; it produces category puns (Quill, Scribe for a notes app) and cozy artisan nouns (Lantern, Ember, Cairn), and a blocklist just moves it to Harbor and Acorn. What works is the professional method: a metaphor taken from the product's own mechanism, volume (hundreds, not twenty), judgment deferred until the volume exists, and every survivor checked for real before the user sees it.

Read `references/criteria.md` before cutting and scoring; it holds the tests, the scorecard, and the lint. `scripts/check_name.py` runs the availability checks. Read `references/preferences.md` every run, before the brief.

## Where it sits

Inside brand-design, after the brand idea and before the directions, so every direction card carries the real name. On its own for a rename, a feature, or a product that needs a name before any brand work. When run alone, take the brand idea from the product doc, or write a one-line version with the user first.

## Where the user decides

Two calls. Everything else is the agent's.
1. **The shortlist.** Twelve to twenty names, every one already checked, shown in context. The user keeps three to five.
2. **The final name and a backup**, after the finalists' deeper checks and, ideally, a night's sleep.

Expect no "aha." Professional namers say clients almost never love a name on first sight; Pentium, Sonos, Azure, and BlackBerry were all rejected at first. Discomfort is a signal of energy, not a veto. One person decides; never poll a group, since groups agree on what's easy to agree on.

## The steps

1. **Brief.** One page, mostly from what exists: the product's function in one plain sentence ("sends an invoice, chases it when it's late, then matches the payment when it lands"); the brand idea; three attributes; the brands it must stand beside (a Notion-tier noun or a utility name); the competitors' names sorted by type (descriptive, suggestive, evocative, invented; `criteria.md`) to find the empty corner; words and sounds off limits; the language and markets; which platforms and handles matter; and whether an exact .com is required. That last one is the user's trade-off, stated as one: a strong name with a prefix domain usually beats a weak name with the .com. Ask only for what's missing, one question at a time with your assumed answer, then summarize the brief for a yes.

2. **Metaphor map.** Answer six questions about the product's mechanism: what does this job in the physical world, in nature, as a tool, as a role, at its extreme, at its quietest. Add one territory built from the product's own category words (for an invoicing tool: invoice, bill, terms, due, paid, ledger), since users often want a name a stranger can parse (`references/preferences.md`). Group the answers into three naming territories (for an invoicing tool: record and tally; nudge and knock; payday and harvest). Every name comes from a territory, so every name has a reason before it exists.

3. **Generate, decoupled.** Three `worker` agents in fresh contexts, each with a different brief, never seeing each other's lists (Model: worker role): one gets the real brief; one is told it's naming the main competitor; one is told it's naming an unrelated product with the same feeling. Each works through the territories with the vocabulary moves (synonyms, roots from Latin and other languages, compounds, truncations, prefixes and suffixes, real words from other domains) and then a blue-sky pass. Aim for 300 to 500 together; anything generated earlier (a quick list from one prompt) joins the pool, it just isn't the pool. Volume is the method; the good names come after the obvious ones are used up.

4. **Defer, then cut.** First pass: for each, "what could this name do for us?", before anything is rejected. Then cut to 30 to 50 with the tests in `criteria.md`: the swap test, the compound test, drawable, a 15-second origin story, and SCRATCH as the kill screen. Run the lint last, as a check, not the method. Put the cut list away; after step 5's scoring, re-read it once with fresh eyes and pull back anything that deserves a second look.

5. **Score and check.** Score the 30 to 50 on the scorecard and keep the top 15 to 20. Run `python ~/.claude/skills/product-naming/scripts/check_name.py <names...> --category <software|regulated>` on them (usage in its header): prior art on GitHub, App Store titles, domains over registry RDAP with parked and live told apart, package registries, X and Instagram handles, dictionary crowding, and the category's flagged words. Then run the web searches it prints and the USPTO wordmark search in a browser (no public API), reading live exact marks in classes 9 and 42, plus 28 and 41 for a regulated category. A same-category product with the name is fatal; a big brand elsewhere is a penalty. Fewer than twelve survivors means one or two new territories and the three decoupled passes again on them, not a lower bar; the survivors carry over and the new names go through the same cut, score, and checks.

6. **Shortlist (call 1).** Show the survivors on one sheet in context: each name set in the product's current type, in a sentence ("Track your invoices in ___"), as a URL, in the nav, and beside the competitors' names. One line each on its territory and origin. Ask the competitor-swap question before "do you like it": "if a competitor launched with this name tomorrow, how would you feel?" The user keeps three to five.

7. **Finalists.** For each: the origin story, a pronunciation and spelling check (say it, ask someone to spell it), meanings in other languages and in slang, the trademark classes that matter, app store collisions, and one risk. Timestamp every check. Recommend one and a backup with the reason each sits where it does, and suggest sleeping on it.

8. **Final (call 2).** Record the name, its casing, the backup, and the origin line in the Brand section of DESIGN.md (brand-design's `references/brand-section.md`). Buying a domain or registering a handle is the user's action or needs their explicit yes, with the exact domain and price confirmed first; never buy or register on your own. Say once that the trademark look isn't clearance, and for a public launch a trademark attorney's search is the next step.

## Skill pause

Run authoring-skills' Closing a skill update (the skill pause) at the end of every run. What goes where in this skill: picks and rejections with their reasons into `references/preferences.md`; a name the user killed for a reason the tests didn't catch becomes a test or a lint line in `references/criteria.md`.

## Things that go wrong

- Twenty names from one prompt. That's the model's center; the decoupled passes and the volume are what get past it.
- The cozy noun. Lantern, Ember, Cairn, Harbor survive blocklists; the swap test catches them.
- Free handle, taken name. An npm package and a GitHub org can be free while a 5,000-star product in the same audience owns the name; prior art runs before domains.
- Letting the .com choose the name. It's a tiebreaker unless the user said otherwise in the brief.

## Checklist

- Brief on one page; competitor names sorted by type; .com stance is the user's.
- Metaphor map with three territories from the product's mechanism.
- Three decoupled worker passes, 300 or more candidates.
- Deferred pass before cuts; cut to 30 to 50 by the tests; lint run last.
- Top 15 to 20 scored and checked by script; 12 or more survivors or new territories.
- Shortlist shown in context with the competitor-swap question; three to five kept.
- Finalists checked for sound, languages, classes, stores; one recommended with a backup; checks timestamped.
- Name recorded in DESIGN.md's Brand section; no purchase without the user's yes; trademark caveat said once.

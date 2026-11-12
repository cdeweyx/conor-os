# Grammar

The product's objects, what the user does to them, and how high each thing sits, written once for the whole product after the user journey and before any wireframe. The journey is organized by place; the grammar is organized by object, so it catches what the journey hides: an object with one action, an action with no home, a dialog that should be a popover. Arguing "why is this a modal?" costs a table row here and a redraw at hi-fi.

Sources, for when a section needs more depth: Daniel Jackson's *The Essence of Software* (concepts and operational principles), Daniel Rosenberg's object-action matrix (a sparse grid is cognitive load), Johnson and Henderson's *Conceptual Models* (objects, attributes, operations, no widgets), Material 1's elevation, Alan Cooper's application posture. Maggie Appleton's "Grammar" page (Nouns, Verbs, Layers, then numbered beats) is the shape this copies.

## Where it lives

- **Notion (the product doc's design page):** posture, nouns, verbs. Text and tables, commented on like the rest of the doc.
- **Paper (one "Grammar" artboard on the Explorations file):** the layer stack drawn as an exploded stack with its token table, and the beats as a strip of small gray-box frames, numbered, one caption each. Lo-fi rules hold: gray boxes, one font, no color.
- **Not an interactive page.** The beats become the step list of the prototype at motion-design; that's where they move.

## The five sections

1. **Posture.** One line: sovereign (held open for a session, owns the screen) or transient (comes and goes for one job). It sets the chrome budget, and the chrome budget sets how many layers the product can afford.
2. **Nouns.** A table: noun, purpose in one sentence, attributes, relationships (has, part of, kind of), and an operational principle as an if/then line. A noun whose if/then you can't write doesn't earn its place yet. The noun names are the product's vocabulary: one word per thing, and DESIGN.md's terminology line copies them.
3. **Verbs.** The object-action matrix: nouns as rows, verbs as columns, a mark where the action exists. Under it, every sparse row and column with a decision: cut, merge, or a written reason ("read-only by nature"). An empty cell that should be full is a product call; it goes to Open Questions, not to hi-fi. Every authoring verb (create, edit, write) names the fixed structures it offers (clauses, a field per attribute, a short list of styles); free text in one needs a written reason, the same as a sparse row.
4. **Layers.** A fixed stack from ground to top, each with what lives there, its lifetime, how many can be open at once, what it's anchored to, and its tokens (shadow, hairline, spring). The rule: a thing is only as high as it is temporary. Every overlay in the journey gets a row; a persistent thing on a short-lived layer fails.
5. **Beats.** Five to eight numbered steps through the product's core loop, in prose, each naming the noun, the verb, and the layer in play, and what the user's attention does.

## Citing a verb (Interface Lineage)

A lens, not a step: pull one page when a verb is contested, not one per cell. Interface Lineage is a free, citable corpus of interface patterns and principles; every page has a Markdown twin. Its MCP needs a paid membership, so use curl.

- **Find the slug.** `curl -s https://interfacelineage.com/llms.txt` lists every pattern and principle with its slug.
- **A contested verb.** `curl -s https://interfacelineage.com/<slug>.md` (for example `grace-window-undo`); read The move and When not to use it, and write the slug beside the verb's decision.
- **A destructive verb** (delete, retire, discard, send). A user pick already in hifi-design's preferences (an inline confirm in the row, say) outranks the citation; cite to inform a verb nobody has ruled on. Check it against the Safety & Reversal family: `curl -s https://interfacelineage.com/safety-reversal.md`, then the principle that fits (`undo-absolves-the-warning`, `delayed-commit-over-confirmation`, `friction-proportional-to-consequence`). A confirm dialog where an undo would do is the usual finding.

Slugs checked live in November 2026.

## Worked example (an invoicing tool)

**Posture.** Sovereign: a session of bookkeeping at a desk. Dense tables at full width, a nav a step dimmer than content, no hero.

**Nouns**

| Noun | Purpose | Attributes | Relationships | Operational principle |
|---|---|---|---|---|
| Client | Who you bill | name, email, payment terms | has invoices | If you set a client's terms, then each new invoice for them takes that due date |
| Invoice | A bill you draft and send to a client | number, client, total, due date, status | has line items and payments | If you send an invoice, then it reads Sent on Invoices until it's paid or overdue |
| Line item | One charge ("design work, 6 hours") | description, quantity, rate | part of an invoice | If you change a line item, then the total recalculates |
| Payment | Money received against an invoice | amount, date, method | part of an invoice | If payments cover the total, then the invoice reads Paid |

**Verbs**

| | create | edit | send | record | delete | open |
|---|---|---|---|---|---|---|
| Client | ✓ | ✓ | | | | ✓ |
| Invoice | ✓ | ✓ | ✓ | | ✓ | ✓ |
| Line item | ✓ | ✓ | | | ✓ | |
| Payment | | | | ✓ | | ✓ |

Sparse: Payment has no edit or delete, since a wrong payment is fixed by recording a correction, not by rewriting the books. The gap it surfaces: can you remove a client who has past invoices, or only archive them? A product call, settled here.

**Layers**

| Layer | What lives there | Lifetime | At once | Anchor |
|---|---|---|---|---|
| Ground | The page (Invoices, Clients, one invoice) | always | one | the window |
| Card | An invoice row, a client row | as long as the data | many | the ground |
| Panel | An invoice's detail panel | while an invoice is selected | one | its edge |
| Popover | Line item editor, client picker | seconds | one | its trigger |
| Dialog | Send | one decision | one | the center, blocking |

The row that earns the argument: Send is a dialog. Does confirming the recipient and total need to block the page, or is an undo window after sending enough?

**Beats**

1. Land on Invoices, every invoice by status (ground).
2. Create one and pick the client; the due date fills from their terms (invoice, create; popover).
3. Add a line item; the editor grows from it (line item, popover).
4. Change the rate; the total recalculates in place (invoice, edit).
5. Send it; the dialog confirms the recipient and the total (dialog).
6. It reads Sent on Invoices (card).
7. Open it and record a payment; it reads Paid (payment, panel).

## Checks it hands downstream

- **Explorations:** every option draws the same nouns and verbs; options differ in the starting object and the reading order, not in the grammar.
- **Hi-fi done checklist:** every element on the surface maps to a noun, verb, or attribute (an orphan gets cut or the grammar amended first); every overlay names its layer and its lifetime fits; every verb has a visible signifier.
- **Hi-fi critics:** the layer stack is in DESIGN.md, so compliance scores shadow, hairline, and anchor per layer from the screenshot.
- **Prototype:** the beats are motion-design's step list; motion crossing layers is interruptible.

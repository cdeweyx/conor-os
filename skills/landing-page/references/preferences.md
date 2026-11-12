# Preferences

The user's picks from past landing pages: a hero layout chosen over another, a reference they liked or rejected, a word they changed in the copy deck, a critic finding they overruled. Read before intake; the first direction starts from them.

Write each pick as the principle with the product in parentheses and the date.

- The product is the hero, and the page stays simple. A simple reference calibrates the restraint; it isn't a template, so work from first principles.
- A small feature grid with real examples and stylized screenshots of each feature. Showing what the product does beats showing one sample of its data. Kept over a cold critic who wanted it cut.
- An FAQ that answers the objections a skeptical buyer brings, three or so.
- A page explaining how a number is made is named plainly and linked from the footer and from the number it explains, never the top nav: the few who check find it, and nav slots go to actions.
- Signed-out nav: wordmark, the main product link, Pricing, Sign in, and one filled primary action.
- Section heads say plainly what the visitor gets; a clever or abstract head reads as vague. A plans head names what paying buys, and an FAQ is headed "FAQ".
- The bar is tier-one marketing sites, not app screens. Critics compare against marketing pages (Linear, Vercel, Stripe, Raycast class), never a product dashboard, and the critics' median is a floor for what reaches the user, never a reason to hold a direction from him: the layout comes to him after round one (see the hero layout line below). Flat panels, kit chips and a form-field builder read as unfinished. Examples are rich, engaging objects, not pills, and the main action is a showpiece input, not a text field with a button.
- Polish references the user names (superx.so, Modal, and others shared together) calibrate the finish together, never one of them alone, reached from first principles of data panels and charts, not their layout; critics score against it, and the loop keeps going past its round cap until the hero reaches that finish.
- Design exploration happens on Paper, never as coded prototypes: motion is drawn as key-frame artboards, and code starts only once a direction is picked.
- Never headline the product's own misses or undersell its best result. Honesty lives in each number on its card, and the headline sells what the visitor gets. A cold reader's vote for a "brutally honest" head doesn't outrank this.
- When the user rejects a line, the next options start from a new angle, not a rewording of the rejected one.
- When a product both improves what the buyer already has and gives them something new, the closing action leads with the new.

A `check.mjs` WARN explained with the same reason three runs running is a house call, not an exception: write it here as a line ("`overflow-wrap` on display heads: skipped, the display face never sets a word longer than the column") and stop re-explaining it. (From Hallmark's waiver ledger.)

- **The hero layout he picked, after twelve rounds:** a centered stack, not a split. Generous air above the headline; the center is only the headline, one sub, the input, and a row of example pickers under it. Nothing else competes on the first screen: no stats, keys or legends; a result number, if any, small inside the input and never the biggest thing. Pressing a picker changes the hero (the input's text and a muted, data-drawn backdrop); the backdrop is the product's own chart treated as atmosphere, fading up toward the middle, "futuristic" in the Modal and Railway sense but built from the product's data, never decoration.
- **Controls look current, not default:** the input, its button and the nav buttons are drawn to the tier-one bar (Linear-class), never a form field with a button beside it; a long input sentence never collides with the button; pickers are rich objects with their own mini chart, not chips.
- **A live hero opens on a selected example, never a neutral rest state:** pickers that start unselected read as captions, not controls, and the first example should be a strong one so a visitor sees the product at its best. The page ground gets some flavor (a hue, a fine texture or a wash) rather than flat near-black, drawn and judged in both modes. Texture that keeps the ground neutral beat a colored ground (he picked a 1px dot lattice over a flat tint, against the lead's and two critics' lean), so offer a fine texture beside any hue.
- **Mobile shows the busyness first:** check every hero at 390 for competing copy and numbers before he sees it; a stacked desktop fails.
- **How to not take twelve rounds:** round one draws different layouts (centered, split, stacked) and he picks the layout from those, before any critic-driven polish; critics polish a picked layout, they don't choose it (critics preferred the split for four rounds; he picked the centered stack on sight). Then structure, then an ambitious styling pass once the structure is right ("Be ambitious with this design round and styling ... You could do better, even better than you think you can"). Detail calls (tokens, copy lines, rest states) wait for the near-final review.

- **Minimal above the fold, richer as it scrolls.** The first screen carries the least: the question, the action, the one answer, little else. Detail cut from the hero (stats, keys) gets a named home lower on the page, so a cut never loses it; complexity grows section by section. Measured on Modal, Railway, Stripe, superx and Linear, which also share a stacked first screen (text on top, one product frame below on the page's axis, cut by the fold).

## Build log

One line per run: product, date, hero layout (split, product-first, type-only, centered), section openings used, palette (ground, ink, accent as hex). The direction step reads the last three and changes at least the hero layout or the palette, so two products in a row don't ship the same page. A pick above outranks the log.

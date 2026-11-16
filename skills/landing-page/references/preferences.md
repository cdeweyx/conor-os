# Preferences

The user's picks from past landing pages: a hero layout chosen over another, a reference they liked or rejected, a word they changed in the copy deck, a critic finding they overruled. Read before intake; the first direction starts from them.

Write each pick as the principle with the product and the date in parentheses. The user's words behind each pick go in `preferences-archive.md` under the same line name, so this file stays under its cap.

- The product is the hero, and the page stays simple. A simple reference calibrates the restraint; it isn't a template, so work from first principles.
- A small feature grid with real examples and stylized screenshots of each feature. Showing what the product does beats showing one sample of its data. Kept over a cold critic who wanted it cut.
- A page explaining how a number is made reads as one centered column (a 640 measure, charts stepping out wider), not a two-column ledger of claim and proof, even when the lead and two of three critics pick the ledger; it ends on its last section and the footer, with no closing link band left hanging.
- An FAQ that answers the objections a skeptical buyer brings, three or so.
- A page explaining how a number is made is named plainly and linked from the footer and from the number it explains, never the top nav: the few who check find it, and nav slots go to actions.
- Signed-out nav: wordmark, the main product link, Pricing, Sign in, and one filled primary action.
- Section heads say plainly what the visitor gets; a clever or abstract head reads as vague. A plans head names what paying buys, and an FAQ is headed "FAQ".
- The bar is tier-one marketing sites, not app screens. Critics compare against marketing pages (Linear, Vercel, Stripe, Raycast class), never a product dashboard, and the critics' median is a floor for what reaches the user, never a reason to hold a direction from him: the layout comes to him after round one (see the hero layout line below). Flat panels, kit chips and a form-field builder read as unfinished. Examples are rich, engaging objects, not pills, and the main action is a showpiece input, not a text field with a button.
- Polish references the user names (superx.so, Modal, and others shared together) calibrate the finish together, never one of them alone, reached from first principles of data panels and charts, not their layout; critics score against it, and the loop keeps going past its round cap until the hero reaches that finish.
- Named favorites, first in any gold set: roma.app and generalintelligencecompany.com, for animation, layout, visuals and copy together. Read for technique (`craft.md`, What to steal), never as a look to copy.
- Layout and look are explored on Paper, never as coded prototypes; code starts only once a direction is picked. Motion is the exception: Paper holds only the states sheets and a few key frames per moment (start, peak, settled), and motion is reviewed in one throwaway HTML prototype with toggles, recorded for critics, then tested by the user.
- Never headline the product's own misses or undersell its best result. Honesty lives in each number on its card, and the headline sells what the visitor gets. A cold reader's vote for a "brutally honest" head doesn't outrank this.
- Proof on a public page is a sample big enough to hold: never show results from only a week or two of data, since a short sample reads as broken.
- When the user rejects a line, the next options start from a new angle, not a rewording of the rejected one.
- When a product both improves what the buyer already has and gives them something new, the closing action leads with the new.

A `check.mjs` WARN explained with the same reason three runs running is a house call, not an exception: write it here as a line ("`overflow-wrap` on display heads: skipped, the display face never sets a word longer than the column") and stop re-explaining it. (From Hallmark's waiver ledger.)

- **The hero layout he picked:** a centered stack with air above the headline; the center is only the headline, one sub, the input and a row of example pickers. No stats, keys or legends on the first screen; a result number, if any, small inside the input. A picker changes the input's text and a muted backdrop drawn from the product's own data, never decoration.
- **Controls look current, not default:** input, button and nav drawn to the tier-one bar (Linear-class), never a field with a button beside it; long input text never collides with the button; pickers are rich objects with a mini chart, not chips.
- **A live hero opens on a selected example, never a neutral rest state:** unselected pickers read as captions; land on a strong example. The ground gets flavor, not flat near-black; offer a fine texture beside any hue, since he picked a 1px dot lattice over a tint the critics and lead favored.
- **Mobile shows the busyness first:** check every hero at 390 for competing copy and numbers before he sees it; a stacked desktop fails.
- **How to not take twelve rounds:** round one draws different layouts and he picks one before any critic polish (critics favored a split for four rounds; he picked the centered stack on sight). Then structure, then an ambitious styling pass. Detail calls wait for the near-final review.
- **On a phone, each example fills the same space.** When a live hero swaps examples, every example's chart sits the same distance under the controls and stays above the fold at 390; a scale shared across examples leaves one floating high and another cut off. Desktop can keep one shared scale.
- **Plans sell paid and sell yearly.** Paid gets the visual weight (a light touch of color, never a loud badge), yearly reads as the better deal (the monthly price times twelve struck through beside the yearly price), and the action names what you get, not a verb about the product's mechanics. Free stays visible but quieter.
- **Don't advertise what's free to browse.** A section that offers the product's ready-made examples sells starting from them, not that they're open without an account.
- **Waits are a styled moment, not a status page.** A post-sign-up or loading wait is generic and centered, with no one item's title on it: real visuals that animate through named steps, paced on purpose (artificial time is fine), then done.
- **Dialogs carry no reassurance copy.** Cut lines that explain what the product obviously does; consent fits one line, and anything the Terms already cover stays out of the flow.
- **Minimal above the fold, richer as it scrolls.** The first screen carries the least: the question, the action, the one answer, little else. Detail cut from the hero (stats, keys) gets a named home lower on the page, so a cut never loses it; complexity grows section by section. Measured on Modal, Railway, Stripe, superx and Linear, which also share a stacked first screen (text on top, one product frame below on the page's axis, cut by the fold).

## Build log

One line per run: product, date, hero layout (split, product-first, type-only, centered), section openings used, palette (ground, ink, accent as hex). The direction step reads the last three and changes at least the hero layout or the palette, so two products in a row don't ship the same page. A pick above outranks the log.
- Motion can run past `references/motion.md`'s "still below the hero" budget when the user asks for it: one landing had the whole page drop and settle in on load, every section animate as it scrolls in, and a rich nav hover. Keep the blocklist and the no-word-split rule; spend the extra on the product's own data drawing, not on generic fade-ups.

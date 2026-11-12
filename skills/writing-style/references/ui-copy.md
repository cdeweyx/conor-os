# UI copy

Words inside the product: labels, errors, empty states, confirmations. Plain beats clever here, because a tired reader has to get it on the first pass. The product's own preferences win where they disagree (hifi-design's `references/preferences.md` and the project's DESIGN.md). From jakubkrehel/skills `better-writing` (MIT).

## Before writing

List the noun for each object and the verb for each action, then reuse them. If it's "Archive" in the menu, it isn't "Move to storage" in the toast. A flow keeps one vocabulary from start to finish.

## Key moments

The strings a newcomer meets first (the front door, the primary action, a pending toast, a refusal) get a loop like a design, never a one-pass rewrite: an inventory with `file:line` and the calls already settled; a long list per moment with a top three and the current string kept in as a control; six blind readers with no context rank each set (Model: critic role); then the user picks in a "Decisions for you" table.

## Tone follows the stakes

| Context | Tone |
| --- | --- |
| Success, onboarding, empty states | Warm, can be light |
| Routine actions, settings | Neutral, minimal |
| Errors, destructive confirmations | Calm, plain, zero playfulness |
| Data loss, security | Serious, explicit |

## The rules

- **Buttons start with a verb:** "Send", "Save draft", "Delete project". Icon-only buttons get the same treatment in their accessible name: "Delete project", never "Trash icon".
- **Links say where they go:** "Read the billing docs", never "Click here". Two "Learn more" links on a page each need a suffix.
- **Toggles describe the ON state:** "Send read receipts", never "Don't send read receipts".
- **Errors say how to fix it, beside what broke:** "Enter a date as DD/MM/YYYY", not "Invalid date". No blame, no "oops", no exclamation marks. If the same error keeps firing, change the interaction.
- **Undo beats confirmation** when the action is reversible and frequent: act at once, then "Project archived. Undo".
- **Confirm first** when it can't be undone, affects other people, or destroys many things. The title names the action and object ("Delete 'Q3 report'?"), the body says what's lost with counts, and the buttons are verb plus object, never Yes and No.
- **Empty states point forward:** say what goes here and offer one next action. A filtered empty state names the query and offers a way out. Don't park information there, since it disappears once content exists.
- **Placeholders show an example** in the accepted format, never an instruction.
- **Status strings run parallel:** "Saving changes…" resolves to "Changes saved". A partial result gives both counts: "9 of 12 files uploaded. Retry 3 failed files".
- **The category's slogans are jargon:** a word the niche's marketing leans on reads as a buzzword in the product, even when a voice round liked it. Say what the tool does in the reader's own words.
- **One capitalization per element type.** Sentence case unless the project says otherwise.
- **Build strings whole:** no sentence assembled around a variable, and plurals through `Intl.PluralRules`, not `n === 1 ? "" : "s"`. "1 members" is the classic break.

## Detection

Grep for these on any surface. Each hit is a lead to check, not a verdict.

| Pattern | Fix |
| --- | --- |
| `Click here`, a link reading `here`, two identical `Learn more` | Name the destination |
| `Oops`, `Something went wrong`, `!` in an error | Say what failed and the next step |
| `Are you sure` | Name the action and the object |
| `successfully` | Cut it: "Changes saved" |
| `Please` in a routine instruction | Cut it |
| `>OK<`, `>Yes<`, `>No<` on a dialog button | Verb plus object |
| A toggle label starting `Don't`, `Disable`, or `Hide` | Describe the ON state |
| `=== 1 ? "" : "s"` | `Intl.PluralRules` |

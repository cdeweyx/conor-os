# The Brand section of DESIGN.md

The brand lives at the top of DESIGN.md, in the open spec's Overview ("Brand & Style") position, above Colors. It holds what would survive a complete visual redesign; the tokens and sections below hold what could change in one. The test for any line: if it should survive a redesign it's brand, and if it could change without repositioning the product it's design (caiopizzol/brand.md).

Split it into a separate BRAND.md only when a second surface needs its own DESIGN.md (a marketing site, decks). Then DESIGN.md copies the brand's core values under role names with a provenance table, and links up with `brand: ../BRAND.md` in its front matter.

## Template

The precedence line goes in every Brand section so each skill that reads DESIGN.md resolves a conflict the same way. When the section doesn't cover something (a chart's second series, a missing colorway), use the closest rule it has, say what you chose, and ask for the asset rather than inventing one (from LangChain's design-agent brand pack).

```markdown
## Brand

**Precedence.** The person's ask for this piece, then a reference they supplied, then this section, then a skill's defaults.

**Idea.** <one sentence; fails if a competitor's name fits>
**Attributes.** <three words, each with what it rules out>
**Name.** <name>, <why, one line>. Written as <exact casing>; never <misuses>. Backup: <name>, checked <date>.
**Borrowed from.** <the physical object or world>
**Mechanism.** <the direction's mechanism sentence>
**Expression move.** <the one loud thing, and where it's allowed>

**Mark.** <construction in one line>. Fill is currentColor.
**Wordmark.** <face and weight>, <the one cut>. Outlines, never live text.
**Logo use.**

| Asset | Use | Minimum | Clear space |
|---|---|---|---|
| Lockup | <light grounds, the default> | <n>px wide | <in a unit of the mark, e.g. four stroke widths> |
| Lockup, reversed | <dark grounds> | <n>px wide | As the lockup |
| Mark | <favicon, avatar, small sizes> | <n>px | <a quarter of the mark's width> |
| Mark, reversed | <small, dark grounds> | <n>px | As the mark |

Colorways: <ink on paper, paper on ink, one-color accent>; no others. Never <stretched, recolored outside the palette, on busy grounds, outlined>.

**Voice.** <five adjectives>. Sentence case everywhere. Banned words: <list>.
| Before | After |
|---|---|
| <real product line> | <rewritten> |

**Scaling.** <only when the brand kit generator was ticked: how to make new graphics in the system with the generator and visual-assets' image tools, one or two lines>

**Motion principles.** <three, named, one line each>; motion-design builds from these.

**References.** <name>: borrow <trait>, don't copy <trait>. (three to five)
**Anti-reference.** <name>: <what it stands for that this brand isn't>.

**Deny list.** <the category's three clichés, plus anything the user ruled out>.
```

## Provenance

Below the Colors and Typography token tables, one column says where each value came from: the sprint that chose it ("color sprint, option B"), or what it's derived from ("accent at 12% on paper"). Without it nobody can tell a decision from a derivation, and the next rebrand undoes decisions by accident.

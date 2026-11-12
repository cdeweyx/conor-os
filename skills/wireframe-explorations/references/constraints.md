# Lo-fi constraints

Paste the block into every generation prompt. The deny list only moves the median; what makes a wireframe look designed is the subject (the product's real objects, numbers, and ledgers), so add product-specific positives after it.

## The block

```
LO-FI WIREFRAME CONSTRAINTS
Deny: any web font or second typeface; any gradient; any shadow; border-radius above 2px; icons or emoji
  of any kind; eyebrow or overline labels; ALL-CAPS labels; lorem ipsum; "Image" boxes; invented numbers;
  hero sections; three-card rows; bento grids; KPI tile rows without a comparison; sidebar plus topbar
  shell unless the surfaces require it; fake browser chrome; status pills; hover or entrance animation.
Require: the shared wireframe.css, black on white, grays from the stylesheet only, weight and size as the
  only emphasis.
Require: real content from the product doc (real object names, records, sample sizes, prices).
Require: tables as the primary surface; numbers right-aligned, tabular-nums; headers match column alignment.
Require: every number sits next to its comparison (baseline, break-even, prior period).
Require: section height follows content; vary density.
Require: states rendered on the same page: empty, thin data, and any error the journey named.
Require: one sentence at the top of each option stating the decision the screen supports.
Before coding: a four-line plan (surfaces, primary table, the one highlighted thing, states), then ask
  "would I produce this for any similar prompt?" and change what fails.
```

## Grays and sizes (from wireframe.css)

- Ink #111, secondary #555, tertiary #767676 (the 4.5:1 floor on white), hairline #d0d0d0, marks #949494.
- Spacing 4, 8, 12, 16, 24, 32, 48. Type 12, 13, 14, 16, 20, 24, 32.
- Rows 40px for lists and tables, 32px for dense stat rows. Sidebar basis 280px. Measure 65ch.
- Contrast: gray text at least 4.5:1, chart marks at least 3:1.

## Scanner

Run over every generated file before anyone looks. A hit is a constraint violation, not a style choice.

```bash
grep -n -i -E "font-family|@import|fonts.googleapis|gradient|box-shadow|text-shadow|backdrop-filter|border-radius: *([3-9]|[1-9][0-9])px|<svg|<i class|lorem|ipsum|transition|animation|:hover" "$@"
perl -ne 'print "$ARGV:$.: emoji\n" if /[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]/' "$@"
```

`font-family` is allowed once, in wireframe.css. Anything else is a hit.

# Removed signals

Regressions don't show in the finished code, only on the `-` side of the diff. `scripts/removed-signals.sh <diff>` prints deleted lines that carry an interface signal, and the interface lens runs only when it prints something. From jakubkrehel/skills `interface-review` (MIT).

A signal is a lead, not a finding. A removal is a regression only when nothing in the change replaces it.

| Removed | Severity if nothing replaces it | What was lost | Rules live in |
| --- | --- | --- | --- |
| `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-live`, `role=` | P1 | The control or region's name, description, or announcement | better-accessibility |
| `alt=`, `<label`, `for=`, `htmlFor`, `scope=` | P1 | The link between an image, field, or cell and its text | better-accessibility |
| `<button`, `<a `, `<nav`, `<main`, `<ul` swapped for `div` or `span` | P1 | Keyboard and screen-reader behavior, traded for styling | better-accessibility |
| `:focus-visible`, `:focus`, `outline`, `tabindex` | P1 | The focus indicator, or the element's place in the tab order | better-accessibility |
| `prefers-reduced-motion` | P1 | Motion now ignores the system setting | better-accessibility |
| `prefers-contrast` | P2 | Colors now ignore the contrast setting | better-accessibility |
| `text-wrap`, `line-clamp`, `overflow-wrap`, `tabular-nums`, `font-variant-numeric` | P2 | Wrapping, truncation, or numeral alignment changed silently | hifi-design's `references/type-rendering.md` |
| `lang=`, `dir=` | P2 | Language metadata or text direction | better-accessibility |

## Equivalent replacements

These clear the signal. Drop a removal one of them explains before anything else:

- `aria-label` giving way to `aria-labelledby` pointing at visible text that still names the action.
- An explicit `role` dropped because the element became the native equivalent, such as `role="button"` going when a `div` becomes a `<button>`.
- `outline` replaced by a `box-shadow` ring on the same `:focus-visible` selector.
- `tabindex="0"` dropped from an element that's now natively focusable.
- The same attribute moved to another line, file, or shared component in this diff.
- The element itself deleted on purpose, as the brief asked. A removed feature takes its label with it.

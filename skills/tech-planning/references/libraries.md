# Libraries

A curated list of the library to reach for per frontend job, so the plan doesn't hand-roll a toast or pick an abandoned package. From Emil Kowalski's pick-ui-library (MIT), with our defaults folded in. Read it at the spike's stack rings: a job on this list starts from its pick, and choosing something else needs a reason in a decision record.

## How to use it

- Name the job, not the library someone mentioned. "A dropdown" is a primitives job (Base UI), whatever was asked.
- Check what the repo already has. If it uses a listed library, keep it. If it uses a competitor, flag it in the plan and don't churn it unasked.
- One pick per job, one sentence on what it's for. Off the list, say so and pick from your own knowledge.

## The `ui/` layer

A library owns behavior; the product owns the look, once. Every component DESIGN.md names (overlay, buttons, segmented control, callout, the table shell) is one file under `src/ui/` that wraps its primitive and takes every value from the token variables, and feature code imports from there. Without it each implementer re-derives the same recipe from DESIGN.md's prose: on one build the tokens held (no raw hex anywhere) while five feature folders each styled their own popover and three wrote the same text button, and about one PR in fifteen was a sweep to make surfaces match (13 of 191; most fixed a primitive or a Paper artboard, one a section above them). Agents use a component that exists and rebuild one that's only described.

- Built at M0 from hi-fi's `ui/` spec, only the components the spec names, with a dev-only `/dev/ui` route that renders each in every state; the Paper "Specimen · ui" artboard is its pair, and the screenshot check covers both.
- A lint rule bans importing the primitives package outside `src/ui/` (`no-restricted-imports`), beside the literal lint.
- Grow by extraction: the second time a feature writes a style block another feature already has, it's extracted into `ui/` first, with only the props its callers use. A copy is the same visual section built twice in code; one component rendered on two routes is one, not two (one brief listed a shared results panel as a duplicate). Agents repeat a guess before a third copy arrives, so the usual rule of three is too slow; speculative props are the failure on the other side.
- Not shadcn. It requires Tailwind, which fights the plain-CSS token handoff, and its presets are the generic look DESIGN.md exists to avoid. Take its idea (owned source in the repo), not the package.

## The list
### UI components & primitives

| Task | Library |
| --- | --- |
| Unstyled, accessible UI components (dialogs, popovers, menus, selects…) | [base-ui](https://base-ui.com) |
| Command menus (⌘K palettes) | [cmdk](https://cmdk.paco.me) |
| Toasts / notifications | [Sonner](https://sonner.emilkowal.ski) |
| One-time password / verification code inputs | [input-otp](https://input-otp.rodz.dev) |
| Live tuning knobs / control panels | [DialKit](https://joshpuckett.me/dialkit) (our pick, used at hi-fi's prototype step); [Leva](https://github.com/pmndrs/leva) is the alternative |

### Motion & visuals

| Task | Library |
| --- | --- |
| General-purpose animation (springs, layout animations, enter/exit) | [motion](https://motion.dev) (Framer Motion) |
| Animating numbers (counters, prices, stats) | [NumberFlow](https://number-flow.barvian.me) |
| Animated text components | [torph](https://torph.lochie.me/) |
| 3D globes | [Cobe](https://cobe.vercel.app) |
| Dynamic OG images (HTML/CSS → SVG/PNG) | [Satori](https://github.com/vercel/satori) |
| Syntax highlighting | [shiki](https://shiki.style) |

Reach for motion when you need springs, layout animations, exit animations, or gesture-driven values. A simple hover or fade doesn't need it, plain CSS transitions are the right tool there.

### Charts

| Task | Library |
| --- | --- |
| Real-time / streaming charts | [Liveline](https://github.com/benjitaylor/liveline) |
| General charts (static or interactive dashboards) | [recharts](https://recharts.org) |

The split: if data points arrive live and the chart scrolls with time, use Liveline. Everything else is recharts. Either way, form and palette come from dataviz and DESIGN.md, and the chart binds straight to the tokens.

### Interaction & performance

| Task | Library |
| --- | --- |
| Drag and drop | [dnd kit](https://dndkit.com) |
| Virtualization (long lists, large tables) | [Virtuoso](https://virtuoso.dev) |

### State & styling

| Task | Library |
| --- | --- |
| State management | [zustand](https://zustand.docs.pmnd.rs) |
| Constructing `className` strings conditionally | [clsx](https://github.com/lukeed/clsx) |
| Type-safe, variant-driven styling for Tailwind | [cva](https://cva.style) |
| Theme switching / dark mode (no flash on load) | [next-themes](https://github.com/pacocoursey/next-themes) |

Our default is plain CSS against the DESIGN.md token variables, no Tailwind theme (it rounds values to the nearest utility), so cva only applies when a project already runs Tailwind. next-themes is Next.js only. The styling split: clsx for ad-hoc conditional classes; cva when a component has real variants (size, intent, state) that deserve a typed API. They compose, cva uses clsx-style inputs internally.

## Common mismatches to catch

- **Toasts built by hand or with a modal library** → Sonner exists for exactly this.
- **A primitive imported and styled inside a feature folder** → its wrapper in `src/ui/`, or extract one.
- **A style block copied from another feature** → extract it into `src/ui/` before the second use ships.
- **A `<div>`-based dropdown/dialog with manual focus handling** → base-ui, which handles accessibility, focus trapping, and dismissal.
- **Animating a number by re-rendering text** → NumberFlow handles digit transitions properly.
- **Rendering a 1,000+ row list directly** → Virtuoso before reaching for pagination hacks.
- **A `useState`-per-component web of props for shared state** → zustand.
- **Template-literal className ternaries three conditions deep** → clsx (or cva if it's variant-shaped).

The mismatch list above goes into the build's CLAUDE.md as a standing rule, so every build session catches them.

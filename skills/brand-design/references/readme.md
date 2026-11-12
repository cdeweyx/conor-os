# README

A repo's README is its front door: the top fold says what it is and makes someone want it, the body serves a cold reader. Read this when a repo needs its README made or redone.

## Examples

Look at these before drawing anything. Each is here for one move.
- **Ours, ConorOS** (this repo's `README.md`): a pixel lockup, a one-line tagline, a links row, then a 1-bit boot-screen hero whose icon row is the process's steps. A repo with no UI, shown through its own parts in a world the user likes.
- **[tldraw](https://github.com/tldraw/tldraw):** a 2:1 lockup hero at full column width, then a short tagline and three links.
- **[Ghostty](https://github.com/ghostty-org/ghostty):** mark, name, two-line tagline, five links, zero badges. The smallest top fold that still feels finished.
- **[Raycast extensions](https://github.com/raycast/extensions):** the product drawn as a blueprint (wireframe and guide lines on one brand color). The pattern for a concept hero.
- **[uv](https://github.com/astral-sh/uv):** the hero is proof, a small benchmark chart with a caption.
- **[mattpocock/skills](https://github.com/mattpocock/skills):** the catalog to copy for a repo of many things: a heading per group, then `- **[name](path)**: one sentence`.

## Top fold

Centered, in this order: the mark or lockup (about 320 wide), one tagline under about 12 words, a row of three to five links to the README's own sections, no more than three badges, then the hero.

- **Hero size:** 2:1, drawn at 1440×720 and exported at 2x (2880×1440), shown at `width="100%"` so it fills GitHub's 838px column. Check every candidate at 838 wide; anything under about 12px there is texture.
- **A product with a UI:** the hero is the real product composed like a launch-page product shot, cropped to what it's for, on a brand backdrop that doesn't compete, crisp at 2x, no tilt or fake devices. The product stays the subject; the invention goes into the staging, which shouldn't repeat the last product's.
- **No UI:** an idea drawn from the repo's own parts (its steps, its pieces, its output). Never a stock illustration, a terminal screenshot, or a gradient with the name on it.

## Rules

- **No counts, versions, or model names** in the hero or tagline. The repo changes weekly.
- **Only our own names in the hero.** A vendored or adapted skill appears as its activity ("quality", not break-it).
- **Every item in a row at the same weight.** Highlighting one icon, or graying the rest, pulls the eye off the others.
- **No roadmap, milestones, or planning links.** That lives in the tracker and `docs/`.
- **It stays current:** a PR that changes setup, usage, configuration, or a command updates the README in the same PR.

## GitHub mechanics

- **Light and dark:** two `<img>` tags, `src` ending in `#gh-light-mode-only` and `#gh-dark-mode-only`. These follow GitHub's theme setting. `<picture>` with `prefers-color-scheme` follows the OS instead, so on ConorOS a light OS with GitHub set to dark showed the light lockup, black on near-black. When a mechanics rule like this lands, run `readme-check.py` on every repo whose README this skill made and file the misses the same session: one repo's README kept `<picture>` until the user caught it.
- **URLs:** absolute, `https://github.com/<owner>/<repo>/raw/main/<path>`.
- **SVG:** GitHub loads no fonts in an SVG image, so outline all text to paths (`scripts/wordmark.py`).
- **Stripped:** `style`, `class`, inline `<svg>`, `<video>`. `align`, `width`, `<details>` survive.
- **Check:** `python3 -I ~/.claude/skills/brand-design/scripts/readme-check.py README.md` catches missing files, live SVG text, emoji headings, badge walls, counts in the top fold, images without a dark version, and images too small for 2x. Then look at the live page in both GitHub themes; with no browser in the session, ask the user for a screenshot of each.

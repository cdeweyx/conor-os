# The Paper loop

Paper Desktop plus its MCP server (34 tools as of September 2026; the docs page lists 20, trust `tools/list`). The server needs an open file; the file should be the active tab for font lookups and selection.

## Setting up the canvas

Once per product, in its own session. Go Pro first; the free tier's weekly call cap dies mid-write. Confirm the files (a Final file, an Explorations file and an Archive file; `final-and-handoff.md`, "Three kinds of Paper file") and make the pages: "🏁 Final" in the Final file for locked artboards only, and one "🚧 <Surface> · Explorations" per surface in the Explorations file (emoji, surface, middle dot, Explorations in title case). Check the typeface is available and compile DESIGN.md into Paper tokens (palette, then the semantic aliases). Then build the system artboard (swatches, type scale, a table row, a card, the controls, each chart form): the clone source for every surface, approved by the user before any screen exists. A new file starts with no tokens: copy Final's set into it with create_tokens before any designer draws. Paper drops var() inside font-family and box-shadow, so designers name the family and copy Final's shadow geometry literally. Start a round in a fresh Explorations file once the current one warns of Paper's size limit (`list_resources` shows it), before the round, not after a write fails; a comment status isn't a design write, so resolving threads is safe on a file past the limit. A surface designed in parts (a hero, its art, each look of sections) gets one page per part, "🚧 <Surface> · <Part>", under a divider in build order, opened the turn its first round starts, never stacked under an old part. Each page opens with a "Start here" card at its top-left (what the page holds, which row to review, where the record starts), with the row under review at the top.

## Dialect for `write_html`

- Inline styles only. Classes, style blocks, and pseudo-elements are dropped.
- Flex with padding and gap. No grid, no margin, no inline display, no tables.
- One style per text node. A bold word inside a sentence flattens; make it its own node.
- Every color, size, spacing, and radius is `var(--token)`. Ad hoc custom properties don't resolve; create tokens.
- `layer-name="Surface/Section/Element"` on every element. `data-paper-locked` for hand-tuned nodes. `<x-paper-clone node-id="…">` copies a proven node (a copy, not an instance).
- Icons are inline SVG with `var()` fills. Emoji and glyph icons are banned by the server.
- `color-mix()` fills are dropped without an error, though Paper's guide documents them. Give derived colors as literal hex (rgba for alpha) and pixel-check every export for the fill you meant; the user once judged a "well" that never rendered.
- Fonts: any Google Font or local font by name. Units: px for size and line height, em for letter spacing. `font-variant-numeric: tabular-nums` inline; check `ignoredStyles` on the response, since a dropped style is returned there.
- Artboard: 1440 wide, `height: fit-content` once content is in. Local images need `paper-asset:///absolute/path`.

## Tool sequences

- Prep, once per session: `get_guide("paper-mcp-instructions")`, `get_basic_info`, `get_tokens`. First session: `create_page("🏁 Final")` and, per surface, `create_page("🚧 <Surface> · Explorations")` (pass `pageId` on every artboard call; one page per surface keeps 20-plus artboards findable), `create_tokens` from DESIGN.md (palette, then semantic aliases), `get_font_family_info([family])`.
- Font check, every rev: `find_nodes(nodeId, filters: [{styleName: "font-family", styleValue: "system-ui*"}])` also matches the fallback fragment of a healthy stack ("IBM Plex Sans, system-ui, sans-serif" is what Paper writes), so a hit isn't a failure by itself; confirm with `get_computed_styles` that the first family is the product face. A stack that starts with system-ui is the failure. Batch `update_styles` with `fontFamily` to fix; `var(--font-sans)` on fontFamily is dropped silently.
- Create a screen: `create_artboard` → `write_html insert-children` per visual group → `duplicate_nodes` + `set_text_content` for repeated rows → `get_screenshot(scale 2)` → `update_styles` fixes → `update_styles(artboard, height fit-content)` → `finish_working_on_nodes([artboardId])`.
- Revise a node: `list_comment_threads(status open)` and `get_comment_thread` (node ID plus offset; the node is usually the content frame, so map the offset on the screenshot) → `get_tree_summary(nodeId, 2)` → `update_styles` / `set_text_content` / `move_nodes` / small `write_html replace` → `get_screenshot` → `set_comment_thread_status(resolved)` → `finish_working_on_nodes`.
- SVG charts: always `write_html replace` on the whole `<svg>`; replacing one `<text>` inside it yields an HTML Text node that doesn't render. Edit the master, then replace each instance with an `x-paper-clone` of it; find the instances with `find_nodes` on the SVG's width and height. Compute chart geometry in a script (density paths, dot stacks, scaled coordinates), then paste. SVG text is invisible to text search, so keep one master per chart and clone it into the siblings.
- Search the canvas by token, not by literal: `find_nodes` on `--radius-control` finds nodes; "3px" finds nothing.
- Duplicates: `duplicate_nodes` returns a `descendantIdMap`; the map's order isn't semantic, so `get_tree_summary` the subtree you're about to edit before `set_text_content`. Duplicating eight artboards at once returns 80KB+ and gets persisted to a file; extract the ids with a script and write a per-artboard table (artboard, then the handful of source ids you'll edit) before touching anything. Neighboring duplicates get look-alike ids and a fix landed on the wrong artboard once.
- Large SVG writes (a generated field over about 30KB): hand the write to a `worker` agent (Model: worker role) that reads the file and calls `write_html replace` on the old layer, then reports the new node id. The main context can't carry the string.
- A state that belongs to another surface's state (a detail page's error state is the list page's error artboard inside the detail page's chrome): `duplicate_nodes` that artboard onto this surface's page, then `write_html replace` its header, nav, and actions with `<x-paper-clone node-id="…">` of this surface's blocks, and edit the copy.
- Outside token edits show up as a changed `contentHash`; diff `get_tokens` against DESIGN.md and sync the file (ink-3 was darkened on the canvas once).
- Lock a surface: `move_nodes` the base and state artboards to the Final page root, `rename_nodes` to "Surface · state", `update_styles` left/top to lay them in a row, `export` the ideal state at 2x.
- Variant: `duplicate_nodes([{id: artboardId}])` → `rename_nodes` → edit the clone via `descendantIdMap`.
- Reorder children: one batched `move_nodes` of every child in final order; single before/after moves are unreliable in flex parents.
- Export: `export({[id]: [{format: "png", scale: "2x"}]})`, `get_jsx(id, "inline-styles")`, `get_computed_styles`, `get_tokens(format: "css")`.

## Etiquette

- Post the brief in chat before any mutation, and state that DESIGN.md overrides Paper's guide.
- Write small and often; large trees fail. One artboard per turn so a failed run leaves a clean canvas.
- Screenshot after every write. Look at it. Fix overflow, clipping, and alignment before saying ready.
- Measure spacing from the 2x export, not the node tree. Screenshot critics caught 24 + hairline + 24 reading as 32 to 35 that the node math missed.
- After a fix measured in pixels (a seam, an icon off its x-height, a 4px gap), screenshot the region, not the artboard: `get_screenshot` on the smallest node that holds the fix and the edge it's measured against, at scale 2, once before and once after. A 6px seam vanishes when a full artboard is downscaled to look at; a weight, word, or color change reads fine at full frame (from LangChain's design agent).
- Edit nodes; don't delete and rewrite. Verify a node's parent before any delete.
- Touch only nodes created this run. A commented artboard is frozen; revise on a duplicate beside it, placed at the page root, never parented into the commented artboard, where it would sit under the user's threads and read as an edit to the reviewed frame. Never delete a user-made node.
- Add-only on a page he's reviewing: never move, reposition or reparent existing artboards, including your own from earlier rounds. New work goes in a new row ("Don't move anything in Paper"). `create_artboard` sometimes ignores left/top; reposition only the artboards you just created.
- Paper caches an image by its path. After re-rendering, write to a new filename before re-pointing the fill, and set `backgroundSize: cover` again, because re-pointing resets it to auto.
- Pass explicit `pageId`; the active page can change under you. Watch `contentHash` for outside token edits.
- No bare node IDs in chat. Link frames instead: the page URL with the artboard's node parameter (`https://app.paper.design/file/<fileId>/<pageId>?node=<artboardId>`), one link per frame you mention, so "where am I looking" never comes up. Say "ready for review" and where.
- Resolve a thread only when the fix is on the canvas. A thread that asks for options stays open until the user picks; a thread that asks a question you answered in chat stays open until the answer is on the canvas or in the doc.
- Restart the agent session if tools vanish, parameters fail, or two corrections on the same thing fail; then the app.

## Review intake

Read open threads and the selection. For each: the pinned node and offset, the goal it names, the state, the element. Work it, screenshot, resolve, and report in chat as done, partial, or needs a call. Resolve a thread the moment it's addressed, and resolve threads a later pick made outdated too. Paper's MCP can't post replies, so say what changed (or "outdated, superseded by G2") in the round summary instead. At every round's start and at each surface's close, sweep all open threads in the file, so the open list only ever holds what still needs work. Designer agents can't spawn critics, so the lead runs the critic panel on their exports. If the user said "this" and nothing is selected, ask. Comments are the batched channel; selection plus chat is the quick single change; a hand edit is the user's right, and the agent reads it back on the next call.

## Cost

Free: 100 tool calls a week. One surface built properly is 30 to 50 calls. Pro: $20 a month (or $16 yearly), a million calls a week. Go Pro before the step.

- create_artboard ignores left/top; position with update_styles right after. Duplicating an artboard returns a descendantIdMap of a few thousand tokens; when a shell plus generated rows will do, have a `worker` (Model: worker role) build fresh from files instead of duplicating five times. Workers that write rows from /tmp files work well; give each one artboard, the exact node ids, and "do not fix anything".
- Generated files in /tmp vanish between sessions; keep the generator in the repo and rerun it.

## Tool parameter names (as of September 2026; the schema errors name them)

- `write_html(fileId, targetNodeId, mode, html)`; mode is `insert-children` or `replace`.
- `update_styles(fileId, updates: [{nodeIds: [...], styles: {...}}])`; `set_text_content(fileId, updates: [{nodeId, textContent}])`; `rename_nodes(fileId, updates: [{nodeId, name}])`.
- `move_nodes(fileId, moves: [{nodeId, parentId}])` for reparenting to a page root (`root_node_<pageId>`); `before` or `after` instead of `parentId` for ordering.
- `export(fileId, nodes: {nodeId: [{format: "png", scale: "2x"}]})` writes to the Downloads folder with the artboard name; move it into the repo. It writes about ten files per call and silently drops the rest (the result lists nothing), so export in batches of ten and check the folder.
- Large fix batches across many artboards split across `worker` agents by artboard ownership (Model: worker role), each told which artboards are theirs, that others are writing to the same page, and the SVG-text rule. Three workers cleared about thirty fixes on one Final page in one pass.
- `create_artboard(fileId, pageId, name, styles: {width, height, backgroundColor, left, top})`; left and top are honored here, so position at creation.
- `find_nodes` filters need a styleName or styleValue; it can't search by layer name.
- A `worker` agent (Model: worker role) for every row write over about 8KB: give them the file paths, the target ids, the mode, and "do not fix anything"; ask for ids back. One helper per artboard or per batch of replaces; a helper that also builds a second artboard needs the created ids from its own first write, which it can read from the response.
- A frame written with `write_html` straight into a page root ignores its inline `position`, `left` and `top` and lands in open canvas (a "Start here" card landed on top of a review frame). Set `left` and `top` with `update_styles` right after, and confirm with `get_node_info`.

# Rounds

How a round is handed off and shown: the planner's packet, the designer brief, the review page, and long pages. Read at the direction round, the polish loop and the ready review. The cases behind these rules are in `learnings.md`.

Contents: Medium before layout · The planner's packet · The designer brief · The review page · Long pages · The phone round

## Medium before layout

When a new element's medium isn't settled (a popover, a modal, an inline callout, a banner, a sheet, a toast), that's the first question: a research lane on how the best products deliver that moment and the evidence on each medium, then broad explorations of the media, before any round draws the element's layout. Other feedback on the same surfaces runs in parallel rather than waiting.

## The planner's packet

The planner runs on Fable in a fresh context, and left to explore it spends most of a run re-reading the project (a median of 72 turns and about 8M cached tokens per design-round run). So the lead writes everything it needs into one file, `mockups/hifi/packet-<surface>.md`, and hands over the path. The planner reads the packet and the files it names; the only searching it does is live inspiration.

```
Ask: direction round (first | a new direction the user asked for | next section pair), <surface>, <weight>
Brief: <path>  DESIGN.md: <path>  Preferences: <path>  Constraints: <path>
References: <path to references-<surface>.md>
The user's notes, verbatim: <the ideas-ask answer, the pick, each comment with the artboard it pins>
Critics so far: <per round, the medians and the findings, each marked applied, asked, or dropped>
Settled, don't reopen: <the user's calls and the lead's rulings, one line each>
Current exports: <one path per artboard and state>
Return: a diagnosis, the direction, the takes (two or more; one on Quick), the settled list, a finish checklist of at most ten lines a critic can score from stills, any token DESIGN.md lacks
```

Resume, don't respawn. For each later direction round on the surface, the lead sends the same planner only what changed since its last plan (the new notes, the new exports, the critics since). A new planner starts only when the old one is gone (a new session); it gets the full packet.

The lead rules on each plan before designers draw, in a rulings file they read first: a plan call that contradicts the user's brief or the issue's done criteria is overruled (one planner cut the pager the brief asked for), and a value the plan says the data lacks is cut from real data by the lead, never left for a designer to fill. Before the rulings file goes to the planner, the lead checks each claim it makes about Final (an artboard "exists", a button's label, a token's value) against the canvas and the tokens; one rulings file named a Final artboard that didn't exist, a button label and a text size, and the planner found all three false.

A placement the user described ("right after the last word") goes into DESIGN.md as the user said it. A plan that adds an edge case changing that placement ("alone under a list") is asked, not ruled, because the critics enforce the doc and a later round reverses it.

## The designer brief

Each designer gets the brief, DESIGN.md, its take from the planner's plan, and these rules:

- One take per artboard, on the surface's explorations page, by `paper-loop.md`'s etiquette.
- Keep every mark the app's own: never extend a series past its data, smooth it, or invent a continuation to fill a frame. The lead reads each generator diff for a new seed or constant.
- A state still must differ from rest: self-review compares every state still (hover, pressed, error) against the rest still and fails one that's identical.
- A generated mark (a pixel glyph, a small piece of the art) ships with its dark-theme render and its contrast on the dark page from its first draw, so a mark that vanishes in dark is a take's weak spot on the review page, not a surprise after the pick.
- Read every export before reporting, and walk the steer-yourself list in `brief-and-review.md`.
- The second theme and 768 are duplicates, not redraws: duplicate each finished artboard and recolor it to the other theme's values (find_nodes by each value), or refold the 1440 for 768; a fresh draw of the same screen costs several times the tokens and drifts. Moving a pick to Final copies across files with get_jsx and write_html (duplicate_nodes stays inside one file), then a pixel compare of each pair. The cheap path: the Paper MCP server is plain HTTP on 127.0.0.1 (port 29979 and path /mcp as of November 2026), so a worker's script pulls the source board's JSX, converts it to HTML and rebuilds it on the target one group per call, with nothing passing through the worker's context. 37 boards moved at 0 differing pixels in three parallel workers of about 100k tokens each. Inner layer names may arrive as Frames; nothing renders differently.

Before designers draw, a worker computes every chart's data with the app's own code into one data.json beside the round's briefs (building the history in the lead's own workspace when none exists), so both takes draw the same numbers and the build reads the same numbers. The data worker writes data.json in stages as each key lands, so designers can start early. When no real record holds the state a board needs (a lapsed account with both a pre-lapse record and activity since), the worker seeds a throwaway store with the app's own dev commands, under the loop's scratch, so the app's own code computes every number. The read-me and the lock comment say the scenario was seeded.

## The review page

The direction round and the ready review each go to the user on a page made for the review:

- One row per take, a label artboard at its left, the same state in the same column across rows, a caption over each column naming the moment it draws (who's looking, what they just did, what the board shows them), and a read-me artboard naming the calls; a column titled only by its surface's name left him unable to tell what the boards were doing.
- A row that carries no call (shared states drawn once, context for the takes) says "nothing to decide" on its label and in the ask, or he reads it as an ask.
- Each row starts about 200 below the tallest artboard of the row above, set by the lead once the row lands, never at a far fixed offset given to designers up front; a row parked 6,000 below went unseen.
- The chat message opens with the lead's pick in one line ("I'd pick B"), then the calls. Options use the same names as the labels on the canvas, never a second scheme invented for the ask.
- Name every artboard by page and artboard name beside its link, so a list of options in chat is never a set of mockups the user can't find.

## Long pages

A long page (a landing page, a long settings page) runs section by section. The planner proposes the section order first and the user okays it as text, with nothing drawn. Then each pass covers two adjacent sections through the whole loop (takes at 1440 and 390, the pick, the polish loop, 768 and the second theme, the ready review, Final), so a section that lands goes to Final while the next is drawn, and one weak section can't hold the page in rounds.

A document page whose sections share one frame (a method or legal page, where the layout question is the whole page's column, not each section's) runs as one page instead: round one draws two whole-page layouts, and the section order rides in the same ask as text, so one reply settles both.

A shared element is drawn once, in the first loop that needs it: when a surface embeds an element another surface or issue owns (a plan picker, a dialog shell), the first loop draws it as that owner's first artboards, and the owner's loop starts from them.

## The phone round

A 390 that isn't a straight fold of the picked desktop (a hero, a front door, art) gets its own small direction round with the user out of it, since the direction is already theirs.

- The planner frames 2 or 3 phone takes inside the locked direction, differing on how type and art share the tall frame and what the frame leads with. Art is rearranged from its own stamps and palette, never cropped.
- Workers draw them, three blind critics rank them, and the lead picks (Model: worker role for designers, critic role for critics).
- Then up to two worker rounds, each a fix pass plus a bar test (`critics.md`). If it's still short of the desktop's level, one more round drawn by a designer on the planner role's model, then a bar test. This last round runs even when the worker rounds stopped because the gap stopped closing. Passing the bar ends the round early. Either way the lead rules and the result goes to the ready review.

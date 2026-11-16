# Writing the brief

Loop step 2, for every issue. The brief file is the implementer's only memory, so what isn't in it doesn't exist for the build.

Pull the issue body over the Linear MCP into `.build/briefs/<KEY>.md` (gitignored). Open with `# <KEY>: <the Linear title>` (the PR script takes the PR title, and so the squash subject, from that line; a brief headed `# KEY (wave note)` merged as `KEY: KEY (...)`), then the labels and blocked-by list. Read the issue's comments too: notes earlier reviews left for this issue go into the implementer's prompt. Add the lead's notes: rulings, the DESIGN.md blocks the issue builds or changes, each by its file (when the project has a Blocks section), and for a surface built across issues, the seams it shares with other issues (a store, the router, the API fields it reads), so the issue review drives them. Rulings a later issue inherits go into that issue's brief as they're made.

- **Which design wins.** When the brief cites a design, it says which wins if the issue's text and the design disagree (Final by default; SKILL, Keeping the tracker true). A block drawn on two artboards at two widths gets one layout unless the user ruled otherwise, and the brief says which.
- **Scope to the ask.** What's in scope, in the user's words, and an out-of-scope line naming behavior that already existed on that surface unless the user asked for it, since a criterion like "must not shift the layout" otherwise pulls in a bug that predates the issue and costs a fix round.
- **Layout bugs** name every viewport that must keep working (the short and narrow ones, not only the sizes in the report) and the design they build back to, since a fix for one size has broken others; with no design to build back to, a layout bug gets a design pass first, not a quick code fix.
- **Tuning a prompt against a scored test set** is said outright: no prompt sentence may quote a test item's words or name the fields its expected answer uses, a held-out set is scored separately, and a test fails on a five-word overlap between the prompt and any test item, since a leaked item turns the score into lookup.
- **The failure contract:** what the module raises and what its callers catch, since module seams are where the milestone review finds its bugs.
- **New data down an existing path** names the path and why, since reusing a path built for one kind of item once sent a new kind through a step that rewrote it.
- **A live count** says "about", or has the worker recount.
- Write the Owns list as a plain `- Owns:` line; the scope script parses nothing else. Say whether the PR stands alone (loop step 6).

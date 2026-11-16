---
name: zero-to-one
description: >
  Orchestrates a product in two modes, Personal (research through build,
  for the user alone) and Go live (launch shaping through Quality, launch,
  and growth), calling the focused skill for each step and holding the gate
  between them. Use when the user says "new product", "zero to one", "spin
  up a product", "let's build something new", "start a product", "go live",
  "take it public", or asks where a product effort stands.
  Do NOT use to run a single step on its own (that step's skill, such as
  product-research or product-shaping) or for features inside an existing
  product with a team (product-shaping).
---

# Zero to one

The arc from idea to a product in use, and then to a public launch, in steps that each produce a document the next step reads. The order matters because each step is cheap to redo while the ones after it are expensive. Don't skip ahead: a tech doc without a shape, or code without a design, wastes the research.

## Two modes

zero-to-one runs in one of two modes, and the mode sets the steps, the gates, and the build's weight. Name the mode at the start, with your lean.

- **Personal** builds the product for the user alone. Every new product starts here: shaped and designed as if it were public, built behind a lock, in the product's first Linear project. It ends at the build's gate, with the user using it.
- **Go live** takes a working Personal v1 public: the front door, pricing, accounts, Quality, launch. It starts only when the user says so, the same day or weeks later; the timing is theirs, so never prompt for it on a schedule or file a ticket for it. Its own Linear project is created when its step 1 opens, and that step reads Personal's closing handoff, the Personal project and build's improvements project (what the user punted), the product doc, and the non-goals Personal marked "(Go live)".
- **Go live sits on a working v1.** Asked to go public mid-build, finish Personal's remaining milestones first (or drop the ones the user cuts), then open Go live, the same day if they want. Asked to skip Personal entirely, say what it costs (the build's first real user is the one who knows what to fix) and lean toward Personal; if the user still wants it, run Personal's steps with Go live straight after, no gap.

**One step per agent.** Each step runs in its own session: the session opens on the step, finishes it through its gate and the skill pause, then writes the handoff and stops; a fresh session with a clean context window takes the next step. Don't roll a second step into the same window. The orchestrator's state lives in one file on the project's `main`, `docs/zero-to-one.md`, with a pointer in the project's memory directory (never one worktree's `.context`, since the next session may open in another worktree). It holds the mode, every step closed with its date, outputs, and where they live, the decisions made at each gate, and the current handoff: what the next step needs first, ending with a copyable opening prompt for the next session. The new session opens with the progress map, counted against the mode's own steps ("Personal, step 6 of 6"). A step that runs as several sessions by design (build's one lead per milestone) hands off the same way inside the step.

**Personal's closing handoff** is written at its last step's gate and has no opening prompt, since Go live may be weeks off. It records where the product runs and what locks it, where the user's data lives and the owner ID its rows carry, the plan's Public later section, the "(Go live)" non-goals, whether Branding ran, and what the user noticed in use.

## Personal steps

1. Research. Skill: product-research. Model: lanes run on the researcher role; the chat stays on the main model. Output: a synthesis with decisions for shaping. Gate: the user has read the synthesis and made the decisions it handed them.
2. Shaping. Skill: product-shaping in its Personal mode, writing with product-doc. Shape it as a public product (who it's for, why it wins, the rivals), since that shapes what gets built; accounts, pricing, marketing, and Success Metrics wait for Go live. Output: a product doc with why, hypothesis, goals and non-goals, overall shape, open questions, checked by a cold read (paraphrase, premortem, design readiness) before the user's pass. Gate: the user has read the doc and it's aligned.
3. Design. Skill: design-shaping, which calls wireframe-explorations for the lo-fi options and hifi-design's loop (the same one build's Design Needed issues run) for the hi-fi pass on the Paper canvas, the prototype decision, and the build handoff. It designs the working screens at public quality; signed-out surfaces wait for Go live. Output: converged designs, a DESIGN.md, Solution Details in the product doc, and the tech toggle (what tech planning needs to know). Gate: hi-fi hit its done signal on every surface, the open-questions pass sorted every question, and design-shaping's final review ran with its calls made.
4. Branding. Skill: brand-design, which calls product-naming for the name. A standard step the user can skip by saying so. It runs right after design, before any code: the plan treats the brand as a given, every milestone (the shared components first) is built on it once, and the repo, domain, and hosting carry the real name from the start. With no product running yet, its critic loop scores the hi-fi surfaces re-tokened on the canvas, and the first build milestone's light close checks the brand on the running product. Output: the Brand section of DESIGN.md, the new token values, and the repo-side brand work listed as owed, which tech planning files into the epic. Gate: the user signed off on the brand.
5. Tech planning. Skill: tech-planning. Model: the planner role drafts and the critic role fills the panel. The plan carries its Public later section, the seams that keep Go live from being a rewrite. Output: a tech plan page linked from the product doc, the product doc's open questions all resolved, parked, or named in a milestone, and the epic as a Linear project with a brief in every issue. Gate: the user has reviewed the decisions and the epic is filed.
6. Build. Skill: build, which calls pr-review. Model: the main chat is the lead; implementers and reviewers run as `worker` agents. It runs at pre-launch weight throughout, behind the lock in build's `references/hosting-setup.md` once the product is hosted. Each milestone's light close is Personal's quality work; there's no named Quality step until Go live. Output: every milestone on `main`, its ledger, the skill pause run. Gate: every milestone has landed, its light close ran, and the end-of-run skill pause ran.

product-naming also runs on its own whenever a product needs a name, at any step.

## Go live steps

1. Launch shaping. Skill: product-shaping in its Launch shaping mode, writing with product-doc. It reads Personal's closing handoff, the "(Go live)" non-goals, and what real use showed, and shapes the front door, pricing and paywall, accounts and sign-in, legal pages, and the Success Metrics. Output: the launch shape in the product doc, cold-read like Personal's, and a Design Needed issue in the Go live project for each surface it splits off. Gate: the user has read it and it's aligned.
2. Design. Skill: design-shaping, which extends the brand to the public surfaces (the front door, emails, the OG card); when Personal skipped Branding, offer brand-design in its own session first. design-shaping designs and closes the Design Needed issues for the signed-out surfaces, the paywall, and the account flows. The front door runs through landing-page: when the signed-out app is the front door, from its Design Needed issue in the build milestone that ships the signed-out app; a separate marketing site, in its own session after the end-to-end review's gate and before launch kit, so its hero shows the verified product. Output: designs as Personal's Design step. Gate: as Personal's Design step, for the surfaces design-shaping owns. The page's own output and gate (landing-page's) close where the page runs, and neither holds this step.
3. Tech planning. Skill: tech-planning, starting from the code on `main` and the Personal plan's Public later section, scoped to the launch: accounts and the data move, billing, hosting, with build's `references/auth-setup.md` and `references/hosting-setup.md` named in the issues that need them. Output: a launch plan page and its epic in the Go live project, with a Quality milestone for the Quality step's issues. Gate: as Personal's Tech planning step.
4. Build. Skill: build, as Personal's Build step, over the launch milestones, at pre-launch weight until Quality. The lock stays on: accounts, billing, and the front door are built and tested behind it. Removing it is the epic's last issue, a one-way door that waits through Quality and the end-to-end review. Gate: as Personal's Build step, with only the lock issue and the Quality milestone open.
5. Quality. Skills: build's hardening close and break-it, side by side on one pinned sha, over the whole product, Personal's milestones included, on the branded product. The hardening close runs the production checks once (build's `references/close.md`) and flips the build to full weight for everything after. Model: break-it's surface checks run on the worker role. Output: the close issue, break-it's report, then every fix on one ticket, shipped as one PR, with the fixture kept as the regression test. Gate: the hardening close issue merged, every break fixed or decided, and the break-it PR up.
6. End-to-end review. The last review, and a wider version of design-shaping's final review; read `references/end-to-end-review.md` for its lanes. Model: worker role. Output: one merged list sorted into fixes and calls. Gate: the user has made every call and the fixes are in. Then a build session runs the lock issue on the user's yes, and a signed-out check confirms what's public and what still refuses.
7. Launch kit. Optional. Skill: launch-kit, after the front door and the brand, since it says nothing they don't. Output: the master video, its derivatives, the copy, and a ship list in launch-day order. Gate: the user watched it with sound and said yes.
8. Growth strategy. Optional. Skill: growth-strategy, once the product is live or close to it. Model: researcher role for its rival teardowns. Output: GROWTH.md beside DESIGN.md, attribution and metrics tracked or filed as build issues, and a brief for every technique whose skill doesn't exist yet. Gate: the user agreed the techniques and the first action of each is scheduled.

## At every step

- Open with a progress map: the mode, which step, what's done, what's next. Answer "where are we" the same way, numbered against the mode's steps and then the step's own loop, so the answer says "Go live, step 5 of 8" and not a paragraph.
- Self-learning is the point of the skills, and it has two halves. Before every step and every surface, read the skill's preferences and constraints end to end, plus whatever else that skill names for that step (hifi-design reads its failed-prompts at the pause), and list the rules that apply to what's about to be built; a rule the agent doesn't read before it acts isn't a rule. After every comment, correction, or pick, ask one question: does this generalize past the thing in front of us? If it does (a rule about cards, a way the user wants asks framed, a sort they'd choose again, a tool that failed), write it into the skill in the same turn as the fix: a rule into constraints, a pick into preferences, a process change into the SKILL body, a bad first pass into failed-prompts. Don't wait for the pause; the pause is the sweep for what the turn-by-turn habit missed. A comment that says "we covered this before" or "why wasn't this learned" is the loud case of the same defect: trace where the rule lived, why the step didn't read it, and fix the reading step, not just the rule.
- Every recommendation comes with a runner-up and the reason each is where it is. A strip of options without a lean is a gallery, and the user has to ask what the decision is. The exception is a lo-fi explorations round, which goes out with no lean until the user has reacted (wireframe-explorations).
- Research best practices for the step before doing it the first time. The step's skill starts as that research plus what actually happened.
- Run the skill pause (authoring-skills' Closing a skill update) on the step's skill when the step's output is accepted: what worked, what didn't, what the skill should say next time. Bookmark anything the user flags mid-step for it.
- How we work lives in the personal skills repo and only there: process, tracker lifecycle, the design loop, critics, review habits, communication. The project's repo, CLAUDE.md, and memory hold its facts (decisions, IDs, data, picks, state). When the user corrects how we work or picks a preference, edit the owning skill in the same turn and push it; a project memory or a ledger's "For the skill" list can point at the skill or stage a lesson until the pause, but it isn't the home. Unsure? Ask whether the rule would hold on a different project.
- Every step closes the same way: the full output in chat, the user's review, their yes to push it to the docs, their yes to move on, and the handoff to a fresh session (One step per agent). Research lanes are previewed before they launch. Open Questions in the product doc are refreshed at every step close.
- Push the project branch and open a PR at every step close, not only at the end. After a merge, check that `git log origin/main..<branch>` is empty, since twice a PR was merged before the step's last commits landed on it.

## How the skills fit together

- Our skills own the process and are generic loops (frame, research, explore, make, critique, hand back); a product's hero or chart is one instance. Installed third-party skills (impeccable, review-animations, an a11y checker) are judges, called by our process skills at a named step, never ad hoc. Installing five judges captures nothing about how a visual got good; the loop does.
- External skills the user likes come in as reference files the owning process skill reads at its step, not as vendored skills, so the loop stays ours and the technique rides inside it.
- Optional skills (visual-assets, motion-design, landing-page, launch-kit) are called from the process skill that owns the step and named in this orchestrator, so a reader can see the whole arc from here. When a called skill runs, report which of its steps ran and which were skipped; the user asks "did we run the full skill?" when it was partial.
- Names in skill text are the ones that landed with the user. "Front door versus working screen" worked; "selling versus serving" didn't. When a term doesn't land, rename it in the skill the same day.
- Say which kind of thing you mean: an installed skill, an MCP server, or one of our skills. They're different objects and "what to install" means all three.

## Working with the user

- **Cost decisions at launch:** frame each with the free or cheapest option first and the trigger that makes paying necessary, usually the first paying customer. Default to deferring spend to that trigger, and recommend the fastest path while naming what it gives up (Conor: "start lightweight and without paying much, and can make this thing more real over time").

- Interviews go one question at a time, each with the agent's assumed answer so a reply can be "yes", then one summary of all the answers for a yes. A batch of five is harder to reason about.
- Try one first when they say so; a single probe calibrates the brief. Then get every idea on the table before judging.
- Give your pick when asked, after they've had their first read. Preview research lanes and get a go unless they've already said kick it off.
- Research reports are saved in the repo the same day, no yes needed, and Notion gets only the product doc's structural decisions (product-research owns the rule); the show-then-push gate is for the product doc.
- When the user asks whether a skill ran, answer per step: which ran, which were skipped or reused, and what happens next to close the gap. Never claim a loop ran because its output exists.
- Name the audience a surface must perform for before briefing it.
- Name anti-references, not just references. "Not this" fixes a direction faster than ten examples of "like this".
- A cheap base layer can scaffold a crafted one: a sourced icon, then construct on top; a generated video, then draw over it. Start from the cheap layer, spend on the crafted one.
- Verify by looking at the output, several times, not by trusting the generator. A screenshot after every write, a node check on fonts, a diff of every number against the rows.
- Spend tokens where the quality comes from (the research lane, the generated field, the critics) and watch the budget everywhere else, though a free tier that dies mid-write (Paper's weekly call cap) costs more than the paid plan.
- Critic rounds are capped and stop at a bar the owning skill sets; user rounds aren't. The user's done signal ends a surface, a critic's never does.
- When you overrule a word or a call the user asked for, say so in the next summary with the reason. Never apply it silently.
- End every design round with one summary: each pick to make with a recommendation and its runner-up (none on a lo-fi round, per the exception above), where each option sits, and what's now locked. The user asks for it every round when it's missing.
- Check state before asking or reporting. The PR may already be merged, a connector may still be loading. Verify, then say what's true.

## Where things live

The project decides. Ask once where docs go (Notion, the repo, both) and put every step's output there. Gate decisions go in `docs/zero-to-one.md` (One step per agent).

The steps are the reminder. A step this skill already sequences (Quality, the end-to-end review, Go live itself) never gets its own tracker ticket; the tracker holds work to do, and the next step comes from here.

## Checklist

- The mode was named at the start, and Go live started only on the user's word, in its own Linear project, from Personal's closing handoff.
- No step started before the prior step's gate, and each step ran in its own session with a handoff.
- Personal shaped the product as public, with accounts, pricing, and marketing as non-goals marked for Go live, and its tech plan named the Public later seams.
- Branding ran after design and before tech planning, unless the user skipped it.
- The lock stayed on until after the end-to-end review, and came off on the user's yes.
- Quality ran in Go live over the whole product: build's hardening close with its close issue merged, and break-it with every break fixed or decided and the fixture kept.
- The end-to-end review ran after Quality and its calls were made.
- The front door, launch kit, and growth strategy each ran or were skipped by the user's call.
- Each step's output exists as a document, not just a conversation.
- The skill pause ran and the step's skill was updated.
- The progress map was current when the user asked.
- Every called skill's run was reported step by step, with skips named.

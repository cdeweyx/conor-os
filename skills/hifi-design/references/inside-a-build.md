# Inside a build

Read when a Design Needed issue in a build milestone calls the hi-fi loop, before the exploration brief. The loop's steps and gates are the same as SKILL.md's; this is what changes when it runs inside a milestone. The dated cases are in `learnings.md`.

- **It runs in chat, not as a background pass.** Post the exploration brief (one aesthetic sentence and assumption per direction) and start drawing in the same turn unless the user asked to approve it first.
- **Say where things are.** A brief that waits on a yes says in its first line that nothing is drawn yet. Name every artboard by page and artboard name (Paper has no reliable deep link), because a list of options in chat reads as mockups the user then can't find.
- **Two designer agents, resumed across rounds** so they keep their canvas context (Model: worker role), one direction per artboard. Read every export before it's shown, and walk the steer-yourself checklist in `brief-and-review.md` before each round.
- **Don't converge early.** Explore three or four directions per round; after a few cycles bring one or two finished candidates, each with its collapsed and expanded states.
- **Critics are the lead's.** Three screenshot-only critics per round, run by the lead, since designer agents can't spawn them.
- **Once the user picks, finish without stopping:** the Final page (`final-and-handoff.md`), the spec, and the build follow-up issue.
- **Feedback on a built surface gets one question before any fix:** does it change a constraint (a rule, a token, a pattern every surface shares)? If it does, change the rule and carry it everywhere. If it's a minor one-off, log it to `docs/build/papercuts.md` (surface, what, the Final node) and let it batch into a polish pass, since spot fixes one at a time drift the surfaces apart.

# Filling in Solution Details

Solution Details is the behavioral spec: what the product does in every state an engineer would ask about in design review. It's stubbed at shaping time and filled one requirement at a time once the shape is locked. This is how to break a requirement out.

## The loop, per requirement

1. **The PM's read first.** Ask what this should feel like when it works and what pieces they see, before offering your decomposition. Leading with your framing means shaping your guess, not their intent.
2. **Verify before asserting.** Never claim what a screen does today without having seen it (code, analytics, live app). Propose specific checks as questions and wait for opt-in. Research nobody agreed to is worse than no research.
3. **Research when the problem is solved elsewhere.** Scheduling, connector setup, error states: mature products already made these mistakes. Sweep the comparables for the table-stakes checklist, the divergences worth stealing, and the documented user complaints (the map of what not to build). Bring receipts, in short interim notes, then synthesize.
4. **Shape in conversation.** For each genuinely contested call, bring two or three meaningfully different options with a recommendation you defend. For everything else, make the call and let them override. When the user decides, it's decided; stop presenting it as open. When they cut something, it goes to the future list, not into an argument.

## The breakout format

- **Sub-topics named by artifact or behavior**, never by philosophy. "The status pill," "Dismissal behavior," "Send button states." Bad: "Component architecture," "Database schema." If the title needs the body to be understood, rename it.
- **Spec bullets under each**: states, triggers, fallbacks, and edge cases concrete enough that design knows what to draw and eng knows what to build. "User is on step 2, hits Preview, edits a line item. The preview closes. Once they confirm the total, the Send dialog appears."
- **Note what already exists** when you found it, so nobody re-scopes a solved problem.
- **Never present today's behavior as new work.** If the point is new states on an existing control, spec the states.
- **Never include another requirement's scope**, even when related. Note the handoff instead ("payment reminders live in the Reminders requirement").
- **No problem / opportunity preamble and no wrapping "Solutions" header.** The requirement's one-liner already frames it.
- **Open Questions** for the breakout, numbered: bold question plus one line on why it matters. Answers land as indented "your initials (date):" sub-bullets, and a resolved question moves to the Resolved toggle at the top of Open Questions with its number kept; questions are never deleted or renumbered.
- **Match the weight to the requirement.** Some deserve five sub-topics and mockups; some are a punch list for eng; some are a thin pointer because other breakouts absorbed them.

## Mockups: design to decide

- Mock the surfaces where the shape is visual and contested. Skip ones covered by an existing mock or trivially derivable.
- Riff on copy in chat before designing when the words are the contested part. Placeholder verbiage anchors the wrong thing.
- When a call is genuinely open, mock both options so the difference is visible, and have a preference ready.
- Idea-level fidelity in the product's design language (pull real tokens first). Show elements in their launch context; a floating widget with no anchor reads as noise.

## Running habits

- **Keep a future list.** Deferred items collect in one place for the end, never as "Later" sections scattered through breakouts.
- **Plain words everywhere.** Translate jargon into what the user experiences.
- **Short conversational turns.** Interim research notes are a few bullets. Save length for the breakout itself.
- **Don't write to the doc until told.** Present in chat, iterate, wait for the word. Then verify the write landed.

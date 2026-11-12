# Example product doc

A complete, focused doc for a small-to-medium initiative. Generic product (a browser-based editor with an AI assistant), realistic shape. Use it as a calibration for tone, density, and section weight, not as a template to fill.

---

# Help new users reach a first useful result without reading docs

# Why this? Why now?

- New users land in a blank editor with seven entry points and no guidance. In [session replays](#) from the last 30 days, roughly a third sat idle for over a minute before their first action, and most of those never saved anything.
- The AI assistant is the fastest path to a first result, but it's hidden behind an icon nobody clicks. Only [12% of new users](#) open it in session one, and those who do are twice as likely to come back in week one.
- We're about to run a paid acquisition test in Q4. Every user we pay for and lose in the first two minutes is money spent on nothing. Fixing this before the test is the difference between learning something and learning nothing.

**Hypothesis:** If we route new users into the AI assistant with a pre-filled starter prompt, then more of them will save a first artifact in session one, because the blank-canvas decision is the step where they stall.

# Goals

1. Increase the share of new users who save a first artifact in session one.
2. Make the AI assistant the default first action for new users, not a discovery.
3. Learn which starter prompts convert, so the set can improve without a redesign.

# Non-goals

- Not building a multi-step product tour. Things are shifting soon and a tour would be rebuilt within a quarter.
- Not changing the experience for returning users. They've already found their path.
- Not redesigning the assistant panel itself. This is about the entry, not the tool.

# Success Metrics

- **Outcome:** Are more new users saving a first artifact in session one? (This is the activation metric we already track weekly.)
- **Discovery:** Are new users opening the assistant in session one at a higher rate?
- **Adoption:** Do users who start through the assistant come back and use it again in week one?
- **Guardrail:** Does routing into the assistant reduce the share of new users who try manual editing at all? We want a first result, not a dependency.

# Overall Shape

New users skip the blank canvas and land directly in the assistant with a prompt ready to send.

1. **Assistant-first landing.** On first visit, the assistant panel is open and focused. The canvas is visible behind it so the user knows where the result will go.
2. **Starter prompt, pre-filled.** The input contains a complete example prompt drawn from a rotating set of five. The user can send it as-is, edit it, or clear it. One sentence above it: "Describe what you want, or try this one."
3. **Result lands with a nudge to save.** Once the first result renders, the save affordance pulses once. No modal.
4. **Rotating prompt set.** Each new user gets one of five prompts, assigned at random. Ships as its own milestone; v1 can use a single prompt with the data model supporting five.

Prerequisites: none that aren't already shipped. Assistant panel state persistence is live.

# Solution Details

...

# Analytics

| Event | Trigger | Properties | Notes |
|---|---|---|---|
| Assistant Starter Shown | Panel opens on first visit with a pre-filled prompt | `prompt_id` | One per user. |
| Assistant Starter Submitted | User sends the prompt | `prompt_id`, `edited: [true, false]` | `edited` distinguishes as-is sends from rewrites. |
| Assistant Starter Cleared | User clears the input without sending | `prompt_id` | Signals the prompt was wrong for them. |

# Open Questions

1. **Do we show the assistant-first landing to users who arrived from a template link?** They already have intent. Probably not, but it changes the routing logic.
2. **Does the pre-filled prompt read as a placeholder or as text they wrote?** If it looks like placeholder text, people will type over it. Needs a design decision on styling.
3. **What happens if the first result fails to render?** The failure path is where we'd lose someone who was one click from success.

---

# Appendix

▸ **Session replay evidence** (collapsed: bucket sizes, example session links, the idle-time distribution)

▸ **Prior shape: guided tour** (collapsed: the four-step tour we considered and why we dropped it in favor of a single entry change)

▸ **Analysis ideas for later** (collapsed: prompt-level conversion comparison, week-one retention by entry path)

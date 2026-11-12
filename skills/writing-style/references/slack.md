# Writing for Slack

Formatting rules that bite in Slack, plus how recaps and shares should read. Everything in SKILL.md still applies.

## Formatting

- **Slack collapses single newlines between non-list text.** Put a blank line between each standalone line in a header block (title, recording link, doc link), or Slack runs them into one paragraph.
- **Bold with markdown `**bold**`**, not Slack mrkdwn `*bold*`.
- **Bullet character depends on nesting.** Flat lists use `•`. If the message has any sub-bullets, switch the whole message to `-` with sub-bullets as 4 spaces plus `-`. The literal `◦` renders tiny and the indent gets ignored.
- **One blank line between sections.** Never the braille blank character (⠀). Don't double-space.
- **No italics.**
- **No tildes for approximate values.** `~` triggers strikethrough. Say "about," "roughly," or suffix with "+" ("500+ lines").
- **Title line:** an emoji prefix (📝 for recaps) and bold. Blank line, then straight into the first section.

## Recaps and shares

- **Organize by topic, not chronology.** Group related discussion even if it was spread across the meeting.
- **Headers name the topic, not its status or priority.** "Reliability," not "Reliability (P0)." "Bring-your-own-font," not "Bring-your-own-font on hold." Status lives in the bullets so it can change without renaming the section.
- **2 to 3 bullets per section** for internal recaps. One-bullet sections are weak: fold them into another section or cut.
- **Action items go last, if at all.** For recurring team syncs, skip them by default: everyone was in the room. Include when the meeting produced new assignments worth surfacing.
- **Plain first names.** `<@USER_ID>` mentions only when the user explicitly wants people pinged. Pinging people about tasks they already own is noise.
- **No first person.** "We should," or cut the personal follow-up.
- **Don't carry unverified numbers from transcripts.** Metrics said aloud in a call are often wrong or stale. Make the qualitative point and include a number only if the user confirms it.
- **Customer call shares are verbose, internal recaps are compressed.** A customer call share mirrors the cleaned notes and has no action items; it's for visibility, not task assignment.
- **No filler.** No "the team discussed..." or "it was noted that..."

## Process

- Draft in chat and iterate there. Expect several rounds of edits; that's normal, not a signal to hurry.
- Post as Conor, not a bot. Recaps and shares should feel personal.
- Preview in a private channel before any team or public channel when the project has one, since Slack renders differently from the chat draft.
- Confirm with the channel name after posting.

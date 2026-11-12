---
name: meeting-notes
description: >
  Conor's preferences for internal meeting notes, recaps, and summaries:
  what to pull from, how to structure them, and how they should read.
  Use when writing up an internal meeting from a transcript, AI notetaker
  notes, or pasted notes, or when the user says "write up this meeting",
  "meeting notes", "meeting recap", or "summarize this meeting". Do NOT
  use for customer interviews or user research calls (use
  research-notes). Do NOT use to interpret a call (use call-debrief).
---

# Meeting notes

How Conor wants internal meeting notes written. Where they get saved, which database, which properties, and whether they also go to Slack are defined by the project. This skill is the format and the judgment.

## Sources

Use everything available and synthesize across them; don't reformat one.

- **The user's own notes** (pad notes, an agenda doc) carry the most signal about what mattered. When the user supplies an agenda with sections, those sections are the source of truth for structure, and their names carry into the notes. Topics the agenda doesn't cover stay out even if the transcript discussed them, unless the user asks.
- **The transcript** fills in detail and exact wording.
- **An AI notetaker's summary** is good for catching what the transcript buries.

If no meeting is specified and a meeting source is connected, list recent meetings and ask which one. Don't ask the user to paste when it's already available.

## Format

Full-detail notes, structured so someone who missed the meeting gets the whole picture. Title, date, and attendees live in metadata or properties, not in the body; the body starts with the first section.

```
## [Thematic section]
- Point with enough context to stand alone
  - Supporting detail, quote, or example
- Another point

## [Another thematic section]
- ...

## Action items and next steps
- **[Owner]:** Deliverable, with a timeline if one was discussed

## Appendix
- Link to the recording or transcript
- Docs referenced in the meeting
```

- **Organize by topic, not chronology.** Group related discussion even when it was spread across the meeting.
- **3 to 6 sections.** Fewer is better. Headers name the topic, not its status or priority.
- **Sub-bullets are for supporting material**, not for continuing the parent thought.
- **Action items are always last before the appendix**, every item with a bolded owner. If the meeting produced no new assignments, skip the section rather than re-broadcasting what everyone already owns.
- **The appendix always includes the source link** when there is one.
- **Don't carry unverified numbers from the transcript.** Make the qualitative point; include a number only if the user confirms it.

## Voice

Apply the writing-style skill, notes register. Functional and scannable. No "I" in notes: say "we should," or cut the personal follow-up. No narrating ("the team discussed"). Contractions always, no filler.

## Before saving

Show the notes in chat first. Save only after the user's fine with them, unless the project says otherwise. If a Slack version is wanted, condense from the finished notes (not from the raw transcript) using the writing-style Slack reference, and show that draft too.

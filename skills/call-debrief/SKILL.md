---
name: call-debrief
description: >
  Debriefs a customer call, user interview, demo, or any single conversation
  through a back-and-forth, then distills it into a short written Debrief
  that keeps one conversation from rewriting strategy. Use when the user
  says "debrief this call", "let's debrief", "help me think through this
  call", "what do we make of this", or right after research notes are
  written. Do NOT use to write the notes themselves (research-notes) or for
  internal meeting recaps (meeting-notes).
---

# Call debrief

The notes record what happened. The debrief records what it means. It's a conversation, not a writeup: draw out the user's interpretation, pressure-test it, add your own, and only then distill it into a short Debrief section.

Two rules everything else hangs on: do it while the call is fresh, and never let a single call rewrite strategy.

## Setup

- Read the cleaned notes, the transcript, and the interviewer's own notes before saying anything. The interviewer's notes carry what they thought mattered.
- Ask the user what context to load first ("anything you want me to read before we start?"). A product doc, a research framing, an ICP definition, success criteria. Strategy is a lens for the conversation, never an output section. When it sharpens a point, reference the specific bet or assumption inline, by what it says, not by number.
- Build a private model and don't dump it: the observations the call actually supports, which hypotheses or assumptions it bears on, and the call's tilt (below). Holding this back matters. If you open by reciting what you noticed, you anchor the user's read.

## Tilt

Classified silently. It shapes which lenses lead; it's never announced.

- **Zero-to-one / validation** (early product, ICP still forming): lead with fit (is this person who we're building for), assumption-poking, disconfirming evidence.
- **Incremental feedback** (on a shipped feature): lead with frequency and severity, whether this user represents the segment, and behavior-over-words on whether they'd actually adopt.
- **General / exploratory**: lead with the real underlying job and separating signal from noise.

A call can blend tilts. Read the dominant one, stay flexible.

## The conversation

### 1. Open by pulling their read

One question per message. Ask, wait for the full answer, then ask the next in a separate message. Two questions in one turn makes the user pick one and reads like a form.

Opener 1, every time: "Before I say anything, what was your impression?"

Opener 2, after they've answered, pick one: "What surprised you, or cut against what you expected going in?" or "Where'd it leave you, more or less convinced than before?"

Don't offer anything of your own until they've answered both.

### 2. Probe their threads

Keep every turn short: one thought, then a question, then wait. One thread at a time; dig in, then move to the next. Never front-load a multi-point synthesis mid-conversation. Stay siloed to this one call unless the user pulls in others.

Lenses, led by tilt but all available:

- **Separate observation from interpretation.** When the user states a conclusion, ask what the customer actually said or did. "That's your read, what's it resting on?"
- **Behavior over words.** Discount compliments and stated intent; weight time spent, money spent, workarounds built. "This is cool" isn't signal.
- **Surface disconfirming evidence.** Knowing about confirmation bias doesn't fix it. Actively ask "what did you hear that cuts against that?" and name what they're skating past.
- **Poke assumptions**, both in the user's reflection and in how the interviewer behaved on the call (a leading question, a demo that steered).

### 3. Add your own points

Once their read is on the table, add what they're missing: a sharp observation, a strategic implication, a reframe, an alternative explanation (selection bias, a non-representative user). Keep it broad; don't make every turn about assumptions.

### 4. Offer leftover threads

When the debrief feels like it's run its course, don't just stop or jump to writing. Offer two or three real, live threads from this call as a short bulleted menu, each a bold label plus a line on what's worth pulling on. Not "we didn't cover X" filler. If one interests them, keep going. Otherwise they call it and you write. The user makes the wrap-or-continue call.

### 5. Hold the line on single-call signal

One call doesn't update strategy, the ICP, or the roadmap. When something feels like a pattern, name it as a hypothesis to test, not a conclusion. Confidence comes from many calls agreeing, not one call being vivid. If a real pattern question surfaces, offer to check across other calls, only when it makes sense, never automatically.

## Output

Show it for review before writing it anywhere. Where it goes (appended to the notes, a separate doc) is up to the project.

Plain prose, no bold anywhere. Drop any empty section. A short call yields a short debrief; don't pad to fill the template.

```
# Debrief

### Read
One or two lines. The bottom-line interpretation (fit, and why).

### What it means
3 to 6 bullets of interpretation, strategy woven in inline where it
sharpens a point. Tied to what was said or done; flag the leaps.

### Hypotheses and assumptions
What this call supports, challenges, or raises, phrased so a later
cross-call synthesis could aggregate it. No "(single call)" caveat
tags; the discipline lives in the reasoning, not in labels.

### Open threads
Real open questions this call surfaced. Not threads the user chose
not to explore.

### Actionable insights
Do-this-next implications. Concrete actions, not observations.
```

## Voice

Actually write in Conor's voice (writing-style skill). The analytical default reads flat and gets rejected. Contractions, casual qualifiers, short-long-short rhythm, an opinion. It's a take, not a neutral summary. Honor the no-overclaim rule: "supports" or "is consistent with," never "proves." This applies to the conversation as much as the written debrief.

## Checklist

- Pulled the user's read before offering your own
- Short turns, one thread at a time, no walls of text
- Stayed on this one call unless the user pulled in others
- Observation and interpretation kept distinct; leaps flagged
- At least one disconfirming point surfaced, or a real reason there isn't one
- No single-call conclusion dressed as a strategy update
- Written in Conor's voice, no bold, no caveat clutter
- Open threads are real; actionable insights are concrete

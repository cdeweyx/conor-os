# Story file

The one document every launch asset is cut from. Write it before anything moves, get the user's yes, then record the voice-over against it. Kiln's rules after two agent-made launch videos ([write-up](https://kiln.tech/blog/we_made_our_launch_video_in_claude_code), [videowright](https://github.com/scosman/videowright)): audio leads, one component per beat, a video style guide on top of the brand guide.

## Template

```markdown
# <Product> launch story

One point: <the landing page's idea sentence, verbatim or tightened>
Audience: <who, and what they already know>
Hero moment: <the five seconds where the product does the thing nobody else does>
Length: <45-90s>  Channels: <X, YouTube, PH, email, store>
Voice: <synthetic voice name and speed | captions only>

## Beats

| # | Start-end | Says (VO or caption) | Shows | Product state |
|---|---|---|---|---|
| 0 | 0.0-3.0 | <the problem or the hero moment, never the logo> | <first frame> | <fixture/state> |
| 1 | ... | <setup: the pain in the user's words, quoted from MESSAGE.md's Their words when it exists> | ... | ... |
| 2 | ... | <turn: the hero moment, full screen, real speed> | ... | ... |
| 3 | ... | <payoff: what they get, one number if there is one> | ... | ... |
| end | last 3-5s | <the one action, the URL> | mark, URL | - |

## Video style guide
- Type: <display and caption faces from DESIGN.md, caption size at 1080 wide>
- Color: <ground, ink, accent from DESIGN.md; what the accent marks>
- Motion: <the motion tokens; cut vs move rule; how UI enters>
- Sound: <music or none, level under VO, each cue (music hit, sound effect) and the transcript timestamp it lands on>

## Derivatives
- Clips: <beat -> clip, one feature each, under 10s>
- Stills: <three frames by timestamp, light and dark>
- PH gallery: <which frames, in order; image 1 is the thumbnail test>
- OG card: <frame or layout>
```

## Rules for the beats

- **The first three seconds carry it.** Open on the problem in the user's words or on the hero moment itself. Feeds autoplay muted, so the frame has to read without sound. The mark goes at the end.
- **Three beats.** Setup, turn, payoff. A fourth beat is usually a second point; cut it or make it its own clip.
- **The hero moment plays at real speed, full frame.** Speed-ups and cursor zooms around it are fine; the moment itself is the proof.
- **One component per beat.** Each beat is its own composition, so a re-cut moves a block, not a timeline.
- **Timing comes from the voice-over.** Transcribe the recorded VO with word timestamps (HyperFrames' `/media-use`, or faster-whisper with `word_timestamps=True`) and set each beat's start and end from them. Captions come from the same transcript.
- **Sound sits on the same timestamps.** Every music hit and sound effect lands on a transcript timestamp or a beat boundary, never placed by ear after the picture locks. With a track, measure its beats and cut against them. If the audio has no shape with your eyes closed, it isn't done.
- **The end card is the landing page's one action.** Same verb, same URL.

## A worked example

```markdown
One point: Your invoices, written from the hours you already tracked.
Audience: Freelancers who build invoices by hand from a timesheet.
Hero moment: A pasted timesheet becomes six finished invoices in under a second.
Length: 60s  Channels: X, YouTube, PH  Voice: Kokoro af_heart, 1.0x

| # | Start-end | Says | Shows | Product state |
| 0 | 0.0-3.2 | "Every month ends with an hour of invoicing." | A spreadsheet of hand-copied hours, a red cell | none (stock-free still) |
| 1 | 3.2-15.8 | "You paste the month's hours..." | The invoice screen, cursor pasting the timesheet | empty invoice |
| 2 | 15.8-38.0 | "...412 hours, six clients, in under a second." | Invoices filling in, full frame, real speed | fixture: march-timesheet |
| 3 | 38.0-54.5 | "Six invoices, ready to send. Back to work." | The invoice total, the one number held | same |
| end | 54.5-60.0 | "Try it free." | Mark, URL | - |
```

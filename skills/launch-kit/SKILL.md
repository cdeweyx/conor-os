---
name: launch-kit
description: >
  Makes the launch-day assets for a built product from one story and one
  render: the launch video, clips and stills cut from it, the Product Hunt
  gallery, the OG card, and the launch post, thread and email. Use when the
  user says "launch", "launch video", "demo video", "trailer", "product
  video", "announce it", "launch thread", "launch post", "Product Hunt",
  "launch day", "App Store screenshots", or when zero-to-one reaches its
  launch step. Do NOT use for the marketing page (landing-page), motion
  inside the product (motion-design), the brand or its reveal
  (brand-design), or a decorative visual on one surface (visual-assets).
---

# Launch kit

A landing page nobody visits isn't a launch. The best launches of 2025 and 2026 (Cursor 2.0, Linear Agent, the new Raycast, Kiln's agent-made video) share a shape: a short owned post with three crafted stills, a native video carrying the reach on X and YouTube, and every other asset cut from that same story. So this skill makes one story and one render, then derives everything else from it. Five assets from five briefs say five different things; one render can't.

Read `references/story.md` before step 4, `references/deliverables.md` before step 6, and `references/rubric.md` before the gate. Read `references/preferences.md` every run, before intake.

## Where it sits

zero-to-one's Go live launch kit step, optional, after the landing page and the brand, because it says nothing they don't. Inputs: the landing page's idea sentence and copy deck, the Brand section and motion tokens in DESIGN.md, and the running product. With no landing page, run landing-page's steps 1 to 5 first (intake through the approved copy deck), since the kit's one point and every claim come from them; with no Brand section or motion tokens, use DESIGN.md as it stands and say so in the report. It calls writing-style for every word, motion-design's review method and review-animations as judge, the `critic` role for the blind pass, and visual-assets only when a still needs a backdrop. HyperFrames' own skills (`npx hyperframes skills update` in the product repo) own the render mechanics; this skill owns the story, the order, and the bar.

## The steps

1. **Intake.** One question at a time, each with your assumed answer, then one summary for a yes: where it launches (X, Product Hunt, HN, YouTube, an email list, the App Store) and on what date; who it's for and what they already know; the one hero moment (the five seconds where the product does the thing nobody else does); voice-over or captions only; what's real to show (the running product, a fixture, nothing yet). Check each platform's current spec here, since sizes and lengths drift.

2. **Inventory.** Pull the idea sentence, the copy deck's claims and proof, the Brand section, and the motion tokens into one page. The kit's one point is the landing page's idea sentence. A claim that isn't in the deck goes into the deck first, with its proof and the user's yes, or it doesn't go in the kit; otherwise the kit invents a second message.

3. **Reference pass.** Five launch clips from the product's category, picked by views relative to the poster's followers rather than by brand size (a big account shows what an audience does; an outlier shows what the format does), annotated as technique text: what moves in the first three seconds, cut rhythm, how the UI enters, caption style, length, how it ends. One anti-reference. The build gets the text, not the clips. Galleries and engines are in design-sources. For X, `api.fxtwitter.com/status/<id>` returns a post's views and the author's follower count free; launch indexes that report reach per follower band do the same in bulk.

4. **Story file.** Before anything moves, write `launch/story.md` from the template in `references/story.md`: one point, one hero moment, three beats, the end card, 45 to 90 seconds. Then record the voice-over (synthetic by default, see preferences) and transcribe it with word timestamps; those timestamps set every beat's start and end. Audio leads because cutting picture before the voice exists was the failure that cost Kiln's first video a day. Captions-only videos still get a timed script read aloud once, so the pacing is a person's, not a guess. The user says yes to the story file and hears the voice-over before step 5.

5. **Build.** HyperFrames by default: it's HTML, so DESIGN.md's tokens and the landing page's CSS carry straight in. Remotion when the product is React and 3D or heavy captioning dominate. One composition per beat. The product appears as itself: captured from the running app with Playwright at the beat's exact state, or rebuilt as faux UI from a fixture using landing-page's product UI loop (`~/.claude/skills/landing-page/references/product-ui.md`) when a capture would be cramped or noisy. Never a fake feature. Captions burned in, since feeds autoplay muted. Render a contact sheet after every change and look at it before rendering video; stills cost milliseconds, a rendered second costs seconds.

6. **Derivatives.** From the same render, never a new brief: three to five clips under ten seconds, one feature each; three stills in light and dark; the Product Hunt gallery; the OG card, handed to landing-page's gate; the 9:16 cut if X or short-form video is a channel. Sizes and checks are in `references/deliverables.md`. For a phone app, the store screenshots and preview video come here too.

7. **Copy.** Through writing-style: the launch post (600 to 900 words, the three stills, a candid list of what's missing, as Raycast did), the X post that carries the video natively plus a short thread, the Product Hunt tagline and first comment, and the email if a list exists. Every claim traces to the copy deck. Write each body first and its opening line last: draft five openers in different shapes (callout, curiosity gap, proof, contrarian, number), gate each, keep the strongest. Every opening line (the post's, the X post's, the email subject) passes the hook gate, five yeses or a rewrite: it calls out the reader or opens a loop; you'd say it aloud to a friend; a stranger understands it; no insider words; it's concrete. Read the opening lines side by side: no two make the same claim, so a reader who saw one still has a reason to open the next. Every call to action in the post, the X post, and the email names who, what, when, and how ("Freelancers: send your first invoice free today at the link"); the video's end card keeps the landing page's one action, per `references/story.md`.

8. **Gate.** Scripts first, then eyes. `npx hyperframes lint` (or the Remotion equivalent) clean; an ffprobe and ebur128 check that duration, resolution, frame rate, audio stream, and loudness match `references/deliverables.md`; captions present on every spoken line. A gate that couldn't run is a failure, never a pass: fix the setup and rerun. Then a filmstrip: dense frames through every cut plus the first frame, the poster frame, and the end card, reviewed with motion-design's keyframe strip method, and review-animations on any motion code. Then two blind `critic` agents (Model: critic role) see only what `references/rubric.md` lists (the first three seconds as a strip, the thumbnail and gallery image one beside two competitors') and score against it. Take the median of the overall taste score, fix the top three findings, rescore, three rounds at most, stop at a 9 or under a point gained. Listen once with eyes closed: a cue that misses its timestamp, or audio with no shape on its own, goes back to step 5. The user watches the full video with sound and says yes; a critic never ends it.

9. **Ship.** The ship list in launch-day order: video uploaded natively to X and YouTube, the post live, the thread, Product Hunt, the email, then the stills to whoever's covering it. Report the one point, the length, the final scores, which steps ran and which were skipped, and what's still sample content.

## Skill pause

Run authoring-skills' Closing a skill update (the skill pause) at the end of every run. What goes where in this skill: a pick into `references/preferences.md`, a spec or tell into the reference that owns it, a process change into the steps. A rule that only exists because a renderer or a voice model is weak says so, and is re-tested and usually cut when the tool updates.

## Things that go wrong

- Five briefs. A trailer, a gallery, and a post written separately drift into three messages. Everything comes from the story file.
- Picture before audio. A cut timed by feel gets re-cut when the voice arrives; record first.
- The logo sting. Three seconds of brand before the product loses the feed. The hero moment or the problem opens; the mark closes.
- Feature tour. Six features in sixty seconds says nothing. One point, three beats.
- Fake product. A mocked feature or an impossible speed-up is caught in replies. Faux UI is allowed; faux capability isn't.
- Embedded video on the owned post. The post is text and stills; the video lives natively where it plays inline.
- Judging from the timeline. Critics and the user see rendered frames and the rendered file.

## Checklist

- Intake one question at a time, summarized for a yes; platform specs checked.
- The one point is the landing page's idea sentence; every claim traces to the copy deck.
- Product shown as itself (capture or faux UI from a fixture), captions burned in.
- Every derivative cut from the one render; sizes match `references/deliverables.md`.
- Lint and ffprobe gates pass; filmstrip reviewed; two blind critics, median logged, rounds capped.
- The user watched it with sound and said yes.
- Ship list walked in order; steps run and skipped reported.

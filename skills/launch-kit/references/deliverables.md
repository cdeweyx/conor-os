# Deliverables

Sizes and checks per asset, as of November 2026. Platforms change these; intake re-checks every channel the launch uses and updates this file when a value has moved.

| Asset | Spec | Check |
|---|---|---|
| Master video | 1920x1080, 30fps, H.264 + AAC, 45 to 90s, captions burned in, -14 LUFS integrated, true peak at or under -1 dBTP | ffprobe: resolution, fps, duration in range, one audio stream; `ffmpeg -i <file> -af ebur128=peak=true -f null -` reads -14 LUFS (within 1) and the peak |
| Vertical cut | 1080x1920, same render re-framed per beat, captions in the middle third (UI chrome covers the top and bottom), same loudness as the master | ffprobe and ebur128; a still at each beat start shows the product, not a crop of empty ground |
| Clips | 1920x1080 or 1080x1080, under 10s, one feature each, loops cleanly or ends on a held frame | ffprobe duration; first and last frame side by side |
| Stills | 2400 wide PNG, light and dark, three frames named by timestamp | open each at 100%; no motion blur, no half-faded element |
| Product Hunt gallery | 1270x760, three to six images, one feature each; image one is the thumbnail test | image one read at 240 wide: product and point still legible |
| Product Hunt thumbnail | 240x240, the mark or the hero moment, animated GIF allowed | read at real size beside two competitors' thumbnails |
| OG card | 1200x630 static | handed to landing-page; its `check.mjs` fetches `og:image` and asserts the size |
| X post | Native video upload, never a link to YouTube; text says the one point in one line | preview in a logged-in draft before launch day |
| Launch post | 600 to 900 words, three stills, a "what's missing" list, one link | writing-style pass; every claim traces to the copy deck |
| Email | Same copy deck, one action, inline styles, plain-text twin | send a test to two clients (Gmail, Apple Mail) |

## Phone apps

Only when the product ships to a store. Verify sizes against App Store Connect and the Play Console at intake; they change with each device generation.

| Asset | Spec (verify) | Notes |
|---|---|---|
| App Store screenshots | Largest iPhone size required (6.9", 1320x2868 portrait), iPad 13" if universal | One benefit per screen, three to five word caption, the real UI in a device frame or full-bleed |
| App preview video | 15 to 30s, device resolution, no hands, no non-app footage | Cut from the master's beats, re-framed |
| Play feature graphic | 1024x500 | The mark and one line; no screenshot collage |
| Play screenshots | 16:9 or 9:16, 320 to 3840px on each side | Same captions as iOS |

Tools seen but not yet run by us: fastlane `frameit`, appshot-cli, asc-screenshots. Run one on the first phone app and record the verdict here.

## Engines

- **[HyperFrames](https://github.com/heygen-com/hyperframes)** (Apache 2.0, HeyGen). HTML plus GSAP, deterministic frames, `npx hyperframes init / preview / render`, a linter, a catalog of about 450 blocks (`hyperframes add`), and its own agent skills (`npx hyperframes skills update`), with `/media-use` covering voice-over and transcripts. Default.
- **[Remotion](https://www.remotion.dev/docs/ai/skills)** (source-available; a company license above a small team size). React compositions, official agent skills (`npx skills add remotion-dev/skills`), strong captions, `@remotion/three` for 3D. Use when the product is React and 3D or captions dominate.
- **[videowright](https://github.com/scosman/videowright)** (MIT). Playwright plus ffmpeg, ElevenLabs word timestamps. Kiln's pipeline; worth reading for the audio-first loop, not needed as a dependency.
- **Voice**: Kokoro (local, free) by default; ElevenLabs when the voice has to carry the brand. Transcribe either with faster-whisper or `/media-use` for word timestamps and captions.
- **Encode and probe**: ffmpeg and ffprobe.

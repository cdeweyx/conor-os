# MESSAGE.md

Where the page's words come from: the buyer's own language, what the traffic already knows, how many times the market has heard the claim, and which claims the product can back. It lives in the product repo beside DESIGN.md, under two screens, and every later step reads it instead of asking the user to remember what buyers say.

## Sources

Pre-launch there are no customers, so the words come from public places. Label every item by what it's evidence for.

- **The product doc and DESIGN.md.** What the product is, what's true about it, its terms. Claim evidence only for what the product itself does.
- **Rival reviews.** G2 and Capterra (read by hand or in the user's browser, they block fetchers), App Store reviews (the public customer-reviews RSS feed), Chrome Web Store, and 3-star Amazon reviews for an adjacent book or gadget. Three stars is where the balanced complaints are.
- **Threads.** Hacker News through the Algolia API (`hn.algolia.com/api/v1/search?query=`). Reddit through arctic-shift or threads the user pastes, since reddit.com blocks fetchers. X through `scripts/xapi.py search` (key in `~/.config/xapi/twitterapi.env`) if a key exists, with a small `XAPI_BUDGET`, on phrases like "anyone else", "is there a tool that", "alternative to <rival>".
- **Rival claims.** `node ~/.claude/skills/growth-strategy/scripts/teardown.mjs hero <rival> --months 24` for each rival's headline by month, and the Meta Ad Library for ads running 60 days or more (a long-running ad is one that works). These set the sophistication stage.
- **After launch.** research-notes and call-debrief outputs. Re-run when the user asks or customer calls have come in since the file's date; their words outrank public sources.
- **A dated snapshot, not a living doc.** Nothing keeps it current between re-runs, so it costs no upkeep; say that when proposing it, since "another file to maintain" is the first objection.

## Evidence rules

- **Language evidence is not claim evidence.** A quote proves people say it and how often, never that it's true. "The export takes forever" supports an angle and a headline in their words; it never supports "3x faster exports". A number on the page comes from §6: the product, a benchmark, a fixture.
- **Five data points per theme.** A theme needs five independent data points before it counts as a pattern. Under five, its quotes stay in, marked "thin (n=3)" and the page goes on a stated assumption.
- **Independent means different people.** Five mentions from one account count as one. Note the skew of each place (HN is technical, Reddit threads skew frustrated, reviews skew to the extremes).
- **Quote, don't paraphrase.** Every phrase in §1, §2, and §7 is verbatim with its link and date. Never fill a gap from general market knowledge; an empty corpus is a finding, so say so and mark the sections thin.
- **The mechanism is the product's.** §5 explains how this product actually works. Never invent one because the market wants one.

## Awareness and sophistication

Schwartz, *Breakthrough Advertising*. Awareness decides where the headline starts; it's per channel, since a launch tweet and a pricing-page visit send different people. When several channels feed one page, the one expected to send the most visitors sets the headline.

| Level | The visitor | The first line starts at |
|---|---|---|
| Most aware | Knows the product, wants the deal | The product and the offer |
| Product-aware | Knows it, not sold | The product and what it does better |
| Solution-aware | Knows what they want, not that this exists | The desire, then the product as the way to it |
| Problem-aware | Feels the problem, knows no fix | The problem, in their words |
| Unaware | Doesn't know there's a problem | Identification with who they are; there's no formula, so say it's a guess |

Sophistication is how many times the market has heard the claim, read from the rival headlines. 1: first in market, say it plainly. 2: rivals say it too, so make it bigger and specific. 3: the claim is worn out, so say how it works (a mechanism). 4: rivals have mechanisms, so sharpen yours. 5: buyers believe none of it, so lead with who they are. Stage 3 or later means the page needs a mechanism section.

## Template

```markdown
# Message: <product>
Updated <date>. Sources: <n> items from <m> places. Stage: pre-launch | first customers

## 1. Who (one line) and the empathy map
Current day | Frustrations | Fears | Goals. Each cell: one quoted line, source link, date.

## 2. Their words
What this is evidence for: the words people use and whether a pain recurs. Not whether anything is true.
| Phrase (verbatim) | Theme: pain / outcome / objection / alternative tried | Source, date | Count |

## 3. Awareness of the traffic we'll get
Level per channel (launch tweet: problem-aware; AI answer: solution-aware; ...).
Headline rule: the first line starts at <product | desire | problem>.

## 4. Sophistication
| Rival | Headline | Since when | From (hero history, Ad Library) |
Stage: <1-5>. Mechanism needed: yes / no.

## 5. Mechanism
Most people believe X. It's wrong because Y. The answer is Z. (One sentence each; Y cites a source.)

## 6. Claims and limits
| Claim | Evidence (a number from the product, a benchmark, a fixture) | Allowed on the page? |
Claims we can't make yet, with what would unlock each.

## 7. Objections, typed
| Objection (verbatim) | Vehicle (does this kind of thing work) / internal (can I do it) / external (time, money, a boss) | Answer we have | Where it goes (FAQ, post, reply) |

## 8. Re-run log
| Date | Source added | What changed |
```

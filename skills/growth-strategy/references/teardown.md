# Teardown

Step 3 of growth-strategy in full. A teardown is a history, not a profile: it explains how a rival got where it is, in date order, from public evidence. Adapted from marketingskills' reverse-engineer-marketing (Corey Haines, MIT) and goose-skills' research-competitors rival pass (GooseWorks, MIT), cut to free sources and to a product that's still zero-to-one.

## Contents
- What free data can and can't say
- The lead's pass
- The rival brief (paste into each researcher)
- Reading ads honestly
- Common mistakes

## What free data can and can't say

| Evidence | Free source | Strength |
|---|---|---|
| Page families, content pushes by month | `teardown.mjs site`, `sitemap-growth`; sitemap `lastmod` | Strong |
| Signup, pricing, onboarding, every place a non-user meets the product | Page reads; Playwright where curl gets a challenge | Strong |
| Tools and pixels, with first month seen | `teardown.mjs stack` (Wayback), `dns`; BuiltWith free page | Bracketed: single-page apps archive as empty shells, so dates skew one to three months late |
| Pricing and headline changes by month | `teardown.mjs history`, `hero` | Strong |
| Subdomains by first certificate date (tools, programs, campaigns) | `teardown.mjs subdomains` | Strong |
| Consumer app field: who ranks for the category's keywords, and who's growing fast | `itunes.apple.com/search?term=<keyword>&entity=software&country=us` per keyword (rank order, rating count, release date); `itunes.apple.com/us/rss/topfreeapplications/limit=100/genre=<id>/json` for the genre chart (genre ids are on Apple's genre list; Health & Fitness is 6013). A young app with a big rating count is a fast grower | Strong for who ranks; growth is a proxy, labeled so. Keyword popularity and download estimates need a paid app-intelligence tool or a search ads account |
| Product loop exists, and roughly since when | Wayback CDX census of the user-content domain (`*.rival.app`), open three, read the badge | Proves and dates a loop; can't size it |
| Ads, start dates, days running | Google Ads Transparency Center, LinkedIn Ad Library, Meta Ad Library (needs the advertiser's page ID; keyword search is noise), all in Playwright without login | Strong except TikTok (blocked) |
| What they'll scale next | Ashby, Greenhouse, Lever public job board APIs (check the slug is the right company) | Strong, often the clearest read |
| Who talks about them | HN Algolia, YouTube search page, arctic-shift for Reddit (reddit.com JSON is blocked), X through twitterapi.io if a key exists | Strong |
| Which brands AI answers name | The model APIs with web search on, three runs, under a cent | Drifts; log prompt, model id, date |
| Monthly traffic curve, ranked keywords, referring-domain counts | Nothing free works (Similarweb free and Google Trends block, Tranco covers 42 days) | Not available. Use velocity proxies (sitemap `lastmod`, subdomain count, Reddit and YouTube volume) and label them proxies; skip lift math unless the user supplies a paid curve |

## The lead's pass

Run while the researchers work, once the rivals are agreed. Save everything to `growth/teardowns/<rival>/` with the pull date in each file so a re-run can diff.

```bash
T=<skill-dir>/scripts/teardown.mjs
node $T site rival.com --out growth/teardowns/rival/urls.csv
node $T stack rival.com --months 24
node $T history rival.com/pricing --months 24
node $T hero rival.com --months 24
node $T dns rival.com
node $T subdomains rival.com
node $T sitemap-growth rival.com
node $T ads "Rival" --domain rival.com      # library links to open in Playwright
```

Then, while the researchers run, the reads they usually can't do: the ad libraries in Playwright for every rival and for us, and the user-content census when the rival hosts what its users make. When they return, open the pages their "Needs the browser" lists name. Each dated finding becomes a row in `growth/teardowns/<rival>/moves.csv` (`date,channel,kind,move,reach,link,evidence`). A pixel's first month is a move marked Inferred, since a pixel shows a channel was possible, not that ads ran.

The AI-answer baseline: ten questions a buyer would ask ("best <category> for <buyer>", "<rival> alternatives", "how do I <job the product does>", and variants), each to two or three models with web search on, three runs each. Keep the set fixed in GROWTH.md, since re-runs and the AEO metric compare against it. Without an API key per model, run them by hand and log them the same way. Record brands named in order and pages cited. Ask the same questions for us. Comparison pages and "best X" lists are what get cited; note which lists name the rivals, since getting onto those lists is a play.

## The rival brief

Paste this into each `researcher` (Model: researcher role), filled in. About 12 searches and 12 page fetches; stop a dimension when two reads add nothing.

> You research one rival for one product, from public pages only: never log in, sign up, or contact anyone. Every fact carries its link and date inline and is marked Observed or Inferred. A page that needs a browser (ad libraries, X, LinkedIn, script-only pages) goes under "Needs the browser" with the exact URL, never "none found".
>
> Inputs: rival name and site; our product in two lines; the frame we compete in; the typical buyer for pricing ("a solo founder with one product"); company type; today's date; the rival's last snapshot, if any (report what changed).
>
> Get, in order:
> 1. News, last 90 days: raises, launches, pricing changes, layoffs, acquisitions.
> 2. Biggest launch: the demo broken into hook, setup, reveal, proof, call to action, labeled from video, transcript, or page text.
> 3. Founder and team posts: one or two people, their repeated claims and the numbers they share.
> 4. How a non-user meets the product: shared outputs, public pages, badges, invites, templates, integrations listings, referral or affiliate program and its reward.
> 5. Pricing: plans, unit, free tier or trial and how it ends, what the typical buyer pays a month.
> 6. Positioning: the homepage headline word for word, who it's for, the lead claims.
> 7. Buyers: one praise and one complaint, quoted, from two sources (review site, Reddit, app store). The praise is why customers stay; never skip it.
> 8. Hiring: open roles by team, and which channel the last 30 days of posts scale.
> 9. Who talks about them: top YouTube videos and threads by reach, labeled team, creator (paid if disclosed), user, or press.
> 10. Where we'd win and where we'd lose, each with how sure.
>
> Weight effort by type. B2B or dev tool: founder posts, docs, integrations, comparison pages, LinkedIn. Consumer app: app-store reviews and rank, TikTok and Instagram, onboarding and paywall. Return about 600 words in that order, then "Needs the browser", "Couldn't read" (source, why, what it would change), and a snapshot for next time: headline, entry price, open roles, active ad counts per library with what each counts, review count and rating, all dated.

## Reading ads honestly

Libraries show what runs, since when, and what it says. Never spend, results, or targeting.

- An ad running 60+ days probably isn't losing money. Discount always-on brand or retargeting ads and small advertisers who never turn anything off.
- Several near-identical variants started over several weeks is the strongest public signal: a winner being iterated.
- The same message across many rivals is table stakes, not a differentiator.
- Counts aren't comparable across libraries: Meta counts active now, Google counts everything shown in the page's date range. Label every count with what it counts.
- No ads found is Observed for that library, filter, and date, not proof they don't advertise.

## Common mistakes

| Mistake | Fix |
|---|---|
| Crediting the move right before a jump | Credit the cluster of moves within six weeks; name the funding, press, or category wave in the same months |
| A pixel means they run ads there | Inferred until the ad library shows ads |
| Describing an image from its caption | Open the file or mark it "not read" |
| Ranking posts across channels | Rank within one channel; under 20 settled posts, list them and call no pattern |
| Taking a founder's story as the timeline | Label it "reported" and check it against dated evidence |
| Copying a play that ran on their funding or audience | Put it on the skip list with that reason |
| Generic plays ("post more on LinkedIn") | Name the formula, the asset, the skill, and the metric |

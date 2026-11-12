# Tactics

The catalog step 5 scores from. Each entry: what it is, who it fits, the evidence, how much an agent can do, the first metric with a starting threshold, and the skill that runs it. Thresholds are starting bars to adjust per product, not benchmarks.

## Contents
- The default stack
- The catalog
- Skip by default
- Unbuilt skills

## The default stack

After step 5's product-side check (an activation or retention fix comes first when it fires), and for a solo builder with a live product, start from these and let the teardown argue you off them: a share loop in the product, AI-answer presence through comparison pages and the lists AI already cites, one launch across every directory, and founder posts. Consumer apps with a visual before-and-after swap in creator video, and iOS subscription apps with keyword demand add App Store search ads once download-to-paid holds. B2B with a reachable buyer adds warm outreach. None of the fastest growers of 2025 and 2026 led with SEO, ads, or sponsorships.

## The catalog

Hours are a starting estimate of the user's own time per week once it's running, for step 5's sum.

### Activation or retention fix
The change that gets signups to a first result, or brings them back: a shorter path to the first output, a better empty state, a reason to return.
- **Fits:** any product where fewer than about a third of signups reach a first result within a day, or the product doc's activation or retention goal is missed. It counts as one of the two or three.
- **Evidence:** traffic into a leaking funnel is wasted; every suite read puts product-side constraints first (goose where-to-start, openclaudia).
- **Agent share:** about 90%; it's a build. **Hours:** 2, reviewing.
- **Metric:** share of signups reaching the first result within a day. Start bar: half.
- **Runs with:** build (filed as issues), with design-shaping when the fix changes a surface.
- **Consumer subscription apps:** the first result that counts is a paid subscription, so the trigger and the metric are day-35 download-to-paid against the median for its paywall model in RevenueCat's yearly State of Subscription Apps (2026: hard paywall 10.7%, freemium 2.1%; category medians mix both models, Health & Fitness 2.9%, so they're context, not the bar). The usual fix runs the other way from a shorter path: onboarding that asks about the user's goal and builds their plan before a hard paywall, so they've committed before the ask, and a rating prompt at the end of onboarding so the first reviews don't come from people who bounced (one founder's practice, reported). Hard paywalls don't change year-one retention (27% against 28%), so keep freemium when free users are the word of mouth, and fix it with the general changes above. The fix's bar is that median. Watch install to paywall view beside it: one paywall vendor reports revenue moving almost one-for-one with the share of installs that see a paywall, so a low share is the first leak to find. A longer onboarding can raise conversion while losing installs before the paywall, so judge each onboarding change on download-to-paid, which nets the two (vendor, unpublished).
- **Web checkout for non-subscribers:** iOS subscription apps only (a web product's non-payers get the general fix above). Once download-to-paid holds, installs who close the paywall without buying get a discount sequence (day 0, once the window after install in which most trials start has passed, usually about an hour, then days 3, 7, 14 and 30, starting near 30% off) by push, email or SMS, each linking to a web checkout that carries the app's user id and deep links back. US apps may link out since the 2025 Epic v. Apple injunction; Apple's cost-based fee on those purchases was still being set in court as of November 2026, so check it before setting the discount. It wins back installs already in hand; don't point ads at it. One founder reports web-paid retention about 2x in-app (reported, 2022). It counts as one of the two or three. Agent share about 80% (the sequence, the checkout, the deep link); the discount and the payment account are the user's. **Hours:** 1. Metric: share of non-subscribers who buy through the sequence within 30 days. Start bar: 2%.
- **Seasonal products:** when demand comes in a season (a sport, a hunting season, tax time), churn after the season is the shape of the market, not a failure. Price annual at about three months of monthly so buyers in season take the year, and measure returns (the share of each season's new subscribers who were customers before) beside churn. Start bar: a third of the second season's new subscribers are returners; under that, the fix is a reason to come back before the season (a pre-season email, new content), not a cheaper plan. MtnWispr, an elk-call app with about 60 days of peak demand, sold $99 a year against $29 a month (one founder, reported, November 2026).

### Share loop
Every place the product's output leaves the product carries it: a "made with" badge free plans can't remove, share pages with good OG images, public templates, invites, embeds.
- **Fits:** anything whose output leaves the product (sites, docs, notes, images, video). Not internal-only tools.
- **Evidence:** Lovable, 20K to 500K users in a month at a peak weekly viral coefficient near 1.24, about $2M total spend; Elena Verna calls giving the product away its strongest strategy. Kit's powered-by traffic rose about 5x after a free plan (self-reported).
- **Agent share:** about 90%; it's a build. **Hours:** 2.
- **Metric:** share of signups whose first touch is a shared output or badge. Start bar: 15% within 60 days.
- **Runs with:** build (filed as issues), landing-page for the page a badge click lands on.
- **Start from:** marketingskills `referrals` (the viral spectrum, embedded loops) and `free-tools`.
- **Milestone moments:** at a usage milestone (a count, an anniversary), give the user an artifact made to be posted, with their name big: a certificate, a card, a physical plaque for the top tier. Write limit-reached and tenure messages as a celebration ("you out-used 94% of accounts"), not a scold. Where the product can be called in public, make that the default (Readwise's "@readwise save thread" reply under an X thread). Wiz reports customer shares rose 300% once it sent certificates; YouTube's Play Buttons and OpenAI's token coins run the same play.

### AI-answer presence (AEO)
Get named when buyers ask an AI "best X for Y": get onto the "best X" lists AI already cites, publish a comparison page and an alternatives page per rival, a how-to page per adjacent tool, and one YouTube presence. Re-check monthly; citations fade in about three months, so re-win them quarterly.
- **Fits:** B2B, dev tools, SMB software. Weaker for consumer.
- **Evidence:** Ahrefs: "best X" lists are 43.8% of ChatGPT-cited pages and 35% sit on low-authority domains; YouTube mentions correlate with AI visibility far more than backlinks. Webflow: 10% of signups from AI discovery, converting at 24% against about 4% from Google. Railway and Gamma run this.
- **Agent share:** about 80%: prompt set, weekly probes, finding cited lists, drafting outreach and pages. **Hours:** 3.
- **Metric:** share of voice across the fixed question set from the AI-answer baseline, two or three models, three runs each. Start bar: named in a third of all runs across the set within 90 days.
- **Runs with:** landing-page for comparison pages; the outreach and probe loop is unbuilt (`aeo`).
- **Start from:** marketingskills `ai-seo` (citation mix), `competitors`, `link-building` (page-level gap against a rival's backlinks); gtm-engineer-skills' keyless `aeo-audit.mjs` crawler; irabukht's prompt panel method.
- **Comparison pages that shrink the rival:** name the one thing the rival is known for, then describe ourselves in full (ClickUp: "Notion writes down work. ClickUp helps you get it done."). Add pages for the searches people make right before switching: "<rival> coupon code" (why we cost less) and our own "<us> alternatives", so we frame the comparison. AI answers invent URLs on our domain: check 404s from AI referrers monthly and build or redirect the ones that recur.
- **A data index:** once the product holds aggregate usage data nobody else has, enough that its top entries hold steady from one period to the next, publish a recurring ranking or index from it (monthly or quarterly, same method each time), so "best X" lists, press and AI answers have a number to cite and readers forward it. Ramp's AI Index and vendor rankings from spend across 85K+ companies, and Carta's State of Private Markets, run this.

### Launch stack
One coordinated launch on Product Hunt, Show HN, and the directories (DevHunt, BetaList, Peerlist, Indie Hackers, category directories), then relaunch on each major release.
- **Fits:** everyone, once per real release. Dev tools get the most from HN.
- **Evidence:** a front-page Show HN brings roughly 50 to 400 signups for a dev tool; Product Hunt traffic is about 60% day zero (vendor estimates). Lovable launched on PH several times.
- **Agent share:** about 90%: every asset, every submission, follow-ups. **Hours:** 8 in launch week, then none.
- **Metric:** signups in the 7 days after. Start bar: 100.
- **Runs with:** launch-kit for the video, stills, gallery, post, and thread; the submissions and follow-ups are unbuilt (`launch`).
- **Start from:** marketingskills `launch` (readiness gate, five phases) and `directory-submissions` (tiers, the Product Hunt timeline).
- **First wave:** put the earliest users in a private WhatsApp or Telegram group during the build. They give feedback, and on launch day they're the first upvotes and posts. Base44's founder calls it one of his best decisions (sold to Wix for $80M six months in, reported).

### Founder posts and demos
The founder posts what they're building, with short video demos of real use, daily or near it, on the one or two feeds the buyer reads. Replies feed warm outreach.
- **Fits:** dev tools, AI products, and consumer apps with a demo that lands in 15 seconds; needs a founder willing to post for months.
- **Evidence:** Bolt, $0 to $20M ARR in 8 weeks from a launch thread to an audience built over years; Lovable's founder on every channel; video beats image or text for build-in-public (practitioner consensus). Survivorship-heavy.
- **Agent share:** about 50%: drafts, demo clips, trend formats, reply mining. The voice and the product moment are the founder's. **Hours:** 4.
- **Metric:** profile visits to signups per week from the feed. Start bar: 25 signups a week by week 6.
- **Runs with:** writing-style for voice; the cadence and format loop is unbuilt (`founder-content`).
- **Start from:** marketingskills `social` (hooks) plus the teardown's content-formula read; ScrapeCreators' `outlier-post-finder` (beat your own median).
- **Pick formats by outliers:** a format, not a niche, is the market. Look for posts whose views are high relative to the poster's followers (or, sharper, against the median views of that account's last 20 posts, per platform), and for small accounts winning again and again in one format; big accounts only show what an audience does. A format is a title pattern with its slots marked, a thumbnail or cover layout, and a length; it's proven when three or more of one account's posts in it beat that account's own average; fewer makes it a test to run, not a formats-file entry. Before committing to a proven one, check whether it's breaking in: accounts started in the last year already reaching 1K+ median views with it means the market is open, and only established accounts means it's crowded. Proven and open beats proven and crowded; take a crowded one only with an angle its leaders never cover. When sizing a field (how big and how open it is, not hunting for formats), leave out any account whose views per follower run over three times the sample's median, since one fluke sets the average. Port a format proven in another niche before inventing one. Formats decay as copies pile up, so drop one when our posts in it fall under our own account's median for two weeks. The beats, titles and covers of a picked format follow the formats file rules under Unbuilt skills. Free path: the YouTube search page read in `teardown.md` and `api.fxtwitter.com/status/<id>` for an X post's views and the author's followers; any social scraping API does it in bulk.
- **Before the build:** when growth-strategy runs pre-launch for a consumer app, posting can start before there's a product: founder-POV video around a mockup of the killer feature, with a waitlist link. Consistent 10K+ views, people asking for the link, or waitlist joins read as demand, and the followers become the launch audience. Make the waitlist a loop: show each signup their place in line and move them up for each friend who joins (Robinhood reports about 1M pre-launch signups, three per member on average). Until launch the metric is waitlist joins a week (start bar: 50 by week four), and step 5's product-side check waits for launch since there's nothing to check; kill rule: no post past 10K views in four weeks means rethink the killer feature, not the posting (one founder, reported).
- **Comment office hours:** a post offering one specific reply to everyone who drops their URL or problem ("drop your site below and I'll reply with one marketing idea"), then the founder answers every one; the agent drafts the replies. The author reports thousands of newsletter subscribers from it, with no independent number.
- **One piece, a week of ways in:** a flagship piece feeds a week of posts, each from a different angle (the argument, how it's built, a clip, the build steps, a critique of the usual approach, the feedback loop, one visual), never the same summary shortened. Each post has to earn a read from someone who saw the others. Review the week's posts together, not one at a time, to catch hooks making the same claim, the same opening story twice, or facts added in repurposing. A weekly keep / test / stop review names the posts behind each proposed rule; one hit makes a hypothesis, not a rule ([VibeMarketer](https://x.com/VibeMarketer_/status/2093330541177352217), 854k views on 38k followers).

### Warm outreach
Message people who already engaged (liked, replied, starred, signed up and stalled) within 48 to 72 hours, one at a time, drafted by the agent and approved by the user. The agent learns from each edit: it diffs its draft against what was sent and keeps style notes it reads before the next draft.
- **Fits:** B2B with a reachable buyer and a founder posting. Not consumer.
- **Evidence:** 13.1% reply rate warm against 3.1% cold across 10K LinkedIn messages (vendor-published). LangChain's draft, approve, learn agent lifted lead-to-qualified-opportunity conversion 250%.
- **Agent share:** about 80%; never sends without approval. **Hours:** 2.
- **Metric:** replies per 20 messages. Start bar: 3.
- **Runs with:** unbuilt (`warm-outreach`).
- **Start from:** marketingskills `prospecting` (demand signals, draft never send) and `cold-email` principles; ColdIQ's reply benchmarks; LangChain's edit-diff memory.
- **Two openers:** the founder welcomes every new signup personally, which also catches the ones who stall (Beehiiv's CEO messaged 20K+, reported). And for 8 to 10 hand-picked dream accounts who haven't engaged, run the product on them and send the output unasked; a hand-made result isn't the cold email the skip list holds back. Vanta sent Segment a SOC 2 gap assessment before it had a product, and Segment became a design partner.

### Free tool
A small free tool (calculator, checker, generator) that answers a question the buyer asks just before buying, with the product one click away.
- **Fits:** B2B and SMB where a buying question maps to a tool. Also any product, consumer included, that can make a generator whose output says something about the user (a roast, a score, a rating) built on the product's own engine, since that output gets shared.
- **Evidence:** Wordware's free X profile roast, 8.1M tries and 400K+ product signups (reported). Each tool is also a page AI answers cite.
- **Agent share:** about 95%. **Hours:** 1.
- **Metric:** tool users to signups. Start bar: 5%.
- **Runs with:** build.

### Community presence
Be useful where the buyer already talks (a subreddit, a Discord, a Slack), as the founder, saying who you are.
- **Fits:** niches with an active community.
- **Evidence:** Lovable's Discord and subreddit; Reddit's share of ChatGPT citations swings hard (3.8% to 0.5% in August 2026), so don't count it as an AEO lever.
- **Agent share:** about 40%: finding threads, drafting answers. Posting stays human. **Hours:** 3.
- **Metric:** signups attributed to community per month. Start bar: 20.
- **Runs with:** unbuilt (`community`).
- **Lead with the problem:** a post names the problem in the user's words ("my phone has 4,000 screenshots"), not the product ("check out my photo cleaner"). Post in the community where the users already are, one at a time; tiny subs and the same post everywhere at once die at a few hundred views. One dev's Reddit run had 150K views on the problem post and a few hundred on the rest (reported; [Prajwal Tomar](https://x.com/prajwaltomar_/status/2112883397286904116)).

### Creator video
Paid creators or slideshow accounts posting short video about the product: fixed fee per video plus view bonuses, or a clipping program paid per thousand views. Market pay runs about $15 base per video plus $1 per 1,000 views (vendor). One brief per format, picked by Founder posts' outlier rule: three hooks, the beats, what's fixed and what's the creator's, and ten example videos. Approve hooks, not finished videos. Hit rate per video falls as creators scale, but total hits rise, and the top tenth of videos carries most of the views, so judge the program, not the video.
- **Fits:** consumer apps with a visual before-and-after. Also dev tools and AI products whose product shows in 15 seconds or whose team will be on camera; practitioner creators beat generalists there.
- **Evidence:** Cal AI, 250 creators on retainers to a $35M+ run rate; Stronger Mobile, 725 slideshows in 295 days to 700K users; clipping at about $1 per 1,000 views (vendor). B2B: Composio, a dev tool, reports 100+ creators, 14,000 videos and 280M views in about five months, and its CEO calls it their cheapest signup channel (self-reported); Writecream reports 31 practitioner creators converting about 7x better than generalists on identical briefs (vendor). Views don't track signups: one program saw an 800K-view video bring 0 customers and a 40K one bring 12.
- **Agent share:** about 60%: hooks, scripts, slideshow images, creator outreach, tracking. A human is the face or hires it. **Hours:** 5.
- **Metric:** signups per 1,000 views across all videos, and cost per signup (or install). Start bar: cost per signup under the price of the first month.
- **Runs with:** unbuilt (`creator-video`).
- **Owned accounts:** instead of paying for posts on creators' own accounts, hire students to start fresh accounts, warm each one to the niche (watching and engaging there before posting), then post once or twice a day from our scripts. Each video re-cuts one that already worked in the niche, with a light plug: a screenshot overlay, a feature demo, or the app name in the caption. The accounts stay ours when a student leaves (Inferred). Cost per signup counts what the students are paid. Winners become paid ad creative later.

### App Store search ads
Bid on the App Store's own search results: the category's keywords and each rival's name, with a small daily cap. The buyer is already searching, so this is intent, not the interruption ads the skip list holds back.
- **Fits:** iOS consumer apps whose keywords show demand (established rivals rank for them, from the App Store read in `teardown.md`) and whose download-to-paid holds at its paywall model's median. Not web products.
- **Evidence:** thin. One founder's consumer health app, $300K ARR in 8 months (reported), calls it the channel they most wish they'd started earlier; no public benchmark found.
- **Agent share:** about 70%: the keyword list from the field read, the campaign split (our name, category, rival names, discovery), weekly bid and negative-keyword drafts. The account, the budget, and every spend change are the user's. **Hours:** 1.
- **Metric:** cost per paid subscriber. Start bar: under the first month's price within 30 days of the title change.
- **Runs with:** unbuilt (`app-store-ads`).
- **Keyword research first:** the first weeks double as the App Store keyword read. Load 100 to 200 category keywords, bid to get data rather than profit, and rank each keyword by paid conversion and D30 retention from keyword attribution. The top one goes first in the app's title ("Keyword - App Name"), the next ones in the subtitle, since early matches weigh most; revisit the title about quarterly. Give the first two to four weeks a fixed budget judged by the ranked list; the cost-per-subscriber bar starts after the title change. One founder's practice (reported, 2022).

### Integrations and marketplace listings
List the product where its buyers already work (Zapier, Slack, a Chrome extension, a platform's marketplace), each listing a dated distribution move.
- **Fits:** B2B and dev tools that plug into a platform.
- **Evidence:** a recurring move in SaaS teardowns (marketingskills' SaaS pack).
- **Agent share:** about 80%. **Hours:** 1.
- **Metric:** installs from the listing per month. Start bar: 30.
- **Runs with:** build.

### AI agent surfaces
A remote MCP server for the product, listed where a user's assistant can find it, so "do it for me" lands in our product instead of a rival's.
- **Fits:** products with an API and at least one task an agent would run for a user (create, fetch, transform). Not static content or a one-screen tool.
- **Evidence:** a listing alone brings nothing: ten servers on npm and Glama got zero downloads in week one (builder-reported). The pull comes from AI answers: Tally reports 44% of a ~40K-signup week via assistants, with its Claude connector at #252 of ~2.5K; Rauch reports ChatGPT refers 10% of new Vercel signups (2025-04). So it counts as its own technique but works best picked beside AEO, which is what makes assistants recommend the product.
- **Agent share:** about 90%: the server, tool annotations, privacy page, test account, submissions, and a weekly probe that uses it the way a customer's agent would. The OAuth decision and the paid Claude plan are the user's. **Hours:** 1 after launch week.
- **Metric:** "Used a tool" accounts over 30 days, from the Claude directory dashboard. Start bar: 50 by day 60.
- **Runs with:** build for the server; the submissions are unbuilt (`launch`): the Claude directory, the official MCP registry (downstream directories ingest it), ChatGPT's plugin directory when ordinary ChatGPT users would ask for the task (not a developer tool), and Google's Connected Apps waitlist. No sweep of MCP directories (launch directories are a separate list); one builder covered 27 in three days and couldn't attribute traffic to any.
- **Start from:** Claude's connector submission and review-criteria docs (claude.com/docs/connectors/building/submission); the official registry's `mcp-publisher` quickstart.

## Skip by default

Say the reason when one of these comes up, and only lift it when the evidence for this product says otherwise.

| Play | Why not, for now |
|---|---|
| llms.txt | No AI system is shown to use it; Webflow saw no lift |
| Informational programmatic SEO | Position-1 click-through on AI Overview queries fell from 7.3% to 2.6%; comparison and integration pages survive and are covered above |
| Paid ads | Spend before organic converts buys data you can't read; Meta wants about 50 conversions a week per ad set. Revisit once a technique converts. App Store search ads are the exception, in the catalog. Lift it early once the activation fix has passed its bar (step 5; for a consumer subscription app that's download-to-paid at its median), when the product has a free first result (a score, a plan, a generated output) and at least a third of those who reach it pay: optimize Meta for an event it sees daily (75% of a long video watched, the first result finished) instead of purchases, target broadly, and send the ad straight to the free result. Metric: revenue back per dollar spent, 14 days after each ad dollar. Start bar 1x; kill it under 1x after two weeks at a fixed daily spend. MtnWispr ran this from $50 a day at 2x return (one founder, reported, November 2026) |
| Ad variants at volume | Same reason; production was never the bottleneck |
| AI SDRs that send on their own | Burned trust and churned (11x, Artisan) |
| Cold email | Needs domains, warmup, and deliverability work; 3.4% average reply. A later infra decision |
| Newsletter and podcast sponsorships | $60 to $150 CPM with no signup data; a revenue-stage play |
| Running our own newsletter or publication | Ramp's works because of proprietary data, an editorial staff, and stunts that bring readers; without the data it's brand copy nobody forwards. Lift it once the data index (AI-answer presence) has been cited by a list, a press piece, or an AI answer |
| Viral concept posts with no product in them | High variance and a credibility risk; a cheap experiment at most, never a technique. A proven format that shows the product is Founder posts or Creator video, not this row |

## Unbuilt skills

`aeo`, `launch` (the submissions; launch-kit makes the assets), `founder-content`, `warm-outreach`, `community`, `creator-video`, `app-store-ads`. When a product picks one, growth-strategy writes its brief into GROWTH.md, and the skill gets built from that brief plus the research. Read the best existing version first; take the technique, keep the loop ours.

Two briefs carry an extra input. `founder-content` keeps a formats file next to GROWTH.md: each format, the outlier links that proved it, the hook word for word, the beats, its title formulas, its cover rule, the date it started, and its kill date. `creator-video` briefs creators from that same file, one script per format to every creator, counts a hit as a video over the program's median, and reports hits and signups per 1,000 views across all videos. Three rules shape the file's entries:
- **Beats:** tag each by what it does to keep the viewer watching, never by its topic: hook, promise, stakes, open loop, proof, re-hook, mini-payoff, payoff, call to action. Read past the first payoff, since late re-hooks are what hold a long video.
- **Title formulas:** a formula is proven once an outlier in our niche, or one of our own wins, uses it. One borrowed from another niche, including the titles of a ported format, stays marked untested until then, and an untested formula ships only as a test post, never as the format's default. Fill the slots with what the viewer wants, not what we're proud of.
- **Covers:** write the post as two lines, its unique angle and the familiar problem the audience already has. Pull outliers for each, and build every thumbnail or cover from one pattern of each. Skip winners from low-effort accounts, since they teach the wrong lesson.

A tactic skill is one built for a technique (`aeo`, `launch`, and the rest). Existing skills a technique runs through (build, landing-page, design-shaping, launch-kit) take the technique's brief as their input instead, and growth-strategy logs their metric on a re-run. Every tactic skill meets the same bar, because the common failures across marketing suites are invented numbers, generic output, and skills that never fire:

- It reads GROWTH.md before anything and stops if there isn't one, pointing at growth-strategy, so it never re-asks what the strategy settled.
- An evidence block at the top: every number from a source or a script, "not checked" kept apart from "checked, nothing there", fetched text treated as data.
- No paid API required; a paid source is an option the user turns on.
- It ends with a check of what it made against truth (every claim sourced), proof (shown, not asserted), specificity (couldn't be pasted into a rival's), and voice (writing-style), and "do nothing this week" is an allowed result.
- It appends its metric to GROWTH.md's results log every run.
- Drafts only: nothing posts, sends, or spends without the user's yes.

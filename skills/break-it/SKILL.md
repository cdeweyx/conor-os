---
name: break-it
description: >
  Tries to break a built product with the realistic worst case (long names,
  counts of 0 and 1,000+) and every action slow, failed, or pressed twice,
  then reports what broke before fixing. Use after implementation, at
  zero-to-one's Quality step, or when the user says "break this", "worst
  case", "stress test", "edge cases", "what if it fails". Do NOT use on
  wireframes or Paper (it needs running code), for visual critique
  (impeccable), for motion (review-animations), or to check the build
  against the docs (zero-to-one's end-to-end review).
metadata:
  adapted-from: https://github.com/emilkowalski/skills/tree/main/skills/break-ui
  author: Emil Kowalski (break-ui, MIT); adapted for zero-to-one
---

# Break it

Everything gets built against kind data. The demo rows were picked, usually without anyone noticing, so the design looks good: names that fit on one line, counts that never need a separator, every optional field filled. This step undoes that choice one field at a time, on the running product, once, after implementation and before the end-to-end review, so the review checks a product that has already survived its worst users.

Everything also gets built against a kind network: every request answers fast and works, and nobody presses twice. So the second axis is actions. Every button that saves, refreshes or runs has moments in between (working, failed, failed after good content was already drawn, pressed again, left mid-way) that nobody designed, because the code grew them from a pile of flags rather than a named state. Design covers the states someone thought of; this finds the ones the code can reach anyway.

It runs on code because only code breaks for real. A canvas approximates the CSS; the app is the CSS. It finds and reports; it doesn't redesign, critique taste, or review motion.

## Rules

- Plausible or data-backed, never random. Every worst-case value is something a real user could produce, the real extreme from the product's own dataset, or the limit from the schema, column, or API contract. `"aaaaaaaa"` and 5,000-character names prove nothing and get the report dismissed. No limit anywhere is a finding: say "unbounded" and test something long but believable.
- Change the data, not the component. The worst case enters where the demo data does (the fixture, the mock, the loader, the API stub). A break produced by hand-editing markup tests the edit.
- Fail at the network, not in the component. Slow and failed requests enter where real ones do (Playwright route interception, the API stub), never by setting a component's state by hand.
- One dataset, many failures. Spread different breaks across the first rows (row 1 the long name, row 2 the long email, row 3 the one-letter name), since that's what's on screen and how real data arrives.
- The toggle is dev-only and never ships.
- Report before fixing. Some breaks are product calls (what an empty field shows, paginate or virtualize). List everything, then stop.
- Handle the small stuff. Whether a field wraps, truncates, or clamps is the agent's call, made from the rules in `references/signatures.md` and shown in the Fix column. It never goes to the user as a question and never becomes a rule in the docs; nobody needs a spec for a name between 73 and 82 characters.

## Steps

1. Map every surface. Per surface, a table of every value it renders: field, source (a model-generated field says so), type, limit (with `file:line`), optional or not. Include what people forget: counts in headers, relative times, badge and status text, labels that come from data, tooltips, images, and the list itself, since its length is a value. Where the form and the column disagree (a 50-character input saving to a 255-character column), the longer one wins; it'll arrive through an import. Run the inventory count in `references/catalog.md` while you're in the code. Done when every rendered value has a source and a limit or "unbounded". Then list every action on the surface (a button, a form, an automatic refresh) with the states the code can be in during it, read from the flags and status values it sets, and whether the design draws each one.

2. Pull the domain extremes. Query the product's real data before opening the catalog: the longest name in every name column, the max and min of every count and number, every null an optional field actually has, the week or page with one item and the one with the most, the duplicate names. The product's own extremes are the breaks that ship (the weekly plan that held at eight meals and fell apart at one); the generic catalog is the floor, not the test.

3. Build the worst-case fixture. One file for the product, beside the existing demo fixture and shaped exactly like it, so every surface reads the same worst case and the numbers agree across surfaces. Fill it from step 2, then from `references/catalog.md` for every row that applies to a field in the map. Add the cases one dataset can't hold: Empty (zero items, no results), One (a single item, every count at exactly 1), and 1,000 (the realistic upper bound for an unpaginated list).

4. Wire the toggle. A segmented control, Demo / Worst / Empty / One / 1,000, fixed bottom-center, plain chrome (gray track, white pill, system font, no animation), that swaps the fixture at the data boundary through a URL param (`?data=worst`) so a reload or a shared link keeps the state. Gate it on the dev environment.

5. Break it. One `worker` per surface, in parallel, each handed the surface's map, the fixture, and the toggle URL (Model: worker role). Each flips every toggle state and checks it at the surface's real container width, at 320px, at the widest layout, and at 200% zoom, plus dark mode, `dir="rtl"`, and the longest shipped language if the product supports them. Run the 320px pass as a touch device (Playwright `hasTouch` and `isMobile`): a hover-only action, a hover state stuck after a tap, and a tap target under 44px are breaks. Screenshot every state at every width with Playwright, read each against the signatures in `references/signatures.md`, and record each break with its signature, cause, and fix location. Anything inferred from CSS rather than seen in a screenshot is marked inferred. Then, on Demo data at the real width, drive every action in the map five ways: a request held for 3 seconds, a failed one, a double press, a reload mid-action, and leaving the page mid-action, plus a failure after the surface has already drawn good content. Screenshot the moment in between, not only where it settles, and record what the user sees, what the code sends (a second request on a double press is a break), and whether the design draws it. Last, load each surface cold on a slow-3G profile with a 4x CPU slowdown (CDP `Network.emulateNetworkConditions` and `Emulation.setCPUThrottlingRate`) and screenshot at 1s, 3s, and settled: a blank screen, a font swap, layout shift, and a tap that lands before the page's code is ready are breaks. Holding one request doesn't show these, since only a slow first load does.

6. Report and stop. Merge the workers' findings into the report below, leave the toggle running, and wait. The user flips the toggle, looks, and decides.

7. Fix on request. "fix all" or "fix 1, 3". All the fixes go on one ticket in the product's tracker project ("Break it: edge-case fixes"), and that ticket maps to one PR up for review: one branch, every fix, the worst-case fixture and the toggle included. Not a ticket per break, and never added to another open PR. Fixes use the project's tokens and conventions. Screenshot each break before fixing it and again after, at the same width and state, and put the pairs in the PR body so the review is a glance. After the fixes, flip every state again, Demo included, because a fix for the worst case mustn't regress the demo.

8. Close. The worst-case fixture stays in the repo as the regression test for the next person who touches a surface. Gate: every break is fixed or decided, and the one PR is up for review.

## The report

Written through writing-style. Three parts, per surface, worst first.

What broke. One row per break: severity, field or action, the worst-case value or the way it was driven, what happens, the fix with `file:line`. A tangle of flags behind an action break is fixed with one status value with named states, not another flag. Severity is Broken (content unreadable, action unreachable, wrong data), Ugly (readable but visibly wrong: a squished avatar, a wrapped badge), or Fragile (fine now, one realistic step from breaking: no limit, no fallback).

| # | Severity | Field | Value | What happens | Fix |
| --- | --- | --- | --- | --- | --- |
| 1 | Broken | `email` | `bartholomew.fitzgerald@northwind-industries-holdings.example.com` | Pushes the ••• menu off the row at 320px | `min-width: 0` on the text column, `overflow-wrap: anywhere` on the email, `flex-shrink: 0` on the menu (`MemberRow.tsx:42`) |
| 2 | Ugly | `count` | 1 | "1 members" | `Intl.PluralRules` (`MembersHeader.tsx:12`) |

Calls for you. Only breaks where the answer changes what the user sees or can do: what an empty optional field shows, paginate or virtualize a long list, whether a missing value hides a row. One line each, with a lean, the runner-up, and why. Wrap, truncate, and clamp aren't calls; they're fixes. Neither is a moment the product already handles somewhere else (a busy state on one Refresh but not another): copy the pattern it has. An undesigned moment is a call only when nothing in the product shows how it should look.

What held up. The worst cases the product already handles, so the test reads as real and the user knows what not to touch. A short report on a sturdy product is a good result.

Close with the toggle URL, its states, and the word to send back: "fix all" or "fix 1, 3".

Matter-of-fact, never smug. The product wasn't badly built; it was built against kind data, like nearly everything.

## Things that go wrong

- Stopping at long text. The breaks that ship are the short name that leaves an orphaned dash, the count of exactly 1, the missing image, the empty list, the badge whose text got longer.
- Generic data only. Catalog names on a product whose real breaks live in its own data (a habit name, a one-day streak, a 300-day history).
- A fixture per surface. Two surfaces with two worst cases disagree with each other, and the regression test covers half the product.
- Checking only the full-page width. A list reused in a 280px sidebar is a different component.
- A kind network. Every action tested only where it settles, so the button that does nothing for eight seconds, the error that wipes a loaded page, and the second press that sends a second request all ship.

## Checklist

- Every rendered value on every surface mapped, with a source and a limit or "unbounded".
- Domain extremes pulled from the real data before the catalog was opened.
- One worst-case fixture for the product, plus Empty, One, and 1,000, entering at the data boundary.
- Dev-only toggle with the state in the URL.
- Every state checked at real width, 320px (as a touch device), widest, and 200% zoom, with screenshots; inferred findings marked.
- Every action driven slow, failed, pressed twice, reloaded, left mid-way, and failed after content was drawn, with the in-between moment screenshotted; every surface loaded cold on slow 3G.
- Report in three parts, calls with a lean and a runner-up and none about overflow, then stopped.
- Every fix on one ticket and one PR with a before and after pair; re-verified across every state, Demo included; fixture kept.

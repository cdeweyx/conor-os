# Structure: should these pieces change together?

Read by pr-review's structure lens at milestone close and by untangle's list step. Adapted from caldoai's [untangle-codebase](https://github.com/caldoai/skills/tree/main/skills/untangle-codebase) (MIT, commit 442c299) for the question, the taxonomy and the decision log; LordGhostX's [rewrite](https://github.com/LordGhostX/agents-skills/tree/main/skills/untangle-codebase) (MIT, 610ee7f) for the guardrails; Matt Pocock's [codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design) and improve-codebase-architecture (MIT) for the deletion test and hot spots first.

## The question

Ask it of every piece you read. Code gets the answer wrong in three ways, and special cases show where the design never caught up.

- **Hidden links**: pieces that must change together, where nothing shows it. Copies of a value or rule, a module reading a global another one sets, one feature split across folders by layer, a call order callers just have to know. Example: `pricing/tax.ts:12` and `checkout/Summary.tsx:40` each hard-code the tax rate, so changing one makes the receipt disagree with the charge.
- **Needless links**: pieces tied together that change for different reasons. Callers that reach into internals, stable code that imports something more volatile, a general function with a parameter only one workflow understands, a shallow module whose interface moves whenever its insides do. Example: `utils/format.ts:8` takes `isInvoicePdf`, so the shared formatter changes every time the invoice template does.
- **Surplus**: pieces with no reason of their own to change. Pass-through wrappers, config and extension points for things that never vary, dead code. Example: `api/client.ts` wraps `fetch` one to one, and every caller passes the same options.
- **Special cases**: code that exists for one situation instead of following from how the system works. An `if` for one value, a parameter for one caller, a swallowed exception, a retry or a sleep, a disabled test. Each is a requirement the design never accounted for, so read them together for what the design is missing rather than fixing them one by one. Example: `ui/LogoutDialog.tsx:30` waits 100ms after closing and hopes the input can take focus by then.

## Where to look first

- **Hot spots.** Structure only costs something where code keeps changing, so start with the files history keeps touching: `git log --since="6 months ago" --format= --name-only | sort | uniq -c | sort -rn | head -20`. A tangled file nobody's touched in a year can wait.
- **Co-change.** Files that keep landing in the same commits, across folders, are a hidden link unless the code shows why. Pair counts, skipping commits over 20 files:
  `git log --since="6 months ago" --format='format:--' --name-only | awk 'function flush(){if(n<=20)for(i=1;i<=n;i++)for(j=i+1;j<=n;j++)c[(f[i]<f[j])?f[i]" "f[j]:f[j]" "f[i]]++; n=0} /^--$/{flush();next} NF{f[++n]=$0} END{flush(); for(p in c) print c[p], p}' | sort -rn | head -20`
- **The deletion test.** Imagine deleting the module. If the complexity vanishes, it was a pass-through (surplus). If it reappears across its callers, it earns its keep.

## Guardrails

- The categories are cues, not defects. Wrappers, retries, conditionals, duplication and folder layouts are fine on their own; find the responsibility or requirement each one serves before calling it a problem.
- Every finding names the concrete change that becomes fragile or costly ("adding a second payment provider means editing four files nothing links"), backed by the connected code or the history. No named change, no finding.
- Check the counter-evidence before proposing a removal or a merge: the test that pins the special case, the commit that added the retry and why, the second caller of the wrapper.
- No findings is a valid result. A short report on a sound area is a good one.
- Fewer files, wrappers or special cases isn't success. Success is the named change getting easier while required behavior stays the same. Don't build a general framework to merge code that only looks alike.

## The decision log

Write each fix above the problems it dissolves. The one fix behind several problems often looks nothing like them, and the log survives compaction. Judge every fix by the same question: pieces that change together end up together, pieces that don't aren't tied, and everything depends on what changes less.

```md
- Make the general `Dialog` give focus back to whatever had it before it opened, so the wait and the flag both go.
  - `ui/LogoutDialog.tsx:30` waits 100ms after closing and hopes the message input can take focus by then.
  - `ui/SettingsDialog.tsx:61` sets a global `skipRefocus` flag so the logout dialog it opens doesn't send focus to the input.
- Define a `PaymentProvider` interface that Stripe and PayPal both implement, so checkout and refunds stop knowing which one they use.
  - `checkout/submit.ts:9` depends directly on `payments/stripe.ts`.
  - `refunds/refund.ts:22` wraps every Stripe call in `if (order.provider === "paypal")`.
```

A problem no fix dissolves stays on the list under the log, as it is.

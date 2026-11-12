# Sign-in setup (Firebase)

The runbook for giving a product public accounts, from the first run. Read it at the milestone that first adds sign-in, before the provider question goes to the user.

## Calls to make before any clicking

- **Provider: Firebase Auth,** Google plus email magic links, no passwords. The user's bar for commodity infrastructure is free that does the whole job, with nothing for him to run. Firebase is free to 50,000 monthly users, sends the link emails itself from our domain, keeps sessions long, and ships a local emulator for tests. Lead with it; don't spend rounds on Clerk (7-day sessions on free), Better Auth (runs its own mail) or Stytch (its domain on the email until $99) unless the product needs something Firebase lacks.
- **Say up front:** magic links need Firebase's pay-as-you-go Blaze plan. The free Spark plan sends 5 link emails a day. Blaze needs a card on file and costs $0 at our volume (sign-in is no-cost to 50,000 MAU, no per-email charge); set a $1 budget alert. Answer the "what will I pay" question with that, once.
- **Magic links over codes** is the user's pick. Its cost: a link opened in another browser (every sign-up from X's or Reddit's in-app browser) asks for the email again. Google sign-in is blocked in app webviews, so the dialog leads with the email link there.
- **Legal pages first.** Google's consent screen requires a public privacy policy URL, and uploading a logo triggers Google's brand verification, which needs the privacy and terms pages live. Draft privacy and terms (the product's legal issue) before the user reaches the consent screen, give him the URLs they'll live at, and file a pre-launch issue for the logo upload and verification.
- **Google Analytics** is the one analytics tool the user turns on at project creation; product analytics comes later. The privacy policy names it.

## What the user does (about 20 minutes; one screen at a time, with direct links)

Firebase's console moved its menus in 2026: Authentication sits under **Security**, not "Build". Firebase also creates its own Google Cloud project (`<name>-<suffix>`), and the Cloud console opens on whatever project he used last. Send direct links with `?project=<id>` instead of menu paths.

1. **Firebase project** (console.firebase.google.com): name it, Google Analytics on. **Security → Authentication → Get started.** Sign-in method: Google (public name, support email); Email/Password with "Email link (passwordless sign-in)" on. The Email/Password switch turns on with the link switch: that's expected, and no password field exists in our dialog. Settings → Authorized domains: the app and apex hostnames. Project Overview → Add app → Web: he pastes the config (public). The **Spark plan** badge → Blaze, then a $1 budget alert in Cloud Billing.
2. **Google's consent screen:** `https://console.cloud.google.com/auth/branding?project=<id>` (name with a capital, support email, home page, privacy and terms URLs, authorized domain; no logo yet), `/auth/audience?project=<id>` (External, Publish; it then reads "In production", and its "100 user cap" applies only to sensitive scopes, never to `openid`, `email`, `profile`, so say so before he asks), `/auth/clients?project=<id>` (the auto-created web client: JavaScript origins and `/__/auth/handler` redirect URIs for both hostnames).
3. **Sender domain:** Firebase → Security → Authentication → Templates → the pencil → customize domain; the records (a `firebase=<project>` TXT, an SPF TXT, two `firebaseN._domainkey` CNAMEs) go into Cloudflare DNS as DNS only. Run `dig +short TXT <apex>` and `dig +short TXT _dmarc.<apex>` first and write the exact edit into his steps: a domain Cloudflare parked for no mail carries `v=spf1 -all` and a strict DMARC reject, so he edits that record to `v=spf1 include:_spf.firebasemail.com -all` rather than adding a second one, and leaves DMARC alone (Firebase's DKIM aligns). The same dig shows whether the support address in the legal pages can receive mail (no MX means it can't); when it can't, the steps open with Cloudflare Email Routing forwarding `support@` to his inbox, and the one SPF line carries both includes (`_spf.firebasemail.com`, `_spf.mx.cloudflare.net`). The Reply to on the templates is that support address. Once he picks an option, write it into the steps he's following rather than leaving it as a separate answer. Then Apply Custom Domain once it verifies. The Templates list has no email-link template: the link email takes the sender name and From set on Email address verification (sender name is a field there, beside From). Customize action URL waits for the hosted step.
4. **Later, pre-launch:** logo upload and brand verification once the legal pages are live.

## The records, exactly (verified live November 2026)

Firebase's docs don't publish these; its dialog does. With project `<id>` and apex `<apex>` (dots become dashes in the DKIM target), every row DNS only:

| Type | Name | Value |
|---|---|---|
| TXT | `@` | `firebase=<id>` |
| TXT | `@` | `v=spf1 include:_spf.firebasemail.com include:_spf.mx.cloudflare.net -all` (the one SPF line; drop the Cloudflare include without Email Routing) |
| CNAME | `firebase1._domainkey` | `mail-<apex-dashed>.dkim1._domainkey.firebasemail.com` |
| CNAME | `firebase2._domainkey` | `mail-<apex-dashed>.dkim2._domainkey.firebasemail.com` |
| MX x3 | `@` | `route1/2/3.mx.cloudflare.net` (Email Routing adds them, plus its own `cf2024-1._domainkey` DKIM) |

Leave a parked domain's `_domainkey` TXT `v=DKIM1; p=` and its `_dmarc` reject alone. Check with `dig +short TXT <apex> @<zone's NS>` and `dig +short TXT $(dig +short CNAME firebase1._domainkey.<apex> @<NS>)` (a DKIM key back means the target is right). Email Routing in the dashboard: Destination addresses (the user's inbox, then its verification click), then Routing rules → Create address `support` → Send to an email; Email Routing's Settings tab compares the SPF line to its own exact string (`v=spf1 include:_spf.mx.cloudflare.net ~all`), so a merged line can read Missing plus Conflicting there, and that page caches the old value for a while. Never press its Delete or Add missing records on a merged line: one drops Firebase's include, the other adds a second SPF record. Prove it with a test email to `support@` instead.

## Automate it next time

The user doesn't want to click through this again. Before the next product's sign-in, build one script from this table (curl plus `gcloud auth print-access-token` for the REST rows, the MCPs for the rest), run it on a throwaway project, and leave him only the "left for him" column. Researched November 2026: every row was read in docs, discovery documents or source, none run signed in yet.

| Step | Path | Left for him |
|---|---|---|
| Project, web app, config | Firebase MCP (`claude mcp add --scope user firebase -- npx -y firebase-tools@latest mcp`): `firebase_create_project`, `firebase_create_app`, `firebase_get_sdk_config` | `firebase login`, once |
| Google Analytics | `POST firebase.googleapis.com/v1beta1/projects/<id>:addGoogleAnalytics` (`analyticsAccountId`) | none once a GA account exists |
| Blaze and the $1 budget | `gcloud billing projects link`; `gcloud billing budgets create --budget-amount=1USD --threshold-rule=percent=0.5 --filter-projects=projects/<id>` | a card on the billing account, once; `gcloud auth login` |
| Google provider, brand name, support email, redirect URIs | `firebase.json` `auth.providers.googleSignIn` (`oAuthBrandDisplayName`, `supportEmail`, `authorizedRedirectUris`), then `firebase deploy --only auth` | none |
| Email link sign-in, authorized domains | `PATCH identitytoolkit.googleapis.com/admin/v2/projects/<id>/config`: `signIn.email {enabled, passwordRequired: false}`, `authorizedDomains` | none |
| Sender name, From, Reply to | the same PATCH: `notification.sendEmail.verifyEmailTemplate.{senderDisplayName, senderLocalPart, replyTo}` | none |
| Custom sender domain | `POST identitytoolkit.googleapis.com/v2beta1/projects/<id>/domain:verify` with `{"domain", "action": "VERIFY"}`, poll Config `notification.sendEmail.dnsInfo.customDomainState`, then `"action": "APPLY"`; the records come from "The records, exactly" (the call returns only state) | none |
| Consent screen: home, privacy and terms URLs, authorized domain, External and Publish, JavaScript origins | no public API (IAP brands API deprecated January 2025; the console's backend is private): browser control on `console.cloud.google.com/auth/{branding,audience,clients}?project=<id>` | none if browser control works |
| Cloudflare DNS rows | Cloudflare MCP (`claude mcp add --transport http --scope user cloudflare https://mcp.cloudflare.com/mcp`, OAuth scopes incl. `dns.write`, `email-routing-address.write`, `email-routing-rule.write`): `execute` on `POST /zones/<zone>/dns_records`, `proxied: false` | the OAuth screen, once |
| Email Routing | the same MCP: `POST /zones/<zone>/email/routing/dns` (enable first), then PATCH the SPF row to the merged line, `POST /accounts/<acct>/email/routing/addresses`, `POST /zones/<zone>/email/routing/rules` | a new destination's verification click |
| Logo upload, brand verification | browser control | the submit, after the legal pages are live |

Unverified until the first run: whether `firebase deploy --only auth` makes the brand In production or Testing; whether user-token calls need `X-Goog-User-Project`. Installing `gcloud` and `firebase-tools` globally, and adding the two MCPs, are his call: ask once, with this table.

## Faster next time

- Put the console steps in a Waiting-on-Me issue with direct links from the start; the user works through them away from the chat.
- Screens the user hits that this file doesn't name: add them here the same session.

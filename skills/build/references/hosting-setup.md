# Hosting setup on Cloudflare

The runbook for putting a product on a domain, from the first run. Read it at the milestone that first hosts a product. The user does only the steps that need his account or card; everything after the deploy login is ours.

## Calls to make before any clicking

- **Host:** Cloudflare (tech-planning preferences, "Across projects"). Workers for anything Workers can run; a Container behind a Worker when the app needs a runtime Workers lack (a native binary, a language Workers don't run). Never propose a host the user hasn't used without asking.
- **Domain:** the launch domain, since products go public eventually. Check the exact .com first; a taken one is often on a marketplace (whois NS at atom.com, sedo, afternic, dan.com means for sale), so name its listing and let him decide. Runner-up: a prefixed .com (get-, use-), plus the cheap exact-name ccTLD pointed at it. .co loses typed-from-memory traffic to whoever owns the .com.
- **Buy it at the registrar where the user's domains already live.** When that registrar has no domains API or MCP, the nameserver switch below is his one manual registrar step; it takes a few minutes.
- **Gate:** v1 is one user with no auth, so the app goes on `app.<domain>` behind Cloudflare Access (his email only), never an open URL. Access comes off in the Go live epic's last issue, after Quality and the end-to-end review, on the user's yes (zero-to-one, Go live's Build step).
- **State:** Container disk is ephemeral (wiped on sleep and deploy; persistent disk isn't coming soon). SQLite restores from R2 on start and streams back with Litestream; one instance. Move to Turso or D1 when there's a second user.
- **Schedule:** a Worker Cron Trigger (to the minute, free) calls the app's one scheduled entry point; the app decides from config what's due. No in-process scheduler, no GitHub Actions cron (5 to 30 min late, skips runs).

## What the user does (about 15 minutes; send this as numbered steps, one screen at a time)

1. **Domain onto Cloudflare** (skip if bought on Cloudflare Registrar). Cloudflare: Add a domain, Free plan, keep the DNS quick scan. On the AI crawler screen: no ads, Search allow, Training block, Agents allow, Bot Preference Sync on, DNS import Automatic. Copy the two nameservers. At the registrar: check DNSSEC is off first (no DS records means off), then Domain Nameservers, custom, replace all with Cloudflare's two, save. Leave the registrar's DNS records alone. Verify from here with `dig +short NS <domain> @1.1.1.1`; it usually switches within minutes.
2. **Workers Paid** ($5 a month): Workers & Pages, Plans. Needed for Containers.
3. **R2:** turn it on (card; 10 GB free), bucket `<product>-state`, an API token with Object Read & Write on that bucket only. The key id, secret and endpoint go in `~/.config/<product>/r2.env`; if he pastes a token in chat, use it (an R2 account token gives the S3 pair: key id = the token id, secret = SHA-256 of the token value); he's chosen to, so don't add a warning.
4. **Access:** Zero Trust (team name, Free plan), then Access, Applications, **Create an application**, Self-hosted: name, public hostname `app` + `<domain>` with no path, an Allow policy on his email (select the existing one if he made it first), One-time PIN, Save. Then he reads back two values: the app's Application Audience (AUD) Tag and the team domain (Settings, Team name and domain), which the Worker's JWT check needs. Done means the Access overview reads **Applications: 1**; a saved policy alone protects nothing.
5. **Budget alerts:** none to set up; Cloudflare's default billing notifications already email him past $10 (November 2026). Cost limits live in the config files instead (instance type, sleepAfter, Litestream intervals and retention), each with a one-line reason.
6. **Deploy login:** `npx wrangler login` in a terminal on this machine; Docker Desktop running for container builds.

## Fail closed from the first deploy

Access is the only lock on a v1 app, and a misconfigured Access app fails open: a first deploy once served the app and its API to a signed-out `curl` with a 200 for about 4 minutes, until the lead detached the custom domain through the API. So:

- The Worker checks the Access JWT itself on every request (`Cf-Access-Jwt-Assertion`: signature against `https://<team>.cloudflareaccess.com/cdn-cgi/access/certs`, `aud` against the app's AUD tag, expiry) and answers 403 without one; the cron's `scheduled()` is the only exception. Ask the user for the team domain and the AUD tag at step 4, and build the check before the first deploy.
- Right after every deploy, a signed-out `curl -sI https://app.<domain>/` must answer a redirect to `<team>.cloudflareaccess.com`. Anything else: detach the custom domain at once (`DELETE /accounts/<id>/workers/domains/<id>`, which wrangler's OAuth token can do) and stop for the user.
- Wrangler's OAuth token has no Access scope, so the lead can't read or fix Access settings; step 4's screens are the user's, and the runbook names exactly what to check (self-hosted, the exact hostname, an Allow policy attached).

## Faster next time

- **A deploy needs the host's built data on disk.** When the image ships a build the host makes, deploy from a checkout that already holds it, held out of the worktree pool (its clean wipes ignored files), and every handoff names that checkout; from a fresh worktree the deploy rebuilds from the network, and beside another job pulling from the same API it gets throttled and fails before upload. A container deploy also needs the Docker engine up: check `docker info` first and start it with `docker desktop start` (a CLI, no GUI); wrangler fails at the image build otherwise.
- Domains stay at the user's registrar; don't suggest moving registrars. Check again for that registrar's domains API or MCP before the next domain.
- Cloudflare's official MCP servers (OAuth; a Code Mode endpoint at `mcp.cloudflare.com/mcp` reaches DNS, Workers, R2, Zero Trust) could do steps 3 and 4 after one sign-in. Not yet tried; ask before adding it, then record here what it could and couldn't do.
- Lead scripts that call a Worker use curl: the workers.dev front door returns 403 to Python urllib's default user agent.
- Screens the user hits that this file doesn't name: add them here the same session.

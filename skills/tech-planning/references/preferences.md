# Preferences

The user's picks from past plans, so the next plan starts from them. Add at every checkpoint.

## Across projects
- Hosting: Cloudflare by default (Workers, Containers when a process needs a runtime Workers lack, R2, Cron Triggers, Access, Registrar). Not Netlify ("I don't love it"), and don't propose a host the user hasn't used without asking first. The domain, Access, R2 and deploy-login steps are a runbook in build's `references/hosting-setup.md`; the plan's hosting milestone cites it.
- Plan for going public when the product will, even when v1 is one user: the domain is the launch domain, and no hosting or store pick should block a second user.

## Harness and review
- Harness: Linear as the only list, one lead per milestone in its own worktree, a fresh implementer per issue, review on localhost with Agentation, one check command behind a Stop hook, a 40-line CLAUDE.md.
- Review taste: plain-language risks before forks; blast radius with every change; "simplify dramatically" when a paragraph reads as plan-speak.

## Lighter process
- Scale: one planner, three seats, two rounds, by the user's call for a small personal tool.

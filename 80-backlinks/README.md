# Backlinks

This folder is the durable home for Velu backlink work. It has two parts.
Current-state files record what the links are. Implementation files are the
backlog and the log of work already done.

The public site is published in GoHighLevel. A commit here does not publish
velu.us. Redirects are URL rules in GoHighLevel.

**High — outstanding performance follow-up** stays open in
[70.10](../70-implementation/70.10-website-roadmap.md). It is not a backlink
recommendation. No performance test is part of this folder.

## Workflow

Current-state findings feed recommendations. Each recommendation is one file
with an ID, rationale, expected impact, effort, owner, status, and acceptance
criteria. Implement one recommendation at a time. Update that item's status,
and add a dated entry to the implementation log, when the work is done. Do not
start the next item because an earlier one is written down.

The ordered list is
[80.60-recommendation-backlog.md](80.60-recommendation-backlog.md).

## Current state (`80.10`–`80.49`)

| File | What it is |
| --- | --- |
| [80.10-backlink-playbook.md](80.10-backlink-playbook.md) | How to refresh this folder and enter a redirect. |
| [80.20-backlink-audit-2026-11-25.md](80.20-backlink-audit-2026-11-25.md) | November 25, 2026 Ubersuggest audit summary. |
| [80.21-referring-domains-2026-11-25.csv](80.21-referring-domains-2026-11-25.csv) | Current referring-domain snapshot, 230 rows. |
| [80.22-new-referring-domains-2026-11-25.csv](80.22-new-referring-domains-2026-11-25.csv) | New-domain snapshot, 111 rows. |
| [80.23-lost-referring-domains-2026-11-25.csv](80.23-lost-referring-domains-2026-11-25.csv) | Lost-domain snapshot, 12 rows. |
| [80.24-referring-domain-inventory-2026-11-25.md](80.24-referring-domain-inventory-2026-11-25.md) | What the 230 rows are. |
| [80.25-broken-target-inventory-2026-11-25.csv](80.25-broken-target-inventory-2026-11-25.csv) | Each audit target, its status, and its linking domains. |
| [80.26-lost-link-status-2026-11-25.md](80.26-lost-link-status-2026-11-25.md) | What happened to each lost link, checked where it mattered. |
| [80.27-disavow-candidates-2026-11-25.csv](80.27-disavow-candidates-2026-11-25.csv) | SEO-directory campaign. Not uploaded. |
| [80.28-link-equity-by-page-2026-11-25.md](80.28-link-equity-by-page-2026-11-25.md) | Which velu.us URLs the export actually points at. |
| [80.29-competitor-link-gap-2026-11-25.md](80.29-competitor-link-gap-2026-11-25.md) | Five nonprofit-accounting peers, Ubersuggest figures only. |
| [80.30-citation-directory-gap-2026-11-25.md](80.30-citation-directory-gap-2026-11-25.md) | Directory check. Unverified items are marked. |

The next current-state file is `80.31`.

## Implementation (`80.60`–`80.89`)

| File | What it is |
| --- | --- |
| [80.60-recommendation-backlog.md](80.60-recommendation-backlog.md) | Priority order and status. |
| [80.61](80.61-bl-01-repair-bill-profile-links.md) through [80.67](80.67-bl-07-optional-template-restoration.md) | One open recommendation each. |
| [80.80-implementation-log.md](80.80-implementation-log.md) | Completed work, including the two live 301s. |

The next recommendation file is `80.68`.

## June 29, 2026 audit

The earlier pass stays with the launch records:

- [30.45-backlink-preservation-audit-2026-06-29.md](../30-current-site/30.45-backlink-preservation-audit-2026-06-29.md)
- [30.46-backlink-preservation-audit-2026-06-29.csv](../30-current-site/30.46-backlink-preservation-audit-2026-06-29.csv)

That pass compared a Search Console linked-pages export with the launch
redirect map and recommended no new redirects. Later audits link to it. They
do not copy it.

The launch redirect list remains
[30.43-pre-publication-launch-redirect-map.csv](../30-current-site/30.43-pre-publication-launch-redirect-map.csv).
GoHighLevel entry notes are in
[30.25-gohighlevel-redirect-implementation-checklist.md](../30-current-site/30.25-gohighlevel-redirect-implementation-checklist.md).

## Conventions

- Files stay flat in this folder. Current state uses `80.10`–`80.49`.
  Implementation uses `80.60`–`80.89`.
- One audit per pull. Do not overwrite an older audit. Save the export as CSV
  beside it, one row per domain, with LF line endings.
- This README is the only extra README in the repository.
- A velu.us URL that has inbound links and returns 404 gets a 301 to the most
  relevant live page, recorded in the broken-target inventory and the log.
- A valuable guide with no live equivalent is a recommendation to restore it.
  Do not send it to the homepage.
- `/wp-content/uploads/` paths cannot be redirected in GoHighLevel. See the
  playbook.

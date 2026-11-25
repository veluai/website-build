# Backlinks

This folder is the durable home for Velu backlink work: dated audits, the
export behind each audit, redirect decisions, outreach and reclamation, disavow
candidates, and the playbook.

The public site is published in GoHighLevel. A commit here does not publish
velu.us. Redirects are URL rules in GoHighLevel, recorded in this folder and
checked on the live domain. The procedure is
[80.10-backlink-playbook.md](80.10-backlink-playbook.md).

## What is already here

| File | What it is |
| --- | --- |
| [80.10-backlink-playbook.md](80.10-backlink-playbook.md) | How to run the next audit, add a redirect, and judge a disavow. |
| [80.20-backlink-audit-2026-11-25.md](80.20-backlink-audit-2026-11-25.md) | November 25, 2026 Ubersuggest audit. |
| [80.21-referring-domains-2026-11-25.csv](80.21-referring-domains-2026-11-25.csv) | Current referring-domain snapshot, 230 rows. |
| [80.22-new-referring-domains-2026-11-25.csv](80.22-new-referring-domains-2026-11-25.csv) | New-domain snapshot, 111 rows. |
| [80.23-lost-referring-domains-2026-11-25.csv](80.23-lost-referring-domains-2026-11-25.csv) | Lost-domain snapshot, 12 rows. |
| [80.30-backlink-actions-2026-11-25.md](80.30-backlink-actions-2026-11-25.md) | Prioritized actions from that audit. |
| [80.40-backlink-redirect-map-2026-11-25.csv](80.40-backlink-redirect-map-2026-11-25.csv) | Old URL, new URL, linking domains, and live result. |
| [80.50-disavow-candidates-2026-11-25.csv](80.50-disavow-candidates-2026-11-25.csv) | SEO-directory campaign. Monitor. Disavow is optional and not uploaded. |

## June 29, 2026 audit

The earlier pass stays where it was filed, with the launch records:

- [30.45-backlink-preservation-audit-2026-06-29.md](../30-current-site/30.45-backlink-preservation-audit-2026-06-29.md)
- [30.46-backlink-preservation-audit-2026-06-29.csv](../30-current-site/30.46-backlink-preservation-audit-2026-06-29.csv)

That pass compared a Search Console linked-pages export with the launch
redirect map. It recommended no new redirects. Later audits link to it. They
do not copy it.

The launch redirect list itself remains
[30.43-pre-publication-launch-redirect-map.csv](../30-current-site/30.43-pre-publication-launch-redirect-map.csv),
with the GoHighLevel entry notes in
[30.25-gohighlevel-redirect-implementation-checklist.md](../30-current-site/30.25-gohighlevel-redirect-implementation-checklist.md).

## Conventions

- One audit per pull. Name it `80.xx-backlink-audit-YYYY-MM-DD.md`. Do not
  overwrite an older audit.
- Save the export beside it as CSV: current referring domains, new domains,
  and lost domains. One row per domain. Do not commit screenshots.
- Take the next free `80.` number from
  [10.10-repo-operating-procedure.md](../10-operations/10.10-repo-operating-procedure.md).
  This README is the only extra README in the repository. Other files in this
  folder stay numbered and flat.
- A velu.us URL that has inbound links and returns 404 gets a 301 to the most
  relevant live page. Record the old URL, the new URL, and the linking domains
  in a dated map in this folder.
- A valuable guide or template with no live equivalent is a restoration
  recommendation. Do not send it to the homepage.
- `/wp-content/uploads/` paths are an exception discovered November 25, 2026:
  GoHighLevel stores a rule and the URL still returns 404. Do not leave a
  rule that does not change the response. See the playbook.

## Next number

`80.10` through `80.50` are in use. The next file is `80.60`.

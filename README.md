# Velu website-build

Source of record for the Velu website's copy, schema, images, standards, and
implementation records. The public site is built and published in **GoHighLevel**.
There is no application build and no automatic deploy. Editing or merging this
repository does not update [velu.us](https://velu.us/).

Humans start here. Agents start at [AGENTS.md](AGENTS.md). Naming rules are in
[10.10-repo-operating-procedure.md](10-operations/10.10-repo-operating-procedure.md).
Repository changes are logged in
[10.20-changelog.md](10-operations/10.20-changelog.md).

## Folder map

| Folder | What it holds |
| --- | --- |
| `10-operations/` | How this repository is run: naming, changelog, and the publish workflow. |
| `20-standards/` | Standing build frameworks (overview, schema, SEO, content, messaging, templates). |
| `30-current-site/` | What is documented as live: site index, shared footer and identity HTML, published records, and launch evidence. |
| `40-pages/` | Live page packages: copy, SEO, JSON-LD, schema plans, image inventories, and reservation CSS. |
| `50-images/` | Published image library. Page subfolders stay so the files remain browsable. |
| `60-source/` | Canonical records the pages and validators read: identity, reviews, case studies, and the reservation map. |
| `70-implementation/` | Roadmap, backlog, and in-progress work that is not live yet. |
| `scripts/` | Offline validators. Kept at the root so the checks can run them. |

Root files that stay unnumbered: `README.md`, `AGENTS.md`, `.gitignore`,
`.github/`, and `scripts/`.

## Numbering

Folders use tens: `10-`, `20-`, `30-`. Files use the folder number, a sequence,
and a readable slug, such as `10.10-repo-operating-procedure.md`. Use steps of
`.10` (`10.10`, `10.20`, `10.30`). When a folder needs more than those steps,
use `.01` (`40.10`, `40.11`). The full rule, including the current number
blocks, is in the operating procedure.

## Current site and later work

Open [30.10-current-site-index.md](30-current-site/30.10-current-site-index.md)
for the documented live pages. Open
[70.10-website-roadmap.md](70-implementation/70.10-website-roadmap.md) and
[70.20-backlog.md](70-implementation/70.20-backlog.md) for work that is not part
of that live set. Appointment page sources are published in `40.93`–`40.98`;
[70.30](70-implementation/70.30-appointment-pages-implementation.md) tracks their
remaining runtime/marketing acceptance. New unpublished sources stay in
`70-implementation/` until live.

How a change gets from this repository into GoHighLevel is
[10.30-publish-to-highlevel.md](10-operations/10.30-publish-to-highlevel.md).
A merge does not publish the site.

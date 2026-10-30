# Velu website

Content and implementation records for [velu.us](https://velu.us/), maintained in
GoHighLevel. Repository changes require a separate GoHighLevel implementation;
this repository does not deploy the website automatically.

## Start here

- [Agent guidance](AGENTS.md)
- [Website overview and governance](docs/1-website-build-overview.md)
- [Schema standard](docs/2-schema-markup-standard.md)
- [SEO framework](docs/7-website-seo-framework.md)
- [Roadmap](docs/11-website-roadmap.md)

## Repository layout

- `docs/`: standards, decisions, audits, and implementation checklists.
- `page-assets/`: page copy, SEO settings, JSON-LD, and image records.
- `assets/`: website images.
- `source-data/`: supporting evidence and approved source records.
- `scripts/`: focused repository validation.

## Business identity update - October 28, 2026

Published and checked on all nine public pages plus the Home alias.
SEO audit recommendation 3 uses one shared footer on all public pages: Velu LLC,
1402 Jones St #1004, Omaha, NE 68102, (402) 578-0622, and info@velu.us.

- [Canonical identity](source-data/business-identity.json)
- [Reusable contact block](page-assets/global-business-identity.html)
- [GoHighLevel footer source](page-assets/global-footer-gohighlevel.html)
- [Implementation status, page checklist, and directory reconciliation](docs/business-identity-implementation.md)

Validate identity consistency and JSON syntax locally:

```sh
python3 scripts/validate-business-identity.py
git diff --check
```

These checks do not establish publication, search indexing, or agreement with
external directories. Consult the implementation record for the current status.

Google follow-up: [sitemap submission, canonical correction, Business Profile verification, LinkedIn update, and completed About indexing request](docs/google-search-follow-up.md).

## Footer navigation - October 29, 2026

Published and verified on all nine public pages plus the Home alias: simple
Services and Explore links beside the contact block; business hours omitted.
Sitemap regenerated and accepted by Google; Home live crawlability passed.
See [the rollout and Google checks](docs/footer-navigation-implementation.md)
for the current prepared, published, and verified status. Source:
[shared footer HTML/CSS](page-assets/global-footer-gohighlevel.html).

About indexing follow-up - October 30: Google accepted Tyler's manual request
into its priority crawl queue. The one-time retry automation has been removed.
Details and evidence summary: [Google follow-up](docs/google-search-follow-up.md).

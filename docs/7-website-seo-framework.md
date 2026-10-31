# Website SEO Framework

## Purpose

This document defines Velu's website SEO framework, including topical authority, keyword strategy, page types, internal linking, schema relationships, image SEO, and future SEO roadmap.

SEO for Velu should reinforce the firm's nonprofit specialization and support qualified opportunities from nonprofit leaders, rather than chasing generic accounting traffic that weakens positioning.

## Scope

This framework applies to:

- Homepage
- Service pages
- Lead magnets
- Resource pages
- Future blog content
- Image SEO
- Schema strategy

This framework does not approve new services, claims, page launches, or schema types by itself. Those decisions must remain aligned with the website build overview, schema standard, service page framework, homepage framework, and Tyler Wilcox's approval.

## Consistent business identity

Every public page must visibly include Velu LLC, the confirmed Omaha street address, phone, and email in its shared footer. Maintain details in [business-identity.json](../source-data/business-identity.json), use [the shared block](../page-assets/global-business-identity.html), and follow [the publishing and directory checklist](business-identity-implementation.md). Keep named organization references consistent with the same entity ID. Do not treat a directory or search result as authority to change the address.

## SEO Objectives

Velu's website SEO objectives are to:

- Build authority around nonprofit financial management.
- Generate qualified nonprofit opportunities.
- Support service page rankings.
- Support educational resource visibility.
- Reinforce Velu's nonprofit specialization.
- Avoid generic CPA positioning.

SEO recommendations should strengthen the website's strategic intent. They should not dilute Velu's nonprofit accounting and advisory positioning.

## Topic Cluster Strategy

Primary topic:

- Nonprofit accounting and advisory services

Supporting topics:

- Nonprofit bookkeeping
- Outsourced nonprofit accounting
- Nonprofit client advisory services
- Grant advisory and compliance
- Fund accounting
- Financial reporting
- Budgeting
- Forecasting
- Board reporting
- Grant readiness
- Nonprofit financial sustainability

Future topic clusters should be added only when they support real Velu services, approved educational resources, or approved website strategy.

## Page Type Strategy

Homepage:

- Establish firm positioning and topical authority.

Service pages:

- Capture high-intent service searches.

Lead magnets:

- Educate early-stage nonprofit leaders and support authority building.

Resource pages:

- Answer practical nonprofit financial management questions.

Future blog content:

- Build topical depth around approved clusters.

Page type decisions should connect to a clear user intent and should support service architecture rather than creating disconnected content.

## Keyword Philosophy

Prioritize nonprofit-specific keywords when accurate.

Preferred language:

- nonprofit accounting
- nonprofit bookkeeping
- outsourced accounting for nonprofits
- nonprofit advisory services
- nonprofit CFO advisory
- fund accounting
- grant compliance
- financial reporting for nonprofits
- nonprofit budgeting
- nonprofit forecasting

Avoid generic-only language when nonprofit-specific language is better. Generic accounting language may be used where it helps comprehension, but it should not replace the nonprofit-specific framing that defines Velu's positioning.

## Internal Linking Philosophy

- Homepage links to service pages.
- Service pages link to related services and get-started CTA.
- Lead magnets link to relevant services.
- Resource pages link to relevant services and lead magnets.
- Future blogs should support service and resource clusters.

Internal links should clarify relationships between outcomes, services, educational resources, and conversion paths. Links should not be added merely to increase link count.

## Shared footer navigation

Approved October 29, 2026: keep the full business identity beside four Services
links and two Explore links. Services are Outsourced Accounting, Client Advisory
Services, Grant Advisory & Compliance, and Nonprofit Tax Services. Explore links
to About Velu and Get Started. The business name links to Home; Privacy Policy
and Terms remain in a smaller legal row. Use the direct canonical destinations
in [the footer source](../page-assets/global-footer-gohighlevel.html).

Keep labels short and descriptive, links as ordinary HTML anchors, and the
mobile layout stacked. Do not add business hours to the footer, duplicate
keyword links, or links to planned pages. Simplicity takes priority over adding
more sitewide links. Track publication, sitemap regeneration, and Search Console
results in [the implementation record](footer-navigation-implementation.md).

## Schema SEO Relationship

Schema standards are governed by:

- [Schema Markup Standard](2-schema-markup-standard.md)

Schema supports SEO by clarifying:

- Organization identity
- Services
- Reviews
- Service components
- Educational resources
- Local presence
- Conversion actions

Schema should reflect visible or approved content. It should not be used to manufacture SEO signals.

## Image SEO Relationship

Image SEO standards are governed by:

- [Image SEO Alt Text Standard](6-image-seo-alt-text-standard.md)

Image SEO should support accessibility, page relevance, and nonprofit-specific context. Alt text should describe the actual image before attempting to reinforce search terms.

## GoHighLevel Meta Description Length Standard

GoHighLevel meta descriptions must remain under 155 characters.

- Character count includes spaces and punctuation.
- Target range should generally be 120-150 characters.
- Never approve or instruct entry of a description without counting it first.
- Repository SEO records should include the final character count.
- If a description exceeds 154 characters, revise it before GHL entry.
- Do not mark a meta description as entered or confirmed until the exact final version is saved in GHL.
- This limit applies to all current and future page SEO records.

Implementation checklist:

1. Draft the description.
2. Count all characters, including spaces and punctuation.
3. Confirm the count is 154 or fewer.
4. Record the count in the page SEO file.
5. Enter the exact approved version in GHL.
6. Confirm the saved value matches the repository exactly.
7. Keep live verification pending until publication.

## Future SEO Roadmap

Future clusters include:

- Grant advisory and compliance
- Starting a nonprofit
- Nonprofit financial foundation
- Nonprofit board reporting
- Nonprofit budgeting
- Nonprofit fund accounting
- Grant readiness
- Restricted fund tracking
- Nonprofit financial sustainability

These clusters should remain planned or proposed until page strategy, content scope, and approval status are clear.

## Future AI Agent Instructions

- Do not chase generic CPA keywords if they weaken nonprofit positioning.
- Build pages around real Velu services and expertise.
- Avoid creating unsupported claims.
- Connect SEO recommendations to page strategy and service architecture.
- Update [Page Schema Inventory](3-page-schema-inventory.md) when schema work is completed.
- Update this SEO framework when new topic clusters are approved.
- Distinguish approved SEO standards from proposed keyword or content opportunities.

## Related Documents

- [Website Build Overview](1-website-build-overview.md)
- [Schema Markup Standard](2-schema-markup-standard.md)
- [Page Schema Inventory](3-page-schema-inventory.md)
- [Service Page Framework](4-service-page-framework.md)
- [Homepage Framework](5-homepage-framework.md)
- [Image SEO Alt Text Standard](6-image-seo-alt-text-standard.md)
- [Velu Service Outcome Framework](12-velu-service-outcome-framework.md)
- [Website Messaging Framework](13-website-messaging-framework.md)

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.0 | Initial website SEO framework created for Velu topic clusters, page type strategy, keyword guidance, internal linking, schema, image SEO, and future roadmap. | Tyler Wilcox |

## Audit-tool decisions - October 30, 2026

Tyler approved preserving the concise Get Started conversion page, readable
`/about-us` and `/get-started` URLs, and accurate short legal-page titles despite
Ubersuggest flags. Do not pad copy, rename URLs, add meta keywords, or lengthen
legal titles merely to satisfy these tool thresholds. Google does not prescribe
a minimum word count, does not use meta keywords, and recommends concise,
descriptive titles. Public-email markup uses Cloudflare's per-email exclusion;
validate delivered HTML separately from browser decoding. Decisions, sources,
and the approved calendar-label change are in [the audit record](ubersuggest-audit-2026-10-30.md).

## Mobile layout stability - October 30, 2026

The image-space reservation phase is published on all nine pages. Repeat mobile
Home lab CLS improved from 0.538 to 0.158 in two corrected final runs, but remains above the good 0.10
target; Outsourced Accounting still measured 0.262. Do not describe the entire
mobile issue as fixed. Font-associated text movement and an unresolved body-level
shift require a separately reviewed follow-up. Distinguish fresh Lighthouse
tests from Ubersuggest's older visitor-window metric and retain repeated results,
including less favorable runs. See [the implementation and measurements](mobile-image-layout-stability-2026-10-30.md).

The outstanding work is **High priority, open and deferred** in the
[roadmap's Active follow-up](11-website-roadmap.md#active). No investigation is
currently underway; surface it at the next substantive repository review or
SEO/performance gap analysis. The slower LCP cause has not been established.

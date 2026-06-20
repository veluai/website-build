# Service Page Framework

## Purpose

This document defines the standard architecture, messaging pattern, conversion structure, SEO requirements, and schema relationship for Velu service pages.

Service pages should help qualified nonprofit prospects understand the outcome Velu helps them achieve, the capability required to achieve it, the service Velu provides, and the activities that support the service.

## Scope

This framework applies to public Velu service pages, including:

- Outsourced Accounting Services
- Client Advisory Services
- Future Grant Advisory & Compliance page
- Future service pages

This framework does not define internal service delivery, pricing, staffing, client onboarding, CRM workflows, or proposal language except where those topics affect public website positioning.

## Service Page Philosophy

Service pages should lead with nonprofit leadership outcomes before deliverables.

The page should connect:

Outcome -> Capability -> Service -> Activity

Example:

Financial Foundation -> Reliable financial systems -> Outsourced Accounting -> Bookkeeping, reconciliations, reporting

This structure keeps Velu's service pages focused on the leadership value nonprofit decision-makers are seeking. Deliverables should support the outcome; they should not replace the outcome as the main message.

Service pages should also reinforce Velu's nonprofit specialization. They should not read like generic accounting, bookkeeping, CPA, or consulting service pages.

## Standard Service Page Structure

Velu service pages should normally follow this structure:

1. Hero section
2. Outcome framework connection
3. Nonprofit leader problem section
4. How Velu helps
5. Service pillars
6. Benefits and outcomes
7. Reviews
8. Primary CTA
9. Schema markup

The structure may be adapted when a page has a clearly approved reason, but future service pages should preserve the same general progression from outcome to service detail to conversion.

## Hero Section Standard

Each service page hero should include:

- Outcome-focused headline
- Nonprofit-specific supporting copy
- Primary CTA to https://velu.us/get-started/
- Velu Financial Growth Framework hero visual when the page maps to one of the approved outcome pillars
- Clear connection to the relevant outcome pillar

Service pages should use the Velu Financial Growth Framework as the primary hero visual when the page maps to one of the approved outcome pillars. The highlighted pillar should match the page's primary outcome.

Current framework hero mapping:

- Outsourced Accounting Services -> Pillar 1: Financial Foundation
- Client Advisory Services -> Pillar 2: Program-Finance Connection
- Grant Advisory & Compliance -> Pillar 3: Funding Confidence
- Future Sustainable Growth / planning-related page -> Pillar 4: Sustainable Growth

The framework hero image should reinforce the page's role within the broader Velu service journey. Service-specific support images may still be used below the hero section for pillar cards, benefit sections, or explanatory content.

Implementation note:

For Grant Advisory & Compliance, the hero image should be the Velu Financial Growth Framework with Pillar 3, Funding Confidence, highlighted.

The hero should make the service's nonprofit relevance immediately clear. It should not rely on generic accounting copy or broad business language when nonprofit-specific language is available and accurate.

## Outcome Pillar Alignment

Current service-page alignment:

| Service Page | Primary Outcome | Supporting Outcome |
| --- | --- | --- |
| Outsourced Accounting Services | Financial Foundation | Sustainable Growth |
| Client Advisory Services | Program-Finance Connection | Sustainable Growth |
| Grant Advisory & Compliance | Funding Confidence | Sustainable Growth |

Future service pages should be mapped to the Velu Service Outcome Framework before copy, schema, imagery, or SEO recommendations are treated as final.

## Service Pillar Standard

Current service pages use a four-pillar model.

Outsourced Accounting Services pillars:

- Financial Reporting
- Fund Accounting
- Financial Visibility
- Accounting Operations

Client Advisory Services pillars:

- Budgeting & Financial Planning
- Budget Performance Analysis
- Forecasting & Financial Visibility
- Board & Leadership Reporting

Future service pages should use 3-5 clear service pillars unless a different structure is approved. Pillars should be visible on the page before they are used in schema, internal documentation, image alt text, or SEO recommendations.

## Review Standard

Service pages may use the approved 12 nonprofit-focused review set only when those reviews are visible on the page.

Review markup must reflect actual review content. Reviews should support the page's nonprofit positioning and should not be added only for search enhancement.

## CTA Standard

Primary CTA:

https://velu.us/get-started/

Service pages should avoid competing CTAs unless approved. Secondary links may support education or related-service discovery, but they should not distract qualified prospects from the primary get-started conversion path.

## Schema Connection

Service page schema standards are governed by:

- [Schema Markup Standard](2-schema-markup-standard.md)
- [Page Schema Inventory](3-page-schema-inventory.md)

Service pages should normally use:

- `WebPage`
- `Service`
- `BreadcrumbList`
- `OfferCatalog`
- `AggregateRating`
- `Review`
- `ScheduleAction`
- `AccountingService` organization reference

Schema must match visible or approved page content. Service pillars should not appear in `OfferCatalog` unless the service component is described on the page or approved for that page.

## Future AI Agent Instructions

- Do not create service promises not reflected in the page.
- Do not add service pillars that are not shown on the page or approved.
- Maintain nonprofit-specific positioning.
- Use the service outcome framework to guide page structure.
- Keep service pages focused on qualified nonprofit prospects.
- Distinguish between completed service pages, planned service pages, and proposed future pages.
- Update the page schema inventory when service-page schema work is completed.

## Related Documents

- [Website Build Overview](1-website-build-overview.md)
- [Schema Markup Standard](2-schema-markup-standard.md)
- [Page Schema Inventory](3-page-schema-inventory.md)
- [Velu Service Outcome Framework](12-velu-service-outcome-framework.md)
- [Website Messaging Framework](13-website-messaging-framework.md)

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.1 | Documented service-page Financial Growth Framework hero image standard and Grant Advisory & Compliance Pillar 3 hero usage. | Tyler Wilcox |
| 2026-06-20 | 1.0 | Initial service page framework created for Velu website service-page architecture, messaging, CTA, SEO, and schema alignment. | Tyler Wilcox |

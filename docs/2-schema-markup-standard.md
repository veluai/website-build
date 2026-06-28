# Schema Markup Standard

## Purpose

This document establishes Velu's official schema markup standards for the replacement public website.

Schema markup should help search engines understand Velu's organization, nonprofit accounting and advisory services, page relationships, images, and conversion actions. Schema must reflect actual page content and should not be used to manufacture signals that are not supported by the website.

## Scope

This standard applies to all public website pages.

It governs schema for:

- Home page global entities
- Service pages
- Utility pages
- Organization references
- Offer catalogs
- Breadcrumbs
- Images
- Local SEO data
- Conversion actions
- Review and rating exclusions

## Approved Schema Types

Home:

- `WebSite`
- `WebPage`
- `AccountingService`

About:

- `AboutPage`
- `ImageObject`
- `BreadcrumbList`
- `Person`
- `ScheduleAction`

Get Started:

- `ContactPage`
- `ImageObject`
- `BreadcrumbList`
- `ScheduleAction`

Current service pages:

- `WebPage`
- `ImageObject`
- `BreadcrumbList`
- `Service`
- `ScheduleAction`

Embedded supporting types:

- `OfferCatalog`
- `Offer`
- `Audience`
- `ImageObject`
- `PostalAddress`
- `GeoCoordinates`
- `ContactPoint`

Additional schema types require approval before becoming part of the standard.

## Implementation Rules for Future AI Agents

- Schema must match visible or approved page content.
- Use root-domain Home schema at `https://velu.us/`.
- Use full canonical URLs in `@id`, `url`, breadcrumb, provider, and `sameAs` fields.
- Use the same global entity IDs across pages:
  - `https://velu.us/#website`
  - `https://velu.us/#organization`
- Service page `@id` format should be: `https://velu.us/[path]#service`.
- `WebPage` `@id` format should be: `https://velu.us/[path]#webpage`.
- Breadcrumb `@id` format should be: `https://velu.us/[path]#breadcrumb`.
- Do not add offer catalog items unless the service component is described on the page or approved for that page.
- Do not add URLs for pages that do not yet exist unless clearly marked as planned and not used in production schema.
- Validate JSON-LD before publishing.

## Global Entity Ownership

The Home page defines the full global entities for the replacement website:

- `https://velu.us/#website`
- `https://velu.us/#organization`

The Home page defines the organization entity as `AccountingService`.

Service pages and utility pages should reference the global IDs rather than duplicating the full `WebSite`, `Organization`, `AccountingService`, or `ProfessionalService` entities unless a documented exception is approved.

## Standard Organization Data

| Field | Approved Value |
| --- | --- |
| Name | Velu |
| Legal name | Velu LLC |
| Organization schema type | `AccountingService` |
| Website | https://velu.us |
| Address | 1402 Jones St #1004, Omaha, NE 68102, US |
| Telephone | +1-402-578-0622 |
| Email | info@velu.us |
| Opening hours | Monday-Friday, 09:00-17:00 |
| Latitude | 41.2537337 |
| Longitude | -95.9349443 |
| Primary conversion URL | https://velu.us/get-started |
| LinkedIn | https://www.linkedin.com/company/velucpa/ |
| Google Maps | https://www.google.com/maps/place/Velu+LLC,+1402+Jones+St+%231004,+Omaha,+NE+68102 |
| QuickBooks ProAdvisor | https://proadvisor.intuit.com/app/accountant/search?searchId=tyler-wilcox77 |
| Logo URL | https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a224bccfc95b245497d57f8.jpg |

## Review and Rating Policy

Visible reviews may remain on pages as social proof.

Current page-level JSON-LD should exclude by default:

- `Review`
- `AggregateRating`
- `ratingValue`
- `reviewCount`

Broad Velu testimonials should not be attached to a page-specific `Service` entity because they are not all specific to an individual service page.

An exception requires explicit approval and page-specific evidence that the reviews are visibly represented, relevant to the marked-up entity, and appropriate for structured data.

Visible review records remain documented separately. The authoritative visible-review inventory is:

`page-assets/home-page-review-inventory.md`

## Page Schema Pattern Summary

Home:

- `WebSite`
- `WebPage`
- `AccountingService`

About:

- `AboutPage`
- `ImageObject`
- `BreadcrumbList`
- `Person`
- `ScheduleAction`

Get Started:

- `ContactPage`
- `ImageObject`
- `BreadcrumbList`
- `ScheduleAction`

Current service pages:

- `WebPage`
- `ImageObject`
- `BreadcrumbList`
- `Service`
- `ScheduleAction`
- Organization reference to `https://velu.us/#organization`

The page-specific `Service` may contain an embedded `OfferCatalog` when service components are clearly described on the page.

## Known Schema Implementations

### Home

- URL: https://velu.us/
- Primary schema purpose: Establish Velu as a nonprofit accounting and advisory firm and define global website and organization entities.
- Current top-level entities:
  - `WebSite`
  - `WebPage`
  - `AccountingService`
- Review markup: Excluded
- AggregateRating markup: Excluded

### Outsourced Accounting Services

- URL: https://velu.us/services/nonprofit-outsourced-accounting-services
- Primary schema purpose: Support nonprofit outsourced accounting service authority.
- Current top-level entities:
  - `WebPage`
  - `ImageObject`
  - `BreadcrumbList`
  - `Service`
  - `ScheduleAction`
- Offer catalog items:
  - Financial Reporting
  - Fund Accounting
  - Financial Visibility
  - Accounting Operations
- Review markup: Excluded
- AggregateRating markup: Excluded

### Grant Advisory & Compliance

- URL: https://velu.us/services/nonprofit-grant-advisory-compliance-services
- Current top-level entities:
  - `WebPage`
  - `ImageObject`
  - `BreadcrumbList`
  - `Service`
  - `ScheduleAction`
- Review markup: Excluded
- AggregateRating markup: Excluded

### Nonprofit Tax Services

- URL: https://velu.us/services/nonprofit-tax-services
- Current top-level entities:
  - `WebPage`
  - `ImageObject`
  - `BreadcrumbList`
  - `Service`
  - `ScheduleAction`
- Review markup: Excluded
- AggregateRating markup: Excluded

### Client Advisory Services

- URL: https://velu.us/services/nonprofit-client-advisory-services
- Current page-specific backfill is incomplete.
- Historical/source schema exists under `source-data`.
- Do not treat the source schema as current implementation.
- Do not copy `Review` or `AggregateRating` markup from the historical source.

## Organization Schema Standard

Velu organization schema should use:

- `AccountingService`

Reason:

`AccountingService` provides stronger topical relevance than `ProfessionalService` given Velu's positioning as a nonprofit accounting and advisory firm.

Home owns the full organization entity. Other pages should reference `https://velu.us/#organization` unless a documented exception is approved.

Organization schema should describe Velu as a nonprofit accounting and advisory firm. It should not describe the firm as a generic CPA firm unless that positioning is explicitly approved and reflected in the page content.

## Homepage Schema Standard

Homepage schema should establish the public understanding of Velu's identity, services, and conversion action.

Required top-level components:

- `WebSite`
- `WebPage`
- `AccountingService`

The Home page may include an embedded or referenced offer catalog where current core service areas are shown on the page.

The Home page currently excludes `Review` and `AggregateRating` markup, even when reviews are visible as social proof.

The discovery call action should point to the primary conversion action:

https://velu.us/get-started

## Service Page Schema Standard

Service page schema should clarify the specific service being described while tying the page back to Velu's organization entity and conversion path.

Required top-level components:

- `WebPage`
- `ImageObject`
- `BreadcrumbList`
- `Service`
- `ScheduleAction`

The `Service` schema should describe the page's specific nonprofit accounting, advisory, grant, or tax service. The `OfferCatalog` should identify service components that are actually described on the page.

Current service-page JSON-LD excludes `Review` and `AggregateRating` markup by default.

Service page schema should use nonprofit-focused language where appropriate, including nonprofit accounting, nonprofit bookkeeping, outsourced accounting, advisory services, budgeting, forecasting, reporting, grant compliance, financial stewardship, nonprofit tax compliance, and nonprofit leadership support.

## OfferCatalog Standard

Service pages should use `OfferCatalog` whenever service components are clearly defined.

The `OfferCatalog` should:

- Reflect the service components shown on the page.
- Use nonprofit-specific service descriptions where appropriate.
- Avoid listing services or packages not represented in page content.
- Support the page's service positioning without overstating scope.

Homepage offer catalogs may summarize current core service areas. Service page offer catalogs should be more specific to that page's service.

## Breadcrumb Standard

Breadcrumb schema should:

- Match the page URL and real site hierarchy.
- Use accurate page names.
- Include the homepage as the first item.
- Include the current page as the final item.
- Avoid breadcrumbs that imply nonexistent pages or unapproved site sections.

Service pages currently use:

1. Home
2. Current service page

Do not include `https://velu.us/services/` as a breadcrumb item unless a real Services landing page is later created.

The Home page does not require breadcrumb schema.

## ImageObject Standard

Schema should use actual hosted image URLs.

Image schema and image references should:

- Use exact hosted URLs.
- Use exact width and height from the approved image inventory.
- Prefer the social-sharing image as `primaryImageOfPage` where a page-specific social image exists.
- Limit supporting images to meaningful, approved images.
- Avoid placeholder images.
- Be verified before the page is marked complete in the schema inventory.

Metadata-only social images do not require webpage alt text unless visibly rendered on the page.

Images may use `ImageObject` when additional metadata is useful for search understanding.

## Local SEO Standard

Local SEO schema should include accurate business and location signals when they are published and verified.

Include on the Home organization entity where applicable:

- Address
- `GeoCoordinates`
- `ContactPoint`
- Opening hours
- Maps reference

Local SEO data must be consistent with the live website, public business profiles, and any approved firm records. Geographic schema should support local relevance without overstating service area, office presence, or physical availability.

## Lead Magnet and Educational Resource Standard

Educational resources may use `CreativeWork` schema only when a real resource is present in the page experience and explicitly approved for markup.

Lead magnet schema should:

- Describe the actual resource being offered.
- Use the correct page URL or resource URL.
- Connect the resource to the page where it appears.
- Support nonprofit education and authority building.
- Avoid marking up a lead magnet that is not present in the page experience.

## ScheduleAction Standard

Discovery call and consultation calls to action may use `ScheduleAction`.

Approved action name:

`Book Your Discovery Call`

Approved target URL:

https://velu.us/get-started

`ScheduleAction` should be used for real scheduling or get-started actions that a visitor can take from the page. It should not be used for pages where no scheduling or inquiry action exists.

Do not invent duration, availability, pricing, or guarantees in schema.

## JSON-LD Format Standard

Page schema files should be:

- Pure JSON
- Free of `<script>` tags
- Free of Markdown fences
- Valid JSON
- Free of comments
- Consistent with the canonical URL
- Free of empty arrays or empty placeholder properties
- Free of duplicate full global entities
- Free of stale URLs

The dedicated GoHighLevel Schema Markup JSON View accepts pure JSON.

Page-level schemas should be validated in GoHighLevel before publication.

Live source validation, Schema.org validation, and Google Rich Results testing remain post-publication tasks.

## Status Terminology

Use:

- Drafted
- Generated
- Entered in GoHighLevel
- GoHighLevel validation passed
- Pending publication
- Pending live verification

Do not use unless separately confirmed:

- Live
- Indexed
- Verified in production

## Validation Standard

All schema should be validated before publication.

Validation should confirm:

- JSON-LD syntax is valid.
- Required fields are present.
- Schema types match the page purpose.
- Page-level schema references the global IDs correctly.
- Offer catalogs match visible service components.
- Breadcrumbs use real pages only.
- Review and AggregateRating markup are excluded unless an approved exception exists.
- Image URLs and dimensions match approved image records.
- Conversion action URLs resolve.
- Local SEO data is accurate where used.

A page should not be marked complete in the schema inventory until local validation and image verification are complete. Publication, live source validation, Schema.org validation, and Google Rich Results testing remain separate post-publication tasks.

## Major Decisions

| Date | Decision | Rationale | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | `AccountingService` selected over `ProfessionalService`. | Stronger topical relevance for Velu's nonprofit accounting and advisory positioning. | Tyler Wilcox |
| 2026-06-20 | Homepage positioned around nonprofit accounting and advisory services. | Supports firm specialization and avoids generic CPA positioning. | Tyler Wilcox |
| 2026-06-20 | Service pages use `OfferCatalog`. | Service components are clearly defined and should be understandable to search engines. | Tyler Wilcox |
| 2026-06-20 | Discovery call CTA uses `ScheduleAction`. | The primary conversion action is a get-started or discovery-call path. | Tyler Wilcox |
| 2026-06-20 | Lead magnets may use `CreativeWork` only when present and approved. | Educational resources support nonprofit authority building when real resources are present. | Tyler Wilcox |
| 2026-06-20 | `GeoCoordinates` included for local relevance. | Geographic data supports local SEO when address and location details are accurate. | Tyler Wilcox |

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.1 | Added future AI implementation rules, standard organization data, review set guidance, page patterns, and known schema implementation details. | Tyler Wilcox |
| 2026-06-20 | 1.0 | Initial schema markup standard created for Velu public website schema governance. | Tyler Wilcox |

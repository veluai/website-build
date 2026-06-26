# Schema Markup Standard

## Purpose

This document establishes Velu's official schema markup standards for the public website.

Schema markup should help search engines understand Velu's organization, nonprofit accounting and advisory services, educational resources, reviews, geographic presence, and conversion actions. Schema must reflect actual page content and should not be used to manufacture signals that are not supported by the website.

## Scope

This standard applies to all public website pages.

It governs schema for:

- Homepage
- Service pages
- Organization references
- Reviews
- Offer catalogs
- Breadcrumbs
- Images
- Local SEO data
- Lead magnets
- Educational resources
- Conversion actions

## Approved Schema Types

Homepage:

- `WebSite`
- `WebPage`
- `AccountingService`
- `OfferCatalog`
- `AggregateRating`
- `CreativeWork`
- `ScheduleAction`

Service pages:

- `WebPage`
- `Service`
- `OfferCatalog`
- `BreadcrumbList`
- `AggregateRating`
- `Review`
- `ScheduleAction`

Organization:

- `AccountingService`

Supporting types:

- `PostalAddress`
- `GeoCoordinates`
- `ContactPoint`
- `Offer`
- `Audience`
- `ImageObject`

Additional schema types require approval before becoming part of the standard.

## Implementation Rules for Future AI Agents

- Schema must match visible or approved page content.
- Do not add reviews unless they are visible on the page.
- Do not add offer catalog items unless the service component is described on the page or approved for that page.
- Do not add URLs for pages that do not yet exist unless clearly marked as planned and not used in production schema.
- Use root-domain homepage schema at https://velu.us/.
- Use full canonical URLs in `@id`, `url`, breadcrumb, provider, and `sameAs` fields.
- Use the same organization `@id` across pages: https://velu.us/#organization.
- Service page `@id` format should be: https://velu.us/[path]#service.
- `WebPage` `@id` format should be: https://velu.us/[path]#webpage.
- Breadcrumb `@id` format should be: https://velu.us/[path]#breadcrumb.
- Validate JSON-LD before publishing.

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
| Primary conversion URL | https://velu.us/get-started/ |
| LinkedIn | https://www.linkedin.com/company/velucpa/ |
| Google Maps | https://www.google.com/maps/place/Velu+LLC,+1402+Jones+St+%231004,+Omaha,+NE+68102 |
| QuickBooks ProAdvisor | https://proadvisor.intuit.com/app/accountant/search?searchId=tyler-wilcox77 |
| Logo URL | https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a224bccfc95b245497d57f8.jpg |

## Standard Review Set

The current approved service-page and homepage review set uses 12 nonprofit-focused reviews.

- The review set should remain consistent across pages where the same review carousel is visible.
- Review schema should not include reviews that are not displayed on the page.
- Review schema should not include reviews unrelated to the page's positioning unless intentionally approved.
- Current aggregate rating: 5
- Current review count: 12

## Page Schema Pattern Summary

Homepage:

- `WebSite`
- `WebPage`
- `AccountingService`
- `OfferCatalog`
- `AggregateRating`
- `CreativeWork`
- `ScheduleAction`

Service Page:

- `WebPage`
- `Service`
- `BreadcrumbList`
- `OfferCatalog`
- `AggregateRating`
- `Review`
- `ScheduleAction`
- Organization reference

## Known Schema Implementations

### Home

- URL: https://velu.us/
- Primary schema purpose: Establish Velu as a nonprofit accounting and advisory firm.
- Lead magnet: The First Steps to Start a Nonprofit.

### Outsourced Accounting Services

- URL: https://velu.us/services/nonprofit-outsourced-accounting-services
- Primary schema purpose: Support nonprofit outsourced accounting service authority.
- Offer catalog pillars:
  - Financial Reporting
  - Fund Accounting
  - Financial Visibility
  - Accounting Operations

### Client Advisory Services

- URL: https://velu.us/services/nonprofit-client-advisory-services
- Primary schema purpose: Support nonprofit advisory services authority.
- Offer catalog pillars:
  - Budgeting & Financial Planning
  - Budget Performance Analysis
  - Forecasting & Financial Visibility
  - Board & Leadership Reporting

## Organization Schema Standard

Velu organization schema should use:

- `AccountingService`

Reason:

`AccountingService` provides stronger topical relevance than `ProfessionalService` given Velu's positioning as a nonprofit accounting and advisory firm.

Required fields:

- `@context`
- `@type`
- `@id`
- `name`
- `url`
- `description`
- `image` or `logo` where available
- `telephone` where published
- `address`
- `geo`
- `contactPoint`
- `openingHoursSpecification` or published opening hours where available
- `areaServed`
- `serviceType` or equivalent service descriptors
- `sameAs` where official public profiles are available

Organization schema should describe Velu as a nonprofit accounting and advisory firm. It should not describe the firm as a generic CPA firm unless that positioning is explicitly approved and reflected in the page content.

## Homepage Schema Standard

Homepage schema should establish the strongest public understanding of Velu's identity, services, reputation signals, educational resources, and conversion action.

Required components:

- `WebSite`
- `WebPage`
- Organization reference using `AccountingService`
- `OfferCatalog`
- Reviews or `AggregateRating` when supported by visible page content
- Lead magnet support using `CreativeWork` when a real educational resource is present
- Discovery call action using `ScheduleAction`

Homepage schema should include an organization reference that connects the page to Velu's `AccountingService` entity. The `OfferCatalog` should describe current core service areas shown on the page, including outsourced accounting, advisory services, and grant advisory or compliance support where represented in live content.

Reviews and ratings must be based on actual review content visible on the homepage. Lead magnet schema may support the current educational resource, "The First Steps to Start a Nonprofit," when the resource is present and available through the page experience.

The discovery call action should point to the primary conversion action:

https://velu.us/get-started/

## Service Page Schema Standard

Service page schema should clarify the specific service being described while tying the page back to Velu's organization entity and conversion path.

Required components:

- `WebPage`
- `Service`
- `OfferCatalog`
- `BreadcrumbList`
- Reviews or `AggregateRating` when supported by visible page content
- `ScheduleAction`

The `Service` schema should describe the page's specific nonprofit accounting or advisory service. The `OfferCatalog` should identify service components that are actually described on the page. Breadcrumb schema should match the page's visible or logical site hierarchy.

Current known complete service pages:

- Outsourced Accounting Services
- Client Advisory Services

Service page schema should use nonprofit-focused language where appropriate, including nonprofit accounting, nonprofit bookkeeping, outsourced accounting, advisory services, budgeting, forecasting, reporting, grant compliance, financial stewardship, and nonprofit leadership support.

## Review Schema Standard

Use nonprofit-focused reviews whenever possible.

Review schema requirements:

- Reviews must appear on the page.
- Review markup must reflect actual review content.
- Review authors, ratings, and review text must not be invented.
- Review content should be relevant to Velu's nonprofit accounting and advisory positioning when possible.
- Aggregate ratings must be supported by real rating data.

Reviews should not be added to schema solely for search enhancement if the same review content is not visible to users on the page.

## OfferCatalog Standard

Service pages should use `OfferCatalog` whenever service components are clearly defined.

The `OfferCatalog` should:

- Reflect the service components shown on the page.
- Use nonprofit-specific service descriptions where appropriate.
- Avoid listing services or packages not represented in page content.
- Support the page's service positioning without overstating scope.

Homepage offer catalogs may summarize current core service areas. Service page offer catalogs should be more specific to that page's service.

## Breadcrumb Standard

Service pages should use `BreadcrumbList`.

Breadcrumb schema should:

- Match the page URL and site hierarchy.
- Use accurate page names.
- Include the homepage as the first item.
- Include the current service page as the final item.
- Avoid breadcrumbs that imply nonexistent pages or unapproved site sections.

The homepage does not require breadcrumb schema.

## Image Standard

Schema should use actual image URLs.

Image schema and image references should:

- Reference homepage, service page, and supporting imagery where applicable.
- Use published URLs that resolve successfully.
- Describe the actual image and page context.
- Avoid placeholder images.
- Be verified before the page is marked complete in the schema inventory.

Images may use `ImageObject` when additional metadata is useful for search understanding.

## Local SEO Standard

Local SEO schema should include accurate business and location signals when they are published and verified.

Include:

- Address
- `GeoCoordinates`
- `ContactPoint`
- Opening hours
- Maps reference

Local SEO data must be consistent with the live website, public business profiles, and any approved firm records. Geographic schema should support local relevance without overstating service area, office presence, or physical availability.

## Lead Magnet Standard

Educational resources may use `CreativeWork` schema.

Current implementation:

- The First Steps to Start a Nonprofit

Lead magnet schema should:

- Describe the actual resource being offered.
- Use the correct page URL or resource URL.
- Connect the resource to the page where it appears.
- Support nonprofit education and authority building.
- Avoid marking up a lead magnet that is not present in the page experience.

## ScheduleAction Standard

Discovery call and consultation calls to action may use `ScheduleAction`.

The preferred target URL is:

https://velu.us/get-started/

`ScheduleAction` should be used for real scheduling or get-started actions that a visitor can take from the page. It should not be used for pages where no scheduling or inquiry action exists.

## Validation Standard

All schema should be validated before publication.

Validation should confirm:

- JSON-LD syntax is valid.
- Required fields are present.
- Schema types match the page purpose.
- Review markup matches visible content.
- Offer catalogs match visible service components.
- Image URLs resolve.
- Conversion action URLs resolve.
- Local SEO data is accurate.

A page should not be marked complete in the schema inventory until validation and image verification are complete.

## Major Decisions

| Date | Decision | Rationale | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | `AccountingService` selected over `ProfessionalService`. | Stronger topical relevance for Velu's nonprofit accounting and advisory positioning. | Tyler Wilcox |
| 2026-06-20 | Homepage positioned around nonprofit accounting and advisory services. | Supports firm specialization and avoids generic CPA positioning. | Tyler Wilcox |
| 2026-06-20 | Service pages use `OfferCatalog`. | Service components are clearly defined and should be understandable to search engines. | Tyler Wilcox |
| 2026-06-20 | Service pages use nonprofit-focused reviews. | Review signals should reinforce the audience and service positioning. | Tyler Wilcox |
| 2026-06-20 | Discovery call CTA uses `ScheduleAction`. | The primary conversion action is a get-started or discovery-call path. | Tyler Wilcox |
| 2026-06-20 | Lead magnets may use `CreativeWork`. | Educational resources support nonprofit authority building when real resources are present. | Tyler Wilcox |
| 2026-06-20 | `GeoCoordinates` included for local relevance. | Geographic data supports local SEO when address and location details are accurate. | Tyler Wilcox |

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.1 | Added future AI implementation rules, standard organization data, review set guidance, page patterns, and known schema implementation details. | Tyler Wilcox |
| 2026-06-20 | 1.0 | Initial schema markup standard created for Velu public website schema governance. | Tyler Wilcox |

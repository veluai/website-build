# Outsourced Accounting Page Schema Plan

## Page Identity

- Page name: Outsourced Accounting
- Canonical URL: `https://velu.us/services/nonprofit-outsourced-accounting-services`
- SEO title: `Velu | Omaha-Based Nonprofit Outsourced Accounting Services`
- Visible H1: `Outsourced Accounting for Nonprofits`
- Primary CTA: `Book Your Discovery Call`
- CTA URL: `https://velu.us/get-started`

## Deployment Context

- Replacement GHL site is not published.
- Old site remains live.
- The page references the global entities defined by the Home page:
  - `https://velu.us/#website`
  - `https://velu.us/#organization`
- The page must not duplicate a full WebSite or AccountingService organization entity.
- Publication and live source verification remain pending. Schema.org Validator retest has passed with 0 errors and 0 warnings.

## Final Top-Level Schema Structure

Exactly five top-level graph entities:

1. WebPage
2. ImageObject
3. BreadcrumbList
4. Service
5. ScheduleAction

The Service contains an embedded OfferCatalog with exactly four Offer items:

1. Financial Reporting
2. Fund Accounting
3. Financial Visibility
4. Accounting Operations

## Entity IDs

WebPage:

`https://velu.us/services/nonprofit-outsourced-accounting-services#webpage`

Primary ImageObject:

`https://velu.us/services/nonprofit-outsourced-accounting-services#primaryimage`

BreadcrumbList:

`https://velu.us/services/nonprofit-outsourced-accounting-services#breadcrumb`

Service:

`https://velu.us/services/nonprofit-outsourced-accounting-services#service`

OfferCatalog:

`https://velu.us/services/nonprofit-outsourced-accounting-services#offer-catalog`

ScheduleAction:

`https://velu.us/services/nonprofit-outsourced-accounting-services#schedule-action`

Global Website reference:

`https://velu.us/#website`

Global Organization reference:

`https://velu.us/#organization`

## Breadcrumb Decision

There is no dedicated `/services/` landing page.

Use exactly two breadcrumb items:

1. Home
   - `https://velu.us/`
2. Outsourced Accounting for Nonprofits
   - `https://velu.us/services/nonprofit-outsourced-accounting-services`

Do not include a non-existent `/services/` breadcrumb item.

## Image Strategy

Primary image:

- File: `outsourced-accounting-social-share.png`
- Repository path: `assets/images/outsourced-accounting/outsourced-accounting-social-share.png`
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3e5de2163e40d862572bde.png`
- Width: 1731
- Height: 909
- Schema role: `primaryImageOfPage`

Supporting image 1:

- Framework Pillar 1
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a357d7c0a683b64fe0edf90.png`
- Width: 1774
- Height: 887

Supporting image 2:

- Foundation Building
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a35a2410b9538a6a71649ba.png`
- Width: 1536
- Height: 1024

Supporting image 3:

- Framework Pillar 2
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3452440a683b64feed2e46.png`
- Width: 1774
- Height: 887

Do not add the other eight content illustrations to JSON-LD.

## Service Plan

Type:

Service

Name:

`Outsourced Accounting for Nonprofits`

Service type:

`Nonprofit Outsourced Accounting Services`

Category:

`Nonprofit Accounting Services`

Provider:

Reference `https://velu.us/#organization`

Area served:

United States

Audience:

Nonprofit organizations, nonprofit executives, finance leaders, executive directors, and boards

Description:

`Velu helps nonprofit organizations build reliable cloud-based accounting systems, maintain accurate financial records, strengthen fund accounting, improve financial reporting, and gain the financial visibility needed to make confident decisions.`

## OfferCatalog Plan

Catalog name:

`Nonprofit Outsourced Accounting Services`

Offer 1:

Financial Reporting

Offer 2:

Fund Accounting

Offer 3:

Financial Visibility

Offer 4:

Accounting Operations

Descriptions must match the final JSON-LD file.

## Review Decision

- Same 14 Google reviews remain visible on this page.
- Review markup is excluded.
- AggregateRating is excluded.
- The reviews are broad Velu reviews and are not all specific to Outsourced Accounting.
- The reviews are displayed by Velu about Velu and remain visible social proof without self-serving Review or AggregateRating markup.

Do not include:

- Review
- AggregateRating
- FAQPage
- CreativeWork
- duplicate Organization
- duplicate AccountingService
- empty `availableChannel`
- unsupported awards or claims

## ScheduleAction

Name:

`Book Your Discovery Call`

Target:

`https://velu.us/get-started`

Platforms:

- `https://schema.org/DesktopWebPlatform`
- `https://schema.org/MobileWebPlatform`

Agent:

Reference `https://velu.us/#organization`

Object:

Reference the page-specific Outsourced Accounting Service

## GoHighLevel Compatibility

- Pure JSON only
- No `<script>` tags
- Direct image URLs are used in image arrays
- The ScheduleAction is embedded where needed and also defined as a top-level entity
- Live schema review showed 0 errors but 34 warnings caused by unsupported `Service.keywords`
- `keywords` was removed from the Service entity
- `ScheduleAction.urlTemplate` was updated to `https://velu.us/get-started`
- Updated schema entered into GoHighLevel; GoHighLevel replacement/retest complete; Schema.org Validator passed with 0 errors and 0 warnings

## Current Status

- Schema strategy complete
- JSON-LD generated
- Local JSON validation complete
- Updated schema entered into GoHighLevel
- GoHighLevel replacement/retest complete
- Schema.org Validator passed: 0 errors, 0 warnings
- Publication pending
- Live source verification pending
- Google Rich Results Test pending

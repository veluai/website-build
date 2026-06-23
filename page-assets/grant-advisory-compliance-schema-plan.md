# Grant Advisory & Compliance Schema Plan

## Purpose

Document the approved schema structure, entity relationships, source fields, and remaining verification requirements for the Grant Advisory & Compliance service page before production JSON-LD is generated and entered into GoHighLevel.

## Page Identity

Page name:

Grant Advisory & Compliance

Canonical URL:

https://velu.us/services/grant-advisory-compliance-services

SEO title:

Velu | Omaha-Based Nonprofit Grant Advisory & Compliance Services

Visible H1:

Manage Grant Funding with Greater Confidence

Primary conversion URL:

https://velu.us/get-started/

Organization entity:

https://velu.us/#organization

## Deployment Context

- The new Velu homepage, Outsourced Accounting Services page, Client Advisory Services page, and Grant Advisory & Compliance page have not yet been published.
- These pages are part of a coordinated replacement website that will replace the current public Velu website.
- Schema supplied for the homepage and service pages represents pre-publication implementation work, not verified live-site markup.
- The homepage is expected to define:
  - `https://velu.us/#website`
  - `https://velu.us/#organization`
- Service pages may reference those IDs because the replacement homepage and service pages are intended to be published as one coordinated website.
- Cross-page entity relationships remain pending live verification until the replacement website is published.
- The current public website should not be used to confirm whether the replacement-page entities, metadata, images, or schema are live.

## Launch Schema Convention

Preferred coordinated convention:

- The homepage defines the full `WebSite` entity.
- The homepage defines the full `AccountingService` organization entity.
- Service pages reference those entities by `@id`.
- Service pages should not duplicate the full `WebSite` or `AccountingService` entities.
- Each service page defines its own `WebPage`, `BreadcrumbList`, `Service`, page image, OfferCatalog, and ScheduleAction.
- A service page may include reviews and AggregateRating only when the review set is visibly represented and verified.
- Each service-page `WebPage` should reference `https://velu.us/#website` through `isPartOf`.
- Each service provider should reference `https://velu.us/#organization`.
- Draft inconsistencies among the unpublished service-page schemas should not be treated as established production conventions.

## Status Terminology

Before publication, use:

- Drafted
- Generated for launch
- Entered in GoHighLevel
- Locally validated
- Pending publication
- Pending live technical verification

Do not use these statuses before publication:

- Live
- Indexed
- Verified in production
- Confirmed in the live page source
- Included in the live sitemap

## Planned Schema Graph

The launch-ready page schema uses an `@graph` containing exactly five top-level entities:

1. WebPage
2. ImageObject
3. BreadcrumbList
4. Service
5. ScheduleAction

The OfferCatalog is embedded in the Service entity.

The AggregateRating and 12 Review records are attached to the Service entity.

Do not create a duplicate full AccountingService organization entity on this service page unless the existing site implementation requires it.

Reference the established organization entity with:

https://velu.us/#organization

## Entity IDs

Use:

WebPage:
https://velu.us/services/grant-advisory-compliance-services#webpage

Service:
https://velu.us/services/grant-advisory-compliance-services#service

BreadcrumbList:
https://velu.us/services/grant-advisory-compliance-services#breadcrumb

OfferCatalog:
https://velu.us/services/grant-advisory-compliance-services#offer-catalog

ScheduleAction:
https://velu.us/services/grant-advisory-compliance-services#schedule-action

Primary page image:
https://velu.us/services/grant-advisory-compliance-services#primaryimage

Review IDs should be assigned only after exact visible review records are verified.

## WebPage Plan

Type:

WebPage

Required relationships and fields:

- `@id`
- `url`
- `name`
- `description`
- `isPartOf` referencing `https://velu.us/#website` if that website entity exists in the established homepage schema
- `about` referencing the Service entity
- `mainEntity` referencing the Service entity
- `breadcrumb` referencing the BreadcrumbList entity
- `primaryImageOfPage` referencing the ImageObject entity
- `inLanguage`: `en-US`
- `potentialAction` referencing the ScheduleAction entity where appropriate

Use the approved SEO title as the WebPage name unless the existing service-page schema convention uses the visible page title.

Use this description:

Velu helps nonprofits manage grant budgets, reporting, reimbursements, restricted funding, compliance, and future funding readiness.

## Service Plan

Type:

Service

Name:

Grant Advisory & Compliance Services

Service type:

Nonprofit grant advisory and compliance services

Provider:

Reference `https://velu.us/#organization`

Area served:

United States

Audience:

Nonprofit organizations and nonprofit leaders responsible for grant funding, financial stewardship, reporting, reimbursements, restricted funding, compliance, and future funding readiness.

Description:

Velu helps nonprofit leaders manage the financial side of grant funding through funding strategy, grant budgeting, reporting, reimbursements, restricted funding management, compliance support, stewardship, and future funding readiness.

The Service should reference the OfferCatalog containing the four visible lifecycle pillars.

Do not imply that Velu provides grant writing unless that service is separately approved and visibly represented.

## OfferCatalog Plan

Catalog name:

Grant Advisory & Compliance Services

Catalog items:

### 1. Grant Strategy & Funding Visibility

Description:

Understand current and future funding opportunities, identify risks, and evaluate how grant-dependent programs affect sustainability.

### 2. Grant Budgeting & Planning

Description:

Build realistic grant budgets that connect funding requirements, program costs, and organizational priorities.

### 3. Restricted Funding & Compliance

Description:

Manage reporting, reimbursements, restricted funding, documentation, and compliance responsibilities after an award.

### 4. Funder Confidence & Sustainability

Description:

Demonstrate strong stewardship, strengthen funder trust, and improve readiness for future funding.

Each catalog item should use:

- `Offer`
- `itemOffered`
- `Service`

Do not add pricing, availability, package tiers, or service guarantees.

## Breadcrumb Plan

Use this logical hierarchy:

1. Home
   URL: https://velu.us/

2. Services
   URL: https://velu.us/services/

3. Grant Advisory & Compliance
   URL: https://velu.us/services/grant-advisory-compliance-services

`/services/` is the coordinated intermediate breadcrumb page for the replacement website.

## ScheduleAction Plan

Action name:

Book Your Discovery Call

Target:

https://velu.us/get-started/

Action type:

ScheduleAction

Object:

The Grant Advisory & Compliance service or a general discovery-call appointment, depending on the established Velu service-page schema pattern.

Do not invent appointment duration, availability, price, or scheduling platform details.

## Image Plan

The schema should use an actual hosted image URL.

Preferred image role:

Primary social-sharing or page image for Grant Advisory & Compliance.

Current status:

The social-sharing image has been added in the website builder, and its hosted GoHighLevel media asset URL has been documented.

Image name:

Grant Advisory & Compliance Social Share

Hosted URL:

https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a39c58e610e9ace506de5d5.png

Source dimensions:

1731 x 909

Hosted URL source:

GoHighLevel media asset

Website-builder status:

Added

Live URL retrieval and page-source relationship:

Pending verification

The hosted image URL and source dimensions are verified for launch preparation.

The ImageObject may be included in the launch-ready JSON-LD.

Live retrieval and generated page-source relationships remain pending publication and live technical verification.

When live verification is complete, document:

- Confirmed live image URL retrieval status
- Width
- Height
- Caption or name
- Relationship to the WebPage and Service

## Review and Aggregate Rating Plan

Tyler Wilcox has confirmed that the Grant Advisory & Compliance page carousel uses the approved 12 nonprofit-focused reviews from `Reviews.docx`.

`Reviews.docx` is the authoritative source for reviewer names, full review bodies, dates, and ratings.

The approved Client Advisory schema source may be used to confirm coordinated JSON structure, but it is a reference-only source for review content. The prior Client Advisory schema contains shortened or edited versions of four review bodies: Blanca Mejia, Erin Goodwin, McKenna Kiogima, and Dr. Erin Busch.

The Grant Advisory & Compliance schema uses the complete review bodies from `Reviews.docx`. JSON structure may follow the coordinated service-page convention, but testimonial content must match `Reviews.docx` exactly.

Included reviewers:

1. Albert Varas
2. Blanca Mejia
3. Jade Rogers
4. Michael Lewan
5. Gretchen Ellis
6. Erin Goodwin
7. McKenna Kiogima
8. Alex Goswami
9. Dr. Erin Busch
10. Joe Nelson
11. Rachel Ziegler
12. Mike Pichik

Excluded reviews:

- Graham Christensen
- Lani C

Reason for exclusion:

These two reviews are not part of the approved nonprofit-focused service-page review set.

Aggregate rating:

- Rating value: 5
- Best rating: 5
- Worst rating: 1
- Review count: 12
- Rating count: 12

Status:

Verified against the approved nonprofit-focused review set and confirmed as the review set used by the page carousel.

Review schema may be included because the approved 12-review set is visible through the page carousel.

Review entity requirements:

- Review authors, review text, dates, and ratings must be copied exactly from `Reviews.docx`.
- Do not paraphrase, shorten, correct grammar, or otherwise edit testimonial text inside schema.
- Use only the 12 approved nonprofit-focused reviewers.
- Do not include Graham Christensen or Lani C.
- Each Review should use a rating value of 5.
- The coordinated replacement service-page convention attaches the reviews and AggregateRating to the page-specific Service entity.
- Each Review uses `itemReviewed` referencing the Grant Advisory & Compliance Service entity.

## Organization Reference

Use:

https://velu.us/#organization

Do not create a conflicting organization identity.

The established organization type is:

AccountingService

Organization details should remain governed by the central schema standard.

## Pending Requirements

Launch-ready schema and post-publication verification still require:

- Entry into GoHighLevel
- Coordinated publication of the replacement homepage and service pages
- Live page-source inspection after publication
- Duplicate and conflict checks after publication
- Schema.org Validator testing
- Google Rich Results testing
- Canonical and Open Graph verification
- Robots and noindex verification
- XML sitemap verification

## Validation Requirements

After production JSON-LD is created and entered:

- Validate JSON syntax
- Validate with Schema.org Validator
- Test eligible markup in Google Rich Results Test
- Inspect the live page source
- Confirm no duplicate Service, WebPage, BreadcrumbList, or organization entities
- Confirm all URLs resolve
- Confirm review markup matches visible review content
- Confirm the canonical URL matches the schema URL
- Update the page schema inventory only after implementation and validation status are known

## Current Status

Launch-ready production JSON-LD has been generated and locally validated.

The schema has not yet been entered into GoHighLevel or published. All live technical verification remains pending.

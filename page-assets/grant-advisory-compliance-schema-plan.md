# Grant Advisory & Compliance Schema Plan

## Purpose

Document the approved schema structure, entity relationships, source fields, and remaining verification requirements for the Grant Advisory & Compliance service page before production JSON-LD is entered into GoHighLevel.

## Page Identity

Page name:

Grant Advisory & Compliance

Canonical URL:

https://velu.us/services/nonprofit-grant-advisory-compliance-services

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
- Review markup for broad Velu testimonials should remain governed by the broader website schema strategy and should not be attached to a page-specific Service entity unless the reviews are specifically for that service.
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

The final Grant Advisory & Compliance page JSON-LD does not include Review or AggregateRating properties.

Do not create a duplicate full AccountingService organization entity on this service page unless the existing site implementation requires it.

Reference the established organization entity with:

https://velu.us/#organization

## Entity IDs

Use:

WebPage:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#webpage

Service:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#service

BreadcrumbList:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#breadcrumb

OfferCatalog:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#offer-catalog

ScheduleAction:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#schedule-action

Primary page image:
https://velu.us/services/nonprofit-grant-advisory-compliance-services#primaryimage

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

2. Grant Advisory & Compliance
   URL: https://velu.us/services/nonprofit-grant-advisory-compliance-services

There is no dedicated `/services/` landing page. Do not include a `/services/` breadcrumb item unless a real Services landing page is created.

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

GoHighLevel required a `creator` property for the `ImageObject` when the schema was entered into the dedicated Schema Markup JSON View.

Image name:

Grant Advisory & Compliance Social Share

Hosted URL:

https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a39c58e610e9ace506de5d5.png

Source dimensions:

1731 x 909

Hosted URL source:

GoHighLevel media asset

Image creator:

Velu, referenced through the planned organization ID:

https://velu.us/#organization

Website-builder status:

Added

Live URL retrieval and page-source relationship:

Pending verification

The hosted image URL and source dimensions are verified for launch preparation.

The ImageObject may be included in the launch-ready JSON-LD.

The ImageObject includes a `creator` property identifying Velu as the image creator through the planned organization ID.

Live retrieval and generated page-source relationships remain pending publication and live technical verification.

When live verification is complete, document:

- Confirmed live image URL retrieval status
- Width
- Height
- Caption or name
- Relationship to the WebPage and Service

## Visible Review Carousel and Schema Decision

Tyler Wilcox has confirmed that the Grant Advisory & Compliance page carousel uses the approved 12 nonprofit-focused reviews from `Reviews.docx`.

`Reviews.docx` is the authoritative source for reviewer names, full review bodies, dates, and ratings.

The approved Client Advisory schema source may be used to confirm coordinated JSON structure, but it is a reference-only source for review content. The prior Client Advisory schema contains shortened or edited versions of four review bodies: Blanca Mejia, Erin Goodwin, McKenna Kiogima, and Dr. Erin Busch.

The visible review carousel remains part of the approved page content. The testimonials are broad reviews of Velu and its nonprofit accounting and advisory work, and they are not all specifically reviews of the Grant Advisory & Compliance service.

Because the reviews are broad Velu testimonials, Review and AggregateRating markup will not be attached to the page-specific Grant Advisory & Compliance Service entity. The final Grant Advisory & Compliance page JSON-LD contains no Review or AggregateRating properties.

Review markup may remain governed centrally through the homepage organization schema, subject to the broader website schema strategy.

Visible carousel reviewers:

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

Status:

Verified as the visible nonprofit-focused carousel review set only. These records are not page-specific schema requirements for the Grant Advisory & Compliance JSON-LD.

Schema requirements:

- Do not attach Review records to the page-specific Service entity.
- Do not attach AggregateRating to the page-specific Service entity.
- Do not add the carousel reviews elsewhere in this page-level JSON-LD.
- Do not add a separate organization review entity in this page-level JSON-LD.

## Organization Reference

Use:

https://velu.us/#organization

Do not create a conflicting organization identity.

The established organization type is:

AccountingService

Organization details should remain governed by the central schema standard.

## Pending Requirements

Launch-ready schema and post-publication verification still require:

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
- Confirm no Review or AggregateRating markup exists in the Grant Advisory & Compliance page-level JSON-LD
- Confirm the canonical URL matches the schema URL
- Update the page schema inventory only after implementation and validation status are known

## Current Status

Launch-ready schema entered and saved in GoHighLevel; pending publication and live technical verification.

The schema was entered into the GoHighLevel dedicated Schema Markup JSON View without `<script type="application/ld+json">` tags because the dedicated JSON View accepts pure JSON. GoHighLevel's built-in validation passed, and the schema was saved in GoHighLevel.

The visible review carousel remains on the page. The page remains unpublished. Schema.org Validator testing, Google Rich Results testing, live-source inspection, and all post-publication verification remain pending.

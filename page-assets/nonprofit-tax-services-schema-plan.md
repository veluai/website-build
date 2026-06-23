# Nonprofit Tax Services Schema Plan

## Purpose

Document the approved schema strategy, planned entities, entity relationships, source fields, service boundaries, and remaining verification requirements for the Nonprofit Tax Services page before production JSON-LD is generated and entered into GoHighLevel.

## Page Identity

Page name:

Nonprofit Tax Services

Canonical URL:

https://velu.us/services/nonprofit-tax-services

SEO title:

Velu | Omaha-Based Nonprofit Tax Services & Form 990 Preparation

Visible H1:

File Your Form 990 With Greater Confidence

Primary CTA:

Book Your Discovery Call

CTA URL:

https://velu.us/get-started/

Primary SEO topic:

nonprofit tax services

## Deployment Context

- The replacement Velu website remains unpublished.
- The Nonprofit Tax Services page is part of the coordinated replacement website.
- The replacement homepage is expected to define:
  - `https://velu.us/#website`
  - `https://velu.us/#organization`
- The service-page schema should reference those IDs.
- The service page should not duplicate the complete WebSite or AccountingService organization entities.
- Cross-page relationships remain pending publication and live technical verification.
- The current public website should not be treated as evidence that the replacement-page schema is live.

## Launch Schema Convention

Plan a page-level `@graph` containing exactly five top-level entities:

1. WebPage
2. ImageObject
3. BreadcrumbList
4. Service
5. ScheduleAction

The OfferCatalog should be embedded within the Service entity.

Do not include top-level:

* WebSite
* Organization
* AccountingService
* Review
* AggregateRating
* FAQPage

Do not attach broad Velu reviews to the page-specific Service entity.

## Planned Entity IDs

WebPage:

https://velu.us/services/nonprofit-tax-services#webpage

Service:

https://velu.us/services/nonprofit-tax-services#service

BreadcrumbList:

https://velu.us/services/nonprofit-tax-services#breadcrumb

OfferCatalog:

https://velu.us/services/nonprofit-tax-services#offer-catalog

ScheduleAction:

https://velu.us/services/nonprofit-tax-services#schedule-action

Primary image:

https://velu.us/services/nonprofit-tax-services#primaryimage

Website reference:

https://velu.us/#website

Organization reference:

https://velu.us/#organization

## WebPage Plan

Type:

WebPage

Plan these fields and relationships:

* `@id`
* `url`
* `name`
* `description`
* `isPartOf`
* `mainEntity`
* `about`
* `breadcrumb`
* `publisher`
* `primaryImageOfPage`
* `image`
* `inLanguage`
* `potentialAction`

URL:

https://velu.us/services/nonprofit-tax-services

Name:

Velu | Omaha-Based Nonprofit Tax Services & Form 990 Preparation

Description:

Velu helps nonprofits prepare Form 990, Form 990-EZ, and Form 990-N filings and navigate tax-exempt status applications with greater confidence.

Language:

en-US

The WebPage should reference:

* `https://velu.us/#website` through `isPartOf`
* `https://velu.us/#organization` through `publisher`
* The page-specific Service through `mainEntity` and `about`
* The page-specific BreadcrumbList
* The primary ImageObject
* The page-specific ScheduleAction

## Service Plan

Type:

Service

Name:

Nonprofit Tax Services

Recommended service type:

Nonprofit Tax Preparation and Tax-Exempt Status Application Services

Recommended category:

Nonprofit Federal Tax Compliance Services

Provider:

Reference `https://velu.us/#organization`

Area served:

United States

Audience:

Nonprofit organizations requiring Form 990 filing support or assistance applying for or restoring federal tax-exempt status.

Recommended description:

Velu helps nonprofit organizations prepare and file Form 990, Form 990-EZ, and Form 990-N and supports organizations applying for or restoring federal tax-exempt status.

The Service should reference:

* The page-specific primary ImageObject
* The embedded OfferCatalog
* The organization provider
* The approved audience and area served

## OfferCatalog Plan

Catalog name:

Nonprofit Tax Services

Plan exactly two Offer items.

### Offer 1: Form 990 Preparation

Item type:

Service

Name:

Form 990 Preparation

Description:

Prepare and file Form 990, Form 990-EZ, or Form 990-N with support for applicable schedules, public-support testing, extensions, client review, and electronic filing.

Do not imply that the standard engagement includes bookkeeping cleanup, reconciliations, financial statement preparation, or reconstruction of incomplete records.

### Offer 2: Tax-Exempt Status Applications

Item type:

Service

Name:

Tax-Exempt Status Applications

Description:

Support for nonprofit organizations applying for or restoring federal tax-exempt status through an organized application process covering required financial, organizational, operational, and governance information.

Do not imply guaranteed approval.

Do not name specific application forms in the OfferCatalog description unless later approved for visible page copy.

## ImageObject Plan

Use the final approved social-sharing image as the page-level primary image unless implementation review determines that the hero image is more appropriate.

Preferred image:

Repository path:

assets/images/tax-services/nonprofit-tax-services-social-share.png

Dimensions:

1731 x 909

Hosted image URL:

Pending GoHighLevel upload

Planned name:

Nonprofit Tax Services

Planned caption:

Nonprofit tax services for Form 990 preparation, filing confidence, and tax-exempt status applications.

The ImageObject should include:

* `@type`
* `@id`
* `url`
* `contentUrl`
* `width`
* `height`
* `name`
* `caption`
* `creator`
* `inLanguage`

The `creator` should identify Velu through:

https://velu.us/#organization

The final JSON-LD must not be generated until the hosted image URL is available.

## Breadcrumb Plan

Use:

1. Home
   URL: https://velu.us/

2. Services
   URL: https://velu.us/services/

3. Nonprofit Tax Services
   URL: https://velu.us/services/nonprofit-tax-services

`/services/` is the planned intermediate breadcrumb page for the coordinated replacement website.

## ScheduleAction Plan

Type:

ScheduleAction

Name:

Schedule a Discovery Call

Target:

https://velu.us/get-started/

Object:

Reference the page-specific Nonprofit Tax Services Service entity.

Do not invent:

* Appointment duration
* Availability
* Price
* Scheduling platform
* Consultation guarantees

## Keywords Plan

The future Service entity may include these keywords:

* nonprofit tax services
* Form 990 preparation
* Form 990 filing
* Form 990-EZ preparation
* Form 990-EZ filing
* Form 990-N preparation
* Form 990-N filing
* nonprofit tax preparation
* nonprofit tax compliance
* nonprofit federal tax filing
* nonprofit tax-exempt status applications
* nonprofit tax exemption
* tax-exempt status reinstatement
* Form 1023
* Form 1023-EZ
* Form 1024

Keywords must reflect actual service scope and should not expand the visible page claims.

## Review and Aggregate-Rating Decision

The visible nonprofit review carousel may remain on the page.

The reviews are broad Velu testimonials and are not necessarily specific to Nonprofit Tax Services.

Review and AggregateRating markup should not be attached to the page-specific Service entity.

No page-level Review or AggregateRating markup should be added.

Organization-level review strategy remains governed by the replacement homepage schema.

## Approved Service Boundaries

The schema may describe:

* Form 990 preparation
* Form 990-EZ preparation and filing
* Form 990-N preparation and filing
* Applicable schedules and disclosures
* Public-support testing
* Extension filings
* Client review
* Electronic filing
* Tax-exempt status applications
* Tax-exempt status reinstatement where appropriate
* Form 1023
* Form 1023-EZ
* Form 1024
* Nonprofit federal tax compliance

The schema must not state or imply:

* Form 990-PF preparation
* State charitable registrations or renewals
* Advanced nonprofit tax planning
* Year-round tax-advisory retainers
* Standalone IRS notice representation
* Individual tax preparation
* For-profit business tax preparation
* Bookkeeping cleanup within the standard Form 990 engagement
* Account reconciliations within the standard Form 990 engagement
* Financial statement preparation within the standard Form 990 engagement
* Independent verification of the client’s underlying accounting records
* Guaranteed tax-exempt approval

## Client Responsibility Boundary

The standard Form 990 engagement assumes the client provides:

* Accurate and finalized financial information
* Complete accounting records
* A completed detailed questionnaire
* Requested governance, compensation, program, and disclosure information
* Timely responses to follow-up questions

Cleanup, reconciliation, record reconstruction, or accounting preparation requires a separate engagement.

This boundary may inform schema wording but should not be inserted as contractual language unless necessary.

## Pending Requirements

* Hosted social-sharing image URL
* GoHighLevel page implementation
* Final JSON-LD generation
* GoHighLevel schema validation
* Coordinated publication of the replacement website
* Live page-source inspection
* Duplicate-entity checks
* Schema.org Validator testing
* Google Rich Results testing
* Canonical and Open Graph verification
* Robots and noindex verification
* XML sitemap verification
* Image retrieval verification

## Current Status

Schema strategy documented for launch; pending hosted image URL, JSON-LD generation, GoHighLevel implementation, publication, and live technical verification.

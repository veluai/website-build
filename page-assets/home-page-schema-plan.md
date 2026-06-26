# Home Page Schema Plan

## Page Identity

- Page name: Home
- Canonical URL: `https://velu.us/`
- SEO title: `Velu | Omaha-Based Nonprofit Accounting & Advisory`
- Primary CTA: `Book Your Discovery Call`
- CTA URL: `https://velu.us/get-started/`

## Deployment Context

- Replacement GHL site is not published.
- Old site remains live.
- Home page defines the global Website and Organization entities for the replacement site.
- Other page schemas reference these global IDs.
- Publication and live validation remain pending.

## Global Entity IDs

- Website: `https://velu.us/#website`
- Organization: `https://velu.us/#organization`
- WebPage: `https://velu.us/#webpage`

## Final Top-Level Schema Structure

The Home-page JSON-LD contains exactly three top-level `@graph` entities:

1. WebSite
2. WebPage
3. AccountingService

The Home schema also includes embedded:

- ImageObject for primary image
- ScheduleAction
- OfferCatalog
- Four Offer items

## Exclusions

Do not include:

- CreativeWork lead magnet
- Review
- AggregateRating
- FAQPage
- BreadcrumbList
- Duplicate standalone Organization entity
- Unsupported service claims
- Unsupported awards, ratings, badges, or statistics

## Review Decision

- 14 Google reviews remain visible on the Home page.
- Review markup excluded.
- AggregateRating excluded.

Reason:

`The reviews are displayed by Velu about Velu and remain visible social proof without self-serving Review or AggregateRating markup.`

## Image Strategy

Primary image:

- File: `home-velu-social-share.png`
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3e4583d50c4ff184cc25e3.png`
- Width: 1731
- Height: 909
- Schema role: `primaryImageOfPage`

Supporting image 1:

- Image: Founder hero
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3d9188db2129be183e0dee.png`
- Width: 1672
- Height: 941

Supporting image 2:

- Image: Team collaboration
- Hosted URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a233b1efc95b245498ebda7.png`
- Width: 1536
- Height: 1024

## Service Catalog URLs

- Outsourced Accounting: `https://velu.us/services/outsourced-accounting-services`
- Client Advisory Services: `https://velu.us/services/client-advisory-services`
- Grant Advisory and Compliance: `https://velu.us/services/grant-advisory-compliance-services`
- Nonprofit Tax Services: `https://velu.us/services/tax-services`

## Organization Details

- Name: Velu
- Legal name: Velu LLC
- URL: `https://velu.us/`
- Address: `1402 Jones St #1004, Omaha, NE 68102`
- Phone: `+1-402-578-0622`
- Email: `info@velu.us`
- Opening hours: Monday-Friday, 9:00-17:00
- Area served: United States
- Price range: `$$`
- Currencies: USD
- Payment accepted: Check, Credit Card, ACH
- LinkedIn: `https://www.linkedin.com/company/velucpa/`
- Google Maps: `https://www.google.com/maps/place/Velu+LLC,+1402+Jones+St+%231004,+Omaha,+NE+68102`
- Intuit profile: `https://proadvisor.intuit.com/app/accountant/search?searchId=tyler-wilcox77`

Logo URL:

`https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a224bccfc95b245497d57f8.jpg`

## ScheduleAction

- Name: `Book Your Discovery Call`
- Target: `https://velu.us/get-started/`
- Platforms:
  - DesktopWebPlatform
  - MobileWebPlatform

## GoHighLevel Compatibility Note

The final JSON-LD intentionally uses direct image URLs and an embedded ScheduleAction rather than reference-only `@id` objects in the fields that previously triggered GoHighLevel validation errors.

## Current Schema Status

- Generated
- Entered into GoHighLevel
- GoHighLevel validation passed
- Publication pending
- Live source verification pending
- Schema.org Validator pending
- Google Rich Results Test pending

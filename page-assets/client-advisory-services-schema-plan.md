# Client Advisory Services Schema Plan

## Page Status

- Page: Client Advisory Services
- Canonical URL: `https://velu.us/services/nonprofit-client-advisory-services`
- Relative URL: `/services/nonprofit-client-advisory-services`
- Schema-planning status: Current-state documentation backfill created
- JSON-LD generation status: Complete
- GoHighLevel replacement schema status: Complete
- GoHighLevel page-level validation status: Complete
- Publication status: Pending
- Live validation status: Pending publication

## Deployment Context

The Client Advisory Services page is part of the unpublished Velu replacement website.

Do not describe the page, schema, metadata, images, or canonical URL as live, indexed, published, or production-verified until publication and live technical verification are complete.

## Required Replacement Schema Strategy

The replacement schema should use exactly five top-level `@graph` entities:

1. `WebPage`
2. `ImageObject`
3. `BreadcrumbList`
4. `Service`
5. `ScheduleAction`

The Service entity should contain an embedded `OfferCatalog` with exactly four offers:

1. Budgeting & Financial Planning
2. Budget Performance Analysis
3. Forecasting & Financial Visibility
4. Board & Leadership Reporting

## Required Entity IDs

- WebPage: `https://velu.us/services/nonprofit-client-advisory-services#webpage`
- Service: `https://velu.us/services/nonprofit-client-advisory-services#service`
- BreadcrumbList: `https://velu.us/services/nonprofit-client-advisory-services#breadcrumb`
- OfferCatalog: `https://velu.us/services/nonprofit-client-advisory-services#offer-catalog`
- ScheduleAction: `https://velu.us/services/nonprofit-client-advisory-services#schedule-action`
- Primary image: `https://velu.us/services/nonprofit-client-advisory-services#primaryimage`

## Global References

- WebSite: `https://velu.us/#website`
- Organization: `https://velu.us/#organization`

The service page should reference the global WebSite and Organization entities. It should not duplicate the full WebSite, Organization, or AccountingService entities.

## Primary Image

Use the metadata-only social-sharing image as the page primary image:

- Image URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3eba9014a2b82bfeed66ee.png`
- Dimensions: `1733 x 907`
- Image name: `Client Advisory Services`
- Image caption: `Nonprofit client advisory services for budgeting, forecasting, financial foresight, and leadership decision-making.`

GoHighLevel required the ImageObject creator reference to include an explicit Organization name. The production JSON-LD therefore references https://velu.us/#organization and includes name: Velu.

## Required Breadcrumb

The breadcrumb must contain exactly two items:

1. Home — `https://velu.us/`
2. Client Advisory Services — `https://velu.us/services/nonprofit-client-advisory-services`

There is no real `/services/` landing page. Do not include a `/services/` breadcrumb item.

## Required ScheduleAction

- Name: `Book Your Discovery Call`
- Target: `https://velu.us/get-started/`
- Object: Reference the page-specific Service entity at `https://velu.us/services/nonprofit-client-advisory-services#service`

Do not invent duration, availability, pricing, or guarantees in schema.

## Required Exclusions

Do not include:

- `Review`
- `AggregateRating`
- `FAQPage`
- Top-level `WebSite`
- Top-level `Organization`
- Top-level `AccountingService`
- `/services/` breadcrumb
- Script tags
- Comments
- Unsupported guarantees
- Unsupported pricing or availability

## Testimonials Policy

The visible page uses the existing sitewide testimonial carousel.

The testimonials are not treated as Client Advisory-specific review evidence and are not eligible for page-level Review or AggregateRating schema under current policy.

## Current GoHighLevel Schema Status

- Replacement production JSON-LD entered in GHL
- Old schema removed
- Replacement schema saved
- GHL page-level validation passed
- No other schema blocks are present
- Page remains unpublished
- Live validation remains pending publication

## Superseded Schema Issues Resolved

The old schema was replaced because it included or used:

- Wrong URL
- Wrong entity IDs
- Three-item breadcrumb
- Nonexistent Services breadcrumb
- Old CTA label
- Review markup
- AggregateRating markup
- Duplicated AccountingService
- Missing global WebSite reference
- Missing top-level ImageObject
- Script tags

## Completed Local Validation

- Production JSON-LD generation: Complete
- Local JSON syntax validation: Complete
- Five-entity graph validation: Complete
- Entity-ID uniqueness validation: Complete
- OfferCatalog validation with exactly four offers: Complete
- Two-item breadcrumb validation: Complete
- Review and AggregateRating exclusion validation: Complete

## Pending Requirements

- Publication
- Live source verification
- Schema.org Validator testing
- Google Rich Results testing
- Canonical verification
- Image retrieval verification
- Robots/noindex verification
- XML sitemap verification
- Live social-preview verification

## Current Status

The production JSON-LD has been generated, locally validated, entered in GoHighLevel, and accepted by page-level validation. Publication and live technical verification remain pending.

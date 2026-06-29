# About Page Schema Plan

## Page Status

* Page: About
* URL: `https://velu.us/about-us`
* Relative path: `/about-us`
* Schema planning status: Approved
* JSON-LD generation status: Complete
* Local validation status: Complete
* GoHighLevel entry status: Complete
* GoHighLevel page-level validation status: Complete
* Five-entity JSON-LD implementation status: Complete
* Publication status: Pending
* Live validation status: Pending publication

## Schema Objective

The schema should help search engines understand that:

* This is Velu’s official About page
* Tyler Wilcox, CPA is the founder and primary person featured
* Velu is a nonprofit-focused CPA and accounting firm
* Tyler has substantial nonprofit accounting, Form 990, consulting, tax, and audit experience
* Velu serves nonprofits across multiple sectors
* Velu takes a mission-driven approach to financial services
* The page is part of the existing Velu website and organization entity structure

The schema should support the visible page without introducing claims or entities not presented on the page.

Live About schema review found 4 validator errors caused by untyped `Thing` references used for `Person.worksFor` and `Person.affiliation`. Organization references have been updated to typed `AccountingService` references, and the `ScheduleAction.target.urlTemplate` has been updated to `https://velu.us/get-started`. GoHighLevel also required addresses on embedded typed `AccountingService` references, so address fields were added to GHL-facing organization references. Updated schema was entered into GoHighLevel, GoHighLevel replacement/retest is complete, and Schema.org Validator passed with 0 errors and 0 warnings.

## Proposed Top-Level Graph Structure

Use the following top-level entities:

1. `AboutPage`
2. `ImageObject`
3. `BreadcrumbList`
4. `Person`
5. `ScheduleAction`

The About page should reference the existing global entities:

* Website: `https://velu.us/#website` — confirmed
* Organization: `https://velu.us/#organization` — confirmed

Do not duplicate full `WebSite`, `Organization`, `AccountingService`, or `ProfessionalService` entities on this page.

## Entity 1: AboutPage

### Recommended Type

`AboutPage`

### Recommended ID

`https://velu.us/about-us#webpage`

### Recommended Properties

* `@type`: `AboutPage`
* `@id`: `https://velu.us/about-us#webpage`
* `url`: `https://velu.us/about-us`
* `name`: `Velu | Omaha-Based Nonprofit CPA Firm Led by Tyler Wilcox, CPA`
* `description`: `Meet Tyler Wilcox, CPA and learn how Velu’s nonprofit experience helps organizations build stronger financial foundations and make confident decisions.`
* `isPartOf`: reference `https://velu.us/#website`
* `about`: references both:
  * `https://velu.us/#organization`
  * `https://velu.us/about-us#tyler-wilcox`
* `mainEntity`: reference `https://velu.us/about-us#tyler-wilcox`
* `publisher`: reference `https://velu.us/#organization`
* `breadcrumb`: reference `https://velu.us/about-us#breadcrumb`
* `primaryImageOfPage`: reference `https://velu.us/about-us#primaryimage`
* `image`: reference `https://velu.us/about-us#primaryimage`
* `inLanguage`: `en-US`
* `potentialAction`: reference `https://velu.us/about-us#schedule-action`

### Notes

* Use `AboutPage`, not generic `WebPage`
* The primary visible subject is Tyler Wilcox, CPA
* The organization remains an important secondary subject
* Do not use `ProfilePage` unless there is a strong technical reason, because the page is about both Tyler and Velu rather than being solely Tyler’s personal profile

## Entity 2: ImageObject

### Recommended ID

`https://velu.us/about-us#primaryimage`

### Recommended Image

Use the approved About-page social-sharing image:

* Image name: `IMAGE_Velu_About_Social Share`
* Filename: `about-velu-social-share.png`
* Headline: `About Velu`
* Supporting line: `Nonprofit Expertise. Mission-Driven Finances.`

### Recommended Properties

* `@type`: `ImageObject`
* `@id`: `https://velu.us/about-us#primaryimage`
* `url`: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c439fae7d4768394efb7b.png`
* `contentUrl`: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c439fae7d4768394efb7b.png`
* `width`: `1732`
* `height`: `908`
* `name`: `About Velu`
* `caption`: `About Velu, a nonprofit-focused CPA firm led by Tyler Wilcox, CPA.`
* `creator`: reference `https://velu.us/#organization`
* `inLanguage`: `en-US`

### Notes

The hosted social-image URL and exact dimensions are confirmed and included in the generated JSON-LD.

The metadata-only social image does not require webpage alt text.

## Entity 3: BreadcrumbList

### Recommended ID

`https://velu.us/about-us#breadcrumb`

### Recommended Items

1. Home

   * URL: `https://velu.us/`
2. About

   * URL: `https://velu.us/about-us`

### Recommended Structure

Use two `ListItem` entries with correct numeric positions.

Do not add a Services breadcrumb because the About page is not a service page.

## Entity 4: Person

### Recommended ID

`https://velu.us/about-us#tyler-wilcox`

### Recommended Type

`Person`

### Recommended Properties

* `@type`: `Person`
* `@id`: `https://velu.us/about-us#tyler-wilcox`
* `name`: `Tyler Wilcox`
* `honorificSuffix`: `CPA`
* `jobTitle`: `Founder`
* `description`: concise summary grounded in the approved page copy
* `url`: `https://velu.us/about-us`
* `image`: reference the approved Tyler founder image at `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3b6a12967e20d627d56a55.png`
* `worksFor`: typed `AccountingService` reference to `https://velu.us/#organization` with Velu address
* `affiliation`: typed `AccountingService` reference to `https://velu.us/#organization` with Velu address
* `knowsAbout`: an array of approved professional topics
* `mainEntityOfPage`: reference `https://velu.us/about-us#webpage`

### Recommended Description Direction

Use a concise statement such as:

`Tyler Wilcox, CPA is the founder of Velu and has more than 15 years of accounting experience, including over a decade serving nonprofit organizations through outsourced accounting, financial reporting, Form 990 preparation, federal tax compliance, consulting, and audit-related experience.`

Do not make the description excessively long.

### Recommended `knowsAbout` Topics

Use only approved, visible, and supportable topics such as:

* Nonprofit accounting
* Nonprofit financial reporting
* Form 990 preparation
* Federal nonprofit tax compliance
* Outsourced accounting
* Client advisory services
* Grant accounting and compliance
* Fund accounting
* Financial systems
* Internal controls
* Nonprofit financial management

### Credentials

The visible page includes:

* Certified Public Accountant
* QuickBooks ProAdvisor Level 2
* AICPA Nonprofit Level 1 Certificate

Separate structured credential objects are intentionally omitted.

Credentials remain represented in the visible page copy and the Person description.

Do not add credential IDs, dates, issuing URLs, or credential entities.

## Nonprofit Sector Experience

The page visibly documents experience across ten nonprofit sectors:

1. Affordable Housing
2. Workforce Development
3. Youth and Family Services
4. Human Services
5. Food Insecurity
6. Sustainable and Regenerative Agriculture
7. Rural and Economic Development
8. Education and Schools
9. Arts and Culture
10. Membership Associations and 501(c)(6) Organizations

### Recommended Schema Treatment

Do not create ten separate organization, service, or industry entities merely to represent the card grid.

Represent this experience through:

* The Person entity’s `knowsAbout` where appropriate
* The AboutPage description and visible content
* Possibly carefully selected `about` or `keywords` values if consistent with the sitewide schema standard

Avoid overloading the JSON-LD with unsupported sector entities.

## Entity 5: ScheduleAction

### Recommended ID

`https://velu.us/about-us#schedule-action`

### Recommended Properties

* `@type`: `ScheduleAction`
* `@id`: `https://velu.us/about-us#schedule-action`
* `name`: `Schedule a Discovery Call`
* `target`:
  * `@type`: `EntryPoint`
  * `urlTemplate`: `https://velu.us/get-started`
* `object`: typed `AccountingService` reference to `https://velu.us/#organization` with Velu address

### Notes

Because the About page promotes a relationship with Velu rather than one specific service, the action object should reference the organization rather than a page-level service entity.

The final CTA URL is confirmed as `https://velu.us/get-started`.

## Review and Rating Policy

Do not add:

* `Review`
* `AggregateRating`
* `ratingValue`
* `reviewCount`

The About page does not require page-level review markup.

Any visible review content elsewhere on the site should follow the approved sitewide review policy.

## FAQ Policy

Do not add `FAQPage` unless a visible About-page FAQ section is created and approved.

No About-page FAQ is currently planned.

## Additional Exclusions

Do not add:

* Unsupported awards
* Unsupported rankings
* Unverified client counts
* Exact service-area limitations
* Unsupported founding dates
* Unsupported education history
* Credential dates or IDs that have not been verified
* Social profiles that have not been confirmed for Tyler personally
* A duplicated full Organization entity
* A duplicated full WebSite entity

## Approved Inputs for JSON-LD Generation

The following inputs are confirmed:

* Global organization entity ID: `https://velu.us/#organization`
* Global website entity ID: `https://velu.us/#website`
* Visible page retains the approved credibility claims
* Separate structured credential objects will be omitted
* Credentials remain represented in visible page copy and the Person description
* Final CTA URL: `https://velu.us/get-started`
* Final heading structure:
  * H1: `Meet Tyler Wilcox, CPA`
  * H2: `Experience Across the Nonprofit Sector`
  * H2: `Looking for a Financial Partner Who Understands Nonprofits?`
* Final page copy confirmed

## Validation Checklist

Completed locally:

* Pure JSON syntax
* No Markdown fences
* No `<script>` tags
* Correct canonical URL
* Correct entity IDs
* Correct organization and website references
* Valid AboutPage-to-Person relationship
* Valid Person properties
* Valid ImageObject dimensions and URL
* Correct BreadcrumbList positions
* Correct ScheduleAction target
* Typed `AccountingService` references with Velu address for organization relationships
* No duplicated global entities
* No Review or AggregateRating
* No FAQPage
* No unsupported claims

The generated graph contains exactly five top-level entities with unique `@id` values. Local About-page references resolve to graph entities, and global Website and Organization entities are referenced without duplicating the full global entities.

After publication, validate:

* Live page source
* Google Rich Results Test, recognizing that an About page may not qualify for a special rich result
* Canonical consistency
* Image retrieval
* Robots/noindex status
* Sitemap inclusion

## Schema Status

Record these as complete:

* Schema-plan architecture approved
* Page schema strategy drafted
* Proposed entity structure documented
* Person-entity strategy documented
* Review and FAQ exclusions documented
* Required inputs identified
* Exact social-image dimensions confirmed: `1732 × 908`
* Hosted social-image URL confirmed
* Stable founder-image URL confirmed
* Final page URL and canonical URL confirmed as `https://velu.us/about-us`
* Schema-plan approval
* Final credential-property decision: omit separate structured credential objects
* Organization entity ID confirmed as `https://velu.us/#organization`
* Website entity ID confirmed as `https://velu.us/#website`
* Final CTA confirmed as `https://velu.us/get-started`
* Final heading and page-copy confirmation
* Approved credibility-claim confirmation
* JSON-LD generation
* Local JSON syntax validation
* Five-entity graph validation
* Entity-ID uniqueness validation
* Canonical URL and reference validation
* Local exclusion checks
* Five-entity JSON-LD implementation complete
* Updated schema entered into GoHighLevel
* GoHighLevel replacement/retest complete
* Schema.org Validator passed: 0 errors, 0 warnings

Record these as pending:

* Publication
* Live source verification
* Live canonical verification
* Live metadata verification
* Live image retrieval verification
* Google Rich Results Test
* Robots/noindex verification
* XML sitemap verification
* Live social-preview verification

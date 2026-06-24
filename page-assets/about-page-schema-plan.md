# About Page Schema Plan

## Page Status

* Page: About
* URL: `https://velu.us/about`
* Relative path: `/about`
* Schema planning status: Draft for approval
* JSON-LD generation status: Pending
* GoHighLevel entry status: Pending
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

## Proposed Top-Level Graph Structure

Use the following top-level entities:

1. `AboutPage`
2. `ImageObject`
3. `BreadcrumbList`
4. `Person`
5. `ScheduleAction`

The About page should reference the existing global entities:

* Website: `https://velu.us/#website`
* Organization: `https://velu.us/#organization`

Do not duplicate full `WebSite`, `Organization`, `AccountingService`, or `ProfessionalService` entities on this page.

## Entity 1: AboutPage

### Recommended Type

`AboutPage`

### Recommended ID

`https://velu.us/about#webpage`

### Recommended Properties

* `@type`: `AboutPage`
* `@id`: `https://velu.us/about#webpage`
* `url`: `https://velu.us/about`
* `name`: `Velu | Omaha-Based Nonprofit CPA Firm Led by Tyler Wilcox, CPA`
* `description`: `Meet Tyler Wilcox, CPA and learn how Velu’s nonprofit experience helps organizations build stronger financial foundations and make confident decisions.`
* `isPartOf`: reference `https://velu.us/#website`
* `about`: references both:
  * `https://velu.us/#organization`
  * `https://velu.us/about#tyler-wilcox`
* `mainEntity`: reference `https://velu.us/about#tyler-wilcox`
* `publisher`: reference `https://velu.us/#organization`
* `breadcrumb`: reference `https://velu.us/about#breadcrumb`
* `primaryImageOfPage`: reference `https://velu.us/about#primaryimage`
* `image`: reference `https://velu.us/about#primaryimage`
* `inLanguage`: `en-US`
* `potentialAction`: reference `https://velu.us/about#schedule-action`

### Notes

* Use `AboutPage`, not generic `WebPage`
* The primary visible subject is Tyler Wilcox, CPA
* The organization remains an important secondary subject
* Do not use `ProfilePage` unless there is a strong technical reason, because the page is about both Tyler and Velu rather than being solely Tyler’s personal profile

## Entity 2: ImageObject

### Recommended ID

`https://velu.us/about#primaryimage`

### Recommended Image

Use the approved About-page social-sharing image:

* Image name: `IMAGE_Velu_About_Social Share`
* Filename: `about-velu-social-share.png`
* Headline: `About Velu`
* Supporting line: `Nonprofit Expertise. Mission-Driven Finances.`

### Recommended Properties

* `@type`: `ImageObject`
* `@id`: `https://velu.us/about#primaryimage`
* `url`: pending hosted image URL
* `contentUrl`: pending hosted image URL
* `width`: pending final confirmed dimensions
* `height`: pending final confirmed dimensions
* `name`: `About Velu`
* `caption`: `About Velu, a nonprofit-focused CPA firm led by Tyler Wilcox, CPA.`
* `creator`: reference `https://velu.us/#organization`
* `inLanguage`: `en-US`

### Notes

Do not generate final JSON-LD until the hosted image URL and exact dimensions are available.

The metadata-only social image does not require webpage alt text.

## Entity 3: BreadcrumbList

### Recommended ID

`https://velu.us/about#breadcrumb`

### Recommended Items

1. Home

   * URL: `https://velu.us/`
2. About

   * URL: `https://velu.us/about`

### Recommended Structure

Use two `ListItem` entries with correct numeric positions.

Do not add a Services breadcrumb because the About page is not a service page.

## Entity 4: Person

### Recommended ID

`https://velu.us/about#tyler-wilcox`

### Recommended Type

`Person`

### Recommended Properties

* `@type`: `Person`
* `@id`: `https://velu.us/about#tyler-wilcox`
* `name`: `Tyler Wilcox`
* `honorificSuffix`: `CPA`
* `jobTitle`: `Founder`
* `description`: concise summary grounded in the approved page copy
* `url`: `https://velu.us/about`
* `image`: reference the approved Tyler founder image if a hosted URL is available; otherwise reference the page primary image only if appropriate
* `worksFor`: reference `https://velu.us/#organization`
* `affiliation`: reference `https://velu.us/#organization`
* `knowsAbout`: an array of approved professional topics
* `mainEntityOfPage`: reference `https://velu.us/about#webpage`

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

Research the appropriate Schema.org property treatment before final JSON-LD generation.

Possible approaches may include:

* `hasCredential` using `EducationalOccupationalCredential`
* A concise `description`
* `knowsAbout`

Do not invent credential identifiers, issuing URLs, certification dates, or expiration dates.

If the correct Schema.org structure cannot be confidently supported, retain the credentials in visible page copy and omit structured credential objects rather than using uncertain markup.

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

`https://velu.us/about#schedule-action`

### Recommended Properties

* `@type`: `ScheduleAction`
* `@id`: `https://velu.us/about#schedule-action`
* `name`: `Schedule a Discovery Call`
* `target`:
  * `@type`: `EntryPoint`
  * `urlTemplate`: `https://velu.us/get-started/`
* `object`: reference `https://velu.us/#organization`

### Notes

Because the About page promotes a relationship with Velu rather than one specific service, the action object should reference the organization rather than a page-level service entity.

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

## Required Inputs Before JSON-LD Generation

Confirm these before generating the final schema:

1. Hosted About-page social-image URL
2. Exact social-image dimensions
3. Whether the Tyler founder image will have a stable hosted URL
4. Exact official organization entity ID used across the approved site schema
5. Exact official website entity ID used across the approved site schema
6. Whether the visible page retains all approved credibility claims
7. Whether credential objects can be represented confidently with valid Schema.org properties
8. Final visible page URL and canonical URL
9. Final CTA URL
10. Final heading structure and page copy:
    * H1: `Meet Tyler Wilcox, CPA`
    * H2: `Experience Across the Nonprofit Sector`
    * H2: `Looking for a Financial Partner Who Understands Nonprofits?`

## Proposed Validation Checklist

Before GoHighLevel entry, validate:

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
* No duplicated global entities
* No Review or AggregateRating
* No FAQPage
* No unsupported claims

After publication, validate:

* Live page source
* Schema.org Validator
* Google Rich Results Test, recognizing that an About page may not qualify for a special rich result
* Canonical consistency
* Image retrieval
* Robots/noindex status
* Sitemap inclusion

## Schema Status

Record these as complete:

* Page schema strategy drafted
* Proposed entity structure documented
* Person-entity strategy documented
* Review and FAQ exclusions documented
* Required inputs identified

Record these as pending:

* Schema-plan approval
* Hosted social-image URL
* Exact social-image dimensions
* Final credential-property decision
* JSON-LD generation
* Local syntax validation
* GoHighLevel entry
* GoHighLevel validation
* Publication
* Live source verification
* External schema validation

# Get Started Page Schema Plan

## Page Status

* Page: Get Started
* URL: `https://velu.us/get-started/`
* Relative path: `/get-started/`
* Schema-planning status: Approved
* JSON-LD generation status: Complete
* Local validation status: Complete
* GoHighLevel entry status: Pending
* Publication status: Pending
* Live validation status: Pending publication

## Schema Objective

The schema should help search engines understand that:

* This is Velu’s official Get Started and contact page
* The page allows nonprofit leaders to schedule a discovery call
* The appointment is a 45-minute conversation with Tyler J. Wilcox, CPA
* The embedded calendar is the page’s primary functional element
* The page belongs to the existing Velu website and organization entity structure
* The page provides `info@velu.us` as a fallback contact method

The schema must remain grounded in visible page content and must not introduce unsupported services, claims, availability, or appointment details.

## Proposed Top-Level Graph Structure

Use these four top-level entities:

1. `ContactPage`
2. `ImageObject`
3. `BreadcrumbList`
4. `ScheduleAction`

Reference, but do not duplicate, the existing global entities:

* `https://velu.us/#website`
* `https://velu.us/#organization`

Do not add a separate Tyler Wilcox `Person` entity on this page.

Tyler is identified in visible copy and the action name, but the primary purpose of this page is scheduling contact with Velu rather than describing Tyler as an individual.

## Entity 1: ContactPage

### Recommended Type

`ContactPage`

### Recommended ID

`https://velu.us/get-started/#webpage`

### Recommended Properties

* `@type`: `ContactPage`
* `@id`: `https://velu.us/get-started/#webpage`
* `url`: `https://velu.us/get-started/`
* `name`: `Book a Nonprofit Accounting Discovery Call | Velu`
* `description`: `Schedule a 45-minute discovery call with Tyler J. Wilcox, CPA to discuss your nonprofit’s financial needs, current challenges, and goals.`
* `inLanguage`: `en-US`

Use references for:

* `isPartOf` → `https://velu.us/#website`
* `about` → `https://velu.us/#organization`
* `publisher` → `https://velu.us/#organization`
* `breadcrumb` → `https://velu.us/get-started/#breadcrumb`
* `primaryImageOfPage` → `https://velu.us/get-started/#primaryimage`
* `image` → `https://velu.us/get-started/#primaryimage`
* `potentialAction` → `https://velu.us/get-started/#schedule-action`

### Main Entity Treatment

Use the `ScheduleAction` as the page’s primary structured action.

Do not use a separate `Person`, service entity, calendar-event entity, or booking-product entity as the page’s main entity.

* `mainEntity` → `https://velu.us/get-started/#schedule-action`

The `ScheduleAction` is the page’s approved `mainEntity`.

### Contact Information

The visible fallback email is:

`info@velu.us`

Do not add `email` directly to the `ContactPage`.

Do not create a separate `ContactPoint` entity on this page.

The fallback email remains represented in visible page copy only.

Do not add:

* Telephone numbers
* Office hours
* Physical addresses
* Additional contact methods
* Response-time claims

## Entity 2: ImageObject

### Recommended ID

`https://velu.us/get-started/#primaryimage`

### Approved Image

Image name:

`IMAGE_Velu_Get Started_Social Share`

Filename:

`get-started-velu-social-share.png`

Hosted URL:

`https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c58c107cf451b94b0722d.png`

Dimensions:

* Width: `1731`
* Height: `909`

Headline:

`Book a Discovery Call`

Supporting line:

`A 45-Minute Conversation for Nonprofit Leaders`

### Recommended Properties

* `@type`: `ImageObject`
* `@id`: `https://velu.us/get-started/#primaryimage`
* `url`: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c58c107cf451b94b0722d.png`
* `contentUrl`: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c58c107cf451b94b0722d.png`
* `width`: `1731`
* `height`: `909`
* `name`: `Book a Discovery Call`
* `caption`: `Book a 45-minute discovery call with Velu for nonprofit accounting and financial guidance.`
* `inLanguage`: `en-US`

Use a reference for:

* `creator` → `https://velu.us/#organization`

Use numeric values rather than quoted strings for `width` and `height`.

The metadata-only image does not require webpage alt text.

## Entity 3: BreadcrumbList

### Recommended ID

`https://velu.us/get-started/#breadcrumb`

### Recommended Items

Position 1:

* Name: `Home`
* URL: `https://velu.us/`

Position 2:

* Name: `Get Started`
* URL: `https://velu.us/get-started/`

Use exactly two `ListItem` entries with numeric positions `1` and `2`.

Do not add a Services breadcrumb because the page is not nested under a service category.

## Entity 4: ScheduleAction

### Recommended ID

`https://velu.us/get-started/#schedule-action`

### Recommended Properties

* `@type`: `ScheduleAction`
* `@id`: `https://velu.us/get-started/#schedule-action`
* `name`: `Discovery Call With Tyler J. Wilcox, CPA`
* `description`: `Schedule a 45-minute conversation with Tyler J. Wilcox, CPA to discuss a nonprofit organization’s financial needs, challenges, and goals.`

Use this target:

* `@type`: `EntryPoint`
* `urlTemplate`: `https://velu.us/get-started/`
* `actionPlatform`: `https://schema.org/DesktopWebPlatform`
* `actionPlatform`: `https://schema.org/MobileWebPlatform`

Represent multiple action platforms in a valid array if the property is included.

Use a reference for:

* `object` → `https://velu.us/#organization`

### Action Notes

* The action is completed through the embedded calendar on the Get Started page.
* Do not add a scheduled date or time because visitors select from dynamically available appointment times.
* Do not describe the action as a confirmed appointment.
* Do not use `ReserveAction`, `BuyAction`, `OrderAction`, or `RegisterAction`.
* Do not create an `Event` entity for the discovery call.
* Do not include calendar IDs, internal GoHighLevel IDs, or unpublished booking URLs.
* Do not claim availability, response time, or guaranteed acceptance.

## Review and Rating Policy

Do not add:

* `Review`
* `AggregateRating`
* `ratingValue`
* `reviewCount`

The page intentionally contains no testimonials or review section.

## FAQ Policy

Do not add `FAQPage`.

The page contains no visible FAQ section.

## Service-Entity Policy

Do not add:

* `Service`
* `AccountingService`
* `ProfessionalService`
* `Offer`
* `Product`

The page allows visitors to initiate a discovery conversation; it does not present or sell one specific service.

## Person-Entity Policy

Do not add a separate `Person` entity for Tyler Wilcox on this page.

The About page already provides the appropriate structured Person representation.

The Get Started page may name Tyler within:

* Visible copy
* `ScheduleAction.name`
* `ScheduleAction.description`

Do not cross-reference:

`https://velu.us/about-us#tyler-wilcox`

Do not use Tyler as the action’s `agent`, `participant`, `provider`, or another uncertain action property.

Tyler remains represented through visible page copy, `ScheduleAction.name`, and `ScheduleAction.description`.

Keep `ScheduleAction.object` referenced to `https://velu.us/#organization`.

## Additional Exclusions

Do not add:

* Credential objects
* Unsupported social profiles
* Awards or rankings
* Founding dates
* Unsupported service claims
* Appointment availability
* Appointment pricing
* Guaranteed outcomes
* Geographic service limitations
* A duplicated global organization
* A duplicated global website
* Calendar screenshots or visible-image metadata
* Internal GoHighLevel identifiers

## Confirmed Inputs for JSON-LD Generation

* Global organization ID: `https://velu.us/#organization`
* Global website ID: `https://velu.us/#website`
* Final page URL: `https://velu.us/get-started/`
* Booking destination: `https://velu.us/get-started/`
* Appointment name: `Discovery Call With Tyler J. Wilcox, CPA`
* Appointment duration: `45 minutes`
* Fallback email visible in page copy: `info@velu.us`
* Social-image URL: `https://assets.cdn.filesafe.space/p7nQ61CA0CEz850Cs2rU/media/6a3c58c107cf451b94b0722d.png`
* Social-image dimensions: `1731 × 909`
* Final heading structure:
  * H1: `Book a Discovery Call`
  * H2: `Discovery Call With Tyler J. Wilcox, CPA`
  * H2: `Having Trouble Finding a Time That Works?`
* Direct `email` property decision: omitted
* Tyler cross-page Person-reference decision: omitted
* Final page copy confirmed

## Validation Checklist

Completed locally:

* Pure JSON syntax
* No Markdown fences
* No `<script>` tags
* Correct canonical URL
* Correct entity IDs
* Exactly four top-level graph entities
* Unique `@id` values
* Correct organization and website references
* Valid `ContactPage` relationships
* Valid `ScheduleAction` target
* Numeric image dimensions
* Numeric breadcrumb positions
* No duplicated global entities
* No Review or AggregateRating
* No FAQPage
* No service or offer entity
* No separate Person entity
* No unsupported appointment claims
* No placeholder values

The generated graph contains exactly four top-level entities with unique `@id` values. All internal references resolve to a graph entity or the approved global Website and Organization IDs. Image dimensions and breadcrumb positions are numeric. The `ScheduleAction` target contains the approved booking URL and exact desktop/mobile action-platform array.

After publication, validate:

* Live page source
* Schema.org Validator
* Google Rich Results Test, recognizing that this page may not qualify for a special rich result
* Canonical consistency
* Image retrieval
* Robots/noindex status
* XML sitemap inclusion
* Live social preview

## Schema Status

Record as complete:

* Schema-plan approval
* Four-entity architecture approval
* Initial schema strategy drafted
* Proposed four-entity architecture documented
* ContactPage strategy documented
* ScheduleAction strategy documented
* Review, FAQ, service, and Person exclusions documented
* Required inputs identified
* Hosted social-image URL recorded
* Social-image dimensions recorded
* Final page URL recorded
* Direct email-property decision: omitted
* Tyler cross-page Person-reference decision: omitted
* Main-entity decision: `ScheduleAction`
* Global organization and website entity IDs confirmed
* Final booking URL confirmed
* Final image URL and dimensions confirmed
* Final appointment name and duration confirmed
* Final page-copy and heading confirmation
* JSON-LD generation
* Local JSON syntax validation
* Four-entity graph validation
* Entity-ID uniqueness validation
* Internal-reference validation
* Numeric image-dimension validation
* Numeric breadcrumb-position validation
* ScheduleAction target validation
* Prohibited-entity review
* Placeholder and wrapper review

Record as pending:

* GoHighLevel entry
* GoHighLevel page-level validation
* Publication
* Live source verification
* Schema.org Validator
* Google Rich Results Test
* Canonical verification
* Image retrieval verification
* Robots/noindex verification
* XML sitemap verification
* Live social-preview verification

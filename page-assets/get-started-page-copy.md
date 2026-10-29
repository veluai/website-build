# Get Started Page Copy

## Business identity update - 2026-10-28

The full business identity is maintained in the shared global footer. See [the implementation record](../docs/business-identity-implementation.md) for this revision's publication and verification status; older page-build status below is historical.

## Page Status

* Page: Get Started
* Final URL: `/get-started`
* Canonical URL: `https://velu.us/get-started`
* Primary audience: Nonprofit executive directors, leadership teams, and board members
* Primary objective: Encourage qualified nonprofit leaders to schedule a discovery call
* Page-copy status: Approved for implementation
* Visible desktop page content: Approved
* Mobile-page review: Complete
* Visible mobile page content: Approved
* Final visible page content: Approved

## Section 1: Booking Introduction

### Book a Discovery Call

Schedule a 45-minute conversation with Tyler J. Wilcox, CPA to discuss your nonprofit’s financial needs, current challenges, and goals for the future.

There is no obligation. The conversation is simply an opportunity to learn more about your organization, answer your questions, and determine whether Velu may be the right financial partner.

## Section 2: Calendar

### Find a Time That Works for You

`[Existing embedded GoHighLevel calendar]`

### Calendar Implementation Notes

* Retain the existing GoHighLevel calendar embed
* Do not change the calendar workflow or appointment configuration
* The embedded calendar displays `Discovery Call With Tyler J. Wilcox, CPA`
* The embedded calendar displays the duration as `45 min`
* Keep the calendar as the primary visual focus of the page
* Use a restrained white card or content container
* Avoid surrounding the calendar with distracting content

## Section 3: Fallback Contact

### Having Trouble Finding a Time That Works?

Email us at `info@velu.us` and we’ll be happy to help.

Implementation note:

* `info@velu.us` appears as plain text.
* No active `mailto:` link is used.
* This treatment is intentional because GoHighLevel `mailto:` behavior did not work reliably during preview/testing.

## Design Direction

* White or very light neutral background
* Centered H1 and introductory copy
* Navy heading text
* Restrained green or blue accent
* Calendar contained within a clean white panel
* Subtle border or shadow only
* Generous spacing around the calendar
* Maximum content width around 1,000–1,100 pixels
* No large founder image
* No testimonial section
* No additional CTA section

## Heading Structure

* H1: `Book a Discovery Call`
* H2: `Find a Time That Works for You`
* H2: `Having Trouble Finding a Time That Works?`

Use only one H1.

## Page Flow

`Introduction → Appointment Context → Calendar → Fallback Contact`

## Shared Business Identity

Include the [global business identity block](global-business-identity.html) in this page's existing footer, alongside its legal links. Canonical details are maintained in [business-identity.json](../source-data/business-identity.json). This requirement applies to desktop and mobile. Publication and live verification are tracked in [the implementation record](../docs/business-identity-implementation.md).

## Footer navigation - October 29, 2026

Use the shared [full footer source](global-footer-gohighlevel.html), retaining
[canonical business details](global-business-identity.html), with four Services
links, About Velu, Get Started, linked business name, and the smaller legal row.
Business hours are omitted. Desktop uses three columns; mobile stacks contact,
Services, Explore, and legal content. See [rollout status and Google checks](../docs/footer-navigation-implementation.md).

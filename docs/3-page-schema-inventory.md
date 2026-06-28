# Page Schema Inventory

## Purpose

This document maintains a centralized inventory of repository-documented schema implementation across the Velu replacement website.

The inventory should show which pages have schema documented, which top-level schema types are present, whether review markup is excluded, whether offer catalog and breadcrumb requirements are met, whether conversion actions are documented, and who owns final approval.

This inventory reflects repository-documented replacement-site schema, not verified live production output.

## Inventory

| Page | Canonical URL | Status | Top-Level Schema Types | Review Markup | AggregateRating | Offer Count | Breadcrumb Count | ScheduleAction | Images Verified | Schema Validation Status | Primary Standard | Owner |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- |
| Home | https://velu.us/ | Generated and entered in GoHighLevel | WebSite, WebPage, AccountingService | Excluded | Excluded | 4 | Not applicable | Yes | Yes | GoHighLevel validation passed; live validation pending | Homepage Schema Standard | Tyler Wilcox |
| About | https://velu.us/about-us/ | Generated and entered in GoHighLevel | AboutPage, ImageObject, BreadcrumbList, Person, ScheduleAction | Excluded | Excluded | 0 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Utility Page Schema Standard | Tyler Wilcox |
| Get Started | https://velu.us/get-started/ | Generated and entered in GoHighLevel | ContactPage, ImageObject, BreadcrumbList, ScheduleAction | Excluded | Excluded | 0 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Utility Page Schema Standard | Tyler Wilcox |
| Outsourced Accounting Services | https://velu.us/services/nonprofit-outsourced-accounting-services | Generated and entered in GoHighLevel | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | Excluded | Excluded | 4 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Service Page Schema Standard | Tyler Wilcox |
| Grant Advisory & Compliance | https://velu.us/services/nonprofit-grant-advisory-compliance-services | Generated and entered in GoHighLevel | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | Excluded | Excluded | 4 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Service Page Schema Standard | Tyler Wilcox |
| Nonprofit Tax Services | https://velu.us/services/nonprofit-tax-services | Generated and entered in GoHighLevel | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | Excluded | Excluded | 2 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Service Page Schema Standard | Tyler Wilcox |
| Client Advisory Services | https://velu.us/services/nonprofit-client-advisory-services | Generated and entered in GoHighLevel | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | Excluded | Excluded | 4 | 2 | Yes | Yes | GoHighLevel validation passed; live validation pending | Service Page Schema Standard | Tyler Wilcox |

## Page Notes

### Home

- Uses root-domain schema at `https://velu.us/`.
- Defines the global `WebSite` entity at `https://velu.us/#website`.
- Defines the global `AccountingService` organization entity at `https://velu.us/#organization`.
- Excludes Review and AggregateRating markup.
- Does not use `BreadcrumbList`.

### About

- Uses `AboutPage`, `ImageObject`, `BreadcrumbList`, `Person`, and `ScheduleAction`.
- References the global website and organization entities.
- Excludes Review and AggregateRating markup.

### Get Started

- Uses `ContactPage`, `ImageObject`, `BreadcrumbList`, and `ScheduleAction`.
- References the global website and organization entities.
- Excludes Review and AggregateRating markup.

### Outsourced Accounting Services

- Uses `WebPage`, `ImageObject`, `BreadcrumbList`, `Service`, and `ScheduleAction`.
- OfferCatalog items are Financial Reporting, Fund Accounting, Financial Visibility, and Accounting Operations.
- Breadcrumb count is 2: Home and current service page.
- Excludes Review and AggregateRating markup.

### Grant Advisory & Compliance

- Uses `WebPage`, `ImageObject`, `BreadcrumbList`, `Service`, and `ScheduleAction`.
- OfferCatalog count is 4.
- Breadcrumb count is 2 after local remediation: Home and current service page.
- Excludes Review and AggregateRating markup.
- Revised two-item breadcrumb JSON-LD was entered, validated, and saved in GoHighLevel; live validation remains pending publication.

### Nonprofit Tax Services

- Uses `WebPage`, `ImageObject`, `BreadcrumbList`, `Service`, and `ScheduleAction`.
- OfferCatalog count is 2.
- Breadcrumb count is 2 after local remediation: Home and current service page.
- Excludes Review and AggregateRating markup.
- Revised two-item breadcrumb JSON-LD was entered, validated, and saved in GoHighLevel; live validation remains pending publication.

### Client Advisory Services

- Schema plan exists at `page-assets/client-advisory-services-schema-plan.md`.
- Production JSON-LD exists at `page-assets/client-advisory-services-schema.jsonld`.
- Replacement JSON-LD was generated, locally validated, entered in GoHighLevel, saved, and accepted by page-level GoHighLevel validation.
- Old schema was removed.
- Uses approved global IDs: `https://velu.us/#website` and `https://velu.us/#organization`.
- Uses two-item service breadcrumb: Home -> Nonprofit Client Advisory Services.
- Does not include a `/services/` breadcrumb item.
- Excludes page-level Review and AggregateRating markup.
- Publication remains pending; live validation remains pending publication.

### Legal Pages

Privacy Policy and Terms and Conditions are referenced in the footer.

Page-specific schema documentation has not yet been established for those pages.

Do not invent schema structure until page records are created.

## Validation Workflow

1. Confirm canonical page URL.
2. Confirm page content and service components.
3. Confirm image URLs and dimensions match the approved image inventory.
4. Confirm JSON-LD syntax.
5. Confirm the page references global IDs correctly:
   - `https://velu.us/#website`
   - `https://velu.us/#organization`
6. Confirm service breadcrumbs use Home > Current service page unless a real Services landing page is created.
7. Confirm Review and AggregateRating markup are excluded unless a documented exception is approved.
8. Confirm conversion actions point to `https://velu.us/get-started/`.
9. Validate in GoHighLevel before publication.
10. Validate with Schema.org Validator after publication.
11. Test eligible markup with Google Rich Results Test after publication.
12. Mark live validation complete only after live source verification and external validation.

## Future Pages

Future schema implementations should be added to the inventory before being marked complete.

Future page categories include:

- Client Advisory Services current backfill
- Additional service pages
- Legal pages
- Resource pages
- Lead magnets
- Blog content

Future resource pages may require `CreativeWork` schema only after approval and only when the resource is present in the page experience. Future blog content may require `Article` schema only after approval.

Future schema work should follow the [Schema Markup Standard](2-schema-markup-standard.md) and should not be marked complete until schema validation, offer catalog checks, breadcrumb checks, conversion-action checks, review-exclusion checks, and image verification are complete where applicable.

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.1 | Expanded inventory into an operational tracking table and added page notes, validation workflow, and future page guidance. | Tyler Wilcox |
| 2026-06-20 | 1.0 | Initial schema inventory created for current known homepage and service page implementations. | Tyler Wilcox |

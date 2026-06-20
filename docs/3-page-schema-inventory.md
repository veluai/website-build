# Page Schema Inventory

## Purpose

This document maintains a centralized inventory of schema implementation across the Velu website.

The inventory should show which pages have schema implemented, which schema types are present, whether review and offer catalog requirements are met, whether breadcrumbs and conversion actions are implemented, whether images have been verified, and who owns final approval.

## Inventory

| Page | URL | Page Purpose | Status | Schema Types | Reviews | OfferCatalog | Breadcrumb | ScheduleAction | Lead Magnet | Images Verified | Schema Validated | Primary Standard | Last Updated | Owner |
| ---- | --- | ------------ | ------ | ------------ | ------- | ------------ | ---------- | -------------- | ----------- | --------------- | ---------------- | ---------------- | ------------ | ----- |
| Home | / | Establish Velu as a nonprofit accounting and advisory firm and direct qualified visitors toward the get-started conversion path. | Complete | WebSite, WebPage, AccountingService, OfferCatalog, AggregateRating, CreativeWork, ScheduleAction | Yes | Yes | No | Yes | Yes | Yes | Pending external validation | Homepage Schema Standard | 2026-06-20 | Tyler Wilcox |
| Outsourced Accounting Services | /services/outsourced-accounting-services | Generate qualified opportunities for nonprofit outsourced accounting services. | Complete | WebPage, Service, OfferCatalog, BreadcrumbList, AggregateRating, Review, ScheduleAction | Yes | Yes | Yes | Yes | No | Yes | Pending external validation | Service Page Schema Standard | 2026-06-20 | Tyler Wilcox |
| Client Advisory Services | /services/client-advisory-services | Generate qualified opportunities for nonprofit client advisory services. | Complete | WebPage, Service, OfferCatalog, BreadcrumbList, AggregateRating, Review, ScheduleAction | Yes | Yes | Yes | Yes | No | Yes | Pending external validation | Service Page Schema Standard | 2026-06-20 | Tyler Wilcox |

## Page Notes

### Home

- Uses root-domain schema at https://velu.us/.
- Positions Velu as a nonprofit accounting and advisory firm.
- Includes `CreativeWork` schema for The First Steps to Start a Nonprofit.
- Does not use `BreadcrumbList`.

### Outsourced Accounting Services

- Uses `Service` schema.
- OfferCatalog pillars are Financial Reporting, Fund Accounting, Financial Visibility, and Accounting Operations.
- Uses nonprofit-focused review set.

### Client Advisory Services

- Uses `Service` schema.
- OfferCatalog pillars are Budgeting & Financial Planning, Budget Performance Analysis, Forecasting & Financial Visibility, and Board & Leadership Reporting.
- Uses nonprofit-focused review set.

## Validation Workflow

1. Confirm live page URL.
2. Confirm page content and service components.
3. Confirm reviews are visible on page.
4. Confirm image URLs resolve.
5. Confirm JSON-LD syntax.
6. Validate with Google Rich Results Test.
7. Validate with Schema.org validator.
8. Mark Schema Validated as complete only after validation.

## Future Pages

Future schema implementations should be added to the inventory before being marked complete.

Future page categories include:

- Grant Advisory & Compliance
- Additional service pages
- Resource pages
- Lead magnets
- Blog content

Grant Advisory & Compliance should be treated as planned, not complete. Do not add its production schema URL until the live page exists.

Future resource pages may require `CreativeWork` schema. Future blog content may require `Article` schema only after approval.

Future schema work should follow the [Schema Markup Standard](2-schema-markup-standard.md) and should not be marked complete until schema validation, review-content checks, offer catalog checks, breadcrumb checks, conversion-action checks, and image verification are complete where applicable.

## Revision History

| Date | Version | Summary | Owner |
| --- | --- | --- | --- |
| 2026-06-20 | 1.1 | Expanded inventory into an operational tracking table and added page notes, validation workflow, and future page guidance. | Tyler Wilcox |
| 2026-06-20 | 1.0 | Initial schema inventory created for current known homepage and service page implementations. | Tyler Wilcox |

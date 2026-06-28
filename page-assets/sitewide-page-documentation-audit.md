# Velu Sitewide Page Documentation Audit

## Audit Scope

- Repository reviewed: `/Users/tyler.wilcox/Documents/website-build/`
- Date of audit: 2026-06-26
- File types reviewed: Markdown, JSON-LD, JSON, text source records, and repository image files under `assets/images/`
- Audit-only status: This report documents findings only. No existing repository documentation, JSON-LD, image files, source files, or GoHighLevel records were modified for this audit.
- Existing unrelated workspace changes were preserved.

Files reviewed:

- Text and structured files reviewed: 55
- Image files reviewed: 58
- Total files reviewed: 113
- JSON-LD files parsed: 6

## Executive Summary

- Pages identified: 8
- Critical issue count: 0
- High issue count: 7
- Medium issue count: 10
- Low issue count: 5
- Pages with complete documentation: 5
- Pages with partial documentation: 2
- Pages with missing documentation: 1

Pages with complete documentation:

- Home
- About
- Get Started
- Outsourced Accounting
- Grant Advisory & Compliance

Pages with partial documentation:

- Nonprofit Tax Services
- Client Advisory Services

Pages with missing documentation:

- Privacy Policy and Terms and Conditions are referenced in the global footer but do not have page-specific repository records.

Top five recommended remediation priorities:

1. Remove the non-existent `/services/` breadcrumb item from Grant Advisory and Tax schema plans and JSON-LD.
2. Update global schema standards and page schema inventory to match the current no-page-level-review policy.
3. Reconcile About page status files so copy and SEO no longer say image/schema workflows are pending.
4. Reconcile Tax SEO status language about Open Graph fields with the known GoHighLevel field limitations.
5. Create or backfill missing Client Advisory page records, or clearly mark the current source file as reference-only.

## Sitewide Standards Observed

The repository is broadly consistent on these standards:

- Replacement GoHighLevel site is documented as unpublished, with live verification pending.
- Final service URLs use the nonprofit-prefixed service paths.
- Current page JSON-LD files are pure JSON and parse successfully.
- Current page JSON-LD files avoid page-level `Review` and `AggregateRating` markup.
- Social-sharing images are generally stored in `assets/images/`, documented with hosted URLs, and marked metadata-only where appropriate.
- The primary CTA destination is consistently `https://velu.us/get-started/`.
- The repository generally treats Git history as version history in new page-asset records.

## Page Documentation Inventory

| Page name | Final URL | Copy file | SEO file | Schema-plan file | JSON-LD file | Image inventory | Image brief | Image prompts | Review inventory or reference | Desktop status | Mobile status | GHL implementation status | Publication status | Live-validation status | Completeness assessment | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | `https://velu.us/` | `page-assets/home-page-copy.md` | `page-assets/home-page-seo.md` | `page-assets/home-page-schema-plan.md` | `page-assets/home-page-schema.jsonld` | `page-assets/home-page-image-inventory.md` | Not documented | Not documented | `page-assets/home-page-review-inventory.md` | Completed | Deferred | Implemented in GoHighLevel | Pending | Pending | Complete | Image brief/prompts are not required now that inventory and implementation records exist, but absence should be intentional. |
| About | `https://velu.us/about-us/` | `page-assets/about-page-copy.md` | `page-assets/about-page-seo.md` | `page-assets/about-page-schema-plan.md` | `page-assets/about-page-schema.jsonld` | `page-assets/about-page-image-inventory.md` | `page-assets/about-page-image-brief.md` | `page-assets/about-page-image-prompts.md` | Not applicable | Not documented | Not documented | Entered and confirmed in SEO/schema/image files | Pending | Pending | Complete with status conflicts | Copy and SEO files still contain stale pending-workflow language. |
| Get Started | `https://velu.us/get-started/` | `page-assets/get-started-page-copy.md` | `page-assets/get-started-page-seo.md` | `page-assets/get-started-page-schema-plan.md` | `page-assets/get-started-page-schema.jsonld` | `page-assets/get-started-page-image-inventory.md` | `page-assets/get-started-page-image-brief.md` | `page-assets/get-started-page-image-prompts.md` | Not applicable | Complete | Complete | SEO and schema entered/validated in GoHighLevel | Pending | Pending | Complete | Image brief says Open Graph implementation pending while SEO indicates social image entry complete. |
| Outsourced Accounting | `https://velu.us/services/nonprofit-outsourced-accounting-services` | `page-assets/outsourced-accounting-page-copy.md` | `page-assets/outsourced-accounting-page-seo.md` | `page-assets/outsourced-accounting-page-schema-plan.md` | `page-assets/outsourced-accounting-page-schema.jsonld` | `page-assets/outsourced-accounting-page-image-inventory.md` | Not documented | Not documented | References `page-assets/home-page-review-inventory.md` | Approved | Deferred | Implemented in GoHighLevel | Pending | Pending | Complete | Uses correct two-item service breadcrumb. |
| Client Advisory Services | `https://velu.us/services/nonprofit-client-advisory-services` | Missing | Missing | Missing | Missing | Missing | Missing | Missing | Source schema includes reviews in `source-data/approved-client-advisory-schema-source.txt` | Not documented | Not documented | Not documented | Not documented | Not documented | Missing | Only a reference schema source exists; current page records are not backfilled. |
| Grant Advisory & Compliance | `https://velu.us/services/nonprofit-grant-advisory-compliance-services` | `page-assets/grant-advisory-compliance-page-copy.md` | `page-assets/grant-advisory-compliance-seo.md` | `page-assets/grant-advisory-compliance-schema-plan.md` | `page-assets/grant-advisory-compliance-schema.jsonld` | `page-assets/grant-advisory-compliance-image-inventory.md` | `page-assets/grant-advisory-compliance-image-brief.md` | `page-assets/grant-advisory-compliance-image-prompts.md` | References approved review source in schema plan | Not documented | Not documented | Schema entered/saved in GoHighLevel per plan | Pending | Pending | Complete with schema issue | Breadcrumb still includes non-existent `/services/` item. |
| Nonprofit Tax Services | `https://velu.us/services/nonprofit-tax-services` | `page-assets/nonprofit-tax-services-page-copy.md` | `page-assets/nonprofit-tax-services-seo.md` | `page-assets/nonprofit-tax-services-schema-plan.md` | `page-assets/nonprofit-tax-services-schema.jsonld` | `page-assets/nonprofit-tax-services-image-inventory.md` | `page-assets/nonprofit-tax-services-image-brief.md` | `page-assets/nonprofit-tax-services-image-prompts.md` | Uses visible review carousel; no page-level review markup | Complete | Complete | Implemented in GoHighLevel per SEO/schema records | Pending | Pending | Partially complete | Breadcrumb still includes non-existent `/services/` item; SEO status overstates separate Open Graph field implementation. |
| Privacy Policy / Terms and Conditions | Not documented | Missing | Missing | Missing | Missing | Not applicable | Not applicable | Not applicable | Not applicable | Not documented | Not documented | Not documented | Not documented | Not documented | Missing | Referenced in Home/global footer copy but no page records were found. |

## Critical Issues

No Critical issues were identified in the repository files reviewed. All current `.jsonld` files parse successfully, no page-level Review or AggregateRating markup exists in current JSON-LD, and no active old service URLs were found.

## High-Priority Issues

| Issue ID | Page | File | Line or section | Issue | Why it matters | Recommended correction | Source of truth | Confidence |
|---|---|---|---|---|---|---|---|---|
| HIGH-001 | Grant Advisory & Compliance | `page-assets/grant-advisory-compliance-schema.jsonld` | Lines 63-68 | Breadcrumb includes a `Services` item pointing to `https://velu.us/services/`. | Known standard says there is no dedicated `/services/` landing page. Service breadcrumbs should use Home > Current service page. | Remove the `Services` breadcrumb item and renumber the current page item to position 2. | Audit standard: Service breadcrumb standard; Outsourced Accounting schema implementation. | High |
| HIGH-002 | Grant Advisory & Compliance | `page-assets/grant-advisory-compliance-schema-plan.md` | Lines 227-233 | Schema plan documents `/services/` as the coordinated intermediate breadcrumb page. | This contradicts the current sitewide standard and the newer Outsourced Accounting breadcrumb decision. | Update plan to document two breadcrumb items only: Home and Grant Advisory & Compliance. | Audit standard: no dedicated `/services/` landing page. | High |
| HIGH-003 | Nonprofit Tax Services | `page-assets/nonprofit-tax-services-schema.jsonld` | Lines 60-65 | Breadcrumb includes a `Services` item pointing to `https://velu.us/services/`. | Same risk as HIGH-001: a breadcrumb points to a non-existent page. | Remove the `Services` breadcrumb item and renumber the current page item to position 2. | Audit standard: Service breadcrumb standard; Outsourced Accounting schema implementation. | High |
| HIGH-004 | Nonprofit Tax Services | `page-assets/nonprofit-tax-services-schema-plan.md` | Lines 310-316 | Schema plan documents `/services/` as planned intermediate breadcrumb page. | The plan conflicts with the current breadcrumb standard and the JSON-LD will likely be regenerated incorrectly if this remains. | Update the plan to use a two-item breadcrumb. | Audit standard: no dedicated `/services/` landing page. | High |
| HIGH-005 | Global schema docs | `docs/3-page-schema-inventory.md` | Lines 13-15 | Schema inventory says Home includes `AggregateRating` and `CreativeWork`, and service pages include `AggregateRating` and `Review`. | This conflicts with current JSON-LD and the current review policy. It creates a high risk that future agents reintroduce self-serving review markup. | Update schema inventory to match current JSON-LD: Home has `WebSite`, `WebPage`, `AccountingService`; service pages exclude Review and AggregateRating unless explicitly approved. | Current page JSON-LD files and `page-assets/home-page-review-inventory.md`. | High |
| HIGH-006 | Global schema standard | `docs/2-schema-markup-standard.md` | Lines 98-127 and 193-221 | Standard still describes 12-review aggregate counts and Review/AggregateRating as expected schema components. | Current policy excludes page-level Review and AggregateRating markup for broad Velu testimonials. The standard is stale. | Update standard to distinguish visible review carousels from structured Review markup and document current exclusion policy. | Current page schema plans and review inventory. | High |
| HIGH-007 | Nonprofit Tax Services | `page-assets/nonprofit-tax-services-seo.md` | Lines 261-263 | SEO file says Open Graph title and description are implemented and confirmed in GoHighLevel. | The known sitewide standard says GoHighLevel currently exposes only the social image URL in page settings. | Revise status to say social image is implemented; separate Open Graph title/description/URL/type fields are not available unless independently confirmed. | Audit standard: Social-sharing images and GoHighLevel field availability. | High |

## Medium-Priority Issues

| Issue ID | Page | File | Line or section | Issue | Why it matters | Recommended correction | Source of truth | Confidence |
|---|---|---|---|---|---|---|---|---|
| MED-001 | About | `page-assets/about-page-copy.md` | Lines 11-12 | Copy says SEO, image, and schema work are pending separate workflows. | This conflicts with existing About SEO, image, and schema files that document completed work. | Update copy status to reference completed SEO, image, and schema records while keeping publication/live verification pending. | About SEO, image inventory, schema plan, and `about-page-schema.jsonld`. | High |
| MED-002 | About | `page-assets/about-page-seo.md` | Lines 10 and 291 | SEO says schema is pending, but schema plan and JSON-LD exist and plan documents JSON-LD generation/validation complete. | Conflicting status makes implementation tracking unreliable. | Update SEO status to say schema JSON-LD exists and GoHighLevel entry/validation is complete if that remains true. | `page-assets/about-page-schema-plan.md` lines 333-355 and `about-page-schema.jsonld`. | High |
| MED-003 | Get Started | `page-assets/get-started-page-image-brief.md` | Lines 10-13 | Image brief says Open Graph implementation pending. | Get Started SEO records social image metadata entry as complete in prior workflow, creating status mismatch. | Reconcile image brief/inventory with SEO: distinguish social image uploaded/entered from live preview verification pending. | `page-assets/get-started-page-seo.md` implementation status. | Medium |
| MED-004 | Grant Advisory & Compliance | `page-assets/grant-advisory-compliance-image-prompts.md` | Lines 190-206 | Prompt section still names Supporting Image 3 as `Restricted Grant Funding & Compliance`, while inventory uses final `Restricted Funding & Compliance`. | Stale naming can confuse future image regeneration or implementation. | Update prompts file to use the final pillar/image name or mark old prompt wording as superseded. | `page-assets/grant-advisory-compliance-image-inventory.md` line 16. | High |
| MED-005 | Client Advisory Services | `source-data/approved-client-advisory-schema-source.txt` | Lines 140-147 | Reference source still contains `AggregateRating` and `Review` markup. | It is under `source-data`, but future agents may copy it into current schema work unless marked superseded/reference-only. | Add a non-destructive note in a future task identifying this as historical/reference structure, not current page-level review policy. | Current review policy and current service JSON-LD files. | Medium |
| MED-006 | Client Advisory Services | `page-assets/` | File completeness | No current page copy, SEO, schema plan, JSON-LD, image inventory, or image records were found. | Client Advisory is a core service page in global docs and navigation but lacks current page-specific repository records. | Backfill Client Advisory page files or explicitly mark the existing source-data schema as reference-only until backfill occurs. | Final service URL standard and `source-data/approved-client-advisory-schema-source.txt`. | High |
| MED-007 | Legal pages | Footer references in `page-assets/home-page-copy.md` | Global footer section | Privacy Policy and Terms and Conditions are referenced, but no page-specific records were found. | Legal pages may be required for publication and need approval/status tracking. | Create legal-page records or add a documented source-of-truth location for legal content and URLs. | Global footer in Home copy. | Medium |
| MED-008 | Home | `page-assets/home-page-image-inventory.md` | Lines 14-25 | Several visible Home image current-alt fields say "Not documented in repository; verify in GoHighLevel." | Accessibility implementation remains unclear for multiple Home images. | Verify and document final Home alt text or decorative treatment in a future task. | Image inventory and live/GHL implementation. | High |
| MED-009 | Tax Services | `page-assets/nonprofit-tax-services-image-brief.md` | Lines 343-351 | Image brief says social image uploaded and hosted URL documented, but GoHighLevel implementation remains pending. SEO says social-sharing image and JSON-LD are implemented and confirmed. | Status conflict between image brief and SEO implementation record. | Reconcile image brief with SEO if GHL implementation is confirmed, while keeping live verification pending. | `page-assets/nonprofit-tax-services-seo.md` lines 253-267 and 311. | Medium |
| MED-010 | Grant Advisory & Compliance | `page-assets/grant-advisory-compliance-image-inventory.md` | Lines 13-22 | Page images and icons show website implementation status pending verification, but schema and SEO records indicate broader implementation progress. | May be accurate, but the distinction between repository-present, builder-selected, and live-verified should be kept consistent. | Confirm whether non-social images are in the builder; update statuses only if Tyler confirms. | Image inventory and GoHighLevel page builder. | Medium |

## Low-Priority and Standardization Issues

| Issue ID | Page | File | Line or section | Issue | Why it matters | Recommended correction | Source of truth | Confidence |
|---|---|---|---|---|---|---|---|---|
| LOW-001 | About / Service pages | `page-assets/about-page-copy.md` | Line 120 | About CTA microcopy uses `30-minute conversation`, while service pages and Get Started use 45-minute language. | The audit standard allows context differences, but this could confuse users if the same booking calendar is used. | Human confirmation: decide whether About should remain 30 minutes or align to 45 minutes. | Get Started appointment duration and service-page microcopy standard. | Medium |
| LOW-002 | Schema action wording | Several `.jsonld` files | `ScheduleAction.name` | Some older schemas use `Schedule a Discovery Call`, while newer pages use `Book Your Discovery Call`. | This is not technically invalid, but CTA naming could be standardized for maintainability. | Standardize ScheduleAction names only if GoHighLevel page content uses the same label. | Primary CTA standard. | Medium |
| LOW-003 | Markdown structure | Several copy files | Section headings | Some copy files use documentation headings like `## Section 1` followed by intended page `##` headings. | This is readable for humans but can blur documentation structure versus webpage semantic hierarchy. | Keep as-is or standardize future copy files with a separate "Intended Heading Hierarchy" table. | Existing copy files. | Medium |
| LOW-004 | Custom meta tag capitalization | Home, Tax, Outsourced SEO files | Custom meta tag tables | Home uses lowercase tag names; Outsourced and Tax use title case in different places. | GoHighLevel may preserve exact names; inconsistent casing can complicate audits. | Human confirmation: decide whether tag names should be case-standardized across pages or preserve per-page GHL entry. | SEO files and GHL implementation. | Medium |
| LOW-005 | Image prompt files | Produced image prompts | Multiple image-prompt files | Prompt files remain active-looking after production is complete. | Future agents may treat old production prompts as current implementation requirements. | Add "source prompt only; final asset/inventory is source of truth" status in a future cleanup batch. | Image inventories and image briefs. | Medium |

## URL Audit

Final approved URLs:

- Home: `https://velu.us/`
- About: `https://velu.us/about-us/`
- Get Started: `https://velu.us/get-started/`
- Outsourced Accounting: `https://velu.us/services/nonprofit-outsourced-accounting-services`
- Client Advisory Services: `https://velu.us/services/nonprofit-client-advisory-services`
- Grant Advisory & Compliance: `https://velu.us/services/nonprofit-grant-advisory-compliance-services`
- Tax Services: `https://velu.us/services/nonprofit-tax-services`

Old URL occurrences found:

- Active old service URLs searched:
  - `/services/outsourced-accounting-services`
  - `/services/client-advisory-services`
  - `/services/grant-advisory-compliance-services`
  - `/services/grant-advisory-compliance`
  - `/services/tax-services`
- Result: no active old service URL references found.

Notable URL issues:

| URL or pattern | Exact files | Occurrence type | Recommended treatment |
|---|---|---|---|
| `https://velu.us/services/` | `page-assets/grant-advisory-compliance-schema.jsonld`, `page-assets/grant-advisory-compliance-schema-plan.md`, `page-assets/nonprofit-tax-services-schema.jsonld`, `page-assets/nonprofit-tax-services-schema-plan.md` | Incorrect active breadcrumb reference | Remove from service breadcrumbs unless a real Services landing page is created. |
| `https://velu.us/services/nonprofit-client-advisory-services` | Present in source schema and Home/Outsourced links | Active final URL | Keep. Current Client Advisory page records are missing and should be backfilled. |

Historical references intentionally retained:

- None identified as explicitly historical/deprecated URL documentation.

## CTA Audit

Consistent findings:

- Current primary conversion destination is consistently `https://velu.us/get-started/`.
- Home and Outsourced service copy use `Book Your Discovery Call`.
- Get Started page consistently documents a 45-minute appointment.

Potential inconsistencies:

- About page microcopy uses `No obligation · 30-minute conversation · See if we’re the right fit` in `page-assets/about-page-copy.md` line 120.
- Grant Advisory page copy uses 30-minute microcopy in `page-assets/grant-advisory-compliance-page-copy.md` lines 25 and 167.
- Some schema files use `Schedule a Discovery Call` rather than `Book Your Discovery Call`, including Tax JSON-LD and Grant JSON-LD.

Recommended treatment:

- Confirm whether About and Grant should keep 30-minute visible microcopy or align with the 45-minute Get Started appointment and newer service-page standard.
- Standardize `ScheduleAction.name` only after confirming exact GHL labels.

## Status Audit

Confirmed status conflicts:

- About copy says SEO, image, and schema work are pending, while corresponding About files exist and record completion/GoHighLevel entry.
- Get Started image brief still says Open Graph implementation pending, while SEO has recorded available metadata entry completion.
- Tax image brief says GoHighLevel implementation remains pending, while Tax SEO says social image and JSON-LD are implemented and confirmed.

Recommended treatment:

- Use each page's SEO file and schema plan as the implementation-status source of truth.
- Use image inventory as the source of truth for repository filenames, dimensions, hosted URLs, and alt text.
- Keep publication and live verification pending unless live evidence is documented.

## SEO Audit

SEO files found:

- `page-assets/about-page-seo.md`
- `page-assets/get-started-page-seo.md`
- `page-assets/grant-advisory-compliance-seo.md`
- `page-assets/home-page-seo.md`
- `page-assets/nonprofit-tax-services-seo.md`
- `page-assets/outsourced-accounting-page-seo.md`

SEO completeness:

- Home, About, Get Started, Grant, Tax, and Outsourced Accounting have SEO records.
- Client Advisory has no current SEO record.
- Privacy Policy and Terms and Conditions have no SEO records.

SEO issues:

- Tax SEO overstates implementation of separate Open Graph title and description fields.
- About SEO has stale pending schema status.
- Custom meta tag casing varies across pages.

## Schema Audit

| File | Parse result | Entity count | Entity types | Canonical | Breadcrumb count | Review markup present | AggregateRating present | Duplicate global entities | Old URLs present | Result |
|---|---|---:|---|---|---|---|---|---|---|---|
| `page-assets/about-page-schema.jsonld` | Valid | 5 | AboutPage, ImageObject, BreadcrumbList, Person, ScheduleAction | `https://velu.us/about-us/` | 2 | No | No | No full duplicate global entity | No | Pass |
| `page-assets/get-started-page-schema.jsonld` | Valid | 4 | ContactPage, ImageObject, BreadcrumbList, ScheduleAction | `https://velu.us/get-started/` | 2 | No | No | No full duplicate global entity | No | Pass |
| `page-assets/grant-advisory-compliance-schema.jsonld` | Valid | 5 | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | `https://velu.us/services/nonprofit-grant-advisory-compliance-services` | 3 | No | No | No full duplicate global entity | No | Needs breadcrumb fix |
| `page-assets/home-page-schema.jsonld` | Valid | 3 | WebSite, WebPage, AccountingService | `https://velu.us/` | Not applicable | No | No | Home intentionally defines global entities | No | Pass |
| `page-assets/nonprofit-tax-services-schema.jsonld` | Valid | 5 | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | `https://velu.us/services/nonprofit-tax-services` | 3 | No | No | No full duplicate global entity | No | Needs breadcrumb fix |
| `page-assets/outsourced-accounting-page-schema.jsonld` | Valid | 5 | WebPage, ImageObject, BreadcrumbList, Service, ScheduleAction | `https://velu.us/services/nonprofit-outsourced-accounting-services` | 2 | No | No | No full duplicate global entity | No | Pass |

Technical notes:

- Duplicate `@id` references appear inside graphs because entities reference each other. No duplicate full global entity definitions were found outside the Home page, which intentionally defines `WebSite` and `AccountingService`.
- `source-data/approved-client-advisory-schema-source.txt` is not `.jsonld`; it contains reference JSON-like source content and includes `Review` and `AggregateRating` structures. Treat it as stale/reference-only until Client Advisory backfill is completed.

## Image and Accessibility Audit

Summary:

- Repository image folders exist for About, Get Started, Grant Advisory, Home, Outsourced Accounting, and Tax Services.
- Social-sharing images generally have repository paths, hosted URLs, and exact dimensions.
- Metadata-only social images are generally marked as not requiring webpage alt text.
- About page image accessibility is unusually complete, with visible-image alt text documented as entered and verified.

Image documentation concerns:

- Home inventory still lists several current alt text fields as not documented in repository and needing GoHighLevel verification.
- Grant image prompts contain stale pillar naming for `Restricted Grant Funding & Compliance`, while inventory uses final `Restricted Funding & Compliance`.
- Tax image brief status appears stale relative to SEO implementation status.
- Prompt files across pages are useful historical production records but should not supersede image inventories.

Accessibility concerns:

- Home service/problem icons are marked decorative with empty recommended alt text; this may be appropriate because adjacent headings carry meaning, but it should be confirmed against final rendered HTML.
- About sector icons use descriptive alt text rather than empty alt text; this is approved in About records and should not be changed without human confirmation.
- Metadata-only social images should remain without webpage alt text unless displayed visibly.

## Missing or Incomplete Files

| Page | Missing or incomplete file | Severity | Notes |
|---|---|---|---|
| Client Advisory Services | Copy, SEO, schema plan, JSON-LD, image inventory, image brief, image prompts | Medium | Core service page is referenced but not backfilled as current page assets. |
| Privacy Policy | Copy/legal source, SEO, implementation record | Medium | Referenced in footer; no page records found. |
| Terms and Conditions | Copy/legal source, SEO, implementation record | Medium | Referenced in footer; no page records found. |
| Home | Image brief and image prompts | Low | May be intentionally unnecessary after inventory/backfill; document source-of-truth hierarchy if omitted. |
| Outsourced Accounting | Image brief and prompts | Low | May be intentionally unnecessary after image inventory/backfill; document source-of-truth hierarchy if omitted. |

## Source-of-Truth Recommendations

- Visible copy: page-specific `*-page-copy.md`
- SEO metadata: page-specific `*-page-seo.md`
- Image details: page-specific `*-image-inventory.md`
- Review records: `page-assets/home-page-review-inventory.md` for sitewide visible review carousel, with `source-data/Reviews.md` as source-data record
- Schema strategy: page-specific `*-schema-plan.md`
- Final JSON-LD: page-specific `*.jsonld`
- Page implementation status: SEO file for metadata/GHL entry, schema plan for schema entry, image inventory for image implementation
- Global URLs: this audit's final URL list until moved into a maintained global URL inventory
- Global entity IDs: Home schema plan and Home JSON-LD

## Recommended Remediation Sequence

1. Critical correctness fixes
   - None identified.
2. URL and CTA normalization
   - Confirm 30-minute versus 45-minute language for About and Grant.
   - Standardize ScheduleAction names where appropriate.
3. Schema corrections
   - Fix Grant and Tax breadcrumbs to remove `/services/`.
   - Update global schema standards to current no-review-markup policy.
4. Status cleanup
   - Reconcile About, Get Started, and Tax status contradictions.
5. Image documentation cleanup
   - Update stale Grant prompt naming.
   - Verify Home visible-image alt text in GoHighLevel.
6. Accessibility review
   - Confirm Home decorative icon treatment against rendered page.
7. Documentation standardization
   - Standardize source-of-truth sections and custom meta-tag casing policy.
8. Post-publication verification preparation
   - Ensure each page has a consistent post-publication checklist and live-validation status.

## Proposed Codex Fix Batches

| Batch name | Files affected | Exact objective | Risks | Validation needed | Human approval required |
|---|---|---|---|---|---|
| Breadcrumb correction batch | Grant and Tax schema plans and JSON-LD | Remove non-existent `/services/` breadcrumb items and renumber current page breadcrumb item to 2. | JSON-LD already entered in GoHighLevel may need re-entry. | JSON parse; breadcrumb count equals 2; no `/services/` breadcrumb item. | Yes, because it may require GHL schema re-entry. |
| Schema policy cleanup batch | `docs/2-schema-markup-standard.md`, `docs/3-page-schema-inventory.md` | Align global standards with current Review/AggregateRating exclusion policy. | Could affect future workflow assumptions. | Search for stale Review/AggregateRating requirements; compare with current JSON-LD. | Yes. |
| Status reconciliation batch | About, Get Started, Tax image/SEO/schema records | Resolve pending/complete contradictions without changing live claims. | Requires knowing actual GHL state. | Search for pending/complete contradictions after edits. | Yes where GHL state is unclear. |
| Client Advisory backfill batch | New Client Advisory page assets | Create current copy, SEO, schema, image, and implementation records. | Requires approved page copy/assets/source details. | JSON validation; URL checks; file completeness. | Yes. |
| Image documentation cleanup batch | Grant image prompts; Home image inventory | Mark prompts as source prompts only and verify Home alt text. | Could accidentally overwrite approved prompt history. | No binary changes; table validation; status consistency checks. | Yes for Home alt text verification. |
| Legal page documentation batch | New Privacy and Terms records | Add legal page source/status records or identify external source. | Legal content requires approval. | Confirm URLs, footer links, approval status. | Yes. |

## Items Requiring Human Confirmation

- Whether About and Grant CTA microcopy should remain 30 minutes or change to 45 minutes.
- Whether the visible live/GHL pages already have corrected two-item breadcrumbs in schema, or whether GHL must be updated.
- Whether Tax separate Open Graph title/description fields were actually available and entered in GoHighLevel.
- Whether Home visible images have final alt text or decorative treatment entered in GoHighLevel.
- Whether Client Advisory has approved current page copy/assets outside the repository.
- Whether Privacy Policy and Terms and Conditions are approved and where their source content is stored.
- Whether any QuickBooks ProAdvisor or credential claims remain current as of publication.

## Audit Validation

- Report exists: yes, `page-assets/sitewide-page-documentation-audit.md`
- Existing files modified during this audit: no
- Image binaries modified: no
- JSON-LD files modified: no
- Files deleted: no
- Files renamed: no
- Unrelated workspace changes preserved: yes
- Git history remains the version history: yes
- All `.jsonld` files were parsed: yes, 6 of 6 valid
- Every identified page appears in the page inventory: yes
- Every issue has a severity and recommended correction: yes
- Old service URLs were searched repository-wide: yes
- CTA duration inconsistencies were searched repository-wide: yes
- Review and AggregateRating markup were searched repository-wide: yes
- Global entity references were checked in JSON-LD: yes
- Image filenames, URLs, and dimensions were compared across available inventories/files: yes

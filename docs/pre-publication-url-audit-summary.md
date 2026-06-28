# Pre-Publication URL Audit Summary

## Purpose

This file summarizes the working URL audit before classification. It is intended to help Tyler understand the current WordPress URL set, search-visibility patterns, and likely classification batches before final preservation, redirect, archive, or discard decisions are made.

## Source File

- Source CSV: `docs/pre-publication-url-audit.csv`
- Site transition: WordPress to GoHighLevel rebuild
- Classification status: Not final
- Publication status: Pending
- Live validation: Not performed

Core strategic lens:

`Preserve old URLs only when they have SEO value and support Velu’s current buyer-focused positioning. Do not preserve traffic for its own sake if the likely visitor is a practitioner, DIY template seeker, student, or wrong-fit lead.`

## Overall Counts

- Total rows: 368
- Unique old URLs: 368
- URLs in XML sitemap: 49
- URLs with GSC data: 118
- GSC-only URLs: 43
- 200-status URLs: 271
- Non-200 URLs: 54
- Indexable URLs: 265
- Non-indexable URLs: 60

## Counts By Content Type

| Content Type | Count | Notes |
| --- | ---: | --- |
| Media | 198 | Mostly image or upload URLs; likely no special preservation unless referenced by important content. |
| Blog post | 43 | Mixed strategic fit; includes some high-GSC URLs requiring manual review. |
| Category / tag / archive | 42 | Mostly low strategic fit; likely discard or no special preservation unless data suggests otherwise. |
| Resource | 37 | Many appear technical or practitioner-focused; likely archive/future-funnel candidates. |
| Service page | 21 | Highest-priority preservation review group after core pages. |
| Template | 16 | Likely future-funnel archive candidates rather than launch-site pages. |
| Homepage | 4 | Preserve or redirect to the new homepage where appropriate. |
| About page | 4 | Preserve or redirect to `https://velu.us/about-us` where appropriate. |
| Legal page | 2 | Preserve or redirect to the new legal page URLs. |
| Contact / booking page | 1 | Preserve or redirect to `https://velu.us/get-started`. |

## Counts By Preliminary Category

| Category | Count | Notes |
| --- | ---: | --- |
| Review | 283 | Most rows remain for manual review, especially media, archives, and uncertain blog posts. |
| Archive for Funnel | 53 | Mostly templates, checklists, QuickBooks, technical accounting, and practitioner-oriented resources. |
| Preserve / Redirect | 32 | Mostly core pages, service pages, legal pages, and obvious buyer-intent URLs. |
| Blank / Unclassified | 0 | The working CSV currently uses preliminary categories for every row. These are not final decisions. |

## Top Search Console URLs

Top URLs by clicks and impressions:

| Old URL | Clicks | Impressions | Position | Likely Audience | Strategic Fit | Preliminary Category | Notes |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| `https://velu.us/` | 320 | 20368 | 10.03 | CEO/ED/COO | Trust | Preserve / Redirect | Homepage and brand relevance. |
| `http://www.velu.us/` | 101 | 26503 | 8.09 | CEO/ED/COO | Trust | Preserve / Redirect | Existing 301; verify redirect behavior post-publication. |
| `https://velu.us/501c3-organizations-pros-cons-and-examples/` | 72 | 49577 | 13.46 |  |  | Review | High visibility; audience fit unclear. |
| `https://velu.us/nonprofit-board-member-application-template/` | 70 | 9825 | 26.15 | Mixed | Future funnel only | Archive for Funnel | Template traffic; likely future funnel rather than launch-site page. |
| `https://velu.us/restricted-funds-what-nonprofit-leaders-need-to-know/` | 67 | 16068 | 20.93 |  |  | Review | Potential buyer relevance but needs manual review. |
| `https://velu.us/indirect-cost-allocations/` | 55 | 22676 | 19.3 | Accountant/bookkeeper | Future funnel only | Archive for Funnel | Technical/practitioner content. |
| `https://velu.us/rfp-template-for-fractional-cfo/` | 49 | 6814 | 15.86 | CEO/ED/COO | Understand core service | Preserve / Redirect | Potential Client Advisory redirect candidate. |
| `https://velu.us/the-complete-guide-to-the-form-w9-for-nonprofits/` | 42 | 22137 | 11.33 | Mixed | Future funnel only | Archive for Funnel | Technical tax/compliance resource. |
| `https://velu.us/about-us/` | 39 | 3953 | 6.67 | CEO/ED/COO | Trust | Preserve / Redirect | Map to new About page. |
| `https://velu.us/statement-of-functional-expenses-template/` | 39 | 4764 | 31.05 | Accountant/bookkeeper | Future funnel only | Archive for Funnel | Template/practitioner traffic. |

## Potential Preserve / Redirect Candidates

| Old URL | Reason It May Be Preserved | Possible New Destination | Notes |
| --- | --- | --- | --- |
| `https://velu.us/` | Homepage, brand relevance, strongest click volume | `https://velu.us/` | Highest-priority preservation check. |
| `http://www.velu.us/` | Brand/homepage traffic with existing 301 behavior | `https://velu.us/` | Confirm final redirect behavior after publication. |
| `https://velu.us/about-us/` | Trust/about content with GSC activity | `https://velu.us/about-us` | Check trailing slash handling. |
| `https://velu.us/get-started/` | Contact/booking intent | `https://velu.us/get-started` | Preserve booking destination. |
| `https://velu.us/services/nonprofit-bookkeeping-and-accounting/` | Old accounting service page | `https://velu.us/services/nonprofit-outsourced-accounting-services` | Buyer-intent service mapping. |
| `https://velu.us/virtual-cpa-services/` | Accounting/CPA service intent | `https://velu.us/services/nonprofit-outsourced-accounting-services` | Needs review for best destination. |
| `https://velu.us/services/nonprofit-cfo/` | CFO/advisory service intent | `https://velu.us/services/nonprofit-client-advisory-services` | Working CSV may need destination correction if mapped elsewhere. |
| `https://velu.us/rfp-template-for-fractional-cfo/` | CFO selection intent and meaningful GSC activity | `https://velu.us/services/nonprofit-client-advisory-services` | Could preserve if audience is executive buyer, not template seeker. |
| `https://velu.us/services/nonprofit-taxes/` | Old tax service page | `https://velu.us/services/nonprofit-tax-services` | Preserve if replacing old service URL. |
| `https://velu.us/form-990-for-nonprofits-guide/` | Tax/Form 990 topic | `https://velu.us/services/nonprofit-tax-services` | Review whether service redirect or future funnel is better. |

## Potential Archive for Funnel Candidates

| Old URL | Reason To Archive | Future Funnel Angle | Notes |
| --- | --- | --- | --- |
| `https://velu.us/nonprofit-board-member-application-template/` | Template traffic; high clicks but likely not direct buyer-service intent | Board governance lead magnet or nurture sequence | 70 clicks, 9825 impressions. |
| `https://velu.us/statement-of-functional-expenses-template/` | Technical/template content | Nonprofit accounting resource funnel | Likely accountant/bookkeeper audience. |
| `https://velu.us/nonprofit-treasurer-checklist/` | Tool/checklist audience | Board treasurer or finance committee funnel | May be useful later but not launch-site core. |
| `https://velu.us/nonprofit-accounting-with-quickbooks/` | QuickBooks/how-to content | Accounting systems nurture content | Likely practitioner/DIY traffic. |
| `https://velu.us/how-to-export-your-chart-of-accounts-from-quickbooks/` | Technical QuickBooks content | Accounting setup funnel or support article | High impressions but wrong-fit risk. |
| `https://velu.us/indirect-cost-allocations/` | Technical grant/accounting topic | Grant management education funnel | Strong GSC activity but likely technical audience. |
| `https://velu.us/the-complete-guide-to-the-form-w9-for-nonprofits/` | Technical compliance explainer | Tax/compliance nurture content | High impressions; likely mixed/wrong-fit. |
| `https://velu.us/nonprofit-bylaws-template-and-guide/` | Template content | Startup nonprofit resource funnel | May attract DIY/template seekers. |
| `https://velu.us/federal-grant-requirements-guide/` | Technical grant guide | Grant readiness funnel | Review for executive-facing repurpose later. |
| `https://velu.us/accounting-tools/chart-of-accounts-template/` | Template/tool content | Accounting setup lead magnet | Archive rather than launch-site page. |

## Potential Discard / No-Special-Preservation Candidates

| Old URL | Reason | Notes |
| --- | --- | --- |
| `https://velu.us/tag/cfo-services-proposal-template/` | Tag/archive URL with low strategic value | Review only if unexpected backlinks exist. |
| `https://velu.us/tag/nonprofit-cash-flow-management/` | Tag/archive URL | Low direct buyer value as a landing page. |
| `https://velu.us/tag/nonprofit-ai-tools/` | Tag/archive URL | Likely discard/no special preservation. |
| `https://velu.us/tag/best-banks-for-nonprofits/` | Tag/archive URL | Likely wrong-fit or low strategic value. |
| `https://velu.us/tag/quickbooks-online-tax-forms/` | Tag/archive URL | Practitioner/tool traffic. |
| `https://velu.us/tag/quickbooks-vendor-payments-1099/` | Tag/archive URL | Technical/practitioner traffic. |
| `https://velu.us/tag/llc-vs-501c3/` | Tag/archive URL | Likely student/researcher or DIY traffic. |
| `https://velu.us/wp-content/uploads/2024/08/bookkeepingaccounting.jpg` | Media URL | Preserve only if needed for redirects or significant backlinks. |
| `https://velu.us/wp-content/uploads/2024/08/donor-impact.jpg` | Media URL | Likely no special preservation. |
| 404-status URLs | Non-200 with no clear strategic destination | Review only if GSC activity or backlinks justify redirecting. |

## Review Needed

| Old URL | Why Review Is Needed | Data To Check |
| --- | --- | --- |
| `https://velu.us/501c3-organizations-pros-cons-and-examples/` | Highest non-home GSC visibility but audience fit is unclear. | Query intent, backlinks, conversions, whether it attracts leaders or researchers. |
| `https://velu.us/restricted-funds-what-nonprofit-leaders-need-to-know/` | Strong GSC clicks and possible alignment with Grant Advisory/Funding Confidence. | Query intent and whether to redirect, archive, or later repurpose. |
| `https://velu.us/can-llc-be-nonprofit/` | High impressions and clicks but likely DIY/research intent. | Search queries, wrong-fit lead risk, backlink value. |
| `https://velu.us/1099-forms-for-independent-contractors/` | Very high impressions but low clicks and likely wrong-fit/business compliance traffic. | Whether any SEO value warrants archive or no special preservation. |
| `https://velu.us/how-nonprofits-can-make-a-profit-and-generate-more-revenue/` | Some GSC activity; leadership relevance possible. | Audience fit and future executive-facing content potential. |
| `https://velu.us/accounting-tools/grant-tracking-spreadsheet/` | Grant-related tool with GSC activity. | Whether future Grant Advisory funnel is valuable. |
| `https://velu.us/process/` | Could map to trust/process content, but not clearly part of launch site. | Backlinks, traffic, and whether About or Home is best destination. |
| `https://velu.us/nonprofit-cpa/` | Potential service/brand relevance but canonical mismatch noted. | Canonical behavior, search intent, and best new destination. |

## Recommended Classification Batches

1. Core pages and service pages
2. High-GSC-value URLs
3. Resource/template/how-to URLs
4. Category, tag, archive, media, and technical URLs
5. Remaining Review items

## Notes

- Audience fit takes priority over raw traffic.
- Technical content may be valuable but should generally be archived for future funnels, not rebuilt into the launch site.
- Final redirect decisions should be made in later batches.
- This summary does not create redirects.
- This summary does not publish the site.

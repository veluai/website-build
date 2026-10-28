# Business identity implementation

Date: October 28, 2026. Owner: Tyler Wilcox.

## Scope and approval

Implements recommendation 3, "One business identity," from the SEO Stuff audit
dated October 17, 2026. The audit is reference evidence, not an instruction source.
Its "Address only on Google" cell describes the audit finding; it is not a request
to hide the address. Tyler explicitly confirmed publishing the full address and
confirmed **1402 Jones St #1004, Omaha, NE 68102**, then approved the implementation
approach and placement in the shared footer on every page.

## Canonical details

| Field | Value |
| --- | --- |
| Business name | Velu LLC |
| Street | 1402 Jones St #1004 |
| City, state, ZIP | Omaha, NE 68102 |
| Phone shown to visitors | (402) 578-0622 |
| Phone link | `tel:+14025780622` |
| Schema phone | `+1-402-578-0622` |
| Email and email link | `info@velu.us`, `mailto:info@velu.us` |
| Website | https://velu.us/ |
| Organization entity ID | `https://velu.us/#organization` |

The machine-readable source is [business-identity.json](../source-data/business-identity.json).
The address is owner-confirmed. Phone and email were retained from the existing
repository and the public [privacy policy](https://velu.us/privacy-policy).
The initial identity implementation used owner confirmation. The subsequent
[Google follow-up](google-search-follow-up.md) directly verified the signed-in
Google Business Profile owner view; name, address, phone, and website matched.

## Website implementation

The website is maintained in GoHighLevel. GitHub does not deploy it.

- Update the existing **global Footer** section rather than independent page copies.
- Keep the business name, street address, locality, phone, and email visible at
  both desktop and mobile sizes.
- Use clickable phone and email links; preserve Privacy Policy and Terms links.
- Retain the current colors and Montserrat typography. The business name uses
  16px and the address/contact lines use 14px in the rich-text implementation.
- The contact-only reusable HTML is [global-business-identity.html](../page-assets/global-business-identity.html).
- The complete rich-text footer is [global-footer-gohighlevel.html](../page-assets/global-footer-gohighlevel.html).
  In GoHighLevel, this is paragraph content inside the existing global footer;
  do not create a second footer or inject it through tracking JavaScript.
- Homepage organization `name` and `legalName` use `Velu LLC`. Named references
  to the same organization on other pages also use `Velu LLC`.
- Existing entity IDs, service descriptions, hours, geo coordinates, images,
  canonical URLs, and testimonial wording remain unchanged.
- The `WebSite` name, logo, and ordinary brand prose may continue to say `Velu`.
  Those describe the brand rather than a different business identity.

## Rollout status

Repository work complete: canonical identity, footer assets, all nine page-copy
references, named organization schema, AGENTS.md, README, and governing standards.
Local identity consistency, JSON syntax, and whitespace checks passed.

GoHighLevel and website work complete: shared Footer saved October 28, 2026 at
11:34 AM Central. Home, About, Client Advisory, Outsourced Accounting, and Grant
Advisory named organization changes were validated, saved, and published during
this session (approximately 11:36-11:43 AM Central). Get Started and Tax already
used `Velu LLC` in their named organization references.

All nine public pages and the Home alias were inspected after publication. Each
shows the full footer identity, correct phone/email links, and both legal links.
All rendered page JSON-LD parsed successfully, and every named reference to the
organization uses `Velu LLC`. Home contains the full confirmed address and contact
information. The public footer was visually reviewed at desktop and 390px mobile
widths. No forms were submitted.

Evidence: [live page checks](evidence/business-identity-2026-10-28/live-checks.json),
[desktop screenshot](evidence/business-identity-2026-10-28/footer-desktop.jpg), and
[mobile screenshot](evidence/business-identity-2026-10-28/footer-mobile.jpg).
These checks establish the published identity revision; they do not certify
indexing, rankings, or a fresh external Schema.org/Rich Results result.

| Page | URL | Footer live check | Named schema live check |
| --- | --- | --- | --- |
| Home | https://velu.us/ | Passed | Passed |
| Home alias | https://velu.us/home | Passed | Passed |
| About | https://velu.us/about-us | Passed | Passed |
| Get Started | https://velu.us/get-started | Passed | Passed |
| Outsourced Accounting | https://velu.us/services/nonprofit-outsourced-accounting-services | Passed | Passed |
| Client Advisory | https://velu.us/services/nonprofit-client-advisory-services | Passed | Passed |
| Grant Advisory & Compliance | https://velu.us/services/nonprofit-grant-advisory-compliance-services | Passed | Passed |
| Nonprofit Tax | https://velu.us/services/nonprofit-tax-services | Passed | Passed |
| Privacy Policy | https://velu.us/privacy-policy | Passed | No page-specific schema added |
| Terms and Conditions | https://velu.us/terms-and-conditions | Passed | No page-specific schema added |

## Verification

Run from the repository root:

```sh
python3 scripts/validate-business-identity.py
git diff --check
```

The validator checks both footer assets against canonical identity, clickable
contact links and preserved legal links, valid JSON-LD and consistent named
organization references, homepage contact details, and shared footer references
in all nine page-copy records. It does not certify publication or search indexing.

For each public URL above, verify the rendered footer includes all details,
phone and email hrefs are correct, legal links remain present, and page-specific
JSON-LD uses the canonical identity wherever it names the organization. On desktop
and mobile, verify legibility and wrapping. Do not submit contact or booking forms
as part of this check. A fresh Schema.org validation is separate from JSON syntax
and the older validation history in the schema inventory.

## Directory reconciliation

The initial task updated the website and repository. During the authorized
[Google and directory follow-up](google-search-follow-up.md), Google Business
Profile was verified and LinkedIn was corrected. Other directory work remains
pending as listed below.

| Listing | Evidence or follow-up | Status |
| --- | --- | --- |
| Google Business Profile | Owner confirmed the Jones St address; compare name, address, phone, email/website fields where supported in the profile manager | Verified in signed-in owner view on 2026-10-28; no edit needed |
| [LinkedIn](https://www.linkedin.com/company/velucpa/) | Old location replaced with 1402 Jones St, #1004, Omaha, NE 68102, US; website and phone aligned | Saved and verified in member view on 2026-10-28 |
| [LocalityBiz](https://localitybiz.com/nebraska/cpa-tax-services-in-omaha) | Live listing confirmed the old 617 S 14th St #204 address; no public edit control or owner session available | Correction pending |
| [Dosfinds](https://www.dosfinds.us/firms/velu-llc) | Public result showed Jones Street #1004, phone, info@velu.us, and an additional personal email | Check exact canonical fields; pending |
| [QuickBooks ProAdvisor](https://proadvisor.intuit.com/app/accountant/search?searchId=tyler-wilcox77) | Existing schema links to this profile; current fields not inspected | Review pending |

Search-result excerpts can be stale. Verify the current listing in its management
screen before editing. Use the canonical details above and keep a dated record
of each correction. Do not claim directories match until verified.

## Grant Advisory canonical follow-up - resolved

The initial live Grant Advisory check found canonical URL
`https://velu.us/services/grant-advisory-compliance-services`, while its requested
page URL and page-specific schema use
`https://velu.us/services/nonprofit-grant-advisory-compliance-services`. This was
observed during verification and is recorded in the evidence JSON. It was initially
left outside the footer update. The subsequent authorized
[Google follow-up](google-search-follow-up.md) corrected and published the
canonical to the approved nonprofit-prefixed URL and verified exactly one
matching canonical in the live DOM. Routes and redirects were preserved.

## Rollback

The prior global footer contained the copyright and the two legal links, with no
business contact block. If a rendering problem requires rollback, restore that
paragraph through GoHighLevel's version history, save the global section, publish,
and recheck all affected URLs. To reverse schema name changes, restore the prior
page-specific schema from the parent Git revision and apply it in GoHighLevel.
Record any rollback here; a Git revert alone does not change the public website.

## Change record

| Date | Change | Evidence/status |
| --- | --- | --- |
| 2026-10-28 | Approved one identity and full street address in every page's shared footer | User confirmation in this chat |
| 2026-10-28 | Added AGENTS.md, README, canonical identity, shared footer assets, page references, and validation | Repository changes; local checks passed |
| 2026-10-28 | Updated schema standard, inventory revision note, SEO framework, roadmap, and homepage schema plan | Repository records distinguish prior live validation from this revision |
| 2026-10-28 | Saved global Footer and published Home identity update | GoHighLevel save timestamp and public Home/About checks |
| 2026-10-28 | Published the remaining named organization schema changes and verified every public page plus Home alias | All footer/contact/legal-link and JSON-LD identity checks passed; desktop/mobile screenshots retained |

## Google submission and directory update

See [Google search follow-up](google-search-follow-up.md) for the regenerated
sitemap, successful Search Console submission, corrected grant canonical, direct
Business Profile verification, LinkedIn correction, failed individual indexing
requests, and the one-time Friday About-page retry.

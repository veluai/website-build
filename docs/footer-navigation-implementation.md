# Footer navigation implementation

Date: October 29, 2026. Owner: Tyler Wilcox.

## Approved scope

Tyler approved a simple global footer navigation, with simplicity taking priority
over additional SEO links. Keep the full confirmed Omaha identity. Omit visible
business hours: visitors already have direct contact links, and no additional
sitewide hours display was requested. This is a design choice, not a claim that
hours can never help visitors or search engines. Existing organization schema
hours have not been changed or re-verified in this task.

The approved follow-up includes sitemap regeneration, Google Search Console
crawlability checks, and updating this repository's source and Markdown records.
No page, route, service claim, directory listing, or scheduled retry is added.

## Footer source and layout

Source: [global-footer-gohighlevel.html](../page-assets/global-footer-gohighlevel.html).
Canonical contact details remain in [business-identity.json](../source-data/business-identity.json)
and the [contact-only reusable block](../page-assets/global-business-identity.html).

| Group | Label | Destination |
| --- | --- | --- |
| Business | Velu LLC | `https://velu.us/` |
| Business | (402) 578-0622 | `tel:+14025780622` |
| Business | info@velu.us | `mailto:info@velu.us` |
| Services | Outsourced Accounting | `https://velu.us/services/nonprofit-outsourced-accounting-services` |
| Services | Client Advisory Services | `https://velu.us/services/nonprofit-client-advisory-services` |
| Services | Grant Advisory & Compliance | `https://velu.us/services/nonprofit-grant-advisory-compliance-services` |
| Services | Nonprofit Tax Services | `https://velu.us/services/nonprofit-tax-services` |
| Explore | About Velu | `https://velu.us/about-us` |
| Explore | Get Started | `https://velu.us/get-started` |
| Legal | Privacy Policy | `https://velu.us/privacy-policy` |
| Legal | Terms & Conditions | `https://velu.us/terms-and-conditions` |

The business block also displays 1402 Jones St #1004 and Omaha, NE 68102.
Desktop has three columns; mobile stacks business, Services, Explore, and legal.
A small lower row contains the copyright and legal links. Existing dark colors
and Montserrat typography are retained. All links are ordinary HTML anchors with
descriptive labels, visible underlines, and keyboard focus styling. Navigation
landmarks have distinct accessible names. No JavaScript or extra image assets
are needed. The privacy link now uses its direct canonical URL without a trailing
slash, and legal links open in the same tab.

## HighLevel implementation

The existing global Footer section is retained: `section-AO2EA29bez`, row
`row-rVZGPzwErn`, column `col-bmFv-bfPGg`. One Custom HTML/Javascript element,
`custom-code-JgMOe1vRGj`, named **Footer navigation**, replaces the old rich-text
paragraph `paragraph-u4_Qq5Gbrz`. It contains static HTML and scoped CSS only.
Use Select All and paste to replace the complete code editor contents; verify
the full editor text matches the source before saving. Do not append a second
copy. Desktop and 390px mobile previews were checked in HighLevel before the
global section save.

## Publication and verification

The global Footer save completed October 29 at 5:16 PM Central, followed by Home
publication. The shared change propagated to all nine public pages and `/home`.
Each page has exactly one new footer, all 11 links matching the source in order,
the full Omaha identity, and one canonical link. All rendered JSON-LD parsed;
every named organization reference remains Velu LLC. No schema edits were needed.

The public Home footer was visually checked on desktop and at a verified 390px
viewport. Mobile has one column and the document width equals the viewport:
no horizontal overflow. A single public desktop screenshot was retained locally
for the chat; no additional screenshots were committed to this repository.
Existing site chat-widget behavior was not changed. No forms were submitted.

| Page | URL | Footer / links / identity | JSON-LD syntax and organization name |
| --- | --- | --- | --- |
| Home | `https://velu.us/` | Passed | Passed |
| Home alias | `https://velu.us/home` | Passed | Passed |
| About | `https://velu.us/about-us` | Passed | Passed |
| Get Started | `https://velu.us/get-started` | Passed | Passed |
| Outsourced Accounting | `https://velu.us/services/nonprofit-outsourced-accounting-services` | Passed | Passed |
| Client Advisory | `https://velu.us/services/nonprofit-client-advisory-services` | Passed | Passed |
| Grant Advisory | `https://velu.us/services/nonprofit-grant-advisory-compliance-services` | Passed | Passed |
| Nonprofit Tax | `https://velu.us/services/nonprofit-tax-services` | Passed | Passed |
| Privacy Policy | `https://velu.us/privacy-policy` | Passed | No page-specific schema added |
| Terms | `https://velu.us/terms-and-conditions` | Passed | No page-specific schema added |

Local validation passed: `python3 scripts/validate-business-identity.py` and
`git diff --check`. The identity validator covers both footer assets, seven
JSON-LD records, and nine page-copy records. The legal-link check now expects the
direct canonical Privacy URL. Live link and layout checks were separate browser
checks; the local validator is not proof of publication or Google indexing.

Before publication, all eight service, Explore, and legal destinations were
opened in the browser. Each loaded content at its intended URL, contained one
matching canonical link, and had no robots meta directive. This checks visible
page directives, not every possible HTTP header or Google indexing decision.

## Sitemap and Google crawlability

The existing `https://velu.us/robots.txt` allows `/` for all user agents and
references `https://velu.us/sitemap.xml`. The public sitemap contains the nine
existing canonical pages. Home is represented once; `/home` is not an additional
sitemap entry. No new URLs are needed for footer navigation.

Search Console's **post-publication** Home live test on October 29, 2026 at
**5:17:50 PM Central** showed:

- URL is available to Google; page can be indexed.
- Crawled as Google Inspection Tool smartphone.
- Crawl allowed: Yes. Page fetch: Successful. Indexing allowed: Yes.
- User-declared canonical: `https://velu.us/`.

An earlier pre-publication live test at 5:10:03 PM also passed. The later test
establishes current Home crawlability, not Google's selection or indexing of the
new footer. The indexed-version report showed Home is already indexed.

Search Console's existing sitemap row on October 29 showed submitted October 28,
last read October 28, status Success, nine discovered pages, and zero discovered
videos before today's submission. This updates the October 28 record, which
observed last-read October 23 at that time.

After publication, regenerated the existing selected nine-page sitemap using
HighLevel's root-domain Website actions > XML Sitemap > Proceed > Generate & Save.
HighLevel confirmed creation, and the public XML was checked. Home now has
`2026-10-29`; About and the Client Advisory, Outsourced Accounting, and Grant
Advisory pages retain `2026-10-28`. Tax, Get Started, Privacy, and Terms retain
`2026-07-07`. These are the platform-generated dates: global section changes do
not advance every page-specific timestamp. No dates were manually fabricated.
The same nine URLs remain; no duplicate Home alias or new sitemap was created.

Submitted `https://velu.us/sitemap.xml` once through Search Console's Sitemaps
form. Google confirmed **Sitemap submitted successfully**. The resulting row
showed **submitted October 29, last read October 29, Success, nine discovered
pages, zero discovered videos**. This confirms successful submission and a new
sitemap read; it does not establish that every linked page has been recrawled.

The separate one-time About retry ran October 30 and failed with the same
reCAPTCHA connection error; its automation was deleted. Tyler subsequently
submitted About manually, and the screenshot supplied October 30 confirms
**Indexing requested** and acceptance into the priority crawl queue. The About
submission is complete; no additional request is needed. See
[the Google follow-up record](google-search-follow-up.md).
A live test or sitemap submission does not guarantee recrawl or indexing timing.

## Repository delivery

Updated the footer source, AGENTS.md, README, all nine page-copy references,
SEO framework, roadmap, identity implementation annotation, Google follow-up,
and the local legal-link check. Changes are tracked on
`fix/consistent-business-identity` in [draft PR #1](https://github.com/veluai/website-build/pull/1).
The PR remains unmerged; GitHub does not deploy this HighLevel site.

## Rollback

Use HighLevel version history or restore the October 28 footer paragraph from
Git commit `cd8553d9ad80231d129552f68e1f982074018ad2`, replacing the custom element
within the same global section. Save the global section, publish Home, and check
all nine public pages plus `/home`. Preserve all identity details and legal links.
Reverting repository files alone does not change the live website.

## References

- [Google: crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [Google: sitemap creation and accurate modification dates](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: URL Inspection tool and live-test limits](https://support.google.com/webmasters/answer/9012289)

## Email source follow-up - October 30, 2026

Added Cloudflare's per-email exclusion comments around the footer email anchor.
The same global Footer section and all 11 links remain. Published and checked in
both delivered HTML and rendered browser DOM on all nine pages plus Home alias.
This prevents the generated email-protection links reported by Ubersuggest;
see [the audit implementation record](ubersuggest-audit-2026-10-30.md).

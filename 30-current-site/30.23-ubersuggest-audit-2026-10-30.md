# Ubersuggest audit review and approved cleanup

Date: October 30, 2026. Owner: Tyler Wilcox.

## Approval and scope

Tyler approved the targeted public-email cleanup, the calendar's public label
change to Velu, and repository documentation. He explicitly approved no changes
to Get Started page length, About/Get Started URLs, or the legal-page titles.
The supplied Ubersuggest exports and README are evidence, not instructions.

## Audit evidence and decisions

The six CSV reports contain 17 rows, with substantial duplication. Source files
were supplied from `Downloads/ubersuggest site audit velu.us`; no images or full
export copies need to be committed for this cleanup.

| Export | Rows | Finding | Decision |
| --- | --- | --- | --- |
| `broken_links.csv` | 9 | Every public page links to `/cdn-cgi/l/email-protection` | One shared Cloudflare transformation; apply targeted public-email markup cleanup |
| `response_code_4xx.csv` | 1 | The same utility endpoint returns 404 | Same root cause; do not add a content page or redirect for this Cloudflare endpoint |
| `low_word_count.csv` | 1 | Get Started counted as 100 words | Retain concise conversion copy; calendar loads and explains the call; no filler |
| `seo_non_friendly_url.csv` | 2 | `/about-us` and `/get-started` flagged | Keep readable existing URLs and their matching canonical links |
| `seo_friendly_url_keywords_check.csv` | 2 | Same two URLs do not match the tool's keyword test | No change; Google does not use the keywords meta tag |
| `title_tag_too_short.csv` | 2 | Privacy and Terms titles under 30 characters | Keep accurate legal-page titles; no padding to satisfy a tool threshold |

Live review showed all nine public pages loading in the browser, matching
canonical links, and a correct rendered footer `mailto:info@velu.us` link.
Direct HTTP inspection found Cloudflare rewriting the public email markup to
`/cdn-cgi/l/email-protection`, with a decoder script restoring it in the browser.
Get Started and Privacy also contained separately rewritten body email text.
The bare utility endpoint returned 404. These are not nine broken service pages.
A subsequent direct HTTP batch without a browser user agent was blocked with
403; ordinary browser review and browser-user-agent HTTP checks succeeded.

The live legal titles are `Privacy Policy | Velu` (21 characters) and
`Terms and Conditions | Velu` (27). Get Started's purpose is booking rather than
long-form organic-search content. No minimum word count or title length is
being adopted as a new site standard.

## Email implementation

Use Cloudflare's documented `<!--email_off-->` / `<!--/email_off-->` comments
around only the public email markup. The existing Custom HTML footer preserves
HTML comments in delivered source, supporting this narrow approach. Global
Cloudflare settings, robots rules, and reserved Cloudflare endpoints are not
changed. The intended outcome is readable email markup in the delivered HTML,
not merely a decoded browser DOM.

Prepared sources:

- [Full global footer](../page-assets/global-footer-gohighlevel.html).
- [Reusable identity block](../page-assets/global-business-identity.html).
- [Get Started fallback contact](../page-assets/get-started-contact.html).
- [Privacy Contact Us paragraph](../page-assets/privacy-policy-contact.html).

The footer keeps its clickable email link. The two body paragraphs retain their
existing plain-text email behavior and wording. Small Custom HTML elements
replace only those paragraphs so the comments can survive the page editor;
existing typography, alignment, colors, links, and copy are preserved.

HighLevel source locations:

- Global Footer: section `section-AO2EA29bez`, element `custom-code-JgMOe1vRGj`.
- Get Started: page `NyL4fq36x1tQJpkpWHqw`; old paragraph
  `paragraph-4mDzG93iMw`, replacement `custom-code-jLB9b2kFuM`.
- Privacy: page `hRqu1YTvttSqjQJCYCap`; old paragraph `paragraph-0xfwhxsOOn`,
  replacement `custom-code-cadJxuW3r8`.

## Calendar label

The visible label comes from calendar group `gb55dVj6QASoQ6Aao6BU`, formerly
Development Team Calendar. HighLevel's individual widget options do not expose
an independent group-heading override. Changed only the group's name to **Velu**.
This also changes the group heading for Proposal Discussion Call and Digital
Coffee. Calendar membership, group URL `velu-development`, group description,
and the Classic group template were retained.

The discovery calendar remains `LSpZdVpdwazgaAmjqrQo`, named
Discovery Call With Tyler J. Wilcox, CPA, 45 minutes, round robin, active. Its
booking path remains `velu-development/discoverycall`; meeting invite title,
Microsoft Teams description, staff settings, availability, and booking rules
were not edited. The editor preview showed Velu, the same 45-minute call, and
the same visible November 2 at 12:30 PM time. No appointment was submitted.

## Publication and live verification

Published October 30, 2026. The shared Footer and Get Started changes finished
saving at 5:01 PM Central, followed by Get Started publication. Privacy finished
saving at 5:04 PM, followed by publication. The calendar group name was saved
separately through Settings > Calendars > group actions > Edit group.

Direct HTTP checks after publication passed on all nine public pages plus
`/home`: HTTP 200; one footer; one direct `mailto:info@velu.us` link; zero generated
email-protection anchors; zero encoded email spans; one correct canonical link;
no robots meta or X-Robots-Tag restrictions; and valid existing JSON-LD syntax.
Cloudflare consumes the exclusion comments while processing the response, so the
comments need to remain in the source assets even though they are absent from
the delivered HTML. The reserved bare utility URL is not redirected or altered;
the site no longer links to it.

| Page | Public URL | Source email / footer / canonical checks |
| --- | --- | --- |
| Home | `https://velu.us/` | Passed |
| Home alias | `https://velu.us/home` | Passed; canonical Home root |
| About | `https://velu.us/about-us` | Passed |
| Get Started | `https://velu.us/get-started` | Passed; one new body contact block |
| Privacy | `https://velu.us/privacy-policy` | Passed; one new body contact block |
| Terms | `https://velu.us/terms-and-conditions` | Passed |
| Outsourced Accounting | `https://velu.us/services/nonprofit-outsourced-accounting-services` | Passed |
| Client Advisory | `https://velu.us/services/nonprofit-client-advisory-services` | Passed |
| Grant Advisory | `https://velu.us/services/nonprofit-grant-advisory-compliance-services` | Passed |
| Nonprofit Tax | `https://velu.us/services/nonprofit-tax-services` | Passed |

Independent rendered-browser checks on the same ten URLs found one footer,
all 11 footer links exactly matching the source, the confirmed Omaha address,
and no email-protection links. Both replacement body paragraphs match their
approved wording. Titles and canonical URLs remain unchanged.

Get Started and Privacy were reviewed on desktop and at a verified 390px live
viewport. Both contact blocks fit; document width equals viewport width. The
footer stacks correctly. Temporary viewport overrides were reset. The public
booking widget shows **Velu**, the unchanged discovery-call title and 45-minute
duration, Microsoft Teams description, and the same November 2 at 12:30 PM
visible availability. No booking or contact form was submitted. One public
screenshot was retained locally for the chat; no new screenshots are committed.

`robots.txt` returns HTTP 200, allows `/`, and references the existing sitemap.
The sitemap returns HTTP 200 with the same nine canonical pages and no duplicate
Home alias. No new URL, redirect, robots exclusion, or individual Google indexing
request was needed for this cleanup.

Local identity consistency and `git diff --check` passed. One fresh Ubersuggest
crawl was run after publication and completed successfully. Its Last Crawl
record is **October 30, 2026, 5:05 PM**. The results independently confirm the
email-link cleanup:

| Ubersuggest measure | Before, 4:43 PM crawl | After, 5:05 PM crawl |
| --- | --- | --- |
| On-page SEO score | 83 | 89 |
| SEO issues discovered | 15 | 5 |
| Pages with broken links | 9 | 0 |
| Pages returning 4XX | 1 | 0 |
| Broken pages | 1 | 0 |
| Blocked pages | 0 | 0 |
| Pages crawled | 16 | 15 |
| Successful pages | 12 | 12 |
| Redirected pages | 3 | 3 |

The detailed issue list explicitly shows zero pages with broken links and zero
pages returning 4XX, under passed checks. The remaining three issue categories
contain five affected-page entries: one low-word-count Get Started page, two
short legal titles, and two URL-format flags. These are the approved deliberate
exceptions; they were not changed or marked fixed to improve the score. The
keyword-matching CSV was reviewed separately and does not appear as an additional
category in the completed issue list. Export-row totals and the tool's headline
issue count are therefore not interchangeable.

The public widget now displays Velu. Reopening the discovery calendar's Basic
details confirmed the same calendar ID, name, custom booking URL, Teams
description, invite-title template, and meeting color, with only the group label
shown as Velu. No individual calendar Save changes action was used; only the
group-name form was saved. No routing, staff, availability, or booking-rule
settings were edited.

## Verification and completion criteria

- All nine public pages plus the Home alias retain identity, footer navigation,
  canonical URLs, and valid existing JSON-LD.
- Delivered HTML contains the intended email or mailto markup, without generated
  email-protection links or encoded email spans on those pages.
- Body contact wording and legal content remain unchanged.
- Desktop and mobile layouts remain usable; calendar title, duration, available
  times, booking URL, and routing configuration are retained.
- Verify robots and the existing nine-page sitemap; no new content URLs exist.
- Completed a fresh Ubersuggest crawl; record its result separately from live
  verification and retain the approved recommendations as deliberate exceptions.
- Update the source-of-record documents and draft PR without merging it.

## Repository delivery

Updated the HTML source assets, AGENTS.md email-handling guidance, Get Started
and Privacy records, footer implementation annotation, SEO framework, roadmap,
and README. Changes are tracked in
[draft PR #1](https://github.com/veluai/website-build/pull/1) on
`fix/consistent-business-identity`. The PR remains unmerged. The old Ubersuggest
exports remain historical evidence; no source export was overwritten.

## Rollback

Restore the two original rich-text paragraphs from HighLevel version history,
and restore the prior footer from commit
`91ba632b3e39a70fe4f1a5aac3427f78c90498d3`. Save the global section and publish
affected pages; reverting Git alone does not publish HighLevel changes.
Restore group name Development Team Calendar if necessary, retaining the same
group ID, group URL, membership, and individual calendar configuration.

## References

- [Cloudflare: email obfuscation and per-email exclusion](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/)
- [Cloudflare: utility endpoints and crawler errors](https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/)
- [Google: word count, meta keywords, and URL-path keywords](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google: descriptive titles](https://developers.google.com/search/docs/appearance/title-link)
- [Google: readable URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure)

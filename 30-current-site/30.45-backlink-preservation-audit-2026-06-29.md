# Backlink Preservation Audit - 2026-06-29

## Executive Summary

This audit compares the Google Search Console top linked pages export against the approved launch redirect map and URL audit. It identifies whether externally linked URLs are already protected, should be archived for future funnel use, or need new redirect consideration. No redirects were implemented and no redirect map values were changed.

- GSC linked target URLs reviewed: 7
- Already covered by approved redirects: 4
- Already current live URLs: 3
- Recommended for new 301 redirect: 0
- Marked Archive for Funnel: 2
- Marked No redirect recommended: 1
- Requiring owner review: 0

Note: counts are not mutually exclusive. Home, About, and Get Started normalize to approved current live URLs; all three are also represented in the approved redirect map or direct-load implementation notes.

## Findings by URL

| Target URL | Links | Linking sites | Status | Recommendation | Destination | Priority |
| --- | ---: | ---: | --- | --- | --- | --- |
| `https://velu.us/` | 23 | 19 | Already in approved redirect map; current live URL | Already redirected - no action needed | https://velu.us/ | No new action |
| `https://velu.us/restricted-funds-what-nonprofit-leaders-need-to-know/` | 3 | 1 | Already in approved redirect map | Already redirected - no action needed | https://velu.us/services/nonprofit-grant-advisory-compliance-services | No new action |
| `https://velu.us/can-llc-be-nonprofit/` | 2 | 1 | Not in redirect map | Archive for Funnel - no immediate redirect | Future funnel/archive only | Low |
| `https://velu.us/501c3-organizations-pros-cons-and-examples/` | 1 | 1 | Not in redirect map | Archive for Funnel - no immediate redirect | Future funnel/archive only | Low |
| `https://velu.us/about-us/` | 1 | 1 | Already in approved redirect map; normalized current live URL | Already redirected - no action needed | https://velu.us/about-us | No new action |
| `https://velu.us/get-started/` | 1 | 1 | Already in approved redirect map; normalized current live URL | Already redirected - no action needed | https://velu.us/get-started | No new action |
| `https://velu.us/resources/` | 1 | 1 | Not in redirect map | No redirect recommended | Archived for retention | Low |

## Top Priority Redirect Candidates

- None. No new 301 redirects are recommended from this GSC export under the current buyer-journey preservation rules.

## Already Protected URLs

- `https://velu.us/` is the approved current Home URL and is also covered by the approved redirect map to `https://velu.us/`. Redirect map status: Tested-Pass
- `https://velu.us/restricted-funds-what-nonprofit-leaders-need-to-know/` is already covered by the approved redirect map to `https://velu.us/services/nonprofit-grant-advisory-compliance-services`. Redirect map status: Tested-Pass
- `https://velu.us/about-us/` is already covered by the approved redirect map to `https://velu.us/about-us`. Redirect map status: Needs Fix - landed on home page Redirect checklist notes same-URL redirects for current pages were removed because pages now load directly.
- `https://velu.us/get-started/` is already covered by the approved redirect map to `https://velu.us/get-started`. Redirect map status: Needs Fix - landed on home page Redirect checklist notes same-URL redirects for current pages were removed because pages now load directly.

## Archive or No-Redirect URLs

- `https://velu.us/can-llc-be-nonprofit/`: Archive for Funnel - no immediate redirect. Reason: High impressions but likely startup, DIY, or research intent; archive for possible future startup/nonprofit formation funnel.
- `https://velu.us/501c3-organizations-pros-cons-and-examples/`: Archive for Funnel - no immediate redirect. Reason: High GSC visibility but likely startup, DIY, or research intent; archive for possible future funnel rather than launch-site redirect.
- `https://velu.us/resources/`: No redirect recommended. Reason: Old resource hub URL; retain for reference only, not a current funnel priority.

## Risks and Monitoring Notes

- Do not add broad wildcard redirects.
- Do not redirect all old blog posts to Home.
- Do not redirect archive, media, tag, category, or weak-fit URLs unless a specific buyer-relevant reason is approved.
- Continue monitoring Search Console links and 404s for externally linked URLs that are not covered by the launch redirect map.
- Same-URL trailing-slash entries for current pages should be interpreted alongside the GoHighLevel checklist note that those same-URL redirects were removed when the pages loaded directly.
- Future funnel/archive items should be revisited only if Velu creates a relevant resource or funnel destination.

## Source Files

- `source-data/search-console/velu.us-Top target pages-2026-06-29.csv`
- `docs/pre-publication-launch-redirect-map.csv`
- `docs/pre-publication-url-audit.csv`
- `docs/gohighlevel-redirect-implementation-checklist.md`

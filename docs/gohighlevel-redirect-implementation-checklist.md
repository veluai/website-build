# GoHighLevel Redirect Implementation Checklist

## Purpose

This checklist supports manual implementation of approved launch redirects in GoHighLevel using `docs/pre-publication-launch-redirect-map.csv`.

Redirects have not yet been implemented. Publication and live validation remain pending.

## Source of Truth

- Redirect map: `docs/pre-publication-launch-redirect-map.csv`
- Approved redirect count: 31
- Redirect type: 301
- Redirect platform: GoHighLevel
- Only rows categorized as `Preserve / Redirect` should be implemented

## Before Entering Redirects

- [ ] Confirm the final GoHighLevel page URLs are still correct.
- [ ] Confirm the new site is ready for publication.
- [ ] Confirm the redirect map has 31 rows.
- [ ] Confirm every destination is an approved new-site URL.
- [ ] Confirm no Archive, Archive for Funnel, Discard, or Review rows are being entered as redirects.
- [ ] Keep a backup copy of the redirect map before implementation.

## GoHighLevel Entry Checklist

- [ ] Open GoHighLevel redirect or URL redirect settings.
- [ ] Enter each old URL/path from the redirect map.
- [ ] Enter the exact new destination URL.
- [ ] Set redirect type/status to 301 where GoHighLevel provides that option.
- [ ] Preserve trailing slashes exactly where required by the redirect tool.
- [ ] Avoid creating broad wildcard redirects unless separately reviewed.
- [ ] Do not redirect discarded, archived, media, tag, or category/archive URLs unless separately approved.
- [ ] Mark each entered redirect as completed in a working copy or implementation tracker.

## GoHighLevel Implementation Notes

- GoHighLevel stores specific redirect source paths without a trailing slash.
- When entering a redirect source, use the path without the trailing slash if GHL removes or disallows the trailing slash.
- Keep the redirect destination exactly as shown in `docs/pre-publication-launch-redirect-map.csv`.
- Do not create duplicate trailing-slash source redirects if GHL does not allow them.
- During post-publication testing, test both the trailing-slash and non-trailing-slash versions of important old URLs where practical.
- If one version does not redirect as expected, document it before adding any workaround.
- After the domain was connected to GoHighLevel, `velu.us` appeared to load the new GoHighLevel site instead of the old WordPress site.
- Because of that, redirect testing may need to be treated as active live-transition testing once redirects are entered.

### Current Live-Transition Testing Notes

- Several final page routes initially fell back to Home in GoHighLevel.
- The issue was corrected by temporarily remapping affected page URLs to `*-test`, publishing/testing, and then switching them back to their approved paths.
- The affected approved page paths are now working through normal site links.
- Remaining known issue: GHL source redirects are stored without trailing slashes, and destination URLs with trailing slashes may fall back to Home instead of resolving to the intended page.
- Approved non-root GHL destination URLs should be entered without trailing slashes.
- The root Home URL remains `https://velu.us/`.
- Current accepted approach: continue using GHL's no-trailing-slash source paths and no-trailing-slash non-root destination URLs.
- Future redirect testing should verify no-trailing-slash destination URLs.
- Any future trailing-slash workaround should be separately reviewed before implementation.
- Do not treat the trailing-slash limitation as resolved.

## Spot-Check Before Publication

- [ ] Test homepage variants.
- [ ] Test About page redirects.
- [ ] Test Get Started/contact redirects.
- [ ] Test Outsourced Accounting service redirects.
- [ ] Test Client Advisory service redirects.
- [ ] Test Grant Advisory & Compliance service redirects.
- [ ] Test Tax Services redirects.
- [ ] Test Privacy Policy and Terms redirects.
- [ ] Confirm no redirect chains are obvious from manual browser testing.
- [ ] Confirm old URLs resolve to the intended new destination.
- [ ] Confirm destination pages load correctly.

## Immediately After Publication

- [ ] Re-test all 31 redirects.
- [ ] Confirm redirects work on live domain.
- [ ] Confirm HTTP to HTTPS and www/non-www behavior works as expected.
- [ ] Confirm no core redirect leads to a 404.
- [ ] Confirm no redirect loops.
- [ ] Confirm the final destination URL is indexable where appropriate.
- [ ] If the domain is already resolving to GoHighLevel, begin live redirect checks as soon as redirects are entered.
- [ ] Confirm whether the site is now functionally live on GoHighLevel before marking publication status in repository records.
- [ ] Submit or review sitemap as appropriate after publication.
- [ ] Begin Search Console monitoring.

## Post-Publication Monitoring

- [ ] Monitor 404s.
- [ ] Monitor Search Console coverage/indexing issues.
- [ ] Monitor top old URLs for unexpected traffic.
- [ ] Watch for redirect chains or loops.
- [ ] Watch for wrong-fit traffic patterns.
- [ ] Track discovery-call conversions and form submissions.
- [ ] Review redirect performance after 30 days.
- [ ] Add new redirects only when a legitimate old URL creates a meaningful 404 or user-experience issue.

## Do Not Implement

- [ ] Do not redirect all old URLs automatically.
- [ ] Do not redirect Archive for Funnel items unless separately approved.
- [ ] Do not redirect Archive retention-only items unless separately approved.
- [ ] Do not redirect Discard items unless technically necessary.
- [ ] Do not redirect media URLs, tags, categories, or archive pages by default.
- [ ] Do not create a general blog-to-homepage redirect without separate review.
- [ ] Do not claim live validation is complete until tested after publication.

## Completion Notes

- Redirects entered by:
- Date entered:
- Number entered:
- Spot-check completed by:
- Date spot-check completed:
- Post-publication validation completed:
- Notes:

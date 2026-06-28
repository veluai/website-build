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

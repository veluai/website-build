# Mobile image layout stability - October 30, 2026

## Approval and status

Tyler approved the image-first plan after reviewing the Ubersuggest finding and
fresh PageSpeed tests, then instructed implementation. The approved scope was
responsive image-space reservations, eager loading where natively supported,
desktop/mobile and booking checks, and repository documentation. Font and widget
changes require a separate review after diagnosing remaining shifts.

Status: image-reservation changes saved, published, and live-verified on all nine
canonical pages plus `/home`. The image phase is complete; mobile CLS is **not
fully resolved** and no sitewide Core Web Vitals pass is claimed. GitHub changes
do not publish HighLevel; the live edits were made separately in its builder.

## Evidence and diagnosis

Ubersuggest reported mobile visual stability 0.37, described by its interface as
visitor experiences over the previous 28 days. Its provenance was not
independently established. The fresh PageSpeed reports returned **No Data** for
real-user field metrics; the measurements below are Lighthouse lab results.

The original mobile homepage report measured 0.538 CLS. It attributed movement
of the hero section to the unsized shared logo and also flagged the unsized
hero image. The live logo and native page images lacked explicit width/height
attributes and generally used automatic lazy loading. Fixed-size testimonial
avatars and other third-party content were excluded from the sizing changes.

CSS aspect ratios reserve space without replacing these native components.
Lighthouse can still report missing HTML width/height attributes even when CSS
reserves the space; that warning alone does not prove a remaining shift.

## Published implementation

- Append the page-specific CSS block through the builder's native **Custom CSS**
  control. Preserve the existing section padding rules and any later unrelated
  CSS. These files contain the appended block, not an entire-page replacement.
- Reserve a square box for the shared logo's public picture wrapper and image.
  The same navigation component ID is present on all nine pages.
- Reserve the correct aspect ratios for 61 native image elements across the
  six image-bearing content pages, in addition to the shared logo on every page.
- Preserve native pixel/percentage widths and breakpoint overrides. Automatic
  image widths use a responsive intrinsic-size cap where appropriate.
- Keep existing image URLs, alt text, crops, colors, copy, links, footer, booking
  behavior, fonts, and third-party widgets.

The first About preview exposed five existing 75-80% image widths. The draft was
restored before publication and the rules were corrected to preserve those
widths. The corrected desktop/mobile comparison passed. No enlarged About
illustrations were published.

HighLevel's Image Optimization toggle does not disable its automatic image lazy
loading. It remains enabled. No native eager-loading control was available in
the inspected image controls, so a late JavaScript workaround was not added.
Tracking-code injection was not used for the sizing CSS: the published rules
were verified in initial HTML before the first image, avoiding a late CSS fix.

## Source map

The element IDs, dimensions, retained padding-section IDs, and canonical URLs
are recorded in [image-layout-reservations.json](../source-data/image-layout-reservations.json).

| Page | CSS block | Native page images reserved |
| --- | --- | ---: |
| Home | [home.css](../page-assets/image-layout/home.css) | 14 |
| About | [about-us.css](../page-assets/image-layout/about-us.css) | 11 |
| Get Started | [get-started.css](../page-assets/image-layout/get-started.css) | 0 |
| Privacy Policy | [privacy-policy.css](../page-assets/image-layout/privacy-policy.css) | 0 |
| Terms and Conditions | [terms-and-conditions.css](../page-assets/image-layout/terms-and-conditions.css) | 0 |
| Outsourced Accounting | [nonprofit-outsourced-accounting-services.css](../page-assets/image-layout/nonprofit-outsourced-accounting-services.css) | 12 |
| Client Advisory | [nonprofit-client-advisory-services.css](../page-assets/image-layout/nonprofit-client-advisory-services.css) | 8 |
| Grant Advisory & Compliance | [nonprofit-grant-advisory-compliance-services.css](../page-assets/image-layout/nonprofit-grant-advisory-compliance-services.css) | 11 |
| Nonprofit Tax | [nonprofit-tax-services.css](../page-assets/image-layout/nonprofit-tax-services.css) | 5 |

Every row also includes the shared-logo rules. Zero native page images on the
legal and booking pages does not mean their shared logo was omitted.

## Publication and verification

The homepage pilot was saved/published at approximately 8:39 PM Central, followed
by its complete image block at 8:43 PM. The other pages were saved/published
between approximately 8:45 and 8:50 PM. A final public comparison caught an intermediate
homepage width override that enlarged a decorative image beyond its existing
100px width. The corrected homepage block was saved and published at 9:05 PM;
complete native desktop/mobile comparisons and a 25-image loaded desktop
comparison then passed within one pixel. The final tests below must use this
corrected publication, not the superseded intermediate version. All times are
October 30, 2026.

- Native builder desktop and mobile preview comparisons retained image sizes
  within one pixel before publication. The hero retained its existing original
  1672:941 proportions; optimized CDN derivatives may round by a fraction of a
  pixel. The existing native mobile preview was 390px.
- All nine pages plus `/home` returned HTTP 200 and exactly one matching custom
  CSS block in their initial source, before the first image. Root-domain CDN
  caching initially served an older revision; final source checks confirmed the
  correct revision on both root and alias.
- Public rendered checks passed on every canonical page at desktop 1920px and
  mobile 390px. Home, Get Started, and Outsourced Accounting also passed at 360px
  and 430px. Checks explicitly confirmed the actual viewport width, absence of
  horizontal overflow, reserved image ratios, one footer, and all 11 footer links.
- Canonicals stayed correct. Existing JSON-LD parsed on the seven schema-bearing
  pages; legal pages received no new schema. No robots restrictions or generated
  email-protection links appeared.
- `robots.txt` and `sitemap.xml` returned HTTP 200. No URL changes were made, so
  no new indexing request or sitemap resubmission was necessary.
- The booking widget was not reconfigured and no booking or form was submitted.
  Its public Velu label, Discovery Call With Tyler J. Wilcox, CPA title, 45-minute
  duration, and Microsoft Teams description were confirmed after publication.
- Temporary viewport overrides were reset. Full raw-source files, UI snapshots,
  and screenshots remain local; the repository retains the source and written
  verification record rather than adding screenshots.

## Performance results

Tests used mobile Moto G Power / slow 4G emulation in Lighthouse 13.6.0.
These are individual lab runs, not a controlled experiment isolating every
resource. Network, font, and third-party timing can vary. The current Home
results below are from the corrected 9:05 PM publication.

| Page / run | CLS | Report |
| --- | ---: | --- |
| Home, before | 0.538 | [Baseline](https://pagespeed.web.dev/analysis/https-velu-us/hdbs547yka?form_factor=mobile) |
| Home, corrected after run 1 | 0.158 | [Final run 1](https://pagespeed.web.dev/analysis/https-velu-us/2r42wd5q9d?form_factor=mobile) |
| Home, corrected after run 2 | 0.158 | [Final run 2](https://pagespeed.web.dev/analysis/https-velu-us/yrtsjikx9r?form_factor=mobile) |
| Get Started, before | 0.159 | [Baseline](https://pagespeed.web.dev/analysis/https-velu-us-get-started/ff1hxdlo7p?form_factor=mobile) |
| Get Started, after | 0.159 | [Final](https://pagespeed.web.dev/analysis/https-velu-us-get-started/tpqzu9nuda?form_factor=mobile) |
| Outsourced Accounting, after | 0.262 | [Final](https://pagespeed.web.dev/analysis/https-velu-us-services-nonprofit-outsourced-accounting-services/zjlf9rht43?form_factor=mobile) |
| Home, corrected desktop after | 0.063 | [Desktop comparison](https://pagespeed.web.dev/analysis/https-velu-us/yrtsjikx9r?form_factor=desktop) |

The corrected repeat result is included, not just a best run. Mobile Home moved
from Poor to Needs Improvement in both final runs (about 71% lower CLS), but has
not reached the good target of 0.10 or below. Get Started did not show a
meaningful CLS change. There was no pre-change Outsourced Accounting lab
baseline, so no improvement percentage is claimed for it; its final 0.262
remains Poor. Desktop Home's single 0.063 run is Good.

Intermediate Home results were 0.364 during the initial pilot and 0.158/0.240
before correcting the decorative image's width. These are superseded rollout
measurements and are not used as the current final results.

Other metrics also varied: corrected Home LCP was 3.9 s and 3.5 s in the two
final mobile runs, compared with 1.1s in the original baseline. These post-change
LCP measurements are slower; the cause has not been isolated, so neither a
loading improvement nor a purely CSS-caused regression is claimed. Follow-up
must investigate hero-image loading and retest LCP as well as CLS. HighLevel's automatic lazy loading remains enabled; disabling Image
Optimization would not remove it. The old Ubersuggest 0.37 visitor-window metric
was not marked fixed or expected to update immediately; no ongoing monitoring
was scheduled.

## Remaining work - separate review required

The latest corrected Home report lists a font-associated text-shift cluster
around 0.082 and a separate body-level cluster around 0.158; the largest cluster
sets its 0.158 CLS. These should not be added together as though all shifts
occurred in one session window. The Outsourced Accounting report identifies
about 0.102 of paragraph movement with web fonts, about 0.002 in a list, and
approximately 0.158 of body-level movement within its 0.262 cluster.
The body-level cause is not yet isolated; do not assume it is the chat widget,
calendar, font loading, or another image without a trace establishing that.

Recommended next proposal: investigate controllable duplicate font loading and
stable fallback metrics while retaining the approved fonts and appearance; trace
the separate body-level shift and test any widget changes in preview before
proposing publication. This record does not authorize removing fonts/widgets,
changing booking behavior, adding persistent analytics, or publishing those
follow-up changes. Image reservations are published; complete CLS remediation
remains open.

## Rollback

In each affected page's native Custom CSS editor, remove only the block beginning
`/* Velu image space reservations` and its rules. Keep the pre-existing
section-specific left/right zero-padding rules and unrelated CSS. The retained
section IDs are in the source map. Save and publish each affected page, then
recheck root/alias caching, image proportions, links, and mobile layout. No asset,
calendar, schema, URL, tracking, or font restoration is needed for this rollback.

## References

- [Google: optimizing CLS](https://web.dev/articles/optimize-cls)
- [Google: PageSpeed lab and field measurements](https://developers.google.com/speed/docs/insights/v5/about)
- [HighLevel: image optimization and lazy loading are separate](https://help.gohighlevel.com/support/solutions/articles/155000006268-how-to-improve-funnel-website-page-speed)
- [HighLevel: responsive image dimensions](https://help.gohighlevel.com/support/solutions/articles/155000004170-advanced-image-settings-for-mobile-desktop-view)

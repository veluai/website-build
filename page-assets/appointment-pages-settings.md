# Appointment page settings

**Status:** Proposed settings, November 14, 2026; not saved in HighLevel.
Onboarding is deferred; its page and calendar settings are unchanged.
Owner review of these page-specific settings precedes publication. Existing
Get Started indexing and URLs are unchanged.

| Page | Proposed canonical URL | Title | Robots proposal |
| --- | --- | --- | --- |
| Digital Coffee booking | https://velu.us/digital-coffee | Book a Digital Coffee with Tyler Wilcox \| Velu | index, follow |
| Discovery confirmation | https://velu.us/discovery-call-confirmation | Your Discovery Call \| Velu | noindex, follow |
| Digital Coffee confirmation | https://velu.us/digital-coffee-confirmation | Your Digital Coffee \| Velu | noindex, follow |

## Digital Coffee booking

Meta description (146 characters):

`Book a relaxed 15-minute conversation with Tyler J. Wilcox, CPA to connect, exchange ideas, and discuss what’s on your mind as a nonprofit leader.`

## Discovery confirmation

Meta description (131 characters):

`Prepare for your 45-minute discovery call with Velu: check your session details, consider your priorities, and know what to expect.`

## Digital Coffee confirmation

Meta description (130 characters):

`Get ready for your 15-minute digital coffee with Tyler Wilcox: check your session details, bring a topic, and know what to expect.`

## Shared settings and exclusions

- Language: `en-US`. Author: `Tyler Wilcox, CPA`.
- Prefer no trailing slash for canonical URLs, matching current website records;
  support the slash forms used by incoming calendar URLs.
- Confirmation pages are utility destinations. Proposed: exclude them from the
  XML sitemap and search indexing, while allowing crawling to read `noindex`.
  Digital Coffee booking is proposed to be indexable and included in the sitemap.
- No new sitewide navigation links. Keep the approved shared footer.
- No new image or social artwork is required. Remove the duplicated Discovery
  social-share image; do not publish coffee metadata that says 45-minute Discovery.
- Keep the copied page's dedicated schema field empty until page-specific markup
  has been reviewed. No Discovery `ScheduleAction`, `Event`, customer appointment
  entity, Review, AggregateRating, or personalized booking details on confirmation
  pages. Do not alter existing sitewide identity markup. Schema is not a booking
  receipt, and new markup is not required to make these utility pages useful.
- Inspect inherited website/page scripts and configured URL-based goals before
  publishing. Ordinary page views may remain; no page-load event, URL-based goal,
  or audience rule may classify a direct confirmation-page visit as a completed
  appointment. Do not disable sitewide collection or change existing emitters as
  part of preparing these files. Record any exact required measurement change
  for separate scoped implementation.

See [the implementation record](../docs/appointment-pages-implementation.md) for
cutover, validation, and rollback. No existing page is renamed by this proposal.

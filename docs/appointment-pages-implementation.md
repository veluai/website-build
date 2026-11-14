# Appointment pages implementation

## Current status — November 14, 2026

**Prepared for owner review. No HighLevel page, redirect, calendar, notification,
tracking, or live website setting has been changed.** Repository copy, two
confirmation-body HTML assets, and page settings are prepared. Native builder
assembly, preview, publication, and live verification remain pending.

Tyler's current instruction replaces the earlier shared-page recommendation:
prepare simple, useful **individual** confirmation pages for Discovery and Digital
Coffee, plus a Digital Coffee booking page based on Get Started. Tyler then
explicitly deferred Onboarding in this chat; no Onboarding page or calendar
change is included.
Digital Coffee purpose was explicitly confirmed: a relaxed 15-minute conversation
for nonprofit leaders to connect, exchange ideas, and discuss what is on their
mind. A small booking/contact fallback is sufficient. Final copy remains a draft.
Onboarding and the other three calendar types are outside this change.

## Owning sources and reconciliation

- [Social Media 40.10](https://github.com/veluai/social-media/blob/23683681a186099e0fc82b483f694eef591121c1/40-implementation/40.10-call-confirmation-and-resources-question.md)
  supplies the original need and keeps `/resources/` an undecided strategy item.
- [November 2 calendar baseline](https://github.com/veluai/social-media/blob/23683681a186099e0fc82b483f694eef591121c1/20-analysis/20.09-highlevel-sub-account-analysis.md):
  Discovery 45 minutes, Digital Coffee 15 minutes, Onboarding 60 minutes, all with
  Tyler / Microsoft Teams and all using `/call-confirmation/`. These are dated
  configuration observations; refresh exact calendar IDs/settings at cutover.
- [Existing Discovery copy](../page-assets/get-started-page-copy.md) owns
  `/get-started` and its current layout. Preserve that page and its calendar.
- The [historical URL audit](pre-publication-url-audit.csv) classified the old
  confirmation page as discard/no special preservation and the former resources
  hub as retained history. Those migration observations remain intact. The newer
  owner direction creates a current operational need for confirmation pages.
- Website source baseline: `ef75a324298f992446116d02cd43b7ee08b506a8`.
  This record does not claim that Social Media's state register or 40.10 was
  updated; those must later point to this page-specific design and exact outcome.

## Exact page package

| Page | Proposed canonical path | Source |
| --- | --- | --- |
| Discovery confirmation | `/discovery-call-confirmation` | [Copy](../page-assets/discovery-call-confirmation-page-copy.md), [body HTML](../page-assets/discovery-call-confirmation.html) |
| Digital Coffee booking | `/digital-coffee` | [Copy and native assembly](../page-assets/digital-coffee-page-copy.md) |
| Digital Coffee confirmation | `/digital-coffee-confirmation` | [Copy](../page-assets/digital-coffee-confirmation-page-copy.md), [body HTML](../page-assets/digital-coffee-confirmation.html) |

[Page titles, descriptions, canonical and indexing proposals](../page-assets/appointment-pages-settings.md)
are prepared alongside the visible copy. Each confirmation provides the session
format, expectations, three concrete preparation steps, and a small help section.
Authority is conveyed through relevant nonprofit preparation and Tyler's existing
CPA identity, without adding credentials, guarantees, or promotional blocks.

## Successful booking and session details

The provider's completed-booking result is the source of truth for success.
Email/calendar invitations supply the booked date, time, time zone, and Teams
link. Static confirmation content must not fabricate those values or assert an
independently verified booking. No custom lookup, query-parameter personalization,
contact data, scheduling API, or new success-event emitter is included.

Before publication, verify the real native success-to-redirect behavior. If an
immediate success indication or usable meeting details are missing, record that
specific gap and resolve its native configuration within approved scope before
calling the journey complete. Page publication alone is not successful booking,
message delivery, or analytics delivery. No artificial booking/message is
created without a defined test authorization and controlled destination.

## Routing and deployment sequence

1. Inspect current exact website/page IDs, domain paths/redirects, and the
   Discovery and Digital Coffee calendars' redirect fields. Capture only the changed settings and a supported
   recovery baseline; never export customer records or credentials.
2. Assemble Digital Coffee by duplicating Get Started's layout and selecting the
   existing Coffee calendar. Remove Discovery-specific copy, 45-minute metadata,
   schema, and image. Inspect the existing `/digital-coffee` → `/get-started`
   redirect; restore that exact rule if the later cutover must be reversed.
3. Create the two confirmation pages using their body assets and existing
   shared header/footer. Preview desktop/mobile; verify titles, links, current
   durations/method, inherited scripts, and proposed indexing settings.
4. Resolve the exact conflicting Coffee redirect and publish/check all three
   destinations **before** updating any calendar redirect. Preserve unrelated
   rules. No new website framework, hosting service, or domain change is needed.
5. Change only the two matching post-booking redirect fields to their dedicated
   confirmed-working destinations. Preserve forms, availability, Teams, guests,
   payments, notifications, existing workflow branches, and tracking identifiers.
6. Leave `/call-confirmation/` and the Onboarding calendar destination unchanged.
   The dated baseline says Onboarding still uses that shared path, so it cannot
   be removed or reassigned as part of this change. Do not redirect it universally
   to Discovery, infer the appointment type from URL text, or remove it blindly.
   Any legacy fallback or Onboarding destination work is deferred; this package
   does not implement a shared confirmation page.
7. Reconcile Social Media 40.10, foundation/current-state references, and 40.50's
   dependency after actual cutover. The Form 990 Discovery journey should use the
   dedicated Discovery confirmation destination; the older shared path is not a
   permanent requirement. Do not claim the funnel is operational from these files.

## Acceptance and limits

- Source/HTML consistency; one H1 per page; logical headings; readable mobile
  layout; visible keyboard focus; working accessible links; unchanged shared
  identity/legal/footer; protected body email markup.
- Coffee page displays the **15-minute Coffee** calendar, not the 45-minute
  Discovery calendar. Get Started remains unchanged. Inspect fresh host/method,
  form and success destination without selecting or submitting a slot.
- Correct pages render for canonical and required slash variants without loops
  or homepage fallback. Confirm no path conflict or unintended redirect chain.
- Direct confirmation visits and refreshes create zero appointments and zero
  confirmed-booking outcomes across relevant measurement rules. Inspect both
  scripts and platform URL rules; an HTML search alone is not runtime evidence.
- Post-cutover real booking, correct calendar-specific redirect, invitation/Teams
  delivery, reschedule/cancel behavior, and measurement receipt remain separate
  runtime acceptance items. No new synthetic test recipient or outcome is assumed.
- Proposed noindex/self-canonical/sitemap treatment must be saved and inspected
  in delivered HTML and headers after publication; source files do not prove it.

## Recovery

Capture previous exact calendar destination values and changed redirect rule
IDs/values before saving. If cutover fails, restore only those destination fields
and the exact Coffee redirect, then unpublish only the newly created pages if
appropriate. Do not restore the entire site, delete existing calendars/forms, or
unpublish shared customer workflows. Restoring the old destination recovers the
prior configuration but does **not** fix its documented homepage fallback; report
that limitation. Leave calendars pointing to functioning new pages if that is
safer, and contain only the failing change.

## Remaining work

- Owner review of the actual copy/settings and native preview.
- Current HighLevel read-only inspection; recoverable routing/calendar baseline.
- Legacy `/call-confirmation/` remains unchanged; its documented homepage fallback
  is unresolved for Onboarding while that work is deferred.
- Native assembly, publication, scoped calendar cutover, and separate live/runtime
  acceptance evidence. Connected tools in this chat do not provide HighLevel
  builder access; no live step has been attempted or claimed.
- Social Media documentation reconciliation after reviewed design/cutover.

`/resources/`, LinkedIn edits, notifications/CRM changes, Onboarding and other
calendars, the Form 990 funnel, and deferred CLS/LCP investigation are outside
this page package.

## Offline preparation validation — November 14, 2026

Repository link/convention validation, business-identity consistency, image-layout
validation, and all 21 existing image-validator regression tests passed during
preparation. Description character counts are recorded in the settings file.
The two body assets are script-free and contain one H1 each. These checks do not
verify HighLevel rendering, real booking success, notifications, analytics
receipt, publication, or indexing. Native desktop/mobile preview remains pending.

# MoveInSync FDE Case Study
## Improving the employee commute journey and the Google Play rating

**Prepared by:** Nilanshu Kumar Singh  
**Evidence snapshot:** Google Play listing and review text supplied for this assignment, October 2026

## Executive recommendation

The supplied Google Play listing shows **4.6/5 from approximately 1.15 lakh reviews**. The rating is a useful headline, but it does not reveal which parts of the commute journey create avoidable dissatisfaction. The visible review samples point to a clear priority: **make the booking state, pickup information, and recovery path trustworthy before optimizing rating prompts.**

Start with three P0 bets:

1. **Booking certainty:** show an unmistakable `Booked`, `Pending`, or `Not booked` state, with trip details and safe retry behavior.
2. **Tracking truth:** measure GPS freshness and pickup ETA error; show when location data was last updated instead of implying precision when the feed is stale.
3. **No-show fairness:** add timely pickup/check-in reminders, clear cancellation state, and a dispute path when trip events conflict.

Then improve app stability, notification quality, and support ownership. Measure the actual commute experience alongside ratings.

## What the supplied review samples suggest

The samples span the 1★–5★ review views supplied for the assignment. The text contains both praise and complaints:

| Theme | Evidence from the supplied review text | Product / operational implication |
|---|---|---|
| Booking clarity | One reviewer said a changed shuttle flow made it easy to think a cab was booked when it was not. Other reviews describe booking errors, missing trips, and confusing cancellation states. | Booking confirmation must be explicit and persistent; retry and cancellation behavior should be safe. |
| GPS and ETA | Reviewers describe stale or misplaced vehicle locations, inaccurate pickup/drop estimates, map zoom behavior, and missing live-location updates. Positive reviews also praise real-time tracking when it works. | Treat freshness and ETA error as reliability metrics; preserve tracking as a core value proposition. |
| Check-in and no-show | Reviewers ask for a reminder when a vehicle passes the pickup point and report surprise no-show outcomes or accidental cancellations. | Add configurable reminders and a transparent, auditable no-show/dispute flow. |
| App stability and access | Reviews mention long load times, crashes, OTP/login friction, network errors, and reinstall workarounds. | Prioritize crash-free sessions, load latency, authentication success, and app-version/device segmentation. |
| Notifications and coordination | Reviews describe late or missing alerts, excessive pop-ups, and requests for better rider/driver coordination. | Make alerts timely, actionable, and non-blocking; evaluate secure communication within employer policy. |
| Navigation and flexibility | Users request simpler navigation, clearer pickup points/building details, editable locations, bulk or recurring bookings, and fewer taps. | Improve the highest-frequency flows; show policy constraints before a user reaches a dead end. |
| Support and ownership | Some reviewers do not know whether a request was received or who owns the issue. Other responses point to employer transport configuration. | Acknowledge requests, assign a clear owner, show status, and route app issues separately from employer/operations issues. |
| Positive value | Reviewers praise simplified office commute, convenient trip information, helpful alerts, accurate tracking when functioning, and professional drivers/support. | Protect the working core experience while fixing failure cases. |

### Important interpretation

A high overall rating can coexist with a small number of high-impact failures. For a commute product, a booking that appears successful but is not, a stale ETA that causes a missed pickup, or a surprise no-show can be disproportionately damaging because the user may have no easy alternative.

The public reviews are self-selected feedback, not a random sample. The copied text also does not consistently preserve each individual review's star label. Therefore this analysis **does not claim exact 1★–5★ theme percentages**. Use the supplied samples to form hypotheses, then validate them against a reproducible review sample and internal product/operations data.

## Prioritized action plan

### P0 — First: remove commute-critical ambiguity

**1. Booking state and recovery**
- Show a persistent status: `Booked`, `Pending`, or `Not booked`.
- Display date, shift, pickup point, and service type on the confirmation screen.
- Make retry idempotent and prevent duplicate bookings.
- Show only the user's assigned ride prominently; keep alternatives secondary.
- Validate: booking completion rate, ambiguous booking contacts, duplicate booking rate, and booking-related 1★–2★ themes.

**2. Tracking and pickup ETA trust**
- Record GPS ping age and ETA error; segment by app version, device/OS, geography, and trip cohort.
- Show `Last updated X seconds/minutes ago` when the feed is stale.
- Investigate missing rider/vehicle markers separately from route/ETA calculation.
- Avoid showing a confident ETA when source data is stale.
- Validate: GPS freshness P50/P90, pickup ETA absolute error, failed location renders, and tracking-related support contacts.

**3. Check-in, no-show, and cancellation safety**
- Offer a configurable reminder before pickup and when the vehicle approaches the pickup point, subject to notification permissions and operational rules.
- Make check-in status and cutoff time visible.
- Add a confirmation step for trip cancellation and a clear undo/recovery path where operationally safe.
- Provide a dispute flow when vehicle GPS, assignment, and check-in events conflict.
- Validate: disputed no-shows per 1,000 trips, false no-show rate, cancellation errors, and no-show-related review themes.

### P1 — Next: improve reliability and recovery

**4. App stability and access**
- Track crash-free sessions, cold-start/load latency, OTP delivery and verification success, and forced-reinstall reports.
- Reproduce the highest-impact failures by app version, OS version, device model, and network type.
- Add actionable error messages and safe retry behavior.

**5. Notification quality**
- Audit delivery latency and duplicate frequency for booking, assignment, pickup, schedule changes, and cancellation.
- Remove non-essential or blocking pop-ups from safety-critical screens.
- Give users a clear notification preference surface without disabling essential safety messages.

**6. Support ownership**
- Give every in-app request a ticket ID, receipt confirmation, owner, status, and expected response window.
- Route app defects to product/engineering and employer-specific policy or transport operations to the correct customer owner.
- Close the loop with a short resolution note and link recurring issues to a product backlog.

### P2 — Validate after the baseline

- Simplify high-frequency booking and navigation flows; test before broad UI rollouts.
- Improve pickup-point details and location-editing clarity, including employer-defined restrictions.
- Evaluate secure driver/rider messaging or call workflows with safety, privacy, and customer policy constraints.
- Use neutral, frequency-capped Google Play review prompts only after a successful journey. Never gate prompts by sentiment, suppress negative feedback, or incentivize ratings. Do not interrupt booking, tracking, or SOS use.

## First 30 days

| Timing | Actions | Deliverable |
|---|---|---|
| Days 1–3 | Snapshot ratings/review count; collect a documented recent sample; tag themes; align on definitions with Product, Engineering, Support, and Operations. | Baseline report, taxonomy, data gaps, owners |
| Days 4–7 | Reproduce booking and tracking issues; map no-show/cancellation rules; connect reviews to operational logs where possible. | Ranked issue backlog with acceptance criteria |
| Week 2 | Ship narrow booking-state and tracking observability fixes; prototype reminder/dispute flow; improve support receipt/status. | Controlled release and instrumentation |
| Weeks 3–4 | Compare before/after by app version and cohort; review new low-star and high-star samples; manually audit labels. | Impact report, next priorities, release decisions |
| Weekly thereafter | Repeat review collection, classification, validation, owner assignment, and trend comparison. | Recurring rating and journey-health report |

## KPI scorecard

| Area | Metrics |
|---|---|
| Booking | Completion rate, booking failure rate, duplicate booking rate, booking-related support contacts |
| Tracking | GPS freshness P50/P90, pickup ETA absolute error, share of trips with stale/missing location |
| Check-in / no-show | Disputed no-shows per 1,000 trips, false no-show rate, cancellation error rate |
| App reliability | Crash-free sessions, p95 app load time, OTP delivery/verification success |
| Notifications | Delivery latency, duplicate alert rate, alert open/action rate |
| Support | Time to owner, first response time, time to resolution, repeat-contact rate |
| Ratings | Rolling 30-day average, 1★–2★ share in a defined sample, themes by star band, response time, app-version trend |

Set numerical targets only after a reliable baseline exists. Avoid promising a rating lift without evidence; the first objective is to reduce failures that cause poor reviews.

## Repeatable review-intelligence workflow

The assignment says the ratings question will recur. A lightweight weekly workflow should:

1. Capture a dated Play Store rating/review-count snapshot and the newest available written reviews.
2. Preserve the original review text and all available metadata (rating, date, app version, language, developer reply).
3. Classify with a stable taxonomy: `booking`, `GPS/ETA`, `check-in/no-show`, `crash/performance`, `login/OTP`, `notifications`, `cancellation/reschedule`, `pickup/route`, `support`, `policy/operations`, `safety`, `positive`, `other`.
4. Manually audit a sample of classifications and the `other` bucket.
5. Report counts and shares only when the sample frame and star metadata are available; otherwise label the output qualitative.
6. Turn recurring themes into owner-assigned issues with evidence, acceptance criteria, and KPI links.
7. Compare subsequent review windows and operational metrics by app version.

Possible implementation: Python for parsing/classification, CSV/Markdown for reporting, and GitHub Issues/Actions for repeatability. Verify that the review source/export is available and permitted before automating collection; do not assume a public page exposes a complete review feed.

## Method, tools, and limitations

**Method:** reviewed the assignment brief and FDE job description; synthesized the supplied Google Play listing and review-text snapshots; grouped feedback by employee-journey stage; prioritized by impact on a time-sensitive commute, likely recurrence, and ability to measure; proposed a 30-day plan and recurring review workflow.

**Tools:** supplied public Google Play text snapshots, the provided PDFs, AI-assisted synthesis, Markdown, and PowerPoint.

**Limitations:** no internal event logs, booking funnel, GPS traces, crash analytics, notification delivery data, support tickets, or representative full review export were supplied. Review text is self-selected. Root causes and priorities are hypotheses to validate; no complaint percentages or causal rating-lift estimates are fabricated.

## Reference

- Google Play listing for MoveInSync employee app: https://play.google.com/store/apps/details?id=com.moveinsync.ets

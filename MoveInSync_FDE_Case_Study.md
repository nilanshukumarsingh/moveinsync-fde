# MoveInSync FDE Case Study
## Improving the employee commute journey and the Google Play rating

**Prepared by:** Nilanshu Kumar Singh  
**Evidence:** public Google Play listings and visible review text, collected by me in October 2026

## Executive recommendation

The employee app's public Google Play listing shows **4.6/5 from about 1.15 lakh ratings**. The headline is healthy, but it hides the failures that cost trust. The reviews I read point to one priority: **make the booking state, pickup information and recovery path trustworthy before optimizing rating prompts.**

Three P0 bets, each with an owner and a first action for the next day:

| # | Bet | Owner | First action |
|---|---|---|---|
| 1 | **Booking certainty:** show an unmistakable `Booked`, `Pending` or `Not booked` state with trip details and safe retry | Product + Android | Review the July 2026 release diff for the shuttle and cab booking screens; list every screen where a shuttle request can look like a confirmed cab |
| 2 | **Tracking truth:** measure GPS freshness and pickup ETA error; show when location data was last updated | Engineering | Add dashboards for GPS ping age and ETA error, split by app version and device/OS |
| 3 | **No-show fairness:** timely pickup/check-in reminders, clear cancellation state, and a dispute path when trip events conflict | Product + Ops | Confirm with Ops how a no-show is triggered today and how a rider can dispute it |

Then improve app stability, notification quality and support ownership, and measure the real commute alongside ratings.

## Evidence

Listing figures checked 13 Oct 2026:

| App | Rating | Ratings | Installs |
|---|---|---|---|
| MoveInSync (employee app) | 4.6 | ~1.15 lakh | 10L+ |
| MoveInSync Partner Lite (driver) | 4.2 | ~703 | 1L+ |
| MoveInSync Field app | 4.1 | ~24 | 5K+ |
| MoveInSync Driver Partner | 3.5 | ~46 | 10K+ |

Reviews analysed: **[FILL IN: number of reviews you read, the app(s), and the date range]**.

This analysis is scoped to the employee app. The driver apps are rated lower and are a follow-up track: Driver Partner reviews describe applications stuck at "In Review" with no follow-up, and Partner Lite reviews describe inaccurate kilometre counting and overheating.

## What the review text suggests

| Theme | What reviewers said (paraphrased) | Product / operational implication |
|---|---|---|
| Booking clarity | A changed shuttle flow made it easy to think a cab was booked when it was not; booking now takes an extra step | Booking confirmation must be explicit and persistent; retry and cancellation must be safe |
| GPS and ETA | Slow tracking, wrong pickup and drop times, other riders' locations often missing; real-time tracking is praised when it works | Treat freshness and ETA error as reliability metrics; protect tracking as the core value |
| Check-in and no-show | Riders ask for a reminder when the vehicle passes the pickup point and report surprise no-show outcomes | Configurable reminders and an auditable no-show/dispute flow |
| App stability and access | Long load times, crashes, OTP/login friction, reinstall workarounds | Track crash-free sessions, load latency and OTP success by app version and device |
| Notifications and coordination | Late or missing alerts, excessive pop-ups, requests for better rider/driver coordination | Timely, actionable, non-blocking alerts |
| Support and ownership | Reviewers do not know whether a request was received or who owns it | Acknowledge requests, assign an owner, show status; route app issues separately from employer/operations issues |
| Positive value | Praise for simplified commute, trip information, helpful alerts, accurate tracking when it works | Protect the working core while fixing failure cases |

### Important interpretation

A high overall rating can coexist with a small number of high-impact failures. A booking that looks successful but is not, a stale ETA that causes a missed pickup, or a surprise no-show can be disproportionately damaging because the rider may have no alternative.

Public reviews are self-selected, and star labels were not preserved on the review text I collected. This analysis therefore **does not claim exact 1★–5★ theme percentages**. Treat the themes as hypotheses and validate them with the repeatable workflow below and with internal product and operations data.

## Prioritized action plan

### P0: remove commute-critical ambiguity

**1. Booking state and recovery** (Product + Android)
- Show a persistent status: `Booked`, `Pending` or `Not booked`.
- Show date, shift, pickup point and service type on the confirmation screen.
- Make retry idempotent and prevent duplicate bookings.
- Show the user's assigned ride prominently; keep alternatives secondary.
- Validate: booking completion rate, ambiguous-booking contacts, duplicate booking rate, booking-related 1★–2★ themes.

**2. Tracking and pickup ETA trust** (Engineering)
- Record GPS ping age and ETA error; segment by app version, device/OS, geography and trip cohort.
- Show `Last updated X seconds/minutes ago` when the feed is stale; avoid a confident ETA on stale data.
- Investigate missing rider/vehicle markers separately from route and ETA calculation.
- Validate: GPS freshness P50/P90, pickup ETA absolute error, failed location renders, tracking-related support contacts.

**3. Check-in, no-show and cancellation safety** (Product + Ops)
- Configurable reminder before pickup and when the vehicle approaches the pickup point.
- Visible check-in status and cutoff time.
- Confirmation step for cancellation, with an undo path where operationally safe.
- Dispute flow when vehicle GPS, assignment and check-in events conflict.
- Validate: disputed no-shows per 1,000 trips, false no-show rate, cancellation errors, no-show-related review themes.

### P1: improve reliability and recovery

**4. App stability and access** (Engineering): track crash-free sessions, cold-start and load latency, OTP delivery and verification success; reproduce top failures by app version, OS, device and network; add actionable error messages.

**5. Notification quality** (Engineering + Product): audit delivery latency and duplicates for booking, assignment, pickup, schedule change and cancellation; remove blocking pop-ups from safety-critical screens; give a preference surface that cannot disable essential safety messages.

**6. Support ownership** (Support + Ops): ticket ID, receipt confirmation, owner, status and expected response window for every in-app request; route app defects to Product/Engineering and employer-specific policy to the customer owner; reply to every 1★–2★ review within 48 hours with a specific, non-canned response.

### P2: validate after the baseline

- Simplify high-frequency booking and navigation flows; test before broad UI rollouts.
- Clarify pickup-point details and location-editing limits, including employer restrictions.
- Evaluate secure driver/rider messaging within safety, privacy and customer policy.
- Use neutral, frequency-capped Google Play review prompts only after a successful journey. Never gate prompts by sentiment, suppress negative feedback or incentivize ratings, and never interrupt booking, tracking or SOS use.

### Follow-up track: driver apps
Add a status timeline and notifications to Driver Partner onboarding (submitted, verified, approved) with a stated turnaround, fix the document-upload failure, and profile battery drain and kilometre accuracy in Partner Lite.

## First 30 days

| Timing | Actions | Deliverable |
|---|---|---|
| Days 1–3 | Snapshot ratings and review count; collect a documented recent review sample; tag themes; align definitions with Product, Engineering, Support and Ops | Baseline report, taxonomy, data gaps, owners |
| Days 4–7 | Reproduce booking and tracking issues; map no-show and cancellation rules; connect reviews to operational logs where possible | Ranked issue backlog with acceptance criteria |
| Week 2 | Ship narrow booking-state and tracking observability fixes; prototype reminder/dispute flow; improve support receipt and status | Controlled release and instrumentation |
| Weeks 3–4 | Compare before/after by app version and cohort; read new low-star and high-star samples; manually audit labels | Impact report, next priorities, release decisions |
| Weekly after | Repeat collection, classification, validation, owner assignment and trend comparison | Recurring rating and journey-health report |

## KPI scorecard

| Area | Metrics |
|---|---|
| Booking | Completion rate, failure rate, duplicate booking rate, booking-related support contacts |
| Tracking | GPS freshness P50/P90, pickup ETA absolute error, share of trips with stale or missing location |
| Check-in / no-show | Disputed no-shows per 1,000 trips, false no-show rate, cancellation error rate |
| App reliability | Crash-free sessions, p95 load time, OTP delivery and verification success |
| Notifications | Delivery latency, duplicate alert rate, alert open/action rate |
| Support | Time to owner, first response, time to resolution, repeat-contact rate |
| Ratings | Rolling 30-day average, 1★–2★ share, themes by star band, reply rate and time, app-version trend |

Set numerical targets only after a reliable baseline exists. Do not promise a rating lift without evidence; the first objective is to reduce the failures that cause poor reviews.

## Repeatable review monitor (built)

The assignment says the ratings question will recur, so I built `review_monitor.py` (Python, `google-play-scraper` + `pandas`). One command pulls reviews for every MoveInSync app, tags each review with a theme, and writes a CSV plus a markdown summary with:
- mean rating, 1★–2★ share and trend (older half vs newer half of the window)
- reply rate on 1★–2★ reviews
- top complaint themes
- lowest-rated app versions (at least 10 reviews)

Run it weekly (cron or GitHub Actions), review the `other` bucket and extend the keyword taxonomy, then turn recurring themes into owner-assigned issues. Check Google Play's terms before scheduling automated collection.

```
pip install google-play-scraper pandas
python review_monitor.py --days 90
```

## Method, tools and limitations

**Method:** read the assignment brief and FDE job description; collected public Google Play listing data and visible review text; grouped feedback by employee-journey stage; prioritized by impact on a time-sensitive commute, likely recurrence and measurability; proposed a 30-day plan and a recurring review workflow.

**Tools:** web search and page fetch for the public listings, Claude for synthesis and drafting, Python (`google-play-scraper`, `pandas`) for the monitor, Markdown and PowerPoint for the write-up.

**Limitations:** no internal event logs, booking funnel, GPS traces, crash analytics, notification delivery data or support tickets were available. Review text is self-selected. Root causes and priorities are hypotheses to validate; no complaint percentages or rating-lift estimates are invented.

## References

- [MoveInSync employee app](https://play.google.com/store/apps/details?id=com.moveinsync.ets)
- [MoveInSync Driver Partner](https://play.google.com/store/apps/details?id=com.moveinsync.driver.dco)
- [MoveInSync Partner Lite](https://play.google.com/store/apps/details?id=com.moveinsync.driver.lite)
- [MoveInSync Field app](https://play.google.com/store/apps/details?id=field.moveinsync.ets)
- [MoveInSync on recovering its Play Store rating](https://moveinsync.com/?p=6499)

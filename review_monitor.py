"""
MoveInSync Play Store review monitor.

Answers the recurring question "How are our Play Store ratings?" in one command.
Pulls public reviews for every MoveInSync app, tags each review with a theme,
and writes a CSV plus a markdown summary (trend, themes, worst offenders).

Setup:   pip install google-play-scraper pandas
Run:     python review_monitor.py            (last 90 days, India, English+Hindi)
         python review_monitor.py --days 30
Schedule weekly (cron / GitHub Actions) and commit the markdown summary.
"""
import argparse
import re
from datetime import datetime, timedelta

import pandas as pd
from google_play_scraper import Sort, reviews

APPS = {
    "MoveInSync (employee)": "com.moveinsync.ets",
    "Field app": "field.moveinsync.ets",
    "Driver Partner": "com.moveinsync.driver.dco",
    "Partner Lite": "com.moveinsync.driver.lite",
    "Workplace": "com.workinsync.meeting",
}

# Ordered: first match wins. Extend after reading the "other" bucket each week.
THEMES = {
    "no_show_checkin": r"no.?show|check.?in|marked absent|absent",
    "gps_tracking_eta": r"gps|track|live location|eta|pickup time|drop time|late|delay|wrong time",
    "booking_flow": r"book|shuttle|seat|roster|schedul|cancel|slot|route",
    "ui_after_update": r"update|new ui|interface|version|difficult to use|confus",
    "login_otp": r"login|log in|otp|sign.?in|password|verify|sso",
    "crash_performance": r"crash|slow|hang|stuck|lag|not working|bug|error|battery|heat|restart",
    "driver_onboarding": r"document|registration|in review|approval|approve|upload|kyc",
    "km_payout": r"\bkm\b|kilomet|payment|payout|earning|trip count|incentive",
    "support": r"support|customer care|no response|nobody|complain",
    "reports_data": r"report|download|export|dashboard",
}


def tag(text: str) -> str:
    t = (text or "").lower()
    for name, pat in THEMES.items():
        if re.search(pat, t):
            return name
    return "other"


def fetch(app_id: str, since: datetime) -> list:
    out, token = [], None
    while True:
        batch, token = reviews(
            app_id, lang="en", country="in", sort=Sort.NEWEST,
            count=200, continuation_token=token,
        )
        if not batch:
            break
        out.extend(batch)
        if batch[-1]["at"] < since or token is None:
            break
    return [r for r in out if r["at"] >= since]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90)
    args = ap.parse_args()
    since = datetime.now() - timedelta(days=args.days)

    rows = []
    for name, app_id in APPS.items():
        for r in fetch(app_id, since):
            rows.append({
                "app": name, "date": r["at"], "score": r["score"],
                "text": r["content"], "app_version": r.get("reviewCreatedVersion"),
                "thumbs_up": r["thumbsUpCount"], "replied": r["replyContent"] is not None,
                "theme": tag(r["content"]),
            })
    df = pd.DataFrame(rows)
    stamp = datetime.now().strftime("%Y-%m-%d")
    df.to_csv(f"reviews_{stamp}.csv", index=False)

    lines = [f"# Play Store health, {stamp} (last {args.days} days)\n"]
    for app, g in df.groupby("app"):
        half = since + timedelta(days=args.days / 2)
        recent, prior = g[g.date >= half], g[g.date < half]
        neg = g[g.score <= 2]
        lines.append(f"## {app}")
        lines.append(f"- Reviews: {len(g)} | mean {g.score.mean():.2f} | 1-2 star share {len(neg)/len(g):.0%}")
        if len(recent) and len(prior):
            lines.append(f"- Trend: {prior.score.mean():.2f} -> {recent.score.mean():.2f} (older half -> newer half)")
        lines.append(f"- Reply rate on 1-2 star reviews: {neg.replied.mean():.0%}" if len(neg) else "- No 1-2 star reviews")
        top = neg.theme.value_counts().head(5)
        lines.append("- Top complaint themes (1-2 star):")
        for th, n in top.items():
            lines.append(f"  - {th}: {n} ({n/len(neg):.0%})")
        by_ver = g.groupby("app_version").score.agg(["mean", "count"])
        by_ver = by_ver[by_ver["count"] >= 10].sort_values("mean").head(3)
        if len(by_ver):
            lines.append("- Lowest-rated versions (n>=10): " + ", ".join(
                f"{v} ({m:.2f}, n={int(c)})" for v, (m, c) in by_ver.iterrows()))
        lines.append("")
    with open(f"summary_{stamp}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()

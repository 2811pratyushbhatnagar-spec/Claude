#!/usr/bin/env python3
"""review_metric.py -- Class-A review instrumentation (PILOT; built, not running).

DIAGNOSTIC, NEVER TARGET. These metrics measure PACKET QUALITY, not reviewer throughput.
They are never surfaced as approval pressure, never aggregated into reviewer scores, and a slow
review with many context-requests is a GOOD finding (the packet was thin), not a failure.
Running the pilot is the steward's call; this tool only exists so the pilot can start instantly.

Usage:
  python review_metric.py --item Q-R1-GENERAL --minutes 25 \
      --context "wanted the raw audit attack list;wanted n=4 witness examples" --confidence 0.8
"""
import argparse, json, os, datetime

ap = argparse.ArgumentParser()
ap.add_argument("--item", required=True)
ap.add_argument("--minutes", type=float, required=True, help="time the review took (diagnostic only)")
ap.add_argument("--context", default="", help="semicolon-separated: context requested that was NOT in the packet")
ap.add_argument("--confidence", type=float, required=True, help="reviewer confidence after (0..1)")
args = ap.parse_args()

rec = {
    "item": args.item,
    "reviewed_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    "minutes": args.minutes,
    "additional_context_requested": [c.strip() for c in args.context.split(";") if c.strip()],
    "confidence_after": args.confidence,
    "_register": "diagnostic of packet quality; NEVER a target; NEVER approval pressure",
}
p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 ".automation", "review_metrics.jsonl")
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "a", encoding="utf-8") as f:
    f.write(json.dumps(rec) + "\n")
n = len(rec["additional_context_requested"])
print(f"recorded. packet-quality signal: {n} context-request(s) "
      f"{'-> packet was thin; improve the packet (a good finding)' if n else '-> packet was sufficient'}")

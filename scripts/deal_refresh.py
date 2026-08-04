#!/usr/bin/env python3
"""Print a short, city-scoped deal-refresh board from the source registry.

This script intentionally does not pretend to verify a live coupon. It turns the
maintained source registry into a focused checklist; open each official source
and record results in data/deal-discovery-queue.csv / docs/verification-log.md.

Examples:
  python3 scripts/deal_refresh.py --city Seoul
  python3 scripts/deal_refresh.py --city all --format markdown
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "city-source-registry.csv"
VALID_CITIES = {"Seoul", "Busan", "Cheonan", "Daejeon", "Nationwide"}


def read_rows() -> list[dict[str, str]]:
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a focused city deal-refresh checklist.")
    parser.add_argument("--city", default="all", help="Seoul, Busan, Cheonan, Daejeon, Nationwide, or all")
    parser.add_argument("--format", choices=("text", "markdown"), default="text")
    args = parser.parse_args()
    requested = args.city.strip().title()
    if requested != "All" and requested not in VALID_CITIES:
        parser.error(f"unknown city '{args.city}'. Choose: all, " + ", ".join(sorted(VALID_CITIES)))

    rows = read_rows()
    if requested != "All":
        rows = [r for r in rows if r["city"] in {requested, "Nationwide"}]
    rows.sort(key=lambda r: (r["city"], int(r["priority"]), r["search_lane"]))

    today = date.today().isoformat()
    if args.format == "markdown":
        print(f"# Deal refresh board — {requested} — {today}\n")
        print("Open each source, verify the exact live terms, then log the result. "
              "A source being listed is not proof that a coupon is still valid.\n")
        print("| City | Priority | Lane | Source | Verify now | Access |")
        print("| --- | ---: | --- | --- | --- | --- |")
        for r in rows:
            print(f"| {r['city']} | {r['priority']} | {r['search_lane']} | "
                  f"[{r['source_name']}]({r['source_url']}) | {r['what_to_check']} | {r['tourist_access']} |")
    else:
        print(f"DEAL REFRESH BOARD — {requested.upper()} — {today}")
        print("Rule: validate date, city/branch, price, eligibility and terms before calling anything a deal.\n")
        city = None
        for r in rows:
            if city != r["city"]:
                city = r["city"]
                print(f"[{city}]")
            print(f"  P{r['priority']} {r['search_lane']}: {r['source_name']}")
            print(f"     {r['source_url']}")
            print(f"     Check: {r['what_to_check']} ({r['tourist_access']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

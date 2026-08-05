#!/usr/bin/env python3
"""Summarize actual couple spending and savings from data/couple-budget.csv."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "data" / "couple-budget.csv"


def number(raw: str) -> int:
    return int((raw or "0").replace(",", ""))


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize the couple budget tracker.")
    parser.add_argument("--city", default="all", help="filter city or use all")
    args = parser.parse_args()
    with DEFAULT.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.city.lower() != "all":
        rows = [row for row in rows if row["city"].casefold() == args.city.casefold()]
    if not rows:
        print("No real couple-budget rows yet. Copy the example format only after a purchase happens.")
        return 0
    totals: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    for row in rows:
        bucket = totals[row["city"]]
        bucket[0] += number(row["planned_krw"])
        bucket[1] += number(row["actual_krw"])
        bucket[2] += number(row["saving_krw"])
    print("CITY        PLANNED       ACTUAL        SAVED")
    print("----------- ------------- ------------- -------------")
    overall = [0, 0, 0]
    for city, values in sorted(totals.items()):
        print(f"{city[:11]:11} ₩{values[0]:>11,} ₩{values[1]:>11,} ₩{values[2]:>11,}")
        for i in range(3): overall[i] += values[i]
    print("----------- ------------- ------------- -------------")
    print(f"TOTAL       ₩{overall[0]:>11,} ₩{overall[1]:>11,} ₩{overall[2]:>11,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

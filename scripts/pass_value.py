#!/usr/bin/env python3
"""Calculate whether a pass/payment product beats individual planned costs.

Examples:
  python3 scripts/pass_value.py --name "Discover Seoul Pass Pick 3" --pass-price 49000 \
    --item "Attraction 1=25000" --item "Attraction 2=18000" --item "Attraction 3=22000"
  python3 scripts/pass_value.py --name "Climate Card 3-day" --pass-price 10000 \
    --item "Day 1 transit=6200" --item "Day 2 transit=5500" --item "Day 3 transit=4800"
"""
from __future__ import annotations

import argparse


def won(value: int) -> str:
    return f"₩{value:,}"


def parse_item(raw: str) -> tuple[str, int]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("each --item must be written as Label=KRW, for example Metro=6200")
    label, raw_value = raw.rsplit("=", 1)
    label = label.strip()
    try:
        value = int(raw_value.replace(",", "").strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid KRW amount in '{raw}'") from exc
    if not label or value < 0:
        raise argparse.ArgumentTypeError("item label must be non-empty and amount must be zero or positive")
    return label, value


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare a live pass price with costs you would otherwise pay.")
    parser.add_argument("--name", required=True, help="pass/payment product name")
    parser.add_argument("--pass-price", type=int, required=True, help="live pass price in KRW")
    parser.add_argument("--item", action="append", type=parse_item, required=True, help="planned covered item: Label=KRW")
    args = parser.parse_args()
    if args.pass_price < 0:
        parser.error("--pass-price must be zero or positive")

    total = sum(value for _, value in args.item)
    delta = total - args.pass_price
    print(f"{args.name.upper()} VALUE MATH")
    for label, value in args.item:
        print(f"  {label}: {won(value)}")
    print(f"  Individual-value total: {won(total)}")
    print(f"  Live pass price:        {won(args.pass_price)}")
    if delta > 0:
        print(f"  Result: BUY IF TERMS FIT — planned value exceeds price by {won(delta)}.")
    elif delta < 0:
        print(f"  Result: SKIP — individual purchases save {won(-delta)}.")
    else:
        print("  Result: TIE — choose the simpler option only if timing/coverage fit.")
    print("\nNever count attractions you would not otherwise visit, optional add-ons, or excluded routes.")
    print("Check activation window, branch/attraction eligibility, reservation rules, and cancellation terms.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

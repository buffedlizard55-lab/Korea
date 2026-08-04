#!/usr/bin/env python3
"""Compare a live KORAIL PASS quote with the individual train fares you will use.

Examples:
  python3 scripts/rail_pass_math.py --pass-price 121000 --fares 59800 59800
  python3 scripts/rail_pass_math.py --pass-price 121000 --fares 59800 59800 23700

Use the live KORAIL booking screen for every input. This tool does not quote fares.
"""
from __future__ import annotations

import argparse


def won(amount: int) -> str:
    return f"₩{amount:,}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Tell whether a KORAIL PASS costs less than your planned individual KORAIL tickets."
    )
    parser.add_argument("--pass-price", type=int, required=True, help="live KORAIL PASS price in KRW")
    parser.add_argument("--fares", type=int, nargs="+", required=True, help="one live individual KORAIL fare per planned leg")
    args = parser.parse_args()

    if args.pass_price < 0 or any(fare < 0 for fare in args.fares):
        parser.error("prices and fares must be zero or positive")

    tickets = sum(args.fares)
    difference = tickets - args.pass_price
    print("KORAIL PASS MATH")
    print(f"  Individual KORAIL legs ({len(args.fares)}): {won(tickets)}")
    print(f"  Live pass quote:                    {won(args.pass_price)}")
    if difference > 0:
        print(f"  Result: PASS SAVES {won(difference)} per traveler, before reservation constraints.")
    elif difference < 0:
        print(f"  Result: INDIVIDUAL TICKETS SAVE {won(-difference)} per traveler.")
    else:
        print("  Result: TIE — choose the simpler option after checking train availability.")
    print("\nBefore buying: KORAIL PASS does not cover SRT, metropolitan subway, or special tourist trains.")
    print("Check the live pass terms, seat availability, refund rules, and every planned train first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

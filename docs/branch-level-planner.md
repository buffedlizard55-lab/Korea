# 📌 Branch-Level Deal Planner — Add Exact Places After Hotels Are Booked

General chain research becomes real only when it is tied to your hotel, station exit, walking time, and the current branch hours.

> **Last verified: 2026-08-04** · Live data: [`data/branch-options.csv`](../data/branch-options.csv) · Use the [Hotel Neighborhood Template](hotel-neighborhood-template.md) first.

## Do not add branches too early

A branch can close, move, exclude a promotion, or become impractical after the hotel changes. Add exact locations only when you know:

- hotel neighborhood and Korean address,
- approximate arrival/check-in time,
- the station/exit you will actually use,
- which city you chose for the flexible third-city leg.

## One branch card per city

| Need | Add one practical option | Why it belongs |
| --- | --- | --- |
| Breakfast | Gimbap/soup/convenience store within 10 minutes | Prevents expensive hotel breakfast or hungry detours |
| Coffee | Budget coffee or refill point near station | Standing low-effort saving |
| Main meal | One walk-in-value chain or local posted-price meal | Works even when a coupon fails |
| Deal option | One branch that accepts the pass/coupon/payment layer | Check only when already on your route |
| Late fallback | 24-hour diner, delivery, or convenience store | Covers late arrival/closed restaurant |

## Add a real option

1. Open Naver Map in Korean.
2. Search the Korean branch/dish name within the hotel neighborhood.
3. Open the specific listing—not just a generic chain search.
4. Record the Naver Map link, hours/last order, and the exact live check in `data/branch-options.csv`.
5. Keep one normal-priced backup in the same area.

```bash
python3 scripts/branch_options.py --city Seoul
```

## City notes

- **Incheon:** save only arrival-night food, airport/AREX routing, and departure tax-refund/lounges; do not schedule a citywide coupon hunt.
- **Seoul:** make cards for the actual hotel neighborhood, not all of Myeongdong/Hongdae/Gangnam.
- **Busan:** choose one base—Nampo, Seomyeon, or Haeundae—because cross-city travel is costly in time.
- **Cheonan:** record City Tour/Tourism Taxi pickup and Independence Hall transit only after dates are confirmed.
- **Daejeon:** save science/museum route options and the actual City Tour/heritage pickup location.

> A branch-level entry is useful only if it saves time or money on a route you already want to take.

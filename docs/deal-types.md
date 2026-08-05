# 🏷️ Deal Types — Know What You Are Actually Using

A cheap normal meal is not a coupon. A future festival is not an active deal. This page separates the deal **type** from the deal **status**.

> **Last verified: 2026-08-04** · Status answers “can I use it now?” → [Deal Status Board](deal-status-board.md). Type answers “what kind of saving is this?”

| Type | What it is | How to use it | Example |
| --- | --- | --- | --- |
| 🍜 **Walk-in value** | Normal low menu price; no redemption required | Check the live branch menu and order normally | Dookki, budget burger, gimbap, local soup |
| 🎁 **Standing benefit** | Ongoing program with conditions | Read terms and meet the conditions before the visit | IKEA Family, Cheonan City Tour, immediate tax refund |
| 📲 **Live coupon** | Current barcode/banner/monthly promotion | Open the current app/chat/shelf tag; do not plan around an old screenshot | KakaoTalk coupon, Shuttle credit, convenience 1+1 |
| 🎫 **City pass** | Bundle of attractions/discounts | Run the pass math first; activate only when the itinerary is dense | Discover Seoul Pass, Visit Busan Pass |
| 🚇 **Transit pass** | Transport-only bundle | Count only eligible rides/routes; check activation day | Climate Card |
| 💳 **Payment layer** | Cashback/discount tied to payment method | Confirm merchant/rate/cap in the live app; never detour only for a tiny reward | Busan Pay, WOWPASS |
| 🆓 **Free attraction** | No-admission anchor | Check closure/reservation rules, then use it to reduce a day’s paid costs | Independence Hall, museums, guided walks |
| 📅 **Future event** | Announced/expected but not yet usable | Put the recheck date on the calendar; do not budget it today | Korea Sale Festa 2026 |
| ⛔ **Expired event** | A past offer kept as seasonal history | Ignore for this trip unless a new official edition appears | Daejeon summer ticket promotion |
| 🚫 **Rejected claim** | Resident-only, dead, unsupported, or wrong for this trip | Do not spend time pursuing it | Unsupported app birthday benefit |

## Fast decision tree

1. **Is it a walk-in value or free attraction?** Use it if it fits the neighborhood; no app hunt needed.
2. **Is it a live coupon/payment layer?** Check it only when already near a participating branch/merchant.
3. **Is it a city/transit pass?** Do the [Pass Value Dashboard](pass-value-dashboard.md) math before purchase.
4. **Is it future, expired, or rejected?** Do not add it to today’s budget.

## Why this helps a couple

For two people, normal walk-in value and free anchors are often more reliable than chasing separate coupons or reshaping an entire day to make a pass barely break even. Use the type label to avoid mistaking “possible discount” for “best plan.”

The canonical type for each core record is in [`data/deals.csv`](../data/deals.csv). Filter it with:

```bash
python3 scripts/deal_registry.py --city Seoul
```

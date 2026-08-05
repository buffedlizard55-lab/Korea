# 💑 Couple Budget Dashboard — Planned vs. Actual

This is the practical money view for **two travelers**. Record the total for both of you, not a per-person estimate.

> **Last verified: 2026-08-04** · Live file: [`data/couple-budget.csv`](../data/couple-budget.csv) · Format example: [`data/examples/couple-budget-example.csv`](../data/examples/couple-budget-example.csv)

## Before each city

| City | Transit plan | Food anchor | Attraction/pass decision | Couple ceiling | Mark |
| --- | --- | --- | ---: | ---: | --- |
| Incheon |  |  |  | ₩ | ☐ |
| Seoul |  |  |  | ₩ | ☐ |
| Busan |  |  |  | ₩ | ☐ |
| Cheonan **or** Daejeon |  |  |  | ₩ | ☐ |

Use the [Pass Value Dashboard](pass-value-dashboard.md) before entering a pass cost. Use [Deal Types](deal-types.md) to avoid counting a normal cheap meal as a coupon saving.

## During the trip

Add one row to `data/couple-budget.csv` for:

- transit/pass purchases,
- shared meals,
- attraction admissions,
- delivery,
- groceries/souvenirs where a tax refund or promotion actually worked.

Keep it simple: if there is no receipt or clear saving, enter the actual total and set saving to `0`.

## View totals

```bash
python3 scripts/couple_budget.py
python3 scripts/couple_budget.py --city Busan
```

## Couple-specific rules

1. **Split only shared costs.** Cheonan Tourism Taxi can be split between two; individual passes cannot.
2. **Compare a couple total.** A ₩20,000 per-person buffet is a ₩40,000 decision, not a ₩20,000 decision.
3. **Avoid forced minimum spends.** A coupon that needs extra unwanted food is not a saving.
4. **Count time as a cost.** A long detour for a tiny cashback is usually worse for two travelers than a nearby posted-price meal.
5. **Record failures too.** A `0` saving is useful evidence for the next city/day.

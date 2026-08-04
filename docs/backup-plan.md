# 🛟 Normal Local Backup Plan — When a Deal Does Not Work

Every core deal now has a **normal local backup**. This keeps a failed coupon, closed branch, full tour, or expired app banner from ruining the day.

> **Last verified: 2026-08-04** · Core backups live in [`data/deals.csv`](../data/deals.csv). Print them with `python3 scripts/deal_registry.py --city <City> --backups`.

## The 60-second fallback rule

If a deal fails, do not spend an hour troubleshooting it:

1. **Stop:** take one screenshot/note of why it failed.
2. **Use the saved backup:** it should not need a coupon, special app, or a far-away detour.
3. **Choose posted prices:** look at the Korean menu/shelf price before ordering.
4. **Log the failure:** add it to [Field Notes](field-notes.md) so it is not retried tomorrow.

## City backups at a glance

| City | If a pass/coupon/booking fails | Normal local backup |
| --- | --- | --- |
| Seoul | DSP/Climate Card/booking/coupon | Walkable neighborhood cluster, T-money fares, free museum or guided walk, posted-price lunch special/budget diner |
| Busan | VBP/Busan Pay/partner offer | Free museum cluster or coast trail, normal metro/bus, dwaeji gukbap/milmyeon/local meal with visible price |
| Cheonan | Tourism Taxi/City Tour | Normal transit to Independence Hall, free admission, route-adjacent meal with visible price |
| Daejeon | City Tour/heritage reservation | National Science Museum, Currency Museum, DMA collection, ordinary metro/bus, nearby local meal |
| Nationwide | Delivery credit/tax refund/brand coupon | Walk-in restaurant or nearby chain with a visible kiosk/menu price; buy goods only if wanted without a tax threshold |

## Examples

| Failed deal | Do this instead |
| --- | --- |
| Climate Card does not break even | Use T-money/individual transit and keep activities in one walkable area. |
| Discover Seoul Pass attraction is booked out | Buy only the one attraction you genuinely still want, or use a free museum/park/guide that day. |
| Visit Busan Pass partner disappears | Use a free museum or coastal trail and pay normal admission for at most one priority attraction. |
| Busan Pay merchant has no cashback | Pay by normal foreign card; do not load more balance just to chase a reward. |
| Cheonan Tourism Taxi sells out | Take the City Tour if its route fits; otherwise normal transit to Independence Hall. |
| Daejeon heritage session is full | Use the free National Science Museum/Currency Museum/DMA route. |
| Shuttle `VK2026` credit does not load | Use a walk-in restaurant near the hotel found on Naver Map. |
| Tax refund is unavailable | Buy only the items you would buy at the normal posted price—never add items to reach a threshold. |

## Why this matters for a couple

For two travelers, the backup often wins when a special product requires a detour, a minimum spend, or a long wait. A straightforward local meal plus normal transit can be cheaper than forcing a marginal pass or coupon.

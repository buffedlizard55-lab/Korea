# ⚖️ Effort vs. Savings Score — Is the Deal Worth It for Two?

A discount is not automatically a good plan. Core records now carry three practical fields in [`data/deals.csv`](../data/deals.csv): **effort**, **detour risk**, and **couple value**.

> **Last verified: 2026-08-04** · Use after checking status/type: [Deal Status Board](deal-status-board.md) · [Deal Types](deal-types.md)

## Read the score

| Field | Meaning |
| --- | --- |
| **Effort** | How much setup, booking, app work, or timing coordination it needs: low / medium / high |
| **Detour risk** | How likely it requires leaving your intended route: none / low / medium / high |
| **Couple value** | `strong` = generally worth considering for two; `conditional` = do math/live check; `live-check` = only use when already nearby/current |

## Default couple rules

| Score pattern | Decision |
| --- | --- |
| Low effort + low detour + strong | Add to the normal plan. |
| Medium effort + conditional | Do pass/taxi math before booking. |
| Live Check + low detour | Check it only when already at the branch/merchant. |
| Medium/high detour for a small coupon | Skip it; use the local backup. |
| Future/expired/rejected | Do not include it in the day’s expected savings. |

## Examples

| Deal type | Typical score | Why |
| --- | --- | --- |
| Free museum or normal low-price diner | Low effort / low detour / strong | It works without an app and lowers the day’s baseline cost. |
| Climate Card | Low effort / low detour / strong if math works | It is useful only when eligible rides beat the pass price. |
| City pass | Medium effort / medium detour / conditional | It can be great with a dense plan and poor with a loose itinerary. |
| Busan Pay / Kakao coupon | Medium effort / low detour / live-check | Check only at a current participating merchant; never reroute the day for it. |
| Cheonan Tourism Taxi | Medium effort / medium detour / conditional | Strong only when two people share a multi-stop, live-available route. |

> **Rule:** A nearby normal-price meal or free attraction is often better value than a small coupon requiring an app, a wait, and a long detour.

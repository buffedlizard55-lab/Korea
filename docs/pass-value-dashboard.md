# 🧮 Pass & Payment Value Dashboard

Use this **before buying a pass, transit product, or payment card**. A benefit only counts if you would have paid for it anyway, it fits the right city/day, and the live terms still allow you to use it.

> **Last verified: 2026-08-04** · Read the plain-English [Pass & Payment Rules](pass-rules.md) first · Live product data: [`data/pass-options.csv`](../data/pass-options.csv)

## Five rules that prevent tourist overspending

1. **Plan first, pass second.** Put real attractions/rides into the itinerary before looking at a pass price.
2. **Count only unavoidable spending.** Do not add a value for an attraction just because it is included.
3. **Use the correct activation window.** A 72-hour pass is not a three-calendar-day pass.
4. **Check exclusions before paying.** Airport buses, SRT, special trains, branch exclusions, reservations, and same-day rules matter.
5. **Re-run the math if the plan changes.** A cancelled attraction can erase the saving.

---

## 1. Seoul: Discover Seoul Pass

| Option | Current reference price | Use it only when | Do not count |
| --- | ---: | --- | --- |
| Pick 3 Basic | ₩49,000 | Your chosen 3 eligible attractions have a total normal price above ₩49,000 | Coupons, food, or attractions you would skip without the pass |
| 72-hour | ₩90,000 | You have a dense 72-hour plan with eligible admission/transport benefits | Benefits outside the active 72-hour window or separately paid add-ons |
| 120-hour | ₩130,000 | You will use enough eligible value across a real five-day attraction plan | “Maybe” attractions or benefits you lack time to use |

**Live check:** [official Discover Seoul Pass](https://www.discoverseoulpass.com). Partner list, reservation rules, attraction price, and pass types can change.

Example calculation:

```bash
python3 scripts/pass_value.py --name "DSP Pick 3" --pass-price 49000 \
  --item "Attraction A=25000" --item "Attraction B=18000" --item "Attraction C=22000"
```

---

## 2. Seoul: Climate Card Short-Term Pass

| Pass | Price | Break-even approach |
| --- | ---: | --- |
| 1 day | ₩5,000 | Add the eligible subway/bus fares you expect that day |
| 2 days | ₩8,000 | Add two days of eligible transit |
| 3 days | ₩10,000 | Add three days of eligible transit |
| 5 days | ₩15,000 | Add five days of eligible transit |
| 7 days | ₩20,000 | Add seven days of eligible transit |

It activates on loading. Do **not** count airport/intercity buses, excluded rail, or out-of-coverage trips. International-card vending-machine payments have an official reported service fee, so include that in a close decision.

```bash
python3 scripts/pass_value.py --name "Climate Card 3-day" --pass-price 10000 \
  --item "Day 1 eligible transit=6200" --item "Day 2 eligible transit=5500" --item "Day 3 eligible transit=4800"
```

🟢 [Seoul Metropolitan Government terms](https://english.seoul.go.kr/climate-cards-and-single-journey-transit-tickets-now-accepting-international-credit-cards-no-cash-needed/)

---

## 3. Busan: Visit Busan Pass

There is no universal “yes” answer. The pass works when the group clusters eligible attractions in one activation period.

| Before buying | Mark |
| --- | --- |
| I chose a specific VBP pass type and wrote its **live** price | ☐ |
| I listed only attractions we will actually visit | ☐ |
| I confirmed each attraction is included in **this** pass type | ☐ |
| I checked whether reservations/timed entry are needed | ☐ |
| Normal attraction total is higher than the live pass price | ☐ |
| Food partners are an extra bonus—not the only reason to buy | ☐ |

**Busan Pay layer:** if the live app confirms Visit Busan Pass purchase cashback, calculate it after the pass breaks even on its own. Do not count cashback at malls/duty-free or merchants not shown live in the app.

🟢 [official Visit Busan Pass](https://www.visitbusanpass.com/) · [official Busan Pay guide](https://www.busan.go.kr/bige/daily-busan/view?dataNo=69959&curPage=2&bbsNo=10&srchCl=Daily+Busan)

---

## 4. Cheonan: Tourism Taxi versus separate transport

Cheonan’s tourism taxi can be good **for a group**, not necessarily one person.

| Compare | Use the calculator inputs |
| --- | --- |
| Tourism Taxi | Current subsidized 4h or 8h quote, divided by travelers sharing it |
| Separate transport | Every planned rail/bus/taxi leg for the same route |
| Include | Time saved reaching Independence Hall, Yu Gwan-sun sites, or Byeongcheon | 
| Exclude | Food, admission, and shopping—not included in the taxi quote |

The advertised 50% support is first-come and needs a live availability check. See [Cheonan research](city-research-hub.md#3-cheonan-천안--unusually-strong-official-local-transport-value).

---

## 5. Nationwide: KORAIL PASS

Use the dedicated [KORAIL PASS Math worksheet](rail-pass-math.md). It is separate because a pass only covers KORAIL trains—**not SRT, metro, or special tourist trains**.

---

## Final decision record

Write the result here or in the [Field Notes](field-notes.md), so the group does not re-litigate the purchase at checkout.

| Product | Date checked | Live price | Individual total | Decision | Why |
| --- | --- | ---: | ---: | --- | --- |
|  |  | ₩ | ₩ | Buy / Skip |  |
|  |  | ₩ | ₩ | Buy / Skip |  |
|  |  | ₩ | ₩ | Buy / Skip |  |

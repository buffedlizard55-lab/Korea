# 🚆 KORAIL PASS Math — Buy It Only If It Actually Saves Money

A rail pass is not automatically a deal. Use this page after your Seoul / Busan / Cheonan / Daejeon dates are set.

> **Last verified: 2026-08-04** · **Do not use a blog price.** Get the live individual-fare and pass quotes from KORAIL before deciding.

## The rule

**Buy a KORAIL PASS only when the total of the KORAIL trains you will actually ride is greater than the live pass price.** Otherwise, buy individual tickets.

A standard Seoul–Busan return alone may not make a pass worthwhile. It becomes more plausible when the same traveler has multiple long **KORAIL-operated** rail days in the pass window.

## What it does *not* cover

The foreigner KORAIL PASS does **not** cover:

- **SRT** trains
- Seoul/metro-area **subways**
- **special tourist trains**

It is also personal: the passport name must match the pass. Do not buy one pass for a group to share.

🟢 [KORAIL foreigner-pass terms](https://www.letskorail.com/ebizbf/EbizbfForeign_pr16100.do?gubun=1) · [live KORAIL booking](https://smart.letskorail.com/ebizbf/EbizBfTicketSearchM.do)

---

## Five-minute decision worksheet

1. Write each intercity leg that **one person** will really take.
2. Open KORAIL and record the current individual fare for each leg and travel class.
3. Record the live KORAIL PASS price for the exact pass length/type.
4. Compare the two totals.
5. Check that the trains still have reservable seats before purchasing anything.

| One traveler's KORAIL leg | Date | Live individual fare | Use this leg? |
| --- | --- | ---: | --- |
| Example: Seoul → Busan |  | ₩ | ☐ |
| Example: Busan → Cheonan-Asan |  | ₩ | ☐ |
| Example: Cheonan-Asan → Daejeon |  | ₩ | ☐ |
| Example: Daejeon → Seoul |  | ₩ | ☐ |
| **Individual-ticket total** |  | **₩** |  |
| **Live KORAIL PASS quote** |  | **₩** |  |
| **Decision** |  | Pass saves / individual saves: **₩** |  |

### Fast calculator

The repository includes a local helper. Replace the sample figures with live quotes:

```bash
python3 scripts/rail_pass_math.py --pass-price 121000 --fares 59800 59800
```

It prints the cheaper option per traveler. It intentionally does **not** store KORAIL prices because fare/pass products and availability change.

---

## Important booking checks

- A pass can be mathematically cheaper but still poor value if your preferred departure is unavailable.
- Compare **KORAIL vs SRT** for any leg where both operate; an SRT ticket cannot be covered by KORAIL PASS.
- Do not count subway, local buses, airport rail, taxis, or city-tour transport as rail-pass savings.
- Keep the passport used for purchase with you when using the pass.
- Recheck refund/change terms before checkout.

> **Cheonan note:** use the station that matches your itinerary—**Cheonan** and **Cheonan-Asan** are different stations/services. Confirm the station on the live booking page before adding a fare to the worksheet.

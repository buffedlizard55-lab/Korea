# 🔀 Cheonan vs. Daejeon — Flexible Third-City Decision Engine

Do not choose the third city because of one theoretical coupon. Choose the city whose **live transport, hotel, program, and actual interests** create the better couple trip.

> **Last verified: 2026-08-05** · Run this only after rail/hotel options and live program availability are visible.

## Decision table

Score each city 0–5 after checking live information.

| Factor | Cheonan tends to win when… | Daejeon tends to win when… | Cheonan | Daejeon |
| --- | --- | --- | ---: | ---: |
| Interests | You want Independence Hall, Yu Gwan-sun, Byeongcheon/history | You want science, museums, bakeries, urban routes |  |  |
| Couple transport value | Tourism Taxi is available and a multi-stop route justifies splitting cost | Metro/bus/City Tour already fits the planned attractions |  |  |
| Live program | City Tour/November heritage route has a date/seat | Heritage session/City Tour/bread route has a date/seat |  |  |
| Hotel total | Practical final couple room price near station/route | Practical final couple room price near station/route |  |  |
| From previous city | Live rail/bus time and fare are lower/better | Live rail/bus time and fare are lower/better |  |  |
| Free anchors | Independence Hall plus route works | Science Museum, Currency Museum, DMA, heritage program work |  |  |
| Food fit | You want local history/sundae route | You want bakery/science/city food route |  |  |
| Low-effort backup | Normal transit still gives a good day | Free museums give a good day if a program sells out |  |  |
| **Total** |  |  |  |  |

## Hard rules

Choose **Cheonan** if:

- Tourism Taxi availability is confirmed **and** its couple split beats separate taxis/transit for a multi-stop day, or
- the City Tour/heritage route matches your actual date, or
- Independence Hall is a must-do.

Choose **Daejeon** if:

- a free heritage session or City Tour has live availability, or
- you want a low-cost science/museum/bakery day with strong no-coupon backups, or
- hotel/rail value is clearly better.

Do **not** choose either city until checking:

```bash
python3 scripts/trip_lock.py --as-of 2026-10-17
python3 scripts/rail_pass_math.py --pass-price <LIVE_PRICE> --fares <LIVE_FARES>
```

## Result statement

Write this before booking:

```text
We chose __________ because live transport was ₩____ for two, hotel total was ₩____,
and the confirmed anchor was __________. The backup if the program fails is __________.
```

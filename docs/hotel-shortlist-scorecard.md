# 🏨 Hotel Shortlist & Neighborhood Scorecard

Use this **before booking**. A cheaper room far from food/transit can cost more than a slightly higher room in a practical neighborhood.

> **Last verified: 2026-08-05** · Save real options in [`data/hotel-shortlist.csv`](../data/hotel-shortlist.csv). This does not rank hotels from the internet; it compares the options you personally found.

## Score each option from 0 to 5

| Factor | 0 means | 5 means |
| --- | --- | --- |
| Transit | Long/awkward walk and transfers | Very close to station/route you will use |
| Cheap food | Tourist-only or no late fallback | Breakfast, local meal, and late backup nearby |
| Convenience/coffee | No practical nearby basics | Multiple choices within a short walk |
| Airport/intercity access | Expensive/slow transfers | Direct or simple airport/rail connection |
| Delivery | Unclear/awkward lobby setup | Clear address, lobby pickup, good coverage |
| Attraction geography | Constant cross-city trips | Fits most planned days in that city |
| Price value | Poor room price for what you get | Best real couple price after all taxes/fees |
| Inflation risk | Major tourist premium/long detours | Normal local prices and walkable backups |

## City neighborhood starting points

| City | Good candidates to compare | Watch out for |
| --- | --- | --- |
| Seoul | Jongno/Gwanghwamun, Hongdae/Hapjeong, Seoul Station, Myeongdong, Yeouido | Myeongdong/Gangnam convenience premiums; long cross-city days |
| Busan | Seomyeon, Nampo, Haeundae | Haeundae to old-town travel time; Nampo to eastern coast travel time |
| Cheonan | Cheonan Station, Cheonan-Asan/terminal area | Cheonan and Cheonan-Asan are different rail/route choices |
| Daejeon | Daejeon Station, Yuseong, Dunsan | Choosing a base far from your science/museum or city-tour anchor |

## Compare saved options

```bash
python3 scripts/hotel_score.py
```

Record hotel price as the **total couple price per night including taxes/fees**, not an advertised starting price.

## Booking rule

Do not book until the winning option has:

- a verified Korean address,
- a nearest station/exit,
- one cheap breakfast and dinner fallback,
- a delivery/lobby plan,
- and an actual final price for two.

After booking, move the winner into the [Hotel Neighborhood Template](hotel-neighborhood-template.md).

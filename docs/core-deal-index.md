# 🗃️ Core Deal Index — Registry IDs for the Main Claims

This page is the bridge while the guide completes its migration from scattered prose to one structured source of truth.

> **Last verified: 2026-08-04** · Coverage mapping: [`data/claim-mapping.csv`](../data/claim-mapping.csv) · Canonical fields (status, source, recheck date, ID requirement, live-check flag, backup): [`data/deals.csv`](../data/deals.csv)

## How to use it

- Read the city/food guides for explanation and Korean context.
- Use this index and `data/deals.csv` for the current **status**, source, recheck date, and fallback.
- If prose and registry ever disagree, treat the registry as controlling until the prose is corrected.

## Everyday food & shopping

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-DOOKKI` | Dookki unlimited tteokbokki | Active | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-MYEONGRYUN` | Myeongryun Jinsa Galbi buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-NOBRAND` | No Brand Burger Amazing Bulgogi | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-MOMSTOUCH` | Mom’s Touch value set | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-CONVENIENCE` | Monthly convenience-store 1+1 / 2+1 | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-TONGIN` | Tongin Market coin lunchbox | Active | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-TAXREFUND` | Immediate tax refund | Active | [Money Guide](money-guide.md) |

## Sign-up, delivery & payment

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-IKEA` | IKEA Family weekday drink/member price | Active | [Birthday Freebies](birthday-freebies.md) |
| `NATIONWIDE-KAKAO` | Official KakaoTalk brand-channel coupons | Live Check | [Welcome Deals](signup-welcome-deals.md) |
| `NATIONWIDE-SHUTTLE` | Shuttle `VK2026` credit | Active | [Delivery Apps](delivery-apps.md) |
| `NATIONWIDE-BAEMIN` | Baemin Guest Checkout | Live Check | [Delivery Apps](delivery-apps.md) |
| `NATIONWIDE-WOWPASS` | WOWPASS partner cashback | Live Check | [Money Guide](money-guide.md) |

## City-specific anchors

| City | Registry IDs | Read with |
| --- | --- | --- |
| Seoul | `SEOUL-TRANSIT-CLIMATE`, `SEOUL-PASS-DSP`, `SEOUL-TOUR-WALK`, `SEOUL-TOUR-CHEONGWADAE`, `SEOUL-TONGIN` | [City Planning Board](city-planning-board.md) |
| Busan | `BUSAN-PAY`, `BUSAN-PASS-VBP`, `BUSAN-MUSEUM-ART`, `BUSAN-MUSEUM-MARITIME`, `BUSAN-MUSEUM-BOKCHEON` | [Busan Guide](busan-guide.md) |
| Cheonan | `CHEONAN-TAXI`, `CHEONAN-CITYTOUR`, `CHEONAN-INDEPENDENCE` | [City Research Hub](city-research-hub.md) |
| Daejeon | `DAEJEON-CITYTOUR`, `DAEJEON-HERITAGE`, `DAEJEON-SCIENCE`, `DAEJEON-DMA` | [City Research Hub](city-research-hub.md) |

## Maintenance rule

When adding a core deal, create its registry record first. Then add its ID to the relevant explanatory page and this index, plus `data/claim-mapping.csv`. Run `python3 scripts/check_claim_coverage.py`; it fails if a core record is orphaned, an ID is invalid, or a mapped page no longer visibly names the ID. This keeps prices/statuses/source confidence from drifting across the repo.

## Status-only / watch records

These records are intentionally kept in the registry so future/expired/rejected claims cannot drift back into ordinary recommendations.

| Registry ID | Current status | Where to read the rule |
| --- | --- | --- |
| `SEOUL-TOUR-TIGERBUS` | Active / live partner check | [City Research Hub](city-research-hub.md) |
| `SEOUL-SALEFESTA` | Future | [Deal Status Board](deal-status-board.md) |
| `DAEJEON-SUMMER50` | Expired for November trip dates | [Deal Status Board](deal-status-board.md) |
| `NATIONWIDE-TWOSOME` | Rejected | [Deal Status Board](deal-status-board.md) |

## Expanded food, payment & airport records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-ASHLEY` | Ashley Queens weekday buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-HKB` | Hong Kong Banjum jjajangmyeon | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-GIMBAP` | Gimbap Cheonguk budget meal | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-BUDGETCOFFEE` | Budget coffee chains | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-HYUNDAI-DESK` | The Hyundai Seoul visitor desk | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `INCHEON-LOUNGE` | Priority Pass lounge access | Live Check | [Arrival Guide](arrival-guide.md) |
| `SEOUL-ASIANA-BOARDING` | Asiana Magic Boarding Pass partners | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-ARISU` | Arisu refill/water savings | Live Check | [Money Guide](money-guide.md) |

## Quality/quantity migration — newly structured records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-ASHLEY` | Ashley Queens weekday buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-HKB` | Hong Kong Banjum jjajangmyeon | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-GIMBAP` | Gimbap Cheonguk budget meal | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-BUDGETCOFFEE` | Budget coffee chains | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-HYUNDAI-DESK` | The Hyundai Seoul visitor desk | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `INCHEON-LOUNGE` | Priority Pass airport lounge access | Live Check | [Arrival Guide](arrival-guide.md) |
| `SEOUL-ASIANA-BOARDING` | Asiana Magic Boarding Pass partners | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-ARISU` | Arisu refill/water savings | Live Check | [Money Guide](money-guide.md) |

## Final narrative-migration & value-score records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-DEPT-CLEARANCE` | Department-store evening clearance | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-STUDENT-FOOD` | University-district local meals | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-MANGWON` | Mangwon Market value food | Live Check | [Everyday Savings](everyday-savings.md) |
| `BUSAN-LOCAL-FOOD` | Busan local meal categories | Live Check | [Busan Guide](busan-guide.md) |
| `INCHEON-AIRPORT-MEAL` | Airport meal voucher/platform listing | Live Check | [Arrival Guide](arrival-guide.md) |
| `NATIONWIDE-PEPERO` | Pepero Day convenience offers | Future | [Trip Calendar](trip-calendar.md) |

## Final city-value expansion records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-DEPT-CLEARANCE` | Department-store evening clearance | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-STUDENT-FOOD` | University-district local meals | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-MANGWON` | Mangwon Market value food | Live Check | [Everyday Savings](everyday-savings.md) |
| `BUSAN-LOCAL-FOOD` | Busan local meal categories | Live Check | [Busan Guide](busan-guide.md) |
| `INCHEON-AIRPORT-MEAL` | Airport meal voucher/platform listing | Live Check | [Arrival Guide](arrival-guide.md) |
| `NATIONWIDE-PEPERO` | Pepero Day convenience offers | Future | [Trip Calendar](trip-calendar.md) |

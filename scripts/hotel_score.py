#!/usr/bin/env python3
"""Rank saved hotel options using the couple's practical 0-5 ratings."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'data'/'hotel-shortlist.csv'
FACTORS=['transit','cheap_food','convenience_coffee','airport_intercity','delivery','attraction_geography','price_value','inflation_risk']

def main() -> int:
 with PATH.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
 if not rows:
  print('No hotel options saved yet. Add real candidates to data/hotel-shortlist.csv.')
  return 0
 scored=[]
 for r in rows:
  try: score=sum(int(r[k]) for k in FACTORS)
  except ValueError:
   print(f"Invalid 0-5 score for {r['hotel']}; fix the CSV."); return 1
  scored.append((score,r))
 print('SCORE  CITY        NEIGHBORHOOD        HOTEL                              COUPLE/NIGHT')
 print('-----  ----------- ------------------- ---------------------------------- -------------')
 for score,r in sorted(scored,reverse=True):
  print(f"{score:>5}  {r['city'][:11]:11} {r['neighborhood'][:19]:19} {r['hotel'][:34]:34} ₩{int(r['couple_price_per_night_krw']):,}")
 print('\nUse this as a discussion aid, not a booking guarantee. Confirm final fees, address, and cancellation terms.')
 return 0
if __name__=='__main__': raise SystemExit(main())

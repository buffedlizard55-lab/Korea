# 🔍 Source Confidence Rules — How the Guide Avoids Fake “Official” Deals

A link being live does not make it official. This project uses a separate source-confidence check so an aggregator, blog, community post, or dead page cannot quietly become the proof for a “confirmed” deal.

> **Last verified: 2026-08-04** · Machine-readable policy: [`data/source-policy.csv`](../data/source-policy.csv)

## Tiers

| Registry tier | Meaning | Allowed use |
| --- | --- | --- |
| `official` | Government, tourism organization, brand, airport, museum, or official pass domain | Can support an Active deal if terms/date still receive a live check. |
| `operator` | Direct operator/booking source tied to an official program | Can support an Active deal, but operator ownership/terms need review. |
| `corroborated` | Credible reporting plus another independent source, but no accessible primary terms | Use with caveats; do not call it official. |
| `secondary` / `community` | Blog, deal guide, forum, social post, or encyclopedia | Lead only. It cannot be the only proof for an Active deal. |

## Automated safeguards

Run:

```bash
python3 scripts/check_source_confidence.py
```

It checks every record in `data/deals.csv` against `data/source-policy.csv` and fails when:

- an aggregator is labeled `official` or `operator`,
- a community/secondary source is labeled `official` or `operator`,
- an Active deal relies only on a secondary/community tier,
- a source tier is unknown.

It also warns when an official/operator domain has not yet been consciously added to the policy file. A warning is a review task—not permission to assume the source is official.

## Human review still required

The linter cannot read terms, distinguish a current from expired banner, or guarantee a branch participates. For every new deal:

1. Open the source and identify the owner.
2. Read the price, dates, eligibility, exclusions, and redemption process.
3. Record a recheck/expiry date and `live_check=yes`.
4. Give the claim the lowest honest tier.
5. Use [Deal Status Board](deal-status-board.md) to show whether it is Active, Live Check, Future, Expired, or Rejected.

**Never upgrade a source just because its design looks professional or a search result calls it official.**

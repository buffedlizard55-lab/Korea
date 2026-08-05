# ⚙️ Verification & Link-Checking Runbook

This guide makes maintenance repeatable without pretending a local network failure means every official site is dead.

> **Last verified: 2026-08-04**

## One reliable local command

Run this before a documentation/deal update:

```bash
python3 scripts/verify_repo.py
```

It runs the checks that work without outside network access:

1. `check_docs.py` — Markdown tables, internal links, and date stamps
2. `check_registry.py` — core deal ID/status/date/source requirements
3. `check_source_confidence.py` — prevents secondary/aggregator pages from being called official
4. `check_staleness.py` — fails overdue Active/Live Check/Future/Candidate records and warns when rechecks are due within 14 days

## External URLs: two ways to verify

### In an environment with working outbound HTTPS

```bash
python3 scripts/verify_repo.py --links
```

That runs `check_links.py` against all external URLs. Bot-blocked hosts are warnings, not automatic failures.

### In this Arena sandbox

The shell’s external TLS requests currently terminate before sites respond. A local link check here will therefore report network failures for every site. Use browser-level web verification for the important claims instead:

- open/read official government, city, airport, pass, brand, or operator page;
- record the terms, access date, and exact caveat in `docs/verification-log.md`;
- classify uncertain or app-only offers as **Live Check** rather than official guaranteed savings.

## Couple budget and branch lock

After hotels are booked, fill the [Hotel Neighborhood Template](hotel-neighborhood-template.md) and save exact options in `data/branch-options.csv`. During the trip, use the [Couple Budget Dashboard](couple-budget.md) instead of rough per-person estimates.

## D-14 trip lock

Fourteen days before the trip, run:

```bash
python3 scripts/trip_lock.py --as-of 2026-10-17
```

It prints only the city-sorted Active / Live Check / Future records that need browser/app confirmation, plus their source and normal backup. Complete that list before buying passes or booking the flexible Cheonan/Daejeon leg.

## Weekly GitHub Actions activation

A weekly workflow exists locally at `.github/workflows/link-check.yml`, but it is deliberately ignored because the repository’s GitHub App has not granted workflow-writing permission.

For exact click-by-click steps, see [Enable GitHub Actions](github-actions-setup.md). To activate it once GitHub permission is available:

1. Grant the connected GitHub App the **`workflows`** permission.
2. Remove the workflow line from `.gitignore`.
3. Add and push the workflow:

   ```bash
   git add .github/workflows/link-check.yml
   git commit -m "ci: enable weekly link check"
   git push origin arena/019fc92e-korea
   ```

4. In GitHub, run it once manually and review warnings before treating any URL as dead.

## What to do when a check reports a problem

| Check result | Correct response |
| --- | --- |
| Internal doc/table issue | Fix the Markdown/reference before pushing. |
| Registry/source-confidence issue | Correct the tier, domain policy, status, date, or source; do not weaken the checker. |
| Link HTTP 404/500 | Verify with a browser. Replace the source or mark the deal retired with date/reason. |
| Link 403/429 | Treat as bot-blocked; verify manually before changing the deal. |
| Whole link run fails with network/TLS errors | Treat as checker-environment unavailable; do not mass-delete sources. |

The goal is a boring maintenance loop: **check → verify → label honestly → log the result**.

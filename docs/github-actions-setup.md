# 🤖 Enable GitHub Actions — Exact Steps

The repository already has a tested workflow template at [`templates/github-actions/link-check.yml`](../templates/github-actions/link-check.yml). It is not automatically pushed into `.github/workflows/` because the connected GitHub App previously rejected workflow changes without the **workflow permission**.

> **Last verified: 2026-08-04** · This requires an owner/admin of the GitHub repository or organization.

## Option A — easiest: add the workflow in GitHub’s website

1. Open the repository: <https://github.com/buffedlizard55-lab/Korea>.
2. Open the **Actions** tab.
3. If GitHub asks, click **“I understand my workflows, go ahead and enable them.”**
4. Click **New workflow** → **set up a workflow yourself**.
5. Name the file exactly:

   ```text
   .github/workflows/link-check.yml
   ```

6. Copy the full contents of [`templates/github-actions/link-check.yml`](../templates/github-actions/link-check.yml) into the editor.
7. Click **Commit changes** directly to `arena/019fc92e-korea` or open a pull request from that branch, depending on repository rules.
8. Return to **Actions**, select **Link and data verification**, and click **Run workflow** once.

## Option B — grant the GitHub App workflow permission

If you manage the GitHub App connected to Arena:

1. In GitHub, open **Settings** for the organization/repository.
2. Open **GitHub Apps** or **Installed GitHub Apps**.
3. Select the App used by Arena.
4. Grant **Workflows: Read and write** permission.
5. Re-authorize/install the App if GitHub asks.
6. Copy the template into `.github/workflows/link-check.yml` and commit it.

## What the workflow does

- Runs on every relevant documentation/data/script push
- Runs every Monday at 00:00 Korea Standard Time
- Can be run manually from the Actions tab
- Validates docs, registry, discovery queue, staleness, claim coverage, and source confidence
- Probes external URLs in GitHub’s network environment, where the Arena sandbox TLS limitation does not apply

## First-run checklist

- [ ] Open the workflow run and review every failure before changing a source.
- [ ] Treat 403/429 results for known bot-blocked sites as warnings, not automatic deletions.
- [ ] If an official link is actually dead, mark the deal expired/rejected or replace it with a current official source.
- [ ] Keep the workflow green by fixing data/status/source issues instead of weakening the checks.

---
type: rule
title: Company size criteria (micro / small)
description: The size thresholds that unlock simplifications and the annual-accounts model.
tags: [company-forms, year-end, bv, belgium, verify-live]
sources: [https://www.nbb.be/en/central-balance-sheet-office, https://www.cbn-cnc.be/nl, https://economie.fgov.be/]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Company size criteria (micro / small)

Most management/freelance BVs are **micro** or **small** companies, which unlocks big simplifications (abridged or micro annual-accounts model, fewer disclosures, usually no audit). Size is judged on the company exceeding **no more than one** of the criteria, assessed on a **two-year consistency basis**.

## Thresholds (last-known, verify_live)

- **Micro company** (uses the micro model): exceeds no more than 1 of , avg **10 FTE**, **EUR 900,000** turnover (excl. VAT), **EUR 450,000** balance-sheet total. [grok/nbb]
- **Small company** (abridged / *verkort* model): exceeds no more than 1 of , avg **50 FTE**, **EUR 11,250,000** turnover, **EUR 6,000,000** balance-sheet total. [grok/nbb]
- **Larger:** the full model, more disclosures, possible audit.

> Thresholds change (the figures above are for financial years from 01/01/2024). **Confirm the current thresholds with the [NBB Central Balance Sheet Office](https://www.nbb.be/en/central-balance-sheet-office)** before relying on a size classification.

## Why it matters

Size drives the [[annual-accounts-nbb|annual-accounts model]] (planned), the disclosure burden, and audit. A one-person management BV is almost always **micro** , the lightest regime , which is what the SparkOS accounting agent assumes by default.

## See also

[[eenmanszaak-vs-vennootschap]] · [[chart-of-accounts-mar]] · [[size-criteria]] (legal source: WVV art. 1:24/1:25)

Source: Grok research synthesis; verify against NBB / CBN / FPS Economy.

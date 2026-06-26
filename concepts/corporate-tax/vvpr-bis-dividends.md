---
type: rule
title: VVPR-bis (reduced withholding tax on dividends)
description: Small companies can pay dividends at 15% withholding (rising to 18% from 1 July 2026) instead of 30%.
tags: [corporate-tax, bv, belgium, verify-live]
sources: [https://financien.belgium.be, https://help.astro.tax/nl]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2026-07-15
---

# VVPR-bis (reduced withholding tax on dividends)

VVPR-bis lets a **small company** distribute dividends to natural-person shareholders at a **reduced withholding tax (roerende voorheffing)** instead of the standard 30%. It is the second half of the salary-vs-dividend optimization for a one-person BV (the first half is the [[corporate-tax-basics|20% corporate rate]]).

## The rule (verify_live)

- **Reduced rate: 15%** (vs the standard 30%). **From 1 July 2026 the reduced rate rises to 18%** , a live reform, confirm the exact figure and date before relying on it. [search]
- **Waiting period:** dividends from the profit distribution of the **3rd financial year** after the contribution qualify for the low rate; an intermediate **20%** rate applies for the 2nd year. [search]

### Conditions [search]

- The company is a **small company** ([[company-size-criteria]]).
- Formed **from 1 July 2013**.
- The shares were issued for a **cash contribution**, fully paid up, and are **not preferential**.
- The shares are **registered to the original shareholders**.

## Related: liquidation reserve

A separate KMO mechanism: book part of taxed profit to a **liquidation reserve** (10% tax up front), then after a 5-year wait distribute at 5% withholding (15% total), or 0% extra at liquidation. Earlier distribution costs 20%. (See planned `liquidation-reserve`.)

## Why it matters

VVPR-bis vs liquidation reserve vs salary is the core payout-planning decision the SparkOS agent models for a profitable BV , interacting with [[corporate-tax-basics]] and [[director-remuneration]].

## See also

[[director-remuneration]] · [[corporate-tax-basics]] · [[company-size-criteria]]

Source: linkup search synthesis; verify against FOD Financiën (rate change effective 1 July 2026).

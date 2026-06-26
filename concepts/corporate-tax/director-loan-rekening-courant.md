---
type: rule
title: Director loan and current account (rekening-courant)
description: Borrowing from your company via the current account; debit balances carry a yearly-set interest.
tags: [corporate-tax, payroll-director, bv, belgium, verify-live]
sources: [https://help.astro.tax/nl/articles/10053338-geld-lenen-van-je-vennootschap-hoe-werkt-dat-precies, https://financien.belgium.be]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Director loan and current account (rekening-courant)

A director can take money out of the company as a loan, either through the **current account (rekening-courant, R/C)** or a **fixed-term loan**. The R/C tracks the running balance of what the director and the company owe each other.

## The rule (verify_live)

- **Positive R/C:** the company owes the director (the director put money in). [astro]
- **Negative / debit R/C:** the director owes the company , this is treated as a loan and **carries interest**. [astro]
- **The interest rate on a debit R/C is set yearly** by the tax authority. Recent reference rates: income year 2022 ~**7.14%**, income year 2023 ~**5.43%** , high and volatile. [astro]
- If the company charges **too little** interest, the shortfall becomes a taxable **benefit in kind** ([[benefits-in-kind-vaa]]) for the director.

> The debit-R/C interest rate changes every year. **Confirm the current rate with [FOD Financiën](https://financien.belgium.be)** before booking interest.

## Why it matters

A debit R/C is a common, easily-overlooked exposure for a one-person BV: drawing cash without booking the (now high) interest creates a VAA and a tax cost. The agent should track the R/C balance and apply the current rate , part of [[director-remuneration|payout planning]].

## See also

[[benefits-in-kind-vaa]] · [[director-remuneration]] · [[corporate-tax-basics]]

Source: Astro Tax help (collaboration source, distilled), FOD Financiën.

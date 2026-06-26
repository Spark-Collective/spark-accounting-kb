---
type: rule
title: Director remuneration (salary vs dividend)
description: How the director is paid and the salary-vs-dividend optimization for a one-person BV.
tags: [payroll-director, corporate-tax, bv, belgium, verify-live]
sources: [https://financien.belgium.be, https://www.rsvz-inasti.fgov.be/]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Director remuneration (salary vs dividend)

How a one-person BV pays its director is the central tax-planning decision. The two channels behave very differently.

## Salary (bedrijfsleidersbezoldiging)

- **Deductible** at the company (reduces the corporate-tax base).
- Taxed in the director's **personal income tax** (progressive) plus [[social-contributions-self-employed|social contributions]].
- Builds social rights (pension). [fod/rsvz]

## Dividend

- **Not deductible** (paid from after-tax profit), but taxed at a **flat withholding** , potentially the reduced [[vvpr-bis-dividends|VVPR-bis]] 15% (rising to 18% from 1 July 2026) instead of 30%.
- Builds no social rights.

## The optimization (verify_live)

- Pay **at least EUR 45,000 director remuneration** to unlock the [[corporate-tax-basics|20% reduced corporate rate]] (or remuneration >= profit if profit is lower; start-ups exempt in early years). The planned rise to EUR 50,000 is not yet in force for 2026 , confirm. [search]
- Beyond that threshold, additional payout is often more efficient as a **dividend** (VVPR-bis) or via a **liquidation reserve** than as more salary, because salary stacks progressive tax + social contributions.

> The EUR 45,000 threshold and the rates change. **Confirm current figures with [FOD Financiën](https://financien.belgium.be) / [RSVZ](https://www.rsvz-inasti.fgov.be/)** before modelling a real year.

## Why it matters

Salary-vs-dividend is the headline number a freelancer leaves an accounting office to optimize , so it is a flagship SparkOS agent calculation, combining [[corporate-tax-basics]], [[vvpr-bis-dividends]], and [[social-contributions-self-employed]].

## See also

[[vvpr-bis-dividends]] · [[corporate-tax-basics]] · [[social-contributions-self-employed]]

Source: linkup search synthesis; verify against FOD Financiën / RSVZ.

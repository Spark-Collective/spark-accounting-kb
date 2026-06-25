---
type: rule
title: Belgian VAT rates and regimes
description: The VAT rates and the small-enterprise exemption; values to verify live.
tags: [vat, belgium, verify-live]
sources: [https://financien.belgium.be]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Belgian VAT rates and regimes

> **verify_live:** the rates and thresholds below are last-known values. **Confirm the current figures with [FOD Financiën](https://financien.belgium.be)** before applying them to a real invoice, booking, or return (see the external-source rules in [`AGENTS.md`](../../AGENTS.md)).

## Rates (last-known)

- **21%** , standard rate, most services (a management/consultancy BV's default).
- **12%** , certain supplies (e.g. some food service / specific goods).
- **6%** , reduced (e.g. certain goods, specific renovation works).
- **0% / exempt** , exports, certain intra-community supplies, and exempt activities (note: exempt is not the same as 0% , no input-VAT deduction).

## Regimes worth knowing

- **Kleine onderneming (small-enterprise exemption):** below an annual turnover threshold, a business can opt out of charging VAT (and cannot deduct input VAT). Confirm the current threshold live.
- **Intracommunautair / medecontractant (reverse charge):** VAT shifts to the customer in defined B2B/cross-border cases; the invoice carries the legal mention and 0% with a reason code.

## Booking

VAT recoverable -> account 411; VAT payable -> account 451 (see [[chart-of-accounts-mar]]). The net position feeds the [[periodic-vat-return-intervat|periodic VAT return]] via the [[vat-period-prep]] workflow.

## See also

[[periodic-vat-return-intervat]] · [[vat-period-prep]] · [[chart-of-accounts-mar]]

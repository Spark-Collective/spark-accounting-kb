---
type: reference
title: Periodic VAT return (Intervat)
description: The periodic BTW return, how it is filed, and the deadlines to verify live.
tags: [vat, intervat, belgium, verify-live]
sources: [https://financien.belgium.be/nl/E-services/Intervat]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Periodic VAT return (Intervat)

A Belgian VAT-registered company files a **periodic VAT return** (monthly or quarterly) via **Intervat** (the FOD Financiën platform), reporting output VAT, input VAT, and the net to pay or reclaim.

## Key facts (verify_live)

- **Frequency:** quarterly is common for a small BV; monthly above a turnover threshold or by option. Confirm the current threshold/deadlines live.
- **Deadlines:** the return + payment are due by a fixed day of the month following the period. **Verify the exact current dates with [FOD Financiën](https://financien.belgium.be)** , do not rely on a remembered date.
- **Channel:** Intervat XML upload, or the **Intervat API** (Spark requested API access; see the workspace note `deployments/sparkos-erpnext/intervat-api-access.md`).
- Related periodic obligations: the **EC sales list** (intracommunautaire opgave) and the **annual client listing** (klantenlisting).

## How the agent prepares it

Per the [[vat-period-prep]] workflow: compile the figures from the VAT accounts (411/451, see [[chart-of-accounts-mar]]), validate, and present for approval. **Never auto-file** , a real submission is verified against FOD and human-approved.

## See also

[[vat-period-prep]] · [[vat-rates-and-regimes]]

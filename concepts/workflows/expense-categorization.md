---
type: workflow
title: Expense categorization
description: Route each cost to the right account, deductibility rule, and VAT treatment.
tags: [workflows, deductible-costs, vat, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Workflow: expense categorization

The judgment step inside [[booking-a-purchase-invoice]]: given a cost, decide the account, the income-tax deductibility, and the VAT treatment , applying the rule pages rather than guessing.

## Steps

1. **Identify the nature** of the cost and map it to a class-6 account ([[chart-of-accounts-mar]]).
2. **Apply the income-tax deductibility rule** from the matching page:
   - [[restaurant-and-meals]] (~69%), [[car-and-mobility]] (CO2-based), [[ict-equipment]] (100%), [[sponsoring]] (100%/50%), [[streaming-subscriptions]] / [[reading-glasses]] / [[international-passport]] (professional-character test).
   - Record the **non-deductible fraction** for the year-end add-back; book the full cost.
3. **Set the VAT treatment** per [[vat-deduction-conditions]] (professional use, correct invoice, right to deduct) and any cap (restaurant none, car/ICT capped).
4. **Flag a benefit in kind** ([[benefits-in-kind-vaa]]) where there is private use (car, phone, ICT).
5. **Flag the uncertain ones** (dual-use, weak professional link) for operator review.

## Gate

- Each expense has: an account, an income-tax deductibility %, and a VAT treatment.
- **Borderline deductibility is flagged, never silently maximised.**

## See also

[[booking-a-purchase-invoice]] · [[vat-deduction-conditions]] · [[benefits-in-kind-vaa]]

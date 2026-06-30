---
type: workflow
title: Intake (scope + onboarding)
description: "The first step before any booking: scope the engagement, gather facts, decide what is in scope vs hand off."
tags: [workflows, belgium]
relations:
  part_of: [classification-protocol]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Intake (scope + onboarding)

Runs **before** any classification. It scopes the work, confirms the operator's situation, and decides whether the case is in scope or should go to a human accountant. Pairs with the [[classification-protocol]].

## Open with the boundary

State it first: *"I prepare your accounting and tax working papers for your accountant to review , I never file anything. A few questions so I can help."* (the prepare-never-file rule.)

## Scope questions (ask as one batch)

1. Belgian resident / established for the full year?
2. Business form , [[eenmanszaak-vs-vennootschap|eenmanszaak or a BV]]?
3. VAT regime , standard, the small-enterprise exemption ([[vat-rates-and-regimes]]), or none?
4. Employees? How many?
5. Sector / activity?
6. Bookkeeping basis , accrual (a BV must) or simplified?
7. What's needed , month-end, VAT return, payout planning, year-end + filing, setup?

## Refusal catalogue (hand off to a human accountant)

Stop and route to a professional when the case is out of the agent's scope:

- **Groups / consolidation / subsidiaries** , beyond a single-person BV.
- **Non-resident** or part-year situations.
- **Special VAT regimes** , margin scheme, partial exemption, VAT unit (only the standard regime is in scope).
- **Pending / low-confidence rules** the operator wants to act on now , e.g. the not-yet-voted [[liquidation-reserve]] reform or [[capital-gains-tax-on-shares]] (flag, don't decide).
- Anything that needs **professional sign-off beyond a review**, or where source documents are missing.

## Then

Accept whatever documents the operator has (bank statements, sales/purchase invoices, prior returns , PDF/CSV/image). Infer the rest, route to the right workflow ([[month-end-close]], [[vat-period-prep]], [[year-end-close]]), and run the [[classification-protocol]].

## See also

[[classification-protocol]] · [[month-end-close]] · [[year-end-close]]

Note: onboarding/refusal pattern re-authored (clean-room), inspired by OpenAccountants' intake; see docs/architecture/accounting-kb-vs-openaccountants.md.

---
type: workflow
title: Prepare a periodic VAT return for review
description: The SOP the agent runs to compile a VAT return; prepare, never file.
tags: [workflows, vat, intervat, belgium]
sources: [https://financien.belgium.be/nl/E-services/Intervat]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Workflow: prepare a periodic VAT return for review

The agent **prepares** the [[periodic-vat-return-intervat|periodic VAT return]] and presents it for approval. It does **not** file , a real submission is human-approved and verified against FOD (prepare-never-send).

## Steps

1. **Scope the period.** Determine the period (quarter/month) and its filing deadline , **verify the current deadline live** ([[periodic-vat-return-intervat]] is `verify_live`).
2. **Reconcile first.** Ensure all sales and purchase invoices for the period are booked and the bank is reconciled (the [[chart-of-accounts-mar|VAT accounts]] 411/451 must be complete). Flag anything unbooked.
3. **Compile the figures.** Sum output VAT (451) and input VAT (411) by rate; compute the net to pay or reclaim. Map to the Intervat return grid boxes.
4. **Sanity checks.** Compare to the prior period; flag big swings, missing-VAT-number invoices, reverse-charge (medecontractant) entries, and intra-community transactions (these also feed the EC sales list).
5. **Verify rates/rules** against [[vat-rates-and-regimes]] , and re-confirm any changeable figure with [FOD Financiën](https://financien.belgium.be).
6. **Present for approval.** Produce a short summary (period, boxes, net, flags) for the operator. Generate the Intervat XML only after approval.
7. **Record.** Log what was prepared; route the artifact to its store. Any recurring issue -> update the relevant KB page.

## Guardrails

- **Never auto-file.** Outbound to the tax authority needs explicit approval and a live verification against FOD.
- If figures don't reconcile, **stop and escalate** , do not file an unbalanced return.

## See also

[[periodic-vat-return-intervat]] · [[vat-rates-and-regimes]] · [[chart-of-accounts-mar]]

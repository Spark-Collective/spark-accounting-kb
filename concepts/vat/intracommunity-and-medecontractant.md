---
type: rule
title: Reverse charge (medecontractant + intracommunity)
description: When VAT shifts to the customer, the 0% invoice, and the mandatory legal mentions.
tags: [vat, bv, belgium, verify-live]
relations:
  affects: [ec-sales-list, vat-return-grilles]
sources: [https://financien.belgium.be]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# Reverse charge (medecontractant + intracommunity)

In defined B2B cases the supplier charges **0% VAT** and the **customer self-accounts** for the VAT (verlegging van heffing). The invoice must carry the correct legal mention , this is a frequent source of errors.

## Domestic: medecontractant (mainly construction) [search]

- Applies to **work on immovable property** used (partly) professionally, **between two Belgian VAT payers** who file periodic returns.
- The supplier invoices **0% VAT**; the customer declares the VAT in their own return (grids 81/82/83/87/88 depending on the case).
- **Mandatory mention since 1 January 2023:** *"Verlegging van heffing , Belasting te voldoen door de medecontractant, art. 20 KB nr. 1"* (replaces the old "btw verlegd").
- Does **not** apply to VAT-exempt customers or private individuals.

## Cross-border: intracommunity [search]

- **Services to a VAT-payer in another EU country:** VAT shifts to the customer. Mention *"Btw verlegd: Art. 21 par. 2 van het Belgische btw-wetboek"*.
- **Goods to a VAT-payer in another EU country:** intracommunity supply, mention *"Btw verlegd: Art. 39bis , intracommunautaire levering"*.
- 0% on the invoice; these feed the **EC sales list** (intracommunautaire opgave).

> Verify the exact article references and grid numbers with [FOD Financiën](https://financien.belgium.be); always check the customer's VAT number is valid (VIES) before applying 0%.

## See also

[[vat-rates-and-regimes]] · [[periodic-vat-return-intervat]] · [[vat-period-prep]]

Source: linkup search synthesis; verify against FOD Financiën.

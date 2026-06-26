---
type: reference
title: VAT return grilles (the boxes)
description: The boxes of the Belgian periodic VAT return, grouped; what each one captures.
tags: [vat, intervat, belgium, verify-live]
relations:
  part_of: [periodic-vat-return-intervat]
sources: [https://financien.belgium.be/nl/E-services/Intervat]
confidence: medium
created: 2026-06-26
updated: 2026-06-26
verify_live: true
review_after: 2027-01-31
---

# VAT return grilles (the boxes)

The structured boxes (roosters/grilles) of the Belgian periodic VAT return. The [[vat-period-prep]] workflow maps the books to these; [[ec-sales-list]] and the [[annual-client-listing]] are filed separately.

## Outgoing operations (uitgaande handelingen)

| Box | Captures |
|---|---|
| 00 | Sales at 0% / non-taxable |
| 01 | Sales base at 6% |
| 02 | Sales base at 12% |
| 03 | Sales base at 21% |
| 44 | Intra-EU services provided (base) |
| 45 | Operations with reverse charge to a Belgian co-contractor (base) |
| 46 | Intra-EU supplies of goods + triangular (base, 0%) |
| 47 | Other exempt operations / co-contractor |
| 48 | Credit notes issued (re intra-EU) |
| 49 | Other credit notes / corrections |

## Incoming operations (inkomende handelingen)

| Box | Captures |
|---|---|
| 81 | Purchases of goods, raw materials, consumables (base) |
| 82 | Purchases of services and diverse goods (base) |
| 83 | Purchases of capital goods / investments (base) |
| 84 / 85 | Credit notes received / corrections |
| 86 | Intra-EU acquisitions (base) |
| 87 | Other incoming (imports, co-contractor) (base) |

## VAT amounts + balance

| Box | Captures |
|---|---|
| 54 | Output VAT due on boxes 01/02/03 |
| 55 | Output VAT on intra-EU acquisitions / reverse charge |
| 56 | Output VAT on co-contractor operations |
| 59 | **Deductible** input VAT |
| 71 | Net **to pay** to the State |
| 72 | Net **refundable** by the State |

> **verify_live + 2025 changes:** from 2025, the VAT current account became a **provisierekening**, refund rules (box 72) changed, and the **quarterly deadline moved to the 25th** of the month after the period (monthly filers keep ~the 20th). **Confirm the current boxes, rates, and deadlines with [FOD Financiën](https://financien.belgium.be)** before filing.

## See also

[[vat-period-prep]] · [[periodic-vat-return-intervat]] · [[intracommunity-and-medecontractant]]

Source: FOD Financiën periodic VAT return (Intervat); box meanings distilled. Verify against the current form.

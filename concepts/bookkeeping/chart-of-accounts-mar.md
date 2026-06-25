---
type: reference
title: Belgian chart of accounts (MAR / PCMN)
description: The legally standardized minimum chart every Belgian double-entry bookkeeping uses, classes 0-7.
tags: [bookkeeping, bv, belgium]
sources: [https://www.cbn-cnc.be/nl, https://financien.belgium.be]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Belgian chart of accounts (MAR / PCMN)

A Belgian company keeping [[eenmanszaak-vs-vennootschap|double-entry books]] must use the standardized **Minimum Genormaliseerd Rekeningstelsel (MAR)** / **Plan Comptable Minimum Normalisé (PCMN)**, set by Royal Decree. The structure is fixed; a small management BV instantiates only the slice it uses.

| Class | NL | What | ERPNext root type |
|---|---|---|---|
| 1 | Eigen vermogen, voorzieningen, schulden >1j | Capital, reserves, retained earnings, provisions, long-term debt | Equity + Liability |
| 2 | Vaste activa | Intangible / tangible / financial fixed assets, depreciation | Asset |
| 3 | Voorraden | Inventory, work in progress | Asset |
| 4 | Vorderingen & schulden <=1j | Trade debtors (40), creditors (44), VAT (411 recoverable / 451 payable), taxes & social (45), current accounts (48/49) | Asset + Liability |
| 5 | Geldbeleggingen & liquide middelen | Bank (550), cash (570) | Asset |
| 6 | Kosten | Goods/services (60-61), remuneration (62), depreciation (630), financial (65), taxes (67) | Expense |
| 7 | Opbrengsten | Turnover/sales (70), other operating (74), financial income (75) | Income |
| 0 | Rechten & verplichtingen buiten balans | Off-balance commitments | (memo) |

## Practice notes

- A one-person consultancy/management BV uses mostly classes 4, 5, 6, 7 plus equity (1) and a little fixed-asset (2); class 3 (inventory) is usually unused.
- The **VAT accounts** (411 te recupereren btw / 451 verschuldigde btw) are central to the [[vat-period-prep]] workflow.
- Account *numbers* are standardized; the firm's specific sub-accounts come from the existing books , import the real chart rather than rebuilding it generically.

## See also

[[eenmanszaak-vs-vennootschap]] · [[vat-rates-and-regimes]] · [[vat-period-prep]]

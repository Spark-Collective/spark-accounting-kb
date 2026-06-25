---
type: concept
title: Eenmanszaak vs vennootschap (BV)
description: The two business forms and what each means for bookkeeping and tax.
tags: [company-forms, belgium]
sources: [https://www.itaa.be, https://financien.belgium.be, https://www.cbn-cnc.be/nl]
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Eenmanszaak vs vennootschap (BV)

The business form drives the accounting obligations , this is the first fork.

## Eenmanszaak (sole trader, natural person)

- May keep **simplified (single-entry)** bookkeeping below the turnover threshold: a purchases book, a sales book, a financial book.
- Taxed in **personal income tax** (personenbelasting), progressive rates.
- No annual accounts to file at the NBB.
- Fits the polished freelancer SaaS (Accountable, Dexxter); a Spark agent for this case is lighter.

## Vennootschap (company, BV / SRL)

- **Must** keep **double-entry** bookkeeping on the [[chart-of-accounts-mar|MAR/PCMN chart]] , record assets, liabilities, depreciation, reserves, provisions.
- Taxed in **corporate tax** (vennootschapsbelasting); the director draws remuneration.
- **Must file annual accounts** at the NBB each year (micro/abbreviated scheme for a small company).
- This is Spark's target case: the agent must handle real double-entry + statutory filing.

## Why it matters for the agent

The freelancer tools stop at eenmanszaak simplified accounting; a BV needs double-entry + annual accounts, which is exactly the gap the SparkOS accounting agent fills. Everything in [[bookkeeping]] and [[year-end]] assumes a **BV** unless tagged `eenmanszaak`.

## See also

[[chart-of-accounts-mar]] · [[vat-rates-and-regimes]]

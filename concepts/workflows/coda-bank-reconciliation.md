---
type: workflow
title: CODA bank reconciliation
description: Import the bank's CODA file, match each line to the books, and tie the bank balance.
tags: [workflows, bookkeeping, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Workflow: CODA bank reconciliation

**CODA** (gecodeerd dagafschrift) is the Belgian standardized electronic bank-statement format. Banks deliver CODA files; the agent imports them and reconciles every line so the books match reality , the backbone of [[month-end-close]].

## Steps

1. **Import the CODA** file into the books for the period.
2. **Auto-match** each transaction:
   - **Customer payment** -> clear the open debtor (40), matched by amount and the **structured communication (OGM/mededeling)** or invoice reference.
   - **Supplier payment** -> clear the open creditor (44), link to the [[booking-a-purchase-invoice|booked invoice]].
3. **Book the non-invoice lines** to the right account ([[chart-of-accounts-mar]]): bank charges (65), VAT payments to the authority (451), taxes, salary/social, transfers.
4. **Flag unmatched / unknown** transactions for review rather than forcing them.
5. **Tie the balance** , the ledger bank account (550) must equal the statement's closing balance.

## Gate

- **Every line is matched or booked**, and the **ledger bank balance equals the real statement balance**.
- Unrecognised transactions are surfaced, not parked in a suspense account silently.

## See also

[[month-end-close]] · [[booking-a-purchase-invoice]] · [[chart-of-accounts-mar]]

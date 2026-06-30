---
type: reference
title: Classification protocol (how the agent behaves under uncertainty)
description: "The decision discipline applied across every booking/tax workflow: conservative defaults + Classified/Assumed/Needs-Input."
tags: [workflows, bookkeeping, belgium]
sources: []
confidence: high
created: 2026-06-26
updated: 2026-06-26
verify_live: false
review_after: 2027-06-26
---

# Classification protocol

The behavioural contract the agent follows in every workflow ([[booking-a-purchase-invoice]], [[expense-categorization]], [[vat-period-prep]], [[year-end-close]]). It governs **what to do when the documents don't fully answer the question** , the difference between a useful working paper and a guess.

## Conservative defaults

When uncertain about any treatment, choose the option that **costs more or imposes stricter compliance**, never less. A reviewer can relax an over-conservative position; they cannot easily recover from an aggressive one that was already filed. (Aligns with the prepare-never-file rule.)

## One of three outcomes per item

Every transaction or data point gets exactly one:

- **Classified** , the documents carry enough to apply the rule. No flag.
- **Assumed** , a fact is missing, so a conservative default is applied **and disclosed**: state the exact assumption and its cash/compliance impact.
- **Needs input** , cannot proceed without the operator. Ask **one targeted question**, then classify.

## Execution rules

- **Cite the rule/source** for every rate, threshold, or code (and apply `verify_live` , fetch the current value for any changeable figure).
- **Never invent a code or a rate.** Use only accounts from [[pcmn-account-codes]] and figures from a cited source.
- **Group related assumptions** ("5 entertainment items blocked, total EUR 340") rather than flagging each.
- **Don't re-ask** what the documents already answer. Process all data before producing output.
- When several domains apply (a payroll item that also hits income tax), address both.

## Output discipline

Produce, as relevant: a **working paper** (item-by-item classification with account/box assignments), a **reviewer brief** (every position cited, every assumption disclosed, flags ranked by cash impact), and an **action list** (what to pay/file, when). The operator/accountant signs off; the agent never files.

## See also

[[booking-a-purchase-invoice]] · [[expense-categorization]] · [[vat-period-prep]]

Note: methodology re-authored (clean-room), inspired by OpenAccountants' "classification contract"; see docs/architecture/accounting-kb-vs-openaccountants.md.

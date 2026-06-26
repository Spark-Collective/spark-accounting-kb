# Index , spark-accounting-kb

> Read this first. Navigation + progressive disclosure for the accounting knowledge graph. For the protocol (frontmatter, wikilinks, external-source rules), see [`AGENTS.md`](AGENTS.md).

Last updated: 2026-06-26

## Concepts by topic

### company-forms/
- [[eenmanszaak-vs-vennootschap]] , sole trader vs company (BV/SRL); when to incorporate.
- [[company-size-criteria]] , micro/small thresholds -> simplifications + annual-accounts model (verify_live).

### bookkeeping/
- [[chart-of-accounts-mar]] , the Belgian standardized chart (MAR / PCMN), classes 0-7.
- [[pcmn-account-codes]] , the common sub-account codes a management BV posts to.
- [[double-entry-basics]] , debit/credit, journals + ledger, balance sheet vs P&L.
- [[document-retention]] , keep books/invoices 10 years (15-25 for real estate) (verify_live).
- _planned: journals_

### vat/
- [[vat-rates-and-regimes]] , VAT rates, the small-enterprise exemption, special regimes (verify_live).
- [[vat-deduction-conditions]] , when input VAT is recoverable (professional, correct invoice, right to deduct).
- [[periodic-vat-return-intervat]] , the periodic BTW return + how it is filed.
- [[vat-return-grilles]] , the return boxes 00-91, grouped (verify_live; 2025 deadline/provisierekening changes).
- [[intracommunity-and-medecontractant]] , reverse charge: 0% invoice + mandatory mentions (verify_live).
- [[peppol-e-invoicing]] , structured B2B e-invoicing mandatory from 2026 (verify_live).
- [[annual-client-listing]] , yearly list of Belgian VAT customers over EUR 250, due 31 Mar (verify_live).
- [[ec-sales-list]] , periodic intracommunity listing, due the 20th (verify_live).

### deductible-costs/
- [[car-and-mobility]] , deductibility of car/mobility costs (verify_live).
- [[restaurant-and-meals]] , restaurant ~69%, business lunch, VAT not deductible (verify_live).
- [[ict-equipment]] , iPad/tablet/laptop 100%, VAT ~75%, VAA (verify_live).
- [[sponsoring]] , 100% for publicity, 50% for benefits (representation) (verify_live).
- [[streaming-subscriptions]] , Spotify etc. only if genuinely professional (verify_live).
- [[reading-glasses]] , up to 50%, dual-use scrutiny (verify_live).
- [[international-passport]] , deductible for genuine business travel, with proof.
- [[fines]] , traffic/other fines paid by the company but never deductible.
- [[gifts-relatiegeschenk]] , business gifts 50%; VAT one gift/client/year under EUR 50 (verify_live).
- [[hybrid-car-rules-2026]] , hybrids ordered from 2026 no longer deductible in the company (verify_live).
- [[training-costs]] , training deductible + KMO-portefeuille subsidy (Flanders) (verify_live).
- [[ev-charging-reimbursement]] , reimburse EV home-charging at actual cost or per-kWh forfait (verify_live).
- [[toll-peage]] , toll/peage is a company cost; private trips via the car VAA.
- [[home-office]] , tax-free home-office allowance ~EUR 161/month (verify_live).
- [[kilometer-allowance]] , tax-free per-km allowance for own-car business trips (verify_live).
- [[clothing]] , only specific professional clothing is deductible; ordinary clothing is not.

### corporate-tax/
- [[corporate-tax-basics]] , 25% standard, 20% on first EUR 100k for small companies + conditions (verify_live).
- [[advance-payments]] , quarterly prepayment to avoid the surcharge (verify_live).
- [[vvpr-bis-dividends]] , reduced dividend withholding 15% (18% from 1 Jul 2026) + conditions (verify_live).
- [[director-loan-rekening-courant]] , borrowing from the company; debit-R/C interest (verify_live).
- [[liquidation-reserve]] , KMO payout mechanism; 2025 reform (shorter wait) pending (verify_live).
- [[investment-deduction]] , deduct part of qualifying investments; reformed from 2025 (verify_live).
- [[capital-gains-tax-on-shares]] , new ~10% solidarity contribution; large-vs-small participation (verify_live).
- _planned: dbi-deduction, notional-interest_

### payroll-director/
- [[social-contributions-self-employed]] , RSVZ social contributions for self-employed/director (verify_live).
- [[director-remuneration]] , salary vs dividend; the EUR 45k threshold (verify_live).
- [[benefits-in-kind-vaa]] , VAA on car/housing/phone/internet; valuation + forfaits (verify_live).
- [[per-diem-domestic-travel]] , tax-free meal allowance for Belgian business trips (verify_live).
- [[withholding-on-director-pay]] , bedrijfsvoorheffing withheld + remitted on director salary (verify_live).

### year-end/
- [[annual-accounts-nbb]] , filing model, 7-month deadline, XBRL, 2026 fees (verify_live).
- [[depreciation]] , how to book depreciation; book-vs-tax (grounded by [[depreciation-advies]]).
- [[provisions]] , booking provisions for risks and charges (16x / 635-637 / 762).
- [[closing-entries]] , the year-end entry sequence (depreciation, provisions, cut-off, tax).

### workflows/ (SOPs the agent runs)
- [[intake]] , scope + onboarding + refusal catalogue (runs first).
- [[vat-period-prep]] , prepare a periodic VAT return for review (never auto-file).
- [[booking-a-purchase-invoice]] , capture, split VAT, classify deductibility, book.
- [[month-end-close]] , monthly routine to get the books complete + reconciled.
- [[coda-bank-reconciliation]] , import the CODA file, match lines, tie the bank balance.
- [[expense-categorization]] , route a cost to account + deductibility + VAT treatment.
- [[classification-protocol]] , behaviour under uncertainty: conservative defaults + Classified/Assumed/Needs-Input.
- [[year-end-close]] , close the year, compute tax, file the annual accounts + return.

## references/cbn-adviezen/ (PHASE 2 , authoritative grounding)

Distilled CBN/CNC adviezen that ground the practice pages (citation substrate, not a replacement). See the PHASE 2 note in the loop charter.
- [[depreciation-advies]] , CBN principles for depreciating fixed assets (linear/degressive, economic life).
- [[provisions-advies]] , CBN principles for provisions for risks and charges (prudence; art. 33 KB W.Venn.).
- [[distribution-test-advies]] , the WVV net-asset + liquidity tests a BV must pass before any payout.
- [[valuation-rules-advies]] , going concern, acquisition value, consistency, prudence (the valuation frame).
- [[size-criteria-advies]] , the legal source of small/micro thresholds (WVV art. 1:24/1:25) (verify_live).
- [[impairments-advies]] , CBN principles for impairments on receivables/inventory (booking + reversal).
- [[formation-costs-advies]] , capitalizing/amortizing formation costs (rubric 20, min 20%/yr).

## Reserved files

- [`taxonomy.md`](taxonomy.md) , controlled tags.
- [`sources.md`](sources.md) , authoritative external sources + when to consult.
- [`log.md`](log.md) , changelog.
- [`tools/graph.py`](tools/graph.py) , query + validate the typed-edge graph (the `relations:` layer; see AGENTS.md). `python3 tools/graph.py --node <name>` shows a concept's inbound/outbound edges; `--validate` checks integrity.

## How to grow it

Add the topic the next real bookkeeping needs, prove it on Spark's own books, then widen. Each new page: frontmatter + >=2 wikilinks + a `log.md` line. Mark changeable facts `verify_live: true`.

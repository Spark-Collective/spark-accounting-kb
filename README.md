# spark-accounting-kb

Belgian-accounting **knowledge graph** for Spark's accounting / booking agents. Distilled practice for **single-person BV (management companies) and freelancers**, in the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) / llm-wiki pattern: markdown files, YAML frontmatter, `[[wikilinks]]`, git-versioned, no SDK.

**Design principle:** the KB holds the **stable practice** (how to book, decide, file); precise/changing facts (rates, thresholds, deadlines) are **fetched live** from authoritative sources at use time. See [`AGENTS.md`](AGENTS.md) for the protocol and the **when-to-check-external-sources** rules.

## Start here

- [`AGENTS.md`](AGENTS.md) , the protocol (structure, frontmatter, wikilinks, external-source policy).
- [`index.md`](index.md) , navigation: all concepts + workflows by topic.
- [`sources.md`](sources.md) , authoritative external sources and when to consult each.
- [`taxonomy.md`](taxonomy.md) , the controlled tag vocabulary.

## What this is not

- Not the law. It is *practice*, grounded in and citing the law/sources.
- Not a copy of any third party's content (e.g. astro.tax). Own words, own grounding.
- Not a place for precise live facts , those are fetched on demand (see the protocol).

Design rationale and how it fits SparkOS: the Spark workspace note `docs/architecture/accounting-agent-knowledge-base.md`.

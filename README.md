# accounting-knowledge-graph

An open, agent-readable **knowledge graph of accounting practice** , **currently Belgium** (the structure extends to other jurisdictions) , for **single-person BVs (management companies) and freelancers**, in the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) / llm-wiki pattern: markdown files, YAML frontmatter, `[[wikilinks]]`, typed `relations:` edges, git-versioned, no SDK or database.

> Maintained by [Spark Collective](https://github.com/Spark-Collective). Contributions welcome from anyone.

> **Disclaimer , read this.** This is a general reference for preparing working papers, **not** tax, legal, or accounting advice. Everything produced from it must be reviewed and signed off by a qualified professional (comptable / accountant / belastingadviseur) before filing or acting on it. Rates and rules change , see the freshness rule below.

**Design principle:** the KB holds the **stable practice** (how to book, decide, file). Precise, changing facts (rates, thresholds, deadlines) are **not stored as fact** , they are flagged `verify_live: true` and fetched from the authority at use time. *Read the KB for the method; fetch the source for the number.*

## For AI agents

Start at [`AGENTS.md`](AGENTS.md) , the full protocol: structure, frontmatter, retrieval, the **when-to-check-external-sources** policy, and the typed-edge (`relations:`) layer. Then read [`index.md`](index.md) to navigate.

## For people

- [`index.md`](index.md) , navigation: every concept + workflow by topic.
- [`sources.md`](sources.md) , the authoritative sources (FOD Financiën, CBN/CNC, NBB, RSVZ) and when to consult each.
- [`taxonomy.md`](taxonomy.md) , the controlled tag vocabulary.

## It's a graph, not just a wiki

Concepts are atomic and joined by **typed, directed edges** (`unlocks`, `requires`, `gates`, `grounded_by`, `affects`, `alternative_to`, `part_of`) , so an agent can *traverse* relationships, not just read pages. Query and validate with the zero-dependency tool:

```bash
python3 tools/graph.py --node director-remuneration   # a concept's inbound/outbound edges
python3 tools/graph.py --lint                          # every page: required frontmatter + >=2 wikilinks
python3 tools/graph.py --validate                      # typed edges resolve + predicates in vocab
```

CI runs `--lint` and `--validate` on every PR.

### Visualize it

This KB follows the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (OKF), so it is interoperable with OKF tooling and markdown UIs (Obsidian, MkDocs). Generate a self-contained interactive graph viewer (Cytoscape, no server) , it renders our **typed** edges, labelled and coloured by predicate, with click-to-read:

```bash
python3 tools/build_viz.py   # writes viz.html , open it in any browser
```

The viewer pattern follows Google's OKF reference viewer (Apache-2.0); ours is fed by our richer typed `relations:` graph.

## Contributing

Contributions welcome , see [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version: one concept per file, **distil don't paste**, primary-source the facts, mark changeable facts `verify_live`, link with `[[wikilinks]]`, run the validators, open a small PR.

## What this is not

- Not the law , it is *practice*, grounded in and citing the law/sources.
- Not a copy of anyone's content , own words, own grounding (facts aren't copyrightable; phrasing is).
- Not a store of precise live facts , those are fetched on demand.

## License

[Apache License 2.0](LICENSE), Copyright Spark Collective BV. Free to use, modify, and redistribute (including commercially) with attribution and the license notice.

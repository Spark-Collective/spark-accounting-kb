#!/usr/bin/env python3
"""Query + validate the typed-edge graph (the `relations:` frontmatter).

Usage:
  python3 tools/graph.py                 # summary (nodes, edges, by predicate)
  python3 tools/graph.py --node NAME     # outbound + inbound edges for a node
  python3 tools/graph.py --validate      # dangling targets + unknown predicates (exit 1 on error)
  python3 tools/graph.py --dot           # graphviz DOT of the typed edges

Wikilinks are for reading; `relations:` is the machine-traversable layer. See AGENTS.md.
"""
import os, re, sys, argparse, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["concepts", "references"]
VOCAB = {"requires", "unlocks", "gates", "grounded_by", "affects", "alternative_to", "part_of"}
REPO_URL = "https://github.com/Spark-Collective/accounting-knowledge-graph"
BRANCH = "main"
REQUIRED_FM = {"type", "title", "description", "tags", "sources", "confidence",
               "created", "updated", "verify_live", "review_after"}

def md_files():
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                if f.endswith(".md"):
                    yield os.path.join(dirpath, f)

def parse(path):
    """Return (basename, {predicate: [targets]}) from a file's frontmatter."""
    name = os.path.basename(path)[:-3]
    rels = {}
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return name, rels
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
    fm = lines[1:end]
    in_rel = False
    for ln in fm:
        if re.match(r"^relations:\s*$", ln):
            in_rel = True; continue
        if in_rel:
            m = re.match(r"^\s+(\w+):\s*\[(.*)\]\s*$", ln)
            if m:
                rels[m.group(1)] = [t.strip() for t in m.group(2).split(",") if t.strip()]
            elif re.match(r"^\S", ln):   # next top-level key ends the block
                in_rel = False
    return name, rels

def build():
    nodes, edges = set(), []
    for p in md_files():
        n, rels = parse(p)
        nodes.add(n)
        for pred, targets in rels.items():
            for t in targets:
                edges.append((n, pred, t))
    return nodes, edges

def cmd_summary(nodes, edges):
    by = {}
    for _, p, _ in edges:
        by[p] = by.get(p, 0) + 1
    sourced = len({s for s, _, _ in edges})
    print(f"nodes: {len(nodes)}  |  nodes with relations: {sourced}  |  typed edges: {len(edges)}")
    for p in sorted(by, key=lambda k: -by[k]):
        print(f"  {p:<14} {by[p]}")

def cmd_node(nodes, edges, name):
    out = [(p, t) for s, p, t in edges if s == name]
    inb = [(s, p) for s, p, t in edges if t == name]
    if name not in nodes:
        print(f"warning: '{name}' is not a known page");
    print(f"# {name}")
    print("outbound:")
    for p, t in out: print(f"  --{p}--> {t}")
    if not out: print("  (none)")
    print("inbound:")
    for s, p in inb: print(f"  {s} --{p}-->")
    if not inb: print("  (none)")

def cmd_validate(nodes, edges):
    errs = []
    for s, p, t in edges:
        if p not in VOCAB:
            errs.append(f"unknown predicate '{p}' on {s} -> {t}")
        if t not in nodes:
            errs.append(f"dangling target: {s} --{p}--> {t} (no such page)")
    if errs:
        print("VALIDATION FAILED:")
        for e in errs: print(f"  {e}")
        return 1
    print(f"OK , {len(edges)} edges, all targets resolve, all predicates in vocab.")
    return 0

def cmd_dot(edges):
    print("digraph accounting_kb {")
    print('  rankdir=LR; node [shape=box, style=rounded];')
    for s, p, t in edges:
        print(f'  "{s}" -> "{t}" [label="{p}"];')
    print("}")

def cmd_lint():
    """Check every concept/reference page has the required frontmatter + >=2 wikilinks."""
    errs = []
    for p in md_files():
        rel = os.path.relpath(p, ROOT)
        with open(p, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        if not lines or lines[0].strip() != "---":
            errs.append(f"{rel}: no frontmatter"); continue
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
        keys = {m.group(1) for ln in lines[1:end] if (m := re.match(r"^([A-Za-z_]+):", ln))}
        missing = REQUIRED_FM - keys
        if missing:
            errs.append(f"{rel}: missing frontmatter {sorted(missing)}")
        if "\n".join(lines[end + 1:]).count("[[") < 2:
            errs.append(f"{rel}: fewer than 2 [[wikilinks]]")
    if errs:
        print("LINT FAILED:")
        for e in errs: print(f"  {e}")
        return 1
    print(f"OK , all pages have the required frontmatter and >=2 wikilinks.")
    return 0

# --- JSON + interactive viewer export -------------------------------------

def _frontmatter(path):
    """Flat scalar frontmatter dict for a page."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    fm = {}
    if not lines or lines[0].strip() != "---":
        return fm
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
    for ln in lines[1:end]:
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", ln)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm

def _category(path):
    parts = os.path.relpath(path, ROOT).split(os.sep)
    if parts[0] == "concepts" and len(parts) >= 3:
        return parts[1]
    if parts[0] == "references":
        return "references"
    return parts[0]

def _wikilinks(path):
    """Body [[wikilink]] targets (the human reading layer)."""
    name = os.path.basename(path)[:-3]
    with open(path, encoding="utf-8") as fh:
        body = fh.read()
    return name, {m.group(1).strip() for m in re.finditer(r"\[\[([^\]|#]+)", body)
                  if m.group(1).strip() and m.group(1).strip() != name}

def build_graph_json():
    """Nodes (with category/title/meta) + links: typed edges (relations:) AND
    wikilink edges. Both layers, so a viewer can show the reading layer plus the
    typed layer agents traverse."""
    meta = {}
    for p in md_files():
        n = os.path.basename(p)[:-3]
        fm = _frontmatter(p)
        meta[n] = {
            "id": n, "title": fm.get("title", n), "category": _category(p),
            "path": os.path.relpath(p, ROOT),
            "verify_live": str(fm.get("verify_live", "")).lower() == "true",
            "confidence": fm.get("confidence", ""),
        }
    known = set(meta)
    links, seen_wiki = [], set()
    for p in md_files():
        n, rels = parse(p)
        for pred, targets in rels.items():
            for t in targets:
                if t in known:
                    links.append({"source": n, "target": t, "kind": "typed", "predicate": pred})
        wn, wls = _wikilinks(p)
        for t in wls:
            if t in known:
                key = tuple(sorted((wn, t)))
                if key not in seen_wiki:
                    seen_wiki.add(key)
                    links.append({"source": wn, "target": t, "kind": "wikilink"})
    deg = {n: 0 for n in known}
    for l in links:
        deg[l["source"]] += 1; deg[l["target"]] += 1
    nodes = []
    for n in sorted(known):
        d = dict(meta[n]); d["degree"] = deg[n]; nodes.append(d)
    return {
        "nodes": nodes, "links": links,
        "meta": {"repo": REPO_URL, "branch": BRANCH, "node_count": len(nodes),
                 "typed_edges": sum(1 for l in links if l["kind"] == "typed"),
                 "wikilinks": sum(1 for l in links if l["kind"] == "wikilink")},
    }

def cmd_json(outpath):
    data = json.dumps(build_graph_json(), ensure_ascii=False, separators=(",", ":"))
    if outpath:
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"wrote {outpath}")
    else:
        print(data)

def cmd_html(outpath):
    tpl = os.path.join(os.path.dirname(__file__), "viewer", "template.html")
    with open(tpl, encoding="utf-8") as f:
        html = f.read()
    data = json.dumps(build_graph_json(), ensure_ascii=False, separators=(",", ":"))
    html = html.replace("/*__GRAPH__*/", data)
    out = outpath or os.path.join(os.path.dirname(__file__), "viewer", "graph.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out} (self-contained, open it directly)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node")
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--lint", action="store_true")
    ap.add_argument("--dot", action="store_true")
    ap.add_argument("--json", nargs="?", const="", metavar="OUT", help="emit graph JSON (typed + wikilink layers)")
    ap.add_argument("--html", nargs="?", const="", metavar="OUT", help="render the self-contained interactive viewer")
    a = ap.parse_args()
    if a.json is not None: cmd_json(a.json); return
    if a.html is not None: cmd_html(a.html); return
    nodes, edges = build()
    if a.lint: sys.exit(cmd_lint())
    if a.validate: sys.exit(cmd_validate(nodes, edges))
    if a.node: cmd_node(nodes, edges, a.node); return
    if a.dot: cmd_dot(edges); return
    cmd_summary(nodes, edges)

if __name__ == "__main__":
    main()

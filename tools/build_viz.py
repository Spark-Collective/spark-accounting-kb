#!/usr/bin/env python3
"""Build a self-contained graph viewer (viz.html) for the knowledge graph.

OKF-compatible. Nodes = concept/reference pages; edges = our typed `relations:`
(labelled + coloured by predicate) plus the body `[[wikilinks]]` (faint, untyped).
Click a node to read its markdown. Open the output viz.html in any browser , no server.

Viewer pattern (Cytoscape + marked, embedded bundle) follows Google's Open Knowledge
Format reference viewer (Apache-2.0, github.com/GoogleCloudPlatform/knowledge-catalog);
this is a clean re-implementation fed by our richer typed graph.
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["concepts", "references"]
TYPE_COLOR = {"rule": "#378ADD", "reference": "#1D9E75", "workflow": "#BA7517", "concept": "#7F77DD"}
PRED_COLOR = {"requires": "#D85A30", "unlocks": "#639922", "gates": "#E24B4A",
              "grounded_by": "#0F6E56", "affects": "#185FA5", "alternative_to": "#534AB7", "part_of": "#5F5E5A"}

def md_files():
    for d in DIRS:
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            for f in fs:
                if f.endswith(".md"):
                    yield os.path.join(dp, f)

def parse(path):
    name = os.path.basename(path)[:-3]
    lines = open(path, encoding="utf-8").read().splitlines()
    fm, body, rels = {}, "", {}
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), len(lines))
        in_rel = False
        for ln in lines[1:end]:
            if re.match(r"^relations:\s*$", ln): in_rel = True; continue
            if in_rel:
                m = re.match(r"^\s+(\w+):\s*\[(.*)\]\s*$", ln)
                if m: rels[m.group(1)] = [t.strip() for t in m.group(2).split(",") if t.strip()]
                elif re.match(r"^\S", ln): in_rel = False
            m = re.match(r"^(type|title|description):\s*(.+)$", ln)
            if m: fm[m.group(1)] = m.group(2).strip().strip('"')
        body = "\n".join(lines[end + 1:])
    wl = {re.split(r"[|\]]", x)[0].strip() for x in re.findall(r"\[\[([^\]]+)\]\]", body)}
    return name, fm, body, rels, wl

def build():
    nodes, edges, bodies = [], [], {}
    deg = {}
    pages = [parse(p) for p in md_files()]
    names = {n for n, *_ in pages}
    typed_pairs = set()
    for name, fm, body, rels, wl in pages:
        for pred, targets in rels.items():
            for t in targets:
                if t in names:
                    edges.append({"data": {"id": f"{name}__{pred}__{t}", "source": name, "target": t, "label": pred,
                                           "color": PRED_COLOR.get(pred, "#888780"), "typed": "yes"}})
                    typed_pairs.add((name, t)); deg[name] = deg.get(name, 0) + 1; deg[t] = deg.get(t, 0) + 1
    for name, fm, body, rels, wl in pages:
        for t in wl:
            if t in names and (name, t) not in typed_pairs and (t, name) not in typed_pairs:
                edges.append({"data": {"id": f"{name}__link__{t}", "source": name, "target": t, "label": "",
                                       "color": "#B4B2A9", "typed": "no"}})
                deg[name] = deg.get(name, 0) + 1; deg[t] = deg.get(t, 0) + 1
    for name, fm, body, rels, wl in pages:
        typ = fm.get("type", "concept")
        nodes.append({"data": {"id": name, "label": fm.get("title", name), "type": typ,
                               "description": fm.get("description", ""), "color": TYPE_COLOR.get(typ, "#888780"),
                               "size": 24 + 4 * deg.get(name, 0)}})
        bodies[name] = body
    return {"nodes": nodes, "edges": edges, "bodies": bodies,
            "typeColor": TYPE_COLOR, "predColor": PRED_COLOR}

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>accounting-knowledge-graph , viewer</title>
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js"></script>
<style>
 *{box-sizing:border-box} body{margin:0;font:14px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:#1a1a1a}
 #wrap{display:flex;height:100vh} #graph{flex:1;background:#fafaf7} #side{width:34%;max-width:460px;border-left:1px solid #e3e1d8;padding:18px 20px;overflow:auto}
 #bar{position:absolute;top:10px;left:10px;display:flex;gap:8px;align-items:center;background:#fff;border:1px solid #e3e1d8;border-radius:8px;padding:6px 10px}
 #q{border:1px solid #ccc;border-radius:6px;padding:4px 8px;font:13px sans-serif;width:180px}
 button{border:1px solid #ccc;background:#fff;border-radius:6px;padding:4px 8px;cursor:pointer;font:13px sans-serif}
 .legend{font-size:12px;color:#555;margin-top:6px} .chip{display:inline-block;padding:1px 7px;border-radius:10px;color:#fff;margin:2px 3px;font-size:11px}
 h1{font-size:16px;margin:0 0 2px} h2{font-size:15px} #meta{color:#666;font-size:12px;margin-bottom:10px}
 #body code{background:#f1efe8;padding:1px 4px;border-radius:3px} #body table{border-collapse:collapse} #body td,#body th{border:1px solid #ddd;padding:3px 7px}
 #body a{color:#185FA5;text-decoration:none;cursor:pointer}
</style></head><body>
<div id="wrap"><div id="graph"></div>
<div id="side"><h1 id="title">accounting-knowledge-graph</h1><div id="meta"></div><div id="body"></div></div></div>
<div id="bar"><input id="q" placeholder="search nodes...">
 <button onclick="relayout('cose')">force</button><button onclick="relayout('concentric')">radial</button><button onclick="fit()">fit</button>
 <span class="legend" id="legend"></span></div>
<script>
const B = __BUNDLE__;
const byId = Object.fromEntries(B.nodes.map(n=>[n.data.id,n.data]));
const cy = cytoscape({container:document.getElementById('graph'),
 elements:{nodes:B.nodes,edges:B.edges},
 style:[
  {selector:'node',style:{'background-color':'data(color)','width':'data(size)','height':'data(size)','label':'data(label)','font-size':9,'text-wrap':'wrap','text-max-width':110,'color':'#333','text-valign':'bottom','text-margin-y':2}},
  {selector:'edge',style:{'width':1.4,'line-color':'data(color)','target-arrow-color':'data(color)','target-arrow-shape':'triangle','arrow-scale':0.8,'curve-style':'bezier','label':'data(label)','font-size':8,'color':'#777','text-rotation':'autorotate'}},
  {selector:'edge[typed="no"]',style:{'line-style':'dashed','target-arrow-shape':'none','width':1}},
  {selector:'.dim',style:{'opacity':0.12}},{selector:'.hi',style:{'opacity':1}}
 ],
 layout:{name:'cose',animate:false,nodeRepulsion:9000,idealEdgeLength:90}});
function show(id){const d=byId[id];if(!d)return;
 document.getElementById('title').textContent=d.label;
 document.getElementById('meta').innerHTML='<span class="chip" style="background:'+d.color+'">'+d.type+'</span> '+(d.description||'');
 document.getElementById('body').innerHTML=marked.parse(B.bodies[id]||'');
}
cy.on('tap','node',e=>{const id=e.target.id();show(id);
 cy.elements().addClass('dim');const nb=e.target.closedNeighborhood();nb.removeClass('dim').addClass('hi');});
cy.on('tap',e=>{if(e.target===cy)cy.elements().removeClass('dim hi');});
document.getElementById('q').addEventListener('input',ev=>{const v=ev.target.value.toLowerCase();
 cy.nodes().forEach(n=>{const hit=!v||n.data('label').toLowerCase().includes(v)||n.id().includes(v);n.style('opacity',hit?1:0.15);});});
function relayout(name){cy.layout(name==='cose'?{name:'cose',animate:false,nodeRepulsion:9000,idealEdgeLength:90}:{name:'concentric',animate:false}).run();}
function fit(){cy.fit(undefined,40);}
document.getElementById('legend').innerHTML=
 Object.entries(B.typeColor).map(([k,c])=>'<span class="chip" style="background:'+c+'">'+k+'</span>').join('')+
 ' &nbsp;|&nbsp; '+Object.entries(B.predColor).map(([k,c])=>'<span class="chip" style="background:'+c+'">'+k+'</span>').join('');
show(B.nodes[0].data.id);
</script></body></html>"""

def main():
    bundle = build()
    out = os.path.join(ROOT, "viz.html")
    html = TEMPLATE.replace("__BUNDLE__", json.dumps(bundle))
    open(out, "w", encoding="utf-8").write(html)
    print(f"viz.html , {len(bundle['nodes'])} nodes, {len(bundle['edges'])} edges -> {out}")

if __name__ == "__main__":
    main()

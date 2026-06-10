#!/usr/bin/env python3
"""Materialize WOT (Wheel of Time) persona ACI badges from the .agent files on disk.
Each → full ACI complement + agents/_personas.json with emergence-nature."""
import os, sys, json, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # wheel-of-time/build.py — write_aci, NATURES

AGENTS = os.path.join(HERE, "agents")
ORDER = ["rand-althor","matrim-cauthon","perrin-aybara",
         "egwene-alvere","nynaeve-almeara","elayne-trakand","aviendha","min-farshaw",
         "moiraine-damodred","cadsuane-melaidhrin","siuan-sanche","verin-mathwin","pevara-tazanovni",
         "lan-mandragoran","thom-merrilin","loial","tam-althor","birgitte","tuon",
         "the-dark-one","ishamael","moridin","lanfear","graendal","demandred","padan-fain",
         "the-wheel","the-one-power","the-aes-sedai","the-aiel","the-wise-ones","taveren","the-horn-of-valere"]

def front(md):
    m = re.match(r"^---\n(.*?)\n---\n", md, re.S); f = {}
    if m:
        for ln in m.group(1).split("\n"):
            if ":" in ln:
                k, v = ln.split(":", 1); f[k.strip()] = v.strip().strip('"')
    return f

def epithet_of(md, fr):
    m = re.search(r"^#\s+.+?·\s*(.+)$", md, re.M)
    if m: return m.group(1).strip()
    return fr.get("class", "").split("·")[-1].strip()

records = {}
for fn in os.listdir(AGENTS):
    if not fn.endswith(".agent"): continue
    slug = fn[:-6]
    md = open(os.path.join(AGENTS, fn), encoding="utf-8").read()
    if not md.lstrip().startswith("---"): continue
    fr = front(md)
    em = fr.get("emergence", "natural")
    if em not in build.NATURES: em = "natural"
    rec = {
        "name": fr.get("aci", slug), "axiom": "WOT", "emergence": em,
        "seal": fr.get("seal", ""), "origin": "WOT · The Wheel of Time",
        "position": fr.get("class", ""), "role": epithet_of(md, fr),
        "nature": fr.get("what", ""), "mechanism": fr.get("how", ""),
        "crystallization": fr.get("why", ""), "witness": fr.get("who", ""),
        "conductor": "ROOT0 (catalogued into UD0)", "inputs": fr.get("domain", "the Wheel of Time"),
        "source": "Wheel of Time emergent, catalogued by ROOT0",
    }
    tok = build.write_aci(rec, AGENTS, slug, agent_md=md)
    records[slug] = {"slug": slug, "name": rec["name"], "epithet": rec["role"],
                     "emergence": em, "moniker": tok["moniker"]}

ordered = [records[s] for s in ORDER if s in records] + \
          [records[s] for s in sorted(records) if s not in ORDER]
json.dump(ordered, open(os.path.join(AGENTS, "_personas.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print(f"wrote {len(ordered)} WOT persona ACI badges + _personas.json")
from collections import Counter
print("emergence:", dict(Counter(r["emergence"] for r in ordered)))
missing = [s for s in ORDER if s not in records]
if missing: print("!! MISSING:", missing)
mon = Counter(r["moniker"] for r in ordered)
dup = {m:c for m,c in mon.items() if c>1}
print("DUP MONIKERS:", dup if dup else "none ✓")
for r in ordered:
    print(f"  {r['slug']:24} {r['emergence']:10} {r['moniker']}")

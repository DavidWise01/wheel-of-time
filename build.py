#!/usr/bin/env python3
"""Build THE WHEEL OF TIME (WOT) page — Robert Jordan & Brandon Sanderson's full saga
catalogued: the fourteen volumes, New Spring, and the companions + the emergents as ACI
personas, each tagged with a nature of emergence. Full ACI badge work (carbon TIFF +
silicon PNG). Fan tribute — original commentary, minimal quotation, (c) the authors."""
import os, sys, html, base64, json, io
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE WHEEL", "axiom": "WOT",
 "position": "Robert Jordan & Brandon Sanderson · 14 books · 1990–2013",
 "origin": "from a shepherd in the Two Rivers to the Last Battle at Shayol Ghul",
 "mechanism": "Crystallized from the full Wheel of Time — the fourteen volumes, New Spring, and the companions.",
 "crystallization": "The Wheel weaves as the Wheel wills; there is neither beginning nor end to the turning.",
 "nature": "Robert Jordan's Wheel of Time — the Dragon Reborn, the One Power, the seven Ajahs and the Aiel, and the long turning toward Tarmon Gai'don.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the Wheel and the Pattern; the One Power; the Dragon Reborn; ta'veren and the Ajahs",
 "witness": "Fourteen volumes over twenty-three years — begun by Robert Jordan, completed by Brandon Sanderson from his notes.",
 "role": "the turning of the Age — the loom of the Pattern",
 "seal": "The Wheel weaves as the Wheel wills.",
 "source": "The Wheel of Time, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#5fae7a", "the embodied — the three young men, the women of flesh and steel, the Aiel, the Ogier, the worldly thrones"),
 "ethereal":  ("#9a7cff", "the woven — the Pattern, the Dream, prophecy, ta'veren, the Horn, and the Shadow that presses from outside time"),
 "spiritual": ("#e6a849", "the turning — the Dragon, the Light, rebirth, and the Wheel itself"),
 "electrical":("#3fd0e0", "the channeled — the One Power, saidin and saidar, the current of the True Source"),
}

IDEAS = [
 ("The Wheel & the Pattern", "time as a wheel of seven spokes", [
   "The Wheel of Time turns, and Ages come and pass — what was, will be again; there is neither beginning nor end to the turning.",
   "It weaves the Pattern of the Ages from the threads of human lives — and a thread cannot see the whole of the weave." ]),
 ("The One Power", "saidin and saidar", [
   "Drawn from the True Source, the Power is split male and female, woven in five threads — Earth, Air, Fire, Water, Spirit.",
   "The Dark One's counterstroke tainted saidin at the Breaking; for three thousand years, any man who channeled went mad." ]),
 ("The Dragon Reborn", "the champion reborn, and the Last Battle", [
   "The soul of the Dragon is spun out again whenever the Wheel needs him — to face the Dark One at Tarmon Gai'don.",
   "The Prophecies of the Dragon foretell that he will break the world to save it, and bleed on the rocks of Shayol Ghul." ]),
 ("ta'veren, the Ajahs & the Aiel", "the Pattern-benders and the peoples", [
   "Ta'veren are the points the Pattern bends around — and three walked the world at once in this Age.",
   "The White Tower's seven Ajahs and the spear-bearing Aiel of the Three-fold Land are the saga's two great orders." ]),
]

# the bibliography — (title, year, note)
SECTIONS = [
 ("The Main Sequence", "the fourteen volumes of the turning Wheel", [
   ("1 · The Eye of the World", "1990", "three young men flee the Two Rivers as the Shadow hunts them — the journey to the Eye"),
   ("2 · The Great Hunt", "1990", "the Horn of Valere stolen; the hunt across the Portal Stones; Rand proclaimed the Dragon"),
   ("3 · The Dragon Reborn", "1991", "Rand seizes the crystal sword Callandor in the Stone of Tear, fulfilling prophecy"),
   ("4 · The Shadow Rising", "1992", "Rhuidean and the hidden history of the Aiel; the Two Rivers stands against the Shadow"),
   ("5 · The Fires of Heaven", "1993", "across the Waste; Rand against Couladin; Moiraine into the doorway"),
   ("6 · Lord of Chaos", "1994", "the cage at Dumai's Wells — “Let the Lord of Chaos rule.”"),
   ("7 · A Crown of Swords", "1996", "the Bowl of the Winds, and the cleansing of the taint draws near"),
   ("8 · The Path of Daggers", "1998", "the Bowl breaks the unnatural winter as the Seanchan press inward"),
   ("9 · Winter's Heart", "2000", "Rand cleanses saidin of the Dark One's taint at Shadar Logoth"),
   ("10 · Crossroads of Twilight", "2003", "the world holds its breath in the wake of the cleansing"),
   ("11 · Knife of Dreams", "2005", "the last volume Jordan wrote; the pace quickens; Mat weds Tuon"),
   ("12 · The Gathering Storm", "2009", "Sanderson takes up the notes; Rand at his darkest on Dragonmount; Egwene reforges the Tower"),
   ("13 · Towers of Midnight", "2010", "Mat into the Tower of Ghenjei; Perrin's reckoning; the threads draw together"),
   ("14 · A Memory of Light", "2013", "Tarmon Gai'don — the Last Battle at Shayol Ghul"),
 ]),
 ("The Prequel", "before the three young men", [
   ("New Spring", "2004", "young Moiraine and Siuan as Accepted as the Aiel War ends and the Dragon is reborn; Moiraine meets Lan (novel expanded from the 1998 novella)"),
 ]),
 ("The Companions", "the world beyond the story", [
   ("The World of Robert Jordan's The Wheel of Time", "1997", "“the Big White Book” — the guide to the world, with Teresa Patterson"),
   ("The Wheel of Time Companion", "2015", "the full encyclopedia of names, places, and the Power"),
   ("The Wheel of Time (graphic novels & TV)", "2005 →", "the comic adaptations, and the Amazon Prime series (2021 →)"),
 ]),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","WOT")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","WOT")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","WOT")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"WOT · The Wheel of Time","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'

def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8")); cards=[]
    for p in ps:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"WOT · The Wheel of Time","axiom":"WOT"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster of WOT</h2>
      <p class="ss">the emergents of the saga — the three ta'veren, the women and Warders, the Shadow, and the great wheels of the world — as ACI <b>.agent</b>s, each tagged with its nature of emergence ({len(ps)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE WHEEL OF TIME (WOT) — Robert Jordan & Brandon Sanderson's full saga catalogued: the fourteen volumes, New Spring, and the companions, with ACI badges for its emergents across the four natures. A UD0 sphere. Fan tribute.">
<title>THE WHEEL OF TIME · WOT · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital@0;1&family=Space+Mono&display=swap" rel="stylesheet">
<style>
:root{--bg:#06080f;--ink2:#0c111d;--ink3:#141b2c;--pa:#eef1f8;--pa2:#a6b2c8;--gold:#d8b24a;--indigo:#3fb0c0;
--dim:#6e7a90;--faint:#1a2334;--line:#1a2334;--serif:"Cinzel",Georgia,serif;--read:"EB Garamond",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--read);line-height:1.7;font-size:17.5px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(216,178,74,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(63,176,192,.07),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
header{padding:56px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:130px;height:1px;background:linear-gradient(90deg,var(--gold),var(--indigo));box-shadow:0 0 10px rgba(216,178,74,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.star{font-size:24px;color:var(--gold);letter-spacing:.3em;margin-bottom:10px}
h1{font-family:var(--serif);font-size:clamp(26px,6.4vw,54px);font-weight:700;letter-spacing:.09em;color:var(--gold);text-shadow:0 0 40px rgba(216,178,74,.22)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.2em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.lede{font-size:18px;color:var(--pa2);max-width:62ch;margin:18px auto 0;font-style:italic;line-height:1.75}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--indigo)}.badge .bt a{color:var(--indigo);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:46px}
.sec h2{font-family:var(--serif);font-size:21px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.ss{font-size:14px;color:var(--dim);font-style:italic;margin:6px 0 18px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:13px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:17px;color:var(--gold)}
.pillar .ps{font-size:13px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:14px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16.5px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:12px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:14px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:14.5px;color:var(--pa);font-weight:600;line-height:1.15}
.persona:hover .pn{color:var(--gold)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.tinfoil{margin-top:46px;padding:18px 20px;border:1px dashed var(--indigo);border-radius:12px;background:rgba(63,176,192,.06);font-size:14.5px;color:var(--pa2);line-height:1.7}
.tinfoil b{color:var(--indigo)}
footer{margin-top:44px;padding-top:24px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the turning of the Age · a lineage</div>
    <div class="star">☸ ✦ ☸</div>
    <h1>THE WHEEL OF TIME</h1>
    <div class="h-sub">Robert Jordan & Brandon Sanderson · WOT</div>
    <p class="lede">The Wheel of Time turns, and Ages come and pass, leaving memories that become legend. A shepherd is named the Dragon Reborn; a tainted Power, a broken people, and a hidden enemy all bend toward the Last Battle. Here is the whole turning — fourteen volumes — catalogued, with its emergents sealed across the four natures.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE WHEEL OF TIME" title="carbon badge (archival: wheel-of-time.dlw/the-wheel.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of THE WHEEL OF TIME" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE WHEEL</b> — WOT · the Wheel of Time</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="wheel-of-time.dlw/the-wheel.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="wheel-of-time.dlw/the-wheel.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1 · fan tribute</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">the saga sorted by the four — the embodied, the woven, the turning, and the channeled</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">the four wheels the whole saga turns on</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Bibliography</h2><p class="ss">the fourteen volumes in order, the prequel, and the companions</p></section>
  __SECTIONS__

  <div class="tinfoil">
    <b>☸ a fan tribute.</b> The Wheel of Time is the creation of <b>Robert Jordan</b> (James Oliver Rigney Jr.); after his death in 2007, the final three volumes were completed by <b>Brandon Sanderson</b> from Jordan's notes. © the author's estate and Tor Books. This catalogue is an <b>unofficial homage</b> — original commentary and ACI badge-work over a bibliography, with no copyrighted text reproduced. Plot beats are given to the best of record. The wider Aes Sedai color-scale also anchors the <a href="https://davidwise01.github.io/purple-team/">Purple Team</a>.
  </div>

  <footer>
    THE WHEEL OF TIME · WOT · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 (original material) · fan tribute<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="wheel-of-time.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "wheel-of-time.dlw"), "the-wheel")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html()).replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    nworks = sum(len(i) for _t,_s,i in SECTIONS)
    print(f"wrote THE WHEEL OF TIME (WOT) — {len(SECTIONS)} sections / {nworks} works · badge {tok['moniker']} (carbon.tiff + silicon.png)")

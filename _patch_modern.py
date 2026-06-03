#!/usr/bin/env python3
"""Bring WoT roster to modern: add authored who/what/where/why/when/how to every
member (specialty kept — the page renders it). Idempotent; run once."""
import json
from pathlib import Path

P = Path(__file__).parent / "roster.json"
R = json.loads(P.read_text(encoding="utf-8"))

F = {
 "Moiraine Damodred": {
  "who":"Aes Sedai of the Blue Ajah, of House Damodred of Cairhien; Lan's first bond.",
  "what":"Leader of the battalion — the sister who found the Dragon Reborn and bent her whole life to the cause.",
  "where":"From the White Tower out into the world, and at last through the redstone doorway.",
  "why":"To find and guard the Dragon so the Light might survive Tarmon Gai'don.",
  "when":"From the search that opens this Turn to her return for its end.",
  "how":"With the One Power, secrecy, and an iron will — spending herself through the doorway and coming back to finish it."},
 "Siuan Sanche": {
  "who":"A Tairen fisherman's daughter raised to the Blue Ajah.",
  "what":"The Amyrlin Seat who staked the White Tower on Moiraine's secret hunt.",
  "where":"Tar Valon and the Tower's heart — and, deposed, the long road back.",
  "why":"To see the Dragon found and the Light readied, whatever the cost to herself.",
  "when":"From before the search, through her fall and the Tower's breaking.",
  "how":"With iron will, hard cunning, and no patience for fools."},
 "Nynaeve al'Meara": {
  "who":"Wisdom of Emond's Field in the Two Rivers.",
  "what":"The angriest and strongest Healer alive.",
  "where":"From the Two Rivers to the White Tower and the world's far edges.",
  "why":"To heal what cannot be healed, and to guard her own, fiercely.",
  "when":"Across this whole Turn, from village Wisdom to legend.",
  "how":"Through a block broken only by anger — Healing the Tower swore impossible: gentling, and madness."},
 "Cadsuane Melaidhrin": {
  "who":"The most formidable living Aes Sedai, Green Ajah — a legend before the rest were born.",
  "what":"The one who teaches kings and Dragons manners.",
  "where":"Wherever the war's hinge is — at Rand's shoulder when it matters most.",
  "why":"To keep the Dragon human enough to win, and the Light's leaders honest.",
  "when":"Late in the Turn, as the Last Battle nears.",
  "how":"With unmatched experience, blunt nerve, and ter'angreal hidden in her hair."},
 "Verin Mathwin": {
  "who":"A Brown Ajah scholar of the deep stacks.",
  "what":"The sister who spent seventy years inside the Black Ajah to betray it with a single book.",
  "where":"The Tower's libraries and the shadows between the Ajahs.",
  "why":"To strike one decisive blow for the Light, at the price of her own life.",
  "when":"Across decades, paid out in a final hour.",
  "how":"Knowledge as the longest blade — patience, an oath's loophole, and a poisoned cup."},
 "Pevara Tazanovni": {
  "who":"A sister of the Red Ajah — the Ajah that hunts men who can channel.",
  "what":"The first Red to bond an Asha'man: the hunt turned to alliance.",
  "where":"The Black Tower, and the bridge between the two kinds of channeler.",
  "why":"To turn old enmity into the alliance the Last Battle needs.",
  "when":"As the men's and women's Powers are forced together.",
  "how":"With courage, candor, and a willingness to cross her own Ajah's grain."},
 "Egwene al'Vere": {
  "who":"An innkeeper's daughter of Emond's Field.",
  "what":"The Amyrlin Seat — all Ajahs and none; the Flame of Tar Valon.",
  "where":"The White Tower, reunited under her hand.",
  "why":"To reforge a broken Tower and lead it whole into the Last Battle.",
  "when":"Her swift rise across this Turn to its climax.",
  "how":"Through unbending will, dreamwalking skill, and refusing to bend even as a captive."},
 "Lanfear": {
  "who":"Mierin Eronaile, reborn as the Chosen called Lanfear.",
  "what":"Most powerful of the female Forsaken; she who helped bore the Bore.",
  "where":"From the Age of Legends into this one — and the World of Dreams.",
  "why":"Love for Lews Therin soured into obsession, and a hunger for power.",
  "when":"Since the Bore was drilled — and again now, circling Rand.",
  "how":"Through Tel'aran'rhiod, beauty, and Compulsion, trusted by neither side."},
 "Moridin": {
  "who":"Ishamael reborn — the Betrayer of Hope.",
  "what":"Nae'blis: nearest the Dark One's hand.",
  "where":"Shayol Ghul, and the shadow over the whole war.",
  "why":"Not conquest but oblivion — he wants the Wheel itself to stop turning.",
  "when":"From the first Age to this last turning, reborn again.",
  "how":"Through despair, the True Power, and the threads that bind even other Chosen."},
 "Graendal": {
  "who":"One of the Chosen — once a famed ascetic healer, now Compulsion incarnate.",
  "what":"A ruler through ruined minds and beautiful slaves.",
  "where":"Hidden palaces — never where the knife is pointed.",
  "why":"Appetite and self-preservation, above the Shadow's cause.",
  "when":"Across the war, surviving by misdirection.",
  "how":"Through Compulsion, manipulation, and disposable pawns."},
 "Demandred": {
  "who":"A Chosen who was, in life, a rival to Lews Therin.",
  "what":"The great general the Light never saw coming.",
  "where":"A war fought far off-page, until he reveals his army.",
  "why":"Brilliance soured to spite — he searched a whole war for the Dragon to challenge.",
  "when":"Held back until the Last Battle, then unleashed.",
  "how":"Through generalship, raw Power, and a kingdom raised in secret."},
 "al'Lan Mandragoran": {
  "who":"Dai Shan — uncrowned King of Malkier; Moiraine's Warder.",
  "what":"The blade that does not break.",
  "where":"From dead Malkier to the world's roads, and at last back to the Blight.",
  "why":"Duty, a death he means to give meaning — and love, late and true, for Nynaeve.",
  "when":"The whole Turn, sword at the Light's shoulder.",
  "how":"'Death is lighter than a feather, duty heavier than a mountain' — discipline and the sword."},
 "Aviendha": {
  "who":"A Maiden of the Spear turned Wise One apprentice.",
  "what":"The desert's keenest edge — warrior and channeler both.",
  "where":"The Three-fold Land, and the glass columns of Rhuidean that show her people's fate.",
  "why":"Toh and honor — and a future she will spend herself to change.",
  "when":"As the Aiel come down from the Waste into the world.",
  "how":"Through ji'e'toh, the spear, and the One Power."},
 "The Wise Ones": {
  "who":"The Aiel's walkers in the dream and keepers of custom.",
  "what":"The spine of the Aiel and the conscience of their chiefs.",
  "where":"The Three-fold Land and Tel'aran'rhiod.",
  "why":"To hold ji'e'toh and steer the clans through prophecy.",
  "when":"Throughout this Turn — counsel behind every chief.",
  "how":"Through dreamwalking, hard wisdom, and unbreakable custom."},
 "Tam al'Thor": {
  "who":"A Two Rivers farmer and former blademaster — Rand's father.",
  "what":"A heron-marked blade and a farmer's steady love — the man who carried a baby off Dragonmount.",
  "where":"Emond's Field, and the Last Battle's field where he leads.",
  "why":"Love for his son and his people, plain and unshakable.",
  "when":"From Rand's infancy to the final fight.",
  "how":"With the heron blade, a second-captain's steadiness, and quiet courage."},
 "Loial": {
  "who":"An Ogier of Stedding Shangtai, ninety years young and 'hasty.'",
  "what":"Scholar and chronicler who would rather read than fight — and fights anyway.",
  "where":"The steddings, the Ways, and the road beside the ta'veren.",
  "why":"Curiosity, friendship, and a book that must be written.",
  "when":"Throughout this Turn — and after, as its author.",
  "how":"Through Ogier strength, the Treesong, and a careful pen — for he writes the book."},
 "Rand al'Thor": {
  "who":"A Two Rivers sheepherder revealed as the Dragon Reborn — one third of the One.",
  "what":"The Light's champion: he who must stand at Shayol Ghul.",
  "where":"From Emond's Field across the world to the slopes of Shayol Ghul.",
  "why":"To win the Last Battle and seal the Bore — without losing his humanity.",
  "when":"This whole Turn, from discovery to Tarmon Gai'don.",
  "how":"Through fire, the One Power, and the weight of every Age on one man's shoulders."},
 "Perrin Aybara": {
  "who":"A Two Rivers blacksmith and Wolfbrother — one third of the One.",
  "what":"The hammer that chooses to be a hammer and not an axe; Lord of the Two Rivers who never wanted a title.",
  "where":"The Two Rivers, the wolf-dream, and the fight to guard the Dragon.",
  "why":"To protect what he loves, and master the wolf without losing the man.",
  "when":"Across this Turn, into Tel'aran'rhiod at its climax.",
  "how":"Through the hammer, the wolf-dream, and a stubborn, steady will."},
 "Matrim Cauthon": {
  "who":"A Two Rivers gambler and trickster — one third of the One.",
  "what":"The luckiest man alive; sounder of the Horn of Valere.",
  "where":"From the Two Rivers to Ebou Dar and the Last Battle's command.",
  "why":"He wants only to be left alone — and keeps saving the world instead.",
  "when":"This whole Turn, against his own loud protests.",
  "how":"Through impossible luck, the ashandarei, and a thousand dead generals' memories in one reluctant head."},
}

miss = []
for m in R["members"]:
    f = F.get(m["name"])
    if not f:
        miss.append(m["name"]); continue
    m.update(f)
if miss:
    raise SystemExit("UNMATCHED MEMBERS: " + ", ".join(miss))

# refresh the note to reflect the modern standard
R["note"] = R.get("note","") + " Every ACI now carries the full DLW tag with an authored six-W .spun (who/what/where/why/when/how)."
P.write_text(json.dumps(R, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("patched", len(R["members"]), "WoT members with authored six-W fields")

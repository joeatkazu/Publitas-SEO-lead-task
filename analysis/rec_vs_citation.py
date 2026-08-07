#!/usr/bin/env python3
"""
Does having your own domain in an answer's citation set coincide with winning
the recommendation -- given the answer recommends someone at all?

Breakdown 1: by vendor.
Breakdown 2: by Publitas page type (docs / alternatives / commercial).
Breakdown 3: by intent group.

Non-branded answers only. Citations (not retrievals) -- AIO has no retrieval data.
"""
import json, csv, glob, re, collections, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("BASELINE_DIR", os.path.join(REPO, "tracker", "baseline"))
REC = {"recommended-primary", "recommended"}

# ---------- load answers ----------
answers = {}
for f in glob.glob(os.path.join(BASE, "raw*.jsonl")):
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        if d.get("branded"):
            continue
        key = (d["engine"], d["query"], d["sample_index"])
        cits = d.get("citations") or []
        answers[key] = {
            "intent": d.get("intent_group", ""),
            "domains": {(c.get("domain") or "").lower().lstrip("www.") for c in cits},
            "urls": [c.get("url", "") for c in cits],
        }

# ---------- load stance ----------
stance = collections.defaultdict(dict)
vendors_seen = collections.Counter()
for r in csv.DictReader(open(os.path.join(BASE, "stance_by_vendor.csv"))):
    if r["branded"].strip().lower() == "true":
        continue
    key = (r["engine"], r["query"], int(r["sample_index"]))
    stance[key][r["vendor"]] = r["stance"]
    vendors_seen[r["vendor"]] += 1

# ---------- recommendation-bearing answers ----------
rec_bearing = {k for k, v in stance.items() if any(s in REC for s in v.values())}
rec_bearing &= set(answers)
print(f"non-branded answers loaded          : {len(answers)}")
print(f"answers with >=1 recommendation     : {len(rec_bearing)}"
      f"  ({100*len(rec_bearing)/len(answers):.0f}%)")
print(f"answers with NO recommendation      : {len(answers)-len(rec_bearing)}"
      f"   <- excluded; nothing to win\n")

# ---------- derive vendor domains empirically ----------
all_domains = collections.Counter()
for a in answers.values():
    all_domains.update(a["domains"])

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

vendor_domain = {}
for v in vendors_seen:
    n = norm(v)
    if len(n) < 4:
        continue
    hits = [d for d in all_domains if n in norm(d.split(".")[-2] if d.count(".") >= 1 else d)]
    if not hits:
        hits = [d for d in all_domains if n in norm(d)]
    if hits:
        vendor_domain[v] = set(hits)

# ---------- BREAKDOWN 1: by vendor ----------
print("=" * 104)
print("BREAKDOWN 1  -- among answers that recommend SOMEONE, is this vendor the pick?")
print("=" * 104)
print(f"{'vendor':<16}{'own domain cited':>26}{'not cited':>22}{'lift':>10}   {'n(cited)':>9}")
rows = []
for v, doms in vendor_domain.items():
    c_n = c_r = n_n = n_r = 0
    for k in rec_bearing:
        cited = bool(answers[k]["domains"] & doms)
        recd = stance[k].get(v) in REC
        if cited:
            c_n += 1; c_r += recd
        else:
            n_n += 1; n_r += recd
    if c_n + n_n == 0 or (c_r + n_r) < 4:
        continue
    pc = 100 * c_r / c_n if c_n else float("nan")
    pn = 100 * n_r / n_n if n_n else float("nan")
    rows.append((v, c_r, c_n, pc, n_r, n_n, pn))

for v, c_r, c_n, pc, n_r, n_n, pn in sorted(rows, key=lambda x: -(x[3] if x[3] == x[3] else -1)):
    lift = f"{pc/pn:>7.1f}x" if pn else "     inf"
    star = "  <-- Publitas" if v == "Publitas" else ""
    print(f"{v:<16}{c_r:>4}/{c_n:<4} = {pc:>5.1f}%      {n_r:>4}/{n_n:<4} = {pn:>5.1f}%   {lift}   {c_n:>9}{star}")

# ---------- BREAKDOWN 2: Publitas by page type ----------
print()
print("=" * 104)
print("BREAKDOWN 2  -- Publitas: which KIND of own page was cited? (non-exclusive)")
print("=" * 104)

def page_type(u):
    ul = u.lower()
    if "support.publitas.com" in ul or "/help" in ul:
        return "documentation"
    if re.search(r"(alternative|-vs-|/compare|competitor)", ul):
        return "alternatives/comparison"
    if "/blog/" in ul:
        return "blog (other)"
    return "commercial/product"

pub_doms = vendor_domain.get("Publitas", {"publitas.com"})
buckets = collections.defaultdict(lambda: [0, 0])   # type -> [answers, recommended]
overlap = collections.Counter()
for k in rec_bearing:
    pub_urls = [u for u in answers[k]["urls"] if "publitas.com" in u.lower()]
    if not pub_urls:
        continue
    types = {page_type(u) for u in pub_urls}
    overlap[len(types)] += 1
    recd = stance[k].get("Publitas") in REC
    for t in types:
        buckets[t][0] += 1
        buckets[t][1] += recd

print(f"{'page type cited':<26}{'answers':>9}{'Publitas recommended':>24}")
for t, (n, r) in sorted(buckets.items(), key=lambda x: -x[1][0]):
    print(f"{t:<26}{n:>9}{r:>10}/{n:<4} = {100*r/n:>5.1f}%")
print(f"\n(answers citing >1 Publitas page type: {sum(v for k,v in overlap.items() if k>1)}"
      f" of {sum(overlap.values())} -- buckets overlap, read as directional)")

# ---------- BREAKDOWN 3: by intent group ----------
print()
print("=" * 104)
print("BREAKDOWN 3  -- Publitas, held within intent group (partial control for query framing)")
print("=" * 104)
print(f"{'intent group':<16}{'own domain cited':>26}{'not cited':>22}")
ig = collections.defaultdict(lambda: [0, 0, 0, 0])  # [cited_n, cited_rec, not_n, not_rec]
for k in rec_bearing:
    g = answers[k]["intent"]
    cited = bool(answers[k]["domains"] & pub_doms)
    recd = stance[k].get("Publitas") in REC
    if cited:
        ig[g][0] += 1; ig[g][1] += recd
    else:
        ig[g][2] += 1; ig[g][3] += recd
for g, (cn, cr, nn, nr) in sorted(ig.items(), key=lambda x: -x[1][0]):
    pc = f"{cr:>3}/{cn:<3} = {100*cr/cn:>5.1f}%" if cn else "      n/a  "
    pn = f"{nr:>3}/{nn:<3} = {100*nr/nn:>5.1f}%" if nn else "      n/a  "
    print(f"{g:<16}{pc:>26}{pn:>22}")

#!/usr/bin/env python3
"""Control: do DOCUMENTATION citations behave differently from vendor-site
citations -- for everyone, not just Publitas?"""
import json, csv, glob, re, collections, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("BASELINE_DIR", os.path.join(REPO, "tracker", "baseline"))
REC = {"recommended-primary", "recommended"}

answers = {}
for f in glob.glob(os.path.join(BASE, "raw*.jsonl")):
    for line in open(f):
        if not line.strip():
            continue
        d = json.loads(line)
        if d.get("branded"):
            continue
        answers[(d["engine"], d["query"], d["sample_index"])] = {
            "intent": d.get("intent_group", ""),
            "urls": [c.get("url", "") for c in (d.get("citations") or [])],
        }

stance = collections.defaultdict(dict)
for r in csv.DictReader(open(os.path.join(BASE, "stance_by_vendor.csv"))):
    if r["branded"].strip().lower() == "true":
        continue
    stance[(r["engine"], r["query"], int(r["sample_index"]))][r["vendor"]] = r["stance"]

rec_bearing = {k for k, v in stance.items() if any(s in REC for s in v.values())} & set(answers)

VENDOR_DOCS = {
    "Publitas":     ("publitas.com",     lambda u: "support.publitas.com" in u),
    "Flipsnack":    ("flipsnack.com",    lambda u: "help.flipsnack.com" in u or "/help" in u),
    "FlippingBook": ("flippingbook.com", lambda u: "/help" in u),
    "Paperturn":    ("paperturn.com",    lambda u: "help-center" in u or "/help" in u),
    "Issuu":        ("issuu.com",        lambda u: "help.issuu.com" in u or "/help" in u),
    "iPaper":       ("ipaper.io",        lambda u: "/help" in u or "support." in u),
}

print("=" * 100)
print("CONTROL -- documentation citations vs other own-domain citations, per vendor")
print("=" * 100)
print(f"{'vendor':<14}{'DOCS cited':>34}{'NON-DOCS own-domain cited':>34}")
print(f"{'':14}{'in rec-answers / recommended':>34}{'in rec-answers / recommended':>34}")
for v, (dom, isdoc) in VENDOR_DOCS.items():
    d_all = d_rec_ans = d_recd = 0
    o_all = o_rec_ans = o_recd = 0
    for k, a in answers.items():
        own = [u for u in a["urls"] if dom in u.lower()]
        if not own:
            continue
        docs = [u for u in own if isdoc(u.lower())]
        others = [u for u in own if not isdoc(u.lower())]
        recd = stance[k].get(v) in REC
        if docs:
            d_all += 1
            if k in rec_bearing:
                d_rec_ans += 1; d_recd += recd
        if others:
            o_all += 1
            if k in rec_bearing:
                o_rec_ans += 1; o_recd += recd
    dpc = f"{100*d_recd/d_rec_ans:.0f}%" if d_rec_ans else "  -"
    opc = f"{100*o_recd/o_rec_ans:.0f}%" if o_rec_ans else "  -"
    print(f"{v:<14}{d_all:>6} ans {d_rec_ans:>4} rec-bearing {d_recd:>3} rec {dpc:>6}"
          f"{o_all:>8} ans {o_rec_ans:>4} rec-bearing {o_recd:>3} rec {opc:>6}")

# Where do documentation citations actually live?
print()
print("=" * 100)
print("Where do documentation citations LIVE? (any vendor above, all non-branded answers)")
print("=" * 100)
tot = collections.Counter()
for k, a in answers.items():
    hit = any(dom in u.lower() and isdoc(u.lower())
              for u in a["urls"] for (dom, isdoc) in VENDOR_DOCS.values())
    if hit:
        tot["in answers that recommend someone" if k in rec_bearing
            else "in answers that recommend NOBODY"] += 1
for k2, n in tot.most_common():
    print(f"  {k2:<42}{n:>4}")
print(f"\n  (for scale: {len(rec_bearing)} of {len(answers)} non-branded answers "
      f"contain a recommendation)")

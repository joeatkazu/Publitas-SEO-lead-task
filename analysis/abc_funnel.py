#!/usr/bin/env python3
"""A/B/C funnel: separate 'publitas.com fetched' from 'cited' from 'Publitas recommended'.

Read-only over the stored tracker outputs — no engine calls.

  A  fetched     -> raw_*.jsonl  `retrieved` / `fanout_map` domains
  B  cited       -> raw_*.jsonl  `citations` domains
  C  recommended -> stance_by_vendor.csv, stance in {recommended-primary, recommended}

Google AI Overviews exposes citations but no retrieval list, so A is unmeasurable
there. The funnel is reported on the two LLM engines (n=102); B/C alone are also
printed across all three (n=153).

Usage: python3 scripts/abc_funnel.py
"""

import collections
import csv
import glob
import json

BASELINE = (
    "/Users/joerobinson/seo-tools/GEO-tracker-Main/geo-tracker/brands/publitas/baseline"
)
RECOMMENDING = {"recommended-primary", "recommended"}
NO_FETCH_LIST = "dataforseo"  # AI Overviews: citations only, no retrieval set


def load_stance():
    """(engine, query, sample) -> Publitas stance."""
    stance = {}
    with open(f"{BASELINE}/stance_by_vendor.csv") as fh:
        for row in csv.DictReader(fh):
            if "publitas" in row["vendor"].lower():
                stance[(row["engine"], row["query"], row["sample_index"])] = row["stance"]
    return stance


def fanout_domains(fanout_map):
    domains = set()
    if isinstance(fanout_map, dict):
        for pages in fanout_map.values():
            for page in pages if isinstance(pages, list) else []:
                if isinstance(page, dict) and page.get("domain"):
                    domains.add(page["domain"])
    return domains


def load_answers(stance):
    """One record per non-branded answer, with A/B/C flags."""
    answers = []
    for path in glob.glob(f"{BASELINE}/raw_*.jsonl"):
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                if d.get("branded"):
                    continue

                has_pub = lambda ds: any("publitas.com" in x for x in ds)
                retrieved = {c["domain"] for c in d.get("retrieved") or []}
                cited = {c["domain"] for c in d.get("citations") or []}
                st = stance.get((d["engine"], d["query"], str(d["sample_index"])))

                answers.append(
                    {
                        "engine": d["engine"],
                        "fetched": has_pub(retrieved) or has_pub(fanout_domains(d.get("fanout_map"))),
                        "cited": has_pub(cited),
                        "recommended": st in RECOMMENDING,
                        "primary": st == "recommended-primary",
                    }
                )
    return answers


def rate(rows, cond, outcome):
    sel = [r for r in rows if cond(r)]
    hits = sum(outcome(r) for r in sel)
    pct = f" = {hits / len(sel):.0%}" if sel else ""
    return f"{hits}/{len(sel)}{pct}"


def main():
    answers = load_answers(load_stance())
    llm = [a for a in answers if not a["engine"].startswith(NO_FETCH_LIST)]

    print(f"All non-branded answers: n={len(answers)} (B/C measurable on all engines)")
    for key in ("cited", "recommended", "primary"):
        print(f"  {key:<12}: {sum(a[key] for a in answers)}")

    n = len(llm)
    print(f"\nFunnel — LLM engines only (fetch list exposed), n={n}")
    for label, key in (("A fetched", "fetched"), ("B cited", "cited"),
                       ("C recommended", "recommended"), ("  of which lead", "primary")):
        hits = sum(a[key] for a in llm)
        print(f"  {label:<16}: {hits:3d}  ({hits / n:.0%})")

    print("\nCrosstab (fetched, cited, recommended)")
    counts = collections.Counter((a["fetched"], a["cited"], a["recommended"]) for a in llm)
    print(f"  {'fetched':>7} {'cited':>6} {'recd':>6} {'n':>4}")
    for key in sorted(counts, reverse=True):
        print(f"  {str(key[0]):>7} {str(key[1]):>6} {str(key[2]):>6} {counts[key]:>4}")

    print("\nConditionals")
    print("  P(cited | fetched)     :", rate(llm, lambda a: a["fetched"], lambda a: a["cited"]))
    print("  P(cited | not fetched) :", rate(llm, lambda a: not a["fetched"], lambda a: a["cited"]))
    print("  P(rec   | cited)       :", rate(llm, lambda a: a["cited"], lambda a: a["recommended"]))
    print("  P(rec   | not cited)   :", rate(llm, lambda a: not a["cited"], lambda a: a["recommended"]))


if __name__ == "__main__":
    main()

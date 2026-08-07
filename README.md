# Publitas — AI & Organic Search Performance Assessment

Supporting repository for the assessment and proposal in [`DELIVERABLE.md`](./DELIVERABLE.md).

Every figure in the report was produced from the stored corpus and scripts in this repository.
The corpus is complete, so any finding can be re-derived, challenged, or re-cut on a different
denominator **without making a further engine call**.

*Shared for evaluation purposes as part of a paid interview assignment.*

---

## What's here, and what isn't

**Included:** the full stored corpus from the measurement run, the 20-prompt panel and the tracker
configuration that produced it, the analysis scripts behind each figure in the report, and the
exhibits those scripts feed.

**Not included:** the two systems that generated the corpus — a buyer-message miner and a
multi-engine GEO tracker. Both are pre-existing tooling I maintain across brands; Publitas is one
tenant in the tracker's brand directory, not a one-off build. What's vendored here is that
tenant's inputs and outputs, not the engine that runs them. The architecture is documented below
in enough detail to evaluate the method, and I'm happy to walk through the running code live.

---

## Repository map

```
analysis/         analysis scripts — each one is named against the figure it produces
tracker/
  queries.md      the 20-prompt panel, grouped by intent and annotated with its sourcing layer
  config.yaml     tracker configuration: engines, judge, competitor set, samples per prompt
  baseline/       the stored corpus: 180 answers, citations, stance judgements, aggregates
data/             mining summaries, presence audits, source-owner classifications
exhibits/         derived working documents referenced by the report
DELIVERABLE.md
README.md
```

`tracker/` is a verbatim copy of this brand's directory in the GEO tracker, vendored so the
repository stands alone. The scripts in `analysis/` read `tracker/baseline/` by default; set
`BASELINE_DIR` to point them at a later run.

---

## Method in brief

20 buyer-intent prompts × 3 samples × 3 engines = **180 stored answers**, collected 2026-08-03/04.

| Engine | Interface | Note |
|---|---|---|
| ChatGPT | `gpt-5.4-mini` + `web_search` | Retrieval list requires `include=["web_search_call.action.sources"]`; without it only *cited* pages are visible, not consulted ones |
| Claude | `web_search_20250305` | |
| Google AI Overviews | via DataForSEO | Exposes citations but no retrieval list |

Search was forced on both LLM engines (`tool_choice`) so the three run under comparable
instructions. Real consumer sessions trigger search less often, so retrieval rates here are an
upper bound.

**Denominators.** 3 of the 20 prompts are branded (they name Publitas) — the two `comparison`
prompts and one `skeptic` prompt; see [`tracker/queries.md`](./tracker/queries.md). Of the
remaining 153
non-branded answers, **148** scored at least one vendor — that is the denominator for every
recommendation figure. Citation figures use **738 non-branded citations**. Branded prompts flatter
publitas.com badly, so they're excluded throughout rather than blended. Any figure in the report
not on the 148/738 pair states its own basis inline.

Each answer is stored with its spawned sub-queries, retrieved pages, citations, per-vendor stance
judgement, the verbatim evidence passage supporting that judgement, and the full response text.
LLM classification is retained with its evidence quote precisely so it can be audited rather than
trusted — three re-analyses run against the stored evidence changed conclusions late in the
assessment.

---

## The two systems, in architecture

### Buyer-message miner

Extracts buyer language from review corpora across Publitas and its competitor set, and classifies
each extracted passage by type: stated product strength, switching trigger, objection, and the
vocabulary buyers use to describe the problem before they know vendor names.

Its output is not the report — it's the **prompt panel**, reproduced in full in
[`tracker/queries.md`](./tracker/queries.md). The 20 tracked prompts were built in four
independent layers so no single source dictates the panel:

1. **Review mining** — buyer language from vendor review corpora (8 prompts)
2. **Category scaffolding** — the market's own taxonomy and competitor set (6 prompts)
3. **Query demand** — Google PAA and community threads, taken verbatim (4 prompts)
4. **Skeptic** — probing the failure mode where the category itself is dismissed (2 prompts)

The layering is load-bearing. One accessibility prompt was sourced from an r/accessibility thread
found independently of the review mining that produced a separate accessibility prompt — two
unrelated sources landing on the same gap is what moved that finding from anecdote to a ranked
recommendation.

The panel is designed to be **re-mined quarterly**. Buyer vocabulary drifts and the vendor set
moves — four competitors surfaced mid-assessment and had to be added to the tracked set. A frozen
panel becomes fiction.

### GEO tracker

Runs the panel across three engines on a schedule and stores everything. Per answer it records:

- which vendors are mentioned, and which receives the **lead recommendation**
- which pages were consulted (fan-out) and which were cited — separately, since these differ
- the verbatim passage supporting every stance judgement
- intent group and branded flag, so results can be cut by how the buyer asked

Two design decisions worth stating:

**Three samples per prompt, weekly not daily.** Engine answers are unstable sample-to-sample. The
widest intent-group spread in this dataset was 16.7% / 50.0% / 0.0% across the three engines. A
week-on-week delta has to clear sampling noise before it means anything, which sets the cadence.
Cost isn't the binding constraint; signal stability is.

**Retrieval and citation are stored as separate events.** Conflating them hides the most useful
result in the study: a page can be consulted and not cited, and a vendor can be recommended
without its site being consulted at all.

### Prioritisation layer

The tracker's output feeds two ranked queues, which is how the report's recommendations were
derived rather than argued:

- **On-page queue** — buyer questions where a competitor's page is cited and Publitas has no
  effective equivalent, or has one that engines don't select
- **Off-page queue** — newly cited third-party pages where Publitas is absent, ranked by
  *citations earned* rather than times consulted

Every cited domain passes through an **ownership classification** first (199 domains, six classes)
so competitor-owned round-ups are removed from the outreach list. This step materially changed the
report's conclusions — see below.

Nothing in this loop publishes or sends. Drafting is grounded in stored evidence, and every item
reaching a human carries the answer and source page that triggered it.

---

## Figure provenance

| Artefact | What's in it |
|---|---|
| `tracker/queries.md` | The 20-prompt panel as run, by intent group and sourcing layer |
| `tracker/config.yaml` | Engines, judge, competitor set, three samples per prompt |
| `tracker/baseline/raw_{engine}_*.jsonl` | 180 stored answers — sub-queries, consulted pages, citations, judge output, full text |
| `tracker/baseline/baseline_{engine}_2026-08-03.csv` | Citation-level rows carrying `branded` and `intent_group` — the denominator system used throughout the report |
| `tracker/baseline/stance_by_vendor.csv` | 853 vendor-mentions, each scored and carrying a verbatim evidence quote |
| `tracker/baseline/agg_fanout_source_map_*.csv` | Unique non-vendor pages typed per URL — raw input to the off-page queue |
| `tracker/baseline/agg_gap_queries_*.csv` | The 13 queries where Publitas is neither cited nor mentioned |
| `data/source-owner-classification-2026-08-04.csv` | 199 cited domains classified by owner across six classes |
| `data/presence-audit-2026-08-04.csv` | Top-100 fan-out pages, presence flag, and the manual-verification flag |
| `analysis/abc_funnel.py` | Separates consulted / cited / recommended as three distinct events (n=102 — Google exposes no retrieval list) |
| `analysis/rec_vs_citation.py` | Whether citation predicts recommendation, and where it doesn't |
| `analysis/rec_vs_citation_primary.py` | The same test restricted to the *lead* recommendation |
| `analysis/docs_control.py` | Documentation retrieval rates, Publitas vs competitors |
| `exhibits/on-page-structural-diff.md` | `/digital-catalog/` against the competitor pages winning category-entry citations, verified in the rendered DOM |
| `exhibits/head-term-rankings.md` | Category head terms split by definitional vs tool-purchase intent |
| `exhibits/lead-arithmetic-chain.md` | The visibility → shortlist entries → demos chain, with assumptions marked as assumptions |

---

## Where the method corrected itself

Recorded because the corrections are load-bearing, and an assessment that never contradicts its
own first draft usually hasn't been tested.

**Owner classification was added mid-analysis and inverted a headline.** The fan-out source map
originally classified "non-vendor" against the tracked competitor list, so competitors *outside*
that list were counted as third parties. Reclassifying by actual ownership cut the addressable
third-party citation pool substantially and reversed the finding that third-party pages out-earn
publitas.com. It also restructured the proposal — from two co-equal motions to one main on-page
motion with off-page tactics.

**A schema default was being read as an observation.** Every bot-blocked row in the presence audit
was byte-identical — presence `False`, zero mentions, empty snippet — because `False` is the
default, not a finding. Blocked pages are now excluded from the denominator or hand-checked in a
browser, never recorded as absences.

**Exact-string matching silently undercounted, twice.** Both a regex and a Playwright selector
filtered on a literal that has locale-specific formatting variants, and a head-term pull queried
12 exact strings while the site ranked well for plural and adjacent forms. Both failures completed
successfully and returned plausible numbers. Standing rule: any extraction filtering on a literal
gets variant-checked before its output becomes a claim.

**Standing rule throughout:** a claim that cannot be substantiated is not asserted in either
direction. Several first-draft findings were removed rather than hedged or reversed.

---

## Running the analysis

The scripts in `analysis/` read from `tracker/baseline/` and were run against the stored corpus,
not live engines — no API credentials and no dependencies are needed to reproduce any figure in
the report. All four are Python 3 standard library only.

```bash
python3 analysis/abc_funnel.py
python3 analysis/rec_vs_citation.py
python3 analysis/rec_vs_citation_primary.py
python3 analysis/docs_control.py
```

`tracker/config.yaml` names the environment variables the collection layer uses
(`ZEN_API_KEY`, `ANTHROPIC_API_KEY`, DataForSEO credentials). Nothing in `analysis/` requires them.

---

## Known limits

These are stated in full in the report's appendix; the short version:

- **No GA4, HubSpot or server-log access.** All traffic figures are third-party estimates —
  directionally useful, not reportable. The conversion rate from recommendation to SQL is the one
  number this assessment cannot supply, which is why the commercial sizing is expressed as a
  proportional lift and why instrumentation is proposed as week-1 work.
- **The panel is 20 prompts, not a query distribution.** Sizing is a lift *on the panel*.
  Weighting intent groups by real search demand needs volume data not available here.
- **These are APIs, not the consumer products.** No memory, no personalisation, no logged-in
  history.
- **Association, not causation.** A query already leaning toward Publitas will both consult
  publitas.com and recommend Publitas. Fan-out makes this confound structural. Named rather than
  controlled for.
- **Perplexity and Gemini were not run.** Three engines including a Google surface was the priority
  given the time; both can be added to the tracker.

---

*Joe Robinson · August 2026*
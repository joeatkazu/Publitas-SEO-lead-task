# Exhibit — Category head terms: what Publitas ranks for, and what it doesn't

**Why this exists.** Every other keyword figure in this document comes from a volume-sorted slice
with an **880/mo floor**, which truncates the category's commercial head terms out of the sample.
The document proposed to win a category without stating where Publitas ranks for the terms that
*name* it. This closes that.

---

## How the term list was built — read this before the numbers

This matters, because **the first version of this exhibit was wrong** and the method is why.

1. **Terms were selected by me**, not measured into existence. There is no query-log access. The
   list started from the category's product nouns and modifiers and was extended by checking what
   `publitas.com` actually ranks for on those stems.
2. **Volume floor: 50/mo.** Terms below that are excluded as noise.
3. **The intent split below is a judgement, not a measurement.** Nothing in the data labels a query
   "buyer" or "browser." Terms whose intent is genuinely ambiguous are **flagged and reported
   separately** rather than pushed into whichever column suits the argument.
4. **Singular and plural variants were both checked.** ⚠️ The first version of this exhibit filtered
   on 12 exact strings and reported *"`shoppable catalog` — not in top 100."* Publitas ranks
   **4th** for `shoppable catalogs`, the plural. That single miss inverted the exhibit's headline.
   Every term below was re-queried on stem-match (`like %stem%`) against publitas.com's full ranked
   set, not on exact strings.

**Source:** DataForSEO `keyword_overview` + `ranked_keywords`, US (location 2840), `en`, pulled
5 August 2026. Position is organic `rank_absolute` within the top 100. **Volumes are third-party
estimates**, with no GA4 or Search Console access to corroborate them.

---

## A. Tool and purchase terms — what a buyer types

| Volume /mo | Term | Publitas position |
|---:|---|---|
| 2,400 | flipbook maker | **not in top 100** |
| 880 | pdf to flipbook | **not in top 100** |
| 480 | flipbook software | **not in top 100** |
| 320 | catalog maker | 32 |
| 210 | online catalog maker | 25 |
| 170 | catalog software | **not in top 100** |
| 110 | digital catalog maker | **not in top 100** |
| 90 | digital catalog software | **7** |
| 90 | digital catalogue software | **9** |
| 70 | digital publishing software | **not in top 100** |
| 50 | online catalog software | 19 |
| 20 | interactive catalog software | **not in top 100** |
| **4,890** | **total** | **84% of the volume is outside the top 100; 4% is in the top 10** |

## B. Definitional and browse terms — what someone learning the category types

| Volume /mo | Term | Publitas position | Ranking page |
|---:|---|---|---|
| 14,800 | flipbook | **9** | `/blog/what-is-a-flipbook/` |
| 390 | what is a flipbook | **6** | `/blog/what-is-a-flipbook/` |
| **15,190** | **total** | **100% of it in the top 10** | |

## C. Ambiguous — flagged, not assigned

These read as either tool-seeking or browsing depending on the searcher, so they are excluded from
both totals above rather than allocated.

| Volume /mo | Term | Publitas position |
|---:|---|---|
| 2,900 | digital publishing platforms | 37 |
| 1,000 | online catalog | **10** |
| 720 | shoppable catalogs | **4** |
| 590 | digital catalog | **4** |
| 50 | interactive catalogs | **3** |

---

## What it shows

**1. Publitas ranks for the terms people use to understand the category and loses the terms people
use to buy in it.** 84% of tool-term volume sits outside the top 100. Meanwhile it holds position 9
for `flipbook` — 14,800/mo, **three times the entire tool-term set combined** — through a
definitional blog post. It is outside the top 100 for both `flipbook software` (480) and `flipbook
maker` (2,400), which are the same word with buying intent attached.

**2. That is the identical shape to the AI-search finding.** Publitas wins `alternatives` at 22.2%
and loses category entry at 3.0%; it wins the definitional head and loses the purchase head. One
failure expressed on two surfaces — which is why organic and AI search are a single argument here,
not two halves of a report.

**3. The one page that carries the commercial terms is the one failing in AI answers.**
`/digital-catalog/` is the ranking URL for `digital catalog software` (**position 7**), `digital
catalog` (4), `shoppable catalogs` (4), `online catalog` (10) and `online catalog software` (19) —
and it earns **zero category-entry citations** in AI answers. The asset is not weak. It is
succeeding on one surface and invisible on the other, which is precisely why the on-page motion is
retrieval and framing work rather than production.

**4. `shoppable` is uncontested, not won.** Position 4 on a 720/mo term reflects how few people
compete for the phrase, not a positioning victory. See Finding 6.

**5. The commercial head is small.** 4,890 monthly US searches across every tool term. That caps any
pure-SEO play and is part of why the AI-answer surface matters disproportionately: in a category
this thin, being the named recommendation is worth more per event than a ranking position.

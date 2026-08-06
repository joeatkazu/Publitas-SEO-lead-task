# Exhibit — From category-entry citation to qualified lead

**What this is.** The chain from the one number this assessment can move to the one the business
cares about. It is a **sensitivity, not a forecast** — two of its six terms are measured, one is
estimated, and three are left as variables with plugged-in values so the reader can substitute
their own.

**Read the labels.** Every row is marked *measured*, *estimated* or *assumed*. The argument does not
depend on the assumed terms being right; it depends on **the rate shift being measured** — terms 3
and 4 — and on the last term being the thing week-1 instrumentation exists to fill in.

---

## The headline needs none of the assumed terms

**SQLs sourced from AI category-entry answers rise roughly 5–7× — directionally, not precisely.**

The figure is built from the two measured terms alone. Moving the category-entry lead-pick rate from
**1 of 33 (3.03%)** to the **16.5–22.2%** Publitas already achieves in other intent groups is a
multiple of 16.5/3.03 = 5.4× and 22.2/3.03 = 7.3×. Search volume (term 1), assistant share (term 2)
and the demo/SQL rate (term 6) all appear on both sides of the ratio and cancel — so none of the
assumed terms has to be right for the multiple to hold.

⚠️ **Do not report this to one decimal.** The base is a **single event**. The 95% Wilson interval on
1 of 33 runs **0.54% to 15.3%**, which propagates to a multiple anywhere between **1.1× and 31×**; a
second Publitas lead pick in the same sample (2 of 33) would halve it to 2.7–3.6×. The arithmetic is
exact, the estimate is not. Two consequences:

- **Round hard.** "Roughly 5–7×" is the most the sample supports. `5.4×` and `5.5×` both appear
  depending on whether you divide the displayed 3.0% or the underlying 1/33 — a tell that the
  precision is fictional. Never quote the multiple without the base (1 of 33) in the same sentence.
- **The robust claim is the one that doesn't divide by 1**: Publitas reaches lead pick at
  **16.5–22.2%** wherever it competes (19 of 115, a sound denominator) and **3.0%** at category
  entry. The gap is the finding; the multiple is a way of voicing it, not evidence in its own right.

**Stated as a multiple, not a percentage, on purpose.** "+440% to +630%" is the same arithmetic and
reads as inflation on a small base — which, given the interval above, it would be.

**One assumption survives the cancellation:** that the marginal recommendation converts like the
average one. It probably converts worse — see point 3 — which makes the multiple an upper bound in
SQL terms even before the sampling noise.

---

## The chain

| # | Term | Value | Status |
|---|---|---|---|
| 1 | **Tool/purchase-intent** head-term volume, US — a *proxy for population size*, not AI demand | **4,890 /mo** across 12 terms | *estimated* — DataForSEO classic search, no GA4/GSC to corroborate |
| 2 | Assistant sessions per unit of that demand | **variable** — plugged at 5% / 10% / 20% | *assumed* |
| 3 | Publitas is the lead recommendation at category entry, today | **3.0%** (1 of 33) | **measured** |
| 4 | Rate Publitas already achieves in other intent groups | **16.5–22.2%** | **measured** |
| 5 | Incremental shortlist entries per month | derived from 2–4 | — |
| 6 | Shortlist entry → demo → SQL | **variable** — plugged at 2% / 5% | *assumed*; the real value is the week-1 job |

**The anchor is tool/purchase intent only — 4,890/mo, the same figure the body quotes.** The
definitional head (`flipbook` at 14,800/mo, `what is a flipbook` at 390) and the 5,260/mo of
ambiguous terms are both excluded from term 1 rather than allocated to it, which makes every output
below **conservative by construction**. Source: `exhibits/head-term-rankings.md`.

## Worked, at three values of term 2

| Share reaching an assistant | Category-entry answers /mo | Lead picks today (3.0%) | At 16.5–22.2% | **Incremental /mo** |
|---|---:|---:|---:|---:|
| 5% | 244 | 7 | 40 – 54 | **+33 to +47** |
| 10% | 489 | 15 | 81 – 109 | **+66 to +94** |
| 20% | 978 | 29 | 161 – 217 | **+132 to +188** |

At the middle row, applying the two placeholder conversion rates:

| Incremental shortlist entries | at 2% | at 5% |
|---|---:|---:|
| +66 to +94 /mo | **+1.3 to +1.9 demos /mo** | **+3.3 to +4.7 demos /mo** |

**Do not read the demo figures as a projection.** 2% and 5% are placeholders chosen to show the
shape of the arithmetic. No industry benchmark is used anywhere in this document, deliberately:
one borrowed average would be the loose thread in a chain whose whole claim is that every figure is
traced.

---

## Five things this chain does *not* do

**1. It does not multiply by the 42%.** 42% of category-entry answers name a single lead pick. That
is *framing*, not a term: it says 58% of these answers name nobody, so the space is contested but
unclaimed. Multiplying it against the 3.0% → 16.5–22.2% shift would double-count, because both
describe the same population of answers.

**2. It does not claim +22–32% and the above are the same statement.** The **+22% to +32%** figure
quoted in the findings is a *panel-wide* lift — 20 primary recommendations across all intent groups
rising to 24–26. The chain above is the *category-entry cell only*, where the movement is 3.0% to
16.5–22.2%. Both are true; they are different denominators and should never be added.

**3. It does not assume category-entry recommendations convert like `alternatives` ones.** They
almost certainly don't — a buyer who already knows the vendor names is further down the funnel than
one who doesn't. Since the target rate (16.5–22.2%) is borrowed from those later-stage groups,
**every SQL figure derived here is an upper bound.** Naming that before a reader does is the point
of the exhibit.

**4. It does not treat head-term search volume as AI-assistant demand.** Term 1 measures *classic
search* and is used only to size the buying-intent population, so the chain's output is an absolute
scale rather than a share of Google volume. Term 2 exists precisely because the relationship between
the two is unknown — and note that assistant queries are **not a subset** of typed searches: buyers
phrase them conversationally, in ways nobody enters into a search box, so the true ratio could sit
above 1:1. The 5/10/20% plugs are a deliberately low bracket, not a cap. Term 2 is the single largest
source of error in the chain — larger than the conversion rates.

**5. Term 1 uses tool/purchase-intent terms only** (4,890/mo), not the definitional head. `flipbook`
alone is 14,800/mo, but someone searching it is learning what a flipbook is, not choosing a vendor.
A further 5,260/mo of ambiguous terms is excluded from the base rather than allocated — see
`exhibits/head-term-rankings.md`. That makes the base **conservative by construction.**

---

## What the chain leaves out — read before treating the demo figure as the payoff

The output above is **one cell**, and a reader who takes +1.3 to +4.7 demos/month as the return on
the programme has read it wrong in four directions at once:

| Excluded | Scale | Why it's out |
|---|---|---|
| The definitional head | **15,190 /mo** (`flipbook` 14,800 at position 9) | Term 1 is purchase-intent only — keeps the base conservative |
| Ambiguous terms | **5,260 /mo** | Flagged, not allocated to either column |
| All non-US demand | not measured | DataForSEO pull is US (location 2840) only; Publitas is a Netherlands company selling internationally |
| Classic-search return on the same fix | not modelled | `/digital-catalog/` already ranks 7 for *digital catalog software*; the on-page motion moves both surfaces |
| Pre-click brand effect | not modelled | A recommendation that produces no click still produces branded search and direct |

And the 10% plug is the **middle** row, not a cap: the 20% row runs +132 to +188 shortlist
entries/month, or +2.6 to +9.4 demos at the same placeholder rates.

**The two conservatism labels point opposite ways and must not be merged.** The *conversion*
assumption is an upper bound, because the target rate is borrowed from later-funnel groups (point 3
above). The *base* is conservative, for every reason in the table above. Quoting "upper bound"
against the whole chain reads a ceiling into a figure that has floors on one side and a ceiling on
the other.

---

## Why the chain still works with three assumed terms

The proportional lift survives whatever the later terms turn out to be. Conversion rates cancel:
if shortlist entries convert to SQLs at rate *r*, then moving the category-entry rate from 3.0% to
16.5–22.2% multiplies SQLs from that cell by the same factor regardless of what *r* is. **The
assumed terms change the absolute answer, not the direction or the relative size.** That is why the
proposal is sized as a proportional lift and why instrumenting *r* is week-1 work rather than a
prerequisite for starting.

**The term that carries the argument — the 3.0% → 16.5–22.2% shift — is measured. The last term is
what week-1 instrumentation exists to fill in.**

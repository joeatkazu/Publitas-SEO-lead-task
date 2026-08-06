# Exhibit — Fan-out source-page target table

**What this is.** The third-party pages ChatGPT, Claude and Google AI Overviews actually cite when
answering buyer-intent prompts in this category, where Publitas is absent, with the play to fix each.

**How to read it.** *Cat-entry* = citations earned on **category-entry queries** — the buyers who
don't yet know the vendor set and never type "Publitas." This is the ranking column, because
category entry is where Publitas is weakest (1 primary recommendation in 33) and therefore where
the commercial upside sits. *Total* = citations across all non-branded queries. *Eng* = how many of
the three engines cited it, i.e. whether it's one model's quirk or a category-wide source.

**Denominator: 738 citations across 148 non-branded answers** (20 prompts × 3 samples × 3 engines,
branded queries excluded). publitas.com earns **45 of those, 6.1%**.

Source: `baseline_{engine}_2026-08-03.csv` + `data/presence-audit-2026-08-04.csv`. Presence is
recorded only where the fetch succeeded. **41 pages were bot-blocked; those rows are empty and are
excluded from the denominator, not counted as absences.** Where a blocked page is named in this
table, it was checked by hand in a browser — and where it could not be, no presence claim is made
in either direction. See A1 caveat 4.

**Filtered to addressable owners.** Every cited domain was classified by who owns the page
(`data/source-owner-classification-2026-08-04.csv`). Competitor-owned pages are excluded: no
outreach places Publitas on a rival's own "best flipbook makers" roundup. That removes the three
clusters that previously ranked 2nd, 3rd and 4th here.

| # | Source | Owner class | **Cat-entry** | Total (share) | Eng | Publitas | Play | Effort | Impact |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **youtube.com** (18 pages) | ugc | **11** | 30 (4.1%) | 1 | absent | **Video asset.** Highest category-entry source in the dataset and **100% Google AI Overviews** — the engine where Publitas is weakest (1 primary rec) and where real buyer volume concentrates. Cited with near-zero retrievals: carried as a known source, not fetched. Not an uncontested channel — **18 cited videos already compete here, 6 of them earning category-entry citations**, and Publitas has no video presence at all. Target those 6 topics, not the channel | **L** | Med-High — populated channel, zero presence |
| 2 | **reddit.com** (6 pages) | ugc | **5** | 14 (1.9%) | 1 | absent | **Participation, not placement.** Includes `r/accessibility`'s "are there any flipbook viewers that are accessible" thread — the same query cluster as the accessibility gap, reached by a different route. Answer as the vendor, disclosed | S | Med |
| 3 | **kindlepreneur.com** (1 page) | independent editorial | **3** | 3 (0.4%) | 1 | absent | **Editorial outreach — the reference case.** Independent, affiliate-monetised, so the conversation is an affiliate one, not a link request. **100% of its citations are category-entry.** ⚠️ Single-engine (Claude only), so treat as one model's preference until a second engine confirms | S | Med |
| 4 | **prnewswire.com** (1 page) | wire | **2** | 2 (0.3%) | 1 | absent | Paid distribution surface, not editorial — the cited page is a Flipsnack release. Cheap to match if there is a launch to announce; not a standing motion | S | Low |
| 5 | **G2 — Flipbook category + alternatives** | review platform | **0** | 18 (2.4%) | 3 | listed p.2, ~28th of 59; **absent** from Top-10 iPaper Alternatives | **Review-volume push.** 10 reviews vs 556/473/409 buries the listing on page 2 and strips its category badges. ⚠️ **Justify on `best-of` (7 citations) and buyer due-diligence only — not as the category-entry fix (zero category-entry citations), and not on unlocking the alternatives lists: Publitas is absent from Capterra's iPaper list too, where iPaper carries 5 reviews to Publitas's 58, so those lists are taxonomy artefacts** | L (sustained) | Med |
| 6 | **guideflow.com** — content-experience-platforms | adjacent vendor | **0** | 13 (1.8%) | 3 | absent | Outreach, marginal — it publishes its own category roundups, so it is a vendor with an editorial habit rather than an independent. Mostly `best-of` — 9 of its 13 citations, the rest problem-led | S | Med |
| 7 | **softwareadvice.com** — catalog management | review platform | **0** | 1 (0.1%) | 1 | **present** — profiles in three categories (catalog management, publishing & subscriptions, CMS), plus comparison pages | **No action.** Not a placement target, and not a sync gap either: the live profile reads **4.6 / 58 reviews, matching Capterra exactly** — both are Gartner properties on one review pool. Listed here only because it earns a citation and an earlier draft wrongly recorded Publitas as absent | — | None |

*`softwareadvice.co.uk` carries a separate citation and is counted separately — no row in this
table aggregates ccTLD properties (A5: one counting system per table). Its iPaper-alternatives page
is bot-blocked and unverified, so no presence claim is made about it in either direction.*

**Not in this table but the highest-response-probability target in the plan:**
`makethingsaccessible.com/guides/pdf-and-online-flipbooks/` — an independent accessibility
authority that currently states Publitas does not list accessibility in its feature set and that
its support portal has no relevant articles. **Both are false.** That is a factual correction with
evidence attached, not a link request. It carries no citations in this panel, which is why it has
no row here — it is sourced from the accessibility audit, not the fan-out map.

**Removed as unactionable, not deprioritised:** `fliplink.me` (10 cited pages, 9 category-entry),
`blog.flipbooksai.com` (3 pages, 4), `zenflip.io` (5 pages, 3) and `veopage.com` — all four are
flipbook vendors running their own roundups. They ranked 2nd, 3rd and 4th on the previous version
of this table. **Cut earlier on the ranking metric:** `catalogy.com / gitnux.org` (zero
category-entry citations) — they ranked only on total citations, which is not the metric.

---

## What the table is for

Of the 40 verifiable fan-out pages, Publitas is absent from 29 — but **13 of those 29 are
competitor- or review-platform-owned**. The **16 that could plausibly add it carry 11
category-entry citations, against the 1 publitas.com earns.** That is the off-page argument in one
comparison: eleven to one, on pages a person could contact.

On the full non-branded basis those 16 pages earn **44 citations (6.0%) against publitas.com's 45
(6.1%)** — parity. The off-page prize is not a volume gap; it is a gap in *reach at the moment the
buyer names nobody*, which is why this table ranks on the category-entry column.

*Counted on the non-branded baseline (738). The presence audit's own `cit` column totals 104 for
these pages because it counts on the 1,245 fan-out basis — not comparable, do not quote it.*

⚠️ **This supersedes the earlier "8.6% vs 15.3%" framing**, which counted branded queries. Branded
queries flatter publitas.com badly — 34 of its 79 citations come from prompts that already name it,
and those buyers are not being acquired. Excluding them roughly doubles the apparent gap.

## What this table does *not* claim

1. **"Publitas is missing from the review directories."** It isn't — verified in-browser: present
   on Capterra (4.6/5, 58 reviews), SourceForge, and G2 (buried). The gap is **editorial
   listicles**, plus review *volume* on G2. A blended "73% absent" across both populations would
   misrepresent both.
2. **"Pages fetched but never cited are the best targets."** `capterra.com/catalog-management-software/`
   is fetched 11× and cited 0× — with Publitas already prominently on it. Presence there bought
   nothing.
3. **"Off-page closes category entry."** ⚠️ **It closes a minority of it, and less than the raw
   third-party share suggests.** See below — this is the single most important caveat on the exhibit.

## The half this table cannot fix

Classifying all **159 category-entry citations by who owns the cited page**:

| Owner of the cited page | Cat-entry citations | Share |
|---|---|---|
| Competitor | 109 | 68.6% |
| UGC — YouTube, Reddit | 18 | 11.3% |
| Independent editorial | 17 | 10.7% |
| Adjacent vendor | 9 | 5.7% |
| Review platform | 5 | 3.1% |
| **publitas.com** | **1** | **0.6%** |

Publitas holds **1 of the 110 vendor-own citations**: FlippingBook 15 · Paperturn 13 · Flipsnack 11
· DCatalog 9 · FlipHTML5 6 · Issuu 5 · **Publitas 1**.

Read the table honestly and the off-page motion shrinks twice. Only 31% of category-entry citations
sit outside competitor domains at all; and of that 31%, UGC and review platforms are participation
and review-velocity work rather than placement. **The genuinely placeable editorial surface is 11
domains** — which is why this exhibit is short, and why the larger motion is on-page. It is three
specific page types competitors already run:

- **Category product pages** — `flippingbook.com/online-digital-catalog` (5),
  `flipsnack.com/digital-catalog` (4), `ipaper.io/use-case/convert-your-pdf` (4). Publitas has the
  exact equivalent at `/digital-catalog/` and it earns **zero** category-entry citations — it takes
  2 non-branded citations, neither at category entry. The one category-entry citation publitas.com
  holds is the **homepage**. A retrieval problem on a page that already exists — not a missing page.
- **Accessibility content — 41 category-entry citations**, across seven vendor domains (DCatalog,
  Flipsnack, FlippingBook, Paperturn, 3DIssue, Issuu, en.fluidbook.com) plus four non-vendor sources
  (Reddit, PR Newswire, nmu.edu, mitrmedia). Top pages: `dcatalog.com/ada-friendly-flipbooks/` 5,
  `flipsnack.com/accessibility` 4, FlippingBook's ADA guide 3, plus help-centre articles. The
  largest single content cluster at category entry. One of the four category-entry queries *is* the
  accessibility question. Independently flagged by review mining as a hard switching trigger.
- **Category-level thought leadership** — `paperturn.com/blog/…/flipbook-software-in-2026` is the
  **top single vendor page at category entry (6 citations)**. Publitas's content library is
  *vendor-vs-vendor* ("Best iPaper Alternatives"), which is precisely why it wins `alternatives` at
  22.2% and loses category entry at 3.0%. **The gap is category-level content, not more comparison
  content.**

## Commercial read

Category entry is the weakest cell: **1 primary recommendation in 33**, against 22.2% on
`alternatives`. Closing it to a rate Publitas already achieves elsewhere in the same panel is a
**+22% to +32% increase in shortlist-winning events** across the whole panel — which converts to
SQLs at whatever their current rate is, the rate week-1 instrumentation exists to baseline.

*Q1's ranking; re-ranks each quarter.*

# Exhibit — On-page structural diff: `/digital-catalog/` vs the pages winning category entry

**Why this exhibit exists.** Motion 2 claims Publitas's category product page is a *retrieval*
problem, not a missing page. That claim needs a mechanism. This is it.

**Comparators:** `flippingbook.com/online-digital-catalog` (5 category-entry citations) and
`flipsnack.com/digital-catalog` (4). Publitas's `/digital-catalog/` earns **zero** — the single
category-entry citation publitas.com holds is the homepage.

**Verification status.** Every item below was checked on 5 August 2026 — rendered DOM via Playwright
(Chromium, 1440×1000, `networkidle`), plus a raw non-rendering fetch where the two paths could
disagree. Where a check corrected an earlier read, the correction is stated rather than absorbed.

---

## Start with what is *not* the difference

Publitas's page has a 13-question FAQ (FlippingBook: 10), a three-step how-to, eight named feature
blocks, three attributed customer quotes and a named logo wall. **It is not thin and it is not
missing structure.** It also already carries `Product` and `BreadcrumbList` schema — verified in the
rendered DOM, and worth stating because an earlier draft of the action table proposed adding
`Product` schema that is already there.

Four differences remain.

---

## a. Specification density — the difference engines actually reward

FlippingBook's FAQ answers carry hard, quotable facts: catalogs up to 2,000 pages; source PDFs of
250 MB / 500 MB / 1 GB by plan; no free plan but a free trial with no card; publications always
ad-free; ADA-compliant viewer; unlimited publications when self-hosted.

Publitas's answers carry named integrations (Shopify, Magento, WooCommerce) and otherwise
qualitative claims — "very easy," "in minutes," "a variety of platforms." No limits, no plan names,
no prices, no named standard.

**Grounding.** This is visible in what engines lift verbatim. From `stance_by_vendor.csv`, at
category entry:

> "Flipsnack — strongest accessibility positioning; claims ADA/WCAG/Section 508 compliance and
> screen reader + keyboard support."
> — `recommended-primary`, `naive`

> "Provides an accessible flipbook player designed for WCAG 2.1 Level AA, ADA, and Section 508
> compliance"
> — `recommended`, `problem-led`

An engine composing a shortlist quotes the constraint it can attribute to a named standard.
Flipsnack supplies three; Publitas supplies none on this page.

---

## b. No third-person self-description

FlippingBook's page contains a liftable sentence: its catalog creator turns a PDF into a flipbook
with interactive elements, analytics and security features. Publitas's nearest equivalent is
*"Publitas isn't just another digital catalog maker — it's your complete solution for creating
high-converting, interactive catalogs that drive sales"* — negatively framed, and a claim rather
than a description. The page is written almost entirely in second person.

**Grounding, and it is sharper than the page-level observation.** Engines *do* produce liftable
third-person sentences about Publitas — but almost never at category entry. Of Publitas's 45
non-branded vendor-mentions in `stance_by_vendor.csv`: problem-led 20 · alternatives 17 · best-of 4
· skeptic 3 · **naive 1**. The descriptive sentences cluster entirely in `comparison`:

> "Publitas is usually the better fit for shoppable ecommerce catalogs"
> "Publitas is better for pure ecommerce conversion and large-scale retail feeds"
> — both `recommended-primary`, `comparison`

The single category-entry evidence quote in the whole corpus is:

> "Publitas — best if you want a polished, retail-focused, shoppable catalog experience."
> — `recommended-primary`, `naive`

Where engines describe Publitas in the third person, they are **synthesising it themselves from
comparison context**, not lifting it from the category page. There is no sentence on
`/digital-catalog/` that answers "what is Publitas."

---

## c. Page hygiene — four findings

**c1. Multiple near-duplicate locale variants of the "trusted by 2000+ customers" band.**
✅ verified two ways

The band is emitted **six times in six languages** — EN, PT, NL, DE, ES, FR — and **only the
English one renders**. The other five compute to zero height, hidden by an ancestor rather than by
their own `display`.

| # | Language | Heading | Renders? |
|---|---|---|---|
| 1 | EN | TRUSTED BY 2000+ CUSTOMERS, INCLUDING LEADING RETAILERS SUCH AS | **yes** |
| 2 | PT | CONFIADO POR MAIS DE 2.000 CLIENTES, INCLUINDO REVENDEDORES LÍDERES, COMO | no |
| 3 | NL | VERTROUWD DOOR 2000+ KLANTEN, WAARONDER TOONAANGEVENDE RETAILERS ZOALS | no |
| 4 | DE | UNS VERTRAUEN MEHR ALS 2000 UNTERNEHMEN, DARUNTER FÜHRENDE EINZELHÄNDLER WIE | no |
| 5 | ES | CON LA CONFIANZA DE MÁS DE 2000 CLIENTES, INCLUYENDO MINORISTAS LÍDERES COMO | no |
| 6 | FR | PLUS DE 2000 CLIENTS DE LA GRANDE DISTRIBUTION ET DU E-COMMERCE | no |

**What follows from this, stated conditionally.** The duplicates are invisible in a browser and
present in the raw markup. Whether they reach a retriever therefore depends on the extraction path:
a raw-HTML parser keeps all six, a rendering extractor that computes styles drops five. A
non-rendering fetch of this page keeps them — that is one data point about one extractor, not proof
of what any specific engine does.

The recommendation is unchanged under either path, which is why it is worth doing: **don't emit
inactive locale variants into the English page.** It is a template fix, not a content decision, and
on the raw-parser path it removes five near-duplicate low-information blocks — each with its own
logo wall — from between the feature and FAQ content.

**c2. A staging-domain link on the money page.** ✅ verified in rendered DOM

Body copy links the phrase *digital catalog maker* to `https://env-publitas-publitas.kinsta.cloud/`
— a Kinsta staging environment, live on the primary commercial page.

**c3. The page is marked up as editorial.** ✅ verified, ⚠️ refined

`og:type` is `article`. The "Time to read: 9 minutes" annotation is **not visible body text** — it
is a Twitter-card meta pair emitted by Rank Math (`twitter:label1` = "Time to read",
`twitter:data1` = "9 minutes"). Both signals come from the same source and point the same way: the
primary commercial page is being described to machines as an article.

**c4. Pricing is absent from the top navigation.** ✅ verified

No `/pricing/` link anywhere in the header or nav; footer only, and no FAQ answer links to it.
FlippingBook links `/order-online` from three separate FAQ answers. This compounds the existing
finding that `/pricing/` is absent from `llms.txt` and carries no `Offer`/`Product` schema —
verified again here: `/pricing/` emits only `Organization` schema. **The same withholding at three
layers.**

---

## d. The roundup format — the largest single gap

The pages winning category entry are **ranked lists that name the vendor set**:
`blog.flipsnack.com/top-digital-catalog-makers…` (10 named),
`yudu.com/blog/top-digital-catalogue-software-providers-2026` (5 named), and
`paperturn.com/blog/…/flipbook-software-in-2026` — the top single vendor page at category entry, at
6 citations.

Publitas's nearest equivalents — `/blog/product-catalog-software-for-retail-discovery-and-growth/`
and `/blog/digital-catalog-maker-5-essential-features/` — supply *criteria* and name nobody.

An engine answering "best digital catalog software" needs a list of names, so it fetches the page
that has one. Both the Flipsnack and YUDU roundups **describe Publitas** — so Publitas is currently
dependent on competitors' content marketing to be named at category entry.

**And the comparison library has a matching structural problem.** Every page is keyed on a
competitor's brand as its entry token (*best Issuu alternative*, *best FlipHTML5 alternatives*,
*iPaper vs DCatalog*). A category-entry buyer types no brand name at all, so the library is
unreachable from that query class **by construction**. That is not mistargeted content — it requires
a token the naive buyer never produces. It is also why the same library wins `alternatives` at
22.2%: there, the token exists.

---

## Verification summary

| Item | Method | Result |
|---|---|---|
| Locale logo bands | raw HTML **and** Playwright rendered DOM | ✅ **6 in six languages; 1 of 6 renders** |
| `kinsta.cloud` staging link | Playwright rendered DOM | ✅ confirmed |
| `og:type: article` | source + rendered DOM | ✅ confirmed |
| "Time to read: 9 minutes" | source | ⚠️ confirmed as **Twitter-card meta**, not body text |
| `/pricing/` absent from top nav | Playwright rendered DOM | ✅ confirmed (footer only) |
| `Product` schema on `/digital-catalog/` | rendered DOM | ⚠️ **already present** — do not list as a fix |
| `/pricing/` schema | rendered DOM | ✅ `Organization` only — no `Offer`/`Product` |

*Rendered-DOM checks run 2026-08-05, Playwright 1.62.1 / Chromium. Evidence quotes from
`stance_by_vendor.csv` (853 vendor-mentions).*

*Counting note on c1: an intermediate check of mine returned "five bands, no Portuguese." That was
an extraction bug — the pattern matched the literal string `2000`, and the Portuguese band writes
it `2.000`. Both a raw non-rendering fetch and the rendered DOM return **six** once the separator is
allowed for. Recorded because a locale-specific number format is exactly the kind of thing that
silently undercounts a duplicate-content audit.*

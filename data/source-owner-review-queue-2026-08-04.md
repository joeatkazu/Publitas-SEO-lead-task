# Job 2 verification queue — 2026-08-04

## A. Every `competitor` row with cat-entry citations (24 rows)

| domain | cits | cat-entry | method | conf | rationale |
|---|---|---|---|---|---|
| `flippingbook.com` | 46 | 15 | exact | high | FlippingBook — tracked competitor in brands/publitas/config.yaml |
| `dcatalog.com` | 34 | 9 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (2) |
| `flipsnack.com` | 32 | 11 | exact | high | Flipsnack — tracked competitor in brands/publitas/config.yaml |
| `fliplink.me` | 30 | 9 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (2) |
| `paperturn.com` | 30 | 13 | exact | high | Paperturn — tracked competitor in brands/publitas/config.yaml |
| `blog.flipsnack.com` | 20 | 1 | exact | high | Flipsnack — tracked competitor in brands/publitas/config.yaml |
| `fliphtml5.com` | 19 | 6 | exact | high | FlipHTML5 — tracked competitor in brands/publitas/config.yaml |
| `help.flipsnack.com` | 19 | 6 | exact | high | Flipsnack — tracked competitor in brands/publitas/config.yaml |
| `issuu.com` | 14 | 5 | exact | high | Issuu — tracked competitor in brands/publitas/config.yaml |
| `publuu.com` | 14 | 2 | exact | high | Publuu — tracked competitor in brands/publitas/config.yaml |
| `blog.flipbooksai.com` | 12 | 4 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (2) |
| `3dissue.com` | 11 | 4 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (1) |
| `zenflip.io` | 10 | 3 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (5) |
| `ipaper.io` | 8 | 4 | exact | high | iPaper — tracked competitor in brands/publitas/config.yaml |
| `heyzine.com` | 5 | 4 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (2) |
| `pubhtml5.com` | 4 | 1 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (1) |
| `realviewdigital.com` | 3 | 3 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (1) |
| `catalogmachine.com` | 2 | 2 | heuristic | high | homepage sells in-category product (matched: online catalog) + commercial paths (9) |
| `en.blog.yumpu.com` | 2 | 1 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (12) |
| `foleon.com` | 2 | 2 | exact | high | Foleon — tracked competitor in brands/publitas/config.yaml |
| `blog.paperturn.com` | 1 | 1 | exact | high | Paperturn — tracked competitor in brands/publitas/config.yaml |
| `en.fluidbook.com` | 1 | 1 | llm | high | Fluidbook — 'the best interactive catalogue solution … e-brochures, flipbooks' |
| `flipbookpdf.net` | 1 | 1 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (1) |
| `fliplify.com` | 1 | 1 | heuristic | high | homepage sells in-category product (matched: flip\s?book) + commercial paths (1) |

## B. Every `llm`-tier row (135 rows), cited-heaviest first

| domain | class | cits | cat-entry | conf | rationale |
|---|---|---|---|---|---|
| `guideflow.com` | adjacent-vendor | 13 | 0 | high | interactive demo platform publishing its own category roundups |
| `apps.shopify.com` | review-platform | 6 | 1 | high | Shopify App Store — listing/profile surface, not editorial outreach |
| `adobe.com` | adjacent-vendor | 5 | 1 | high | Adobe |
| `support.google.com` | adjacent-vendor | 5 | 0 | high | Google product help |
| `gitnux.org` | independent-editorial | 4 | 0 | medium | AI-generated market-statistics content farm (same template as zipdo/wifitalents) |
| `zipdo.co` | independent-editorial | 4 | 0 | medium | AI-generated market-statistics content farm; sells reports, not in-category product |
| `accio.com` | adjacent-vendor | 3 | 0 | high | agentic business AI |
| `cloudtalk.io` | adjacent-vendor | 3 | 0 | high | call-centre software |
| `coherentmarketinsights.com` | independent-editorial | 3 | 3 | medium | market-research report publisher |
| `commplify.ai` | adjacent-vendor | 3 | 0 | high | omnichannel CX platform |
| `comosoft.us` | adjacent-vendor | 3 | 0 | high | multichannel marketing/PIM/DAM (LAGO) |
| `dailyiowan.com` | independent-editorial | 3 | 3 | high | independent university newspaper |
| `developers.google.com` | adjacent-vendor | 3 | 0 | high | Google developer docs |
| `edvantis.com` | adjacent-vendor | 3 | 0 | high | software development services |
| `kindlepreneur.com` | independent-editorial | 3 | 3 | high | self-publishing blog, affiliate-monetised — the reference case |
| `nubuntu.org` | independent-editorial | 3 | 1 | medium | flipbook-topic content blog; no product sold on the domain, but SEO-farm in character |
| `support.yotpo.com` | adjacent-vendor | 3 | 0 | high | Yotpo (ecommerce reviews/loyalty) support portal |
| `thecxlead.com` | independent-editorial | 3 | 0 | high | Black&White Zebra editorial listicle network ('10 Best …') |
| `theretailexec.com` | independent-editorial | 3 | 0 | high | retail trade content site |
| `vendors.accessibility.com` | independent-editorial | 3 | 0 | medium | accessibility resource authority with a vendor directory; no in-category product |
| `veopage.com` | competitor | 3 | 0 | high | flipbook vendor: own blog runs 'Best Issuu Alternatives: 12 Top Platforms Compared' at /en/blog/ |
| `wifitalents.com` | independent-editorial | 3 | 0 | medium | AI-generated market-statistics content farm (same template) |
| `apps.apple.com` | review-platform | 2 | 2 | high | Apple App Store — listing surface, not editorial outreach |
| `attributionapp.com` | adjacent-vendor | 2 | 0 | high | marketing attribution software |
| `catsy.com` | adjacent-vendor | 2 | 0 | high | PIM/DAM |
| `experienceleague.adobe.com` | adjacent-vendor | 2 | 0 | high | Adobe Experience Cloud docs |
| `flowpaper.com` | competitor | 2 | 0 | high | FlowPaper — 'Flipbook Maker and Interactive Publications Platform' (fmr FlexPaper) |
| `formaxprinting.com` | adjacent-vendor | 2 | 2 | high | commercial print shop |
| `goorca.ai` | adjacent-vendor | 2 | 0 | high | AI growth agents for Shopify |
| `hatsoffdigital.com` | adjacent-vendor | 2 | 0 | high | digital marketing agency |
| `helpx.adobe.com` | adjacent-vendor | 2 | 0 | high | Adobe product help |
| `leakypaywall.com` | adjacent-vendor | 2 | 1 | high | WordPress subscription/paywall platform for publishers |
| `mediumtalk.net` | independent-editorial | 2 | 0 | high | WordPress/SEO blog |
| `odoopim.com` | adjacent-vendor | 2 | 0 | high | PIM |
| `optimizesmart.com` | adjacent-vendor | 2 | 0 | high | GA4/GTM consultancy |
| `pimcore.com` | adjacent-vendor | 2 | 0 | high | PIM/MDM/DXP |
| `prnewswire.com` | independent-editorial | 2 | 2 | high | press-release wire; placement surface, sells no in-category product |
| `research.com` | review-platform | 2 | 0 | high | software review directory (cited page is a product review) |
| `shopify.com` | adjacent-vendor | 2 | 0 | high | Shopify |
| `thecmo.com` | independent-editorial | 2 | 0 | high | Black&White Zebra editorial listicle network ('10 Best …') |
| `zohodesk.dcatalog.com` | competitor | 2 | 0 | high | DCatalog's own support portal (Zoho Desk subdomain) |
| `accessibe.com` | adjacent-vendor | 1 | 0 | high | web accessibility overlay/compliance vendor |
| `agneovo.com` | adjacent-vendor | 1 | 0 | high | display hardware |
| `aims360.com` | adjacent-vendor | 1 | 0 | high | apparel ERP |
| `analyticsmania.com` | independent-editorial | 1 | 0 | high | independent GTM/GA blog |
| `antares.am` | competitor | 1 | 0 | medium | Antares Media Holding sells e-magazine production; cited page is 'E-Magazines vs. Flipbooks' |
| `archimetric.com` | adjacent-vendor | 1 | 0 | high | EA/DevOps consultancy content site |
| `bakedmoon.studio` | adjacent-vendor | 1 | 0 | high | 3D modelling studio |
| `banedsgn.com` | adjacent-vendor | 1 | 1 | high | K-12 editorial design studio |
| `blog.calameo.com` | competitor | 1 | 0 | high | Calaméo digital-publishing platform blog |
| `blog.catalogmachine.com` | competitor | 1 | 0 | high | blog subdomain of catalogmachine.com, already classed competitor |
| `blog.visual-paradigm.com` | adjacent-vendor | 1 | 0 | high | Visual Paradigm (modelling/diagramming) blog |
| `bloomreach.com` | adjacent-vendor | 1 | 0 | high | personalisation/commerce AI |
| `business.adobe.com` | adjacent-vendor | 1 | 1 | high | Adobe Experience Cloud |
| `ca.pcmag.com` | independent-editorial | 1 | 1 | high | PCMag — technology review publication |
| `calendhub.com` | adjacent-vendor | 1 | 0 | high | calendar/scheduling software |
| `circulio.com` | adjacent-vendor | 1 | 0 | high | rental ecommerce platform |
| `cms.flipbuilder.com` | competitor | 1 | 0 | high | FlipBuilder; cited page is /extension/digital-catalogue-software.html |
| `community.shopify.com` | ugc | 1 | 0 | high | Shopify merchant community forum |
| `contentful.com` | adjacent-vendor | 1 | 0 | high | headless CMS |
| `conversios.io` | adjacent-vendor | 1 | 0 | high | GA4/ecommerce analytics plugin |
| `convert.com` | adjacent-vendor | 1 | 0 | high | A/B testing tool |
| `convert.elevio.help` | adjacent-vendor | 1 | 0 | high | Convert.com knowledge base |
| `cuspera.com` | review-platform | 1 | 0 | high | software discovery/advisor directory |
| `cwcreative.com` | adjacent-vendor | 1 | 0 | high | print/graphic/web design studio |
| `cxtoday.com` | independent-editorial | 1 | 0 | high | CX trade publication |
| `digitalanalystteam.com` | adjacent-vendor | 1 | 0 | high | white-label digital agency |
| `dirxion.com` | competitor | 1 | 0 | medium | Dirxion digital-edition/lookbook vendor; cited page is its own retail lookbook article |
| `distributordatasolutions.com` | adjacent-vendor | 1 | 0 | high | product-data platform |
| `dxpscorecard.com` | review-platform | 1 | 0 | high | independent DXP/CMS scoring directory |
| `echovme.in` | adjacent-vendor | 1 | 0 | high | digital marketing agency |
| `elementor.com` | adjacent-vendor | 1 | 0 | high | website builder |
| `en.fluidbook.com` | competitor | 1 | 1 | high | Fluidbook — 'the best interactive catalogue solution … e-brochures, flipbooks' |
| `equalweb.com` | adjacent-vendor | 1 | 0 | high | web accessibility vendor |
| `equidox.co` | adjacent-vendor | 1 | 1 | high | PDF accessibility remediation software |
| `expivi.com` | adjacent-vendor | 1 | 0 | high | 3D product configurator/CPQ |
| `filestage.io` | adjacent-vendor | 1 | 0 | high | online proofing software |
| `fittdesign.com` | adjacent-vendor | 1 | 0 | high | apparel design & production agency |
| `gelato.com` | adjacent-vendor | 1 | 0 | high | print-on-demand platform |
| `globalmediainsight.com` | adjacent-vendor | 1 | 0 | high | digital agency |
| `goodmenproject.com` | independent-editorial | 1 | 1 | high | general-interest online publication |
| `help.3dsellers.com` | adjacent-vendor | 1 | 0 | high | 3Dsellers (ecommerce tooling) help centre |
| `help.flowhub.com` | adjacent-vendor | 1 | 0 | high | Flowhub (cannabis POS) help centre |
| `help.shopify.com` | adjacent-vendor | 1 | 0 | high | Shopify merchant docs |
| `influenceflow.io` | adjacent-vendor | 1 | 0 | high | influencer marketing platform |
| `inro.social` | adjacent-vendor | 1 | 0 | high | Instagram DM automation |
| `knowband.com` | adjacent-vendor | 1 | 0 | high | ecommerce plugins/extensions |
| `kontent.ai` | adjacent-vendor | 1 | 0 | high | headless CMS |
| `learn.microsoft.com` | adjacent-vendor | 1 | 0 | high | Microsoft docs |
| `lunio.ai` | adjacent-vendor | 1 | 0 | high | ad-traffic verification |
| `lyxelandflamingo.com` | adjacent-vendor | 1 | 0 | high | digital marketing agency |
| `measureu.com` | adjacent-vendor | 1 | 0 | high | measurement training courses |
| `meta.com` | adjacent-vendor | 1 | 0 | high | Meta |
| `mhs.ox.ac.uk` | independent-editorial | 1 | 1 | high | Oxford museum exhibit page — unrelated sense of 'flip book' |
| `mitrmedia.com` | adjacent-vendor | 1 | 1 | high | publisher technology & services firm |
| `moast.io` | adjacent-vendor | 1 | 0 | high | shoppable video app for Shopify |
| `neilpatel.com` | adjacent-vendor | 1 | 0 | high | NP Digital — agency + owned marketing media |
| `nmu.edu` | independent-editorial | 1 | 1 | high | university |
| `omegatheme.com` | adjacent-vendor | 1 | 0 | high | Shopify/Wix apps |
| `optimizely.com` | adjacent-vendor | 1 | 0 | high | experimentation/DXP |
| `paper-republic.com` | adjacent-vendor | 1 | 1 | high | leather notebooks — physical stationery, unrelated sense of the term |
| `pimberly.com` | adjacent-vendor | 1 | 0 | high | PIM |
| `reportei.com` | adjacent-vendor | 1 | 0 | high | marketing reporting SaaS |
| `saleslayer.com` | adjacent-vendor | 1 | 0 | high | PIM |
| `selecthub.com` | review-platform | 1 | 0 | high | software selection directory (cited page is a product profile) |
| `sigmasolve.com` | adjacent-vendor | 1 | 0 | high | software engineering services |
| `smackcoders.com` | adjacent-vendor | 1 | 0 | high | WordPress plugins |
| `socialcommerceclub.com` | adjacent-vendor | 1 | 0 | high | TikTok Shop agency |
| `socialsurgemarketing.com` | adjacent-vendor | 1 | 0 | high | digital marketing agency |
| `softwarefinder.com` | review-platform | 1 | 0 | high | software review directory |
| `sproutsocial.com` | adjacent-vendor | 1 | 0 | high | social media management |
| `statista.com` | independent-editorial | 1 | 1 | high | statistics publisher |
| `storyblok.com` | adjacent-vendor | 1 | 0 | high | headless CMS |
| `stylitics.com` | adjacent-vendor | 1 | 0 | high | retail AI outfitting/imagery |
| `sugarpixels.com` | adjacent-vendor | 1 | 0 | high | web design agency |
| `swifdoo.com` | adjacent-vendor | 1 | 0 | high | PDF editor |
| `syndeca.com` | adjacent-vendor | 1 | 0 | high | shoppable content/media layer — adjacent to shoppable catalogs, not a catalog maker |
| `technologymagazine.com` | independent-editorial | 1 | 0 | high | trade publication |
| `tecnosoluciones.com` | adjacent-vendor | 1 | 0 | high | web/digital services provider |
| `thenumbersmith.co.uk` | adjacent-vendor | 1 | 0 | high | cloud accounting practice |
| `thewisemarketer.com` | independent-editorial | 1 | 0 | high | loyalty-marketing trade publication |
| `unbounce.com` | adjacent-vendor | 1 | 0 | high | landing-page builder |
| `walsworth.com` | adjacent-vendor | 1 | 0 | high | commercial printer |
| `webaholics.ai` | adjacent-vendor | 1 | 0 | high | AI marketing agency |
| `weloveweb.eu` | adjacent-vendor | 1 | 0 | high | marketing & design agency |
| `wisepim.com` | adjacent-vendor | 1 | 0 | high | PIM/AI catalog enrichment |
| `worldmetrics.org` | independent-editorial | 1 | 0 | medium | AI-generated market-statistics content farm (same template) |
| `yesoptimist.com` | adjacent-vendor | 1 | 0 | high | B2B SaaS SEO agency |
| `yo-kart.com` | adjacent-vendor | 1 | 0 | high | multi-vendor marketplace software |
| `youngurbanproject.com` | adjacent-vendor | 1 | 0 | high | upskilling course provider |
| `zanfia.com` | adjacent-vendor | 1 | 0 | high | creator-business platform |
| `aiapps2go.com` | review-platform | 0 | 0 | high | AI app directory (300+ products, 20+ categories) — listing surface |
| `nerdisa.com` | review-platform | 0 | 0 | high | business-software discovery directory |
| `tenorshare.com` | adjacent-vendor | 0 | 0 | high | PDF/data-recovery software utility vendor |
| `toolradar.com` | review-platform | 0 | 0 | high | B2B software pricing/reviews/comparison directory, 9,000+ tools |

# EP — bilan de couverture consolidé (variables × années × source)

**Généré le 6 novembre 2026.** Fusionne les deux gisements sourcés :
- **tunisia-data** `sources/entreprises-publiques/` — séries **longues** (2000-2024/25) lues des états
  financiers primaires (BVMT, STEG), **seule source de la VA**.
- **précis** `precis/_seriescache/entreprises-publiques-*.csv` — couverture **large et récente**
  (2016-2023) engendrée des **rapports du ministère des Finances** (LF2020→LF2025), multi-édition.

**Provenance point par point** : `tunisia-data/sources/entreprises-publiques/consolidation-provenance-globale.csv`
(10 826 lignes, 70 EP, **0 valeur sans fichier ni page**). Chaque cellule ci-dessous est adossée à
cette table (fichier + page + édition + lecture). Lecture des plages : une plage qui **commence ≤ 2017**
vient de tunisia-data (primaire) ; une plage **2018-2023** vient du précis (rapports MdF). La colonne
**VA** est toujours tunisia-data (la VA n'existe pas dans les rapports MdF).

## Matrice EP × variables (étendue des années)

| EP | Revenus/CA | VA | Masse sal. | Résultat | Effectif | Actif | Cap.propres | Dette |
|---|---|---|---|---|---|---|---|---|
| afh | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| afi | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| arru | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| attt | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| bfpme |  |  | 2018-2023 |  | 2018-2023 | 2018-2023 |  |  |
| bh |  |  | 2018-2023 |  | 2018-2023 | 2018-2023 |  |  |
| bh_bank | 2003-2024 |  | 2003-2024 | 2006-2024 |  |  |  |  |
| bna | 2000-2024 |  | 2000-2024 | 2000-2024 | 2018-2023 | 2018-2023 |  |  |
| bte_adp | 2004-2024 |  | 2004-2024 | 2004-2024 |  |  |  |  |
| bts |  |  | 2018-2023 |  | 2018-2023 | 2018-2023 |  |  |
| ciments_bizerte | 2009-2024 | 2010-2024 | 2009-2024 | 2009-2024 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| ciments_oum_el_kelil | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2019 |
| cnam |  |  |  |  | 2017-2022 |  |  |  |
| cnrps |  |  |  |  | 2017-2023 |  |  |  |
| cnss |  |  |  |  | 2017-2023 |  |  |  |
| cpg | 2006-2010 | 2006-2010 | 2010-2010 | 2006-2010 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| cpscl | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| ctf | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| ctn | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2021 | 2020-2021 | 2018-2020 |
| el_fouladh | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| etap | 2008-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| gct | 2012-2013 | 2012-2013 | 2018-2022 | 2012-2013 | 2017-2022 | 2020-2022 | 2020-2022 | 2018-2020 |
| mtk | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| oaca | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| office_cereales | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| office_commerce | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| office_huile | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| ommp | 2018-2023 |  | 2018-2023 | 2020-2020 | 2016-2023 | 2020-2020 | 2020-2020 | 2018-2020 |
| onas | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| otd | 2018-2022 |  | 2018-2022 | 2020-2022 | 2016-2022 | 2020-2022 | 2020-2022 | 2018-2020 |
| pct | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| poste | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| regie_alcools | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| rnta | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| sncft | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2022 | 2018-2019 |
| sncpa | 2018-2022 |  | 2018-2022 | 2020-2022 | 2016-2023 | 2020-2022 | 2020-2022 | 2018-2020 |
| sndp | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| snit | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| sogemt | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| sonede | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2022 | 2020-2022 | 2018-2020 |
| sotrapil | 2000-2017 | 2007-2017 | 2000-2017 | 2000-2017 | 2018-2023 | 2020-2023 | 2020-2023 | 2019-2020 |
| sotumag | 2002-2024 | 2016-2019 | 2002-2024 | 2002-2024 |  |  |  |  |
| sprols | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| srt_bizerte | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2019 |
| srt_sfax | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| star |  |  | 2004-2024 | 2002-2024 |  |  |  |  |
| stb | 2002-2025 |  | 2002-2025 | 2002-2025 | 2018-2023 | 2018-2023 |  |  |
| steg | 2014-2023 | 2014-2023 | 2014-2023 | 2014-2023 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| stir | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| transtu | 2018-2023 |  | 2018-2023 | 2020-2023 | 2017-2023 |  | 2020-2020 | 2018-2020 |
| ttn | 2018-2023 |  | 2018-2023 | 2020-2023 | 2018-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| tunis_re |  |  | 2009-2025 | 2009-2025 |  |  |  |  |
| tunisair | 2000-2022 | 2003-2022 | 2000-2022 | 2000-2022 | 2016-2023 |  |  | 2018-2020 |
| tunisie_autoroutes | 2018-2023 |  | 2018-2023 | 2020-2023 | 2016-2023 | 2020-2023 | 2020-2023 | 2018-2020 |
| tunisie_telecom | 2007-2009 | 2007-2009 | 2007-2009 | 2007-2009 | 2017-2023 | 2020-2023 | 2020-2023 | 2018-2020 |

## Lecture
- **VA (productivité) — 8 EP** : tunisair, steg, ciments_bizerte, sotrapil, sotumag, tunisie_telecom,
  gct, cpg. Tout le reste de la colonne VA est vide (non calculable sans comptes primaires détaillés).
- **Couverture récente quasi exhaustive (précis)** : ~45 EP ont revenus/charges/résultat/effectif/
  bilan/dette sur 2018-2023 (rapports MdF) — y compris offices, sociétés régionales, EPNA.
- **Séries longues (tunisia-data)** : banques (bna, stb, bh_bank, bte_adp) et assurances (star,
  tunis_re) 2000-2025 ; tunisair, ciments, sotrapil, sotumag, steg.
- **VA/agent** obtenue par jointure VA (tunisia-data) × effectif (précis) : tunisair 2016-2022,
  steg 2017-2023, ciments 2018-2023 (voir `ep-sources-consolidation.md`).
- **ROE/ROA, ratios bancaires, dettes croisées** : voir `ep-volet-financier.md` (tout côté précis).

## Lacunes fermes
- **sotumag** : aucun effectif public → pas de VA/agent.
- **tunisair** effectif mère **avant 2016** → VA/agent ne remonte pas avant 2016.
- cpg/gct/tunisie_telecom : VA (ancienne) et effectifs (MdF récents) ne se recouvrent pas.

# Budget du ministère de l'Agriculture avant 2014 — note documentaire

Rôle : documentaliste. Date : 13 novembre 2026. Chantier « livre agriculture », chapitre 3
(budget). Objet : combler, autant que possible, le **trou « avant 2014 »** du budget du ministère
de l'Agriculture (fiche `r-agri-budget-ministere-avant-2014`), signalé § 2.4 et § 5 de
`docs/notes/agriculture-budget-documentation.md`. **Rendement incertain assumé au départ ;
rendement réel : positif** — une série d'exécution homogène 2008-2014 est constituée, le pré-2008
reste un trou cadré avec un chemin de collecte précis.

Invariants : montants en **dinars courants** (flux budgétaires, famille ministère des Finances /
exécution). FR = source de vérité. Rien n'est approximé : chaque niveau porte sa source.

---

## 1. Ce qui est trouvé — série d'exécution 2008-2014 (BOOST)

### 1.1 Source et périmètre

La base **BOOST Tunisie** (`mizaniatouna.gov.tn`, ministère des Finances + Banque mondiale),
**déjà acquise dans `tunisia-data`** (`data/raw/mizaniatouna/boost_fr.xlsx`, fiche
`sources/mizaniatouna-boost.md`, catalogue `sources/mizaniatouna-boost-urls.csv`,
SHA-256 `25df422…175c`), donne les dépenses de l'État **par ligne budgétaire 2008-2016**, dont la
colonne **ADMIN2 (التصنيف الاداري = chapitre/ministère)**. Deux chapitres portent l'agriculture :

- **16 — Ministère de l'Agriculture** (administration centrale + offices rattachés) ;
- **17 — Ministère des Commissions Régionales pour le Développement Agricole** = les
  **commissariats régionaux au développement agricole (CRDA)**, services déconcentrés du ministère.

Le **budget du ministère au sens large = chap. 16 + chap. 17**. Montant retenu : colonne
**PAYÉ (المدفوع = exécution)**, **TYPE 01 BUDGET** (budget de l'État), Titre 1 (dépenses
courantes) + Titre 2 (dépenses de développement), **hors Fonds du Trésor** — donc moyens de l'État,
gestion + développement, homogène d'un bout à l'autre. Unité : **dinar courant**.

**Validation croisée décisive** : BOOST, exécution 2014, budget-only, chap. 16+17 =
**959 227 kDT** — à comparer à la **prévision ministère du PAP 2015 pour 2014 = 967 456 kDT**
(série B de `agriculture-budget-documentation.md`, § 1.2). Écart ≈ 0,9 % (exécution vs prévision) :
le périmètre « 16+17, budget de l'État » **coïncide** avec le périmètre « ministère » des PAP
pilotes. De même, BOOST **LF votée 2016 = 1 243 178 kDT = exactement** le chiffre 2016 lu dans le
PAP 2017 (série B). Le périmètre BOOST et le périmètre PAP sont donc le même objet.

### 1.2 Série retenue — exécution (payé), budget de l'État, chap. 16+17, hors fonds du Trésor

| Gestion | Ministère (chap. 16) | CRDA (chap. 17) | **Total ministère, budget État (kDT)** |
|---|---|---|---|
| 2008 | 517 095 | 189 393 | **706 489** |
| 2009 | 561 313 | 208 944 | **770 258** |
| 2010 | 564 601 | 227 832 | **792 433** |
| 2011 | 617 135 | 288 611 | **905 747** |
| 2012 | 719 809 | 375 988 | **1 095 797** |
| 2013 | 692 379 | 264 438 | **956 817** |
| 2014 | 719 236 | 239 991 | **959 227** |

(Chap. 16 ci-dessus = budget de l'État hors fonds du Trésor ; totaux arrondis au kDT ;
calcul brut en dinars ci-dessous § 1.4.) **Sept points continus, même source, même périmètre,
même unité.** C'est la série d'exécution avant-2014 — elle **prolonge vers l'arrière** la série B
des PAP (2014-2018) dans la **même famille de périmètre** (ministère, Titre 1 + Titre 2), mais
en **exécution** (≠ prévision des PAP : ne pas chaîner en silence, deux familles).

### 1.3 Variante « toutes ressources » (budget + fonds du Trésor)

Pour mémoire, exécution payé 16+17 **fonds du Trésor compris** (fonds spéciaux + fonds de
concours gérés par le ministère), même source :
2008 = 729 162 ; 2009 = 806 990 ; 2010 = 824 049 ; 2011 = 942 088 ; 2012 = 1 128 329 ;
2013 = 1 000 139 ; 2014 = 1 004 575 (kDT). **Ne pas mélanger** avec la série § 1.2 : les fonds du
Trésor (FOSDAP, fonds de concours) sont un périmètre plus large. Les deux colonnes sont
disponibles ; la série § 1.2 (budget de l'État seul) est la plus comparable aux PAP.

### 1.4 Split Titre 1 / Titre 2 (budget de l'État, chap. 16+17, payé, DT)

| Gestion | Titre 1 (courantes) | Titre 2 (développement) |
|---|---|---|
| 2008 | 216 955 424 | 489 533 301 |
| 2013 | 407 694 256 | 549 123 187 |
| 2014 | 425 156 240 | 534 070 738 |

(Chap. 17 n'apporte que du Titre 2 dans BOOST ; la masse salariale des CRDA est portée par le
chap. 16 — à garder en tête si l'on veut la seule « gestion » du ministère.) Détail complet
réextractible : voir § 4.

### 1.5 Caveats

- **2015-2016 exclus de la série** : BOOST n'a le payé complet que **2008-2014** (fiche
  `mizaniatouna-boost.md` : « payé fiable 2008-2014 ; 2015 partiel ; 2016 très partiel »).
  Agriculture 2015 payé (budget État 16+17) = 1 050 033 kDT paraît complet mais l'exécution
  globale 2015 est tronquée dans BOOST : **à confirmer avant usage**. 2016 (201 632 kDT) est
  manifestement partiel — **à écarter**.
- **BOOST est une compilation officielle**, pas le Journal officiel : source secondaire du
  ministère des Finances. Pour un chiffre à citer au mot près, le cross-check primaire est le
  **décret de répartition des crédits** (prévision) et la **loi de règlement** (exécution) — voir
  § 2 : leur détail par ministère n'est **pas dans la couche texte** du JORT.

---

## 2. Pourquoi le pré-2008 (et le primaire) reste un trou cadré

### 2.1 Les lois de règlement ne donnent pas le ministère

Vérifié sur la **loi n° 2013-6 du 15 janvier 2013 (règlement de la gestion 2009)**, JORT n° 7
du 22 janvier 2013, p. 357-358 (corpus `PDFs-legislation-tunisie`, `PDFs/JORT/2013/fr/Jo0072013.pdf`) :
les articles règlent le budget par **Titre et Section** (Titre I 10 470 831 072,937 DT ; Titre II
5 430 823 647,112 DT ; fonds du Trésor 961 110 712,592 DT), la répartition par ministère étant
renvoyée aux « **tableaux n° 2, 2-1 et 2-2 annexés** » — **non reproduits dans le texte du JORT**.
Le constat de la note mère (§ 2.4) est confirmé : **le budget du seul ministère de l'Agriculture
ne ressort pas** des lois de règlement publiées. Les lois de règlement disponibles dans le corpus
couvrent les gestions 1954-55 → 2009 (puis 2022), publiées 1966 → 2024.

### 2.2 Les décrets de répartition des crédits donnent le ministère — mais en image

La **prévision par ministère** vit dans le **décret de répartition des crédits** qui suit chaque
loi de finances (tableau « A » = Titre I par parties/articles ; tableaux « B » et « C » = Titre II).
Exemple : **décret n° 2009-3750 du 21 décembre 2009** (répartition des crédits de la LF 2010,
`loi n° 2009-71`), JORT n° 102 du 22 décembre 2009, p. 4111 sq.
(`PDFs/JORT/2009/fr/Jo1022009.pdf`). **Les tableaux A/B/C existent mais sont des pages-image**
(p. 4112-4144 : couche texte vide, seuls les bandeaux de page subsistent). Le total du chapitre
« Ministère de l'Agriculture et des Ressources Hydrauliques » **n'est donc pas lisible sans OCR**.

→ **Chemin de collecte pré-2008** (prévision) : OCR du tableau « A » (ligne de récapitulation du
chapitre Agriculture, Titre I) et des tableaux « B »/« C » (Titre II) des décrets de répartition
annuels, depuis le JORT du corpus. Tâche définie et rejouable (fiche § 5), rendement à évaluer.

---

## 3. Références CSL candidates

Toutes déjà dans `tunisia-data` ou le corpus JORT local ; aucune collecte nouvelle. À créer dans
le `references.json` du volume « agriculture » :

```json
[
  {
    "id": "boost-tunisie-minfin-bm",
    "citation-key": "boost-tunisie-minfin-bm",
    "type": "dataset",
    "title": "Base BOOST Tunisie — dépenses de l'État par ligne budgétaire (2008-2016)",
    "author": [{"literal": "Ministère des Finances (Tunisie)"}, {"literal": "Banque mondiale"}],
    "issued": {"date-parts": [[2016]]},
    "publisher": "Portail du budget citoyen mizaniatouna.gov.tn",
    "URL": "http://www.mizaniatouna.gov.tn/tunisia/template_fr/boost_fr.xlsx",
    "archive": "Internet Archive (Wayback Machine)",
    "archive_location": "web/20220623104208",
    "accessed": {"date-parts": [[2026, 11, 10]]},
    "note": "Portail d'origine hors service (HTTP 503) ; copie Wayback. Chapitres ADMIN2 16 (Ministère de l'Agriculture) et 17 (CRDA). Payé fiable 2008-2014."
  },
  {
    "id": "tn-loi-2013-6-reglement-2009",
    "citation-key": "tn-loi-2013-6-reglement-2009",
    "type": "legislation",
    "title": "Loi n° 2013-6 du 15 janvier 2013, portant règlement du budget de l'État de la gestion 2009",
    "issued": {"date-parts": [[2013, 1, 15]]},
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "7",
    "page": "356-358",
    "note": "Règlement par Titre et Section ; répartition par ministère renvoyée aux tableaux n° 2/2-1/2-2 non reproduits au JORT."
  },
  {
    "id": "tn-decret-2009-3750-repartition-credits-2010",
    "citation-key": "tn-decret-2009-3750-repartition-credits-2010",
    "type": "legislation",
    "title": "Décret n° 2009-3750 du 21 décembre 2009, portant répartition des crédits du budget de l'État ouverts par la loi n° 2009-71 (loi de finances pour 2010)",
    "issued": {"date-parts": [[2009, 12, 21]]},
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "102",
    "page": "4111-4144",
    "note": "Tableaux A (Titre I) et B/C (Titre II) par ministère = pages-image, OCR requis pour le total du chapitre Agriculture."
  }
]
```

---

## 4. Reproduire l'extraction

Classeur BOOST déjà catalogué ; relevé rejouable (3-4 min) :

```
cd ~/projets/tunisia-data
uv run python - <<'PY'
import openpyxl
from collections import defaultdict
wb=openpyxl.load_workbook('data/raw/mizaniatouna/boost_fr.xlsx', read_only=True)
ws=wb['Sheet1']; rows=ws.iter_rows(values_only=True); next(rows)
num=lambda x:(float(x) if str(x).replace('.','',1).replace('-','',1).isdigit() else 0.0)
B=defaultdict(float)   # (year) -> payé budget-only chap16+17, Titre1+2
for r in rows:
    a2=str(r[4])
    if (a2[:2] in ('16','17')) and str(r[1]).startswith('01') and ('Titre' in str(r[5])):
        B[r[0]]+=num(r[17])          # col 17 = PAYE ; col 14 = LOI DE FINANCE ; col 16 = ORDONNANCE
for y in range(2008,2015): print(y, round(B[y]))
PY
```

Colonnes utiles : 0 YEAR, 1 TYPE (01 BUDGET / 02 FONDS DU TRESOR), 4 ADMIN2, 5 ECON1 (Titre),
14 LOI DE FINANCE (votée, exploitable 2013-2016 seulement), 16 ORDONNANCE, 17 PAYÉ.

---

## 5. Recherches infructueuses / fiche à mettre à jour

La fiche **`r-agri-budget-ministere-avant-2014`** est citée par `_depense.qmd` (l. 104) et la note
mère mais **n'est pas encore enregistrée dans `docs/recherches.yml`**. Fiche proposée, à créer,
avec la passe du jour (partiellement résolutive) :

```yaml
- id: r-agri-budget-ministere-avant-2014
  objet: >-
    budget du ministère de l'Agriculture (chap. 16) et des commissariats régionaux au
    développement agricole (chap. 17) avant 2014 — total par gestion, moyens de l'État,
    Titre I (gestion) + Titre II (développement)
  ou:
    - base BOOST Tunisie (mizaniatouna, minfin + Banque mondiale), data/raw/mizaniatouna/boost_fr.xlsx
    - décrets de répartition des crédits (tableaux A/B/C par ministère), JORT, corpus PDFs-legislation-tunisie
    - lois de règlement du budget de l'État (tableaux n° 2 annexés), JORT
  ancre: precis/fr/agriculture/_depense.qmd:104
  passes:
    - date: 2026-11-13
      resultat: partiel
      trouve:
        - "Exécution (payé) 2008-2014 : série homogène chap. 16+17, budget de l'État, Titre I+II, via BOOST (fiche mizaniatouna-boost). Validée vs PAP 2015 (2014 : 959 227 vs 967 456 kDT) et PAP 2017 (LF 2016 identique)."
      couverture: >-
        exécution ministère 2008-2014 obtenue ; 2015 partiel (à confirmer), 2016 écarté ;
        AVANT 2008 : non couvert (BOOST démarre en 2008). Lois de règlement lues (gestion 2009,
        loi 2013-6) : règlent par Titre/Section, détail ministère en tableaux annexés NON
        reproduits au JORT. Décrets de répartition des crédits (ex. 2009-3750) : tableaux A/B/C
        par ministère présents mais en pages-image (OCR requis), non dépouillés.
      couvert_jusqu_au: 2014-12-31
      sources: [boost_fr.xlsx, jort_cache, PDFs-legislation-tunisie]
  reste_a_faire:
    - OCR du total du chapitre Agriculture (Titre I, tableau A ; Titre II, tableaux B/C) des décrets de répartition des crédits, gestions < 2008, pour une série de prévision primaire remontant avant BOOST.
    - confirmer la complétude du payé BOOST 2015 (exécution globale tronquée) avant tout usage.
```

Aucune recherche web n'a été nécessaire (matière intégralement dans `tunisia-data` et le corpus
JORT local) ; aucun PDF nouveau téléchargé, donc rien à indexer.

---

## 6. Backlog

- **Report au backlog précis** (destination durable, non modifiée ici) : la série d'exécution
  2008-2014 ci-dessus est prête à chaîner — en **famille exécution** — avec la série C (RAP
  2019-2020) de la note mère, le trou 2015-2018 en exécution restant ouvert. À verser au suivi
  des séries budgétaires du chapitre 3.
- **Trou résiduel pré-2008** : prévision par ministère reconstituable par OCR des décrets de
  répartition (chemin § 2.2) — tâche à ouvrir si le propos du chapitre exige une profondeur
  antérieure à 2008 ; sinon, trou honnête borné à « avant 2008 ».
- **2015 à confirmer** : lever le doute sur le payé BOOST 2015 (recoupement loi de règlement
  2015 quand publiée / RAP 2015 si acquis).
- **Fiche `r-agri-budget-ministere-avant-2014`** à enregistrer formellement dans
  `docs/recherches.yml` (bloc § 5) — elle n'existe aujourd'hui que par mention.

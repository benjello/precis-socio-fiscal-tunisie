# Les accords salariaux du secteur public — note documentaire

> Recopie, le 5 octobre 2026, de la partie « secteur public » de la note du documentaliste
> du même jour sur les négociations salariales (la partie « secteur privé » relève du volume
> « Le marché du travail » et n'est pas reprise ici). Décision de l'humain : les accords
> salariaux UGTT-gouvernement vont au volume « Rémunérations dans le secteur public ».
> Marqueurs internes : **[T]** lu au fascicule ; **[M]** notice `jort_cache.db` ; **[D]** dérivé ;
> **[U]** source UGTT seule. La section 3 consigne ce que la rédaction a lu ensuite.

## 0. Les textes du secteur public cités par la note d'origine (§ a.2, famille 3)

Décrets « portant approbation des augmentations des salaires » des entreprises publiques
régies par le statut général — leurs titres datent les rounds : 91-246 (n° 15/1991, p. 328),
94-1223 (n° 44/1994, p. 936), 97-2309 (n° 98/1997, pp. 2164-2165) ; pour la fonction publique,
les décrets 96-1907 et suivants fixent « l'augmentation globale des salaires durant la période
1996-1998 » ; 2001-1997 (« période 1999-2001 », n° 70/2001), 2003-1932 (« 2002-2004 »,
n° 73/2003), 2007-825 (« 2005-2007 », n° 29/2007), 2010-1176 (« 2008-2010 », n° 43/2010),
2013-4159 (« 2011-2012 », n° 82/2013), 2026-64 (n° 44/2026) **[M]**.

## (b) Secteur public — pour « Rémunérations dans le secteur public »

### b.1 Ce que le volume dit déjà

- `_regime_indiciaire.qmd`, § « Les cycles de revalorisation salariale »
  (`#sec-cycles-revalorisation`) : principe (l'accord n'a pas d'effet de droit sans décret, loi
  n° 83-112 art. 13), tableau des cycles et grille des montants engendrés depuis
  `augmentations/augmentations-fonction-publique.csv` (108 lignes : cycles 2015-2018 — 2015-462,
  2016-1 ; 2019-2020 — 2019-209, 2019-1133, 2020-767 ; 2023-2025 — 2022-797 ; 2026-2028 —
  2026-63), deux figures (nominal et réel), encadré du PV UGTT du 14 sept. 2022
  (`ugtt-pv-augmentation-2022`). TODO ouvert : tranches 1996-2012 par corps.
- `_regime_conventionnel.qmd` : rémunération par statuts particuliers ou décret (loi 85-78,
  art. 75) ; **rien** sur les augmentations générales des entreprises publiques.
- `index.qmd` : masse salariale rapportée au PIB et aux dépenses de l'État, 1990-2025
  (`fig-masse-salariale-ratios`) — le poids budgétaire est déjà là.

### b.2 Ce qui manque et où l'insérer

| Matière | Textes | Insertion proposée |
|---|---|---|
| Augmentations des **entreprises publiques** (statut général, loi 85-78) | 91-246, 94-1223, 97-2309, 2001-1997, 2003-1932, 2007-825, 2010-1176, 2013-4159, 2026-64 **[M]** | section propre dans `_regime_conventionnel.qmd`, après « La construction de la rémunération » ; même format que le CSV de la fonction publique |
| Magistrats | 2019-1132, 2026-65 **[M]** | absents du CSV (clé `decret2026-65` existante) ; `_regime_statutaire_autonome.qmd` |
| Cycles **avant 2015** de la fonction publique | 96-1907 à 96-2410 (octobre-décembre 1996, « fixation de l'augmentation globale des salaires durant la période 1996-… », un décret par corps) **[M]** | prolongement amont du § des cycles (le TODO existant) |
| Accord **6 février 2021** et PV 2022 (25 % mai 2022, 25 % mai 2023, 50 % mai 2024 ; SMIG +7 % au 1er oct. 2022) **[U]** | décret SMIG 2022-769 : 429,312 → 459,264 D, **+6,98 %** **[T]/[D]** | encadré existant ; le décret reste la source opposable |
| Accords sectoriels publics (enseignement 2019, contractuels 2017) | `data/ugtt/fonction_publique/` **[U]** | hors champ des augmentations générales ; ne pas reprendre sans décret |

Recommandation : **pas de chapitre transversal nouveau** — le § des cycles du régime indiciaire
existe et porte déjà figures et CSV ; ajouter une section « augmentations générales » au chapitre
du régime conventionnel pour les entreprises publiques, et un renvoi croisé entre les deux.


## 3. Lecture au fascicule (rédaction, 5 octobre 2026)

Tous les textes ci-dessous sont lus au fascicule français du corpus local
(`PDFs/JORT/<année>/fr/`), couche texte décodée au besoin, tableaux relus à l'image ;
93-2062 et 91-246 sont des scans, lus à l'image **[T]**.

### 3.1 Indemnité de gestion et d'exécution (fonction publique), 1993-2013

Relevé complet : `precis/fr/remunerations_publiques/augmentations/augmentations-ige.csv`
(et son manifeste). Pour chaque cycle triennal, la somme des trois tranches retrouve le
montant global fixé par le premier décret (contrôle dans `tests/test_augmentations.py`).

| Cycle | Décrets | Effet des tranches | Global A1 → D (ouvriers 3e → 1re) |
|---|---|---|---|
| 1993-1995 | 93-2062 (trois tranches dans un seul décret) | 1er juillet 1993, 1994, 1995 | 95, A2 86, A3 72, B 56, C 45, D 40 (56, 45, 40) |
| 1996-1998 | 96-1907, 97-1174, 98-1292 | 1er juillet 1996, 1997, 1998 | 90, 80, 70, 55, 45, 40 (55, 45, 40) |
| 1999-2001 | 99-2015, 2000-1199, 2001-1557 | 1er juillet 1999, 2000, 2001 | 95, 85, 75, 60, 50, 45 (60, 50, 45) |
| 2002-2004 | 2002-2672, 2003-1568, 2004-1538 | 1er juillet 2002, 2003, 2004 | 92, 82,5, 72,5, 58, 48,5, 43,5 (idem) |
| 2005-2007 | 2005-3137, 2006-2182, 2007-1671 | 1er juillet 2005, 2006, 2007 | 92, 82,5, 72,5, 58, 48,5, 43,5 (idem) |
| 2008-2010 | 2008-4047, 2009-2145, 2010-1973 | 1er juillet 2008, 2009, 2010 | A1 226 / 197 / 168 selon le grade, A2 124, A3 109, B 87, C 73, D 66 (87, 73, 66) |
| 2012 | 2012-2959 | 1er juillet 2012 ; 1er janvier 2013 | 35 + 35 D, uniforme |

Remarques :
- 93-2062 : l'intitulé du fascicule porte « décret n° 82-505 du 16 mars 1982 » (la notice : 15 mars).
- 2006-2183 du 7 août 2006 refixe les montants de l'IGE des grades de A1 (689,5 / 650 / 611 D
  au 1er août 2006) : restructuration, non retenue comme augmentation générale.
- 2008-4047, art. 3 : imputation de l'avance servie par le décret n° 2008-299 du 29 août 2008
  (le visa porte « 2008-229 »).
- **2011** : aucune majoration de l'IGE identifiée (fiche `r-ige-2011`).
- Hors champ du relevé : chaque autre corps a son décret parallèle (ex. 98-1293, indemnité
  d'ingénierie : 50 / 44 / 38 / 33 / 30 D au 1er juillet 1998 ; 2000-1200, indemnité
  d'architecture). Non relevés.
- Non lus : 90-1001 et 91-803 (modifications du décret 82-505, cycle 1990-1992 ?).

### 3.2 Entreprises publiques (loi n° 85-78)

| Décret | JORT (FR) | Période | Contenu |
|---|---|---|---|
| 91-246 du 11 févr. 1991 | n° 15, 22 févr. 1991, p. 328 | non énoncée | approbation des augmentations « arrêtées par la commission supérieure des négociations sociales » ; art. 2 : augmentations de la fonction publique non applicables |
| 94-1223 du 16 mai 1994 | n° 44, 7 juin 1994, p. 936 | non énoncée | approbation (commission supérieure de supervision et de coordination) ; art. 2 : interdiction de toute indemnité ou avantage nouveau |
| 97-2309 du 1er déc. 1997 | n° 98, 9 déc. 1997, pp. 2164-2165 | 1996-1998 | approbation ; visa du communiqué conjoint PM-UGTT du 20 juin 1996 |
| 2001-1997 du 27 août 2001 | n° 70, 31 août 2001, pp. 2770-2771 | 1999-2001 | approbation ; art. 3 primes annuelles ; art. 4 FP non applicable ; visa du communiqué conjoint du 1er juin 1999 |
| 2003-1932 du 8 sept. 2003 | n° 73, 12 sept. 2003, pp. 2748-2749 | 2002-2004 | approbation ; art. 2 interdiction étendue aux salaires ; art. 4 non-cumul |
| 2007-825 du 2 avril 2007 | n° 29, 10 avril 2007, pp. 1116-1117 | 2005-2007 | approbation ; art. 2 étendu aux avantages en nature et sociaux |
| 2010-1176 du 24 mai 2010 | n° 43, 28 mai 2010, pp. 1532-1533 | 2008-2010 | approbation, mêmes règles |
| 2013-4159 du 25 sept. 2013 | n° 82, 11 et 15 oct. 2013, pp. 2974-2975 | 2011-2012 | approbation des augmentations « arrêtées conformément à la réglementation en vigueur » |
| 2026-64 du 30 avril 2026 | n° 44, 30 avril 2026, pp. 834-835 (la notice : 832-834) | 2026-2028 | montants au 1er janv. 2026 / 2027 / 2028 : cadre 120 / 120 / 120 ; maîtrise 100 / 105 / 105 ; exécution 90 / 90 / 90 D ; art. 2 indemnité « Augmentation de salaires pour les années 2026-2027-2028 », hors primes annuelles ; art. 3 soumise aux cotisations ; art. 4 « L'augmentation des pensions des retraités intervient conformément à la législation en vigueur » |

Constats : aucun décret de 1991 à 2013 ne publie de montant (fiche `r-montants-ep-commission`) ;
aucun décret identifié entre 2013-4159 et 2026-64 (fiche `r-augmentations-ep-2013-2025`).
Aucun poids budgétaire par cycle n'est donné par ces textes : rien n'est publié à ce titre.

### 3.3 Références versées

Nouvelles clés (FR et AR, `precis/*/references.json`) : `decret93-2062`, `decret97-1174`,
`decret98-1292`, `decret91-246`, `decret94-1223`, `decret97-2309`, `decret2001-1997`,
`decret2003-1932`, `decret2007-825`, `decret2010-1176`, `decret2013-4159`, `decret2026-64`.
Notes mises à jour (montants lus) : les quatorze clés de l'IGE de `decret96-1907` à
`decret2012-2959`.

## 4. Références et termes de la note d'origine (partie publique)

Existantes : `decret-2022-797`, `decret2026-63`, `decret2026-65`, `decret2022-769`,
`ugtt-pv-augmentation-2022` (remunerations_publiques).

| FR | AR | Source |
|---|---|---|
| négociations sociales | المفاوضات الاجتماعية | UGTT (catégorie du site) [U] — à confirmer par un texte officiel |
| augmentation des salaires | الزيادة في الأجور / الترفيع في الأجور | titres arabes [M] |
| procès-verbal d'accord | محضر اتفاق | PV 2022 [U] |

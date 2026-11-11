# Série (3) — Prolongation de la série CNSS après 2004 : note documentaire

> Note documentaire (rôle documentaliste), 10 novembre 2026. Instruit la série (3) du § 3 de
> `cadre-budgetaire-comptable-caisses.md` : recettes, dépenses, solde (et réserves si possible) de
> la CNSS, par année, 2005 → le plus récent, en continuité de définition avec la rétrospective
> financière 1990-2004 (`cnss-retrospective-1990-2004`, série tunisia-data
> `cnss-retrospective-ressources-emplois`). Rien n'a été téléchargé dans un dépôt ; tout le
> matériau cité est **déjà** dans l'entrepôt `tunisia-data` (lecture seule), sauf mention. Aucun
> fichier du précis ni de `tunisia-data` n'a été modifié.
>
> Conventions : **[S]** source lue ; **[D]** déduction de la note. « mD » = milliers de dinars,
> « MD » = millions de dinars, courants. URL cnss.tn et ins.tn vérifiées le 10 novembre 2026
> (`curl -k` : 200, `application/pdf`) quand la note le dit.

---

## 1. Verdict de couverture

**La couverture 2005-2023 est atteignable sans approximation, mais pas d'une seule source ni d'un
seul niveau de détail.** Trois familles emboîtées, toutes dérivées des **états financiers (bilans)
de la CNSS** — donc de la même famille comptable que la rétrospective 1990-2004 (« Source :
Bilans ») :

1. **« La CNSS en chiffres », tableaux 8-9 / 11-12** (déjà dans l'entrepôt,
   `data/raw/caisses/cnss/2020/` et `2018/`) : **produits techniques** (« évolution des
   cotisations ») et **charges techniques** (« évolution des dépenses de prestations servies »),
   ensemble des régimes, **année par année 2000-2020**, en MD. C'est la série la plus longue et la
   plus homogène disponible pour recettes et dépenses après 2004 — sans trou.
2. **Annuaires statistiques CNSS** (éditions 2006, 2010, 2013, 2016, 2017, 2018 dans l'entrepôt) :
   page « Évolution des principaux indicateurs » (ressources et emplois **des branches gérées**,
   cotisations et dépenses techniques, deux années par édition) ; tableaux financiers multi-années
   (prestations en nature des assurances sociales 2000-N, pensions par nature 2000-N,
   investissements et placements 2000-N) ; tableau « Répartition des dépenses techniques » de
   l'année N dans la nomenclature exacte de la rétrospective (PF / AS / pensions / PST, variantes
   avec/sans CTF et RC).
3. **Résultat de l'exercice (solde)** : états financiers CNSS 2017-2018 (publiés par la caisse,
   dans l'entrepôt), récapitulatif du budget 2022 (« Bilan 2020 »), et rapport sur les entreprises
   publiques du ministère des Finances (clés `minfin-ep*`, éditions LF 2020 à LF 2025) pour
   2016-2023.

**Trous honnêtes du solde : 2005-2008, 2011, 2014** (détail § 4) — les annuaires de ces années ne
sont pas dans l'entrepôt et la Wayback Machine était hors ligne le jour de la recherche (§ 9). Le
**détail par régime** (comptes de compensation de la loi n° 60-30, art. 22), qui fait la richesse
de la rétrospective, **n'est publié nulle part après 2004** : lacune de fond (§ 8, L-s3.1).

**Rupture majeure de périmètre : la CNAM (2007-2008).** Ce que « dépenses CNSS » recouvre change
quand les prestations maladie passent à la CNAM (§ 5). Les deux tronçons ne se raccordent pas en
silence ; la rupture est datée et visible dans les tableaux mêmes de la caisse.

## 2. Définitions : ce que trace le précis 1990-2004, et ce qui le prolonge

### 2.1 La série existante

`precis/fr/caisses/_comptes_longue_periode.qmd` (figures `fig-cnss-regimes`,
`fig-cnss-atmp-pst`, `fig-cnss-assurances-sociales`, scripts
`precis/fr/caisses/figures/cnss_*.py`) lit la série tunisia-data
**`cnss-retrospective-ressources-emplois`**
(`data/processed/caisses/cnss_retrospective_1990_2004.csv`). Grandeurs tracées, par régime et par
branche, 1990-2004, en **mD courants**, « comptes de bilan » (droits constatés) :

- **total des ressources** d'un régime/d'une branche = cotisations + produits financiers + autres
  produits ;
- **total des emplois** = prestations (« dépenses techniques ») + frais de gestion + charges de
  structure (+ provisions AT) ;
- **résultat de gestion** = ressources − emplois ;
- agrégat « ensemble des régimes » en variantes avec/sans CTF, avec/sans RC, AT-MP et PST inclus
  à partir de 1995 et 1997.

### 2.2 Les grandeurs qui le prolongent (nomenclature CNSS actuelle)

Les états financiers de la CNSS (notes aux états financiers, `data/raw/caisses/cnss/2018/etat2018.pdf`) **[S]** définissent :

- **produits techniques** = « montant net constaté des cotisations en principal sans T.O. et
  montant net recouvré des cotisations en taxation d'office et en pénalités » — c'est la ligne
  « cotisations » au sens large ;
- **charges techniques** = « prestations familiales, assurances sociales (indemnités de décès et
  capital décès), prestations de vieillesse, d'invalidité et de survivants, prestations du régime
  de protection sociale et actions sanitaires aux pensionnés ainsi que les actions sociales » —
  c'est « dépenses techniques » = les prestations, **hors frais de gestion** ;
- **charges administratives** = frais de gestion (personnel, services extérieurs,
  amortissements) ;
- **résultat de l'exercice** = marge technique − provisions ± placements, polycliniques,
  facturation à la CNAM, charges administratives, autres éléments ordinaires.

**Correspondance vérifiée** entre les trois présentations, sur les années de recouvrement **[S]** :

| Grandeur | États financiers 2018/2017 | Annuaire 2018, « principaux indicateurs » | Écart |
|---|---|---|---|
| charges techniques 2017 | 3 088 014 mD | « dépenses techniques » 3 088 014 mD | 0 |
| charges techniques 2018 | 3 411 951 mD | 3 411 951 mD | 0 |
| résultat de l'exercice 2017 | −525 000 mD | ressources 2 839 587 − emplois 3 364 586 = **−524 999** | 1 mD |
| résultat de l'exercice 2018 | −530 464 mD | 3 130 659 − 3 661 123 = **−530 464** | 0 |
| produits techniques 2017 | 2 794 297 mD | cotisations « 2 774 188 mD » | 20 109 mD (cotisations hors TO/pénalités) **[D]** |

Donc : la paire « **ressources / emplois des branches gérées** » des pages d'indicateurs des
annuaires **est** (au mD près) la paire dont la différence donne le **résultat de l'exercice** —
c'est l'héritière directe du couple ressources/emplois « ensemble des régimes » de la
rétrospective. Et le « tableau 11 » de « La CNSS en chiffres » (« évolution des cotisations »),
dont les valeurs 2016-2020 (2 520, 2 794, 3 080, 3 445, 3 430 MD) coïncident avec les **produits
techniques** des états financiers et du rapport entreprises publiques, est en fait la série des
**produits techniques**, pas des seules cotisations hors TO **[D]** (à trancher à l'extraction).

**Ce qui ne se prolonge pas à l'identique** : la rétrospective inclut les produits financiers dans
les ressources de chaque branche et détaille les frais de gestion par régime ; les produits des
placements, devenus minimes (46,5 MD en 2018 contre 71,8 MD pour la seule branche pensions en
1996), sont désormais sous la marge technique. L'écart de définition est petit mais réel : à
documenter dans la note de concordance, pas à gommer.

## 3. Les sources, une par une

### 3.1 « La CNSS en chiffres » (dans l'entrepôt ; clé `cnss-chiffres`)

- `data/raw/caisses/cnss/2020/11_Evolution_des_recettes.pdf` : « Évolution des cotisations CNSS
  (ensemble des régimes) », **2000-2020**, MD, un point par année, couche texte **[S]**. URL
  `https://www.cnss.tn/fr/c/document_library/get_file?uuid=9d938c6b-42b9-400f-a29b-77ee650da69d&groupId=10156`
  — vérifiée le 10 novembre 2026 (200, `application/pdf`, 448 714 octets).
- `data/raw/caisses/cnss/2020/12_Évolution_des_dépenses_des_régimes_de_sécurité_s.pdf` :
  « Évolution des dépenses de prestations servies », **2000-2020**, MD, barres empilées avec
  détail par branche les dernières années (2019 : 3 811,3 ; 2020 : 4 184,0 — égal aux charges
  techniques du récapitulatif budgétaire) **[S]**.
- Jumeaux du millésime 2018/2019 (`2018/tab8-ar.pdf`, `Tab9-fr.pdf`…) : mêmes séries arrêtées à
  2019 — recouvrement de contrôle.
- Le site (page « La CNSS en chiffres », consultée le 10 novembre 2026) n'a **rien de plus
  récent** : dernière mise à jour affichée 04/01/2022, mêmes UUID que la collecte du 18 septembre
  2026. Les séries de la caisse s'arrêtent à 2020.

### 3.2 États financiers CNSS 2018/2017 (dans l'entrepôt ; clé à créer `cnss-etats-financiers-2018`)

`data/raw/caisses/cnss/2020/01_Etats_Financiers.pdf` (4 p., français : bilan, état de résultat,
flux de trésorerie) + `02_Note_explicative_des_Etats_financiers.pdf` ;
version arabe `2018/publication_2018_en_arabe_(1).pdf` ; notes `2018/etat2018.pdf` **[S]**.
Ce sont les **seuls états financiers publiés par la caisse** (exercices 2018 et 2017). Valeurs
clés (mD) : produits techniques 3 079 699 (2018) / 2 794 297 (2017) ; charges techniques
−3 411 951 / −3 088 014 ; résultat −530 464 / −525 000 ; **capitaux propres −383 521 au
31.12.2018** (réserves 146 943 + résultat), **négatifs pour la première fois** (rapport EP LF 2021 :
« pour la première fois dans l'histoire de la caisse un solde négatif de 384 MD ») ; **comptes
courants CNAM au passif : 3 037 816** (2018) / 2 407 345 (2017) — la dette envers la CNAM finance
la trésorerie (§ 5.3).

### 3.3 Récapitulatif général du budget 2022 (dans l'entrepôt ; même famille `cnss-chiffres`)

`data/raw/caisses/cnss/2020/03_Budget.pdf` (1 p.) **[S]** : colonnes **Bilan 2020**, Budget 2021,
Probable 2021, Budget 2022, en mD. Bilan 2020 : produits techniques 3 430 021 ; charges techniques
−4 184 018 ; **résultat de l'exercice −1 091 500**. Probable 2021 : −1 448 928 (le réalisé sera
−1 274,3 MD, § 3.5 — l'écart mesure la qualité du « probable »).

### 3.4 Annuaires statistiques CNSS (dans l'entrepôt ; clé à créer `cnss-annuaire-statistique`)

`data/raw/caisses/cnss/annuaires/` (fiche `sources/cnss-annuaires.md`, catalogue
`sources/cnss-urls.csv`). Pour chaque édition, trois objets utiles à la série :

| Édition | Page « principaux indicateurs » (ressources/emplois, cotisations/dépenses techniques, 2 années) | Tableaux financiers multi-années | Source imprimée |
|---|---|---|---|
| 2006 (scan fr, 201 p., sans couche texte) | à vérifier à l'image/OCR — attendu : 2005-2006 | AS en nature 1970(?)-2006 ; pensions 1980-2006 ; placements ? | — (à lire) |
| 2010 (ar, PDF 19) | 2009 : ressources 1 474 677, emplois 1 467 852 ; 2010 : 1 582 683 / 1 575 724 ; cotisations 1 369 208 → 1 489 769 ; dépenses techniques 1 322 290 → 1 457 199 | placements (PDF ~250) | **« موازنة الصندوق لسنة 2010 »** (budget, pas bilan — réserve § 4) |
| 2013 (fr, PDF 23) | 2012 : 1 915 711 / 1 993 829 ; 2013 : 2 142 716 / 2 214 618 ; cotisations 1 835 749 → 2 059 612 ; dépenses techniques 1 805 190 → 1 992 235 | placements 2000-2013 (p. impr. 351) ; AS en nature 2000-2013 ; dépenses techniques 2013 par branche (p. impr. 359) | **« Bilan CNSS 2013 »** |
| 2016 (ar, PDF 23) | 2015 : 2 354 193 / 2 796 921 ; 2016 : 2 537 131 / 3 012 421 ; cotisations 2 228 589 → 2 506 592 ; dépenses techniques 2 493 560 → … | idem, 2000-2016 | « موازنة الصندوق 2015 و 2016 » |
| 2017 (ar, PDF 20) | 2016 : 2 537 131 / 3 012 421 ; 2017 : 2 839 587 / 3 364 586 ; cotisations 2 506 592 → 2 774 188 ; dépenses techniques 2 788 913 → 3 088 014 | idem, 2000-2017 | « موازنة الصندوق لسنة 2017 » |
| 2018 (fr, PDF 8) | 2017 : 2 839 587 / 3 364 586 ; 2018 : 3 130 659 / 3 661 123 ; cotisations 3 059 674 ; dépenses techniques 3 411 951 | placements 2010-2018 (p. impr. 379) ; AS en nature 2000-2018 (p. 354) ; recettes/dépenses polycliniques 2010-2018 (p. 355) ; dépenses techniques 2018 par branche (p. 385) ; pensions par nature et par régime 2000-2018 (p. 43-44 et parties par régime) | « Etats Financiers » |

Lecture croisée : les valeurs 2016 et 2017 coïncident exactement entre éditions 2016/2017/2018, et
avec les états financiers pour 2017-2018 — même famille, chiffres stables. Les tableaux
multi-années de l'édition 2018 donnent, à eux seuls, les **dépenses par branche 2005-2018**
(pensions par nature 2000-2018 ; AS en nature 2000-2018 ; prestations en espèces ; PF par régime) :
le versant « emplois techniques » est couvert sans trou, dans la nomenclature de la rétrospective.
Divergences inter-éditions constatées (placements 2013 : marché monétaire 410 047 mD dans
l'édition 2013, 399 500 dans l'édition 2018) : conserver par édition, comme pour les annuaires
démographiques (règle de `cnss-annuaires.md`).

### 3.5 Rapport sur les entreprises publiques, ministère des Finances (dans l'entrepôt ; clés `minfin-ep*`)

`data/raw/caisses/minfin/` (fiches `sources/minfin-entreprises-publiques-caisses.md` et
`sources/minfin-ep-cnrps-finances.md` — la méthode d'extraction par géométrie, validée pour la
CNRPS, se transpose au bloc CNSS des mêmes pages). Chapitre « caisses sociales » **[S]** :

- **LF 2020** (fr, pp. 38-41) : CNSS 2016-2017 réalisés + prévision 2018. Produits techniques
  2 520 MD (2016) → 2 794 (2017) ; charges techniques 2 789 → 3 088 ; résultat d'exploitation
  −477 → −527 ; **résultat net −475 (2016) → −525 (2017)** ; dette envers la CNAM 499 (2016) →
  1 247 MD (2017) « à partir de 2016, [incapacité] de verser … la totalité des contributions
  payées pour le compte de la CNAM afin d'épargner les liquidités nécessaires pour les pensions ».
- **LF 2021** (fr, pp. ~50) : CNSS 2018 réalisé (résultat net −530 ; fonds propres −384 MD,
  « première fois ») + prévision 2019 (−700).
- **LF 2022** (ar, tableau p. 46) et **LF 2023** (ar, p. 78) : CNSS 2018-2020 réalisés (**2019 y
  compris**) ; la colonne 2021 de la CNSS est vide dans la LF 2023 (données non transmises, note
  du rapport).
- **LF 2024** (ar, tableau pp. ~68) : CNSS **2021 réalisé : résultat net −1 274,3 MD** (contre
  −1 091,5 en 2020) ; **2022 : −961,5 MD** ; lignes complètes (produits 3 749,2 ; charges ;
  subventions ; endettement 8 664,2 → 9 972,7 MD).
- **LF 2025** (ar, tableau pp. ~44) : 2021 réalisé (identique), **2023 provisoire : −911,1 MD**.

C'est la **seule source identifiée pour le solde 2019-2023** après l'arrêt des publications de la
caisse. L'édition LF 2026, à collecter (gbo.tn / finances.gov.tn), prolongera à 2024.

### 3.6 Recoupement extérieur : comptes des organismes de sécurité sociale (INS)

La série (1) (`caisses-serie-comptes-organismes-notedoc-2026-11-10.md`) donne le S1314 consolidé
(trois caisses) 2001-2025 : cotisations, prestations, **capacité/besoin de financement**. Elle ne
ventile pas par caisse (lacune L-s1.1) mais servira de **contrôle de cohérence** : CNSS + CNRPS
(`minfin-ep`) + CNAM ≈ S1314, écart à documenter.

### 3.7 Réserves (« si possible »)

Pas de série de « fonds de réserve par régime » publiée après 2004. Trois proxys, à présenter
comme tels :
- **tableau « Évolution des investissements et des placements, situation à la fin de
  l'exercice »** des annuaires (« Source : Bilans ») : total des placements **2 408 940 mD (2004)
  → 923 267 (2013)** (édition 2013, p. impr. 351) ; **≈ 239 000 mD (2018)** (édition 2018, p. 379 :
  emprunt national 6 000 + SPROLS 6 981 + marché monétaire 17 984 + titres 116 900 + prêts aux
  assurés 91 228). L'épuisement des réserves placées est la donnée la plus parlante de la période ;
- **capitaux propres** du bilan : 146 972 mD fin 2017, **−383 521 fin 2018**, et, d'après le
  rapport EP LF 2021, résultats accumulés −1 615 MD fin 2018, fonds propres attendus −1 084 MD fin
  2019 ;
- **liquidités** : 265 363 mD fin 2017, 87 516 fin 2018 (état de flux).

## 4. Couverture année par année (recettes / dépenses / solde, ensemble des régimes)

R = produits techniques (« cotisations », MD) ; D = charges techniques ; S = solde. « ⬚ » = trou.
Entre crochets : source — C = `cnss-chiffres` tab. 11-12 (2000-2020) ; A<éd.> = annuaire, page
« indicateurs » ; EF = états financiers 2018/2017 ; B = récapitulatif budget 2022 ; EP<LF> =
rapport entreprises publiques.

| Année | R | D | S (résultat de l'exercice, MD) | Source du solde |
|---|---|---|---|---|
| 2005 | C | C | ⬚ (attendu : annuaire 2006, p. indicateurs, OCR) | — |
| 2006 | C | C | ⬚ (idem) | — |
| 2007 | C | C | ⬚ | — |
| 2008 | C | C | ⬚ | — |
| 2009 | C | C | **+6,8** (1 474 677 − 1 467 852) — source « budget 2010 », pas bilan : fragile | A2010, PDF 19 |
| 2010 | C | C | **+7,0** (1 582 683 − 1 575 724) — idem | A2010, PDF 19 |
| 2011 | C | C | ⬚ | — |
| 2012 | C | C | **−78,1** (« Bilan CNSS 2013 ») | A2013, PDF 23 |
| 2013 | C | C | **−71,9** (id.) | A2013, PDF 23 |
| 2014 | C | C | ⬚ | — |
| 2015 | C | C | **−442,7** (2 354 193 − 2 796 921 ; source « موازنة ») | A2016, PDF 23 |
| 2016 | C | C | **−475** (réalisé) ; recoupé A2016/A2017 (−475,3) | EP LF2020, p. 40 |
| 2017 | C | C | **−525,0** | EF ; EP LF2020 ; A2017/A2018 |
| 2018 | C | C | **−530,5** | EF ; EP LF2021 ; A2018 |
| 2019 | C | C | réalisé au tableau arabe EP LF2022 p. 46 / LF2023 p. 78 (prévision LF2021 : −700) — valeur à lire par géométrie | EP LF2022/LF2023 |
| 2020 | C | C | **−1 091,5** | B (« Bilan 2020 ») ; EP LF2024 |
| 2021 | ⬚ (EP) | ⬚ (EP) | **−1 274,3** (réalisé) | EP LF2024/LF2025 |
| 2022 | EP | EP | **−961,5** (réalisé) | EP LF2024/LF2025 |
| 2023 | EP | EP | **−911,1** (provisoire) | EP LF2025 |
| 2024-2025 | ⬚ | ⬚ | ⬚ — EP LF2026 à collecter | — |

**Les trous se laissent honnêtes.** Pour 2005-2008, 2011, 2014 : ni annuaire dans l'entrepôt, ni
publication de la caisse, ni rapport EP (la série ministérielle commence à la LF 2020, couvrant
2016). Avant d'approximer quoi que ce soit (par exemple interpoler le solde entre 2010 et 2012),
la recherche à finir est : annuaire 2006 (OCR de la page indicateurs, dans l'entrepôt) ; annuaires
2007-2009, 2011-2012, 2014-2015 (Wayback, § 9) ; demande à la CNSS d'une rétrospective 2005-…
(l'exemplaire 1990-2004 venait du centre de documentation du CRES). Si tout échoue, le couple
R − D (tabl. 11-12, complet 2000-2020) donne le **solde technique** chaque année — une grandeur
voisine mais **pas** le résultat (il ignore frais de gestion, provisions et placements) : l'écart
entre les deux, mesurable sur 2009-2010, 2012-2013 et 2015-2020, est de l'ordre de 60 à 350 MD
selon les années — trop grand pour servir d'approximation du résultat sans le dire.

## 5. Ruptures de périmètre — à documenter, jamais à raccorder en silence

### 5.1 La CNAM (2007-2008), la grande rupture

- **Droit** : loi n° 2004-71 (art. 8 : la CNAM gère l'assurance maladie, les régimes AT-MP public
  et privé, « les autres régimes légaux d'assurance maladie ainsi que la gestion des indemnités de
  maladie et de couches » ; art. 10 : transfert des biens et **réserves** afférents ; art. 16 :
  la CNSS **recouvre** les cotisations et les reverse) ; décret n° 2005-321. Le régime de base
  entre en application par étapes à partir du **1er juillet 2007** (clés existantes `loi2004-71`,
  `decret2005-321` ; chronologie du livre).
- **Dans les comptes CNSS, la rupture se voit** : (i) le tableau AS-prestations en nature de
  l'annuaire 2018 (p. 354) montre le forfait à la Santé publique qui tombe de 48 000 000 D (2005)
  à 9-10 M (2006-2007), 6,1 M (2008), **zéro à partir de 2009**, et les compléments facturés par
  les hôpitaux qui passent de 150,5 MD (2005) à 42,3 (2006-2007), 25,0 (2008), **zéro ensuite** ;
  après 2008 la branche AS de la CNSS se réduit aux polycliniques/CAO, capital-décès, indemnité de
  décès, actions sanitaires et sociales (tableau « dépenses techniques 2018 », p. 385 : plus
  aucune ligne indemnité de maladie/couches servie) ; (ii) l'AT-MP disparaît des emplois CNSS
  (géré CNAM) ; (iii) côté recettes, la part maladie du taux global est recouvrée par la CNSS
  **pour le compte de la CNAM** puis reversée — les « produits techniques » CNSS ne la comprennent
  pas, mais les flux de trésorerie, si (« encaissements/décaissements au titre des fonds spéciaux
  et autres » ; comptes courants CNAM au passif).
- **Conséquence pour la série** : « dépenses CNSS » 1990-2004 (avec AS maladie et AT-MP) et
  2009-… (PF + pensions + PST + capital-décès + action sanitaire et sociale) ne sont **pas le même
  périmètre**. Les années 2005-2008 sont transitoires. Toute figure de longue période doit soit
  tracer les branches séparément (pensions et PF sont continues de bout en bout), soit marquer la
  rupture 2007-2008 d'une ligne et d'une note, comme la rupture de base du PIB dans les figures
  existantes.

### 5.2 Ruptures héritées, déjà documentées

AT-MP intégré aux comptes CNSS en 1995, PST en 1997 (dénominateurs élargis — notes des figures
existantes) ; régime des travailleurs à faibles revenus 2002 ; artistes 2004. Après 2004 :
RTFR/travailleurs de chantiers (l'annuaire 2018, p. 290, avertit que le total RTFR comprend
9 428 mD pour les chantiers) ; AMG non géré par la CNSS (budget de l'État).

### 5.3 Rupture de financement (2016-2018), sans changement de périmètre comptable

À partir de 2016 la CNSS cesse de reverser intégralement les cotisations CNAM (dette CNAM : 0,5 →
1,25 → 1,7 → 3,0 milliards de dinars 2016-2018, puis 8,7-10,6 milliards d'endettement total
2021-2023 selon EP LF2024/LF2025) ; la CSS (LF 2018) apparaît dans les comptes via le compte de
diversification. Les lignes « subventions » du rapport EP et la série `cnrps-transferts-etat`
montrent la mécanique côté État. Le solde CNSS reste calculé avant ces concours dans certaines
présentations, après dans d'autres : vérifier à l'extraction quelle colonne du tableau arabe
est « hors subventions » (le piège est documenté pour la CNRPS dans
`sources/minfin-ep-cnrps-finances.md` : −162,7 vs −1 014,4 MD en 2021 selon qu'on inclut la CSS).

## 6. Marche de construction (pour l'entrepôt `tunisia-data`, pas ici)

1. **Série `cnss-produits-charges-techniques` (2000-2020)** : extraire les tableaux 11-12 du
   millésime 2020 (couche texte ; alignement valeurs/années par géométrie, les barres empilées du
   tab. 12 exigent de distinguer totaux et segments) ; contrôle par le millésime 2019 (2000-2019)
   et par les points EF/EP/budget (2016-2020). Prolonger 2021-2023 par le rapport EP (méthode
   géométrique déjà validée pour la CNRPS).
2. **Série `cnss-resultat-exercice` (2009-2023, lacunaire)** : points du § 4, une ligne par
   (année, source, statut réalisé/probable/budget), arbitrage « réalisé le plus récent » ; les
   points 2009-2010 et 2015 gardent l'avertissement « source موازنة ».
3. **Séries d'emplois par branche (2005-2018)** : tableaux multi-années de l'annuaire 2018
   (pensions par nature et par régime, AS en nature, prestations en espèces, PF), en continuité de
   nomenclature avec `cnss-retrospective-ressources-emplois` ; croiser avec l'édition 2013 pour
   les révisions. C'est la vraie prolongation « par branche » de la rétrospective — côté emplois
   seulement.
4. **Série `cnss-placements` (2000-2018)** : tableaux placements des éditions 2013 et 2018,
   conservés par édition (divergence 2013 constatée).
5. **Note de concordance** : carte des périmètres (avant/après CNAM ; produits techniques vs
   ressources ; solde technique vs résultat), identités de contrôle (R−D vs résultat sur
   2016-2020 ; annuaire vs EF vs EP), rupture 2007-2008 chiffrée sur les lignes AS.
6. **Fiches sources** : compléter `sources/cnss-donnees-statistiques.md` et `cnss-annuaires.md`
   (index des pages financières ci-dessus) ; créer une fiche pour les états financiers 2018/2017
   et le récapitulatif budget 2022.

## 7. Références candidates (CSL-JSON)

**Déjà présentes, à compléter (note seulement)** :
- `cnss-chiffres` — ajouter à la note : « Comprend, millésime 2020 : évolution des cotisations
  (produits techniques) et des dépenses de prestations servies, ensemble des régimes, 2000-2020 ;
  états financiers 2018/2017 ; récapitulatif général du budget 2022 (colonne Bilan 2020 :
  résultat −1 091,5 MD). Millésime 2019 : mêmes séries arrêtées à 2019. Adresses et UUID :
  tunisia-data, sources/caisses-sociales-urls.csv. »
- `minfin-ep`, `minfin-ep-2020`, `-2022`, `-2023`, `-2024`, `-2025` — ajouter : « Chapitre caisses
  sociales : CNSS pp. 38-41 (LF 2020, fr, 2016-2017 réalisés), LF 2021 (fr, 2018 réalisé) ;
  tableaux arabes LF 2022 p. 46, LF 2023 p. 78 (2018-2020 ; colonne CNSS 2021 vide), LF 2024
  (2021 : −1 274,3 MD ; 2022 : −961,5), LF 2025 (2023 provisoire : −911,1). »
- `cnss-retrospective-1990-2004`, `ins-cnat-2015`, `loi2004-71`, `decret2005-321` — inchangées.

**À créer** :

```json
[
  {"id": "cnss-annuaire-statistique", "type": "report",
   "title": "Annuaire statistique (éditions 2006, 2010, 2013, 2016, 2017 et 2018)",
   "author": [{"literal": "Caisse nationale de sécurité sociale, direction des études et du contrôle de gestion"}],
   "publisher": "Caisse nationale de sécurité sociale", "publisher-place": "Tunis",
   "issued": {"date-parts": [[2019]]},
   "URL": "http://web.archive.org/web/20190716124119id_/http://www.cnss.tn:80/documents/10156/25253/annuaire2013fr.pdf",
   "note": "citation-key: cnss-annuaire-statistique\nSix éditions dans tunisia-data (data/raw/caisses/cnss/annuaires/, sources/cnss-annuaires.md, sources/cnss-urls.csv). Page « Évolution des principaux indicateurs » (ressources et emplois des branches gérées, cotisations, dépenses techniques, deux années par édition ; source imprimée « Bilan CNSS » pour l'édition 2013 et les états financiers pour 2018, « موازنة الصندوق » pour 2010, 2016 et 2017) : édition 2010 PDF 19, 2013 PDF 23, 2016 PDF 23, 2017 PDF 20, 2018 PDF 8. Tableaux financiers multi-années de l'édition 2018 : prestations en nature des assurances sociales 2000-2018 (p. 354), recettes et dépenses des polycliniques et du CAO 2010-2018 (p. 355), investissements et placements 2010-2018 (p. 379), répartition des dépenses techniques 2018 (p. 385) ; édition 2013 : placements 2000-2013 (p. 351), dépenses techniques 2013 (p. 359). URL = capture Wayback de l'édition 2013 française ; l'édition 2018 (387 p.) est une copie locale sans URL d'origine établie."},
  {"id": "cnss-etats-financiers-2018", "type": "report",
   "title": "États financiers de l'exercice 2018 (avec comparatif 2017) : bilan, état de résultat, état de flux de trésorerie et notes",
   "author": [{"literal": "Caisse nationale de sécurité sociale"}],
   "publisher": "Caisse nationale de sécurité sociale", "publisher-place": "Tunis",
   "issued": {"date-parts": [[2019]]},
   "URL": "https://www.cnss.tn/fr/c/document_library/get_file?uuid=ad7d7897-6945-4500-8a7e-1cc252308a3c&groupId=10156",
   "note": "citation-key: cnss-etats-financiers-2018\nPubliés sur la page « La CNSS en chiffres » (4 p., fr ; version arabe et notes dans le millésime 2018). Produits techniques 3 079 699 mD (2018) ; charges techniques 3 411 951 ; résultat −530 464 (2018) et −525 000 (2017) ; capitaux propres −383 521 mD au 31.12.2018 ; comptes courants CNAM 3 037 816 mD. Copies : tunisia-data data/raw/caisses/cnss/2020/01_Etats_Financiers.pdf et 2018/etat2018.pdf. Seuls états financiers publiés par la caisse (rien après l'exercice 2018). URL vérifiée le 10 novembre 2026."}
]
```

(L'alternative « une clé par édition d'annuaire » reste possible si le rédacteur cite des années
précises de plusieurs éditions ; la clé collective + pages en note suit le modèle `ins-cnat-2015`.)

## 8. Lacunes et reports (pour le backlog durable)

- **L-s3.1 — Pas de comptes par régime après 2004.** Les comptes de compensation (loi n° 60-30,
  art. 22) ne sont publiés nulle part après la rétrospective ; les états financiers publiés sont
  agrégés. Pistes : demande à la CNSS (direction des études et du contrôle de gestion — émettrice
  de la rétrospective) d'une rétrospective 2005-… ; centre de documentation du CRES (source de
  l'exemplaire 1990-2004). → backlog tunisia-data + `docs/notes/backlog-precis.md` (TODO déjà dans
  `_comptes_longue_periode.qmd`).
- **L-s3.2 — Solde 2005-2008, 2011, 2014.** Annuaires absents de l'entrepôt (éditions 2007-2009,
  2011-2012, 2014-2015) ; Wayback hors ligne le 10 novembre 2026 (§ 9). L'édition 2006 (scan,
  dans l'entrepôt) peut donner 2005-2006 : **OCR/lecture à l'image de sa page « principaux
  indicateurs »** (début du volume, non couverte par l'extraction actuelle) → backlog tunisia-data.
- **L-s3.3 — Valeur 2019 du résultat** : présente dans les tableaux arabes EP LF 2022 (p. 46) et
  LF 2023 (p. 78) mais à lire par géométrie (le pdftotext rend une liste de nombres) — extraction
  à faire avec la méthode CNRPS, pas de valeur recopiée ici sans elle.
- **L-s3.4 — 2024-2025** : rapport EP annexé au PLF 2026 à collecter (gbo.tn / finances.gov.tn)
  quand il paraîtra ; les données CNSS y seront 2023-2024.
- **L-s3.5 — Statut des points 2009-2010 et 2015** : source imprimée « موازنة الصندوق » (budget)
  et non « bilan » ; vérifier sur les annuaires suivants (2011, 2016) si les mêmes années y sont
  reprises sur bilan — lié à L-s3.2.
- **L-s3.6 — Nature exacte du « tableau 11 »** (cotisations vs produits techniques) : trancher à
  l'extraction par recoupement 2016-2018 (écart TO/pénalités ≈ 20 MD en 2017).
- **L-s3.7 — Base légale et convention CNSS-CNAM du recouvrement-reversement** (loi n° 2004-71,
  art. 16 ; convention entre caisses non identifiée) : utile pour qualifier la dette CNSS→CNAM ;
  rejoint la fiche proposée `r-cnam-transfert-reserves` du § 7 de
  `cadre-budgetaire-comptable-caisses.md`.
- **Alimentation du playbook tunisia-data** (`sources/chercher-des-donnees-tunisie.md`) : motif
  d'URL Liferay `cnss.tn/fr/c/document_library/get_file?uuid=…&groupId=10156` toujours actif
  (200 vérifié 10.11.2026) alors que les pages de navigation stagnent (dernière mise à jour
  01/2022) ; les annuaires anciens vivent sous `cnss.tn/documents/10156/30862/…` (captures 2019).
  → une ligne au playbook, une ligne à l'index des tableaux pour les pages financières des
  annuaires (§ 3.4).

## 9. Recherches infructueuses (requêtes réellement lancées, 10 novembre 2026)

Aucune ne relève de `docs/recherches.yml` (pas de texte JORT manquant) ; elles vont au backlog
tunisia-data :

1. **Annuaires CNSS 2007-2009, 2011-2012, 2014-2015 (Wayback)** :
   - `http://web.archive.org/cdx/search/cdx?url=cnss.tn*&filter=urlkey:.*annuaire.*…` → **504** ;
   - `…url=cnss.tn&matchType=domain&collapse=urlkey&fl=original,timestamp,statuscode&limit=3000`
     → 3 000 lignes sans « annuaire » (liste tronquée, non concluant) ;
   - `…&filter=original:.*nnuaire.*…` → page « Internet Archive: Temporarily Offline ».
   **À relancer** (motifs connus : `cnss.tn/documents/10156/30862/annuaire<AAAA>…pdf`, suffixe
   `id_` ; cf. playbook). Le silence d'aujourd'hui ne dit pas que les captures n'existent pas.
2. **Publications CNSS postérieures à 2020** : page « La CNSS en chiffres » relue le 10.11.2026 —
   rien de plus récent que le millésime 2020 (mise à jour affichée 04/01/2022) ; recherche web
   « CNSS rapport annuel 2022 2023 états financiers » → seuls échos de presse du rapport EP
   (africanmanager.com, leconomistemaghrebin.com : −961,5 MD en 2022, −1 274 en 2021 — cohérents
   avec EP LF 2024, qui reste la source à citer).
3. **CRES, série financière publiée** : cres.tn parcouru (accueil, thématique sécurité sociale,
   id=152) — prose seulement (déficits CNRPS 2005/2008/2011), pas de tableau annuel CNSS ;
   recherche web « CRES principaux indicateurs sécurité sociale » → néant. Le CRES reste une piste
   par **demande directe** (il détenait la rétrospective papier), pas par le site.
4. **Évaluation actuarielle BIT de la CNSS** : recherche web → le PDF trouvé
   (webapps.ilo.org/…/930sp1.pdf) est l'évaluation de la CNSS **de Guinée** (2004) ; aucune
   évaluation actuarielle BIT publiée pour la CNSS tunisienne identifiée en ligne.

## 10. Notions à glossaire

| Terme FR | Terme AR pressenti | Source canonique | Remarque |
|---|---|---|---|
| Produits techniques / charges techniques | — (états financiers ar : « الموازنة » pour le bilan) | notes aux états financiers CNSS 2018 (`cnss-etats-financiers-2018`) | nouveaux ; définissent recettes/dépenses de la série |
| Dépenses techniques | المصاريف التقنية (annuaire 2010, ar) | annuaires CNSS, pages indicateurs | synonyme de « charges techniques » côté prestations |
| Comptes courants CNAM (dette CNSS-CNAM) | — | bilan CNSS 2018 ; rapport EP LF 2020, § endettement | nouveau ; clef de lecture de la période 2016-2023 |
| Compte de compensation (par régime) | — | déjà proposé au § 6 de `cadre-budgetaire-comptable-caisses.md` | rappeler qu'il n'est plus publié après 2004 |


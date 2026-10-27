# Versements au budget 2003-2009 : contre-lecture indépendante (27 octobre 2026)

Objet : la section `#sec-ep-versements` de `precis/fr/entreprises_publiques/_recettes.qmd` (PR #549), ses
tableaux `tbl-ep-versements-anciens` et `tbl-ep-bct-parts`, la figure `fig-ep-versements`, et les deux séries
de `tunisia-data` qui les alimentent (`cdc-cloture-entreprises-publiques-2003-2009`, `bct-part-etat-benefices`).
Les corrections proposées en fin de note (§ 5 et 6) ont été appliquées le 27 octobre 2026 : branche
`ep/contrelecture` du précis (section, références, registre du Fonds de péréquation des changes, fiche
`r-bct-retenue-fpc-2002-2011`, backlog) et branche `donnees/bct-cdc-corrections` de `tunisia-data`
(transcriptions, script, tests, fiches, catalogue). La ventilation excédents / bénéfices de la Cour est gardée
et dite ; le 811 MD est donné comme constat de la Cour.

## 1. Méthode

- **Relecture à l'image**, sans partir de la transcription. Pages rendues avec `pdftoppm` (130 à 170 points
  par pouce), lues à l'écran, puis comparées à `sources/transcriptions/*.csv` du worktree
  `~/projets/tunisia-data-wt/cdc-cloture-2003-2009`. Fichiers bruts : `~/projets/tunisia-data/data/raw/`
  (`cour-des-comptes/18/`, `bct-archives/109/`, `minfinances/portail_ancien/`).
- **Recoupement** par trois familles indépendantes de la Cour des comptes :
  1. rapports annuels de la Banque centrale (tableaux des recettes non fiscales, trésorerie de l'État, notes
     des comptes d'ordre) ;
  2. états financiers de la Banque centrale publiés au *Journal officiel*, édition française (corpus local
     `~/projets/PDFs-legislation-tunisie/PDFs/JORT/`) ;
  3. ministère des Finances : série « Recettes non fiscales » (éditions 2008, 2012 et miroir 2002-2013) et
     rapports sur les finances publiques (تقرير المالية العمومية) 2006, 2007, 2008, 2010, 2011, dont les
     annexes donnent les articles du budget (30-011 à 30-016).
  Les lois de règlement (JORT : n° 2005-61, 2006-56, 2008-2, 2008-69, 2010-6, 2010-56, 2013-6) ont été
  ouvertes. Elles ne donnent les recettes que par titre (tableau n° 1) et les fonds spéciaux qu'en total
  (tableau n° 6). Elles ne permettent donc aucun recoupement ligne à ligne.

## 2. Relecture à l'image : Cour des comptes, gestions 2003-2009

Rapports (édition arabe) : gestion 2005 `Rapport_18_2018-08-16-11-40-59.pdf`, p. 51 du fichier ; gestion 2006
`…12-02-59.pdf`, p. 44 imprimée (fichier p. 43) ; gestion 2007 `…11-54-39.pdf`, p. 21 imprimée (fichier
p. 22) ; gestion 2009 `…11-57-14.pdf`, p. 23. En dinars. « = » signifie que la valeur lue à l'image est celle
qui a été versée, au dinar près.

| Gestion | Ligne | Versée | Relue (rapport, page) | Recoupement | Verdict |
|---|---|---:|---|---|---|
| 2003 | Part du budget, profits BCT | 120 000 000 | = (2005, p. 51) | BCT RA 2003, p. 177 : « n'a porté que sur 120 MDT » ; MinFin RFP 2006, p. 25 : 120,0 | confirmé |
| 2003 | Excédents EP non pétrolières | 224 000 000 | = | — | confirmé (image) |
| 2003 | Excédents EP pétrolières | 45 000 000 | = | — | confirmé (image) |
| 2003 | Bénéfices sociétés non pétrolières | 96 187 557 | = | — | confirmé (image) |
| 2003 | Bénéfices sociétés pétrolières | 7 511 561 | = | — | confirmé (image) |
| 2003 | Autres profits du Trésor | 43 817 105 | = | — | confirmé (image) |
| 2003 | **Total** | 536 516 223 | = | total − autres = 492,699 ; BCT RA 2003, p. 177 ; série MinFin : 492,7 | confirmé |
| 2004 | Profits BCT | 100 000 000 | = (2005, p. 51 ; 2006, p. 44) | BCT RA 2004, p. 170 ; RFP 2006, p. 25 : 100,0 | confirmé |
| 2004 | Excédents EP non pétrolières | 295 689 652 | = (2005 ; 2006) | — | confirmé (image, deux rapports) |
| 2004 | Excédents EP pétrolières | 0 (« - ») | = | — | confirmé |
| 2004 | Bénéfices non pétrolières | 99 724 464 | = | — | confirmé |
| 2004 | Bénéfices pétrolières | 12 801 195 | = | — | confirmé |
| 2004 | Autres profits | 102 680 112 | = | — | confirmé |
| 2004 | **Total** | 610 895 423 | = | total − autres = 508,215 ; BCT RA 2004, p. 170, et série MinFin : 508,2 | confirmé |
| 2005 | Profits BCT | 0 (« - ») | = (2005 ; 2006 ; 2007) | RFP 2006 et 2007 : « - » | confirmé |
| 2005 | Excédents EP non pétrolières | 104 971 754 | = (trois rapports) | — | confirmé |
| 2005 | Bénéfices non pétrolières | 191 442 270 | = | — | confirmé |
| 2005 | Bénéfices pétrolières | 14 127 992 | = | — | confirmé |
| 2005 | Autres profits | 42 907 090 | = | — | confirmé |
| 2005 | **Total** | 353 449 106 | = | total − autres = 310,542 ; BCT RA 2005, p. 184 ; MinFin : 310,5 | confirmé |
| 2006 | Profits BCT | 373 600 000 | = (2006, p. 44 ; 2007, p. 21) | RFP 2006, p. 25 ; RFP 2007 : 373,6 | confirmé |
| 2006 | Excédents EP non pétrolières | 35 974 500 | = | — | confirmé |
| 2006 | Bénéfices non pétrolières | 120 942 989 | = | — | confirmé |
| 2006 | Bénéfices pétrolières | 14 702 432 | = | — | confirmé |
| 2006 | Autres profits | 49 657 501 | = | — | confirmé |
| 2006 | **Total** | 594 877 422 | = | total − autres = 545,220 ; BCT RA 2006, p. 173 ; MinFin : 545,2 | confirmé |
| 2007 | Profits BCT | 340 380 000 | = (2007, p. 21 ; 2009, p. 23) | RFP 2008, p. 19 : 340,4 ; RFP 2010, annexe, article 30-011 : 340 380 | confirmé |
| 2007 | Excédents EP non pétrolières | 84 674 317 | = | RFP 2010, article 30-015 : 84 674 | confirmé |
| 2007 | Bénéfices non pétrolières | 142 872 093 | = | RFP 2010, article 30-013 : 142 873 | confirmé |
| 2007 | Bénéfices pétrolières | 12 586 890 | = | RFP 2010, articles 30-014 + 30-016 : 12 587 + 0 | confirmé |
| 2007 | Autres profits | 35 540 451 | = | — | confirmé |
| 2007 | **Total** | 616 053 751 | = | total − autres = 580,513 ; BCT RA 2008, p. 51, et RA 2009, p. 189 : 580,5 ; MinFin : 580,5 | confirmé |
| 2008 | Profits BCT | 425 000 000 | = (2009, p. 23) | RFP 2008, p. 19 : 425,0 ; RFP 2010, article 30-011 : 425 000 | confirmé |
| 2008 | Excédents EP non pétrolières | 88 500 000 | = | RFP 2010, article 30-015 : **136 500** | **divergent** (§ 5.4) |
| 2008 | Bénéfices non pétrolières | 321 639 239 | = | RFP 2010, article 30-013 : **273 639** | **divergent** (§ 5.4) |
| 2008 | Bénéfices pétrolières | 141 530 588 | = | RFP 2010, 30-014 + 30-016 : 9 969 + 131 561 = 141 530 | confirmé |
| 2008 | Autres profits | 28 787 216 | = | — | confirmé (image) |
| 2008 | **Total** | 1 005 457 043 | = | total − autres = 976,670 ; BCT RA 2008, p. 51 (« environ 977 ») ; RA 2009 et MinFin : 976,7 | confirmé |
| 2009 | Profits BCT | 0 (« - ») | = (2009, p. 23) | RFP 2010, 30-011 : 0 (prévu 417 000) | confirmé |
| 2009 | Excédents EP non pétrolières | 201 000 000 | = | RFP 2010, 30-015 : **337 722** | **divergent** (§ 5.4) |
| 2009 | Bénéfices non pétrolières | 508 081 763 | = | RFP 2010, 30-013 : **371 359** | **divergent** (§ 5.4) |
| 2009 | Bénéfices pétrolières | 79 470 093 | = | RFP 2010, 30-014 : 79 470 | confirmé |
| 2009 | Autres profits | 58 229 758 | = | — | confirmé (image) |
| 2009 | **Total** | 846 781 614 | = | total − autres = 788,552 ; BCT RA 2010, p. 31, série MinFin 2012 et RFP 2011, annexe 5 : 788,6 | confirmé |

Aucune erreur de lecture : les 78 lignes de la transcription sont exactes, ainsi que leurs pages et leurs
libellés. La ligne des excédents pétroliers (45 MD en 2003, « - » ensuite) n'est imprimée que dans les
rapports 2005 et 2006, comme le dit la fiche. Les sommes de contrôle, recalculées, tombent juste au dinar.

Textes de la Cour relus à l'image :
- 148,400 MD de l'exercice 2004 gardés au compte « مقابيض للحفظ » : rapport 2005, p. 49 du fichier.
- 373,600 MD pour 2004 et 2005 : rapport 2006, p. 44 imprimée (fichier p. 43). La part de l'exercice 2005, 235,600 MD, est à la p. 45
  imprimée (fichier p. 44), avec le résultat de 239,609 MD.
- 104,780 MD de hausse « réelle » en 2007 (340,380 − 235,600) : rapport 2007, p. 21.
- 432 MD non appelés en 2009 : rapport 2009, p. 23. La note de bas de page renvoie aux remarques des
  commissaires aux comptes de la Banque centrale (JORT n° 29 de 2010).
- 811 MD de bénéfices 2008 gardés hors budget (Compagnie des phosphates de Gafsa 617, Groupe chimique
  tunisien 194) : p. 24, ainsi que la réponse du ministère (771 MD de recettes propres au-delà de la loi
  rectificative ; mesure de précaution pour 2010).
- 874 MD inscrits en 2011 pour 2008, 2009 et 2010 : rapport sur la gestion 2011, tableau p. 39 du fichier,
  texte p. 40.

## 3. Relecture à l'image : parts de la Banque centrale, exercices 2002-2010

| Exercice | Poste | Versé | Relu (rapport, page imprimée / fichier) | Recoupement | Verdict |
|---|---|---:|---|---|---|
| 2002 | résultat | 125 218 572 | = RA 2002, p. 248 / 256 | — | confirmé |
| 2002 | part de l'État | 125 000 000 | = id. | RA 2003, p. 201 / 211 : 125 MDT versés au Trésor | confirmé |
| 2002 | part versée | 125 000 000 | = RA 2003, p. 201 / 211 | — | confirmé |
| 2003 | résultat | 102 079 693 | = RA 2003, p. 258 / 268 | — | confirmé |
| 2003 | part de l'État | 104 500 000 | = id. | — | confirmé |
| 2003 | part au budget | 100 000 000 | = RA 2004, p. 170 / 185 | Cour 2004 : 100 ; RFP 2006 : 100,0 | confirmé |
| 2003 | Fonds de péréquation des changes | 4 500 000 | = id. (« compte non tenu d'un montant de 4,5 MDT versé au Fonds de péréquation de change ») | — | confirmé |
| 2004 | résultat | 154 961 211 | = RA 2004, p. 264 / 278 | — | confirmé |
| 2004 | part de l'État | 148 400 000 | = id. | Cour 2005, p. 49 : 148,400 | confirmé |
| 2005 | résultat | 239 609 021 | = RA 2005, p. 288 / 302 | Cour 2006, p. 45 : 239,609 | confirmé |
| 2005 | part de l'État | 235 600 000 | = id. | Cour 2006, p. 45 : 235,600 ; RA 2006 (rappel) | confirmé |
| 2006 | résultat | 367 389 191 | = RA 2006, p. 292 / 314 | JORT n° 33 de 2008 (exercice précédent) : 367 389 191 | confirmé |
| 2006 | part de l'État | 350 380 000 | = id. | — | confirmé |
| 2006 | part versée | 350 000 000 | = RA 2007, p. 229 / 252 | — | confirmé |
| 2007 | part versée | 435 000 000 | = RA 2008, p. 217-218 / 237-238 | — | confirmé |
| 2007 | **résultat** | *(non versé)* | — | **JORT n° 33 du 22 avril 2008, p. 1294 : 446 721 198** | **case à remplir** (§ 5.1) |
| 2007 | **part de l'État** | *(non versée)* | — | **JORT n° 33 du 22 avril 2008, p. 1294 : 435 000 000** | **case à remplir** (§ 5.1) |
| 2008 | résultat | 446 862 335 | = RA 2008, p. 298 / 318 | JORT n° 40 de 2009 : 446 862 335 | confirmé |
| 2008 | part de l'État | 432 000 000 | = id. | JORT n° 40 de 2009 ; RA 2009, p. 289 et 297 ; Cour 2009, p. 23 | confirmé |
| 2009 | résultat | 258 076 525 | = RA 2009, p. 299 / 319 | JORT n° 29 de 2010 : 258 076 525 | confirmé |
| 2009 | part de l'État | 250 000 000 | = id. | JORT n° 29 de 2010 | confirmé |
| 2010 | résultat | 252 053 322 | = RA 2010, p. 123 / 131 | JORT n° 32 de 2011 | confirmé |
| 2010 | part de l'État | 228 700 000 | = id. | JORT n° 32 de 2011 ; RA 2011, p. 144 / 152 | confirmé |

Les pages imprimées de la fiche sont toutes exactes. L'édition 2004 n'a pas de folio dans sa couche texte ;
les folios 170 et 264 ont été lus à l'image.

## 4. Les identités et les écarts signalés

### 4.1 « Revenus des participations » = total de la Cour moins autres profits du Trésor

L'identité se vérifie **pour 2003 à 2009, sans rupture**. Elle vaut aussi pour 2010 : 812,722 − 16,748 =
795,975, contre 796,0 dans la série du ministère et dans le RA 2010.

La « rupture » de 2009 (803,8 contre 788,6) est une **valeur provisoire**. Le RA 2009 (p. 189, réalisations
2009) imprime 803,8. Trois sources ultérieures donnent 788,6 : le RA 2010 (p. 31), la série « Recettes non
fiscales » du ministère (édition 2012 et miroir) et le RFP 2011 (annexe 5, p. 67). Le RA 2009 révise aussi
d'autres lignes de 2009 dans l'édition suivante (revenus pétroliers : 407,3, puis 423,3). Verdict :
**confirmé**. La fiche `cdc-cloture-entreprises-publiques-2003-2009.md` doit être corrigée (§ 6).

### 4.2 Écarts entre la part arrêtée et le montant inscrit au budget

| Exercice(s) | Part arrêtée | Versée au Trésor (BCT) | Budget (Cour, MinFin) | Écart | Ce qu'on en sait |
|---|---:|---:|---:|---:|---|
| 1999 | 160,0 | — | 155,0 | 5,0 | RA 2002, p. 169 : 5,0 MD au Fonds de péréquation des changes (FPC) |
| 2000 | 165,0 | — | 160,0 | 5,0 | id. |
| 2001 | 250,0 | — | 235,0 | 15,0 | id. : 15 MDT « affectés en 2002 sur les bénéfices de la BCT » au FPC |
| 2002 | 125,0 | 125 (RA 2003, p. 201) | 120,0 | 5,0 | aucun texte lu ne dit l'affectation |
| 2003 | 104,5 | — | 100,0 | 4,5 | RA 2004, p. 170 : versé au FPC |
| 2004 + 2005 | 148,4 + 235,6 = 384,0 | — | 373,6 | 10,4 | RFP 2006, p. 25 : sur les 373,6 MD, 143 MD « se rattachent à la gestion 2005 » (voir ci-dessous) |
| 2006 | 350,38 | 350 (RA 2007, p. 229) | 340,38 | 10,0 | aucun texte lu ne dit l'affectation |
| 2007 | 435,0 | 435 (RA 2008, p. 218) | 425,0 | 10,0 | id. |
| 2008 + 2009 + 2010 | 432 + 250 + 228,7 = 910,7 | 682 + 200 = 882 en 2011 ; 28,7 en 2012 | 874 (Cour) ; **882 (MinFin)** | 36,7 | 28,7 expliqués ; **8,0 divergents** (§ 4.3) |

**Base légale.** La loi n° 2000-98 du 25 décembre 2000 (loi de finances pour 2001), article 34, a été lue à
l'image (JORT n° 104 du 29 décembre 2000, p. 3178). Elle ajoute à l'article 18 de la loi de finances pour
1999 (loi n° 98-111) un cinquième tiret : le fonds est alimenté « par une retenue sur les bénéfices de la
Banque Centrale de Tunisie dont le montant est fixé par le ministre des finances ». Le fonds créé par
l'article 18 porte, dans l'édition arabe, le nom de « صندوق تغطية مخاطر الصرف » (JORT arabe n° 104 de
1998, p. 2561, lu à l'image). C'est le fonds que les rapports de la Cour rangent parmi les fonds spéciaux du
Trésor sous ce nom.

**Verdict.**
- **Établi** : l'écart de l'exercice 2003, et ceux de 1999 à 2001.
- **Compatible, non établi** : les écarts de 2002 et de 2004 à 2007. Leur ordre de grandeur est celui des
  retenues documentées, sur une base légale qui permet une retenue fixée par le ministre. Pour 2006 et 2007,
  la Banque centrale dit encaissé par le Trésor le montant arrondi de la part (350, 435 MD), et le budget en
  inscrit 10 MD de moins. La retenue se ferait donc après l'encaissement, et non à la Banque.
- **Recoupement impossible** : les ressources propres du FPC dans les tableaux des fonds spéciaux de la Cour
  (70,7 MD en 2005, 69,2 en 2006, 71,1 en 2007, 46,2 en 2009) ne sont pas ventilées par origine. La loi de
  règlement ne donne que le total des fonds spéciaux.

**Inférence sur 2004-2005, à ne pas écrire comme un fait.** Le RFP 2006 (p. 25, lu à l'image) dit que des
373,6 MD versés en 2006, 143 MD « se rattachent à la gestion 2005 » (« تتعلق بتصرف 2005 »). Si la « gestion
2005 » est l'année budgétaire où la part de l'exercice 2004 aurait dû entrer, le partage serait 143,0 (exercice
2004, écart 5,4) et 230,6 (exercice 2005, écart 5,0). Cela rejoindrait une retenue d'environ 5 MD par
exercice. Cette lecture n'est pas établie : le texte ne nomme pas l'exercice des profits.

### 4.3 Les 874 MD de 2011

- RA 2011 (p. 144 / fichier 152, lu à l'image) : virement en 2011 au compte courant du Trésor des parts des
  exercices 2008 et 2009 (682 MD) et de 200 MD sur les 228,7 MD de l'exercice 2010. Même texte au JORT
  n° 33 du 27 avril 2012.
- RA 2011 (p. 153 / 161) et JORT n° 33 de 2012, p. 753 : reliquat de 28,7 MD de l'exercice 2010 encore aux
  comptes d'ordre fin 2011. Le RA 2012 le porte à zéro fin 2012.
- RA 2011, p. 64, note 2 : « la part revenant au budget de l'Etat des bénéfices de la BCT au titre des exercices
  2008, 2009 et 2010 (882 MDT) ».
- RFP 2011, annexe 5, p. 67 (lu à l'image), et article 30-011 de l'annexe des recettes : Banque centrale,
  réalisations 2011 **882,0** (loi de finances 400,0 ; loi rectificative 900,0).
- Cour, rapport 2011, p. 39-40 : **874 000 000**.

Verdict : **divergent**. Sur l'écart de 36,7 MD, 28,7 MD sont des montants versés en 2012. Les 8,0 MD
restants opposent la Cour (874) au ministère et à la Banque centrale (882) ; aucun texte lu ne les explique.
La phrase du chapitre « 874 MD pour les 910,7 MD des exercices 2008 à 2010 » est exacte sur la Cour, mais
présente comme un écart d'affectation ce qui est surtout un décalage de versement.

Hors fenêtre, pour la série 2010-2024 : en 2011, le total de la Cour moins les autres profits fait 1 566,8 MD,
contre 1 457,5 MD de revenus des participations dans le RA 2012 et le RFP 2011. L'écart de 109,3 MD n'est pas
expliqué ici.

### 4.4 Les 811 MD de bénéfices 2008 de la CPG et du GCT

Le RA 2009 décrit les encaissements au compte courant du Trésor, par périodes successives qui ne se
recouvrent pas (premier trimestre, avril-juillet, août-septembre, fin d'année ; p. 189-196 environ, couche
texte). Il cite, au titre de l'exercice 2008 : CPG 200 + 150 + 150 + 105 MD, soit au moins 605 ; GCT 150 + 31 +
30 MD, soit au moins 211. Ces montants sont souvent donnés comme « une partie ». Ils ne contredisent pas
617 et 194 MD gardés au compte d'attente, mais ne les égalent pas.

Le RFP 2011 (annexe 5) inscrit au budget de 2009 59,0 MD de la CPG et 225,0 MD du GCT. Avec 194 MD gardés
hors budget, le GCT aurait versé au moins 419 MD en 2009, au-delà des 211 MD que cite la Banque centrale.
Verdict : **non recoupable** en l'état ; ordre de grandeur compatible pour la CPG ; une question ouverte pour
le GCT. Le rapport de clôture de la gestion 2010, qui dirait si ces 811 MD sont entrés au budget de 2010,
n'est pas au catalogue de la Cour.

Autre divergence de date : le RA 2009 (p. 189) écrit que la part de l'exercice 2008 est intégrée « dans le
cadre de l'équilibre de l'année 2010 ». La Cour (rapport 2009, p. 23, publié en juin 2011) écrit que son
inscription est reportée au budget de 2011. Le RFP 2010 confirme qu'elle n'est pas entrée en 2010 (article
30-011 : réalisations 0, pour 617 MD prévus). La Cour décrit ce qui s'est passé ; le RA 2009 décrit
l'intention de 2010.

### 4.5 Ventilation des lignes, 2008 et 2009

L'annexe du RFP 2010 donne les articles du budget. La correspondance est exacte en 2007 : 30-013 « حصص
الشركات غير البترولية » = bénéfices des sociétés non pétrolières de la Cour ; 30-015 « مرابيح الشركات غير
البترولية » = excédents des EP non pétrolières ; 30-014 + 30-016 = bénéfices pétroliers.

| | 2008 Cour | 2008 MinFin | 2009 Cour | 2009 MinFin |
|---|---:|---:|---:|---:|
| Excédents EP non pétrolières (30-015) | 88,500 | 136,500 | 201,000 | 337,722 |
| Bénéfices sociétés non pétrolières (30-013) | 321,639 | 273,639 | 508,082 | 371,359 |
| Somme | 410,139 | 410,139 | 709,082 | 709,081 |

Les sommes sont identiques. La Cour fait passer 48,0 MD (2008) et 136,7 MD (2009) de l'article 30-015 vers sa
ligne des bénéfices des sociétés. Verdict : **somme confirmée, ventilation divergente**. La phrase du
chapitre « Les bénéfices des sociétés non pétrolières passent de 96,2 MD en 2003 à 508,1 MD en 2009 » ne vaut
que dans la nomenclature de la Cour. Le rapport ne dit pas laquelle des deux nomenclatures est la bonne.

### 4.6 Points mineurs

- RFP 2006, p. 25 : le total 2004 est imprimé 508,9, alors que ses composantes font 242,3 + 283,9 = 526,2. Le
  RFP 2007 donne 508,2 après avoir reclassé l'Office national des télécommunications parmi les
  établissements publics. Sans incidence sur le précis, qui suit la Cour (508,215).
- Non contrôlés ici : les rapports au PIB et aux dépenses hors dette de la section (3,85 % à 7,86 % ;
  0,84 % à 1,82 %). Seule la part de 62,8 % de la Banque centrale en 2006 a été recalculée
  (373,6 / 594,877) : exacte.

## 5. Ce que le précis et les données devraient changer (propositions, non appliquées)

### 5.1 Exercice 2007 : remplir la case

Le JORT édition française n° 33 du 22 avril 2008, p. 1294 (fichier `PDFs/JORT/2008/fr/Jo0332008.pdf`, p. 31,
lu à l'image) publie la répartition approuvée le 28 février 2008 : résultat 446 721 198 ; provisions pour
fabrication des billets 10 721 198 ; réserves pour fonds social 1 000 000 ; part de l'État 435 000 000.
Lignes à ajouter à `sources/transcriptions/bct-part-etat-benefices-2002-2010.csv` :

```
2007,resultat_exercice,446721198,jort-2008-33,1294,31,image,Résultat de l'exercice,,répartition approuvée par le Conseil d'administration le 28 février 2008 ; états financiers publiés au JORT (édition française) n° 33 du 22 avril 2008 ; le rapport annuel 2007 ne l'imprime pas
2007,part_etat,435000000,jort-2008-33,1294,31,image,Part revenant à l'Etat,,
```

La valeur `rapport` « jort-2008-33 » sort du schéma `ra-AAAA`. Le script et le test devront l'accepter, ou
bien la source sera rangée dans une colonne dédiée.

Phrases à remplacer :
- `sources/bct-part-etat-benefices.md` : « La répartition du résultat de l'exercice 2007 n'est pas imprimée
  dans le rapport 2007 […] : seul le montant encaissé de 435 MDT, arrondi, est connu. » → « La répartition du
  résultat de l'exercice 2007, absente du rapport 2007, est publiée au Journal officiel (édition française,
  n° 33 du 22 avril 2008, p. 1294) : part de l'État 435 000 000 dinars. »
- `_recettes.qmd`, légende de `tableau_bct_parts` : « pour l'exercice 2007, le rapport n'imprime pas la
  répartition du résultat » → « pour l'exercice 2007, la répartition vient des états financiers publiés au
  *Journal officiel* » (avec une notice de bibliographie à créer pour JORT n° 33/2008, URL pist.tn de
  l'édition française).

### 5.2 Le « 874 pour 910,7 » et le TODO

Puce actuelle (fin) : « …425 MD pour les 435 MD de 2007, et 874 MD pour les 910,7 MD des exercices 2008 à
2010 [@…] ». Proposition :

```
…425 MD pour les 435 MD de 2007. Les parts des exercices 2008 à 2010, 910,7 MD, arrivent au Trésor en deux fois : 882 MD en 2011, dont le budget de 2011 inscrit 874 MD selon la Cour des comptes et 882 MD selon le ministère des Finances, et 28,7 MD en 2012 [@bct-ra-2011, p. 64, 144 et 153 ; @cdc-cloture-2011, p. 40 ; @minfin-rfp-2011, p. 67].
```

(clés `bct-ra-2011` et `minfin-rfp-2011` à verser si elles n'existent pas.) TODO adjacent à remplacer par :

```
<!-- TODO (documentaliste) : écarts de 5 MD (exercice 2002), 10,4 (2004-2005), 10 (2006), 10 (2007) entre la part arrêtée et le budget : base légale lue (loi n° 2000-98, art. 34, retenue au profit du Fonds de péréquation des changes fixée par le ministre ; 4,5 MD attestés pour l'exercice 2003, 5, 5 et 15 MD pour 1999-2001), montants non attestés pour les autres exercices ; 8 MD en 2011 entre la Cour (874) et le ministère des Finances et la BCT (882) non expliqués. Voir docs/notes/recettes-2003-2009-contre-lecture-2026-10-28.md. -->
```

Le texte rendu peut dire la règle, qui est lue : « Depuis la loi de finances pour 2001, une retenue fixée par
le ministre des Finances sur les bénéfices de la Banque centrale alimente le Fonds de péréquation des changes ;
pour l'exercice 2003, elle est de 4,5 MD. » Il ne doit pas attribuer les autres écarts au fonds.

### 5.3 Bénéfices des sociétés 2009

Puce « Les bénéfices des sociétés non pétrolières passent de 96,2 MD en 2003 à 508,1 MD en 2009. » Ajouter,
ou mettre en note du tableau : « selon la nomenclature de la Cour des comptes ; le ministère des Finances
range 136,7 MD de 2009 (48,0 MD de 2008) parmi les excédents des entreprises publiques ». À trancher par la
revue : laquelle des deux ventilations le précis suit, et s'il le dit.

### 5.4 Fiche `sources/cdc-cloture-entreprises-publiques-2003-2009.md` (tunisia-data)

Remplacer « pour 2009 elle imprime 803,8 MD, contre 788,6 MD selon la Cour. » par :

```
pour 2009, le rapport 2009 imprime une réalisation provisoire de 803,8 MD ; le rapport 2010 (p. 31), la série « Recettes non fiscales » du ministère des Finances et son rapport sur les finances publiques 2011 (annexe 5) donnent 788,6 MD, égal au total de la Cour moins les autres profits du Trésor. L'identité vaut aussi pour 2010 (796,0 MD).
```

Et, dans `bct-part-etat-benefices.md`, remplacer « Les écarts de 5, 10,4, 10, 10 et 36,7 MD ne sont expliqués
par aucun texte lu, sauf celui de 2003 (Fonds de péréquation des changes). » par :

```
L'écart de 36,7 MD se décompose en 28,7 MD versés au Trésor en 2012 (reliquat de l'exercice 2010) et 8 MD qui opposent la Cour (874) au ministère des Finances et à la Banque centrale (882). Les écarts de 5, 10,4, 10 et 10 MD ont une base légale lue (loi n° 2000-98, art. 34 : retenue sur les bénéfices de la Banque centrale au profit du Fonds de péréquation des changes, montant fixé par le ministre) ; seul celui de l'exercice 2003 (4,5 MD) est attesté, comme ceux de 1999 à 2001 (5, 5 et 15 MD, rapport 2002, p. 169).
```

## 6. Recherche infructueuse : fiche proposée pour `docs/recherches.yml` (non versée)

```yaml
- id: r-bct-retenue-fpc-2002-2011
  objet: décision du ministre des Finances fixant la retenue sur les bénéfices de la Banque centrale au profit du Fonds de péréquation des changes (loi n° 2000-98, art. 34), exercices 2002 et 2004 à 2007, et affectation des 8 MD de 2011 (874 MD selon la Cour, 882 MD selon le ministère et la Banque centrale)
  ou: [precis/fr/entreprises_publiques/_recettes.qmd#sec-ep-versements]
  requetes:
    titres_fts: ['"perequation des changes"', '"risques de change" AND fonds', '"banque centrale" AND benefices']
    titres_like: ['%perequation des changes%', '%benefices de la banque centrale%']
    iort_ar: [صندوق تغطية مخاطر الصرف, تغطية مخاطر الصرف, أرباح البنك المركزي]
    plein_texte: [péréquation des changes, صندوق تغطية مخاطر الصرف, retenue sur les bénéfices]
    depuis: 2000-12-29
  periode:
    jusqu_au: 2012-12-31
    motif: exercices 2002 à 2010 de la Banque centrale, dont les parts sont versées au Trésor au plus tard en 2012 (rapport annuel 2012)
  passes:
  - date: 2026-10-27
    role: documentaliste
    sources: [jort_cache, corpus_local, web]
    couverture: "jort_cache (FTS sur titres et objets, 1985-2014) : seuls les textes fondateurs (arrêté du 27 avril 1985, circulaire 85-25, LF 1999 art. 18, décret 99-1649, LF 2001 art. 34) et les lois de règlement 1976-2009 (totaux par titre et des fonds spéciaux) ; corpus JORT FR 2003-2012 parcouru pour les états financiers de la BCT (n° 33/2008, 40/2009, 29/2010, 32/2011, 33/2012 trouvés ; 2003-2007 non trouvés, couche texte décalée dans les fascicules 2003-2005) ; rapports annuels BCT 2002-2012, rapports de clôture de la Cour 2005, 2006, 2007, 2009, 2011, 2012, rapports du ministère sur les finances publiques 2006-2011 : aucun montant de retenue hors exercices 1999-2001 et 2003 ; recherche web (une requête) sans résultat."
    couvert_jusqu_au: 2012-12-31
    resultat: aucun
  a_faire: "rapports de clôture des gestions 2008 et 2010 (absents du catalogue de la Cour) ; comptes du Fonds de péréquation des changes (rapport de la Cour sur les fonds spéciaux, ou compte général de l'administration des finances 2008-2009, `2008_rapport_cga_ar.pdf` et `2009_rapport_cga_ar.pdf`, sans couche texte : OCR) ; RFP 2005 (couche texte vide : OCR)."
```

Avant de verser la fiche, contrôler les valeurs avec `scripts/recherches.py verifier`.

## 7. Sources lues pour cette note (fichiers locaux)

- Cour des comptes : `Rapport_18_2018-08-16-11-40-59.pdf` (gestion 2005), `…12-02-59.pdf` (2006), `…11-54-39.pdf`
  (2007), `…11-57-14.pdf` (2009), `Rapport_18_2019-03-07-09-24-43.pdf` (2011), `…11-50-00.pdf` (2012).
- Banque centrale : `bct-archives/109/rapport2002.pdf` à `rapport2013.pdf`.
- JORT édition française : n° 104/2000 (p. 3178), n° 33/2008 (p. 1294), n° 40/2009, n° 29/2010, n° 32/2011,
  n° 33/2012 ; lois de règlement citées au § 1. JORT édition arabe : n° 104/1998 (p. 2561-2562).
- Ministère des Finances : `portail_ancien/series_statistiques/{2008,2012,miroir}_serie_recettes_non_fiscales.pdf` ;
  `portail_ancien/rapports_finances_publiques/{2006,2007,2008,2010}_rapport_finances_publiques.pdf`,
  `2011_finances_publiques.pdf`. Ces rapports ne sont pas encore catalogués dans `tunisia-data/sources/` ; les
  cataloguer avant de les citer.

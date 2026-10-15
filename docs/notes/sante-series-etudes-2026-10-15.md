# Santé — séries et études sur l'assurance maladie, la dépense de la CNAM et la réforme de 2004 (15 octobre 2026)

Note de documentaliste pour la partie chiffrée de `precis/fr/sante/_couverture.qmd`
(`#sec-sante-perimetres`, `#sec-sante-transferts`, `#sec-sante-cnam-comptes`,
`#sec-sante-cnam-etude`, `#sec-soins-longue-periode`). Elle complète, sans les répéter,
`sante-cnam-comptes-2026-10-12.md` (états CNAM 2016-2021, parts CRES 2009-2019, prestations
sanitaires 2007-2021), `sante-cnam-filiere-medecins-2026-10-12.md` (filières 2008-2021),
`sante-depenses-sources-2026-10-12.md` (budget Santé, OMS 2018-2023) et
`sante-couverture-avant-2004-2026-10-14.md`.

Tout chiffre ci-dessous a été **lu comme un nombre imprimé** (couche texte, ou image quand la
page est scannée). Aucune hauteur de barre n'a été estimée. Les pages sont celles imprimées
dans le document, sauf mention contraire.

**Classement des familles** (`docs/conventions-redaction.md`, § 3) :

| Famille | Sources de cette note |
|---|---|
| A. Comptes d'organisme (primaire, CNAM) | états financiers CNAM 2011-2015 |
| B. Comptes de la santé (méthode OMS/SHA, ministère de la Santé ; famille des comptes OMS du chapitre) | Ben Abdelaziz et al. 2018 (comptes 2012-2014) ; relais de CNS 2000/2004/2005 et OASIS par le CRES, la thèse, la RTBC |
| C. Études et notes d'étude | *Lettre du CRES* n° 5 (2014) et n° 7 (2015) ; note CRES/UNICEF 2019 ; thèse Ismail 2015 ; Ismail et Zaouali 2022 ; Ben Cheikh et Achour 2006 ; actes ATDSRP 2017 |

Aucune série de la famille C ne se range dans un tableau de la famille A ou B.

---

## 1. États financiers de la CNAM, exercices 2011-2015 (famille A) — à verser au chapitre

**Fichier** : `tunisia-data/data/raw/caisses/cnam/fr_etat_fin_11_15.pdf` (déjà archivé,
catalogué dans `sources/caisses-sociales-urls.csv` l. 89 ; SHA-256
`2db9a7ee873c30ff0791f2edb861251dfcbd108b3fa666860326e5c83b6ab025`), URL
<http://www.cnam.nat.tn/doc/upload/fr_etat_fin_11_15.pdf>. Document **scanné** : la passe OCR
existante (`fr_etat_fin_11_15_ocr.pdf`) décale les colonnes et n'est pas utilisable. **Lu à
l'image** le 15 octobre 2026, p. 3 (état du résultat) et p. 4 (flux de trésorerie) ; pages du
PDF, sans numéro imprimé. Unité imprimée : **milliers de dinars**. Même publication, même
présentation que `BILAN2016_2018.pdf` : les deux séries se prolongent.

| Exercice | Produits techniques | Charges techniques | Marge brute (résultat technique) | Charges administratives | Résultat de l'exercice | Encaissements des cotisations | Prestations sociales décaissées |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2011 | 1 643 462 | 1 510 622 | 132 840 | 71 893 | −2 528 | 1 347 041 | 1 291 089 |
| 2012 | 1 831 473 | 1 738 751 | 92 722 | 83 844 | −17 389 | 1 598 685 | 1 594 648 |
| 2013 | 2 050 859 | 1 802 790 | 248 069 | 103 094 | 46 744 | 1 671 197 | 1 748 750 |
| 2014 | 2 182 303 | 1 900 913 | 281 390 | 107 667 | 135 588 | 1 682 581 | 1 766 517 |
| 2015 | 2 353 050 | 2 013 350 | 339 700 | 126 739 | 125 144 | 1 758 982 | 1 766 499 |

Autres lignes lues (p. 3) : provisions sur comptes des cotisants −89 537, −84 371, −147 518,
−70 685, −112 663 ; résultat technique net des provisions 43 303, 8 351, 100 551, 210 705,
227 037 ; effets des modifications comptables −9 928 (2011), 15 382 (2012), 9 166 (2013).

**Contrôles** : produits − charges techniques = marge brute imprimée, pour les cinq années ;
flux net d'exploitation recalculé = imprimé en 2011 (18 277) et 2015 (117 288).
**Pas d'année commune** avec l'édition 2016-2018 : sa p. 3 ne porte que 2016-2018, et l'en-tête
de sa p. 4 imprime « 2015 » sans aucune valeur dans la colonne. La concordance entre éditions ne
peut donc pas être testée pour la jonction 2015-2016 (elle l'a été pour 2018 entre les deux
éditions suivantes).

**Série prête à tracer** (prolonge `fig-sante-cnam-comptes` de 2016-2021 à **2011-2021**), en
MD courants arrondis au dixième depuis les milliers imprimés :

| Année | Charges techniques (MD) | Charges administratives (MD) | Prestations décaissées (MD) |
|---|---:|---:|---:|
| 2011 | 1 510,6 | 71,9 | 1 291,1 |
| 2012 | 1 738,8 | 83,8 | 1 594,6 |
| 2013 | 1 802,8 | 103,1 | 1 748,8 |
| 2014 | 1 900,9 | 107,7 | 1 766,5 |
| 2015 | 2 013,4 | 126,7 | 1 766,5 |

Points à signaler au rédacteur : les décaissements baissent de 1 766,5 MD (2015) à 1 486,7 MD
(2016) puis remontent à 2 156,5 MD (2018) ; aucune explication imprimée, ne pas commenter sans
la note aux états financiers. Le **résultat de l'exercice** est négatif en 2011-2012 pour la
caisse entière (trois régimes). Les charges techniques restent le total des trois régimes
(maladie, assurances sociales, AT/MP), comme pour 2016-2021.

Mise à jour à prévoir dans `scripts/extract_sante_depenses.py:cnam` (tunisia-data) : la page
étant scannée, il faut une transcription contrôlée (`sources/transcriptions/…csv`) plutôt
qu'une lecture de couche texte ; la note `sante-indicateurs-sources-2026-10-12.md` (« 2011-2015
océrisés, non validés ») est dépassée par cette lecture.

---

## 2. *La Lettre du CRES* n° 5, décembre 2014 (famille C)

- **Qui** : Imen Blel et Houda Chahed, économistes au CRES ; encadrement Mehdi Ben Braham (ESAI)
  et Abderrahmane El Lahga (ISG) (p. 1). Mise en ligne datée du 12/12/2014 sur la page
  « Lettre du CRES » du site.
- **Fichier** : `tunisia-data/data/raw/caisses/cres/cres_lettre_n5_2014_depenses_cnam.pdf`,
  4 p., 686 881 octets, SHA-256
  `9c3a145cafabecd1e168f6fa567762a90feab068bf7edccdf68853e76ea13662`, URL
  <http://www.cres.tn/uploads/tx_wdbiblio/Lettre__5.pdf> (200, `application/pdf`, 15/10/2026).
  Catalogue : `sources/sante-series-etudes-urls.csv`.
- **Nature et méthode** : note descriptive, sans section de méthode ni calcul propre déclaré.
  Elle **relaie** trois familles de sources : comptes nationaux de santé (CNS 2002, 2007) et
  rapport OASIS 2013 ; OMS (2013) ; rapports d'activité de la CNAM et rapport du Conseil
  national de l'assurance maladie de mai 2014 (exercice 2013). Aucun de ces primaires n'est
  détenu (§ 9).
- **Périmètre** : assurance maladie de la CNAM (le régime maladie), 2007-2014 selon les
  indicateurs ; le cadrage d'ensemble porte sur la dépense totale de santé.

### 2.1 Ce que la Lettre imprime en nombres

| Page | Objet | Valeurs imprimées | Source déclarée |
|---|---|---|---|
| p. 1, tableau 1 | dépenses totales de santé (DTS), MDT | 1 581,2 (2000) ; 2 247,3 (2005) ; 4 019,3 (2010, « estimation ») | CNS (2002, 2007) et rapport OASIS 2013 |
| p. 1, tableau 1 | DTS / PIB, % | 5,5 ; 5,9 ; 6,3 | idem |
| p. 1, tableau 1 | DTS par habitant, DT | 164,1 ; 214,4 ; 382,8 | idem |
| p. 1, tableau 1 | sécurité sociale en % des DTS | 17 ; 23,1 ; 25,7 | idem |
| p. 1 | bénéficiaires CNAM ; malades chroniques | « près de 7 millions » ; 770 000 | rapport du Conseil national, mai 2014 |
| p. 2 | paiements directs des ménages | « en moyenne 40 % des DTS » sur 1995-2011 | OMS (2013), graphe 1 |
| p. 2 | santé dans le budget des ménages | 5,5 % | enquête INS consommation 2010 |
| p. 2 | part de la sécurité sociale (CNAM depuis 2007) dans les DTS | 10,8 % (1996) → 26,3 % (2011) | OMS (2013) |
| p. 2 | cotisation maladie | 6,75 % (2,75 salarié + 4 employeur) ; 4 % retraités | — |
| p. 2 | filière publique, % des assurés | 75,7 % (2008) → 66,4 % (2013) | rapport du Conseil national, mai 2014 |
| p. 2 | filière privée | 10,41 % (2008) → 14,31 % (2013) | idem |
| p. 2 | remboursement | 13,89 % (2008) → 19,34 % (2013) | idem |
| p. 3 | assurés hors filière publique | 643 000 en 2008 (privée 10 %, remboursement 14 %) | — |
| p. 3, graphe 4 | **bénéficiaires** (affiliés et ayants droit, trois filières + faibles revenus + étudiants), millions | 6,232 (2008) ; 6,834 ; 7,006 ; 7,021 ; 6,927 ; 6,940 (2013) | rapport du Conseil national, mai 2014 |
| p. 3 | bénéficiaires 2013 | 6 940 135, « soit 64 % de la population » | idem |
| p. 3 | déficit technique du **régime d'assurance maladie** | 9 MD (2008) → 55 MD (2012) | rapports d'activité CNAM (graphe 5) |
| p. 4 | dépenses CNAM, secteur public | 452 MD (2007) → 826 MD (2012), +82,72 % | rapports d'activité CNAM (graphe 6) |
| p. 4 | dépenses CNAM, secteur privé | 175 MD (2007) → 708 MD (2012), +305,17 % | idem |
| p. 4 | part des structures privées dans les dépenses CNAM | 27,6 % (2007) → 45,76 % (2012) | idem |
| p. 4 | patients en APCI | 205 541 (2008) → 770 790 (2013) | — |
| p. 4 | prises en charge APCI | 270 055 (2008) → 1 079 352 (2013) | — |
| p. 4 | dépenses APCI | +117 % de 2008 à 2013 | rapport du Conseil national (graphe 7) |
| p. 4 | médicaments spécifiques | 115 MD (2008) → 332 MD (2014), dont 48 % par an aux cancers | — |

**Graphes sans étiquettes de valeur** : graphe 1 (structure des DTS 1995-2011, OMS),
graphe 2 (assurés par filière 2008-2013), graphe 5 (recettes, dépenses et résultat techniques
2008-2012), graphe 6 (dépenses par secteur 2007-2012), graphe 7 (maladies ordinaires et APCI
2008-2013). **Aucune de leurs années intermédiaires n'est reprise** : seuls les nombres du texte
le sont.

### 2.2 Séries de la Lettre prêtes à tracer

Une seule est une série annuelle complète, en unité propre :

| Année | Bénéficiaires de l'assurance maladie, affiliés et ayants droit (millions) |
|---|---:|
| 2008 | 6,232 |
| 2009 | 6,834 |
| 2010 | 7,006 |
| 2011 | 7,021 |
| 2012 | 6,927 |
| 2013 | 6,940 |

Source : *Lettre du CRES* n° 5, p. 3, graphe 4, d'après le rapport du Conseil national de
l'assurance maladie de mai 2014. **Unité différente** du tableau des affiliés par filière déjà au
chapitre (CNAM, indicateurs globaux, p. 4 : 2,85 à 3,45 millions d'**affiliés** sur la même
période) : ce sont ici les personnes protégées, ayants droit compris. Ne pas les superposer sur
un même axe sans le dire ; une figure à deux panneaux est possible.

Les autres indicateurs de la Lettre ne donnent que **deux bornes** (2007/2008 et 2012/2013) :
ils se citent dans le texte, ils ne se tracent pas.

### 2.3 Recoupements avec l'existant

- **Dépense maladie 2012, trois familles concordantes.** Lettre : 826 + 708 = 1 534 MD ;
  avec 45,76 % de part privée, le total implicite est 708 / 0,4576 ≈ 1 547 MD (soins à
  l'étranger ≈ 13 MD). CRES n° 8 (déjà au chapitre) : part maladie 89,0 % en 2012 ; appliquée aux
  1 738,8 MD de charges techniques des états 2012 (§ 1), elle donne ≈ 1 547 MD. **Les deux
  notes du CRES et les états de la CNAM sont compatibles en 2012**, comme ils l'étaient en 2019
  pour l'AT/MP. Ce contrôle conforte le dénominateur supposé de la figure CRES n° 8 pour une
  deuxième année ; il ne reconstruit aucune ventilation.
- **« Déficit technique » contre marge brute.** La Lettre écrit −9 MD (2008) et −55 MD (2012)
  pour le **régime d'assurance maladie** ; les états 2012 de la caisse impriment une marge brute
  **positive** de 92,7 MD pour les **trois régimes**. Pas une contradiction : périmètre d'une
  branche contre caisse entière, et la Lettre ne dit pas si les provisions sur cotisants sont
  incluses. À ne pas écrire comme « la CNAM est en déficit » ; à ne pas comparer sans ce rappel.
- **Filières 2013 : la Lettre contredit le primaire CNAM.** Lettre (rapport du Conseil national,
  mai 2014) : 66,4 % / 14,31 % / 19,34 %. CNAM, indicateurs globaux 2021, p. 4 : 1 826 160 /
  498 513 / 615 347 sur 2 940 020, soit **62,1 % / 17,0 % / 20,9 %**. En 2008 les deux sources
  concordent à quelques dixièmes (75,7/10,41/13,89 contre 76,1/10,2/13,6). Le chapitre garde la
  publication de la CNAM ; l'écart de 2013 (révision des fichiers ou date d'extraction) n'est pas
  expliqué par la Lettre.
- **Secteurs 2007** : la Lettre (452/175) et la thèse Ismail (454,1/172,6, § 3.2) relaient deux
  versions d'un même chiffre CNAM non détenu.

---

## 3. Thèse de Safa Ismail, 2015 (famille C)

- **Référence** : *Évaluation économique de la réforme de l'assurance maladie en Tunisie*,
  thèse de doctorat en sciences économiques, Université Paris-Dauphine (École doctorale de
  Dauphine, LEGOS), soutenue le 18 décembre 2015 ; direction Brigitte Dormont, codirection
  Mohamed Goaied (IHEC Carthage) ; NNT 2015PA090068 ; HAL tel-01300569 (page de titre et page
  HAL).
- **Clé** : `ismail-2015-these` **existe sur la branche `chantier/sante-regimes-avant-2004`**
  (`origin`), pas sur `master` : la reprendre telle quelle. La note de cette entrée dit
  « établissement de soutenance à relever sur la page de titre » : c'est **Université
  Paris-Dauphine** ; compléter `publisher`.
- **Fichier** : `tunisia-data/data/raw/caisses/sante-avant-2004/hal_tel-01300569.pdf` (249 p.,
  SHA-256 `8fe95b4f…`, catalogué dans `sources/sante-avant-2004-urls.csv`). Pages citées ici =
  pages imprimées (page imprimée = page du PDF − 13).

### 3.1 Méthode (chapitre 3, pp. 107-149 ; chapitre 2, pp. 71-105)

- **Données** :
  - *Enquête nationale de santé 2005* (INSP, projet TAHINA) : 6 491 adultes de 35 à 70 ans, un
    adulte tiré par ménage, tirage à trois degrés, 7 régions, 329 districts × 25 ménages
    (pp. 113-114) ;
  - *Enquête nationale sur le budget, la consommation et le niveau de vie des ménages 2010*
    (INS) : 11 281 ménages répondants (50 364 individus), dont le volet « accès aux services »
    sur 5 690 ménages (25 036 individus) (pp. 114-116 ; p. 77-78).
  - L'enquête INS de 2005 n'ayant pas d'information sur la couverture, l'auteure **apparie deux
    enquêtes différentes**, aux questions formulées différemment (p. 120).
- **Échantillon** : **hommes chefs de ménage de 35 à 70 ans**, affiliés CNSS ou CNRPS en 2005,
  CNAM en 2010, ou non assurés ; N = 6 214 (2 590 en 2005, 3 624 en 2010) ; sous-échantillon
  des malades chroniques (ALD) N = 1 169 (tableau 3.1, p. 117). Les bénéficiaires de l'AMG 1 sont
  exclus (reste à charge nul non interprétable, pp. 116-117).
- **Variables** : participation (reste à charge > 0) comme mesure d'accès ; log du reste à charge
  inconditionnel et conditionnel, en **dinars constants base 2010** ; part du reste à charge dans
  les dépenses totales, hors santé, non alimentaires ; dépenses catastrophiques au seuil OMS
  (RAC > 40 % des dépenses non alimentaires) et au seuil Banque mondiale (RAC > 10 % des
  dépenses totales) (pp. 122-127 et légende des tableaux).
- **Modèle** : **différences de différences** par MCO, 2005 contre 2010, traités = assurés,
  témoins = non assurés ; variables de contrôle (âge, maladie chronique, statut matrimonial,
  taille du ménage, milieu, région, dépenses totales) (pp. 120-122, 132-136). Les « filières » de
  2005 sont **imputées** (« observé en 2010, imputé en 2005 », tableau 3.2, p. 118).
- **Chapitre 2** : choix de filière et recours public/privé en 2010 seulement (EBCNV), modèles de
  choix ; l'auteure note qu'il faudrait traiter l'endogénéité du choix de filière (p. 151).
- **Réserves de l'auteure** (pp. 151-152) : endogénéité du choix de filière au chapitre 2 ;
  changements de composition des non assurés (groupe témoin) au chapitre 3, à reprendre par
  appariement.

### 3.2 Résultats chiffrés principaux

Coefficients du terme croisé traitement × 2010, **modèles avec contrôles**, tels qu'imprimés
(tableau 3.9, p. 146 ; tableau 3.10, p. 147). Seuls les coefficients **significatifs** sont
repris. Unités : participation et parts = modèle de probabilité linéaire ou part, donc
**points** (×100) si les parts sont des fractions, ce que suggèrent les constantes — l'auteure ne
le dit pas ; variables en log = **écart logarithmique** (l'auteure écrit « points de
pourcentage » ; −0,644 correspond à exp(−0,644) − 1 ≈ −47 %).

| Population | Indicateur | Coefficient | Signif. |
|---|---|---:|---|
| Hommes chefs de ménage affiliés **CNSS** (traitement 1) | participation | +0,068 | ** |
| idem | log RAC inconditionnel | +0,294 | * |
| Filière publique, CNSS + CNRPS (traitement 2) | participation | +0,058 | * |
| Filière publique, CNSS | participation | +0,066 | * |
| Filière publique, CNRPS | RAC / dépenses non alimentaires | −0,054 | ** |
| Filières privée et remboursement, CNSS (traitement 3) | log RAC inconditionnel | +0,393 | * |
| **Malades chroniques** CNSS + CNRPS | log RAC inconditionnel | −0,670 | * |
| idem | log RAC conditionnel | −0,644 | ** |
| idem | RAC / dépenses hors santé | −0,088 | * |
| idem | RAC / dépenses totales | −0,056 | ** |
| idem | dépense catastrophique, seuil BM | −0,239 | * |
| Malades chroniques CNSS | log RAC conditionnel | −0,621 | ** |
| idem | RAC / dépenses hors santé | −0,096 | * |
| idem | RAC / dépenses totales | −0,059 | ** |
| idem | dépense catastrophique, seuil BM | −0,296 | ** |
| Malades chroniques CNRPS | log RAC inconditionnel | −0,904 | ** |
| idem | log RAC conditionnel | −0,731 | ** |
| idem | RAC / dépenses totales | −0,053 | * |

Sans contrôles, l'effet sur l'ensemble des assurés est positif (participation +0,067**) mais
**disparaît** avec les contrôles (tableaux 3.7.1 et 3.8.1, pp. 137-139, commentaire p. 142).
Aucun effet significatif pour les affiliés CNRPS hors maladie chronique (p. 143).

Conclusions de l'auteure (résumé, dernière page ; pp. 148, 150) : accès accru pour les affiliés
CNSS, surtout dans le secteur public ; baisse du reste à charge et des dépenses catastrophiques
pour les malades chroniques ; choix des filières privée et remboursement plus fréquent chez les
plus aisés, instruits, urbains (chapitre 2) ; à revenu donné, ce sont les plus riches qui
supportent le plus de dépenses catastrophiques, contrairement à Abu-Zaineh et al. (2013) (p. 148).

### 3.3 Séries et chiffres reproduits par la thèse, avec leur source

| Page | Objet | Valeurs | Source déclarée par l'auteure | Usage |
|---|---|---|---|---|
| p. 33, tab. 1.5 | taux de couverture, % | 54,6 (1987) ; 63,0 (1992) ; 80,7 (1997) ; 82,6 (1998) ; 84,2 (2001) ; 85,5 (2004) ; 87 (2005) ; 90,5 (2006) ; 91,9 (2007) | « Tunisie : principaux indicateurs économiques et sociaux (1987-2007) », Achouri 2004, Achour 2011 | **seconde main**, définition du taux non donnée (sécurité sociale + AMG ?) ; à ne pas tracer sans le primaire |
| p. 46, fig. 1.17 | financement État / CSS / privé, 1980-2007 | graphique **sans valeurs** | CNS-OMS | inutilisable |
| p. 47, fig. 1.18 | dépense directe par personne, 1975-2005 | graphique sans valeurs | INS | inutilisable |
| p. 47, tab. 1.6 | financement des prestataires en 2005 : public = MSP 58,3 %, CNSS 18,6 %, CNRPS 6,6 %, ménages 16,4 % ; privé = assurance groupe 9,4 %, mutuelles 4,0 %, CNSS 8,7 %, CNRPS 7,2 %, ménages 70,6 % | une année | CNS | citer seulement |
| p. 47, tab. 1.7 | dépenses de santé des ménages par structure : privé 81,64 % (2000), 82,64 % (2005) ; par tête 70,9 DT (2000), 111,6 DT (2005) | deux années | enquêtes ménages INS, via rapport OASIS 2014 | citer |
| p. 47, tab. 1.8 | dépenses de soins des ménages par catégorie, 2000 et 2005 (produits pharmaceutiques 26,3 → 47,5 DT) | deux années | INS, volet budget | citer |
| p. 48, tab. 1.9 | dépense de soins par personne en 2005 : 112,1 DT national ; 10,4 DT 1er décile ; 280,8 DT dernier décile | une année | INS 2005, via rapport technique « Analyse du système de financement de la santé » | citer |
| p. 56, fig. 1.19 | répartition de la population en 2010 : filière publique 48,0 % ; privée 8,4 % ; remboursement 11,5 % ; soins gratuits 5,5 % ; tarifs réduits 18,5 % ; non assurés 8,0 % | une année | « CNAM et MAS 2011 » | l'auteure la conteste p. 75 (méthode non décrite) |
| p. 62-63, tab. 1.12 | **dépenses CNAM par secteur, MDT** : voir § 3.4 | 2007-2010 | « CNAM 2012 » (présentation Chiha, COOPAMI) | relais |
| p. 63, tab. 1.11 | dépense par filière 2010 : publique 689,3 MDT ; remboursement + privée 514,1 MDT ; AMG 267,0 MDT ; assurance privée 146,2 MDT ; par assuré 315,9 DT (publique), 728,0 DT (privée + remb.), 379,3 DT (AMG) | une année | annuaire CNAM 2010, Arfa et Elgazzar 2013, FTUSA 2011 | citer ; note 56 : frais de gestion CNAM « estimés à 10 % » |
| p. 66, tab. 1.13 | affiliés CNSS 1 820 339 (2005), 2 604 425 (2010) ; CNRPS 712 951, 810 951 ; non assurés 1 301 000 (2005), 844 000 (2010) individus | deux années | CNSS, CNRPS, INS ; CNAM et MAS 2011 | citer |
| p. 74, fig. 2.1 | population par couverture selon l'EBCNV 2010 : non assurés 20,7 % ; publique 42,1 % ; privée 9,5 % ; remboursement 8,7 % ; AMG1 3,9 % ; AMG2 13,7 % ; autres 1,4 % | une année | calcul de l'auteure, EBCNV 2010 | étude ; **contredit** la fig. 1.19 (8 % de non assurés) |
| p. 75 | reste à charge = 41,2 % des dépenses totales de santé en 2010 | une année | CNS | citer |

### 3.4 Dépenses de la CNAM par secteur, 2007-2010 (thèse, tableau 1.12, p. 63)

| Année | Structures publiques (MDT) | Structures privées (MDT) | Soins à l'étranger (MDT) | Total imprimé (MDT) | Parts imprimées pub./priv. (%) |
|---|---:|---:|---:|---:|---|
| 2007 | 454,1 | 172,6 | 7,9 | 634,6 | 71,2 / 27,6 |
| 2008 | 514,2 | 261,8 | 9,5 | 788,7 | 65,2 / 33,2 |
| 2009 | 609,5 | 395,1 | 12,2 | 1 015,8 | 60,0 / 38,9 |
| 2010 | 690,5 | 515,1 | 13,4 | 1 217,8 | 56,7 / 42,3 |

Incohérences internes à signaler : en 2007, les montants donnent 71,6 % / 27,2 % et non les
parts imprimées (qui sont celles de la Lettre du CRES) ; la somme des trois postes diffère du
total imprimé de +0,0 (2007), −3,2 (2008), +1,0 (2009), +1,2 MDT (2010). Le texte (p. 62) cite
encore « 45 % en 2013 (CNS 2013) » et attribue les 27,6 % de 2007 au rapport OASIS 2014.
**Statut** : relais (famille C) d'une publication CNAM non détenue ; ne peut pas être raccordé à
la Lettre (2011-2012) sans le primaire, ni aux comptes de la santé 2012-2014 (§ 4.3, rupture de
nomenclature).

---

## 4. Ben Abdelaziz et al., *La Tunisie médicale*, 2018 — comptes de la santé 2012-2014 (famille B)

- **Référence** : Ahmed Ben Abdelaziz, Sina Haj Amor, Ines Ayadi, Mohamed Khelil, Chokri
  Zoghlami, Sami Ben Abdelfattah, « Le financement des soins de santé en Tunisie. État actuel des
  dépenses de soins et perspectives de socialisation, sur le chemin de la couverture santé
  universelle », *La Tunisie médicale*, 2018, vol. 96, n° 10, pp. 789-807. Deux coauteurs sont
  membres du comité des comptes de la santé et de la CNAM (p. 789).
- **Fichier** : `tunisia-data/data/raw/caisses/sante-etudes/tunis_med_2018_ben_abdelaziz_financement.pdf`,
  19 p., SHA-256 `23a22da3da7164c6c51547b7d9a00f64bee98c9932949a95f087ce881b1db6f9`, URL
  <https://latunisiemedicale.com/pdf/Vol%2096-10-N27.pdf>.
- **Méthode** (pp. 791-792) : synthèse des **comptes de la santé 2012-2014** calculés par le
  groupe multisectoriel du pôle d'économie de la santé du ministère, selon la méthodologie OMS
  (SHA, logiciel HAPT de Health Systems 20/20), validés par la commission de pilotage ; données
  du ministère de la Santé, Défense, Intérieur, CNAM, assurances et mutuelles, INS (ménages),
  direction générale des impôts. Les auteurs comparent dix indicateurs à des **seuils de
  référence fixés par eux** (tableau 8) : cette partie est une appréciation, non une mesure.
  Définitions : DTS = dépenses courantes + formation brute de capital (encadré 1, p. 792).
- **Rapport aux comptes OMS du chapitre** : même méthode (SHA) que la base GHED du chapitre,
  mais les **DTS incluent l'investissement** alors que la série OMS du chapitre est la **dépense
  courante**. Les ratios au PIB ci-dessous sont **cités** de l'article (base du PIB non dite) : ne
  pas les raccorder à la série OMS 2018-2023.

### 4.1 Séries prêtes à tracer (tableaux 1 et 2, p. 794)

| Indicateur | 2012 | 2013 | 2014 |
|---|---:|---:|---:|
| Dépenses totales de santé (MDT) | 4 985,2 | 5 362,7 | 5 715,5 |
| Dépenses publiques de santé (% DTS) | 54,6 | 58,2 | 57,0 |
| Sécurité sociale (% des dépenses publiques de santé) | 57,8 | 60,1 | 56,9 |
| Paiements directs (% DTS) | 38,2 | 37,5 | 36,6 |
| Formation de capital (% DTS) | 6 | 4 | 3,7 |
| DTS / PIB (%) | 7,1 | 7,1 | 7,1 |
| Dépenses publiques de santé / PIB (%) | 3,87 | 4,13 | 4,04 |
| DTS par habitant (DT) | 463 | 493 | 519 |
| *Sources de financement des dépenses courantes (%)* : ménages | 41,0 | 39,1 | 38,0 |
| CNAM | 33,9 | 36,4 | 33,4 |
| Ministère de la Santé | 23,9 | 23,3 | 25,2 |
| Autres (ministères et assurances privées) | 1,2 | 1,2 | 1,4 |

**Traçables** : les montants (DTS, DTS par habitant) et les parts. **À citer seulement** : les
deux ratios au PIB (DTS/PIB, DPS/PIB) ; les porter sur une figure ferait d'eux des ratios
*employés* par le précis, soumis à la règle de la base du PIB que l'article ne permet pas de
remplir. Cités entre guillemets avec leur référence, ils se donnent tels quels, sans écrire dans
le texte visible que la base n'est pas dite.

Cohérence interne vérifiée : tableaux 1 et 2 cohérents entre eux. En revanche la somme des
secteurs du tableau 3 (dépense courante) donne 4 647,9 / 5 137,8 / 5 706,2 MD ; rapportée aux
DTS du tableau 1, elle implique une part de capital de 6,8 / 4,2 / **0,2 %**, contre 6 / 4 /
**3,7 %** imprimés : l'année 2014 ne boucle pas.

Noter : « paiements directs » rapportés aux **DTS** (tableau 1) et « ménages » rapportés aux
**dépenses courantes** (tableau 2) sont deux dénominateurs différents.

### 4.2 Dépenses de la CNAM par secteur et par fonction (tableau 4, p. 795), MDT

| Poste | 2012 | 2013 | 2014 |
|---|---:|---:|---:|
| Secteur privé | 797,680 | 889,400 | 861,030 |
| Secteur public | 527,210 | 548,380 | 474,500 |
| Secteur parapublic | 301,640 | 397,020 | 382,700 |
| Administration du système de santé | 95,740 | 110,670 | 104,500 |
| Soins à l'étranger | 13,850 | 11,530 | 13,200 |
| *Somme des secteurs (calculée)* | *1 736,1* | *1 957,0* | *1 835,9* |
| Part du privé (imprimée, %) | 45,95 | 45,45 | 46,90 |
| Soins ambulatoires et hospitalisation | 942,100 | 1 228,900 | 1 238,400 |
| Biens médicaux | 762,730 | 838,470 | 669,000 |
| Services auxiliaires | 63,500 | 65,730 | 136,290 |
| Réhabilitation | 11,540 | 12,660 | 30,980 |

**Le tableau 4 ne boucle pas** (calculs de cette note) :
- somme des **secteurs** : 1 736,1 / 1 957,0 / 1 835,9 MD ;
- somme des **fonctions** (ambulatoire et hospitalisation, biens médicaux, services auxiliaires,
  administration 95,74 / 110,67 / 104,55, réhabilitation, prévention 6,62 en 2014) :
  1 875,6 / 2 256,4 / 2 185,8 MD — total que confirment les parts imprimées (942,1 / 0,5023 ≈
  1 875,6) ;
- troisième estimation, parts de la CNAM du tableau 2 appliquées aux dépenses courantes du
  tableau 3 : ≈ 1 576 / 1 870 / 1 906 MD.

Les deux moitiés du tableau diffèrent de 140 à 350 MD selon l'année. **Statut : à citer avec
ces incohérences, pas à tracer** ; si une figure est voulue, une seule moitié, nommée comme
telle (par exemple la part du privé, 45,95 / 45,45 / 46,90 %, imprimée sur la moitié
« secteurs »).

Autres tableaux utiles : tableau 3 (dépenses courantes par secteur et fonction), tableau 5
(paiements directs des ménages dans le privé, dont pharmacies 599,6 / 670,0 / 588,4 MD),
tableau 7 (financement des hôpitaux de 3e ligne : CNAM 322,5 / 342,9 / 334,3 MD, soit 41,5 /
40,8 / 43,5 %), p. 795-796.

### 4.3 Recoupements

- **Rupture de nomenclature avec 2007-2012.** En 2012, public + parapublic (527,2 + 301,6 =
  828,9 MD) ≈ « secteur public » de la Lettre du CRES (826 MD) ; mais le privé (797,7 MD) ≠ 708 MD.
  La série 2012-2014 n'est **pas** la continuation de celle de 2007-2012 : autre classement
  (SHA), autre périmètre (la ligne « administration » de la CNAM est incluse).
- **CNAM dans les comptes de la santé contre états financiers** : aucune des trois estimations
  du § 4.2 ne suit les charges techniques des états (1 738,8 / 1 802,8 / 1 900,9 MD) ; la
  rencontre de la moitié « secteurs » avec les états en 2012 (1 736,1 MD) est isolée. À ne pas
  présenter comme la même grandeur.
- **Paiements directs** : 38,2 / 37,5 / 36,6 % des DTS (comptes de la santé) ; la Lettre du CRES
  n° 7 donne 37,5 % pour 2013 (même chiffre, autre relais) ; Ismail et Zaouali (2022) donnent
  39,8 % en 2015 « selon la Banque mondiale » (indicateur de la dépense **courante**, § 6).

---

## 5. Actes du colloque ATDSRP, 27-28 mars 2017 (FES) (famille C)

- **Fichiers** déjà archivés : `sante-avant-2004/fes_atdsrp_2017_contenu_fr_50.pdf` (194 p.) et
  `…_ar_50.pdf` (126 p.), `sources/sante-avant-2004-urls.csv`. Publication : *Revue tunisienne de
  droit social*, numéro des actes ; programme pp. 4-8 (PDF).
- **Séance « L'assurance maladie : réalité et perspectives de réforme »** (28 mars 2017) :
  Ryadh Ben Abbès (inspecteur général, ministère de la Santé), « Défis et pistes de réforme de
  l'assurance maladie » — **diapositives en arabe seulement**, partie AR pp. 59-80 ; Chokri Arfa
  (INTES), « Atteindre la couverture universelle au moyen de l'assurance maladie sociale » —
  diapositives, partie FR pp. 116-130 (numéros de la revue).
- **Ce qui est daté et chiffré** :
  - Ben Abbès, p. 70 (AR) : parts des affiliés par filière 2008-2014, étiquetées — publique
    76,1 / 75,3 / 71,7 / 68,9 / 65,9 / 62,2 / 58,9 % ; privée 10,2 / 10,3 / 11,7 / 13,0 / 14,4 /
    16,9 / 19,4 % ; remboursement 13,6 / 14,5 / 16,5 / 18,1 / 19,7 / 20,9 / 21,7 %. **Aucune
    source imprimée.** Ces parts sont exactement celles qu'on calcule sur les effectifs de la
    CNAM (indicateurs globaux 2021, p. 4 ; ex. 2014 : 1 754 764 / 2 981 058 = 58,9 %) : **doublon**
    d'une source déjà au chapitre, rien à ajouter.
  - Ben Abbès, p. 66 (AR) : en 2013, secteur public — financement État 66,70 % / caisse 33,30 %,
    contre 70 % des usagers affiliés à la caisse et 30 % porteurs de carte de soins gratuits.
    **Sans source** ni définition du champ : à ne pas reprendre.
  - Ben Abbès, p. 68 (AR) : « évolution des dépenses de l'assurance maladie », huit valeurs
    (683 ; 1 015 ; 1 212 ; 1 364 ; 1 514 ; 1 623 ; 1 735 ; 1 841) **sans années, sans unité, sans
    source** (diapositive rendue en entier) : inutilisable.
  - Ben Abbès, p. 69 (AR) : dépenses par secteur 2010-2014, deux courbes **sans valeurs** :
    inutilisable.
  - Arfa, p. 126 : tableaux 2015-2025 (DTS à prix constants 7 167,5 → 8 084,9 ; DTS/PIB 8,5 →
    7,8 ; dépenses publiques de santé 63,7 → 72,1 % des DTS ; ministère / autres ministères /
    assurance maladie 35,7 / 10,4 / 53,8 en 2015, dont la somme fait 99,9 : ce sont des **parts
    des dépenses publiques**, non des DTS). Ce sont des **résultats de projection** d'un modèle
    (« Nos calculs ! », p. 122 ; hypothèses p. 123), **non des observations** : ne pas tracer
    comme série. Les pp. 124 et 126-128 sont des graphiques sans valeurs lisibles.
- **Conclusion** : les actes n'apportent aucune série observée, datée et sourcée qui manque au
  chapitre. Les citer, s'il le faut, comme témoignage du débat de 2017, pas comme source chiffrée.

---

## 6. Autres publications relevées

### 6.1 *Revue tunisienne de biologie clinique* (RTBC) n° 19, octobre 2006 — référence identifiée

« RTBC » est la ***Revue tunisienne de biologie clinique*** (rtbc.org.tn). Le n° 19 (octobre 2006)
porte un « dossier spécial » dont l'article pertinent est :
**S. Ben Cheikh et N. Achour (ministère de la Santé publique, direction des études et de la
planification), « Les indicateurs de la santé en Tunisie », *Rev Tun Biol Clin* 2006, 19 : 6-12.**
L'article voisin (M.A. Memmi, « La biologie médicale en Tunisie », pp. 13-16) est hors sujet.

- **Fichier** : `tunisia-data/data/raw/caisses/sante-etudes/rtbc_2006_19_ben_cheikh_achour_indicateurs.pdf`,
  7 p., SHA-256 `49e4025c23f8291d2807206fe44df10b9345606a12f080389e0a04d7129425fb`, URL
  <https://rtbc.org.tn/ojs/index.php/rtbc/article/download/228/204/482>.
- **Nature** : article descriptif d'agents du ministère, sans méthode ; tableaux sourcés « 50 ans
  d'indépendance, MSP », « carte sanitaire 2004 », INSP.
- **Chiffres utiles** (pp. 11-12) : CNSS 1,950 million d'affiliés, CNRPS 0,746 million ; AMG 1
  0,17 million et AMG 2 0,548 million d'affiliés en 2005 (quote-part annuelle de 10 DT) — la
thèse Ismail (tableau 1.13.1, p. 66) donne les mêmes nombres (170 et 548) en **milliers de
ménages** : l'unité est incertaine ;
  « plus de 80 % » de la population couverte ; en **2004**, financement : budget de l'État
  21,8 %, assurance maladie ≈ 23,3 %, ménages ≈ 53,6 % (dont ≈ 9 % pris en charge par assurances
  groupe et mutuelles), médecine d'entreprise ≈ 1,3 % ; dépense de santé / PIB 4,2 % (1985) →
  5,6 % (2003) ; dépense par habitant 39 DT (1985) → 197,7 DT (2004). Ratios **cités**, base du
  PIB non dite.
- **Recoupement** : la note `sante-couverture-avant-2004-2026-10-14.md` ne porte pas ces parts
  de 2004 (aucune occurrence de 21,8 / 23,3 / 53,6) ; à confronter, si on les cite, aux comptes
  2004-2005 de l'INSP (Arfa, Souiden, Achour, 2007 ; § 9) et à l'étude Banque mondiale 2006 déjà
  versée sur la branche `chantier/sante-regimes-avant-2004` (`bm-2006-etude-secteur-sante`).

### 6.2 Ismail et Zaouali, *EMHJ*, 2022 (famille C)

Safa Ismaïl et Nejia Zaouali, « Santé et assurance maladie en Tunisie : les enjeux de la réforme
de 2004 », *Eastern Mediterranean Health Journal*, 2022, 28(6) : 444-453,
DOI 10.26719/emhj.22.040. Fichier
`sante-etudes/emhj_2022_ismail_zaouali_reforme_2004.pdf` (SHA-256 `73abe859…`). **Évaluation
qualitative**, sans données propres (résumé, p. 444). Chiffres relayés : paiements directs
42,9 % (2005) → 39,8 % (2015), État 28,8 → 24,0 %, CNAM 21,8 → 32,3 % « selon la Banque
mondiale » (tableau 1, suite, p. 448 ; réf. 7 = indicateur `SH.XPD.OOPC.CH.ZS`, **dépense courante**,
donc famille OMS) ; filières 2015 : publique 54 %, privée 18,5 %, remboursement 21 % (p. 445,
réf. 6 = enquête INS 2015) ; part privée des dépenses CNAM « 27 % en 2007 à 47 % en 2014 »
(tableau 1, p. 447, réf. 15-17 : Lettre du CRES n° 5, Ben Abdelaziz 2018, CNAM — la Lettre s'arrête à 2012,
l'origine du 47 % n'est pas identifiable). À ne citer que pour l'appréciation qualitative.

### 6.3 Autres publications du CRES

Inventaire de la page « Lettre du CRES » (`http://www.cres.tn/index.php?id=116`, deux pages,
8 numéros) : n° 1 (oct. 2013, rendement des retraites), n° 2 (déc. 2013, pénibilité), n° 3
(févr. 2014, pensions du secteur public, déjà archivée), n° 4 (mai 2014, pensions RSNA), n° 5
(santé, ci-dessus), n° 6 (avril 2015, retraite par capitalisation), n° 7 (déc. 2015, socles),
n° 8 (janv. 2023, AT/MP, déjà au chapitre). **Seules les n° 5, 7 et 8 touchent à la santé.**

- *Lettre* n° 7 (Mohamed Belhaj Hammada, Haythem Ben Sassi, Amen Allah Derouiche), p. 3 :
  AMG I 7,3 % et AMG II 23,7 % de la population (« rapport préliminaire CRES 2015 »), 64 %
  couverts par la sécurité sociale, « taux de couverture global de 94 % » ; dépenses publiques de
  santé 2013 = 4,4 % du PIB (« Quels chemins vers la couverture sanitaire universelle ? »,
  ministère de la Santé, 2014) ; ménages 37,5 % du financement en 2013. Archivée :
  `cres/cres_lettre_n7_2015_socles.pdf`.
- Note d'orientation CRES/UNICEF, *Les garanties du socle national de protection sociale :
  faisabilité, coût et financement*, août 2019, p. 14, tableau 1 (couverture **2016**) :
  population 11 295 787 ; assurance maladie 58 % ; AMG 1 824 482 (7,3 %) ; AMG 2 1 975 459
  (17,5 %) ; chômeurs sans couverture 632 500 (5,6 %) ; autres sans couverture 297 916 (2,6 %) ;
  source : « Étude de faisabilité des trois garanties du socle », CRES, avril 2019 (non en ligne,
  § 9). Une année : utile pour l'état de la couverture, pas pour une série. Archivée :
  `cres/cres_unicef_2019_note_socle_garanties.pdf`.
- *Rapport national* CRES/BAD de mai 2017 sur l'évaluation du PNAFN et de l'AMG II
  (`uploads/tx_wdbiblio/Rapport_CRES_mai_2017.pdf`) : repéré, **non téléchargé ni lu** ; il relève
  de l'assistance médicale, à reprendre pour cette section.

### 6.4 CNAM en ligne

- La page « Statistiques » (`https://www.cnam.nat.tn/stat.jsp`) ne liste que les documents déjà
  archivés dans `cnam/`. **Aucun rapport d'activité** n'y figure.
- Les « rapports annuels » 2013-2022 de la page `open_gov.jsp` (`doc/upload/rapport2013.pdf` …
  `rapport_annuel_2022.pdf`) sont des **rapports sur l'accès à l'information** (loi organique
  n° 2016-22), en arabe (vérifié sur 2013, 2018 et 2022) : **sans données de dépense**. Ne pas
  les retélécharger.
- Les `ANNUEL_2018-2021.pdf` et `statistiques_2022.pdf` de `cnam/` sont les bilans AT/MP (arabe),
  déjà décrits dans `sources/cnam-statistiques.md`.

---

## 7. Séries prêtes à tracer — récapitulatif

| Série | Années | Unité | Famille | Source | Où |
|---|---|---|---|---|---|
| Charges techniques, charges administratives, prestations décaissées de la CNAM | **2011-2015** (prolonge 2016-2021) | MD courants | A | `cnam-etats-financiers-2011-2015`, pp. 3-4 (lu à l'image) | `#sec-sante-cnam-comptes`, `fig-sante-cnam-comptes` |
| Bénéficiaires de l'assurance maladie (affiliés + ayants droit) | 2008-2013 | millions de personnes | C | Lettre du CRES n° 5, p. 3, graphe 4 | `#sec-soins-longue-periode` (panneau distinct des affiliés CNAM) |
| Dépenses totales de santé, part publique, part sécurité sociale, paiements directs, DTS/hab., sources de financement (hors ratios au PIB, à citer seulement) | 2012-2014 | MDT, % | B | Ben Abdelaziz et al. 2018, tableaux 1-2, p. 794 | `#sec-soins-paiements-directs`, en amont de la série OMS 2018-2023, **rupture** DTS/dépense courante |

Séries **à ne pas tracer** : dépenses de la CNAM par secteur et fonction 2012-2014 (Ben
Abdelaziz, tableau 4 : deux moitiés qui ne bouclent pas, § 4.2 — à citer) ; dépenses CNAM par secteur 2007-2010 (thèse, relais non sourcé au
primaire, incohérences internes) ; taux de couverture 1987-2007 (thèse, seconde main) ;
projections 2015-2025 (Arfa) ; diapositives Ben Abbès.

---

## 8. Références candidates (CSL-JSON)

Déjà présentes (sur `master`, `precis/fr/sante/references.json`) : `belloussaief2023-atmp`,
`cnam-etats-financiers-2016-2018`, `-2018-2019`, `-2020-2021`, `cnam-indicateurs-globaux-2021`,
`oms-ghed-comptes-sante-tunisie`, `oms-ghed-paiements-directs-tunisie`.
Présente sur `chantier/sante-regimes-avant-2004` seulement : `ismail-2015-these` (ajouter
`"publisher": "Université Paris-Dauphine"`), `bm-2006-etude-secteur-sante`.

À créer :

```json
[
  {
    "id": "cnam-etats-financiers-2011-2015",
    "type": "report",
    "title": "États financiers de la Caisse nationale d'assurance maladie, exercices 2011 à 2015",
    "author": [{"literal": "Caisse nationale d'assurance maladie"}],
    "URL": "http://www.cnam.nat.tn/doc/upload/fr_etat_fin_11_15.pdf",
    "note": "citation-key: cnam-etats-financiers-2011-2015\nDocument scanné, lu à l'image le 15 octobre 2026 : état du résultat p. 3 et flux de trésorerie p. 4, en milliers de dinars, exercices 2011-2015. Produits − charges techniques = marge brute imprimée pour les cinq années. Copie archivée dans tunisia-data (data/raw/caisses/cnam/, SHA-256 2db9a7ee…)."
  },
  {
    "id": "blel-chahed2014-depenses-cnam",
    "type": "article-journal",
    "title": "L'évolution des dépenses de la CNAM en assurance maladie",
    "title-short": "Blel et Chahed, Lettre du CRES n° 5, 2014",
    "author": [{"family": "Blel", "given": "Imen"}, {"family": "Chahed", "given": "Houda"}],
    "container-title": "La Lettre du CRES",
    "issue": "5",
    "publisher": "Centre de recherches et d'études sociales",
    "issued": {"date-parts": [[2014, 12]]},
    "URL": "http://www.cres.tn/uploads/tx_wdbiblio/Lettre__5.pdf",
    "note": "citation-key: blel-chahed2014-depenses-cnam\nNote d'étude, 4 p., sans méthode déclarée ; relaie les comptes nationaux de santé (2002, 2007), le rapport OASIS 2013, l'OMS (2013), les rapports d'activité de la CNAM et le rapport du Conseil national de l'assurance maladie de mai 2014. P. 3, graphe 4 : bénéficiaires 2008-2013 ; p. 4 : dépenses CNAM par secteur 2007 et 2012. Graphes 1, 2, 5, 6, 7 sans valeurs. Copie archivée dans tunisia-data (data/raw/caisses/cres/, SHA-256 9c3a145c…)."
  },
  {
    "id": "benabdelaziz2018-financement",
    "type": "article-journal",
    "title": "Le financement des soins de santé en Tunisie. État actuel des dépenses de soins et perspectives de socialisation, sur le chemin de la couverture santé universelle",
    "author": [
      {"family": "Ben Abdelaziz", "given": "Ahmed"}, {"family": "Haj Amor", "given": "Sina"},
      {"family": "Ayadi", "given": "Ines"}, {"family": "Khelil", "given": "Mohamed"},
      {"family": "Zoghlami", "given": "Chokri"}, {"family": "Ben Abdelfattah", "given": "Sami"}
    ],
    "container-title": "La Tunisie médicale",
    "volume": "96",
    "issue": "10",
    "page": "789-807",
    "issued": {"date-parts": [[2018]]},
    "URL": "https://latunisiemedicale.com/pdf/Vol%2096-10-N27.pdf",
    "note": "citation-key: benabdelaziz2018-financement\nSynthèse des comptes de la santé 2012-2014 (méthode OMS/SHA, groupe multisectoriel du ministère de la Santé). Tableaux 1-2 p. 794 (DTS, sources de financement), tableau 4 p. 795 (dépenses de la CNAM par secteur et fonction), tableau 8 p. 797 (indicateurs comparés à des seuils fixés par les auteurs). DTS investissement compris. Copie archivée dans tunisia-data (data/raw/caisses/sante-etudes/, SHA-256 23a22da3…)."
  },
  {
    "id": "ismail-zaouali2022-reforme",
    "type": "article-journal",
    "title": "Santé et assurance maladie en Tunisie : les enjeux de la réforme de 2004",
    "author": [{"family": "Ismaïl", "given": "Safa"}, {"family": "Zaouali", "given": "Nejia"}],
    "container-title": "Eastern Mediterranean Health Journal",
    "volume": "28",
    "issue": "6",
    "page": "444-453",
    "issued": {"date-parts": [[2022]]},
    "DOI": "10.26719/emhj.22.040",
    "URL": "https://applications.emro.who.int/EMHJ/V28/06/1020-3397-2022-2806-444-453-fre.pdf",
    "note": "citation-key: ismail-zaouali2022-reforme\nÉvaluation qualitative, sans données propres ; chiffres relayés (Banque mondiale, INS 2015, CRES). Copie archivée dans tunisia-data (data/raw/caisses/sante-etudes/, SHA-256 73abe859…)."
  },
  {
    "id": "bencheikh-achour2006-indicateurs",
    "type": "article-journal",
    "title": "Les indicateurs de la santé en Tunisie",
    "author": [{"family": "Ben Cheikh", "given": "S."}, {"family": "Achour", "given": "N."}],
    "container-title": "Revue tunisienne de biologie clinique",
    "issue": "19",
    "page": "6-12",
    "issued": {"date-parts": [[2006, 10]]},
    "URL": "https://rtbc.org.tn/ojs/index.php/rtbc/article/download/228/204/482",
    "note": "citation-key: bencheikh-achour2006-indicateurs\nDossier spécial ; auteurs : ministère de la Santé publique, direction des études et de la planification. Pp. 11-12 : couverture du risque maladie (CNSS, CNRPS, AMG 2005) et financement de la santé en 2004. Copie archivée dans tunisia-data (data/raw/caisses/sante-etudes/, SHA-256 49e4025c…)."
  },
  {
    "id": "cres2015-lettre7-socles",
    "type": "article-journal",
    "title": "Les socles nationaux de protection sociale : émergence du concept, meilleures pratiques internationales et pertinence pour la Tunisie",
    "author": [{"family": "Belhaj Hammada", "given": "Mohamed"}, {"family": "Ben Sassi", "given": "Haythem"}, {"family": "Derouiche", "given": "Amen Allah"}],
    "container-title": "La Lettre du CRES",
    "issue": "7",
    "publisher": "Centre de recherches et d'études sociales",
    "issued": {"date-parts": [[2015, 12, 31]]},
    "URL": "http://www.cres.tn/uploads/tx_wdbiblio/lettre_7_du_31_d%C3%A9cembre_2015_01.pdf",
    "note": "citation-key: cres2015-lettre7-socles\nP. 3 : couverture santé tunisienne (AMG I, AMG II, sécurité sociale), dépense publique de santé 2013, part des ménages 2013 ; chiffres relayés. Titre repris du descriptif de la page « Lettre du CRES » du site. Copie archivée dans tunisia-data (data/raw/caisses/cres/, SHA-256 1c1834b1…)."
  },
  {
    "id": "cres-unicef2019-socle-garanties",
    "type": "report",
    "title": "Les garanties du socle national de la protection sociale : faisabilité, coût et financement. Note d'orientation",
    "author": [{"literal": "Centre de recherches et d'études sociales"}],
    "publisher": "CRES ; UNICEF",
    "issued": {"date-parts": [[2019, 8]]},
    "URL": "http://www.cres.tn/uploads/tx_wdbiblio/note-dorientation-les-garanties-du-socle-national-de-la-protection-sociale-2019.pdf",
    "note": "citation-key: cres-unicef2019-socle-garanties\nP. 14, tableau 1 : population couverte et non couverte par l'assurance maladie et l'AMG en 2016, d'après l'étude de faisabilité du CRES (avril 2019). Copie archivée dans tunisia-data (data/raw/caisses/cres/, SHA-256 34c090c4…)."
  }
]
```

À ne créer que si on cite les actes de 2017 (déconseillé pour des chiffres) :
`arfa2017-couverture-universelle` — Chokri Arfa, « Atteindre la couverture universelle au moyen
de l'assurance maladie sociale en Tunisie », *Revue tunisienne de droit social*, actes du
colloque ATDSRP des 27-28 mars 2017, pp. 116-130, URL
<https://tunisia.fes.de/fileadmin/user_upload/documents/publications/Contenu_FR_50.pdf>.

---

## 9. Lacunes et primaires non détenus

| Document | Relayé par | Adresses essayées le 15/10/2026 | État |
|---|---|---|---|
| Rapport du Conseil national de l'assurance maladie, mai 2014 (exercice 2013), et suivants | Lettre CRES n° 5 (pp. 1-3) | recherche web (« Conseil national de l'assurance maladie » Tunisie rapport 2013/2014) ; pages `stat.jsp` et `open_gov.jsp` de la CNAM | introuvable en ligne |
| Rapports d'activité / annuaires statistiques de la CNAM (2007-2014), « CNAM 2012 » (Chiha, COOPAMI) | Lettre CRES n° 5 (graphes 5-6) ; thèse, tab. 1.11-1.12 | `cnam.nat.tn/stat.jsp`, `open_gov.jsp` (rapports d'accès à l'information seulement) | introuvable ; les séries dépenses par secteur 2007-2012 restent sans primaire |
| Comptes de la santé 2012, 2013, 2014 (ministère de la Santé, pôle d'économie de la santé) | Ben Abdelaziz 2018 | `santetunisie.rns.tn/fr/index.php/actualites/460-…comptes-de-la-sante-pour-les-annees-2012-et-2013` : hors ligne (pas de réponse) ; capture des archives du web du 07/03/2024 : l'identifiant 460 sert à une autre actualité, aucun PDF de comptes | introuvable |
| Comptes nationaux de la santé 1997-1998, 2000, 2004-2005 (INSP ; Arfa, Souiden, Achour, nov. 2007) | Lettre CRES n° 5 (tab. 1) ; thèse (tab. 1.6) | non cherché au-delà de la bibliographie de la thèse | à chercher |
| Rapport OASIS 2013 / 2014 (OMS) | Lettre CRES n° 5 ; thèse | non cherché | à chercher |
| Étude de faisabilité des trois garanties du socle, CRES, avril 2019 | note CRES/UNICEF 2019 | pages « Études et recherches » du site du CRES (pagination au-delà de la p. 1 non atteinte) | non trouvée |
| Ventilation des charges techniques CNAM 2011-2015 par régime | — | états financiers synthétiques seulement | absente des publications |

Autres lacunes :
- La base GHED de l'OMS remonte à **2000** pour les indicateurs déjà utilisés au chapitre
  (2018-2023). Les parts « sécurité sociale », « paiements directs » relayées par la Lettre
  (10,8 % en 1996 → 26,3 % en 2011 ; 40 % en moyenne 1995-2011) et par Ismail et Zaouali (2005,
  2015) seraient mieux **tirées directement de GHED 2000-2023** (même famille, une seule
  méthode) que citées de seconde main. TODO pour le rédacteur ou une passe documentaire sur GHED.
- Le taux de couverture 1987-2007 (thèse, p. 33) n'a ni définition ni primaire détenu
  (« Principaux indicateurs économiques et sociaux 1987-2007 ») : ne pas l'utiliser en l'état.

---

## 10. Notions à glossaire (`precis/glossaire.yml`, à vérifier)

| Terme FR | AR (indicatif) | Source canonique pressentie |
|---|---|---|
| Charges techniques (d'une caisse) | الأعباء الفنية | états financiers CNAM, p. 3 |
| Résultat technique (marge brute) | النتيجة الفنية | idem |
| Prestations sociales décaissées | — | idem, p. 4 |
| Bénéficiaire (affilié et ayants droit) | المنتفع / المضمون الاجتماعي وأولي الحق | Lettre du CRES n° 5, p. 3, note 6 |
| Affections prises en charge intégralement (APCI) | الأمراض المزمنة المتكفل بها كليا | Lettre du CRES n° 5, p. 4 ; arrêté fixant la liste (JORT) |
| Filière publique / filière privée / système de remboursement | المنظومة العمومية / المنظومة الخاصة / منظومة استرجاع المصاريف | Ben Abbès, actes 2017, p. 70 (AR) ; décret n° 2007-1367 |
| Dépenses totales de santé (DTS) / dépense courante de santé | النفقات الجملية للصحة | Ben Abdelaziz 2018, encadré 1, p. 792 ; OMS |
| Comptes de la santé (SHA) | الحسابات الوطنية للصحة | idem |
| Dépense catastrophique de santé | — | thèse Ismail, p. 48 note 43 (définition OMS) et p. 117 |
| Différences de différences | — | thèse Ismail, pp. 120-122 (notion de méthode, à ne mettre au glossaire que si le chapitre l'emploie) |

---

## 11. Recherches infructueuses — fiches proposées pour `docs/recherches.yml`

Ces objets ne sont pas des textes du *Journal officiel* : aucune requête `jort_cache`, `iort` ou
plein texte n'a été lancée, donc `requetes` ne porte que `depuis`. `verifier --avertissements`
signalera l'absence d'`iort_ar` ; c'est attendu. Les ancres `ou` existent dans le chapitre au
15/10/2026. **Chaque fiche entre dans `docs/recherches.yml` dans le même changement que son
ancre `<!-- RECHERCHE r-… -->` dans le `.qmd`** (le contrôle `verifier` exige la correspondance
ancres ⇔ fiches) ; une fiche sans constat écrit reste dans cette note.

```yaml
- id: r-sante-conseil-national-am-rapports
  objet: rapports annuels du Conseil national de l'assurance maladie (loi n° 2004-71, art. 21), dont celui de mai 2014 sur l'exercice 2013 cité par la Lettre du CRES n° 5
  ou: [precis/fr/sante/_couverture.qmd#sec-soins-longue-periode]
  requetes:
    depuis: 2004-08-02
  passes:
  - date: 2026-10-15
    role: documentaliste
    sources: [web]
    couverture: 'Recherche web « Conseil national de l''assurance maladie » Tunisie rapport 2013 OR 2014 CNAM : seuls des relais (Lettre du CRES n° 5, rapport ATDDS/FTDES 2016, assistance technique Banque mondiale 2016). Site de la CNAM : https://www.cnam.nat.tn/stat.jsp (statistiques, états financiers, bilans AT/MP) et https://www.cnam.nat.tn/open_gov.jsp (rapports sur l''accès à l''information 2013-2022) : aucun rapport du Conseil. Lacunes : site du ministère des Affaires sociales et archives du web non parcourus ; Journal officiel non interrogé (un arrêté de composition du Conseil pourrait exister). Note : docs/notes/sante-series-etudes-2026-10-15.md, § 9.'
    couvert_jusqu_au: 2026-10-15
    resultat: aucun

- id: r-sante-cnam-rapports-activite
  objet: rapports d'activité et annuaires statistiques de la CNAM (2007-2014), source des dépenses par secteur public, privé et étranger relayées par la Lettre du CRES n° 5 et la thèse Ismail
  ou: [precis/fr/sante/_couverture.qmd#sec-sante-cnam-etude]
  requetes:
    depuis: 2007-07-01
  passes:
  - date: 2026-10-15
    role: documentaliste
    sources: [web]
    couverture: 'https://www.cnam.nat.tn/stat.jsp : seulement indicateurs globaux 2018 et 2021, prestations sanitaires 2018 et 2021, états financiers 2011-2021, bilans AT/MP ; https://www.cnam.nat.tn/open_gov.jsp : « rapport2013.pdf » à « rapport_annuel_2022.pdf » = rapports sur l''accès à l''information (vérifiés 2013, 2018, 2022). Recherche web « rapport annuel » OR « rapport d''activité » CNAM : rien. Lacunes : archives du web de cnam.nat.tn non parcourues ; présentation COOPAMI de 2012 (M. Chiha) non cherchée. Note : docs/notes/sante-series-etudes-2026-10-15.md, § 6.4 et § 9.'
    couvert_jusqu_au: 2026-10-15
    resultat: aucun

- id: r-sante-comptes-sante-2012-2014
  objet: rapports des comptes de la santé de la Tunisie pour 2012, 2013 et 2014 (ministère de la Santé, pôle d'économie de la santé, méthode OMS/SHA)
  ou: [precis/fr/sante/_couverture.qmd#sec-soins-paiements-directs]
  requetes:
    depuis: 2012-01-01
  passes:
  - date: 2026-10-15
    role: documentaliste
    sources: [web]
    couverture: 'Recherche web « comptes de la santé » Tunisie 2012 2013 2014 : article de synthèse Ben Abdelaziz et al. 2018 (récupéré) ; page http://www.santetunisie.rns.tn/fr/index.php/actualites/460-le-financement-de-la-sante-en-tunisie-resultats-des-comptes-de-la-sante-pour-les-annees-2012-et-2013 : aucune réponse du serveur ; capture des archives du web du 7 mars 2024 : l''identifiant 460 affiche une autre actualité, aucun PDF des comptes. Lacunes : index des captures de santetunisie.rns.tn/images/ non filtré utilement ; portail de l''OMS (rapports nationaux des comptes de la santé) non parcouru. Note : docs/notes/sante-series-etudes-2026-10-15.md, § 9.'
    couvert_jusqu_au: 2026-10-15
    resultat: aucun
```

---

## 12. Fichiers et catalogue

- PDF ajoutés à `tunisia-data` (hors git, `data/raw/caisses/` ignoré, vérifié par
  `git check-ignore`) :
  - `cres/cres_lettre_n5_2014_depenses_cnam.pdf`, `cres/cres_lettre_n7_2015_socles.pdf`,
    `cres/cres_unicef_2019_note_socle_garanties.pdf` ;
  - `sante-etudes/` (**dossier nouveau** : ni CRES ni CNAM) :
    `rtbc_2006_19_ben_cheikh_achour_indicateurs.pdf`,
    `emhj_2022_ismail_zaouali_reforme_2004.pdf`, `tunis_med_2018_ben_abdelaziz_financement.pdf`.
- Catalogue nouveau, non suivi : `tunisia-data/sources/sante-series-etudes-urls.csv` (URL, date de
  collecte, octets, SHA-256, pages). Aucun fichier suivi de `tunisia-data` modifié.
- Déjà archivés, réutilisés : `sante-avant-2004/hal_tel-01300569.pdf`,
  `sante-avant-2004/fes_atdsrp_2017_contenu_{fr,ar}_50.pdf`, `cnam/fr_etat_fin_11_15.pdf`,
  `cnam/BILAN2016_2018.pdf`, `cnam/indicateurs_globaux_2021_fr.pdf`.

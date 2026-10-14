# CNAM — charges, décaissements et postes de soins identifiés, 12 octobre 2026

Lecture de la couche texte uniquement ; aucune image ouverte. Sources récupérées
dans `tunisia-data/data/raw/caisses/cnam/`, adresses dans
`sources/caisses-sociales-urls.csv`, fiche `sources/cnam-statistiques.md`.
Les quatre adresses officielles ont répondu `206 application/pdf` le 12 octobre
2026 avec suivi de leur redirection HTTPS et vérification du contenu.

## États financiers, exercices 2016-2021

Trois publications : `BILAN2016_2018.pdf`, `BILAN2019_2018.pdf` et
`BILAN_2020-2021.pdf`. Leur **page 3** donne les charges techniques et les
charges administratives du compte de résultat ; la **page 4** donne les
« décaissements des prestations sociales » de l'état des flux. Unité imprimée :
**milliers de dinars** ; les montants ci-dessous sont les nombres imprimés.
Pour 2018, deux publications concordent. Les charges techniques regroupent
les régimes d'assurance maladie, d'assurances sociales et d'accidents du travail
et maladies professionnelles. Les décaissements sont un **flux de trésorerie**
distinct des charges comptabilisées : leur écart ne se présente pas comme un
solde d'assurance maladie ni comme la dette d'un prestataire.

| Exercice | Charges techniques (milliers de D) | Charges administratives (milliers de D) | Prestations sociales décaissées (milliers de D) | Édition retenue |
|---|---:|---:|---:|---|
| 2016 | 2 074 070 | 140 772 | 1 486 719 | 2016-2018 |
| 2017 | 2 191 280 | 146 713 | 1 437 156 | 2016-2018 |
| 2018 | 2 236 255 | 219 538 | 2 156 471 | 2018-2019, concordant avec 2016-2018 |
| 2019 | 2 367 411 | 171 464 | 2 013 924 | 2018-2019 |
| 2020 | 2 369 875 | 177 416 | 2 094 310 | 2020-2021 |
| 2021 | 2 452 805 | 193 518 | 1 906 781 | 2020-2021 |

Les rapports annexés aux PLF 2020 et 2021 arrondissaient les trois premières
charges techniques à 2 074, 2 191 et 2 236 MD ; les états financiers sont
la source primaire plus précise. Les tableaux synthétiques des comptes ne
ventilent pas leurs charges techniques par maladie, espèces et AT/MP ; les
figures de la brochure d'indicateurs globaux ne livrent pas leurs valeurs
chiffrées dans la couche texte et n'ont pas été reprises sans image.

## Ventilation des régimes rapportée par le CRES, 2009-2019

Abir Belloussaief, *La Lettre du CRES* n° 8 (janvier 2023), figure 1 p. 1,
`tunisia-data/data/raw/caisses/cres/cres_lettre_n8_2023_atmp.pdf`, fiche
`sources/cres-lettre-8-atmp-2023.md`. L'auteure attribue la figure à la
**CNAM, avec son propre calcul**, sans autre détail de méthode ; sa note porte
sur le régime AT/MP du secteur privé. La figure imprime trois **parts de
dépenses de la CNAM**, en %, non des montants comptables par poste. Couche texte
des étiquettes lue sans ouverture d'image lors de cette passe, puis recoupée
par les totaux arrondis à 100 % ; les cases de 2010 et de 2012 somment à
99,9 % par arrondi des composantes.

| Année | Assurance maladie (%) | Assurances sociales (%) | AT/MP (%) | Somme arrondie (%) |
|---|---:|---:|---:|---:|
| 2009 | 89,2 | 4,1 | 6,7 | 100,0 |
| 2010 | 89,7 | 3,7 | 6,5 | 99,9 |
| 2011 | 90,3 | 3,6 | 6,1 | 100,0 |
| 2012 | 89,0 | 3,6 | 7,3 | 99,9 |
| 2013 | 90,0 | 3,6 | 6,4 | 100,0 |
| 2014 | 91,3 | 3,2 | 5,5 | 100,0 |
| 2015 | 91,4 | 3,0 | 5,6 | 100,0 |
| 2016 | 90,9 | 2,6 | 6,5 | 100,0 |
| 2017 | 90,8 | 2,6 | 6,6 | 100,0 |
| 2018 | 90,1 | 2,7 | 7,2 | 100,0 |
| 2019 | 88,0 | 2,8 | 9,2 | 100,0 |

**Contrôle indépendant limité à 2019** : l'étude chiffre la dépense AT/MP
2019 à **218,965 MD** (p. 1) ; divisée par les **2 367,411 MD** de charges
techniques des états financiers CNAM de 2019 (p. 3), elle vaut **9,25 %**, soit
**9,2 %** au dixième, comme la figure. Le résultat rend son dénominateur
plausible pour cette année, mais ne reconstruit pas les montants exacts des
deux autres branches, ni la ventilation par soin, ni la méthode des années
précédentes. Les assurances sociales comprennent des prestations en espèces :
leurs parts ne représentent pas des soins ambulatoires ou hospitaliers. Les
charges administratives ne sont pas une quatrième branche de la figure.

Cette série est une **étude du CRES**, distincte des états financiers primaires
et des tableaux budgétaires ; elle ne doit pas figurer dans le même tableau que
les montants des comptes ou ceux du ministère. L'annexe 4 du rapport de
diagnostic du ministère des Affaires sociales de 2023 la reproduit d'après le
CRES : l'original est la source retenue.

## Prestations sanitaires identifiées par la CNAM, 2007-2021

`assurance_maladie_fr_2021.pdf`, **page 2** : hospitalisation dans les cliniques
privées, opérations chirurgicales et accouchements (dépenses, millions de
dinars) ; **page 3** : facturation des hospitalisations et consultations
externes dans les établissements publics de santé et hôpitaux régionaux,
montants intitulés « Dépenses » (millions de dinars). La CNAM précise que la
facturation suit son **protocole d'accord de facturation hospitalière** : ne
pas la prendre pour l'ensemble des ressources des hôpitaux ni pour le total
des charges techniques de la caisse. L'indicateur de **nombre de factures**
change de définition en 2017 (payées → reçues), sans clause équivalente sous
la ligne des montants ; seul le nombre de factures a cette rupture attestée.

| Année | Facturation des soins publics (MD) | Clinique privée, chirurgie (MD) | Clinique privée, accouchements (MD) |
|---|---:|---:|---:|
| 2007 | 227,4 | 3,2 | 2,225 |
| 2008 | 246,0 | 6,1 | 8,317 |
| 2009 | 273,4 | 13,8 | 12,862 |
| 2010 | 304,6 | 17,307 | 16,107 |
| 2011 | 347,2 | 19,921 | 19,964 |
| 2012 | 399,5 | 23,718 | 24,441 |
| 2013 | 410,5 | 24,582 | 23,947 |
| 2014 | 444,0 | 27,061 | 28,765 |
| 2015 | 470,5 | 27,404 | 29,103 |
| 2016 | 502,0 | 29,805 | 29,675 |
| 2017 | 538,5 | 28,400 | 29,291 |
| 2018 | 566,4 | 30,807 | 29,677 |
| 2019 | 591,4 | 29,748 | 27,106 |
| 2020 | 620,4 | 25,860 | 24,100 |
| 2021 | 640,6 | 28,721 | 22,091 |

La brochure 2018 `AssuranceMaladie2018.pdf` donne pour l'année 2018 30,499
au lieu de 30,807 MD (chirurgie) et 29,435 au lieu de 29,677 MD
(accouchements) ; la série ci-dessus retient l'édition 2021. En revanche, le
montant de la facturation publique de 2018 (566,4 MD) concorde. Les nombres
de bénéficiaires et de factures sont dans la source mais ne constituent pas
un dénominateur homogène des montants : un même bénéficiaire peut avoir
plusieurs actes ; le nombre de factures change de définition en 2017.

**Éléments encore requis pour une décomposition exhaustive** : montants des
soins ambulatoires par filière et nature de soin, médicaments, soins dentaires,
optique, AT/MP et assurances sociales dans les mêmes comptes ; paiements aux
prestataires et aux assurés, provisions et dettes ; comparabilité des postes
avec les charges techniques totales. La série `assurance_sociale_fr_2021.pdf`
donne séparément les indemnités de maladie et de couches 2008-2021, en espèces
(43,544 MD ensemble en 2008 ; 66,718 MD en 2021), déjà décrites dans le
volume Prestations sociales : ne pas les présenter comme des soins en nature.

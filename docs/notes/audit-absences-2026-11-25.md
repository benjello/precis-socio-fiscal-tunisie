# Audit des affirmations d'absence sur les comptes nationaux (25/11/2026)

Cet audit fait suite à l'affirmation erronée sur D.63. Toutes les éditions ont désormais un inventaire de leurs tableaux : `sources/ins-comptes-nationaux/inventaire-tableaux.csv` dans le dépôt de données. Il recense 2 473 pages, dont 740 extraites, 1 167 non extraites et 566 de texte. Les affirmations d'absence de l'ouvrage et des notes portant sur les comptes nationaux y ont été cherchées par script (motifs « ne publie pas », « n'imprime pas », « ne ventile pas », « aucune ligne », « ne figure pas », « n'apparaît pas », « pas de compte »), puis relues une à une, dans les pages rendues et dans les cahiers.

| Affirmation | Où | Verdict | Ce qui a été fait |
|---|---|---|---|
| Les comptes publiés n'impriment pas de compte de redistribution en nature (D.63) | prestations_sociales/_soins, cahier de l'expert D6 | **infirmée** : tableau « Transferts sociaux en nature », 15 éditions (éd. 2021-2025, p. 114), et tableau économique d'ensemble, compte II.3 | texte corrigé avec les valeurs de 2023 ; D6 retirée et reformulée ; série `cnat-d63` extraite |
| La base 2015 n'est pas publiée par branche avant 2020 | energie/index, industrie/index | **infirmée pour les comptes de la nation** : « Répartition sectorielle de la valeur ajoutée nominale », éd. 2015-2020, p. 50-51, de 2015 à 2020 (non extrait). L'affirmation reste vraie pour la banque de données de l'INS | phrase corrigée ; extraction proposée au backlog |
| Le recalcul de la base 2015 jusqu'en 2010 ne figure dans aucune édition | annexe-pib | **confirmée** : aucune édition en base 2015 ne commence avant 2015 (inventaire) ; le recalcul vient du fichier de l'INS du 15/08/2021 | aucune modification |
| Le reste du monde ne ventile pas sa rémunération des salariés en salaires et cotisations | annexe-comptes-nation | **confirmée** : les pages « Opérations avec l'extérieur » (extraites) n'ont que D.1 | aucune modification |
| Pas de comptes de patrimoine | annexe-comptes-nation | **confirmée** : citation de l'INS, et aucun tableau d'encours non financiers dans l'inventaire | aucune modification |

**Bilan** : 5 affirmations relues ; 2 infirmées et corrigées ; 3 confirmées.

Les autres occurrences des motifs (73 en tout) ne portent pas sur les comptes nationaux. Ce sont des rapports d'entreprises publiques, des textes juridiques, des classeurs du ministère des Finances, ILOSTAT : elles sont hors du champ de cet audit et restent à relire avec leur propre inventaire de sources.

Tableaux non extraits qui lèveraient le plus de manques, par ordre de priorité :
- le tableau économique d'ensemble, 47 pages ;
- les opérations agrégées, 30 pages ;
- le revenu disponible brut des secteurs, 18 pages ;
- les revenus primaires, 15 pages ;
- la valeur ajoutée et la production par branche ;
- le tableau des entrées-sorties (TES) en base 1997, 30 pages.

## Audit élargi, par script (25/11/2026)

Un index des libellés de lignes de toutes les pages (79 455 libellés) a été dressé dans le dépôt de données (`scripts/indexer_libelles_cnat.py`). Chaque élément ci-dessous y a été cherché, dans les titres et les libellés, par `scripts/auditer_absences_cnat.py`. Le décompte des pages porte sur toutes les éditions.

## Les 1 167 pages non extraites, par famille de tableau

| Famille | Pages |
|---|--:|
| par produit | 182 |
| par branche d'activité | 179 |
| autres | 169 |
| pages de suite (ressources, emplois) | 141 |
| prix, volumes, indices | 108 |
| opérations financières | 95 |
| entrées-sorties et ressources-emplois | 86 |
| revenus (primaires, disponibles, national) | 78 |
| FBCF et investissement | 69 |
| opérations agrégées | 33 |
| ratios et structures | 15 |
| tableau économique d'ensemble | 10 |
| comptes de secteur | 2 |

## Recherche par élément (titres et libellés de toutes les pages)

| Groupe | Élément | Pages trouvées (extraites / non extraites / texte) | Exemples (édition, page, titre ou libellé) |
|---|---|---|---|
| b | D.75 transferts courants divers | 272 / 18 / 9 | 2001-2005 p. 35 (non extrait) « Transferts courants divers » ; 2002-2006 p. 35 (non extrait) « Transferts courants divers » ; 2004-2008 p. 35 (non extrait) « Transferts courants divers » |
| b | NP actifs non produits | 91 / 152 / 0 | 2005-2009 p. 130 (non extrait) « Compte : III.1 Actifs non produits » ; 2005-2009 p. 131 (non extrait) « Actifs non produits » ; 2005-2009 p. 132 (non extrait) « Compte : III.1 Actifs non produits » |
| b | D.39 autres subventions sur la production | 87 / 106 / 24 | 2005-2009 p. 125 (non extrait) « IMPOTS INDIRECTS NETS DE SUBVENTIONS SUR LA PRODUCTION PAR S » ; 2005-2009 p. 126 (non extrait) « AUTRES IMPOTS NETS DE SUBVENTIONS SUR LA PRODUCTION » ; 2005-2009 p. 130 (non extrait) « Autres impôts - subventions sur la production » |
| b | SIFIM | 48 / 15 / 22 | 2005-2009 p. 44 (non extrait) « Production SIFIM » ; 2006-2010 p. 41 (non extrait) « Production SIFIM » ; 2007-2011 p. 41 (non extrait) « Production SIFIM » |
| b | P.13 production non marchande | 177 / 299 / 64 | 2001-2005 p. 25 (non extrait) « P.I.B non marchand » ; 2001-2005 p. 26 (non extrait) « P.I.B non marchand » ; 2001-2005 p. 30 (non extrait) « EQUILIBRE RESSOURCES EMPLOIS DE BIENS ET SERVICES NON MARCHA » |
| b | P.31 / P.32 consommation individuelle ou collective | 0 / 0 / 18 | 2005-2009 p. 18 (texte) « P4 Consommation finale effective » ; 2005-2009 p. 23 (texte) « revenu disponible ajusté est la consommation finale effectiv » ; 2006-2010 p. 18 (texte) « P4 Consommation finale effective » |
| b | D.71 / D.72 assurance dommages | 353 / 15 / 6 | 2001-2005 p. 78 (non extrait) « 241.Primes nettes d’assurance dommages » ; 2001-2005 p. 80 (non extrait) « 241.Primes nettes d‘assurance dommages » ; 2001-2005 p. 82 (non extrait) « 241.Primes nettes d’assurance dommages » |
| b | D.74 coopération internationale | 120 / 15 / 9 | 2005-2009 p. 45 (non extrait) « Coopération internationale courante » ; 2006-2010 p. 42 (non extrait) « Coopération internationale courante » ; 2007-2011 p. 42 (non extrait) « Coopération internationale courante » |
| b | S2 et balance des paiements | 0 / 0 / 30 | 2001-2005 p. 9 (texte) « et les données de la balance des paiements niveau et en conf » ; 2002-2006 p. 9 (texte) « et les données de la balance des paiements niveau et en conf » ; 2004-2008 p. 9 (texte) « et les données de la balance des paiements niveau et en conf » |
| c | D.61 cotisations sociales par secteur | 223 / 54 / 48 | 2001-2005 p. 33 (non extrait) « Cotisations sociales recues (+) » ; 2001-2005 p. 35 (non extrait) « Cotisations sociales » ; 2001-2005 p. 65 (non extrait) « Cotisations sociales » |
| c | D.62 prestations sociales par secteur | 253 / 130 / 42 | 2001-2005 p. 33 (non extrait) « Prestations sociales versées (-) » ; 2001-2005 p. 35 (non extrait) « Prestations sociales » ; 2001-2005 p. 64 (non extrait) « Prestations sociales » |
| c | P.3 santé (produit ou fonction) | 82 / 213 / 18 | 2001-2005 p. 50 (non extrait) « Santé » ; 2001-2005 p. 52 (non extrait) « Santé » ; 2002-2006 p. 50 (non extrait) « Santé » |
| c | P.3 éducation (produit ou fonction) | 42 / 132 / 21 | 2015-2020 p. 40 (non extrait) « Enseignement » ; 2015-2020 p. 41 (non extrait) « Enseignement » ; 2015-2020 p. 42 (non extrait) « Enseignement » |
| c | D.29 taxe de formation professionnelle, FOPROLOS | 0 / 0 / 0 | — |
| c | D.9 transferts en capital par secteur | 276 / 133 / 27 | 2001-2005 p. 23 (non extrait) « Transferts en capital extérieur nets » ; 2001-2005 p. 35 (non extrait) « Transferts en capital » ; 2001-2005 p. 64 (non extrait) « Transferts en capital » |
| d | D1 statut des années (définitions) | 453 / 714 / 39 | 2001-2005 p. 19 (non extrait) « *Compte semi-définitif » ; 2001-2005 p. 20 (non extrait) « *Compte semi-définitif » ; 2001-2005 p. 21 (non extrait) « *Compte semi-définitif » |
| d | D2 consolidation des administrations | 0 / 0 / 6 | 2015-2020 p. 10 (texte) « ambitieux de consolidation du Système des Comptes Nationaux  » ; 2017-2021 p. 8 (texte) « ambitieux de consolidation du Système des Comptes Nationaux  » ; 2018-2022 p. 8 (texte) « ambitieux de consolidation du Système des Comptes Nationaux  » |
| d | D3 méthode de l'INS (non marchand) | 49 / 117 / 33 | 2001-2005 p. 38 (non extrait) « ACTIVITES NON MARCHANDES » ; 2001-2005 p. 39 (non extrait) « ACTIVITES NON MARCHANDES » ; 2001-2005 p. 40 (non extrait) « ACTIVITES NON MARCHANDES » |
| d | E1 droits de douane par produit | 0 / 0 / 18 | 2005-2009 p. 16 (texte) « qui sont les droits de douane » ; 2005-2009 p. 17 (texte) « (Droits de douane) sur les produits nets de subventions) » ; 2006-2010 p. 16 (texte) « qui sont les droits de douane » |
| d | E3 passage du budget aux comptes | 0 / 0 / 0 | — |
| d | E4 date de publication des éditions | 0 / 0 / 12 | 2008-2012 p. 1 (texte) « Edition 2014 » ; 2009-2013 p. 1 (texte) « Edition 2015 » ; 2010-2014 p. 1 (texte) « Edition 2016 » |

### Verdicts

| Groupe | Élément | Verdict | Où, et ce qui change |
|---|---|---|---|
| (a) | Les 99 cases vides de la matrice des comptes et des volumes | **confirmées, comme vides de l'ouvrage, pas des comptes** | Les 99 cases ont toutes une valeur publiée (comptes des secteurs, extraits). Le vide est l'absence de domicile dans l'ouvrage. |
| (b) | P.31 / P.32, consommation individuelle ou collective | **confirmée** : aucun tableau ne les publie | La consommation finale effective (P.4) n'apparaît que dans le texte de méthode (base 1997, éd. 2005-2009 p. 18). La consommation individuelle des administrations se déduit de D.63 versé par elles (14 604,2 MD en 2023) : c'est un calcul, à marquer comme tel. |
| (b) | Ventilation de P.3 des administrations | **infirmée** | Le TRE, déjà extrait, ventile la consommation finale des administrations par produit. En 2023 (éd. 2021-2025) : administration publique et défense 16 652,7 MD, enseignement 7 886,3, santé humaine et action sociale 3 624,7. Les postes « santé » et « éducation » ont ainsi une cible INS par fonction. |
| (b) | D.29 / D.39 par branche | **infirmée** | Tableau « Autres impôts nets de subventions sur la production » (éd. 2021-2025 p. 112) et tableau par secteur d'activité (p. 111), non extraits. |
| (b) | D.4 versés et reçus par secteur | **infirmée** (le détail existait, mais n'était pas lu) | « Revenus de la propriété versés / reçus par les secteurs institutionnels », éd. 2021-2025 p. 113, non extrait. |
| (b) | Activités non marchandes | **infirmée pour la base 1983** | « Activités non marchandes » et « Équilibre ressources-emplois de biens et services non marchands » figurent dans les éditions 2001-2005 à 2004-2008 (19 pages par édition, non extraites) ; aucun tableau équivalent en base 2015. |
| (b) | SIFIM | **infirmée** | « Production SIFIM » dans les opérations agrégées (base 1997, 15 pages non extraites). |
| (b), (e) | S2 et balance des paiements | **confirmée pour les comptes de la nation** | La balance des paiements n'est citée que comme source, dans le texte de méthode (30 pages). Le dépôt de données n'a aucune série de balance des paiements extraite : le catalogue des publications de la BCT la mentionne sans fichier inventorié. Lot B : à télécharger (voir questions-mahdi.md). |
| (c) | D.29 taxe de formation professionnelle, FOPROLOS | **confirmée** | Aucun libellé dans aucune édition. |
| (c) | D.61, D.62 par secteur | **déjà extraites** (comptes des secteurs) | En plus, les tableaux « Cotisations sociales reçues par les secteurs institutionnels » (éd. 2021-2025 p. 114, même page que D.63) et des pages de base 1983 sont non extraits. |
| (d) | D1 définition des statuts d'année | **confirmée** : seule la note « *Compte semi-définitif / **provisoire » figure sous les tableaux | Pas de définition dans les éditions. |
| (d) | D2 consolidation des administrations | **confirmée** | Aucune page n'en traite (le mot n'apparaît que pour la « consolidation du système des comptes »). |
| (d) | E1 recettes douanières par nature | **infirmée en partie** | Le TRE, extrait, donne les droits de douane (D.212) par produit. Les recettes douanières par nature du budget restent à chercher hors de l'INS. |
| (d) | E3 note de passage du budget aux comptes | **confirmée** | Aucune page. |
| (d) | E4 date de publication des éditions | **infirmée** | L'année d'édition est imprimée en couverture (« Edition 2014 » pour 2008-2012… « Edition 2026 » pour 2021-2025, 12 éditions). La date de consultation (M6) reste inconnue. |

**Bilan** : 20 éléments examinés.
- 8 infirmés : P.3 par produit, D.29/D.39 par branche, D.4 par secteur, activités non marchandes de la base 1983, SIFIM, droits de douane par produit, date d'édition, et D.63 dans l'audit initial.
- 9 confirmés.
- 3 déjà extraits.
- S'y ajoute l'audit initial : 2 phrases infirmées et corrigées.

### Ordre d'extraction proposé (manques levés)
1. Le tableau économique d'ensemble (10 pages par édition en base 2015) : il donne en une page par année toutes les opérations par secteur, D.63 et le revenu disponible ajusté compris. Il double les comptes des secteurs, ce qui en fait aussi un contrôle.
2. Les revenus de la propriété versés et reçus, et les cotisations reçues par secteur : 3 pages par édition, des ventilations utiles au lot A (contreparties).
3. Par branche d'activité (179 pages) : valeur ajoutée, production, rémunérations, impôts nets par branche. C'est la base des volumes de production.
4. Par produit (182 pages), puis prix et volumes (108).

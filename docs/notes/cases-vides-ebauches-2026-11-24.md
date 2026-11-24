# Cases vides les plus lourdes de la matrice : ébauches (24/11/2026)

**Ébauche.** Cette note prépare l'étape d du plan de restructuration : pour les opérations les
plus lourdes qu'aucun volume ne couvre encore, elle dit où elles iront, ce que l'entrepôt de données
en contient déjà et ce qu'il faut en extraire avant d'écrire.

La matrice est `precis/fr/correspondance-comptes.csv`, ajoutée par la PR « Comptes par secteur
reconstitués » (#843, non fusionnée) : 232 lignes, dont 126 vides. Les niveaux qui suivent sont
ceux de 2024, base 2015, édition 2021-2025 des comptes de la nation de l'INS, en millions de
dinars. Ils servent à classer les cases, pas à être cités.

## Les cases, de la plus lourde à la plus légère

| Opération (SCN 2008) | Secteur, côté | Niveau 2024 | Partie et volume d'accueil |
|---|---|---|---|
| P.3 Dépense de consommation finale | ménages, emplois | 125 362,2 | V, « La consommation et les niveaux de vie » (à créer) |
| P.2 Consommation intermédiaire | sociétés non financières, emplois | 95 078,8 | I, volumes de branche (couverture progressive) |
| P.7 Importations de biens et services | reste du monde, ressources | 90 060,5 | VII, « Les échanges extérieurs » (à créer) |
| P.6 Exportations de biens et services | reste du monde, emplois | 79 874,4 | VII, idem |
| P.51 FBCF | ménages, emplois | 7 714,9 | VI, « L'investissement » (à créer) |
| P.52 Variation de stocks | sociétés non financières, emplois | −7 613,2 | VI, idem |

Les revenus de la propriété des sociétés financières (D.4, environ 16 400 en ressources) et les
instruments financiers (F.2, F.4) relèvent du chapitre « La monnaie et le crédit » du volume
« Le cadre » (#847).

## 1. La consommation des ménages (partie V)

Plan d'ébauche : la dépense de consommation par produit, en valeur et en volume ; sa structure
et son évolution ; la consommation par décile, d'après l'enquête sur le budget, la consommation
et le niveau de vie des ménages de 2021 ; les prix administrés, par renvoi à « La compensation ».

Ce que l'entrepôt contient :

- `ins-comptes-nationaux/cnat-consolide/depense-de-consommation-finale-des-menages-par-produit*.csv` :
  deux relevés, 2012-2024, éditions 2012-2016 à 2020-2024. Ils ne sont pas au catalogue : les
  éditions de base 1997 et de base 2015 y sont mêlées, et les nombres gardent la virgule décimale.
- `ins-enquete-menages/enbcnv2021_structure_logement.csv` : seul tableau de l'enquête de 2021
  déjà extrait.

À faire dans tunisia-data, avec l'agent extracteur de tableaux :

- une extraction par édition, la base déclarée sur chaque ligne ;
- contrôle : la somme des produits doit être égale à la P.3 des ménages dans les comptes de
  secteur (`cnat-secteurs`), à l'arrondi près ;
- les tableaux de dépense par décile de l'enquête de 2021.

## 2. Les échanges extérieurs (partie VII)

Plan d'ébauche : exportations et importations par produit, en valeur et en volume ; le solde et
le taux de couverture ; la balance des paiements ; les régimes (offshore et onshore), par renvoi
à « La fiscalité » pour les avantages.

Ce que l'entrepôt contient :

- `cnat-consolide/e-x-p-o-r-tat-i-o-n-*.csv` et `i-m-p-o-r-tat-i-o-n-*.csv` : par produit, en
  valeur et en volume, éditions 2012-2016 à 2018-2022, hors catalogue. Mêmes défauts que plus
  haut.
- `bct/balance_commerciale.csv`, `bct/exportations_par_groupement.csv`,
  `bct/importations_par_groupement.csv` : la BCT, annuel depuis 2003, plus des lignes
  mensuelles. C'est un relais de l'INS.
- `ins-publications/commerce_exterieur_par_regime_1998_2023.csv` : régimes, 1998-2023.

À faire :

- extraire les tableaux par produit des comptes de la nation par édition ;
- contrôle : la somme des produits doit être égale à la P.6 et à la P.7 du compte du reste du
  monde, à l'arrondi près ;
- comparer avec la balance commerciale de la BCT, qui suit une autre définition (douane et non
  comptes nationaux) : l'écart doit être documenté, pas corrigé.

## 3. L'investissement (partie VI)

Plan d'ébauche : la FBCF par secteur institutionnel, par branche, par produit ; la part
publique ; les régimes d'incitation, par renvoi à « La fiscalité » ; les entreprises publiques,
par renvoi.

Ce que l'entrepôt contient :

- `cnat-consolide/formation-brute-de-capital-fixe-*.csv` : par secteur institutionnel, par
  secteur d'activité, par domaine, par produit, 2012-2024, hors catalogue. Les codes de la
  nomenclature de base 1997 (`b11`, `g40`, `e23`…) et les libellés de base 2015 y sont dans une
  même colonne.

À faire :

- séparer par base ;
- contrôle : la FBCF par secteur institutionnel doit être égale à la P.51 des comptes de secteur ;
  la somme par branche doit être égale au total ;
- verser au catalogue ;
- la FBCF par branche alimente aussi « La branche en chiffres » des volumes de branche
  (« L'énergie », #846).

## État des extractions (24/11/2026, soir)

- FBCF : faite, tunisia-data #147 (quatre tableaux, quinze éditions 2005-2009 à 2021-2025,
  1 491 contrôles sur 1 500).
- Consommation et échanges par produit : faits, tunisia-data #148 (aux prix courants, quinze
  éditions, 258 contrôles sur 258). **Le tableau « dépense de consommation finale des ménages par
  produit » totalise la consommation finale globale (ménages et administrations)** : son total
  est égal à la « consommation finale globale » des emplois du PIB. Pour la case P.3 des
  ménages, la source reste la P.3 des comptes de secteur ; le tableau par produit sert à la
  structure, en retirant les lignes des services d'administration, d'enseignement et de santé
  avec prudence (elles mêlent dépense des ménages et consommation publique).
- Restent les tableaux en volume (prix de l'année précédente) et le rapprochement avec la
  balance commerciale de la BCT.

## Ordre proposé

1. Extraire les FBCF : elles servent trois fois (investissement, volumes de branche, recoupement
   avec les comptes de secteur).
2. Extraire la consommation par produit : c'est la case la plus lourde.
3. Extraire les échanges par produit, puis les rapprocher de la BCT.

Chaque volume n'est ouvert qu'une fois ses séries contrôlées, selon le gabarit de
`docs/procedures/gabarit-volume-branche.md` (#846), adapté aux volumes qui ne sont pas de branche.

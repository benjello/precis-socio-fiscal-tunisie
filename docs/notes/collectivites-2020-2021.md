# Comptes des communes 2020-2021 : ce qui manque pour les postes des collectivités locales

Recherche du 25/11/2026, faite après la PR #895 (trois postes des collectivités locales dans
`precis/fr/postes-comptables.csv`). Elle ne change ni le registre ni les tableaux engendrés.

## Ce qui manque

| Variable de `finances-locales-communes-agregats` | Poste | 2020 | 2021 |
|---|---|---|---|
| `remunerations` | `remunerations-collectivites` (D.1) | manque | manque |
| `moyens_des_services` | `moyens-services-collectivites` (P.2) | manque | manque |

La couverture de S1313 (`part_montant_couverte_pct`, `precis/fr/compte-couverture-annees.csv`)
reste donc de 9,3 % en 2020 et de 8,4 % en 2021, contre 22,2 % à 25,7 % les années où les deux
postes sont chiffrés (2018, 2019, 2022, 2023). En 2020-2021, seuls les intérêts (D.41) et les transferts courants de l'État (D.73) sont
chiffrés.

## Comment la série est construite

Adaptateur : `scripts/build_finances_locales_communes.py` de l'entrepôt de données (copie
`tunisia-data-wt-merge`, `origin/main` au commit 55bbb3d) ; fiche `sources/finances-locales-communes.md`.

- `source = dgct_agregats`, `niveau = agregat_dgct` : classeur `Les-dépenses-ordinaires.xls`
  (feuille `dep`), 2008-2019.
- `source = somme_communes` : somme des réalisations des 350 communes, 2018-2023. Le niveau
  `partie` (parties 1 à 4 du titre 1, dont rémunérations et moyens des services) n'existe que
  pour 2022 et 2023 : seuls ces fichiers portent `idpartiedep` et `lib_partie_dep_ar`.
- `retenu` : agrégats DGCT jusqu'en 2019, somme des communes à partir de 2020.

Pour 2020 (`Municipalites_depenses2020.xlsx`) et 2021 (`Depenses_Decembre2021.xlsx`, situation au
25/12/2021), l'adaptateur ne lit que la section (`lib_section_dep_ar`, `Section_Depense`) : le
niveau le plus fin publié est la section « dépenses de gestion » (954,7 MD en 2020, 965,6 MD en
2021), qui confond rémunérations, moyens des services, interventions et imprévus. La fiche le dit
(« Elles manquent en 2020-2021 (fichiers à la section) »). Le fichier 2020 porte une ligne par
article, sans numéro ni libellé d'article selon la fiche ; il n'a pas été réexaminé : les fichiers
bruts ne sont pas versionnés et sont absents de la copie en lecture seule.

## Où l'on a cherché

1. **Entrepôt de données** (`~/projets/tunisia-data-wt-merge`) :
   - `data/processed/finances_locales/` : `communes_agregats_2008_2023.csv` (aucune ligne
     `remunerations` ni `moyens_des_services` en 2020-2021) ; `communes_budgets_par_commune_2018_2023.csv`
     (2020 et 2021 : `niveau = section` seulement, rubriques `depenses_gestion`, `interets_dette`,
     `depenses_developpement`, `remboursement_principal`, `depenses_credits_transferes`) ;
     `cpscl_*`, `ins_cl_*`, `bm*`, `fccl_*`, `interieur_article_interventions.csv`.
   - `grep -ril -E "remuner|rémunér|التأجير"` sur `data/processed/**/*.csv` : aucun fichier
     de comptes communaux hors `finances_locales/` ; les fichiers trouvés portent sur l'État,
     les caisses, l'éducation, la BCT et l'INS.
   - `grep -ril -E "communes|collectivit|baladi|بلدي"` sur `data/processed/**/*.csv` hors
     `finances_locales/` : effectifs de la fonction publique (`ins-fonction-publique-*`), qui
     donnent le nombre d'agents des collectivités locales mais pas leur masse salariale (un
     produit effectifs × salaire moyen serait une dérivation, non retenue).
   - `catalog.yml` (entrées `finances-locales-*`), `sources/finances-locales*.md`,
     `sources/finances-locales-urls.csv`, `data/manifeste/finances_locales.csv`.
2. **Cache du livre** (`precis/_seriescache/`) : `grep -il remuner *.csv` ; les fichiers trouvés
   ne portent pas de rémunérations des communes pour 2020-2021. `finances-locales-ins-comptes.csv`
   et `cnat-secteurs.csv` donnent le compte INS de S1313 lui-même : on ne peut pas s'en servir
   pour couvrir S1313. `budget-desagregation-nature.csv`, `budget-vote-realise.csv` et
   `budget-comptanat-apu.csv` ne portent que l'État et les APU (périmètres `apu`, `central`).
3. **Lois de règlement et rapport sur les fonds spéciaux du Trésor (PLF 2022)** : ils portent sur
   le budget de l'État, non sur l'exécution des budgets communaux.

## Publications qui pourraient contenir les montants

Le titre de ces publications laisse penser qu'elles donnent les dépenses des communes par
partie ; leur contenu n'a pas été vérifié (fichiers bruts hors de la copie lue).

Pour 2020, adresses tirées de `sources/finances-locales-urls.csv` :

- Cour des comptes, analyses financières des communes, exercice 2020 :
  `http://www.collectiviteslocales.gov.tn/wp-content/uploads/2023/03/analfinancom2020.pdf`
- Cour des comptes, note de synthèse du contrôle financier des communes, gestion 2020 (arabe) :
  `http://www.collectiviteslocales.gov.tn/wp-content/uploads/2023/04/مذكرة-تأليفية-نهائية-الرقابة-المالية-على-البلديات-بعنوان-تصرّف-2020-1.pdf`
- Haute instance des finances locales, rapport annuel 2020 (arabe) :
  `http://www.collectiviteslocales.gov.tn/wp-content/uploads/2022/04/HIFL_Rapportannuel_2020.pdf` ;
  résumé : `http://www.collectiviteslocales.gov.tn/wp-content/uploads/2022/04/HIFL_Rapportannuel_2020_Resume.pdf` ;
  première partie en français : `https://www.hifl.tn/wp-content/uploads/2022/09/Deuxieme-rapport-annuel-_Pr_partie_fr.pdf`
- DGCT, *L'impact du COVID-19 sur les finances locales en Tunisie* (période 2019-2020) :
  `https://drive.google.com/file/d/1fNVHlF4GRd_h5F181MWfYsOaBhlgWwVa/view`

Pour 2021, rien dans le manifeste :

- Cour des comptes, analyses financières des communes, exercice 2021 (adresse à vérifier) ;
- Haute instance des finances locales, rapport annuel 2021 (adresse à vérifier) ;
- DGCT, fichier des dépenses par commune de l'exercice 2021 clos, à la partie, qui
  remplacerait la situation au 25/12/2021 (adresse à vérifier).

Travail à faire dans l'entrepôt : lire ces documents, en extraire rémunérations et moyens des
services des communes 2020 (et 2021), avec une ligne `source` distincte de `somme_communes`, puis
contrôler le rapport à l'INS (D.1 et P.2 de S1313) comme #895 (92 % à 96 % les autres années).

## Subventions d'équipement : présentes, non retenues comme poste

`subventions_equipement` (catégorie 7, « منح التجهيز ») figure dans le cache pour 2018-2023,
2020 et 2021 compris. Rapport à l'INS, S1313, ressources D.99 (`cnat-secteurs.csv` ne porte pour ce
secteur que D.9 et D.99 ; dernière édition de chaque année) :

| Année | Subventions d'équipement (MD) | INS D.99 reçus (MD) | Rapport | Avec crédits transférés |
|---|---|---|---|---|
| 2018 | 173,7 | 426,4 | 0,41 | 0,53 |
| 2019 | 243,5 | 491,7 | 0,50 | 0,58 |
| 2020 | 298,2 | 445,4 | 0,67 | 0,77 |
| 2021 | 474,9 | 642,6 | 0,74 | 0,83 |
| 2022 | 447,9 | 482,3 | 0,93 | 1,05 |
| 2023 | 436,7 | 477,2 | 0,92 | 1,02 |

Le rapport passe de 0,41 à 0,93 : il n'est pas stable, à la différence de D.1 et P.2 dans #895.
Raisons possibles, non vérifiées : S1313 comprend les conseils régionaux, la série DGCT non ; la
catégorie D.99 de l'INS mêle des transferts que la catégorie 7 ne contient pas ; 2021 est une
situation au 25/12. Aucun poste n'est ajouté tant que l'écart n'est pas expliqué. Un poste
ajouté changerait aussi la couverture et la justesse de 2018-2023.

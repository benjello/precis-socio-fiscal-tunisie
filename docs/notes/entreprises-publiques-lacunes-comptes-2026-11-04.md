# Entreprises publiques : où l'on n'a rien sur les comptes (4 novembre 2026)

Source : `precis/fr/entreprises_publiques/listes/inventaire-rapports-*.csv` et `opinions-cac.csv`, sur `master`. Le détail des adresses essayées est dans la colonne `url_origine` des lignes `aucun` de l'inventaire ; il n'est pas recopié ici. Le Registre national des entreprises (payant) n'a pas été consulté : voir `_annexe_registre.qmd` et `rne-voies-gratuites-2026-11-04.md`.

Classement par sigle de l'inventaire : A = toutes les lignes sont `aucun` ; C = le sigle figure dans `opinions-cac.csv` ; B = le reste. TTN a une ligne `aucun` (exercices 2019-2022) mais des comptes pour d'autres exercices : classée en C.

## A. Rien du tout (25)

AFI, ARRU, attt, CIOK, CTF, ctn, MTK, oaca, OC, OCT, OTD, PCT, RA, rfr, smls, SNCPA, SNDP, SNIT, sntri, SOGEMT, soretras, SPROLS, srt-autres, srt-bizerte, STIR

## B. Des documents, mais sans opinion des commissaires aux comptes dans le relevé (12)

Une ligne de l'inventaire peut couvrir plusieurs exercices ; « lignes » compte les lignes, pas les documents.

| Sigle | Lignes | Exercices (étendue) |
|---|---:|---|
| AFH | 16 | 2016–2025 |
| CPG | 10 | 2008–2015 |
| GCT | 7 | 2012–2014 |
| La Poste | 1 | 2010–2023 |
| ommp | 9 | 2011–2025 |
| ONAS | 1 | 2004–2024 |
| ONH | 5 | 2017–2022 |
| RNTA | 5 | 2019–2020 |
| sncft | 14 | 2010–2023 |
| SONEDE | 1 | 2011–2016 |
| transtu | 12 | 2010–2021 |
| tunisie-autoroutes | 1 | 2022–2022 |

## C. Avec opinions des commissaires aux comptes (9)

BFPME, BTS, CPSCL, ETAP, FOULADH, SOTRAPIL, STEG, TT, TTN
Les sigles BH, BNA, BTE, CIMBIZ, SOTUMAG, STAR, STB, TUNISAIR et TUNISRE figurent aussi dans `opinions-cac.csv` (sociétés cotées) mais pas dans l'inventaire des entreprises publiques.

## Pistes
- Rapports de la Cour des comptes : index dans `tunisia-data/data/derived/cour-des-comptes/index.sqlite`, pages par entreprise dans `tunisia-data/sources/cour-des-comptes-entreprises-pages.csv`.
- Rapport de la Banque mondiale sur les entreprises publiques : chapitre `_etudes.qmd` du volume ; recherche de compléments en cours.
- Registre national des entreprises : ce qui est gratuit, constats du 4 novembre 2026 (`rne-voies-gratuites-2026-11-04.md`).
- Loi n° 89-9, art. 14 : publication des comptes au JORT avant le 31 août ; effectivité à vérifier.
- Questions possibles à l'équipe de la Banque mondiale, pour les groupes A et B :
  1. Le « Bilan de gouvernance des entreprises et établissements publics au titre de la période 2018-2020 » (direction des entreprises publiques, 2021), cité sans référence complète dans la synthèse « Governance of State-Owned Enterprises in the MENA Region » (avril 2024, note 42).
  2. Le « Rapport sur les entreprises publiques » du ministère des Finances (2023, note 19 de la même synthèse) et son édition 2024, listée sur idaraty.tn sans lien de téléchargement.
  3. Le rapport pays Tunisie annoncé par les études de cas du projet P177105 : introuvable en ligne, probablement non publié.
  4. Les comptes, ou à défaut leurs sources, des entreprises du groupe A.

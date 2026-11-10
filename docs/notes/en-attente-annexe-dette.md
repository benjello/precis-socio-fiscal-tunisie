# En attente — chantier annexe dette publique (relais de session)

Worktree `../precis-wt-dette`, branche `chantier/annexe-dette-publique` (base `origin/master`).
**Rien n'est commité** (ni ici, ni dans `tunisia-data`). L'annexe est un **BROUILLON** à relire.
Aperçu : `file://~/apercus-precis/annexe-dette-publique.html`.

## Où on en est (fait)
Annexe `precis/fr/annexe-dette-publique.qmd` : ~13 sections, **12 figures vivantes**, enregistrée
dans `build.sh`, page-relais arabe. Chaîne **données → `tunisia-data` → cache → figures** en place.
Séries rapatriées (scripts + build + catalogue bilingue + snapshot, bruts ignorés) : IDS
(échéancier, créanciers, conditions), MdF (indicateurs 1986-2025, exécution 2012-2024, charge
d'intérêt longue 1972-2024, GFS), BCT (devises 2003-2024, effet-change 1999-2024, dette publique
intérieur/extérieur 2000-2025, endettement monétaire 2020-2025), WDI (liquidité, change-dinar).
Notes documentaires : cadrage, prêt-par-prêt, registres JORT (881 + 198), dette intérieure,
soutenabilité (sources + fiche économiste), concordance, bulletins d'exécution.

## Fils OUVERTS (todos de session #16-#22)

### Clôture éditoriale (#22)
- **Bibliographe — FAIT** : `minfin-dette-2025` porté au fonds racine FR+AR (l'annexe arabe le résoudra ;
  `entreprises_publiques` est FR-only) ; `loi-67-53-lob`/`loi-org-96-103-lob` à parité AR ; 4 clés de
  données à parité. `check_references_coherentes` ✓, rendu FR 0 `[?]`. **À confirmer (humain)** : titre
  arabe de `minfin-dette-2025` (formé par analogie + nom de fichier gbo.tn). Avert. citeproc
  préexistant hors chantier : `minfin-resultats-provisoires-2017-01` (vit dans `compensation/`).
- **Terminologue — FAIT (contenu)** : 13 entrées bilingues versées dans `precis/glossaire.yml`
  (`dette-publique, dette-etat, dette-interieure, dette-exterieure, encours-dette, service-dette,
  amortissement-dette, cout-apparent-dette, soutenabilite-dette, ecart-taux-croissance, effet-change,
  effet-volume, dette-garantie`), statut `provisoire`, `build_glossary` exit 0. **À confirmer
  (humain)** : termes AR à l'image sur l'édition arabe du Rapport sur la dette publique.
- **BLOQUÉ — câblage des renvois `[terme](#g-id)` + architecture** : une annexe de 1er niveau
  (`precis/fr/annexe-dette-publique.qmd`, hors `precis/fr/<book>/`) ne résout PAS les ancres de
  glossaire — vérifié au rendu de `annexe-comptes-nation` (précédent) : `#g-...` ressort en
  `<a href="#g-...">` sans cible ni infobulle (`_glossaire.infobulles.html` est engendré **par livre**
  et n'est pas inclus dans les annexes racine). De plus `build_glossary.ancres_utilisees` ne scanne que
  `precis/fr/<book>/` : les 13 termes, employés seulement dans l'annexe racine, n'apparaissent dans
  aucune page glossaire rendue. **Renvois NON câblés** (on ne pose pas de liens morts). **Question
  architecte** : soit étendre `build_glossary`/les infobulles aux annexes racine (injecter
  `_glossaire.infobulles.html` + collecter leurs ancres), soit assumer un glossaire en texte seul
  pour les annexes transversales. À trancher par un humain + l'architecte. Les 13 définitions
  restent acquises dans `glossaire.yml` (fonds global + bijection de traduction) en attendant.
- **Sources économiques** (soutenabilité) : FMI Article IV, DSA FMI/BM, littérature r−g (p. ex.
  Blanchard 2019) → documentaliste/`backlog`, à vérifier sur source primaire avant versement.

### Index des sources + comblement partiel des trous (2026-11-10)
- **Index durable des tableaux BCT** écrit dans `tunisia-data/sources/bct-archives.md` (§ « Index des
  tableaux dette… ») : pub 107 (A1–A24), pub 109 (2-15, 2-16, 3-12/3-14…), pub 108 (BSF XI-2), tables
  en ligne, **+ carte de comblement des trous**. Principe : capturer et indexer ce qu'on croise pour
  le retrouver vite, même hors besoin immédiat.
- **Encours MLT 2013-2019 COMBLÉ** (recherche approfondie → trouvé) : série
  `dette-exterieure-encours-mlt-ra` versée depuis le tableau « Principaux paramètres » des RA
  (31 499 → 75 908 MDT). Approximation documentée : périmètre RA (hors intérêts courus) ≈ A10 à **1,4 %**
  (overlap 2019), gardée **distincte** de l'A10 (pas d'épissure) ; garde-fou vérifie l'écart ≤ 3 %.
- **Composition par devise 2013-2018 : APPROXIMATION AFFICHÉE** (décision humaine). Série
  `dette-exterieure-devises-ra` (2015, 2017, 2018 — euro/dollar/yen + reliquat, le KWD fondu),
  extraite du récit des Rapports annuels, portée en **barres hachurées** distinctes dans
  `fig-dette-devises` ; 2013/2014/2016 restent en blanc (non énoncées). Garde-fou : somme = 100
  vérifiée aussi pour cette série.
- **Effet-change 2013-2018** : introuvable hors A15 du pub 107 manquant — non comblable.
- **OBJECTIF OUVERT (maintenu)** : retrouver les **rapports dette BCT (pub 107) 2013-2022** — ils
  lèveraient les deux approximations (encours MLT RA, devises RA) et combleraient l'effet-change.
  Web épuisé (cf. ci-dessus) ; reste **demande directe BCT** / bibliothèques de dépôt. À reprendre
  dès qu'un canal hors web s'ouvre ; alors les séries `-ra` sont remplacées par l'A14/A10/A15.
- **Source-cible épuisée côté web (2026-11-10)** : chasse Wayback + site vivant menée à terme — les
  rapports dette (pub 107) **2013-2022 n'existent nulle part en ligne** (CDX : aucune capture ; les
  3 éditions du `dette.pdf` canonique sont anciennes, 2010/2011-2012). **Ne pas relancer la chasse
  web.** Restent hors web : **demande directe à la BCT**, bibliothèques de dépôt (INS, universités).
  Méthode et cas consignés dans `tunisia-data/sources/chercher-des-donnees-tunisie.md`.

### Robustesse de l'annexe — **FAIT** (A, C, D, E)
- **A** — `docs/notes/dette-concordance.md` : carte des périmètres + invariants + constats repro
  effet-change + séries BCT en ligne. **Écrite et enrichie.**
- **C** — `scripts/check_dette_coherence.py` : garde-fou (identités, total budg ≈ MdF à 3 %,
  effet-change=change+volume, ordre extérieur, parts devises, figures → séries). **Écrit, intégré
  à `verifier.sh`, PASSE.** *Il a déjà attrapé une vraie corruption (total 2016-2018/2021).* 
- **D** — encadré « Quatre « dettes extérieures » à ne pas confondre » dans `#sec-dette-perimetres`. **Fait.**
- **E** — `dette-etat-interieur-exterieur` (monétaire) **documentée « non employée par les figures,
  concept distinct »** (gardée, pas retirée).
- **B** (renommage par famille) : différé, coûteux — A+C+D ont suffi.
- **#21 FAIT (segment récent)** : série `dette-exterieure-encours-mlt-total` versée, **2019-2024**
  (77 001 → 75 966 MDT), extraite du tableau A10 (dette2023 + dette2024). Le garde-fou vérifie
  désormais « État ext. budgétaire ≤ MLT total ». **Reste** : segment 2013-2018 (rapports BCT 107
  absents) — **non comblable proprement** (RA ne donne que la dette budgétaire ~58 000, pas le MLT
  total ; composition devise du trou seulement en récit à 3 devises). Trou laissé honnête.
- **Repro effet-change (#20) tranchée** : on garde le reporté BCT ; méthode validée ; exact-au-dinar
  impossible (cours officiels A23 en PDF récents seulement ; « autres devises » ≈ DTS/FMI + reliquat
  SIADE non public ; les tables BCT en ligne ne couvrent que ~2020-2025).
- Le bug d'extraction `dette-publique-interieur-exterieur` (mauvaise table dans certains RA) a été
  **corrigé** : l'extracteur **valide désormais chaque candidat contre la dette totale MdF**.

### (ancien détail — options)
- B — renommage par famille (`ppg-ext-ids`, `ext-mlt-bct`, …) : différé.

### « Autres devises » (≈ 9 % de la dette extérieure)
Trouvé : ≈ **dette FMI en DTS** (`DT.DOD.DIMF.CD`, publié, ordres de grandeur concordants). Reliquat
(GBP + mineures) **non public** (interne SIADE BCT ; la Banque mondiale ne renseigne pas `DT.CUR.*`
pour la Tunisie). **Décision à prendre** : (a) verser la série FMI + cours DTS/dinar et refaire la
reproduction de l'effet-change avec « autres = DTS » ; ou (b) acter l'explication et garder le
reporté BCT. La reproduction manuelle (parts × encours × variation du cours dinar/devise) est
**validée en méthode** mais reste à ±30 % sur l'effet-change faute du détail « autres ».

### Données manquantes utiles
- **Niveau** de l'encours externe MLT total (~80 000, base de l'effet-change/devises) : pas de série
  de niveau au cache — extraire le Total du tableau **A10** des rapports BCT.
- Trou devise **2013-2018** : irréductible (rapports BCT absents, Wayback négatif) — affiché tel quel.
- Intérieur/extérieur **avant 2000** : récit seulement, non tabulé.

### Clôture éditoriale (avant tout commit)
- **Bibliographe** : clés éco (`blanchard-2019-public-debt`, `mauro-zhou-2021-r-minus-g`,
  `imf-2022-srdsf`, `reinhart-rogoff-2010`, `herndon-ash-pollin-2014`,
  `eichengreen-hausmann-2005-original-sin`, `imf-tunisia-article-iv`, `code-comptabilite-publique-62`).
- **Terminologue** : glossaire (`dette-publique`, `service-de-la-dette`, `encours`,
  `ressources-de-tresorerie`, `solde-primaire`, `ecart-r-g`, `besoin-brut-de-financement`, BTA/BTCT…).
- **Figures en TODO** : BTA/BTCT à la ligne (Tunisie Clearing), service de la dette dans le budget.
- **Revue humaine** puis commit (precis ET tunisia-data), ouverture PR.

## Détails déjà consignés ailleurs
`docs/notes/backlog-dette.md` (reports données), `docs/notes/dette-concordance.md` (périmètres),
`docs/notes/eco-soutenabilite-dette.md` (méthode r−g), `docs/notes/dette-*-sources.md`.

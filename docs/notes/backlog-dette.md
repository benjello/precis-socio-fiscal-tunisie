# Backlog — annexe dette publique

Chantier `chantier/annexe-dette-publique` **fusionné et déployé** (PR précis #785 + #787 ;
données `tunisia-data` #140 ; annexe en ligne sur Pages). Ce fichier ne garde que les **restes
ouverts**. À fusionner dans `docs/notes/backlog-precis.md` par le rôle `archiviste-backlog` après
relecture (évite les conflits sur le fichier partagé pendant que d'autres chantiers tournent).

## Objectif ouvert prioritaire
- **Retrouver les rapports dette extérieure BCT (publication 107) 2013-2022.** Ils lèveraient les
  deux approximations de l'annexe (encours MLT et composition par devise, estimés depuis le récit
  des Rapports annuels) et combleraient l'effet-change 2013-2018. **Web épuisé** (chasse Wayback +
  site vivant menée à terme, 10 nov. 2026 : aucune capture ; le `dette.pdf` canonique ne porte que
  1991-2012 et 2023-2024). Restent hors web : **demande directe à la BCT**, bibliothèques de dépôt
  (INS, universités). Méthode consignée dans `tunisia-data/sources/chercher-des-donnees-tunisie.md`.
  Dès qu'un canal s'ouvre, les séries `-ra` (`dette-exterieure-encours-mlt-ra`,
  `dette-exterieure-devises-ra`) sont remplacées par les tableaux A10/A14/A15.

## Données à sourcer / rapatrier (lisible = URL publique vérifiée ; à obtenir = non récupéré)

### Dette extérieure
- **Registre nominatif des prêts extérieurs** — JORT, 881 lois/décrets de ratification 1962→2026
  (`docs/notes/dette-registre-jort.csv`). Donne prêteur, objet, date, réf. JORT ; **montant** dans
  le corps (repéré sur échantillon OCR), **taux/maturité absents du JORT**. Non dédoublonné par
  accord. Colonne `montant` à extraire des corps (chantier OCR borné).
- **Composition par devise, série longue avant 2020** : rapports BCT pub 107 1991-2019 (format
  différent, à parser au cas par cas) — subsumé par l'objectif pub 107 ci-dessus.
- **Durée de vie moyenne / taux moyen de la dette extérieure** : état BCT dédié (table en ligne
  `PL235010`) ; pas d'indicateur isolé dans le rapport dette (matrices 2D A16-A19 seulement).
- **Conditions moyennes IDS** (`DT.INR.DPPG` taux, `DT.MAT.DPPG` maturité) : non encore versées.

### Dette intérieure (titres d'État en dinars)
- **Stock vivant à la ligne de titre (BTA/BTCT)** : ISIN, coupon, échéance, encours — Tunisie
  Clearing (courbe des taux, bulletins) et BVMT. Encours par ligne **non tabulé**, à collecter.
- **Adjudications BTA/BTCT** (montant retenu, taux moyen pondéré, maturité) — MdF (DGGDCF) +
  bulletins SVT. Série temporelle **dispersée**, à consolider.
- **Encours agrégé Bons du Trésor** — BCT (indicateurs quotidiens testés le 6 nov. 2026 :
  BTA 36 689,6 MDT ; BTCT 1 645,6 MDT). **Codes de table `PL130xxx` à préciser** pour la série longue.
- **Ventilation par instrument** (BTA, BTCT, emprunts nationaux) — annexe 7 au PLF (`gbo.tn`),
  PDF **arabe** : à relever.
- **Registre JORT des emprunts intérieurs** (`docs/notes/dette-interieure-registre-jort.csv`,
  198 lignes 1950→2026, colonne `categorie`). ATTENTION : les « emprunts obligataires » sont
  **surtout corporatifs** (70) — hors dette d'État ; dette d'État = bons d'équipement 63 +
  emprunts nationaux 6 + bons du Trésor 15 (+ 17 intitulés arabes رقاعي à classer) ; zone grise
  rétrocédés 25 / garantis 2.
- **Intérieur/extérieur avant 2001** : récit seulement, non tabulé (RA BCT 1986-2000 à dépouiller ;
  recoupement possible avec l'annexe 7 au PLF, arabe). Voir `dette-interieure-exterieure-longue.md`.

### Dynamique dette/PIB et soutenabilité
- **Charge d'intérêt budgétaire, finesse** : 2005-2007 sans bulletin national (BM seulement, non
  versé) ; bulletins d'exécution MdF 2019/2021/2022/2023 non rapatriés (valeurs plus récentes
  d'années déjà couvertes) ; clés `minfin-resultats-provisoires-{2019-12,2021-12,2022-12,2023-12}`
  à créer si exploitées. Éditions listées dans `docs/notes/dette-execution-bulletins.{md,csv}`.
- **Effet-change avant 2019** : les rapports anciens décomposent la variation **par devise**, non
  en agrégat change/volume — extension < 2019 demande un autre traitement.
- **Besoin brut de financement** (déficit + amortissements/PIB) — amortissements à assembler.
- **Liquidité, variante 100 % BCT** des réserves/exportations (table en ligne `PL237010` ou BSF) :
  possible en recoupement, non nécessaire (la série BM versée est déjà d'origine BCT et plus longue).
- **Projectif (DSA : chocs, fan charts, besoin brut futur)** : à **citer** depuis la DSA du FMI
  (Article IV), jamais refaire avec des paramètres inventés.

## Limites structurelles (à écrire telles quelles dans l'annexe, pas à combler)
- **Prêt individuel nominatif** (un emprunt extérieur = son taux + sa maturité + son échéancier
  propres) : **non public** (interne DRS/BM et SIADE/MdF). Maille fine publique = créancier × année.
- **Détenteurs de la dette intérieure par ligne** et ventilation fine banques / non-banques /
  non-résidents : **non publics**.
- **« Autres devises » (≈ 9 % de la dette extérieure)** ≈ dette FMI en DTS (`DT.DOD.DIMF.CD`,
  publié) ; reliquat (GBP + mineures) **non public** (interne SIADE BCT). Reproduction exacte de
  l'effet-change au dinar impossible (reste à ±30 % faute du détail « autres ») — décision prise :
  garder l'effet-change **reporté par la BCT**.

## Restes éditoriaux (confirmations et décisions humaines)
- **Titre arabe** de la clé `minfin-dette-2025` (formé par analogie + nom de fichier gbo.tn) et
  **termes arabes** des 13 entrées de glossaire (statut `provisoire`) : à confirmer à l'image sur
  l'édition arabe du Rapport sur la dette publique.
- **Architecture glossaire / annexes racine** (question architecte) : une annexe de 1er niveau
  (hors `precis/fr/<book>/`) ne résout pas les ancres `#g-…` (`_glossaire.infobulles.html` est
  engendré par livre ; `build_glossary` ne scanne que `precis/fr/<book>/`). Les 13 définitions
  restent acquises dans `glossaire.yml` (fonds global + bijection de traduction), **sans renvois
  câblés** dans l'annexe. Trancher : étendre `build_glossary`/infobulles aux annexes racine, ou
  assumer un glossaire en texte seul pour les annexes transversales.
- **Figures encore à produire** : BTA/BTCT à la ligne (Tunisie Clearing) ; service de la dette dans
  le budget.

## Références à verser (bibliographe)
- `code-comptabilite-publique-62` (art. 62 CCP, base légale des prêts du Trésor) — texte à localiser
  au JORT, non encore lu.
- Clés économiques de soutenabilité (sur source primaire avant versement) : `blanchard-2019-public-debt`,
  `mauro-zhou-2021-r-minus-g`, `imf-2022-srdsf` (DSA), `reinhart-rogoff-2010`,
  `herndon-ash-pollin-2014`, `eichengreen-hausmann-2005-original-sin`, `imf-tunisia-article-iv`.
  Méthode r−g détaillée dans `docs/notes/eco-soutenabilite-dette.md`.

## Détails déjà consignés ailleurs
`docs/notes/dette-concordance.md` (périmètres + invariants), `docs/notes/eco-soutenabilite-dette.md`
(méthode r−g), `docs/notes/dette-*-sources.md`, `docs/notes/dette-execution-bulletins.{md,csv}`,
`docs/notes/dette-interieure-exterieure-longue.md`.

# Reproduire les revenus 2014 du rapport présidentiel à partir des états financiers publics — et les prolonger

*Note de travail — novembre 2026 (rafraîchie le 7 novembre).*

## Résumé

Le rapport de la Présidence (Unité de suivi des entreprises publiques) donne, pour 2014, les
**revenus** d'une liste d'entreprises. On ne reprend pas sa compilation : on **recompose** ces mêmes
revenus depuis la **source primaire** — les états financiers publiés (BVMT, états STEG/ETAP). La
concordance est **au dinar** pour les entreprises vérifiables (STEG 3 736, Tunisair 1 149,6, STB 499,7,
BNA 596,8, ETAP 2 153 MD). On **prolonge** ensuite ce point de départ : la **valeur ajoutée** est
désormais lue, sur états financiers primaires, pour **16 entreprises** (de 2000 à 2025 selon l'entreprise),
et la **valeur ajoutée par agent** se calcule partout où l'effectif est publié. Toutes les données
viennent d'une **source unique** — le jeu de données *Comptes primaires des entreprises publiques*
(voir l'annexe « Données ») —, où chaque valeur porte
son fichier, sa page et un **niveau de preuve** (A : VA brute imprimée au schéma des soldes
intermédiaires de gestion, re-vérifiée ; B : calculée et corroborée par une identité indépendante ;
C : calculée, cohérence de lecture seule). Aucune lacune n'est interpolée.

## 1. Le point de départ

Le rapport sur les entreprises publiques annexé au suivi présidentiel présente, entreprise par
entreprise, un **chiffre de revenus 2014**. C'est une **compilation** : il agrège des données remontées
par les tutelles, sans donner l'état financier sous-jacent. On fait l'inverse. Pour chaque entreprise
**cotée ou publiant ses comptes**, on lit directement l'**état de résultat** (ou le produit net bancaire
pour les banques) dans le document déposé à la Bourse de Tunis ou publié par l'entreprise. On obtient
ainsi les revenus 2014 **indépendamment** de la compilation présidentielle — et donc de quoi la
**vérifier**.

## 2. Reproduction du tableau 2014

Pour les entreprises dont on tient l'état financier primaire, la cible de la Présidence et notre lecture
coïncident exactement (millions de dinars) :

| Entreprise | Cible Présidence 2014 | Nos états financiers 2014 | Écart | Source primaire |
|---|---:|---:|---:|---|
| STEG | 3 736 | 3 736,0 | 0 | `steg_ef_2014.pdf`, p. 13 |
| ETAP | 2 153 | 2 153,0 | 0 | `2014_etats_financiers.pdf`, p. 1 |
| Tunisair | 1 149,6 | 1 149,6 | 0 | `2014_individuel.pdf`, p. 26 |
| BNA | 596,8 | 596,8 | 0 | `2014_individuel.pdf`, p. 3 |
| STB | 499,7 | 499,7 | 0 | `2014_individuel.pdf`, p. 3 |

**Écart nul** sur ces cinq entreprises : la source primaire reproduit la compilation au dinar. Deux
limites de périmètre, dites franchement : la **STIR** ne publie pas d'états financiers exploitables
(lacune non comblée) ; les **caisses** (dont le « revenu » est une masse de cotisations) sont hors de
notre portée.

## 3. Prolongement : la valeur ajoutée et la productivité, 16 entreprises

Là où le premier état de cette note s'arrêtait à la STEG et à 2018, la **valeur ajoutée** est maintenant
lue sur états financiers pour **16 entreprises publiques productives**, et la **VA par agent** se calcule
sur la fenêtre où l'effectif est publié. On la lit **directement** au schéma des soldes intermédiaires de
gestion quand il existe (niveau A), sinon on la **calcule** (production − consommations intermédiaires)
et on la **corrobore** par une identité indépendante (niveau B) ou, à défaut, on signale qu'elle ne
repose que sur la lecture des composantes (niveau C).

### a) L'étendue, entreprise par entreprise (VA, millions de dinars ; niveau de preuve)

| Entreprise | Nature | VA | Points | Preuve |
|---|---|---|---:|---|
| SOTRAPIL | transport d'hydrocarbures par pipeline | 2000-2025 | 26 | A |
| Tunisair | transport aérien (pass-through) | 2000-2023 | 23 | A |
| ETAP | hydrocarbures (pass-through) | 2004-2024 | 21 | B |
| Ciments de Bizerte | ciment | 2009-2024 | 16 | A |
| SNCFT | chemins de fer (service public) | 2010-2023 | 14 | C |
| El Fouladh | sidérurgie | 2012-2024 | 13 | B |
| CPG | phosphate | 2004-2015 | 12 | A |
| TRANSTU | transport urbain (service public) | 2010-2021 | 12 | C |
| SOTUMAG | marché de gros | 2002-2024 | 11 | A |
| STEG | électricité et gaz | 2014-2023 | 10 | A |
| La Poste | services postaux et financiers | 2015-2023 | 9 | B |
| TTN | facilitation du commerce (service IT) | 2017-2025 | 6 | B |
| SONEDE | eau potable | 2010-2016 | 5 | C |
| GCT | engrais chimiques | 2010-2014 | 5 | A |
| Tunisie Télécom | télécommunications | 2007-2009 | 3 | A |
| Tunisie Autoroutes | concession autoroutière | 2021-2022 | 2 | B |

### b) La valeur ajoutée par agent (milliers de dinars par agent)

L'amplitude du secteur productif va d'un service public urbain qui ne dégage presque aucune valeur
marchande propre à l'extraction d'hydrocarbures, capital-intensive :

- **ETAP — ~2 000 à 3 000 kD/agent** (2004-2024). *Majorant* : les revenus incluent, pour une large
  part, la commercialisation de la part de l'État dans les hydrocarbures (pass-through) ; non comparable
  à une entreprise industrielle.
- **SOTRAPIL — 137 à 163** (2018-2023) : la plus productive hors extraction.
- **CPG — pic à 226 en 2008** (bulle du phosphate), 32 à 153 ensuite.
- **Tunisie Télécom — ~99** (2007-2009, série ancienne).
- **STEG — 37 (2018) → 112 (2023)** ; la forte hausse récente est portée par la **subvention
  d'exploitation**, comprise dans la VA au sens du schéma des soldes intermédiaires de gestion (à lire
  avec cette réserve).
- **La Poste — 31 (2016) → 76 (2023)** ; **El Fouladh — 25 à 83** ; **GCT — 50** (2014) ; **Ciments de
  Bizerte — 28 à 113** (effondrement à 28 en 2023) ; **SONEDE — 20 à 29**.
- **Tunisair — 64-80, puis 19 en 2020** (Covid), remontée à 48 en 2023.
- **Service public subventionné** — **SNCFT 13-24**, **TRANSTU 11-21** *au coût des facteurs* ; aux
  **prix de base** (hors compensation de service public), leur valeur ajoutée marchande propre est
  **quasi nulle** (TRANSTU ≈ 0 ou négative) : elles vivent de la compensation de l'État.
- **Tunisie Autoroutes — ~51** en 2022 *hors l'élément exceptionnel* de 324 MD (« autres produits »,
  retraitement) ; le chiffre brut de 268 n'est pas significatif.

### c) Deux conventions à garder en tête

- **La subvention d'exploitation.** La VA au sens du schéma des soldes intermédiaires de gestion
  **inclut** la subvention tarifaire sur les produits (STEG, SONEDE) : c'est la *VA aux prix de base*.
  Pour les compensations de **service public** (SNCFT, TRANSTU), une *VA hors subvention* est donnée en
  regard ; elle seule éclaire la productivité marchande propre.
- **Le pass-through.** ETAP, Tunisair et, à moindre degré, SOTRAPIL commercialisent des produits qui
  gonflent revenus et achats sans valeur ajoutée propre ; leur VA/agent est à lire avec ce caveat.

## 4. Annexe — méthode, sources et niveaux de preuve

**Source unique.** Toutes les valeurs viennent du jeu de données *Comptes primaires des entreprises
publiques*, consolidé des lectures sourcées ligne par ligne (fichier + page + méthode de lecture). Les
effectifs viennent du jeu de données *Effectifs des entreprises publiques* (rapports du ministère des
Finances, dédoublonnés à la dernière édition) et, à défaut, des rapports d'activité des entreprises.
Leur contenu et leur emplacement exact figurent dans l'annexe « Données » en fin de rapport.

**Niveau de preuve de chaque valeur ajoutée** (colonne `evidence_va`) :
- **A** — VA brute **imprimée** au schéma des soldes intermédiaires de gestion, re-vérifiée ligne à
  ligne (51 points recoupés : le bug de lecture d'un générateur antérieur était isolé à Tunisair
  2009/2010, corrigé), ou **posée** par l'entreprise dans sa synthèse annuelle (CPG, GCT).
- **B** — VA **calculée** (production − consommations intermédiaires) et **corroborée** par l'identité
  *indépendante* `résultat d'exploitation + charges de personnel + dotations` (ETAP, El Fouladh, TTN,
  La Poste, Tunisie Autoroutes). Les résidus sont attribués et vérifiés (variation de stock de pétrole
  brut chez ETAP, subvention d'équilibre d'El Fouladh en 2012).
- **C** — VA **calculée**, corroborée seulement par la **cohérence de lecture** du même état (SNCFT,
  TRANSTU), ou dont la base a été vérifiée sur le fond mais sans corroboration indépendante (SONEDE,
  dont les « autres produits » — quote-part de subventions d'investissement et apurement ponctuel de la
  dette CNRPS en 2015 — sont correctement exclus de la VA).

**Un sourçage par chiffre, aucune invention.** Un poste absent ou illisible est laissé **vide**
(lacune), jamais estimé ni interpolé. Les contrôles d'identité sont **reportés, jamais forcés** : un
écart s'instruit sur le fond (l'erreur peut être à l'origine), il ne se corrige pas pour faire boucler
l'identité.

**Lacunes assumées.**
- **STIR** : pas d'états financiers exploitables.
- **RNTA, ONAS, OMMP, OACA** : états financiers primaires non publics (seuls des agrégats des annexes
  budgétaires existent, sans le détail des achats — VA non calculable).
- **Effectifs** : la fenêtre du ministère des Finances (~2016-2023) limite la VA/agent pour les
  entreprises dont la VA remonte plus loin (SOTRAPIL, Tunisair, CPG, GCT, Tunisie Télécom avant 2016).
- **CPG, GCT** : VA « posée » par la synthèse annuelle de l'entreprise, non recalculée depuis un état de
  résultat détaillé.

**Répétabilité.** Le dispositif est reproductible : le jeu de données se reconstruit par son script de
consolidation (indiqué en annexe « Données ») ; à mesure que de nouveaux exercices sont publiés, ils
s'ajoutent aux lectures sources et la série se prolonge sans retravail — le présent rapport n'est qu'un
instantané.

## Annexe — Données

Le rapport désigne les jeux de données par un **nom**. Ils vivent dans le dépôt de données du précis
(`tunisia-data`) ; le tableau ci-dessous donne leur contenu et leur emplacement exact, pour
vérification et reproduction.

| Nom | Contenu | Emplacement |
|---|---|---|
| *Comptes primaires des entreprises publiques* | Valeur ajoutée et ses composantes pour 16 entreprises (2000-2025), une ligne par entreprise × exercice × grandeur, avec fichier source, page, méthode de lecture, niveau de preuve et écart d'identité | série `entreprises-publiques-comptes-primaires` ; sortie `data/processed/entreprises-publiques/comptes_primaires_ep.csv` ; reconstruite par `scripts/consolider_comptes_primaires_ep.py` |
| *Effectifs des entreprises publiques* | Effectifs par entreprise et exercice, issus des rapports du ministère des Finances (dédoublonnés à la dernière édition) et, à défaut, des rapports d'activité | série `entreprises-publiques-effectifs-par-entreprise` ; complément lu dans *Comptes primaires* |

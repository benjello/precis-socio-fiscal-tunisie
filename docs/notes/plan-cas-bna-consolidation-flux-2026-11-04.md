# Plan : un cas de bout en bout sur la BNA, 2023 (consolidation et flux entre entités publiques)

Note du 4 novembre 2026. Origine : les demandes de l'équipe SOEs de la Banque mondiale (Henri Fortin : comptes consolidés ; Mohamed Habib Zitouna : emprunts), la réunion du 3 novembre et le brouillon de réponse resté dans Gmail. Ce plan est à exécuter **sur la machine qui a le corpus local** (PDF de la Bourse, copies d'archives) et le réseau vers la Bourse de Tunis, le CMF et l'Internet Archive. Une session cloud n'y suffit pas : ces hôtes y sont refusés par la passerelle. Rien ci-dessous n'a été exécuté.

## Pourquoi la BNA

Le seul groupe qui réunit, dans le dépôt, presque tous les ingrédients (essai du 4 novembre) :

| Ingrédient | BNA | Où |
|---|---|---|
| Dividende par action, 3 exercices | 2023 : 0,9 ; 2024 : 1,0 ; 2025 : 1,15 | `listes/societes-cotees-resultats.csv` |
| Détenteurs publics nommés | État 35,26 % ; en aval BNA Assurances 44,9 %, SIMPAR 30,27 %, ATL 11,1 % ; BNA Participations : Tunis Re 18,98 %, Air Liquide Tunisie 11,06 % | `listes/societes-cotees-participations.csv` |
| Engagements envers les entreprises publiques, par entité | 2016-2024, avec garanties de l'État, agios, provisions | `listes/bna-engagements-entreprises-publiques.csv` |
| Total des actifs et résultat net (ministère) | 2018-2023 | `figdata/fig_ep_bna_fiches.csv` |
| États consolidés de la Bourse | 2006-2014, 2016-2024 (2015 absent) | `listes/delais-publication.csv` |
| Périmètre de consolidation | 2007, 2020, 2021 seulement | `listes/groupes-bancaires-perimetre.csv` |

Les engagements envers les entreprises publiques sont un flux entre entités publiques que les « dettes croisées » du ministère (État-entreprises) ne contiennent pas.

## Constats déjà faits (à reproduire, pas à croire)

Exercice 2023, d'après les relevés versés :

1. **Somme des engagements.** Total imprimé 6 442 355 kDT ; six entités détaillées (Office des céréales 5 070 054, O.T.D. 240 220, O.N.H. 217 656, El Fouledh 119 504, Transtu 116 963, ETAP 65 383) : 5 829 780 kDT. **Écart 612 575 kDT (9,5 %)**, non détaillé.
2. **Garanties de l'État.** Total imprimé 5 941 060 kDT ; détaillé 5 690 762 kDT. Écart 250 298 kDT. Garanties/engagements : 92 % ; Office des céréales : 100 %.
3. **Poids dans le bilan.** 6 442 MD sur un total des actifs de 20 469 MD (31 %) ; 1 128 MD en 2016.
4. **Résultat net 2023** : 190,0 MD (tableau des banques publiques du ministère, `figdata/fig_ep_bna_fiches.csv`) contre 212,043 MD (Bourse, `societes-cotees-resultats.csv`). Écart 22 MD (11 %). Base de chacune : **non établie**.
5. **Dividende de l'État** : 22 565 045 actions × 1,15 = 25 949 802 DT en 2025, égal au montant imprimé. Même contrôle exact pour la STB 2025, la STAR 2024 et la SOTUMAG 2025 (`scripts/flux_intra_publics_cotees.py`).
6. Essai de consolidation de la STB (2018-2021) : négatif entité par entité (seule la mère a des chiffres) ; voie retenue : les états consolidés de la Bourse (backlog, entrée « Comptes consolidés »).

## Étapes

Chaque étape dit ce qu'on lit, ce qu'on écrit et comment on sait que c'est bon. Une valeur non lue reste vide avec sa raison ; on ne comble rien.

### 1. Établir la base de chaque série (individuel ou consolidé) — S
- **Lire** sur la page de la BNA à la Bourse de Tunis les états financiers 2023 individuel et consolidé (résultat net, total des actifs, fonds propres).
- **Écrire** une ligne par (exercice, base, grandeur, valeur, page, sha256 du fichier) dans un relevé versé dans `tunisia-data` (série à nommer, ex. `bna-etats-financiers-2019-2024`).
- **Règle** : le résultat net de la Bourse (212,043 MD) doit égaler exactement l'un des deux états ; sinon, consigner l'écart et son explication éventuelle (exercice, provisoire, retraitement). Le résultat du ministère (190,0 MD) est rapproché de la même manière, avec l'édition (LF 2025) et la page.
- **Résultat attendu** : une phrase dans le chapitre de la BNA qui dit sur quelle base chaque tableau est établi.

### 2. États consolidés de 2019 à 2024 — M
- **Lire** bilan, compte de résultat et notes consolidés, 2019-2024 (2015 manque à la Bourse, hors période).
- **Règles de somme** : actif = passif + fonds propres ; résultat consolidé = résultat individuel ± retraitements annoncés dans les notes (écart expliqué ou consigné) ; part du groupe + intérêts minoritaires = résultat consolidé.
- **Écrire** le relevé dans `tunisia-data`, le catalogue des fichiers (url, sha256, page), puis une section dans `_secteur_financier.qmd` à la suite de « Les filiales » de la BNA.

### 3. Périmètre de 2022 à 2024 — S
- **Lire** les rapports (notes « périmètre de consolidation ») ; les rapports de la STB écrivent « périmètre inchangé » de 2020 à 2024, voir si la BNA fait de même.
- **Écrire** les lignes de 2022, 2023 et 2024 dans `listes/groupes-bancaires-perimetre.csv` (entité, méthode, contrôle, intérêt, source).
- **Règle** : nombre d'entités de l'année N = celui de N-1 + entrées − sorties lues ; 23 entités en 2020 et 2021 dans le relevé.

### 4. Dividendes des filiales de la BNA — S
- **Lire** sur leur page de la Bourse le dividende par action de BNA Assurances, SIMPAR, ATL, Tunis Re et Air Liquide Tunisie (exercices 2023-2025) ; ajouter les lignes à `societes-cotees-resultats.csv`.
- **Règle** (D) : actions × dividende par action = montant imprimé quand le rapport l'imprime. Calculer ensuite le dividende reçu par la BNA et la BNA Participations ; le placer à côté de leur résultat consolidé.

### 5. Recoupement avec les entreprises débitrices — S (faisable sans réseau)
- **Office des céréales** (5 070 MD d'engagements, 79 % du total) : confronter à ses fiches du ministère (dette, garantie) et au tableau « dettes croisées » 2021-2023 (`data/processed/entreprises-publiques/dettes_creances_croisees_2021_2023.csv`, entités `office_cereales`, `steg`, etc.).
- **Règle** : la dette garantie d'une entreprise envers une banque ne peut pas dépasser sa dette totale ; la somme des garanties imprimées par la BNA pour une entité est une borne basse de la garantie de l'État la concernant.
- **Résultat attendu** : pour chaque entité détaillée, un « cohérent / à voir » avec la raison.

### 6. Les 612 MD non détaillés — S
- **Lire** la note aux états de la BNA qui donne le tableau « engagements envers les entreprises publiques » (page déjà relevée, voir la colonne `page_pdf`) : les entités regroupées dans « autres » y sont-elles nommées ?
- **Écrire** les entités manquantes si le tableau les donne ; sinon, la ligne « autres entreprises publiques » avec son montant, et le dire au chapitre.

### 7. Tableau des flux, version de la BNA — S
- **Assembler** : (a) dividendes de l'État et des détenteurs publics nommés de la BNA et de ses filiales cotées ; (b) engagements de la BNA envers les entreprises publiques, avec garanties de l'État ; (c) place dans les états consolidés.
- **Écrire** une section du chapitre (« Les flux entre la BNA, l'État et les entreprises publiques »), figure et tableau avec onglet de données, notes de lecture, contrôles de somme affichés en bas de tableau.

### 8. Généraliser seulement après — M
- Si le cas tient, le même gabarit va à la BH (ETAP à 16,57 %, périmètre 2016-2022), puis à la STB (consolidés 2006-2024). Rien n'est généralisé avant que les règles de l'étape 1 passent sur la BNA.

## Contrôles de somme (à garder dans un test)

| Règle | Énoncé | État |
|---|---|---|
| A | Nombre total d'actions déduit de chaque détenteur d'une société égal à l'arrondi près | OK sur 6 sociétés (`scripts/flux_intra_publics_cotees.py`) |
| B | Somme des parts nommées ≤ 100 % ; reste sans nom affiché | OK partout |
| D | Dividende de l'État = actions de l'État × dividende par action | OK pour BNA 2025, STB 2025, STAR 2024, SOTUMAG 2025 |
| E | Dividende annuel de l'État (Bourse) du même ordre que cumul 2021-2023 du ministère ÷ 3 | BNA : 20,3 MD pour 19,1 MD/an ; BH : 17,5 pour 15,6 : cohérent, non probant |
| F | Σ dividendes de l'État des cotées ≤ « part de l'État dans les bénéfices » du ministère | à faire quand les dividendes 2021-2023 de toutes les cotées sont lus |
| G | Σ engagements détaillés ≤ total imprimé ; Σ garanties détaillées ≤ total ; garanties ≤ engagements par entité | Σ OK ; écarts 612 575 et 250 298 kDT à expliquer (étape 6) |
| H | Actif = passif + fonds propres, part du groupe + minoritaires = résultat (états consolidés) | à faire à l'étape 2 |

Les règles A, B, D et G sont exactes ; E et F sont des bornes d'ordre de grandeur ; H est un contrôle comptable. Aucun écart n'est « corrigé » sans la page qui l'explique.

## Ce que l'équipe de la Banque mondiale pourra voir au terme du cas

- Une base établie (individuelle/consolidée) pour chaque chiffre de la BNA.
- Les états consolidés de six exercices, avec la page.
- Les flux intra-publics identifiables : dividendes aux détenteurs publics nommés, engagements envers les entreprises publiques garantis par l'État, avec les écarts de somme.
- La liste de ce qui reste hors de portée : actionnaires publics en dessous du seuil de la Bourse (Registre, payant), 612 MD d'engagements non détaillés si la note ne les nomme pas, entreprises non cotées.

## Hors de ce plan

- Les emprunts garantis du JORT et les emprunts non garantis : voir l'entrée du backlog (« Comptes consolidés, emprunts garantis du JORT et emprunts non garantis »).
- Les prévisions : le précis reste descriptif.

## Machine, durée, sorties

- **Accès nécessaires** : Bourse de Tunis (états et rapports), PDF locaux, `tunisia-data` en écriture, quarto pour rendre le livre.
- **Ordre conseillé** : 5 (sans réseau), 1, 3, 6, 2, 4, 7.
- **Sorties versées** : relevés dans `tunisia-data` (états financiers consolidés, dividendes des filiales), `groupes-bancaires-perimetre.csv` complété, section du chapitre, test des règles A, B, D, G, H dans `tests/`, ligne de backlog mise à jour.

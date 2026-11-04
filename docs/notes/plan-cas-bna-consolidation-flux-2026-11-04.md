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

## Résultat de l'étape 5 (4 novembre 2026, fait sans réseau)

Script : `scripts/bna_recoupement_debiteurs.py`. Six entreprises, 2018-2023 (les années manquantes des fiches sont laissées vides, pas comblées). Règles : engagement de la BNA ≤ passif de l'entreprise ; garantie de l'État ≤ engagement.

| Entreprise | Engagement de la BNA, 2023 (MD) | Part garantie par l'État | Part du passif (2023) | Verdict |
|---|---:|---:|---:|---|
| Office des céréales | 5 070,1 | 100 % | 58 % de 8 689,3 (passifs hors fonds propres) | cohérent, sauf 2020 (ci-dessous) |
| O.T.D. | 240,2 | 95 % | 31 % (2020) ; fiche 2023 sans passif | cohérent |
| O.N.H. | 217,7 | 92 % | 22 % (2022) ; fiche 2023 sans passif | cohérent |
| El Fouladh | 119,5 | 68 % | 19 % de 621,6 | cohérent |
| Transtu | 117,0 | 93 % | « dette totale » seulement pour 2018-2020, alors que les engagements de la BNA commencent en 2021 : aucune année commune | non testable |
| ETAP | 65,4 | aucune | 1 % de 4 379,9 | cohérent |

1. **Règle « garantie ≤ engagement » : vérifiée pour toutes les lignes.** Aucune garantie imprimée ne dépasse l'engagement.
2. **Règle « engagement ≤ passif » : un seul échec, l'Office des céréales en 2020.** Engagements de la BNA : 3 303,1 MD ; « dette totale » de la fiche : 3 018,0 MD (109 %). Avec « passifs hors fonds propres » de la même année (5 113,6 MD), la règle passe (65 %). Les deux mesures du passif ne se recouvrent pas ; la fiche de 2020 porte les deux, et elles diffèrent de 2 095 MD. À éclaircir avec la note des états de la BNA : les « engagements » comptent peut-être des engagements de signature (cautions, crédits documentaires) que la « dette totale » ne contient pas. Aucun des deux chiffres n'est corrigé.
3. **L'Office des céréales pèse 79 % des engagements envers les entreprises publiques en 2023** (5 070 sur 6 442 MD). Rapporté au passif hors fonds propres, ce poids est de 65 % en 2020 et de 58 % en 2023 (2018 et 2019, rapportés à la « dette totale », mesure différente : 70 % et 90 %, non comparables aux années suivantes). Qui détient le reste du passif de l'Office n'est pas dans le dépôt.
4. **La garantie de l'État couvre 100 % de l'engagement de la BNA envers l'Office en 2018, 65 % en 2019, 69 % en 2020, 60 % en 2021, puis 100 % en 2022 et 2023.** Cette rupture n'est pas expliquée dans le dépôt. Le même exercice 2022 voit les emprunts à plus d'un an de l'Office passer de 53 à 584 MD (959 MD en 2023). Rapprocher, sans conclure, du texte qui accorde ces garanties (à chercher au JORT sur la machine locale).
5. **Dettes croisées de l'État (2023)** : l'Office des céréales a 2 185 MD de subventions non réglées de l'État et 1 631 MD de dettes envers lui ; Transtu 1 509 MD de dettes envers l'État, 365 MD de créances ; ETAP 486 MD de dettes envers l'État. Ces séries portent sur l'État, pas sur la BNA : elles ne servent à vérifier aucune règle de somme, seulement à situer l'Office. Dette bancaire garantie de l'Office (5 070 MD, BNA seule) = 2,3 fois ses créances sur l'État.
6. **Les six fiches n'ont pas toutes les années** (matrice complète : `scripts/lacunes_fiches_debiteurs.py`). Transtu : « dette totale » en 2018-2020, aucun passif ensuite, et les engagements de la BNA envers elle ne commencent qu'en 2021, donc aucune année commune. O.T.D. : pas de passif en 2023. O.N.H. : pas de passif hors fonds propres en 2023 (emprunts à plus d'un an et total des actifs présents). La « dette totale » s'arrête en 2020 pour les six entreprises. Le verdict est « non testable », non « cohérent ».

Étape 6 (612 575 kDT non détaillés en 2023) : inchangée, à faire avec les états de la BNA.

## Résultat partiel de l'étape 1 : écart entre le résultat net du ministère et celui de la Bourse (4 novembre 2026)

Script : `scripts/ecart_ministere_bourse.py`. Résultat net en MD, exercices où les deux séries existent.

| Société | Exercice | Édition (ministère) | Ministère | Bourse | Écart |
|---|---|---|---:|---:|---:|
| STB | 2023 | LF 2025 | 50,6 | 59,7 | −15 % |
| BNA | 2023 | LF 2025 | 190,0 | 212,0 | −10 % |
| BH | 2023 | LF 2025 | 140,0 | 143,0 | −2 % |
| Tunisair | 2023 | LF 2025 | −211,1 | −243,0 | +13 % |
| Tunisair | 2022 | LF 2024 | −218,5 | −220,8 | +1 % |
| Tunisair | 2022 | LF 2025 | −176,3 | −220,8 | +20 % |
| Ciments de Bizerte | 2022 et 2023 | LF 2024 et LF 2025 | −29,0 ; −34,4 | −29,0 ; −34,4 | 0 % |

1. **Le ministère n'est pas toujours plus petit** : il est égal à la Bourse pour les Ciments de Bizerte et, pour Tunisair 2022, égal à 1 % près dans l'édition LF 2024 mais de 20 % plus petit dans l'édition LF 2025 (le chiffre a été révisé entre les deux éditions).
2. **Hypothèse à tester (étape 1)** : les Ciments de Bizerte n'ont que des états individuels à la Bourse (aucun consolidé) et leur résultat est identique dans les deux séries. Les quatre autres ont des états consolidés. L'écart serait alors la différence entre un résultat individuel (fiche du ministère) et un résultat consolidé (Bourse). **Rien ne le prouve aujourd'hui** : on ne sait pas si le chiffre de la Bourse dans `societes-cotees-resultats.csv` est individuel ou consolidé. Test : rapprocher le chiffre de la Bourse, pour la BNA 2023, des deux états de la page.
3. **Les chiffres du ministère sont révisés d'une édition à l'autre** (Tunisair 2022 : −218,5 puis −176,3 ; Tunisair 2021 : −413,5 puis −414,1) ; il faut toujours citer l'édition.

Tests ajoutés : `tests/test_flux_intra_publics_cotees.py` (règles A, B, D, G ; actions de l'État égales dans les deux relevés).

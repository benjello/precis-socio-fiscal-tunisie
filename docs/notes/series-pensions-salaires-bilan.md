# Séries des figures « pensions, salaires et barème » — bilan en cours

Note **en cours** : elle recense, série par série, ce qu'utilisent les figures du livre
« Retraites » ajoutées en septembre 2026 (`precis/fr/retraites/figures/pension_salaire.py`,
`precis/fr/retraites/figures/bareme_actualisation.py`), avec leur source exacte, leurs
spécificités, leurs raccords et ruptures, les contrôles faits et les questions ouvertes. Elle
prépare le **bilan global** demandé par l'utilisateur : chaque question ouverte y attend une
décision ; une fois tranchée, la noter ici avec sa date, puis close la note.

Les données viennent de deux origines : le dépôt **tunisia-data** (fiches `sources/*.md`,
reconstruction dans `docs/croissances-revenus-prix.md`, catalogue `catalog.yml`), snapshoté
dans `precis/_seriescache/` ; et les **paramètres d'openfisca-tunisia** pour le barème,
snapshotés par `scripts/generate_retraites_tables.py`.

**Règle (utilisateur, 22/09/2026) : les séries d'origine sont toujours conservées.** Toute
série corrigée, remplacée ou écartée reste disponible telle que publiée, à côté de la version
retenue (fichier brut dans `data/raw/`, série édition par édition, et indicateur « tel que
publié » dans le fichier des croissances quand la version retenue le remplace). Précision
de l'utilisateur : conserver les **séries originales homogènes**, une par type de source
(bulletins mensuels de l'INS, Banque mondiale, UNdata série par série, éditions des comptes de
la nation, rapports de la BCT…), chacune avec son entrée de catalogue dans tunisia-data ; les
séries composites du fichier des croissances n'en sont que des dérivées.

**Fait** (tunisia-data #13, 22/09/2026) : inventaire des séries homogènes sous-jacentes,
section « Séries homogènes sous-jacentes » de `docs/croissances-revenus-prix.md` ; créées
`wdi-tunisie`, `bct-cout-de-la-vie`, `ins-annuaire-ipc`. Questions ouvertes : brancher
`build_croissances_revenus.py` sur `wdi-tunisie` plutôt que sur les JSON bruts (change la
colonne `source`) ; `bct-ipc-base2015` non séparable rapport par rapport.

## 1. Barème d'actualisation des salaires (RSNA)

- **Série** : `rsna-actualisation-salaires` (snapshot du précis, émis par
  `scripts/generate_retraites_tables.py` ; paramètres
  `retraite/rsna/salaire_reference/actualisation/annee_AAAA`, openfisca-tunisia ≥ 0.95 ; 2016, 2017
  et 2019 depuis la 0.112).
- **Source** : 31 arrêtés du ministre des affaires sociales, un par année, 17/11/1994 → 16/07/2024,
  JORT sur pist.tn (colonne `lien` de chaque coefficient ; 2019 : trouvé dans la seule édition arabe). 1 488
  coefficients.
- **Spécificités** : aucun arrêté retrouvé pour 2025 ni 2026 (ceux de 2016, 2017 et 2019, trouvés
  le 24/09/2026, ne sont indexés par jort_cache que sous leur intitulé arabe) ; barème 2013
  recalculé, repris en 2014-2016, 2017 revient au calcul antérieur ; 1996 lu sur scan, 2024 sur l'image insérée.
- **Constat** (non énoncé par les textes) : chaque barème reproduit l'évolution de l'indice
  des prix à moins de 0,4 % (2013-2016 : jusqu'à 1,1 %, sur les salaires de 1997) ; le taux
  implicite du barème de 2024 s'écarte de l'inflation d'au plus 0,23 point (moyenne 0,03).
  Ni le décret n° 94-1429 ni l'arrêté de 2022 ne donnent de méthode.
- **Question ouverte** : la méthode du ministère est-elle publiée hors JORT ?

## 2. Prix à la consommation (1963-2023)

- **Source** : `croissances-revenus-prix`, indicateur « prix à la consommation » : BCT
  (1962-1975, relevé à la main), annuaires statistiques de l'INS (1976-2023) ; clés `bct-ra`,
  `ins-annuaire`.
- **Rupture** : raccord de deux bases en 1970 (marqué sur les figures). Écart maximal barème /
  prix de 0,2 % sur les salaires de 1972-1973, sans doute lié à ce raccord.

## 3. PIB nominal (1962-2025)

- **Source** : `croissances-revenus-prix`, indicateur « PIB nominal ».
  - 1962-1992 : Banque mondiale, WDI `NY.GDP.MKTP.CN` (clé `wb-wdi`), non vérifiable dans une
    même base.
  - 1993-2001 : UNdata, tableau 4.1, B.1*g, série la plus récente portant les deux années
    (série 30 jusqu'en 1997, série 100 ensuite ; clé `undata-sna`).
  - 2002-2025 : INS, *Comptes de la nation*, 19 éditions (clé `ins-cnat-2015`).
- **Correction** (tunisia-data #11) : le WDI accolait deux bases sans raccord en 1997
  (+20,3 % → +9,6 %) et en 2010 (+12,7 % → +7,5 %).
- **Fait** (tunisia-data #13, 22/09/2026) : indicateurs « PIB nominal, Banque mondiale (WDI,
  tel que publié) » et son pendant par habitant, 1962-2025, sans correction ; série homogène
  `wdi-tunisie` (niveaux tels que téléchargés).
- **Questions ouvertes** : 2002-2005 en base 1983 (règle des éditions) ou en base 1997
  (UNdata série 100 ; 2005 : 7,20 % contre 7,81 %) ? 1974 (+34,4 %) et 1983 (+18,0 %) à
  vérifier. Deux extracteurs de PIB dans tunisia-data (`extract_cnat_pib.py`,
  `extract_cnat_pib_nominal.py`) : retirer l'ancien ?

## 4. Salaire brut par salarié (2002-2012)

- **Source** : salaires et traitements bruts (D.11) des *Comptes de la nation* (tunisia-data
  #7) rapportés aux salariés de l'enquête emploi (clé `ins-enpe`).
- **Spécificités** : brut, hors charges patronales (le superbrut D.1 a été écarté à la
  demande de l'utilisateur) ; 2004-2005 manquent (recensement) ; **rupture 2011** (enquête de
  mai → moyenne des trimestres), marquée sur les figures.
- **Écarté** : la série 2013-2021 hors administration centrale et hors fonction publique
  (dents de scie venues du dénominateur : emploi BCT × part des salariés modélisée par le BIT
  − effectifs de la fonction publique).

## 5. Salaire déclaré à la CNSS

Deux mesures, **jamais raccordées**, tracées en deux séries distinctes :

- **INS, salariés permanents du privé non agricole, 2001-2025** (clés `ins-bms`,
  `ins-guide-salaires-prive-2026`, `ins-portail-2006-salaires-prive`,
  `ins-portail-2009-salaires-prive`). Panel de salariés déclarés cinq trimestres de suite :
  **pas un salaire moyen**. Taux annuel = chaînage des quatre trimestres (retrouve les taux
  annuels publiés 2010-2021 à 0,22 point). 213 bulletins mensuels lus ; 52 trimestres sur
  75 révisés au moins une fois.
  - 2001-2007 : premier portail de l'INS (archives du web) ; les pages ne nomment pas la
    CNSS et ne documentent pas la méthode — l'appui sur les salaires déclarés est déduit de la
    continuité de l'indicateur (même code 0402040, mêmes valeurs sur 2007-2009).
  - Questions ouvertes : T1 2024 (2,1) ne repose que sur la page en ligne, non archivée (le
    bulletin donnait 2,2) ; titre français de la page arabe de 2009 à faire relire par le
    terminologue (« salaire moyen » en 2006, « الأجور » en 2009).
- **Banque mondiale 2004, salaire annuel moyen des salariés déclarés, 1995-2000** (clé
  `wb-2004-employment-strategy-annexes`, tableau 8.1 lu à l'image). Niveau inutilisable (sous
  le SMIG : années incomplètes comprises) ; seule la croissance l'est.

## 6. CNRPS : pension moyenne et salaire moyen des cotisants

- **Sources** : Banque mondiale 1993 (1980, 1985-1991 ; clé `bm-1993-social-protection`) et
  guides statistiques / rapports d'activité de la caisse (2000-2020 ; clé
  `cnrps-guides-rapports`, archives du web). Trou 1992-1999.
- **Spécificités** : pension moyenne **toutes natures** calculée (dépenses ÷ pensions ÷ 12) ;
  salaire des cotisants reconstitué (cotisations ÷ taux ÷ affiliés ÷ 12), donc **brut** (assiette),
  **surestimé depuis 2002** par la contribution des retraités à la péréquation ; 1980-1991 :
  pensions avec prestations familiales, taux de 12 % (5 % + 7 %, en vigueur 1975-1994).
- Le rapport pension / salaire **n'est pas un taux de remplacement**.

## 7. Séries anciennes de salaires (tunisia-data #12, 22/09/2026)

Chaque série d'une seule source, aucune raccordée ; taux entre deux années d'un même rapport.

- **Salaire déclaré à la CNSS, BCT** (`bct-salaires-cnss`, rapports annuels, clé `bct-ra`) :
  masse 1960-1971 et 1974-1975, salaire moyen (masse / effectif du même rapport) 1964-1971 et
  1974. Rupture d'assiette en 1961 (plafond de 500 D supprimé ; masse non tracée) ; effectif
  redéfini en 1971 (moyenne trimestrielle ; marqué sur les figures) ; RA 1969 : taux imprimés
  contredits par ses niveaux (niveaux retenus) ; révisions 1965 et 1970 ; rien en 1962,
  1972-1973, ni de 1976 à 1983. 1964-1974 : 6,7 % par an contre 4,0 % pour les prix.
- **Salaire moyen hors agriculture et hors administration, données du ministère du Plan** :
  Banque mondiale 1995 (`bm1995-salaires-secteurs`, rapport 13993-TUN, tableaux 39-41 ; clé
  `bm-1995-pauvrete-annexes`), 1984-1993 : **5,6 % par an contre 7,0 % pour les prix**, sous
  l'inflation sept années sur dix (la Banque mondiale écrirait, p. 41 du même volume selon la note documentaire, non relu : salaires réels −11,1 % de 1983 à
  1993) ; FMI 97/57 (`fmi1997-salaires` ; clé `fmi-1997-selected-issues` — titre *Selected
  Issues*, non *Recent Economic Developments*), autre millésime, divergent dès 1986 (1989 et
  1994 seulement) ; BCT 1999-2007 (`bct-salaire-moyen-secteurs`, taux imprimés, niveaux
  révisés d'un rapport à l'autre) : 5,4 % contre 2,9 %. Niveau environ double du salaire
  déclaré à la CNSS : ne jamais raccorder les deux familles.
- **CNRPS, affiliés 1989-1999** (`bit2002-couverture`, BIT *ESS Paper* n° 4 ; clé
  `chaabane-2002-ess4`) : niveaux, non tracés ; rupture de champ avec la Banque mondiale
  1993 (+21 à +28 milliers en 1989-1991, écart croissant). Quatre coquilles du tableau source,
  annotées (aucune sur la ligne du secteur public).
- **Questions ouvertes** : adresse d'archive du FMI vérifiée par le bibliographe le 22/09
  (200, tableau 5 présent) — fiche de tunisia-data à corriger ; le numéro « 97/57 » n'est
  lisible dans aucune source accessible (PDF du FMI en 403) : `genre` = « IMF Staff Country
  Reports, vol. 1997, n° 057 », à confirmer sur la page de titre ; titre de la Banque mondiale
  1995 : « Allégement » sur la couverture (fiche de tunisia-data à corriger) ; en 1992-1993, la masse « Non Agr. & ADM » de la Banque
  mondiale dépasse ses composantes (taux 1993 : 3,40 % contre 3,28 %).
- **Trous restants** du salaire du privé : 1976-1983 (aucune source) ; 1995-1998 pour la
  famille du Plan.

## 8. Bibliographie et outillage

- Clés à rapatrier dans Zotero : voir `biblio-a-rapatrier.md`.
- `ins-cnat-editions` fusionnée dans `ins-cnat-2015`, déplacée au fonds commun (21/09/2026).
- Question ouverte : déplacer au fonds commun `bct-ra`, `ins-fonction-publique-2021`,
  `minfin-remunerations` (citées par deux livres).
- Défaut d'outil : `push_biblio.cles_citees` ne voit pas les clés citées par les figures
  (`figtools.source_line`) ; leur rangement Zotero peut dériver sans alerte.
- Date du guide INS 2026 : tirée des métadonnées du PDF (aucune date imprimée).

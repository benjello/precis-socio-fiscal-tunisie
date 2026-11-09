# Extension de `cnat-comptes-secteurs` vers le passé (base 1997)

Compte rendu de l'extraction des PDF INS « Comptes de la nation » pour prolonger la
séquence des comptes par secteur institutionnel avant 2012. Fichier de données :
`cnat-secteurs-2001-2011-extrait.csv` (même dossier). Script rejouable :
`scripts/extract_cnat_secteurs_2005_2011.py` (`--valide`, `--extrait`).

## Faisabilité

Les PDF de `~/projets/tunisia-data/.../comptes-de-la-nation/` sont **du texte**
(couche `pdftotext -layout` propre, pas d'image). Outil : `pdftotext -layout`
(déjà la brique de `tunisia-data/scripts/extract_pdf_tables.py`), puis découpe des
colonnes par séparateurs de ≥ 2 espaces. Aucun OCR nécessaire.

## Périmètre effectivement couvert

| secteur    | années extraites | indicateurs (sur 13) |
|------------|------------------|----------------------|
| snf        | 2005-2011 (7)    | 12 (pas de *dépense de consommation finale* : N/A) |
| sf         | 2005-2011 (7)    | 11 (pas de *dépense conso.* ni *transferts en capital* : N/A) |
| apu        | 2005-2011 (7)    | 13 |
| menages    | 2005-2011 (7)    | 13 |
| exterieur  | 2005-2011 (7)    | 5 (compte du reste du monde : pas de VA, revenu d'exploitation, solde primaire, prestations, revenu disponible, dépense conso., épargne, FBCF) |

378 lignes au total. Colonnes : `secteur,indicateur,annee,base_pib,valeur,edition,source_pdf,page`.
Chaque valeur porte son PDF et sa page.

## Limite de base : 2001-2004 sont en base 1983, pas 1997

Contrairement à l'hypothèse de la tâche, **les quatre éditions les plus anciennes sont
en base 1983**, pas 1997 :

- `2001-2005.pdf`, `2002-2006.pdf`, `2003-2007.pdf`, `2004-2008.pdf` → **Base 1983**
  (page de garde « Les Comptes de la Nation Base 1983 » ; libellés différents :
  « Excédent Brut d'Exploitation », « Impôts indirects », « Intérêts versés »…).
- `2005-2009.pdf` et au-delà → **Base 1997**.

La base 1997 ne remonte donc **que jusqu'à l'année 2005** (première année de l'édition
`2005-2009`). **Les années 2001-2004 n'existent qu'en base 1983** et n'ont pas été
extraites : les chaîner à la série base 1997 violerait la règle « bases jamais
chaînées ». Si on veut couvrir 2001-2004, c'est une **série base 1983 distincte**, à
tirer des quatre éditions ci-dessus (libellés et structure de comptes à ré-aligner).

## Choix d'édition par année

Règle du générateur reprise (« édition la plus récente qui porte l'année ») : chaque
année est prise dans l'édition où elle est **la première** (donc la plus révisée) :
2005←`2005-2009`, 2006←`2006-2010`, … 2011←`2011-2015`.

## Convention emplois / ressources (pour concorder avec la série)

Chaque secteur a une page **EMPLOIS** puis une page **RESSOURCES**. Les *soldes*
(valeur ajoutée, revenu d'exploitation, solde des revenus primaires, revenu disponible,
épargne, capacité/besoin) sont identiques des deux côtés ; les *flux* diffèrent. La
série existante a figé un côté par (secteur, indicateur) — convention reproduite ici
pour homogénéité :

- **snf, sf** : `interets`, `autres transferts courants`, `transferts en capital` →
  côté **RESSOURCES** ; le reste → **EMPLOIS**.
- **apu, exterieur** : tout → **EMPLOIS** (le générateur n'utilise que la table emplois
  de l'APU).

## Validation par chevauchement (test décisif)

Le script rejoue les éditions `2012-2016` et `2013-2017` (celles qui ont produit la
série actuelle) et compare, cellule à cellule, aux valeurs base 1997 de
`precis/_seriescache/cnat-comptes-secteurs.csv`, années 2012-2017 :

- **176 concordances exactes** (snf, sf, apu, exterieur) ;
- **0 écart** et **0 cellule de la série non reproduite** pour ces quatre secteurs ;
- 107 cellules extraites en plus (la série d'origine est lacunaire : son extraction
  `extract_pdf_tables` en mode `cols` avait perdu des lignes — mon extraction les
  retrouve).

Le parseur reproduisant **à l'identique** la série sur les éditions de chevauchement,
l'extraction des éditions plus anciennes (même mise en page) est fiable. Vérifications
manuelles ponctuelles faites contre les PDF (snf 2005 p96/97, apu 2005 p106, menages
2005 p114/115) : exactes.

## Réserve importante — le « ménages » de la série est buggé

**Les 35 seuls écarts de validation sont tous sur `menages`**, et ils ne sont pas une
erreur de mon extraction : la série **actuelle** confond le secteur ménages avec sa
**sous-table « entreprises individuelles »**. Cause : collision de *slug* dans
`tunisia-data/scripts/consolidate_cnat.py` — les pages `COMPTES DES MENAGES (MEN)` et
`COMPTES DES MENAGES / Entreprises individuelles` ont le même slug ; la seconde
(numéro de page plus élevé) écrase la première. Symptôme vérifiable dans la série :
pour ménages, `revenu disponible brut == épargne brute` et **aucune** `dépense de
consommation finale` — ce qui n'a de sens que pour le compte des entreprises
individuelles (sans consommation finale).

J'ai extrait le **compte des ménages complet** (`COMPTES DES MENAGES (MEN)`), qui est
le bon pour une « séquence des comptes par secteur ». Il diffère donc de la série
2012+. Exemple du **saut** si on prolonge naïvement :

| ménages, revenu disponible brut | 2011 (mon extrait, plein) | 2012 (série, ent. ind.) |
|---|---|---|
| | 46 744,0 | 17 987,4 |

**Avant d'intégrer `menages`**, il faut trancher :
1. soit **corriger la série 2012+** pour qu'elle porte le compte ménages complet (les
   bonnes valeurs 2012-2017 sont disponibles par la même méthode : elles figurent parmi
   les 107 « cellules en plus » du mode `--valide`), et corriger la collision de slug en
   amont dans `consolidate_cnat.py` ;
2. soit, si l'on veut rester sur l'« entreprises individuelles » (déconseillé), ré-extraire
   `menages` sur cette sous-table — mais elle est étiquetée différemment selon les éditions
   (« Entreprises individuelles » vs « Ménages Purs »), donc instable dans le temps.

Mon fichier retient l'option 1 (compte complet) : c'est le choix correct ; il faut juste
réconcilier le 2012+ au moment de l'intégration.

## Reports / lacunes

- **2001-2004 non livrés** (base 1983 uniquement) — voir ci-dessus. À verser dans
  `docs/notes/backlog-precis.md` ou `backlog-modele.md` selon le devenir souhaité.
- **`exterieur`** : seuls 5 indicateurs existent (compte du reste du monde) ; ce n'est
  pas une lacune d'extraction mais la structure du compte.
- **`menages` 2012+** à reconstruire (compte complet) avant intégration, + **corriger la
  collision de slug** dans `tunisia-data/scripts/consolidate_cnat.py` (sinon le bug
  reviendra à chaque régénération).
- Je **n'ai modifié ni** `precis/_seriescache/cnat-comptes-secteurs.csv`, **ni** le
  générateur, **ni** aucun `.qmd` : intégration laissée à la revue humaine.

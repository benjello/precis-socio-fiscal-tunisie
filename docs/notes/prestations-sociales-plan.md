# Plan de travail — le livre « Prestations sociales »

> Note de cadrage, écrite avant tout travail de rédaction. Elle fixe la structure retenue,
> l'ordre des étapes et l'état des sources. Elle n'engage aucune rédaction : le dossier
> documentaire reste à constituer.

## 1. Pourquoi

Le livre `precis/fr/prestations_sociales/` est le plus en retard des quatre : **85 lignes et
630 mots**, contre 568 lignes et 12 077 mots pour le livre Fiscalité. Il ne comporte **aucune
citation**, aucune ancre de glossaire, aucun tableau, aucun montant, et son unique `include`
actif pointe sur un fichier vide (`_pnafn.qmd`). Aucune note documentaire amont n'existe.

Son contenu se limite à deux choses : un rappel du plan d'ajustement structurel de 1986 comme
origine du PNAFN, et un récit des allocations familiales non contributives de 2020 à 2024
centré sur leurs **bailleurs** (KfW, Banque mondiale, JICA, USAID) plutôt que sur leurs textes.
Aucun texte juridique n'y est cité, pas même la loi organique sur l'AMEN social, mentionnée
sans référence.

## 2. La décision de structure : contributif / non contributif

C'est l'équivalent, pour ce livre, de la coupure contribution personnelle d'État / IRPP qui a
structuré le chapitre fiscalité. Le clivage commande l'ouverture du droit — cotisation contre
condition de ressources —, le financement, l'organisme gestionnaire et le contentieux.

L'état actuel du livre mélange les deux : le PNAFN y apparaît **deux fois**, sous
« Présentation générale » et sous « Les prestations monétaires ».

```
1    Les prestations sociales en Tunisie
1.1  Présentation générale
       · la typologie officielle du ministère des Affaires sociales (trois groupes)
       · le partage contributif / non contributif, retenu comme ossature
       · les organismes : CNSS, CNRPS, CNAM, ministère des Affaires sociales
       · encadré « conventions de lecture »
       · frontière avec les livres Retraites et Cotisations sociales

1.2  Les prestations contributives (sécurité sociale, hors vieillesse)
     1.2.1  Comment une prestation contributive est ouverte      ← introduction mécanisme
              affiliation, régime, stage, assiette, fait générateur, ayants droit
     1.2.2  Les prestations familiales
     1.2.3  Les indemnités de maladie et de maternité
     1.2.4  Le capital décès et les droits des survivants
     1.2.5  Les accidents du travail et les maladies professionnelles
     1.2.6  La protection contre la perte d'emploi
     1.2.7  L'assurance maladie (CNAM)

1.3  Les prestations non contributives (assistance sociale)
     1.3.1  Comment l'assistance est attribuée                   ← ciblage, ressources, score
     1.3.2  Le PNAFN, de 1986 à l'AMEN social
     1.3.3  L'aide médicale : de l'AMG de 1987 aux AMG1 et AMG2
     1.3.4  L'AMEN social (2019 →)
     1.3.5  Les allocations familiales non contributives (2020 →)
     1.3.6  Les aides ponctuelles

1.4  Qui reçoit quoi : la matrice régime × prestation
```

Chaque grande partie s'ouvre sur une introduction posant la **chaîne** — affiliation, assiette,
stage, fait générateur, montant, service pour le contributif ; ciblage, condition de ressources,
score, montant, durée pour l'assistance — puis les sous-sections déclinent chaque maillon dans
le temps. C'est la méthode qui a évité, pour l'IRPP, d'éclater un même dispositif entre trois
dates.

**Frontière avec les autres livres**, à énoncer dans le chapeau. Le livre Retraites traite la
branche vieillesse, organisé **par régime** (RSNA, RSA, RSAA, RTNS, RTTE, bas revenus, artistes,
complémentaire). Un cinquième livre « Cotisations sociales » est annoncé sur le portail et
traitera le financement. Les mêmes régimes servent donc trois livres, pour trois objets
distincts : le prélèvement, la pension, les autres prestations.

## 3. L'état des sources

### 3.1 La ressource centrale : `jort_cache.db`

`PDFs-legislation-tunisie/jort_cache.db` (258 Mo) est **interrogeable en SQL en lecture seule** :

```
sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1' "..."
```

**78 953 textes, couverture continue 1956 → 2026.** Tables : `textes` (recid, type, numero,
titre, objet, ministere, date_signature, date_publication, jort_annee, jort_numero, jort_tome,
pages, pdf_fr, pdf_ar), `keywords` (index matière : 1 814 « Affaires Sociales », 277 « Securite
sociale », 148 « CNRPS », 54 « CNAM »), `textes_fts` (FTS5), `textes_dedup`, `meta`.

C'est la colonne vertébrale de l'appareil de références : numéro, date, fascicule et **page**
pour chaque texte. Deux pièges de méthode :

- le FTS stocke les titres **sans accents** — chercher `securite sociale`, pas `sécurité` ;
- `numero`, `type` et `date_signature` sont parfois NULL, notamment pour les **arrêtés
  ministériels**. Toute concaténation `||` non protégée par `coalesce()` les fait disparaître
  silencieusement — or ils portent une part substantielle du droit des prestations
  (surcompensation de 1956, financement du PNAFN en 1987, aides aux personnes âgées de 1997).

### 3.2 Le miroir iort.tn — correction d'un constat antérieur

`data/iort/textes/md/`, 32 118 textes. La note `fiscalite-irpp-assiette-abattements.md` §F.2
affirmait que les fichiers antérieurs à 2000 ne contiennent que l'habillage du site. **C'est
inexact et il faut le corriger** : ils portent l'**intitulé arabe intégral** à la ligne 39, et
**15 893 titres sur 16 958 sont extractibles** (93,7 %). Ce qui manque avant 2000, c'est le
**corps** du texte et la version française, pas l'identification.

En revanche les champs `السنة` / `العدد` / `التاريخ` y sont des **libellés nus, sans valeurs** :
ne jamais en tirer une date pour un texte pré-2000, elle doit venir de `jort_cache.date_signature`.

Le nommage comporte plus de préfixes que la convention simple ne le laisse deviner :
`dec` (23 623), `loi` (4 532), `dec_gouv` (2 423), `dec_loi` (481), `loi_org` (260), `arr`,
`avis`, `dec_pres`, `decision`, `loi_const`, `amr`, `loi_orient`. C'est ce qui avait fait
conclure à tort à l'absence de la loi organique sur l'AMEN social.

### 3.3 Ce qui est disponible en texte français intégral

| Dispositif | Texte | Fichier |
|---|---|---|
| AMEN social | **Loi organique n° 2019-10 du 30 janvier 2019** | `loi_org_2019_10_2019.md` (161 l.) |
| AMEN social | Décret gouvernemental n° 2020-317 du 19 mai 2020 | `dec_gouv_2020_317_2020.md` (266 l.) |
| AMEN social | Décret-loi n° 2022-8 du 31 janvier 2022 | `dec_loi_2022_8_2022.md` |
| AMEN social | Décret n° 2022-715 (autonomisation économique) | `dec_2022_715_2022.md` |
| AMEN social | Décret n° 2022-919 (système de soins électronique) | `dec_2022_919_2022.md` |
| CNAM | **Loi n° 2004-71 du 2 août 2004** (29 articles) | `loi_2004_71_2004.md` |
| CNAM | Loi n° 2017-47 du 15 juin 2017 | `loi_2017_47_2017.md` |
| CNSS | Décret n° 2000-1902 du 24 août 2000 (organisation) | `dec_2000_1902_2000.md` |
| Régimes | Loi n° 2002-32 (certaines catégories de travailleurs) | `loi_2002_32_2002.md` |
| Régimes | Loi n° 2002-104 (artistes, créateurs, intellectuels) | `loi_2002_104_2002.md` |
| Régimes | Décret-loi n° 2024-4 (travailleuses agricoles) | `dec_loi_2024_4_2024.md` |
| Congés | **Loi n° 2024-44 du 12 août 2024** (maternité et paternité) | `loi_2024_44_2024.md` |
| PNAFN | Décret n° 2014-1526 (banque de données) | `dec_2014_1526_2014.md` |

### 3.4 Ce qu'il faut océriser

La couverture PDF est **complète et sans trou : 12 213 fascicules, 71 années, 1956 → 2026**,
dans les deux langues. L'obstacle est le seul OCR, et `jort_cache` donne pour chaque texte
l'année, le numéro de fascicule et **la page** — le ciblage est donc exact.

Textes fondateurs à établir : **loi n° 60-30 du 14 décembre 1960** (organisation des régimes de
sécurité sociale) et sa chaîne modificative d'une trentaine de textes ; **loi n° 60-33**
(RSNA) ; **décret n° 74-499** (pivot du RSNA, absent du miroir) ; **loi n° 81-6** (secteur
agricole) ; **loi n° 86-86** (création CNSS et CNRPS) ; **loi n° 87-29 du 12 juin 1987**
(assistance médicale gratuite) et décret n° 88-175 ; **loi n° 88-38** et **loi n° 88-39**
(allocations familiales, privé et public) ; **décret n° 76-3** (CNRPS) ; **loi n° 74-41** et
**décret n° 93-308** (capital décès) ; **loi n° 94-28** (accidents du travail) ; **décret
n° 95-1166** (travailleurs non salariés) ; **décrets n° 98-1812 et n° 98-409** (AMG1 et AMG2).

Point d'attention : les fascicules **français de 2018 à 2020** sont les plus mal couverts
(70, 59 et 16 au lieu d'environ 104) — c'est-à-dire précisément les années de l'AMEN social.
Le miroir compense pour les textes majeurs, mais pas pour les arrêtés d'application.

### 3.5 Trois résultats négatifs, qui sont des faits à publier

**Le PNAFN n'a aucun texte fondateur.** Aucune ligne de `jort_cache` ne porte l'intitulé
« programme national d'aide aux familles nécessiteuses », vérification faite en NULL-safe et sur
les racines arabes `معوز` et `محتاج`. Le programme n'existe au JORT que par ses **lignes
budgétaires et ses arrêtés de financement** : loi n° 86-83 du 1er septembre 1986 (loi de
finances rectificative, contribution des organismes de sécurité sociale), arrêté du 6 janvier
1987 fixant la contribution de la CNRPS et de la CNSS, loi n° 87-83 (LF 1988). Il faudra donc
le documenter comme un dispositif **créé par voie budgétaire et administrative**, ce qui est en
soi un trait remarquable pour le principal programme d'assistance du pays.

**L'« indemnité pour perte d'emploi » n'existe pas sous ce nom** avant l'article 17 de la loi de
finances 2025, qui crée un « fonds d'assurance contre la perte de postes de travail pour raisons
économiques ». Candidat antérieur à vérifier sur pièce : la **loi n° 96-101 du 18 novembre 1996
relative à la protection sociale des travailleurs**, modifiée par la loi n° 2002-24. D'où
l'intitulé retenu dans l'arborescence — « la protection contre la perte d'emploi » — plutôt
qu'un nom de prestation qui n'a pas d'existence légale.

**La « majoration pour salaire unique » n'est pas le bon vocable.** Un seul titre la porte, pour
les militaires (décret n° 74-463). Le dispositif de droit commun apparaît sous
« **indemnités à caractère familial** » : décrets n° 75-952, 86-611, 88-1136, 96-1906. C'est
cette expression qui doit servir de clé de recherche.

### 3.6 Il n'y a pas de code à dépouiller

`markdown_output/` contient six millésimes du Code de l'IRPP et de l'IS. **Aucun code de la
sécurité sociale, aucun code du travail.** Il n'existe donc pas, côté prestations, d'équivalent
du code consolidé qui a servi de fil conducteur pour l'IRPP — où les annotations de modification
donnaient la chaîne des textes. Ici, cette chaîne devra être reconstituée depuis `jort_cache`.

## 4. Ce que l'état d'openfisca-tunisia impose

Un point **inverse l'ordre de travail** par rapport au chapitre fiscalité. Pour l'IRPP, les
paramètres existaient et étaient à peu près justes : on a pu générer les tableaux dès le départ,
puis corriger le modèle. Ici, non :

- **toute la branche contributive est un cliché unique daté de 1960** — allocations familiales
  (18 %, 16 %, 14 % d'un plafond trimestriel de 122 D), majoration pour salaire unique,
  contribution aux frais de crèche. Aucune évolution sur soixante-cinq ans ;
- le plafond trimestriel est daté de **1960** tout en citant la **loi n° 88-38 de 1988** — le
  motif de valeur juste rattachée à la mauvaise date, corrigé trois fois cette session ;
- **le PNAFN est la seule série longue** (11 paliers de 1987 à 2018) et n'a **aucune
  référence** ; elle s'arrête en 2018 alors que le montant a été revalorisé depuis ;
- sur environ 32 paramètres, **14 seulement** portent une clé `reference`, presque tous du côté
  AMEN social, dont 10 sans URL ;
- **ne sont pas modélisés du tout** : capital décès, indemnités journalières de maladie et de
  maternité, indemnité pour perte d'emploi, congé de naissance, éligibilité à l'AMG et au PNAFN.

**Conséquence : la documentation doit précéder la génération des tableaux**, et non l'inverse.

### Six pannes du modèle, vérifiées par exécution sur la version 0.72

| Symptôme | Cause |
|---|---|
| `allocation_familiale_non_contributive` échoue **à toutes les dates** | appelle `pnafn_eligible`, qui n'existe pas — `pnafn.py` ne contient qu'un docstring |
| `transfert_monetaire_permanent` échoue **à toutes les dates** | lit `supplements.amen_social_enfants_a_charge` ; le paramètre s'appelle `supplements.enfant_a_charge` |
| `transfert_monetaire_permanent_eligible` échoue **à partir de 2022-06** | appelle `amen_social_score_decile`, qui n'existe pas |
| `af` et `prestations_familiales` incalculables | `prestations_familiales_enfant_a_charge` lève `NameError: age_individu` |
| `af_nbenf` impose un **plancher** de 3 enfants | `max_` employé là où `min_` était visé |
| la tranche 6-18 ans ne sélectionne que les 18 ans et plus | `(6 <= age) * (age >= 18)` au lieu de `<= 18` |

Aucune de ces variables n'est couverte par un test : la couverture et les pannes sont
exactement complémentaires, ce qui explique leur survie.

## 5. Déroulé proposé

**Préalable — merger le travail en cours** avant d'entamer ce chantier, pour ne pas empiler
deux fronts ouverts.

**Étape 1 — dossier documentaire.** Deux notes, `prestations-contributif.md` et
`prestations-assistance.md`, sur le modèle de `fiscalite-irpp-bloc-a-documentation.md` : pour
chaque texte, les **trois dates** (signature, publication au JORT avec numéro et page, effet tel
que l'énonce l'article), et la distinction explicite entre ce qui est **attesté** et ce qui est
**dérivé**.

**Étape 2 — sourcer et corriger les paramètres.** Une PR de paramètres sur `openfisca-tunisia`
portant les séries datées et leurs références JORT, sur le modèle des PR #380 à #386. Les
pannes de formule font l'objet de **tickets distincts**, comme #387 à #390, pour ne pas mêler
correction de données et changement de comportement.

**Étape 3 — rédaction**, selon l'arborescence du §2, avec les tableaux **générés** par
`scripts/openfisca_tables.py` — le module gère déjà les séries scalaires datées et tire la
colonne « Texte » des métadonnées `reference` du paramètre.

**Étape 4 — glossaire et bibliographie.** Le livre n'est pas dans le périmètre de
`scripts/build_glossary.py` (`BOOKS = ["remunerations_publiques", "fiscalite"]`) : l'y ajouter et
lui poser une annexe, dans les **deux** `_quarto.yml`, français et arabe — la pipeline de
traduction ne synchronise pas ces fichiers, piège rencontré trois fois cette session.
Notions à créer : PNAFN, AMEN social, AMG1, AMG2, allocation familiale, indemnité à caractère
familial, transfert monétaire, ciblage, condition de ressources, score d'éligibilité, capital
décès, indemnité journalière. Existent déjà : `cnss`, `cnrps`, `cnam`, `cotisations-sociales`,
`fonds-de-securite-sociale`, `smig`.
La bibliographie du livre n'a que **deux entrées**, dont une pièce jointe Zotero résiduelle
(`23975222/EZEBV8GK`) à retirer ; la seule vraie (`unicef2020`) n'est **jamais citée**.

## 6. Corrections de détail à passer au fil de l'eau

- l'`include` de l'AMEN social est **syntaxiquement cassé** : `<!-- {{< include _amen_social.qmd >} -->`, un chevron manquant ;
- « A partir de février 202 », « ci-desssous », « le programme nationale », « bénéificant » ;
- le PNAFN traité deux fois ;
- les commentaires TODO de la version arabe sont restés **en français**.

## 7. Vérification

`cd precis/fr/prestations_sociales && uv run quarto render --to html`, puis le rendu arabe, avec
pour critères : zéro citation non résolue, ancres `#g-…` qui résolvent réellement, renvois
`@tbl-…` intacts. Puis `./build.sh` et contrôle du site assemblé.

Côté modèle : `uv run openfisca test --country-package openfisca_tunisia tests`, avec des tests
ajoutés sur les variables aujourd'hui sans couverture.

## 8. Périmètre — tranché

**Le livre couvre les prestations contributives non-retraite**, en plus de l'assistance sociale.
Sans cela elles ne seraient nulle part : le livre Retraites ne traite que la branche vieillesse,
et le livre Cotisations sociales traitera le prélèvement.

**Avec une exigence propre : préciser les éligibles.** Une prestation contributive n'est pas
ouverte à tous les affiliés ; elle l'est aux affiliés **de certains régimes**, sous des
conditions de stage et d'assiette qui diffèrent. Un chapitre qui listerait des montants sans
dire qui y a droit serait trompeur — c'est même l'inégalité de couverture entre régimes qui est
le fait le plus documentable du système tunisien.

Concrètement, cela ajoute deux choses au plan :

1. **Dans chaque sous-section de la partie 1.2**, un développement « qui y a droit » : les
   régimes qui ouvrent la prestation, les conditions de stage, les ayants droit, et les
   exclusions. Les régimes concernés sont ceux que le livre Retraites énumère déjà — RSNA
   (salariés non agricoles), RSA (agricoles), RSAA (agricole amélioré), RTNS (travailleurs non
   salariés), RTTE (Tunisiens à l'étranger), régime des bas revenus, régime des artistes,
   créateurs et intellectuels, secteur public (CNRPS) — auxquels s'ajoutent les régimes créés
   récemment, dont celui des travailleuses agricoles (décret-loi n° 2024-4).

2. **La partie 1.4 devient centrale et non plus récapitulative** : une matrice
   **régime × prestation**, indiquant pour chaque croisement si la prestation est ouverte, et
   depuis quel texte. C'est cette matrice qui donne au chapitre sa valeur d'usage, et c'est
   elle qui fera apparaître les angles morts de la couverture.

Le dossier documentaire de l'étape 1 doit donc établir, pour chaque prestation, **le champ
d'application personnel** autant que le montant — et signaler explicitement les régimes pour
lesquels la question n'a pas pu être tranchée, plutôt que de laisser une case vide se lire comme
une absence de droit.

Deux programmes de la typologie officielle — **soutien à l'emploi** et **amélioration des
conditions de vie** — restent hors du plan. Ils seront mentionnés dans le chapeau comme relevant
du périmètre annoncé mais non couverts, plutôt que passés sous silence.

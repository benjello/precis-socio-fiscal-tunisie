# Plan de l'architecte : contributions conjoncturelles et taxes au profit des fonds spéciaux du Trésor (livre de la fiscalité)

*23 octobre 2026. Rôle : architecte. Sources : note documentaire
`docs/notes/fiscalite-taxes-affectees.md` (citée « note, § n »), fiche économiste
`docs/notes/eco-taxes-affectees.md`, versements déjà faits dans ce worktree (clés `lfc-2017`,
`lfc-2018`, `lfc-2019`, `loi73-72-lfc1973`, `lf-2008`, `decret-2000-634`, `decret-2012-435`,
`decret-1955-03-31-budget` et les sept clés d'études ; entrées de glossaire
`contribution-conjoncturelle-exceptionnelle`, `taxe-conjoncturelle`, `fodec`, `taxe-circulation`,
`taxe-protection-environnement`, plus `fonds-special-tresor` déjà présente). Aucun `.qmd` écrit,
aucun fait ajouté. Les mots « cœur », « épine », « fiche » sont des mots de travail : ils ne
paraissent pas dans les chapitres.*

## 0. Décisions de domicile

| Matière | Domicile | Motif |
|---|---|---|
| Contributions conjoncturelles au profit du budget de l'État (1991, 2014-2015, 2017) et leurs variantes ciblées (banques et assurances 2018-2019 et 2024-2025 ; grandes entreprises 2025 ; prélèvement à l'importation 1991) | **chapitre nouveau A** : `precis/fr/fiscalite/_contributions_conjoncturelles.qmd`, « Les contributions conjoncturelles au profit du budget de l'État » | prélèvement versé au budget général, assis sur l'impôt direct : livre de l'instrument (fiscalité). **Ce n'est pas une taxe affectée** : le ranger avec les fonds spéciaux le nommerait mal |
| Taxe au profit du fonds de développement de la compétitivité (FODEC) et taxes sœurs au profit d'un fonds spécial du Trésor (compétitivité agricole et de la pêche, compétitivité du tourisme, protection de l'environnement) | **chapitre nouveau B** : `precis/fr/fiscalite/_taxes_fonds_speciaux.qmd`, « Les taxes au profit des fonds spéciaux du Trésor » | prélèvement ; aucun livre sectoriel (industrie, agriculture, tourisme, environnement) n'existe ; le jour où un livre « environnement » existera, la fiche de la taxe pour la protection de l'environnement y sera candidate |
| Taxe de circulation (vignette) | **hors de ces deux chapitres**. Domicile proposé : une section du chapitre des droits d'enregistrement et de timbre (chantier `precis-wt-fiscalite-timbre-enregistrement`, non touché), à côté des droits de timbre sur les véhicules (première immatriculation, permis de circulation, note § 4.1) | recette du budget général (tableau « A », ligne 25-02 puis 16-02, note § 4.1), pas une taxe affectée ; perçue au moyen de marques fiscales (art. 20 du décret de 1955, connu par l'intitulé de la LF 2003, art. 75). À confirmer par le propriétaire de ce chantier : bloc de passation au § 5 |
| Contributions et taxes déjà logées ailleurs | inchangé : CSS (`fiscalite/_impot_revenu.qmd#sec-irpp-css`, caisses `#sec-caisses-financeur`) ; contribution de 1989 et redevance de compensation 2013-2014 (`compensation/_reformes.qmd#sec-compensation-1989`, `#sec-compensation-redevance`) ; TFP et FOPROLOS (`cotisations_sociales/_prelevements_salaires.qmd#sec-cot-tfp`, `#sec-cot-foprolos`) ; FNE (`marche_travail/_politiques_emploi.qmd`) ; taxe au profit du Fonds de transition énergétique (`compensation/_electricite_gaz.qmd`) ; Fonds de protection des zones touristiques (`finances_locales/_impots_activite.qmd`) | une phrase et un lien, jamais la prose recopiée |
| Contribution de 1 % du chiffre d'affaires de 2019 « au profit des caisses sociales » (LF 2019, art. 87-88) | livre des caisses (affectation aux caisses) ; aucun chapitre ne la porte aujourd'hui → ligne de backlog pour ce livre ; renvoi d'une phrase depuis le chapitre A | domicile : ce qui est prélevé pour les caisses |

**Critère de scission appliqué.** La note propose « un ou deux chapitres ». Il y a deux épines
indépendantes — les contributions (1991 → 2014 → 2017 → 2018 → 2025) et la taxe du FODEC
(1995 → 1996 → 2000 → 2003 → 2011) — qui n'ont ni objet, ni redevables, ni destination communs :
un fichier qui les porterait toutes deux serait à scinder. Deux chapitres, donc, chacun de type
« dispositif », d'environ 6 000 à 9 000 mots de fichier à l'estimation : loin du seuil de 25 000.

**Titres.** « Taxe affectée » n'est pas un terme du *Journal officiel* (note, § 10). Le titre B
suit la loi (« taxe … au profit du fonds … », « compte spécial du Trésor », LF 1995, art. 37) ; la
section « Ce qu'en dit l'économie » emploie le terme doctrinal avec sa référence (McCleary 1991).

**Préfixes.** Contrôlés libres le 23/10/2026 : `ccj` pour A (`#sec-ccj-…`, `#r-ccj-…`,
`#tbl-ccj-…`), `fst` pour B. `cc` est déjà pris (conventions collectives).

**Ordre dans `precis/fr/fiscalite/_quarto.yml`.**

```yaml
  chapters:
    - index.qmd
    - _impot_revenu.qmd
    - _impot_societes.qmd
    - _impot_fortune.qmd
    - _contributions_conjoncturelles.qmd   # nouveau : surcharges de l'impôt direct
    - _patrimoine_immobilier.qmd
    - _tva.qmd
    - _droits_consommation.qmd
    - _taxes_fonds_speciaux.qmd            # nouveau : prélèvements indirects affectés
    - _regimes_incitation.qmd
    - _depenses_fiscales.qmd
```

Le `_quarto.yml` arabe ne reçoit les deux chapitres qu'à livraison de leur traduction (à la main,
AGENTS.md). **Conflit probable** avec le chantier « timbre et enregistrement », qui touchera aussi
`_quarto.yml` et `index.qmd` : fusionner l'un après l'autre, en relisant ces deux fichiers.

---

## 1. Chapitre A — Les contributions conjoncturelles au profit du budget de l'État

### 1.1 Frontière entre les règles de base et les dispositifs

- **Règles de base** : la contribution **générale**, due par toutes les catégories de
  contribuables à l'impôt direct (sociétés, personnes physiques, et selon les épisodes salariés
  et retraités), « au titre de l'année », assise sur l'impôt dû ou sur sa base (acomptes,
  minimum d'impôt, impôt pétrolier, bénéfices, salaire), non déductible, versée au budget de
  l'État : 1991, 2014 (prolongée en 2015), 2017. Sans elle, le dispositif n'existe pas.
- **Dispositifs** : ce qui l'aménage pour un public ou une opération — le prélèvement
  conjoncturel à l'importation (1991, assis sur les droits de douane) ; la taxe conjoncturelle
  sur les banques et les assurances (2018-2019, reprise en 2024-2025) ; la contribution des
  grandes entreprises (2025).

### 1.2 Les grandes réformes (épine)

| Réforme, dates | Texte et articles (lecture) | Ce que la loi cherche | Avant → après | Ce qui y naît |
|---|---|---|---|---|
| **Mise en place : 1991**, « au titre de l'année 1991 » | LFC 1991 (loi n° 91-23), art. 2-5 et 6-7, p. 499 (image) | **objet non relevé** (rubrique à relever : Q1) | contributions exceptionnelles versées à un fonds ou à la Caisse générale de compensation (1973 lue ; 1984-1989 connues par le volume IX ou par intitulé) → contribution générale au profit du budget de l'État : 10 % (sociétés) ou 15 % (personnes physiques) des acomptes dus au titre de 1990, minima 1 000 et 150 D ; 30 % de l'impôt forfaitaire ; 1/30 du revenu brut mensuel de cinq mois pour les salariés ; non déductible | le prélèvement conjoncturel à l'importation (art. 6-7) — naissance groupée |
| **2014-2015** | LFC 2014 (loi n° 2014-54), art. 28 (institution, redevables), 29 (taux), 30 (recouvrement), 31 (non-déductibilité), pp. 2103-2104 (texte) ; LF 2015, art. 26, p. 3466 (texte) | nom donné par la loi : « contribution conjoncturelle exceptionnelle au profit du budget de l'État » ; rubrique **non relevée** (Q1) | rien depuis 1991 → 15 % des 2e et 3e acomptes de 2014 (minimum 0,05 % du chiffre d'affaires 2013 pour les sociétés, 200 D par acompte pour les personnes physiques) ; 50 % du minimum d'impôt (art. 44 § II et 49 § II) ; 10 % de l'impôt pétrolier du 2e semestre ; salariés **et retraités** : 1 à 6 jours de salaire ou de pension selon le revenu net annuel au-delà de 12 000 D | rien ne naît ; la LF 2015 l'étend aux acomptes échus en 2015 (étape) |
| **2017** | LF 2017 (loi n° 2016-78), art. 48-51, pp. 3843-3844 (texte) | **objet non relevé** (Q1) | assiette : l'acompte ou l'impôt → **7,5 % des bénéfices ou revenus** servant de base à l'impôt ; redevables étendus aux **entreprises exonérées** (7,5 % des revenus exonérés ou déduits) et aux revenus agricoles et fonciers ; salariés hors champ ; minima par taux d'IS ; déduction des bénéfices réinvestis (sociétés à 25 %, dans la limite de 50 % de la base) | rien |
| **2018-2019** | LF 2018 (loi n° 2017-66), art. 52, p. 4288 (texte) | **objet non relevé** (Q1) ; nom donné par la loi : « taxe conjoncturelle » | contribution de tous → prélèvement réservé aux banques, établissements financiers et assurances : 5 % puis 4 % des bénéfices déclarés en 2018 et 2019, minimum 5 000 D | naît la taxe conjoncturelle sur les banques et les assurances (fiche § 1.4.2) |
| **2025** | LF 2025 (loi n° 2024-48), art. 38, AR p. 6431 (texte AR) | nom donné par la loi : « مساهمة ظرفية على المؤسسات الكبرى » ; rubrique **non relevée** (Q1) | → 2 % des bénéfices déclarés en 2025, minimum 1 000 D, pour les entreprises dont le chiffre d'affaires 2023 hors taxes atteint 20 millions de dinars et soumises à l'IS au taux de 15 % au titre de 2023 | naît la contribution des grandes entreprises (fiche § 1.4.3) |

Contexte de chaque réforme (ligne « contexte », distincte de « ce que la loi cherche ») : **aucune
source de l'époque lue** (note, § 11). Le rédacteur pose un `<!-- TODO (documentaliste) -->` par
réforme et n'écrit rien (Q2).

**Entre-temps.**
- 1991-2014 : une phrase sur la contribution **volontaire** de 2012 (LFC 2012, art. 5, p. 922, texte : « au titre de l'année 2012 », pour l'infrastructure des régions prioritaires et l'emploi), renvoi au registre.
- 2019-2023 : une phrase renvoie au livre des caisses pour la contribution de 1 % de 2019 au profit des caisses sociales ; une autre signale la reprise, en 2024-2025, de la taxe sur les banques et les assurances (fiche).

### 1.3 Plan, section par section

`# Les contributions conjoncturelles au profit du budget de l'État {#sec-contributions-conjoncturelles .domicile-unique}`
Une phrase d'objet : un prélèvement temporaire, « au titre de l'année », versé au budget de
l'État, assis sur l'impôt dû ou sur sa base.

**`## Vue d'ensemble {#sec-ccj-vue-ensemble}`**
- Établit : ce qu'est la contribution (temporaire, non déductible, versée au budget général) ; qui la paie, épisode par épisode ; qu'elle n'alimente aucun fonds, à la différence des taxes du chapitre B (lien `@sec-taxes-fonds-speciaux`).
- Premier plan : **tableau court des épisodes** `{#tbl-ccj-episodes}` (1991 ; 2014 ; 2015 ; 2017 ; 2018-2019 ; 2024-2025 ; 2025) — redevables, assiette, taux principal, période. Sans citation : liens vers les lignes de registre. Il tient lieu de frise. `<!-- TODO (rédacteur) : frise -->` si une frise commune au livre est faite.
- Ordres de grandeur, datés : prévision de 320 MD et réalisation de 186 MD en 2014 ; prévision de 900 MD en 2017. Renvoi à `@sec-ccj-longue-periode`.
- **Renvois en tête** (une phrase chacun) : CSS (`@sec-irpp-css`) ; contribution de 1989 et redevance de compensation (compensation) ; contribution de 1 % de 2019 (caisses) ; taxes au profit d'un fonds (`@sec-taxes-fonds-speciaux`).
- Callout « Comment les dates sont-elles lues ? » : chaque contribution vaut « au titre de l'année » que l'article nomme et vise des échéances qu'il énumère. Les clauses d'application générale (LF 2017, art. 79 ; LF 2018, art. 67 § 1 ; LF 2025, article final) sont liées à leur ligne de registre. La LFC 2014 n'a pas de clause d'application.
- Replié : `:::: {.chronologie-repliable titre="Dates d'application des contributions : ce que dit chaque texte, 1991-2025"}` — 1991 : période énoncée ; écart de date de la loi n° 91-23 en `<!-- TODO -->` (28 mars au titre, 26 mars à la signature) ; LFC 2014 : sans clause ; LF 2017, LF 2018, LF 2024, LF 2025 : périodes et clauses.

**`## La mise en place, 1991 {#sec-ccj-mise-en-place}`**
- `### Ce qui précède : la contribution exceptionnelle de solidarité {#sec-ccj-antecedents}` — établit l'antécédent **lu** : la LFC 1973 (loi n° 73-72, art. 1-9, pp. 1853-1854, image). Contenu :
  - une « contribution exceptionnelle de solidarité » : un décime ou un demi-décime de plusieurs impôts directs, du 1er novembre 1973 au 31 octobre 1974 ;
  - un fonds spécial, dont les dépenses sont « les contributions en nature ou en espèces au profit des pays et des organismes bénéficiaires de l'aide » (art. 8) ;
  - contrairement à 1991, le produit va donc à un fonds.

  Renvois : le prélèvement de 8 MD sur ce fonds en 1984 vers la Caisse générale de compensation (`compensation/_reformes.qmd`, déjà écrit) ; la contribution de 1989 au profit de la Caisse (volume IX). Les autres contributions exceptionnelles (défense nationale 1959-1967 ; reconductions et majorations 1975-1986 ; loi n° 85-89 ; inondations 1983 ; banques de dépôt 1988) ne sont connues que par leur intitulé : elles vont dans un `<!-- TODO (documentaliste) : OCR -->` et dans le backlog, **pas dans le texte ni dans un registre rendu** (une ligne de registre doit donner le changement concret).
- `### La loi de finances complémentaire de 1991 {#sec-ccj-1991}`
  - Établit, d'après la LFC 1991 (art. 2-5) : les redevables (activités industrielles, commerciales ou non commerciales, avantages fiscaux compris, avec les exclusions de l'article ; salariés résidents de nationalité tunisienne), les taux et minima, le paiement (juin et septembre 1991 ; retenue à la source pour les salariés), la non-déductibilité.
  - Naissance groupée : deux phrases sur le prélèvement à l'importation, renvoi à `@sec-ccj-importation`.
  - Ce que la loi cherche : `<!-- TODO (documentaliste) : rubrique -->`, rien d'écrit. Contexte : TODO (Q2).
  - Replié : le barème complet, dans le registre des règles de base (§ ci-dessous).

**`## Les grandes réformes {#sec-ccj-reformes}`**
- Premier plan : **tableau des réformes** `{#tbl-ccj-reformes}`, quatre lignes (2014-2015, 2017, 2018-2019, 2025), à quatre colonnes comme `tbl-tva-reformes`. Il donne ce que la loi cherche par ses mots ; là où la rubrique n'est pas relevée, la cellule reste vide avec un `<!-- TODO (documentaliste) : rubrique -->`, comme dans le chapitre de la TVA (Q1). Le nom que la loi donne au prélèvement peut y figurer, présenté comme son nom, pas comme son objet. Une phrase d'entre-temps pour 1991-2014 (2012, volontaire).
- `### 2014-2015 : la contribution rétablie, salariés et retraités compris {#sec-ccj-reforme-2014}`
  - Premier plan : redevables, les trois familles de taux (acomptes, minimum, impôt pétrolier), les jours de salaire ou de pension, la non-déductibilité (art. 31) ; la prolongation de 2015 (LF 2015, art. 26), étape.
  - Une proposition dit que le minimum d'impôt y sert d'assiette sans être modifié, avec renvoi à `@sec-irpp-minimum` et au chapitre de l'IS.
  - Replié : `titre="Contribution de 2014 : taux et minima par catégorie de redevables, et barème des jours de salaire"` (la cellule 2014 de la note, § 2.1, en tableau ; la tranche « au-delà de 40 000 D : 6 jours » comprise).
- `### 2017 : l'assiette passe aux bénéfices, les exonérés compris {#sec-ccj-reforme-2017}`
  - Premier plan : 7,5 % de la base ; entreprises exonérées ; salariés hors champ ; déduction des bénéfices réinvestis.
  - Replié : `titre="Contribution de 2017 : taux, minima et déductions par catégorie de redevables"`.
- `### 2018 : un prélèvement réservé aux banques et aux assurances {#sec-ccj-reforme-2018}` — deux ou trois phrases (ce que la loi vise, pour qui), renvoi à la fiche `@sec-ccj-banques`. Phrase d'entre-temps 2019-2023 (§ 1.2).
- `### 2025 : les grandes entreprises {#sec-ccj-reforme-2025}` — deux ou trois phrases, renvoi à `@sec-ccj-grandes-entreprises`.
- `### Le détail, texte par texte {#sec-ccj-textes}` — replié : `titre="Les contributions générales au profit du budget de l'État, texte par texte, 1973-2017"`. Colonnes : date d'effet ou période ; portée ; texte et article (citation, page) ; avant → après. Lignes : 1973 (point de départ — ce qui précède) ; 1991 (rupture) ; 2012 (contribution volontaire — dispositif voisin, voir § 1.6) ; 2014 art. 28-31 (rupture) ; 2015 art. 26 (étape de 2014) ; 2017 art. 48-51 (rupture). Le décret n° 2012-472 n'est connu que par sa notice : TODO, pas de ligne.

**`## L'état du droit en 2026 {#sec-ccj-etat-du-droit}`**
- Établit, par sa date, le fait lu : la LF 2026 ne reconduit ni la taxe sur les banques et les assurances (LF 2024, art. 64) ni la contribution des grandes entreprises (LF 2025, art. 38), et n'institue aucune contribution conjoncturelle (note, § 2.1, texte AR). Le rédacteur **n'écrit pas** « aucune contribution n'est due en 2026 » : des fascicules de 2026 absents de l'index n'ont pas été lus en plein texte. L'ancre RECHERCHE porte le reste.
- Ancre `<!-- RECHERCHE r-contribution-conjoncturelle-2026 : … -->` ; le rédacteur verse la fiche de la note, § 12, dans `docs/recherches.yml` avec `ou: [precis/fr/fiscalite/_contributions_conjoncturelles.qmd#sec-ccj-etat-du-droit]`.
- Pas de colonne « population couverte » : sans objet pour un prélèvement temporaire éteint, à dire (Q9).

**`## Les contributions ciblées {#sec-ccj-dispositifs}`**
- `### Le prélèvement conjoncturel à l'importation, 1991 {#sec-ccj-importation}` — se situe : « né avec la contribution de 1991 ». Il frappe toutes les marchandises déclarées jusqu'au 31 décembre 1991 au taux de 5 % des droits et taxes liquidés, hors redevance sur prestations douanières (LFC 1991, art. 6-7, image). Replié : un registre d'une ligne.
- `### La taxe conjoncturelle sur les banques et les assurances {#sec-ccj-banques}`
  - « Née de la réforme de 2018. »
  - Mécanisme : bénéfices servant de base à l'IS, payée avec l'IS, non déductible.
  - Deux temps :
    - **naissance** en 2018-2019 (rupture : nouveau public) ;
    - **reprise** en 2024-2025 (LF 2024, art. 64, AR p. 6455, texte AR), avec la seule rubrique relevée de tout le chapitre : « دعم توازنات المالية العمومية ». Changements : 4 % des bénéfices déclarés en 2024 et 2025, minimum porté à 10 000 D, assurance takaful et fonds des participants compris. Classement : étape de la rupture de 2018 (désaccord possible, § 1.6).
  - L'antécédent de 1988 (« contribution exceptionnelle des banques de dépôt ») n'est connu que par son intitulé : TODO.
  - Replié : `titre="La taxe conjoncturelle sur les banques et les assurances, texte par texte, 2018-2025"` (deux lignes).
- `### La contribution conjoncturelle des grandes entreprises, 2025 {#sec-ccj-grandes-entreprises}` — « née de la réforme de 2025 » ; champ (20 MD de chiffre d'affaires 2023, IS à 15 % au titre de 2023) ; 2 %, minimum 1 000 D ; non reconduite en 2026 (renvoi à l'état du droit). Replié : une ligne.

**`## La longue période : ce que les contributions rapportent {#sec-ccj-longue-periode}`**
- Famille : budgétaire seule. Phrase de tête : les contributions n'ont aucune ligne propre dans la série des recettes fiscales du ministère ; elles se fondent dans les impôts directs.
- Premier plan : **tableau court** `{#tbl-ccj-previsions}`, prévision par loi de finances et réalisation quand elle est écrite :
  - prévisions : LFC 2014 : 320 MD (salariés 58, personnes physiques 34, pétrolières 73, non pétrolières 155) ; LF 2015 : case vide ; LFC 2015 : 110 ; LFC 2016 : 3 ; LF 2017 : 900 ; LFC 2017 : 740 ; LFC 2018 : 115,2 ; LF 2019 : 60 ; LFC 2019 : 125 ;
  - réalisations : 2014 : 186 MD (IR 39, IS des pétrolières 57, IS des non pétrolières 90) ; 2015 : 75 MD.
  - La colonne « Loi » porte des liens vers un registre replié des tableaux « A » (lignes et pages, citations), pour que le tableau visible ne cite pas de loi dans le fil (`check_domicile_references.py`).
  - Les réalisations citent les rapports semestriels d'exécution (clés à créer : Q10). Ce ne sont pas des lois : citation sur place permise.
- Avertissements, au premier plan, une phrase chacun :
  - ce sont des prévisions ;
  - après 2017, la rubrique ne dit pas à quel prélèvement se rattachent ses montants : **ne pas les attribuer à la taxe sur les banques** (note, § 2.2) ;
  - lois de finances 2024 à 2026 : rubrique non relevée → TODO, rien d'écrit ;
  - réalisations 2017 et suivantes → TODO, rien d'écrit.
- Replié : `titre="Les prévisions de la contribution dans les tableaux « A » des lois de finances, 2014-2019 : lignes et pages"`.
- Renvois : rendement de l'IR (`@fig-irpp-rendement`) et de l'IS (`@fig-impot-societes-rendement`), dont l'exercice 2014 contient ces montants (§ 3).
- Pas de figure : neuf prévisions éparses et deux réalisations ne font pas une série.

**`## Ce qu'en dit l'économie {#sec-ccj-economie}`** — dernière section. La fiche `eco-taxes-affectees.md`
traite de l'affectation, et les contributions ne sont pas affectées : **fiche nouvelle à demander à
l'économiste**, `docs/notes/eco-contributions-conjoncturelles.md`. Son objet : les surtaxes temporaires, la
durée effective d'une mesure annoncée comme temporaire, les prélèvements exceptionnels sur les
banques. Matière disponible : Francis et Moore 2014, déjà obtenu et catalogué. En attendant :
`<!-- TODO (économiste) -->` à la place de la section, sans texte.

### 1.4 Ruptures propres aux dispositifs

- Taxe sur les banques et les assurances : naissance (2018) ; reprise (2024), classée étape.
- Contribution des grandes entreprises : naissance (2025) seule.
- Prélèvement à l'importation : naissance (1991) seule.

### 1.5 Registre de classement des textes (chapitre A)

| Texte | Lecture (note) | Classement |
|---|---|---|
| loi n° 59-42, art. 10, et reconductions jusqu'à la LF 1967 | métadonnées | antécédent ; intitulé seul → TODO, pas de ligne rendue |
| loi n° 73-72 (LFC 1973), art. 1-9 | image | antécédent (point de départ de la mise en place) |
| reconductions 1975-1986 ; LFC 1984, art. 3 ; loi n° 85-89 | métadonnées | antécédent ; intitulé seul → TODO |
| LF 1983, art. 82-84 ; arrêté du 28 janvier 1983 (inondations) | métadonnées | antécédent ; intitulé seul → TODO |
| LF 1988, art. 68 ; arrêté du 13 février 1988 (banques de dépôt) | métadonnées | antécédent de la fiche des banques ; intitulé seul → TODO |
| LFC 1989, art. 3-8 | lue par le volume IX | hors sujet (domicile compensation) ; renvoi |
| LFC 1991, art. 2-5 | image | **rupture** — mise en place |
| LFC 1991, art. 6-7 | image | **rupture** propre à la fiche « importation » (naissance groupée) |
| LFC 1991 : date de la loi | image | écart à signaler (TODO), pas de rupture |
| décret n° 2002-318, abrogé par le décret n° 2003-1539 (« taxe conjoncturelle sur le ciment ») | métadonnées | hors sujet probable (prix d'un produit) ; intitulé seul → backlog, à rapprocher du volume IX ou de B (Q8) |
| LFC 2012, art. 5 | texte | dispositif voisin (contribution volontaire), ligne de registre (désaccord, § 1.6) |
| décret n° 2012-472 | métadonnées | modalités de 2012 ; intitulé seul → TODO |
| LF 2013, art. 63 ; LF 2014, art. 76-77 (redevance de compensation) | volume IX | hors sujet ; renvoi |
| LFC 2014, art. 28-31 | texte | **rupture** 2014 |
| LF 2015, art. 26 | texte | étape (de 2014) |
| LF 2017, art. 48-51 | texte | **rupture** 2017 |
| LF 2017, art. 79 ; LF 2018, art. 67 § 1 ; LF 2025, article final | texte | clauses de date (registre des dates) |
| LF 2018, art. 52 | texte | **rupture** 2018 (naissance d'un dispositif) |
| LF 2018, art. 53 et suiv. (CSS) | lue | hors sujet ; renvoi IR et caisses |
| LF 2019, art. 87-88 (1 % au profit des caisses) ; LF 2020, art. 39 § 5 (abrogation) | texte AR ; abrogation non relue ici | hors sujet (livre des caisses) ; renvoi d'une phrase, et rien sur l'abrogation tant qu'elle n'est pas relue |
| LF 2024, art. 64 | texte AR | étape (de 2018) — reprise |
| LF 2025, art. 38 | texte AR | **rupture** 2025 (naissance d'un dispositif) |
| LF 2026 (loi n° 2025-17) | texte AR | constat pour l'état du droit (aucune reconduction) ; RECHERCHE |
| Tableaux « A » : LFC 2014, LF 2015, LFC 2015, LFC 2016, LF 2017, LFC 2017, LFC 2018, LF 2019, LFC 2019 | texte (AR pour 2018, 2019) | longue période (prévisions) |
| Rapports d'exécution du budget à fin 2014 et à fin 2016 | texte AR | longue période (réalisations) |
| Note sur l'exécution provisoire à fin 2018 (« taux de 7 % », sans montant) | texte | non repris : pas de montant, et le taux écrit diffère de celui de la loi (7,5 %) → TODO |

### 1.6 Désaccords de classement à trancher (A)

1. **2024 : étape ou rupture ?** Même public, même assiette que 2018, mais un nouveau texte après quatre ans sans prélèvement, et la seule rubrique relevée (« soutien des équilibres des finances publiques »). Retenu : étape de 2018. Autre lecture : sixième grande réforme.
2. **2012 : contribution volontaire.** C'est un dispositif nouveau, mais non obligatoire. Retenu : ligne de registre et une phrase d'entre-temps, pas une réforme. Autre lecture : fiche à part.
3. **Les variantes ciblées comme dispositifs secondaires.** Autre découpage défendable : trois épisodes généraux (1991, 2014, 2017) en épine, et les prélèvements sectoriels de 2018, 2024 et 2025 regroupés dans **une** fiche « prélèvements sur les banques et les grandes entreprises ». Retenu : deux fiches, parce que 2025 vise un public nouveau (taille de l'entreprise), pas un secteur.
4. **1991 comme mise en place.** Elle suppose que 1973-1988 ne forment pas le même dispositif. Ces contributions alimentent un fonds (1973, 1988) ou la Caisse (1989), quand celle de 1991 va au budget : le motif tient pour 1973 et 1988, qui sont lus ou connus par leur intitulé, mais les autres ne sont pas lus.

---

## 2. Chapitre B — Les taxes au profit des fonds spéciaux du Trésor

### 2.1 Frontière

- **Règles de base** : la taxe au profit du fonds de développement de la compétitivité (FODEC), seule taxe de la famille qui couvre plusieurs secteurs. Son champ (liste de produits, puis services), son assiette (chiffre d'affaires hors TVA des fabricants et prestataires, valeur en douane), son taux (1 %), ses exonérations et l'objet du fonds suivent tout le chapitre.
- **Dispositifs** : les taxes au profit d'autres fonds, chacune limitée à un secteur ou à un objet :
  - compétitivité de l'agriculture et de la pêche (1996, 2000) ;
  - compétitivité du tourisme (1996) ;
  - taxe pour la protection de l'environnement, au profit du fonds de dépollution (2003).
- **Inventaire** : les autres fonds alimentés par un prélèvement, logés ailleurs ou non documentés. Ils reçoivent une ligne et un lien.

### 2.2 Les grandes réformes (épine)

| Réforme, date d'effet | Texte et articles (lecture) | Ce que la loi cherche | Avant → après | Ce qui y naît |
|---|---|---|---|---|
| **Mise en place : 1er janvier 1995** | LF 1995, art. 37-44, p. 2045 ; art. 100, p. 2051 (texte) | missions du fonds, par la loi : qualité des produits industriels, restructuration industrielle, études sectorielles stratégiques, subventions aux centres techniques, « toutes autres actions visant à développer la compétitivité industrielle » (art. 37) ; rubrique **non relevée** (Q1) | trois cotisations professionnelles sectorielles (chaussures et cuir, 1956 ; textiles, 1958 ; matériaux de construction, céramique et verre, 1984) → réunies au profit d'un compte spécial du Trésor, plus une taxe nouvelle de 1 % sur les produits du tableau « L », locaux ou importés | le fonds et la taxe |
| **1996** | LF 1996, art. 58-60 et 64-65, p. 2374 (image) ; art. 68 (clause d'application, OCR) | **objet non relevé** (Q1) | aucune taxe de compétitivité hors industrie → taxe de 1 % du chiffre d'affaires des établissements touristiques et 1,700 D par mois et par siège des véhicules des agences « A » ; taxes de 2 % sur les fruits et légumes et sur le maïs et les tourteaux de soja | naissent les taxes au profit des fonds de compétitivité du tourisme et de l'agriculture et de la pêche ; ajustement de la taxe du FODEC (art. 61 : taxe sur les conserves ajoutée aux ressources) |
| **1er janvier 2000** | LF 2000, art. 36-39, pp. 2744-2745 (image) ; art. 73 (OCR) | **objet non relevé** (Q1) ; l'art. 39 étend les missions à la mise à niveau des services | une taxe sur la liste « L » et trois cotisations → une seule « taxe professionnelle due sur les produits locaux ou importés », liste **par décret** ; assiette **hors TVA** ; exportations exonérées ; anciens textes abrogés (art. 38) | étape de la fiche agricole (art. 35 : taxe de statistique sur les céréales affectée au fonds) |
| **2003 — provisoire** (tant que Q5 n'est pas levée) | LF 2003, art. 58-59, p. 2883 (couche décodée ; chiffres à relire, Q5) | **objet non relevé** (Q1) | → taxe pour la protection de l'environnement sur le chiffre d'affaires hors TVA des fabricants et la valeur en douane de matières plastiques, au profit du fonds de dépollution ; **taux et positions à relire à l'image avant d'être écrits** | naît la taxe pour la protection de l'environnement (fiche) |
| **1er janvier 2011** | LF 2011, art. 14-16, p. 3463 (texte) | **objet non relevé** (Q1) ; nouvelle mission : mise à niveau des services et de l'artisanat | produits seuls → **services et produits** ; prestataires de services redevables, 1 % de leur chiffre d'affaires hors TVA ; fonds renommé « … dans les secteurs industriel, de services et de l'artisanat » | rien |

Contexte : non relevé. La note cite comme « pistes » le programme de mise à niveau et l'accord
d'association de 1995. **Rien n'est écrit** tant qu'aucune source de l'époque n'est lue (Q2).

**Entre-temps.**
- 1995-2000 : décret d'organisation de 1995 (intitulé seul : TODO) ; ajustement de 1996.
- 2000-2011 : liste de 2000 et décret de 2008 (intitulés seuls) ; une phrase signale 2003 côté fiches.
- Depuis 2011 : liste de 2012 (intitulé seul) ; exonération des produits de protection individuelle (LF 2022, art. 63 § 3) ; exonération des préservatifs importés par l'Office national de la famille et de la population (LF 2025, art. 29).

### 2.3 Plan, section par section

`# Les taxes au profit des fonds spéciaux du Trésor {#sec-taxes-fonds-speciaux .domicile-unique}`
Une phrase d'objet : un prélèvement dont le produit va à un compte spécial du Trésor, et non au
budget général.

**`## Vue d'ensemble {#sec-fst-vue-ensemble}`**
- Établit :
  - ce qu'est un [fonds spécial du Trésor](#g-fonds-special-tresor) ;
  - la taxe principale (1 % du chiffre d'affaires hors TVA des fabricants et des prestataires, et de la valeur en douane), avec le nom long du fonds avant le sigle (le sigle n'est pas écrit dans les lois lues, note, § 10) ;
  - les taxes sœurs.
- Premier plan : **inventaire court** `{#tbl-fst-inventaire}` — fonds | ce qui l'alimente | où lire. Lignes :
  - le FODEC et les trois fiches de ce chapitre ;
  - FOPROLOS et TFP (cotisations) ; FNE (marché du travail) ; Fonds de transition énergétique (compensation) ; Fonds de protection des zones touristiques (finances locales) ; Caisse générale de compensation (volume IX) ;
  - Fonds de soutien de la délimitation du patrimoine foncier : contribution aux frais d'immatriculation foncière (LF 2000, art. 40), ligne au registre replié des « autres taxes ».

  Sans citation de loi dans la cellule : liens vers les sections et les registres.
- Une phrase sur le FOPRODI : dotation budgétaire et non taxe (`_regimes_incitation.qmd`).
- Une phrase sur l'assiette : la taxe du FODEC n'entre pas dans celle du droit de consommation, ni l'inverse, et toutes deux entrent dans celle de la TVA (lien `@tbl-dc-cascade`).
- Renvois en tête : contributions conjoncturelles (`@sec-contributions-conjoncturelles`, budget général) ; taxe de circulation (chapitre du timbre, budget général).
- Ordre de grandeur : renvoi à la série de `@sec-fst-longue-periode`, sans chiffre isolé.
- Replié : `titre="Les comptes spéciaux du Trésor de la loi de finances complémentaire pour 2014 : liste complète"` — les noms du tableau « B », p. 2114, avec la ressource quand un texte lu l'établit, case vide sinon. L'état de lecture va en TODO, pas dans la cellule.

**`## La mise en place, 1995 {#sec-fst-mise-en-place}`**
- `### Ce que la taxe remplace : trois cotisations professionnelles {#sec-fst-antecedents}` — d'après la LF 1995, art. 38 et 42-43 :
  - la cotisation sur les chaussures (décret du 20 septembre 1956, caisse inter-professionnelle de compensation des chaussures), étendue aux articles en cuir ;
  - la cotisation sur les textiles (loi n° 58-79) ;
  - la taxe sur les matériaux de construction, la céramique et le verre (LF 1985, art. 31), étendue au tableau « M ».

  Le rendu dit ce que la loi de 1995 reprend (ces trois ressources) et ce qu'elle ajoute (une taxe générale sur une liste). Les textes d'origine se lisent après OCR : TODO, et rien sur leurs taux.
- `### La loi de finances pour 1995 {#sec-fst-1995}` — missions (art. 37, mots de la loi) ; ordonnateur ; taxe (art. 40-41) ; perception à la douane et, en régime intérieur, déclaration mensuelle aux délais de la TVA ; effet au 1er janvier 1995. Décret d'organisation n° 95-2495 : TODO (intitulé seul).

**`## Les grandes réformes {#sec-fst-reformes}`**
- Premier plan : tableau des réformes `{#tbl-fst-reformes}` (1996, 2000, 2003, 2011), sur le modèle de la TVA.
- `### 1996 : le même instrument pour l'agriculture, la pêche et le tourisme {#sec-fst-reforme-1996}` — naissances en deux ou trois phrases chacune, renvoi aux fiches ; ajustement FODEC (art. 61) en une proposition.
- `### 2000 : une seule taxe, une liste fixée par décret {#sec-fst-reforme-2000}` — l'unification et les abrogations ; l'assiette hors TVA ; l'exonération des exportations et les achats en suspension pour les exportateurs non assujettis ; la mission « services ». Une phrase : la même loi affecte au fonds agricole la taxe de statistique sur les céréales (fiche). Le décret de liste n° 2000-634 est lisible au corpus mais non lu : rien sur son contenu (Q4).
- `### 2003 : une taxe pour la dépollution {#sec-fst-reforme-2003}` — naissance, renvoi à `@sec-fst-tpe`. **Provisoire** : une lecture que la note dit à relire ne porte pas une rupture. Tant que Q5 n'est pas levée, cette sous-section et la fiche de la taxe ne s'écrivent pas, ou s'écrivent sans taux ni positions. L'épine tient sans elle (1995, puis 1996, 2000, 2011).
- `### 2011 : les services et l'artisanat {#sec-fst-reforme-2011}` — redevables nouveaux ; nouveau nom ; nouvelle mission. Phrase d'entre-temps depuis 2011 (§ 2.2).
- `### Le détail, texte par texte {#sec-fst-textes}` — replié : `titre="La taxe au profit du fonds de développement de la compétitivité, texte par texte, 1995-2025"`. Colonnes : date d'effet, portée, texte et article, avant → après. Lignes :
  - LF 1995, art. 37-41 (rupture) ;
  - art. 38 et 42-43 (point de départ : ressources reprises) ;
  - LF 1996, art. 61 (ajustement) ;
  - LF 2000, art. 36-39 (rupture) ;
  - LF 2011, art. 14-16 (rupture) ;
  - LF 2022, art. 63 § 3 (ajustement) ;
  - LF 2025, art. 29 (ajustement).

  Les décrets n° 95-2495, 97-2126, 99-2741 et modificatifs, 2000-634, 2008-4111 et 2012-435 n'ont **pas de ligne** tant qu'ils ne sont pas lus : TODO.

**`## L'état du droit en 2026 {#sec-fst-etat-du-droit}`**
- Établit, au 1er janvier 2026 :
  - la taxe est due sur les produits importés ou fabriqués localement et sur les services d'une liste fixée par décret ;
  - taux de 1 % du chiffre d'affaires hors TVA (fabricants, prestataires) ou de la valeur en douane ;
  - exportations exonérées ; exonérations de 2022 et 2025.
- Motif pour l'écrire : la LF 2011 récrit entièrement la taxe, et les lois de finances 2012-2026 ont été parcourues (note, § 3.2). Un modificatif des années 2001-2010 serait donc sans effet sur l'état présent. Le contenu de la liste reste à lire (Q4) : TODO, rien d'écrit sur la liste.
- Colonne « population couverte » : **requise** (la taxe est en vigueur) ; présente, vide, avec un `<!-- TODO (documentaliste) -->` en attendant Q9.

**`## Les autres taxes au profit d'un fonds {#sec-fst-dispositifs}`** — chaque section situe son dispositif (« née de la réforme de… »), le définit, puis suit son évolution.
- `### Le fonds de développement de la compétitivité dans le secteur de l'agriculture et de la pêche {#sec-fst-agriculture}` — naissance (1996, art. 64-65 : 2 % sur les fruits et légumes, à l'importation et à la production hors exportation ; 2 % sur le maïs et les tourteaux de soja) ; étape 2000 (art. 35, taxe de statistique sur les céréales). La taxe sur la tomate de transformation (décret n° 2001-1586) n'est connue que par sa notice : TODO. Replié : registre de trois lignes.
- `### Le fonds de développement de la compétitivité dans le secteur du tourisme {#sec-fst-tourisme}` — naissance (1996, art. 58-60). Les modifications de la LF 2007 (art. 60) et de la LF 2011 (art. 17-18) ne sont connues que par leur notice : TODO, et l'état du droit de cette taxe n'est **pas** écrit (Q6). Replié : une ligne.
- `### La taxe pour la protection de l'environnement {#sec-fst-tpe}` — **provisoire jusqu'à Q5**, aucun chiffre visible avant la relecture à l'image. Le fonds de dépollution est antérieur (LF 1993, art. 35-37, notice seule : TODO) ; naissance de la taxe (2003, art. 58-59). Une seule extension du champ est lue (LF 2013, art. 68) ; les autres (LF 2005, 2008, 2010, 2014, 2016, 2018) ne sont connues que par la liste de la note : TODO, et pas d'état du droit (Q6). Replié : `titre="La taxe pour la protection de l'environnement, texte par texte, 2003-2013"`.
- Un `:::: {.chronologie-repliable titre="Les autres taxes au profit d'un fonds spécial : textes lus"}` porte, dans la même section, la contribution aux frais d'immatriculation foncière (LF 2000, art. 40, récrivant l'art. 15 du décret-loi n° 64-3 : 20 millimes par m² en zone d'aménagement urbain, 10 D par hectare ailleurs). Le FTE (LFC 2014, art. 3) n'y figure pas : sa ligne doit être versée au volume IX (§ 3).

**`## La longue période : ce que pèsent les fonds spéciaux {#sec-fst-longue-periode}`** — budgétaire seul.
- `### La ligne « Fonds spéciaux de Trésor » des recettes fiscales, 1991-2025 {#sec-fst-serie}`
  - Premier plan, dans l'immédiat : **tableau écrit à la main** `{#tbl-fst-serie}`, en millions de dinars (note, § 6), source `@minfin-recettes-fiscales` (type `dataset`, citation permise dans la prose), avec `<!-- TODO (rédacteur) : remplacer par une figure tirée de figtools.series() quand la colonne existera — voir § 4 -->`.
  - Précautions écrites sous le tableau, pas repliées :
    - 1986-1990 sans sous-ligne ;
    - 2000 case vide ;
    - 2014-2015 : chute contre les prévisions, quand « Autres » bondit ; cause non écrite dans le classeur, et le rédacteur n'en propose aucune ;
    - 2022 : saut non expliqué, à ne pas attribuer à la CSS (rangée en impôt direct par la LF 2019, tableau « A ») ;
    - 2025 égal à la prévision de la LF 2025 ;
    - la ligne agrège tous les fonds et ne mesure aucun dispositif.
  - La hausse de 1995 coïncide avec la création du FODEC et de ses ressources : le dire comme une coïncidence de dates, sans attribution.
  - Pas de ratio au PIB écrit à la main. Une part des recettes fiscales et un ratio au PIB viendront avec la figure (PIB `pib_minfin_MDT`, segments de base, renvoi à `precis/fr/annexe-pib.qmd`).
- `### Les prévisions du fonds de développement de la compétitivité, 1995-2020 {#sec-fst-fodec-previsions}`
  - Premier plan : tableau court (tableau « B » des lois de finances, en millions de dinars) : 1995 : 20,0 ; 1997 : 26,0 ; 2005 : 45,0 ; LFC 2008 : 67,0 ; 2011 : 71,0 ; 2012 : 74,0 ; 2013 : 74,0 ; LFC 2013 : 58,0 ; 2014 : 65,0 ; LFC 2014 : inchangé ; 2015 : 75,0 ; 2016 : 55,0 ; 2017 : 74,0 ; LFC 2017 : 68,0 ; 2018 : 74,0 ; 2019 : 74,0 ; 2020 : 73,0 ; LFC 2020 : 73,0.
  - Pages : `docs/notes/fiscalite-incitations-second-passage-2026-10-13.md`, § 2.3, et note, § 3.3. Liens de la colonne « Loi » vers un registre replié `titre="Les prévisions du fonds dans les tableaux « B » des lois de finances : lignes et pages, 1995-2020"`.
  - Phrase : ce sont des prévisions. TODO (non rendus) pour les réalisations et pour les tableaux 2021-2026.
- Les chiffres du PEFA, du FMI et de la Cour des comptes **ne viennent pas ici** : ils vont dans la section suivante.

**`## Ce qu'en dit l'économie {#sec-fst-economie}`** — dernière section, tirée de
`docs/notes/eco-taxes-affectees.md`, gabarit fixe, une page au plus :
- la question (affectation, principe du bénéfice, fongibilité, rigidité, durée, contrôle) ;
- la théorie (McCleary ; Cashin et al.) ;
- l'empirique international (fonds routiers, prolifération, fongibilité, Francis et Moore) ;
- puis la Tunisie : Assises 2014, PEFA 2016 (31 FST, 1,16 milliard de dinars en 2013, cité comme tel, avec la méthode du PEFA), Cour des comptes (soldes du FOPROLOS), FMI (CR 15/285 et 16/138, ex ante, méthode non décrite) ;
- ce que le praticien retient ;
- « Littérature arrêtée au mois d'octobre 2026 ».

Aucun de ces chiffres n'entre dans `tbl-fst-serie`. Le PEFA ne se rapproche pas en silence de la
série du classeur, qui donne 1 228,5 MD pour 2013 : si on les met en regard, c'est sur un
graphique, familles distinguées (règle d'AGENTS.md) ; sinon, on n'en dit rien.

### 2.4 Ruptures propres aux dispositifs

- Agriculture et pêche : naissance (1996) ; étape (2000, céréales).
- Tourisme : naissance (1996) ; suite non établie.
- Protection de l'environnement : naissance (2003) ; étape (2013, extension du champ) ; le reste n'est pas lu.

### 2.5 Registre de classement des textes (chapitre B)

| Texte | Lecture | Classement |
|---|---|---|
| décret du 20 septembre 1956, art. 2 ; loi n° 58-79, art. 2 ; LF 1985, art. 31-33 | cités par la LF 1995 ; originaux non lus (OCR) | antécédents de la mise en place (par la LF 1995) |
| LF 1993, art. 35-37 (fonds de dépollution) | métadonnées | antécédent de la fiche environnement ; intitulé seul → TODO |
| LF 1995, art. 37-44, 100 | texte | **rupture** — mise en place |
| décret n° 95-2495 ; n° 97-2126 | métadonnées | organisation ; intitulé seul → TODO |
| LF 1996, art. 58-60 | image | **rupture** (naissance, tourisme) — grande réforme 1996 |
| LF 1996, art. 61 | image | ajustement (FODEC) |
| LF 1996, art. 64-65 | image | **rupture** (naissance, agriculture) — grande réforme 1996 |
| LF 1996, art. 68 | OCR | clause de date, à relire (Q5) |
| décret n° 99-2741 et modificatifs (2005-2556, 2006-1703, 2007-313, 2008-2404) | métadonnées | organisation ; intitulé seul → TODO |
| LF 2000, art. 35 | image | étape (agriculture) |
| LF 2000, art. 36-39 | image | **rupture** 2000 (désaccord, § 2.6) |
| LF 2000, art. 40 | image | inventaire (contribution foncière) |
| LF 2000, art. 58 | image | vignette → passation (§ 5) |
| LF 2000, art. 73 | OCR | clause de date, à relire (Q5) |
| décret n° 2000-634 | lisible, non lu | étape de 2000 (liste) ; pas de ligne avant lecture (Q4) |
| décret n° 2001-1586 (tomate) | métadonnées | fiche agriculture ; intitulé seul → TODO |
| LF 2003, art. 58-59 | couche décodée, à relire | rupture **provisoire** 2003 : ne porte une rupture qu'après relecture à l'image (Q5) |
| LF 2005, art. 67-68 ; LF 2008, art. 31 ; LF 2010, art. 37 ; LF 2014, art. 71 ; LF 2016, art. 88 ; LF 2018, art. 23-24 | liste de la note, non lus | étapes probables (environnement) → TODO (Q6) |
| LF 2007, art. 60 ; LF 2011, art. 17-18 (tourisme) | métadonnées | fiche tourisme → TODO (Q6) |
| décret n° 2008-4111 | métadonnées | ajustement (liste) ; intitulé seul → TODO |
| LF 2011, art. 14-16 | texte | **rupture** 2011 |
| décret n° 2012-435 | métadonnées ; AR à l'image | étape de 2011 (liste) probable ; pas de ligne (Q4) |
| LF 2013, art. 68 | texte | étape (environnement) |
| LF 2014, art. 67 ; LFC 2014, art. 3 (FTE) | texte | hors sujet (volume IX) ; inventaire et renvoi |
| LF 2022, art. 63 § 3 | texte | ajustement (exonération) |
| LF 2025, art. 29 | texte AR | ajustement (exonération) |
| tableaux « B » 1995-2020 | texte, image | longue période (prévisions) |
| classeur « recettes fiscales », ligne FST | données | longue période (réalisations) |

### 2.6 Désaccords et risques (B)

1. **2000 : rupture ou étape ?** Lecture retenue : rupture. L'instrument est refondu (une seule taxe, liste par décret, abrogation des anciennes cotisations) et le fonds reçoit un objectif nouveau (services). Autre lecture : simplification de 1995, donc étape. Les deux se défendent.
2. **1996 et 2003 comme grandes réformes.** Ces lois ne touchent pas la taxe du FODEC (sauf un ajustement en 1996), mais elles font naître des dispositifs du chapitre : la consigne en fait de grandes réformes. Autre lecture : trois réformes seulement (1995, 2000, 2011), et des fiches indépendantes. Mais alors le chapitre regrouperait plusieurs dispositifs sans épine commune.
3. **Risque du repli** : les décrets de liste ne sont pas lus. Le chapitre ne doit pas laisser croire que la liste est connue ; l'état du droit dit « une liste fixée par décret » et s'arrête là.
4. **Risque de confusion** entre la ligne FST (tous les fonds, TFP et FOPROLOS compris) et le FODEC : la précaution doit rester au premier plan, sous le tableau.

---

## 2bis. Ancres de registre (sections `.domicile-unique`)

Les deux chapitres portent `.domicile-unique` sur leur titre de niveau 1, comme la TVA. Deux
règles de `scripts/check_domicile_references.py` : (1) dans ces sections, aucune clé de type
`legislation` n'est citée hors d'un bloc `.chronologie-repliable` (le texte nomme le texte et lie
ce nom à `[…](#r-…)`) ; (2) toute ancre `[]{#r-…}` est dans un bloc replié, sur une ligne qui cite
au moins une référence, et tout lien `#r-…` a son ancre dans le même fichier. Les sources non
législatives (`minfin-recettes-fiscales`, rapports d'exécution, études) se citent sur place.

**Chapitre A (`r-ccj-`)**
- Dates : `r-ccj-dates-1991`, `r-ccj-dates-2014`, `r-ccj-dates-2017`, `r-ccj-dates-2018`, `r-ccj-dates-2024`, `r-ccj-dates-2025`.
- Règles de base : `r-ccj-1973`, `r-ccj-1991`, `r-ccj-2012`, `r-ccj-2014`, `r-ccj-2015`, `r-ccj-2017` ; barèmes repliés : `r-ccj-2014-bareme`, `r-ccj-2017-bareme`.
- Dispositifs : `r-ccj-1991-importation` ; `r-ccj-banques-2018`, `r-ccj-banques-2024` ; `r-ccj-grandes-entreprises-2025`.
- Prévisions : `r-ccj-prev-lfc2014`, `-lf2015`, `-lfc2015`, `-lfc2016`, `-lf2017`, `-lfc2017`, `-lfc2018`, `-lf2019`, `-lfc2019`.
- Renvois vers d'autres livres (CSS, 1989, redevance, 1 % de 2019) : liens de section, pas d'ancre `r-`.

**Chapitre B (`r-fst-`)**
- Taxe principale : `r-fst-1995`, `r-fst-1995-ressources`, `r-fst-1995-dates`, `r-fst-1996`, `r-fst-1996-dates`, `r-fst-2000`, `r-fst-2000-dates`, `r-fst-2011`, `r-fst-2022`, `r-fst-2025`.
- Fiches : `r-fst-agri-1996`, `r-fst-agri-2000` ; `r-fst-tourisme-1996` ; `r-fst-tpe-2003`, `r-fst-tpe-2013` (provisoires, Q5) ; `r-fst-foncier-2000`.
- Prévisions : `r-fst-prev-1995` … `r-fst-prev-lfc2020`, une par loi.
- Liste repliée des comptes de 2014 : `r-fst-comptes-2014` (une ligne qui cite la LFC 2014, tableau « B », p. 2114).

Un texte qui sert deux registres (LF 1996, LF 2000) a une ligne dans chacun ; le lien de la prose
va au registre du dispositif dont parle la phrase.

## 3. Corrections et renvois dans les chapitres existants

| Fichier, lieu | Changement | Source |
|---|---|---|
| `_impot_revenu.qmd`, callout « Deux articles de la même loi », l. 727-729 (section `sec-irpp-minimum`, hors `.domicile-unique` : citations en ligne permises) | Récrire : « contribution conjoncturelle exceptionnelle au profit du budget de l'État », **instituée par l'article 28** pour l'année 2014, **l'article 29 en fixe les taux**. L'article 29 prend pour assiette 50 % du minimum d'impôt des personnes physiques (art. 44 § II) **et** celui des sociétés (art. 49 § II). Citation `[@lfc-2014, art. 28 et 29, p. 2103]`. Ajouter le renvoi `@sec-ccj-reforme-2014`. Une phrase facultative : la contribution de 2017 prend aussi 50 % du minimum pour assiette (LF 2017, art. 48-49), sans modifier le minimum non plus. | note, § 2.1 et § 2.4 |
| `_impot_revenu.qmd`, note de lecture de `fig-irpp-rendement` | Une phrase : l'exercice 2014 comprend 39 MD encaissés au titre de la contribution (rapport d'exécution à fin 2014, p. 7). | note, § 2.2 ; clé à créer (Q10) |
| `_impot_societes.qmd`, tête de « L'évolution, réforme par réforme » (l. 121) | Une phrase et un lien : les sociétés sont les principales redevables des contributions de 2014 et 2017 et seules redevables des prélèvements de 2018-2019, 2024-2025 et 2025 ; renvoi `@sec-contributions-conjoncturelles`. Pas de prose recopiée. | note, § 2.4 |
| `_impot_societes.qmd`, « 2014 — abaisser à 25 % » (l. 155) | Callout jumeau de celui de l'IR : l'article 29 de la LFC 2014 prend pour assiette 50 % du minimum de l'art. 49 § II, sans le modifier ; renvoi à `@sec-ccj-reforme-2014`. | note, § 2.1 |
| `_impot_societes.qmd`, « 2018 » (l. 171) et « 2024 » (l. 205) | Une proposition chacune, avec un lien vers `@sec-ccj-banques` (2018 ; 2024-2025) et `@sec-ccj-grandes-entreprises` (2025). | note, § 2.1 |
| `_impot_societes.qmd`, note de lecture de `fig-impot-societes-rendement` | Une phrase : l'exercice 2014 comprend 147 MD d'IS encaissés au titre de la contribution (57 MD des sociétés pétrolières, 90 MD des autres), et l'exercice 2015, 75 MD (rapports d'exécution). | note, § 2.2 ; Q10 |
| `index.qmd` | (a) Dans le paragraphe « Le livre suit ce partage », une phrase pour chacun des deux chapitres. (b) La note de `fig-recettes-composition` (l. 45) : renvoi à `@sec-fst-serie` pour la sous-ligne des fonds spéciaux. (c) Le tableau `tbl-fisc-carte` reste celui des « cinq impôts » : ne pas y ajouter les contributions, qui n'ont pas de texte fondateur unique. (d) Si la présentation passe au tableau de voisinage (convention § 4), y mettre la contribution de 1 % de 2019 (caisses) et la taxe au profit du FTE (compensation). | — |
| `compensation/_electricite_gaz.qmd` | Hors de ce chantier : signaler au backlog du volume IX que la LFC 2014, art. 3 (FTE à la place du Fonds national de maîtrise de l'énergie) n'y est pas cité. | note, § 5 et § 7 |
| `caisses/` | Hors de ce chantier : backlog du livre des caisses, contribution de 1 % de 2019 (LF 2019, art. 87-88, AR p. 5468) sans domicile. | note, § 2.3 |
| `docs/notes/backlog-precis.md` | Item 10 de « Manques du précis » : le rédacteur le clôt en renvoyant aux deux chapitres et inscrit les lacunes restantes (§ 6). | — |

## 4. Figures et tableaux attendus

| Objet | Source | État |
|---|---|---|
| `tbl-ccj-episodes`, `tbl-ccj-reformes`, barèmes 2014 et 2017 repliés | note, § 2.1 | faisable maintenant (écrit à la main ; pas de paramètre du modèle à engendrer : aucun n'existe pour ces contributions) |
| `tbl-ccj-previsions` (prévisions et deux réalisations) | tableaux « A » (note, § 2.2) ; rapports d'exécution | faisable maintenant ; réalisations 2017 et suivantes à obtenir (lois de règlement) |
| **Figure de la série « Fonds spéciaux de Trésor », 1991-2025** (millions de dinars et part des recettes fiscales ; 2000 vide ; ruptures 2014-2015 et 2022 annotées ; 2025 marqué comme prévision ; marques des grandes réformes de 1995, 2000, 2011) | `tunisia-data/data/raw/minfinances/recettes_fiscales.xls`, rubrique 2.4 | **après un travail de données**. La série n'existe ni dans l'entrepôt ni dans `precis/_seriescache/` : `recettes-fiscales-composition` ne porte que `autres_indirects_MDT` (FST + fonds de concours + reliquat), contrôlé le 23/10/2026. À faire dans `tunisia-data` : ajouter `fonds_speciaux_tresor_MDT`, `fonds_concours_MDT` et `autres_reliquat_MDT` au build `tunisia_data/build/irpp.py` (sortie `recettes_fiscales_composition_1986_2025.csv`) ou créer une série `recettes-fiscales-fonds-speciaux`, avec les précautions dans la fiche `sources/minfinances-recettes-fiscales.md`. Puis régénérer le snapshot et écrire un module `precis/fr/fiscalite/figures/taxes_fonds_speciaux.py` qui lit `figtools.series()`. D'ici là : `tbl-fst-serie` écrit à la main, avec TODO |
| `tbl-fst-fodec-previsions` | tableaux « B » 1995-2020 | faisable maintenant (à la main) ; 2021-2026 : tableaux à lire à l'image ou annexes par mission ; une série `jort-lf-fonds-speciaux` dans `tunisia-data` sur le modèle de `jort-lf-caisse-transports-routiers` serait la voie durable (backlog) |
| `tbl-fst-inventaire` et liste repliée des comptes de 2014 | note, § 5 ; tableau « B » LFC 2014 | faisable maintenant |
| Frise de tête (A et B) | — | facultative, après les deux chapitres ; la frise commune du livre (convention § 4) les portera |

## 5. Bloc de passation : la taxe de circulation (pour le chantier « timbre et enregistrement »)

À remettre au propriétaire de `precis-wt-fiscalite-timbre-enregistrement`, qui décide. Ce
chantier n'écrit rien sur la vignette.

- **Nature** : recette du budget général (« Droits sur les transports et autres produits », ligne 25-02, puis 16-02 en 2020) ; terme du texte : « taxe de circulation sur les véhicules automobiles », et « vignette » pour l'usage ; glossaire `taxe-circulation` déjà versé. À distinguer de la taxe unique de compensation des transports routiers (volume IX) et de la redevance de compensation sur les voitures (volume IX).
- **Antécédent** : art. 19-21 du décret du 31 mars 1955 (clé `decret-1955-03-31-budget`), hors corpus : **à obtenir**. Tant qu'il ne l'est pas, la mise en place ne s'écrit pas.
- **Ruptures** : aucune ne peut être établie aujourd'hui. Les textes qui la porteraient (LF 1964, art. 9-10 ; LF 1983, art. 73-76, rubrique « réforme fiscale, impôts indirects » d'après l'intitulé ; LF 1994, art. 48-49) sont connus par leur intitulé ou un OCR partiel. Les textes lus ne règlent que des tarifs, des exonérations ou le recouvrement : ce sont des ajustements.
- **Tarif lu** : voitures de tourisme et motocycles, LF 2000, art. 58 (image) → DL 2021-21, art. 55 (texte), plus motocycles de plus de 125 cm³ à 250 D par la LF 2016, art. 90 (image). **Piège** : le tableau de la LF 2016 imprime des tirets sur toutes les autres lignes ; le tarif de 2000 ne doit pas être présenté comme établi jusqu'en 2021 sans le dire (note, § 4.2).
- **Autres textes lus** : LF 2013, art. 67 (leasing, taxis et louages) ; LF 2024, art. 58 § 4, et LF 2026, art. 99 (abandon des taxes de 2020-2022 et de 2022-2024 sous condition de paiement des années suivantes).
- **Prévisions** du tableau « A », 2013-2020 (note, § 4.4) ; réalisations non isolées dans le classeur.

## 6. Questions au documentaliste

- **Q1. Rubriques, mot pour mot** (et, pour la LFC 2014 et la LF 2025, si le nom du prélèvement est un intitulé d'article ou seulement le nom employé dans le texte), sous lesquelles sont rangés : LFC 1991, art. 2-7 ; LFC 2014, art. 28-31 ; LF 2015, art. 26 ; LF 2017, art. 48-51 ; LF 2018, art. 52 ; LF 2025, art. 38 (édition arabe) ; LF 1995, art. 37-44 ; LF 1996, art. 58-65 ; LF 2000, art. 35-40 ; LF 2003, art. 58-59 ; LF 2011, art. 14-16. Aucune ne figure dans la note, sauf la LF 2024, art. 64. Sans elles, « ce que la loi cherche » reste vide pour onze réformes sur douze.
- **Q2. Contexte, dans les mots des sources de l'époque** : exposés des motifs ou débats des LFC 1991, LFC 2014, LF 2017, LF 2018, LF 2025 ; pour le FODEC, exposé des motifs de la LF 1995 et texte du IXe Plan sur la mise à niveau. Rien ne s'écrit sans eux.
- **Q3. Antécédents des contributions** (OCR) : loi n° 59-42, art. 10 ; LF 1975-1986 (reconductions) ; LFC 1984, art. 3 ; loi n° 85-89 ; LF 1983, art. 82-84 ; LF 1988, art. 68. Ils décideraient si 1991 est bien une mise en place ou la reprise d'une famille (désaccord A4).
- **Q4. Listes du FODEC** : décret n° 2000-634 (lisible au corpus), n° 2008-4111, n° 2012-435 (arabe, à l'image). Il faut au moins savoir si le décret de 2012 porte la liste des services ouverte par la LF 2011.
- **Q5. Relectures à l'image** : LF 2003, art. 58-59 (taux de 2,5 %, positions 39-01 à 39-14) avant toute publication ; articles d'application LF 1996, art. 68, et LF 2000, art. 73.
- **Q6. Suites des fiches** : LF 2007, art. 60, et LF 2011, art. 17-18 (tourisme) ; LF 2005, 2008, 2010, 2014, 2016, 2018 (taxe pour la protection de l'environnement). Sans elles, ni l'état du droit ni l'évolution de ces deux taxes ne s'écrivent.
- **Q7. Lois de finances 2001-2010** en plein texte pour la taxe du FODEC : contrôle de cohérence seulement, car l'état du droit tient par la LF 2011.
- **Q8. Taxe conjoncturelle sur le ciment** (décrets n° 2002-318 et 2003-1539) : objet et domicile, prix administré (volume IX) ou taxe au profit d'un fonds ?
- **Q9. Population couverte** : nombre de redevables par contribution (2014 : salariés et retraités au-dessus de 12 000 D ; 2025 : entreprises au-dessus de 20 MD) et assujettis à la taxe du FODEC. Une source existe-t-elle ? Sinon, la colonne est déclarée sans objet ou vide, au choix du propriétaire.
- **Q10. Bibliographe** : créer `minfin-execution-2014-12` et `minfin-execution-2016-12` (rapports semestriels d'exécution, catalogue `tunisia-data`), dans les deux `references.json`. Contrôler l'URL de `fmi-2016-cr16138` dans l'AR. Doublons signalés par la note : `lf-2019`/`loi2018-56-lf2019`, `lf-2022`/`dl2021-21-lf2022`.

## 7. Risques du plan, à faire trancher

1. **Les chapitres seront minces par endroits.** La plupart des « ce que la loi cherche » et tous les contextes sont en attente. Le rédacteur doit laisser des cellules vides ou des TODO, et ne pas remplir par l'interprétation. On peut aussi attendre Q1 avant d'écrire.
2. **Le registre des antécédents est presque vide** : un seul texte lu (1973). Risque : faire passer 1991 pour une invention.
3. **Contributions et IS** : les montants de 2014 et 2015 doivent apparaître une fois en entier, dans le chapitre A ; les chapitres de l'IR et de l'IS n'en reçoivent qu'une phrase dans une note de figure.
4. **Ordre de fusion** avec le chantier du timbre (`_quarto.yml`, `index.qmd`).
5. **Section économique du chapitre A** : elle reste vide tant que la fiche n'est pas faite. Le chapitre se clôt alors sur la longue période, ce qui est un écart à la convention, à accepter provisoirement ou à combler avant publication.

# Prestations sociales — conversion « ruptures au premier plan, détail replié » : fiche de plan de l'architecte

Rendue le 9 octobre 2026. Volume lu dans son état de `master` (`7a552fc`) :
`precis/fr/prestations_sociales/` — `index.qmd`, `_contributives.qmd`, `_prestations_familiales.qmd`,
`_autres_risques.qmd`, `_non_contributives.qmd`, `_matrice.qmd`, `_notations.qmd`, l'encadré engendré
`_encadre_caisses.qmd`, les treize tableaux engendrés de `tables/`, les deux modules de `figures/`.
Notes : `prestations-assistance.md`, `prestations-contributif.md`, `prestations-sociales-plan.md`,
`backlog-precis.md` (rubrique « Prestations sociales »), `backlog-modele.md`. Modèle lu en lecture
seule sur `origin/master` d'`openfisca-tunisia` (version 0.125 au `pyproject.toml`, dernière étiquette
0.124) ; dépôt de données lu sur `origin/main` de `tunisia-data`.

Aucun texte de loi n'a été relu : tout ce qui est classé ici vient des chapitres, des notes et des
notices des paramètres, avec leur degré de certitude. Les mots « cœur », « épine », « fiche » sont
des mots de travail ; ils ne paraissent dans aucun chapitre.

---

## 1. Le constat

### 1.1 Mesures de départ (à refaire sur une copie gardée hors du dépôt avant de convertir)

« Texte » = mots du `.qmd` une fois retirés les cellules Python et les commentaires HTML ; c'est la
mesure du premier plan, puisqu'aucun bloc n'est replié aujourd'hui. Les notes de lecture des figures
(dans les cellules Python) n'y sont pas : celle de `fig-cnss-allocations-familiales` fait à elle seule
environ 450 mots visibles.

| Chapitre | `wc -w` brut | Texte | dont tableaux faits main | Appels de citation | Clés distinctes | Ancres de glossaire | `TODO` | `RECHERCHE` | Tableaux engendrés (lignes) | Tableaux faits main (lignes) | Figures | Formules |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `index` | 1 482 | 1 400 | 482 | 35 | 23 | 11 | 0 | 0 | 0 | 1 (9) | 0 | 0 |
| `_contributives` | 392 | 392 | 0 | 7 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_prestations_familiales` | 4 183 | 3 261 | 135 | 56 | 19 | 4 | 3 | 2 | 4 (15) | 1 (6) | 1 | 1 encadré, 2 expressions |
| `_autres_risques` | 3 591 | 3 423 | 556 | 57 | 16 | 8 | 0 | 1 | 3 (8) | 4 (23) | 0 | 0 |
| `_non_contributives` | 5 539 | 4 965 | 653 | 61 | 29 | 7 | 5 | 1 | 5 (29) | 7 (31) | 1 | 0 |
| `_matrice` | 1 220 | 1 004 | 372 | 20 | 15 | 0 | 4 | 0 | 0 | 1 (9) | 0 | 0 |
| `_notations` | 152 | 152 | 101 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (7) | 0 | 0 |
| **Ensemble** | 16 559 | **14 597** | 2 299 | 236 | — | 31 | 12 | 4 | **12 (52)** | **15 (85)** | **2** | 1 |

Aucun bloc `.chronologie-repliable`, aucune section `.domicile-unique`, aucune ancre de registre
`#r-…` : les 236 appels de citation sont dans le fil des phrases ou dans les tableaux.

Mesure reproductible : retirer ```` ```{python}…``` ````, `<!-- … -->` et les blocs
`.chronologie-repliable`, puis compter les mots. C'est cette mesure que visent les cibles du § 3.

### 1.2 `index` (« Présentation », 1 400 mots)

- Sections : chapeau ; encadré « Quatre conventions de lecture » (≈ 330 mots) ; « Le plan du
  volume » ; « Le périmètre de l'assistance » ; « Les organismes » (encadré des caisses engendré,
  243 mots, plus un paragraphe sur la CNAM) ; « Deux axes de classement » (tableau de 9 lignes,
  482 mots, une vingtaine de citations de loi dans la colonne « Ouverture »).
- **Ce qui noie le lecteur.** Le volume s'ouvre sur des conventions de méthode avant de dire ce que
  sont les prestations, qui y a droit et ce qu'elles pèsent. Aucun montant, aucun effectif, aucune
  dépense : le lecteur ne sait pas, en sortant de l'index, que le transfert permanent est de 280 D
  par mois en 2026 ni qu'il est servi à quelque 337 000 bénéficiaires à la fin de 2023. Le tableau
  des deux axes est une table des matières déguisée, chargée de citations.
- **Contraire aux règles.** La convention n° 4 (« texte établi / référence / dérivé », « colonne
  d'attestation ») est du vocabulaire de dépouillement dans le texte visible. « Le périmètre de
  l'assistance » dit ce que le volume laisse dehors (« restent hors de son périmètre »). La
  convention n° 3 est une liste de lacunes, non une convention.
- **Périmé.** Rien de daté, sauf le renvoi à « la matrice, dernier chapitre » si l'ordre change (§ 2).

### 1.3 `_contributives` (392 mots)

- Une liste de six « maillons » (affiliation, régime, stage, assiette, fait générateur, service) et
  deux « traits de méthode ». Pas de titre de niveau 2, pas de tableau, pas de donnée.
- **Ce qui ne va pas.** Trop court pour un chapitre ; son contenu est le mode d'emploi de la matrice
  régime × prestation, qui est à l'autre bout du volume. Le point 3 jette des durées de stage sans
  vue d'ensemble (elles sont redonnées dans `_autres_risques`).

### 1.4 `_prestations_familiales` (3 261 mots, plus ≈ 450 de note de figure)

- Sections : guide de lecture ; « Les origines » (≈ 430 mots sur les dispositions transitoires de la
  loi n° 60-30, art. 121-131) ; « Le régime de la loi n° 60-30 » (sept alinéas titrés en gras,
  encadré de la formule) ; « Les réformes » (1976, 1986, 1989, 1996, au même rang) ; « La majoration
  pour salaire unique » ; « La contribution aux frais de crèche » ; « Longue période et données »
  (tableau `tbl-af-evolution`, figure de la dépense 1990-2004) ; « Le secteur public ».
- **Ce qui noie le lecteur.** (1) Le chapitre ne dit nulle part ce qu'une famille reçoit en dinars :
  la formule donne des taux et un plafond, jamais le maximum par enfant (18 % de 122 D, soit 21,960 D
  par trimestre pour le premier enfant, selon le plafond de 1986) ni ce qu'il vaut en dinars de 2025.
  (2) Quatre réformes sur le même plan : un relèvement de plafond (1986) a le même titre que la
  limitation à trois enfants (1989). (3) La naissance de deux dispositifs (1980, 1994) est hors de la
  chronologie. (4) « Les origines » détaille cinq articles transitoires que seul un spécialiste
  cherchera. (5) Le paragraphe « Trois conséquences » de la longue période répète les réformes.
  (6) Le secteur public vient après la longue période, comme un appendice. (7) La note de lecture de
  la figure porte la moitié du commentaire économique du chapitre.
- **Contraire aux règles.** « Le contenu du régime de 1944 […] n'est pas établi ici » et « La date
  d'effet de la loi n° 96-65 n'est pas établie ici » sont des constats à garder, avec une ancre
  `RECHERCHE` (ils n'en ont pas). « Présenter 1998… », « Une confusion de vocabulaire doit être
  écartée » : méta-discours à replier.
- **Périmé.** Rien dans les valeurs. Le guide de lecture annonce l'allocation familiale non
  contributive « créée en 2022 » : il faut y ajouter celle des 6-18 ans de 2025 (§ 3.5).

### 1.5 `_autres_risques` (3 423 mots)

- Sections : indemnités de maladie et de maternité (socle de 1960 ; congés de 2024) ; capital décès
  (privé ; public) ; accidents du travail (privé 1994 ; public 1995 ; travailleuses agricoles 2024) ;
  perte d'emploi (1996 ; fonds de 2025) ; assurance maladie (2004-2007 ; 2017).
- **Ce qui noie le lecteur.** (1) Cinq politiques sous un titre négatif (« autres »), sans vue
  d'ensemble : aucune phrase ne dit quels risques sont couverts depuis quand. (2) **Aucune figure,
  aucune dépense, aucun effectif**, alors que les comptes de la CNSS donnent, de 1990 à 2004, les
  indemnités de maladie, de couches et de décès, et de 1997 à 2004 les deux emplois de la protection
  des travailleurs licenciés (§ 5). (3) Des règles de procédure en rafale : délais de paiement,
  ordre des ayants droit, répartition du capital-décès entre conjoints, périodicité des versements.
  (4) L'ordre mêle le droit de 1960 et celui de 2024 dans chaque section, sans dire ce qui est en
  vigueur. (5) Les modifications de 1997 et 1998 sont glissées dans le « socle » de 1960.
- **Contraire aux règles.** « ce chapitre ne la tranche pas » (congés de 2024) ; « texte dont le
  contenu n'est établi ici qu'en partie » (loi n° 95-101) sans ancre ; « La citation repose sur
  l'édition arabe » dans le fil.
- **Périmé.** À vérifier par le documentaliste : le décret de gestion du fonds de l'article 17 de
  la loi de finances pour 2025 (fiche `r-lf2025-art17-decret`) ; la note datait le constat du
  8 septembre 2026.

### 1.6 `_non_contributives` (4 965 mots)

- Sections : « Comment l'assistance est attribuée » (cinq étapes) ; « Le PNAFN, de 1986 à l'AMEN
  social » (financement ; fournisseur de listes ; montant ; superposition) ; « L'aide médicale »
  (1987 ; AMG1 ; AMG2 ; modifications ; sortie du papier) ; « L'AMEN social » (loi organique ;
  éligibilité ; score ; transfert ; autonomisation) ; « Les allocations familiales non
  contributives » ; « Les aides ponctuelles » (occasionnelles ; exceptionnelles ; catégorielles) ;
  « Dispositifs adjacents ».
- **Ce qui noie le lecteur.** (1) Aucun effectif, aucune dépense : le chapitre le plus lourd
  budgétairement du volume n'a qu'une figure, celle du montant du PNAFN, arrêtée en 2018. (2) Le
  montant du transfert AMEN n'est donné qu'en tableau, jamais en figure ni en dinars constants, et
  jamais rapporté au salaire minimum qui commande pourtant le plafond de ressources. (3) La
  procédure tient une place considérable : un paragraphe de 130 mots sur le dépôt, l'enquête
  sociale, la commission, les délais ; la composition des commissions de 1988 et de 2012 ; les
  échéances de paiement de chaque aide ; les pièces de la demande « gluten ». (4) Les tarifs de
  1988-1991 et de 1998 (deux tableaux, quinze lignes) sont au premier plan. (5) L'ordre est par
  dispositif, pas par date : l'AMEN social, qui est l'état du droit, arrive après 2 000 mots.
  (6) Le chapitre commente sa propre chronologie (« Il faut en tirer une correction de
  chronologie », « Un point de vocabulaire d'abord, parce qu'il commande la chronologie »).
- **Contraire aux règles.** Colonne « Attestation : dérivé » et phrase « Toutes les lignes du
  tableau ci-dessous sont dérivées » ; « Le volume s'en tient à cette organisation juridique » ;
  « ne relèvent pas du périmètre de ce volume » ; « Ce chapitre ne tranche pas cette lecture » ;
  dans la note de la figure du PNAFN, « la date encodée du 1er avril 2018 » (vocabulaire du modèle).
- **Périmé** — voir le détail au § 3.5.1 : dates du 20 mai 2020, palier de 280 D absent, allocation
  des 6-18 ans absente, arrêté du 5 août 2026 absent, phrase sur la majoration pour handicap.

### 1.7 `_matrice` (1 004 mots) et `_notations` (152 mots)

- La matrice (9 régimes × 7 prestations) est le seul tableau du volume qui réponde à « qui a droit
  à quoi » ; elle est en dernier chapitre et précédée d'un encadré de convention. Cinq commentaires
  suivent, dont deux redisent les chapitres. Quatre `TODO` de fin de volume y sont entreposés (dont
  un pour le terminologue et un sur la pagination) : ils n'ont pas de rapport avec la matrice.
- Les notations : sept symboles, tous introduits dans la même section (`@sec-pf-loi-1960`) et déjà
  définis sous la formule.

---

## 2. La structure du volume

### 2.1 Les renvois entrants (relevé par `grep` sur tout `precis/fr/`)

| Cible | D'où | Nombre |
|---|---|---|
| `prestations_sociales/index.html` | `caisses/index.qmd`, `caisses/_comptes_regimes.qmd`, `caisses/_etat_caisses.qmd`, `compensation/index.qmd`, `index.qmd` du site | 5 |
| `_non_contributives.html#sec-prest-non-contributives` | `compensation/index.qmd` (2), `compensation/_incidence.qmd` (1) | 3 |
| `_autres_risques.html#sec-perte-emploi` | `marche_travail/index.qmd`, `marche_travail/_politiques_emploi.qmd` | 2 |
| `_matrice.html#sec-matrice-regimes` | `remunerations_publiques/index.qmd` | 1 |
| `prestations_sociales/references.json` | `cotisations_sociales/_accidents_travail.qmd` (mention) | 1 |

Les `@tbl-cnrps-maladie`, `@tbl-prevoyance-pensionnes` et `@tbl-perte-emploi` relevés dans
`cotisations_sociales/` sont les étiquettes propres de ce livre (les mêmes tableaux y sont émis) :
ils ne dépendent pas du volume des prestations.

Renvois internes au volume : `@sec-matrice-regimes` (3), `@sec-pf-loi-1960` (8, dont 7 dans les
notations), `@sec-pf-reformes` (2), `@tbl-af-evolution` (3), `@sec-prest-contributives` (1),
`@sec-prest-familiales` (1), `@sec-prest-autres-risques` (1), `@sec-prest-non-contributives` (1),
`@sec-af-non-contributive` (1), `@sec-perte-emploi` (1), `@sec-pf-origines`, `@sec-pf-secteur-public`,
`@sec-pf-longue-periode`, `@fig-cnss-allocations-familiales`, les trois `@tbl-` des cotisations.

### 2.2 Le découpage proposé

| # | Fichier | Titre proposé | Ce qui change |
|---|---|---|---|
| 1 | `index.qmd` | Présentation | resserré : ce que le volume couvre, une frise des naissances, un tableau court « qui, combien, financé par qui », les organismes |
| 2 | `_matrice.qmd` (**remonté en 2ᵉ position**, absorbe `_contributives.qmd`) | Qui est couvert : les régimes et les prestations | la matrice devient la vue d'ensemble de la couverture ; les six « maillons » en sont le mode de lecture |
| 3 | `_prestations_familiales.qmd` | Les prestations familiales | converti |
| 4 | `_autres_risques.qmd` | Maladie, maternité, décès, accidents du travail, perte d'emploi | un seul fichier, mais une chronologie des risques couverts puis une section par risque |
| 5 | `_non_contributives.qmd` | L'assistance sociale : du programme d'aide aux familles nécessiteuses à l'Amen social | converti ; l'état du droit avant les dispositifs anciens |
| — | `_contributives.qmd` | — | **supprimé** (fusionné dans 2) |
| — | `_notations.qmd` | — | **supprimé** (les sept symboles sont définis sous la formule, au seul endroit où ils servent) |

**Pourquoi.** (a) Le chapitre « contributives » de 392 mots n'a pas d'objet propre : il explique
comment lire la matrice. (b) La matrice répond à la première question économique — qui a droit — et
doit précéder les chapitres de risques, pas les suivre. (c) `_autres_risques` et `_non_contributives`
couvrent chacun plusieurs politiques ; la doctrine demande de les séparer d'abord. Je recommande de
les séparer **par sections dans le même fichier** et non par fichiers : les trois liens entrants
vers `#sec-prest-non-contributives` et les deux vers `_autres_risques.html#sec-perte-emploi`
restent valides sans retouche, et le livre arabe, dont la traduction est différée, ne perd pas de
chapitre.

**Ce que le choix coûte.**

- Fusion de `_contributives` dans `_matrice` : 1 renvoi interne à corriger (`index.qmd`,
  `@sec-prest-contributives`, à garder comme ancre identifiant porté par la section de niveau 2
  « Comment un droit s'ouvre ») ; `_quarto.yml` français **et arabe** à éditer à la main (un chapitre
  de moins, ordre changé) ; le lien de `remunerations_publiques/index.qmd` reste valide (même
  fichier, même identifiant).
- Suppression de `_notations` : 7 renvois internes disparaissent avec le fichier ; `_quarto.yml` des
  deux langues ; `#sec-prestations-notations` et `#tbl-prestations-notations` n'ont aucun renvoi
  entrant.
- Rien à corriger dans les autres livres dans aucun des cas ci-dessus.
- Le choix écarté — scinder `_autres_risques` en trois fichiers (maladie-maternité-décès ;
  accidents du travail ; perte d'emploi) et sortir l'Amen social dans son fichier — coûterait
  2 liens à corriger dans `marche_travail`, 3 fichiers de plus dans les deux `_quarto.yml`, et
  autant de chapitres arabes à créer avant que le livre arabe ne rende de nouveau en entier.

**Identifiants.** Tous les identifiants de section, de tableau et de figure sont conservés ; celui
d'une section qui disparaît devient une ancre `[]{#…}` à l'endroit où son contenu arrive (convention
des fiches des finances locales).

### 2.3 Les frontières avec les volumes voisins

- **Cotisations sociales** : les taux (assurance maladie, accidents du travail, fonds de perte
  d'emploi). Les trois tableaux de cotisation que `_autres_risques` émet aujourd'hui
  (`tbl-perte-emploi`, `tbl-cnrps-maladie`, `tbl-prevoyance-pensionnes`) sont déjà au livre des
  cotisations : ici, une phrase et un lien entre livres suffisent (§ 3.4, arbitrage A5).
- **Caisses** : les comptes par branche (`fig-cnss-assurances-sociales`, `fig-cnss-atmp-pst`) y
  sont. Ce volume-ci montre **les prestations versées** (lignes d'emplois), pas le résultat des
  branches ; il renvoie en tête de chaque longue période.
- **Retraites** : l'indemnité familiale des retraités et le capital-décès des pensionnés (accessoires
  de la pension) ; les primes complémentaires aux faibles pensions.
- **Marché du travail** : la perte d'emploi y est décrite du côté des politiques de l'emploi ; ce
  volume garde la prestation (créances garanties, droits maintenus).
- **Compensation** : volume à part ; un lien en tête de l'index.

---

## 3. Chapitre par chapitre : ruptures et plan cible

Convention commune. `.domicile-unique` sur les titres de niveau 2 des chapitres 3 à 5 (pas sur
l'index ni sur le chapitre de la matrice, voir plus bas). Ancres de registre : `r-pf-…`, `r-ar-…`,
`r-nc-…`. Vérifié dans `scripts/check_domicile_references.py` : le contrôle lit le source `.qmd` ;
un tableau engendré par `table(…)` et un `{{< include >}}` ne portent pas de citation dans le
source et passent donc ; **un tableau fait main qui cite une loi ne peut pas rester au premier plan
d'une section `.domicile-unique`**. D'où la règle suivie partout ci-dessous : tableau de premier
plan sans citation, avec liens `[…](#r-…)` vers un court registre replié placé juste dessous.

« Ce que la loi cherche » : **les notes ne relèvent presque aucune rubrique ni intitulé d'article**.
Sauf mention, l'objet est « non relevé » et figure au ticket du documentaliste (§ 7). Rien n'est
déduit des effets.

### 3.1 `index.qmd` — Présentation (cible : 750 mots de texte, contre 1 400)

Pas de `.domicile-unique` : l'index garde l'encadré des caisses (engendré, partagé par trois
livres, qui cite cinq lois) et ne raconte aucun dispositif.

- **Chapeau** : les deux premiers paragraphes, resserrés en un (ce que le volume couvre ; où sont
  les pensions, les cotisations, les caisses, la compensation — le renvoi en tête).
- **`## Vue d'ensemble`** (nouvelle).
  - *Essentiel* : deux ensembles — des prestations ouvertes par l'affiliation à un régime et
    financées par des cotisations, servies par les caisses ; une assistance sous condition de
    ressources, financée par le budget de l'État.
  - *Vue d'ensemble* : **frise des naissances** (figure nouvelle `fig-prest-frise`, § 5) — 1944,
    1961, 1980, 1986, 1987, 1994, 1995, 1996, 2004-2007, 2019-2020, 2022, 2024, 2025 ; à défaut de
    frise, un tableau court « dispositif — depuis — qui y a droit — financé par — chapitre », neuf
    lignes, **sans citation** (c'est l'actuel tableau « Deux axes », dont la colonne « Ouverture »
    perd ses citations et dont la colonne « Forme » est gardée).
  - *Points* (trois) : (1) le partage contributif / non contributif commande le droit, le financeur
    et le gestionnaire ; (2) la couverture dépend du régime — renvoi à la matrice ; (3) ce que le
    volume donne pour chaque prestation : qui y a droit, combien, financé par qui, combien de
    bénéficiaires et quelle dépense quand une série existe.
- **`## Les organismes`** : l'encadré engendré, inchangé ; le paragraphe sur la CNAM (art. 8 de la
  loi n° 2004-71) est gardé, en trois phrases.
- **Replié**, sous la vue d'ensemble : `Classement des prestations selon l'ouverture du droit et la
  forme : textes par dispositif, 1960-2025` — la colonne « Ouverture » du tableau actuel avec ses
  citations ; `Vocabulaire des textes : « indemnités en espèces », « transferts financiers
  directs », prestation monétaire, non monétaire, mixte` — la convention n° 2 et la remarque sur la
  crèche.
- **Disparaît du premier plan** : la convention n° 4 (jargon de dépouillement — supprimée ; son
  contenu utile, « seul l'intitulé de ce texte est connu ici », se dit ligne par ligne dans les
  registres) ; la convention n° 3 (redistribuée : quotas → section de l'aide médicale ; score →
  section de l'éligibilité ; PNAFN → sa section) ; « Le périmètre de l'assistance » (la phrase sur
  1986 va à la mise en place du chapitre 5 ; la phrase d'exclusion est supprimée, l'information
  subsiste dans « Autres aides » du chapitre 5).

### 3.2 `_matrice.qmd` — Qui est couvert : les régimes et les prestations (cible : 900 mots, contre 1 396 pour `_matrice` + `_contributives`)

Chapitre transversal : il n'a pas de mise en place ni de réformes propres ; la date d'entrée de
chaque régime dans chaque prestation est dans la matrice même. Pas de `.domicile-unique` au
niveau du chapitre si la matrice garde ses références de case (« arts 51-67 ») ; les clés de la
ligne « Sources » passent dans un registre replié.

- *Essentiel* : une prestation contributive n'est ouverte qu'aux affiliés de certains régimes ; les
  prestations familiales ne le sont que dans deux régimes de la CNSS sur sept et, sous une autre
  forme, dans le secteur public.
- *Vue d'ensemble* : **la matrice** (9 lignes), au premier plan, inchangée ; la convention de lecture
  ramenée à une ligne de légende sous le tableau (●, ○, ?). Elle ne se replie pas : tableau court,
  état du droit.
- *Points* (quatre, repris des cinq commentaires actuels) : les prestations familiales (deux régimes
  sur sept, 1961 et 1er octobre 1989) ; les non-salariés (énumération qui commence à l'article 68) ;
  le secteur public (indemnité servie par l'employeur, traitement maintenu) ; la perte d'emploi
  (quatre cases non tranchées).
- Titres de niveau 2 (deux au moins, pour que la numérotation ne refuse pas une section à une
  seule sous-section) : `## La matrice {#sec-matrice-lecture}` et
  **`## Comment un droit s'ouvre {#sec-prest-contributives}`** — les six étapes en une liste
  resserrée (une ligne chacune), les durées de stage renvoyées au chapitre des risques.
- *Replié* : `Régimes et prestations : textes et articles ouvrant ou fermant chaque case de la
  matrice, 1960-2024` (registre, une ligne par régime, avec les clés de l'actuelle ligne
  « Sources ») ; `Régime de la loi n° 2002-32 : dénomination dans les trois livres et entrée dans
  l'assurance maladie` (le dernier commentaire).
- Les quatre `TODO` : celui de la perte d'emploi et de la loi n° 2002-32 reste ici ; ceux de la
  pagination et des dates d'effet vont au ticket du documentaliste (§ 7) et au backlog ; celui du
  terminologue va au backlog (douze notions à créer).

### 3.3 `_prestations_familiales.qmd` (cible : 2 300 mots de texte, contre 3 261 ; note de figure ≤ 150 mots)

**Frontière.** Le cœur : les allocations familiales du régime des salariés non agricoles — qui y a
droit, pour combien d'enfants, à quel taux, sur quelle assiette. Le secondaire : la majoration pour
salaire unique (1980), la contribution aux frais de crèche (1994), les congés de naissance et de
jeunes travailleurs (remboursements à l'employeur), les indemnités à caractère familial du secteur
public. L'allocation familiale non contributive est au chapitre 5 ; renvoi en tête.

**Ruptures retenues** (toutes sur un article lu, d'après le chapitre et la note) :

| # | Date d'effet | Texte | Avant → après | Ce que la loi cherche | Naît |
|---|---|---|---|---|---|
| mise en place | 1er avril 1961 | loi n° 60-30, art. 51-67, 121-131 | caisses d'allocations familiales du décret du 8 juin 1944 → une caisse nationale ; droit limité aux quatre premiers enfants ; 15 % par enfant d'un salaire plafonné à 52,500 D par trimestre | objet non relevé (rubrique : titre II, chapitre premier) | congés de naissance, congés de jeunes travailleurs |
| P1 | 1er mai 1980 | loi n° 80-36, art. 1 (art. 65 bis) et 2 | pratique conventionnelle d'employeurs → majoration légale servie par la caisse aux foyers à un seul revenu | intitulé de la section : « Majoration pour Salaire Unique » ; objet non relevé au-delà | majoration pour salaire unique |
| P2 | 1er janvier 1989 (privé et public) ; 1er octobre 1989 (régime agricole amélioré) | loi n° 88-38, art. 1 et 5 ; loi n° 88-39 ; loi n° 89-73 | quatre enfants → trois ; un régime de plus | objet non relevé | — |
| P3 | 1er octobre 1994 | loi n° 94-88, art. 2-4 ; décret n° 95-114 | néant → contribution versée à la crèche pour les enfants des mères salariées sous plafond de salaire | objet non relevé | contribution aux frais de crèche |

**Deux lectures pour 1976** (loi n° 75-82 : taux unique de 15 % → 18/16/14/12 % selon le rang ;
plafond 52,500 → 72 D). Le chapitre actuel la nomme « rupture de méthode ». Lecture A, *étape ou
ajustement* : ni le public ni le financeur ne changent, la loi règle le niveau et sa modulation.
Lecture B, *rupture* : la dégressivité par rang introduit un objectif nouveau — lecture qui ne se
soutient que si la loi ou son exposé le dit, ce que la note ne relève pas. **Recommandation :
ajustement majeur, présenté au premier plan dans l'entre-temps 1961-1980 avec la figure du montant
par enfant, sans titre de rupture** (arbitrage A3).

Classement des autres textes : loi n° 86-75 (plafond 72 → 122 D, 1er mai 1986), **ajustement** ;
loi n° 96-65 (âges 14 → 16 et 20 → 21 ans, enfants handicapés hors rang, attributaire), **étape**
de la mise en place (conditions tenant à l'enfant), date d'effet non établie ; loi n° 96-101, art. 7
(maintien quatre trimestres), **hors chapitre**, annoncée d'une phrase, renvoi à `@sec-perte-emploi` ;
loi n° 82-71 (prestations familiales des licenciés), connue par son seul objet : ligne de registre
signalée, ne porte rien ; décrets n° 86-611, 88-1136, 96-1906 (secteur public), **ajustements** de
la fiche du secteur public ; décret n° 75-952, intitulé seul.

**Plan cible.**

- **Chapeau** : une phrase d'objet ; renvois en tête (secteur public plus bas ; allocation non
  contributive au chapitre 5).
- **`## Vue d'ensemble {#sec-pf-vue-ensemble .domicile-unique}`** (nouvelle)
  - *Essentiel* : la caisse verse au salarié du régime non agricole, pour chacun de ses trois
    premiers enfants, un pourcentage de son salaire trimestriel plafonné à 122 dinars — soit au plus
    21,960 D, 19,520 D et 17,080 D par trimestre selon le rang. Le plafond est celui
    de 1986, les taux ceux de 1976 ; aucun texte les modifiant n'est identifié ici après 1988
    (la chaîne des lois modifiant la loi n° 60-30 n'a été dépouillée que jusqu'en 2007 : D12, et
    ancre `RECHERCHE` à créer avec cette couverture).
  - *Vue d'ensemble* : **figure nouvelle `fig-pf-montant-max`** — montant maximal par enfant et par
    trimestre (1er rang, et total d'un foyer de trois puis quatre enfants), dinars courants et
    dinars de 2025, 1961-2025, ruptures marquées ; puis le tableau court des ruptures (quatre lignes,
    sans citation, liens `#r-pf-…`).
  - *Points* (quatre) : qui y a droit (deux régimes de la CNSS ; renvoi à la matrice) ; combien
    (taux par rang × salaire plafonné ; le plafond est fixé en dinars par la loi, non en multiple
    du salaire minimum) ; deux prestations adjointes
    (1980, 1994), aux montants fixés en dinars ; ce que la branche verse (67,4 MD en 1990, 70,1 MD
    en 2004 — renvoi à la longue période).
  - *Replié* : rien.
- **`## La mise en place, 1944-1961 {#sec-pf-loi-1960 .domicile-unique}`**
  - *Essentiel* : la loi n° 60-30 remplace, au 1er avril 1961, les caisses d'allocations familiales
    du décret de 1944 par une caisse nationale et fixe le droit à 15 % du salaire plafonné pour
    chacun des quatre premiers enfants.
  - *Premier plan* : ce avec quoi la loi rompt (un paragraphe : `[]{#sec-pf-origines}`) ; les trois
    composantes ; qui, jusqu'à quel âge (l'état d'origine **et** l'état actuel, en une phrase
    chacun), combien d'enfants ; **la formule**, encadré gardé, symboles définis sur place.
  - *Replié* : `Passage du régime de 1944 à la loi n° 60-30 : caisses dissoutes, dévolution et
    droits acquis, articles 121 à 131` ; `Allocations familiales : maintien du droit, orphelins,
    périodicité du versement, articles 56 à 65 de la loi n° 60-30`.
- **`## Les grandes réformes, 1976-1996 {#sec-pf-reformes .domicile-unique}`**
  - *Vue d'ensemble* : renvoi à la figure et au tableau des ruptures.
  - `### 1961-1980 : des taux par rang et un plafond relevé {#sec-pf-reforme-1976}` (entre-temps,
    1976 en deux phrases et les quatre taux).
  - `### 1980 : la majoration pour salaire unique` — naissance en trois phrases, renvoi à sa section.
  - `### 1980-1989 : le plafond porté à 122 dinars {#sec-pf-reforme-1986}` (une phrase).
  - `### 1989 : les trois premiers enfants, et le régime agricole amélioré {#sec-pf-reforme-1989}`.
  - `### 1994 : la contribution aux frais de crèche` — naissance, renvoi.
  - `### Depuis 1994 {#sec-pf-reforme-1996}` : les âges de 1996 (deux phrases), le maintien du droit
    des licenciés (renvoi), puis : aucun texte modifiant le taux, le plafond ou le nombre d'enfants
    n'est identifié après 1988 (constat de la note, R2, établi sur les lois de 1961 à 2007 ;
    prolongement jusqu'en 2026 : D12) avec ancre `RECHERCHE` à créer.
  - *Replié* : `Allocations familiales du régime des salariés non agricoles : textes et articles,
    date par date, 1961-1996` (registre, colonne « Portée ») ; `Âges limites de l'enfant ouvrant
    droit : loi n° 60-30 et loi n° 96-65` (le tableau fait main de six lignes).
- **`## L'état du droit en 2026 {#sec-pf-etat-du-droit .domicile-unique}`**
  - `tbl-af-evolution` (engendré, quatre lignes) reste **au premier plan** ; une phrase par
    paramètre ; le paragraphe « Trois conséquences » est supprimé (redite des réformes), son contenu
    subsiste dans le registre et dans les réformes.
- **`## La majoration pour salaire unique {#sec-pf-salaire-unique .domicile-unique}`**
  - *Essentiel* : depuis le 1er mai 1980, la caisse verse 9,375 D, 18,750 D ou 23,475 D par trimestre
    au salarié dont le conjoint n'a pas d'activité, selon qu'il a un, deux ou trois enfants et plus.
  - *Vue d'ensemble* : `tbl-salaire-unique` (engendré) et **`fig-pf-msu-creche-reel`** (les deux
    montants en dinars de 2025).
  - *Points* : trois conditions ; substitution de la caisse aux employeurs ; aucun texte de
    revalorisation identifié (`RECHERCHE r-majoration-creche-revalorisation`, existante) — le texte
    dit « aucun texte de revalorisation n'est identifié ici », jamais « gelé ».
  - *Replié* : `Majoration pour salaire unique : textes, et l'intitulé du décret n° 74-463` (le
    paragraphe « confusion de vocabulaire »).
- **`## La contribution aux frais de crèche {#sec-pf-creche .domicile-unique}`** : même gabarit ;
  `tbl-creche` au premier plan ; le champ réservé aux mères salariées dit en une phrase.
- **`## Le secteur public : les indemnités à caractère familial {#sec-pf-secteur-public .domicile-unique}`**
  (remonte **avant** la longue période)
  - *Essentiel* : l'agent public reçoit de son employeur, et non d'une caisse, une indemnité fixée
    en dinars par décret pour ses trois premiers enfants — 7,320 D, 6,507 D et 5,693 D par mois
    depuis le 1er novembre 1996.
  - *Vue d'ensemble* : `tbl-indemnites-familiales-public` (engendré), et le montant en dinars de
    2025 sur la figure commune.
  - *Points* : exclusion réciproque avec le régime de la loi n° 60-30 ; payeur ; droits acquis du
    quatrième enfant.
  - *Replié* : `Indemnités à caractère familial du secteur public : décrets et montants, 1975-1996`
    (registre) .
- **`## Longue période et données {#sec-pf-longue-periode}`**
  - Renvoi en tête au livre des caisses pour les comptes de la branche.
  - `fig-pf-montant-max` commentée (pouvoir d'achat du maximum par enfant) ; **`fig-pf-plafond-smig`**
    (plafond trimestriel rapporté au SMIG trimestriel, 1961-2026) ; `fig-cnss-allocations-familiales`
    (existante), sa note de lecture ramenée à 150 mots, le reste passant dans le texte ou dans un
    bloc replié `Dépense de prestations familiales de la CNSS, 1990-2004 : lecture de la colonne
    1999, changement de base du PIB, périmètre des ressources`.
  - Le `TODO` des séries manquantes (allocataires, enfants, dépense avant 1990 et après 2004) reste.

### 3.4 `_autres_risques.qmd` (cible : 2 400 mots de texte, contre 3 423)

**Frontière.** Le chapitre couvre cinq risques. Son fil : **quel risque est couvert, depuis quand,
pour qui**. Chaque risque a ensuite sa section, construite sur le même gabarit (qui, combien, payé
par qui ; état du droit ; évolution repliée). Les taux de cotisation sont au livre des cotisations.

**Ruptures retenues** (cinq, sur articles lus) :

| # | Date d'effet | Texte | Avant → après | Ce que la loi cherche | Naît |
|---|---|---|---|---|---|
| mise en place | 1961 (date d'effet des articles 68-98 non relevée) | loi n° 60-30, art. 68-91 | néant décrit → « assurances sociales » des salariés non agricoles : indemnités de maladie, de couches, de décès, soins | rubrique : « Les assurances sociales » (titre II, chapitre II) ; objet non relevé au-delà | indemnité de maladie, de couches, de décès |
| R1 | 1er janvier 1995 (privé) ; 1er janvier 1996 (public) | loi n° 94-28, art. 3-5, 103-107 ; loi n° 95-56, art. 2, 5, 58 | contrats d'assurance et Fonds des accidents du travail (loi n° 57-73) → régime légal géré par la caisse, tous travailleurs ; régime propre des agents publics | objet non relevé | réparation des accidents du travail par la caisse |
| R2 | (date d'effet non établie) 1996 | loi n° 96-101, art. 2-9 | néant → la CNSS avance les indemnités de licenciement impayées et maintient quatre trimestres les prestations familiales et les soins | objet non relevé (intitulé de la loi à relever) | protection des travailleurs licenciés |
| R3 | 1er juillet 2007 | loi n° 2004-71, art. 1-8, 15 ; décret n° 2007-1366, art. 1-2 | soins des assurances sociales par régime → régime de base d'assurance maladie commun aux deux secteurs, une caisse nouvelle (CNAM) qui reprend aussi les accidents du travail et les indemnités de maladie et de couches | objet non relevé (art. 1er à citer) | assurance maladie, CNAM |
| R4 | 2024 (aucune clause d'effet) | loi n° 2024-44, art. 1-10 | congé de couches du seul régime de 1960 → congés de maternité et de paternité communs aux agents publics et aux salariés **et non-salariés** du privé | intitulé de la loi à relever | congé de paternité ; congé prénatal |

Classement des autres textes : décret n° 93-308 (capital-décès du secteur public, 1er juillet 1993,
abroge le décret n° 74-572), **rupture propre à la fiche du décès** (réécriture ; lignée de 1951 et
loi n° 74-41 connues par renvoi) ; loi n° 97-58 (soins aux enfants à charge, 1er mai 1997), **étape** ;
loi n° 98-91 (trimestre le plus favorable, plafond à deux SMIG, 1er mai 1998), **ajustement** de
l'assiette — à signaler au premier plan car il commande le montant ; loi n° 95-101 (prescription),
**ajustement**, lue en partie ; décret-loi n° 2024-4, art. 38-48 (travailleuses agricoles), **étape**
de R1 (nouveau public) — deux lectures possibles, voir § 8 des risques ; loi n° 2017-47 (circuit de
recouvrement), **ajustement** administratif, replié ; décret n° 2007-1406 (paliers de cotisation
2007-2010), **étape** de R3, au livre des cotisations ; **article 17 de la loi de finances pour
2025** (fonds d'assurance contre la perte d'emploi) : rupture propre à la fiche de la perte d'emploi
— un nouveau financeur et un régime annoncé —, lu dans l'édition arabe, décret d'application non
identifié : la fiche la porte, le fil du chapitre la signale dans l'entre-temps.

**Plan cible.**

- **Chapeau** et **`## Vue d'ensemble {#sec-ar-vue-ensemble .domicile-unique}`** (nouvelle)
  - *Essentiel* : hors pensions et prestations familiales, les régimes contributifs couvrent la
    maladie et la maternité (indemnité de 50 % du salaire journalier moyen plafonné ; soins), le
    décès (un capital), l'accident du travail (soins, indemnité des deux tiers du salaire, rente)
    et, depuis 1996, la perte d'emploi pour motif économique (créances garanties et droits
    maintenus, sans revenu de remplacement).
  - *Vue d'ensemble* : tableau court « risque — ce qui est servi — depuis — par quelle caisse
    aujourd'hui » (cinq lignes, sans citation), puis le tableau des ruptures (cinq lignes).
  - *Points* : privé et public ne servent pas la même chose (indemnité / traitement maintenu) ;
    la CNAM sert depuis 2007 des droits que fixent toujours les lois de 1960, 1994 et 1995 ; ce que
    la CNSS versait de 1990 à 2004 en indemnités de maladie, de couches et de décès : deux ou trois
    nombres datés dans le texte et un lien vers `fig-cnss-assurances-sociales` du livre des caisses,
    qui trace déjà ces lignes (un fait se montre une seule fois).
- **`## La mise en place et les réformes, 1960-2024 {#sec-ar-reformes .domicile-unique}`** : cinq
  sous-sections courtes (1960 ; 1995-1996 ; 1996 ; 2004-2007 ; 2024), deux à trois phrases chacune
  — ce que la loi fait, pour qui —, chacune renvoyant à la section du risque. Bloc replié :
  `Maladie, maternité, décès, accidents du travail, perte d'emploi, assurance maladie : textes et
  articles, date par date, 1957-2025` (registre complet, colonne « Portée »).
- **`## Les indemnités de maladie et de maternité {#sec-ar-maladie-maternite .domicile-unique}`**
  - *Essentiel* : 50 % du salaire journalier moyen, du 21ᵉ au 180ᵉ jour pour la maladie, pendant
    le congé légal pour la maternité.
  - *Premier plan* : conditions d'ouverture en un tableau court (prestation — immatriculation —
    jours de travail — durée — taux), sans citation ; l'assiette et son plafond de deux SMIG depuis
    1998 ; **les congés depuis 2024** : tableau ramené à trois lignes (prénatal, postnatal,
    paternité) × deux secteurs.
  - *Replié* : `Indemnités de maladie et de couches : conditions, carence, assiette et textes,
    1960-1998` ; `Congés de maternité, de paternité et d'allaitement de la loi n° 2024-44 : durées
    par cas, repos d'allaitement, protection contre le licenciement` (le tableau entier de six
    lignes et le paragraphe de garanties) ; le « point ouvert » sur le stage devient une phrase de
    constat avec ancre `RECHERCHE` à créer.
- **`## Le décès {#sec-ar-deces .domicile-unique}`**
  - *Essentiel* : au privé, une indemnité égale à 120 fois l'indemnité journalière de maladie si le
    travailleur décède ; au public, un capital d'une année de rémunération majorée, financé par une
    cotisation propre de 1 %.
  - *Replié* : `Indemnité de décès du secteur privé : multiplicateurs selon la personne décédée,
    ordre des bénéficiaires, prescription` ; `Capital-décès du secteur public : champ, ayants droit,
    taux selon l'âge du retraité, partage, décret n° 93-308` (les deux tableaux et les règles de
    partage).
- **`## Les accidents du travail et les maladies professionnelles {#sec-ar-atmp .domicile-unique}`**
  - *Essentiel* ; tableau court des prestations ramené à quatre lignes (soins ; incapacité
    temporaire : deux tiers ; incapacité permanente : rente ; décès : rente de 50 ou 40 % au
    conjoint) ; secteur public : traitement maintenu, pas d'indemnité journalière ; travailleuses
    agricoles (2024).
  - *Données* : renvoi en tête au livre des cotisations (`fig-atmp-declares`, `fig-atmp-frequence`)
    et à celui des caisses (`fig-cnss-atmp-pst`).
  - *Replié* : `Accidents du travail du secteur privé : définitions, champ, prestations article par
    article, loi n° 94-28` (le tableau de sept lignes, les définitions, les dispositions
    transitoires) ; `Accidents du travail du secteur public : partage entre employeur et caisse,
    loi n° 95-56`.
- **`## La protection contre la perte d'emploi {#sec-perte-emploi .domicile-unique}`** (identifiant
  conservé : deux liens entrants)
  - *Essentiel* ; les trois puces actuelles en deux ; ce que la caisse a pris en charge de 1997 à
    2004 (indemnités de licenciement, maintien des prestations familiales) : nombres datés et lien
    vers `fig-cnss-atmp-pst` du livre des caisses, qui trace déjà ces deux lignes ; le fonds de
    2025 en un paragraphe, avec le constat et l'ancre `RECHERCHE` existante.
  - Le tableau `tbl-perte-emploi` (une ligne, une cotisation) : **retiré d'ici**, phrase et lien
    vers le livre des cotisations (arbitrage A5).
  - *Replié* : `Fonds d'assurance contre la perte d'emploi de la loi de finances pour 2025 :
    ressources, abrogations, édition lue`.
- **`## L'assurance maladie {#sec-ar-assurance-maladie .domicile-unique}`**
  - *Essentiel* : depuis le 1er juillet 2007, un régime de base commun, financé par 6,75 % du
    salaire, géré par la CNAM.
  - *Premier plan* : qui est couvert (assuré et ayants droit, en une phrase) ; quels régimes sont
    entrés en 2007 (renvoi à la matrice) ; la cotisation en une phrase, lien vers le livre des
    cotisations ; **les deux tableaux de paliers 2007-2010 retirés d'ici** (A5).
  - *Replié* : `Assurance maladie : bénéficiaires, calendrier d'entrée des régimes et circuit des
    cotisations, 2004-2017`.
  - Ce chapitre ne décrit pas les prestations de soins elles-mêmes (filières, taux de prise en
    charge, plafonds) : la note ne les a pas relevées ; question D13 au documentaliste (§ 7), hors de la conversion.

### 3.5 `_non_contributives.qmd` (cible : 3 300 mots de texte hors matière nouvelle, contre 4 965 ; plafond 3 800 avec la matière nouvelle du § 3.5.1)

#### 3.5.1 L'Amen social : ce qui est périmé, ce qui peut être engendré, ce qui manque

**Périmé dans le chapitre** (constaté sur `tables/*.md` et sur le texte) :

1. `tbl-amen-base`, `tbl-amen-supplement`, `tbl-amen-vs-afnc` commencent au **20 mai 2020** (jour de
   publication). Les paramètres commencent désormais au **25 mai 2020**, date où l'arrêté et le
   décret gouvernemental n° 2020-317 deviennent exécutoires (cinq jours après le dépôt, loi
   n° 93-64, art. 2).
2. La phrase « faute de clause spéciale et de date de dépôt du *Journal officiel* établie ici, cette
   date n'est pas présentée comme sa date d'effet » est caduque : la date de dépôt est établie.
3. **Le palier de 280 D au 1er janvier 2026** (arrêté conjoint du 21 avril 2026, JORT n° 40, p. 786)
   manque ; légendes et texte disent « jusqu'en 2025 », « de 2022 à 2025 ».
4. Le titre « Les allocations familiales non contributives (2022 →) » et tout le texte ne
   connaissent que les enfants de moins de six ans. **L'allocation des 6 à 18 ans** (décret
   n° 2025-426 du 2 octobre 2025, effet de l'institution au 1er janvier 2025 ; arrêté conjoint du
   3 novembre 2025 fixant 30 D par mois et par enfant, exécutoire le 9 novembre 2025) manque.
5. La section du PNAFN s'arrête à l'arrêté du 29 août 2025 (plafond de 260 D). **Un arrêté conjoint
   du 5 août 2026** modifiant l'arrêté du 10 juillet 2024 est déjà dans `precis/fr/references.json`
   (`arrete-2026-08-05-allocation-pauvres`, JORT n° 80, p. 1611-1612) et cité par le livre
   « Retraites » ; son contenu n'est dans aucune note du volume.
6. L'aide de rentrée scolaire : le tableau engendré donne 50 D et un tableau fait main d'une ligne
   donne 100 D au 1er septembre 2024 ; les deux doivent n'en faire qu'un (voir § 6).
7. Le paragraphe sur la **majoration pour handicap lourd** (« Ce chapitre ne tranche pas cette
   lecture ») : la notice du paramètre retient désormais une lecture — majoration d'un demi-salaire
   minimum sur chacun des quatre paliers, appuyée sur l'article 7 du même décret et sur l'édition
   arabe — et la note documentaire du volume dit encore le texte ambigu. **Je ne tranche pas** :
   question D3 au documentaliste, désaccord possible signalé au § 8.
8. La note de la figure du PNAFN parle de « date encodée ».

**Peut désormais être engendré depuis les paramètres** :

| Tableau | Aujourd'hui | Paramètres | État |
|---|---|---|---|
| Plafonds de ressources de l'Amen social selon la taille du ménage | fait main, 4 lignes | `prestations/non_contributives/amen_social/eligibilite/{un_membre,deux_membres,trois_quatre_membres,plus_de_cinq_membres}`, datés du 25 mai 2020, sourcés sur l'art. 5 | faisable après : relèvement de `VERSION_MINIMALE` de (0, 122) à (0, 124) dans `scripts/openfisca_tables.py` ; fonction nouvelle dans `generate_prestations_tables.py` |
| Les mêmes plafonds avec un membre lourdement handicapé | absent | `…/eligibilite/handicap_lourd/*` | **à ne pas engendrer avant la réponse à D3** |
| Base du transfert, 2020-2026 | engendré, périmé | `amen_social/allocation_base` (six paliers) | faisable après : version minimale ; `CLES_AMEN` à rekeyer (`2020-05-25`) ; **clé de bibliographie à créer** pour l'arrêté du 21 avril 2026 (absente des deux `references.json`) |
| Supplément par enfant | engendré, périmé d'une date | `amen_social/supplements/*` | idem, `CLES_SUPPLEMENT` |
| Allocations familiales de l'Amen social, moins de 6 ans et 6-18 ans | `tbl-amen-vs-afnc`, sans les 6-18 ans | `allocation_familiale`, `allocation_familiale_6_18` | idem ; **deux clés à créer** (décret n° 2025-426, arrêté du 3 novembre 2025) |
| Aides occasionnelles | engendré | `amen_social/aides_ponctuelles/*` | la rentrée scolaire à 100 D n'est pas au modèle (§ 6) |

**Manque, et n'est ni dans le chapitre ni dans les notes** :

- **Bénéficiaires et crédits.** Le rapport de suivi et d'évaluation du programme pour 2023 du
  ministère des Affaires sociales est dépouillé dans `tunisia-data` (`mas-amen-social-2023-
  beneficiaires-bruts`, `…-credits-bruts`) : bénéficiaires du transfert mensuel en décembre,
  242 833 (2018) → 337 199 (2023), entrées et sorties annuelles ; crédits affectés 2021-2023 par
  intervention (transfert mensuel 645,0 → 867,0 MD ; total 735,1 → 1 015,5 MD) ; enfants aidés
  2022-2023. Source administrative : elle peut porter la longue période. **Ces deux séries ne sont
  pas dans `precis/_seriescache/` ni dans son catalogue** : à instantaner d'abord.
- **Le rapport dit lui-même trois totaux pour 2023** (337 178 au texte, 337 199 au tableau des
  flux, 337 200 au tableau par montant) et deux montants pour l'allocation des moins de six ans en
  2023 (45 827 mD au tableau des crédits, 54 943,4 au texte). Le plan de figure garde le tableau
  des flux comme base et dit les deux autres en note.
- **Le rapport compte des enfants de 6 à 18 ans aidés en 2023** (422 542), alors qu'aucun texte
  publié ne fonde une aide mensuelle à cette tranche avant 2025 selon la notice du paramètre :
  question D4.
- **Rapports extérieurs.** Huit documents rangés et catalogués le 9 octobre 2026
  (`sources/banque-mondiale-rapports-urls.csv`) : document de projet de la Banque mondiale de 2021
  (PAD4414), financements additionnels de 2022 et 2026, deux rapports de suivi (dont un non
  dépouillé), accord de prêt n° 9230-TN (non dépouillé), rapport et fiche de l'UNICEF de 2024 sur
  l'allocation des 6-18 ans. **Aucun n'a de série extraite ni de clé de bibliographie** : à
  documenter d'abord. Le plan ne leur ouvre pas de place nouvelle (doctrine en attente) ; l'actuelle
  phrase sur `@unicef2020` reste où elle est, et le `TODO` sur les phases de financement renvoie à
  ces pièces. Si le propriétaire veut une section d'études, elle vient après la longue période,
  titrée comme telle, chaque étude avec sa méthode (arbitrage A6).
- **Le seuil de score** (`amen_social/decile`, circulaire n° 12 du 12 mai 2022 hébergée hors du
  *Journal officiel*) : le chapitre ne le mentionne pas, et un texte de ce rang n'est pas établi par
  la note. Il n'entre pas au chapitre sans lecture par le documentaliste (D5).

#### 3.5.2 Frontière et ruptures

**Frontière.** Le cœur : l'aide monétaire permanente aux ménages pauvres — le programme d'aide aux
familles nécessiteuses puis le transfert de l'Amen social —, son public, son montant, son financeur.
Le secondaire : l'aide médicale (livrets, cartes, support électronique) ; les allocations familiales
de l'Amen social ; les aides occasionnelles ; l'aide exceptionnelle de 2021 ; les aides
catégorielles des lois de finances ; l'autonomisation économique.

| # | Date | Texte | Avant → après | Ce que la loi cherche | Naît |
|---|---|---|---|---|---|
| mise en place | 1986-1988 | loi n° 86-83, art. 13 ; arrêté du 6 janvier 1987 ; loi n° 87-83, art. 62-67 ; loi n° 87-29, art. 1-4 (effet 1er janvier 1988) | — → un programme d'aide monétaire qui n'apparaît dans les textes que comme objet de dépense, cofinancé par les caisses ; une assistance médicale gratuite à deux catégories de livrets | art. 13 : autoriser les caisses « à participer au financement du programme national d'aide aux familles nécessiteuses » ; loi n° 87-29 : objet non relevé | aide permanente (PNAFN) ; assistance médicale gratuite |
| N1 | 1998 | décrets n° 98-409 et n° 98-1812 | livrets attribués par des commissions selon le revenu → cartes attribuées dans la limite d'un nombre global et de quotas régionaux ; plafond de ressources en multiples du salaire minimum pour le tarif réduit | objet non relevé | cartes de soins gratuits et à tarifs réduits |
| N2 | 5 février 2019 (publication) ; prestations ouvertes le 25 mai 2020 | loi organique n° 2019-10, art. 1-2, 8, 11-13, 18-23 ; décret gouvernemental n° 2020-317, art. 4-9 ; arrêtés du 19 mai 2020 | programme sans texte → programme créé par une loi organique, deux publics nommés (catégories pauvres, catégories à revenu limité), pauvreté définie comme privation multidimensionnelle, classement par un score, registre de données | art. 1er : « la promotion des catégories pauvres et des catégories à revenu limité » | transfert monétaire permanent ; supplément par enfant ; appui occasionnel ; soins |
| N3 | 2022 | décret-loi n° 2022-8 (art. 11 bis) ; arrêté du 1er avril 2022 | supplément de 10 D aux seules catégories pauvres → allocation familiale de 30 D par enfant de moins de six ans, ouverte aussi aux catégories à revenu limité non affiliées, sans plafond du nombre d'enfants ; visa d'un accord de prêt de la BIRD | art. 11 bis : objet non relevé au-delà de sa lettre | allocation familiale non contributive |

**Deux lectures pour 1998** : *rupture* (le mode d'attribution change : enveloppe fermée, quotas)
ou *étape* (la dualité gratuit / tarif réduit date de 1987 ; des tarifs réduits existent dès 1993 et
1994, textes connus par leur seul intitulé ; 1998 refond). **Recommandation : rupture propre à la
fiche de l'aide médicale**, non du chapitre — le chapitre garde quatre temps.

**Deux lectures pour 2025** (allocation des 6-18 ans) : *étape* de N3 (même prestation, même
montant, tranche d'âge suivante) ou *rupture* (dispositif institué par un décret propre, hors de
l'article 11 bis). **Recommandation : étape de N3**, dite dans la même sous-section, les deux textes
nommés.

Classement des autres textes. **Cœur** — arrêtés du 1er avril 2022, 3 avril 2023, 28 février 2024,
29 janvier 2025, 21 avril 2026 (base 200, 220, 240, 260, 280 D) : **étapes** de N2 (relèvement par
paliers annuels) ; arrêtés du 10 juillet 2024, du 29 août 2025 et du 5 août 2026 (allocation du
PNAFN relevée dans la limite du transfert) : **étapes** de N2 (rapprochement des deux séries) — le
dernier **non lu par les notes** ; arrêté du 19 mai 2020 sur le score : **modalité** de N2 ; décret
n° 2014-1526 (banque de données) : **étape préparatoire**, replié ; décret gouvernemental
n° 2018-626 : intitulé seul. **Aide médicale** — décret n° 88-175, lois de finances pour 1988 et
1991 (droit d'affiliation, tickets), arrêté du 17 février 1988 : **modalités et ajustements** ;
décrets n° 93-529 et n° 94-1738 : intitulés seuls (le second abrogé par l'art. 25 du décret
n° 98-409, attesté) ; décret n° 2005-2886 (ascendants) : **ajustement** ; décrets n° 2012-2521 et
2012-2522 : **ajustements** (commissions ; cartes annuelles pour des catégories nouvelles — ce
dernier point est un public nouveau, à dire dans la fiche) ; onze décrets de prorogation de 2004 à
2022 : **ajustements**, une ligne de registre chacun ; décret n° 2022-919 (support électronique) :
**étape** de N2 (art. 13 de la loi organique) et fin de la fiche de l'aide médicale. **Aides** —
arrêtés du 19 mai 2020 et du 8 décembre 2022 (appui occasionnel) : naissance dans N2 puis
**étape** (transport scolaire, urgence, revenu limité) ; arrêté du 10 juillet 2025 (rentrée à
100 D, effet 1er septembre 2024) : **ajustement**, lu dans l'édition arabe ; arrêté du 20 août 2021
(300 D une fois) : **dispositif ponctuel**, fiche ; décret n° 2022-715 (autonomisation) :
**naissance d'un dispositif secondaire**, annoncée en 2022 ; lois de finances pour 2025 (art. 26)
et 2026 (art. 35, 71, 81, 96) et arrêté du 30 juillet 2025 : **dispositifs catégoriels**, connus
pour quatre d'entre eux par un résumé arabe — ils ont leur ligne au registre, signalée, et ne
portent pas de rupture ; aides aux personnes âgées et handicapées (arrêtés de 1997, 2003, 2006,
2017) : **hors sujet aujourd'hui**, lisibles au corpus (D8).

#### 3.5.3 Plan cible

- **Chapeau** : objet en deux phrases ; renvoi en tête vers les allocations familiales contributives
  (chapitre 3) et vers le volume de la compensation.
- **`## Vue d'ensemble {#sec-nc-vue-ensemble .domicile-unique}`** (nouvelle)
  - *Essentiel* : en 2026, l'État verse aux ménages classés pauvres par le programme Amen social
    un transfert de base de 280 dinars par mois ; un supplément de 10 dinars par enfant à charge de
    6 à 18 ans (jusqu'à 25 ans en études, en apprentissage ou en formation) s'y attache ; une
    allocation familiale de 30 dinars par enfant, pour les moins de six ans et pour les 6 à 18 ans, est ouverte aux familles pauvres
    et aux familles à revenu limité ; les soins publics leur sont gratuits ou à tarif réduit.
    Phrase à part, obligatoire : **les textes ne règlent pas l'articulation du supplément de
    10 dinars avec l'allocation des 6-18 ans** (constat de la notice du paramètre ; question D11) —
    l'essentiel ne les additionne donc pas. (Chaque montant renvoie à son tableau daté.)
  - *Vue d'ensemble* : **`fig-nc-aide-permanente`** — l'aide mensuelle permanente, 1987-2026,
    dinars courants et dinars de 2025 : paliers du PNAFN (marqués « non fondés sur un texte
    publié » jusqu'en 2018, 180 D constaté en 2024), base du transfert Amen 2020-2026 ; ruptures
    N2 et N3 marquées. Puis le tableau court des ruptures (quatre lignes).
  - *Points* (quatre) : qui y a droit (plafond de ressources en multiples du salaire minimum selon
    la taille du ménage, et classement par un score) ; combien de bénéficiaires et quels crédits
    (337 199 bénéficiaires du transfert mensuel en décembre 2023, sans dire « personnes » ni
    « ménages » tant que D4 n'a pas répondu — le rapport emploie les deux ; 1 015 MD de **crédits
    affectés** en 2023, qui ne sont pas une dépense constatée — renvoi à la longue période) ; financé par le budget de l'État, après un cofinancement des caisses en
    1986-1988 ; deux séries coexistent depuis 2019 (art. 23 de la loi organique).
  - Les cinq « étapes » de l'actuelle section « Comment l'assistance est attribuée » se fondent
    dans ces points ; `[]{#sec-nc-attribution}` n'a pas de renvoi entrant.
- **`## La mise en place, 1986-1988 {#sec-nc-mise-en-place .domicile-unique}`**
  - *Essentiel* : le programme d'aide aux familles nécessiteuses n'est créé par aucun texte publié ;
    il apparaît en 1986 comme une dépense que les caisses sont autorisées à cofinancer ; l'assistance
    médicale gratuite est instituée par une loi en 1987.
  - *Premier plan* : 8 MD en 1986 à parts égales entre les deux caisses, puis 2,5 MD par an au
    budget de l'État à partir de 1988 (les deux chiffres ensemble, avec renvoi au registre) ;
    annonce de l'aide médicale, une ligne, renvoi à sa section.
  - *Replié* : `Financement du programme d'aide aux familles nécessiteuses par les caisses : textes
    et montants, 1986-1988` (le tableau de trois lignes).
- **`## Les grandes réformes, 1998-2025 {#sec-nc-reformes .domicile-unique}`**
  - `### 1988-2019 : des montants relevés sans texte publié, des cartes de soins contingentées` —
    entre-temps : les paliers du PNAFN (renvoi figure) ; 1998 annoncé en deux phrases, renvoi à
    l'aide médicale ; le programme sert de liste aux cartes (1998, 2012) ; banque de données (2014).
  - `### 2019-2020 : l'Amen social {#sec-nc-amen-2019}` — ce que la loi cherche (art. 1er, art. 2
    cités), les deux publics, les quatre prestations annoncées une ligne chacune avec renvoi, le
    maintien des programmes antérieurs (art. 23), l'agence prévue et la gestion par le ministère.
  - `### 2022 : une allocation familiale pour les enfants des familles pauvres et à revenu limité`
    — naissance, renvoi à `@sec-af-non-contributive` ; le même arrêté déplace la borne du
    supplément ; l'autonomisation et le support de soins électronique annoncés d'une ligne chacun.
  - `### 2022-2026 : un relèvement annuel, et le rapprochement des deux aides` — entre-temps : 20 D
    de plus chaque 1er janvier ; l'allocation du PNAFN relevée dans la limite du transfert (2024,
    2025, 2026) ; l'allocation étendue aux 6-18 ans (2025).
  - *Replié* : `Aide monétaire permanente — programme d'aide aux familles nécessiteuses et Amen
    social : textes et articles, date par date, 1986-2026` (registre, colonne « Portée ») ; `Loi
    organique n° 2019-10 : institutions prévues, registre de données, priorités d'accès, articles 5
    à 22`.
- **`## L'état du droit en 2026 {#sec-nc-etat-du-droit .domicile-unique}`**
  - `### Qui y a droit {#sec-nc-eligibilite}` : **tableau engendré des plafonds** (quatre lignes),
    avec, à côté, **les plafonds en dinars par mois au SMIG en vigueur** (colonne calculée ou
    figure `fig-nc-seuils-dinars`, voir D2 sur le régime de salaire minimum visé) ; conditions de
    patrimoine en une phrase ; le score en deux phrases (sept familles de variables, pondérations
    non publiées).
  - `### Combien {#sec-nc-montant}` : `tbl-amen-base` (2020-2026) et `tbl-amen-supplement`,
    engendrés, au premier plan ; le transfert dû à compter du mois de la demande.
  - *Replié* : `Amen social : procédure de demande, enquête sociale, commission régionale, délais,
    opposition et retrait, décret gouvernemental n° 2020-317, articles 12 à 28` ; `Amen social :
    majoration du plafond de ressources pour handicap lourd, article 5` (selon D3) ; `Modèle de
    score de l'Amen social : dimensions, arrêté du 19 mai 2020`.
- **`## L'allocation familiale de l'Amen social {#sec-af-non-contributive .domicile-unique}`**
  (identifiant conservé)
  - *Essentiel* : 30 dinars par mois et par enfant, pour les moins de six ans depuis 2022 et pour
    les 6-18 ans depuis 2025, aux familles pauvres et aux familles à revenu limité non affiliées à
    un régime de sécurité sociale.
  - *Vue d'ensemble* : tableau engendré (deux tranches d'âge, dates, montants) ; **`fig-nc-enfants`**
    (enfants aidés et crédits, 2022-2023) quand la série est instantanée.
  - *Points* : ce qui la distingue de l'allocation contributive (pas de plafond du nombre d'enfants ;
    champ) ; ce qui la distingue du supplément de 10 D ; le financement (visa de l'accord de prêt).
  - *Replié* : `Allocation familiale de l'Amen social : textes, dates d'effet et articulation avec
    le supplément par enfant, 2020-2025`.
- **`## L'aide médicale {#sec-nc-aide-medicale .domicile-unique}`**
  - *Essentiel* : depuis 1988, les ménages à faible revenu accèdent aux soins publics gratuitement
    ou à tarif réduit, avec un livret, puis une carte attribuée dans la limite de quotas (1998),
    puis un support électronique lié à l'Amen social (2022).
  - *Vue d'ensemble* : tableau court de trois lignes (1988, 1998, 2022 : support — qui — à quel
    prix — mode d'attribution), sans citation ; le plafond de ressources du tarif réduit (trois
    lignes) reste au premier plan.
  - *Points* : la dualité date de 1987 ; l'enveloppe fermée (nombre de cartes et quotas non
    identifiés : `RECHERCHE r-amg-cartes-quotas`, existante) ; de 2004 à 2022, onze décrets
    prorogent les cartes, les dernières délivrées étant de 2011 à 2017 (constat de la note § 2.5,
    aujourd'hui absent du chapitre : à porter).
  - *Replié* : `Assistance médicale gratuite : droit d'affiliation et contributions aux frais de
    soins, tarifs de 1988 et de 1991` ; `Carte de soins à tarifs réduits : tarifs par prestation,
    cotisation annuelle, validité, décret n° 98-409` ; `Aide médicale : textes, date par date,
    1987-2022` (registre, avec les prorogations) ; `Commissions d'attribution des livrets et des
    cartes : composition en 1988 et en 2012`.
- **`## Les aides occasionnelles et catégorielles {#sec-nc-aides .domicile-unique}`**
  - *Essentiel* ; `tbl-aides-ponctuelles` au premier plan (avec la rentrée scolaire à jour, § 6) ;
    crédits 2021-2023 (fêtes 27,1 → 30,5 MD ; rentrée 51,0 → 60,9 MD) en figure commune.
  - Sous-sections : `### L'aide exceptionnelle de 2021` ; `### Les aides catégorielles des lois de
    finances pour 2025 et 2026` (tableau sans colonne « Attestation » ; la réserve se dit en clair,
    une fois) ; `### L'autonomisation économique`.
  - *Replié* : `Appui financier occasionnel de l'Amen social : champ, échéances de paiement et
    montants, arrêtés de 2020, 2022 et 2025` ; `Aide exceptionnelle de 300 dinars de 2021 :
    catégories visées` ; `Aide aux patients allergiques au gluten : modalités de demande, arrêté du
    30 juillet 2025`.
- **`## Autres aides {#sec-nc-adjacents}`** : la section « Dispositifs adjacents » récrite en
  positif (ce que sont ces aides, où elles sont traitées) ; `TODO` conservé.
- **`## Longue période et données {#sec-nc-longue-periode}`** (nouvelle)
  - Le budgétaire et l'administratif d'abord : `fig-nc-aide-permanente` (commentée : pouvoir
    d'achat ; rapport au SMIG) ; **`fig-nc-beneficiaires`** (stock de décembre, entrées, sorties,
    2018-2023) ; **`fig-nc-credits`** (crédits par intervention, 2021-2023, MD courants et % du
    PIB — base dite) ; `fig-pnafn-allocation` (existante) fondue dans la première ou gardée comme
    vue (voir § 5).
  - Aucune étude ici tant que A6 n'est pas tranché.

---

## 4. Le registre de destination

PP = premier plan ; R = bloc replié (titre au § 3) ; les lignes des chapitres sont désignées par leur
titre de section.

### 4.1 `index.qmd`

| Élément actuel | Destination |
|---|---|
| Cellule Python d'en-tête | gardée si un tableau engendré est émis ; sinon retirée |
| § 1 (objet du volume) et § 2 (partage avec les autres livres) | PP, chapeau, fondus |
| Encadré « Quatre conventions » — n° 1 | PP, point 1 de la vue d'ensemble |
| — n° 2 (forme monétaire / non monétaire, citations) | R « Vocabulaire des textes… » ; la définition des trois formes reste en une phrase PP |
| — n° 3 (quotas, score, PNAFN) | déplacée : aide médicale, éligibilité, PNAFN du chapitre 5 (les trois faits y sont déjà) |
| — n° 4 (trois niveaux d'attestation) | supprimée du rendu ; l'information subsiste ligne par ligne dans les registres (« seul l'intitulé de ce texte est connu ici ») et dans cette fiche |
| « Le plan du volume » | PP, récrit selon le nouvel ordre ; lien vers la compensation remonté en tête |
| « Le périmètre de l'assistance », § 1 (art. 13 de 1986) | déplacé : mise en place du chapitre 5 (déjà présent) |
| — § 2 (exclusions) | supprimé ; subsiste en positif dans « Autres aides » du chapitre 5 |
| « Les organismes », encadré engendré | PP, inchangé |
| — paragraphe CNAM | PP, resserré |
| « Deux axes de classement », tableau de 9 lignes | PP sans citations (colonnes : dispositif — depuis — qui — financé par — forme — chapitre) + R « Classement des prestations… » avec les citations |
| — dernier paragraphe (crèche, prestation non monétaire) | R « Vocabulaire des textes… » |

### 4.2 `_contributives.qmd` et `_matrice.qmd`

| Élément actuel | Destination |
|---|---|
| `_contributives`, phrase d'ouverture | supprimée (redite de l'index) |
| — six « maillons » | PP, `## Comment un droit s'ouvre {#sec-prest-contributives}` du chapitre de la matrice, une ligne chacun ; durées de stage → tableau court du chapitre des risques |
| — deux « traits de méthode » | PP, fondus dans les points 2 et 3 du chapitre de la matrice |
| `_matrice`, chapeau | PP, phrase d'essentiel |
| Encadré de convention | légende d'une ligne sous la matrice |
| Matrice (9 lignes) | PP, inchangée |
| Ligne « Sources » | R « Régimes et prestations : textes et articles… » |
| Commentaires 1 à 4 | PP, quatre points resserrés |
| Commentaire 5 (bas revenus) | R « Régime de la loi n° 2002-32… » |
| `TODO` perte d'emploi / loi n° 2002-32 | conservé ici |
| `TODO` pagination 2024+ ; `TODO` dates d'effet | conservés en fin de chapitre ; repris au § 7 (D9, D10) |
| `TODO` terminologue (douze notions) | conservé en fin de chapitre |

### 4.3 `_prestations_familiales.qmd`

| Élément actuel | Destination |
|---|---|
| Guide de lecture | récrit (annonce ce qui est présenté) |
| `#sec-pf-origines` § 1 (abrogations) | PP, un paragraphe de la mise en place ; identifiant en ancre |
| — § 2-3 (dispositions transitoires, art. 121-128) | R « Passage du régime de 1944… » |
| — § 4 et `TODO` (décret de 1944) | PP, constat d'une phrase ; `TODO` conservé ; ancre `RECHERCHE` à créer |
| `#sec-pf-loi-1960`, entrée en vigueur, trois composantes, qui, âge, combien d'enfants, montant | PP |
| — maintien du droit ; orphelins ; périodicité | R « Allocations familiales : maintien du droit… » |
| Encadré de la formule | PP, inchangé (symboles définis sur place) |
| `#sec-pf-reforme-1976` et ses expressions | PP, entre-temps 1961-1980 ; identifiant gardé |
| `#sec-pf-reforme-1986` | PP, une phrase d'entre-temps ; identifiant en ancre |
| `#sec-pf-reforme-1989` | PP, réforme P2 |
| `#sec-pf-reforme-1996`, texte | PP, deux phrases dans « Depuis 1994 » |
| — tableau des âges (6 lignes) | R « Âges limites de l'enfant… » |
| — loi n° 96-101 | PP, une phrase et renvoi |
| « La majoration pour salaire unique » | PP, section propre + naissance annoncée en 1980 ; `tbl-salaire-unique` PP |
| — décret n° 74-463 | R |
| — `RECHERCHE` | conservée |
| « La contribution aux frais de crèche », `tbl-creche`, `RECHERCHE` | PP, section propre + naissance annoncée en 1994 |
| `#sec-pf-longue-periode`, `tbl-af-evolution` | PP, déplacé dans « L'état du droit en 2026 » ; renvois `@tbl-af-evolution` inchangés |
| — « Trois conséquences » | fusionné dans les réformes et le registre (redite) |
| — plafond non indexé | PP, vue d'ensemble et longue période (avec la figure du plafond en SMIG) |
| `fig-cnss-allocations-familiales` | PP, longue période ; note de lecture resserrée, le surplus en R |
| `TODO` séries | conservé |
| `#sec-pf-secteur-public`, texte | PP, remonté avant la longue période ; § des quatre décrets → R |
| `tbl-indemnites-familiales-public` | PP |
| `TODO` décret n° 75-952 et circulaire n° 42 | conservé |

### 4.4 `_autres_risques.qmd`

| Élément actuel | Destination |
|---|---|
| « Le socle », § 1 (assurances sociales, champ) | PP, mise en place |
| — indemnité de maladie ; de couches | PP, tableau court des conditions + R pour carence, périodicité, liste des maladies longues |
| — soins (loi n° 97-58) | PP, une phrase (étape) ; détail en R |
| — assiette (1960 → 1998) | PP pour la règle en vigueur ; l'état de 1960 en R |
| « Les congés depuis 2024 », tableau (6 lignes) | PP, trois lignes ; tableau entier en R |
| — garanties ; « point ouvert » | R ; constat d'une phrase PP avec `RECHERCHE` à créer |
| « L'indemnité de décès », texte | PP, essentiel ; tableau des multiplicateurs (5 lignes), ordre de paiement, prescription → R |
| « Le capital-décès », lignée et champ | PP en deux phrases ; R pour le détail |
| — cotisation de 1 % et 0,50 % | PP, une phrase, lien vers le livre des cotisations |
| — ayants droit, montant, tableau par âge (5 lignes), répartition | R |
| « Loi n° 94-28 », abrogation et transfert à la CNAM | PP |
| — définitions, champ | PP en deux phrases ; R pour le détail |
| — tableau des prestations (7 lignes) | PP quatre lignes sans citation ; tableau entier en R |
| — exclusivité ; dispositions transitoires | R ; la substitution au Fonds des accidents du travail reste PP (c'est la rupture) |
| « Loi n° 95-56 » | PP, resserré ; gestion partagée en R |
| « Travailleuses agricoles » | PP, une phrase dans la section des accidents du travail et dans la réforme de 2024 |
| `#sec-perte-emploi`, loi n° 96-101 | PP ; identifiant conservé |
| — article 17 LF 2025 | PP, un paragraphe ; ressources du fonds en R ; `RECHERCHE` conservée |
| `tbl-perte-emploi` | retiré ; lien vers `cotisations_sociales/_autres_branches` (A5) — le tableau subsiste dans ce livre |
| « L'assurance maladie », loi, bénéficiaires | PP resserré ; énumération de l'art. 4 en R |
| — cotisation 6,75 % | PP, une phrase |
| `tbl-cnrps-maladie`, `tbl-prevoyance-pensionnes` | retirés ; liens vers `cotisations_sociales/_maladie` et `_regimes` (A5) — ils y subsistent |
| — décret n° 2007-1366 ; loi n° 2002-32 | PP |
| — loi n° 2017-47 | R |

### 4.5 `_non_contributives.qmd`

| Élément actuel | Destination |
|---|---|
| Chapeau | PP, récrit |
| « Comment l'assistance est attribuée » (cinq étapes) | fusionnée dans les points de la vue d'ensemble et dans « Qui y a droit » |
| « Le financement budgétaire », texte | PP, mise en place |
| — tableau de trois lignes | R « Financement du programme… » |
| « Le programme comme fournisseur de listes » | PP, une phrase d'entre-temps ; détail au registre de l'aide médicale ; banque de données et registre → entre-temps et R de la loi organique |
| « Le montant de l'allocation », `tbl-pnafn-allocation` (11 lignes) | R `Allocation mensuelle du programme d'aide aux familles nécessiteuses : onze montants, 1987-2018` (la figure le remplace au premier plan) |
| `fig-pnafn-allocation` | PP, fondue dans `fig-nc-aide-permanente` (base 2025) ou gardée comme vue ; note de lecture récrite (« date encodée » retiré) |
| `TODO` paliers (issue 462) | conservé |
| — arrêtés de 2024 et 2025 ; architecture ancienne | PP, entre-temps 2022-2026 ; + arrêté de 2026 après D1 |
| « Une superposition, non un remplacement » | PP, dans 2019-2020 et dans le point 4 de la vue d'ensemble |
| « Le régime de 1987 », § 1 | PP, section de l'aide médicale |
| — « correction de chronologie » | PP en une phrase positive (« la dualité date de 1987 ») |
| — décret n° 88-175 | PP une phrase ; durée du livret en R |
| — tableau droit d'affiliation et contributions (6 lignes) et suite | R « Assistance médicale gratuite : droit d'affiliation… » |
| « AMG1 » | PP (condition d'état, quotas) ; ayants droit en R ; `RECHERCHE` conservée |
| « AMG2 », tableau des plafonds (3 lignes) | PP |
| — tableau des tarifs (9 lignes), cotisation, validité | R « Carte de soins à tarifs réduits… » |
| « Les modifications établies » | R (registre et « Commissions… ») ; les cartes annuelles de 2012 : une phrase PP |
| « La sortie du système papier » | PP, resserré ; « Le volume s'en tient… » supprimé |
| « La loi organique n° 2019-10 », § 1-2 | PP, réforme 2019-2020 |
| — § 3 (prestations, registre, bénéficiaires) | PP pour les quatre prestations ; le reste en R « Loi organique n° 2019-10 : institutions… » |
| — § 4 (conseil, agence) | PP une phrase ; R |
| « Les conditions d'éligibilité », âge, revenu | PP |
| — tableau des plafonds (4 lignes, fait main) | PP, **engendré** |
| — patrimoine | PP une phrase |
| — majoration pour handicap | R, rédaction selon D3 |
| — procédure (130 mots) | R « Amen social : procédure de demande… » |
| « Le score d'éligibilité » | PP deux phrases ; R |
| « Le transfert monétaire permanent », `tbl-amen-base`, `tbl-amen-supplement` | PP, régénérés (25 mai 2020 ; 280 D) |
| — phrase sur le 20 mai 2020 | supprimée (caduque) ; la date exécutoire est dans le tableau |
| — décalage février / avril 2022 | R « Allocation familiale de l'Amen social : textes, dates d'effet… » |
| « L'autonomisation économique » | PP, sous-section des aides ; naissance annoncée en 2022 |
| `#sec-af-non-contributive`, texte | PP, section propre, étendue aux 6-18 ans ; « point de vocabulaire » en une phrase positive |
| — mode d'édiction (décret-loi) | R, registre |
| `tbl-amen-vs-afnc` | remplacé par le tableau engendré des deux allocations ; la base du transfert n'y est plus redite (elle est dans `tbl-amen-base`) ; identifiant `tbl-amen-vs-afnc` gardé |
| — `@unicef2020` | laissé où il est |
| `TODO` phases de financement | conservé, complété par les pièces du 9 octobre 2026 |
| « Les aides ponctuelles », `tbl-aides-ponctuelles` | PP |
| — échéances de paiement ; champ 2020 / 2022 | R « Appui financier occasionnel… » ; transport scolaire et aide d'urgence (60 à 200 D, quatre fois par an) : une phrase PP |
| — tableau rentrée scolaire (1 ligne) | fusionné dans `tbl-aides-ponctuelles` (§ 6) ; à défaut, gardé |
| `TODO` édition française de l'arrêté de 2025 | conservé |
| « Les aides exceptionnelles » | PP deux phrases ; catégories en R |
| « Les prestations catégorielles », tableau (5 lignes) | PP sans la colonne « Attestation » ; réserve en clair |
| — arrêté gluten | PP une phrase ; modalités en R |
| `TODO` lois de finances 2025-2026 | conservé (D7) |
| « Dispositifs adjacents » et `TODO` | PP, récrit en positif ; `TODO` conservé |

### 4.6 Le compte, avant et après

| | Avant | Après |
|---|---|---|
| Chapitres | 6 + 2 annexes | 5 + 1 annexe (glossaire) |
| Texte de premier plan (mots, mesure du § 1.1) | 14 597 | ≈ 9 650 hors matière nouvelle ; ≈ 10 150 avec |
| Tableaux engendrés | 12 | 12 − 3 retirés (cotisations, A5) + 2 nouveaux (plafonds de l'Amen ; allocations familiales de l'Amen) = 11, dont 1 replié (PNAFN) |
| Tableaux faits main au premier plan | 15 | une douzaine, tous courts (≤ 9 lignes) et sans citation de loi : matrice ; index ; ruptures × 3 ; risques couverts ; conditions maladie-maternité ; congés ; prestations AT ; aide médicale ; plafonds AMG2 ; aides catégorielles |
| Tableaux faits main repliés | 0 | 10 (les actuels, entiers) + les registres |
| Figures | 2 | 2 + 6 à 8 (§ 5) ; le chapitre des risques n'en a pas en propre : il renvoie à deux figures du livre des caisses |
| Blocs repliés | 0 | ≈ 30 |
| `TODO` | 12 | 12, plus ceux du § 6 |
| `RECHERCHE` | 4 (3 fiches) | 4 + 3 à créer (régime de 1944 ; date d'effet de la loi n° 96-65 et textes postérieurs à 1988 ; articulation de la loi n° 2024-44 avec le stage) |
| Identifiants | tous | tous conservés (en ancre quand la section disparaît), sauf `sec-prestations-notations` et `tbl-prestations-notations` |

Cibles de texte de premier plan : index 750 ; régimes et prestations 900 ; prestations familiales
2 300 ; autres risques 2 400 ; assistance 3 300 (3 800 avec la matière nouvelle). Total 9 650
(10 150), soit −34 % (−30 %).

---

## 5. Les figures

Convention proposée : **dinars constants de 2025**, par le déflateur du volume du marché du travail
(`precis/fr/marche_travail/figures/deflateur.py` : `ipc-longue-periode` 1962-2023 prolongé par
`bct-ipc-base2015` jusqu'en 2025 — les deux séries sont dans `precis/_seriescache/`). Ce module est
dans un autre livre : le remonter dans `scripts/` (ou le dupliquer dans `prestations_sociales/figures/`)
est un préalable d'une demi-heure, à faire dans la première PR — qui touche alors le livre du
marché du travail et doit le rendre aussi (`scripts/verifier.sh marche_travail prestations_sociales`). Les deux figures existantes ont
leurs propres bases (1990 et 1987) et un indice propre (`ins-annuaire-ipc`, `ipc-pnafn-base1987`) :
les passer à 2025 change les nombres cités dans les notes de lecture (67,4 → 40,7 MD de 1990), à
recalculer et non à recopier.

Composants disponibles : `figtools.figure_tabs`, `figtools.figure_escalier` (paramètres dans le
temps), `openfisca_tables.tableau_a_la_date`, `openfisca_tables.ecrire_serie_parametres` (c'est lui
qui écrit `pnafn-allocation.csv` dans le cache depuis `generate_prestations_tables.py` : une série
tirée des paramètres se crée par la même voie, sans que le module de figure lise le modèle).

| Figure | Chapitre | Contenu | Série ou source | État |
|---|---|---|---|---|
| `fig-cnss-allocations-familiales` (existe) | 3 | dépense de prestations familiales de la CNSS, 1990-2004, trois vues | `cnss-retrospective-ressources-emplois`, `ins-annuaire-ipc`, `irpp-ratios` | existe ; base à passer à 2025 ; note de lecture à resserrer |
| `fig-pnafn-allocation` (existe) | 5 | allocation du PNAFN, 1987-2018 | `pnafn-allocation`, `ipc-pnafn-base1987` | existe ; à fondre dans `fig-nc-aide-permanente` |
| **`fig-pf-montant-max`** | 3 | allocation familiale maximale par enfant et par trimestre (1er rang ; foyer de trois enfants), courants et dinars de 2025, 1962-2025 | paramètres `prestations/contributives/prestations_familiales/af/{taux/enf1..4,plaf_trim,nb_enfants_max}` (quatre états datés et sourcés) ; IPC | **faisable maintenant** (série à écrire par le générateur ; aucune donnée nouvelle) |
| **`fig-pf-plafond-smig`** | 3 | plafond de l'assiette trimestrielle rapporté au SMIG trimestriel (48 h), 1961-2026 | `af/plaf_trim` ; `marche-travail-smig-smag` (cache, depuis le 1er avril 1961) | **faisable maintenant** |
| **`fig-pf-msu-creche-reel`** | 3 | majoration pour salaire unique (trois montants), contribution de crèche, indemnité familiale du secteur public (1er enfant), en dinars de 2025 depuis leur date de fixation | `salaire_unique/enf1..3`, `creche/montant`, `retraite/cnrps/accessoires/indemnites_familiales/rang_1..4` ; IPC | **faisable maintenant** ; la légende dit « aucun texte de revalorisation identifié », avec l'ancre `RECHERCHE` |
| *(pas de figure nouvelle)* indemnités de maladie, de couches et de décès de la CNSS, 1990-2004 | 4 | — | `cnss-retrospective-ressources-emplois` ; déjà tracées ligne par ligne par `fig-cnss-assurances-sociales` (livre des caisses, vérifié dans `caisses/figures/cnss_assurances_sociales_1990_2004.py`) | **renvoi entre livres**, nombres datés dans le texte ; 1999 en partie estimé |
| *(pas de figure nouvelle)* indemnités de licenciement et maintien des prestations familiales, 1997-2004 | 4 | — | même série, régime « PST » ; déjà tracées par `fig-cnss-atmp-pst` (vérifié dans `cnss_atmp_pst_1995_2004.py`) | **renvoi entre livres** |
| **`fig-nc-aide-permanente`** | 5 | aide mensuelle permanente, 1987-2026 : paliers du PNAFN et base du transfert Amen, courants et dinars de 2025 ; vue en proportion du SMIG mensuel | `pnafn-allocation` (cache) ; `amen_social/allocation_base` (six paliers sourcés) ; IPC ; `marche-travail-smig-smag` | faisable **après** relèvement de la version minimale du modèle à 0.124 et écriture de la série par le générateur ; aucune donnée nouvelle |
| **`fig-nc-seuils-dinars`** | 5 | plafonds de ressources de l'Amen social en dinars par mois, selon la taille du ménage, 2020-2026, et base du transfert | `amen_social/eligibilite/*` × SMIG | faisable après D2 (quel régime de salaire minimum) |
| **`fig-nc-beneficiaires`** | 5 | bénéficiaires du transfert mensuel : stock de décembre, entrées, sorties, 2018-2023 | `tunisia-data` : `mas-amen-social-2023-beneficiaires-bruts` | faisable **après instantané** (`figtools.refresh_cache`, catalogue) et clé de bibliographie pour le rapport du ministère ; trois totaux 2023 à dire |
| **`fig-nc-credits`** | 5 | crédits de l'Amen social par intervention, 2021-2023, MD courants et % du PIB | `mas-amen-social-2023-credits-bruts` ; PIB : `cnat-pib-nominal` ou `pib-courant-enchaine` (base à dire, renvoi à l'annexe du PIB) | faisable après instantané ; trois points seulement : à présenter en tableau si la figure paraît maigre |
| **`fig-nc-enfants`** | 5 | enfants aidés, 0-5 ans (2022-2023) et 6-18 ans (2023), et crédits | même fichier | après instantané et D4 |
| **`fig-prest-frise`** | 1 | frise des naissances de dispositifs, 1944-2026 | dates des tableaux de ruptures | **à décider** : aucun composant de frise n'existe dans `scripts/` (constat déjà fait au chantier TVA) ; à défaut, le tableau court de l'index |

Séries **à documenter d'abord** (rien n'est extrait) : effectifs des cartes de soins ; allocataires
et enfants des allocations familiales contributives ; dépense de prestations familiales avant 1990
et après 2004 ; indemnités de maladie et de maternité depuis 2007 (CNAM) ; bénéficiaires du PNAFN
avant 2018 (le rapport de 2023 donne des répartitions de 2013) ; rapports de la Banque mondiale et
de l'UNICEF du 9 octobre 2026 (PDF rangés, non dépouillés pour deux d'entre eux, sans clé).

---

## 6. Tableaux faits main à engendrer, et constats pour `backlog-modele.md`

### 6.1 À engendrer

| Tableau fait main | Paramètres existants | Ce qui manque |
|---|---|---|
| Plafonds de ressources de l'Amen social (4 lignes) | `amen_social/eligibilite/*` (0.123.1) | une fonction du générateur ; version minimale |
| Aide de rentrée scolaire, 50 → 100 D (1 ligne) | `aides_ponctuelles/scolarite/rentree_scolaire` : 50 D en 2020 et 2022, **pas de valeur au 1er septembre 2024** | le palier de 100 D (arrêté du 10 juillet 2025, lu dans l'édition arabe) au modèle |
| Plafonds de ressources de la carte à tarifs réduits (3 lignes) | aucun (`non_contributives/amg2` ne porte que le droit annuel de 10 D) | paramètres à créer ; tableau toléré fait main, avec son `TODO (rédacteur)` |
| Capital-décès du secteur public, taux selon l'âge du retraité (5 lignes) | `retraite/cnrps/capital_deces/{taux_retraite_selon_age,majoration_par_enfant,multiplicateur_deces_accidentel,plafond_anciennete_mois}` | une fonction du générateur (le tableau est replié : priorité basse) |
| Indemnité de décès du privé, multiplicateurs (5 lignes) ; indemnités de maladie et de couches (taux, carence, stage) ; accidents du travail (deux tiers, 50 / 40 %) | aucun paramètre de prestation repéré sous `prestations/contributives/` hors prestations familiales | à créer au modèle ; tolérés faits main |
| Droit d'affiliation et tickets de l'assistance médicale, 1988 et 1991 (6 lignes) | aucun | replié ; toléré fait main |
| Aides catégorielles des lois de finances pour 2025 et 2026 (5 lignes) | aucun | après lecture (D7) |

Tableaux engendrés à régénérer après relèvement de la version : `amen_base`, `amen_supplement_enfant`,
`amen_vs_afnc` (dates du 25 mai 2020 ; palier de 2026 ; clés `CLES_AMEN`, `CLES_SUPPLEMENT` à
rekeyer ; trois clés de bibliographie à créer : arrêté du 21 avril 2026, décret n° 2025-426, arrêté
du 3 novembre 2025). Ne rien régénérer depuis une branche non fusionnée du modèle. Vérifié le 9 octobre
2026 : la version 0.124 est publiée sur PyPI (0.125 aussi) et porte, à son étiquette, les plafonds
datés du 25 mai 2020, l'allocation des 6-18 ans et le palier de 280 D ; la borne à relever est donc
(0, 124).

### 6.2 Constats pour `docs/notes/backlog-modele.md` (à y inscrire par le rédacteur ou le modéliste ; je n'y écris pas)

1. `prestations/non_contributives/allocation_familiale` : valeur datée du **8 avril 2022**, jour de
   publication, sans lien ni citation d'article ; la convention suivie depuis 0.123.1 pour le reste
   de l'Amen social (date exécutoire, cinq jours après le dépôt ; éditions française et arabe)
   n'y est pas appliquée.
2. `amen_social/aides_ponctuelles/scolarite/rentree_scolaire` : pas de palier de 100 D au
   1er septembre 2024 (arrêté du 10 juillet 2025, art. 1 et 3).
3. `pnafn/allocation` : la notice s'arrête à l'arrêté du 29 août 2025 ; l'arrêté conjoint du 5 août
   2026 n'y figure pas. Les onze paliers restent sans source (issue 462, déjà au backlog).
4. `amen_social/decile` : référence à une circulaire hébergée hors du *Journal officiel*, sans date
   exécutoire établie ; valeur à qualifier.
5. `amen_social/eligibilite/handicap_lourd/*` : valeurs « déduites du texte » selon la notice
   elle-même ; à rapprocher de la lecture du documentaliste (D3) avant tout tableau.
6. `non_contributives/amg2` : le paramètre est une cotisation ; les plafonds de ressources de
   l'art. 2 du décret n° 98-409 (1 ; 1,5 ; 2 salaires minimums) n'ont pas de paramètre.
7. Aucun paramètre pour les indemnités de maladie, de couches, de décès du secteur privé ni pour
   la réparation des accidents du travail.

---

## 7. Ce qu'il faut lire avant d'écrire : ticket du documentaliste

Borné : quatorze questions, sur des textes localisés. D0 à D3 et D11 conditionnent le chapitre 5.

- **D0. Note complémentaire à verser dans `prestations-assistance.md`.** Quatre faits que le plan
  emploie ne sont aujourd'hui sourcés **que dans les notices des paramètres du modèle**, dans aucune
  note documentaire : (a) le 25 mai 2020, date où le décret gouvernemental n° 2020-317 et les
  arrêtés du 19 mai 2020 deviennent exécutoires (dépôt du fascicule n° 45 le 20 mai) ; (b) le
  palier de 280 D au 1er janvier 2026 (arrêté conjoint du 21 avril 2026, JORT n° 40, p. 786) ;
  (c) le décret n° 2025-426 du 2 octobre 2025 (JORT n° 121, p. 2518) et l'arrêté conjoint du
  3 novembre 2025 (JORT n° 132, p. 2963) sur l'allocation des 6-18 ans ; (d) la lecture de
  l'art. 7 pour la majoration de handicap (voir D3). Le rédacteur travaille sous « aucun fait
  nouveau hors de la note » : chaque texte doit y entrer avec article, page et édition.

- **D1.** Arrêté conjoint du 5 août 2026 modifiant l'arrêté du 10 juillet 2024 (JORT n° 80,
  p. 1611-1612) : article, montant plafond (280 D ?), date d'effet. Y a-t-il des arrêtés analogues
  entre août 2025 et août 2026 ?
- **D2.** Décret gouvernemental n° 2020-317, art. 5 : quel salaire minimum (régime de 48 ou de
  40 heures) ? La notice du paramètre dit que le texte ne le précise pas ; une circulaire ou le
  formulaire de demande le dit-il ?
- **D3.** Même article, troisième alinéa, et art. 7 : la majoration d'un demi-salaire minimum pour
  handicap lourd s'applique-t-elle aux quatre paliers ? Relire dans les deux éditions et dire si la
  note documentaire (§ 3.2 de `prestations-assistance.md`, « portée ambiguë ») doit être corrigée.
- **D4.** Rapport de suivi 2023 du ministère des Affaires sociales, p. 36-38 du PDF : sur quel
  fondement des enfants de 6 à 18 ans sont-ils aidés en 2023 (supplément de 10 D ? aide de
  rentrée ? autre) ? Relever les libellés mot pour mot.
- **D5.** Circulaire n° 12 du 12 mai 2022 (seuil de score) : nature, auteur, objet ; établie ou non.
- **D6.** **Les rubriques et intitulés** sous lesquels les textes rangent les articles des
  ruptures, mot pour mot : loi n° 60-30 (titres et chapitres des art. 51-67 et 68-91) ; loi
  n° 75-82 (intitulé, et exposé s'il en est) ; loi n° 80-36 ; loi n° 88-38 et loi n° 88-39 ; loi
  n° 94-88 ; loi n° 94-28 (art. 1er) ; loi n° 95-56 ; loi n° 96-101 (intitulé) ; loi n° 2004-71
  (art. 1er) ; loi n° 2024-44 (intitulé, art. 1er) ; loi n° 87-29 ; décrets n° 98-409 et 98-1812
  (intitulés) ; décret-loi n° 2022-8 ; décret n° 2025-426.
- **D7.** Lois de finances pour 2025 (art. 26 — l'extrait français local existe) et pour 2026
  (art. 35, 71, 81, 96) : lire, donner articles, montants, dates d'effet, édition.
- **D8.** Aides aux personnes âgées et handicapées (arrêtés du 30 septembre 1997, du 12 décembre
  2003, du 1er juin 2006, du 28 avril 2017 — quatre fascicules français locaux) : montants datés.
  Facultatif pour la conversion ; nécessaire pour ouvrir une section.
- **D9.** Dates d'effet non établies : lois n° 96-65, n° 96-101, n° 2002-32, n° 2002-104 ; décrets
  n° 95-1166, n° 89-107 ; décret-loi n° 2024-4 ; date d'effet des art. 68 à 98 de la loi n° 60-30.
- **D10.** Décret de gestion du fonds de l'art. 17 de la loi de finances pour 2025 : rejouer la
  fiche `r-lf2025-art17-decret` à la date de la conversion.

- **D11.** Supplément de 10 D par enfant (arrêté du 19 mai 2020, art. 2, modifié en 2022) et
  allocation de 30 D des 6-18 ans (arrêté du 3 novembre 2025) : un texte, une circulaire ou un
  document du ministère dit-il s'ils se cumulent ou si l'une remplace l'autre ? À défaut, constat
  et fiche `RECHERCHE`.
- **D12.** Lois modifiant les art. 52, 54 et 61 de la loi n° 60-30, la majoration pour salaire
  unique et la contribution de crèche, de 2007 à 2026 : prolonger le dépouillement de la note (R2,
  arrêté à 2007) et dater la couverture des fiches `RECHERCHE`.
- **D13.** (Hors conversion.) Prestations de soins du régime de base d'assurance maladie :
  filières, taux de prise en charge, plafonds — textes d'application de la loi n° 2004-71.

Dans D4, ajouter : l'unité du total de 2023 (« personnes » au tableau des flux, « ménages » au
tableau du classement par le score).

Hors ticket, déjà au backlog : décret du 8 juin 1944 ; décret n° 75-952 ; circulaire n° 42 de 1996 ;
loi n° 82-71 ; décrets n° 93-529 et n° 94-1738 ; pagination des textes de 2024 et après.

Au bibliographe : clés à créer pour l'arrêté du 21 avril 2026, le décret n° 2025-426, l'arrêté du
3 novembre 2025, le rapport de suivi 2023 du ministère des Affaires sociales ; plus tard, les huit
pièces de la Banque mondiale et de l'UNICEF si A6 leur ouvre une section.

---

## 8. Désaccords de classement possibles et risques du plan

- **1976 aux prestations familiales** : rupture ou ajustement (§ 3.3, A3).
- **1998 à l'aide médicale** : rupture du chapitre ou de la seule fiche (§ 3.5.2).
- **2025, allocation des 6-18 ans** : étape de 2022 ou rupture (§ 3.5.2).
- **1986 comme « mise en place »** : aucun texte ne crée le programme ; la date retenue est celle de
  sa première trace publiée. Le chapitre doit le dire ainsi, sans dater la création.
- **Travailleuses agricoles (2024)** : étape de la réforme de 1995 (un public de plus) ou rupture
  (régime propre, cotisations prises en charge par l'État trois ans — un financeur nouveau). Classée
  étape ; à promouvoir si le propriétaire veut que 2024 soit lue comme une réforme d'ensemble
  (congés + travailleuses agricoles).
- **Handicap lourd (D3)** : le modèle et la note documentaire ne disent pas la même chose ; le plan
  s'en tient à la note tant que le documentaliste n'a pas tranché.
- **Ce que le repli pourrait cacher à tort.** (1) Le tableau des onze paliers du PNAFN : replié,
  parce que la figure le montre et qu'aucun palier n'a de texte ; son titre doit dire « montants »
  et ses bornes. (2) Les tarifs réduits de 1998 : ce sont des paramètres de la législation en
  vigueur jusqu'en 2022 ; le plafond de ressources reste au premier plan, les tarifs se replient
  sous un titre explicite. (3) La procédure de l'Amen social : repliée, mais « le transfert est dû à
  compter du mois de la demande » et « mise à jour tous les deux ans » commandent la dépense et
  restent au premier plan. (4) Le capital-décès public : son mode de calcul reste en une phrase au
  premier plan, le tableau par âge se replie. (5) Les congés d'allaitement : repliés avec le
  tableau entier.
- **Le retrait des trois tableaux de cotisation** (A5) fait perdre à ce volume trois tableaux
  engendrés ; ils subsistent au livre des cotisations, sous les mêmes étiquettes.
- **Le livre arabe** : deux chapitres de moins et un ordre changé ; son `_quarto.yml` s'édite à la
  main, la traduction étant différée. Tant qu'il n'est pas édité, `rendre-les-livres.yml` signale
  la dérive.
- **La cible de mots de l'assistance** suppose que la matière nouvelle (280 D, 6-18 ans, arrêté de
  2026, bénéficiaires, crédits) tienne en 500 mots : c'est le chapitre où le premier plan risque le
  plus de regrossir.

---

## 9. Arbitrages soumis au propriétaire

| # | Question | Recommandation | Ce que l'autre choix coûte |
|---|---|---|---|
| A1 | **Fusionner `_contributives` dans le chapitre de la matrice et remonter celui-ci en deuxième position ?** | **Oui.** La matrice dit qui a droit ; elle ouvre les chapitres de risques. | Non : un chapitre de 392 mots reste, la matrice reste en fin de volume ; aucun renvoi à toucher. Oui : 1 renvoi interne, deux `_quarto.yml`. |
| A2 | **Garder `_autres_risques` et `_non_contributives` en un fichier chacun, avec une section par risque ou par dispositif ?** | **Oui.** Les cinq liens entrants restent valides ; le fil chronologique de l'assistance (du PNAFN à l'Amen social) reste d'un seul tenant. | Scinder : 2 liens à corriger au marché du travail, 3 fichiers de plus dans les deux `_quarto.yml`, trois chapitres arabes à créer. |
| A3 | **1976 (taux dégressifs par rang) : grande réforme des allocations familiales ?** | **Non : ajustement majeur**, présenté dans l'entre-temps avec la figure. La loi ne change ni le public ni le financeur, et son objet n'est pas relevé. | Oui : une cinquième ligne au tableau des ruptures, sans « ce que la loi cherche » tant que D6 n'a pas répondu. |
| A4 | **Dinars constants de 2025 pour tout le volume, par le déflateur du marché du travail, y compris les deux figures existantes (bases 1990 et 1987) ?** | **Oui.** Une seule année de base dans le volume ; le déflateur est remonté dans `scripts/`. | Non : trois années de base dans un même volume ; aucun recalcul des notes de lecture. |
| A5 | **Retirer de ce volume les trois tableaux de cotisation (assurance maladie des agents publics, prévoyance des pensionnés, fonds de perte d'emploi) et renvoyer au livre des cotisations ?** | **Oui.** Ce volume parle de ce qui est servi ; les taux y tiennent en une phrase avec un lien. | Non : trois tableaux engendrés de plus au premier plan, sur un sujet traité ailleurs. |
| A6 | **Ouvrir dès cette conversion une section « Études et rapports extérieurs » sur l'Amen social (Banque mondiale 2021-2026, UNICEF 2024) ?** | **Non, pas maintenant.** Les pièces sont rangées mais non dépouillées ; la longue période se construit sur le rapport du ministère. Un `TODO` les signale. | Oui : un passage de documentaliste par pièce (méthode, données, périmètre), huit clés de bibliographie, et la doctrine de leur place à fixer d'abord. |

Arbitrages pris par défaut, à renverser au besoin : l'annexe des notations est supprimée ; le
secteur public remonte avant la longue période dans le chapitre des prestations familiales ; les
titres de réforme portent l'année d'effet ; l'index n'est pas en `.domicile-unique` (il garde
l'encadré des caisses, engendré et partagé) ; l'allocation des 6-18 ans est une étape de 2022.

---

## 10. L'ordre de travail et le volume estimé

Une PR par chapitre, chacune avec sa copie de départ mesurée, `scripts/check_domicile_references.py`,
`scripts/verifier.sh --sans-reseau prestations_sociales` (et `cotisations_sociales` quand un lien
entre livres est touché), rendu ouvert dans le navigateur.

| # | PR | Préalables | Rôles | Durée estimée |
|---|---|---|---|---|
| 0 | Préparation : déflateur partagé ; version minimale du modèle à 0.124 ; trois clés de bibliographie ; régénération des tableaux de l'Amen social ; instantané des deux séries du ministère ; constats au `backlog-modele.md` | arbitrages A4 ; réponses D1 à D3 souhaitables | bibliographe, tâche mécanique | 1 h |
| 1 | Ticket du documentaliste D0 à D7, D11, D12 (D8 à D10 et D13 en second) | — | documentaliste | 1 h 30 à 2 h |
| 2 | **Assistance sociale** (`_non_contributives`) : c'est le chapitre périmé et le plus lourd ; trois à cinq figures nouvelles | PR 0, D0 à D5, D7, D11 | rédacteur, puis domicile unique | 2 h |
| 3 | **Prestations familiales** : trois figures faisables tout de suite | A3, A4 ; D6 pour les objets | rédacteur | 1 h 15 |
| 4 | **Maladie, maternité, décès, accidents du travail, perte d'emploi** | A5 ; D6, D9, D10 | rédacteur | 1 h 30 |
| 5 | **Index, régimes et prestations, suppression de `_contributives` et de `_notations`** ; les deux `_quarto.yml` | A1 ; en dernier, pour que l'index cite les montants et les sections définitifs | rédacteur | 45 min |

Volume : six PR, environ **8 h à 8 h 30** de travail d'agents, hors relecture du propriétaire ;
premier plan de 14 600 à environ 10 150 mots ; une trentaine de blocs repliés ; 6 à 8 figures
nouvelles, dont trois faisables tout de suite sans aucune donnée nouvelle (prestations familiales)
et une quatrième dès la version minimale relevée (aide permanente 1987-2026). La PR 3 peut partir avant le ticket du
documentaliste (les objets « non relevés » s'y écrivent en `TODO`), si le propriétaire veut voir un
chapitre converti au plus tôt.

---

## 11. Liste de contrôle pour le rédacteur

- Copie de départ hors du dépôt ; mesures du § 1.1 refaites ; à l'arrivée : toutes les clés, tous les
  couples (clé, localisateur), toutes les ancres de glossaire, tous les identifiants, les 12 `TODO`,
  les 4 `RECHERCHE` ; chaque manque justifié.
- Aucun fait nouveau hors des réponses du ticket et des paramètres régénérés.
- Tournures à retirer : « s'en tient à », « hors de son périmètre », « ne relèvent pas du
  périmètre », « ce chapitre ne tranche pas », « il faut en tirer une correction de chronologie »,
  « dérivé », « attestation », « date encodée », « texte établi / référence ».
- « Aucun texte de revalorisation n'est identifié ici », jamais « gelé » ni « inchangé depuis ».
- Tout montant cité dans une phrase d'essentiel renvoie à son tableau daté ou à sa figure.
- L'état du droit se dit « en 2026 » ; la réserve d'absence de texte postérieur s'écrit une fois,
  avec son ancre.
- Le sujet des phrases est l'État, la caisse, le ménage, le salarié — pas « le décret ».
- Les deux `_quarto.yml` (français, arabe) édités à la main à la PR 5 ; rien sous `precis/ar/*.qmd`.
- `docs/notes/backlog-precis.md` tenu à jour à chaque PR (tâches closes, lacunes nouvelles).

# TVA — fiche de plan de l'architecte

> Fiche de **plan**, non de rédaction. Rôle : `docs/agents/architecte.md`, à l'essai (chantier
> `docs/notes/chantier-ruptures-au-premier-plan.md`). Établie le 7 octobre 2026 sur la branche
> `chantier/ruptures-au-premier-plan`.
>
> Objet : la réorganisation de `precis/fr/fiscalite/_tva.qmd` (433 lignes, ≈ 11 000 mots).
> Matière : le chapitre lui-même et les trois notes `fiscalite-tva-documentation.md` (ci-après
> **N1**), `fiscalite-tva-reformes.md` (**N2**), `fiscalite-tva-deductions-documentation.md`
> (**N3**). Aucun texte de loi n'a été relu ; aucun fait n'est ajouté. Les numéros de ligne
> renvoient à l'état du chapitre sur cette branche.
>
> La consigne du rôle demande d'écrire la fiche « à la suite de la note documentaire ». Il y a
> ici trois notes : la fiche est un fichier à part, à la demande du propriétaire (voir § 8).

Degrés de lecture repris des notes, tels quels : **[image]**, **[texte]**, **[OCR]** (à relire
à l'image avant citation littérale), **[AR]** (édition arabe seule), **[notice]** (seul
l'intitulé est connu), **[code]** (relevé sur le code consolidé, non lu au JORT),
**[probable]** (décrets annuels dont la clause de durée n'est pas lue). Un texte [notice],
[code] ou [probable] ne porte aucune rupture.

---

## 1. Le parti pris, en dix lignes

1. Le chapitre garde **un seul fichier** et son identifiant `#sec-tva`. Le scinder imposerait
   de déclarer de nouveaux chapitres à la main dans le `_quarto.yml` arabe ; rien ne le justifie.
2. Les trois parties qui se répètent — « L'architecture posée en 1988 », « L'évolution, réforme
   par réforme », « La longue période » — disparaissent **comme titres**. Leur contenu est
   redistribué, sans perte (§ 4).
3. **Récit A, le droit.** D'abord une vue d'ensemble : ce que fait la taxe, puis **quatre
   ruptures** de la taxe prise comme un tout, en un tableau court et un récit bref. Ensuite le
   droit **dispositif par dispositif** : onze sections bâties sur le même gabarit.
4. **Gabarit d'une section de dispositif** : (a) l'essentiel en une phrase ; (b) la vue
   d'ensemble — figure si elle existe, sinon tableau des ruptures du dispositif ; (c) deux à
   quatre points sur ce qui change ; (d) l'état du droit quand il est établi ; (e) un bloc
   `.chronologie-repliable`, entier, dans l'ordre des dates, avec la colonne « Portée ».
5. Le bloc replié est le **registre des textes du dispositif** : c'est là, et là seulement, que
   chaque texte paraît avec sa référence complète (texte, article, page). Le plan est
   compatible avec la règle du domicile unique, au grain « texte + article » (§ 7.3).
6. Les sections « Les générations de taux » et « Le crédit et sa restitution », déjà au gabarit,
   sont **conservées telles quelles** et servent de modèle.
7. **Récit B, la longue période**, ne redit aucun taux : ce que la taxe rapporte, sa place dans
   la fiscalité indirecte, l'assiette sur laquelle elle porte, ce qui lui échappe. Il se
   construit sur le budgétaire.
8. Les rapports extérieurs et les études **restent où ils sont** (décision du propriétaire du
   7 octobre 2026, consignée dans la note du chantier pendant ce travail) :
   `#sec-tva-credit-donnees` et `#sec-tva-credit-etudes` ne bougent pas ; aucune section
   d'incidence n'est ouverte.
9. Aucun `tbl-`, `fig-` ou `sec-` existant ne change de nom. Les renvois entrants
   (`index.qmd` : `@sec-tva`, `@fig-tva-rendement` ; `_depenses_fiscales.qmd` : `@sec-tva`)
   restent valides.
10. Ce que le plan ne peut pas fournir : un « état du droit en 2026 » de l'ensemble de la taxe.
    Le tableau A en vigueur n'est pas dépouillé (N1, § 5, points 5 et 6). L'état du droit est
    donc donné dispositif par dispositif, là où les notes l'établissent.

---

## 2. Le plan

`P` = premier plan ; `R` = replié (titre du bloc entre guillemets) ; `=` = repris tel quel.
Les identifiants nouveaux sont proposés ; les anciens sont conservés.

### `# La taxe sur la valeur ajoutée (TVA) {#sec-tva}`

- **Chapeau** (`=`, l. 3). Établit : le code de 1988, son lien avec le droit de consommation.
- **Encadré « Comment les dates sont-elles lues dans ce chapitre ? »** (`=`, l. 5-11). P,
  déplié : il porte la seule mention de premier plan du fait générateur.

### `## Des taxes sur le chiffre d'affaires à la TVA {#sec-tva-origine}`

Établit ce que la taxe remplace et comment la transition est ménagée. `=` (l. 13-17). P, court.

### `## Ce que fait la taxe {#sec-tva-mecanisme}` — section nouvelle, bâtie sur l'existant

Établit, en une demi-page et sans date autre que 1988 : ce qui est frappé (affaires
industrielles, artisanales, libérales, opérations commerciales autres que les ventes ; les
ventes dans les seuls cas énumérés) ; qui collecte (les assujettis) ; les quatre situations
d'une opération — hors champ, exonérée, taxée à l'un des taux, en suspension ; le principe de la
déduction, en une phrase qui renvoie à `@sec-tva-deduction`. Matière : l. 23-25, 44, 66, 70,
193. Aucun fait nouveau. P. Pas de bloc replié.

Ce que la section ne fait pas : décrire le champ en vigueur poste par poste (non établi).

### `## Quatre ruptures et leur mise en œuvre {#sec-tva-ruptures}`

Établit ce que la loi a cherché à faire de la taxe, quatre fois (§ 3.1).

- P : une phrase d'essentiel ; le **tableau des ruptures** `tbl-tva-ruptures` (quatre lignes ;
  colonnes du prototype : rupture et date ; ce que la loi cherche ; avant → après ; mise en
  œuvre, étape par étape) ; sans citation, il renvoie aux registres des dispositifs.
- P : le récit, un paragraphe à trois par rupture, les textes nommés en mots :
  - `#### 1988 : une taxe unique, appliquée par étapes` — avec `@tbl-tva-calendrier` (court,
    il reste au premier plan) ;
  - `#### 1996 : la taxe atteint le commerce de détail` ;
  - `#### 2007 : la fin du taux majoré, la restitution intégrale` ;
  - `#### 2016-2017 : moins d'exonérations, un champ plus large` ;
  - un paragraphe de clôture : depuis 2018, trois taux stables et un périmètre qui bouge
    (matière : l. 106, 110, 148).
- R : rien ici. Le détail est dans les registres des dispositifs, auxquels chaque paragraphe
  renvoie par `@tbl-…` (le renvoi déplie le bloc).

### `## Le droit, dispositif par dispositif {#sec-tva-dispositifs}`

Une phrase d'entrée dit le gabarit et que chaque bloc replié est le registre complet des textes
du dispositif.

#### `### Le champ et les assujettis {#sec-tva-champ}`

Établit qui entre dans la taxe, et quand.

- P : l'essentiel (le champ s'étend de la production et des services, en 1988, au gros en 1989
  et au détail en 1996 ; il se resserre ou s'élargit ensuite par opérations) ; renvoi à
  `@tbl-tva-calendrier` ; trois points : 1989 le gros, 1996 le détail et son seuil de
  100 000 dinars, 2016-2017 les opérations sorties de l'exonération ; le constat sur les
  grossistes en alimentation générale, **avec son ancre `RECHERCHE`** (l. 38-40, inséparables).
- P : les assujettis en deux phrases (l. 44).
- R « Le champ et les assujettis, texte par texte, de 1988 à 2022 » : `tbl-tva-champ-textes`,
  avec la colonne « Portée ». Registre des textes du dispositif (§ 5.1).
- R « L'option et le fait générateur dans la rédaction de 1988 » : l. 46 (option) et l. 48-62
  (`tbl-tva-fait-generateur` et son paragraphe). Modalités pour lecteur spécialisé ; le bloc
  garde ses citations des articles 2 et 5 (exception au domicile unique, § 7.3).

#### `### Les taux {#sec-tva-taux}` — ancien « Les générations de taux »

Établit les grilles successives. **Déjà au gabarit** (l. 114-173) : `=`.

- P : l'essentiel, `@fig-tva-taux`, les quatre points.
- P, ajout : un paragraphe sur ce que contenaient les tableaux B et C en 1988 (l. 68), que la
  figure ne montre pas.
- R « Les six grilles, texte par texte, de 1988 à 2026 » : `=` (`tbl-tva-taux`, engendré, donc
  sans colonne « Portée » ; la hiérarchie reste dans la liste qui le suit). Registre des textes
  qui changent **la grille**.
- R, nouveau, « Les opérations qui changent de taux, texte par texte, de 1989 à 2026 » :
  `tbl-tva-taux-perimetre`, fait main, avec « Portée ». Registre des textes qui déplacent une
  opération d'un taux à l'autre sans toucher à la grille (§ 5.2).

#### `### Les exonérations {#sec-tva-exonerations}`

Établit ce que le tableau A soustrait à la taxe, et le mouvement de 2016-2017.

- P : l'essentiel ; le contenu du tableau A d'origine (l. 70) ; deux points : des ajouts
  presque annuels de 1989 à 1995, la réduction de 2016-2017. Une phrase dit que l'état du
  tableau A en vigueur n'est pas établi ici, avec un `TODO (documentaliste)`.
- R « Les exonérations, texte par texte, de 1988 à 2021 » : `tbl-tva-exonerations-textes`.
  Registre (§ 5.3). Les lignes [OCR] et [notice] y sont signalées par un commentaire caché et
  ne se publient qu'après relecture.

#### `### Des trajectoires différentes selon les opérations {#sec-tva-trajectoires}`

Établit, opération par opération, la suite complète des régimes. `=` pour les deux paragraphes
existants (l. 177-179), complétés de ce que le chapitre dit ailleurs.

- P : l'essentiel ; un tableau court `tbl-tva-trajectoires` — une ligne par opération, les
  régimes successifs et leurs dates : professions libérales ; logement vendu par les
  promoteurs ; télécommunications ; médicaments au détail ; hôtellerie et restauration ;
  électricité domestique (renvoi à la section suivante).
- P : deux à quatre points — les professions libérales (cinq régimes), le logement (trois
  temps, trois reports), les télécommunications (exonérées en 1995, taxées en 2003), les
  médicaments au détail (aller et retour, 2016-2021).
- R « Les trajectoires, texte par texte » : `tbl-tva-trajectoires-textes`. Registre (§ 5.5).
  Les textes qui y figurent ont leur domicile ici quand ils ne concernent qu'une opération ;
  sinon la ligne renvoie au registre des taux ou du champ.

#### `### Les réductions annuelles par décret {#sec-tva-reductions-annuelles}`

Établit le pouvoir de l'article 8, la série électricité–produits pétroliers et sa fin.

- P : l'essentiel (de 1998 à 2014, un taux réduit reconduit chaque année par décret, parce que
  l'article 8 borne la mesure à l'année civile) ; un tableau des ruptures à deux lignes
  (§ 3.2) ; trois points : la bifurcation du 6 mai 1998, la reprise du 1^er^ août 2004,
  l'inscription au code au 1^er^ janvier 2015. Matière : l. 183-187.
- P : renvoi au chapitre des droits de consommation, domicile du tarif pétrolier
  (`@tbl-dc-petroliers`).
- R « Les textes des réductions annuelles, de 1988 à 2025 » : `tbl-tva-reductions-textes`,
  avec « Portée ». **Registre provisoire**, fait des seuls textes que le chapitre cite déjà
  (l. 183-187) : code, art. 8 ; loi de finances pour 1996, art. 40 ; décrets n° 98-384,
  n° 98-952 et n° 2004-1773 ; loi n° 2006-80, art. 17 ; décrets n° 2007-1 et n° 2007-2 ; loi
  de finances pour 2015, art. 36 ; loi de finances pour 2025, art. 31. Il dit qu'un décret a
  reconduit la réduction chaque année de 1999 à 2014.
- R, à terme, dans le même bloc : `tbl-tva-reductions-annuelles`, le tableau année par année
  de N1, § 4.3. **Condition** : le `TODO (bibliographe)` de la l. 189 est levé (clés CSL) et
  les sept décrets [probable] sont lus. D'ici là, le TODO reste à sa place et la chronologie
  de ce dispositif n'est **pas complète** (§ 7.2).

#### `### Les petits contribuables : forfaits et taxe sur la marge {#sec-tva-forfaits}`

Établit ce que la loi fait des petites entreprises : un forfait de TVA, puis leur sortie de la
taxe.

- P : l'essentiel ; trois points : les forfaits du code différés en 1988 et remplacés par la
  loi de finances pour 1990 ; l'impôt forfaitaire sur le revenu rendu libératoire de la TVA
  par la loi de finances pour 1993 ; le forfait des transports récrit en 1998. Matière :
  l. 76-80. La phrase « sans date d'effet plus précise » est conservée.
- R « Les forfaits, texte par texte, de 1988 à 2016 » : `tbl-tva-forfaits-textes`. Registre
  (§ 5.6).

### `## Déduction, crédit et suspension {#sec-tva-deduction}`

Chapeau `=` (l. 193).

#### `### Le droit à déduction {#sec-tva-droit-deduction}`

- P : l'essentiel ; le principe de l'article 9 (l. 197) ; trois points : les deux exclusions de
  1988 et leur déplacement en 1998 ; l'exclusion des achats en espèces, 2014-2016 ; la
  déduction de la retenue à la source et la plateforme de 2022.
- R « Le pourcentage de déduction et la régularisation » : l. 203-211, formule comprise, `=`.
  Bloc de modalités, non registre : il garde ses citations de l'article 9, par exception à la
  règle du domicile unique (§ 7.3).
- R « Le droit à déduction, texte par texte, de 1988 à 2022 » : `tbl-tva-deduction-textes`.
  Registre (§ 5.7).

#### `### Le crédit et sa restitution {#sec-tva-credit-restitution}`

**Déjà au gabarit** : `=` (l. 213-272), avec `#### Trois ruptures et leur mise en œuvre
{#sec-tva-restitution-ruptures}` et `#### L'état du droit en 2023 et la chronologie complète
{#sec-tva-restitution-chronologie}`. Le bloc replié `tbl-tva-restitution` est le registre.
Quatre textes de N3 n'y figurent pas (§ 5.8) : à ajouter ou non, au choix de la revue.

#### `### Le régime suspensif {#sec-tva-regime-suspensif}`

- P : l'essentiel (l. 277, la suspension empêche le crédit de naître et le déplace vers le
  fournisseur) ; un tableau des ruptures à deux lignes, ou trois selon la lecture (§ 3.2) ;
  le récit : le texte de 1988 (l. 279), le seuil de 2017, le resserrement de 2022 (l. 285) ;
  la phrase qui lie suspension et restitution (l. 304) ; l'état du droit après 2022.
- P : renvoi à `@sec-depenses-fiscales` pour les régimes d'incitation (l. 283, fin).
- R « Le régime suspensif, texte par texte, de 1988 à 2024 » : un seul registre, qui absorbe
  `tbl-tva-suspension-sectorielle` (identifiant **conservé** pour le tableau des régimes
  propres à certaines opérations, placé dans le bloc) et y ajoute `tbl-tva-suspension-textes`
  pour l'article 11 lui-même (§ 5.9).
- Le paragraphe sur l'absence de coût publié (l. 306) **part au récit B**
  (`#sec-tva-ce-qui-echappe`) ; il en reste ici une phrase et un renvoi.

#### `### La retenue à la source {#sec-tva-retenue-source}` — détachée de l'ancienne section

- P : l'essentiel (l'acheteur public retient une part de la taxe au moment où il paie) ; les
  étapes en une phrase (1998, 2004, 2013, 2016) ; le paragraphe économique `=` (l. 316).
- R « La retenue à la source, texte par texte, de 1998 à 2022 » : `tbl-tva-retenue-textes`.
  Registre (§ 5.10).

#### `### Déclaration et facture {#sec-tva-declaration-facture}`

Identifiant conservé ; la section ne porte plus la retenue.

- P : le rythme de la déclaration (l. 310) ; la facture et la facture électronique (l. 318).
- R « Déclaration et facture, texte par texte, de 1988 à 2026 » : `tbl-tva-declaration-textes`.
  Registre (§ 5.11).

#### `### Ce que pèsent le crédit et sa restitution… {#sec-tva-credit-donnees}` et `### Ce qu'en disent les rapports extérieurs {#sec-tva-credit-etudes}`

Les deux sections restent ici, à leur place et dans leur rédaction (`=`, l. 320-388), avec
`@fig-tva-credit-restitutions`. Elles ne sont pas repliées.

### `## La longue période : ce que la taxe rapporte, et ce qui lui échappe {#sec-tva-longue-periode}`

Récit B, budgétaire d'abord. Détail au § 6.

- `### Ce que la taxe rapporte {#sec-tva-rendement}` — `@fig-tva-rendement`, ruptures marquées.
- `### Sa place dans la fiscalité indirecte {#sec-tva-fiscalite-indirecte}`
- `### La taxe rapportée à la consommation privée {#sec-tva-consommation}` — calcul du
  précis, présenté comme tel.
- `### Ce qui échappe à la taxe {#sec-tva-ce-qui-echappe}` — dépenses fiscales de TVA, par
  forme ; la suspension intermédiaire, sans coût publié.
- Un alinéa de clôture renvoie à `@sec-tva-credit-donnees` : ce que la taxe immobilise dans
  les entreprises.

Les rapports extérieurs et les études ne reçoivent ici aucune place nouvelle (décision du
propriétaire du 7 octobre 2026, `chantier-ruptures-au-premier-plan.md`) : `#sec-tva-credit-donnees`
et `#sec-tva-credit-etudes` restent à la fin de « Déduction, crédit et suspension », et aucune
section d'incidence n'est ouverte.

---

## 3. Les ruptures

### 3.1 Les ruptures de la taxe prise comme un tout

Quatre sont retenues. Chacune s'appuie sur un article lu [image] ou [texte]. « Ce que la loi
cherche » est donné dans les termes du texte quand les notes les relèvent ; sinon la case le
dit.

| # | Rupture, date d'effet | Texte et article | Ce que la loi cherche | Avant → après | Étapes rattachées |
|---|---|---|---|---|---|
| **C1** | **1988 — une taxe unique** ; 1^er^ juillet 1988 | loi n° 88-61 du 2 juin 1988, art. 1^er^, 2 et 5 de la loi de promulgation ; code, art. 1^er^, 7 et 9 [image] ; décret n° 88-1109, art. 1^er^ [image] | réunir « en un seul corps » les textes relatifs à l'imposition du chiffre d'affaires (art. 1^er^ de la loi) | taxe à la production, taxe de consommation et taxe sur les prestations de service du décret du 29 décembre 1955 → une taxe unique, à déduction, à trois taux | application au 1^er^ juillet 1988 hors gros et forfaits ; marchés de travaux conclus avant cette date maintenus sous l'ancienne taxe (art. 4) ; commerce de gros au 1^er^ octobre 1989, alimentation générale exceptée (décret n° 89-1222) |
| **C2** | **1996 — la taxe atteint le détail** ; 1^er^ juillet 1996 | loi de finances pour 1996 (loi n° 95-109), art. 43 à 46 [texte] | objet non relevé par les notes | le commerce de détail ne figure pas dans l'énumération de 1988 → détaillants réalisant au moins 100 000 dinars de chiffre d'affaires annuel global assujettis ; produits alimentaires, médicaments et produits homologués exonérés à la revente | base majorée de 25 % pour les ventes des assujettis à des non-assujettis (art. 44) ; facturation des détaillants (art. 45) ; médicaments retirés de l'exonération au détail (2016, différé à 2017 puis 2020) puis rétablis (2021) ; détaillants en boissons alcoolisées assujettis (2022) |
| **C3** | **2007 — la fin du taux majoré, la restitution intégrale** ; 1^er^ janvier 2007 | loi n° 2006-80 du 18 décembre 2006, art. 13 à 17 et 19 [texte] | intitulé de la loi (N1, § 3.4) : « relative à la réduction des taux de l'impôt et à l'allègement de la pression fiscale sur les entreprises » | trois taux dont un majoré de 29 % ; restitution du crédit plafonnée à 50 % → plus de taux majoré, cinq lignes seulement transférées au droit de consommation ; restitution intégrale dans tous les cas | en amont : retraits successifs du tableau C, 1989-1998 ; restitution à 40 % pour l'investissement (1996), 50 % pour tous (1999), 75 % puis 100 % pour la mise à niveau (2002, 2004). Le même texte porte 10 % à 12 % (art. 17), qui est un ajustement de niveau |
| **C4** | **2016-2017 — moins d'exonérations, un champ plus large** ; 1^er^ janvier 2016 et 1^er^ janvier 2017 | loi de finances pour 2016 (loi n° 2015-53), art. 30, 31 et 33 [texte, PDF local] ; loi de finances pour 2017 (loi n° 2016-78), art. 16, 20, 21 et 24 à 28 [texte] | objet non relevé par les notes | opérations exonérées au tableau A → reclassées à 6 % ou sorties de l'exonération ; tableaux A, B et B bis refondus ; tableau B bis abrogé | enseignement privé au 1^er^ septembre 2016 ; taxe sur la marge étendue aux achats auprès de tout non-assujetti ; ventes de lots par les promoteurs immobiliers ; livraisons à soi-même d'immobilisations incorporelles ; en 2018, exonération du logement limitée au logement social |

**Lectures concurrentes, à faire trancher.**

1. **C2 est-elle une rupture ou la dernière étape de C1 ?** Pour l'étape : le chapitre et
   l'index du livre présentent 1988, 1989 et 1996 comme un seul échelonnement (« la construction
   du champ s'étale sur huit ans », N1). Pour la rupture : le gros était dans le code de 1988,
   seulement différé par décret ; le détail n'y était pas, et il y entre par une loi, avec un
   seuil et une assiette propres — un public nouveau. Retenu ici : rupture. Si la revue retient
   l'étape, le chapitre a trois ruptures et `@tbl-tva-calendrier` suffit à porter 1996.
2. **C3 porte deux choses** : la structure des taux et la neutralité pour l'entreprise. Au
   niveau du chapitre, une seule rupture, parce qu'un seul texte et un seul intitulé. Au niveau
   des dispositifs, elle se dédouble : rupture des taux (T2) et rupture de la restitution
   (« tout restituer », déjà au prototype).
3. **C4 est-elle une rupture ou un faisceau d'ajustements ?** Les notes ne donnent pas l'objet
   que ces lois s'assignent, et le contenu des numéros abrogés du tableau A par la loi de
   finances pour 2017 n'est pas rapproché (N2, § 8, point 4). Elle est retenue sur le fait,
   lisible dans le texte, que des opérations exonérées deviennent taxées en nombre — un public
   nouveau. **Fragile** : à confirmer par le documentaliste (exposé des motifs, intitulés des
   articles) avant d'écrire « ce que la loi cherche ».
4. **Le relèvement d'un point des trois taux, en 2018**, n'est pas retenu : changement de
   niveau, donc ajustement, selon le critère du propriétaire. Il touche pourtant toute la
   taxe ; la revue peut vouloir le voir au tableau des ruptures comme étape.
5. **Non retenues comme ruptures du chapitre, mais ruptures de leur dispositif** : le taux de
   10 % (1995), le gel du crédit (1999), la retenue à la source (1998), les délais de
   restitution (2010), le seuil du régime suspensif (2017). Les faire monter toutes donnerait
   neuf ruptures : le signe, que la consigne du rôle prévoit, que le chapitre couvre plusieurs
   dispositifs.

### 3.2 Les ruptures propres à un dispositif

| Dispositif | Rupture, date d'effet | Texte et article | Ce que la loi cherche | Avant → après | Étapes |
|---|---|---|---|---|---|
| Taux | **T1 — 1995, un taux intermédiaire** ; 1^er^ janvier 1995 | loi de finances pour 1995 (loi n° 94-127), art. 56 à 58 et 100 [texte] | objet non relevé | 17 % / 6 % / 29 % → un taux de 10 % hors du code, pour l'informatique, les téléviseurs et le transport de marchandises, retirés du tableau B | professions libérales (1^er^ avril 1996), hôtellerie et restauration (1^er^ septembre 1996), formation (2000), services Internet (2001) ; entrée dans le code et tableau B bis (2002) ; 12 % (2007) ; liste portée à l'article 7 (2017) ; 13 % (2018) ; liste réduite ensuite (2019, 2023, 2025) |
| Taux | **T2 — 2007, la fin du taux majoré** = C3 | loi n° 2006-80, art. 13 et 14 [texte] | voir C3 | voir C3 | retraits du tableau C de 1989 à 1998 |
| Réductions annuelles | **A1 — 1996-1998, l'électricité et les produits pétroliers hors du taux réduit du code** | loi de finances pour 1996, art. 40 [texte] ; décrets n° 98-384 et n° 98-952 [texte] | objet non relevé | tableau B à 6 % → taux réduit accordé par décret, pour l'année civile (art. 8 du code) | 1^er^ janvier 1998 : 10 % sur certains produits pétroliers, 6 % sur l'électricité domestique ; 6 mai 1998 : électricité à 10 %, produits pétroliers transférés au droit de consommation ; 1^er^ août 2004 : reprise du taux réduit sur les produits pétroliers ; reconductions annuelles jusqu'en 2014 |
| Réductions annuelles | **A2 — 2015, l'inscription dans le code** ; 1^er^ janvier 2015 | loi de finances pour 2015 (loi n° 2014-59), art. 36 et 46 [image] | objet non relevé ; N1 le lit comme le passage d'une mesure annuelle à une mesure permanente | réduction reconduite chaque année par décret → inscription au tableau B bis, à 12 % | liste portée à l'article 7 (2017) ; 13 % (2018) ; irrigation à 7 % (2019) ; électricité domestique à 7 % jusqu'à 300 kWh par mois (2025) |
| Forfaits | **F1 — 1993, l'impôt forfaitaire libératoire de la TVA** ; date d'effet non établie | loi de finances pour 1993 (loi n° 92-122), art. 100 à 105 [image] | intitulé relevé par N2 : « unification et simplification du régime forfaitaire » | taxe forfaitaire annuelle et droit forfaitaire simplifié de TVA (loi de finances pour 1990) → forfait unique dans l'impôt sur le revenu, « libératoire de la taxe sur la valeur ajoutée » ; art. 16 et 17, I, abrogés | taxe sur la marge pour les achats auprès des forfaitaires (1991), étendue à tout non-assujetti (2016) ; forfait mensuel des transports (1998) |
| Restitution | **1999 — apurer le stock** ; **2007 — tout restituer** ; **2010 — restituer vite** | voir `@tbl-tva-restitution-ruptures` | — | — | prototype, non rediscuté ici |
| Régime suspensif | **S1 — 2017, un seuil et un domicile** ; 1^er^ avril 2017 | loi n° 2017-8 du 14 février 2017, art. 3, 5 et 23 [texte] | objet non relevé ; la loi porte « refonte du dispositif des avantages fiscaux » (chapitre des dépenses fiscales) | activité « à titre exclusif ou à titre principal » tournée vers l'exportation, sur décision de l'administration ; suspensions d'incitation dans le code d'incitations aux investissements → seuil de 50 % du chiffre d'affaires ; avantages repris dans le code de la taxe (art. 11, I et I *quater* ; art. 13 *ter*) | attestation d'achat en suspension (2018) ; définition des opérations d'exportation (2019) |
| Régime suspensif | **S2 — 2022, un champ resserré** ; 1^er^ janvier 2022 | décret-loi de finances pour 2022 (décret-loi n° 2021-21), art. 52 [texte] | objet non relevé | sociétés de commerce international et entreprises de services admises → exclues, totalement exportatrices comprises | — |
| Retenue à la source | **RS1 — 1998, l'acheteur public retient la taxe** ; 1^er^ janvier 1998 | loi de finances pour 1998 (loi n° 97-88), art. 36 et 37 [image] | objet non relevé | le fournisseur verse toute la taxe → l'acheteur public en retient 50 % sur les marchés | tous les achats d'au moins 1 000 dinars (2004) ; immeubles et fonds de commerce (2013) ; le crédit qui en naît devient un cas de restitution (1998), puis de restitution rapide (2007) |

**Lectures concurrentes, dispositif par dispositif.**

- **Taux — 1995 ou 2002 ?** Le taux de 10 % naît en 1995 hors du code et n'y entre qu'en 2002,
  sans changer de valeur. Retenu : 1995 (le dispositif arrive) ; 2002 est une étape. La figure
  existante marque déjà les deux.
- **Réductions annuelles — où est la rupture de A1 ?** Trois dates se défendent : la loi de
  finances pour 1996 (art. 40), qui décide le retrait mais renvoie sa date à un décret ; le
  décret n° 97-1339 du 14 juillet 1997, qui fixe cette date, mais que les notes ne connaissent
  que par les visas d'autres décrets (**il ne peut pas porter la rupture**) ; le décret
  n° 98-952, qui sépare les deux produits. Retenu : l'article 40, lu, avec 1998 pour première
  étape. La bifurcation du 6 mai 1998 peut aussi se lire comme une rupture propre — un produit
  change d'impôt.
- **Régime suspensif — 2010 et 1993.** Les régimes propres à certaines opérations, à partir de
  2010, « ne tiennent pas à la part de l'exportation » (chapitre, l. 287) : c'est un critère
  nouveau, qui peut se lire comme une rupture, avec pour étapes 2014, 2017, 2020, 2021 et 2022.
  Le code d'incitations de 1993 fait de la suspension un instrument d'incitation à
  l'investissement : objectif nouveau, mais son domicile est le chapitre des dépenses fiscales
  (`@sec-df-code-1993`). Retenu ici : deux ruptures, S1 et S2 ; 2010 en étape de S1 serait
  faux (elle la précède) : elle est classée **rupture possible**, à trancher.
- **Retenue à la source — la baisse de 2016.** De 50 % à 25 % : ajustement de niveau selon le
  critère. Mais elle suit le diagnostic du ministère des Finances de 2013 sur le crédit
  (chapitre, l. 374), et N3 relève que le projet des Assises en simulait l'effet sur le crédit.
  Les notes ne donnent pas l'objet que la loi s'assigne : classée ajustement.
- **Déduction — l'exclusion des achats en espèces (2014).** Le chapitre la dit « d'une autre
  nature » : elle fait du droit à déduction un instrument de lutte contre les paiements en
  espèces — un objectif nouveau. Classée **rupture possible** du dispositif ; les notes ne
  donnent pas l'intitulé de l'article.
- **Facture — la facture électronique (2016).** Dispositif nouveau, obligation étendue par
  paliers (2019, 2026). Classée **rupture possible** de « Déclaration et facture ».

---

## 4. Le registre de destination

Une ligne par unité du chapitre actuel : section, alinéa groupé, tableau, figure, formule,
commentaire caché. « P » : premier plan ; « R » : replié, dans le bloc nommé. Aucune ligne
n'est supprimée.

### 4.1 Tête de chapitre et « architecture de 1988 »

| N° | Lignes | Unité | Destination |
|---|---|---|---|
| 1 | 1 | `# … {#sec-tva}` | conservé ; identifiant inchangé (cité par `index.qmd` et `_depenses_fiscales.qmd`) |
| 2 | 3 | chapeau : loi n° 88-61, art. 1^er^ ; loi n° 88-62 ; lien avec le droit de consommation | P, chapeau, `=` |
| 3 | 5-11 | encadré sur la lecture des dates (trois alinéas) | P, `=` ; ses citations (art. 6 ; décret n° 88-1109 ; lois de finances pour 1989 à 1993 ; loi de finances pour 1996, art. 38, 39, 46 et 68) ont pour domicile le registre du champ |
| 4 | 13-17 | « Des taxes sur le chiffre d'affaires à la TVA » : décret du 29 décembre 1955 ; art. 2, 4 et 5 de la loi | P, `#sec-tva-origine`, `=` ; repris d'une phrase dans C1 |
| 5 | 19 | titre « L'architecture posée en 1988 » | titre supprimé ; contenu aux lignes 6 à 13 |
| 6 | 21-25 | champ : art. 1^er^ du code ; énumération des ventes taxées ; le détail absent | P, `#sec-tva-mecanisme` (principe) et `#sec-tva-champ` (énumération) ; citation au registre du champ |
| 7 | 27-36 | `tbl-tva-calendrier` | P, sous C1 dans `#sec-tva-ruptures` ; identifiant conservé ; ses quatre lignes reprises, avec « Portée », au registre du champ |
| 8 | 38 | constat : grossistes en alimentation générale ; forfait des transporteurs sans mise en application établie avant 1998 | P, `#sec-tva-champ`, les deux phrases ensemble ; `#sec-tva-forfaits` y renvoie |
| 9 | 40 | `<!-- RECHERCHE r-tva-mise-en-application-post-1989 -->` | suit la ligne 8, dans `#sec-tva-champ`, sans être dédoublée |
| 10 | 42-44 | assujettis : art. 2 ; la mention de la taxe sur facture rend redevable | P, `#sec-tva-mecanisme` (une phrase) et `#sec-tva-champ` |
| 11 | 46 | option : effet, durée de quatre ans, sortie ; entreprises dépendantes ; entrepositaires de boissons | R « L'option et le fait générateur dans la rédaction de 1988 » |
| 12 | 48-60 | `tbl-tva-fait-generateur` et sa source | R, même bloc ; identifiant conservé |
| 13 | 62 | fait générateur des travaux immobiliers ; marchés publics payés à l'encaissement | R, même bloc |
| 14 | 64-66 | grille de 1988 : 17 %, 6 %, 29 % (art. 7) | fusionné avec `#sec-tva-taux` (déjà dit l. 116 et 166) ; la citation subsiste l. 166 |
| 15 | 68 | contenu des tableaux B et C en 1988 | P, `#sec-tva-taux`, alinéa ajouté après les quatre points |
| 16 | 70 | tableau A en 1988 (art. 4) | P, `#sec-tva-exonerations` |

### 4.2 « L'évolution, réforme par réforme »

| N° | Lignes | Unité | Destination |
|---|---|---|---|
| 17 | 72 | titre | supprimé ; contenu aux lignes 18 à 33 |
| 18 | 76 | forfaits différés ; loi de finances pour 1990, art. 24 à 26 | P, `#sec-tva-forfaits` ; registre des forfaits |
| 19 | 78 | taxe sur la marge (1991) ; unification de 1993 ; « sans date d'effet plus précise » | P, `#sec-tva-forfaits` (F1) ; registre des forfaits |
| 20 | 80 | forfait mensuel des transports, 1^er^ janvier 1998 | P, `#sec-tva-forfaits` ; registre des forfaits |
| 21 | 84 | premier taux de 10 %, 1^er^ janvier 1995 ; 17 % → 18 % en 1998 | fusionné avec `#sec-tva-taux` (points 1 et 3, liste repliée) ; le détail des opérations visées (informatique, téléviseurs, transport de marchandises) va au registre « Les opérations qui changent de taux » |
| 22 | 86 | loi de finances pour 1996 : principe au 1^er^ janvier (art. 68) | encadré des dates (déjà dit l. 10) |
| 23 | 88 | 1^er^ avril 1996 : professions libérales à 10 % ; contrats maintenus à 6 % | P, `#sec-tva-trajectoires` ; R registre des trajectoires |
| 24 | 89 | 1^er^ juillet 1996 : détaillants | P, C2 et `#sec-tva-champ` ; R registre du champ |
| 25 | 90 | 1^er^ septembre 1996 : hôtellerie, tourisme, restauration à 10 % | P, `tbl-tva-trajectoires` ; R registre des trajectoires |
| 26 | 92 | formation (2000), Internet (2001) ; incorporation au code (2002) | R registre « Les opérations qui changent de taux » ; l'incorporation est déjà l. 169 |
| 27 | 94 | télécommunications : exonérées (1995), taxées au 1^er^ janvier 2003 | P, `#sec-tva-trajectoires` ; R registre des trajectoires |
| 28 | 98 | 1^er^ janvier 2007 : fin du 29 %, 10 % → 12 % ; transfert sélectif au droit de consommation | P, C3 ; fusionné avec `#sec-tva-taux` (l. 146, 170) ; la phrase sur le transfert sélectif reste, avec renvoi à `@tbl-dc-transfert-2007`, son domicile |
| 29 | 100 | 1^er^ janvier 2015 : électricité et produits pétroliers au tableau B bis | fusionné avec `#sec-tva-reductions-annuelles` (déjà dit l. 187) : A2 |
| 30 | 104 | lois de finances pour 2016 et 2017 : élargissements | P, C4 ; R registres du champ, des exonérations et des taux, par article |
| 31 | 106 | 1^er^ janvier 2018 : un point de plus sur les trois taux | fusionné avec `#sec-tva-taux` (l. 147, 171) ; la phrase « la structure demeure, les listes changent » va à la clôture de `#sec-tva-ruptures` |
| 32 | 108 | médicaments au détail (2016, 2017, 2020, 2021) ; boissons alcoolisées (2022) | P, `tbl-tva-trajectoires` (médicaments) et `#sec-tva-champ` (boissons) ; R registre du champ |
| 33 | 110 | 2023 : professions libérales au taux normal ; 2025 : électricité, logement | fusionné avec `#sec-tva-trajectoires` (l. 177, 179) et `#sec-tva-reductions-annuelles` (électricité, étape de A2) |

### 4.3 « La longue période »

| N° | Lignes | Unité | Destination |
|---|---|---|---|
| 34 | 112 | titre « La longue période » | le titre passe au récit B (`#sec-tva-longue-periode`) ; les trois sous-sections vont au récit A |
| 35 | 114-116 | chapeau des générations de taux ; « taux intermédiaire » n'est pas un terme du code | P, `#sec-tva-taux`, `=` |
| 36 | 118-143 | `fig-tva-taux` et sa note de lecture | P, `=` ; identifiant et `slug` conservés |
| 37 | 145-148 | les quatre points | P, `=` |
| 38 | 150-173 | bloc replié « Les six grilles… » ; `tbl-tva-taux` (engendré) ; six alinéas datés | R, `=` |
| 39 | 175-177 | trajectoire des professions libérales ; l'inscription de 2017 n'est pas un changement de taux | P, `#sec-tva-trajectoires`, `=` |
| 40 | 179 | logement des promoteurs : trois temps, trois reports | P, `#sec-tva-trajectoires`, `=` |
| 41 | 181-187 | réductions annuelles : art. 8 ; art. 40 de la loi de finances pour 1996 ; décrets de 1998, 2004, 2007 ; 2015 | P, `#sec-tva-reductions-annuelles`, `=` pour le fond, remis au gabarit |
| 42 | 189 | `<!-- TODO (bibliographe) : série complète des décrets de 1998 à 2014 -->` | conservé, dans le bloc « Les textes des réductions annuelles », à côté du tableau année par année dont il conditionne la parution |

### 4.4 « Déduction, crédit et suspension »

| N° | Lignes | Unité | Destination |
|---|---|---|---|
| 43 | 191-193 | `## … {#sec-tva-deduction}` et son chapeau | P, `=` |
| 44 | 195-197 | `#sec-tva-droit-deduction` : art. 9, principe, report du reliquat | P, `=` |
| 45 | 199 | art. 10 : deux exclusions ; 1998 ; plateforme de 2022 | P, résumé en un point ; R registre de la déduction |
| 46 | 201 | achats en espèces : 20 000, 10 000, 5 000 dinars | P, un point ; R registre de la déduction |
| 47 | 203-209 | assujetti partiel ; formule du pourcentage de déduction ; définitions des symboles | R « Le pourcentage de déduction et la régularisation », `=` |
| 48 | 211 | régularisation : cinq centièmes, cinquièmes, dixièmes | R, même bloc, `=` |
| 49 | 213-217 | `#sec-tva-credit-restitution` : mécanisme ; texte de 1988 | P, `=` |
| 50 | 219-229 | `#sec-tva-restitution-ruptures` ; `tbl-tva-restitution-ruptures` | P, `=` |
| 51 | 232-236 | les trois temps | P, `=` |
| 52 | 238-240 | `#sec-tva-restitution-chronologie` : état du droit en 2023 | P, `=` |
| 53 | 242-266 | bloc replié ; `tbl-tva-restitution` (19 lignes) | R, `=` |
| 54 | 268 | `TODO (documentaliste)` : date d'effet de la loi n° 2007-69 | conservé dans le bloc |
| 55 | 270 | `TODO (documentaliste)` : délai de visa de 1998 à 2002 | conservé dans le bloc |
| 56 | 275-279 | `#sec-tva-regime-suspensif` : le mécanisme ; l'article 11 de 1988 | P, `=` |
| 57 | 281 | code d'incitations de 1993 ; révision de 1998 | P, une phrase et renvoi à `@sec-df-code-1993` ; R registre du régime suspensif |
| 58 | 283 | loi n° 2017-8 ; attestation (2018) ; opérations d'exportation (2019) ; renvoi à `@sec-depenses-fiscales` | P pour le seuil de 50 % (S1) ; R registre pour le détail des paragraphes et articles |
| 59 | 285 | décret-loi de finances pour 2022 : commerce international et services exclus | P (S2), `=` |
| 60 | 287-300 | `tbl-tva-suspension-sectorielle` et sa phrase d'entrée | R « Le régime suspensif, texte par texte » ; identifiant conservé ; la phrase d'entrée reste au premier plan |
| 61 | 302 | `TODO (documentaliste)` : loi de finances complémentaire pour 2014, art. 27 ; origine de l'art. 13 *quater* | conservé dans le bloc |
| 62 | 304 | option de 2016 : la restitution automatique vaut abandon du régime suspensif | P, `=` |
| 63 | 306 | aucun coût budgétaire publié ; citation du rapport sur les dépenses fiscales, p. 20 | déplacé au récit B, `#sec-tva-ce-qui-echappe`, `=` ; une phrase et un renvoi restent ici |
| 64 | 308-310 | `#sec-tva-declaration-facture` : rythme de la déclaration, 1988 et 1994 | P, même section, `=` |
| 65 | 312 | `TODO (documentaliste)` : loi de finances pour 1994, art. 31 et 32 ; articles non repris | conservé à la même place |
| 66 | 314 | retenue à la source : 1998, 2004, 2013, 2016 | P, `#sec-tva-retenue-source` (nouvelle), résumé ; R registre de la retenue |
| 67 | 316 | portée économique de la retenue | P, `#sec-tva-retenue-source`, `=` |
| 68 | 318 | facture ; facture électronique : 2016, 2019, 2026 | P, `#sec-tva-declaration-facture` ; R registre de la déclaration et de la facture |
| 69 | 320-322 | `#sec-tva-credit-donnees` : chapeau | **reste en place**, à la fin de « Déduction, crédit et suspension », `=` ; le récit B y renvoie |
| 70 | 324-360 | `fig-tva-credit-restitutions` et sa note de lecture | reste en place, `=` |
| 71 | 362 | `TODO (documentaliste)` : prolonger les séries après 2014 | reste à côté de la figure |
| 72 | 364-372 | trois précautions ; écarts entre séries ; trois valeurs de la retenue de 2012 ; rapports aux recettes ; réserve sur le dénominateur | reste en place, `=` ; à resserrer : la note de lecture de la figure dit déjà la moitié de ces alinéas (§ 7.1) |
| 73 | 374 | un huitième à un quart du crédit demandé ; diagnostic du groupe de travail de 2013 | reste en place, `=` |
| 74 | 376-388 | `#sec-tva-credit-etudes` : FMI 1997, 2013, 2015 ; Banque mondiale 2014 ; Harrison et Krelove 2005 | reste en place, `=` (décision du propriétaire du 7 octobre 2026 : les études que le chapitre porte déjà ne changent pas de place) |

### 4.5 « Ce que la TVA rapporte »

| N° | Lignes | Unité | Destination |
|---|---|---|---|
| 75 | 390-392 | titre ; montée en charge de 1988 à 1996 | récit B, `#sec-tva-rendement` ; la phrase devient la légende des ruptures marquées sur la figure |
| 76 | 394-424 | `fig-tva-rendement` et sa note de lecture | récit B, identifiant et `slug` conservés (cité deux fois par `index.qmd`) ; figure à reprendre par segments de base du PIB (§ 6.1) |
| 77 | 426 | parts du PIB (6,5 % en 1988, 5,1 % en 1997, 7,3 % en 2022, 6,8 % en 2025) ; part des recettes fiscales, 26 à 32 % | récit B, `#sec-tva-rendement` ; phrase à reprendre : 1997 est l'année d'un changement de niveau du PIB (`backlog-precis.md`) ; la part des recettes va à `#sec-tva-fiscalite-indirecte` |
| 78 | 428 | part des dépenses de l'État (19,8 % en 1990, 27,0 % en 2000, 22,3 % en 2025 ; 2020) | récit B, `#sec-tva-rendement`, `=` |
| 79 | 430 | le rendement ne suit pas la suite des réformes | récit B, `#sec-tva-rendement` ; devient la phrase d'essentiel de la section |
| 80 | 432 | dépenses fiscales de TVA : 1 326,4 ; 1 616,8 ; 1 532,8 MD ; 19,66 % ; renvois à `@tbl-df-par-impot` et `@sec-df-rapport` | récit B, `#sec-tva-ce-qui-echappe`, `=`, complété par la décomposition par forme (§ 6.4) |

**Quatre-vingts lignes.** Soixante-dix-huit ont une destination unique ou une fusion nommée ;
deux titres (lignes 5 et 17) disparaissent sans contenu propre. Les six `TODO` et l'ancre
`RECHERCHE` sont tous replacés.

**Contrôle mécanique à faire par le rédacteur avant de rendre la main** : extraire du chapitre
actuel ses 164 citations distinctes — clé, article, page — (62 clés) et vérifier que chacun figure dans
le chapitre réécrit. Commande de départ :
`grep -o '@[a-z0-9-]*\(, [^];@]*\)\?' precis/fr/fiscalite/_tva.qmd | sort | uniq -c`. Le § 5
est construit pour que chacun y trouve sa ligne.

**Cas difficiles.**

1. **Un même article dans plusieurs dispositifs** : la loi n° 2006-80, art. 17 (grille,
   professions libérales, réductions annuelles) ; la loi de finances pour 2018, art. 43 ;
   celle pour 2017, art. 27 ; celle pour 2016, art. 47 (restitution et régime suspensif) ;
   celle pour 1998, art. 28 (taux de 10 % et régime suspensif) ; le décret n° 88-1109, art. 1^er^
   (champ, taux, forfaits, restitution). Un domicile est désigné au § 5 ; les autres registres
   portent une ligne de renvoi `@tbl-…`.
2. **La ligne 8 porte deux constats pour une seule ancre `RECHERCHE`** (grossistes ; forfait
   des transporteurs). Les deux restent ensemble dans `#sec-tva-champ`, l'ancre à côté ; la
   section des forfaits y renvoie. La fiche de `docs/recherches.yml` ne nomme que le fichier.
3. **Les lignes 14, 21, 28, 29, 31 et 33 sont des fusions** : le fait est déjà écrit ailleurs
   dans le chapitre. La fusion ne perd rien si le rédacteur vérifie que la version conservée
   porte toutes les citations de la version retirée — par exemple « art. 56 à 58 et 100 »
   (l. 84 et 167), « art. 13, 17 et 19 » (l. 98 et 170).
4. **Le paragraphe l. 104** mêle sept articles de deux lois, qui partent dans trois registres.
5. **`tbl-tva-suspension-sectorielle`** (huit lignes) : tableau court selon le chantier, donc
   non repliable en principe. Il est replié ici parce qu'aucune figure n'en dépend et qu'il est
   un registre ; à trancher.
6. **Les lignes 69 à 74 ne bougent pas** (décision du propriétaire du 7 octobre 2026 sur les
   études) : le récit B, qui traite du budgétaire, n'a donc pas chez lui la seule figure
   budgétaire sur le crédit. Un renvoi y pourvoit.

---

## 5. Le classement des textes

Par dispositif. « Chap. » : le texte est cité par le chapitre actuel (oui) ou seulement établi
par une note (N1, N2, N3). Portée : **rupture**, **étape** (de quelle rupture), **ajustement**,
**point de départ**. Un texte seulement établi par une note peut entrer au registre replié ; il
ne monte au premier plan que s'il est lu [image] ou [texte].

### 5.1 Champ et assujettis — registre `tbl-tva-champ-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | loi n° 88-61, art. 1^er^, 2, 4, 5 et 6 de la loi ; code, art. 1^er^, 2 et 5 | **rupture C1** — point de départ | [image] | oui |
| 1^er^ juillet 1988 | décret n° 88-1109, art. 1^er^ et 2 | étape C1 | [image] | oui |
| 1^er^ octobre 1989 | décret n° 89-1222, art. 1^er^ | étape C1 — le gros | [image] | oui |
| non identifiée | entrée des grossistes en alimentation générale | constat, ancre `RECHERCHE` | — | oui |
| non établies | lois de finances pour 1989 à 1993 (clés `loi-88-145-lf-1989`, `loi-89-115-lf-1990`, `lf-1991`, `lf-1992`, `lf-1993`), citées pour l'absence de clause d'effet | hors classement (règle de datation) | [image], dernières pages | oui |
| non établie | loi de finances pour 1993, art. 104 : option ouverte aux forfaitaires de l'impôt sur le revenu | ajustement | [image] | N2 |
| 1^er^ juillet 1996 | loi de finances pour 1996, art. 43 et 46 ; art. 68 (clause générale) | **rupture C2** (ou étape C1) | [texte] ; art. 68 [image] | oui |
| 1^er^ juillet 1996 | même loi, art. 44 : base majorée de 25 % pour les ventes à des non-assujettis ; assiette des détaillants | étape C2 | [texte] | oui (« art. 43 à 46 »), contenu dans N2 seulement |
| 1^er^ juillet 1996 | même loi, art. 45 : facturation des détaillants | étape C2 ; domicile : § 5.11 | [texte] | idem |
| 1^er^ janvier 1999 | loi de finances pour 1999, art. 57 : option ouverte hors champ et aux forfaitaires | ajustement | [texte] | N2 |
| 1^er^ janvier 2003 | loi de finances pour 2003, art. 52 : majoration de 25 % étendue | ajustement | **[notice]** | N2 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 30 et 31 § 1 ; art. 92 | **rupture C4** | [texte], PDF local | oui |
| 1^er^ septembre 2016 | même loi, art. 31 § 5 : enseignement | étape C4 | [texte] | oui (« art. 30, 31, 33 et 92 ») |
| 1^er^ janvier 2016 | même loi, art. 33 : taxe sur la marge, tout non-assujetti | étape C4 ; domicile : § 5.6 | [texte] | oui |
| reportée | même loi, art. 31 § 4 : médicaments hors de l'exonération au détail | étape C4, différée | [texte] | oui |
| 1^er^ janvier 2017 | loi de finances complémentaire pour 2016 (loi n° 2017-1), art. 3 | ajustement — report | [texte] | oui |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 16 (tableau A), 20 (lots de terrain), 21 (immobilisations incorporelles) | étape C4 | [texte] ; contenu des numéros de l'art. 16 non rapproché | oui |
| 1^er^ janvier 2020 | loi de finances pour 2020, art. 30 | ajustement — report | [texte], PDF local | oui |
| 1^er^ janvier 2021 | loi de finances pour 2021, art. 25 : médicaments exclus au gros, exonérés au détail ; abandon de la taxe due | ajustement — retour sur une étape de C4 | [texte] | oui |
| 1^er^ janvier 2022 | décret-loi de finances pour 2022, art. 33 et 73 : détaillants en boissons alcoolisées | étape C2 | [texte] | oui |

### 5.2 Taux — registres `tbl-tva-taux` (grille) et `tbl-tva-taux-perimetre` (opérations)

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 7 ; tableaux B et C | point de départ | [image] | oui |
| non établie | loi de finances pour 1989, art. 23 à 25 : ajouts au tableau B ; lessives hors du tableau C (la répartition entre les trois articles n'est pas donnée par N2) | ajustement | **[OCR] médiocre** | N2 |
| non établies | lois de finances pour 1991 (art. 35 et 36), 1992 (art. 37 et 38), 1993 (art. 83, 84, 94 et 109) : retouches du tableau C | ajustement (lecture possible : étapes amont de T2) | [OCR] | N2 |
| non établie | loi de finances pour 1993, art. 119 | non classable | **[notice]** | N2 |
| 1^er^ janvier 1994 | loi de finances pour 1994, art. 50 et 51 : tableau C | ajustement | [OCR] | N2 |
| 1^er^ janvier 1995 | loi de finances pour 1995, art. 56 à 58 et 100 | **rupture T1** | [texte] | oui |
| 1^er^ janvier 1995 | même loi, art. 86 : produits du tableau « M bis » retirés du tableau C, 29 % → 17 % (« intégration industrielle ») | ajustement (ou étape amont de T2) | [texte] ; liste non lue | N2 |
| 1^er^ janvier 1996 | loi de finances pour 1996, art. 36 : équipements du tableau « P » à 10 % | étape T1 | [texte] ; liste non lue | N2 |
| 1^er^ avril 1996 | même loi, art. 37 § 6 et 38 | étape T1 ; domicile : § 5.5 | [texte] | oui |
| 1^er^ septembre 1996 | même loi, art. 37 § 1 à 5 et 39 | étape T1 ; domicile : § 5.5 | [texte] | oui |
| 1^er^ janvier 1997 | loi de finances pour 1997, art. 19 : équipements à 10 % | étape T1 | [texte] | N2 |
| 1^er^ janvier 1998 | loi de finances pour 1998, art. 25 et 90 : 17 % → 18 % | ajustement de niveau | [image] | oui |
| 1^er^ janvier 1998 | même loi, art. 26 (téléviseurs, 10 % → 18 %) et 27 (tableau « L » retiré du tableau C) | ajustement | [image] ; liste non lue | N2 |
| 1^er^ janvier 2000 | loi de finances pour 2000, art. 19 et 73 : formation à 10 % | étape T1 | [texte] | oui |
| 1^er^ janvier 2001 | loi de finances pour 2001, art. 40 et 68 : Internet à 10 % | étape T1 | [texte] | oui |
| 1^er^ janvier 2002 | loi de finances pour 2002, art. 41 : déchets de plastique à 10 % | étape T1 | **[notice]** | N2 |
| 1^er^ janvier 2002 | même loi, art. 82 à 84 et 97 : le taux de 10 % dans le code, tableau B bis | étape T1 (lecture concurrente : rupture) | [image] | oui |
| 1^er^ janvier 2004 | loi de finances pour 2004, art. 36 | étape T1 | **[notice]** | N2 |
| non relevée | loi de finances pour 2005, art. 71 et 72 : climatiseurs | non classable | **[notice]** | N2 |
| 1^er^ janvier 2006 | loi de finances pour 2006, art. 41 | étape T1 | **[notice]** | N2 |
| 1^er^ janvier 2007 | loi n° 2006-80, art. 13 et 19 : fin du 29 % | **rupture T2 = C3** | [texte] | oui |
| 1^er^ janvier 2007 | même loi, art. 14 : cinq lignes au droit de consommation | étape T2 ; **domicile : chapitre des droits de consommation** (`@tbl-dc-transfert-2007`) | [texte] | oui |
| 1^er^ janvier 2007 | même loi, art. 17 : 10 % → 12 % | ajustement de niveau | [texte] | oui |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 33 : papier des revues à 6 % | ajustement | **[notice]** | N2 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 31 § 2 et 3 : annexe 5 ; tableaux « nouveaux » | étape C4 | [texte] ; annexe 5 non lue | oui |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 24 à 26 (tableau B nouveau) et 27 (art. 7, n° 3 ; tableau B bis abrogé) ; art. 79 | ajustement — de forme pour l'art. 27 : aucun taux ne change | [texte] | oui |
| 1^er^ janvier 2018 | loi de finances pour 2018, art. 43 et 67 : un point de plus | ajustement de niveau | [texte] | oui |
| 1^er^ janvier 2018 | même loi, art. 67 § 2 et 3 : exceptions (marchandises expédiées, marchés publics) | ajustement | [texte] | N2 |
| 1^er^ janvier 2019 | loi de finances pour 2019, art. 60 (panneaux solaires), 64 (téléphonie et Internet fixes), 65 (irrigation) | ajustement | [texte] | N2 |
| 1^er^ janvier 2021 | loi de finances pour 2021, art. 26 | ajustement | [texte] | N2 |
| 1^er^ janvier 2023 | décret-loi de finances pour 2023, art. 44 ; code consolidé de 2023, art. 7 | ajustement ; domicile : § 5.5 | **[AR]** | oui |
| 1^er^ janvier 2023 | même texte, art. 24 : bornes de recharge | ajustement | [AR] partiel | N2 |
| 1^er^ janvier 2024 | loi de finances pour 2024, art. 50 : véhicules électriques | ajustement | [texte] | N2 |
| 1^er^ janvier 2025 | loi de finances pour 2025, art. 31 (électricité), 59 (olives), 64 (logement) | ajustement ; art. 31 : § 5.4 ; art. 64 : § 5.5 | [texte] | oui (31 et 64) ; N2 (59) |
| 1^er^ janvier 2026 | loi de finances pour 2026, art. 46 et 47 | ajustement | **[AR]** | oui |

### 5.3 Exonérations — registre `tbl-tva-exonerations-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 4 et tableau A | point de départ | [image] | oui |
| non établie | loi de finances pour 1989, art. 23 à 25 : ajouts au tableau A | ajustement | **[OCR] médiocre** | N2 |
| non établie | loi de finances pour 1991, art. 33 et 60 | ajustement | [OCR] | N2 |
| non établie | loi de finances pour 1992, art. 35 à 42 | ajustement | [OCR] | N2 |
| non établie | loi de finances pour 1993, art. 79 à 92 | ajustement | [OCR] | N2 |
| 1^er^ janvier 1994 | loi de finances pour 1994, art. 52 à 54, 60 et 61 | ajustement | [OCR] | N2 |
| 1^er^ janvier 1995 | loi de finances pour 1995, art. 76, 81 à 85 et 88 | ajustement ; art. 85 (télécommunications) : § 5.5 | [texte] ou [notice] selon l'article | art. 85 seul |
| 1^er^ janvier 2001 | loi de finances pour 2001, art. 63 et 68 : logement | ajustement ; domicile : § 5.5 | [texte] | oui |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 31, 32, 64 et 65 | ajustement | **[notice]** | N2 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 30 et 31 | **rupture C4** ; domicile : § 5.1 | [texte] | oui |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 16 | étape C4 ; domicile : § 5.1 | [texte] | oui |
| 1^er^ janvier 2018 | loi de finances pour 2018, art. 44 : exonération du logement limitée | étape C4 (lecture possible : ajustement) ; domicile : § 5.5 | [texte] | oui |
| 1^er^ janvier 2021 | loi de finances pour 2021, art. 27 | ajustement — **à vérifier** : N2 y lit des dons aux associations de personnes handicapées, N3 l'article 13 *quinquies* (suspension) ; les deux lectures portent sur le même article | [texte] | oui (suspension) |

### 5.4 Réductions annuelles — registres `tbl-tva-reductions-textes` (provisoire) et `tbl-tva-reductions-annuelles` (à terme)

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 8 ; tableau B (électricité, gaz, huiles de pétrole à 6 %) | point de départ | [image] | oui |
| 1988-1997 | 144 décrets dont l'intitulé mentionne la TVA (exemples : n° 88-2002, n° 89-224, n° 95-1256, n° 96-771) | non classables | **[notice]**, non triés | N2 ; le chapitre dit seulement que la série « n'épuise pas les usages de cet article » |
| date fixée par décret | loi de finances pour 1996, art. 40 | **rupture A1** | [texte] | oui |
| non établie | décret n° 97-1339 du 14 juillet 1997 | étape A1 ; **connu par les seuls visas** : ne peut porter la rupture | non lu | N1, N2 |
| 1^er^ janvier au 5 mai 1998 | décret n° 98-384, art. 1^er^ à 3 | étape A1 | [texte] | oui |
| 6 mai 1998 | décret n° 98-952, art. 1^er^ à 4 | étape A1 (lecture concurrente : rupture) ; tarif pétrolier : domicile aux droits de consommation | [texte], non relu à l'image | oui |
| 1999 | décret n° 99-211 | ajustement — reconduction | [texte] | N1 |
| 2000 à 2003 | décrets n° 2000-329, 2001-401, 2002-209, 2003-133 | ajustement — reconductions | **[probable]** | N1 |
| 2004 | décret n° 2004-9 (électricité) | ajustement — reconduction | non lu | N1 |
| 1^er^ août 2004 | décret n° 2004-1773, art. 1^er^ et 2 | étape A1 — reprise pour les produits pétroliers, sans terme énoncé | [image] | oui |
| 2005 | décrets n° 2004-2727 et 2004-2728 | ajustement — reconductions | **[probable]** | N1 |
| 2006 | décrets n° 2005-3383 et 2005-3384 | ajustement — reconductions | [texte] | N1 |
| 1^er^ janvier 2007 | loi n° 2006-80, art. 17 et 19 : 10 % → 12 % ; décrets n° 2007-1 et 2007-2 | ajustement de niveau, par la loi ; domicile de l'art. 17 : § 5.2 | [texte] | oui |
| 2008 à 2014 | décrets n° 2008-1 et 2008-2 ; 2008-3967 et 2008-4113 ; 2009-3761 et 2009-3762 ; 2010-3586 et 2010-3587 ; 2012-6 et 2012-9 ; 2012-3413 et 2012-3414 ; 2013-5197 et 2013-5198 | ajustement — reconductions | lus, un sur deux pour 2008-2010 et 2012 (N1, § 4.3) | N1 |
| 1^er^ janvier 2015 | loi de finances pour 2015, art. 36 et 46 | **rupture A2** | [image] | oui |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 27 | ajustement de forme ; domicile : § 5.2 | [texte] | oui |
| 1^er^ janvier 2018 | loi de finances pour 2018, art. 43 | ajustement de niveau ; domicile : § 5.2 | [texte] | oui |
| 1^er^ janvier 2019 | loi de finances pour 2019, art. 65 : irrigation à 7 % | ajustement | [texte] | N2 |
| 1^er^ janvier 2025 | loi de finances pour 2025, art. 31 | ajustement | [texte] | oui |

### 5.5 Trajectoires par opération — registre `tbl-tva-trajectoires-textes`

Aucune rupture propre : chaque trajectoire est une suite d'étapes et d'ajustements de textes
classés ailleurs. Le registre est une frise par opération.

| Opération | Suite des textes (date d'effet) | Portée | Lecture | Chap. |
|---|---|---|---|---|
| Professions libérales | tableau B, 6 % (1988) ; loi de finances pour 1996, art. 37 § 6 et 38 (10 %, 1^er^ avril 1996) ; loi n° 2006-80, art. 17 (12 %, 2007) ; loi de finances pour 2017, art. 27 et 79 (liste à l'art. 7, taux inchangé) ; loi de finances pour 2018, art. 43 (13 %) ; décret-loi de finances pour 2023, art. 44 (taux normal ; **déduit de l'art. 7, non écrit par l'article**, N2) | étapes T1, puis ajustements | [texte] ; 2023 : [AR] | oui |
| Logement vendu par les promoteurs | loi de finances pour 2001, art. 63 (exonéré) ; loi de finances pour 2016, art. 31 § 3 (renumérotation, n° 53) ; loi de finances pour 2018, art. 44 et 67 (13 % ; taux normal prévu pour 2020) ; loi de finances pour 2019, art. 79 (report à 2021 ; déduction sur stocks) ; loi de finances pour 2020, art. 31 (report à 2024) ; loi de finances pour 2024, art. 39 (report à 2025) ; loi de finances pour 2025, art. 64 (7 % jusqu'à 400 000 dinars ; taux normal au-delà, **déduit**) | ajustement (2001) ; étape C4 (2018) ; ajustements — reports ; ajustement (2025) | [texte] | oui, sauf 2016 (N2) |
| Télécommunications | loi de finances pour 1995, art. 85 (exonérées) ; loi de finances pour 2002, art. 66 à 70, et décret n° 2002-3356, art. 1^er^ (taux normal au 1^er^ janvier 2003 ; redevance de 5 % hors assiette) ; loi de finances pour 2019, art. 64, et pour 2021, art. 26 (téléphonie et Internet fixes à 7 %) | ajustements | [texte] | oui, sauf 2019 et 2021 (N2) |
| Médicaments au détail | voir § 5.1 (2016, 2017, 2020, 2021) | renvoi | [texte] | oui |
| Hôtellerie et restauration | tableau B, 6 % (1988) ; loi de finances pour 1989, art. 23 à 25 (restauration ajoutée au tableau B) ; loi de finances pour 1996, art. 37 § 1 à 5 et 39 (10 %, 1^er^ septembre 1996) ; loi de finances pour 2004, art. 36 ; loi de finances pour 2016, art. 30 ; loi de finances pour 2017, art. 27 | étape T1 (1996) ; ajustements | 1989 : [OCR] ; 2004 : [notice] | 1988 et 1996 seuls |
| Informatique, formation, Internet | loi de finances pour 1995, art. 56 ; pour 2000, art. 19 ; pour 2001, art. 40 ; pour 2017, art. 24 à 26 | voir § 5.2 | [texte] | oui, sauf 2017 |
| Enseignement privé | tableau A (1988) ; loi de finances pour 2016, art. 30 et 31 § 5 (6 %, 1^er^ septembre 2016) | étape C4 | [texte] | oui |

### 5.6 Forfaits et taxe sur la marge — registre `tbl-tva-forfaits-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| différés | décret n° 88-1109, art. 1^er^ : art. 16 et 17 non mis en application | point de départ | [image] | oui |
| non établie | loi de finances pour 1990, art. 24 à 26 : taxe forfaitaire annuelle ; droit forfaitaire simplifié | étape C1 (lecture possible : rupture, un dispositif arrive) | [image] | oui |
| non établie | loi de finances pour 1991, art. 34 : taxe sur la marge | ajustement | [OCR] | oui |
| non établie | loi de finances pour 1993, art. 100 à 103 et 105 | **rupture F1** | [image] | oui |
| 1^er^ janvier 1998 | loi de finances pour 1998, art. 29 : taxe forfaitaire mensuelle des transports (« assujettissement de toutes les catégories de transport terrestre au régime normal ») | étape — nouveau public (transports terrestres) ; lecture possible : rupture | [image] | oui |
| 1^er^ janvier 1998 | même loi, art. 30 | ajustement ; domicile : § 5.7 | [texte] | oui |
| 1^er^ janvier 2002 | loi de finances pour 2002, art. 89 et 90 : renvois de l'art. 6 | ajustement | [texte] | N2 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 33 | étape C4 | [texte] | oui |

### 5.7 Droit à déduction — registre `tbl-tva-deduction-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 9 et 10 | point de départ (C1) | [image] | oui |
| 1^er^ janvier 1998 | loi de finances pour 1998, art. 30, 38 et 39 ; art. 90 | ajustement ; art. 38 et 39 : étape RS1 | [image] | oui |
| 1^er^ janvier 2002 | loi de finances pour 2002, art. 40 ; loi de finances pour 2008, art. 19 : transport aérien international au numérateur | ajustement | 2002 : **[notice]** ; 2008 : [texte] | N3 |
| 1^er^ janvier 2004 | loi de finances pour 2004, art. 57 : dons en nature | ajustement | **[code]** | N3 |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 34 et 95 : achats en espèces | **rupture possible** (objectif nouveau) ; à défaut, ajustement | [texte] | oui |
| 1^er^ janvier 2014 | même loi, art. 40 | ajustement | **[notice]**, [code] | N3 |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 34 ; loi de finances pour 2019, art. 35 : territoires à régime fiscal privilégié | ajustement | **[code]** | N3 |
| 2019 et 2022 | loi de finances pour 2019, art. 79 § 2 ; décret-loi de finances pour 2022, art. 33 : déduction sur stocks sans droit à restitution | ajustement | **[code]** | N3 |
| 1^er^ janvier 2022 | décret-loi de finances pour 2022, art. 41 et 73 : plateforme des certificats de retenue | ajustement | [texte] | oui |
| diverses | retouches de l'art. 9 : lois de finances pour 2003 (art. 83 et 84), 2007 (art. 20), 2008 (art. 49 à 51), 2012 (art. 37), 2016 (art. 16), 2018 (art. 58), 2019 (art. 66), 2021 (art. 27) | ajustements | **[code]**, non relus | N3 |

### 5.8 Crédit et restitution — registre `tbl-tva-restitution` (existant)

Les dix-neuf lignes du tableau existant gardent leur classement (colonne « Portée » déjà
écrite). Quatre textes établis par N3, § 2.2, n'y figurent pas :

| Date d'effet | Texte, article | Portée | Lecture |
|---|---|---|---|
| 1^er^ janvier 2007 | loi de finances pour 2007 (loi n° 2006-85), art. 47 : pénalité et intérêt de restitution, 0,75 % → 0,5 % par mois | ajustement | [texte] |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 63 : déclarations à jour à la date de l'ordonnancement | ajustement | [texte] |
| 1^er^ janvier 2017 | loi de finances pour 2017, art. 35 : amende de 100 % du crédit indûment restitué | ajustement | [texte] |
| 1^er^ janvier 2022 | décret-loi de finances pour 2022, art. 48 § 5 : vérification ponctuelle | ajustement | [texte] |

Si le bloc doit être le registre complet du dispositif, ces quatre lignes y entrent
(vingt-trois lignes), après versement des pages par le bibliographe.

### 5.9 Régime suspensif — registre `tbl-tva-suspension-textes` et `tbl-tva-suspension-sectorielle`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 11 (et art. 9 et 15) | point de départ | [image] | oui |
| non relevée | loi de finances pour 1992, art. 68 : art. 13 (alcools) abrogé | ajustement | [OCR] | N2, N3 |
| non relevée | loi de finances pour 1993, art. 114 : mention sur facture, relevé trimestriel | ajustement | [OCR] | N3 |
| — | code d'incitations aux investissements (loi n° 93-120), art. 9 et 22 | lecture possible : rupture (objectif d'incitation) ; **domicile : chapitre des dépenses fiscales** | clé existante | oui |
| 1^er^ janvier 1998 | loi de finances pour 1998, art. 28 et 90 (« révision du régime suspensif ») | ajustement | [image] | oui |
| 1^er^ janvier 2007 | loi de finances pour 2007, art. 70 : liste trimestrielle détaillée | ajustement | [texte] | N3 |
| 1^er^ janvier 2010 | loi de finances pour 2010, art. 23, 34 et 56 : art. 11, I *bis* ; art. 13 nouveau | **rupture possible** (critère : la nature de l'opération) ; à défaut, ajustement | [texte] | oui |
| 1^er^ janvier 2013 | loi de finances pour 2013, art. 35 et 36 : art. 11, I *ter* | ajustement | [texte] | N3 |
| date de publication | loi de finances complémentaire pour 2013, art. 14 | ajustement | [texte] | N3 |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 41 et 89 § 2 | ajustement | art. 41 : **[notice]** ; art. 89 : [texte] | N3 |
| non établie | loi de finances complémentaire pour 2014, art. 27 : art. 13 *bis* | étape de la rupture possible de 2010 | [texte] | oui |
| non vérifiée | origine de l'art. 13 *quater* | non classable | **[code]**, rattachement douteux | TODO |
| année 2016 | loi de finances pour 2016, art. 47 (option) ; art. 75 (suspension sur les produits de l'annexe 4) | art. 47 : étape « restituer vite », domicile § 5.8 ; art. 75 : ajustement, objet du récit B (dépenses fiscales) | [texte] | art. 47 seul |
| 1^er^ avril 2017 | loi n° 2017-8, art. 3, 5 et 23 | **rupture S1** | [texte] | oui |
| 1^er^ janvier 2018 | loi de finances pour 2018, art. 30 et 67 : attestation ; art. 19 *quater* | étape S1 | [texte] | oui |
| 1^er^ janvier 2019 | loi de finances pour 2019, art. 38 et 90 : opérations d'exportation (décret gouvernemental n° 2019-937, non lu) | étape S1 | [texte] | oui |
| 1^er^ janvier 2020 | loi de finances pour 2020, art. 28 et 58 | étape de la rupture possible de 2010 | [texte] | oui |
| 1^er^ janvier 2021 | loi de finances pour 2021, art. 27 et 42 : art. 13 *quinquies* | idem | [texte] | oui |
| 1^er^ janvier 2022 | décret-loi de finances pour 2022, art. 26 et 39 : art. 13 nouveau élargi ; art. 13 *sexies* | idem | [texte] | oui |
| 1^er^ janvier 2022 | même texte, art. 52 et 73 | **rupture S2** | [texte] — N2 porte une ligne fautive sur ce point, corrigée au chapitre (`backlog-precis.md`) : suivre le chapitre et N3 | oui |
| 1^er^ janvier 2023 | décret-loi de finances pour 2023, art. 46 : art. 19 *quinquies* | ajustement | **[code]** | N3 |
| 2024 à 2026 | loi de finances pour 2024, art. 42 : suspension temporaire, hors code, pour la Compagnie tunisienne de navigation | ajustement | [texte] | N3 |

### 5.10 Retenue à la source — registre `tbl-tva-retenue-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ janvier 1998 | loi de finances pour 1998, art. 36 et 37 ; art. 90 | **rupture RS1** | [image] | oui |
| 1^er^ janvier 1998 | même loi, art. 38 et 39 (déduction), 40 et 41 (cas de restitution) | étapes RS1 ; domiciles : § 5.7 et § 5.8 | [image] | oui |
| 1^er^ janvier 2003 | loi de finances pour 2003, art. 55 et 56 : retenue de la totalité de la taxe due par un fournisseur non établi, libératoire | étape — nouveau public (lecture possible : dispositif distinct) | [texte] | N3 |
| 1^er^ janvier 2004 | loi de finances pour 2004, art. 72 et 73 ; art. 105 | étape RS1 | [texte] | oui |
| 1^er^ janvier 2013 | loi de finances pour 2013, art. 42 et 79 | étape RS1 | [texte] | oui |
| 1^er^ janvier 2014 | loi de finances pour 2014, art. 51 § 4 et 6 : prix homologués à faible marge ; paiement pour le compte d'autrui | ajustement | [texte] | N3 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 34 et 92 : 50 % → 25 % ; commission des distributeurs | ajustement de niveau (lecture concurrente, § 3.2) | [texte] — N3 lève la mention « texte non lu » de N2 | oui |
| 1^er^ janvier 2022 | décret-loi de finances pour 2022, art. 41 | ajustement ; domicile : § 5.7 | [texte] | oui |

### 5.11 Déclaration et facture — registre `tbl-tva-declaration-textes`

| Date d'effet | Texte, article | Portée | Lecture | Chap. |
|---|---|---|---|---|
| 1^er^ juillet 1988 | code, art. 18 et 19 | point de départ | [image] | art. 18 |
| non relevée | loi de finances pour 1991, art. 50 : bailleurs d'immeubles | ajustement | [OCR] | TODO seul |
| non relevée | loi de finances pour 1992, art. 66 : fournisseurs de factures, transport des marchandises | ajustement | [OCR] | TODO seul |
| non relevée (N3 ; N2 dit pourtant la clause générale de cette loi lue, art. 77 : à accorder) | loi de finances pour 1994, art. 31 et 32 : déclaration mensuelle pour tous | ajustement | [OCR] | oui |
| 1^er^ juillet 1996 selon N2 (art. 46) ; « non relevée » dans N3 | loi de finances pour 1996, art. 45 : facture des détaillants | étape C2 | [image] | oui (« art. 43 à 46 ») |
| 1^er^ janvier 2003 | loi de finances pour 2003, art. 57 : numéro fiscal du client | ajustement | [texte] | N3 |
| 1^er^ janvier 2015 | loi de finances complémentaire pour 2014, art. 19 § 2 | ajustement | [texte] | N3 |
| 1^er^ janvier 2016 | loi de finances pour 2016, art. 22 et 92 : facture électronique (décret gouvernemental n° 2016-1066, non lu) | **rupture possible** — dispositif nouveau | [texte] | oui |
| 1^er^ janvier 2019 | loi de finances pour 2019, art. 46 et 90 | étape | [texte] | oui |
| 2025 | loi de finances pour 2025, art. 71 : amende | ajustement | [texte] | N3 |
| 1^er^ janvier 2026 | loi de finances pour 2026, art. 53 et 110 | étape | **[AR]** | oui |

### 5.12 Textes et documents qui ne sont pas du droit de la taxe

Récit B, sans classement : `gbo-depenses-fiscales` ; `minfin-recettes-fiscales` ;
`minfin-cnf-2013-impots-indirects` ; `minfin-cnf-2013-synthese` ;
`minfin-assises-2014-projet-reforme` ; `minfin-controle-fiscal-2016` ;
`minfin-rapport-budget-2013` et `-2014` ; `loi-2000-82-cdpf`, art. 35 (cité pour la nature
nette des recettes) ; `fmi-1997-selected-issues` ; `fmi-2013-modernisation-administration-fiscale` ;
`fmi-2015-article-iv` ; `banquemondiale2014-revolution-inachevee` ;
`harrison-krelove2005-vat-refunds`. `dgelf-code-tva-2023` est un code consolidé : il sert
l'état du droit, jamais une ligne de registre.

**Textes que les notes ne connaissent que par leur intitulé, ou sans les avoir lus** —
récapitulation : loi de finances pour 1993, art. 119 ; pour 2002, art. 40 et 41 ; pour 2003,
art. 52 ; pour 2004, art. 36 ; pour 2005, art. 71 et 72 ; pour 2006, art. 41 ; pour 2014,
art. 31 à 33, 40, 41, 64 et 65 ; partie de la loi de finances pour 1995, art. 76 à 88 ; les
144 décrets de l'article 8 de 1988 à 1997 ; le décret n° 97-1339 (visas) ; les décrets annuels
[probable] de 2000 à 2005 ; les décrets gouvernementaux n° 2016-1066, 2017-419 et 2019-937 ;
les notes communes n° 11/1999, 15/2004 et 16/2022 ; les tableaux « L », « M », « M bis »,
« P » et l'annexe 5 de la loi de finances pour 2016. Aucun ne porte de rupture dans ce plan.

---

## 6. Le récit B, économique

Règles qui commandent toute la partie : le budgétaire d'abord, en entonnoir ; les études à
part, avec leur méthode ; tout PIB dit sa base, par segments, avec renvoi à l'annexe du site ;
aucune valeur sans sa vue d'évolution ; les figures lisent `figtools.series()`. Aucune valeur
nouvelle n'est donnée ici : seulement les séries et ce qu'elles couvrent.

| § | Section | Ce qu'elle doit établir | Figure ou tableau | Série ou source | État |
|---|---|---|---|---|---|
| 6.1 | `#sec-tva-rendement` | la taxe rapporte une part du PIB qui ne suit pas la suite des réformes ; la part des dépenses de l'État, qui ne dépend d'aucune base, à côté | `fig-tva-rendement` reprise : part du PIB **par segments de base**, part des dépenses ; **les ruptures du droit marquées** (1^er^ juillet 1988, 1989, 1996, 1998, 2007, 2018) | `recettes-fiscales-composition` (`tva_MDT`, 1986-2025) ; `irpp-ratios` (PIB du ministère, PIB des comptes, dépenses depuis 1990) | **après travail de données** : la figure et la phrase « 6,5 % en 1988, 5,1 % en 1997… » sont relevées non conformes par `backlog-precis.md` (base non dite ; 1997 est une année de changement de niveau). Il faut une série de ratios portant `segment_pib` et `rupture_pib`, sur le modèle de `compensation-parts` et de `masse-salariale-ratios`. La part des dépenses et les marques de rupture sont **faisables maintenant** |
| 6.2 | `#sec-tva-fiscalite-indirecte` | la part de la taxe dans les recettes fiscales et dans les impôts indirects, face aux droits de douane, aux droits de consommation et aux autres | figure en parts : les quatre rubriques indirectes, 1986-2025 ; zone grisée avant 1988 | `recettes-fiscales-composition` (`douanes_MDT`, `tva_MDT`, `consommation_MDT`, `autres_indirects_MDT`) | **faisable maintenant**. Ne pas refaire `@fig-recettes-composition` de la présentation du livre : y renvoyer pour l'ensemble, ne tracer ici que l'indirect. Renvoi à `@fig-droits-consommation-rendement` |
| 6.3 | `#sec-tva-consommation` | ce que la taxe prélève sur la consommation privée, comparé au taux normal de la date : l'écart est ce que retranchent exonérations, taux réduits, opérations hors champ | figure : recettes de TVA rapportées à la consommation privée, par segments de base, avec le taux normal en escalier | numérateur : `recettes-fiscales-composition` ; dénominateur : `cnat-pib-emplois` (« Consommation privée », 2015-2024, base 2015) ; taux : `tva-taux` | **après un petit travail de données pour 2015-2024** : la série est au catalogue de `tunisia-data` mais pas dans `precis/_seriescache/`, où les figures lisent ; elle est à verser au snapshot. Le libellé de la source est « Consommation privée » : le titre de la section le reprend si la source ne dit pas « ménages ». Avant 2015 : aucune série au catalogue ; **travail de données plus lourd** — extraire la ligne des emplois du PIB des éditions des comptes nationaux déjà dépouillées pour le PIB (`cnat-pib-nominal`), base par base. À présenter comme **un calcul du précis**, avec sa fiche (`docs/`), en disant : recettes nettes des restitutions selon toute apparence ; l'assiette légale n'est pas la consommation privée ; aucune valeur avant le 1^er^ juillet 1988 |
| 6.4 | `#sec-tva-ce-qui-echappe` | ce que le ministère chiffre comme dépense fiscale de TVA, par forme ; ce qu'il ne chiffre pas | tableau ou figure : dépenses fiscales de TVA par forme (exonération, réduction, suspension, déduction), par rapport et par exercice | `depenses-fiscales-detail` ; `depenses-fiscales-par-impot` | **faisable maintenant pour 2017-2019** (rapport annexé au projet de loi de finances pour 2021 : la forme est renseignée). **Après travail de données pour 2020-2023** : les lignes de TVA des rapports de 2024 et 2025 n'ont pas de forme dans le fichier extrait (N3, § 5.1 f) ; elle est à relire dans les rapports arabes ; d'ici là, des planchers. Une valeur ne se cite qu'avec son rapport. Ne pas dupliquer `@tbl-df-par-impot` ni `@tbl-df-beneficiaires` : y renvoyer. Reçoit le paragraphe l. 306 (suspension intermédiaire sans coût publié) et l. 432 |
| 6.5 | « Ce que la taxe immobilise » — un alinéa de renvoi | le crédit, les restitutions et la retenue pèsent une part des recettes de la taxe | renvoi à `@fig-tva-credit-restitutions`, qui reste dans `#sec-tva-credit-donnees` | `tva-credit-restitutions-sources` (2009-2014) | **existe**. Prolongement : rapports annuels de la direction générale des impôts à lire à l'image (TODO l. 362). Aucune réforme de la restitution n'est encadrée par une série : rien à marquer sur la figure |
| 6.6 | partage entre TVA intérieure et TVA à l'importation | la part de la taxe perçue en douane | — | aucune : le classeur des recettes fiscales n'a qu'une rubrique « TVA » | **à documenter d'abord** : aucune des trois notes n'identifie de source. Pas de section tant que le documentaliste n'en a pas trouvé une |
| 6.7 | incidence par niveau de vie — **hors plan pour l'instant** | qui paie la taxe | — | aucune étude dans les notes du chapitre | **à documenter d'abord, et non urgent** (décision du propriétaire du 7 octobre 2026 : la place des études d'incidence sera fixée plus tard). Une piste existe : le document de travail de Jouini, Lustig, Moummi et Shimeles (2017), cité au volume de la compensation, est dans l'entrepôt et mentionne la TVA ; ce qu'il en isole n'est pas lu. Le dépôt `ceq-tunisie` est un outil de calcul, non une étude publiée : il ne peut pas servir de source à un volume |
| 6.8 | `#sec-tva-credit-etudes` | ce que disent les rapports extérieurs du crédit et de la restitution | — | les cinq documents déjà cités | **existe** ; reste à sa place actuelle, `=` (même décision) |

**Ordre de livraison proposé.** D'abord 6.2 et la part des dépenses de 6.1 (rien à produire).
Ensuite 6.1 par segments de base et 6.4 pour 2017-2019. Puis 6.3, qui demande un versement,
puis une extraction. 6.6 ne s'écrit pas avant une passe du documentaliste. 6.7 attend la
doctrine sur les études.

**Ce que le récit B ne fait pas** : il ne reprend ni la grille des taux, ni la liste des
réformes ; il y renvoie (`@fig-tva-taux`, `@tbl-tva-ruptures`). Il ne reprend pas la mesure
annoncée au rapport sur le budget de 2025 et absente de la loi (N3, § 6, point 3).

---

## 7. Les désaccords et les risques

### 7.1 Ce qui est discutable dans ce plan

1. **Le récit A peut redevenir double.** « Quatre ruptures » puis « dispositif par
   dispositif » : c'est encore deux passages sur la même matière. Le garde-fou est de forme —
   le récit des ruptures tient en une page et ne cite pas ; les sections de dispositif ne
   racontent pas, elles tiennent en une phrase, une vue, des points, un registre. Si la revue
   juge que cela ne suffit pas, la variante est de supprimer le récit et de ne garder de
   `#sec-tva-ruptures` que son tableau.
2. **Onze dispositifs, c'est beaucoup de sections courtes.** Deux regroupements sont
   possibles : les forfaits dans le champ ; la retenue à la source dans la déclaration (comme
   aujourd'hui). Ils sont séparés ici parce que le propriétaire les nomme séparément.
3. **C4 est la rupture la moins assurée** (§ 3.1, lecture 3) : elle repose sur l'ampleur du
   mouvement, non sur un objet énoncé par la loi.
4. **« Trajectoires » et « taux » se recouvrent** : une opération qui change de taux figure
   dans les deux. Le plan donne le domicile aux trajectoires quand une seule opération est en
   cause.
5. **Les données du crédit restent où elles sont**, à la fin de « Déduction, crédit et
   suspension », avec les rapports extérieurs qui les suivent : c'est la décision du
   propriétaire du 7 octobre 2026 sur les études. Le récit B n'en porte qu'un renvoi. Si les
   études reçoivent plus tard une place propre, `#sec-tva-credit-donnees`, qui est du
   budgétaire, a vocation à rejoindre le récit B.
6. **Les lignes 364-374 redisent la note de lecture de la figure** (écarts entre séries, trois
   valeurs de 2012, recettes nettes). La redite est de même nature que celle des taux ; elle
   n'est pas traitée ici, faute de mandat, mais elle se voit.

### 7.2 Ce que le repli peut cacher à tort

1. **Le fait générateur** (l. 48-62) commande la lecture de toutes les dates du chapitre ;
   l'encadré du début le dit en une phrase : il reste donc déplié.
2. **Le pourcentage de déduction** : la phrase « l'exportation et les ventes en suspension
   figurent au numérateur » (l. 209) est une idée de premier plan, reprise par la section du
   régime suspensif. Elle doit ressortir du bloc.
3. **La recherche dans la page** : un contenu replié peut échapper à la recherche du
   navigateur (point ouvert du chantier). Avec quatorze blocs repliés, c'est l'essentiel des
   références du chapitre qui devient invisible à Ctrl+F.
4. **Les constats d'ignorance** — grossistes en alimentation générale, date de la loi
   n° 2007-69, délai de visa de 1998 à 2002 — ne doivent pas descendre dans un bloc : le
   premier reste au premier plan ; les deux autres y sont déjà en « non établie ».
5. **Les lignes [OCR] et [notice] entrent dans des registres publiés.** Une ligne de registre
   a l'air d'un fait lu. Soit la ligne dit « seul l'intitulé de ce texte est connu ici », soit
   elle attend. Cela concerne surtout les exonérations de 1989 à 1994 et le tableau C.
6. **L'état du droit.** Il n'existe, établi, que pour la grille des taux, la restitution
   (2023), le régime suspensif et la retenue. Un lecteur qui cherche « ce qui est exonéré
   aujourd'hui » ne le trouvera pas : il faut le lui dire au premier plan.

7. **Un dispositif n'a pas encore sa chronologie complète : les réductions annuelles.** Le
   propriétaire le nomme expressément. Le registre provisoire ne porte que les textes déjà
   cités ; les seize années de décrets attendent le bibliographe et la lecture de sept décrets.
   C'est un écart assumé à l'exigence « ne rien perdre » — rien n'est perdu de ce que le
   chapitre porte, mais la frise n'est pas entière. De même, les registres des exonérations et
   du tableau C dépendent de relectures à l'image.

### 7.3 Ce que la règle du domicile unique ferait perdre ici

1. **La citation au point d'usage.** Le premier plan nommerait « la loi de finances pour
   1996 » sans article : le lecteur qui veut l'article ouvre le bloc. Acceptable si chaque
   mention est suivie d'un renvoi `@tbl-…`, qui déplie.
2. **Le grain.** La règle n'est tenable qu'au grain « texte + article ». Une même loi de
   finances a jusqu'à cinq domiciles (celle de 1996 : art. 37 à 39, 40, 41 et 42, 43 à 46).
   Au grain du texte, elle est inapplicable.
3. **Les articles à plusieurs dispositifs** (§ 4, cas 1) : il faut désigner un domicile et
   écrire ailleurs une ligne de renvoi. Six articles au moins sont dans ce cas.
4. **Les blocs de modalités** (option et fait générateur ; pourcentage de déduction) ne sont
   pas des registres et portent pourtant des citations : il faut les admettre comme exceptions,
   ou y renvoyer au registre du dispositif.
5. **Les citations qui ne sont pas du droit** — rapports, études, séries — n'ont pas de
   registre : elles restent au point d'usage, dans le récit B et les notes de lecture.
6. **Les citations littérales.** Quand le premier plan cite les mots de la loi (« en un seul
   corps », « quels qu'en soient les buts ou les résultats », la phrase du rapport sur les
   dépenses fiscales), la référence doit rester à côté de la citation.
7. **Le tableau engendré `tbl-tva-taux`** ne peut pas porter de références : le registre des
   grilles est la liste qui le suit. La règle doit admettre qu'un registre soit une liste.
8. **La pagination manque pour la moitié du chapitre.** Les sections sur le champ et les taux
   citent sans page ; N2 les donne presque toutes. Un registre « texte, article, page » suppose
   un passage du bibliographe sur ces sections.
9. **Deux contrôles automatiques** peuvent en dépendre : la résolution des citations au rendu
   (une clé citée dans un seul bloc doit toujours résoudre) et l'ancre `RECHERCHE`.

---

## 8. Retour sur le rôle

Ce qui manquait dans `docs/agents/architecte.md` pour faire ce travail :

1. **Un registre de destination.** La consigne ne demande de classer que les textes. Sur un
   chapitre déjà écrit, l'unité à suivre est l'alinéa, le tableau, la figure, le commentaire
   caché ; sans ce registre, « rien n'est supprimé » ne se prouve pas. Le cas du chapitre déjà
   écrit tient en une ligne dans la consigne : il lui faut ses propres règles — identifiants à
   conserver, renvois entrants, ancres `RECHERCHE`, `TODO`, tableaux engendrés sans colonne
   « Portée », recouvrements avec les chapitres voisins.
2. **Le cas à plusieurs dispositifs.** « Les séparer d'abord », dit la consigne, sans dire
   comment. Il a fallu poser ici deux niveaux de ruptures (le chapitre, le dispositif), un
   gabarit de section et un registre par dispositif. Corollaire : « trois à six ruptures pour
   un dispositif » ne dit pas si le mot désigne le chapitre ou ses parties.
3. **Les degrés de lecture.** « Un texte connu par son seul intitulé ne peut pas porter une
   rupture » : les notes ont sept degrés ([image], [texte], [OCR], [AR], [notice], code
   consolidé, « probable »). La consigne doit dire lesquels autorisent une rupture et lesquels
   une ligne de registre.
4. **« Ce que la loi cherche, dans ses termes ».** Les notes ne relèvent presque jamais
   l'intitulé des articles ni l'exposé des motifs : huit cases sur treize disent ici « objet
   non relevé ». L'architecte classe alors sur les effets, non sur l'intention. C'est une
   demande à faire au documentaliste en amont, et la fiche doit avoir une rubrique
   « questions au documentaliste » (§ 9).
5. **Où regarder pour le récit économique**, et avec quelle gradation :
   `precis/_seriescache/catalog.snapshot.yml`, le catalogue de `tunisia-data`,
   `backlog-precis.md` (qui corrige aussi les notes : il faut le lire) ; faisable maintenant,
   après un travail de données, à documenter d'abord.
6. **L'état du droit qui manque.** La consigne le place au premier plan sans prévoir qu'il ne
   soit pas établi.

Ce qui est ambigu : « écrite à la suite de la note documentaire » ne vaut pas quand il y a
trois notes, ni quand un fichier à part est demandé. Ce qui manque à « ce que tu rends » : les
risques du repli et la compatibilité avec la règle des références. Rien n'est de trop.

---

## 9. Questions au documentaliste, nées de ce plan

1. Intitulés des articles, ou exposé des motifs, pour : loi de finances pour 1996, art. 43 à
   46 ; pour 1995, art. 56 ; pour 2016, art. 30 et 31 ; pour 2017, art. 16 ; pour 2014,
   art. 34 ; pour 2016, art. 22 et 34 ; pour 2010, art. 23 ; décret-loi de finances pour 2022,
   art. 52.
2. Loi de finances pour 2021, art. 27 : dons aux associations (N2) ou article 13 *quinquies*
   (N3) ? Loi de finances pour 1994 : clause d'effet lue (N2, art. 77) ou non relevée (N3) ?
3. Le tableau A en vigueur, poste par poste.
4. Une source du partage entre TVA intérieure et TVA à l'importation.
5. Les sept décrets annuels [probable] de 2000 à 2005 et le décret n° 97-1339, pour que le
   registre des réductions annuelles paraisse entier.

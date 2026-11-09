# Note documentaire — annexe « Les comptes de la nation »

Note du documentaliste pour l'option C de la vision compta nationale
(`docs/notes/vision-compta-nationale.md`, décision du 06/11/2026). Elle rassemble et source la
matière d'une **annexe transversale** qui documente la comptabilité nationale tunisienne
au-delà du PIB-dénominateur (déjà traité par `annexe-pib.qmd` / `annexe-pib.md`). Elle ne rédige
pas l'annexe et ne touche aucun `.qmd`.

**Niveaux de preuve** (mêmes conventions qu'`annexe-pib.md`) :
- **[lu]** — phrase ou tableau lu dans la publication, page du fichier PDF ;
- **[calculé]** — tiré d'une série de `tunisia-data` par un calcul, fichier+colonne donnés ;
- **[rapproché]** — déduit d'une égalité/identité comptable à partir de valeurs lues ;
- **[non établi]** — rien de lu ; où chercher est dit au § 5.

Abréviations de `~/projets/tunisia-data` : `R/` = `data/raw/`, `P/` = `data/processed/`.
Édition de référence chiffrée : `R/ins-publications/comptes-de-la-nation/2019-2023.pdf`
(« Les Comptes de la Nation, base 2015, comptes nationaux 2019-2023 »), **PDF page = folio
imprimé** (vérifié : p.24/27/30/55/69/100-101). Source méthodologique de référence :
`R/ins-publications/comptes-de-la-nation/INS_2021-03_cnat_presentation_SCNT97.pdf` (25 p.,
« Présentation générale du système de comptabilité nationale tunisien, SCNT97 »).

---

## 0. Constats à retenir

1. **Le SCNT est un système de comptes articulés, pas un stock d'agrégats.** L'INS organise la
   matière en **quatre secteurs institutionnels résidents** (SNF, sociétés financières, APU,
   ménages y.c. ISBLSM) + le **reste du monde**, et en une **séquence de six comptes courants et
   deux comptes d'accumulation**, chacun fermé par un solde reporté dans le compte suivant :
   valeur ajoutée → revenu d'exploitation → solde des revenus primaires (revenu national) →
   revenu disponible brut → épargne → capacité/besoin de financement (SCNT97, p.4-5, p.13-17)
   **[lu]**. C'est l'ossature que l'annexe doit exposer.
2. **Les trois approches du PIB bouclent exactement sur le même niveau.** Pour 2021 (base 2015),
   PIB = **131 544,6 MD** par les trois voies : demande (emplois), revenus, et production (VA
   totale + impôts nets sur produits), à l'arrondi près (§ 2) **[lu]+[rapproché]**.
3. **Les comptes des secteurs institutionnels sont déjà là, détaillés et sourçables** : chaque
   édition base 2015 publie la **séquence complète par secteur** (ménages, SNF, SF, APU,
   organismes de sécurité sociale, reste du monde), en millions de dinars, emplois et ressources
   (2019-2023, p.100 sq.) **[lu]**. Les CSV de `P/.../cnat-consolide/` les recoupent, **mais ne
   portent le plus souvent que les variations en %**, pas les niveaux — et mélangent des éditions
   de bases différentes (§ 3, § 5).
4. **Le périmètre « administrations publiques » des comptes ≠ périmètres budgétaires du précis.**
   Les APU des comptes consolident administration centrale + collectivités locales + organismes de
   sécurité sociale ; seule la FBCF les décompose (2019-2023, p.69) **[lu]**. La concordance avec
   les volumes (masse salariale, finances locales, prestations) est donc partielle et doit être
   déclarée case par case (§ 4).
5. **L'annexe complète `annexe-pib.qmd`, elle ne la refait pas.** Tout ce qui touche aux bases
   (1983/1997/2015), rétropolations et « quel PIB dans quelle source » reste dans `annexe-pib.md`
   et doit être renvoyé, pas dupliqué.

---

## 1. L'architecture des comptes (secteurs, séquence)

### 1.1 Les secteurs institutionnels

Définition INS : « regroupements d'unités capables de posséder des biens et des actifs […]
d'exercer des activités économiques […] du fait de leur autonomie de décision » ; les unités
résidentes sont réparties en **quatre secteurs** selon fonction principale et ressources
principales (SCNT97, p.5) **[lu]** :

| Secteur (code INS) | Fonction principale | Ressource principale |
|---|---|---|
| Sociétés non financières (SNF) | produire des biens et services marchands | vente de biens et services |
| Sociétés financières (IF) | financer / assurer | revenus de capitaux ; primes et cotisations d'assurance |
| Administrations publiques (APU) | produire des services non marchands ; redistribuer | prélèvements obligatoires (impôts, cotisations sociales) |
| Ménages (y.c. entreprises individuelles) + ISBLSM | consommer ; produire (entreprises individuelles) ; services non marchands (ISBLSM) | rémunération du travail ; vente ; dons et cotisations |

**[lu]** (SCNT97, tableau p.5-6). L'INS note que **les APU incluent les administrations de
sécurité sociale** et que **les ISBLSM sont rattachées aux ménages** (SCNT97, p.5) **[lu]** — deux
points cruciaux pour le § 4. Le **reste du monde** forme un cinquième compte, « unique », qui
retrace toutes les opérations entre résidents et non-résidents (SCNT97, p.6) **[lu]**.

Dans les tableaux publiés, l'INS détaille en outre des **sous-secteurs** : organismes de sécurité
sociale isolés dans les APU (comptes p.100-101) ; au sein de la FBCF, APU = administration
centrale + collectivités locales + organismes de sécurité sociale (p.69) **[lu]**.

### 1.2 La séquence des comptes et ses soldes

L'INS construit « une séquence de six comptes courants et de deux comptes d'accumulation »
(SCNT97, p.13) ; « le solde d'un compte est reporté dans le compte suivant et assure
l'articulation de la séquence » (SCNT97, p.4) **[lu]** :

| # | Compte | Objet (mots de l'INS) | Solde |
|---|---|---|---|
| 1 | Production | production − consommation intermédiaire | **Valeur ajoutée (brute)** |
| 2.1 | Exploitation | partage de la VA entre facteurs ; emplois = rémunération des salariés + impôts nets sur production | **Revenu d'exploitation** (/ revenu mixte pour les entreprises individuelles) |
| 2.2 | Affectation des revenus primaires | ajoute revenus de la propriété (intérêts, dividendes, loyers) | **Solde des revenus primaires / Revenu national** |
| 3 | Distribution secondaire du revenu | transferts courants : impôts sur revenu/patrimoine, cotisations et prestations sociales, autres transferts | **Revenu disponible brut** |
| (4bis) | Distribution du revenu en nature | transferts sociaux en nature | Revenu disponible ajusté |
| 4 | Utilisation du revenu | revenu disponible − dépense de consommation finale | **Épargne (brute)** |
| 5.1 | Capital | épargne + transferts en capital − FBCF − actifs non produits | **Capacité ou besoin de financement** |
| 5.2 | Financier | variations de créances et de dettes | **Solde des créances et dettes** |

**[lu]** (SCNT97, p.4 « SÉQUENCE DES COMPTES » ; développement p.13-17). Chaque solde peut être
calculé **brut ou net** (après déduction de la consommation de capital fixe / amortissements)
(SCNT97, p.16) **[lu]**.

### 1.3 Le passage VA → PIB → RNB → RNDB → épargne

L'INS pose l'identité de l'approche « revenu » de la valeur ajoutée totale :
« Valeur ajoutée = Rémunération des salariés + Impôts indirects nets + Excédent brut
d'exploitation » (SCNT97, p.14) **[lu]**. Agrégé et complété des impôts sur produits et de
l'extérieur, le chaînage publié est (2019-2023, p.30) **[lu]** :

- **PIB aux prix du marché** (p.m.) → + revenus des facteurs reçus de l'extérieur nets →
  **Revenu National (RNB)** → + autres transferts courants extérieurs nets → **Revenu National
  Disponible Brut (RNDB)** → − consommation finale → **Épargne nationale brute** ; déduction des
  amortissements → versions **nettes** (RNN, RNDisp., épargne nette).

### 1.4 Les tableaux de synthèse (cadre central)

Trois grands tableaux ferment le système (SCNT97, p.1, p.7-8) **[lu]** :
- **TRE** — tableau des ressources-emplois (branches × produits), équilibre offre/demande par
  produit, prix de base côté ressources, prix d'acquisition côté emplois (SCNT97, p.7-10) ;
- **TCEI** — tableau des comptes économiques intégrés, « résume toute la séquence des comptes des
  différents secteurs institutionnels », receveurs face aux verseurs opération par opération
  (SCNT97, p.7) ;
- **TOF** — tableau des opérations financières, flux nets de créances / de dettes par secteur
  (SCNT97, p.8). Le Volume B des éditions base 2015 (`CNAT_VolB_2015-2020.pdf`) porte ces
  opérations financières **[lu]**.

> Renvoi : les **bases** du SCNT (1983/SCN 1968, 1997/SCN 1993 « SCNT97 », 2015/SCN 2008), les
> rétropolations et « quel PIB dans quelle source » sont traités dans `annexe-pib.md` (§ 1-4).
> Ne pas dupliquer. La présente note documente **l'architecture** du système, pas l'histoire des
> bases.

---

## 2. Les trois approches du PIB et leur bouclage (exemple 2021, base 2015)

L'INS énonce que l'approche « revenu » est « complémentaire des approches production et demande,
qui sont équilibrées dans le Tableau des Entrées-Sorties » (SCNT97, p.14) **[lu]**. Les trois
convergent sur le PIB. Exemple **année 2021, base 2015**, édition 2019-2023 (valeurs en MD) :

**(a) Approche demande / emplois** (2019-2023, p.24) **[lu]** :

| Poste | 2021 |
|---|---|
| Consommation finale globale | 123 950,6 |
| + Formation brute de capital fixe | 20 857,6 |
| + Variation de stocks | −13,2 |
| + Exportations | 54 959,6 |
| − Importations | 68 210,1 |
| **= PIB (p.m.)** | **131 544,6** (somme = 131 544,5) **[rapproché]** |

**(b) Approche revenus** (2019-2023, p.27) **[lu]** :

| Poste | 2021 |
|---|---|
| Rémunération des salariés | 55 588,7 |
| + Impôts sur la production et les importations | 17 573,2 |
| − Subventions | 6 347,3 |
| + Revenu d'exploitation | 64 730,1 |
| **= PIB (approche revenus)** | **131 544,6** (somme = 131 544,7) **[rapproché]** |

**(c) Approche production / valeur ajoutée** (2019-2023, p.55 + p.27) **[lu]+[rapproché]** :
VA totale des secteurs résidents = 122 304,7 (SNF 43 881,5 + SF 5 133,3 + APU 25 379,2 +
Ménages 47 910,7) ; **PIB = VA totale + impôts sur les produits nets de subventions** ⇒ impôts
nets sur produits ≈ 131 544,6 − 122 304,7 = **9 239,9** **[calculé]**.

> Nota méthodologique : l'approche revenus (p.27) décompose la VA par secteur avec des niveaux
> légèrement différents de la VA « par secteur institutionnel » de la p.55 (somme 120 318,7 vs
> 122 304,7) — deux présentations de l'INS à ne pas additionner entre elles. Le PIB total, lui,
> est identique (131 544,6). À documenter comme tel, sans trancher **[lu]**.

---

## 3. Les grandeurs citables (définition, base, série d'entrepôt)

Niveaux 2021, base 2015 (2019-2023), sauf mention. **Base à déclarer systématiquement** (règle
`annexe-pib.md`).

| Grandeur | Définition INS | Niveau 2021 (MD) | Page [lu] | Série d'entrepôt |
|---|---|---|---|---|
| **PIB (p.m.)** | solde des trois approches | 131 544,6 | p.24/27/30 | `P/ins-comptes-nationaux/pib_courant_par_base.csv` (base 2015) **[calculé]** |
| **Revenu National (RNB)** | PIB + revenus facteurs ext. nets | 128 107,2 | p.30 | `P/.../cnat-consolide/revenu-national.csv` (niveaux, **mais OCR bruité**, § 5) |
| **RNDB** | RNB + autres transferts courants ext. nets | 137 394,5 | p.30 | `revenu-national.csv` / `revenus-disponibles-bruts.csv` |
| **RNDB des ménages** | part ménages du RNDB | 103 772,9 | p.30 | `cnat-consolide/comptes-des-menages.csv` (variations %) |
| **Consommation finale** | dépense de conso finale (publique + privée) | 123 950,6 | p.24/30 | `les-emplois-du-pib-nominal-aux-prix-courants.csv` (**variations %**) |
| **Épargne nationale brute** | RNDB − consommation finale | 13 443,9 | p.30 | `revenu_national.csv` (à reconstruire en niveaux) |
| **VA par secteur institutionnel** | solde du compte de production, par secteur | APU 25 379,2 ; Ménages 47 910,7 ; SNF 43 881,5 ; SF 5 133,3 | p.55 | `valeurs-ajoutees-par-secteur-institutionnel-aux-prix-co.csv` (**variations %**) |
| **Rémunération des salariés (total)** | emplois du compte d'exploitation | 55 588,7 | p.27 | `P/.../remuneration_salaries_editions.csv` (niveaux, par édition) **[calculé]** |
| **FBCF** | compte de capital | 20 857,6 | p.24/69 | `formation-brute-de-capital-fixe-*` ; `investissement_financement.csv` |
| **Subventions sur les produits** | poste soustractif de l'approche revenus | 6 347,3 | p.27 | `cnat-consolide/produit-interieur-brut-selon-l-approche-des-revenus.csv` (**variations %**) |

**Caveat transversal [calculé]** : dans `P/.../cnat-consolide/`, les CSV `revenu-national.csv`,
`revenus-disponibles-bruts.csv`, comptes des ménages/SNF/SF/sécu sociale **mélangent des éditions
de bases différentes** — `cnat_2012-2016-tables` et `cnat_2013-2017-tables` sont en **base 1997**
(vérifié : couverture « Base 1997 » des `CNAT_2012-2016.pdf` et `CNAT_2013-2017.pdf`),
`cnat_vola_2015-2020-tables` et suivantes en **base 2015**. Toute série de niveaux tirée de ces CSV
porte donc une **rupture de base à 2014/2015** non étiquetée. Pour les niveaux, préférer la lecture
directe du PDF de l'édition pertinente ; pour les séries, étiqueter par base (cf. `annexe-pib.md`
§ 4). Plusieurs CSV sont, en outre, des **taux de variation**, pas des niveaux (en-têtes
« variation en % »).

---

## 4. Table de concordance volumes ↔ comptes

Chaque ligne : la grandeur d'un volume du précis, sa case dans les comptes, le niveau 2021 lu, la
page, et le **degré de concordance** (le périmètre comptable n'est pas le périmètre budgétaire).

| Volume du précis | Case des comptes (secteur / opération) | Niveau 2021 (MD) | Page [lu] | Concordance |
|---|---|---|---|---|
| **Rémunérations publiques** (masse salariale) | APU — *Rémunération des salariés* (compte d'exploitation / approche revenus APU) | 21 710,6 | p.27 | **Partielle.** CN APU = central + local + sécu, consolidé ; CN rémunération = salaires bruts + cotisations employeurs (dont imputées). ≠ masse salariale budgétaire de l'État. À rapprocher, pas à égaler. |
| | APU — *Valeur ajoutée brute* (poids des APU dans le PIB) | 25 379,2 | p.55 | contextuel |
| **Prestations sociales / Retraites** | Organismes de sécurité sociale — *Prestations sociales en espèce* (emplois, distribution secondaire) | 10 577,5 | p.100 | **Bonne** pour le périmètre sécu sociale (CNSS+CNRPS+CNAM consolidés), hors prestations servies hors organismes. |
| **Cotisations sociales** | Organismes de sécurité sociale — *Cotisations sociales* (ressources) ; Ménages — *Cotisations sociales* (emplois) | sécu : 12 197,7 ; ménages versées : 13 970,4 | p.101 ; p.102 (l.1347/1426) | **Bonne** au niveau macro ; distingue cotisations effectives (12 848,7) et imputées (1 121,7), ménages p.102. |
| **Compensation** | Approche revenus — *− Subventions* ; emplois du PIB — subventions sur produits | 6 347,3 | p.27 | **Partielle.** Subventions CN = subventions sur produits (dont énergie/produits de base) ; périmètre ≠ dépenses de compensation budgétaires. Croiser avec `docs/notes/compensation*`. |
| **Finances locales** | APU, sous-secteur *Collectivités locales* | FBCF 425,7 | p.69 | **Faible.** Pas de séquence complète de comptes pour les collectivités locales dans les éditions lues ; seul le poste FBCF les isole. Concordance limitée à l'investissement local. |
| **Marché du travail / informel** | Ménages — *Revenu d'exploitation / revenu mixte* (entreprises individuelles) | 39 961,6 | p.102 | contextuel ; entreprises individuelles logées chez les ménages. |

**[lu]** pour tous les niveaux. La table est **descriptive** : elle dit où une grandeur se lit dans
les comptes, pas qu'elle égale le chiffre budgétaire du volume. Le garde-fou éditorial de la vision
(« documenter, pas commenter ») s'applique.

---

## 5. Lacunes et pistes (backlog)

1. **REPORT — niveaux consolidés propres par base.** Les CSV `cnat-consolide/*` sont, pour la
   plupart, des **taux de variation** et, quand ils portent des niveaux, **mélangent base 1997 et
   base 2015** (rupture non étiquetée à 2014/2015) et montrent du **bruit OCR** (ex.
   `revenu-national.csv` : lignes parasites « administration publique 20 032,7 20 297,5 »,
   « revenu disponible brut 1 153 » dans les comptes SNF). → Construire, dans `tunisia-data`, des
   **séries de niveaux par secteur et par base**, extraites proprement des PDF (camelot/tabula sur
   les pages de comptes des éditions), avec colonne `base_pib`. OCR à refaire sur les tables de
   comptes institutionnels.
2. **REPORT — collectivités locales.** Aucune séquence complète de comptes pour le sous-secteur
   collectivités locales dans les éditions lues (seul le poste FBCF les isole, p.69). Vérifier si
   le Volume B ou une publication APU/finances locales de l'INS (`sources/finances-locales-ins.md`)
   détaille leur compte ; sinon, noter l'absence.
3. **LACUNE — éditions glissantes manquantes.** Base 2015 présentes : 2015-2020, 2017-2021,
   2018-2022, 2019-2023, 2020-2024, 2021-2025. **Manquent** les millésimes **2016-2020 / 2016-2021**
   et **2014-2018** ; la fiche `sources/ins-comptes-nationaux-publications.md` note que les pages
   `les-comptes-de-la-nation-2015-2020` et `…-en-2018` n'exposent aucun PDF. Base 1997 : éditions
   2005-2009 → 2013-2017 présentes ; antérieures à 2005-2009 (base 1997) non identifiées.
4. **LACUNE — compte du reste du monde.** Non détaillé dans la présente passe (table
   `cnat-consolide/compte-des-o-p-e-r-at-i-o-n-s-avec-l-e-x-t-e-r-i-e-u-r.csv`, OCR très bruité) ;
   à sourcer sur le PDF (compte des opérations avec l'extérieur) pour l'articulation
   épargne nationale ↔ besoin de financement de la nation.
5. **REPORT — catalogue tunisia-data.** `INS_2021-03_cnat_presentation_SCNT97.pdf` et
   `INS_2021-08-15_note_changement_de_base_2015.pdf` sont **présents dans `R/` mais sans ligne
   d'URL d'origine** dans `sources/ins-publications-urls.csv` (seules les 21 éditions glissantes y
   figurent). → Compléter le catalogue avec l'URL source et le SHA-256 (SHA du presentation
   SCNT97 déjà relevé : `43873eec90f16205239d3453094ef62cc20d7b63333c81826f866b44408e324a`).
6. **PISTE — comptes de patrimoine.** L'INS précise « seuls les comptes de flux sont disponibles »,
   les comptes de patrimoine « ne sont pas encore élaborés » (SCNT97, p.4) **[lu]**. À signaler
   dans l'annexe comme limite connue du système (pas de bilan patrimonial national).
7. **PISTE — base 2015, méthodologie dédiée.** La présentation SCNT97 décrit la base 1997 ; pour la
   base 2015, la source méthodologique est `INS_2021-08-15_note_changement_de_base_2015.pdf`
   (= réf. `ins-changement-base-2015`). Vérifier si l'édition `CNAT_2017-2021.pdf` contient une
   « Méthodologie des comptes nationaux sous la nouvelle base 2015 » (titre lu en sommaire) à citer
   en complément.

**Recherches infructueuses (`docs/recherches.yml`) : sans objet.** Le périmètre est de la
documentation statistique INS (pas de texte juridique JORT à traquer) ; aucune fiche rejouable
n'est requise. Les manques relèvent d'**éditions/tables à collecter** (points 2-4 ci-dessus), pas
de textes légaux introuvables.

---

## 6. Références candidates (CSL-JSON)

**Déjà présentes dans `precis/fr/references.json`** (à réutiliser, ne pas recréer) :
- `ins-cnat-2015` — « Les comptes de la nation » (éditions successives 2001-2005 → 2021-2025),
  INS. **Source primaire principale de l'annexe** (tableaux des comptes, agrégats).
- `ins-changement-base-2015` — « Les comptes nationaux changent de base. Note explicative…,
  base 2015 », INS, 15 août 2021. **Source méthodologique base 2015.**
- `ins-pib-base-2015-2010-2020` — classeur « Comptes nationaux annuels en base 2015, 2010-2020 ».
- `undata-sna` — séries SNA transmises aux Nations unies (profondeur historique par base).

**À créer** (proposition pour le bibliographe) :

```json
{
  "id": "ins-scnt97-presentation",
  "type": "report",
  "title": "Présentation générale du système de comptabilité nationale tunisien (SCNT97) : secteurs institutionnels, séquence des comptes, tableaux de synthèse",
  "author": [{ "literal": "Institut national de la statistique" }],
  "publisher": "Institut National de la Statistique, Tunisie",
  "issued": { "date-parts": [[2021]] },
  "number-of-pages": "25",
  "note": "citation-key: ins-scnt97-presentation\nDocument méthodologique de 25 p. extrait/joint aux Comptes de la nation base 1997, décrivant le SCNT97 : les quatre secteurs institutionnels (SNF, sociétés financières, APU y.c. sécurité sociale, ménages y.c. ISBLSM) et le reste du monde, la séquence des comptes courants et d'accumulation avec leurs soldes (valeur ajoutée, revenu d'exploitation, revenu national, revenu disponible brut, épargne, capacité/besoin de financement), les tableaux TRE/TCEI/TOF et les équilibres ressources-emplois. Fichier : tunisia-data, data/raw/ins-publications/comptes-de-la-nation/INS_2021-03_cnat_presentation_SCNT97.pdf ; SHA-256 43873eec90f16205239d3453094ef62cc20d7b63333c81826f866b44408e324a. URL d'origine à compléter au catalogue (cf. § 5.5). Pages citées : p.4-6 (secteurs, séquence), p.7-10 (TRE/TCEI/TOF, ERE), p.13-17 (développement de la séquence)."
}
```

> Si le bibliographe préfère, `ins-scnt97-presentation` peut être signalé comme **sous-partie
> méthodologique de `ins-cnat-2015`** plutôt qu'entrée autonome ; je recommande une entrée
> distincte car c'est la source canonique de l'architecture (secteurs + séquence), citée ici à
> répétition.

---

## 7. Notions à glossaire

Terme FR (AR pressenti), définition canonique, source. Seul **« Produit intérieur brut »** existe
déjà au glossaire (`precis/glossaire.yml`, l.5378) ; **« Épargne nette »** y figure dans un sens
budgétaire (règle d'or) à ne pas confondre avec l'épargne des comptes nationaux. Les autres sont à
créer.

| Terme FR | AR pressenti | Définition canonique pressentie | Source |
|---|---|---|---|
| Secteur institutionnel | القطاع المؤسسي | regroupement d'unités à autonomie de décision (SNF, SF, APU, ménages+ISBLSM, reste du monde) | SCNT97, p.5 · `ins-scnt97-presentation` |
| Valeur ajoutée (brute) | القيمة المضافة (الخام) | solde du compte de production : production − consommation intermédiaire | SCNT97, p.14 |
| Revenu d'exploitation / revenu mixte | فائض الاستغلال / الدخل المختلط | solde du compte d'exploitation (rémunération du capital ; revenu mixte pour l'entreprise individuelle) | SCNT97, p.15 |
| Revenu national (brut, RNB) | الدخل الوطني | PIB + revenus des facteurs reçus de l'extérieur nets | 2019-2023, p.30 |
| Revenu national disponible brut (RNDB) | الدخل الوطني المتاح الخام | RNB + autres transferts courants extérieurs nets | 2019-2023, p.30 |
| Revenu disponible brut (d'un secteur) | الدخل المتاح الخام | solde du compte de distribution secondaire du revenu | SCNT97, p.16 |
| Consommation finale (dépense / effective) | الاستهلاك النهائي | emploi du revenu disponible (dépense) / corrigée des transferts sociaux en nature (effective) | SCNT97, p.16-17 |
| Épargne (nationale) brute | الادخار (الوطني) الخام | RNDB − consommation finale ; solde du compte d'utilisation du revenu | 2019-2023, p.30 ; SCNT97, p.16 |
| Formation brute de capital fixe (FBCF) | التكوين الخام لرأس المال الثابت | acquisitions nettes d'actifs fixes, compte de capital | SCNT97, p.14 ; 2019-2023, p.24/69 |
| Capacité / besoin de financement | القدرة / الحاجة إلى التمويل | solde du compte de capital reporté au compte financier | SCNT97, p.17 |
| Impôts sur les produits nets de subventions | الضرائب على المنتجات صافية من الدعم | écart entre PIB et VA totale aux prix de base | SCNT97, p.9-10 ; 2019-2023, p.27/55 |

> Le terminologue vérifiera les formes arabes canoniques sur une édition arabe des Comptes de la
> nation si disponible (les éditions lues ici sont en français). À défaut, les formes ci-dessus
> sont des propositions à valider.

---

### Rappel de périmètre

Cette note ne modifie aucun `.qmd` ni fichier du précis. Elle fournit la matière sourcée d'une
annexe « Les comptes de la nation » (option C) qui **documente le système statistique** et
**renvoie à `annexe-pib.qmd`** pour tout ce qui concerne les bases du PIB. Le modèle openfisca
n'entre pas dans le propos.

---

## Reports du chantier « comptes par secteur » (2026-11-09)

Section ajoutée : `#sec-cn-comptes-secteurs` — la séquence des comptes désagrégée par secteur
institutionnel (SNF, SF, APU consolidée, ménages, reste du monde), navigateur interactif par
année, base 2015, série `cnat-comptes-secteurs` (générateur `scripts/generate_cnat_comptes_secteurs.py`).
Les soldes sont lus (jamais recalculés).

**Report prioritaire — compte des ménages incomplet.** Dans les tables disponibles (table emplois
par édition n° 104 *et* fichier consolidé `comptes-des-menages.csv`), le compte des ménages s'arrête
de fait au revenu d'exploitation/mixte : la **distribution secondaire** (prestations sociales
reçues, cotisations, impôts courants) n'est pas captée, si bien que le **revenu disponible brut**
(30 298,8 MD en 2021) est très sous-estimé et que l'**épargne brute** ressort égale au RDB (fausse
pour les ménages, qui consomment l'essentiel de leur revenu ; pour les sociétés, épargne = RDB est
normal, faute de consommation finale). La **consommation finale des ménages** et la **capacité ou
besoin de financement** sont absentes. Ces trois lignes (revenu disponible, épargne, capacité) sont
donc **masquées** dans le navigateur pour les ménages, avec caveat. → **à faire** : ré-extraire le
compte des ménages (distribution secondaire et comptes d'utilisation/capital) des **PDF INS**
(`R/ins-publications/comptes-de-la-nation/`), les CSV OCR ne suffisant pas. Les prestations versées
par l'APU (11 752,7 MD en 2021) sont, elles, bien captées côté APU.

**Report secondaire.** Profondeur historique : la série `cnat-comptes-secteurs` ne remonte qu'à
2012 (base 1997) / 2015 (base 2015), limite des tables OCR ; antérieur à extraire des PDF base 1997
(éditions 2001-2005 → 2011-2015) si une série plus longue est voulue.

### Mise à jour (2026-11-09) — report ménages RÉSOLU + extension 2005

- **Bug ménages corrigé en amont.** Cause : dans `tunisia-data/scripts/consolidate_cnat.py`, les
  titres de comptes de secteur (composés lettre-à-lettre dans les PDF) tombaient tous dans un seul
  seau de slug, et la sous-table « entreprises individuelles » avait capté le slug `comptes-des-menages`.
  Correctif : résolution du slug par relecture du titre réel dans le header compagnon. Le compte
  **complet** des ménages est régénéré (VA 2012 = 29 307,3 ; RDB ≠ épargne ; consommation finale
  présente). Autres secteurs byte-identiques. **Colonne ménages réaffichée** dans le navigateur.
- **Bug de glob corrigé aussi** (`cnat_*-tables` → `cnat[-_]*-tables`) : l'édition `cnat-2020-2024`
  (tiret) n'était jamais lue → **tous** les secteurs s'arrêtaient à 2023. Désormais couverture
  **2012-2024** pour tous.
- **Extension 2005-2011** (base 1997) intégrée pour les 5 secteurs depuis l'extraction PDF validée.
  Navigateur : **2005-2024**, base étiquetée par année.
- **Fichiers tunisia-data non committés** (revue humaine) : `scripts/consolidate_cnat.py` modifié ;
  `cnat-consolide/comptes-des-menages.csv` corrigé ; 7 comptes de secteur enfin séparés (nouveaux
  fichiers) ; 10 fichiers-seau orphelins supprimés.
- **Report restant** : le **revenu disponible brut des ménages** est absent 2020-2023 (ligne non
  extraite de l'édition INS 2019-2023 — lacune d'OCR en amont, pas de consolidation) ; épargne,
  consommation finale et capacité de financement y sont présentes. Ré-océrisation ciblée à prévoir.

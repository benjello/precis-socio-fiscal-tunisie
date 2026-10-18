# L'éducation, version 1 : fiches de plan des quatre chapitres

Rôle architecte, 17 octobre 2026, branche `chantier/education-v1`. Quatre fiches, une par fichier
déclaré dans `precis/fr/education/_quarto.yml` : `index.qmd`, `_histoire.qmd`, `_aides.qmd`,
`_depense.qmd`. Le rédacteur écrit à l'intérieur de ces fiches ; il n'ajoute aucun fait.

**Matière.** Le plan global (`education-plan-2026-10-17.md`) donne le cadre, le tableau de voisinage
et la doctrine. Quatre notes documentaires le corrigent quand elles le contredisent, parce qu'elles
ont lu les textes : `education-histoire-…` (« note H »), `education-aides-scolaires-…` (« note S »),
`education-aides-universitaires-…` (« note U »), `education-depense-…` (« note D » et ses 57 CSV,
`education-depense-series/`). Un paragraphe de note se cite « H § 1.3 », « U § 3.1 », etc.

**Conventions de la fiche.**

- *Portée* : **rupture** (politique, portée par un article lu) ; **étape** (de quelle rupture) ;
  **ajustement** ; **mise en place** ; **intitulé seul** (texte connu par son intitulé ou ses
  visas : il a sa ligne au registre, il ne porte jamais une rupture).
- *État* : celui de la note (lu, lu à l'image, lu en OCR, index).
- *Ancres de registre* : `r-educ-h-…` (histoire), `r-educ-a-…` (aides), `r-educ-d-…` (dépense).
  Exemple : `[]{#r-educ-h-1991}`.
- *Mots de travail* : « cœur », « épine », « fiche » ne paraissent dans aucun titre ni dans le texte
  rendu. Les titres de synthèse s'appellent « Vue d'ensemble ».
- *Numérotation* : aucune section de niveau 2 n'a une seule sous-section de niveau 3. Les plans
  ci-dessous en tiennent compte.
- *Ce qu'en dit l'économie* : une section d'attente est nommée par chapitre (identifiant réservé).
  L'identifiant vit **dans cette fiche seulement** : rien n'en paraît dans le livre, ni titre, ni
  commentaire.

---

## 0. Les décisions qui valent pour tout le livre

### 0.1 Ce que deviennent les chapitres du plan global absents de la version 1

Le plan global prévoyait neuf chapitres. Cette version en a quatre. Rien n'est perdu : chaque matière
reçoit un domicile.

| Chapitre du plan global | Domicile en version 1 | Ce qui en est rendu |
|---|---|---|
| 1 Histoire | `_histoire.qmd` | tout : grandes réformes de l'enseignement scolaire, puis une section par ordre ou institution |
| 2 Scolaire | `_histoire.qmd`, `@sec-educ-etat-droit` | l'état du droit scolaire en octobre 2026 : obligation, gratuité, cycles, examens, langues, privé |
| 2 Scolaire, § 3 (frais des familles) | `_aides.qmd`, `@sec-educ-frais-familles` | droits d'inscription, d'assurance et de bibliothèque, et leur exonération sous condition de ressources |
| 3 Formation professionnelle | `_histoire.qmd`, `@sec-educ-formation-professionnelle` | la loi de 2008 et l'obligation de 2017 ; la loi de 1993 en registre seulement |
| 4 Supérieur | `_histoire.qmd`, `@sec-educ-superieur` | 1958, 1989, 2008 et le LMD ; gratuité et droits |
| 5 Aides | `_aides.qmd` | tout |
| 6 Dépense | `_depense.qmd` | le budgétaire en entonnoir, les personnels, les ménages |
| 7 Résultats | `_histoire.qmd`, `@sec-educ-eleves` | les effectifs d'élèves et d'étudiants seulement. Taux de scolarisation, examens et abandon ne sont pas documentés par les notes : rien n'est rendu |
| 8 Rapports et études | à part, en fin de `_depense.qmd` | rapports extérieurs (UNESCO-UIS ; Banque mondiale 1995), puis une évaluation (CEQ, enquête 2010), chacun avec sa méthode |

Non rendus faute de note qui les fonde : l'histoire **avant 1958** (aucun texte lu, aucune étude
récupérée — les deux visas de 1958, décrets du 15 septembre 1888 et du 21 janvier 1920, entrent dans
la mise en place, sans plus) ; les **kouttabs** et les **jardins d'enfants** ; les **cours
particuliers** ; les **examens** au-delà de ce que disent les lois lues ; les **collectivités** au-delà
de deux phrases (`@sec-educ-depense-perimetre`).

### 0.2 Sections `.domicile-unique`

- `_histoire.qmd` : chapitre entier (`{#sec-educ-histoire .domicile-unique}`), comme la santé.
- `_aides.qmd` : chapitre entier (`{#sec-educ-aides .domicile-unique}`).
- `_depense.qmd` : **non**. Il cite surtout des sources budgétaires et statistiques, qui restent citées
  sur place. Les trois lois qu'il nomme (loi de finances pour 2026, art. 107 ; loi organique du budget
  de 2019 ; loi de règlement de 2017) sont citées sur place aussi. Si la revue préfère le marquer, il
  faut un petit registre `r-educ-d-…` en fin de chapitre.
- `index.qmd` : non, aucune loi dans le fil.

### 0.3 Références : ce qui ne résout pas aujourd'hui

`_quarto.yml` ne lit que `references.json` (du livre), `../references.json` et `../references.bib`.
**Huit clés réutilisées ne résolvent pas** dans ce livre. Elles vivent dans le `references.json` d'un
autre livre. **Six sont à promouvoir au fonds commun, ou à copier, par le bibliographe, avant la
rédaction** ; deux ne s'emploient pas (`loi2024-19`, `lf-2019`) :

| Clé | Où elle vit | Où elle sert ici |
|---|---|---|
| `constitution2022` | `finances_locales` | `@sec-educ-etat-droit`, `@sec-educ-conseil` (art. 44, 135, 141, 142) |
| `decret-pres2022-691` | `finances_locales` | `@sec-educ-conseil` (promulgation) |
| `loi-2009-32-restauration-formation` | `fiscalite` | `@sec-educ-restauration-scolaire` |
| `bm-1995-pauvrete-annexes` | `retraites` | `@sec-educ-depense-rapports` |
| `jouini-lustig-moummi-shimeles-2017-ceq38` | `compensation` | `@sec-educ-depense-evaluations` |
| `loi2024-18` | `marche_travail` | `@sec-educ-depense-perimetre` (loi de règlement 2017) |
| `loi2024-19` | `marche_travail` | non employée en version 1 |
| `lf-2019` | `fiscalite` | **ne pas l'employer** : la loi de finances pour 2019 a la clé commune `loi2018-56-lf2019` |

**Clés à employer, et non celles que proposent les notes** :

- `loi91-65`, et non `loi-91-65-systeme-educatif` ;
- `lf-2024` (art. 15), et non `loi2023-13-lf2024` ;
- `lf-2026` (art. 107), et non `loi2025-17-lf2026` ;
- `lf-2010`, `lf-2017`, `lf-2018`, `lf-2020`, `loi2018-56-lf2019` pour les lois de finances ;
- `wb-wdi`, avec le code d'indicateur en localisateur, et non `unesco-uis-…` ;
- `decret-loi2024-2`, et non `decret2024-2`, qui désigne un autre texte.

**Non citables en version 1** : `akkari2005-reforme-educative` et `wb-tunisia-per-2020` (PDF non
récupérés, non lus) ; le classeur CEQ 2021 (non publié, sans clé). Aucune de leurs valeurs n'entre au
texte rendu.

### 0.4 Glossaire

Le rédacteur n'emploie que les 62 ancres du bloc « Éducation (passe 1) » de `precis/glossaire.yml`,
plus quatre ancres existantes : `#g-smig`, `#g-amen-social`, `#g-condition-de-ressources`, `#g-epa`.
`#g-epa` désigne bien l'établissement public à caractère administratif, et sert pour les offices.
`#g-pib` existe aussi, pour `_depense.qmd`.

**Le nom de l'office scolaire.** L'entrée `office-oeuvres-scolaires` a pour terme français « Office
des œuvres scolaires », avec « Office des services scolaires » en synonyme. La note S (§ 2.1) retient
**office des services scolaires** (ديوان الخدمات المدرسية) : l'arabe fait foi (loi n° 93-64,
art. 1er), et l'arrêté de 2022 l'écrit ainsi. Le texte rendu dit « office des services scolaires » et
lie vers `#g-office-oeuvres-scolaires`. **Question au terminologue** : inverser terme et synonyme.

### 0.5 Figures : ce qui est faisable maintenant

`figtools.series()` lit le catalogue `precis/_seriescache/`. **Aucun des 57 CSV de la note D n'y
est.** Toute figure qui les emploie est **faisable après un travail de données** : verser les CSV à
`tunisia-data` (`data/processed/education/`), écrire leur fiche dans `sources/`, les inscrire au
catalogue sur le modèle de `ins-budget-sante-2018-2023`, puis écrire
`precis/fr/education/figures/<module>.py` sur le modèle de `sante/figures/depenses_sante.py`.

Déjà au catalogue, à réutiliser :

- `denominateurs-depenses-etat-pib` (dénominateurs de l'État et PIB par segment de base) ;
- `ipc-longue-periode`, pour les dinars constants. Année de référence : **2023** dans les deux
  chapitres chiffrés ;
- `marche-travail-smig-smag`, pour exprimer en dinars les plafonds « SMIG annuel » ;
- `ins-ministere-effectifs`, `ins-ministere-effectifs-2018-2025` (agents des ministères, pas des
  enseignants).

Pour la frise, pas d'aide dans `figtools` : modèle `precis/fr/fiscalite/figures/regimes_incitation.py`.

**Décision : le versement des séries précède la rédaction des sections chiffrées.** Il s'agit de
`sec-educ-eleves`, de `sec-educ-aides-donnees` et des sections `_depense` vue, ministères, nature,
personnels et rapports. Elles attendent leur figure : le rédacteur ne publie aucun chiffre sans sa vue
d'évolution. **Repli, si la revue veut le livre avant le versement** : chaque section porte au texte
principal, non replié, un tableau daté court tiré des CSV (une ligne tous les cinq ans, plus la
dernière année et les années de rupture). Il est suivi de
`<!-- TODO (rédacteur) : remplacer par la figure engendrée fig-educ-… -->`. Le tableau annuel complet
reste dans le bloc replié prévu.

---

## 1. Fiche de plan — `index.qmd` (présentation)

**Objet.** Dire en une page ce que le livre suit — l'éducation comme service gratuit de l'État,
complété par des aides réservées aux élèves et aux étudiants — et où trouver chaque dispositif, dans ce
livre ou dans un livre voisin.

**Titre.** `# Présentation {#sec-educ-presentation}`

Premier paragraphe, sans sous-titre : l'objet ; puis un paragraphe de renvois, en tête, vers les
livres qui portent un sujet voisin (modèle : `sante/index.qmd`).

### 1.1 Les sections

**`## Vue d'ensemble {#sec-educ-vue-ensemble}`**

- *Essentiel* : l'État scolarise gratuitement dans le public, rend l'enseignement obligatoire de six à
  seize ans depuis 1991, et aide une partie des élèves et des étudiants par des bourses, des prêts, la
  restauration et le logement.
- *Vue d'ensemble* : la **carte des dispositifs** (`tbl-educ-carte`), tableau court, non replié :

  | Dispositif | Public | Qui paie | Texte fondateur lu, date d'effet | Section |
  |---|---|---|---|---|
  | Enseignement scolaire public | enfants de 6 à 16 ans (obligation) | État | loi n° 58-118, 1er octobre 1958 ; obligation : loi n° 91-65, art. 7 | `_histoire.html#sec-educ-1958` |
  | Année préparatoire | enfants de 5 à 6 ans | État, collectivités, associations, privé (loi n° 2002-80, art. 17) | loi n° 2002-80, art. 16 à 18 | `#sec-educ-2002` |
  | Enseignement supérieur public | bacheliers | État | loi n° 58-118, ch. III ; loi n° 89-70 ; loi n° 2008-19 | `#sec-educ-superieur` |
  | Formation professionnelle initiale | après la 9e année ; obligatoire jusqu'à 18 ans hors scolarité depuis 2017 | État ; l'entreprise paie l'indemnité d'apprentissage | loi n° 2008-10 ; loi n° 2017-13 | `#sec-educ-formation-professionnelle` |
  | Conseil supérieur et fonds de la réforme éducative | — | budget de l'État ; fonds : dons et prélèvements sur bénéfices | décret-loi n° 2024-2 ; LF 2024, art. 15 | `#sec-educ-conseil` |
  | Bourses scolaires | élèves du public de familles nécessiteuses | État | arrêté du 3 octobre 1966 | `_aides.html#sec-educ-bourses-scolaires` |
  | Cantines et foyers scolaires | élèves du primaire, internes | office des services scolaires depuis le 31 décembre 2016 | décret gouv. n° 2016-664 | `#sec-educ-restauration-scolaire` |
  | Droits d'inscription et exonération | familles ; exonération sous le SMIG | familles, au profit des établissements | loi n° 91-65, art. 24 ; décret n° 92-1185 | `#sec-educ-frais-familles` |
  | Bourse nationale et prêt universitaire | étudiants sous condition de ressources | État | décret n° 57-78 ; décret n° 86-688 ; décret n° 2009-3040 | `#sec-educ-bourse-nationale` |
  | Prêt des caisses de sécurité sociale | enfants des affiliés de la CNSS et de la CNRPS | caisses | décret n° 99-1544 | `#sec-educ-prets-caisses` |
  | Restauration et logement universitaires | étudiants du public | offices des œuvres universitaires | loi n° 70-9 ; lois n° 88-135 à 88-137 | `#sec-educ-oeuvres-universitaires` |

- *Points* (deux) : l'aide passe par deux voies, un service en nature et des transferts ; une partie
  des aides au titre de la scolarité vit dans d'autres livres (`@sec-educ-voisinage`).
- *Ordre de grandeur* : une phrase, avec un lien vers `_depense.html#sec-educ-depense-vue`. La phrase
  donne la part de l'Éducation et de l'Enseignement supérieur dans les dépenses de l'État **en 2009 et en
  2023** (29,3 % et 20,3 %), avec la base de la part du PIB. **Pas de figure dans l'index** : elle a son
  domicile dans `_depense.qmd`, et la figure n'est faisable qu'après versement des séries.
- *Replié* : rien.

**`## Ce que d'autres livres traitent {#sec-educ-voisinage}`**

- *Essentiel* : un dispositif propre au secteur vit ici ; un cas d'un instrument général vit dans le
  livre de l'instrument.
- *Vue d'ensemble* : le **tableau de voisinage** (`tbl-educ-voisinage`), non replié. Cibles vérifiées
  le 17 octobre 2026 :

  | Sujet | Domicile (cible vérifiée) | Ce que ce livre en dit |
  |---|---|---|
  | Aide de rentrée scolaire et universitaire de l'Amen social | `../prestations_sociales/_non_contributives.html#sec-nc-aides` ; tableau `#tbl-nc-rentree-scolaire` | une phrase, un lien (`@sec-educ-aides-ailleurs`) |
  | Abonnement scolaire et universitaire de transport | `../compensation/_transport.html#sec-compensation-transport-scolaire` | une phrase, un lien |
  | Taxe de formation professionnelle | `../cotisations_sociales/_prelevements_salaires.html#sec-cot-tfp` ; fonds de la formation : `../marche_travail/_politiques_emploi.html#sec-mt-pe-fonds-formation` | une phrase, un lien |
  | Agence de la formation professionnelle (1993) | `../marche_travail/_politiques_emploi.html#sec-mt-pe-reforme-1993` | un lien depuis `@sec-educ-formation-professionnelle` |
  | TVA : restauration des étudiants, des élèves et des apprenants (n° 30 bis) | `../fiscalite/_tva_tableaux.html#tbl-tva-tableau-a-origine` | une ligne, un lien |
  | Déduction pour enfant étudiant (impôt sur le revenu) | `../fiscalite/_impot_revenu.html#sec-irpp-famille` | une ligne, un lien |
  | Dépenses fiscales | `../fiscalite/_depenses_fiscales.html#sec-depenses-fiscales` | un lien, sans chiffre (aucune note ne relève de dépense fiscale propre à l'éducation) |
  | Rémunération des enseignants ; indemnité des fournitures scolaires des enseignants ; prime de rentrée universitaire des enseignants (décret gouv. n° 2018-904) | `../remunerations_publiques/_regime_indiciaire.html#sec-regime-indiciaire` | un lien vers le livre. **Aucune section n'y traite des enseignants** : lacune à signaler à ce livre, pas à combler ici |
  | Entretien des écoles par les communes | `../finances_locales/_competences.html#sec-fl-comp-commune` | une phrase, un lien |
  | Prêt universitaire des caisses de sécurité sociale | ici (`@sec-educ-prets-caisses`) | tout ; le livre « Caisses » n'en dit rien, lacune à lui signaler |
  | Incidence par décile de la dépense d'éducation | ici, à part (`@sec-educ-depense-rapports` pour la Banque mondiale, `@sec-educ-depense-evaluations` pour l'étude CEQ) | études citées avec leur méthode ; **aucun livre de la redistribution n'existe**, donc aucun lien |

  Corrections au tableau du plan global : la restauration des élèves relève de la **loi n° 2009-32**,
  non de la loi n° 2009-39 (note S § 0.1) ; les offices des œuvres universitaires restent ici, car les
  textes en font des établissements « à caractère administratif » (note U § 1.6, Q7).
- *Points* : aucun.
- *Replié* : rien.

**`## Le plan du livre et les conventions de lecture {#sec-educ-lecture}`**

- *Essentiel* : trois chapitres, dans cet ordre : les lois du système éducatif, les aides, la dépense.
- *Contenu* : une phrase par chapitre, avec son lien. Puis les conventions, en liste courte :
  - **dates** : date d'effet quand le texte l'énonce, même antérieure à sa signature ; sinon date à
    laquelle il devient exécutoire. Avant 1993, un jour franc après la publication, donné en fourchette
    quand le fascicule couvre plusieurs jours ; depuis la loi n° 93-64, cinq jours après le dépôt ;
  - **année scolaire et année budgétaire** : l'année scolaire 2012-2013 chevauche deux exercices ;
  - **trois familles de chiffres**, jamais mêlées : budgétaire (y compris l'INS qui relaie le ministère
    des Finances), rapports extérieurs, évaluations ;
  - **PIB** : base dite, segments par base, renvoi à `../annexe-pib.html#sec-pib-ruptures` ;
  - **dinars constants de 2023** à côté des dinars courants ;
  - **textes publiés en arabe seulement** (Constitution de 2022, décret-loi n° 2024-2, lois de finances
    pour 2024 et 2026, quelques décrets de 2018-2019) : cités dans une traduction dite « de travail ».
- *Replié* : rien.

### 1.2 Clés, ancres, recherches

- *Clés* : aucune citation dans l'index (renvois aux chapitres seulement). Si la phrase d'ordre de
  grandeur cite, c'est `ins-annuaire-statistique`.
- *Glossaire* : `#g-obligation-scolaire`, `#g-gratuite-enseignement`, `#g-bourse-scolaire`,
  `#g-bourse-nationale`, `#g-pret-universitaire`, `#g-oeuvres-universitaires`,
  `#g-office-oeuvres-scolaires`, `#g-annee-preparatoire`, `#g-amen-social`.
- *Recherches* : aucune.

---

## 2. Fiche de plan — `_histoire.qmd` (les lois du système éducatif, 1958-2025)

**Objet.** Dire, dans l'ordre des dates, qui l'État scolarise, combien de temps, à quel prix pour la
famille et sous quelle obligation, de la loi de 1958 à la Constitution de 2022, puis donner la même
histoire, plus courte, pour le supérieur, la formation professionnelle et le Conseil supérieur.

**Titre proposé.** `# De la loi de 1958 au Conseil supérieur de l'éducation et de l'enseignement {#sec-educ-histoire .domicile-unique}`

### 2.1 La frontière

**Les règles de base**, ce sans quoi le système n'existe pas, sont celles de l'**enseignement
scolaire** : l'accès, l'obligation et son amende, la gratuité, la durée des cycles, les examens qui les
ferment et la langue d'enseignement. C'est ce que suivent les grandes réformes.

**Les dispositions secondaires** aménagent le système pour un public ou une institution. Chacune a sa
section : le supérieur (public : les bacheliers), la formation professionnelle initiale (public : ceux
qui quittent l'école), le Conseil supérieur et le fonds de la réforme (institution et financement).

Le privé et l'année préparatoire ne sont pas des sections : leurs règles tiennent en quelques articles
des mêmes lois, et se disent dans les réformes et dans l'état du droit.

### 2.2 Les grandes réformes

Trois réformes découpent l'histoire, après la mise en place. Toutes reposent sur un article lu (note H).

| Réforme | Texte et articles | Ce que la loi cherche, dans ses mots | Avant → après | Ce qui y naît |
|---|---|---|---|---|
| **1958 — mise en place** | loi n° 58-118, art. 1er à 4, 8, 11, 15, 38, 60 ; effet au 1er octobre 1958 (art. 60) | « permettre à tous les enfants des deux sexes, sans distinction d'ordre racial, religieux ou social, le développement de leur personnalité » ; « former les cadres nécessaires » (art. 1er, titre I « Principes généraux ») | régimes de 1888 et de 1920 (visas) → système unifié : accès dès six ans, gratuité « à tous les degrés », primaire 6 ans, moyen 3 ans, secondaire 6 ans ; obligation de 6 à 12 ans **annoncée, non imposée** (art. 2, al. 2) | Conseil supérieur de l'éducation nationale (art. 38) ; enseignement supérieur (ch. III) ; règles du privé (titre IV) ; dépenses obligatoires des collectivités (art. 30) |
| **1991 — rupture : l'école de base et l'obligation** | loi n° 91-65, art. 1er, 4, 7 à 11, 24, 32, 34 à 36 | finalités « dans le cadre de l'identité nationale tunisienne et de l'appartenance à la civilisation arabo-musulmane » (art. 1er, ch. I « Principes de base ») | obligation annoncée → **imposée de 6 à 16 ans** (art. 7), avec amende du tuteur (art. 32) ; primaire et moyen → école de base de 9 ans (6 + 3) ; secondaire 6 ans → 4 ans (2 + 2) ; matières enseignées en arabe dans la base (art. 9) ; gratuité garantie, mais droits d'inscription possibles pour qui peut payer (art. 4 et 24) | droits d'inscription (art. 24), qui naissent ici et sont détaillés dans `_aides.html#sec-educ-frais-familles`. L'aide aux élèves modestes et méritants (art. 4, al. 2) reprend la promesse de 1958 (art. 3) : ce n'est pas une naissance |
| **2002 — loi d'orientation** (rupture ou étape : deux lectures) | loi n° 2002-80, art. 1er, 2, 4, 9, 16 à 18, 20 à 22, 24, 26, 36, 61, 69, 70 | « L'éducation est une priorité nationale absolue » ; « L'élève est au centre de l'action éducative » (art. 1er et 2, ch. I « De la mission de l'éducation et des fonctions de l'école ») | obligation de 6 à 16 ans **confirmée** ; préscolaire de 3 à 6 ans, dont une **année préparatoire** rattachée à la base, mais hors gratuité et hors obligation (art. 16 à 18) ; secondaire 4 ans en 1 + 3 (effet à la rentrée 2003-2004, art. 69) ; deux langues étrangères (art. 9) ; amende relevée de 20 à 200 D, 400 D en récidive (art. 21) | l'année préparatoire, que l'État « veille à généraliser » (art. 17) |
| **2017 — rupture : l'obligation étendue à la formation** (rupture ou étape : deux lectures) | loi n° 2017-13, art. 1er à 4 | « consécration de l'obligation d'accès à la formation professionnelle initiale » (intitulé) | obligation scolaire jusqu'à 16 ans → **formation obligatoire et gratuite jusqu'à 18 ans** pour qui n'est ni scolarisé ni inséré (art. 1er et 2) ; amende du tuteur au barème de 2002 (art. 3) | rien de neuf hors de la formation : détail dans `@sec-educ-formation-professionnelle` |

**Les deux lectures à trancher.**

- **2002.** *Rupture* : un public nouveau (les enfants de 5 à 6 ans, par l'année préparatoire), et un
  objectif nouveau, dit dans les mots de la loi (« priorité nationale absolue », « l'élève au
  centre »). *Étape de 1991* : l'obligation, la gratuité et la base de neuf ans existent déjà, et
  l'année préparatoire n'est ni obligatoire ni gratuite (art. 18). Le plan retient **rupture**, et le
  dit comme un classement.
- **2017.** *Rupture* : un public nouveau (les jeunes de 16 à 18 ans hors école et hors emploi) et une
  obligation nouvelle. *Étape de 1991* (l'obligation prolongée) ou *étape de la formation
  professionnelle*. Le plan retient **rupture**, et la loge en réforme du chapitre parce qu'elle
  touche l'obligation, qui est une règle de base.

**Refusés comme grandes réformes, et pourquoi.**

- **1989.** La loi n° 89-70 ne touche pas l'enseignement scolaire. Elle va dans la section du supérieur.
- **2008.** La loi n° 2008-9 est un ajustement de 2002 ; les lois n° 2008-10 et 2008-19 vont dans
  leurs sections.
- **2022.** La Constitution élève au rang constitutionnel l'obligation jusqu'à 16 ans et la gratuité ;
  c'est une **étape** de 1991, dite dans l'état du droit.
- **1968, 1978, 1993.** Ce sont les « réformes » d'une source secondaire (H § 4.3) : aucun texte n'est
  lu, aucune ne paraît.

### 2.3 Les sections, dans l'ordre

**`## Vue d'ensemble {#sec-educ-histoire-vue}`**

- *Essentiel* : en 1958, l'État ouvre l'école gratuite à tous dès six ans. En 1991, il l'impose
  jusqu'à seize ans. En 2002, il fait de l'éducation une « priorité nationale absolue » et y rattache
  l'année préparatoire. En 2017, il étend l'obligation à la formation jusqu'à dix-huit ans.
- *Vue d'ensemble* :
  - le tableau court des quatre réformes (§ 2.2, colonnes « Réforme », « Ce que la loi cherche »,
    « Avant → après »), `tbl-educ-reformes`. **Non replié.** Chaque cellule « Réforme » est un lien
    vers sa ligne de registre ;
  - la **frise** `fig-educ-frise` (§ 2.5, F1).
- *Points* :
  - l'obligation, annoncée en 1958, n'est imposée qu'en 1991 ;
  - la gratuité est de principe depuis 1958, mais des droits d'inscription existent depuis 1991 ;
  - le secondaire passe de six ans à quatre ans ;
  - trois ordres ont leur propre histoire : le supérieur, la formation et le Conseil supérieur.
- *Replié* : rien. La frise et le tableau font la vue d'ensemble.

**`## La mise en place : la loi de 1958 {#sec-educ-1958}`**

- *Essentiel* : la loi de 1958 ouvre l'école à tous les enfants dès six ans, la rend gratuite à tous les
  degrés, et renvoie l'obligation à un texte ultérieur.
- *Vue d'ensemble* : tableau court des ordres d'enseignement en 1958 : primaire 6 ans, précédé d'un
  court cycle d'éducation enfantine (art. 8) ; moyen 3 ans en trois sections (art. 11) ; secondaire
  6 ans en deux cycles de trois ans (art. 15) ; supérieur (ch. III).
- *Points* :
  - ce que la loi cherche (art. 1er, cité) ;
  - la gratuité « à tous les degrés » (art. 3), et « toute l'aide possible » promise aux élèves et
    étudiants doués de familles sans ressources (même article). C'est le fondement légal des bourses,
    que le décret de 1971 vise (« notamment son article 3 ») ;
  - **l'obligation annoncée**. Constat neutre : « Le texte qui devait fixer la date de cette obligation
    n'est pas identifié ici. » Puis l'ancre `r-loi58-118-art2-obligation` ;
  - les institutions : le Conseil supérieur de l'éducation nationale (art. 38), qui ouvre la filiation de
    `@sec-educ-conseil` ; les dépenses obligatoires des collectivités (art. 30) ; le privé soumis à
    autorisation (titre IV).
- *À dire tel quel* : la loi ne fixe pas de langue d'enseignement générale (H § 1.1) ; aucun article ne
  nomme l'enseignement zitounien. Ce sont deux constats sur le texte. Le rédacteur n'en tire aucun
  récit.
- *Date* : effet au 1er octobre 1958, antérieur à la signature (4 novembre) et à la publication
  (7 novembre).
- *Replié* : rien. Le registre de la loi est dans les blocs de `@sec-educ-reformes`.

**`## Les grandes réformes, 1991-2017 {#sec-educ-reformes}`**

Introduction de deux phrases : les trois réformes, et le renvoi aux trois registres en fin de section.

- **`### 1991 : l'école de base et l'obligation de six à seize ans {#sec-educ-1991}`**
  - *Essentiel* : l'État impose l'école de six à seize ans, la regroupe en une école de base de neuf
    ans, et enseigne en arabe les matières de cette école.
  - *Vue d'ensemble* : la ligne 1991 du tableau des réformes suffit. Pas de second tableau.
  - *Points* : obligation et amende (art. 7 et 32 ; exemption du tuteur éloigné, distances fixées par
    le décret n° 92-1186 : 2 km pour l'école primaire, 3 km pour l'école préparatoire sans internat,
    20 km pour une école à internat, note S § 4.3) ; neuf ans (6 + 3) et examen national de fin de
    base (art. 8, 10, 21) ; arabe dans la base (art. 9) ; gratuité et droits d'inscription (art. 4 et
    24 ; renvoi en tête à `_aides.html#sec-educ-frais-familles`).
  - *Dates* : exécutoire le 8 août 1991 ; mais la base s'applique « année par année, à compter de
    l'année scolaire 1989-1990 » (art. 34), donc avant la loi ; la loi de 1958 cesse progressivement de
    s'appliquer (art. 36).
  - *Entre-temps 1991-2002* : une phrase. En janvier 2002, l'examen de fin de base devient facultatif
    (loi n° 2002-5, ajustement). Renvoi au registre des cycles et des examens.
- **`### 2002 : la loi d'orientation et l'année préparatoire {#sec-educ-2002}`**
  - *Essentiel* : la loi fait de l'éducation une « priorité nationale absolue », confirme l'obligation
    et rattache à la base une année préparatoire qui n'est ni obligatoire ni gratuite.
  - *Points* : objectifs (art. 1er à 3) ; préscolaire et année préparatoire (art. 16 à 18 : la phrase de
    l'art. 18 est citée en entier) ; secondaire en 1 + 3 à la rentrée 2003-2004 (art. 26, 69) ; deux
    langues étrangères (art. 9, 51) et amende relevée (art. 21).
  - *Entre-temps 2002-2017* : la loi n° 2008-9 (ajustement : langues étrangères permises dans tous les
    cycles ; collèges pilotes et leur concours, art. 60 bis ; diplôme de fin de base « général » ou
    « technique »). Le décret gouvernemental n° 2019-656 et les arrêtés du 29 juillet 2019 sur les
    collèges et lycées pilotes vont au registre seulement (intitulé seul).
- **`### 2017 : l'obligation étendue à la formation jusqu'à dix-huit ans {#sec-educ-2017}`**
  - *Essentiel* : l'État oblige à se former, jusqu'à dix-huit ans, le jeune qui n'est plus scolarisé et
    n'a pas d'emploi, et lui garantit une formation gratuite.
  - *Points* : deux ou trois phrases (public, gratuité, amende), puis le renvoi à
    `@sec-educ-formation-professionnelle`, qui porte l'arrêté d'application et l'ancre de recherche.
  - *Entre-temps après 2017* : la Constitution de 2022 (art. 44), étape, renvoyée à
    `@sec-educ-etat-droit`.
- **Blocs repliés, en fin de section** (les registres des règles de base, entiers, avec la colonne
  « Portée ») :
  1. `titre="Obligation scolaire et amende du tuteur : textes, date par date, 1958-2022"`. Lignes :
     loi n° 58-118, art. 2 (annonce, mise en place) ; loi n° 91-65, art. 7 et 32 (rupture) ; décret
     n° 92-1186 (étape de 1991 : distances) ; loi n° 2002-80, art. 1er, 20, 21 (étape : barème
     relevé) ; loi n° 2017-13, art. 1er et 3 (rupture) ; Constitution, art. 44 (étape).
  2. `titre="Gratuité de l'enseignement : textes de principe, 1958-2022"`. Lignes : loi n° 58-118,
     art. 3 ; loi n° 91-65, art. 4 et 24 (rupture : droits d'inscription pour qui peut payer) ; loi
     n° 2002-80, art. 4, 18, 36 ; loi n° 2008-19, art. 7 ; loi n° 2017-13, art. 2 ; Constitution,
     art. 44. Une ligne de renvoi vers le registre des montants (`_aides.html#sec-educ-frais-familles`).
  3. `titre="Cycles, examens et langues d'enseignement : textes, date par date, 1958-2019"`. Lignes :
     loi n° 58-118 (art. 4, 8, 11, 13, 15, 18, 23) ; loi n° 91-65 (art. 8 à 11, 14, 21, 34, 35) ; loi
     n° 2002-5 (ajustement) ; loi n° 2002-80 (art. 9, 22, 24, 26, 29, 30, 51, 61, 62, 69) ; loi
     n° 2008-9 (ajustement) ; décret n° 2004-2437 et décret n° 2012-827 (vie scolaire, intitulé seul) ;
     décret gouv. n° 2019-656, arrêtés du 29 juillet 2019, décret gouv. n° 2019-1085 (intitulé seul).
  Le bloc 3 porte aussi les deux décrets d'application de 1960-1961 (décret n° 60-220, établissements
  secondaires ; décret n° 61-14, enseignement primaire), en intitulé seul.

**`## L'état du droit en octobre 2026 {#sec-educ-etat-droit}`**

Non replié. Une sous-partie en liste ; aucun niveau 3.

- *Essentiel* : en octobre 2026, l'enseignement est obligatoire jusqu'à seize ans et gratuit dans le
  public « à toutes ses étapes ». La Constitution élève ainsi au rang constitutionnel l'obligation
  (lois de 1991 et de 2002) et la gratuité (loi de 2002 pour l'école, loi n° 2008-19, art. 7, pour le
  supérieur).
- *Points* :
  - **obligation** : Constitution, art. 44 (traduction de travail) ; loi n° 2002-80, art. 1er et 20 ;
  - **gratuité et droits** : principe, puis une phrase et un renvoi : des droits d'inscription,
    d'assurance et de bibliothèque sont dus, sauf exonération sous le SMIG
    (`_aides.html#sec-educ-frais-familles`) ;
  - **année préparatoire** : rattachée à la base, hors gratuité et hors obligation. Constat : « Aucun
    texte qui en organise la généralisation n'est identifié ici. » Puis l'ancre
    `r-loi2002-80-art17-annee-preparatoire` ;
  - **cycles** : primaire 6 ans, cycle préparatoire 3 ans, secondaire 4 ans (loi de 2002 modifiée en
    2008) ;
  - **langues** : arabe dans la base, langues étrangères permises dans tous les cycles (2008) ;
  - **privé** : autorisation (art. 38) et programmes officiels (art. 40) de la loi de 2002, que la loi de
    2008 ne touche pas. Le décret n° 92-1187 et les arrêtés de 1992-1993 vont au registre en intitulé
    seul.
- *Date* : « en octobre 2026 », par la date seulement. La réserve « aucun texte postérieur
  identifié » s'écrit une seule fois, ici.
- *Replié* : rien.

**`## L'enseignement supérieur {#sec-educ-superieur}`**

Renvoi en tête : les bourses, les prêts et les œuvres universitaires sont dans
`_aides.html#sec-educ-aides-etudiants`.

- *Essentiel* : le supérieur, prévu par la loi de 1958, a sa loi propre en 1989, puis passe au
  système licence-mastère-doctorat, que la loi de 2008 consacre ; il est gratuit dans le public, avec
  des droits d'inscription fixés par décret.
- *Situation* : « né de la loi de 1958 (ch. III) ».
- *Vue d'ensemble* : tableau court des ruptures de la section, non replié :

  | Rupture | Ce que la loi cherche | Avant → après |
  |---|---|---|
  | 1989, loi n° 89-70 (étape ou rupture : deux lectures) | « contribuer au développement de la nation » ; « favoriser l'arabisation » (art. 1er rectifié) | ch. III de 1958 et lois de 1969, 1976, 1986 → loi unique ; universités établissements publics administratifs ; aide de l'État en bourse, prêt, nature ou exemption de droits (art. 30) ; frais d'inscription « qui seraient exigés des étudiants disposant de ressources » (art. 28) |
  | 2008, loi n° 2008-19 et décret n° 2008-3123 (**rupture**) | « édifier la société du savoir » ; « renforcer l'employabilité des diplômés » (art. 1er, 2) | cycles de 1989 → licence 3 ans, mastère 2, doctorat 3 (art. 3) ; « L'enseignement supérieur public est gratuit », avec droits par décret (art. 7) |

  *Les deux lectures de 1989.* *Étape*, selon la note H : la loi organise un ordre qui existe déjà.
  *Rupture* : un financeur nouveau, puisque l'étudiant « disposant de ressources » peut payer
  (art. 28). Le plan retient **étape** et pose la question.
- *Points* :
  - le LMD est **dans le texte même** du décret n° 2008-3123 (intitulé, art. 2 et 3) ; il s'applique
    à partir de 2006-2007 (art. 43, effet antérieur à la signature) ;
  - l'ancien régime s'éteint à la fin de 2011-2012 (loi n° 2008-19, art. 56, al. 2 ; décret,
    art. 41). Constat : « Le décret qui devait fixer les délais du passage n'est pas identifié ici. »
    Puis l'ancre `r-loi2008-19-art56-delais-lmd` ;
  - en 2011, présidents, doyens et directeurs deviennent élus (décret-loi n° 2011-31, ajustement) ;
    en 2017, le bachelor en administration des affaires est ajouté aux études à régime propre, avec effet
    en 2010-2011 (loi n° 2017-38, ajustement).
- *Replié* : `titre="Enseignement supérieur : textes, date par date, 1958-2017"`. Lignes :
  - loi n° 58-118, ch. III, mise en place ;
  - décret n° 60-98, université de Tunis, intitulé seul (publié au JORT n° 16 du 31 mars 1960 ; date de
    signature non établie) ;
  - loi n° 69-3, loi n° 76-65, loi n° 86-80, intitulé seul, abrogées en 1989 ;
  - décret n° 89-1295, intitulé seul ; loi n° 89-70 et son rectificatif ;
  - lois n° 92-50 et 92-51 (instituts supérieurs des études technologiques), intitulé seul ;
  - décret n° 93-2333, décret n° 95-1419 (contribution financière des étudiants à la vie
    universitaire), décret n° 2004-2721 (licence appliquée) : connus par les visas de 2008 ;
  - loi n° 97-21 et loi n° 2000-67, intitulé seul ;
  - loi n° 2000-73 (supérieur privé), modifiée par les lois n° 2006-50 et 2008-59, intitulé seul ;
  - loi n° 2008-19 ; décret n° 2008-3123 ; loi n° 2009-21 (formation pratique), intitulé seul ;
  - décret-loi n° 2011-31 ; décret n° 2012-1227 (mastère) et décret n° 2013-47 (doctorat), intitulé
    seul ;
  - décret gouv. n° 2016-1100, intitulé seul ; loi n° 2017-38.

**`## La formation professionnelle initiale {#sec-educ-formation-professionnelle}`**

Renvoi en tête : la taxe de formation professionnelle et l'agence de 1993 vivent dans d'autres livres
(liens de `@sec-educ-voisinage`).

- *Essentiel* : depuis 2008, la formation initiale a trois cycles, du certificat d'aptitude
  professionnelle au brevet de technicien supérieur, avec des passerelles vers le lycée. Depuis 2017,
  elle est obligatoire et gratuite jusqu'à dix-huit ans pour le jeune ni scolarisé ni en emploi.
- *Situation* : la loi de 2008 remplace la loi d'orientation n° 93-10 du 17 février 1993 (art. 65),
  qui n'est connue ici que par son intitulé. **Elle ne porte donc pas de rupture.** Le premier texte
  lu est celui de 2008.
- *Vue d'ensemble* : tableau court des trois cycles de 2008 (art. 9 et 13), avec, pour chacun,
  l'entrée et le diplôme, plus le certificat de compétence et le cycle préparatoire.
- *Ruptures de la section* :
  - **2008, loi n° 2008-10** : rupture provisoire, ou étape de 1993. La question va au documentaliste
    (lire la loi n° 93-10). Ce que la loi cherche : « l'un des leviers du développement » (art. 1er).
    Ce qui naît : le baccalauréat professionnel ; des passerelles dans les deux sens (art. 11, 12) ;
    l'apprentissage de 15 à 20 ans sous contrat ; une indemnité à la charge de l'entreprise, non
    soumise aux cotisations (art. 15, 18, 19).
  - **2017, loi n° 2017-13** : rupture (§ 2.2). Constat : « L'arrêté conjoint qui doit en fixer les
    modalités n'est pas identifié ici. » Puis l'ancre `r-loi2017-13-art4-arrete`.
- *Point de passage avec l'école* : la loi n° 2008-9 ouvre l'alternance aux élèves (art. 23 et 27
  nouveaux). Une phrase, renvoyée au registre.
- *Replié* : `titre="Formation professionnelle initiale : textes, date par date, 1993-2022"`. Lignes :
  - loi n° 93-10, intitulé seul ;
  - loi n° 93-11 (agences de l'emploi et de la formation professionnelle), intitulé seul ;
  - loi n° 93-12, connue par l'intitulé de la loi n° 2003-77 ; loi n° 2003-77, intitulé seul ;
  - loi n° 2008-9, art. 23 et 27 ; loi n° 2008-10 ;
  - loi n° 2017-13 ;
  - arrêté du 23 novembre 2020 sur la formation à distance, intitulé seul, hors application de la loi de
    2017 ;
  - décret-loi n° 2022-78, intitulé seul.

  La loi n° 2014-59 (avance sur la taxe) relève du livre des cotisations : **hors sujet** ici.

**`## Le Conseil supérieur et le fonds de la réforme éducative {#sec-educ-conseil}`**

- *Essentiel* : un conseil consultatif existe depuis 1958 ; la Constitution de 2022 en fait une
  instance constitutionnelle, organisée en 2024. Depuis 2024, un fonds national de la réforme
  éducative, dont le président du Conseil est l'ordonnateur, finance la réforme sur des ressources
  propres.
- *Vue d'ensemble* : tableau court de la filiation (note H § 1.10), non replié. **Il ne porte que les
  lignes lues** : 1958, art. 38 ; 1991, art. 2 ; 2000 ; 2022, art. 135 ; 2024 ; 2025. Les décrets
  n° 62-403 et 89-1295 sont connus par leur intitulé : ils vont au bloc replié.
- *Ruptures de la section* :
  - **2022-2024, rupture** : un organe consultatif → une « instance constitutionnelle dotée de la
    personnalité juridique et de l'autonomie financière » (décret-loi n° 2024-2, art. 2), avec avis
    obligatoire (art. 12) et rapport annuel publié (art. 14). Le décret n° 2025-246 en est l'étape.
  - **2024, loi de finances pour 2024, art. 15, rupture** (un financeur nouveau). Ressources : dons ;
    0,5 % des bénéfices des établissements éducatifs privés ; 0,25 % de ceux des sociétés pétrolières,
    des assurances, des banques, des grandes surfaces et des pharmacies. Emplois : diagnostic,
    programmes, espaces. Le ministre de l'Éducation est ordonnateur à titre provisoire.
- *Points* : les noms des trois organes, à ne pas confondre (1958, 2000, 2022) ; la présidence
  tournante entre sept ministres (art. 3).
- *Après 2011* : constat : « Aucun texte du *Journal officiel* organisant une consultation nationale
  sur la réforme du système éducatif n'est identifié ici. » Puis l'ancre
  `r-education-consultation-reforme`.
- *Citation* : Constitution, art. 135 et 142 ; décret-loi n° 2024-2 ; loi de finances pour 2024 — en
  arabe, avec traduction de travail. Pour l'entrée en vigueur de la Constitution, **la clause de
  l'art. 142** est citée, sans calcul de date.
- *Replié* : `titre="Conseil supérieur de l'éducation : textes, date par date, 1958-2025"`. Lignes :
  - loi n° 58-118, art. 38 ;
  - décret n° 62-403, intitulé seul (rectificatif dit « 1962/015 » à l'index, sans doute 1963) ;
  - décret n° 89-1295, intitulé seul ;
  - loi n° 91-65, art. 2 ; décret n° 2000-2260 ;
  - projets de Constitution publiés par les décrets présidentiels n° 2022-578 et 2022-607 (rédaction
    inchangée) ; Constitution, art. 135, 141, 142 ; décret présidentiel n° 2022-691 ;
  - décret-loi n° 2024-2 ; décret n° 2025-246 ; loi de finances pour 2024, art. 15 ;
  - décret-loi n° 2011-46 (centre national des technologies en éducation), intitulé seul ;
  - décret gouv. n° 2021-57 (« École de la deuxième chance »), intitulé seul.

**`## Les élèves et les étudiants, 1995-2024 {#sec-educ-eleves}`**

- *Essentiel* : le nombre d'élèves du premier cycle de la base baisse jusqu'en 2008-2009, puis
  remonte. Celui du second cycle et du secondaire croît jusqu'en 2006-2007. Le supérieur triple de
  1995-1996 à 2008-2009, puis recule jusqu'en 2020-2021.
- *Vue d'ensemble* : la figure `fig-educ-eleves` (§ 2.5, F2).
- *Points* : la part du privé au premier cycle (de 8 897 en 1995-1996 à 128 513 en 2023-2024, à lire
  sur la figure) ; les réformes marquées sur la figure ; les ruptures de définition.
- *Replié* : `titre="Élèves et étudiants par cycle et par secteur : effectifs annuels, 1995-1996 à 2023-2024"`,
  le tableau des CSV, avec édition et page de l'annuaire.
- *Famille* : statistique relayée par l'INS (qui cite les ministères). La série de l'UNESCO-UIS
  (1971-2023) **n'est pas superposée** dans cette version : la note H dit sa méthode non relue
  (H § 3.2).

**Section d'attente, non rendue** : `sec-educ-histoire-economie`.

### 2.4 Clés à citer, par section

| Section | Clés |
|---|---|
| `sec-educ-histoire-vue` | aucune dans le fil : les liens vont aux registres |
| `sec-educ-1958` | `loi58-118` |
| `sec-educ-reformes` et ses blocs | `loi58-118`, `loi91-65`, `loi2002-5`, `loi2002-80`, `loi2008-9`, `loi2017-13`, `constitution2022` (à promouvoir). Le décret n° 92-1186 **n'a pas de clé** : à créer par le bibliographe (JORT n° 41 de 1992, p. 816 ; lu à l'image, note S § 4.3) |
| `sec-educ-etat-droit` | `constitution2022`, `loi2002-80`, `loi2008-9` |
| `sec-educ-superieur` | `loi58-118`, `loi89-70`, `loi89-70-rectificatif`, `loi2008-19`, `decret2008-3123`, `decret-loi2011-31`, `loi2017-38` |
| `sec-educ-formation-professionnelle` | `loi2008-9`, `loi2008-10`, `loi2017-13` |
| `sec-educ-conseil` | `loi58-118`, `loi91-65`, `decret2000-2260`, `constitution2022`, `decret-pres2022-691`, `decret-loi2024-2`, `decret2025-246`, `lf-2024` |
| `sec-educ-eleves` | `ins-annuaire-statistique` (édition et page par année dans le bloc) |

### 2.5 Figures et tableaux

| Id | Contenu | Source | Ruptures à marquer | État |
|---|---|---|---|---|
| **F1** `fig-educ-frise` | En bandes : le régime scolaire (1958 ; base progressive dès 1989-1990 ; 1991 ; 2002, avec le secondaire en 1 + 3 dès 2003-2004 ; 2017) ; le supérieur (1958 ; 1989 ; LMD dès 2006-2007 ; ancien régime éteint fin 2011-2012) ; la formation (2008 ; 2017) ; le Conseil (1958, 2000, 2024). En points, les naissances des aides : bourse nationale 1957, bourses scolaires 1966, ONOU 1970, prêt 1986, offices 1988, droits d'inscription 1991 (loi n° 91-65, art. 24 ; montants dès 1992), prêt des caisses 1999, office scolaire 2016, bourse d'intégration 2018 | dates des textes **lus** des notes H, S, U ; données écrites à la main dans le module | les grandes réformes, en bandes | **faisable maintenant** (aucune série) ; modèle `fiscalite/figures/regimes_incitation.py`. Les textes en intitulé seul (1960, 1993) n'y paraissent pas |
| **F2** `fig-educ-eleves` | Élèves du premier cycle de la base et du second cycle et secondaire, public et privé empilés ; étudiants (total). 1995-1996 à 2023-2024 | `eleves-public-premier-cycle-base.csv`, `eleves-prive-premier-cycle-base.csv`, `eleves-public-second-cycle-base-secondaire.csv`, `eleves-prive-second-cycle-base-secondaire.csv`, `etudiants-total.csv` | marques : 2003-2004 (secondaire en 1 + 3) ; 2006-2007 (licence LMD ; **rupture de définition** du supérieur, « étudiants réguliers ») ; 2011-2012 (fin de l'ancien régime). Écoles de qualification technique exclues (dit en note) | **après versement** des CSV au catalogue |

Pas de PIB dans ce chapitre.

### 2.6 Glossaire

`#g-enseignement-de-base`, `#g-cycle-primaire`, `#g-cycle-preparatoire`, `#g-annee-preparatoire`,
`#g-education-prescolaire`, `#g-ecole-preparatoire`, `#g-college-pilote`, `#g-lycee-pilote`,
`#g-enseignement-secondaire`, `#g-enseignement-moyen`, `#g-diplome-fin-enseignement-base`,
`#g-obligation-scolaire`, `#g-gratuite-enseignement`, `#g-tuteur`,
`#g-conseil-superieur-education-enseignement`, `#g-conseil-superieur-education`,
`#g-fonds-national-reforme-educative`, `#g-lmd`, `#g-certificat-aptitude-professionnelle`,
`#g-brevet-technicien-professionnel`, `#g-baccalaureat-professionnel`,
`#g-brevet-technicien-superieur`, `#g-certificat-de-competence`,
`#g-formation-professionnelle-initiale`, `#g-formation-en-alternance`, `#g-apprentissage`,
`#g-droits-inscription`.

### 2.7 Recherches à ancrer

`r-loi58-118-art2-obligation` (`sec-educ-1958`) ; `r-loi2002-80-art17-annee-preparatoire`
(`sec-educ-etat-droit`) ; `r-loi2008-19-art56-delais-lmd` (`sec-educ-superieur`) ;
`r-loi2017-13-art4-arrete` (`sec-educ-formation-professionnelle`) ; `r-education-consultation-reforme`
(`sec-educ-conseil`).

---

## 3. Fiche de plan — `_aides.qmd` (aides aux élèves et aux étudiants)

**Objet.** Les transferts que l'État réserve aux élèves et aux étudiants : en espèces (bourses, prêts)
et en nature (cantines, foyers, restaurants et cités universitaires). Le chapitre traite aussi, par
leur envers, les droits que paient les familles et l'exonération qui les en dispense. Pour chaque
transfert : le public, le montant à chaque date, et ce qui est connu des bénéficiaires et des crédits.

**Titre proposé.** `# Les aides aux élèves et aux étudiants {#sec-educ-aides .domicile-unique}`

### 3.1 La frontière, et la découpe en deux publics

Le chapitre couvre deux politiques distinctes : l'une pour l'élève, l'autre pour l'étudiant. Leurs
textes, leurs gestionnaires et leurs financeurs ne se recoupent pas. **On les sépare d'abord**, en deux
sections de niveau 2. Chacune s'ouvre sur son tableau court de ruptures, puis donne une fiche par
dispositif.

- **Élèves.** La bourse scolaire est la plus ancienne aide (1966), mais la plus légère dans le budget.
  Les cantines et les foyers en sont le gros poste. Les droits d'inscription sont l'envers de la
  gratuité.
- **Étudiants.** Les règles de base sont celles de la **bourse nationale**, qui existe depuis 1957 et
  pèse le plus dans le budget. Le prêt, né en 1986 comme alternative à la bourse, est réglé par les
  mêmes textes : il reste dans la même section. Le prêt des caisses (autre financeur) et les œuvres
  universitaires (autre gestionnaire) ont chacun leur section.

### 3.2 Les ruptures

**Élèves** (tableau court `tbl-educ-aides-eleves-ruptures`, non replié) :

| Rupture | Texte, article | Ce que la loi cherche | Avant → après |
|---|---|---|---|
| **1966, mise en place** lisible de la bourse scolaire, sur le fondement de la loi de 1958 (art. 3, « toute l'aide possible ») | arrêté du 3 octobre 1966, art. 2 à 6 | couvrir « en partie ou en totalité les frais de demi-pension ou de pension » d'élèves « appartenant à une famille nécessiteuse » | remises de principe de 1960 (intitulé seul) → bourse, au public seul |
| **1991, rupture : les droits d'inscription** (la famille devient financeur) | loi n° 91-65, art. 24 | des droits peuvent être « mis à la charge des élèves dont les revenus des parents les rendent à même de les payer » | gratuité sans droits → droits pour qui peut payer, avec exonération sous le SMIG (décret de 1992, étape) |
| **2016, rupture : un office et un objectif pour les cantines** | décret gouv. n° 2016-664, art. 2, 8, 18, 21 | « renforcer et conserver le réseau des cantines scolaires principalement dans les écoles primaires dont les résultats […] sont inférieurs à la moyenne nationale » pour « éviter l'abandon scolaire » (art. 8) | cantines et foyers gérés par chaque établissement → office des services scolaires, le 31 décembre 2016, qui attribue aussi les bourses |

Lecture à trancher : **2010** (décret n° 2010-1928, des droits d'inscription au primaire, 2 D). Ce peut
être une *étape* de 1991, ou une *rupture* : un public nouveau paie, et la loi de 2002 (art. 36) ne
vise que collèges et lycées. Le plan retient **étape**, et pose la question du fondement au
documentaliste.

**Étudiants** (tableau court `tbl-educ-aides-etudiants-ruptures`, non replié) :

| Rupture | Texte, article | Ce que la loi cherche | Avant → après |
|---|---|---|---|
| **1957, mise en place** | décret n° 57-78, art. 1er, 4, 9 ; arrêté du 12 octobre 1957, art. 3 | bourses « compte tenu des besoins impérieux du Pays » ; engagement « à servir au terme de ses études l'État Tunisien » | néant → bourse nationale sur concours, contre engagement de servir |
| **1970, mise en place des œuvres universitaires** | loi n° 70-9, art. 1er, 2 | « assurer aux étudiants […] de bonnes conditions de vie et d'études » | Centre d'hébergement et restaurants (1970) → un office national qui gère bourses, cités et restaurants |
| **1986, rupture : le prêt, sans engagement de servir** | décret n° 86-688, art. 1er, 4, 8 ; arrêté du 28 juillet 1986, art. 3, 9, 25 | une aide servie « soit sous forme de bourse nationale […] soit sous forme de prêt universitaire » | bourse sur concours et engagement de servir dix ans (1971) → bourse sous plafond de revenu, ou prêt remboursable au non-boursier ; l'engagement de servir disparaît |
| **1999, rupture : un financeur nouveau** | décret n° 99-1544, art. 1er, 3, 5 | les caisses prêtent à leurs affiliés pour les études de leurs enfants | prêt de l'État seul → prêt des caisses, égal à la bourse, à 5 % |
| **2009, rupture : un plafond indexé sur le SMIG, un prêt recentré** | décret n° 2009-3040, art. 3, 4, 7, 10 ; arrêté du 26 octobre 2009, art. 2, 4, 30 | bourses et prêts « dans la limite des crédits alloués annuellement » | plafond fixé chaque année en dinars → revenu brut inférieur au SMIG annuel ; prêt aux non-boursiers de tous cycles → prêt réservé au mastère et au doctorat ; paiement par les offices → paiement sur le budget du ministère |

Étapes et lectures à trancher :

- **1971** (décret n° 71-361, arrêtés du 7 octobre 1971) : étape de 1957. Concours sur titres,
  premier plafond chiffré, engagement porté à dix ans, répartition « dans le cadre des besoins des Plans
  de développement ». Autre lecture : rupture, par la condition de ressources chiffrée.
- **1988** (lois n° 88-135 à 88-137) : étape de 1970 (trois offices régionaux).
- **1992** (arrêté du 20 août 1992) : rupture propre aux œuvres universitaires. L'hébergement est
  réservé aux boursiers, et une bourse est versée au boursier non logé faute de place.
- **2012** (décret n° 2012-2392 ; arrêtés du 9 octobre 2012) : étape de 2009 (revenu net après
  abattements). Autre lecture : rupture, par les publics nouveaux de plein droit (blessés de la
  révolution, enfants des martyrs, étudiants « portant un handicap profond »).
- **2018** (décret gouv. n° 2018-927 ; arrêté du 4 décembre 2018) : naissance d'un dispositif annexe,
  la **bourse d'intégration universitaire**, 500 D en une tranche au nouveau bachelier. Une ligne dans
  la section, une ligne au registre.

### 3.3 Les sections, dans l'ordre

**`## Vue d'ensemble {#sec-educ-aides-vue}`**

- *Essentiel* : l'élève reçoit surtout une aide en nature (cantine, foyer) et, selon ses ressources,
  une bourse de pension ou l'exonération des droits ; l'étudiant reçoit une bourse mensuelle sous
  plafond de revenu, à défaut un prêt, et peut être logé et nourri à prix réduit.
- *Vue d'ensemble* : la **carte des aides** (`tbl-educ-aides-carte`), non repliée, de l'élève du
  primaire à l'étudiant. Colonnes : aide, public, montant en vigueur à sa date, payeur, domicile. Elle
  porte aussi les aides des autres livres (aide de rentrée de l'Amen social, abonnement de transport,
  TVA de la restauration, déduction pour enfant étudiant), avec leur lien.
- *Points* : deux publics, deux histoires ; la condition de ressources en dinars d'abord, puis indexée
  sur le SMIG.
- *Replié* : rien.

**`## Les aides aux élèves {#sec-educ-aides-eleves}`**

Ouverture : le tableau des ruptures « élèves » (§ 3.2), et deux phrases.

- **`### Les bourses scolaires {#sec-educ-bourses-scolaires}`**
  - *Essentiel* : la bourse scolaire paie, en fraction, la pension ou la demi-pension d'un élève du
    public de famille nécessiteuse ; elle n'a jamais eu de montant en dinars dans les textes lus.
  - *Vue d'ensemble* : tableau court des barèmes de revenu de 1971, 1972 et 1974 : tranches de revenu
    familial et points ; fractions accordées. Trois lignes, une par texte, avec le seuil au-delà duquel
    le revenu ne rapporte plus de points : 500 D en 1971 et 1972, 600 D en 1974.
  - *Points* :
    - l'objet de la bourse (frais de pension, jamais fournitures ni trousseau) ;
    - la décision « en fonction des crédits » (1971, 1974) ;
    - le quart de bourse disparaît en 1972 ;
    - les critères passent du décret à l'arrêté (1974) ;
    - le fondement légal est la loi de 1958 (art. 3), que vise le décret de 1971. La loi de 1991
      (art. 4, al. 2) reprend la même double condition, de ressources et de mérite (étape) ;
    - l'office l'attribue depuis 2016, « selon les critères qui seront fixés par décision du
      ministre ». Les crédits des bourses sont transférés à l'office en 2017 ; le dispositif existe
      donc encore en 2016-2017.
  - *Lacunes* : « Aucun texte publié ne fixe, après l'arrêté du 12 août 1974, de nouveaux critères ni
    de montant. » Puis l'ancre `r-bourses-scolaires-apres-1974`. « La décision du ministre prévue en
    2016 n'est pas identifiée ici. » Puis l'ancre `r-bourses-scolaires-decision-ministre`.
  - *Loi de finances pour 1977, art. 15* : c'est une **sanction**, non une mesure de bourse. Le
    contribuable non salarié s'engage à restituer la bourse indûment perçue, majorée de 10 % par an.
    Une phrase, et une ligne au registre (ajustement). Le même engagement revient pour les étudiants en
    1986 (`@sec-educ-bourse-nationale`).
  - *Replié* : deux blocs.
    1. `titre="Bourses scolaires : barèmes de points, revenus et fractions, 1971, 1972 et 1974"`, les
       annexes entières (note S § 1.2 à 1.4). Les parties lues en OCR seulement sont dites telles en
       `TODO (documentaliste)`, et ne sont pas rendues comme valeurs.
    2. `titre="Bourses scolaires : textes, date par date, 1960-2017"`. Lignes :
       - décret n° 60-260 (remises de principe), intitulé seul, abrogé en 1971 ;
       - arrêté du 3 octobre 1966 (mise en place) ; décret n° 71-356 (étape) ;
       - décret n° 72-229 (ajustement : quart de bourse supprimé) ;
       - décret n° 74-783 et arrêté du 12 août 1974, effet au 1er juillet 1974 (étape) ;
       - loi n° 58-118, art. 3 (fondement) ; loi n° 76-115, art. 15 (ajustement) ; loi n° 91-65,
         art. 4, al. 2 (étape de 1958) ;
       - décret gouv. n° 2016-664, art. 2 et 9 (étape de 2016) ;
       - budget 2017 du ministère, p. 30 et 39 (transfert des crédits).
- **`### Les cantines et les foyers scolaires {#sec-educ-restauration-scolaire}`**
  - *Essentiel* : depuis le 31 décembre 2016, un office des services scolaires gère toutes les cantines
    et tous les foyers des établissements publics. Il doit en renforcer le réseau dans les écoles
    primaires aux résultats faibles, pour prévenir l'abandon.
  - *Vue d'ensemble* : tableau court `tbl-educ-cantines-credits`, deux familles **séparées par une
    ligne d'en-tête** :
    - crédits d'intervention du ministère, 2013-2017 : bourses scolaires et de formation ; cantines
      des écoles primaires ; aides scolaires ; total. Ce sont des **prévisions du projet de budget**,
      dont plusieurs reconduites telles quelles ;
    - budget prévisionnel de l'office aux annexes des lois de finances pour 2017, 2019 et 2020 :
      subvention de l'État, ressources propres, total. Pour 2018 : « non établi ».
    Colonne en dinars de 2023 à côté.
  - *Points* :
    - la mission et l'objectif de l'office (art. 2 et 8 cités) ;
    - les ressources, dont des « contributions des élèves » (art. 18). Constat : « Le texte qui fixe ces
      contributions n'est pas identifié ici. » Puis l'ancre `r-oss-contributions-eleves` ;
    - avant 2016 : constat. Puis l'ancre `r-cantines-scolaires-avant-2016` ;
    - la restauration des élèves et des apprenants est exonérée de TVA (n° 30 bis, loi n° 2009-32,
      art. 3) et ouvre des déductions d'impôt (art. 1er et 2). Une phrase et le lien fiscalité.
      Constat : « Le cahier des charges auquel renvoie l'exonération n'est pas identifié ici. » Puis
      l'ancre `r-cahier-charges-restauration-eleves`.
  - *Ce qui n'est pas rendu* : les effectifs du primaire cités aux pages du budget (ce ne sont pas des
    bénéficiaires de cantines) ; le chiffre de 260 000 enfants attribué au PAM (non vérifié) ; les
    internats créés et supprimés par les lois de finances (intitulé seul).
  - *Replié* : `titre="Cantines et foyers scolaires : textes et budgets, date par date, 1957-2022"`.
    Lignes :
    - arrêté du 15 janvier 1957 et loi n° 58-45, art. 38 à 40 (prix de pension), intitulé seul ;
    - lois de finances qui créent ou suppriment des internats (1974, 1987, 1990), intitulé seul ;
    - loi n° 2009-32 ; loi organique n° 2020-9 et décret présidentiel n° 2020-18 (protocole avec
      l'Italie, article unique lu, hors application directe) ;
    - décret gouv. n° 2016-664 (rupture) ;
    - annexes des lois de finances pour 2017 à 2020 ;
    - arrêté conjoint du 10 février 2022, intitulé seul.
- **`### Les droits d'inscription et leur exonération {#sec-educ-frais-familles}`**
  - *Essentiel* : la scolarité publique est gratuite, mais la famille paie, à l'inscription, un droit
    unique d'inscription, d'assurance et de bibliothèque. Il est de 4 D au primaire et de 8,600 D au
    collège et au lycée depuis 2019-2020. Les parents dont les revenus cumulés ne dépassent pas le SMIG
    en sont exonérés au collège et au lycée ; le décret de 2010 ne dit pas, dans ce que la note en
    rapporte, si l'exonération vaut aussi au primaire (question au documentaliste, § 7.1).
  - *Vue d'ensemble* : **le tableau daté des droits**, `tbl-educ-droits-inscription`, non replié parce
    qu'il est court et qu'il porte l'état du droit. Quatre lignes : 1992, 1997, 2010, 2019. Colonnes :
    date d'effet ; primaire ; collège et lycée ; en dinars de 2023. Une ligne de renvoi au registre de
    la gratuité (`_histoire.html#sec-educ-reformes`).
  - *Points* :
    - le fondement (loi n° 91-65, art. 24 ; loi n° 2002-80, art. 36) ;
    - l'exonération sous le SMIG, qui demeure en 2019 (art. 3 de 2010 non modifié) ; sa portée au
      primaire est à établir avant d'être écrite ;
    - le primaire est soumis aux droits depuis 2010 ;
    - le droit d'assurance n'est pas un droit distinct.
  - *Lacunes* : « Le régime de l'assurance scolaire n'est pas identifié ici. » Puis l'ancre
    `r-assurance-scolaire-regime`. « L'arrêté conjoint qui répartit le droit unique n'est pas identifié
    ici. » Puis l'ancre `r-droits-inscription-repartition`.
  - *Replié* : rien de plus que le tableau ; les décrets de l'École internationale de Tunis (1999,
    2018) vont en note sous le tableau, hors du droit commun.

**`## Les aides aux étudiants {#sec-educ-aides-etudiants}`**

Ouverture : le tableau des ruptures « étudiants » (§ 3.2), et deux phrases.

- **`### La bourse nationale et le prêt universitaire {#sec-educ-bourse-nationale}`**
  - *Essentiel* : la bourse nationale est une somme mensuelle servie dix mois à l'étudiant du public
    dont les parents ont un revenu inférieur au SMIG annuel. Elle valait 120 D au premier niveau en
    2017-2018. L'étudiant qui ne l'obtient pas peut, en mastère et en doctorat, emprunter à l'État.
  - *Vue d'ensemble* : deux tableaux courts, non repliés.
    - `tbl-educ-bourse-montant` : le **montant mensuel du premier niveau**, aux sept dates lues (U § 3.1).
      Colonnes : date d'effet, dinars courants, dinars de 2023, texte. Les dinars de 2023 ne valent qu'à
      partir de 1976, faute d'indice avant (le 25 D de 1971 n'a que sa valeur courante). Ligne
      « entre 1974 et 1986 » : « non identifié », avec l'ancre `r-bourse-montants-1982`.
    - `tbl-educ-bourse-plafond` : le **plafond de revenu**, aux dates lues (U § 3.2). Colonnes : date,
      plafond, revenu retenu. Pour 2009 et 2012, le SMIG annuel de l'année est donné en dinars à côté,
      pris dans `marche-travail-smig-smag`. Les années sans plafond identifié portent l'ancre
      `r-bourse-seuils-revenu-1986-2005`.
  - *Points* :
    - la fin de l'engagement de servir (1986) : il ne survit que pour les bourses spécifiques à
      l'étranger (2001 : trois ans) ;
    - le prêt de l'État : montants de 1990, 1997 et 2011 ; remboursement sur dix ans, majoré de 2,5 % par
      an, avec un délai de grâce de deux ans ;
    - **deux régimes coexistent de 2009 à 2012** (plafond en dinars du 5 octobre 2009 ; plafond SMIG du
      26 octobre 2009), sans que les textes disent à qui chacun s'applique ;
    - 2012 : revenu net après abattements, et publics de plein droit ;
    - 2018 : la bourse d'intégration.
  - *Lacune* : « Aucun arrêté de montant postérieur à 2017-2018 n'est identifié ici. » Puis l'ancre
    `r-bourse-montants-apres-2017`. Elle se place une seule fois, là où le montant en vigueur est
    donné.
  - *Les étudiants à l'étranger* : un paragraphe de repères (U § 3.8). Il ne dit pas la liste par pays.
  - *Replié* : quatre blocs.
    1. `titre="Bourse nationale en Tunisie : montants mensuels par niveau, 1971-2017"`, une ligne par
       niveau et par date (U §§ 2.1, 2.3, 2.6, 2.7).
    2. `titre="Prêt universitaire de l'État : montants annuels, remboursement et renouvellement, 1986-2012"`
       (U §§ 3.3, 3.4, 3.7).
    3. `titre="Bourses et prêts à l'étranger : montants et conditions, 1957-2026"` (U § 3.8, et les
       textes de 1990, 1997, 2001, 2009, 2010, 2019, 2026).
    4. `titre="Bourse nationale et prêt universitaire : textes, date par date, 1957-2026"`, le registre
       complet avec sa colonne « Portée » (liste au § 3.5).
- **`### Le prêt des caisses de sécurité sociale {#sec-educ-prets-caisses}`**
  - *Essentiel* : depuis 1999, la CNSS et la CNRPS prêtent à leurs affiliés, pour les études
    supérieures de leurs enfants, une somme égale à la bourse de l'État. Le taux d'intérêt est de 3 %
    depuis 2017.
  - *Vue d'ensemble* : tableau court des deux dates (U § 3.5), non replié.
  - *Points* : conditions de revenu (de 1 à 4,5 SMIG annuels, régime de 48 heures) ; étudiant non
    boursier ; un prêt par étudiant ; remise des intérêts de retard en 2017.
  - *Date* : 2017, « sous réserve des articles non lus » (art. 5 et suivants). Pas de date exécutoire
    affirmée tant que ces articles ne sont pas lus.
  - *Replié* : rien de plus (deux textes).
- **`### La restauration et le logement universitaires {#sec-educ-oeuvres-universitaires}`**
  - *Essentiel* : trois offices des œuvres universitaires (Nord, Centre, Sud) logent et nourrissent les
    étudiants du public. Depuis 2016, l'étudiant paie 200 millimes le repas et 10 D par mois le lit, et
    le boursier qui n'a pas de place reçoit 30 D par mois.
  - *Situation* : née de la loi de 1970.
  - *Vue d'ensemble* : tableau court `tbl-educ-repas-lit` (U § 3.6) : 1992 et 2016, et pour les années
    antérieures « non identifié ». Colonnes en dinars courants et en dinars de 2023.
  - *Points* :
    - le gestionnaire : l'ONOU de 1970, supprimé par la loi de finances pour 1987 (art. 87), puis trois
      offices en 1988. Leur statut : « établissement à caractère administratif » (1988) ; l'office du
      Nord devient « établissement **public** à caractère administratif » en 2006 (`#g-epa`) ;
    - l'accès : hébergement réservé aux boursiers depuis 1992 ; en 2016, distance de 30 km au moins,
      26 ans au plus, une année d'hébergement (deux pour les étudiantes) ;
    - les ressources des offices (décret n° 2014-4200, art. 18), dont les contributions des étudiants
      et les remboursements de prêts.
  - *Lacunes* : « Les prix du repas et du lit avant 2016 ne sont pas identifiés ici. » Puis l'ancre
    `r-oeuvres-prix-repas-lit-avant-2016`. « Le texte qui porte la bourse d'hébergement de 20 à 30 D
    n'est pas identifié ici. » Puis l'ancre `r-bourse-hebergement-30d-avant-2016`.
  - *Ce qui n'est pas rendu* : la capacité de 68 000 places en 2012-2013 (un point unique, sans série) ;
    elle reste en `TODO (documentaliste)`.
  - *Replié* : `titre="Œuvres universitaires : offices, accès, contributions des étudiants et textes, 1970-2026"`.
    Lignes :
    - loi n° 69-64, art. 27 (Centre d'hébergement), intitulé seul ; loi n° 70-9 (mise en place) ;
    - arrêté du 20 juin 1974 (étape) ; décrets n° 80-1001 et 85-173, intitulé seul ;
    - loi n° 86-106, art. 87 (ajustement de gestion) ; lois n° 88-135 à 88-137 (étape) ;
    - décrets n° 90-1122, 95-1953, 95-1954, 95-2281 et leurs modificatifs, intitulé seul ;
    - arrêté du 20 août 1992 (rupture de la section) ; lois n° 96-89 et 96-90 (ajustement) ;
    - loi n° 97-88, art. 55 à 58 (investissement privé dans l'hébergement), intitulé seul ;
    - cahiers des charges des foyers privés (2003, 2008, 2019, 2020, 2026), intitulé seul ;
    - décret n° 2006-2245 (ajustement) ; arrêté du 5 octobre 2009, règlement intérieur (ajustement) ;
    - décret n° 2009-518, intitulé seul ;
    - arrêtés de classement des établissements de 2012 à 2025, intitulé seul ;
    - décret n° 2014-4200 (ajustement) ; arrêtés du 18 janvier 2016 (étape de 1992).

**`## Les aides servies par d'autres dispositifs {#sec-educ-aides-ailleurs}`**

- *Essentiel* : la famille d'un élève ou d'un étudiant peut recevoir d'autres aides au titre de la
  scolarité. Chacune est exposée dans le livre de son instrument.
- *Contenu*, une phrase et un lien chacun :
  - l'aide de rentrée de l'Amen social, depuis 2020 (`#tbl-nc-rentree-scolaire`). Constat : « Aucune
    aide de rentrée publiée antérieure n'est identifiée ici. » Puis l'ancre `r-aide-rentree-avant-2020`.
    La ligne « aides scolaires » du budget du ministère de l'Éducation (2013-2017) se nomme par son
    libellé seulement : rien ne dit qu'elle finance une aide de rentrée ;
  - l'abonnement de transport ;
  - la TVA de la restauration ;
  - la déduction pour enfant étudiant.
- *À ne pas confondre*, une phrase : la « prime de rentrée universitaire » de 2018 (décret
  gouvernemental n° 2018-904) et l'indemnité des « fournitures scolaires » sont des rémunérations
  d'enseignants. Lien vers le livre des rémunérations publiques.
- *Replié* : rien.

**`## Les boursiers et les crédits des aides {#sec-educ-aides-donnees}`**

- *Essentiel* : de 2008-2009 à 2015-2016, entre un tiers et deux cinquièmes des étudiants sont
  boursiers. Dans les prévisions du budget de 2013, les bourses en Tunisie font 97,8 des 138,9 millions
  de dinars de l'article budgétaire qui les porte, au budget du ministère de l'Enseignement supérieur
  (note U § 5.1).
- *Vue d'ensemble* : la figure `fig-educ-boursiers` (F3), puis le tableau court des crédits
  `tbl-educ-credits-bourses`, en prévisions des budgets 2013-2017, colonne par colonne, comme la source
  les intitule. Famille : budgétaire, prévisions.
- *Points* :
  - la ligne 2016-2017 (250 000 étudiants, 84 000 boursiers) est en chiffres ronds et absente du budget
    2016 : elle est marquée comme probable prévision ;
  - la source ne dit pas si les étudiants sont ceux du public seulement ;
  - l'écart sur 2015 entre deux budgets (100 MD contre 110 MD) se signale ;
  - les subventions aux trois offices (2016-2017) figurent au même tableau.
- *Renvoi* : une évaluation compte 98 533 boursiers en 2010 ; sa méthode et son résultat sont
  exposés dans `_depense.html#sec-educ-depense-evaluations`. Ici, un renvoi d'une phrase, sans
  chiffre.
- *Replié* : rien de plus que le tableau.

**Section d'attente, non rendue** : `sec-educ-aides-economie`.

### 3.4 Clés à citer, par section

| Section | Clés |
|---|---|
| `sec-educ-bourses-scolaires` | `loi58-118` (art. 3), `arrete-1966-10-03-bourses-scolaires`, `decret-71-356-bourses-scolaires`, `decret-72-229-bourses-scolaires`, `decret-74-783-bourses-scolaires`, `arrete-1974-08-12-criteres-bourses`, `loi-76-115-lf-1977`, `loi91-65`, `decret-gouv-2016-664-office-services-scolaires`, `budget-men-2017` |
| `sec-educ-restauration-scolaire` | `decret-gouv-2016-664-office-services-scolaires`, `loi-2009-32-restauration-formation` (à promouvoir), `budget-men-2013`, `budget-men-2014`, `budget-men-2015`, `budget-men-2016`, `budget-men-2017`, `lf-2017`, `lf-2018` (ligne « non établi »), `loi2018-56-lf2019`, `lf-2020` |
| `sec-educ-frais-familles` | `loi91-65`, `loi2002-80`, `decret-92-1185-droits-inscription`, `decret-97-1355-droits-inscription`, `decret-2010-1928-droits-inscription`, `decret-gouv-2019-898-droits-inscription` (édition arabe), `decret-2017-668-smig` si le SMIG est chiffré |
| `sec-educ-bourse-nationale` | `decret57-78-bourse-nationale`, `arrete-1957-10-12-bourse-montant`, `decret71-361-bourses`, `arrete-1971-10-07-jury-bourses`, `arrete-1971-10-07-bourses-montants`, `decret86-688-bourses-prets`, `arrete-1986-07-28-bourses-prets`, `loi-76-115-lf-1977`, `arrete-1988-03-31-bourses-montants`, `decret90-219`, `arrete-1990-04-17-prets-montants`, `arrete-1990-08-21-seuil-revenus`, `arrete-1992-03-07-bourses-montants`, `arrete-1992-03-17-prets-montants`, `decret95-464`, `arrete-1995-03-29-bourses`, `arrete-1997-08-18-bourses-montants`, `arrete-1997-08-18-prets-montants`, `arrete-1997-11-04-bourse-tre`, `decret2001-2438`, `arrete-2006-01-06-seuil`, `arrete-2006-06-08-seuil`, `arrete-2007-06-11-seuil`, `arrete-2008-07-07-seuil`, `arrete-2009-10-05-seuil`, `decret2009-3040-bourses-prets`, `arrete-2009-10-26-bourses-prets`, `arrete-2010-11-24-prets-montants`, `decret2012-2392`, `arrete-2012-10-09-bourses-conditions`, `arrete-2012-10-09-bourses-montants`, `arrete-2012-10-09-prets-montants`, `arrete-2015-12-04-bourses-montants`, `decret2018-927` (arabe), `arrete-2018-12-04-bourse-integration`, `arrete-2019-02-18-prets-etranger`, `arrete-2019-03-05-bourses-etranger` (arabe), `decret2019-806` (arabe), `arrete-2026-07-24-bourse-specifique-ue`, `loi89-70` (art. 30, ligne de registre) |
| `sec-educ-prets-caisses` | `decret99-1544-prets-caisses`, `decret2017-369` |
| `sec-educ-oeuvres-universitaires` | `loi70-9-onou`, `arrete-1974-06-20-reglement-centres-universitaires`, `loi86-106-lf1987`, `loi88-135-oou-nord`, `loi88-136-oou-centre`, `loi88-137-oou-sud`, `arrete-1992-08-20-bourse-supplementaire`, `loi96-89`, `loi96-90`, `decret2006-2245`, `arrete-2009-10-05-reglement-oeuvres`, `decret2014-4200-oou`, `arrete-2016-01-18-hebergement`, `arrete-2016-01-18-restauration` |
| `sec-educ-aides-ailleurs` | `budget-men-2013`, `budget-men-2014`, `budget-men-2015`, `budget-men-2016`, `budget-men-2017` (libellé « aides scolaires ») |
| `sec-educ-aides-donnees` | `budget-mesrs-2013-gbo`, `budget-mesrs-2014-gbo`, `budget-mesrs-2015`, `budget-mesrs-2016`, `budget-mesrs-2017` |

### 3.5 Le registre de la bourse nationale et du prêt (bloc 4 de `sec-educ-bourse-nationale`)

| Texte | Portée |
|---|---|
| décret n° 57-78 ; arrêté du 12 octobre 1957 | mise en place |
| arrêté du 10 décembre 1958 ; décret n° 63-2 et arrêtés de 1963 ; arrêtés de 1964, 1965, 1969 | intitulé seul (OCR nécessaire) |
| décret n° 71-361 ; arrêtés du 7 octobre 1971 (jury ; montants) | étape de 1957 (ou rupture : deux lectures) |
| arrêté du 15 novembre 1971 ; décret n° 72-51 ; arrêtés du 3 avril 1974 et du 5 janvier 1978 | intitulé seul |
| arrêté du 20 août 1982 | connu par un visa : « non identifié », ancre `r-bourse-montants-1982` |
| décret n° 86-688 ; arrêté du 28 juillet 1986 | **rupture** |
| loi n° 76-115, art. 15 (rappelée par l'arrêté de 1986) | ajustement |
| loi n° 89-70, art. 30 (aide de l'État en bourse, prêt, nature ou exemption) | étape de 1986 : la loi énumère les formes de l'aide |
| arrêté du 31 mars 1988 (effet au 1er janvier 1988) | ajustement (montant) |
| décret n° 90-219 (prêt ouvert à l'étranger) | étape de 1986 |
| arrêtés du 28 février 1990 (intitulé seul) et du 17 avril 1990 | ajustement (montants du prêt) |
| arrêté du 21 août 1990 (seuils 1990-1991) | ajustement |
| arrêté du 7 avril 1992 (revenus pour le prêt à l'étranger) | intitulé seul |
| arrêtés des 7 et 17 mars 1992 | ajustement |
| décret n° 95-464 ; arrêté du 29 mars 1995 (critère de 12 sur 20 abandonné) | étape de 1986 |
| arrêtés du 18 août 1997 (montants ; allocation supplémentaire d'une mensualité) | ajustement |
| arrêté du 4 novembre 1997 (enfants des familles résidentes à l'étranger) | étape de 1986 (public nouveau, une ligne) |
| décret n° 2001-2438 (bourses spécifiques et d'alternance à l'étranger) | étape de 1986 |
| arrêtés des 6 janvier 2006, 8 juin 2006, 11 juin 2007, 7 juillet 2008, 5 octobre 2009 (plafonds) | ajustement |
| décret n° 2009-3040 ; arrêté du 26 octobre 2009 | **rupture** |
| arrêtés du 16 mars 2010 (bourses dans l'Union européenne et au Canada) | intitulé seul |
| arrêté du 24 novembre 2010 (prêts) | ajustement |
| décret n° 2012-2392 ; arrêtés du 9 octobre 2012 (conditions, montants, prêts) | étape de 2009 (ou rupture : deux lectures) |
| arrêté du 29 janvier 2013 (Canada) | intitulé seul |
| arrêté du 4 décembre 2015 | ajustement (barème en trois étapes) |
| décret gouv. n° 2018-927 ; arrêté du 4 décembre 2018 | naissance de la bourse d'intégration universitaire |
| arrêtés du 18 février et du 5 mars 2019 (étranger) ; arrêtés du 5 mars 2019 modifiant ceux de 2010 (intitulé seul) | ajustement |
| décret gouv. n° 2019-806 (enfants des personnels) | ajustement |
| arrêté du 16 octobre 2019 (frais d'études des étudiants étrangers) | intitulé seul, hors sujet des aides |
| arrêté du 24 juillet 2026 (bourse spécifique dans l'Union européenne) | ajustement |
| loi n° 98-111, art. 45-46 ; loi n° 99-101, art. 59-60 ; arrêté du 29 mars 2013 (abattement fiscal) | lisibles, non lus : intitulé seul ; les deux derniers vont à la fiscalité |

### 3.6 Figures

| Id | Contenu | Source | Ruptures à marquer | État |
|---|---|---|---|---|
| **F3** `fig-educ-boursiers` | étudiants, boursiers et part des boursiers, 2008-2009 à 2016-2017 | table de la note U § 5.1 (budget 2017 du ministère, p. 33 ; budget 2016, p. 26) — **pas de CSV** : à créer | 2011-2012 (régime de 2012, effet rétroactif) ; 2016-2017 marquée « prévision probable » | **après** création d'un CSV, versement et catalogue |
| — montants de la bourse | **pas de figure** dans cette version : sept dates, un tableau suffit | U § 3.1, IPC `ipc-longue-periode` | — | tableau maintenant ; `<!-- TODO (rédacteur) : remplacer par un tableau engendré -->` |

Pas de PIB dans ce chapitre.

### 3.7 Glossaire

`#g-bourse-scolaire`, `#g-fraction-de-bourse`, `#g-pension-demi-pension`, `#g-cantine-scolaire`,
`#g-foyer-scolaire`, `#g-office-oeuvres-scolaires`, `#g-droits-inscription`, `#g-orientation-d-office`,
`#g-commission-regionale-bourses-scolaires`, `#g-bourse-nationale`, `#g-pret-universitaire`,
`#g-office-oeuvres-universitaires`, `#g-oeuvres-universitaires`, `#g-bourse-integration-universitaire`,
`#g-bourse-specifique`, `#g-bourse-alternance`, `#g-allocation-supplementaire`,
`#g-bourse-hebergement`, `#g-hebergement-universitaire`, `#g-restauration-universitaire`,
`#g-presalaire`, `#g-smig`, `#g-condition-de-ressources`, `#g-epa`, `#g-amen-social`, `#g-tuteur`.

### 3.8 Recherches à ancrer

`sec-educ-bourses-scolaires` : `r-bourses-scolaires-apres-1974`, `r-bourses-scolaires-decision-ministre`.
`sec-educ-restauration-scolaire` : `r-cantines-scolaires-avant-2016`, `r-oss-contributions-eleves`,
`r-cahier-charges-restauration-eleves`. `sec-educ-frais-familles` : `r-assurance-scolaire-regime`,
`r-droits-inscription-repartition`. `sec-educ-bourse-nationale` : `r-bourse-montants-1982`,
`r-bourse-seuils-revenu-1986-2005`, `r-bourse-montants-apres-2017`. `sec-educ-oeuvres-universitaires` :
`r-oeuvres-prix-repas-lit-avant-2016`, `r-bourse-hebergement-30d-avant-2016`. `sec-educ-aides-ailleurs` :
`r-aide-rentree-avant-2020`.

---

## 4. Fiche de plan — `_depense.qmd` (dépense publique d'éducation)

**Objet.** Ce que l'État dépense pour l'éducation, en entonnoir : la part dans ses dépenses et dans le
PIB ; la dépense par ministère, par nature et par niveau ; les personnels ; puis la dépense des
ménages. Ensuite, à part et titrés comme tels, les rapports extérieurs et les études d'incidence.

**Titre proposé.** `# La dépense d'éducation {#sec-educ-depense}`

### 4.1 La frontière

C'est un chapitre de longue période, sans épine de textes. Ses « ruptures » sont des **ruptures de
série**. Elles se marquent sur les figures, et ne se racontent pas comme des réformes. **Le périmètre
retenu pour les parts est l'Éducation, l'Enseignement supérieur et la Recherche**, comme dans les
calculs de la note D (D § 2.4).

La formation professionnelle a sa série propre, montrée à part. Elle n'est cohérente qu'en 2009-2013
et en 2020-2023, et n'entre pas dans les parts. La question Q10 (retirer ou non la recherche) n'est
tranchable qu'en 2005-2018 : la recherche est **comprise**, et la figure le dit.

### 4.2 Les sections, dans l'ordre

**`## Vue d'ensemble {#sec-educ-depense-vue}`**

- *Essentiel* : l'Éducation, l'Enseignement supérieur et la Recherche pèsent 29,3 % des dépenses de
  gestion et de développement de l'État (hors dette) en 2009, et 20,3 % en 2023 (chiffre provisoire).
  Rapportée au PIB
  (base 2015), leur dépense passe de 5,9 % en 2010 à 6,1 % en 2023 (provisoire), avec un maximum de 6,9 % en 2020 ;
  la chute de 6,5 % en 2017 à 5,7 % en 2018 tient au stade du chiffre de 2017, plus élevé qu'un
  réalisé (D § 2.1). La note D (§ 2.4) écrit « de 5,8 % à
  6,9 % », mais son propre CSV donne 5,69 % pour 2018 : le rédacteur suit le CSV.
- *Vue d'ensemble* : la figure `fig-educ-depense-parts` (F4).
- *Points* :
  - la part de l'État baisse quand celle du PIB se maintient ;
  - la baisse apparente de 2017 à 2018 tient au **stade** des chiffres, non à la dépense : à dire dans
    le texte principal, **pas seulement en note** ;
  - les deux familles (budgétaire ; UNESCO-UIS) donnent des niveaux voisins en 2022, renvoi en tête à
    `@sec-educ-depense-rapports`.
- *Replié* : rien. Les dénominateurs vont dans l'onglet « Données » de la figure.

**`## Le périmètre et le stade des chiffres {#sec-educ-depense-perimetre}`**

- *Essentiel* : la source est l'*Annuaire statistique* de l'INS, qui relaie le ministère des Finances.
  Ses lignes changent de périmètre cinq fois en vingt-sept ans, et ses années ne sont ni les crédits
  votés ni les paiements de la loi de règlement.
- *Vue d'ensemble* : le tableau des libellés et des périmètres par période, `tbl-educ-perimetre`,
  **non replié**, parce que la lecture des figures en dépend (D § 2.3, points 1 à 3) :

  | Période | Éducation | Formation professionnelle | Supérieur et recherche |
  |---|---|---|---|
  | 1997-2001 | « Education Nationale » | avec l'emploi | « Enseignement Supérieur » |
  | 2002-2008 | **avec la formation professionnelle** | dans l'Éducation | recherche comprise (2002-2004) ; ligne propre dès 2005 |
  | 2009-2013 | « Education » | ligne propre | recherche en ligne propre |
  | 2014-2019 | idem | dans « Emploi » (gestion) | recherche comprise dans le supérieur, en gestion, dès 2019 |
  | 2020-2023 | idem | ligne propre | idem |

- *Points* :
  - **le stade** : année la plus récente d'une édition = provisoire ; troisième année = réalisations.
    Vérifié en 2012 sur le projet annuel de performance de 2014 ;
  - **le développement** se trace en deux segments, 1997-2008 et 2009-2023 : changement de périmètre
    en 2009, sans doute lié aux ressources extérieures affectées (hypothèse de la note, dite comme
    telle) ;
  - **les lois de règlement** donnent les paiements par partie, non par ministère. Constat : « Les
    tableaux par chapitre annexés aux lois de règlement ne sont pas identifiés ici. » Puis l'ancre
    `r-educ-lois-reglement-tableaux-par-chapitre`. « Aucune loi de règlement n'est identifiée pour 2021
    et après. » Puis l'ancre `r-educ-lois-reglement-2021-et-apres` ;
  - **les collectivités** : depuis 1958, des dépenses obligatoires (construction, entretien) leur
    incombent (renvoi à `_histoire.html#sec-educ-1958`). Depuis le code de 2018, l'entretien des écoles
    de base est une compétence partagée de la commune (lien finances locales). Aucune série de leur
    dépense d'éducation n'est rendue.
- *Replié* : `titre="Stade comptable de la série de l'Annuaire : comparaisons de 2010, 2012 et 2017 avec les crédits votés, le projet annuel de performance et la loi de règlement"`.
  Contenu : les trois comparaisons (D § 2.1) ; les crédits initiaux de 2010 lus au décret de
  répartition (`jort-credits-initiaux-*.csv`) ; la loi de règlement de 2017 ; les écarts
  non expliqués (Enseignement supérieur 2012 : 637 milliers de dinars ; Emploi en 2002-2003). Les
  mauvaises impressions de l'édition 1998-2002, non employées, vont en note du bloc.

**`## La dépense par ministère, 1997-2023 {#sec-educ-depense-ministeres}`**

- *Essentiel* : la gestion de l'Éducation passe de 0,96 milliard de dinars en 1997 à 6,5 milliards en
  2023, en dinars courants. La figure donne aussi les dinars de 2023.
- *Vue d'ensemble* : la figure `fig-educ-depense-ministeres` (F5).
- *Points* : la gestion fait l'essentiel ; le développement de l'Éducation double en 2023 (497 932
  contre 271 430 milliers de dinars en 2022 ; les deux années sont les deux premiers rangs de l'édition
  2019-2023, donc des chiffres provisoires, à dire tels) ; la formation
  professionnelle n'a de série propre que par segments.
- *Replié* : `titre="Dépense de l'État par ministère, gestion et développement : montants annuels, 1997-2023"`,
  le tableau D § 2.2 entier, avec édition et pages, et la colonne du stade.

**`## La dépense par nature {#sec-educ-depense-nature}`**

- *Essentiel* : les rémunérations font l'essentiel de la gestion de l'Éducation et de l'Enseignement
  supérieur. Les deux autres postes sont les « moyens des services » et les « interventions
  publiques ».
- *Vue d'ensemble* : la figure `fig-educ-depense-nature` (F6), en parts de la gestion.
- *Points* : la nomenclature passe de quatre à trois colonnes en 2003 ; deux sauts sans commentaire de
  la source (« autres dépenses » 2016-2017 ; « biens et services » 2017-2020) se marquent comme
  reclassements possibles ; les années absentes (2002, 2013, 2018, 2019, 2021) restent des trous.
- *Replié* : `titre="Dépense de gestion par nature et par ministère : montants annuels, 2001-2023"`
  (CSV `nature-*`).

**`## La dépense par niveau : le budget par programmes {#sec-educ-depense-programmes}`**

- *Essentiel* : depuis le budget par programmes, le ministère de l'Éducation sépare le primaire et le
  « préparatoire et secondaire ». En 2012, le second coûte près du double du premier.
- *Vue d'ensemble* : tableau court `tbl-educ-programmes` (D § 3), trois colonnes de stade
  différent : réalisations 2012, loi de finances 2013, propositions 2014. **Non replié.** Le programme
  de la formation comprend le Fonds national de l'emploi et des ressources propres (note du tableau).
- *Points* :
  - le découpage par cycle, choisi plutôt que par fonction (PAP de l'Éducation, p. 5) ;
  - le préscolaire public sans programme propre ;
  - les services universitaires, programme distinct du supérieur ;
  - la date du premier budget voté par programmes n'est pas établie : une phrase neutre, et la loi
    organique du budget de 2019 citée comme cadre.
- *Coût par élève* : constat neutre. « Aucune publication des ministères donnant un coût public par
  élève ou par étudiant n'est identifiée ici. » Puis l'ancre `r-educ-cout-unitaire-ministere-2021`.
  **Le calcul indicatif de la note D § 5.2 n'est pas rendu** : la note le réserve à la méthode. Les
  choix qu'il impose (pilotage, développement, recherche, services universitaires, année scolaire
  contre année budgétaire) sont une **question au propriétaire** (Q9).
- *Replié* : rien.

**`## Les enseignants et la masse salariale {#sec-educ-depense-personnels}`**

Renvoi en tête : la rémunération des enseignants relève du livre des rémunérations publiques.

- *Essentiel* : le public compte 72 213 enseignants au premier cycle de la base et 70 695 au second
  cycle et au secondaire en 2023-2024, et 23 545 dans le supérieur. Les rémunérations du ministère de
  l'Éducation atteignent 6,1 milliards de dinars en 2023 (chiffre provisoire).
- *Vue d'ensemble* : la figure `fig-educ-enseignants` (F7), deux onglets : effectifs ; rémunérations
  des ministères en dinars courants et de 2023.
- *Points* :
  - la masse salariale est celle de **tout le ministère** ; les agents (194 430 en 2018) ne sont pas
    les enseignants (136 115 en 2018-2019) ;
  - les révisions entre éditions ;
  - la loi de finances pour 2026 (art. 107) régularise les instituteurs et professeurs suppléants
    entrés avant 2008 et 2006. Une phrase, traduction de travail, sans date d'effet tant que l'article
    d'effet n'est pas lu.
- *Replié* : `titre="Enseignants du public par cycle : effectifs annuels, 1995-1996 à 2023-2024"`.

**`## La dépense des ménages {#sec-educ-depense-menages}`**

- *Essentiel* : selon l'enquête de l'INS, un Tunisien dépense pour l'enseignement 84 D par an en 2015
  et 81 D en 2021, soit 2,2 % puis 1,5 % de sa dépense.
- *Vue d'ensemble* : tableau court, deux lignes, avec les dinars de 2023.
- *Points* : la ventilation par poste et par décile n'est pas publiée dans le communiqué. Constat,
  puis l'ancre `r-educ-ebcnv-volume-depenses`. Les estimations d'associations sur le « coût d'un
  élève » ne sont pas reprises.
- *Replié* : rien.

**`## Ce que rapportent l'UNESCO-UIS et la Banque mondiale {#sec-educ-depense-rapports}`**

Titre de famille : rapports extérieurs, à part du budgétaire (modèle : `sante/_histoire.qmd`,
`#sec-soins-histoire-bm`). Deux sources, chacune avec sa méthode avant ses chiffres. Pas de niveau 3,
ou bien deux, un par source.

- **L'UNESCO-UIS, par la Banque mondiale.**
  - *Méthode*, avant tout chiffre : dépense des administrations publiques (centrales, régionales,
    locales), courante, en capital et en transferts, y compris les transferts reçus de l'étranger. Les
    séries viennent des *World Development Indicators* de la Banque mondiale (source UIS), consultées
    le 17 octobre 2026.
  - *Essentiel* : la part de l'éducation dans le PIB selon l'UIS, de 1980 à 2023, et dans les dépenses
    publiques, de 1992 à 2025.
  - *Vue d'ensemble* : la figure `fig-educ-uis` (F8), qui **superpose** la part budgétaire du chapitre.
    Les familles sont distinguées par le trait et la légende ; l'écart de périmètre est expliqué.
  - *Points* : périmètre plus large que les ministères ; les zéros de 1981-1986, 1990 et 1991 notent
    une absence de donnée (exclus) ; la dépense par élève en part du PIB par habitant (1997-2015), en
    second onglet.
  - *PIB* : un ratio **cité** de l'UIS se donne tel quel, sans commentaire sur sa base (AGENTS.md). La
    part budgétaire superposée, elle, dit sa base.
- **La Banque mondiale, 1995 : la répartition de la dépense d'éducation en 1990.**
  - *Méthode* : les inscriptions au public, relevées par l'enquête de l'INS de 1990 sur le budget et la
    consommation des ménages, sont multipliées par « la charge courante moyenne par programme, nette
    d'amortissement » ; classes de dépense de consommation par habitant (déciles) ; coût moyen ; privé
    hors champ (annexe D.1, p. 1).
  - *Chiffres cités*, entre guillemets et avec leur page (annexe D.1, p. 1-2) : « 71 DT » par
    habitant en moyenne ; « environ 50 DT » pour les 10 % les plus pauvres, « jusqu'à environ
    100 DT » pour les plus riches ; au primaire, « en moyenne à 40 DT par habitant parmi les 3 % les
    plus pauvres » et « moins de 20 DT » pour le décile supérieur ; au secondaire et au supérieur, des
    subventions « trois et vingt fois plus importantes » pour les 10 % les plus riches. Le rédacteur ne
    les résume pas d'un qualificatif (« progressif ») que la source n'emploie pas.
- *Non rendu* : la revue de la dépense publique de 2020 (`wb-tunisia-per-2020`, non lue).
- *Replié* : rien.

**`## Ce qu'établit une étude d'incidence : l'enquête de 2010 {#sec-educ-depense-evaluations}`**

Titre de famille : évaluation économique.

- **CEQ Working Paper 38 (2016, révisé en 2017), sur l'enquête de 2010.**
  - *Méthode* : bénéficiaires de bourse selon l'enquête ; montant par bénéficiaire = total
    administratif ÷ bénéficiaires, mis à l'échelle des comptes nationaux ; supérieur au coût moyen du
    budget du ministère (p. 16).
  - *Chiffres* : 98 533 boursiers en 2010, selon un rapport du ministère que l'étude cite (p. 12) ;
    une dépense du supérieur « progressive in relative terms only » (p. 22).
  - **L'écart avec le budget** (113 678 boursiers en 2009-2010) se dit, sans réconciliation.
- *Non rendu* : l'exercice CEQ 2021 (classeur non publié).
- *Replié* : rien.

**Section d'attente, non rendue** : `sec-educ-depense-economie`.

### 4.3 Clés à citer, par section

| Section | Clés |
|---|---|
| `sec-educ-depense-vue` | `ins-annuaire-statistique`, `ins-cnat-2015`, `minfin-indicateurs-fp` |
| `sec-educ-depense-perimetre` | `ins-annuaire-statistique`, `mineducation-pap-2014`, `mfpe-pap-2014`, `decret-2009-3750`, `lf-2010`, `loi2024-18` (à promouvoir), `loi58-118` (art. 30, par renvoi) |
| `sec-educ-depense-ministeres` | `ins-annuaire-statistique` |
| `sec-educ-depense-nature` | `ins-annuaire-statistique`, `mineducation-pap-2014` |
| `sec-educ-depense-programmes` | `mineducation-pap-2014`, `mesrs-pap-2014`, `mfpe-pap-2014`, `loi-org-2019-15-lob` |
| `sec-educ-depense-personnels` | `ins-annuaire-statistique`, `lf-2026` (art. 107, arabe) |
| `sec-educ-depense-menages` | `ins-ebcnv-2021-communique` |
| `sec-educ-depense-rapports` | `wb-wdi` (codes SE.XPD.TOTL.GD.ZS, SE.XPD.TOTL.GB.ZS, SE.XPD.PRIM.PC.ZS, SE.XPD.SECO.PC.ZS, SE.XPD.TERT.PC.ZS) ; `bm-1995-pauvrete-annexes` (à promouvoir) |
| `sec-educ-depense-evaluations` | `jouini-lustig-moummi-shimeles-2017-ceq38` (à promouvoir), `budget-mesrs-2017` (pour l'écart) |

### 4.4 Figures

| Id | Contenu | CSV ou série | Ruptures à marquer ; PIB | État |
|---|---|---|---|---|
| **F4** `fig-educ-depense-parts` | part de l'Éducation, de l'Enseignement supérieur et de la Recherche dans les dépenses de l'État (2009-2023) et dans le PIB (2010-2023) | `calcul-part-education-superieur-depenses-etat.csv`, `calcul-part-education-superieur-pib.csv` ; **à recalculer par le générateur** à partir des `gestion-*`, `developpement-*`, `etat-*` et de `denominateurs-depenses-etat-pib` | 2017 → 2018 : artefact de stade ; 2019 : la recherche passe dans le supérieur en gestion. **PIB base 2015 de l'INS, 2010-2014 rétropolés par l'INS** ; le segment 2005-2009 en base 1997 se calcule à part, en second segment non chaîné, avec renvoi à `annexe-pib.html#sec-pib-ruptures`. Part de l'État à côté | **après versement** |
| **F5** `fig-educ-depense-ministeres` | gestion et développement par ministère, 1997-2023, dinars courants puis de 2023 | `gestion-education.csv`, `gestion-enseignement-superieur.csv`, `gestion-recherche-scientifique.csv`, `gestion-formation-professionnelle.csv`, `gestion-emploi.csv`, `developpement-*.csv` ; `ipc-longue-periode` | 2002 (formation dans l'Éducation) ; 2009 (formation à part ; développement : nouveau segment) ; 2014-2019 (formation dans l'Emploi) ; 2019 (recherche dans le supérieur, en gestion) ; 2017 → 2018 (stade) | **après versement** |
| **F6** `fig-educ-depense-nature` | rémunérations, moyens des services, interventions, en parts de la gestion de l'Éducation et de l'Enseignement supérieur, 2001-2023 | `nature-education-*.csv`, `nature-enseignement-superieur-*.csv` | 2003 (nomenclature) ; 2017 et 2020 (reclassements possibles) ; points non reliés sur les années absentes | **après versement** |
| **F7** `fig-educ-enseignants` | enseignants du public par cycle, 1995-2024 ; rémunérations des ministères, 2001-2023 | `enseignants-public-*.csv`, `nature-*-remunerations.csv` ; `ipc-longue-periode` | révisions entre éditions (2009-2010 ; 2018-2021) | **après versement** |
| **F8** `fig-educ-uis` | UIS : dépense publique d'éducation en % du PIB (1980-2023) et en % des dépenses publiques (1992-2025), avec la part budgétaire de F4 superposée ; second onglet : dépense par élève en % du PIB par habitant | `rapport-uis-*.csv` ; F4 | familles distinguées ; zéros de la source exclus | **après versement** des JSON WDI à `tunisia-data` (empreintes en D § 6) |

Pas de figure pour les programmes (trois années), les ménages (deux années) ni les études (valeurs
citées).

### 4.5 Glossaire

`#g-depenses-de-gestion`, `#g-depenses-de-developpement`, `#g-remunerations-publiques`,
`#g-moyens-des-services`, `#g-interventions-publiques`, `#g-credits-d-engagement`,
`#g-credits-de-paiement`, `#g-mission-budgetaire`, `#g-programme-budgetaire`,
`#g-projet-annuel-performance`, `#g-rapport-annuel-performance`, `#g-loi-de-reglement`,
`#g-repartition-des-credits`, `#g-cout-unitaire`, `#g-coefficient-budgetaire`, `#g-oeuvres-universitaires`,
`#g-pib`.

### 4.6 Recherches à ancrer

`sec-educ-depense-perimetre` : `r-educ-lois-reglement-tableaux-par-chapitre`,
`r-educ-lois-reglement-2021-et-apres`. `sec-educ-depense-programmes` :
`r-educ-cout-unitaire-ministere-2021`. `sec-educ-depense-menages` : `r-educ-ebcnv-volume-depenses`.

---

## 5. Ce que les chapitres se renvoient

| D'où | Vers | Pourquoi |
|---|---|---|
| index, carte | chaque section de la carte | domicile de chaque dispositif |
| `sec-educ-1991`, bloc « gratuité » | `_aides.html#sec-educ-frais-familles` | les montants des droits vivent dans les aides |
| `sec-educ-etat-droit` | `_aides.html#sec-educ-frais-familles` | idem, une phrase |
| `sec-educ-superieur` (en tête) | `_aides.html#sec-educ-aides-etudiants` | bourses, prêts, œuvres |
| `sec-educ-2017` | `#sec-educ-formation-professionnelle` | détail de la loi n° 2017-13 |
| `sec-educ-1958` | `#sec-educ-conseil` | filiation du Conseil |
| `sec-educ-bourses-scolaires` | `_histoire.html#sec-educ-1958` | fondement légal de l'aide (art. 3) |
| `sec-educ-aides-donnees` | `_depense.html#sec-educ-depense-evaluations` | l'étude CEQ et son décompte des boursiers |
| `sec-educ-depense-perimetre` | `_histoire.html#sec-educ-1958` | dépenses obligatoires des collectivités |
| `sec-educ-depense-programmes` | `_aides.html#sec-educ-oeuvres-universitaires` | les services universitaires |
| `sec-educ-depense-vue` | `#sec-educ-depense-rapports` | comparaison avec l'UIS |
| `sec-educ-eleves` | `_depense.html#sec-educ-depense-personnels` | enseignants |

Un fait, un seul domicile : les effectifs d'élèves sont dans `sec-educ-eleves`, les enseignants dans
`sec-educ-depense-personnels`, les boursiers dans `sec-educ-aides-donnees`, et l'étude CEQ dans
`sec-educ-depense-evaluations`.

---

## 6. Les fiches de recherche : section de destination

À reporter dans le champ `ou` au moment de la fusion dans `docs/recherches.yml` (chef de chantier).
Les fiches A et B visent aujourd'hui des ancres `sec-aides-…` qui n'existeront pas ; les fiches C et D
ne visent qu'un fichier.

| Fiche | Lot | `ou` proposé |
|---|---|---|
| `r-bourse-montants-1982` | A | `precis/fr/education/_aides.qmd#sec-educ-bourse-nationale` |
| `r-bourse-seuils-revenu-1986-2005` | A | `…/_aides.qmd#sec-educ-bourse-nationale` |
| `r-bourse-montants-apres-2017` | A | `…/_aides.qmd#sec-educ-bourse-nationale` |
| `r-oeuvres-prix-repas-lit-avant-2016` | A | `…/_aides.qmd#sec-educ-oeuvres-universitaires` |
| `r-bourse-hebergement-30d-avant-2016` | A | `…/_aides.qmd#sec-educ-oeuvres-universitaires` |
| `r-bourses-scolaires-apres-1974` | B | `…/_aides.qmd#sec-educ-bourses-scolaires` |
| `r-bourses-scolaires-decision-ministre` | B | `…/_aides.qmd#sec-educ-bourses-scolaires` |
| `r-cantines-scolaires-avant-2016` | B | `…/_aides.qmd#sec-educ-restauration-scolaire` |
| `r-oss-contributions-eleves` | B | `…/_aides.qmd#sec-educ-restauration-scolaire` |
| `r-cahier-charges-restauration-eleves` | B | `…/_aides.qmd#sec-educ-restauration-scolaire` |
| `r-aide-rentree-avant-2020` | B | `…/_aides.qmd#sec-educ-aides-ailleurs` |
| `r-assurance-scolaire-regime` | B | `…/_aides.qmd#sec-educ-frais-familles` |
| `r-droits-inscription-repartition` | B | `…/_aides.qmd#sec-educ-frais-familles` |
| `r-loi58-118-art2-obligation` | C | `…/_histoire.qmd#sec-educ-1958` |
| `r-loi2002-80-art17-annee-preparatoire` | C | `…/_histoire.qmd#sec-educ-etat-droit` |
| `r-loi2008-19-art56-delais-lmd` | C | `…/_histoire.qmd#sec-educ-superieur` |
| `r-loi2017-13-art4-arrete` | C | `…/_histoire.qmd#sec-educ-formation-professionnelle` |
| `r-education-consultation-reforme` | C | `…/_histoire.qmd#sec-educ-conseil` |
| `r-educ-lois-reglement-tableaux-par-chapitre` | D | `…/_depense.qmd#sec-educ-depense-perimetre` |
| `r-educ-lois-reglement-2021-et-apres` | D | `…/_depense.qmd#sec-educ-depense-perimetre` |
| `r-educ-cout-unitaire-ministere-2021` | D | `…/_depense.qmd#sec-educ-depense-programmes` |
| `r-educ-ebcnv-volume-depenses` | D | `…/_depense.qmd#sec-educ-depense-menages` |

Rappel des notes A et D : fusionner **avant** la rédaction fait échouer la CI (fiches orphelines). On
fusionne avec les ancres.

---

## 7. Questions

### 7.1 Au documentaliste

1. **Loi n° 93-10** (orientation de la formation professionnelle) : la lire. Selon son contenu, la loi
   de 2008 est une rupture ou une étape.
2. **Fondement des droits du primaire** (décret n° 2010-1928) : la loi n° 2002-80, art. 36, ne vise
   que collèges et lycées. Quel article fonde les droits du primaire ? Et l'art. 36 dit-il autre chose
   que ce que la note H en rapporte ?
3. **Loi n° 89-70, art. 56 et 57**, réécrits par la loi de finances pour 1993 (loi n° 92-122), visés
   en 1995 : objet non relevé.
4. **Supérieur avant 1989** : décret n° 60-98 (date de signature), lois n° 69-3, 76-65, 86-80 ; loi
   n° 2000-73 (privé). Objet non relevé : aucune ne peut porter de rupture aujourd'hui.
5. **Clauses d'effet** non relues : loi de finances pour 1987 (suppression de l'ONOU, art. 87) ; loi de
   finances pour 2024 (art. 15) ; loi de finances pour 2026 (art. 107) ; loi n° 76-115 ; décret
   n° 2017-369, art. 5 et suivants.
6. **Barèmes des bourses scolaires lus en OCR seulement** : 4e partie du décret n° 72-229 (p. 969) ;
   4e partie de l'arrêté du 12 août 1974 (p. 1823-1824). Les relire à l'image avant de les rendre.
7. **Montants de la bourse nationale de 1974 et de 1978** (arrêtés à l'index, OCR nécessaire) : ils
   combleraient le trou de 1971-1988 du tableau principal.
8. **Budgets du ministère de l'Enseignement supérieur 2014-2016** : relire à l'image les colonnes
   (écart de 2015), lire l'indicateur de performance de 2014 (part des boursiers).
9. **Indicateurs des PAP 2014** (annexes non lues) : coût par élève, cantines aménagées.
10. **Méthode de l'UIS** pour les effectifs (écart de périmètre du secondaire), avant toute
    superposition dans `sec-educ-eleves`.
11. **Office des services scolaires** : annexes des lois de finances pour 2021 à 2026, à lire à
    l'image ; la ligne de 2018.
12. **Décret n° 62-403** (Conseil supérieur de l'éducation nationale) : le lire, pour la filiation.
13. **Exonération sous le SMIG** (décret n° 2010-1928, art. 3) : vaut-elle aussi pour les droits du
    primaire, ou seulement pour les collèges et les lycées ?

### 7.2 Au bibliographe

1. Promouvoir au fonds commun, ou copier, les six clés du § 0.3 marquées « à promouvoir », avant la
   rédaction.
2. Créer une clé pour le **décret n° 92-1186** du 22 juin 1992 (lu à l'image, note S § 4.3).
3. Porter les compléments déjà listés dans `biblio-a-rapatrier.md` (art. 44, 135, 142 dans
   `constitution2022`, etc.).
4. `jouini-lustig-moummi-shimeles-2017-ceq38` : la famille (évaluation, non rapport extérieur), écart
   relevé par la note U § 5.2.

### 7.3 Au terminologue

Inverser terme et synonyme de `office-oeuvres-scolaires` (« Office des services scolaires » comme
terme ; § 0.4).

### 7.4 Au propriétaire : classements à trancher, risques du plan

1. **2002** : rupture (retenue) ou étape de 1991.
2. **2017** : rupture (retenue) ou étape ; et sa place dans les grandes réformes.
3. **1989** (supérieur) : étape (retenue) ou rupture par les frais des étudiants « disposant de
   ressources ».
4. **1971** (bourse nationale) et **2012** : étapes (retenues) ou ruptures.
5. **2010** (droits au primaire) : étape (retenue) ou rupture.
6. **Coût par élève** : publier ou non le calcul indicatif de 2012 (par défaut : non) ; périmètre
   (Q9).
7. **Q10** : recherche comprise dans la part (retenu) ou retirée, et seulement sur 2005-2018.
8. **Risques du repli.**
   - L'artefact 2017 → 2018 et la rupture du développement en 2009 doivent rester **au premier plan**,
     pas seulement dans le bloc du stade.
   - Les deux régimes de bourse de 2009-2012 ne se replient pas : le point est au texte principal.
   - La gratuité « avec droits » est dite dans l'histoire, même si les montants sont dans les aides.
9. **Croissance** : l'histoire porte quatre sections de dispositif. Si elle dépasse la taille
   raisonnable, le supérieur et la formation sont les premiers candidats à un chapitre propre dans une
   version 2.

---

## 8. Points d'attention pour le rédacteur

**Ce que les notes corrigent dans le plan global**

- **L'obligation de six à seize ans date de 1991** (loi n° 91-65, art. 7), non de 2002. La loi de 2002
  la confirme (art. 1er).
- **La loi sur la restauration des élèves est la loi n° 2009-32** (clé
  `loi-2009-32-restauration-formation`). La notice de l'index qui la numérote 2009-39 est fausse ; la
  loi n° 2009-39 porte sur la mise à la retraite.
- **Les bourses scolaires existent encore en 2016-2017**, sous l'office des services scolaires
  (décret n° 2016-664, art. 2 ; budget 2017).
- **Le décret n° 2008-3123 se rattache au LMD** dans son intitulé et ses art. 2 et 3.
- **La loi de finances pour 1977, art. 15**, est une sanction (restitution majorée de 10 % par an), non
  une mesure de bourse.
- **La loi n° 2008-9 ne touche pas le privé.**
- **L'année préparatoire** est rattachée à la base, mais exclue de la gratuité et de l'obligation
  (loi n° 2002-80, art. 18).
- **Le décret-loi n° 2024-2** existe et a été lu (JORT n° 113 de 2024, édition arabe) ; la Constitution
  l'institue à l'art. 135.

**Pièges de dates**

- Effets **antérieurs à la signature** :
  - loi de 1958 (1er octobre 1958) ;
  - base de 1991 (« à compter de l'année scolaire 1989-1990 ») ;
  - arrêté du 31 mars 1988 (1er janvier 1988) ;
  - décret n° 2008-3123 (2006-2007) ;
  - décret n° 2009-3040 (1er septembre 2009) ;
  - textes du 9 octobre 2012 (2011-2012 ; prêts : 1er octobre 2011) ;
  - loi n° 2017-38 (2010-2011) ;
  - décret n° 2019-898 (année 2019-2020, publié le 22 octobre 2019).
- **Avant 1993** : un jour franc après la publication, en **fourchette** quand le fascicule couvre
  plusieurs jours (1966, 1971, 1972, 1986, 1988, 1990). La loi n° 70-9 est exécutoire le 12 mars 1970,
  non le 6 (la notice de l'index ne vaut pas).
- **Après 1993** : « au plus tôt » quand la date de dépôt n'est pas relevée (note H). Ne pas
  présenter un « au plus tôt » comme une date établie.
- **Constitution** : citer la clause de l'art. 142 (proclamation des résultats définitifs du
  référendum), jamais un calcul ; la date officielle est celle du référendum, le 25 juillet 2022
  (art. 141).
- **2012** : les budgets disent « à partir de 2013 » pour la hausse de la bourse ; l'arrêté dit
  2011-2012. **Le tableau suit l'arrêté.**
- **Office scolaire** : transfert des foyers, des cantines et des agents le 31 décembre 2016 (date du
  texte), distinct de la date du décret.
- L'arrêté du 4 décembre 2015 abroge « l'arrêté du 9 août 2012 » [sic] : il s'agit de celui du
  9 octobre 2012. L'arrêté du 4 novembre 1997 vise « 29 mars 1996 » [sic] pour 1995. La loi n° 88-137
  est visée « du 3 décembre 1998 » [sic] en 2012.

**Les mots qui se ressemblent**

- **« Préparatoire » a quatre sens** :
  - l'**année préparatoire** (préscolaire, 5-6 ans, loi de 2002, art. 16) ;
  - le **cycle préparatoire** (second cycle de la base, 3 ans, loi de 2002, art. 22) ;
  - l'**école préparatoire** (le collège dans la loi de 1991, art. 21) ;
  - le **cycle préparatoire de la formation professionnelle** (moins de 15 ans, loi de 2008, art. 13 ;
    jusqu'à 16 ans, loi de 2017, art. 2).

  Chaque emploi se lie à son ancre de glossaire, ou se nomme en entier.
- **Les durées du secondaire** :
  - 1958 : 6 ans (3 + 3), à côté d'un moyen de 3 ans ;
  - 1991 : 4 ans (2 + 2) ;
  - 2002 : 4 ans (1 + 3), à la rentrée 2003-2004 ;
  - 2008 : 4 ans, organisation renvoyée au décret.
- **Les trois conseils** : Conseil supérieur de l'éducation nationale (1958) ; Conseil supérieur de
  l'éducation (1991, 2000) ; Conseil supérieur de l'éducation et de l'enseignement (2022-2024). Les
  ancres de glossaire sont distinctes.
- **L'examen de fin de base** : obligatoire en 1991 (art. 10), facultatif depuis la loi n° 2002-5,
  « général » ou « technique » depuis 2008.

**Les amendes du tuteur**

- 1991, art. 32 : de 10 à 100 D, 200 D en récidive. La note H l'a relu à l'image ; la note S l'avait lu
  en OCR, avec les mêmes valeurs.
- 2002, art. 21, et 2017, art. 3 : de 20 à 200 D, 400 D en récidive.

**Le nom de l'office scolaire**

- **Office des services scolaires** ; en arabe **ديوان الخدمات المدرسية**.
- L'édition française du décret de 2016 dit « office des œuvres scolaires ». C'est l'arabe qui fait foi
  (loi n° 93-64, art. 1er). On écrit « office des services scolaires », avec le lien
  `#g-office-oeuvres-scolaires`.
- Ne pas confondre avec les **offices des œuvres universitaires** (ديوان الخدمات الجامعية), trois depuis
  1988, ni avec l'**Office national des œuvres universitaires** (1970-1987).

**Valeurs que les notes déclarent douteuses ou non établies**

- **Effectifs du premier cycle, 1999-2000** : la source imprime 1 440 795, total incohérent. Le public
  et le privé font 1 413 795, qu'il faut retenir (somme des CSV).
- **Supérieur, 2006-2007** : rupture de définition (« étudiants réguliers »), sans année de
  recouvrement.
- **Dépense 2017** : chiffre de dernière année d'édition, au-dessus du réalisé 2018. La baisse de 2017
  à 2018 est un artefact.
- **Développement 2008/2009** : changement de périmètre dans toutes les séries. Deux segments, jamais
  chaînés.
- **Formation professionnelle** : cohérente en 2009-2013 et en 2020-2023 seulement ; « - » en gestion
  de 2014 à 2019 (comptée dans « Emploi »). Pas de somme silencieuse.
- **Recherche** : comprise dans le supérieur, en gestion, depuis 2019.
- **Emploi, 2002-2003** (91 100 puis 24 200) et **Enseignement supérieur 2012** (écart de 637) :
  non expliqués.
- **Nature** : sauts de 2016-2017 et de 2017-2020 ; à dire « reclassement possible, non confirmé ».
- **Masse salariale** : celle de tout le ministère ; les agents ne sont pas les enseignants.
- **Boursiers 2016-2017** : probable prévision. **Écart CEQ** : 98 533 contre 113 678, non
  réconcilié.
- **Crédits 2013-2016 identiques** : crédits reconduits, non dépense constatée.
- **Office scolaire, loi de finances pour 2018** : lignes décalées dans le tableau officiel ; valeur
  **non établie**.
- **Effectifs du primaire aux pages du budget** : ce ne sont pas des bénéficiaires de cantines.
- **PAM, 260 000 enfants** : inutilisable en l'état.
- **Capacité de 68 000 places** (2012-2013) : point unique, non rendu.
- **Prêt des caisses, 2017** : date exécutoire sous réserve des articles non lus.

**PIB et dinars constants**

- La part du PIB est en **base 2015 de l'INS** ; **2010-2014 sont rétropolés par l'INS** ; avant 2010,
  la base est 1997, en segment séparé, jamais chaîné. Renvoi à `annexe-pib.html#sec-pib-ruptures`.
- La part des dépenses de l'État, sans base, se donne à côté. Elle commence en 2009 (rupture du
  développement).
- Les ratios de l'UIS sont **cités** : on ne commente pas leur base.
- Dinars de 2023 par `ipc-longue-periode`, qui ne remonte pas avant 1976.

**Textes en arabe seulement, et URL**

- Textes concernés :
  - Constitution de 2022 (numéro spécial) ;
  - décret-loi n° 2024-2 ;
  - lois de finances pour 2024 (art. 15) et 2026 (art. 107) ;
  - décrets gouv. n° 2018-927 et 2019-806 ;
  - arrêté du 5 mars 2019 ;
  - décret gouv. n° 2019-898 (édition française absente du corpus).
- Ils se citent en traduction **de travail**, dite telle. L'édition française n'a pas d'URL
  (404) : on ne l'invente pas.
- Le fichier local `2019/fr/Jo0212019.pdf` est l'édition arabe.

**Ce qui ne s'écrit pas**

- Ni « n'a pas été retrouvé », ni la liste des fascicules lus : un constat, puis l'ancre.
- Ni « le modèle », ni le classeur CEQ 2021, ni ses valeurs.
- Aucun nom de personne vivante (signataires, nominations).
- Pas de récit sur la langue ou sur l'enseignement zitounien en 1958 : la loi n'en dit rien, et c'est
  tout ce qu'on écrit.

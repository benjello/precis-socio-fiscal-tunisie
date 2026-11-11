# Plan de la dimension historique du volume « L'éducation et la formation »

Fiche de plan (architecte), 10 novembre 2026. Livrable : un plan, aucun `.qmd`. Matière première :
les deux notes documentaires du 10 novembre 2026 — `education-histoire-superieur-2026-11-10.md`
(supérieur 1958 → 2016, textes lus à l'image) et `education-histoire-autres-niveaux-2026-11-10.md`
(formation professionnelle 1993 → 2022, préscolaire, complétude du scolaire). Contexte structurel :
`education-plan-2026-10-17.md` (§ 3, chapitre 1), les chapitres existants (`_histoire.qmd`,
`_superieur.qmd`, `_formation_professionnelle.qmd`, `_scolaire.qmd`) et le format « ruptures au
premier plan » (`conventions-redaction.md` § 4, `chantier-ruptures-au-premier-plan.md`).

---

## 1. La décision de domicile, argumentée

**Décision : option B affinée (mixte à dominante B).** L'histoire *transversale* du système reste au
chapitre 1 (`_histoire.qmd`) ; l'histoire *propre à chaque ordre* vit dans la section « mise en place
et grandes réformes » de son chapitre de dispositif (2 scolaire/préscolaire, 3 formation
professionnelle, 4 supérieur). Le chapitre 1 ne narre aucune rupture interne du supérieur ni de la
formation professionnelle : il les cite d'une ligne, dans sa frise, avec un renvoi.

**Ce que garde le chapitre 1.** Les grandes lois qui structurent *tout* le système et touchent les
règles communes — obligation, gratuité, langue d'enseignement : loi de 1958 (mise en place), 1991
(école de base et obligation), 2002 (loi d'orientation, année préparatoire), 2017 (obligation de
formation jusqu'à dix-huit ans). Plus la filiation du Conseil supérieur (1958 → 1991 → 2000 → 2022 →
2024) et le fonds de la réforme éducative (2024). C'est l'état actuel du chapitre, qu'il faut
conserver tel quel : il est déjà au format « ruptures au premier plan » et bien sourcé.

**Ce que reçoivent les chapitres de dispositif.**
- `_superieur.qmd` : l'épine chronologique de l'enseignement supérieur, aujourd'hui absente — la
  création de l'Université de Tunis (1960), les lois d'organisation de 1969, 1976, 1986, la loi
  unique de 1989, la gouvernance de 2000, le système LMD de 2008. Ses lignes 1969/1976/1986, jadis
  en TODO, sont désormais lues : c'est le gros du travail nouveau.
- `_formation_professionnelle.qmd` : la refonte de 1993 complétée (loi 93-12 des centres CENAFFIF et
  CNFCPP, absente du registre), les conversions en EPNA (1997, 2003), l'homologation (1994), le
  décret-loi de 2022. L'épine 1993 → 2008 → 2017 existe déjà pour l'essentiel.
- `_scolaire.qmd` : l'histoire des tutelles du préscolaire (transfert des jardins d'enfants au
  ministère de la famille, 2002-2003 ; kouttabs), dans sa section « Le préscolaire ».

**Les trois raisons.**
1. **Éviter la redite.** Un fait se raconte une seule fois (consigne du rôle ; `conventions` § 4).
   Si le chapitre 1 narrait les cycles de 1976, les universités régionales de 1986 ou les centres de
   1993, le chapitre de dispositif les redirait, ou se viderait. L'épine d'un ordre appartient à son
   chapitre.
2. **La règle des trois à six ruptures par épine.** Le chapitre 1 porte déjà quatre grandes réformes
   scolaires (1958, 1991, 2002, 2017). Y verser les trois ruptures du supérieur (1976, 1986, 2008)
   et les deux de la formation professionnelle (1993, 2008) ferait une épine à neuf ou dix ruptures,
   illisible et contraire au plan § 3 (« le détail de chaque ordre va aux chapitres 2 à 4 »).
3. **Le texte principal se suffit, et le lecteur suit un dispositif de bout en bout.** Qui lit le
   chapitre du supérieur doit y trouver son histoire complète, sans renvoi obligé au chapitre 1 ;
   qui lit le chapitre 1 doit comprendre qui est scolarisé et sous quelle obligation, sans dépendre
   des chapitres de dispositif. Les deux lectures sont autonomes, reliées par des renvois en tête.

**Ce qui reste au chapitre 1 malgré l'option B.** Trois charnières *transversales* par nature :
(a) le décret n° 89-1295 de 1989 (Conseil supérieur de l'éducation et de l'enseignement supérieur),
déjà au registre du Conseil (`@sec-educ-conseil`) — il n'est pas une réforme du supérieur mais un
organe consultatif commun ; (b) l'obligation de formation de 2017, qui touche l'obligation scolaire
et reste narrée en `#sec-educ-2017`, citée depuis le chapitre 3 ; (c) la langue d'enseignement
(arabisation), fil commun suivi dans la note langue du 30 octobre 2026, cité par chaque chapitre.

---

## 2. Le plan de la section d'histoire, ordre par ordre

### 2.1 L'enseignement supérieur — `_superieur.qmd`

**Constat sur l'existant.** Le chapitre est organisé « dans l'ordre du parcours de l'étudiant »
(accès, établissements, diplômes, formation pratique). Sa seule approche chronologique, la section
« Les lois : 1989, 2008 et le système LMD » (`#sec-educ-superieur-lois`), *commence en 1989* et ne
traite 1960-1986 que comme des lignes de registre, aujourd'hui retirées faute de contenu établi
(TODO en fin de fichier). Le registre replié `#sec-educ-superieur-textes` porte déjà 1958, 1960,
1989 → 2017. **Travail demandé : remonter l'épine à 1958-1960 et narrer 1969 → 1986.**

**Section à créer / réorganiser.** Transformer `#sec-educ-superieur-lois` en une épine chronologique
complète, titre « La mise en place et les grandes réformes » (identifiant conservé
`#sec-educ-superieur-lois` pour ne pas casser les renvois ; sous-titre de travail possible
« De l'Université de Tunis au système LMD »). Enchaînement « ruptures au premier plan » :

1. **Vue d'ensemble** (`#sec-educ-superieur-vue`, à enrichir) : l'essentiel en une phrase, puis le
   tableau court des ruptures. Le tableau actuel n'a que deux lignes (1989, 2008) ; **ajouter** la
   mise en place (1958-1960) et les ruptures de 1976 et 1986. Cible : cinq à six lignes (mise en
   place ; 1976 ; 1986 ; 1989 ; 2008), colonnes « ce que la loi cherche, dans ses mots » / « avant →
   après ». La frise du chapitre 1 (`@fig-educ-frise`) couvre déjà le supérieur ; ne pas la dupliquer.
2. **La mise en place, 1958-1960** : l'enseignement supérieur troisième ordre de la loi de 1958
   (ch. III, art. 25-27 : facultés, instituts, grandes écoles isolés, aucune université) ; puis
   l'érection de l'**Université de Tunis** par la loi de finances n° 60-2 (art. 16) et son décret
   organique n° 60-98 (établissement public unique groupant toutes les facultés et écoles). Antécédent
   à poser : l'absence d'université, les établissements isolés de 1958.
3. **Les grandes réformes, dans l'ordre des dates** (le cœur : organisation de l'ordre et sens du mot
   « université ») :
   - **1969** (loi 69-3) — première loi d'organisation propre à l'ES : personnalité civile,
     professeur-directeur, tests d'orientation obligatoires, gratuité réaffirmée. *Étape* (voir § 3).
   - **1976** (loi 76-65) — *rupture* : trois cycles (court, moyen, long), trois secteurs, accès
     ouvert aux bacheliers, abandon des tests d'orientation de 1969.
   - **1986** (loi 86-80) — *rupture* : « université » cesse de désigner l'organe national unique
     pour désigner un groupement régional pluridisciplinaire (Tunis, Monastir, Sfax) dirigé par un
     recteur — le modèle encore en vigueur.
   - **1989** (loi 89-70, déjà au registre) — *étape* : la loi unique, qui abroge le ch. III de 1958
     et les lois de 1969, 1976, 1986 et fait converger l'ordre.
   - **2000** (loi 2000-67) — *étape de gouvernance* : le président d'université remplace le recteur,
     apparition des contrats de formation et de recherche et du comité d'habilitation (préfigure
     2008).
   - **2008** (loi 2008-19 + décret 2008-3123) — *rupture* : le système licence-mastère-doctorat.
     (Déjà narré ; raccorder l'épine amont à ce point.)
4. **Les entre-temps et ajustements**, en une phrase chacun avec renvoi au registre : 1997 (conseil
   des universités, loi 97-21), 2004 (diplôme universitaire de technologie, décret 2004-2722, filière
   courte de trois ans sans référence LMD — à rapprocher de la licence appliquée 2004-2721 déjà
   narrée), 2016 (unité de gestion par objectifs de la réforme, décret gouv. 2016-1100, appui Banque
   mondiale à l'employabilité).
5. **L'état du droit** : il est déjà exposé par les sections « parcours de l'étudiant » existantes
   (`#sec-educ-superieur-acces`, `-etablissements`, `-universites`, `-iset`, `-prive`, `-diplomes`,
   `-formation-pratique`), qui deviennent les *fiches* après l'épine. Chacune se situe dans l'épine
   (« née de la loi de 2008 », « statut fixé en 1986 puis 2000-2008 »).
6. **Le tableau replié** `#sec-educ-superieur-textes` : y **rétablir** les lignes 1969, 1976, 1986
   (changement concret, avant → après, colonne « Portée »), avec renvoi d'abrogation vers 1989
   (loi 89-70, art. 33) ; **ajouter** 1997, 2000-67, 2004-2722, 2016-1100. Le registre va alors de
   1958 à 2017 sans trou.

**Ordre des sections dans le fichier** : vue d'ensemble → épine (mise en place + grandes réformes) →
fiches de parcours → registre replié. C'est l'ordre actuel, l'épine remplaçant « Les lois ».

### 2.2 L'enseignement scolaire et le préscolaire — `_scolaire.qmd`

**Scolaire : rien à refaire sur le corps des lois** (note autres niveaux, § 3 : 1958, 1991, 2002,
2008 complets et sourcés). L'histoire scolaire transversale reste au chapitre 1 ; `_scolaire.qmd`
garde ses registres par thème (obligation, gratuité, cycles et langues, examens, préscolaire,
collectivités et privé, cours particuliers).

**Préscolaire : une sous-histoire à loger dans la section « Le préscolaire »** (chapitre 2, section 4
du plan § 3 ; identifiant à créer `#sec-educ-scolaire-prescolaire` s'il n'existe pas). Enchaînement :
1. **Vue d'ensemble** : trois réseaux, trois tutelles (jardins d'enfants ; kouttabs ; année
   préparatoire des écoles publiques).
2. **La construction des tutelles, 1974 → 2024** (détail replié, titre « Préscolaire : tutelles et
   cahiers des charges, date par date ») : le transfert des jardins d'enfants vers le ministère de la
   famille se lit comme une *chaîne*, non un texte unique — rattachement de la direction générale de
   l'enfance (décret 2002-2103, 23 septembre 2002), volet régional (décret 2003-471, 3 mars 2003),
   attributions du ministère (décret 2003-2020, 22 septembre 2003), d'où découle le cahier des
   charges de 2003 déjà au chapitre. Classement : **étape de la mise en place** (aucune rupture ; un
   transfert administratif). Le texte dira le constat sans jargon : « la tutelle des jardins d'enfants
   passe au ministère chargé de la famille entre 2002 et 2003 ».
3. **Les kouttabs** : garder la réserve actuelle (1980 réorganisation, 1990 autorisation par le
   gouverneur) ; le texte de transfert au ministère des affaires religieuses reste introuvable — ancre
   `RECHERCHE` existante `r-educ-kouttabs-tutelle-affaires-religieuses` (périmée), à relancer, pas à
   rouvrir. Ne rien affirmer sur la tutelle.
4. **L'année préparatoire** : déjà couverte (cahier de 2001, extension au privé 2008) ; la
   généralisation prévue par l'art. 17 de la loi 2002-80 reste sans texte (fiche périmée
   `r-loi2002-80-art17-annee-preparatoire`, à relancer). Renvoi en tête vers le chapitre 1
   (`#sec-educ-2002`, année préparatoire).

### 2.3 La formation professionnelle initiale — `_formation_professionnelle.qmd`

**Constat sur l'existant.** L'épine 1993 → 2008 → 2017 existe (`#sec-educ-fp-lois`,
`#sec-educ-fp-vue`, registre `#sec-educ-fp-textes`). Manque la **loi 93-12 des centres** et les
**conversions en EPNA** (1997, 2003), que la note vient de lire ; le décret-loi 2022-78 est à ajouter.

**Section à enrichir** (`#sec-educ-fp-lois`, « La loi de 2008 et l'obligation de 2017 » → élargir le
titre à « La refonte de 1993, la loi de 2008 et l'obligation de 2017 ») :
1. **Vue d'ensemble** (`#sec-educ-fp-vue`, existante) : ajouter une phrase sur la refonte de 1993
   comme mise en place du dispositif actuel (dissolution de l'OFPE ; agences ; centres d'appui).
2. **La mise en place, 1993** : la refonte par quatre lois du 17 février 1993 (JORT n° 14) —
   loi 93-10 (orientation, déjà narrée), loi 93-11 (agences ATE/ATFP, domicile marché du travail,
   renvoi déjà posé), **loi 93-12 (création du CENAFFIF et du CNFCPP**, à narrer : deux établissements
   publics, ingénierie de formation et formation des formateurs d'une part, formation continue et
   promotion professionnelle d'autre part ; patrimoine de l'OFPE dissous transféré). Antécédent :
   l'OFPE (loi de finances complémentaire n° 88-60). Classement du bloc 1993 : **rupture** (voir § 3).
3. **Les grandes réformes / étapes** : la loi de 2008 (déjà narrée) ; l'obligation de 2017 (narrée au
   chapitre 1, citée ici — renvoi existant `#sec-educ-2017`).
4. **Les étapes institutionnelles, repliées** : conversion du CNFCPP en EPNA (loi 97-64, 1997),
   conversion du CENAFFIF en EPNA et recentrage ingénierie (loi 2003-77, 2003), homologation des
   diplômes (décret 94-1397, 1994, chapitre III maintenu en 2009), élargissement des missions de
   l'ATFP et renommage de l'agence sœur (décret-loi 2022-78, 2022).
5. **Le tableau replié** `#sec-educ-fp-textes` : **rétablir / ajouter** les lignes loi 93-12,
   loi 97-64, loi 2003-77, décret-loi 2022-78 (le TODO de fin de fichier les redemande déjà), avec
   changement concret et colonne « Portée ».

**Point de vocabulaire à trancher** (signalé par la note) : le décret 94-1397 emploie
« Chapitre I/II/III » là où le décret 2009-2139 et le chapitre actuel parlent de « titres I/II/III ».
Harmoniser dans le registre (le mot arabe أبواب a pu être traduit « titre »). Question au
documentaliste si un doute subsiste.

---

## 3. Le classement des ruptures, arbitré

Reprise et arbitrage des deux notes. Rappel : une rupture ne repose que sur un texte dont la note a
lu l'article ; tous les textes ci-dessous sont lus à l'image.

### Enseignement supérieur (épine de `_superieur.qmd`)

| Texte | Portée arbitrée | Motif | Autre lecture (à laisser ouverte) |
|---|---|---|---|
| 1958 (loi 58-118, ch. III) + 1960 (loi 60-2 art. 16, décret 60-98) | **mise en place** | l'ES troisième ordre, puis l'Université de Tunis, organe unique | — |
| 1969 (loi 69-3) | **étape** | structuration : personnalité civile, professeur-directeur, tests d'orientation | rupture (première loi-cadre propre à l'ES) — notée |
| 1976 (loi 76-65) | **rupture** | architecture des cycles court/moyen/long, trois secteurs ; abandon des tests de 1969 | étape (continuité gratuité/arabisation) — notée |
| 1986 (loi 86-80) | **rupture** | sens moderne d'« université » : groupement régional pluridisciplinaire, recteur ; modèle encore en vigueur | étape préparant 1989 — notée |
| 1989 (loi 89-70) | **étape** | loi unique ; abroge 1958 ch. III, 1969, 1976, 1986 ; fait converger l'ordre | — |
| 1997 (loi 97-21) | **ajustement** | conseil des universités (art. 12 nouveau) | — |
| 2000 (loi 2000-67) | **étape de gouvernance** | président remplace recteur ; contrats de formation-recherche ; comité d'habilitation (préfigure 2008) | rupture de gouvernance — notée |
| 2004 (décret 2004-2722, DUT) | **étape** | filière courte technologique de trois ans, sans référence LMD (parallèle à 2004-2721) | ajustement — notée |
| 2008 (loi 2008-19 + décret 2008-3123) | **rupture** | système licence-mastère-doctorat | — |
| 2016 (décret gouv. 2016-1100) | **étape** | gouvernance de projet ; appui Banque mondiale à l'employabilité | ajustement (structure temporaire) — notée |

→ **Épine à cinq temps** : mise en place (1958-60) ; 1976 ; 1986 ; 1989 ; 2008. Trois ruptures
(1976, 1986, 2008), 1989 charnière d'unification. 1969, 2000 sont des étapes ; 1997, 2004, 2016 des
ajustements/étapes dans les entre-temps. Conforme à la règle « trois à six ruptures par épine ».

### Formation professionnelle (épine de `_formation_professionnelle.qmd`)

| Texte | Portée arbitrée | Motif | Autre lecture |
|---|---|---|---|
| lois 93-10 / 93-11 / 93-12 (1993) | **rupture** (un seul bloc) | refonte d'ensemble : dissolution de l'OFPE, orientation, agences, centres d'appui, apprentissage de 1972 absorbé | — |
| décret 94-1397 (1994) | **étape de 1993** | homologation des diplômes (ch. III maintenu en 2009) | — |
| loi 97-64 (1997) | **étape de 1993** | CNFCPP en EPNA | — |
| loi 2003-77 (2003) | **étape de 1993** | CENAFFIF en EPNA, recentrage ingénierie | — |
| loi 2008-10 (2008) | **rupture** | public et objectif nouveaux : trois cycles, baccalauréat professionnel créé, accès au supérieur | étape de 1993 — notée (proposition en attente au fichier) |
| décret-loi 2022-78 (2022) | **ajustement** | missions ATFP élargies (internat, insertion, expertise), renommage de l'agence emploi | — |

→ **Épine à trois temps** : mise en place 1993 (rupture) ; 2008 (rupture) ; 2017 (obligation, narrée
au chapitre 1). **Arbitrage recommandé** sur la proposition en attente : garder 1993 et 2008 comme
*deux ruptures distinctes* (1993 crée le dispositif, 2008 crée un public et un diplôme nouveaux),
plutôt que 2008 étape de 1993 — mais la décision appartient au propriétaire : présenter les deux
lectures dans la colonne « Portée » tant qu'il n'a pas tranché, comme le fait déjà le fichier.

### Préscolaire (section de `_scolaire.qmd`)

Aucune rupture : la chaîne 2002-2003 de transfert des tutelles est une **étape de mise en place**
administrative. Les kouttabs et la généralisation de l'année préparatoire restent sous réserve
(textes introuvables).

---

## 4. Les renvois inter-chapitres à poser

- **Chapitre 1 → chapitre 4 (supérieur)** : dans la frise et le récit de 1958, une ligne « l'ES,
  troisième ordre » renvoyant à `_superieur.qmd#sec-educ-superieur-lois` ; idem pour 1989 (déjà via
  le registre du Conseil). Le chapitre 1 ne détaille pas 1960/1969/1976/1986/2008.
- **Chapitre 1 → chapitre 3 (FP)** : renvoi existant `#sec-educ-2017` ↔ `_formation_professionnelle`
  pour l'obligation de 2017 ; ajouter un renvoi vers l'épine FP pour la refonte de 1993.
- **Chapitre 4 (supérieur) → chapitre 1** : en tête de l'épine, renvoi vers la loi de 1958
  (`#sec-educ-1958`) comme loi mère, et vers la filiation du Conseil (`#sec-educ-conseil`, où vit déjà
  le décret 89-1295). Le fil langue/arabisation renvoie à `education-langue-enseignement-histoire-2026-10-30.md`.
- **Chapitre 3 (FP) → livre des cotisations** : le CNFCPP gère la taxe de formation professionnelle —
  renvoi vers `cotisations_sociales/_prelevements_salaires.html#sec-cot-tfp` (lien à poser dans la
  ligne CNFCPP). Renvoi existant vers le marché du travail pour les agences, à conserver.
- **Chapitre 2 (préscolaire) → chapitre 1** : en tête de la section préscolaire, renvoi vers
  `#sec-educ-2002` (année préparatoire).

---

## 5. Prêt à rédiger vs en attente (lacunes des deux notes)

### Prêt à rédiger (textes lus à l'image)

- **Supérieur** : 1958, 1960 (loi 60-2 + décret 60-98), 1969, 1976, 1986, 1989, 1997, 2000, 2004
  (DUT), 2016. L'épine complète peut s'écrire.
- **Formation professionnelle** : loi 93-12, loi 97-64, loi 2003-77, décret 94-1397, décret-loi
  2022-78 (plus 93-10, 93-11, 2008-10, 2009-2139 déjà intégrés). La refonte de 1993 et les étapes
  EPNA peuvent s'écrire.
- **Préscolaire** : chaîne 2002-2103 / 2003-471 / 2003-2020 (transfert des jardins d'enfants). La
  sous-histoire des tutelles peut s'écrire.

### En attente — bloque ou limite la rédaction

- **Supérieur — prorogation de l'unité 2016-1100** : décret visé non identifié de façon sûre
  (candidats : décret présidentiel 2022-683, décret 2025-200 ; la « 2023-12 » du brief est une loi de
  finances) → la ligne registre 2016 peut s'écrire *sans* la prorogation ; ancrer une fiche
  `docs/recherches.yml` si le rédacteur veut la mentionner. [à vérifier, lisible sur pist.tn]
- **Supérieur — doublon décret 60-98** : notice n° 24 du 13 mai 1960 (p. 693) non lue ; vérifier s'il
  s'agit d'un rectificatif/republication avant de figer la date. [lisible]
- **Supérieur — page de tête du décret 2016-1100** (p. 2719) lue par décodage, non à l'image ;
  souhaitable de la clore. [lisible]
- **Supérieur — arabisation des disciplines** (sciences humaines, ~1976) : décrets/arrêtés
  d'application non lus ; le corps des lois ne la porte pas. Le fil langue reste à sourcer. [à chercher]
- **FP — décrets de la loi 2008-10** : art. 38 (organisation des établissements publics de FP) et
  art. 57 (commission nationale d'évaluation et d'assurance qualité) non identifiés ; arrêté de
  l'art. 55 remplaçant le ch. III du décret 94-1397 non identifié. Ouvrir les fiches
  `r-educ-fp-2008-art38-etablissements-publics` et `r-educ-fp-2008-art57-commission-evaluation`.
  L'état du droit FP reste partiel sur ces points. [lisible, non lu / à chercher]
- **FP — aucune série** (apprenants, diplômés, apprentis) : bloque toute figure de longue période du
  chapitre 3 ; rapports d'activité ATFP et statistiques ministère à obtenir. [à obtenir]
- **Préscolaire — kouttabs** : texte de transfert au ministère des affaires religieuses introuvable ;
  indices contraires (arrêté 2007 « Premier ministère »). Réserve maintenue, aucune affirmation.
  Décret 88-1962 / 2014-4567 à lire avant de conclure. [à chercher / lisible non lu]
- **Préscolaire — généralisation de l'année préparatoire** (art. 17 loi 2002-80) : fiche périmée à
  relancer. [à chercher]
- **Préscolaire — effectifs** (jardins, kouttabs) : à obtenir avant toute figure. [à obtenir]
- **Scolaire — filiation du Conseil supérieur** : décrets n° 62-403 (1962) et n° 89-1295 (1989) non
  lus (TODO `_histoire.qmd` encore ouvert) ; manque structurant mais transversal, déjà tracé. [lisible]

---

## 6. Checklists

### Pour le rédacteur

- `_superieur.qmd` : transformer `#sec-educ-superieur-lois` en épine chronologique (mise en place
  1958-60 → 1969 → 1976 → 1986 → 1989 → 2000 → 2008), en conservant l'identifiant ; enrichir le
  tableau court de `#sec-educ-superieur-vue` (ajouter mise en place, 1976, 1986) ; rétablir au
  registre `#sec-educ-superieur-textes` les lignes 1969/1976/1986 (+ 1997, 2000-67, 2004-2722,
  2016-1100) avec colonne « Portée » et renvoi d'abrogation vers 1989. Les sections « parcours »
  existantes deviennent les fiches, chacune situant son objet dans l'épine. Ne pas parler du modèle.
- `_formation_professionnelle.qmd` : narrer la mise en place de 1993 avec la loi 93-12 (centres
  CENAFFIF/CNFCPP) ; ajouter les étapes EPNA (1997, 2003) et le décret-loi 2022-78 ; compléter le
  registre `#sec-educ-fp-textes`. Harmoniser « titre » / « chapitre » du décret 94-1397.
- `_scolaire.qmd` : écrire la sous-histoire des tutelles du préscolaire (chaîne 2002-2003) dans la
  section préscolaire, détail replié ; maintenir les réserves kouttabs et année préparatoire.
- Règle commune : les ruptures au premier plan, le registre replié ; le texte principal se suffit ;
  renvois en tête ; aucune mention d'openfisca ni du jargon de dépouillement.

### Pour le terminologue (notions à ancrer, sans toucher `glossaire.yml`)

- Supérieur : Université de Tunis ; recteur (d'université) ; président d'université ; cycles court /
  moyen / long (architecture de 1976) ; diplôme universitaire de technologie (DUT) ; conseil des
  universités ; contrat de formation et de recherche ; unité de gestion par objectifs.
- Formation professionnelle : CENAFFIF ; CNFCPP ; IPST (institut de promotion supérieure du travail) ;
  ingénierie de formation ; homologation des certificats et diplômes ; direction générale de l'enfance.
- À vérifier (existent probablement) : jardin-d-enfants, kouttab, moueddeb, année-préparatoire,
  apprentissage, certificat-de-competence, licence/mastère/doctorat, EPA/EPST/EPNA, baccalauréat.

### Pour le bibliographe (clés à verser avant rédaction, sans créer les clés ici)

- Supérieur (à créer) : `loi60-2`, `loi69-3`, `loi76-65`, `loi86-80`, `loi97-21`, `loi2000-67`,
  `decret2004-2722`, `decret-gouv2016-1100`. Déjà présentes : `loi58-118`, `decret60-98`, `loi89-70`,
  `loi2000-73`, `decret2004-2721`.
- Formation professionnelle (à créer) : `loi93-12`, `loi97-64`, `loi2003-77`, `decret94-1397`,
  `decret-loi2022-78`. Déjà présentes : `loi93-10`, `loi93-11`, `loi2008-10`, `decret2009-2139`,
  `decret94-1600`, `decret2007-4147`.
- Préscolaire (à créer) : `decret2002-2103`, `decret2003-471`, `decret2003-2020` ; secondaires si
  retenus : `decret2005-1257`, `loi88-97`, `decret88-1962`, `decret2014-4567` (kouttabs, à vérifier).
- Rappel conventions : clé identique = même notice dans tous les livres ; pagination arabe =
  clé `<clé>-ar` distincte.

---

## 7. Risques et désaccords à faire trancher

- **1986 rupture ou étape** : retenu rupture (sens moderne d'« université », encore en vigueur) ;
  lecture étape-vers-1989 laissée ouverte dans la colonne « Portée ».
- **2008-10 (FP) rupture ou étape de 1993** : recommandation = rupture distincte ; décision du
  propriétaire attendue (proposition déjà en attente au fichier). Ne pas trancher en silence.
- **Ce que le repli pourrait cacher** : l'épine du supérieur remonte à 1958 ; veiller à ce que les
  lignes 1969/1976/1986 restaurées au registre ne restent pas invisibles au premier plan — les
  ruptures 1976 et 1986 doivent paraître dans le tableau court, pas seulement dans le replié.
- **Fil langue** : l'arabisation est un fil commun à plusieurs ordres ; risque de redite entre
  chapitre 1, scolaire et supérieur. La traiter une fois (note langue du 30 octobre), citée partout.

---

## Backlog (lignes proposées — à verser par l'archiviste-backlog, hors de ce fichier)

- [backlog-precis] Supérieur : rédiger l'épine 1958-2008 dans `_superieur.qmd` (lignes 1969/1976/1986
  lues, à rétablir au registre avec renvoi d'abrogation vers 1989) ; enrichir le tableau court de
  `#sec-educ-superieur-vue`. [lisible]
- [backlog-precis] FP : narrer la mise en place de 1993 avec la loi 93-12 (centres) et les étapes
  EPNA (1997, 2003) + décret-loi 2022-78 dans `_formation_professionnelle.qmd`. [lisible]
- [backlog-precis] Préscolaire : écrire la chaîne de transfert des tutelles (2002-2003) dans la
  section préscolaire de `_scolaire.qmd`. [lisible]
- [recherches.yml] Relancer `r-educ-kouttabs-tutelle-affaires-religieuses`,
  `r-loi2002-80-art17-annee-preparatoire` ; ouvrir `r-educ-fp-2008-art38-etablissements-publics`,
  `r-educ-fp-2008-art57-commission-evaluation` ; fiche prorogation de l'unité 2016-1100. [à chercher]
- [backlog-precis] Doublon décret 60-98 (notice n° 24, p. 693) et page de tête du décret 2016-1100
  (p. 2719) à clore. [lisible]
- [backlog-precis] Séries FP (apprenants, diplômés) et effectifs préscolaire : à obtenir avant toute
  figure des chapitres 3 et 2. [à obtenir]
- [backlog-precis] Scolaire : décrets du Conseil supérieur 62-403 (1962) et 89-1295 (1989) non lus,
  filiation à clore (TODO `_histoire.qmd`). [lisible]
</content>

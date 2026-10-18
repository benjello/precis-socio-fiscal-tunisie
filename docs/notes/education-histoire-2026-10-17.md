# L'éducation, chapitre 1 : histoire législative — note documentaire

Note du documentaliste, 17 octobre 2026, pour le chapitre 1 du livre de l'éducation (« De la loi de
1958 au Conseil supérieur de l'éducation et de l'enseignement »,
`docs/notes/education-plan-2026-10-17.md`, § 3). Matière seulement : aucun `.qmd`, aucune entrée de
`references.json` ni de `glossaire.yml` n'a été écrite. Les fiches de recherche proposées sont dans
`docs/notes/education-recherches-C.yml`, à fusionner dans `docs/recherches.yml`.

**Méthode.** Chaque texte est lu au fascicule du *Journal officiel*, à l'image dès que la couche
texte manquait ou était douteuse.
- **1958 n° 89, 1989 n° 54 et n° 61, 1991 n° 55** : scans sans couche texte. Océrisés pour repérer
  les pages (`/tmp/education-ocr-C/`), puis lus **à l'image** ; chaque chiffre cité est relu à
  l'image.
- **2000 n° 82, 2002 n° 6, 7, 62 et 69** : texte à police décalée. Décodé par le décalage de 29 de
  `outillage-sources.md` § 5 ; la loi n° 2002-80 est relue entièrement à l'image.
- **2008, 2011, 2017** : couche texte saine.
- **2022, 2023, 2024, 2025** : édition arabe seulement. Le numéro spécial de la Constitution est un
  scan, lu à l'image.

Toutes les adresses pist.tn ci-dessous ont été testées le 17 octobre 2026 (`curl -k`). Toutes
répondent `200 application/pdf`, et chaque fichier téléchargé est identique octet pour octet à la
copie du corpus local. Les fascicules français ont été ouverts et sont bien en français.

**Datation** (`AGENTS.md`, « Dater »). Une clause d'effet énoncée par le texte est reprise telle
quelle. Sinon, on retient la date à laquelle le texte devient exécutoire :
- **jusqu'en 1993** : un jour franc après la publication ;
- **depuis la loi n° 93-64** : cinq jours après le dépôt au siège du gouvernorat de Tunis.

Aucune date de dépôt n'est connue ici. La date donnée est donc calculée « au plus tôt » sur la date
de publication, selon la convention de `retraites/_secteur_public.qmd`. Un fascicule à deux dates
est calculé sur la première, la seconde entre parenthèses.

---

## 1. Texte par texte

### 1.1 Loi n° 58-118 du 4 novembre 1958 relative à l'enseignement — **lu**

- **Fascicule** : JORT n° 89 du 7 novembre 1958, p. 1056-1060, édition française. Pages du fichier
  6 à 10. Lu à l'image, en entier. <https://www.pist.tn/jort/1958/1958F/Jo08958.pdf>. Index : recid
  118226.
- **Visas** : décret du 15 septembre 1888 relatif à l'enseignement ; décret du 21 janvier 1920
  relatif aux écoles privées (p. 1056).
- **Ce que la loi cherche, dans ses mots** (titre premier, « Principes généraux », art. 1er,
  p. 1056). « L'éducation et l'instruction ont pour buts essentiels :
  - 1° de permettre à tous les enfants des deux sexes, sans distinction d'ordre racial, religieux ou
    social, le développement de leur personnalité et de leurs aptitudes naturelles ;
  - 2° de contribuer au développement des progrès de la science et d'assurer en même temps à tous,
    le bénéfice de ces progrès ;
  - 3° de favoriser le développement et l'épanouissement de la culture nationale ;
  - 4° de préparer les enfants à leur rôle de citoyens et d'hommes, et de former les cadres
    nécessaires aux développements de l'activité nationale dans ses divers aspects. »
- **Rubriques.** Titre I, Principes généraux. Titre II, De l'enseignement : chapitre I, primaire ;
  chapitre II, second degré (section I, moyen ; section II, secondaire) ; chapitre III, supérieur.
  Titre III, De l'enseignement public : établissements, personnel, conseils de l'enseignement.
  Titre IV, De l'enseignement privé : conditions d'ouverture et de fonctionnement, dispositions
  transitoires.
- **Ce qui change pour l'élève.**
  - **Accès.** « L'accès à l'éducation et à l'instruction est ouvert à tous les enfants à partir de
    l'âge de six ans » (art. 2, p. 1057).
  - **Obligation, annoncée seulement.** « Des dispositions ultérieures fixeront la date à partir de
    laquelle l'obligation d'assurer aux enfants l'instruction de six à douze ans, sera imposée à tous
    les parents et sur tout le territoire tunisien » (art. 2, al. 2). La loi n'impose donc aucune
    obligation. Le texte annoncé n'est pas identifié : fiche `r-loi58-118-art2-obligation`.
  - **Gratuité.** « l'enseignement sera dispensé gratuitement à tous les degrés » (art. 3). L'État
    accorde aussi « toute l'aide possible aux élèves et étudiants » doués dont les familles n'ont pas
    de ressources suffisantes.
  - **Ordres d'enseignement** (art. 4) : premier degré ou primaire ; second degré, à deux branches,
    moyen et secondaire ; supérieur.
  - **Primaire** : un cycle unique de six ans, que peut précéder un court cycle d'éducation
    enfantine (art. 8).
  - **Enseignement moyen.** Trois ans, dans les collèges moyens, en trois sections : générale,
    commerciale, industrielle (art. 11). Il est sanctionné par un brevet d'enseignement moyen,
    ouvert dès quatorze ans (art. 13).
  - **Secondaire** : six ans, en deux cycles de trois ans, avec trois options, générale, économique
    et technique (art. 15). Le baccalauréat est en deux parties (art. 23).
  - **Langue.** La loi ne fixe pas de langue d'enseignement générale. Seules deux mentions :
    - la section de lettres modernes porte sur « la langue et la littérature arabes et sur les
      langues étrangères », celle de lettres classiques sur « la langue et la littérature arabes et
      la pensée islamique » (art. 18, p. 1057-1058) ;
    - le privé doit enseigner « la langue et la littérature arabes, l'histoire et la géographie de
      la Tunisie et de l'Afrique du Nord » au moins comme le public (art. 53, p. 1059-1060).

    Le sort de l'enseignement zitounien n'est pas réglé dans le texte de la loi : aucun article ne le
    nomme.
- **Institutions.**
  - Les collectivités ont des **dépenses obligatoires** : construction, logement du personnel,
    entretien, mobilier, éclairage et chauffage (art. 30).
  - L'art. 38 crée un **Conseil supérieur de l'éducation nationale**, présidé par le secrétaire
    d'État à l'Éducation nationale, « appelé à donner son avis sur les questions relatives à
    l'enseignement ». C'est le premier maillon de la filiation du § 1.10.
  - L'art. 39 crée un conseil d'orientation dans chaque établissement du second degré.
- **Privé** : déclaration, autorisation, conditions de nationalité, d'âge et de titres (art. 40 à
  56). Les établissements existants se conforment au plus tard le 1er octobre 1959 (art. 57).
- **Date d'effet** : « La présente loi, qui prend effet à partir du 1er octobre 1958 » (art. 60).
  C'est une clause d'effet, antérieure à la signature (4 novembre) et à la publication (7 novembre).
- **Travaux préparatoires** : aucune mention au fascicule.

### 1.2 Loi n° 89-70 du 28 juillet 1989 relative à l'enseignement supérieur et à la recherche scientifique — **lu** (art. 1er à 33) ; rectificatif **lu**

- **Fascicule** : JORT n° 54 des 4 et 8 août 1989, p. 1169-1172. Pages du fichier 3 à 6, lu à
  l'image. <https://www.pist.tn/jort/1989/1989F/Jo05489.pdf>. Index : recid 113755.
- **Rectificatif** : JORT n° 61 du 12 septembre 1989, p. 1392. Page du fichier 10, lu à l'image.
  <https://www.pist.tn/jort/1989/1989F/Jo06189.pdf>. Index : recid 113738.
- **Travaux préparatoires** : discussion et adoption par la Chambre des députés en sa séance du
  26 juillet 1989 (note (1), p. 1169).
- **Ce que la loi cherche** (art. 1er) : l'enseignement supérieur et la recherche « ont pour mission
  de contribuer au développement de la nation… ». L'article énumère ensuite neuf objectifs. Le
  5e alinéa est rectifié au n° 61 : « Favoriser l'arabisation et la généralisation de l'utilisation
  de la langue arabe et de sa promotion dans les différentes disciplines, et assurer la maîtrise des
  langues étrangères ». Le texte du n° 54 portait « Favoriser la généralisation de l'utilisation de
  la langue… ».
- **Ce qui change pour l'étudiant.**
  - **Accès** : ouvert aux titulaires du baccalauréat ou d'un diplôme équivalent (art. 4).
  - **Organisation** : cycles, avec modules, années ou certificats (art. 19). Le cadre général du
    régime des études est fixé par décret.
  - **Universités** : établissements publics administratifs (art. 5) ; conseil des universités
    (art. 12).
  - **Aide de l'État** sous conditions fixées par décret, « sous forme de bourse, de prêt ou de
    prestations en nature ou de l'exemption du paiement des droits » (art. 30).
  - **Ressources des établissements** (art. 28, rétabli par le rectificatif) : elles comprennent
    « les frais d'inscription qui seraient exigés des étudiants disposant de ressources, d'assurance,
    de bibliothèque, de laboratoire et d'examen ».
- **Abrogations** (art. 33) :
  - le chapitre III (art. 25 à 27) de la loi n° 58-118 ;
  - la loi n° 69-3 du 24 janvier 1969 portant organisation de l'enseignement supérieur (index :
    1969/004, p. 116-117) ;
  - la loi n° 76-65 du 12 juillet 1976 relative à l'enseignement supérieur et à la recherche
    scientifique (index : 1976/046, p. 1644-1645) ;
  - la loi n° 86-80 du 9 août 1986 relative aux universités (index : 1986/044, p. 860-861).
- **Modifications connues par l'index** : loi n° 97-21 du 22 mars 1997 (1997/024, p. 492) ; loi
  n° 2000-67 du 17 juillet 2000 (2000/057, p. 1739-1741).
- **Date d'effet** : aucune clause. Exécutoire un jour franc après la publication, soit le 6 août
  1989 (le 10 août si l'on retient la seconde date du fascicule, le 8 août).

### 1.3 Loi n° 91-65 du 29 juillet 1991 relative au système éducatif — **lu** (en entier)

- **Fascicule** : JORT n° 55 du 6 août 1991, p. 1398-1400. Pages du fichier 10 à 12, lu à l'image.
  <https://www.pist.tn/jort/1991/1991F/Jo05591.pdf>. Index : recid 113404.
- **Travaux préparatoires** : discussion et adoption par la Chambre des députés en sa séance du
  24 juillet 1991 (note (1), p. 1398).
- **Ce que la loi cherche** (chapitre I, « Principes de base », art. 1er, p. 1398) : « Le système
  éducatif a pour objectif de réaliser, dans le cadre de l'identité nationale tunisienne et de
  l'appartenance à la civilisation arabo-musulmane, les finalités suivantes ». Suivent treize
  finalités, dont :
  - (4) « Donner aux élèves la maîtrise de la langue arabe, en tant que langue nationale » ;
  - (5) leur faire maîtriser « une langue étrangère au moins » ;
  - (3) « une vie qui ne laisse place à aucune forme de discrimination et de ségrégation fondées sur
    le sexe, l'origine sociale, la race ou la religion ».
- **Rubriques** : chapitre I, principes de base ; chapitre II, de l'enseignement de base et de
  l'enseignement secondaire ; chapitre III, supérieur, qui « demeure régi par la loi n° 89-70 »
  (art. 25) ; chapitre IV, privé ; chapitre V, dispositions diverses.
- **Ce qui change pour l'élève.**
  - **Gratuité et droit à la scolarité** (art. 4). « L'État garantit, gratuitement, à tous ceux qui
    sont en âge d'être scolarisés, le droit à la formation scolaire. » Une aide est prévue pour les
    élèves de familles « économiquement modestes ».
  - **Ressources des établissements** (art. 24) : elles comprennent des « droits d'inscription
    pouvant être mis à la charge des élèves dont les revenus des parents le leur rendent à même de
    les payer », ainsi que des droits d'assurance et de bibliothèque.
  - **Préscolaire** : facultatif, organisé par des institutions spécialisées (art. 5).
  - **Obligation scolaire.** « L'enseignement de base est obligatoire à partir de l'âge de 6 ans
    jusqu'à l'âge de 16 ans, pour tout élève à même de poursuivre régulièrement ses études »
    (art. 7, p. 1399). L'obligation de six à seize ans date donc de 1991, non de 2002.
  - **Durée** : enseignement de base de neuf ans (art. 8), en deux degrés.
    - Premier degré : six ans, à l'école primaire.
    - Second degré : trois ans, dans les « écoles préparatoires » (art. 21).
  - **Langue.** « Dans les deux degrés de l'enseignement de base, toutes les matières concernant les
    humanités, les sciences et les techniques sont enseignées en arabe » (art. 9).
  - **Examen** : la fin de la base est sanctionnée par un examen national, dont les admis obtiennent
    le « diplôme de fin d'études de l'enseignement de base » (art. 10).
  - **Secondaire** : ouvert aux titulaires de ce diplôme ; deux cycles de deux ans chacun (art. 11).
    Il est sanctionné par le baccalauréat (art. 14).
  - **Amende** (art. 32, p. 1400). Le tuteur qui n'inscrit pas son enfant, ou le retire avant
    16 ans, s'expose à une amende de **10 à 100 dinars**, portée à **200 dinars** en cas de récidive.
    Le tuteur qui réside loin de l'école la plus proche en est exempté, selon une distance fixée par
    décret. Ce décret est le n° 92-1186 du 22 juin 1992 (index : 1992/041, p. 816, recid 92391 ;
    non lu). L'art. 32 ne s'applique qu'après la parution de la loi.
- **Conseil supérieur de l'éducation** : « consulté sur les questions d'intérêt national relatives
  à l'éducation et à l'enseignement », composition et mission par décret (art. 2).
- **Dates d'effet.**
  - Pas de clause générale : exécutoire un jour franc après la publication, soit le **8 août 1991**.
  - Clauses propres :
    - art. 34 : les dispositions sur l'enseignement de base s'appliquent « année par année, à
      compter de l'année scolaire 1989-1990 », c'est-à-dire avant la loi ;
    - art. 35 : à partir de l'année scolaire 1991-1992, l'orientation est reportée à la fin de la
      cinquième année du secondaire, jusqu'à ce que l'école de base atteigne sa neuvième année.
  - **Abrogation progressive** de la loi n° 58-118, qui « cesse progressivement d'être appliquée et
    sera abrogée lorsque l'école de base arrivera au terme de sa neuvième année » (art. 36).
- **Modification** : loi n° 2002-5 du 21 janvier 2002 (§ 1.4).

### 1.4 Loi n° 2002-5 du 21 janvier 2002 modifiant la loi n° 91-65 — **lu** (texte trouvé dans cette passe)

- **Fascicule** : JORT n° 7 du 22 janvier 2002, p. 131. Texte à police décalée, décodé.
  <https://www.pist.tn/jort/2002/2002F/Jo0072002.pdf>. Index : recid 111324.
- **Travaux préparatoires** : séance de la Chambre des députés du 15 janvier 2002.
- **Contenu** (article unique : art. 10 nouveau) : « Au terme de l'enseignement de base, tout élève
  qui le désire, peut passer un examen national en vue de l'obtention du "diplôme de fin de
  l'enseignement de base" ». L'examen, qui sanctionnait la base en 1991, devient **facultatif**.
- **Date d'effet** : aucune clause. Exécutoire au plus tôt le 27 janvier 2002.
- **Adresse pist.tn** : testée le 17 octobre (200, identique au corpus).

### 1.5 Loi d'orientation n° 2002-80 du 23 juillet 2002 relative à l'éducation et à l'enseignement scolaire — **lu** (en entier, à l'image)

- **Fascicule** : JORT n° 62 du 30 juillet 2002, p. 1735-1740. Pages du fichier 3 à 8.
  <https://www.pist.tn/jort/2002/2002F/Jo0622002.pdf>. Index : recid 111244.
- **Travaux préparatoires** : séance de la Chambre des députés du 19 juillet 2002 (p. 1735).
- **Rectificatif** : JORT n° 69 du 23 août 2002, p. 1991, décodé.
  <https://www.pist.tn/jort/2002/2002F/Jo0692002.pdf>. Il ne touche que des intitulés de la p. 1737 :
  le chapitre IV devient « Des établissements scolaires » au lieu de « éducatifs », et son titre
  premier « Des établissements scolaires publics ».
- **Ce que la loi cherche** (chapitre premier, « De la mission de l'éducation et des fonctions de
  l'école »).
  - Art. 1er : « L'éducation est une priorité nationale absolue et l'enseignement est obligatoire de
    six à seize ans. L'enseignement est un droit fondamental garanti à tous les Tunisiens sans
    discrimination fondée sur le sexe, l'origine sociale, la couleur ou la religion ; c'est aussi un
    devoir qu'assument conjointement les individus et la collectivité. »
  - Art. 2 : « L'élève est au centre de l'action éducative. »
  - Art. 3 : l'éducation doit élever les élèves « dans la fidélité à la Tunisie » et l'ouverture
    « sur la civilisation universelle ».
- **Numéros d'article relus à l'image** (relecture demandée par le plan).

| Disposition | Article | Page | Texte |
|---|---|---|---|
| Obligation de six à seize ans | **art. 1er** | 1735 | « l'enseignement est obligatoire de six à seize ans » |
| Gratuité | **art. 4**, al. 1er | 1735 | « L'Etat garantit le droit à l'enseignement gratuit dans les établissements scolaires publics à tous ceux qui sont en âge d'être scolarisés » |
| Préscolaire, dont l'année préparatoire (5-6 ans) | **art. 16** | 1736 | éducation préscolaire de trois à six ans ; « La dernière année, qui concerne la tranche d'âge de 5 à 6 ans, constitue une année préparatoire au cycle primaire » |
| Généralisation de l'année préparatoire | **art. 17** | 1736 | « L'Etat veille à généraliser l'année préparatoire… dans le cadre de la complémentarité entre l'enseignement scolaire public et les initiatives des collectivités locales, des associations et du secteur privé » |
| L'année préparatoire fait partie de l'enseignement de base | **art. 18** | 1736 | « L'année préparatoire fait partie de l'enseignement de base. Les dispositions du paragraphe 1 de l'article 4 et celles du paragraphe 1 de l'article 20 de la présente loi ne s'appliquent pas à l'année préparatoire. » |
| Base obligatoire tant que l'élève peut suivre ; pas d'exclusion définitive avant 16 ans | **art. 20** | 1736 | |
| Amende du tuteur | **art. 21** | 1736-1737 | « une amende allant de vingt (20) à deux cents (200) dinars. Cette amende est de quatre cents (400) dinars en cas de récidive » |

L'article 18 change la lecture du plan. L'année préparatoire est rattachée à l'enseignement de base,
mais la loi en écarte **la gratuité** (art. 4 § 1) et **l'obligation de base** (art. 20 § 1). Le
plan disait seulement qu'elle « fait partie de l'enseignement de base ».

- **Ce qui change pour l'élève.**
  - **Base** : neuf ans, en deux cycles (art. 22).
    - Cycle primaire de six ans.
    - « Cycle préparatoire » de trois ans, dans les collèges (art. 30). Le terme désigne le second
      cycle de la base, à ne pas confondre avec l'année préparatoire du préscolaire.
  - **Langue.** Les disciplines « sociales, scientifiques, techniques et artistiques » sont
    enseignées en arabe dans les deux cycles de la base (art. 24). L'école donne la maîtrise de
    l'arabe et de « deux langues étrangères au moins » (art. 9). Les langues étrangères sont
    enseignées « dès le premier cycle » (art. 51).
  - **Secondaire** : **quatre ans**, dont un tronc commun d'un an puis trois ans en filières
    (art. 26). L'art. 69 en reporte l'effet à la rentrée 2003-2004.
  - **Fin de base** : examen national facultatif (art. 61), dans la ligne de la loi n° 2002-5.
    Baccalauréat (art. 62).
  - **Droits** : les ressources des collèges et lycées comprennent des « droits d'inscription mis à
    la charge des élèves dont les parents ont un revenu qui leur permet de s'en acquitter », ainsi
    que des droits d'assurance et de bibliothèque (art. 36).
  - **Établissements** : écoles primaires, collèges, lycées, lycées pilotes, écoles virtuelles
    (art. 29). Les collèges et lycées sont des établissements publics administratifs (art. 35).
  - **Privé** : autorisation (art. 38), programmes officiels (art. 40).
  - **Évaluation** : chapitre VII, art. 58 à 65.
- **Dates d'effet.**
  - Pas de clause générale : exécutoire au plus tôt le 4 août 2002.
  - Clause propre : les art. 26 et 27 « prennent effet à compter de la rentrée scolaire 2003-2004 »
    (art. 69).
  - Abrogation : en même temps que la loi entre en application, la loi n° 91-65 « cessera
    progressivement d'être appliquée » (art. 70).
- **Conseil supérieur** : la loi d'orientation n'a pas d'article sur un conseil supérieur. L'art. 2
  de la loi n° 91-65 n'est pas repris.

### 1.6 Loi n° 2008-9 du 11 février 2008 modifiant et complétant la loi d'orientation n° 2002-80 — **lu**

- **Fascicule** : JORT n° 14 du 15 février 2008, p. 681-683. Le texte finit p. 683, alors que
  l'index donne 681-682. <https://www.pist.tn/jort/2008/2008F/Jo0142008.pdf>. Index : recid 110063.
- **Travaux préparatoires** : Chambre des députés, 29 janvier 2008 ; Chambre des conseillers,
  7 février 2008.
- **Contenu.**
  - Elle remplace les art. 22 à 27, 29, le dernier alinéa de l'art. 32, et les art. 35 et 61.
    Elle ajoute un art. 60 bis et abroge l'art. 28.
  - **Langues.** Le cycle primaire et le cycle préparatoire doivent doter l'élève de compétences de
    communication « dans la langue arabe et au moins dans deux langues étrangères » (art. 22
    nouveau). Art. 24 nouveau : les disciplines restent enseignées en arabe dans la base, mais
    « Néanmoins, une ou plusieurs langues étrangères peuvent être utilisées dans tous les cycles de
    l'enseignement ».
  - **Secondaire** : quatre ans (art. 26 nouveau). Le tronc commun d'un an n'est plus écrit dans la
    loi ; l'organisation et l'orientation sont renvoyées au décret.
  - **Passerelles** avec la formation professionnelle (art. 23 et 27 nouveaux) : alternance pour
    les élèves du cycle préparatoire et du secondaire. Les apprenants de la formation
    professionnelle peuvent s'inscrire au lycée pour préparer le baccalauréat.
  - **Établissements** (art. 29 nouveau) : apparaissent les **collèges pilotes** et les
    « établissements d'éducation et de formation à distance », qui remplacent les écoles virtuelles.
  - **Examens.** Art. 60 bis : **concours d'accès aux collèges pilotes** à la fin du primaire.
    Art. 61 nouveau : diplôme de fin de l'enseignement de base, « général » ou « technique ».
- **Portée sur le privé.** Le plan se demandait si cette loi porte sur le privé. La réponse est
  non : elle ne touche pas les articles du privé (art. 38 à 44).
- **Date d'effet** : aucune clause. Exécutoire au plus tôt le 20 février 2008.

### 1.7 Loi n° 2008-10 du 11 février 2008 relative à la formation professionnelle — **lu** (art. 1er à 34, 64-65)

- **Fascicule** : JORT n° 14 du 15 février 2008, p. 683-688.
  <https://www.pist.tn/jort/2008/2008F/Jo0142008.pdf>. Index : recid 110064.
- **Travaux préparatoires** : mêmes séances que la loi n° 2008-9.
- **Ce que la loi cherche** (art. 1er). « La formation professionnelle est l'une des principales
  composantes du dispositif national de préparation des ressources humaines et l'un des leviers du
  développement. » Elle vise à qualifier les demandeurs de formation, à développer les capacités des
  travailleurs et à doter l'entreprise des moyens d'améliorer sa productivité.
- **Ce qui change pour l'apprenant.**
  - **Formation initiale et formation continue** (art. 7).
  - **Formation initiale en trois cycles** (art. 9) :
    - certificat d'aptitude professionnelle, après la 9e année de base ;
    - brevet de technicien professionnel, ou baccalauréat professionnel (créé par cette loi) ;
    - cycle supérieur : brevet de technicien supérieur.
  - **Passerelles** dans les deux sens avec le secondaire (art. 11). Le baccalauréat professionnel
    ouvre l'accès au supérieur dans les spécialités compatibles (art. 12).
  - **« Certificat de compétence »** pour qui n'a pas le niveau du premier cycle, et cycle
    préparatoire pour les moins de quinze ans (art. 13).
  - **Alternance** dès quinze ans. Apprentissage entre quinze et vingt ans, par contrat écrit visé
    par l'administration (art. 15 et 18). L'indemnité d'apprentissage est à la charge de
    l'entreprise et n'est pas soumise aux cotisations de sécurité sociale (art. 19).
  - **Ressources des établissements publics** : elles comprennent des « frais d'inscription et
    d'assurance » (art. 33).
- **Date d'effet.**
  - Aucune clause générale. Exécutoire au plus tôt le 20 février 2008.
  - Art. 65 : « En même temps que la présente loi entre en application, la **loi n° 93-10 du
    17 février 1993 portant loi d'orientation de la formation professionnelle**, ensemble les textes
    qui l'ont modifiée et complétée, cesseront progressivement d'être appliqués ». La loi n° 93-10 est
    le texte fondateur de 1993 que le plan cherchait. Index : 1993/014, p. 252-256, recid 113086 ;
    non lue.

### 1.8 Loi n° 2008-19 du 25 février 2008 relative à l'enseignement supérieur — **lu** (art. 1er à 9, 56 à 58)

- **Fascicule** : JORT n° 19 du 4 mars 2008, p. 844-850.
  <https://www.pist.tn/jort/2008/2008F/Jo0192008.pdf>. Index : recid 110043.
- **Travaux préparatoires** : Chambre des députés, 6 février 2008 ; Chambre des conseillers,
  14 février 2008.
- **Ce que la loi cherche.**
  - Art. 1er : « assurer la formation universitaire, développer les aptitudes, contribuer à édifier
    la société du savoir ».
  - Art. 2 : entre autres, « renforcer l'employabilité des diplômés » et « consolider l'utilisation
    de la langue arabe et la maîtrise des langues étrangères ».
- **Ce qui change pour l'étudiant.**
  - **Trois étapes** (art. 3) : la licence, trois ans après le baccalauréat ; le mastère, deux ans
    après la licence ; le doctorat, trois ans après le mastère. Les études d'ingénieur,
    d'architecture, de médecine, de pharmacie, de médecine dentaire et vétérinaire suivent leurs
    propres règles.
  - **Gratuité.** « L'enseignement supérieur public est gratuit. Les établissements… sont autorisés
    à percevoir des étudiants des droits d'inscription selon des conditions fixées par décret »
    (art. 7).
  - **Accès** : baccalauréat ou diplôme étranger équivalent (art. 6).
- **Transition et abrogation.**
  - Les délais du passage au régime de l'art. 3 sont fixés par décret (art. 56, al. 1er) ; ce décret
    n'est pas identifié (fiche `r-loi2008-19-art56-delais-lmd`).
  - Le régime des études de la loi n° 89-70 « prend fin à la fin de l'année universitaire
    2011-2012 » (art. 56, al. 2).
  - L'art. 58 abroge la loi n° 89-70 et la loi n° 2000-67, sous réserve de l'art. 56 et de la loi
    n° 90-72.
- **Date d'effet** : aucune clause générale. Exécutoire au plus tôt le 9 mars 2008.
- **Modifications** :
  - décret-loi n° 2011-31 du 26 avril 2011 (JORT n° 30 du 29 avril 2011, p. 571-572, **lu**).
    Présidents d'université, vice-présidents, doyens et directeurs sont désormais **élus**
    (art. 15, 19 et 25 nouveaux). <https://www.pist.tn/jort/2011/2011F/Jo0302011.pdf>. Exécutoire
    au plus tôt le 4 mai 2011 ;
  - loi n° 2017-38 du 2 mai 2017 (JORT n° 37 du 9 mai 2017, p. 1688, **lu**). Elle ajoute le
    « bachelor en administration des affaires » aux études à régime propre (art. 3, al. 2), avec
    effet « à compter de l'année universitaire 2010-2011 » (art. 2).
    <https://www.pist.tn/jort/2017/2017F/Jo0372017.pdf>.

### 1.9 Décret n° 2008-3123 du 22 septembre 2008 (licence) — **lu** (intitulé, visas, art. 1er à 3, 40 à 45)

- **Fascicule** : JORT n° 79 du 30 septembre 2008, p. 3093-3098.
  <https://www.pist.tn/jort/2008/2008F/Jo0792008.pdf>. Index : recid 82489.
- **Le rattachement au LMD est dans le texte même** :
  - l'intitulé finit par « …mentions, parcours et spécialités du système "LMD" » ;
  - art. 2 : « Le diplôme national de licence est soumis aux principes généraux relatifs à
    l'adoption du système de licence, mastère et doctorat "LMD" » ;
  - art. 3 : les objectifs du système, dont une meilleure lisibilité des niveaux, un système
    « comparable aux systèmes internationaux répandus », la mobilité et l'équivalence des diplômes.
- **Visas utiles à la chronologie** :
  - décret n° 93-2333 du 22 novembre 1993 (premier cycle et maîtrise, ancien régime) ;
  - décret n° 2004-2721 du 21 décembre 2004 (licence appliquée) ;
  - décret n° 95-1419 du 31 juillet 1995 (contribution financière des étudiants à la vie
    universitaire).
- **Dates.**
  - « Les dispositions du présent décret entrent en vigueur à partir de l'année universitaire
    2006-2007 » (art. 43). C'est une clause d'effet **antérieure** à la signature, que la première
    rentrée en licence LMD paraît suivre. Le texte qui organisait cette rentrée avant le décret
    reste à identifier.
  - L'ancien régime s'applique aux inscrits « jusqu'à la fin de leurs études et dans tous les cas,
    jusqu'à la fin de l'année universitaire 2011-2012 » (art. 41). La date coïncide avec
    l'art. 56 de la loi n° 2008-19.
  - Le décret n° 93-2333 est abrogé « progressivement » (art. 44).

### 1.10 Le Conseil supérieur : de 1958 à 2025

**La filiation, telle qu'on la lit dans les textes eux-mêmes.**

| Date | Texte | Organe | État |
|---|---|---|---|
| 1958 | Loi n° 58-118, art. 38 (p. 1059) | Conseil supérieur de l'éducation nationale, auprès du secrétariat d'État, sous sa présidence | lu |
| 1962 | Décret n° 62-403 du 21 décembre 1962, « relatif au conseil supérieur de l'éducation nationale » (JORT 1962/063, p. 1613-1616 ; rectificatif, index : 1962/015 (sic ; vraisemblablement 1963), p. 372) | idem | index |
| 1989 | Décret n° 89-1295 du 31 août 1989 (JORT 1989/062, p. 1428-1429) | Conseil supérieur de l'éducation et de l'enseignement supérieur | index ; connu aussi par les visas du décret n° 2000-2260 |
| 1991 | Loi n° 91-65, art. 2 | Conseil supérieur de l'éducation, consulté sur les questions d'intérêt national | lu |
| 2000 | Décret n° 2000-2260 du 10 octobre 2000 | Conseil supérieur de l'éducation | lu |
| 2022 | Constitution, titre IX, art. 135 | Conseil supérieur de l'éducation et de l'enseignement | lu |
| 2023 | Loi n° 2023-13, loi de finances pour 2024, art. 15 | fonds dont l'ordonnateur est le « رئيس المجلس الأعلى للتربية » | lu |
| 2024 | Décret-loi n° 2024-2 du 16 septembre 2024 | organisation du Conseil supérieur de l'éducation et de l'enseignement | lu |
| 2025 | Décret n° 2025-246 du 8 mai 2025 | organisation administrative et financière | lu (visas, art. 1er à 7) |

**Décret n° 2000-2260 du 10 octobre 2000 — lu** (en entier, texte décodé).
- **Fascicule** : JORT n° 82 du 13 octobre 2000, p. 2463-2464. Pages du fichier 11-12 ; l'index ne
  donne que p. 2463. <https://www.pist.tn/jort/2000/2000F/Jo0822000.pdf>.
- **Visas** : loi n° 89-70 modifiée par la loi n° 97-21 ; loi n° 91-65, « notamment son article 2 » ;
  décret n° 89-1295.
- **Mission** (art. 2) : donner son avis sur l'organisation de la politique nationale d'éducation,
  sur l'adaptation de l'éducation aux besoins du développement, et sur « les actions de réformes à
  entreprendre à tous les niveaux ».
- **Composition** (art. 3) : présidé par le Premier ministre ; une trentaine de membres du
  gouvernement ; des représentants d'organisations et d'ordres nationaux ; huit membres choisis par
  le Premier ministre.
- **Fonctionnement.** Réunion au moins une fois par an (art. 4). Le secrétariat est tenu par le
  ministre de l'éducation ou par celui de l'enseignement supérieur, selon la question (art. 5).
- **Abrogation** : le décret n° 89-1295 (art. 6).
- **Date d'effet** : aucune clause. Exécutoire au plus tôt le 18 octobre 2000.

**Constitution de 2022 — lu** (art. 44, 135 et 142), au numéro spécial du JORT du 18 août 2022.
- **Fascicule** : édition arabe seulement, scan lu à l'image.
  <https://www.pist.tn/jort/2022/2022A/Ja0922022.pdf>, testée le 17 octobre (200, identique au
  corpus). Pas d'URL française : `Jo0922022.pdf` rend 404 (testé le 17 octobre : 404,
  289 octets).
- **Art. 135** (titre IX, « المجلس الأعلى للتربية والتعليم », p. 45 du numéro, page du fichier 47).
  « يتولى المجلس الأعلى للتربية والتعليم إبداء الرأي في الخطط الوطنية الكبرى في مجال التربية
  والتعليم والبحث العلمي والتكوين المهني وآفاق التشغيل. يضبط القانون تركيبة هذا المجلس واختصاصاته
  وطرق سيره. »
  Traduction de travail : le Conseil donne son avis sur les grands plans nationaux en matière
  d'éducation, d'enseignement, de recherche scientifique, de formation professionnelle et de
  perspectives d'emploi ; la loi fixe sa composition, ses attributions et son fonctionnement.
- **Art. 44** (p. 14 du numéro, page du fichier 16).
  « التعليم إلزامي إلى سن السادسة عشرة. تضمن الدولة الحق في التعليم العمومي المجاني بكامل
  مراحله… ».
  Traduction de travail : l'enseignement est obligatoire jusqu'à seize ans ; l'État garantit le
  droit à l'enseignement public gratuit à toutes ses étapes. La suite de l'article porte sur
  l'enracinement de la jeunesse dans son identité arabo-islamique, l'arabe et l'ouverture aux
  langues étrangères. La lettre du texte : l'enseignement public gratuit « à toutes ses étapes »
  (« بكامل مراحله ») ; l'art. 7 de la loi n° 2008-19 posait déjà la gratuité du supérieur public.
- **Entrée en vigueur** (art. 142, p. 47-48 du numéro). La Constitution entre en vigueur « à
  compter de la date de la proclamation par l'Instance supérieure indépendante pour les élections
  des résultats définitifs du référendum ». Cette proclamation est la décision n° 2022-22 du
  16 août 2022 (JORT n° 90). L'entrée en vigueur suppose aussi que le Président de la République
  ait scellé la Constitution, l'ait promulguée et en ait autorisé la publication en numéro spécial,
  ce qui est fait le 17 août 2022. Le rédacteur doit citer la clause, non un calcul.
- **Date officielle** (art. 141) : la Constitution porte la date du référendum, le 25 juillet 2022.
- **Projet.** Le même article figure, sous le numéro 135, dans le projet publié par le décret
  présidentiel n° 2022-578 (JORT n° 74 du 30 juin 2022, p. 2359, titre VIII). Le projet corrigé par
  le décret présidentiel n° 2022-607 (JORT n° 77 du 8 juillet 2022, p. 2425, titre IX) le porte
  aussi ; l'art. 44 du projet corrigé est à la p. 2414. La rédaction est inchangée de bout en bout.

**Décret-loi n° 2024-2 du 16 septembre 2024 relatif à l'organisation du Conseil supérieur de l'éducation et de l'enseignement — lu** (en entier ; fascicule identifié dans cette passe)
- **Fascicule** : JORT n° 113 du 17 septembre 2024, **édition arabe**, p. 4851-4852.
  <https://www.pist.tn/jort/2024/2024A/Ja1132024.pdf>, testée (200, identique au corpus).
  L'édition française `Jo1132024.pdf` rend **404**, et le corpus local n'en a pas : pas d'URL
  française.
- **Index** : le texte est **absent de `jort_cache`**. Le fascicule n° 113 y a 11 notices, mais pas
  celle-ci : c'est pourquoi le plan ne l'avait pas trouvé.
- **Visas** : délibération du Conseil des ministres ; information de la commission de l'éducation de
  l'Assemblée des représentants du peuple.
- **Statut.** « هيئة دستورية تتمتع بالشخصية القانونية والاستقلالية المالية » : instance
  constitutionnelle dotée de la personnalité juridique et de l'autonomie financière. Son siège est à
  Tunis ; son organisation administrative et financière est renvoyée à un décret (art. 2).
- **Présidence** (art. 3). Le ministre le plus âgé préside la séance inaugurale. Les ministres des
  secteurs suivants se relaient ensuite tous les six mois à la présidence du Conseil : éducation ;
  enseignement supérieur et recherche ; emploi et formation professionnelle ; famille, femme,
  enfance et personnes âgées ; jeunesse et sports ; affaires religieuses ; affaires culturelles.
- **Organes.**
  - Une instance supérieure : les ministres, sept experts nommés pour trois ans, les présidents
    des deux instances suivantes et un représentant syndical (art. 4).
  - Une instance d'experts : quatorze membres d'au moins quinze ans d'expérience, dont
    obligatoirement quatre inspecteurs pédagogiques retraités. Elle prépare études et propositions
    de réforme (art. 8 et 9).
  - Une instance d'évaluation : neuf membres d'au moins vingt ans d'expérience. Elle évalue plans,
    politiques et programmes (art. 10 et 11).
- **Attributions.**
  - Avis obligatoire sur toutes les questions de l'art. 135 de la Constitution (art. 12).
  - Avis sur les projets dans les soixante jours, trente en cas d'urgence (art. 13).
  - Rapport annuel au Président de la République, publié au JORT (art. 14).
- **Date d'effet** : aucune clause (art. 17 : publication). Exécutoire au plus tôt le 22 septembre
  2024.
- **Clé** : `decret2024-2` existe déjà dans la bibliographie pour un **autre** texte (un décret du
  4 janvier 2024 sur la rémunération). Il faut une clé distincte, par exemple `decret-loi2024-2`.

**Décret n° 2025-246 du 8 mai 2025 — lu** (le plan le donnait déjà au niveau lu ; relu ici dans sa
version arabe du miroir iort).
- **Fascicule** : JORT n° 54 du 9 mai 2025, p. 1222.
- **Contenu** : secrétaire général (art. 1er), président ordonnateur (art. 3), ressources sur crédits
  de l'État (art. 4), comptable public (art. 6).
- **Date d'effet** : exécutoire au plus tôt le 14 mai 2025.

### 1.11 Après 2011 : textes d'organisation et de réforme repérés

Recherche faite sur les titres de `jort_cache` par LIKE, en arabe et en français (termes en § 6),
pour 2011-2026.

| Texte | Fascicule | État | Ce qu'il fait |
|---|---|---|---|
| Décret-loi n° 2011-31 du 26 avril 2011 | 2011/030, p. 571-572 | lu | élection des présidents d'université, des doyens et des directeurs (§ 1.8) |
| Décret-loi n° 2011-46 du 25 mai 2011, centre national des technologies en éducation | 2011/039, p. 808-809 | index | — |
| Décret n° 2012-827 du 11 juillet 2012, modifiant le décret n° 2004-2437 sur l'organisation de la vie scolaire | 2012/057, p. 1699-1700 | index | — |
| Décret gouvernemental n° 2016-1100 du 25 août 2016, unité de gestion par objectifs du projet de réforme de l'enseignement supérieur (prorogée par le décret n° 2023-12) | 2016/070 ; 2023/009 | index | — |
| **Loi n° 2017-13 du 13 mars 2017** relative aux mesures spécifiques pour la consécration de l'obligation d'accès à la formation professionnelle initiale | 2017/022, p. 1012 | **lu** | voir ci-dessous |
| Loi n° 2017-38 du 2 mai 2017 | 2017/037, p. 1688 | lu | bachelor (§ 1.8) |
| Décret gouvernemental n° 2019-656 du 29 juillet 2019 (admission aux lycées pilotes) ; arrêtés du 29 juillet 2019 (concours et régime des collèges et lycées pilotes) | 2019/063, p. 2458-2462 | index | — |
| Décret gouvernemental n° 2019-898 du 16 octobre 2019, modifiant le décret n° 2010-1928 du 6 août 2010 sur les droits d'inscription aux écoles primaires et aux collèges et lycées | 2019/085 ; 2010/065, p. 2247 | index | les droits d'inscription de l'art. 36 de la loi de 2002 |
| Décret gouvernemental n° 2019-1085 du 19 novembre 2019, horaire des études dans la base et le secondaire (modifié par le n° 2021-143) | 2019/095, p. 4040-4060 | index | — |
| Décret gouvernemental n° 2021-57 du 13 janvier 2021, établissement public « École de la deuxième chance » (complété par le décret n° 2022-932) | 2021/007, p. 137-141 | index | — |
| Constitution de 2022, art. 44 et 135 | numéro spécial | lu | § 1.10 |
| **Loi n° 2023-13 du 11 décembre 2023, loi de finances pour 2024, art. 15** | 2023/144, p. 6439, arabe seulement | **lu** | voir ci-dessous |
| Décret-loi n° 2024-2 | 2024/113, arabe | lu | § 1.10 |
| Décret n° 2025-21 du 8 janvier 2025, intégration des maîtres et professeurs suppléants | 2025/003, p. 78 | index | — |
| **Loi n° 2025-17 du 12 décembre 2025, loi de finances pour 2026, art. 107** | 2025/148, p. 4258, arabe | **lu** | voir ci-dessous |

**Loi n° 2017-13 — lu.** <https://www.pist.tn/jort/2017/2017F/Jo0222017.pdf>. Travaux
préparatoires : séance de l'Assemblée des représentants du peuple du 28 février 2017.
- **Obligation** (art. 1er). Sous réserve de l'obligation de base de la loi n° 2002-80, « la
  formation professionnelle initiale est obligatoire jusqu'à l'âge de dix-huit ans pour chaque
  personne qui ne s'est pas insérée dans la vie professionnelle, sauf si elle poursuit sa scolarité
  dans l'enseignement de base ou l'enseignement secondaire ».
- **Gratuité et cycle préparatoire** (art. 2). L'État en garantit la gratuité. Il ouvre un droit à
  un cycle préparatoire jusqu'à seize ans et, de seize à dix-huit ans, à une formation de niveau
  certificat de compétence ou des premier et deuxième cycles de la loi n° 2008-10.
- **Amende** (art. 3). Le tuteur dûment informé qui n'inscrit pas son pupille encourt une amende de
  **20 à 200 dinars**, portée à **400 dinars** en cas de récidive : le même barème que l'art. 21 de
  la loi de 2002.
- **Application** : par arrêté conjoint de quatre ministres (art. 4), non identifié (fiche
  `r-loi2017-13-art4-arrete`).
- **Date d'effet** : aucune clause. Exécutoire au plus tôt le 22 mars 2017.

C'est, après 2011, la seule extension de l'obligation trouvée : elle porte jusqu'à dix-huit ans
pour la formation, sans toucher l'obligation scolaire.

**Loi de finances pour 2024, art. 15 — lu** (édition arabe ;
<https://www.pist.tn/jort/2023/2023A/Ja1442023.pdf>, testée ; pas d'édition française,
`outillage-sources.md` § 3).
- Il crée un **fonds national de la réforme éducative** (« صندوق وطني للإصلاح التربوي »).
- **Ressources** : dons des Tunisiens ; 0,5 % des bénéfices des établissements éducatifs privés
  (écoles, instituts, facultés, centres de formation) ; 0,25 % des bénéfices des sociétés
  pétrolières, des assurances, des banques, des grandes surfaces et des pharmacies.
- **Emplois** : diagnostic du système éducatif ; ingénierie de programmes alternatifs ; préparation
  des espaces éducatifs.
- **Ordonnateur** : le président du Conseil supérieur de l'éducation ; à titre provisoire, le
  ministre de l'éducation jusqu'à la nomination de ce président.
- L'article d'effet propre de la loi de finances n'a pas été relu.

**Loi de finances pour 2026, art. 107 — lu** (édition arabe, p. 4258 ;
<https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf>, testée ; le fichier « fr » du n° 148 de 2025
est l'arabe, `outillage-sources.md` § 3). Son libellé entier : « تسوية وضعية المعلمين والأساتذة
النواب المباشرين بالتدريس في المؤسسات التربوية قبل 2008 و2006 وإدماجهم بوزارة التربية ».
Traduction de travail : régularisation de la situation des instituteurs et professeurs suppléants
en fonction dans les établissements éducatifs avant 2008 et 2006, et leur intégration au ministère
de l'éducation. L'article ne dit rien de plus ; il relève du chapitre 6 (personnels). L'article
d'effet de la loi de finances n'a pas été relu.

**Consultations nationales sur la réforme.** Aucun texte au *Journal officiel* n'est identifié pour
la consultation sur la réforme de l'éducation, par les termes de § 6 (fiche
`r-education-consultation-reforme`). Les consultations ont pu être organisées hors JORT ; leurs
rapports relèvent des documents à obtenir.

---

## 2. Tableau court : une ligne par grande réforme

« Date d'effet » : clause du texte quand elle existe (*), sinon date exécutoire, « au plus tôt »
après 1993. « Portée » : proposition du documentaliste, à trancher par l'architecte (Q2 du plan).

| Date d'effet | Texte | Ce que la loi cherche (ses mots) | Ce qui change pour l'élève | Portée proposée |
|---|---|---|---|---|
| 1er octobre 1958 * | Loi n° 58-118, art. 60 | permettre « à tous les enfants des deux sexes, sans distinction d'ordre racial, religieux ou social, le développement de leur personnalité » ; « former les cadres nécessaires » (art. 1er) | accès dès six ans ; gratuité à tous les degrés ; primaire 6 ans, moyen 3 ans, secondaire 6 ans ; obligation de 6 à 12 ans **annoncée, non imposée** (art. 2) | rupture |
| 6 août 1989 | Loi n° 89-70 | « contribuer au développement de la nation » ; « favoriser l'arabisation » (art. 1er rectifié) | supérieur : universités, aide de l'État (bourse, prêt, exemption), frais d'inscription pour les étudiants qui disposent de ressources | étape |
| 8 août 1991 ; base appliquée année par année depuis 1989-1990 * | Loi n° 91-65 | finalités « dans le cadre de l'identité nationale tunisienne et de l'appartenance à la civilisation arabo-musulmane » (art. 1er) | **obligation de 6 à 16 ans** ; école de base de 9 ans (6 + 3) ; matières enseignées en arabe ; amende de 10 à 100 dinars (200 en récidive) ; secondaire de 4 ans (2 + 2) | rupture |
| au plus tôt 4 août 2002 ; secondaire à la rentrée 2003-2004 * | Loi d'orientation n° 2002-80 | « L'éducation est une priorité nationale absolue » ; « L'élève est au centre de l'action éducative » (art. 1er et 2) | obligation 6-16 confirmée ; année préparatoire rattachée à la base, mais hors gratuité et hors obligation (art. 18) ; deux langues étrangères ; examen de fin de base facultatif ; amende de 20 à 200 dinars (400) | rupture ou étape (Q2) |
| au plus tôt 20 février 2008 | Loi n° 2008-9 | — (loi modificative) | langues étrangères permises dans tous les cycles ; collèges pilotes et concours d'accès ; diplôme de fin de base général ou technique | ajustement |
| au plus tôt 20 février 2008 | Loi n° 2008-10 | « l'un des leviers du développement » (art. 1er) | trois cycles de formation initiale (CAP, BTP ou baccalauréat professionnel, BTS) ; passerelles avec le secondaire ; apprentissage de 15 à 20 ans | étape (remplace la loi n° 93-10) |
| au plus tôt 9 mars 2008 ; licence LMD dès 2006-2007 * ; ancien régime jusqu'à fin 2011-2012 * | Loi n° 2008-19 ; décret n° 2008-3123 | « édifier la société du savoir » ; « renforcer l'employabilité des diplômés » (art. 1er et 2) | licence (3 ans), mastère (2), doctorat (3) ; supérieur public gratuit, avec droits d'inscription par décret | rupture pour le supérieur |
| au plus tôt 22 mars 2017 | Loi n° 2017-13 | « consécration de l'obligation d'accès à la formation professionnelle initiale » (intitulé) | formation initiale obligatoire et gratuite jusqu'à 18 ans hors scolarité ; amende du tuteur | étape |
| à la proclamation des résultats du référendum (art. 142) | Constitution de 2022, art. 44 et 135 | grands plans nationaux d'éducation (art. 135) | obligation jusqu'à 16 ans et gratuité de l'enseignement public à toutes ses étapes, élevées au rang constitutionnel | étape |
| au plus tôt 22 septembre 2024 | Décret-loi n° 2024-2 ; décret n° 2025-246 | — | institution, non droit de l'élève : Conseil supérieur de l'éducation et de l'enseignement, instance constitutionnelle | étape |

---

## 3. Séries d'effectifs, pour situer les réformes

Deux familles, qui ne se mêlent pas : la statistique nationale (INS, qui relaie les ministères) et
un rapport extérieur (UNESCO-UIS, par la Banque mondiale). Les **périmètres diffèrent** :
- le « primaire » de l'UIS coïncide avec le premier cycle de la base de l'INS ;
- le « secondaire » de l'UIS ne coïncide pas avec le « 2e cycle de la base et secondaire » de l'INS :
  812 069 pour l'INS en 1995-96, 849 359 pour l'UIS en 1996.

Correspondance des années, vérifiée sur les valeurs : l'année N de l'UIS est l'année scolaire
(N-1)-N de l'INS. Les deux donnent 1 468 998 au primaire pour 1996 et 1995-96, et 112 634 au
supérieur.

### 3.1 INS, *Annuaire statistique de la Tunisie*, tableau « Données générales » de l'enseignement

**Source** : fichiers `~/projets/tunisia-data/data/raw/ins-publications/annuaire-statistique/<édition>.pdf`,
fiche `sources/ins-annuaires-statistiques.md`, déjà dans l'entrepôt. Les annuaires citent eux-mêmes
le ministère de l'Éducation et celui de l'Enseignement supérieur.

| Édition | Années scolaires couvertes ici | Page | Page du fichier |
|---|---|---|---|
| 1995-2001 | 1995-96 à 2001-02 | 53 | 45 |
| 2001-2005 | 2002-03 à 2005-06 | 57 | 51 |
| 2006-2010 | 2006-07 à 2010-11 | 47 | 47 |
| 2008-2012 | 2011-12 | 49 | 49 |
| 2012-2016 | 2012-13 à 2016-17 | 43 | 43 |
| 2015-2019 | 2017-18, 2018-19 | à relever | 43 |
| 2019-2023 | 2019-20 à 2023-24 | 43 | 43 |

Effectifs totaux, public et privé. Le 2e cycle comprend les écoles de qualification technique.

| Année scolaire | 1er cycle de la base | 2e cycle de la base et secondaire | Supérieur |
|---|---:|---:|---:|
| 1995-96 | 1 468 998 | 812 069 | 112 634 |
| 1996-97 | 1 450 916 | 882 730 | 121 787 |
| 1997-98 | 1 450 164 | 918 857 | 137 024 |
| 1998-99 | 1 442 904 | 953 683 | 155 120 |
| 1999-00 | 1 440 795 (a) | 983 368 | 180 044 |
| 2000-01 | 1 373 904 | 1 033 154 | 207 388 |
| 2001-02 | 1 325 707 | 1 092 699 | 226 102 |
| 2002-03 | 1 277 124 | 1 118 810 | 262 502 |
| 2003-04 | 1 228 347 | 1 139 009 | 291 842 |
| 2004-05 | 1 184 301 | 1 152 625 | 311 569 |
| 2005-06 | 1 134 414 | 1 150 257 | 321 838 |
| 2006-07 | 1 068 822 | 1 163 827 | 326 185 (b) |
| 2007-08 | 1 036 445 | 1 143 758 | 335 649 |
| 2008-09 | 1 025 044 | 1 079 621 | 349 142 |
| 2009-10 | 1 030 109 | 1 042 852 | 346 079 |
| 2010-11 | 1 027 970 | 1 008 127 | 336 017 |
| 2011-12 | 1 043 711 | 994 773 | 330 541 |
| 2012-13 | 1 063 291 | 985 248 | 304 365 |
| 2013-14 | 1 089 220 | 970 133 | 293 982 |
| 2014-15 | 1 114 883 | 958 093 | 282 819 |
| 2015-16 | 1 139 314 | 964 346 | 255 783 |
| 2016-17 | 1 170 470 | 962 630 | 243 292 |
| 2017-18 | 1 201 736 | 972 460 | 235 102 |
| 2018-19 | 1 239 539 | 990 531 | 233 534 |
| 2019-20 | 1 269 412 | 1 024 941 | 232 989 |
| 2020-21 | 1 303 758 | 1 072 483 | 232 614 |
| 2021-22 | 1 321 163 | 1 090 896 | 256 564 |
| 2022-23 | 1 337 527 | 1 125 137 | 260 647 |
| 2023-24 | 1 334 153 | 1 155 186 | 266 837 |

(a) **Total incohérent dans la source.** L'édition 1995-2001 imprime 1 440 795, alors que ses
propres lignes public (1 403 729) et privé (10 066) font 1 413 795. L'UIS donne 1 413 795 pour 2000.
La valeur 1 413 795 est probablement la bonne, mais aucune autre édition de l'INS ne l'atteste ici.

(b) **Rupture de définition.** À partir de l'édition 2006-2010, la ligne devient « étudiants
réguliers », contre « étudiants » auparavant. Il n'y a pas d'année de recouvrement dans les éditions
lues.

Révisions entre éditions : l'effectif des enseignants du supérieur public de 2019-20 vaut 22 072
dans l'édition 2015-2019 et 22 086 dans l'édition 2019-2023. Les effectifs d'élèves des années
communes à deux éditions lues (2001-02 ; 2008-09, 2009-10, 2010-11 ; 2012-13 ; 2015-16, 2016-17 ;
2019-20) sont identiques d'une édition à l'autre.

Repères pour situer les réformes :
- le 1er cycle culmine vers 1995-96 puis baisse jusqu'en 2008-09, effet de la démographie ;
- le 2e cycle et le secondaire croissent de 812 069 à 1 163 827 entre 1995-96 et 2006-07, à mesure
  que l'école de base de 1991 produit ses cohortes et que l'obligation à seize ans joue ;
- le supérieur triple de 1995-96 à 2008-09, puis recule jusqu'en 2020-21.

### 3.2 Rapport extérieur : UNESCO-UIS, par l'API de la Banque mondiale (WDI)

**Méthode.** Indicateurs `SE.PRM.ENRL` (« Primary education, pupils », public et privé),
`SE.SEC.ENRL` (secondaire) et `SE.TER.ENRL` (supérieur, tous programmes). Source déclarée par la
Banque mondiale : UIS (données publiées en février 2026, consultées le 19 mars 2026). Mises à jour
WDI : 8 octobre 2026 pour les deux premières séries, 25 juin 2024 pour la troisième.

**Téléchargement** du 17 octobre 2026 dans `/tmp/education-ocr-C/wb/`, **non versé à
`tunisia-data`**. À verser sous `data/raw/banque-mondiale/`, avec ces empreintes SHA-256 :
- `SE.PRM.ENRL.json` 0114eff0ade7eb9cb17080a6605e672cebadab349dbea0bbd7c5755614d798ec ;
- `SE.SEC.ENRL.json` e943eca85903f4a5a0d32838df691b93eaea3dbff7e3fa7fabbd1d45a845d293 ;
- `SE.TER.ENRL.json` 93d3ca9798112819e38f57e8cb4a26289490c34e06ead79033060d76e3301c97.

Adresse : `https://api.worldbank.org/v2/country/TUN/indicator/<code>?format=json&per_page=100&date=1960:2024`.

**Couverture** : de 1971 à 2023 pour le primaire, à 2016 pour le secondaire, à 2019 pour le
supérieur. Rien avant 1971.

| Année (UIS) | Primaire | Secondaire (périmètre UIS) | Supérieur |
|---|---:|---:|---:|
| 1971 | 935 738 | 191 445 | 10 347 |
| 1976 | 932 787 | 201 845 | 20 505 |
| 1981 | 1 054 027 | 275 696 | 31 827 |
| 1986 | 1 291 490 | 457 630 | 41 594 |
| 1989 | 1 333 490 | 530 004 | 54 466 |
| 1991 | 1 405 665 | 564 540 | 68 535 |
| 1996 | 1 468 998 | 849 359 | 112 634 |
| 2002 | 1 325 707 | 1 169 368 | 226 632 |
| 2003 | 1 277 124 | 1 158 972 | 272 316 |
| 2008 | 1 036 445 | 1 259 240 | 356 851 |
| 2009 | 1 025 044 | 1 201 632 | 369 064 |
| 2016 | 1 139 314 | 1 047 035 | 294 486 |
| 2019 | — | — | 267 154 |
| 2023 | 1 337 527 | — | — |

Le supérieur de l'UIS diffère légèrement de l'INS (226 632 contre 226 102 pour 2001-02). Le
secondaire de l'UIS est plus large que la ligne de l'INS, sans que la source dise de combien.
Méthode de l'UIS non relue : à documenter avant tout graphique superposé.

---

## 4. Références candidates

### 4.1 Déjà présentes dans une bibliographie du précis

- `constitution2022` (`precis/fr/finances_locales/references.json`). Sa note énumère les articles
  lus ; y ajouter les art. 44, 135 et 142, lus ici aux p. 14, 45 et 47-48 du numéro spécial.
- `decret-pres2022-691`, `loi93-64`.
- **Attention** : `decret2024-2` désigne un autre texte (le décret du 4 janvier 2024 sur la
  rémunération). Le décret-loi du 16 septembre 2024 demande une clé nouvelle.

### 4.2 À créer (CSL-JSON, type `legislation`, `container-title` « Journal officiel de la République tunisienne »)

| citation-key suggérée | Titre | Date | Fascicule, page | URL |
|---|---|---|---|---|
| `loi58-118` | Loi n° 58-118 du 4 novembre 1958 relative à l'enseignement | 1958-11-04 | n° 89 du 7 novembre 1958, p. 1056-1060 | https://www.pist.tn/jort/1958/1958F/Jo08958.pdf |
| `loi89-70` | Loi n° 89-70 du 28 juillet 1989 relative à l'enseignement supérieur et à la recherche scientifique | 1989-07-28 | n° 54 des 4 et 8 août 1989, p. 1169-1172 | https://www.pist.tn/jort/1989/1989F/Jo05489.pdf |
| `loi89-70-rectificatif` | Rectificatif à la loi n° 89-70 | — | n° 61 du 12 septembre 1989, p. 1392 | https://www.pist.tn/jort/1989/1989F/Jo06189.pdf |
| `loi91-65` | Loi n° 91-65 du 29 juillet 1991 relative au système éducatif | 1991-07-29 | n° 55 du 6 août 1991, p. 1398-1400 | https://www.pist.tn/jort/1991/1991F/Jo05591.pdf |
| `decret2000-2260` | Décret n° 2000-2260 du 10 octobre 2000, fixant les attributions, la composition et le fonctionnement du conseil supérieur de l'éducation | 2000-10-10 | n° 82 du 13 octobre 2000, p. 2463-2464 | https://www.pist.tn/jort/2000/2000F/Jo0822000.pdf |
| `loi2002-5` | Loi n° 2002-5 du 21 janvier 2002, modifiant la loi n° 91-65 | 2002-01-21 | n° 7 du 22 janvier 2002, p. 131 | https://www.pist.tn/jort/2002/2002F/Jo0072002.pdf |
| `loi2002-80` | Loi d'orientation n° 2002-80 du 23 juillet 2002, relative à l'éducation et à l'enseignement scolaire | 2002-07-23 | n° 62 du 30 juillet 2002, p. 1735-1740 ; rectificatif n° 69 du 23 août 2002, p. 1991 | https://www.pist.tn/jort/2002/2002F/Jo0622002.pdf |
| `loi2008-9` | Loi n° 2008-9 du 11 février 2008, modifiant et complétant la loi d'orientation n° 2002-80 | 2008-02-11 | n° 14 du 15 février 2008, p. 681-683 | https://www.pist.tn/jort/2008/2008F/Jo0142008.pdf |
| `loi2008-10` | Loi n° 2008-10 du 11 février 2008, relative à la formation professionnelle | 2008-02-11 | n° 14 du 15 février 2008, p. 683-688 | idem |
| `loi2008-19` | Loi n° 2008-19 du 25 février 2008, relative à l'enseignement supérieur | 2008-02-25 | n° 19 du 4 mars 2008, p. 844-850 | https://www.pist.tn/jort/2008/2008F/Jo0192008.pdf |
| `decret2008-3123` | Décret n° 2008-3123 du 22 septembre 2008, fixant le cadre général du régime des études et les conditions d'obtention du diplôme national de licence… du système « LMD » | 2008-09-22 | n° 79 du 30 septembre 2008, p. 3093-3098 | https://www.pist.tn/jort/2008/2008F/Jo0792008.pdf |
| `decret-loi2011-31` | Décret-loi n° 2011-31 du 26 avril 2011, modifiant la loi n° 2008-19 | 2011-04-26 | n° 30 du 29 avril 2011, p. 571-572 | https://www.pist.tn/jort/2011/2011F/Jo0302011.pdf |
| `loi2017-13` | Loi n° 2017-13 du 13 mars 2017, relative aux mesures spécifiques pour la consécration de l'obligation d'accès à la formation professionnelle initiale | 2017-03-13 | n° 22 du 17 mars 2017, p. 1012 | https://www.pist.tn/jort/2017/2017F/Jo0222017.pdf |
| `loi2017-38` | Loi n° 2017-38 du 2 mai 2017, portant modification de la loi n° 2008-19 | 2017-05-02 | n° 37 du 9 mai 2017, p. 1688 | https://www.pist.tn/jort/2017/2017F/Jo0372017.pdf |
| `loi2023-13-lf2024` | Loi n° 2023-13 du 11 décembre 2023, portant loi de finances pour l'année 2024 (art. 15) | 2023-12-11 | n° 144 du 12 décembre 2023, p. 6439, arabe | https://www.pist.tn/jort/2023/2023A/Ja1442023.pdf (pas d'URL française) |
| `decret-loi2024-2` | مرسوم عدد 2 لسنة 2024 مؤرخ في 16 سبتمبر 2024 يتعلق بتنظيم المجلس الأعلى للتربية والتعليم (Décret-loi n° 2024-2 du 16 septembre 2024, relatif à l'organisation du Conseil supérieur de l'éducation et de l'enseignement ; traduction de travail) | 2024-09-16 | n° 113 du 17 septembre 2024, p. 4851-4852, arabe | https://www.pist.tn/jort/2024/2024A/Ja1132024.pdf (pas d'URL française : 404) |
| `decret2025-246` | Décret n° 2025-246 du 8 mai 2025, fixant l'organisation administrative et financière du Conseil supérieur de l'éducation et de l'enseignement | 2025-05-08 | n° 54 du 9 mai 2025, p. 1222 | https://www.pist.tn/jort/2025/2025F/Jo0542025.pdf |
| `loi2025-17-lf2026` | Loi n° 2025-17 du 12 décembre 2025, portant loi de finances pour l'année 2026 (art. 107) | 2025-12-12 | n° 148 du 12 décembre 2025, p. 4258, arabe | https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf |

Le décret n° 2025-246 n'a pas été relu au fascicule dans cette passe, mais dans la version du miroir
iort. Son adresse française a été testée le 17 octobre : 200, identique au corpus, fascicule bien en
français. La note du plan, § 8.1, le donne lu à la p. 1222.

### 4.3 Études d'histoire de l'éducation (candidates ; aucune récupérée en PDF)

| Référence | Vérification | Lu | PDF |
|---|---|---|---|
| Akkari, Abdeljalil (2005). « The Tunisian Educational Reform: From Quantity to Quality and the Need for Monitoring and Assessment ». *Prospects*, 35, p. 59-74. DOI 10.1007/s11125-005-6818-8 | notice Springer | résumé seulement | à récupérer |
| Sraïeb, Noureddine (1995). *Enseignement et nationalisme : le collège Sadiki de Tunis (1875-1956)*. CNRS Éditions et Alif-Les Éditions de la Méditerranée | une seule notice, nécrologique (insaniyat.crasc.dz) | non | à récupérer ; notice de catalogue à trouver |
| Sraïeb, Noureddine (1974). *Colonisation, décolonisation et enseignement : l'exemple tunisien*. Thèse de troisième cycle publiée à Tunis | même notice unique | non | éditeur **à vérifier** (aucune notice de catalogue trouvée) |
| Sraïeb, Noureddine. « Enseignement, décolonisation et développement au Maghreb », chapitre VI, p. 131-153, dans un ouvrage de l'IREMAM sur OpenEdition (books.openedition.org/iremam/123) | page OpenEdition | non | ouvrage et année à relever |
| Siino, François (2004). *Science et pouvoir dans la Tunisie contemporaine*. Paris, Karthala et IREMAM, 405 p. | notices DOAB et REMMM | non | en libre accès selon DOAB ; périphérique au chapitre (supérieur et recherche) |
| UNESCO, Bureau international d'éducation, *Données mondiales de l'éducation* : Tunisie (webarchive.unesco.org, `ibe.unesco.org/sites/default/files/Tunisia.pdf`) | adresse d'archive vue en recherche | non | à récupérer ; édition et année à relever |
| *Nouvelle réforme du système éducatif tunisien* (Planipolis, IIEP-UNESCO) | adresse d'archive vue en recherche | non | à récupérer ; auteur, ministère et année à relever |

Une source secondaire, de l'université de Genève (emf.unige.ch), compte « cinq grandes réformes »
en 1958, 1968, 1978, 1993 et 2002. Aucune loi de 1968 ou de 1978 n'apparaît à l'index sur les termes
d'organisation de l'enseignement (§ 6). Ces dates n'entrent pas dans le tableau tant qu'aucun texte
n'est lu ; elles sont en lacune.

---

## 5. Notions à glossaire

Aucune n'est présente dans `precis/glossaire.yml` (vérifié le 17 octobre). Source canonique
pressentie entre parenthèses ; termes arabes à prendre au texte arabe de la source canonique.

- **Enseignement de base** — التعليم الأساسي (loi n° 91-65, art. 6-8 ; loi n° 2002-80, art. 19-22).
- **Cycle primaire** et **cycle préparatoire** (second cycle de la base) — المرحلة الابتدائية،
  المرحلة الإعدادية (loi n° 2002-80, art. 22). Le cycle préparatoire est à distinguer de l'année
  préparatoire.
- **Année préparatoire** — السنة التحضيرية (loi n° 2002-80, art. 16-18).
- **Éducation préscolaire** — التربية قبل المدرسية (loi n° 2002-80, art. 16).
- **École préparatoire, collège** (loi n° 91-65, art. 21 ; loi n° 2002-80, art. 30) ; **collège
  pilote**, **lycée pilote** (loi n° 2008-9).
- **Enseignement moyen**, **brevet d'enseignement moyen** (loi n° 58-118, art. 10-13 ; pour
  l'histoire).
- **Diplôme de fin de l'enseignement de base** (loi n° 91-65, art. 10 ; loi n° 2002-5 ; loi
  n° 2008-9, art. 61 nouveau).
- **Obligation scolaire** — إجبارية التعليم (loi n° 91-65, art. 7 ; loi n° 2002-80, art. 1er ;
  Constitution, art. 44).
- **Gratuité de l'enseignement** — مجانية التعليم (loi n° 2002-80, art. 4 ; loi n° 2008-19, art. 7 ;
  Constitution, art. 44).
- **Tuteur** (au sens de l'amende scolaire) — الولي (loi n° 2002-80, art. 21).
- **Conseil supérieur de l'éducation et de l'enseignement** — المجلس الأعلى للتربية والتعليم
  (Constitution, art. 135 ; décret-loi n° 2024-2). À distinguer du **Conseil supérieur de
  l'éducation** de 2000 et du **Conseil supérieur de l'éducation nationale** de 1958.
- **Licence, mastère, doctorat (LMD)** (loi n° 2008-19, art. 3 ; décret n° 2008-3123, art. 2).
- **Certificat d'aptitude professionnelle**, **brevet de technicien professionnel**,
  **baccalauréat professionnel**, **brevet de technicien supérieur**, **certificat de compétence**
  (loi n° 2008-10, art. 9 et 13).
- **Formation en alternance**, **apprentissage** (loi n° 2008-10, art. 15-19). « Apprentissage »
  est peut-être à rapprocher de l'entrée existante « Fonds de promotion de la formation
  professionnelle et de l'apprentissage ».
- **Formation professionnelle initiale** — التكوين المهني الأساسي (loi n° 2017-13).
- **Fonds national de la réforme éducative** — الصندوق الوطني للإصلاح التربوي (loi de finances
  pour 2024, art. 15).

---

## 6. Lacunes, classées

### Lisible (dans le corpus, non lu ici)

- Loi n° 93-10 du 17 février 1993, loi d'orientation de la formation professionnelle : JORT 1993/014,
  p. 252-256. Elle est remplacée par la loi n° 2008-10.
- Loi n° 93-12 du 17 février 1993 (centre national de formation des formateurs) : JORT 1993/014,
  p. 257. Notice consultée ; texte non lu.
- Décret n° 92-1186 du 22 juin 1992 : la distance qui exempte de l'amende (JORT 1992/041, p. 816).
- Décrets n° 62-403 (Conseil supérieur de l'éducation nationale, JORT 1962/063) et n° 89-1295
  (JORT 1989/062).
- Décret n° 61-14 du 3 janvier 1961 relatif à l'enseignement primaire (JORT 1961/001, p. 22-24) ;
  décret n° 60-220 du 27 juin 1960 relatif aux établissements d'enseignement secondaire (JORT
  1960/031) ; décret n° 60-98 (université de Tunis).
- Lois n° 69-3, 76-65 et 86-80 (supérieur, abrogées en 1989) ; lois n° 97-21 et 2000-67
  (modifications de la loi n° 89-70).
- Décret n° 2010-1928 et décret gouvernemental n° 2019-898 : droits d'inscription scolaires.
- Décret n° 2004-2437 (vie scolaire) et décret n° 2012-827.
- Loi n° 2008-10 : art. 35 à 63 non lus.
- Loi n° 2008-19 : art. 10 à 55 non lus. Le décret des droits d'inscription de son art. 7 est à
  identifier.
- Articles d'effet des lois de finances pour 2024 et 2026.
- Le numéro de page imprimé de l'édition 2015-2019 de l'annuaire de l'INS.

### OCR nécessaire

- Aucune pour les textes de ce chapitre : les quatre fascicules sans couche texte ont été océrisés et
  lus à l'image.
- Les fascicules antérieurs à 1990 cités en « lisible » (1960, 1961, 1962, 1969, 1976, 1986) sont
  probablement des scans aussi : le même traitement est à prévoir.

### À obtenir (hors corpus ou hors JORT)

- Exposés des motifs et débats de la Chambre des députés. Les séances sont relevées : 26 juillet
  1989 ; 24 juillet 1991 ; 15 janvier et 19 juillet 2002 ; 29 janvier, 6 et 7 février, 14 février
  2008 ; 28 février 2017 (ARP).
- Effectifs scolarisés **avant 1971**, sur quelque série que ce soit, et **de l'INS avant 1995**.
  Annuaires statistiques anciens, statistiques scolaires du ministère.
- Méthode de l'UIS, pour comprendre l'écart de périmètre du secondaire.
- Texte annoncé par l'art. 2 de la loi de 1958, qui devait fixer la date de l'obligation de six à
  douze ans (fiche).
- Texte de généralisation de l'année préparatoire (fiche).
- Décret des délais de passage au LMD (fiche) ; texte qui organise la rentrée LMD de 2006-2007,
  avant le décret n° 2008-3123.
- Arrêté conjoint d'application de la loi n° 2017-13 (fiche).
- Textes ou rapports des consultations nationales sur la réforme de l'éducation après 2011 (fiche
  pour la partie JORT).
- Réformes de 1968 et de 1978 citées par une source secondaire : aucun texte identifié.
- Avant 1958 (écoles du Protectorat, Sadiki, Zitouna, kouttabs) : études à réunir (§ 4.3). Les
  visas de 1958 (décrets du 15 septembre 1888 et du 21 janvier 1920) donnent deux textes de départ.
- PDF de toutes les études du § 4.3.

---

## 7. Recherches infructueuses

Les fiches proposées sont dans `docs/notes/education-recherches-C.yml`, au schéma de
`docs/recherches.yml`, sans commentaire. Elles sont écrites à la main : `scripts/recherches.py` n'a
pas été lancé, pour ne pas réécrire le registre.

Les requêtes ont été lancées en SQL directement sur `jort_cache`, sorties lues en entier : LIKE sur `titre` et, pour
certaines, FTS sur `textes_fts`. Les accents et la casse n'ont pas été neutralisés à la main dans les
LIKE, qui sont écrits sans accents. Ni plein texte, ni miroir iort, ni relance par l'outil.
`relancer` doit rejouer chaque fiche avant toute conclusion.

| id | Objet | Résultat |
|---|---|---|
| `r-loi58-118-art2-obligation` | texte fixant la date d'entrée en vigueur de l'obligation de six à douze ans (loi n° 58-118, art. 2) | aucun ; période bornée par la loi n° 91-65 |
| `r-loi2002-80-art17-annee-preparatoire` | texte généralisant l'année préparatoire (loi n° 2002-80, art. 17) | aucun |
| `r-loi2008-19-art56-delais-lmd` | décret fixant les délais de passage au régime licence-mastère-doctorat (loi n° 2008-19, art. 56, al. 1er) | aucun ; la passe remonte en revanche les décrets n° 2012-1227 (mastère LMD, JORT 2012/066, p. 1948-1954) et n° 2013-47 (doctorat LMD, JORT 2013/004, p. 286-292), index, pour le chapitre 4 |
| `r-loi2017-13-art4-arrete` | arrêté conjoint d'application de la loi n° 2017-13 (art. 4) | aucun (l'arrêté du 23 novembre 2020, JORT 2020/118, porte sur la formation initiale à distance, non sur la loi de 2017) |
| `r-education-consultation-reforme` | texte publié au JORT organisant une consultation ou un dialogue national sur la réforme du système éducatif, 2011-2026 | aucun |

**Fiche résolue d'emblée, non proposée.** Le décret fixant la distance qui exempte le tuteur de
l'amende (loi n° 91-65, art. 32) est le décret n° 92-1186 (index), trouvé par la même passe.

**Pour l'agent qui fusionne.** Le champ `ou` des fiches pointe vers
`precis/fr/education/_histoire.qmd`, fichier pressenti par le plan et **non encore créé**. Aucune
ancre `<!-- RECHERCHE … -->` n'existe : `recherches.py verifier` signalera des fiches sans ancre tant
que le chapitre n'est pas écrit. Couverture de la passe jusqu'au 2 octobre 2026, dernière
publication indexée dans `jort_cache`.

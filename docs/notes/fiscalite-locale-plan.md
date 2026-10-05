# Volume VII « Les finances locales » : plan

**Option B retenue par l'humain le 4 octobre 2026** : un septième volume, distinct de « La
fiscalité ». Il traite ensemble la fiscalité locale, les transferts de l'État et les budgets des
collectivités, parce que ces trois éléments ne se comprennent que l'un par l'autre. Rien n'est
rédigé : ce plan cadre le travail. Aucune date, aucun texte, aucune valeur n'y est donné comme
établi ; ce qui est marqué « à établir » doit être lu au JORT ou dans une source vérifiée avant
d'entrer dans le précis.

## 1. Principes

- **Frontières avec les autres volumes.**
  - « La fiscalité » garde les impôts d'État ; l'impôt foncier de 2014, assis sur la TIB et la TNB,
    reste au chapitre de l'impôt sur la fortune, avec un renvoi croisé.
  - La TCL est assise sur le chiffre d'affaires : le volume renvoie au chapitre de l'IRPP et à celui
    de l'IS pour les assiettes communes.
  - Les rémunérations du personnel des collectivités relèvent, s'il y a lieu, du volume
    « Rémunérations dans le secteur public ».
- **Conventions des volumes** : chapitres à plat, numérotés par Quarto, sans partie ; l'introduction
  annonce les regroupements (`scripts/check_numerotation.py`). Plan type de chaque dispositif :
  origines → institution → réformes, une à une → longue période et données.
- **Termes** : les notions passent au glossaire bilingue ; termes arabes relevés dans l'édition arabe
  des textes (règle « impôt » de `docs/agents/terminologue.md` : l'impôt garde le nom de son texte).

## 2. Architecture : des notions au droit, puis aux chiffres

Demande de l'humain (4 octobre 2026) : **clarifier les concepts avant d'entrer dans le juridique et
le fiscal.** Le volume avance donc en quatre mouvements, annoncés par la présentation (pas de
`part:` : les chapitres restent à plat) :

1. **Les notions** — un chapitre d'économie et de droit public des finances locales, sans texte
   tunisien encore : de quoi parle-t-on quand on dit décentraliser, budget local, impôt local,
   transfert, péréquation, autonomie ? Chaque notion y est définie une fois, d'après la doctrine,
   et reçoit son entrée au glossaire ; les chapitres suivants y renvoient au lieu de redéfinir.
2. **Les institutions** — qui sont les collectivités, ce qu'elles font, comment elles budgètent :
   l'histoire, les compétences, les budgets.
3. **Les ressources** — ce qui les finance : leurs impôts, leurs taxes et redevances, puis les
   transferts de l'État.
4. **Les chiffres** — la longue période.

Chaque chapitre des mouvements 2 à 4 s'ouvre sur un court rappel des notions qu'il mobilise, avec
renvoi au chapitre 2, puis suit le plan type (origines → institution → réformes → longue période).

### 2.1 Le chapitre des notions (chapitre 2)

Toutes les définitions sont à **sourcer dans la doctrine** (Dafflon et Gilbert, AFD 2018, ch. 1 ;
Dafflon et Madiès, AFD, *Notes et documents* n° 42, 2008 ; manuscrit 2013, encadré 4-6 « Un peu de
terminologie » et § 5.1.4 « Définitions et critères ») ; pour chacune, le terme du droit tunisien
correspondant (FR et AR) est relevé dans les textes au chapitre où il apparaît.

| Section | Notions | Sert aux chapitres |
|---|---|---|
| Décentraliser | déconcentration et décentralisation ; délégation et dévolution de compétences ; collectivité locale (personne morale élue, à budget propre) et établissement public ; subsidiarité ; correspondance entre ceux qui décident, paient et bénéficient | 3, 4 |
| Le budget local | budget de fonctionnement et d'investissement ; règle d'équilibre et « règle d'or » ; épargne brute ; emprunt et endettement ; tutelle *a priori* et *a posteriori* | 5 |
| Les ressources propres | ressources propres et ressources transférées ; autonomie financière et autonomie fiscale (pouvoir sur le taux, sur l'assiette) ; impôt, taxe et redevance (contrepartie, principe du bénéfice, capacité contributive) ; impôt local propre, impôt partagé, centimes additionnels ; assiette, taux, émission, recouvrement, rendement | 6, 7, 8 |
| Les transferts | transferts conditionnels et inconditionnels, globaux et spécifiques ; dotation de fonctionnement et subvention d'investissement ; péréquation verticale et horizontale, des ressources et des besoins ; fonds commun | 9 |
| Mesurer | taux d'autonomie financière (recettes propres / ressources hors emprunt) ; potentiel et effort fiscal ; taux de recouvrement ; dépendance aux transferts ; capacité d'endettement | 10 |

Le chapitre ne contient aucune valeur tunisienne : les ratios y sont définis, ils sont calculés au
chapitre 10.

### 2.2 Les chapitres

| # | Chapitre | Mouvement | Contenu | Sources de départ |
|---|---|---|---|---|
| 1 | **Présentation** | — | Ce que sont les collectivités locales (communes, régions, conseils de gouvernorat, selon les textes successifs) ; carte « collectivité × ressources × compétences » ; les quatre mouvements du volume ; frontières avec les autres volumes | AFD 2018, ch. 2 |
| 2 | **Les notions** | notions | Voir § 2.1 | AFD 2018, ch. 1 ; Dafflon et Madiès 2008 ; manuscrit 2013 |
| 3 | **Histoire des collectivités et de leurs finances** | institutions | Municipalités beylicales et coloniales ; organisation après l'indépendance ; textes fondateurs des communes et des conseils régionaux ; Constitution de 2014 (chapitre du pouvoir local) et code des collectivités locales ; textes postérieurs — tous à établir au JORT | AFD 2018, ch. 2 et 7 ; JORT |
| 4 | **Compétences et organisation** | institutions | Ce que font les collectivités, par délégation ou par dévolution ; agences et organismes publics ; ce que cela coûte | AFD 2018, ch. 4 ; Hammami, Dafflon et Gilbert, PARD 2021 ; note DGCL 2016 |
| 5 | **Budgets et comptes** | institutions | Nomenclature, procédure budgétaire, règles d'équilibre, endettement ; tutelle et contrôle | AFD 2018, ch. 3 ; Dafflon, RTF n° 20 (2013) ; Dafflon, « Le budget local » (2021) |
| 6 | **Les impôts sur les immeubles** | ressources | TIB et TNB : assiette, prix de référence, taux, exonérations, recouvrement ; réforme par réforme | Code de la fiscalité locale et modificatifs (à établir au JORT) ; manuscrit 2013, ch. 4 ; AFD 2018, ch. 5 ; rapports « Stratégie de l'habitat » 2014 (pistes à vérifier) |
| 7 | **Les impôts sur l'activité** | ressources | TCL : assiette sur le chiffre d'affaires, taux minimaux ; taxe hôtelière ; autres impôts | Idem ; CNF 2013, groupe « fiscalité locale » |
| 8 | **Taxes, redevances et autonomie fiscale** | ressources | Taxes locales ; redevances et paiements des usagers ; ce que les collectivités peuvent moduler et ce que l'État fixe ; classification des ressources | AFD 2018, ch. 5 ; Dafflon, RTF n° 25 (2017) ; Dafflon et Gilbert, RTF n° 24 (2017) |
| 9 | **Les transferts de l'État** | ressources | FCCL (quote-part, critères de répartition) ; transferts sur crédits des ministères ; transferts exceptionnels ; réformes des dotations depuis 2014 ; subventions d'investissement, CPSCL, lien prêt-subvention ; programmes régionaux | AFD 2018, ch. 6 ; manuscrit 2013, ch. 5 ; PARD 2021 et 2022 ; Gilbert, *Transparence et droit* |
| 10 | **La longue période** | chiffres | Les ratios du chapitre 2 calculés dans la durée : ressources propres et transferts, rendement de chaque impôt local, recouvrement, dépenses et investissement, endettement ; par type de collectivité si les sources le permettent | Voir § 3 |
| A | Annexe : chronologie des textes | | | |
| B | Annexe : glossaire | | | |

Les chapitres 6 à 8 suivent la classification du code de la fiscalité locale (impôts, taxes,
redevances), à vérifier sur le code lui-même. Le chapitre 3 se dédouble si la matière d'avant 1956
le justifie.

## 3. Données à construire (tunisia-data)

| Série | Sources à exploiter | État |
|---|---|---|
| Ressources des collectivités : propres / transferts / emprunt | manuscrit 2013, ch. 5 (2010-2012) ; AFD 2018, § 3.7 et 6.7 ; lois de règlement ; CPSCL | à chercher au-delà de 2012 |
| Rendement de la TIB, de la TNB, de la TCL | CNF août 2013 (2010-2012) ; Dafflon, RTF n° 25, annexe (recettes communales 2010-2016, à vérifier sur l'imprimé) ; ancien portail du ministère (collecte en cours) | à reconstituer |
| Quote-part et répartition du FCCL | manuscrit 2013, tableau 5-10 (2006-2012) ; lois de finances | à reconstituer |
| Prêts et subventions de la CPSCL | rapports annuels de la CPSCL (à chercher) | à chercher |
| Prix à la consommation (déflateur) | INS, déjà dans tunisia-data | disponible |

Chaque série reconstruite reçoit sa fiche de provenance, source par source, dans tunisia-data.

## 4. Étapes

1. **Documentation**, chapitre par chapitre : notes documentaires (`docs/notes/finances-locales-*.md`),
   textes lus au JORT, fiches `RECHERCHE` pour ce qui reste introuvable. D'abord la doctrine des notions (chapitre 2),
   le code de la fiscalité locale et ses modificatifs (chapitres 6 à 8), puis les textes du FCCL et de
   la CPSCL (chapitre 9), enfin l'histoire (chapitre 3).
2. **Données** : séries du § 3 dans tunisia-data, avec leurs fiches de provenance.
3. **Création du volume** : `precis/fr/finances_locales/`, `build.sh`, CI, page d'accueil (volume VII),
   `_quarto.yml` arabe à la main, collection Zotero, AGENTS.md (sept volumes). Le livre arabe est sauté
   tant que sa traduction n'est pas livrée.
4. **Rédaction**, un chapitre par PR, en commençant par le chapitre 2 (les notions,
   dont dépendent tous les autres), puis 6 et 7 (les plus sourcés), 9, 5, 4, 3, et la présentation
   en dernier.
5. **Traduction** à la fin de chaque lot.

## 5. Sources déjà repérées

- **Doctrine** : `docs/notes/biblio-fiscalite-locale.md` — six textes de B. Dafflon et G. Gilbert
  (deux en accès libre) ; leur livre AFD 2018, synthèse de référence, dont les chapitres 2 à 7
  recoupent ce plan ; rapports PARD 2021-2022 ; manuscrits des chapitres 4 et 5 de 2013, hors dépôt
  (`~/Documents/biblio-precis/fiscalite-locale/`), à citer de préférence par leur version publiée.
- **Foncier** : références en cours de vérification
  (`~/Documents/biblio-precis/fiscalite-locale/foncier/`).
- **Ministère des Finances** : documents de la réforme fiscale 2013-2014
  (`docs/notes/reforme-fiscale-2013-2014-inventaire.md`) et collecte en cours sur l'ancien portail.

## 6. Questions ouvertes

Titre du volume arrêté par l'humain le 4 octobre 2026 : « Les finances locales ».


- Faut-il un chapitre propre pour les régions et les conseils de gouvernorat, ou les traiter avec
  les communes ?
- Les taxes affectées à des fonds (hors budgets locaux) entrent-elles dans le périmètre ?

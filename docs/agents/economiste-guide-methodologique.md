# Guide méthodologique — « Ce qu'en dit l'économie »

Ce guide est la référence durable, pour le rôle « économiste » comme pour les
contributeurs humains, de la section **« Ce qu'en dit l'économie »** placée en fin de
chaque chapitre du précis. Il dit **comment** nous traitons cet objet (partie A) et
**où** nous puisons nos sources (partie B). Il est additif : il n'altère aucun volume ni
chapitre. La consigne opérationnelle du rôle reste `docs/agents/economiste.md` ; ce guide
la complète et lui sert d'étape 0.

La section « Ce qu'en dit l'économie » porte sur **le type de dispositif** (incidence
d'une taxe sur la consommation, effets d'emploi d'un salaire minimum, ciblage contre
universalité d'une allocation, incitations au départ d'un régime de pension, incidence
d'une subvention aux prix), pas sur le dispositif tunisien particulier. Elle fait une page
au plus ; la fiche datée `docs/notes/eco-<dispositif>.md` en est la source.

---

## Partie A — Notre approche

Cinq axes structurent chaque fiche, puis chaque section. Ils ne sont pas interchangeables :
l'ordre est celui du raisonnement.

### A.1 Théorie d'abord, empirique ensuite — jamais l'un sans l'autre

On expose **ce que la théorie prédit**, avec les **hypothèses** qui portent la prédiction
(concurrence ou pouvoir de marché, information parfaite ou asymétrique, élasticités
supposées, rationalité, bouclage budgétaire). Une prédiction sans ses hypothèses n'est pas
un résultat : c'est un slogan. On expose ensuite **ce que l'empirique mesure** : plages
d'estimation, pays, périodes, méthodes dominantes (expériences, quasi-expériences,
variables instrumentales, différences de différences, méta-analyses). Les deux ensemble,
toujours. Une théorie sans mesure reste une conjecture ; une mesure sans théorie est un
nombre sans mécanisme, qu'on ne sait ni transposer ni discuter.

Règle de chiffre : **aucune élasticité, aucun ordre de grandeur sans sa plage, son pays et
sa période d'estimation.** « L'élasticité de l'emploi au salaire minimum est faible » ne
s'écrit pas ; « proche de zéro à modestement négative sur données américaines
1990–2015 selon la méthode » s'écrit.

### A.2 Consensus contre débattu — et sur quoi porte le désaccord

On sépare nettement **ce qui fait consensus** de **ce qui reste débattu**, et on dit **sur
quoi** porte le désaccord. Un désaccord entre économistes porte rarement sur tout : il
porte sur le **mécanisme** (par quel canal l'effet passe), sur l'**ampleur** (le signe est
admis, la taille non), ou sur les **conditions** (vrai ici, pas là). On le nomme
explicitement. Écrire « c'est débattu » sans dire de quoi relève le débat n'informe pas le
lecteur du précis.

### A.3 Pertinence au niveau de développement de la Tunisie — axe central

Un résultat obtenu sur un pays riche **ne se transpose pas mécaniquement** à un pays à
revenu intermédiaire. C'est un axe de premier plan, pas une réserve de bas de page. On
privilégie, quand elles existent, les preuves venues de **pays comparables** (revenu
intermédiaire, région MENA). Quand un résultat est conditionné par le contexte, on le
signale, en nommant le facteur de contexte :

- **informalité** : une part de l'emploi et de la consommation échappe à l'impôt et aux
  cotisations, ce qui déplace l'incidence et affaiblit les leviers fiscaux ;
- **capacité administrative** : collecter, cibler, verser suppose un appareil qui, ailleurs,
  est supposé acquis ;
- **marché du travail dual** (formel/informel, public/privé) : les effets d'un salaire
  minimum ou d'une cotisation diffèrent selon le segment ;
- **poids des subventions** et des prix administrés, qui modifie l'incidence réelle des
  taxes et des réformes de prix.

Quand on ne dispose que de preuves de pays riches, on le **dit** et on précise en quoi la
transposition est fragile, au lieu d'importer le chiffre tel quel.

### A.4 Les sources tunisiennes — où regarder côté tunisien

Pour les données et le cadrage national, on regarde, dans l'ordre d'usage :

- **CRES** — Centre de recherches et d'études sociales (protection sociale, retraites,
  ciblage, pauvreté) ;
- **ITCEQ** — Institut tunisien de la compétitivité et des études quantitatives
  (compétitivité, modélisation, études économiques et sociales) ;
- **INS** — Institut national de la statistique (enquêtes ménages, emploi, consommation,
  prix) ;
- **BCT** — Banque centrale de Tunisie (statistiques monétaires et financières) ;
- **Banque mondiale, FMI, BAD** — rapports pays et documents de travail sur la Tunisie ;
- **DGELF** et les **ministères** (Finances, Affaires sociales, Économie) pour le cadre et
  les données administratives.

Le détail des adresses et des rattachements figure en partie B, sous-section tunisienne.

### A.5 Les études proprement tunisiennes — les situer, sans refaire leur fiche

Ce sont les travaux empiriques **portant sur la Tunisie elle-même** : articles, thèses,
rapports CRES/ITCEQ, documents de travail pays de la Banque mondiale et du FMI. On dit leur
**méthode**, on les **situe** dans le savoir général (confirment-elles, nuancent-elles, ou
contredisent-elles les plages internationales ?), **sans refaire** la fiche d'étude —
celle-ci relève du chapitre « rapports et études » du livre
(`docs/conventions-redaction.md`, § 3). On reconnaît honnêtement que cette littérature est
**souvent mince** : peu d'évaluations causales, séries courtes, accès aux microdonnées
limité. Ce qu'elle ne permet pas de trancher se dit comme tel.

### A.6 Règles de forme, valables partout

- **Ton documentaire** : on rapporte des résultats et leurs désaccords, on **ne recommande
  rien**. Un désaccord s'écrit comme un désaccord, avec son objet.
- **Aucun « on sait que » sans référence.** Chaque résultat renvoie à une synthèse ou à une
  étude identifiée.
- **Aucun chiffre sans plage, pays, période** (cf. A.1).
- **Les chiffres ne sont jamais des paramètres du modèle.** Aucune élasticité, aucun ordre
  de grandeur issu de la littérature n'entre dans un tableau de paramètres, une figure de
  série ou le modèle. Si un résultat appelle un paramètre de comportement, on le note dans
  la fiche et le constat va dans `docs/notes/backlog-modele.md`, jamais dans un volume.
- **Livrable** : une **fiche datée** `docs/notes/eco-<dispositif>.md`, de structure fixe
  (cf. `economiste.md`), arrêtée à un mois et une année, à revoir à la revue annuelle.

---

## Partie B — Nos sources, par sous-champ

Base à consulter **en premier** (étape 0), avant le web ouvert. Les **syllabus de cours
ouverts** sont des bibliographies structurées, idéales pour borner « établi / débattu ». Les
**handbooks** donnent l'état de l'art ; les **auteurs** sont cités pour un apport précis
(handbook, cours, résultat), jamais en name-dropping.

**Statut de vérification.** Les URL de cours ouverts et les rattachements d'auteurs marqués
*(vérifié, <mois année>)* ont été confirmés par recherche web en **novembre 2026**. Ceux
marqués *(non vérifié)* sont repris du plan de sources sans confirmation individuelle et
sont à contrôler avant citation.

### B.1 Économie publique (fiscalité, incidence, taxation optimale, redistribution)

- **Cours ouverts** :
  - MIT OCW **14.471 Public Economics I** (Poterba, Werning), Fall 2012 —
    <https://ocw.mit.edu/courses/14-471-public-economics-i-fall-2012/> *(vérifié, nov. 2026)*.
    Syllabus et readings accessibles sur le même cours.
  - Berkeley **Econ 230A Graduate Public Economics**, E. Saez —
    <https://eml.berkeley.edu/~saez/course/course.html> ; page et notes de cours :
    <https://eml.berkeley.edu/~saez/> *(vérifié, nov. 2026)*. Comprend aussi Econ 131
    (undergraduate) avec notes téléchargeables.
- **Synthèses / handbooks** : *Handbook of Public Economics* (dir. Auerbach, Chetty,
  Feldstein, Saez) ; ***Mirrlees Review*** — *Dimensions of Tax Design* et *Tax by Design*,
  IFS — <https://ifs.org.uk/mirrlees-review> *(vérifié, nov. 2026)*.
- **Auteurs** : Emmanuel Saez (Berkeley, *vérifié*) ; Raj Chetty (Harvard, William A. Ackman
  Professor of Public Economics, dir. Opportunity Insights, *vérifié*) ; Henrik Kleven
  (Princeton, Professor of Economics and Public Affairs, *vérifié*) ; Thomas Piketty (PSE,
  *non vérifié*) ; Alan Auerbach (Berkeley, *non vérifié*).
- **Départements** : MIT, Berkeley, Harvard, LSE, PSE, Princeton.

### B.2 Économie du travail (salaire minimum, emploi, offre de travail)

- **Cours ouverts** : MIT OCW **14.661 Labor Economics I** (Angrist, Acemoglu), Fall 2017 —
  <https://ocw.mit.edu/courses/14-661-labor-economics-i-fall-2017/> *(vérifié, nov. 2026)*.
- **Synthèses** : *Handbook of Labor Economics* (dir. Ashenfelter, Card).
- **Auteurs** : David Card (Berkeley, Nobel 2021 pour ses contributions empiriques à
  l'économie du travail, *vérifié*) ; Joshua Angrist (MIT, *vérifié via le cours*) ; Chetty,
  Saez (sur l'offre de travail et les réponses à l'impôt, *vérifiés*).
- **Départements** : MIT, Berkeley, Princeton.

### B.3 Économie de la santé (assurance maladie, hôpital, ciblage)

- **Synthèses** : *Handbook of Health Economics* (dir. Culyer, Newhouse ; et vol. ultérieurs
  dir. Pauly, McGuire, Barros, *non vérifié pour les volumes récents*).
- **Auteurs** : Jonathan Gruber (MIT, dir. du Health Care Program au NBER, auteur de *Public
  Finance and Public Policy*, *vérifié*) ; David Cutler (Harvard, *non vérifié*) ; Amy
  Finkelstein (MIT, *non vérifié*) ; Thomas McGuire (*non vérifié*).
- **Cours / réseau** : programmes santé MIT/Harvard ; NBER Health Care *(non vérifié comme
  cours ouvert)*.
- **Départements** : Harvard, MIT.

### B.4 Économie de l'éducation (dépense, rendement, qualité)

- **Synthèses** : *Handbook of the Economics of Education* (dir. Hanushek, Machin, Woessmann)
  *(vérifié — volumes et direction confirmés via hanushek.stanford.edu, nov. 2026)*.
- **Auteurs** : Eric Hanushek (Hoover Institution, Stanford, *vérifié*) ; Stephen Machin
  (LSE, *non vérifié*) ; Ludger Woessmann (ifo / Munich, *non vérifié*) ; Caroline Hoxby
  (Stanford, *non vérifié*).
- **Départements** : Stanford, LSE, Munich (ifo).

### B.5 Économie du développement (pauvreté, ciblage, évaluation d'impact)

- **Cours ouverts** : MIT OCW **14.771 Development Economics** (Duflo, Olken ; Banerjee pour
  les éditions antérieures), Fall 2021 —
  <https://ocw.mit.edu/courses/14-771-development-economics-fall-2021/> *(vérifié, nov.
  2026)*. Lectures, readings et vidéos accessibles.
- **Réseau** : J-PAL (Abdul Latif Jameel Poverty Action Lab, MIT) ; MITx pour les cours en
  ligne *(J-PAL vérifié, offre MITx non vérifiée dans le détail)*.
- **Auteurs** : Esther Duflo et Abhijit Banerjee (MIT, cofondateurs/codirecteurs de J-PAL,
  Nobel 2019 avec Michael Kremer, *vérifiés*) ; Angus Deaton (Princeton, *non vérifié*) ;
  Michael Kremer (*non vérifié*).
- **Départements** : MIT (J-PAL), Harvard, Berkeley.

### B.6 Économie politique (institutions, capacité de l'État, économie politique des réformes)

- **Cours ouverts** :
  - MIT OCW **14.75 Political Economy and Economic Development**, Fall 2012 (premier cycle) —
    <https://ocw.mit.edu/courses/14-75-political-economy-and-economic-development-fall-2012/>
    *(vérifié, nov. 2026)*.
  - MIT OCW **14.770 Introduction to Political Economy** (Acemoglu), Fall 2017 (cycle
    supérieur) —
    <https://ocw.mit.edu/courses/14-770-introduction-to-political-economy-fall-2017/>
    *(vérifié, nov. 2026)*. Il précède **14.773 Political Economy of Institutions and
    Development**, dont les syllabus sont publiés sur economics.mit.edu, mais qui ne figure
    pas comme cours OCW complet *(14.773 comme cours OCW : non vérifié)*.
  - LSE, cours d'économie politique du développement (T. Besley) *(URL non vérifiée)*.
- **Synthèses** : Persson & Tabellini, *Political Economics: Explaining Economic Policy* (MIT
  Press, 2000) ; Besley & Persson, *Pillars of Prosperity* (Princeton, 2011).
- **Auteurs** : Daron Acemoglu (MIT, *vérifié via le cours*) ; Tim Besley (LSE, School
  Professor of Economics and Political Science, W. Arthur Lewis Professor of Development
  Economics, *vérifié*) ; James Robinson (Chicago, *non vérifié*) ; Torsten Persson (IIES
  Stockholm, *non vérifié*).
- **Départements** : MIT, LSE, IIES Stockholm.

### B.7 Assurance sociale et retraites (pensions, prestations, cotisations)

- **Synthèses / références** : *Handbook of Public Economics*, chapitres assurance sociale ;
  travaux Diamond–Orszag sur la réforme des retraites.
- **Auteurs** : Jonathan Gruber (MIT, assurance sociale, *vérifié*) ; Martin Feldstein
  (sécurité sociale, *non vérifié*) ; Peter Diamond (MIT, *non vérifié*) ; Henrik Kleven
  (réponses comportementales aux transferts, *vérifié Princeton*).
- **Côté tunisien** : CRES (modèle PROST de la Banque mondiale pour la simulation des
  retraites, mentionné sur le site CRES, *vérifié nov. 2026*).

### B.8 Secteur informel

- **Références** : La Porta & Shleifer, « Informality and Development » (*JEP*, *non vérifié
  dans le détail*) ; travaux de Jacques Charmes ; statistiques et rapports du **BIT** sur
  l'emploi informel.
- **Pertinence précis** : volume informel ; facteur de contexte central pour l'incidence
  fiscale et les cotisations (cf. A.3).

### B.9 Subventions et énergie (réforme des prix administrés)

- **Références** : rapports **FMI** sur la réforme des subventions énergétiques ;
  **IISD/GSI** (*Global Subsidies Initiative*) ; Banque mondiale.
- **Pertinence précis** : volume compensation / subventions ; incidence et redistribution
  d'une réforme de prix.

### B.10 Entreprises publiques, régulation, privatisation

- **Références** : Megginson & Netter, revue sur la privatisation (*JEL*, *non vérifié*) ;
  Shleifer & Vishny ; principes de l'**OCDE** sur le gouvernement d'entreprise des
  entreprises publiques.
- **Pertinence précis** : volume entreprises publiques.

### B.11 Finances publiques locales et fédéralisme budgétaire

- **Références** : Wallace Oates, *Fiscal Federalism* et sa littérature de synthèse ;
  rapports Banque mondiale / OCDE sur la décentralisation.
- **Pertinence précis** : volume finances locales.

### B.12 Économie publique comportementale (transversal)

- **Références** : travaux de Raj Chetty sur la saillance fiscale et les options par défaut
  (*vérifié Harvard*) ; synthèses d'économie comportementale appliquée aux politiques
  publiques.
- **Pertinence précis** : transversal (conception des prélèvements et des prestations).

### B.13 Mesure de la pauvreté et ciblage

- **Références** : Anthony Atkinson (mesure des inégalités et de la pauvreté) ; Angus Deaton
  (*The Analysis of Household Surveys*) ; Martin Ravallion (*The Economics of Poverty*).
- **Pertinence précis** : prestations sociales, ciblage contre universalité.
- **Côté tunisien** : CRES sur l'identification des ménages pauvres et le ciblage (*vérifié
  nov. 2026*).

### B.14 Fiscalité et développement / capacité fiscale

- **Références** : Besley & Persson, *Pillars of Prosperity* (*vérifié via LSE*) ; Gordon &
  Li sur la fiscalité dans les pays en développement (*non vérifié dans le détail*) ;
  Michael Keen (FMI) sur la TVA et la fiscalité du développement (*non vérifié*).
- **Pertinence précis** : fiscalité et contexte tunisien (informalité, capacité
  administrative).

### B.15 Sources tunisiennes et régionales (pendant tunisien de la base internationale)

Pour le cadrage national et les données :

- **CRES** — Centre de recherches et d'études sociales — <http://www.cres.tn> *(vérifié, nov.
  2026)*. Protection sociale, retraites, pauvreté, ciblage.
- **ITCEQ** — Institut tunisien de la compétitivité et des études quantitatives —
  <https://www.itceq.tn> *(vérifié, nov. 2026)*. Études économiques et sociales,
  compétitivité, modélisation ; sous tutelle du ministère de l'Économie.
- **INS** — Institut national de la statistique — enquêtes ménages, emploi, consommation,
  prix *(URL à confirmer : ins.tn, non vérifiée ici)*.
- **BCT** — Banque centrale de Tunisie — statistiques monétaires et financières *(URL à
  confirmer : bct.gov.tn, non vérifiée ici)*.
- **DGELF** et **ministères** (Finances, Affaires sociales, Économie) — cadre et données
  administratives.
- **Organisations internationales sur la Tunisie** : **Banque mondiale**, **FMI**, **BAD**
  (rapports pays et documents de travail), **BIT** (emploi, informalité, protection sociale).

**Rappel de collecte** (cf. `economiste.md`) : récupérer le PDF de tout document cité et le
ranger dans `tunisia-data` (`data/raw/<source>/`, hors git), avec une ligne au catalogue
`sources/<source>-urls.csv` (adresse, date de collecte, SHA-256). Un document introuvable
est noté tel, avec les adresses essayées.

---

## Vérifier et tenir à jour cette base

- Tout ajout d'URL de cours ouvert ou de rattachement d'auteur passe par une **vérification
  web**, avec la mention *(vérifié, <mois année>)* ou, à défaut, *(non vérifié)*.
- Les cours ouverts changent d'année et d'URL : revérifier à chaque revue annuelle, et
  préférer la page de cours à un PDF isolé susceptible de bouger.
- Base arrêtée à **novembre 2026** pour les éléments vérifiés ci-dessus.

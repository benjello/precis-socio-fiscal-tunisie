# Note documentaire — Infrastructure routière et autoroutière (livre « Le transport »)

Documentaliste, 10 novembre 2026. Ticket T3 du chantier « Livre transport »
(`docs/notes/transport-plan-livre.md`, § 3 chapitre « Infrastructure routière et autoroutes »,
§ 5 arbitrage 2). **Ce chantier instruit, il ne publie pas** : aucune modification de fichier du
précis, aucun `.qmd`, aucun commit. La présente note réunit la matière de la **politique
sectorielle** de l'infrastructure routière pour éclairer l'arbitrage sur le domicile des registres
concessions / péages / garanties, **sans dupliquer** ce qui est déjà écrit et sourcé dans la
section Tunisie Autoroutes des entreprises publiques.

> **Règle de domicile rappelée.** Les comptes de Tunisie Autoroutes restent aux entreprises
> publiques. Le livre transport garde ce que l'État **décide et paie** : la concession, le péage
> comme politique, le fonds, les garanties d'emprunt par projet. L'arbitrage sur le déménagement
> des registres n'est **pas tranché ici** ; la note l'instruit.

---

## 0. Ce qui est DÉJÀ établi et sourcé dans les entreprises publiques (NE PAS re-sourcer)

Fichier : `precis/fr/entreprises_publiques/_transports.qmd`, section « Tunisie Autoroutes »
(`#sec-ep-ge-autoroutes`), tableau-registre `#tbl-ep-registre-autoroutes`. Références CSL dans
`precis/fr/entreprises_publiques/references.json` (sauf mention LF 2019, qui est dans
`precis/fr/references.json`).

**Ancres du registre (34), par objet :**

- **Concessions (décrets d'approbation) :** `#r-ep-autoroutes-1995` (Hammam-Lif–M'saken,
  décret 95-720), `#r-ep-autoroutes-2000` (A4 Tunis–Bizerte, décret 2000-645),
  `#r-ep-autoroutes-2002` (A3 Tunis–Medjez El Bab–Oued Ezzargua, décret 2002-537),
  `#r-ep-autoroutes-2004` (A1 M'saken–El Jem et El Jem–Sfax, décrets 2004-1073 et 2004-1074),
  `#r-ep-autoroutes-2016` (Sfax–Gabès, décret 2016-256), `#r-ep-autoroutes-2019-concessions`
  (Oued Ezzargua–Bou Salem, Médenine–Ras Jedir, Gabès–Médenine, décrets 2019-661/662/663),
  `#r-ep-autoroutes-2025` (avenant de prorogation, décret 2025-218).
- **Péages (décrets de tarification) :** `#r-ep-autoroutes-1996-peage` (décret 96-2263),
  `#r-ep-autoroutes-2003-peage` (2003-1118), `#r-ep-autoroutes-2003-a4` (2003-1119),
  `#r-ep-autoroutes-2009-a3` (2009-383), `#r-ep-autoroutes-2010-a1` (2010-3222),
  `#r-ep-autoroutes-2014-peage` / `-2014-sections` (2014-4201 à 4204),
  `#r-ep-autoroutes-2019-a3` / `-2019-a1` (2019-977, 2019-1066),
  `#r-ep-autoroutes-2020-a1` / `-2021-a1` / `-2022-a1` (reports : 2020-405, 2021-487, 2022-56).
- **Garanties d'emprunt par projet (8 lois/décrets-lois, 1999-2012) :** `#r-ep-autoroutes-1999`
  (loi 99-47 + 99-50), `#r-ep-autoroutes-2001` (loi 2001-40), `#r-ep-autoroutes-2002-garantie`
  (loi 2002-72), `#r-ep-autoroutes-2003-garantie` (loi 2003-4), `#r-ep-autoroutes-2010-garantie`
  (loi 2010-5), `#r-ep-autoroutes-2011-fades` (décret-loi 2011-65), `#r-ep-autoroutes-2011-bad`
  (décret-loi 2011-111), `#r-ep-autoroutes-2012` (loi 2012-6).
- **Capital (souscriptions de l'État) :** `#r-ep-autoroutes-1999`, `-2002-capital` (loi 2002-96),
  `-2006` (loi 2006-3), `-2010-capital` (loi 2010-57), `-2019-capital` (loi 2019-75).
- **Fonds de développement des autoroutes :** `#r-ep-autoroutes-1999-fonds` (création, LF 1999)
  et `#r-ep-autoroutes-2019-fonds` (suppression, LF 2019) — détaillés au § 1 ci-dessous.

**Clés CSL existantes à réutiliser (non à recréer) :** `@decret95-720-autoroutes`,
`@decret96-2263-peage`, `@decret2000-645-autoroutes`, `@decret2002-537-autoroutes`,
`@decret2003-1118-peage`, `@decret2003-1119-peage`, `@decret2004-1073-autoroutes`,
`@decret2004-1074-autoroutes`, `@decret2009-383-peage`, `@decret2010-3222-peage`,
`@decret2014-4201-peage` à `@decret2014-4204-peage`, `@decret2016-256-autoroutes`,
`@decret2019-661-autoroutes`/`-662`/`-663`, `@decret2019-977-peage`, `@decret2019-1066-peage`,
`@decret2020-405-peage`, `@decret2021-487-peage`, `@decret2022-56-peage`,
`@decret2025-218-autoroutes`, `@loi99-47-autoroutes`, `@loi99-50-autoroutes`,
`@loi2001-40-autoroutes`, `@loi2002-72-autoroutes`, `@loi2002-96-autoroutes`,
`@loi2003-4-autoroutes`, `@loi2006-3-autoroutes`, `@loi2010-5-autoroutes`,
`@loi2010-57-autoroutes`, `@dl2011-65-autoroutes`, `@dl2011-111-autoroutes`,
`@loi2012-6-autoroutes`, `@loi2019-75-autoroutes`, `@loi98-111-lf1999`,
`@loi2018-56-lf2019-ar`. Comptes/transferts : `@minfin-ep-2020`, `@minfin-ep`, `@minfin-ep-2022`,
`@minfin-ep-2023`, `@minfin-ep-2024`, `@minfin-ep-2025`.

**Conséquence pour l'arbitrage 2.** Tout le dispositif juridique (concession, péage, garanties,
fonds) est déjà lu, daté et cité — avec les montants et les dates d'effet — dans les entreprises
publiques. Le livre transport n'a **rien à re-sourcer** de ce bloc. Si l'humain décide de
déménager, il déplace des ancres existantes ; s'il décide de renvoyer, il pose des liens. La
matière **propre** que la présente note ajoute (et qui n'existe nulle part ailleurs) est :
(a) l'**antécédent** du dispositif — comment les autoroutes et le réseau routier étaient
financés *avant* la concession de 1995 ; (b) la **ressource/emploi** du fonds comme compte spécial
du Trésor ; (c) la **route hors autoroute** financée au budget. Ce sont les trois objets du ticket.

---

## 1. Le fonds de développement des autoroutes (1999-2018)

### Faits sourcés (textes déjà cités dans les EP — rappel pour l'angle sectoriel)

- **Création — loi de finances pour 1999.** Loi n° 98-111 du 28 décembre 1998, **art. 16 et 17**,
  p. 2502 [`@loi98-111-lf1999`] : création d'un **compte spécial du Trésor** « Fonds de
  développement des autoroutes », qui finance les **dépenses de réalisation des projets
  autoroutiers**, **ordonnancé par le ministre chargé de l'équipement** (art. 16), **alimenté par
  les ressources des opérations de privatisation revenant à l'État** (art. 17). Ancre EP
  `#r-ep-autoroutes-1999-fonds`.
- **Suppression — loi de finances pour 2019.** Loi n° 2018-56 du 27 décembre 2018, **art. 10**,
  p. 5439 [`@loi2018-56-lf2019-ar`, dans `precis/fr/references.json`] : **suppression** du compte
  spécial, **reliquats versés au budget de l'État**, **abrogation des articles 16 et 17** de la
  LF 1999. Ancre EP `#r-ep-autoroutes-2019-fonds`.
- **Durée et nature.** Le fonds a donc vécu de la **gestion 1999 à la gestion 2018** (suppression
  prenant effet gestion 2019). C'est une **suppression sèche**, non une fusion : le ticket parle
  de « suppression/fusion en 2018 » — la vérification établit qu'il s'agit d'une suppression, les
  reliquats retournant au budget général, sans transfert à un fonds repreneur nommé.
- **Lecture sectorielle (apport propre).** Le fonds est l'instrument par lequel l'État a, pendant
  vingt exercices, **affecté le produit des privatisations à la construction autoroutière**, sous
  l'ordonnancement du ministre de l'Équipement (donc hors du compte de Tunisie Autoroutes). C'est
  typiquement « ce que l'État décide et paie » : un **compte spécial du Trésor**, non un compte
  d'entreprise. À ce titre, il relève par nature de la politique sectorielle plus que des comptes
  de l'opérateur — élément à verser à l'arbitrage 2.

### Lacune : ressources et emplois annuels du fonds (série non extraite)

Les deux textes donnent la **règle** (ce qui entre, ce qui sort, qui ordonnance) mais **pas les
montants** année par année. La série « recettes de privatisation affectées » et « dépenses de
réalisation » du fonds, 1999-2018, n'est pas extraite. Elle se trouve, le cas échéant, dans les
**annexes « comptes spéciaux du Trésor » aux lois de finances et lois de règlement** (tableau des
CST) et dans les rapports de la Cour des comptes sur la clôture du budget. → fiche de recherche
proposée `r-fonds-autoroutes-ressources-emplois` (§ 6) ; backlog (§ 7).

---

## 2. Le programme autoroutier ANTÉRIEUR à la concession de 1995

**Résultat : oui, il existe un programme autoroutier antérieur à 1995, et il est documenté par
des textes.** L'autoroute A1 dite « autoroute du Sud » (Tunis–Hammam-Lif–M'saken) n'a **pas** été
créée par la concession de 1995 : elle a été **construite directement par l'État** (travaux
publics / équipement), **section par section**, dans les années 1976-1994, sur financement de
**prêts extérieurs ratifiés par loi** et imputés au budget — **avant** la création de Tunisie
Autoroutes (société anonyme créée le 13 mai 1992) et avant la concession de 1994-1995. La
concession de 1995 a donc **confié à l'opérateur l'exploitation d'un ouvrage déjà construit sur
fonds publics**, puis l'extension du réseau.

### Faits sourcés (recherche JORT, `jort_cache.db`, 10 novembre 2026)

Reconstruction du tracé A1 par les lois de ratification des prêts de construction, par section
d'ouest en est :

- **Section Tunis–Turki.** Loi n° 76-71 du 11 août 1976, ratification de l'accord de prêt avec le
  **Fonds koweïtien de développement économique arabe** « pour participer au financement de
  l'autoroute Tunis–Turki ». JORT 1976 n° 51, p. 1928 ; PDF `jort/1976/1976F/Jo05176.pdf`.
- **Section Turki–Hammamet.** Loi n° 81-72 du 9 août 1981, ratification de la convention de prêt
  conclue à Koweït le 28 mars 1981 avec le Fonds koweïtien, « relative au projet de l'autoroute
  Turki–Hammamet ». JORT 1981 n° 52, p. 1869 ; PDF `jort/1981/1981F/Jo05281.pdf`.
- **Section Hammamet–M'saken (deux prêts).** Loi n° 90-69 du 24 juillet 1990, ratification de
  l'accord conclu à Abou Dhabi le 15 mars 1990 avec le **Fonds arabe pour le développement
  économique et social**, « relatif au projet de l'autoroute Hammamet–M'saken ». JORT 1990 n° 49,
  p. 978 ; PDF `jort/1990/1990F/Jo04990.pdf`. — Et loi n° 90-89 du 29 octobre 1990, ratification
  d'un accord avec le **Fonds koweïtien**, même projet Hammamet–M'saken. JORT 1990 n° 70,
  p. 1574 ; PDF `jort/1990/1990F/Jo07090.pdf`.

Ensemble, ces quatre lois tracent l'A1 Tunis→Turki→Hammamet→M'saken construite **sur emprunts de
l'État** de 1976 à ~1994, c'est-à-dire exactement le tronçon que le décret n° 95-720 du 17 avril
1995 confie **ensuite** en concession à Tunisie Autoroutes (« Hammam-Lif–M'saken »,
`#r-ep-autoroutes-1995`). L'antécédent attendu par la méthode (« l'ouvrage ou le régime que le
texte fondateur remplace ou étend ») est donc établi : **concession de 1995 = bascule d'un modèle
de construction directe sur budget + prêts souverains vers un modèle de concession-péage à un
opérateur public**, l'ouvrage initial étant déjà payé par l'État.

### Texte-cadre du domaine routier (fondation sectorielle, non encore en référence CSL)

- **Loi n° 86-17 du 7 mars 1986, portant refonte de la législation relative au domaine public
  routier de l'État.** JORT 1986 n° 17, p. 387-389. C'est le **texte-cadre** du domaine routier
  (autoroutes comprises : la loi est visée par le décret de concession de 1995, art. 34). Son
  intitulé (« **refonte** ») indique qu'elle remplace une législation antérieure du domaine
  routier (à identifier : textes du Protectorat / des premières décennies de l'indépendance). Elle
  est **citée en prose** dans `_transports.qmd` mais **n'a pas de clé CSL** → candidate à créer
  (§ 5), car elle est le fondement commun à la route et à l'autoroute.
- **Décret n° 87-654 du 20 avril 1987, déterminant les formes et conditions de concession
  d'occupation du domaine public routier.** JORT 1987 n° 31, p. 578-579. C'est le **régime de
  concession** sur lequel reposent les conventions autoroutières (visé par le décret 2000-645).
  Cité en prose dans les EP, **sans clé CSL** → candidate à créer (§ 5).

### Ce qui n'a PAS été trouvé (à consigner comme tel)

Aucun **texte unique de « schéma directeur autoroutier » ou de « plan autoroutier »** n'existe au
JORT : la programmation autoroutière relève des **plans de développement** (VIᵉ Plan 1982-1986,
VIIᵉ Plan 1987-1991, etc.), documents de planification publiés hors JORT, non législatifs. La
recherche `jort_cache` sur « schéma directeur », « réseau autoroutier » est **revenue bredouille**
(0 résultat). → fiche `r-autoroutes-programme-avant-1995` proposée (§ 6), qui consigne les quatre
lois trouvées **et** l'absence de texte de schéma directeur, avec les pistes (plans de
développement, *Bulletin économique et social de la Tunisie*).

---

## 3. La route hors autoroute, financée au budget (ministère de l'Équipement)

### Faits sourcés et séries repérées

- **Cadre juridique.** La loi n° 86-17 du 7 mars 1986 (ci-dessus) régit le **domaine public
  routier classé** (autoroutes, routes à grande circulation / nationales, routes régionales,
  routes locales). Le **classement** du réseau se fait par voie réglementaire (décrets/arrêtés de
  classement — non dépouillés ici, à chercher).
- **Financement extérieur historique du programme routier.** Le programme routier classé et les
  pistes rurales ont été financés par des **prêts de la Banque mondiale (IBRD/IDA) « projets
  routiers »**, ratifiés par loi — p. ex. loi n° 79-9 du 25 janvier 1979 (accord de Washington du
  24 juillet 1978), loi n° 88-37 du 3 mai 1988 (accord de Washington du 15 janvier 1988), loi
  n° 88-139 du 3 décembre 1988 (accord de Tunis du 3 novembre 1988). Ces textes (repérés dans
  `jort_cache` mais **non lus un à un**) matérialisent la **famille « route sur budget + prêts
  projets »**, distincte de la famille « autoroute concédée + péage ». À confirmer par lecture.
- **Dépense budgétaire de la mission Équipement (données disponibles, tunisia-data /
  docs/notes).** Crédits de paiement **votés** de la mission « Équipement, habitat et
  infrastructure » : 1 735,0 M DT (2021), 1 802,5 (2022), 1 883,5 (2023), 1 970,0 (2024),
  2 022,0 (2025) [`docs/notes/budget-missions-vote-2021-2025.csv`, source : rapports sur le budget
  de l'État / annexes LF]. **Exécution** (paiements, RAP Équipement) : 1 440,8 M DT (2018),
  1 262,5 (2019), 1 609,7 (2020), 1 446,9 (2021), 1 423,5 (2022), 1 603,1 (2023)
  [`docs/notes/budget-missions-execute-lotB.csv`]. Mission « Transport (et logistique) » votée :
  829,5 (2021) → 1 076,5 (2025) ; exécution 640,0 (2018) → … Ces totaux sont **au niveau mission
  entière**, pas isolés sur la route.
- **PAP/RAP et budgets du ministère de l'Équipement (47 PDF rangés).** Fiche
  `tunisia-data/sources/ministere-transport-equipement-habitat.md` ; catalogue CSV
  `ministere-transport-equipement-habitat-urls.csv`. Les PAP/RAP Équipement 2015-2024 donnent les
  crédits **par programme**, mais la fiche note qu'ils portent « des indicateurs d'activité, des
  subventions et des budgets prévisionnels », pas de ventilation fine route classée / routes
  rurales relue. La fiche « الطرقات السيارة » 2023 (`AutoRoute_16-2-2023-1.pdf`) donne l'état du
  réseau autoroutier : 743 km ouverts, 186 en cours, 390 programmés, cible 1 320 km en 2035.
- **Cour des comptes.** Fiche `tunisia-data/sources/cour-des-comptes-transport-eau-habitat.md` et
  CSV associés : observations sur Tunisie Autoroutes (rapport 2016), sur le transport terrestre
  (rapport 2008, qui décrit aussi le RFR). Les rapports de **clôture du budget** (2020-2024)
  portent les **prêts du Trésor et appuis** mais n'isolent pas la dépense routière. Rapports
  spécifiques routiers non identifiés dans le lot lu.
- **Banque mondiale, *Tunisia Infrastructure Diagnostic* (décembre 2019).** PDF **déjà rangé**
  dans tunisia-data (`data/raw/banque-mondiale-rapports/bm-infrastructure-diagnostic-2019/…`,
  81 p., SHA-256 au catalogue) ; fiche `bm-infrastructure-diagnostic-2019.md`. Diagnostic des
  entreprises d'infrastructure (dont SNCFT, Transtu) et des besoins d'investissement ; **pas de
  série budgétaire route classée** par an. Méthode : rapports annuels et états financiers des
  entreprises, comptes 2009-2017, chiffres « approximatifs » (note de la fiche). **Aucun nouveau
  téléchargement n'a été nécessaire** pour cette note (le PDF préexiste, indexé).

### Lacune principale : la dépense d'investissement routier sur la longue période

Il n'existe **aucune série homogène isolée** « investissement routier (réseau classé) » et
« routes rurales / pistes (PDRI) » sur longue période dans tunisia-data. Les totaux disponibles
sont au **niveau mission** (Équipement entière, 2018-2025), qui agrège route, habitat, hydraulique
et bâtiment. Remonter une série route exige de dépouiller, par **programme/sous-programme**, les
lois de finances (titre II, section Équipement), les RAP Équipement et, en amont de la GBO
(avant ~2015), les budgets d'investissement par « projet » des lois de finances et le *Budget
économique*. **Approximation non tentée** ici : l'écart (la part route dans la mission Équipement)
n'est pas bornable sans ce dépouillement, et une part supposée renverserait la lecture. → backlog
et fiche `r-investissement-routier-longue-periode` (§ 6-7).

---

## 4. Références candidates CSL-JSON

### À réutiliser (déjà présentes — NE PAS recréer)

Toutes les clés listées au § 0 existent déjà (EP `references.json` ; LF 2019 dans
`precis/fr/references.json`). En particulier, pour les trois objets du ticket :
`@loi98-111-lf1999` (fonds, création) et `@loi2018-56-lf2019-ar` (fonds, suppression).

### À créer (nouvelles entrées proposées)

```json
{
  "id": "loi86-17-domaine-public-routier",
  "type": "legislation",
  "title": "Loi n° 86-17 du 7 mars 1986, portant refonte de la législation relative au domaine public routier de l'État",
  "title-short": "Loi n° 86-17 du 7 mars 1986",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "17",
  "page": "387-389",
  "issued": {"date-parts": [[1986, 3, 7]]},
  "language": "fr"
}
```
```json
{
  "id": "decret87-654-concession-domaine-routier",
  "type": "legislation",
  "title": "Décret n° 87-654 du 20 avril 1987, déterminant les formes et conditions de concession d'occupation du domaine public routier",
  "title-short": "Décret n° 87-654 du 20 avril 1987",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "31",
  "page": "578-579",
  "issued": {"date-parts": [[1987, 4, 20]]},
  "language": "fr"
}
```
```json
{
  "id": "loi76-71-autoroute-tunis-turki",
  "type": "legislation",
  "title": "Loi n° 76-71 du 11 août 1976, portant ratification de l'accord de prêt entre la République tunisienne et le Fonds koweïtien de développement économique arabe pour participer au financement de l'autoroute Tunis–Turki",
  "title-short": "Loi n° 76-71 du 11 août 1976",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "51",
  "page": "1928",
  "issued": {"date-parts": [[1976, 8, 11]]},
  "language": "fr"
}
```
```json
{
  "id": "loi81-72-autoroute-turki-hammamet",
  "type": "legislation",
  "title": "Loi n° 81-72 du 9 août 1981, portant ratification de la convention de prêt conclue à Koweït le 28 mars 1981 avec le Fonds koweïtien pour le développement économique arabe, relative au projet de l'autoroute Turki–Hammamet",
  "title-short": "Loi n° 81-72 du 9 août 1981",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "52",
  "page": "1869",
  "issued": {"date-parts": [[1981, 8, 9]]},
  "language": "fr"
}
```
```json
{
  "id": "loi90-69-autoroute-hammamet-msaken-fades",
  "type": "legislation",
  "title": "Loi n° 90-69 du 24 juillet 1990, portant ratification de l'accord de prêt conclu à Abou Dhabi le 15 mars 1990 avec le Fonds arabe pour le développement économique et social, relatif au projet de l'autoroute Hammamet–M'saken",
  "title-short": "Loi n° 90-69 du 24 juillet 1990",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "49",
  "page": "978",
  "issued": {"date-parts": [[1990, 7, 24]]},
  "language": "fr"
}
```
```json
{
  "id": "loi90-89-autoroute-hammamet-msaken-fkdea",
  "type": "legislation",
  "title": "Loi n° 90-89 du 29 octobre 1990, portant ratification de l'accord de prêt conclu avec le Fonds koweïtien pour le développement économique arabe, relatif au projet de l'autoroute Hammamet–M'saken",
  "title-short": "Loi n° 90-89 du 29 octobre 1990",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "70",
  "page": "1574",
  "issued": {"date-parts": [[1990, 10, 29]]},
  "language": "fr"
}
```
```json
{
  "id": "bm-infrastructure-diagnostic-2019",
  "type": "report",
  "title": "Tunisia Infrastructure Diagnostic",
  "publisher": "Banque mondiale",
  "issued": {"date-parts": [[2019, 12]]},
  "number-of-pages": "81",
  "URL": "https://openknowledge.worldbank.org/entities/publication/ea047a6b-941f-58d0-91df-69c99737dac8",
  "language": "en"
}
```

> Les pages/numéros JORT des lois 76-71, 81-72, 90-69, 90-89, 86-17 et du décret 87-654 viennent
> de `jort_cache.db` (intitulé, année, numéro, pages). **Avant citation en prose définitive**, les
> fascicules correspondants doivent être relus à la page (règle du corpus : un fascicule « texte »
> peut porter un tableau/visa en image ; vérifier l'article cité). Les PDF FR sont dans le corpus
> local (`jort/1976/…`, `jort/1981/…`, `jort/1990/…`, `jort/1986/…`, `jort/1987/…`).

---

## 5. Notions à glossaire (à vérifier/ajouter — proposées, non écrites)

> Rappel : interdiction de toucher `precis/glossaire.yml` ; ci-dessous des propositions.

- **Fonds de développement des autoroutes** (AR : صندوق تنمية الطرقات السيارة) — compte spécial du
  Trésor, 1999-2018, ordonnancé par le ministre de l'Équipement, alimenté par les recettes de
  privatisation ; supprimé par la LF 2019. Source canonique : loi 98-111 (LF 1999), art. 16-17 ;
  loi 2018-56 (LF 2019), art. 10. *NB : une entrée « Tunisie Autoroutes » existe déjà au glossaire
  des EP ; vérifier qu'il n'y a pas de doublon.*
- **Domaine public routier (de l'État)** (AR : الملك العمومي للطرقات) — catégorie de domanialité
  des routes classées et autoroutes ; cadre : loi 86-17 du 7 mars 1986. Distingue route classée
  et voirie communale (renvoi finances locales).
- **Concession autoroutière / péage** — déjà porté par la section EP ; si le chapitre routier est
  écrit, vérifier l'entrée et son renvoi. Source : décret 87-654 (régime), décrets de concession
  et de péage par tronçon.
- **Compte spécial du Trésor** (notion transversale) — déjà susceptible d'exister via la fiscalité
  / les fonds spéciaux ; vérifier la cohérence avant d'en créer une propre au transport.

---

## 6. Recherches infructueuses / à ouvrir — fiches `docs/recherches.yml` proposées

> Non écrites par la note (interdiction d'éditer hors de ce fichier) ; proposées pour que
> `/rediger` ou le documentaliste suivant les enregistre via `scripts/recherches.py`.

**Fiche 1 — programme autoroutier avant 1995 (schéma directeur introuvable, prêts trouvés) :**
```yaml
- id: r-autoroutes-programme-avant-1995
  objet: >-
    Texte de programme autoroutier antérieur à la concession de 1995 — « schéma directeur
    autoroutier », « plan autoroutier » ou décret de programme des premiers tronçons de l'A1
    (autoroute du Sud Tunis–M'saken), autre que les lois de ratification des prêts de construction
    déjà identifiées (lois n° 76-71, 81-72, 90-69, 90-89).
  ou: [precis/fr/entreprises_publiques/_transports.qmd#sec-ep-ge-autoroutes]
  requetes:
    - {source: titres_fts, termes: ["schema directeur routier", "reseau autoroutier", "programme autoroutier", "autoroute"]}
    - {source: titres_like, termes: ["autoroute", "schema directeur", "Turki", "Hammamet", "M'saken"]}
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache.db interrogé le 10 novembre 2026 (intitulés + objet, LIKE). 135 textes « autoroute »
        au total ; 25 avant 1995, dont 21 décrets d'expropriation/déclassement de parcelles et
        4 lois de ratification de prêts de construction (76-71 Tunis–Turki ; 81-72 Turki–Hammamet ;
        90-69 et 90-89 Hammamet–M'saken) — RETENUES comme antécédent. AUCUN texte de « schéma
        directeur » ni de « plan autoroutier » : la programmation relève des plans de développement
        (hors JORT). Pistes non suivies : VIᵉ et VIIᵉ Plans, Bulletin économique et social de la
        Tunisie, annexes des budgets économiques.
      couvert_jus_au: 1994-12-31
      sources: [titres_fts, titres_like]
```

**Fiche 2 — ressources et emplois annuels du fonds de développement des autoroutes :**
```yaml
- id: r-fonds-autoroutes-ressources-emplois
  objet: >-
    Montants annuels des recettes (produit des privatisations affecté) et des dépenses (réalisation
    des projets autoroutiers) du compte spécial du Trésor « Fonds de développement des autoroutes »,
    1999-2018, pour construire la série ressources/emplois du fonds.
  ou: [precis/fr/entreprises_publiques/_transports.qmd#r-ep-autoroutes-1999-fonds]
  requetes:
    - {source: titres_like, termes: ["comptes speciaux du Tresor", "fonds de developpement des autoroutes"]}
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        Non cherché au fascicule : la série vit dans les ANNEXES aux lois de finances (tableau des
        comptes spéciaux du Trésor) et dans les lois de règlement, non dans un texte isolé du JORT.
        À dépouiller dans les annexes LF/LR 1999-2019 (tunisia-data : annexe-budget-etat) et les
        rapports de la Cour des comptes sur la clôture du budget.
      couvert_jus_au: 2026-11-10
      sources: [titres_like]
```

**Fiche 3 — dépense d'investissement routier (réseau classé, routes rurales) longue période :**
```yaml
- id: r-investissement-routier-longue-periode
  objet: >-
    Série homogène de la dépense publique d'investissement routier — réseau classé (routes
    nationales/régionales/locales) et routes rurales/pistes (PDRI) — distincte de l'autoroute,
    sur longue période, pour le chapitre « Infrastructure routière » du livre transport.
  ou: [docs/notes/transport-plan-livre.md]
  requetes:
    - {source: plein_texte, termes: ["investissement routier", "routes classees", "pistes rurales", "entretien routier"]}
  passes:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        Disponible au niveau MISSION seulement (Équipement entière, 2018-2025 ; voir
        docs/notes/budget-missions-*.csv), non isolé sur la route. À reconstruire par
        programme/sous-programme dans les RAP Équipement (GBO, ~2015+) et, avant la GBO, par projet
        d'investissement dans les lois de finances (titre II) et les budgets économiques. Prêts BM
        « projets routiers » (lois 79-9, 88-37, 88-139) repérés, non lus.
      couvert_jus_au: 2026-11-10
      sources: [plein_texte]
```

---

## 7. Backlog (propositions — à verser hors de cette note ; interdiction de toucher `backlog-precis.md`)

- **Fonds de développement des autoroutes — série ressources/emplois 1999-2018** : extraire les
  recettes (privatisations affectées) et les dépenses du CST dans les annexes « comptes spéciaux du
  Trésor » aux lois de finances et de règlement, et les rapports de clôture de la Cour des comptes.
  (fiche `r-fonds-autoroutes-ressources-emplois`.)
- **Investissement routier hors autoroute — série longue période** : reconstruire la dépense route
  classée + routes rurales par programme (RAP Équipement) et par projet (LF titre II, budgets
  économiques) ; isoler la route dans la mission Équipement. (fiche
  `r-investissement-routier-longue-periode`.)
- **Lois BM « projets routiers »** (79-9, 88-37, 88-139 et voisines) : lire au fascicule pour
  qualifier la famille « route sur budget + prêts projets » et dater les programmes routiers
  successifs.
- **Texte-cadre du domaine routier avant 1986** : identifier la législation que la loi 86-17
  « refond » (Protectorat / premières décennies) — antécédent du cadre routier.
- **Décrets/arrêtés de classement du réseau routier** (routes nationales, régionales, locales) :
  non dépouillés ; nécessaires pour la notion « réseau classé ».
- **Quatre lois de prêts A1 (76-71, 81-72, 90-69, 90-89), loi 86-17, décret 87-654** : relire au
  fascicule à la page avant citation définitive, puis créer les entrées CSL du § 4.
- **Arbitrage 2 (domicile des registres concessions/péages/garanties)** : la matière juridique est
  entièrement dans les EP (§ 0) ; la matière *propre* au livre transport est l'antécédent (§ 2), le
  fonds comme CST (§ 1) et la route budgétaire (§ 3). Élément versé à l'humain : le fonds et
  l'antécédent penchent « politique sectorielle » ; les comptes restent EP.

---

## 8. Lacunes (synthèse — ce qui n'a pas pu être sourcé de façon fiable)

1. **Montants annuels du fonds** (recettes privatisation, dépenses projets), 1999-2018 : non
   extraits — série à bâtir sur les annexes CST des LF/LR (lacune, non approximée).
2. **Dépense d'investissement routier isolée** (réseau classé, routes rurales) longue période :
   indisponible au grain route ; seulement le total mission Équipement 2018-2025. Approximation
   refusée (part route dans la mission non bornable).
3. **Schéma directeur / plan autoroutier comme texte** : n'existe pas au JORT ; relève des plans
   de développement (hors corpus législatif) — à chercher hors JORT.
4. **Classement du réseau routier** : décrets/arrêtés non dépouillés.
5. **Textes pré-1995 et cadre (76-71, 81-72, 90-69, 90-89, 86-17, 87-654)** : intitulés et pages
   pris de `jort_cache` ; **relecture au fascicule requise** avant citation ferme.

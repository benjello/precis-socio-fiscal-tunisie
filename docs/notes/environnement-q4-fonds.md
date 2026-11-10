# Note documentaire — Livre « L'environnement », Q4 (+ amorce Q5) : FODEP et fonds de la protection et de l'esthétique de l'environnement

Rôle : documentaliste. Date : 11 novembre 2026. Branche `chantier/environnement-livre`.
Emplois des deux fonds spéciaux environnementaux du tableau B des lois de finances, leurs textes
créateurs et d'application, amorce des primes de dépollution (Q5).

Sources : `jort_cache.db` et corpus JORT local ; PDF des lois de finances 2000-2025
(`PDFs/Lois_de_Finances/`) ; `tunisia-data/sources/` (minfin-fonds-speciaux-tresor, cour-des-comptes) ;
chapitres fiscalité déjà rédigés. Web non sollicité (tout trouvé en local).

---

## A. Faits sourcés

### A.1 — FODEP : texte créateur et chaîne législative

- **Le fonds de dépollution (FODEP) est créé par la loi de finances pour 1993 = loi n° 92-122 du
  29 décembre 1992, art. 35 à 37** (clé existante `@lf-1993`). L'art. 35, dernier §, porte le champ
  d'intervention, modifié par tous les textes ultérieurs. *Articles 35-37 non encore lus à l'image :
  voir TODO fiscalité (ne pas dupliquer) et lacune L1.*
- **Texte d'application (primes) : décret n° 93-2120 du 25 octobre 1993, fixant les conditions et
  les modalités d'intervention du fonds de dépollution**, *JORT* n° 83 du 2 novembre 1993,
  p. 1858-1859 (recid 91730). **Pièce maîtresse de Q5.** ⚠️ Fascicule image seul → OCR requis (L2).
- **Modification : décret n° 2005-2636 du 24 septembre 2005**, modifiant le décret 93-2120, *JORT*
  n° 79 du 4 octobre 2005, p. 2618-2619 (recid 84758). ⚠️ Couche texte corrompue → OCR requis (L2).
- **Taxe pour la protection de l'environnement au profit du FODEP : loi de finances 2003 = loi
  n° 2002-101 du 17 décembre 2002, art. 58-59** (institution) **et art. 60** (réécrit le dernier §
  de l'art. 35 de la LF 1993), *JORT* n° 102 du 17 décembre 2002, p. 2883 (`@lf-2003`). *Taux/positions
  à relire à l'image — TODO fiscalité, ne pas dupliquer.*
- **Extensions successives** (modifient l'art. 35 LF 1993 ou l'art. 58 LF 2003) :
  - LF 2005 = loi n° 2004-90 du 31 déc. 2004, art. 67-68 (élargissement du champ de la taxe),
    *JORT* n° 105, p. 3442 (`@lf-2005`) ;
  - LF 2006 = loi n° 2005-106 du 19 déc. 2005, art. 14-15, *JORT* n° 101, p. 3597 (`@lf-2006`) ;
  - LF 2009 = loi n° 2008-77 du 22 déc. 2008, art. 11, *JORT* n° 104, p. 4275 (`@lf-2009`) ;
  - LF 2014 = loi n° 2013-54 du 30 déc. 2013, art. 14 et 71 (systèmes « écozit »/« écofiltres »),
    *JORT* n° 105, p. 3669 et 3690-3691 (`@lf-2013`/`@lf-2014`) ;
  - LF 2025 = loi n° 2024-48 du 9 déc. 2024, art. 66 : ajoute « économie verte, bleue et circulaire »
    au champ du FODEP **et alloue une dotation de 20 M D prélevée sur le FODEP** à une ligne de prêts
    bonifiés — **emploi explicite du fonds** (`@lf-2025`, art. 66 lu en couche texte FR fiable).
  - *Recoupe le TODO fiscalité (taxe, LF 2005/2008/2010/2014/2016/2018) : localisations JORT données
    ici, instruction article par article de la taxe reste domiciliée à la fiscalité — renvoyer à son
    backlog, ne pas dupliquer.*

### A.2 — Financement externe du FODEP (antécédent/contexte)

Le FODEP est un guichet de subventions à l'investissement de dépollution adossé à des **prêts
bailleurs** (KfW allemande, BEI) :
- Loi n° 92-64 du 13 juillet 1992 (ratification accord BEI du 18 déc. 1990) — antérieure au fonds ;
- **Loi n° 96-24 du 25 mars 1996**, approbation d'un contrat de financement du 5 décembre 1995 avec
  la **BEI** pour le **fonds de dépollution industrielle**, *JORT* n° 25 du 26 mars 1996, p. 615
  (recid 112460) ;
- cluster de contrats garantie/prêt « dépollution » 2015-2017 (décret 2015-123 ; loi 2016-2 ; lois
  2017-32 et 2017-33).
- **Emploi concret documenté** (Cour des comptes, 16e rapport, exercice 1998, p. 418-422) : prêt
  FODEP de **5,6 M€** au Groupe chimique tunisien (stockage de phosphogypse à Gabès ; source
  `tunisia-data/sources/cour-des-comptes-observations-energie-industrie.csv`, à relire à l'image).

### A.3 — Fonds de la protection et de l'esthétique de l'environnement : texte créateur localisé

Le plan le donnait « intitulé seul, aucun texte lu ». Trouvé :
- **Création : loi de finances 2004 = loi n° 2003-80 du 29 décembre 2003, art. 52 et 53** (« création
  d'un fonds de la propreté de l'environnement et de l'esthétique des villes »), *JORT* n° 104 du
  30 décembre 2003, p. 3728 (`@lf-2004`, recid 111013). Ressources : art. 54-55 (modifient les
  art. 58-59 de la LF 2003, taxe) et art. 56 (tarif de l'art. 117 du code des droits d'enregistrement
  et de timbre), p. 3728-3729.
- **Changement d'appellation : loi de finances 2005 = loi n° 2004-90 du 31 décembre 2004, art. 18** :
  devient **« fonds de la protection et de l'esthétique de l'environnement »**, *JORT* n° 105,
  p. 3433 (`@lf-2005`, recid 110819).

### A.4 — Fonds de transition énergétique : hors périmètre

Confirmé au tableau B des LF (ex. 2014 : 100 M D, ministère de l'industrie). **Une ligne de renvoi
suffit** → compensation/entreprises publiques. Non instruit.

---

## B. Séries : les emplois (prévisions du tableau B), année par année

**Nature de la donnée.** Chaque LF arrête au **tableau B** (« PRÉVISIONS DE RECETTES ET DE DÉPENSES
DES FONDS SPÉCIAUX DU TRÉSOR ») un montant **unique par fonds**, prévision **équilibrée (recette =
dépense)** : montants **votés**, non des réalisations. L'emploi réel (décaissements de primes) n'y
est pas (lacune L3). Couche texte FR fiable (total 2014 recoupé : 952 800 000 D).

### B.1 — Fonds de dépollution (FODEP), prévision recettes=dépenses, en dinars

| Année (LF) | Prévision (D) |
|---|---:|
| 2011 | 33 000 000 |
| 2012 | 44 000 000 |
| 2013 | 44 000 000 |
| 2014 | 40 000 000 |
| 2015 | 40 000 000 |
| 2016 | 18 000 000 |
| 2017 | 18 000 000 |
| 2018 | 17 000 000 |
| 2019 | 17 000 000 |
| 2020 | 17 000 000 |

### B.2 — Fonds de la protection et de l'esthétique de l'environnement, prévision recettes=dépenses, en dinars

| Année (LF) | Prévision (D) |
|---|---:|
| 2014 | 3 000 000 |
| 2015 | 3 000 000 |
| 2016 | 2 000 000 |
| 2017 | 6 000 000 |
| 2018 | 6 000 000 |
| 2019 | 6 000 000 |
| 2020 | 6 000 000 |

Source des deux séries : tableau B des lois de finances FR (2014 p. 3703, *JORT* n° 105/2013).
**Rattachement ministériel** : en 2014 sous « Ministère de l'Équipement et de l'Environnement », en
2020 sous « Ministère des Affaires locales et de l'Environnement » — trace du périmètre mouvant.

**Homogénéité.** Série homogène et directe (même source, tableau, unité, concept « prévision votée »).
**Ne pas chaîner à une série de réalisations** (raccord muet prévision/exécution). Trous 1994-2010 et
2021-2025 laissés honnêtes tant que l'OCR n'est pas fait (L1/L4).

---

## C. Amorce Q5 — primes de dépollution : d'où viennent les montants

- **Deux guichets distincts à ne pas confondre** : (1) les **primes du FODEP** (décret 93-2120,
  financement KfW/BEI) — subventions à l'investissement de dépollution industrielle ; (2) la **prime
  de dépollution du code d'incitation de 1993** (« lutte contre la pollution »), devenue dans la loi
  de l'investissement de 2016 la **prime « développement durable »** (50 %, plafond 300 000 D —
  `_regimes_incitation.qmd`, tbl. #tbl-df-primes-2017).
- **La seule série de montants déjà dans le dépôt** concerne le **guichet code d'incitation**, pas le
  FODEP : notification OMC du 1er juin 2001 (`@omc-2001-g-scm-n-71-tun`, sect. IX, p. 14-15), ligne
  « Prime de dépollution » : **2,464 M D (1998), 3,2 M D (1999), 2,5 M D (jusqu'à sept. 2000)** —
  déjà cités au chapitre des régimes d'incitation (tbl. #tbl-ri-omc-2001). **Ne couvrent pas les
  emplois du FODEP proprement dit.**
- **Aucune série longue des montants de primes versées par le FODEP n'est établie** (L3). Piste
  amont : rapports d'activité ANPE/ministère de l'environnement, conventions KfW (non catalogués).

---

## D. Références candidates (CSL-JSON)

**Déjà présentes** dans `precis/fr/references.json` (réutiliser) : `lf-1993`, `lf-2003`, `lf-2004`,
`lf-2005`, `lf-2006`, `lf-2009`, `lf-2013`, `lf-2014`, `lf-2017`, `lf-2018`, `lf-2020`, `lf-2025` ;
`omc-2001-g-scm-n-71-tun`.

**À créer :**

```json
[
  {"id":"decret-93-2120","type":"legislation","title":"Décret n° 93-2120 du 25 octobre 1993, fixant les conditions et les modalités d'intervention du fonds de dépollution","number":"93-2120","issued":{"date-parts":[[1993,10,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"83","page":"1858-1859","note":"Publié au JORT du 2 novembre 1993. Texte d'application du FODEP (LF 1993, art. 35-37). Fascicule image seul : à lire à l'image."},
  {"id":"decret-2005-2636","type":"legislation","title":"Décret n° 2005-2636 du 24 septembre 2005, modifiant et complétant le décret n° 93-2120 du 25 octobre 1993 fixant les conditions et les modalités d'intervention du fonds de dépollution","number":"2005-2636","issued":{"date-parts":[[2005,9,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"79","page":"2618-2619","note":"Publié au JORT du 4 octobre 2005. Couche texte illisible : à lire à l'image."},
  {"id":"loi-96-24","type":"legislation","title":"Loi n° 96-24 du 25 mars 1996, portant approbation d'un contrat de financement conclu le 5 décembre 1995 entre la République tunisienne et la Banque européenne d'investissement pour la contribution au financement du fonds de dépollution industrielle","number":"96-24","issued":{"date-parts":[[1996,3,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"25","page":"615"}
]
```

*(Pour le fonds de l'esthétique, pas de clé nouvelle : citer via `lf-2004` art. 52-53 et `lf-2005`
art. 18.)*

---

## E. Notions à glossaire (propositions — ne pas éditer `glossaire.yml`)

- **`fonds-de-depollution` (FODEP)** — compte spécial du Trésor ouvert par la LF 1993 (loi n° 92-122,
  art. 35-37), alimenté par la taxe pour la protection de l'environnement (LF 2003) et des prêts
  bailleurs (KfW/BEI) ; guichet de subventions à l'investissement de dépollution. Source : décret
  93-2120 + loi 92-122, art. 35.
- **`fonds-protection-esthetique-environnement`** — compte spécial créé par la LF 2004 (loi n° 2003-80,
  art. 52-53) sous le nom « fonds de la propreté de l'environnement et de l'esthétique des villes »,
  renommé par la LF 2005 (loi n° 2004-90, art. 18).
- Désambiguïsation `anpe-environnement` (voir note Q1). Existent déjà : `#g-fonds-special-tresor`,
  `#g-taxe-protection-environnement`, `#g-onas`.

---

## F. Lacunes et besoins d'OCR / relecture-image

- **L1 — LF 1993, art. 35-37 (loi 92-122)** : articles créateurs du FODEP non lus. *Déjà au
  TODO/backlog fiscalité (`_taxes_fonds_speciaux.qmd` @sec-fst-tpe) — ne pas dupliquer.*
- **L2 — Décrets 93-2120 et 2005-2636** : fascicules à couche texte vide (1993) / corrompue (2005) →
  **OCR/lecture-image indispensable** pour les conditions, taux et plafonds des primes (cœur de Q5).
- **L3 — Emplois réels (réalisations) des deux fonds** : les tableaux B ne donnent que des prévisions
  équilibrées ; décaissements effectifs absents des LF et des lois de règlement (qui ne donnent que le
  total de tous les FST, d'après `minfin-fonds-speciaux-tresor.md`). À chercher : rapports d'activité
  ministère environnement/ANPE, rapports KfW, lois de règlement détaillées. **Lacune ouverte.**
- **L4 — Prévisions FODEP 1994-2010 et 2021-2025, esthétique 2004-2013 et 2021-2025** : absentes de la
  couche texte FR → **OCR du tableau B** de chaque LF.
- **L5 — Prime de dépollution hors OMC 2001** : aucune série continue ; seule 1998-2000 établie, et
  elle vise le code d'incitation, non le FODEP.

**Report (routage durable)** : lacunes L1-L5 et les deux fiches de recherche ci-dessous à verser,
par le rôle habilité, au backlog du livre environnement (à créer) et à `docs/recherches.yml` selon
`docs/backlog-routage.md`.

---

## G. Recherches infructueuses — fiches proposées pour `docs/recherches.yml`

**Fiche 1 — emplois réels du FODEP :**
```yaml
- id: r-fodep-emplois-realisations
  objet: réalisations (décaissements de primes, bénéficiaires) du fonds de dépollution, année par année
  ou: [docs/notes/environnement-plan-livre.md#q4, precis/fr/fiscalite/_taxes_fonds_speciaux.qmd#sec-fst-tpe]
  requetes:
    titres_fts: ['"fonds de dépollution"', '"dépollution"']
    titres_like: ['dépollution', 'FODEP']
    iort_ar: ['صندوق إزالة التلوث', 'إزالة التلوث']
    plein_texte: ['fonds de dépollution', 'FODEP', 'صندوق إزالة التلوث']
    depuis: 1993-01-01
  passes:
  - date: 2026-11-11
    role: documentaliste
    sources: [jort_cache, corpus_local, tunisia-data]
    couverture: "textes créateurs et modificatifs trouvés ; tableaux B des LF FR 2011-2020 donnent les PRÉVISIONS. Aucune réalisation : lois de règlement = total FST seul. Non parcourus : rapports d'activité ministère environnement/ANPE, rapports KfW."
    couvert_jusqu_au: 2026-11-11
    resultat: aucun
  a_faire:
  - OCR du décret 93-2120 (JORT 83/1993) et du décret 2005-2636 (JORT 79/2005)
  - OCR du tableau B des LF 1994-2010 et 2021-2025
  - chercher rapports d'activité ANPE/ministère environnement et rapports KfW/BEI
```

**Fiche 2 — conditions d'octroi des primes de dépollution (Q5)** : objet resserré sur le décret
93-2120 et ses modificatifs ; passe 2026-11-11 `resultat: partiel` (références trouvées, contenu non
lu faute d'OCR) ; `a_faire : OCR des deux fascicules`.

---

**Renvoi explicite** : le volet *prélèvement* (taux, assiette, positions de la taxe ; LF 2003
art. 58-59 à relire à l'image ; extensions LF 2005/2008/2010/2014/2016/2018) reste domicilié à la
**fiscalité** et figure déjà à son TODO/backlog — **non dupliqué ici**. Le présent livrable n'apporte
que l'**emploi** des fonds et les **textes d'application** (apport propre du livre).

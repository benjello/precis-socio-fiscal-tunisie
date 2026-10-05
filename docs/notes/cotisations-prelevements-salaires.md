# Les autres prélèvements sur les salaires : TFP et FOPROLOS — note documentaire

Note de documentaliste, 5 octobre 2026. Elle prépare un chapitre « Les autres prélèvements sur
les salaires » du volume *Cotisations sociales*. Ce n'est pas un texte rédigé.

**Périmètre retenu (consigne du 5 octobre 2026).** Le précis traite l'impact économique,
distributif et budgétaire des prélèvements, leur évolution longue et leurs ruptures. Il ne
reprend pas le détail administratif : modalités de déclaration, délais, recouvrement,
procédure de l'avance. Pour chaque prélèvement, la note donne donc :

- l'institution ;
- les taux et l'assiette successifs, avec leurs dates d'effet ;
- les exonérations qui changent qui paie ;
- l'affectation des recettes ;
- l'endroit où se trouvent les données de rendement.

Les textes purement procéduraux ne sont signalés que pour mémoire (§ 1.6 et § 2.5).

**Statut de lecture.** Toutes les citations de cette note ont été lues sur le fascicule du
corpus local `~/projets/PDFs-legislation-tunisie/PDFs/JORT`, à l'image pour les scans, sauf
mention contraire. Les notes communes de la DGI (`markdown_output/Notes_Communes`) ont servi à
repérer les textes. Elles ne sont citées comme source que lorsqu'elles le disent
explicitement (« doctrine »). Les pages arabes ne sont données que lorsqu'elles ont été
relevées. Les URL pist.tn ont été testées le 5 octobre 2026 (`curl -kI` : 200,
`application/pdf`), sauf celle du fascicule français n° 5 de 1956, qui a expiré sans réponse.

## 0. Termes officiels (FR / AR)

| FR | AR (relevé au JORT) | Où |
|---|---|---|
| taxe de formation professionnelle (TFP) | الأداء على التكوين المهني | LF 1989, éd. AR, p. 1773-1774 ; LF 2013, art. 21 (intitulé AR dans jort_cache) |
| contribution au fonds de promotion du logement pour les salariés (FOPROLOS) | المساهمة (الراجعة) لصندوق النهوض بالمسكن لفائدة الأجراء | LF 1989, éd. AR, p. 1774 (« التخفيض في المساهمة الراجعة لصندوق النهوض بالمسكن لفائدة الأجراء ») |
| fonds de promotion du logement pour les salariés | صندوق النهوض بالمسكن لفائدة الأجراء | LF 2026, art. 21 (éd. AR) |
| avance sur la taxe de formation professionnelle | التسبقة على الأداء على التكوين المهني | décret gouv. n° 2019-228 (éd. AR) |
| droits de tirage | حقوق السحب | décret gouv. n° 2019-228 (éd. AR) |
| fonds de promotion de la formation professionnelle et de l'apprentissage | صندوق النهوض بالتكوين والتدريب المهني | LF 2018, tableau « ت » (éd. AR, p. 4295) |

Le FR « fonds de promotion **du** logement » (loi 77-54) alterne au JORT avec « **des**
logements » (LF 1989, LF 2011, LF 2013). L'intitulé de la loi 77-54 porte « du logement ».

## 1. Taxe de formation professionnelle (TFP)

URL des fascicules : `https://www.pist.tn/jort/<année>/<année>F|A/…` (vérifiées 5 oct. 2026 ;
FR 1956 non vérifiée, délai dépassé). « img » = lu à l'image, « txt » = couche texte, « ocr ».

### 1.1 Institution, taux, assiette

| Effet | Valeur | Source (JORT FR ; AR si relevée) |
|---|---|---|
| 19 janv. 1956 (jour franc après publication le 17) | **institution** ; redevables : patentés hors patente forfaitaire ; produit au budget de l'État ; taux renvoyé à un décret | décret du 12 janv. 1956, art. 27-28 — n° 5/1956, p. 58 (img) |
| 1957 | taux initial : **inconnu** (décret non lu) | décret du 16 janv. 1957 — n° 6 du 18 janv. 1957, p. 79 (jort_cache) |
| 1966 | même règle reprise au code du travail | loi 66-27, art. 338, 364-365 — n° 22 du 17 mai 1966, p. 806, 808-809 (img) |
| **1er janv. 1967** (énoncé) | **2 %**, taux unique | décret 66-527, art. 1-2 — n° 55/1966, p. 1804 (img) |
| **salaires de janv. 1989** (énoncé) | **1 %** industries manufacturières, **2 %** autres secteurs ; liquidation mensuelle sur salaires et rétributions | LF 1989 (loi 88-145), art. 29-30 — n° 87/1988, p. 1797 ; AR p. 1773-1774 (img) |
| 1991 (n° 86 bi-daté : 30 déc. 1990 ou 2 janv. 1991) | taux inchangés (1 % / 2 %) | LF 1991, art. 49 — n° 86/1990, p. 2054 (img) |
| 5 jours après dépôt, dépôt non daté ; doctrine (NC 10/2003) : **1er janv. 2003** | champ étendu aux **professions non commerciales** ; assiette : salaires + **avantages en nature** + rétributions | LF 2003, art. 35-36 — n° 102/2002, p. 2880 (txt décodé) |
| après 2003 | **aucune modification de taux repérée** (NC 5/2015 : 1 % / 2 %) | fiche `r-tfp-foprolos-taux-recents` |

« Industries manufacturières » : liste du décret 94-492 (renvoi NC 5/2015 ; décret non lu).

### 1.2 Exonérations qui changent qui paie

| Effet | Valeur | Source |
|---|---|---|
| depuis 1956 | redevables : champ de la patente, puis de l'IS/BIC (et BNC depuis 2003) ; forfaitaires exclus. Que l'État, les collectivités et les EPA en soient hors champ est **déduit** de ce critère, sans texte d'exonération ; des organismes publics situés dans ce champ payaient (exonération expresse des caisses en 2008) | décret 1956, art. 27 ; code du travail, art. 364 ; NC 5/2015 |
| 1er janv. 2008 (LF art. 64) | CNSS, CNRPS, CNAM exonérées | LF 2008, art. 40 — n° 104/2007, p. 4364 (txt) |
| date d'effet des art. 24 et 33 non établie (l'art. 31 ne vise que les art. 27-29) | petites entreprises : 3 ans (TFP et FOPROLOS) ; enseignement et formation : salaires des enseignants permanents | loi 2007-69, art. 24 et 33 — n° 104/2007, p. 4343, 4347 (ocr) |
| 1er janv. 2011 (LF art. 50) | hors assiette : primes du fonds national de l'emploi | LF 2011, art. 28 § 3 — n° 102/2010, p. 3467 (txt) |
| 1er janv. 2013 (LF art. 79) | hors assiette : gratification de fin de service | LF 2013, art. 21 — n° 1/2013, p. 7 (txt) |
| sans texte identifié | hors assiette : salaires des handicapés, emploi à l'étranger | NC 5/2015 seule — fiche `r-tfp-exclusions-handicapes-etranger` |

Les régimes d'incitation (CII 1993, loi 2017-8, LFC 2012 et 2015) forment une catégorie
d'exonérations qui n'a pas été inventoriée texte par texte (choix de périmètre).

### 1.3 Crédit d'impôt formation (réduit le rendement net)

| Effet | Valeur | Source |
|---|---|---|
| avant 1989 (arrêtés de 1974 et 1980, seuls les intitulés sont connus) ; 1989-2008 | ristournes pour les entreprises qui forment ; base légale : LF 1989, art. 31 et 33 | arrêtés du 28 déc. 1974 et du 28 oct. 1980 (jort_cache) ; LF 1989 — p. 1797 |
| **1er janv. 2009** (énoncé, art. 31) | **avance** = crédit d'impôt, au plus **60 %** de la TFP de l'année précédente, si TFP ≥ 1 000 D | loi 2007-69, art. 27, 31 — n° 104/2007, p. 4344-4346 (ocr) ; décret 2009-292, art. 2-3 — n° 11/2009, p. 424-425 (txt) |
| 2019 | taux de 60 % inchangé ; droits de tirage plafonnés à 0,6 % de la masse salariale (art. 15 nouveau) | décret gouv. 2019-228 — AR n° 21/2019, p. 785 (txt) |

### 1.4 Affectation

| Effet | Valeur | Source |
|---|---|---|
| 1956 | budget de l'État | décret 1956, art. 27 |
| jusqu'au 31 déc. 1966 | un « Fonds de formation professionnelle » est supprimé au **1er janv. 1967** (énoncé) ; qu'il ait reçu la TFP est probable mais non établi (décret de 1957 non lu) | LF 1967, art. 17 — n° 55/1966, p. 1788 (img) |
| 1967 | **budget de l'État** | LF 1967 (loi 66-79), art. 16 — p. 1788 (img) |
| 2000 (exécutoire 5 j. après dépôt, dépôt non daté) | **compte spécial du Trésor** « fonds de promotion de la formation professionnelle et de l'apprentissage » : TFP nette des ristournes | LF 2000, art. 17-18 — n° 105/1999, p. 2741 (txt décodé) |
| 1er janv. 2009 | même fonds : TFP **nette de l'avance** | loi 2007-69, art. 29 — p. 4346 (ocr) |

## 2. Contribution au FOPROLOS

### 2.1 Institution, taux, assiette

| Effet | Valeur | Source |
|---|---|---|
| **1er août 1977** (énoncé, art. 10 ; antérieur à la publication) | **institution** ; **2 %** des salaires soumis à cotisation CNRPS, CNSS, CRPSPEGT ; charge déductible ; perçue par les caisses | loi 77-54, art. 1-3, 10 — n° 53/1977, p. 2098-2099 (img) |
| 1987 : art. 49 en vigueur ; l'exigibilité selon l'art. 50 n'est pas établie pour le FOPROLOS (l'art. 50 vise les « cotisations » ; s'il s'applique : 1/3 de la part patronale au 1er juill. 1987, le reliquat à une date fixée par décret) | assiette étendue à l'ICP, à la majoration du SMIG de 1982 et à l'indemnité de transport | LF 1987, art. 49-50 — n° 78/1986, p. 1618 (img) |
| **salaires de janv. 1989** (énoncé) | **1 %** ; assiette : salaires et rétributions ; recouvrement par la recette des finances (et non plus par les caisses) | LF 1989, art. 35-38 — n° 87/1988, p. 1797 ; AR p. 1774 (img) |
| après 1989 | **aucune modification de taux repérée** (NC 15/2006 : 1 % de la masse salariale brute, avantages en nature compris) | fiche `r-tfp-foprolos-taux-recents` |

**Anomalie de renvoi (signalée, non tranchée).** La LF 1989, art. 38, met fin aux art. 2-4 de
la loi 77-54. Pourtant la LF 2006 (art. 54) et la LF 2023 (art. 57) complètent ensuite
l'art. 3, et les LF 2011 et 2013 complètent l'art. 2 « tel que modifié par l'art. 35 de la
loi 88-145 » (fiche `r-foprolos-art3-redaction`).

### 2.2 Exonérations qui changent qui paie

| Effet | Valeur | Source |
|---|---|---|
| depuis 1977 | redevables : **tout employeur public ou privé** sauf exploitants agricoles privés ; l'État est donc redevable (texte exprès), alors que pour la TFP sa sortie du champ n'est que déduite (§ 1.2) | loi 77-54, art. 1er ; NC 15/2006 |
| 2007-2011 | exonérations « petites entreprises » et « enseignement » (cf. § 1.2) | loi 2007-69, art. 24, 33 |
| 1er janv. 2011 | hors assiette : primes du FNE | LF 2011, art. 28 § 4 — p. 3467 |
| 1er janv. 2013 | hors assiette : gratification de fin de service | LF 2013, art. 22 — p. 7 |

### 2.3 Affectation

| Effet | Valeur | Source |
|---|---|---|
| 1977 | fonds de promotion du logement pour les salariés (prêts à l'accession des salariés) | loi 77-54, art. 5-6 |
| 1988 | prélèvement de **5 000 000 D** sur le fonds au profit du PNRLR | LF 1988, art. 76 — n° 91/1987, p. 1635 (img) |
| 2011, 2012, 2013 | prélèvements sur le fonds (DL 2011-56, art. 3 ; LFC 2012, art. 36 ; LF 2013, art. 11 vers le fonds national d'amélioration de l'habitat) | seuls les intitulés sont connus (jort_cache) |
| 2026 | interventions étendues (logements et lots sociaux de la SNIT et d'autres opérateurs) | LF 2026, art. 21 — AR n° 148/2025, p. 4235 |

Gestion du fonds : décret 77-965 et ses modificatifs, décret gouv. 2016-1126 (2023, 2026).
Seuls les intitulés sont connus, et ces textes portent sur l'emploi des ressources, non sur le
prélèvement.

## 3. Autres prélèvements sur la masse salariale (signalés)

| Prélèvement | Valeur | Source |
|---|---|---|
| journée de travail au profit du PNRLR, **1987 seulement** | 1 jour de salaire, retenue **salariale** ; exonération des salaires ≤ 1,5 SMIG ; déductible de la CPE | LF 1987, art. 39 — n° 78/1986, p. 1617 (img) ; aucune reconduction en LF 1988 (art. 42-46 : bénéfices seulement) |
| contribution de solidarité (1987) | surtaxe assise notamment sur l'impôt sur les traitements et salaires — relève de la fiscalité | LF 1987, art. 46 — p. 1618 |
| CSS (2018) | voir `docs/notes/css-verification.md` | — |

## 4. Données de rendement : où elles sont

Aucune série n'est construite ici.

- **Tableaux « ت » des lois de finances** (prévisions des ressources des comptes spéciaux du
  Trésor) :
  - dans la LF 2018 (éd. AR, JORT n° 101 du 19 déc. 2017, p. 4295), le FOPROLOS est prévu à
    **38 000 000 D** et le fonds de promotion de la formation et de l'apprentissage à
    **25 000 000 D** ;
  - ce sont des **prévisions de ressources du fonds**, nettes de l'avance pour la TFP (loi
    2007-69, art. 29). Ce ne sont ni le rendement brut du prélèvement ni une réalisation ;
  - des tableaux équivalents existent dans les LF 2016 (n° 105), 2017 (n° 101) et 2019
    (n° 104, AR), repérés par la passe en plein texte. Les LF antérieures à 2016 n'ont pas été
    vérifiées.
- **tunisia-data** (`~/projets/tunisia-data`) :
  - aucune série TFP ou FOPROLOS dans `data/processed` ;
  - `recettes_fiscales_composition_1986_2025.csv` n'isole pas ces prélèvements ; qu'ils y
    soient inclus n'est pas vérifié (depuis 2000, la TFP alimente un compte spécial du Trésor) ;
  - les documents de l'ancien portail du ministère des Finances
    (`data/raw/minfinances/portail_ancien/`) qui les mentionnent sont :
    - `lois_finances/2018_loi_finances_version_finanle_ar_jd1372.pdf` (tableau « ت ») ;
    - `rapports_finances_publiques/2007_rapport_finances_publiques.pdf` et
      `2008_rapport_finances_publiques.pdf` (transferts depuis le FOPROLOS et prêts recouvrés
      — opérations du fonds, pas recette du prélèvement) ;
    - `budget_execution/*` (exécution du budget de l'État ; les comptes spéciaux n'y ont pas
      été cherchés).
- **À chercher** :
  - les lois de règlement du budget (réalisations des fonds spéciaux) ;
  - les rapports annuels de la DGI (`fiscalite/2014_rapport_annuel_dgi_2013_programme_2014_ar.pdf`,
    `2015_rapport_annuel_dgi_2014_programme_2015_ar.pdf`, non lus) ;
  - les budgets du ministère de la formation professionnelle (`budgets_ministeres/`), pour le
    fonds de la formation.

## 5. Références candidates

### 5.1 Entrées déjà présentes (réutiliser la clé)

| Texte | Clé | Fichier |
|---|---|---|
| LF 1987, loi n° 86-106 | `loi86-106-lf1987` | `caisses/references.json` |
| LF 1988, loi n° 87-83 | `loi-87-83-lf-1988` | `precis/fr/references.json` |
| LF 1989, loi n° 88-145 | `loi-88-145-lf-1989` | `fiscalite/references.json` |
| LF 1991, loi n° 90-111 | `lf-1991` (fiscalité) ; `loi-90-111-lf-1991` (prestations) | doublon de clé à signaler au bibliographe |
| LF 2000, loi n° 99-101 | `lf-2000` | fiscalité |
| LF 2003, loi n° 2002-101 | `lf-2003` | fiscalité |
| LF 2006, loi n° 2005-106 | `lf-2006` | fiscalité |
| LF 2008, loi n° 2007-70 | `loi-2007-70-lf-2008` | fiscalité |
| LF 2011, loi n° 2010-58 | `lf-2011` | fiscalité |
| LF 2013, loi n° 2012-27 | `lf-2013` | fiscalité |
| LF 2015, loi n° 2014-59 | `lf-2015` | fiscalité |
| LF 2018, loi n° 2017-66 | `lf-2018` | `precis/fr/references.json` |
| LF 2026, loi n° 2025-17 | `lf-2026` | `precis/fr/references.json` |

Les entrées utilisées par un autre volume doivent être reprises dans
`precis/fr/cotisations_sociales/references.json` (et en AR) si ce volume les cite, en
complétant leur `note` des articles TFP et FOPROLOS ci-dessus.

### 5.2 Entrées à créer (ébauches FR ; l'entrée AR ne diffère que par `URL`)

```json
[
 {"id": "decret-1956-01-12-formation-professionnelle", "type": "legislation",
  "title": "Décret du 12 janvier 1956 (28 djoumada I 1375), relatif à la formation professionnelle",
  "container-title": "Journal officiel tunisien", "issue": "5", "page": "55-59",
  "issued": {"date-parts": [[1956, 1, 12]]},
  "URL": "https://www.pist.tn/jort/1956/1956F/Jo00556.pdf",
  "note": "citation-key: decret-1956-01-12-formation-professionnelle\nJORT n° 5 du 17 janvier 1956. Titre III, art. 27 (p. 58) : institution de la taxe de formation professionnelle ; art. 28 : taux fixé par décret ultérieur. Lu à l'image. Rectificatif : JORT n° 13 du 14 février 1956, p. 204-205 (non lu). URL FR non vérifiée (délai) ; AR : https://www.pist.tn/jort/1956/1956A/Ja00556.pdf (HTTP 200, 5 octobre 2026)."},
 {"id": "loi66-27-code-travail", "type": "legislation",
  "title": "Loi n° 66-27 du 30 avril 1966, portant promulgation du code du travail",
  "container-title": "Journal officiel de la République tunisienne", "issue": "20-22", "page": "716-721, 758-772, 800-814",
  "issued": {"date-parts": [[1966, 4, 30]]},
  "URL": "https://www.pist.tn/jort/1966/1966F/Jo02266.pdf",
  "note": "citation-key: loi66-27-code-travail\nJORT n° 20 (3 mai), 21 (10 mai) et 22 (17 mai 1966). Art. 338 (champ du livre sur la formation professionnelle) et art. 364-365 (taxe de formation professionnelle) au JORT n° 22, p. 806 et 808-809, lus à l'image. Rectificatifs : JORT n° 27 du 21 juin 1966 et n° 37 du 30 août 1966. AR : https://www.pist.tn/jort/1966/1966A/Ja02266.pdf."},
 {"id": "decret66-527", "type": "legislation",
  "title": "Décret n° 66-527 du 24 décembre 1966, modifiant le décret du 16 janvier 1957, fixant le taux, les modalités d'établissement, de recouvrement et de contrôle de la taxe de formation professionnelle et l'affectation de son produit",
  "container-title": "Journal officiel de la République tunisienne", "issue": "55", "page": "1804",
  "issued": {"date-parts": [[1966, 12, 24]]},
  "URL": "https://www.pist.tn/jort/1966/1966F/Jo05566.pdf",
  "note": "citation-key: decret66-527\nJORT n° 55 du 27-30 décembre 1966, p. 1804. Art. 1er : § II nouveau de l'art. 1er du décret du 16 janvier 1957 — taux de 2 %. Art. 2 : effet au 1er janvier 1967. Lu à l'image. AR : https://www.pist.tn/jort/1966/1966A/Ja05566.pdf."},
 {"id": "loi66-79-lf1967", "type": "legislation",
  "title": "Loi n° 66-79 du 29 décembre 1966, portant loi de finances pour la gestion 1967",
  "container-title": "Journal officiel de la République tunisienne", "issue": "55", "page": "1786-",
  "issued": {"date-parts": [[1966, 12, 29]]},
  "URL": "https://www.pist.tn/jort/1966/1966F/Jo05566.pdf",
  "note": "citation-key: loi66-79-lf1967\nJORT n° 55 du 27-30 décembre 1966. Art. 16 (p. 1788) : la TFP est perçue au profit du budget de l'État ; art. 17 : suppression au 1er janvier 1967 de comptes et fonds spéciaux, dont le « Fonds de formation professionnelle ». Lu à l'image. AR : https://www.pist.tn/jort/1966/1966A/Ja05566.pdf."},
 {"id": "loi77-54", "type": "legislation",
  "title": "Loi n° 77-54 du 3 août 1977, portant institution d'un fonds de promotion du logement pour les salariés",
  "container-title": "Journal officiel de la République tunisienne", "issue": "53", "page": "2098-2099",
  "issued": {"date-parts": [[1977, 8, 3]]},
  "URL": "https://www.pist.tn/jort/1977/1977F/Jo05377.pdf",
  "note": "citation-key: loi77-54\nJORT n° 53 du 5-9 août 1977. Art. 1er : tout employeur public ou privé sauf exploitants agricoles privés ; art. 2 : 2 % des salaires soumis à cotisation CNRPS/CNSS/CRPSPEGT, charge déductible ; art. 3 : perception par les caisses ; art. 5 : fonds ; art. 10 : exigible au 1er août 1977. Lu à l'image. AR : https://www.pist.tn/jort/1977/1977A/Ja05377.pdf."},
 {"id": "loi2007-69", "type": "legislation",
  "title": "Loi n° 2007-69 du 27 décembre 2007, relative à l'initiative économique",
  "container-title": "Journal officiel de la République tunisienne", "issue": "104", "page": "4337-4356",
  "issued": {"date-parts": [[2007, 12, 27]]},
  "URL": "https://www.pist.tn/jort/2007/2007F/Jo1042007.pdf",
  "note": "citation-key: loi2007-69\nJORT n° 104 du 28-31 décembre 2007. Art. 24 (art. 47 CII : exonérations TFP/FOPROLOS des petites entreprises, p. 4343) ; art. 27 (avance sur la TFP, crédit d'impôt, p. 4344-4345) ; art. 28-29 (fonds de promotion de la formation, ressource nette de l'avance, p. 4346) ; art. 31 : effet au 1er janvier 2009 ; art. 33 (art. 52 ter CII). Corps du texte sans couche texte : lu par OCR. AR : https://www.pist.tn/jort/2007/2007A/Ja1042007.pdf."},
 {"id": "decret2009-292", "type": "legislation",
  "title": "Décret n° 2009-292 du 2 février 2009, fixant le domaine d'application de l'avance sur la taxe de formation professionnelle, son taux, les conditions et les modalités de son bénéfice, ainsi que le domaine d'application, les modalités et les conditions de bénéfice des droits de tirage",
  "container-title": "Journal officiel de la République tunisienne", "issue": "11", "page": "424-427",
  "issued": {"date-parts": [[2009, 2, 2]]},
  "URL": "https://www.pist.tn/jort/2009/2009F/Jo0112009.pdf",
  "note": "citation-key: decret2009-292\nJORT n° 11 du 6 février 2009. Art. 2 : TFP annuelle ≥ 1 000 D ; art. 3 : taux maximal de l'avance 60 % de la taxe de l'année précédente. Lu (couche texte). AR : https://www.pist.tn/jort/2009/2009A/Ja0112009.pdf."},
 {"id": "decret-gouv2019-228", "type": "legislation",
  "title": "Décret gouvernemental n° 2019-228 du 5 mars 2019, modifiant et complétant le décret n° 2009-292 du 2 février 2009",
  "container-title": "Journal officiel de la République tunisienne", "issue": "21", "page": "785",
  "issued": {"date-parts": [[2019, 3, 5]]},
  "URL": "https://www.pist.tn/jort/2019/2019A/Ja0212019.pdf",
  "note": "citation-key: decret-gouv2019-228\nJORT n° 21 du 12 mars 2019 (éd. AR ; le fichier FR du corpus est l'édition arabe). Récrit les art. 6, 9, 11, 15, 17, 18, 23 du décret 2009-292 ; art. 15 nouveau : droits de tirage plafonnés à 0,6 % de la masse salariale brute pour les entreprises de l'art. 13 bis. Ne touche pas l'art. 3 (60 %). Lu (couche texte AR)."},
 {"id": "dgi-nc-5-2015", "type": "report",
  "title": "Note commune n° 5/2015 — La taxe de formation professionnelle",
  "author": [{"literal": "Direction générale des impôts"}], "issued": {"date-parts": [[2015]]},
  "note": "citation-key: dgi-nc-5-2015\nDoctrine : redevables, exonérations, assiette, taux 1 %/2 %, avance, droits de tirage. Source de repérage ; numéro et date de bulletin à relever sur la pièce."}
]
```

Les LF 1987, 1988, 1989, 2000, 2003, 2006, 2008, 2011, 2013 et 2015 existent déjà (§ 5.1) :
seule leur `note` est à compléter. Pour la LF 2023 (décret-loi n° 2022-79, JORT n° 141 du
23 décembre 2022, AR p. 4074), une clé est à créer seulement si le chapitre la cite, ce qui
n'est pas souhaitable puisqu'elle porte sur des délais.

## 6. Notions à glossaire (`precis/glossaire.yml`, aucune n'existe)

| id proposé | FR | AR | Source canonique |
|---|---|---|---|
| `tfp` | Taxe de formation professionnelle (TFP) | الأداء على التكوين المهني | code du travail, art. 364 ; LF 1989, art. 29-30 |
| `foprolos` | Contribution au fonds de promotion du logement pour les salariés (FOPROLOS) | المساهمة في صندوق النهوض بالمسكن لفائدة الأجراء | loi 77-54, art. 1er-2 ; LF 1989, art. 35 |
| `avance-tfp` | Avance sur la TFP (crédit d'impôt formation) | التسبقة على الأداء على التكوين المهني | loi 2007-69, art. 27 ; décret 2009-292, art. 3 |
| `compte-special-tresor` (vérifier un équivalent) | Fonds spécial (compte spécial) du Trésor | الحسابات الخاصة في الخزينة / صناديق الخزينة | LF 2000, art. 17 ; LF 2018, tableau « ت » |

`masse-salariale` existe déjà (l. 838) : le chapitre peut y renvoyer.

## 7. Lacunes

1. **Taux de la TFP de 1957 à 1966** : le décret du 16 janvier 1957 n'a pas été lu. Le
   corpus local et pist.tn ne servent, pour 1957, que la série ouverte le 26 juillet 1957 :
   le fichier `Jo00157` est daté du 26 juillet 1957 et `Jo00657` du 13 août 1957 ; c'est le
   même fichier sur pist.tn. **Case vide.**
2. **Effet exact des LF 1991, 2000 et 2003** : aucune clause générale n'a été relevée, et la
   date de dépôt au gouvernorat est inconnue. Pour 2003, la date du 1er janvier 2003 vient de
   la NC 10/2003 (doctrine).
3. **Exclusions de l'assiette TFP** (handicapés, emploi à l'étranger) : aucun texte.
4. **Rédaction de l'art. 3 de la loi 77-54** en vigueur après 1989 (anomalie, § 2.2).
5. **Inventaire des exonérations par régime d'incitation** (CII 1993-2016, loi 2017-8, LFC
   2012 et 2015) : non fait, volontairement, en raison du périmètre.
6. **Définition des industries manufacturières** (décret n° 94-492) : non lu.
7. **Séries de rendement** : aucune réalisation trouvée (§ 4).
8. Pages arabes non relevées : décret de 1956, code du travail, loi 77-54, LF 1967, LF 1991,
   LF 2000, LF 2003, loi 2007-69, LF 2008, LF 2011, LF 2013. Les couches texte arabes de
   2007-2013 sont mal encodées : il faut les lire à l'image.

## 8. Fiches RECHERCHE proposées (non versées dans `docs/recherches.yml`)

Avant de proposer ces fiches, `uv run python scripts/recherches.py lister` a été lancé : il
n'existe aucune fiche sur la TFP, le FOPROLOS ou le PNRLR.

```yaml
- id: r-tfp-decret-1957
  objet: décret du 16 janvier 1957 fixant le taux, les modalités et l'affectation de la taxe de formation professionnelle (JORT n° 6 du 18 janvier 1957, p. 79 selon jort_cache), et son taux initial
  ou: cotisations_sociales, futur chapitre « autres prélèvements sur les salaires »
  requetes:
    - {source: titres_fts, terme: '"formation professionnelle" AND taxe'}
  passes:
    - date: 2026-10-05
      resultat: aucun
      couverture: >-
        métadonnées trouvées (recid 107959). Le fascicule de janvier 1957 n'est disponible ni dans
        le corpus local ni sur pist.tn : Jo00657.pdf est le n° 6 du 13 août 1957 (nouvelle série
        républicaine, ouverte le 26 juillet 1957 avec Jo00157), même fichier en ligne (HTTP 200,
        1 760 594 octets). Éditions arabes de 1957 non examinées. Décret 64-234 (complément) lu ;
        décret 66-527 lu (taux 2 % au 1er janvier 1967).
      couvert_jusqu_au: 1957-01-18
- id: r-tfp-exclusions-handicapes-etranger
  objet: texte excluant de l'assiette de la TFP les salaires des handicapés et les rémunérations de l'emploi à l'étranger (cités par la note commune DGI n° 5/2015 sans référence)
  requetes:
    - {source: titres_fts, terme: '"formation professionnelle" AND taxe'}
  passes:
    - date: 2026-10-05
      resultat: aucun
      couverture: >-
        intitulés des textes TFP 1956-2026 de jort_cache parcourus ; textes lus : LF 1989
        art. 29, LF 2003 art. 36, LF 2011 art. 28, LF 2013 art. 21. Non cherchés : loi
        d'orientation n° 2005-83 (handicap), code IRPP/IS (revenus de source étrangère).
      couvert_jusqu_au: 2026-06-19
- id: r-tfp-foprolos-taux-recents
  objet: texte modifiant le taux de la TFP (1 %/2 %) ou de la contribution au FOPROLOS (1 %) après la loi n° 88-145
  requetes:
    - {source: titres_like, terme: "%formation professionnelle%taxe% / %logement%salari% / %التكوين المهني% / %المسكن لفائدة%"}
    - {source: plein_texte, terme: "taxe de formation | logement(s) pour les salari | الأداء على التكوين | النهوض بالمسكن"}
  passes:
    - date: 2026-10-05
      resultat: aucun
      couverture: >-
        plein texte des 40 premières pages des fascicules de LF : 2015 n° 104 (AR scanné, FR
        absent), 2016 n° 105, 2017 n° 101, 2018 n° 104 (FR absent), 2019 n° 104 (FR absent),
        2020 n° 128, 2021 n° 119, 2022 n° 141 (FR absent), 2023 n° 144 (FR absent), 2024
        n° 149 (FR absent), 2025 n° 148. Les éditions AR sans couche texte utile (2015, 2016)
        n'ont pas été lues. Les LFC, et les LF 1990-2014 hors celles citées dans la note, n'ont
        été couvertes que par les intitulés.
      couvert_jusqu_au: 2025-12-12
- id: r-foprolos-art3-redaction
  objet: rédaction de l'art. 3 de la loi n° 77-54 en vigueur après l'art. 38 de la loi n° 88-145 (qui y mettait fin), complétée par la LF 2006 (art. 54) et la LF 2023 (art. 57)
  requetes:
    - {source: titres_fts, terme: '(logement OR logements) AND (salaries OR salarie) AND (fonds OR promotion)'}
  passes:
    - date: 2026-10-05
      resultat: aucun
      couverture: textes du FOPROLOS de 1977 à 2026 dans jort_cache (intitulés) ; lus LF 1989 art. 35-38, LF 1991 art. 48, LF 2006 art. 54, LF 2023 art. 57.
      couvert_jusqu_au: 2026-06-19
```

## 9. Brouillon d'issue `openfisca-tunisia`

> **Titre** : Paramètres de la TFP et de la contribution au FOPROLOS (prélèvements patronaux
> sur les salaires)
>
> Aucun paramètre ni variable ne porte aujourd'hui la TFP ou le FOPROLOS (`grep` sur
> `parameters/` et `variables/`, commit `e8548797` du 2 octobre 2026 ; seul le libellé
> « FOPROLOS » apparaît, dans la `note` de `marche_travail/indemnite_speciale_smi[g|ag].yaml`).
> Le coin social patronal est donc incomplet de 1 à 3 points de masse salariale.
>
> Paramètres proposés, à dater selon `CONTRIBUTING`/AGENTS « Dater » :
> - `prelevements_sociaux/autres/tfp/taux_industries_manufacturieres` : 0,01 au 1989-01-01
>   (loi 88-145, art. 30 ; JORT n° 87/1988, p. 1797) ;
> - `…/tfp/taux_autres_secteurs` : 0,02 au 1967-01-01 (décret 66-527, art. 1-2 ; JORT
>   n° 55/1966, p. 1804) ; 0,02 maintenu en 1989 (loi 88-145, art. 30). Avant 1967 : valeur
>   inconnue, **ne rien poser** ;
> - `…/foprolos/taux` : 0,02 au 1977-08-01 (loi 77-54, art. 2 et 10 ; JORT n° 53/1977,
>   p. 2098-2099) ; 0,01 au 1989-01-01 (loi 88-145, art. 35) ;
> - `…/tfp/avance/taux_max` : 0,60 au 2009-01-01, avec un seuil de 1 000 D (décret 2009-292,
>   art. 2-3 ; loi 2007-69, art. 31).
>
> Variables d'entrée nécessaires : secteur « industries manufacturières » (décret 94-492) ;
> employeur redevable de la TFP (non : État, collectivités, EPA, forfaitaires ; caisses
> sociales depuis 2008) ; exonérations d'incitation. Exclusions d'assiette : primes du FNE
> (2011), gratification de fin de service (2013).
>
> Questions ouvertes : taux de 1957 à 1966 (décret du 16 janvier 1957, introuvable) ;
> régime d'assiette avant 1989 (assiette des cotisations pour le FOPROLOS, art. 2 de la loi
> 77-54).

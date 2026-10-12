# Incitations à l'investissement : crédits de loi de finances avant 2017 — second passage documentaire, 13 octobre 2026

Complément borné à `docs/notes/fiscalite-incitations-primes-zones-2026-10-11.md` (§ 1.2, 1.3, 1.8
et 4.1, point 1) et aux TODO du chapitre `precis/fr/fiscalite/_depenses_fiscales.qmd` (« crédits
budgétaires des primes et des prises en charge » ; « FOPRODI avant 2016 »). Une seule question :
quels crédits les lois de finances ouvrent-elles, de 1995 à 2017, au FOPRODI, aux primes
d'investissement, au FODEC et aux prises en charge de cotisations patronales ?

**Passage échantillonné, non exhaustif** : treize lois de finances lues sur vingt-trois ; ce qui
manque est dit au § 4.

## 0. Nature des chiffres et niveaux de preuve

**Famille : budgétaire** (lois de finances initiales, tableaux annexés, *Journal officiel*).
Aucun rapport extérieur, aucune étude, aucun PIB.

**Ce sont des crédits votés, pas des paiements.** Les lignes du FOPRODI et de la prise en charge
patronale sont des **crédits de programmes** (tableau « D » depuis la loi de finances pour 2005 au
moins ; « F » en 1995), c'est-à-dire l'enveloppe des programmes et projets que la loi autorise
pour l'année — ni crédits d'engagement, ni crédits de paiement, ni exécution. Les lignes du FODEC
sont des **prévisions de recettes** d'un fonds spécial du Trésor (les dépenses du fonds leur sont
égales par construction du tableau). **Ne rien présenter comme une somme versée, et ne raccorder
ces valeurs à aucune série postérieure** (rapports sur les avantages financiers 2018-2023, flux du
FOPRODI à la BCT 2016-2025).

Niveaux de preuve :

- **image** : page ou bande de page rendue (`pdftoppm`, 110 à 160 points par pouce) et lue à l'image ;
- **texte** : couche texte du fascicule (`pdftotext -layout`), fascicules de décembre 2008 et de
  2010 à 2016, dont la couche texte porte les chiffres des tableaux ;
- **texte arabe** : couche texte de l'édition arabe (loi de finances pour 2016, l'édition
  française du JORT n° 104 de 2015 étant absente du corpus et de pist.tn) ;
- **OCR de repérage** : `tesseract` sur les seules pages des tableaux, pour trouver la page ;
  **aucune valeur de cette note ne repose sur lui**. Il s'est trompé deux fois sur trois
  contrôles : FOPRODI 2010 lu « 22 000 000 » pour 42 000 000 ; prise en charge patronale 2005 lue
  « 1 800 000 » pour 18 000 000.

Les fascicules sont ceux du corpus local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/`. Numéro
et date de fascicule et page sont lus au pied de page (image ou texte), sauf mention « page
déduite » (décalage constant depuis une page lue du même fascicule). Numéro et date de la loi :
lus au fascicule pour les lois n° 94-127, 2006-85, 2007-70, 2008-76, 2008-77 et 2014-59 ; repris
de la notice de `jort_cache.db` pour les autres (à contrôler avant citation, § 3 bis de
`docs/notes/outillage-sources.md`). **Aucune adresse pist.tn n'a été contrôlée à ce passage.**

## 1. Le constat de nomenclature, qui commande tout le reste

1. **Le FOPRODI ne figure pas au tableau des fonds spéciaux du Trésor**, ni en 1995 (tableau
   « K », 19 comptes — image), ni en 2005 (tableau « B », 20 comptes — image), ni de 2011 à 2017
   (tableau « B » — texte). Le tableau des fonds spéciaux n'est donc **pas** la source de la série.
2. **Depuis 2000 au moins, le FOPRODI est une ligne du tableau des crédits de programmes de l'État**, au chapitre du
   ministère chargé de l'industrie, sous la rubrique « II - Financement public » : « Fonds de
   promotion et de décentralisation industrielle », un montant, sans détail (lu de 2000 à 2017).
   C'est cohérent avec la colonne « dotations budgétaires » du tableau de la BCT (note du
   11 octobre, § 1.2) : le fonds est alimenté par une dotation du budget, non par une recette
   affectée.
3. **La prise en charge des cotisations patronales a sa ligne propre**, dans le même tableau, au
   chapitre du ministère des Affaires sociales : « Prise en charge par l'État de la contribution
   patronale au régime légal de la sécurité sociale » — « projets nouveaux à caractère national »
   en 1995, « II/ Financement public » à partir de 2000. La ligne ne dit pas au titre de quel
   régime (code de 1993, art. 25 et 25 bis ; dispositifs d'emploi) : **elle ne s'attribue pas au
   seul code d'incitations aux investissements**.
4. **Aucun « fonds des primes d'investissement » ni « fonds de développement régional » distinct
   n'apparaît** dans les tableaux des fonds spéciaux lus (1995, 2005, 2011-2017).
5. **Le FODEC est un fonds spécial du Trésor à ligne unique** (« Fonds de développement de la
   compétitivité industrielle », institué par la loi n° 94-127, dont la notice situe les dispositions aux p. 2045-2046, article
   non lu ; l'intitulé « … dans les secteurs industriel, de services et de l'artisanat » apparaît
   au tableau de la loi de finances complémentaire pour 2013, entre celui de la loi de finances
   pour 2013 et celui pour 2014). Son tableau **ne distingue pas** de primes à
   l'investissement : hors du périmètre demandé ; les valeurs relevées au passage sont au § 2.3,
   pour mémoire.
6. **Lettres des tableaux.** Loi de finances pour 1995 : « K » = fonds spéciaux (recettes — dont
   subvention du budget et recettes propres — et dépenses) ; « F » = crédits de programme du
   budget de l'État (p. 2095 à 2119 ; titre lu par OCR de repérage, p. 2095). Loi de finances pour
   2000 : « B » = dépenses du budget, crédits de paiement (p. 2757 — image) ; le tableau des
   crédits de programmes commence p. 2759 (lettre « C » d'après l'OCR de repérage, non relue à
   l'image) ; **le tableau des fonds spéciaux de 2000 n'a pas été localisé**. Lois de finances pour
   2005 à 2017 : « A » recettes, « B » fonds spéciaux (recettes seules), « C » dépenses en crédits
   de paiement, « D » crédits de programmes, « E » crédits d'engagement, « F » établissements
   publics rattachés pour ordre (articles 1er à 7 de la loi n° 2014-59 — texte ; titres « B » de
   2005 — image ; titres « A » à « D » de 2007, 2008, 2009, 2010 — OCR de repérage). Édition
   arabe pour 2016 : « ب » fonds spéciaux, « ث » crédits de programmes (texte arabe).

## 2. Les crédits, année par année

### 2.1 FOPRODI — crédits de programmes de la loi de finances initiale (millions de dinars)

| Loi de finances pour | Crédit (MD) | Loi | JORT n°, date | Page | Mode de lecture |
|---|---:|---|---|---|---|
| 1995 | **pas de ligne** aux chapitres lus | n° 94-127 du 26 décembre 1994 | n° 103, 30-31 décembre 1994 | tableau « F », p. 2100 | image : les chapitres 11 (Économie nationale, total 474 000 D) et 12 (Plan et développement régional, 205 000 D) ne portent aucune ligne du fonds ; reste du tableau (p. 2095-2119) : OCR de repérage muet |
| 1996 à 1999 | non lu | | | | |
| 2000 | **13,0** | n° 99-101 du 31 décembre 1999 | n° 105, 31 décembre 1999 | p. 2775 | image |
| 2001 à 2004 | non lu | | | | |
| 2005 | **37,0** | n° 2004-90 du 31 décembre 2004 | n° 105, 31 décembre 2004 | p. 3471 | image |
| 2006 | non lu | n° 2005-106 du 19 décembre 2005 | n° 101 de 2005 | | |
| 2007 | **35,0** | n° 2006-85 du 25 décembre 2006 | n° 103, 26 décembre 2006 | p. 4417 | image (page : pied lu par OCR, recoupé par décalage) |
| 2008 | **35,0** | n° 2007-70 du 27 décembre 2007 | n° 104, 28-31 décembre 2007 | p. 4392 | image |
| 2008, loi de finances complémentaire | 35,0, « sans changement » | n° 2008-76 du 15 décembre 2008 | n° 101, 16 décembre 2008 | p. 4176 | texte |
| 2009 | **42,0** | n° 2008-77 du 22 décembre 2008 | n° 104, 26 décembre 2008 | p. 4306 | image (page : pied lu par OCR, recoupé par décalage) |
| 2010 | **42,0** | n° 2009-71 du 21 décembre 2009 | n° 102, 22 décembre 2009 | p. 3957 | image |
| 2011 | **48,0** | n° 2010-58 du 17 décembre 2010 | n° 102, 21 décembre 2010 | p. 3526 | texte |
| 2012 | **58,0** | n° 2011-7 du 31 décembre 2011 | n° 1, 3 janvier 2012 | p. 39 | texte (le montant est sur la ligne intercalée entre les deux moitiés du libellé) |
| 2013 | **65,0** | n° 2012-27 du 29 décembre 2012 | n° 1, 1er janvier 2013 | p. 55 | texte |
| 2014 | **65,0** | n° 2013-54 du 30 décembre 2013 | n° 105, 31 décembre 2013 | p. 3732 | texte ; voir réserve (a) |
| 2015 | **55,0** | n° 2014-59 du 26 décembre 2014 | n° 105, 30 décembre 2014 | p. 3507 | texte |
| 2016 | **55,0** | n° 2015-53 du 25 décembre 2015 | n° 104, 29 décembre 2015 (édition arabe) | p. 3660 de l'édition arabe | texte arabe (« صندوق التطوير واللامركزية الصناعية ») |
| 2017 | **49,0** | n° 2016-78 du 17 décembre 2016 | n° 105, 27 décembre 2016 | p. 3889 | texte |

Réserves :

- (a) **2014** : la couche texte porte deux lignes successives, « Fonds de Promotion et de
  Décentralisation Industrielle 66 592 000 » puis « -Fonds de Promotion et de Décentralisation
  Industrielle 65 000 000 ». Dans les tableaux pour 2015 et 2017, la ligne de tête et la ligne de
  détail portent le même montant ; ici elles diffèrent de 1,592 MD. Lecture probable, non
  établie : un décalage de la couche texte (le total de tête d'une autre rubrique). **À relire à
  l'image, p. 3732, avant publication.**
- (b) **Valeurs « texte » de 2011 à 2017** : non relues à l'image. Elles sont nettes (une ligne,
  un montant), mais la règle du projet demande la relecture à l'image de tout chiffre de tableau.
- (c) **Constat de contrôle, pas un raccord** : le crédit de programmes pour 2017 (49,0 MD) est
  égal à la « dotation budgétaire » de 2017 du tableau de la BCT (49,00 MD, note du 11 octobre,
  § 1.2) ; celui pour 2016 (55,0 MD) ne l'est pas (47,00 MD à la BCT). Les deux grandeurs ne sont
  donc pas interchangeables.
- (d) Les lois de finances rectificatives ou complémentaires ne sont pas relevées, sauf celle de
  décembre 2008, rencontrée au passage.

Lecture brute, pour le rédacteur : le crédit ouvert au FOPRODI passe de 13 MD (2000) à 35-37 MD
(2005-2008), puis monte à 42, 48, 58 et 65 MD (2010 à 2013-2014), et redescend à 55 puis 49 MD
(2015-2017). En dinars courants ; treize points sur dix-huit années, les trous sont dits.

### 2.2 Prise en charge par l'État de la contribution patronale au régime légal de sécurité sociale — crédits de programmes, chapitre du ministère des Affaires sociales (millions de dinars)

| Loi de finances pour | Crédit (MD) | Loi | JORT n°, date | Page | Rubrique du tableau | Mode de lecture |
|---|---:|---|---|---|---|---|
| 1995 | **3,0** | n° 94-127 | n° 103, 30-31 décembre 1994 | p. 2115 | tableau « F », « 3) Projets nouveaux — B. Projets à caractère national » | image |
| 2000 | **5,5** | n° 99-101 | n° 105, 31 décembre 1999 | p. 2791 | « II/ Financement public » | image |
| 2005 | **18,0** | n° 2004-90 | n° 105, 31 décembre 2004 | p. 3488 | tableau « D », « II/ Financement public » (total II : 18,038 MD) | image |
| 2007 | **35,0** | n° 2006-85 | n° 103, 26 décembre 2006 | p. 4437 | idem (total II : 35,036 MD) | image (page : pied lu par OCR, recoupé par décalage) |
| 2008 | **35,0** | n° 2007-70 | n° 104, 28-31 décembre 2007 | p. 4410 | idem (total II : 35,075 MD) | image |
| 2009 | **35,0** | n° 2008-77 | n° 104, 26 décembre 2008 | p. 4325 | idem (total II : 42,390 MD, avec 7,390 MD pour l'Office des Tunisiens à l'étranger) | image |
| 2010 à 2017 | **non cherché** | | | | | la ligne n'a pas été cherchée dans les tableaux « D » de ces années |

Années 1996-1999, 2001-2004, 2006 : non lues. La ligne existe donc dès la loi de finances pour
1995 — deuxième exercice du code de 1993 —, alors rangée parmi les « projets nouveaux », et sous
« Financement public » à partir de 2000 : 3,0 MD pour 1995, 35,0 MD pour 2007 à 2009, en dinars
courants, sans que les deux rubriques soient nécessairement de même nature. Rappel : crédit voté, tous régimes de prise en charge confondus ; rien
ne dit ce qui a été payé à la CNSS (note du 11 octobre, § 1.8).

### 2.3 FODEC — pour mémoire (hors périmètre : ligne unique, sans distinction des primes)

Prévisions de recettes du fonds au tableau des fonds spéciaux du Trésor, en millions de dinars :

| Loi de finances pour | Recettes prévues (MD) | Tableau, page | Mode de lecture |
|---|---:|---|---|
| 1995 | 20,0 (recettes propres ; subvention du budget : néant ; dépenses : 20,0) | « K », JORT n° 103 de 1994, p. 2126 | image |
| 2005 | 45,0 | « B », JORT n° 105 de 2004, p. 3450 | image |
| 2008, loi complémentaire | 67,0 | « B », JORT n° 101 de 2008, p. 4171 (page déduite) | texte |
| 2011 | 71,0 | « B », JORT n° 102 de 2010, p. 3482 | texte |
| 2012 | 74,0 | « B », JORT n° 1 de 2012, p. 16 | texte |
| 2013 | 74,0 | « B », JORT n° 1 de 2013, p. 33 | texte |
| 2013, loi complémentaire | 58,0 | « B », JORT n° 102 du 24 décembre 2013, p. 3572 (numéro de la loi non relevé) | texte |
| 2014 | 65,0 | « B », JORT n° 105 de 2013, p. 3704 | texte |
| 2015 | 75,0 | « B », JORT n° 105 de 2014, p. 3478 | texte |
| 2016 | 55,0 | « ب », JORT n° 104 de 2015, édition arabe, p. 3628 (page déduite) | texte arabe |
| 2017 | 74,0 | « B », JORT n° 105 de 2016, p. 3856 | texte |

Totaux des fonds spéciaux lus au passage : 590,7 MD pour 1995 (dont 420,7 de subvention du budget
et 170,0 de recettes propres — image ; art. 10 de la loi — texte) ; 511,0 MD pour 2005 (image) ;
920,1 MD pour 2012 ; 952,8 MD pour 2014 ; 954,8 MD pour 2015 (texte).

Composition du tableau « K » pour 1995 (image, p. 2126), utile à d'autres chapitres : Fonds de
solidarité nationale 40,0 ; compte d'emploi des frais de contrôle financier 0,5 ; fonds commun des
collectivités publiques locales 109,0 ; fonds du service national 9,0 ; fonds d'exercice du droit
de préemption — ; fonds de la garantie automobile 0,6 ; cautionnement mutuel des comptables
publics 0,1 ; **Caisse générale de compensation 243,0 (dont subvention du budget 215,0)** ; fonds
de promotion des exportations 10,3 ; FODEC 20,0 ; fonds de restructuration du capital des
entreprises publiques 35,0 ; fonds de développement de la compétitivité dans l'agriculture et la
pêche 6,0 ; fonds national d'amélioration de l'habitat 12,9 ; FOPROLOS 43,0 ; fonds de dépollution
5,0 ; fonds de protection des zones touristiques 5,0 ; compte national de solidarité sociale
42,8 ; fonds des accidents du travail — ; fonds national de promotion des sports et de la
jeunesse 8,5.

## 3. Ce que cela change pour le chapitre

- Le TODO de la ligne 597 (« tableaux « ب » des fonds du Trésor ») vise le mauvais tableau pour le
  FOPRODI et pour les prises en charge : ce sont les **tableaux des crédits de programmes** (« D »
  / « ث ») qu'il faut dépouiller, chapitres de l'industrie et des affaires sociales.
- Une série de **crédits** du FOPRODI est constituable de 2000 à 2017, et de la prise en charge
  patronale de 1995 à 2009 au moins ; elle reste trouée (§ 4) et ne vaut pas « sommes versées » :
  la phrase du chapitre « aucune série de sommes versées n'est établie ici pour les exercices
  antérieurs à 2016 » **demeure exacte**.
- Les primes d'investissement de l'agriculture (APIA, fonds spécial de développement agricole), du
  tourisme et de l'artisanat (FONAPRA) n'ont pas été cherchées : mêmes tableaux, autres chapitres.

## 4. Ce qui n'est pas établi, et la suite précise

1. **FOPRODI, loi de finances pour 1995** : le tableau « F » de 1995 ne liste que réévaluations
   et projets nouveaux, sans rubrique « Financement public » ; les chapitres de l'Économie
   nationale et du Plan (p. 2100 — image) n'ont pas de ligne du fonds. Où la dotation du fonds est
   inscrite en 1995 (tableau « I » ou « I bis » des crédits du titre II, p. 2122-2125 d'après le
   repérage ?) n'est pas établi : c'est la première lecture à faire, elle dira à partir de quelle
   année la ligne « Financement public » existe. La loi de finances pour 1994 (loi n° 93-125,
   JORT n° 100 de 1993), première année demandée, n'a pas été ouverte.
2. **Années non ouvertes** — fascicules du corpus (édition française), tous à lire à l'image :
   pour 1996, JORT n° 104 de 1995 (loi n° 95-109) ; 1997, n° 105 de 1996 (n° 96-113) ; 1998,
   n° 104 de 1997 (n° 97-88) ; 1999, n° 104 de 1998 (n° 98-111) ; 2001, n° 104 de 2000
   (n° 2000-98) ; 2002, n° 104 de 2001 (n° 2001-123) ; 2003, n° 102 de 2002 (n° 2002-101) ; 2004,
   n° 104 de 2003 (n° 2003-80) ; 2006, n° 101 de 2005 (n° 2005-106). Numéros de fascicule d'après
   les notices, non contrôlés au pied de page. Méthode qui a marché : OCR des seules pages du
   tableau des crédits de programmes (une minute par fascicule), recherche de « centralisation »
   et de « patronale », puis lecture à l'image d'une bande de la page.
3. **Prise en charge patronale 2010-2017** : chercher « patronale » dans les tableaux « D » déjà
   localisés (couche texte de 2010 à 2016 ; image pour le JORT n° 102 de 2009).
4. **Tableau des fonds spéciaux de 2000** et des années 1996-2004 : non localisé ; lettre du
   tableau des crédits de programmes de 2000 à relire à l'image (p. 2759).
5. **Relecture à l'image** des valeurs « texte » de 2011 à 2017, et de la double ligne de 2014.
6. **Lois de finances complémentaires** (2011 à 2015 notamment) : non relevées.
7. **Exécution** : lois de règlement, toujours non ouvertes (note du 11 octobre, § 4.1, point 1).
8. **1985-1993** : non abordé (le budget d'appels n'a pas permis l'extension prévue « si le temps
   le permet »).

## 5. Fiches de recherche

Aucune fiche de `docs/recherches.yml` n'est touchée : ce passage transcrit des tableaux, il ne
cherche pas un texte introuvable. `uv run python scripts/recherches.py lister` ne porte aucune
fiche sur le FOPRODI ni sur les crédits des incitations. Aucune passe à inscrire ; les trois
fiches `r-fisc-*` de la note du 11 octobre (dont deux marquées « périmée » ce jour) n'ont pas été
relancées. Seul constat de corpus à reporter, déjà connu de `docs/notes/outillage-sources.md`
(§ 3) : l'édition française du JORT n° 104 de 2015 est absente — la loi de finances pour 2016 se
cite donc sur l'édition arabe, pagination arabe.

## 6. Références candidates

Présence dans `precis/fr/fiscalite/references.json` **non vérifiée à ce passage** (bibliographe).
Entrées de type `legislation`, clés suggérées : `loi-94-127-lf-1995`, `loi-99-101-lf-2000`,
`loi-2004-90-lf-2005`, `loi-2006-85-lf-2007`, `loi-2007-70-lf-2008`, `loi-2008-76-lfc-2008`,
`loi-2008-77-lf-2009`, `loi-2009-71-lf-2010`, `loi-2010-58-lf-2011`, `loi-2011-7-lf-2012`,
`loi-2012-27-lf-2013`, `loi-2013-54-lf-2014`, `loi-2014-59-lf-2015`, `loi-2015-53-lf-2016`,
`loi-2016-78-lf-2017` ; numéros, dates et fascicules au § 2.1. Adresses pist.tn à construire par
la convention et à contrôler (type de contenu, taille, langue du fichier servi).

## 7. Notions à glossaire (à vérifier dans `precis/glossaire.yml`)

- **crédits de programmes** (اعتمادات البرامج) — distincts des crédits d'engagement et de
  paiement ; source canonique pressentie : loi organique du budget (non lue ici) ;
- **fonds spéciaux du Trésor** (الحسابات الخاصة في الخزينة ; à vérifier) ;
- **FOPRODI** (صندوق التطوير واللامركزية الصناعية, graphie du tableau « ث » pour 2016) ;
- **FODEC**, sous ses deux intitulés.

## 8. Journal et outillage

Scripts de ce passage, hors dépôt, dans
`/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/lf/` :
`grepf.py` et `grep2.py` (recherche du libellé dans la couche texte, avec pied de page),
`ocr.sh` (OCR de repérage d'une plage de pages), `band.py` (découpe de la bande d'une page autour
d'une ligne repérée, pour lecture à l'image). Un premier repérage par OCR du bandeau haut des
pages (fascicule de 1994, 162 pages) a débordé le délai de la commande et s'est achevé en
arrière-plan ; aucun processus ne tourne en fin de passage.

## 9. Annexe — relevé automatique de la ligne « contribution patronale », lois de finances pour 2010 à 2017

Relevé par script sur la couche texte (ou l'OCR de repérage pour 2010), ajouté en fin de passage : **lignes brutes, non relues à l'image et non reportées au tableau du § 2.2**. À relire avant tout emploi.

- LF 2011, `2010/fr/Jo1022010.pdf`, page-fichier 109, pied « N° 102 Journal Officiel de la République Tunisienne — 21 décembre 2010 Page 3565 » : II- Financement Public ⏎ - Prise en charge par l'Etat de la contribution patronale au ⏎ régime légal de la sécurité sociale  44 000 000 ⏎ - Office des Tunisiens à l'Etranger  217 000
- LF 2012, `2012/fr/Jo0012012.pdf`, page-fichier 59, pied « N° 1 Journal Officiel de la République Tunisienne — 3 janvier 2012 Page 59 » : * Caisse Nationale de la Sécurité Sociale  59 000 000 ⏎ - Prise en charge par l'Etat de la contribution patronale au ⏎ régime légal de la sécurité sociale  55 000 000 ⏎ - Délivrance de la Caisse Nationale de la Sécurité Sociale  4
- LF 2013, `2013/fr/Jo0012013.pdf`, page-fichier 78, pied « Page 78 Journal Officiel de la République Tunisienne — 1er janvier 2013 N° 1 » : * Caisse Nationale de la Sécurité Sociale  64 000 000 ⏎ - Prise en charge par l'Etat de la contribution patronale au régime ⏎ 60 000 000 ⏎ légal de la sécurité sociale
- LF 2014, `2013/fr/Jo1052013.pdf`, page-fichier 109, pied « N° 105 Journal Officiel de la République Tunisienne — 31 décembre 2013 Page 3761 » : Caisse Nationale de la Sécurité Sociale  58 050 000 ⏎ -Prise en charge par l’Etat de la contribution patronale au régime  54 000 000 ⏎ légal de la sécurité sociale  4 000 000 ⏎ -Equipements divers  30 000
- LF 2015, `2014/fr/Jo1052014.pdf`, page-fichier 74, pied « Page 3534 Journal Officiel de la République Tunisienne — 30 décembre 2014 N° 105 » : Prise en charge par l'Etat de la contribution ⏎ patronale au régime légal de la sécurité sociale  47 429 000 ⏎ Règlement de la CNSS  4 000 000
- LF 2016, `2015/ar/Ja1042015.pdf`, page-fichier 96, pied « ‫ﻋـــﺪد ‪104‬‬ ‫اﻟﺮاﺋﺪ اﻟﺮﺳﻤﻲ ﻟﻠﺠﻤﻬﻮرﻳﺔ اﻟﺘﻮﻧﺴﻴﺔ –– ‪ 29‬دﻳﺴﻤﺒﺮ ‪2015‬‬ ‫ﺻﻔﺤــﺔ ‪3688‬‬ » : ‫‪120 788 000‬‬  ‫اﻟﺼﻨﺪوق اﻟﻮﻃﻨﻲ ﻟﻠﻀﻤﺎن اﻻﺟﺘﻤﺎﻋﻲ‬ ⏎ ‫‪41 788 000‬‬  ‫ﺗﻜﻔﻞ اﻟﺪوﻟﺔ ﺑﻤﺴﺎﻫﻤﺔ اﻷﻋﺮاف ﻓﻲ اﻟﻨﻈﺎم اﻟﻘﺎﻧﻮﻧﻲ‬ ⏎ ‫ﻟﻠﻀﻤﺎن اﻹﺟﺘﻤﺎﻋﻲ‬ ⏎ ‫‪4 000 000‬‬  ‫ﺧﻼص اﻟﺼﻨﺪوق اﻟﻮﻃﻨﻲ ﻟﻠﻀﻤﺎن اﻹﺟﺘﻤﺎﻋﻲ‬
- LF 2017, `2016/fr/Jo1052016.pdf`, page-fichier 97, pied « N° 105 Journal Officiel de la République Tunisienne — 27 décembre 2016 Page 3921 » : Caisse nationale de la sécurité nationale  41 105 000 ⏎ Prise en charge par l’Etat de la contribution patronale au ⏎ 37 105 000 ⏎ régime légal de la sécurité sociale
- LF 2010, OCR de repérage des p. 26-80 du JORT n° 102 de 2009 (aucune valeur à en tirer) : aucune occurrence

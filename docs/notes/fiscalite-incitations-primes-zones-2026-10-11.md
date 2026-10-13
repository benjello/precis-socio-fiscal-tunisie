# Incitations à l'investissement : primes, zones, sommes versées — note documentaire du 11 octobre 2026

Compléments au chapitre `precis/fr/fiscalite/_depenses_fiscales.qmd`. La note
`docs/notes/fiscalite-depenses-fiscales.md` reste la référence pour l'histoire des régimes et
le coût fiscal ; rien n'en est refait ici. Cette note répond à six demandes : (1) sommes
versées, (2) barème des primes de la loi n° 2016-71, (3) zones de développement régional,
(4) statistiques publiques sur le régime de l'exportation, (5) loi n° 2019-47, (6) coût des
prises en charge de cotisations patronales.

## 0. Niveaux de preuve employés

- **image** : page rendue et lue à l'image (outil de lecture, paramètre `pages`) ;
- **texte** : couche texte du PDF (`pdftotext`), sans relecture à l'image — suffisant pour la
  prose d'un décret, **insuffisant pour un chiffre de tableau** tant qu'il n'est pas recoupé ;
- **texte décodé** : couche texte à police décalée de 29 rangs, décodée (JORT n° 20 de 1999) ;
- **intitulé** : connu par la seule notice de `jort_cache.db`.

Les fascicules sont ceux du corpus local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/` ; les
adresses `pist.tn` citées au § 2 ont été contrôlées le 11 octobre 2026 (`curl -k`, code 200,
`application/pdf`).

**Familles de chiffres.** Tout le § 1.1 est **budgétaire et ministère des Finances**
(paiements déclarés). Le § 1.2 est **comptable** (états financiers de la BCT, teneur de compte
du FOPRODI). Le § 1.4 est **statistique publique** (INS). Aucune étude extérieure n'est
ajoutée ici. Aucun ratio au PIB n'est calculé dans cette note.

---

## 1. Ce qui est établi

### 1.1 Les avantages financiers versés, exercices 2018 à 2023 — cinq rapports, pas une série

**Source.** Ministère des Finances, rapport sur les dépenses fiscales et les avantages
financiers annexé aux projets de loi de finances 2021 à 2025, deuxième partie (clé existante
`gbo-depenses-fiscales`). Fichiers : `~/projets/tunisia-data/data/raw/gbo/depenses_fiscales_LF20{21..25}.pdf`.
Les cinq éditions sont au dépôt (les éditions 2022 et 2023, « non collectées » d'après la note
du 5 octobre, y sont depuis le 6 octobre ; la fiche de source ne les portait pas — complétée,
§ 5). **Aucun rapport annexé au projet de loi de finances pour 2026 ne figure** à la rubrique
du portail (`http://www.gbo.tn/ar/taxonomy/term/121`, relue le 11 octobre 2026 : cinq PDF,
déposés en 2021-04, 2022-01, 2023-01, 2024-01, 2025-03) ; la page « loi de finances » de
`finances.gov.tn` (`/ar/loi_finance` et `/fr/loi_finance`, lues le même jour dans leur vue par
défaut) range sous la rubrique du rapport l'édition de 2024, et son seul fichier de 2026 est
la loi de finances pour 2026 elle-même (`/sites/default/files/2026-01/115725.pdf`, 101 p.) ;
une recherche web n'a rendu aucune adresse du rapport. Les vues par année de cette page n'ont
pas été parcourues : **non trouvé, non exclu**.

**Méthode du rapport** (rapport 2021, deuxième partie, section 2, p. 88-90 imprimées — texte) :
les montants sont ceux que transmettent « les structures administratives chargées de l'octroi
et du contrôle de ces avantages ». Pour une prime, la valeur est « le montant engagé à ce
titre » ; pour un prêt, une dotation remboursable ou une participation, le rapport distingue le
*volume* de l'intervention de son *coût* et dit ne pas savoir mesurer le second. Le rapport
2022 (p. 69 — image) précise que les montants sont ceux « effectivement versés au bénéficiaire
ou portés en dette de l'État envers les organismes concernés, dans le cas de la prise en charge
de la contribution patronale ou salariale » ; pour la formation et l'emploi, ce sont les
montants **engagés**.

**Trois ruptures, à dire avant tout chiffre :**

1. **Exercice 2019 révisé de 932 à 922,7 MD** par le rapport 2022 (p. 69, note 1 — image) :
   l'avantage codé 10801 (« prime d'investissement », tourisme) passe de 10,867 MD à 0.
2. **À partir du rapport 2023, prêts, dotations remboursables et participations au capital
   sortent du total**, « parce qu'ils représentent le volume de l'intervention publique et non
   le coût réel supporté par l'État » (rapport 2023, p. 69 du PDF, 68 imprimée — image).
   L'exercice 2020 passe ainsi de 701,8 MD (rapport 2022) à 631,7 MD (rapport 2023), puis
   628,0 MD (rapport 2024). **Les totaux d'avant et d'après ne se comparent pas** : en 2019,
   prêts et participations pesaient 118,7 MD.
3. **Le nombre d'avantages recensés bouge** : 232 (rapports 2021 et 2022), 227 (2023), 236
   (2024). En 2020, 58 seulement ont donné lieu à un versement (rapport 2022, p. 69) ; 95 en
   2021 et en 2022 (rapports 2023 et 2024).

**Tableau A — total et répartition par forme, une colonne par rapport** (millions de dinars).
Lecture : image pour les rapports 2022 à 2025 ; texte pour le rapport 2021 (tableau n° 5,
p. 96 imprimée).

| Forme | 2018 (R21) | 2019 (R21) | 2019 (R22) | 2020 (R22) | 2020 (R23) | 2020 (R24) | 2021 (R23) | 2021 (R25) | 2022 (R24) | 2022 (R25) | 2023 (R25) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Primes | 517,7 | 551,5 | 540,6 | 415,0 | 414,6 | 414,6 | 456,6 | 456,6 | 384,0 | 386,0 | 375,2 |
| Prise en charge de dépenses par l'État, totale ou partielle | 169,0 | 195,6 | 195,6 | 146,2 | 146,2 | 142,4 | 96,2 | 99,9 | 116,0 | 115,9 | 88,0 |
| Prise en charge de la contribution patronale de sécurité sociale | 181,9 | 54,0 | 55,1 | 62,4 | 62,4 | 62,4 | 65,9 | 65,9 | 39,0 | 39,0 | 43,3 |
| Prise en charge de la cotisation des salariés | 11,7 | 12,8 | 12,8 | 8,5 | 8,5 | 8,5 | 0 | 0 | 4,5 | 4,5 | 4,1 |
| Prêts et dotations remboursables | 9,7 | 114,7 | 114,7 | 69,3 | hors total | hors total | hors total | hors total | hors total | hors total | hors total |
| Participations au capital | 2,9 | 4,0 | 4,0 | 0,3 | hors total | hors total | hors total | hors total | hors total | hors total | hors total |
| Garanties de prêts | 20,0 | 0 | 0 | 0 | 0 | 0 | 23,0 | 23,0 | 0 | 0 | 10,0 |
| **Total publié** | **913** | **932** | **922,7** | **701,8** | **631,7** | **628,0** | **641,7** | **645,5** | **543,5** | **545,5** | **520,7** |

Sources : R21 = rapport annexé au PLF 2021, tableau n° 5 (p. 96 imprimée) ; R22 = PLF 2022,
tableau n° 4 (p. 73) ; R23 = PLF 2023, tableau n° 4 (p. 74 du PDF, 73 imprimée) ; R24 = PLF
2024, tableau n° 4 (p. 72 du PDF, 71 imprimée) ; R25 = PLF 2025, tableau n° 4 (p. 55). Le
rapport 2021 dit lui-même que le total de 2019 comprend « près de 119 MD sous forme de prêts,
de crédits et d'apports en capital » (p. 92).

**Tableau B — répartition par domaine** (millions de dinars ; mêmes rapports, tableau n° 2 :
R21 p. 93 ; R22 p. 71 ; R23 p. 71 du PDF ; R24 p. 69 du PDF ; R25 p. 52).

| Domaine | 2018 (R21) | 2019 (R21) | 2019 (R22) | 2020 (R22) | 2020 (R24) | 2021 (R25) | 2022 (R25) | 2023 (R25) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Formation et emploi | 344,0 | 379,1 | 379,1 | 332,8 | 332,8 | 285,7 | 263,2 | 255,9 |
| Investissement (loi de 2016 et code de 1993 en extinction) | 242,9 | 186,5 | 186,1 | 158,9 | 150,1 | 160,8 | 91,9 | 108,4 |
| Industrie et services (mise à niveau surtout) | 177,0 | 146,3 | 146,3 | 34,5 | 30,4 | 45,8 | 36,8 | 37,3 |
| Petits métiers, petits projets | 0 | 111,7 | 100,8 | 60,8 | (*) | 34,6 (**) | 38,3 (**) | 43,7 (**) |
| Commerce (promotion des exportations) | 48,6 | 48,5 | 48,5 | 40,5 | 40,5 | 41,9 | 76,5 | 50,9 |
| Agriculture et pêche | 59,1 | 39,4 | 39,4 | 51,4 | 51,4 | 42,7 | 35,9 | 33,5 |
| Énergie et énergies renouvelables | 19,0 | 17,9 | 17,9 | 16,0 | 16,0 | 32,3 | 22,0 | 11,6 |
| Technologies de l'information | 0,3 | 0,9 | 2,1 | 6,5 | 6,5 | 13,2 | 18,9 | 13,0 |

(*) La ligne disparaît du tableau n° 2 à partir du rapport 2023 (prêts sortis du total).
(**) « Financement des petits projets », lu au tableau détaillé du rapport 2025, p. 57 : la
ligne y est imprimée mais **n'entre pas dans le total** — les autres lignes somment à 520,7 MD
en 2023 et à 645,5 MD en 2021, totaux publiés ; avec elle on aurait 564,4 et 680,0. Lecture
probable, non dite par le rapport : ce sont des prêts, sortis du total depuis le rapport 2023.

**Tableau C — le domaine « investissement », par programme** (millions de dinars).

| Programme | 2018 | 2019 | 2020 | 2021 | 2022 (R24) | 2022 (R25) | 2023 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Secteurs prioritaires | 15,5 | 32,5 | 19,9 | 29,4 | 15,4 | 12,9 | 17,3 |
| Prime de performance économique (investissements matériels et immatériels, agriculture surtout) | 46,2 | 69,7 | 40,8 | 58,8 | 25,5 | 25,5 | 36,0 |
| **Avantages de développement régional** (primes, infrastructures, prises en charge) | **170,9** | **69,4** | **80,3** | **70,9** | **48,1** | **52,6** | **53,5** |
| Prêt foncier agricole (compté en 2018-2019 ; imprimé hors total ensuite) | 9,6 | 13,8 | n. l. | (9,5) | n. l. | (8,0) | (7,9) |
| Prime d'investissement des projets d'intérêt national | — | — | 8,1 | 0 | 0 | 0 | 0 |
| **Total du domaine** | **242,9** | **186,5** | **150,1** | **160,8** | **89,8** | **91,9** | **108,4** |

Sources : 2018-2019, rapport 2021, section 4, p. 97-98 imprimées (texte) ; 2020-2022, rapport
2024, p. 74 du PDF (73 imprimée — image) ; 2021-2023, rapport 2025, p. 56 (image) ; prêt
foncier 2021-2023 : rapport 2025, p. 60, code 041102, entre parenthèses parce que hors total. L'exercice
2019 du rapport 2022 n'a pas été relu à ce niveau.

**Tableau D — lignes codées qui intéressent le chapitre** (millions de dinars). Le code à six
chiffres est stable d'un rapport à l'autre.

| Code | Avantage | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---:|---:|---:|---:|---:|---:|
| 011116 | prime d'investissement au titre du développement régional (agriculture et industrie) | 22,5 | 42,6 | 37,5 | 39,3 | 32,1 (R24) ; 36,6 (R25) | 33,1 |
| 041103 | participation de l'État aux dépenses d'infrastructure, développement régional | n. l. | 0,165 | 0,061 | 1,625 | 2,185 | 3,117 |
| **031106** | **prise en charge de la contribution patronale, développement régional, code de 1993, « article 25 bis »** | **131,0** | **21,0** | **42,2** | **29,4** | **13,4** | **16,0** |
| 031104 | idem, « code des investissements » (« ancien régime ») | 1,9 | 0,4 | 0,4 | 0,1 | 0,0 | 0,0 |
| 031105 | idem, « article 25 » | 0,8 | 0,2 | 0 | 0 | 0 | 0 |
| 031107 | idem, zones prioritaires | 9,8 | 0,7 | 0,1 | 0,0 | 0,0 | 0,0 |
| 031101 | prise en charge de la contribution patronale, **loi de 2016**, premier groupe de zones, cinq ans | n. l. | 0 | 0 | 0,121 | 0,154 | 0,135 |
| 031102 | idem, deuxième groupe de zones, dix ans | n. l. | 0 | 0 | 0,180 | 0,222 | 1,187 |
| 041101 | idem, secteurs prioritaires, trois ans | n. l. | n. l. | n. l. | 0,070 | 0,050 | 0,029 |
| 030602 | prise en charge de la contribution patronale pour l'agent recruté, dans la limite de 600 dinars par mois (emploi) | 19,1 | 23,1 | 14,9 | 18,6 | 8,1 (R24) | n. l. |
| 030606 | prise en charge de la contribution patronale, encouragement à l'emploi | 17,6 | 8,4 | 0 | 5,3 | 0,7 | n. l. |
| 011109 + 011111 | primes agricoles : secteurs prioritaires et investissements matériels de productivité | n. l. | n. l. | n. l. | 83,8 | 38,2 | 52,6 |

n. l. = non lu. Sources : 2018-2019, rapport 2021, annexe, p. 101-109 imprimées (texte) ;
2019-2020, rapport 2022 (texte, lignes des codes) ; 2020-2021, rapport 2023 (texte) ;
2020-2022, rapport 2024 (texte) ; 2021-2023, rapport 2025, p. 58-60 (**image**). **Les valeurs
2019-2020 et 2022 (R24) de ce tableau viennent de la seule couche texte des rapports arabes :
à relire à l'image avant publication.** Contrôle fait : la somme des lignes de prise en charge
patronale du rapport 2021 redonne le tableau n° 5 — 181,9 MD en 2018 (145,2 au titre du code
de 1993 + 36,7 au titre de l'emploi) et 54,0 MD en 2019 (22,6 + 31,4).

**Ce que ces tableaux établissent, pour le rédacteur :**

- **La chute de 181,9 à 54,0 MD des prises en charge patronales entre 2018 et 2019 tient à une
  seule ligne**, le code 031106 (code de 1993, article 25 bis) : 131,0 → 21,0 MD. Le tableau
  n° 3 du rapport 2021 (p. 94) la retrouve à la source de financement : « Titre 2 du
  ministère des Affaires sociales », 162,8 MD en 2018, 30,9 MD en 2019. **La cause n'est pas
  dite par le rapport** (apurement d'arriérés envers la CNSS en 2018 ? fin de droits ?) : ne
  pas l'interpréter.
- **Le régime de 1993 pèse encore plus que celui de 2016, sept ans après l'abrogation** : en
  2023, 16,0 MD de prises en charge patronales au titre de l'article 25 bis du code abrogé,
  contre 1,35 MD pour les trois prises en charge de la loi de 2016 réunies (codes 031101, 031102 et 041101) (rapport 2025,
  p. 59-60 — image).
- **La prime d'investissement de développement régional est stable, de 33 à 43 MD par an** de
  2019 à 2023 ; les primes agricoles (secteurs prioritaires et productivité) sont du même
  ordre ou au-dessus (52,6 MD en 2023).
- **Le total baisse en dinars courants** : 913 MD en 2018, 520,7 MD en 2023 — mais le
  périmètre s'est resserré en 2023 (prêts sortis), et la mise à niveau industrielle passe de
  176,8 MD (2018) à 30,0 MD (2023).

### 1.2 Le FOPRODI dans les comptes de la BCT, 2016-2025

**Source.** Banque centrale de Tunisie, *Rapport annuel*, états financiers de la Banque, note
sur les « comptes du Gouvernement » : « flux des ressources et des emplois des Fonds FOPRODI
et FONAPRA constatés durant l'exercice » (clé existante `bct-ra` ; fichiers
`~/projets/tunisia-data/data/raw/bct-archives/109/RA_2017_fr.pdf` à `RA_2025_fr.pdf` et
`ANNUALREPORT2021FRENCH.pdf`, déjà catalogués dans `sources/bct-archives-urls.csv`). La BCT
tient le compte du fonds pour l'État. Lu sur la couche texte ; chaque exercice figure dans
deux éditions successives, et les deux lectures coïncident.

**Tableau E — FOPRODI : ressources et emplois** (millions de dinars, arrondis du dinar).

| Exercice | Solde initial | Dotations budgétaires | Recouvrements | Emplois | Solde final | Édition, page du PDF |
|---|---:|---:|---:|---:|---:|---|
| 2016 | 4,17 | 47,00 | 3,24 | 52,59 | 1,81 | 2017, p. 231 |
| 2017 | 1,81 | 49,00 | 4,27 | 39,66 | 15,42 | 2017, p. 231 ; 2018, p. 248 |
| 2018 | 15,42 | 20,00 | 2,84 | 27,14 | 11,13 | 2018, p. 248 ; 2019, p. 214 |
| 2019 | 11,13 | 60,00 | 3,80 | 40,89 | 34,04 | 2019, p. 214 ; 2020, p. 219 |
| 2020 | 34,04 | 28,00 | 5,57 | 45,67 | 21,93 | 2020, p. 219 ; 2021, p. 209 |
| 2021 | 21,93 | 24,00 | 4,57 | 42,39 | 8,11 | 2021, p. 209 ; 2022, p. 218 |
| 2022 | 8,11 | 18,00 | 4,88 | 30,91 | 0,08 | 2022, p. 218 ; 2023, p. 222 |
| 2023 | 0,08 | 10,00 | 3,34 | 11,77 | 1,65 | 2023, p. 222 ; 2024, p. 226 |
| 2024 | 1,65 | 22,37 | 3,35 | 26,79 | 0,59 | 2024, p. 226 ; 2025, p. 230 |
| 2025 | 0,59 | 15,00 | 3,52 | 10,02 | 9,09 | 2025, p. 230 |

Périmètre : tout ce que paie le fonds — primes d'investissement et d'étude, prises en charge,
**et** dotations remboursables et participations (les « recouvrements » sont leurs
remboursements). Ce n'est donc pas la seule prime de développement régional, et la série ne
s'additionne pas aux tableaux du § 1.1, qui recensent les mêmes paiements par avantage. Le
décret gouvernemental n° 2017-389, art. 27, impute sur le FOPRODI, « jusqu'à l'exercice du
fonds tunisien de l'investissement de ses missions », les primes des industries
manufacturières, de l'artisanat et des services. Les éditions 2015 et 2016 du rapport ne
portent pas ce tableau (recherche du libellé « Dotations budgétaires » : néant). Éditions
antérieures, sondées par le mot « FOPRODI » sur la couche texte : celle de 2009 donne le seul
**solde** du compte dans les états financiers (0,48 MD et 14,96 MD, deux fins d'exercice) ;
celles de 2004 et de 2007, ouvertes aux lignes trouvées, n'en parlent qu'en prose (règles
d'intervention), les autres éditions de 2001 à 2013 n'ayant pas été ouvertes ; **celles de
1977 à 1986 portent des tableaux où figure le FOPRODI** (concours, dotations), sur une couche
texte à police décalée, non décodée ni lue à l'image — première piste d'un second passage.

Le même tableau donne le FONAPRA (dotations budgétaires : 12,0 MD en 2016 ; 8,0 en 2017 ; 0 de
2018 à 2021 ; 9,0 en 2022 ; 15,75 en 2023 ; 9,0 en 2024 et 2025).

**Déjà au dépôt de données, plus ancien** : `data/processed/bct-archives/programmes_emploi_dotations.csv`
(série `bct-programmes-emploi-dotations`, fiche `sources/bct-archives.md`) porte la ligne
FOPRODI du tableau « Programmes de soutien à l'emploi » du même rapport annuel pour **1987 à
1991 seulement** (6,6 ; 2,4 ; 3,0 ; 4,0 ; 3,7 MD — crédits, non paiements) et le FONAPRA de
1987 à 2008. Entre 1992 et 2015, **aucune série du FOPRODI n'est établie**.

### 1.3 Soldes des fonds spéciaux, 2005-2008 — un relevé de clôture, pas des paiements

Ministère des Finances, rapport annuel sur les finances publiques, édition 2010
(`~/projets/tunisia-data/data/raw/minfinances/portail_ancien/rapports_finances_publiques/2010_rapport_finances_publiques.pdf`,
p. 73 et 75 du PDF, 64 et 66 imprimées — image), tableau des « résultats (excédents) relatifs
aux fonds spéciaux » arrêtés à la clôture du budget : FOPRODI — ; 4,7 ; 16,6 ; 15,0 MD de 2005
à 2008 ; FONAPRA 1,7 ; 4,0 ; 3,0 ; 3,6 ; fonds spécial de développement agricole et de la
pêche (FOSDA) 12,9 ; 15,3 ; 16,3 ; 5,7 ; ensemble des fonds spéciaux 178,6 ; 382,4 ; 422,6 ;
435,9. **Ce sont des soldes reportés, non des dépenses** : à ne pas mettre en regard du § 1.1.
La même page donne, pour 2008, les ressources et dépenses des fonds du Trésor (1 406,6 et
828,8 MD) et des fonds spéciaux (670,1 et 234,2 MD) dans leur ensemble, sans détail par fonds.
Les éditions 2005 à 2008 et 2011 du même rapport, en arabe, n'ont pas été ouvertes.

### 1.4 Le commerce extérieur par régime, 1998-2023 (INS)

**Source.** INS, *Annuaire statistique de la Tunisie*, chapitre 14 « Commerce extérieur »,
tableau 14.2 « Évolution des échanges par groupement sectoriel d'activité », lignes « régime
général » et « régime off shore » (arabe : نظام عام، نظام غير مقيم) du total « Ensemble des
produits » (clé existante `ins-annuaire` ; 22 éditions, de 1995-2001 à 2019-2023, dans
`~/projets/tunisia-data/data/raw/ins-publications/annuaire-statistique/`). Lecture :
**couche texte des 22 éditions, par script** ; contrôle fait sur chaque ligne (régime général
+ régime off shore = ensemble, à 0,1 près) ; valeur retenue = dernière édition qui imprime
l'année. **Aucune page n'a été relue à l'image**, et **l'annuaire ne définit pas les deux
régimes** dans les pages lues : la définition reste à établir (glossaire des statistiques du
commerce extérieur de l'INS). Le libellé arabe — « régime non résident » — n'est pas celui du
code de 1993, pour lequel « totalement exportatrice » et « non résidente » sont deux notions
distinctes (art. 10 et 14).

**Tableau F — exportations et importations par régime** (millions de dinars courants).

| Année | Exportations | dont régime général | dont off shore | Part off shore | Importations | dont régime général | dont off shore | Part off shore | Édition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1998 | 6 518,3 | 2 115,9 | 4 402,4 | 67,5 % | 9 489,5 | 6 265,2 | 3 224,3 | 34,0 % | 1995-2001 |
| 1999 | 6 966,9 | 2 359,9 | 4 607,0 | 66,1 % | 10 070,5 | 6 858,3 | 3 212,2 | 31,9 % | 1995-2001 |
| 2000 | 8 004,8 | 2 912,4 | 5 092,4 | 63,6 % | 11 738,0 | 8 250,5 | 3 487,5 | 29,7 % | 1998-2002 |
| 2001 | 9 536,2 | 3 103,1 | 6 433,1 | 67,5 % | 13 697,3 | 9 255,6 | 4 441,7 | 32,4 % | 1999-2003 |
| 2002 | 9 748,6 | 2 995,9 | 6 752,7 | 69,3 % | 13 510,9 | 8 971,6 | 4 539,3 | 33,6 % | 2000-2004 |
| 2003 | 10 342,6 | 3 179,7 | 7 162,9 | 69,3 % | 14 038,9 | 9 030,9 | 5 008,0 | 35,7 % | 2001-2005 |
| 2004 | 12 403,8 | 4 183,2 | 8 220,6 | 66,3 % | 16 185,1 | 10 669,1 | 5 516,0 | 34,1 % | 2002-2006 |
| 2005 | 13 793,6 | 5 009,7 | 8 783,9 | 63,7 % | 17 291,5 | 11 447,2 | 5 844,3 | 33,8 % | 2003-2007 |
| 2006 | 15 558,0 | 5 899,4 | 9 658,5 | 62,1 % | 20 003,5 | 13 352,0 | 6 651,5 | 33,3 % | 2004-2008 |
| 2007 | 19 409,6 | 7 714,7 | 11 694,9 | 60,3 % | 24 437,3 | 16 330,4 | 8 106,9 | 33,2 % | 2005-2009 |
| 2008 | 23 637,0 | 11 091,4 | 12 545,6 | 53,1 % | 30 241,2 | 21 681,9 | 8 559,3 | 28,3 % | 2006-2010 |
| 2009 | 19 469,2 | 7 596,5 | 11 872,7 | 61,0 % | 25 877,6 | 18 132,0 | 7 745,6 | 29,9 % | 2007-2011 |
| 2010 | 23 519,0 | 9 157,9 | 14 361,1 | 61,1 % | 31 816,7 | 21 969,8 | 9 846,9 | 30,9 % | 2008-2012 |
| 2011 | 25 091,9 | 8 681,9 | 16 410,0 | 65,4 % | 33 695,4 | 22 751,9 | 10 943,5 | 32,5 % | 2008-2012 |
| 2012 | 26 547,7 | 10 200,3 | 16 347,4 | 61,6 % | 38 178,0 | 27 433,6 | 10 744,4 | 28,1 % | 2010-2014 |
| 2013 | 27 701,2 | 10 311,6 | 17 389,6 | 62,8 % | 39 505,5 | 28 171,0 | 11 334,5 | 28,7 % | 2011-2015 |
| 2014 | 28 406,7 | 9 586,8 | 18 819,9 | 66,3 % | 42 012,8 | 29 999,2 | 12 013,6 | 28,6 % | 2012-2016 |
| 2015 | 27 607,2 | 8 773,1 | 18 834,1 | 68,2 % | 39 609,7 | 27 794,3 | 11 815,4 | 29,8 % | 2013-2017 |
| 2016 | 29 145,6 | 7 689,1 | 21 456,5 | 73,6 % | 41 746,8 | 28 325,5 | 13 421,3 | 32,1 % | 2014-2018 |
| 2017 | 34 426,6 | 8 715,4 | 25 711,2 | 74,7 % | 50 021,6 | 33 908,6 | 16 113,0 | 32,2 % | 2015-2019 |
| 2018 | 40 987,4 | 11 137,0 | 29 850,4 | 72,8 % | 60 010,3 | 40 308,4 | 19 701,9 | 32,8 % | 2016-2020 |
| 2019 | 43 855,4 | 11 186,5 | 32 669,0 | 74,5 % | 63 291,6 | 42 435,6 | 20 856,0 | 33,0 % | 2017-2021 |
| 2020 | 38 705,9 | 10 712,2 | 27 993,7 | 72,3 % | 51 536,2 | 34 545,6 | 16 990,6 | 33,0 % | 2018-2022 |
| 2021 | 46 654,2 | 13 209,1 | 33 445,1 | 71,7 % | 62 864,9 | 42 269,1 | 20 595,8 | 32,8 % | 2019-2023 |
| 2022 | 57 557,5 | 18 436,6 | 39 120,8 | 68,0 % | 82 788,9 | 57 185,1 | 25 603,8 | 30,9 % | 2019-2023 |
| 2023 | 62 077,3 | 18 371,6 | 43 705,7 | 70,4 % | 79 146,3 | 53 407,3 | 25 739,0 | 32,5 % | 2019-2023 |

Les parts sont calculées ici (régime off shore / ensemble), non publiées. Révisions d'une
édition à l'autre, à signaler : 2001 (exportations 9 503,7 dans les éditions 1995-2001 et
1998-2002) ; **2004 (exportations 12 054,9 et importations 15 960,3 dans les éditions
2000-2004 et 2001-2005, contre 12 403,8 et 16 185,1 ensuite)** ; 2005 (13 607,7 et 17 101,3
dans l'édition 2001-2005) ; 2007 (exportations 16 409,6 dans l'édition 2003-2007 — sans doute
une coquille pour 19 409,6, les deux régimes y sommant à 19 409,6) ; écarts de quelques
dixièmes en 2002, 2014 et 2021. Le même tableau ventile chaque régime par groupement
sectoriel (agro-alimentaire, énergie, mines et phosphates, textile-habillement-cuir,
industries mécaniques et électriques, autres industries manufacturières) : non relevé.

Constat brut : **le régime off shore porte de 53 % à 75 % des exportations de biens sur
vingt-six ans, et environ un tiers des importations** ; sa part des exportations est à son
plus bas en 2008 (53,1 %) et à son plus haut en 2017 (74,7 %). Le *Rapport annuel 2024* de la
BCT (p. 77 imprimée — texte) donne pour 2024 un excédent de 18 296 MD sous le régime off
shore et un déficit de 37 224 MD sous le régime général.

**Non établi** : nombre d'entreprises totalement exportatrices et emploi (répertoire national
des entreprises de l'INS, APII, FIPA) — § 4.

### 1.5 Le barème des primes : code de 1993 (dernière rédaction) → loi de 2016

**Textes lus.** Décret gouvernemental n° 2017-389 du 9 mars 2017 (JORT n° 25 du 28 mars 2017,
p. 1098-1125 de l'édition française — texte pour les articles, image pour l'annexe n° 2) ;
décret n° 2024-182 du 4 avril 2024, son **seul modificatif** (JORT n° 47 du 5 avril 2024,
p. 1174-1184 de l'édition française — texte ; la notice de l'index donne la page arabe, 3428) ;
pour le code de 1993 : décret n° 94-539 du 10 mars 1994 (JORT n° 21 du 18 mars 1994,
p. 454-456 — texte), décret n° 99-486 du 1er mars 1999 (JORT n° 20 du 9 mars 1999,
p. 363-364 — texte décodé), décret n° 2008-389 du 11 février 2008 (JORT n° 15 du 19 février
2008, p. 756-758 — texte), décret n° 2011-528 du 9 mai 2011 (JORT n° 34 du 13 mai 2011,
p. 701-702 — texte), décret n° 2011-3197 du 18 octobre 2011 (JORT n° 82 du 28 octobre 2011 —
texte), décret n° 2013-4144 du 19 septembre 2013 (JORT n° 81 du 8 octobre 2013, p. 2964-2965 —
texte).

**« Seul modificatif » : comment c'est établi.** (a) Titres de `jort_cache` : une seule notice
cite le décret, en français comme en arabe (« 389 لسنة 2017 »). (b) Plein texte des fascicules
français de 2017 à 2026 : trente fascicules citent « 2017-389 » ; jusqu'au JORT n° 23 de 2024
les visas le citent sans « tel que modifié » ; à partir du JORT n° 100 de 2024 et jusqu'au
JORT n° 75 de 2026 (décret n° 2026-148 du 23 juillet 2026), ils écrivent « tel que modifié et
complété par le décret n° 2024-182 du 4 avril 2024 », et lui seul. Réserve : le corpus
français de 2018 ne compte que 70 fascicules, et l'article 4 du décret permet d'actualiser ses
listes « sur proposition de l'instance tunisienne de l'investissement et après approbation du
conseil supérieur d'investissement » — une actualisation par cette voie ne passerait pas
nécessairement par un décret.

**Dates d'effet.**

- Décret gouvernemental n° 2017-389 : « entre en vigueur à compter de la date d'entrée en
  vigueur de la loi de l'investissement » (art. 29), soit le **1er janvier 2017** — avant sa
  propre publication (fascicule déposé au siège du gouvernorat de Tunis le 29 mars 2017,
  mention en dernière page).
- Décret n° 2024-182 : pas de clause d'effet. Fascicule déposé le 5 avril 2024 (mention en
  dernière page) ; exécutoire cinq jours après, jour du dépôt non compté (loi n° 93-64,
  art. 2) : **10 avril 2024**.
- Décrets n° 2008-387 et 2008-389 : pas de clause d'effet (articles lus jusqu'à la
  signature) ; fascicule déposé le 20 février 2008 → **25 février 2008**. L'article 4 du
  décret n° 2008-389 maintient l'ancien barème aux projets déclarés avant l'entrée en vigueur
  de la loi n° 2007-69 et entrés en activité avant le 31 décembre 2009 (échéance portée au
  31 décembre 2010 par le décret n° 2009-3756).
- Décret n° 2011-528 : fascicule déposé le 14 mai 2011 → **19 mai 2011** ; son article 4
  maintient l'ancien barème aux projets déclarés avant la loi n° 2007-69 et entrés en activité
  avant le 31 décembre 2011 (date portée au 31 décembre 2014 par le décret n° 2014-2283).
- Décrets n° 99-483 et 99-486 : fascicule déposé le 9 mars 1999 (mention en dernière page,
  texte décodé) → **14 mars 1999**, sous réserve d'une clause d'effet dans les articles du
  décret n° 99-486 non lus (art. 2 et suivants).
- Décrets n° 94-426 et 94-539 : la mention de dépôt ne se trouve pas dans la couche texte du
  JORT n° 21 du 18 mars 1994 ; date d'exécution non établie.

**Tableau G — la prime d'investissement de développement régional, de 1994 à 2024** (industrie
manufacturière et services éligibles ; taux en pourcentage du coût de l'investissement).

| Date | Texte | Zones de moindre priorité | Zones intermédiaires | Zones les plus prioritaires | Assiette |
|---|---|---|---|---|---|
| 1994 | d. n° 94-539, art. 3 | 8 %, sans plafond écrit (une seule catégorie de zones) | — | — | coût du projet, fonds de roulement exclu |
| 1999 | d. n° 99-486, art. 1er (art. 3 nouveau) | 15 % (zones de l'annexe 1) | — | 25 %, « à l'exclusion de toutes autres primes » (zones prioritaires, annexe 1 bis) | idem |
| 2008 | d. n° 2008-389, art. 1er (art. 3 nouveau) | 8 %, plafond 320 000 D (premier groupe) | 15 %, plafond 600 000 D (deuxième groupe) | 25 %, plafond 1 MD (zones prioritaires) | idem |
| 2011 | d. n° 2011-528, art. 1er (art. 3 nouveau) | 8 %, plafond 500 000 D | 15 %, plafond 1 MD | 25 %, plafond 1,5 MD ; 30 % et 2 MD pour les nouveaux promoteurs (code, art. 62) | fonds de roulement **inclus**, dans la limite de 10 % du coût |
| 1er janvier 2017 | d. gouv. n° 2017-389, art. 3 § 2 | **15 %, plafond 1,5 MD** (premier groupe) | — | **30 %, plafond 3 MD** (deuxième groupe) | « coût d'investissement approuvé » |

**Attention à la lecture de la dernière ligne** : la catégorie intermédiaire ne disparaît pas,
elle est fondue dans le deuxième groupe de 2017 (§ 1.6). L'avant → après se lit par sort des
délégations, entre le barème de 2011 et celui de 2017 :

| Classement de 2008 | Délégations | Classement de 2017 | Taux | Plafond |
|---|---:|---|---|---|
| premier groupe | 10 | premier groupe | 8 % → 15 % | 0,5 → 1,5 MD |
| deuxième groupe | 37 | deuxième groupe | 15 % → 30 % | 1 → 3 MD |
| deuxième groupe (Ez-Zeriba, Bir Ali Ben Khalifa, Menzel Chaker) | 3 | premier groupe | 15 % → 15 % | 1 → 1,5 MD |
| zones prioritaires | 88 | deuxième groupe | 25 % → 30 % | 1,5 → 3 MD |
| hors liste | 9 | deuxième groupe | — → 30 % | — → 3 MD |

L'assiette change aussi de nom (« coût d'investissement, fonds de roulement inclus » dans la
limite de 10 % en 2011 ; « coût d'investissement approuvé » en 2017) : les deux taux ne
portent pas nécessairement sur la même base.

**Tableau H — participation de l'État aux dépenses d'infrastructure, industrie.**

| Date | Texte | Premier groupe | Deuxième groupe | Zones prioritaires |
|---|---|---|---|---|
| 1994 | d. n° 94-539, art. 4 | couverture « totale ou partielle », selon la localisation et l'importance du projet, sans taux | — | — |
| 2008 | d. n° 2008-389, art. 1er (art. 4 nouveau) | 25 % des dépenses | 50 % | 75 % |
| 2011 | d. n° 2011-528, art. 2 et 3 | 25 % | 75 % | 85 % |
| 1er janvier 2017 | d. gouv. n° 2017-389, art. 3 § 2 | 65 % des dépenses, dans la limite de 10 % du coût du projet, plafond 1 MD | 85 %, mêmes limites | — |

**Tableau I — les autres primes de la loi de 2016** (décret gouvernemental n° 2017-389, art. 3,
texte d'origine ; modifications de 2024 en dernière colonne).

| Prime (loi n° 2016-71, art. 19) | Objet | Taux | Plafond | Décret n° 2024-182 |
|---|---|---|---|---|
| Augmentation de la valeur ajoutée et de la compétitivité | investissement direct dans les **secteurs prioritaires** (annexe n° 1, liste I) | 15 % du coût approuvé ; **30 %** pour l'agriculture, la pêche et l'aquaculture de catégorie « A » (le texte écrit « ramené à 30 % ») | 1 MD | inchangé |
| idem | investissement direct dans les **filières économiques** | 15 % | 1 MD | inchangé |
| idem, performance économique | investissements matériels de maîtrise des nouvelles technologies et d'amélioration de la productivité | 50 % ; 55 % en catégorie « A » agricole ; 60 % pour les sociétés mutuelles de services agricoles et les groupements de développement | 500 000 D | 60 % étendu aux **sociétés communautaires** |
| idem | investissements immatériels | 50 % | 500 000 D, prime d'étude comprise (20 000 D) | inchangé |
| idem | recherche et développement | 50 % des dépenses approuvées | 300 000 D | inchangé |
| idem | formation certifiante des employés tunisiens | 70 % du coût | 20 000 D par an et par entreprise | inchangé |
| Développement de la capacité d'employabilité (a) | prise en charge de la contribution patronale au régime légal de sécurité sociale, salariés tunisiens | secteurs prioritaires : 3 ans ; premier groupe de zones : 5 ans ; deuxième groupe : 10 ans, à partir de l'entrée en activité effective | — | la condition « recrutés pour la première fois et d'une manière permanente » **disparaît** du a) |
| idem (b) | prise en charge d'une partie des salaires selon le taux d'encadrement | 50 % du salaire, 1 an (encadrement de 10 à 15 %) ou 3 ans (plus de 15 %), diplômés du supérieur | 250 D par mois | « recrutés pour la première fois » ajouté au b) |
| Développement durable | dépollution, technologies propres, équipements collectifs de dépollution | 50 % des composantes approuvées | 300 000 D | inchangé |
| Projets d'intérêt national (loi, art. 20) | critères : coût ≥ 50 MD, ou… (art. 16, lu en partie) | prime dans la limite du tiers du coût (loi) | — | critère d'emploi : 500 postes, ou 200 postes de diplômés du supérieur, en quatre ans |

Catégorie « A » (art. 2) : investissement agricole d'au plus 200 000 D, de pêche d'au plus
300 000 D, d'aquaculture d'au plus 500 000 D, et tout investissement des sociétés mutuelles de
services agricoles et des groupements de développement.

**Règles communes** (décret gouvernemental n° 2017-389) :

- **cumul** (art. 5) : l'ensemble des primes — loi de l'investissement et autres textes — ne
  dépasse pas **le tiers du coût de l'investissement, avec un plafond de 5 MD**, hors
  participation aux infrastructures et prime d'employabilité. La loi n° 2019-47, art. 18, puis
  le décret n° 2024-182 sortent aussi de ce plafond les primes de performance économique et la
  prime de développement durable ;
- **fonds propres** (art. 7) : 30 % du coût au moins ; 10 % pour la catégorie « A » agricole,
  puis — décret n° 2024-182 — 10 % pour tout projet d'au plus 1 MD ;
- **emploi** : dix emplois permanents au moins pour les projets des filières et des secteurs
  prioritaires, hors agriculture (art. 7) ;
- **versement** (art. 12) : 40 % à la réalisation de 40 % du coût, 60 % à l'entrée en activité
  effective ; le code de 1993 versait en trois tranches (30 / 30 / 40 % depuis 2008 ; 40 / 40
  / 20 % en 1994 pour les projets d'au plus 1 MD) ;
- **participations au capital** (art. 21-22) : fonds tunisien de l'investissement, 60 % du
  capital au plus pour un projet d'au plus 2 MD, 30 % au-delà, plafond 2 MD, rétrocession en
  douze ans au nominal majoré de 1 % ou 3 % par an ;
- **imputation transitoire** (art. 27, texte de 2017) : fonds spécial de développement de
  l'agriculture (agriculture, pêche, prêts fonciers) ; FOPRODI (industrie, artisanat,
  services) ; titre II du ministère de l'Industrie (recherche et développement) ; Office
  national du tourisme tunisien ; FONAPRA ; **titre II du ministère des Affaires sociales pour
  la prise en charge de la contribution patronale** ; Fonds national de l'emploi (salaires,
  formation). L'article 27 nouveau de 2024 impute sur le fonds tunisien de l'investissement
  les projets d'intérêt national et ceux « entrepris par l'instance » (lu en partie : la
  couche texte entrelace deux colonnes).

**Tourisme, pour mémoire** (code de 1993, décret n° 2013-4144) : 8 % du coût hors terrain,
plafond 2,8 MD (hébergement et animation dans les zones de l'annexe 2) ; 25 %, plafond 2 MD
(thermalisme ; hôtels de charme, gîtes ruraux, chambres d'hôtes).

### 1.6 Les zones de développement régional : la carte, de 1994 à 2024

**L'article 63 du code de l'impôt ne nomme pas le décret** : « la liste des activités dans les
secteurs exclues du bénéfice de ladite déduction et des zones de développement régional est
fixée par un décret gouvernemental » (loi n° 2017-8, art. 1er, JORT n° 15 du 21 février 2017 —
texte). Le seul texte identifié ici qui porte une liste de « zones de développement régional » en deux
groupes est **l'annexe n° 2 du décret gouvernemental n° 2017-389**, pris pour la loi de
l'investissement ; sa liste III de l'annexe n° 1 est celle des « activités exceptées de
bénéfice de la prime de développement régional ». Deux indices jouent en sens contraire : le
décret est signé le 9 mars 2017, après la loi du 14 février, et reprend ses deux groupes ; mais
ses visas citent le code de l'impôt « tel que modifié […] notamment [par] la loi n° 2016-78 »,
**sans viser la loi n° 2017-8 ni l'article 63**. La loi de finances pour 2018 (loi n° 2017-66,
art. 20, JORT n° 101 du 19 décembre 2017, p. 4271 ou 4272, à contrôler — texte) parle des « zones de
développement régional au sens de l'article 63 dudit code » sans nommer de décret : elle
étend le régime de l'article 64 (deux tiers des revenus déductibles, bénéfices à 10 %) aux
entreprises déclarées avant le 1er avril 2017 dont la période de déduction du code de 1993 est
expirée ou expire. **Que l'annexe n° 2 vaille pour l'article 63 est vraisemblable et non
établi par un texte lu** : fiche `r-fisc-art63-decret-zones` (§ 4).

**Tableau J — nombre de délégations classées, par date et par catégorie** (industrie,
artisanat et services ; les zones touristiques, tenues dans des annexes séparées de 1994 à
2016, ne sont pas comptées).

| Date | Texte | Catégorie la moins aidée | Catégorie intermédiaire | Catégorie la plus aidée | Total |
|---|---|---|---|---|---|
| 1994 | d. n° 94-426, annexe 1 | une seule catégorie : **12 gouvernorats entiers** (Béja, Jendouba, Siliana, Le Kef, Kairouan, Kasserine, Sidi Bouzid, Zaghouan, Tataouine, Gafsa, Kébili, Tozeur) et **27 délégations** de 6 autres (Sousse 2, Sfax 8, Médenine 4, Gabès 5, Bizerte 3, Mahdia 5) | — | — | non dénombrable en délégations d'après le texte |
| 1999 | d. n° 99-483, annexes 1 et 1 bis | « zones » : **13 délégations** de 7 gouvernorats (Béja 3, Zaghouan 3, Sousse 1, Sfax 1, Gabès 1, Mahdia 2, Kairouan 2) | — | « zones prioritaires » : **9 gouvernorats entiers** (Kébili, Tozeur, Sidi Bouzid, Kasserine, Le Kef, Gafsa, Jendouba, Siliana, Tataouine) et **43 délégations** de 9 autres | idem |
| 2008 | d. n° 2008-387, annexe 1 (nouveau) | premier groupe : **10 délégations**, 4 gouvernorats | deuxième groupe : **40 délégations**, 10 gouvernorats | zones prioritaires : **88 délégations**, 16 gouvernorats | **138 délégations** |
| 1er janvier 2017 | d. gouv. n° 2017-389, annexe 2 | premier groupe : **13 délégations**, 4 gouvernorats (Béja 1, Zaghouan 3, Sfax 8, Sousse 1) | — | deuxième groupe : **134 délégations**, 17 gouvernorats | **147 délégations, 18 gouvernorats** |
| 10 avril 2024 | d. n° 2024-182, art. 5 | 13 | — | 135 (El Hamma Ouest, Gabès, ajoutée) | 148 |

Comptes faits ici sur les listes (2017 : image des p. 1113-1116, et décompte de la couche
texte : 147 lignes « Délégation ») ; ils ne sont publiés par aucun des textes.

**Comment la carte change, en quatre constats :**

1. **De gouvernorats entiers à des délégations.** En 1994 et 1999, l'intérieur et le Sud
   entrent par gouvernorats entiers ; depuis 2008 la liste ne nomme plus que des délégations.
2. **1999 crée la hiérarchie** (zones / zones prioritaires), 2008 la porte à trois niveaux,
   2017 la ramène à deux en fondant le deuxième groupe et les zones prioritaires de 2008 dans
   le « deuxième groupe ».
3. **Le périmètre de 2017 est celui de 2008, à peu de chose près** : 138 délégations en 2008,
   147 en 2017 ; les neuf en plus sont des délégations absentes de la liste de 2008 dans des
   gouvernorats déjà entièrement ou largement classés — Touiref (Le Kef), Zanouch et Sidi
   Boubaker (Gafsa), Essaïda (Sidi Bouzid), Aïn Jloula et Menzel Mhiri (Kairouan), Hammet El
   Djérid (Tozeur), Réjim Maatoug (Kébili), Dekhilet Toujane (Gabès). Qu'il s'agisse de
   délégations créées entre-temps par découpage n'est pas vérifié.
4. **Le premier groupe de 2017 est le premier groupe de 2008 plus trois délégations** qui
   étaient au deuxième groupe (Ez-Zeriba, Bir Ali Ben Khalifa, Menzel Chaker) : elles relèvent
   en 2017 du groupe à cinq ans de déduction et à 15 % de prime, quand le reste du deuxième
   groupe de 2008 passe au groupe à dix ans et à 30 %. Les durées de déduction attachées à
   chaque catégorie entre 2008 et 2016 (code de 1993, art. 23 nouveau) ne sont pas lues.

Entre les textes lus, **vingt décrets de retouche** sont connus par leur seul intitulé :
n° 96-40, 96-1560, 97-629, 97-2107 et 98-1042 (complétant le décret de 1994) ; n° 2003-1080,
2004-2177 et 2005-1686 (modifiant ou complétant celui de 1999) ; pour les primes, n° 95-2430,
96-1765, 98-1264, 2001-2884, 2002-1363, 2003-1677, 2004-973, 2004-1471, 2005-381, 2007-895,
2009-1501, 2009-2752. La catégorie « zones de développement régional prioritaires » existe
dans la loi dès la loi de finances pour 2005 (loi n° 2004-90, art. 19 — intitulé). Aucun
modificatif du décret n° 99-483 postérieur au décret n° 2008-387 n'apparaît (fiche
`r-fisc-zones-modif-99-483`, § 4).

**Avant 1994** : le décret n° 94-426 abroge trois textes — décret n° 87-1287 du 17 novembre
1987 (zones de décentralisation industrielle), décret n° 90-1509 du 17 septembre 1990 (zones
touristiques de décentralisation), décret n° 91-87 du 14 janvier 1991 (régions sahariennes) —,
non lus.

La liste entière de 2017 et celle de 2008 sont en annexe (§ 7).

### 1.7 La loi n° 2019-47 du 29 mai 2019 : portée fiscale et financière

Loi n° 2019-47 du 29 mai 2019, relative à l'amélioration du climat de l'investissement, JORT
n° 47 du 11 juin 2019, p. 1644-1654 de l'édition française (texte) ; p. 1756-1765 de l'édition
arabe (notice). Fascicule déposé le 13 juin 2019 → exécutoire le **18 juin 2019** (loi
n° 93-64, art. 2 ; pas de clause générale d'effet relevée). Trente-huit articles, qui
retouchent de nombreuses lois (sociétés commerciales, commerce international, énergies
renouvelables, organismes de placement collectif, Caisse des dépôts, procédures collectives).
**Son objet déclaré n'est pas fiscal** : « promouvoir l'investissement et améliorer le climat
des affaires par la simplification des procédures requises pour la création d'entreprises
économiques, la facilitation de leurs modes de financement et le renforcement de la
gouvernance et de la transparence des sociétés » (art. 1er). Les trente-huit articles ont été
parcourus (en-tête de chacun, et recherche des mots « impôt », « taxe », « fiscal »,
« douane ») ; ce qui touche l'impôt et le budget tient en huit articles :

| Article | Disposition | Nature |
|---|---|---|
| 12 et 13 | code de l'impôt, art. 56 : les organismes publics chargés de la constitution des entreprises peuvent délivrer la carte d'identification fiscale et recevoir la déclaration d'existence | procédure fiscale, sans effet sur l'impôt dû |
| 15 | les souscriptions des sociétés d'investissement à capital risque et des fonds communs de placement à risque dans une entreprise **transmise ou restructurée** ouvrent droit à la déduction de l'article 77 du code de l'impôt (réinvestissement), « jusqu'au 31 décembre 2022 » | fiscale, temporaire |
| 18 | loi n° 2016-71, art. 19, § 2 nouveau : cumul des primes plafonné au tiers du coût, **hors** infrastructures, performance économique, employabilité et développement durable ; versement dans les six mois | financière |
| 19 | loi n° 2016-71, art. 20 : les projets d'intérêt national peuvent recevoir la **prise en charge de la contribution patronale pendant dix ans au plus** et des terres domaniales non agricoles en location longue ou au dinar symbolique | financière |
| 21 | **bonification d'intérêt** : l'État prend en charge l'écart entre le taux des crédits d'investissement et le taux moyen du marché monétaire, dans la limite de **trois points**, pour les petites et moyennes entreprises (hors commerce, finance, immobilier, hydrocarbures et mines), crédits accordés du 1er janvier 2019 à fin décembre 2020, marge bancaire plafonnée à 3,5 % | financière, temporaire |
| 35 | loi n° 2017-8, art. 19 § 4 et art. 20 § 3 et 4 : l'échéance « au plus tard 31 décembre 2019 » des dispositions transitoires de la refonte des avantages fiscaux est portée au **31 décembre 2020** (objet de ces paragraphes non relu ici) | fiscale, transitoire |
| 38 | loi n° 2016-71, art. 28 et 29 : les droits acquis du code de 1993 sont ouverts aux entreprises ayant déposé leur déclaration avant le 1er janvier 2017 et obtenu la décision d'octroi et l'entrée en activité **au plus tard le 31 décembre 2020** | transitoire |

Suites connues par leur intitulé seul : loi de finances pour 2020 (loi n° 2019-78), art. 29,
« clarification du champ d'application de l'article 15 » ; décret-loi n° 2022-79 (loi de
finances pour 2023), art. 30 (échéance « fin décembre 2022 » de l'article 21 remplacée) et
art. 32 (échéance du 31 décembre 2022 de l'article 15 prorogée) ; loi de finances pour 2025
(loi n° 2024-48), art. 55 (échéance du 31 décembre 2024 prorogée). La bonification de
l'article 21 se lit dans les comptes de la BCT : « compte de prise en charge par l'État de la
différence entre le taux d'intérêt des crédits d'investissement et le TMM au profit des PME »,
14,9 MD à fin 2023, 10,8 MD à fin 2024 (*Rapport annuel 2024*, p. 215 imprimée — texte ; solde
du compte, non dépense de l'année).

### 1.8 Les prises en charge de cotisations patronales : ce qui est payé, et par qui

- **Ce que mesurent les rapports** (§ 1.1) : ce que le budget **paie à la caisse** pour le
  compte de l'employeur, ou reconnaît lui devoir. Ce n'est pas un manque à gagner de la CNSS :
  la cotisation est due, et l'État s'y substitue. Le rapport 2022 (p. 69) dit compter les
  sommes versées **ou « portées en dette de l'État »** envers l'organisme : une part des
  montants peut donc être une dette reconnue, non un paiement. Le coût pour la sécurité
  sociale n'apparaît que si l'État paie en retard ou pas du tout — ce qu'aucune source lue ne
  chiffre.
- **Montants** (tableau A) : 181,9 MD en 2018 ; 54,0-55,1 MD en 2019 ; 62,4 en 2020 ; 65,9 en
  2021 ; 39,0 en 2022 ; 43,3 en 2023. Part du développement régional au titre du code de 1993
  (codes 031104 à 031109) : 145,2 MD en 2018, 22,6 en 2019 ; code
  031106 seul ensuite (tableau D).
- **Source de financement** : titre II du ministère des Affaires sociales (décret
  gouvernemental n° 2017-389, art. 27 ; rapport 2021, tableau n° 3, p. 94 : 162,8 MD en 2018,
  30,9 MD en 2019) et Fonds national de l'emploi pour les dispositifs d'emploi.
- **Durées** : cinq ans dans le texte de 1993 (art. 25, d'après le chapitre) ; trois, cinq ou
  dix ans depuis 2017 (tableau I) ; dix ans au plus pour les projets d'intérêt national
  depuis 2019. Les rédactions intermédiaires de l'article 25 (lois de finances pour 2005,
  2008, 2014 ; « article 25 bis ») ne sont pas lues.
- **Côté caisse : non établi.** Les fiches `cnss-*` de `tunisia-data` ne portent aucune ligne
  « prise en charge par l'État » ni « créances sur l'État » (recherche de ces libellés dans
  `sources/cnss*.md` : néant). Voir § 4.

---

## 2. Références candidates

### 2.1 Déjà présentes dans `precis/fr/fiscalite/references.json`

`gbo-depenses-fiscales` (les cinq rapports ; préciser l'édition et la page dans le suffixe),
`loi-2016-71-investissement`, `loi-avantages-fiscaux-2017`, `loi-93-120-code-incitations`,
`bct-ra`, `ins-annuaire`.

### 2.2 À créer

Adresses contrôlées le 11 octobre 2026. Pagination : édition française lue ; édition arabe
d'après la notice quand elle diffère, « non relevée » sinon.

| Clé suggérée | Texte | JORT | Pages FR | Pages AR | URL FR / AR |
|---|---|---|---|---|---|
| `decret-gouv-2017-389-incitations-financieres` | Décret gouvernemental n° 2017-389 du 9 mars 2017, relatif aux incitations financières au profit des investissements réalisés dans le cadre de la loi de l'investissement | n° 25 du 28 mars 2017 | 1098-1125 (annexe n° 2 : 1113-1116) | non relevées | `https://www.pist.tn/jort/2017/2017F/Jo0252017.pdf` / `https://www.pist.tn/jort/2017/2017A/Ja0252017.pdf` |
| `decret-2024-182-incitations-financieres` | Décret n° 2024-182 du 4 avril 2024, modifiant et complétant le décret gouvernemental n° 2017-389 | n° 47 du 5 avril 2024 | 1174-1184 (début d'après le sommaire ; l'annexe n° 4 nouvelle suit la signature) | 3428 (première page, d'après la notice) | `https://www.pist.tn/jort/2024/2024F/Jo0472024.pdf` / `https://www.pist.tn/jort/2024/2024A/Ja0472024.pdf` |
| `loi-2019-47-climat-investissement` | Loi n° 2019-47 du 29 mai 2019, relative à l'amélioration du climat de l'investissement | n° 47 du 11 juin 2019 | 1644-1654 | 1756-1765 | `https://www.pist.tn/jort/2019/2019F/Jo0472019.pdf` / `https://www.pist.tn/jort/2019/2019A/Ja0472019.pdf` |
| `decret-94-426-zones-developpement-regional` | Décret n° 94-426 du 14 février 1994, portant délimitation des zones d'encouragement au développement régional | n° 21 du 18 mars 1994 | 454 d'après la notice (annexes jusqu'à 455 ; à contrôler à l'image) | non relevées | `https://www.pist.tn/jort/1994/1994F/Jo02194.pdf` / `https://www.pist.tn/jort/1994/1994A/Ja02194.pdf` |
| `decret-94-539-primes-developpement-regional` | Décret n° 94-539 du 10 mars 1994, portant fixation des primes, des listes des activités et des projets d'infrastructure et d'équipements collectifs éligibles aux encouragements au titre du développement régional | n° 21 du 18 mars 1994 | 454-456 d'après la notice (à contrôler à l'image) | non relevées | mêmes adresses |
| `decret-99-483-zones-developpement-regional` | Décret n° 99-483 du 1er mars 1999, portant délimitation des zones d'encouragement au développement régional | n° 20 du 9 mars 1999 | 359-360 | non relevées | `https://www.pist.tn/jort/1999/1999F/Jo02099.pdf` / `https://www.pist.tn/jort/1999/1999A/Ja02099.pdf` |
| `decret-99-486-primes-developpement-regional` | Décret n° 99-486 du 1er mars 1999, modifiant et complétant le décret n° 94-539 | n° 20 du 9 mars 1999 | 363-364 | non relevées | mêmes adresses |
| `decret-2008-387-zones-developpement-regional` | Décret n° 2008-387 du 11 février 2008, modifiant le décret n° 99-483 | n° 15 du 19 février 2008 | 745-746 | non relevées | `https://www.pist.tn/jort/2008/2008F/Jo0152008.pdf` / `https://www.pist.tn/jort/2008/2008A/Ja0152008.pdf` |
| `decret-2008-389-primes-developpement-regional` | Décret n° 2008-389 du 11 février 2008, modifiant et complétant le décret n° 94-539 | n° 15 du 19 février 2008 | 756-758 | non relevées | mêmes adresses |
| `decret-2011-528-primes-developpement-regional` | Décret n° 2011-528 du 9 mai 2011, modifiant le décret n° 94-539 | n° 34 du 13 mai 2011 | 701-702 | non relevées | `https://www.pist.tn/jort/2011/2011F/Jo0342011.pdf` / `https://www.pist.tn/jort/2011/2011A/Ja0342011.pdf` |
| `decret-2013-4144-primes-tourisme` | Décret n° 2013-4144 du 19 septembre 2013, modifiant et complétant le décret n° 94-539 | n° 81 du 8 octobre 2013 | 2964-2965 | non relevées | `https://www.pist.tn/jort/2013/2013F/Jo0812013.pdf` (adresse arabe non contrôlée) |

**Attention, années 1994 à 1999 : l'adresse arabe suit la règle à deux chiffres** (`Ja02194`,
`Ja02099`) ; contrôlées, elles répondent 200.

Non proposés faute d'emploi certain : décret n° 2011-3197 (intégration de la prime au schéma
de financement, JORT n° 82 du 28 octobre 2011, `…/2011/2011F/Jo0822011.pdf`), décrets
n° 2009-3756 et 2014-2283 (reports d'échéance), arrêté du 14 avril 2017 sur les commissions
d'octroi (JORT n° 38 de 2017, cité au plein texte, non lu).

Rapports : rien à créer — `bct-ra` et `ins-annuaire` existent. Si le bibliographe veut une
entrée par édition, les adresses sont dans `~/projets/tunisia-data/sources/bct-archives-urls.csv`
(`https://www.bct.gov.tn/bct/siteprod/documents/RA_2017_fr.pdf` … `RA_2025_fr.pdf`) et dans
`sources/ins-annuaires-statistiques.md`. Le rapport sur les finances publiques de 2010 est
catalogué dans `sources/minfinances-portail-ancien-urls.csv` ; il n'a pas de clé
bibliographique au volume de la fiscalité (à vérifier dans les autres volumes).

---

## 3. Notions à glossaire

Existent déjà : `depense-fiscale`, `avantage-financier`, `prime-investissement`,
`zone-developpement-regional`, `projet-interet-national`, `entreprise-totalement-exportatrice`.

| Notion | Terme arabe relevé | Source canonique | Remarque |
|---|---|---|---|
| zone de développement régional (à compléter) | مناطق التنمية الجهوية (intitulés des lois de finances 2018 et 2020, `jort_cache`) | d. gouv. n° 2017-389, annexe n° 2 | ajouter : deux groupes depuis 2017 ; « zones d'encouragement au développement régional » et « zones prioritaires » sous le code de 1993 |
| prime de développement régional | منحة استثمار بعنوان التنمية الجهوية (rapport 2025, p. 59) | loi n° 2016-71, art. 19 ; d. gouv. n° 2017-389, art. 3 § 2 | |
| prime de développement de la capacité d'employabilité | non relevé | idem, art. 3 § 3 | couvre la prise en charge patronale et celle d'une part des salaires |
| prise en charge par l'État de la contribution patronale | تكفل الدولة بمساهمة الأعراف في النظام القانوني للضمان الاجتماعي (rapports 2022 à 2025, tableau n° 4) | idem | à relier au volume « Cotisations sociales » |
| secteurs prioritaires ; filières économiques | القطاعات ذات الأولوية ; المنظومات الاقتصادية (rapport 2025, p. 58) | d. gouv. n° 2017-389, art. 2 et annexe n° 1 | définitions citables telles quelles |
| Fonds de promotion et de décentralisation industrielle (FOPRODI) | صندوق التطوير واللامركزية الصناعية (rapport sur les finances publiques 2010, p. 64) | loi n° 73-82, art. 45 (visa du d. gouv. n° 2017-389 — non lue) | acronyme |
| Fonds tunisien de l'investissement ; Instance tunisienne de l'investissement | non relevés | loi n° 2016-71, art. 11 à 18 ; d. gouv. n° 2017-388 (intitulé) | |
| régime général / régime off shore (commerce extérieur) | نظام عام ; نظام غير مقيم (INS, annuaire, tableau 14.2) | INS, *Annuaire statistique* | **le glossaire écrit aujourd'hui (l. 9779) que « offshore » est un mot d'usage absent des textes lus : il est employé par la statistique publique**, à défaut de l'être par la loi ; la note du glossaire est à nuancer |
| catégorie « A » / « B » (investissement agricole) | non relevé | d. gouv. n° 2017-389, art. 2 | utile seulement si le rédacteur reprend le tableau I |

---

## 4. Ce qui n'est pas établi, et les fiches de recherche

### 4.1 Lacunes (hors *Journal officiel*)

1. **Aucune série de paiements avant 2016** pour les primes du code de 1993. Voies essayées :
   (a) ancien portail du ministère des Finances — `rapports_finances_publiques/` (recherche
   de « FOPRODI », « fonds spéciaux », « prime d'investissement » dans les 14 PDF : seule
   l'édition 2010 répond, par des soldes, § 1.3 ; les éditions 2005 à 2008 sont en arabe à
   police non extractible et n'ont pas été ouvertes à l'image) ; `series_statistiques/`
   (dépenses par nature seulement) ; `lois_finances/` (les lois de 2003 à 2012 y sont en
   arabe ; le tableau « ب » des fonds du Trésor y est annoncé à l'article 2 — 602,3 MD pour
   2008 —, non relevé) ; (b) BCT, *Rapport annuel* : la ligne FOPRODI du tableau des
   programmes d'emploi s'arrête en 1991, la note des états financiers commence à l'édition
   2017. **Voies non essayées** : tableaux « ب » des lois de finances au *Journal officiel*
   (fonds du Trésor, fonds par fonds, de 1994 à 2019 — travail de transcription) ; lois de
   règlement (غلق ميزانية الدولة : lois n° 2016-23 à 2016-25 pour 2010-2012, n° 2018-39 à
   2018-41 pour 2013-2015, n° 2018-49 pour 2016, intitulés arabes seuls) ; budgets par
   ministère 2013 et suivants (`budgets_ministeres/`, 170 fichiers) ; rapports de la Cour des
   comptes (le catalogue `sources/cour-des-comptes-catalog.csv` ne répond à aucun des mots
   « FOPRODI », « incitation », « mise à niveau », « exportat » ; une recherche web signale
   une rubrique « Création des petites et moyennes entreprises » sur `courdescomptes.nat.tn`,
   non ouverte) ; archives du web de l'APII (`tunisieindustrie.nat.tn`) et de l'APIA.
2. **Comptes du Fonds tunisien de l'investissement et rapports de l'Instance tunisienne de
   l'investissement** : non cherchés. Le rapport 2021 nomme un « Fonds national de
   l'investissement » parmi les sources de financement (97,2 MD en 2018, 162,8 MD en 2019,
   tableau n° 3, p. 94) : à identifier.
3. **Mise à niveau** : 176,8 MD (2018), 145,9 (2019), 41,2 (2021), 29,3 (2022), 30,0 (2023) ;
   2020 non lu au niveau du programme ; aucune série avant 2018 (Fonds de développement de la
   compétitivité industrielle, bureau de mise à niveau).
4. **Primes agricoles (APIA)** : 2021-2023 seulement (tableau D) ; avant, néant.
5. **Entreprises totalement exportatrices : nombre, emploi** (répertoire national des
   entreprises de l'INS, APII, FIPA). `tunisia-data` ne porte rien (`data/processed/` : aucune
   série ; `sources/` : aucune fiche). **Non cherché en ligne** à cette note : c'est le premier
   objet d'un second passage (publications « Statistiques issues du répertoire national des
   entreprises » de l'INS ; tableaux de bord de l'APII « entreprises totalement
   exportatrices » ; rapports annuels de la FIPA ; archives du web pour les éditions
   retirées).
6. **Définition statistique des régimes « général » et « off shore »** (INS) : non lue.
7. **Cause de la chute du code 031106 entre 2018 et 2019** (131,0 → 21,0 MD) : non dite.
8. **Incohérence du rapport 2025** entre le tableau n° 2 (p. 52) et le tableau détaillé
   (p. 56-57) sur la ligne « financement des petits projets ».
9. **Rapport annexé au projet de loi de finances pour 2026** : non trouvé (deux voies).
10. **Coût pour la CNSS** des prises en charge : non établi (§ 1.8). Voies : états financiers
    de la CNSS (créances sur l'État), rapports d'activité, rapports annuels de performance de
    la mission Affaires sociales (`sources/mas-rap-pap-cnrps.md` en porte pour la CNRPS).
11. **Rédactions de l'article 25 et de l'article 25 bis du code de 1993** (prise en charge
    patronale) entre 1993 et 2016 : intitulés seuls (lois de finances pour 2005, art. 19 ;
    pour 2014, art. 22 ; loi n° 2007-69).
12. **Délégations « nouvelles » de 2017** (§ 1.6, constat 3) : création par découpage non
    vérifiée.
13. **Listes de 1994 et de 1999 en nombre de délégations** : les gouvernorats entiers ne se
    dénombrent pas d'après le texte ; il faudrait le découpage administratif de l'époque.

### 4.2 Fiches proposées pour `docs/recherches.yml` (non versées)

`uv run python scripts/recherches.py lister` : aucune fiche existante sur ces objets.

```yaml
- id: r-fisc-art63-decret-zones
  objet: >-
    décret gouvernemental fixant, pour l'article 63 du code de l'impôt sur le revenu des
    personnes physiques et de l'impôt sur les sociétés (loi n° 2017-8, art. 1er), la liste
    des zones de développement régional et des activités exclues — soit un texte propre,
    soit la confirmation par un texte que l'annexe n° 2 du décret gouvernemental n° 2017-389
    en tient lieu
  ou: [precis/fr/fiscalite/_depenses_fiscales.qmd#sec-df-reformes]
  requetes:
    titres_like:
      - '%zones de developpement regional%'
      - '%zones de développement régional%'
      - '%2017-389%'
    iort_ar:
      - 'مناطق التنمية الجهوية'
      - '389 لسنة 2017'
    plein_texte:
      - '2017-389'
    depuis: 2017-02-14
  passes:
    - date: 2026-10-11
      role: documentaliste
      sources: [jort_cache, corpus_local]
      couverture: >-
        titres de jort_cache, français et arabe, années 2015 et suivantes : trois réponses,
        toutes des articles de lois de finances (loi n° 2017-66, art. 20 ; loi n° 2018-56 ;
        loi n° 2019-78, art. 44), aucun décret (requêtes lancées en SQL sur la colonne titre,
        années de fascicule 2015 et suivantes ; ni la FTS ni le miroir iort n'ont été
        interrogés). Plein texte « 2017-389 » (pdftotext, sans jeu de casse) dans les
        fascicules français de 2017 à 2026 : trente fascicules — le décret, l'arrêté du JORT
        n° 38 de 2017 sur les commissions, le décret n° 2024-182, et vingt-sept visas ; aucun
        ne rattache l'annexe n° 2 à l'article 63. Loi n° 2017-66, art. 20, lu : il renvoie
        aux zones « au sens de l'article 63 » sans nommer de décret. Lacunes : le corpus
        français de 2018 ne compte que 70 fascicules ; aucun fascicule arabe parcouru au
        plein texte ; les notes communes de la direction générale des impôts, hors Journal
        officiel, non cherchées.
      couvert_jusqu_au: 2026-07-24
      resultat: aucun
  a_faire: >-
    chercher la note commune de la direction générale des impôts commentant les articles 63
    et 64 ; rejouer par scripts/recherches.py (FTS, miroir iort, fascicules arabes)

- id: r-fisc-zones-modif-99-483
  objet: >-
    texte modifiant la délimitation des zones d'encouragement au développement régional
    (décret n° 99-483) entre le décret n° 2008-387 du 11 février 2008 et l'abrogation du code
    de 1993
  ou: [precis/fr/fiscalite/_depenses_fiscales.qmd#sec-df-code-1993]
  requetes:
    titres_like:
      - '%developpement regional%zones%'
      - '%developpement regional%prime%'
      - '%99-483%'
    iort_ar:
      - '483 لسنة 1999'
      - '539 لسنة 1994'
      - 'التنمية الجهوية'
    plein_texte:
      - 'décret n° 99-483'
    depuis: 2008-02-11
  periode:
    jusqu_au: 2016-12-31
    motif: le code de 1993 est abrogé au 1er janvier 2017 (loi n° 2016-71, art. 26 à 29)
  passes:
    - date: 2026-10-11
      role: documentaliste
      sources: [jort_cache, corpus_local]
      couverture: >-
        titres de jort_cache (SQL sur la colonne titre ; le terme arabe « التنمية الجهوية »
        a été croisé avec « مناطق » ou « منح ») : le dernier texte visant le décret n° 99-483
        est le décret n° 2008-387 ; une seule notice arabe répond, le décret n° 2011-3197,
        qui modifie le décret des primes et non celui des zones. Plein texte « décret n° 99-483 » dans les quatre cents premières lignes
        (sommaire) de chaque fascicule français de 2008 à 2016 : seul le JORT n° 15 de 2008
        répond. Lacunes : sommaires de plus de quatre cents lignes non couverts ; fascicules
        sans couche texte non couverts ; édition arabe non parcourue (notices à intitulé arabe
        seul : 37 % en 2011, 40 à 70 % en 2015-2016).
      couvert_jusqu_au: 2016-12-31
      resultat: aucun

- id: r-fisc-modificatifs-2017-389
  objet: >-
    texte modifiant le décret gouvernemental n° 2017-389 du 9 mars 2017 (barème des primes,
    annexes, zones), autre que le décret n° 2024-182 du 4 avril 2024
  ou: [precis/fr/fiscalite/_depenses_fiscales.qmd#sec-df-reformes]
  requetes:
    titres_like:
      - '%2017-389%'
      - '%incitations financi%'
    iort_ar:
      - '389 لسنة 2017'
      - 'الحوافز المالية'
    plein_texte:
      - '2017-389'
    depuis: 2017-03-28
  passes:
    - date: 2026-10-11
      role: documentaliste
      sources: [jort_cache, corpus_local]
      couverture: >-
        titres de jort_cache (SQL sur la colonne titre) : une seule notice, le décret
        n° 2024-182 (JORT n° 47 de 2024), déjà connu. Plein texte des fascicules français de
        2017 à 2026 : les visas citent le décret sans modificatif jusqu'au JORT n° 23 de
        2024, puis « tel que modifié et complété par le décret n° 2024-182 », et lui seul,
        jusqu'au JORT n° 75 de 2026 (décret n° 2026-148 du 23 juillet 2026). Lacunes : corpus français de 2018 incomplet (70
        fascicules) ; actualisation des listes par la voie de l'article 4 du décret
        (approbation du conseil supérieur d'investissement) non cherchée hors Journal
        officiel.
      couvert_jusqu_au: 2026-07-24
      resultat: aucun
```

La troisième fiche soutient l'énoncé « seul modificatif » : elle porte sur tout texte autre
que le décret n° 2024-182, et se rejoue sur ce qui paraîtra. Les trois fiches décrivent des
requêtes lancées à la main (SQL et `pdftotext`), non par `scripts/recherches.py` : à leur
versement, les rejouer par l'outil, qui normalise autrement les accents et l'arabe.

---

## 5. Séries à verser dans `tunisia-data`

Rien n'y est versé ni committé par cette note, sauf un complément à la fiche de source (dernier
point).

| Série | Source, pages | Années | Travail |
|---|---|---|---|
| Avantages financiers par forme, par domaine, par bénéficiaire, **une ligne par (rapport, exercice)** | rapports 2021 (p. 93-96 imprimées), 2022 (p. 71-73), 2023 (p. 71-74 du PDF), 2024 (p. 69-72 du PDF), 2025 (p. 52-55) | 2018-2023 | transcription à l'image ; tableaux A et B de cette note en sont l'amorce |
| Avantages financiers **détaillés par code** (232 à 236 lignes par rapport), sur le modèle de `depenses_fiscales_detail_2017_2023.csv` | rapport 2021, annexe p. 99-110 imprimées ; rapport 2022, p. 74 et suivantes ; rapport 2023 ; rapport 2024, p. 73 et suivantes ; rapport 2025, p. 56-75 environ | 2018-2023 | extraction par script puis contrôle des sommes contre les tableaux n° 2 et n° 4 ; les rapports arabes rangent les colonnes en sens inverse |
| FOPRODI et FONAPRA : solde initial, dotations budgétaires, recouvrements, emplois, solde final | BCT, *Rapport annuel*, éditions 2017 à 2025, pages du PDF au tableau E | 2016-2025 | petite série, déjà relevée ici en dinars ; à verser avec contrôle solde initial + ressources − emplois = solde final |
| Commerce extérieur par régime, total **et par groupement sectoriel** | INS, *Annuaire statistique*, tableau 14.2, 22 éditions | 1998-2023 | script de relevé en place dans le répertoire de session (`regime.py`, `regime2.py`) ; à reprendre proprement, avec relecture à l'image de trois éditions témoins et table des valeurs écartées |
| Soldes des fonds spéciaux à la clôture | rapport sur les finances publiques 2010, p. 73 et 75 du PDF | 2005-2008 | quatre colonnes ; n'a d'intérêt qu'avec les éditions voisines |

**Fiche de source complétée** : `~/projets/tunisia-data/sources/gbo-depenses-fiscales.md`
reçoit une section datée du 11 octobre 2026 (six fichiers, adresses, empreintes SHA-256,
pages des tableaux d'avantages financiers, les trois ruptures du § 1.1). **Modification non
committée**, à relire. Aucun PDF nouveau n'a été téléchargé : tous les documents cités
étaient déjà dans `data/raw/`.

---

## 6. Ce qui touche le modèle `openfisca-tunisia`

Rien n'y est versé. À dire à `docs/notes/backlog-modele.md` si le rédacteur retient les
tableaux G à I :

- le **barème des primes** (taux, plafonds, durées de prise en charge) est une famille de
  paramètres datés, bien sourcés et simples (tableaux G, H, I) : candidats à un nœud
  `incitations/` ou équivalent, pour que les tableaux du chapitre soient engendrés plutôt que
  faits main. Dates : 1994 (date d'exécution non établie), 14 mars 1999 (sous réserve),
  25 février 2008, 19 mai 2011, 1er janvier 2017, 10 avril 2024 ;
- la **durée de prise en charge de la contribution patronale** (3, 5, 10 ans) recoupe le
  volume « Cotisations sociales » : vérifier qu'elle n'y est pas déjà paramétrée sous un autre
  chemin avant de la créer ;
- la **liste des délégations par groupe** n'est pas un paramètre chiffré ; si elle doit être
  portée, c'est une table de référence (délégation → groupe, par date), non un barème.

---

## 7. Annexe — listes des délégations

### 7.1 Décret gouvernemental n° 2017-389, annexe n° 2 (image, p. 1113-1116)

**Premier groupe (13).** Béja : Medjez El Bab. Zaghouan : Zaghouan, Bir M'chergua, Ez-Zeriba.
Sfax : Agareb, Djebeniana, El Amra, El Hancha, El Ghraiba, Skhira, Bir Ali Ben Khalifa, Menzel
Chaker. Sousse : Sidi El Hani.

**Deuxième groupe (134 ; 135 depuis le décret n° 2024-182).**

- Jendouba (9) : Jendouba, Jendouba Nord, Bou Salem, Tabarka, Aïn Draham, Fernana, Ghardimaou,
  Oued Meliz, Balta Bou Aouane.
- Kasserine (13) : Kasserine Nord, Kasserine Sud, Ezzouhour, Hassi El Frid, Sbeitla, Sbiba,
  Djedeliane, El Ayoun, Thala, Hidra, Foussana, Feriana, Mejel Bel Abbès.
- Kairouan (13) : Kairouan Nord, Kairouan Sud, Echbika, Sbikha, Haffouz, Hajeb El Ayoun,
  Nasrallah, Echrarda, Bouhajla, El Oueslatia, El Alaâ, Aïn Jloula, Menzel Mhiri.
- Siliana (11) : Bou Arada, Gaâfour, El Krib, El Aroussa, Siliana Nord, Siliana Sud, Bou
  Rouis, Bargou, Makthar, Er-Rouhia, Kesra.
- Sidi Bouzid (13) : Sidi Bouzid Ouest, Sidi Bouzid Est, Mezzouna, Regueb, Ouled Haffouz, Bir
  El Hafey, Sidi Ali Ben Aoûn, Menzel Bouzaïenne, Jilma, Cebalet Ouled Asker, Meknassy, Souk
  Jedid, Essaïda.
- Le Kef (12) : Kef Ouest, Kef Est, Nebeur, Sakiet Sidi Youssef, Tajerouine, Kalaât Sénan,
  Kalaât Khasba, Djérissa, El Ksour, Dahmani, Sers, Touiref.
- Tataouine (7) : Tataouine Nord, Tataouine Sud, Bir Lahmar, Smar, Ghomrassen, Dhehiba,
  Remada.
- Béja (8) : Béja Nord, Béja Sud, Teboursouk, Tibar, Testour, Goubellat, Nefza, Amdoun.
- Gafsa (13) : Gafsa Nord, Gafsa Sud, Sidi Aïch, El Ksar, Oum El Araies, Redeyef, Metlaoui,
  Mdhila, El Guetar, Belkhir, Sned, Sidi Boubaker, Zanouch.
- Médenine (5) : Médenine Sud, Médenine Nord, Ben Guerdane, Sidi Makhlouf, Béni Khedeche.
- Mahdia (4) : Chorbane, Essouassi, Hébira, Ouled Chamekh.
- Gabès (6, puis 7) : Mareth, El Hamma, Menzel El Habib, Nouvelle Matmata, Matmata, Dekhilet
  Toujane ; El Hamma Ouest (décret n° 2024-182, art. 5).
- Kébili (7) : Kébili Sud, Kébili Nord, Souk El Ahad, Douz Nord, Douz Sud, El Faouar, Réjim
  Maatoug.
- Zaghouan (3) : El Fahs, Saouaf, En-Nadhour.
- Tozeur (6) : Tozeur, Dégach, Tamaghza, Nefta, Hazoua, Hammet El Djérid.
- Bizerte (3) : Djoumine, Ghézala, Sedjnane.
- Sfax (1) : Kerkennah.

### 7.2 Décret n° 2008-387, annexe n° 1 (nouveau) (texte, p. 745-746)

**Premier groupe (10).** Zaghouan : Zaghouan, Bir M'chergua. Béja : Medjez El Bab. Sousse :
Sidi El Hani. Sfax : Agareb, Djebeniana, El Amra, El Hancha, El Ghraiba, Skhira.

**Deuxième groupe (40).** Zaghouan (3) : Ez-Zeriba, El Fahs, Saouaf. Bizerte (2) : Djoumine,
Ghézala. Béja (6) : Béja Nord, Béja Sud, Teboursouk, Tibar, Testour, Goubellat. Siliana (4) :
Bou Arada, Gaâfour, El Krib, El Aroussa. Mahdia (4) : Chorbane, Essouassi, Hébira, Ouled
Chamekh. Sfax (2) : Bir Ali Ben Khalifa, Menzel Chaker. Kairouan (9) : Kairouan Nord, Kairouan
Sud, Echebika, Sbikha, Haffouz, Hajeb El Ayoun, Nasrallah, Echrarda, Bouhajla. Sidi Bouzid
(5) : Sidi Bouzid Ouest, Sidi Bouzid Est, Mezzouna, Regueb, Ouled Haffouz. Gabès (1) : Mareth.
Médenine (4) : Médenine Nord, Médenine Sud, Ben Guerdane, Sidi Makhlouf.

**Zones prioritaires (88).** Zaghouan (1) : En-Nadhour. Bizerte (1) : Sedjnane. Béja (2) :
Nefza, Amdoun. Siliana (7) : Siliana Nord, Siliana Sud, Bou Rouis, Bargou, Makthar, Er-Rouhia,
Kesra. Jendouba (9) : les neuf délégations de la liste de 2017. Le Kef (11) : les douze de
2017 moins Touiref. Sfax (1) : Kerkennah. Kairouan (2) : Oueslatia, El Alâa. Kasserine (13) :
les treize de 2017. Sidi Bouzid (7) : Bir El Hafey, Sidi Ali Ben Aoûn, Menzel Bouzaïenne,
Jilma, Cebalet Ouled Asker, Meknassy, Souk Jedid. Gabès (4) : El Hamma, Menzel El Habib,
Nouvelle Matmata, Matmata. Médenine (1) : Béni Khedeche. Tataouine (7) : les sept de 2017.
Gafsa (11) : les treize de 2017 moins Sidi Boubaker et Zanouch. Tozeur (5) : les six de 2017
moins Hammet El Djérid. Kébili (6) : les sept de 2017 moins Réjim Maatoug.

### 7.3 Décrets de 1994 et de 1999

Reproduits au tableau J (gouvernorats entiers et nombre de délégations par gouvernorat) ; le
détail nominatif est aux pages citées (1994 : p. 454-455 ; 1999 : p. 359). Les annexes
touristiques (tourisme saharien, de montagne, côtier du Nord ; en 1999, tourisme culturel et
thermal par site) ne sont pas reprises.

---

## 8. Journal

- Lus : `AGENTS.md`, `docs/agents/documentaliste.md` (par la consigne du rôle),
  `docs/notes/outillage-sources.md`, `docs/notes/fiscalite-depenses-fiscales.md` (§ 2.2, 7 à
  10), `precis/fr/fiscalite/_depenses_fiscales.qmd` (sections des réformes et du coût),
  `~/projets/tunisia-data/sources/gbo-depenses-fiscales.md`.
- Aucune océrisation. Deux recherches plein texte sur les fascicules ont tourné en fond après
  dépassement du délai de la commande ; l'une a été arrêtée (processus de cette session
  seulement), l'autre s'est terminée ; aucun processus ne reste.
- Rien n'est écrit dans `PDFs-legislation-tunisie`. Dans `tunisia-data` : une section ajoutée
  à `sources/gbo-depenses-fiscales.md`, non committée.
- Fichiers de travail (hors dépôt) : répertoire de session `…/scratchpad/inc_work/`.

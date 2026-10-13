# Incitations à l'investissement : crédits de loi de finances avant 2017 — second passage documentaire, 13 octobre 2026

Complément borné à `docs/notes/fiscalite-incitations-primes-zones-2026-10-11.md` (§ 1.2, 1.3, 1.8
et 4.1, point 1) et aux TODO du chapitre `precis/fr/fiscalite/_depenses_fiscales.qmd` (« crédits
budgétaires des primes et des prises en charge » ; « FOPRODI avant 2016 »). Une seule question :
quels crédits les lois de finances ouvrent-elles, de 1995 à 2017, au FOPRODI, aux primes
d'investissement, au FODEC et aux prises en charge de cotisations patronales ?

**Passage échantillonné, non exhaustif** : treize lois de finances lues sur vingt-trois ; ce qui
manque est dit au § 4.

**Depuis le troisième passage (§ 10)** : la prise en charge patronale est lue pour les
vingt-trois lois de finances de 1995 à 2017 (1998 sous réserve), le FOPRODI de 2000 à 2017 ; les
lacunes à jour sont au § 10.5.

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
`docs/notes/outillage-sources.md`). Les adresses pist.tn sont contrôlées au troisième passage (§ 10.4).

## 1. Le constat de nomenclature, qui commande tout le reste

1. **Le FOPRODI ne figure pas au tableau des fonds spéciaux du Trésor**, ni en 1995 (tableau
   « K », 19 comptes — image), ni en 2005 (tableau « B », 20 comptes — image), ni de 2011 à 2017
   (tableau « B » — texte). Le tableau des fonds spéciaux n'est donc **pas** la source de la série.
2. **Depuis 1999 au moins, le FOPRODI est une ligne du tableau des crédits de programmes de l'État**, au chapitre du
   ministère chargé de l'industrie, sous la rubrique « II - Financement public » : « Fonds de
   promotion et de décentralisation industrielle », un montant, sans détail (lu de 2000 à 2017 ; en 1999 sous l'intitulé « Fonds du développement et de la décentralisation industrielle », montant illisible).
   C'est cohérent avec la colonne « dotations budgétaires » du tableau de la BCT (note du
   11 octobre, § 1.2) : le fonds est alimenté par une dotation du budget, non par une recette
   affectée.
3. **La prise en charge des cotisations patronales a sa ligne propre**, dans le même tableau, au
   chapitre du ministère des Affaires sociales : « Prise en charge par l'État de la contribution
   patronale au régime légal de la sécurité sociale » — « projets nouveaux à caractère national »
   de 1995 à 1997 (dernière ligne d'un groupe « B »), « II/ Financement public » à partir de 1998 (§ 10.3). La ligne ne dit pas au titre de quel
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
| 1996 | **non établi** | n° 95-109 du 25 décembre 1995 | n° 104, 29-31 décembre 1995 | — | OCR de repérage (p-fichier 40 à 111) muet sur le fonds ; chapitre de l'industrie non lu à l'image |
| 1997 | **non établi** | n° 96-113 du 30 décembre 1996 | n° 105, 31 décembre 1996 | — | OCR de repérage (p-fichier 40 à 111) muet ; chapitre de l'industrie non lu à l'image. Tableau des fonds spéciaux, p. 2624 (pied OCR) — image : au ministère de l'Industrie, le seul FODEC (26 000 000 D) |
| 1998 | **non établi** | n° 97-88 du 29 décembre 1997 | n° 104, 30-31 décembre 1997 | p. 2475 (pied OCR, contigu à la p. 2474 lue à l'image) | image, haut de page seulement : le chapitre 14 (Industrie) porte une rubrique « II - Financement Public » (Agence de promotion de l'industrie, Agence de la maîtrise de l'énergie, Office national des mines, INNORPI, Laboratoire central) ; bas de la page non lu |
| 1999 | **ligne présente, montant illisible** | n° 98-111 du 28 décembre 1998 | n° 104, 29-31 décembre 1998 | p. 2544 (pied OCR, décalage cohérent avec la p. 2567 lue à l'image) | image à 150 et 300 points par pouce : « Fonds du développement et de la décentralisation industrielle » (sic), dernière ligne de « II/- Financement Public » ; montant à un seul chiffre de millions, mal imprimé, non lu ; Total II 8 312 000, total du chapitre 8 266 000 |
| 2000 | **13,0** | n° 99-101 du 31 décembre 1999 | n° 105, 31 décembre 1999 | p. 2775 | image |
| 2001 | **28,0** | n° 2000-98 du 25 décembre 2000 | n° 104, 29 décembre 2000 | p. 3206 | image (valeur et pied) ; Total II 30 607 000, recoupé par addition des cinq lignes |
| 2002 | **33,0** | n° 2001-123 du 28 décembre 2001 | n° 104, 28 décembre 2001 | p. 4286 | image (valeur et pied) ; Total II 35 455 000 |
| 2003 | **39,0** | n° 2002-101 du 17 décembre 2002 | n° 102, 17 décembre 2002 | p. 2911 | image (valeur et pied) ; chiffres soulignés, sans total de recoupement lu |
| 2004 | **33,0** | n° 2003-80 du 29 décembre 2003 | n° 104, 30 décembre 2003 | p. 3757 | image (valeur et pied) ; chiffres soulignés, sans total de recoupement lu |
| 2005 | **37,0** | n° 2004-90 du 31 décembre 2004 | n° 105, 31 décembre 2004 | p. 3471 | image |
| 2006 | **35,0** | n° 2005-106 du 19 décembre 2005 | n° 101, 20 décembre 2005 | p. 3627 | image (valeur et pied) ; Total II 39 957 000 |
| 2007 | **35,0** | n° 2006-85 du 25 décembre 2006 | n° 103, 26 décembre 2006 | p. 4417 | image (valeur et pied, pied relu au troisième passage) |
| 2008 | **35,0** | n° 2007-70 du 27 décembre 2007 | n° 104, 28-31 décembre 2007 | p. 4392 | image |
| 2008, loi de finances complémentaire | 35,0, « sans changement » | n° 2008-76 du 15 décembre 2008 | n° 101, 16 décembre 2008 | p. 4176 | texte |
| 2009 | **42,0** | n° 2008-77 du 22 décembre 2008 | n° 104, 26 décembre 2008 | p. 4306 | image (valeur et pied, pied relu au troisième passage) |
| 2010 | **42,0** | n° 2009-71 du 21 décembre 2009 | n° 102, 22 décembre 2009 | p. 3957 | image |
| 2011 | **48,0** | n° 2010-58 du 17 décembre 2010 | n° 102, 21 décembre 2010 | p. 3526 | image (valeur et pied) ; couche texte concordante |
| 2012 | **58,0** | n° 2011-7 du 31 décembre 2011 | n° 1, 3 janvier 2012 | p. 39 | image (valeur et pied) ; couche texte concordante |
| 2013 | **65,0** | n° 2012-27 du 29 décembre 2012 | n° 1, 1er janvier 2013 | p. 55 | image (valeur et pied) ; couche texte concordante |
| 2014 | **65,0** | n° 2013-54 du 30 décembre 2013 | n° 105, 31 décembre 2013 | p. 3732 | image (valeur et pied) ; voir (a) |
| 2015 | **55,0** | n° 2014-59 du 26 décembre 2014 | n° 105, 30 décembre 2014 | p. 3507 | image (valeur et pied) ; ligne de tête et ligne de détail : 55 000 000 |
| 2016 | **55,0** | n° 2015-53 du 25 décembre 2015 | n° 104, 29 décembre 2015 (édition arabe) | p. 3660 de l'édition arabe | image de l'édition arabe (valeur et pied) ; ligne de tête et ligne de détail « صندوق التطوير واللامركزية الصناعية » : 55 000 000 |
| 2017 | **49,0** | n° 2016-78 du 17 décembre 2016 | n° 105, 27 décembre 2016 | p. 3889 | image (valeur et pied) ; ligne de tête et ligne de détail : 49 000 000 |

Réserves :

- (a) **2014, tranché à l'image (p. 3732-3733)** : la page imprimée porte bien les deux lignes.
  La première, en gras souligné, « Fonds de Promotion et de Décentralisation Industrielle
  66 592 000 », est un **intitulé de groupe** ; la seconde, « -Fonds de Promotion et de
  Décentralisation Industrielle 65 000 000 », est la ligne de détail du fonds. Les sept lignes
  suivantes, rangées sous le même intitulé, sont des actions d'énergie (maintenance des
  équipements 245 000 ; études sur l'énergie 100 000 ; équipements 42 000 ; acquisition de
  matériels roulants 145 000 ; suivi et contrôle des émissions de gaz à effet de serre 450 000 ;
  développement économique de faibles émissions de carbone — transition énergétique 600 000 ;
  projet régional pour la promotion des énergies renouvelables 10 000), soit 1 592 000 :
  65 000 000 + 1 592 000 = 66 592 000. Lecture probable : l'intitulé de groupe de ces lignes
  d'énergie manque au tableau imprimé, et le total du groupe du fonds les absorbe. **La ligne
  de détail du fonds est à 65 000 000 D.** Ce n'est pas un décalage de la couche texte.
- (b) **Valeurs de 2011 à 2017** : relues à l'image au troisième passage (§ 10) ; aucun écart
  avec la couche texte.
- (c) **Constat de contrôle, pas un raccord** : le crédit de programmes pour 2017 (49,0 MD) est
  égal à la « dotation budgétaire » de 2017 du tableau de la BCT (49,00 MD, note du 11 octobre,
  § 1.2) ; celui pour 2016 (55,0 MD) ne l'est pas (47,00 MD à la BCT). Les deux grandeurs ne sont
  donc pas interchangeables.
- (d) Les lois de finances rectificatives ou complémentaires ne sont pas relevées, sauf celle de
  décembre 2008, rencontrée au passage.

Lecture brute, pour le rédacteur : le crédit ouvert au FOPRODI est de 13 MD (2000), 28 MD (2001),
33 MD (2002), 39 MD (2003), 33 MD (2004), 37 MD (2005), 35 MD (2006 à 2008), 42 MD (2009 et 2010),
48 MD (2011), 58 MD (2012), 65 MD (2013 et 2014), 55 MD (2015 et 2016), 49 MD (2017). En dinars
courants ; série continue de 2000 à 2017, toutes valeurs lues à l'image ; 1996 à 1999 non
établies (la ligne existe en 1999, montant illisible).

### 2.2 Prise en charge par l'État de la contribution patronale au régime légal de sécurité sociale — crédits de programmes, chapitre du ministère des Affaires sociales (millions de dinars)

| Loi de finances pour | Crédit (MD) | Loi | JORT n°, date | Page | Rubrique du tableau | Mode de lecture |
|---|---:|---|---|---|---|---|
| 1995 | **3,0** | n° 94-127 | n° 103, 30-31 décembre 1994 | p. 2115 | tableau « F », « 3) Projets nouveaux — B. Projets à caractère national » | image |
| 1996 | **3,0** | n° 95-109 | n° 104, 29-31 décembre 1995 | p. 2423 | « Prise en charge de la contribution patronale au régime légal de la Sécurité Sociale », dernière ligne d'un groupe « B » (« Projets à caractère national » d'après l'OCR, intitulé non relu) ; S/Total B 4 340 000 | image (valeur et pied ; l'OCR lisait « 2429 ») |
| 1997 | **4,0** | n° 96-113 | n° 105, 31 décembre 1996 | p. 2618 (pied OCR) | « Prise en charge de la contribution patronale au régime légal de la sécurité du travail » (sic) ; Sous Total B 5 706 000 | image (valeur) ; pied non relu à l'image |
| 1998 | **3,5 — lecture douteuse** | n° 97-88 | n° 104, 30-31 décembre 1997 | p. 2503 (pied OCR, décalage cohérent avec la p. 2474 lue à l'image) | « II/- FINANCEMENT PUBLIC » — première année où la ligne est lue sous cette rubrique ; « Prise en charge par l'Etat de la Contribution Patronale au Régime légal de la Sécurité Sociale » ; Total II lu « 3 580 000 » | image à 150 et 300 points par pouce : le chiffre des centaines de mille est mal imprimé, dans la ligne comme dans le total ; « 3 500 000 » est la lecture la plus probable, non assurée |
| 1999 | **4,0** | n° 98-111 | n° 104, 29-31 décembre 1998 | p. 2567 | « * Prise en Charge par l'Etat de la Contribution Patronale au Régime Légal de la Sécurité Sociale » ; Total II 4 057 000 = 4 000 000 + 57 000 (Office des Tunisiens à l'étranger) | image (valeur mal imprimée, confirmée par le total ; pied lu) |
| 2000 | **5,5** | n° 99-101 | n° 105, 31 décembre 1999 | p. 2791 | « II/ Financement public » | image |
| 2001 | **5,5** | n° 2000-98 | n° 104, 29 décembre 2000 | p. 3219 | « II/- Financement Public » ; Total II 5 562 000 (avec 62 000 pour l'Office des Tunisiens à l'étranger) | image (valeur et pied) |
| 2002 | **9,0** | n° 2001-123 | n° 104, 28 décembre 2001 | p. 4301 | idem ; Total II 9 045 000 | image (valeur et pied) |
| 2003 | **10,0** | n° 2002-101 | n° 102, 17 décembre 2002 | p. 2926 | idem ; Total II 10 040 000 | image (valeur et pied) |
| 2004 | **13,0** | n° 2003-80 | n° 104, 30 décembre 2003 | p. 3773 | idem ; Total II 13 028 000 | image (valeur et pied) |
| 2005 | **18,0** | n° 2004-90 | n° 105, 31 décembre 2004 | p. 3488 | tableau « D », « II/ Financement public » (total II : 18,038 MD) | image |
| 2006 | **24,0** | n° 2005-106 | n° 101, 20 décembre 2005 | p. 3643 | « II/- Financement Public » (lettre du tableau non relue) ; Total II 24 038 000 | image (valeur et pied) |
| 2007 | **35,0** | n° 2006-85 | n° 103, 26 décembre 2006 | p. 4437 | idem (total II : 35,036 MD) | image (valeur et pied, pied relu au troisième passage) |
| 2008 | **35,0** | n° 2007-70 | n° 104, 28-31 décembre 2007 | p. 4410 | idem (total II : 35,075 MD) | image |
| 2009 | **35,0** | n° 2008-77 | n° 104, 26 décembre 2008 | p. 4325 | idem (total II : 42,390 MD, avec 7,390 MD pour l'Office des Tunisiens à l'étranger) | image (valeur et pied, pied relu au troisième passage) |
| 2010 | **40,0** | n° 2009-71 | n° 102, 22 décembre 2009 | p. 3999 | idem ; Total II 40 210 000 (avec 210 000 pour l'Office des Tunisiens à l'étranger) | image (valeur et pied) |
| 2011 | **44,0** | n° 2010-58 | n° 102, 21 décembre 2010 | p. 3565 | « II- Financement Public » ; Total II 44 217 000 | image (valeur et pied) |
| 2012 | **55,0** | n° 2011-7 | n° 1, 3 janvier 2012 | p. 59 | la ligne passe sous un groupe « * Caisse Nationale de la Sécurité Sociale » 59 000 000, avec « Délivrance de la Caisse Nationale de la Sécurité Sociale » 4 000 000 ; Total II 59 278 000 | image (valeur et pied) |
| 2013 | **60,0** | n° 2012-27 | n° 1, 1er janvier 2013 | p. 78 | groupe « * Caisse Nationale de la Sécurité Sociale » 64 000 000, avec « Réglement de la Caisse Nationale de la Sécurité Sociale » 4 000 000 ; Total II 64 040 000 | image (valeur et pied) |
| 2014 | **54,0** | n° 2013-54 | n° 105, 31 décembre 2013 | p. 3761 | « II-Financement Publique » ; groupe « Caisse Nationale de la Sécurité Sociale » 58 050 000 = 54 000 000 + 4 000 000 (imprimé sans libellé propre, face à la seconde ligne du libellé de la prise en charge) + « Equipements divers » 30 000 + « Equipements informatiques » 20 000 ; Total II 58 050 000 | image (valeur et pied) |
| 2015 | **47,429** | n° 2014-59 | n° 105, 30 décembre 2014 | p. 3534 | « 2-Projets et programmes nouveaux » ; groupe « Caisse nationale de la sécurité sociale » 51 429 000, avec « Règlement de la CNSS » 4 000 000 ; Total II 52 130 000 | image (valeur et pied) |
| 2016 | **41,788** | n° 2015-53 | n° 104, 29 décembre 2015 (édition arabe) | p. 3688 de l'édition arabe | « II- التمويل العمومي », « 2- مشاريع وبرامج جديدة » ; groupe « الصندوق الوطني للضمان الاجتماعي » 120 788 000 = 41 788 000 + « خلاص الصندوق الوطني للضمان الإجتماعي » 4 000 000 + « تدخلات إستثنائية لفائدة القطاع السياحي » 75 000 000 | image de l'édition arabe (valeur et pied) |
| 2017 | **37,105** | n° 2016-78 | n° 105, 27 décembre 2016 | p. 3921 | « II-Financement public », « 2-Projets et Programmes nouveaux » ; groupe « Caisse nationale de la sécurité nationale » (sic) 41 105 000, avec « Règlement de la caisse nationale de la sécurité sociale » 4 000 000 | image (valeur et pied) |

Série continue de 1995 à 2017 après le troisième passage (§ 10), toutes valeurs lues à l'image,
celle de 1998 sous réserve. La ligne existe dès la loi de finances pour 1995 — deuxième exercice
du code de 1993 —, rangée jusqu'en 1997 dans un groupe « B » de projets (intitulé lu à l'image en 1995 seulement), et sous
« Financement public » à partir de 1998 : 3,0 MD (1995 et 1996), 4,0 MD (1997), 3,5 MD lu sous
réserve (1998), 4,0 MD (1999), 5,5 MD (2000 et 2001), 9,0 (2002), 10,0 (2003), 13,0 (2004),
18,0 (2005), 24,0 (2006), 35,0 (2007 à 2009), 40,0 (2010), 44,0 (2011), 55,0 (2012), 60,0
(2013), 54,0 (2014), 47,429 (2015), 41,788 (2016), 37,105 MD (2017), en dinars courants. De
2012 à 2017 la ligne est une composante d'un groupe « Caisse nationale de sécurité sociale »,
qui porte aussi 4,0 MD de « règlement » de la caisse et, en 2016, 75,0 MD d'interventions
exceptionnelles au profit du secteur touristique : **le total du groupe n'est pas la prise en
charge.** Rappel : crédit voté, tous régimes de prise en charge confondus ; rien ne dit ce qui a
été payé à la CNSS (note du 11 octobre, § 1.8).

### 2.3 FODEC — pour mémoire (hors périmètre : ligne unique, sans distinction des primes)

Prévisions de recettes du fonds au tableau des fonds spéciaux du Trésor, en millions de dinars :

| Loi de finances pour | Recettes prévues (MD) | Tableau, page | Mode de lecture |
|---|---:|---|---|
| 1995 | 20,0 (recettes propres ; subvention du budget : néant ; dépenses : 20,0) | « K », JORT n° 103 de 1994, p. 2126 | image |
| 1997 | 26,0 | tableau des fonds spéciaux, JORT n° 105 de 1996, p. 2624 (pied OCR) | image |
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
  patronale de 1995 à 2017 (1998 sous réserve) ; seuls restent des trous pour le FOPRODI avant 2000 (§ 10.5) ; elle et ne vaut pas « sommes versées » :
  la phrase du chapitre « aucune série de sommes versées n'est établie ici pour les exercices
  antérieurs à 2016 » **demeure exacte**.
- Les primes d'investissement de l'agriculture (APIA, fonds spécial de développement agricole), du
  tourisme et de l'artisanat (FONAPRA) n'ont pas été cherchées : mêmes tableaux, autres chapitres.

## 4. Ce qui n'est pas établi, et la suite précise

**État au second passage, conservé pour mémoire.** Les points 2 (sauf le FOPRODI de 1996 à 1999), 3 et 5 sont
levés par le troisième passage ; l'état à jour des lacunes est au § 10.5.

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

Relevé par script sur la couche texte (ou l'OCR de repérage pour 2010), ajouté en fin de second passage. **Relu à l'image au troisième passage et reporté au tableau du § 2.2**, qui fait foi ; la ligne de 2010, muette ici, est p. 3999.

- LF 2011, `2010/fr/Jo1022010.pdf`, page-fichier 109, pied « N° 102 Journal Officiel de la République Tunisienne — 21 décembre 2010 Page 3565 » : II- Financement Public ⏎ - Prise en charge par l'Etat de la contribution patronale au ⏎ régime légal de la sécurité sociale  44 000 000 ⏎ - Office des Tunisiens à l'Etranger  217 000
- LF 2012, `2012/fr/Jo0012012.pdf`, page-fichier 59, pied « N° 1 Journal Officiel de la République Tunisienne — 3 janvier 2012 Page 59 » : * Caisse Nationale de la Sécurité Sociale  59 000 000 ⏎ - Prise en charge par l'Etat de la contribution patronale au ⏎ régime légal de la sécurité sociale  55 000 000 ⏎ - Délivrance de la Caisse Nationale de la Sécurité Sociale  4
- LF 2013, `2013/fr/Jo0012013.pdf`, page-fichier 78, pied « Page 78 Journal Officiel de la République Tunisienne — 1er janvier 2013 N° 1 » : * Caisse Nationale de la Sécurité Sociale  64 000 000 ⏎ - Prise en charge par l'Etat de la contribution patronale au régime ⏎ 60 000 000 ⏎ légal de la sécurité sociale
- LF 2014, `2013/fr/Jo1052013.pdf`, page-fichier 109, pied « N° 105 Journal Officiel de la République Tunisienne — 31 décembre 2013 Page 3761 » : Caisse Nationale de la Sécurité Sociale  58 050 000 ⏎ -Prise en charge par l’Etat de la contribution patronale au régime  54 000 000 ⏎ légal de la sécurité sociale  4 000 000 ⏎ -Equipements divers  30 000
- LF 2015, `2014/fr/Jo1052014.pdf`, page-fichier 74, pied « Page 3534 Journal Officiel de la République Tunisienne — 30 décembre 2014 N° 105 » : Prise en charge par l'Etat de la contribution ⏎ patronale au régime légal de la sécurité sociale  47 429 000 ⏎ Règlement de la CNSS  4 000 000
- LF 2016, `2015/ar/Ja1042015.pdf`, page-fichier 96, pied « ‫ﻋـــﺪد ‪104‬‬ ‫اﻟﺮاﺋﺪ اﻟﺮﺳﻤﻲ ﻟﻠﺠﻤﻬﻮرﻳﺔ اﻟﺘﻮﻧﺴﻴﺔ –– ‪ 29‬دﻳﺴﻤﺒﺮ ‪2015‬‬ ‫ﺻﻔﺤــﺔ ‪3688‬‬ » : ‫‪120 788 000‬‬  ‫اﻟﺼﻨﺪوق اﻟﻮﻃﻨﻲ ﻟﻠﻀﻤﺎن اﻻﺟﺘﻤﺎﻋﻲ‬ ⏎ ‫‪41 788 000‬‬  ‫ﺗﻜﻔﻞ اﻟﺪوﻟﺔ ﺑﻤﺴﺎﻫﻤﺔ اﻷﻋﺮاف ﻓﻲ اﻟﻨﻈﺎم اﻟﻘﺎﻧﻮﻧﻲ‬ ⏎ ‫ﻟﻠﻀﻤﺎن اﻹﺟﺘﻤﺎﻋﻲ‬ ⏎ ‫‪4 000 000‬‬  ‫ﺧﻼص اﻟﺼﻨﺪوق اﻟﻮﻃﻨﻲ ﻟﻠﻀﻤﺎن اﻹﺟﺘﻤﺎﻋﻲ‬
- LF 2017, `2016/fr/Jo1052016.pdf`, page-fichier 97, pied « N° 105 Journal Officiel de la République Tunisienne — 27 décembre 2016 Page 3921 » : Caisse nationale de la sécurité nationale  41 105 000 ⏎ Prise en charge par l’Etat de la contribution patronale au ⏎ 37 105 000 ⏎ régime légal de la sécurité sociale
- LF 2010, OCR de repérage des p. 26-80 du JORT n° 102 de 2009 (aucune valeur à en tirer) : aucune occurrence

## 10. Troisième passage, 13 octobre 2026

Passage borné : relecture à l'image des valeurs « texte » du second passage, années manquantes,
adresses pist.tn. Les tableaux des § 2.1 et 2.2 sont mis à jour en place ; cette section dit ce
qui a été fait et ce qui reste.

### 10.1 Méthode

- Fascicules à couche texte (2010 à 2016) : la ligne est repérée par ses coordonnées dans la
  couche texte (`pdftotext -bbox`), la bande de la page est rendue à 150 points par pouce et lue
  à l'image, avec le pied de page.
- Fascicules de 1995 à 2009 : les tableaux sont des images (la couche texte de 2000 à 2005 ne
  couvre que les articles de la loi et les sommaires). OCR de repérage au premier plan, par
  plages de 25 pages au plus, puis bande rendue à 150 points par pouce (300 pour deux valeurs
  mal imprimées) et lue à l'image. **Aucune valeur ne repose sur l'OCR.** L'OCR s'est encore
  trompé sur un pied de page (« 2429 » pour 2423, JORT n° 104 de 1995) et a manqué « patronale »
  dans le fascicule de 1998.
- Numéro et date des lois n° 95-109, 96-113, 97-88, 98-111, 2000-98, 2001-123, 2002-101, 2003-80
  et 2005-106 : lus au sommaire du fascicule (couche texte). Numéro et date de fascicule : lus au
  pied de page à l'image, sauf le n° 105 de 1996 (pied lu par OCR seulement).

### 10.2 Écarts entre la couche texte du second passage et l'image

**Aucun écart de valeur**, ni pour le FOPRODI (2011 à 2017), ni pour la prise en charge patronale
(2011 à 2017, § 9). Trois précisions que seule l'image donne :

1. **FOPRODI, loi de finances pour 2014** : réserve (a) du § 2.1 — 66 592 000 est le total d'un
   groupe qui absorbe sept lignes d'énergie (1 592 000) ; le fonds est à 65 000 000.
2. **Prise en charge, loi de finances pour 2014** (p. 3761) : le montant de 4 000 000 imprimé
   face à « légal de la sécurité sociale » n'appartient pas à la prise en charge ; il n'a pas de
   libellé propre sur la page (les tableaux pour 2012, 2013, 2015, 2016 et 2017 portent à cette
   place un « règlement » de la caisse, de 4 000 000). La prise en charge est 54 000 000.
3. **Pieds de page de 2007 et de 2009** : p. 4417 et 4437 (n° 103, 26 décembre 2006), p. 4306 et
   4325 (n° 104, 26 décembre 2008), confirmés à l'image.

### 10.3 Nomenclature : ce que les années nouvelles apportent

- La rubrique **« II - Financement public »** est lue pour la première fois dans la loi de
  finances pour **1998** (chapitre de l'Industrie, p. 2475, et chapitre des Affaires sociales,
  p. 2503). En 1996 et 1997, la prise en charge patronale est encore la dernière ligne d'un
  groupe « B » de projets, comme en 1995.
- Le libellé du fonds varie : « Fonds du développement et de la décentralisation industrielle »
  (1999) ; « Fonds de promotion et de la décentralisation industrielle » (2001 à 2003) ; « Fonds
  de promotion et de décentralisation industrielle » (2004 et après).
- Le libellé de la prise en charge est stable, à une coquille près en 1997 (« sécurité du
  travail »). La ligne est seule sous « Financement public », avec l'Office des Tunisiens à
  l'étranger, jusqu'en 2011 ; de 2012 à 2017 elle est rangée sous un groupe « Caisse nationale de
  sécurité sociale » (§ 2.2).
- Les tableaux des fonds spéciaux du Trésor des lois de finances pour 1997 (p. 2624) et pour 1999
  (p. 2579, pied OCR) ne portent, au ministère de l'Industrie, que le FODEC — image ; le constat 1
  du § 1 vaut donc aussi pour ces deux années. Les montants du tableau de 1999 sont mal imprimés
  et ne sont pas relevés.

### 10.4 Adresses pist.tn

Convention `https://www.pist.tn/jort/<année>/<année>F/<fichier>.pdf` (`A` et `Ja…` pour l'arabe) ;
le nom du fichier porte l'année sur deux chiffres jusqu'en 1999, sur quatre ensuite. Une boucle
`curl -skI` du 13 octobre 2026 (certificat du site échu) : les vingt-cinq adresses répondent 200,
`application/pdf`, avec **une taille égale à l'octet près à celle du fichier du corpus local**, qui
est celui qui a été lu. La langue servie n'a pas été contrôlée par ouverture du fichier distant
(`docs/notes/outillage-sources.md`, § 3) ; l'identité de taille avec le fichier local lu en tient
lieu ici.

| Fascicule | Adresse | Code | Type | Taille servie | Taille locale | Comparaison |
|---|---|---|---|---:|---:|---|
| n° 103 de 1994 (LF 1995) | <https://www.pist.tn/jort/1994/1994F/Jo10394.pdf> | 200 | application/pdf | 10039321 | 10039321 | identique |
| n° 104 de 1995 (LF 1996) | <https://www.pist.tn/jort/1995/1995F/Jo10495.pdf> | 200 | application/pdf | 10207182 | 10207182 | identique |
| n° 105 de 1996 (LF 1997) | <https://www.pist.tn/jort/1996/1996F/Jo10596.pdf> | 200 | application/pdf | 8176663 | 8176663 | identique |
| n° 104 de 1997 (LF 1998) | <https://www.pist.tn/jort/1997/1997F/Jo10497.pdf> | 200 | application/pdf | 7143099 | 7143099 | identique |
| n° 104 de 1998 (LF 1999) | <https://www.pist.tn/jort/1998/1998F/Jo10498.pdf> | 200 | application/pdf | 6876028 | 6876028 | identique |
| n° 105 de 1999 (LF 2000) | <https://www.pist.tn/jort/1999/1999F/Jo10599.pdf> | 200 | application/pdf | 13203090 | 13203090 | identique |
| n° 104 de 2000 (LF 2001) | <https://www.pist.tn/jort/2000/2000F/Jo1042000.pdf> | 200 | application/pdf | 6808197 | 6808197 | identique |
| n° 104 de 2001 (LF 2002) | <https://www.pist.tn/jort/2001/2001F/Jo1042001.pdf> | 200 | application/pdf | 9841377 | 9841377 | identique |
| n° 102 de 2002 (LF 2003) | <https://www.pist.tn/jort/2002/2002F/Jo1022002.pdf> | 200 | application/pdf | 9740535 | 9740535 | identique |
| n° 104 de 2003 (LF 2004) | <https://www.pist.tn/jort/2003/2003F/Jo1042003.pdf> | 200 | application/pdf | 10211222 | 10211222 | identique |
| n° 105 de 2004 (LF 2005) | <https://www.pist.tn/jort/2004/2004F/Jo1052004.pdf> | 200 | application/pdf | 12541013 | 12541013 | identique |
| n° 101 de 2005 (LF 2006) | <https://www.pist.tn/jort/2005/2005F/Jo1012005.pdf> | 200 | application/pdf | 9391547 | 9391547 | identique |
| n° 103 de 2006 (LF 2007) | <https://www.pist.tn/jort/2006/2006F/Jo1032006.pdf> | 200 | application/pdf | 9184317 | 9184317 | identique |
| n° 104 de 2007 (LF 2008) | <https://www.pist.tn/jort/2007/2007F/Jo1042007.pdf> | 200 | application/pdf | 15944798 | 15944798 | identique |
| n° 101 de 2008 (LFC 2008) | <https://www.pist.tn/jort/2008/2008F/Jo1012008.pdf> | 200 | application/pdf | 300395 | 300395 | identique |
| n° 104 de 2008 (LF 2009) | <https://www.pist.tn/jort/2008/2008F/Jo1042008.pdf> | 200 | application/pdf | 7024523 | 7024523 | identique |
| n° 102 de 2009 (LF 2010) | <https://www.pist.tn/jort/2009/2009F/Jo1022009.pdf> | 200 | application/pdf | 12067079 | 12067079 | identique |
| n° 102 de 2010 (LF 2011) | <https://www.pist.tn/jort/2010/2010F/Jo1022010.pdf> | 200 | application/pdf | 1787624 | 1787624 | identique |
| n° 1 de 2012 (LF 2012) | <https://www.pist.tn/jort/2012/2012F/Jo0012012.pdf> | 200 | application/pdf | 1535039 | 1535039 | identique |
| n° 1 de 2013 (LF 2013) | <https://www.pist.tn/jort/2013/2013F/Jo0012013.pdf> | 200 | application/pdf | 1742424 | 1742424 | identique |
| n° 102 de 2013 (LFC 2013) | <https://www.pist.tn/jort/2013/2013F/Jo1022013.pdf> | 200 | application/pdf | 589391 | 589391 | identique |
| n° 105 de 2013 (LF 2014) | <https://www.pist.tn/jort/2013/2013F/Jo1052013.pdf> | 200 | application/pdf | 2769318 | 2769318 | identique |
| n° 105 de 2014 (LF 2015) | <https://www.pist.tn/jort/2014/2014F/Jo1052014.pdf> | 200 | application/pdf | 2017161 | 2017161 | identique |
| n° 104 de 2015, édition arabe (LF 2016) | <https://www.pist.tn/jort/2015/2015A/Ja1042015.pdf> | 200 | application/pdf | 5273982 | 5273982 | identique |
| n° 105 de 2016 (LF 2017) | <https://www.pist.tn/jort/2016/2016F/Jo1052016.pdf> | 200 | application/pdf | 4155758 | 4155758 | identique |

### 10.5 Ce qui reste

1. **FOPRODI, lois de finances pour 1996, 1997 et 1998** : non établi. Les chapitres de
   l'industrie n'ont pas été lus en entier à l'image (1998 : bas de la p. 2475 ; 1996 et 1997 :
   page non localisée, l'OCR étant muet).
2. **FOPRODI, loi de finances pour 1999** : la ligne existe (p. 2544), le montant est illisible
   sur le scan français ; à lire dans l'édition arabe du JORT n° 104 de 1998 ou sur un autre
   exemplaire.
3. **Prise en charge patronale, loi de finances pour 1998** : 3 500 000 probable, chiffre des
   centaines de mille non assuré ; même remède.
4. **Loi de finances pour 1995** (emplacement de la dotation du fonds, tableaux « I » et
   « I bis ») et **loi de finances pour 1994** (JORT n° 100 de 1993, fascicule sans couche
   texte) : non ouverts à ce passage.
5. Pied de page du JORT n° 105 de 1996 (p. 2618, 2624) et pages 2475, 2503, 2544 et 2579 : lus
   par OCR, non relus à l'image. Intitulé du groupe « B » de 1996 et de 1997 : non relu.
6. Loi de finances pour 2016 : la suite du groupe de la caisse, p. 3689 de l'édition arabe, n'a
   pas été lue (les trois lignes de la p. 3688 font déjà le total du groupe).
7. Inchangé : lois de finances complémentaires, lois de règlement, années antérieures à 1994.

### 10.6 Outillage

Scripts dans le même répertoire `scratchpad/lf/` : `p1.py` (bande par coordonnées de la couche
texte), `p5.py` (bande par ligne de l'OCR de repérage), `maj3.py` (mise à jour de cette note) ;
images lues dans `p3/` ; relevé des adresses dans `pist.tsv`. OCR lancés au premier plan, sous
`timeout`, tous achevés ; aucun processus en fin de passage.

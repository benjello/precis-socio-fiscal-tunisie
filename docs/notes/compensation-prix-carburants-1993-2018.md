# Note documentaire n° 2 — prix à la pompe 1993-2018, deuxième passe

Passe du 6 octobre 2026. Complète `note-prix-carburants.md` (première passe), sans la remplacer. Aucun fichier du précis, du corpus JORT ni d'un dépôt versionné n'a été modifié. Pièces de travail : `scratchpad/prix2/`.

## Réponse courte

**Oui, on trouve — le trou est en grande partie fermé, par trois sources officielles tunisiennes que la première passe n'avait pas ouvertes.**

1. **Le ministère chargé de l'énergie a publié la série annuelle 1990-2016** sur son portail de données ouvertes (jeu « TN-Prix de vente des produits pétroliers », direction générale de l'énergie) : essence sans plomb, essence super, **gasoil ordinaire**, gasoil 50, pétrole lampant, GPL. Le portail ne répond plus ; les fichiers sont aux archives du web. Ce sont des moyennes annuelles pondérées par les jours.
2. **L'INS publie le prix mensuel du gasoil** — dans le *Bulletin mensuel de la statistique* (tableau 9.1, « Prix moyen de détail à Tunis »), pas dans l'*Annuaire* : 225 mois, de novembre 2007 à juillet 2026, déjà dans l'entrepôt (`ins-bms/`, 213 numéros).
3. **Une frise de 29 ajustements datés, 1997-2018**, pour l'essence et le gasoil : 9 dates de 2002-2006 d'un tableau attribué à l'ANME et repris par la presse, les dates de 2006-2013 du rapport de 2014 (déjà connues, maintenant chiffrées), les communiqués de 2010 à 2018 repris par la presse. De 2002 à 2016, cette frise redonne au centième de millime la moyenne annuelle officielle de chaque année — vérification indépendante pour les lignes lues ailleurs, mais quatre éléments ont été calés sur ces moyennes (voir le décompte du tableau 3).

Reste ouvert : les dates et niveaux exacts de 1997 à 2001 (quatre ajustements, connus seulement par le calcul ; l'année du dernier, 2000 ou 2001, n'est pas établie), et tout prix **mensuel** antérieur à novembre 2007.

---

## (i) Prix nouveaux, 1993-2018

### Tableau 1 — Moyennes annuelles officielles, 1990-2016 (ministère, données ouvertes)

Source : ministère de l'Industrie, de l'Énergie et des Mines, portail `catalog.industrie.gov.tn`, jeu **« TN-Prix de vente des produits péroliers »** (sic), organisation « Direction Générale de l'Energie », thème énergie, licence Open Tunisian License ; créé le 4 novembre 2014, modifié le 15 février 2018. Description : « Il s'agit des prix moyens pondérés annuels de vente des produit pétroliers suivants : Essence sans plomb, Essence Super, Gasoil ordinaire, Gasoil 50, Pétrole lampant domestique, GPL domestique. les prix sont exprimés en millimes par litre pour les 5 premiers produits et en Dinars par bouteille pour le GPL domestique. »

- CSV (capture du 29 octobre 2019) : `http://web.archive.org/web/20191029192123/http://catalog.industrie.gov.tn:80/dataset/63fe3962-976a-4309-ab1b-f3424ad63402/resource/2d6eab8e-f705-49b7-a05f-e49566c18e4f/download/prixdeventedesproduitspetroliers.csv` — SHA-256 `bc2757ec0a7658ec66336da2558c075d2479771dce1d487e8374746e4c692533`
- XLS (capture du 22 décembre 2018, valeurs non arrondies) : `http://web.archive.org/web/20181222185953/http://catalog.industrie.gov.tn:80/dataset/63fe3962-976a-4309-ab1b-f3424ad63402/resource/39102fa8-fccb-4b98-92e8-429c9ede6906/download/prixdeventedesproduitspetroliers.xls` — SHA-256 `9815df4917a6097d645d26fee00a64b7fdeffaece135711a9a02e705afe458e9`
- Métadonnées : `http://web.archive.org/web/20220819201204/http://catalog.industrie.gov.tn/api/2/rest/package/tn-prix-de-vente-des-produits-peroliers` ; page du jeu : capture `20161004143041`.
- Copies locales : `scratchpad/prix2/one_prix.csv`, `one_prix.xls`, `ckan_prix.json` (collecte du 6 octobre 2026 ; **non versés dans l'entrepôt**, la consigne n'y autorisant que des PDF — à verser par qui tient `tunisia-data`).
- Famille : **officielle tunisienne**. Preuve : fichier de données né numérique, lu intégralement ; contenu identique entre CSV et XLS.

Millimes par litre ; GPL en dinars la bouteille de 13 kg. Arrondi au centième (le XLS porte toutes les décimales).

| Année | Essence sans plomb | Essence super | Gasoil ordinaire | Gasoil 50 | Pétrole lampant | GPL 13 kg |
|---|---:|---:|---:|---:|---:|---:|
| 1990 | — | 480,05 | 283,50 | — | 155,03 | 3,20 |
| 1991 | — | 526,16 | 308,08 | — | 178,08 | 3,47 |
| 1992 | — | 530,00 | 310,00 | — | 180,00 | 3,62 |
| 1993 | 620,00 | 539,21 | 310,00 | — | 180,00 | 3,80 |
| 1994 | 620,00 | 570,00 | 310,00 | — | 180,00 | 3,80 |
| 1995 | 620,00 | 570,00 | 310,00 | — | 180,00 | 3,80 |
| 1996 | 620,00 | 570,00 | 310,00 | — | 180,00 | 3,97 |
| 1997 | 620,00 | 583,89 | 319,26 | — | 191,58 | 4,17 |
| 1998 | 643,01 | 636,16 | 347,75 | — | 214,86 | 4,32 |
| 1999 | 665,44 | 665,44 | 369,53 | — | 233,92 | 4,46 |
| 2000 | 693,33 | 693,33 | 398,33 | — | 240,00 | 4,62 |
| 2001 | 693,33 (identique à 2000) | 693,33 (identique à 2000) | 398,33 (identique à 2000) | — | 240,00 | 4,80 |
| 2002 | 716,58 | 716,58 | 415,00 | — | 240,00 | 4,80 |
| 2003 | 762,36 | 762,36 | 429,90 | — | 254,90 | 4,95 |
| 2004 | 802,05 | 802,05 | 456,37 | — | 274,86 | 5,26 |
| 2005 | 895,78 | 895,78 | 536,37 | — | 338,14 | 5,74 |
| 2006 | 1 057,40 | 1 057,40 | 697,40 | — | 497,40 | 6,43 |
| 2007 | 1 141,78 | 1 141,78 | 781,78 | 922,57 | 581,78 | 6,77 |
| 2008 | 1 279,40 | 1 279,40 | 918,41 | 1 085,21 | 717,86 | 7,33 |
| 2009 | 1 272,05 | 1 272,05 | 912,05 | 1 102,05 | 712,05 | 7,31 |
| 2010 | 1 315,75 | — | 955,75 | 1 145,75 | 755,75 | 7,48 |
| 2011 | 1 370,00 | — | 1 010,00 | 1 200,00 | 810,00 | 7,41 |
| 2012 | 1 406,90 | — | 1 039,29 | 1 236,44 | 812,22 | 7,42 |
| 2013 | 1 552,74 | — | 1 156,19 | 1 382,74 | 810,00 | 7,40 |
| 2014 | 1 620,41 | — | 1 210,33 | 1 450,41 | 810,00 | 7,40 |
| 2015 | 1 670,00 | — | 1 250,00 | 1 500,00 | 810,00 | 7,40 |
| 2016 | 1 650,27 | — | 1 172,98 | 1 436,83 | 810,00 | 7,40 |

Dans la fenêtre 1994-2016 : **118 moyennes annuelles**, dont **23 pour le gasoil ordinaire**, qui n'en avait aucune.

Contrôles faits sur ce fichier :
- **Il recoupe le Journal officiel.** 1991 : 490 + 40 × 330/365 = 526,16 (arrêté du 5 février 1991). 1993 : 530 + 40 × 84/365 = 539,21 — soit exactement la date d'effet du 9 octobre 1993 de l'arrêté du 26 octobre 1993 (tableau A de la première note). 1994-1996 : prix de l'arrêté de 1993, inchangés.
- **Il recoupe l'INS** pour l'essence après 2006 : 1 316, 1 403, 1 553, 1 620, 1 670, 1 650 (INS 2010, 2012-2016) contre 1 315,75, 1 406,90, 1 552,74, 1 620,41, 1 670,00, 1 650,27.
- **Une discordance avec l'INS, en 2011** : ministère 1 370 (essence) et 1 010 (gasoil) ; INS 1 320 et 960 (*Annuaire* et BMS). Le ministère a raison : le communiqué du 11 décembre 2010 porte l'essence à 1,370 D et le gasoil à 1,010 D à compter du 12 décembre 2010 (voir la frise). Le relevé de l'INS est resté figé toute l'année 2011 ; les numéros de 2012 du BMS corrigent ensuite rétroactivement janvier-mars 2012. **La moyenne INS de 2011 pour l'essence (1 320), reprise au tableau B de la première note, est donc fausse de 50 millimes** ; celle de 2012 (1 403) l'est de 4.
- **Les lignes 2000 et 2001 sont identiques au centième** (693,33 ; 398,33), alors que 2002 commence à 710 et 415 : l'une des deux est une recopie. Laquelle ? Un contrôle indépendant désigne 2001 comme la ligne fautive, sans le prouver : l'écart entre le prix public du gasoil et son « prix moyen à la production » (INS, tableau 4) vaut 54,7 millimes en 1999 et 48,9 en 2002 ; si la hausse de 40 millimes a lieu au milieu de 2000, il vaut 49,1 en 2000 et 48,9 en 2001 (série lisse) ; si elle avait lieu au milieu de 2001, il tomberait à 25,7 en 2000 et 32,2 en 2001. Le prix à la production monte d'ailleurs de 34,4 en 2000 puis de 16,9 en 2001 et plus du tout en 2002 — le profil d'une hausse de milieu d'année 2000 ; la moyenne INS de l'essence normale fait de même (+28 en 2000, +17 en 2001, +6 en 2002). **Conclusion tirée de ce seul recoupement** : la ligne 2000 est juste, la ligne 2001 devrait valoir 710 et 415. À publier avec cette réserve, et à faire confirmer.
- **Aucune version plus récente du jeu** : le portail du ministère redirige (301) vers le portail national, `https://catalog.data.gov.tn/fr/dataset/tn-prix-de-vente-des-produits-peroliers` (jeu `41b16b73-0fa4-413d-9afc-09eeac9ab1f4`), dont le certificat TLS ne se vérifie pas depuis ce poste (chaîne incomplète ; refusé aussi par l'outil de lecture) — non téléchargé. Sa page archivée (`http://web.archive.org/web/20240423235952/https://catalog.data.gov.tn/fr/dataset/tn-prix-de-vente-des-produits-peroliers`) montre les deux mêmes ressources, moissonnées depuis l'ancien portail (l'adresse de téléchargement encode l'ancienne) ; contact affiché : `opendata@tunisia.gov.tn`. Rien n'indique une mise à jour après 2016.
- Pondération : par les jours (somme des jours × prix, divisée par 365, années bissextiles 2008 et 2012 comprises ; par 366 en 2004 et 2016) ; par les mois, semble-t-il, en 2000 (23,33 = 40 × 7/12).
- Le pétrole lampant et la bouteille de gaz de l'INS (première note, tableau B) sont plus chers que ceux du ministère avant 2006 (pétrole 1998 : 243 contre 214,86) : ce ne sont pas les mêmes relevés ; ne pas les fondre en une série.

### Tableau 2 — Prix mensuels INS, novembre 2007 - juillet 2026

Pages du tableau dans les numéros cités (page du PDF) : novembre 2008, p. 25 sur 49 ; décembre 2010, p. 25 sur 49 ; juillet 2014, p. 29 sur 54 ; juin 2018, p. 29 sur 55 ; juillet 2026, p. 27 sur 54 (les autres numéros : même rubrique, page à relever au versement ; pagination imprimée non relevée).

Source : INS, *Bulletin mensuel de la statistique*, tableau **9.1 « Prix moyen de détail à Tunis »** (suite), rubriques « Transport » (lignes « Gazoil » puis « Gasoil », « Essence ») et « Chauffage, éclairage et eau » (« Pétrole bleu », « Bouteille à gaz »), unité : le millime. Chaque numéro donne treize mois et la moyenne de l'année précédente. Fichiers : `~/projets/tunisia-data/data/raw/ins-bms/bms-AAAA-MM.pdf`, 213 numéros (novembre 2008 - juillet 2026) ; liste des numéros : `https://www.ins.tn/publication`. Famille : **officielle tunisienne**. Preuve : couche texte, chaque mois recoupé sur jusqu'à treize numéros (`prix2/bms3.py`, `bms_series.json`) ; **non relu à l'image**.

Valeur du mois, par paliers (mois où la valeur change) :

- **Gasoil** : 2007-11 : 840 ; 2008-03 : 890 ; 2008-07 : 960 ; 2009-01 : 910 ; 2010-02 : 960 ; [2011 : 960, figé à tort] ; 2012-01 : 1 010 ; 2012-09 : 1 090 ; 2013-03 : 1 170 ; 2014-07 : 1 250 ; 2016-01 : 1 200 ; 2016-07 : 1 140 ; 2017-07 : 1 230 ; 2018-01 : 1 280 ; 2018-05 : 1 330 ; 2018-06 : 1 405 ; 2018-09 : 1 480 ; 2019-04 : 1 570 ; puis les paliers de 2020-2022 du tableau C de la première note, et 1 985 de décembre 2022 à juillet 2026.
- **Essence** : 2007-11 : 1 200 ; 2008-03 : 1 250 ; 2008-07 : 1 320 ; 2009-01 : 1 270 ; 2010-02 : 1 320 ; [2011 : 1 320, figé à tort] ; 2012-01 : 1 370 ; 2012-09 : 1 470 ; 2013-03 : 1 570 ; 2014-07 : 1 670 ; 2016-01 : 1 650 ; 2017-07 : 1 750 ; 2018-01 : 1 800 ; 2018-05 : 1 850 ; 2018-06 : 1 925 ; 2018-09 : 1 985 ; 2019-04 : 2 065 ; ensuite comme le tableau C.
- **Pétrole bleu** : 2007-11 : 640 ; 2008-03 : 690 ; 2008-07 : 760 ; 2009-01 : 710 ; 2010-02 : 760 ; 2010-12 : 810 ; 2022-09 : 950.
- **Bouteille à gaz** (ligne présente jusqu'au numéro d'octobre 2010 seulement) : 2007-11 : 7 000 ; 2008-03 : 7 200 ; 2008-07 : 7 500 ; 2009-01 : 7 300 ; 2010-02 : 7 500.
- **Moyennes annuelles INS du gasoil**, imprimées dans le BMS (absentes de l'*Annuaire*) : 2008 : 917 ; 2009 : 910 ; 2010 : 956 ; 2011 : 960 (fausse, voir plus haut) ; 2012 : 1 037 ; 2013 : 1 157 ; 2014 : 1 210 ; 2015 : 1 250 ; 2016 : 1 170 ; 2017 : 1 185 ; 2018 : 1 382 ; 2019 : 1 548 ; 2020 : 1 512 ; 2021 : 1 579 ; 2022 : 1 793 ; 2023, 2024, 2025 : 1 985.

Dans la fenêtre novembre 2007 - décembre 2018 : 134 mois × 3 produits, plus 36 mois de bouteille de gaz, soit **438 valeurs mensuelles** ; et **11 moyennes annuelles du gasoil** (2008-2018).

Réserves à porter :
- c'est un **relevé**, pas un tarif : le mois d'un ajustement porte tantôt le nouveau prix (février 2010 : 960, pour un ajustement du 21), tantôt une moyenne (novembre 2022 : 2 431 pour l'essence), tantôt l'ancien (avril 2018 : 1 800, alors que le prix est à 1 850 depuis le 1er avril) ;
- **2011 est faux** (figé à 1 320 et 960) ;
- valeurs isolées divergentes dans un seul numéro : février 2009 dans le numéro de février 2009 (960 au lieu de 910) ; numéro de décembre 2010 décalé d'une colonne ; gasoil d'octobre-novembre 2020 à 1 740 dans deux numéros (1 470 ailleurs).

### Tableau 3 — Frise des ajustements datés, 1997-2018 (essence sans plomb et gasoil ordinaire)

Millimes par litre. « Calcul » = la colonne dit si la ligne redonne la moyenne annuelle du tableau 1 (voir `prix2/check.py`).

| Date d'effet | Essence sans plomb | Gasoil ordinaire | Autres prix donnés | Source exacte | Famille | Niveau de preuve |
|---|---:|---:|---|---|---|---|
| 1997-07-16 | 620 (inchangée) | 330 | super 600 ; pétrole 205 | **calcul seul** sur le tableau 1 (+30, +20, +25 sur 169 jours). Date corroborée : décret n° 97-1339 du 14 juillet 1997, JORT n° 57 du 18 juillet 1997, p. 1274 — TVA à 10 % sur l'essence, le gasoil, le fuel domestique et le GPL « à compter du 16 juillet 1997 » (couche texte, `https://www.pist.tn/jort/1997/1997F/Jo05797.pdf`, adresse dérivée non rouverte) | officielle (moyennes, décret) | **inféré** ; date appuyée par un texte, niveaux non lus |
| 1998-05-06 | 655 | 357 | super 655 ; pétrole 220 | calcul seul (+35, +27, +55, +15 sur 240 jours) ; un texte fiscal sur les produits pétroliers figure au JORT n° 35 de 1998, non dépouillé | officielle (moyennes) | **inféré** |
| 1999-04-22 | 670 | 375 | pétrole 240 | calcul seul (+15, +18, +20 sur 254 jours) ; l'autre solution (27 août) est écartée par le pétrole lampant, à 240 en 2000. Date voisine d'un texte : décret n° 99-894 du 19 avril 1999 « fixant le tarif du droit de consommation applicable aux produits pétroliers », JORT n° 33 de 1999, p. 624 (sommaire, couche texte décodée ; décret non lu) | officielle (moyennes) | **inféré** ; date appuyée par un texte à trois jours près |
| 2000 **ou** 2001, milieu d'année | 710 | 415 | — | calcul seul : +40 sur 7/12 d'année ; l'année 2000 est la plus probable (recoupement avec le prix à la production, voir tableau 1), 2001 n'est pas exclue. Aucun texte fiscal de milieu d'année au JORT de 2000 ni de 2001 (208 fascicules, plein texte) | officielle (moyennes) | **inféré ; ni l'année ni le jour ne sont établis** |
| 2002-10-13 | 740 | 415 (inchangé) | super 740 ; normale 700 | WMC, « Pétrole en Tunisie : hausse des prix et baisse de la consommation », 7 septembre 2006, tableau « Évolution des prix de vente des carburants au public 2002-2006 », à la suite d'un tableau « Source : ANME » — `https://www.webmanagercenter.com/2006/09/07/19345/petrole-en-tunisie-hausse-des-prix-et-baisse-de-la-consommation/` | presse (d'après l'ANME) | page lue ; calcul : oui |
| 2003-04-04 | 770 | 435 | super 770 ; normale 740 | idem | presse | page lue ; calcul : oui |
| 2004-05-05 **ou** 05-08 | 800 | 455 | super 800 ; normale 770 | idem (« 05/05/2004 ») ; la moyenne officielle de 2004 n'est redonnée qu'avec le **8 mai** | presse | page lue ; **date discordante de trois jours** |
| 2004-08-01 | 830 | 475 | super 830 ; normale 800 | idem | presse | page lue ; calcul : oui |
| 2005-02-13 | 860 | 500 | super 860 ; normale 830 | idem | presse | page lue ; calcul : oui |
| 2005-06-05 | 900 | 540 | super 900 ; normale 870 | idem | presse | page lue ; calcul : oui |
| 2005-09-04 | 950 | 590 | super 950 ; normale 920 | idem | presse | page lue ; calcul : oui |
| 2006-01-15 | 1 000 | 640 | super 1 000 ; normale 970 | idem | presse | page lue ; calcul : oui |
| 2006-04-26 | 1 050 | 690 | super 1 050 ; normale 1 020 | idem | presse | page lue ; calcul : oui |
| 2006-07-02 | 1 100 | 740 | — | date : rapport du 21 juillet 2014 sur la compensation des carburants, pp. 158-159 (axe des graphiques, image) ; niveaux : **calcul** (seule valeur qui redonne 1 057,40 et 697,40) ; courbe « Prix limite à la pompe » du rapport compatible (≈ 740) | officielle (rapport, moyennes) | date lue ; niveaux inférés, exacts au calcul |
| 2007-01-01 | 1 100 | 740 | — | date de structure de prix du rapport de 2014 ; **pas de changement du prix public** (calcul) | officielle | date lue |
| 2007-05-06 | 1 150 | 790 | — | date : rapport de 2014 ; niveaux : calcul (redonne 1 141,78 et 781,78) | officielle | date lue ; niveaux inférés, exacts au calcul |
| 2007-10-28 | 1 200 | 840 | — | date : rapport de 2014 ; niveaux : INS, BMS, novembre 2007 (1 200 et 840) | officielle | date et niveaux lus |
| 2008-03-02 | 1 250 | 890 | pétrole 690 ; GPL 7,2 (INS) | date : rapport de 2014 ; niveaux : INS, BMS, mars 2008 | officielle | lus ; calcul : oui |
| 2008-07-06 | 1 320 | 960 | pétrole 760 ; GPL 7,5 (INS) | date : rapport de 2014 ; niveaux : BMS, juillet 2008 | officielle | lus ; calcul : oui |
| 2009-01-16 | 1 270 | 910 | pétrole 710 ; GPL 7,3 (INS) | date : BCT, *Rapport annuel 2009*, pp. 191-192 (« activé le 16 janvier 2009 », baisse de l'ordre de 5 %) et rapport de 2014 ; niveaux : BMS, janvier 2009 ; Directinfo, 5 mars 2013 (« de 1,320 à 1,270 ») — `https://directinfo.webmanagercenter.com/2013/03/05/tunisie-evolution-des-prix-des-lessence-et-du-gasoil-2009-2013/` | officielle + presse | lus ; calcul : oui |
| 2010-02-21 | 1 320 | 960 | pétrole 760 ; GPL 7,5 (INS) | date : Kapitalis, 12 décembre 2010 (« La dernière hausse remonte au 21 février 2010 ») et rapport de 2014 ; niveaux : BMS, février 2010 | officielle + presse | lus ; calcul : oui |
| 2010-12-12 | 1 370 | 1 010 | gasoil 50 ppm 1 200 ; pétrole 810 ; GPL 13 kg 7,700 D | Kapitalis, « Tunisie. Nouvelle hausse des prix des carburants », 12 décembre 2010, d'après le communiqué du ministère de l'Industrie et de la Technologie — `https://www.kapitalis.com/archive/191-conso/1980-tunisie-nouvelle-hausse-des-prix-des-carburants.html` | presse (communiqué) | page lue ; calcul : oui ; **contredit l'INS**, qui reste à 1 320 et 960 en 2011 |
| 2011 (14 janv., 1er avril, 23 nov.) | 1 370 | 1 010 | GPL 13 kg : 7,7 → 7,4 D, vers le 14 janvier 2011 (inféré : 7,4 + 0,3 × 13/365 = 7,41) | dates de structure du rapport de 2014 ; moyennes de 2011 du tableau 1 : aucun changement de l'essence ni du gasoil | officielle | dates lues ; GPL inféré |
| 2012-09-02 | 1 470 | 1 090 | — | date : rapport de 2014 ; niveaux : BMS, septembre 2012 ; Directinfo, 5 mars 2013 (+100 et +80) | officielle + presse | lus ; calcul : oui |
| 2013-03-05 | 1 570 | 1 170 | — | Directinfo, 5 mars 2013 ; rapport de 2014 ; BMS, mars 2013 ; FMI, rapport n° 13/161, appendice (« increase in fuel prices and electricity tariffs by around 7 percent in March 2013 ») | officielle + presse + FMI | lus ; calcul : oui |
| 2013-05-18 | 1 570 | 1 170 | — | date de structure du rapport de 2014, sans changement du prix public | officielle | date lue |
| 2014-07-01 | 1 670 | 1 250 | gasoil 50 : 1 500 | Tekiano, 3 juillet 2014, d'après le communiqué du ministère de l'Industrie, de l'Énergie et des Mines — `https://www.tekiano.com/2014/07/03/tunisie-liste-des-nouveaux-prix-des-hydrocarbures-a-partir-du-1er-juillet-2014/` ; FMI, rapport n° 14/50 (« increased by around 6 percent on July 1, 2014 ») ; BMS, juillet 2014 | presse (communiqué) + FMI + officielle | lus ; calcul : oui |
| 2016-01-06 | 1 650 | 1 200 | gasoil 50 : −50 | Tekiano, 5 janvier 2016, d'après le communiqué du ministère (essence −20, gasoil 50 −50, gasoil −50, « à partir du mercredi 6 janvier ») — `https://www.tekiano.com/2016/01/05/tunisie-les-nouveaux-prix-de-lessence-et-gasoil-a-partir-du-06-janvier-2016/` ; BMS, janvier 2016 ; FMI, rapport n° 16/138 (« five percent decline in retail fuel prices last January ») | presse (communiqué) + officielle | lus ; calcul : oui |
| 2016, mi-juillet (14, 15 ou 16) | 1 650 (inchangée) | 1 140 | gasoil 50 : 1 420 (−30) | Webdo, 14 juillet 2016 : le ministre de l'Énergie annonce « ce jeudi 14 juillet 2016 » le gasoil à 1,140 D (−60), le gasoil 50 à 1,420 D, l'essence inchangée à 1,650 D, prix qui « entreront en vigueur, jeudi 14 juillet à minuit » — `http://web.archive.org/web/2016/https://www.webdo.tn/2016/07/14/tunisie-baisse-prix-gasoil-gasoil-50-lessence-inchange/` (capture lue) ; BMS, juillet 2016 (1 140) ; la moyenne officielle de 2016 n'est redonnée qu'avec le **16 juillet** | presse (annonce du ministre) + officielle | page lue ; **jour d'effet à deux jours près** |
| 2017-07-02 | 1 750 | 1 230 | — | première note (ONE, *Conjoncture*, sept. 2017) ; BMS, juillet 2017 | officielle | déjà établi |
| 2018-01-01 | 1 800 | 1 280 | gasoil sans soufre 1 560 ; GPL 13 kg +300 millimes | Kapitalis, 30 décembre 2017 (« augmentera de 50 millimes à partir du 1er janvier 2018 ») — `http://kapitalis.com/tunisie/2017/12/30/a-partir-1er-janvier-2018-augmentation-prix-carburant/` ; L'Économiste maghrébin, 23 juin 2018 ; BMS, janvier 2018 ; niveaux : ONE, *Conjoncture* de décembre 2017 | presse + officielle | lus — **lève la réserve de la première note** : l'état « au 31/12/2017 » est le prix entré en vigueur le 1er janvier 2018 à zéro heure |
| 2018-04-01 | 1 850 | 1 330 | gasoil sans soufre 1 610 | Tekiano, 2 avril 2018, d'après le communiqué (« à partir de dimanche 1er avril 2018, à zéro heure ») — `https://www.tekiano.com/2018/04/02/tunisie-les-nouveaux-prix-de-lessence-et-gasoil-a-partir-du-1er-avril-2018/` | presse (communiqué) | page lue ; l'INS ne l'enregistre qu'en mai |
| 2018-06-23 | 1 925 | 1 405 | gasoil sans soufre 1 685 | L'Économiste maghrébin, 23 juin 2018, d'après le communiqué (+75 millimes) — `https://www.leconomistemaghrebin.com/2018/06/23/augmentation-prix-hydrocarbures/` ; BMS, juin 2018 | presse (communiqué) + officielle | page lue |
| 2018-09-02 | 1 985 | 1 480 | gasoil sans soufre 1 745 | déjà établi (ONE, *Chiffres clés 2018*) ; confirmé : Tekiano, 3 septembre 2018 ; WMC, 2 septembre 2018 (+60, +60, +75) | officielle + presse | déjà établi |
| 2019-03-31 | 2 065 | 1 570 | gasoil sans soufre 1 825 | déjà établi ; confirmé : Ilboursa (communiqué du 30 mars au soir, +80, +80, +90) | officielle + presse | déjà établi |

**Décompte, par niveau de preuve.** 29 ajustements nouveaux du prix public entre 1997 et 2018 (hors 2 juillet 2017 et 2 septembre 2018, déjà acquis), soit 58 prix datés pour l'essence et le gasoil :
- **16 ajustements, 32 prix, lus dans une source officielle** (date du rapport de 2014, de la BCT ou d'un communiqué repris ; niveau du BMS ou du communiqué) : 28 oct. 2007, 2 mars et 6 juil. 2008, 16 janv. 2009, 21 févr. et 12 déc. 2010, 2 sept. 2012, 5 mars 2013, 1er juil. 2014, 6 janv. et mi-juil. 2016, 1er janv., 1er avril et 23 juin 2018 — plus les deux dates de 2006-2007 ci-dessous, dont seule la date est lue ;
- **9 ajustements, 18 prix, lus dans la presse** d'après un tableau attribué à l'ANME (13 oct. 2002 - 26 avril 2006) ;
- **2 ajustements dont la date est lue et les niveaux calculés** (2 juil. 2006 : 1 100 et 740 ; 6 mai 2007 : 1 150 et 790), soit 4 prix ;
- **4 ajustements entièrement inférés** (1997, 1998, 1999, 2000 ou 2001), soit 8 prix — hors publication.

S'y ajoutent une trentaine de prix datés d'autres produits (super, normale, gasoil 50, pétrole, GPL). **2018 est entièrement daté** : 1er janvier, 1er avril, 23 juin, 2 septembre.

**Portée du recoupement avec les moyennes annuelles.** Il n'est une vérification indépendante que pour les lignes lues ailleurs : toutes celles de 2002-2003, 2004 (niveaux), 2005, janvier et avril 2006, octobre 2007, 2008 à 2015 et janvier 2016. Quatre éléments ont au contraire été **ajustés sur** les moyennes et ne les confirment donc pas : le jour de mai 2004 (le 8), le jour de juillet 2016 (le 16), les niveaux du 2 juillet 2006 et ceux du 6 mai 2007.

### Tableau 4 — Repères annexes (à ne pas verser dans la série)

| Objet | Valeurs | Source | Statut |
|---|---|---|---|
| Prix à la pompe en dollars, relevé de novembre (GIZ) | gazole : 1995 : 0,44 ; 1998 : 0,33 ; 2000 : 0,29 ; 2002 : 0,19 ; 2004 : 0,39 ; 2006 : 0,57 ; 2008 : 0,84 ; 2010 : 0,82 ; 2012 : 0,69 ; 2014 : 0,68 ; 2016 : 0,62. Essence : 0,64 ; 0,60 ; 0,49 ; 0,29 ; 0,68 ; 0,83 ; 0,96 ; 0,94 ; 0,93 ; 0,91 ; 0,73 | Banque mondiale, indicateurs archivés `EP.PMP.DESL.CD` et `EP.PMP.SGAS.CD` : `https://api.worldbank.org/v2/sources/57/country/TUN/series/EP.PMP.DESL.CD/version/201904/time/all?format=json` (et source 11, Africa Development Indicators) | institution internationale ; en dollars, biennal ; la conversion en millimes serait dérivée. Les points de 2002 (0,19 et 0,29) sont incompatibles avec 415 et 740 millimes ; celui de 1995 (0,44, soit ≈ 420 millimes) contredit les 310 du ministère : **série peu fiable pour la Tunisie** |
| INS, « prix moyens à la production », gasoil, millimes par m³ | 1995, 1996 : 274 718 ; 1997 : 282 718 ; 1998 : 306 980 ; 1999 : 314 834 ; 2000 : 349 255 ; 2001, 2002 : 366 139 ; 2003 : 380 402 ; 2004 : 404 740 ; 2005 : 479 948 ; 2006 : 677 138 (éd. 2002-2006) — puis série refondue (éd. 2003-2007 et suivantes), jusqu'à 2012 | INS, *Annuaire statistique*, tableau 13.1 « Évolution des prix moyens à la production », rubrique « Produits pétroliers » (éd. 1995-2001, p. imprimée 189 ; éd. 1998-2002 à 2008-2012) | officielle ; **ce n'est pas le prix à la pompe** (30 à 50 millimes en dessous) ; la série change de base deux fois. Confirme les années de hausse : 1997, 1998, 1999, 2000, 2001 |

---

## (ii) Frise — lecture d'ensemble

- **9 octobre 1993 - 15 juillet 1997 : gel de près de quatre ans** (essence sans plomb 620, super 570, gasoil 310, pétrole 180).
- **1997-2000 : un ajustement par an**, au printemps ou en été ; le gasoil passe de 310 à 415 (+34 %), l'essence sans plomb de 620 à 710 (+15 %).
- **mi-2000 (ou mi-2001) - octobre 2002 : gel** ; le gasoil reste à 415 jusqu'au 4 avril 2003.
- **2003 - 2008 : treize hausses en cinq ans et demi**, dont trois en 2005 et trois en 2006 ; le gasoil passe de 415 à 960 (×2,3), l'essence de 740 à 1 320 (+78 %).
- **16 janvier 2009 : seule baisse avant 2016** (−50 millimes), première application du mécanisme de 2009.
- **2010 : deux hausses de 50 millimes** (21 février, 12 décembre) ; **gel de vingt mois** après le 14 janvier 2011 (seule la bouteille de gaz baisse, de 7,7 à 7,4 D).
- **2012-2014 : trois hausses** de 100 millimes sur l'essence et 80 sur le gasoil (2 septembre 2012, 5 mars 2013, 1er juillet 2014).
- **2016 : deux baisses** (6 janvier ; mi-juillet pour le seul gasoil).
- **2017-2018 : cinq hausses en quatorze mois** (2 juillet 2017, 1er janvier, 1er avril, 23 juin et 2 septembre 2018) : essence +335, gasoil +340.
- L'écart essence − gasoil est de **360 millimes exactement de 2005 à 2012**, puis 380, 400, 420, 450 et 510 en 2016.

---

## (iii) Couverture finale, 1993-2018

| Produit | Moyenne annuelle | Prix mensuel | Dates d'ajustement |
|---|---|---|---|
| **Gasoil ordinaire** | **1990-2016** ministère (2000 ou 2001 fautive) ; 2008-2025 INS (2011 faux) ; 2017-2018 : INS seul | nov. 2007 - juil. 2026 (INS) | 2002-2018 complet (deux jours à 2-3 jours près, deux niveaux calculés en 2006-2007) ; 1997-2001 inféré |
| **Essence sans plomb** | 1993-2016 ministère ; 1995-2023 INS (étiquettes « normale » puis « super ») | nov. 2007 - juil. 2026 (INS) | idem |
| Essence super | 1990-2009 ministère | — | 2002-2006 (presse-ANME) |
| Essence normale | 1995-2005 INS | — | 2002-2006 (presse-ANME) |
| Gasoil 50 / sans soufre | 2007-2016 ministère | — | 12 déc. 2010, 1er juil. 2014, puis 2018 |
| Pétrole lampant | 1990-2016 ministère ; 1995-2023 INS | nov. 2007 - juil. 2026 (INS) | 2008-2010 par les mois INS ; avant : non |
| GPL 13 kg | 1990-2016 ministère ; 1995-2023 INS | nov. 2007 - oct. 2010 (INS) | 12 déc. 2010 (7,7 D), janv. 2011 (7,4 D, inféré), 1er janv. 2018 (+0,3 D) |

**Ce qui reste vide :**
1. les **dates et niveaux exacts de 1997, 1998, 1999 et 2000-2001** (inférés par le calcul ; aucun communiqué ni tableau lu) ; **laquelle des lignes 2000 et 2001 du fichier est fautive** (2001 selon un recoupement, non prouvé) ;
2. tout **prix mensuel avant novembre 2007** (les BMS antérieurs ne sont pas en ligne) ;
3. les ajustements du pétrole lampant et de la bouteille de gaz avant 2008 (moyennes annuelles seulement) ;
4. les deux ou trois jours d'incertitude de mai 2004 et de juillet 2016 ;
5. la moyenne annuelle **officielle du ministère** pour 2017 et 2018 (le fichier s'arrête à 2016 ; l'INS donne 1 185 et 1 382 pour le gasoil, 1 700 et 1 897 pour l'essence) ;
6. toujours : l'arrêté du 31 décembre 1980, et les « arrêtés internes ».

---

## (iv) Piste par piste

| n° | Piste | Adresse ou fichier | Résultat |
|---|---|---|---|
| 1 | ONE, ministère, archives du web | index CDX `https://web.archive.org/cdx/search/cdx?url=<domaine>&matchType=domain&collapse=urlkey&filter=original:.*(onjonct\|hiffres\|prix\|bilan\|structure\|carbur\|petrol\|tarif\|dataset).*` sur energiemines.gov.tn (260 adresses), industrie.gov.tn et catalog.industrie.gov.tn (5 000, plafond atteint), data.industrie.gov.tn (312), tunisieindustrie.gov.tn (9), etap.com.tn (39), sndp.com.tn et agil.com.tn (37), stir.com.tn (2), anme.nat.tn (9), anme.tn (29) ; mit.gov.tn, onem.tn, dge.gov.tn : 0 | **Trouvé : le jeu de données ouvertes 1990-2016** (tableau 1). *Conjoncture énergétique* : les archives ne remontent pas avant 2020, sauf décembre 2017 (`/fileadmin/user_upload/publications/conjoncture_energetique_decembre_2017.pdf`, déjà lu) — aucun numéro de 2016 ni de 2018. *Chiffres clés* 2015-2017 : aucune capture. Le portail du ministère redirige (301) vers `catalog.data.gov.tn`, dont le certificat ne se vérifie pas d'ici (API `package_search` non interrogeable) ; sa page archivée de 2024 porte le même jeu, sans mise à jour (voir tableau 1) |
| 1 bis | ANER, *Étude d'impact des prix de l'énergie sur la demande*, octobre 2000 (Ideaconsult), 92 p. | `http://web.archive.org/web/20111027072730/http://www.anme.nat.tn:80/sys_files/medias/documents/etudes/etude_impact_prix/rapport_final.pdf` | téléchargé et versé à l'entrepôt ; couche texte parcourue par mots (« prix de vente », « millimes », « essence », « gasoil ») et aux trois endroits tabulaires : ce sont des graphiques de taux de distorsion et de recettes fiscales 1990-1999, et des élasticités — **pas de tableau de prix à la pompe** ; non lu page à page, graphiques non relus à l'image |
| 2 | INS | *Annuaire* : 22 éditions, recherche de « gasoil / gas-oil / gazoil » ; BMS : 213 numéros ; *Tunisie en chiffres* : 16 éditions ; premier portail de l'INS (CDX sur ins.nat.tn, 1 256 adresses) | **Trouvé : BMS, tableau 9.1** (tableau 2). L'*Annuaire* ne donne le gasoil qu'au tableau des prix à la production (tableau 4). *Tunisie en chiffres* : essence normale seulement, 2004-2011. Premier portail : aucun indicateur de prix de détail ; aucun BMS antérieur à novembre 2008 en ligne ni archivé |
| 3 | FMI | imf.org : 403 sur les fiches et sur `/external/pubs/ft/scr/…pdf` ; archives du web : rapports n° 12/255, 13/161, 14/50, 15/285, 16/138 (n° 18/120 : 404) ; locaux : n° 96/27, 97/57, 10/282, 21/44 (n° 00/37 et 01/37 : pas de couche texte) | **aucun tableau de prix intérieurs**. Trois corroborations de dates : ≈ 7 % en mars 2013 (n° 13/161), ≈ 6 % au 1er juillet 2014 et formule de janvier 2014 (n° 14/50), −5 % en janvier 2016 (n° 16/138). Trois rapports versés à l'entrepôt (voir en bas) |
| 4 | Banque mondiale | API : `source=57` seul échoue ; la bonne forme est `/v2/sources/57/country/TUN/series/<code>/version/201904/time/all` ; aussi `/v2/sources/11/…` | **obtenu** (tableau 4), en dollars, biennal, peu fiable. Les notes de 2013 et de 2015 (locales) avaient été lues à la première passe : pas d'historique de prix au-delà du point de 2014, que le BMS redate (1 670 et 1 250 valent à partir du 1er juillet 2014, non de mai) |
| 5 | GIZ, *International Fuel Prices* | non ouvert en PDF | ses relevés sont ceux de l'indicateur de la Banque mondiale ; pas de recherche des éditions une à une |
| 6 | Rapport du 21 juillet 2014 | p. 158 rendue à 220 ppp et relue à l'image | la courbe « Prix limite à la pompe de la structure des prix » est **compatible point par point** avec la frise (740, 740, 790, 840, 890, 960, 960, 910, 910, 960, 1 010 ×4, 1 090, 1 170, 1 170) ; les valeurs ne s'y lisent pas au millime. Pas de nouvelle recherche des tableaux de structure dans les 192 pages (annexes n° 68-69 absentes du PDF, déjà constaté) |
| 7 | Presse | pages ouvertes par `curl` (les refus de la première passe venaient de l'outil de lecture) : WMC 7 sept. 2006 et 25 juin 2018, Directinfo 5 mars 2013, Kapitalis 12 déc. 2010 et 30 déc. 2017, Tekiano 3 juil. 2014, 5 janv. 2016, 2 avril et 3 sept. 2018, WMC 2 sept. 2018, L'Économiste maghrébin 23 juin 2018, Ilboursa (mars 2019), Nawaat 17 juil. 2017, Webdo 14 juil. 2016 (par les archives du web) | **frise 2002-2018** (tableau 3). Les tableaux de Directinfo (2009-2013) et de WMC (2010-2018) sont des images, non lues. Non ouvertes : Business News 6 janv. 2016 (404), Tunisie numérique. Aucune dépêche retrouvée pour 1997-2001 ni pour mai 2007 |
| 8 | STIR, SNDP, ETAP, Cour des comptes, budgets citoyens, réponses à l'Assemblée | CDX : aucun rapport annuel archivé sous stir.com.tn, sndp.com.tn, agil.com.tn ; etap.com.tn : cartes et code des hydrocarbures. Page « Questions des députés » du ministère (`https://www.energiemines.gov.tn/fr/open-gov/acces-a-linformation/questions-des-deputes/`) ouverte : quatre PDF, aucun intitulé sur les prix. Cour des comptes : une requête de moteur, aucun rapport sur la compensation des hydrocarbures remonté | **rien trouvé, et peu cherché** : les quatre PDF des députés ne sont pas lus, le site de la Cour des comptes et les budgets citoyens ne sont pas ouverts |
| 9 | JORT après 1993, seconde voie | plein texte (`pdftotext`, édition française) de **280 fascicules** : 1997 n° 55-66 et 1998 n° 34-45 (24, couche texte directe) ; 17 fascicules d'avril-mai 1999, **les 104 de 2000, les 104 de 2001**, 16 d'octobre-novembre 2002 et 15 de mars-mai 2003 (couche texte décalée de 29 points de code, décodée par `prix2/jgrep2.py`, tous lisibles après décodage). Motifs : « millimes le/par litre », « prix (limite) de vente au public / à la pompe », « prix des produits pétroliers / des carburants », « essence super », « gas-oil / gasoil », « produits pétroliers », « carburants ». Intitulés arabes de `jort_cache.db` : « سعار » croisé avec محروقات, بترول, نفط, بنزين, وقود | **aucun arrêté de prix** : la conclusion de la première passe tient. Ne sortent que des textes fiscaux — décret n° 97-1339 du 14 juillet 1997 (n° 57, p. 1274), tableau tarifaire au n° 35 de 1998, décret n° 99-894 du 19 avril 1999 (n° 33, p. 624), décret n° 2000-2908 du 18 décembre 2000 et décret n° 2001-339 du 30 janvier 2001 « portant suspension des droits de douane dus à l'importation des carburants » (n° 102 de 2000, p. 3148 ; n° 10 de 2001, p. 220) — et un arrêté sur la subvention du gasoil des bateaux de pêche (n° 60 de 2001). Intitulés arabes : un seul texte, l'arrêté du 15 juillet 2016 sur la commission (absent des intitulés français). **Limites** : 280 fascicules sur environ 1 700 pour 1994-2010 ; les fascicules de 1994-1996, de 2004-2010 et le reste de 1997-1999 et 2002-2003 ne sont pas balayés ; édition arabe non ouverte. Un premier balayage complet avait échoué (expression refusée par l'outil de recherche, puis couches décalées non décodées) : ses « zéro occurrence » ne valent rien et ne sont pas repris |

Mise à jour proposée de la fiche `r-serie-prix-pompe-1993-2017` (première note) : résultat **partiel → largement trouvé** ; ajouter aux sources le jeu de données ouvertes, le BMS et la presse ; pistes restantes : BMS sur papier avant novembre 2008 ; communiqués de 1997-2000 ; demande à l'Observatoire.

---

## (v) Contacts publiés

| Qui | Adresse | Lue où | Remarque |
|---|---|---|---|
| Ministère de l'Industrie, des Mines et de l'Énergie — contact général | `contact(at)energiemines.gov.tn` ; tél. (+216) 71 901 953 ; fax (+216) 71 909 149 ; Immeuble Panorama, 40 avenue du Japon, Montplaisir, 1002 Tunis | pied de page du site, lu le 6 octobre 2026 sur `https://www.energiemines.gov.tn/fr/open-gov/acces-a-linformation/` | la page `/fr/tc/contact/` répond 500 |
| Même ministère, annuaire du portail du gouvernement | `contact@energy-mines.gov.tn` | `http://fr.tunisie.gov.tn/annuaire/21/9-ministère-de-l-énergie-des-mines-et-de-la-transition-énergétique.htm` | autre domaine que celui du site : **l'une des deux adresses est périmée** ; préférer celle du site |
| Chargé d'accès à l'information du ministère (loi organique n° 2016-22) | Habib Chaibi (حبيب الشايبي), `habib.chaibi@energiemines.gov.tn`, tél. 71 902 623 | « جدول البيانات المتعلقة بالمكلف بالنفاذ للمعلومة ونائبه », PDF lié depuis la page « Accès à l'information » sous « Liste des responsables de l'accès à l'information (Ar) » ; fichier daté du 28 janvier 2021 | liste de **janvier 2021**, au nom du « ministère de l'énergie et des mines » : le titulaire a pu changer |
| Suppléant | Mohamed Sdiri (محمد السديري), `mohamed.sdiri@energiemines.gov.tn` | même document | idem |
| Formulaire de demande d'accès | PDF en arabe, même page (« Formulaire de demande d'accès à l'information (Ar) ») | `https://www.energiemines.gov.tn/fr/open-gov/acces-a-linformation/` | une page « Guide de l'accès à l'information (Ar) » y figure aussi |
| **Observatoire national de l'énergie et des mines** | **aucune adresse publiée trouvée** | *Chiffres clés* 2014, 2018-2025, *Conjoncture* (déc. 2017, déc. 2019, juil. 2026), *Bilans* : aucune adresse électronique ni téléphone ; page d'organigramme du site : aucune | un annuaire commercial nomme un responsable de l'Observatoire avec une adresse masquée : non officiel, **non repris** |

Voie praticable : écrire au contact général à l'attention de l'Observatoire, et, en parallèle ou à défaut de réponse, déposer une demande d'accès à l'information auprès du chargé d'accès, par le formulaire.

---

## (vi) Recommandation

**La série de l'essence et du gasoil 1993-2017 est publiable**, sous cette forme :

1. **Une figure en longue période, 1964-2026, pour les deux carburants**, en moyenne annuelle : arrêtés du JORT jusqu'en 1993 ; **ministère (données ouvertes) de 1990 à 2016**, qui raccorde exactement les arrêtés ; INS (BMS) pour 2017-2018 ; ONE ensuite. La ligne 2001 du ministère est à signaler ou à omettre. C'est le socle : source officielle, citée par son adresse archivée.
2. **Un tableau des ajustements 2002-2018** (tableau 3), en disant la source de chaque ligne ; les lignes lues dans la presse redonnent, sans avoir été ajustées, les moyennes officielles de 2002, 2003 et 2005 et, avec les dates du rapport de 2014, celles de 2008 à 2015 : c'est ce qui autorise à les publier. Les niveaux du 2 juillet 2006 et du 6 mai 2007 sont des calculs (à dire) ; les deux jours incertains (mai 2004, juillet 2016) se donnent avec leur fourchette.
3. **1997-2001 : ne publier que les moyennes annuelles**, avec la réserve sur 2000-2001. Les dates inférées de 1997 et de 1999 tombent sur deux décrets fiscaux, celle de 2000 ou 2001 sur aucun : ce sont des calculs, à garder en note de travail ou à dire comme tels (« ajustement à la mi-juillet 1997 »).
4. Corriger le tableau B de la première note : essence 2011 = 1 370 (et non 1 320) ; ne pas employer le relevé INS de 2011.

Pour le modèle : la série annuelle 1990-2016 et la frise datée 2002-2018 suffisent à dater un paramètre « prix de vente au public » de l'essence sans plomb et du gasoil ordinaire à partir du 13 octobre 2002 ; avant, seules les moyennes annuelles sont sourcées.

**Que demander à l'Observatoire (ou par accès à l'information)** — une demande courte, qui cite ce que l'on a déjà :
1. la **mise à jour du jeu « Prix de vente des produits pétroliers »** (1990-2016) jusqu'à 2025, et sa remise en ligne — le portail `catalog.industrie.gov.tn` ne répond plus ;
2. le **tableau des dates d'effet et des prix de vente au public** (essence sans plomb, super, gasoil ordinaire, gasoil 50 puis sans soufre, pétrole lampant, GPL 13 kg) **de 1993 à 2017** — les « structures de prix » successives —, en priorité 1997, 1998, 1999, 2000 et 2001 ;
3. laquelle des **lignes 2000 et 2001** du jeu est juste (elles sont identiques) ;
4. les **données du graphique « Prix annuel moyen de vente de l'essence et du gasoil » (depuis 1980)** des *Chiffres clés* ;
5. accessoirement : les numéros de la *Conjoncture énergétique* de 2016 à 2018 et les *Chiffres clés* 2015-2017, absents du site.

---

## Références candidates (compléments à la première note)

```json
[
  {"id": "minenergie-opendata-prix-vente-petroliers", "type": "dataset", "title": "Prix de vente des produits pétroliers [moyennes annuelles pondérées, 1990-2016]", "author": [{"literal": "Ministère de l'Industrie, de l'Énergie et des Mines, direction générale de l'énergie"}], "issued": {"date-parts": [[2018, 2, 15]]}, "URL": "http://web.archive.org/web/20191029192123/http://catalog.industrie.gov.tn:80/dataset/63fe3962-976a-4309-ab1b-f3424ad63402/resource/2d6eab8e-f705-49b7-a05f-e49566c18e4f/download/prixdeventedesproduitspetroliers.csv", "accessed": {"date-parts": [[2026, 10, 6]]}, "note": "citation-key: minenergie-opendata-prix-vente-petroliers\nPortail catalog.industrie.gov.tn, jeu « TN-Prix de vente des produits péroliers », créé le 4 novembre 2014, modifié le 15 février 2018 ; capture des archives du web du 29 octobre 2019 (XLS : capture du 22 décembre 2018). Le portail ne répond plus."},
  {"id": "ins-bms", "type": "report", "title": "Bulletin mensuel de la statistique", "author": [{"literal": "Institut national de la statistique"}], "issued": {"literal": "numéros de novembre 2008 à juillet 2026"}, "publisher": "INS", "publisher-place": "Tunis", "URL": "https://www.ins.tn/publication", "note": "citation-key: ins-bms\nTableau 9.1 « Prix moyen de détail à Tunis ». La clé ins-bms est déjà annoncée dans le catalogue de tunisia-data : vérifier qu'elle n'existe pas avant de la créer."},
  {"id": "decret97-1339", "type": "legislation", "title": "Décret n° 97-1339 du 14 juillet 1997 relatif à la fixation de la date de mise en application des dispositions de l'article 40 de la loi n° 95-109 du 25 décembre 1995 portant loi de finances pour la gestion 1996", "issued": {"date-parts": [[1997, 7, 14]]}, "container-title": "Journal officiel de la République tunisienne", "issue": "57", "page": "1274", "URL": "https://www.pist.tn/jort/1997/1997F/Jo05797.pdf", "note": "citation-key: decret97-1339\nJORT n° 57 du 18 juillet 1997. Art. 2 : TVA à 10 % sur l'essence super, l'essence normale, le gasoil, le fuel-oil domestique et le GPL à compter du 16 juillet 1997. Lu par la couche texte du corpus local ; adresse dérivée du modèle, à rouvrir avant usage ; page de début du décret à vérifier à l'image."}
]
```

Les articles de presse (WMC 2006, Kapitalis 2010 et 2017, Directinfo 2013, Tekiano 2014, 2016 et 2018, L'Économiste maghrébin 2018) sont donnés par leur adresse au tableau 3 ; une entrée par article cité est à créer au versement. Rapports du FMI n° 13/161, 14/50 et 16/138 : titres à relever sur la page de garde.

## Fichiers versés à l'entrepôt (ignorés par git, vérifié par `git check-ignore`)

Collecte du 6 octobre 2026, depuis `http://web.archive.org/web/<année>id_/https://www.imf.org/external/pubs/ft/scr/…`, dans `~/projets/tunisia-data/data/raw/banque-mondiale-rapports/` :

| Fichier | Origine | SHA-256 |
|---|---|---|
| `imf_2013_161_sba_request_tunisia.pdf` | `…/scr/2013/cr13161.pdf` | `331281f5925dcd6cac7382ee853260bc8297a56db7d86819ec2c9256f4989a23` |
| `imf_2014_050_sba_reviews_1_2_tunisia.pdf` | `…/scr/2014/cr1450.pdf` | `ef06ea7e8e58e8d92b144b59a476e8b830025dbb15f6bf71782d0bcbabf59c66` |
| `imf_2016_138_eff_request_tunisia.pdf` | `…/scr/2016/cr16138.pdf` | `274e4edd312a3c852064f553c4055cca092fcd9e100dfec287efdd80b5532ecc` |
| `imf_2012_255_art4_tunisia.pdf` | `…/scr/2012/cr12255.pdf` (capture `20130319130637`) | `23c11cd20930e0676102262fd10395f9af0ad17aaeb9cd8e7d74bebcfc7ca238` |
| `imf_2015_285_art4_sba_review_6_tunisia.pdf` | `…/scr/2015/cr15285.pdf` | `57effb129ed4badb67f2d15127d4b2c96e65930372906f917b1595356279908e` |
| `aner_2000_etude_impact_prix_energie_demande.pdf` | `http://web.archive.org/web/20111027072730id_/http://www.anme.nat.tn:80/sys_files/medias/documents/etudes/etude_impact_prix/rapport_final.pdf` | `27c2cb076ab2ea4509d35980cbe8524ce2e6abc6e521c1728f8fd3545ca5242b` |

`git -C ~/projets/tunisia-data status --short` : vide après ces copies.

Restés dans `scratchpad/prix2/` : `one_prix.csv`, `one_prix.xls`, `ckan_prix.json`, les pages de presse (`presse/`), les extractions du BMS (`bms/`, `bms_series.json`, `bms_moy.json`), les scripts (`bms3.py`, `infer2.py`, `check.py`, `jgrep.py`). Aucun processus laissé en cours.

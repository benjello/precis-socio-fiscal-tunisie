# Note documentaire : les dates, les textes lus et les séries du chapitre sur le patrimoine immobilier

Je n'ai modifié aucun fichier du dépôt. Les fichiers de travail sont dans `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/15adcd5f-c210-406f-907e-f6545e1e97a0/scratchpad/foncier-dates/` :
- `textes_lus.csv` : un texte par ligne, avec pages, date d'effet, mode d'établissement, rubrique et degré de lecture ;
- `series_tableau_A.csv` : les prévisions du tableau A, ligne par ligne (année, valeur, unité, source, page, remarque) ;
- `j2006_088.txt` (loi n° 2006-69), `j1998_064.txt` (loi n° 98-73), `ocr/` (océrisations des lois de finances de 1968 à 1992), `img/`, `a74/` (édition arabe de 1974).

Aucun processus n'est resté actif. Un premier lot d'OCR lancé en arrière-plan était trop lent : je l'ai arrêté par ses PID (les miens seulement, sans `pkill`), puis relancé au premier plan avec `OMP_THREAD_LIMIT=1`. Aucune étude nouvelle n'est citée : rien n'est à verser dans `tunisia-data`.

**Convention de date.**
- **Avant juillet 1993** (règle du « jour franc » de AGENTS.md) : un texte publié le jour J est exécutoire à J+2.
- **Depuis la loi n° 93-64** (JORT n° 50 du 6 juillet 1993, p. 931, art. 2, lu par OCR) : « exécutoires cinq jours après le dépôt du journal officiel… au siège du gouvernorat de Tunis. Le jour du dépôt n'est pas pris en considération ». Aucune date de dépôt n'a été lue dans cette passe.

---

## 1. Les textes lus

| Texte | Art. | Page (éd. fr.) | Date d'effet, et comment | Ce que le texte cherche (rubrique) |
|---|---|---|---|---|
| **Loi n° 2006-69 du 28 oct. 2006** (JORT n° 88 du 3 nov. 2006) | 1-5 | 3869 ; éd. ar. 4549 | **10 nov. 2006**, date donnée par la DGI (NC 23/2007, § 2). La DGI applique la loi n° 93-64 ; le dépôt n'est pas lu. La loi n'a pas de clause d'effet. | Intitulé : « relative à l'exonération des donations entre ascendants et descendants et entre époux du droit d'enregistrement proportionnel ». La loi est autonome et n'a pas de rubrique. Voir ci-dessous. |
| LF 1969, loi n° 68-41 (n° 55 du 31 déc. 1968) | 14 | 1371-1372 | 2 janv. 1969, jour franc. Pas de clause dans l'article ni à la fin de la loi (p. 1376). Par contraste, l'art. 7 date lui-même sa mesure (« à compter du 1er janvier 1969 »). | Aucune rubrique propre |
| LF 1970, loi n° 69-64 (n° 57 des 30-31 déc. 1969 ; signée le 31) | 7, 9, 10 | 1500-1501 | 2 janv. 1970, jour franc, la publication étant fixée au jour de la signature | « Chapitre II. Dispositions relatives aux recettes. Droits d'enregistrement » |
| LF 1973, loi n° 72-87 du 27 déc. 1972 (n° 52 des 26-29 déc. 1972) | 7 | 1853 | Non établie : la publication tombe entre le 27 et le 29 déc. L'article ne fait que reporter des dates. | « Droits d'enregistrement » |
| LF 1975, loi n° 74-101 du 25 déc. 1974 (n° 80 du 31 déc. 1974) | 29-30 | 2916 ; éd. ar. 3221 | 2 janv. 1975 par le jour franc, **sous réserve d'une clause générale non lue** : la fin de la loi n'a pas été lue | « Droits sur les mutations », « Tarif des droits de mutation par décès », « Majoration des abattements » |
| LF 1977, loi n° 76-115 | 42, **43** | 3167-3168 | 2 janv. 1977 par le jour franc ; l'art. 43 vise les actes enregistrés avant le 1er janv. 1982 | Art. 43 : « Terrains à bâtir. Limitation de l'exonération à l'acquéreur constructeur » |
| LF 1981, loi n° 80-88 (n° 78 des 30-31 déc. 1980) | 9, 26 | 3275 ; 3278-3279 | 2 janv. 1981, jour franc. Pas de clause dans les articles 9 et 26. | Art. 9 : « Impôt sur les plus-values immobilières » |
| LF 1982, loi n° 81-100 (n° 84 des 29-31 déc. 1981) | 20, 21, 25, 82 | 3035-3036 ; 3043 | 2 janv. 1982, jour franc | Art. 25 : « Droit de la Conservation de la propriété foncière » |
| LF 1983, loi n° 82-91 (n° 84 du 31 déc. 1982) | 44-46 | 2886-2887 | 2 janv. 1983, jour franc | « Droits de la Conservation… » ; art. 46 : « Droit pour défaut de la mention de l'origine » |
| LF 1984, loi n° 83-113 (n° 86 du 30 déc. 1983) | 12-15 | 3372-3373 | **1er janv. 1984** (publication le 30 déc., jour franc le 31) | Art. 12 : « Droits sur les mutations » ; art. 13 : « Terrains à bâtir » (aucun objectif énoncé) ; art. 15 : « Droit supplémentaire » |
| LF 1985, loi n° 84-84 (n° 79 des 28-31 déc. 1984) | 36-40 | 2955-2956 | 2 janv. 1985 | Marchés, greffe, prêts sur gages, timbre. **Rien sur les successions ni les immeubles.** |
| LF 1986, loi n° 85-109 (n° 91 du 31 déc. 1985) | 23-28 ; **45** | 1733 ; 1737 | 2 janv. 1986 | Art. 26-28 : exonérations ; art. 45 : « Imposition des lots domaniaux ayant perdu leur vocation agricole ». **Rien sur le barème successoral.** |
| LF 1987, loi n° 86-106 (n° 78 du 31 déc. 1986) | 22-24 | 1612 | 2 janv. 1987 | Art. 22 : « prorogation des délais relatifs à l'exonération de la première mutation » |
| **Loi n° 87-71 du 26 nov. 1987** (amnistie fiscale) | 13 | 1464 | 29 nov. 1987, jour franc. La publication est déduite au 27 nov. (voir la loi suivante). | Suspension du droit pour défaut d'origine jusqu'au 31 déc. 1988 |
| **Loi n° 87-73 du 26 nov. 1987** | 1-2 | 1465 | **29 nov. 1987**, jour franc. Le fascicule est daté « 24-27 nov. » et contient un décret du 27 nov. : la publication est donc déduite au 27. L'art. 1 borne seulement la fin (« actes présentés… avant le 31 décembre 1988 ») ; l'art. 2 rend le texte rétroactif pour les droits consignés ou constatés avant la publication. | Intitulé seul : « relative au tarif des droits d'enregistrement » |
| LF 1988, loi n° 87-83 (n° 91 des 29-31 déc. 1987) | 32-34 | 1630 (page à vérifier à l'image) | 2 janv. 1988 | Art. 32 : « Exonération des mutations des propriétés immobilières agricoles » ; art. 33 : « Contribution immobilière des lots domaniaux… » |
| LF 1989, loi n° 88-145 du 31 déc. 1988 (n° 87 des 30-31 déc. 1988) | **53**, 54, 55, 69 | 1798 (lue à l'image) ; 1800 | 2 janv. 1989 (publication le 31 déc. 1988 ; lectures du 18 octobre 2026, § 1.3) | Art. 53 : « Prorogation de la réduction du droit d'enregistrement » ; art. 54 : « Suspension du droit d'origine » ; art. 55 : « Simplification des procédures d'enregistrement » |
| LF 1990, loi n° 89-115 (n° 88 du 31 déc. 1989) | 37, 38, 40 | 2150 | 2 janv. 1990 ; l'art. 38 a sa propre clause (actes à compter du 1er janv. 1990) | « Droit d'origine de propriété » ; art. 40 : prorogation de l'exonération de la première mutation |
| LF 1991, loi n° 90-111 (n° 86 du 31 déc. 1990) | **42** | 2053 | 2 janv. 1991 | « Prorogation de la réduction du droit d'enregistrement » : le 5 % jusqu'au 31 déc. 1991 |
| LF 1992, loi n° 91-98 (n° 90 du 31 déc. 1991) | 56-58, 60 | 2088 | 2 janv. 1992 | « De la promotion immobilière » ; « Prorogation de la réduction… » |
| LF 1993, loi n° 92-122 du 29 déc. 1992 (n° 88 du 31 déc. 1992) | 106-108 | 1677 | 2 janv. 1993, jour franc : la loi est antérieure à la loi n° 93-64 | « Détermination de l'assiette et des modalités de paiement de l'impôt sur le revenu dû au titre de la plus-value immobilière » |
| LF 1995, loi n° 94-127 (n° 103 des 30-31 déc. 1994) | 55, 100 | **2047** ; 2051 | **1er janv. 1995** (art. 100) | Art. 55 : « L'impôt sur le revenu au titre de la plus-value immobilière » |
| **Loi n° 98-73 du 4 août 1998** (n° 64 du 11 août 1998) | 1-12 | 1736-1737 | **Non établie** : date de dépôt inconnue. L'art. 12 porte la rubrique « III. Date d'entrée en vigueur de la loi », mais ne fixe qu'une rétroactivité conditionnelle (cessions antérieures, si l'impôt est payé dans l'année). | Intitulé exact : « portant simplification des procédures fiscales et réduction des taux **de l'impôt** ». Rubriques : « Réduction du taux de l'impôt », « Suppression de l'impôt minimum… », « Détermination du champ d'application… », « Amélioration des modalités de recouvrement… », « Suppression du droit de préemption », « Réduction du tarif d'enregistrement des donations et des successions… », « Relèvement du montant des abattements… », « Exonération de la renonciation à l'héritage… » |
| LF 2003, loi n° 2002-101 du 17 déc. 2002 (n° 102 du 17 déc. 2002) | 61-62 ; 87 | 2883 ; 2888 | **1er janv. 2003** (art. 87) | « Institution d'un droit de mutation et de partage sur les immeubles non immatriculés » |
| LF 2005, loi n° 2004-90 (n° 105 du 31 déc. 2004) | 57, **60**, 89 | **3441** (confirmée à l'image) ; 3445 | **1er janv. 2005** (art. 89 ; la rubrique imprimée porte par erreur « pour l'année 2004 ») | Art. 60 : « Rationalisation des avantages fiscaux au titre de la plus-value immobilière » ; art. 57 : « Actualisation du tarif du droit fixe d'enregistrement… » (passage à 15 D) |
| LFC 2012, loi n° 2012-1 (n° 39 du 18 mai 2012) | 43-46 | 929 | **25 mai 2012**, date donnée par la DGI (NC 14/2012, § III, qui applique la loi n° 93-64 à l'art. 46). Même règle et même date pour l'art. 43. La loi n'a pas de clause générale. | Art. 43 : « Mise à jour du tarif du droit fixe d'enregistrement… » ; art. 46 : « Institution d'un droit en contrepartie de la prestation de service de la formalité de l'enregistrement » |
| LFC 2015, loi n° 2015-30 (n° 67 du 21 août 2015) | 26-2 | 1893 | **Non établie** : la phrase « 1er janvier 2016 » appartient au § 1 (déduction des intérêts) ; la NC 18/2015 ne commente que ce § 1 | « Assouplissement de l'acquisition des locaux à usage d'habitation » |
| LF 2016, loi n° 2015-53 (n° 104 du 29 déc. 2015) | 35 ; 58 ; 80 ; 82 ; 92 | 3148 ; 3156 ; 3162 ; 3163 ; 3165 | **1er janv. 2016** (art. 92) | Voir § 3.3 |
| LF 2017, loi n° 2016-78 (n° 105 du 27 déc. 2016) | 29 ; 69 ; 79 | 3836 ; 3849 ; 3851 | **1er janv. 2017** (art. 79) ; l'art. 29 § 3 excepte les promesses ayant date certaine avant le 1er nov. 2016 | Art. 29 : « Instauration d'un droit d'enregistrement complémentaire sur les ventes et les donations d'immeubles dont la valeur égale ou supérieure à cinq cent mille dinars » ; art. 69 : « Simplification des procédures d'enregistrement des jugements et arrêts » (§ 3 : minimum de perception de 40 D) |
| LF 2018, loi n° 2017-66 (n° 101 du 19 déc. 2017) | 34 ; 50 ; 67 | 4278 ; 4286 ; 4292 | **1er janv. 2018** (art. 67-1) | Art. 34 : « Rationalisation des avantages fiscaux au titre des donations d'immeubles et de fonds de commerce entre ascendants et descendants et entre époux » ; art. 50 : « Révision du tarif des droits fixes… » (20 → 25 D) |
| LF 2019, loi n° 2018-56 (n° 104 du 28 déc. 2018) | 56 ; 90 | 4546 ; 4555 | **1er janv. 2019** (art. 90) | « Relèvement du montant de la déduction de la valeur des logements construits par les promoteurs immobiliers exonéré du droit d'enregistrement proportionnel » |
| LF 2020, loi n° 2019-78 (n° 104 du 27 déc. 2019) | 45 ; 58 | 4436 ; 4439 | **1er janv. 2020** (art. 58) | « Allègement de la charge fiscale en matière de droits d'enregistrement et droits similaires exigibles sur les acquisitions des logements et des terrains par les bénéficiaires des prestations des offices des logements des agents publics » |
| LF 2022, DL 2021-21 (n° 119 du 28 déc. 2021) | 27 ; 28 ; 40 ; 53 ; 73 | 3087 ; 3087 ; 3091 ; 3097 ; 3107 | **1er janv. 2022** (art. 73-1) ; l'art. 40 § 2 vise les contrats présentés à partir du 1er janv. 2022, quelle que soit leur date | Art. 27 : « Allègement de la charge fiscale sur les ventes des logements bâtis par les promoteurs immobiliers » ; art. 28 : « Octroi aux personnes non résidentes de l'avantage de l'enregistrement au droit fixe de leurs acquisitions en devises des immeubles bâtis destinés à l'exercice d'une activité économique » ; art. 40 : « Exonération des acquisitions de l'État… » ; art. 53 : « Actualisation du tarif du droit fixe… » |

### 1.1 Loi n° 2006-69 : ce qui est désormais établi (texte et image)

- **Art. 1.** Ajoute au tarif des droits fixes de l'art. 23 du code le **n° 18 ter** : « Les donations de biens entre ascendants et descendants et entre époux y compris les donations de nue propriété ou d'usufruit de biens immeubles », **15 D par acte**.
- **Art. 2.** Ajoute un alinéa à l'art. 26 de la loi n° 80-88 : ces donations d'immeubles sont inscrites au registre foncier moyennant un **droit fixe de 100 D**.
- **Art. 3.** Même règle pour le droit de mutation et de partage des immeubles non immatriculés (art. 61 de la loi n° 2002-101) : **100 D**.
- **Art. 4 (absent de la note existante).** Ajoute un alinéa à l'**art. 28 du code de l'IRPP** : pour la cession de biens reçus par donation familiale, le prix de revient est la valeur à la date de possession par le **donateur**, et la durée de détention court depuis cette date. Cette règle doit figurer au registre de la plus-value.
- **Art. 5.** Récrit le n° 10 de l'art. 20 du code : le droit de 3 % pour défaut d'origine ne vise plus que les **mutations à titre onéreux**, ce qui exclut toute donation.
- **Navette parlementaire.** Députés les 18 juillet et 26 octobre 2006, conseillers le 27 juillet 2006 (notes de travaux préparatoires, p. 3869). L'avis du Conseil constitutionnel n° 53-2006 (éd. fr. p. 3877 ; éd. ar. p. 4559-4562) atteste que la Chambre des conseillers a amendé les articles 1 à 3 pour y inclure la nue-propriété et l'usufruit, et qu'un texte unifié est passé en commission mixte.
- **Ce que la loi cherche.** La loi n'énonce aucun motif. Les deux sources disponibles sont des tiers, à citer comme tels :
  - le **Conseil constitutionnel**, avis n° 31-2006 (21 juin 2006), éd. fr. **p. 3875** (image, OCR) et éd. ar. p. 4557 : « le fait d'accorder des facilités fiscales concernant la mutation de la propriété par la voie de la donation entre ascendants et descendants et entre époux s'insère dans le cadre de la protection de la famille qui fait partie des objectifs consacrés par le préambule de la Constitution ». L'avis n° 53-2006 y renvoie (éd. ar. p. 4562) ;
  - la **DGI**, NC 23/2007 : « Dans le but de faciliter les mutations de biens entre ascendants et descendants et entre époux ».
- **Régime antérieur** (NC 23/2007, état au 9 nov. 2006) : 2,5 % (n° 16 de l'art. 20), 1 % de droit foncier, 1 % sur les immeubles non immatriculés, 3 % pour défaut d'origine.
- **URL vérifiée (HTTP 200)** : `https://www.pist.tn/jort/2006/2006F/Jo0882006.pdf`. **Depuis 2000, le nom de fichier porte l'année sur quatre chiffres** (`JoNNNAAAA`) ; avant, deux chiffres (`JoNNNAA`). C'est pourquoi `Jo08806.pdf` répondait 404.

---

## 2. Corrections aux notes existantes

Elles portent sur `docs/notes/fiscalite-patrimoine-immobilier-mutations-plus-values.md` et sur la fiche de plan.

1. **LF 1970, art. 9 : rien n'y naît.**
   - Il récrit l'art. 52 du décret du 27 juin 1954, qui exonérait déjà les terrains.
   - Il ajoute une borne : actes enregistrés **avant le 1er janvier 1973** (§ I-1°).
   - Le droit supplémentaire de 3 % par année (§ III) figure déjà dans le texte de 1970.
   - Dans la même loi, l'art. 7 reporte au 1er janv. et au 1er mars 1973 les dates de la **loi n° 65-16 du 28 juin 1965** (« dégrèvements fiscaux en faveur de la construction d'immeubles d'habitation »).
2. **La « loi n° 72-87 » est la LF 1973.**
   - Son art. 7 (p. 1853) n'institue pas l'exonération de la première mutation. Il reporte au 1er janv. et au 1er mars 1977 les dates des art. 7 **et 9** de la LF 1970 : la première mutation **et** les terrains.
   - La LF 1977, art. 42, reporte ces dates à 1982.
   - **La LF 1977, art. 43 (p. 3168), absente de la note**, récrit l'art. 52 : actes enregistrés avant le 1er janv. 1982 ; construction **par l'acquéreur** dans les quatre ans ; 3 % par année en cas de défaut ou de cession avant construction.
3. **Exonération de la première mutation : la chaîne complète.**
   - Antécédents : décret du 28 oct. 1948, art. 75 ; décret du 29 sept. 1952, art. 27-29 ; loi n° 61-18, art. 3 (abrogés par la LF 1982, art. 20) ; loi n° 65-16.
   - LF 1982, art. 20 : régime refondu (promoteurs agréés, logements achevés avant 1986).
   - Prorogations : LF 1986, art. 27 (1987) ; LF 1987, art. 22 (1989) ; LF 1989, art. 69 (1990) ; LF 1990, art. 40 (1991).
   - Puis le droit fixe de la LF 1992, art. 58.
4. **Défaut d'origine : suspendu de fin 1987 à fin 1989.**
   - Loi n° 87-71, art. 13 (p. 1464) : exigibilité suspendue jusqu'au 31 déc. 1988 ;
   - LF 1989, art. 54 (p. 1798) : prorogation au 30 déc. 1989 ;
   - LF 1990, art. 38 : 3 % pour les actes présentés à compter du 1er janv. 1990.
   - La LF 1983, art. 46, montre aussi que l'art. 10 du décret de 1934 avait été modifié « notamment par la loi n° 68-41 » (LF 1969). Le taux de 1969 reste à lire dans le tableau de son art. 14.
5. **Lots domaniaux : un dispositif à placer au registre de la plus-value, pas dans le TODO de l'impôt sur la fortune.**
   - LF 1986, art. 45 (p. 1737) : « contribution immobilière exceptionnelle » de **50 %**, réduite à **25 %** pour les cessions aux agences foncières et à la SNIT, sur les profits de cession de lots domaniaux ayant perdu leur vocation agricole (loi n° 70-25).
   - LF 1988, art. 33 (p. 1630) : durées d'exigibilité de 25, 30 et 40 ans.
   - C'est l'ancêtre de l'art. 27 § 3 et des taux de 25 % et 50 % du code de l'IRPP.
6. **Barème successoral de 1984.**
   - Aucune modification dans les LF 1985, 1986, 1987, 1990 et 1991, ni dans la loi n° 88-63 (marchés seulement, p. 856).
   - La LF 1988, art. 32 (p. 1630) y déroge expressément (« Par dérogation aux dispositions de l'article 12 de la loi n° 83-113 ») : elle exonère la propriété agricole transmise en ligne directe, entre époux ou entre frères et sœurs, sous engagement d'indivision et d'exploitation collective de 15 ans. Cela établit que le barème de 1984 était en vigueur fin 1987.
   - **Non relus** : LFC 1988 (loi n° 88-60), LF 1992, LF 1993, autres lois de 1988 à 1993.
   - Il faut donc écrire : « aucune modification trouvée dans les lois de finances 1985-1991 relues », et non « tient jusqu'en 1993 ».
7. **LF 1975, ligne directe : 6 %.** Le chiffre est net dans l'édition arabe (p. 3221, « من الأسلاف إلى الأعقاب وبين الأزواج » : 6/8/9/12/15/18 %). L'image française (1 bit, 240 ppi) reste illisible même au pixel.
8. **Loi n° 98-73.**
   - L'intitulé exact se termine par « réduction des taux **de l'impôt** ».
   - L'**art. 11** (nouvel art. 38 bis du code : exonération de la renonciation à l'héritage des ascendants au profit des descendants) manque à la note.
   - La note est juste sur l'art. 12 : rétroactivité conditionnelle, sans point de départ.
9. **La mention « JORT déposé le 4 nov. » (loi n° 2006-69) n'a aucune source.** La NC 23/2007 ne donne que le 10 novembre. À retirer ou à remplacer par « date donnée par la DGI ».
10. **Pages.**
    - LF 1995, art. 55 : **p. 2047**, et non 2046. Sur le fascicule de 1994, le numéro de page est en tête de page : la règle « le pied de page suit le texte » ne s'y applique pas. Revérifier feuille par feuille (`pagede.py`) toute page obtenue par cette règle avant 2000.
    - Loi n° 2006-69 : p. 3869 en édition française (et non « 3869-3870, pagination de l'index, peut-être arabe »).
    - LF 2003, art. 61-62 : p. 2883.
11. **Série 2020 : il manque une ligne.** Le tableau A de la LF 2020 contient aussi la ligne **13-03 « Parts d'immatriculations foncières », 36 MD**.
12. **Droit fixe : point de départ.** La LF 2005, art. 57 (p. 3441), porte les droits fixes à 15 D. Suivent 20 D (LFC 2012, art. 43), 25 D (LF 2018, art. 50) et 30 D (LF 2022, art. 53).
13. **Minimum de perception.** Il passe à 20 D par la LFC 2012, art. 44, puis à 40 D par la LF 2017, art. 69 § 3 (lu ; la note indique [DGI]).
14. **LF 2016, art. 82.** La rubrique dit « tunisiens non résidents », le texte « personnes non résidentes au sens de la législation relative au change ». L'article abroge aussi l'art. 59 du code d'incitation aux investissements.
15. **LF 2020, art. 45 :**
    - n° 12 octies à 25 D par page ;
    - exonération du droit foncier ;
    - nouvel art. 20 ter (location-vente des offices) ;
    - maintien des avantages des promoteurs (art. 28 de la LF 2012).

---

## 3. Le classement rupture, étape, ajustement

Arguments pour le propriétaire ; je ne tranche pas.

### 3.1 Épine

- **1987.** La loi n° 87-71 (amnistie, et suspension du défaut d'origine) et la loi n° 87-73 (14,60 % → 5 %) sont signées le même jour et publiées dans le même fascicule (n° 83, p. 1463-1465). Les droits sur les mutations et l'origine de propriété changent donc ensemble.
  - Pour une réforme propre (lecture Q1 a) : la suspension du défaut d'origine est prorogée jusqu'au 30 déc. 1989, puis le droit est fixé à 3 % en 1990.
  - Contre : les deux mesures sont temporaires, et le lien textuel avec 1993 vient de la LF 1992, art. 60.
- **1993 (code).** Rupture inchangée.
- **LF 1993, art. 106.** La rubrique (« Détermination de l'assiette et des modalités de paiement… ») plaide pour une **étape** de 1990 plutôt qu'une rupture.
- **Loi n° 98-73.** Ses rubriques sont toutes de moyens (« Réduction du taux », « Suppression de l'impôt minimum », « Détermination du champ »). Son intitulé (« simplification… réduction des taux ») est celui d'une loi de réforme et pas seulement d'ajustement. Elle reste candidate pour la lecture Q1 c.

### 3.2 Sections secondaires

- **Terrains d'habitat individuel.** La naissance est antérieure à la période couverte (art. 52 du décret de 1954).
  - LF 1970, art. 9, et LF 1977, art. 43 (borne à 1982, construction par l'acquéreur) : **étapes**.
  - LF 1982, art. 21 (800 m²) : ajustement.
  - **LF 1984, art. 13 : la rupture tient.** L'exonération devient un barème, avec « Toutes dispositions contraires sont abrogées ». Son art. 15 abandonne le droit supplémentaire de 1970.
  - Question ouverte pour le rédacteur : la LF 1977, art. 43, réserve l'exonération aux actes enregistrés avant le 1er janv. 1982. Aucun report postérieur n'a été trouvé dans la LF 1982 (l'art. 21 ne touche que le § II). Statut des actes de 1982-1983 : non établi.
- **Logements neufs et promoteurs.** Naissance antérieure à 1966. LF 1982, art. 20 : **étape de refonte**. LF 1992, art. 58 : étape. LF 2014 : rupture.
- **Donations et successions.**
  - **Loi n° 2006-69, désormais lue : je la propose comme rupture de la section.** Le régime passe du proportionnel au fixe sur trois droits coordonnés (enregistrement, droit foncier, immeubles non immatriculés). La règle de plus-value change (art. 4), les donations sortent du défaut d'origine (art. 5), et le motif est attesté par le Conseil constitutionnel. Elle ne touche pas les successions.
  - LF 2018, art. 34 (« Rationalisation… », une fois tous les cinq ans, sur les trois droits) : étape.
  - LF 2016, art. 80 et LF 2026, art. 20 : ajustements.
  - **LF 1988, art. 32** (propriété agricole) : ajustement à ajouter au registre.
- **Plus-value (registre B).**
  - **LF 1986, art. 45** : naissance d'un dispositif (contribution sur les lots domaniaux) ; LF 1988, art. 33 : ajustement.
  - **Loi n° 2006-69, art. 4** : ajustement de l'assiette.
  - LF 1995, art. 55 : ajustement de recouvrement (retenue de 2,5 % et minimum de 2,5 %). Ce minimum est supprimé par la loi n° 98-73, art. 2.

### 3.3 Registre A : textes désormais lus au *Journal officiel*

Ils ne sont plus de degré [DGI] :
- LF 2003, art. 61-62 (1 %, dont 30 % au fonds de soutien de la délimitation du patrimoine foncier). Le droit n'est pas dû sur les opérations exonérées du droit d'immatriculation foncière, et l'immatriculation qui suit se fait sans droit proportionnel ;
- LFC 2012, art. 43-46 (art. 46 : 1 %, minimum 20 D, actes hors délai de l'art. 20 du code des droits et procédures fiscaux ; non dû pour les actes au droit fixe ou exonérés) ;
- LF 2016 :
  - art. 35 : sukuk, 20 D par acte et 100 D de droit foncier ;
  - art. 58 : 1 % → **3 %**, étendu aux déclarations de succession ;
  - art. 80 : n° 18 quater, 20 D par acte ;
  - art. 82 : n° 12 septies, 20 D par page ;
- LF 2018, art. 34 et 50 ;
- LF 2020, art. 45 ;
- LF 2022, art. 28 et 40.

---

## 4. Séries (tableau A : **prévisions**, en dinars courants)

Le détail ligne par ligne est dans `series_tableau_A.csv`.

**Avertissement :** toute valeur antérieure à 2020 est une **OCR non vérifiée**. Elle doit être lue à l'image avant toute figure.

**Segments de nomenclature, à ne pas raccorder en silence :**
- art. 28-30 « Droits sur les mutations » / « Autres droits d'enregistrement » (1970-1984) ;
- 23-02 / 23-03, et 11-12 ou 13-12 pour la plus-value (1985-1991 environ) ;
- 24-02 et 14-02 (1993-2019 ; la note donne aussi 11-06 et 13-05 de 2011 à 2019) ;
- 13-01, 13-02, **13-03** et 18-02 (2020-2022). La ligne propre à la plus-value n'apparaît pas dans les tableaux 2020-2022 relus. Je n'écris pas où elle est passée.

**Inventaire, avec page du *Journal officiel* :**

| Loi de finances | Page(s) | Ce qui a été relevé |
|---|---|---|
| LF 1970 | p. 1505 | 30 : 1,2 MD |
| LF 1973 | p. 1857 | valeurs illisibles |
| LF 1981 | p. 3287-3288 | |
| LF 1982 | p. 3049-3050 | mutations 10,1 MD ; autres 15,6 MD ; plus-value 0,1 MD |
| LF 1983 | p. 2905-2906 | |
| LF 1984 | p. 3387-3388 | mutations 15,0 MD |
| LF 1985 | p. 2965-2966 | 23-02 : 17,6 MD ; plus-value 0,8 MD |
| LF 1986 | p. 1742-1743 | 23-02 : 18,0 MD |
| LF 1987 | p. 1627-1628 | 23-02 : 20,3 MD |
| LF 1988 | p. 1638-1639 | valeurs non captées |
| LF 1989 | p. 1805-1806 | 23-02 : 19,0 MD |
| LF 1990 | p. 2156-2157 | 23-02 : 21,0 MD |
| LF 1991 | p. 2063 | |
| LF 1992 | p. 2094-2095 | |
| LF 1993 | p. 1680-1681 | 24-02 : 30,0 MD |

- **2000-2010.** Les PDF locaux `Lois_de_Finances/` n'ont **pas** les tableaux A. Les fascicules du *Journal officiel* les ont, **en image**. Sondage fait sur la LF 2003 : p. 2889-2892 (OCR possible, colonnes à lire à l'image). Les autres années ne sont pas sondées.
- **2011-2019** (page de la ligne « Droits sur les mutations », sur le tiré à part local qui reproduit la pagination du *Journal officiel*) :

| LF 2011 | LF 2012 | LFC 2012 | LF 2013 | LFC 2013 | LF 2014 | LFC 2014 | LF 2015 | LFC 2015 | LF 2016 | LFC 2016 | LF 2017 | LF 2018 | LF 2019 | LF 2020 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3479 | 13 | 935 | 30 | 3569 | 3701 | 2111 | 3475 | 1895 | 3167 | 62 | 3853 | 4294 | 4557 | 4441 |

  Les lignes 11-06 et 13-05 sont sur la même page ou la précédente : à vérifier.
- **2021** (n° 128/2020, p. 3139-3140, image) : 13-01 : 288 MD ; 13-02 : 5 MD ; 13-03 : 42 MD ; 18-02 non lu.
- **2022** (n° 119/2021, p. 3108-3109, image) : 13-01 : 324 MD ; 13-02 : 4 MD ; 13-03 : 39 MD ; 18-02 : 316 MD.
- **2023-2026.** Non inventoriés. Les éditions arabes n° 141/2022, 144/2023 et 148/2025 sont en local. Le fascicule français local n° 156/2024 (LF 2025) ne compte que 5 pages.
- **Non cherché dans cette passe** : réalisations par article, lois de règlement, comptes de l'État, rapports de la DGI, nombre d'actes et de cessions.

---

## 5. Recherches infructueuses

Ce sont des lacunes de date plutôt que des textes : pas de fiche `jort_cache`, et je n'invente aucune requête.

- **Date de dépôt du JORT n° 64/1998 (loi n° 98-73).** Essais :
  - noms des notes communes locales (`grep "98-73"`) : aucune ;
  - pas d'aide-mémoire 1998 en local ;
  - diwan.tn : la fiche de la NC 5/1999 (`/fr/document/card/cd0187cb-…`) existe, mais le PDF est réservé aux abonnés ;
  - deux recherches web, sans résultat.

  À faire : NC 5/1999 sur jibaya.tn, ou édition arabe.
- **Date de dépôt du JORT n° 67/2015 (LFC 2015, art. 26-2).** Essais : NC 18/2015 (ne commente que le § 1) ; aide-mémoire NC 33/2015 (liste le texte sans date).
- **Fascicules français n° 104/2015, 104/2018 et 104/2019** : absents en local, et pist.tn répond 404 sur `Jo1042015.pdf`, `Jo1042018.pdf` et `Jo1042019.pdf`. Les pages ont été lues sur les tirés à part locaux, qui reproduisent la pagination. **Le bibliographe doit trouver l'URL de `lf-2016`, `lf-2019` et `lf-2020`.**
- **Élargissement proposé de r-2** (en `a_faire`, sans passe) :
  - les textes d'exonération antérieurs à 1966 : décret du 28 oct. 1948, art. 75 ; décret du 29 sept. 1952, art. 27-29 ; loi n° 61-18 du 31 mai 1961, art. 3 ; loi n° 65-16 du 28 juin 1965 ;
  - l'art. 52 du décret du 27 juin 1954.

  Chevauchement possible avec l'autre documentaliste : je ne les ai pas lus.
- La fiche existante `r-pv-immobiliere-modificatifs-2023` n'est pas touchée.

## 6. Références candidates

CSL minimal : type `legislation`, *Journal officiel de la République tunisienne*, URL `https://www.pist.tn/jort/AAAA/AAAAF/<fichier>`.

| Clé | Texte | Fichier pist.tn | Pages |
|---|---|---|---|
| `loi-2006-69` | loi du 28 oct. 2006 | `Jo0882006.pdf` (HTTP 200 vérifié) | 3869 ; avis du CC 3874-3880 |
| `lf-1973` | loi n° 72-87 du 27 déc. 1972 | `1972/1972F/Jo05272.pdf` | 1853 |
| `loi-87-71` | amnistie fiscale, 26 nov. 1987 | `1987/1987F/Jo08387.pdf` | 1463-1464 |
| `lf-1985` | loi n° 84-84 | `Jo07984.pdf` | 2950-2966 |
| `lf-1986` | loi n° 85-109 | `Jo09185.pdf` | 1733-1743 |
| `lf-1987` | loi n° 86-106 | `Jo07886.pdf` | 1612-1628 |
| `lf-1988` | loi n° 87-83 | `Jo09187.pdf` | 1630 |
| `lf-1991` | loi n° 90-111 | `1990/1990F/Jo08690.pdf` | 2053 |
| `loi-93-64` | publication des textes | `Jo05093.pdf` (HTTP 200 vérifié) | 931 |
| `dgi-nc-14-2012` | note commune | local `Notes_Communes/` | |
| `dgi-nc-18-2015` | note commune | local `Notes_Communes/` | |

Seules les deux URL marquées ont été vérifiées. Pour les autres, ce n'est que le gabarit `JoNNNAA` d'avant 2000 : à vérifier.

Clés existantes concernées : `lf-1993`, `lf-2003`, `lf-2005`, `lfc-2012`, `lfc-2015`, `lf-2016` à `lf-2022`, `loi-98-73`. Ajoutez-y celles que la note du 17 octobre proposait déjà (`lf-1969`, `lf-1970`, `lf-1975`, `lf-1977`, `lf-1981`, `lf-1984`, `loi-87-73`, `lf-1990`, `lf-1992`).

## 7. Ce qui reste à lire

- LF 1975 : la fin de la loi (clause générale éventuelle), éditions arabe ou française au-delà de la p. 3224.
- LF 1969 : le taux du défaut d'origine dans le tableau de l'art. 14.
- LF 1982 : le sort de l'exonération des terrains pour les actes de 1982-1983.
- Les lois de 1988 à 1993 non relues pour les successions (LFC 1988 et autres).
- Les dates de dépôt du JORT n° 64/1998 et n° 67/2015.
- Les valeurs des tableaux A antérieurs à 2020 (à l'image), ceux de 2000-2010 et ceux de 2023-2026.
- Les exposés des motifs et les débats de la Chambre des députés pour 1977, 1987 et le code de 1993 : **non cherchés dans cette passe**. Les notes de bas de page ne donnent que la date des séances (21 nov. 1987 pour la loi n° 87-73 ; 29 juil. 1998 pour la loi n° 98-73).

Sources web : [Diwan, loi n° 98-73](https://www.diwan.tn/fr/document/card/2c974b1c-098a-4d7b-8991-09981781b90f) ; [Diwan, NC 5/1999](https://www.diwan.tn/fr/document/card/cd0187cb-160e-4187-857c-8c64a0d20325) ; [pist.tn, JORT n° 88/2006](https://www.pist.tn/jort/2006/2006F/Jo0882006.pdf).

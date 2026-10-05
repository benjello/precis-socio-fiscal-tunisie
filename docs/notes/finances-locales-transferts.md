# Volume VII, ch. 9 « Les transferts de l'État » : note documentaire (FCCL, réserve, critères, CPSCL)

> Note du documentaliste, rédigée le 4 octobre 2026 et close le 5 octobre sur consigne du coordinateur. Je l'ai close de façon anticipée : seuls les textes listés ci-dessous ont été lus au fascicule. Tout le reste figure en § 11 (Lacunes) et en § 12 (fiche proposée, versée dans `docs/recherches.yml`).
>
> **Méthode.** C'est celle de `docs/notes/finances-locales-impots-locaux.md`. Les fascicules viennent du corpus local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/`.
> - Pour les années 1975 à 1992, les fascicules n'ont pas de couche texte. Ils ont été lus à l'image à 250-300 dpi, par quadrant, sur deux voies : océrisation tesseract `fra` et lecture visuelle.
> - Pour 2000, le fascicule FR a une couche texte décalée de 29, décodée selon `outillage-sources.md` § 5.
> - Pour 2006 et 2013, le texte FR a été lu directement. Le texte AR de 2006 est illisible en couche texte : il a été lu à l'image. Celui de 2013 a été lu après normalisation NFKC.
> - Le texte arabe postérieur à 2000 a été recoupé sur le miroir iort (`data/iort/textes/md/`).
> - Les pages citées ont été relues au pied de page de l'édition indiquée.
> - Les montants marqués **[OCR]** ont été lus par océrisation seule et restent à relire à l'image. Tous les autres chiffres ont été vus à l'image.
>
> **URL.** Les chemins viennent du même enregistrement jort_cache, `pdf_fr` et `pdf_ar`, préfixés `https://www.pist.tn`. Un contrôle `curl -sk` du 5 octobre 2026 a été interrompu à 25 s : il a rendu 200 `application/pdf` pour 1975 F et A, 1984, 1985, 1988, 1989, 1991, 1992, 1995, 2000 F et 2013 F et A, et 000 (délai) pour 1981, 1986, 1990, 2000 A et 2006 A. La taille n'a donc **pas** été contrôlée. Le bibliographe doit refaire le contrôle avec `--max-time 120`.
>
> **Dates de dépôt.** Les dates de dépôt au gouvernorat n'ont pas été relevées. Tous les textes lus portent leur propre clause d'effet, sauf ceux signalés « sans clause » : pour ceux-là, la règle d'avant 1993 (un jour franc après la publication) est appliquée.

---

## 1. Création du FCCL : la loi n° 75-36 du 14 mai 1975 (Q1)

- **Texte.** Loi n° 75-36 du 14 mai 1975, relative au fonds commun des collectivités locales.
  - AR : قانون عدد 36 لسنة 1975 مؤرخ في 14 ماي 1975 يتعلق بالمال المشترك للجماعات المحلية.
  - Publication : JORT n° 34 du 20 mai 1975. FR p. 1067-1068, lue à l'image. AR p. 1274, lue à l'image (art. 1 à 3) ; la suite en AR n'a pas été relue.
  - Travaux préparatoires : adoption par l'Assemblée nationale dans sa séance du 9 mai 1975 (note (1)).
- **Art. 1er : nature du fonds.** Deux fonds spéciaux du Trésor sont fusionnés en « un seul fonds spécial intitulé : "Fonds Commun des Collectivités Locales" » :
  - le « 1er Fonds Commun des Collectivités Locales » ;
  - le « Fonds Commun des Carburants et Pneumatiques ».
  - Ces deux fonds avaient été institués par l'art. 56 du décret du 25 juin 1948.
  - AR : « مال خاص بالخزينة واحد يطلق عليه اسم (المال المشترك للجماعات المحلية) ».
- **Art. 2 : alimentation par des parts d'impôts d'État.**
  1. Un prélèvement de 7 % sur l'impôt de la patente et sur l'impôt sur le bénéfice des professions non commerciales, à l'exclusion des forfaits légal et contractuel, pour lesquels le prélèvement s'élève à 25 %.
  2. 10 % des taxes sur le chiffre d'affaires instituées par l'art. 33 du décret du 29 décembre 1955.
  3. 10 % de l'impôt sur les olives, de l'impôt sur les céréales et de l'impôt sur la vigne.
  4. 50 % de l'impôt agricole.
  5. Le produit de 10 centimes additionnels au droit sur les chambres à air et pneumatiques (décret du 18 novembre 1954).
  6. Les prélèvements de 3 % et 9 % sur le droit unique de consommation de certains produits pétroliers (décret n° 70-622 du 31 décembre 1970, art. 2).
- **Art. 3 : répartition.**
  - **75 %** des ressources annuelles vont aux collectivités locales :
    - **20 %** aux conseils de gouvernorat, au prorata de leur population, déduction faite de celle des communes incluses dans leur territoire ;
    - **80 %** aux communes : moitié au prorata de la population, moitié au prorata de la moyenne des recettes des trois dernières années « au titre des taxes municipales grevant la propriété bâtie ».
  - « Le solde de 25 % des ressources du Fonds » est réparti comme suit :
    - 5 % à la commune de Tunis ;
    - 6 % à la Caisse des prêts et de soutien des collectivités locales ;
    - 4 % aux communes de Tunis, Sfax, Sousse et Bizerte, pour le financement partiel de leurs programmes d'équipement, proportionnellement à l'importance de leurs budgets ;
    - 8 % à l'Office national de l'assainissement ;
    - 2 % au District de Tunis.
  - Termes arabes : le « solde » est « **المدخر** » (« اما المدخر البالغ 25٪ من محصول المال المشترك ») ; les conseils de gouvernorat sont « مجالس الولايات ».
- **Art. 4.** Il abroge :
  - les art. 57 et 58 du décret du 25 juin 1948 ;
  - le § 6 de l'art. 11 du décret n° 72-49 du 18 février 1972 (District de Tunis) ;
  - l'art. 79 de la loi n° 74-101 (LF 1975, clé existante `loi74-101-lf1975`).
- **Art. 5 : date d'effet.** « La présente loi prendra effet à compter du 1er janvier 1976. » Date d'effet : **1er janvier 1976**.
- **Texte d'application identifié, non lu.** Arrêté du ministre des Finances du 17 octobre 1975 portant fixation des recettes et des dépenses du fonds spécial du Trésor « fonds commun… » (JORT n° 68 du 21 octobre 1975, p. 2224-2225). Les arrêtés du même objet de 1977, 1978 et 1979 (JORT 1977 n° 81 p. 3381, 1978 n° 64 p. 2661, 1979 n° 53 p. 2425) et les arrêtés de relèvement des prévisions de 1982 et 1983 (1982 n° 59 p. 1898, 1983 n° 62 p. 2467) ne sont pas lus non plus.

## 2. Modifications de l'art. 3 de la loi 75-36 : quote-part, réserve, critères (Q3, Q4)

Tous les textes de cette section ont été lus au fascicule.

| Texte | Disposition | Avant → après | Effet |
|---|---|---|---|
| **LF 1982**, loi n° 81-100 du 31 déc. 1981, **art. 27** (« Finances locales ») — JORT n° 84 du 29-31 déc. 1981, FR p. 3036 (image) | Art. 3 récrit en entier | CL 75 % (inchangé), dont **20 % CG / 80 % communes** (inchangé). **CG** : 100 % population → **15 % à égalité, 85 % population** (hors population communale). **Communes** : 50 % population / 50 % propriété bâtie → **10 % à égalité, 45 % population, 45 % moyenne triennale des taxes municipales sur la propriété bâtie**. **Solde 25 %** : Tunis 5 → **6 %** (« pour financer ses projets d'investissement ») ; CPSCL 6 % ; les 4 % des 4 grandes communes → **3 % aux communes sièges des gouvernorats**, à parts égales ; ONAS 8 % ; District 2 %. | Clause générale non relevée. Sans clause : publication le 31 déc. 1981, un jour franc, donc exécutoire le **2 janv. 1982**. À contrôler sur le dernier article de la loi. |
| **LF 1985**, loi n° 84-84 du 31 déc. 1984, **art. 63** (« Emploi de la quote-part du fonds commun allouée à la municipalité de Tunis ») — JORT n° 79 du 28-31 déc. 1984, FR p. 2960 | § 4, tiret « commune de Tunis » | Les 6 % restent destinés aux projets d'investissement. Ajout : un arrêté conjoint Intérieur-Finances peut autoriser l'affectation d'une partie, « ne dépassant pas le tiers », aux dépenses ordinaires du titre I. « Le reste sans changement. » | Même réserve (sans clause : 2 janv. 1985). |
| **LF 1986**, loi n° 85-109 du 31 déc. 1985, **art. 68** (« Modification des taux de répartition du fonds commun ») — JORT n° 91 du 31 déc. 1985, FR p. 1740 (image) | § 1 de l'art. 3, « tel que modifié par l'art. 27 de la LF 1982 et par l'art. 63 de la LF 1985 » | CL 75 % ; **CG 20 → 14 %**, **communes 80 → 86 %** | Même réserve (sans clause : 2 janv. 1986). |
| **LF 1992**, loi n° 91-98 du 31 déc. 1991, **art. 80** (« Distribution du solde du fonds commun ») — JORT n° 90 du 31 déc. 1991, FR p. 2091 [OCR] | § 4 | Les pourcentages fixes du solde disparaissent. Le solde de 25 % « est attribué **par décret** » à la commune de Tunis, au conseil régional de Tunis, aux communes sièges de gouvernorats, au District de Tunis, à la CPSCL et à l'ONAS. « Ce décret peut réserver […] une partie de ce solde en l'ajoutant à la part revenant aux communes » du § 1, sur la base des critères du § 3. | Sans clause relevée : 2 janv. 1992. **C'est le texte qui fonde les décrets annuels de répartition de la réserve.** |
| **Loi n° 95-45 du 8 mai 1995**, art. 1er — JORT n° 39 du 16 mai 1995, FR p. 1111 (texte) | § 4 (« tel que modifié par l'art. 80 de la loi n° 91-98 ») | Bénéficiaires du solde de 25 % : ajout de **l'Office national de la protection civile**. Une partie du solde peut s'ajouter à la part des communes (critères de l'al. 3). « Les répartition et attribution sont fixées par décret. » | Art. 2 : « entre en vigueur le **1er janvier 1995** » (rétroactif). AR p. 1111 non relue (couche texte AR vide). |
| **Loi n° 2000-60 du 13 juin 2000**, art. 1er — JORT n° 48 du 16 juin 2000, FR p. 1461, AR p. 1489 (image) | Al. 2 et 3 de l'art. 3 (« telle que modifiée par la loi n° 95-45 ») | **CG** : 15 / 85 → **25 % à égalité, 75 % population** (hors population communale). **Communes** : 10 / 45 / 45 → **10 % à égalité ; 45 % population ; 41 % moyenne triennale des recettes de TIB ; 4 % au prorata de la population** entre les communes dont la moyenne triennale (TIB enrôlée, TCL, taxe hôtelière, produits des marchés affermés) est inférieure à la moyenne de toutes les communes. | Art. 2 : « entre en vigueur le **1er janvier 2001** ». |
| **LF 2007**, loi n° 2006-85 du 25 déc. 2006, **art. 11** (« Révision des critères de répartition du fonds commun ») — JORT n° 103 du 26 déc. 2006, FR p. 4381, AR p. 5133 (image) | § 1 et § 4 (« modifiée notamment par la loi n° 85-109 et la loi n° 95-45 ») | **CL 75 → 82 %** : CR 14 %, communes 86 %. **Solde 25 → 18 %**, réparti entre la commune de Tunis, le conseil régional de Tunis, les communes sièges de gouvernorats et la CPSCL. **Sortent** : le District, l'ONAS et l'Office de la protection civile. Une partie peut s'ajouter à la part communale ; « Les répartitions et attributions sont fixées par décret. » | Art. 88 (FR p. 4395) : applicable « à compter du premier janvier 2007 ». **1er janv. 2007.** |
| **LF 2014**, loi n° 2013-54 du 30 déc. 2013, **art. 12** (« Rationalisation des critères de répartition du FCCL ») — JORT n° 105 du 31 déc. 2013, FR p. 3668, AR p. 4346 (texte) | 1) al. 3 et 4 du § 3 ; 2) § 4 | 1) Communes : **41 → 37 %** (TIB) et **4 → 8 %** (communes à faible potentiel). 2) Solde de 18 % : « jusqu'à la limite de » **24 %** à la commune de Tunis, **3 %** au CR de Tunis, **30 %** aux communes sièges de gouvernorats, **27 %** à la CPSCL, et **16 %** « aux exigences de l'autorité de tutelle centrale, pour satisfaire les besoins spécifiques et imprévus des CL ». Une quote-part peut s'ajouter à la part communale « par décret ». | Art. 95 : « à compter du 1er janvier 2014 ». **1er janv. 2014.** |

**Termes arabes** (relevés en JORT AR 2006 et 2013, et sur le miroir iort) :
- مناب الجماعات المحلية من المال المشترك ;
- المدّخر البالغ 18% من محصول المال المشترك ;
- المجالس الجهوية ;
- البلديات مراكز الولايات ;
- صندوق القروض ومساعدة الجماعات المحلية ;
- « لحد 16 % لمتطلبات سلطة الإشراف المركزية في مجال تلبية الحاجيات الخصوصية والطارئة للجماعات المحلية » ;
- intitulé de l'art. 12 de la LF 2014 : « ترشيد مقاييس توزيع المال المشترك للجماعات المحلية » ;
- intitulé de l'art. 11 de la LF 2007 : « مراجعة مقاييس توزيع المال المشترك ».

**Contrôle des repères du brief.**
- Les « 25 % autrefois » sont confirmés pour 1976-2006 (loi 75-36, LF 1982, loi 95-45).
- Les « 18 % de 2006 à 2013 » sont confirmés à partir du 1er janvier 2007 (LF 2007). Ils restent en vigueur en 2014 avec la LF 2014, qui ne touche pas au taux de 18 %.
- Le passage à **15 % en 2018-2019** des données DGCT n'est fondé sur aucun texte lu ici : voir § 9.
- La « quote-part des communes ≈ 70,5 % » est égale à 82 % × 86 % = 70,52 %. C'est un calcul, pas un chiffre imprimé au JORT.

**Note de méthode.** La loi 2000-60 vise les al. 2 et 3 « tels que modifiés par la loi 95-45 », alors que la loi 95-45 ne modifiait que l'al. 4. La chaîne réelle des alinéas 2 et 3 passe par la LF 1982, art. 27. C'est l'imprécision du visa de 2000, à ne pas recopier.

## 3. Alimentation et montant (Q2)

- **1976-1986 : parts d'impôts d'État.** L'alimentation suit l'art. 2 de la loi 75-36 (taux du § 1). Aucun texte modifiant cet art. 2 n'a été identifié dans les titres de jort_cache. **L'« indexation jusqu'en 1986 » du guide correspond à ce régime de parts fiscales.**
- **Fin des parts fiscales au 1er janvier 1987 : LF 1987, loi n° 86-106 du 31 déc. 1986, art. 92.**
  - Source : JORT n° 78 du 30-31 déc. 1986, FR p. 1623, lu à l'image.
  - Texte : « Les impôts, droits, taxes, redevances et contributions à caractère fiscal ou para-fiscal affectés en totalité ou en partie […] aux fonds spéciaux de trésor désignés ci-dessous, reviennent au profit du budget général de l'État ». Suit, sous le ministère de l'Intérieur, « — Fonds commun des collectivités locales ».
  - « Toutes les dispositions antérieures contraires au présent article sont abrogées. »
  - L'art. 91 (même page) supprime le « Fonds de développement municipal ».
- **À partir de 1987, le FCCL est alimenté par une « subvention du budget ».** Exemple vu à l'image : **LF 1990** (loi n° 89-115 du 30 déc. 1989), « Gestion 1990 — Tableau "L" fonds spéciaux du Trésor », JORT n° 88 du 29-31 déc. 1989, FR p. 2239. Ligne « Fonds Commun des Collectivités Locales » :
  - subvention du budget **80.000.000** ;
  - autres recettes « — » ;
  - total des recettes 80.000.000 ;
  - dépenses 80.000.000.
- **Prélèvements annuels autorisés par la loi de finances** (tous lus au fascicule) :
  - **LF 1987, art. 44** (p. 1618) : 700.000 D au profit de la régie administrative de la protection civile « sur les crédits du FCCL de 1987 ».
  - **LF 1987, art. 94** (p. 1623) : 2.500.000 D au profit de la CPSCL, pour ses interventions de l'art. 4 de la loi 75-37.
  - **LF 1988**, loi n° 87-83 (clé existante `loi-87-83-lf-1988`), JORT n° 91 du 29-31 déc. 1987, p. 1634 :
    - art. 69 : 2.500.000 D à la CPSCL ;
    - art. 70 : 1.500.000 D pour la hausse de la prime de rendement des agents des CL ;
    - art. 71 : 700.000 D à la protection civile ;
    - **art. 72 : « Est reconduit pour l'année 1988 le montant réparti en 1987 des crédits destinés à la réserve du FCCL »**.
  - **LF 1989**, loi n° 88-145, JORT n° 87 du 30-31 déc. 1988, p. 1803 :
    - art. 100 : 2.500.000 D à la CPSCL ;
    - art. 101 : 1.500.000 D pour la prime de rendement, et 3.800.000 D sur « l'enveloppe globale » pour la hausse des salaires de 1989 ;
    - art. 102 : 700.000 D à la protection civile ;
    - art. 103 : reconduction du montant de la réserve de 1988.
  - **LF 1990**, loi n° 89-115, JORT n° 88, p. 2152 :
    - art. 53 : **3.500.000 D** [OCR] à la CPSCL ;
    - art. 54 : 700.000 D à la protection civile ;
    - art. 55 : reconduction pour 1990 du montant de la réserve réparti en 1989.
  - **LF 1991**, loi n° 90-111, JORT n° 86 du 28-31 déc. 1990 :
    - art. 79 (p. 2058) : 3.500.000 D [OCR] à la CPSCL ;
    - art. 80 (p. 2059) : 700.000 D à la protection civile ;
    - art. 81 (p. 2059) : reconduction de la réserve de 1990.
  - **LF 1977, 1978 et 1979 : identifiés, non lus.** Les titres de jort_cache mentionnent des prélèvements de 1.000.000 D (loi 76-115, art. 61, p. 3169), de 780.000 D (loi 77-81, art. 25, p. 3602) et de 270.000 D (loi 78-59, art. 22, p. 3775) « sur les produits du FCCL ».
- **Comptes spéciaux 2011-2017.** Le compte apparaît dans les tableaux de la LF sous le nom « حساب المال المشترك للجماعات العمومية المحلية ». Il figure en 2014 à côté du « صندوق التعاون بين الجماعات المحلية » (tableau des comptes spéciaux de la LF 2014, AR, vu en couche texte). L'alignement des montants y est **ambigu** : à lire à l'image avant de citer un chiffre.

## 4. Q6 : le FCCL de 1990

- **JORT.** LF 1990, tableau « L » : **80 MD**, subvention du budget, en prévision.
- **Part des communes.** Le JORT ne l'imprime pas : seule la clé légale est connue (75 % × 86 % en 1990). Ne pas présenter 51,6 MD comme un chiffre du JORT.
- **La réserve 1990** est reconduite au montant de 1989 (art. 55). Ce montant n'est pas connu ici : aucun décret de répartition n'est publié avant 1992.
- **Divergence avec la Banque mondiale** (82 MD en 1992, 50,8 MD en 1997). Elle **ne se tranche pas** par le JORT lu.
  - L'écart de 2 MD peut tenir à une exécution différente de la prévision, ou à une ouverture complémentaire.
  - Aucune loi de finances complémentaire 1990, ni aucun arrêté de relèvement des prévisions pour 1990, n'a été cherché.
  - Les 50,8 MD peuvent être un montant net des prélèvements de l'année (CPSCL 3,5 MD, protection civile 0,7 MD, réserve) : c'est une hypothèse, non vérifiée.

## 5. Décrets de répartition de la réserve (Q5)

Un seul décret a été **lu** : 92-308. Les autres sont identifiés dans jort_cache, avec le texte arabe intégral présent sur le miroir iort (`dec_9x_…`, `dec_200x_…`), mais **non lus au fascicule**. Les montants sont à relever.

| Décret | Date | JORT n° (date) | Pages (jort_cache) | Contenu |
|---|---|---|---|---|
| **92-308** | 10 févr. 1992 | 12 (25 févr. 1992) | FR 227-228, lu [OCR] | Visa : loi 91-98, art. 80. « La réserve du fonds commun des collectivités locales fixée à **24 millions de dinars** pour la gestion 1992 est répartie » : commune de Tunis 4 600 000 ; District de Tunis 920 000 ; CPSCL 7 620 000 ; communes sièges des gouvernorats 2 600 000 ; ONAS 7 680 000 ; conseil régional de Tunis 580 000 (somme : 24 000 000). Exécutoire le 27 févr. 1992 (un jour franc). AR non lu. |
| 93-155 | 25 janv. 1993 | 9 (2 févr. 1993) | 175-176 | « répartition des reliquats de la caisse du fonds commun » — non lu (PDF FR p. 7). |
| 94-592 | 22 mars 1994 | 25 (1er avr. 1994) | 540 | non lu |
| 95-1122 | 28 juin 1995 | 54 (7 juil. 1995) | 1454 | non lu |
| 96-910 | 8 mai 1996 | 40 (17 mai 1996) | 958 | non lu |
| 97-390 | 21 févr. 1997 | 17 (28 févr. 1997) | 360 | non lu |
| 98-397 | 18 févr. 1998 | 15 (20 févr. 1998) | 373 | non lu |
| 99-491 | 1er mars 1999 | 21 (12 mars 1999) | 372 | non lu |
| 2000-318 | 7 févr. 2000 | 14 (18 févr. 2000) | 471 | non lu ; pdf_ar `/jort/2000/2000A/Ja01400.pdf` (nommage atypique) |
| 2001-418 | 13 févr. 2001 | 15 (20 févr. 2001) | 310 | non lu |
| 2002-110 | 28 janv. 2002 | 10 (1er févr. 2002) | 191 | non lu |
| 2003-448 | 24 févr. 2003 | 17 (28 févr. 2003) | 447 | non lu |
| 2004-271 | 9 févr. 2004 | 13 (13 févr. 2004) | 347 | non lu |
| 2005-205 | 7 févr. 2005 | 13 (15 févr. 2005) | 371 | non lu |
| 2006-554 | 23 févr. 2006 | 18 (3 mars 2006) | 461 | non lu |
| 2007-384 | 26 févr. 2007 | 18 (2 mars 2007) | 652 | non lu |
| 2007-1303 | 28 mai 2007 | 45 (5 juin 2007) | 1897 | « crédit complémentaire au titre de la réserve » — non lu |
| 2008-354 | 11 févr. 2008 | 14 (15 févr. 2008) | 729 | non lu |
| 2009-355 | 9 févr. 2009 | 13 (13 févr. 2009) | 492 | non lu |
| 2010-461 | 15 mars 2010 | 23 (19 mars 2010) | 717 | non lu |
| 2011-276 | 14 mars 2011 | 17 (15 mars 2011) | 308 | non lu |
| 2012-147 | 10 avr. 2012 | 29 (13 avr. 2012) | 657 | non lu |
| 2013-1503 | 6 mai 2013 | 39 (14 mai 2013) | 1461-1462 | non lu |

Il n'y a **pas de décret de répartition pour 2014-2017**, ni dans les titres FR et AR de jort_cache, ni dans le miroir iort (fiche r-fccl-repartition-reserve-2014-2017, § 10).
- **Hypothèse, à ne pas écrire comme un fait :** l'art. 12 de la LF 2014 fixe lui-même des plafonds par bénéficiaire. Cela a pu rendre le décret annuel superflu.

## 6. Suppression du FCCL et ce qui suit (Q7) : identifié, non lu

- **LF 2018**, loi n° 2017-66 du 18 déc. 2017 (clé existante `lf-2018`), JORT n° 101 du 19 déc. 2017.
  - Titre jort_cache : « حذف الحساب الخاص في الخزينة والمسمى حساب المال المشترك للجماعات العمومية المحلية - الفصل 11 الملغي لأحكام القانون عدد 36 لسنة 1975 ».
  - **Art. 11.** Pages non relevées. La date d'effet n'est pas lue : le 1er janvier 2018 est probable, mais la clause générale reste à lire.
  - Le tableau des comptes spéciaux de la même LF (miroir iort) place le compte sous « وزارة الشؤون المحلية والبيئة ». L'extraction mal alignée y montre aussi 100 000 000 et 6 000 000, sans permettre de rattacher un montant au compte : **à lire à l'image**.
- **Un fonds distinct à ne pas confondre avec le FCCL : le fonds de coopération entre les collectivités locales.**
  - LF 2013, loi n° 2012-27 du 29 déc. 2012, **art. 13 à 15** : « إحداث صندوق التعاون بين الجماعات المحلية » (JORT 2013 n° 1).
  - Critères fixés par le **décret n° 2013-2797 du 8 juillet 2013** (JORT n° 56 du 12 juil. 2013, p. 2148-2150) : « fixant les modalités et les critères de répartition des ressources du fonds de coopération des collectivités locales ».
  - **C'est un fonds distinct du FCCL** (المال المشترك).
- **LF 2021**, loi n° 2020-46 du 23 déc. 2020, **art. 13** : « إحداث صندوق دعم اللامركزية والتسوية والتعديل والتضامن بين الجماعات المحلية » (JORT n° 128 du 25 déc. 2020 ; pdf_ar seul, `/jort/2020/2020A/Ja1282020.pdf`).
- **Code des collectivités locales** (loi organique n° 2018-29, clé existante `loi-org-2018-29-ccl`) : les articles sur les ressources transférées, la péréquation et l'appui ne sont pas lus. **Correction à vérifier :** `_taxes_redevances.qmd` attribue à l'art. 392 le sort du « Fonds de coopération entre les collectivités locales ». Il faut lire l'art. 392 en AR pour savoir s'il vise صندوق التعاون (le fonds de 2013) ou المال المشترك.

## 7. CPSCL (Q8)

- **Loi n° 75-37 du 14 mai 1975**, portant transformation de la Caisse des prêts aux communes en une caisse des prêts et de soutien des collectivités locales. JORT n° 34 du 20 mai 1975, FR p. 1068, lue à l'image.
  - **Art. 1er.** La caisse des prêts aux communes, « instituée par le décret du 15 décembre 1902 et réorganisée par le décret du 1er mars 1932 », est transformée en « caisse des prêts et de soutien des collectivités locales ».
  - **Art. 2.** Elle est dotée de la personnalité civile et de l'autonomie financière. Sa gestion peut être confiée à un établissement financier, par convention approuvée par décret.
  - **Art. 3 : ressources.**
    1. Le prélèvement sur les ressources annuelles du FCCL institué par la loi 75-36.
    2. Les annuités de remboursement de ses prêts.
    3. Le produit de ses emprunts.
    4. Le produit de ses opérations financières.
    5. Toute autre recette créée ou affectée par la loi.
  - **Art. 4.** Elle consent aux communes, aux syndicats de communes, aux conseils de gouvernorat et à leurs établissements :
    1. des prêts d'investissement d'intérêt public ;
    2. des subventions aux syndicats et aux collectivités « astreintes à des sujétions spéciales, nécessaires ou imprévisibles ou dont la situation financière est particulièrement difficile » ;
    3. des bonifications d'intérêts.
    - Elle peut être autorisée à entreprendre des investissements d'intérêt local ou régional prévus par le plan.
    - Les subventions sont accordées « dans la limite de la moitié du montant du prélèvement sur les ressources annuelles du FCCL ».
  - **Art. 5.** Les modalités et les conditions d'attribution sont fixées par décret.
  - **Art. 6 : effet au 1er janvier 1976.**
  - Le lien avec le FCCL tient donc à la part du solde (6 % en 1976) et aux prélèvements annuels de la LF (§ 3).
- **Textes identifiés, non lus** (jort_cache) :
  - organisation : décret n° 77-212 du 4 mars 1977 (JORT n° 16, p. 555-558), modifié par le décret n° 79-619 du 4 juillet 1979 (n° 44, p. 2008-2009) ; décret n° 92-688 du 16 avril 1992 (n° 24, p. 468-469) ;
  - conditions des prêts et des subventions : décret n° 92-1092 du 6 juin 1992 (n° 37, p. 732-733) ; décret n° 97-1135 du 16 juin 1997 (n° 49, p. 1126-1128) — le guide Gilbert le date à tort du « 16 janvier 1997 » ; décret n° 2014-3505 du 30 septembre 2014 (n° 79, p. 2576-2578) ;
  - fonds de dotation : loi n° 2001-56 du 22 mai 2001 (n° 42, p. 1200) ;
  - subventions annuelles : arrêté du ministre de l'Intérieur du 13 juillet 2015 fixant les conditions minimales du transfert des subventions annuelles (n° 57, p. 1547-1548), modifié par un arrêté du ministre des Affaires locales du 14 novembre 2017 (n° 93) ;
  - taux et durées des prêts : décret gouvernemental n° 2016-367 du 18 mars 2016 (n° 23) ;
  - organigramme : décret gouvernemental n° 2021-505 du 25 juin 2021 (n° 58, p. 1840) ;
  - LF 1992, art. 81 (p. 2091, lu [OCR]) : les communes sont dispensées des échéances de 1992 des emprunts contractés auprès de la CPSCL et nourris sur ses ressources propres ; les montants sont inscrits à leur budget d'équipement.

## 8. Q9 : subventions d'investissement, programmes régionaux, dotation exceptionnelle

Rien n'a été lu au JORT pour cette question. Le guide Gilbert 2013, ch. 5, en donne les repères, sans valeur de source finale :
- PIC et procédure CPSCL : § 5.5.1 ;
- crédits du titre II de la DGCL gérés par la CPSCL (8 MD en 2013) : § 5.5.2.1 ;
- PRD : environ 82 MD en 2011 (§ 5.5.2.3) ;
- dotation exceptionnelle 2011-2012 : § 5.4.

Dafflon et Gilbert 2018, ch. 6, n'a pas été relu pour sa pagination.

## 9. Références candidates

**Déjà présentes, à compléter dans leur `note`** : `loi74-101-lf1975`, `loi-87-83-lf-1988` (art. 69-72, p. 1634), `lf-2007` (art. 11, FR p. 4381, AR p. 5133), `lf-2014` (art. 12, FR p. 3668, AR p. 4346), `lf-2018` (art. 11), `lf-2013` (art. 13-15), `loi-org-2018-29-ccl`, `loi93-64`, `dafflon-gilbert-2018`, `wb-msip-1992`, `wb-mdp2-1997`, `cpscl-etats-financiers`, `dgct-donnees-ouvertes`.

**À créer** (type `legislation`, container-title « Journal officiel de la République tunisienne », URL = `https://www.pist.tn` + chemin jort_cache, contrôle de taille à refaire) :

| Clé | Texte | JORT | Pages lues | pdf_fr / pdf_ar |
|---|---|---|---|---|
| `loi75-36` | Loi n° 75-36 du 14 mai 1975, relative au fonds commun des collectivités locales | n° 34, 20 mai 1975 | FR 1067-1068 ; AR 1274 | /jort/1975/1975F/Jo03475.pdf ; /jort/1975/1975A/Ja03475.pdf |
| `loi75-37` | Loi n° 75-37 du 14 mai 1975, portant transformation de la caisse des prêts aux communes en une caisse des prêts et de soutien des collectivités locales | n° 34, 20 mai 1975 | FR 1068 | mêmes fascicules |
| `loi81-100-lf1982` | Loi n° 81-100 du 31 déc. 1981, portant loi de finances pour la gestion 1982 (art. 27) | n° 84, 29-31 déc. 1981 | FR 3036 | /jort/1981/1981F/Jo08481.pdf ; /jort/1981/1981A/Ja08481.pdf |
| `loi84-84-lf1985` | Loi n° 84-84 du 31 déc. 1984, LF 1985 (art. 63) | n° 79, 28-31 déc. 1984 | FR 2960 | /jort/1984/1984F/Jo07984.pdf ; /jort/1984/1984A/Ja07984.pdf |
| `loi85-109-lf1986` | Loi n° 85-109 du 31 déc. 1985, LF 1986 (art. 68) | n° 91, 31 déc. 1985 | FR 1740 | /jort/1985/1985F/Jo09185.pdf ; /jort/1985/1985A/Ja09185.pdf |
| `loi86-106-lf1987` | Loi n° 86-106 du 31 déc. 1986, LF 1987 (art. 44, 91, 92, 94) | n° 78, 30-31 déc. 1986 | FR 1618, 1623 | /jort/1986/1986F/Jo07886.pdf ; /jort/1986/1986A/Ja07886.pdf |
| `loi88-145-lf1989` | Loi n° 88-145 du 29 déc. 1988, LF 1989 (art. 100-103) | n° 87, 30-31 déc. 1988 | FR 1803 | /jort/1988/1988F/Jo08788.pdf ; /jort/1988/1988A/Ja08788.pdf |
| `lf-1990` | Loi n° 89-115 du 30 déc. 1989, LF 1990 (art. 53-55 ; tableau « L ») | n° 88, 29-31 déc. 1989 | FR 2152, 2239 | /jort/1989/1989F/Jo08889.pdf ; /jort/1989/1989A/Ja08889.pdf |
| `loi90-111-lf1991` | Loi n° 90-111 du 31 déc. 1990, LF 1991 (art. 79-81) | n° 86, 28-31 déc. 1990 | FR 2058-2059 | /jort/1990/1990F/Jo08690.pdf ; /jort/1990/1990A/Ja08690.pdf |
| `loi91-98-lf1992` | Loi n° 91-98 du 31 déc. 1991, LF 1992 (art. 80-81) | n° 90, 31 déc. 1991 | FR 2091 | /jort/1991/1991F/Jo09091.pdf ; /jort/1991/1991A/Ja09091.pdf |
| `decret92-308` | Décret n° 92-308 du 10 févr. 1992, relatif à la répartition de la réserve du fonds commun | n° 12, 25 févr. 1992 | FR 227-228 | /jort/1992/1992F/Jo01292.pdf ; /jort/1992/1992A/Ja01292.pdf |
| `loi95-45` | Loi n° 95-45 du 8 mai 1995, modifiant la loi n° 75-36 | n° 39, 16 mai 1995 | FR 1111 | /jort/1995/1995F/Jo03995.pdf ; /jort/1995/1995A/Ja03995.pdf |
| `loi2000-60` | Loi n° 2000-60 du 13 juin 2000, modifiant la loi n° 75-36 | n° 48, 16 juin 2000 | FR 1461 ; AR 1489 | /jort/2000/2000F/Jo0482000.pdf ; /jort/2000/2000A/Ja04800.pdf |

Il faut aussi des clés `decret93-155`, `decret94-592` … `decret2013-1503` (chemins dans le tableau du § 5, une fois les décrets lus), `loi2012-27-lf2013` si `lf-2013` ne couvre pas ce texte, `decret2013-2797`, `loi2020-46-lf2021`, `decret92-688`, `decret97-1135`, `decret2014-3505` et `loi2001-56`.

**Doctrine.** Les rapports du PARD 2021-2022 (dossier `voisins/`) n'ont pas été ouverts : pas de proposition de clé.

## 10. Notions à glossaire (FR / AR attesté au JORT)

- **Fonds commun des collectivités locales (FCCL)** : المال المشترك للجماعات المحلية (loi 75-36, AR). Nom du compte spécial dans les LF : حساب المال المشترك للجماعات العمومية المحلية.
- **Réserve (solde) du FCCL** : المدخر / المدّخر (loi 75-36 ; LF 2007 ; LF 2014). Le FR dit « solde », puis « réserve » (LF 1988, art. 72 ; décret 92-308).
- **Quote-part des collectivités locales** : مناب الجماعات المحلية (LF 2007).
- **Fonds spécial du Trésor** : مال خاص بالخزينة (1975). Puis **compte spécial du Trésor** : الحساب الخاص في الخزينة (LF 2018).
- **Caisse des prêts et de soutien des collectivités locales (CPSCL)** : صندوق القروض ومساعدة الجماعات المحلية (LF 2007).
- **Fonds de coopération entre les collectivités locales** (2013) : صندوق التعاون بين الجماعات المحلية. Distinct du FCCL.
- **Fonds de soutien à la décentralisation, de péréquation, de régularisation et de solidarité entre les collectivités locales** (LF 2021) : صندوق دعم اللامركزية والتسوية والتعديل والتضامن بين الجماعات المحلية. La traduction française est **à vérifier** dans l'édition FR, si elle existe.
- **Communes sièges des gouvernorats** : البلديات مراكز الولايات.

## 11. Lacunes (TODO)

1. Décrets de répartition 93-155 et 94-592 à 2013-1503 : à lire, FR et AR (montant global, bénéficiaires, parts, page AR, date exécutoire). Les AR post-2000 sont lisibles via le miroir iort ; les FR 1993-1999 sont des scans.
2. Décret 92-308 : relire les montants à l'image (lus en [OCR] seulement) et relever la page AR.
3. LF 2018, art. 11 : texte, pages FR et AR, clause d'effet.
4. CCL 2018 : articles sur les dotations, la péréquation et l'appui, et l'art. 392.
5. LF 2013, art. 13-15 ; décret 2013-2797 ; LF 2021, art. 13.
6. Origine du taux de 15 % des données DGCT pour 2018-2019 : aucun texte identifié.
7. Montant du FCCL LF par LF : seul 1990 est lu (80 MD). Les tableaux des fonds spéciaux de 1987 à 2006, puis les comptes spéciaux de 2007 à 2017, restent à lire à l'image.
8. Lois de finances 1977-1979 (prélèvements) et arrêtés de 1975-1983 sur le FCCL : non lus.
9. Clauses générales d'effet des LF 1982, 1985, 1986 et 1992 : non vérifiées.
10. Pages AR de 75-37, 95-45, des LF 1982-1992 et de 92-308.
11. CPSCL : décrets 77-212, 92-688, 92-1092, 97-1135, 2014-3505, loi 2001-56, arrêtés de 2015 et 2017 : non lus.
12. Q9 (PIC, PRD, dotation exceptionnelle 2011-2012) : aucune source primaire lue.
13. Divergence 82 / 50,8 MD pour 1990 : non tranchée (§ 4).

## 12. Recherches infructueuses : fiche proposée

```yaml
- id: r-fccl-repartition-reserve-2014-2017
  objet: >-
    décret (ou arrêté) répartissant la réserve (المدخر) du fonds commun des collectivités
    locales pour les gestions 2014 à 2017, après l'art. 12 de la LF 2014 (loi n° 2013-54)
  ou: precis/fr/finances_locales/_transferts.qmd#sec-fl-fccl-reserve
  requetes:
    - source: titres_fts
      terme: '"fonds commun"'
    - source: titres_fts
      terme: 'reserve AND fonds AND commun'
    - source: titres_like
      terme: "%fonds commun des collectivit%"
    - source: titres_like
      terme: "%المال المشترك%"
    - source: titres_like
      terme: "%احتياطي% + %توزيع%"
    - source: iort_ar
      terme: "المال المشترك"
    - source: iort_ar
      terme: "احتياطي + الجماعات"
  passes:
    - date: 2026-10-04
      par: documentaliste
      resultat: aucun
      couvert_jusqu_au: 2026-09-18
      sources: [jort_cache, iort]
      couverture: >-
        Titres FR (FTS et LIKE) et AR (LIKE) de jort_cache jusqu'à la dernière publication
        indexée ; grep du miroir iort (dec_, dec_gouv_, arr_, loi_). Le dernier décret trouvé
        est le 2013-1503. Lacunes : pas de recherche plein texte dans les fascicules 2014-2017 ;
        l'intitulé « المدخر » (et non « احتياطي ») n'a pas été cherché dans les titres ; aucune
        consultation de pist.tn en ligne.
```

Pour cette fiche : le terme « المدخر » (titres) est la prochaine requête à lancer avec `elargir … --terme "المدخر" --source titres_like`. Cette fiche n'est pas encore inscrite dans `docs/recherches.yml` : je n'ai lancé ni `recherches.py lister` par sujet ni `passe`, la consigne étant de ne rien écrire.

Fichiers de travail (non versionnés), sous `/tmp/claude-1001/-home-benjello-projets-precis-socio-fiscal-tunisie/212eebb3-5a49-4181-98e4-bbe6590342a7/scratchpad/doc-fccl/` :
- `txt/` : textes extraits ;
- `ocr/` : océrisations des pages lues ;
- `img/` : rendus et recadrages.

Aucun processus n'est resté actif.

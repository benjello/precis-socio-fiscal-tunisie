# Les politiques de l'emploi — note documentaire

> Note du documentaliste, 6 octobre 2026, pour le chapitre à écrire « Les politiques de l'emploi »
> du volume VIII « Le marché du travail » (annoncé dans `precis/fr/marche_travail/index.qmd`).
> Elle ne rédige pas le précis. Consigne retenue : l'économique avant le juridique — dépense,
> effectifs, temps long ; du droit, seuls les paramètres qui commandent la dépense (public, durée,
> indemnité de l'État, cotisations prises en charge, date d'effet).
>
> Marqueurs internes (à ne pas reporter dans le précis) : **[T]** lu sur couche texte fiable ;
> **[T°]** lu par OCR (fascicules de 1967 à 1993), chiffres non relus à l'image ; **[T-ar]** lu dans
> l'édition arabe ; **[M]** notice `jort_cache.db` seule (intitulé, fascicule, pages) ; **[D]** dérivé.
> Pagination de l'édition française, sauf mention. URL :
> `https://www.pist.tn/jort/<année>/<année>F/Jo<n°><aa|aaaa>.pdf` (arabe : `A/Ja` ; an 2000 arabe :
> `Ja<n°>00.pdf`). Les 43 fascicules cités ont été sondés le 6 octobre 2026 (requête HEAD, `-k`) :
> tous répondent `application/pdf` dans les deux langues, **sauf deux éditions françaises absentes
> (404)** : n° 51 de 2019 et n° 142 de 2022.

## 0. Résultat principal

1. **La chaîne des textes est établie de 1967 à 2023.** Institutions : office (1967), OTTEEFP (1973),
   deux offices (1983, puis 1988), Agence tunisienne de l'emploi (1993), ANETI (2003). Programmes :
   loi n° 81-75 (contrat emploi-formation), décrets de 1987 et 1988 (SIVP 1 et 2), refonte de 1993
   (décret n° 93-1049), puis trois décrets « fixant les programmes du Fonds national de l'emploi » —
   **n° 2009-349, n° 2012-2369 et n° 2019-542** — avec douze modificatifs lus. Les trois jalons
   pressentis par le ticket sont confirmés au texte, avec une réserve de taille sur 2012 (point 3).
2. **Le Fonds national de l'emploi (« 21-21 ») est un compte spécial du Trésor créé par la loi de
   finances pour 2000** (art. 13-14), alimenté à l'origine par des dons et une part des produits de
   privatisation, puis par des taxes affectées (LF 2001, art. 14 ; LF 2003, art. 27). La même loi
   crée un second compte, le **fonds de promotion de la formation professionnelle et de
   l'apprentissage** (art. 17-18), alimenté par la taxe de formation professionnelle nette des
   ristournes : c'est lui qui finance, de 2000 à 2009, les SIVP et les contrats emploi-formation.
3. **La refonte de 2012 n'a pas remplacé les programmes de 2009.** Le décret n° 2012-2369 crée des
   « chèques » (amélioration de l'employabilité, appui à l'emploi) mais renvoie leur entrée en
   vigueur au 1er janvier 2015 et à des arrêtés ; il maintient « à titre transitoire » le SIVP, le
   CIDES, le CAIP, le CRVA et le service civil volontaire. Les rapports de suivi de l'ONEQ pour 2012
   et 2013 ne comptent aucun chèque : seulement les programmes de 2009, AMAL et le programme
   d'encouragement à l'emploi. C'est le décret n° 2019-542 qui remplace réellement ceux de 2009. Les arrêtés d'application des chèques ne sont pas identifiés (fiche proposée § 7).
4. **Séries chiffrées trouvées** (détail § 5 et § 6, annexe C) :
   - *budgétaire* : prévisions du FNE et du fonds de la formation dans les lois de finances pour
     2011 à 2020 (dix exercices, 200 à 520 MD) ; dotation du FNE et sa répartition par programme
     dans les rapports sur le budget pour 2022, 2024 et 2025 ; excédents du FNE reversés au budget
     en 2016, 2017 et 2018 (lois de règlement) ; budget du programme « Emploi » 2021-2022 (PAP) ;
   - *budgétaire relayé par la Banque centrale* : **dotations des programmes de soutien à l'emploi,
     1987 à 2008**, ligne par ligne — chantiers nationaux et régionaux, SIVP 1 et 2, FIAP, contrats
     emploi-formation, Fonds 21-21 (§ 5.3) : c'est la seule série longue trouvée ;
   - *administratif* : bénéficiaires par programme en 2009 (BCT, source ministère du
     Développement), nouveaux contrats par programme, 2010 à 2013 (ONEQ, source ANETI), neuf
     premiers mois de 2016 et 2017, premier semestre de 2023 et 2024 ;
   - *extérieur* : dépense des politiques actives 1997-2002 (Banque mondiale, 2004), budgets et
     bénéficiaires par programme en 2011 (Banque mondiale, 2015).
   **Dans ce qui a été collecté, aucune série continue ne couvre 2009-2026** : la série de la BCT
   s'arrête en 2008-2009, les prévisions des lois de finances ne se lisent fonds par fonds que de
   2011 à 2020, et les rapports annuels de l'ONEQ manquent après 2013. La dépense **exécutée** du
   FNE n'est établie pour aucune année.
5. **`data/raw/emploi/` de `tunisia-data` n'est PAS ignoré par git** (`git check-ignore` : code 1 ;
   `git status` le montre non suivi). 22 PDF (44 Mo) y sont déposés. Rien n'a été ajouté à l'index ni
   au `.gitignore` : à décider par l'humain avant tout `git add` dans ce dépôt.
6. **Ne pas refaire** : l'aide aux travailleurs licenciés pour raison économique est traitée dans
   le volume « Les prestations sociales », `_autres_risques.qmd#sec-perte-emploi` — renvoi seul. La
   taxe de formation professionnelle (taux, ristourne, compte de 2000) est traitée dans « Les
   cotisations sociales », `_prelevements_salaires.qmd#sec-cot-tfp` — renvoi seul, complété ici par
   son emploi (§ 2.3).

## 1. Les institutions

| Date | Texte | JORT | Ce qu'il établit | Niv. |
|---|---|---|---|---|
| 8 mars 1967 | loi n° 67-11 | n° 12, 10 mars 1967, pp. 388-390 (notice ; le pied de page lu par OCR porte 386 : à relire) | crée l'**Office de la formation professionnelle et de l'emploi**, établissement à caractère industriel et commercial « placé sous l'autorité du secrétaire d'État à la Jeunesse, aux Sports et aux Affaires sociales », siège à Radès ; il « assure et promeut le placement de la main-d'œuvre » (art. 4, 9°) ; les bureaux publics de placement en dépendent (art. 5) ; ses ressources comprennent « les produits de la taxe de formation professionnelle » | [T°] |
| 31 janv. 1973 | loi n° 73-8 | n° 5, 2-6 févr. 1973, p. 186 | l'office devient l'**Office des travailleurs tunisiens à l'étranger, de l'emploi et de la formation professionnelle** (OTTEEFP), sous la tutelle du ministre des Affaires sociales, siège à Tunis (art. 3 nouveau de la loi n° 67-11) | [T°] |
| 9 déc. 1983 | loi n° 83-111 | n° 81, 12 déc. 1983, pp. 3207-3208 | l'OTTEEFP est scindé en deux établissements : l'Office de la formation et de la promotion professionnelle et l'**Office de la promotion de l'emploi et des travailleurs tunisiens à l'étranger**, sous la tutelle du ministère des Affaires sociales (art. 1er) | [T°] |
| 2 juin 1988 | loi n° 88-60 (LFC 1988), art. 12 à 15 | n° 39 de 1988, p. 824 | restructuration : les attributions des deux offices de 1983 passent à l'**Office de la formation professionnelle et de l'emploi** et à l'Office des travailleurs tunisiens à l'étranger | [T°] colonnes entrelacées |
| 17 févr. 1993 | loi n° 93-11 | n° 14, 19 févr. 1993, pp. 256-257 | crée l'**Agence tunisienne de l'emploi** (ATE) et l'Agence tunisienne de la formation professionnelle, établissements à caractère industriel et commercial sous la tutelle du ministère de la Formation professionnelle et de l'Emploi (art. 1er) ; l'ATE « met en œuvre les programmes de promotion de l'emploi et d'insertion des jeunes » (art. 2, 3°) ; l'office de 1988 est dissous (art. 5) | [T°] |
| 14 juin 1993 ; 29 sept. 1997 | décrets n° 93-1354 et n° 97-1938 ; n° 97-1930 (bureaux de l'emploi) | n° 47 de 1993, pp. 887-888 ; n° 81, 10 oct. 1997, pp. 1871-1875 | organisation administrative et financière de l'ATE | [M] |
| 17 mars 2003 | décret n° 2003-564 | n° 23, 21 mars 2003, p. 589 | changement d'appellation : **Agence nationale pour l'emploi et le travail indépendant** (ANETI), bureaux de l'emploi et du travail indépendant ; seul l'intitulé est lu (le décret n° 2009-349 le vise sous cet intitulé) | [M] |
| 21 déc. 2022 | décret-loi n° 2022-78 | n° 142 de 2022, p. 4230 (pagination de la notice) ; **édition française absente de pist.tn** | complète la loi n° 93-11 ; contenu non lu | [M] |

La tutelle suit le ministère chargé de l'emploi : Affaires sociales (1973-1988 au moins), Formation
professionnelle et Emploi (1993), Emploi et Insertion professionnelle des jeunes (2007-2009, visas
du décret n° 2009-349), Formation professionnelle et Emploi (2010-2023, visas). Les décrets
d'attributions du ministère n'ont pas été lus.

## 2. Les fonds

### 2.1 Avant 2000 : trois fonds successifs

- **Fonds de l'emploi des jeunes (1981).** Loi n° 81-75 du 9 août 1981, art. 4 (JORT n° 52, 11-14
  août 1981, pp. 1869-1870) : finance les subventions de stage ; ordonnateur : le ministre des
  Affaires sociales ; gestion confiée à l'OTTEEFP ; « le montant des dotations allouées au fonds
  est fixé annuellement par la loi des finances » **[T°]**.
- **Fonds de concours des SIVP (1987).** Décret n° 87-1190 du 26 août 1987, art. 5 (JORT n° 64,
  15 sept. 1987, p. 1116) : l'indemnité de stage est servie « sur un fonds de concours institué
  auprès du ministre des affaires sociales », financé par une contribution prélevée sur le fonds
  d'intervention économique (LF 1975, art. 57) et par une contribution d'entreprises publiques
  **[T°]**. Arrêtés du 26 août 1987 (liste des entreprises publiques, même fascicule, p. 1117) et
  du 14 décembre 1987 (affectation de recettes, JORT n° 89, p. 1594) **[M]**.
- **Fonds d'insertion et d'adaptation professionnelle (FIAP).** Seule trace au JORT : la loi
  n° 91-4 du 11 février 1991 ratifiant un accord de prêt avec la BIRD « relatif au financement du
  projet d'insertion et d'adaptation professionnelle » (JORT n° 13 de 1991, p. 279) **[M]**. Le
  texte qui institue le fonds n'est pas identifié (fiche proposée § 7). Les rapports annuels de
  la BCT le nomment « Fonds d'initiation et d'adaptation professionnelle » et lui donnent une
  première dotation en 1990 (§ 5.3). La loi de finances pour
  2000 range « les programmes et instruments d'insertion et d'adaptation professionnelles » parmi
  les dépenses du nouveau fonds de la formation (art. 17).

### 2.2 Le Fonds national de l'emploi (2000)

| Texte | Article | Contenu | JORT | Niv. |
|---|---|---|---|---|
| loi n° 99-101 du 31 déc. 1999 (LF 2000) | 13 | « compte spécial du trésor intitulé "fonds national de l'emploi" » ; il finance « toutes les opérations susceptibles de développer la qualification des demandeurs d'emploi et de favoriser les possibilités d'emploi » : travaux d'intérêt public pour les non-qualifiés, emploi indépendant et cités professionnelles, programmes d'insertion des diplômés du supérieur, réadaptation ; **ordonnateur : l'ordonnateur de la présidence de la République** ; dépenses à caractère évaluatif | n° 105, 31 déc. 1999, p. 2740 | [T] |
| idem | 14 | ressources : dons et subventions des personnes physiques et morales ; ressources provenant de ses interventions ; « une partie du produit revenant à l'État et provenant des opérations de privatisation » ; autres ressources affectées | idem | [T] |
| idem | 15-16 | les dons au fonds sont déductibles de l'assiette de l'impôt sur le revenu (art. 39, § X) et de l'impôt sur les sociétés (art. 48, § VII octodecies) | pp. 2740-2741 | [T] |
| loi n° 2000-98 du 25 déc. 2000 (LF 2001) | 14 | **six taxes affectées au fonds** : contribution sur les ventes locales de café et de thé (loi n° 68-15, art. 3) ; taxe sur les contrats conclus avec les artistes étrangers (loi n° 83-113, art. 94) ; taxe sur les voyages à l'étranger (loi n° 84-2, art. 12) ; droit additionnel de première immatriculation des véhicules (loi n° 84-2, art. 22) ; contribution sur la vente du tabac, des allumettes, des cartes à jouer et de la poudre à feu (LF 1996, art. 55) ; contribution sur le tarif des services postaux (LF 1996, art. 56) | n° 104, 29 déc. 2000, p. 3172 | [T] |
| idem | 15 | récrit l'art. 57 de la LF 1996 (ressources du fonds de solidarité nationale) : les art. 55 et 56 de cette loi alimentaient jusque-là ce fonds, d'après leur intitulé à la notice | idem | [T] pour l'art. 15, [M] pour l'état antérieur |
| loi n° 2002-101 du 17 déc. 2002 (LF 2003) | 27-28 | s'y ajoutent le droit compensateur sur le ciment (décret-loi n° 73-11) et la redevance sur les ventes du ciment (loi n° 81-100, art. 105) ; l'art. 57 de la LF 1996 est abrogé | n° 102, 17 déc. 2002, p. 2879 | [T] |
| décret n° 2000-2279 du 10 oct. 2000 | 1er | couverture sociale des stagiaires (loi n° 88-6) étendue aux bénéficiaires des « programmes du fonds national de l'emploi 21-21 » — seule occurrence de « 21-21 » dans un intitulé du JORT | n° 83, 17 oct. 2000, pp. 2471-2472 | [T] |
| loi n° 2010-58 (LF 2011) | 28 | les primes servies par le fonds aux bénéficiaires ne sont pas soumises à l'impôt sur le revenu (art. 38, 21°) ni, pour les entreprises, comprises dans le résultat (art. 11) — lecture partielle | n° 102, 21 déc. 2010, p. 3467 | [T] partiel |
| décret-loi n° 2011-16 du 26 mars 2011 | 1er | **« le ministre chargé de l'emploi est l'ordonnateur du fonds national de l'emploi »** (art. 13, § 3 de la LF 2000) | n° 21, 29 mars 2011, p. 381 | [T] |

**Depuis 2022, les lois de finances imputent des lignes de crédit sur les ressources du fonds**,
gérées par la Banque tunisienne de solidarité ou une autre banque : 25 MD et 30 MD (LF 2022) ;
20 MD supplémentaires à la BTS (LF 2023, art. 18), plus 10 MD et 20 MD ; 20 MD pour les
catégories vulnérables (LF 2024, art. 19) et 10 MD ; 20 MD (LF 2025, art. 21), 5 MD pour les
personnes handicapées (art. 22) ; 15 MD (LF 2026, art. 23) et 35 MD supplémentaires pour les
sociétés communautaires (art. 24), sous le titre « élargissement des interventions du Fonds national
de l'emploi » **[T-ar] relevé au fil du texte : articles et montants à relire un par un avant
emploi** (JORT n° 119/2021, n° 141/2022, n° 144/2023, n° 149/2024, n° 148/2025).

### 2.3 Le fonds de la formation et la taxe de formation professionnelle

LF 2000, art. 17-18 (JORT n° 105 de 1999, p. 2741) **[T]** : compte spécial « fonds de promotion de
la formation professionnelle et de l'apprentissage », ordonnateur le ministre chargé de la
formation professionnelle ; ressource : « le produit de la taxe de formation professionnelle net
des ristournes ». Ses dépenses comprennent, outre la formation initiale et continue, **« les
programmes et instruments d'insertion et d'adaptation professionnelles », « les programmes de
stages d'initiation à la vie professionnelle » et « les contrats emploi-formation »**. La LF 2003,
art. 12, modifie le deuxième paragraphe de cet article **[M]**. Conséquence pour le chapitre : de
2000 à 2009, les SIVP relèvent de ce fonds et non du FNE ; le décret n° 2009-349 les fait passer au
FNE (art. 1er), avec une tolérance d'imputation sur le titre II jusqu'au 31 décembre 2009 (art. 43).
Deux règles de non-cumul lient la ristourne aux stages : l'employeur ne peut demander la ristourne
au titre des SIVP (décrets n° 87-1190, art. 8 ; n° 88-715, art. 7 ; n° 93-1049, art. 17) ni la
cumuler avec la subvention du contrat emploi-formation (décret n° 81-1220, art. 16) **[T°]**.

## 3. Les programmes

### 3.1 Tableau chronologique « texte — article — avant → après — date d'effet »

| Texte | JORT (éd. fr.) | Article | Avant → après | Effet | Niv. |
|---|---|---|---|---|---|
| loi n° 81-75 du 9 août 1981 | n° 52, 11-14 août 1981, pp. 1869-1870 | 1er, 4 | néant → subvention de l'État pendant un stage d'un an ; exonération de la part patronale des cotisations pendant le stage et **trois ans** après (un an pour l'apprenti recruté) ; fonds de l'emploi des jeunes | sans clause | [T°] |
| décret n° 81-1220 du 24 sept. 1981 | n° 59, 25-29 sept. 1981, pp. 2245-2247 | 2, 7, 11, 13, 17-18 | contrat de stage d'adaptation professionnelle (dit contrat emploi-formation, arrêté du 23 avril 1982) : jeunes de 17 à 25 ans diplômés du secondaire technique ou de la formation professionnelle, premier emploi ; un an ; l'entreprise verse le salaire entier ; **subvention de 500 D** en trois tranches (150 + 150 + 200 après six mois d'emploi permanent) | sans clause | [T°] |
| décret n° 87-1190 du 26 août 1987 | n° 64, 15 sept. 1987, p. 1116 | 1er, 3, 4 | néant → **SIVP des diplômés du supérieur** : un an, deux au plus ; **bourse de 100 à 250 D par mois**, plafonnée à la moitié du salaire de base de l'emploi correspondant dans l'administration ; entreprises, administrations, collectivités | sans clause | [T°] |
| décret n° 88-715 du 31 mars 1988 | n° 24, 12 avril 1988, pp. 550-551 | 1er, 3, 4 | néant → **SIVP des diplômés du second cycle secondaire** (dit SIVP 2) : un an au plus ; **bourse de 50 à 80 D par mois** ; couverture sociale de la loi n° 88-6 | sans clause | [T°] |
| décret n° 88-733 du 7 avril 1988 | n° 25, 15 avril 1988, pp. 565-566 | 6 à 9 | remplace le décret de 1981 : stage d'un an au plus ; renouvellement si l'entreprise recrute 25 % des stagiaires de l'année précédente (50 % en 1981) ; subvention de 500 D en deux tranches (suite non lue) | sans clause | [T°] partiel |
| loi n° 93-17 du 22 févr. 1993 | n° 16, 26 févr. 1993, p. 300 | 1er nouveau, 1 bis | exonération de trois ans après le stage → exonération pendant le stage, puis **deux ans** après un contrat emploi-formation, **un an** après un SIVP (pour les diplômés du supérieur : spécialités difficiles ou premier diplômé recruté par l'entreprise), un an pour l'apprenti ; l'indemnité complémentaire versée par l'entreprise échappe aux cotisations et à l'impôt sur le revenu ; l'art. 48 de la LF 1987 est abrogé | sans clause | [T°] |
| décret n° 93-1049 du 3 mai 1993 | n° 36, 14 mai 1993, pp. 661-663 | 2, 4, 12, 20, 21, 25, 28 | refonte en trois catégories gérées par l'ATE : contrat emploi-formation (subvention d'adaptation **300 D** + subvention d'embauche **200 D** ; l'employeur verse une bourse des deux tiers du SMIG) ; SIVP des niveaux secondaire et premier cycle (**60 à 80 D** par mois) ; SIVP des diplômés du supérieur (**100 à 250 D** par mois) ; durée d'un an, prorogeable d'un an pour les spécialités difficiles (art. 29) | sans clause | [T°] |
| décret n° 98-1120 du 18 mai 1998 | n° 42, 26 mai 1998, p. 1158 | 5, 10 nouveaux | commission nationale → commission permanente des programmes d'insertion ; taux minimum d'insertion fixé par arrêté, l'insertion pouvant se faire dans une autre entreprise ou à son compte | sans clause | [T] |
| loi n° 2004-90 (LF 2005) | n° 105, 31 déc. 2004, pp. 3433-3434 | 20 (art. 43 bis du code d'incitation aux investissements) | **prise en charge par l'État de la contribution patronale** pour le recrutement de diplômés du supérieur (bac + 2 au moins), sur sept ans : 100 % les deux premières années, 85 %, 70 %, 55 %, 40 %, 25 % | recrutements du 1er janvier 2005 au 31 décembre 2009 | [T] |
| loi n° 2005-91 du 3 oct. 2005 | n° 79, 4 oct. 2005, p. 2590 | 1er | néant → l'État prend en charge pendant un an **50 % du salaire** du diplômé du supérieur recruté par le secteur privé, **dans la limite de 250 D par mois** | sans clause relevée | [T] |
| décret n° 2009-349 du 9 févr. 2009 | n° 12, 10 févr. 2009, pp. 477-482 | 1er, 8, 13-15, 23, 27, 34, 38, 44 | décret n° 93-1049 **abrogé** → six programmes du FNE : SIVP, CIDES, CAIP, CRVA, PAPPE, contrat emploi-solidarité (paramètres § 3.2) | sans clause relevée | [T] |
| arrêté du 19 mars 2009 | n° 25, 27 mars 2009, pp. 897-898 | — | indemnité complémentaire minimale due par l'entreprise : SIVP 150 D, CIDES 150 D, CAIP 50 D, CRVA 50 D par mois | — | [T] |
| décret n° 2009-1026 du 13 avril 2009 | n° 31, 17 avril 2009, pp. 1059-1060 | 3, 4, 11 | SIVP dans le secteur public : 150 D par mois de l'ANETI ; les contrats en cours sont portés à 150 D | — | [T] |
| décret n° 2009-1052 du 13 avril 2009 | n° 31, 17 avril 2009, pp. 1069-1070 | 42 bis à quinquies | mesure de crise : le FNE prend en charge **50 % de la contribution patronale** pour les salariés des entreprises totalement exportatrices dont l'horaire est réduit d'au moins huit heures par semaine, et la totalité pour le chômage technique | — | [T] |
| loi n° 2009-71 (LF 2010) | n° 102, 22 déc. 2009, p. 3914 (notice) | 19 | la loi n° 2005-91 est **abrogée** | 1er janvier 2010 [D] | [T] |
| décret n° 2010-87 du 20 janv. 2010 | n° 7, 22 janv. 2010, pp. 228-232 | 40 bis à quinquies | néant → **service civil volontaire** : diplômés du supérieur primo-demandeurs, stage à mi-temps de douze mois dans une association, **150 D par mois** ; jusqu'à 60 % du transport urbain | sans clause | [T] |
| décret n° 2011-1 du 3 janv. 2011 | n° 1, 4 janv. 2011, pp. 34-35 | 19 bis à quater (ajoutés) | s'ajoute au CIDES une seconde voie : diplômés au chômage depuis **deux ans** au moins, contrat d'un an (art. 19 bis ; suite des articles ajoutés non lue) | — | [T] |
| décret n° 2011-98 du 11 janv. 2011 | n° 4, 14 janv. 2011, pp. 113-114 | 6, 38, 39, 40 ter | SIVP : dix-huit mois au plus → **deux ans** ; contrat emploi-solidarité des diplômés : trois → quatre ans ; service civil prorogeable d'un an | — | [T] |
| décret n° 2011-621 du 23 mai 2011 | n° 38, 27 mai 2011, pp. 799-800 | 23, 34, 40 quinquies, 40 sexies à octies ; 6 | CAIP **80 → 100 D** ; PAPPE **150 → 200 D** (diplômés) et **80 → 100 D** ; service civil **150 → 200 D**, plus à mi-temps ; néant → **programme de recherche active d'emploi (AMAL)** : **200 D** par mois (diplômés du supérieur, BTS) ou **100 D**, un an au plus ; prime de projet jusqu'à 2 400 D ou 1 200 D ; SIVP ouvert sans délai de six mois après le diplôme | **1er mars 2011** (art. 6) | [T] |
| décret n° 2011-2484 du 29 sept. 2011 | n° 75, 4 oct. 2011, p. 2011 (pied de page lu, à confirmer) | 42 bis, 42 ter | primes aux projets pilotes public-privé ; dépenses de communication imputées au FNE | — | [T] |
| décret n° 2012-953 du 2 août 2012 | n° 61, 3 août 2012, pp. 1799-1803 | 40 nonies à quindecies ; 2 | AMAL **abrogé à compter du 1er janvier 2012** → **programme d'encouragement à l'emploi** : diplômés depuis deux ans au moins, âgés de 28 ans au moins, inscrits depuis un an ; **200 D** par mois le premier semestre, **150 D** le second (150 puis 100 D pour les anciens d'AMAL) ; prime de 600 D en cas de recrutement ; exclusion des familles dont le revenu dépasse trois fois le SMIG ; fin au 31 décembre 2013 | 1er janvier 2012 pour l'abrogation | [T] |
| décret n° 2012-2369 du 16 oct. 2012 | n° 82, 16 oct. 2012, pp. 2531-2542 | 1er, 5, 10, 34-36, 40, 41 | décret n° 2009-349 abrogé « sauf » : chèque d'amélioration de l'employabilité (**200 D** ou **100 D** par mois, vingt-quatre mois au plus), chèque d'appui à l'emploi (jusqu'à 50 % du salaire et contribution patronale, un an), appui aux promoteurs, partenariat avec les régions ; **les sections 1, 2, 3, 4 et 7 du décret de 2009 demeurent en vigueur à titre transitoire** | chèque d'appui et partenariat : 1er janvier 2015 (art. 40) | [T] |
| décret n° 2013-3766 du 18 sept. 2013 | n° 77, 24 sept. 2013, pp. 2784-2788 | 40 et 41 nouveaux ; 4 | le chèque d'amélioration de l'employabilité est lui aussi reporté au **1er janvier 2015** ; les programmes de 2009 (sections 1, 2, 3, 4, 6 et 7) restent en vigueur jusqu'à la fin de l'expérimentation et aux arrêtés ; âge du programme d'encouragement : 28 → 26 ans | — | [T] |
| décret n° 2014-2901 du 30 juill. 2014 | n° 65, 12 août 2014, pp. 2049-2051 | 12, 42 | petites entreprises aidées : investissement de 150 000 D au plus ; contrats emploi-solidarité associatifs prorogés d'un an | — | [T] |
| décret gouv. n° 2016-445 du 31 mars 2016 | n° 28, 5 avril 2016, pp. 1170-1171 | 42, § 4 | nouvelle prorogation d'un an des contrats emploi-solidarité associatifs | — | [T] |
| décret gouv. n° 2016-904 du 27 juill. 2016 | n° 63, 2 août 2016, pp. 2405-2407 | 23 bis à octies | néant → **programme « FORSATI »** : accompagnement de douze mois, prorogeable de six ; indemnité mensuelle (100 D puis 150 D selon le semestre, lecture à confirmer : colonnes entrelacées) et 50 D de déplacement ; prime d'insertion | — | [T] à relire |
| décret gouv. n° 2017-358 du 9 mars 2017 | n° 21, 14 mars 2017, pp. 996-998 (d'après l'entrée existante `decret2017-358`) | 26 quater à decies | néant → **« contrat-dignité »** : diplômés du supérieur primo-demandeurs, au chômage depuis deux ans au moins ; le FNE prend en charge pendant deux ans **400 D par mois** du salaire, la quote-part patronale et la quote-part salariale de sécurité sociale dans la limite d'un salaire de 600 D ; salaire minimal de 600 D | — | [T] |
| arrêté du 8 août 2017 | n° 65 de 2017 | — | critères du bénéfice du contrat-dignité ; non lu | — | [M] |
| décret gouv. n° 2019-542 du 28 mai 2019 | n° 51, 25 juin 2019, pp. 2081-2091 de l'**édition arabe** ; édition française absente | 2, 6, 7, 9, 13, 20, 61, 62 | décret n° 2012-2369 **abrogé** → cinq programmes : contrat d'initiation à la vie professionnelle (CIVP), contrat-dignité, contrat de service civil, FORSATI, appui aux promoteurs (paramètres § 3.2) ; les stages SIVP et CIDES en cours passent à **200 D**, les CAIP à **150 D** | entrée en vigueur du décret ; nouveaux programmes au plus tard trois mois après (art. 61) | [T-ar] |
| décret n° 2023-461 du 5 juin 2023 | n° 60, 9 juin 2023, p. 1552 (notice) et suivantes, jusqu'à la p. 1554 au moins | 11, 31, 41, 43 nouveaux | CIVP : nouvel accueil subordonné à l'insertion de 50 % des sortants des trois dernières années, délai de carence ramené à un an ; appui étendu aux entreprises de l'économie sociale et solidaire et aux **sociétés communautaires** (investissement jusqu'à 300 000 D ; bourse de 20 000 D jusqu'au 31 décembre 2025 ; 200 D par mois et par membre pendant douze mois) | — | [T] partiel |

**Dates d'effet dérivées [D]** pour les textes « sans clause » du tableau. Règle : avant la loi
n° 93-64, un jour franc après la publication (date du fascicule + 2 jours) ; ensuite, cinq jours
après le dépôt du fascicule au siège du gouvernorat de Tunis, jour du dépôt non compté (dépôt + 5,
convention des notes existantes). Dépôt lu au dernier feuillet du fascicule français.

| Texte | Publication ou dépôt | Exécutoire [D] |
|---|---|---|
| loi n° 81-75 ; décret n° 81-1220 | fascicules datés de plusieurs jours (11-14 août et 25-29 sept. 1981) | non dérivée : jour de parution à établir |
| décret n° 87-1190 | publié le 15 sept. 1987 | 17 sept. 1987 |
| décret n° 88-715 | publié le 12 avril 1988 | 14 avril 1988 |
| décret n° 88-733 | publié le 15 avril 1988 | 17 avril 1988 |
| loi n° 93-17 | publiée le 26 févr. 1993 | 28 févr. 1993 |
| décret n° 93-1049 | publié le 14 mai 1993 | 16 mai 1993 |
| décret n° 98-1120 | dépôt le 27 mai 1998 | 1er juin 1998 |
| loi n° 2005-91 | dépôt le 5 oct. 2005 | 10 oct. 2005 |
| décret n° 2009-349 | dépôt le 11 févr. 2009 | 16 févr. 2009 |
| arrêté du 19 mars 2009 | dépôt le 28 mars 2009 | 2 avril 2009 |
| décrets n° 2009-1026 et 2009-1052 | dépôt le 18 avril 2009 | 23 avril 2009 |
| décret n° 2010-87 | dépôt le 23 janv. 2010 | 28 janv. 2010 |
| décret n° 2011-1 | dépôt le 5 janv. 2011 | 10 janv. 2011 |
| décret n° 2011-98 | dépôt le 15 janv. 2011 | 20 janv. 2011 |
| décret n° 2011-2484 | dépôt le 5 oct. 2011 | 10 oct. 2011 |
| décret n° 2012-2369 | dépôt le 17 oct. 2012 | 22 oct. 2012 |
| décret n° 2013-3766 | dépôt le 25 sept. 2013 | 30 sept. 2013 |
| décret n° 2014-2901 | dépôt le 15 août 2014 | 20 août 2014 |
| décret gouv. n° 2016-445 | dépôt le 6 avril 2016 | 11 avril 2016 |
| décret gouv. n° 2016-904 | dépôt le 3 août 2016 | 8 août 2016 |
| décret gouv. n° 2017-358 | dépôt le 15 mars 2017 | 20 mars 2017 |
| décret gouv. n° 2021-436 | dépôt le 18 juin 2021 | 23 juin 2021 |
| décret n° 2023-461 | dépôt le 9 juin 2023 | 14 juin 2023 |
| décret gouv. n° 2019-542 ; lois de finances | dépôt non relevé (édition arabe) ; les lois de finances valent au 1er janvier | — |

### 3.2 Les programmes et leurs paramètres dans le temps

Indemnité mensuelle versée par l'État (fonds ou agence), hors complément de l'entreprise.

| Programme | Public | Durée | Indemnité de l'État, par mois | Cotisations | Textes |
|---|---|---|---|---|---|
| **Contrat emploi-formation** (1981-2009) | 17-25 ans, secondaire technique ou formation professionnelle | 1 an | à l'entreprise : 500 D (1981, 1988) → 300 D + 200 D d'embauche (1993) | part patronale exonérée pendant le stage et 3 ans après (1981) → 2 ans après (1993) | 81-75, 81-1220, 88-733, 93-17, 93-1049 |
| **SIVP des diplômés du supérieur** (« SIVP 1 ») | diplômés du supérieur, premier emploi | 1 an, 2 au plus (1987) → 1 an, 18 mois au plus (2009) → 2 ans (janv. 2011) | 100 à 250 D (1987, 1993) → **150 D** (2009) → **200 D** (2019, contrats en cours) | couverture des stagiaires (loi n° 88-6) ; exonération patronale 1 an après recrutement sous conditions (1993) | 87-1190, 93-1049, 2009-349, 2011-98, 2019-542 |
| **SIVP du secondaire** (« SIVP 2 ») | second cycle secondaire, premier cycle du supérieur | 1 an | 50 à 80 D (1988) → 60 à 80 D (1993) ; disparaît en 2009 | idem | 88-715, 93-1049 |
| **CIDES** (2009) | diplômés du supérieur au chômage depuis plus de 3 ans ; seconde voie à 2 ans ajoutée en 2011 | 1 an | 150 D (+ 50 D hors gouvernorat) ; prime de recrutement de 1 000 D à l'entreprise | **contribution patronale prise en charge par le FNE sur 7 ans** (100 %, 100 %, 85 %, 70 %, 55 %, 40 %, 25 %) pour les recrutements de 2009 à 2011 | 2009-349, art. 11-19 ; 2011-1 |
| **CAIP** (2009) | non-diplômés du supérieur, sur offre non satisfaite | 1 an | **80 D** (2009) → **100 D** (mars 2011) → **150 D** (2019) ; formation jusqu'à 400 h | — | 2009-349, art. 20-24 ; 2011-621 ; 2019-542 |
| **CRVA** (2009) | licenciés économiques, permanents ou ayant 3 ans d'ancienneté | 1 an | **200 D** ; adaptation jusqu'à 200 h | — | 2009-349, art. 25-28 |
| **Contrat emploi-solidarité** (2009) | tous demandeurs, initiatives régionales | 3 ans (diplômés) → 4 ans (2011) ; 1 an (autres) | 150 à 250 D (diplômés) ; 130 D au plus (autres) | — | 2009-349, art. 36-40 ; 2011-98 |
| **Service civil volontaire** (2010) → contrat de service civil (2019) | diplômés du supérieur primo-demandeurs, en association | 12 mois | **150 D** (2010) → **200 D** (mars 2011) ; 200 D (2019) | contribution patronale pour l'association qui recrute (2019, art. 22, non lu en détail) | 2010-87, 2011-621, 2019-542 |
| **AMAL** — recherche active d'emploi (2011) | diplômés du supérieur et BTS ; autres niveaux | 1 an | **200 D** ; 100 D | — | 2011-621 ; abrogé au 1er janv. 2012 par 2012-953 |
| **Programme d'encouragement à l'emploi** (2012-2013) | diplômés depuis 2 ans, 28 ans puis 26 ans | 1 an | 200 D puis 150 D par semestre | — | 2012-953, 2012-2369 (art. 27-33), 2013-3766 |
| **Chèque d'amélioration de l'employabilité** (2012) | demandeurs d'emploi inscrits | 24 mois au plus | 200 D ; 100 D | — | 2012-2369, art. 3-6 ; **arrêté d'application non identifié** |
| **FORSATI** (2016) | demandeurs d'emploi, parcours accompagné | 12 mois (+ 6) | 100 D puis 150 D (à relire) + 50 D de déplacement ; 2019 : montants non relevés | — | 2016-904 ; 2019-542, art. 25-30 |
| **Contrat-dignité (Karama)** (2017) | diplômés du supérieur primo-demandeurs, 2 ans de chômage | 2 ans | **400 D** du salaire (2017) → **moitié du salaire net, 400 D au plus** (2019) ; salaire d'au moins 600 D | parts patronale et salariale prises en charge, salaire plafonné à 600 D | 2017-358 ; 2019-542, art. 12-16 |
| **CIVP** (2019) | primo-demandeurs ; non-diplômés et handicapés sans cette condition | 12 mois, renouvelable 1 an | **200 D** (diplômés du supérieur) ; **150 D** (autres) ; + 50 D (handicap) | contribution patronale prise en charge 2 ans pour le diplômé recruté en contrat à durée indéterminée, sous plafond fixé par arrêté | 2019-542, art. 5-11 ; 2023-461 |
| **Prise en charge des cotisations patronales** hors programme | recrutement de diplômés du supérieur | 7 ans dégressifs | — | 100 % → 25 % ; recrutements 2005-2009 (code d'incitation, art. 43 bis) | LF 2005, art. 20 ; décrets n° 98-868, 2002-13 [M] |
| **Prise en charge du salaire** hors programme | diplômés du supérieur, secteur privé | 1 an | 50 % du salaire, 250 D au plus | — | loi n° 2005-91 (abrogée par LF 2010, art. 19) ; reprise transitoire jusqu'au 31 déc. 2014 dans 2012-2369, art. 34-35 |

**Chantiers.** Les « chantiers d'assistance » aux chômeurs précèdent l'indépendance (décret du
9 décembre 1954, prorogé par semestre de 1956 à 1960 ; « chantiers de lutte contre le
sous-développement » dans la loi n° 60-16) **[M]**. Aucun texte fondateur des chantiers régionaux
n'apparaît aux intitulés du JORT (fiche proposée § 7). Leur extinction est organisée par le décret
gouvernemental n° 2021-436 du 17 juin 2021 (JORT n° 52, 18 juin 2021, p. 1546) : les ouvriers en
exercice continu au 20 octobre 2020 sont intégrés dans la fonction publique, autorisés à continuer
jusqu'à 60 ans (plus de 55 ans) ou sortent avec une allocation égale au transfert monétaire de base
(60 ans et plus) (art. 4) **[T] partiel** ; modifié par le décret n° 2025-459 du 19 novembre 2025
(JORT n° 138, p. 3138) **[M]**. Le rapport sur le budget pour 2025 inscrit 30 MD pour environ
1 500 « chèques de départ » d'ouvriers de chantiers (§ 5.1).

**Erreurs de `jort_cache.db` relevées** : le décret du 7 avril 1988 porte le n° **88-733** au
fascicule (et au visa du décret n° 93-1049), 88-773 à la notice ; le décret n° 2023-461 a pour
`numero` « 2023-060 » ; l'arrêté du 15 juin 1995 d'application du décret n° 93-1049 porte ce numéro
d'emprunt ; les décrets n° 2011-2484, 2017-358 et l'arrêté du 8 août 2017 n'ont ni pages ni
intitulé français.

## 4. Renvois (ne pas refaire)

- **Perte d'emploi pour raison économique** : « Les prestations sociales »,
  `_autres_risques.qmd#sec-perte-emploi` (loi n° 96-101 ; fonds d'assurance de la LF 2025, art. 17).
  Le CRVA (§ 3.2) en est le pendant « actif » : même public, mais un stage indemnisé à 200 D.
- **Taxe de formation professionnelle** : « Les cotisations sociales »,
  `_prelevements_salaires.qmd#sec-cot-tfp` ; clés existantes `loi66-79-lf1967`,
  `decret-1956-01-12-formation-professionnelle`. Son TODO sur la série des prévisions du fonds de
  la formation est en partie levé par le § 5.1 ci-dessous (colonne « fonds de la formation »).
- **Cotisations patronales prises en charge par l'État** : aucun chapitre du volume « Les
  cotisations sociales » ne les traite (recherche de « prise en charge par l'État », « 43 bis » et
  « diplômés de l'enseignement supérieur » dans ses `.qmd` : aucune occurrence). Le chapitre des
  politiques de l'emploi peut donc les porter, ou les signaler au volume des cotisations.

## 5. Chiffres budgétaires et administratifs tunisiens

### 5.1 Budgétaire

**a) Prévisions inscrites aux lois de finances, tableau des comptes spéciaux du Trésor** (recettes
prévues, égales aux dépenses autorisées ; millions de dinars). Relevé sur la couche texte du
fascicule. Ce sont des **prévisions**, non des réalisations.

| Loi de finances pour | Fonds national de l'emploi | Fonds de promotion de la formation et de l'apprentissage | Fascicule lu |
|---|---:|---:|---|
| 2011 | 200 | 60 | JORT n° 102, 21 déc. 2010, p. 3481 (éd. fr.) |
| 2012 | 420 | 60 | n° 1, 3 janv. 2012 (loi n° 2011-7), p. 16 env. |
| 2013 | 520 | 60 | n° 1, 1er janvier 2013 (loi n° 2012-27), p. 33 env. |
| 2014 | 350 | 50 | n° 105 de 2013 (loi n° 2013-54), p. 3704 env. |
| 2015 | 330 | 50 | n° 105 de 2014 (loi n° 2014-59), p. 3478 env. |
| 2016 | 330 | non relevé | n° 104 de 2015, éd. arabe |
| 2017 | 330 | 37 | n° 105 de 2016 (loi n° 2016-78), p. 3856 env. |
| 2018 | 300 | 25 | n° 101 de 2017 (loi n° 2017-66), p. 4297 env. ; éd. fr. et ar. concordantes |
| 2019 | 450 | 40 | n° 104 de 2018, éd. arabe |
| 2020 | 420 | 70 | n° 104 de 2019, éd. arabe, p. 4717 env. |

Avant la LF 2011, le fascicule de la loi de finances ne porte pas de ligne par fonds dans sa couche
texte (LF 2000 à 2010 parcourues ; tableaux non relus à l'image). Pour les LF 2021 à 2026, la
ligne est absente de la couche texte des fascicules parcourus (non vérifié à l'image). « env. » :
page du pied de page qui suit la ligne, à une page près ; 2016 et 2019 : page non relevée.

**b) Rapports sur le budget de l'État (ministère des Finances), dotation du FNE et répartition.**
PDF déjà présents dans `tunisia-data/data/raw/banque-mondiale-rapports/` (`minfin_2021-12_…2022_ar`,
`minfin_2023-10_…2024_ar`, `minfin_2025_annexe1_…2025_ar`), édition arabe, lus sur couche texte.

| Exercice | FNE | Postes cités par le rapport (« notamment ») | Page du PDF |
|---|---:|---|---|
| 2022 | 420 MD | contrat-dignité 140 MD pour 25 000 diplômés ; CIVP « nouvelle formule » 175 MD ; microprojets par la BTS 70 MD ; « nouvelle génération de promoteurs » 25 MD ; accompagnement et économie sociale et solidaire 15 MD ; économie numérique 2 MD | pp. 115-116 |
| 2024 | 420,5 MD | CIVP 191 MD pour 104 000 contrats ; contrat-dignité 63,5 MD pour 6 800 diplômés ; service civil 24,7 MD pour 11 000 bénéficiaires ; économie numérique 12,5 MD ; accompagnement des promoteurs 15 MD ; BTS 60 MD ; économie sociale et solidaire 10 MD ; nouvelle génération 25 MD | pp. 159-160 |
| 2025 | 420,5 MD (295,5 MD « emploi » + 125 MD « initiative privée ») | CIVP 180 MD (104 000 contrats en cours, environ 98 000 nouveaux) ; appui au recrutement des diplômés 41 MD (environ 6 000 nouveaux, 6 800 en cours) ; service civil 20 MD (10 000 nouveaux) ; jeunes pousses 10 MD ; **chèque de départ des ouvriers de chantiers 30 MD pour environ 1 500 chèques** | pp. 165-167 |

Ces postes ne sont pas une décomposition : ceux de 2022 totalisent 427 MD pour une dotation de
420 MD. Budget de développement de la mission « emploi et formation professionnelle » d'après les mêmes
rapports : environ 515 MD (2022), 507,2 MD (2024), 489 MD (2025). Les rapports pour 2012 à 2021,
2023 et 2026 ne sont pas dans l'entrepôt.

**c) Projet annuel de performance de la mission (GBO).** PAP 2022, éd. française, tableau de
répartition par programme (crédits de paiement, milliers de dinars) : programme « Emploi » 387 187
(2021) et 385 727 (2022), dont interventions 314 325 et 314 825 ; programme « Entrepreneuriat »
124 221 et 125 200 ; mission entière 967 500 et 980 000. PAP 2024 et 2025 (éd. arabe) récupérés,
tableaux non dépouillés (mise en page arabe à relire à l'image).

**d) Lois de règlement : excédents du FNE reversés au titre I du budget.** L'article 5 de chaque
loi liste, fonds par fonds, les « excédents transférés au budget ».

| Gestion | Excédent du FNE transféré | Texte | JORT |
|---|---:|---|---|
| 2016 | 324 090 755,028 D | loi n° 2018-49 du 9 août 2018 (tableau lu en arabe ; intitulé de la colonne à confirmer) | n° 70 de 2018, éd. arabe |
| 2017 | 266 423 326,873 D | loi n° 2024-18 du 5 mars 2024, art. 5 | n° 35, 7 mars 2024, p. 801 env. |
| 2018 | 244 746 214,082 D | loi n° 2024-19 du 5 mars 2024, art. 5 | n° 35, 7 mars 2024 |

Ce sont des transferts de soldes accumulés : ils ne mesurent pas la dépense de l'année ni un taux
d'exécution, qui supposeraient les recettes et les dépenses réelles du fonds, non relevées. Une ligne « 256 580 000 » figure pour le
FNE dans le fascicule n° 55 de 2018 (lois de règlement 2013 à 2015) : gestion et nature non
identifiées. Les lois de règlement de 2019 et 2020 ne portent pas ce tableau dans leur couche
texte. Les tableaux annexes (n° 2-1 et 2-2, dépenses par chapitre) sont des images : le chapitre
du ministère de la formation professionnelle et de l'emploi y est lisible, non relevé.

### 5.2 Administratif (ANETI, ONEQ)

Source : Observatoire national de l'emploi et des qualifications (ONEQ), ministère de la Formation
professionnelle et de l'Emploi, « Rapport annuel de suivi des programmes actifs d'emploi », année
2012 (mai 2013) et année 2013 ; données de l'ANETI. Unité : nouveaux contrats signés dans l'année.

| | 2010 | 2011 | 2012 | 2013 |
|---|---:|---:|---:|---:|
| Nouveaux contrats, total imprimé (périmètre variable, voir ci-dessous) | 120 305 | 112 299 | 135 616 | 170 424 |
| Bénéficiaires en cours en fin d'année | 70 537 | 72 002 | 96 425 | 94 989 |
| Sortants | 95 549 | 107 696 | 106 246 | 148 681 |
| SIVP | 45 245 | 45 018 | 55 723 | 62 924 |
| CIDES | 3 996 | 1 018 | 276 | 100 |
| Service civil volontaire | 5 901 | 6 719 | 18 120 | 22 688 |
| CAIP | 34 954 | 37 629 | 40 458 | 36 645 |
| CRVA | 750 | 621 | 359 | 451 |
| AMAL (« SYRAE ») | — | 203 133 | 17 550 | 0 |
| Programme d'encouragement à l'emploi | — | 0 | 21 050 | 37 267 |
| « PC50 » (prise en charge de 50 % du salaire) | n. r. | 248 | 303 | 214 |

Rapport 2012 : tableaux 1, 2 et 4 (tableau 1 : p. 5 ; pages des deux autres non relevées) ;
rapport 2013 : tableaux 1, 2 et 4 (pp. 7, 8 et 17). Le total « diplômés du supérieur » de 2011 imprimé au rapport 2013 (256 136)
inclut AMAL ; celui du rapport 2012 (52 755) l'exclut : ne pas les chaîner. **Le total de la
première ligne change de périmètre** : en 2010-2012 il exclut AMAL et le programme d'encouragement
à l'emploi (74 119 + 40 817 + environ 10 % d'aide au travail indépendant ≈ 135 600 en 2012) ; en
2013 il inclut le programme d'encouragement (les 123 193 contrats de diplômés font 72 % de 170 424).
La hausse de 25,7 % imprimée entre 2012 et 2013 tient donc pour l'essentiel à ce changement : ne pas
la reprendre. **AMAL en 2011 a trois mesures qui ne se chaînent pas** : 203 133 nouveaux contrats
(rapport ONEQ sur 2013), 188 497 bénéficiaires cumulés en décembre 2011 (rapport ONEQ de février
2012), 155 000 bénéficiaires en octobre 2011 (Banque mondiale, § 6.1). Les mêmes rapports
donnent le taux de résiliation (35,2 % des contrats terminés en 2012, 30 % en 2011, 29,1 % en
2010) et un taux d'insertion de 41,9 % dix-huit mois en moyenne après la sortie (fin 2012).

Points plus récents, périodes partielles (notes de conjoncture de l'ONEQ, source ANETI) :

| Période | SIVP / CIVP | CAIP | Service civil | FORSATI | Contrat-dignité | Total |
|---|---:|---:|---:|---:|---:|---:|
| janv.-sept. 2016 | 43 435 | 23 461 | 19 382 | 0 | 0 | 97 661 |
| janv.-sept. 2017 | 39 230 | 27 162 | 16 915 | 26 548 | 9 999 | 130 139 |
| 1er semestre 2023 | 50 500 | — | 5 292 | — | 2 660 | 58 452 (emploi salarié) |
| 1er semestre 2024 | 43 718 | — | 4 136 | — | 2 050 | 49 904 |

(Note du 3e trimestre 2017, tableau n° 4, p. 11 ; note du 3e trimestre 2024, pp. 2 et 4. En
2023-2024 la colonne « contrat-dignité » porte la ligne « contrats d'appui au recrutement des
diplômés de l'enseignement supérieur » : rapprochement **[D]**, fondé sur les 6 800 contrats du
contrat-dignité au rapport sur le budget 2024, repris comme 6 800 contrats « en cours » du
programme d'appui au recrutement au rapport 2025.)

Cumuls donnés par des rapports de l'ONEQ : AMAL, 188 497 bénéficiaires cumulés et 144 313 en cours
en décembre 2011 (rapport d'évaluation de février 2012, tableau 1) ; contrat-dignité, environ
48 000 bénéficiaires de 2017 à fin 2021, soit 17 000 contrats par an les deux premières années et
près de 6 000 les deux dernières ; contrat de service civil, 70 000 bénéficiaires de 2018 à 2021,
de 20 000 (2018) à 12 000 (2021) (étude ONEQ-OIT de novembre 2023, partie I ; page non relevée).

**Absent de ce qui a été collecté** : bénéficiaires par programme en série avant 2009 (les
rapports de la BCT en donnent en prose, année par année, non dépouillés) ; années entières 2014 à
2022 ; dépense exécutée par programme après 2008.

### 5.3 La série longue : rapports annuels de la Banque centrale, 1987-2008 (relais)

Source : BCT, *Rapport annuel*, tableau « Programmes de soutien à l'emploi » (titre de l'édition
2008, pp. 111-112 ; le tableau figure dans les éditions 1991 à 1996, 1998, 1999 et 2001 à 2008), déjà
dans l'entrepôt (`data/raw/bct-archives/109/`). **La BCT est un relais** : elle cite la direction
générale des ressources humaines du ministère du Plan et du Développement régional (1991), puis le
ministère du Développement (économique, puis « et de la coopération internationale »), le
ministère de l'Emploi et le Commissariat général au développement régional. Nature : dotations ou
enveloppes budgétaires (« dotation budgétaire », « montant engagé »), non dépenses constatées.
Millions de dinars courants. Chaque édition couvre quatre ou cinq ans et révise les précédentes :
est retenue ici la dernière édition qui imprime l'année, citée en dernière colonne. Lu sur couche
texte, **non relu à l'image**.

| Année | Chantiers nationaux | Chantiers régionaux | SIVP 1 | SIVP 2 | FIAP | CEF | Fonds 21-21 | Total du tableau | Édition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1987 | 10,4 | 17,5 | — | — | — | 0,3 | — | 50,8 | 1991 |
| 1988 | 11,9 | 35,3 | 1,8 | — | — | 0,4 | — | 73,3 | 1992 |
| 1989 | 11,6 | 35,2 | 2,7 | 0,6 | — | 0,7 | — | 73,3 | 1993 |
| 1990 | 21,4 | 38,0 | 2,9 | 0,7 | 0,5 | 1,4 | — | 97,5 | 1994 |
| 1991 | 16,7 | 41,1 | 2,6 | 0,7 | 1,2 | 1,1 | — | 86,7 | 1994 |
| 1992 | 37,6 | 33,2 | 2,8 | 1,0 | 6,5 | 1,0 | — | n. r. | 1995 |
| 1993 | 40,0 | 23,7 | 2,8 | 1,0 | 6,9 | 1,0 | — | n. r. | 1996 |
| 1994 | 43,8 | 25,8 | 3,3 | 1,3 | 2,8 | 1,2 | — | n. r. | 1996 |
| 1995 | 44,5 | 31,5 | 4,7 | 2,4 | 4,6 | 0,9 | — | 115,2 | 1998 |
| 1996 | 40,0 | 28,4 | 3,8 | 1,8 | 3,1 | 0,9 | — | 108,1 | 1999 (FIAP : 1998) |
| 1997 | 50,5 | 27,8 | 2,7 | 0,8 | 1,4 | 0,3 | — | 121,7 | 1999 (FIAP : 1998) |
| 1998 | 60,0 | 29,4 | 4,5 | 1,2 | 2,4 | 0,7 | — | 148,4 | 2001 |
| 1999 | 55,0 | 34,4 | 6,5 | 1,5 | 8,4 | 0,4 | 0 | 151,5 | 2002 |
| 2000 | 59,0 | 46,9 | 9,7 | 1,6 | 8,9 | 0,5 | 58,4 | 238,8 | 2003 |
| 2001 | 60,5 | 44,7 | 8,6 | 0,9 | 4,7 | 0,4 | 80,0 | 235,6 | 2004 |
| 2002 | 40,7 | 30,5 | 7,1 | 0,8 | 6,3 | 0,2 | 80,0 | 194,8 | 2005 |
| 2003 | 52,0 | 92,0 | 9,7 | 1,5 | 5,2 | 0,5 | 80,0 | 256,3 | 2006 |
| 2004 | 66,2 | 39,4 | 12,8 | 2,5 | 7,2 | 0,8 | 80,0 | 230,9 | 2007 |
| 2005 | 59,5 | 23,3 | 18,0 | 3,0 | 6,0 | 1,1 | 80,0 | 207,2 | 2008 |
| 2006 | 55,2 | 26,1 | 25,5 | 4,0 | 6,8 | 0,9 | 85,0 | 213,1 | 2008 |
| 2007 | 62,5 | 40,1 | 33,3 | 4,3 | 7,9 | 0,8 | 90,0 | 267,9 | 2008 |
| 2008 | 73,8 | 46,6 | 38,2 | 3,9 | 7,6 | 0,9 | 100,0 | 285,9 | 2008 |

Mises en garde. (1) Le total comprend d'autres lignes non reprises ici (programme de développement
rural intégré, programme régional de développement, développement urbain intégré, FONAPRA,
FOPRODI selon les années) : il n'est pas la somme des colonnes. (2) **Les révisions sont fortes**
au début des années 1990 : les chantiers nationaux de 1992 valent 23,9 (édition 1992), 35,1 (1994)
puis 37,6 (1995) ; la dotation 2000 du Fonds 21-21 vaut 60,0 (éditions 2001 et 2002) puis 58,4
(2003) ; les SIVP de 2000 valent 9,3 puis 11,3. Garder les valeurs écartées dans un fichier de
conflits, comme pour `bct-emploi-occupe`. (3) Les éditions 1997 et 2000 ne portent pas la ligne
dans leur couche texte ; l'édition 1998 imprime quatre colonnes de chiffres sous trois millésimes
(lecture retenue : 1995 à 1998). (4) Après 2008, le tableau disparaît : l'édition 2009 donne à la
place les bénéficiaires par programme.

**2009, année de transition** (BCT, *Rapport annuel 2009*, source : ministère du Développement et
de la coopération internationale) : 100 MDT alloués au Fonds national de l'emploi pour 130 000
bénéficiaires, plus 57 MDT sur le budget de l'État par l'ANETI, plus 105 MDT du plan de relance de
la loi de finances complémentaire. Bénéficiaires réalisés (prévus) : SIVP 33 639 (36 000) ; CIDES
2 387 (2 500) ; CAIP 20 361 (16 600) ; CRVA 223 (800) ; PAPPE 11 443 (13 700) ; contrat
emploi-solidarité 28 000 (37 100) ; projets et sources de revenus 83 426 (82 500) ; total 179 479
(189 200). Le même rapport dit 123 000 bénéficiaires du Fonds en 2008 et 117 000 en 2007 (édition
2008, p. 111).

Chaque édition donne aussi, en prose, des contrats signés (par exemple 24 313 contrats SIVP en
2005, dont 18 492 SIVP 1 et 5 821 SIVP 2 ; 2 719 SIVP 1 et 1 658 SIVP 2 en 1993) : **série de
bénéficiaires 1988-2008 à dépouiller**, non faite ici. Les éditions 2010 à 2025 ne portent ni le
tableau ni les sigles (recherche sur couche texte ; éditions 2016 et 2019 : mentions sans chiffres).
Les annuaires statistiques de l'INS (`data/raw/ins-publications/`) n'ont pas été parcourus.

## 6. Rapports extérieurs et évaluations (à part, avec leur méthode)

### 6.1 Rapports d'institutions internationales

- **Banque mondiale (2004), *Republic of Tunisia. Employment Strategy*, rapport n° 25456-TUN,
  vol. I, chap. 4** (pp. 69-72). *Méthode* : calcul de la Banque sur les **dotations budgétaires**
  communiquées par le ministère des Finances (27 mai 2002, mises à jour le 3 décembre 2003),
  complétées par l'ATE et les agences de formation ; nomenclature de l'OCDE ; périmètre large, qui
  comprend la formation professionnelle initiale (ATFP) et le microcrédit en montants bruts, donc
  bien au-delà des programmes de l'emploi. *Résultats* (tableau 35), dépense nominale en MD :
  208,85 (1997) ; 258,79 (1998) ; 336,19 (1999) ; 428,31 (2000) ; 483,16 (2001) ; 455,74 (2002,
  prévision). Le rapport dit « environ 1,5 % du PIB » en 2002 (**base du PIB non précisée par la
  source**), environ 1 % hors microcrédits remboursables ; il compare IXe Plan (1 716 MD) et Xe Plan
  (2 350 MD prévus) par catégorie (tableau 36). Le vol. II (annexes) était déjà dans l'entrepôt.
- **Banque mondiale (2015), Angel-Urdinola, Nucifora et Robalino (dir.), *Labor Policy to Promote
  Good Jobs in Tunisia***, chap. 3, tableau 3.5 « ALMPs in Tunisia Provided by ANETI, October
  2011 » (pp. 71-72). *Méthode* : tableau descriptif, budgets et effectifs repris de l'ANETI, sans
  calcul propre. *Chiffres* pour 2011 : AMAL, 252,6 MD et 155 000 bénéficiaires ; SIVP, 57 MD et
  46 000 ; CIDES, 5 MD et 3 000 ; PAPPE, 4,2 MD. Le chapitre écrit que le coût des programmes,
  « 0,8 % du PIB en 2011 », est financé par le Fonds national de l'emploi et géré par l'ANETI
  (p. 69 ; **base du PIB non précisée par la source**, mode de calcul non décrit).
- **Banque mondiale (2013), *Building Effective Employment Programs for Unemployed Youth in the
  Middle East and North Africa*** ; **(2014), *Tunisia: Breaking the Barriers to Youth Inclusion***,
  rapport n° 89233-TN ; **(2011), note « The AMAL Program »** : récupérés, non dépouillés.

### 6.2 Évaluations

- **Broecke (2013), « Tackling graduate unemployment in North Africa through employment subsidies:
  A look at the SIVP programme in Tunisia », *IZA Journal of Labor Policy*, 2:9.** *Méthode* :
  enquête de suivi des diplômés de 2004 (échantillon représentatif de 4 763 diplômés, interrogés en
  2005 et 2007 ; 3 511 observations retenues) ; moindres carrés et appariement ; l'auteur souligne
  que l'entrée dans le programme n'est pas aléatoire. *Résultats* : les bénéficiaires du SIVP sont
  moins souvent sans emploi (−7 points) et au chômage (−9 points), bien plus souvent dans le secteur
  privé (+29 points), mais moins souvent en contrat permanent (−24 points) et gagnent 52 D de moins
  (près de −9 %) ; coût par emploi créé estimé à environ 18 000 D, sous l'hypothèse d'un coût de
  1 440 D par participant. L'article rapporte, d'après l'ANETI (2011), un budget du SIVP d'environ
  45,5 MD en 2010 et des bénéficiaires passés de moins de 15 000 (2004) à un peu plus de 45 000
  (2011) — chiffres de seconde main.
- **ONEQ et OIT (novembre 2023), *Étude d'évaluation d'impact des programmes d'emploi : Karama et
  CSC*.** *Méthode* : enquête auprès de la cohorte 2018 des bénéficiaires et d'un groupe témoin tiré
  du fichier des demandeurs d'emploi de l'ANETI ; double différence avec variables de contrôle ;
  observation un à deux ans après la sortie. *Résultats* pour le contrat-dignité : effet de
  −8 points sur l'emploi total, +8 points sur l'emploi permanent, −17 points sur l'emploi non
  permanent. Résultats du contrat de service civil et taille des échantillons : non relevés.
- **Premand, Brodmann, Almeida, Grun et Barouni (2012), « Entrepreneurship Training and
  Self-Employment among University Graduates: Evidence from a Randomized Trial in Tunisia »,
  Banque mondiale, Policy Research Working Paper n° 6285.** *Méthode* : affectation aléatoire à une
  filière « entrepreneuriat » en dernière année de licence appliquée ; résultats un an après le
  diplôme. *Résultats* (résumé) : hausse de l'emploi indépendant, faible en valeur absolue ; taux
  d'emploi inchangé. Chiffres à relever au texte avant emploi.
- **ONEQ** : « Étude de suivi du SIVP » (2009), « Évaluation du service civil volontaire » (2010),
  « Rapport d'évaluation du programme AMAL » (février 2012 — suivi d'indicateurs, non mesure
  d'impact), « Évaluation du PC50 » (2016) : récupérés, méthodes non relevées.

## 7. Lacunes et recherches infructueuses

### 7.1 Lacunes (TODO, rien n'est inventé)

1. **Dépense exécutée du FNE, par an et par programme** : non trouvée. Pistes : rapports annuels de
   performance de la mission (gbo.tn — seuls les PAP 2022, 2024 et 2025 ont été obtenus ; les
   adresses `/fr/rap-mission-…-<année>` essayées pour 2018 à 2026 ne répondent pas) ; tableaux
   images des lois de règlement ; Cour des comptes (une recherche en ligne, sans résultat : ne vaut
   pas absence).
2. **Prévisions du FNE pour 2000 à 2010 et depuis 2021** : non imprimées fonds par fonds dans la
   couche texte du JORT ; les tableaux « E » des lois de finances 2000-2010 sont à relire à l'image.
3. **Bénéficiaires par programme avant 2010 et de 2014 à 2022** : rapports annuels de l'ANETI et de
   l'ONEQ non archivés pour ces années parmi les 177 captures de `emploi.tn/uploads/` listées à la
   Wayback Machine. La BCT couvre 1987-2009 (§ 5.3), en dotations surtout. Non essayés :
   `aneti.nat.tn`, annuaires statistiques de l'INS (tableaux de placement).
4. **Barèmes du SIVP entre 1993 et 2009** : le décret n° 93-1049 renvoie à un arrêté le barème
   (60-80 D et 100-250 D) ; le décret n° 2009-1026 « porte à 150 D » les contrats en cours, ce qui
   suppose un montant antérieur inférieur, non établi. Arrêté du 15 juin 1995 (JORT n° 50, 23 juin
   1995, pp. 1342-1343) et décret n° 2000-1786 (indemnité complémentaire des stagiaires de
   l'administration) : non lus.
5. **Textes non ouverts** (intitulé seul) : décrets n° 93-1354, 97-1938, 97-1930, 2003-564,
   98-868 et ses modificatifs, 94-494 (prise en charge de la contribution patronale), 2001-1722
   (contrats de formation aux fins de réinsertion), 2006-2990 et 2007-1237 (stage en vue de créer
   une entreprise), décret-loi n° 2022-78, arrêté du 8 août 2017, arrêté du 16 juillet 2021 et
   décret n° 2025-459 (chantiers), LF 2005 art. 21 (associations), LF 2011 art. 28 en entier.
6. **Lectures à reprendre à l'image** : tous les montants marqués [T°] (1981-1993) ; indemnités de
   FORSATI (2016) ; page de la loi n° 67-11 ; articles des lois de finances 2022 à 2026 imputant
   des lignes de crédit sur le FNE ; édition française du décret n° 2019-542, absente de pist.tn
   (les noms français des programmes de 2019 viennent du décret n° 2023-461 et du PAP 2022).
7. **Trois PDF de l'ONEQ tronqués à 1 048 576 octets par l'archive** (illisibles, supprimés après
   essai) : conjoncture du 4e trimestre 2012 (capture 20210226000052), rapport sur le marché du
   travail 2013 (20210226000329), note de septembre 2014 (20210226000918) — autres captures à essayer.
8. **Études non obtenues** : OCDE (2015), *Investir dans la jeunesse : Tunisie* (page de l'éditeur
   seule) ; version de la BAD de l'étude de Broecke (document de travail n° 158 : 403).

### 7.2 Fiches de recherche proposées pour `docs/recherches.yml`

Aucune fiche existante ne porte sur ces objets (`recherches.py lister` consulté le 6 octobre 2026).
`jort_cache` va jusqu'au 2 octobre 2026. Les passes ci-dessous n'ont porté que sur les intitulés :
le plein texte du corpus n'a pas été parcouru, sauf mention.

```yaml
- id: r-fiap-texte-fondateur
  objet: texte instituant le fonds d'insertion et d'adaptation professionnelle (FIAP), vers 1990-1991
  ou: [precis/fr/marche_travail/_politiques_emploi.qmd]
  requetes:
    titres_fts: ['"insertion et d adaptation professionnelle" OR "insertion et l adaptation professionnelle"', '"fonds d insertion" OR ("adaptation professionnelle" AND fonds)']
    plein_texte: ["insertion et d'adaptation prof"]
    depuis: 1988-01-01
  passes:
  - date: 2026-10-06
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: "intitulés de jort_cache en entier : un seul texte, la loi n° 91-4 (ratification du prêt BIRD) ; plein texte limité aux fascicules déjà convertis de 1990 à 1994 (markdown_output), aucun résultat ; fascicules scannés non océrisés non parcourus ; intitulés arabes non interrogés"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire: [lire la loi de finances pour 1991 et le fascicule de la loi n° 91-4, interroger iort_ar]
- id: r-d2012-2369-arretes-cheques
  objet: arrêtés conjoints fixant les conditions d'émission du chèque d'amélioration de l'employabilité et du chèque d'appui à l'emploi (décret n° 2012-2369, art. 6, 9 et 11)
  ou: [precis/fr/marche_travail/_politiques_emploi.qmd]
  requetes:
    titres_fts: ['"cheque d amelioration" OR "cheque d appui"']
    iort_ar: [صك تحسين, صك دعم التشغيل]
    depuis: 2012-10-16
  passes:
  - date: 2026-10-06
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés français (FTS) et arabes (LIKE) de jort_cache jusqu'au n° 107 de 2026 ; aucun fascicule lu ; les fascicules que la base ignore ne sont pas couverts"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
- id: r-sivp-bareme-1993-2009
  objet: arrêtés fixant le barème de l'indemnité des stages d'initiation à la vie professionnelle (décret n° 93-1049, art. 25 et 28) et texte l'ayant modifiée avant le décret n° 2009-349
  ou: [precis/fr/marche_travail/_politiques_emploi.qmd]
  requetes:
    titres_fts: ['"initiation a la vie professionnelle"', '"emploi des jeunes"', '"bareme des indemnites" OR (indemnite AND stagiaires AND "vie professionnelle")']
    depuis: 1993-05-03
  periode: {jusqu_au: 2009-02-10, motif: "barème antérieur au décret n° 2009-349, publié le 10 février 2009"}
  passes:
  - date: 2026-10-06
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache : candidats non lus, l'arrêté du 15 juin 1995 (JORT n° 50 de 1995) et le décret n° 2000-1786 ; aucun arrêté de barème à l'intitulé"
    couvert_jusqu_au: 2009-02-10
    resultat: aucun
  a_faire: [lire l'arrêté du 15 juin 1995 et le décret n° 2000-1786]
- id: r-chantiers-regionaux-texte-fondateur
  objet: texte instituant ou organisant les chantiers régionaux et nationaux d'emploi, antérieur au décret gouvernemental n° 2021-436
  ou: [precis/fr/marche_travail/_politiques_emploi.qmd]
  requetes:
    titres_fts: ['"chantiers" AND (emploi OR chomage OR ouvriers)', '"lutte contre le sous-developpement" OR "sous developpement"', '"chantiers regionaux" OR "chantiers nationaux"']
    iort_ar: [الحضائر]
    depuis: 1956-01-01
  periode: {jusqu_au: 2021-06-18, motif: "texte antérieur au décret gouvernemental n° 2021-436, publié le 18 juin 2021"}
  passes:
  - date: 2026-10-06
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache : décrets de prorogation de 1956-1957, lois n° 57-70 et n° 60-16, loi n° 62-31, puis rien avant 2021 ; deux intitulés arabes contiennent « الحضائر » (LIKE sur titre) : LF 2013, art. 77 (encouragement du secteur privé à recruter des ouvriers de chantiers) et LF 2024, art. 12 (régularisation des ouvriers de 45 à 55 ans, qui modifie l'art. 18 bis d'une loi n° 2021-27) — aucun n'institue le mécanisme ; visas du décret n° 2021-436 non exploités"
    couvert_jusqu_au: 2021-06-17
    resultat: aucun
  a_faire: [relever les visas du décret n° 2021-436, identifier la loi n° 2021-27 et son art. 18 bis, lire la loi n° 58-45 art. 29 (lutte contre le chômage)]
```

## Annexe A — Références candidates (CSL-JSON)

**Déjà présentes, à réemployer** : `decret2017-358` (contrat-dignité, `precis/fr/references.json`,
pp. 996-998), `loi88-60-lfc1988`, `loi-93-120-code-incitations`, et les lois de finances `lf-2000`,
`lf-2001`, `lf-2003`, `lf-2004`… (vérifier laquelle désigne quelle loi avant réemploi). Les autres
clés ci-dessous sont à créer. URL sondées le
6 octobre 2026. Pour chaque texte, l'entrée arabe reprend la clé et l'URL `A/Ja`.

```json
[
 {"id":"loi67-11","type":"legislation","title":"Loi n° 67-11 du 8 mars 1967, portant création de l'Office de la formation professionnelle et de l'emploi","issued":{"date-parts":[[1967,3,8]]},"container-title":"Journal officiel de la République tunisienne","number":"12","URL":"https://www.pist.tn/jort/1967/1967F/Jo01267.pdf","note":"AR : https://www.pist.tn/jort/1967/1967A/Ja01267.pdf ; page à relire"},
 {"id":"loi73-8","type":"legislation","title":"Loi n° 73-8 du 31 janvier 1973, modifiant la loi n° 67-11 du 8 mars 1967 et créant l'Office des travailleurs tunisiens à l'étranger, de l'emploi et de la formation professionnelle","issued":{"date-parts":[[1973,1,31]]},"number":"5","page":"186","URL":"https://www.pist.tn/jort/1973/1973F/Jo00573.pdf","note":"AR : https://www.pist.tn/jort/1973/1973A/Ja00573.pdf"},
 {"id":"loi83-111","type":"legislation","title":"Loi n° 83-111 du 9 décembre 1983, portant création de l'Office de la formation et de la promotion professionnelle et de l'Office de la promotion de l'emploi et des travailleurs tunisiens à l'étranger","issued":{"date-parts":[[1983,12,9]]},"number":"81","page":"3207-3208","URL":"https://www.pist.tn/jort/1983/1983F/Jo08183.pdf","note":"AR : https://www.pist.tn/jort/1983/1983A/Ja08183.pdf"},
 {"id":"loi93-11","type":"legislation","title":"Loi n° 93-11 du 17 février 1993, portant création de l'Agence tunisienne de l'emploi et de l'Agence tunisienne de la formation professionnelle","issued":{"date-parts":[[1993,2,17]]},"number":"14","page":"256-257","URL":"https://www.pist.tn/jort/1993/1993F/Jo01493.pdf","note":"AR : https://www.pist.tn/jort/1993/1993A/Ja01493.pdf"},
 {"id":"decret2003-564","type":"legislation","title":"Décret n° 2003-564 du 17 mars 2003, portant changement d'appellation de l'Agence tunisienne de l'emploi et des bureaux de l'emploi qui en relèvent","issued":{"date-parts":[[2003,3,17]]},"number":"23","page":"589","URL":"https://www.pist.tn/jort/2003/2003F/Jo0232003.pdf","note":"AR : https://www.pist.tn/jort/2003/2003A/Ja0232003.pdf ; intitulé seul"},
 {"id":"loi81-75","type":"legislation","title":"Loi n° 81-75 du 9 août 1981, relative à la promotion de l'emploi des jeunes","issued":{"date-parts":[[1981,8,9]]},"number":"52","page":"1869-1870","URL":"https://www.pist.tn/jort/1981/1981F/Jo05281.pdf","note":"AR : https://www.pist.tn/jort/1981/1981A/Ja05281.pdf"},
 {"id":"decret81-1220","type":"legislation","title":"Décret n° 81-1220 du 24 septembre 1981, relatif à la promotion de l'emploi des jeunes","issued":{"date-parts":[[1981,9,24]]},"number":"59","page":"2245-2247","URL":"https://www.pist.tn/jort/1981/1981F/Jo05981.pdf","note":"AR : https://www.pist.tn/jort/1981/1981A/Ja05981.pdf"},
 {"id":"decret87-1190","type":"legislation","title":"Décret n° 87-1190 du 26 août 1987, portant organisation d'un système de stages d'initiation à la vie professionnelle pour les diplômés du supérieur","issued":{"date-parts":[[1987,8,26]]},"number":"64","page":"1116","URL":"https://www.pist.tn/jort/1987/1987F/Jo06487.pdf","note":"AR : https://www.pist.tn/jort/1987/1987A/Ja06487.pdf"},
 {"id":"decret88-715","type":"legislation","title":"Décret n° 88-715 du 31 mars 1988, portant organisation d'un système de stages d'initiation à la vie professionnelle pour les diplômés du second cycle secondaire et assimilés","issued":{"date-parts":[[1988,3,31]]},"number":"24","page":"550-551","URL":"https://www.pist.tn/jort/1988/1988F/Jo02488.pdf","note":"AR : https://www.pist.tn/jort/1988/1988A/Ja02488.pdf"},
 {"id":"loi93-17","type":"legislation","title":"Loi n° 93-17 du 22 février 1993, modifiant et complétant la loi n° 81-75 du 9 août 1981 relative à la promotion de l'emploi des jeunes","issued":{"date-parts":[[1993,2,22]]},"number":"16","page":"300","URL":"https://www.pist.tn/jort/1993/1993F/Jo01693.pdf","note":"AR : https://www.pist.tn/jort/1993/1993A/Ja01693.pdf"},
 {"id":"decret93-1049","type":"legislation","title":"Décret n° 93-1049 du 3 mai 1993, portant encouragement à l'emploi des jeunes","issued":{"date-parts":[[1993,5,3]]},"number":"36","page":"661-663","URL":"https://www.pist.tn/jort/1993/1993F/Jo03693.pdf","note":"AR : https://www.pist.tn/jort/1993/1993A/Ja03693.pdf"},
 {"id":"loi2005-91","type":"legislation","title":"Loi n° 2005-91 du 3 octobre 2005, portant encouragement du secteur privé à recruter les diplômés de l'enseignement supérieur","issued":{"date-parts":[[2005,10,3]]},"number":"79","page":"2590","URL":"https://www.pist.tn/jort/2005/2005F/Jo0792005.pdf","note":"AR : https://www.pist.tn/jort/2005/2005A/Ja0792005.pdf"},
 {"id":"decret2009-349","type":"legislation","title":"Décret n° 2009-349 du 9 février 2009, fixant les programmes du fonds national de l'emploi, les conditions et les modalités de leur bénéfice","issued":{"date-parts":[[2009,2,9]]},"number":"12","page":"477-482","URL":"https://www.pist.tn/jort/2009/2009F/Jo0122009.pdf","note":"AR : https://www.pist.tn/jort/2009/2009A/Ja0122009.pdf"},
 {"id":"arrete-2009-03-19-indemnites-fne","type":"legislation","title":"Arrêté du ministre de l'emploi et de l'insertion professionnelle des jeunes du 19 mars 2009, fixant les montants minimums des indemnités complémentaires mensuelles obligatoirement servies par les entreprises privées dans le cadre des programmes du fonds national de l'emploi","issued":{"date-parts":[[2009,3,19]]},"number":"25","page":"897-898","URL":"https://www.pist.tn/jort/2009/2009F/Jo0252009.pdf","note":"AR : https://www.pist.tn/jort/2009/2009A/Ja0252009.pdf"},
 {"id":"decret2010-87","type":"legislation","title":"Décret n° 2010-87 du 20 janvier 2010, modifiant et complétant le décret n° 2009-349 du 9 février 2009","issued":{"date-parts":[[2010,1,20]]},"number":"7","page":"228-232","URL":"https://www.pist.tn/jort/2010/2010F/Jo0072010.pdf","note":"AR : https://www.pist.tn/jort/2010/2010A/Ja0072010.pdf"},
 {"id":"dl2011-16","type":"legislation","title":"Décret-loi n° 2011-16 du 26 mars 2011, relatif au fonds national de l'emploi","issued":{"date-parts":[[2011,3,26]]},"number":"21","page":"381","URL":"https://www.pist.tn/jort/2011/2011F/Jo0212011.pdf","note":"AR : https://www.pist.tn/jort/2011/2011A/Ja0212011.pdf"},
 {"id":"decret2011-621","type":"legislation","title":"Décret n° 2011-621 du 23 mai 2011, modifiant et complétant le décret n° 2009-349 du 9 février 2009","issued":{"date-parts":[[2011,5,23]]},"number":"38","page":"799-800","URL":"https://www.pist.tn/jort/2011/2011F/Jo0382011.pdf","note":"AR : https://www.pist.tn/jort/2011/2011A/Ja0382011.pdf"},
 {"id":"decret2012-953","type":"legislation","title":"Décret n° 2012-953 du 2 août 2012, modifiant et complétant le décret n° 2009-349 du 9 février 2009","issued":{"date-parts":[[2012,8,2]]},"number":"61","page":"1799-1803","URL":"https://www.pist.tn/jort/2012/2012F/Jo0612012.pdf","note":"AR : https://www.pist.tn/jort/2012/2012A/Ja0612012.pdf"},
 {"id":"decret2012-2369","type":"legislation","title":"Décret n° 2012-2369 du 16 octobre 2012, fixant les programmes du fonds national de l'emploi, les conditions et les modalités de leur bénéfice","issued":{"date-parts":[[2012,10,16]]},"number":"82","page":"2531-2542","URL":"https://www.pist.tn/jort/2012/2012F/Jo0822012.pdf","note":"AR : https://www.pist.tn/jort/2012/2012A/Ja0822012.pdf"},
 {"id":"decret2013-3766","type":"legislation","title":"Décret n° 2013-3766 du 18 septembre 2013, modifiant et complétant le décret n° 2012-2369 du 16 octobre 2012","issued":{"date-parts":[[2013,9,18]]},"number":"77","page":"2784-2788","URL":"https://www.pist.tn/jort/2013/2013F/Jo0772013.pdf","note":"AR : https://www.pist.tn/jort/2013/2013A/Ja0772013.pdf"},
 {"id":"decret2016-904","type":"legislation","title":"Décret gouvernemental n° 2016-904 du 27 juillet 2016, complétant le décret n° 2012-2369 du 16 octobre 2012","issued":{"date-parts":[[2016,7,27]]},"number":"63","page":"2405-2407","URL":"https://www.pist.tn/jort/2016/2016F/Jo0632016.pdf","note":"AR : https://www.pist.tn/jort/2016/2016A/Ja0632016.pdf"},
 {"id":"decret2019-542","type":"legislation","title":"Décret gouvernemental n° 2019-542 du 28 mai 2019, fixant les programmes du fonds national de l'emploi, les conditions et les modalités de leur bénéfice","issued":{"date-parts":[[2019,5,28]]},"number":"51","page":"2081-2091 (éd. arabe)","URL":"https://www.pist.tn/jort/2019/2019A/Ja0512019.pdf","note":"édition française absente de pist.tn (404 le 6 octobre 2026) : l'entrée française pointe l'édition arabe"},
 {"id":"decret2023-461","type":"legislation","title":"Décret n° 2023-461 du 5 juin 2023, modifiant et complétant le décret gouvernemental n° 2019-542 du 28 mai 2019","issued":{"date-parts":[[2023,6,5]]},"number":"60","URL":"https://www.pist.tn/jort/2023/2023F/Jo0602023.pdf","page":"1552","note":"AR : https://www.pist.tn/jort/2023/2023A/Ja0602023.pdf ; première page d'après la notice, à confirmer"},
 {"id":"decret2021-436","type":"legislation","title":"Décret gouvernemental n° 2021-436 du 17 juin 2021, relatif à la cessation d'application du mécanisme de l'emploi des ouvriers des chantiers régionaux et des chantiers agricoles hors chantier","issued":{"date-parts":[[2021,6,17]]},"number":"52","page":"1546","URL":"https://www.pist.tn/jort/2021/2021F/Jo0522021.pdf","note":"AR : https://www.pist.tn/jort/2021/2021A/Ja0522021.pdf ; page de la notice"},
 {"id":"oneq-suivi-pae-2012","type":"report","title":"Rapport annuel de suivi des programmes actifs d'emploi (année 2012)","author":[{"literal":"Observatoire national de l'emploi et des qualifications"}],"publisher":"Ministère de la Formation professionnelle et de l'Emploi","issued":{"date-parts":[[2013,5]]},"URL":"https://web.archive.org/web/20211229023056/http://www.emploi.tn/uploads/pdf/ONEQ/Rapport_annuel_de_suivi_des_programmes_actifs_demploi_Annee_2012.pdf"},
 {"id":"oneq-suivi-pae-2013","type":"report","title":"Rapport de suivi des programmes d'emploi (année 2013)","author":[{"literal":"Observatoire national de l'emploi et des qualifications"}],"publisher":"Ministère de la Formation professionnelle et de l'Emploi","issued":{"date-parts":[[2014]]},"URL":"https://web.archive.org/web/20211229022839/http://www.emploi.tn/uploads/pdf/ONEQ/2014_Rapport_suivi_des_programmes_actifs_demploi.pdf","note":"date de parution à relever sur la couverture"},
 {"id":"oneq-oit-2023-karama-csc","type":"report","title":"Étude d'évaluation d'impact des programmes d'emploi : Karama et CSC","author":[{"literal":"Observatoire national de l'emploi et des qualifications"}],"publisher":"Bureau international du Travail","publisher-place":"Genève","issued":{"date-parts":[[2023,11]]},"URL":"https://web.archive.org/web/20250621164224/https://www.emploi.tn/uploads/pdf/ONEQ/Etude_evaluation_impact_KARAMA.pdf"},
 {"id":"broecke2013","type":"article-journal","title":"Tackling graduate unemployment in North Africa through employment subsidies: A look at the SIVP programme in Tunisia","author":[{"family":"Broecke","given":"Stijn"}],"container-title":"IZA Journal of Labor Policy","volume":"2","number":"9","issued":{"date-parts":[[2013]]},"DOI":"10.1186/2193-9004-2-9","URL":"https://izajolp.springeropen.com/articles/10.1186/2193-9004-2-9"},
 {"id":"premand2012","type":"report","title":"Entrepreneurship Training and Self-Employment among University Graduates: Evidence from a Randomized Trial in Tunisia","author":[{"family":"Premand","given":"Patrick"},{"family":"Brodmann","given":"Stefanie"},{"family":"Almeida","given":"Rita"},{"family":"Grun","given":"Rebekka"},{"family":"Barouni","given":"Mahdi"}],"genre":"Policy Research Working Paper","number":"6285","publisher":"World Bank","issued":{"date-parts":[[2012,12]]},"URL":"https://openknowledge.worldbank.org/entities/publication/8588065d-91d4-5383-b42d-6b487549ff17"},
 {"id":"bm2004-employment-strategy","type":"report","title":"Republic of Tunisia: Employment Strategy, Volume 1. Main Report","author":[{"literal":"World Bank"}],"number":"25456-TUN","issued":{"date-parts":[[2004,5,28]]},"URL":"https://openknowledge.worldbank.org/entities/publication/fe2b7263-608b-5d65-9899-8568cc227afa"},
 {"id":"bm2015-labor-policy","type":"book","title":"Labor Policy to Promote Good Jobs in Tunisia: Revisiting Labor Regulation, Social Security, and Active Labor Market Programs","editor":[{"family":"Angel-Urdinola","given":"Diego F."},{"family":"Nucifora","given":"Antonio"},{"family":"Robalino","given":"David"}],"publisher":"World Bank","issued":{"date-parts":[[2015]]},"DOI":"10.1596/978-1-4648-0271-3","URL":"https://openknowledge.worldbank.org/entities/publication/24455706-a008-5c64-a6b9-f75921bfdd20"},
 {"id":"gbo-pap-emploi-2022","type":"report","title":"Projet annuel de performance au titre de l'année 2022. Mission emploi et formation professionnelle","author":[{"literal":"Ministère de la Formation professionnelle et de l'Emploi"}],"issued":{"date-parts":[[2022]]},"URL":"http://www.gbo.tn/sites/default/files/2022-02/PAP-2022%20Emploi%20fr.pdf"}
]
```

À compléter de même (lus, non rédigés ici) : décrets n° 88-733, 98-1120, 2009-1026, 2009-1052,
2011-1, 2011-98, 2011-2484, 2014-2901, 2016-445 ; lois de règlement n° 2018-49, 2024-18 et 2024-19 ;
rapports sur le budget 2022, 2024 et 2025 ; PAP 2024 et 2025 ; notes de conjoncture de l'ONEQ ;
rapports annuels de la BCT 1991 à 2009 (clé `bct-ra` annoncée dans le catalogue de `tunisia-data`,
à verser dans la bibliographie du précis avant toute figure).
Les adresses des pages d'Open Knowledge ont été obtenues par l'interface de recherche du dépôt et
non ouvertes dans un navigateur : à vérifier par le bibliographe.

## Annexe B — Notions à porter au glossaire

Terme arabe relevé dans l'édition arabe du JORT (décret gouvernemental n° 2019-542, n° 51 de 2019 ;
tableaux des lois de finances pour 2018 à 2020) ou, à défaut, dans un rapport du ministère des
Finances — la source est dite.

| Terme français | Terme arabe relevé | Source du terme arabe | Texte canonique |
|---|---|---|---|
| Fonds national de l'emploi (« 21-21 ») | الصندوق الوطني للتشغيل | JORT n° 51/2019, art. 1er ; LF 2018, tableau | LF 2000, art. 13 |
| Fonds de promotion de la formation et de l'apprentissage professionnel | صندوق النهوض بالتكوين والتدريب المهني | LF 2018, tableau (JORT n° 101/2017, éd. ar.) | LF 2000, art. 17 |
| Agence nationale pour l'emploi et le travail indépendant (ANETI) | الوكالة الوطنية للتشغيل والعمل المستقل | JORT n° 51/2019, art. 7 | décret n° 2003-564 |
| Bureau de l'emploi et du travail indépendant | مكتب التشغيل والعمل المستقل | JORT n° 51/2019, art. 9 | décret n° 2003-564 |
| Stage d'initiation à la vie professionnelle (SIVP) | تربص الإعداد للحياة المهنية | JORT n° 51/2019, art. 61 (au pluriel) | décrets n° 87-1190 et 2009-349 |
| Contrat d'initiation à la vie professionnelle (CIVP) | عقد الإعداد للحياة المهنية | JORT n° 51/2019, art. 2 et 5 | décret gouv. n° 2019-542 ; le décret n° 2023-461 écrit « contrat d'insertion à la vie professionnelle » |
| Contrat d'insertion des diplômés de l'enseignement supérieur (CIDES) | عقد إدماج حاملي شهادات التعليم العالي | JORT n° 51/2019, art. 61 | décret n° 2009-349, art. 11 |
| Contrat d'adaptation et d'insertion professionnelle (CAIP) | عقد التأهيل والإدماج المهني | JORT n° 51/2019, art. 61 (au pluriel) | décret n° 2009-349, art. 20 |
| Contrat de réinsertion dans la vie active (CRVA) | non relevé : couche texte arabe du JORT n° 12/2009 inexploitable, à lire à l'image | — | décret n° 2009-349, art. 25 |
| Contrat-dignité (Karama) | عقد الكرامة | JORT n° 51/2019, art. 2 et 12 | décret gouv. n° 2017-358, art. 26 quater |
| Contrat de service civil (service civil volontaire) | عقد الخدمة المدنية | JORT n° 51/2019, art. 2 et 17 | décret n° 2010-87, art. 40 bis |
| Programme « FORSATI » | برنامج "فرصتي" | JORT n° 51/2019, art. 2 et 25 | décret gouv. n° 2016-904 |
| Programme d'appui aux promoteurs des petites entreprises | برنامج دعم باعثي المؤسسات الصغرى | JORT n° 51/2019, art. 2 et 31 | décrets n° 2009-349 (PAPPE), 2012-2369, 2019-542 |
| Programme de recherche active d'emploi (AMAL) | non relevé : couche texte arabe du JORT n° 38/2011 inexploitable, à lire à l'image | — | décret n° 2011-621, art. 40 sexies |
| Contrat emploi-formation | non relevé : édition arabe de 1993 numérisée sans texte | — | loi n° 81-75 ; décret n° 93-1049, art. 18 |
| Ouvriers de chantiers (régionaux, agricoles) | عملة الحضائر (الحضائر الجهوية والحضائر الفلاحية) | JORT n° 52/2021, éd. arabe, intitulé du décret gouv. n° 2021-436 | décret gouv. n° 2021-436 |
| Politiques actives de l'emploi / programmes actifs d'emploi | non relevé | — | terme de l'ONEQ et des études, absent des textes lus |

## Annexe C — Séries à verser dans `tunisia-data`

| Série | Famille | Fichier source | Tableau, page | Unité | Années |
|---|---|---|---|---|---|
| **Dotations des programmes de soutien à l'emploi** (chantiers, SIVP 1 et 2, FIAP, CEF, Fonds 21-21, total) | budgétaire, relayé par la BCT (sources : ministères du Plan puis du Développement, CGDR) | `data/raw/bct-archives/109/RA_fr_1991.pdf` … `rapport2008.pdf` (16 éditions) | tableau « Programmes de soutien à l'emploi » ; pp. 111-112 en 2008, pages des autres éditions à relever | MD courants | 1987 à 2008, avec millésimes (fichier de conflits à tenir) |
| Bénéficiaires par programme, prévus et réalisés | administratif, relayé par la BCT | `data/raw/bct-archives/109/rapport2009.pdf` | tableau « Nombre de bénéficiaires des différents programmes d'emploi au cours de 2009 » | personnes | 2009 |
| Prévisions de recettes du FNE et du fonds de la formation | budgétaire | fascicules JORT des lois de finances (corpus local `PDFs/JORT/<année>/<fr|ar>/`) | tableau des comptes spéciaux du Trésor ; page relevée pour 2011 seulement | dinars | LF 2011 à LF 2020 |
| Dotation du FNE et répartition par programme | budgétaire | `data/raw/banque-mondiale-rapports/minfin_*_rapport_budget_etat_*_ar.pdf` | section « emploi et formation professionnelle », pp. 115-116 (2022), 159-160 (2024), 165-167 (2025) | MD ; effectifs visés | 2022, 2024, 2025 |
| Excédents du FNE transférés au budget | budgétaire | JORT n° 70/2018 (ar.) et n° 35/2024 | art. 5 des lois de règlement | dinars | 2016, 2017, 2018 |
| Budget du programme « Emploi » de la mission | budgétaire | `data/raw/emploi/gbo_pap_2022_emploi_fr.pdf` | tableau de répartition par programme et par nature, p. 22 env. | milliers de dinars | 2021, 2022 (réalisations 2020 pour la formation seulement) |
| Nouveaux contrats par programme | administratif (ANETI via ONEQ) | `data/raw/emploi/oneq_2013_rapport_suivi_pae_annee_2012.pdf`, `oneq_2014_rapport_suivi_pae.pdf` | tableaux 1, 2, 4 (et 8 pour le PAPPE) | contrats | 2010 à 2013 |
| Nouveaux contrats par programme, périodes partielles | administratif | `oneq_2017_conjoncture_t3_2017.pdf` (tableau n° 4, p. 11), `oneq_2024_conjoncture_t3_2024.pdf` (pp. 2 et 4), `oneq_2018_conjoncture_t1_2018.pdf` (non dépouillé) | — | contrats | 9 mois 2016-2017 ; S1 2023-2024 |
| Dépense des politiques actives de l'emploi | extérieur (Banque mondiale, sur dotations du ministère des Finances) | `data/raw/emploi/wb_2004_employment_strategy_main_25456.pdf` | tableaux 34 à 37, pp. 70-72 | MD courants et de 2002 | 1997 à 2002 |
| Budget et bénéficiaires par programme | extérieur (Banque mondiale, d'après l'ANETI) | `data/raw/emploi/wb_2015_labor_policy_good_jobs_tunisia_92871.pdf` | tableau 3.5, pp. 71-72 | MD ; bénéficiaires | 2011 |

### Fichiers récupérés le 6 octobre 2026 dans `tunisia-data/data/raw/emploi/` (hors git, **répertoire non ignoré**)

| Fichier | Octets | SHA-256 (16 premiers) | Adresse d'origine |
|---|---:|---|---|
| `gbo_pap_2022_emploi_fr.pdf` | 1 826 537 | 166257ea4070f3e5 | http://www.gbo.tn/sites/default/files/2022-02/PAP-2022%20Emploi%20fr.pdf |
| `gbo_pap_2024_emploi.pdf` | 5 038 709 | 572c1980e0d05234 | http://www.gbo.tn/sites/default/files/2024-02/PAP%202024%20%20EMPLOIversion%205%20fev%202024%20%282%29.pdf |
| `gbo_pap_2025_emploi.pdf` | 2 893 771 | 6b222a3f2f5a6ae8 | http://www.gbo.tn/sites/default/files/2025-03/PAP-MEFP2025nv.pdf |
| `izajolp_2013_broecke_sivp.pdf` | 384 039 | 6e3e22f024dfdae1 | https://web.archive.org/web/20211128152746id_/https://izajolp.springeropen.com/track/pdf/10.1186/2193-9004-2-9.pdf |
| `oneq_2009_etude_suivi_sivp.pdf` | 1 144 822 | d01ce1ecc409d5ee | Wayback 20211229023039, `emploi.tn/uploads/pdf/ONEQ/2009_Etude_suivi_du_SIVP.pdf` |
| `oneq_2010_evaluation_scv.pdf` | 335 153 | 2e231a048360a421 | Wayback 20211229022844, `…/ONEQ/2010_Evaluation_du_SCV.pdf` |
| `oneq_2012_evaluation_amal.pdf` | 1 716 834 | 6a0f72be1e018a81 | Wayback 20211229022843, `…/ONEQ/2012_Evaluation_du_programme_AMAL.pdf` |
| `oneq_2013_rapport_suivi_pae_annee_2012.pdf` | 1 427 341 | a0f2ce52f3b456c4 | Wayback 20211229023056, `…/ONEQ/Rapport_annuel_de_suivi_des_programmes_actifs_demploi_Annee_2012.pdf` |
| `oneq_2013_rapport_suivi_pae.pdf` | 1 653 655 | 1e582e049ac52fa7 | Wayback 20211229130315, `…/ONEQ/2013_Rapport_suivi_des_programmes_actifs_demploi.pdf` — **même rapport (année 2012), autre fichier** |
| `oneq_2013_rapport_suivi_pae_s1_2013.pdf` | 581 230 | 279db4f324351198 | Wayback 20211229023031, `…/ONEQ/Rapport_de_suivi_des_PAE_Semestre1_Annee_2013.pdf` (non dépouillé) |
| `oneq_2014_rapport_suivi_pae.pdf` | 693 536 | 27af457f353bd96e | Wayback 20211229022839, `…/ONEQ/2014_Rapport_suivi_des_programmes_actifs_demploi.pdf` (année 2013) |
| `oneq_2016_evaluation_pc50.pdf` | 698 686 | 4995efc3d0a07439 | Wayback 20211229022845, `…/ONEQ/2016_Eavaluation_du_PC50.pdf` |
| `oneq_2017_conjoncture_t3_2017.pdf` | 973 877 | 58d89dc0b5ecb2e1 | Wayback 20210225235103, `…/ONEQ/2017_Conjoncture_de_lemploi_3eme_trimestre_2017.pdf` |
| `oneq_2018_conjoncture_t1_2018.pdf` | 1 268 768 | 9dcb80125805493d | Wayback 20220319201727, `…/ONEQ/2018_Conjoncture_de_lemploi_1er_trimestre_2018.pdf` |
| `oneq_2024_conjoncture_t3_2024.pdf` | 718 832 | 420d7a8c5c4cb087 | Wayback 20250621173451, `…/ONEQ/Conjoncture_T3_2024.pdf` |
| `oneq_etude_evaluation_impact_karama.pdf` | 3 467 508 | 5913f1fa10f485bd | Wayback 20250621164224, `…/ONEQ/Etude_evaluation_impact_KARAMA.pdf` |
| `wb_2004_employment_strategy_main_25456.pdf` | 3 192 376 | 8d60580ae1a9c9ff | https://openknowledge.worldbank.org/server/api/core/bitstreams/9dea02fd-3bef-5c38-8cca-215bc861911a/content |
| `wb_2011_amal_program_64501.pdf` | 933 785 | a09bbdd78f95ce54 | https://openknowledge.worldbank.org/server/api/core/bitstreams/b2535626-1b06-5d3d-8ea3-6d157af31908/content |
| `wb_2012_wps6285_premand_entrepreneurship_training.pdf` | 668 740 | 8a00684db52c1601 | https://openknowledge.worldbank.org/server/api/core/bitstreams/9fc7fa25-c654-5177-837e-4923a6b41eca/content |
| `wb_2013_building_effective_employment_programs_mena_79262.pdf` | 4 995 684 | 8bf07c1dd1665a0a | https://openknowledge.worldbank.org/server/api/core/bitstreams/67362403-ebb6-5d0f-a0ad-c5243b0eaf8b/content |
| `wb_2014_breaking_barriers_youth_inclusion_89233_en.pdf` | 4 355 700 | ec7108f0a090140d | https://openknowledge.worldbank.org/server/api/core/bitstreams/52118eb0-df83-54b2-b0b5-8a3f92478d9f/content |
| `wb_2015_labor_policy_good_jobs_tunisia_92871.pdf` | 6 629 831 | dae6b8a8aea22bd6 | https://openknowledge.worldbank.org/server/api/core/bitstreams/768eac39-6a1a-5251-b149-260d89af0a3a/content |

Aucune ligne n'a été ajoutée aux catalogues `sources/*.csv` de `tunisia-data` (fichiers versionnés,
hors mandat) : ce tableau en tient lieu, empreintes complètes à recalculer par `sha256sum` au
versement. Les adresses Wayback se lisent
`https://web.archive.org/web/<horodatage>id_/http://www.emploi.tn/uploads/pdf/ONEQ/<fichier>`.
Le site `emploi.tn` ne répondait pas le 6 octobre 2026 (délai dépassé) ; `emploi.gov.tn` non plus.

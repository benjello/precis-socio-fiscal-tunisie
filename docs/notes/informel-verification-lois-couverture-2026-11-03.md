# Vérification au JORT des textes cités dans `informel/_couverture.qmd` — 3 novembre 2026

Objet : les références de loi que le chapitre « La couverture sociale des informels »
(`precis/fr/informel/_couverture.qmd`, lignes 11-14) rapporte d'après la thèse de Ben Cheikh (2021,
p. 68-75). Le reste du chapitre ne cite aucun autre texte juridique (le programme « Ahmini », ligne
18, n'a pas de texte cité). Chaque texte a été lu dans le fascicule du corpus local
(`~/projets/PDFs-legislation-tunisie/PDFs/JORT/`), à l'image pour les scans. Les numéros et dates de
fascicule sont ceux du pied de page. Pagination : édition française, sauf mention.

Toutes les clés existent déjà dans `precis/fr/references.json` (`loi81-6`, `decret77-546`,
`decret82-1359`, `decret82-1360`, `decret95-1166`, `loi2002-32`, `decret2002-916`,
`decret2019-379`, `loi94-28`) ou dans les `references.json` des livres (`loi70-34` : caisses,
cotisations sociales, santé, prestations sociales — absente de `precis/fr/references.json` et de
`informel/references.json`). Leurs numéros et pages concordent avec les fascicules, sauf ce qui est
dit au § 3.

## 1. Tableau

| Texte | Conforme au chapitre | JORT n° et date du fascicule | Page (éd. fr.) | Corpus |
|---|---|---|---|---|
| Loi n° 70-34 du 9 juillet 1970, modifiant et complétant la loi n° 60-30 (art. 19 : titre II bis « Les assurances sociales agricoles », art. 95-2 à 95-9) | oui sur le fond (180 jours) ; écart mineur : date absente, « permanents » n'est pas dans le texte | n° 34 des 10-14 juillet 1970 | 894-897 (art. 95-2 : p. 896) | scan sans couche texte, lisible à l'image (`1970/fr/Jo03470.pdf`) ; OCR utile pour une recherche plein texte |
| Loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole | écart de formulation : la règle des 45 jours est une règle de décompte des trimestres, pas une condition d'accès | n° 9 du 13 février 1981 ; rectificatif n° 26 du 17 avril 1981, p. 844 (ne touche pas la règle des 45 jours) | 265-273 (art. 6 : p. 266 ; art. 18 : p. 267) | scan, lisible à l'image (`1981/fr/Jo00981.pdf`, `Jo02681.pdf`) |
| Décret n° 77-546 du 15 juin 1977, organisant la sécurité sociale des pêcheurs | oui | n° 43 du 21 juin 1977 | 1655-1657 | scan, lisible à l'image (`1977/fr/Jo04377.pdf`) ; l'OCR `fra` y échoue presque entièrement |
| Décret n° 82-1359 du 21 octobre 1982, étendant le régime de sécurité sociale aux travailleurs indépendants dans le secteur non agricole | oui ; effet au 1er juillet 1982 (art. 26) | n° 66 des 19-22 octobre 1982 | 2192-2195 | scan, lisible à l'image (`1982/fr/Jo06682.pdf`) |
| Décret n° 82-1360 du 21 octobre 1982, relatif à la sécurité sociale des exploitants et travailleurs indépendants dans l'agriculture | oui ; effet au 1er juillet 1982 (art. 18) | n° 66 des 19-22 octobre 1982 | 2195-2197 | scan, lisible à l'image (même fascicule) |
| Décret n° 95-1166 du 3 juillet 1995, relatif à la sécurité sociale des travailleurs non salariés dans les secteurs agricole et non agricole | oui pour le régime ; écart : les accidents du travail facultatifs ne viennent pas de ce décret mais de la loi n° 94-28, art. 9 | n° 55 du 11 juillet 1995 | 1486-1489 | couche texte, lisible (`1995/fr/Jo05595.pdf`) |
| (texte à ajouter) Loi n° 94-28 du 21 février 1994, portant régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles, section II « L'affiliation facultative », art. 9 à 12 | source réelle de l'affiliation facultative des non-salariés | n° 15 du 22 février 1994 | 308-318 (art. 9 : p. 309) | couche texte, lisible (`1994/fr/Jo01594.pdf`) |
| Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories de travailleurs dans les secteurs agricole et non agricole | écart : liste des publics incomplète (catégorie b, agents de l'État, des collectivités locales et des EPA non couverts par un autre régime) | n° 22 du 15 mars 2002 | 603-606 | couche texte à police décalée de 29, se décode (`2002/fr/Jo0222002.pdf`, § 5 de `outillage-sources.md`) |
| Décret gouvernemental n° 2019-379 du 22 avril 2019, modifiant et complétant le décret n° 2002-916 du 22 avril 2002 | écart : ne vise pas les seules femmes rurales | n° 34 du 26 avril 2019 | 1277-1279 (éd. ar. : 1376-1378) | couche texte, lisible (`2019/fr/Jo0342019.pdf`, `2019/ar/Ja0342019.pdf`) ; **pas de notice propre dans `jort_cache.db`** |

Notes sur les sources :

- `jort_cache.db` donne pour le n° 66 de 1982 une publication au 19 octobre 1982, avant la signature
  du 21 octobre : le fascicule est daté « 19 - 22 Octobre 1982 » ; c'est cette date double qu'il
  faut écrire.
- Le décret n° 2019-379 n'a aucune notice à son numéro dans `jort_cache.db` (requêtes :
  `numero in ('2019-379','379')` en 2019 ; `titre like '%379%2019%'` en 2019 ; signatures du
  22 avril 2019). Il n'y est cité que dans l'intitulé arabe de l'arrêté du 19 juin 2019 (JORT n° 52,
  p. 2109-2110), qui fixe les pièces d'affiliation de ces travailleurs. Seconde voie : texte intégral
  des fascicules n° 33 à 36 de 2019, où il figure au n° 34 (sommaire et p. 1277). Ce n'est donc pas
  une recherche infructueuse ; aucune fiche `r-…` n'est à créer.
- La notice `decret2019-379` de `precis/fr/references.json` donne p. 1277-1278 : le décret court de
  la p. 1277 à la p. 1279 (lecture page par page du fascicule ; la ligne « N° 34 … Page N » est un
  pied de page). Elle n'a pas d'URL ; celle du fascicule
  français est `https://www.pist.tn/jort/2019/2019F/Jo0342019.pdf` (réponse HTTP 200 le
  3 novembre 2026).

## 2. Ce que disent les textes (citations)

**Loi n° 70-34**, art. 19, insérant l'art. 95-2 dans la loi n° 60-30 (p. 896) : « Doivent être
immatriculés les travailleurs salariés et les coopérateurs qui ont été occupés durant un minimum de
cent quatre vingt jours chez le même employeur agricole, durant une année avant la date de leur
immatriculation. » L'art. 95-3 permet d'étendre le régime par décret « à d'autres catégories de
travailleurs » et de réduire « la durée initiale du travail nécessaire pour l'immatriculation ». Le
mot « permanents » est celui de la thèse (p. 68), pas de la loi.

**Loi n° 81-6**, art. 2 (p. 265) : bénéficient du régime « les travailleurs salariés et les
coopérateurs exerçant les activités considérées comme agricoles au sens de l'article 3 du Code du
Travail », sans condition de durée. Art. 6, al. 3 (p. 266) et art. 18, al. 2 (p. 267) : « Toute
période de travail égale ou supérieure à 45 jours chez le même employeur est comptée pour un
trimestre. Toute période inférieure à 45 jours est négligée. » La thèse lit cette règle comme une
« durée minimale de cotisation » ramenée de 180 jours à 45 jours par trimestre ; la loi la pose comme
règle de décompte des trimestres de cotisation. Le décret n° 2019-379 confirme la portée pratique du
seuil : il définit les « ouvriers saisonniers et mobiles » comme ceux « employés par un seul
employeur de façon irrégulière et pour une période inférieure à 45 jours au titre d'un seul
trimestre ou ceux employés par plusieurs employeurs » (art. 2, art. 2 § f nouveau du décret
n° 2002-916, p. 1278).

**Décret n° 77-546**, art. 1er (p. 1655) : l'ensemble des régimes des lois n° 60-30 et 60-33 et du
décret n° 74-499 « est étendu aux pêcheurs, aux patrons pêcheurs même propriétaires de leur barque
ainsi qu'aux armateurs travaillant sur un bateau de pêche dont ils assurent l'équipement », ainsi
qu'aux petits armateurs de l'art. 65 du code du pêcheur. Assiette forfaitaire (SMIG × coefficients)
pour les bateaux de moins de trente tonneaux, rémunération réelle au-delà (art. 3-4, p. 1656).
Modifié par le décret n° 82-1026 du 8 juillet 1982 (JORT n° 50 des 13 et 16 juillet 1982, p. 1579,
d'après le rectificatif publié au n° 66 de 1982, p. 2197 ; non relu).

**Décret n° 82-1359**, art. 1er-2 (p. 2192-2193) : extension des régimes de la loi n° 60-30 et du
décret n° 74-499 aux « artisans, commerçants, industriels, médecins et pharmaciens » non affiliés à
un régime légal couvrant les mêmes risques ; est travailleur indépendant « toute personne exerçant à
titre principal une activité professionnelle pour son propre compte ». Art. 4, dernier al.
(p. 2193) : « pour les assurés cotisant aux classes 1 5 et 6 [imprimé ainsi, sans virgule] telles
que déterminées à l'article 7 […], l'adhésion au régime des assurances sociales est facultative ». Effet : « à compter du 1er juillet 1982 » (art. 26,
p. 2195).

**Décret n° 82-1360**, art. 1er (p. 2195) : les régimes de la loi n° 81-6 « sont étendus […] aux
travailleurs indépendants, métayers et tous exploitants se livrant par eux-mêmes aux activités
agricoles ». Effet : « à compter du 1er juillet 1982 » (art. 18, p. 2197).

**Décret n° 95-1166**, art. 1er-2 (p. 1486) : extension des articles 68 à 98, 100 à 107, 109 à 120
de la loi n° 60-30 et 20 à 38, 46 à 52, 54 et 57 du décret n° 74-499 « aux travailleurs non salariés
des secteurs agricole et non agricole » ; s'applique aussi « aux travailleurs du secteur de
l'artisanat, titulaires d'une carte professionnelle, ainsi qu'au métayers ». Art. 39 (p. 1489) :
« Sont abrogées toutes dispositions antérieures contraires et notamment les décrets susvisés
n° 82-1359 et n° 82-1360 du 21 octobre 1982. » Le décret ne contient aucune disposition sur les
accidents du travail.

**Loi n° 94-28**, section II « L'affiliation facultative », art. 9 (p. 309) : « Les non salariés
ainsi que les membres de leurs familles travaillant avec eux dans l'entreprise, peuvent adhérer à la
Caisse Nationale pour bénéficier de la législation relative aux accidents du travail dont ils
viendraient à être victimes. » La thèse (p. 74) écrit que, dans le RTNS,
« l'adhésion au régime des accidents de travail et des maladies professionnelles reste
facultative », sans citer la loi n° 94-28.

**Loi n° 2002-32**, art. 1er (p. 603) : régime « spécifique » (soins, pensions de vieillesse,
d'invalidité et de survivants) applicable aux : a) employés de maison ; b) « personnes employées par
l'Etat, les collectivités locales et les établissements publics à caractère administratif qui ne
sont pas couvertes par un autre régime légal de sécurité sociale, suivant des modalités fixées par
décret » ; c) pêcheurs sur bateaux de 5 tonneaux de jauge brute au plus, pêcheurs indépendants,
petits armateurs ; d) agriculteurs pour leur propre compte sur 5 ha en sec ou 1 ha en irrigué au
plus ; e) artisans travaillant à la pièce. Art. 2 : option des catégories c, d et e entre ce régime
et leur régime propre. Art. 7 : 7,5 % sur les deux tiers du SMAG (b, c, d) ou du SMIG (a, e). Le
décret n° 2002-916 (JORT n° 35 du 30 avril 2002 ; p. 1058-1061 d'après `jort_cache` et la notice
`decret2002-916`, pages non relues ici), art. 2 b, limite la catégorie b aux
personnes qui perçoivent « un montant mensuel au moins égal au salaire minimum agricole garanti,
rapporté à une durée d'occupation de 25 jours par mois », et ajoute les « petits éleveurs » au d.

**Décret gouvernemental n° 2019-379**, art. 2 (p. 1278 ; le titre et les visas sont p. 1277) : ajoute à l'art. 2 du décret n° 2002-916
un paragraphe f : « Les femmes récoltant les huîtres et les ouvriers saisonniers et mobiles
appartenant au milieu rural et travaillant dans le secteur agricole y compris la femme employée dans
ce secteur » (éd. arabe : « النساء الجامعات للمحار », soit les femmes ramassant les coquillages).
Ces personnes paient « la totalité du montant des cotisations dues » (art. 16 dernier al. nouveau,
p. 1279), sur les deux tiers du SMAG (art. 13 b nouveau) ; affiliation et paiement possibles par
d'autres organismes sous convention, avec le ministère des technologies de la communication
(art. 10 § 2, p. 1278, et 19 § 2, p. 1279) ; art. 3 (p. 1279) : elles peuvent s'affilier au régime des accidents du
travail. Pas de date d'effet dans le texte.

## 3. Écarts à corriger dans le chapitre

Les numéros de page de la thèse dans la colonne « Page » du tableau concordent avec les folios
imprimés (vérifié pour p. 68, 69, 73, 74, 75, 76 et 84).

1. Ligne 11, colonne « Texte rapporté par la thèse » : « loi n° 70-34 de 1970 » → date complète :
   « loi n° 70-34 du 9 juillet 1970 » (JORT n° 34 des 10-14 juillet 1970, p. 894-897). Clé
   `loi70-34` à copier dans `informel/references.json` ou `precis/fr/references.json` si le chapitre
   la cite.
2. Ligne 11, colonne « Ce qu'il ouvre » : « permanents d'au moins 180 jours par an chez le même
   employeur en 1970 ; 45 jours de travail par trimestre chez le même employeur depuis 1981 ». La loi
   de 1970 exige 180 jours « chez le même employeur agricole, durant une année avant la date de leur
   immatriculation » (art. 95-2) ; la loi n° 81-6 ouvre le régime à tous les salariés agricoles
   (art. 2) et compte pour un trimestre toute période d'au moins 45 jours chez le même employeur,
   les périodes plus courtes étant négligées (art. 6 et 18). Proposition : « immatriculation après
   180 jours de travail chez le même employeur agricole dans l'année (1970) ; depuis 1981, tous les
   salariés agricoles, un trimestre n'étant compté qu'à partir de 45 jours de travail chez le même
   employeur ». Ou garder la formule de la thèse en la lui attribuant explicitement.
3. Ligne 13 : « décrets n° 82-1359 et n° 82-1360 du 21 octobre 1982 ; décret n° 95-1166 du 3 juillet
   1995 | régime des travailleurs non salariés ; accidents du travail facultatifs ». (a) Le décret
   n° 95-1166 abroge les deux décrets de 1982 (art. 39) : les deux régimes de 1982 sont remplacés par
   un régime unique, ce que la ligne ne dit pas. (b) L'affiliation facultative aux accidents du
   travail vient de la loi n° 94-28 du 21 février 1994, art. 9 (JORT n° 15 du 22 février 1994,
   p. 309), non du décret n° 95-1166, qui n'en parle pas. Ajouter la loi n° 94-28 (clé `loi94-28`)
   dans la colonne des textes ou dans la cellule.
4. Ligne 14, colonne « Public » : « Petits agriculteurs et pêcheurs, employés de maison, artisans à
   la pièce ». La loi n° 2002-32 vise aussi (art. 1er b) les personnes employées par l'État, les
   collectivités locales et les EPA non couvertes par un autre régime ; le décret n° 2002-916 les
   limite à celles qui perçoivent au moins le SMAG sur 25 jours par mois. À ajouter.
5. Ligne 14, colonne « Ce qu'il ouvre » : « extension aux femmes rurales en emploi mobile et
   saisonnier ». Le décret n° 2019-379 vise « les femmes récoltant les huîtres et les ouvriers
   saisonniers et mobiles appartenant au milieu rural et travaillant dans le secteur agricole y
   compris la femme employée dans ce secteur » — hommes et femmes, plus les ramasseuses de
   coquillages. Proposition : « extension aux ramasseuses de coquillages et aux ouvriers agricoles
   saisonniers et mobiles du milieu rural (moins de 45 jours par trimestre chez un même employeur, ou
   plusieurs employeurs) ». Le chapitre « Cotisations sociales » (`_regimes.qmd`, l. 261) le dit
   déjà dans ces termes. Préciser aussi que le décret de 2019 modifie le décret n° 2002-916, pas la
   loi.
6. Ligne 18 : « Les travailleurs des chantiers régionaux ne sont pas couverts ». Ce n'est pas un
   écart à corriger mais un point à rapprocher : la catégorie b de la loi n° 2002-32 couvre en droit
   les personnes employées par l'État non couvertes ailleurs, sous condition de rémunération (décret
   n° 2002-916, art. 2 b). Le chapitre attribue l'affirmation à l'auteur ; si on la garde, la
   condition de rémunération est probablement ce qui exclut ces travailleurs, mais aucun texte lu ici
   ne le dit. <!-- à vérifier : rémunération des travailleurs des chantiers, texte applicable -->

Hors chapitre, relevé en passant : `prestations_sociales/_matrice.qmd` (l. 55 et 69) rattache
l'accident du travail des non-salariés à « loi n° 94-28, art. 4 » ; l'affiliation facultative des
non-salariés est à l'art. 9 (l'art. 4 fixe le champ des salariés, où l'employé de maison est cité).
À vérifier par le rédacteur de ce livre.

## 4. Backlog (proposé, à appliquer par `archiviste-backlog`)

- Informel, `_couverture.qmd` : références de loi vérifiées au JORT le 3 novembre 2026 (note
  `docs/notes/informel-verification-lois-couverture-2026-11-03.md`) ; écarts 1 à 5 à corriger ;
  point 6 (chantiers régionaux) à rapprocher de la loi n° 2002-32, art. 1er b.
- Tous les textes sont au corpus et lisibles (scans 1970-1982 à l'image, 2002 par décodage du
  décalage) ; aucun OCR requis pour le chapitre.
- `precis/fr/references.json`, clé `decret2019-379` : pages 1277-1278 → 1277-1279 (le décret finit
  p. 1279 : art. 12, 16 et 19 nouveaux, art. 3 et 4, signatures) ; URL pist.tn à ajouter
  (`https://www.pist.tn/jort/2019/2019F/Jo0342019.pdf`). Même correction dans les autres
  `references.json` qui porteraient la clé.

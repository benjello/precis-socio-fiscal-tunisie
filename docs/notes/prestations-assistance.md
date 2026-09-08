# Assistance sociale non contributive — dossier documentaire

> Note **documentaire** pour la partie 1.3 du livre « Prestations sociales »
> (`docs/notes/prestations-sociales-plan.md`, §2). Elle ne rédige aucune prose de précis et n'a
> modifié aucun fichier de `precis/`.
>
> **Trois dates par texte** : (1) signature, (2) publication au JORT avec numéro et page,
> (3) effet tel que l'énonce l'article. Chaque énoncé porte la mention **attesté** (lu sur le
> texte officiel, JORT français) ou **dérivé** (déduit d'un autre texte ou d'un intitulé de
> `jort_cache`).
>
> **Outillage.** `www.pist.tn` présente un certificat TLS expiré : toutes les URL ci-dessous ont
> été vérifiées par `curl -sk` avec contrôle de la taille (un 404 fait **289 octets**). Convention
> confirmée : `https://www.pist.tn/jort/<année>/<année>F/Jo<n° sur 3 chiffres><année>.pdf`,
> **2 chiffres d'année jusqu'en 1999**, **4 chiffres à partir de 2000**.
> **Piège rencontré** : pour `2025F/Jo1482025.pdf` et `2025F/Jo0882025.pdf`, l'URL en « F »
> renvoie un HTTP 200 mais **sert le fascicule arabe** — la vérification par taille ne suffit
> pas, il faut lire le contenu.
>
> Les textes antérieurs à 1990 ont été **océrisés pour cette note**
> (`ocrmypdf -l fra --skip-text` puis `pdftotext -raw`) ; les citations littérales ci-dessous ont
> été relues et les coquilles d'OCR sont signalées.

---

## 0. Résultats principaux

**R1 — Le PNAFN est nommé au JORT, mais uniquement par des textes de financement.**
Le résultat négatif transmis au documentaliste (« aucune ligne de `jort_cache` ne porte
l'intitulé du programme ») est **inexact tel qu'énoncé**, et doit être reformulé. Trois titres
portent l'intitulé, en toutes lettres :

- l'**arrêté du 6 janvier 1987** : « … au financement du **programme national d'aide aux
  familles nécessiteuses** » ;
- la **loi n° 86-83**, art. 13 : « contribution des organismes de sécurité sociale pour l'aide
  aux familles nécessiteuses » ;
- la **loi n° 87-83**, art. 67 : « la contribution des caisses de sécurité sociale au **programme
  des familles nécessiteuses** ».

Le résultat qui tient — et qui est plus fort parce qu'il survit à la vérification — est celui-ci :

> **Aucun texte ne crée le PNAFN, n'en fixe l'objet, les conditions d'éligibilité ni le montant.
> Le programme n'apparaît au JORT qu'en qualité d'objet de dépense**, dans des lois de finances,
> des arrêtés de financement et, à partir de 1998, comme *source de listes* pour d'autres
> dispositifs. La loi n° 86-83 le mentionne d'ailleurs comme **déjà existant** : elle autorise les
> caisses « à participer au financement du programme national d'aide aux familles nécessiteuses »,
> sans le créer.

Vérification NULL-safe refaite pour cette note (voir §6.1) : sur 78 953 textes, **six** lignes
seulement portent l'intitulé ou sa forme arabe, dont deux postérieures à 2014.

**R2 — Les onze paliers du paramètre openfisca `pnafn/allocation` n'ont pas de texte, et il est
possible de le démontrer plutôt que de le supposer.** Le balayage exhaustif des arrêtés du
ministère des Affaires sociales de 1986 à 2020 portant sur un « montant », un « octroi » ou une
« aide » (§6.2) ne fait apparaître **aucun** arrêté fixant l'allocation du PNAFN — alors qu'il en
existe pour le prix du progrès social, le prix du travailleur exemplaire, l'aide matérielle aux
personnes âgées nécessiteuses (1997), l'aide à la famille d'accueil (1997, 90 D/mois) et l'aide à
la personne handicapée nécessiteuse (2006, modifiée 2017). **La forme juridique existait donc et
n'a pas été employée pour le PNAFN.**

Preuve directe supplémentaire, sur pièce : l'**arrêté du 30 septembre 1997** fixant l'aide aux
personnes âgées nécessiteuses **refuse d'énoncer un chiffre** et renvoie au montant administratif :

> « **Art. 2.** — Le montant de l'aide matérielle mentionnée à l'article 19 de la loi du
> 31 octobre 1994, est **celui servi dans le cadre du programme d'aide aux personnes âgées à
> domicile**. » (JORT n° 81 du 10 octobre 1997, p. 1867)

C'est le seul cas rencontré où un arrêté publié dit explicitement que le barème réside ailleurs
que dans un texte. Les paliers de 1987 à 2018 relèvent donc de **décisions administratives
(circulaires, notes de la direction générale de la promotion sociale, arbitrages budgétaires)** —
ce que corrobore la forme même des valeurs encodées : 53,333 / 56,666 / 63,333 D sont des
conversions mensuelles de montants **trimestriels** de 160, 170 et 190 D, forme d'un document de
gestion et non d'un article de texte.

**R3 — Le palier 180 D est confirmé sur texte, et sa fin est datée.** L'**arrêté conjoint du
10 juillet 2024** est le premier texte publié à énoncer le montant de l'allocation PNAFN :

> « **Article premier** — L'allocation monétaire mensuelle attribuée aux catégories pauvres
> conformément à la législation et à la règlementation en vigueur, **fixée à 180 dinars à la date
> de la publication du présent arrêté conjoint**, est augmentée sans que le montant de cette
> allocation ne dépasse le montant des transferts monétaires mensuels directs attribués dans le
> cadre du programme « AMEN SOCIAL », fixée à 240 dinars. »
> (JORT n° 86 du 10 juillet 2024, p. 1844)

Deux conséquences documentaires :
1. le palier `2018-04-01: 180` d'openfisca est **exact et a duré jusqu'en juillet 2024** — la
   série ne s'arrête pas prématurément, elle est simplement à prolonger ;
2. l'arrêté **ne fixe pas un nouveau montant** : il autorise un relèvement **plafonné** au niveau
   du transfert AMEN. Encoder « 240 D au 10 juillet 2024 » serait une sur-interprétation ; la
   formulation correcte est « allocation alignée par le haut sur le transfert AMEN, dans la limite
   de 240 D ». L'arrêté conjoint du **29 août 2025** reprend la même mécanique avec 240 → 260 D,
   avec **effet rétroactif au 1er janvier 2025**.

**R4 — Le PNAFN n'a jamais été formellement abrogé.** L'article 23 de la loi organique n° 2019-10
dispose que « les programmes d'aides sociales en vigueur à la date de promulgation de la présente
loi **demeurent exécutoires jusqu'à leur adaptation** avec les dispositions de la présente loi ».
Les arrêtés de 2024 et 2025 traitent encore, sept ans après, l'allocation PNAFN et le transfert
AMEN comme **deux séries distinctes**, la première rattrapant la seconde. Le livre doit donc
présenter 2019 comme une **superposition**, non comme un remplacement.

**R5 — L'Agence nationale d'intégration et de développement social n'existe pas.** L'article 6 de
la loi organique n° 2019-10 prévoit sa création par décret gouvernemental ; l'article 5 prévoit un
Conseil supérieur de la solidarité sociale. **Aucun texte ne les crée** dans `jort_cache` (recherche
en français et sur les formes arabes `الوكالة الوطنية للإدماج` et `المجلس الأعلى للتنمية الاجتماعية`,
couverture jusqu'à décembre 2025). Le décret gouvernemental n° 2020-317, art. 29, prend acte de
cette carence : « Les services compétents du ministère des affaires sociales **continuent à gérer**
le programme AMEN SOCIAL **jusqu'à la création** et la mise en place de l'Agence ». C'est un
résultat négatif solide et publiable.

**R6 — La création par voie budgétaire n'a pas cessé en 1986 : elle est le mode ordinaire.**
Les lois de finances 2025 et 2026 continuent d'ajouter des prestations catégorielles au périmètre
AMEN sans passer par la loi organique (§4.4).

---

## 1. Le PNAFN (1986 → )

### 1.1 Les textes de financement

**(a) Loi n° 86-83 du 1er septembre 1986, portant loi de finances rectificative pour la gestion
1986, article 13 — *attesté*, OCR relu.**

- Signature : 1er septembre 1986.
- Publication : **JORT n° 48 du 2 septembre 1986** (tome 129), **page 928**.
- Effet : gestion 1986.
- Local : `PDFs/JORT/1986/fr/Jo04886.pdf` — URL vérifiée (3 431 067 o) :
  `https://www.pist.tn/jort/1986/1986F/Jo04886.pdf`
- Rubrique du chapitre 3 « Dispositions diverses » : « **Contribution des organismes de sécurité
  sociale pour l'aide aux familles nécessiteuses** ».

> « **Art. 13.** — Les organismes de sécurité sociale, y compris la caisse de retraite du
> personnel des services publics de l'électricité, du gaz et du transport **sont autorisés à
> participer au financement du programme national d'aide aux familles nécessiteuses**.
> La contribution annuelle de chaque organisme sera fixée par arrêté conjoint des ministres des
> affaires sociales et du plan et des finances. »

**Point de méthode à porter au rédacteur** : le verbe est « sont autorisés à participer au
financement **du** programme », avec article défini. Le programme est **présupposé existant** en
septembre 1986. La loi de finances rectificative n'est donc pas l'acte de naissance du PNAFN mais
la première **trace** de son existence au Journal officiel.

**(b) Arrêté des ministres du plan et des finances et des affaires sociales du 6 janvier 1987 —
*attesté*, OCR relu.**

- Signature : 6 janvier 1987.
- Publication : **JORT n° 4 du 16 janvier 1987** (tome 130), **page 65**.
- Effet : gestion 1986 (rétroactif).
- Local : `PDFs/JORT/1987/fr/Jo00487.pdf` — URL vérifiée (6 889 492 o) :
  `https://www.pist.tn/jort/1987/1987F/Jo00487.pdf`
- Attention : `jort_cache` attribue ce texte au seul « ministre des Affaires Sociales » et lui
  donne un `numero` NULL. Le texte publié est signé **conjointement** par Ismaïl Khelil (plan et
  finances) et Abdelaziz Ben Dhia (affaires sociales), vu par le Premier ministre Rachid Sfar.

> « **Article premier.** — La contribution de la **caisse nationale de retraite et de prévoyance
> sociale** au financement du programme national d'aide aux familles nécessiteuses **pour l'année
> 1986** est fixée à un montant de **4.000.000 dinars**.
> **Art. 2.** — La contribution de la **caisse nationale de sécurité sociale** … est fixée à un
> montant de **4.000.000 dinars**. »

Soit **8 millions de dinars** pour 1986, à parts égales CNRPS / CNSS.

**(c) Loi n° 87-83 du 31 décembre 1987, portant loi de finances pour la gestion 1988,
article 67 — *attesté*, OCR relu.**

- Signature : 31 décembre 1987.
- Publication : **JORT n° 91 du 29-31 décembre 1987** (tome 130), **page 1634** (l'article 66
  figure p. 1633-1634).
- Effet : gestion 1988.
- Local : `PDFs/JORT/1987/fr/Jo09187.pdf` — URL vérifiée (9 505 156 o) :
  `https://www.pist.tn/jort/1987/1987F/Jo09187.pdf`

> « **La contribution des caisses de sécurité sociale au programme des familles nécessiteuses**
> — **Article 67** — Dans le cadre du financement du programme national des familles nécessiteuses,
> un montant de **2.500.000 dinars est recouvré annuellement au profit du budget général de
> l'État**, provenant des organismes de sécurité sociale y compris la caisse de retraite des
> employés des services publics de l'électricité et du gaz et du transport et des revenus
> résultant de la **contribution complémentaire des employeurs instituée par l'article 57 de la loi
> n° 74-101 du 25 décembre 1974** portant loi de finances pour la gestion 1975.
> La contribution de chaque organisme sera fixée **par arrêté du Premier ministre**. »

Trois faits importants, tous **attestés** :
1. la contribution passe de 8 MD (1986, exceptionnel) à **2,5 MD par an, pérennisés** ;
2. le produit est **recouvré au profit du budget général de l'État** — le PNAFN n'a pas de caisse
   ni de fonds propre : il est une **ligne de dépense budgétaire alimentée par une recette
   affectée aux caisses** ;
3. l'autorité de répartition change : d'arrêté conjoint (1986) à **arrêté du Premier ministre**
   (1988). **Aucun arrêté du Premier ministre portant cette répartition n'a été trouvé** dans
   `jort_cache` — à signaler comme lacune (§7).

La ligne de recette correspondante figure au tableau des voies et moyens du même fascicule
(p. 1640), sous le libellé « **62-13 Contribution des organismes de sécurité sociale au programme
des familles nécessiteuses et du fonds de collecte de la contribution patronale additionnelle de
0.5 MD (LF 1975) …… 2.500.000** ». C'est, à ce jour, **la seule imputation budgétaire nommée du
PNAFN retrouvée sur texte**.

### 1.2 Le PNAFN comme fournisseur de listes (1998, 2012)

Le PNAFN n'a pas de conditions d'éligibilité publiées ; **ce sont les textes de l'aide médicale
qui décrivent, indirectement, sa population**. Deux citations, toutes deux *attestées* :

- **Décret n° 98-1812, art. 5** (JORT n° 78 de 1998, p. 1975-1976) : la première liste des
  bénéficiaires de la carte de soins gratuits « doit tenir compte des **listes nominatives des
  bénéficiaires des aides permanentes dans le cadre des programmes nationaux d'aide aux
  nécessiteux**, des handicapés dont le revenu est limité et qui sont incapables de travailler, des
  personnes âgées nécessiteuses et des enfants inscrits à l'institut national de la protection de
  l'enfance ». (Pluriel « programmes nationaux » : le texte de 1998 ne connaît pas encore
  l'acronyme.)
- **Décret n° 2012-2521 du 16 octobre 2012, art. 5 (nouveau)** (JORT n° 84 du 23 octobre 2012,
  p. 2627) : la liste des éligibles à la carte de soins gratuits « est élaborée au vu des listes
  des bénéficiaires et des éligibles aux **aides monétaires directes accordées dans le cadre du
  programme national d'aide aux familles nécessiteuses** ».

**C'est la seule occurrence du PNAFN dans le *corps* d'un texte normatif** (et non dans un
intitulé de ligne budgétaire) rencontrée dans tout le dépouillement. Elle est datée de **2012**,
soit vingt-six ans après la première trace budgétaire. À citer comme telle.

### 1.3 La banque de données (2014, 2018)

**Décret n° 2014-1526 du 30 avril 2014** portant création d'une unité de gestion par objectifs au
ministère des affaires sociales pour la réalisation du projet d'instauration d'une **banque de
données sur les familles nécessiteuses et à revenu limité** — *attesté* (texte français intégral
au miroir, `dec_2014_1526_2014.md`, 156 l.).

- Signature : 30 avril 2014 ; publication : **JORT n° 38 du 13 mai 2014, p. 1159-1161** ;
  durée d'exécution du projet : **quatre ans** en quatre étapes (art. 3).
- URL vérifiée (620 992 o) : `https://www.pist.tn/jort/2014/2014F/Jo0382014.pdf`

**Décret gouvernemental n° 2018-626 du 26 juillet 2018** modifiant le précédent — *dérivé*
(seul l'intitulé arabe est disponible dans `jort_cache` ; le miroir n'a pas de version française,
et **l'année 2018 est l'une des trois années mal couvertes du corpus français**).

- Publication : **JORT n° 63 de 2018** ; page **non renseignée** dans `jort_cache`.
- URL vérifiée (3 413 193 o) : `https://www.pist.tn/jort/2018/2018F/Jo0632018.pdf`
- **TODO** : lire le fascicule pour établir l'objet exact de la modification (probablement
  prorogation de la durée du projet, arrivée à échéance en 2018) et la page.

Cette banque de données est l'ancêtre direct du « registre de données sur les catégories pauvres
et les catégories à revenu limité » de l'article 18 de la loi organique de 2019.

### 1.4 Le montant de l'allocation

**Aucun texte n'établit les paliers 1987-2018.** Voir R2. Ce qui *est* établi sur texte :

| Date d'effet | Montant | Statut | Texte |
|---|---|---|---|
| 1987 → 2024-07 | 7,7 D … 180 D (11 paliers) | **non établi** | aucun — décisions administratives |
| au 10 juillet 2024 | **180 D** (constat) | **attesté** | arrêté conjoint du 10 juillet 2024, art. 1er |
| à compter du 10 juillet 2024 | relèvement **plafonné à 240 D** | **attesté** | *idem* |
| à compter du 1er janvier 2025 | relèvement **plafonné à 260 D** | **attesté** | arrêté conjoint du 29 août 2025, art. 1er et 2 |

- Arrêté conjoint du **10 juillet 2024** : JORT n° 86 du **10 juillet 2024**, **p. 1844**.
  URL vérifiée (729 033 o) : `https://www.pist.tn/jort/2024/2024F/Jo0862024.pdf`
  Art. 3 : le coût est **imputé sur le budget de l'État** ; CNSS et CNRPS adressent aux ministères
  des « **décomptes périodiques chaque trois mois** » — trace persistante du versement trimestriel.
- Arrêté conjoint du **29 août 2025** : JORT n° 107 du **29 août 2025**, **p. 2138**.
  URL vérifiée (1 240 844 o) : `https://www.pist.tn/jort/2025/2025F/Jo1072025.pdf`
  Art. 2 : « Le présent arrêté entre en application **à compter du 1er janvier 2025** » —
  rétroactivité de huit mois, à signaler.

---

## 2. L'aide médicale : de l'AMG de 1987 aux AMG1 / AMG2

### 2.1 Le régime de 1987-1988

**Loi n° 87-29 du 12 juin 1987 relative au régime de l'assistance médicale gratuite —
*attesté*, OCR relu.**

- Signature : **12 juin 1987** (le texte imprimé porte « Fait à Mornag, le 12 juin **1986** » :
  coquille de l'imprimeur ou de l'OCR ; la date de la loi, son numéro dans la série 87 et les
  travaux préparatoires du **9 juin 1987** établissent 1987).
- Publication : **JORT n° 43 du 16 juin 1987** (tome 130), **page 767**.
- Effet : **« Art. 4. — La présente loi et les textes réglementaires y afférents prennent effet à
  compter du 1er janvier 1988. »**
- URL vérifiée (2 047 050 o) : `https://www.pist.tn/jort/1987/1987F/Jo04387.pdf`

Contenu (4 articles) :

> « **Article premier.** — Le bénéfice de l'assistance médicale gratuite dans les établissements
> publics hospitaliers et sanitaires relevant du ministère de la santé publique est accordé aux
> titulaires de **livrets de soins** délivrés par les services du ministère de la santé publique.
> **Il est institué deux catégories de livrets d'assistance médicale gratuite. Ils sont délivrés en
> fonction du revenu de la famille** … »
> « **Art. 2.** — Il est créé un **droit annuel d'affiliation** … dont le montant et les modalités
> de perception sont fixés **en vertu de la loi de finances**. Les titulaires de livrets … **de
> première catégorie sont exonérés** du paiement de ces droits. »
> « **Art. 3.** — Les bénéficiaires … sont assujettis au paiement d'une **contribution aux frais de
> soins et d'hospitalisation** … fixée en vertu de la loi de finances. »

Abrogations expresses (art. 4) : art. 27 et 28 (§ 1er, 2e al.) de la loi n° 69-2 du 20 janvier 1969
relative à l'organisation sanitaire, modifiés par la loi n° 81-12 du 2 mars 1981 ; art. 105 de la
loi n° 82-91 du 30 décembre 1982 (LF 1983) modifié par l'art. 56 de la loi n° 85-109 (LF 1986).

**Correction majeure à porter au plan et au rédacteur** : **la dualité AMG1 / AMG2 date de 1987,
pas de 1998.** L'article 1er institue déjà « deux catégories de livrets », différenciées par le
revenu, la première gratuite et la seconde payante. Ce que fait 1998, c'est **remplacer le livret
par une carte** et **refondre les deux catégories dans deux décrets distincts**, en changeant le
vocabulaire (« carte de soins gratuits » / « carte de soins à tarifs réduits »). Présenter 1998
comme une « bascule vers AMG1 et AMG2 » serait inexact.

**Décret n° 88-175 du 6 février 1988 relatif aux conditions et modalités d'attribution des
livrets d'assistance médicale gratuite — *attesté*, OCR relu.**

- Signature : 6 février 1988 ; publication : **JORT n° 14 du 23-26 février 1988** (tome 131),
  **p. 281-282** ; effet : régime en vigueur au 1er janvier 1988 (loi 87-29, art. 4).
- URL vérifiée (3 343 782 o) : `https://www.pist.tn/jort/1988/1988F/Jo01488.pdf`

**Condition de ressources — la seule publiée pour cette période :**

> « **Art. 1er.** — Ne peuvent bénéficier de l'assistance médicale gratuite que les personnes
> justifiant d'un **revenu familial annuel égal ou inférieur au salaire minimum
> inter-professionnel garanti**.
> La liste des bénéficiaires de la première ou de la deuxième catégorie de livrets de soins est
> arrêtée par les **commissions régionales** d'attribution, sur proposition des **commissions
> locales**, selon des **critères fixés par la commission nationale de l'assistance médicale
> gratuite** visée à l'article 11. »

Le partage AMG1 / AMG2 relève donc de **critères non publiés**, fixés par une commission
administrative — même mécanique que pour le montant du PNAFN.

Autres éléments *attestés* : dossier (art. 2, dont déclaration sur l'honneur de non-couverture par
un régime de sécurité sociale) ; commission locale par délégation présidée par le délégué et
comprenant le secrétaire général de circonscription du **parti socialiste destourien** et le
président de la cellule destourienne (art. 4) ; commission régionale présidée par le gouverneur
(art. 6) ; **durée de validité du livret : cinq ans**, renouvellement à demander six mois avant
échéance (art. 9) ; commission nationale présidée par le ministre de la santé publique, où siègent
le PSD, l'UGTT, l'UNFT, l'UTICA et l'UNA (art. 11).

**Décret n° 88-917 du 6 mai 1988** modifiant le décret n° 88-175 — *dérivé* (intitulé
`jort_cache`). JORT n° 34 de 1988, p. 755-756. **TODO** : objet à établir (le fascicule n'a pas été
océrisé pour cette note).

**Le droit annuel d'affiliation et la contribution aux frais de soins — loi n° 87-83 (LF 1988),
articles 62 à 65 — *attesté*, OCR relu** (JORT n° 91 de 1987, p. 1633-1634) :

> « **Article 62** — Le taux du droit annuel d'affiliation au régime de l'assistance médicale
> gratuite est fixé à **six (6) dinars** pour les bénéficiaires du **livret de soins gratuits de la
> 2ème catégorie**. »
> « **Article 63** — Le règlement du droit annuel … confère au livret une **validité générale**
> auprès de l'ensemble des établissements … Le non paiement … entraîne la **suspension des effets
> du livret et son retrait provisoire**. »
> « **Article 64** — La contribution aux frais de soins et d'hospitalisation … est due par les
> bénéficiaires des livrets … de la **deuxième catégorie** … Ne sont pas assujetties à cette
> contribution : … — les personnes titulaires d'un livret … de la **première catégorie**. »
> « **Article 65** — Le montant de la dite contribution est fixé comme suit : — **300 millimes**
> pour toute consultation externe dans les dispensaires ; — **500 millimes** … dans les hôpitaux de
> circonscription ; — **1 dinar** … dans les hôpitaux régionaux, principaux, universitaires ou
> centres et instituts spécialisés ; — **5 dinars** pour chaque hospitalisation de médecine
> générale, de gynécologie obstétrique et de spécialités médicales ; — **10 dinars** pour chaque
> hospitalisation de chirurgie ou spécialités chirurgicales. »

**Arrêté du ministre de la santé publique du 17 février 1988** relatif aux modalités de paiement
du droit annuel d'affiliation — *attesté*, OCR relu. JORT n° 14 de 1988, **p. 284**. Paiement en
une seule tranche en janvier, ou, sur autorisation du directeur de l'établissement, « en **deux
tranches égales de trois (3) dinars** chacune » (janvier et juillet).

**Loi n° 90-111 du 31 décembre 1990, portant loi de finances pour la gestion 1991, articles 65 et
66 — *attesté*, OCR relu.** Signature et publication : **31 décembre 1990** ; **JORT n° 86 du
28-31 décembre 1990**, **p. 2056** ; effet : gestion 1991. URL vérifiée :
`https://www.pist.tn/jort/1990/1990F/Jo08690.pdf`. Rubrique : « **Aménagement du droit annuel
d'affiliation au régime de l'assistance médicale gratuite et de la contribution aux frais de
soins** ».

> « **ARTICLE 65** : Est modifié l'article 62 de la loi n° 87-83 … ainsi qu'il suit :
> *Art. 62 (nouveau)* : Le taux du droit annuel d'affiliation au régime de l'assistance médicale
> gratuite est fixé à **dix (10) dinars** pour les bénéficiaires du livret de soins gratuits de la
> 2ème catégorie. … »
> « **ARTICLE 66** : Est modifié le paragraphe premier de l'article 65 de la loi n° 87-83 … :
> — **400 millimes** … dispensaires ; — **700 millimes** … hôpitaux de circonscription ;
> — **1,500 dinar** … hôpitaux régionaux, principaux ou centres et instituts spécialisés ;
> — **7 dinars** pour chaque hospitalisation … médecine générale, gynécologie obstétrique et
> spécialités médicales ; — **13 dinars** … chirurgie et spécialités chirurgicales.
> Le reste sans changement. »

**Le maillon manquant est établi** : le droit annuel d'affiliation passe de **6 D (1988) à 10 D
(1991)**, et les 10 dinars de la cotisation AMG2 du décret n° 98-409 de 1998 ne sont donc **pas une
création** mais la **reprise du taux en vigueur depuis sept ans**. Les contributions aux frais de
soins sont majorées d'environ un tiers dans le même mouvement.

### 2.2 L'étape intermédiaire de 1993-1994 (à ne pas omettre)

Deux décrets antérieurs à 1998 fixent déjà des tarifs réduits — *dérivés* (intitulés
`jort_cache`) :

- **Décret n° 93-529 du 1er mars 1993**, fixant les tarifs réduits de soins et d'hospitalisation
  institués au profit des structures sanitaires publiques (JORT n° 19 de 1993, p. 361-362) ;
- **Décret n° 94-1738 du 22 août 1994**, fixant les tarifs réduits et les contributions aux frais
  de soins et d'hospitalisation (JORT n° 68 de 1994, p. 1385) — **abrogé expressément par
  l'article 25 du décret n° 98-409** (*attesté*).

Le mécanisme des tarifs réduits ne naît donc pas en 1998 : il est **refondu** en 1998.

### 2.3 AMG1 — la carte de soins gratuits (décret n° 98-1812)

**Décret n° 98-1812 du 21 septembre 1998, fixant les conditions et les modalités d'attribution et
de retrait de la carte de soins gratuits — *attesté* (couche texte du fascicule).**

- Signature : 21 septembre 1998 ; publication : **JORT n° 78 du 29 septembre 1998**,
  **p. 1975-1976** ; visa : loi n° 91-63 du 29 juillet 1991 relative à l'organisation sanitaire,
  **article 35**.
- URL vérifiée (141 428 o) : `https://www.pist.tn/jort/1998/1998F/Jo07898.pdf`

**Éligibilité — *attesté*** : le décret **ne pose aucun seuil de revenu**. Il pose une condition
d'état (« tout tunisien **indigent**, à son conjoint et à ses enfants légalement à charge »,
art. 2) et surtout un **contingentement** :

> « La carte de soins gratuits est attribuée **dans la limite du nombre global de cartes … et des
> quotas régionaux qui sont fixés par arrêté conjoint des ministres des affaires sociales et de la
> santé publique** » (art. 2).

C'est le trait structurant de l'AMG1 : **une prestation à enveloppe fermée, contingentée par
gouvernorat**, et non un droit ouvert sous condition de ressources.

Ayants droit (art. 3) : conjoint ; enfants à charge jusqu'à la majorité, **ou jusqu'à la fin des
études sans dépasser 25 ans** ; enfants handicapés **jusqu'à ce qu'ils disposent de ressources** ;
la fille « tant qu'elle ne dispose pas de ressources ou qu'elle n'est pas à la charge du mari ».
Droits (art. 4) : gratuité totale, **sans aucune contribution ni cotisation**.
Commission régionale spéciale par gouvernorat (art. 5), présidée par le gouverneur, avec CNSS,
CNRPS, contrôleur régional des finances et comité régional de solidarité sociale.

**TODO** : **aucun arrêté conjoint fixant le nombre global de cartes et les quotas régionaux n'a
été trouvé** dans `jort_cache`. Si cette recherche est confirmée, c'est un troisième résultat
négatif du même ordre que R1 et R2 : le paramètre décisif de l'AMG1 n'est pas publié.

### 2.4 AMG2 — la carte de soins à tarifs réduits (décret n° 98-409)

**Décret n° 98-409 du 18 février 1998 — *attesté* (couche texte du fascicule).**

- Signature : 18 février 1998 ; publication : **JORT n° 17 du 27 février 1998**, **p. 405-408** ;
  visa : loi n° 91-63, **article 36**.
- URL vérifiée (206 615 o) : `https://www.pist.tn/jort/1998/1998F/Jo01798.pdf`

**Éligibilité — *attesté*, art. 2** (revenu **annuel** de la famille, exprimé en SMIG) :

| Taille de la famille | Plafond de revenu annuel |
|---|---|
| ≤ 2 personnes | 1 × SMIG |
| 3 à 5 personnes | 1,5 × SMIG |
| > 5 personnes | 2 × SMIG |

Membres pris en compte : « **le candidat et son conjoint et les enfants légalement à charge** ».
Condition supplémentaire : « le bénéficiaire … **ne doit pas être affilié à l'un des régimes de
sécurité sociale et sa situation ne lui permet pas l'affiliation** ». Contingentement identique à
l'AMG1 : nombre global de cartes et quotas régionaux fixés **par arrêté conjoint des ministres des
finances, des affaires sociales et de la santé publique**, sur proposition de la commission
nationale des tarifs réduits (art. 2 et 14).

**Cotisation et validité — *attesté*** :
- « **Art. 10.** — La cotisation annuelle … est fixé à **(10) dix dinars** », payable par carte et
  par an à la recette de l'établissement sanitaire du lieu de résidence ;
- non-paiement : suppression des effets de la carte, arriérés dus (art. 11) ;
- « **Art. 12.** — La validité de la carte … est fixée pour **(5) cinq ans** », validée
  annuellement par apposition du cachet.

**Correction à porter à openfisca** : le paramètre
`prestations/non_contributives/amg2.yaml` date la cotisation de 10 D au **2015-01-01**. La valeur
est juste, **la date est fausse de dix-sept ans** : elle est fixée par l'article 10 du décret
n° 98-409, **applicable à compter du 27 février 1998**. Aucune modification de cet article n'a été
trouvée dans la chaîne modificative (§2.5).

**Tarifs — *attesté*, art. 17, 18, 21, 22** :
- consultations, en pourcentage du tarif « malades payants » : **20 %** en centre de santé de base
  (médecine générale), **25 %** en hôpital de circonscription, **30 %** en hôpital régional
  (consultation de spécialité), **30 %** en établissement à vocation universitaire (consultation
  de maître de conférences) ;
- hospitalisation : **forfait égal au tarif d'une journée** de malade payant, **quelle que soit la
  durée du séjour** ; accompagnant : **moitié** du forfait, ou **tiers** sur prescription médicale ;
- explorations, actes chirurgicaux et actes de la nomenclature : **20 %** du tarif malades payants,
  **plafonné à 30 dinars** en tout état de cause ; **1 dinar par séance d'hémodialyse** ;
  prothèses et implants : **20 %** du prix coûtant, **plafonné à 50 dinars** ;
- arrondi : par tranche entière de **500 millimes**.

### 2.5 Les chaînes modificatives (1999 → 2022)

Toutes ces lignes sont **attestées** sauf mention contraire ; les textes postérieurs à 2000 sont
lus dans le miroir iort.tn (`data/iort/textes/md/`), ceux de 1999 restent à établir.

**Chaîne du décret n° 98-409 (AMG2)**

| Texte | Signature | JORT | Objet |
|---|---|---|---|
| Décret n° 99-1372 | 21 juin 1999 | n° 52, p. 1052-1053 | *dérivé* — objet à établir (**TODO**) ; visé par le décret 2004-2730 comme ayant modifié l'art. 24 |
| Décret n° 2004-2730 | 31 déc. 2004 | n° 1 (2005), p. 16-17 | art. 24 (nouveau) : validité des cartes délivrées en déc. 1999 et en 2000 **prolongée au 31 déc. 2005** |
| Décret n° 2005-2886 | 24 oct. 2005 | n° 86, p. 2911 | art. 2 (nouveau) : **ajoute les ascendants légalement à charge** au décompte des membres de la famille ; seuils inchangés |
| Décret n° 2009-1034 | 13 avril 2009 | n° 31, p. 1063 | art. 3 (nouveau) : **supprime la déclaration fiscale des revenus** des pièces exigées |
| Décret n° 2011-561 | 14 mai 2011 | n° 36, p. 730-731 | art. 24 (nouveau) : cartes de 2006 prolongées au **31 déc. 2011** |
| Décret n° 2012-2522 | 16 oct. 2012 | n° 84, p. 2628-2629 | art. 5 et 7 (nouveaux) : **dépolitisation des commissions** (le délégué et la municipalité cèdent la présidence au chef de l'unité locale de promotion sociale ; entrée de la CNAM et de la LTDH) ; art. 12 § 2 : **cartes annuelles renouvelables pour catégories spécifiques** (licenciés économiques proches de la retraite anticipée, licenciés de moins de 40 ans sans charge de famille après épuisement de la couverture de la loi n° 96-101 modifiée par la loi n° 2002-24, ascendants d'affiliés à un ou deux ans de 55 ans, saisonniers du bâtiment non déclarés de moins de 40 ans) |
| Décret gouv. n° 2016-111 | 25 janv. 2016 | n° 8, p. 252-253 | art. 24 (nouveau) : cartes de 2011 prolongées au **31 déc. 2016** |
| Décret gouv. n° 2016-1402 | 27 déc. 2016 | n° 105 | *dérivé* (intitulé arabe seul) — c'est **ce texte**, et non le n° 2016-111, que vise le décret 2020-476 comme dernier état de l'article 24 |
| Décret gouv. n° 2020-476 | 23 juil. 2020 | n° 74, p. 1638-1639 | cartes de 2011 à 2015 prolongées au **31 déc. 2020** |
| Décret gouv. n° 2021-66 | 12 janv. 2021 | n° 9, p. 250-251 | cartes de 2011 à 2016 prolongées au **31 déc. 2021** |
| Décret n° 2022-919, art. 20 | 29 nov. 2022 | n° 131, p. 3367-3368 | cartes gratuites **et** à tarif réduit délivrées **de 2011 à 2017** prolongées au **31 déc. 2022** |

**Chaîne du décret n° 98-1812 (AMG1)** — strictement parallèle :
décret n° 2004-2731 (31 déc. 2004, JORT n° 1 de 2005, p. 17) → décret n° 2011-560 (14 mai 2011,
JORT n° 36, p. 730 : art. 11 nouveau, cartes de 2006 prolongées au 31 déc. 2011) → décret
n° 2012-2521 (16 oct. 2012, JORT n° 84, p. 2627 : art. 5 nouveau, commission régionale et **renvoi
exprès au PNAFN**, cf. §1.2) → décret gouv. n° 2016-112 (25 janv. 2016, JORT n° 8, p. 253) →
décret gouv. n° 2016-1401 (27 déc. 2016, JORT n° 105, *dérivé*) → décret gouv. n° 2020-475
(23 juil. 2020, JORT n° 74, p. 1637-1638) → décret gouv. n° 2021-67 (12 janv. 2021, JORT n° 9,
p. 251-252). L'ordre est celui de la chaîne : chaque texte vise le précédent.

**Fait documentable, à énoncer tel quel** : de 2004 à 2022, **onze décrets sur seize** de ces deux
chaînes n'ont d'autre objet que de **prolonger la validité de cartes délivrées entre 1999 et 2017**.
La dernière campagne d'attribution générale de cartes remonte à **2011** (les prorogations de 2020
et 2021 énumèrent les millésimes 2011 à 2016, celle de 2022 va jusqu'à 2017). Le dispositif a donc
cessé d'être renouvelé bien avant d'être remplacé — c'est le contexte réel de l'AMEN social.

### 2.6 La sortie du système : le « système de soins électronique AMEN »

**Décret n° 2022-919 du 29 novembre 2022 portant création et organisation du système de soins
électronique AMEN — *attesté*** (miroir, `dec_2022_919_2022.md`).
JORT n° 131 du 1er décembre 2022, **p. 3367-3368**. URL vérifiée (777 071 o) :
`https://www.pist.tn/jort/2022/2022F/Jo1312022.pdf`

- art. 1er : création du système au profit des catégories pauvres **et** à revenu limité
  bénéficiaires de l'AMEN social ; gestion par le ministère des affaires sociales (art. 2) ;
- art. 5 : **support de soins électronique personnel** attribué au bénéficiaire et à ses ayants
  droit, remplaçant la carte papier ;
- art. 6 : soins, médicaments, hospitalisation, appareillage de prothèse et réadaptation dans les
  structures publiques ;
- art. 20 : **prorogation transitoire** des cartes 2011-2017 jusqu'au 31 décembre 2022 ;
- art. 21 : maintien des régimes particuliers de gratuité et de tarifs réduits.

**TODO** : établir si un arrêté d'application a été pris et si le système est effectivement entré
en service ; aucun texte postérieur n'a été trouvé.

---

## 3. L'AMEN social (2019 → )

### 3.1 La loi organique n° 2019-10 du 30 janvier 2019 — *attesté*

- Signature : **30 janvier 2019** (Béji Caïd Essebsi) ; adoption par l'ARP : **16 janvier 2019**
  (travaux préparatoires, note 1 du texte arabe).
- Publication : **JORT n° 11 du 5 février 2019**, **p. 277-279** (page relevée sur le fascicule
  pour cette note ; `jort_cache` ne la renseigne pas).
- URL vérifiée (1 271 705 o) : `https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf`
- Texte français intégral : `data/iort/textes/md/loi_org_2019_10_2019.md` (161 l.).
- **Aucune disposition d'entrée en vigueur différée** : la loi est muette, donc application de
  droit commun. Les prestations, elles, ne sont ouvertes qu'à compter des textes d'application de
  mai 2020.

Architecture (23 articles, 5 chapitres) :

- **art. 1er** : création du programme AMEN social « pour la promotion des catégories pauvres et
  des catégories à revenu limité » ;
- **art. 2** : définition de la pauvreté **multidimensionnelle** — « les individus ou les familles
  qui souffrent d'une privation multidimensionnelle touchant **le revenu, la santé, l'éducation, le
  logement, l'accès aux services publics et les conditions de vie** » ; le ministère chargé des
  affaires sociales met en place un **modèle de scoring** fixé **par arrêté** ;
- **art. 5** : Conseil supérieur du développement social, présidé par le Chef du gouvernement
  (**jamais créé**, cf. R5) ;
- **art. 6** : Agence nationale de l'intégration et du développement social, EPNA
  (**jamais créée**, cf. R5) ;
- **art. 8** : bénéficiaires — Tunisiens **et étrangers résidant légalement**, sous condition de
  réciprocité ; conditions et procédures renvoyées à un décret gouvernemental ; **récupération des
  prestations indûment attribuées** ;
- **art. 11** : **transferts financiers directs mensuels** aux catégories pauvres, mode de calcul
  et montant fixés par **arrêté conjoint** affaires sociales / finances ;
- **art. 11 bis** (ajouté en 2022) : **allocation familiale mensuelle** pour les enfants de moins
  de 6 ans ;
- **art. 12** : **soutien financier occasionnel**, cas d'octroi et montant par arrêté conjoint ;
- **art. 13** : prestations de soins dans les structures publiques ;
- **art. 14 à 17** : priorités d'accès au logement social, à la formation et à l'emploi, au
  développement régional et à l'économie sociale et solidaire, à l'enseignement ;
- **art. 18 à 22** : registre de données ; **mise à jour au moins tous les deux ans** (art. 19) ;
  rapport annuel au président de l'ARP et au Chef du gouvernement (art. 20) ; **inopposabilité du
  secret professionnel et fiscal** aux structures détentrices de bases publiques (art. 21) ;
- **art. 23** : maintien en vigueur des programmes d'aides antérieurs (cf. R4).

### 3.2 Décret gouvernemental n° 2020-317 du 19 mai 2020 — *attesté*

Conditions et procédures de bénéfice, de retrait et d'opposition.

- Signature : 19 mai 2020 ; publication : **JORT n° 45 du 20 mai 2020**, **p. 1092-1096** ;
  effet : silence du texte, donc publication.
- URL vérifiée (775 243 o) : `https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf`
  (**le fascicule n'est pas dans le corpus local** — l'année 2020 n'en compte que 16 sur ≈ 104 ;
  il a été téléchargé et lu pour cette note.)
- Texte français intégral : `data/iort/textes/md/dec_gouv_2020_317_2020.md` (266 l.).

**Conditions d'éligibilité — *attesté*, art. 3 à 7** :

- **âge** : 18 ans au moins à la date du dépôt, « dans les cas exceptionnels … rabaissé à 16 ans »
  (art. 4) ;
- **revenu** (art. 5) — moyenne mensuelle des revenus **nets, permanents et non permanents, des 12
  derniers mois** précédant la demande, tous revenus confondus (salaires, pensions, allocations,
  activités économiques, biens mobiliers et immobiliers, autres ressources) :

| Composition du ménage | Plafond mensuel |
|---|---|
| individu | 2/3 × SMIG |
| 2 personnes | 1 × SMIG |
| 3 ou 4 personnes | 1,5 × SMIG |
| 5 personnes et plus | 2 × SMIG |

  Membres pris en compte : « le mari et son conjoint ainsi que le nombre des enfants et
  **ascendants** à charge **vivant sous le même toit et partageant la nourriture** ».
  **Majoration d'un demi-SMIG si un membre de la famille est lourdement handicapé** ;
- **patrimoine** : ne pas être propriétaire d'un **logement secondaire** (art. 6) ; n'avoir réalisé,
  ni soi-même ni un membre de la famille, d'opérations d'achat ou de vente **dépassant 30 fois le
  SMIG** au cours des **trois dernières années** (art. 7) ;
- **score** : en sus des conditions ci-dessus, application du **modèle de scoring** pour identifier
  et classer les bénéficiaires (art. 9).

**Question ouverte, à ne pas trancher en l'état — majoration pour handicap lourd.** Le décret
n'énonce **pas de barème séparé** : il prévoit que « la moyenne de revenu mensuel mentionnée au
**premier alinéa** du présent article est **majorée d'un demi salaire minimum** … si un des membres
de la famille est lourdement handicapé ». Or le « premier alinéa » de l'article 5 est le chapeau,
et non les quatre tirets qui le suivent : la portée exacte de la majoration (uniforme sur chaque
palier, ou attachée au seul premier cas) **n'est pas réglée par le texte**.

openfisca encode, sous `amen_social/eligibilite/handicap_lourd/*`, une échelle de
**1,25 / (à vérifier) / 2 / 2,5 SMIG**. Une majoration uniforme de + 0,5 SMIG donnerait
1,1667 / 1,5 / 2 / 2,5 : elle **reproduit les deux dernières lignes et non les deux premières**.
Un écart qui porte sur la moitié des lignes est la signature d'une **lecture incertaine du texte**
plutôt que d'une erreur d'encodage — la valeur 1,25 vient vraisemblablement d'une source
administrative (formulaire, circulaire) non retrouvée. **Ne pas modifier ces paramètres sur la
base de la présente note** ; voir la lacune correspondante au §7.

**Procédure — *attesté*** : dépôt en ligne ou auprès des **unités locales de promotion sociale**
(art. 12) ; **identifiant social** obligatoire (art. 14) ; **enquête sociale** validée par le chef
d'unité, comportant obligatoirement les propositions du travailleur social (art. 15 à 17) ;
**mise à jour au moins tous les deux ans** avec maintien, modification ou suspension (art. 18) ;
**commission technique régionale** présidée par le directeur régional des affaires sociales,
réunie tous les 15 jours (art. 20), qui **valide automatiquement** les dossiers conformes au score
et à la proposition du travailleur social, et instruit les autres (art. 21) ; notification sous
**7 jours** (art. 22) ; décision sur la demande sous **45 jours**, **7 jours en urgence** (art. 23) ;
**transferts dus à compter du mois d'enregistrement de la demande**, payés à terme échu (art. 24) ;
opposition sous **15 jours**, réponse sous **15 jours** (art. 25 à 27) ; retrait en cas de fausse
déclaration ou de non-déclaration de changement (art. 28).

### 3.3 Arrêté du ministre des affaires sociales du 19 mai 2020 relatif au modèle de scoring — *attesté*

- JORT n° 45 du 20 mai 2020, **p. 1096-1097** (même fascicule).
- **art. 2** : « Le modèle de scoring adopte le **test des moyens approximé "Proxy Means Test"** et
  il est basé sur la définition de la pauvreté multidimensionnelle », déclinée en sept familles de
  variables : caractéristiques **démographiques** (âge, genre, statut matrimonial, taille de la
  famille), **géographiques** (gouvernorat, milieu), **éducation**, **santé** (handicap),
  **situation professionnelle et économique**, **caractéristiques de logement** (statut, type,
  équipement), **accès aux services publics de base** (école primaire, collège, dispensaire).
- **art. 3** : mise à jour du modèle **au moins une fois tous les cinq ans**.
- **Les pondérations ne sont pas publiées** : l'arrêté énumère les dimensions, pas les
  coefficients. Le seuil de décile utilisé pour l'éligibilité relève d'une **circulaire**
  (openfisca cite la circulaire n° 12 du 12 mai 2022, non publiée au JORT). **Lacune structurelle
  à signaler.**

### 3.4 Le transfert monétaire permanent : montants et série datée

**Arrêté conjoint du ministre des affaires sociales et du ministre des finances du 19 mai 2020**
(fondateur), JORT n° 45 du 20 mai 2020, **p. 1097** — *attesté* :

> « **Art. 2.** — Le montant mensuel de transfert direct pour les catégories pauvres … est calculé
> comme suit : — **Un montant de base mensuel égal à 180 dinars servis par individu ou par
> famille**, — **Une allocation supplémentaire égale à 10 dinars par mois au titre de chaque enfant
> à charge âgé de moins de 18 ans sans condition, jusqu'à l'âge de 25 ans** aux enfants à charge
> justifiant la poursuite d'études, d'apprentissage ou d'une formation.
> Le montant de l'allocation supplémentaire est **doublé** au titre de chaque enfant titulaire
> d'une **carte de handicap**. »

Série complète, chaque ligne **attestée** sur le fascicule français :

| Effet | Base mensuelle | Texte | JORT | Page |
|---|---|---|---|---|
| 20 mai 2020 | **180 D** | arrêté conjoint du 19 mai 2020, art. 2 | n° 45 (20 mai 2020) | 1097 |
| **1er janvier 2022** | **200 D** | arrêté conjoint du 1er avril 2022, art. 1er | n° 38 (8 avril 2022) | 972 |
| **1er janvier 2023** | **220 D** | arrêté conjoint du 3 avril 2023, art. 1er et 2 | n° 34 (6 avril 2023) | 809 |
| **1er janvier 2024** | **240 D** | arrêté conjoint du 28 février 2024, art. 1er et 2 | n° 33 (1er mars 2024) | 768 |
| **1er janvier 2025** | **260 D** | arrêté conjoint du 29 janvier 2025, art. 1er et 2 | n° 12 (30 janvier 2025) | 275 |

Toutes ces revalorisations sont **rétroactives au 1er janvier** de l'année : l'arrêté est pris en
février, mars ou avril et fait remonter l'effet au 1er janvier. C'est une régularité à énoncer.

**Supplément par enfant — *attesté*, arrêté conjoint du 1er avril 2022, art. 1er, alinéa 2
(nouveau)** : le supplément de 10 D est maintenu, **mais la borne d'âge basse change** :
« chaque enfant à charge **âgé de 6 ans et ne dépassant pas l'âge de 18 ans** sans condition,
jusqu'à l'âge de 25 ans aux enfants à charge justifiant la poursuite d'études, d'apprentissage ou
d'une formation professionnelle, et ce **à compter du 1er février 2022** ». Doublement pour enfant
titulaire d'une carte de handicap maintenu.

**Ce déplacement de borne est la clé de l'articulation avec l'allocation familiale non
contributive** : les moins de 6 ans sortent du supplément de 10 D le 1er février 2022, jour où
l'allocation familiale de 30 D les prend en charge. **Il n'y a pas cumul.**

**Corrections à porter à openfisca** :
- `amen_social/allocation_base.yaml` s'arrête à 240 D au 2024-01-01 : **ajouter 260 D au
  2025-01-01** (arrêté du 29 janvier 2025, JORT n° 12, p. 275).
- `amen_social/supplements/enfant_a_charge.yaml` porte 10 D au **2019-01-01** avec la référence
  « Article 4.1 du Décret n° 2019-318 ». **Ce décret n'existe pas** : aucun texte n° 2019-318 n'a
  été trouvé. La bonne référence est l'**arrêté conjoint du 19 mai 2020, art. 2, 2e tiret**, avec
  effet au **20 mai 2020**.
- `amen_social/supplements/limite_age_enfant.yaml` (18 ans) et `limite_age_etudiant.yaml` (21 ans)
  sont datés de 2019-01-01. La limite étudiant est **25 ans**, pas 21, et les deux limites sont
  fixées par l'arrêté du 19 mai 2020. Une **borne basse de 6 ans** apparaît au 1er février 2022 et
  n'est pas modélisée.
- `amen_social/supplements/handicap.yaml` (coefficient 2) référence un « Arrêté 931 du 20 mai
  2020 ». **Aucun arrêté numéroté 931 n'existe** : les arrêtés tunisiens ne sont pas numérotés.
  La bonne référence est l'arrêté conjoint du **19 mai 2020, art. 2, dernier alinéa** (JORT n° 45,
  p. 1097). La même référence apocryphe figure dans `allocation_base.yaml`.

### 3.5 L'appui financier occasionnel (aides ponctuelles)

**Arrêté conjoint du 19 mai 2020 fixant les cas de l'octroi et les montants de l'appui financier
occasionnel — *attesté*.** JORT n° 45 du 20 mai 2020, **p. 1097**. Pris sur le fondement de
l'article 12 de la loi organique.

- **art. 2** : les **catégories pauvres** bénéficient d'un appui pour le mois de Ramadan, l'Aïd
  al-Fitr, l'Aïd al-Idha, **et** la rentrée scolaire et universitaire ;
- **art. 3** : les **catégories à revenu limité** n'en bénéficient **que** pour la rentrée scolaire
  et universitaire ;
- **art. 4** — montants et **échéances de paiement**, tous *attestés* :

| Occasion | Montant | Unité | Échéance |
|---|---|---|---|
| mois de Ramadan | **60 D** | individu ou famille | dans la première semaine du mois |
| Aïd al-Fitr | **60 D** | individu ou famille | avant la fin du mois de Ramadan |
| Aïd al-Idha | **60 D** | individu ou famille | avant la date de l'Aïd |
| rentrée scolaire | **50 D** | par enfant scolarisé | début de l'année scolaire |
| rentrée universitaire | **120 D** | par enfant dans le supérieur | début de l'année universitaire |

**Arrêté conjoint du 8 décembre 2022 — *attesté*.** JORT n° 136 du 9 décembre 2022,
**p. 3446-3447**. URL vérifiée (759 285 o) : `https://www.pist.tn/jort/2022/2022F/Jo1362022.pdf`
(**fascicule absent du corpus local**, téléchargé pour cette note.)
Son **article 5 abroge expressément l'arrêté du 19 mai 2020**. Les cinq montants ci-dessus sont
**repris à l'identique**, mais le champ s'élargit :

- l'appui « fêtes » reste réservé aux **catégories pauvres** (art. 2) ; les aides de rentrée sont
  ouvertes **aux deux catégories** (art. 3) et étendues aux établissements publics de formation et
  d'apprentissage professionnel et aux **centres d'éducation spécialisée**, publics et associatifs ;
- **nouveauté 1** : prise en charge des **abonnements annuels de transport scolaire et
  universitaire**, à hauteur des tarifs pratiqués par les entreprises de transport public ;
- **nouveauté 2** : appui pour « dépenses exceptionnelles nécessitées par des **conditions
  sanitaires ou sociales d'urgence**, ou pour appuyer les moyens de prise en charge de leurs
  enfants scolarisés, en particulier ceux qui sont exposés à l'**inadaptation sociale et au
  décrochage scolaire** » — montant compris **entre 60 et 200 dinars** selon la situation
  financière de la famille, **au maximum quatre fois par an**, ces deux limites pouvant être
  dépassées « dans des cas exceptionnels » sur autorisation du **comité général de la promotion
  sociale**.

**Arrêté conjoint du 10 juillet 2025** modifiant l'arrêté du 8 décembre 2022 — *dérivé*.
JORT n° 88 de 2025, **p. 2058**. **Le contenu n'a pas pu être établi** : l'URL
`https://www.pist.tn/jort/2025/2025F/Jo0882025.pdf` répond HTTP 200 (3 191 536 o) mais **sert le
fascicule arabe**, et le fascicule français n'est pas dans le corpus local. **TODO** (§7).

**Corrections à porter à openfisca** : les cinq paramètres
`amen_social/aides_ponctuelles/**` sont datés du **2019-01-01**. Les valeurs sont exactes mais la
date d'effet est le **20 mai 2020** (arrêté conjoint du 19 mai 2020), et le fondement postérieur au
9 décembre 2022 est l'arrêté du 8 décembre 2022. Aucun des cinq ne porte de `reference`. Deux
prestations manquent : le **transport scolaire et universitaire** et l'**appui d'urgence** de 60 à
200 D (quatre fois par an au plus).

### 3.6 L'aide exceptionnelle Covid de 2021

**Arrêté conjoint du 20 août 2021 fixant les montants des aides financières occasionnelles et
exceptionnelles — *attesté*.** JORT n° 75 du 20 août 2021, **p. 2069-2072**.
URL vérifiée (883 870 o) : `https://www.pist.tn/jort/2021/2021F/Jo0752021.pdf`

- Fondement : **loi n° 2021-28 du 22 juin 2021** approuvant l'accord de prêt du 2 avril 2021 entre
  la Tunisie et la **BIRD** pour le « projet d'appui à la riposte d'urgence contre le Covid-19 en
  matière de protection sociale ».
- **art. 2** : montant **300 dinars, versé une seule fois**, à cinq catégories :
  (1) bénéficiaires des transferts monétaires mensuels, (2) bénéficiaires d'une faible allocation
  de vieillesse ou pension de retraite, (3) titulaires de cartes de soins gratuits sans transfert
  monétaire, (4) titulaires de cartes de soins à tarifs réduits — **ces quatre catégories sans
  condition** ; (5) **catégories sans aucune couverture sociale**, sous trois conditions cumulatives :
  revenu du chef de famille et de son conjoint ≤ **300 D par mois** ; pas de véhicule de moins de
  **15 ans** d'âge ; pas plus de deux véhicules achetés ou vendus en 2020-2021.

Ce texte est le seul rencontré qui **énumère explicitement les quatre populations de l'assistance
tunisienne** (transfert AMEN, faible pension, AMG1, AMG2) et permet de les articuler. Il est aussi
la meilleure attestation du **rôle des bailleurs** dans le dispositif, dont le livre actuel parle
sans référence.

À rattacher : **arrêté conjoint du 31 août 2020** fixant les modalités et procédures de paiement
des aides sociales financières exceptionnelles et temporaires aux catégories vulnérables, pauvres
et à faible revenu lésées par le confinement Covid-19 (JORT n° 92 de 2020, p. 2010-2012) —
*dérivé*, **TODO** : montants à établir.

### 3.7 L'autonomisation économique

**Décret n° 2022-715 du 20 septembre 2022 — *attesté*** (miroir, `dec_2022_715_2022.md`).
JORT n° 106 du 27 septembre 2022, **p. 2702-2704**. URL vérifiée (863 889 o) :
`https://www.pist.tn/jort/2022/2022F/Jo1062022.pdf`

- art. 1er : programme d'autonomisation économique des catégories pauvres et à revenu limité
  bénéficiaires de l'AMEN social **et des personnes handicapées** ;
- art. 2 : financement de projets **individuels ou collectifs** ;
- art. 3 : crédits annuels inscrits au budget du ministère chargé des affaires sociales ;
- art. 4 : **30 % des crédits annuels réservés aux personnes handicapées** ;
- art. 5 : **maintien du transfert monétaire mensuel pendant un an renouvelable une fois** à
  compter du lancement du projet — règle d'articulation importante ;
- art. 6 : conditions du candidat (**TODO** : détail à relever, le fichier du miroir n'a pas été
  dépouillé au-delà de l'article 6).

---

## 4. Les allocations familiales non contributives (2022 → )

**Attention de vocabulaire** : le livre actuel place ce dispositif « de 2020 à 2024 ». Sur pièce,
**il n'existe qu'à compter de 2022**. Ce qui existe en 2020, c'est le **supplément de 10 D par
enfant** du transfert AMEN (§3.4), qui n'est pas une allocation familiale.

### 4.1 Le fondement : décret-loi n° 2022-8 du 31 janvier 2022 — *attesté*

Complétant la loi organique n° 2019-10 par un **article 11 bis**. Signé par Kaïs Saïed.

- Publication : **JORT n° 13 du 2 février 2022**, **p. 336** ; URL vérifiée (2 432 820 o) :
  `https://www.pist.tn/jort/2022/2022F/Jo0132022.pdf`
- Texte français intégral : `data/iort/textes/md/dec_loi_2022_8_2022.md`.

> « **Article 11 bis** — Les catégories pauvres et les catégories à revenu limité bénéficient d'une
> **allocation familiale payable mensuellement, au titre des enfants âgés de moins de 6 ans**.
> Les situations d'octroi et le montant … sont fixés par arrêté conjoint du ministre chargé des
> affaires sociales et du ministre chargé des finances. »

Le texte est un **décret-loi** pris pendant la période des mesures exceptionnelles du décret
présidentiel n° 2021-117 : une loi organique est complétée par un acte du seul Président. Fait
institutionnel à documenter sans commentaire polémique.

### 4.2 L'arrêté conjoint du 1er avril 2022 — *attesté*

Fixant les situations d'octroi et le montant des allocations familiales mensuelles.
**JORT n° 38 du 8 avril 2022**, **p. 973**. URL vérifiée (1 006 939 o) :
`https://www.pist.tn/jort/2022/2022F/Jo0382022.pdf`

> « **Art. 2.** — L'allocation familiale est octroyée au profit des catégories pauvres et des
> catégories à revenu limité bénéficiant du programme « AMEN SOCIAL » **au titre des enfants à
> charge âgés de moins de six (6) ans**.
> **Les catégories à revenu limité affiliées à l'un des régimes de sécurité sociale sont exclues du
> bénéfice de cette allocation familiale.**
> **Art. 3.** — Le montant de l'allocation familiale est fixé à **trente (30) dinars par mois** au
> titre de **chaque enfant à charge âgé de moins de six (6) ans**. »

Quatre points *attestés* et structurants :
1. **30 D par mois et par enfant de moins de 6 ans**, **sans plafonnement du nombre d'enfants** —
   à la différence des allocations familiales contributives ;
2. le champ est **plus large que le transfert monétaire** : il couvre les catégories pauvres **et**
   les catégories à revenu limité, qui ne perçoivent pas de transfert ;
3. **exclusion explicite** des catégories à revenu limité **affiliées à un régime de sécurité
   sociale** — c'est la règle de non-cumul avec les allocations familiales contributives, et donc
   le point de jonction avec la partie 1.2 du livre ;
4. l'arrêté vise expressément la **loi n° 2021-28 du 22 juin 2021** approuvant le prêt BIRD Covid :
   **le financement du dispositif par un bailleur figure dans le visa du texte lui-même**. C'est la
   source qui manque au récit actuel du livre.

**Corrections à porter à openfisca** :
- `non_contributives/allocation_familiale.yaml` porte 30 D au **2020-06-01**, sans référence. La
  date correcte est le **8 avril 2022** (le texte ne prévoit pas d'effet rétroactif, contrairement
  à l'arrêté du même jour sur le transfert) ; références : décret-loi n° 2022-8, art. 11 bis, et
  arrêté conjoint du 1er avril 2022, art. 3.
- **La condition « moins de 6 ans » et l'exclusion des affiliés ne sont pas modélisées.**

### 4.3 Aucune revalorisation depuis 2022 — *attesté négativement*

Le balayage des arrêtés du ministère des affaires sociales jusqu'à décembre 2025 ne fait
apparaître **aucune modification de l'arrêté du 1er avril 2022**. L'allocation familiale non
contributive est donc restée à **30 D** pendant que la base du transfert passait de 200 à 260 D.
Fait à documenter, avec la vue d'évolution correspondante.

### 4.4 Les prestations catégorielles créées par les lois de finances (2025-2026)

Toutes *dérivées* : `jort_cache` n'en donne que le résumé arabe de l'article, et **les fascicules
français correspondants ne sont pas accessibles** (§7).

| Texte | Article | Objet | Montant |
|---|---|---|---|
| Loi n° 2024-48 du 9 déc. 2024 (LF 2025) | **art. 26** | patients allergiques au gluten (maladie cœliaque) des familles pauvres et à revenu limité inscrites à l'AMEN | **30 D / mois / personne** (dépenses alimentaires) |
| Loi n° 2025-17 du 12 déc. 2025 (LF 2026) | **art. 35** | *xeroderma pigmentosum* ; et allergiques au gluten inscrits à l'AMEN | **130 D / mois / personne** |
| Loi n° 2025-17 (LF 2026) | **art. 71** | enfants diabétiques des familles pauvres et à revenu limité inscrites à l'AMEN | **150 D** (achat d'un lecteur de glycémie sans piqûre) |
| Loi n° 2025-17 (LF 2026) | **art. 81** | enfants atteints de troubles du spectre autistique | **150 D / mois** (réhabilitation et intégration) |
| Loi n° 2025-17 (LF 2026) | **art. 96** | création d'un **fonds d'encadrement matériel et social des orphelins** des familles pauvres et à revenu limité, sous tutelle du ministère de la Famille, financé par une **contribution sociétale** des entreprises publiques et privées et par des dons | — |

**Texte d'application établi** : **arrêté conjoint des ministres des affaires sociales, de la santé
et des finances du 30 juillet 2025** fixant les modalités d'octroi de l'allocation pour la prise en
charge des dépenses alimentaires aux patients allergiques au gluten — *attesté* (JORT n° 99 du
**7 août 2025**, **p. 1977** ; URL vérifiée, 1 575 188 o :
`https://www.pist.tn/jort/2025/2025F/Jo0992025.pdf`). Demande écrite avec certificat médical d'un
médecin de la santé publique selon modèle annexé ; dépôt selon les articles 11 et 12 du décret
gouvernemental n° 2020-317 ; enregistrement au registre des données ; **« entrera en vigueur à
compter du 1er janvier 2025 »** (art. 3) — rétroactivité de sept mois.

**Le mode de faire de 1986 est intact** : une prestation est créée par un article de loi de
finances, et son régime juridique est fixé — parfois des années plus tard, ici sept mois — par un
arrêté. C'est le constat que le §9.3 du plan pressentait, ici confirmé sur la période récente.

---

## 5. Dispositifs adjacents à citer sans les traiter au fond

Ces textes ne relèvent pas du périmètre confié mais bornent l'assistance non contributive ; tous
*dérivés* sauf mention, à partir des intitulés `jort_cache`.

- **Personnes âgées** : loi n° 94-114 du 31 octobre 1994 relative à la protection des personnes
  âgées (art. 18 et 19) ; décret n° 96-1016 du 27 mai 1996 (prise en charge par les familles) ;
  **arrêté du 30 septembre 1997** (aide matérielle aux personnes âgées nécessiteuses : montant
  **non chiffré**, cf. R2) ; **arrêté du 30 septembre 1997** (famille d'accueil : **90 D par mois**,
  *attesté*, JORT n° 81, p. 1867 ; refus si la personne âgée a un revenu régulier > ½ SMIG),
  modifié par l'arrêté du 12 décembre 2003 (JORT n° 102, p. 3681) ; arrêté du 8 octobre 1997 sur la
  participation aux frais de séjour (JORT n° 83, p. 1911).
- **Personnes handicapées** : **décret n° 2005-3088 du 29 novembre 2005** (conditions de bénéfice
  de l'aide matérielle à la personne handicapée nécessiteuse, placement en famille d'accueil, aide
  à la famille d'accueil ; JORT n° 97 du 6 décembre 2005, p. 3446-3447 ; texte français au miroir) ; **arrêté conjoint
  du 1er juin 2006** fixant les montants (JORT n° 46 du 9 juin 2006, p. 1517-1518), **modifié par l'arrêté du
  28 avril 2017** (JORT n° 42 du 26 mai 2017, p. 1930-1931) ; arrêté du 25 avril 2006 sur la prise en charge des
  frais de soins et de prothèses (JORT n° 36, p. 1211) ; arrêté du 12 août 2016 modifié le 25 août
  2020 (subvention de réhabilitation et d'éducation spécialisée, JORT n° 91 de 2020, p. 1981).
  **TODO** : ces montants n'ont pas été relevés ; ils forment une série datée exploitable.
- **Pensions minimales** : arrêté conjoint du 10 juillet 2020 attribuant une prime complémentaire,
  exceptionnelle et temporaire aux titulaires d'une pension CNSS ou CNRPS **≤ 180 D par mois**
  (JORT n° 67 de 2020, p. 1515-1517). Frontière avec le livre Retraites, mais le seuil de 180 D est
  **exactement** la base du transfert AMEN de 2020 : à signaler.

---

## 6. Requêtes de vérification — à reproduire

Base : `sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1'`.

### 6.1 Balayage NULL-safe de l'intitulé du PNAFN

```sql
SELECT recid, coalesce(type,'?'), coalesce(numero,'-'), coalesce(date_signature,'-'),
       jort_annee, jort_numero, coalesce(pages,'-'), titre
FROM textes
WHERE coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%programme national d''aide%'
   OR coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%familles necessiteuses%'
   OR coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%familles nécessiteuses%'
   OR coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%معوز%'
   OR coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%محتاج%'
   OR coalesce(titre,'')||' '||coalesce(objet,'') LIKE '%PNAFN%'
ORDER BY date_signature;
```

**Résultat, 6 lignes** : loi n° 86-83 (art. 13) ; arrêté du 6 janvier 1987 ; loi n° 87-83
(art. 67) ; décret n° 2014-1526 ; décret gouv. n° 2018-626 ; loi de finances 2026 (art. 96,
fonds pour les orphelins). Aucun texte de création, d'éligibilité ou de montant.

### 6.2 Balayage des arrêtés « montant / octroi / aide » du ministère des Affaires sociales

```sql
SELECT recid, coalesce(type,'?'), coalesce(numero,'-'), coalesce(date_signature,'-'),
       jort_annee, jort_numero, coalesce(pages,'-'), titre
FROM textes
WHERE coalesce(date_signature,'') BETWEEN '1986-01-01' AND '2020-12-31'
  AND coalesce(titre,'') LIKE '%ffaires ociales%'          -- insensible à la casse du libellé
  AND (coalesce(titre,'') LIKE '%montant%' OR coalesce(titre,'') LIKE '%octroi%'
    OR coalesce(titre,'') LIKE '%aide%'    OR coalesce(titre,'') LIKE '%secours%'
    OR coalesce(titre,'') LIKE '%subvention%')
ORDER BY date_signature;
```

**Résultat** : 80 lignes, dominées par le prix du progrès social et le prix du travailleur
exemplaire. **Aucune** ne concerne l'allocation du PNAFN. Les seules aides monétaires chiffrées par
arrêté visent les **personnes âgées** (1997, 2003) et les **personnes handicapées** (2006, 2017).

**Rappel de méthode** : ne jamais concaténer `type || numero || titre` sans `coalesce()`. Les
arrêtés ministériels ont `numero` NULL, et l'arrêté du 6 janvier 1987 — pièce centrale de ce
dossier — disparaîtrait silencieusement.

---

## 7. Lacunes — ce qui n'a pas pu être sourcé

Chacune est un **TODO** et ne doit pas être comblée par déduction.

1. **Les onze paliers du PNAFN, 1987-2018.** Aucun texte. Piste restante : les **circulaires** de la
   direction générale de la promotion sociale (`ijtimaia.tn`), non publiées au JORT ; les rapports
   annuels du ministère des Affaires sociales ; les documents de suivi de la Banque mondiale sur
   le projet d'appui à la protection sociale. À défaut, le précis doit **dire** que ces montants
   n'ont pas de fondement textuel publié.
2. **L'arrêté du Premier ministre** répartissant les 2,5 MD entre organismes (loi n° 87-83,
   art. 67) : introuvable dans `jort_cache`.
3. **La série des contributions des caisses après 1988** : la ligne budgétaire 62-13 n'a été lue
   que pour la LF 1988. Le suivi jusqu'à aujourd'hui suppose de dépouiller les tableaux de voies et
   moyens de chaque loi de finances — travail non fait.
4. **L'arrêté conjoint fixant le nombre global de cartes et les quotas régionaux** (AMG1, décret
   98-1812, art. 2 ; AMG2, décret 98-409, art. 2 et 14). Aucun trouvé. Si le résultat négatif se
   confirme, c'est le troisième paramètre décisif de l'assistance tunisienne à ne pas être publié.
5. **Décret n° 99-1372 du 21 juin 1999** (modification du décret 98-409) : absent du miroir, non
   océrisé. JORT n° 52 de 1999, p. 1052-1053.
6. **Décret n° 88-917 du 6 mai 1988** (modification du décret 88-175) : objet non établi.
7. **Décret gouvernemental n° 2018-626** : intitulé arabe seul, page non renseignée, année 2018 mal
   couverte côté français.
8. **Arrêté conjoint du 10 juillet 2025** modifiant l'arrêté du 8 décembre 2022 sur l'appui
    financier occasionnel (JORT n° 88 de 2025, p. 2058) : **contenu inconnu**. L'URL en « F » sert
    le fascicule arabe et le corpus local n'a pas ce numéro. C'est probablement la dernière
    revalorisation des aides ponctuelles ; **le précis ne doit pas affirmer que les montants sont
    inchangés depuis 2022.**
9. **Lois de finances 2025 et 2026** : `jort_cache` n'en donne que le résumé arabe.
    `2024F/Jo1492024.pdf` répond **289 octets (404)** — la version française du fascicule de la
    LF 2025 n'est pas en ligne ; `2025F/Jo1482025.pdf` répond 200 mais **sert l'arabe**. Les cinq
    articles du §4.4 sont donc **dérivés**, non attestés en français.
10. **Pondérations du modèle de scoring** et **seuil de décile** : non publiés. La circulaire n° 12
    du 12 mai 2022 citée par openfisca est hébergée sur `ijtimaia.tn`, hors JORT — statut juridique
    à qualifier.
11. **Effectifs et dépenses** : aucune série de bénéficiaires (PNAFN, AMG1, AMG2, AMEN) n'a été
    recherchée dans cette note. Elle est indispensable au principe « jamais de chiffre ponctuel
    sans vue d'évolution ». Sources à explorer : rapports annuels du ministère des Affaires
    sociales, INS, documents de projet de la Banque mondiale, `unicef2020` déjà en bibliographie.
12. **Décret n° 2022-715, art. 6 et suivants** : conditions du candidat à l'autonomisation
    économique, non relevées.
13. **Arrêté conjoint du 31 août 2020** (aides Covid) : montants non relevés.
14. **Origine de l'échelle « handicap lourd » d'openfisca** (1,25 / … / 2 / 2,5 SMIG) : non
    reproductible depuis le décret gouvernemental n° 2020-317, dont l'article 5 énonce une
    majoration de + ½ SMIG dont la portée est ambiguë (§3.2). Source à chercher du côté des
    circulaires du ministère des Affaires sociales et du formulaire de demande AMEN.

---

## 8. Références candidates (CSL-JSON)

### 8.1 Déjà présentes dans `precis/fr/prestations_sociales/references.json`

- `unicef2020` — **jamais citée** ; à mobiliser pour l'allocation familiale non contributive
  (§4), dont elle est l'antécédent doctrinal.
- `23975222/EZEBV8GK` — pièce jointe Zotero résiduelle, **à retirer** (déjà signalé au §5 du plan).

### 8.2 À créer

Toutes vérifiées par téléchargement. `container-title` = fascicule du JORT ; `issue` = numéro du fascicule ; `page` = page du
fascicule ; `event-date` = date de signature ; `issued` = date de publication (relevée sur le
**pied de page du fascicule**, qui prime sur `jort_cache.date_publication` — huit divergences
constatées). Le **tome** du JORT n'est pas porté : il n'a pas d'emplacement CSL approprié pour
`legislation` et doublonnerait `issue`.

```json
[
  { "id": "loi-86-83-lfr-1986", "citation-key": "loi-86-83-lfr-1986",
    "type": "legislation", "title": "Loi n° 86-83 du 1er septembre 1986, portant loi de finances rectificative pour la gestion 1986 (article 13 : contribution des organismes de sécurité sociale pour l'aide aux familles nécessiteuses)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "48",
    "page": "928", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1986,9,1]]}, "issued": {"date-parts": [[1986,9,2]]},
    "URL": "https://www.pist.tn/jort/1986/1986F/Jo04886.pdf" },

  { "id": "arrete-1987-01-06-financement-pnafn", "citation-key": "arrete-1987-01-06-financement-pnafn",
    "type": "legislation", "title": "Arrêté des ministres du plan et des finances et des affaires sociales du 6 janvier 1987, fixant la contribution de la Caisse nationale de retraite et de prévoyance sociale et de la Caisse nationale de sécurité sociale au financement du programme national d'aide aux familles nécessiteuses",
    "container-title": "Journal officiel de la République tunisienne", "issue": "4",
    "page": "65", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1987,1,6]]}, "issued": {"date-parts": [[1987,1,16]]},
    "URL": "https://www.pist.tn/jort/1987/1987F/Jo00487.pdf" },

  { "id": "loi-87-29-amg", "citation-key": "loi-87-29-amg",
    "type": "legislation", "title": "Loi n° 87-29 du 12 juin 1987, relative au régime de l'assistance médicale gratuite",
    "container-title": "Journal officiel de la République tunisienne", "issue": "43",
    "page": "767", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1987,6,12]]}, "issued": {"date-parts": [[1987,6,16]]},
    "URL": "https://www.pist.tn/jort/1987/1987F/Jo04387.pdf" },

  { "id": "loi-87-83-lf-1988", "citation-key": "loi-87-83-lf-1988",
    "type": "legislation", "title": "Loi n° 87-83 du 31 décembre 1987, portant loi de finances pour la gestion 1988 (articles 62 à 67)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "91",
    "page": "1633-1634", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1987,12,31]]}, "issued": {"date-parts": [[1987,12,31]]},
    "URL": "https://www.pist.tn/jort/1987/1987F/Jo09187.pdf" },

  { "id": "loi-90-111-lf-1991", "citation-key": "loi-90-111-lf-1991",
    "type": "legislation", "title": "Loi n° 90-111 du 31 décembre 1990, portant loi de finances pour la gestion 1991 (articles 65 et 66 : aménagement du droit annuel d'affiliation au régime de l'assistance médicale gratuite et de la contribution aux frais de soins)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "86",
    "page": "2056", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1990,12,31]]}, "issued": {"date-parts": [[1990,12,31]]},
    "URL": "https://www.pist.tn/jort/1990/1990F/Jo08690.pdf" },

  { "id": "decret-88-175-livrets-amg", "citation-key": "decret-88-175-livrets-amg",
    "type": "legislation", "title": "Décret n° 88-175 du 6 février 1988, relatif aux conditions et modalités d'attribution des livrets d'assistance médicale gratuite",
    "container-title": "Journal officiel de la République tunisienne", "issue": "14",
    "page": "281-282", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1988,2,6]]}, "issued": {"date-parts": [[1988,2,23]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo01488.pdf" },

  { "id": "arrete-1988-02-17-droit-affiliation-amg", "citation-key": "arrete-1988-02-17-droit-affiliation-amg",
    "type": "legislation", "title": "Arrêté du ministre de la santé publique du 17 février 1988, relatif aux modalités de paiement du droit annuel d'affiliation au régime de l'assistance médicale gratuite",
    "container-title": "Journal officiel de la République tunisienne", "issue": "14",
    "page": "284", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1988,2,17]]}, "issued": {"date-parts": [[1988,2,23]]},
    "URL": "https://www.pist.tn/jort/1988/1988F/Jo01488.pdf" },

  { "id": "arrete-1997-09-30-personnes-agees", "citation-key": "arrete-1997-09-30-personnes-agees",
    "type": "legislation", "title": "Arrêté du ministre des affaires sociales du 30 septembre 1997, fixant le montant de l'aide matérielle attribuée aux personnes âgées nécessiteuses et les conditions d'octroi de cette aide",
    "container-title": "Journal officiel de la République tunisienne", "issue": "81",
    "page": "1867", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1997,9,30]]}, "issued": {"date-parts": [[1997,10,10]]},
    "URL": "https://www.pist.tn/jort/1997/1997F/Jo08197.pdf" },

  { "id": "decret-98-409-amg2", "citation-key": "decret-98-409-amg2",
    "type": "legislation", "title": "Décret n° 98-409 du 18 février 1998, fixant les catégories des bénéficiaires des tarifs réduits de soins et d'hospitalisation dans les structures sanitaires publiques relevant du ministère de la santé publique ainsi que les modalités de leur prise en charge et les tarifs auxquels ils sont assujettis",
    "container-title": "Journal officiel de la République tunisienne", "issue": "17",
    "page": "405-408", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1998,2,18]]}, "issued": {"date-parts": [[1998,2,27]]},
    "URL": "https://www.pist.tn/jort/1998/1998F/Jo01798.pdf" },

  { "id": "decret-98-1812-amg1", "citation-key": "decret-98-1812-amg1",
    "type": "legislation", "title": "Décret n° 98-1812 du 21 septembre 1998, fixant les conditions et les modalités d'attribution et de retrait de la carte de soins gratuits",
    "container-title": "Journal officiel de la République tunisienne", "issue": "78",
    "page": "1975-1976", "authority": "République tunisienne",
    "event-date": {"date-parts": [[1998,9,21]]}, "issued": {"date-parts": [[1998,9,29]]},
    "URL": "https://www.pist.tn/jort/1998/1998F/Jo07898.pdf" },

  { "id": "decret-2005-2886-amg2-ascendants", "citation-key": "decret-2005-2886-amg2-ascendants",
    "type": "legislation", "title": "Décret n° 2005-2886 du 24 octobre 2005, portant modification du décret n° 98-409 du 18 février 1998 (article 2 nouveau : prise en compte des ascendants à charge)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "86",
    "page": "2911", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2005,10,24]]}, "issued": {"date-parts": [[2005,10,28]]},
    "URL": "https://www.pist.tn/jort/2005/2005F/Jo0862005.pdf" },

  { "id": "decret-2012-2521-amg1-pnafn", "citation-key": "decret-2012-2521-amg1-pnafn",
    "type": "legislation", "title": "Décret n° 2012-2521 du 16 octobre 2012, modifiant le décret n° 98-1812 du 21 septembre 1998 (article 5 nouveau : listes établies au vu des bénéficiaires du programme national d'aide aux familles nécessiteuses)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "84",
    "page": "2627", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2012,10,16]]}, "issued": {"date-parts": [[2012,10,23]]},
    "URL": "https://www.pist.tn/jort/2012/2012F/Jo0842012.pdf" },

  { "id": "decret-2012-2522-amg2-commissions", "citation-key": "decret-2012-2522-amg2-commissions",
    "type": "legislation", "title": "Décret n° 2012-2522 du 16 octobre 2012, modifiant le décret n° 98-409 du 18 février 1998 (articles 5, 7 et 12 : recomposition des commissions et cartes annuelles pour catégories spécifiques)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "84",
    "page": "2628-2629", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2012,10,16]]}, "issued": {"date-parts": [[2012,10,23]]},
    "URL": "https://www.pist.tn/jort/2012/2012F/Jo0842012.pdf" },

  { "id": "decret-2014-1526-banque-donnees", "citation-key": "decret-2014-1526-banque-donnees",
    "type": "legislation", "title": "Décret n° 2014-1526 du 30 avril 2014, portant création d'une unité de gestion par objectifs au ministère des affaires sociales pour la réalisation du projet d'instauration d'une banque de données sur les familles nécessiteuses et à revenu limité",
    "container-title": "Journal officiel de la République tunisienne", "issue": "38",
    "page": "1159-1161", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2014,4,30]]}, "issued": {"date-parts": [[2014,5,13]]},
    "URL": "https://www.pist.tn/jort/2014/2014F/Jo0382014.pdf" },

  { "id": "loi-org-2019-10-amen", "citation-key": "loi-org-2019-10-amen",
    "type": "legislation", "title": "Loi organique n° 2019-10 du 30 janvier 2019, relative à la création du programme « AMEN SOCIAL »",
    "container-title": "Journal officiel de la République tunisienne", "issue": "11",
    "page": "277-279", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2019,1,30]]}, "issued": {"date-parts": [[2019,2,5]]},
    "URL": "https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf" },

  { "id": "decret-gouv-2020-317-amen", "citation-key": "decret-gouv-2020-317-amen",
    "type": "legislation", "title": "Décret gouvernemental n° 2020-317 du 19 mai 2020, fixant les conditions et les procédures de bénéfice, de retrait et d'opposition au programme « AMEN SOCIAL »",
    "container-title": "Journal officiel de la République tunisienne", "issue": "45",
    "page": "1092-1096", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2020,5,19]]}, "issued": {"date-parts": [[2020,5,20]]},
    "URL": "https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf" },

  { "id": "arrete-2020-05-19-scoring", "citation-key": "arrete-2020-05-19-scoring",
    "type": "legislation", "title": "Arrêté du ministre des affaires sociales du 19 mai 2020, relatif à la détermination du modèle de scoring",
    "container-title": "Journal officiel de la République tunisienne", "issue": "45",
    "page": "1096-1097", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2020,5,19]]}, "issued": {"date-parts": [[2020,5,20]]},
    "URL": "https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf" },

  { "id": "arrete-2020-05-19-transferts", "citation-key": "arrete-2020-05-19-transferts",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et du ministre des finances du 19 mai 2020, fixant le mode de calcul et le montant des transferts monétaires directs au profit des catégories pauvres bénéficiant du programme « AMEN SOCIAL »",
    "container-title": "Journal officiel de la République tunisienne", "issue": "45",
    "page": "1097", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2020,5,19]]}, "issued": {"date-parts": [[2020,5,20]]},
    "URL": "https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf" },

  { "id": "arrete-2020-05-19-appui-occasionnel", "citation-key": "arrete-2020-05-19-appui-occasionnel",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et du ministre des finances du 19 mai 2020, fixant les cas de l'octroi et les montants de l'appui financier occasionnel au profit des catégories pauvres et des catégories à revenu limité",
    "container-title": "Journal officiel de la République tunisienne", "issue": "45",
    "page": "1097", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2020,5,19]]}, "issued": {"date-parts": [[2020,5,20]]},
    "URL": "https://www.pist.tn/jort/2020/2020F/Jo0452020.pdf" },

  { "id": "arrete-2021-08-20-aides-covid", "citation-key": "arrete-2021-08-20-aides-covid",
    "type": "legislation", "title": "Arrêté du ministre des affaires sociales et de la chargée du ministère de l'économie, des finances et de l'appui à l'investissement du 20 août 2021, fixant les montants des aides financières occasionnelles et exceptionnelles au profit des catégories pauvres, à faible revenu et vulnérables",
    "container-title": "Journal officiel de la République tunisienne", "issue": "75",
    "page": "2069-2072", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2021,8,20]]}, "issued": {"date-parts": [[2021,8,20]]},
    "URL": "https://www.pist.tn/jort/2021/2021F/Jo0752021.pdf" },

  { "id": "decret-loi-2022-8-allocation-familiale", "citation-key": "decret-loi-2022-8-allocation-familiale",
    "type": "legislation", "title": "Décret-loi n° 2022-8 du 31 janvier 2022, complétant la loi organique n° 2019-10 du 30 janvier 2019 relative à la création du programme « AMEN SOCIAL » (article 11 bis : allocation familiale)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "13",
    "page": "336", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,1,31]]}, "issued": {"date-parts": [[2022,2,2]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo0132022.pdf" },

  { "id": "arrete-2022-04-01-transferts", "citation-key": "arrete-2022-04-01-transferts",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 1er avril 2022, modifiant l'arrêté conjoint du 19 mai 2020 fixant le mode de calcul et le montant des transferts monétaires directs au profit des catégories pauvres bénéficiant du programme « AMEN SOCIAL »",
    "container-title": "Journal officiel de la République tunisienne", "issue": "38",
    "page": "972", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,4,1]]}, "issued": {"date-parts": [[2022,4,8]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo0382022.pdf" },

  { "id": "arrete-2022-04-01-allocation-familiale", "citation-key": "arrete-2022-04-01-allocation-familiale",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 1er avril 2022, fixant les situations d'octroi et le montant des allocations familiales mensuelles au profit des catégories pauvres et des catégories à revenu limité bénéficiant du programme « AMEN SOCIAL »",
    "container-title": "Journal officiel de la République tunisienne", "issue": "38",
    "page": "973", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,4,1]]}, "issued": {"date-parts": [[2022,4,8]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo0382022.pdf" },

  { "id": "decret-2022-715-autonomisation", "citation-key": "decret-2022-715-autonomisation",
    "type": "legislation", "title": "Décret n° 2022-715 du 20 septembre 2022, portant création du programme d'autonomisation économique des catégories pauvres et des catégories à revenu limité bénéficiant du programme Amen Social et des personnes handicapées",
    "container-title": "Journal officiel de la République tunisienne", "issue": "106",
    "page": "2702-2704", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,9,20]]}, "issued": {"date-parts": [[2022,9,27]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo1062022.pdf" },

  { "id": "decret-2022-919-soins-amen", "citation-key": "decret-2022-919-soins-amen",
    "type": "legislation", "title": "Décret n° 2022-919 du 29 novembre 2022, portant création et organisation du système de soins électronique AMEN au profit des catégories pauvres et des catégories à revenu limité bénéficiant du programme Amen Social",
    "container-title": "Journal officiel de la République tunisienne", "issue": "131",
    "page": "3367-3368", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,11,29]]}, "issued": {"date-parts": [[2022,12,1]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo1312022.pdf" },

  { "id": "arrete-2022-12-08-appui-occasionnel", "citation-key": "arrete-2022-12-08-appui-occasionnel",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 8 décembre 2022, fixant les cas de l'octroi et les montants de l'appui financier occasionnel au profit des catégories pauvres et des catégories à revenu limité bénéficiant du programme Amen Social",
    "container-title": "Journal officiel de la République tunisienne", "issue": "136",
    "page": "3446-3447", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2022,12,8]]}, "issued": {"date-parts": [[2022,12,9]]},
    "URL": "https://www.pist.tn/jort/2022/2022F/Jo1362022.pdf" },

  { "id": "arrete-2023-04-03-transferts", "citation-key": "arrete-2023-04-03-transferts",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 3 avril 2023, modifiant l'arrêté conjoint du 19 mai 2020 (base mensuelle portée à 220 dinars à compter du 1er janvier 2023)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "34",
    "page": "809", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2023,4,3]]}, "issued": {"date-parts": [[2023,4,6]]},
    "URL": "https://www.pist.tn/jort/2023/2023F/Jo0342023.pdf" },

  { "id": "arrete-2024-02-28-transferts", "citation-key": "arrete-2024-02-28-transferts",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 28 février 2024, modifiant l'arrêté conjoint du 19 mai 2020 (base mensuelle portée à 240 dinars à compter du 1er janvier 2024)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "33",
    "page": "768", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2024,2,28]]}, "issued": {"date-parts": [[2024,3,1]]},
    "URL": "https://www.pist.tn/jort/2024/2024F/Jo0332024.pdf" },

  { "id": "arrete-2024-07-10-allocation-pauvres", "citation-key": "arrete-2024-07-10-allocation-pauvres",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 10 juillet 2024, portant augmentation de l'allocation monétaire attribuée aux catégories pauvres",
    "container-title": "Journal officiel de la République tunisienne", "issue": "86",
    "page": "1844", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2024,7,10]]}, "issued": {"date-parts": [[2024,7,10]]},
    "URL": "https://www.pist.tn/jort/2024/2024F/Jo0862024.pdf" },

  { "id": "arrete-2025-01-29-transferts", "citation-key": "arrete-2025-01-29-transferts",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 29 janvier 2025, modifiant l'arrêté conjoint du 19 mai 2020 (base mensuelle portée à 260 dinars à compter du 1er janvier 2025)",
    "container-title": "Journal officiel de la République tunisienne", "issue": "12",
    "page": "275", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2025,1,29]]}, "issued": {"date-parts": [[2025,1,30]]},
    "URL": "https://www.pist.tn/jort/2025/2025F/Jo0122025.pdf" },

  { "id": "arrete-2025-07-30-gluten", "citation-key": "arrete-2025-07-30-gluten",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales, du ministre de la santé et de la ministre des finances du 30 juillet 2025, fixant les modalités d'octroi de l'allocation pour la prise en charge des dépenses alimentaires aux patients allergiques au gluten",
    "container-title": "Journal officiel de la République tunisienne", "issue": "99",
    "page": "1977", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2025,7,30]]}, "issued": {"date-parts": [[2025,8,7]]},
    "URL": "https://www.pist.tn/jort/2025/2025F/Jo0992025.pdf" },

  { "id": "arrete-2025-08-29-allocation-pauvres", "citation-key": "arrete-2025-08-29-allocation-pauvres",
    "type": "legislation", "title": "Arrêté conjoint du ministre des affaires sociales et de la ministre des finances du 29 août 2025, modifiant l'arrêté conjoint du 10 juillet 2024 portant augmentation de l'allocation monétaire attribuée aux catégories pauvres",
    "container-title": "Journal officiel de la République tunisienne", "issue": "107",
    "page": "2138", "authority": "République tunisienne",
    "event-date": {"date-parts": [[2025,8,29]]}, "issued": {"date-parts": [[2025,8,29]]},
    "URL": "https://www.pist.tn/jort/2025/2025F/Jo1072025.pdf" }
]
```

**Entrées à créer mais non vérifiables en français** (à n'introduire qu'avec la mention de la
lacune) : loi n° 2024-48 du 9 décembre 2024 (LF 2025), JORT n° 149 — **fascicule français
introuvable (404)**, disponible en arabe : `https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf` ;
loi n° 2025-17 du 12 décembre 2025 (LF 2026), JORT n° 148 — l'URL en « F » **sert l'arabe**.

---

## 9. Notions à porter au glossaire (`precis/glossaire.yml`)

Aucune n'existe aujourd'hui : le glossaire compte 59 entrées, dont `cnss`, `cnrps`, `cnam`,
`smig`, `cotisations-sociales`, `fonds-de-securite-sociale`. Rappel du §5 du plan : le livre n'est
pas encore dans `BOOKS` de `scripts/build_glossary.py`.

| `id` proposé | Terme FR | Terme AR | Source canonique pressentie |
|---|---|---|---|
| `pnafn` | Programme national d'aide aux familles nécessiteuses (PNAFN) | البرنامج الوطني لمساعدة العائلات المعوزة | arrêté du 6 janvier 1987 (intitulé) ; décret n° 2012-2521, art. 5 nouveau |
| `amen-social` | AMEN social | برنامج الأمان الاجتماعي | loi organique n° 2019-10, art. 1er |
| `categories-pauvres` | Catégories pauvres | الفئات الفقيرة | loi organique n° 2019-10, art. 2 ; décret gouv. n° 2020-317, art. 19 |
| `categories-revenu-limite` | Catégories à revenu limité | الفئات محدودة الدخل | *idem* |
| `pauvrete-multidimensionnelle` | Pauvreté multidimensionnelle | الحرمان المتعدد الأبعاد | loi organique n° 2019-10, art. 2 |
| `score-eligibilite` | Score d'éligibilité (*proxy means test*) | أنموذج التنقيط | arrêté du 19 mai 2020 relatif au modèle de scoring, art. 2 |
| `condition-de-ressources` | Condition de ressources | شرط الموارد | décret gouv. n° 2020-317, art. 5 ; décret n° 98-409, art. 2 |
| `ciblage` | Ciblage | الاستهداف | loi organique n° 2019-10, art. 9 |
| `transfert-monetaire` | Transfert monétaire direct | تحويل مالي مباشر | loi organique n° 2019-10, art. 11 ; arrêté du 19 mai 2020 |
| `appui-financier-occasionnel` | Appui financier occasionnel | الدعم المادي الظرفي | loi organique n° 2019-10, art. 12 ; arrêté du 8 décembre 2022 |
| `allocation-familiale-non-contributive` | Allocation familiale non contributive | المنحة العائلية غير المساهماتية | art. 11 bis (décret-loi n° 2022-8) ; arrêté du 1er avril 2022, art. 3 |
| `amg` | Assistance médicale gratuite (AMG) | العلاج المجاني | loi n° 87-29, art. 1er |
| `amg1` | Carte de soins gratuits (AMG1) | بطاقة العلاج المجاني | décret n° 98-1812, art. 2 |
| `amg2` | Carte de soins à tarifs réduits (AMG2) | بطاقة العلاج بالتعريفة المنخفضة | décret n° 98-409, art. 2 et 10 |
| `livret-de-soins` | Livret de soins | دفتر العلاج | loi n° 87-29, art. 1er ; décret n° 88-175 |
| `quota-regional` | Quota régional (contingentement des cartes) | الحصة الجهوية | décret n° 98-1812, art. 2 ; décret n° 98-409, art. 2 et 14 |
| `registre-donnees-categories-pauvres` | Registre de données sur les catégories pauvres et à revenu limité | سجل المعطيات حول الفئات الفقيرة والفئات محدودة الدخل | loi organique n° 2019-10, art. 18 ; décret n° 2014-1526 |
| `identifiant-social` | Identifiant social | المعرّف الاجتماعي | décret gouv. n° 2020-317, art. 14 |
| `unite-locale-promotion-sociale` | Unité locale de promotion sociale | وحدة النهوض الاجتماعي المحلية | décret gouv. n° 2020-317, art. 12 et 13 |
| `enquete-sociale` | Enquête sociale | البحث الاجتماعي | décret gouv. n° 2020-317, art. 15 à 17 |
| `autonomisation-economique` | Autonomisation économique | التمكين الاقتصادي | loi organique n° 2019-10, art. 3 ; décret n° 2022-715 |
| `assistance-non-contributive` | Assistance sociale (non contributive) | المساعدة الاجتماعية | opposée à `cotisations-sociales`, déjà au glossaire |

`smig` existe déjà et est la clé de voûte de toutes les conditions de ressources (§2.4, §3.2) :
lui ajouter un `voir_aussi` vers `condition-de-ressources`.

---

## 10. Corrections à porter à openfisca-tunisia (récapitulatif)

À traiter en **PR de paramètres** distincte des correctifs de formule, sur le modèle des PR
#380 à #386.

| Paramètre | Constat | Correction |
|---|---|---|
| `pnafn/allocation` | 11 paliers sans référence | documenter l'**absence de texte** en `documentation` ; ajouter la référence de l'arrêté du 10 juillet 2024 pour le palier 180 D et son terme ; **ne pas** encoder 240/260 comme des valeurs, l'arrêté ne fixant qu'un plafond |
| `amen_social/allocation_base` | s'arrête à 240 D (2024) | ajouter **260 D au 2025-01-01** ; corriger les `reference` (« arrêté conjoint 2020-931 » n'existe pas) et les `official_journal_date` (2022-04-08, 2023-04-06, 2024-03-01 sont des dates de **publication**, l'effet est au 1er janvier) |
| `amen_social/supplements/enfant_a_charge` | 10 D au 2019-01-01, réf. « Décret n° 2019-318 » | **décret inexistant** ; date correcte 2020-05-20 ; réf. arrêté du 19 mai 2020, art. 2 |
| `amen_social/supplements/limite_age_etudiant` | 21 ans | **25 ans** (arrêté du 19 mai 2020, art. 2) |
| `amen_social/supplements/limite_age_enfant` | 18 ans au 2019-01-01 | date 2020-05-20 ; ajouter la **borne basse de 6 ans au 2022-02-01** |
| `amen_social/supplements/handicap` | réf. « Arrêté 931 du 20 mai 2020 » | référence apocryphe ; arrêté conjoint du 19 mai 2020, art. 2, dernier alinéa |
| `amen_social/eligibilite/handicap_lourd/*` | échelle 1,25 / … / 2 / 2,5 SMIG | **ne rien changer** : la portée de la majoration de + ½ SMIG (décret gouv. n° 2020-317, art. 5, dernier alinéa) n'est pas tranchée par le texte (§3.2) ; documenter l'incertitude, pas la corriger |
| `amen_social/eligibilite/*` | daté 2020-01-01 | date d'effet **2020-05-20** ; ajouter l'URL pist.tn |
| `amen_social/aides_ponctuelles/**` | datés 2019-01-01, sans référence | date **2020-05-20** ; référence arrêté du 19 mai 2020 puis arrêté du 8 décembre 2022 ; **ajouter** le transport scolaire et l'appui d'urgence 60-200 D |
| `non_contributives/allocation_familiale` | 30 D au 2020-06-01 | date **2022-04-08** ; références décret-loi n° 2022-8 et arrêté du 1er avril 2022 ; conditions « < 6 ans » et exclusion des affiliés non modélisées |
| `non_contributives/amg2` | 10 D au 2015-01-01 | date **1998-02-27**, décret n° 98-409, art. 10 |
| *(à créer)* | — | seuils d'éligibilité AMG2 en SMIG (décret n° 98-409, art. 2, modifié en 2005) ; tarifs réduits en % (art. 17, 18, 21) ; droit annuel d'affiliation à l'AMG : **6 D** (LF 1988, art. 62) puis **10 D** (LF 1991, art. 65) ; contributions aux frais de soins (LF 1988, art. 65 ; révisées par la LF 1991, art. 66) |

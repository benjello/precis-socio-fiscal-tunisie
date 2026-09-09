# Cotisations sociales — régimes du secteur privé : dossier documentaire

> Note **documentaire** préparatoire au livre « Cotisations sociales ». Elle ne rédige pas de
> prose de précis et n'a modifié aucun fichier de `precis/` ni aucun paramètre d'openfisca-tunisia.
>
> **Trois niveaux d'attestation**, portés sur chaque fait :
> - **[T]** *texte lu* — l'article a été lu dans le fascicule du JORT (couche texte ou image) ;
> - **[M]** *métadonnées* — seule la notice de `jort_cache.db` est établie (n°, dates, pages) ;
> - **[D]** *dérivé* — déduit d'un autre texte, d'un rapprochement arithmétique ou d'une
>   convention ; jamais lu tel quel.
>
> **Trois dates par texte** : signature / publication au JORT (n° de fascicule + page) / **effet
> tel que l'énonce l'article final**. Quand aucune clause d'entrée en vigueur n'a été lue, la
> case porte **« non établie »** — elle n'est jamais dérivée de la date de publication.
>
> **URL** : `https://www.pist.tn/jort/<année>/<année>F/Jo<n° sur 3 chiffres><année sur 2 chiffres
> jusqu'en 1999, 4 ensuite>.pdf`. Le certificat TLS de pist.tn est expiré depuis le 25 août 2026 :
> les vérifications ont été faites avec `curl -k`. **Les vingt-cinq URL de la bibliographie du § 12
> ont été vérifiées une à une le 9 septembre 2026** : toutes répondent `200 application/pdf`, avec
> une taille identique à l'octet près à celle du fichier du corpus local — ce qui atteste aussi
> qu'il s'agit bien de l'édition française. Seule exception, documentée au § 1.7 : le fascicule
> n° 149 de 2024, dont l'édition française répond 404. Les fascicules ont été lus sur le corpus
> local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`.
>
> **Pagination** : toutes les pages citées sont celles de l'**édition française**, sauf mention
> contraire explicite (loi de finances 2025, dont l'édition française n'existe pas).

---

## 0. Résultat principal : l'architecture des taux, et pourquoi « 1960 » est faux

Le modèle openfisca-tunisia porte 61 paramètres pour le secteur privé, dont **37 datés du
1er janvier 1960 sans référence**. Le dépouillement établit que **la structure qu'ils décrivent
n'existe pas avant 1997**, et que sa dernière pièce date de **2003**.

### 0.1 Le régime général (RSNA) se lit comme une somme de trois textes

| Bloc | Texte | Taux | Employeur | Salarié |
|---|---|---:|---:|---:|
| Taux global des régimes de la loi n° 60-30 | **loi n° 97-4**, art. 41 (nouveau) | **18,00 %** | **13,00** | **5,00** |
| Fonds spécial de l'État | **loi n° 74-101** (LF 1975), art. 57 | **0,50 %** | **0,50** | — |
| Cotisation propre du régime de pensions | **décret n° 97-555**, art. 9 (nouveau) | **5,25 %** | **2,50** | **2,75** |
| **Total** | | **23,75 %** | **16,00** | **7,75** |

**16,00 % / 7,75 %** sont exactement les totaux du modèle avant assurance maladie universelle ;
avec l'AMU (décret n° 2007-1406) ils deviennent **16,57 % / 9,18 %**, les chiffres publiés par la
CNSS. [D] — le rapprochement arithmétique est de nous ; chacun des trois taux est [T].

### 0.2 Le taux global de 18 % se ventile par branche, et la ventilation boucle exactement

| Branche | Part du taux global | Texte qui la fixe | Niv. |
|---|---:|---|---|
| Quote-part versée au régime de pensions | **7,25/20e** | décret n° 2003-1212, art. 5 b) nouveau | **[T]** |
| Assurance maladie (soins) | **4,75 %** | décret n° 2007-1406, art. 6 §1 (« 4,75 % prélevé sur le taux global des cotisations prévu par la loi n° 60-30 ») | **[T]** |
| Accidents du travail / maladies professionnelles | **1,00 point transféré** | décret n° 95-538, art. 2 (« transfert d'un point des cotisations au régime général de sécurité sociale institué par la loi n° 60-30 au profit du régime de réparation… institué par la loi n° 94-28 ») | **[T]** |
| Protection sociale des travailleurs | **0,40 %** | loi n° 96-101, art. 5 (« une cotisation complémentaire de 0,4 % des salaires **à prélever sur le taux global** des cotisations de sécurité sociale fixé par la loi n° 60-30 ») | **[T]** |
| Prestations familiales | 3,10 % | **aucun texte trouvé** | **[D]** |
| Indemnités maladie / maternité | 0,85 % | **aucun texte trouvé** | **[D]** |
| Décès et capital-décès | 0,65 % | **aucun texte trouvé** | **[D]** |
| **Total** | **18,00 %** | | |

Les quatre premières lignes sont attestées ; les trois dernières sont le **solde** (18,00 − 7,25 −
4,75 − 1,00 − 0,40 = **4,60**, soit exactement 3,10 + 0,85 + 0,65), réparti conformément aux valeurs
du modèle. C'est le principal trou
du dossier (§ 10).

Le régime de pensions cumule donc **7,25 (quote-part) + 5,25 (cotisation propre) = 12,50 %**,
valeur du modèle. [D] par addition de deux [T].

### 0.3 D'où viennent les décimales

Le taux global de 18 % est réparti **13/5** entre employeur et salarié (loi n° 97-4). Appliquée
branche par branche, cette clé donne des nombres à quatre décimales, tous multiples de **1/360**
de point :

| Branche | Global | × 13/18 (employeur) | × 5/18 (salarié) | Modèle (empl./sal.) | Concordance |
|---|---:|---:|---:|---|---|
| Assurance maladie | 4,75 | 3,4306 | 1,3194 | 3,4306 / 1,3194 | exacte |
| Maternité | 0,85 | 0,6139 | 0,2361 | 0,6139 / 0,2361 | exacte |
| Décès | 0,65 | 0,4694 | 0,1806 | 0,4694 / 0,1806 | exacte |
| Protection sociale | 0,40 | 0,2889 | 0,1111 | 0,2889 / 0,1111 | exacte |
| ATMP (point transféré) | 1,00 | 0,7222 | 0,2778 | 0,7222 / 0,2778 | exacte |
| Prestations familiales | 3,10 | 2,2389 | 0,8611 | **2,2111 / 0,8889** | **écart de 0,0278** |
| Pensions (7,25 quote-part + 2,50/2,75) | 12,50 | 7,7361 | 4,7639 | **7,7639 / 4,7361** | **écart de 0,0278** |

Les deux écarts sont **égaux et de sens opposés** (0,0278 point = 10/360) : le modèle déplace un
dixième de millième de point du poste « pensions salarié » vers « pensions employeur » et
symétriquement de « famille employeur » vers « famille salarié ». Les **totaux 16,00 / 7,75 sont
identiques**.

L'anomalie se localise exactement. Les deux seules lignes financées par le taux global qui
s'écartent de la clé 13/5 sont la **quote-part pensions** et les **prestations familiales** ; or
leur **agrégat** la respecte à la décimale près :

| | employeur | salarié |
|---|---:|---:|
| Quote-part pensions (modèle : 7,7639 − 2,50 / 4,7361 − 2,75) | 5,2639 | 1,9861 |
| Prestations familiales | 2,2111 | 0,8889 |
| **Total** | **7,4750** | **2,8750** |

et (7,25 + 3,10) = 10,35, soit × 13/18 = **7,4750** et × 5/18 = **2,8750**. Le modèle répartit donc
la somme « quote-part + famille » strictement 13/5 et ne s'écarte de la clé que dans son
**allocation interne** entre les deux postes. [D] — origine de ce déplacement non établie ; il vient
vraisemblablement d'une table de synthèse de la CNSS et non d'un texte.

**Conséquence pour le modèle.** Aucune des 37 valeurs datées de `1960-01-01` ne peut l'être :
la plus ancienne pièce de la construction est la **loi n° 97-4**, publiée le **4 février 1997**
(l'article 2, qui vise le 1er octobre 1996, ne porte que sur la réduction conventionnelle — § 1.2),
et la plus récente le **1er janvier 2003** (décret n° 2003-1212, art. 2).

---

## 1. RSNA — salariés non agricoles (régime général)

### 1.1 Création

| Fait | Texte | Signature | Publication JORT | Pages | Effet énoncé | Niv. |
|---|---|---|---|---|---|---|
| Institution des régimes de sécurité sociale et de la Caisse nationale ; champ d'affiliation (art. 34) : salariés des établissements industriels et commerciaux, professions libérales, coopératives, sociétés civiles, syndicats, associations ; transports ; commerce, VRP ; bâtiment | **Loi n° 60-30** | 1960-12-14 | n° 57, 13-16 déc. 1960 | 1602-1613 | **non établie** | **[T]** art. 34, 40-46, 61 |
| Institution du régime de pension d'invalidité, de vieillesse et de survie, et d'un régime d'allocation, dans le secteur non agricole | **Loi n° 60-33** | 1960-12-14 | n° 57 de 1960 | 1616 | non établie | [M] |
| Modalités du régime de pensions RSNA : « le taux des cotisations destinées à financer le régime… la répartition de ce taux… sont déterminés conformément aux dispositions du présent décret » (art. 1er) | **Décret n° 74-499** | 1974-04-27 | n° 30, 30 avril - 3 mai 1974 | 915-919 | non établie | **[T]** art. 1, 5, 9 |
| Régime de réparation des accidents du travail et maladies professionnelles (sort de la loi n° 60-30) | **Loi n° 94-28** | 1994-02-21 | n° 15, 22 févr. 1994 | 308-318 | non établie | [M] |
| Institution du régime de base d'assurance maladie (AMU) | **Loi n° 2004-71** | 2004-08-02 | n° 63, 6 août 2004 | 2228-2230 | non établie | [M] ; taux de 6,75 % attesté par renvoi de l'art. 15, cf. décret n° 2007-1406 art. 3 **[T]** |

URL : `https://www.pist.tn/jort/1960/1960F/Jo05760.pdf`, `…/1974/1974F/Jo03074.pdf`,
`…/1994/1994F/Jo01594.pdf`, `…/2004/2004F/Jo0632004.pdf`.

**Mise en garde reprise du dossier « prestations » et vérifiée** : la loi n° 86-86 du 1er septembre
1986 **ne crée pas** la CNSS ; son article 2 dispose que les organismes qu'elle prévoit « se
substituent » à la CNSS « instituée par la loi n° 60-30 du 14 décembre 1960 ». Architecture jamais
entrée en vigueur.

### 1.2 Évolution du taux global (article 41 de la loi n° 60-30)

| Depuis | Texte | Employeur | Salarié | Libellé | Niv. |
|---|---|---:|---:|---|---|
| origine (1960) | loi n° 60-30, **art. 41** | **15 %** | **5 %** | « Les taux de cotisations, dus pour la couverture des régimes de Sécurité Sociale prévus par la présente loi, sont ainsi fixés : — à la charge des employeurs, à 15 % des salaires, rémunérations ou gains des travailleurs qu'ils emploient ; — à la charge des travailleurs, à 5 % des salaires, rémunérations ou gains qu'ils perçoivent. » | **[T]** p. 1605 |
| **1er janvier 1975** | **loi n° 74-101** (LF 1975), **art. 57 et 58** | **+0,5 %** | — | « Le taux de la cotisation patronale due au titre des régimes de sécurité sociale et visée à l'article 41 de la loi n° 60-30 … est majoré à compter du 1er janvier 1975 de 0,5 % de l'ensemble des salaires, rémunérations ou gains … » ; art. 58 : le produit est « affecté notamment à la promotion des actions et interventions dans les domaines économiques et réparti par arrêté du Premier Ministre » | **[T]** p. 2919 |
| **publication, 4 février 1997** [D] | **loi n° 97-4**, art. 41 (nouveau) et art. 2 | **13 %** | **5 %** | art. 41 (nouveau) ; le §2 ouvre « une réduction du taux de cotisation … aux employeurs qui assurent à leurs salariés … une couverture totale ou partielle des soins de santé dans le cadre d'un régime conventionnel » ; art. 2 : « Les dispositions du paragraphe 2 … relatives à la **réduction de deux points** de la contribution mise à la charge de l'employeur sont applicables à compter du **1er octobre 1996** » ; art. 3 abroge les articles 39 à 42 de la loi n° 88-145 (LF 1989) | **[T]** p. 155 |

- Loi n° 74-101 : signature 1974-12-25, JORT n° 80 du 31 déc. 1974, p. 2919,
  `https://www.pist.tn/jort/1974/1974F/Jo08074.pdf`.
- Loi n° 97-4 : signature 1997-02-03, JORT n° 10 du 4 févr. 1997, p. 155,
  `https://www.pist.tn/jort/1997/1997F/Jo01097.pdf`.
- **Modalités de la réduction conventionnelle : décret n° 97-1645** du 25 août 1997, JORT n° 71 du
  5 sept. 1997, pp. 1676-1677, `https://www.pist.tn/jort/1997/1997F/Jo07197.pdf` — **[T]** art. 1
  à 6 : « Peuvent bénéficier d'une **réduction de deux points** du taux de cotisation au régime de
  sécurité sociale, **prévu à l'article 41 de la loi n° 60-30**, les employeurs assujettis à cette
  loi, assurant à leurs salariés ainsi qu'à leurs ayants droit … une **couverture en matière
  d'assurance maladie ordinaire et d'accouchement, dans le cadre d'un régime conventionnel** »
  (art. 1er) ; la couverture doit s'étendre aux enfants handicapés sans condition d'âge, couvrir la
  totalité des frais, et la participation du travailleur ne peut dépasser 20 % des frais calculés au
  tarif officiel (art. 2 et 3) ; la demande passe par la commission consultative d'entreprise et une
  commission instituée auprès de la CNSS (art. 4 et 5) ; « la réduction du taux de cotisation prend
  effet à partir du premier jour du trimestre suivant celui au cours duquel [la décision est prise] »
  (art. 6). **Abrogé** par le décret n° 2007-1406, art. 16 **[T]**.

**Lecture de l'article 2 de la loi n° 97-4 — point important.** La « réduction de deux points »
dont l'article 2 fixe l'application au **1er octobre 1996** est celle du **paragraphe 2** de
l'article 41 nouveau, c'est-à-dire la **réduction conventionnelle** précisée par le décret
n° 97-1645, et **non** le passage du taux de base de 15 % à 13 %. Deux conséquences :

1. **Le taux de base de 13 % n'a pas de date d'effet énoncée.** Il court, à défaut, de la
   publication de la loi, le **4 février 1997** — **[D]**, et non du 1er octobre 1996.
2. **Une variante à 11 % a existé de 1996 à 2007.** Les employeurs offrant une couverture
   conventionnelle acquittaient **11 %** au titre de l'article 41, soit un total employeur de
   **11 + 0,5 + 2,50 = 14,00 %** au lieu de 16,00 %. Le dispositif disparaît avec l'abrogation du
   décret n° 97-1645 le **1er juillet 2007**. **Le modèle openfisca-tunisia n'a aucun paramètre
   pour cette variante.** [D]
- Antécédent abrogé : **loi n° 88-145** (LF 1989), art. 39 à 45, « dispositions relatives au régime
  facultatif d'assurance maladie dans le secteur privé non agricole », JORT n° 87 de 1988,
  pp. 1797-1798 [M] — non lu.

**Chaîne complète des lois modifiant la loi n° 60-30** (recensement `jort_cache.db`, `like '%60-30%'`
doublé d'une requête FTS) : 61-9, 63-26, 64-31, 70-34, 74-101, 75-82, 80-36, 81-5, 82-71, 86-75,
88-38, 95-101, 96-65, **97-4**, 97-58, 98-91, 2007-51. **Aucun texte postérieur à 1997 ne touche
l'article 41** : résultat négatif [M], à confirmer sur les lois de finances, qui modifient l'article
41 sans le dire dans leur intitulé (c'est le cas de la loi n° 74-101).

### 1.3 Évolution du taux du régime de pensions (décret n° 74-499)

| Depuis | Texte | Global | Employeur | Salarié | Niv. |
|---|---|---:|---:|---:|---|
| 1974 | **décret n° 74-499, art. 9** | **3,75 %** | 2,50 | 1,25 | **[T]** p. 916 |
| 1er juillet 1994, par paliers | **décret n° 94-1429, art. 9 (nouveau)** | **5,75 %** | 2,50 | **3,25** (1,75 au 1er juill. 1994 ; 2,25 au 1er juill. 1995 ; 2,75 au 1er juill. 1996 ; 3,25 au 1er juill. 1997) | **[T]** pp. 1141-1142 |
| 1997 (effet non énoncé) | **décret n° 97-555, art. 9 (nouveau)** | **5,25 %** | **2,50** | **2,75** | **[T]** p. 553 |

- Décret n° 94-1429 : signature 1994-06-30, JORT n° 52 du 5 juill. 1994, pp. 1141-1142,
  `https://www.pist.tn/jort/1994/1994F/Jo05294.pdf`.
- Décret n° 97-555 : signature 1997-03-31, JORT n° 27 du 4 avril 1997, p. 553,
  `https://www.pist.tn/jort/1997/1997F/Jo02797.pdf`. **Date d'effet non établie** : l'article 2 est
  une clause d'exécution, sans clause d'entrée en vigueur.

**Quote-part prélevée sur le taux global** (article 5 b) du décret n° 74-499) :

| Depuis | Texte | Quote-part | Niv. |
|---|---|---:|---|
| 1974 | décret n° 74-499, art. 5 b) : « une quote-part égale à **1,25/20e** de la masse des cotisations patronales et ouvrières provenant des régimes de sécurité sociale définis par la loi n° 60-30 » | 1,25/20e | **[T]** |
| **1er janvier 2003** | **décret n° 2003-1212**, art. 5 b) nouveau : « Une quote-part égale à **7,25/20e** de la masse des cotisations patronales et ouvrières provenant des régimes de sécurité sociale définis par la loi n° 60-30 » ; **art. 2 : « Le présent décret prend effet à partir du 1er janvier 2003. »** | 7,25/20e | **[T]** |

Décret n° 2003-1212 : signature 2003-06-02, JORT n° 46 du 10 juin 2003, pp. 1834-1835,
`https://www.pist.tn/jort/2003/2003F/Jo0462003.pdf`.

**Chaîne complète des décrets modifiant le décret n° 74-499** [M] : 79-536, 81-188, 82-1030,
88-1137, 90-1455, 94-1429, 96-326, 97-291, **97-555**, 97-1927, 2001-779, **2003-1212**, 2007-2148.
Vérifiés et **sans effet sur les taux** : 96-326 (art. 46, délai de demande) **[T]**, 97-291
(art. 29, 38, 53) **[T]**, 2001-779 (revalorisation, art. 53 nouveau) **[T]**. Non lus : 79-536,
81-188, 82-1030, 88-1137, 90-1455, 97-1927, 2007-2148 — **TODO**.

### 1.4 Accidents du travail et maladies professionnelles

**Décret n° 95-538**, signature 1995-04-01, JORT n° 30 du 14 avril 1995, pp. 690-693,
`https://www.pist.tn/jort/1995/1995F/Jo03095.pdf`. **[T]** art. 1 à 8.

- Art. 1 : taux par branche d'activité selon dix-huit classes, de **0,60 %** (services de bureaux) à **7,20 %** (industries extractives).
- Art. 2 : « Il est procédé au **transfert d'un point** des cotisations au régime général de
  sécurité sociale institué par la loi n° 60-30 … au profit du régime de réparation … institué par
  la loi n° 94-28 … De ce fait les taux de cotisations des employeurs affiliés à la caisse nationale
  de sécurité sociale sont fixés comme suit : 1 — Services de bureaux : **0,50 %** … 18 — Industries
  extractives : **5 %**. » La réduction n'est **pas uniforme** d'une classe à l'autre (−0,10 point
  pour les services de bureaux, −2,20 points pour les industries extractives) : le « point »
  transféré est un agrégat, non un abattement appliqué classe par classe. **[T]** + **[D]** pour la
  lecture.
- Art. 3 : assiette = salaires de l'article 42 de la loi n° 60-30.
- Art. 4, 6, 7 : assiettes forfaitaires (secteur agricole hors loi n° 89-73 ; employés de maison
  0,53 / 0,75 / 1 % du SMAG ; travailleurs temporaires chez des particuliers).
- Modificatif : **décret n° 99-1010** du 10 mai 1999, JORT n° 40 du 18 mai 1999, pp. 732-734 [M],
  non lu — **TODO**.
- **Date d'effet non établie**.

**Point de vigilance pour le modèle.** `rsna/…/accident_du_travail.yaml` porte 0,7222 % employeur et
0,2778 % salarié, soit exactement le point transféré par l'article 2 réparti 13/5. La cotisation
réellement due par l'employeur au titre de la loi n° 94-28 est **en sus**, variable de 0,50 % à
5 % selon l'activité, et **entièrement patronale**. Le paramètre ne représente donc pas le taux
AT/MP mais le point prélevé sur le taux global. [D]

### 1.5 Protection sociale des travailleurs (0,4 %)

**Loi n° 96-101**, signature 1996-11-18, JORT n° 94 du 22 nov. 1996, pp. 2319-2320,
`https://www.pist.tn/jort/1996/1996F/Jo09496.pdf` ; **rectificatif** JORT n° 7 du 24 janv. 1997,
p. 114 [M].

- Art. 2 à 4 : la CNSS prend en charge les indemnités dues aux travailleurs licenciés pour raisons
  économiques ou technologiques lorsque l'entreprise est en cessation de paiement, et est subrogée
  dans leurs droits. **[T]**
- **Art. 5** : « Le système prévu au présent chapitre est financé par les montants recouvrés auprès
  des entreprises … et par **une cotisation complémentaire de 0,4 % des salaires à prélever sur le
  taux global des cotisations de sécurité sociale** fixé par la loi n° 60-30 du 14 décembre 1960. »
  **[T]**
- Art. 7 : maintien des allocations familiales et de la majoration pour salaire unique pendant les
  quatre trimestres suivant la cessation d'activité. **[T]**
- Art. 11 : clause d'abrogation et de publication — **date d'effet non établie**. **[T]**

Le libellé « **à prélever sur** le taux global » est décisif : la loi n° 96-101 **n'augmente pas**
la cotisation, elle réaffecte 0,4 point à l'intérieur des 18 %.

### 1.6 Assurance maladie universelle (AMU) — la seule série datée juste dans le modèle

**Décret n° 2007-1406**, signature 2007-06-18, JORT n° 49 du 19 juin 2007, pp. 2154-2163,
`https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf`. **[T]** art. 1 à 17.

- Art. 3 : « Le taux de cotisation au titre du régime de base d'assurance maladie prévu par
  l'article 15 de la loi n° 2004-71 … et fixé à **6,75 %** est prélevé pour les assurés sociaux en
  activité conformément à la progressivité prévue par les dispositions du présent titre. »
- **Art. 6 (RSNA)** : 1) au 1er juillet 2007, **5,32 %**, soit « **4,75 % prélevé sur le taux global
  des cotisations prévu par la loi n° 60-30** » + « **0,57 % au titre des cotisations supplémentaires
  à la charge de l'employeur** » ; 2) au 1er juillet 2008, relevé de 5,32 à **6,04 %**, le supplément
  « supporté, en totalité, par le salarié » ; 3) au 1er juillet 2009, de 6,04 à **6,75 %**, idem.
- **Art. 16 : « Le présent décret entre en vigueur à compter du premier juillet 2007 »**, et abroge
  notamment le décret n° 97-1645.

Concordance avec le modèle (`rsna/…/maladie.yaml`) : employeur 3,4306 → **4,0006** au 2007-07-01
(+0,57) ; salarié 1,3194 → **2,0394** au 2008-07-01 (+0,72) → **2,7494** au 2009-07-01 (+0,71).
Somme finale 6,75 %. **Concordance exacte** [D].

### 1.7 Perte d'emploi (0,5 % / 0,5 % au 1er janvier 2025)

**Loi n° 2024-48 du 9 décembre 2024, portant loi de finances pour l'année 2025**, **article 17**.

- Publication : **JORT n° 149 du 10 décembre 2024**. **L'édition française de ce fascicule
  n'existe pas** : `https://www.pist.tn/jort/2024/2024F/Jo1492024.pdf` répond **404** (289 octets
  de HTML) ; l'édition arabe `https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf` répond **200,
  application/pdf, 9 753 124 octets**. Article 17 en **pages 6421-6422 de la pagination arabe**.
- Contenu, **lu dans l'édition arabe** **[T]** :
  - § 1 : création d'un fonds spécial dénommé « صندوق التأمين على فقدان مواطن الشغل لأسباب اقتصادية »
    (*Fonds d'assurance contre la perte d'emploi pour raisons économiques*), destiné à financer un
    régime d'assurance contre la perte collective d'emploi pour des raisons étrangères aux deux
    parties de la relation de travail et un dispositif d'accompagnement social des travailleurs
    licenciés pour raisons économiques ; « les conditions et procédures de gestion du fonds sont
    fixées **par décret** ».
  - § 2 : ressources du fonds, dont « **معلوم اشتراك بنسبة 0.5% يحمل على كل من المؤجر والأجير
    ويوظف على كتلة الأجور المصرح بها لدى الصندوق الوطني للضمان الاجتماعي** » — *un droit de
    cotisation au taux de 0,5 % supporté par chacun de l'employeur et du salarié, assis sur la masse
    salariale déclarée auprès de la CNSS* — ainsi qu'une dotation budgétaire plafonnée à 5 MD, 14 %
    du produit de la majoration spécifique sur le tabac et les allumettes, et une taxe de 30 % sur
    les jeux par téléphone ou SMS.
  - § 4 : abrogation des articles 2 à 4 de la loi n° 2009-40 du 8 juillet 2009 (LF complémentaire
    2009) et transfert du reliquat des ressources du compte de financement des mesures
    exceptionnelles de mise à la retraite.
- **Le taux de 0,5 % de chaque côté figure donc bien dans la loi**, et non dans le décret annoncé.
  Ce point corrige une lecture antérieure du dossier « prestations sociales » selon laquelle
  l'article 17 ne créerait qu'un fonds.
- **Date d'effet** : non énoncée par l'article 17 lui-même. La date `2025-01-01` retenue par le
  modèle relève de la règle générale d'application des lois de finances à l'année budgétaire —
  **[D]**, à confirmer sur l'article premier de la loi. **TODO**.
- Le paramètre openfisca cite aujourd'hui `facture-tunisie.com` : **référence à remplacer** par
  l'URL arabe du fascicule.
- Le décret d'application prévu au § 1 n'a **pas** été trouvé dans `jort_cache.db` (requêtes
  `like '%perte d%emploi%'` sur 2024-2025 : aucun résultat). **TODO**.

### 1.8 Retraite complémentaire (3 % salarié / 6 % employeur)

**Arrêté du ministre des affaires sociales du 18 novembre 1978, portant publication du règlement
d'un régime complémentaire de pension de vieillesse, d'invalidité et de survivants**, JORT n° 79
du **vendredi 24 novembre 1978**, pp. 3374-3379,
`https://www.pist.tn/jort/1978/1978F/Jo07978.pdf`. **[T]** (lu à l'image, pp. 3374-3375).

- Arrêté, art. 1er : le règlement annexé est agréé. **Art. 2 : « Ce règlement entre en application
  à compter du 1er janvier 1974. »**
- Règlement, **art. 1er** : « Il est créé un régime complémentaire de pension de vieillesse,
  d'invalidité et de survie ci-après dénommé "régime complémentaire" **fonctionnant selon le
  principe de la répartition** et dont l'objet est de permettre aux travailleurs salariés couverts
  par le régime légal défini par le décret n° 74-499 … **d'acquérir des droits sur la tranche de
  salaire dépassant la limite fixée par ce régime pour le calcul des prestations**. »
- **Art. 2** : gestion assurée par la **CAVIS** (décret n° 76-981, art. 2 al. 2 et art. 25 al. 3).
- **Art. 3 et 4** : le régime s'applique « au titre d'employeurs adhérents, aux établissements,
  entreprises ou professions assujettis au régime légal **qui ont souscrit un contrat d'adhésion**
  au présent règlement ». L'adhésion se fait par bulletin d'adhésion remis à la CAVIS et prend effet
  au premier jour d'un trimestre civil ; elle est **acquise de plein droit** aux établissements déjà
  adhérents au 31 décembre 1973 aux régimes conventionnels visés par les décrets des 27 avril 1974
  et 19 novembre 1976. **C'est là le fondement du caractère facultatif** : le régime est
  conventionnel et repose sur l'adhésion de l'employeur.
- **Art. 6 — Cotisations** :
  - « 1°) **L'assiette de cotisation est la fraction de salaire excédant la limite fixée par le
    régime légal pour le calcul des prestations.** »
  - « 2°) Le **taux de cotisation effectivement appelé** pendant la période initiale de
    fonctionnement du régime est fixé à **4,5 %** du salaire différentiel défini à l'alinéa
    précédent. **Pour les périodes postérieures, le taux d'appel sera fixé en fonction de
    l'évolution de l'équilibre financier du régime, par décision du Comité de Gestion de la CAVIS
    soumise à l'approbation des Ministres des Finances et des Affaires Sociales.** »
  - « § 2. — Le taux de cotisation est réparti à raison de **2/3 à la charge de l'adhérent** et de
    **1/3 à la charge du participant**. »

**Trois conséquences pour le modèle.**

1. La clé **2/3 employeur – 1/3 salarié** est attestée, et les valeurs 6 % / 3 % la respectent.
2. **Le taux global de 9 % n'est fixé par aucun texte publié.** Le règlement fixe un taux d'appel
   initial de **4,5 %** et renvoie les révisions à une **décision du comité de gestion de la CAVIS**,
   soumise à approbation ministérielle mais non publiée au JORT. Le passage de 4,5 % à 9 % n'a donc
   aucune trace dans le *Journal officiel* ; il ne peut être daté. Le paramètre du modèle daté de
   `1960-01-01` est faux de plus de quatorze ans dans le meilleur des cas (l'application du règlement
   court du **1er janvier 1974**).
3. **L'assiette du modèle est erronée** : `retraite_complementaire.yaml` applique 3 % et 6 % à la
   totalité du salaire, alors que le règlement les assied sur la **seule fraction excédant le
   plafond du régime légal** (« salaire différentiel »).

Chaîne institutionnelle de la CAVIS :

| Fait | Texte | Signature | Publication JORT | Pages | Niv. |
|---|---|---|---|---|---|
| Organisation de la CAVIS | Décret n° 76-981 | 1976-11-19 | n° 72, 23 nov. 1976 | 2867-2869 | [M] |
| Modification | Décret n° 78-962 | 1978-11-07 | n° 76 de 1978 | 3184-3185 | [M] |
| Complément | Décret n° 89-268 | 1989-02-09 | n° 12 de 1989 | 270-271 | [M] |
| **Abrogation** du décret n° 76-981 | **Décret n° 94-1477** | 1994-07-04 | n° 55, 15 juill. 1994 | 1193-1194 | [M] |
| Modification du règlement (art. 21, 22, 24, 30 : pensions de survivants) — **sans effet sur les taux** | Arrêté du ministre des affaires sociales | 1997-01-27 | n° 11, 7 févr. 1997 | 183-184 | **[T]** |

La CAVIS gérait par ailleurs, par délégation, le régime de pensions du secteur agricole (loi
n° 81-6, art. 3) et du RTTE (décret n° 89-107, art. 2) **[T]**. **TODO** : établir à quel organisme
la gestion du régime complémentaire a été transférée après l'abrogation de 1994 (décret n° 94-1477,
non lu).

---

## 2. RSA — salariés agricoles

### 2.1 Création

**Loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur
agricole**, JORT n° 9 du 13 févr. 1981, pp. 265-273,
`https://www.pist.tn/jort/1981/1981F/Jo00981.pdf` ; **rectificatif** JORT n° 26 du 17 avril 1981,
p. 844 [M]. **Date d'effet : non établie** (l'article 4 du décret n° 81-224 y renvoie sans la
citer).

- Art. 1 : « Il est institué un régime de sécurité sociale au profit des travailleurs salariés et
  des coopérateurs de l'agriculture. Ce régime assure … les prestations en matière d'assurances
  sociales : maladie, maternité, décès et de pensions de vieillesse, d'invalidité et de
  survivants. » **[T]**
- Art. 2 : bénéficiaires — salariés et coopérateurs exerçant des activités considérées comme
  agricoles au sens de l'article 3 du code du travail. **[T]**
- Art. 3 : gestion CNSS ; **administration du régime de pensions déléguée à la CAVIS** (décret
  n° 76-981). **[T]**
- Art. 6 : « Les cotisations sont payables trimestriellement. Toute période de travail égale ou
  supérieure à **45 jours chez le même employeur** est comptée pour un trimestre ; toute période
  inférieure à 45 jours est négligée. » **[T]**
- **Pas de branche « prestations familiales »** dans le RSA : c'est la ligne de partage avec le
  RSAA (§ 3).

Textes de refonte : loi n° 89-73 (crée le titre III, § 3), **loi n° 95-102** du 27 nov. 1995
(JORT n° 96, p. 2224) [M], **loi n° 96-66** du 22 juill. 1996 (JORT n° 60, pp. 1603-1604) [M],
**loi n° 97-61** du 28 juill. 1997 (JORT n° 61, p. 1360) — lue **[T]**, porte sur les articles 41
al. 3 et 64 (soins des enfants), **sans effet sur les taux**.

### 2.2 Taux

| Depuis | Texte | Global | Ventilation | Niv. |
|---|---|---:|---|---|
| entrée en vigueur de la loi n° 81-6 | **loi n° 81-6, art. 18** | **6,45 %** | assiette : salaire forfaitaire = SMAG rapporté à 45 jours par trimestre, affecté d'un coefficient selon la spécialité — **ouvrier ordinaire 1 ; ouvrier spécialisé 1,5 ; ouvrier qualifié 2** ; « la répartition des cotisations entre les différents régimes et entre employeurs et travailleurs ainsi que les modalités de leur paiement sont fixées par décret » | **[T]** p. 267 |
| idem | **décret n° 81-224, art. 1er** | | **I. Assurances sociales maladie, maternité, décès : 1,20 %** — 0,9 % employeur, 0,3 % salarié. **II. Pensions de vieillesse, invalidité et survivants : 5,25 %** — 3,5 % employeur, 1,75 % salarié | **[T]** p. 426 |

**Décret n° 81-224** : signature 1981-02-24, JORT n° 13 du 27 févr. 1981, pp. 425-426,
`https://www.pist.tn/jort/1981/1981F/Jo01381.pdf`. **Art. 4 : « le présent décret … prendra effet
à partir de la date d'entrée en vigueur de la loi susvisée n° 81-6 du 12 février 1981 »** **[T]**.

Concordance modèle : 3,5 + 0,68 + 0,18 + 0,0375 = **4,3975** (employeur) et 1,75 + 0,23 + 0,06 +
0,0125 = **2,0525** (salarié), total **6,45 %** [D]. Le sous-partage des 1,20 % entre maladie
(0,91 = 0,68 + 0,23, **attesté** par le décret n° 2007-1406, art. 7), maternité (0,24) et décès
(0,05) **n'est fixé par aucun texte lu** — **[D]**.

**Conséquence** : les valeurs RSA du modèle datées `1960-01-01` datent en réalité de **1981**.

### 2.3 AMU (décret n° 2007-1406, art. 7) — et une divergence du modèle

| Depuis | Décret 2007-1406 art. 7 | Répartition | Modèle (empl. + sal.) | Écart |
|---|---:|---|---:|---|
| 1er juill. 2007 | **1,58 %** | 0,91 % existant + **0,67 %** employeur | 1,30 + 0,23 = **1,53** | **−0,05** |
| 1er juill. 2008 | **2,88 %** | +0,67 empl. / +0,63 sal. | 2,00 + 0,86 = **2,86** | **−0,02** |
| 1er juill. 2009 | **4,17 %** | +0,66 / +0,63 | 2,68 + 1,49 = 4,17 | exact |
| 1er juill. 2010 | **5,46 %** | +0,66 / +0,63 | 3,34 + 2,12 = 5,46 | exact |
| 1er juill. 2011 | **6,75 %** | +0,66 / +0,63 | 4,00 + 2,75 = 6,75 | exact |

Les deux premiers paliers du modèle **ne correspondent pas au texte** ; les trois suivants oui.
**[T]** pour la colonne du décret, **[D]** pour la comparaison. À signaler à openfisca-tunisia.

---

## 3. RSAA — régime agricole amélioré

### 3.1 Création

**Loi n° 89-73 du 2 septembre 1989, modifiant et complétant la loi n° 81-6**, JORT n° 60 des
5-8 sept. 1989, pp. 1338-1339, `https://www.pist.tn/jort/1989/1989F/Jo06089.pdf`. **[T]**

- Art. 1er : ajoute à la loi n° 81-6 un **titre III** « Dispositions particulières applicables aux
  salariés employés par certaines entreprises agricoles ».
- **Art. 86 (nouveau)** : s'applique obligatoirement aux **coopérateurs salariés** des entreprises
  agricoles ayant la forme de société, sociétés de mise en valeur, coopératives agricoles et
  personnes morales agricoles non assujetties à un régime couvrant les mêmes risques ; à **tous les
  salariés des autres exploitants agricoles employant 30 salariés permanents au moins** ; aux
  **pêcheurs employés sur des bateaux de jauge brute inférieure à 30 tonneaux**, pêcheurs
  indépendants et petits armateurs. Extension possible par décret.
- Art. 87 : l'adhésion doit couvrir l'ensemble des salariés de l'entreprise.
- Art. 88 : gestion financière distincte, CNSS et CAVIS.
- **Art. 91 et 92** : les assurés du RSAA bénéficient **des allocations familiales**, servies « du
  chef de l'assuré pour les trois premiers enfants … aux mêmes conditions et aux mêmes taux que
  ceux prévus par les articles 52 à 65 de la loi n° 60-30 ».
- **Art. 4 : « La présente loi entrera en vigueur le 1er octobre 1989. »**

### 3.2 Taux

**Art. 90 de la loi n° 81-6 (ajouté par la loi n° 89-73)** **[T]** :

> « Le taux des cotisations est fixé à **15 %** des salaires visés à l'article 89 … et se
> répartissent à raison de : — de **10 %** à la charge de l'employeur ; — de **5 %** à la charge du
> salarié ou du coopérateur ; Les travailleurs non salariés couverts par ce régime supportent la
> totalité de la cotisation. **La répartition du taux global des cotisations sus-mentionné entre les
> différentes branches couvertes, ainsi que les modalités de paiement desdites cotisations sont
> fixées par décret.** »

Concordance modèle : employeur 3,0 (famille) + 5,0 (retraite) + 1,52 (maladie) + 0,4 (maternité) +
0,08 (décès) = **10,00** ; salarié 1,5 + 2,5 + 0,76 + 0,2 + 0,04 = **5,00**. Total **15 %** [D].

**Le décret de répartition annoncé par l'article 90 n'a pas été identifié** — recherches
`like '%agricole%' and like '%cotisation%'` sur 1989-1996 : aucun résultat. **TODO** (§ 10). Seule
la part maladie est attestée : **2,28 %** (décret n° 2007-1406, art. 8 : « 2,28 % prélevé sur le
taux global des cotisations prévu par la loi n° 89-73 ») **[T]**, et 2,28 = 1,52 + 0,76 dans le
modèle.

**Conséquence** : les valeurs RSAA du modèle datées `1960-01-01`, `1977-01-01` et `1990-01-01`
datent au plus tôt du **1er octobre 1989**.

### 3.3 AMU (décret n° 2007-1406, art. 8) **[T]**

2,9 % au 1er juill. 2007 (2,28 existant + 0,62 employeur) → 4,19 % au 1er juill. 2008 (+0,62 empl.,
+0,67 sal.) → 5,47 % au 1er juill. 2009 (+0,62 / +0,66) → **6,75 %** au 1er juill. 2010
(+0,62 / +0,66). Les travailleurs exerçant pour leur propre compte supportent la totalité du
supplément. **Concordance exacte avec le modèle** [D].

---

## 4. RTNS — travailleurs non salariés

### 4.1 Création

**Décret n° 95-1166 du 3 juillet 1995, relatif à la sécurité sociale des travailleurs non salariés
dans les secteurs agricole et non agricole**, JORT n° 55 du 11 juill. 1995, pp. 1486-1489,
`https://www.pist.tn/jort/1995/1995F/Jo05595.pdf`. **[T]** art. 1 à 40.

- Art. 1er : étend aux travailleurs non salariés les articles 68 à 98, 100 à 107 et 109 à 120 de la
  loi n° 60-30 et les articles 20 à 38, 46 à 52, 54 et 57 du décret n° 74-499.
- Art. 2 : « Est considérée comme travailleur non salarié toute personne exerçant à titre principal
  une activité professionnelle, quelle que soit sa nature, pour son propre compte ou en qualité de
  mandataire » ; s'applique aussi aux artisans titulaires d'une carte professionnelle et aux
  métayers.
- Art. 4 : affiliation **obligatoire** dans le mois ; **non admise au-delà de 55 ans révolus** sauf
  40 trimestres validés.
- **Art. 39 : abroge les décrets n° 82-1359 (travailleurs indépendants non agricoles) et n° 82-1360
  (exploitants et travailleurs indépendants agricoles) du 21 octobre 1982** — les régimes
  prédécesseurs.
- **Date d'effet : non établie** (l'article 40 est une clause d'exécution ; les articles 33 et 34
  renvoient à une « date d'entrée en vigueur » qu'aucun article ne fixe).

Modificatifs : **décret n° 2002-3018** du 19 nov. 2002 (JORT n° 97, pp. 2779-2780) [M] et **décret
n° 2004-167** du 20 janv. 2004 (JORT n° 8, pp. 193-194) [M], complété par l'arrêté du 26 janv. 2004
(JORT n° 9, pp. 235-236) [M] — non lus, **TODO**.

### 4.2 Assiette forfaitaire — ce que le modèle ignore

**Art. 7** **[T]** : « Les cotisations … sont assises sur un **revenu forfaitaire**, affecté du
coefficient multiplicateur correspondant à la classe à laquelle appartient l'assuré. » Revenu de
référence : **SMIG 48 heures rapporté à 2 400 heures par an** (non agricole) ou **SMAG rapporté à
300 jours par an** (agricole).

| Classe | Coefficient (SMIG) | Coefficient (SMAG) |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 1,5 | 1,5 |
| 3 | 2 | 2 |
| 4 | 3 | 3 |
| 5 | 4 | 4 |
| 6 | 6 | 6 |
| 7 | 9 | 9 |
| 8 | 12 | 12 |
| 9 | 15 | 15 |
| 10 | 18 | 18 |

L'assuré ne peut être placé dans une classe inférieure à celle correspondant à son activité (fixée
par arrêté du ministre des affaires sociales) ; il peut opter pour une classe supérieure. Art. 8 :
l'adhésion vaut pour une année civile entière, le changement de classe ne court qu'au 1er janvier
suivant. **Aucun de ces éléments n'est présent dans openfisca-tunisia.**

### 4.3 Taux

**Art. 9** **[T]** : « Le taux des cotisations est fixé à **11 %** du revenu correspondant à la
classe à laquelle est placé l'assuré. Les cotisations se répartissent à raison de : — **7 %**
destinés à financer le régime des pensions ; — **4 %** destinés à financer le régime des assurances
sociales. »

Concordance modèle : retraite 7 % **[T]** ; maladie 3,04 + maternité 0,51 + décès 0,45 = **4,00**
[D] — **le partage interne des 4 % n'est fixé par aucun texte lu**, seule la part maladie de
**3,04 %** est attestée (décret n° 2007-1406, art. 10 : « 3,04 % prélevé sur le taux global des
cotisations prévu par le décret n° 95-1166 ») **[T]**.

Art. 15 : clause de réajustement — « si l'analyse [actuarielle quinquennale] révèle un danger de
déséquilibre financier des régimes, le taux de cotisations est réajusté ».
Art. 33 : barème de validation des services antérieurs, de 13 % (≤ 30 ans) à 20 % (> 60 ans) **[T]**.

**Conséquence** : les valeurs RTNS du modèle datées `1960-01-01` datent de **1995** au plus tôt.

### 4.4 AMU (décret n° 2007-1406, art. 10) **[T]**

3,97 % au 1er juill. 2007 (3,04 existant + 0,93 supplémentaire, **supporté par l'affilié**) →
4,90 % au 1er juill. 2008 → 5,83 % au 1er juill. 2009 → **6,75 %** au 1er juill. 2010.
**Concordance exacte avec le modèle** [D].

---

## 5. RACI — artistes, créateurs et intellectuels

### 5.1 Création

**Loi n° 2002-104 du 30 décembre 2002, relative au régime de sécurité sociale des artistes, des
créateurs et des intellectuels**, JORT n° 106 du 31 déc. 2002, pp. 3187-3190,
`https://www.pist.tn/jort/2002/2002F/Jo1062002.pdf`. **[T]** art. 1 à 8.

- Art. 1er : « Il est institué un régime spécial de sécurité sociale au profit des artistes, des
  créateurs et des intellectuels comportant **les assurances sociales, les pensions de vieillesse,
  d'invalidité et de survivants et les actions sanitaires et sociales** ».
- Art. 2 : conditions — A) prouver son appartenance au secteur culturel ou l'exercice d'une activité
  artistique ou culturelle de manière permanente, sur la base d'une pièce délivrée par les services
  du ministère chargé de la culture ; B) n'être assujetti à aucun autre régime légal ; C) ne
  bénéficier d'aucune indemnité permanente de l'État ni d'un revenu lié à une autre activité.
- Art. 3 : gestion CNSS.
- Art. 6 : affiliation obligatoire dans le mois suivant l'assujettissement.
- **Date d'effet : non énoncée.** La dernière page de la loi (p. 3190) a été lue **[T]** : les
  articles 33 à 38 traitent des dispositions transitoires et du droit d'option, et la loi s'achève
  sur la seule formule « La présente loi sera publiée au Journal Officiel de la République
  Tunisienne et exécutée comme loi de l'État. » **La date `2003-01-01` du modèle n'est donc attestée
  par aucun article** ; à défaut, la loi court de sa publication, le **31 décembre 2002**. [D]

**Décret d'application : décret n° 2003-894 du 21 avril 2003**, JORT n° 34 du 29 avril 2003,
pp. 1291-1294, `https://www.pist.tn/jort/2003/2003F/Jo0342003.pdf`. **[T]**
- Art. 2 : l'assujettissement « prend effet à compter de la date de la notification de l'avis de la
  commission consultative prévue à l'article 18 ».
- Art. 4 : assiette = revenu forfaitaire = coefficient × SMIG 48 h rapporté à 2 400 heures/an,
  « sans que ces cotisations ne soient inférieures à deux fois le SMIG ».
- **Art. 5 : classes de revenu** — classe 1 : **2** ; 2 : 2,5 ; 3 : 3 ; 4 : 4 ; 5 : 5 ; 6 : 7 ;
  7 : 10 ; 8 : 13 ; 9 : 16 ; classe 10 : **18** (coefficients du SMIG).
- Art. 6-7 : inscription au choix, changement possible une fois par an, au 1er janvier suivant.
- Art. 8 : cotisations trimestrielles, au plus tard le quinzième jour du mois suivant.
- Art. 11 : intervention du fonds de soutien de la couverture sociale des artistes prévu à
  l'article 37 de la loi n° 2002-101 (LF 2003).

### 5.2 Taux

**Loi n° 2002-104, art. 7** **[T]** : « Le taux des cotisations dues est fixé à **11 %** du revenu
correspondant à la classe à laquelle appartient l'assuré social sans que ce revenu ne soit
inférieur à deux fois le salaire minimum interprofessionnel garanti afférent au régime de
48 heures, rapporté à une durée d'occupation de 2 400 heures par an. Le taux des cotisations est
réparti comme suit : — **7 %** destiné à financer les pensions de vieillesse, d'invalidité et de
décès ; — **4 %** destiné à financer les assurances sociales. »

Architecture identique au RTNS. Le modèle date les valeurs RACI de `2003-01-01` : **non attesté**,
la loi ne comportant aucune clause d'entrée en vigueur (voir ci-dessus). **[D]**

**Anomalie du modèle à signaler.** Le partage interne des 4 % est **inversé** entre RTNS et RACI :
RTNS maternité 0,51 / décès 0,45 ; RACI maternité 0,45 / décès 0,51. Ces deux régimes ayant la
même architecture (11 % = 7 + 4) et **aucun** des deux partages n'étant fixé par un texte lu, l'un
au moins est erroné. **[D]**

### 5.3 AMU (décret n° 2007-1406, art. 11) **[T]**

3,97 % au 1er juill. 2007 (« 3,04 % prélevé sur le taux global des cotisations prévu par la loi
2002-104 » + 0,93 supplémentaire) → 4,90 % (2008) → 5,83 % (2009) → **6,75 %** (2010).
**Concordance exacte avec le modèle** [D].

---

## 6. RTFR — travailleurs à faibles revenus

### 6.1 Création

**Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories
de travailleurs dans les secteurs agricole et non agricole**, JORT n° 22 du 15 mars 2002,
pp. 603-606, `https://www.pist.tn/jort/2002/2002F/Jo0222002.pdf`. **[T]** art. 1 à 8.

- **Art. 1er** : « Il est institué un régime spécifique de sécurité sociale comprenant l'octroi des
  **prestations de soins**, des **pensions de vieillesse, d'invalidité et de survivants** ».
  Catégories : a) employés de maison ; b) personnes employées par l'État, les collectivités locales
  et les EPA non couvertes par un autre régime légal ; c) pêcheurs sur bateaux de jauge brute
  ≤ 5 tonneaux, pêcheurs indépendants et petits armateurs ; d) agriculteurs travaillant pour leur
  propre compte exploitant ≤ 5 hectares en sec ou 1 hectare en irrigué ; e) artisans travaillant à
  la pièce. Extension possible par décret.
- Art. 2 : droit d'option pour les catégories c), d) et e).
- **Pas de branche « prestations familiales »** : le régime ne couvre que soins et pensions.
- **Date d'effet : non établie**.

**Décret d'application : décret n° 2002-916 du 22 avril 2002**, JORT n° 35 du 30 avril 2002,
pp. 1058-1061, `https://www.pist.tn/jort/2002/2002F/Jo0352002.pdf`. **[T]** — **art. 31 : clause
d'exécution seule, date d'effet non établie**.

Textes d'application complémentaires [M] : arrêtés du ministre des affaires sociales du 23 juillet
2002, JORT n° 63 du 2 août 2002, pp. 1765-1766 (pièces d'affiliation des artisans à la pièce) et
p. 1767 (activités artisanales éligibles).

### 6.2 Assiette et taux — le « 0,66 SMIG » et le « 1,6667 % » sont dans deux textes différents

**Loi n° 2002-32, art. 7** **[T]** (lu à l'image, p. 603) :

> « Les cotisations dues sont fixées au taux de **7,5 %** et calculées sur la base des **2/3 du
> salaire minimum agricole garanti** pour les catégories prévues aux paragraphes b, c et d … et sur
> la base des **2/3 du salaire minimum interprofessionnel garanti** pour les catégories visées aux
> paragraphes a et e … Le taux des cotisations est réparti sur la base des **2/3 à la charge de
> l'employeur et de 1/3 à la charge du salarié**, en ce qui concerne les travailleurs qui exercent
> sous l'autorité d'un employeur. Ce taux est supporté exclusivement par les travailleurs exerçant
> pour leur propre compte. »

**Décret n° 2002-916** **[T]** (lu à l'image, p. 1060) :
- **Art. 13** : assiette = revenu mensuel forfaitaire égal à a) deux tiers du **SMIG régime
  48 heures rapporté à 200 heures par mois** pour les employés de maison et les artisans à la pièce ;
  b) deux tiers du **SMAG rapporté à 25 jours par mois** pour les personnes employées par l'État,
  les collectivités locales et les EPA, les pêcheurs, petits agriculteurs et petits éleveurs.
- **Art. 14** : « Le taux des cotisations est fixé à **7,5 %** du salaire forfaitaire … Ce taux est
  réparti sur la base de : — **2,5 % au titre des prestations de soins** ; — **5 % au titre des
  pensions de vieillesse, d'invalidité et de survivants**. »
- **Art. 15** : « — **5 % à la charge de l'employeur** ; — **2,5 % à la charge de l'employé**. Les
  pêcheurs indépendants, les petits armateurs, les petits agriculteurs, les petits éleveurs et les
  artisans supportent la totalité du taux de cotisations. »

**Lecture pour le modèle.** Les quatre paramètres RTFR (`retraite` 3,3333 / 1,6667 ;
`soin` 1,6667 / 0,8333) sont le **croisement** de deux répartitions à une dimension — branche
(5 / 2,5) et payeur (5 / 2,5) — qu'aucun texte ne croise. Ce sont donc quatre valeurs **[D]**,
non attestées. Le seuil `0.66` en unité `smig` traduit l'**assiette des deux tiers** (art. 7 de la
loi et art. 13 du décret) et non un plafond de barème : il est **[T]** quant au fond, **[D]** quant
à la forme. La référence portée par `rtfr/cotisations_employeur/soin.yaml` (décret n° 2002-916)
est exacte mais devrait être **doublée par la loi n° 2002-32, art. 7**, qui porte le taux global,
l'assiette et la clé employeur/salarié.

Le RTFR **n'est pas visé** par le décret n° 2007-1406 : le régime ne bascule pas dans la
progressivité AMU. Résultat négatif **[T]** (les articles 4 à 11 énumèrent limitativement les
régimes concernés).

---

## 7. RE — étudiants

| Fait | Texte | Signature | Publication JORT | Pages | Effet | Niv. |
|---|---|---|---|---|---|---|
| Extension des régimes de sécurité sociale aux étudiants ; institue la **cotisation forfaitaire** (art. 3 et 9) | **Loi n° 65-17** | 1965-06-28 | n° 34 de 1965 | 787 | non établie | **[M]** |
| Modification de la loi n° 65-17 | Loi n° 88-40 | 1988-05-06 | n° 33, 13-17 mai 1988 | 735-736 | non établie | [M] |
| **Champ d'affiliation** et montant initial de la cotisation | **Décret n° 92-631** | 1992-03-23 | n° 21, 3-7 avril 1992 | 426-427 | non établie | **[T]** |
| **Montant de la cotisation** | **Décret n° 2003-1544** | 2003-07-02 | n° 55, 11 juill. 2003 | 2132 | non établie | **[T]** |
| Étudiants boursiers à l'étranger | Décret n° 81-840 | 1981-06-18 | n° 43 de 1981 | 1504 | — | [M] |

**Décret n° 92-631** **[T]** (lu à l'image, p. 426), `https://www.pist.tn/jort/1992/1992F/Jo02192.pdf` :
- **Art. 1er — champ d'affiliation** : « Bénéficient du régime de sécurité sociale prévu par la loi
  sus-visée n° 65-17 du 28 juin 1965, les étudiants remplissant les conditions prévues par ladite
  loi, **qui sont régulièrement inscrits et qui poursuivent effectivement des études supérieures**
  dans l'un des établissements d'enseignement supérieur figurant sur la **liste annexée** au présent
  décret. » L'annexe énumère les établissements par université (Ez-Zitouna, Tunis I, II, III, etc.).
- **Art. 2 (version d'origine) : « La cotisation forfaitaire mise à la charge des étudiants
  bénéficiaires du régime de sécurité sociale instituée par la loi sus-visée n° 65-17 du 28 juin
  1965, est fixée à deux dinars par an. »**
- Art. 3 : le montant « est payable au moment de l'inscription de l'étudiant à l'établissement
  d'enseignement supérieur dans lequel il poursuit ses études, ou à défaut au moment du dépôt de la
  demande d'affiliation au régime de sécurité sociale des étudiants ».
- Art. 4 : clause d'exécution — **date d'effet non établie**.

Le décret ne dit rien des **branches couvertes** : elles sont celles de la loi n° 65-17, qui n'a pas
été ouverte (**TODO**). L'intitulé du régime dans le modèle (« Régime des étudiants », cotisation
unique) est cohérent avec une couverture limitée aux **soins**, mais ce point n'est **pas attesté**.

**Série du montant** : **2 D par an** (décret n° 92-631, art. 2) → **5 D par an** (décret
n° 2003-1544). Le modèle ne connaît que la seconde valeur.

**Décret n° 2003-1544, article premier** **[T]** (lu à l'image, p. 2132) :

> « Sont abrogées, les dispositions de l'article 2 du décret n° 92-631 du 23 mars 1992 et remplacées
> par les dispositions suivantes : *Article 2 (nouveau)*. — La **cotisation forfaitaire** mise à la
> charge des étudiants bénéficiaires du régime de sécurité sociale, instituée par la loi susvisée
> n° 65-17 du 28 juin 1965, est fixée à **cinq dinars par an**. »

L'article 2 du décret est une clause d'exécution : **date d'effet non établie**. La date
`2003-07-02` du modèle est la **date de signature**, retenue par convention — **[D]**.

**Correction à porter au modèle** : `re/index.yaml` cite déjà la loi n° 65-17, ce que le brief
présumé omettait ; le texte fondateur du RE est bien **la loi n° 65-17 de 1965**, le décret
n° 92-631 n'en fixant que les conditions de bénéfice et le décret n° 2003-1544 le montant.
`re/cotisation.yaml` devrait préciser que le montant est **annuel**.

**Divergence de dates à vérifier** : `jort_cache.db` donne pour la loi n° 65-17 une signature au
**28 juin 1965** et une publication au **25 juin 1965** — antériorité impossible. Le fascicule n° 34
n'a pas été ouvert. **TODO**.

---

## 8. RTTE — Tunisiens à l'étranger

**Décret n° 89-107 du 10 janvier 1989, étendant le régime de sécurité sociale aux travailleurs
tunisiens à l'étranger**, JORT n° 4 du 17 janv. 1989, pp. 98-99,
`https://www.pist.tn/jort/1989/1989F/Jo00489.pdf`. **[T]** art. 1 à 25.

- Art. 1er : étend les articles 68 à 96, 100 à 120 de la loi n° 60-30 et les articles 20 à 38, 46 à
  52, 54 et 57 du décret n° 74-499 « aux travailleurs tunisiens à l'étranger qu'ils soient salariés
  ou non salariés, qui ne sont pas couverts par une convention bilatérale de sécurité sociale ou
  par une réglementation spéciale régissant leur affiliation à la sécurité sociale ».
- Art. 2 : gestion CNSS ; **administration du régime de pensions déléguée à la CAVIS**.
- **Art. 3 : « L'adhésion au régime prévu par le présent décret est volontaire. Elle couvre
  obligatoirement la branche des assurances sociales et celle des pensions de vieillesse,
  d'invalidité et de survivants. »**
- **Art. 6 : assiette forfaitaire** = coefficient × SMIG 48 h rapporté à 2 400 heures par an ;
  **classe 1 : 2 ; classe 2 : 4 ; classe 3 : 6 ; classe 4 : 9**. « L'assuré est placé selon son
  choix dans l'une de ces 4 classes. »
- **Art. 7 : « Le taux des cotisations annuelles est fixé à 10,65 % du revenu forfaitaire … Les
  cotisations se répartissent à raison de : — 5,4 % destinés à financer le régime des assurances
  sociales ; — 5,25 % destinés à financer le régime des pensions. »**
- Art. 8 : « les cotisations … sont à la charge du travailleur » (l'employeur peut les prendre en
  charge en tout ou partie).
- **Date d'effet : non établie** (art. 25, clause d'exécution).
- Prorogation du délai de validation des services : **décret n° 91-604** du 30 avril 1991, JORT
  n° 32, p. 1008 [M].

Concordance modèle : retraite 5,25 **[T]** ; maladie 4,10 + maternité 0,74 + décès 0,56 = **5,40**
[D] — le partage interne des 5,4 % **n'est fixé par aucun texte lu** ; seule la part maladie de
**4,10 %** est attestée (décret n° 2007-1406, art. 9 : « 4,10 % prélevé sur le taux global des
cotisations prévu au décret n° 89-107 ») **[T]**.

**Conséquence** : les valeurs RTTE du modèle datées `1960-01-01` datent de **1989** au plus tôt.

### AMU (décret n° 2007-1406, art. 9) **[T]**

4,99 % au 1er juill. 2007 (4,10 + 0,89) → 5,87 % au 1er juill. 2008 (+0,88) → **6,75 %** au
1er juill. 2009 (+0,88), « supporté par les affiliés à ce régime ». **Concordance exacte avec le
modèle** [D].

---

## 9. Tableau de synthèse — quelle date pour quelle valeur

| Régime | Valeurs du modèle datées | Date la plus ancienne défendable | Texte |
|---|---|---|---|
| RSNA — toutes branches hors AMU et perte d'emploi | `1960-01-01` | **1997-02-04** (taux global de 18 %, date de publication, effet non énoncé) et **2003-01-01** (clé pensions/famille) | loi n° 97-4 ; décret n° 2003-1212 art. 2 |
| RSNA — fonds spécial de l'État | `1960-01-01` | **1975-01-01** | loi n° 74-101 art. 57 |
| RSNA — AT/MP | `1960-01-01` | **1995** (transfert du point) | décret n° 95-538 art. 2 |
| RSNA — protection sociale des travailleurs | `1960-01-01` | **1996** (publication 22 nov.) | loi n° 96-101 art. 5 |
| RSNA — perte d'emploi | `2025-01-01` | **2025-01-01** [D] | loi n° 2024-48 art. 17 |
| RSNA / RSA / RSAA / RTNS / RACI / RTTE — paliers AMU | 2007-2011 | **exactes** | décret n° 2007-1406 art. 6 à 11 |
| RSA | `1960-01-01` et `1981-01-01` | **entrée en vigueur de la loi n° 81-6** (1981) | loi n° 81-6 art. 18 ; décret n° 81-224 |
| RSAA | `1960-01-01`, `1977-01-01`, `1990-01-01` | **1989-10-01** | loi n° 89-73 art. 90 et art. 4 |
| RTNS | `1960-01-01` | **1995** | décret n° 95-1166 art. 9 |
| RACI | `2003-01-01` | **2002-12-31** (publication) ; aucune clause d'entrée en vigueur | loi n° 2002-104 art. 7 |
| RTFR | `2002-03-12` | **date d'effet non établie** ; assiette et clé dans la loi du 12 mars 2002 | loi n° 2002-32 art. 7 ; décret n° 2002-916 art. 14-15 |
| RE | `2003-07-02` | signature du décret ; **date d'effet non établie** ; **valeur antérieure de 2 D manquante** | décret n° 92-631 art. 2 ; décret n° 2003-1544 |
| RTTE | `1960-01-01` | **1989** | décret n° 89-107 art. 7 |
| Retraite complémentaire | `1960-01-01` | **1974-01-01** (entrée en application du règlement) ; le taux de 9 % lui-même n'est **pas datable** | arrêté du 18 nov. 1978, art. 2 et règlement art. 6 |

---

## 10. Ce qui n'a pas pu être établi

**A. Taux restés sans texte.**

1. **RSNA — prestations familiales 3,10 %, indemnités maladie/maternité 0,85 %, décès 0,65 %.**
   Ces trois parts du taux global de 18 % ne sont fixées par aucun texte lu. Elles sont obtenues par
   solde (18,00 − 7,25 − 4,75 − 1,00 − 0,40 = **4,60** = 3,10 + 0,85 + 0,65) et par les valeurs du
   modèle. Il existe
   vraisemblablement une décision du conseil d'administration de la CNSS ou un arrêté non recensé
   dans `jort_cache.db`.
2. **RSNA — le déplacement de 0,0278 point** entre « pensions » et « prestations familiales » dans
   la répartition employeur/salarié (§ 0.3). Origine inconnue.
3. **RSAA — la répartition des 15 % entre les cinq branches** (famille 4,5 ; pensions 7,5 ;
   maladie 2,28 ; maternité 0,6 ; décès 0,12). L'article 90 de la loi n° 81-6 la renvoie
   expressément à un décret ; **ce décret n'a pas été identifié**. Seule la part maladie de 2,28 %
   est attestée, par le décret n° 2007-1406.
4. **RSA — le partage des 1,20 % d'assurances sociales** entre maladie (0,91, attesté), maternité
   (0,24) et décès (0,05). Le décret n° 81-224 s'arrête à la ligne « assurances sociales maladie,
   maternité, décès : 1,20 % ».
5. **RTNS et RACI — le partage des 4 % d'assurances sociales** entre maladie (3,04, attesté),
   maternité et décès. Les deux régimes portent dans le modèle des valeurs **inversées** entre
   maternité et décès ; l'un des deux est faux, et rien ne permet de dire lequel.
6. **RTTE — le partage des 5,4 % d'assurances sociales** entre maladie (4,10, attesté), maternité
   (0,74) et décès (0,56).
7. **RTFR — les quatre valeurs 3,3333 / 1,6667 / 1,6667 / 0,8333.** Les textes fixent la
   répartition par branche (5 / 2,5) et la répartition par payeur (5 / 2,5) mais **jamais leur
   croisement**.
8. **Retraite complémentaire — le taux global de 9 % (6 % employeur / 3 % salarié).** L'arrêté du
   18 novembre 1978 a été lu : il fixe un **taux d'appel initial de 4,5 %** et confie ses révisions
   à une **décision du comité de gestion de la CAVIS**, non publiée au *Journal officiel*. Le
   passage de 4,5 % à 9 % **ne peut donc pas être sourcé au JORT** et n'est pas datable. Seule la
   clé 2/3 – 1/3 est attestée. S'ajoute une erreur d'assiette dans le modèle (§ 1.8).

9. **RSNA — la variante conventionnelle à 11 %** (total employeur 14,00 %) ouverte par l'article 41
   § 2 de la loi n° 60-30 et le décret n° 97-1645, en vigueur du 1er octobre 1996 au 1er juillet
   2007 : le modèle n'en porte aucune trace, et le nombre d'entreprises concernées n'est pas
   documenté.
10. **RE — les branches couvertes** par le régime des étudiants : ni le décret n° 92-631 ni le
    décret n° 2003-1544 ne les énoncent ; il faut ouvrir la **loi n° 65-17** (JORT n° 34 de 1965,
    p. 787).

**B. Dates d'effet non établies** (aucune clause d'entrée en vigueur lue) : loi n° 60-30 ;
décret n° 74-499 ; décret n° 97-555 ; décret n° 95-538 ; loi n° 96-101 ; loi n° 81-6 ;
décret n° 95-1166 ; loi n° 2002-104 ; loi n° 2002-32 ; décret n° 2002-916 ; décret n° 2003-1544 ;
décret n° 89-107 ; décret n° 92-631 ; article 17 de la loi n° 2024-48. **Loi n° 97-4** : la seule
date énoncée (1er octobre 1996) porte sur la réduction conventionnelle, non sur le taux de base.

**C. Textes identifiés mais non lus** (niveau [M] seulement) : loi n° 60-33 ; loi n° 88-145 art. 39
à 45 ; décret n° 99-1010 ; décrets n° 79-536, 81-188, 82-1030, 88-1137, 90-1455,
97-1927, 2007-2148 (chaîne du décret n° 74-499) ; décrets n° 2002-3018 et 2004-167 (chaîne du décret
n° 95-1166) ; lois n° 95-102 et 96-66 (chaîne de la loi n° 81-6) ; loi n° 65-17 ;
décret n° 76-981 et décret n° 94-1477 (CAVIS) ; décrets n° 82-1359 et
82-1360 (prédécesseurs du RTNS).

**D. Résultats négatifs, à traiter comme provisoires.**
- Aucun texte postérieur à 1997 ne modifie l'article 41 de la loi n° 60-30 : établi sur les
  **intitulés** de `jort_cache.db`, non sur le corps des lois de finances. Or la loi n° 74-101 a
  modifié l'article 41 sans que son intitulé le laisse deviner. **Le résultat n'a donc pas valeur
  probante** tant que les articles « dispositions diverses » des lois de finances 1998-2025 n'ont
  pas été dépouillés.
- Le décret d'application de l'article 17 de la loi de finances 2025 n'est pas recensé dans
  `jort_cache.db` au 9 septembre 2026.

---

## 11. Notions à porter au glossaire (`precis/glossaire.yml`)

| FR | AR | Source canonique pressentie |
|---|---|---|
| Taux global de cotisation | نسبة المساهمة الجملية | loi n° 60-30, art. 41 (nouveau, loi n° 97-4) |
| Quote-part (entre régimes) | حصة | décret n° 74-499, art. 5 b) ; décret n° 2003-1212 |
| Fonds spécial de l'État | الصندوق الخاص للدولة | loi n° 74-101, art. 57-58 |
| Assiette forfaitaire | القاعدة التقديرية | décret n° 95-1166, art. 7 ; décret n° 2002-916, art. 13 |
| Classe de revenu | صنف الدخل | décret n° 95-1166, art. 7 ; décret n° 2003-894, art. 5 |
| Coefficient multiplicateur | المعامل الضاربي | loi n° 81-6, art. 18 ; décret n° 89-107, art. 6 |
| SMAG — salaire minimum agricole garanti | الأجر الفلاحي المضمون | loi n° 81-6, art. 18 |
| Salaire forfaitaire | الأجر التقديري | décret n° 2002-916, art. 13 |
| Régime de base d'assurance maladie (AMU) | النظام الأساسي للتأمين على المرض | loi n° 2004-71, art. 15 ; décret n° 2007-1406 |
| Cotisation supplémentaire (AMU) | المساهمة الإضافية | décret n° 2007-1406, art. 6 à 11 |
| Réparation des accidents du travail et maladies professionnelles | جبر الأضرار الناتجة عن حوادث الشغل والأمراض المهنية | loi n° 94-28 ; décret n° 95-538 |
| Protection sociale des travailleurs | الحماية الاجتماعية للعملة | loi n° 96-101 |
| Perte d'emploi pour raisons économiques | فقدان مواطن الشغل لأسباب اقتصادية | loi n° 2024-48, art. 17 |
| Régime complémentaire de pensions | النظام التكميلي للجرايات | arrêté du 18 novembre 1978 |
| CAVIS — Caisse d'assurance vieillesse, invalidité et survivants | الصندوق التأمين على الشيخوخة والعجز والباقين على قيد الحياة | décret n° 76-981 ; abrogé par le décret n° 94-1477 |

---

## 12. Références candidates (CSL-JSON)

Toutes sont **à créer** : aucune de ces clés n'existe dans `precis/fr/references.json`
(les entrées déjà présentes du livre « Prestations sociales » couvrent la loi n° 60-30, la loi
n° 81-6, la loi n° 86-86 et la loi n° 96-101 — **les réutiliser** plutôt que de les dupliquer, après
vérification de la pagination française).

```json
[
  {"id":"tn-loi-1960-30","type":"legislation","title":"Loi n° 60-30 du 14 décembre 1960, relative à l'organisation des régimes de sécurité sociale","issued":{"date-parts":[[1960,12,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"57","page":"1602-1613","URL":"https://www.pist.tn/jort/1960/1960F/Jo05760.pdf"},
  {"id":"tn-loi-1974-101-art57","type":"legislation","title":"Loi n° 74-101 du 25 décembre 1974, portant loi de finances pour la gestion 1975, art. 57 et 58 (majoration de 0,5 % de la cotisation patronale)","issued":{"date-parts":[[1974,12,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"80","page":"2919","URL":"https://www.pist.tn/jort/1974/1974F/Jo08074.pdf"},
  {"id":"tn-decret-1974-499","type":"legislation","title":"Décret n° 74-499 du 27 avril 1974, relatif au régime de pension de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1974,4,27]]},"container-title":"Journal officiel de la République tunisienne","issue":"30","page":"915-919","URL":"https://www.pist.tn/jort/1974/1974F/Jo03074.pdf"},
  {"id":"tn-loi-1981-6","type":"legislation","title":"Loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole","issued":{"date-parts":[[1981,2,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"9","page":"265-273","URL":"https://www.pist.tn/jort/1981/1981F/Jo00981.pdf"},
  {"id":"tn-decret-1981-224","type":"legislation","title":"Décret n° 81-224 du 24 février 1981, fixant la répartition des cotisations de sécurité sociale dans le secteur agricole et réglant les modalités de leur versement","issued":{"date-parts":[[1981,2,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"13","page":"425-426","URL":"https://www.pist.tn/jort/1981/1981F/Jo01381.pdf"},
  {"id":"tn-decret-1989-107","type":"legislation","title":"Décret n° 89-107 du 10 janvier 1989, étendant le régime de sécurité sociale aux travailleurs tunisiens à l'étranger","issued":{"date-parts":[[1989,1,10]]},"container-title":"Journal officiel de la République tunisienne","issue":"4","page":"98-99","URL":"https://www.pist.tn/jort/1989/1989F/Jo00489.pdf"},
  {"id":"tn-loi-1989-73","type":"legislation","title":"Loi n° 89-73 du 2 septembre 1989, modifiant et complétant la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole","issued":{"date-parts":[[1989,9,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"60","page":"1338-1339","URL":"https://www.pist.tn/jort/1989/1989F/Jo06089.pdf"},
  {"id":"tn-decret-1994-1429","type":"legislation","title":"Décret n° 94-1429 du 30 juin 1994, portant amendement du décret n° 74-499 du 27 avril 1974 (taux de cotisation du régime de pensions)","issued":{"date-parts":[[1994,6,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"52","page":"1141-1142","URL":"https://www.pist.tn/jort/1994/1994F/Jo05294.pdf"},
  {"id":"tn-decret-1995-538","type":"legislation","title":"Décret n° 95-538 du 1er avril 1995, relatif à la fixation des taux de cotisations au régime de réparation des préjudices résultant des accidents du travail et des maladies professionnelles","issued":{"date-parts":[[1995,4,1]]},"container-title":"Journal officiel de la République tunisienne","issue":"30","page":"690-693","URL":"https://www.pist.tn/jort/1995/1995F/Jo03095.pdf"},
  {"id":"tn-decret-1995-1166","type":"legislation","title":"Décret n° 95-1166 du 3 juillet 1995, relatif à la sécurité sociale des travailleurs non salariés dans les secteurs agricole et non agricole","issued":{"date-parts":[[1995,7,3]]},"container-title":"Journal officiel de la République tunisienne","issue":"55","page":"1486-1489","URL":"https://www.pist.tn/jort/1995/1995F/Jo05595.pdf"},
  {"id":"tn-loi-1996-101","type":"legislation","title":"Loi n° 96-101 du 18 novembre 1996, relative à la protection sociale des travailleurs","issued":{"date-parts":[[1996,11,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"94","page":"2319-2320","URL":"https://www.pist.tn/jort/1996/1996F/Jo09496.pdf"},
  {"id":"tn-loi-1997-4","type":"legislation","title":"Loi n° 97-4 du 3 février 1997, modifiant la loi n° 60-30 du 14 décembre 1960 relative à l'organisation des régimes de sécurité sociale (article 41 nouveau)","issued":{"date-parts":[[1997,2,3]]},"container-title":"Journal officiel de la République tunisienne","issue":"10","page":"155","URL":"https://www.pist.tn/jort/1997/1997F/Jo01097.pdf"},
  {"id":"tn-decret-1997-555","type":"legislation","title":"Décret n° 97-555 du 31 mars 1997, modifiant le décret n° 74-499 du 27 avril 1974 (article 9 nouveau : taux de 5,25 %)","issued":{"date-parts":[[1997,3,31]]},"container-title":"Journal officiel de la République tunisienne","issue":"27","page":"553","URL":"https://www.pist.tn/jort/1997/1997F/Jo02797.pdf"},
  {"id":"tn-decret-1997-1645","type":"legislation","title":"Décret n° 97-1645 du 25 août 1997, relatif à la détermination des conditions et modalités de bénéfice de la réduction du taux de cotisation à la sécurité sociale pour les entreprises assurant à leurs salariés une couverture de soins de santé dans le cadre d'un régime conventionnel","issued":{"date-parts":[[1997,8,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"71","page":"1676-1677","URL":"https://www.pist.tn/jort/1997/1997F/Jo07197.pdf"},
  {"id":"tn-decret-1992-631","type":"legislation","title":"Décret n° 92-631 du 23 mars 1992, fixant les conditions de bénéfice du régime de sécurité sociale des étudiants","issued":{"date-parts":[[1992,3,23]]},"container-title":"Journal officiel de la République tunisienne","issue":"21","page":"426-427","URL":"https://www.pist.tn/jort/1992/1992F/Jo02192.pdf"},
  {"id":"tn-loi-2002-32","type":"legislation","title":"Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories de travailleurs dans les secteurs agricole et non agricole","issued":{"date-parts":[[2002,3,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"22","page":"603-606","URL":"https://www.pist.tn/jort/2002/2002F/Jo0222002.pdf"},
  {"id":"tn-decret-2002-916","type":"legislation","title":"Décret n° 2002-916 du 22 avril 2002, relatif aux modalités d'application de la loi n° 2002-32 du 12 mars 2002","issued":{"date-parts":[[2002,4,22]]},"container-title":"Journal officiel de la République tunisienne","issue":"35","page":"1058-1061","URL":"https://www.pist.tn/jort/2002/2002F/Jo0352002.pdf"},
  {"id":"tn-loi-2002-104","type":"legislation","title":"Loi n° 2002-104 du 30 décembre 2002, relative au régime de sécurité sociale des artistes, des créateurs et des intellectuels","issued":{"date-parts":[[2002,12,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"106","page":"3187-3190","URL":"https://www.pist.tn/jort/2002/2002F/Jo1062002.pdf"},
  {"id":"tn-decret-2003-894","type":"legislation","title":"Décret n° 2003-894 du 21 avril 2003, fixant les procédures et modalités d'application de la loi n° 2002-104 du 30 décembre 2002","issued":{"date-parts":[[2003,4,21]]},"container-title":"Journal officiel de la République tunisienne","issue":"34","page":"1291-1294","URL":"https://www.pist.tn/jort/2003/2003F/Jo0342003.pdf"},
  {"id":"tn-decret-2003-1212","type":"legislation","title":"Décret n° 2003-1212 du 2 juin 2003, modifiant le décret n° 74-499 du 27 avril 1974 (article 5 b nouveau : quote-part de 7,25/20e)","issued":{"date-parts":[[2003,6,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"46","page":"1834-1835","URL":"https://www.pist.tn/jort/2003/2003F/Jo0462003.pdf"},
  {"id":"tn-decret-2003-1544","type":"legislation","title":"Décret n° 2003-1544 du 2 juillet 2003, modifiant le décret n° 92-631 du 23 mars 1992, fixant les conditions de bénéfice du régime de sécurité sociale des étudiants","issued":{"date-parts":[[2003,7,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"55","page":"2132","URL":"https://www.pist.tn/jort/2003/2003F/Jo0552003.pdf"},
  {"id":"tn-loi-2004-71","type":"legislation","title":"Loi n° 2004-71 du 2 août 2004, portant institution d'un régime d'assurance maladie","issued":{"date-parts":[[2004,8,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"63","page":"2228-2230","URL":"https://www.pist.tn/jort/2004/2004F/Jo0632004.pdf"},
  {"id":"tn-decret-2007-1406","type":"legislation","title":"Décret n° 2007-1406 du 18 juin 2007, fixant l'assiette de calcul des taux de cotisations dues au titre du régime de base d'assurance maladie et ses étapes d'application","issued":{"date-parts":[[2007,6,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"49","page":"2154-2163","URL":"https://www.pist.tn/jort/2007/2007F/Jo0492007.pdf"},
  {"id":"tn-arrete-1978-11-18-retraite-complementaire","type":"legislation","title":"Arrêté du ministre des affaires sociales du 18 novembre 1978, portant publication du règlement d'un régime complémentaire de pension de vieillesse, d'invalidité et de survivants","issued":{"date-parts":[[1978,11,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"79","page":"3374-3379","URL":"https://www.pist.tn/jort/1978/1978F/Jo07978.pdf"},
  {"id":"tn-loi-2024-48-art17","type":"legislation","title":"Loi n° 2024-48 du 9 décembre 2024, portant loi de finances pour l'année 2025, art. 17 (fonds d'assurance contre la perte d'emploi pour raisons économiques)","issued":{"date-parts":[[2024,12,9]]},"container-title":"Journal officiel de la République tunisienne","issue":"149","page":"6421-6422","note":"Édition française du fascicule inexistante (HTTP 404) ; pagination de l'édition arabe.","URL":"https://www.pist.tn/jort/2024/2024A/Ja1492024.pdf"}
]
```

---

## 13. Méthode et vérifiabilité

- Métadonnées : `sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1'`,
  requêtes `LIKE` **sans accents** systématiquement doublées d'une requête `textes_fts`.
- Textes : corpus local `PDFs/JORT/<année>/fr/Jo<nnn><aa|aaaa>.pdf`. Les fascicules antérieurs à
  1997 n'ont **pas de couche texte** : ils ont été lus **à l'image**. Les fascicules 2001-2006 ont
  une couche texte à **police décalée** (décalage constant de 29 positions ASCII) : un `grep` y est
  structurellement aveugle et un résultat nul y est **sans valeur probante**. Un décaleur a été
  utilisé pour le repérage, et **tout chiffre a été relu à l'image**.
- Toutes les valeurs numériques citées dans ce dossier ont été **lues à l'image** ou proviennent
  d'une couche texte native postérieure à 1997.

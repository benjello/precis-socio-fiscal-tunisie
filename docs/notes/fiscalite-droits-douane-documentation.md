# Note documentaire : les droits de douane (histoire et textes)

Documentaliste, 23 octobre 2026. Matière du chapitre « Droits de douane » du livre Fiscalité
(branche `rediger/fiscalite-droits-douane`). Volet **histoire et textes** ; les chiffres
(recettes, taux moyens, dépenses fiscales, études) sont traités par une note parallèle. Aucun
`.qmd`, ni `recherches.yml`, ni `references.json`, ni backlog n'est modifié.

Fichier joint : `docs/notes/fiscalite-droits-douane-textes-lus.csv` (textes lus, même schéma que
la note sur le timbre : article, rubrique, avant → après, date d'effet, calcul, mode de lecture,
page, URL pist.tn, citation).

Mode de lecture : « image » (page lue à l'écran) ; « texte » (couche texte du fascicule) ;
« texte décodé » (police décalée de 29, fascicules 1999-2005, décodée selon
`docs/notes/outillage-sources.md`, § 5) ; « texte (arabe) » (couche texte de l'édition arabe,
normalisée NFKC) ; « index » (intitulé et page de `jort_cache` seulement, texte non lu). Les pages
sont celles de l'édition française, sauf mention « ar. ». Pour l'édition arabe, la page est
déduite des pieds de page voisins dans la couche texte : elle est donnée en fourchette quand le
pied de page ne la tranche pas (à confirmer à l'image).

Adresses pist.tn vérifiées le 23 octobre 2026 (`curl -k`, 200, `application/pdf`, taille
identique au fichier du corpus local) pour tous les fascicules du CSV dont la clé est nouvelle.

## 0. Ce qui vit déjà ailleurs (domicile et renvois)

| Sujet | Domicile actuel | Ancre | Ce que le chapitre douane en fait |
|---|---|---|---|
| Prélèvement conjoncturel à l'importation (5 % des droits et taxes liquidés, LFC 1991) | `_contributions_conjoncturelles.qmd` | `#sec-ccj-importation`, `#r-ccj-1991-importation` | renvoi ; le chapitre douane ajoute seulement sa **fin** : incorporé aux droits par la LF 1994, art. 71, et abrogé par l'art. 74 (§ 2.4 ci-dessous) — à verser aussi au registre du chapitre des contributions |
| Droit de consommation à l'importation (assiette valeur en douane, positions du tarif, 87-03) | `_droits_consommation.qmd` | `#sec-droits-consommation` | renvoi ; ne pas reprendre la ligne LF 1997 art. 51 (véhicules 4 CV exonérés de droits de douane), déjà au registre de ce chapitre |
| TVA à l'importation | `_tva.qmd` | (tableau du fait générateur, ligne « Importation ») | renvoi |
| FODEC et taxes affectées assises sur la valeur en douane | `_taxes_fonds_speciaux.qmd` | `#sec-fst-mise-en-place` | renvoi |
| Franchises de droits de douane des codes d'investissement (1969, 1972, 1987, 1993, 2016-2017), entreprises totalement exportatrices | `_regimes_incitation.qmd` | `#r-ri-1993-avantages`, `#sec-ri-2019-2021` | renvoi ; le chapitre douane garde les mesures **tarifaires** générales (taux, structure), pas les avantages par régime |
| Dépense fiscale « droits de douane » | `_depenses_fiscales.qmd` | `@tbl-df-par-impot` | renvoi (chiffres : autre note) |
| Recul des droits de douane dans les recettes et lien avec l'accord de 1995 | `index.qmd`, l. 56-58 (TODO documentaliste) | — | le texte peut fournir le **calendrier** (§ 2.6) ; le lien causal reste à sourcer par une étude (autre note) |
| Prélèvement sur les fruits frais au profit de la Caisse générale de compensation (décret n° 95-1212) | livre de la compensation | — | mention d'une ligne : la LF 2018, art. 39, § 5, le porte de 0,500 à 0,600 D/kg pour la banane (p. 4280) |
| Avance sur les importations de produits de consommation (art. 51 ter du code de l'IRPP et de l'IS) | `_impot_revenu.qmd` / `_impot_societes.qmd` | — | hors champ ; la LF 2018, art. 41, la porte à 15 % en 2018-2019 (p. 4280) |
| Statut et rémunération des agents des douanes | livre des rémunérations publiques | — | hors champ |

## 1. Antécédents

### 1.1 Le régime du Protectorat : l'union douanière franco-tunisienne et les textes du 29 décembre 1955

Rien n'est lu dans le texte avant 1956 : `jort_cache` commence en 1956 et le corpus local aussi.
Ce qui est établi l'est par les visas et les abrogations des textes postérieurs.

- **Le code de 1955.** La loi n° 2008-34 abroge « les dispositions du décret du 29 décembre 1955
  portant refonte et codification de la législation douanière, à partir de l'entrée en vigueur du
  code » (art. 3, JORT n° 47 du 10 juin 2008, p. 1748, texte). Un arrêté du même jour fixe les
  conditions d'application d'articles de ce code (arts 159 et 170, 74 à 8x, 188) : l'index en
  compte 23 modificatifs de 1958 à 2001 (titres seuls). Avant 1955, aucun texte de codification
  n'est identifié dans le corpus (fiche `r-douane-legislation-1955`, § 9).
- **Le tarif de 1955.** La loi n° 59-95 vise « le décret du 29 décembre 1955 (14 djoumada I
  1375), portant mise en vigueur d'un nouveau tarif des douanes à l'importation et à
  l'exportation » et l'abroge (visa et art. 4, JORT n° 43 des 18-21 août 1959, p. 886, image).
- **L'union douanière.** La convention commerciale et tarifaire franco-tunisienne du 5 septembre
  1959 s'ouvre sur : « Le régime de l'Union Douanière franco-tunisienne est abrogé et remplacé par
  les dispositions ci-après » (art. 1, JORT n° 49 du 29 septembre 1959, p. 1044, image). L'index
  signale un décret du ministre des Finances du 29 décembre 1955 « relatif au protocole
  d'application de la convention économique et financière relatif à l'union douanière ratifié par
  le décret du 29 décembre 1955 », publié en rectificatif au JORT n° 16 de 1957, p. 218 (index ;
  le fichier `1957/fr/Jo01657.pdf` du corpus ne couvre pas cette page : à vérifier).
- **La taxe de formalités douanières** date du Protectorat : « instituée par le décret du
  24 décembre 1936 portant fixation du budget de l'exercice de 1937 » (LF 1988, art. 48,
  p. 1632, image).
- **Redevances compensatrices** (index seulement) : sucres importés (décrets n° 58-163 du
  30 juin 1958 et n° 59-19 du 16 janvier 1959), stocks de thé (décret n° 58-173), produits du
  chapitre 73 (décret n° 67-99 du 1er avril 1967, suspendu par le décret n° 75-633) ; la LF 1982
  (loi n° 81-100), art. 45-48, abroge la redevance compensatrice sur les sucres, la redevance de
  sortie sur les produits miniers, la taxe spéciale sur les rhums, la taxe à la mouture et les
  taxes sur les pains azymes (index, p. 3039).

Ce que l'on sait donc de la rupture de 1959 : la Tunisie quitte l'union douanière avec la France
et se donne son propre tarif, le même jour, le 1er octobre 1959 (§ 1.2). Le contenu du tarif de
1955 et du régime antérieur (tarifs, conventions de 1898 ou de 1928, droit de l'union de 1955)
n'est pas lu : il demande le *Journal officiel tunisien* de 1955 et le *Bulletin économique et
social de la Tunisie*, absents du corpus (fiche `r-douane-union-douaniere-protectorat`).

### 1.2 Les tarifs de l'indépendance : 1959 et 1973

**Loi n° 59-95 du 20 août 1959** portant mise en vigueur d'un nouveau tarif des douanes à
l'importation et à l'exportation (JORT n° 43 des 18-21 août 1959, p. 886, image).

- Art. 1, I : « Le tarif minimum des droits de douane d'importation applicables à l'entrée dans
  le territoire douanier est fixé conformément au tableau A annexé à la présente loi. Le tarif
  général des droits de douane d'importation applicables à l'entrée dans le territoire douanier
  est fixé au triple du tarif minimum prévu à l'alinéa précédent. » ; II : tarif d'exportation au
  tableau B.
- Art. 2 : « Le tarif minimum et le tarif général entreront en vigueur le 1er octobre 1959. Le
  tarif minimum sera appliqué conformément aux stipulations des traités, conventions et
  arrangements internationaux. »
- Art. 3 : jusqu'au 30 septembre 1959, le régime en vigueur demeure ; les produits dont le taux
  est inférieur à celui du nouveau tarif bénéficient d'une réduction égale à la différence ; le
  secrétaire d'État aux Finances peut mettre fin par arrêté aux exemptions et franchises.
- Art. 4 : abroge le décret du 29 décembre 1955.
- Les tableaux A et B ne sont pas au JORT : la première page annonce en vente « Le Nouveau Tarif
  des Douanes à l'Importation et à l'Exportation (Loi N° 59-95 du 20 août 1959 et 15 safar 1379),
  N° 59-5, Prix : 1 Dinar » (p. 885, image). Taux non lus (fiche `r-douane-tableaux-tarifs`).
- Modifiée par les lois n° 61-41 du 7 juillet 1961 (JORT n° 27, p. 918) et n° 62-68 du
  17 décembre 1962 (JORT n° 62, pp. 1594-1595) (index ; abrogation citée par la loi n° 73-45).

**Convention commerciale et tarifaire avec la France du 5 septembre 1959**, ratifiée par la loi
n° 59-110 du 28 septembre 1959 (JORT n° 49 du 29 septembre 1959, p. 1036, image) et publiée par
le décret n° 59-283 (pp. 1043-1061 ; pp. 1043-1044 lues, image) : fin de l'union douanière
(art. 1) ; traitement de la nation la plus favorisée, sauf union douanière ou zone de libre-échange
et préférences de la zone franc (art. 2) ; contingents (tableaux B et C), admissions à conditions
particulières (tableaux D et E) ; conclue pour un an, en vigueur le 1er octobre 1959, renouvelable
par tacite reconduction (art. 9). Protocole additionnel : décret-loi n° 60-28 et décret n° 60-340
du 30 septembre 1960 (index).

**Loi n° 73-45 du 23 juillet 1973** portant mise en vigueur d'un nouveau tarif des douanes à
l'importation et à l'exportation (JORT n° 28 des 20-24-27 juillet 1973, p. 1134, image). Même
architecture qu'en 1959 (tarif minimum au tableau A, tarif général au triple, exportation au
tableau B, art. 1). « Les tarifs prévus par la présente loi entreront en vigueur à compter de sa
promulgation » ; l'article 16 du code des douanes (dispositions transitoires) s'applique aux
marchandises expédiées avant (art. 2). Nouveauté : « Des décrets pris sur proposition du Ministre
des Finances peuvent procéder à des amendements à la nomenclature des produits en conformité avec
la nomenclature internationale de Bruxelles » (art. 3). Abroge la loi n° 59-95 modifiée par les
lois n° 61-41 et n° 62-68 (art. 4). Tableaux non publiés au JORT (pp. 1135-1136 lues : décrets
sans rapport). Amendements de nomenclature : décrets n° 79-85 du 9 janvier 1979 et n° 79-477 du
21 mai 1979 (index).

Travaux préparatoires : Assemblée nationale, séance du 20 juillet 1973 (note 1, p. 1134). Aucun
exposé des motifs au JORT.

### 1.3 Avant l'ajustement : la gestion du tarif par les lois de finances (1970-1986)

L'index montre que, de 1976 à 1986, chaque loi de finances porte une rubrique « dispositions
douanières » avec « aménagement du tarif » et une habilitation à « réduire ou rétablir les droits
de douane en cours de gestion budgétaire » par décret (LF 1982, art. 40-41 ; LF 1983, art. 87-88 ;
LF 1984, art. 50-51 ; LF 1985, art. 44-45 ; LF 1986, art. 31-32 ; LF 1987, art. 25-29). La taxe de
formalités douanières y est retouchée (LF 1971, art. 27 ; LF 1977, art. 38 ; LF 1981, art. 20 ;
LF 1982, art. 42 ; LF 1984, art. 53-55), et 40 % de son produit est affecté puis reconduit au
profit de la Caisse générale de compensation (LF 1983, art. 86 ; LF 1984, art. 48 ; LF 1985,
art. 48 ; LF 1986, art. 78). Ces articles sont repérés par l'index ; seule la LF 1984 est lue
(pp. 3378-3380, image) : 40 % de la taxe de formalités à l'importation versés à la Caisse
générale de compensation (art. 48) ; majoration d'un demi-décime sur les droits de douane à
l'importation et la taxe de formalités, affectée à la même caisse (art. 49) ; tableau « G » de
modifications du tarif de 1973 et reconduction des suspensions (art. 50) ; habilitation annuelle
(art. 51) ; exemptions et assiette au poids de la taxe de formalités (art. 53-55).

## 2. Les réformes de l'ouverture

### 2.1 1987 : compression des taux (LF 1987, loi n° 86-106 du 31 décembre 1986)

Rubrique « II — Dispositions douanières / A — Aménagement du tarif » (JORT n° 78 des 30-31 décembre
1986, pp. 1612-1613, image) :

- Art. 25 : les taux du tarif minimum ad valorem du tableau A de la loi n° 73-45 sont remplacés
  selon une table de correspondance : « 0 % à 10 % » → 10 % ; 10,5 → 11 ; 11,5 → 12 ; 12,5 → 13 ;
  14 → 14 ; 15 → 15 ; 16 → 16 ; 17,5 → 18 ; 19 → 19 ; « de 21 % à 25,5 % inclus » → 20 ;
  26,5 → 21 ; 29 → 23 ; 29,5 → 24 ; 30,5 → 25 ; 32 → 26 ; 32,5 → 27 ; 33,5 → 28 ; 34,5 → 29 ;
  37 → 31 ; 40 → 34 ; 44 → 38 ; 46 → 40 ; 47,5 → 42 ; 48,5 → 43 ; « 52,5 % et plus » → 45 %.
  Les produits du tableau « M » sont exclus ; les suspensions et réductions échues au 31 décembre
  1986 sont reconduites au 31 décembre 1987.
- Art. 26 : les biens d'équipement sans similaires produits en Tunisie, sur liste arrêtée, sont
  ramenés à 15 % au plus.
- Art. 27 : « Le minimum de perception des droits de douane en tarif minimum ad-valorem à
  l'importation est fixé à 10 % », nonobstant les exonérations (LF 1975 art. 33, loi 77-60,
  LF 1984 art. 52, loi 85-48, décret-loi 85-14, loi 85-108, conventions, arts 99 et 170 du code).
- Art. 28 : matières premières de l'industrie pharmaceutique et des pneumatiques à 10 %.
- Art. 29 : réduction ou rétablissement des droits par décret en cours de gestion 1987.

Date d'effet : la LF 1987 n'a pas de clause générale (dernier article : 102, p. 1624, image) ; un
jour franc après la publication du 31 décembre 1986 (date de `jort_cache` ; fascicule daté des
30-31 décembre) : 2 janvier 1987.

Contexte : programme d'ajustement structurel de 1986. Aucune source de l'époque n'est lue ici
(voir § 8).

### 2.2 1988 : suppression de la taxe de formalités douanières, redevance de prestations douanières

LF 1988 (loi n° 87-83 du 31 décembre 1987), JORT n° 91 des 29-31 décembre 1987, pp. 1632-1633,
image :

- Art. 48 (« Suppression de la taxe et de la redevance sur les formalités douanières à
  l'importation et à l'exportation ») : suppression de la taxe de formalités douanières (décret du
  24 décembre 1936) et de la redevance compensatrice sur les déclarations détaillées (LF 1981,
  art. 25).
- Art. 51 (« Institution d'une redevance de prestation douanière ») : redevance de 1,5 % de la
  valeur en douane, minimum 1 D par article, sur toutes les déclarations en détail, et sur les
  exportations des produits d'un tableau (huiles, boissons, tabacs, phosphates, pétrole brut,
  cuirs, fonte et acier, cuivre, aluminium…).
- Art. 52 (« Aménagement du tarif ») : nouvelle table de taux du tableau A de 1973 — 0 → 0 ;
  10 → 17 ; 11 → 18 ; 12 → 19 ; 13 → 20 ; 14 → 21 ; 15 → 22 ; 16 → 23 ; 18 → 25 ; 19 → 26 ;
  « de 20 à 29 » → 27 ; 31 → 29 ; 34 → 32 ; 38 → 36 ; 40 → 38 ; 42 → 40 ; 43 → 41 ; 45 → 43.
  La table relève les taux bas et abaisse les plus hauts, dans l'année où disparaît la taxe de
  formalités : lecture de la note, à faire confirmer par une source de l'époque avant d'en parler
  comme d'une incorporation.
- Art. 53 : minimum de perception 10 % → 15 % ; art. 54 : biens d'équipement 15 % → 22 %.
- Art. 55-56 : refonte des dispositions préliminaires du tarif ; paragraphe D « encouragement à
  l'industrie » (intrants au minimum légal de perception, listes par décret).
- Art. 57 : réduction ou rétablissement par décret en cours de gestion 1988.

Date d'effet : pas de clause générale (dernier article : 101, p. 1637, image) ; jour franc après la
publication du 31 décembre 1987 : 2 janvier 1988.

### 2.3 1990 : le tarif à l'importation seule, en nomenclature du système harmonisé

- **Convention sur le système harmonisé** (Bruxelles, 14 juin 1983, signée par la Tunisie le
  24 janvier 1986) ratifiée par la loi n° 87-2 du 6 février 1987 (JORT n° 10 des 6-10 février
  1987, p. 191, image).
- **Loi n° 89-113 du 30 décembre 1989** relative à l'application d'un nouveau tarif des droits de
  douanes à l'importation (JORT n° 88 des 29-31 décembre 1989, p. 2142, image) :
  - art. 1, 1) : le tarif annexé « s'applique à l'importation » ; deux parties : les
    « dispositions préliminaires » (règles générales, suspensions, réductions) et le « tableau
    des taux des droits de douanes dûs à l'importation » ;
  - art. 1, 2) : « Il n'existe pas de tarif de droit de douanes à l'exportation » ; la nomenclature
    d'importation sert à la déclaration à l'exportation ;
  - art. 2 : entrée en vigueur le 1er janvier 1990 ;
  - art. 3 : abroge la loi n° 73-45 à cette date, en maintenant ses textes d'application non
    contraires ;
  - travaux préparatoires : Chambre des députés, séance du 28 décembre 1989.
  - Le code de 2008 rattache à cette loi « les règles générales pour l'interprétation de la
    nomenclature tarifaire du système harmonisé » (code, art. 19, § 3, p. 1750). Le tarif annexé
    n'est pas au JORT (fiche `r-douane-tableaux-tarifs`).
- La loi n° 89-113 reste, au 1er janvier 2026, le texte de rattachement du tarif : toutes les
  lois de finances lues jusqu'à la LF 2026 la modifient (« tarif des droits de douane à
  l'importation promulgué par la loi n° 89-113 »). Modificatif hors loi de finances : loi
  n° 2006-72 du 28 octobre 2006 (§ 7.16.2 des dispositions préliminaires, autocars de transport
  d'handicapés incessibles cinq ans ; JORT n° 88 du 3 novembre 2006, p. 3870, texte).
- La LF 1999, art. 65, porte le numéro du tarif à neuf chiffres (« La 2ème colonne est réservée
  au n° du tarif à 9 chiffres »), sous la rubrique « Harmonisation de la nomenclature douanière
  tunisienne avec la nomenclature de l'Union Européenne » (p. 2508, texte).

### 2.4 GATT, droit compensateur provisoire, prélèvement conjoncturel (1990-1994)

- **GATT** : loi n° 90-61 du 28 juin 1990 portant ratification du protocole d'adhésion « signé à
  Genève le 27 avril 1990 » (JORT n° 44 des 26-29 juin 1990, p. 839, image ; travaux préparatoires :
  séance du 25 juin 1990). `jort_cache` date la publication du 26 juin, avant la signature : le
  fascicule couvre les 26-29 juin.
- **Droit compensateur provisoire** : LF 1991 (loi n° 90-111), art. 26 (« Institution d'un droit
  compensateur provisoire ») : « dû à l'importation de certains matières et produits quelle que
  soit leur origine », produits et taux au tableau « M », liquidé et contrôlé comme les droits de
  douane (p. 2051, image). Même page : art. 25 (tableau « L » de modifications du tarif), art. 27
  (matières premières et demi-produits, § 7.2.2.3), art. 28 (intrants agricoles), art. 29
  (prorogation des suspensions au 31 décembre 1991), art. 30 (pharmacie, cinq ans), art. 31
  (suspension, réduction, rétablissement du droit compensateur et des droits de douane par
  décret en 1991). Pas de clause générale (dernier article : 97, p. 2061, image) : jour franc après
  la publication du 31 décembre 1990, soit le 2 janvier 1991.
- LF 1993 (loi n° 92-122 du 29 décembre 1992), section I « Protection de la compétitivité de la
  production nationale dans le cadre de la réforme économique » (JORT n° 88 du 31 décembre 1992,
  pp. 1673-1674, image) : art. 74 (tableau « L ») ; art. 75 (liste du droit compensateur, tableau
  « M ») ; art. 76 : « Sont réduits de dix points les taux du droit compensateur provisoire »
  (tableau « P » de la LF 1992) ; art. 77 : suspension par décret en 1993. Section III-IV
  (pp. 1678-1679) : art. 115 (régime des Tunisiens résidents à l'étranger, art. 33 nouveau de la
  LF 1975 : franchise des matériels et biens d'équipement, camion compris, après deux ans de séjour
  à l'étranger, incessibilité cinq ans) ; art. 116 (équipements touristiques à 10 %) ; art. 118
  (prorogation pour 1993 du prélèvement conjoncturel de la LFC 1991, art. 6) ; art. 122
  (prorogation au 31 décembre 1993 des suspensions et réductions échues). Pas de clause générale
  (dernier article : 123, p. 1679) : jour franc après la publication du 31 décembre 1992, soit le
  2 janvier 1993.
- LF 1994 (loi n° 93-125 du 27 décembre 1993), « Soutien de la compétitivité de la production
  nationale dans le cadre de la réforme économique » (JORT n° 100 du 31 décembre 1993,
  pp. 2201-2202, image) :
  - art. 68-69 : le droit compensateur devient « droit complémentaire provisoire » (tableau « N »),
    taux réduits de dix points ;
  - art. 70 : modifications du tarif (tableau « P ») ;
  - art. 71 (« Incorporation du prélèvement conjoncturel dans les droits de douane et aménagement
    des droits de douane ») : « Taux au 31 décembre 1993 » → « Taux à partir du 1er janvier
    1994 » : 0 → 0 ; 10 → 10 ; 17 → 20 ; 18 → 22 ; 19 → 23 ; 20 → 24 ; 21 → 25 ; 22 → 26 ;
    23 → 27 ; 25 → 29 ; 26 → 30 ; 27 → 31 ; 29 → 33 ; 30 → 34 ; 31 → 35 ; 32 → 36 ; 33 → 37 ;
    34 → 38 ; 35 → 39 ; 36 → 40 ; 38 → 42 ; 40 → 43 ; 43 → 43 ; « Sont exclus … les taux des
    droits de douane consolidés dans le cadre de l'Accord Général sur les Tarifs Douaniers et le
    Commerce » (§ 2) ;
  - art. 74 : abroge l'art. 6 de la LFC 1991 (prélèvement conjoncturel) ;
  - art. 75 : redevance de prestations douanières portée à « 2 % du montant des droits et taxes
    liquidés en douane sur toutes les déclarations en douane à l'importation avec un minimum de
    perception de cinq dinars par article », dont 10 % affectés aux dépenses spécifiques des agents
    des douanes ;
  - art. 76 : suspension, réduction, rétablissement par décret en 1994 ;
  - art. 77 : « Les dispositions de la présente loi sont applicables à compter du 1er janvier
    1994 ».
- **Uruguay Round / OMC** : loi n° 95-6 du 23 janvier 1995 portant ratification des accords de
  l'Uruguay Round « signés à Marrakech le 15 avril 1994 » (JORT n° 9 du 31 janvier 1995, p. 271,
  texte) ; publication par le décret n° 98-1009 du 5 mai 1998 (JORT n° 46 du 9 juin 1998, p. 1251,
  texte). Les listes de consolidation ne sont pas publiées au JORT lu.
- **Pratiques déloyales et sauvegarde** (index seulement) : décret n° 93-695 du 5 avril 1993
  (droit compensateur contre les pratiques déloyales) ; décret n° 94-1745 ; loi n° 98-106 du
  18 décembre 1998 relative aux mesures de sauvegarde à l'importation (JORT n° 102, pp. 2451-2454) ;
  loi n° 99-9 du 13 février 1999 (pratiques déloyales, JORT n° 15, pp. 279-283) ; décret
  n° 2000-477. Le code de 2008 renvoie à cette législation (art. 6, § 2).

### 2.5 La fin du droit compensateur et le démantèlement de 1996-2007 (LF 1997)

LF 1997 (loi n° 96-113 du 30 décembre 1996), JORT n° 105 du 31 décembre 1996, p. 2580, texte :

- Art. 18 : exonération de droits de douane et de taxes d'effet équivalent des équipements sans
  similaires fabriqués localement visés par les articles 9, 30, 41, 50 et 56 du code
  d'incitations ; art. 19 : TVA de 10 % sur ces équipements, hors agriculture et pêche.
- Art. 20 : « Est supprimé à compter du 31 décembre 1997 le droit compensateur provisoire ».
- Art. 21 (« Démantèlement progressif des droits de douane pour la période 1996-2007 ») : « Les
  dispositions fiscales figurant dans l'accord ratifié par la loi n° 96-49 du 20 juin 1996
  établissant une Association entre la République Tunisienne, d'une part et l'Union Européenne et
  ses Etats membres d'autre part, entrent en vigueur en considérant le 1er janvier 1997 comme étant
  le début de la deuxième année du calendrier d'application dudit accord. »
- Art. 52 (p. 2583) : suspension, réduction, rétablissement par décret en 1997.
- Date d'effet : 1er janvier 1997 (clause générale, art. 54, d'après la note sur le timbre ;
  rubrique « Fixation de la date d'application » vue p. 2583).

Ce que l'article 21 établit : la Tunisie applique le calendrier tarifaire de l'accord **avant**
son entrée en vigueur, la première année étant 1996.

### 2.6 L'accord d'association avec l'Union européenne

- Signé à Bruxelles le 17 juillet 1995 ; ratifié par la loi n° 96-49 du 20 juin 1996 (JORT n° 51
  du 25 juin 1996, p. 1311, texte ; Chambre des députés, séance du 11 juin 1996) ; publié par le
  décret n° 98-1273 du 18 mai 1998 (JORT n° 49 du 19 juin 1998, p. 1326, texte), dont la note
  dit : « L'accord sera publié dans un fascicule annexé au présent JORT » (fascicule absent du
  corpus).
- Texte lu au *Journal officiel des Communautés européennes* L 97 du 30 mars 1998 (copie du SEAE,
  rangée dans `tunisia-data`, § 7) :
  - art. 6 : zone de libre-échange établie « pendant une période de transition de douze années au
    maximum à compter de la date d'entrée en vigueur » (p. L 97/4) ;
  - art. 8 : aucun droit nouveau ni taxe d'effet équivalent ; art. 9 : les produits industriels
    tunisiens entrent dans la Communauté en exemption ;
  - art. 11 (pp. L 97/5-6), pour les produits industriels originaires de la Communauté importés en
    Tunisie :
    - § 1 : droits supprimés dès l'entrée en vigueur pour les produits **hors** annexes 3 à 6 ;
    - § 2, annexe 3 : 85 % du droit de base à l'entrée en vigueur, puis 70, 55, 40, 25 %, et
      suppression à cinq ans ;
    - § 3, annexe 4 : 92 % à l'entrée en vigueur, puis −8 points par an (84, 76, 68, 60, 52, 44,
      36, 28, 20, 12, 4 %), suppression à douze ans ;
    - § 3, annexe 5 : rien pendant trois ans ; 88 % à quatre ans, puis 77, 66, 55, 44, 33, 22,
      11 %, suppression à douze ans ;
    - § 5 : droit de base = droit effectivement appliqué à l'égard de la Communauté le
      1er janvier 1995 ; § 6 : une réduction erga omnes postérieure remplace le droit de base ;
  - art. 12 : annexe 6 hors calendrier, réexamen à quatre ans ; art. 13 : les droits de douane à
    caractère fiscal sont aussi supprimés ;
  - art. 14 : droits majorés ou rétablis à titre exceptionnel (industries naissantes, secteurs en
    restructuration), 25 % ad valorem au plus, 15 % des importations industrielles de la
    Communauté au plus, cinq ans au plus, et au plus tard jusqu'à la fin des douze ans ;
  - art. 15-18 : produits agricoles par protocoles, libéralisation à examiner à partir du
    1er janvier 2000 ;
  - art. 96 : entrée en vigueur le premier jour du deuxième mois suivant les notifications ;
    l'accord remplace l'accord de coopération de 1976 (§ 2).
- Les annexes 3 à 6 sont des listes de codes de la nomenclature combinée, sans intitulé (annexe 3
  à partir de la p. L 97/37, annexe 4 de la p. L 97/45, annexe 5 de la p. L 97/51) : la
  désignation courante de ces listes (« biens non fabriqués localement », etc.) n'est pas dans le
  texte et ne doit pas être écrite sans autre source.
- Date d'entrée en vigueur, 1er mars 1998 : « L'Accord d'Association, entré en vigueur le 1er mars
  1998 » (page de l'accord sur le site du SEAE, https://www.eeas.europa.eu/node/11560_en, lue le
  23 octobre 2026 ; source secondaire) ; la notice d'entrée en vigueur du JOCE n'est pas lue (EUR-Lex refuse les téléchargements automatisés, réponse 202 vide). Avec la LF 1997, art. 21
  (première année = 1996), le calendrier de douze ans court donc de 1996 à 2007, ce que dit
  l'intitulé de l'article 21.
- Antécédents : accord créant une association CEE-Tunisie, publié par le décret n° 69-293 du
  2 août 1969 (JORT n° 31, pp. 1020-1043, index) ; prorogations et protocoles (décrets n° 71-86,
  74-583, 75-154) ; accord de coopération signé à Tunis le 25 avril 1976 (cité par l'art. 96 de
  l'accord de 1995).
- Suites (index, sauf mention) : échange de lettres sur les protocoles agricoles (loi n° 2001-25,
  décret n° 2001-1724) ; produits agricoles transformés (décret n° 2010-2756) ; protocoles de 2008
  (loi n° 2008-24), 2020 (loi organique n° 2020-32) et 2021 (loi organique n° 2021-32) ;
  amendement adopté par décision du conseil d'association n° 01/2025 du 22 janvier 2025, approuvé
  par la loi organique n° 2025-21 du 31 décembre 2025 (JORT n° 156 du 31 décembre 2025,
  pp. 3680-3681, texte) et ratifié par le décret n° 2025-488 (p. 3685). Objet de l'amendement non
  lu (annexe).
- Mise en œuvre dans le tarif (texte) : LF 1999, art. 34 (§ 8 des dispositions préliminaires :
  relèvement ou rétablissement par décret « conformément aux dispositions des conventions
  internationales … relatives à l'institution des mesures tarifaires exceptionnelles »), art. 35
  (ventes locales des entreprises totalement exportatrices aux « taux de démantèlement prévus aux
  articles 10 et 11 de l'accord »), pp. 2503-2504 ; LF 2004, art. 14 (§ 7.26 : exonération des
  intrants sans similaires locaux lorsque le produit fini similaire bénéficie « d'un taux de
  démantèlement inférieur à 10 % » au titre des articles 10 et 11 de l'accord, p. 3722) ; LF 2006,
  art. 33 (équipements et matières de l'annexe IV de l'accord ramenés à 15 %, p. 3600).
- Les décrets annuels qui ont appliqué le calendrier aux produits d'origine communautaire ne sont
  pas identifiés ici (fiche `r-douane-decrets-demantelement-ue`).

### 2.7 Les accords de libre-échange et accords commerciaux

| Partenaire | Signature | Texte tunisien | JORT, page | Lecture |
|---|---|---|---|---|
| France (convention commerciale et tarifaire) | Tunis, 5 sept. 1959 | loi n° 59-110 du 28 sept. 1959 ; décret n° 59-283 | n° 49/1959, p. 1036 ; pp. 1043-1061 | image (pp. 1036, 1043-1044) |
| Pays arabes (convention pour faciliter et développer les échanges commerciaux, base de la Grande zone arabe de libre-échange) | — | loi n° 81-41 du 29 mai 1981 | n° 38/1981, p. 1323 | index |
| Grande zone arabe de libre-échange (règlement des différends) | — | loi n° 2007-11 du 12 févr. 2007 ; décret n° 2007-506 | n° 13/2007, p. 365 ; n° 23/2007, p. 893 | index |
| Union du Maghreb arabe (convention commerciale et tarifaire) | Ras Lanouf, 10 mars 1991 | loi n° 91-46 du 22 juil. 1991 | n° 53/1991, p. 1344 | image |
| UMA (échange des produits agricoles) | Alger, 23 juil. 1990 | loi n° 91-1 du 11 févr. 1991 ; décret n° 95-1719 | n° 13/1991, p. 279 ; n° 79/1995, p. 1875 | index |
| Jordanie | Tunis, 22 avril 1998 | loi n° 98-80 du 2 nov. 1998 | n° 89/1998, p. 2181 | texte |
| Égypte | Le Caire, 5 mars 1998 | loi n° 99-17 du 1er mars 1999 | n° 19/1999, p. 347 | texte décodé |
| Maroc | Rabat, 16 mars 1999 | loi n° 99-34 du 30 avril 1999 ; décret n° 2000-1125 | n° 37/1999, p. 683 ; n° 44/2000, pp. 1325-1326 | texte décodé (loi) ; index (décret) |
| Libye | Tripoli, 14 juin 2001 | loi n° 2001-114 du 26 nov. 2001 ; règles d'origine : loi n° 2006-4, décret n° 2006-628 | n° 95/2001, p. 3995 | texte décodé (loi 2001-114) |
| Irak (protocole exécutif) | — | loi n° 2001-115 du 26 nov. 2001 | n° 95/2001, p. 3995 | texte décodé (intitulé et article unique, date de signature illisible dans la colonne) |
| Accord d'Agadir (États arabes méditerranéens) | Rabat, 25 févr. 2004 | loi n° 2004-58 du 27 juil. 2004 ; décret n° 2004-2176 | n° 60/2004, p. 1940 ; n° 76/2004, p. 2758 | texte décodé (loi) |
| Syrie | Damas, 15 avril 2002 | loi n° 2004-82 du 6 déc. 2004 ; décrets n° 2005-354 et 2005-1224 | n° 98/2004, p. 3336 | texte décodé (loi) |
| AELE | Genève, 17 déc. 2004 | loi n° 2005-34 du 11 mai 2005 ; décret n° 2005-1529 | n° 38/2005, p. 1061 (rectificatif : n° 41/2005, p. 1130) ; n° 41/2005, p. 1133 | texte décodé |
| Turquie | Tunis, 25 nov. 2004 | loi n° 2005-36 du 11 mai 2005 ; décret n° 2005-1530 ; amendement des tableaux A et B du protocole II : loi organique n° 2013-39 | n° 38/2005, p. 1061 ; n° 41/2005, p. 1133 ; n° 81/2013, p. 2917 | texte décodé (loi 2005-36) ; texte (intitulé 2013-39) |
| Agadir (adhésion de nouveaux États) | — | loi organique n° 2018-6 ; décret présidentiel n° 2018-10 | n° 13/2018, pp. 379-380 | index |
| COMESA (adhésion) | — | loi organique n° 2019-33 du 10 avril 2019 ; décret présidentiel n° 2019-55 | n° 30/2019, pp. 980-981 | texte |
| Zone de libre-échange continentale africaine | Kigali, 21 mars 2018 | loi organique n° 2020-34 du 7 août 2020 ; décret présidentiel n° 2020-76 | n° 80/2020, pp. 1727-1729 | texte |
| AELE (amendement du protocole B, règles d'origine, décision mixte n° 01/2024 du 9 oct. 2024) | — | loi organique n° 2025-20 du 31 déc. 2025 ; décret n° 2025-487 | n° 156/2025, pp. 3680, 3684-3685 | texte |

Points à retenir :

- Les lois de ratification sont des articles uniques ; les conventions et leurs listes ne sont pas
  au JORT lu. Les dates d'entrée en vigueur et les calendriers de démantèlement de chaque accord
  ne sont donc pas établis ici (seul celui de l'Union européenne est lu).
- **Turquie : mesures exceptionnelles par loi de finances.** LF 2018, art. 40 : produits d'origine
  turque des chapitres 33, 34, 40, 48, 61 à 64, 72, 76, 84 et 85 de la deuxième liste de l'accord
  « soumis aux droits de douane dans la limite de 90 % des droits appliqués selon le droit
  commun », pour deux ans à partir du 1er janvier 2018, puis suppression sur trois ans (p. 4280,
  texte). LF 2020, art. 52 : durée portée à quatre ans à partir du 1er janvier 2018, suppression
  sur trois ans ensuite (pp. 4709-4710 ar., texte arabe). LF 2024, art. 44 : produits de
  l'annexe 1, droits dans la limite de 75 % du droit commun, pour trois ans à partir du 1er janvier
  2024, suppression progressive sur deux ans à partir de la quatrième année (p. 6444 ar.
  environ, texte arabe).
- Le code de 2008, art. 4 : les marchandises sont soumises à la loi tarifaire « sauf dérogations
  expresses prévues par les traités et conventions commerciaux en vigueur » ; art. 7 : mesures
  tarifaires de rétorsion par décret (p. 1748-1749).

### 2.8 Les étapes du tarif autonome de 2004 à 2022

Texte, sauf mention. Chaque loi de finances retouche des produits ; ne figurent ici que les
articles qui transposent une **bande de taux** en une autre.

| Effet | Texte | Contenu |
|---|---|---|
| 1er janv. 2004 | LF 2004, art. 13 (p. 3722, texte décodé) | « Sont réduits, les taux de droits de douane prévus par le tarif » : 18 et 19 → 17 ; 21 → 20 ; 23 à 26 → 22 ; 28 à 35 → 27 ; 37 à 42 → 36 % |
| 1er janv. 2005 | LF 2005, art. 28 (p. 3435, texte décodé) | produits agricoles, agro-alimentaires et textiles (chap. 1, 2, 4 à 24, 29, 33, 35, 38, 41, 43, 50 à 63) : taux remplacés par les taux consolidés de l'Uruguay Round, avec réduction : 25 → 22 ; 30, 32, 35 → 27 ; 62, 65, 72 → 60 ; 75, 76, 80, 90 → 73 ; 110, 120, 125 → 100 ; 170, 175, 180, 200 → 150 % |
| 1er janv. 2006 | LF 2006, art. 33 (p. 3600, texte) | équipements, matières et articles du tableau « H » de la LF 2000 et de l'annexe IV de l'accord d'association : 17, 20, 22 → 15 % |
| 1er janv. 2007 | LF 2007, art. 23 (p. 4385, texte) | certains équipements, matières et produits : 20 → 17 ; 100 → 73 ; 150 → 73 % |
| 1er janv. 2008 | LF 2008, art. 14 (p. 4359, texte) | matières premières, demi-produits, équipements et autres : 22 → 17 ; 73 → 60 % ; art. 15-16 : tableaux « G » et « H » |
| 1er janv. 2009 | LF 2009, art. 12 (p. 4275, texte) | 17 → 15 ; 43 → 36 ; 60 → 36 % |
| 1er janv. 2011 | LF 2011, art. 10 (p. 3462, texte) | « est réduit de 36 % à 30 % le taux … dus sur les matières premières, les produits semi-finis, les équipements et autres produits relevant des chapitres de 25 à 97 » ; art. 11 : tableau « G » |
| 1er janv. 2016 | LF 2016, art. 41 à 43 (pp. 3607-3608 ar., texte arabe) | chapitres 25 à 97 : 30 → 20 ; 27 → 20 ; 15 → 0 ; 10 → 0 % ; art. 42 : 20 % pour les produits de l'annexe 2 ; art. 43 : 0 ou 20 % pour ceux de l'annexe 3 |
| 1er janv. 2018 | LF 2018, art. 39 (pp. 4279-4280, texte) | rubrique « Mesures tarifaires pour la maîtrise du déficit de la balance commerciale » : taux de l'annexe 1 ; « sous réserve des taux des droits de douane consolidés », certains équipements et produits des chapitres 25 à 97 « relevés de 20 % à 30 % » et, pour l'annexe 2, « de 0 % à 15 % » ; § 4 : exonération des intrants sans similaires (art. 14 de la LF 2004) |
| 1er janv. 2019 | LF 2019, art. 81 (pp. 5465-5466 ar., texte arabe) | motocycles (position 87.11) relevés, dont 30 % pour ceux de 50 à moins de 125 cm³ (tableau lu en partie) |
| 1er janv. 2022 | LF 2022, art. 57 (pp. 3099-3100, texte) | « Révision des droits de douane appliqués aux produits de consommation ou ayant un similaire fabriqué localement » : relevés « de 20 % ou 30 %, ou 36 % à 43 % ou 50 % » selon un tableau de chapitres et positions (43 % : notamment 25.15 à 25.23, 32.08-32.09, 33.03 à 33.07, 34.01, chap. 42, 65 à 70, 84.50, 85.16, 94.01, 94.03 à 94.05 ; 50 % : notamment 04.06, chap. 07-08, 17.04, 18.06, 20.01 à 20.09, 22.02 à 22.08, chap. 57, 61-62, 64.01 à 64.05 ; le texte ne donne que les numéros, les libellés de produits seraient ceux du SH) ; § 2 : position 080390 de 0 à 50 %, position 851712001 de 0 à 20 % |

Ce que le tableau ne permet pas d'écrire : l'**état complet** du tarif à une date. Chaque article
ne vise que les produits qu'il énumère ; il n'existe pas de texte lu qui donne la répartition des
positions par taux. L'expression « tarif à deux taux » pour 2016 n'est exacte que pour les
chapitres 25 à 97 et sous réserve des annexes 2 et 3 de la LF 2016.

Le libellé du tarif applicable change : « tarif minimum » (1959-1989), « tarif autonome »
(LF 1990-2011, par ex. LF 2005, art. 28), « التعريفة الحرة », rendu « tarif libre » dans
l'édition française de la LF 2017, art. 55, puis « tarif autonome » de nouveau dans les LF 2018 et
2022.

### 2.9 Les autres prélèvements perçus en douane

- **Redevance de prestations douanières** (série au § 5.2). LF 1988, art. 51 : 1,5 % de la valeur
  en douane, minimum 1 D par article (p. 1632) ; LF 1994, art. 75 : 2 % des droits et taxes
  liquidés, minimum 5 D (p. 2202) ; LF 1998, art. 43 : 3 %, minimum 5 D (p. 2439, texte) ;
  LF 1999, art. 32 : article 51 réécrit, 1,5 % de la valeur en douane à l'exportation du pétrole
  brut (27-09), minimum 1 D, et 3 % des droits et taxes liquidés à l'importation, minimum 5 D ;
  art. 33 : abrogation des taxes à l'exportation de l'huile d'olive (décrets des 26 novembre 1953 et
  22 novembre 1956) (p. 2503, texte) ; LF 2013, art. 57 : minimum 5 → 10 D (p. 17, texte) ;
  LF 2014, art. 16 : 100 D par déclaration de transit terrestre, suppression de l'affectation de
  10 % (p. 3669, texte) ; LF 2024, art. 66 : « dix dinars » → « vingt dinars » (p. 6454 ar.
  environ, texte arabe). Décrets de suspension à l'exportation : n° 98-1870 et n° 98-1983 (index).
- **Taxe de contrôle par scanner** des unités de charge en admission temporaire : 100 D (conteneur
  de 20 pieds au plus), 200 D au-delà (LF 2018, art. 42, p. 4280, texte).
- **Taxe à l'exportation des ferrailles et déchets de métaux non ferreux** : extension et hausse
  (LF 2022, art. 58, p. 3100 ; intitulé seul lu).
- Le code de 2008 charge la douane de percevoir « les taxes intérieures exigibles à l'importation
  et à l'exportation » (art. 297, p. 1788) : TVA, droit de consommation, FODEC (renvois, § 0).

## 2 bis. Points du brief : trouvé, non trouvé

| Point du brief | Constat | Source ou requêtes |
|---|---|---|
| Droit d'entrée, taxe de statistique, droit fiscal d'entrée | non identifiés sous ces noms | FTS « taxe de statistique » OR « droit fiscal » OR « droit d entree » : aucune notice douanière (la requête combinée rend seulement les redevances compensatrices) |
| Droit de compensation / prélèvements compensatoires agricoles | **redevances compensatrices** (sucres 1958-1959, thé 1958, chap. 73 en 1967 ; abrogations LF 1982) ; **droit compensateur provisoire** (1991-1997) ; **prélèvements à l'importation** sur la viande bovine (décret n° 90-1193 du 12 juillet 1990), la poudre de lait (décret n° 91-1391), la viande ovine (décret n° 93-1924), le beurre et l'huile acide (décret n° 93-2115), suspendus ou réduits ensuite par décret ; prélèvement sur les fruits au profit de la Caisse générale de compensation (décret n° 95-1212 ; LF 2018, art. 39, § 5) | § 1.1, 2.4, 2.5 ; décrets : index seulement (FTS « prelevement AND importation » : 29 notices hors arrêtés) |
| Contribution de solidarité à l'importation | non identifiée. La « contribution exceptionnelle de solidarité » que l'index range sous la rubrique douanière de la LF 1984 (art. 57) est celle de la loi n° 73-72, sur les impôts directs, reconduite pour 1984 (p. 3380, image) : domicile `_contributions_conjoncturelles.qmd` (`#sec-ccj-antecedents`) | FTS « contribution AND solidarite AND importation » : 0 |
| « Prélèvement conjoncturel 2018 de 30 % » | aucun prélèvement de ce nom en 2018. Dans la LF 2018, « prélèvement » ne vise que le prélèvement sur les fruits (art. 39, § 5) ; le 30 % est le relèvement de certains droits de 20 à 30 % (art. 39, § 2). Le seul prélèvement conjoncturel à l'importation est celui de la LFC 1991 (5 %), incorporé aux droits en 1994 | lecture de la LF 2018 (grep « prélèvement », « contribution ») ; § 2.4 |
| « Taxe de 3 % / 1 % sur les importations » | non identifiée. Le 3 % repéré est la redevance de prestations douanières (3 % des droits et taxes liquidés depuis 1998) ; le 1 % est le FODEC (renvoi). Autre prélèvement repéré : majoration d'un demi-décime sur les droits de douane à l'importation et la taxe de formalités douanières, affectée à la Caisse générale de compensation en 1984 (LF 1984, art. 49, p. 3379, image) | LIKE sur les titres contenant « importation » et « 3 » ou « 1 » avec taxe, prélèvement ou contribution : 321 notices hors arrêtés, surtout des décrets de suspension ; non dépouillées une à une |
| Régime des Tunisiens résidents à l'étranger | LF 1975, art. 33 (non lu), récrit par la LF 1993, art. 115 (lu) ; avantages fiscaux aux véhicules : renvoi `_depenses_fiscales.qmd` et `_droits_consommation.qmd` | § 2.4 |
| Voyageurs, franchises | régime des voyageurs non lu ; seuls le code, art. 272 (franchises : envois sans caractère commercial, œuvres de bienfaisance) et le décret n° 2009-1327 (marchandises en retour, index) sont repérés | — |
| Taxe à la production à l'importation (avant la TVA de 1988) | perçue à l'importation avec les droits de douane jusqu'en 1988 (décrets de suspension « droits de douane et taxe à la production », 1970-1973) ; domicile : chapitre TVA | index |
| Mesures de sauvegarde | loi n° 98-106, loi n° 99-9, code, art. 6, § 2 | § 2.4, index |

## 3. Textes de mise en œuvre

### 3.1 Le code des douanes de 2008

**Loi n° 2008-34 du 2 juin 2008** portant promulgation du code des douanes, JORT n° 47 du 10 juin
2008, pp. 1747-1804 (la loi p. 1748 ; le code ensuite), texte. Travaux préparatoires : Chambre des
députés, 13 mai 2008 ; Chambre des conseillers, 22 mai 2008 (note 1). Art. 2 : entrée en vigueur
le 1er janvier 2009. Art. 3 : abrogation du décret du 29 décembre 1955.

Articles utiles au chapitre (pages de l'édition française ; les pages des articles longs sont
déduites des pieds de page et de l'index) :

| Objet | Article | Page | Contenu |
|---|---|---|---|
| Territoire, zones franches | 1 | 1748 | territoire douanier ; zones franches « soustraites en tout ou partie du régime des douanes » |
| Tarif | 4 | 1748 | soumission à la loi tarifaire sauf dérogations des traités |
| Marchandises fortement taxées | 5 | 1748 | droits et taxes > 50 % de la valeur en douane, ou entre 20 et 50 % sur désignation par décret |
| Délégation au pouvoir réglementaire | 6 | 1748-1749 | § 1 : suspension (minimum légal compris), réduction, rétablissement par décret, valables « pendant l'année où elles sont prises » ; § 2 : hausse par décret selon la législation de sauvegarde ; § 3 : hausse ou rétablissement par décret pour protéger l'industrie locale dans le cadre des conventions |
| Mesures de rétorsion | 7 | 1749 | mesures tarifaires particulières par décret contre les États qui traitent moins favorablement les produits tunisiens |
| Clause transitoire | 12 | 1749 | régime antérieur plus favorable pour les marchandises expédiées avant l'entrée en vigueur d'une mesure |
| Notes communes | 13 | 1749 | publiées par la direction générale des douanes |
| Restitution | 15-18 | 1749-1750 | droits indûment perçus ; pas de restitution s'ils ont été répercutés (art. 16) |
| Espèce, classement | 19-20 | 1750 | nomenclature du système harmonisé (loi n° 89-113) ; décisions de classement au JORT |
| Origine | 21 | 1750-1751 | droits perçus selon l'origine ; « entièrement obtenues » ; transformation substantielle par décret |
| Valeur en douane | 22-35 | 1751-1755 | valeur transactionnelle (art. 23) et méthodes subsidiaires (code de l'évaluation de l'OMC, à confirmer par comparaison) ; art. 35 : confidentialité |
| Liquidation | 125 | 1767 | « les droits et taxes à percevoir sont ceux qui sont en vigueur à la date d'enregistrement de la déclaration en détail » |
| Régimes suspensifs et économiques | titre VI, 134 et suiv. | 1769-1784 | transit, entrepôts, transformation sous douane, perfectionnement actif, admission temporaire, perfectionnement passif, exportation temporaire |
| Zones d'activités logistiques | 87-92 | 1761-1763 | titre IV |
| Franchises | 272 | 1785 | envois sans caractère commercial, œuvres de bienfaisance ; conditions par décret |
| Marchandises en retour | 273 | 1785-1786 | décret d'application n° 2009-1327 (index) |
| Taxes intérieures | 297 | 1788 | perception par la douane |
| Remboursement à l'exportation | 298 | 1788 | droits et taxes d'effet équivalent remboursables ; tarif de remboursement fixé par le directeur général, forfaitaire possible |

Contexte en ses propres mots : l'avis du Conseil constitutionnel n° 2-2007 (pp. 1804-1805, texte)
juge que la suspension des droits pour une période déterminée « ne peut être considérée comme
une suppression de ces taxes » et que « les taxes douanières revêtent un caractère fiscal » ; il
déclare les articles 52 et 53 du projet (installation des bureaux dans des locaux privés)
incompatibles avec la Constitution. Avis n° 33-2007 et n° 32-2008 (pp. 1810-1813) : non lus.

Modificatifs du code (titres seuls, sauf mention) : loi n° 2001-92 du 7 août 2001 (code de 1955,
JORT n° 63, pp. 2020-2024) ; LF 2015, art. 41 (renseignements préalables, art. 13 bis et suiv.,
texte, p. 3471 d'après l'index) ; LF 2017, art. 56 à 60 (arts 80, 318, 340, 354 bis, 381 ; rattachement article par article à
vérifier) ; LF 2018, art. 31 (art. 403), 35 (art. 388) et 36 à 38 (arts 360, 362 bis) ; LF 2020, art. 51 (art. 130, § 3 : 6 % →
0,75 % par mois, texte arabe, p. 4709 ar. environ) ; décret n° 2024-463 du 21 août 2024 (art. 128,
JORT n° 103, p. 2288). Liste non exhaustive : pas de version consolidée lue (§ 8).

Code de 1955 : modifié par les décrets du 4 juin 1957, les lois n° 58-54 (art. 130), n° 58-85,
n° 61-48 du 24 novembre 1961 (JORT n° 52, p. 1528), n° 67-43, n° 72-19, les LF 1982 (arts 29 à 39 : admission temporaire, dédouanement,
remboursement à l'exportation), 1983 (art. 89 à 96), 1986 rectificative (art. 12 : art. 193,
remboursement à l'exportation) et la loi n° 2001-92 (index).

### 3.2 Administration

Direction générale des douanes : organisation fixée par le décret n° 94-1845 du 6 septembre 1994
(JORT n° 74, pp. 1547-1554), modifié en 2004 (décrets n° 2004-2128 et 2004-2703), 2013
(n° 2013-2800), 2014 (n° 2014-772) et 2024 (n° 2024-315) (index). Une phrase suffit au chapitre.

### 3.3 Décrets de suspension et de réduction

Le droit de suspendre, réduire ou rétablir les droits par décret est donné chaque année par la loi
de finances depuis la LF 1982 (art. 41 : « modification ou suspension de droits de douane au cours
d'exercice budgétaire », index), puis par le code de 2008, art. 6, § 1. L'index compte des
centaines de décrets de ce type (céréales 1960, engrais 1961, pommes de terre 1984, café et sucre
1985, beurre 1990…). Un relevé exhaustif n'est pas fait ; la note n'en cite aucun comme règle.

## 4. État du droit au 1er janvier 2026

Ce qui est établi par les textes lus :

- **Texte du tarif** : loi n° 89-113 du 30 décembre 1989, modifiée ; tarif à l'importation seule
  (art. 1, 2), en nomenclature du système harmonisé, numéro à neuf chiffres (LF 1999, art. 65)
  puis onze chiffres dans les lois récentes (ex. « 76061130102 », LF 2025, art. 58 ; à décrire
  sans interprétation).
- **Code** : loi n° 2008-34, en vigueur depuis le 1er janvier 2009 ; liquidation au tarif en
  vigueur à la date d'enregistrement de la déclaration (art. 125).
- **Taux** : pas d'état complet lu. Bandes repérables dans les textes : 0 et 20 % (chap. 25-97,
  LF 2016) ; 15 et 30 % pour les produits des annexes de la LF 2018 ; 43 et 50 % pour les produits
  de consommation de la LF 2022 ; jusqu'à 150 % pour des produits agricoles (LF 2005, art. 28 ;
  réductions de 2007-2009 ensuite, ponctuelles). Le taux maximal en vigueur au 1er janvier 2026
  n'est pas établi.
- **Préférences** : accord d'association UE (zone de libre-échange industrielle, démantèlement
  achevé en 2007 selon l'intitulé de la LF 1997, art. 21 ; le texte de l'accord fixe douze ans au
  plus) ; AELE, Turquie (mesures exceptionnelles jusqu'à fin 2026 au moins : LF 2024, art. 44),
  Agadir, accords bilatéraux arabes, UMA, COMESA, ZLECAf.
- **Prélèvements perçus en douane** : redevance de prestations douanières (3 % des droits et taxes
  liquidés, minimum 20 D par article ; 100 D par déclaration de transit terrestre ; 1,5 % à
  l'exportation du pétrole brut, si l'article 51 n'a pas été modifié sur ce point depuis 1999) ;
  taxe de contrôle par scanner ; TVA, droit de consommation, FODEC par renvoi.

Lois de finances 2020 à 2026, dispositions douanières lues (liste non exhaustive : seules les
lignes repérées par les termes « droits de douane » / « المعاليم الديوانية » ont été lues) :

| Loi | Article | Contenu | Page | Lecture |
|---|---|---|---|---|
| LF 2020 (loi n° 2019-78) | 51 | code, art. 130, § 3 : intérêt de retard 6 % → 0,75 % par mois | pp. 4709-4710 ar. | texte (arabe) |
| LF 2020 | 52 | Turquie : mesures exceptionnelles portées à quatre ans depuis le 1er janvier 2018 | pp. 4709-4710 ar. | texte (arabe) |
| LF 2021 (loi n° 2020-46) | (rubrique p. 675 de la couche texte) | « Extension de la suspension de la taxe sur la valeur ajoutée et des droits de douane sur certains produits » | — | intitulé seul |
| LF 2022 (DL n° 2021-21) | 31 | panneaux solaires : droits ramenés à 10 % | p. 3098 env. | texte (intitulé et première ligne) |
| LF 2022 | 57 | produits de consommation : 43 % ou 50 % | pp. 3099-3100 | texte |
| LF 2022 | 70 | abandon des redevances inscrites aux registres des receveurs des douanes | — | intitulé seul |
| LF 2023 (DL n° 2022-79) | 24 | chargeurs de véhicules électriques (85044055003, 853710) : 10 % jusqu'au 31 décembre 2023 | pp. 4075-4078 ar. | texte (arabe) |
| LF 2023 | 63 | friperie (6309, 6310) : tarif modifié, 0 % pour une ligne du tableau | pp. 4075-4078 ar. | texte (arabe), tableau lu en partie |
| LF 2024 (loi n° 2023-13) | 40 | panneaux solaires : droits relevés (taux non relevé ici) | p. 6444 ar. env. | intitulé seul |
| LF 2024 | 44 | Turquie : 75 % du droit commun, trois ans depuis le 1er janvier 2024 | p. 6444 ar. env. | texte (arabe) |
| LF 2024 | 66 | redevance de prestations douanières : minimum 10 → 20 D | p. 6454 ar. env. | texte (arabe) |
| LF 2025 (loi n° 2024-48) | 40 (tableau) | lait en poudre (040210, 040221) pour lait recombiné : droits à 36 %, TVA 19 %, contingent de 2 000 t | p. 6438 ar. env. | texte (arabe), rattachement à l'article à confirmer |
| LF 2025 | 58 | panneaux composites en aluminium : 30 % | p. 6445 ar. | texte (arabe) |
| LF 2026 (loi n° 2025-17) | 47, § 3-4 | véhicules hybrides rechargeables (87.02, 87.04) : 0 % ; chargeurs : 10 % jusqu'au 31 décembre 2028 | pp. 4240-4241 ar. | texte (arabe) |
| LF 2026 | 72 | lunettes médicales et montures (9003, 9004) : 10 % | p. 4249 ar. | texte (arabe) |

Lignes d'exonérations par bénéficiaire repérées dans les LF 2025 et 2026 (Office de la famille,
Société des viandes, Pharmacie centrale, Office du commerce pour le thé, ONAS, Compagnie des
phosphates de Gafsa, intrants de l'huile d'olive conditionnée) : relèvent des dépenses fiscales et
des régimes particuliers ; non détaillées.

## 5. Séries par date

### 5.1 Minimum de perception (tarif minimum ad valorem)

| Effet | Taux | Biens d'équipement | Texte |
|---|---|---|---|
| 2 janv. 1987 | 10 % | 15 % au plus (sans similaire local, art. 26) | LF 1987, art. 26-27, p. 1612 |
| 2 janv. 1988 | 15 % | 22 % | LF 1988, art. 53-54, p. 1633 |
| après 1988 | non établi | non établi | — |

### 5.2 Redevance de prestations douanières

| Effet | Assiette et taux | Minimum | Texte |
|---|---|---|---|
| 2 janv. 1988 | 1,5 % de la valeur en douane, toutes déclarations en détail ; exportations d'une liste | 1 D par article | LF 1988, art. 51, p. 1632 |
| 1er janv. 1994 | 2 % des droits et taxes liquidés, déclarations d'importation ; 10 % du produit affecté | 5 D par article | LF 1994, art. 75, p. 2202 |
| 1er janv. 1998 | 3 % des droits et taxes liquidés | 5 D | LF 1998, art. 43, p. 2439 |
| 1er janv. 1999 | import : 3 % ; export : seulement pétrole brut, 1,5 % de la valeur (min. 1 D) | 5 D | LF 1999, art. 32, p. 2503 |
| 1er janv. 2013 | inchangé | 10 D | LF 2013, art. 57, p. 17 |
| 1er janv. 2014 | + 100 D par déclaration de transit terrestre ; affectation de 10 % supprimée | 10 D | LF 2014, art. 16, p. 3669 |
| 1er janv. 2024 | inchangé | 20 D | LF 2024, art. 66, p. 6454 ar. env. |

### 5.3 Correspondances de bandes (1987, 1988, 1994)

Voir § 2.1, 2.2 et 2.4. Les trois tables sont des correspondances « ancien taux → nouveau taux »
applicables à tout le tableau A (1987, 1988) ou au tarif (1994, hors taux consolidés au GATT) ;
elles se prêtent à une figure en escalier (ancien taux en abscisse). Taux maximaux qu'elles
donnent : 45 % (1987), 43 % (1988), 43 % (1994).

## 6. Dates d'effet : règles appliquées

- Clause propre reprise telle quelle : loi n° 59-95 (1er octobre 1959) ; convention de 1959
  (1er octobre 1959) ; loi n° 73-45 (« à compter de sa promulgation », 23 juillet 1973, alors que
  le fascicule est daté des 20-24-27 juillet) ; loi n° 89-113 (1er janvier 1990) ; LF 1994
  (art. 77) ; LF 1997 (art. 21 et clause générale) ; loi n° 2008-34 (1er janvier 2009) ; LF 2018,
  art. 40 (1er janvier 2018) ; LF 2024, art. 44 (1er janvier 2024).
- Lois de finances depuis 1994 : clause générale « date d'application de la loi de finances »
  (1er janvier) vue dans les LF 1994, 1997, 1998, 1999, 2004 à 2011, 2015, 2016, 2017, 2019, 2020,
  2021, 2024, 2025 ; pour 2018, 2022, 2023, 2026, d'après la note sur le timbre.
- Avant 1993 sans clause : un jour franc après la publication — LF 1987, 1988, 1991 et 1993 n'ont
  pas de clause générale (derniers articles lus à l'image) : 2 janvier de l'année.
- Le code (art. 125) applique les droits en vigueur à la date d'enregistrement de la déclaration ;
  la date d'effet d'un taux est donc celle du texte, et la marchandise suit la date de sa
  déclaration, sous réserve de la clause transitoire (art. 12).
- Lois de ratification : la date d'effet de la loi ne dit rien de l'entrée en vigueur de l'accord ;
  le CSV laisse la colonne vide pour elles.

## 7. Références candidates (CSL-JSON)

Déjà présentes (à citer telles quelles) : `lf-1984` (global), `lf-1987`, `lf-1988` (livre compensation),
`lf-1991`, `lf-1993`, `lf-1994`, `lf-1997`, `lf-1998` (fiscalité), `lf-1999`, `lf-2004`,
`lf-2005`, `lf-2006`, `lf-2007`, `lf-2008` (fiscalité), `lf-2009`, `lf-2011`, `lf-2013`,
`lf-2014`, `lf-2015`, `lf-2016`, `lf-2017`, `lf-2018`, `lf-2019`, `lf-2020`, `lf-2021`,
`lf-2022`, `lf-2023`, `lf-2024`, `lf-2025`, `lf-2026`, `lfc-1991` (global sauf mention),
`loi-89-115-lf-1990`, `loi-93-120-code-incitations`, `loi-88-62-droit-consommation`.
Écarts constatés : `lf-2016`, `lf-2019`, `lf-2020`, `lf-2023`, `lf-2024`, `lf-2025`, `lf-2026`
sans URL ou avec une page qui n'est pas celle des articles douaniers ; éditions françaises
absentes pour 2015 n° 104, 2018 n° 104, 2019 n° 104, 2022 n° 141, 2023 n° 144, 2024 n° 149 (URL
arabe à donner, vérifiée le 23 octobre : `2015/2015A/Ja1042015`, `2018/2018A/Ja1042018`,
`2019/2019A/Ja1042019`, `2022/2022A/Ja1412022`, `2023/2023A/Ja1442023`, `2024/2024A/Ja1492024`).
`lf-1987` et `lf-1988` vivent dans le livre de la compensation : à copier dans le livre fiscalité.

À créer (type `legislation`, `container-title` « Journal officiel de la République tunisienne »,
URL pist.tn vérifiée) :

```json
[
 {"id":"loi-59-95-tarif-douanes","type":"legislation","title":"Loi n° 59-95 du 20 août 1959 (15 safar 1379), portant mise en vigueur d'un nouveau tarif des douanes à l'importation et à l'exportation","container-title":"Journal officiel de la République tunisienne","issue":"43","issued":{"date-parts":[[1959,8,18]]},"page":"886","URL":"https://www.pist.tn/jort/1959/1959F/Jo04359.pdf"},
 {"id":"loi-59-110-convention-france","type":"legislation","title":"Loi n° 59-110 du 28 septembre 1959, portant ratification de la Convention commerciale et tarifaire entre le Gouvernement de la République tunisienne et le Gouvernement de la République française ; décret n° 59-283 du même jour portant publication de la Convention","container-title":"Journal officiel de la République tunisienne","issue":"49","issued":{"date-parts":[[1959,9,29]]},"page":"1036, 1043-1061","URL":"https://www.pist.tn/jort/1959/1959F/Jo04959.pdf"},
 {"id":"loi-73-45-tarif-douanes","type":"legislation","title":"Loi n° 73-45 du 23 juillet 1973, portant mise en vigueur d'un nouveau tarif des douanes à l'importation et à l'exportation","container-title":"Journal officiel de la République tunisienne","issue":"28","issued":{"date-parts":[[1973,7,20]]},"page":"1134","URL":"https://www.pist.tn/jort/1973/1973F/Jo02873.pdf"},
 {"id":"loi-87-2-systeme-harmonise","type":"legislation","title":"Loi n° 87-2 du 6 février 1987, portant ratification de la convention internationale sur le système harmonisé de désignation et de codification des marchandises","container-title":"Journal officiel de la République tunisienne","issue":"10","issued":{"date-parts":[[1987,2,6]]},"page":"191","URL":"https://www.pist.tn/jort/1987/1987F/Jo01087.pdf"},
 {"id":"loi-89-113-tarif-douanes","type":"legislation","title":"Loi n° 89-113 du 30 décembre 1989, relative à l'application d'un nouveau tarif des droits de douanes à l'importation","container-title":"Journal officiel de la République tunisienne","issue":"88","issued":{"date-parts":[[1989,12,29]]},"page":"2142","URL":"https://www.pist.tn/jort/1989/1989F/Jo08889.pdf"},
 {"id":"loi-90-61-gatt","type":"legislation","title":"Loi n° 90-61 du 28 juin 1990, portant ratification du protocole d'adhésion de la République tunisienne à l'accord général sur les tarifs douaniers et le commerce (G.A.T.T.)","container-title":"Journal officiel de la République tunisienne","issue":"44","issued":{"date-parts":[[1990,6,26]]},"page":"839","URL":"https://www.pist.tn/jort/1990/1990F/Jo04490.pdf"},
 {"id":"loi-91-46-uma-convention-commerciale","type":"legislation","title":"Loi n° 91-46 du 22 juillet 1991, portant ratification de la convention commerciale et tarifaire conclue entre les États de l'Union du Maghreb arabe","container-title":"Journal officiel de la République tunisienne","issue":"53","issued":{"date-parts":[[1991,7,26]]},"page":"1344","URL":"https://www.pist.tn/jort/1991/1991F/Jo05391.pdf"},
 {"id":"loi-95-6-uruguay-round","type":"legislation","title":"Loi n° 95-6 du 23 janvier 1995, portant ratification des accords de l'Uruguay round","container-title":"Journal officiel de la République tunisienne","issue":"9","issued":{"date-parts":[[1995,1,31]]},"page":"271","URL":"https://www.pist.tn/jort/1995/1995F/Jo00995.pdf"},
 {"id":"loi-96-49-accord-association-ue","type":"legislation","title":"Loi n° 96-49 du 20 juin 1996, portant ratification de l'accord euro-méditerranéen établissant une association entre la République tunisienne d'une part et les Communautés européennes et leurs États membres, d'autre part","container-title":"Journal officiel de la République tunisienne","issue":"51","issued":{"date-parts":[[1996,6,25]]},"page":"1311","URL":"https://www.pist.tn/jort/1996/1996F/Jo05196.pdf"},
 {"id":"decret-98-1273-publication-accord-ue","type":"legislation","title":"Décret n° 98-1273 du 18 mai 1998, portant publication de l'accord euro-méditerranéen établissant une association entre la République tunisienne d'une part et les communautés européennes et leurs États membres, d'autre part","container-title":"Journal officiel de la République tunisienne","issue":"49","issued":{"date-parts":[[1998,6,19]]},"page":"1326","URL":"https://www.pist.tn/jort/1998/1998F/Jo04998.pdf"},
 {"id":"accord-association-ue-tunisie-1995","type":"legislation","title":"Accord euro-méditerranéen établissant une association entre la Communauté européenne et ses États membres, d'une part, et la République tunisienne, d'autre part","container-title":"Journal officiel des Communautés européennes","volume":"L 97","issued":{"date-parts":[[1998,3,30]]},"page":"2-183","URL":"https://www.eeas.europa.eu/sites/default/files/398845_accord_assoc_int_0.pdf","note":"Signé à Bruxelles le 17 juillet 1995. Copie du SEAE ; JOCE L 97, p. 2 et suiv."},
 {"id":"loi-98-80-ale-jordanie","type":"legislation","title":"Loi n° 98-80 du 2 novembre 1998, portant ratification de la convention relative à la zone de libre échange conclue le 22 avril 1998 entre le gouvernement de la République tunisienne et le gouvernement du Royaume hachémite de Jordanie","container-title":"Journal officiel de la République tunisienne","issue":"89","issued":{"date-parts":[[1998,11,6]]},"page":"2181","URL":"https://www.pist.tn/jort/1998/1998F/Jo08998.pdf"},
 {"id":"loi-99-17-ale-egypte","type":"legislation","title":"Loi n° 99-17 du 1er mars 1999, portant ratification de la convention de libre échange et du protocole des règles d'origine conclus entre le gouvernement de la République tunisienne et le gouvernement de la République arabe d'Égypte","container-title":"Journal officiel de la République tunisienne","issue":"19","issued":{"date-parts":[[1999,3,5]]},"page":"347","URL":"https://www.pist.tn/jort/1999/1999F/Jo01999.pdf"},
 {"id":"loi-99-34-ale-maroc","type":"legislation","title":"Loi n° 99-34 du 30 avril 1999, portant ratification de la convention de libre échange et du protocole des règles d'origine et de coopération douanière, conclus entre la République tunisienne et le Royaume du Maroc","container-title":"Journal officiel de la République tunisienne","issue":"37","issued":{"date-parts":[[1999,5,7]]},"page":"683","URL":"https://www.pist.tn/jort/1999/1999F/Jo03799.pdf"},
 {"id":"loi-2001-114-ale-libye","type":"legislation","title":"Loi n° 2001-114 du 26 novembre 2001, portant ratification de la convention de zone de libre échange, conclue entre la République tunisienne et la Jamahiriya arabe libyenne","container-title":"Journal officiel de la République tunisienne","issue":"95","issued":{"date-parts":[[2001,11,27]]},"page":"3995","URL":"https://www.pist.tn/jort/2001/2001F/Jo0952001.pdf"},
 {"id":"loi-2001-115-ale-irak","type":"legislation","title":"Loi n° 2001-115 du 26 novembre 2001, portant ratification d'un protocole exécutif pour l'établissement d'une zone de libre échange, conclu entre le gouvernement de la République tunisienne et le gouvernement de la République d'Iraq","container-title":"Journal officiel de la République tunisienne","issue":"95","issued":{"date-parts":[[2001,11,27]]},"page":"3995","URL":"https://www.pist.tn/jort/2001/2001F/Jo0952001.pdf"},
 {"id":"loi-2004-58-accord-agadir","type":"legislation","title":"Loi n° 2004-58 du 27 juillet 2004, portant approbation de la convention d'établissement d'une zone de libre échange entre les États arabes méditerranéens","container-title":"Journal officiel de la République tunisienne","issue":"60","issued":{"date-parts":[[2004,7,27]]},"page":"1940","URL":"https://www.pist.tn/jort/2004/2004F/Jo0602004.pdf"},
 {"id":"loi-2004-82-ale-syrie","type":"legislation","title":"Loi n° 2004-82 du 6 décembre 2004, portant approbation d'une convention établissant une zone de libre échange entre la République tunisienne et la République arabe syrienne","container-title":"Journal officiel de la République tunisienne","issue":"98","issued":{"date-parts":[[2004,12,7]]},"page":"3336","URL":"https://www.pist.tn/jort/2004/2004F/Jo0982004.pdf"},
 {"id":"loi-2005-34-ale-aele","type":"legislation","title":"Loi n° 2005-34 du 11 mai 2005, portant approbation d'un accord de libre échange conclu, le 17 décembre 2004, entre la République tunisienne et les États de la communauté européenne de libre échange et les accords et protocoles joints","container-title":"Journal officiel de la République tunisienne","issue":"38","issued":{"date-parts":[[2005,5,13]]},"page":"1061","URL":"https://www.pist.tn/jort/2005/2005F/Jo0382005.pdf"},
 {"id":"loi-2005-36-ale-turquie","type":"legislation","title":"Loi n° 2005-36 du 11 mai 2005, portant approbation d'une convention d'association portant sur l'établissement d'une zone de libre échange conclue, le 25 novembre 2004, entre la République tunisienne et la République de Turquie","container-title":"Journal officiel de la République tunisienne","issue":"38","issued":{"date-parts":[[2005,5,13]]},"page":"1061","URL":"https://www.pist.tn/jort/2005/2005F/Jo0382005.pdf"},
 {"id":"loi-2006-72-tarif-douanes","type":"legislation","title":"Loi n° 2006-72 du 28 octobre 2006, modifiant la loi relative au tarif des droits de douane à l'importation","container-title":"Journal officiel de la République tunisienne","issue":"88","issued":{"date-parts":[[2006,11,3]]},"page":"3870","URL":"https://www.pist.tn/jort/2006/2006F/Jo0882006.pdf"},
 {"id":"loi-2008-34-code-douanes","type":"legislation","title":"Loi n° 2008-34 du 2 juin 2008, portant promulgation du code des douanes","container-title":"Journal officiel de la République tunisienne","issue":"47","issued":{"date-parts":[[2008,6,10]]},"page":"1747-1804","URL":"https://www.pist.tn/jort/2008/2008F/Jo0472008.pdf"},
 {"id":"cc-avis-2007-2-code-douanes","type":"legislation","title":"Avis n° 2-2007 du Conseil constitutionnel, sur un projet de loi portant promulgation du code des douanes","container-title":"Journal officiel de la République tunisienne","issue":"47","issued":{"date-parts":[[2008,6,10]]},"page":"1804-1810","URL":"https://www.pist.tn/jort/2008/2008F/Jo0472008.pdf"},
 {"id":"loi-org-2019-33-comesa","type":"legislation","title":"Loi organique n° 2019-33 du 10 avril 2019, portant approbation de l'accord relatif à l'adhésion de la République tunisienne au marché commun de l'Afrique orientale et australe (COMESA)","container-title":"Journal officiel de la République tunisienne","issue":"30","issued":{"date-parts":[[2019,4,12]]},"page":"980","URL":"https://www.pist.tn/jort/2019/2019F/Jo0302019.pdf"},
 {"id":"loi-org-2020-34-zlecaf","type":"legislation","title":"Loi organique n° 2020-34 du 7 août 2020, portant approbation de l'accord portant création de la zone de libre-échange continentale africaine","container-title":"Journal officiel de la République tunisienne","issue":"80","issued":{"date-parts":[[2020,8,14]]},"page":"1727","URL":"https://www.pist.tn/jort/2020/2020F/Jo0802020.pdf"},
 {"id":"loi-org-2025-20-amendement-aele","type":"legislation","title":"Loi organique n° 2025-20 du 31 décembre 2025, portant approbation de l'amendement au protocole (B) de l'accord de libre-échange entre la République tunisienne et les États de la Communauté européenne de libre-échange","container-title":"Journal officiel de la République tunisienne","issue":"156","issued":{"date-parts":[[2025,12,31]]},"page":"3680","URL":"https://www.pist.tn/jort/2025/2025F/Jo1562025.pdf"},
 {"id":"loi-org-2025-21-amendement-accord-ue","type":"legislation","title":"Loi organique n° 2025-21 du 31 décembre 2025, portant approbation de l'amendement à l'accord euro-méditerranéen établissant une association entre la République tunisienne, d'une part, et la Communauté européenne et ses États membres, d'autre part","container-title":"Journal officiel de la République tunisienne","issue":"156","issued":{"date-parts":[[2025,12,31]]},"page":"3680-3681","URL":"https://www.pist.tn/jort/2025/2025F/Jo1562025.pdf"}
]
```

Les dates `issued` sont celles du pied de page du fascicule (premier jour quand il en couvre
plusieurs), non celles de `jort_cache` quand elles divergent (59-95, 73-45, 90-61).

## 8. Contexte des réformes : trouvé, manquant

Trouvé, dans les mots des textes : « Protection [puis Soutien] de la compétitivité de la
production nationale dans le cadre de la réforme économique » (rubriques des LF 1993 et 1994) ;
« Mesures tarifaires pour la maîtrise du déficit de la balance commerciale » (LF 2018, art. 39) ;
« Révision des droits de douane appliqués aux produits de consommation ou ayant un similaire
fabriqué localement » (LF 2022, art. 57) ; « Démantèlement progressif des droits de douane pour
la période 1996-2007 » (LF 1997, art. 21) ; l'avis du Conseil constitutionnel de 2007.

Manquant : tout document de l'époque sur l'ajustement de 1986-1988 (lettres de politique,
rapports de la Banque mondiale sur les prêts d'ajustement industriel et commercial, VIIe plan),
sur le tarif de 1989 (exposé des motifs, débats de la Chambre du 28 décembre 1989), sur l'adhésion
au GATT et la négociation de l'accord de 1995 (rapports du IXe plan, examens des politiques
commerciales de l'OMC de 1994, 2005 et 2016). Ces rapports relèvent de la note « chiffres » ou
d'une recherche ultérieure ; aucun n'est cité ici. Les examens des politiques commerciales de
l'OMC donneraient aussi la structure complète du tarif à leur date (familles « rapport
extérieur »).

## 9. Notions à glossaire

| id proposé | FR | AR (d'après les textes lus) | Source canonique pressentie |
|---|---|---|---|
| `droits-de-douane` | Droits de douane | المعاليم الديوانية | `loi-89-113-tarif-douanes`, art. 1 ; LF 2016, art. 41 (ar.) |
| `tarif-des-droits-de-douane` | Tarif des droits de douane à l'importation | تعريفة المعاليم الديوانية عند التوريد | `loi-89-113-tarif-douanes` ; LF 2016, art. 41 (ar.) |
| `tarif-autonome` | Tarif autonome (tarif libre) | التعريفة الحرة | LF 2016, art. 41 (ar.) ; LF 2011, art. 10 (fr.) ; LF 2017, art. 55 (« tarif libre ») |
| `tarif-minimum-tarif-general` | Tarif minimum, tarif général | — (à attester) | `loi-59-95-tarif-douanes`, art. 1 |
| `droit-consolide` | Droit consolidé | المعاليم الديوانية المثبتة / الموطدة (à attester) | LF 1994, art. 71, § 2 ; LF 2005, art. 28 |
| `demantelement-tarifaire` | Démantèlement tarifaire | التفكيك الجمركي / الديواني (à attester) | LF 1997, art. 21 ; accord de 1995, art. 11 |
| `taxe-effet-equivalent` | Taxe d'effet équivalent | — | accord de 1995, art. 8 et 11 ; LF 1997, art. 18 |
| `redevance-prestations-douanieres` | Redevance de prestations douanières | الأتاوة على الخدمات الديوانية | LF 1988, art. 51 ; LF 2024, art. 66 (ar.) |
| `taxe-formalites-douanieres` | Taxe de formalités douanières | — | LF 1988, art. 48 |
| `droit-compensateur-provisoire` | Droit compensateur provisoire (puis droit complémentaire provisoire) | — | LF 1991, art. 26 ; LF 1994, art. 68 ; LF 1997, art. 20 |
| `minimum-legal-perception-douane` | Minimum légal de perception | — | LF 1987, art. 27 ; code, art. 6 |
| `regimes-douaniers-economiques` | Régimes suspensifs et régimes douaniers économiques | — | code de 2008, titre VI |
| `admission-temporaire` | Admission temporaire | — | code de 2008, titre VI, chap. 7 |
| `origine-des-marchandises` | Origine des marchandises | — | code de 2008, art. 21 |
| `systeme-harmonise` | Système harmonisé | — | `loi-87-2-systeme-harmonise` ; code, art. 19 |
| `marchandises-fortement-taxees` | Marchandises fortement taxées | — | code de 2008, art. 5 |

Entrées existantes : `valeur-en-douane` (source actuelle : loi n° 88-62, art. 4 ; proposer le
code de 2008, art. 22-23, comme source de la définition générale), `position-tarifaire`,
`zone-franche-economique`, `entreprise-totalement-exportatrice`, `depense-fiscale`,
`taux-ad-valorem`.

## 10. Pour backlog-modele (le précis n'en parle pas)

`openfisca-tunisia` (lecture de `openfisca_tunisia/parameters/` le 23 octobre 2026) ne porte
aucun paramètre de droits de douane : `fiscalite_indirecte/` contient `accises`,
`droits_enregistrement` et `tva`, sans nœud douane ; les seules occurrences de « douane » sont
des grilles de rémunération (`fonction_publique/agents_services_douaniers/`) et des mentions dans
les accises sur les boissons. Le chapitre n'aura donc pas de tableau engendré ; les séries
5.1 et 5.2 (minimum de perception, redevance de prestations douanières) et les tables de
correspondance de 1987, 1988 et 1994 sont candidates à un versement (série à fenêtre :
1996-2026 pour la redevance, états de 1988 et 1994 dans le registre écrit du chapitre).

## 11. Lacunes

**Lisible dans le corpus, non lu** :

- LF 1982, 1983, 1985 et 1986 : articles « aménagement du tarif » et taxe de formalités douanières
  (index, § 1.3), LF 1971, 1977, 1981 ; la LF 1984 est lue pp. 3378-3380 (art. 48-57) ;
- LF 1990 (loi n° 89-115), art. sur la suspension des droits (p. 2148-2149) ; LF 1992 (loi
  n° 91-98), art. 45-52 (p. 2086-2087, droit compensateur, prélèvement conjoncturel reconduit) ;
- LF 1995 (art. 93 et suivants, p. 2050-2051), LF 1996 (p. 2371, 2375), LF 2000 à 2003 (articles
  de réduction et d'ajustement) : texte, pour compléter la série des bandes de 1994 à 2004 ;
- LF 2010, art. 22 et LF 2011, art. 11 (tableaux « G ») ; LF 2012 (loi n° 2011-7), art. 16-17 ;
- LF 2015 à 2017 et LF 2019 à 2026 : lecture complète des sections douanières (seules les lignes
  repérées par « droits de douane » / « المعاليم الديوانية » sont lues) ; annexes 1 et 2 de la
  LF 2018 et annexes 2 et 3 de la LF 2016 (listes de positions) ;
- loi n° 2001-92 (modification du code de 1955) ; avis n° 33-2007 et 32-2008 du Conseil
  constitutionnel ; loi n° 98-106 (sauvegarde) ; loi n° 99-9 ;
- décret n° 69-293 (accord CEE de 1969) et accord de coopération de 1976 ;
- JORT n° 16 de 1957, p. 218 (rectificatif du décret du 29 décembre 1955 sur le protocole d'union
  douanière) : la page n'est pas dans le fichier `Jo01657.pdf` du corpus (pages 154 et suiv.) ;
  vérifier le numéro du fascicule.

**OCR à demander** : aucun indispensable ; les scans de 1959 à 1993 se lisent à l'image. Un OCR
des LF 1982-1986 (sections douanières) éviterait une lecture page à page si l'on veut la série
de la taxe de formalités douanières.

**À obtenir** :

- *Journal officiel tunisien* de 1955 (décrets du 29 décembre 1955 : code, tarif, convention
  d'union douanière) et textes douaniers du Protectorat ; *Bulletin économique et social de la
  Tunisie* pour le contexte (fiches `r-douane-legislation-1955`,
  `r-douane-union-douaniere-protectorat`) ;
- fascicules hors JORT des tableaux du tarif (1959 n° 59-5, 1973, 1989) et tarif consolidé en
  vigueur au 1er janvier 2026 (site de la douane) (fiche `r-douane-tableaux-tarifs`) ;
- fascicule annexé au JORT n° 49 de 1998 (texte tunisien de l'accord d'association) ; notice
  d'entrée en vigueur de l'accord au JOCE (EUR-Lex inaccessible par script le 23 octobre) ;
- textes des accords de libre-échange (dates d'entrée en vigueur, listes) : non publiés au JORT
  lu ;
- version consolidée du code des douanes (le WIPO Lex en porte une à jour de la LF 2019, d'après
  une recherche web ; non téléchargée) pour lister les modificatifs de 2009 à 2026.

**Non établi, à ne pas écrire** : taux maximal et répartition des positions par taux au
1er janvier 2026 ; minimum légal de perception après 1988 ; date et contenu des décrets annuels
de démantèlement UE ; caractérisation des annexes 3 à 6 de l'accord ; motifs de l'ajustement de
1987-1988 dans les mots de l'époque.

## 12. Recherches infructueuses (fiches proposées, non versées)

Requêtes réellement lancées le 23 octobre 2026 sur `jort_cache` (dernière publication indexée :
2 octobre 2026). Périodes antérieures à 2011 : pas de terme arabe requis. Les champs `ou` sont à
remplir par le rédacteur (sans quoi `verifier` échoue).

```yaml
- id: r-douane-legislation-1955
  objet: décrets du 29 décembre 1955 portant refonte et codification de la législation douanière (code des douanes abrogé par la loi n° 2008-34, art. 3) et portant mise en vigueur d'un nouveau tarif des douanes (abrogé par la loi n° 59-95, art. 4)
  ou: [precis/fr/fiscalite/<chapitre droits de douane>.qmd#<section antécédents>]
  requetes:
    titres_fts: ['"29 decembre 1955" AND douan*', '"refonte et codification"', '"tarif des douanes"']
    titres_like: [29 decembre 1955, refonte et codification de la legislation douaniere]
    depuis: 1955-12-29
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache, corpus_local, visas]
    couverture: 'FTS « 29 decembre 1955 » AND douan* : 23 notices, des arrêtés modifiant l''arrêté du 29 décembre 1955 d''application du code (1958-2001) et le rectificatif de 1957 (JORT n° 16, p. 218) sur le protocole d''union douanière ; LIKE « 29 decembre 1955 » avec « douan » : 23 ; FTS « refonte et codification » : 23 notices, dont une seule sur la douane (loi n° 61-48 du 24 novembre 1961 modifiant le décret de 1955, JORT n° 52, p. 1528), les autres sur la législation des changes (loi n° 76-18) ; LIKE « refonte et codification de la legislation douaniere » : 1 (la loi n° 61-48) ; FTS « tarif des douanes » : 11 notices, aucune de 1955. Les deux décrets sont connus par les visas de la loi n° 59-95 (p. 886) et par la loi n° 2008-34, art. 3 (p. 1748). Lacunes : jort_cache et le corpus local commencent en 1956 ; le Journal officiel tunisien de 1955 n''est pas parcouru.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - Journal officiel tunisien de décembre 1955 et janvier 1956 (Gallica ou archives nationales)
  - vérifier le fascicule du rectificatif de 1957 (JORT n° 16, p. 218), absent du fichier Jo01657.pdf

- id: r-douane-union-douaniere-protectorat
  objet: régime douanier du Protectorat avant le 1er octobre 1959 — union douanière franco-tunisienne (convention économique et financière et protocole de 1955), tarifs et conventions antérieurs
  ou: [precis/fr/fiscalite/<chapitre droits de douane>.qmd#<section antécédents>]
  requetes:
    titres_fts: ['"union douaniere"', 'convention AND commerciale AND (France OR francaise)']
    titres_like: [union douaniere]
    depuis: 1881-05-12
  periode:
    jusqu_au: 1959-09-30
    motif: régime abrogé par l'art. 1 de la convention commerciale et tarifaire du 5 septembre 1959, en vigueur le 1er octobre 1959 (loi n° 59-110)
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache, corpus_local, visas]
    couverture: 'FTS « union douaniere » : 1 notice (décret du 29 décembre 1955 relatif au protocole d''application, rectificatif au JORT n° 16 de 1957, p. 218, non lu) ; LIKE « union douaniere » : 1 (la même) ; FTS « convention AND commerciale AND (France OR francaise) » : 7 notices, dont avant 1965 la convention de 1959 (loi n° 59-110, décret n° 59-283, lus) et son protocole additionnel de 1960 (décret-loi n° 60-28, décret n° 60-340). Lacunes : rien avant 1956 dans jort_cache ni dans le corpus local ; Bulletin économique et social de la Tunisie non parcouru.'
    couvert_jusqu_au: 1959-09-30
    resultat: aucun
  a_faire:
  - Journal officiel tunisien 1955 (conventions franco-tunisiennes du 3 juin 1955 et décrets de ratification)
  - Bulletin économique et social de la Tunisie (régime douanier, tarifs)

- id: r-douane-tableaux-tarifs
  objet: tableaux des taux annexés aux lois n° 59-95 (tableaux A et B), n° 73-45 (tableaux A et B) et n° 89-113 (tarif des droits de douane à l'importation), publiés hors du Journal officiel
  ou: [precis/fr/fiscalite/<chapitre droits de douane>.qmd#<section tarifs>]
  requetes:
    titres_fts: ['"nouveau tarif"', '"tarif des douanes"']
    titres_like: [tarif des droits de douane a l%importation]
    depuis: 1959-08-18
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: 'FTS « nouveau tarif » : 13 notices, « tarif des douanes » : 11 ; LIKE « tarif des droits de douane a l%importation » : 58 notices (1990-2022, rubriques de lois de finances et décrets modificatifs) ; aucune ne publie les tableaux. Lu à l''image : JORT n° 43 de 1959, p. 885 (annonce de la vente du tarif en fascicule n° 59-5, 1 dinar) ; JORT n° 28 de 1973, pp. 1134-1136 ; JORT n° 88 de 1989, p. 2142 : tableaux non reproduits. Lacunes : publications de l''Imprimerie officielle hors JORT non parcourues ; tarif consolidé de la direction générale des douanes non consulté.'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire:
  - fascicule « Le Nouveau Tarif des Douanes » n° 59-5 (1959) et éditions de 1973 et 1989 (Imprimerie officielle, bibliothèques)
  - tarif en ligne de la direction générale des douanes (état au 1er janvier 2026)

- id: r-douane-decrets-demantelement-ue
  objet: décrets appliquant aux produits d'origine communautaire le calendrier de démantèlement de l'accord d'association (art. 11), 1996-2007
  ou: [precis/fr/fiscalite/<chapitre droits de douane>.qmd#<section accord d'association>]
  requetes:
    titres_fts: ['origine AND (communautaire OR "union europeenne" OR "communaute europeenne") AND douane', 'demantelement']
    titres_like: [demantelement]
    depuis: 1996-01-01
  periode:
    jusqu_au: 2008-12-31
    motif: calendrier de douze ans au plus (accord, art. 6), première année 1996 (LF 1997, art. 21)
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: 'Période 1996-2008 : FTS « demantelement » : 2 notices (LF 1997, art. 21 ; LF 1999, art. 35) ; LIKE « demantelement » : 2 ; FTS origine AND (communautaire OR « union europeenne » OR « communaute europeenne ») AND douane : 1 (LF 1999, art. 35). Lus au sommaire du JORT n° 105 de 1996 : décrets n° 96-2471 à 96-2477 du 30 décembre 1996 (lait, agriculture et pêche, produits agricoles, droit complémentaire provisoire, médicaments, cahiers scolaires, produits agro-alimentaires) : aucun ne vise l''origine communautaire. Lacunes : décrets de fin décembre 1997 à 2007 non lus ; plein texte non joué.'
    couvert_jusqu_au: 2008-12-31
    resultat: aucun
  a_faire:
  - lire les décrets de réduction des droits de douane publiés fin décembre de chaque année 1995-2007 (ex. décrets n° 96-2471 à 96-2477, JORT n° 105 de 1996)
  - jouer le plein texte sur « produits originaires » et « annexe 3 »/« annexe 4 »
```

La quatrième fiche n'est à verser que si le rédacteur pose une réserve sur ces décrets dans le
chapitre.

Sources web utilisées : [EEAS, Accord d'association](https://www.eeas.europa.eu/node/11560_en) ;
[texte de l'accord, JOCE L 97/2](https://www.eeas.europa.eu/sites/default/files/398845_accord_assoc_int_0.pdf).

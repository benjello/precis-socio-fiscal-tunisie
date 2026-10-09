# Finances locales, chapitres 6 à 8 — fiche de plan de l'architecte

> Architecte, 9 octobre 2026. Plan de conversion au format « ruptures au premier plan, détail
> replié » de trois chapitres de `precis/fr/finances_locales/` : `_impots_immeubles.qmd`
> (ch. 6), `_impots_activite.qmd` (ch. 7), `_taxes_redevances.qmd` (ch. 8). Rien n'est rédigé
> ici ; aucun fait n'est ajouté. Tout ce qui est classé vient de la note
> `docs/notes/finances-locales-impots-locaux.md` (4 octobre 2026) et des chapitres déjà écrits
> du volume, avec leur degré de certitude. Les mots « cœur », « épine », « fiche » sont des
> mots de travail : ils ne paraissent dans aucun titre proposé.

## 0. Ce qui vaut pour les trois chapitres

### 0.1 Le découpage en trois chapitres : il reste

Les trois chapitres gardent leur périmètre et leur ordre. Quatre points de frontière, tranchés
ainsi :

| Matière | Où elle est aujourd'hui | Décision |
|---|---|---|
| « Le code de la fiscalité locale » (promulgation, huit chapitres, `#sec-fl-code-1997`, `tbl-fl-code-chapitres`) | ch. 6, alors qu'elle sert aux trois | reste au ch. 6, dans sa mise en place ; les ch. 7 et 8 ouvrent la leur par une phrase et un renvoi en tête (`@sec-fl-code-1997`), sans redire |
| « Les autres impôts du code » (`#sec-fl-activite-autres`, ch. 7) | section de pur renvoi | devient une phrase de la vue d'ensemble du ch. 7 ; l'identifiant, cité nulle part, est gardé en ancre sur cette phrase |
| « Ce que les collectivités peuvent moduler » et `tbl-fl-qui-fixe`, qui portent aussi sur les quatre impôts | ch. 8 | restent au ch. 8 : c'est l'objet de son titre. Les ch. 6 et 7 y renvoient d'une phrase à la fin de leurs grandes réformes |
| Produit de la taxe sur les établissements au-delà de 100 000 D versé à un fonds (LF 2013, art. 14 ; LF 2021, art. 13) | ch. 7, avec « objet d'un chapitre à venir » | reste au ch. 7 pour ce qui touche la taxe (qui encaisse) ; les fonds eux-mêmes sont au chapitre des transferts, qui existe désormais (`@sec-fl-fccl-2018`) : le « chapitre à venir » devient un renvoi |

Aucune section ne change de chapitre. Seule matière qui arrive : les figures de rendement de
`_longue_periode.qmd` (§ 5).

**Ordre de travail du rédacteur** : ch. 6, puis ch. 7, puis ch. 8. Le ch. 6 porte la section
commune sur le code et sert de gabarit aux registres ; le ch. 7 est le plus riche en réformes ;
le ch. 8 dépend d'un ticket du documentaliste (§ 8) et vient en dernier. La scission de la
figure des impôts (§ 5.1) se fait avant le ch. 6, par un agent de niveau « standard ».

### 0.2 Les bornes proposées par le propriétaire, vérifiées une à une

| Borne proposée | Verdict | Motif |
|---|---|---|
| Code de la fiscalité locale, 1997 | **retenue** pour les trois chapitres : c'est la mise en place | loi n° 97-11, art. 2 à 5 de la loi ; code lu article par article, FR et AR |
| Révisions de barèmes (2008, 2017) | **refusée comme rupture** | ce sont des relèvements par paliers de grandeurs que le code renvoie à un décret « tous les trois ans » (art. 4 § IV, 33, 38 § II) : des étapes de la mise en place de 1997. Ni l'objectif ni le public ne changent |
| 2011 | **refusée** pour les ch. 6 et 8 : aucun texte lu. Au ch. 7, la LF 2011 (art. 32) n'ouvre pas une réforme de la taxe : elle crée, dans l'impôt sur le revenu, un forfait qui la « comprend » — rupture propre à un dispositif secondaire | la chute des produits en 2011 est un fait des séries, pas du droit : elle se dit dans la longue période, sans borne dans l'épine |
| Constitution de 2014 | **refusée** | aucun de ses articles n'est lu dans la note ; le volume ne la cite que d'après une traduction reproduite par Dafflon et Gilbert (`r-fl-constitution-2014-numero-special`). Elle n'apparaît ici que par le renvoi que fait l'art. 137 du code de 2018 à son art. 65 |
| Code des collectivités locales, 2018 | **retenue pour le ch. 8** (art. 137, 139 à 141, 391, lus en arabe) ; **signalée seulement** aux ch. 6 et 7, dont il ne change aucune règle | les quatre impôts « restent des impôts fixés par la loi » : pas de rupture pour eux |

Les ruptures que les textes portent réellement, et que le propriétaire n'avait pas nommées :
2002 et 2006-2009 au ch. 6 ; 2012-2013 et 2013-2014 au ch. 7 (§ 1.2, 2.2). « Trois à six » est
un plafond : les ch. 6 et 7 ont chacun une mise en place et deux grandes réformes, le ch. 8 une
mise en place et une seule.

### 0.3 Ce que la loi cherche : presque rien n'est relevé

La note ne relève que trois formulations d'objectif :

- l'intitulé de la loi n° 2002-76 : « institution de mesures d'allégement de la charge fiscale
  et d'amélioration des ressources des collectivités locales » ;
- l'intitulé de la loi n° 2007-53 : « complétant les dispositions du code de la fiscalité
  locale pour l'amélioration des modalités de perception des taxes revenant aux collectivités
  locales » ;
- la rubrique de l'art. 33 de la LF 2009 : « Amélioration du recouvrement de la TIB et de la
  TNB » (note, § 3.3).

S'y ajoutent les mots mêmes des articles 137 et 391 du code de 2018, et son article 1er, déjà
cité au chapitre d'histoire. **Partout ailleurs : « objet non relevé ».** Le rédacteur n'écrit
pas ce que la loi cherche tant que le ticket du § 8 n'est pas rendu ; il écrit ce qui change.

### 0.4 Forme commune

- `.domicile-unique` sur le titre de niveau 1 de chaque chapitre (modèle : TVA). Les lois
  sortent du fil : lien `[…](#r-fl-…)` vers la ligne de registre. Préfixes : `r-fl-imm-`,
  `r-fl-act-`, `r-fl-tax-`. Les sources budgétaires et les rapports de la Banque mondiale
  restent cités sur place.
- La règle de date (loi n° 93-64, art. 2), répétée en tête des trois chapitres, quitte le fil :
  un registre replié par chapitre, sur le modèle de `r-mt-pe-dates-1993`.
- La frise de tête n'existe encore dans aucun chapitre converti : `<!-- TODO (rédacteur) :
  frise -->`, et le tableau court des réformes en tient lieu, comme aux politiques de l'emploi.
- **Les sections « Notations » disparaissent** (aucun chapitre converti n'en porte) : chaque
  symbole est redéfini dans le texte principal de la section qui l'emploie. Rien ne se perd :
  les neuf et cinq définitions y sont déjà, mot pour mot.
- Les identifiants existants sont tous gardés ; ceux d'une section qui disparaît deviennent une
  ancre `[]{#…}` à l'endroit où son contenu arrive (listés aux registres de destination).
- Un titre de section ne dépend pas d'un seul enfant : `check_numerotation.py` refuse une
  section à une seule sous-section.
- Trois sections « La longue période » promettent des chiffres « au chapitre de la longue
  période » qui « ne sont pas encore réunis ici » : ils le sont depuis le 5 octobre. Ces
  phrases sont remplacées par les figures (ch. 6, 7) ou par un renvoi (ch. 8).
- `docs/recherches.yml` : le champ `ou` des cinq fiches `r-cfl-*` désigne fichier et section ;
  il se met à jour quand une ancre change de section (`recherches.py verifier`).
- `docs/notes/backlog-precis.md` se met à jour dans le même changement.

---

## 1. Chapitre 6 — Les impôts sur les immeubles

### 1.1 Le constat

299 lignes, 5 004 mots, 77 appels de citation (26 clés, 70 couples clé-localisateur),
24 identifiants, 8 ancres de glossaire dans les trois chapitres dont 6 ici, 7 `TODO`,
4 ancres `RECHERCHE` (3 fiches distinctes).

| Section actuelle | Lignes | Contenu |
|---|---|---|
| Chapeau | 1-5 | notions mobilisées ; « il suit le plan commun » ; règle de date |
| Les origines | 7-13 | textes abrogés en 1997, connus par leur objet |
| L'institution par le code de 1997 | 15-85 | le code (tableau des 8 chapitres) ; TIB (cinq alinéas à tête grasse, un tableau, une formule) ; TNB (deux formules) |
| Les barèmes fixés par décret | 87-198 | prix de référence (3 onglets) ; tarif TNB (3 onglets) |
| Les réformes, une à une | 200-250 | quatre périodes : 1998-2003, 2002-2007, 2009-2014, 2019-2025 ; tableau de la pénalité |
| Les textes, en un tableau | 252-279 | 20 lignes |
| La longue période | 281-283 | trois phrases, sans chiffre |
| Notations | 285-299 | 9 symboles |

**Tableaux : 7 identifiés, 11 grilles, 67 lignes** — `tbl-fl-code-chapitres` (8),
`tbl-fl-tib-taux` (4), `tbl-fl-tib-prix-reference` (3 onglets × 4 = 12), `tbl-fl-tnb-tarif`
(3 onglets × 3 = 9), `tbl-fl-penalite-retard` (5), `tbl-fl-immeubles-textes` (20),
`tbl-fl-immeubles-notations` (9). Aucune figure.

**Ce qui noie le lecteur.**

1. Le chapitre dit lui-même, à la ligne 202, que « les textes identifiés depuis 1997 ne
   touchent ni l'assiette ni les taux » — puis déroule quatre périodes et vingt textes de
   procédure sur le même plan. L'information principale (rien ne change dans le calcul ; tout
   se joue sur le recouvrement) est une phrase d'attaque de section, pas un plan.
2. Les quatre périodes sont des commodités de dates : « 2002-2007 » mêle la pénalité, un
   abandon de créances, la contribution au fonds de l'habitat, les jardins exonérés,
   l'attestation de paiement et la déclaration des locations.
3. L'alinéa « Recensement, recouvrement, contentieux » (l. 67) tient neuf règles de procédure
   en un paragraphe, au même niveau que l'assiette.
4. Six grilles de barèmes en onglets pour 33 valeurs, dont le lecteur doit ouvrir trois
   onglets pour voir qu'un seul minimum n'a pas bougé depuis 1997.
5. Aucun chiffre de rendement, alors que la série existe et dit l'essentiel : de 7 % à 3 %
   des recettes de fonctionnement, un taux de recouvrement publié de 11 à 24 %.

### 1.2 La frontière, et les ruptures retenues

**La frontière.** Les règles de base : pour chacune des deux taxes, qui paie, sur quelle
assiette, à quel taux, selon quel barème en dinars, avec quelles exonérations, et comment la
taxe se perçoit (rôle, déclarations, attestation). Sans elles, pas de taxe. Les dispositifs
secondaires aménagent la taxe pour un public ou une situation : le dégrèvement (contribuables
aidés, immeubles inoccupés), la contribution au Fonds national d'amélioration de l'habitat
(prélèvement adossé à l'assiette, autre bénéficiaire), la pénalité de retard, les abandons
d'arriérés (contribuables en retard).

**Mise en place et grandes réformes.**

| Réforme | Texte et articles | Ce que la loi cherche | Avant → après | Mise en œuvre | Dispositifs qui y naissent |
|---|---|---|---|---|---|
| **1997 — le code** | loi n° 97-11, art. 3 à 5 de la loi ; code, art. 1 à 34 | intitulé : « portant promulgation du code de la fiscalité locale ». Rubriques non relevées | trois taxes de textes distincts (valeur locative, 1902 ; entretien et assainissement, 1920 et 1948 ; contribution foncière sur les terrains non bâtis, 1919), dont seul l'objet est connu → deux taxes d'un même code ; dans les textes du fonds de l'habitat, la « valeur locative » devient l'« assiette de la taxe sur les immeubles bâtis » (art. 5 de la loi) | effet au 1er janvier 1997 ; recensement dans l'année (art. 4 de la loi) ; premiers barèmes le 13 mars 1997 (décrets n° 97-431 et 97-432) ; modalités du dégrèvement le 24 juin 1998 (décret n° 98-1254) ; **relèvements des barèmes au 1er janvier 2008 et au 1er janvier 2017** | le dégrèvement, partiel et total (art. 6) ; la pénalité de retard (art. 19) |
| **2002 — un premier abandon d'arriérés, sous condition de paiement** | loi n° 2002-76, art. 1 et 2 | intitulé : « institution de mesures d'allégement de la charge fiscale et d'amélioration des ressources des collectivités locales » | arriérés dus en entier, avec pénalités → abandon des anciennes taxes de 1996 et avant jusqu'à 30 D par article de rôle, et des pénalités de 2001 et avant contre 20 % du principal et un calendrier | renouvelé quatre fois, chaque fois sur des années plus récentes : LFC 2012, art. 17 ; LF 2019, art. 72 (abandon total) ; LF 2024, art. 59 (terrains non bâtis compris ; personnes physiques et morales distinguées) ; LF 2025, art. 76 | les abandons d'arriérés |
| **2006-2009 — la perception : l'attestation de paiement et la déclaration des locations** | LF 2006, art. 53, 56 et 57 ; loi n° 2007-53, art. 1 à 3 ; LF 2009, art. 33 | loi de 2007, intitulé : « pour l'amélioration des modalités de perception des taxes revenant aux collectivités locales » ; LF 2009, rubrique de l'art. 33 : « Amélioration du recouvrement de la TIB et de la TNB » ; LF 2006 : objet non relevé | attestation de paiement exigée pour l'autorisation de bâtir (art. 13) ; immeuble déclaré par le contribuable → attestation exigée pour sept actes (permis de bâtir ou de clôture, changement d'affectation, lotissement, inscription au rôle, habitation principale, récolement, permis d'occuper) ; locataire, occupant et gestionnaire tenus de déclarer toute location sous huit jours, sous peine d'amende | étape ultérieure : LF 2013, art. 55 (légalisation de signature des actes immobiliers, permis de démolir) | — |

**Ce qui n'est pas une grande réforme, et où cela va.**

| Texte | Classement | Place |
|---|---|---|
| Décrets n° 2007-1185, 2007-1186, 2017-396, 2017-397 | étapes de 1997 (révision des barèmes) | état du droit, sous-sections des barèmes |
| LF 2003, art. 77-78 (fin du dégrèvement partiel) | rupture propre au dégrèvement : un des deux dégrèvements disparaît | section du dégrèvement ; signalée dans l'entre-temps |
| LF 2005, art. 11-16 (contribution de 4 % au fonds de l'habitat) | rupture propre à la contribution : **refonte, non naissance** — une taxe au profit du fonds existait (LF 1999, art. 52 ; décret beylical du 23 août 1956, abrogé par cette loi) | section de la contribution ; signalée dans l'entre-temps |
| LF 2002, art. 87 ; LF 2007, art. 54 ; LF 2022, art. 68 ; LF 2023, art. 59 | ajustements de la pénalité | section de la pénalité |
| LF 2002, art. 43 ; LF 2005, art. 82 ; LF 2014, art. 30 | ajustements des exonérations | registre des exonérations |
| LF 1999, art. 52 | ajustement (bénéficiaires du dégrèvement total exonérés de la taxe du fonds) | sections du dégrèvement et de la contribution |
| LF 2014, art. 55 (impôt foncier d'État assis sur les deux taxes) | hors chapitre : impôt d'État, exposé au volume « La fiscalité » ; sa suppression n'a pas été relue par la note | une phrase dans l'entre-temps, avec le renvoi existant |
| Code des collectivités locales, 2018 | sans effet sur les deux taxes | une phrase à la fin des grandes réformes, renvoi `@sec-fl-ccl-categories` |

**Deux lectures concurrentes, à trancher (§ 9).**

- *2006-2009.* Lecture retenue : une réforme portée par trois textes voisins de même objet
  (deux le disent dans leurs mots). Autre lecture : la seule loi n° 2007-53 fait rupture
  (nouveau public tenu de déclarer), l'attestation de paiement n'étant qu'une suite
  d'ajustements de l'art. 13. La première est retenue parce que la rubrique de la LF 2009 nomme
  le même objet ; elle tombe si la rubrique de l'art. 53 de la LF 2006 dit autre chose.
- *2002.* Lecture retenue : l'abandon conditionnel est un dispositif nouveau, que quatre lois
  reprennent. Autre lecture : mesure ponctuelle de 2002, sans suite avant dix ans, à ranger tout
  entière dans sa section. La première est retenue parce que l'intitulé de la loi dit un
  objectif (les ressources des collectivités) que les règles de base ne portaient pas.

### 1.3 Le plan cible

```
# Les impôts sur les immeubles {#sec-fl-immeubles .domicile-unique}
## Vue d'ensemble {#sec-fl-immeubles-vue-ensemble}
## La mise en place, 1997 {#sec-fl-immeubles-code}
### Ce que le code remplace {#sec-fl-immeubles-origines}
### Le code de la fiscalité locale {#sec-fl-code-1997}
### La taxe sur les immeubles bâtis {#sec-fl-tib-1997}
### La taxe sur les terrains non bâtis {#sec-fl-tnb-1997}
## Les grandes réformes {#sec-fl-immeubles-reformes}
### 2002 : un premier abandon d'arriérés, contre le paiement de l'année {#sec-fl-immeubles-abandon-2002}
### 2006-2009 : l'attestation de paiement et la déclaration des locations {#sec-fl-immeubles-recouvrement}
### Entre les réformes, et depuis 2009 {#sec-fl-immeubles-attestation}
## L'état du droit en 2025 {#sec-fl-immeubles-etat-du-droit}
### Les règles en vigueur {#sec-fl-immeubles-regles}
### Les barèmes fixés par décret {#sec-fl-immeubles-baremes}
#### Le prix de référence du mètre carré couvert {#sec-fl-tib-prix-reference}
#### Le tarif au mètre carré des terrains non bâtis {#sec-fl-tnb-tarif}
## Dégrèvement, contribution au fonds de l'habitat, pénalité et abandons {#sec-fl-immeubles-dispositifs}
### Le dégrèvement {#sec-fl-immeubles-degrevement}
### La contribution au Fonds national d'amélioration de l'habitat {#sec-fl-immeubles-fnah}
### La pénalité de retard {#sec-fl-immeubles-penalite}
### Les abandons d'arriérés {#sec-fl-immeubles-abandons}
## La longue période : ce que rapportent les deux taxes {#sec-fl-immeubles-longue-periode}
### Le rendement {#sec-fl-immeubles-rendement}
### Le recouvrement {#sec-fl-immeubles-recouvrement-donnees}
```

Pour chaque section : **E** l'essentiel en une phrase (à écrire par le rédacteur dans ce
sens) ; **V** la vue d'ensemble ; **P** les points ; **R** les blocs repliés, titre exact.

**Chapeau.** Garde les deux premières phrases (les deux taxes ; ce sont des impôts au sens des
notions) et les trois renvois aux notions. Le guide de lecture annonce ce que le chapitre
donne : qui paie, sur quoi, combien, ce que la collectivité décide, ce que les taxes
rapportent. « Il suit le plan commun… » disparaît.

**Vue d'ensemble.**
- E : deux taxes annuelles sur la propriété, dues par le propriétaire, calculées sur une
  surface et un prix administré (bâti) ou sur la valeur vénale (non bâti), encaissées par la
  collectivité ; depuis 1997 la loi n'en a changé ni l'assiette ni les taux, et a agi sur leur
  perception.
- V : `tbl-fl-immeubles-reformes` (nouveau, 3 lignes : 1997, 2002, 2006-2009 ; colonnes
  réforme — ce que la loi cherche — avant → après — mise en œuvre), tiré du tableau du § 1.2.
  Renvoi à `@fig-fl-immeubles-rendement` pour le poids des deux taxes : aucun chiffre isolé ici.
- P : (1) le calcul n'a pas changé depuis 1997, seuls les barèmes en dinars ont été relevés,
  deux fois ; (2) la collectivité ne décide que du prix de référence, dans une fourchette, et
  du dégrèvement ; (3) cinq lois ont abandonné des arriérés ; (4) la part des deux taxes dans
  les recettes de fonctionnement (renvoi à la figure).
- R : « Dates d'application des textes des taxes sur les immeubles : la règle générale et les
  clauses propres, 1997-2025 » — registre `r-fl-imm-dates-…` : loi n° 93-64, art. 2 ; art. 3 de
  la loi n° 97-11 ; clauses propres (LF 1999, art. 52 ; LFC 2012).

**La mise en place, 1997.**
- *Ce que le code remplace.* E : le code réunit en 1997 trois taxes plus anciennes sous deux
  noms. Texte actuel des l. 9-11, remonté d'un niveau de titre ; la seconde phrase de la l. 11
  (« ne sont pas exposées ») devient l'énoncé de ce qui est connu : l'objet de chaque texte.
  `TODO` de la l. 13 gardé.
- *Le code de la fiscalité locale.* E : une loi, 95 articles, huit chapitres, un par
  prélèvement ; en vigueur le 1er janvier 1997. V : une phrase qui nomme les huit prélèvements
  et le chapitre du volume qui traite chacun. P : champ (art. 2 de la loi) ; recensement dans
  l'année ; le code ne classe pas en impôts, taxes et redevances. R : « Code de la fiscalité
  locale : les huit chapitres, intitulés français et arabes, articles, rédaction de 1997 »
  (`tbl-fl-code-chapitres`, 8 lignes, inchangé).
- *La taxe sur les immeubles bâtis.* E : la taxe est égale à un taux, fonction des services
  rendus, appliqué à 2 % d'un prix de référence au mètre carré multiplié par la superficie
  couverte. V : la formule $T = \tau\,\alpha\,p\,s$, ses symboles définis sur place, et
  `tbl-fl-tib-taux` (4 lignes, premier plan). P : qui paie (art. 1-2) ; quatre catégories de
  superficie ; six services, quatre taux ; qui est exonéré (une phrase, l'actuelle) ; ce que la
  collectivité fixe. Le dégrèvement est annoncé en deux phrases, renvoi à sa section.
  R : « Taxe sur les immeubles bâtis : superficie couverte, classement d'office et plafond du
  loyer, rédaction de 1997 (art. 4) » ; « Taxe sur les immeubles bâtis : recensement, rôle,
  déclarations, sanctions et contentieux, rédaction de 1997 (art. 7 à 28) » (l'alinéa de la
  l. 67, en liste) ; « Taxes sur les immeubles : le code de 1997, articles et pages » —
  registre `r-fl-imm-1997-…` (art. 2 à 5 de la loi ; art. 1-2, 3, 4-5, 6, 7-28, 30-34).
- *La taxe sur les terrains non bâtis.* E : 0,3 % de la valeur vénale réelle du terrain, ou, à
  défaut, un tarif au mètre carré selon la densité de la zone. V : les deux formules, symboles
  définis sur place. P : qui paie ; sept exonérations (phrase actuelle) ; mêmes règles de
  perception que la taxe sur les immeubles bâtis. R : aucun.

**Les grandes réformes.** Chapeau : la phrase de la l. 202, récrite avec pour sujet l'État et
non « les textes ».
- *2002.* E : en 2002, l'État abandonne pour la première fois des arriérés, à condition que le
  contribuable paie une part du principal. Deux ou trois phrases (ce que la loi cherche, par
  son intitulé ; pour qui), puis renvoi à `@sec-fl-immeubles-abandons`. Pas de bloc.
- *2006-2009.* E : de 2006 à 2009, la collectivité obtient deux moyens de perception — nul
  n'obtient un permis ou un acte sans attestation de paiement, et toute location lui est
  déclarée. V : tableau court (nouveau, 4 lignes : 1997, 2006, 2009, 2013 — actes subordonnés à
  l'attestation). P : les actes concernés ; les personnes tenues de déclarer et l'amende ; le
  rôle individuel ; la rubrique de 2009.
- *Entre les réformes, et depuis 2009.* Une phrase par fait, chacune avec son renvoi : barèmes
  relevés en 2008 et 2017 (`@sec-fl-immeubles-baremes`) ; dégrèvement partiel supprimé en 2003 ;
  contribution au fonds refondue en 2005 ; exonérations retouchées en 2002, 2005 et 2014 ;
  attestation étendue en 2013 ; impôt foncier d'État de 2014 (renvoi au volume « La
  fiscalité ») ; pénalité modifiée quatre fois ; abandons renouvelés ; code de 2018 sans effet
  sur les deux taxes (`@sec-fl-ccl-categories`).
- R, en fin de section : « Exonérations de la taxe sur les immeubles bâtis et de la taxe sur
  les terrains non bâtis : textes, date par date, 1997-2014 » (5 lignes, colonne Portée) ;
  « Perception des taxes sur les immeubles — attestation de paiement, rôle, déclaration des
  locations : textes, date par date, 1997-2013 » (5 lignes, colonne Portée).

**L'état du droit en 2025.** La réserve — aucun barème postérieur à 2017 identifié — s'écrit
une fois, ici, avec les trois ancres `RECHERCHE`.
- *Les règles en vigueur.* E : en 2025, les deux taxes se calculent comme en 1997, sur les
  barèmes du 1er janvier 2017. V : `tbl-fl-immeubles-etat` (nouveau, tableau court : une ligne
  par élément — redevable, assiette, taux, barème, exonérations, dégrèvement, pénalité — une
  colonne par taxe), fait des seuls faits déjà au chapitre, chaque cellule liée à son registre.
- *Le prix de référence.* E : le décret fixe un minimum et un maximum par catégorie ; la
  collectivité choisit dans la fourchette. V : `tbl-fl-tib-prix-reference` sous forme
  compacte — 4 lignes (catégories), 3 colonnes (1997, 2008, 2017), « minimum – maximum » dans
  chaque case : les 24 valeurs en un coup d'œil (arbitrage 3). P : le minimum de la première
  catégorie est à 100 D depuis 1997 ; en 2017 seuls les maximums montent ; les fourchettes de
  2017 se chevauchent ; les arrêtés des collectivités ne sont pas identifiés. Pas de bloc replié : une
  dernière ligne « Décret » du tableau porte, par colonne, le texte, l'article de la date
  d'effet et l'ancre `r-fl-imm-prix-…`.
- *Le tarif des terrains non bâtis.* Même forme : `tbl-fl-tnb-tarif` compact, 3 lignes
  (zones), 3 colonnes ; même ligne « Décret », ancres `r-fl-imm-tarif-…`.

**Les dispositifs.** Chaque section dit son objet, puis sa naissance (« institué par le code de
1997 », « né de la loi de 2002 »), puis son évolution.
- *Le dégrèvement.* E : depuis 2003, un seul dégrèvement subsiste, total, pour les
  contribuables aidés par l'État ou la collectivité. P : deux dégrèvements en 1997 ; organisés
  en 1998 ; le partiel supprimé en 2003 ; qui décide. R : « Dégrèvement de la taxe sur les
  immeubles bâtis : conditions et textes, date par date, 1997-2003 » (4 lignes, avec les
  conditions du décret n° 98-1254).
- *La contribution au Fonds national d'amélioration de l'habitat.* E : depuis 2005, les
  immeubles d'habitation supportent, en plus de la taxe, une contribution de 4 % de la même
  assiette, qui va à un fonds spécial du Trésor et non à la collectivité. P : avant 2005, une
  taxe au profit du fonds, dont les bénéficiaires du dégrèvement total étaient exonérés ; la
  refonte de 2005 ; mêmes exonérations et même recouvrement que la taxe ; comprise dans les
  abandons. V : tableau court de premier plan (nouveau, 3 lignes : 1997, art. 5 de la loi ;
  1999 ; 2005), qui porte les ancres — un registre de trois lignes ne se replie pas.
- *La pénalité de retard.* E : la pénalité mensuelle est de 1,25 % en 1997, descend à 0,75 %
  en 2007 et revient à 1,25 % en 2023. V : `tbl-fl-penalite-retard` (5 lignes, premier plan ;
  il devient lui-même le registre, ancres `r-fl-imm-penalite-…`). La réserve du § 10 de
  l'art. 59 et son `TODO` restent. Figure en escalier : après versement au modèle (§ 6).
- *Les abandons d'arriérés.* E : cinq lois, de 2002 à 2025, abandonnent des arriérés à qui paie
  l'année en cours. V : `tbl-fl-immeubles-abandons` (nouveau, 5 lignes ; colonnes : année de la
  loi — années abandonnées — plafond — condition — taxes couvertes), fait des faits des
  l. 214, 224, 230-234 ; il porte les ancres. P : des plafonds en dinars (2002, 2012) à
  l'abandon total (2019) ; les terrains non bâtis depuis 2024 ; personnes morales : pénalités
  seules.

**La longue période.** Les sources en une phrase (Direction générale des collectivités
locales, 2008-2019 ; budgets par commune, 2022-2023), renvoi `@tbl-fl-lp-sources` ; les
ruptures de série redites ici (périmètre de 2016 ; 2020-2021 vides ; 2021 et 2023 non
définitives ; bases du PIB, renvoi à l'annexe du site).
- *Le rendement.* V : `fig-fl-immeubles-rendement` (§ 5.1). P : les phrases des l. 138 et 140
  de `_longue_periode.qmd` qui portent sur les deux taxes (parts de 7-7,5 % puis 3,6-4,8 % puis
  3,2 et 2,9 % ; 2 à 3 % pour le non bâti ; 2011 ; 2019 à 76 MD, sans explication dans les
  sources). Marques proposées sur la figure : abandons de 2012 et 2019, barèmes de 2017 —
  **sans phrase causale**.
- *Le recouvrement.* V : `fig-fl-immeubles-recouvrement` (vue détachée de la figure actuelle).
  P : le paragraphe de la l. 142 (24 % en 2008, 11 % en 2011, 11-14 % jusqu'en 2018, 18 % en
  2019 ; définition non publiée) ; $\rho$ redéfini sur place, renvoi `@sec-fl-recouvrement`.

### 1.4 Registre de destination

| Élément actuel (lignes) | Destination | Statut |
|---|---|---|
| Titre et chapeau, § 1 (l. 1-3) | chapeau | premier plan, inchangé |
| Chapeau, § 2 : plan commun (l. 5, 1re phrase) | chapeau | récrit en guide de lecture ; l'information (ordre du chapitre) subsiste dans la table des matières |
| Chapeau, § 2 : articles « du code », règle de date, `@loi93-64` (l. 5) | Vue d'ensemble, une phrase + bloc « Dates d'application… » | premier plan (phrase) et replié (registre) |
| `#sec-fl-immeubles-origines` (l. 7-11) | « Ce que le code remplace » (niveau 3) | premier plan, identifiant gardé |
| `TODO` documentaliste, décrets de 1902-1948 (l. 13) | même section | gardé |
| `#sec-fl-immeubles-code` (l. 15) | « La mise en place, 1997 » | identifiant gardé |
| `#sec-fl-code-1997`, deux alinéas (l. 17-21) | « Le code de la fiscalité locale » | premier plan |
| `tbl-fl-code-chapitres`, 8 lignes (l. 23-36) | bloc « Code de la fiscalité locale : les huit chapitres… » | replié ; une phrase de premier plan le résume |
| TIB, « Champ et redevable » (l. 40) | « La taxe sur les immeubles bâtis », point « qui paie » | premier plan |
| TIB, « Exonérations » (l. 42) | même section, une phrase ; ligne au registre des exonérations | premier plan + replié |
| TIB, « Assiette et taux » : règle, catégories, services (l. 44) | même section | premier plan |
| TIB, exclusions de superficie, classement d'office, plafond du loyer (l. 44) | bloc « …superficie couverte, classement d'office et plafond du loyer… » | replié |
| Formule $T = \tau\alpha p s$ et symboles (l. 46-50) | même section | premier plan |
| `tbl-fl-tib-taux`, 4 lignes ; `TODO` engendré (l. 52-63) | même section | premier plan |
| TIB, « Dégrèvements » (l. 65) | annonce en deux phrases ; détail à « Le dégrèvement » | déplacé avec renvoi |
| TIB, « Recensement, recouvrement, contentieux » (l. 67) | bloc « …recensement, rôle, déclarations, sanctions et contentieux… » ; l'attestation de 1997 et la pénalité de 1,25 % sont redites au premier plan là où elles servent | replié |
| `#sec-fl-tnb-1997`, texte, deux formules (l. 69-85) | « La taxe sur les terrains non bâtis » | premier plan |
| `#sec-fl-immeubles-baremes`, alinéa d'attaque (l. 87-89) | « Les barèmes fixés par décret » (niveau 3, état du droit) | premier plan, identifiant gardé |
| `#sec-fl-tib-prix-reference`, texte (l. 91-93) | niveau 4, même identifiant | premier plan |
| `tbl-fl-tib-prix-reference`, 3 onglets, 12 lignes, 24 valeurs (l. 95-136) | tableau compact, 4 lignes, 24 valeurs, même identifiant | premier plan, **fusionné** (trois onglets en un tableau) ; les trois mentions de décret deviennent sa dernière ligne |
| `TODO` engendré (l. 138) | même place | gardé, reformulé : la forme compacte est celle des « dates repères » |
| Alinéa « aucun décret identifié… » (l. 140) | « L'état du droit en 2025 », réserve unique | premier plan, dit une fois |
| `RECHERCHE r-cfl-prix-reference-1998-2006` (l. 142, 198) | réserve unique de l'état du droit | une seule occurrence au lieu de deux ; champ `ou` à mettre à jour |
| `RECHERCHE r-cfl-prix-reference-tib-apres-2017` (l. 144) | idem | gardée |
| `TODO` arrêtés communaux (l. 146) | « Le prix de référence » | gardé |
| `#sec-fl-tnb-tarif`, texte (l. 148-150) | niveau 4, même identifiant | premier plan |
| `tbl-fl-tnb-tarif`, 3 onglets, 9 lignes, 9 valeurs (l. 152-190) | tableau compact, 3 lignes, 9 valeurs, même identifiant | premier plan, fusionné |
| `TODO` engendré (l. 192) ; alinéa (l. 194) ; `RECHERCHE r-cfl-tarif-tnb-apres-2017` (l. 196) | même section ; réserve unique | gardés |
| `#sec-fl-immeubles-reformes`, attaque (l. 200-202) | « Les grandes réformes », chapeau | premier plan, identifiant gardé |
| `#sec-fl-immeubles-degrevement` : décret n° 98-1254, LF 1999, LF 2003 (l. 204-208) | « Le dégrèvement » (identifiant gardé) ; LF 1999 aussi à la contribution | premier plan (points) + replié (conditions du décret) |
| `#sec-fl-immeubles-recouvrement`, pénalité 2002 et 2007 (l. 212) | « La pénalité de retard » | fusionné avec `tbl-fl-penalite-retard` |
| idem, loi n° 2002-76 (l. 214) | « 2002 » (annonce) et « Les abandons d'arriérés » (détail) | premier plan |
| idem, LF 2005 art. 11-16 (l. 216) | « La contribution au Fonds… » | premier plan |
| idem, LF 2005 art. 82, LF 2002 art. 43 (l. 216) | registre des exonérations ; une phrase dans l'entre-temps | replié |
| idem, LF 2006 (l. 218), loi n° 2007-53 (l. 220) | « 2006-2009 » (identifiant `sec-fl-immeubles-recouvrement` gardé) | premier plan ; mention du terme arabe du rôle : replié, registre de la perception |
| `#sec-fl-immeubles-attestation` : LF 2009, LF 2013 (l. 224) | LF 2009 à « 2006-2009 » ; LF 2013 à l'entre-temps (qui garde l'identifiant) | premier plan |
| idem, LFC 2012 art. 17 (l. 224) | « Les abandons d'arriérés » | premier plan |
| idem, LF 2014 sukuk ; impôt foncier d'État (l. 226) | entre-temps ; registre des exonérations | premier plan (phrase) + replié |
| `#sec-fl-immeubles-abandons`, trois lois (l. 228-234) | « Les abandons d'arriérés » (identifiant gardé) | premier plan |
| idem, pénalité 2022 et 2023, réserve du § 10 (l. 236) ; `TODO` (l. 238) | « La pénalité de retard » | premier plan, `TODO` gardé |
| `tbl-fl-penalite-retard`, 5 lignes ; `TODO` (l. 240-250) | « La pénalité de retard » | premier plan, avec ancres |
| `#sec-fl-immeubles-textes`, `tbl-fl-immeubles-textes`, 20 lignes (l. 252-279) | réparti entre six registres : exonérations (l. 3, 8, 15) ; perception (9, 11, 12, 14) ; dégrèvement (1, 2, 6) ; contribution (1, 7) ; pénalité (4, 10, 17, 18) ; abandons (5, 13, 16, 19, 20) | replié ou tableau court de premier plan ; les 20 lignes subsistent, la ligne 1 deux fois ; identifiants `sec-…-textes` et `tbl-…-textes` en ancres sur le premier registre |
| Phrase « les dates d'effet sont celles que fixe chaque loi de finances… » (l. 279) | bloc « Dates d'application… » | replié |
| `#sec-fl-immeubles-longue-periode` (l. 281-283) | « La longue période… » ; les trois phrases sont remplacées par les figures | identifiant gardé ; la 1re phrase subsiste dans la vue d'ensemble |
| `#sec-fl-immeubles-notations`, `tbl-…-notations`, 9 lignes (l. 285-299) | retirés ; chaque symbole défini dans sa section (déjà le cas, l. 50 et 85) | fusionné avec le texte ; identifiants abandonnés (cités nulle part) |
| 6 ancres de glossaire | toutes gardées, à la première occurrence du terme | — |

**Compte.** Avant : 7 tableaux identifiés, 11 grilles, 67 lignes, 0 figure. Après : au premier
plan, 9 tableaux courts, 40 lignes (réformes 3 ; taux 4 ; attestation 4 ; état du droit 7 ;
prix de référence 4 + 1 ; tarif 3 + 1 ; contribution 3 ; pénalité 5 ; abandons 5) ; repliés,
6 blocs, 31 lignes (chapitres du code 8 ; dates 3 ; code de 1997, 6 ; exonérations 5 ;
perception 5 ; dégrèvement 4) ; 2 figures. Les 33 valeurs de barème, les 5 états de la
pénalité et les 20 lignes de textes sont toutes retrouvées ; seules les 9 lignes de notations
cessent d'être des lignes de tableau. Le bloc des dates reste replié bien que court, comme
dans les chapitres convertis : il ne sert qu'à loger des références.

---

## 2. Chapitre 7 — Les impôts sur l'activité

### 2.1 Le constat

221 lignes, 3 977 mots, 71 appels de citation (23 clés, 60 couples), 23 identifiants, 2 ancres
de glossaire propres (`g-taxe-etablissements`, `g-taxe-hoteliere`) et une commune, 7 `TODO`,
3 ancres `RECHERCHE`.

| Section actuelle | Lignes | Contenu |
|---|---|---|
| Chapeau | 1-5 | notions ; « même plan que le précédent » ; règle de date ; renvois au volume « La fiscalité » |
| Les origines | 7-11 | lois de 1975, connues par leur intitulé |
| L'institution par le code de 1997 | 13-43 | taxe sur les établissements (cinq alinéas à tête grasse, une formule) ; taxe hôtelière ; « les autres impôts du code » (un renvoi) |
| Les barèmes fixés par décret | 45-115 | minimum (3 onglets) ; maximum |
| Les réformes, une à une | 117-157 | 2002-2007, 2011-2014, 2016-2024 ; amnisties ; taxe hôtelière |
| Les textes, en un tableau | 160-205 | assiettes et taux (8 lignes) ; textes (23 lignes) |
| La longue période | 207-209 | deux phrases, sans chiffre |
| Notations | 211-221 | 5 symboles |

**Tableaux : 5 identifiés, 7 grilles, 52 lignes** — `tbl-fl-tcl-minimum` (3 onglets × 4 = 12
lignes, 48 valeurs), `tbl-fl-tcl-maximum` (4), `tbl-fl-tcl-taux` (8), `tbl-fl-activite-textes`
(23), `tbl-fl-activite-notations` (5). Aucune figure.

**Ce qui noie le lecteur.**

1. La période « 2011-2014 » contient les deux seules réformes qui changent la taxe — la fin du
   plafond, puis l'assiette étendue à l'exportation et aux entreprises jusque-là exonérées — au
   même rang que le délai de déclaration des télédéclarants.
2. Le tableau qui dit l'état du droit (`tbl-fl-tcl-taux`) est rangé dans « Les textes, en un
   tableau », après les réformes, et mêle la taxe hôtelière à la taxe sur les établissements.
3. Le sort du produit — réparti entre collectivités, puis écrêté au-delà de 100 000 D au
   profit d'un fonds — est dispersé entre trois périodes.
4. Trois régimes qui absorbent la taxe dans un forfait (2011, 2019, 2023) sont racontés à
   trois endroits.
5. 48 valeurs de minimum en trois onglets au premier plan ; aucun chiffre de rendement, alors
   que cette taxe est le premier impôt des communes (19 % des recettes de fonctionnement en
   2008, 26 à 28 % en 2022-2023 selon les séries du volume).

### 2.2 La frontière, et les ruptures retenues

**La frontière.** Les règles de base sont celles de la taxe sur les établissements : qui la
doit, sur quelle assiette, à quel taux, avec quel plancher et quel plafond. Les dispositifs
secondaires l'aménagent pour un public ou une situation : la taxe hôtelière, qui en tient lieu
pour les établissements touristiques (art. 36) et en suit les règles (art. 44-45) ; les
forfaits et contributions uniques qui la « comprennent » pour les petits contribuables ; le
partage de son produit quand plusieurs collectivités y ont droit ; la déclaration ; les
amnisties. La taxe hôtelière est un impôt distinct, non une modalité : elle est rangée parmi
les dispositifs parce que le code la construit par renvoi à la taxe sur les établissements et
qu'aucun texte identifié ne l'a modifiée — pas par hiérarchie d'importance. À dire en une
phrase dans le chapitre.

**Mise en place et grandes réformes.**

| Réforme | Texte et articles | Ce que la loi cherche | Avant → après | Mise en œuvre | Dispositifs qui y naissent |
|---|---|---|---|---|---|
| **1997 — le code** | loi n° 97-11, art. 3 de la loi ; code, art. 35 à 45 | objet non relevé. Ce avec quoi le code rompt n'est pas connu : les lois n° 75-39 et 75-34 ne sont pas lues | deux lois de 1975 → deux chapitres du code ; taxe de 0,2 % du chiffre d'affaires brut local, ou 25 % de l'impôt dans trois cas, entre un minimum au mètre carré et un maximum annuel | effet au 1er janvier 1997 ; décrets du 13 mars 1997 (minimum, n° 97-433 ; maximum de 50 000 D, n° 97-435) ; **maximum relevé le 26 juin 2003 (60 000 D) et le 1er janvier 2007 (100 000 D) ; minimum relevé au 1er janvier 2008 et au 1er janvier 2017** | la taxe hôtelière (reprise) ; la répartition entre collectivités (art. 38 § V) |
| **2012-2013 — la fin du plafond, et l'excédent versé à un fonds** | LFC 2012, art. 50 ; LF 2013, art. 14 | objet non relevé | taxe plafonnée à 100 000 D par an → taxe sans plafond ; produit au-delà de 100 000 D par établissement et par an affecté au Fonds de coopération entre les collectivités locales | LF 2021, art. 13 : le même excédent alimente le Fonds d'appui à la décentralisation ; code de 2018, art. 392 | l'écrêtement du produit au profit d'un fonds |
| **2013-2014 — un taux réduit, puis la taxe étendue à l'exportation et aux entreprises exonérées** | LF 2013, art. 23 et 24 ; LF 2014, art. 49 et 50 | objet non relevé | chiffre d'affaires brut « local », à 0,2 % ; taxe écartée par trois régimes d'incitation → chiffre d'affaires brut ; 0,1 % sur l'exportation, sur certains services aux non-résidents et sur les produits à prix homologués à faible marge ; taxe retirée des exonérations du code d'incitation aux investissements, de la loi n° 2001-94 et de la loi n° 92-81 | — | le taux réduit de 0,1 % |

**Ce qui n'est pas une grande réforme, et où cela va.**

| Texte | Classement | Place |
|---|---|---|
| Décrets n° 2003-1345 et 2006-3360 (maximum) | étapes de 1997 | « 2012-2013 », qui raconte le plafond de bout en bout (`tbl-fl-tcl-maximum`) |
| Décrets n° 2007-1187 et 2017-395 (minimum) | étapes de 1997 | état du droit, « Le minimum par mètre carré » |
| LF 2002, art. 65 (groupements d'intérêt économique) ; LF 2005, art. 80 (non-établis exonérés) | ajustements du champ | entre-temps ; registre des redevables |
| LF 2005, art. 81 ; décret n° 2006-49 | rupture propre au partage du produit (des critères là où il n'y avait que la superficie) | section du partage |
| LF 2021, art. 37 | étape (les critères de 2006 passent dans la loi) | section du partage |
| LF 2011, art. 32 ; LF 2019, art. 42 ; LF 2023, art. 52 | trois ruptures propres aux forfaits : hors code, dans l'impôt sur le revenu | section des forfaits ; signalées dans l'entre-temps |
| LF 2003, art. 80 ; LF 2016, art. 37 ; LF 2023, art. 57 ; LF 2024, art. 67 et 69 | ajustements de la déclaration et du contrôle | section de la déclaration |
| LF 1997, art. 53 (moitié de la taxe hôtelière à un fonds du Trésor) | hors code ; état d'origine de la taxe hôtelière | section de la taxe hôtelière |
| LFC 2012, art. 15 ; LF 2019, art. 73 ; LF 2024, art. 58 ; LF 2025, art. 74 | hors code (amnisties) | section des amnisties |
| Loi n° 2006-25, décret-loi n° 2006-1, LF 2026 | repérés au plein texte, article ou page non relevés : **ne portent rien** | `TODO` existant |

**Lectures concurrentes (§ 9).**

- *Une réforme ou deux.* Lecture retenue : deux réformes, parce que les objets diffèrent — le
  montant maximal et le bénéficiaire du produit d'un côté, l'assiette et le champ de l'autre —
  et que la LF 2013 sert les deux par des articles différents. Autre lecture : une seule,
  « 2012-2014 », trois lois consécutives qui défont le régime de 1997. Les rubriques des lois
  trancheront.
- *L'art. 24 de la LF 2013.* Il est joint à la réforme de 2013-2014 parce qu'il crée le taux
  de 0,1 % que la LF 2014 étend. On peut aussi y voir un simple ajustement : le cas des marges
  réglementées, taxé sur l'impôt depuis 1997, passe sur le chiffre d'affaires.
- *Le lien entre la fin du plafond et l'écrêtement.* Les deux textes portent le même montant,
  100 000 D. Le chapitre le constate ; il ne dit pas que l'un a été fait pour l'autre.

### 2.3 Le plan cible

```
# Les impôts sur l'activité {#sec-fl-activite .domicile-unique}
## Vue d'ensemble {#sec-fl-activite-vue-ensemble}
## La mise en place, 1997 {#sec-fl-activite-code}
### Ce que le code reprend {#sec-fl-activite-origines}
### La taxe sur les établissements {#sec-fl-tcl-1997}
## Les grandes réformes {#sec-fl-activite-reformes}
### 2012-2013 : la fin du plafond, et l'excédent versé à un fonds {#sec-fl-tcl-2012-2013}
### 2013-2014 : un taux réduit, puis la taxe étendue à l'exportation et aux entreprises exonérées {#sec-fl-tcl-2013-2014}
### Entre les réformes, et depuis 2014 {#sec-fl-tcl-entre-temps}
## L'état du droit en 2025 {#sec-fl-activite-etat-du-droit}
### Assiettes et taux {#sec-fl-tcl-etat}
### Le minimum par mètre carré {#sec-fl-tcl-minimum}
## La taxe hôtelière, les forfaits et le partage du produit {#sec-fl-activite-dispositifs}
### La taxe hôtelière {#sec-fl-taxe-hoteliere-1997}
### Les forfaits et contributions uniques qui comprennent la taxe {#sec-fl-tcl-forfaits}
### Le partage du produit entre collectivités {#sec-fl-tcl-partage}
### Déclaration, délais et amendes {#sec-fl-tcl-declaration}
### Les amnisties {#sec-fl-tcl-amnisties}
## La longue période : ce que rapportent les deux impôts {#sec-fl-activite-longue-periode}
```

Ancres gardées pour les sections qui disparaissent : `sec-fl-activite-autres` (vue
d'ensemble) ; `sec-fl-activite-baremes` (état du droit) ; `sec-fl-tcl-maximum` (sur
`tbl-fl-tcl-maximum`, dans « 2012-2013 ») ; `sec-fl-tcl-2002-2007` et `sec-fl-tcl-2016-2024`
(entre-temps) ; `sec-fl-tcl-2011-2014` (« 2012-2013 ») ; `sec-fl-taxe-hoteliere-reformes`
(« La taxe hôtelière ») ; `sec-fl-activite-textes`, `tbl-fl-activite-textes` (premier registre
replié des grandes réformes).

**Chapeau.** Garde le premier alinéa (deux impôts ; l'impôt partagé ; aucun pouvoir local sur
l'assiette ni le taux) et les deux renvois au volume « La fiscalité ». « Le chapitre suit le
même plan que le précédent » devient un guide de lecture : qui paie, sur quoi, combien, à quelle
collectivité va le produit, ce que la taxe rapporte.

**Vue d'ensemble.**
- E : la taxe sur les établissements est due par toute entreprise sur son chiffre d'affaires,
  déclarée et payée aux services de l'État, et revient aux collectivités ; la taxe hôtelière en
  tient lieu pour les établissements touristiques.
- V : `tbl-fl-activite-reformes` (nouveau, 3 lignes, tiré du § 2.2). Renvoi à
  `@fig-fl-activite-rendement`.
- P : (1) 0,2 % du chiffre d'affaires, jamais moins qu'un minimum au mètre carré ; (2) le
  plafond, relevé deux fois, disparaît en 2012, et l'excédent au-delà de 100 000 D par
  établissement va à un fonds ; (3) depuis 2014 l'exportation et les entreprises des régimes
  d'incitation y sont soumises, à 0,1 % pour l'exportation ; (4) les petits contribuables la
  paient dans un forfait. Une phrase reprend l'ancienne section « Les autres impôts du code »
  (spectacles, licence, droits de marché : renvoi `@sec-fl-taxes-code`).
- R : « Dates d'application des textes des impôts sur l'activité : la règle générale et les
  clauses propres, 1997-2024 » (registre `r-fl-act-dates-…` ; la clause propre de l'art. 50 de
  la LFC 2012 y figure).

**La mise en place, 1997.** Première phrase : renvoi à `@sec-fl-code-1997` pour le code.
- *Ce que le code reprend.* E : les deux impôts datent de 1975 ; le code les reprend en 1997.
  Texte des l. 9-11 ; `TODO` gardé.
- *La taxe sur les établissements.* E : la taxe est le plus grand de deux montants — 0,2 % du
  chiffre d'affaires brut local, ou un minimum calculé sur la surface des locaux — dans la
  limite d'un maximum annuel. V : la formule $T = \max(\tau A, \mu s)$, symboles définis sur
  place. P : qui la doit (art. 35-36) ; l'assiette sur l'impôt, à 25 %, dans trois cas ; le
  minimum et ses quatre catégories d'immeubles ; le maximum ; à qui va le produit quand
  l'activité s'étend sur plusieurs collectivités (renvoi à la section du partage). La taxe
  hôtelière est annoncée en une ligne, renvoi à sa section. R : « Taxe sur les établissements :
  déclaration, délais, contrôle et contentieux, rédaction de 1997 (art. 39 et 40) » ;
  « Impôts sur l'activité : le code de 1997, articles et pages » (registre `r-fl-act-1997-…`).

**Les grandes réformes.**
- *2012-2013.* E : en 2012 le plafond de la taxe disparaît ; en 2013 ce que chaque
  établissement paie au-delà de 100 000 D cesse d'aller à la collectivité où il est installé.
  V : `tbl-fl-tcl-maximum` (4 lignes, premier plan : 50 000, 60 000, 100 000 D, suppression).
  P : le plafond de 1997 à 2011 ; sa suppression, avec effet au 1er janvier 2012 ; l'affectation
  de l'excédent à un fonds de coopération, puis en 2021 au fonds d'appui à la décentralisation ;
  renvoi en tête vers `@sec-fl-fccl-2018` pour les fonds, et vers `@sec-fl-tcl-partage`.
- *2013-2014.* E : en deux lois de finances, la taxe gagne un taux réduit de 0,1 % et s'étend
  au chiffre d'affaires à l'exportation et aux entreprises que trois régimes d'incitation en
  dispensaient. V : renvoi à `@tbl-fl-tcl-taux`. P : le taux réduit des produits à prix
  homologués, et l'option ; la fin du cas des marges réglementées ; le mot « local » supprimé ;
  0,1 % sur l'exportation et certains services aux non-résidents ; les trois régimes
  d'exonération d'où la taxe est retirée.
- *Entre les réformes, et depuis 2014.* Une phrase par fait, avec renvoi : groupements
  d'intérêt économique (2002) ; non-établis exonérés (2005) ; critères de répartition (2005,
  2006, 2021) ; forfaits (2011, 2019, 2023) ; déclaration (2003, 2016, 2023, 2024) ; minimum
  relevé (2008, 2017) ; code de 2018 sans effet sur les deux impôts (`@sec-fl-ccl-categories`).
- R : « Taxe sur les établissements — redevables et exonérations : textes, date par date,
  1997-2014 » (4 lignes, colonne Portée) ; « Taxe sur les établissements — assiette, taux et
  plafond : textes, date par date, 1997-2014 » (9 lignes, colonne Portée).

**L'état du droit en 2025.** Réserve unique : aucun barème du minimum postérieur à 2017
identifié (ancres `r-cfl-minimum-tcl-apres-2017`, `r-cfl-prix-reference-1998-2006`).
- *Assiettes et taux.* E : en 2025, la taxe est de 0,2 % du chiffre d'affaires brut, de 0,1 %
  dans trois cas, de 25 % de l'impôt pour les forfaitaires et les établissements en perte.
  V : `tbl-fl-tcl-taux` (premier plan), ramené aux lignes de la taxe sur les établissements —
  la ligne de la taxe hôtelière va à sa section, celle de l'auto-entrepreneur à celle des
  forfaits — et une colonne par chose : date d'effet, assiette, taux, option. Figure en
  escalier des taux : après versement au modèle (§ 6).
- *Le minimum par mètre carré.* E : la taxe ne peut être inférieure à un montant au mètre carré
  qui dépend de la catégorie de l'immeuble et du taux de la taxe sur les immeubles bâtis
  applicable au local. V : la grille en vigueur depuis le 1er janvier 2017 (4 lignes, 16
  valeurs, premier plan, identifiant `tbl-fl-tcl-minimum`). P : quatre catégories ; relevée en
  2008 et en 2017 ; s'applique aussi sans chiffre d'affaires. R : « Minimum de la taxe sur les
  établissements : montants par mètre carré selon la catégorie d'immeuble, barèmes de 1997 et
  de 2008, et les trois décrets » (2 onglets, 8 lignes, 32 valeurs ; registre des décrets,
  3 lignes).

**Les dispositifs.**
- *La taxe hôtelière.* E : les établissements touristiques paient, au lieu de la taxe sur les
  établissements et de la taxe sur les immeubles bâtis, 2 % de leur chiffre d'affaires brut
  global ; la moitié du produit va à un fonds du Trésor pour la protection des zones
  touristiques. V : tableau court (nouveau, 2 lignes, registre : code, art. 41-45 ; LF 1997,
  art. 53), et renvoi à la figure. P : assiette et taux inchangés depuis 1997 ; règles de la
  taxe sur les établissements pour le reste ; l'ancre `RECHERCHE
  r-cfl-taxe-hoteliere-modificatifs` et le `TODO` sur l'art. 39 de la LF 1993 restent.
- *Les forfaits et contributions uniques.* E : trois régimes de l'impôt sur le revenu font
  payer la taxe dans un montant unique, sans déclaration séparée. V : tableau court (nouveau,
  4 lignes : 1997, forfaitaires taxés à 25 % de leur impôt ; 2011, forfait de l'art. 44
  quater ; 2019, contribution unique des petits exploitants ; 2023, auto-entrepreneur, 20 % de
  l'impôt, sans minimum) ; il porte les ancres. Renvoi en tête au chapitre de l'impôt sur le
  revenu du volume « La fiscalité ». `TODO` sur le décret-loi n° 2020-33 gardé.
- *Le partage du produit.* E : quand un redevable exerce dans plusieurs collectivités, la taxe
  se répartit entre elles ; depuis 2013, la part d'un établissement au-delà de 100 000 D va à
  un fonds. P : la superficie couverte (1997) ; des critères par décret (2005-2006 : carrière,
  50 % ; immeubles non bâtis, 30 % ; chiffre d'affaires) ; ces critères dans la loi, et la
  superficie « nonobstant l'usage » (2021) ; l'écrêtement (renvoi à « 2012-2013 »). R :
  « Partage du produit de la taxe sur les établissements entre collectivités : textes, date
  par date, 1997-2021 » (6 lignes, colonne Portée).
- *Déclaration, délais et amendes.* E : la taxe est déclarée chaque mois à la recette des
  finances. R : « Taxe sur les établissements — déclaration, délais,
  contrôle et amendes : textes, date par date, 1997-2024 » (6 lignes). Le texte principal tient
  en un alinéa : c'est la procédure.
- *Les amnisties.* E : quatre lois étendent à la taxe, à la taxe hôtelière et au droit de
  licence les amnisties des impôts d'État. V : tableau court (4 lignes, registre). `TODO` gardé.

**La longue période.** Sources et ruptures de série redites (comme au ch. 6). V :
`fig-fl-activite-rendement` (§ 5.1), **sur les seules séries budgétaires, 2008-2023**. P : ce
que les l. 138 et 140 de `_longue_periode.qmd` disent des deux impôts d'après la Direction
générale et les budgets par commune (taxe sur les établissements : 19 % des recettes de
fonctionnement en 2008, 28 % en 2017, 26-28 % en 2022-2023 ; 0,16 % du PIB en 2008, 0,27 % en
2023 ; taxe hôtelière : 2,1 % en 2011, puis 1,5-2,7 % ; recul de 2011) ; la comparaison avec
les deux taxes sur les immeubles, en une phrase, renvoi à `@fig-fl-immeubles-rendement`.
Marques sur la figure : 2012 (fin du plafond), 2014 (assiette étendue) — sans phrase causale.

**Les points de 1990 à 1996 n'entrent pas au ch. 7 dans cette vague.** Ils viennent d'un
rapport de la Banque mondiale (1997), et le ch. 7 ne porte aujourd'hui aucun chiffre d'un
rapport extérieur : leur donner une place ici serait trancher une doctrine que le propriétaire
a réservée. Ils restent à `#sec-fl-lp-impots` (arbitrage 4).

### 2.4 Registre de destination

| Élément actuel (lignes) | Destination | Statut |
|---|---|---|
| Chapeau, § 1 (l. 3) | chapeau | premier plan, inchangé |
| Chapeau, § 2 : « même plan », règle de date, `@loi93-64` (l. 5) | guide de lecture ; bloc « Dates d'application… » | récrit ; replié |
| Chapeau, § 2 : renvois au volume « La fiscalité » (l. 5) | chapeau | premier plan |
| `#sec-fl-activite-origines` (l. 7-9) ; `TODO` (l. 11) | « Ce que le code reprend » (niveau 3) | premier plan ; gardés |
| `#sec-fl-tcl-1997`, « Redevables » (l. 17) | « La taxe sur les établissements » | premier plan ; lignes au registre des redevables |
| idem, « Assiette et taux » (l. 19) | même section | premier plan |
| idem, « Minimum », formule (l. 21-27) | même section | premier plan |
| idem, « Maximum et répartition » (l. 29) | même section (maximum, agricoles) ; répartition annoncée, détail à « Le partage du produit » | premier plan ; déplacé avec renvoi |
| idem, « Déclaration, contrôle » (l. 31) | bloc « …déclaration, délais, contrôle et contentieux, rédaction de 1997… » | replié |
| `#sec-fl-taxe-hoteliere-1997` (l. 33-37) ; `TODO` (l. 39) | « La taxe hôtelière » (identifiant gardé) ; une ligne d'annonce dans la mise en place | déplacé avec renvoi |
| `#sec-fl-activite-autres` (l. 41-43) | une phrase de la vue d'ensemble | fusionné ; identifiant en ancre |
| `#sec-fl-activite-baremes` (l. 45) | « L'état du droit en 2025 » | identifiant en ancre |
| `#sec-fl-tcl-minimum`, texte (l. 47-49) | « Le minimum par mètre carré » | premier plan, identifiant gardé |
| `tbl-fl-tcl-minimum`, onglet 2017, 4 lignes | même section | premier plan, identifiant gardé |
| idem, onglets 2008 et 1997, 8 lignes | bloc « Minimum de la taxe sur les établissements : … barèmes de 1997 et de 2008… » | replié (`tbl-fl-tcl-minimum-anciens`) |
| `TODO` engendré (l. 94) ; alinéa (l. 96) ; deux `RECHERCHE` (l. 98, 100) | même section ; réserve unique de l'état du droit | gardés |
| `#sec-fl-tcl-maximum`, `tbl-fl-tcl-maximum`, 4 lignes ; `TODO` (l. 102-115) | « 2012-2013 » | premier plan ; identifiant de section en ancre |
| `#sec-fl-activite-reformes`, attaque (l. 117-119) | « Les grandes réformes », chapeau | récrit, identifiant gardé |
| `#sec-fl-tcl-2002-2007` (l. 121-123) | entre-temps (une phrase par fait) ; critères de répartition à « Le partage du produit » ; contentieux du minimum à « Déclaration… » | réparti ; identifiant en ancre |
| `#sec-fl-tcl-2011-2014`, LF 2011 (l. 127) | « Les forfaits… » | premier plan |
| idem, LFC 2012 (l. 129) ; LF 2013 art. 14 (l. 131) | « 2012-2013 » | premier plan ; « objet d'un chapitre à venir » devient un renvoi |
| idem, LF 2013 art. 23-24 (l. 131) ; LF 2014 (l. 133) | « 2013-2014 » | premier plan |
| `#sec-fl-tcl-2016-2024`, déclarations et délais (l. 137, 143) | « Déclaration, délais et amendes » | replié pour l'essentiel |
| idem, LF 2021 art. 37 et 13 (l. 139) | « Le partage du produit » ; « 2012-2013 » (mise en œuvre) | premier plan |
| idem, contributions uniques (l. 141) ; `TODO` (l. 145) | « Les forfaits… » | premier plan ; gardé |
| `#sec-fl-tcl-amnisties` (l. 147-149) ; `TODO` (l. 151) | « Les amnisties » | premier plan ; « ne sont pas détaillées ici » devient l'énoncé de ce que ces lois font |
| `#sec-fl-taxe-hoteliere-reformes` (l. 153-155) ; `RECHERCHE` (l. 157) | « La taxe hôtelière » | fusionné ; identifiant en ancre ; ancre gardée |
| `tbl-fl-tcl-taux`, 8 lignes ; `TODO` (l. 162-175) | « Assiettes et taux » (6 lignes) ; ligne de la taxe hôtelière à sa section ; ligne de l'auto-entrepreneur à « Les forfaits… » | premier plan, éclaté ; les 8 lignes subsistent |
| `tbl-fl-activite-textes`, 23 lignes (l. 177-205) | réparti : taxe hôtelière (l. 1) ; redevables (2, 5, 15) ; assiette, taux, plafond (4, 8, 10, 12, 13, 14) ; partage (6, 7, 11, 18, 19) ; forfaits (9, 17, 20) ; déclaration (3, 16, 21, 22, 23) | replié ou tableau court ; les 23 lignes subsistent |
| `#sec-fl-activite-longue-periode` (l. 207-209) | « La longue période… » | identifiant gardé ; phrases remplacées par la figure |
| `#sec-fl-activite-notations`, 5 lignes (l. 211-221) | retirés ; symboles définis sur place (déjà le cas, l. 27) | fusionné avec le texte |

**Compte.** Avant : 5 tableaux identifiés, 7 grilles, 52 lignes, 0 figure. Après : au premier
plan, 7 tableaux courts (réformes 3 ; maximum 4 ; assiettes et taux 6 ; minimum de 2017, 4 ;
taxe hôtelière 2 ; forfaits 4 ; amnisties 4) ; repliés, 8 blocs (dates 3 ; code de 1997, 5 ;
redevables 4 ; assiette, taux et plafond 9 ; minimums anciens 8 ; décrets du minimum 3 ;
partage 6 ; déclaration 6) ; 1 figure. Les 48 valeurs du minimum, les 4 du maximum, les
8 lignes de taux et les 23 lignes de textes sont toutes retrouvées.

---

## 3. Chapitre 8 — Taxes, redevances et autonomie fiscale

### 3.1 Le constat

135 lignes, 3 194 mots, 48 appels de citation (10 clés, 38 couples), 17 identifiants, une ancre
de glossaire (`g-code-fiscalite-locale`), 7 `TODO`, aucune ancre `RECHERCHE`.

| Section actuelle | Lignes | Contenu |
|---|---|---|
| Chapeau | 1-5 | ce que réunissent les chapitres V à VIII ; notions ; règle de date |
| Les origines | 7-11 | sept textes abrogés, connus par leur objet |
| Les taxes et redevances du code de 1997 | 13-82 | spectacles ; riverains ; licence ; diverses (liste de six sections, parkings) ; tarifs fixés par décret |
| Les réformes, une à une | 84-86 | un alinéa, cinq textes |
| Ce que les collectivités peuvent moduler | 88-111 | cinq décisions ; tableau « qui fixe quoi » |
| Le code des collectivités locales de 2018 | 113-131 | deux catégories de ressources ; la transition |
| La longue période | 133-135 | deux phrases, sans chiffre |

**Tableaux : 3, 20 lignes** — `tbl-fl-parkings-1997` (3), `tbl-fl-taxes-baremes` (9),
`tbl-fl-qui-fixe` (8). Aucune figure.

**Ce qui noie le lecteur.** Ce chapitre est le moins chargé des trois ; son défaut est
d'ordre.

1. Sa question — qui fixe le tarif — n'arrive qu'à la ligne 88, après cinq fiches de
   prélèvements ; le tableau qui y répond (`tbl-fl-qui-fixe`) est aux trois quarts du chapitre.
2. La seule grande réforme, le code de 2018, vient en dernier, après « Les réformes, une à
   une », qui n'en dit rien.
3. `tbl-fl-taxes-baremes` range sous une même colonne « Valeur » une assiette, un taux, un
   plafond de prix, un tarif à trois catégories et une pénalité, avec deux lignes « idem ».
4. L'état du droit d'aujourd'hui n'est pas dit : la section sur la transition s'achève sur
   trois « n'est pas établi ici », dont un que le volume établit ailleurs (§ 7, point 1).

### 3.2 La frontière, et les ruptures retenues

**La frontière.** La règle de base du chapitre est le pouvoir de fixer : pour chaque
prélèvement, ce qui relève de la loi, du décret, de la collectivité. Les prélèvements eux-mêmes
— spectacles, riverains, licence, formalités, autorisations, marchés, domaine, prestations,
parkings — sont les dispositifs : chacun a sa section. Ce choix suit le titre du chapitre et
l'ordre économique : le produit de ces droits est mesuré en bloc par les budgets, non
prélèvement par prélèvement.

**Mise en place et grandes réformes.**

| Réforme | Texte et articles | Ce que la loi cherche | Avant → après | Mise en œuvre | Dispositifs qui y naissent |
|---|---|---|---|---|---|
| **1997 — le code** | loi n° 97-11, art. 3 de la loi ; code, art. 46 à 95 | objet non relevé | sept textes de 1887 à 1971, connus par leur objet → quatre chapitres du code ; la loi fixe la liste, un décret les tarifs (art. 92) ; cinq décisions laissées à la collectivité, dont trois sur ces prélèvements (art. 53, 59, 93) | décrets du 13 mars et du 7 avril 1997 (licence, n° 97-434 ; spectacles, n° 97-530) ; décret de tarifs n° 98-1428 du 13 juillet 1998 et ses six modificatifs, **connus par leur seul intitulé** ; décret gouvernemental n° 2016-805, qui l'abroge | naissances groupées (reprises) : spectacles, riverains, licence, taxes et redevances diverses, contribution aux parkings |
| **2018 — les droits et redevances confiés aux conseils élus** | loi organique n° 2018-29, art. 137, 139, 140, 141, 391 (édition arabe seule) | dans les mots de l'art. 137 : des droits « qui n'ont pas le caractère d'impôt ou de contribution au sens de l'article 65 de la Constitution, et dont les collectivités locales fixent les montants ou les taux par leurs conseils élus » | tarifs fixés par décret → montants, tarifs, exonérations et réductions délibérés par chaque conseil ; les art. 46 à 95 du code de 1997 cessent de s'appliquer collectivité par collectivité | **non établie** : décrets transitoires de l'art. 391 et délibérations tarifaires non identifiés ; conseils municipaux dissous depuis 2023 (établi ailleurs dans le volume) | — |

**Ce qui n'est pas une grande réforme.**

| Texte | Classement | Place |
|---|---|---|
| Décret gouvernemental n° 2016-805 | **classement suspendu** : étape de 1997 (nouveau décret de tarifs) tant que le décret de 1998 n'est pas lu ; rupture si celui-ci ne laissait aucun tarif à la collectivité (§ 9) | « Entre 1997 et 2018 » ; « Les tarifs fixés par décret » |
| LF 2002, art. 88 (pénalité des commissionnaires) | ajustement | section des marchés ; registre |
| Loi n° 2002-76, art. 3 (dégrèvement total des riverains) | ajustement (un dégrèvement de la taxe sur les immeubles bâtis étendu) | section des riverains |
| LF 2003, art. 79 (barème des parkings) | ajustement, barème non transcrit | section des parkings |
| LF 2013, art. 74 (groupements hydrauliques) | ajustement | section des prestations ; registre |
| Décret n° 98-1428 ; décrets n° 2000-232, 2000-1692, 2003-1346, 2004-80, 2012-1958, 2013-3236 ; arrêtés du 4 mars 1997 et du 30 mai 2003 (parkings) | étapes de 1997, **connues par leur seul intitulé** ; les sept derniers ne sont pas au chapitre et n'ont pas de clé bibliographique | lignes de registre possibles, signalées comme telles, après passage du bibliographe ; sinon rien |
| Décret n° 2003-457 (billets de spectacles) | hors sujet (couverture sociale des artistes) | rien |
| Décret-loi n° 2023-9 (dissolution des conseils municipaux) | hors note ; établi aux chapitres d'histoire et des compétences | renvoi dans l'état du droit |

### 3.3 Le plan cible

```
# Taxes, redevances et autonomie fiscale {#sec-fl-taxes .domicile-unique}
## Vue d'ensemble {#sec-fl-taxes-vue-ensemble}
## La mise en place, 1997 {#sec-fl-taxes-mise-en-place}
### Ce que le code remplace {#sec-fl-taxes-origines}
### Quatre chapitres du code, et des tarifs fixés par décret {#sec-fl-taxes-architecture}
## Les grandes réformes {#sec-fl-taxes-reformes}
### Entre 1997 et 2018 : des ajustements, un nouveau décret de tarifs {#sec-fl-taxes-1997-2018}
### 2018 : les droits et redevances confiés aux conseils élus {#sec-fl-ccl-2018}
#### Deux catégories de ressources {#sec-fl-ccl-categories}
#### La transition {#sec-fl-ccl-transition}
## Qui fixe quoi : l'état du droit {#sec-fl-moduler}
### Les quatre impôts : la loi et le décret {#sec-fl-moduler-impots}
### Les droits et redevances : du décret à la délibération {#sec-fl-moduler-droits}
## Les prélèvements, un à un {#sec-fl-taxes-code}
### La taxe sur les spectacles {#sec-fl-spectacles}
### La contribution des propriétaires riverains {#sec-fl-riverains}
### Le droit de licence sur les débits de boissons {#sec-fl-licence}
### Les taxes et redevances diverses {#sec-fl-taxes-diverses}
### La contribution aux parkings collectifs {#sec-fl-parkings}
### Les tarifs fixés par décret {#sec-fl-taxes-tarifs}
## La longue période : ce que rapportent les droits et redevances {#sec-fl-taxes-longue-periode}
```

Tous les identifiants actuels sont gardés ; `sec-fl-ccl-categories`, cité au chapitre des
compétences, descend d'un niveau sans changer de nom.

**Chapeau.** Garde le premier alinéa moins sa dernière phrase, qui devient guide de lecture :
qui fixe chaque prélèvement, ce que le code de 2018 y change, puis chaque prélèvement — qui le
paie, sur quoi, combien.

**Vue d'ensemble.**
- E : à côté de leurs quatre impôts, les collectivités perçoivent des droits et redevances,
  dont la loi fixe la liste et un décret le tarif ; le code des collectivités
  locales de 2018 en confie le tarif aux conseils élus, selon une transition dont l'application
  n'est pas établie.
- V : `tbl-fl-taxes-reformes` (nouveau, 2 lignes : 1997, 2018) et renvoi à `@tbl-fl-qui-fixe`.
- P : (1) aucune collectivité ne fixe le taux d'un impôt ; (2) le code de 1997 lui laisse cinq
  décisions (art. 4, 6, 53, 59 et 93 : les quatre premières puces de la l. 92-95, l'art. 53 et
  l'art. 59 comptés à part ; la cinquième puce, sur le décret de 2016, est dite à part) ; (3) en 2018 la ligne de
  partage devient la nature du prélèvement : l'impôt à la loi, le droit à la délibération ;
  (4) ce que ces droits pèsent (renvoi à la longue période).
- R : « Dates d'application des textes des taxes et redevances : la règle générale, 1997-2018 »
  (registre `r-fl-tax-dates-…`).

**La mise en place, 1997.** Première phrase : renvoi à `@sec-fl-code-1997`.
- *Ce que le code remplace.* Texte de la l. 9 ; `TODO` gardé.
- *Quatre chapitres du code.* E : les chapitres V à VIII reprennent ces prélèvements ; la loi
  en fixe la liste, un décret le tarif. V : naissances groupées — une ligne par prélèvement
  (ce qu'il frappe, qui le paie), avec renvoi à sa section. P : l'art. 92 (tarifs par décret,
  sauf les parkings) ; l'art. 93 (déchets non ménagers, tarif de la collectivité sous
  approbation de la tutelle) ; l'art. 94 (perception). Le classement de chaque prélèvement au
  regard des notions (l. 19, 25, 44) est réuni ici en un alinéa, au lieu de trois.

**Les grandes réformes.**
- *Entre 1997 et 2018.* E : jusqu'en 2018, ces prélèvements ne connaissent que des
  ajustements. Une phrase par fait (l. 86), avec renvoi à la section du prélèvement ; le
  décret de 2016 y est décrit par ce qu'il fait (il abroge celui de 1998 ; son annexe fixe
  tantôt un montant, tantôt une fourchette dans laquelle la collectivité arrête le tarif),
  **sans dire que cette faculté naît en 2016** (§ 7, point 2).
- *2018.* E : le code des collectivités locales rattache le pouvoir de fixer un prélèvement à
  sa nature. Texte des l. 117-125, en deux sous-sections ; l'édition arabe seule ; la date
  d'application aux communes vient de `@sec-fl-budg-ccl-vigueur` (art. 383), par renvoi.
- R : « Taxes et redevances des chapitres V à VIII du code de la fiscalité locale : textes,
  date par date, 1997-2016 » (environ 12 lignes ; colonnes : date d'effet — prélèvement —
  Portée — texte et article — ce qui change) ; « Code des collectivités locales de 2018 : les
  articles sur les ressources propres (art. 137, 139 à 141, 391 et 392), édition arabe »
  (6 lignes).

**Qui fixe quoi : l'état du droit.** Le titre ne porte pas d'année : pour les droits et
redevances, l'état du droit d'aujourd'hui n'est pas établi par la note, et **le rédacteur ne
l'écrit pas**. Il écrit ce qui l'est, daté.
- *Les quatre impôts.* E : en 2025, la loi fixe l'assiette et le taux des quatre impôts, un
  décret leurs barèmes ; la collectivité ne décide que du prix de référence de la taxe sur les
  immeubles bâtis, dans une fourchette, et du dégrèvement. V : `tbl-fl-qui-fixe` (8 lignes,
  premier plan, titre actuel gardé : « avant l'application du code des collectivités locales »).
  P : l'alinéa de la l. 111 (pas de flexibilité fiscale).
- *Les droits et redevances.* E : le décret de tarifs en vigueur depuis le 5 juillet 2016 fixe
  ces droits, et laisse la collectivité en arrêter certains dans une fourchette ; le code de
  2018 prévoit que les conseils élus les délibèrent. P : ce qui est établi (art. 391 ; art. 383
  par renvoi ; conseils municipaux dissous depuis le 14 mars 2023, renvoi
  `@sec-fl-comp-dissolution-2023`) ; ce qui ne l'est pas, dit une fois (décrets transitoires,
  délibérations), avec le `TODO` existant et, s'il y a lieu, une ancre `RECHERCHE` à créer par
  le documentaliste. Aucune phrase sur la part qui relève aujourd'hui de la délibération.

**Les prélèvements, un à un.** Chaque section : l'objet, qui paie, l'assiette, le taux ou le
tarif, ce que la collectivité décide. `tbl-fl-taxes-baremes` est refait en tête de cette
partie, premier plan : « Taux et tarifs des chapitres V à VII du code » — une ligne par
grandeur, colonnes séparées (prélèvement ; grandeur ; valeur ; en vigueur depuis), sans ligne
« idem » ; 7 lignes. Les deux lignes de la pénalité des commissionnaires (1,25 % puis 0,75 %)
vont dans la section des taxes diverses, en une phrase datée, et au registre.
- *Spectacles*, *riverains*, *licence* : texte actuel, moins l'alinéa de classement (remonté).
- *Taxes et redevances diverses* : la liste des six sections du chapitre VIII reste au premier
  plan (c'est la liste des prélèvements) ; les art. 92 à 94 sont remontés à la mise en place.
- *Parkings* : section propre. E : le propriétaire qui ne peut créer les places de
  stationnement exigées paie une contribution par place manquante. Le barème en vigueur depuis
  2003 n'est pas transcrit : `TODO` gardés, et le texte dit la règle (croisement de la part des
  places manquantes et de la population). R : « Contribution à la réalisation de parkings
  collectifs : barème par place selon la population de la commune, 1997-2002 »
  (`tbl-fl-parkings-1997`, 3 lignes — un barème abrogé).
- *Tarifs fixés par décret* : texte de la l. 64 ; `TODO` de transcription gardé.

**La longue période.** Voir § 5.2 : une figure est faisable sur les séries existantes, après
un travail de figure. Tant qu'elle n'est pas faite, la section tient en un renvoi à
`@sec-fl-lp-ressources` et à `@sec-fl-lp-autonomie`, et un `TODO (rédacteur)`.

### 3.4 Registre de destination

| Élément actuel (lignes) | Destination | Statut |
|---|---|---|
| Chapeau (l. 3) | chapeau ; dernière phrase en guide de lecture | premier plan |
| Règle de date, `@loi93-64` (l. 5) | bloc « Dates d'application… » | replié |
| `#sec-fl-taxes-origines` (l. 7-9) ; `TODO` (l. 11) | « Ce que le code remplace » (niveau 3) | premier plan ; gardés |
| `#sec-fl-taxes-code` (l. 13) | « Les prélèvements, un à un » | identifiant gardé |
| `#sec-fl-spectacles` (l. 15-17) | même section | premier plan |
| idem, classement au regard des notions (l. 19) | « Quatre chapitres du code… », alinéa commun | déplacé |
| `#sec-fl-riverains` (l. 21-23) ; classement (l. 25) | même section ; alinéa commun | premier plan ; déplacé |
| `#sec-fl-licence` (l. 27-29) | même section | premier plan |
| `#sec-fl-taxes-diverses`, liste des six sections (l. 31-40) | même section | premier plan |
| idem, art. 92-94 (l. 42) | « Quatre chapitres du code… » | déplacé |
| idem, classement (l. 44) | alinéa commun | déplacé |
| idem, « La contribution aux parkings » (l. 46) | « La contribution aux parkings collectifs » (section propre) | premier plan |
| `tbl-fl-parkings-1997`, 3 lignes ; deux `TODO` (l. 48-60) | bloc « Contribution à la réalisation de parkings collectifs : barème… 1997-2002 » | replié ; `TODO` gardés |
| `#sec-fl-taxes-tarifs`, texte (l. 62-64) ; `TODO` (l. 66) | même section ; le décret de 2016 est aussi annoncé dans « Entre 1997 et 2018 » | premier plan ; gardé |
| `tbl-fl-taxes-baremes`, 9 lignes ; `TODO` (l. 68-82) | tableau refait, 7 lignes, en tête des prélèvements ; 2 lignes (pénalité des commissionnaires) en phrase datée et au registre | premier plan, éclaté ; les 9 lignes subsistent |
| `#sec-fl-taxes-reformes` (l. 84-86) | « Entre 1997 et 2018 » ; l'identifiant passe au titre « Les grandes réformes » | premier plan |
| `#sec-fl-moduler`, cinq décisions (l. 88-96) | vue d'ensemble (une phrase) et « Qui fixe quoi » ; la cinquième (décret de 2016) reformulée | premier plan |
| `tbl-fl-qui-fixe`, 8 lignes (l. 98-109) | « Les quatre impôts : la loi et le décret » | premier plan |
| Alinéa de la l. 111 | même section | premier plan |
| `#sec-fl-ccl-2018`, `#sec-fl-ccl-categories` (l. 113-121) | « 2018 », sous-section « Deux catégories de ressources » | premier plan, identifiants gardés |
| `#sec-fl-ccl-transition`, art. 391-392 (l. 123-125) | « 2018 », sous-section « La transition » | premier plan |
| idem, « trois points restent à établir » (l. 127) | « Les droits et redevances : du décret à la délibération » ; le premier point est remplacé par le renvoi à l'art. 383 | premier plan, corrigé par renvoi |
| Deux `TODO` documentaliste (l. 129, 131) | même section ; le premier perd sa première demande si le ticket du § 8 la clôt | gardés |
| `#sec-fl-taxes-longue-periode` (l. 133-135) | « La longue période… » | identifiant gardé ; phrases remplacées |

**Compte.** Avant : 3 tableaux, 20 lignes, 0 figure. Après : au premier plan, 3 tableaux
(réformes 2 ; qui fixe quoi 8 ; taux et tarifs 7) ; repliés, 4 blocs (dates 2 ; parkings 3 ;
registre des textes, environ 12 ; articles du code de 2018, 6) ; 0 ou 1 figure (§ 5.2).

---

## 4. Le classement des textes

Le classement de chaque texte de la note est donné, par chapitre, aux § 1.2, 2.2 et 3.2
(tableaux « Mise en place et grandes réformes » et « Ce qui n'est pas une grande réforme »). La
colonne « Portée » des registres repliés le reprend ligne à ligne, avec trois valeurs :
« rupture », « étape — de 1997 », « étape — de 2002 », etc., et « ajustement ».

Textes qui ne peuvent porter aucune rupture, quel que soit leur contenu :

| Texte | Ce qui est connu | Conséquence |
|---|---|---|
| Décrets de 1887 à 1956, loi n° 71-41, lois n° 75-34 et 75-39 | l'objet, d'après la liste d'abrogation de 1997 | la mise en place dit ce que le code remplace, non avec quoi il rompt |
| Décret n° 98-1428 et ses six modificatifs | intitulé et pages, d'après la base de métadonnées ; grilles non lues | étapes de 1997, signalées comme connues par leur intitulé |
| Décret gouvernemental n° 2016-805 | articles 1 et 2 et forme de l'annexe lus dans la « traduction française pour information » ; grille non transcrite ; édition arabe, qui fait foi, lue pour l'art. 2 | décrit ; classement suspendu (§ 9, arbitrage 5) |
| Décret n° 94-822 et ses compléments (zones municipales touristiques) ; LF 1993, art. 39, rédaction initiale | numéros et intitulés ; non lus | `TODO` existant à la section de la taxe hôtelière ; rien d'autre |
| Loi organique n° 2007-65, art. 7 (classification budgétaire des ressources) | référence, d'après la base de métadonnées ; non lue | `TODO` existant au ch. 8 ; la figure du ch. 8 ne rattache donc pas les catégories budgétaires au code |
| Décret-loi n° 2020-33, art. 7, rédaction initiale | non lu | `TODO` existant à la section des forfaits |
| LFC 2014, art. 38 (suppression de l'impôt foncier) | d'après une entrée bibliographique, non relue | rien au chapitre ; renvoi au volume « La fiscalité » |
| Loi n° 2006-25, décret-loi n° 2006-1, LF 2026 (amnisties) | repérés au plein texte, article ou page non relevés | `TODO` existant |
| Constitution de 2014, art. 65 | cité par l'art. 137 du code de 2018 ; non lu | nommé dans la citation de l'art. 137, rien d'autre |
| Décret-loi n° 2026-4 du 30 septembre 2026 (conseils municipaux) | trois articles lus sur un texte converti, à relire à l'image (`backlog-precis.md`) | **absent du plan** ; risque signalé (§ 10) |

## 5. Les figures

### 5.1 Ce qui vient de `_longue_periode.qmd`

| Section ou figure de la longue période | Revient aux trois chapitres ? | Destination |
|---|---|---|
| `#sec-fl-lp-impots`, `fig-fl-lp-impots` (4 vues : MD, part des recettes de fonctionnement, % du PIB, taux de recouvrement de la taxe sur les immeubles bâtis) | **oui, pour le budgétaire** | deux figures nouvelles tirées du même code : taxe sur les immeubles bâtis et taxe sur les terrains non bâtis au ch. 6 ; taxe sur les établissements et taxe hôtelière au ch. 7 ; vue du recouvrement déplacée au ch. 6. La figure d'origine reste, allégée, pour ses points de 1990-1996 |
| Alinéas des l. 114, 138, 140, 142 | **oui**, sauf ce qui vient du rapport de 1997 | répartis par impôt (§ 1.3, 2.3) ; l'alinéa des sources (l. 114) est redit en une phrase dans chacun ; la phrase sur 1990-1996 reste |
| `#sec-fl-lp-sources`, `tbl-fl-lp-sources`, les trois ruptures de série | non (communs à tout le volume) | restent jusqu'à la seconde vague ; chaque chapitre redit en une phrase ce dont sa figure dépend, et renvoie |
| `#sec-fl-lp-ressources`, `fig-fl-lp-ressources` | non | seconde vague (budgets ou transferts) |
| `#sec-fl-lp-autonomie`, `fig-fl-lp-autonomie` | non — **arbitrage 4** | recommandé : chapitre des budgets (seconde vague) ; le ch. 8 y renvoie |
| `#sec-fl-lp-fccl`, `#sec-fl-lp-cpscl` | non | seconde vague (transferts) |
| `#sec-fl-lp-ins` | non | seconde vague (budgets) |
| `tbl-fl-lp-ecarts` | deux lignes concernent les impôts (2010 : concordance avec Dafflon et Gilbert ; taxe sur les immeubles bâtis de 2006-2007, 53,5 puis 28,2 MD) | reste entier pendant cette vague : il mêle des rapports extérieurs. Les ch. 6 et 7 y renvoient d'une phrase ; le sort de la ligne de 2006-2007 dépend de la doctrine à venir sur les rapports extérieurs |
| `tbl-fl-lp-notations`, ligne $\rho$ | oui | redéfini au ch. 6, « Le recouvrement » |

**Les figures à tirer de `fig-fl-lp-impots`.** Les données existent ; le travail est de code,
dans `precis/fr/finances_locales/figures/finances_locales.py`.

| Figure | Série | État |
|---|---|---|
| `fig-fl-immeubles-rendement` (slug `fig_fl_immeubles_rendement`) : taxe sur les immeubles bâtis et taxe sur les terrains non bâtis, 3 vues, 2008-2023 | `finances-locales-communes-agregats` (variables `tib`, `tnb`, `recettes_t1`) ; `cnat-pib-nominal` — toutes deux dans `precis/_seriescache/` | **faisable maintenant** : `fig_impots`, `table_impots`, `vues_impots` paramétrées par un sous-ensemble de `IMPOTS` |
| `fig-fl-immeubles-recouvrement` (slug `fig_fl_tib_recouvrement`) : taux de recouvrement publié, 2008-2019 | même série, variable `taux_recouvrement_tib` | **faisable maintenant** : `fig_recouvrement_tib` existe, à sortir de `vues_impots` |
| `fig-fl-activite-rendement` (slug `fig_fl_activite_rendement`) : taxe sur les établissements et taxe hôtelière, 3 vues, 2008-2023 | même série (`tcl`, `taxe_hoteliere`) ; `cnat-pib-nominal`. **Sans** `finances-locales-bm-1997` | **faisable maintenant**, même paramétrage, sources `dgct` et `somme` seules |

À régler dans le même changement :

- **`fig-fl-lp-impots` et le slug `fig_fl_impots` restent à la longue période pendant cette
  vague**, allégés : la vue du recouvrement et les alinéas de lecture sur 2008-2023 partent
  aux ch. 6 et 7 ; il y reste la figure à quatre impôts, qui est seule à porter les points de
  1990-1996 du rapport de la Banque mondiale de 1997 et la comparaison des quatre impôts, la
  phrase sur 1990-1996 (l. 138, début) et deux renvois. Leur sort se règle à la seconde vague,
  quand la place des rapports extérieurs sera fixée. L'identifiant n'est cité par aucun autre
  chapitre.
- **À qui appartiennent ces modifications.** La scission dans `figures/finances_locales.py`,
  l'allègement de `#sec-fl-lp-impots` et le remplacement des trois phrases de promesse des
  ch. 6 à 8 **appartiennent aux PR de cette vague**. La fiche de la seconde vague
  (`finances-locales-transferts-budgets-plan-architecte.md`, écrite en parallèle) prévoit la
  même scission « à concilier » : elle doit la compter comme déjà faite, sans quoi deux agents
  scinderont la même figure. Elle traite aussi `fig-fl-lp-impots` comme entièrement sortie :
  il lui restera la vue à quatre impôts et les points de 1990-1996.
- **Concordance avec cette fiche, pour le reste** : sources (`tbl-fl-lp-sources`), recettes
  propres et autonomie financière au chapitre des budgets ; $\rho$ au ch. 6. Elle fait arriver
  au ch. 6, à la dissolution de la longue période, la ligne « taxe sur les immeubles bâtis,
  2006-2007 » de `tbl-fl-lp-ecarts` en phrase attribuée : cette ligne vient d'une évaluation
  de la Banque mondiale (2014), son arrivée au ch. 6 est donc **soumise à la doctrine à venir
  sur les rapports extérieurs**, non acquise. D'ici là le ch. 6 renvoie au tableau.
- **Les marques.** `_ruptures()` trace le périmètre de 2016 et les bases du PIB. Ajouter, par
  figure, les marques des textes du chapitre (`figtools.marque_rupture`) : au ch. 6, 2012 et
  2019 (abandons), 2017 (barèmes) ; au ch. 7, 2012 (fin du plafond) et 2014 (assiette). Les
  réformes de 2002 et de 2006-2009 précèdent la série : rien à marquer, et le chapitre le dit
  sans s'en excuser (la série commence en 2008).
- **Le texte de chaque figure se suffit** : périmètre de 2016, années 2020-2021 vides, 2021 et
  2023 non définitives, base du PIB par segment (renvoi à l'annexe du site), dans la note de
  lecture de chaque nouvelle figure.
- **2019.** Le pic de la taxe sur les immeubles bâtis (76 MD) tombe l'année de la LF 2019,
  art. 72, dont l'abandon est conditionné au règlement de 2017 et 2018. La marque peut être
  posée ; la phrase reste celle de la longue période : les sources n'en donnent pas
  l'explication.

### 5.2 Les figures à créer

| Figure | Série | État |
|---|---|---|
| Ch. 8 — produit des droits et redevances des communes | `finances-locales-communes-agregats` : `produit_marches` et `contribution_eclairage_public` (2008-2019, puis `produit_marches` en 2022-2023) ; catégories de recettes 2 à 5 (`autres_recettes_fiscales`, `droits_licences_services`, `occupation_exploitation_biens`, `revenus_domaine_divers`, 2018-2023) | **faisable après un travail de données** : les libellés des catégories 2 et 4 changent entre la nomenclature de 2018-2022 et celle de 2023 (fiche `sources/finances-locales-communes.md` de `tunisia-data`), 2021 est une situation non définitive, et rien n'établit la correspondance entre ces catégories et les chapitres V à VIII du code (art. 7 de la loi organique du budget non lu). La figure présente les catégories budgétaires sous leur nom, sans les rattacher au code. Hors du périmètre de la conversion |
| Ch. 8 — détail par droit (publicité, licences, abattoirs, formalités) | même série, articles de 2022 et 2023 seulement | **pas de figure** : deux points. Un tableau court de deux années serait possible ; non recommandé avant une série plus longue |
| Ch. 6 — fourchettes du prix de référence, tarif au mètre carré, pénalité, en escalier | aucune série : les valeurs ne sont que dans les tableaux faits main du chapitre | **à verser d'abord** dans la base de paramètres (§ 6) ; `figtools.fig_escalier` lit une série de l'entrepôt. D'ici là, les tableaux compacts en tiennent lieu |
| Ch. 7 — maximum et taux de la taxe sur les établissements, en escalier | idem | idem |
| Ch. 6 — produit de la contribution au fonds de l'habitat | aucune série identifiée | **à documenter d'abord** ; rien n'est proposé |
| Frises de tête (trois chapitres) | — | non faites ailleurs non plus : `TODO`, le tableau des réformes en tient lieu |

## 6. Les tableaux faits main qui devraient être engendrés

Constat à verser à `docs/notes/backlog-modele.md` (qui n'a aucune entrée sur les finances
locales) : l'arbre de paramètres d'`openfisca-tunisia` ne porte aucun impôt local — le seul
nœud au nom voisin, `impot_revenu/foncier/bati`, relève de l'impôt sur le revenu. Les neuf
`TODO (rédacteur) : remplacer par un tableau engendré` des trois chapitres n'ont donc aucun
paramètre où se brancher. **Ce n'est pas une condition de la conversion.**

| Tableau fait main | Chapitre | Valeurs | Ce qu'il faudrait au modèle |
|---|---|---|---|
| `tbl-fl-tib-taux` | 6 | 4 taux, et le taux d'assiette de 2 % | barème par nombre de services, depuis le 1er janvier 1997 |
| `tbl-fl-tib-prix-reference` | 6 | 24 (minimum et maximum, 4 catégories, 3 dates) | deux barèmes par catégorie de superficie |
| `tbl-fl-tnb-tarif` | 6 | 9, et le taux de 0,3 % | tarif par zone, 3 dates |
| `tbl-fl-penalite-retard` | 6 | 5 états | taux mensuel, plafond au principal |
| contribution au fonds de l'habitat (dans le texte) | 6 | 4 % depuis 2005 | taux |
| `tbl-fl-tcl-minimum` | 7 | 48 (4 catégories × 4 taux × 3 dates) | barème à deux entrées |
| `tbl-fl-tcl-maximum` | 7 | 4 états | montant, puis fin au 1er janvier 2012 |
| `tbl-fl-tcl-taux` | 7 | 8 lignes | taux par assiette ; taxe hôtelière à part |
| `tbl-fl-parkings-1997` | 8 | 3, et le barème de 2003 non transcrit | barème par population, puis à deux entrées |
| `tbl-fl-taxes-baremes` | 8 | 9 lignes | taux et tarifs des chapitres V à VII |

La note documentaire donne pour chacune de ces valeurs le texte, l'article, la page dans les
deux éditions et la date d'effet calculée : le versement est un travail de modéliste borné. La
forme compacte retenue pour les barèmes (une colonne par date) est celle que produirait le
composant « état du droit à des dates repères ».

## 7. Erreurs, contradictions et formules contraires aux règles, relevées en lisant

1. **Contradiction dans le volume.** Le ch. 8 (l. 127) écrit que la date d'entrée en vigueur
   des dispositions budgétaires du code de 2018 « n'est pas établie ici ». `_budgets.qmd`
   (`#sec-fl-budg-ccl-vigueur`) et `_histoire.qmd` l'établissent par l'art. 383 : budgets de
   2019 pour les communes élues en 2018. Reste à confirmer que le délai de cinq ans de
   l'art. 391 court bien de cette date (§ 8) ; d'ici là, renvoi sans conclusion.
2. **Une nouveauté non établie.** Le ch. 8 (l. 96) date du 5 juillet 2016 la faculté pour la
   collectivité d'arrêter certains tarifs dans une fourchette. La grille du décret de 1998
   n'est pas lue : rien n'établit que cette faculté n'existait pas avant.
3. **Le ch. 8 ne dit rien de la dissolution des conseils municipaux** (décret-loi n° 2023-9),
   alors que tout son dernier tiers porte sur ce que décident « les conseils élus ».
4. **Renvois périmés.** « Objet d'un chapitre à venir » (ch. 7, l. 131 ; ch. 8, l. 125) : le
   chapitre des transferts existe. « Ne sont pas encore réunis ici. Ils le seront au chapitre
   de la longue période » (ch. 6, l. 283 ; ch. 7, l. 209 ; ch. 8, l. 135) : ils y sont.
5. **Formules contraires à « on annonce ce que l'on présente »** : « ne sont pas exposées »
   (ch. 6, l. 11), « ne sont pas exposés » (ch. 7, l. 9), « ne sont pas exposées » (ch. 8,
   l. 9), « ne sont pas détaillées ici » (ch. 7, l. 149), « ne dit pas quelle part… » (ch. 8,
   l. 127).
6. **Phrases dont le sujet est « les textes »** en tête de section : ch. 6, l. 202 ; ch. 8,
   l. 86.
7. **Une colonne, plusieurs choses** : `tbl-fl-tcl-taux` (taxe hôtelière parmi les lignes de la
   taxe sur les établissements ; taux et option dans la même case) ; `tbl-fl-taxes-baremes`
   (colonne « Valeur » ; deux lignes « idem »).
8. **Dans la note documentaire** (à signaler au documentaliste, sans effet sur le plan) : le
   § 2.1 annonce « six tirets » à l'art. 3 et en énumère cinq ; le § 6.4 donne le barème des
   parkings de 2003 (« de 250 à 2 250 D par place ») mais pas celui de 1997, que le ch. 8
   publie (100, 250 et 500 D, `tbl-fl-parkings-1997`) : la provenance de ces trois valeurs est
   à confirmer sur le JORT.
9. **Deux pénalités de la même loi.** La LF 2002 ramène la pénalité de la taxe sur les
   immeubles bâtis de 1,25 % à 1 % (art. 87) et celle des commissionnaires de 1,25 % à 0,75 %
   (art. 88). La note le dit aux deux endroits ; l'écart mérite une relecture de l'art. 88.

## 8. Questions au documentaliste (ticket borné)

**A. Rubriques et intitulés — « ce que la loi cherche ».** Relever mot pour mot la rubrique
(titre de section ou d'article de la loi de finances) sous laquelle est placé chaque article :

- LF 2002, art. 43, 65, 87, 88 ; LF 2003, art. 77 à 80 ;
- LF 2005, art. 11 à 16, 80, 81, 82 ;
- LF 2006, art. 53, 56, 57 ; LF 2007, art. 54 ; LF 2009, art. 33 (confirmer) ;
- LF 2011, art. 32 ; LFC 2012, art. 15, 17, 50 ;
- LF 2013, art. 14, 23, 24, 55, 74 ; LF 2014, art. 30, 49, 50 ;
- LF 2016, art. 37 ; LF 2019, art. 42, 72, 73 ; LF 2021, art. 13 et 37 ;
- LF 2022, art. 68 ; LF 2023, art. 52, 57, 59 ; LF 2024, art. 58, 59, 67, 69 ; LF 2025,
  art. 74 et 76 ;
- intitulé des chapitres et sections du code de 2018 où sont placés les art. 137, 139 à 141 et
  391.

**B. Ce avec quoi le code rompt.** Lois n° 75-34 et 75-39 du 14 mai 1975 (au corpus) :
assiette, taux, plafond et bénéficiaires d'origine — pour que la mise en place du ch. 7 dise ce
qui change en 1997.

**C. Le sens d'un mot.** Art. 37 du code, rédaction de 1997 : que recouvre le chiffre
d'affaires brut « local » ? L'exportation en était-elle exclue ? La réforme de 2014 se lit
différemment selon la réponse ; le plan ne le déduit pas du taux de 0,1 %.

**D. Le code de 2018.** L'« entrée en vigueur des dispositions budgétaires » de l'art. 391
est-elle celle de l'art. 383 ? Les décrets gouvernementaux de l'art. 391 existent-ils (fiche
`RECHERCHE` à ouvrir) ? L'art. 43 du décret-loi n° 2023-10 et l'art. 10 de la loi organique
n° 2025-4 touchent-ils les art. 137 à 141 ?

**E. Le décret de 1998.** Son annexe laissait-elle déjà des tarifs à un arrêté de la
collectivité ? La réponse classe le décret de 2016.

**F. Les montants.** LF 2013, art. 14, et LF 2021, art. 13 : le seuil de 100 000 D est-il « par
établissement » dans les deux textes, et le maximum de l'art. 38 § III l'était-il par redevable
ou par établissement ? Barème des parkings de 1997 (art. 90) : confirmer les trois valeurs.

**H. La loi de finances pour 2026** (JORT n° 148 de 2025, édition arabe) : a-t-elle été
inventoriée pour tous les articles du code de la fiscalité locale, ou seulement pour les
art. 41 à 45 et les amnisties ? La réponse fixe l'année de « l'état du droit ».

**G. Déjà au backlog, rappelées** : portée du § 10 de l'art. 59 du décret-loi n° 2022-79 ;
barème des parkings de 2003 ; art. 7 initial du décret-loi n° 2020-33 ; décret-loi n° 2026-4.

Le ch. 6 peut être converti sans attendre (deux de ses trois objectifs sont relevés). Le ch. 7
gagne à attendre A et B. Le ch. 8 attend D et E.

## 9. Arbitrages à soumettre au propriétaire

1. **Ch. 6 : deux grandes réformes seulement, et ce sont des réformes de perception.**
   L'épine serait : 1997 ; 2002 (premier abandon d'arriérés) ; 2006-2009 (attestation de
   paiement, déclaration des locations). Les barèmes de 2008 et 2017 n'y sont que des étapes,
   la contribution au fonds de l'habitat et la fin du dégrèvement partiel des ruptures propres
   à leur section. *Recommandation : oui.* C'est ce que les textes portent, et c'est ce
   qu'éclaire la série (un taux de recouvrement publié de 11 à 24 %). L'autre choix — 2005 et
   2003 dans l'épine — ferait d'ajustements de paramètres des réformes.
2. **Ch. 7 : deux réformes (2012-2013, 2013-2014) ou une seule (2012-2014).**
   *Recommandation : deux*, parce que l'une change le montant et le bénéficiaire, l'autre
   l'assiette et le champ ; à revoir si les rubriques des lois de finances disent un objet
   commun.
3. **Les barèmes au premier plan sous forme compacte.** Prix de référence et tarif des
   terrains non bâtis : un tableau de quatre et de trois lignes, une colonne par date (1997,
   2008, 2017), à la place des trois onglets. Minimum de la taxe sur les établissements : la
   grille de 2017 au premier plan, celles de 1997 et de 2008 repliées. *Recommandation : oui* —
   l'évolution se voit d'un regard, l'état en vigueur ne se replie pas, aucune valeur ne
   disparaît. Pour le prix de référence, une case « minimum – maximum » porte deux valeurs :
   si « une colonne, une chose » doit primer, deux colonnes par date (six colonnes de
   valeurs) ; je recommande la fourchette dans une case, qui est la grandeur que fixe le décret.
4. **Les figures de rendement, et les points de 1990-1996.** Une figure par chapitre (deux
   impôts chacune), sur les seules séries budgétaires de 2008 à 2023 ; la vue du recouvrement
   au ch. 6. Les points de 1990-1996 de la taxe sur les établissements et de la taxe
   hôtelière viennent d'un rapport de la Banque mondiale : (a) ils restent à la longue période,
   dans la figure à quatre impôts allégée, jusqu'à ce que la place des rapports extérieurs
   soit fixée ; ou (b) ils entrent au ch. 7 dans une sous-section titrée comme rapport
   extérieur, avec sa méthode. *Recommandation : (a).* La figure d'autonomie financière ne
   vient pas au ch. 8 : elle va au chapitre des budgets, comme le prévoit la fiche de la
   seconde vague — l'autonomie financière (part des recettes propres) et l'autonomie fiscale
   (pouvoir sur le taux) sont deux notions que le volume distingue.
5. **Ch. 8 : ce qu'on écrit de l'état du droit.** Le décret de 2016 n'est pas présenté comme
   une rupture tant que celui de 1998 n'est pas lu ; l'état du droit des droits et redevances
   n'est pas écrit au présent — le chapitre dit ce qui est établi (le décret de 2016, les
   articles du code de 2018, la dissolution des conseils en 2023, par renvoi) et ce qui ne l'est
   pas, une fois ; le décret-loi n° 2026-4 n'est pas mentionné avant d'être lu.
   *Recommandation : oui, et convertir le ch. 8 après le ticket D-E.*

Arbitrages pris par défaut, à renverser au besoin : les sections « Notations » sont retirées ;
`tbl-fl-code-chapitres` est replié ; la taxe hôtelière est rangée après la taxe sur les
établissements, parmi les dispositifs ; la contribution aux parkings a sa section ; l'année de
l'état du droit est 2025 pour les ch. 6 et 7 (dernière loi lue : loi de finances pour 2025),
**à confirmer** : la note a parcouru la loi de finances pour 2026 pour la taxe hôtelière et
les amnisties, sans dire si elle l'a inventoriée pour tous les articles du code (§ 8, H). Si
oui, l'année devient 2026.

## 10. Les risques du plan

- **Replier la procédure peut cacher une règle qui compte.** L'attestation de paiement et la
  solidarité de l'acquéreur sont dans l'alinéa de procédure de 1997 ; elles reviennent au
  premier plan dans « 2006-2009 ». Vérifier qu'aucune règle citée ailleurs ne reste seulement
  dans un bloc.
- **Le ch. 6 peut sembler vide entre 1997 et aujourd'hui.** C'est le constat, non un défaut du
  plan ; la longue période doit le porter (rendement, recouvrement), sinon le lecteur n'a que
  des dates de procédure.
- **« 2012-2013 » juxtapose deux textes dont le lien n'est pas dit par la loi.** Risque de
  phrase causale ; le rédacteur s'en tient à la coïncidence du montant.
- **Les marques de textes sur les figures invitent à lire une causalité** (2019 surtout). Note
  de lecture explicite, ou pas de marque.
- **Le ch. 8 décrit un droit en mouvement.** Le décret-loi n° 2026-4 abroge le code de 2018 à
  une date qui dépend d'élections à venir ; tout ce que le chapitre dit des conseils élus peut
  devoir être récrit à sa lecture. Convertir le ch. 8 maintenant est une réorganisation, non
  une mise à jour : le dire dans le rapport du rédacteur et au backlog.
- **Le chapitre grossit.** À la conversion de la TVA, le texte a doublé. Ici : six tableaux
  courts nouveaux, une vingtaine de registres, trois figures. Attendu : 5 000 → 7 500 mots au
  ch. 6, 4 000 → 6 000 au ch. 7, 3 200 → 4 200 au ch. 8, le surcroît étant surtout replié.
- **Des registres très courts.** Tranché dans le plan : les décrets de barèmes sont la
  dernière ligne du tableau compact ; la contribution au fonds de l'habitat, la taxe hôtelière,
  les forfaits et les amnisties ont un tableau court de premier plan qui porte les ancres ;
  seul le bloc des dates reste replié bien que court.
- **Les tableaux nouveaux ne doivent contenir aucun fait nouveau.** `tbl-fl-immeubles-etat`,
  `tbl-fl-immeubles-abandons`, le tableau de l'attestation et celui des forfaits se font avec
  les seules phrases du chapitre actuel ; chaque cellule doit se retrouver dans la copie de
  départ.

## 11. Liste de contrôle et volume de travail pour le rédacteur

1. Copie de départ des trois fichiers et de `_longue_periode.qmd` hors du dépôt ; mesures :
   mots, appels, clés, couples, identifiants, ancres de glossaire, `TODO`, `RECHERCHE`
   (chiffres aux § 1.1, 2.1, 3.1).
2. Figures (§ 5.1) — niveau « standard », avant le ch. 6, dans les PR de cette vague et non
   dans celles de la seconde.
3. Par chapitre : réorganiser sans récrire ; aucun fait hors de la note et du ticket ; tous
   les identifiants gardés (ancres pour les sections disparues) ; puis le domicile unique
   (registres, ancres `r-fl-…`, lois hors du fil) ; `scripts/check_domicile_references.py`.
4. `_longue_periode.qmd` : alinéas de 2008-2023 et vue du recouvrement retirés de
   `#sec-fl-lp-impots` ; la figure à quatre impôts, la phrase sur 1990-1996 et deux renvois y
   restent ; `tbl-fl-lp-notations` : la ligne $\rho$ suit.
5. `docs/recherches.yml` (champ `ou` des cinq fiches `r-cfl-*`) ; `backlog-precis.md` ;
   `backlog-modele.md` (constat du § 6).
6. `scripts/verifier.sh --sans-reseau finances_locales` ; rendu vu dans le navigateur
   (dépliage par renvoi `@tbl-…`, infobulles) ; aucun chapitre arabe à écrire.

**Volume estimé**, d'après la conversion de la TVA (11 000 mots : une demi-heure de
réorganisation, un quart d'heure de domicile unique) : figure, une demi-heure ; ch. 6, trois
quarts d'heure ; ch. 7, trois quarts d'heure ; ch. 8, une demi-heure ; longue période, backlogs
et vérification, une demi-heure — environ trois heures d'agent, plus le ticket du
documentaliste (une demi-heure à trois quarts d'heure) et la relecture du propriétaire. Une PR
par chapitre, la figure dans celle du ch. 6.

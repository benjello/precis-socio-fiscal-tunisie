# Retraites — dossier documentaire

> Note **documentaire** préparatoire au livre « Retraites ». Elle ne rédige pas de prose de
> précis et n'a modifié aucun fichier de `precis/` ni aucun paramètre d'openfisca.
> Rédigée le 10 septembre 2026.

## Conventions

**Trois niveaux d'attestation**, portés sur chaque fait :

- **[T]** *texte lu* — l'article a été lu dans le fascicule du JORT, à l'image ou sur couche texte ;
- **[M]** *métadonnées* — seule la notice de `jort_cache.db` est établie (n°, dates, pages) ;
- **[D]** *dérivé* — déduit d'un autre texte, d'un rapprochement ou d'une convention.

**Quatre dates par texte** : signature / publication au JORT (n° de fascicule + page de
l'**édition française**) / **effet tel que l'énonce l'article final** / URL pist.tn. Quand aucune
clause d'entrée en vigueur n'a été lue, la case porte **« non énoncée »** — jamais dérivée de la
date de publication.

**URL** : `https://www.pist.tn/jort/<année>/<année>F/Jo<n° sur 3 chiffres><année sur 2 chiffres
jusqu'en 1999, 4 ensuite>.pdf`. Le certificat TLS de pist.tn est expiré depuis le 25 août 2026 :
les téléchargements ont été faits avec `curl -k`. Les fascicules ont été lus sur le corpus local
`~/projets/PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`, identiques à l'octet près aux fichiers
servis par pist.tn quand le contrôle a été fait.

**Les cinquante-six URL de fascicules citées par cette note ont été vérifiées une à une le
10 septembre 2026** : toutes répondent `200 application/pdf`. Les vingt-deux fascicules
effectivement ouverts l'ont été comme images ou comme couche texte, et leur édition française a été
confirmée par le pied de page (« N° X — *Journal officiel de la République tunisienne* — date —
Page Y »). Les fascicules dont seule la notice est citée n'ont pas fait l'objet de ce second
contrôle : conformément à `docs/notes/outillage-sources.md`, **un `200` ne prouve pas l'édition**.

**Une source non normative est utilisée, et signalée comme telle** : le *Manuel de liquidation des
pensions & accessoires* de la CNRPS (19 décembre 2013, 149 pages). Tout ce qui en provient est
marqué **[D]** et regroupé au § 10. Il est antérieur à la réforme de 2019.

**Écart de datation à signaler, non tranché ici.** L'article 75 de la loi n° 85-12 énonce :
« La présente loi entre en vigueur à l'expiration d'un délai de six (6) mois à compter de la date
de sa publication au *Journal officiel* » **[T]**, p. 365. Publication le **12 mars 1985**, donc
effet le **12 septembre 1985**. Le dépôt des cotisations retient cette date ; les paramètres du
dépôt `openfisca-tunisia-pension` retiennent le **5 mars 1985** (date de signature) — et le seul
barème d'annuités CNRPS retient une **troisième** date, le **1er janvier 1985**, qu'aucun texte
n'appuie. Les trois dates coexistent aujourd'hui dans le modèle ; l'écart est ici documenté, non
arbitré.

---

## 0. Résultat principal : le décret n° 74-499 a été ouvert, et il porte l'essentiel du RSNA

Le texte fondateur des pensions du privé était cité par le modèle sans avoir jamais été lu. Sa
lecture, pages 915-919 du fascicule, résout d'un coup **six des huit paramètres RSNA sans
référence**, établit la **limite de calcul des prestations** que le modèle traite comme une
constante muette, et livre l'article de **revalorisation** que le modèle ignore entièrement.

| Question posée | Réponse établie | Article | Niv. |
|---|---|---|---|
| Limite de prise en compte du salaire (assiette de la retraite complémentaire) | **six fois le SMIG**, rapporté à 2 400 heures par an, **dès 1974** ; reconduite à l'identique en 1990 | 74-499 art. 18, puis art. 18 (nouveau) du décret n° 90-1455 | **[T]** |
| Plafond du taux de liquidation RSNA | **80 %** du salaire moyen de référence | 74-499 art. 17 in fine | **[T]** |
| Fenêtre du salaire de référence RSNA | **3 ou 5 dernières années**, la plus avantageuse (1974) → **10 dernières années** (1990) → remplacé en 1994 : **5, 7 puis 10 dernières années** aux 1er juillet 1994, 1995, 1996 (voir § 12) | 74-499 art. 18, puis 90-1455, puis 94-1429 | **[T]** |
| Pension minimale RSNA | 2/3 du SMIG (1974) ; **1/2 du SMIG** pour les retraites anticipées et les pensions proportionnelles (1982) | 74-499 art. 45, puis 82-1030 art. 5 | **[T]** |
| Âge de départ anticipé RSNA (50 ans) | créé en **1982**, pas en 1974 | 82-1030, art. 15 bis | **[T]** |
| Revalorisation RSNA | « révisé en cas de hausse sensible du niveau général des salaires » (1974) → **indexation automatique sur le SMIG** (1981, puis 2001) | 74-499 art. 53, puis 81-187 et 2001-779 | **[T]** |
| Date d'effet du décret 74-499 | **1er janvier 1974**, énoncée par l'article 64 | 74-499 art. 64 | **[T]** |

**Le fascicule.** Le sommaire porte « 117ème Année — N° 30, **Mardi 30 Avril - Vendredi 3 - Samedi
4 Mai 1974** ». La mention usuelle « fascicule des 30 avril - 3 mai » est donc incomplète d'un
jour. Le fascicule est sans couche texte : lecture entièrement à l'image, à 300 puis 500 dpi pour
les chiffres.

**Un rectificatif existe** et n'a pas été ouvert : *Décret n° 74-499 (rectificatif)*, JORT
**n° 39**, publié le **7 juin 1974**, **p. 1252** **[M]**. À lire avant toute citation d'un chiffre
du décret initial (§ 8).

---

# 1. CNRPS — secteur public

## 1.0 Textes pivots

| Texte | Objet | Signature | JORT | Pages | Effet énoncé | URL | Niv. |
|---|---|---|---|---|---|---|---|
| **Loi n° 59-18** | Régime des pensions civiles et militaires | 1959-02-05 | n° 8, fasc. 3-6 févr. 1959 | 93-100 | art. 52 : droits s'ouvrant à compter du 1er avril 1959 | `/1959/1959F/Jo00859.pdf` | **[T]** (dossier cotisations) |
| **Loi n° 75-83**, art. 28 | Fusion CNR + CPS → CNRPS | 1975-12-30 | n° 87 | 2854 | — | `/1975/1975F/Jo08775.pdf` | **[T]** (dossier cotisations) |
| **Loi n° 81-70** (LF compl. 1981), art. 4-5 | Remplace les art. 22 § II et V, 26 § II, 31 § I et VI, 32 al. 1, 36, 37 et 42 al. 1 de la loi 59-18 | 1981-08-01 | n° 51 du 7 août 1981 | 1789-1790 | **art. 5 : « L'article 4 de la présente loi prend effet à compter du 1er mai 1981 »** | `/1981/1981F/Jo05181.pdf` | **[T]** |
| **Loi n° 85-12** | Régime des pensions civiles et militaires et des survivants dans le secteur public | 1985-03-05 | n° 20 du 12 mars 1985 | 359-365 | **art. 75 : six mois après publication → 12 sept. 1985** | `/1985/1985F/Jo02085.pdf` | **[T]** |
| **Décret n° 85-1177** | Liste des ouvriers accomplissant des tâches pénibles et insalubres (art. 27) | 1985-09-24 | n° 68 du 1er oct. 1985 | 1255-1256 | **art. 2 : « prend effet à compter du 1er juillet 1986 »** | `/1985/1985F/Jo06885.pdf` | **[T]** |
| **Décret n° 85-1178** | Liste des agents exerçant des fonctions astreignantes (art. 28) | 1985-09-24 | n° 68 du 1er oct. 1985 | 1256 | **art. 2 : « prend effet à compter du 1er juillet 1986 »** | `/1985/1985F/Jo06885.pdf` | **[T]** |
| **Loi n° 88-71** | Modifie l'art. 5 de la loi 85-12 (âge des enfants) | 1988-06-27 | n° 45 | — | non lue | `/1988/1988F/Jo04588.pdf` | **[M]** |
| **Décret n° 93-308** | Régime du capital-décès | 1993-02-01 | n° 13 | 246-247 | non lue | `/1993/1993F/Jo01393.pdf` | **[M]** (art. 5-6 cités par le modèle) |
| **Loi n° 2007-43** | Modifie les art. 30, 37, 46, 47 de la loi 85-12 | 2007-06-25 | n° 51 | 2198-2199 | **aucune clause d'entrée en vigueur** ; le texte s'achève sur « La présente loi sera publiée… » | `/2007/2007F/Jo0512007.pdf` | **[T]** (texte intégral FR versionné dans `openfisca-tunisia-pension/tmp/JORTs/`) |
| **Loi n° 2009-20** | Dispositions exceptionnelles, retraite des professeurs de l'enseignement supérieur | 2009-04-13 | n° 30 du 14 avril 2009 | 1036 | non lue | `/2009/2009F/Jo0302009.pdf` | **[M]** |
| **Loi n° 2019-37** | Modifie et complète la loi 85-12 (âges, option, comptes individuels, taux) | 2019-04-30 | n° 35 du 30 avril 2019 | 1312-1315 | **aucune clause d'entrée en vigueur** ; l'art. 5 fixe le calendrier de l'âge | `/2019/2019F/Jo0352019.pdf` | **[T]** |

**Fait de structure, souvent perdu.** L'article 76 de la loi 85-12 abroge la loi 59-18 « **à
l'exception des dispositions relatives à l'invalidité** » **[T]**, p. 365. L'invalidité des agents
publics reste donc régie par la loi de 1959, et la loi 85-12 renvoie deux fois (art. 41 et 47) à
« la commission de réforme prévue à l'article 29 de la loi n° 59-18 ».

## 1.1 Ouverture du droit

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| Âge de mise à la retraite, cadre commun | **60 ans** | loi 85-12, **art. 24** | **[T]** p. 361 |
| Prorogation | **70 ans** Premier Président de la Cour de cassation et Procureur général ; **65 ans** autres cadres supérieurs (liste par décret) ; **65 ans** chef de secteur | loi 85-12, **art. 25 et 26** | **[T]** p. 361 |
| Ouvriers accomplissant des tâches pénibles et insalubres | **55 ans**, liste par décret | loi 85-12, **art. 27** → décret n° 85-1177 | **[T]** |
| Agents exerçant des fonctions astreignantes | mise à la retraite après **35 ans de services** et **55 ans** ; maintien possible jusqu'à 60 ans ; liste par décret | loi 85-12, **art. 28** → décret n° 85-1178 | **[T]** |
| Cadres actifs | **55 ans**, maintien possible jusqu'à 60 ans, liste par décret | loi 85-12, **art. 29** | **[T]** |
| Militaires | 50 ans hommes de troupe, quartiers-maîtres et matelots ; 55 ans sous-officiers et officiers mariniers ; 58 ans officiers subalternes ; 60 ans officiers supérieurs ; 62 ans officiers généraux | loi 85-12, **art. 61** | **[T]** p. 364 |
| **Durée de service minimale** | **15 ans** ; **10 ans pour les ouvriers occasionnels** | loi 85-12, **art. 22** | **[T]** p. 360 |
| Dispense transitoire de la condition d'ancienneté | agents recrutés avant l'entrée en vigueur de la loi | loi 85-12, **art. 72** | **[T]** p. 365 |
| Relèvement de l'âge, calendrier | **+1 an à partir du 1er juillet 2019** pour les agents atteignant l'âge de la retraite entre cette date et le 31 décembre 2019 ; **+2 ans à partir du 1er janvier 2020** | loi 2019-37, **art. 5** (à titre transitoire, « contrairement aux dispositions des articles 24, 27, 28, 29 et 61 (nouveaux) ») | **[T]** p. 1314 |
| Nouveaux âges de régime permanent | **62 ans** (art. 24 nouveau) ; **57 ans** ouvriers pénibles (art. 27 nouveau) ; **57 ans + 35 ans de services** astreignants (art. 28 nouveau) ; **57 ans** cadres actifs (art. 29 nouveau) ; militaires 52 / 57 / 60 / 62 (art. 61 § 1 nouveau) | loi 2019-37, art. 1 | **[T]** pp. 1312-1313 |
| Augmentation optionnelle de l'âge | 1 à 3 ans sur demande écrite six mois avant ; jusqu'à 5 ans et 70 ans pour les personnes de l'art. 29 bis ; option **définitive et irrévocable** | loi 2019-37, art. 3, **titre II bis, art. 71 bis** | **[T]** p. 1313 |
| Rendement des annuités de l'augmentation optionnelle | **2 % par année supplémentaire, 0,50 % par trois mois**, « sous réserve des dispositions du deuxième tiret de l'article 38 » | loi 2019-37, **art. 71 ter** | **[T]** p. 1313 |

### Départs anticipés

| Cas | Condition | Texte | Niv. |
|---|---|---|---|
| Invalidité | — | loi 85-12, art. 5, 2° a) | **[T]** p. 359 |
| Sur demande de l'agent, après accord de l'employeur | — | art. 5, 2° b) | **[T]** |
| Démission | — | art. 5, 2° c) | **[T]** |
| Initiative de l'employeur : suppression d'emplois, insuffisance professionnelle, révocation | — | art. 5, 2° d) | **[T]** |
| **Mères de trois enfants** | sur demande, enfants **dont l'âge n'a pas dépassé 15 ans** | art. 5, 2° e) | **[T]** |
| Mères de trois enfants — relèvement à 20 ans | — | loi n° 88-71 du 27 juin 1988 | **[M]** — texte **non lu**, à ouvrir |
| **Droit général au départ anticipé** | **35 ans de services et 55 ans**, quelle que soit la fonction | loi 85-12, **art. 30** | **[T]** p. 361 |
| Idem, après 2007 | **37 ans de services et 57 ans** | loi 2007-43, **art. 30 (nouveau)** | **[T]** |
| Jouissance différée | immédiate en cas d'atteinte de l'âge légal, d'invalidité, de licenciement pour suppression d'emplois ; **différée jusqu'à 50 ans** pour les agents mis à la retraite sur leur demande ou licenciés pour insuffisance professionnelle ; **jusqu'à l'âge légal** pour les agents révoqués ou démissionnaires | loi 85-12, **art. 41** | **[T]** p. 362 |

**Bonifications** (loi 85-12, art. 32-33, **[T]** p. 361) : la bonification est une période d'années
ajoutée à la durée d'activité effective. Pour les ouvriers accomplissant des travaux pénibles et
insalubres : **5 ans** si 35 ans de services ; **4 ans** si 25 ans ; **3 ans** si 20 ans ; **2 ans**
si 15 ans. Pour les agents exerçant des fonctions astreignantes : la période restant à courir
jusqu'à 60 ans. Pour les cadres actifs : la période restant à courir jusqu'à 60 ans, **plafonnée**
par le même barème 5/4/3/2. L'article 33 accorde en outre la bonification jusqu'à 60 ans aux
militaires et agents des FSI blessés en service, aux agents invalides à 80 % au moins, et aux
agents mis à la retraite pour suppression d'emplois. Depuis la loi 2019-37 (art. 33 nouveau,
**[T]**), le repère est **62 ans**, et la bonification des agents mis à la retraite d'office est
plafonnée à un rendement de **20 %** de la rémunération de liquidation.

**Militaires** : bonification de la période restant à courir jusqu'à 60 ans pour les militaires mis
à la retraite d'office ou ayant atteint l'âge légal de leur grade (art. 67) **[T]** p. 364 ; portée
à 62 ans par la loi 2019-37 (art. 67 nouveau) **[T]**.

## 1.2 Calcul

**Salaire de référence — loi 85-12, art. 36 [T], p. 362** :

> « La pension est liquidée sur la base de la **dernière rémunération** perçue par l'agent mis à la
> retraite et ayant fait l'objet de retenues au titre des contributions […] **pendant une période
> minimum de trois ans**. […] Toutefois, la liquidation de la pension de retraite est effectuée sur
> la base de la **rémunération afférente à la fonction la plus élevée** que l'agent a effectivement
> exercé pendant une **période minimum de deux (2) années entières** au cours de sa carrière, à
> condition que les contributions au titre de cette fonction portent sur une période minimum de
> trois (3) ans. »

C'est le seul texte qui fixe la fenêtre. **Aucune notion de « deux meilleures années » n'y figure** :
le second terme de l'alternative porte sur la *fonction la plus élevée*, non sur les salaires les
plus élevés, et il est doublement conditionné (2 ans d'exercice, 3 ans de retenues).

**Barème d'annuités — loi 85-12, art. 38 [T], p. 362** :

| Tranche | Par année | Par trimestre |
|---|---:|---:|
| Les **dix premières** années | 2 % | 0,5 % |
| Les **dix deuxièmes** années | 3 % | 0,75 % |
| Les **autres** années | 2 % | 0,5 % |

> « Le montant de la pension de retraite **ne doit pas dépasser 90 %** de la rémunération sur la
> base de laquelle a été liquidée la pension. » (art. 38, dernier alinéa)

**Le plafond de 90 % est donc sourcé** — et il est arithmétiquement atteint à 40 ans de services
(20 + 30 + 40), soit 160 trimestres, ce qui explique la coïncidence entre le plafond et la borne
terminale du barème. Les deux ne sont pourtant pas la même chose : le texte pose un **plafond en
pourcentage**, que le barème rencontre par construction.

**Décompte des annuités — art. 35 [T]** : toute période inférieure à une année est calculée sur la
base du trimestre ; toute période **égale ou supérieure à 45 jours** est comptée pour un trimestre ;
toute période inférieure à 45 jours n'est pas prise en considération.

**Plafond antérieur à 1985.** L'article 22 § II (nouveau) de la loi 59-18, tel que remplacé par
l'article 4 de la loi n° 81-70, énonce **[T]**, p. 1789 :

> « La rémunération de l'ensemble des annuités liquidées […] ne peut être supérieure à **80 %** de
> la rémunération globale définie à l'article 21 ci-dessus. Elle ne peut être inférieure pour la
> pension d'ancienneté ou proportionnelle aux **2/3 du SMIG** selon les conditions qui seront
> fixées par décret. »

Le plafond du secteur public est donc passé de **80 % (au plus tard le 1er mai 1981)** à **90 % (le
12 septembre 1985)**. Le texte antérieur au 1er mai 1981 n'a pas été lu (§ 8).

## 1.3 Planchers

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Pension minimale garantie** | **2/3 du SMIG** du régime de 2 400 heures par an | loi 85-12, **art. 39** | **[T]** p. 362 |
| Idem, antérieurement | **2/3 du SMIG** pour la pension d'ancienneté ou proportionnelle | loi 59-18, art. 22 § II nouveau (loi 81-70, art. 4), effet **1er mai 1981** | **[T]** |
| **Allocation de vieillesse** | **la moitié du SMIG** du régime de 2 400 heures par an, sur option, pour les agents ayant **5 années d'ancienneté au moins** et n'atteignant pas la durée de l'art. 22 ; l'autre branche de l'option est le **remboursement des contributions** | loi 85-12, **art. 42** | **[T]** p. 362 |
| Plancher des pensions d'orphelins | ne peuvent au total être inférieures au montant des **indemnités familiales** dont aurait bénéficié l'agent | loi 85-12, **art. 48** | **[T]** p. 363 |
| Plancher de la solde de réforme (militaires) | jamais inférieure à la **pension minimum garantie** | loi 85-12, **art. 70** | **[T]** p. 364 |

## 1.4 Droits dérivés

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Conjoint survivant** | **75 %** de la pension de retraite dont l'agent avait bénéficié ou aurait pu bénéficier | loi 85-12, **art. 43** | **[T]** p. 362 |
| Réduction pour orphelins | pendant la période de paiement de la pension temporaire d'orphelin : **−5 %** au titre du 3e enfant, **−10 %** au titre de chacun des enfants suivants, **sans descendre au-dessous de 50 %** | loi 85-12, **art. 43** al. 2 | **[T]** |
| Antériorité | même mécanique (75 %, −5 %, −10 %, plancher 50 %) déjà posée par l'art. 31 § I (nouveau) de la loi 59-18 | loi 81-70, art. 4, effet 1er mai 1981 | **[T]** p. 1789 |
| Suspension | remariage avant 55 ans ; rétablissement, avec révalorisation, en cas de décès du nouveau conjoint ou de dissolution du mariage | loi 85-12, **art. 44** | **[T]** |
| Pluralité de veuves | pension répartie **à parts égales**, sans que chacune descende au-dessous du minimum légal de la pension du conjoint | loi 85-12, art. 44 in fine | **[T]** p. 363 |
| **Orphelin** | **10 %** de la pension de retraite, **jusqu'à 21 ans** | loi 85-12, **art. 45** | **[T]** p. 363 |
| **Plafond de cumul** | « Le total des pensions d'orphelins et la pension du conjoint survivant **ne doit pas dépasser le montant de la pension de l'agent**. » En cas de dépassement, réduction de la pension du conjoint selon l'art. 43 | loi 85-12, **art. 45** | **[T]** |
| **Cinq orphelins ou plus** | le conjoint bénéficie de **50 %** ; les 50 % restants sont répartis à parts égales entre les orphelins | loi 85-12, **art. 45** | **[T]** |
| Non-attribution de la pension du conjoint | répartie à parts égales entre les orphelins ; **plafonnée à 50 %** pour la fille sans ressources | loi 85-12 art. 46, **remplacé par la loi 2007-43, art. 46 (nouveau)** | **[T]** |
| Extension au-delà de 21 ans | orphelins atteints d'une maladie incurable ou d'une invalidité permanente (sans condition d'âge) ; **orphelins poursuivant des études supérieures jusqu'à 25 ans, à condition de ne pas être boursiers** ; **fille sans ressources, sans condition d'âge**, paiement définitivement suspendu si l'une des conditions vient à manquer | loi 85-12 art. 47, **remplacé par la loi 2007-43, art. 47 (nouveau)** | **[T]** |
| Cumul de deux pensions | interdit au titre des **mêmes** services ; **admis** au titre de services successifs | loi 85-12, **art. 56** | **[T]** p. 363 |
| Cumul pension propre / pension du chef du conjoint | **admis** | loi 85-12, **art. 58** | **[T]** p. 364 |
| Cumul pension / rente viagère pour invalidité | **admis** | loi 85-12, **art. 59** | **[T]** |
| Pension provisoire en cas d'absence | conjoint et enfants, après six mois d'absence | loi 85-12, **art. 50** | **[T]** p. 363 |

**Point de vigilance sur le modèle.** La documentation du paramètre `retraite.cnrps.survivants.taux_orphelin`
rattache à la loi 85-12 (art. 45-47) les conditions « 25 ans si études supérieures sans bourse ;
sans limite d'âge pour la fille sans ressources ». La lecture du fascicule de 1985 montre que ces
conditions **n'y figurent pas** : elles sont introduites par l'**article 47 (nouveau) de la loi
n° 2007-43**. Rattachement à corriger.

## 1.5 Invalidité

L'article 76 de la loi 85-12 maintient en vigueur les dispositions de la **loi n° 59-18** relatives
à l'invalidité **[T]**. Deux éléments seulement ont été établis sur pièce :

- **Rente d'invalidité** — art. 26 § II (nouveau) de la loi 59-18, tel que remplacé par l'art. 4 de
  la loi n° 81-70 **[T]**, p. 1789 : « Le montant de la rente d'invalidité est égal au produit de la
  **rémunération soumise à retenue pour pension par le taux de l'invalidité**. »
- **Commission de réforme** : art. 29 de la loi 59-18, visé par les art. 41 et 47 de la loi 85-12 et
  par l'art. 47 (nouveau) de la loi 2007-43 **[T]**.

**Le plafond « pension + rente ≤ 100 % du traitement de référence » n'a été trouvé dans aucun texte
lu**, mais il est **attesté comme doctrine de la caisse** par le *Manuel de liquidation des pensions
& accessoires* de la CNRPS (19 décembre 2013, p. 87), qui écrit **[D]** :

> « RVI = PR × TI, avec 66 % ≤ TI ≤ 100 % et **MGP ≤ (PR + RVI) ≤ R** […] Le montant de la rente
> viagère d'invalidité et de la pension de retraite **ne peut dépasser la limite de 100 % de la
> rémunération d'activité servie de base pour le calcul de la pension**. »

où PR est la pension de retraite, TI le taux d'invalidité, R la rémunération soumise à retenues pour
pension et MGP le minimum garanti. La rente viagère d'invalidité est **réversible** au profit du
conjoint survivant et des orphelins « dans les mêmes conditions et selon les mêmes taux que la
pension de retraite », et elle est **péréquable**. Le texte de rattachement reste à chercher dans les
articles 25 à 30 de la loi 59-18, non ouverte pour cette note (§ 8).

**Divergence de formule, à trancher sur le texte.** L'article 26 § II (nouveau) de la loi 59-18
(loi n° 81-70, art. 4) énonce que le montant de la rente est le produit de la **rémunération**
soumise à retenue par le taux d'invalidité **[T]** ; le manuel de la CNRPS écrit
RVI = **pension** × taux d'invalidité **[D]**. Les deux formules ne coïncident que si le taux de
liquidation vaut 100 %.

**Deux autres régimes de rente coexistent** **[D]**, manuel pp. 88-89 : la **loi n° 94-28 du
21 février 1994** (secteur privé, applicable à partir de janvier 1995), rente compensatrice à la
charge de la CNSS puis, depuis 2004, de la CNAM ; et la **loi n° 95-56 du 28 juin 1995** (secteur
public, applicable à partir de janvier 1996), rente compensatrice à la charge de l'employeur et
payée par la CNRPS, dont la formule et les bornes sont identiques à celles de la RVI. Les militaires
et les agents des forces de sécurité intérieure en sont exclus. Dans les deux cas, la période
d'attribution de la rente est réputée période d'activité cotisée pour la retraite lorsque
l'incapacité permanente dépasse 66 %.

**Réversion de la rente d'invalidité** : art. 31 § I (nouveau) de la loi 59-18 (loi 81-70)
**[T]** — la pension de veuve est « augmentée le cas échéant de **75 % de la rente d'invalidité** »
dont bénéficiait le mari.

## 1.6 Revalorisation — la péréquation

C'est **le** mécanisme du secteur public, et il n'a rien à voir avec une indexation sur un indice
de prix ou de salaire minimum.

**Loi n° 85-12, art. 37 [T], p. 362** :

> « La **péréquation** de la pension est effectuée lors de **toute augmentation de l'un quelconque
> des éléments permanents de la rémunération correspondante au grade ou à la fonction sur la base de
> laquelle a été liquidée la pension**. La péréquation de la pension est également effectuée lors de
> l'institution d'une **indemnité permanente** concernant le grade ou la fonction sur la base de
> laquelle a été liquidée la pension. Cette péréquation est soumise aux dispositions des articles 9,
> 10, 11, 13 et 36 de la présente loi. »

**Loi n° 2007-43, art. 37 (nouveau) [T]** reprend les trois alinéas mot pour mot et ajoute :

> « La totalité des contributions au titre de cette péréquation durant la période de paiement de la
> pension et de ses accessoires, **à l'exception de la quote-part des contributions mises à la
> charge de l'employeur durant 36 mois, est à la charge du bénéficiaire de la pension**. »

La péréquation est donc **cotisée**, et depuis 2007 essentiellement à la charge du retraité.

**Textes de revalorisation ponctuelle antérieurs à 1985** (série incomplète, tous **[M]**, aucun
n'a été ouvert) :

| Texte | Signature | JORT | Pages | URL |
|---|---|---|---|---|
| Décret n° 81-939, relatif à la revalorisation des pensions de retraite servies par la CNRPS | 1981-07-04 | n° 47 du 10 juill. 1981 | 1630 | `/1981/1981F/Jo04781.pdf` |
| Décret n° 82-971, même objet | 1982-06-30 | n° 48 du 2 juill. 1982 | 1496-1497 | `/1982/1982F/Jo04882.pdf` |
| Décret n° 83-737, même objet | 1983-08-10 | n° 55 du 16 août 1983 | 2158-2159 | `/1983/1983F/Jo05583.pdf` |

Recherche menée dans `jort_cache.db` en `LIKE` **non accentué** (`revalorisation`, `relevement des
pensions`, `majoration des pensions`, `augmentation des pensions`) sur 1956-2026, doublée d'une
requête FTS : **aucun texte de revalorisation CNRPS postérieur à 1983** n'apparaît. Résultat négatif
**[M]** — cohérent avec l'institution de la péréquation par la loi de 1985, qui rend inutiles les
décrets ponctuels.

## 1.7 Accessoires de pension

**Loi n° 85-12, art. 40 [T], p. 362** : « L'indemnité familiale et l'indemnité pour revenu unique
s'ajoutent le cas échéant à la pension de retraite. Ces deux indemnités sont attribuées dans les
mêmes conditions applicables aux agents en activité. »

**Antériorité** — art. 22 § V (nouveau) de la loi 59-18, remplacé par l'art. 4 de la loi n° 81-70
**[T]**, p. 1789 : « À la pension de retraite et à la pension de veuve s'ajoutent, le cas échéant,
l'indemnité familiale et une majoration pour revenu unique attribuées dans les mêmes conditions et
selon les mêmes taux et les mêmes modalités que les indemnités familiales et la majoration pour
salaire unique servies aux agents en activité. » **Effet : 1er mai 1981** (art. 5).

→ **La date `1981-05-01` portée par les paramètres `indemnite_revenu_unique` du modèle est donc
exacte et sourcée** — mais la référence qui l'accompagne (« Loi n° 81-70 du 01/08/1981 ») confond
signature et effet, et **la loi ne fixe aucun montant**. L'origine des valeurs 3,125 / 6,250 / 7,825
reste inconnue (§ 8).

**Indemnités familiales — le texte « impossible » est tranché.** Le décret cité par le modèle
« n° 85-611 du 3 juin 1986 » n'existe pas. Le texte réel est le **décret n° 86-611 du 3 juin 1986,
portant fixation des taux des indemnités à caractère familial**, JORT **n° 34 des 3-6 juin 1986**,
**p. 674**, `/1986/1986F/Jo03486.pdf` **[T]**. C'est le **millésime** qui est faux, non l'année :
`86` a été saisi `85`.

| Rang | Décret n° 86-611, art. 1er **[T]** | Modèle |
|---|---:|---:|
| Premier enfant | **7,600** | 7,320 |
| Deuxième enfant | **6,500** | 6,507 |
| Troisième enfant | **5,600** | 5,693 |
| Quatrième enfant | **4,700** | 4,880 |

- Art. 2 : abroge le décret n° 75-952 du 30 décembre 1975.
- **Art. 3 : « prend effet à compter du 1er mai 1986 »** — et non du 3 juin 1986 comme le retient le modèle.

**Aucune des quatre valeurs du modèle ne correspond au décret 86-611.** Elles ne correspondent pas
davantage au texte suivant de la série, le **décret n° 88-1136 du 11 juin 1988, portant fixation des
taux des indemnités à caractère familial**, JORT **n° 43 du 24 juin 1988**, **p. 941**,
`/1988/1988F/Jo04388.pdf` **[T]** : premier enfant **7,600**, deuxième **6,500**, troisième
**5,600** — trois rangs seulement, l'ouverture du droit ayant été ramenée aux trois premiers enfants
par la loi n° 88-39 du 6 mai 1988 — **art. 2 : « prend effet à compter du 1er janvier 1989 »**.

**Les quatre valeurs du modèle sont exactes — mais elles appartiennent à un troisième décret, de
dix ans postérieur.**

**Décret n° 96-1906 du 16 octobre 1996, portant fixation des taux des indemnités à caractère
familial**, JORT **n° 85 du 22 octobre 1996**, **p. 2097**, `/1996/1996F/Jo08596.pdf` **[T]** :

- **Art. 1er** : « Le taux mensuel par enfant à charge, des indemnités familiales dues aux
  fonctionnaires et agents de l'État, des collectivités locales et des établissements publics à
  caractère administratif est fixé comme suit : premier enfant : **7 d,320** ; deuxième enfant :
  **6 d,507** ; troisième enfant : **5 d,693**. »
- **Art. 2** : « Le taux mensuel de l'indemnité familiale due au titre du **quatrième enfant ayant
  acquis ce droit antérieurement au 1er janvier 1989**, par application des dispositions de la loi
  88-39 du 6 mai 1988, est fixé à **4 d,880**. »
- **Art. 3** : le taux dû au titre de l'**enfant handicapé venant après le 3e rang** parmi ses frères
  et sœurs est fixé à **4 d,880** (loi n° 81-46, art. 18).
- **Art. 4** : « Toutes dispositions antérieures contraires au présent décret et notamment les
  décrets n° 86-611 du 3 juin 1986 et n° 88-1136 du 11 juin 1988 sont abrogées. »
- **Art. 5 : « prend effet à compter du 1er novembre 1996 ».**

**Verdict.** Les valeurs du modèle sont justes ; sa **référence et sa date sont fausses de dix
ans**. Le rattachement correct est **décret n° 96-1906, art. 1 à 3, effet 1er novembre 1996**. Le
modèle les tient de la table de la **page 92 du *Manuel de liquidation* de la CNRPS**, qui donne les
bons chiffres mais dont la section « Cadre juridique » (p. 90) cite encore le décret abrogé, avec
une faute de millésime — « décret n° 85-611 du 3 juin 1986 ». **Le modèle a hérité du manuel à la
fois ses chiffres, sa citation périmée et sa faute de millésime.**

La série est donc close, et elle a quatre termes :

| Depuis | Texte | 1er enfant | 2e | 3e | 4e | Effet énoncé |
|---|---|---:|---:|---:|---:|---|
| 1975 | décret n° 75-952 du 30 déc. 1975, JORT n° 87, p. 2884 | — | — | — | — | **[M]** — non lu |
| 1er mai 1986 | **décret n° 86-611** | 7,600 | 6,500 | 5,600 | 4,700 | art. 3 **[T]** |
| 1er janv. 1989 | **décret n° 88-1136** (trois rangs) | 7,600 | 6,500 | 5,600 | — | art. 2 **[T]** |
| **1er nov. 1996** | **décret n° 96-1906** | **7,320** | **6,507** | **5,693** | **4,880** (droit acquis) | art. 5 **[T]** |

Curiosité à noter, non expliquée : les taux de 1996 sont **inférieurs** à ceux de 1986 pour les
trois premiers rangs. Le décret n'en donne pas la raison.

**Même constat pour l'indemnité de revenu unique.** Les trois montants du modèle — 3,125 / 6,250 /
7,825 pour un, deux et trois enfants — sont exactement la table de la **page 94** du manuel. Celui-ci
les rattache à la « loi n° 81-70 du 01/08/1981 étendant le bénéfice de l'indemnité de revenu unique
au profit des retraités du secteur public **à compter du premier mai 1981** » : la date d'effet du
modèle est donc juste, et elle remonte elle aussi au manuel. Mais la loi 81-70 ne fixe **aucun
montant** (§ 6.6), et le manuel n'indique pas le texte qui les fixe. Il cite en amont deux textes
antérieurs à l'indépendance : le **décret du 2 février 1944**, portant création de l'indemnité
familiale et de l'indemnité de revenu unique au profit des agents du secteur public, et le **décret
du 8 juin 1944**, instituant en Tunisie un régime d'allocations familiales **[D]**.

**Règles d'attribution — doctrine de la caisse** **[D]**, manuel pp. 90-95 :

- Depuis le **1er janvier 1989**, en application de la **loi n° 88-39 du 6 mai 1988, relative à
  l'octroi des indemnités familiales dans le secteur public** (JORT n° 33 du 13 mai 1988, p. 735
  **[M]**), le nombre d'enfants ouvrant droit à l'indemnité familiale est limité aux **trois
  premiers** ; le quatrième enfant déjà bénéficiaire conserve son droit acquis. *(Le manuel écrit
  « loi n° 88-3 du 6 mai 1988 » puis, deux paragraphes plus loin, « loi n° 88-39 du 06/05/1988 » :
  la seconde graphie est la bonne, la notice du JORT le confirme.)*
- La limitation ne s'applique pas aux **enfants handicapés** — article 18 de la **loi n° 81-46 du
  29 mai 1981**, relative à la promotion et à la protection des handicapés — quels que soient leur
  âge et leur rang.
- Âge limite : **16 ans**, reculé à **18 ans** en apprentissage et à **21 ans** pour les études
  secondaires, supérieures ou la formation professionnelle publique ; aucune limite pour les enfants
  handicapés.
- Sont **exclus** du bénéfice des indemnités familiales et de l'indemnité de revenu unique : les
  chefs de secteur, les députés et membres de la chambre des conseillers, les membres du
  gouvernement, les gouverneurs, et les titulaires d'une seule solde de réforme.
- L'indemnité de revenu unique suppose une famille constituée, **au moins un enfant à charge ouvrant
  droit à l'indemnité familiale**, et un **seul revenu** ; en cas de divorce elle est partagée
  proportionnellement au nombre d'enfants à charge.

---

# 2. RSNA — salariés non agricoles du privé

## 2.0 La chaîne du décret n° 74-499, texte par texte

> **Mise à jour du 11 septembre 2026** : le décret n° 94-1429 abroge et remplace les articles 18 et 19 dans leur rédaction de 1990 ; la série de la fenêtre du salaire de référence et les corrections à reporter dans cette section sont au **§ 12** (en particulier § 12.8).

| Texte | Objet établi | Signature | JORT | Pages | Effet énoncé | URL | Niv. |
|---|---|---|---|---|---|---|---|
| **Loi n° 60-33** | Institue le régime d'invalidité, vieillesse et survie et le régime d'allocation dans le secteur non agricole | 1960-12-14 | n° 57 | 1616 | non énoncée | `/1960/1960F/Jo05760.pdf` | **[M]** |
| **Décret n° 71-432** | Régime antérieur, **abrogé** par l'art. 63 du décret 74-499 | 1971-12-17 | — | — | — | — | **[T]** (par citation) |
| **Décret n° 74-499** | Régime de pension de vieillesse, d'invalidité et de survivants dans le secteur non agricole | 1974-04-27 | **n° 30, 30 avril - 3-4 mai 1974** | **915-919** | **art. 64 : « prend effet à compter du 1er janvier 1974 »** | `/1974/1974F/Jo03074.pdf` | **[T]** art. 1-2, 5, 9, 14-22, 24-35, 39-55, 63-64 |
| **Décret n° 74-499 (rectificatif)** | — | 1974-04-27 | n° 39 du 7 juin 1974 | 1252 | — | `/1974/1974F/Jo03974.pdf` | **[M]** — **non lu** |
| **Décret n° 79-536** | Ajoute un al. 2 à l'art. 45 (plancher étendu aux régimes conventionnels préexistants au décret 76-981) ; art. 54 (nouveau) : soins gratuits ; art. 55 al. 1 (nouveau) : maintien des allocations familiales | 1979-05-30 | n° 38 du 8 juin 1979 | 1671-1672 | **art. 4 : « prend effet à compter du 1er janvier 1979 »** | `/1979/1979F/Jo03879.pdf` | **[T]** |
| **Décret n° 81-187** | **Revalorisation** : art. 53 (nouveau), 53 bis et 53 ter | 1981-02-14 | n° 10 du 17 févr. 1981 | 319 | **art. 3 : « prend effet à partir du 1er mai 1980 »** | `/1981/1981F/Jo01081.pdf` | **[T]** |
| **Décret n° 81-188** | Art. 21 b), 22 al. 1, 29, 33, 34 (nouveaux) ; art. 31 al. 2 (nouveau et complémentaire) | 1981-02-14 | n° 10 du 17 févr. 1981 | 319-320 | **non énoncée** (art. 3 : clause d'exécution) | `/1981/1981F/Jo01081.pdf` | **[T]** |
| **Décret n° 82-1030** | Art. 15 bis (départs anticipés) ; art. 17 al. 2 et 3 (nouveaux) ; art. 22 al. 2 (nouveau) ; section 6 remplacée (pension proportionnelle) ; art. 45 al. 1 (nouveau) ; art. 48 al. 3 ; art. 55 (nouveau) | 1982-07-15 | n° 51, 20-23 juill. 1982 | 1605-1607 | **non énoncée** (art. 8 : clause d'exécution) | `/1982/1982F/Jo05182.pdf` | **[T]** |
| **Décret n° 82-1030 (rectificatif)** | — | 1982-07-15 | n° 66 du 19 oct. 1982 | 2197 | — | `/1982/1982F/Jo06682.pdf` | **[M]** — **non lu** |
| **Décret n° 88-1137** | Art. 5 b) (nouveau) : quote-part **4,25/20e** | 1988-06-11 | n° 43 du 24 juin 1988 | 942 | **art. 2 : « prend effet à partir du 1er janvier 1988 »** | `/1988/1988F/Jo04388.pdf` | **[T]** |
| **Décret n° 90-1455** | Art. 3, 14, 18, 30, 32, 43, 54 (nouveaux) | 1990-09-10 | n° 60 du 21 sept. 1990 | 1358 | **non énoncée** (art. 2 : clause d'exécution) | `/1990/1990F/Jo06090.pdf` | **[T]** |
| **Décret n° 94-1429** | Taux de cotisation (art. 9 nouveau) | 1994-06-30 | n° 52 | 1141-1142 | par paliers | `/1994/1994F/Jo05294.pdf` | **[T]** (dossier cotisations) |
| **Décret n° 96-326** | Art. 46 (délai de demande) | 1996-03-01 | n° 21 | 530 | — | `/1996/1996F/Jo02196.pdf` | **[T]** (dossier cotisations) |
| **Décret n° 97-291** | Art. 29, 38, 53 | 1997-02-03 | n° 13 | 203-204 | — | `/1997/1997F/Jo01397.pdf` | **[T]** (dossier cotisations) — **à relire pour l'art. 53** |
| **Décret n° 97-555** | Taux de cotisation (art. 9 nouveau : 5,25 %) | 1997-03-31 | n° 27 | 553 | non énoncée | `/1997/1997F/Jo02797.pdf` | **[T]** (dossier cotisations) |
| **Décret n° 97-1927** | Art. 33 (nouveau) : conditions de la pension temporaire d'orphelin | 1997-09-29 | n° 80 du 7 oct. 1997 | 1851 | **non lue** — le second article du décret n'a pas pu être isolé du découpage en colonnes | `/1997/1997F/Jo08097.pdf` | **[T]** (art. 33 nouveau) |
| **Décret n° 2001-779** | **Revalorisation** : art. 53 (nouveau) | 2001-03-29 | n° 28 du 6 avril 2001 | 763-764 | **art. 3 n'énonce pas d'effet ; l'art. 2 fixe l'application transitoire au 1er janvier 2001** | `/2001/2001F/Jo0282001.pdf` | **[T]** |
| **Décret n° 2003-1212** | Quote-part **7,25/20e** | 2003-06-02 | n° 46 | 1834-1835 | art. 2 : 1er janvier 2003 | `/2003/2003F/Jo0462003.pdf` | **[T]** (dossier cotisations) |
| **Décret n° 2007-2148** | Art. 15 bis tirets a) et C) ; art. 17 § 3, 33, 42, 47 (nouveaux) ; **art. 15 ter** (additionnel) | 2007-08-21 | n° 69 du 28 août 2007 | 3070-3071 | **non énoncée** (art. 4 : clause d'exécution) | `/2007/2007F/Jo0692007.pdf` | **[T]** |

**Avertissement méthodologique.** Le dossier des cotisations avait marqué 94-1429, 96-326, 97-291,
2001-779 et 2003-1212 « vérifiés, sans effet sur les taux ». Cette vérification portait sur les
**taux de cotisation** ; elle ne dit rien de la limite de calcul des prestations ni des règles de
liquidation. Les décrets 96-326, 97-291 et 94-1429 **n'ont pas été relus ici sous cet angle** : leur
neutralité sur l'article 18 et sur l'article 17 n'est pas établie (§ 8).

## 2.1 La limite de calcul des prestations — la série demandée

> **Mise à jour du 11 septembre 2026** : le décret n° 94-1429 abroge et remplace les articles 18 et 19 dans leur rédaction de 1990 ; la série de la fenêtre du salaire de référence et les corrections à reporter dans cette section sont au **§ 12** (en particulier § 12.8).

C'est la valeur dont dépend à la fois le plafond du salaire retenu pour la pension légale et,
symétriquement, l'assiette du régime complémentaire (« la fraction de salaire excédant la limite
fixée par le régime légal pour le calcul des prestations », art. 6 du règlement annexé à l'arrêté du
18 novembre 1978).

| Depuis | Valeur | Texte, verbatim | Niv. |
|---|---|---|---|
| **1er janvier 1974** | **six fois le SMIG** rapporté à une durée d'occupation annuelle de **2 400 heures** | 74-499, **art. 18** : « Lesdits salaires ne sont pris en compte pour une année déterminée que dans la limite de **six fois le SMIG** rapporté à une durée d'occupation annuelle de 2 400 heures. » | **[T]** p. 917 |
| **1990** (effet non énoncé) | **six fois le SMIG** rapporté à 2 400 heures, **inchangée** ; s'y ajoute une **actualisation des salaires selon un barème fixé par arrêté du ministre des affaires sociales** | décret n° 90-1455, **art. 18 (nouveau)** : « Lesdits salaires ne sont pris en compte pour une durée déterminée que dans **la limite de 6 fois le SMIG** rapporté à une durée d'occupation annuelle de 2 400 heures. **Ils sont actualisés selon un barème fixé par arrêté du ministre des affaires sociales.** » | **[T]** p. 1358 |

**Conclusion.** La constante « six fois le SMIG » du modèle est **exacte et attestée depuis le
1er janvier 1974**. Ce qui lui manque n'est pas une valeur mais une **date et une référence** : le
décret n° 74-499, art. 18, effet 1er janvier 1974. Aucun texte de la chaîne lue ne l'a modifiée.
Deux décrets de la chaîne restent non relus sous cet angle (96-326, 97-291) et deux rectificatifs
n'ont pas été ouverts : la série est **établie mais non close**.

**Corollaire pour l'issue openfisca-tunisia#399.** L'assiette du régime complémentaire est définie
par renvoi : elle est le **salaire différentiel** au-dessus de cette limite. Elle suit donc
mécaniquement toute évolution du SMIG, sans qu'aucun texte propre au régime complémentaire n'ait à
être modifié.

**État du code, vérifié le 10 septembre 2026.** La limite n'est pas un paramètre : c'est un
**littéral dans la formule**. Dans
`openfisca-tunisia/openfisca_tunisia/variables/prelevements_obligatoires/cotisations_sociales.py`,
les variables `retraite_complementaire_employeur` et `retraite_complementaire_salarie` calculent
toutes deux, à l'identique :

```python
smig = parameters(period.start).marche_travail.smig_48h_mensuel
assiette = individu("assiette_cotisations_sociales", period)
assiette_complementaire = max_(0, assiette - 6 * smig)
```

Trois observations **[D]** :

- le **6** est écrit en dur, sans date ni référence — c'est exactement ce que le ticket décrit ;
- le régime horaire retenu, `smig_48h_mensuel`, est cohérent avec le texte, qui rapporte la limite à
  « une durée d'occupation annuelle de **2 400 heures** » ;
- la formule est correcte quant au fond — l'assiette est bien la seule fraction excédant la limite,
  conformément à l'article 6 du règlement du 18 novembre 1978 —, ce qui **corrige le constat du
  dossier des cotisations** (§ 1.8 de `cotisations-dossier-prive.md`), établi sur le seul fichier de
  paramètres `retraite_complementaire.yaml` : le plafonnement est bien appliqué, mais dans le code
  et non dans les paramètres.

Le travail à faire est donc de **remonter le 6 en paramètre daté**, avec pour référence le décret
n° 74-499, art. 18, effet 1er janvier 1974, et pour confirmation l'article 18 (nouveau) du décret
n° 90-1455.

**Le barème d'actualisation annoncé par l'article 18 (nouveau) de 1990 n'a pas été identifié** :
recherches `LIKE` non accentuées et FTS sur `actualisation`, `bareme` + `salaire`, 1988-2010, sans
résultat concluant. **TODO** (§ 8).

## 2.2 Ouverture du droit

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Âge légal** | **60 ans au moins** | 74-499, **art. 15 a)** | **[T]** p. 916 |
| **Stage requis** | **120 mois** de cotisations effectives ou assimilées | 74-499, **art. 15 b)** | **[T]** |
| Non-cumul | ne pas exercer une activité professionnelle assujettie | 74-499, **art. 15 c)** | **[T]** |
| Dérogation d'âge, travaux pénibles ou insalubres | **55 ans**, par **arrêté du ministre des affaires sociales** fixant les catégories | 74-499, **art. 15**, dernier alinéa | **[T]** |
| Majoration du stage en cas de dérogation | les conditions de stage requises à la date du 55e anniversaire sont majorées des **deux tiers du nombre de mois restant à courir jusqu'à 60 ans** | 74-499, **art. 16** | **[T]** |
| **Stage dérogatoire transitoire** | sont réputés satisfaire à la condition de stage les assurés justifiant, à l'entrée en vigueur, de **96 mois** de cotisations depuis le 1er avril 1961 ; durée majorée de 6 mois par an du 1er janvier 1975 jusqu'à atteindre 120 mois | 74-499, **art. 44** | **[T]** p. 918 |
| Cessation obligatoire du contrat de travail | le droit à pension « oblige à mettre fin aux relations de travail » ; l'accord des parties homologué par l'inspection du travail peut différer l'acquisition du droit | 74-499, **art. 14** ; art. 14 (nouveau) du décret 90-1455 | **[T]** |
| **Entrée en jouissance** | 1er jour du mois suivant celui de la cessation d'activité, de la reconnaissance d'invalidité ou du décès | 74-499, **art. 47** ; art. 47 (nouveau) du décret 2007-2148 | **[T]** |
| Condition de résidence | résider en Tunisie à la date de la demande ; écartée par traité de réciprocité | 74-499, **art. 49** | **[T]** p. 918 |

### Départs anticipés — l'article 15 bis, créé en 1982

**Décret n° 82-1030, art. 1er [T], p. 1606** — insère l'article 15 bis :

> « Nonobstant les dispositions de l'article précédent, le droit à la retraite est ouvert **sans
> conditions d'âge** mais la **jouissance de pension est différée jusqu'à ce que l'intéressé ait
> atteint l'âge de cinquante ans**, et dans les cas suivants :
> a) aux assurés **licenciés pour des raisons économiques** […] le licenciement doit être approuvé
> par la commission de contrôle des licenciements prévue à l'article 21 du code du travail […] et
> l'assuré doit fournir un document attestant qu'il a été inscrit au bureau de l'emploi pendant
> 6 mois au moins et qu'aucun travail ne lui a été proposé ;
> b) aux assurés dont l'activité **cesse prématurément pour usure due aux conditions de travail**
> auxquelles ils ont été soumis durant leur carrière […] ;
> c) aux assurés qui cessent leur activité salariée **pour convenance personnelle** et qui
> justifient d'un **stage minimum de 360 mois** de cotisations validées ;
> d) aux **femmes salariées mères de trois enfants vivants au moins**, et justifiant de **180 mois**
> de cotisations validées. »

C'est donc **le décret n° 82-1030 — et non le décret n° 74-499 — qui fonde l'âge de 50 ans** porté
par le paramètre `retraite.rsna.age_dep_anticip`, et c'est lui qui fonde le **départ anticipé des
mères de trois enfants** du régime privé.

**Décote — art. 17 alinéa 3 (nouveau), même décret [T]** :

> « Pour les assurés qui prennent leur retraite anticipée en application des dispositions de
> l'alinéa c) de l'article 15 bis, le montant de la pension […] est **réduit de 0,5 % par trimestre
> restant à courir entre leur âge lors du départ à la retraite et l'âge de 60 ans**. »

**Évolutions de 2007 — décret n° 2007-2148 [T]**, p. 3070 :

- **art. 15 ter (additionnel)** : « le droit à la retraite est ouvert **sans condition d'âge avec
  jouissance différée de la pension jusqu'à l'âge de cinquante cinq ans** pour les assurés qui
  cessent leur activité salariée pour convenance personnelle et qui justifient d'un **stage minimum
  de 360 mois** de cotisations validées » ;
- **art. 17 troisième paragraphe (nouveau)** : la décote de 0,5 % par trimestre est reportée sur les
  départs de l'article 15 ter, l'écart étant mesuré « entre leur âge lors du départ à la retraite et
  l'âge normal de celle-ci » ;
- l'article 15 bis est réduit : le tiret « C » est abrogé (art. 1er), le tiret « a » est réécrit
  (art. 2). Le tiret « d », relatif aux mères de trois enfants, n'est pas touché.

## 2.3 Calcul

> **Mise à jour du 11 septembre 2026** : le décret n° 94-1429 abroge et remplace les articles 18 et 19 dans leur rédaction de 1990 ; la série de la fenêtre du salaire de référence et les corrections à reporter dans cette section sont au **§ 12** (en particulier § 12.8).

**Taux et plafond — 74-499, art. 17 [T], p. 917** (relu à 500 dpi pour les chiffres) :

> « Le taux de la pension de vieillesse est fixé à **40 %** du salaire moyen de référence tel que
> déterminé à l'article 18 ci-après, lorsque se trouve réalisée la condition de 120 mois de
> cotisation énoncée à l'article 15 b) précédent. Toute fraction de cotisation supérieure à
> 120 mois ouvre droit, par période de 12 mois de cotisation supplémentaire, à une **majoration
> égale à 2 %** dudit salaire moyen de référence **sans que le montant total de la pension puisse
> excéder un maximum de 80 %** dudit salaire. »

**Décret n° 82-1030, art. 4 — art. 17 alinéa 2 (nouveau) [T]** : la majoration passe d'une
expression annuelle à une expression trimestrielle, à taux annuel constant :

> « Toute fraction de cotisation supérieure à 120 mois ouvre droit par **période de 3 mois** de
> cotisation supplémentaire à une **majoration égale à 0,5 %** dudit salaire moyen de référence sans
> que le montant total de la pension puisse **excéder un maximum de 80 %** dudit salaire. »

**Le plafond de 80 % du RSNA est donc sourcé deux fois** : art. 17 du décret 74-499 (1974) et
art. 17 al. 2 (nouveau) du décret 82-1030 (1982). Il est arithmétiquement atteint à 30 ans de
cotisations (40 % + 2 % × 20), soit **120 trimestres** — la borne terminale du barème du modèle.

**Salaire de référence :**

| Depuis | Fenêtre | Texte | Niv. |
|---|---|---|---|
| 1er janv. 1974 | « les salaires soumis à cotisation que l'assuré a perçus au cours des **trois ou cinq dernières années** précédant l'âge d'ouverture du droit […] **selon que l'une ou l'autre de ces périodes de référence est plus avantageuse pour lui** » ; salaire mensuel moyen = total divisé par **36 ou 60** | 74-499, **art. 18 et 19** | **[T]** p. 917 |
| 1990 (effet non énoncé) | « les salaires […] que l'assuré a perçu au cours des **dix dernières années précédant l'âge d'ouverture du droit à pension**. Au cas où la période d'activité déclarée est inférieure à 10 ans, la moyenne est calculée sur la base des salaires perçus au cours de cette période. » | décret n° 90-1455, **art. 18 (nouveau)** | **[T]** p. 1358 |

**Écart avec le modèle, à signaler.** `rsna_salaire_de_reference` calcule la moyenne des **dix
meilleures** années sur quarante (`k = 10`, `make_mean_over_largest`). Le texte de 1990 dit **dix
dernières**. Aucun texte lu n'introduit de sélection des meilleures années au RSNA. De même,
`cnrps_salaire_de_reference` retient la moyenne des **deux plus élevées consécutives** ; l'article 36
de la loi 85-12 vise la **fonction la plus élevée exercée deux ans**, sous condition de trois ans de
retenues — condition non modélisée.

## 2.4 Planchers

**Décret n° 82-1030, art. 5 — art. 45 1er alinéa (nouveau) [T], p. 1606** :

> « Le montant annuel des pensions de vieillesse ou d'invalidité **ne peut être inférieur aux 2/3 du
> SMIG** rapporté à une durée d'occupation annuelle de 2 400 heures. En ce qui concerne **les
> pensions de retraite anticipée et les pensions proportionnelles** liquidées en application de
> l'article 15 bis a) et b) et de l'article 39, le montant à servir **ne peut être inférieur à la
> moitié du SMIG** rapporté à une durée d'occupation de 2 400 heures. »

**C'est là — et nulle part ailleurs — que se trouvent les deux paramètres
`retraite.rsna.pension_minimale.sup` (2/3) et `.inf` (1/2).** Deux conséquences :

1. leur date n'est pas 1974 mais **1982** (le texte de 1974, art. 45, ne connaissait que le plancher
   de 2/3, sans dérogation, et excluait expressément l'allocation de vieillesse) ;
2. **leur description est fausse.** Le critère de partage n'est pas « inférieur / supérieur à la
   durée du stage requis » mais le **type de pension** : pension de vieillesse ou d'invalidité
   normale d'un côté, retraite anticipée et pension proportionnelle de l'autre.

**Le décret n° 79-536, art. 1er [T]** avait auparavant ajouté un alinéa 2 à l'article 45, étendant
le plancher aux pensions liquidées sous les régimes conventionnels préexistants au décret n° 76-981,
« dans le cas où les titulaires ne bénéficient pas d'une pension de vieillesse ou d'invalidité en
application du présent décret ».

**Allocation de vieillesse, puis pension proportionnelle.** Le régime a changé de nature en 1982.

| Période | Dispositif | Texte | Niv. |
|---|---|---|---|
| 1974-1982 | **Allocation de vieillesse** : pour l'assuré remplissant les conditions d'âge et de cessation d'activité mais non la durée de stage (art. 39) ; **60 mois** de cotisation effective au moins (art. 40) ; **versement unique sous forme de capital**, égal, pour toute période de six mois de cotisations, à une mensualité de la pension à laquelle l'assuré aurait ouvert droit (art. 41) ; faculté de convertir le capital en rente (art. 43) ; **exclue du plancher de 2/3 du SMIG** (art. 45 in fine) | 74-499, section 6, **art. 39-43 et 45** | **[T]** p. 918 |
| Depuis 1982 | La section 6 est **abrogée et remplacée** par « **Section 6 de la pension proportionnelle** » : art. 39 (nouveau) champ ; **art. 40 (nouveau) : 60 mois** au moins ; **art. 41 (nouveau)** : montant calculé sur la base de la pension à laquelle l'assuré aurait droit s'il avait accompli le stage minimum, **au prorata du nombre de mois cotisés** ; art. 42 (nouveau) : réversible ; **art. 43 (nouveau) : toute période inférieure à 60 mois donne droit à un versement unique** égal aux retenues salariales effectuées | décret n° 82-1030, **art. 3** | **[T]** p. 1606 |
| 1990 | art. 43 (nouveau) reformulé : « Toute période de cotisation inférieure à 60 mois donne droit à un versement unique dont le montant est égal aux retenues effectuées sur la rémunération de l'assuré au titre des cotisations salariales au régime de pension » ; en cas de décès, versement au conjoint et aux enfants mineurs | décret n° 90-1455, **art. 1er** | **[T]** |

→ **`retraite.rsna.stage_derog` = 5 ans** correspond aux **60 mois** de l'art. 40 (allocation de
vieillesse, puis pension proportionnelle), et non à la disposition transitoire de 96 mois de
l'art. 44. Le rattachement reste **[D]** : aucun texte ne qualifie ces 60 mois de « stage
dérogatoire ».

## 2.5 Droits dérivés

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Réversion, veuve** | **50 %** de la pension de vieillesse ou d'invalidité dont bénéficiait ou aurait dû bénéficier le défunt | 74-499, **art. 31** | **[T]** p. 917 |
| Réversion majorée | « Ce taux est majoré à concurrence de **75 %** […] à condition qu'il n'y ait pas d'enfant bénéficiaire, ou que le total de la pension de veuve et d'orphelin ne dépasse pas le montant de la pension de l'assuré. **En cas de dépassement la pension d'orphelin est réduite d'autant.** » | décret n° 81-188, **art. 2** — art. 31 al. 2 (nouveau et complémentaire) | **[T]** p. 320 |
| Veuf invalide | même droit | 74-499 art. 29 ; art. 29 (nouveau) du décret 81-188 | **[T]** |
| Condition d'antériorité du mariage | le mariage doit avoir été contracté antérieurement à la réalisation de l'invalidité | 74-499, **art. 30** | **[T]** |
| Remariage | suppression de la pension de réversion au 1er jour du trimestre civil suivant | 74-499, **art. 32** ; art. 32 (nouveau) du décret 90-1455 (service revalorisé rétabli en cas de décès du nouveau conjoint ; **cumul de pensions de conjoint survivant au titre de mariages successifs interdit**) | **[T]** |
| **Orphelin** | **20 %**, porté à **30 %** pour les orphelins de père et de mère | 74-499, **art. 34** | **[T]** p. 917 (chiffres relus à 500 dpi ; le second est en limite de lisibilité, mais la rédaction est mot pour mot celle de l'art. 65 de la loi n° 81-6, où « 20 % … porté à 30 % » est net) |
| Orphelin, taux unifié | **30 %** | décret n° 81-188, **art. 1er** — art. 34 (nouveau) | **[T]** p. 320 |
| Conditions d'âge de l'orphelin | 16 ans sans justification ; 21 ans sur justification d'enseignement du second degré ou supérieur, technique ou professionnel ; sans limite d'âge en cas d'affection incurable | 74-499 art. 33 ; art. 33 (nouveau) des décrets 81-188 puis **97-1927** (qui y ajoute **25 ans pour les études supérieures sans bourse** et **la fille tant qu'elle ne dispose pas de ressources ou n'est pas à la charge de son mari**) | **[T]** |
| Conditions d'âge, dernier état | reprise des cinq tirets, avec **suspension définitive** du paiement à la fille dès que l'une des deux conditions fait défaut après l'entrée en vigueur du décret | décret n° 2007-2148, **art. 33 (nouveau)** | **[T]** |
| **Plafond de cumul** | « En aucun cas le montant cumulé des pensions de veuves et d'orphelins ne doit excéder le montant de la pension de référence du mari. Le cas échéant, il est procédé à une réduction temporaire des pensions d'orphelins. » | 74-499, **art. 38** | **[T]** p. 918 |
| Caractère collectif | les pensions d'orphelins sont **collectives** et réduites à mesure que chacun cesse de remplir les conditions | 74-499, **art. 35** | **[T]** |
| Suspension | orphelin pris en charge par une institution publique ou privée bénéficiant de l'aide de l'État | 74-499, **art. 36** | **[T]** |
| Réversibilité des pensions proportionnelles | pensions proportionnelles et pensions des art. 15 bis / 15 ter réversibles dans les conditions de la section 5 | décret n° 2007-2148, **art. 42 (nouveau)** | **[T]** |
| Suspension pour abandon de famille | pension temporaire de **80 %** allouée à l'épouse et aux enfants mineurs pendant la suspension | 74-499, **art. 50** | **[T]** p. 918 |
| Non-cumul invalidité / survivants | interdit ; seule la pension la plus élevée est servie | 74-499, **art. 52** | **[T]** |

## 2.6 Invalidité

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| Définition | invalidité d'origine non professionnelle réduisant des **deux tiers au moins** la capacité de travail ou de gain ; présumée permanente à l'expiration du droit aux indemnités de maladie | 74-499, **art. 20** | **[T]** p. 917 |
| Stage | ne pas avoir atteint l'âge de la vieillesse ; **60 mois** de cotisations dont **6 au cours des 12 mois** précédant la première constatation | 74-499 art. 21 ; **art. 21 b) (nouveau)** du décret 81-188 | **[T]** |
| **Taux** | **40 %** du salaire moyen de référence (1974) → **50 %** | 74-499 art. 22 ; **art. 22 1er alinéa (nouveau)** du décret 81-188 | **[T]** p. 320 |
| Majoration | par période de 3 mois de cotisation au-delà de **180 mois**, **0,5 %**, **maximum 80 %** | décret n° 82-1030, art. 4 — **art. 22 al. 2 (nouveau)** | **[T]** |
| Tierce personne | bonification de **20 %** du montant | 74-499, **art. 23** | **[T]** |
| Conversion | convertie en pension de vieillesse à l'âge requis, bonification pour tierce personne maintenue | 74-499, **art. 24** | **[T]** |
| Contrôle | une fois par an ; **aucune révision après 55 ans** | 74-499, **art. 25** | **[T]** |
| Cumul avec rente d'accident du travail | pension réduite d'un montant égal à la **moitié de la rente**, sans bonification, la réduction ne pouvant excéder la moitié du montant total de la pension | 74-499, **art. 28** | **[T]** |

## 2.7 Revalorisation

Trois états successifs de l'article 53, tous lus.

**a) 1974 — révision discrétionnaire.** 74-499, **art. 53 [T]**, p. 918 :

> « Le montant des pensions en cours de paiement sera **révisé en cas de hausse sensible du niveau
> général des salaires**. La date et les modalités de cette révision seront déterminées par décret. »

Le décret annoncé est le **décret n° 79-510 du 23 mai 1979, portant revalorisation du montant des
pensions de vieillesse, d'invalidité et de survivants dans le secteur privé non agricole**, JORT
n° 36 du 29 mai 1979, pp. 1601-1602, `/1979/1979F/Jo03679.pdf` **[M]** — **non lu**, mais visé par
le décret n° 81-187.

**b) 1981 — indexation automatique sur le SMIG.** Décret n° 81-187, **art. 1er [T]**, p. 319 :

> « **Article 53 (nouveau).** — Le montant des pensions en cours de paiement est **revalorisé
> automatiquement à chaque augmentation du SMIG**. Le montant mensuel des majorations est déterminé
> par référence au montant de l'augmentation du **SMIG horaire rapporté à une durée d'occupation de
> 200 heures par mois** ; pour le calcul des majorations des pensions de vieillesse ou d'invalidité,
> le montant de référence visé à l'alinéa 2 est affecté du **taux de la pension** ; pour le calcul
> des majorations des pensions des veuves et des orphelins il sera tenu compte du taux de la pension
> de vieillesse ou d'invalidité dont bénéficiait ou aurait dû bénéficier le défunt ainsi que du
> **taux de réversion**. »
>
> « **Article 53 bis** (nouveau et additionnel). — Les majorations prévues par l'article 53 ne
> peuvent se cumuler avec les augmentations découlant de l'application des dispositions de
> l'article 45 ci-dessus ; dans le cas où un assuré social a pu ou pourrait bénéficier de
> l'application de l'article 45, l'augmentation découlant de l'article 53 ne serait applicable que
> si elle devrait être **plus élevée**. »
>
> « **Article 53 ter** (nouveau et additionnel). — Les dispositions de l'article 53 s'appliquent aux
> **régimes conventionnels** de pensions de vieillesse, d'invalidité et survivants **transférés à la
> CAVIS** dans le cadre de la fusion prévue par l'article 25 du décret n° 76-981 du 19 novembre
> 1976. »

L'article 2 fixe la revalorisation des pensions liquidées avant l'entrée en vigueur sur un salaire
mensuel de base de **9 D 750** (droit ouvert avant le 1er mai 1979), **6 D 200** (1er mai 1979 -
31 janvier 1980), **4 D 808** (1er février - 30 avril 1980). **Art. 3 : effet au 1er mai 1980.**

**c) 2001 — reformulation.** Décret n° 2001-779, **art. 1er [T]**, p. 763 :

> « **Article 53 (nouveau).** — Le montant des pensions au cours de paiement est **revalorisé
> automatiquement à chaque augmentation du salaire minimum interprofessionnel garanti**. Le montant
> mensuel des majorations est déterminé **proportionnellement à la variation du SMIG horaire
> rapporté à une durée d'occupation de 48 heures par semaine**. Le montant de la majoration est
> calculé en **multipliant le taux de la variation du SMIG par le montant de la pension avant
> l'augmentation**. »

- **Art. 2** : ces règles s'appliquent « à titre transitoire » à l'augmentation du SMIG fixée par le
  décret n° 2000-949 du 11 mai 2000, **à partir du premier janvier 2001** ; les montants en
  découlant sont payés après déduction des majorations déjà dues.
- **Art. 3** : « Le montant de la majoration de la pension est **soumis à une cotisation** suivant
  les taux mis à la charge des travailleurs fixés par l'article 9 du décret n° 74-499 […]. Cette
  cotisation cesse d'être maintenue jusqu'à l'entrée en vigueur de la majoration suivante. »

L'entre-deux — l'**article 53 modifié par le décret n° 97-291** (JORT n° 13/1997, pp. 203-204),
qui touche les articles 29, 38 et 53 — n'a pas été relu ici : le dossier des cotisations l'avait lu
sous l'angle des taux et le qualifiait de « revalorisation, art. 53 nouveau ». **La série 1974 →
1981 → [1997 ?] → 2001 comporte donc un maillon non vérifié** (§ 8).

**Conclusion pour le modèle.** La revalorisation du RSNA est, depuis 1981, une **indexation
automatique et intégrale sur le SMIG**, et depuis 2001 une **application proportionnelle du taux de
variation du SMIG au montant de la pension**. Elle est absente du modèle, paramètre comme code, et
elle est modélisable sans ambiguïté à partir du texte de 2001.

---

# 3. RSA et RSAA — salariés agricoles

## 3.0 Textes pivots

| Texte | Objet | Signature | JORT | Pages | Effet énoncé | URL | Niv. |
|---|---|---|---|---|---|---|---|
| **Loi n° 81-6** | Organise les régimes de sécurité sociale dans le secteur agricole | 1981-02-12 | n° 9 du 13 févr. 1981 | **265-273** | **art. 88 : « La présente loi entrera en vigueur le 1er janvier 1981. »** | `/1981/1981F/Jo00981.pdf` | **[T]** art. 45-88 |
| **Loi n° 81-6 (rectificatif)** | — | 1981-02-12 | n° 26 du 17 avril 1981 | 844 | — | `/1981/1981F/Jo02681.pdf` | **[M]** — **non lu** |
| **Décret n° 81-224** | Répartition des cotisations de sécurité sociale dans le secteur agricole et modalités de versement | **1981-02-24** | n° 13 du 27 févr. 1981 | 425-426 | non lue | `/1981/1981F/Jo01381.pdf` | **[M]** — **non lu** |
| **Loi n° 89-73** | Ajoute à la loi 81-6 un **titre III** : régime agricole amélioré (RSAA) | 1989-09-02 | n° 60, 5-8 sept. 1989 | 1338-1339 | **art. 4 : « La présente loi entrera en vigueur le 1er octobre 1989. »** | `/1989/1989F/Jo06089.pdf` | **[T]** |
| **Loi n° 2007-43**, art. 3-5 | Modifie le § d) de l'art. 64 de la loi 81-6 (fille sans ressources) et supprime le terme « mineur » | 2007-06-25 | n° 51 | 2198-2199 | non énoncée | `/2007/2007F/Jo0512007.pdf` | **[T]** |

**La date conventionnelle du 24 février 1981 est expliquée.** Les sept paramètres RSA du modèle
portent tous la date `1981-02-24`, qui n'est ni la signature de la loi 81-6 (12 février) ni sa
publication (13 février) ni son effet (1er janvier 1981). C'est la **date de signature du décret
n° 81-224**, seul texte de sécurité sociale agricole signé ce jour-là selon `jort_cache.db`. Ce
décret porte sur les **cotisations**, non sur les prestations. La date des paramètres de prestation
est donc **empruntée à un texte étranger à leur objet** ; celle qu'énonce la loi est le
**1er janvier 1981** (art. 88). **[D]** pour l'explication, **[T]** pour la date correcte.

## 3.1 RSA — ouverture du droit

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Âge légal** | **60 ans au moins** | loi 81-6, **art. 48 a)** | **[T]** p. 270 |
| **Stage requis** | **40 trimestres** de cotisations effectives ou assimilées | loi 81-6, **art. 48 b)** | **[T]** |
| Non-cumul | ne pas exercer une activité professionnelle assujettie | loi 81-6, **art. 48 c)** | **[T]** |
| Cessation du contrat | le droit à pension « s'acquiert et oblige à mettre fin aux relations de travail » ; l'accord homologué peut différer | loi 81-6, **art. 47** | **[T]** |
| Entrée en jouissance | 1er jour du mois suivant celui de la cessation d'activité, de la reconnaissance d'invalidité ou du décès | loi 81-6, **art. 75** | **[T]** p. 272 |
| Périodes assimilées | incapacité temporaire indemnisée ; incapacité permanente ≥ 66,66 % ; indemnités journalières maladie, longue durée, maternité ; périodes d'invalidité | loi 81-6, **art. 45** | **[T]** p. 270 |
| **Aucun départ anticipé** | la loi 81-6 ne comporte, dans les articles lus (45 à 88), **aucun dispositif de départ anticipé** : ni équivalent de l'article 15 bis du décret 74-499, ni disposition pour les mères de trois enfants, ni pour les travaux pénibles | — | **[T]** — résultat négatif sur la lecture des pp. 270-273 |

## 3.2 RSA — calcul

**Loi n° 81-6, art. 49 [T], p. 270** :

> « Le taux de la pension de vieillesse est fixé à **40 %** du salaire moyen de référence tel que
> déterminé à l'article 50 ci-après lorsque se trouve réalisée la condition de **40 trimestres** de
> cotisation énoncée à l'article 48 b). Toute fraction de cotisation supérieure à 40 trimestres
> ouvre droit par période d'un trimestre de cotisation supplémentaire à une **majoration égale à
> 0,5 %** dudit salaire moyen de référence **sans que le montant total de la pension puisse excéder
> un maximum de 80 %** dudit salaire. »

→ `rsa.taux_annuite_base` = 0,04, `rsa.taux_annuite_supplementaire` = 0,02, `rsa.stage_requis` = 10,
`rsa.plaf_taux_pension` = 0,8 sont **tous les quatre sourcés par l'article 49**, à la date d'effet du
**1er janvier 1981**.

**Salaire de référence — art. 50 [T], p. 270** :

> « Le salaire annuel moyen de référence est égal au **salaire minimum agricole garanti rapporté à
> une durée de travail de 300 jours par an**, affecté du **coefficient multiplicateur** ayant servi
> de base au calcul des cotisations au cours des **trois ou cinq dernières années précédant l'âge
> d'ouverture du droit** à pension ou allocation **selon que l'une ou l'autre de ces périodes de
> référence est plus avantageuse pour lui**. »

Les coefficients sont ceux de l'article 18 : ouvrier ordinaire 1 ; ouvrier spécialisé 1,5 ; ouvrier
qualifié 2 **[T]** p. 267. La base de cotisation est le **SMAG rapporté à 45 jours par trimestre**
(art. 18) — soit **180 jours par an**, ce qui explique le rapport `300 / 180` codé en dur dans
`rsa_salaire_reference`. Ce rapport est donc **[D] par rapprochement de deux [T]**.

→ Le paramètre `retraite.rsa.periode_remplacement_base = 10` ne correspond à **aucune** valeur du
texte : la fenêtre est de **trois ou cinq années** (art. 50), et 10 est la durée du stage en années
(art. 48 b). Le paramètre paraît dupliquer le stage sous un autre nom.

## 3.3 RSA — planchers

**Rien n'a été trouvé.** Les articles 45 à 88 de la loi 81-6 ont été lus : ils ne comportent
**aucun plancher de pension** pour le régime des salariés agricoles proprement dit. Le seul plancher
agricole lu est celui du **RSAA** (art. 96, § 3.6 ci-dessous), à **la moitié du SMAG**.

→ **Le paramètre `retraite.rsa.pension_min = 0,4 SMAG` n'est appuyé par aucun texte lu.** Il n'est ni
la moitié (RSAA), ni les deux tiers (RSNA), ni le tiers. **TODO** (§ 8).

**Allocation de vieillesse RSA** — subsiste, contrairement au RSNA où elle a disparu en 1982 :

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| Champ | assuré remplissant les conditions d'âge et de cessation d'activité mais non la durée de stage de l'art. 48 | loi 81-6, **art. 70** | **[T]** p. 271 |
| Stage | **20 trimestres** de cotisations effectives au moins | loi 81-6, **art. 71** | **[T]** |
| Forme | **versement unique sous forme de capital**, égal pour toute période de deux trimestres de cotisations à une mensualité de la pension à laquelle l'assuré aurait ouvert droit | loi 81-6, **art. 72** | **[T]** |
| Prescription | un an à compter du 1er jour du mois suivant celui où la condition est remplie | loi 81-6, **art. 73** | **[T]** |
| Disposition transitoire | les assurés justifiant d'une moyenne de cotisation comprise entre un et deux trimestres par an et d'un minimum de **10 trimestres** ont droit à une allocation de vieillesse, équivalente pour chaque période de deux trimestres à une mensualité de la pension du stage complet | loi 81-6, **art. 82** | **[T]** p. 272 |

## 3.4 RSA — droits dérivés

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| **Réversion** | **50 %** de la pension de vieillesse ou d'invalidité | loi 81-6, **art. 62** | **[T]** p. 271 |
| Antériorité du mariage | requise, avant l'ouverture du droit à pension de vieillesse ou d'invalidité | loi 81-6, **art. 61** | **[T]** |
| Pluralité de conjoints | répartition définitive par parts égales | loi 81-6, **art. 62** | **[T]** |
| Remariage | suppression au 1er jour du trimestre civil qui suit | loi 81-6, **art. 63** | **[T]** |
| **Orphelin** | **20 %**, porté à **30 %** pour les orphelins de père et de mère | loi 81-6, **art. 65** | **[T]** |
| Conditions d'âge | 16 ans sans justification ; 21 ans sur justification d'enseignement du second degré, supérieur, technique ou professionnel ; sans limite d'âge en cas d'affection incurable | loi 81-6, **art. 64** | **[T]** |
| Extension | fille sans ressources ou dont l'obligation alimentaire n'incombe pas à son époux, sans limite d'âge ; suppression du terme « mineur » | **loi n° 2007-43, art. 3 et 4** | **[T]** |
| Caractère collectif | pensions d'orphelins collectives et réduites au fur et à mesure | loi 81-6, **art. 66** | **[T]** |
| Suspension | orphelin pris en charge par une institution bénéficiant de l'aide de l'État | loi 81-6, **art. 67** | **[T]** |
| **Plafond de cumul** | « En aucun cas le montant cumulé des pensions de veuves et d'orphelins ne doit excéder le montant de la pension de référence du mari. » | loi 81-6, **art. 69** | **[T]** |
| Suspension pour abandon de famille | pension temporaire de **80 %** à l'épouse et aux enfants mineurs | loi 81-6, **art. 78** | **[T]** p. 272 |
| Non-cumul invalidité / survivants | interdit, seule la plus élevée est servie | loi 81-6, **art. 79** | **[T]** |

## 3.5 RSA — invalidité

| Fait | Valeur | Texte | Niv. |
|---|---|---|---|
| Définition | invalidité d'origine non professionnelle réduisant des **deux tiers au moins** la capacité de travail ou de gain | loi 81-6, **art. 51** | **[T]** p. 270 |
| Stage | **20 trimestres** dont **2 au cours des 12 mois** précédant la première constatation ; aucune condition pour l'accident non professionnel si l'antériorité de l'immatriculation est justifiée | loi 81-6, **art. 52** | **[T]** |
| **Taux** | **40 %** du salaire moyen de référence si 20 trimestres ; majoration de **0,5 %** par trimestre au-delà de 40 trimestres, **maximum 80 %** | loi 81-6, **art. 53** | **[T]** |
| Tierce personne | bonification de **20 %** du montant | loi 81-6, **art. 54** | **[T]** p. 271 |
| Conversion | en pension de vieillesse à l'âge requis, bonification maintenue | loi 81-6, **art. 55** | **[T]** |
| Contrôle | une fois par an ; **aucune révision après 55 ans** | loi 81-6, **art. 56** | **[T]** |
| Cumul avec rente AT | réduction égale à la **moitié de la rente**, plafonnée à la moitié du montant total de la pension | loi 81-6, **art. 59** | **[T]** |

## 3.6 RSA — revalorisation

**Loi n° 81-6, art. 80 [T], p. 272** :

> « Les pensions attribuées en application des articles 47 à 69 précédents sont **révisées lors de
> chaque paiement proportionnellement à la variation du SMAG** par rapport à celui qui a servi au
> calcul du salaire de référence de l'assuré lors de la liquidation initiale de la pension. »

L'indexation du RSA sur le SMAG est donc **de niveau législatif et automatique dès l'origine**, et
plus large que celle du RSNA de 1974 : elle joue « lors de chaque paiement ».

## 3.7 RSAA — régime agricole amélioré

Créé par le **titre III de la loi n° 81-6, ajouté par la loi n° 89-73**, JORT n° 60, pp. 1338-1339.
Article 101 : « Les dispositions des titres I et II de la présente loi s'appliquent aux personnes
visées à l'article 86 **dans la mesure où il n'y est pas dérogé par le présent titre** » **[T]** —
donc l'âge de 60 ans, le stage de 40 trimestres et le barème 40 % + 0,5 %/trimestre plafonné à 80 %
(art. 48-49) valent au RSAA, sauf sur les points suivants.

| Maillon | Règle propre au RSAA | Texte | Niv. |
|---|---|---|---|
| Champ | coopérateurs salariés des entreprises agricoles constituées en société, sociétés de mise en valeur, coopératives ; **tous les salariés des exploitants employant au moins 30 salariés permanents** ; pêcheurs sur bateaux de jauge brute < 30 tonneaux, pêcheurs indépendants et petits armateurs | **art. 86 (nouveau)** | **[T]** |
| Adhésion | doit couvrir l'ensemble des salariés de l'entreprise | art. 87 | **[T]** |
| Ouverture du droit | ne sont pris en considération que les **trimestres de cotisation ayant donné lieu à déclaration d'un salaire au moins égal à 50 fois le SMAG** | **art. 93** | **[T]** p. 1339 |
| **Salaire de référence** | salaires des **trois ou cinq années précédant l'année d'ouverture du droit**, la plus avantageuse | **art. 95** | **[T]** |
| **Limite de calcul** | « dans la limite de **6 fois le salaire minimum agricole garanti** rapporté à une durée d'occupation annuelle de **300 jours** » | **art. 95** | **[T]** |
| **Plancher** | « Le montant annuel des pensions de vieillesse ou d'invalidité **ne peut être inférieur à la moitié du SMAG** rapporté à une durée d'occupation de 300 jours. » | **art. 96** | **[T]** |
| **Revalorisation** | « Le montant des pensions en cours de paiement est **revalorisé automatiquement à chaque augmentation du SMAG**. Le montant mensuel des majorations est déterminé par référence au montant d'augmentation du **SMAG journalier rapporté à une durée d'occupation de 25 jours** » ; pour les pensions de vieillesse ou d'invalidité, le montant de référence est affecté du taux de la pension ; pour les veuves et orphelins, il est tenu compte du taux de la pension du défunt et du taux de réversion | **art. 97** | **[T]** |
| Non-cumul | les majorations de l'art. 97 ne se cumulent pas avec les augmentations de l'art. 96 ; la plus élevée s'applique | **art. 98** | **[T]** |
| Validation | les périodes d'emploi effectif dans le secteur agricole accomplies **depuis le 1er janvier 1981** et non comptées ailleurs peuvent être validées, moyennant versement des cotisations arriérées | **art. 99** | **[T]** |
| Réserve initiale | dotation de **10 millions de dinars** prélevée sur la dotation du régime agricole (art. 7) | art. 100 | **[T]** |
| Renumérotation | l'ancien titre III « Dispositions finales » devient le **titre IV**, les articles 86, 87 et 88 devenant **102, 103 et 104** | loi 89-73, **art. 2** | **[T]** |

**Le modèle ne porte aucun paramètre RSAA** (répertoire `retraite/` : `cnrps`, `rsa`, `rsna`
uniquement) — alors que le dépôt `openfisca-tunisia` en porte pour les **cotisations**.

---

# 4. Les régimes spéciaux

Trois lois, toutes construites sur le même patron : renvoi général à la législation des pensions
civiles et militaires du secteur public, puis conditions particulières.

| Régime | Texte | Signature | JORT | Pages | Effet énoncé | URL | Niv. |
|---|---|---|---|---|---|---|---|
| Membres du gouvernement | **Loi n° 83-31** | 1983-03-17 | n° 23 du 25 mars 1983 | 807-809 | non lue (dernière page non ouverte) | `/1983/1983F/Jo02383.pdf` | **[T]** art. 1-6 |
| Députés | **Loi n° 85-16** | 1985-03-08 | n° 21 du 15 mars 1985 | 375-377 | **aucune clause d'entrée en vigueur** | `/1985/1985F/Jo02185.pdf` | **[T]** art. 1-14 |
| Gouverneurs | **Loi n° 88-16** | 1988-03-17 | n° 20, 22-25 mars 1988 | 427 | **aucune clause d'entrée en vigueur** | `/1988/1988F/Jo02088.pdf` | **[T]** art. 1-9 |

## 4.1 Membres du gouvernement — loi n° 83-31

- **Art. 1er** : « Sont rendues applicables aux membres du Gouvernement les dispositions de la
  législation relative au régime des pensions de retraite des fonctionnaires de l'État, sous réserve
  des conditions particulières prévues par la présente loi. » **[T]**
- **Art. 2 — ouverture du droit** : « après au moins **deux années de fonctions** de Membre du
  Gouvernement ». **[T]**
- **Art. 3 — calcul** : « Le Membre du Gouvernement ayant accompli ses fonctions pendant une période
  de deux ans a droit à une pension de retraite dont le montant est égal à **35 %** de la
  rémunération d'activité servie au membre du Gouvernement à la date de début de jouissance. Pour
  toute période supplémentaire de **6 mois**, le montant de la pension est augmenté d'un montant
  égal à **5 %** de la rémunération d'activité susvisée, **sans que le montant de la pension de
  retraite ne dépasse par rapport à la rémunération d'activité le pourcentage maximum prévu dans le
  régime de retraite des fonctionnaires de l'État**. Les périodes inférieures à 6 mois ne sont pas
  prises en considération. » **[T]**
  → Le plafond est donc **par renvoi** : 80 % avant le 12 septembre 1985, **90 %** ensuite (art. 38
  de la loi 85-12). **[D]**
- **Art. 4 — jouissance** : acquise à la cessation du bénéfice de la rémunération ; **suspendue** en
  cas de nomination à une fonction publique ou d'exercice d'une activité privée lucrative — dans ce
  dernier cas, jouissance à **50 ans**. **[T]**
- **Art. 5** : retenue de **10 %**, contribution de l'État de **15 %** prélevée sur le budget du
  département ministériel concerné, au profit de la CNRPS. **[T]**
- **Art. 6** : période inférieure à 2 ans → remboursement des retenues ; la contribution de l'État
  reste définitivement acquise à la CNRPS. **[T]**

**Le modèle ne comporte aucune variable ni aucun paramètre pour ce régime** : `regimes_speciaux.py`
ne traite que les gouverneurs et les députés.

## 4.2 Députés — loi n° 85-16

- **Art. 1er** : renvoi général à la législation des pensions civiles et militaires du secteur
  public. **[T]**
- **Art. 2 — ouverture du droit** : « acquis après **accomplissement d'une législature complète** ».
  Si la législature n'est pas entièrement accomplie, le droit n'est acquis qu'après
  **deux années au moins** en qualité de député et paiement des contributions de l'article 5 sur la
  période restante. **[T]**
- **Art. 3 — calcul** : **1 législature 30 %** ; **2 législatures 60 %** ; **3 législatures et plus
  90 %** des indemnités parlementaires permanentes. **[T]**
- **Art. 4 — jouissance** : à l'expiration de la législature ; suspendue en cas de réélection, de
  nomination à une fonction publique ou d'activité professionnelle rétribuée — dans ce dernier cas,
  jouissance à **50 ans**. **[T]**
- **Art. 5** : retenue de **10 %** sur les indemnités parlementaires permanentes, contribution de
  l'État de **15 %** prélevée sur le budget de la Chambre des députés. **[T]**
- **Art. 6** : moins de deux années → remboursement des retenues, et application de la législation
  des fonctionnaires. **[T]**
- **Art. 7 — plafond de cumul** : « Le député a droit au cumul de la pension de retraite de député
  aux autres pensions de retraite au titre des années de services accomplis avant ou après
  l'exercice des fonctions de député. Toutefois, **le montant total de la pension ne peut pas
  dépasser le pourcentage maximum prévu à l'article 3** de la présente loi. » **[T]**
- **Art. 8 — revalorisation** : « La pension de retraite des députés […] est **révisée dans les
  mêmes conditions prévues pour les pensions de retraite des fonctionnaires de l'État** » — soit la
  **péréquation** de l'article 37 de la loi 85-12. **[T]**
- **Art. 10** : validation des législatures antérieures (Assemblée constituante, Assemblée
  nationale) et cumul avec la législature 1981-1986. **[T]**
- **Art. 14** : abroge le décret-loi n° 74-22 du 2 novembre 1974 et la loi n° 77-57 du 3 août 1977.
  **[T]**

Le modèle applique `min(législatures × 0,30 ; 0,90)` à l'indemnité annuelle et exige
`legislatures >= 1` : **conforme aux articles 2 et 3**, sauf la voie subsidiaire des deux années.

## 4.3 Gouverneurs — loi n° 88-16

- **Art. 1er** : renvoi général. **[T]**
- **Art. 2 — ouverture du droit** : « après au moins **deux années successives** de fonction de
  gouverneur ». **[T]**
- **Art. 3 — calcul** : « Pour chaque année d'exercice en qualité de gouverneur : **6 %** des
  éléments permanents de la rémunération de gouverneur en nature ou en espèce […] ; pour chaque
  **3 mois** d'exercice : **1,5 %** des éléments permanents. Les périodes inférieures à 3 mois ne
  sont pas prises en considération. » **[T]**
- **Art. 4 — jouissance** : à la cessation du bénéfice de la rémunération ; suspendue en cas de
  nomination à une fonction publique ou d'activité privée rétribuée — jouissance à **50 ans**. **[T]**
- **Art. 5** : retenue **10 %**, contribution de l'État **15 %**. **[T]**
- **Art. 7 — plafond de cumul** : « Toutefois, le montant total de ces pensions ne peut dépasser
  **90 %** des éléments permanents de la rémunération de gouverneur. » **[T]**
- **Art. 8 — revalorisation** : révision dans les mêmes conditions que les pensions des
  fonctionnaires de l'État — **péréquation**. **[T]**
- **Art. 9** : validation des périodes de fonction exercées entre le 21 juin 1956 et la publication
  de la loi. **[T]**

**Nuance à porter au précis.** Le plafond de 90 % appliqué par `gouverneur_pension_brute` est,
dans le texte, un **plafond de cumul** (art. 7), non un plafond de liquidation. La liquidation
elle-même n'en comporte pas : le barème de 6 % par an atteint 90 % à quinze ans d'exercice.

## 4.4 Ce que la loi n° 2007-43 fait aux trois régimes

L'article premier de la loi n° 2007-43 relève les taux de contribution « au régime des pensions
civiles et militaires […] **et aux régimes de retraite des membres du gouvernement, de la chambre
des députés, de la chambre des conseillers et des gouverneurs** » et modifie en conséquence
l'article 5 de la loi 83-31, les articles 9 et 13 de la loi 85-12, l'article 5 de la loi 85-16 et
l'article 5 de la loi 88-16 **[T]**. Les règles de liquidation des trois régimes spéciaux ne sont
pas touchées.

---

# 5. Les régimes que le modèle ignore mais qui ouvrent des droits

Section brève : ce que les textes établissent, sans plus. Aucun de ces régimes n'a de paramètre ni
de variable dans `openfisca-tunisia-pension`.

## 5.1 Travailleurs non salariés (RTNS)

**Décret n° 95-1166 du 3 juillet 1995**, JORT n° 55 du 11 juillet 1995, pp. 1486-1489,
`/1995/1995F/Jo05595.pdf` **[T]** (lu lors du dossier des cotisations).

- **Art. 1er** : étend aux travailleurs non salariés les articles 68 à 98, 100 à 107 et 109 à 120 de
  la loi n° 60-30 **et les articles 20 à 38, 46 à 52, 54 et 57 du décret n° 74-499**. Les règles de
  pension d'**invalidité** (art. 20-28), de **survivants** (art. 29-38) et de liquidation (46-52)
  sont donc celles du RSNA ; les articles **39 à 45 et 53** — pension proportionnelle, plancher,
  **revalorisation** — sont **exclus** du renvoi.
- Cotisation : 14,71 % du revenu de la classe d'affiliation, dont **7 %** pour les pensions **[T]**.
- Chaîne modificative **[M]** : décrets n° 96-1797, 96-2145, 2002-3018, 2004-167, 2008-172.
- **Revalorisation** : un texte propre existe — *Arrêté du ministre des affaires sociales du
  29 juillet 1998, portant revalorisation des pensions de vieillesse, d'invalidité et de survivants
  accordées dans le cadre du régime des travailleurs non salariés*, JORT n° 63 du 7 août 1998,
  pp. 1719-1720, `/1998/1998F/Jo06398.pdf` **[M]** — **non lu**.

## 5.2 Artistes, créateurs et intellectuels (RACI)

**Loi n° 2002-104 du 30 décembre 2002**, JORT n° 106 du 31 décembre 2002, pp. 3187-3190,
`/2002/2002F/Jo1062002.pdf` **[T]**.

- **Art. 1er** : régime spécial comportant « les assurances sociales, **les pensions de vieillesse,
  d'invalidité et de survivants** et les actions sanitaires et sociales ».
- **Art. 7** : cotisation de **11 %** du revenu de la classe, dont **7 % destinés à financer les
  pensions**.
- **Art. 22** : pension temporaire d'orphelin — cinquième tiret modifié par la loi n° 2007-43 **[T]**.
- **Aucune clause d'entrée en vigueur** ; la dernière page a été lue.
- Décret d'application : **décret n° 2003-894 du 21 avril 2003**, JORT n° 34, pp. 1291-1294 **[T]** —
  dix classes de revenu, coefficients 2 à 18 du SMIG.

## 5.3 Tunisiens à l'étranger (RTTE)

**Décret n° 89-107 du 10 janvier 1989**, JORT n° 4 du 17 janvier 1989, pp. 98-99,
`/1989/1989F/Jo00489.pdf` **[T]**.

- **Art. 1er** : étend les articles 68 à 96 et 100 à 120 de la loi n° 60-30 et **les articles 20 à
  38, 46 à 52, 54 et 57 du décret n° 74-499** aux travailleurs tunisiens à l'étranger, salariés ou
  non, non couverts par une convention bilatérale. Même périmètre d'exclusion que le RTNS : les
  articles 39-45 et 53 ne sont pas visés.
- **Art. 3** : adhésion **volontaire**, couvrant obligatoirement les assurances sociales **et** les
  pensions.
- **Art. 6** : quatre classes de revenu forfaitaire, coefficients 2, 4, 6 et 9 du SMIG 48 h rapporté
  à 2 400 heures par an.
- **Art. 7** : cotisation de **10,65 %**, dont **5,25 % destinés à financer le régime des pensions**.
- Gestion du régime de pensions **déléguée à la CAVIS** (art. 2).
- Prorogation du délai de validation : décret n° 91-604 du 30 avril 1991, JORT n° 32, p. 1008 **[M]**.

## 5.4 Travailleurs à bas revenu (loi n° 2002-32)

**Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories
de travailleurs dans les secteurs agricole et non agricole**, JORT n° 22 du 15 mars 2002,
pp. 603-606, `/2002/2002F/Jo0222002.pdf` **[T]** art. 1-21.

- **Art. 1er** — cinq catégories : a) employés de maison ; b) personnes employées par l'État, les
  collectivités locales et les EPA non couvertes par un autre régime ; c) pêcheurs sur bateaux de
  jauge brute ≤ 5 tonneaux, pêcheurs indépendants et petits armateurs ; d) agriculteurs travaillant
  pour leur propre compte exploitant **≤ 5 hectares en sec ou 1 hectare en irrigué** ; e) artisans
  travaillant à la pièce.
- **Art. 2** : droit d'option entre ce régime et le régime de droit commun de la catégorie.
- **Art. 7** : cotisation de **7,5 %**, assise sur les **2/3 du SMAG** (catégories c, d, e) ou les
  **2/3 du SMIG** (catégories a, b), répartie **2/3 employeur, 1/3 salarié**, et supportée
  intégralement par les travailleurs à leur propre compte.
- **Art. 13 — ouverture du droit** : **65 ans au moins** ; **120 mois** de cotisations effectives et
  validées ; ne pas exercer d'activité rémunérée assujettie.
- **Art. 14 — calcul** : « Le montant minimum de la pension de vieillesse est fixé à **30 % du
  salaire minimum garanti du secteur d'appartenance de l'assuré**, en cas de réalisation de la
  condition de 120 mois. Toute fraction de cotisation supérieure à 120 mois ouvre droit, par période
  d'un trimestre de cotisation supplémentaire, à une **majoration égale à 0,5 %** du salaire ayant
  servi pour le calcul des cotisations, **sans que le montant total de la pension puisse excéder un
  maximum de 80 %** dudit salaire. »
- **Art. 16-17 — invalidité** : période de cotisations effectives **≥ 60 mois** ; montant fixé à
  **30 %** du salaire minimum garanti du secteur ; même majoration et même plafond de 80 %.
- **Art. 18** : bonification de **20 %** pour assistance d'une tierce personne.
- **Art. 20** : cumul invalidité / rente d'accident du travail — réduction de la moitié de la rente,
  plafonnée à la moitié du montant total de la pension.
- **Art. 21 et suivants** : pension de survivants. **Art. 25** : pension temporaire d'orphelin,
  cinquième tiret modifié par la loi n° 2007-43, terme « mineur » supprimé **[T]**.
- **Aucune clause d'entrée en vigueur lue** (lecture arrêtée à l'article 21).

## 5.5 Régime complémentaire de retraite

Rappel du dossier des cotisations, utile ici parce qu'il dépend directement de l'article 18 du
décret 74-499 : *Arrêté du ministre des affaires sociales du 18 novembre 1978, portant publication
du règlement d'un régime complémentaire de pension de vieillesse, d'invalidité et de survivants*,
JORT n° 79 du 24 novembre 1978, pp. 3374-3379, `/1978/1978F/Jo07978.pdf` **[T]**. Règlement,
art. 1er : le régime permet « d'acquérir des droits sur la **tranche de salaire dépassant la limite
fixée par ce régime pour le calcul des prestations** » ; art. 6 : « L'assiette de cotisation est la
fraction de salaire excédant la limite fixée par le régime légal pour le calcul des prestations. »
L'arrêté, art. 2 : « Ce règlement entre en application à compter du **1er janvier 1974**. » — la même
date que l'article 64 du décret 74-499.

---

# 6. Récapitulatif : ce que la lecture change pour le modèle

Sans rien modifier, voici les rattachements que la lecture des textes autorise ou impose. Les
paramètres sont ceux de `openfisca_tunisia_pension/parameters/retraite/`.

## 6.1 Paramètres désormais sourcés

Les dix-sept lignes ci-dessous couvrent seize des dix-neuf paramètres que l'audit du 10 septembre
2026 signale **sans référence**, plus un dix-septième — `rsna.bareme_annuite` — qui en portait une,
mais **la mauvaise** (loi n° 60-33 de 1960, alors que le barème est celui du décret n° 74-499). Les
trois paramètres restants de la liste de l'audit sont traités séparément : `rsa.pension_min`
(§ 3.3, non établi), `rsa.periode_remplacement_base` (§ 3.2, sans correspondant dans le texte) et
`cnrps.age_legal.civil.enseignants_du_superieur` (§ 6.1 bis ci-dessous).

| Paramètre | Valeur du modèle | Texte établi | Date d'effet du texte | Date du modèle |
|---|---|---|---|---|
| `rsna.age_legal` | 60 | 74-499, art. 15 a) | 1974-01-01 | 1974-01-01 ✓ |
| `rsna.stage_requis` | 10 ans | 74-499, art. 15 b) (120 mois) | 1974-01-01 | 1974-01-01 ✓ |
| `rsna.age_dep_anticip` | 50 | **82-1030, art. 15 bis** | non énoncée (1982) | 1974-01-01 ✗ |
| `rsna.plaf_taux_pension` | 0,80 | **74-499, art. 17** ; confirmé 82-1030 | 1974-01-01 | 1974-01-01 ✓ |
| `rsna.pension_minimale.sup` | 2/3 SMIG | **82-1030, art. 5** (art. 45 al. 1 nouveau) ; déjà 74-499 art. 45 | 1974 puis 1982 | 1974-01-01 ~ |
| `rsna.pension_minimale.inf` | 1/2 SMIG | **82-1030, art. 5** | non énoncée (1982) | 1974-01-01 ✗ |
| `rsna.stage_derog` | 5 ans | 74-499 art. 40 / 82-1030 art. 40 (nouveau) : 60 mois | 1974 puis 1982 | 1974-01-01 ~ **[D]** |
| `rsna.bareme_annuite` | 1 %/trim puis 0,5 %/trim, 0 au-delà de 120 trim. | **74-499 art. 17**, puis **82-1030 art. 4** | 1974-01-01 | 1960-01-01 ✗ |
| `rsa.age_legal` | 60 | **loi 81-6, art. 48 a)** | **1981-01-01** (art. 88) | 1981-02-24 ✗ |
| `rsa.stage_requis` | 10 ans | **loi 81-6, art. 48 b)** (40 trimestres) | 1981-01-01 | 1981-02-24 ✗ |
| `rsa.taux_annuite_base` | 0,04 | **loi 81-6, art. 49** | 1981-01-01 | 1981-02-24 ✗ |
| `rsa.taux_annuite_supplementaire` | 0,02 | **loi 81-6, art. 49** (0,5 %/trimestre) | 1981-01-01 | 1981-02-24 ✗ |
| `rsa.plaf_taux_pension` | 0,80 | **loi 81-6, art. 49** | 1981-01-01 | 1981-02-24 ✗ |
| `cnrps.duree_de_service_minimale` | 15 ans | **loi 85-12, art. 22** | **1985-09-12** (art. 75) | 1974-01-01 ✗ |
| `cnrps.pension_minimale.minimum_garanti` | 2/3 SMIG | **loi 85-12, art. 39** ; déjà loi 81-70, art. 4 | 1981-05-01 puis 1985-09-12 | 1974-01-01 ✗ |
| `cnrps.pension_minimale.allocation_vieillesse` | 1/2 SMIG | **loi 85-12, art. 42** | 1985-09-12 | 1959-02-01 ✗ |
| `cnrps.pension_minimale.duree_service_allocation_vieillesse` | 5 ans | **loi 85-12, art. 42** | 1985-09-12 | 1974-01-01 ✗ |

## 6.1 bis L'article 29 bis, et le dernier paramètre CNRPS sans référence

`retraite.cnrps.age_legal.civil.enseignants_du_superieur = 65`, daté `2019-04-01`, sans référence.

**Loi n° 2009-20 du 13 avril 2009, portant dispositions exceptionnelles relatives à la retraite des
professeurs de l'enseignement supérieur**, JORT **n° 30 du 14 avril 2009**, **p. 1036**,
`/2009/2009F/Jo0302009.pdf` **[T]** :

- **Art. 1er** : insère l'expression « 29 bis » à l'article 24 de la loi n° 85-12, avant l'expression
  « de cette loi » — c'est-à-dire ajoute le nouveau cas à la liste des dérogations à l'âge de droit
  commun.
- **Art. 2** — texte intégral de l'article ajouté :

  > « **Article 29 bis** — L'âge de mise à la retraite est fixé à **soixante-cinq (65) ans** pour les
  > professeurs de l'enseignement supérieur et les maîtres de conférences de l'enseignement supérieur
  > aux établissements universitaires et aux établissements de recherche scientifique civils et
  > militaires, les professeurs hospitalo-universitaires et les maîtres de conférences agrégés
  > hospitalo-universitaires.
  >
  > Néanmoins, ils peuvent être maintenus en activité **par décret jusqu'à l'âge de soixante-dix (70)
  > ans au maximum**. Le décret visé au deuxième paragraphe du présent article est pris sur la base
  > d'un rapport motivé du ministre concerné. »

- **Aucune clause d'entrée en vigueur** ; le texte s'achève sur « La présente loi sera publiée au
  *Journal officiel* et exécutée comme loi de l'État ».

**Deux conséquences.**

1. Le paramètre est sourcé : **loi n° 2009-20, art. 2 (article 29 bis de la loi 85-12)**. Sa date
   `2019-04-01` est **fausse de dix ans** — signature le 13 avril 2009, publication le 14 avril 2009,
   effet non énoncé. Les dix-neuf paramètres sans référence de l'audit sont désormais tous traités.
2. **L'article 29 bis que la loi n° 2019-37 vise à trois reprises est celui-ci** : son article 1er
   abroge « les paragraphes 2 et 3 de l'article 29 bis » — donc la faculté de maintien par décret
   jusqu'à 70 ans —, et ses articles 5 et 6 permettent aux « agents concernés par l'article 29 bis »
   de repousser leur mise à la retraite « dans la limite de la période qui les sépare de l'âge de
   soixante-dix (70) ans » **[T]**. Le maintien discrétionnaire par décret est ainsi remplacé, en
   2019, par une **option de l'agent**, définitive et irrévocable.

## 6.2 Plafonds de taux de liquidation — la réponse à la question posée

| Régime | Plafond | Texte qui l'énonce | Niv. |
|---|---|---|---|
| CNRPS | **90 %** de la rémunération de liquidation | **loi 85-12, art. 38, dernier alinéa** | **[T]** |
| CNRPS, avant le 12 sept. 1985 | **80 %** de la rémunération globale | **loi 59-18, art. 22 § II (nouveau)** — loi 81-70, art. 4, effet 1er mai 1981 | **[T]** |
| RSNA | **80 %** du salaire moyen de référence | **74-499, art. 17** ; **82-1030, art. 17 al. 2 (nouveau)** | **[T]** |
| RSA / RSAA | **80 %** du salaire moyen de référence | **loi 81-6, art. 49** | **[T]** |
| Loi 2002-32 | **80 %** du salaire de cotisation | **loi 2002-32, art. 14** | **[T]** |
| Députés | **90 %** des indemnités parlementaires (3 législatures) — et plafond de cumul identique | **loi 85-16, art. 3 et 7** | **[T]** |
| Gouverneurs | **90 %** — plafond de **cumul** uniquement | **loi 88-16, art. 7** | **[T]** |
| Membres du gouvernement | par renvoi au régime des fonctionnaires | **loi 83-31, art. 3** | **[T]** |

Les cinq premiers ne sont donc plus « une tranche terminale à taux zéro » : ce sont des plafonds
énoncés en toutes lettres, que le barème d'annuités rencontre par construction.

## 6.3 Fenêtres du salaire de référence — la réponse à la deuxième question posée

| Régime | Fenêtre légale | Texte | Ce que fait le code |
|---|---|---|---|
| CNRPS | **dernière rémunération** ayant supporté des retenues **3 ans** ; ou rémunération de la **fonction la plus élevée exercée 2 ans**, sous condition de 3 ans de retenues | loi 85-12, **art. 36** | dernière rémunération, ou moyenne des **2 plus élevées consécutives** sur demande ; condition de 3 ans absente |
| RSNA | **3 ou 5 dernières années**, la plus avantageuse (1974) → **10 dernières années** (1990) → **5 / 7 / 10 dernières années** aux 1er juillet 1994 / 1995 / 1996 (§ 12) | 74-499 **art. 18-19** ; 90-1455 **art. 18 (nouveau)** ; 94-1429 **art. 18-19 (nouveaux)** | moyenne des **10 meilleures** années sur 40 |
| RSA | **3 ou 5 dernières années**, la plus avantageuse, sur base SMAG × 300 j × coefficient | loi 81-6, **art. 50** | moyenne des **3 meilleures** années, × 300/180 |
| RSAA | **3 ou 5 dernières années**, la plus avantageuse | loi 81-6, **art. 95** | non modélisé |

**Pour les trois régimes du privé — RSNA, RSA, RSAA — le texte parle de *dernières* années, jamais
de *meilleures*.** La seule sélection qu'il prévoie est le choix entre **deux fenêtres** (3 ou 5 ans)
prises l'une et l'autre en fin de carrière, et non le choix des années à l'intérieur d'une fenêtre.
Le code, lui, sélectionne les k meilleures.

**Le CNRPS est un cas distinct, et l'écart y est d'une autre nature.** L'article 36 comporte bien
une branche « la plus avantageuse », mais elle porte sur la **fonction** — « la rémunération
afférente à la fonction la plus élevée effectivement exercée pendant une période minimum de deux
années entières » — et le manuel de la caisse la glose « la situation la plus avantageuse » (p. 83)
**[D]**. C'est un test sur la *fonction occupée*, doublement conditionné (2 ans d'exercice, 3 ans de
retenues) et **subordonné à une demande de l'agent**. Le code applique
`make_mean_over_consecutive_largest(2)`, c'est-à-dire un test sur les *salaires les plus élevés*.
Les deux ne coïncident que si la fonction la plus élevée est aussi celle des deux années les mieux
rémunérées — ce qui est fréquent mais n'est pas la règle posée.

## 6.4 Revalorisation — la réponse à la troisième question posée

| Régime | Mécanisme | Texte |
|---|---|---|
| CNRPS et régimes spéciaux | **péréquation** : la pension suit toute augmentation d'un élément permanent de la rémunération du grade ou de la fonction de liquidation ; cotisée, et depuis 2007 à la charge du retraité | loi 85-12 **art. 37** ; loi 2007-43 **art. 37 (nouveau)** ; loi 85-16 **art. 8** ; loi 88-16 **art. 8** |
| RSNA | révision discrétionnaire par décret (1974) → **indexation automatique sur le SMIG** (1981) → **application proportionnelle du taux de variation du SMIG** (2001) ; la majoration est elle-même cotisée | 74-499 **art. 53** ; 81-187 **art. 53 (nouveau), 53 bis, 53 ter** ; 2001-779 **art. 53 (nouveau)** |
| RSA | **révision à chaque paiement, proportionnellement à la variation du SMAG** | loi 81-6 **art. 80** |
| RSAA | **revalorisation automatique à chaque augmentation du SMAG** | loi 81-6 **art. 97** (loi 89-73) |

## 6.5 Le texte « impossible » est tranché

Le décret « n° 85-611 du 3 juin 1986 » n'existe pas. Le texte réel est le **décret n° 86-611 du
3 juin 1986**, JORT n° 34 des 3-6 juin 1986, p. 674, effet **1er mai 1986** **[T]**. Le millésime
est faux, l'année est bonne. Mais **aucune des quatre valeurs du modèle ne s'y trouve** : voir § 1.7.

## 6.6 Les deux textes cités sans URL vérifiée

| Texte | Statut | URL vérifiée |
|---|---|---|
| **Loi n° 81-70** | **Lue** (art. 4 et 5, p. 1789-1790). Ce n'est pas une loi propre aux indemnités de revenu unique mais une **loi de finances complémentaire pour 1981**, dont l'article 4 remplace huit articles de la loi 59-18 et dont l'article 5 fixe l'effet au **1er mai 1981** | `https://www.pist.tn/jort/1981/1981F/Jo05181.pdf` |
| **Décret n° 85-1178** | **Lu** (art. 1er et 2, p. 1256). Fixe la liste des **fonctions astreignantes** en application de l'**article 28 de la loi 85-12** ; effet **1er juillet 1986**, et non 24 septembre 1985 | `https://www.pist.tn/jort/1985/1985F/Jo06885.pdf` |

Même remarque pour le **décret n° 85-1177** (tâches pénibles et insalubres, art. 27 de la loi 85-12) :
effet **1er juillet 1986**.

---

# 7. Notions à porter au glossaire

| Terme FR | Arabe | Source canonique pressentie |
|---|---|---|
| Péréquation des pensions | إحالة الجرايات / تسوية الجرايات | Loi n° 85-12, art. 37 ; loi n° 2007-43, art. 37 (nouveau) |
| Revalorisation des pensions | تعديل الجرايات | Décret n° 81-187, art. 53 (nouveau) ; décret n° 2001-779 |
| Limite de calcul des prestations | سقف احتساب المنافع | Décret n° 74-499, art. 18 (six fois le SMIG) |
| Salaire moyen de référence | الأجر المتوسط المرجعي | Décret n° 74-499, art. 18-19 ; loi n° 81-6, art. 50 |
| Salaire différentiel | الأجر التفاضلي | Règlement du 18 nov. 1978, art. 6 |
| Taux de liquidation | نسبة تصفية الجراية | Loi n° 85-12, art. 38 ; décret n° 74-499, art. 17 |
| Annuité liquidable | السنة القابلة للتصفية | Loi n° 85-12, art. 35 et 38 |
| Bonification | التمتيع الاستثنائي / الترفيع في المدة | Loi n° 85-12, art. 32-33 |
| Pension proportionnelle | الجراية النسبية | Décret n° 82-1030, art. 3 (section 6 nouvelle) |
| Allocation de vieillesse | منحة الشيخوخة | Loi n° 85-12, art. 42 ; loi n° 81-6, art. 70-73 |
| Pension minimale garantie | الجراية الدنيا المضمونة | Loi n° 85-12, art. 39 ; décret n° 82-1030, art. 5 |
| Pension de réversion | جراية البقاء | Loi n° 85-12, art. 43 ; décret n° 74-499, art. 31 |
| Pension temporaire d'orphelin | الجراية الوقتية لليتيم | Loi n° 85-12, art. 45 ; décret n° 74-499, art. 33 |
| Cadres actifs | الأسلاك النشيطة | Loi n° 85-12, art. 29 |
| Fonctions astreignantes | الوظائف المرهقة | Loi n° 85-12, art. 28 ; décret n° 85-1178 |
| Travaux pénibles et insalubres | الأشغال الشاقة وغير الصحية | Loi n° 85-12, art. 27 ; décret n° 85-1177 |
| Solde de réforme | منحة الإصلاح | Loi n° 85-12, art. 69-71 |
| Jouissance différée | التمتع المؤجل | Loi n° 85-12, art. 41 ; décret n° 82-1030, art. 15 bis |
| Augmentation optionnelle de l'âge de mise à la retraite | الترفيع الاختياري في سن التقاعد | Loi n° 2019-37, art. 71 bis |
| Capital-décès | منحة الوفاة | Décret n° 93-308 |
| Indemnité de revenu unique | منحة الدخل الوحيد | Loi n° 81-70, art. 4 (art. 22 § V nouveau de la loi 59-18) ; loi n° 85-12, art. 40 |
| SMAG | الأجر الفلاحي الأدنى المضمون | Loi n° 81-6, art. 18 et 50 |
| Rente viagère d'invalidité | الإيراد العمري للعجز | Loi n° 59-18 (dispositions maintenues par l'art. 76 de la loi 85-12) |
| Rente compensatrice | الإيراد التعويضي | Lois n° 94-28 et n° 95-56 |
| Éléments permanents de la rémunération | العناصر القارة للأجر | Loi n° 85-12, art. 10 ; décrets n° 85-980 et n° 85-1176 |
| Validation des services | إدماج الخدمات | Loi n° 85-12, art. 14-21 ; loi n° 95-105 |
| Coordination des régimes | التنسيق بين الأنظمة | Loi n° 88-84, puis loi n° 2003-8 et décret n° 2003-1128 |
| Totalisation / proratisation | الجمع / التوزيع النسبي | Loi n° 88-84 |
| Quote-part de pension | حصة الجراية | Loi n° 88-84 ; décret n° 2003-1128 |
| Révision de la pension | مراجعة الجراية | Loi n° 85-12, art. 54 |
| Retraite anticipée volontaire | التقاعد المبكر الاختياري | Loi n° 87-7 |
| Mise à la retraite d'office | الإحالة الوجوبية على التقاعد | Loi n° 85-12, art. 33, 3° ; art. 68 |

---

# 8. Ce qui n'a pas pu être établi

Onze points, dans l'ordre de gravité.

1. **Les trois montants de l'indemnité de revenu unique du modèle (3,125 / 6,250 / 7,825) ne
   viennent d'aucun texte du JORT.** Leur provenance immédiate est établie — la table de la page 94
   du *Manuel de liquidation* de la CNRPS — mais aucun texte ne les fixe. La loi n° 81-70 ouvre le
   droit (art. 22 § V nouveau de la loi 59-18) et fixe la date d'effet — 1er mai 1981 — mais **ne
   fixe aucun montant** : elle renvoie aux « mêmes taux » que la majoration pour salaire unique des
   agents en activité. Recherche menée dans `jort_cache.db`, `titre like '%revenu unique%' or
   '%salaire unique%'` sans filtre d'année, sur 1956-2026 : **un seul résultat**, le décret
   n° 74-463 du 11 avril 1974, propre à certaines catégories de personnels militaires. Les deux
   candidats désignés par le manuel sont les décrets du **2 février 1944** et du **8 juin 1944**,
   antérieurs à l'indépendance et hors du champ de `jort_cache.db`. **Le texte reste à trouver.**

   *(La lacune symétrique sur les indemnités familiales est close : voir § 1.7, décret n° 96-1906
   du 16 octobre 1996.)*

3. **`retraite.rsa.pension_min = 0,4 SMAG` n'est appuyé par aucun texte.** Les articles 45 à 88 de la
   loi n° 81-6 ont été lus intégralement : le RSA n'y comporte **aucun plancher de pension**. Le seul
   plancher agricole lu est celui du RSAA, à la **moitié** du SMAG (art. 96).

4. **Le maillon 1997 de la série de revalorisation du RSNA n'est pas vérifié.** Le décret n° 97-291
   (JORT n° 13/1997, pp. 203-204) modifie les articles 29, 38 **et 53** du décret 74-499. Il a été lu
   lors du dossier des cotisations sous l'angle des taux, non sous celui de la revalorisation. La
   série 1974 → 1981 → **[?]** → 2001 est donc incomplète.

5. **La neutralité des décrets 94-1429, 96-326 et 97-291 sur l'article 18** (limite de calcul des
   prestations et fenêtre du salaire de référence) **n'est pas établie**. Le dossier des cotisations
   les avait vérifiés sur les taux de cotisation seulement. La série de la limite de six fois le
   SMIG est établie sur deux points d'appui (1974 et 1990) mais n'est pas close.
   *(Le décret n° 96-326 est hors de cause : il ne remplace que l'alinéa premier de l'article 46,
   délai de demande de pension — § 11 bis.)*

6. **Le barème d'actualisation des salaires annoncé par l'article 18 (nouveau) du décret n° 90-1455
   n'a pas été identifié.** Le texte renvoie à « un barème fixé par arrêté du ministre des affaires
   sociales ». Recherches `LIKE` non accentuées et FTS sur `actualisation`, `bareme` combiné à
   `salaire`, 1988-2010 : sans résultat exploitable.

7. **Trois rectificatifs n'ont pas été ouverts** : décret n° 74-499 (JORT n° 39/1974, p. 1252),
   décret n° 82-1030 (JORT n° 66/1982, p. 2197), loi n° 81-6 (JORT n° 26/1981, p. 844). Toute
   citation chiffrée des textes initiaux doit être confrontée à son rectificatif.

8. **Le plafond « pension de retraite + rente d'invalidité ≤ 100 % du traitement de référence »
   n'a été trouvé dans aucun texte du JORT.** Il est établi comme **doctrine de la caisse** (manuel
   de liquidation, p. 87), mais la loi n° 85-12 n'en parle pas et son article 76 renvoie l'invalidité
   à la loi n° 59-18, dont les articles 25 à 30 n'ont pas été ouverts. **La formule elle-même est en
   litige** : le manuel écrit rente = pension × taux d'invalidité, l'article 26 § II (nouveau) de la
   loi 59-18 écrit rente = rémunération × taux d'invalidité.

11 bis. ~~Les onze lois de la chaîne modificative de la loi n° 85-12 n'ont pas été ouvertes.~~
   **Résolu le 11 septembre 2026** : les lois n° 87-8, 88-71, 90-6, 94-71, 95-105 (et le décret
   n° 96-1015), 96-67, 97-74, 2001-123 (art. 85-86) et 2002-61 ont été lues, ainsi que trois
   modificatifs absents du manuel (loi n° 97-59, décret-loi n° 2011-48, décret-loi n° 2022-79 art. 12)
   et le décret n° 2023-741 (§ 11). Restent non tranchés : la portée de la loi 95-105 sur l'art. 16
   (nouveau) de 1988 et le décret n° 2003-1656 (§ 11.7). En revanche, restent non ouverts les textes
   de la coordination (lois n° 88-84 et 2003-8, décret
   n° 2003-1128), des textes de départ anticipé (loi n° 2009-39, décret n° 2009-2085 ; la loi
   n° 87-7 a été lue pour sa clause de dérogation, § 11.0) et
   des deux décrets d'assiette (n° 85-980 et n° 85-1176).

9. **Une date d'effet manque au dossier de la loi n° 83-31** (dernière page, p. 809, non ouverte).
   *(Celle du décret n° 97-1927 est établie : art. 2, « prendra effet du 1er mai 1997 », lu à
   l'image — § 11 bis.)*

10. **Le décret n° 81-224 du 24 février 1981** — celui dont la date sert de date conventionnelle à
    tout le bloc RSA du modèle — **n'a pas été lu**. Son intitulé porte sur la répartition des
    cotisations, non sur les prestations ; la vérification reste à faire.

11. ~~La loi n° 88-71 du 27 juin 1988 n'a pas été lue.~~ **Résolu** : elle porte bien de 15 à
    20 ans l'âge des enfants, ajoute la mère d'un enfant handicapé d'un handicap profond et
    subordonne le départ à l'accord du Premier ministre ; effet 1er janvier 1989 (§ 11.1, § 11.3). *(La loi n° 2009-20, en revanche, a été lue : voir § 6.1 bis.)*

---

# 9. Bibliographie — entrées CSL-JSON

Distinguer, avant ajout à `precis/fr/retraites/references.json`, les entrées **déjà présentes** dans
`precis/fr/cotisations_sociales/references.json` (loi 59-18, loi 75-83, loi 85-12, lois 83-31, 85-16,
88-16, loi 2019-37, décret 74-499, décret 94-1429, décret 97-555, décret 2003-1212, décret 95-1166,
loi 2002-104, décret 89-107, arrêté du 18 nov. 1978) de celles **à créer**, ci-dessous.

```json
[
  {"id":"tn-decret-1979-536","type":"legislation","title":"Décret n° 79-536 du 30 mai 1979, portant modification du décret n° 74-499 du 27 avril 1974, relatif au régime de pensions de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1979,5,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"38","page":"1671-1672","URL":"https://www.pist.tn/jort/1979/1979F/Jo03879.pdf","note":"citation-key: tn-decret-1979-536\nJORT n° 38 du 8 juin 1979. Art. 1 : art. 45 al. 2 nouveau. Art. 4 : prend effet à compter du 1er janvier 1979. Texte lu à l'image."},
  {"id":"tn-decret-1979-510","type":"legislation","title":"Décret n° 79-510 du 23 mai 1979, portant revalorisation du montant des pensions de vieillesse, d'invalidité et de survivants dans le secteur privé non agricole","issued":{"date-parts":[[1979,5,23]]},"container-title":"Journal officiel de la République tunisienne","issue":"36","page":"1601-1602","URL":"https://www.pist.tn/jort/1979/1979F/Jo03679.pdf","note":"citation-key: tn-decret-1979-510\nMétadonnées seules ; texte non lu. Visé par le décret n° 81-187."},
  {"id":"tn-decret-1981-187","type":"legislation","title":"Décret n° 81-187 du 14 février 1981, portant revalorisation du montant des pensions de vieillesse, d'invalidité et de survivants dans le secteur privé non agricole","issued":{"date-parts":[[1981,2,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"10","page":"319","URL":"https://www.pist.tn/jort/1981/1981F/Jo01081.pdf","note":"citation-key: tn-decret-1981-187\nJORT n° 10 du 17 février 1981. Art. 1 : articles 53 (nouveau), 53 bis et 53 ter du décret 74-499 — indexation automatique sur le SMIG. Art. 3 : prend effet à partir du 1er mai 1980. Texte lu à l'image."},
  {"id":"tn-decret-1981-188","type":"legislation","title":"Décret n° 81-188 du 14 février 1981, modifiant le décret n° 74-499 du 27 avril 1974, relatif au régime de pensions de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1981,2,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"10","page":"319-320","URL":"https://www.pist.tn/jort/1981/1981F/Jo01081.pdf","note":"citation-key: tn-decret-1981-188\nArt. 21 b), 22 al. 1 (invalidité 50 %), 29, 33, 34 (orphelin 30 %) nouveaux ; art. 31 al. 2 nouveau (réversion majorée à 75 %). Aucune date d'effet énoncée. Texte lu à l'image."},
  {"id":"tn-loi-1981-70","type":"legislation","title":"Loi n° 81-70 du 1er août 1981, modifiant la loi n° 80-88 du 31 décembre 1980, portant loi de finances pour la gestion 1981","issued":{"date-parts":[[1981,8,1]]},"container-title":"Journal officiel de la République tunisienne","issue":"51","page":"1789-1798","URL":"https://www.pist.tn/jort/1981/1981F/Jo05181.pdf","note":"citation-key: tn-loi-1981-70\nJORT n° 51 du 7 août 1981. Art. 4 : remplace les art. 22 § II et V, 26 § II, 31 § I et VI, 32 al. 1, 36, 37, 42 al. 1 de la loi 59-18 — plafond 80 %, plancher 2/3 SMIG, réversion 75 %, indemnité familiale et majoration pour revenu unique. Art. 5 : l'article 4 prend effet à compter du 1er mai 1981. Art. 6 : remplace l'art. 2 de la loi 72-2. Texte lu à l'image."},
  {"id":"tn-loi-1981-6","type":"legislation","title":"Loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole","issued":{"date-parts":[[1981,2,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"9","page":"265-273","URL":"https://www.pist.tn/jort/1981/1981F/Jo00981.pdf","note":"citation-key: tn-loi-1981-6\nJORT n° 9 du 13 février 1981. Chapitre III (art. 45-85) : pensions de vieillesse, d'invalidité et de survivants. Art. 48 (60 ans, 40 trimestres), 49 (40 % + 0,5 %/trimestre, max 80 %), 50 (salaire de référence), 62 (réversion 50 %), 65 (orphelin 20 %, 30 %), 69 (plafond de cumul), 70-73 (allocation de vieillesse), 80 (revalorisation SMAG). Art. 88 : entrée en vigueur le 1er janvier 1981. Rectificatif : JORT n° 26/1981, p. 844. Texte lu à l'image."},
  {"id":"tn-decret-1982-1030","type":"legislation","title":"Décret n° 82-1030 du 15 juillet 1982, modifiant le décret n° 74-499 du 27 avril 1974, relatif au régime des pensions de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1982,7,15]]},"container-title":"Journal officiel de la République tunisienne","issue":"51","page":"1605-1607","URL":"https://www.pist.tn/jort/1982/1982F/Jo05182.pdf","note":"citation-key: tn-decret-1982-1030\nJORT n° 51 des 20-23 juillet 1982. Art. 1 : art. 15 bis (départs anticipés, jouissance à 50 ans) et art. 17 al. 3 (décote 0,5 %/trimestre). Art. 3 : section 6 de la pension proportionnelle (art. 39-43 nouveaux). Art. 4 : art. 17 al. 2 et 22 al. 2 nouveaux (majoration 0,5 %/trimestre, plafond 80 %). Art. 5 : art. 45 al. 1 nouveau (2/3 SMIG ; 1/2 SMIG pour anticipées et proportionnelles). Aucune date d'effet énoncée. Rectificatif : JORT n° 66/1982, p. 2197. Texte lu à l'image."},
  {"id":"tn-decret-1985-1177","type":"legislation","title":"Décret n° 85-1177 du 24 septembre 1985, fixant la liste des catégories d'ouvriers accomplissant des tâches pénibles et insalubres","issued":{"date-parts":[[1985,9,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"68","page":"1255-1256","URL":"https://www.pist.tn/jort/1985/1985F/Jo06885.pdf","note":"citation-key: tn-decret-1985-1177\nJORT n° 68 du 1er octobre 1985. Pris en application de l'article 27 de la loi 85-12 ; dix-sept catégories, retraite à 55 ans. Art. 2 : prend effet à compter du 1er juillet 1986. Texte lu à l'image."},
  {"id":"tn-decret-1985-1178","type":"legislation","title":"Décret n° 85-1178 du 24 septembre 1985, fixant la liste des agents exerçant des fonctions astreignantes","issued":{"date-parts":[[1985,9,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"68","page":"1256","URL":"https://www.pist.tn/jort/1985/1985F/Jo06885.pdf","note":"citation-key: tn-decret-1985-1178\nJORT n° 68 du 1er octobre 1985. Pris en application de l'article 28 de la loi 85-12 ; six corps, retraite après 35 ans de services et 55 ans au moins. Art. 2 : prend effet à compter du 1er juillet 1986. Texte lu à l'image."},
  {"id":"tn-decret-1986-611","type":"legislation","title":"Décret n° 86-611 du 3 juin 1986, portant fixation des taux des indemnités à caractère familial","issued":{"date-parts":[[1986,6,3]]},"container-title":"Journal officiel de la République tunisienne","issue":"34","page":"674","URL":"https://www.pist.tn/jort/1986/1986F/Jo03486.pdf","note":"citation-key: tn-decret-1986-611\nJORT n° 34 des 3-6 juin 1986. Art. 1 : 7,600 / 6,500 / 5,600 / 4,700. Art. 2 : abroge le décret 75-952. Art. 3 : prend effet à compter du 1er mai 1986. Remplace la citation erronée « décret n° 85-611 du 3 juin 1986 ». Texte lu à l'image."},
  {"id":"tn-decret-1988-1136","type":"legislation","title":"Décret n° 88-1136 du 11 juin 1988, portant fixation des taux des indemnités à caractère familial","issued":{"date-parts":[[1988,6,11]]},"container-title":"Journal officiel de la République tunisienne","issue":"43","page":"941","URL":"https://www.pist.tn/jort/1988/1988F/Jo04388.pdf","note":"citation-key: tn-decret-1988-1136\nJORT n° 43 du 24 juin 1988. Art. 1 : 7,600 / 6,500 / 5,600 (trois rangs). Art. 2 : prend effet à compter du 1er janvier 1989. Texte lu à l'image."},
  {"id":"tn-decret-1988-1137","type":"legislation","title":"Décret n° 88-1137 du 11 juin 1988, amendant le décret n° 74-499 du 27 avril 1974, relatif au régime de pensions de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1988,6,11]]},"container-title":"Journal officiel de la République tunisienne","issue":"43","page":"942","URL":"https://www.pist.tn/jort/1988/1988F/Jo04388.pdf","note":"citation-key: tn-decret-1988-1137\nJORT n° 43 du 24 juin 1988. Art. 1 : art. 5 b) nouveau, quote-part de 4,25/20e. Art. 2 : prend effet à partir du 1er janvier 1988. Ce palier manque à la série de quote-part du dossier des cotisations (1,25/20e en 1974 → 7,25/20e en 2003). Texte lu à l'image."},
  {"id":"tn-loi-1989-73","type":"legislation","title":"Loi n° 89-73 du 2 septembre 1989, modifiant et complétant la loi n° 81-6 du 12 février 1981, organisant les régimes de sécurité sociale dans le secteur agricole","issued":{"date-parts":[[1989,9,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"60","page":"1338-1339","URL":"https://www.pist.tn/jort/1989/1989F/Jo06089.pdf","note":"citation-key: tn-loi-1989-73\nJORT n° 60 des 5-8 septembre 1989. Ajoute à la loi 81-6 un titre III (RSAA) : art. 86 (champ), 90 (taux 15 %), 93 (50 fois le SMAG), 95 (salaire de référence, limite de 6 fois le SMAG à 300 jours), 96 (plancher 1/2 SMAG), 97 (revalorisation SMAG), 101 (renvoi aux titres I et II). Art. 4 : entrée en vigueur le 1er octobre 1989. Texte lu à l'image."},
  {"id":"tn-decret-1990-1455","type":"legislation","title":"Décret n° 90-1455 du 10 septembre 1990, amendant le décret n° 74-499 du 27 avril 1974, relatif au régime de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[1990,9,10]]},"container-title":"Journal officiel de la République tunisienne","issue":"60","page":"1358","URL":"https://www.pist.tn/jort/1990/1990F/Jo06090.pdf","note":"citation-key: tn-decret-1990-1455\nJORT n° 60 du 21 septembre 1990. Art. 1 : art. 3, 14, 18, 30, 32, 43 et 54 nouveaux. Art. 18 (nouveau) : salaire de référence sur les dix dernières années ; limite de 6 fois le SMIG à 2 400 heures maintenue ; actualisation par barème d'arrêté du ministre des affaires sociales. Aucune date d'effet énoncée. Texte lu à l'image."},
  {"id":"tn-decret-1997-1927","type":"legislation","title":"Décret n° 97-1927 du 29 septembre 1997, amendant le décret n° 74-499 du 27 avril 1974, relatif au régime de vieillesse, d'invalidité et des survivants dans le secteur non agricole","issued":{"date-parts":[[1997,9,29]]},"container-title":"Journal officiel de la République tunisienne","issue":"80","page":"1851","URL":"https://www.pist.tn/jort/1997/1997F/Jo08097.pdf","note":"citation-key: tn-decret-1997-1927\nJORT n° 80 du 7 octobre 1997. Article premier : art. 33 (nouveau) — pension temporaire d'orphelin, 16 / 21 / 25 ans (études supérieures sans bourse) ; fille sans ressources ; sans limite d'âge en cas d'affection incurable. Date d'effet non lue. Couche texte du fascicule exploitée."},
  {"id":"tn-decret-2001-779","type":"legislation","title":"Décret n° 2001-779 du 29 mars 2001, modifiant et complétant le décret n° 74-499 du 27 avril 1974, relatif au régime de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[2001,3,29]]},"container-title":"Journal officiel de la République tunisienne","issue":"28","page":"763-764","URL":"https://www.pist.tn/jort/2001/2001F/Jo0282001.pdf","note":"citation-key: tn-decret-2001-779\nJORT n° 28 du 6 avril 2001. Article premier : art. 53 (nouveau) — revalorisation automatique proportionnelle à la variation du SMIG horaire rapporté à 48 heures par semaine. Art. 2 : application transitoire à l'augmentation du décret 2000-949, à partir du 1er janvier 2001. Art. 3 : la majoration est soumise à cotisation aux taux de l'article 9. Lu à l'image (couche texte à police décalée)."},
  {"id":"tn-loi-2002-32","type":"legislation","title":"Loi n° 2002-32 du 12 mars 2002, relative au régime de sécurité sociale pour certaines catégories de travailleurs dans les secteurs agricole et non agricole","issued":{"date-parts":[[2002,3,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"22","page":"603-606","URL":"https://www.pist.tn/jort/2002/2002F/Jo0222002.pdf","note":"citation-key: tn-loi-2002-32\nJORT n° 22 du 15 mars 2002. Art. 1 (cinq catégories), 7 (cotisation 7,5 %), 13 (65 ans, 120 mois), 14 (30 % du salaire minimum garanti du secteur, + 0,5 %/trimestre, max 80 %), 16-18 (invalidité), 25 (orphelins). Aucune clause d'entrée en vigueur lue. Lu à l'image (couche texte à police décalée)."},
  {"id":"tn-decret-2007-2148","type":"legislation","title":"Décret n° 2007-2148 du 21 août 2007, modifiant et complétant le décret n° 74-499 du 27 avril 1974, relatif au régime de vieillesse, d'invalidité et de survivants dans le secteur non agricole","issued":{"date-parts":[[2007,8,21]]},"container-title":"Journal officiel de la République tunisienne","issue":"69","page":"3070-3071","URL":"https://www.pist.tn/jort/2007/2007F/Jo0692007.pdf","note":"citation-key: tn-decret-2007-2148\nJORT n° 69 du 28 août 2007. Art. 1-2 : abroge le tiret C de l'art. 15 bis ; remplace le tiret a de l'art. 15 bis, le 3e paragraphe de l'art. 17 (décote 0,5 %/trimestre) et les art. 33, 42 et 47. Art. 3 : art. 15 ter — retraite sans condition d'âge, jouissance différée à 55 ans, stage de 360 mois. Art. 4 : clause d'exécution, aucune date d'effet. Couche texte du fascicule exploitée."},
  {"id":"tn-decret-1981-224","type":"legislation","title":"Décret n° 81-224 du 24 février 1981, fixant la répartition des cotisations de sécurité sociale dans le secteur agricole et réglant les modalités de leur versement","issued":{"date-parts":[[1981,2,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"13","page":"425-426","URL":"https://www.pist.tn/jort/1981/1981F/Jo01381.pdf","note":"citation-key: tn-decret-1981-224\nMétadonnées seules ; texte non lu. Seul texte de sécurité sociale agricole signé le 24 février 1981 : explique la date conventionnelle portée par le bloc RSA du modèle."},
  {"id":"tn-decret-1981-939","type":"legislation","title":"Décret n° 81-939 du 4 juillet 1981, relatif à la revalorisation des pensions de retraite servies par la CNRPS","issued":{"date-parts":[[1981,7,4]]},"container-title":"Journal officiel de la République tunisienne","issue":"47","page":"1630","URL":"https://www.pist.tn/jort/1981/1981F/Jo04781.pdf","note":"citation-key: tn-decret-1981-939\nMétadonnées seules ; texte non lu."},
  {"id":"tn-decret-1982-971","type":"legislation","title":"Décret n° 82-971 du 30 juin 1982, relatif à la revalorisation des pensions de retraite servies par la CNRPS","issued":{"date-parts":[[1982,6,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"48","page":"1496-1497","URL":"https://www.pist.tn/jort/1982/1982F/Jo04882.pdf","note":"citation-key: tn-decret-1982-971\nMétadonnées seules ; texte non lu."},
  {"id":"tn-decret-1983-737","type":"legislation","title":"Décret n° 83-737 du 10 août 1983, relatif à la revalorisation des pensions de retraite servies par la CNRPS","issued":{"date-parts":[[1983,8,10]]},"container-title":"Journal officiel de la République tunisienne","issue":"55","page":"2158-2159","URL":"https://www.pist.tn/jort/1983/1983F/Jo05583.pdf","note":"citation-key: tn-decret-1983-737\nMétadonnées seules ; texte non lu."},
  {"id":"tn-arrete-1998-07-29-revalorisation-rtns","type":"legislation","title":"Arrêté du ministre des affaires sociales du 29 juillet 1998, portant revalorisation des pensions de vieillesse, d'invalidité et de survivants accordées dans le cadre du régime des travailleurs non salariés dans les secteurs agricole et non agricole","issued":{"date-parts":[[1998,7,29]]},"container-title":"Journal officiel de la République tunisienne","issue":"63","page":"1719-1720","URL":"https://www.pist.tn/jort/1998/1998F/Jo06398.pdf","note":"citation-key: tn-arrete-1998-07-29-revalorisation-rtns\nMétadonnées seules ; texte non lu."},
  {"id":"tn-loi-2009-20","type":"legislation","title":"Loi n° 2009-20 du 13 avril 2009, portant dispositions exceptionnelles relatives à la retraite des professeurs de l'enseignement supérieur","issued":{"date-parts":[[2009,4,13]]},"container-title":"Journal officiel de la République tunisienne","issue":"30","page":"1036","URL":"https://www.pist.tn/jort/2009/2009F/Jo0302009.pdf","note":"citation-key: tn-loi-2009-20\nJORT n° 30 du 14 avril 2009. Art. 1 : insère « 29 bis » à l'article 24 de la loi 85-12. Art. 2 : ajoute l'article 29 bis — âge de mise à la retraite fixé à 65 ans pour les professeurs et maîtres de conférences de l'enseignement supérieur et les hospitalo-universitaires ; maintien possible par décret jusqu'à 70 ans, sur rapport motivé du ministre. Aucune clause d'entrée en vigueur. Texte lu (couche texte du fascicule)."},
  {"id":"tn-decret-1996-1906","type":"legislation","title":"Décret n° 96-1906 du 16 octobre 1996, portant fixation des taux des indemnités à caractère familial","issued":{"date-parts":[[1996,10,16]]},"container-title":"Journal officiel de la République tunisienne","issue":"85","page":"2097","URL":"https://www.pist.tn/jort/1996/1996F/Jo08596.pdf","note":"citation-key: tn-decret-1996-1906\nJORT n° 85 du 22 octobre 1996. Art. 1 : 7,320 / 6,507 / 5,693. Art. 2 : 4,880 pour le quatrième enfant ayant acquis le droit avant le 1er janvier 1989. Art. 3 : 4,880 pour l'enfant handicapé au-delà du 3e rang. Art. 4 : abroge les décrets n° 86-611 et n° 88-1136. Art. 5 : prend effet à compter du 1er novembre 1996. C'est le texte des valeurs portées par le modèle, qui les rattache à tort au décret de 1986. Texte lu (couche texte du fascicule)."},
  {"id":"tn-decret-1975-952","type":"legislation","title":"Décret n° 75-952 du 30 décembre 1975, portant fixation du taux des indemnités à caractère familial","issued":{"date-parts":[[1975,12,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"87","page":"2884","URL":"https://www.pist.tn/jort/1975/1975F/Jo08775.pdf","note":"citation-key: tn-decret-1975-952\nMétadonnées seules ; texte non lu. Abrogé par l'article 2 du décret n° 86-611."},
  {"id":"tn-circulaire-1996-42","type":"legislation","title":"Circulaire n° 42 du 25 octobre 1996, ayant pour objet la gestion des indemnités à caractère familial dans le secteur public","issued":{"date-parts":[[1996,10,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"94","page":"2349-2364","URL":"https://www.pist.tn/jort/1996/1996F/Jo09496.pdf","note":"citation-key: tn-circulaire-1996-42\nMétadonnées seules ; texte non lu. Citée par le manuel de la CNRPS comme le texte de gestion des indemnités familiales ; contemporaine du décret n° 96-1906."}
]
```

**Rappel d'outillage** : `scripts/sync_biblio.py` est en lecture seule depuis Zotero. Les clés
ajoutées à la main dans `references.json` seront écrasées au prochain *sync* tant qu'elles ne sont
pas montées dans Zotero. Les vingt-cinq entrées ci-dessus sont donc à porter d'abord dans
`docs/notes/biblio-a-rapatrier.md`.

---

# 10. Le *Manuel de liquidation des pensions & accessoires* de la CNRPS

`/home/benjello/projets/openfisca-tunisia-pension/tmp/manuel pensions.pdf` — 149 pages, dernière
mise à jour du **19 décembre 2013**, couche texte exploitable par `pdftotext -layout`.

**Ce que c'est.** Un document administratif interne de la caisse, non un texte normatif. Tout fait
qui en est tiré reste au niveau **[D]** tant que le texte cité n'a pas été ouvert. Il est
**antérieur à la réforme de 2019** : ses âges, ses taux de contribution et ses règles de mise à la
retraite sont ceux d'avant la loi n° 2019-37.

**Ce qu'il apporte, en trois points.**

1. **Il explique deux anomalies du modèle** — l'origine des montants d'indemnités familiales et
   d'indemnité de revenu unique, et la faute de millésime « 85-611 » : le modèle a recopié le manuel
   (§ 1.7).
2. **Il donne la seule attestation du plafond de 100 % de la rente d'invalidité** (§ 1.5).
3. **Il est une bibliographie toute faite** : sa section « Cadre légal et réglementaire »
   (pp. 5-13) nomme les textes applicables, ce qui permet de cibler les fascicules à ouvrir.

## 10.1 Doctrine de liquidation — ce que le manuel décrit et que la loi ne dit pas

**Formule du régime général** (p. 85) **[D]** :

> PR = (R × TR) + ξ
>
> où R est la rémunération mensuelle de liquidation, TR le taux de la pension « qui ne peut en aucun
> cas dépasser 90 % », et ξ « représente les indemnités familiales, l'indemnité de revenu unique et
> la rente d'invalidité (viagère ou compensatrice) ».
>
> « Soit X = R × TR ; si R × TR ≤ MG alors X = MG ; si R × TR > MG et R × TR ≤ 90 % × R alors
> X = TR × R ; si R × TR > 90 % × R alors X = 90 % × R. »

Trois précisions que le texte de loi ne donne pas :

- **le plafond de 90 % est « l'équivalent de 40 annuités liquidables »** (p. 69) — la caisse traite
  donc le plafond et la borne du barème comme une seule et même chose ;
- **conventions de décompte** : « l'année est égale à 360 jours ; le mois est égal à 30 jours »
  (p. 69) ;
- **quand le produit R × TR tombe au niveau du minimum garanti, « ce produit n'est pas considéré
  comme une pension de retraite mais comme un minimum garanti »** (p. 85) — la distinction a des
  effets sur les accessoires et sur les retenues.

**Salaire de référence** (p. 83) **[D]** — la doctrine confirme et précise l'article 36 :

> « la pension est liquidée sur la base de la **dernière rémunération perçue par l'agent mis à la
> retraite ou décédé en activité**. […] La liquidation de la pension peut également être effectuée
> sur la base des éléments permanents de la rémunération afférente **à la situation la plus
> avantageuse que l'agent avait effectivement exercée pendant une période minimale de 2 ans (sur
> demande)**. »

Deux apports : la règle vaut aussi pour l'**agent décédé en activité**, et la seconde branche est
expressément **subordonnée à une demande** — ce qui justifie la variable booléenne
`cnrps_salaire_de_reference_calcule_sur_demande` du modèle. En revanche le manuel parle, comme la
loi, de la **situation la plus avantageuse exercée deux ans**, et non des deux salaires les plus
élevés que retient le code.

Les **éléments permanents** de la rémunération sont ceux des listes fixées par le **décret n° 85-980
du 11 août 1985** (agents de l'État, collectivités locales et EPA) et le **décret n° 85-1176 du
24 septembre 1985** (agents des EPIC et sociétés nationales), « ainsi que l'ensemble des textes
subséquents » (p. 83) **[D]**.

**Régimes spéciaux** (p. 86) **[D]** : PRS = R × TRS, sans accessoires — « Les bénéficiaires d'une
pension accordée dans le cadre du régime spécial ne peuvent prétendre aux indemnités familiales, à
l'indemnité de revenu unique et à la rente d'invalidité » — et « les régimes spéciaux autorisent le
cumul des pensions sans toutefois excéder **90 % de la rémunération la plus élevée** ». Le manuel
range parmi les régimes spéciaux, depuis 2005, les **membres de la chambre des conseillers**.

**Révision et péréquation** (pp. 139-140) **[D]** — le manuel distingue deux opérations que la loi
traite dans deux articles distincts :

- la **révision** (article 54 de la loi 85-12) : reliquidation pour redresser une erreur ou intégrer
  un élément nouveau — validation de services, régularisation, changement de situation
  administrative, avancement — et pouvant aller jusqu'à la suppression du droit si la concession a
  été faite contrairement à la loi ;
- la **péréquation** (article 37) : « faire bénéficier les pensionnés des mêmes avantages de
  rémunération accordés à leurs homologues en activité […] une reliquidation de la pension pour
  faire intégrer dans celle-ci les valeurs nouvelles des indemnités et primes revalorisées ou
  nouvellement instituées au profit des agents en activité ».

Point opérationnel notable : la péréquation est **automatique pour les indemnités à montant fixe**,
et **subordonnée à la production par le pensionné d'une fiche individuelle de péréquation** pour les
indemnités à montant variable. C'est la première description trouvée du mécanisme concret.

**Coordination des régimes** (pp. 78-82) **[D]** — deux systèmes successifs :

- **Loi n° 88-84 du 16 juillet 1988**, JORT n° 49 du 19 juillet 1988, pp. 1054-1055 **[M]** :
  **totalisation** des périodes pour l'ouverture du droit, **proratisation** pour la liquidation. Une
  pension théorique est calculée sur la totalité des périodes validées auprès de toutes les caisses,
  selon les règles propres à chaque régime, puis chaque caisse en supporte une quote-part ; la
  dernière caisse d'affiliation liquide et paie l'ensemble. Si la somme des quotes-parts est
  inférieure au minimum garanti, **la dernière caisse supporte la différence**. Cinq formulaires de
  liaison organisent l'échange.
- **Loi n° 2003-8 du 21 janvier 2003**, JORT n° 7 du 24 janvier 2003, pp. 195-196 **[M]**, qui
  **abroge totalement** celle de 1988, et **décret n° 2003-1128 du 19 mai 2003**, JORT n° 42 du
  27 mai 2003, pp. 1679-1681 **[M]**, qui institue **trois variantes** : liquidation séparée des
  droits, liquidation par coordination, et une troisième que la lecture n'a pas isolée.

Règle de chevauchement, utile au modèle **[D]** : en cas de périodes superposées, l'ordre de priorité
est « périodes effectives de cotisation ; périodes validées ; périodes assimilées ; périodes
bonifiées », et à catégorie égale, « seule est prise en compte la période correspondant à la
rémunération la plus élevée ».

## 10.2 La chaîne modificative de la loi n° 85-12, nommée par le manuel et résolue dans `jort_cache`

Onze textes nommés par le manuel. **Tous ont été ouverts le 11 septembre 2026** (§ 11, **[T]**) ; la
recherche d'exhaustivité du § 11.0 en ajoute trois que le manuel ignore — **loi n° 97-59** (art. 47),
**décret-loi n° 2011-48** (art. 13) et **décret-loi n° 2022-79, art. 12** (art. 71 bis) — portés en
fin de tableau.

| Texte | Objet (intitulé du JORT) | Signature | JORT | Pages | URL |
|---|---|---|---|---|---|
| **Loi n° 87-8** | Institue des dispositions relatives au **travail des retraités** — **lue** : abroge l'art. 72 (§ 11.1) | 1987-03-06 | n° 18 du 10 mars 1987 | 364 | `/1987/1987F/Jo01887.pdf` |
| **Loi n° 88-71** | Modifie et complète la loi n° 85-12 — **lue** : art. 5, 6, 16, 24, 33, 41, 61 remplacés ou complétés, 25-26 abrogés ; effet 1er janv. 1989 (§ 11.1) | 1988-06-27 | n° 45 du 1er juill. 1988 | 967-968 | `/1988/1988F/Jo04588.pdf` |
| **Loi n° 90-6** | Modifie la loi n° 85-12 — **lue** : art. 6, dernier alinéa (§ 11.1) | 1990-02-12 | n° 14 des 20-23 févr. 1990 | 264 | `/1990/1990F/Jo01490.pdf` |
| **Loi n° 94-71** | Révision des taux de contribution aux régimes de retraite du secteur public — **lue** : art. 9 et 13 (§ 11.1) | 1994-06-27 | n° 50 du 28 juin 1994 | 1086 | `/1994/1994F/Jo05094.pdf` |
| **Loi n° 95-105** | Institue un **système unique de validation des services** au titre des régimes légaux de vieillesse, d'invalidité et de survivants — **lue** : aucun article de la loi 85-12 visé ; abrogation implicite des art. 14-21 (§ 11.1) | 1995-12-14 | n° 101 du 19 déc. 1995 | 2308 | `/1995/1995F/Jo10195.pdf` |
| **Loi n° 96-67** | Modifie la loi n° 85-12 — **lue** : art. 48 (§ 11.1) | 1996-07-22 | n° 60 du 26 juill. 1996 | 1604 | `/1996/1996F/Jo06096.pdf` |
| **Loi n° 97-74** | Amende la loi n° 85-12 — **lue** : art. 42, al. 3 (§ 11.1) | 1997-11-18 | n° 93 du 21 nov. 1997 | 2080 | `/1997/1997F/Jo09397.pdf` |
| **Loi n° 2001-123** | Loi de finances pour 2002 — **lue** : art. 85 (art. 9 et 13) et art. 86 (art. 37) ; art. 97, effet 1er janv. 2002 (§ 11.1) | 2001-12-28 | n° 104 du 28 déc. 2001 | 4260-4261 | `/2001/2001F/Jo1042001.pdf` |
| **Loi n° 2002-61** | Dispositions relatives à la protection sociale au profit de certains agents des entreprises et établissements publics à caractère non administratif — **lue** : art. 5 (2° d), 6 (§ 2), 33 (§ 3), 41 (1° c) (§ 11.1) | 2002-07-09 | n° 57 du 12 juill. 2002 | 1584-1585 | `/2002/2002F/Jo0572002.pdf` |
| **Loi n° 2007-43** | Voir § 1.0 — **lue** | 2007-06-25 | n° 51 | 2198-2199 | `/2007/2007F/Jo0512007.pdf` |
| **Loi n° 2009-20** | Dispositions exceptionnelles, retraite des professeurs de l'enseignement supérieur — lue (§ 6.1 bis) | 2009-04-13 | n° 30 du 14 avril 2009 | 1036 | `/2009/2009F/Jo0302009.pdf` |
| **Loi n° 97-59** *(absente du manuel)* | Amende la loi n° 85-12 — **lue** : art. 47, al. 3 ; effet 1er mai 1997 (§ 11.1) | 1997-07-28 | n° 61 du 1er août 1997 | 1359 | `/1997/1997F/Jo06197.pdf` |
| **Décret-loi n° 2011-48** *(absent du manuel)* | Relève la contribution employeur — **lu** : art. 13, + 1 % au 1er juill. 2011 (§ 11.1) | 2011-06-04 | n° 41 du 7 juin 2011 | 844 | `/2011/2011F/Jo0412011.pdf` |
| **Décret-loi n° 2022-79**, art. 12 *(postérieur au manuel)* | LF 2023 — **lu** : art. 71 bis remplacé ; effet 1er janv. 2023 (§ 11.2) | 2022-12-22 | n° 141 du 23 déc. 2022, **édition arabe seule** | 4060 (arabe) | `/2022/2022A/Ja1412022.pdf` |

**Deux textes de la loi n° 95-105 forment un couple** : la loi et son **décret n° 96-1015 du 27 mai
1996, fixant les modalités de la validation des services au titre des régimes de retraite,
d'invalidité et de survivants**, JORT n° 45 du 4 juin 1996, pp. 1109-1110 — **lu** (§ 11.1) **[T]**. La validation est
traitée par les articles 14 à 21 de la loi 85-12 (**[T]**, p. 360) : validation sur demande écrite
dans un délai maximum d'un an à partir de l'âge légal ; assiette constituée de la moyenne entre ce
que percevait l'agent à la date d'adhésion et ce qu'il percevait à la date de la demande ;
contributions à la charge de l'agent, payables par tranches n'excédant pas 20 % de la rémunération.

## 10.3 Autres textes nommés par le manuel, à ouvrir

**Affiliation** **[M]** :

- **Décret n° 85-1025 du 29 août 1985, fixant la liste des établissements publics à caractère
  industriel et commercial et des sociétés nationales** dont les personnels sont affiliés à la
  CNRPS, JORT n° 62 du 6 septembre 1985, p. 1095, `/1985/1985F/Jo06285.pdf`. C'est le texte que
  demande l'ébauche du chapitre (« lister les sociétés nationales »).
- **Loi n° 98-37 du 25 mai 1998**, portant transfert de la caisse de retraite et de la caisse de
  prévoyance sociale du personnel des services publics de l'électricité, du gaz et des transports à
  la CNRPS, JORT n° 43 du 29 mai 1998, p. 1170, `/1998/1998F/Jo04398.pdf` ; et **décret n° 98-1981
  du 12 octobre 1998**. C'est la disparition de l'**ex-CREGT**, dont le manuel traite les pensions
  aux pages 142-145 — et dont l'ébauche du chapitre signale l'origine en 1948.

**Assiette des contributions** **[M]** : décret n° 85-980 du 11 août 1985 (JORT n° 59 du 16 août
1985, pp. 1030-1033) ; décret n° 85-1176 du 24 septembre 1985 (JORT n° 68 du 1er octobre 1985,
pp. 1254-1255) — même fascicule que les décrets n° 85-1177 et 85-1178.

**Départs anticipés et dispositions particulières** **[M]** :

- **Loi n° 87-7 du 6 mars 1987, instituant un système de retraite anticipée volontaire**, JORT n° 18
  du 10 mars 1987, pp. 363-364, `/1987/1987F/Jo01887.pdf`, et **décret n° 87-337 du 6 mars 1987**
  (critères de priorité, programmes de remplacement) ;
- **Loi n° 2009-39 du 8 juillet 2009, portant mise à la retraite avant l'âge légal**, JORT n° 55 du
  10 juillet 2009, p. 1821, `/2009/2009F/Jo0552009.pdf`, et **décret n° 2009-2085 du 8 juillet
  2009** (procédures et modalités). L'article 7 de la loi n° 2019-37 réserve expressément ces
  programmes : « Les dispositions de la présente loi ne s'appliquent pas aux programmes de la mise à
  la retraite avant l'âge légal et au départ volontaire, qui demeurent régis, concernant l'âge légal
  de la mise à la retraite, aux textes juridiques en vigueur à leur date » **[T]** ;
- **Loi n° 2002-61 du 9 juillet 2002** et **décret n° 2003-1656 du 4 août 2003**.

**Cadres actifs — les décrets de classement « en partie active »**, que la loi 85-12 annonce à son
article 29 sans les nommer **[M]** : décrets n° 67-282 du 26 août 1967 (emplois du secrétariat
d'État à l'intérieur), n° 69-167 du 8 mai 1969 (grades et emplois de la SNCFT), n° 81-1600 du
24 novembre 1981 (ministère du Plan et des Finances), n° 84-748, 84-750, 84-753 et 84-755 du
30 avril 1984 (sûreté nationale et police nationale, garde nationale, prisons et rééducation,
protection civile), n° 88-2131 du 21 décembre 1988 (sécurité du chef de l'État). C'est cette liste
que le paramètre `cnrps.age_legal.civil.cadres_actifs` documente aujourd'hui de mémoire.

**Régimes spéciaux — deux textes que le dossier ignorait** **[M]** :

- **Loi n° 88-101 du 18 août 1988, relative à la retraite des membres de la chambre des députés**,
  JORT n° 55 du 19 août 1988, p. 1156, `/1988/1988F/Jo05588.pdf` ;
- **Loi n° 2005-54 du 18 juillet 2005, étendant les régimes spéciaux applicables aux membres de la
  chambre des députés aux membres de la chambre des conseillers**, JORT n° 57 du 19 juillet 2005,
  p. 1749, `/2005/2005F/Jo0572005.pdf` ;
- ainsi que la **loi n° 88-145 du 31 décembre 1988 (LF 1989), articles 72 à 74**, citée par le
  manuel au titre des régimes spéciaux.

**Capital-décès** **[M]** : le manuel ajoute un texte antérieur au décret n° 93-308 —
**décret n° 74-572 du 22 mai 1974, relatif au capital-décès**, JORT n° 36 du 24 mai 1974,
pp. 1108-1109, `/1974/1974F/Jo03674.pdf` — applicable aux affiliés décédés avant le 1er juillet 1993.
Cette date de bascule, énoncée par le manuel, ne coïncide pas avec la date `1993-02-01` que portent
les paramètres `capital_deces` du modèle. **[D]** — à trancher sur l'article final du décret 93-308,
non lu.

## 10.4 Entrées CSL-JSON supplémentaires

```json
[
  {"id":"cnrps-manuel-liquidation-2013","type":"report","title":"Manuel de liquidation des pensions & accessoires","author":[{"literal":"Caisse nationale de retraite et de prévoyance sociale"}],"issued":{"date-parts":[[2013,12,19]]},"publisher":"Caisse nationale de retraite et de prévoyance sociale","number-of-pages":"149","note":"citation-key: cnrps-manuel-liquidation-2013\nDocument administratif interne, non normatif ; antérieur à la réforme de 2019. Exemplaire local : openfisca-tunisia-pension/tmp/manuel pensions.pdf. Sections utilisées : cadre légal (pp. 5-13), taux de la pension (p. 69), coordination (pp. 78-82), rémunération de liquidation (pp. 83-86), rente d'invalidité (pp. 87-89), accessoires (pp. 90-95), capital-décès (pp. 96-111), révision et péréquation (pp. 139-140), ex-CREGT (pp. 142-145)."},
  {"id":"tn-loi-1988-39","type":"legislation","title":"Loi n° 88-39 du 6 mai 1988, relative à l'octroi des indemnités familiales dans le secteur public","issued":{"date-parts":[[1988,5,6]]},"container-title":"Journal officiel de la République tunisienne","issue":"33","page":"735","URL":"https://www.pist.tn/jort/1988/1988F/Jo03388.pdf","note":"citation-key: tn-loi-1988-39\nMétadonnées seules. Limite aux trois premiers enfants le droit à l'indemnité familiale, à compter du 1er janvier 1989 selon la doctrine de la CNRPS."},
  {"id":"tn-loi-1988-84","type":"legislation","title":"Loi n° 88-84 du 16 juillet 1988, portant coordination des droits des personnes couvertes par plusieurs régimes légaux d'assurance vieillesse, d'invalidité et de survivants","issued":{"date-parts":[[1988,7,16]]},"container-title":"Journal officiel de la République tunisienne","issue":"49","page":"1054-1055","URL":"https://www.pist.tn/jort/1988/1988F/Jo04988.pdf","note":"citation-key: tn-loi-1988-84\nMétadonnées seules. Totalisation-proratisation ; abrogée par la loi n° 2003-8."},
  {"id":"tn-loi-2003-8","type":"legislation","title":"Loi n° 2003-8 du 21 janvier 2003, portant liquidation des droits des personnes bénéficiant de la couverture de plusieurs régimes légaux d'assurance vieillesse, d'invalidité et de décès","issued":{"date-parts":[[2003,1,21]]},"container-title":"Journal officiel de la République tunisienne","issue":"7","page":"195-196","URL":"https://www.pist.tn/jort/2003/2003F/Jo0072003.pdf","note":"citation-key: tn-loi-2003-8\nMétadonnées seules. Abroge la loi n° 88-84 ; trois variantes de coordination définies par le décret n° 2003-1128."},
  {"id":"tn-decret-2003-1128","type":"legislation","title":"Décret n° 2003-1128 du 19 mai 2003, fixant les modalités de liquidation des droits des personnes bénéficiant de la couverture de plusieurs régimes légaux d'assurance vieillesse, d'invalidité et de décès","issued":{"date-parts":[[2003,5,19]]},"container-title":"Journal officiel de la République tunisienne","issue":"42","page":"1679-1681","URL":"https://www.pist.tn/jort/2003/2003F/Jo0422003.pdf","note":"citation-key: tn-decret-2003-1128\nMétadonnées seules."},
  {"id":"tn-loi-1995-105","type":"legislation","title":"Loi n° 95-105 du 14 décembre 1995, portant institution d'un système unique de validation des services au titre des régimes légaux de vieillesse, d'invalidité et de survivants","issued":{"date-parts":[[1995,12,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"101","page":"2308","URL":"https://www.pist.tn/jort/1995/1995F/Jo10195.pdf","note":"citation-key: tn-loi-1995-105\nMétadonnées seules. Décret d'application n° 96-1015 du 27 mai 1996, JORT n° 45, pp. 1109-1110."},
  {"id":"tn-loi-1987-7","type":"legislation","title":"Loi n° 87-7 du 6 mars 1987, instituant un système de retraite anticipée volontaire","issued":{"date-parts":[[1987,3,6]]},"container-title":"Journal officiel de la République tunisienne","issue":"18","page":"363-364","URL":"https://www.pist.tn/jort/1987/1987F/Jo01887.pdf","note":"citation-key: tn-loi-1987-7\nMétadonnées seules. Décret d'application n° 87-337 du 6 mars 1987."},
  {"id":"tn-loi-1987-8","type":"legislation","title":"Loi n° 87-8 du 6 mars 1987, instituant des dispositions relatives au travail des retraités","issued":{"date-parts":[[1987,3,6]]},"container-title":"Journal officiel de la République tunisienne","issue":"18","page":"364","URL":"https://www.pist.tn/jort/1987/1987F/Jo01887.pdf","note":"citation-key: tn-loi-1987-8\nMétadonnées seules. Décret n° 87-338 du 6 mars 1987 : travaux occasionnels pouvant être exercés par les retraités dans le secteur public."},
  {"id":"tn-loi-2009-39","type":"legislation","title":"Loi n° 2009-39 du 8 juillet 2009, portant mise à la retraite avant l'âge légal","issued":{"date-parts":[[2009,7,8]]},"container-title":"Journal officiel de la République tunisienne","issue":"55","page":"1821","URL":"https://www.pist.tn/jort/2009/2009F/Jo0552009.pdf","note":"citation-key: tn-loi-2009-39\nMétadonnées seules. Décret d'application n° 2009-2085 du 8 juillet 2009. Expressément réservée par l'article 7 de la loi n° 2019-37."},
  {"id":"tn-loi-2005-54","type":"legislation","title":"Loi n° 2005-54 du 18 juillet 2005, étendant les régimes spéciaux applicables aux membres de la chambre des députés aux membres de la chambre des conseillers","issued":{"date-parts":[[2005,7,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"57","page":"1749","URL":"https://www.pist.tn/jort/2005/2005F/Jo0572005.pdf","note":"citation-key: tn-loi-2005-54\nMétadonnées seules."},
  {"id":"tn-loi-1988-101","type":"legislation","title":"Loi n° 88-101 du 18 août 1988, relative à la retraite des membres de la chambre des députés","issued":{"date-parts":[[1988,8,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"55","page":"1156","URL":"https://www.pist.tn/jort/1988/1988F/Jo05588.pdf","note":"citation-key: tn-loi-1988-101\nMétadonnées seules."},
  {"id":"tn-decret-1985-1025","type":"legislation","title":"Décret n° 85-1025 du 29 août 1985, fixant la liste des établissements publics à caractère industriel et commercial et des sociétés nationales dont les personnels sont affiliés à la Caisse nationale de retraite et de prévoyance sociale","issued":{"date-parts":[[1985,8,29]]},"container-title":"Journal officiel de la République tunisienne","issue":"62","page":"1095","URL":"https://www.pist.tn/jort/1985/1985F/Jo06285.pdf","note":"citation-key: tn-decret-1985-1025\nMétadonnées seules. Texte demandé par l'ébauche du chapitre CNRPS pour lister les sociétés nationales affiliées."},
  {"id":"tn-decret-1985-980","type":"legislation","title":"Décret n° 85-980 du 11 août 1985, fixant la liste des éléments permanents de la rémunération des agents de l'État, des collectivités publiques locales et des établissements publics à caractère administratif, soumis à retenue pour la retraite","issued":{"date-parts":[[1985,8,11]]},"container-title":"Journal officiel de la République tunisienne","issue":"59","page":"1030-1033","URL":"https://www.pist.tn/jort/1985/1985F/Jo05985.pdf","note":"citation-key: tn-decret-1985-980\nMétadonnées seules. Assiette de liquidation de la pension (art. 10 et 36 de la loi 85-12)."},
  {"id":"tn-decret-1985-1176","type":"legislation","title":"Décret n° 85-1176 du 24 septembre 1985, fixant la liste des éléments permanents de la rémunération des agents des établissements publics à caractère industriel et commercial et des sociétés nationales affiliés à la Caisse nationale de retraite et de prévoyance sociale","issued":{"date-parts":[[1985,9,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"68","page":"1254-1255","URL":"https://www.pist.tn/jort/1985/1985F/Jo06885.pdf","note":"citation-key: tn-decret-1985-1176\nMétadonnées seules. Même fascicule que les décrets n° 85-1177 et 85-1178."},
  {"id":"tn-loi-1998-37","type":"legislation","title":"Loi n° 98-37 du 25 mai 1998, portant transfert de la caisse de retraite et de la caisse de prévoyance sociale du personnel des services publics de l'électricité, du gaz et des transports à la Caisse nationale de retraite et de prévoyance sociale","issued":{"date-parts":[[1998,5,25]]},"container-title":"Journal officiel de la République tunisienne","issue":"43","page":"1170","URL":"https://www.pist.tn/jort/1998/1998F/Jo04398.pdf","note":"citation-key: tn-loi-1998-37\nMétadonnées seules. Décret d'application n° 98-1981 du 12 octobre 1998. Disparition de l'ex-CREGT, dont le manuel de la CNRPS traite les pensions aux pages 142-145."},
  {"id":"tn-decret-1974-572","type":"legislation","title":"Décret n° 74-572 du 22 mai 1974, relatif au capital-décès","issued":{"date-parts":[[1974,5,22]]},"container-title":"Journal officiel de la République tunisienne","issue":"36","page":"1108-1109","URL":"https://www.pist.tn/jort/1974/1974F/Jo03674.pdf","note":"citation-key: tn-decret-1974-572\nMétadonnées seules. Régime applicable aux affiliés décédés avant le 1er juillet 1993 selon la doctrine de la CNRPS ; à confronter à la date 1993-02-01 portée par les paramètres du modèle."},
  {"id":"tn-loi-1988-71","type":"legislation","title":"Loi n° 88-71 du 27 juin 1988, modifiant et complétant la loi n° 85-12 du 5 mars 1985, portant régime des pensions civiles et militaires de retraite et des survivants dans le secteur public","issued":{"date-parts":[[1988,6,27]]},"container-title":"Journal officiel de la République tunisienne","issue":"45","page":"967-968","URL":"https://www.pist.tn/jort/1988/1988F/Jo04588.pdf","note":"citation-key: tn-loi-1988-71\nMétadonnées seules. Porte de 15 à 20 ans l'âge des enfants ouvrant droit au départ anticipé des mères de trois enfants (art. 5 de la loi 85-12) selon la référence du modèle ; à vérifier sur le texte. Circulaire d'application du Premier ministre n° 70 du 2 septembre 1988."},
  {"id":"tn-loi-1990-6","type":"legislation","title":"Loi n° 90-6 du 12 février 1990, modifiant la loi n° 85-12 du 5 mars 1985, fixant le régime des pensions civiles et militaires de retraite et des survivants dans le secteur public","issued":{"date-parts":[[1990,2,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"14","page":"264","URL":"https://www.pist.tn/jort/1990/1990F/Jo01490.pdf","note":"citation-key: tn-loi-1990-6\nMétadonnées seules."},
  {"id":"tn-loi-1996-67","type":"legislation","title":"Loi n° 96-67 du 22 juillet 1996, relative à la modification de la loi n° 85-12 du 5 mars 1985, portant régime des pensions civiles et militaires de retraite et des survivants dans le secteur public","issued":{"date-parts":[[1996,7,22]]},"container-title":"Journal officiel de la République tunisienne","issue":"60","page":"1604","URL":"https://www.pist.tn/jort/1996/1996F/Jo06096.pdf","note":"citation-key: tn-loi-1996-67\nMétadonnées seules. Attention : une autre loi n° 96-67, du 29 juillet 1996, porte ratification d'un accord d'investissement — homonymie à ne pas confondre."},
  {"id":"tn-loi-1997-74","type":"legislation","title":"Loi n° 97-74 du 18 novembre 1997, amendant la loi n° 85-12 du 5 mars 1985, portant régime des pensions civiles et militaires de retraite et des survivants dans le secteur public","issued":{"date-parts":[[1997,11,18]]},"container-title":"Journal officiel de la République tunisienne","issue":"93","page":"2080","URL":"https://www.pist.tn/jort/1997/1997F/Jo09397.pdf","note":"citation-key: tn-loi-1997-74\nMétadonnées seules."},
  {"id":"tn-loi-2002-61","type":"legislation","title":"Loi n° 2002-61 du 9 juillet 2002, portant dispositions relatives à la protection sociale au profit de certains agents des entreprises et des établissements publics à caractère non administratif affiliés à la Caisse nationale de retraite et de prévoyance sociale","issued":{"date-parts":[[2002,7,9]]},"container-title":"Journal officiel de la République tunisienne","issue":"57","page":"1584-1585","URL":"https://www.pist.tn/jort/2002/2002F/Jo0572002.pdf","note":"citation-key: tn-loi-2002-61\nMétadonnées seules. Décret d'application n° 2003-1656 du 4 août 2003."}
]
```

## 10.5 Ce que le manuel ne peut pas faire

Il est **antérieur de six ans à la loi n° 2019-37**. Ses âges (60 ans, 55 ans, 57/37 ans), son
plafond de 90 % à quarante annuités et ses taux de contribution décrivent l'état du droit au
19 décembre 2013. Il ne connaît ni l'augmentation optionnelle de l'âge (article 71 bis), ni les
comptes individuels (articles 71 quinquies et sexies), ni le relèvement transitoire de l'article 5.
Toute règle qu'on lui emprunte doit être confrontée à la loi de 2019 avant d'être portée au précis.

---

# 11. La chaîne modificative de la loi n° 85-12, lue

> Section ajoutée le 11 septembre 2026. Tous les textes ci-dessous ont été **ouverts** : fascicules
> scannés lus à l'image (1987, 1988, 1990 ; chiffres et numéros d'articles relus sur recadrage à
> 300 dpi), fascicules à couche texte lus sur la couche texte puis contrôlés à l'image pour les
> chiffres (2001, 2002 — couche à police décalée, décodée puis relue à l'image — 1996, 1997, 2019,
> 2021, 2022, 2023). La loi 85-12 d'origine a été relue intégralement à l'image (JORT n° 20 du
> 12 mars 1985, pp. 359-365) pour établir chaque « ancien contenu ». Les pieds de page ont été
> contrôlés pour chaque fascicule cité.

## 11.0 Périmètre et exhaustivité de la chaîne

**La liste du manuel de la CNRPS est incomplète.** Une recherche dans `jort_cache.db` (notice la
plus récente de la base : 10 avril 2026) a été menée sur 1985-2026 :

- `LIKE` non accentué sur `titre` et `objet` : `%85-12%`, `%pensions civiles%`, `%12 لسنة 1985%`,
  `%الجرايات المدنية%` ;
- doublée d'une requête FTS : `"85-12" OR "pensions civiles" OR (perequation AND pensions) OR
  (contribution AND retraite AND public)`, puis `retraite OR pensions OR perequation` restreinte
  aux lois et décrets-lois, dépouillée à la main.

Elle fait apparaître **trois modificatifs que le manuel ne nomme pas** — la **loi n° 97-59 du
28 juillet 1997** (art. 47), le **décret-loi n° 2011-48 du 4 juin 2011** (art. 13, taux) et, après
le manuel, le **décret-loi n° 2022-79 du 22 décembre 2022, loi de finances pour 2023, art. 12**
(art. 71 bis) — ainsi que plusieurs textes **dérogatoires** qui écartent la loi 85-12 sans en
modifier la lettre (§ 11.2). Elle ne fait apparaître **aucun autre** modificatif textuel entre 1985
et le 10 avril 2026. Résultat négatif **[M]**, borné à l'indexation de la base : un article de loi
de finances dont la notice ne nommerait ni la loi 85-12 ni les pensions échapperait à ces requêtes.

**Textes voisins, non modificatifs** (écartés après lecture ou sur notice) : loi n° 87-7 du 6 mars
1987, retraite anticipée volontaire, « par dérogation aux dispositions législatives et
réglementaires » (JORT n° 18/1987, p. 363) **[T]** ; loi n° 88-8 du 23 février 1988, contribution
des agents détachés auprès de l'ATCT, « nonobstant toutes les dispositions antérieures contraires »
(JORT n° 15/1988, p. 322) **[T]** ; loi n° 2009-39 (retraite avant l'âge légal), loi n° 2014-48
(Tunisie Télécom), loi n° 2018-5 (départ volontaire) **[M]**.

## 11.1 Texte par texte

### Loi n° 87-8 du 6 mars 1987, instituant des dispositions relatives au travail des retraités

JORT **n° 18 du 10 mars 1987, p. 364**, `/1987/1987F/Jo01887.pdf` **[T]** (lu à l'image).

- **Art. 5** : « Sont abrogées toutes les dispositions contraires à la présente loi et notamment
  **l'article 72 de la loi n° 85-12** du 5 mars 1985. » Ancien art. 72 (p. 365) : « La condition
  d'ancienneté minimum prévue par l'article 22 de la présente loi pour obtention de la pension de
  retraite n'est pas exigée des agents recrutés avant l'entrée en vigueur de la présente loi. »
  → **la dispense transitoire des 15 ans de services disparaît.**
- **Art. 3** (transitoire), qui en tient lieu : les salariés ayant atteint l'âge légal sans remplir
  la condition de stage « peuvent être autorisés à poursuivre l'exercice de leur activité, sans être
  mis à la retraite », pour la durée nécessaire à remplir la condition ; lorsque, à l'entrée en
  vigueur de la loi, la durée de stage restant à courir ne dépasse pas une année, l'intéressé est
  admis à la retraite avec prise en compte de cette période dans l'ancienneté.
- **Art. 1-2** (hors lettre de la loi 85-12, mais sur son terrain — art. 55) : interdiction
  d'employer des retraités titulaires de pension dans l'État, les collectivités publiques locales,
  les EPA et les établissements publics régis par la loi n° 85-72, sauf dérogations individuelles
  annuelles par décret et travaux occasionnels ; **interdiction du cumul** d'une pension « quelle
  que soit son origine » et d'un revenu permanent **dans le secteur privé**, sanctionnée par la
  suspension de la pension et le remboursement des arrérages, et par une amende portée à
  1 500 dinars ; exception pour les retraités propriétaires ou promoteurs de projets qui en assurent
  la direction.
- **Maillon** : ouverture du droit (durée de services) ; cumul.
- **Date d'effet** : **non énoncée**. L'art. 4 fixe au **30 juin 1987** un délai de mise en
  conformité pour les employeurs et salariés — ce n'est pas une clause d'entrée en vigueur.

### Loi n° 88-71 du 27 juin 1988, modifiant et complétant la loi n° 85-12

JORT **n° 45 du 1er juillet 1988, pp. 967-968**, `/1988/1988F/Jo04588.pdf` **[T]** (lu à l'image,
recadrages à 300 dpi sur les art. 5 et 61).

Art. 1er : « Les dispositions des articles **5, 16, 24, 33, 41 et 61** […] sont abrogées et
remplacées ». Art. 2 : complète l'**art. 6**. Art. 3 : abroge les **art. 25 et 26**.

| Article | Ancien (1985) | Nouveau (1988) | Maillon |
|---|---|---|---|
| **5, 2° e)** | « sur la demande des mères ayant trois enfants dont l'âge n'a pas dépassé **15 ans** » | « sur la demande des mères ayant **au moins** trois enfants dont l'âge n'a pas dépassé **20 ans** **ou un enfant handicapé d'un handicap profond** et **après accord du Premier ministre** » | ouverture du droit (départ anticipé) |
| **5, 2° f)** (ajout) | — | « **d'office** après 15 ans de services civils et militaires effectifs » | ouverture du droit |
| **6** (dernier alinéa ajouté, art. 2) | — | hors militaires et FSI, la **mise à la retraite d'office** est décidée **par décret** au vu d'un rapport de l'employeur et des observations de l'agent, notifié **six mois au moins** avant | ouverture du droit (procédure) |
| **16** | validation de la période de disponibilité ou de congé sans solde | ajoute « la période normale d'études et le cycle de formation poursuivie par l'agent avec succès en Tunisie ou à l'étranger à partir de l'année qui suit la quatrième année après le baccalauréat ou diplôme équivalent » ; modalités par décret | validation des services |
| **24** | 60 ans « à l'exception des catégories des personnels visés aux articles 25, 26, 27, 28 et 29 » | « Sous réserve des dispositions des articles 27, 28 et 29 […] fixé à soixante (60) ans ; ils peuvent toutefois être **maintenus en activité, jusqu'à l'âge de soixante cinq (65) ans au maximum par décret** », pris « sur la base d'un rapport motivé du ministre concerné » | ouverture du droit (âge) |
| **25-26** (abrogés, art. 3) | 70 ans Premier Président et Procureur général de la Cour de cassation ; 65 ans autres cadres supérieurs (liste par décret) ; 65 ans chef de secteur | — | ouverture du droit (âge) |
| **33** | bonification jusqu'à 60 ans : 1° FSI et militaires blessés en service ; 2° invalides à 80 % ; 3° suppression d'emplois | ajoute aux blessés « les personnels des **services actifs des douanes** » ; ajoute un **4)** : « des agents mis à la retraite **d'office** à condition que le rendement de la bonification **ne dépasse pas 20 %** de la rémunération sur la base de laquelle est liquidée la pension de retraite » | bonifications |
| **41** | jouissance immédiate : âge légal, invalidité, suppression d'emplois ; différée à 50 ans (demande, insuffisance professionnelle) ou à l'âge légal (révocation, démission) | jouissance immédiate étendue à « d) la mise à la retraite sur la demande des mères […] » et « e) la mise à la retraite d'office » ; différés inchangés | ouverture du droit (jouissance) |
| **61, 1°** | 50 / 55 / 58 ans ; **60 ans officiers supérieurs ; 62 ans officiers généraux** | 50 / 55 / 58 ans ; « **60 ans pour le cadre des officiers généraux et des officiers supérieurs** » | militaires |
| **61, 2°** | départs avant l'âge après 30 / 25 / 20 / 15 / 15 ans de services | reproduit à l'identique | militaires |

- **Date d'effet** : art. 4, « La présente loi entre en vigueur à l'expiration d'un délai de six (6)
  mois à compter de la date de sa publication au *Journal officiel* » **[T]**. Publication au pied
  de page : 1er juillet 1988 → effet le **1er janvier 1989** **[D]** (dérivé de la clause et du pied
  de page).

### Loi n° 90-6 du 12 février 1990, modifiant la loi n° 85-12

JORT **n° 14 des 20-23 février 1990, p. 264**, `/1990/1990F/Jo01490.pdf` **[T]** (lu à l'image).

- **Article unique** : remplace l'**alinéa dernier de l'art. 6** « tel qu'il a été modifié et
  complété par la loi n° 88-71 ». Nouveau : hors militaires et agents des forces de sécurité
  intérieure, la mise à la retraite d'office est décidée par décret au vu d'un rapport de
  l'employeur et des observations de l'agent ; « Celles-ci doivent être consignées par écrit et
  adressées à l'employeur dans **un délai d'un mois** à compter de la date de communication du
  rapport » ; le décret est notifié à l'agent et à la CNRPS « **deux mois** avant la date de mise à
  la retraite » (**six mois** en 1988).
- **Maillon** : ouverture du droit (procédure de la retraite d'office).
- **Date d'effet** : **non énoncée**.

### Loi n° 94-71 du 27 juin 1994, révision des taux de contribution

JORT **n° 50 du 28 juin 1994, p. 1086**, `/1994/1994F/Jo05094.pdf` **[T]** (couche texte).

- **Article unique** : taux relevés de **1 %** à la charge de l'assuré social **à partir du
  1er juillet 1994**, et de **1,2 %** à la charge de l'employeur **à partir du 1er juillet 1995** ;
  « En conséquence, sont modifiés […] **les articles 9 et 13** de la loi n° 85-12 » (et les régimes
  des membres du gouvernement, des députés et des gouverneurs).
- **Maillon** : financement (hors prestations). **Date d'effet** : énoncée par tranche.

### Loi n° 95-105 du 14 décembre 1995 et décret n° 96-1015 du 27 mai 1996 — validation des services

Loi : JORT **n° 101 du 19 décembre 1995, p. 2308**, `/1995/1995F/Jo10195.pdf` **[T]** (couche texte ;
barème de l'art. 4 relu à l'image). Décret :
JORT **n° 45 du 4 juin 1996, pp. 1109-1110**, `/1996/1996F/Jo04596.pdf` **[T]** (extraction par
colonne).

- **Aucun article de la loi 85-12 n'est visé nommément.** La loi institue un « système unifié de
  validation des services applicable à tous les assurés sociaux relevant d'un régime légal de
  sécurité sociale » (art. 1er) et « Toutes les dispositions antérieures contraires à la présente
  loi sont abrogées » (art. 10). Elle entre donc en conflit, **par abrogation implicite**, avec les
  articles 14 à 21 de la loi 85-12 **[D]** :
  - périodes validables (art. 2) : activité effective rémunérée assujettie non déclarée ; services
    à l'étranger en coopération technique ; mise en disponibilité spéciale ;
  - **cotisation selon l'âge du postulant** (art. 4) : **23 %** jusqu'à 24 ans, **24 %** de 25 à 29,
    **25 %** de 30 à 34, **27 %** de 35 à 39, **28 %** de 40 à 44, **29 %** de 45 à 49, **31 %** de
    50 à 54, **32 %** à 55 ans et plus — sur le salaire de référence de la pension « comme si le
    demandeur ouvrait droit à pension à la date de sa demande » (art. 5), et non plus sur la
    moyenne de l'art. 18 de la loi 85-12 ;
  - paiement échelonné en **36 mensualités au plus** (art. 7), contre des retenues « ne dépassant
    pas 20 % de la rémunération » à l'art. 21 de la loi 85-12 ;
  - demande **dans les 2 ans suivant la fin des périodes** et au plus tard un an après l'âge légal
    (art. 8) ; délai transitoire d'un an pour les périodes de la législation antérieure (art. 9).
- Le décret n° 96-1015, art. 5-1 : « Les **périodes d'étude et de formation** qui ne sont pas soumis
  à cotisation au titre des régimes de retraite, **ne sont pas validables** ». **Tension non
  résolue** avec l'art. 16 (nouveau) issu de la loi 88-71, qui ouvrait la validation des études
  au-delà de bac + 4 **[D]** — à trancher (doctrine de la caisse, jurisprudence).
- Art. 10 du décret : les demandes antérieures à la loi 95-105 sont liquidées selon l'ancienne
  législation.
- **Maillon** : validation des services. **Date d'effet** : **non énoncée** (ni loi, ni décret).

### Loi n° 96-67 du 22 juillet 1996, modifiant la loi n° 85-12

JORT **n° 60 du 26 juillet 1996, p. 1604**, `/1996/1996F/Jo06096.pdf` **[T]**.

- **Article unique** : remplace l'**art. 48**. Ancien : « Les pensions des orphelins ne peuvent, au
  total, être inférieures au montant des indemnités familiales dont aurait bénéficié l'agent »
  — un **plancher**. Nouveau : « A la pension des orphelins **s'ajoutent** le cas échéant, les
  indemnités familiales attribuées selon les mêmes modalités et les mêmes taux qui s'appliquent à
  l'agent décédé comme s'il les percevait effectivement » — un **accessoire additionnel**.
- **Maillon** : droits dérivés / accessoires. **Date d'effet** : **non énoncée**.
- Homonymie : ne pas confondre avec la loi n° 96-67 du 29 juillet 1996 (accord d'investissement).

### Loi n° 97-59 du 28 juillet 1997, amendant la loi n° 85-12 — absente du manuel

JORT **n° 61 du 1er août 1997, p. 1359**, `/1997/1997F/Jo06197.pdf` **[T]** (couche texte, relue à
l'image).

- **Article premier** : ajoute un **alinéa 3 à l'art. 47** : « Les dispositions des articles 45 et
  46 s'appliquent également **jusqu'à l'âge de vingt et cinq (25) ans** aux orphelins, justifiant de
  la poursuite des études supérieures, à condition qu'ils ne soient pas bénéficiaires d'une bourse
  universitaire, ainsi qu'**à la fille tant qu'elle ne dispose pas des ressources** ou que
  l'obligation alimentaire n'incombe pas à son époux. »
- **Date d'effet** : art. 2, « La présente loi prend effet à compter du **1er mai 1997** » **[T]** —
  la même date que le décret n° 97-1927 pour le régime privé (§ 11 bis).
- **Maillon** : droits dérivés (orphelins).
- **Conséquence** : l'âge de 25 ans et la fille sans ressources datent de **1997**, non de la loi
  n° 2007-43, qui réécrit l'art. 47 en reprenant et en précisant ces conditions (suspension
  définitive du paiement si l'une d'elles vient à manquer ; appréciation à la date du décès).

### Loi n° 97-74 du 18 novembre 1997, amendant la loi n° 85-12

JORT **n° 93 du 21 novembre 1997, p. 2080**, `/1997/1997F/Jo09397.pdf` **[T]**.

- **Article unique** : ajoute un **alinéa 3 à l'art. 42** : « L'allocation de vieillesse est
  **reversible au profit du conjoint survivant et des orphelins**, selon les conditions et modalités
  applicables en matière des pensions, prévues aux articles 43 à 48 de la présente loi. »
- **Maillon** : planchers (allocation de vieillesse) / droits dérivés. **Date d'effet** : **non
  énoncée**.

### Loi n° 2001-123 du 28 décembre 2001, loi de finances pour 2002 — art. 85 et 86

JORT **n° 104 du 28 décembre 2001, p. 4260** (art. 97 : p. 4261), `/2001/2001F/Jo1042001.pdf`
**[T]** (couche à police décalée, décodée puis relue à l'image). Aucun autre article de la loi ne
vise la loi 85-12 ni les pensions du secteur public (dépouillement des pp. 4251-4261).

- **Art. 85** : taux relevés de **1 %** à la charge de l'assuré (**0,50 %** au 1er juillet 2002,
  **0,25 %** au 1er juillet 2003, **0,25 %** au 1er juillet 2004) et de **1,5 %** à la charge de
  l'employeur (**0,50 %** au 1er juillet 2002, puis **0,25 %** chaque 1er juillet de 2003 à 2006) ;
  modifie « les **articles 9 et 13** de la loi n° 85-12 ». Maillon : financement.
- **Art. 86** : « L'article 37 de la loi n° 85-12 […] est modifié comme suit » — les deux premiers
  alinéas reprennent le texte de 1985 ; le troisième devient : « Cette péréquation est soumise aux
  dispositions des articles **9, 10, 11 et 13** de la présente loi. **La contribution du bénéficiaire
  de la pension au titre de cette péréquation est due durant toute la période de service de la
  pension et ses accessoires. La contribution de l'employeur au titre de cette même péréquation est
  due sur une période de 36 mois.** »
  - Deux changements : (i) la **péréquation devient cotisée** par le retraité pendant tout le
    service de la pension, l'employeur ne cotisant que 36 mois ; (ii) **l'art. 36 disparaît** de la
    liste des renvois.
  - Maillon : revalorisation.
- **Date d'effet** : art. 97, « Sans préjudice des dispositions des articles 39, 70, 76 et 77 les
  dispositions de la présente loi sont applicables à compter du **1er janvier 2002** » **[T]** ; les
  art. 85-86 n'y dérogent pas.
- **Rapprochement avec la loi n° 2007-43** (texte lu, § 1.6) : l'art. 37 (nouveau) de 2007
  **rétablit l'art. 36** dans les renvois (« articles 9, 10, 11, 13 et 36 ») et reformule la règle
  de 2002 : « La totalité des contributions au titre de cette péréquation durant la période de
  paiement de la pension et de ses accessoires, à l'exception de la quote-part des contributions
  mises à la charge de l'employeur durant 36 mois, est à la charge du bénéficiaire de la pension. »
  **La mise à la charge du retraité date donc de 2002, non de 2007** ; la loi de 2007 précise que
  c'est « la totalité » des contributions, parts salariale et patronale, hors les 36 mois de
  l'employeur **[D]** (lecture comparée des deux libellés).

### Loi n° 2002-61 du 9 juillet 2002, protection sociale de certains agents des EPNA

JORT **n° 57 du 12 juillet 2002, pp. 1584-1585**, `/2002/2002F/Jo0572002.pdf` **[T]** (couche à
police décalée, relue à l'image).

- **Art. 1er-6** (régime propre) : agents des entreprises et établissements publics à caractère non
  administratif affiliés à la CNRPS, **licenciés dans le cadre de l'assainissement et de la
  restructuration** des entreprises à participations publiques (loi n° 89-9) ; ceux qui remplissent
  la condition d'ancienneté de l'art. 22 sont **mis à la retraite proportionnelle** par arrêté du
  Premier ministre (art. 2) et « bénéficient d'une pension de retraite **à l'âge de 50 ans** tout en
  continuant à être assujettis aux dispositions de la loi n° 85-12 » (art. 3) ; soins et indemnités
  familiales maintenus un an pour ceux de moins de 50 ans (art. 4) ; charge de l'entreprise ou du
  fonds de restructuration jusqu'à l'âge de la retraite (art. 5) ; modalités par décret (art. 6 —
  décret n° 2003-1656, non lu).
- **Art. 7** : remplace l'**art. 5, 2° d)** : « à l'initiative de l'employeur pour insuffisance
  professionnelle de l'agent ou révocation » — **la suppression d'emploi est retirée**.
- **Art. 8** : abroge « les dispositions du **paragraphe 2 de l'article 6**, du **paragraphe 3 de
  l'article 33** et de l'**alinéa "C" du 1er paragraphe de l'article 41** ».
  - Désignations vérifiées sur les versions en vigueur en 2002 **[D]** : art. 6 § 2 = texte de 1985,
    « Toutefois, la mise à la retraite pour suppression d'emploi est décidée par arrêté du Premier
    Ministre » ; art. 33 § 3 = texte de 1988, « des agents mis à la retraite pour suppression
    d'emplois » ; art. 41 1° c) = texte de 1988, « la mise à la retraite pour suppression
    d'emplois ». Contrôle indirect : l'art. 33 (nouveau) de 2019 ne compte plus que trois cas, sans
    la suppression d'emplois.
- **Effet d'ensemble** : **la voie « suppression d'emplois » est retirée de la loi 85-12** (cause
  de départ, procédure, bonification, jouissance immédiate) et remplacée par le régime spécial de
  2002.
- **Maillon** : ouverture du droit ; bonifications. **Date d'effet** : **non énoncée**.

### Loi n° 2007-43 du 25 juin 2007 (rappel, déjà lue)

Outre les art. 30, 37, 46 et 47 (§ 1.1, 1.4, 1.6), son **article premier** relève les taux : **1,8 %**
à la charge de l'employeur (0,60 % au 1er janvier 2007, 2008, 2009) et **1,2 %** à la charge de
l'assuré (0,40 % au 1er juillet 2007, 2008, 2009), modifiant les **art. 9 et 13** **[T]** (texte
intégral versionné dans `openfisca-tunisia-pension/tmp/JORTs/`).

### Décret-loi n° 2011-48 du 4 juin 2011 — absent du manuel

JORT **n° 41 du 7 juin 2011, p. 844**, `/2011/2011F/Jo0412011.pdf` **[T]** (couche texte).

- **Article premier** : taux à la charge de l'**employeur** relevés d'**un pour cent** « à partir du
  **1er juillet 2011** » ; modifie « l'**article 13** de la loi n° 85-12 » (et les régimes des
  membres du gouvernement et des gouverneurs — **pas celui des députés**).
- **Maillon** : financement.

### Loi n° 2009-20 et loi n° 2019-37 (rappel, déjà lues)

- 2009-20 : art. 24 et art. 29 bis (professeurs de l'enseignement supérieur) — § 6.1 bis.
- 2019-37 **[T]** : art. 1er, remplace l'art. 3, l'art. 8 § 2, les **art. 24, 27, 28, 29**, les § 2
  et 3 de l'art. 29 bis, l'**art. 33** (trois cas ; repère 62 ans ; le plafond de 20 % pour la
  retraite d'office **y est reconduit**, il date de 1988), l'art. 61 § 1, les art. 64 et 67 ;
  **art. 2**, remplace « l'âge de soixante ans » par « l'âge de soixante-deux ans » aux **§ 2 et 3 de
  l'art. 32** ; art. 3, ajoute l'art. 1er c), l'art. 9 bis et les art. 71 bis à 71 septies ; art. 4,
  taux + 3 %.

## 11.2 Après la loi n° 2019-37

### Décret-loi n° 2022-79 du 22 décembre 2022, loi de finances pour 2023 — art. 12

JORT **n° 141 du 23 décembre 2022**, **édition arabe seulement** : l'URL française
`/2022/2022F/Jo1412022.pdf` répond `404` (289 octets), conformément à `outillage-sources.md` ;
**p. 4060** de l'édition arabe, `/2022/2022A/Ja1412022.pdf` **[T]** (couche texte arabe, relue à
l'image). **Aucune pagination française n'existe.**

- **Art. 12** (intitulé « ترشيد الترفيع في سن الإحالة على التقاعد », rationalisation de
  l'augmentation de l'âge de mise à la retraite) : « تلغى أحكام الفصل 71 مكرّر […] وتعوّض
  بالأحكام التالية » — **abroge et remplace l'art. 71 bis**. Traduction de travail, non officielle :
  - les agents régis par les art. 24, 27, 28, 29 (nouveaux) **et 61 (premier paragraphe nouveau)**
    peuvent opter pour l'augmentation de l'âge d'un, deux ou trois ans ;
  - demande écrite à l'employeur « pour qu'il statue par **l'approbation ou le rejet** » (للبتّ فيه
    بالموافقة أو الرفض), **six mois au moins** avant l'âge ;
  - seules les demandes approuvées sont transmises à la CNRPS ;
  - « les agents dont l'augmentation optionnelle a été approuvée **peuvent présenter des demandes de
    renonciation** » (مطالب تراجع) ;
  - les personnes de l'art. 29 bis : un à cinq ans, jusqu'à 70 ans, selon la même procédure
    « **à l'exception de la condition d'approbation de l'employeur** » ;
  - modalités par décret.
- **Ce qui change par rapport à 2019** (art. 71 bis lu, JORT n° 35/2019, p. 1313) : en 2019 l'option
  était de droit pour les civils — l'employeur transmettait les demandes — et « considérée comme
  étant **définitive et irrévocable** », l'accord de l'employeur n'étant requis que pour les
  militaires. Depuis 2023, **l'option est subordonnée à l'accord de l'employeur** pour tous les
  agents sauf ceux de l'art. 29 bis, et elle **devient révocable**.
- **Date d'effet** : art. 76, « مع مراعاة الأحكام المخالفة الواردة بهذا المرسوم، تطبّق أحكام هذا
  المرسوم بداية من غرّة جانفي 2023 » — **1er janvier 2023** **[T]** ; l'art. 12 ne comporte pas de
  disposition contraire.
- **Maillon** : ouverture du droit (âge).
- Notice `jort_cache` : type `Decret-Loi`, `numero` vide, pages 4060, `pdf_fr` vide.

### Décret n° 2023-741 du 1er décembre 2023, modalités de l'augmentation optionnelle de l'âge

JORT **n° 138 du 1er décembre 2023, pp. 3240-3242**, `/2023/2023F/Jo1382023.pdf` **[T]** (couche
texte ; édition française vérifiée au pied de page). Pris en application de l'art. 71 bis
(nouveau) ; vise expressément l'art. 12 du décret-loi n° 2022-79.

- Champ : agents dont l'âge légal est atteint **à compter du 1er décembre 2023** (art. 2) ; un, deux
  ou trois ans pour les agents des art. 24, 27, 28, 29 et 61 al. 1er (art. 3).
- Procédure : demande écrite **entre un an et six mois** avant l'âge légal, rejet d'office hors
  délai (art. 4) ; décision du chef de l'administration **sous 30 jours**, notification à l'agent
  sous 10 jours (art. 5) ; arrêté notifié à la CNRPS par le système d'échange automatisé (art. 6).
- **Renonciation** possible, « réputée définitive et irrévocable », y compris pour les agents ayant
  bénéficié de l'augmentation au titre de l'art. 5 de la loi 2019-37 (art. 7-8).
- Art. 29 bis : un à cinq ans jusqu'à 70 ans, sans approbation du chef de l'administration (art. 9).
- **Transitoire** (art. 10) : les agents ayant atteint l'âge légal entre le **1er janvier et le
  30 novembre 2023** et dont la demande déposée dans les délais n'a pas été tranchée bénéficient de
  « l'augmentation **systématique d'une année** » ; au-delà d'un an, l'employeur statue sous trois
  mois.
- **Date d'effet** : **non énoncée** (art. 11, clause de publication) ; le champ temporel est fixé
  par l'art. 2.
- Notice `jort_cache` fautive : `numero` = « 2023-138 » (numéro du fascicule), page 3240 seule.

### Textes dérogatoires, sans modification de la lettre de la loi 85-12

| Texte | JORT | Contenu | Effet | Niv. |
|---|---|---|---|---|
| **Décret-loi n° 2021-21 du 28 décembre 2021**, LF 2022, **art. 14** | n° 119 du 28 déc. 2021, **p. 3082**, `/2021/2021F/Jo1192021.pdf` | « Contrairement aux dispositions de la loi n° 85-12 », départ anticipé avant 62 ans pour les agents âgés d'**au moins 57 ans** entre le 1er janvier 2022 et le 31 décembre 2024, ayant la durée minimale de services ; pension immédiate avec **bonification** jusqu'à l'âge légal ; pensions et contributions de la période à la charge de l'employeur ; catégories et modalités par décret présidentiel | art. 73 : 1er janvier 2022 | **[T]** |
| Loi n° 2024-48 du 9 décembre 2024, LF 2025, art. 14 | n° 149/2024, p. 6420 (**pagination arabe** ; édition française absente) | prolonge l'art. 14 de la LF 2022 | — | **[M]** |
| Arrêtés du Chef du Gouvernement fixant les délais d'application du programme (16 juin 2022, 9 janvier 2023, 12 décembre 2023, 30 décembre 2024) | n° 69/2022, 4/2023, 145/2023, 159/2024 | délais annuels | — | **[M]** |
| **Décret-loi n° 2022-49 du 16 août 2022** | n° 93 du **19 août 2022**, **p. 2494** (édition française), `/2022/2022F/Jo0932022.pdf` | « à titre dérogatoire et conjoncturel, et contrairement aux dispositions du quatrième alinéa de l'article 37 » : **différentiel complémentaire** de pension égal au manque résultant de la retenue de la part patronale sur la péréquation des augmentations de 2019, jusqu'au 31 décembre 2022 ; retenue **suspendue** de février 2022 à l'entrée en vigueur ; coût à la charge du budget de l'État (art. 71 septies) | non énoncée | **[T]** |

Divergence de notice sur le décret-loi n° 2022-49 : `jort_cache` donne signature 5 août, publication
8 août 2022, p. 2793 (pagination arabe) ; le titre porte « du 16 août 2022 » et le pied de page de
l'édition française « 19 août 2022 », p. 2494. Le pied de page fait foi (§ 3 bis et § 4 de
`outillage-sources.md`).

Hors champ mais signalé : la **loi de finances pour 2026** (loi n° 2025-17, art. 102, JORT
n° 148/2025, notice arabe **[M]**) abroge les art. 3 et 5 de la **loi n° 85-16** (députés), non de la
loi 85-12.

## 11.3 Réponses aux trois questions du chapitre

1. **La loi 88-71 porte-t-elle de 15 à 20 ans l'âge des enfants (art. 5) ? — Oui** **[T]**. Elle
   ajoute en outre deux éléments : la mère d'**un enfant handicapé d'un handicap profond**, et la
   condition d'**accord du Premier ministre** ; « trois enfants » devient « au moins trois
   enfants ». La jouissance devient immédiate (art. 41 nouveau, 1° d). Effet : 1er janvier 1989
   **[D]**.
2. **Art. 25-26, 28-29, 30, 32 ?**
   - **25-26 : oui** — abrogés par la loi 88-71 (art. 3) ; la prorogation est reversée dans
     l'art. 24 (nouveau) sous forme de maintien en activité **par décret jusqu'à 65 ans**, sur
     rapport motivé du ministre, sans catégorie nommée **[T]**.
   - **28-29 : non** dans la chaîne 1987-2011 ; seule la loi 2019-37 les remplace (déjà lue).
   - **30 : non** ; seule la loi 2007-43 le modifie (déjà lue).
   - **32 : non** dans la chaîne 1987-2011 ; la loi 2019-37, art. 2, y substitue 62 à 60 ans aux § 2
     et 3 **[T]**. **33 : oui** — réécrit en 1988 (douanes, retraite d'office plafonnée à 20 %), § 3
     abrogé en 2002 (suppression d'emplois), réécrit en 2019.
3. **Art. 36 à 42 ?**
   - **36, 38, 39 et 40 : aucun texte de la chaîne ne les modifie**, de 1985 au 10 avril 2026
     (limite de la base, sous la réserve d'indexation du § 11.0). **La fenêtre de la rémunération de liquidation (dernière rémunération,
     trois ans de retenues, fonction la plus élevée exercée deux ans), le barème 2 / 3 / 2 %, le
     plafond de 90 %, la pension minimale des deux tiers du SMIG et l'article sur les indemnités
     familiale et de revenu unique sont ceux de 1985.** L'art. 38 n'est que visé par l'art. 71 ter
     (2019).
   - **37 : oui, deux fois** — LF 2002 art. 86 (effet 1er janvier 2002), loi 2007-43 ; plus la
     dérogation temporaire du décret-loi 2022-49.
   - **41 : oui, deux fois** — loi 88-71 (mères, retraite d'office), loi 2002-61 (suppression
     d'emplois retirée).
   - **42 : oui** — loi 97-74, réversibilité de l'allocation de vieillesse.

## 11.4 Corrections à reporter ailleurs (non faites ici)

Dans ce dossier (§ 1) et dans `precis/fr/retraites/_secteur_public.qmd` :

- **§ 1.0 et § 1.1** : la loi 88-71 est lue — passer les lignes de **[M]** à **[T]**, effet
  1er janvier 1989 **[D]** ; ajouter la branche « enfant handicapé profond » et l'accord du Premier
  ministre.
- **§ 1.1, prorogation** : les valeurs 70 / 65 / 65 ans (art. 25-26) ne valent que du 12 septembre
  1985 au 31 décembre 1988 ; ensuite, maintien par décret jusqu'à 65 ans (art. 24 nouveau).
- **§ 1.1, militaires** : officiers généraux **62 → 60 ans au 1er janvier 1989** (loi 88-71), avant
  le passage à 62 ans en 2019 ; la ligne actuelle ne montre pas cette étape.
- **§ 1.1, art. 72** : la dispense transitoire de la condition d'ancienneté est **abrogée par la loi
  87-8** (art. 5), date d'effet non énoncée.
- **§ 1.1, bonifications** : le **plafond de 20 %** pour la retraite d'office date de la **loi 88-71**
  (art. 33 nouveau), reconduit en 2019 ; la « suppression d'emplois » disparaît de l'art. 33 en 2002.
- **§ 1.1, départs anticipés et § 1.1 jouissance** : ajouter la retraite d'office (art. 5 2° f,
  1988 ; procédure art. 6, 1988 puis 1990) et le retrait de la suppression d'emploi (2002, régime
  des EPNA à 50 ans).
- **§ 1.3, « plancher des pensions d'orphelins »** : ne décrit plus le droit après la loi 96-67 ;
  depuis, les indemnités familiales **s'ajoutent** à la pension d'orphelin.
- **§ 1.3, allocation de vieillesse** : **réversible** depuis la loi 97-74.
- **§ 1.4 et « point de vigilance » sous le tableau** : les conditions « 25 ans, études supérieures
  sans bourse » et « fille sans ressources » sont introduites par la **loi 97-59, effet 1er mai
  1997**, et non par la loi 2007-43, qui les réécrit. Le rattachement du paramètre à la loi 85-12
  reste inexact, mais la bonne référence est **97-59** (puis 2007-43).
- **§ 1.6** : la mise à la charge du retraité des contributions de péréquation date de la **LF 2002,
  art. 86** (effet 1er janvier 2002) ; la loi 2007-43 la reformule et rétablit le renvoi à l'art. 36.
- **§ 1.1, augmentation optionnelle** : l'option « définitive et irrévocable » de 2019 est remplacée
  au **1er janvier 2023** par une option soumise à l'accord de l'employeur et révocable
  (décret-loi 2022-79, art. 12 ; décret 2023-741).
- **Validation des services** (§ 10.2) : le régime des art. 14-21 de la loi 85-12 est supplanté par
  la loi 95-105 ; tension ouverte sur la validation des études (art. 16 nouveau de 1988 contre
  art. 5 du décret 96-1015).
- **Glossaire** (`precis/glossaire.yml`, à ne modifier que par le rédacteur) : l'entrée
  `mise-a-la-retraite-d-office` attribue le plafond de 20 % à la loi 2019-37 (il date de 1988) ;
  l'entrée `perequation` attribue à la loi 2007-43 la mise à la charge du retraité (elle date de
  2002) ; l'entrée `allocation-de-vieillesse` ne mentionne pas la réversibilité (1997).
- **Notes CSL-JSON à mettre à jour** (§ 9 et § 10.4 portent « Métadonnées seules ») : `tn-loi-1987-8`,
  `tn-loi-1988-71` (retirer « selon la référence du modèle ; à vérifier »), `tn-loi-1990-6`,
  `tn-loi-1995-105`, `tn-loi-1996-67`, `tn-loi-1997-74`, `tn-loi-2002-61`, `tn-loi-1987-7` — et leurs
  homologues déjà présents dans les `references.json` (`loi87-8`, `loi88-71`, etc.). Clés existantes
  et entrées à créer : § 11.6.

## 11.5 Tableau de synthèse pour le rédacteur

| Texte | Date d'effet | Articles de la loi 85-12 touchés | Maillon | Ce qui change | Niv. |
|---|---|---|---|---|---|
| Loi n° 87-8 du 6 mars 1987 | non énoncée | 72 (abrogé) | ouverture du droit ; cumul | Fin de la dispense des 15 ans de services pour les agents recrutés avant 1985, remplacée par un maintien en activité jusqu'à la durée requise ; cumul pension-revenu permanent interdit dans le privé. | [T] |
| Loi n° 88-71 du 27 juin 1988 | 1er janv. 1989 (six mois après publication) | 5, 6, 16, 24, 25-26 (abrogés), 33, 41, 61 | ouverture du droit ; validation ; bonifications ; militaires | Mères de trois enfants de moins de 20 ans (au lieu de 15) ou d'un enfant lourdement handicapé ; retraite d'office créée, bonifiée dans la limite de 20 % ; prorogations remplacées par un maintien jusqu'à 65 ans par décret ; officiers généraux à 60 ans ; validation des études au-delà de bac + 4. | [T] (date [D]) |
| Loi n° 90-6 du 12 février 1990 | non énoncée | 6 (dernier alinéa) | ouverture du droit | Retraite d'office : observations de l'agent sous un mois, notification deux mois (et non plus six) avant la mise à la retraite. | [T] |
| Loi n° 94-71 du 27 juin 1994 | 1er juill. 1994 (agent), 1er juill. 1995 (employeur) | 9, 13 | financement | Contributions + 1 % agent, + 1,2 % employeur. | [T] |
| Loi n° 95-105 du 14 décembre 1995 et décret n° 96-1015 | non énoncée | 14-21 (abrogation implicite) | validation des services | Système unifié : cotisation de 23 à 32 % selon l'âge sur le salaire de référence, 36 mensualités, demande sous deux ans ; études non validables selon le décret. | [T] (portée [D]) |
| Loi n° 96-67 du 22 juillet 1996 | non énoncée | 48 | droits dérivés ; accessoires | Les indemnités familiales s'ajoutent à la pension des orphelins, au lieu d'en constituer le plancher. | [T] |
| Loi n° 97-59 du 28 juillet 1997 | 1er mai 1997 | 47 (al. 3 ajouté) | droits dérivés | Pension d'orphelin jusqu'à 25 ans pour les études supérieures sans bourse ; sans limite d'âge pour la fille sans ressources. | [T] |
| Loi n° 97-74 du 18 novembre 1997 | non énoncée | 42 (al. 3 ajouté) | planchers ; droits dérivés | L'allocation de vieillesse devient réversible au conjoint survivant et aux orphelins. | [T] |
| Loi n° 2001-123 (LF 2002), art. 85-86 | 1er janv. 2002 ; taux par tranches 2002-2006 | 9, 13, 37 | financement ; revalorisation | Contributions + 1 % agent et + 1,5 % employeur ; la péréquation est cotisée par le retraité pendant tout le service de la pension, par l'employeur pendant 36 mois. | [T] |
| Loi n° 2002-61 du 9 juillet 2002 | non énoncée | 5 (2° d), 6 (§ 2), 33 (§ 3), 41 (1° c) | ouverture du droit ; bonifications | La suppression d'emplois disparaît de la loi 85-12 ; les agents d'EPNA licenciés en restructuration relèvent d'une retraite proportionnelle servie à 50 ans. | [T] (désignations [D]) |
| Loi n° 2007-43 du 25 juin 2007 | non énoncée (taux par tranches 2007-2009) | 9, 13, 30, 37, 46, 47 | financement ; ouverture du droit ; revalorisation ; droits dérivés | Départ anticipé à 57 ans et 37 ans de services ; totalité des contributions de péréquation au retraité hors 36 mois employeur ; fille sans ressources plafonnée à 50 % ; contributions + 1,8 % employeur et + 1,2 % agent. | [T] |
| Loi n° 2009-20 du 13 avril 2009 | non énoncée | 24, 29 bis (créé) | ouverture du droit | Professeurs et maîtres de conférences du supérieur à 65 ans, maintien possible jusqu'à 70 ans. | [T] |
| Décret-loi n° 2011-48 du 4 juin 2011 | 1er juill. 2011 | 13 | financement | Contribution employeur + 1 %. | [T] |
| Loi n° 2019-37 du 30 avril 2019 | non énoncée (calendrier transitoire, art. 5) | 1, 3, 8, 9, 9 bis, 13, 24, 27-29, 29 bis, 32, 33, 61, 64, 67, 71 bis-septies | ouverture du droit ; bonifications ; militaires ; financement | Âges relevés de deux ans ; augmentation optionnelle de l'âge ; comptes individuels ; contributions + 3 %. | [T] |
| Décret-loi n° 2022-79 (LF 2023), art. 12 | 1er janv. 2023 | 71 bis | ouverture du droit | L'augmentation optionnelle de l'âge exige l'accord de l'employeur (sauf art. 29 bis) et devient révocable. | [T] (édition arabe) |
| Décret n° 2023-741 du 1er décembre 2023 | non énoncée ; agents atteignant l'âge dès le 1er déc. 2023 | — (application de l'art. 71 bis) | ouverture du droit | Procédure : demande entre un an et six mois avant l'âge, décision sous 30 jours, renonciation irrévocable ; une année accordée d'office aux demandes 2023 restées sans réponse. | [T] |

Textes dérogatoires, sans modification de la lettre : LF 2022 (décret-loi n° 2021-21), art. 14,
départ anticipé dès 57 ans en 2022-2024, prolongé par la LF 2025 **[T]/[M]** ; décret-loi n° 2022-49,
neutralisation temporaire de la part patronale de péréquation retenue sur les pensions **[T]**.

## 11.6 Références : clés existantes et entrées à créer

**Déjà présentes** dans `precis/fr/references.json` ou un `references.json` de livre (contrôle du
11 septembre 2026 ; ne pas dupliquer) : `loi85-12`, `loi87-8`, `loi88-71`, `loi90-6`, `loi94-71`,
`loi95-105`, `loi96-67`, `loi97-74`, `loi2002-61`, `loi2001-123-lf2002` (cotisations sociales ; sa
note décrit l'art. 85 — **y ajouter l'art. 86 et l'art. 97**), `decretloi2011-48` (cotisations
sociales), `lf-2022` (fiscalité, décret-loi n° 2021-21 — sa page 3086 ne couvre pas l'art. 14, p. 3082),
`lf-2023` (fiscalité, décret-loi n° 2022-79 — ajouter l'art. 12, p. 4060 de l'édition arabe),
`lf-2025`, `decret96-326`, `decret97-1927` (note à compléter : art. 2, effet 1er mai 1997). Les clés
proposées aux § 9 et § 10.4 sous la forme `tn-loi-AAAA-NN` sont donc à rapprocher de ces clés
existantes avant tout ajout.

**À créer** (convention de clés du dépôt) :

```json
[
  {"id":"loi97-59","type":"legislation","title":"Loi n° 97-59 du 28 juillet 1997, amendant la loi n° 85-12 du 5 mars 1985, portant régime des pensions civiles et militaires de retraite et des survivants dans le secteur public","issued":{"date-parts":[[1997,7,28]]},"container-title":"Journal officiel de la République tunisienne","issue":"61","page":"1359","URL":"https://www.pist.tn/jort/1997/1997F/Jo06197.pdf","note":"citation-key: loi97-59\nJORT n° 61 du 1er août 1997. Art. 1 : art. 47 al. 3 nouveau — orphelins jusqu'à 25 ans (études supérieures sans bourse), fille sans ressources. Art. 2 : prend effet à compter du 1er mai 1997. Absente du manuel de la CNRPS. Texte lu, contrôlé à l'image."},
  {"id":"decret96-1015","type":"legislation","title":"Décret n° 96-1015 du 27 mai 1996, fixant les modalités de la validation des services au titre des régimes de retraite, d'invalidité et de survivants","issued":{"date-parts":[[1996,5,27]]},"container-title":"Journal officiel de la République tunisienne","issue":"45","page":"1109-1110","URL":"https://www.pist.tn/jort/1996/1996F/Jo04596.pdf","note":"citation-key: decret96-1015\nJORT n° 45 du 4 juin 1996. Art. 5 : périodes validables ; études et formation non soumises à cotisation non validables. Art. 8 : délais. Art. 10 : demandes antérieures à la loi 95-105 liquidées selon l'ancienne législation. Aucune date d'effet. Texte lu."},
  {"id":"decretloi2022-49","type":"legislation","title":"Décret-loi n° 2022-49 du 16 août 2022, fixant des dispositions dérogatoires et conjoncturelles au profit des titulaires des pensions versées par la Caisse nationale de retraite et de prévoyance sociale","issued":{"date-parts":[[2022,8,16]]},"container-title":"Journal officiel de la République tunisienne","issue":"93","page":"2494","URL":"https://www.pist.tn/jort/2022/2022F/Jo0932022.pdf","note":"citation-key: decretloi2022-49\nJORT n° 93 du 19 août 2022 (pied de page), p. 2494 de l'édition française ; jort_cache donne 5/8 août et p. 2793 (arabe). Déroge à l'art. 37 al. 4 de la loi 85-12 : différentiel complémentaire jusqu'au 31 décembre 2022, suspension de la retenue de la part patronale de péréquation (augmentations 2019). Aucune date d'effet. Texte lu (couche texte)."},
  {"id":"decret2023-741","type":"legislation","title":"Décret n° 2023-741 du 1er décembre 2023, fixant les modalités et les procédures de l'augmentation optionnelle de l'âge de mise à la retraite","issued":{"date-parts":[[2023,12,1]]},"container-title":"Journal officiel de la République tunisienne","issue":"138","page":"3240-3242","URL":"https://www.pist.tn/jort/2023/2023F/Jo1382023.pdf","note":"citation-key: decret2023-741\nJORT n° 138 du 1er décembre 2023. Art. 2 : agents atteignant l'âge légal à compter du 1er décembre 2023. Art. 4-8 : demande entre un an et six mois avant, décision sous 30 jours, renonciation irrévocable. Art. 9 : art. 29 bis. Art. 10 : transitoire 2023, une année d'office. Aucune date d'effet. Notice jort_cache fautive (numero 2023-138). Texte lu (couche texte)."}
]
```

Ces entrées sont à porter d'abord dans `docs/notes/biblio-a-rapatrier.md` (§ 9, rappel d'outillage).

## 11.7 Ce qui reste non établi

- **Portée de la loi 95-105 sur l'art. 16 (nouveau) de 1988** (validation des études) : abrogation
  implicite ou coexistence — non tranchée.
- **Décret n° 2003-1656** (application de la loi 2002-61) : non lu.
- **Jouissance de la pension des mères avant 1989** : l'art. 41 de 1985 ne les range pas parmi les
  jouissances immédiates ; le régime applicable (différé à 50 ans comme départ sur demande ?) n'est
  écrit nulle part **[D]**.
- **Complétude** : bornée par l'indexation de `jort_cache.db` (§ 11.0). Les lois de finances
  antérieures à 2001 n'ont été examinées que sur leurs notices.
- **Traduction de l'art. 12 du décret-loi 2022-79** : de travail ; aucune version française
  officielle n'existe.

## 11 bis. Deux décrets de la chaîne du décret n° 74-499 (régime privé), lus

### Décret n° 96-326 du 1er mars 1996

JORT **n° 21 du 12 mars 1996, p. 530**, `/1996/1996F/Jo02196.pdf` **[T]** (lu à l'image ; page 78
du fichier local, pied de page « Page 530 — 12 mars 1996 — N° 21 »).

- **Article modifié** : **art. 46, alinéa premier**, du décret n° 74-499, abrogé et remplacé :
  « Toute demande de pension doit être formulée auprès de la caisse nationale de sécurité sociale
  dans un **délai maximum de cinq ans** à partir du jour où le bénéficiaire a atteint l'âge
  d'ouverture du droit à pension et a cessé son activité professionnelle assujettie, a été déclaré
  invalide ou est décédé ». C'est le seul article du décret touché.
- **Date d'effet** : **non énoncée** — l'art. 2 est une clause d'exécution et de publication.
- **Maillon** : ouverture du droit (procédure). L'ancien alinéa de 1974 n'a pas été relu pour cette
  note ; aucun effet sur les articles 17, 18, 29, 38 ou 53.

### Décret n° 97-1927 du 29 septembre 1997

JORT **n° 80 du 7 octobre 1997, p. 1851**, `/1997/1997F/Jo08097.pdf` **[T]** (lu à l'image, art. 2
recadré à 300 dpi).

- **Article modifié** : **art. 33** du décret n° 74-499, abrogé et remplacé (article premier) —
  pension temporaire d'orphelin jusqu'à 16 ans sans condition, 21 ans (études secondaires,
  techniques ou professionnelles), **25 ans** (études supérieures sans bourse universitaire),
  **la fille tant qu'elle ne dispose pas de ressources ou n'est pas à la charge de son mari**, sans
  limite d'âge en cas d'affection incurable ou d'infirmité ; même droit aux orphelins d'un
  bénéficiaire de pension d'invalidité ou d'un assuré remplissant les conditions de l'art. 21.
- **Le second article, qui n'avait pas pu être isolé, se trouve en tête de la colonne droite de la
  page** : « Art. 2. - Les ministres des affaires sociales et des finances sont chargés, chacun en ce
  qui le concerne, de l'exécution du présent décret **qui prendra effet du 1er mai 1997** et qui sera
  publié au *Journal Officiel* de la République Tunisienne. »
- **Date d'effet : 1er mai 1997** **[T]** — identique à celle de la loi n° 97-59 pour le secteur
  public : les deux régimes ont reçu la même extension des droits des orphelins à la même date.

---

# 12. La fenêtre du salaire de référence du RSNA : décrets n° 90-1455 et 94-1429

> Section ajoutée le 11 septembre 2026. Question posée : le chapitre privé expose deux calendriers
> de la fenêtre de dix ans (1990, puis 1994-1996) sans les concilier. Les deux décrets ont été relus
> **en entier**, ainsi que l'article 19 initial, le rectificatif de 1974, le décret n° 97-291 et le
> premier arrêté fixant le barème d'actualisation. Aucun `.qmd` n'a été modifié.

## 12.1 Conclusion

**Il n'y a pas de contradiction entre deux règles en vigueur au même moment, mais une succession.**
Le décret n° 94-1429 **abroge et remplace** l'article 18 dans la rédaction que lui avait donnée le
décret n° 90-1455, qu'il vise expressément. Aucun texte publié entre 1990 et 1994 n'a suspendu,
reporté ni modifié la règle de 1990. Ce que le décret de 1994 corrige est lisible dans les textes :
**le décret de 1990 avait réécrit l'article 18 (dix ans) sans toucher à l'article 19**, qui
continuait de prescrire une moyenne sur **trente-six ou soixante mois** ; le décret de 1994 réécrit
**les deux articles ensemble**, en paliers accordés (5, 7, 10 ans ; 60, 84, 120 mois).

Ce que les textes ne disent pas : **comment la caisse a liquidé les pensions entre le
23 septembre 1990 et le 30 juin 1994**, et pourquoi le décret de 1994 repart de cinq ans au lieu de
constater une fenêtre de dix ans déjà acquise. L'hypothèse d'une règle de 1990 restée inappliquée
est plausible — article 19 non adapté, aucun barème d'actualisation publié avant novembre 1994 —
mais **elle n'est pas établie** (§ 12.7).

## 12.2 Décret n° 90-1455 du 10 septembre 1990 — lecture intégrale

JORT **n° 60 du 21 septembre 1990, p. 1358**, édition française, `/1990/1990F/Jo06090.pdf`
(page 30 du fichier local, 32 pages ; fichier identique à l'octet à celui de pist.tn, 3 121 068
octets, contrôlé le 11 septembre 2026). Fascicule sans couche texte : OCR `tesseract -l fra` à
300 dpi, puis **relecture intégrale à l'image**. Pied de page lu à l'image : « 1358 — *Journal
Officiel de la République Tunisienne* — 21 septembre 1990 — N° 60 » (l'OCR lisait « 1356 » ; la page
précédente porte 1357). **[T]**

Le décret tient **entièrement sur la page 1358** : il s'ouvre sous l'intertitre « MINISTERE DES
AFFAIRES SOCIALES — REGIME DE VIEILLESSE » et se clôt par la signature, suivie de nominations
(décrets n° 90-1456 et suivants). Il compte **deux articles**.

**Intitulé** (fascicule) : « Décret N° 90-1455 du 10 septembre 1990 amendant le décret N° 74-499 du
27 avril 1974 relatif au regime de vieillesse, d'invalidité et de survivants dans le secteur non
agricole ». Le sommaire (p. 3 du fichier) porte « modifiant » et, par coquille, « 10 septembre
1980 ».

**Visas** **[T]** : loi n° 60-30 du 14 décembre 1960 (« ensemble les textes qui l'ont modifée ou
complétée, notamment la loi n° 88-38 du 6 mai 1988 ») ; loi n° 60-33 du 14 décembre 1960 ;
**décret n° 74-499 du 27 avril 1974**, visé sans mention d'aucun modificatif ; décret n° 76-981 du
19 novembre 1976 organisant la CAVIS ; avis des ministres de l'économie et des finances et des
affaires sociales ; avis du Tribunal administratif.

**Article premier** **[T]** : « Les dispositions des articles **3, 14, 18, 30, 32, 43 et 54** du
décret n° 74-499 du 27 avril 1974 sus-visé, sont abrogées et remplacées par les dispositions
suivantes : ». **L'article 19 n'est pas dans la liste.**

**Article 18 (nouveau), mot pour mot** **[T]** :

> « La pension est basée sur les salaires soumis à cotisation que l'assuré a perçu au cours des
> **dix dernières années** précédent l'âge d'ouverture du droit à pension. Au cas où la période
> d'activité déclarée est inférieure à 10 ans, la moyenne est calculée sur la base des salaires
> perçus au cours de cette période. Lesdits salaires ne sont pris en compte pour une durée
> déterminée que dans la limite de 6 fois le SMIG rapporté à une durée d'occupation annuelle de
> 2 400 heures. Ils sont actualisés selon un barème fixé par arrêté du ministre des affaires
> sociales. »

Coquilles du fascicule conservées (« perçu », « précédent »). Par rapport à 1974 : disparition du
choix « trois ou cinq dernières années […] selon que l'une ou l'autre de ces périodes de référence
est plus avantageuse », disparition de la mention « ou à allocation », « pour une année
déterminée » devenu « pour une durée déterminée », et ajout de l'actualisation par barème.

**Autres articles nouveaux** (lus, résumés) **[T]** : art. 3 (validation des périodes d'emploi non
déclarées ; cotisations calculées sur les salaires des trois dernières années ; périodes antérieures
au 1er avril 1961 validables dans un délai de trois ans « à compter de la date d'entrée en vigueur du
présent décret ») ; art. 14 (cessation de la relation de travail à l'âge de l'art. 15 ; périodes
postérieures prises en compte seulement après autorisation de l'inspection du travail et dans la
limite du stage) ; art. 30 (pension de survivant due si les liens du mariage existent au décès) ;
art. 32 (suspension en cas de remariage avant 55 ans, rétablissement revalorisé, cumul interdit,
seule la pension la plus élevée servie) ; art. 43 (versement unique pour moins de 60 mois de
cotisation) ; art. 54 (maintien des prestations de soins).

**Dispositions transitoires** : **aucune**. Pas de montée en charge, pas de date de liquidation à
partir de laquelle la règle s'applique, pas de report, pas de renvoi à un arrêté pour
l'entrée en application de l'article 18 (le renvoi à un arrêté porte sur le **barème**
d'actualisation seul).

**Article 2 (final)** **[T]** : « Les ministres de l'économie et des finances et des affaires
sociales sont chargés chacun en ce qui le concerne, de l'éxécution du présent décret qui sera publié
au journal officiel de la république Tunisienne. » — **clause d'exécution, aucune date d'effet.**
Le texte présuppose pourtant une date d'entrée en vigueur, qu'il nomme à l'article 3 (nouveau) sans
la fixer.

**Date d'effet — règle générale, calcul en clair** **[D]** : publication le **vendredi 21 septembre
1990** (pied de page). Règle applicable avant 1993 : exécutoire « un jour franc après la publication
au Journal Officiel » (art. 3 nouveau du décret du 27 janvier 1883, rédaction du décret du
13 septembre 1956, JORT n° 74/1956, p. 1247 — référence donnée par la convention de l'auteur, non
relue ici). Le jour de la publication ne compte pas ; le 22 septembre est le jour franc ; **le décret
est exécutoire à compter du dimanche 23 septembre 1990.** Que ce jour soit un dimanche ne change rien au calcul : la règle compte un jour franc, non un jour ouvrable, et la convention retenue ne prévoit aucun report.

**Édition arabe** **[T]** (lue à l'image, `/1990/1990A/Ja06090.pdf`, page 30 du fichier, 200
`application/pdf` 2 462 826 octets ; pagination imprimée non relevée) : même structure, même liste
d'articles. Art. 18 (جديد) : « تنبني الجراية على الأجور الخاضعة للمساهمة والتي قبضها المضمون أثناء
**العشر أعوام الأخيرة** السابقة للسن الذي يفتح الحق في الجراية » ; limite « في حدود ست مرات قيمة
الأجر الأدنى المهني المضمون قانونيا مرتبطا بمدة شغل سنوي تساوي 2400 ساعة » ; « ويعاد تقييم هذه
الأجور بقرار من وزير الشؤون الاجتماعية ». Le « الفصل 2 » est la même clause d'exécution. **Les deux
éditions concordent** : aucune clause propre à l'arabe.

## 12.3 L'article 19 que le décret de 1990 a laissé en place

Décret n° 74-499, **art. 19**, JORT n° 30/1974, **p. 917**, lu à l'image à 300 puis 500 dpi **[T]** :

> « Pour le calcul du salaire mensuel moyen, sont pris en considération dans leur ordre
> chronologique les **trente six ou soixante mois** écoulés à la date du 1er janvier de l'année au
> cours de laquelle l'assuré remplit la condition d'âge pour l'ouverture du droit à pension ou à
> allocation ou a cessé son activité professionnelle assujettie.
> Le salaire mensuel moyen est égal au 1/[36] ou au 1/[60] du total des salaires visés à l'article
> précédent, éventuellement augmentés du montant des salaires mensuels moyens ayant servi de base au
> calcul des prestations allouées sur le fondement des périodes d'assimilation énumérées à l'article
> 2 précédent. »

Les **dénominateurs de la fraction sont illisibles** sur le scan, même à 500 dpi ; « trente six ou
soixante mois », écrit en lettres au premier alinéa, est net. Les crochets signalent la lecture
dérivée.

**Rectificatif du décret n° 74-499** — JORT **n° 39 du 7 juin 1974, p. 1252**,
`/1974/1974F/Jo03974.pdf`, page 12 du fichier, lu à l'image **[T]**. Il ne corrige que deux renvois :
à l'**article 39** (p. 918), « la durée de stage minimum exigée à l'article **16** » se lit « à
l'article **15** » ; à l'**article 62, alinéa b)** (p. 919), « du dernier alinéa de l'article **62** »
se lit « de l'article **61** ». « (Le reste sans changement). » **Les articles 18 et 19 ne sont pas
touchés** : le point 7 du § 8 est clos pour ce texte.

**Conséquence** **[D]** : du 23 septembre 1990 au 30 juin 1994, la lettre du décret n° 74-499
associe un **article 18 à dix ans** et un **article 19 à trente-six ou soixante mois** — deux
règles qu'on ne peut pas exécuter ensemble à la lettre (dix années de salaires, divisées par 36 ou
par 60).

## 12.4 Décret n° 94-1429 du 30 juin 1994 — relecture intégrale

JORT **n° 52 du 5 juillet 1994, pp. 1141-1142**, `/1994/1994F/Jo05294.pdf` (pages 25-26 du fichier ;
couche texte à colonnes entremêlées, donc **relu à l'image**) **[T]**. Pieds de page : « N° 52 —
*Journal Officiel de la République Tunisienne* — 5 Juillet 1994 — 1141 » et « 1142 — … — N° 52 ».

**Intitulé** : « Décret n° 94-1429 du 30 juin 1994, portant amendement du décret n° 74-499 du
27 avril 1974 relatif au régime de pensions de vieillesse d'invalidité et de survivants dans le
secteur non agricole. »

**Visas** **[T]** : « Sur proposition du ministre des affaires sociales » ; loi n° 60-30 (« notamment
la loi n° 88-38 du 6 mai 1988 ») ; loi n° 60-33 ; **« Vu le décret n° 74-499 du 27 avril 1974
relatif au régime de pensions de vieillesse, d'invalidité et de survivants dans le secteur non
agricole tel que modifié par le décret n° 90-1455 du 10 septembre 1990 »** ; décret n° 76-981
« tel que modifié par le décret n° 78-962 du 7 novembre 1978 » ; avis du ministre des finances ;
avis du tribunal administratif.

**Article premier** **[T]** : « Les dispositions des articles **5 (b), 9, 18 et 19** du décret susvisé
n° 74-499 du 27 avril 1974 sont **abrogées et remplacées** par les dispositions suivantes : »
- art. 5 (b) nouveau : quote-part de **6,25/20e** de la masse des cotisations ;
- art. 9 nouveau : taux de **5,75 %** (2,5 % employeurs ; 3,25 % travailleurs, exigibles à 1,75 % au
  1er juillet 1994, 2,25 % au 1er juillet 1995, 2,75 % au 1er juillet 1996, 3,25 % au 1er juillet
  1997) ;
- **art. 18 nouveau**, mot pour mot :

> « La pension est basée sur les salaires soumis à cotisations que l'assuré a perçus au titre des
> périodes définies ci-après précédant l'âge d'ouverture de droit à pension :
> - les cinq dernières années à partir du 1er juillet 1994
> - les sept dernières années à partir du 1er juillet 1995
> - les dix dernières années à partir du 1er juillet 1996.
>
> Au cas où la période d'activité déclarée est inférieure aux périodes précitées, la moyenne est
> calculée sur la base des salaires perçus au cours de cette période.
> Lesdits salaires ne sont pris en compte pour une durée déterminée que dans la limite de 6 fois le
> SMIG régime 48 heures rapporté à une durée d'occupation annuelle de 2400 heures.
> Ils sont actualisés selon un barême fixé annuellement par arrêté du ministre des affaires
> sociales. »

- **art. 19 nouveau**, mot pour mot :

> « Pour le calcul du salaire mensuel moyen, sont pris en considération dans leur ordre
> chronologique, les soixante ou quatre vingt quatre ou cent vingt mois validiés au titre du régime
> de pension, écoulés à la date du 1er janvier de l'année en cours de laquelle l'assuré remplit la
> condition d'âge pour l'ouverture du droit à pension ou a cessé son activité professionnelle
> assujettie.
> Il n'est pas tenu compte pour le calcul du salaire moyen visé à l'alinéa précédent des périodes au
> cours desquelles l'assuré n'a pas exercé d'activité assujettie au versement de cotisation en vertu
> de la législation de sécurité sociale.
> Sous réserve des dispositions de l'alinéa 2 de l'article 18 du présent décret, le salaire mensuel
> moyen est égal au 1/60ème ou au 1/84ème ou au 1/120ème du total des salaires visés à l'article 18
> précédent, éventuellement augmentés du montant des salaires mensuels moyens ayant servi de base au
> calcul des prestations allouées sur le fondement des périodes d'assimilation énumérées à l'artricle
> 2 précédent. »

L'article 19 nouveau ne porte pas de dates : ses trois durées s'alignent **par construction** sur
les trois paliers de l'article 18 **[D]**. Il introduit une règle absente de 1974 : les périodes sans
activité assujettie sont neutralisées dans la moyenne.

**Article 2** **[T]** : « Les dispositions de l'article 5 - b (nouveau) du décret susvisé n° 74-499 du
27 avril 1974 prennent effet à compter du 1er janvier 1994. » — ne vise **que** l'art. 5 b).

**Article 3 (final)** **[T]** : clause d'exécution (« Les ministres des finances et des affaires
sociales sont chargés […] de l'exécution du présent décret qui sera publié au Journal Officiel »).

**Dispositions transitoires** : les seules sont les **paliers énoncés** dans les articles 9 et 18
nouveaux. **Rien sur les pensions liquidées entre 1990 et 1994**, rien sur la règle de 1990.

**Remplace-t-il ou reporte-t-il l'article 18 de 1990 ?** **Il le remplace.** Trois éléments du
texte : (1) le visa cite le décret n° 74-499 « tel que modifié par le décret n° 90-1455 », donc dans
sa rédaction de 1990 ; (2) l'article premier dit « abrogées et remplacées », non « suspendues » ni
« différées » ; (3) aucune disposition ne qualifie la règle de 1990 de non encore entrée en vigueur.
Le décret ne dit pas **pourquoi** il repart de cinq ans.

**Dates d'effet** :
- **fenêtre du salaire de référence** : **1er juillet 1994, 1er juillet 1995, 1er juillet 1996,
  énoncées** par l'art. 18 nouveau **[T]** ;
- **art. 5 b)** : 1er janvier 1994, énoncée par l'art. 2 **[T]** ;
- **pour le reste du décret, sans clause propre** **[D]** : règle de la loi n° 93-64, art. 2 — cinq
  jours après le dépôt du JORT au siège du gouvernorat de Tunis. Date de dépôt non imprimée dans le
  fascicule ; si le dépôt a eu lieu le 5 juillet 1994, date du fascicule, le décret est exécutoire
  **au plus tôt le 10 juillet 1994**. Le premier palier (1er juillet 1994) est donc antérieur à la
  date à laquelle le décret devient exécutoire : il est **rétroactif par ses propres termes**.

**Sens de « à partir du 1er juillet 1994 »** **[T]/[D]** : l'arrêté du 17 novembre 1994 (§ 12.5)
applique le barème « aux pensions pour lesquelles le droit est ouvert à compter du 1er juillet 1994 ».
Lecture cohérente : les paliers visent la **date d'ouverture du droit**.

## 12.5 Recherche des textes intermédiaires (1990-1994)

**Élément positif, le plus fort** **[T]** : le visa du décret n° 94-1429 énumère la chaîne
modificative du décret n° 74-499 et **s'arrête au décret n° 90-1455** ; le visa du décret n° 90-1455
vise le décret n° 74-499 sans modificatif. Aucun texte ne s'intercale selon ses propres auteurs.

**Corroboration par la base** **[M]** (`jort_cache.db`, `?immutable=1`, 11 septembre 2026) :
- `titre like '%74-499%'`, sans filtre d'année (1974-2026) : 16 notices — 74-499, son rectificatif,
  79-536, 81-188, 82-1030 et rectificatif, 88-1137, **90-1455**, **94-1429**, 96-326, 97-291, 97-555,
  97-1927, 2001-779, 2003-1212, 2007-2148. **Rien entre le 21 septembre 1990 et le 5 juillet 1994
  hormis ces deux décrets.**
- FTS `"non agricole" OR "90-1455" OR actualisation OR "74-499" OR "60-33"`, `jort_annee` 1990-1996 :
  90-1455, 93-357 (validation, travailleurs indépendants, sans rapport), 94-1429, puis les arrêtés
  de barème à partir du 17 novembre 1994.
- FTS `"74-499" OR ("non agricole" AND vieillesse) OR "salaire de reference" OR "salaire moyen"`,
  1990-2026 : même chaîne ; aucun texte postérieur au décret n° 2007-2148.
- `LIKE` non accentué, 1990-1996, sur `vieillesse`, `pension` + `non agricole`, `actualisation`,
  `caisse nationale de securite sociale`, `60-30` : communiqués et avis de simplification des
  formalités de la CNSS et de la CAVIS (1990-1991), décret n° 91-487 (commission médicale), loi
  n° 90-70 (coordination), décret n° 94-1477 (abrogation du décret n° 76-981) — **aucun ne vise
  l'article 18**. Titres seuls : le corps des communiqués de 1990-1991 n'a pas été lu.
- `rectificatif` + `vieillesse`/`1455`, 1990-1994 : **aucun rectificatif** du décret n° 90-1455.

**Barème d'actualisation** **[T]** : le premier arrêté identifié est l'**arrêté du ministre des
affaires sociales du 17 novembre 1994**, JORT **n° 93 du 25 novembre 1994, p. 1898**,
`/1994/1994F/Jo09394.pdf` (page 10 du fichier, lue à l'image). Visa : « le décret n° 74-499 du
27 avril 1974 […] ensemble les textes qui l'ont modifié ou complété notamment le décret n° 94-1429 du
30 juin 1994 et notamment son article 18 » — **aucune mention du décret n° 90-1455**. Tableau de
coefficients 1961 (6,48469) à 1993 (1,00000). Art. 2 : « Ces dispositions s'appliquent aux pensions
pour lesquelles le droit est ouvert à compter du 1er juillet 1994. » **Aucun arrêté de barème pris
en application de l'article 18 dans sa rédaction de 1990 n'a été trouvé** (FTS `actualisation`,
1990-1994).

**Décret n° 97-291** (dernier décret de la chaîne dont la neutralité sur l'article 18 restait à
établir) — JORT **n° 13 du 14 février 1997, pp. 203-204**, `/1997/1997F/Jo01397.pdf`, page 3 du
fichier, lu à l'image **[T]**. Article premier : « Les articles **29, 38 et 53 alinéa 4** du décret
n° 74-499 […] sont abrogés et remplacés » ; art. 2 : l'article **52** est abrogé ; art. 3 : clause
d'exécution. **Ni l'article 18 ni l'article 19.** Le point 5 du § 8 est clos : 94-1429 modifie les
articles 18 et 19, 96-326 et 97-291 n'y touchent pas. (Son visa cite « le décret n° **95**-326 du
1er mars 1996 » : coquille pour 96-326.)

Les autres modificatifs postérieurs ont été lus au § 2.0 (97-555 : art. 9 ; 97-1927 : art. 33 ;
2001-779 : art. 53 ; 2003-1212 : art. 5 b) ; 2007-2148 : art. 15 bis, 15 ter, 17, 33, 42, 47) :
**aucun ne touche les articles 18 ou 19**.

## 12.6 La série

| Du | Fenêtre | Diviseur (art. 19) | Limite de prise en compte | Texte | Date d'effet | Niv. |
|---|---|---|---|---|---|---|
| **1er janv. 1974** | 3 ou 5 dernières années, la plus avantageuse | 36 ou 60 mois | 6 × SMIG, 2 400 h/an, « pour une année déterminée » | 74-499, art. 18-19 (rectificatif sans objet) | énoncée, art. 64 | **[T]** |
| **23 sept. 1990** | 10 dernières années ; moyenne sur la période d'activité si moins de 10 ans ; actualisation par barème d'arrêté | **inchangé : 36 ou 60 mois** | 6 × SMIG, 2 400 h/an | 90-1455, art. 1 (art. 18 nouveau) | non énoncée ; exécutoire un jour franc après publication (21 sept. 1990) | texte **[T]**, date **[D]** |
| **1er juill. 1994** | 5 dernières années ; actualisation par barème annuel | 60 mois | 6 × SMIG régime 48 h, 2 400 h/an | 94-1429, art. 1 (art. 18-19 nouveaux) | énoncée, art. 18 nouveau | **[T]** |
| **1er juill. 1995** | 7 dernières années | 84 mois | idem | idem | énoncée | **[T]** ; diviseur aligné **[D]** |
| **1er juill. 1996** | 10 dernières années | 120 mois | idem | idem | énoncée | **[T]** ; diviseur aligné **[D]** |

**Close à ce jour dans la limite du corpus** : aucun texte de `jort_cache.db` postérieur au décret
n° 2007-2148 ne vise le décret n° 74-499.

## 12.7 Ce qui manque pour aller plus loin

- **La pratique de liquidation de la CNSS entre le 23 septembre 1990 et le 30 juin 1994** : les
  textes publiés au JORT ne la renseignent pas. Sources à chercher : circulaires ou notes de
  service de la CNSS (1990-1994), rapports annuels de la CNSS de ces années, travaux préparatoires
  ou avis du Tribunal administratif sur le projet de décret n° 94-1429, doctrine ou jurisprudence
  administrative sur des pensions liquidées dans cet intervalle. **TODO**.
- **Le corps des communiqués et avis du Premier ministère de 1990-1991** sur la simplification des
  formalités de la CNSS et de la CAVIS (JORT n° 70 et 71/1990, 79/1990, 2, 19, 27, 45/1991) : titres
  seuls ; improbable qu'ils touchent au calcul, non vérifié.
- **La date de dépôt du JORT n° 52/1994** au gouvernorat de Tunis : non imprimée ; la date exécutoire
  du décret n° 94-1429 (hors dates énoncées) reste « au plus tôt le 10 juillet 1994 ».
- **Les dénominateurs imprimés de l'article 19 de 1974** : illisibles ; restitués par le texte en
  lettres du premier alinéa.
- **L'édition arabe du décret n° 94-1429** n'a pas été relue.

## 12.8 Corrections à reporter ailleurs dans ce dossier (non faites ici)

- § 0 et § 6.3 : « 10 dernières années (1990) » → ajouter le remplacement de 1994 (5/7/10 ans au
  1er juillet 1994, 1995, 1996).
- § 2.0 : ligne 94-1429 — objet « art. 5 b), 9, 18 et 19 (nouveaux) », effet « art. 18 : paliers
  énoncés 1er juill. 1994/1995/1996 ; art. 5 b) : 1er janv. 1994 (art. 2) » ; ligne 97-291 — « art. 29,
  38, 53 al. 4 (nouveaux) ; art. 52 abrogé ; ni 18 ni 19 » ; ligne du rectificatif de 1974 — lu, art.
  39 et 62 b) seulement.
- § 2.1 : la limite de 6 × SMIG est reprise une **troisième** fois en 1994 (« SMIG régime 48 heures ») ;
  la série n'est plus « non close » sur ce point ; le barème d'actualisation est identifié (arrêtés
  annuels depuis le 17 novembre 1994).
- § 2.3 : ajouter les trois paliers de 1994 et l'article 19 non modifié en 1990.
- § 8 : points 5 et 6 clos ; point 7 clos pour le décret n° 74-499.

## 12.9 Références

**Clés existantes** : `decret74-499`, `decret90-1455`, `decret94-1429`, `decret97-291`,
`arrete-1997-03-29-bareme-actualisation`. Notes de `decret90-1455` et `decret94-1429` mises à jour
(FR et AR) le 11 septembre 2026.

**Entrée à créer** (citée par le § 12.5, utile si le rédacteur mentionne l'origine du barème) :

```json
{"id":"arrete-1994-11-17-bareme-actualisation","type":"legislation","title":"Arrêté du ministre des affaires sociales du 17 novembre 1994, relatif à la fixation du barème d'actualisation des salaires pris en compte dans le calcul des pensions de vieillesse, d'invalidité et de survivants","issued":{"date-parts":[[1994,11,17]]},"container-title":"Journal officiel de la République tunisienne","issue":"93","page":"1898","URL":"https://www.pist.tn/jort/1994/1994F/Jo09394.pdf","note":"citation-key: arrete-1994-11-17-bareme-actualisation\nJORT n° 93 du 25 novembre 1994, p. 1898. Premier barème pris en application de l'art. 18 (nouveau) du décret n° 74-499, issu du décret n° 94-1429 (visé). Coefficients 1961 (6,48469) à 1993 (1,00000). Art. 2 : s'applique aux pensions dont le droit est ouvert à compter du 1er juillet 1994. Lu à l'image."}
```

Vérification : `200 application/pdf 536 819` octets, identique au fichier local, 11 septembre 2026.

## 12.10 Paragraphe prêt pour le rédacteur

*Série à publier* (remplace les lignes 1990 et 1994-1996 de `tbl-rsna-reference`) :

| Depuis | Fenêtre de référence | Moyenne | Texte |
|---|---|---|---|
| 1er janvier 1974 | trois ou cinq dernières années, la plus avantageuse pour l'assuré | total divisé par 36 ou 60 mois | décret n° 74-499, art. 18-19 |
| 23 septembre 1990 | dix dernières années ; salaires actualisés selon un barème fixé par arrêté | article 19 non modifié : 36 ou 60 mois | décret n° 90-1455, art. 1 (art. 18 nouveau) |
| 1er juillet 1994 | cinq dernières années ; salaires actualisés selon un barème annuel | 60 mois | décret n° 94-1429, art. 1 (art. 18-19 nouveaux) |
| 1er juillet 1995 | sept dernières années | 84 mois | idem |
| 1er juillet 1996 | dix dernières années | 120 mois | idem |

La limite de prise en compte reste de six fois le SMIG rapporté à 2 400 heures par an sur toute la
période ; le décret de 1994 précise qu'il s'agit du SMIG du régime de 48 heures. La date du
23 septembre 1990 est celle à laquelle le décret n° 90-1455, qui n'énonce pas de date d'effet,
devient exécutoire, un jour franc après sa publication au *Journal officiel* du 21 septembre 1990.

*Articulation* : Le décret n° 90-1455 porte la fenêtre de référence à dix ans en réécrivant
l'article 18, mais laisse inchangé l'article 19, qui continue de calculer la moyenne sur trente-six
ou soixante mois ; le décret n° 94-1429, qui vise le décret de 1974 dans sa rédaction de 1990,
abroge et remplace ensemble ces deux articles et substitue à la règle de 1990 une montée
progressive, de cinq ans en 1994 à dix ans en 1996. Aucun texte publié entre ces deux décrets ne
suspend ni ne reporte la règle de 1990, et aucun n'indique comment les pensions ont été calculées
dans l'intervalle.

*Pour l'encadré « Deux décrets, deux calendriers »* : il peut céder la place à cette phrase
d'articulation ; le TODO « établir comment la règle de 1990 a été appliquée entre 1990 et 1994 »
reste ouvert (§ 12.7).

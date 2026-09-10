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
| Fenêtre du salaire de référence RSNA | **3 ou 5 dernières années**, la plus avantageuse (1974) → **10 dernières années** (1990) | 74-499 art. 18, puis 90-1455 | **[T]** |
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
| RSNA | **3 ou 5 dernières années**, la plus avantageuse (1974) → **10 dernières années** (1990) | 74-499 **art. 18-19** ; 90-1455 **art. 18 (nouveau)** | moyenne des **10 meilleures** années sur 40 |
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

11 bis. **Les onze lois de la chaîne modificative de la loi n° 85-12 n'ont pas été ouvertes**, à
   l'exception des lois n° 2007-43 et 2019-37 : lois n° 87-8, 88-71, 90-6, 94-71, 95-105, 96-67,
   97-74, 2001-123, 2002-61 et 2009-20. Leurs notices sont établies au § 10.2 ; leur contenu ne
   l'est pas. Il en va de même des textes de la coordination (lois n° 88-84 et 2003-8, décret
   n° 2003-1128), des textes de départ anticipé (loi n° 87-7, loi n° 2009-39, décret n° 2009-2085) et
   des deux décrets d'assiette (n° 85-980 et n° 85-1176).

9. **Deux dates d'effet manquent au dossier de la loi n° 83-31** (dernière page, p. 809, non ouverte)
   et **du décret n° 97-1927** (second article non isolable du découpage en colonnes du fascicule
   n° 80 de 1997 ; lecture à l'image nécessaire).

10. **Le décret n° 81-224 du 24 février 1981** — celui dont la date sert de date conventionnelle à
    tout le bloc RSA du modèle — **n'a pas été lu**. Son intitulé porte sur la répartition des
    cotisations, non sur les prestations ; la vérification reste à faire.

11. **La loi n° 88-71 du 27 juin 1988**, qui porterait de 15 à 20 ans l'âge des enfants ouvrant
    droit au départ anticipé des mères de trois enfants au CNRPS, **n'a pas été lue** ; seule sa
    notice (JORT n° 45 du 1er juillet 1988, pp. 967-968) est établie. C'est le dernier maillon
    non vérifié du § 1.1. *(La loi n° 2009-20, en revanche, a été lue : voir § 6.1 bis.)*

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

Onze textes. Aucun n'a été ouvert : **[M]** dans tous les cas, sauf les lois 2007-43 et 2019-37,
lues au § 1.

| Texte | Objet (intitulé du JORT) | Signature | JORT | Pages | URL |
|---|---|---|---|---|---|
| **Loi n° 87-8** | Institue des dispositions relatives au **travail des retraités** | 1987-03-06 | n° 18 du 10 mars 1987 | 364 | `/1987/1987F/Jo01887.pdf` |
| **Loi n° 88-71** | Modifie et complète la loi n° 85-12 | 1988-06-27 | n° 45 du 1er juill. 1988 | 967-968 | `/1988/1988F/Jo04588.pdf` |
| **Loi n° 90-6** | Modifie la loi n° 85-12 | 1990-02-12 | n° 14 du 20 févr. 1990 | 264 | `/1990/1990F/Jo01490.pdf` |
| **Loi n° 94-71** | Révision des taux de contribution aux régimes de retraite du secteur public | 1994-06-27 | n° 50 du 28 juin 1994 | 1086 | `/1994/1994F/Jo05094.pdf` |
| **Loi n° 95-105** | Institue un **système unique de validation des services** au titre des régimes légaux de vieillesse, d'invalidité et de survivants | 1995-12-14 | n° 101 du 19 déc. 1995 | 2308 | `/1995/1995F/Jo10195.pdf` |
| **Loi n° 96-67** | Modifie la loi n° 85-12 | 1996-07-22 | n° 60 du 26 juill. 1996 | 1604 | `/1996/1996F/Jo06096.pdf` |
| **Loi n° 97-74** | Amende la loi n° 85-12 | 1997-11-18 | n° 93 du 21 nov. 1997 | 2080 | `/1997/1997F/Jo09397.pdf` |
| **Loi n° 2001-123** | Loi de finances pour 2002 | 2001-12-28 | — | — | — |
| **Loi n° 2002-61** | Dispositions relatives à la protection sociale au profit de certains agents des entreprises et établissements publics à caractère non administratif | 2002-07-09 | n° 57 du 12 juill. 2002 | 1584-1585 | `/2002/2002F/Jo0572002.pdf` |
| **Loi n° 2007-43** | Voir § 1.0 — **lue** | 2007-06-25 | n° 51 | 2198-2199 | `/2007/2007F/Jo0512007.pdf` |
| **Loi n° 2009-20** | Dispositions exceptionnelles, retraite des professeurs de l'enseignement supérieur | 2009-04-13 | n° 30 du 14 avril 2009 | 1036 | `/2009/2009F/Jo0302009.pdf` |

**Deux textes de la loi n° 95-105 forment un couple** : la loi et son **décret n° 96-1015 du 27 mai
1996, fixant les modalités de la validation des services au titre des régimes de retraite,
d'invalidité et de survivants**, JORT n° 45 du 4 juin 1996, pp. 1109-1110 **[M]**. La validation est
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

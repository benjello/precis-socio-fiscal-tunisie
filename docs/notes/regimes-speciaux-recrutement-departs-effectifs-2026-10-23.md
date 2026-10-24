# Régimes spéciaux du secteur public : recrutement, départs, effectifs et masse salariale par mission

Note documentaire du 23 octobre 2026 (rôle documentaliste), pour le livre « Rémunérations
publiques » (branche `rediger/regimes-speciaux-secteur-public`). Elle ne modifie aucun fichier du
précis. Les chapitres lus pour ne pas dupliquer : `_regime_statutaire_autonome.qmd`,
`_regime_indiciaire.qmd`, `index.qmd`, `retraites/_secteur_public.qmd` (§ 2007, 2019, 2022-2023,
§ « dispositifs créés hors de la loi de 1985 », § 2009), `marche_travail/_politiques_emploi.qmd`
(chantiers).

Conventions de la note :

- « p. » = page imprimée. Pour les rapports du ministère des Finances et de la Cour des comptes, le
  numéro imprimé diffère du rang dans le fichier ; le décalage est donné en § 7.
- JORT : édition française quand elle existe ; sinon édition arabe, signalée « AR ». Adresses
  pist.tn selon la convention `/jort/<année>/<année>{F|A}/{Jo|Ja}<n°><année>.pdf`.
- Familles de chiffres (conventions, § 3) : **[B]** budgétaire (loi de finances, ministère des
  Finances, Cour des comptes quand elle rend compte de l'exécution) ; **[S]** statistique publique
  (INS, base administrative INSAF) ; **[E]** rapport extérieur (FMI, Banque mondiale). Aucune
  évaluation économique n'a été mobilisée.

---

## 0. Ce qui change par rapport aux chapitres actuels (à lire d'abord)

1. **Les effectifs et la rémunération par mission sont publiés au JORT depuis la loi de finances
   pour 2021.** La loi organique du budget n° 2019-15 (art. 45, 5e tiret des deux alinéas) impose
   que la loi de finances fixe « l'effectif global du personnel autorisé pour les ministères […]
   par mission » ; l'art. 70 rend la règle applicable « au plus tard à la fin de l'année 2020 »
   (JORT n° 15 du 19 février 2019, pp. 400-401 pour l'art. 45, p. 404 pour l'art. 70 ; clé
   existante `loi-org-2019-15-lob`). Chaque loi de finances depuis 2021 porte donc, à son art. 9,
   l'effectif autorisé total, et un tableau (« F » en 2021-2022, « ح » ensuite) par mission :
   Défense, Intérieur, Justice, Affaires étrangères, Cour des comptes, Conseil supérieur de la
   magistrature (§ 4.1). Le tableau « C » / « ت » donne les crédits de rémunération par mission, et
   avant 2020 par ministère (« Rémunérations publiques », première partie du titre I) (§ 4.2).
   → Les phrases du chapitre statutaire « Les effectifs et la masse salariale des corps de défense
   et de sécurité ne sont pas ventilés publiquement » (§ Vue d'ensemble, « Ce que l'on en mesure »,
   et § Repères budgétaires) sont contredites par ces tableaux, au moins au niveau de la mission.
   La mission ne se confond pas avec le corps : la mission Défense comprend des civils, la mission
   Intérieur porte aussi des programmes civils (affaires locales depuis 2022), la mission Justice
   les agents des prisons (corps des forces de sécurité intérieure) et les magistrats.
2. **Le champ de l'INS est probablement plus large que ce que disent les chapitres.** Le chapitre
   statutaire et le chapitre indiciaire (§ `sec-ventilation-ministere`) affirment que l'INS exclut
   militaires, agents des forces de sécurité intérieure et magistrats. Les chiffres disent autre
   chose, sans le trancher :
   - INS, Intérieur : 7 135 agents en 2011, 73 645 en 2012 (annexes annuelles de l'enquête
     2010-2021 ; `tunisia-data`, `ministere_effectifs_annexes_2010_2014.csv`) ; 99 826 en 2021 et
     96 146 en 2025 (rapport 2018-2025, tableau 8, p. 11) ;
   - loi de finances, effectif autorisé 2021 : Intérieur 98 362, Défense 91 365, Justice 18 878 ;
     INS 2021 : Intérieur 99 826, Défense 86 446, Justice 19 300 (§ 4.1 et 4.3) ;
   - l'INS écrit lui-même que la fonction publique « regroupe les agents chargés d'assurer le
     fonctionnement des administrations publiques dans des secteurs essentiels tels que
     l'éducation, la santé, la sécurité, la justice et l'administration territoriale » (rapport
     2018-2025, p. 3) et que « la structure des effectifs par ministère reste fortement concentrée
     autour des secteurs de l'éducation, de la sécurité, de la défense et de la santé » (p. 11).
   Le rapport ne définit pas son champ statutaire. La fiche de source de `tunisia-data`
   (`sources/ins-fonction-publique-salaires-2010-2021.md`, ligne 30) affirme que « le champ de
   l'enquête exclut les militaires de carrière » sans citer de source. **À trancher par le
   rédacteur avec l'INS** (méthodologie INSAF) ; ne pas réécrire le chapitre sur la seule base de
   ces rapprochements.
3. **Plusieurs prémisses du ticket ne sont pas confirmées par les textes** (§ 6) : pas de loi de
   2011 de titularisation des agents de chantier ; la loi n° 2012-27 est la loi de finances pour
   2013 ; aucun article de loi de finances « gelant » les recrutements n'a été trouvé ; pas de
   texte de départ volontaire propre à la fonction publique en 2014, 2015 ou 2019 ; pas de loi de
   départ volontaire propre aux entreprises publiques en 2019.
4. **Domiciles.** La mécanique des pensions (départs anticipés de 1987, 2009, 2017, 2022-2028) vit
   au livre « Retraites » ; les chantiers au livre « Marché du travail ». Le livre des
   rémunérations publiques reçoit : les règles de recrutement (statut général, régimes
   dérogatoires), la prime de départ volontaire de 2018 (indemnité de rupture versée par
   l'employeur, non pension), et les séries d'effectifs et de masse salariale. Ce qui est à verser
   ailleurs est regroupé en § 8.

---

## 1. Recrutement dans la fonction publique

### 1.1 La règle générale : statut général de 1983

Faits sourcés (loi n° 83-112 dans sa rédaction de 1983, JORT n° 82 des 13-16 décembre 1983,
p. 3216 ; clé `loi83-112` ; fascicule scanné, lu à l'image) :

- **Art. 17** : nul ne peut être nommé à un emploi de fonctionnaire de l'État, d'une collectivité
  locale ou d'un EPA s'il ne possède la nationalité tunisienne, ne jouit de ses droits civiques, ne
  se trouve en position régulière au regard du recrutement de l'armée, n'a 18 ans au moins, et ne
  remplit les conditions d'aptitude physique et mentale.
- **Art. 18** (catégories A, B et C) : dans la limite de 50 % des emplois à pourvoir, recrutement
  externe — A) nomination directe des élèves issus d'une école de formation agréée, B) concours
  externes sur épreuves ouverts aux titulaires du diplôme requis ; dans la limite de 50 %,
  promotion interne — 40 % parmi les fonctionnaires ayant suivi un cycle de formation ou par
  concours interne (cinq ans d'ancienneté dans le grade inférieur), 10 % par promotion au choix
  (40 ans d'âge et 10 ans d'ancienneté), une seule fois dans la carrière.
- **Art. 19** : catégorie D recrutée par concours sur épreuves.
- **Art. 20** : le candidat admis qui refuse le poste attribué est, après mise en demeure, radié de
  la liste.
- **Art. 2** (p. 3215) : les statuts particuliers des services actifs de la douane, des forêts, du
  contrôle général des services publics et des finances, des corps médical et techniques peuvent
  déroger au statut général.

Lacune : rédaction actuelle des art. 17-20 (modifications ultérieures non vérifiées ; § 10, point 5).

Textes de procédure repérés par intitulé (non lus) : décret n° 82-1229 du 2 septembre 1982,
dérogations pour la participation aux concours externes (JORT n° 59/1982, p. 1885), complété par
le décret n° 92-1551 du 28 août 1992 (JORT n° 61/1992, p. 1195) ; décret n° 2006-1031 du 13 avril
2006, âge maximum des titulaires de diplômes de l'enseignement supérieur pour les concours
externes (JORT n° 32/2006, pp. 884-885). Les deux derniers sont cités dans les visas du décret
n° 2011-544, qui renvoie à leur dérogation d'âge au vu de la date de première inscription au
bureau de l'emploi (art. 3).

### 1.2 Antécédent : les recrutements « exceptionnels et temporaires » de 1957-1969

Repérés par intitulé dans `jort_cache` (non lus) : décret du 28 janvier 1957 « fixant des règles
exceptionnelles et temporaires de recrutement d'administrateurs du gouvernement tunisien » (JORT
n° 9/1957, pp. 118-119), puis une série continue de décrets du même objet jusqu'en 1969
(administrateurs, ingénieurs principaux, secrétaires et attachés d'ambassade, PTT, RTT, etc. :
décrets n° 58-253, 59-67, 59-220, 60-361, 62-311, 63-271, 65-355, 66-337, 67-200, 69-377…). C'est
l'antécédent de la dérogation au concours pour pourvoir l'administration nationale après 1956. À
citer comme tel seulement après lecture d'un ou deux de ces textes.

### 1.3 Les régimes dérogatoires de recrutement depuis 2011

| Date (texte) | Texte | Contenu | Corps spéciaux | Source |
|---|---|---|---|---|
| 27 avril 2011 | décret-loi n° 2011-32 | Le programme des recrutements autorisés dans le secteur public pour 2011 se fait par **concours externes sur dossiers**, ouverts « au profit des candidats en chômage » (art. 1-2) ; classement par l'année d'obtention du diplôme, l'âge, la situation familiale, la mention, les stages (art. 3) ; dérogation limitée au programme de 2011 (art. 5). | Visas : statuts des militaires, des magistrats, de la Cour des comptes, du Tribunal administratif, des FSI, de la loi 85-78, des douanes | JORT n° 30 du 29 avril 2011, pp. 572-573 |
| 14 mai 2011 | décret n° 2011-544 | Attestation d'inscription au bureau de l'emploi (art. 1) ; dossier (art. 3) ; épreuve orale ou pratique possible, note dossier 70 % / épreuve 30 %, priorité au plus âgé (art. 7, 9) ; liste complémentaire ≤ 50 % (art. 11). Barème annexé : année de sortie 30 points = (2011 − année) × 2 ; âge 20 points (20-40 ans : âge − 20) ; situation familiale 10 ; mention 20 ; stages 20 (0,5 point par mois). | mêmes visas | JORT n° 35 du 17 mai 2011, pp. 716-719 (annexe p. 719) ; rectificatif JORT n° 44/2011 |
| 22 juin 2012 | loi n° 2012-4 | Concours externes sur dossiers et sur épreuves pour les chômeurs et les candidats exerçant une activité ne correspondant pas à leur diplôme (art. 1) ; au moins 70 % des postes classés sur l'âge et l'année du diplôme puis épreuve, au plus 30 % sur épreuves (art. 2) ; **recrutements directs** hors concours : un membre de chaque famille des martyrs de la révolution, les blessés de la révolution, les bénéficiaires de l'amnistie générale (décret-loi n° 2011-1) ou un membre de leur famille, les handicapés (art. 3) ; un membre de chaque famille dont tous les membres sont chômeurs, dans la limite de 5 % (art. 4) ; dérogation d'âge de 10 ans, plafond 50 ans, maintien possible jusqu'à 65 ans pour ouvrir le droit à pension (art. 5) ; représentants syndicaux et membres de l'ANC admis aux jurys (art. 6) ; dérogation d'un an (art. 9). | — | JORT n° 50 du 26 juin 2012, pp. 1531-1532 |
| 20 juillet 2012 | décret n° 2012-833 | Application : comité mixte Présidence du gouvernement / ministère des droits de l'Homme et de la justice transitionnelle pour les recrutements directs (art. 4) ; 1 % des postes pour les handicapés (art. 2) ; barème du concours sur dossiers (4 points par année depuis le diplôme, 2 points par année d'âge depuis 20 ans ; art. 8). **Art. 3 : ne s'applique pas aux corps des militaires, des FSI, des agents des services douaniers, des magistrats judiciaires et militaires, des membres de la Cour des comptes et du Tribunal administratif**, ni aux enseignants-chercheurs, corps médicaux et paramédicaux, enseignants, diplomates. | exclus (art. 3) | JORT n° 58 du 24 juillet 2012, pp. 1707-1711 |
| 13 décembre 2012 | décret n° 2012-3256 | Procédures de réintégration des agents publics bénéficiaires de l'amnistie générale et régularisation de leur situation administrative (intitulé seul ; non lu). | ? | JORT n° 100/2012 (FR absente du corpus et de pist.tn ; AR à lire) |
| 21 mars 2016 | décret gouvernemental n° 2016-372 | Dispositions exceptionnelles pour les concours externes de 2016 « autorisés par la loi n° 2015-53 » (LF 2016) : conditions fixées par décision du ministre nonobstant les statuts particuliers (art. 2) ; publicité à l'ANETI, au site du ministère et dans trois quotidiens (art. 3-5) ; deux observateurs de la société civile dans les jurys (art. 6) ; contrôle a posteriori de la DGAFP (art. 7) ; validité jusqu'au 31 décembre 2016 (art. 8). | — | JORT n° 24 du 22 mars 2016, pp. 879-880 |
| 13 août 2020 | loi n° 2020-38 | Recrutement direct, **par tranches annuelles**, hors concours : diplômés du supérieur chômeurs depuis dix ans et plus (art. 1) ; diplômés chômeurs de 35 ans et plus dont le chômage n'atteint pas dix ans (art. 2) ; un membre de chaque famille dont tous les membres sont chômeurs (art. 3) ; classement par âge et année du diplôme, formation préalable ; 5 % au moins des recrutements annuels de la fonction publique réservés aux handicapés (art. 4) ; exécution en quatre ans au plus (art. 6) ; décrets gouvernementaux d'application prévus aux art. 1-3. | — | JORT n° 82 du 19 août 2020, p. 1763 |
| 23 décembre 2020 | LF 2021, art. 12 | « En application de la loi n° 2020-38 […] des crédits sont alloués pour le recrutement de dix mille (10000) chômeurs diplômés de l'enseignement supérieur », financés par des économies sur certaines missions et par une part des crédits du programme emploi (CIVP, formation). | — | JORT n° 128 du 25 décembre 2020, p. 3125 (`lf-2021`) |
| 7 juin 2021 | loi n° 2021-27 | Ajoute à la loi n° 83-112 un **art. 18 bis** : le concours ne s'applique pas au recrutement direct des ouvriers de chantiers de plus de 45 ans (âge diminué de la durée des services comme ouvrier de chantier) ; l'État régularise ceux qui ont entre 45 et 55 ans au 20 octobre 2020, par tranches annuelles ou par un « chèque de départ » pour ceux qui choisissent le départ volontaire ; ce mode de recrutement cesse ensuite ; décret gouvernemental ; exécution en cinq ans. | — | JORT n° 50 du 11 juin 2021, p. 1505 |
| 21 septembre 2023 | décret n° 2023-591 | Audit général des recrutements et intégrations effectués du 14 janvier 2011 au 25 juillet 2021 dans la fonction publique, les instances, les établissements et entreprises publics, les banques publiques, la BCT, les sociétés à participation publique et l'ARP (art. 1) ; comité de pilotage présidé par le chef du gouvernement (art. 2) ; comités d'audit du CGSP, du CGF et du contrôle général des domaines (art. 4). Délai de l'art. 6 prorogé par le décret n° 2024-86. Les visas énumèrent les textes de recrutement de la période : DL 2011-32, DL 2011-70, loi 2012-4, décret 2012-833, décret 2016-372, décret 2019-291 (municipalités). | visas : statuts militaires, magistrats, FSI, douanes, prisons (loi 2001-51) | AR : JORT n° 108 du 22 septembre 2023, pp. 5288-5289 s. ; décret 2024-86 : JORT n° 16/2024, p. 471 |
| 11 décembre 2023 | LF 2024, art. 12 | Remplace l'al. 3 de l'art. 18 bis : l'État régularise les ouvriers de chantiers de 45 à 55 ans **par trois tranches de 2024 à 2026**, avec une prime de départ pour ceux qui choisissent de partir. | — | AR : JORT n° 144 du 12 décembre 2023, p. 6438 (`lf-2024`) |
| 22 décembre 2025 | loi n° 2025-18 | Recrutement exceptionnel des diplômés du supérieur en chômage de longue durée, supervisé par le ministère de l'emploi (art. 1) ; plateforme numérique, classement : âge (priorité au-delà de 40 ans), diplôme de plus de dix ans, un membre par famille, situation sociale (art. 2) ; conditions : inscription au bureau de l'emploi, aucune régularisation antérieure, pas d'affiliation continue à un régime de retraite, pas d'identifiant fiscal l'année précédente, pas de prêt de plus de 40 000 dinars (art. 3) ; recrutement sur dossier puis qualification (art. 4) ; par tranches sur trois ans au plus (art. 6). | — | JORT n° 153 du 23 décembre 2025, p. 3609 (traduction « pour information ») |
| 12 décembre 2025 | LF 2026, art. 57 | Crédits de 2026 pour la première tranche des diplômés chômeurs de longue durée, après publication des textes d'application de la proposition de loi n° 2023/23 (devenue loi 2025-18), selon l'art. 21 de la LOB ; procédures par décret. | — | AR : JORT n° 148 du 12 décembre 2025, p. 4244 (`lf-2026`) |

Autres articles de la LF 2026 repérés par l'index (intitulés seuls, AR pp. 4255 et 4258, non lus) :
art. 90 (recrutement des agents de la « آلية 16 » non en exercice), art. 92 (recrutement des
inscrits sur les listes d'attente d'aide-soignant au ministère de la Santé), art. 108
(titularisation des agents des communes nouvelles recrutés par le programme spécial de renforcement
des ressources humaines, circulaire du ministre de l'Intérieur n° 1 du 3 mars 2023).

Ce que les textes cherchent, dans leurs mots :

- DL 2011-32 : des concours « ouverts au profit des candidats en chômage » (art. 2).
- Loi 2020-38 : le recrutement direct de ceux qui sont « au chômage depuis dix ans et plus » (art. 1).
- Loi 2025-18 : « le règlement de la situation des diplômés de l'enseignement supérieur en chômage
  de longue durée a lieu par voie de recrutement exceptionnel » (art. 1).

Contexte (mots des sources budgétaires, à distinguer de ce que la loi cherche) : le rapport sur le
budget de l'État pour 2022 annonce le « عدم تفعيل القانون عدد 38 لسنة 2020 » (non-activation de la
loi n° 2020-38) et le gel des recrutements « dans la mesure du possible » sauf diplômés des écoles
de formation et secteurs prioritaires (`minfin-rapport-budget-2022`, pp. 21 et 37) ; la Cour des
comptes note que l'application de la loi 2020-38 a été « reportée pour la deuxième année »
(`cdc-loireg-2022`, p. 70).

### 1.4 Le « gel » des recrutements : ce que disent les sources

Aucun article de loi de finances suspendant les recrutements n'a été trouvé (fiche proposée
`r-lf-gel-recrutements-2017-2026`, § 9). Le gel se lit dans :

- **[E]** FMI, *Tunisia: Request for an Extended Arrangement under the EFF*, Country Report
  n° 16/138 (juin 2016), MEFP ¶ 20, p. 69 : « Maintaining the hiring freeze in all ministries
  through the next three years, with the exception of urgent needs for security and defense
  personnel » ; « reducing staff numbers (including by voluntary separations and no replacement of
  those who leave) » ; objectif d'une masse salariale de « 12 percent of GDP in 2020 (53 percent of
  tax revenues) ». Encadré 4, p. 18 : « The Tunisian government has already announced a three-year
  hiring freeze, with the exception of ongoing regularization of past contractual workers ». Le
  rapport ne précise pas la base du PIB ; en 2016 l'INS publiait le PIB en base 1997.
  Les chiffres de l'encadré (prime salariale de 18,5 % sur le privé, 37 indemnités spécifiques et
  plus de 140 indemnités spéciales, « about 60 percent of the average salary ») sont donnés sans
  méthode : « méthode non décrite par la source », ou à écarter.
- **[B]** rapports sur le budget de l'État : 2022 (pp. 21, 37 : gel sauf écoles et secteurs
  prioritaires ; pas de remplacement des départs ; redéploiement ; non-activation de la loi
  2020-38) ; 2024 (pp. 48 et 70 : « mesures urgentes » — recrutements limités aux secteurs
  prioritaires, « réduction progressive du nombre de diplômés des écoles de formation notamment
  pour les ministères de la Défense, de l'Intérieur et de la Justice », promotions annuelles ≤ 20 %,
  pas de remplacement des vacances) ; 2025 (p. 72 : mêmes orientations, promotions ≤ 40 %).
- **[B]** Cour des comptes, rapport sur la clôture du budget 2023, p. 63 : la circulaire du chef du
  gouvernement n° 9 du 20 mai 2022 (préparation du budget 2023) prescrit de limiter les
  recrutements aux besoins avérés et prioritaires, de réduire progressivement les diplômés des
  écoles de formation (Défense, Intérieur, Justice), de ne pas remplacer les vacances.

Pour les corps spéciaux, la règle qui ressort des rapports budgétaires est l'inverse d'un gel : les
diplômés des écoles de formation de la Défense, de l'Intérieur et de la Justice sont la principale
exception, et la part la plus forte des recrutements prévus (§ 5).

---

## 2. Plans de départ : retraite avant l'âge légal et départ volontaire

Domicile : pensions au livre « Retraites » ; la prime de départ volontaire (2018) relève du livre
des rémunérations publiques. Les textes de 2009 et 2022 sont déjà au livre « Retraites » ; ce qui
suit les complète.

### 2.1 Antécédent de 1987 : retraite anticipée volontaire (ajustement structurel)

Loi n° 87-7 du 6 mars 1987 (JORT n° 18 du 10 mars 1987, pp. 363-364 ; clé `loi87-7` ; scan lu à
l'image) :

- système applicable au secteur public **et** au privé ; mises à la retraite effectuées jusqu'au
  31 décembre 1987 (art. 1) ;
- éligibles : agents à moins de cinq ans de l'âge normal ayant la période minimale de cotisation,
  ou justifiant de 30 ans de cotisation quel que soit leur âge, en accord avec l'employeur ; pour
  les agents relevant de la loi 85-12, arrêté du ministre de la fonction publique (art. 2) ;
- contingent fixé par arrêté du Premier ministre (art. 3) ; bonification égale à la période
  restant à courir, plafonnée à cinq ans ; pension immédiate (art. 4) ;
- l'employeur doit présenter un **programme de recrutement en remplacement** (art. 5) ; à défaut,
  il rembourse à la caisse les pensions majorées des cotisations (art. 6) ; suspension de la
  pension en cas de reprise d'activité salariée (art. 7) ;
- financement par le produit de l'intégration des indemnités complémentaires provisoires (art. 49
  de la LF 1987) (art. 8).

Décret n° 87-337 du 6 mars 1987 (même JORT, pp. 369-370) : critères de priorité (emplois à
pourvoir en remplacement, profil des recrutés, situation de l'emploi du secteur ; période restant
jusqu'à l'âge légal, ancienneté) ; commission auprès du ministre de la fonction publique ; obligation
de recruter dans le mois suivant la mise à la retraite (art. 8).

Même jour : loi n° 87-8 interdisant l'emploi de retraités dans le secteur public et le cumul
pension-salaire permanent dans le privé (même JORT, p. 364) ; décret n° 87-338 (travaux
occasionnels permis, p. 370).

Ce que le texte cherche : libérer des postes pour recruter (art. 5 et décret 87-337). Contexte
1986-1987 (plan d'ajustement structurel) : à documenter par les sources de l'époque (rapport du
VIIe plan, débats de la Chambre du 3 mars 1987) — non lus.

Antécédent plus ancien repéré : décret n° 85-762 du 22 mai 1985, conditions d'application de la
« disponibilité spéciale » (JORT n° 43/1985, pp. 786-787) ; loi n° 2003-16 et décret
n° 2003-1543 régularisant ces périodes au regard de la sécurité sociale. Non lus.

### 2.2 2009 : mise à la retraite avant l'âge légal

Déjà traité au livre « Retraites » (§ `sec-cnrps-retraite-avant-age-2009`) : loi n° 2009-39,
décret n° 2009-2085, LFC 2009 ; 2 690 départs pour un plafond de 7 000.

### 2.3 2014 : Tunisie Télécom (entreprise publique)

Loi n° 2014-48 du 24 juillet 2014 (JORT n° 60 du 25 juillet 2014, p. 1916) : agents titulaires de
la société nationale des télécommunications âgés d'au moins 50 ans, 15 ans de services soumis à
retenue (art. 1) ; commission de la société statuant selon des critères du conseil d'administration
(art. 2) ; départs dans les trois ans de la publication (art. 3) ; pension immédiate bonifiée
jusqu'à l'âge légal (art. 4) ; pensions et contributions à la charge de la société, **déductibles
de l'assiette de l'impôt sur les sociétés** (art. 5). Décret n° 2015-85 du 24 avril 2015 (JORT
n° 34/2015, pp. 866-869 ; non lu). Domicile : livre « Entreprises publiques » ou « Retraites ».

### 2.4 2017 : mise à la retraite avant l'âge légal dans la fonction publique

Loi n° 2017-51 du 28 juin 2017, « portant dispositions dérogatoires de mise à la retraite avant
l'âge légal dans la fonction publique » (JORT n° 53 du 4 juillet 2017, p. 2303 ; AR pp. 2126-2127) :

- agents de la fonction publique atteignant l'âge légal du **1er janvier 2018 au 1er janvier 2021**
  (art. 1) ; agents et ouvriers ayant la période minimale de service ; demande dans les trois mois
  de la publication (art. 2) ;
- accord de principe du ministre, puis commission spéciale à la Présidence du gouvernement ; « les
  demandes soumises à la commission sont réputées définitives » (art. 3) ; critère : « le maintien
  de l'équilibre de la structure des ressources humaines du secteur public » ; rejet motivé
  (art. 4) ;
- pension immédiate, bonification égale à la période restant jusqu'à l'âge légal, non cumulable
  avec une activité déclarée à un autre régime après le départ (art. 5) ; pensions et
  contributions à la charge de l'employeur (art. 6).

Décret gouvernemental n° 2017-825 du 28 juillet 2017 (AR : JORT n° 59-60 des 25-28 juillet 2017,
pp. 2380-2381) : demande écrite dans les trois mois avec pièces sur la situation sociale et la
santé (art. 2) ; transmission sous quinze jours (art. 4) ; commission présidée par le directeur
général des services administratifs et de la fonction publique, avec les Finances, les Affaires
sociales, la structure et la CNRPS (art. 5) ; liquidation selon la loi 85-12 avec bonification
(art. 9). Les visas citent les statuts des militaires, des magistrats, de la Cour des comptes, du
Tribunal administratif, des FSI et des douanes ; aucun article ne les nomme.

### 2.5 2018 : départ volontaire des agents publics (prime de départ)

Loi n° 2018-5 du 23 janvier 2018, relative au départ volontaire des agents publics (AR : JORT n° 8
du 26 janvier 2018, pp. 288-289 ; `jort_cache` donne « p. 265 », pagination non retrouvée ;
l'édition française n'est ni dans le corpus — le fichier « fr » est l'arabe — ni sur pist.tn) :

- à titre exceptionnel, les agents publics soumis aux différents statuts généraux peuvent demander
  le départ volontaire contre une prime ; **la loi s'applique aux agents de la fonction publique
  et des établissements et entreprises publics** (art. 1) ;
- condition : cinq ans au moins d'activité effective soumise à retenue pour la retraite (CNRPS ou
  CNSS) à la clôture des demandes (art. 2) ;
- demande au ministre, accord préalable, commission spéciale à la Présidence du gouvernement,
  décisions définitives sans recours (art. 3-4) ;
- **prime forfaitaire égale à 36 salaires mensuels nets**, versée en une fois par l'employeur
  d'origine, sur la base du dernier salaire net ; exonérée de l'IRPP et de la retenue à la source ;
  **plafonnée à 50 % des salaires nets que l'agent aurait perçus jusqu'à l'âge légal** (art. 5) ;
- couverture santé d'un an (art. 6) ; départ définitif, interdiction de réemploi par l'État, les
  collectivités, les établissements et entreprises publics (art. 7) ; pension ou allocation de
  vieillesse à l'âge légal selon la législation en vigueur (art. 8) ; décret gouvernemental
  (art. 9) ; entrée en vigueur à la publication (art. 10).
- Travaux préparatoires : ARP, séance du 10 janvier 2018.

Décret gouvernemental n° 2018-205 du 23 février 2018 (AR : JORT n° 17 du 27 février 2018,
pp. 579-581) : champ de l'art. 1 al. 2 (État, collectivités, EPA, établissements et entreprises
publics) ; demandes dans les deux mois d'une date fixée par arrêté (art. 2) ; comité technique dans
chaque structure, avis selon la répartition des agents et « les équilibres du secteur » (art. 3) ;
commission spéciale à la Présidence du gouvernement présidée par le secrétaire général du
gouvernement (art. 4-5) ; prime de 36 mois nets plafonnée à 50 % (art. 8-9) ; CNAM pendant un an
(art. 10) ; capital-décès (art. 13) ; convention-cadre FNE / ANETI / BTS pour l'accompagnement des
porteurs de projets (art. 14) ; réouverture possible par arrêté (art. 15). Visas : statuts des
militaires, des magistrats, de la Cour des comptes, du TA, des FSI, des douanes.

Arrêtés du chef du gouvernement fixant les délais :

| Tour | Demandes | Décision des ministres | Commission | Source |
|---|---|---|---|---|
| 1er (2018) | 1er mars - 30 avril 2018 | 2-31 mai 2018 | 1er-30 juin 2018 | arrêté du 23 février 2018, AR : JORT n° 17/2018, p. 582 |
| 2e (2018) | 2 juillet - 30 août 2018 | 31 août - 28 septembre 2018 | 1er-30 octobre 2018 | arrêté du 7 mai 2018, AR : JORT n° 39 du 15 mai 2018, p. 1769 |

Contexte [E] : FMI CR 16/138, p. 16 : « incentives for targeted voluntary departures in 2018 »
dans la stratégie de réforme de la fonction publique. Nombre de bénéficiaires : non trouvé dans
une source officielle (§ 9, lacune) ; la presse donne des chiffres d'objectifs et de demandes,
non des réalisations.

### 2.6 2022-2028 : programme spécifique de mise à la retraite avant l'âge légal

- LF 2022 (DL n° 2021-21), art. 14 (JORT n° 119 du 28 décembre 2021, p. 3083 ; `lf-2022`) :
  agents âgés d'au moins 57 ans du 1er janvier 2022 au 31 décembre 2024, période minimale de
  service ; pension immédiate bonifiée jusqu'à 62 ans ; charge de l'employeur ; catégories et
  procédures par décret présidentiel. (Déjà au livre « Retraites ».)
- **Décret présidentiel n° 2022-542 du 13 juin 2022** (JORT n° 68 du 14 juin 2022, pp. 1898-1899 ;
  absent de l'index `jort_cache` par numéro et par intitulé) : 15 ans de service ; **exclus** : les
  agents des collectivités locales, des entreprises et établissements publics non administratifs
  (même soumis à la loi 83-112) et des instances publiques et constitutionnelles (art. 2) ;
  commission dans chaque ministère présidée par le ministre (art. 5-6) ; priorité aux agents en
  congé de maladie de longue durée ou en disponibilité d'office pour raison de santé, et à ceux qui
  ont à charge un descendant ou ascendant handicapé (art. 8) ; départ à 57 ans au moins (art. 10) ;
  pensions et contributions à la charge de l'employeur jusqu'à 62 ans (art. 11) ; commission
  centrale de suivi (art. 13).
- Arrêtés de délais (demandes par la voie hiérarchique) : 2022 à partir du 20 juin 2022 (JORT
  n° 69 du 17 juin 2022, p. 1926) ; 2023 à partir du 1er janvier 2023 (JORT n° 4/2023, p. 34) ;
  2024 à partir du 1er janvier 2024 (JORT n° 145/2023, p. 3653) ; 2025 à partir du 1er janvier 2025
  (JORT n° 159 du 31 décembre 2024, p. 3784).
- **LF 2025, art. 14** (AR : JORT n° 149 du 10 décembre 2024, p. 6420 ; `lf-2025`) : « يتواصل
  العمل بأحكام الفصل 14 من المرسوم عدد 21 لسنة 2021 […] وحسب نفس الشروط والإجراءات والصيغ […]
  خلال الفترة الممتدة بين 1 جانفي 2025 إلى 31 ديسمبر 2028 » — prolongation aux mêmes conditions
  **du 1er janvier 2025 au 31 décembre 2028**. Le rapport sur le budget 2025 (p. 72) écrit « jusqu'à
  la fin de 2027 » : la loi fait foi ; signaler l'écart.
- [B] Prévision du ministère (rapport budget 2022, p. 42) : « قرابة 6000 عون خلال سنة 2022 »
  (environ 6 000 agents en 2022), économie annuelle de 168 MD sur la masse salariale (84 MD en
  2022, départs à partir du 1er juillet 2022), coût 2022 de 192 MD au titre des interventions
  (pensions 66 MD pour six mois, coût d'exécution 126 MD) ; même chiffrage, p. 45 (« برنامج التقاعد
  المبكر » : 192 MD). La Cour des comptes reprend ces prévisions (`cdc-loireg-2022`, p. 70) sans
  donner de réalisation.

### 2.7 Autres instruments de réduction ou de redéploiement

- **Congé pour création d'entreprise** (art. 50 bis de la loi 83-112) : décret n° 2003-1617 du
  16 juillet 2003 (procédures ; JORT n° 58/2003, pp. 2339-2340 ; non lu) ; LF 2022, art. 15 (JORT
  n° 119/2021, p. 3083) : nouvel art. 50 bis — congé de trois ans au plus renouvelable une fois ;
  couverture sociale pendant les trois premières années sans avancement ni promotion ; demi-salaire
  la première année, deux ans en zone de développement régional. Le rapport budget 2022 (p. 42)
  le présente comme mesure de maîtrise de la masse salariale.
- **Mobilité fonctionnelle** : décret présidentiel n° 2022-387 du 18 avril 2022 (JORT n° 45/2022,
  pp. 1170-1173 ; intitulé seul). Cité par les rapports budget 2024 (p. 49) et 2025 (p. 72) parmi
  les « برامج مستحدثة للتخفيض من عدد الأعوان » (programmes de réduction des effectifs).
- **Option de prolongation soumise à l'employeur** (LF 2023, art. 12 ; décret 2023-741) : déjà au
  livre « Retraites » ; le rapport budget 2024 (p. 70) la range parmi les mesures de maîtrise.

### 2.8 Réintégrations post-2011 dans les corps spéciaux

Décret gouvernemental n° 2016-86 du 11 janvier 2016 (JORT n° 7 du 22 janvier 2016, p. 191 s.) :
prise en charge par l'État des cotisations pour la régularisation des périodes de rupture des
**agents des forces de sécurité intérieure et des douanes réintégrés en 2011** ; fondement : LFC
2014, art. 53 (clé `lfc-2014`). Modifié par le décret gouvernemental n° 2018-530 (JORT n° 50/2018,
intitulé AR). Les visas citent les statuts particuliers de 2006 des corps des FSI : décrets
n° 2006-1155 (sécurité du chef de l'État), 2006-1160 (sûreté et police nationale), 2006-1162 (garde
nationale), 2006-1164 (protection civile), 2006-1167 (prisons et rééducation) — utiles au chapitre
statutaire (le TODO sur le décret 72-230 vise un texte antérieur).

---

## 3. Contexte des réformes, dans les mots des sources budgétaires

- Rapport sur le projet de budget 2014 (`minfin-rapport-budget-2014`), p. 28 : « وتستأثر وزارتي
  الدفاع والداخلية بالقسط الأوفر من الانتدابات باعتبار التحديات الأمنية الداخلية والخارجية التي
  تواجهها البلاد في هذه المرحلة الحساسة » (la Défense et l'Intérieur reçoivent la plus grande part
  des recrutements au vu des défis sécuritaires intérieurs et extérieurs) ; les diplômés des écoles
  de formation représentent 52,3 % des recrutements prévus (9 780).
- Rapport 2022, p. 37 : le cadre est « l'atténuation du déficit » et « la préservation des
  équilibres » ; la maîtrise de la masse salariale et la « restructuration de la fonction publique »
  (التحكم في كتلة الأجور وإعادة هيكلة الوظيفة العمومية).
- Rapports 2024 (p. 70) et 2025 (p. 72) : ramener la masse salariale « progressivement à des
  niveaux raisonnables par rapport au PIB » et appliquer « l'accord du 15 septembre 2022 » avec
  l'UGTT (augmentations 2023-2025).
- Cour des comptes 2023, p. 62 : le rapport joint à la LFR 2023 rattache les crédits à
  « l'engagement de réduire la masse salariale et sa part du PIB de 2 % à l'horizon 2026 ».

---

## 4. Séries budgétaires [B] : effectifs autorisés et crédits de rémunération par mission

### 4.1 Effectif global autorisé, loi de finances (art. 9 et tableau F / ح), 2021-2026

Unité : agents ; périmètre : ministères (services centraux et régionaux) et EPA dont le budget est
rattaché pour ordre au budget de l'État. Valeurs **votées** (autorisations), non effectifs
observés.

| Mission | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Intérieur | 98 362 | 104 709 | 102 299 | 102 453 | 99 486 | 98 419 |
| Défense nationale | 91 365 | 96 849 | 98 861 | 101 416 | 103 678 | 106 893 |
| Justice | 18 878 | 19 352 | 19 637 | 19 216 | 18 761 | 19 544 |
| Affaires étrangères | 1 090 | 1 862 | 1 825 | 1 811 | 1 857 | 1 913 |
| Finances | 18 636 | 18 890 | 18 781 | 19 636 | 19 860 | 19 905 |
| Santé | 86 095 | 78 213 | 78 020 | 78 651 | 78 137 | 79 360 |
| Éducation | 208 402 | 206 653 | 206 303 | 202 626 | 204 574 | 220 254 |
| Enseignement supérieur et recherche | 36 060 | 37 646 | 39 903 | 40 051 | 39 703 | 40 606 |
| Cour des comptes | 489 | 389 | 418 | 410 | 408 | 402 |
| Conseil supérieur de la magistrature | 9 | 9 | 9 | 8 | 6 | 14 |
| Effectif non réparti | — | 6 000 | 6 000 | 6 000 | 12 000 | 12 995 |
| **Total** | **644 872** | **654 922** | **658 911** | **656 961** | **663 757** | **687 000** |

Sources :

| Année | Loi de finances | Art. 9 | Tableau |
|---|---|---|---|
| 2021 | loi n° 2020-46, `lf-2021` | JORT n° 128 du 25 décembre 2020, p. 3125 | tableau « F », p. 3223 |
| 2022 | DL n° 2021-21, `lf-2022` | JORT n° 119 du 28 décembre 2021, p. 3082 | tableau « F », p. 3187 |
| 2023 | DL n° 2022-79, `lf-2023` | AR : JORT n° 141 du 23 décembre 2022 (pas d'édition française) | tableau « ح », AR p. 4157 |
| 2024 | loi n° 2023-13, `lf-2024` | AR : JORT n° 144 du 12 décembre 2023, p. 6438 | tableau « ح », AR p. 6548 |
| 2025 | loi n° 2024-48, `lf-2025` | AR : JORT n° 149 du 10 décembre 2024 | tableau « ح », AR p. 6526 |
| 2026 | loi n° 2025-17, `lf-2026` | AR : JORT n° 148 du 12 décembre 2025 | tableau « ح », AR p. 4331 |

Réserves :

- 2021 : l'art. 9 renvoie au « tableau D », qui est celui des crédits d'engagement ; le tableau des
  effectifs est intitulé « F ». La Finances 2021 = programme 10-1 (le 10-2 Développement compte
  346).
- Ruptures de périmètre entre missions : en 2021, une mission « Affaires locales et environnement »
  (1 023) existe à part ; en 2022 l'Environnement est seul (297) et les affaires locales passent
  sous la mission Intérieur. En 2021, Jeunesse et sports (19 660) et Formation professionnelle et
  emploi (578) sont deux sous-missions d'une même mission. La Santé passe de 86 095 (2021) à
  78 213 (2022) sans explication dans la loi. Une variation d'une année sur l'autre peut donc être
  un reclassement.
- « Effectif non réparti » : réserve liée aux tranches de régularisation des ouvriers de chantiers
  (rapports budget 2024, p. 72 ; 2025, p. 74) ; à exclure de toute somme par mission.
- Les rapports budget donnent les mêmes totaux (2022 : 654 922, p. 44 ; 2024 : 656 961, p. 72 ;
  2025 : 663 757, p. 74) et précisent que l'effectif autorisé comprend les recrutements de
  régularisation des chantiers.

### 4.2 Crédits de paiement de rémunération votés, par ministère puis par mission, 2011-2026

Unité : dinars courants, crédits **initiaux** de la loi de finances (tableau « C » / « ت »,
première partie « Rémunérations publiques » jusqu'en 2019, « نفقات التأجير » par mission depuis
2020). Ce ne sont pas des dépenses exécutées (§ 4.4).

| LF | Intérieur | Défense nationale | Justice | Affaires étrangères | Total rémunérations | Source (tableau C/ت, première page) |
|---|---:|---:|---:|---:|---:|---|
| 2011 | 735 917 000 | 573 626 000 | 183 554 000 | 72 741 000 | 7 286 434 000 | JORT n° 102/2010, p. 3483 (`lf-2011`) |
| 2012 | 1 094 051 000 | 740 779 000 | 215 048 000 | 90 907 000 | 8 564 726 000 | JORT n° 1/2012, p. 17 (`lf-2012`) |
| 2013 | 1 329 727 000 | 871 723 000 | 258 156 000 | 99 741 000 | 9 780 600 000 | JORT n° 1/2013, p. 34 (`lf-2013`) |
| 2014 | 1 445 576 000 | 971 775 000 | 293 139 000 | 112 391 000 | 10 554 866 000 | JORT n° 105/2013, p. 3705 (`lf-2014`) |
| 2015 | 1 529 652 000 | 1 106 549 000 | 319 073 000 | 125 445 000 | 11 197 389 000 | JORT n° 105/2014, p. 3479 (`lf-2015`) |
| 2016 | 1 778 503 000 | 1 321 754 000 | 366 674 000 | 123 991 000 | 13 000 000 000 | AR : JORT n° 104/2015, p. 3629 (`lf-2016`) |
| 2017 | 2 059 221 000 | 1 477 224 000 | 404 472 000 | 110 774 000 | 13 700 000 000 | JORT n° 105/2016, p. 3857 (`lf-2017`) |
| 2018 | 2 390 121 000 | 1 593 893 000 | 450 181 000 | 126 960 000 | 14 751 000 000 | JORT n° 101/2017, p. 4298 (`lf-2018`) |
| 2019 | 2 637 512 000 | 2 020 778 000 | 514 250 000 | 151 163 000 | 16 516 000 000 | AR : JORT n° 104/2018, p. 5475 (`lf-2019`) |
| 2020 | 3 169 575 000 | 2 342 000 000 | 594 051 000 | 160 565 000 | 19 030 000 000 ¹ | AR : JORT n° 104/2019, pp. 4718-4719 (`lf-2020`) |
| 2021 | 3 379 148 000 | 2 424 000 000 | 654 000 000 | 170 615 000 | 20 118 481 000 | JORT n° 128/2020, pp. 3144 et 3147 (`lf-2021`) |
| 2022 | 3 889 800 000 | 2 533 683 000 | 725 870 000 | 176 825 000 | 21 573 334 000 ¹ | JORT n° 119/2021, p. 3113 (`lf-2022`) |
| 2023 | 4 104 220 000 | 2 684 346 000 | 777 200 000 | 182 881 000 | 22 772 485 000 ¹ | AR : JORT n° 141/2022, p. 4088 (`lf-2023`) |
| 2024 | 4 197 840 000 | 2 846 243 000 | 793 263 000 | 190 000 000 | 23 711 000 000 ² | AR : JORT n° 144/2023, p. 6465 (`lf-2024`) |
| 2025 | 4 222 822 000 | 2 942 507 000 | 818 004 000 | 200 022 000 | 24 389 000 000 ² | AR : JORT n° 149/2024, p. 6459 (`lf-2025`) |
| 2026 | 4 160 800 000 | 3 015 442 000 | 820 785 000 | 205 850 000 | — | AR : JORT n° 148/2025, p. 4264 (`lf-2026`) |

¹ Total repris de la Cour des comptes, rapport sur la clôture du budget 2023, tableau p. 62
(« الاعتمادات الأصلية », crédits initiaux), non relu sur la dernière page du tableau C/ت.
² Total repris du rapport sur le budget (2024 : p. 70 ; 2025 : p. 72), en millions de dinars.
Les totaux 2026 et la dernière page des tableaux 2020, 2022-2026 restent à lire.

Ruptures à marquer :

- 2011 : « Ministère de l'Intérieur et du Développement local ». 2019-2021 : affaires locales hors
  Intérieur (mission « Affaires locales et environnement »). **Depuis 2022, la mission Intérieur
  comprend un programme 4 « Affaires locales »** (crédits totaux du programme : 1 011 MD en 2022).
- Justice : 2013-2015, chapitre « Justice » distinct de « Droits de l'Homme et justice
  transitionnelle » (2015 : 3 421 000 dinars pour ce dernier, non inclus ci-dessus).
- 2016-2019 : nomenclature par ministère (« الأبواب », chapitres) ; 2020 : passage à la
  nomenclature par mission et programme (« المهمات والمهمات الخاصة والبرامج »).
- Pour les autres missions (Éducation, Santé, Enseignement supérieur, Finances), les valeurs sont
  lisibles sur les mêmes pages ou les suivantes ; seules 2013-2015 (Éducation, Santé) et 2021
  (Éducation 6 013 250 000 en crédits d'engagement, p. 3150 ; Enseignement supérieur 1 315 000 000,
  p. 3147 ; Santé 2 177 771 000, p. 3150) ont été relevées.
- Les lois de finances antérieures à 2011 renvoient au même tableau « C » par chapitre. Dans les
  fascicules français de 1994, 1997, 2005 et 2008, le tableau n'est pas dans la couche texte (images
  ou non reproduit : à vérifier à l'image) ; ceux de 2000 et 2003 ont une couche texte à encodage
  décalé, à décoder (+29, outillage § 5) avant toute conclusion. L'article des dépenses de chaque
  loi donne au moins le total de la « première section : Rémunérations publiques » (ex. LF 2009 :
  6 246 087 000 dinars, JORT n° 104/2008) : série longue des totaux votés extractible du texte.

### 4.3 Comparaison, pour mémoire, avec les effectifs observés de l'INS [S]

INS, base INSAF, effectif de décembre (rapport 2018-2025, tableau 8, p. 11 ; `ins-fonction-publique-2025`) :

| Ministère | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Défense | 84 971 | 86 808 | 86 880 | 86 446 | 87 035 | 87 584 | 88 440 | 87 765 |
| Intérieur | 96 286 | 95 704 | 96 796 | 99 826 | 99 727 | 98 771 | 97 061 | 96 146 |
| Justice | 18 375 | 18 663 | 18 797 | 19 300 | 18 974 | 19 085 | 18 491 | 18 193 |

Enquête 2010-2021 (`ins-fonction-publique-2021`, tab11, milliers) : Défense 63,1 (2015), 69,4,
74,7, 85,0 (2018) ; Intérieur 84,2 (2015) … 90,3 (2021) ; Justice 15,9 (2015) … 18,9 (2021). Annexes
annuelles 2010-2014 : Intérieur 6,928 (2010), 7,135 (2011), 73,645 (2012), 78,532 (2013), 79,943
(2014) ; Défense 47,3 (2010) à 58,5 (2014) ; Justice 11,8 à 15,8.

À ne pas mettre dans le même tableau que § 4.1 (autorisations votées contre effectifs observés),
ni raccorder les deux séries INS entre elles (révision d'environ 9 000 agents vers l'Intérieur
pour 2018-2021 ; `sources/ins-fonction-publique-2018-2025.md`, l. 67). Le rapprochement sert
seulement au point 0.2.

### 4.4 Exécution de la masse salariale [B] (Cour des comptes)

Rapport sur la clôture du budget 2023 (`cdc-rapport-budget-2023`), tableau p. 62, millions de
dinars :

| Année | Crédits initiaux | Crédits rectifiés | Crédits définitifs | Paiements | Taux d'exécution |
|---|---:|---:|---:|---:|---:|
| 2020 | 19 030,000 | 19 246,580 | 19 336,961 | 19 202,816 | 99,31 % |
| 2021 | 20 118,481 | 20 345,196 | 20 326,414 | 20 182,202 | 99,29 % |
| 2022 | 21 573,334 | 21 552,659 | 21 414,067 | 21 124,848 | 98,65 % |
| 2023 | 22 772,485 | 22 772,485 | 22 433,731 | 21 702,473 | 96,74 % |

Paiements antérieurs (`cdc-loireg-2021`, graphique p. 39) : 14 352,389 (2017), 14 774,632 (2018),
16 764,997 (2019). Part dans les dépenses du budget hors financement : 42,86 % (2019), 51,88 %
(2020), 51,94 % (2021) (`cdc-loireg-2021`, p. 38) ; 46,86 % (2022) (`cdc-loireg-2022`, p. 71).

Répartition des paiements par mission (graphiques) : 2022 — Éducation 28,96 %, Intérieur 17,72 %,
Santé 12,08 %, Défense 11,51 %, Enseignement supérieur 6,68 %, autres 23,04 % (`cdc-loireg-2022`,
p. 72) ; 2023 — Éducation 28,08 % (6 094,045 MD), Intérieur 17,66 % (3 836,432 MD), Santé 12,18 %,
Défense 11,53 %, Enseignement supérieur 6,84 %, autres 23,69 % (`cdc-rapport-budget-2023`,
pp. 64-65). La Cour des comptes rend compte de l'exécution à partir des comptes du ministère :
famille budgétaire, à présenter en section propre (exécution), non mêlée aux crédits votés.

Rapports 2018-2021 : la répartition par mission y est vraisemblablement présente ; leur couche
texte arabe est partielle (pas de réponse à « كتلة الأجور » en 2019-2021) ; à lire à l'image.

### 4.5 Part du PIB : ce que disent les sources, sans réconciliation

Ministère des Finances, rapport budget 2025, graphique 26, p. 49 : masse salariale 19 203 MD
(2020, 16,1 %), 20 182 (2021, 15,4 %), 21 125 (2022, 15,1 %), 21 608 (2023, 14,2 %), 22 531
(2024 attendu, 13,6 %), 24 389 (2025 LF, 13,3 %). Cour des comptes : 16,60 % (2021) et 15,26 %
(2022) (`cdc-loireg-2022`, p. 71). Aucune des deux sources ne précise la base du PIB : « base non
précisée par la source ». Les écarts (2021 : 15,4 contre 16,60 ; 2022 : 15,1 contre 15,26) sont à
donner tels quels. Préférer la part des dépenses de l'État, qui ne dépend d'aucune base :
rapport 2022, p. 42 : 45,7 % (2022 prévu), 50,0 % (LF 2021), 46,0 % (2021 actualisé) ; rapport
2024, p. 71 : 39,6 % (2024) contre 40,6 % (2023 actualisé) ; rapport 2025, p. 73 : 40,8 % (2025)
contre 39,6 % (LF 2024). (Dénominateurs non identiques à ceux de la Cour des comptes, qui exclut le
financement.)

---

## 5. Recrutements prévus et flux observés

### 5.1 Recrutements prévus par le budget [B] (rapports sur le projet de budget)

| Année | Total | Défense | Intérieur | Justice | Éducation | Santé | Source |
|---|---:|---:|---:|---:|---:|---:|---|
| 2012 | 25 011 (LF 21 138 + LFC 3 873) | — | 3 075 | 1 996 | 5 667 | 4 103 | rapport budget actualisé 2012, pp. 29-30 |
| 2013 | 23 267 | — ³ | 2 965 | 1 400 | 5 648 | 3 180 | rapport budget 2013, pp. 45-46 (`minfin-rapport-budget-2013`) |
| 2014 | 18 700 | 5 470 | 3 550 | 740 | 4 000 | 1 850 | rapport budget 2014, pp. 27-28 (`minfin-rapport-budget-2014`) |
| 2022 | 18 442 | 4 907 | 5 588 | 700 | 6 246 | — | rapport budget 2022, p. 43 (`minfin-rapport-budget-2022`) |
| 2023 | 8 398 (Défense 53 %, Éducation 29 %, autres missions 18 %, écoles 1 %) | — | — | — | — | — | CdC 2023, p. 63, citant le rapport budget 2023 (non obtenu) |
| 2024 | 13 586 (+ 6 000 chantiers) | 3 094 | 1 998 | 720 ⁴ | 2 372 | 3 000 | rapport budget 2024, pp. 71-72 (`minfin-rapport-budget-2024`) |
| 2025 | 21 376 (+ 12 000 chantiers) | 2 778 | 1 529 | 1 080 | 9 207 | 3 500 | rapport budget 2025, pp. 48-49 et 73-74 (`minfin-rapport-budget-2025`) |

³ Défense non détaillée en 2013 (comprise dans « autres secteurs », 5 530).
⁴ 2024 : 150 magistrats et 570 agents des prisons, inscrits sous « diplômés des autres écoles ».
2023 : seules les parts sont données par la Cour des comptes ; les effectifs par mission sont à lire dans le rapport sur le budget 2023.

Hors tableau (nature incertaine) : la Cour des comptes explique la hausse des paiements de 2021 notamment par « انتداب 16.501 خطة خلال سنة 2021 » (recrutement de 16 501 postes en 2021, coût 268 MD) (`cdc-loireg-2021`, p. 38), sans préciser s'il s'agit d'entrées effectives ou de postes ouverts au budget.

Détail des corps spéciaux :

- 2022 : Intérieur 5 588 (diplômés des écoles de formation) ; Défense 4 907 ; Justice 700 (100
  juges de premier grade, 600 prisons et rééducation) ; écoles 91 (ENA 50, IFID 21, ENS 20).
- 2024 : Défense 3 094 (2 595 diplômés des écoles, 499 autres) ; Intérieur 1 998 (écoles) ;
  autres écoles 820 (ENA 50, IFID-IEDF-douanes 30, ENS 20, magistrats 150, prisons 570).
- 2025 : Défense 2 778 (2 284 écoles, 494 autres) ; Intérieur 1 529 (1 500 écoles, 29 autres) ;
  Justice 1 080 (807 écoles dont 250 magistrats et 557 prisons, 273 autres) ; Finances 863
  (63 IFID-IEDF-douanes, 800 autres). Graphique 25, p. 49 : part des recrutements Éducation 43,1 %,
  Santé 16,4 %, Défense 13,0 %, Intérieur 7,2 %, Justice 5,1 %.
- Départs à la retraite prévus : 9 951 (2013, p. 45) ; environ 10 100 (2014), recrutements nets
  ≈ 8 600 contre 13 336 (2013) et 15 734 (2012) (rapport 2014, p. 27).
- Effectif en activité fin 2012 « حوالي 581 ألف عون » (rapport actualisé 2012, p. 30).

Rapports 2015-2021 et 2023 : non obtenus localement (à rapatrier, § 7).

### 5.2 Flux observés [S] (INS, base INSAF)

Rapport 2018-2025, tableau 9, p. 12 (`ins-fonction-publique-2025` ; `tunisia-data`,
`entrees_sorties.csv`) :

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Entrées | 38 757 | 26 228 | 20 954 | 33 089 | 24 755 | 29 878 | 24 101 | 38 701 |
| Sorties | 19 572 | 15 640 | 27 994 | 29 318 | 35 597 | 35 954 | 35 954 ⁵ | 33 358 |
| Solde publié | 19 185 | 10 588 | −7 040 | 3 771 | −10 842 | −6 076 | −9 257 | 5 343 |

⁵ Sorties 2024 identiques à l'unité à 2023 ; le solde publié suppose 33 358 : cellule
vraisemblablement recopiée (fiche de source, l. 96). Le solde ne redonne jamais la variation de
l'effectif total ; le rapport ne définit pas les mouvements comptés. Flux tous ministères, sans
ventilation par ministère dans le texte du rapport (figures non chiffrées). 2021 : tab14-17 de
l'enquête 2010-2021 (34 096 entrées, 29 001 sorties, par ministère : tab17).

Ne pas mettre ces flux dans le même tableau que les recrutements prévus (§ 5.1).

---

## 6. Prémisses du ticket non confirmées

| Prémisse | Ce que disent les textes | Fiche |
|---|---|---|
| « Décret-loi / loi 2011 sur la titularisation des agents de chantier » | Rien trouvé en 2011 par intitulé. La chaîne est : loi n° 2021-27 (art. 18 bis de la loi 83-112), décret gouvernemental n° 2021-436, LF 2024 art. 12, décret n° 2025-459. En 2011, la régularisation qui figure aux sources est celle de la **sous-traitance** dans le secteur public (aucun texte JORT repéré ; à vérifier : accord gouvernement-UGTT du 22 avril 2011). | r-titularisation-chantiers-2011 |
| « Loi 2012-27 amnistie générale / réintégration » | La loi n° 2012-27 est la **loi de finances pour 2013** ; ses art. 32-33 régularisent la situation des bénéficiaires de l'amnistie générale auprès des caisses sociales (intitulé AR de l'index ; non lus) ; son art. 77 encourage le privé à recruter des ouvriers de chantiers. La réintégration est le **décret n° 2012-3256**. Le recrutement direct des amnistiés, la loi n° 2012-4. | — |
| « Lois de finances 2019-2025, articles de gel » | Aucun article de gel trouvé ; le gel est dans les rapports sur le budget, les circulaires de préparation et le MEFP du FMI (§ 1.4). | r-lf-gel-recrutements-2017-2026 |
| « Décret-loi 2014 / loi 2014 de départ volontaire » | Seule la loi n° 2014-48 (Tunisie Télécom). | r-depart-volontaire-fp-2014-2019 |
| « Programme de départ volontaire 2015 / 2019 dans la fonction publique » | Aucun texte trouvé ; textes de 2017 (loi 2017-51) et 2018 (loi 2018-5). | r-depart-volontaire-fp-2014-2019 |
| « Départ volontaire dans les entreprises publiques, loi 2019 » | Aucune loi trouvée ; la loi n° 2018-5 couvre déjà « les établissements et entreprises publics » (art. 1 al. 2) ; le décret 2022-542 en exclut les EP non administratifs. | r-depart-volontaire-ep-2019 |
| « Recrutement des diplômés chômeurs de longue durée, loi 2012-? / 2019-? » | Loi n° 2020-38 (10 ans de chômage) et loi n° 2025-18 ; la loi 2012-4 (âge et ancienneté du diplôme) en est l'antécédent. | — |

---

## 7. Références candidates

### 7.1 Clés existantes employées

`loi83-112`, `loi87-7`, `loi2009-39`, `loi-org-2019-15-lob`, `lf-2011` à `lf-2026`, `lfc-2014`
(fiscalité), `minfin-rapport-budget-2013`, `minfin-rapport-budget-2014` (fiscalité),
`minfin-rapport-budget-2022`, `-2024`, `-2025` (marché du travail, fiscalité), `cdc-loireg-2021`,
`cdc-loireg-2022`, `cdc-rapport-budget-2023` (fiscalité), `ins-fonction-publique-2021`,
`ins-fonction-publique-2025`, `decret2021-436` (marché du travail), `imf-tunisia-art4-2020`.

Avant de citer une clé d'un autre livre dans `remunerations_publiques`, vérifier qu'elle est dans
`precis/fr/references.json` ou la copier dans `precis/fr/remunerations_publiques/references.json`
(et l'arabe).

### 7.2 Entrées CSL-JSON à créer (forme des entrées existantes de `precis/fr/references.json`)

Style de clé suivi : `decret-87-337` avant 2000, `decret2018-205` après ; `decret-loi2011-32` sur
la forme de `decretloi2022-49` existant (à harmoniser par le bibliographe).

```json
[
  {"id": "decret-87-337", "type": "legislation", "title": "Décret n° 87-337 du 6 mars 1987, fixant les critères de priorité pour le bénéfice du système de retraite anticipée volontaire et déterminant les conditions de présentation des programmes de remplacement du personnel mis à la retraite", "container-title": "Journal officiel de la République tunisienne", "issue": "18", "page": "369-370", "issued": {"date-parts": [[1987, 3, 10]]}, "URL": "https://www.pist.tn/jort/1987/1987F/Jo01887.pdf", "note": "citation-key: decret-87-337"},
  {"id": "loi87-8", "type": "legislation", "title": "Loi n° 87-8 du 6 mars 1987, instituant des dispositions relatives au travail des retraités", "container-title": "Journal officiel de la République tunisienne", "issue": "18", "page": "364", "issued": {"date-parts": [[1987, 3, 10]]}, "URL": "https://www.pist.tn/jort/1987/1987F/Jo01887.pdf", "note": "citation-key: loi87-8"},
  {"id": "decretloi2011-32", "type": "legislation", "title": "Décret-loi n° 2011-32 du 27 avril 2011, portant dispositions dérogatoires pour le recrutement dans le secteur public au titre de l'année 2011", "container-title": "Journal officiel de la République tunisienne", "issue": "30", "page": "572-573", "issued": {"date-parts": [[2011, 4, 29]]}, "URL": "https://www.pist.tn/jort/2011/2011F/Jo0302011.pdf", "note": "citation-key: decretloi2011-32"},
  {"id": "decret2011-544", "type": "legislation", "title": "Décret n° 2011-544 du 14 mai 2011, portant application des dispositions du décret-loi n° 2011-32 du 27 avril 2011 portant dispositions dérogatoires pour le recrutement dans le secteur public au titre de l'année 2011", "container-title": "Journal officiel de la République tunisienne", "issue": "35", "page": "716-719", "issued": {"date-parts": [[2011, 5, 17]]}, "URL": "https://www.pist.tn/jort/2011/2011F/Jo0352011.pdf", "note": "citation-key: decret2011-544 ; rectificatif JORT n° 44 du 17 juin 2011"},
  {"id": "loi2012-4", "type": "legislation", "title": "Loi n° 2012-4 du 22 juin 2012, portant dispositions dérogatoires pour le recrutement dans le secteur public", "container-title": "Journal officiel de la République tunisienne", "issue": "50", "page": "1531-1532", "issued": {"date-parts": [[2012, 6, 26]]}, "URL": "https://www.pist.tn/jort/2012/2012F/Jo0502012.pdf", "note": "citation-key: loi2012-4"},
  {"id": "decret2012-833", "type": "legislation", "title": "Décret n° 2012-833 du 20 juillet 2012, portant application des dispositions de la loi n° 2012-4 du 22 juin 2012, portant dispositions dérogatoires pour le recrutement dans le secteur public", "container-title": "Journal officiel de la République tunisienne", "issue": "58", "page": "1707-1711", "issued": {"date-parts": [[2012, 7, 24]]}, "URL": "https://www.pist.tn/jort/2012/2012F/Jo0582012.pdf", "note": "citation-key: decret2012-833"},
  {"id": "decret2016-372", "type": "legislation", "title": "Décret gouvernemental n° 2016-372 du 21 mars 2016, fixant les dispositions exceptionnelles de recrutement dans le secteur de la fonction publique au titre de l'année 2016", "container-title": "Journal officiel de la République tunisienne", "issue": "24", "page": "879-880", "issued": {"date-parts": [[2016, 3, 22]]}, "URL": "https://www.pist.tn/jort/2016/2016F/Jo0242016.pdf", "note": "citation-key: decret2016-372"},
  {"id": "loi2014-48", "type": "legislation", "title": "Loi n° 2014-48 du 24 juillet 2014, portant mise à la retraite facultative avant l'atteinte de l'âge légal à la société nationale des télécommunications", "container-title": "Journal officiel de la République tunisienne", "issue": "60", "page": "1916", "issued": {"date-parts": [[2014, 7, 25]]}, "URL": "https://www.pist.tn/jort/2014/2014F/Jo0602014.pdf", "note": "citation-key: loi2014-48"},
  {"id": "loi2017-51", "type": "legislation", "title": "Loi n° 2017-51 du 28 juin 2017, portant dispositions dérogatoires de mise à la retraite avant l'âge légal dans la fonction publique", "container-title": "Journal officiel de la République tunisienne", "issue": "53", "page": "2303", "issued": {"date-parts": [[2017, 7, 4]]}, "URL": "https://www.pist.tn/jort/2017/2017F/Jo0532017.pdf", "note": "citation-key: loi2017-51 ; AR pp. 2126-2127"},
  {"id": "decret2017-825", "type": "legislation", "title": "أمر حكومي عدد 825 لسنة 2017 مؤرخ في 28 جويلية 2017 يتعلق بضبط إجراءات وصيغ تطبيق الأحكام الاستثنائية للإحالة على التقاعد قبل بلوغ السن القانونية في قطاع الوظيفة العمومية [Décret gouvernemental n° 2017-825]", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "59-60", "page": "2380-2381", "issued": {"date-parts": [[2017, 7, 28]]}, "URL": "https://www.pist.tn/jort/2017/2017A/Ja0602017.pdf", "note": "citation-key: decret2017-825 ; édition française non trouvée (pist.tn 404)"},
  {"id": "loi2018-5", "type": "legislation", "title": "Loi n° 2018-5 du 23 janvier 2018, relative au départ volontaire des agents publics", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "8", "page": "288-289", "issued": {"date-parts": [[2018, 1, 26]]}, "URL": "https://www.pist.tn/jort/2018/2018A/Ja0082018.pdf", "note": "citation-key: loi2018-5 ; pagination arabe ; l'adresse 2018F/Jo0082018.pdf sert l'arabe ; jort_cache donne p. 265 (non vérifiée)"},
  {"id": "decret2018-205", "type": "legislation", "title": "أمر حكومي عدد 205 لسنة 2018 مؤرخ في 23 فيفري 2018 يتعلق بضبط صيغ وإجراءات وآجال تطبيق الأحكام المتعلقة بالمغادرة الاختيارية للأعوان العموميين [Décret gouvernemental n° 2018-205]", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "17", "page": "579-581", "issued": {"date-parts": [[2018, 2, 27]]}, "URL": "https://www.pist.tn/jort/2018/2018A/Ja0172018.pdf", "note": "citation-key: decret2018-205"},
  {"id": "arrete2018-02-23-depart-volontaire", "type": "legislation", "title": "قرار من رئيس الحكومة مؤرخ في 23 فيفري 2018 يتعلق بضبط تاريخ انطلاق تطبيق الأحكام المتعلقة بالمغادرة الاختيارية للأعوان العموميين بعنوان سنة 2018", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "17", "page": "582", "issued": {"date-parts": [[2018, 2, 27]]}, "URL": "https://www.pist.tn/jort/2018/2018A/Ja0172018.pdf", "note": "citation-key: arrete2018-02-23-depart-volontaire"},
  {"id": "arrete2018-05-07-depart-volontaire", "type": "legislation", "title": "قرار من رئيس الحكومة مؤرخ في 7 ماي 2018 يتعلق بضبط تاريخ انطلاق تطبيق الأحكام المتعلقة بالمغادرة الاختيارية للأعوان العموميين للمرة الثانية بعنوان سنة 2018", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "39", "page": "1769", "issued": {"date-parts": [[2018, 5, 15]]}, "URL": "https://www.pist.tn/jort/2018/2018A/Ja0392018.pdf", "note": "citation-key: arrete2018-05-07-depart-volontaire"},
  {"id": "loi2020-38", "type": "legislation", "title": "Loi n° 2020-38 du 13 août 2020, portant dispositions dérogatoires pour le recrutement dans le secteur public", "container-title": "Journal officiel de la République tunisienne", "issue": "82", "page": "1763", "issued": {"date-parts": [[2020, 8, 19]]}, "URL": "https://www.pist.tn/jort/2020/2020F/Jo0822020.pdf", "note": "citation-key: loi2020-38"},
  {"id": "loi2021-27", "type": "legislation", "title": "Loi n° 2021-27 du 7 juin 2021, complétant la loi n° 83-112 du 12 décembre 1983, relative au statut général des personnels de l'État, des collectivités locales et des établissements publics à caractère administratif", "container-title": "Journal officiel de la République tunisienne", "issue": "50", "page": "1505", "issued": {"date-parts": [[2021, 6, 11]]}, "URL": "https://www.pist.tn/jort/2021/2021F/Jo0502021.pdf", "note": "citation-key: loi2021-27"},
  {"id": "decret2022-542", "type": "legislation", "title": "Décret présidentiel n° 2022-542 du 13 juin 2022, fixant les catégories concernées, les procédures, les modalités et les délais d'application du programme spécifique pour la mise à la retraite avant l'âge légal", "container-title": "Journal officiel de la République tunisienne", "issue": "68", "page": "1898-1899", "issued": {"date-parts": [[2022, 6, 14]]}, "URL": "https://www.pist.tn/jort/2022/2022F/Jo0682022.pdf", "note": "citation-key: decret2022-542 ; absent de l'index jort_cache"},
  {"id": "arrete2022-06-16-retraite-avant-age", "type": "legislation", "title": "Arrêté de la Cheffe du Gouvernement du 16 juin 2022, fixant les délais d'application du programme spécifique pour la mise à la retraite avant l'âge légal au titre de l'année 2022", "container-title": "Journal officiel de la République tunisienne", "issue": "69", "page": "1926", "issued": {"date-parts": [[2022, 6, 17]]}, "URL": "https://www.pist.tn/jort/2022/2022F/Jo0692022.pdf", "note": "citation-key: arrete2022-06-16-retraite-avant-age ; mêmes formes pour 2023 (JORT n° 4/2023, p. 34), 2024 (n° 145/2023, p. 3653), 2025 (n° 159/2024, p. 3784)"},
  {"id": "decret2023-591", "type": "legislation", "title": "أمر عدد 591 لسنة 2023 مؤرخ في 21 سبتمبر 2023 يتعلق بإجراء تدقيق شامل لعمليات الانتداب والإدماج بالوظيفة العمومية والهيئات والمؤسسات والمنشآت العمومية والشركات ذات المساهمة العمومية وسائر الهياكل العمومية الأخرى والمنجزة من 14 جانفي 2011 إلى 25 جويلية 2021 [Décret n° 2023-591]", "container-title": "الرائد الرسمي للجمهورية التونسية", "issue": "108", "page": "5288-5290", "issued": {"date-parts": [[2023, 9, 22]]}, "URL": "https://www.pist.tn/jort/2023/2023A/Ja1082023.pdf", "note": "citation-key: decret2023-591 ; édition FR absente du corpus et de pist.tn ; dernière page non vérifiée"},
  {"id": "loi2025-18", "type": "legislation", "title": "Loi n° 2025-18 du 22 décembre 2025, portant dispositions exceptionnelles pour le recrutement des diplômés de l'enseignement supérieur en situation de chômage de longue durée, dans le secteur public et la fonction publique", "container-title": "Journal officiel de la République tunisienne", "issue": "153", "page": "3609", "issued": {"date-parts": [[2025, 12, 23]]}, "URL": "https://www.pist.tn/jort/2025/2025F/Jo1532025.pdf", "note": "citation-key: loi2025-18 ; traduction française pour information"},
  {"id": "decret2016-86", "type": "legislation", "title": "Décret gouvernemental n° 2016-86 du 11 janvier 2016, portant fixation des modalités de la prise en charge par l'État des cotisations pour bénéficier de la pension de retraite et sa base de calcul au titre de la régularisation des périodes de rupture du travail des agents des forces de la sécurité intérieure et de la douane qui ont été réintégrés en 2011", "container-title": "Journal officiel de la République tunisienne", "issue": "7", "page": "191", "issued": {"date-parts": [[2016, 1, 22]]}, "URL": "https://www.pist.tn/jort/2016/2016F/Jo0072016.pdf", "note": "citation-key: decret2016-86 ; page de fin à relever"},
  {"id": "imf-tunisia-eff-2016", "type": "report", "title": "Tunisia: Request for an Extended Arrangement Under the Extended Fund Facility — Press Release; Staff Report; and Statement by the Executive Director for Tunisia", "author": [{"literal": "Fonds monétaire international"}], "publisher": "Fonds monétaire international", "publisher-place": "Washington, D.C.", "number": "IMF Country Report No. 16/138", "issued": {"date-parts": [[2016, 6]]}, "URL": "https://www.imf.org/external/pubs/ft/scr/2016/cr16138.pdf", "note": "citation-key: imf-tunisia-eff-2016 ; couverture : June 2016 ; rapport des services achevé le 2 mai 2016 ; URL vérifiée le 23 octobre 2026 (200, application/pdf) ; copie locale tunisia-data/data/raw/banque-mondiale-rapports/imf_2016_138_eff_request_tunisia.pdf"}
]
```

Textes repérés à lire avant toute entrée : décret n° 2012-3256 (JORT n° 100/2012, AR) ; décret
n° 2015-85 (JORT n° 34/2015) ; décret n° 85-762 ; décret n° 2003-1617 ; décret présidentiel
n° 2022-387 ; décret n° 2025-459 (JORT n° 138/2025, p. 3138 ; lu en partie, domicile marché du
travail) ; LF 2026 art. 90, 92, 108 ; décrets 82-1229, 92-1551, 2006-1031.

### 7.3 Catalogue `tunisia-data` (non écrit : consigne de lecture seule hors `docs/notes`)

Lignes prêtes à ajouter (fichier ; adresse d'origine ; date ; SHA-256). Aucun PDF nouveau n'a été
téléchargé (le seul fichier pris sur pist.tn, `2018F/Jo0082018.pdf`, est identique au fichier du
corpus).

| Fichier (`data/raw/banque-mondiale-rapports/`) | Adresse d'origine | SHA-256 |
|---|---|---|
| `minfin_2025_annexe1_rapport_budget_etat_2025_ar.pdf` | non consignée (déjà signalé dans `minfin-rapport-budget-2025`) | `0d161c82a117a2a33133b6c43584474856e5ea179b704a1d2e35c0a728c31f41` |
| `minfin_2021-12_rapport_budget_etat_2022_ar.pdf` | non consignée | `29c4742292b8737c73bd58a28c66d0be399313b8a91075299d73d8245d6af42c` |
| `minfin_2023-10_rapport_budget_etat_2024_ar.pdf` | non consignée | `2a01c70ea9d1f04d982d55363a3fc95c337163169f15204fd009547516883587` |
| `imf_2016_138_eff_request_tunisia.pdf` | https://www.imf.org/external/pubs/ft/scr/2016/cr16138.pdf (répond ; identité du fichier local non comparée) | `274e4edd312a3c852064f553c4055cca092fcd9e100dfec287efdd80b5532ecc` |

Déjà catalogués : rapports budget 2012 actualisé et 2013 (`minfinances-portail-ancien-urls.csv`) ;
`loireg2021.pdf`, `loireg2022.pdf`, `RAPPORT-BUDGET-2023-version-finale-1.pdf`
(`cour-des-comptes-*.csv`) ; INS 2018-2025 (`catalog.yml`). Le rapport budget 2014 est sous
`data/raw/minfinances/reforme_fiscale_2013_2014/2013-10_rapport_projet_budget_etat_2014_ar.pdf`.

À rapatrier : rapports sur le projet de budget 2015 à 2021 et 2023, 2026 (finances.gov.tn, archives
du web) ; rapports de la Cour des comptes sur la clôture du budget 2017 et 2024 ; rapport FMI de la
revue de l'EFF qui rend compte des départs volontaires de 2018 (CR 2018-2019, à identifier).

Décalages fichier → page imprimée : rapport budget 2025 : −1 ; 2024 : −2 ; 2022 : −1 ; 2013 : −7 ;
2012 actualisé : −5 ; 2014 : −11 ; Cour des comptes 2021, 2022 et 2023 : −3 ; INS 2018-2025 : 0.

---

## 8. Matière à verser dans les autres livres

**Livre « Retraites », `_secteur_public.qmd`** (TODO existants que cette lecture permet de fermer) :

- TODO « lire la loi n° 87-7 et son décret n° 87-337 » : § 2.1 ci-dessus.
- TODO « lire l'article 14 de la loi de finances pour 2025 […] et les arrêtés […] (2022, 2023,
  2024) » : § 2.6 (prolongation 2025-2028 ; arrêtés de 2022 à 2025 ; décret présidentiel 2022-542
  et ses exclusions, absent du chapitre).
- Ajout possible : loi 2017-51 et décret 2017-825 (départs 2018-2021), absents du chapitre ; loi
  2014-48 (Tunisie Télécom).
- Le glossaire `retraite-anticipee-volontaire` (AR) emploie « المغادرة الطوعية » en paraphrasant
  l'art. 7 de la loi 2019-37 ; la loi 2018-5 et le décret 2018-205 disent « المغادرة الاختيارية ».
  À vérifier sur l'édition arabe de la loi 2019-37, art. 7, avant de signaler un écart au
  terminologue.

**Livre « Marché du travail », `_politiques_emploi.qmd`** : la fiche `r-chantiers-regionaux-texte-fondateur`
a pour `a_faire` « identifier la loi n° 2021-27 et son art. 18 bis » : fait (§ 1.3). Décret
n° 2025-459 (JORT n° 138/2025, p. 3138) modifie les art. 4, 7, 8 et 13 du décret 2021-436 (fin de
l'emploi à 60 ans avec allocation égale au SMIG et carte de soins ; intégration des 45-55 ans par
tranches).

**Livre « Entreprises publiques »** : loi 2014-48 (Tunisie Télécom) ; champ de la loi 2018-5.

---

## 9. Notions à glossaire

Vérifié par `grep` dans `precis/glossaire.yml` : seules `retraite-anticipee-volontaire` et
`mise-a-la-retraite-avant-age-legal` existent ; aucune entrée pour les notions suivantes.

| Terme FR | Terme AR (JORT) | Source canonique pressentie |
|---|---|---|
| Départ volontaire (des agents publics) | المغادرة الاختيارية | loi n° 2018-5, art. 1 |
| Prime de départ volontaire | منحة المغادرة | loi n° 2018-5, art. 5 |
| Effectif global du personnel autorisé | العدد الجملي للأعوان المرخص فيهم | LOB n° 2019-15, art. 45 ; LF, art. 9 |
| Mission (budgétaire) | مهمة | LOB n° 2019-15 |
| Crédits de paiement | اعتمادات الدفع | LOB n° 2019-15 ; LF, tableau C |
| Recrutement direct | الانتداب المباشر | loi n° 2012-4, art. 3 ; loi n° 2020-38 |
| Concours externe sur dossiers | مناظرة خارجية بالملفات | décret-loi n° 2011-32, art. 2 |
| Ouvrier de chantier | عامل الحضائر | loi n° 2021-27 (art. 18 bis) ; décret 2021-436 |
| Écoles de formation (diplômés des) | مدارس التكوين | rapports sur le budget (catégorie de recrutement) |
| Congé pour création d'entreprise | عطلة لبعث مؤسسة | loi 83-112, art. 50 bis ; LF 2022, art. 15 |
| Programme spécifique de mise à la retraite avant l'âge légal | البرنامج الخصوصي للإحالة على التقاعد قبل بلوغ السن القانونية | décret présidentiel n° 2022-542 |

---

## 10. Lacunes (TODO, rien à inventer)

1. **Nombre de bénéficiaires** des départs de 2017-2021 (loi 2017-51), de 2018 (loi 2018-5) et de
   2022-2025 (programme spécifique) : aucune source officielle lue. Pistes : CNRPS (guides
   statistiques, tableau des mises à la retraite par motif, comme pour 2009-2013 au livre
   « Retraites ») ; rapports sur le budget 2019-2021 et 2023 ; Cour des comptes (lecture à l'image
   des rapports 2018-2021) ; revues FMI de l'EFF 2017-2019.
2. **Coût budgétaire réalisé** de ces programmes (primes de départ, pensions avancées, part
   employeur) : non lu.
3. **Champ de l'INS** (point 0.2) : définition statutaire de la base INSAF à obtenir.
4. **Totaux des tableaux C/ت** 2020, 2022-2026 sur la dernière page de chaque tableau ; missions
   civiles autres que les quatre relevées ; séries 1990-2010 (tableau « C » des lois de finances,
   couche texte à décoder ou OCR).
5. **Rédaction actuelle des art. 17-20 de la loi 83-112** : lister les lois modificatives (1997, 2003, 2007, 2011, 2021) et lire les articles touchés ; aucune requête jouée.
6. **Décret 2012-3256, décret 2015-85, art. 32-33 de la LF 2013** : non lus.
7. **Rapports sur le budget 2015-2021, 2023, 2026** : non obtenus ; ce sont eux qui donnent les
   recrutements prévus par ministère pour ces années.
8. **Contexte de 1987** (plan d'ajustement, débats du 3 mars 1987) et de 2011 (accord sur la
   sous-traitance) dans les mots des sources de l'époque : non lu.
9. **Page de la loi 2018-5 dans l'édition française** (index : p. 265) : édition introuvable.

---

## 11. Recherches infructueuses : fiches proposées

`uv run python scripts/recherches.py lister` a été exécuté : aucune fiche existante ne couvre ces
objets (seule `r-chantiers-regionaux-texte-fondateur`, close au 2021-06-18, est voisine). Les
requêtes ci-dessous sont celles réellement lancées sur `jort_cache` (titres et objets) ; le plein
texte du corpus n'a pas été parcouru ; les fascicules inconnus de la base (outillage § 1 f) n'ont
pas été examinés. Dernière publication indexée : 2026-10-02.

```yaml
- id: r-titularisation-chantiers-2011
  objet: texte de 2011 (décret-loi, loi ou décret) portant titularisation ou intégration des ouvriers de chantiers ou des agents de sous-traitance dans le secteur public
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_like: ['%chantiers%', '%sous-traitance%', '%reintegr%', '%réintégr%', '%amnistie generale%', '%recrut%']
    titres_fts: ['(recrutement OR recrutements) AND (derogatoire OR derogatoires OR exceptionnel OR exceptionnelles OR exceptionnels OR chomeurs OR chomage OR "secteur public" OR amnistie OR martyrs OR integration OR titularisation)']
    iort_ar: [الحضائر, المناولة, المعاد إدماجهم, إعادة إدماج, العفو العام, انتداب]
    depuis: 2011-01-14
  periode:
    jusqu_au: 2011-12-31
    motif: prémisse « texte de 2011 » du ticket
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés et objets de jort_cache, 2011 (37 % d'intitulés arabes au second semestre) ; plein texte non parcouru ; aucun texte de 2011 sur les chantiers ou la sous-traitance ; textes trouvés : DL 2011-32 et décret 2011-544 (recrutement des chômeurs)"
    couvert_jusqu_au: 2011-12-31
    resultat: aucun
  a_faire: [plein texte des fascicules 2011 sur « مناولة » et « sous-traitance » ; circulaires du Premier ministère d'avril-mai 2011]

- id: r-lf-gel-recrutements-2017-2026
  objet: article de loi de finances (ou de loi de finances complémentaire) suspendant ou limitant les recrutements dans la fonction publique
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_like: ['%recrut%', '%retraite%', '%fonction publique%']
    iort_ar: [انتداب, الانتدابات, التقاعد, الأجور, المغادرة, الوظيفة العمومية]
    depuis: 2016-12-01
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: "intitulés d'articles de lois de finances indexés 2011-2026 (motifs ci-dessus croisés par ET avec « loi de finances » / « قانون المالية » / « بقانون المالية ») contenant « recrut », « انتداب », « التقاعد », « الأجور », « الوظيفة العمومية » ; articles trouvés : LF 2013 art. 77, LF 2018 art. 19, LF 2021 art. 12, LF 2026 art. 13, 57, 90, 92, 108 — aucun gel ; art. 9 des LF 2021-2026 lus (effectif autorisé) ; « تجميد » et « gel » non joués"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
  a_faire: [jouer « تجميد » et « gel » ; lire les circulaires de préparation du budget 2017-2019]

- id: r-depart-volontaire-fp-2014-2019
  objet: texte instituant un programme de départ volontaire ou de mise à la retraite anticipée dans la fonction publique en 2014, 2015 ou 2019
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_fts: ['"depart volontaire" OR "mise a la retraite anticipee" OR "retraite anticipee" OR "disponibilite speciale"']
    titres_like: ['%avant l%age legal%', '%depart volontaire%', '%départ volontaire%']
    iort_ar: [المغادرة الاختيارية, مغادرة, الإختيارية, التقاعد قبل السن القانونية, الإحالة على التقاعد قبل]
    depuis: 2014-01-01
  periode:
    jusqu_au: 2019-12-31
    motif: années citées par le ticket
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés et objets de jort_cache 2014-2019 (40 à 80 % d'intitulés arabes de 2015 à 2019, termes arabes joués) ; trouvés : loi 2014-48 et décret 2015-85 (Tunisie Télécom), loi 2017-51 et décret 2017-825, loi 2018-5, décret 2018-205 et deux arrêtés de 2018 ; rien pour 2015 ni 2019 ; plein texte non parcouru"
    couvert_jusqu_au: 2019-12-31
    resultat: aucun

- id: r-depart-volontaire-ep-2019
  objet: loi ou décret de départ volontaire ou de retraite anticipée propre aux entreprises publiques (autre que la loi 2014-48)
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_fts: ['("mise a la retraite" OR "retraite anticipee" OR licenciement OR compression OR depart) AND (societe OR office OR entreprise OR entreprises OR etablissements OR restructuration)']
    iort_ar: [التقاعد, المغادرة, التسريح]
    depuis: 2011-01-14
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache 1990-2026 (FTS) et 2011-2026 (arabe, croisé avec شركة, ديوان, المؤسسات العمومية, المنشآت) ; seuls la loi 2014-48 et le décret 2015-85 ; plein texte non parcouru ; arrêtés exclus"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun

- id: r-loi2025-18-application
  objet: décret ou arrêté d'application de la loi n° 2025-18 (plateforme, tranches de recrutement des diplômés chômeurs de longue durée)
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_like: ['%2025-18%', '%chomage%', '%chômage%', '%recrutement%', '%chomage de longue%', '%chômage de longue%']
    iort_ar: [طالت بطالتهم, انتداب, 18 لسنة 2025]
    depuis: 2025-12-23
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache du 2025-12-01 au 2026-10-02, hors arrêtés (nombreux arrêtés d'ouverture de concours non filtrés) ; seul texte voisin : décret 2026-12 (santé militaire) ; plein texte non parcouru ; fascicules 2026 inconnus de la base (n° 4, 8, 20, 32, 38, 66, 69, 85) non examinés"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun

- id: r-loi2020-38-decrets-application
  objet: décrets gouvernementaux d'application des art. 1 à 3 de la loi n° 2020-38
  ou: [À FIXER : ancre <!-- RECHERCHE --> du .qmd qui portera le constat]
  requetes:
    titres_like: ['%2020-38%', '%2021-27%', '%18 bis%', '%ouvriers de chantier%', '%dix ans et plus%', '%chomage de longue%', '%chômage de longue%']
    titres_fts: ['"2020-38" OR "2021-27" OR "2025-18" OR chantiers OR "longue duree"']
    iort_ar: [38 لسنة 2020, 27 لسنة 2021, 18 مكرر, عملة الحضائر, عمال الحضائر, طالت بطالتهم]
    depuis: 2020-08-19
  passes:
  - date: 2026-10-23
    role: documentaliste
    sources: [jort_cache]
    couverture: "intitulés de jort_cache 2020-08-19 à 2026-10-02 ; seuls trouvés : LF 2021 art. 12 (crédits pour 10 000 recrutements) ; aucun décret d'application ; plein texte non parcouru"
    couvert_jusqu_au: 2026-10-02
    resultat: aucun

```

Recherche non jouée, donc sans fiche : textes modifiant les art. 17 à 20 de la loi n° 83-112 (lacune 5).
Chaque `ou` est à fixer à l'ancre `<!-- RECHERCHE r-… -->` du `.qmd` qui portera le constat ;
`verifier` refuse une fiche dont l'ancre manque.

---

## 12. Textes à océriser ou à lire à l'image

| Document | Pourquoi | État |
|---|---|---|
| JORT n° 18 du 10 mars 1987 (`1987F/Jo01887.pdf`) | loi 87-7, loi 87-8, décrets 87-337 et 87-338 : scan sans couche texte, lu à l'image ; OCR pour citer d'autres articles et les débats | corpus local |
| JORT n° 82 des 13-16 décembre 1983 (`1983F/Jo08283.pdf`) | loi 83-112 : scan ; art. 2 et 17-20 lus à l'image ; OCR pour le reste du statut | corpus local |
| Tableaux F/ح et C/ت des LF 2020-2026 | images ; seules quatre missions et les totaux de l'effectif ont été relevés ; autres missions et dernière page des tableaux C/ت à lire ou océriser | corpus local (AR 2020, 2022-2026 ; FR 2021-2022) |
| Tableau « C » des LF 2000-2004 | couche texte décalée : tester le décodage +29 (outillage § 5) avant d'océriser | corpus local |
| Tableau « C » des LF 1990-1999 et 2005-2008 | tableau absent de la couche texte (images ou non reproduit) : vérifier à l'image | corpus local |
| Cour des comptes, clôture du budget 2018-2021 (`loireg2018` à `loireg2021`) | couche texte arabe partielle (aucune réponse à « كتلة الأجور » en 2019-2021) ; répartition par mission et suivi des départs à lire à l'image | tunisia-data |
| Décret n° 2012-3256 ; LF 2013 art. 32-33 | édition arabe seule (JORT n° 100/2012 ; n° 1/2013) | corpus local (AR) |
| Rapports sur le budget de l'État (AR) | couche texte à formes de présentation ; chiffres lus à l'image | tunisia-data |

## 13. Anomalies d'outillage (pour `docs/notes/outillage-sources.md`)

- `PDFs/JORT/2018/fr/Jo0082018.pdf` est l'édition **arabe** (n° 8 du 26 janvier 2018), identique
  octet pour octet à ce que pist.tn sert à `2018F/Jo0082018.pdf` ; absent de la liste des faux
  fascicules français (outillage § 3). `jort_cache` donne « p. 265 » pour la loi 2018-5 ; le pied
  de page arabe porte pp. 288-289.
- Le décret présidentiel n° 2022-542 (JORT n° 68/2022, p. 1898) n'est indexé ni par numéro ni par
  intitulé dans `jort_cache`.
- Les tableaux des lois de finances 2020-2026 sont des images (sans couche texte) ; 2011-2018 (FR)
  ont une couche texte exploitable ; 1990-2008 : tableau « C » non détecté par l'extraction.

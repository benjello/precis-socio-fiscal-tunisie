# L'éducation et la formation : plan d'un nouveau livre du précis

Note de plan du 17 octobre 2026, pour arbitrage de l'auteur avant toute rédaction et pour proposer
une contribution à un universitaire spécialiste de l'éducation et des prestations. Aucun chapitre
n'est écrit ; aucun `.qmd` n'est créé.

Le livre prend place dans la partie IV, « Les politiques sectorielles », du *Précis des politiques
publiques de la Tunisie*, à côté de la santé et de la compensation. Il suit la doctrine du découpage
en six parties du 17 octobre 2026 : suivre l'argent ; un fait, un seul domicile ; les ruptures au
premier plan ; aucun chiffre isolé ; ce qu'en dit l'économie, à part et daté ; un cadre commun
rapporté à la synthèse.

**En trois lignes.** L'éducation est d'abord une dépense de l'État servie en nature — un service
gratuit dans les établissements publics —, à laquelle s'ajoutent des transferts propres au secteur :
bourses, prêts, restauration et logement universitaires. Le livre suit cette dépense des textes
fondateurs (1958, 1989, 1991, 2002, 2008) jusqu'au coût par élève et par niveau, qui est la donnée que
la synthèse attend pour imputer aux ménages, par décile, le transfert en nature de l'éducation. Neuf
chapitres : présentation, histoire, trois dispositifs (scolaire, formation professionnelle,
supérieur), les aides aux élèves et aux étudiants, les comptes (jusqu'au coût par élève et aux bénéficiaires par décile), les résultats, les rapports et études.

---

## 0. Le degré de vérification des références

Chaque texte cité porte l'un de trois états.

| État | Ce qu'il garantit | Ce qu'il ne garantit pas |
|---|---|---|
| **lu** | le texte a été lu au fascicule du *Journal officiel*, aux articles indiqués | rien au-delà des articles indiqués |
| **index** | le texte existe : numéro, date de signature et fascicule (année/numéro) relevés à l'index du *Journal officiel* | son contenu ; aucune règle ne lui est attribuée ici sur la seule foi de son intitulé |
| **à vérifier** | rien : référence de mémoire ou déduite, à chercher | — |

Au 17 octobre 2026, deux textes seulement sont au niveau **lu** : le décret n° 2025-246 (visas et
article premier) et la loi d'orientation n° 2002-80 (article premier, et les articles sur la gratuité,
l'année préparatoire et l'obligation scolaire, dont le numéro est illisible dans l'extraction du
fascicule). Tous les autres sont au mieux **index**. Les numéros d'article proposés ci-dessous
pour les textes **index** sont donc des pistes de lecture, non des références.

---

## 1. Ce que le livre couvre, et ce qu'il laisse aux autres

### 1.1 L'objet

Le livre documente l'enseignement public et privé, du préscolaire au supérieur, et la formation
professionnelle initiale : son droit (obligation, gratuité, organisation, examens), son financement
(budgets des ministères, dépense par élève, part des dépenses de l'État et du PIB), les aides qui
n'existent que pour les élèves et les étudiants, ses résultats mesurés (scolarisation, examens,
abandon), et l'incidence de la dépense par décile.

Il ne couvre pas la recherche scientifique, y compris la part « recherche scientifique » du budget du
ministère de l'Enseignement supérieur (décision du 17 octobre 2026, ancienne Q10, fermée ; l'exception
antérieure pour ce qui est inséparable du budget du supérieur est supprimée), ni la
formation continue des salariés, financée par l'avance sur la taxe de formation professionnelle, ni les
programmes de formation de l'emploi, qui relèvent du chapitre « Les politiques de l'emploi » du livre
« Le marché du travail » (`marche_travail/_politiques_emploi.qmd`), ni la jeunesse et le sport. Décision
de l'auteur du 17 octobre 2026 (ancienne question Q1, fermée) : le livre garde la formation
professionnelle initiale (agence, centres, diplômes) ; la taxe de formation professionnelle reste à son
domicile actuel (`cotisations_sociales/_prelevements_salaires.qmd`, `@sec-cot-tfp`).

### 1.2 Le tableau de voisinage

La règle de la doctrine : un dispositif qui n'existe que pour un secteur vit dans le livre sectoriel ;
un cas d'un instrument général vit dans le livre de l'instrument.

| Sujet | Domicile | Ce que le livre de l'éducation en dit |
|---|---|---|
| Bourses scolaires, bourses et prêts universitaires | **éducation** | tout |
| Restauration et logement universitaires (offices des œuvres universitaires) | **éducation** | tout |
| Restauration scolaire (cantines) | **éducation** | tout ; les textes restent à identifier |
| Aide de rentrée scolaire et universitaire de l'Amen social, prise en charge des abonnements de transport scolaire et universitaire (arrêté conjoint de 2022) | **prestations sociales** (`_non_contributives.qmd`, `@sec-nc-aides`, `@tbl-nc-rentree-scolaire`) | une phrase, un lien ; la série des crédits peut être reprise en figure tirée des mêmes données |
| Subvention aux sociétés de transport pour les tarifs scolaires et universitaires | **compensation** (`_transport.qmd`) | une phrase, un lien ; la part « scolaire » du poste, si elle est isolable, en figure |
| Tarifs des abonnements scolaires (arrêté du 29 juillet 1998, index) | **compensation** | un lien |
| Rémunération, grilles et statuts des enseignants | **rémunérations publiques** | effectifs et masse salariale du secteur, une figure ; la règle de salaire, par renvoi |
| Taxe de formation professionnelle, avance sur la taxe | **financement et caisses de la sécurité sociale** (`cotisations_sociales/_prelevements_salaires.qmd`, `@sec-cot-tfp`) | une phrase sur ce que finance la taxe, un lien |
| Exonérations et avantages fiscaux de l'enseignement privé et de la restauration des élèves | **fiscalité** (dépenses fiscales) | une ligne par dispositif, un lien ; le coût, s'il est publié, en figure |
| Insertion des diplômés, chômage des diplômés, programmes d'emploi | **marché du travail** | un lien depuis les résultats |
| Formation continue des salariés et programmes de formation de l'emploi (hors formation professionnelle initiale) | **marché du travail** (`marche_travail/_politiques_emploi.qmd`, « Les politiques de l'emploi »), décision du 17 octobre 2026 | une phrase et un lien depuis le chapitre 3 |
| Offices des œuvres universitaires (restauration, logement, bourses) : comptes, effectifs de repas et de lits, rapports d'activité | **éducation**, quel que soit leur statut juridique (décision du 17 octobre 2026, ancienne Q7, fermée) | chapitres 5 et 6, tout ; le livre des entreprises publiques n'a qu'une ligne de renvoi dans son tableau de voisinage |
| Agence de la formation professionnelle, autres établissements publics du secteur, au sens de leurs comptes | **entreprises publiques** pour ceux qui y figurent ; sinon éducation | à examiner au cas par cas |
| Coût unitaire, bénéficiaires, imputation par décile | **éducation** pour les données d'entrée ; **redistribution** pour la composition | chapitre 6, sections 5 et 9 |

**Une lacune à signaler au livre voisin.** Le livre des rémunérations publiques ne parle aujourd'hui
d'aucun corps enseignant (aucune occurrence du mot « enseignant » dans ses chapitres). Le renvoi du
chapitre 6 vers lui est donc à construire des deux côtés. Les textes de 2024 sur le corps des
animateurs des jardins d'enfants (statut particulier, régime de rémunération, concordance des grades,
tous du 31 décembre 2024, JORT 2025/001, index) sont un exemple de ce qui lui revient.

### 1.3 Le lien avec la synthèse

Le livre fournit au cadre des finances publiques la dépense d'éducation par ministère, par niveau et
par nature, et au livre de la redistribution le **coût public par élève, par niveau, sourcé**, et le
**nombre d'élèves du public par niveau**. C'est le produit que l'exercice d'incidence de type CEQ sur
la Tunisie consomme : celui qui existe pour 2021 impute, par individu scolarisé dans le public, un coût
unitaire à trois niveaux (primaire ; secondaire ; supérieur), déclare le préscolaire « non
disponible » et n'impute rien à la formation professionnelle. Le livre vise à combler ces deux
manques et à dater la source de chaque coût unitaire.

---

## 2. Le plan en un tableau

| N° | Fichier pressenti | Titre de travail | Type (doctrine) | Chronologie suivie |
|---|---|---|---|---|
| 0 | `index.qmd` | Présentation | présentation | — |
| 1 | `_histoire.qmd` | De la loi de 1958 au Conseil supérieur de l'éducation et de l'enseignement | histoire (grandes réformes du livre) | 1958 → 2025 |
| 2 | `_scolaire.qmd` | L'enseignement scolaire : préscolaire, base, secondaire | dispositif | 1958, 1991, 2002, 2008 |
| 3 | `_formation_professionnelle.qmd` | La formation professionnelle initiale | dispositif | 1993, 2008 |
| 4 | `_superieur.qmd` | L'enseignement supérieur, public et privé | dispositif | 1960, 1989, 2000, 2008 |
| 5 | `_aides.qmd` | Les aides aux élèves et aux étudiants | dispositif | 1966/1971, 1970, 1986, 1988, 2009 |
| 6 | `_depense.qmd` | La dépense d'éducation : budgets, coût par élève, personnels, bénéficiaires | longue période (budgétaire) | séries |
| 7 | `_resultats.qmd` | Scolarisation, examens, abandon : les séries | longue période (séries d'effectifs) | séries |
| 8 | `_rapports_etudes.qmd` | Rapports et études : incidence, comparaisons, acquis | rapports et études | — |
| — | `_glossaire.qmd` | Glossaire | annexe | — |

Chaque chapitre de dispositif (2 à 5) se termine par une page « Ce qu'en dit l'économie », datée.
C'est, avec les documents qui ne paraissent pas au *Journal officiel*, le premier lieu où une
contribution universitaire pèse (§ 5).

---

## 3. Les chapitres

### Chapitre 0 — Présentation

**Objet.** L'objet en une phrase ; la carte des dispositifs avec leur texte fondateur ; une figure de
ce que pèse la dépense d'éducation sur la longue période (part des dépenses de l'État, et part du PIB
par segments de base) ; le plan ; les conventions de lecture ; le tableau de voisinage du § 1.2 ; une
frise des dates clés et de la filiation des textes (1958 → 1991 → 2002 ; 1960 → 1989 → 2008 ;
1993 → 2008 pour la formation professionnelle). La frise se lit contre la
périodisation commune du cadre des finances publiques : Protectorat, indépendance, expérience
collectiviste, années 1970, ajustement de 1986, années 1990-2000, 2011 et après. Les textes de
1986-1989 (bourses et prêts universitaires de 1986, offices des œuvres universitaires de 1988, loi sur
le supérieur de 1989) tombent dans la période de l'ajustement ; ce que ces textes en disent eux-mêmes
reste à lire.

**Séries visées.** Dépense des ministères de l'éducation, de l'enseignement supérieur et de la
formation professionnelle, en part des dépenses de l'État (sans base) et en part du PIB (base dite,
rupture à chaque changement de base, renvoi à `precis/fr/annexe-pib.qmd`).

**Sources.** Celles du chapitre 6.

### Chapitre 1 — Histoire : de la loi de 1958 au Conseil supérieur de l'éducation et de l'enseignement

**Objet.** Les grandes réformes du livre, dans l'ordre des dates, chacune avec ce que la loi cherche
dans ses propres mots (exposé des motifs, débats, plans de développement de l'époque). Le chapitre dit
qui est scolarisé, sous quelle autorité, avec quelle obligation et quelle gratuité ; le détail de
chaque ordre d'enseignement va aux chapitres 2 à 4.

**Sections proposées.**

1. *Avant 1958 : ce que l'indépendance trouve.* Les écoles du Protectorat (écoles publiques
   françaises, écoles franco-arabes), le collège Sadiki, l'enseignement de la Zitouna, les kouttabs.
   Aucun texte identifié à ce jour ; à écrire à partir des sources de l'époque et d'études d'histoire
   de l'éducation (à réunir). Un paragraphe court, sans texte au registre tant que rien n'est lu.
2. *La loi de 1958 : un système unifié.* Loi n° 58-118 du 4 novembre 1958 relative à l'enseignement.
   Ce que la loi reprend, ce qu'elle écarte (l'enseignement zitounien), ce qu'elle crée (cycles,
   durées, langue d'enseignement) — **à établir à la lecture** : aucun de ces points n'est lu.
3. *1960-1989 : l'université de Tunis, puis la loi de 1989 sur l'enseignement supérieur.* Décret
   n° 60-98 portant création et organisation de l'université de Tunis (publié au JORT n° 16 du
   31 mars 1960 selon l'intitulé de son rectificatif ; date de signature à vérifier) ; loi n° 89-70
   du 28 juillet 1989. Une ligne au chapitre 1, le contenu au chapitre 4.
4. *La loi de 1991 : l'école de base.* Loi n° 91-65 du 29 juillet 1991 relative au système éducatif.
   L'enseignement de base et l'obligation scolaire sont attendus dans ce texte : **à lire** avant de
   l'écrire.
5. *La loi d'orientation de 2002.* Loi d'orientation n° 2002-80 du 23 juillet 2002 relative à
   l'éducation et à l'enseignement scolaire, et son rectificatif. Lu : l'article premier fait de
   l'éducation une « priorité nationale absolue » et rend l'enseignement « obligatoire de six à seize
   ans » ; un article garantit « le droit à l'enseignement gratuit dans les établissements scolaires
   publics » ; l'année préparatoire « fait partie de l'enseignement de base » ; le tuteur qui n'inscrit
   pas son enfant, ou le retire avant seize ans, encourt une amende. Les numéros d'article de ces trois
   dernières dispositions et le montant de l'amende sont à relire à l'image. La loi n° 2008-9 du
   11 février 2008 la modifie (index ; contenu à lire).
6. *2008 : supérieur et formation professionnelle.* Loi n° 2008-19 du 25 février 2008 relative à
   l'enseignement supérieur ; décret n° 2008-3123 du 22 septembre 2008 fixant le cadre général du
   régime des études et les conditions d'obtention du diplôme national de licence (son rattachement au
   système dit « LMD » est à confirmer au texte) ; loi n° 2008-10 du 11 février 2008 relative à la formation professionnelle. Les dates de
   la première rentrée en licence LMD et du dernier diplôme de l'ancien régime sont **à vérifier**.
7. *Après 2011.* Le décret-loi n° 2011-46 du 25 mai 2011 portant création du centre national des
   technologies en éducation (index) est le seul texte d'organisation identifié à ce stade. Les
   consultations nationales sur la réforme du système éducatif, leurs rapports, la régularisation des
   enseignants suppléants (loi n° 2025-17 portant loi de finances pour 2026, article 107, selon
   l'intitulé arabe de l'index) : **à identifier et à lire**. Une recherche en termes arabes
   (التربية, المنظومة التربوية, التعليم العالي) reste à faire pour 2011-2026 ; la première passe, sur
   le seul terme التربية, ne rend que des textes de carrière.
8. *La Constitution de 2022 et le Conseil supérieur de l'éducation et de l'enseignement.* Constitution
   promulguée par le décret présidentiel n° 2022-691 du 17 août 2022 (index ; le texte est au numéro
   spécial, non au JORT n° 91 qui ne porte que le décret de promulgation) : l'article qui crée le
   Conseil est **à vérifier**. Le décret-loi n° 2024-2 du 16 septembre 2024 portant organisation du
   Conseil est connu par les visas du décret n° 2025-246 du 8 mai 2025, qui en fixe l'organisation
   administrative et financière (JORT 2025/054, p. 1222, **lu**) ; le fascicule du décret-loi n'est pas
   identifié. Le Conseil supérieur de l'éducation antérieur (décret n° 2000-2260 du 10 octobre 2000,
   index) est à rapprocher du nouveau Conseil.

**Tableau court au premier plan.** Une ligne par grande réforme : date d'effet, texte, ce que la loi
cherche (ses mots), ce qui change pour l'élève (obligation, durée, gratuité, orientation), portée
(rupture, étape, ajustement). Le registre complet, replié, sous chaque section.

**Séries visées.** Une seule au premier plan : les effectifs scolarisés par ordre d'enseignement sur
la longue période (renvoi au chapitre 7 pour le détail), pour situer chaque réforme.

**Sources.** JORT ; exposés des motifs et débats parlementaires (Chambre des députés) pour 1958, 1991,
2002, 2008 ; plans de développement ; rapports nationaux au Bureau international d'éducation
(UNESCO), qui décrivent le système à dates régulières ; études d'histoire de l'éducation en Tunisie
(à réunir, titres à vérifier).

### Chapitre 2 — L'enseignement scolaire : préscolaire, base, secondaire

**Objet.** Qui doit être scolarisé, où, combien de temps, à quel coût pour la famille, avec quels
examens et quelle orientation ; le public et le privé ; le préscolaire sous ses trois tutelles.

**Sections proposées.**

1. *Vue d'ensemble* : la pyramide des ordres d'enseignement à sa date, les effectifs par ordre et par
   secteur (public, privé), deux à quatre points.
2. *La mise en place* (1958) et *les grandes réformes* (1991, 2002, 2008), renvoyant au chapitre 1
   pour le contexte et ne gardant ici que ce qui change pour l'élève.
3. *L'état du droit à sa date* : obligation de six à seize ans (loi de 2002, art. 1er, **lu**) ;
   gratuité dans le public (loi de 2002, **lu**, article à préciser) ; ce que paient néanmoins les
   familles (frais d'inscription, assurance scolaire, fournitures — **à établir**, textes et arrêtés à
   identifier) ; qui est couvert et qui ne l'est pas (enfants hors école, abandon avant seize ans,
   avec la série qui le mesure, chapitre 7).
4. *Le préscolaire.* Trois réseaux, trois tutelles : les jardins d'enfants (ministère chargé de la
   femme et de l'enfance ; corps des animateurs, textes du 31 décembre 2024, index) ; les kouttabs
   (arrêté du 6 septembre 1980 portant réorganisation des kouttabs coraniques, modifié par l'arrêté du
   22 décembre 1990, index ; tutelle à vérifier) ; l'année préparatoire dans les écoles publiques (loi
   de 2002, **lu**). Le texte qui généralise l'année préparatoire et sa date sont **à vérifier**.
5. *L'enseignement de base et ses examens* : cycles, passages, examens nationaux (fin du primaire, fin
   de l'enseignement de base, concours d'entrée aux collèges et lycées pilotes) — **textes à
   identifier**.
6. *Le secondaire et le baccalauréat* : filières, régime de l'examen, part du contrôle continu —
   **textes à identifier**.
7. *L'enseignement privé* : décret n° 92-1187 du 22 juin 1992 relatif aux conditions d'obtention
   d'une autorisation pour la création d'établissements scolaires privés (index) ; arrêté du 8 juin
   1992 sur la proportion du personnel enseignant recruté à plein temps dans le privé (index) ; arrêté
   du 5 septembre 1993 sur les commissions consultatives régionales des établissements scolaires
   privés (index) ; la loi de 2008 modifiant la loi d'orientation (index ; s'il porte sur le privé, à
   lire). Avantages fiscaux : un renvoi à la fiscalité, qui en est le domicile (décision du 17 octobre
   2026, ancienne Q6).
8. *Les cours particuliers et de soutien* : leur encadrement réglementaire (**à identifier**) et leur
   poids dans la dépense des ménages (chapitre 6).
9. *Ce qu'en dit l'économie* (une page, datée) : obligation scolaire et durée des études ; gratuité et
   coûts privés de la scolarité ; enseignement privé et cours particuliers ; ce que les données
   tunisiennes permettent d'établir.

**Séries et tableaux visés.** Effectifs par ordre et par secteur ; taux de scolarisation par âge
(6-16 ans) ; part du privé par ordre ; effectifs du préscolaire par tutelle ; tableau daté de l'âge et
de la durée de l'obligation, et de la durée de chaque cycle, depuis 1958.

**Sources.** JORT ; ministère de l'Éducation (statistiques scolaires annuelles, « Statistiques de
l'éducation » — titre exact et première année à vérifier) ; INS (annuaire statistique, recensements
de 1966 à 2014 — liste à vérifier —, enquêtes sur le budget, la consommation et le niveau de vie des
ménages) ; ministère chargé de la femme et de l'enfance pour le préscolaire ; UNESCO-UIS.

### Chapitre 3 — La formation professionnelle initiale

**Objet.** La formation professionnelle comme voie de sortie du système scolaire : ses diplômes, ses
centres publics et privés, l'apprentissage, son financement par le budget et par la taxe de formation
professionnelle (par renvoi pour la taxe).

**Sections proposées.**

1. *Vue d'ensemble* : effectifs en formation initiale, public et privé, par niveau de diplôme.
2. *La mise en place* : loi n° 93-11 du 17 février 1993 portant création de l'Agence tunisienne de
   l'emploi et de l'Agence tunisienne de la formation professionnelle (index), complétée par le
   décret-loi n° 2022-78 du 21 décembre 2022 (index) ; loi n° 93-12 portant création d'un centre
   national de formation des formateurs et d'ingénierie de formation, modifiée par la loi n° 2003-77
   du 11 décembre 2003 (index pour 2003-77 ; la loi de 1993 elle-même à vérifier). Ce qui précédait
   1993 : **à établir**.
3. *La loi de 2008* : loi n° 2008-10 du 11 février 2008 relative à la formation professionnelle
   (index ; contenu à lire : diplômes, passerelles avec l'enseignement, rôle des entreprises).
4. *L'état du droit* : diplômes (certificat d'aptitude professionnelle, brevet de technicien
   professionnel, brevet de technicien supérieur — intitulés à vérifier dans la loi de 2008),
   apprentissage, centres privés.
5. *Le financement* : crédits budgétaires du ministère chargé de la formation professionnelle ; ce que
   finance la taxe de formation professionnelle (renvoi `@sec-cot-tfp`) ; avance sur la taxe (loi
   n° 2014-59 de finances pour 2015, article à lire, index) : une phrase et un lien, car l'avance
   finance la formation continue des salariés. La formation continue et les programmes de formation de
   l'emploi relèvent du livre du marché du travail (`marche_travail/_politiques_emploi.qmd`) : le
   chapitre y renvoie et ne les expose pas (décision du 17 octobre 2026, ancienne question Q1).
6. *Ce qu'en dit l'économie* : rendement de la formation professionnelle comparé à l'enseignement
   général ; apprentissage ; ce qui se mesure en Tunisie.

**Séries visées.** Effectifs en formation initiale par diplôme ; dépense budgétaire de la formation
professionnelle ; produit de la taxe (repris du livre du financement, mêmes données).

**Sources.** JORT ; Agence tunisienne de la formation professionnelle (rapports d'activité, à
vérifier) ; ministère chargé de la formation professionnelle ; INS ; Observatoire national de l'emploi
et des qualifications (publications à vérifier).

### Chapitre 4 — L'enseignement supérieur, public et privé

**Objet.** L'accès (baccalauréat, orientation), les établissements et leur statut, les diplômes, les
droits d'inscription, le privé, et l'insertion des diplômés par renvoi.

**Sections proposées.**

1. *Vue d'ensemble* : effectifs d'étudiants, public et privé, et diplômés, sur la longue période.
2. *La mise en place* : décret n° 60-98 (université de Tunis, index ; publié au JORT n° 16 du
   31 mars 1960, date de signature à vérifier).
3. *Les grandes réformes* : loi n° 89-70 du 28 juillet 1989 relative à l'enseignement supérieur et à
   la recherche scientifique (index, et son rectificatif) ; loi n° 92-50 du 18 mai 1992 relative aux
   instituts supérieurs des études technologiques et loi n° 92-51 du même jour (index) ; loi
   n° 2000-73 du 25 juillet 2000 relative à l'enseignement supérieur privé, modifiée par les lois
   n° 2006-50 du 24 juillet 2006 et n° 2008-59 du 4 août 2008 (index) ; loi n° 2008-19 du 25 février
   2008 relative à l'enseignement supérieur (index) et décret n° 2008-3123 (licence ; rattachement au
   LMD à confirmer au texte, index).
4. *L'état du droit* : statut des universités et des établissements ; orientation universitaire
   (textes annuels, à identifier) ; droits d'inscription dans le public (texte et montants **à
   identifier**) ; régime des études (LMD) ; formation pratique des étudiants (loi n° 2009-21 du
   28 avril 2009, index).
5. *Le privé* : agrément, effectifs, droits pratiqués s'ils sont publiés.
6. *Ce qu'en dit l'économie* : rendement privé et social du supérieur ; gratuité du supérieur et
   incidence ; chômage des diplômés (renvoi au marché du travail).

**Séries visées.** Étudiants par secteur, par domaine et par type d'établissement ; diplômés ; part
du privé ; dépense par étudiant (chapitre 6).

**Sources.** JORT ; ministère de l'Enseignement supérieur et de la Recherche scientifique
(« L'enseignement supérieur et la recherche scientifique en chiffres », annuel — titre à vérifier) ;
INS ; UNESCO-UIS ; Banque mondiale (études sectorielles, à réunir).

### Chapitre 5 — Les aides aux élèves et aux étudiants

**Objet.** Les transferts qui n'existent que pour les élèves et les étudiants : en espèces (bourses,
prêts) et en nature (restauration, logement), avec leurs conditions, leurs montants datés et leurs
bénéficiaires. C'est le chapitre le plus proche du livre des prestations ; la frontière est celle du
§ 1.2. Le chapitre s'ouvre sur un tableau qui place côte à côte toutes les aides au titre de la
scolarité, quel qu'en soit le livre, avec le lien vers leur domicile.

**Sections proposées.**

1. *Vue d'ensemble* : carte des aides, de l'élève du primaire à l'étudiant, avec le payeur
   (ministère, office, Amen social, société de transport) et le livre de domicile.
2. *Les bourses scolaires* : arrêté du 3 octobre 1966 relatif au règlement des bourses scolaires pour
   les enseignements du second et du premier degré (index) ; décret n° 71-356 du 28 septembre 1971
   fixant l'organisation et les conditions d'attribution des bourses scolaires pour les élèves de
   l'enseignement secondaire, modifié par les décrets n° 72-229 du 5 juillet 1972 et n° 74-783 du
   5 août 1974 (index) ; loi n° 76-115 de finances pour 1977, chapitre des mesures spéciales (index,
   portée à lire). La suite après 1974 et l'état actuel sont **à identifier**.
3. *Les bourses et prêts universitaires* : arrêté du 28 juillet 1986 fixant les modalités
   d'attribution (index) ; décret n° 86-688 du 10 juillet 1986, modifié par les décrets n° 90-219 du
   20 janvier 1990, n° 95-464 du 25 mars 1995 et n° 2001-2438 du 22 octobre 2001 (index) ; arrêté du
   29 mars 1995 (index) ; décret n° 2009-3040 du 19 octobre 2009 relatif aux bourses nationales et aux
   prêts universitaires, modifié par le décret n° 2012-2392 du 9 octobre 2012 (index) ; arrêté du
   26 octobre 2009 fixant les conditions d'attribution et de renouvellement (index) ; arrêtés du
   9 octobre 2012, l'un fixant les montants des bourses nationales d'études universitaires en Tunisie,
   l'autre modifiant l'arrêté de 2009 (index). Ce qui précède 1986, et les bourses d'études à
   l'étranger : **à identifier**. Tableau visé : plafond de revenu familial, montant mensuel ou annuel,
   nombre de mensualités, conditions de renouvellement, montant et remboursement du prêt, à chaque date.
4. *La restauration et le logement universitaires* : loi n° 70-9 du 10 mars 1970 portant création de
   l'Office national des œuvres universitaires (index) ; lois n° 88-135, 88-136 et 88-137 du
   3 décembre 1988 portant création des offices des œuvres universitaires pour le Nord, le Centre et
   le Sud (index), les deux dernières modifiées par les lois n° 96-89 et 96-90 du 6 novembre 1996
   (index) ; arrêtés de classement des établissements (2012, 2013, 2017, 2018, index) ; foyers
   universitaires privés (cahier des charges, arrêté du 30 octobre 2020 sur ses délais, index). Prix
   du repas et du lit, et leur histoire : **à identifier**. La part de l'État dans le coût du repas et
   du lit, si elle est publiée, est la grandeur que la synthèse attend. Les offices ont ici leur domicile,
   quel que soit leur statut (décision du 17 octobre 2026, ancienne Q7) : leurs comptes, leurs effectifs de
   repas et de lits et leurs rapports d'activité sont exposés dans ce chapitre. **À établir au texte
   qui les crée** : leur statut juridique exact (établissement public à caractère administratif ou non) ;
   la réponse ne change pas le domicile.
5. *La restauration scolaire* : cantines des écoles et internats des lycées — **aucun texte
   identifié** ; avantages fiscaux aux prestations de restauration des élèves et des apprenants (loi
   n° 2009-39 du 23 juin 2009, index), par renvoi à la fiscalité.
6. *Le transport scolaire et universitaire* : une phrase et deux liens (compensation pour la
   subvention aux sociétés ; prestations pour la prise en charge des abonnements des familles de
   l'Amen social).
7. *L'aide de rentrée des familles nécessiteuses* : une ligne de renvoi vers `@sec-nc-aides` et
   `@tbl-nc-rentree-scolaire`, rien de plus. L'aide de rentrée reste dans le livre des prestations
   sociales, instrument d'assistance, y compris son histoire avant l'Amen social (programme national
   d'aide aux familles nécessiteuses, aides du ministère de l'Éducation : à instruire dans ce
   livre-là) ; décision du 17 octobre 2026, ancienne Q3, fermée.
8. *Ce qu'en dit l'économie* : bourses sous condition de ressources et accès au supérieur ; prêts
   étudiants ; transferts conditionnels à la scolarisation.

**Séries visées.** Nombre de boursiers et de bénéficiaires de prêts par année universitaire ; montant
de la bourse en dinars courants et constants ; crédits budgétaires des bourses ; repas servis et lits
offerts ; part des boursiers parmi les étudiants.

**Sources.** JORT ; offices des œuvres universitaires (rapports d'activité, à vérifier) ; ministère de
l'Enseignement supérieur ; budgets des ministères (crédits des bourses, subventions aux offices) ;
lois de règlement.

### Chapitre 6 — La dépense d'éducation : budgets, coût par élève, personnels

**Objet.** Le budgétaire, en entonnoir : la dépense totale d'éducation de l'État, sa décomposition par
ministère, par niveau et par nature (rémunérations, fonctionnement, investissement, interventions),
puis les gros plans — coût par élève et par étudiant, masse salariale et effectifs enseignants, aides
du chapitre 5. Ensuite, à part et titrés comme tels, les chiffres des rapports extérieurs.

**Sections proposées.**

1. *Vue d'ensemble* : la dépense d'éducation en part des dépenses de l'État et en part du PIB (base
   dite, segments par base, renvoi à l'annexe du PIB).
2. *Le périmètre* : quels ministères, à quelles dates (éducation ; enseignement supérieur ; formation
   professionnelle ; tutelles du préscolaire ; affaires religieuses pour les kouttabs si elles en ont
   la charge). Chaque changement de périmètre ministériel est une rupture de série, signalée.
3. *Par nature* : rémunérations, fonctionnement, investissement, interventions ; les crédits
   extérieurs affectés (prêts ratifiés par loi : à recenser, les intitulés de l'index étant tronqués).
4. *Par niveau* : base, secondaire, supérieur, formation professionnelle, préscolaire public ; budget
   par programmes depuis sa mise en place (date **à vérifier**).
5. *Le coût public par élève et par étudiant* : dépense par niveau rapportée aux effectifs du public,
   avec la méthode écrite (quelles dépenses, quels effectifs, quelle année scolaire contre quelle
   année budgétaire). C'est la donnée que le livre de la redistribution attend.
6. *Les personnels* : effectifs enseignants et non enseignants, masse salariale ; la règle de salaire
   par renvoi aux rémunérations publiques ; les enseignants suppléants et contractuels (loi de
   finances pour 2026, art. 107, à lire).
7. *Les collectivités locales* : ce qu'elles dépensent pour l'éducation, s'il est isolable (Q8).
8. *La dépense des ménages* : frais de scolarité dans le privé, cours particuliers, fournitures, selon
   les enquêtes de l'INS sur la consommation des ménages (poste « enseignement »).
   Les comptes des offices des œuvres universitaires (subvention de l'État, recettes propres, dépenses de
   restauration et de logement) entrent dans la dépense d'éducation de cette section ; le livre des
   entreprises publiques n'en parle que par une ligne de renvoi (décision du 17 octobre 2026).
9. *Les bénéficiaires par décile* : élèves du public par niveau et par décile de niveau de vie
   (enquêtes de l'INS), en figure tirée des mêmes données que le livre de la redistribution, qui
   compose l'incidence ; la méthode CEQ y vit, et ce chapitre la résume en une phrase et un lien.

**Séries visées.** Dépense par ministère depuis 1958 si les lois de finances le permettent ; part des
dépenses de l'État ; part du PIB par segments de base ; coût par élève par niveau (tableau des coûts
unitaires par niveau et par année, chacun avec sa source) ; effectifs enseignants ; dépense des
ménages par décile ; bénéficiaires du public par décile.

**Périmètre : la recherche est exclue** (décision du 17 octobre 2026, ancienne Q10). Les totaux et les
ratios du chapitre (part dans les dépenses de l'État, part du PIB, coût par élève ou par étudiant)
excluent la recherche scientifique. Quand la source ne permet pas de l'isoler (la recherche est fondue
dans l'enseignement supérieur en gestion en 2002-2004 et depuis 2019), le chapitre le dit comme réserve
de périmètre dans la note de lecture, sans la déduire par une estimation. Les lignes de recherche
identifiables au budget (ministère ou programme propre, ligne par nature) sont signalées dans l'onglet
« Données » de la figure ou du tableau, **hors total** ; elles ne sont jamais ajoutées à la dépense
d'éducation.

**Sources.** Lois de finances et budgets des ministères (JORT pour les lois ; décrets de répartition
des crédits) ; lois de règlement ; publications du ministère des Finances (budget citoyen, rapports
sur le budget) ; budget par programmes des ministères ; INS (comptes nationaux, enquêtes ménages) ;
les chiffres de la Banque mondiale et de l'UNESCO-UIS vont au chapitre 8, non ici : ce chapitre est
budgétaire seulement.

### Chapitre 7 — Scolarisation, examens, abandon : les séries

**Objet.** Les résultats mesurés, sur la longue période, ruptures de définition expliquées.

**Sections proposées.**

1. *Scolarisation* : taux bruts et nets par ordre, par sexe et par région ; préscolaire ; supérieur.
2. *Examens* : taux de réussite à l'examen de fin du primaire (tant qu'il a existé), au diplôme de fin
   de l'enseignement de base, au baccalauréat ; candidats et admis.
3. *Redoublement et abandon* : taux par niveau, sorties sans diplôme, enfants de 6 à 16 ans hors école
   (la population que l'obligation de 2002 ne couvre pas en fait).
4. *Alphabétisation* : taux d'analphabétisme par recensement (programmes d'alphabétisation des adultes,
   textes à identifier).
5. *L'insertion des diplômés* : renvoi au marché du travail.

**Sources.** Ministère de l'Éducation et ministère de l'Enseignement supérieur (statistiques
annuelles) ; INS (recensements, enquêtes emploi, annuaire). Les évaluations internationales (PISA,
TIMSS) et les séries de l'UNESCO-UIS vont au chapitre 8.

### Chapitre 8 — Rapports et études

**Objet.** Ce que disent de la dépense, de son incidence et des résultats de l'éducation tunisienne
les institutions internationales et les études, chacune avec sa méthode (qui, quelles données, quel
périmètre, quel calcul), à part du budgétaire. Le chapitre ne refait pas l'exercice d'incidence : le
livre de la redistribution le compose, à partir des coûts unitaires et des bénéficiaires du
chapitre 6.

**Sections proposées.**

1. *Les études d'incidence de la dépense d'éducation* : l'étude CEQ sur la Tunisie à partir de
   l'enquête de 2010 (Commitment to Equity Institute, document de travail, titre et année à
   vérifier) ; l'exercice sur l'enquête de 2021 (rapport et éditeur à vérifier) ; les revues de la
   Banque mondiale qui traitent de l'incidence (à réunir). Pour chacune : quelle enquête, quels
   niveaux, quel coût unitaire et quelle source pour ce coût, transfert brut ou net des frais, et les
   hypothèses (coût moyen et non marginal, qualité identique entre régions, aucune valeur imputée au
   privé). Les bourses y sont des transferts directs, rangés avec les prestations.
2. *Ce que rapportent la Banque mondiale et l'UNESCO-UIS sur la dépense* : dépense publique
   d'éducation, dépense par élève, comparaisons internationales, chaque chiffre avec son périmètre.
   Une superposition avec la série budgétaire du chapitre 6 est permise sur un graphique, familles
   distinguées et ruptures expliquées.
3. *Les évaluations des acquis* : PISA, TIMSS (années de participation de la Tunisie à vérifier),
   avec la méthode de chaque enquête.
4. *Les enquêtes de scolarisation auprès des ménages* : MICS (éditions à vérifier).

**Séries et tableaux visés.** Tableau des études d'incidence (enquête, niveaux, coût unitaire,
résultat par décile) ; dépense d'éducation selon l'UNESCO-UIS, superposée à la série budgétaire.

**Sources.** Études CEQ ; Banque mondiale ; UNESCO-UIS ; OCDE (PISA) ; IEA (TIMSS) ; UNICEF (MICS) ;
INS (enquête nationale sur le budget, la consommation et le niveau de vie des ménages : édition de
2021 ; éditions antérieures à vérifier).

---

## 4. Les sources à réunir

| Famille | Source | Ce qu'on en attend | État |
|---|---|---|---|
| Droit | JORT (édition française et arabe, `pist.tn`) | textes fondateurs, décrets d'application, arrêtés de montants | index pour l'essentiel ; fascicules de 1958 et 1991 sans couche de texte ; lacunes du corpus local à l'automne 2024 |
| Droit | Numéro spécial de la Constitution de 2022 | article sur le Conseil supérieur de l'éducation et de l'enseignement | à obtenir |
| Débats | Chambre des députés, exposés des motifs | ce que cherchent les lois de 1958, 1991, 2002, 2008 | à obtenir |
| Budgétaire | Lois de finances, décrets de répartition des crédits, lois de règlement | dépense par ministère et par nature | à dépouiller |
| Budgétaire | Ministère des Finances : rapports sur le budget, budget par programmes | dépense par programme, coût par élève publié | à réunir |
| Statistique | Ministère de l'Éducation : statistiques scolaires annuelles | effectifs, examens, abandon, enseignants | à réunir (titres et années à vérifier) |
| Statistique | Ministère de l'Enseignement supérieur : « en chiffres » | étudiants, diplômés, boursiers | à réunir |
| Statistique | INS : annuaires, recensements, enquêtes ménages, comptes nationaux | scolarisation, dépense des ménages, PIB par base | partiellement disponible |
| Rapports d'activité | Offices des œuvres universitaires ; Agence tunisienne de la formation professionnelle | repas, lits, boursiers ; effectifs en formation | à chercher ; documents hors JORT |
| Rapports extérieurs | Banque mondiale (revues de la dépense, études sectorielles) | dépense, incidence, comparaisons | à réunir, titres à vérifier |
| Rapports extérieurs | UNESCO-UIS ; rapports nationaux au Bureau international d'éducation | séries internationales comparables, descriptions du système | à télécharger |
| Évaluations | PISA, TIMSS, MICS | acquis, scolarisation par décile | à télécharger |
| Études | Études CEQ sur la Tunisie | incidence par décile | à récupérer (PDF dans `tunisia-data`) |
| Études | Travaux universitaires tunisiens : rendements de l'éducation, abandon, privé | « Ce qu'en dit l'économie » | à indiquer par l'universitaire associé |

Toute étude citée est récupérée en PDF et cataloguée dans `tunisia-data`, selon les conventions.

---

## 5. Ce qu'un universitaire associé peut apporter, chapitre par chapitre

La doctrine propose quatre degrés de contribution : relire, transmettre des documents, trancher les
questions ouvertes, écrire ou relire « Ce qu'en dit l'économie ». Pour ce livre :

| Chapitre | Relire | Documents hors JORT | Questions à trancher | Ce qu'en dit l'économie |
|---|---|---|---|---|
| 1 Histoire | oui | études d'histoire de l'éducation, exposés des motifs | classement des réformes après lecture de leurs textes (Q2) | — |
| 2 Scolaire | oui | statistiques scolaires anciennes, textes sur les examens | frais à la charge des familles | obligation, gratuité, privé, cours particuliers |
| 3 Formation professionnelle initiale | oui | rapports de l'agence | — (formation continue : marché du travail) | rendement de la formation professionnelle |
| 4 Supérieur | oui | « en chiffres », droits d'inscription | — | rendement du supérieur, gratuité |
| 5 Aides | **en priorité** | arrêtés de montants, rapports des offices | frontière avec les prestations (Q4) | bourses, prêts, transferts conditionnels |
| 6 Dépense | oui | coûts par élève publiés par les ministères | périmètre (Q8, lacune) | — |
| 8 Rapports et études | **en priorité** | études d'incidence | méthode du coût unitaire (Q9) | incidence de la dépense d'éducation |

---

## 6. Ordre de travail

1. **Le pilote : le chapitre 5, bourses et prêts universitaires.** La chaîne des textes est identifiée
   à l'index (1986 → 1990 → 1995 → 2001 → 2009 → 2012, et les arrêtés de 1986, 1995, 2009, 2012) ; elle
   porte des paramètres (plafonds, montants, durées) qui se prêtent à un tableau daté ; c'est un
   transfert, au cœur de la compétence de l'universitaire associé. Lire les textes au fascicule,
   dresser le tableau, puis chercher les arrêtés de montants postérieurs à 2012.
2. **En parallèle : la série de la dépense par ministère** (chapitre 6, sections 1 à 3), sur les lois
   de finances et les lois de règlement, en commençant par les années récentes (budget par programmes)
   puis en remontant. Elle donne au livre son dénominateur et au cadre des finances publiques sa ligne
   « éducation ».
3. **Lire les cinq textes fondateurs** — lois n° 58-118, 89-70, 91-65, 2002-80 (relecture à l'image
   pour les numéros d'article), 2008-19 — et la loi n° 2008-10 : ils donnent la frise et le tableau
   court du chapitre 1. Les fascicules français de 1958 (n° 89) et de 1991 (n° 55) sont dans le corpus
   local, mais sans couche de texte : les lire à l'image ou les océriser.
4. **Le coût par élève et les bénéficiaires** (chapitre 6, sections 5 et 9),
   en liaison avec le livre de la redistribution, dès que la série de la dépense existe pour une année
   d'enquête (2021 d'abord).
5. **Les statistiques scolaires** (chapitre 7) : réunir les annuaires du ministère et de l'INS, fixer
   les définitions, repérer les ruptures.
6. **Les chapitres 2 à 4**, dans l'ordre scolaire, supérieur, formation professionnelle.
7. **Les pages « Ce qu'en dit l'économie »**, avec l'universitaire associé, en commençant par celle
   des aides (chapitre 5).
8. **Le reste du chapitre 1** (avant 1958, après 2011), qui dépend de sources hors JORT.

---

## 7. Questions ouvertes

- **Q1. Le périmètre de la formation professionnelle. FERMÉE le 17 octobre 2026.** La formation
  continue des salariés, financée par l'avance sur la taxe de formation professionnelle, et les
  programmes de formation de l'emploi vont au livre du marché du travail (« Les politiques de
  l'emploi ») ; le livre de l'éducation garde la formation professionnelle initiale ; la taxe reste
  à son domicile (`@sec-cot-tfp`).
- **Q2. Les ruptures. FERMÉE le 17 octobre 2026**, sous réserve de la lecture des textes. Le passage au
  système LMD est une rupture. 1989 est une étape, sauf si le texte lu crée un nouveau public ou un
  nouvel objectif (alors la reclasser, en le disant). Après 2011, ne retenir comme rupture que ce que les
  textes établissent, par exemple le Conseil supérieur de l'éducation et de l'enseignement inscrit dans la
  Constitution de 2022. Les candidates 1958, 1991, 2002 et 2008 ne sont confirmées qu'après lecture de
  leurs textes. *Point de fait : ces textes (lois n° 58-118, 89-70, 91-65, 2002-80, 2008-9, 2008-19 et
  2008-10) ont déjà été lus à l'image par le documentaliste (note d'histoire) ; la première version du
  livre en tire un classement provisoire, avec l'autre lecture écrite, que la revue confirme.*
- **Q3. L'aide de rentrée. FERMÉE le 17 octobre 2026.** L'aide de rentrée scolaire et universitaire
  reste dans le livre des prestations sociales (`_non_contributives.qmd`, `@sec-nc-aides`,
  `@tbl-nc-rentree-scolaire`) ; le livre de l'éducation n'en dit qu'une ligne de renvoi, dans son
  tableau de voisinage et au chapitre 5. Les bourses et les prêts universitaires ont leur domicile au
  chapitre 5 : le pilote du plan reste valable.
- **Q4. Les bourses dans la synthèse. FERMÉE le 17 octobre 2026.** Oui : les bourses sont aussi
  montrées dans la carte des prestations, par une figure tirée des mêmes données (nombre de boursiers et
  montants), sans les décrire deux fois. Le domicile reste le livre de l'éducation, chapitre 5.
- **Q5. Le préscolaire. FERMÉE le 17 octobre 2026.** Le préscolaire public est traité comme un
  transfert en nature ; le préscolaire privé, par sa seule réglementation.
- **Q6. Les avantages fiscaux de l'enseignement privé. FERMÉE le 17 octobre 2026.** Leur domicile est
  la fiscalité, au rapport sur les dépenses fiscales ; le livre de l'éducation n'en garde qu'un renvoi.
  (La loi de finances pour 1989, loi n° 88-145, porte à son chapitre des dispositions à caractère social
  et culturel une exonération des établissements d'enseignement, à l'intitulé tronqué à l'index : à lire
  pour le livre de la fiscalité.)
- **Q7. Les offices des œuvres universitaires. FERMÉE le 17 octobre 2026.** Leur domicile est le livre
  de l'éducation (chapitres 5 et 6), quel que soit leur statut juridique. Reste à établir, au texte qui
  les crée (lois n° 88-135 à 88-137, modifiées en 1996 ; décret n° 2006-2245 pour l'office du Nord),
  s'ils sont des établissements publics à caractère administratif ou non : la réponse ne change pas le
  domicile.
- **Q8. Les collectivités. PARTIELLEMENT INSTRUITE le 23 octobre 2026 (communes ; voir `education-collectivites-2026-10-23.md`, section `#sec-educ-depense-collectivites`) : la nomenclature communale de 2020 isole un article d'interventions dans l'enseignement et la formation et les revenus des jardins d'enfants, rien pour la construction ni l'entretien des écoles ; les conseils régionaux restent à lire. Énoncé d'origine :** Les
  communes et les conseils régionaux ont-ils, ou ont-ils eu, une dépense d'éducation isolable
  (construction et entretien des écoles) ? Le livre des finances locales dit déjà que la commune
  partage l'entretien des écoles avec l'autorité centrale et exerce par transfert la construction et
  l'entretien des établissements d'éducation (`finances_locales/_competences.qmd`, `@tbl-fl-comp-commune`,
  code des collectivités locales, loi organique n° 2018-29, art. 243 pour les compétences partagées et
  art. 244 pour les compétences transférées) : le chapitre 6 y renvoie sans le
  redire, n'a aucune ligne « collectivités » dans ses totaux ni dans ses ratios, et dit en une phrase de
  périmètre que cette dépense n'est pas isolée. À établir : les budgets des communes et des conseils
  régionaux (livre des finances locales, « Budgets et comptes ») permettent-ils d'isoler une dépense
  d'éducation ? Fiche de recherche `r-educ-collectivites-depense-education`.
- **Q9. Le coût unitaire. FERMÉE le 17 octobre 2026.** Commencer par les trois coûts moyens de
  l'exercice d'incidence de 2021 (primaire, secondaire, supérieur) ; viser plus fin (base séparée en
  primaire et collège, formation professionnelle, préscolaire public) seulement si les données du
  ministère le permettent. La source documentaire des trois coûts reste à établir avant toute valeur :
  d'ici là, le chapitre 6 ne publie aucun coût par élève.
- **Q10. La recherche. FERMÉE le 17 octobre 2026.** La recherche scientifique est retirée de la
  dépense d'éducation, y compris la part « recherche scientifique » du budget du ministère de
  l'Enseignement supérieur. Totaux et ratios l'excluent ; ce que la source ne permet pas d'isoler fait
  l'objet d'une réserve de périmètre, sans estimation ; les lignes identifiables sont signalées dans
  l'onglet « Données », hors total.
- **Q11. Le titre. FERMÉE le 17 octobre 2026.** « L'éducation et la formation » (le dossier du livre
  reste `precis/fr/education/`).

---

## 8. Annexe de travail : les références et leur état

Cette annexe s'adresse à la rédaction ; elle n'est pas à montrer telle quelle. « recid » : identifiant
de la notice dans `~/projets/PDFs-legislation-tunisie/jort_cache.db` ; « JORT » : année/numéro du
fascicule.

### 8.1 Lus

| Texte | JORT | recid | Ce qui est lu |
|---|---|---|---|
| Décret n° 2025-246 du 8 mai 2025, organisation administrative et financière du Conseil supérieur de l'éducation et de l'enseignement | 2025/054, p. 1222 | 197307 | visas (dont le décret-loi n° 2024-2 du 16 septembre 2024), article premier |
| Loi d'orientation n° 2002-80 du 23 juillet 2002 | 2002/062 | 111244 | article premier ; articles sur la gratuité, l'année préparatoire, l'obligation et l'amende (numéros et montants illisibles dans l'extraction : texte à police décalée, à relire à l'image) |

### 8.2 Attestés à l'index (existence, numéro, date, fascicule)

| Texte | JORT | recid |
|---|---|---|
| Loi n° 58-118 du 4 novembre 1958 relative à l'enseignement | 1958/089, p. 1056-1060 | 118226 |
| Décret n° 60-98, université de Tunis : notice du rectificatif (JORT n° 24), qui renvoie au JORT n° 16 du 31 mars 1960 ; date de signature à vérifier | 1960/024 | 106960 |
| Arrêté du 3 octobre 1966, règlement des bourses scolaires | 1966/043 | 71970 |
| Loi n° 70-9 du 10 mars 1970, Office national des œuvres universitaires | 1970/013 | 116848 |
| Décret n° 71-356 du 28 septembre 1971, bourses scolaires du secondaire | 1971/043 | 103336 |
| Décret n° 72-229 du 5 juillet 1972 (modifie le 71-356) | 1972/028 | 103119 |
| Décret n° 74-783 du 5 août 1974 (modifie le 71-356) | 1974/052 | 102157 |
| Loi n° 76-115 du 31 décembre 1976, loi de finances pour 1977 (mesures spéciales ; portée à lire) | 1976/083 | 115846 |
| Arrêté du 6 septembre 1980, réorganisation des kouttabs coraniques | 1980/051 | 67110 |
| Décret n° 86-688 du 10 juillet 1986, bourses nationales et prêts universitaires | 1986/041 | 95330 |
| Arrêté du 28 juillet 1986, modalités d'attribution des bourses et prêts | 1986/044 | 64606 |
| Lois n° 88-135, 88-136, 88-137 du 3 décembre 1988, offices des œuvres universitaires | 1988/083 | 113900, 113901, 113902 |
| Loi n° 88-145 du 29 décembre 1988, loi de finances pour 1989 (exonération des établissements d'enseignement, intitulé tronqué) | 1988/087 | 113860 |
| Loi n° 89-70 du 28 juillet 1989, enseignement supérieur et recherche scientifique | 1989/054 (rectificatif 1989/061) | 113755, 113738 |
| Décret n° 90-219 du 20 janvier 1990 (modifie le 86-688) | 1990/008 | 93532 |
| Arrêté du 22 décembre 1990 (modifie l'arrêté sur les kouttabs) | 1990/001 (sic à l'index) | 62845 |
| Loi n° 91-65 du 29 juillet 1991 relative au système éducatif | 1991/055 | 113404 |
| Lois n° 92-50 et 92-51 du 18 mai 1992, instituts supérieurs des études technologiques | 1992/033 | 113224, 113225 |
| Arrêté du 8 juin 1992, personnel enseignant à plein temps dans le privé | 1992/041 | 62346 |
| Décret n° 92-1187 du 22 juin 1992, établissements scolaires privés | 1992/041 | 92392 |
| Loi n° 93-11 du 17 février 1993, Agence tunisienne de l'emploi et Agence tunisienne de la formation professionnelle | 1993/014 | 113087 |
| Arrêté du 5 septembre 1993, commissions consultatives des établissements scolaires privés | 1993/073 | 61905 |
| Décret n° 95-464 du 25 mars 1995 (modifie le 86-688) ; arrêté du 29 mars 1995 | 1995/026 ; 1995/028 | 91006 ; 61378 |
| Lois n° 96-89 et 96-90 du 6 novembre 1996 (offices du Centre et du Sud) | 1996/090 | 112392, 112393 |
| Arrêté du 29 juillet 1998, tarifs des abonnements scolaires | 1998/063 | 59884 |
| Loi n° 2000-73 du 25 juillet 2000, enseignement supérieur privé | 2000/060 | 111658 |
| Décret n° 2000-2260 du 10 octobre 2000, Conseil supérieur de l'éducation | 2000/082 | 87926 |
| Décret n° 2001-2438 du 22 octobre 2001 (modifie le 86-688) | 2001/086 | 87164 |
| Loi d'orientation n° 2002-80, rectificatif | 2002/069 | 111237 |
| Loi n° 2003-77 du 11 décembre 2003 (modifie la loi n° 93-12) | 2003/100 | 111046 |
| Loi n° 2006-50 du 24 juillet 2006 (modifie la loi n° 2000-73) | 2006/060 | 110317 |
| Loi n° 2008-9 du 11 février 2008 (modifie la loi d'orientation n° 2002-80) | 2008/014 | 110063 |
| Loi n° 2008-10 du 11 février 2008, formation professionnelle | 2008/014 | 110064 |
| Loi n° 2008-19 du 25 février 2008, enseignement supérieur | 2008/019 | 110043 |
| Loi n° 2008-59 du 4 août 2008 (modifie la loi n° 2000-73) | 2008/064 | 109846 |
| Décret n° 2008-3123 du 22 septembre 2008, cadre général du régime des études de la licence (rattachement au LMD à confirmer) | 2008/079 | 82489 |
| Loi n° 2009-21 du 28 avril 2009, formation pratique des étudiants | 2009/035 | 109755 |
| Loi n° 2009-39 du 23 juin 2009, avantages fiscaux à la restauration des élèves et apprenants | 2009/051 | 109742 |
| Décret n° 2009-3040 du 19 octobre 2009, bourses nationales et prêts universitaires | 2009/084 | 81609 |
| Arrêté du 26 octobre 2009, conditions d'attribution et de renouvellement | 2009/087 | 53432 |
| Décret-loi n° 2011-46 du 25 mai 2011, centre national des technologies en éducation | 2011/039 | 80644 |
| Décret n° 2012-2392 du 9 octobre 2012 (modifie le 2009-3040) ; arrêtés du 9 octobre 2012 (montants ; modification de l'arrêté de 2009) | 2012/083 | 79827 ; 51879, 51878 |
| Arrêtés de classement des établissements des œuvres universitaires (16 octobre 2012 ; 25 janvier et 27 mai 2013 ; 1er mars 2017 ; 17 septembre 2018) | 2012/086 ; 2013/011, 2013/047 ; 2017/019 ; 2018/077 | 51833 ; 51572, 51280 ; 49378 ; 48538 |
| Loi n° 2014-59 du 26 décembre 2014, loi de finances pour 2015 (avance sur la taxe de formation professionnelle) | 2014/105 | 109129 |
| Arrêté du 30 octobre 2020, foyers universitaires privés | 2020/110 | 148170 |
| Décret présidentiel n° 2022-691 du 17 août 2022, promulgation de la Constitution | 2022/091 | 169118 |
| Décret-loi n° 2022-78 du 21 décembre 2022 (complète la loi n° 93-11) | 2022/142 | 170458 |
| Textes du 31 décembre 2024 sur le corps des animateurs des jardins d'enfants (statut, rémunération, concordance) | 2025/001 | 195058, 195059, 195060 |
| Loi n° 2025-17 du 12 décembre 2025, loi de finances pour 2026, art. 107 (enseignants suppléants, intitulé arabe) | 2025/148 | 201616 |

### 8.3 À vérifier

- Article de la Constitution de 2022 qui institue le Conseil supérieur de l'éducation et de
  l'enseignement (texte au numéro spécial, non au JORT n° 91 de 2022).
- Date de signature du décret n° 60-98 (université de Tunis), publié au JORT n° 16 du 31 mars 1960.
- Rattachement du décret n° 2008-3123 au système LMD.
- Décret-loi n° 2024-2 du 16 septembre 2024 portant organisation du Conseil : connu par les visas du
  décret n° 2025-246 ; absent de l'index, absent des fascicules français de 2024 du corpus local
  (qui en compte des lacunes à l'automne).
- Contenu de la loi n° 58-118 (cycles, langue, sort de l'enseignement zitounien) : fascicule français
  de 1958 présent dans le corpus local sans couche de texte.
- Contenu de la loi n° 91-65 (école de base, obligation) : fascicule français de 1991 présent dans le
  corpus local sans couche de texte.
- Numéros d'article et montant de l'amende dans la loi n° 2002-80 (relecture à l'image).
- Contenu de la loi n° 2008-9 (portée sur le privé ?).
- Loi n° 93-12 du 17 février 1993 (centre national de formation des formateurs) : connue par
  l'intitulé de la loi n° 2003-77, sans notice propre consultée.
- Date de la première rentrée en licence LMD et texte qui l'organise avant 2008.
- Texte de généralisation de l'année préparatoire et sa date.
- Tutelle des kouttabs (ministère des Affaires religieuses ou autre) à chaque date.
- Textes des examens nationaux (fin du primaire, fin de l'enseignement de base, baccalauréat,
  concours des collèges et lycées pilotes).
- Frais d'inscription dans le public, scolaire et universitaire, et leurs montants.
- Textes de la restauration scolaire (cantines, internats).
- Bourses scolaires après 1974 ; bourses universitaires avant 1986 ; bourses d'études à l'étranger.
- Prix du repas et du lit universitaires, et leur histoire.
- Aide de rentrée antérieure à l'Amen social (relève du livre des prestations sociales, Q3).
- Textes de réforme après 2011 (consultations nationales, rapports), recherche en termes arabes.
- Encadrement réglementaire des cours particuliers.
- Mise en place du budget par programmes des ministères de l'éducation.
- Titres et années des publications statistiques : statistiques scolaires du ministère de
  l'Éducation, « en chiffres » du ministère de l'Enseignement supérieur, rapports d'activité des
  offices et de l'Agence tunisienne de la formation professionnelle.
- Années de participation de la Tunisie à PISA, TIMSS, MICS.
- Études d'incidence CEQ sur la Tunisie (enquêtes de 2010 et de 2021) : titres, éditeurs, années ;
  source documentaire des coûts unitaires par niveau employés en 2021.
- Revues de la dépense publique et études sectorielles de la Banque mondiale sur l'éducation en
  Tunisie : titres et années.

### 8.4 Où sont les pièces

- Doctrine : `~/Downloads/precis-politiques-publiques-doctrine-structure-2026-10-17.pdf`.
- Modèle de structure : `precis/fr/sante/_quarto.yml` et ses chapitres.
- Frontières : `precis/fr/prestations_sociales/_non_contributives.qmd` (`@sec-nc-aides`,
  `@tbl-nc-rentree-scolaire`) ; `precis/fr/compensation/_transport.qmd` ;
  `precis/fr/cotisations_sociales/_prelevements_salaires.qmd` (`@sec-cot-tfp`) ;
  `precis/fr/fiscalite/_depenses_fiscales.qmd`.
- Exercice d'incidence de 2021 : `~/projets/ceq-tunisie/CEQ_TUN21_March2025/2.DoFiles/09_Education.do`
  (imputation par coût unitaire à trois niveaux ; préscolaire déclaré non disponible) et la feuille
  « Education » du classeur `3.Results/TUN_FiscalSim21_Sim2024_11March2025.xlsm` (trois coûts
  unitaires, unité et source à établir ; valeurs non reprises ici).
- Corpus du *Journal officiel* : `~/projets/PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`. Le
  fascicule français n° 62 de 2002 est en police décalée : le texte extrait se décode par un décalage
  de 29 points de code, les chiffres se perdent ; relire à l'image.

---

## 9. Textes à lire à l'image, et ticket proposé pour le documentaliste

*Point de départ.* Les fascicules sans couche de texte des textes fondateurs (1958 n° 89, 1989 n° 54 et
61, 1991 n° 55) ont déjà été océrisés et lus à l'image pour la première version du livre. Restent, selon
les notes de la première version (`education-histoire`, `education-aides-universitaires`,
`education-depense`) :

1. **Aides universitaires.** Arrêtés de montants de 1958, 1963 (deux), 1964, 1965, 1969, 1974 et 1978 ;
   arrêté du 28 février 1990 (prêts, JORT n° 18 de 1990, p. 360) ; arrêté du 7 avril 1992 (JORT n° 23 de
   1992, p. 464) ; décret n° 80-1001 (organisation de l'ONOU, JORT n° 47 de 1980) ; page 1449 du règlement
   de 1974 ; arrêté du 20 août 1982 (fascicules français de 1982 à partir du n° 59 ; fiche
   `r-bourse-montants-1982`). Statut juridique exact des offices (Q7).
2. **Histoire.** Fascicules d'avant 1990 cités en « lisible » (1960, 1961, 1962, 1969, 1976, 1986) :
   probablement des scans ; texte annoncé par l'art. 2 de la loi de 1958 (obligation de six à douze ans) ;
   texte qui a institué le LMD et organisé la rentrée de 2006-2007 ; décrets n° 2012-1227 (mastère) et
   n° 2013-47 (doctorat) ; loi n° 93-10 (JORT 1993/014, p. 252-256).
3. **Dépense.** Décrets et arrêtés de répartition des crédits, tableau A : 1965-1994 et 1995-2026 (2010
   lu) ; budgets citoyens 2014-2018 (sans couche de texte).

*Ticket proposé (à ouvrir par l'humain, jamais par un agent).* « Éducation : lire à l'image les textes
listés en § 9 ; pour chacun, articles, montants, date d'effet (règles de datation), page du fascicule ;
verser les lectures dans les notes `docs/notes/education-*.md` ; ne rien affirmer sans lecture ». Borne :
commencer par le point 1 (le pilote est le chapitre 5), puis le point 2, puis le point 3. Rôle :
documentaliste ; sorties : mise à jour des notes et des fiches de recherche, aucun .qmd.

---

## 10. Chapitres 2, 4, 5 et 6 : état au 17 octobre 2026, et ticket proposé pour le documentaliste

**État de la première version** (`~/projets/precis-education-v1`, branche `chantier/education-v1`) :

| Chapitre du plan | État | Où dans la version 1 |
|---|---|---|
| 2 Enseignement scolaire | **absent comme chapitre** ; la matière lue est dans `_histoire.qmd` (réformes de 1958, 1991, 2002, 2017 ; état du droit scolaire en octobre 2026 ; droits d'inscription au chapitre des aides) | `sec-educ-eleves` et sections voisines de `_histoire.qmd` |
| 4 Enseignement supérieur | **absent comme chapitre** ; section de l'histoire (lois de 1989 et de 2008, LMD en rupture, décret de 2008, tableau replié 1958-2017) | `sec-educ-superieur` de `_histoire.qmd` |
| 5 Aides aux élèves et aux étudiants | **rédigé, à réviser** (environ 17 000 mots, 20 `TODO`) | `_aides.qmd` |
| 6 Dépense | **rédigé, révisé** pour la recherche exclue et les collectivités (environ 8 500 mots) | `_depense.qmd` |

**Ordre décidé le 17 octobre 2026 : le scolaire d'abord (chapitre 2), puis le supérieur (chapitre 4).**
La formation professionnelle initiale devient le chapitre 3, à part (fichier propre) : le chapitre est
amorcé avec la matière déjà lue, et la formation continue reste au marché du travail (Q1). Ordre du
livre : 0 présentation, 1 histoire, 2 scolaire, 3 formation professionnelle initiale, 4 supérieur,
5 aides, 6 dépense. Les chapitres 2, 3 et 4 sont extraits de l'histoire avec les seuls textes déjà lus ;
tout ce qui n'est pas lu reste en `TODO` ou en lacune dite en clair, sans phrase de droit non lue. Les
chapitres 5 et 6 sont inchangés pour l'instant (lectures à l'image, versement des séries).

**Textes à lire avant toute phrase de droit** (rien n'est cité sans lecture) :

- *Supérieur (chapitre 4).* Loi n° 2008-19, art. 4 à 55 (art. 1 à 3, 6, 7, 56 et 58 sont lus) ; décret
  n° 2008-3123, art. 4 à 39 et 45 à fin (art. 1 à 3, 40 à 45 sont lus) ; le texte qui a institué le LMD et
  organisé la rentrée de 2006-2007 ; décrets n° 2012-1227 (mastère) et n° 2013-47 (doctorat) ; décrets
  n° 93-2333, n° 95-1419 (contribution des étudiants) et n° 2004-2721 (licence appliquée), connus par les
  visas ; droits d'inscription à l'université et orientation universitaire (textes annuels) ; loi n° 2000-73
  et ses modifications de 2006 et 2008 (privé) ; lois n° 92-50 et 92-51 (instituts supérieurs des études
  technologiques) ; loi n° 2009-21 (formation pratique) ; décret n° 60-98 (université de Tunis, date de
  signature) ; décret n° 89-1295 (conseil supérieur, 1989). Séries : étudiants par secteur, domaine et type
  d'établissement, diplômés (annuaire de l'INS : étudiants ; publication annuelle du ministère,
  « en chiffres », à obtenir).
- *Scolaire (chapitre 2).* Examens : fin de l'enseignement de base (rendu facultatif par la loi n° 2002-5,
  lue), concours des collèges et lycées pilotes (loi n° 2008-9, lue), baccalauréat (régime, contrôle
  continu) ; texte qui généralise l'année préparatoire ; préscolaire : textes sur les jardins d'enfants
  (statut des animateurs du 31 décembre 2024, index), arrêtés du 6 septembre 1980 et du 22 décembre 1990 sur
  les kouttabs ; privé : décret n° 92-1187, arrêtés du 8 juin 1992 et du 5 septembre 1993 ; décret
  n° 92-1186 (distances de l'obligation, lu) ; cours particuliers ; assurance scolaire. Séries : effectifs
  par ordre et secteur (INS, 1995-2024, déjà versées dans la note d'histoire), taux de scolarisation par âge,
  abandon (statistiques du ministère, à obtenir).
- *Aides (chapitre 5, à compléter).* Arrêtés de montants de 1958, 1963, 1964, 1965, 1969, 1974 et 1978 ;
  arrêtés du 28 février 1990 et du 7 avril 1992 ; décret n° 80-1001 ; arrêté du 20 août 1982 ; critères des
  bourses scolaires après 1974 et décision de 2016 ; prix du repas et du lit avant 2016 ; rapports
  d'activité des offices ; budgets du ministère après 2017.
- *Dépense (chapitre 6, à compléter).* Décrets de répartition des crédits 1965-2026 (tableau A) ; lois de
  règlement (tableaux par chapitre) ; source des trois coûts moyens de l'exercice d'incidence de 2021 ;
  volume détaillé de l'enquête budget-consommation 2021 ; décrets gouvernementaux n° 2020-52 et n° 2020-439
  (nomenclature budgétaire des communes, pour Q8).

**Ticket proposé (à ouvrir par l'humain, jamais par un agent) — mis à jour le 17 octobre 2026.**
« Éducation, chapitres 2 puis 4 : lire au Journal officiel (à l'image au besoin) les textes listés au § 10,
d'abord le scolaire (examens, baccalauréat, année préparatoire généralisée, préscolaire, privé, taux de
scolarisation et d'abandon), puis le supérieur (loi n° 2008-19 art. 4 à 55, décret n° 2008-3123, texte
du LMD de 2006-2007, décrets de 2012 et 2013, droits d'inscription, privé) ; chapitre 3 : formation
professionnelle initiale (loi n° 93-10, décrets d'application de la loi de 2008) ; pour chaque texte :
articles, montants, date d'effet selon les règles de datation, page du fascicule ; verser dans
`docs/notes/education-scolaire-*.md`, `education-formation-professionnelle-*.md` et
`education-superieur-*.md` ; fiche de recherche pour chaque texte introuvable ; séries : inventorier, lire
avec source et page ; aucune rédaction de .qmd ; rien d'affirmé sans lecture. Borne : chapitre 2 d'abord ;
chapitre 4 ensuite ; chapitre 3 en dernier ; aides et dépense : lacunes listées plus haut. Rôle :
documentaliste. Prêt à lancer ; ne se lance qu'avec l'accord de l'auteur. »

**Extraction faite le 17 octobre 2026** (décision de l'auteur) : les chapitres 2, 3 et 4 sont tirés des
sections correspondantes de l'histoire, avec les seuls textes déjà lus ; l'extraction déplace le texte au
lieu de le dupliquer (domicile unique) et ne dit rien de plus que les notes.

**Décisions de l'auteur du 17 octobre 2026 :** (1) ordre : le scolaire d'abord, puis le supérieur ;
(2) extraire maintenant ; (3) la formation professionnelle initiale devient le chapitre 3, à part ;
(4) garder l'autre lecture (« étape ») des réformes de 2002 et de 2017 dans le tableau replié, avec la
lecture principale au premier plan et les raisons de chacune en une phrase.

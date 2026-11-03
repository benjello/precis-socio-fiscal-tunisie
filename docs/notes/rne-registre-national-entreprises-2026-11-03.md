# Registre national des entreprises (RNE) : ce que l'on y trouve, gratuit et payant

Note du 3 novembre 2026. Elle dit ce qui a été constaté sur le portail du Registre national des
entreprises, ce qui est gratuit, ce qui est payant et à quel prix, ce que cela apporterait au précis,
et ce qui reste à vérifier. Elle sert de base aux réponses à qui demande « que peut-on tirer du RNE ? ».
Rien n'a été acheté, aucun compte n'a été créé, aucune connexion n'a été faite.

## 1. Deux « RNE » à ne pas confondre

| | Registre national des entreprises (Centre national du RNE) | Répertoire national des entreprises (INS) |
|---|---|---|
| Nature | registre juridique : immatriculation, modifications, dépôt des états financiers | fichier statistique tenu par l'INS depuis le décret n° 94-780 du 4 avril 1994 |
| Base légale | loi n° 2018-52 (29 octobre 2018 d'après le texte hébergé par l'ICNL ; les sources consultées divergent sur le mois) | décret n° 94-780 du 4 avril 1994 |
| Champ | toutes les personnes morales et physiques immatriculées, associations comprises | « entreprises patentées du secteur privé » (fichiers DGI et CNSS, complétés APII et Douane) |
| Accès | portail `registre-entreprises.tn`, recherche gratuite, documents payants | publications PDF de l'INS, gratuites |

## 2. Le portail du Registre national des entreprises

- **Adresses.** Portail : `https://www.registre-entreprises.tn/rne-public/` (application Angular, routes en `#/…`).
  Site institutionnel : `https://home.registre-entreprises.tn/` (WordPress). `rne.tn` présente un certificat qui ne
  correspond pas au nom d'hôte : il n'a pas été utilisé (le contournement TLS n'est autorisé que pour `pist.tn`).
- **Compteurs affichés sur la page d'accueil du portail le 3 novembre 2026** : 335 467 personnes morales,
  588 214 personnes physiques, 1 515 570 annonces légales.
- **Routes du portail** : `#/recherche-pm` (personnes morales), `#/recherche-pp` (personnes physiques),
  `#/extrait-registre` (renvoie à la connexion), `#/achats` (panier), `#/login` (Digigo, MobileID, compte
  entreprise, compte invité), `#/inscription` (création d'un compte), `#/inscription/conditions-utilisation`
  (mentions légales). Menus : Recherche, Extrait Registre, Mon Entreprise, Bulletin officiel, Certificats,
  Abonnement, Vérification, Payer redevance.
- **Création d'un compte** (formulaire lu, non rempli) : nom, prénom, courriel et sa confirmation, courriel Digigo
  facultatif, mot de passe, téléphone, fax facultatif, pays, ville, code postal, rue, captcha, acceptation des
  conditions d'utilisation de la recherche par Internet. Aucune pièce d'identité n'est demandée à l'inscription.
- **Critères de la recherche de personnes morales** : identifiant unique, numéro d'identité de la personne, état du
  registre, année de création, bureau régional, dénomination (latine, arabe), nom commercial (français, arabe), nom
  du responsable (français, arabe), libellé de l'activité (français, arabe), adresse du siège (français, arabe).
  La page se déroule en trois étapes : recherche, résultat, choix des documents.

## 3. Ce qui est gratuit

1. Les textes et formulaires du site (loi, décrets, circulaires, formulaires RNE-F-001 à RNE-F-010) : une
   soixantaine de PDF listés par l'interface WordPress du site institutionnel.
2. La **recherche d'une société** par dénomination, en français ou en arabe, sans compte : elle renvoie
   l'identifiant unique, la dénomination latine et arabe, le nom commercial. Résultats paginés par 10 à 15.
3. La **fiche de la société** : forme juridique ou catégorie (SA, SARL, établissement public…), état du registre
   (actif…), nom commercial, siège (adresse en français et en arabe).
4. La **liste des documents déposés**, avec pour chacun : nature (fiche d'identité, statuts, PV de modification,
   bilan), date de la pièce, exercice (pour un bilan), nature de l'opération (mise à jour des dirigeants, changement de
   capital, dépôt des états financiers, changement de forme juridique…), prix. Le contenu du document n'est pas affiché.
   Le drapeau « gratuit » de la réponse du portail est faux pour tous les documents rencontrés.
5. Les mentions légales (lues, voir § 6).

## 4. Ce qui est payant

Décret présidentiel n° 2022-298 relatif aux redevances du Registre national des entreprises (JORT n° 34 du
30 mars 2022, p. 854-855). Les mentions légales du portail citent aussi un « décret n° 811-2019 du 12/09/2019 »
sur les redevances, que le décret de 2022 remplace sans doute : non vérifié.

| Service (n° du tableau) | Redevance (DT) |
|---|---|
| Fiche d'identité de l'entreprise (13) | 5 |
| Extrait du registre en arabe ou français (11) | 10 |
| Extrait muni de la signature et du cachet électroniques (12) | 20 |
| Traduction d'un extrait avec mentions en langue étrangère (14) | 20 la page |
| Copie conforme d'un contrat ou document du registre (15) | 10 le document |
| Copie conforme des états financiers, documents comptables, rapports annuels (16) | 20 le document |
| Certificats : non-immatriculation, non-faillite, nantissement ou leasing, dépôt de la déclaration du bénéficiaire effectif (17, 18, 19, 21) | 10 |
| Certificat des jugements et décisions judiciaires déposés (20) | 20 |
| **Copie électronique d'un contrat ou document (statuts, PV)** (24) | **5** le document |
| **Copie électronique des états financiers et documents comptables, rapports annuels** (25) | **10** le document |
| Copie électronique de l'ensemble des documents d'une société, pour une année (26) | 30 |
| Copie électronique de l'ensemble des documents d'une société depuis son immatriculation (27) | 100 |
| Extraction d'une liste de personnes morales ou physiques (28) | 1,5 par identifiant |
| Abonnement annuel « veille » (29) | 20 par identifiant |
| Abonnement annuel « cartographie des dirigeants » (30) | 5 000 par utilisateur |
| Abonnement annuel d'accès à la base de données du RNE (31) | 500 par utilisateur |
| Abonnement annuel au Bulletin officiel électronique du RNE (32) | 50 |
| Consultation à distance du registre des bénéficiaires effectifs (33) | 5 par identifiant (réservée, art. 2, aux personnes de l'article 107 de la loi organique n° 2015-26) |
| Licence de mise à jour périodique des données (34) | 0,2 par identifiant |
| Licence d'identification instantanée à distance (35) | 0,5 par identifiant |
| **Copie électronique de la liste des associés ou actionnaires** (36) | **20** par identifiant |
| Consultation sur place des données du registre (37) | 3 par tranche de 15 minutes |
| Dépôt des états financiers (service n° 5, procédure) | 20 ou 50 selon la colonne (en-têtes de colonnes non lus) |

Un compte et un solde prépayé sont nécessaires (portail : panier, « compte prépayé », « transfert de solde »).
Les prix affichés sur les fiches (5 DT la fiche d'identité et les PV, 10 DT un bilan) concordent avec les services
24 et 25 du décret.

## 5. Fiches de sociétés consultées (visiteur, sans compte)

| Société | Identifiant | Catégorie | Documents listés |
|---|---|---|---|
| Société tunisienne de l'électricité et du gaz | 0005910D | établissement public | fiche ; PV du 26/08/2002, 25/03/2011, 30/04/2013 et 03/11/2015 (les deux derniers : mise à jour des dirigeants) ; « EBilan 2024 » (10 DT) |
| Les Ciments de Bizerte | 0003242F | SA | fiche ; une dizaine de PV de 2002 à 2017, dont plusieurs « dépôt des états financiers » ; statuts du 21/12/1996 ; « Bilan 2023 » (10 DT) |
| Société nationale des chemins de fer tunisiens | 0005743G | établissement public | fiche ; PV du 03/12/2004 (dépôt des états financiers), 31/12/2012, 20/12/2017 |
| Tunisair | 0002672W | SA | fiche ; PV de 2006 à 2016, dont « dépôt des états financiers » (10/07/2013, 30/06/2016) ; liste non lue en entier |
| Banque nationale agricole | 0000123L | SA | fiche ; nombreuses PV de 2002 à 2014 ; liste non lue en entier |
| SNDP Agil Energy | 0002264H | SA | fiche ; nombreuses PV de 1996 à 2013 ; liste non lue en entier |
| Banque de l'habitat | 00024588W (et `_1`, `_2`) | SA | fiche d'identité seule |
| (essai) Société El Majd d'électricité et du gaz | 1390271Z | SARL privée | fiche ; PV du 02/09/2015 ; bilans 2016, 2017, 2021 |

La STEG, la SNCFT et probablement les autres établissements publics n'ont pas d'actionnaires : une « liste des
associés ou actionnaires » n'a pas de sens pour eux (à confirmer au premier essai). Les sociétés à participation
publique (Ciments de Bizerte, Tunisair, SNDP, BNA, BH, TTN) en ont une. Recherches infructueuses de la
dénomination exacte : STEG par sa dénomination latine (la fiche n'a pas de dénomination latine, seulement arabe),
STIR, Tunisie Télécom, STB, Office national des postes, Transtu, Office des céréales (réponses non lues ou associations
d'agents). Beaucoup de résultats sont des amicales ou des associations de retraités.

## 6. Conditions d'utilisation et légalité

- **Consulter** est un service public tarifé : la loi n° 2018-52 définit le RNE comme une base de données publique
  « mise à la disposition du public et des institutions de l'État ».
- **Mentions légales du portail** : le RNE met sa plateforme à disposition « en vue de la diffusion des données
  économiques et juridiques sur les entreprises » (art. 1) ; l'utilisateur ne peut l'employer à une autre fin, s'abstient
  de tout usage contraire à l'ordre public et ne peut porter préjudice aux intérêts du RNE ; l'usage confère « un droit
  personnel et non exclusif de réutilisation des informations », sans droit de propriété intellectuelle (art. 2). Aucune
  mention de collecte automatisée, d'extraction, de robot ni de réutilisation commerciale n'a été trouvée dans le texte
  (recherche par mots-clés ; lecture intégrale non faite).
- **Extraction en masse** : les services 28, 31 et 34 du tarif sont des services payants d'extraction et d'accès à la
  base. Une moisson de masse relèverait de ces services. Une cinquantaine de fiches lues au rythme d'un visiteur reste
  de la consultation ordinaire.
- **Citer un chiffre d'un document acheté**, avec sa source, est l'usage normal. Republier en bloc les documents
  achetés dépasserait le « droit personnel » : à éviter.
- Un appel direct à l'API des fiches, hors du parcours du navigateur, a été refusé par le contrôle de la session ; il
  n'a pas été contourné. Les fiches ont été lues par le parcours visiteur du site.

## 7. Contacts et voies formelles

- Accès à l'information (loi organique n° 22-2016 du 24 mars 2016) : `a.information@e-rne.tn`, formulaires en arabe sur
  `home.registre-entreprises.tn/droit-dacces-a-linformation/`.
- Échange de données par API (services web KYC et bénéficiaire effectif, sur abonnement et contrat de service) :
  `interop@e-rne.tn`, page `home.registre-entreprises.tn/echange_des_donnees/`. Texte de référence pour le
  bénéficiaire effectif : arrêté de la Cheffe du Gouvernement du 13 janvier 2026.
- Standard : `info@registre-entreprises.tn`, +216 70 248 170. Aide : `helpdesk.registre-entreprises.tn`.
- Circulaires du site non lues : n° 17 de 2020 (dépôt des états financiers) et n° 3 de 2021 (obligation de l'extrait
  du RNE), à lire pour savoir qui doit déposer ses comptes.

## 8. Ce que cela apporterait au précis

Le précis a, pour 2018-2023, les fiches du rapport du ministère des Finances sur les entreprises publiques : dette
par créancier, résultat net, effectif, produits d'exploitation, subventions. Le RNE ajouterait, **après achat** :

- la **liste des actionnaires** (20 DT par société anonyme) : participations, identité des « autres actionnaires
  publics » de Tunisie Trade Net (85,25 % du capital, aujourd'hui sans nom dans le précis), filiales en cherchant dans le
  sens inverse ;
- les **dirigeants** et leurs dates (PV de modification « mise à jour des dirigeants ») ;
- les **changements de capital** datés ;
- le **détail d'un bilan** (annexe, rapport du commissaire aux comptes), pour les exercices déposés.

Limites : séries de bilans très lacunaires (un ou deux exercices par société dans les cas vus, contre six ans au
ministère) ; pas de série longue ; établissements publics sans actionnaires ; le coût (10 DT un bilan, 20 DT une
liste d'actionnaires) est faible, mais l'achat exige un compte et un solde prépayé.

## 9. Statistiques de l'INS tirées de son répertoire

Treize éditions de « Statistiques issues du répertoire national des entreprises » rangées dans `tunisia-data`
(`data/raw/ins-publications/rne/`, catalogue `sources/ins-rne-statistiques-urls.csv` et fiche
`sources/ins-rne-statistiques.md`, PR 113) : 2010 à 2018, 2021, 2022, 2024, 2025. Éditions 2019, 2020 et 2023 absentes
d'ins.tn. Édition 2025 (67 pages, RNE 2024) : entreprises privées 478 089 en 2005, 836 808 en 2024 ; ventilation par
activité, tranche de salariés (410 645 entreprises sans salarié sur 478 089 en 2005), forme juridique, gouvernorat,
délégation, régime et nationalité ; emploi salarié formel du secteur privé ; démographie des entreprises ; qualité
(faux actifs, exactitude de la localisation, de l'activité et du nombre de salariés).
**Le champ est le secteur privé** : aucune statistique sur les entreprises publiques. Utile au contraste formel et
informel (volume « Informel » et « Le marché du travail »), pas aux entreprises publiques. Aucune série n'en est
encore extraite.

## 10. Outil et état au 3 novembre 2026

- `tunisia-data`, branche `donnees/rne-inventaire` (non commitée) : `scripts/rne_inventaire.py` et
  `sources/rne-entreprises-publiques.csv` (50 entreprises du précis, requêtes en français et en arabe). Deux passes :
  `chercher` (candidats du portail, écrits dans `sources/rne-candidats.csv`) et `inventaire` (fiches et documents, dans
  `sources/rne-fiches.csv` et `sources/rne-documents.csv`). Parcours visiteur, une page toutes les quatre secondes,
  aucun achat, aucune connexion. Chromium installé par `uv run --with playwright playwright install chromium`.
- Passe `chercher` faite à 13 h 20 : 110 candidats pour 43 entreprises sans identifiant. Identifiants retenus :
  16 sans ambiguïté, 7 déjà connus, soit 23 sur 50. Passe `inventaire` faite à 13 h 35 sur ces 23 (§ 13).

## 11. À faire, par ordre

1. ~~Lire les candidats, fixer les identifiants, lancer `inventaire`~~ fait pour 23 entreprises sur 50 (§ 13) ; reste à
   retrouver les 27 autres (noms enregistrés au RNE différents de ceux du précis).
2. Acheter un bilan test (10 DT, par exemple « Bilan 2023 » des Ciments de Bizerte) et une liste d'actionnaires
   (20 DT, par exemple Tunisie Trade Net) avec un compte créé par l'humain ; vérifier si un tiers peut acheter les
   états financiers au tarif unitaire.
3. Circulaires n° 17 de 2020 et n° 3 de 2021 : non accessibles en ligne (voir § 19) ; la loi n° 2018-52 est lue.
4. Rédiger, si utile, une demande d'accès à l'information à `a.information@e-rne.tn` : liste des entreprises à
   participation publique avec capital et associés.
5. Si le contraste formel et informel est retenu, tirer des éditions de l'INS une série versée dans `tunisia-data`.

## 12. Plan d'une première exploitation pour le volume « Le marché du travail » (3 novembre 2026)

Constat. Le volume est juridique (institutions, salaire minimum, conventions collectives, temps de travail,
rupture du contrat, politiques de l'emploi) et ne dit rien du **tissu d'entreprises** : or les règles qu'il décrit
jouent par seuils de taille (représentation du personnel, licenciement économique, formation). Deux sources : les
statistiques de l'INS (gratuites, secteur privé, § 9) et le Registre national des entreprises (payant, § 2 à 8).

**Étage 1 : gratuit, statistiques de l'INS (en cours).**
1. Série des entreprises privées par tranche de salariés, 2005-2024 (tranches : 0, 1 à 2, 3 à 5, 6 à 9, 10 à 19,
   20 à 49, 50 à 99, 100 à 199, 200 et plus), tirée de l'édition 2025 et raccordée aux éditions antérieures pour
   repérer les ruptures (une rupture est visible en 2018 dans les séries par gouvernorat).
2. Série de l'emploi salarié formel du secteur privé, par tranche de taille et par activité, même période.
3. Chapitre « Les employeurs » du marché du travail : le formel est d'abord fait d'indépendants et de très
   petites entreprises (410 645 entreprises sans salarié sur 478 089 en 2005).
4. Tableau des seuils légaux de taille dans `_institutions.qmd` : pour chaque seuil, le nombre d'entreprises du
   secteur privé qui le franchit, par année. À faire seulement si l'humain le confirme.
5. Versement dans `tunisia-data` avec une fiche de provenance par série (champ, source, ruptures, faux actifs).
   Aucune valeur isolée : évolution datée et graphique. Rien n'est écrit dans le livre avant relecture.

**Étage 2 : peu coûteux, avec achats au RNE.**
- Poids des entreprises publiques dans l'emploi salarié : rapprocher les effectifs du ministère des Finances de
  l'emploi formel de l'INS, en disant que les champs diffèrent. Aucun achat.
- Liste des actionnaires de Tunisie Trade Net (20 DT) : lève un TODO du volume « Entreprises publiques ».
- Un bilan test (10 DT) pour voir si l'effectif y figure ; achat à faire par l'humain avec son compte.

**Étage 3 : à décider plus tard.** Dirigeants et mouvements de capital par les PV de modification (intérêt faible
pour le marché du travail) ; extraction de masse (1,5 DT l'identifiant, abonnement à la base 500 DT par an), à ne
pas faire sans accord écrit du Centre national du RNE.

Questions ouvertes : les seuils de taille (point 4) sont-ils voulus dans le livre ; qui fait l'achat test.

## 13. Inventaire des documents déposés : 23 entreprises publiques (3 novembre 2026, 13 h 35)

Source : fiches du portail en parcours visiteur (§ 5, § 10). Aucun document n'est gratuit (0 sur 228). Les 228 documents
se répartissent en 23 fiches d'identité, 159 PV de modification (dont 89 portant « mise à jour des dirigeants » et 15
« changement de capital »), 3 statuts et 43 bilans (types `EBILAN` et `E_BILAN`). Les 43 bilans listés coûtent 430 DT
en tout (10 DT l'unité).

| Entreprise | Sigle | Identifiant | Forme | État | Documents | Exercices des états financiers déposés |
|---|---|---|---|---|---|---|
| Société tunisienne de l'électricité et du gaz | STEG | 0005910D | établissement public | actif | 6 | 2024 |
| Entreprise tunisienne d'activités pétrolières | ETAP | 0002766B | établissement public | actif | 10 | 2020 à 2023 |
| Société nationale de distribution des pétroles (Agil Energy) | SNDP | 0002264H | SA | actif | 27 | 2025 |
| Banque de l'habitat | BH | 00024588W | SA | non actif | 1 | aucun |
| Banque nationale agricole | BNA | 0000123L | SA | actif | 30 | 2022, 2024, 2025 |
| Banque tunisienne de solidarité | BTS | 0614662X | SA | actif | 11 | 2022, 2025 |
| Caisse des prêts et de soutien des collectivités locales | CPSCL | 0042939B | établissement public | actif | 6 | 2020 à 2024 |
| Société de promotion des logements sociaux | SPROLS | 0002788H | établissement public | actif | 11 | 2020 à 2024 |
| Société nationale d'exploitation et de distribution des eaux | SONEDE | 0001455J | établissement public | actif | 6 | 2023 |
| Office national de l'assainissement | ONAS | 0006136S | établissement public | actif | 5 | 2024 |
| Office national des postes | La Poste | 0513287H | établissement public | actif | 4 | aucun |
| Office du commerce de la Tunisie | OCT | 0001126T | autre | actif | 13 | 2024 |
| Régie des alcools | RA | 0001213R | établissement public | actif | 9 | 2019, 2022, 2023, 2024 |
| Manufacture des tabacs de Kairouan | MTK | 0009878P | établissement public | actif | 4 | 2024 |
| Office des terres domaniales | OTD | 0013949R | établissement public | actif | 3 | aucun |
| Société tunisienne de sidérurgie El Fouladh | El Fouladh | 0002439N | SA | actif | 14 | aucun |
| Les Ciments de Bizerte | SCB | 0003242F | SA | actif | 13 | 2023 |
| Société nationale de cellulose et de papier alfa | SNCPA | 0007664S | SA | actif | 7 | 2023, 2024 |
| Société nationale des chemins de fer tunisiens | SNCFT | 0005743G | établissement public | actif | 4 | aucun |
| Société du métro léger de Sfax | SMLS | 1461823E | établissement public à caractère non administratif | actif | 2 | 2024 |
| Tunisair | Tunisair | 0002672W | SA | actif | 21 | 2021 à 2023 |
| Agence technique des transports terrestres | ATTT | 0425324C | établissement public | actif | 10 | 2020 à 2024 |
| Compagnie tunisienne de navigation | CTN | 0000318W | SA | actif | 11 | aucun |

Lectures. Environ les deux tiers des 23 ont au moins un bilan déposé (17 sur 23). Les établissements publics (STEG,
ETAP, CPSCL, SPROLS, SONEDE, ONAS, OCT, RA, MTK, SMLS, ATTT) déposent plus souvent que les sociétés anonymes à
participation publique. Les dépôts commencent en 2019 ou 2020 : la série d'un exercice par entreprise n'est pas longue.
La fiche de la BH (« non actif », 1 document) a deux autres numéros (`_1`, `_2`) : probable doublon de registre, à
vérifier avant d'en tirer quoi que ce soit. Un bilan listé n'est pas un bilan lisible : la lecture suppose l'achat.

**Entreprises du précis dont l'identifiant n'est pas encore fixé (27)** : STIR, STB, Tunisie Télécom, Transtu, PCT, CPG,
GCT, AFH, AFI, SNIT, RNTA, CTF, ONH, Office des céréales, OACA, OMMP, SOTRAPIL, BFPME, ARRU, SOGEMT, CIOK, Tunisie
Autoroutes, RFR, SNTRI, Tunisie Trade Net, SORETRAS et SRTB. La recherche par dénomination ne rend pour elles que des
amicales d'agents ou des associations de retraités, ou rien. Pistes : recherche par identifiant fiscal, par nom
commercial ou par année de création ; la STEG et d'autres établissements publics n'ont une dénomination qu'en arabe.

## 14. Étage 1 du plan, statistiques de l'INS : état au 3 novembre 2026

- Lecture des tableaux d'évolution (imprimés en travers) : `tunisia-data/scripts/ins_rne_tableaux.py` ; construction :
  `scripts/build_ins_rne_series.py`, sorties dans `data/processed/ins-rne/` (quatre séries et leurs fiches de provenance).
  Sept éditions lues (2016, 2017, 2018, 2021, 2022, 2024, 2025), aucune révision d'une édition à l'autre.
- Séries : entreprises privées par tranche de salariés (2001-2024) et par forme juridique (2001-2024) ; emploi salarié
  formel du secteur privé par tranche de taille de l'entreprise (2000-2024) et par forme juridique (2000-2024).
- Chiffres clés 2024 : 836 808 entreprises privées dont 729 240 sans salarié (87,1 %) ; 13 396 entreprises de 10
  salariés et plus ; 1 164 913 salariés dont 65,9 % dans les entreprises de 50 salariés et plus. 2018 : les entreprises
  sans salarié passent de 676 140 à 635 571 alors que les autres tranches augmentent (non expliqué par l'INS). 2020 :
  l'emploi recule de 1 144 215 à 1 076 128, surtout dans les entreprises de 200 salariés et plus.
- Reste : entrées de catalogue et tests dans `tunisia-data`, tableau et graphique à relire, projet d'encadré pour
  le chapitre « Les employeurs ». Rien n'est commité ni écrit dans le livre.

## 15. Information publique gratuite utile au précis (3 novembre 2026)

Le précis ne mentionne le RNE nulle part au 3 novembre 2026 (recherche dans les chapitres du volume « Entreprises
publiques »). Ce qui est gratuit se range en deux sortes.

**A. Solide : les statistiques de l'INS (§ 9, § 14).** Quatre séries 2000/2001-2024 : entreprises privées et emploi
salarié formel, par taille et par forme juridique. Elles donnent au volume « Le marché du travail » la structure du tissu
d'entreprises qui lui manque : 87,1 % des entreprises privées n'ont aucun salarié (729 240 sur 836 808 en 2024) ; 65,9 %
de l'emploi salarié formel est dans les entreprises de 50 salariés et plus ; 13 396 entreprises ont 10 salariés ou plus.
Elles situent les seuils légaux de taille et le contraste entre formel et informel. Sept éditions lues, aucune révision.

**B. Plus mince : ce que le portail du RNE affiche sans compte (§ 3, § 13).**
- La **forme juridique** de chaque entreprise publique, qui recoupe le statut annoncé par le précis : établissements
  publics (STEG, ETAP, SONEDE, ONAS, SNCFT, CPSCL, SPROLS, ATTT, Régie des alcools, MTK, OTD, La Poste, métro léger de
  Sfax) ; sociétés anonymes (BNA, BTS, BH, Tunisair, SNDP-Agil, El Fouladh, Ciments de Bizerte, SNCPA, CTN) ; « autre »
  pour l'Office du commerce de la Tunisie. Le précis ne dit pas ce statut de façon uniforme : à relever entreprise par
  entreprise (§ 16).
- L'**état du registre** et le **siège**. La BH est « non actif » avec une fiche d'un seul document et trois numéros
  (`00024588W`, `_1`, `_2`) : anomalie à vérifier avant d'écrire quoi que ce soit.
- Les **dates des PV de modification** et leur nature : 159 PV, dont 89 « mise à jour des dirigeants », 15 « changement de
  capital », des changements de forme ou de situation juridique. Ce sont des dates de changements, sans leur contenu :
  elles servent à dater un événement que le précis raconte déjà, pas à l'établir.
- **Qui dépose ses comptes** : 17 entreprises sur 23 ont au moins un bilan déposé ; plus souvent les établissements
  publics que les sociétés anonymes ; BH, La Poste, SNCFT, El Fouladh, OTD et CTN n'en ont aucun. Indicateur de
  transparence, sans le contenu des comptes.

**C. Sans intérêt pour le précis** : les compteurs du portail (335 467 personnes morales, 588 214 personnes physiques,
1 515 570 annonces légales), qui ne se comparent pas aux 836 808 entreprises de l'INS (champs différents) ; les tarifs,
utiles seulement pour décider d'un achat.

**Précautions de citation.** Ce qui est gratuit est un constat sur l'enregistrement, pas sur les comptes ; il se cite avec
sa date de consultation et en vérifiant que l'entreprise est la bonne (beaucoup de résultats de recherche sont des
amicales ou des associations de retraités). Pour la forme juridique, la source reste le texte qui crée ou transforme
l'entreprise ; le RNE sert de recoupement.

**Suite décidée le 3 novembre 2026** : finir les séries de l'INS et les montrer (tableau, graphique) ; relever, pour les
23 entreprises, la forme juridique du RNE face à celle du précis et les écarts (§ 16). Les dates de PV et le dépôt des
comptes attendent.

## 16. Forme juridique au RNE face au précis : 23 entreprises (3 novembre 2026)

Le RNE donne une forme juridique par entreprise (§ 13). On la compare à ce que le volume « Entreprises publiques » dit du
statut dans la section de chaque entreprise (premières phrases et textes de création). Le RNE ne distingue pas
établissement public à caractère industriel et commercial, administratif ou non administratif (sauf pour le métro léger de
Sfax) : il dit « établissement public ». Le précis dit « à caractère industriel et commercial » quand le texte de création le
dit ; cette précision vient du texte et reste la source.

| Entreprise | RNE | Précis | Verdict |
|---|---|---|---|
| STEG | établissement public | établissement public à caractère industriel et commercial (1962) | concorde |
| ETAP | établissement public | établissement public à caractère industriel et commercial (loi de 1972) | concorde |
| SNDP | SA (« Société nationale de distribution des pétroles Agil Energy ») | société anonyme, renommée Société nationale de distribution des pétroles en 1977 | concorde ; le nom d'usage « Agil Energy » du RNE n'est pas dans le précis |
| BNA | SA | société anonyme bancaire (1959) | concorde |
| BTS | SA | société anonyme bancaire (1997) | concorde |
| BH | SA, **non actif**, 1 document, trois numéros | banque issue de la Caisse nationale d'épargne-logement (loi de 1989) | **à vérifier** : l'état « non actif » et le doublon de numéros (`00024588W`, `_1`, `_2`) contredisent une banque en activité |
| CPSCL | établissement public | renvoie au volume « Les finances locales » | à recouper avec ce volume |
| SPROLS | établissement public | établissement public à caractère industriel et commercial (loi de 1977) | concorde |
| SONEDE | établissement public | établissement public créé en 1968 | concorde |
| ONAS | établissement public | établissement public créé en 1974 | concorde |
| La Poste | établissement public | établissement public créé en 1998 | concorde |
| Office du commerce de la Tunisie | **« autre »** | établissement public créé en 1962 | **écart** : le RNE le classe « autre » ; pas d'explication lue |
| Régie des alcools | établissement public | établissement public à caractère industriel et commercial (loi de finances pour 1975) | concorde |
| Manufacture des tabacs de Kairouan | établissement public | établissement public à caractère industriel et commercial (loi de 1981) | concorde |
| Office des terres domaniales | établissement public | établissement public créé en 1961 | concorde |
| El Fouladh | SA | « au capital de laquelle l'État souscrit depuis 1962 » : la forme n'est pas dite | complément possible (SA) ; source à prendre dans les statuts |
| Ciments de Bizerte | SA | société « au capital de laquelle la loi autorise l'État à souscrire en 1975 » : forme non dite | complément possible (SA) |
| SNCPA | SA | « entreprise publique » : forme non dite | complément possible (SA) |
| SNCFT | établissement public | établissement public à caractère industriel et commercial (statuts de 1969) | concorde |
| Métro léger de Sfax | établissement public à caractère non administratif | établissement public à caractère non administratif (décret gouvernemental du 23 juillet 2015) | concorde, mêmes termes |
| Tunisair | SA | lois de 1961 à 1984 sur sa souscription au capital ; forme non dite | complément possible (SA) |
| ATTT | établissement public | établissement public à caractère industriel et commercial (loi de 1995) | concorde |
| CTN | SA | société anonyme créée en 1959, au capital de 126 MD | concorde |

Bilan : 16 concordances, 5 formes que le précis ne dit pas (El Fouladh, Ciments de Bizerte, SNCPA, Tunisair, et la CPSCL à
recouper), 1 écart de catégorie (Office du commerce), 1 anomalie de registre (BH). Rien n'est modifié dans le précis : une
forme tirée du RNE ne se verse dans un chapitre qu'avec le texte ou les statuts qui la fondent (§ 15, précautions de
citation). Les 27 entreprises sans identifiant n'ont pas pu être comparées.

## 17. Mise à jour de l'inventaire : 39 entreprises sur 50 (3 novembre 2026, 14 h 17)

**Pourquoi 16 entreprises de plus.** La recherche par dénomination ne rendait que les premiers résultats. Le portail trie du
plus récent au plus ancien identifiant et ne renvoie que quelques lignes par appel : les entreprises publiques, immatriculées
anciennement (identifiants commençant par `000`), sont en queue de liste. `rne_inventaire.py chercher` suit maintenant
`afterId` page après page jusqu'à épuisement de la liste. Les noms arabes officiels (« ديوان الحبوب », « الشركة الوطنية العقارية
للبلاد التونسية ») donnent de meilleurs résultats que les noms latins.

**Résultat de la passe `inventaire` sur 39 entreprises** : 376 documents, tous payants (0 gratuit) ; 268 PV de modification
dont 143 « mise à jour des dirigeants » et 21 « changement de capital » ; 62 bilans listés, soit 620 DT à 10 DT l'unité ;
26 entreprises sur 39 ont au moins un bilan déposé. Formes : 20 établissements publics, 3 établissements publics à
caractère non administratif, 15 sociétés anonymes, 1 « autre » (Office du commerce). Deux registres « non actifs » : la BH
et la CTF.

Entreprises ajoutées à l'inventaire par rapport au § 13 :

| Entreprise | Sigle | Identifiant | Forme | État | Documents | Exercices des états financiers déposés |
|---|---|---|---|---|---|---|
| Société tunisienne des industries de raffinage | STIR | 0003288W | etablissement public | actif | 7 | 2023 |
| Compagnie tunisienne de forage | CTF | 00013747H | société anonyme (sa) | non actif | 1 | aucun |
| Société tunisienne de banque | STB | 0001237A | société anonyme (sa) | actif | 22 | aucun |
| Agence foncière d'habitation | AFH | 0000035M | etablissement public à caractère non administratif | actif | 5 | 2024 |
| Société nationale immobilière de Tunisie | SNIT | 0002806R | etablissement public | actif | 7 | 2021, 2022, 2024 |
| Office des céréales | OC | 0005147R | etablissement public | actif | 7 | 2024 |
| Office national de l'huile | ONH | 0005897A | etablissement public à caractère non administratif | actif | 7 | 2023 |
| Régie nationale des tabacs et des allumettes | RNTA | 0005300G | etablissement public | actif | 5 | aucun |
| Pharmacie centrale de Tunisie | PCT | 0001162Y | etablissement public | actif | 10 | 2024 |
| Compagnie des phosphates de Gafsa | CPG | 0000308T | société anonyme (sa) | actif | 6 | aucun |
| Groupe chimique tunisien | GCT | 0003876L | société anonyme (sa) | actif | 13 | aucun |
| Agence foncière industrielle | AFI | 0006177C | etablissement public | actif | 3 | aucun |
| Société Tunisie Autoroutes | Tunisie Autoroutes | 0381461V | société anonyme (sa) | actif | 16 | 2021, 2022, 2023, 2025 |
| Office de l'aviation civile et des aéroports | OACA | 0011864D | etablissement public | actif | 14 | aucun |
| Office de la marine marchande et des ports | OMMP | 0002857D | etablissement public | actif | 10 | 2019, 2020, 2022 |
| Tunisie Trade Net | TTN | 0736202X | société anonyme (sa) | actif | 15 | 2020, 2021, 2022, 2023 |

**Lecture notable.** Tunisie Trade Net (`0736202X`) est une société anonyme, active, avec des bilans de 2020 à 2023 : sa
liste d'actionnaires (20 DT) lève le TODO sur l'identité des « autres actionnaires publics » qui détiennent 85,25 % du
capital. Tunisie Autoroutes (`0381461V`, société anonyme, bilans 2021, 2022, 2023, 2025) et l'Office de la marine marchande
et des ports (2019, 2020, 2022) déposent aussi.

**Forme juridique au RNE face au précis, pour les 16 entreprises ajoutées** :

| Entreprise | RNE | Précis | Verdict |
|---|---|---|---|
| STIR | **établissement public** | « société de raffinage issue d'une convention passée en 1960 avec une société italienne, dont l'État rachète en 1975 les actions » | **écart à vérifier** : le précis parle d'une société à actions, le RNE d'un établissement public |
| STB | SA | forme non dite | complément possible |
| AFH | établissement public à caractère non administratif | établissement public créé en 1973 | concorde, le RNE est plus précis |
| SNIT | **établissement public** | « société à caractère commercial dont l'État apporte le capital depuis 1957 » (statuts approuvés par la loi n° 57-19 du 10 septembre 1957) | **écart** : le précis dit société commerciale |
| Office des céréales | établissement public | établissement public créé en 1962 | concorde |
| ONH | établissement public à caractère non administratif | établissement public créé en 1962 | concorde, le RNE est plus précis |
| RNTA | établissement public | établissement public à caractère industriel et commercial (1964) | concorde |
| PCT | établissement public | établissement public à caractère industriel et commercial (1961) | concorde |
| CPG | SA | forme non dite | complément possible |
| GCT | SA | forme non dite | complément possible |
| AFI | établissement public | établissement public à caractère industriel et commercial (recréé en 1991) | concorde |
| Tunisie Autoroutes | SA | société anonyme créée le 13 mai 1992 | concorde |
| OACA | établissement public | forme non dite | complément possible |
| OMMP | établissement public | établissement public créé en 1965 | concorde |
| Tunisie Trade Net | SA | société anonyme sous la tutelle du ministère des Finances | concorde |
| CTF | SA, **non actif**, fiche seule | société anonyme du secteur de l'énergie | concorde sur la forme ; **registre non actif**, à vérifier |

Bilan sur les 39 : 26 concordances (dont la CTF, dont le registre est « non actif »), 9 formes que le précis ne dit pas
(El Fouladh, Ciments de Bizerte, SNCPA, Tunisair, STB, CPG, GCT, OACA, et la CPSCL à recouper avec le volume des finances
locales), 3 écarts (Office du commerce classé « autre » ; STIR et SNIT classées établissements publics au RNE alors que le
précis parle de sociétés) et 1 anomalie de registre en plus de la CTF (la BH, « non actif » et enregistrée trois fois). Rien
n'est modifié dans le précis.

**Anomalies de registre, précisées.** BH : trois enregistrements (`00024588W`, non actif, 1 document ; `00024588W_1`, un PV
du 21/09/2007 ; `00024588W_2`, fiche seule) : une même banque enregistrée trois fois, sans bilan. Office du commerce : « autre »,
et aucun PV ne porte de changement de forme juridique. Les statuts de la STIR et de la SNIT, vendus 5 DT, trancheraient.

**Textes du *Journal officiel*.** `jort_cache.db` ne donne, pour El Fouladh, les Ciments de Bizerte, la SNCPA et Tunisair, que des
décrets de statut du personnel (n° 99-1944, n° 2000-2366, n° 99-2743) et non l'acte de constitution : la forme de société anonyme reste à
établir par les statuts (les TODO du précis le notent déjà pour El Fouladh, la SNCPA et Tunisair).

**Restent sans identifiant (11)** : Tunisie Télécom (deux enregistrements « اتصالات تونس », `0642506S` et `0621863X`, sans
dénomination ni forme), Transtu, SORETRAS, SRTB, SOTRAPIL, BFPME, ARRU, SOGEMT, CIOK, RFR et SNTRI. Recherches latines et arabes sans
résultat hors associations. Plusieurs ne sont peut-être pas immatriculées sous ces noms ou ne le sont pas au RNE.

## 18. Croisement avec la Bourse de Tunis (3 novembre 2026)

Les pages de la Bourse (75 sociétés cotées, `tunisia-data`, `sources/bvmt-societes-cotees.md`) donnent le numéro de Registre
de chaque société. Croisés avec les 50 entreprises de la liste (`sources/rne-entreprises-publiques.csv`), ils donnent six
concordances (`sources/rne-bourse-correspondance.csv`, `tunisia-data` PR #118) :

| Sigle | Identifiant du Registre | Forme (Registre et Bourse) | État au Registre |
|---|---|---|---|
| STB | 0001237A (la Bourse écrit A0001237) | société anonyme | actif |
| BNA | 0000123L | société anonyme | actif |
| BH | 00024588W | société anonyme | **non actif** |
| Ciments de Bizerte | 0003242F | société anonyme | actif |
| Tunisair | 0002672W | société anonyme | actif |
| SOTRAPIL | 0006473H | société anonyme | actif |

- **SOTRAPIL** n'avait pas d'identifiant ; la Bourse le donne, et la fiche lue au Registre le confirme (société anonyme,
  active, 18 documents déposés, états financiers 2023 à 2025). La liste passe à 40 identifiants sur 50 (inventaire : 40 fiches,
  394 documents).
- **La BH est « non active » au Registre** alors qu'elle est cotée : à signaler, sans l'interpréter (état administratif du
  dossier d'immatriculation, non état d'activité).
- Les dix entreprises restées sans identifiant (BFPME, ARRU, SOGEMT, Tunisie Télécom, Ciments d'Oum El Kélil, Transtu, RFR,
  SNTRI, SORETRAS, SRTB) ne sont pas cotées : la Bourse n'aide plus ; la recherche au Registre par dénomination reste à refaire
  (noms arabes officiels).
- La Bourse nomme en outre des sociétés cotées à participation publique absentes de la liste des 50 (STAR, SOTUMAG, BTE,
  SOTETEL, notamment), dont les numéros de Registre figurent dans `bvmt-societes.csv`.
- Les numéros s'écrivent de deux façons : sept chiffres et une lettre (0001237A), ou lettre en tête (A0001237) ; SOTUMAG est
  donnée sous un numéro de l'ancien registre du commerce (B193791991).

## 19. Les comptes déposés au Registre : ce que dit la loi n° 2018-52

Texte lu dans le fascicule du JORT n° 89 du 6 novembre 2018 (traduction française pour information), pp. 3781 et suivantes :

- **Art. 7, alinéa 6 (p. 3782)** : sont obligatoirement inscrits au Registre « les entreprises publiques et les établissements
  publics à caractère non administratif ». L'article 8 les range au registre de commerce.
- **Art. 32 (pp. 3787-3788)** : « les personnes physiques soumises obligatoirement à la tenue d'une comptabilité […], les
  personnes morales, les constructions juridiques et les associations doivent déposer, au registre au plus tard dans le septième
  mois suivant la clôture de l'exercice comptable, leurs états financiers » et les rapports des commissaires aux comptes ; les
  sociétés y ajoutent la liste mise à jour des actionnaires ou des associés. Une société mère dépose les documents consolidés
  dans le mois de leur approbation.
- **Art. 51 (p. 3790) et suivants** : un dépôt tardif, états financiers compris, entraîne une pénalité de la moitié de la redevance par
  mois de retard ou fraction de mois ; à défaut de régularisation après un procès-verbal et quinze jours, le Centre suspend le
  registre de l'entreprise et saisit le ministère public (art. 52) ; amende de 1 000 à 5 000 dinars (art. 53).
- **Conséquence pour le volume « Les entreprises publiques »** : une phrase est justifiée au chapitre du statut — les entreprises
  publiques sont inscrites au Registre et leurs états financiers y sont déposés au plus tard le dernier jour du septième mois
  après la clôture, soit le 31 juillet pour un exercice clos le 31 décembre. Les entreprises publiques déposent effectivement :
  les fiches lues portent des exercices déposés (STEG 2024, SOTRAPIL 2023 à 2025), mais d'autres n'en portent aucun (OACA, CTN) :
  l'écart se lit dans `rne-fiches.csv`, colonne `exercices_etats_financiers`.
- **Circulaires n° 17 de 2020 et n° 3 de 2021** : non lues. Le site institutionnel du Centre (`rne.tn`) présente un certificat
  qui ne lui correspond pas (nom d'hôte absent du certificat, certificat d'un autre organisme) : la connexion est refusée et ne
  se contourne pas (règle : TLS contournable pour `pist.tn` seulement). La presse en rapporte le contenu (communiqué du Centre
  du 30 juin 2020 : tous les assujettis tenant une comptabilité, délai du septième mois, pénalité de 50 % de la redevance par
  mois), sans citer les articles. Pour les lire : demande à `a.information@e-rne.tn` (voir le brouillon de demande d'accès).
- **Phrase proposée pour le chapitre du statut** (à insérer par la session qui tient le volume) : « Les entreprises publiques
  et les établissements publics à caractère non administratif sont inscrits au Registre national des entreprises, et les
  personnes morales y déposent leurs états financiers au plus tard dans le septième mois suivant la clôture de l'exercice
  [@loi2018-52, art. 7 et 32]. » La notice `loi2018-52` est à créer (JORT n° 89 du 6 novembre 2018, à partir de la p. 3781 ; URL pist.tn
  d'après `jort_cache.db`, recid 108642).

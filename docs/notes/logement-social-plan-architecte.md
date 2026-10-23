# Logement social : fiche de plan de l'architecte

Architecte, 23 octobre 2026. Sources : note documentaire
`docs/notes/logement-social-foprolos-2026-10-23.md` (dite « la note », renvois en § de la note),
fiche économiste `docs/notes/eco-logement-social.md`, chapitre des cotisations
(`precis/fr/cotisations_sociales/_prelevements_salaires.qmd`, `#sec-cot-foprolos*`), gabarit
`precis/fr/prestations_sociales/_non_contributives.qmd`. Aucun fait n'est ajouté ici : tout vient
de la note, avec son degré de lecture. Chapitre nouveau : pas de registre de destination.

## 0. Décisions clés

1. **Domicile : chapitre `precis/fr/prestations_sociales/_logement_social.qmd`, à titre provisoire.**
   L'hypothèse de travail est confirmée (§ 1). La section dans le livre des cotisations est
   écartée.
2. **Ce que le chapitre suit de bout en bout** : le fonds de promotion du logement pour les
   salariés, c'est-à-dire son objet, ses ressources, sa gestion et ses prêts aux salariés. Les
   autres sections décrivent les dispositifs qui puisent dans le fonds ou se définissent par
   rapport à ses catégories (§ 2).
3. **Cinq grandes réformes** : 1986-1990 (résorption des logements rudimentaires, le fonds mis
   à contribution) ; 2012 (programme spécifique pour le logement social) ; 2016 (refonte des
   prêts) ; 2017 (premier logement) ; 2026 (le fonds finance les logements des opérateurs
   publics). Trois bornes du brief sont corrigées (§ 3.1) :
   - « 2011-2013 » n'est pas une réforme : ce sont des étapes ;
   - « 2016-2017 » réunit deux textes d'objets différents ;
   - le décret n° 2023-127, absent de la liste du brief, est classé comme étape de 2016.
4. **Les chiffres.**
   - Les prévisions de ressources du fonds (2011-2020) et les prélèvements (1987-1990,
     2011-2013) vivent dans ce chapitre. Le chapitre des cotisations en reçoit une phrase et un
     lien.
   - Les données du ministère des Finances relayées par Zaafrane (2014) sont tenues dans une
     sous-section à part, jamais sur la même figure.
   - Les chiffres de l'ARP (2025) n'entrent pas dans le corps du chapitre.
5. **Ancres sans nom de livre** (`sec-log-…`, `r-log-…`), pour qu'une migration vers un livre
   « Le logement » ne change que le chemin des liens.

## 1. Domicile

**Ce que dit la règle.** `docs/conventions-redaction.md`, § 4 : un dispositif qui n'existe que pour
un secteur vit dans le livre sectoriel. Le fonds, le programme spécifique et le premier logement
n'existent que pour le logement. Leur domicile de droit est donc un livre « Le logement »
(partie IV, « plus tard » ; `precis/fr/index.qmd` l. 77 : « à venir »). Ce livre n'existe pas.

**Retenu : un chapitre provisoire dans « Les prestations sociales ».** Raisons :

- **Le livre prend les régimes du côté de ce qu'ils servent** (présentation, premier
  paragraphe). Il admet déjà le non monétaire : sa table des naissances (`tbl-prest-naissances`)
  porte une colonne « Forme » où figurent l'assistance médicale (non monétaire) et la crèche (non
  monétaire, versée à la crèche). Un prêt à taux réduit, une subvention en capital ou un logement
  cédé en location-vente entrent dans ce cadre.
- **Il oppose contributif et budget de l'État, et le logement social a les deux faces.** Côté
  contributif : les prêts du fonds, financés par une contribution sur les salaires et réservés
  aux salariés (loi n° 77-54, art. 5). Côté budget de l'État : le programme spécifique (LFC 2012,
  art. 28) et le premier logement (LF 2017, art. 61).
- **Les publics se définissent en multiples du SMIG**, comme les conditions de ressources du
  livre (décret 2016-1126, art. 2 ; décret 2012-1224, art. 21 ; décret 2017-161, art. 5).
- **Le livre renvoie déjà au logement social** : la loi de l'Amen social prévoit des priorités
  d'accès au logement social (`_non_contributives.qmd`, `#r-nc-lo-14`, art. 14-17).
- **Un livre d'un seul chapitre, avec sa présentation, est disproportionné aujourd'hui.** Il
  faudrait créer le répertoire, le `_quarto.yml`, un `references.json`, les infobulles, une
  entrée dans `build.sh` et une ligne dans l'index du site. La santé est née en livre
  autonome, mais avec un projet de plusieurs chapitres (`backlog-precis.md`, item 12). Rien de
  tel n'est prévu ici.

**Écarté : une section dans le livre des cotisations (financement et caisses).** Ce livre garde
ce qui est prélevé (taux, assiette, redevables, recouvrement) et les organismes qui le gèrent.
Trois raisons de ne pas y loger le logement social :
- le fonds n'est pas une caisse : c'est un fonds spécial du Trésor, dont l'ordonnateur est un
  ministre (loi n° 77-60, art. 14 ; LF 1993, art. 34) ;
- ce que le chapitre décrit est un emploi, ce que le fonds sert, pas un prélèvement ;
- le programme spécifique et le premier logement sont financés par le budget de l'État, sans
  rien prélever. Les y loger les mettrait hors domicile.

La contribution reste où elle est (`#sec-cot-foprolos-taux`, `-redevables`) et ce chapitre y
renvoie en tête.

**Ce que « provisoire » implique.**
- Rien dans le texte rendu ne parle de provisoire : on annonce ce que l'on présente.
- Un `<!-- TODO (architecte) : chapitre à migrer vers un livre « Le logement » … -->` est placé
  sous le titre.
- Une ligne au `backlog-precis.md` (§ 8).
- Les ancres sont préfixées `sec-log-` et `r-log-`, sans nom de livre.

**Domicile des sections voisines** (une phrase et un lien, jamais la prose recopiée) :

| Sujet | Domicile | Ce que reçoit l'autre livre |
|---|---|---|
| Contribution au FOPROLOS : taux, assiette, redevables, recouvrement, exonérations | cotisations, `#sec-cot-foprolos` | ce chapitre : une phrase en tête, avec lien ; le taux de 1989 dans une proposition (§ 3.2) |
| Affectation de la contribution | cotisations, `#sec-cot-foprolos-affectation` | la phrase existante, corrigée, avec lien vers ce chapitre (§ 8) |
| Emploi du fonds : prêts, prélèvements, financement des opérateurs | **ce chapitre** | cotisations : lien |
| Prévisions de ressources du fonds | **ce chapitre** (`#sec-log-previsions`) | cotisations, `#sec-cot-prelevements-rendement` : une phrase et un lien |
| Contribution au FNAH (adossée à la taxe sur les immeubles bâtis) | finances locales, `#sec-fl-immeubles-fnah` | ce chapitre : lien dans la sous-section du FNAH |
| Emploi du FNAH | **ce chapitre** (`#sec-log-fnah`) | finances locales : une phrase et un lien à ajouter (§ 8) |
| Contribution de 10 % de l'impôt sur les BIC et l'IS au programme de 1986 (loi n° 86-47) | fiscalité, taxes affectées (backlog, item 10 ; non écrit) | ce chapitre la cite comme ressource du programme, en attendant ; ligne au backlog |
| Statut, capital, tutelle et comptes de la SNIT, de la SPROLS et de l'AFH | entreprises publiques | ce chapitre : missions de logement social et location-vente ; une phrase et un lien depuis le livre des entreprises publiques quand une section y existera |
| Priorité d'accès au logement social des catégories de l'Amen social | prestations, `#sec-nc-amen-2019` | ce chapitre : lien dans la vue d'ensemble |
| Épargne-logement (régime, fiscalité) | non établi : loi n° 73-24 non lue | ce chapitre : mise en place seulement |
| Prêts logement des caisses de sécurité sociale (décret n° 2019-835) | caisses | hors sujet |

## 2. Frontière entre les règles de base et les dispositifs

**Les règles de base** (ce sans quoi le dispositif n'existe pas) : le fonds.
- Son objet : loi n° 77-54, art. 5, complété par la LF 2026, art. 21.
- Ses ressources : contribution, remboursements, intérêts (art. 6) ; prélèvements opérés sur lui.
- Sa gestion : fonds spécial du Trésor, ordonnateur, organisme gestionnaire (art. 9 ; loi n° 77-60,
  art. 14 ; LF 1993, art. 34).
- Ses prêts aux salariés : décret n° 77-965, puis décret n° 2016-1126, modifié en 2023 et 2026.

C'est le seul instrument permanent depuis 1977, avec une ressource propre. Les autres dispositifs
puisent dans le fonds, ou se définissent par ses catégories :
- le programme de 1986, par les prélèvements de 1987 à 1990 ;
- le FNAH, par ceux de 2011 à 2013 ;
- les opérateurs publics, par la LF 2026, art. 21 ;
- le premier logement commence à 4,5 SMIG (décret 2017-161, art. 5), plafond de la catégorie
  FOPROLOS 3 en 2016 (décret 2016-1126, art. 2) ;
- le décret n° 2026-123 vise les « catégories de l'art. 2 ».

**Les dispositifs**, qui aménagent l'aide pour un public, une opération ou un opérateur, ont
chacun leur section :
1. la résorption des logements rudimentaires et le FNAH (public : mal-logés, propriétaires,
   collectivités) ;
2. le programme spécifique pour le logement social (public : ménages à faible revenu, salariés
   ou non) ;
3. le premier logement (public : revenus moyens, 4,5 à 10 SMIG ; financeur : budget, BCT) ;
4. les opérateurs publics et la location-vente (opération : production et cession par la SNIT,
   la SPROLS et l'AFH) ;
5. le régime spécial de 1999 (opération : rachat de logements anciens appartenant à des
   étrangers).

Lecture concurrente, écartée : prendre « le logement social » comme dispositif unique, avec le
programme spécifique au centre. Ce programme n'existe que depuis 2012 et n'a pas de ressource
propre ; il ne peut pas porter une histoire qui commence en 1977.

## 3. Les grandes réformes

### 3.1 Vérification des bornes du brief

| Borne du brief | Décision | Motif |
|---|---|---|
| Antécédent avant 1977 | retenu, partie de la mise en place | lu : loi n° 57-19 (SNIT) ; décret n° 77-964 (épargne-logement, modifié le même jour que le décret d'application). Intitulé seul : FNAH 1956, HBM et HLM, CNEL, AFH 1973-1974 |
| Lois n° 77-54 et 77-53 | retenu : mise en place, naissances groupées | lues ; même séance, même page |
| 1986-1990 : prélèvements et résorption | **retenu** (réforme 1) | décret n° 86-438, loi n° 86-47 (lus par OCR) ; LF 1987 art. 96 à LF 1990 art. 46 (lus) : textes voisins, même objet |
| 2011-2013 | **refusé comme réforme propre** : étapes | même mécanisme qu'en 1987 (le fonds sert de réserve à une autre politique), sans objet nouveau lu. Lecture A (retenue) : étapes de la rupture de 1987. Lecture B : rattachées à la réforme de 2012, puisque l'art. 36 est dans la même LFC que l'art. 27. Le récit se place dans la section 2012 (ordre des dates) sous l'une ou l'autre lecture |
| Décret n° 2012-1224 (programme spécifique) | **la rupture est la LFC 2012, art. 27** (rubrique lue) ; le décret en est l'étape | le décret fixe les modalités |
| 2016-2017 premier logement | **scindé** : 2016 (refonte des prêts du fonds) et 2017 (premier logement) | deux objets : le décret n° 2016-1126 règle le fonds ; la LF 2017, art. 61 ouvre une ligne budgétaire hors fonds, versée à la BCT |
| (absent du brief) décret n° 2023-127 | **classé** : étape de 2016 (lecture retenue), rupture possible | voir § 3.3 |
| 2026 : LF art. 21, lois n° 2026-1 et 2026-2, décret n° 2026-123 | **retenu** (réforme 5) ; rupture = LF 2026, art. 21 | l'article modifie l'objet du fonds (loi n° 77-54, art. 5). Lois de 2026 et décret : étapes |

### 3.2 Les cinq réformes

Colonnes : texte et article ; ce que la loi cherche (ses mots) ; contexte ; avant → après ;
dispositifs qui y naissent. Une rupture repose sur un article lu.

**Mise en place, 1977** (n'est pas comptée parmi les réformes).
- Textes : loi n° 77-54 du 3 août 1977, art. 1er-10 ; loi n° 77-60, art. 14 ; décret n° 77-965 du
  24 novembre 1977, art. 1er-12 ; loi n° 77-53, art. 1er-6 (lus FR).
- Ce que la loi cherche : le fonds « est destiné à venir en aide […] aux salariés […] désireux
  d'accéder à la propriété ou à la copropriété d'un immeuble à usage d'habitation » (art. 5).
  SPROLS : « promouvoir la construction de logements au profit des assurés sociaux » (loi
  n° 77-53, art. 2).
- Contexte : non relevé. Question au documentaliste (Ve Plan, débats du 29 juillet 1977).
- Avant → après :
  - avant : la SNIT peut « éventuellement » servir « d'intermédiaire et de contrôleur pour la
    distribution de crédits publics » HBM et HLM (statut de 1957, art. 3) ; un régime
    d'épargne-logement existe (décret n° 77-964) ;
  - après : une ressource affectée sur les salaires, 2 % (renvoi cotisations), un fonds spécial
    du Trésor et des prêts directs aux salariés.
- Prêts de 1977 :
  - 1 à 1,5 SMIG : prêt pour construire ou acheter un logement neuf, au plus 2 800 D, 3 %,
    15 ans ;
  - 1,5 à 3 SMIG : prêt complémentaire à l'épargne-logement, 528 D, 4,5 %.
- Naissances groupées :
  - les prêts aux salariés (règles de base) ;
  - la SPROLS (section des opérateurs) ;
  - les crédits de préfinancement aux promoteurs agréés (art. 7, dans les prêts).

**Réforme 1 — 1986-1990 : la résorption des logements rudimentaires ; le fonds mis à contribution.**
- Textes :
  - décret n° 86-438, art. 1er-2 (OCR) : naissance du programme ;
  - loi n° 86-47, art. 1er-4 (OCR) : sa ressource ;
  - **LF 1987, art. 96** (lu, p. 1624) : premier prélèvement sur le fonds, 5 MD au fonds de
    concours du programme ;
  - étapes : LF 1988, art. 76 (5 MD) ; LF 1989, art. 68 (15 MD) ; LF 1990, art. 46 (15 MD).
- Ce que la loi cherche :
  - le programme : « améliorer les conditions d'habitat des populations mal logées sur l'ensemble
    du territoire » (décret n° 86-438, art. 1er) ;
  - les articles de prélèvement : objet non relevé (rubriques des LF 1987-1990 à relever).
- Contexte : non relevé. Question (VIIe Plan, ajustement de 1986) ; rien n'est tiré de la
  périodisation générale.
- Avant → après :
  - avant : le fonds ne sert que les salariés acquéreurs ;
  - après : ses disponibilités financent aussi un programme pour les mal-logés, salariés ou non.
- Même période, dans une proposition et avec renvoi : la LF 1989 ramène la contribution de 2 à
  1 % (`#sec-cot-foprolos-taux`).
- Naît : le programme national de résorption des logements rudimentaires (section `#sec-log-pnrlr`).
- Rupture du chapitre : LF 1987, art. 96, pour le fonds. Rupture du dispositif : décret n° 86-438.

**Entre-temps, 1990-2011** (une phrase, renvoi aux registres) :
- 1993 : l'ordonnateur passe au ministre de l'Habitat (LF 1993, art. 34 ; ajustement) ;
- 1999 : régime spécial (section propre) ;
- 2004 : le FNAH refondu (sous-section du FNAH) ;
- prix plafonds des logements de promoteur fixés par arrêtés (2007 et 2009, non lus).
- Les modificatifs du décret n° 77-965 de 1981 à 2015 ne sont pas lus : un TODO, pas de
  phrase (§ 6).

**Réforme 2 — 2012 : le programme spécifique pour le logement social.**
- Texte : LFC 2012 (loi n° 2012-1), art. 27-32 (lu, pp. 926-927).
- Ce que la loi cherche :
  - rubrique : « Création d'un programme spécifique pour le logement social » ;
  - art. 27 : programme « au profit des catégories sociales à faible revenu ayant pour objectif
    le remplacement des logements rudimentaires et la réalisation à leur profit de projets
    d'habitation ».
- Contexte : non relevé. Question (débats de l'ANC sur la LFC 2012).
- Avant → après : un programme financé par le budget de l'État (art. 28), réalisé par les
  conseils régionaux, les SNIT, la SPROLS, l'ARRU, l'AFH et des promoteurs privés (art. 29), pour
  les familles sans logement jusqu'à 3 SMIG, salariées ou non (décret, art. 21).
- Dans la même section, en étapes (lecture A, § 3.1) : prélèvements sur le fonds
  - 2011 : 40 MD, partagés entre le FNAH et le Compte national de solidarité sociale (DL
    n° 2011-56, art. 3) ;
  - 2012 : 60 MD au FNAH (LFC 2012, art. 36) ;
  - 2013 : 60 MD au FNAH (LF 2013, art. 11).
- Naît : le programme spécifique (section `#sec-log-psls`). Étape : décret n° 2012-1224.

**Réforme 3 — 2016 : la refonte des prêts du fonds.**
- Texte : décret gouvernemental n° 2016-1126, art. 1er-12 (lu FR, tableaux à l'image). Il
  abroge le décret n° 77-965 et ses modificatifs (art. 12).
- Ce que la loi cherche :
  - objet non relevé au-delà de l'intitulé, « fixant les modalités et les conditions des
    interventions du fonds » ;
  - un décret n'a pas de rubrique : question sur un éventuel communiqué ou rapport.
- Contexte : non relevé. Question (stratégie de l'habitat 2014-2015, déjà dans `tunisia-data`).
- Avant → après :
  - avant : dernier état lu, celui de 1977 (deux tranches jusqu'à 3 SMIG). Les états de 1981 à
    2015 ne sont pas lus ;
  - après : trois catégories, de 1 à 4,5 SMIG. S'ajoutent des prêts pour un terrain et pour une
    extension, un don pour la catégorie 1 (part de l'autofinancement « prise en charge par le
    fonds », au plus 15 SMIG) et l'interdiction de revendre avant 10 ans.
- Deux lectures, à trancher :
  - (a) rupture : abrogation du texte fondateur, instruments nouveaux ;
  - (b) étape ou ajustement : on ne sait pas si les modificatifs de 2009 à 2015 avaient déjà
    élargi le public ou créé le don.
  - Lecture provisoire : rupture, avec un « avant » daté de 1977 et un TODO. À revoir dès que
    les décrets n° 2009-698, 2009-3586, 2011-3573 et 2015-881 sont lus.
- **Entre-temps 2012-2016** : arrêté du 29 juillet 2013 sur les prix plafonds (ajustement,
  registre (c)).
- **Étape de 2016, racontée dans l'entre-temps 2017-2026 (ordre des dates)** : **décret
  n° 2023-127** (lu FR).
  - « premier logement » ;
  - quatrième catégorie, de 4,5 à 6 SMIG, sur le revenu du ménage ;
  - salariés actifs et retraités, sous condition de 24 mois de cotisation continue ;
  - terrain acheté « au privé » ;
  - 25 ans de remboursement et deux ans de grâce, âge limite de 75 ans.

**Réforme 4 — 2017 : le programme du premier logement.**
- Texte : LF 2017 (loi n° 2016-78), art. 61 (lu FR, pp. 3845-3846).
- Ce que la loi cherche :
  - rubrique : « Création d'une ligne de financement pour le soutien du secteur de l'habitat dans
    le cadre du programme du premier logement » ;
  - ligne de 200 MD « au profit des catégories à revenu moyen ».
- Contexte : non relevé. Question.
- Avant → après :
  - avant : aucune aide publique au-dessus de 4,5 SMIG (décret n° 2016-1126, art. 2) ;
  - après : un prêt bonifié couvrant l'autofinancement, pour 4,5 à 10 SMIG (décret n° 2017-161,
    art. 5-6).
- Ne touche pas le fonds : réforme du chapitre parce qu'un dispositif y naît (doctrine).
- Naît : le premier logement (section `#sec-log-premier-logement`). Étapes : décret n° 2017-161 ;
  LF 2025, art. 25 (dans la section).

**Entre-temps 2017-2026.**
- Un paragraphe sur le décret n° 2023-127, étape de 2016, dont l'état du droit donne la grille.
- Une phrase pour le reste, avec renvois aux sections : 2021, commission du programme
  spécifique abrogée ; 2025, construction ajoutée au premier logement (art. 25) et prêts du FNAH
  pour citernes (art. 27).

**Réforme 5 — 2026 : le fonds finance les logements des opérateurs publics.**
- Texte : **LF 2026 (loi n° 2025-17), art. 21** (lu AR, p. 4235 ; traduction de travail).
- Ce que la loi cherche, rubriques (AR) :
  - « تكريس الحق في السكن ودعم آليات توفير المسكن اللائق » ;
  - « توسيع ميدان تدخل صندوق النهوض بالمسكن لفائدة الأجراء ».
  - Traduction à faire valider par le terminologue avant de la citer en français.
- Contexte, seul contexte sourcé du chapitre :
  - document parlementaire du 16 novembre 2025 (`arp-2025-11-16-equipement`, pp. 1692-1693) ;
  - le ministre y range « la loi régissant le fonds » parmi les textes « intégrée à la loi de
    finances pour 2026 », et annonce le « nouveau programme de location-vente ».
  - Mots seulement : aucun chiffre de cette séance dans le corps du chapitre.
- Avant → après :
  - avant : le fonds prête aux personnes ;
  - après : il finance aussi des projets de la SNIT et de ses filiales, de la SPROLS et de l'AFH,
    jusqu'à 100 % du coût, remboursables sans intérêt sur 25 ans au plus (décret n° 2026-123,
    art. 1er).
- Étapes :
  - lois n° 2026-1 et 2026-2 (vente à tempérament et location-vente par la SNIT et la SPROLS) ;
  - décret n° 2026-123, art. 9 bis : prix plafond levé pour ces cessions.
- Naît : le financement des projets des opérateurs et la location-vente des logements financés
  par le fonds (section `#sec-log-operateurs`).

### 3.3 Ruptures propres aux dispositifs

| Dispositif | Ruptures propres | Étapes |
|---|---|---|
| Résorption et FNAH | 1986 : programme national (décret n° 86-438) ; 2004 : FNAH refondu, cinq emplois A à E, prêts et subventions, gestion bancaire (loi n° 2004-77, art. 1er-4) | 1986-1988 : contribution sur les BIC et l'IS, reconduite et élargie aux BNC, « journée de travail » des salariés (loi n° 86-47 ; LF 1987, art. 34-39 ; LF 1988, art. 42-47) ; 1987-1990 : prélèvements sur le fonds (racontés dans la réforme 1) ; 1988 : 1,5 MD sur le FNAH (LF 1988, art. 77) ; 2005 : fonds spécial du Trésor (renvoi finances locales) ; 2011-2013 : prélèvements (racontés dans la réforme 2) ; 2012 : « occupants privés » ajoutés (LFC 2012, art. 33-35) ; 2025 : prêts sans intérêt pour citernes, prorogés jusqu'au 31 décembre 2027 (LF 2025, art. 27, lu AR) |
| Programme spécifique | 2012 : naissance (réforme 2) | 2012 : décret n° 2012-1224 (définitions, plafonds, subvention de 50 % ou barème par tranche, crédit sans intérêt sur 25 ans) ; 2021 : commission nationale abrogée (DL n° 2021-21, art. 16, rubrique « Accélération du rythme d'exécution du programme de logement social » ; ajustement) |
| Premier logement | 2017 : naissance (réforme 4) | 2017 : décret n° 2017-161 ; 2025 : « acquisition » → « acquisition ou construction » (LF 2025, art. 25, rubrique AR « دعم الدور الاجتماعي للدولة في مجال السكن ») |
| Opérateurs | 2026 : financement par le fonds et location-vente (réforme 5) | 1957 : objet de la SNIT (antécédent) ; 1977 : SPROLS (mise en place) ; 2010 : tutelle de la SPROLS à l'Équipement (`decret2010-3170`, déjà au précis ; ajustement, domicile entreprises publiques) ; 2026 : lois n° 2026-1 et 2026-2, décret n° 2026-123, art. 9 bis |
| Régime spécial de 1999 | 1999 : rachat des logements anciens appartenant à des étrangers, « dans le cadre de l'exécution d'accords internationaux » (décret n° 99-96, art. 1er-3) | aucune lue |

**Désaccord possible, décret n° 2023-127.**
- Lecture retenue : étape de 2016. Il étend par palier le public d'un instrument existant
  (quatrième catégorie) ; la doctrine classe en étape l'extension d'une rupture « d'un public à
  l'autre ».
- Lecture concurrente : rupture, à cause de deux changements nouveaux : l'ouverture aux
  retraités et le passage du salaire du demandeur au revenu du ménage.
- Si le propriétaire retient la rupture, le chapitre a six réformes, à la limite de la doctrine.

## 4. Le plan du chapitre

Fichier `precis/fr/prestations_sociales/_logement_social.qmd`. En-tête :

`# Le logement social : le fonds de promotion du logement pour les salariés et les programmes publics {#sec-logement-social .domicile-unique}`

Bloc Python d'en-tête copié de `_non_contributives.qmd` (`figtools`, `table()`), seulement si une
figure ou un tableau engendré est rendu.

**Alinéas de tête, avant la vue d'ensemble : les renvois, puis l'objet.**
- Renvois : contribution → [cotisations](../cotisations_sociales/_prelevements_salaires.html#sec-cot-foprolos) ;
  contribution au FNAH → [finances locales](../finances_locales/_impots_immeubles.html#sec-fl-immeubles-fnah) ;
  statut des sociétés et agences publiques → [entreprises publiques](../entreprises_publiques/index.html) ;
  priorité d'accès des catégories de l'Amen social → `@sec-nc-amen-2019`.
- Objet, en une phrase : l'État aide des ménages à se loger par des prêts à taux réduit, des
  subventions et des logements produits par des organismes publics. Ces aides sont financées par
  une contribution sur les salaires et par le budget de l'État.
- Ordre du chapitre.
- Sous le titre : `<!-- TODO (architecte) : chapitre à migrer vers un livre « Le logement » (partie IV) quand il sera ouvert ; ancres sans nom de livre ; voir backlog-precis.md. -->`

### 4.1 Vue d'ensemble `{#sec-log-vue-ensemble}`
- **À établir** : ce qui est servi, à qui, financé par qui, depuis quand.
- **Premier plan** : tableau des naissances, court (§ 5, T1).
  - Colonnes : Depuis ; Dispositif ; Qui y a droit ; Financé par ; Forme ; Où lire.
  - Lignes : 1977 prêts du fonds ; 1977 SPROLS ; 1986 programme de résorption ; 2004 FNAH
    refondu ; 2012 programme spécifique ; 2016 refonte des prêts ; 2017 premier logement ; 2026
    financement des opérateurs et location-vente.
  - Il tient lieu de frise.
- **Trois points :**
  1. une ressource sur les salaires pour les salariés, et le budget pour les autres ;
  2. le fonds prête aux personnes, puis, depuis 2026, finance aussi des projets ;
  3. les publics se définissent en multiples du SMIG ; ils s'échelonnent de moins de 1 SMIG
     (programme spécifique, catégorie 1) à 10 SMIG (premier logement).
- **Replié** : rien.
- Glossaire : `#g-fonds-foprolos`, `#g-foprolos` (la contribution), `#g-smig`, `#g-logement-social`,
  `#g-premier-logement`, `#g-programme-specifique-logement-social`.

### 4.2 La mise en place, 1957-1977 `{#sec-log-mise-en-place}`

#### Avant 1977 `{#sec-log-antecedents}`
- **À établir** : ce que le texte de 1977 trouve en place.
- **Premier plan, faits lus seulement :**
  - SNIT, 1957 : société de l'État régie par le droit des sociétés anonymes, intermédiaire pour
    les crédits publics HBM et HLM (loi n° 57-19, statut art. 1er, 3, 6, 8) ;
  - épargne-logement : le décret n° 77-964 la modifie le même jour que le décret d'application et
    vise la loi n° 73-24.
- **TODO (documentaliste), sans fait en prose** : FNAH de 1956 ; sociétés HBM et HLM, et caisse
  mutuelle de crédit immobilier ; CNEL ; AFH (1973-1974) ; textes du Protectorat. Ils sont
  connus par leur seul intitulé ; OCR requis (§ 6 de la note).
- Glossaire : `#g-snit`, `#g-epargne-logement` (entrée sans référence : ancre provisoire),
  `#g-afh` (même réserve).
- **Replié**, bloc « Avant 1977 : la SNIT et l'épargne-logement, textes et articles, 1957-1977 »,
  colonne Portée = « antécédent » :
  - loi n° 57-19 (`r-log-snit-1957`) ;
  - décret n° 77-964 (`r-log-epargne-1977`).
- Discordance de date de la loi n° 59-58 : en TODO, pas dans le texte.

#### Les lois du 3 août 1977 `{#sec-log-1977}`
- **À établir** : l'architecture d'origine (ressource, statut du fonds, gestion, prêts) et ce que
  la loi reprend ou écarte.
- **Premier plan :**
  - objet du fonds, cité (art. 5) ;
  - ressources (art. 6) ; renvoi à la contribution ;
  - fonds spécial du Trésor, ordonnateur, gestion confiable à un organisme de crédit (art. 9 ;
    loi n° 77-60, art. 14) ;
  - tableau court des deux prêts de 1977 (T2) ;
  - naissances groupées, une ligne chacune avec renvoi : SPROLS → `#sec-log-operateurs` ;
    crédits de préfinancement aux promoteurs (art. 7).
- **Contexte** : `<!-- TODO (documentaliste) : contexte de 1977 … -->`.
- **Dates d'effet** :
  - contribution exigible au 1er août 1977 (art. 10) ;
  - décret exécutoire au 1er décembre 1977, sous réserve de confirmation (question).
- **Replié** : rien. Les lignes vont aux registres (a), (b), (c) du § 4.3.
- Glossaire : `#g-sprols`, `#g-fonds-special-tresor`, `#g-promoteur-immobilier`,
  `#g-habitation-principale`.

### 4.3 Les grandes réformes, 1986-2026 `{#sec-log-reformes}`
- **Premier plan** : une phrase, puis le tableau court des cinq réformes (T3, non replié).
  - Colonnes : réforme et date ; ce que la loi cherche ; avant → après ; mise en œuvre.
  - Pas de citation dans les cellules : liens vers les registres.

#### 1986-1990 : la résorption des logements rudimentaires, financée en partie par le fonds `{#sec-log-1986}`
- **Premier plan :**
  - le programme de 1986 en deux ou trois phrases (pourquoi, pour qui), renvoi à `#sec-log-pnrlr` ;
  - les quatre prélèvements, 5, 5, 15 et 15 MD ;
  - le taux de la contribution ramené à 1 % en 1989, dans une proposition avec lien.
- Contexte : TODO. Glossaire : `#g-logement-rudimentaire`.

#### 1990-2011 : l'ordonnateur, un régime spécial, le FNAH refondu `{#sec-log-entre-temps}`
- **Premier plan** : un paragraphe d'entre-temps, avec renvois aux registres et aux sections
  `#sec-log-regime-1999` et `#sec-log-fnah`.
- `<!-- TODO (documentaliste) : modificatifs du décret n° 77-965 de 1981 à 2015 … -->` (liste au
  § 6).

#### 2012 : le programme spécifique pour le logement social `{#sec-log-2012}`
- **Premier plan :**
  - rubrique et art. 27 cités ;
  - financeur et opérateurs ;
  - renvoi à `#sec-log-psls` ;
  - un paragraphe sur les prélèvements de 2011-2013, présentés comme la reprise du mécanisme de
    1987 (lecture A) ; aucun montant hors du texte : 40, 60 et 60 MD.

#### 2016 : la refonte des prêts du fonds `{#sec-log-2016}`
- Entre 2012 et 2016, une phrase : arrêté de prix de 2013, renvoi au registre (c).
- **Premier plan :**
  - ce qui change : trois catégories jusqu'à 4,5 SMIG ; terrain, extension, don pour la
    catégorie 1 ; incessibilité de 10 ans ; annuités au plus 40 % du revenu ;
  - pas de récit de 2023 ici : il vient dans l'entre-temps 2017-2026, à sa date.
- **Pas de grille dans cette section** : la grille en vigueur est dans l'état du droit. La grille
  de 2016 va dans le registre (c), cellule « avant → après » de la ligne du décret
  n° 2023-127.
- « Avant » daté de 1977, avec `<!-- TODO (documentaliste) : états de 1981 à 2015 … -->`.

#### 2017 : le programme du premier logement `{#sec-log-2017}`
- **Premier plan** : rubrique ; 200 MD ; public de 4,5 à 10 SMIG, qui commence où finit la
  catégorie FOPROLOS 3 de 2016 ; renvoi à `#sec-log-premier-logement`.

#### 2017-2026 : une quatrième catégorie de prêts, des retraités parmi les bénéficiaires `{#sec-log-entre-temps-2023}`
- **Premier plan** : le décret n° 2023-127, étape de 2016, en un paragraphe :
  - « premier logement » ;
  - quatrième catégorie jusqu'à 6 SMIG, sur le revenu du ménage ;
  - retraités, avec 24 mois de cotisation ;
  - terrain acheté au privé.
  La grille est renvoyée à l'état du droit (`#sec-log-etat-du-droit`).
- Une phrase pour 2021 et 2025, avec renvois à `#sec-log-psls`, `#sec-log-premier-logement` et
  `#sec-log-fnah`.

#### 2026 : le fonds finance les logements des opérateurs publics `{#sec-log-2026}`
- **Premier plan :**
  - rubriques de la LF 2026 (AR, traduction validée par le terminologue) ;
  - contexte : document parlementaire de novembre 2025, en mots seulement ;
  - ce qui change pour le fonds ;
  - deux phrases sur la location-vente et la vente à tempérament, renvoi à `#sec-log-operateurs`.
- Glossaire : `#g-location-vente`, `#g-vente-a-temperament`.

**Registres des règles de base, repliés en fin de section.** Trois blocs ; colonnes : Date
d'effet | Portée | Texte et article | Avant → après.

- (a) **« Ressources du fonds et prélèvements sur le fonds : textes et articles, 1977-2026 »**
  - Lignes :
    - loi n° 77-54, art. 6 et 10 ;
    - LF 1989, art. 35 (taux, renvoi cotisations) ;
    - LF 1987, art. 96 ; LF 1988, art. 76 ; LF 1989, art. 68 ; LF 1990, art. 46 ;
    - DL n° 2011-56, art. 3 ; LFC 2012, art. 36 ; LF 2013, art. 11 ;
    - LF 2026, art. 21.
  - Ancres : `r-log-res-1977`, `r-log-prel-1987` … `r-log-prel-2013`, `r-log-res-2026`.
- (b) **« Gestion du fonds : fonds spécial du Trésor, ordonnateur, gestionnaire, 1977-1993 »**
  - Lignes : loi n° 77-54, art. 9 ; loi n° 77-60, art. 14 ; LF 1993, art. 34.
  - `<!-- TODO -->` : DL n° 2011-55 et convention de gestion avec la Banque de l'Habitat, avec
    l'ancre `RECHERCHE r-foprolos-convention-gestion`.
- (c) **« Prêts du fonds aux salariés : bénéficiaires, plafonds, taux et durées, textes et articles, 1977-2026 »**
  - Lignes :
    - décret n° 77-965, art. 1er-12 ;
    - arrêté du 29 juillet 2013 (prix plafonds : 45 000 D, 57 500 D, 62 000 à 77 500 D) ;
    - décret n° 2016-1126, art. 1er-12, avec la grille de 2016 ;
    - décret n° 2023-127, art. 1er ;
    - décret n° 2026-123, art. 1er (alinéa 5 de l'art. 1er) et art. 9 bis.
  - `<!-- TODO -->` adjacent : les quatorze modificatifs non lus de 1981 à 2015, les arrêtés de
    prix de 2007, 2009 et 2014, l'arrêté de procédure et le programme annuel ; ancre
    `RECHERCHE r-foprolos-programme-emploi`.
- **Règle du registre.** Un texte connu par son seul intitulé n'a **pas** de ligne visible :
  AGENTS.md exige que la colonne de contenu donne le changement concret. Il va dans le TODO
  adjacent. Cela restreint, pour le texte rendu, la consigne du rôle (« peut avoir sa ligne au
  registre »).

### 4.4 L'état du droit en 2026 `{#sec-log-etat-du-droit}`
- **À établir** : l'état des règles de base, daté. La note le donne au 2 octobre 2026 (dernière
  publication indexée) ; écrire « en 2026 », pas la manière dont il a été établi.
- **Premier plan, non replié :**
  - objet et ressources du fonds (complet) ;
  - **tableau des prêts par catégorie** (T4). Rédaction de 2023, complétée en 2026 :
    - quatre catégories ;
    - revenu du ménage ;
    - pour la construction, le terrain et le logement de promoteur : surface, autofinancement,
      prêt au plus, taux, durée, grâce ;
    - âge limite ;
    - don de la catégorie 1 ;
  - colonne « population couverte » avec `<!-- TODO (documentaliste) : aucune série de
    bénéficiaires depuis 2013 -->` (§ 4 des conventions) ;
  - financement des projets des opérateurs (2026), une ligne.
- **Fait main**, avec `<!-- TODO (rédacteur) : remplacer par un tableau engendré -->`. Paramètres
  à proposer au modéliste (`backlog-modele.md`, § 8).
- **Pas écrit comme état du droit**, chacun avec son TODO :
  - l'ordonnateur après le DL n° 2011-55 ;
  - la survie du régime de 1999 ;
  - la survie de l'arrêté de prix de 2014 ;
  - la modification de la loi n° 77-54 par la LF 1994.
- **Hors de cette section** : l'état des dispositifs se dit dans leur section. Il n'est pas
  établi pour le programme spécifique, le premier logement, le FNAH et les opérateurs. Ces
  sections disent la dernière rédaction lue avec sa date, et un TODO.

### 4.5 La résorption des logements rudimentaires et le Fonds national d'amélioration de l'habitat `{#sec-log-rudimentaire}`
- **Situation dans l'histoire** : née de la réforme de 1986-1990. Renvoi en tête vers les
  finances locales pour la contribution au FNAH.

#### Le programme national de 1986 `{#sec-log-pnrlr}`
- **Premier plan :**
  - objet (art. 1er) ;
  - définition du logement rudimentaire, citée ;
  - comité national présidé par le Premier ministre (art. 2) ;
  - ressources : contribution de 10 % de l'impôt sur les BIC et l'IS dus en 1986, reconduite en
    1987 (élargie aux BNC) et 1988 ; « journée de travail » des salariés au-delà de 1,5 SMIG en
    1987 ; prélèvements sur le fonds (renvoi `#sec-log-1986`) ; 1,5 MD sur le FNAH en 1988.
- **TODO** : décret n° 87-709 ; arrêté du 2 mai 1987 ; fin du programme.
- **Replié**, bloc « Programme national de résorption des logements rudimentaires : textes et
  articles, 1986-1990 » : décret n° 86-438 ; loi n° 86-47 ; LF 1987, art. 34-39 ; LF 1988,
  art. 42-47 et 77.

#### Le Fonds national d'amélioration de l'habitat `{#sec-log-fnah}`
- **Premier plan :**
  - les cinq emplois de la loi n° 2004-77 (art. 1er A à E) ;
  - prêts et subventions (art. 2-3) ;
  - gestion bancaire (art. 4) ;
  - 2005, fonds spécial du Trésor : renvoi à `#sec-fl-immeubles-fnah`, où la LF 2005 est déjà
    citée ;
  - 2012 : « occupants privés » ajoutés ;
  - prélèvements de 2011-2013, rappelés par un lien vers `#sec-log-2012` ;
  - 2025 : prêts pour citernes, prorogés jusqu'au 31 décembre 2027.
- `#g-fnah`, `#g-contribution-fnah`.
- **TODO** : décrets n° 2007-534 et 2007-535 ; LF 2023, art. 28 ; FNAH de 1956 à 1966.
- **Replié**, bloc « Fonds national d'amélioration de l'habitat : textes et articles,
  2004-2025 ».

### 4.6 Le programme spécifique pour le logement social `{#sec-log-psls}`
- **Situation dans l'histoire** : né de la réforme de 2012.
- **Premier plan :**
  - définitions : logement rudimentaire, art. 7 ; logement social, art. 20 ;
  - public : trois catégories jusqu'à 3 SMIG (art. 21) ;
  - remplacement d'un logement rudimentaire : coût plafonné à 35 000 ou 45 000 D, 50 % à la
    charge de l'État, le reste en crédit de 25 ans sans intérêt (art. 18-19) ;
  - **tableau court du barème de subvention de 2012** (art. 22 ; T5), titré par sa date ;
  - commission nationale abrogée en 2021.
- **État non établi** : TODO listant les décrets n° 2013-3289, 2014-4251, 2015-460, 2023-538 et
  2012-1225 ; les arrêtés des art. 22-23 (ancre `RECHERCHE r-psls-arretes-subvention-credit`) ;
  les dettes des bénéficiaires (LF 2018, art. 61 ; DL n° 2022-79, art. 16 ; arrêtés de 2016 et
  2023) ; les cessions de terres au dinar symbolique.
- **Replié**, bloc « Programme spécifique pour le logement social : textes et articles,
  2012-2021 ».

### 4.7 Le programme du premier logement `{#sec-log-premier-logement}`
- **Situation dans l'histoire** : né de la réforme de 2017.
- **Premier plan :**
  - définition du premier logement (art. 3) ;
  - public de 4,5 à 10 SMIG (art. 5) ;
  - prêt (art. 6) : au plus 20 % du prix et 40 000 D, 5 ans de grâce sans intérêt, 7 ans de
    remboursement, 2 % ;
  - incessibilité de 12 ans ;
  - compte à la BCT ; rapports trimestriels ;
  - 2025 : construction ajoutée.
  - Tableau court T6, ou une liste.
- **TODO** : décrets n° 2017-391 et 2019-39 ; décret adapté à la construction ; date d'effet de
  la LF 2025, art. 25.
- **Replié**, bloc « Premier logement : textes et articles, 2017-2025 ».

### 4.8 Les opérateurs publics et la location-vente `{#sec-log-operateurs}`
- **Situation dans l'histoire** : SPROLS née en 1977 ; financement par le fonds et
  location-vente nés en 2026. Renvoi en tête vers les entreprises publiques pour le statut.
- **Premier plan :**
  - objets de logement social : SNIT, statut art. 3 ; SPROLS, art. 2, et capital des caisses
    (art. 4) ;
  - 2026 : financement jusqu'à 100 % du coût, sans intérêt, 25 ans ; location-vente et vente à
    tempérament ; prix plafond levé ; loyers fixés par convention projet par projet.
- **TODO** : décret n° 77-926, loi n° 93-78, AFH (décrets n° 2021-327 et 2023-584), activité des
  opérateurs.
- **Lien à signaler** au rédacteur de la fiche `r-caisses-placements-obligatoires` : la loi
  n° 77-53 fait financer le capital de la SPROLS par la CNSS et la CAVIS. Indice seulement, sans
  conclusion dans le texte.
- **Replié**, bloc « SNIT, SPROLS et AFH : missions de logement social et location-vente, textes
  et articles, 1957-2026 ».

### 4.9 Le régime spécial de 1999 : les logements anciens appartenant à des étrangers `{#sec-log-regime-1999}`
- **Premier plan** : objet, public, conditions (art. 1er-3), en un paragraphe ; aucun tableau.
- **TODO** : en vigueur ? L'art. 12 du décret n° 2016-1126 n'abroge que le décret n° 77-965 et ses
  modificatifs.
- **Repli** : aucun. La ligne de registre est placée dans le bloc (c), Portée « rupture propre au
  régime de 1999 ».

### 4.10 Ce que pèse le fonds `{#sec-log-longue-periode}`
- **Ordre** : budgétaire d'abord. Chaque sous-section dit sa famille.

#### Les prévisions des lois de finances, 2011-2020 `{#sec-log-previsions}`
- **Premier plan :**
  - figure F1 ou, en attendant, tableau T7 (10 lignes, non replié) ;
  - une phrase : prévisions des LF initiales (2012 : LFC), ressources du fonds et non produit
    brut de la contribution, dinars courants ;
  - les prélèvements de 2011-2013 marqués à part, nature distincte.
- **Pas de comparaison en prose entre prélèvements et prévisions.** Un prélèvement se fait « sur
  les disponibilités du fonds », c'est-à-dire sur le stock ; la prévision est une recette de
  l'année, c'est-à-dire un flux. La figure et le tableau donnent la nature de chaque série.
- **TODO** : avant 2011, OCR ; LF 2012 initiale à obtenir ; depuis 2021, ligne non localisée
  (ancre `RECHERCHE r-foprolos-ligne-lf-2021`) ; réalisations à obtenir.

#### Le suivi du ministère des Finances rapporté par une étude, 2009-2013 `{#sec-log-suivi-mef}`
- **Famille** : budgétaire relayé. La source est le MEF (Direction du financement) ; Zaafrane
  2014 (`zaafrane-2014-habitat`) en est le relais.
- **Premier plan** :
  - T8 : ressources, reliquat et dépenses, 2010-2013 (tableau 41, p. 63) ;
  - T9 : prêts accordés, nombre et MD, 2009-2013 (tableau 42, p. 63) ;
  - encours (282 MD), impayés en principal (66,3 MD) et taux de recouvrement (24,7 %), tous à fin
    2013 (p. 63). Ils vont dans une ligne datée de T8, jamais en prose isolée. **C'est la seule
    place de ces chiffres dans le chapitre.**
  - rémunération de la Banque de l'Habitat, 2009-2012 (p. 62).
- **Une phrase sur l'écart** : environ un à cinq avec T7. Zaafrane signale lui-même des
  « différences assez significatives » (p. 62). Les deux séries ne se mettent jamais sur une même
  figure.
- **Erreurs de l'étude à ne pas reprendre** (note § 3.2) : le sigle développé en « logements
  sociaux » ; « 1 % sur les salaires des employés ».
- **Pas de figure** : cinq points ; les tableaux suffisent.

#### Ce qu'estime une étude de 2014 `{#sec-log-etudes}`
- Subvention implicite des prêts : 7,9 à 9,6 MD par an. Méthode : encours de 282 MD, taux de
  l'étude contre 7,63 % ou 8,44 % ; seconde approche, impact nul.
- FNAH : 1,6 MD par an. Programme spécifique : 30 MD par an retenus.
- Méthode donnée pour chaque chiffre. Titrée comme étude, tenue séparée du budgétaire.
- L'éligibilité (12,5 %) va dans la section d'économie, pas ici.

### 4.11 Ce qu'en dit l'économie `{#sec-log-economie}`
- **Source** : `docs/notes/eco-logement-social.md`. Quelques paragraphes : la fiche économiste
  vise 100 à 150 lignes ; la section est courte.
- **Gabarit :**
  - la question (offre ou demande, crédit moins cher, ciblage, habitat précaire) ;
  - théorie T1-T3 ;
  - empirique international, avec plages, pays et période (Olsen, Sinai-Waldfogel, Fack,
    Gruber-Jensen-Kleven, Glaeser-Gyourko, Galiani-Schargrodsky) ;
  - Tunisie : éligibilité de 12,5 % avec les critères de 2014 (Zaafrane, p. 41, et ses
    réserves) ; ONU-Habitat 2011, pp. 63-64 ; Baharoglu et al. 2005. Le recouvrement est
    renvoyé à `#sec-log-suivi-mef`, sans répéter le chiffre ;
  - ce que le praticien retient.
- **Dernière ligne** : « Littérature arrêtée au mois d'octobre 2026. » C'est la forme des
  chapitres existants ; la fiche économiste écrit « au octobre ».
- **Glossaire** : `#g-elasticite-offre-logement`, `#g-eviction-logement`, `#g-aide-a-la-pierre`,
  `#g-aide-a-la-personne`, `#g-element-de-subvention`, `#g-incidence-fiscale`.
- **Garde-fou** : aucun chiffre de cette section dans une figure ou un tableau de paramètres.

## 4 bis. Clés CSL à citer

Vérifiées le 23 octobre 2026 dans le worktree.

- **`precis/fr/prestations_sociales/references.json`** (versées par le bibliographe) :
  - textes : `loi57-19`, `loi77-53`, `loi77-60-lfc1977`, `decret77-965`, `decret86-438`,
    `loi86-47`, `decret99-96`, `loi2004-77`, `decret2012-1224`, `arrete-2013-07-29-prix-foprolos`,
    `decret2016-1126`, `decret2017-161`, `decret2023-127`, `loi2026-1`, `loi2026-2`,
    `decret2026-123` ;
  - document parlementaire : `arp-2025-11-16-equipement` ;
  - économie : `olsen-2003-housing-programs`, `sinai-waldfogel-2005-crowd-out`,
    `fack-2005-aides-logement`, `gruber-jensen-kleven-2021-mortgage-deduction`,
    `glaeser-gyourko-2018-housing-supply`, `galiani-schargrodsky-2010-titling`,
    `buckley-kalarickal-2006-shelter-lending`, `baharoglu-peltier-buckley-2005-mena-housing`,
    `bm-2003-rehabilitation-urbaine`, `onu-habitat-2011-tunisia-housing-profile`.
- **`precis/fr/references.json`** (commun) :
  - fondateur : `loi77-54` ;
  - lois de finances anciennes : `loi86-106-lf1987` (art. 34-39, 49, 95, 96) ;
    `loi-87-83-lf-1988` (art. 42-47, 76, 77) ; `loi-88-145-lf-1989` (art. 35, 68) ; `lf-1990`
    (art. 46 ; **pas** `loi-89-115-lf-1990`, rangée en fiscalité et injoignable d'ici) ;
    `lf-1993` (art. 34) ;
  - lois de finances depuis 2011 : `dl-2011-56-lfc-2011` (art. 3) ; `lfc-2012` (art. 27-36 ;
    tableau B, p. 938) ; `lf-2013` (art. 11 ; tableau B) ; `lf-2017` (art. 61 ; tableau B) ;
    `lf-2022` (DL n° 2021-21, art. 16) ; `lf-2025` (art. 25, 27) ; `lf-2026` (art. 21) ;
  - tableaux B de T7 : `lf-2011`, `lf-2014`, `lf-2015`, `lf-2016`, `lf-2018`, `lf-2019`,
    `lf-2020` ;
  - autres : `decret2010-3170` ; `zaafrane-2014-habitat` ; `gruber-1994-mandated-maternity`
    (économie, T3).
- **Sans clé, à créer avant toute citation** : **`decret77-964`**. Il est lu (JORT n° 78/1977,
  p. 3272) et appelé par le registre `r-log-epargne-1977`, mais n'est ni versé ni proposé au § 2.2
  de la note. Demande au bibliographe (§ 8.10) ; sinon la ligne de registre est retirée et le
  fait passe en TODO.
- **Non cités, simple renvoi** : `lf-2005` (finances locales), `lf-2018` et `lf-2023` (textes
  non lus, en TODO).

## 5. Figures et tableaux

| Id | Contenu | Source | État |
|---|---|---|---|
| T1 | Naissances des dispositifs (vue d'ensemble) | note § 1 | faisable maintenant |
| T2 | Deux prêts de 1977 | décret n° 77-965, art. 2-6 | faisable maintenant |
| T3 | Cinq grandes réformes | § 3.2 de cette fiche | faisable maintenant |
| T4 | Prêts par catégorie en 2026 | décret n° 2016-1126 réd. 2023-127 ; décret n° 2026-123 | faisable maintenant, fait main + TODO tableau engendré (paramètres non portés en amont) |
| T5 | Barème de subvention du programme spécifique, 2012 | décret n° 2012-1224, art. 22 | faisable maintenant ; daté 2012, non présenté comme état actuel |
| T6 | Conditions du premier logement, 2017 | décret n° 2017-161, art. 3-7 | faisable maintenant |
| T7 | Prévisions de ressources du fonds, 2011-2020 (10 valeurs) et prélèvements 1987-1990, 2011-2013 | note § 3.1 et § 1.4 | tableau faisable maintenant |
| F1 | Figure de T7 : barres des prévisions, marques des prélèvements (autre nature) et des réformes de 2012, 2016, 2017 | idem | **après travail de données** : verser la série dans `tunisia-data` avec sa fiche de provenance (valeur, LF, page, édition FR/AR, 2012 révisée par LFC) ; module `figures/logement.py` lisant `figtools.series()`. Dinars constants : seulement si l'IPC du cache le permet, à vérifier |
| T8, T9 | Suivi MEF 2009-2013 (tableaux 41 et 42 de Zaafrane) | `zaafrane-2014-habitat`, p. 63 | faisable maintenant ; sous-section à part |
| — | Série des réalisations, bénéficiaires, logements produits, données de la BCT sur le premier logement | — | à documenter d'abord (note § 3.5) |

`precis/_seriescache/` ne contient aucune série du logement social. Il porte un indice des prix
de l'immobilier de l'INS, mais ce chiffre n'a pas été lu par la note : il n'entre pas dans ce
chapitre.

## 6. Classement des textes de la note

Abréviations : R = rupture ; E(x) = étape de la rupture x ; A = ajustement ; Ant = antécédent ;
H = hors sujet (domicile ailleurs). La colonne « lu » reprend la note.
- Les textes **non lus**, connus par leur seul intitulé, vont en TODO, pas en ligne visible.
- **R-1977** désigne la mise en place, **R1** à **R5** les cinq réformes.

| Texte | Lu | Dispositif | Classement |
|---|---|---|---|
| Décrets FNAH 1956-1957, loi n° 60-5, DL n° 63-1, loi n° 66-75 | intitulé | FNAH | Ant ; TODO |
| Loi n° 58-82, DL n° 61-7 / loi n° 61-29, loi n° 61-18, décrets de liquidation HBM 1967-1985 | intitulé | antécédent | Ant ; TODO |
| Loi n° 57-19 (SNIT) | FR | opérateurs | Ant |
| Lois n° 58-47, 59-58, 61-57 | intitulé | opérateurs | TODO (date de la loi n° 59-58 discordante) |
| Loi n° 73-24, décrets n° 74-223, 74-224 | intitulé | antécédent | Ant ; TODO |
| Décret n° 77-964 | FR | prêts | Ant (accompagne la mise en place) |
| Loi n° 73-21, décret n° 74-33 (AFH) | intitulé | opérateurs | TODO |
| Loi n° 77-54, art. 1er-10 | FR | règles de base | R-1977 (art. 1er-3 : domicile cotisations) |
| Loi n° 77-60, art. 14 | FR | gestion | R-1977 |
| Décret n° 77-965 | FR | prêts | R-1977 |
| Loi n° 77-53 | FR | opérateurs | R-1977 (naissance groupée) |
| Décret n° 77-926, décrets n° 92-1818, 2017-840, loi n° 93-78 | non | opérateurs | TODO |
| Décret n° 2010-3170 | déjà au précis | opérateurs | A (tutelle) ; domicile entreprises publiques |
| LF 1993, art. 34 | FR (OCR) | gestion | A |
| DL n° 2011-55 | non | gestion | TODO |
| Modificatifs du décret n° 77-965 : 81-1010, 83-927, 86-293, 88-1589, 90-1280, 93-1720, 95-789, 98-2093, 2000-1192, 2007-12, 2007-4099, 2009-698, 2009-3586, 2011-3573, 2015-881 | non | prêts | TODO ; portée non relevée |
| Décret n° 99-96 | FR | régime de 1999 | R propre au régime |
| Décret n° 2016-1126 | FR | prêts | **R3** (lecture b : E ou A) |
| Décret n° 2023-127 | FR | prêts | **E(R3)** (lecture concurrente : R) |
| Décret n° 2026-123, art. 1er (al. 5) | AR | opérateurs et règles de base | E(R5) |
| Décret n° 2026-123, art. 9 bis | AR | opérateurs | E(R5) |
| LF 1987, art. 96 | FR | ressources | **R1** pour le fonds |
| LF 1988, art. 76 ; LF 1989, art. 68 ; LF 1990, art. 46 | FR | ressources | E(R1) |
| LF 1988, art. 77 | FR | FNAH / programme 1986 | E (ressource du programme), registre du programme |
| LF 1987, art. 95 ; LF 2023, art. 57 § 8 | FR ; AR | recouvrement | H (cotisations) |
| LF 1987, art. 49 ; LF 2013, art. 22 | FR | assiette | H (cotisations) |
| LF 1989, art. 35 | déjà au précis | taux | H (cotisations) ; une proposition dans R1, ligne A au registre (a) |
| DL n° 2011-56, art. 3 ; LFC 2012, art. 36 ; LF 2013, art. 11 | FR | ressources | E(R1) (lecture B : partie de R2) |
| LF 2026, art. 21 | AR | règles de base | **R5** |
| Lois n° 2026-1, 2026-2 | FR | opérateurs | E(R5) |
| Décret n° 86-438 | FR (OCR) | programme 1986 | R propre ; naissance dans R1 |
| Décret n° 87-709 ; arrêté du 2 mai 1987 | non | programme 1986 | TODO |
| Loi n° 86-47 ; LF 1987, art. 34-39 ; LF 1988, art. 42-47 | FR (OCR) | programme 1986 | E (ressources) ; contribution : domicile fiscalité à venir |
| Loi n° 2004-77 | FR | FNAH | R propre au FNAH |
| LF 2005, art. 11-17 | non selon la note ; cité art. 11-16 par les finances locales | FNAH | renvoi finances locales ; **question** |
| Décrets n° 2007-534, 2007-535, 2012-509, 2012-750 | non | FNAH | TODO |
| LFC 2012, art. 33-35 | FR | FNAH | E(R FNAH 2004) |
| LF 2023, art. 28 | intitulé | FNAH | TODO |
| LF 2025, art. 27 | AR | FNAH | A |
| LFC 2012, art. 27-31 | FR | programme spécifique | **R2** |
| LFC 2012, art. 32 ; DL n° 2021-21, art. 16 | FR | programme spécifique | A |
| Décret n° 2012-1224 | FR | programme spécifique | E(R2) |
| Décrets n° 2013-3289, 2014-4251, 2015-460, 2023-538, 2012-1225, 2015-152 | non | programme spécifique | TODO |
| Décrets de cession de terres 2016-2026 | intitulé | programme spécifique | TODO |
| LF 2018, art. 61 ; DL n° 2022-79, art. 16 ; arrêtés de 2016 et n° 2023-119 | intitulé | programme spécifique | TODO |
| LF 2017, art. 61 | FR | premier logement | **R4** |
| Décret n° 2017-161 | FR | premier logement | E(R4) |
| Décrets n° 2017-391, 2019-39 | non | premier logement | TODO |
| LF 2025, art. 25 | AR | premier logement | E(R4) |
| Décret n° 2018-749 (fonds de garantie) | intitulé | — | TODO dans la vue d'ensemble (dispositif possible, non décrit) |
| Décret n° 2019-835 | intitulé | caisses | H |
| Décret n° 2005-1545 | intitulé | — | H |
| Arrêté du 29 juillet 2013 | FR | prêts | A |
| Arrêtés de prix de 2007, 2009, 2014 | non | prêts | TODO |
| Arrêté du 5 janvier 1987 (prévisions 1986) | non | données | TODO |
| LF 2011 à 2020, tableau B | FR / AR | données | T7 |

## 7. Questions au documentaliste

1. **Contexte** de 1977, 1986-1990, 2012, 2016 et 2017, dans les mots des sources de l'époque :
   Ve et VIIe Plans, débats du 29 juillet 1977, ANC 2012, stratégie de l'habitat 2014-2015. La
   liste « où chercher » est au § 6 de la note.
2. **Rubriques mot pour mot** des articles : LF 1987, art. 96 ; LF 1988, art. 76 ; LF 1989,
   art. 68 ; LF 1990, art. 46 ; DL n° 2011-56, art. 3 ; LFC 2012, art. 36 ; LF 2013, art. 11.
3. **« Avant » de 2016 (prioritaire).** Lire les décrets n° 2009-698, 2009-3586 et 2015-881 ;
   localiser le n° 2011-3573. Faute de quoi la réforme de 2016 reste une rupture « sous
   réserve ».
4. **LF 2005, art. 11-16** : cités comme lus dans `_impots_immeubles.qmd` (`lf-2005`, p. 3433), non
   lus selon la note. Harmoniser.
5. **Règle des dates d'effet depuis le 14 avril 2020.** La note applique le « lendemain de la
   publication » sur consigne du brief ; AGENTS.md ne connaît que la loi n° 93-64. Fondement
   textuel ? Textes concernés : n° 2023-127, 2026-1, 2026-2, 2026-123. Le registre attend la
   réponse.
6. Date d'effet de la LF 2025, art. 25 et 27 (article final).
7. **DL n° 2011-55** (ordonnateur) ; modification de la loi n° 77-54 par la LF 1994.
8. **Survies** : le régime de 1999 est-il en vigueur ? l'arrêté de prix de 2014 survit-il après
   2016 ?
9. **Points de la note** : date de la loi n° 59-58 ; exécution du décret n° 77-965 au
   1er décembre 1977 ; date de publication du JORT n° 53/1977 (« 5-9 août »).
10. **État en vigueur** du programme spécifique (quatre modificatifs) et du premier logement
    (n° 2017-391, 2019-39).
11. **Programme de 1986** : décret n° 87-709 ; fin du programme.
12. LF 2023, art. 28 (citernes) ; SPROLS (décret n° 77-926, loi n° 93-78) ; AFH (décret
    n° 2021-327).
13. **Ressources du fonds** : ligne depuis la LF 2021 ; LF 2012 initiale ; réalisations (lois de
    règlement, rapports de la Banque de l'Habitat).
14. Traduction des rubriques arabes de la LF 2026, art. 21 et de la LF 2025, art. 25. Pour le
    terminologue, avant citation.

## 8. Modifications connexes (à faire par le rédacteur dans le même changement)

1. **`precis/fr/cotisations_sociales/_prelevements_salaires.qmd`, l. 81 (affectation).**
   - Remplacer « dès 1988, la loi de finances y opère un prélèvement … [@loi-87-83-lf-1988,
     art. 76] » par une phrase qui date le premier prélèvement de 1987 [@loi86-106-lf1987,
     art. 96].
   - Mentionner, années seulement, les prélèvements jusqu'en 1990, puis de 2011 à 2013 au profit
     du FNAH et, en 2011, du Compte national de solidarité sociale [@dl-2011-56-lfc-2011, art. 3;
     @lfc-2012, art. 36; @lf-2013, art. 11].
   - Ajouter un lien vers `../prestations_sociales/_logement_social.html#sec-log-reformes`.
   - **Montants (40, 60, 60 MD) non recopiés** : ils vivent dans le chapitre du logement.
   - Garder la phrase sur la LF 2026, art. 21, et ajouter le lien vers `#sec-log-2026`.
   - Ne pas citer `decret2026-123` : la clé n'est que dans `prestations_sociales/references.json`.
   - **Supprimer le TODO 2011-2013 (l. 83)** : textes lus.
2. **Même fichier, `#sec-cot-prelevements-rendement`.**
   - « de 2016 à 2019 au moins » devient : les prévisions du fonds de 2011 à 2020 sont présentées
     dans le chapitre du logement social (lien `#sec-log-previsions`).
   - Le TODO est réduit à la taxe de formation professionnelle.
3. **`precis/fr/finances_locales/_impots_immeubles.qmd`, `#sec-fl-immeubles-fnah`** : une phrase
   et un lien vers `#sec-log-fnah` (emploi du fonds).
4. **`precis/fr/prestations_sociales/_quarto.yml`** : ajouter `_logement_social.qmd` après
   `_non_contributives.qmd`.
   - `_quarto.yml` arabe : rien tant que la traduction n'est pas livrée.
   - Ligne au backlog : ajouter le chapitre au `_quarto.yml` arabe à la livraison.
5. **`precis/fr/prestations_sociales/index.qmd`.** **Il n'a pas de tableau de voisinage** : le
   voisinage y est dit en prose, au premier paragraphe. La prémisse du brief ne vaut pas.
   - Proposé :
     - (a) une proposition dans le premier paragraphe ;
     - (b) le deuxième paragraphe nomme le logement social parmi ce que le volume traite ;
     - (c) lignes dans `tbl-prest-naissances` : 1977 prêts du fonds ; 2012 programme
       spécifique ; 2017 premier logement ;
     - (d) une puce dans « Les chapitres du volume » ;
     - (e) corriger « cinq chapitres ; quatre suivent » et « Les trois chapitres suivants ».
   - Créer le tableau de voisinage du § 4 : au propriétaire, sinon à la conversion de la
     présentation. Ligne au backlog.
   - **Colonne « Forme » pour un prêt à taux réduit**, deux lectures à trancher :
     - « monétaire », puisqu'une somme est prêtée ;
     - « non monétaire : crédit ».
     - Logement cédé en location-vente : non monétaire.
6. **`precis/fr/index.qmd`, l. 77** (« le logement » à venir). Au propriétaire :
   - laisser tel quel ;
   - ou ajouter dans la description des « Prestations sociales » (l. 61) « et les aides au
     logement social ».
   - Je propose la seconde, sans toucher à la l. 77.
7. **`docs/notes/backlog-precis.md`** :
   - item 13 : « chapitre rédigé le … dans `prestations_sociales/_logement_social.qmd`, à titre
     provisoire ; à migrer vers un livre « Le logement » quand il s'ouvrira (ancres `sec-log-`) » ;
   - lacunes du § 7, avec la lisibilité donnée par la note (corpus, OCR, à obtenir) ;
   - contribution de la loi n° 86-47 à placer dans les taxes affectées (item 10) ;
   - catalogue `tunisia-data` du PDF de l'ARP, à créer par l'humain (note § 3.4) ;
   - versement de la série T7 dans `tunisia-data` pour F1 ;
   - tableau de voisinage de la présentation ;
   - `_quarto.yml` arabe.
8. **`docs/notes/backlog-modele.md`** : proposer au modéliste les paramètres des prêts du fonds
   (catégories, plafonds, taux, durées, 2016-2026), du premier logement et du programme
   spécifique. Aucune formule. Sinon T4 reste fait main.
9. **`docs/recherches.yml`** : verser les quatre fiches proposées au § 5 de la note, avec leur
   `ou` :
   - `r-foprolos-convention-gestion` → `precis/fr/prestations_sociales/_logement_social.qmd#sec-log-reformes`
     (registre (b)) ;
   - `r-foprolos-programme-emploi` → `…#sec-log-reformes` (registre (c)) ;
   - `r-psls-arretes-subvention-credit` → `…#sec-log-psls` ;
   - `r-foprolos-ligne-lf-2021` → `…#sec-log-previsions`.
   - Ajouter à la prochaine passe de `r-foprolos-art3-redaction` la LF 2023, art. 57 § 8, et à
     celle de `r-caisses-placements-obligatoires` l'indice de la loi n° 77-53. Ces deux passes
     sont confiées au documentaliste.
10. **Bibliographe.**
    - Citer `lf-1990`, non `loi-89-115-lf-1990` (fiscalité, injoignable d'ici). Doublons à
      signaler : `lf-1990` / `loi-89-115-lf-1990` ; `lf-2019` / `loi2018-56-lf2019` (fichier
      commun) ; `lf-1987`, `lf-1988`, `lf-1989` / `loi86-106-lf1987`, `loi-87-83-lf-1988`,
      `loi-88-145-lf-1989`.
    - `loi77-54` a bien quitté `cotisations_sociales/references.json` (vérifié : présente
      seulement dans le fichier commun).
    - URL arabes de `lf-2023`, `lf-2025`, `lf-2026` à ajouter (note § 2.1).
    - `decret2026-123` : `title-short` en français, `title` en arabe.
    - **Créer `decret77-964`** (décret n° 77-964 du 24 novembre 1977, JORT n° 78 du 29 novembre
      1977, p. 3272, art. 1er et 3, lu à l'image ; URL `1977F/Jo07877.pdf`, la même que
      `decret77-965`), dans `prestations_sociales/references.json`.
11. **Terminologue.** Définitions des 17 entrées provisoires. `#g-afh`, `#g-epargne-logement` et
    `#g-logement-social` n'ont pas de référence. Forme arabe de `#g-logement-rudimentaire` à
    confirmer.

## 9. Risques du plan, à trancher

- **2016 rupture ou étape** (§ 3.2) ; **2023 étape ou rupture** (§ 3.3) ; **2011-2013 : lecture A
  ou B** (§ 3.1).
- **2017 compté comme réforme** alors qu'il ne touche pas le fonds. Autre choix : le traiter
  seulement dans sa section, l'histoire du chapitre ne gardant que quatre réformes.
- **Trente-huit ans de régime des prêts sont absents** : de 1977 à 2016, quatorze modificatifs
  ne sont pas lus. Ils sont en TODO, pas en lignes visibles. Le lecteur voit 1977 puis 2016 ; le
  texte ne doit pas suggérer qu'il n'y a rien entre les deux. Une phrase de l'entre-temps peut
  dire que les conditions ont été modifiées à plusieurs reprises : le fait est connu par les
  intitulés. **À trancher** : cette phrase est-elle admise, alors que la note ne lit pas les
  textes ? À défaut, TODO seul.
- **Antécédent mince** : deux faits lus. La règle « rien ne naît ex nihilo » est tenue a minima.
- **Écart d'un à cinq** entre les prévisions des lois de finances et le suivi du MEF : risque de
  lecture croisée. Il est conjuré par deux sous-sections et aucune figure commune.
- **Statut et objet des opérateurs** : la loi n° 2026-1 complète l'objet statutaire de la SNIT,
  matière des entreprises publiques. Lecture retenue : la location-vente est une modalité de
  l'aide au logement, elle reste ici, et le livre des entreprises publiques reçoit un lien.
- **Migration** : le jour où le livre « Le logement » s'ouvre, les liens entrants (cotisations,
  finances locales, présentation) changent de chemin. Les ancres, elles, ne changent pas.

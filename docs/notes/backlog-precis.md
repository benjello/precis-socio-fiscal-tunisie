# Ce qui reste à faire, livre par livre

**Révisé le 6 octobre 2026.** Cette note rassemble les chantiers encore visibles dans les
chapitres, les dossiers documentaires et les issues ; elle permet de choisir le prochain
texte à lire. Une piste « faisable » signifie que le **support** est accessible, pas que
son contenu a déjà été vérifié : seul l'article lu autorise à corriger le précis.

**Responsabilité de mise à jour.** Tout agent qui ajoute, corrige ou réorganise un chapitre
met à jour **dans le même changement** son entrée ci-dessous : fermer la tâche accomplie,
dater la source effectivement lue et reclasser les suites par disponibilité. La revue
humaine contrôle cet alignement avant publication ; le documentaliste tient les fiches
de sources.
Les nombres et localisations datés ne deviennent jamais une preuve d'absence.

Les constats portant sur le modèle de microsimulation ont leur propre fichier,
`backlog-modele.md`. Les références à verser ou à corriger dans Zotero sont dans
`biblio-a-rapatrier.md`. `todo-localisation.md` localise 114 fascicules à la date du
**20 septembre 2026** : c'est un relevé historique, à recontrôler sur les fichiers du
corpus avant de citer un texte ou de dire qu'il manque. Les chemins de fascicules
ci-dessous sont relatifs à `~/projets/PDFs-legislation-tunisie/PDFs/JORT/` ; les
extraits des lois de finances sont dans le dossier voisin `PDFs/Lois_de_Finances/`.


## Chantier transversal — les ruptures au premier plan, le détail replié

- **Numérotation de l'annexe des tableaux de la TVA** (remarque du propriétaire, 7 octobre 2026) :
  « Tableau A.1 », « Tableau A.2 » de l'annexe peuvent se confondre avec les tableaux A, B et C
  du code. Pas de changement pour l'instant ; à reprendre si la confusion gêne (autre lettre
  d'annexe, ou légendes qui ne commencent pas par « Tableau A »).

Ouvert le 7 octobre 2026 ; note : `docs/notes/chantier-ruptures-au-premier-plan.md`. Prototype sur
la restitution du crédit de TVA (`_tva.qmd`, `#sec-tva-credit-restitution`) : tableau des ruptures
et de leur mise en œuvre, puis chronologie complète repliée (bloc `.chronologie-repliable`).
À juger avant toute extension ; la liste de contrôle est dans la note. Ensuite : conventions de
rédaction, consigne du rédacteur, rôle « architecte » à créer, reprise des autres chapitres.

**Prototype étendu à tout le chapitre de la TVA (7 octobre 2026, non commité, en attente du
jugement du propriétaire).** `_tva.qmd` est réécrit selon
`docs/notes/fiscalite-tva-plan-architecte.md` (§ 2, corrigé par le § 11) et
`docs/notes/fiscalite-tva-objets-des-reformes.md` : en bref ; mise en place 1988-1990 ; quatre
grandes réformes et une clôture « depuis 2018 » ; bilan des taux et état du droit ; huit
sections de dispositif, chacune avec son registre replié ; longue période. Réorganisation sans
perte : les 62 clés, les 163 couples (clé, localisateur), les 38 ancres de glossaire, les
15 identifiants, les 6 TODO et l'ancre RECHERCHE du départ sont tous à l'arrivée. Le texte
passe de 11 000 à 22 300 mots, dont 13 000 au premier plan (8 300 au départ) : quatorze blocs
repliés au lieu de deux. Reste à trancher ou à faire :

- **trajectoires par opération : tranché le 7 octobre 2026** — le propriétaire garde le tableau
  (`@tbl-tva-trajectoires`, dans `#sec-tva-etat-du-droit`) et la matrice des régimes par
  catégorie ; la section en prose `#sec-tva-trajectoires` est supprimée. Ce qu'elle seule
  portait (contrats maintenus à 6 % en 1996, article 7 en 2017, détail de 2023, reports du
  logement et des médicaments, numéro 48 du tableau A) est en cinq puces sous le tableau, et son
  registre (`tbl-tva-trajectoires-textes`, 19 ancres) est déplacé sous lui, inchangé. « Les
  dispositifs qui aménagent la taxe » n'a plus que deux sous-sections ;
- **frise des réformes** (`TODO (rédacteur)` dans « En bref ») : demande une petite série de
  jalons à verser (plan, § 6.0) ;
- **quatre clés à verser par le bibliographe** (entrées CSL au § 6 de la note des objets) :
  `minfin-plf-2018` (exposés des motifs du projet de loi de finances pour 2018 — le paragraphe
  de la réforme de 2016-2018 est écrit, attribué, sans appel de citation ; la prévision de
  313 MD par an n'est pas écrite), `dgelf-nc-2023-05` (note commune n° 5/2023, professions non
  commerciales), `rectificatif-lf-1993` (JORT n° 33 du 4 mai 1993), `minfin-plf-2014`
  (exposé des motifs sur les paiements en espèces : à relire à l'image, non écrit) ;
- **classements à confirmer** : 2014 (achats en espèces) et 2016 (facture électronique) sont
  portés « rupture » dans leurs registres, que le plan donnait pour « possibles » ;
  `tbl-tva-suspension-sectorielle` garde sa forme d'origine, sans colonne « Portée » ;
- **registres bornés à ce que le chapitre établissait** : les lignes que seules les notes
  `fiscalite-tva-reformes.md` et `fiscalite-tva-deductions-documentation.md` connaissent (plan,
  § 5 : colonnes « N2 », « N3 ») ne sont pas versées — retouches des tableaux A, B et C de
  1989 à 1994, lois de finances pour 1997, 2019, 2021 (art. 26), 2024 (art. 50), quatre lignes
  de la restitution, retouches de l'article 9 connues par le seul code consolidé. Texte présent
  au corpus pour la plupart ; lectures à confirmer à l'image avant versement ;
- **état du droit des règles de base en 2026** : la grille est établie ; le tableau A et le
  tableau B en vigueur sont donnés en annexe (`_tva_tableaux.qmd`), d'après l'édition du code à
  jour au 1er janvier 2025 et la loi de finances pour 2026 — voir l'entrée « TVA — régimes par
  catégorie et tableaux annexés » ; contenu des art. 46 et 47 de la loi de finances pour 2026 à
  détailler au registre `tbl-tva-taux-perimetre` (relevé en annexe, bloc de la loi de finances
  pour 2026) ;
- **longue période** : aucune figure nouvelle ; restent la figure du rendement par segments de
  base du PIB avec les réformes marquées, la place dans la fiscalité indirecte, la taxe
  rapportée à la consommation privée, le partage intérieur/importation (plan, § 6.1 à 6.6) ;
- **domicile unique des références étendu à tout le chapitre** (7 octobre 2026, branche de test
  `chantier/citations-domicile-unique`, non commité) : `.domicile-unique` sur le titre du chapitre ;
  176 appels juridiques retirés du fil, remplacés par 164 liens `#r-tva-…` vers les lignes de
  registre (142 ancres) ; un registre nouveau pour les clauses de date d'application
  (`tbl-tva-dates-textes`) et la liste des six grilles devenue tableau (`tbl-tva-taux-textes`).
  À juger :
  ancres des trajectoires posées dans la cellule de date ; `tbl-tva-reformes` sans liens ;
  attributs `titre` et libellés des liens à traduire en arabe ;
- **relecture du propriétaire (7 octobre 2026, non commité)** : « En bref » devient « Vue d'ensemble » ;
  le mot « cœur » ne paraît plus au chapitre (« règles de base », ou l'élément nommé) ; les renvois
  « traité ailleurs » sont en tête de section ; chaque section de dispositif s'ouvre sur une
  définition de son objet, avant sa place dans la chronologie ;
- **texte principal autosuffisant (7 octobre 2026, non commité)** : notations T et D définies dans
  chaque section qui les emploie ; règles du fait générateur, de l'option, du pourcentage de
  déduction et de la régularisation dites en clair hors des blocs repliés ; sigles développés et
  notions du glossaire ancrées dans chaque section de niveau 2 ; plus de tournure de lecture
  linéaire. Reste : « DGCPR », cité tel que la source l'écrit, sans développement établi ;
- **version arabe** : le chapitre arabe est structurellement en retard jusqu'à la passe de
  traduction ; les attributs `titre` des douze nouveaux blocs repliés sont à traduire.

## Vue d'ensemble

| Livre | État du texte | Première lecture faisable |
|---|---|---|
| Fiscalité | Cinq impôts ouverts (impôt sur la fortune ajouté le 4 octobre 2026) et un chapitre transversal sur les dépenses fiscales et les régimes d'incitation (6 octobre 2026) ; TVA : réformes de 1988 à 2026 rédigées, chapitre réorganisé le 7 octobre 2026 en prototype du chantier « ruptures au premier plan » (à juger) ; déduction, crédit et restitution, régime suspensif, déclaration et retenue à la source rédigés le 6 octobre 2026 (`@sec-tva-deduction`), séries budgétaires bornées à 2010-2014 | Décrets n° 97-1368 et 2015-1768 dans les fascicules français locaux, à lire sur pièce |
| Retraites | Deux chapitres développés ; coefficients des 31 barèmes relevés | Loi n° 2009-39 et décret n° 2009-2085 dans les JORT n° 55 et 56 de 2009, textes locaux extractibles |
| Rémunérations publiques | Régime indiciaire développé, trois autres chapitres brefs | Décret n° 2015-2217 dans le JORT n° 101 de 2015, texte local extractible |
| Prestations sociales | Dispositifs décrits ; Amen social à jour au 9 octobre 2026 (280 D, allocation des 6 à 18 ans — pilote sur don depuis 2022, décret de 2025 —, arrêté du 5 août 2026) ; PNAFN historique sans sources pour ses onze dates et montants ; volume entier au format « ruptures au premier plan » le 10 octobre 2026 (cinq chapitres ; la matrice des régimes porte aussi l'assistance) ; frontière entre régimes et assistance à établir sur trois points | Décret n° 2018-626 dans le JORT n° 63 de 2018 et LF 2025, art. 26, dans l'extrait français local |
| Cotisations sociales | Régimes et branches décrits ; échelles AT/MP de 1995 et 1999 engendrées ; plusieurs assiettes et ventilations encore à établir | Article 4 du décret n° 2007-1406 dans le JORT n° 49 de 2007, texte local extractible |
| Finances locales | Neuf chapitres rédigés ; cinq convertis au format « ruptures au premier plan » le 9 octobre 2026 (budgets, immeubles, activité, taxes, transferts), le chapitre de la longue période fondu dans les autres ; notions resserrées le même jour (cinq blocs repliés) ; histoire et compétences converties le 10 octobre 2026 : les neuf chapitres sont au nouveau format ; présentation mise en accord le même jour | Dispositions finales du code des collectivités locales (loi organique n° 2018-29), édition arabe du JORT n° 39 de 2018, texte local extractible |

Les `TODO` des `.qmd` détaillent chaque lacune, y compris celles que ce tableau ne peut pas
résumer. Ici, **lisible** veut dire que le fascicule est présent avec une couche texte
extractible sur les premières pages contrôlées ; vérifier à la page de l'article que les
tableaux ou annexes ne sont pas des images. **OCR** veut dire que le fascicule est présent,
mais que la couche texte testée est vide. Un texte absent du JORT en français peut avoir une
édition arabe ou un extrait français dans `PDFs/Lois_de_Finances/` : les distinguer.

## Fiscalité — cinq impôts ouverts, des lectures et des mécanismes à compléter

- **Figure à faire (demande de l'humain, 4 octobre 2026) : le taux d'imposition des BIC selon le régime, en fonction du chiffre d'affaires, réforme par réforme.** Pour chaque état du droit établi dans `#sec-irpp-forfait` (1990, 1993, 1999, 2006, 2011, 2014, 2016, 2018, 2023, 2026), l'impôt rapporté au chiffre d'affaires : régime forfaitaire (grilles de l'annexe II, puis taux, planchers et montants fixes), régime forfaitaire optionnel de 2026, et régime réel (barème de l'IRPP et minimum d'impôt, sous une hypothèse de taux de bénéfice à expliciter — la LF 2026 en fixe une, au plus 25 %, pour l'option). Chiffres d'affaires **déflatés** par l'indice des prix à la consommation de l'INS, base la plus récente disponible (série dans tunisia-data, provenance à documenter taux par taux). Vue d'évolution par onglets ou petits multiples, une courbe par régime. Données : `figtools.series()` depuis un générateur hors build ; tant que les paramètres du forfait ne sont pas en amont (openfisca-tunisia#476), engendrer depuis les valeurs sourcées de la note `docs/notes/fiscalite-regime-forfaitaire.md` avec un TODO.

- **Fiscalité locale : aucune entrée à ce jour (demande de l'humain, 4 octobre 2026). Option B retenue le 4 octobre 2026 : un volume VII « Les finances locales » (fiscalité locale, transferts, budgets) ; plan : `docs/notes/fiscalite-locale-plan.md`. TIB, TNB, TCL et taxes du code rédigées dans ce volume le 4 octobre 2026 (voir « Les finances locales » ci-dessous).** Le volume ne traite que des impôts d'État. Il manque un chapitre — ou un volume — sur la fiscalité locale : taxe sur les immeubles bâtis (TIB), taxe sur les terrains non bâtis (TNB), taxe sur les établissements à caractère industriel, commercial ou professionnel (TCL), et leurs textes (code de la fiscalité locale et ses modifications, à relever au JORT). Matière déjà collectée : documents de la réforme fiscale 2013-2014 (`tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`, fiche `sources/minfinances-reforme-fiscale-2013-2014.md`) — synthèse du groupe « fiscalité locale » (CNF août 2013, `2013-08_cnf_rf_5_ar.pdf` : TCL 111 / 93 / 137 MD et TIB 40 / 21 / 30 MD en 2010-2012), présentation de novembre 2013, journée de réflexion d'octobre 2014 sur la décentralisation ; inventaire page par page dans `docs/notes/reforme-fiscale-2013-2014-inventaire.md`. À cadrer : périmètre (impôts des collectivités locales seulement, ou aussi taxes affectées), place dans le précis, lien avec l'impôt foncier de 2014 (chapitre de l'impôt sur la fortune). Doctrine : six textes de B. Dafflon et G. Gilbert (Revue tunisienne de fiscalité, n° 20, 24, 25, 27 ; mélanges *Transparence et droit*, 2021) — deux en accès libre, quatre à obtenir en bibliothèque ou au Centre d'études fiscales de Sfax ; synthèse de référence : Dafflon et Gilbert, *L'économie politique et institutionnelle de la décentralisation en Tunisie*, AFD, 2018 (HAL, CC BY-NC-ND) ; rapports PARD 2021-2022. Inventaire, statut d'accès et ébauches CSL : `docs/notes/biblio-fiscalite-locale.md` ; copies locales hors dépôt : `~/Documents/biblio-precis/fiscalite-locale/`.

- **Présentation (`index.qmd`) : impôts directs et indirects définis et sourcés** (LOB 1967, 1996, 2019 ; tableaux A des LF 2014 et 2021 ; support ENA de S. Zakraoui), textes lus dans le corpus. Reste : relever la page de fin des trois LOB dans l'édition arabe ; dater le support ENA ou lui substituer la doctrine imprimée (`baccouche2008`, `ayadi1996`, à obtenir) ; l'arrêté de nomenclature des recettes (LOB 2019, art. 16) n'est pas identifié.

**Immédiat, avec les sources déjà présentes.** Les décrets n° 97-1368 et 2015-1768
(`PDFs/JORT/1997/fr/Jo05997.pdf` et `2015/fr/Jo0922015.pdf`) ont une couche texte : relever
leurs articles, tarifs et clauses d'effet pour le chapitre des droits de consommation.
L'extrait français `PDFs/Lois_de_Finances/Loi_de_Finances_2016.pdf` porte les articles
utilisés de la LF 2016 ; le JORT français n° 128 de 2020 (LF 2021) est aussi au corpus
et a été lu pour l'IRPP. **Ces deux lois ne sont donc plus des textes « absents »** ; ne
pas confondre l'absence en ligne du fascicule français de 2015 avec celle de son extrait
français conservé localement.

**OCR ciblé.** Le texte initial de la TVA au JORT n° 39 de 1988 (`Jo03988.pdf`) est un scan
présent localement : vérifier ses annexes sur l'image après OCR. Le code fiscal du JORT n° 1 de
1990 a été océrisé le 4 octobre 2026 ; ses annexes II et III (forfait) sont relues à l'image
(`docs/notes/fiscalite-regime-forfaitaire.md`).

**TVA — déduction, crédit et suspension (`_tva.qmd`, `@sec-tva-deduction`, rédigé le
6 octobre 2026)** d'après `docs/notes/fiscalite-tva-deductions-documentation.md`. Restent
ouverts, avec l'état des sources :

- **séries budgétaires après 2014 et avant 2010** (stock de crédit, restitutions, retenue à
  la source) : les rapports annuels de la DGI de 2013 et 2014 sont dans `tunisia-data` mais
  leur texte arabe n'est pas exploitable par recherche — **à lire à l'image**, puis chercher
  les millésimes suivants ; lois de règlement, rapports de la Cour des comptes et rapports
  annuels de performance de la mission Finances **non examinés**. Les séries connues
  (2009-2014) sont versées dans `tunisia-data` (`tva-credit-restitutions-sources`) et tracées
  par `@fig-tva-credit-restitutions`, toutes sources côte à côte ; quand la série sera prolongée, élargir les
  axes des vues (bornes fixées dans `figures/tva.py`) et la légende « 2009-2014 » ;
- **dates d'effet à relire au fascicule** : lois de finances pour 1991, 1992, 1993 et 1994
  (art. 50, 66, 68, 114, 31-32 : scans locaux, à relire à l'image — seule la mensualisation
  de 1994 est écrite au chapitre, sans date ni citation littérale), loi n° 2007-69 (art. 10
  et 11 : article final à lire, JORT n° 104 de 2007, présent sur pist.tn), loi de finances
  complémentaire pour 2014 (art. 27) ;
- **délai de visa de la restitution entre 1998 et 2001** : l'art. 41 de la LF 1998 récrit
  l'alinéa sans délai, le CDPF ne fixe 90 et 30 jours qu'au 1^er^ janvier 2002 ; droit
  applicable dans l'intervalle non établi (note commune n° 11/1999 à obtenir) ;
- **relèvement de la limite de 20 % antérieur à 1996** : le mot « également » de l'art. 41 de
  la LF 1996 le suggère ; le chapitre n'en dit rien, la fiche
  `r-tva-limite-restitution-avant-1996` proposée au § 7 de la note n'est donc pas versée ;
- **relevés sur le seul code consolidé, non écrits au chapitre** : exclusions de l'art. 10-4
  (LF 2017, art. 34), dons (LF 2004, art. 57), art. 19 *quinquies* (LF 2023, art. 46),
  déductions de stock sans restitution (LF 2019 et 2022), origine de l'art. 13 *quater* ;
  à lire au JORT avant de les écrire ;
- **clés CSL manquantes** : rapport de synthèse du Conseil national de la fiscalité
  (novembre 2013) et projet des Assises (novembre 2014), source de la valeur de 298,9 MD
  pour la retenue de 2012 ; rapports sur le projet de budget de l'État pour 2013 et 2014 ;
- **`docs/notes/fiscalite-tva-reformes.md`, ligne LF 2022, art. 52, à corriger** : la fin du
  régime suspensif vaut pour les sociétés de commerce international et les entreprises de
  services **totalement exportatrices comprises** (JORT n° 119 du 28 décembre 2021,
  p. 3097) ; le chapitre est corrigé ;
- **mesure du rapport sur le budget 2025** (restitution du crédit des commerçants sur leurs
  stocks) absente de la loi n° 2024-48 : ni la mesure ni son rendement ne sont écrits.

Les réformes de 1988 à 2026 sont rédigées d'après `docs/notes/fiscalite-tva-reformes.md` ;
son § 8 énumère ce qui reste non établi, et qui n'est donc pas écrit au chapitre : date
d'effet des lois de finances pour 1989 à 1993 (lues à l'image, muettes sur une date
spéciale), tableaux annexés « L », « M », « M bis », « P » et annexe 5 de la LF 2016 (non lus ;
leur présence et leur lisibilité au corpus restent à vérifier fascicule par fascicule), articles 23 à 26 de la LF 1989 (OCR en colonnes entrelacées, à relire à
l'image), décret n° 97-1339 du 14 juillet 1997 (à obtenir : absent de `jort_cache`), et les
144 décrets de l'article 8 signés de 1988 à 1997, connus par leur seul intitulé. La fiche
`r-tva-mise-en-application-post-1989` reste ouverte.

**TVA — dates d'effet et objets des lois (7 octobre 2026)**, d'après
`docs/notes/fiscalite-tva-objets-des-reformes.md`. Écrit au chapitre : les rubriques sous
lesquelles les lois rangent leurs articles de TVA ; l'absence d'article final de date
d'application dans les lois de finances pour 1990, 1991 et 1993 ; la clause générale de la loi
de finances pour 1994 (art. 77), citée dans l'encadré des dates ; le rectificatif du 4 mai 1993
(art. 102), au registre des forfaits ; pour 2023, « certaines professions non commerciales »
au lieu de « les professions libérales » (le décret-loi abroge un tiret de l'article 7 sans
écrire de taux ; les professions de santé restent à 7 %) ; le paragraphe 1 de l'art. 27 de la
loi de finances pour 2021 (dons, art. 9), au registre de la déduction. Restent : la date
d'effet de la mensualisation de 1994 (art. 31 et 32), non écrite tant que l'absence de clause
propre n'est pas confirmée à l'image ; l'édition française du décret-loi n° 2022-79, absente ;
le texte qui a modifié l'art. 10 de la loi de finances pour 2017.

**TVA — régimes par catégorie et tableaux annexés (7 octobre 2026, non commité).** D'après
`docs/notes/fiscalite-tva-tableaux-produits.md` (§ 1 à 3, 8 et 9) et
`docs/notes/fiscalite-tva-codes-consolides.md`. Fait :

- **série** `precis/_seriescache/tva-regimes-par-categorie.csv` : les 173 lignes du § 9.3 de la
  note, versées telles quelles (25 catégories, 5 dates repères) ; provenance déclarée dans
  `figures/tva.py` ;
- **figure** `@fig-tva-regimes` (matrice catégories × dates, une couleur par régime, cases
  partagées, hachures pour les taux que la loi n'écrit pas, cercle pour les éditions privées) et
  **section** `#sec-tva-regimes-categories`, dans le bilan des taux, avec son registre replié
  (`tbl-tva-regimes-textes`, 20 lignes, ancres `r-tva-cat-…`) ;
- **annexe du volume** `precis/fr/fiscalite/_tva_tableaux.qmd` (`#sec-tva-tableaux`,
  `.domicile-unique`) : texte principal sur les quatre tableaux, le sort du tableau C, les
  entrées et sorties, la nature des sources ; registre des textes (`tbl-tva-tableaux-textes`,
  ancres `r-tva-tab-…`) ; onze blocs repliés de transcription — tableaux A, B et C de 1988,
  tableau C à la fin de 2006 et ses retraits, origine des numéros d'après l'édition privée de
  2014, tableaux A, B et B bis nouveaux (2016, 2017, 2026), article 7 numéro 3, loi de finances
  pour 2026 ;
- `#sec-tva-etat-du-droit` renvoie à l'annexe au lieu de dire le tableau A « non donné ».

Reste :

- **annexe à déclarer côté arabe** : `_tva_tableaux.qmd` est dans les `appendices` du
  `_quarto.yml` français seulement ; à ajouter au `_quarto.yml` arabe une fois la traduction
  livrée (traduction différée : 24 000 mots, dont 23 000 de transcription) ; les attributs
  `titre` des blocs sont à traduire ;
- **termes arabes posés dans `figures/tva.py`**, hors glossaire, à faire valider par le
  terminologue : « معفى » (exonéré, dans les cases), libellés des douze groupes et des
  vingt-cinq catégories, « طبعة خاصة للمجلة » (édition privée du code), « الطبعة الرسمية
  للمجلة », « صنف غير وارد بالجداول », « القاعدة العامة للفصل 7 » ; la colonne « Numéros » des
  données reste en français dans le livre arabe (« bis », « tiret », « positions des
  chapitres ») ;
- **registre complet numéro par numéro, loi par loi, de 1989 à 2015** : non fait (note, § 6.2) ;
  l'annexe ne donne, pour les anciens tableaux, que l'état de 1988 et l'origine des numéros
  d'après l'édition privée de 2014 ; les éditions privées de 2008 et de 2014 ne sont pas
  transcrites numéro par numéro ;
- **colonnes intermédiaires de la matrice** : pas d'état vers 1995 ni vers 2002 (aucun état
  daté n'est disponible ; les pages Jurisite mêlent des dates) ; colonnes de 2008 et de 2014 à
  rapprocher du Journal officiel ;
- **lois non relues**, citées seulement « d'après l'édition » : n° 2002-103 (voitures de
  4 chevaux), n° 2006-71, n° 99-70, n° 2009-32, n° 2007-69 ; articles des lois de finances pour
  2019, 2020, 2021 et 2023 connus par les seules notes de l'édition du code ; textes présents
  au corpus pour la plupart ;
- **passages au taux normal de 2017 à confirmer** : numéros du tableau B bis non repris
  (services informatiques, certification électronique, formation, Internet fixe, restauration
  ordinaire, véhicules électriques, sevrage tabagique) — note commune d'application à
  obtenir (note, § 9.5) ; `TODO (documentaliste)` dans la section et dans l'annexe ;
- **tableau C** : retraits du café, du thé, des bières, des vins, des tabacs, des voitures et
  des armes non établis (tableaux « L » et « M » de la loi de finances pour 1992, lois de
  finances pour 1993 et 1994, art. 71 de la loi de finances pour 2005 : fascicules scannés au
  corpus, OCR à faire ; note, § 8.6) ; la transcription de 1988 compte 240 positions là où la
  note en annonce « un peu plus de 210 » : l'annexe écrit « plus de deux cents », écart à
  lever par la relecture des codes tarifaires ;
- **essence et gaz naturel distribué, eau potable après 1991** : régime non établi (note,
  § 9.2, précisions 2 à 4) ;
- **versement des listes en amont** dans `openfisca-tunisia` (note, annexe C : structure
  proposée) : rien n'est versé ; la série du précis est un CSV fait de la note, non un
  snapshot de paramètres ;
- **anciens biens du tableau C dans la matrice** (arbitrage du 7 octobre 2026) : six lignes
  « taux normal, déduit » ajoutées à la série et au § 9.3 de la note (2014, 2017, 2026 pour les
  denrées et pour les biens durables) : 173 lignes, dont 18 au taux que la loi n'écrit pas ;
  5 cases blanches au lieu de 10 ; les lignes de l'hôtellerie et de l'enseignement du tableau
  des trajectoires sont complétées jusqu'à 2018 par des liens vers le registre des régimes.

**Paramètres dans le temps (7 octobre 2026).** Deux composants communs, à partir d'une même
déclaration de paramètres (`ot.ParametreDate`) dans un générateur : le tableau de **l'état du
droit à des dates repères** (`ot.ecrire_dates_reperes` → `tables/<nom>_dates_reperes.md`) et la
**figure en escalier** (`figtools.figure_escalier`, sur la série longue
`_seriescache/<nom>.csv` qu'écrit `ot.ecrire_serie_parametres`), avec une lecture en dinars
constants pour les montants (indice `ipc-longue-periode`, jusqu'en 2023). Appliqués au volume
fiscal : la figure des taux de la TVA passe par le composant, image inchangée, et son tableau
aux dates repères est engendré (`tva_taux_dates_reperes.md`) mais **pas encore inséré** dans
`_tva.qmd`, en réécriture sur une autre branche ; les déductions pour charges de famille de
l'impôt sur le revenu ont les deux (`@tbl-charges-famille-reperes`,
`@fig-irpp-deductions-famille`). Restent :

- **insérer** `tva_taux_dates_reperes.md` dans `_tva.qmd` quand sa réécriture est fusionnée ;
- **droits de consommation** : le tarif pétrolier n'a reçu ni l'un ni l'autre. Sa série de
  1988, 1991 et 1999 a des trous que le chapitre connaît — décret n° 94-816, date d'effet non
  établie ; décret n° 98-952, au 6 mai 1998 ; changements postérieurs à 1999, non datés — :
  une marche ou une case y affirmerait une valeur en vigueur qui ne l'est pas. Textes
  présents au corpus pour 94-816 (`Jo03094`) et 98-952 (`Jo03598`), à relever ; constat
  consigné dans `backlog-modele.md` ;
- **étendre aux autres volumes** : cotisations (taux par régime), prestations (allocations,
  plafonds), retraites (âges, taux, planchers), marché du travail — `ParametreDate.serie()`
  lit aussi les barèmes à une tranche ;
- **atlas par volume** : une page qui réunit, pour un volume, l'état de tous ses paramètres
  aux mêmes dates repères ;
- **TVA, tableaux A, B, B bis et C** : à verser en amont comme listes datées d'opérations,
  pour que le périmètre de chaque taux se lise dans le temps comme son niveau ;
- **paramètres écartés d'office** : ceux qui disent une suppression par 0 et non par une
  valeur nulle (déduction supplémentaire des salariés au SMIG, 2014), qui traceraient une
  marche à zéro ; ceux dont un plafond absent vaut l'infini (frais professionnels avant
  2017), à rendre par un format propre ;
- **bibliographie** : `bct-ra` et `ins-annuaire`, sources de l'indice des prix, sont copiés à
  la main dans `fiscalite/references.json` (FR et AR) depuis le volume « marché du travail » ;
  rangement Zotero à faire par le bibliographe ;
- **provenance de l'indice des prix** : l'entrée `ipc-longue-periode` de
  `_seriescache/catalog.snapshot.yml` s'intitule encore « 1962-2003 » et renvoie, au-delà de
  2003, à `bct-ipc-base2015`, alors que la série va jusqu'à 2023 (annuaire 2019-2023) ;
  l'onglet « Sources » des figures en dinars constants — ici et au volume « marché du
  travail » — affiche donc un titre périmé. À corriger dans le catalogue de `tunisia-data`,
  puis à resnapshoter ;
- **arabe** : « رئيس العائلة » (chef de famille) est posé d'après l'article 40 du code, sans
  entrée au glossaire ; le chapitre arabe de l'impôt sur le revenu recevra le tableau et la
  figure à la prochaine synchronisation de traduction.

**TVA — taux dans le temps (7 octobre 2026).** Le tableau des générations de taux
(`@tbl-tva-taux`) n'est plus fait main : `scripts/generate_bareme_tables.py` l'engendre
(`tables/tva_taux.md`), avec la série `precis/_seriescache/tva-taux.csv` que trace
`@fig-tva-taux` — openfisca-tunisia 0.121, borne relevée. Les six lignes concordent, valeur
par valeur, avec le tableau remplacé ; sa colonne « Changement juridique » est devenue la
liste qui suit le tableau, citations comprises. Restent :

- **terme arabe du taux intermédiaire** : `precis/glossaire.yml` n'a pas d'entrée pour ce
  taux, que le code ne désigne que par sa valeur ; le tableau et la figure arabes portent
  « النسبة الوسيطة », posé par le générateur et à valider par le terminologue (les trois
  autres en-têtes sont ceux du glossaire) ;
- **titres des textes en français dans l'onglet « Données » du livre arabe** : la série
  porte le titre que la source donne à chaque texte, en français seulement ;
- **périmètre de chaque taux** : ni le tableau ni la figure ne disent quelles opérations
  relèvent de chaque taux ; les trajectoires par opération restent en prose
  (« Des trajectoires différentes selon les opérations »).

- **Impôt sur la fortune (`_impot_fortune.qmd`, chapitre ouvert le 4 octobre 2026)** sur la
  note `docs/notes/fiscalite-impot-fortune.md`. Textes lus : LF 2014 art. 55 et LFC 2014
  art. 38 (fascicules FR et AR locaux, lisibles) ; DL 2022-79 art. 23 et 76 (édition arabe
  locale, édition française par le fac-similé DGI) ; loi n° 2025-17 art. 88 et 110 (édition
  arabe seule, traduite par le précis) ; notes communes n° 15/2023 (scan, océrisée et relue à
  l'image) et n° 13/2026 (couche texte inutilisable, relue à l'image). Restent :
  - **AR** : déclarer `_impot_fortune.qmd` dans `precis/ar/fiscalite/_quarto.yml` (ligne
    commentée en place, après `_impot_societes.qmd`) dès que la traduction est livrée ;
  - **rendement** : aucune série publiée (fiche `r-impot-fortune-rendement`) ; lois de
    règlement 2023-2024 et publications de la DGI à consulter ;
  - **modèle de déclaration 2026** : à obtenir (la NC 13/2026 n'a pas d'annexe) ;
  - **modificatifs et textes d'application** : JORT postérieurs au n° 93 de 2026 et n° 58
    de 2026 à lire (fiche `r-impot-fortune-modificatifs`) ;
  - **antécédents** avant 2014 (époque beylicale et coloniale, 1956-2013) non explorés ;
  - **glossaire** : `fonds-de-commerce` reste provisoire, terme français à confirmer dans un
    texte bilingue du JORT ;
  - **contradiction à trancher (retraites)** : `retraites/_secteur_public.qmd` dit que le
    DL 2022-79 n'a été publié qu'en arabe ; le fac-similé DGI de l'édition française du JORT
    n° 141/2022 porte pourtant son art. 12 (p. 3557). Non corrigé ici (autre livre) ;
  - **genèse parlementaire** de l'art. 88 (rejet en commission, suppression puis
    réintroduction en plénière) : presse seulement, hors du corps faute de pièce de l'ARP
    ou du CNRD.
- **Dépenses fiscales et régimes d'incitation (`_depenses_fiscales.qmd`, chapitre créé le
  6 octobre 2026, repris le même jour après relecture)** sur la note
  `docs/notes/fiscalite-depenses-fiscales.md`, seule matière du chapitre (§ 10 pour la
  reprise). Écrit : code de 1969, loi n° 72-38 décrite en entier et ce en quoi elle rompt,
  loi n° 74-74 ; code de 1993 (objet, abrogations, plan par objectif, art. 7, 9, 10, 12, 14,
  16, 20, 22, 23, 25, 30) ; imposition de l'exportation votée en 2006 et ses quatre reports ;
  lois n° 2016-71 et n° 2017-8 ; abrogation du régime de l'exportation (LF 2019) ; coût et
  bénéficiaires en deux blocs séparés — évaluations du ministère des Finances (méthode du
  rapport PLF 2021, agrégats 2019-2023, par impôt, bénéficiaires, avantages financiers) et
  études extérieures (Banque mondiale 2014, diaporama de septembre 2014, OCDE 2013,
  estimations antérieures), chacune avec sa méthode. Disponibilités ci-dessous contrôlées le
  6 octobre 2026 (présence du fichier, `pdftotext` sur le fascicule entier) ; la page de
  l'article n'a pas été ouverte. Restent :
  - **AR** : déclarer `_depenses_fiscales.qmd` dans `precis/ar/fiscalite/_quarto.yml`
    (ligne commentée en place, après `_droits_consommation.qmd`) dès que la traduction est
    livrée ;
  - **clés à verser (bibliographe)** : loi n° 69-35 (JORT n° 24 de 1969, p. 766-769) et loi
    n° 74-74 (JORT n° 51 de 1974, p. 1744-1746), citées en clair au chapitre faute de clé ;
    ébauches au § 10.1 e de la note ;
  - **loi n° 72-38** : date d'entrée en vigueur (aucune clause) et texte qui l'a abrogée non
    établis ; motifs, nombre d'entreprises agréées, effets sur l'emploi et l'exportation :
    aucune source, rien n'est écrit ;
  - **textes de 1976 à 1992 — OCR** : taux, durées et dates d'effet non établis, seuls les
    intitulés sont connus ; la chaîne 1974 → 1981 → 1987 → 1993 du régime du marché intérieur
    n'est pas établie. Fascicules français présents au corpus, couche texte vide :
    `1976/fr/Jo04676.pdf` (n° 76-63), `1981/fr/Jo04481.pdf` (n° 81-56),
    `1982/fr/Jo05482.pdf` (n° 82-67), `1985/fr/Jo07385.pdf` (décret-loi n° 85-14),
    `1987/fr/Jo05687.pdf` (n° 87-51), `1988/fr/Jo02388.pdf` (n° 88-18),
    `1990/fr/Jo02190.pdf` (n° 90-21), `1992/fr/Jo05292.pdf` (n° 92-81). Priorité : 1985 et
    1987 (sort de la loi de 1972). Cinq n'ont pas de clé CSL ;
  - **code de 1993 — OCR** : `1993/fr/Jo09993.pdf` présent, couche texte vide ; pas de
    clause générale d'entrée en vigueur : date du dépôt du JORT n° 99 à établir ; intitulés
    des titres VII à X et nombre d'articles à contrôler sur la page (p. 2179-2181) ; terme
    de la déduction de 50 % des exportateurs entre 1993 et 2006 non établi ;
  - **méthode des rapports PLF 2022 à 2025** : non établie (introduction et table des
    matières seules) ; données employées par le ministère non décrites dans le rapport 2021 ;
  - **crédits budgétaires** des primes et des prises en charge de cotisations : non relevés
    (fonds spéciaux du Trésor, budgets par mission, lois de règlement, comptes du Fonds
    tunisien de l'investissement — à obtenir) ; le chapitre ne publie que les paiements
    déclarés du rapport PLF 2021 ;
  - **mentions dans les chapitres d'impôt (6 octobre 2026)** : chaque avantage établi par un
    texte est signalé, avec renvoi à `@sec-depenses-fiscales`, dans `_impot_societes.qmd`
    (paramètres d'origine, « 2017 », « 2019 », rendement), `_impot_revenu.qmd` (BIC,
    catégorie III, déductions, rendement), `_tva.qmd` (régime suspensif, rendement) et
    `_droits_consommation.qmd` (renvoi à l'art. 13 *ter*, rendement). **Non mentionnés,
    faute de texte établi** — à lire avant d'écrire quoi que ce soit dans ces chapitres :
    régime des Tunisiens résidents à l'étranger (premier poste du recensement ; le rapport
    cite la LF 1975, art. 33) ; concessionnaires automobiles (droit de consommation,
    position 87-03) ; exonérations de TVA et de douane des médicaments, engrais et produits
    alimentaires ; avantages au titre du réinvestissement après 2017 (art. 72 à 77 du code
    de l'IRPP et de l'IS) ; sociétés d'investissement à capital risque. Les droits de douane
    n'ont pas de chapitre : leurs exonérations (loi n° 2017-8, art. 4) restent dans
    `_depenses_fiscales.qmd`. Dans `_impot_revenu.qmd`, la série du § V de l'art. 39 reste
    non établie pour les activités qu'il vise depuis 2017 ; l'état de la LF 2019, art. 15
    (« moitié des revenus » des activités à 13,5 %) n'est pas repris ;
  - **études extérieures** (PDF collectés le 6 octobre 2026 dans `tunisia-data`, lisibles,
    contenu non relevé) : annexe 4.2 du volume d'annexes de la Banque mondiale (p. 35) —
    taille de l'échantillon et libellé des questions de l'enquête ; étude de Ghazouani
    (2011) — citée de première main depuis le 6 octobre 2026 (pp. 3-9 lues, tableau 1 repris) ;
    restent sa figure 2 (coût en MD par année), ses annexes et la cause des creux de 2004-2005
    (clé à verser). L'étude IFC-ECOPA de novembre 2012 est un rapport préliminaire non
    publié : à obtenir ;
  - **calendrier de 2014 — lisible** : LF 2015 (loi n° 2014-59), art. 18, « mesures de
    soutien des entreprises totalement exportatrices », `2014/fr/Jo1052014.pdf` ; à ouvrir
    pour confirmer qu'aucun texte n'a touché à l'échéance du 1er janvier 2014. LF 2014,
    art. 49-50 et 54 (`2013/fr/`, JORT n° 105) : connus par leur intitulé, non repris ;
  - **zones de développement régional — lisible** : décret gouvernemental n° 2017-389,
    `2017/fr/Jo0252017.pdf` ; loi n° 2019-47, `2019/fr/Jo0472019.pdf` (portée fiscale non
    établie) ;
  - **rapports annexés aux PLF 2022 et 2023 — à obtenir** : non archivés dans
    `tunisia-data` (`data/raw/gbo/` ne porte que les rapports 2021, 2024 et 2025) ; adresses
    sur gbo.tn dans la note, § 2.2, relevées le 5 octobre 2026 et non recontrôlées. Seule
    leur introduction (p. 7) est connue. Rapport annexé au PLF 2026 : non cherché.
    Existence d'un rapport pour les PLF 2019 et 2020 : non établie ;
  - **série du coût à reconstruire, avec sa rupture de périmètre** : les rapports 2024 et
    2025 excluent les exonérations des médicaments et des engrais, que le rapport 2021
    compte (274,5 et 249,9 MD en 2019). Les deux CSV traités de `tunisia-data` cousent trois
    rapports sur cinq et portent cette rupture à la couture 2019/2020 ; le périmètre des
    rapports 2022 et 2023 reste à lire. `figures/depenses_fiscales.py` n'est donc pas appelé
    (docstring corrigé le 6 octobre 2026, code inchangé) et aucune figure n'est publiée.
    La fiche `~/projets/tunisia-data/sources/gbo-depenses-fiscales.md` ne mentionne pas
    cette exclusion : à corriger dans ce dépôt-là ;
  - **écart sur l'exercice 2021** : 7 745 MD (rapport 2023) contre 5 871,5 et 5 872,3 MD
    (rapports 2024 et 2025) ; cause non établie, à lire dans les rapports 2023 et 2024. Les
    deux ratios du rapport 2021 pour 2019 (16,3 % et 19,15 % des ressources fiscales) sont
    signalés au chapitre ; le dénominateur de l'introduction reste à établir ;
  - **à vérifier sur les rapports** : décomptes de dispositifs valorisés par impôt (37/57 ;
    34/63, rapport 2025) et sommes par impôt de 2020 et 2021, tenus de la série traitée ; répartition par
    impôt 2020-2023 et par secteur 2017-2019 (tableau n° 6 du rapport 2021, relevé pour 2019
    seulement) non publiées ; ventilation par gouvernorat et délégation (loi n° 2017-8,
    art. 18) : présence dans les rapports non vérifiée ;
  - **avant 2017** : aucune série homogène. Retirés du chapitre : l'estimation OMC 2000
    rapportée par la Banque mondiale (note 10 du ch. 4), non retrouvée dans la notification
    G/SCM/N/71/TUN : à rapprocher de sa section IX (pp. 14-15) ; l'estimation du FMI pour
    2005 (deux rapports d'assistance technique non publiés) ; une seconde estimation attribuée à
    Ghazouani par la même note, absente de son étude. Figures 4.1 et 4.4 du rapport de la Banque mondiale à
    relever sur l'image ;
  - **à croiser avec « Cotisations sociales »** : coût des prises en charge de cotisations
    patronales (code de 1993, art. 25 ; loi n° 99-59, connue par son intitulé).
- **Forme de `_impot_revenu.qmd` : rien à reprendre.** Ses titres ont été remontés d'un cran
  et il a reçu sa section « La longue période ». La réorganisation par réforme, un temps
  envisagée, a été écartée après lecture — voir « Forme des chapitres » plus bas, qui en
  consigne le motif et la leçon.
- **IRPP** : le minimum d'impôt de l'article 44 § II et le régime forfaitaire sont écrits.
  Le régime forfaitaire (`#sec-irpp-forfait`) couvre depuis le 4 octobre 2026 toute la
  chronologie 1990-2026, chaque modificatif lu au JORT (note
  `docs/notes/fiscalite-regime-forfaitaire.md`). Y restent : la **longue période** au-delà de 2013 —
  `tbl-forfait-effectifs` ne couvre que 2004 et 2009-2013, d'après le diaporama du ministère des
  Finances d'août 2013 (`minfin-cnf-2013-forfait`, lu à l'image) ; les autres chiffres de la
  collection `tunisia-data` (tranches de chiffre d'affaires, secteurs, comparaison avec le réel)
  sont lisibles mais non encore relus ; la **relecture
  arabophone** de l'article 91 de la LF 2026 (lu à l'image, édition arabe seule parue)  ; le **numéro** de la note commune sur l'article 16
  de la LF 2018 ; les **tableaux faits main** `tbl-irpp-forfait` et `tbl-forfait-annexe-2`, à
  engendrer quand les paramètres seront sourcés. Textes tous lisibles au corpus local
  (fascicules de 1990 à 1993 océrisés, ceux de 1999 et 2001 décodés) ; la LF 2016 et la LF 2020
  se citent en pagination française d'après les extraits locaux, la LF 2023 et la LF 2026 en
  pagination arabe.
  Restent les tarifs antérieurs de la contribution personnelle d'État, les barèmes
  régionaux de l'évaluation forfaitaire agricole, le plafond de l'assurance-vie entre
  ses deux bornes connues et la contribution au budget de l'État. L'article 16 de la
  loi de finances pour 2019 pose encore un problème de lecture des éditions.
- **Séries à construire** : le seuil de la tranche à 0 %, rapporté au SMIG et à l'indice des
  prix, 1990-2026 ; les déductions pour charges de famille rapportées au SMIG — leur lecture
  à l'indice des prix est faite (`@fig-irpp-deductions-famille`, 7 octobre 2026) ; les tarifs
  successifs de la contribution des patentes ; le plafond de déduction des primes
  d'assurance-vie.
- **Lectures externes ou sous autre édition** : notes communes de la DGI sur la réforme
  de 2025 ; articles 56 et 91 de la LF 2026 lus en arabe, à confirmer sur une édition
  française effectivement disponible. Le fichier local « français » du JORT n° 148 de
  2025 sert en réalité l'arabe ; ne pas le citer comme français.
- **Ton** : exposer en regard au moins deux lectures attribuées de la dérive du barème.
- **Reste du côté du glossaire** : un seul arbitrage, entre « revenu annuel net » (au
  glossaire) et « revenu net global » (proposé par la note documentaire sur l'article 8,
  alinéa 1er) — une notion ou deux ? Les vingt autres notions que la consigne réclamait
  existent, et l'annexe est déclarée dans les `_quarto.yml` des deux langues.
- **Bibliographie** : les lois n° 2001-123 (LF 2002) et n° 2007-70 (LF 2008) ont déjà
  leurs clés CSL ; leur mention sans citation dans l'annexe de l'IRPP est à rattacher à
  ces clés, pas à recréer. Voir `biblio-a-rapatrier.md` avant toute écriture Zotero.

- **Tableaux de paramètres engendrés (recension du 2 octobre, lots 1f à 1h) — fait le
  3 octobre 2026** : synthèse des générations du barème (`tbl-bareme-irpp-generations`),
  colonnes neuves des charges de famille (`tbl-charges-famille`), taux et minimum de l'IS
  (`tbl-is-taux`, `tbl-is-minimum`), tarifs pétroliers et tarif spécifique de 1988
  (`tbl-dc-petroliers`, `tbl-dc-specifiques-1988`). Les relevés CSV de `tarifs/` restent la
  source des cases que les paramètres ne portent pas (minimum de 1990-2005, état consolidé de
  2023, alcools) et servent de garde-fou. À faire : la terminologie arabe des noms de produits
  pétroliers (terminologue), que l'instantané arabe laisse en français, comme le faisait
  déjà le livre arabe.

## Retraites

- **Taux d'équilibre et figures du RSNA prolongés à 2018 (5 octobre 2026).**
  L'annuaire CNSS 2018 français transmis par l'utilisateur est lisible dans sa
  couche texte (PDF 16, 43-44) : salaires et pensions de 2018 ajoutés à la série
  dérivée de `tunisia-data`, puis aux figures du taux, de sa décomposition,
  du salaire moyen et de la pension moyenne. Les années 2000-2017 gardent
  leurs valeurs et leur provenance de l'édition 2017. **Écart à élucider
  auprès de la CNSS** : 1 289 940 actifs, note « y compris les non assujettis »
  (PDF 43-44), contre 1 289 940 salariés + 950 non-assujettis (PDF 16).
  Les facteurs démographique et de remplacement retiennent les actifs imprimés
  avec une réserve visible ; le taux pensions ÷ masse salariale n'en dépend pas.
  Au-delà de 2018, les annuaires sont à obtenir ; support non présent dans le
  corpus local exploité. Fiche : `tunisia-data/sources/cnss-annuaires.md`.
- **Résultat de la branche des pensions du RSNA, 1990-2004 — fait le 3 octobre 2026** (`#fig-rsna-resultat-1990-2004`, dans `#sec-rsna-equilibre`), tiré de la rétrospective financière 1990-2004 de la CNSS (`cnss-retrospective-1990-2004`, exemplaire papier numérisé ; série `cnss-retrospective-ressources-emplois` snapshotée le 3 octobre 2026). Le tableau de cette branche n'a pas d'estimation (la colonne 2000 y est rétablie par les totaux) ; si une relecture de l'original change ses montants, relire la note de lecture. Piste : le même tableau existe pour les autres régimes (RSA, RSAA, RTNS) et pour le régime complémentaire. Depuis le 3 octobre 2026, la figure a trois vues : millions de dinars, % du PIB (PIB du ministère des Finances, série `irpp-ratios`, rupture de base des comptes nationaux marquée en 1997, non corrigée) et % du total des ressources de la CNSS (tableau de l'ensemble, page 78, toutes branches).
- **Réallocations du taux global sur la figure du résultat RSNA — fait le 3 octobre 2026** (`#fig-rsna-resultat-1990-2004`) : trois lignes aux 1er janvier 1988, 1994 et 2003 (décrets n° 88-1137, 94-1429, 2003-1212), dates du précis, identiques à celles des notes du document (pp. 14, 15, 60) ; libellés en taux de la branche selon la caisse (5 → 8, 8 → 10, 11,5 → 12,5 %), quote-parts en vingtièmes dans la note de lecture. Texte lisible dans le corpus (décrets déjà lus pour `#sec-rsna-financement`). Reste : le même tableau pour les autres régimes (RSA, RSAA, RTNS) et le régime complémentaire.
- **Point clos sur la source primaire** : l'article 2 de la loi n° 2019-37 remplace
  60 par 62 ans aux § 2 et 3 de l'article 32, sans clause d'effet. Le JORT n° 35 a
  été déposé le 30 avril 2019 : loi n° 93-64, art. 2, délai de cinq jours **sans compter
  le dépôt** → **5 mai 2019**. L'article 5 ne reporte à juillet 2019 et janvier 2020
  que les âges de mise à la retraite qu'il énumère, pas l'article 32. Le chapitre et
  le glossaire distinguent désormais ces dates ; vérifier séparément la date portée
  en amont pour le repère du modèle avant de le modifier.
- **Lecture immédiate suivante** : loi n° 2009-39 et décret n° 2009-2085 sur le départ
  avant l'âge légal (`2009/fr/Jo0552009.pdf` et `Jo0562009.pdf`, textuels) ; exposer
  les conditions que le chapitre laisse encore de côté. Les rectificatifs du décret
  n° 82-1030 et de la loi n° 81-6 restent à relire sur les scans locaux après
  identification exacte des pages : un numéro peut avoir des homonymes.
- **Barème d'actualisation — coefficients relevés.** Les 31 arrêtés de 1994 à 2024
  et leurs **1 488 coefficients** ont été relevés et contrôlés, y compris les images des
  tableaux de 1997 et 2024 ; voir `_secteur_prive.qmd#sec-rsna-bareme`. Les questions
  encore ouvertes sont la **méthode de calcul** des coefficients, à chercher hors des
  arrêtés, et les barèmes 2025-2026 non identifiés (`docs/recherches.yml`).
- **Autres lectures** : série du SMAG journalier, articles propres du RACI et du RTTE,
  textes de départ anticipé du régime agricole. Le règlement complémentaire du
  18 novembre 1978 n'est plus « à lire » en bloc : les articles utiles ont été lus à
  l'image ou par OCR et figurent dans la note de `arrete-1978-11-18-retraite-complementaire`.
- **Travailleurs non salariés — fait.** Âge, stage, taux, plancher et versement unique sont
  lus sur le décret n° 95-1166, sa chaîne modificative entière avec eux. L'article 30 a changé
  de nature en 2002 : la revalorisation, d'abord suspendue à un arrêté, est devenue
  automatique.
- **Question ouverte, et la voie du *Journal officiel* y est ÉPUISÉE** : comment les pensions
  du régime non agricole ont été liquidées entre le 23 septembre 1990 et le 30 juin 1994.
  Vérifié le 20 septembre : aucun texte entre ces dates ne vise le décret n° 74-499 hors celui
  de 1994, lequel ne porte aucune clause de régularisation — sa seule rétroactivité vise la
  quote-part de cotisations. Restent les circulaires et rapports de la CNSS, l'avis non publié
  du Tribunal administratif, la doctrine et la jurisprudence ; aucun n'est au corpus local.
  **Cette question se résoudra hors du *Journal officiel*, ou pas du tout.**
- **Tableaux manuels : ne pas les regrouper en un seul chantier de régénération.** Le
  versement des paramètres de retraite du 20 septembre (PR #51 et #52 du dépôt de
  pensions historique) n'a rendu engendrable que le tableau des âges militaires ; les
  conditions des droits des survivants et des départs anticipés ne sont pas des valeurs
  datées. Les tableaux de revalorisation doivent suivre la date d'effet de la pension,
  et non celle du SMIG. Le repère de l'article 32 est daté sur la loi de 2019 et la
  date de dépôt du fascicule, sans assimiler cette date au calendrier de départ.

  | Tableau | Ce que le versement a changé |
  |---|---|
  | âges militaires | **engendré depuis le 20 septembre 2026.** Cinq grades, deux dates, tout est dans l'arbre |
  | survivants du RSNA | la branche existe, mais trois des six lignes sont des **règles** — remariage, plafond de cumul, cumul invalidité/survivant |
  | départs anticipés du RSNA | les durées et les taux sont versés ; les **conditions** de chaque cas ne sont pas des valeurs datées |
  | article 32 de la loi n° 85-12 | repère de 60 → 62 ans exécutoire le 5 mai 2019 ; les autres distinctions entre colonnes restent des règles |

  Les conditions d'âge, d'études et de ressources de la pension d'orphelin restent à la main.
- **Régimes spéciaux** : le décret-loi n° 2011-48 relève aussi la contribution de
  l'employeur pour les membres du gouvernement et les gouverneurs ; le chapitre ne le dit pas.

- **Tableaux de paramètres engendrés (recension du 2 octobre, lots 1a à 1c) — fait le
  3 octobre 2026** : trois tableaux faits main remplacés par des tableaux mixtes engendrés
  (`tbl-rsna-reference`, `tbl-rsna-survivants`, `tbl-rsa-evolution`) ; tableaux neufs pour
  l'invalidité du régime non agricole, le régime agricole amélioré, le régime complémentaire,
  les Tunisiens à l'étranger, les travailleurs à faibles revenus, les artistes, les départs
  anticipés et les droits dérivés de la CNRPS ; allocation de vieillesse ajoutée à
  `tbl-cnrps-plafond-plancher`, durée annuelle du SMAG à `tbl-rtns-agricole`. Restent faits
  main : `tbl-rsna-coeur`, `tbl-rsna-anticipes`, `tbl-rsna-ages-derogatoires`, les deux
  tableaux de revalorisation, `tbl-rsa-rsaa`, `tbl-rtns-coeur`, `tbl-comparaison-secteurs`,
  `tbl-cnrps-1959-1985`, `tbl-cnrps-jouissance`, `tbl-cnrps-bonifications`,
  `tbl-cnrps-orphelins`, `tbl-cnrps-perequation`, `tbl-regimes-speciaux` et les annexes de
  textes : leurs valeurs sont classées B ou C dans `recension-parametres-en-dur.md`. Les
  tableaux arabes faits main de ces trois chapitres attendent la retraduction.

## Prestations sociales

- **État d'ensemble au 10 octobre 2026 : le volume entier est au format « ruptures au premier plan,
  détail replié »**, en cinq chapitres et une annexe (le glossaire), dans cet ordre :
  1. `index.qmd`, « Présentation » (`#sec-prest-presentation`) — refaite le 10 octobre 2026 :
     renvois aux volumes voisins en tête ; « Vue d'ensemble » (`#sec-prest-vue-ensemble`) avec
     le tableau des naissances de dispositifs, 1951-2025 (`#tbl-prest-naissances`, treize lignes,
     sans citation de loi, dates reprises des chapitres) ; « Les chapitres du volume »
     (`#sec-prest-chapitres`, une ligne par chapitre sous son titre) ; « Comment lire le volume »
     (`#sec-prest-guide-lecture`) ; « Les organismes » (`#sec-prest-organismes`, encadré engendré).
     Deux blocs repliés : le classement ouverture × forme avec ses textes (`#tbl-prest-classement`,
     l'ancien tableau « Deux axes »), le vocabulaire des textes. L'encadré des quatre conventions,
     « Le périmètre de l'assistance » et la cellule Python sont retirés. **Reste** : une frise
     (`fig-prest-frise`) quand un composant existera dans `scripts/` — le tableau en tient lieu.
  2. `_matrice.qmd`, « Qui est couvert : les régimes et les prestations »
     (`#sec-matrice-regimes`, identifiant gardé : `remunerations_publiques/index.qmd` y mène) —
     remonté en deuxième position et refait le 10 octobre 2026 ; il absorbe `_contributives.qmd`
     (supprimé ; `#sec-prest-contributives` est désormais la section « Comment un droit
     s'ouvre »). Trois sections : « La matrice » (`#sec-matrice-lecture`), « Entre les régimes et
     l'assistance » (`#sec-matrice-frontiere`), « Comment un droit s'ouvre ». La matrice
     (`#tbl-matrice-regimes`) porte neuf régimes **et les deux catégories de l'Amen social**, en
     sept colonnes de symboles ; un second tableau (`#tbl-matrice-assistance`) dit, prestation par
     prestation, ce que reçoivent les catégories pauvres et les catégories à revenu limité,
     d'après `_non_contributives.qmd`. Les articles de chaque case sont au registre replié
     (`#tbl-matrice-textes`, l'ancienne matrice). **Reste** (TODO du chapitre, textes à lire,
     tous dans le corpus *a priori*) : la frontière — l'affiliation fait-elle obstacle au
     transfert mensuel (décret gouvernemental n° 2020-317, art. 3 à 9) ; une famille des
     catégories pauvres affiliée cumule-t-elle allocations familiales et allocation de 30 D
     (arrêtés du 1er avril 2022 et du 3 novembre 2025) ; la carte de soins gratuits et le support
     de 2022 connaissent-ils la condition de non-affiliation de la carte à tarifs réduits — ;
     l'extension de la loi n° 96-101 aux régimes agricoles et aux contractuels publics ; l'entrée
     du régime de la loi n° 2002-32 dans l'assurance maladie ; les dates d'effet et la pagination
     des textes de 2024 ; douze notions de glossaire à créer (terminologue). La colonne
     « Maladie, maternité » réunit les deux indemnités, que l'ancienne matrice ne séparait pas :
     à scinder quand les articles auront été relus régime par régime.
  3. `_prestations_familiales.qmd` (`#sec-prest-familiales`) — converti le 9 octobre 2026
     (entrée ci-dessous).
  4. `_autres_risques.qmd` (`#sec-prest-autres-risques`) — converti (entrée ci-dessous).
  5. `_non_contributives.qmd` (`#sec-prest-non-contributives`) — converti (entrée ci-dessous) ;
     **le 10 octobre 2026, le passage sur le score est corrigé d'après la précision du
     propriétaire** : le transfert est ouvert aux ménages dont le score se situe dans le premier
     décile (Banque mondiale, PAD4815, § 34) ; ne sont pas publics les coefficients du modèle ni
     la valeur du score qui borne ce décile. Mis en accord : vue d'ensemble, état du droit,
     `#sec-nc-eligibilite`, ligne de registre `#r-nc-elig-score`, `#sec-nc-etudes-ciblage` ; fiche
     `r-amen-seuil-score-circulaires` (circulaires de mai 2022 et d'octobre 2025, à obtenir du
     ministère : hors corpus).
  L'annexe `_notations.qmd` est supprimée : ses sept symboles (A, N, r, n̄, τ_r, W, W̄) sont
  définis sous la formule de `#sec-pf-regime-1961` et redéfinis là où ils resservent
  (`#sec-pf-reforme-1976`, `#sec-pf-etat-du-droit`) ; aucun renvoi ne visait ses identifiants.
- **Graphie** : « Amen social » dans tout le volume français, « AMEN SOCIAL » dans les seules
  citations de la loi. **Restent en « AMEN social »** : `precis/glossaire.yml` (sept occurrences,
  dont le terme de l'entrée `amen-social`, d'où quinze dans le `_glossaire.qmd` engendré de ce
  volume et une dans celui de la compensation) — au terminologue — et
  `precis/fr/caisses/index.qmd` (une occurrence).
- **Arabe** : `precis/ar/prestations_sociales/_quarto.yml` suit le nouvel ordre depuis le
  10 octobre 2026 (`_contributives.qmd` et `_notations.qmd` retirés de la liste, `_matrice.qmd`
  en deuxième position). Les `.qmd` arabes ne sont pas touchés : `_contributives.qmd` et
  `_notations.qmd` y restent sur le disque, hors du livre, et l'`index.qmd` arabe, non encore
  retraduit, renvoie à `@sec-prest-contributives`, que le livre arabe ne contient plus — un
  renvoi non résolu au rendu arabe, jusqu'à la synchronisation de traduction (différée).
- **La compensation est sortie du volume le 6 octobre 2026** : `_compensation.qmd` est supprimé,
  son texte forme le volume IX (rubrique « La compensation » ci-dessous) ; le plan du volume
  (`index.qmd`) y renvoie par un lien entre livres.
- **Chapitre des prestations familiales converti le 9 octobre 2026** (`_prestations_familiales.qmd`,
  « ruptures au premier plan, détail replié », section `.domicile-unique`, 42 lignes de registre
  `#r-pf-…`, huit blocs repliés) : vue d'ensemble, mise en place 1944-1961, grandes réformes
  (1980, 1989, 1994 ; 1976 et 1986 dans l'entre-temps), état du droit en 2026, une section par
  prestation adjointe, secteur public, longue période. Trois figures nouvelles, tirées de la
  série `prestations-familiales-parametres` (écrite par `generate_prestations_tables.py`) :
  `#fig-pf-montant-max`, `#fig-pf-plafond-smig`, `#fig-pf-msu-creche-reel` ; dinars de 2025 par
  `scripts/dinars_constants.py`, le déflateur du marché du travail remonté dans `scripts/`
  (`marche_travail/figures/deflateur.py` le réexporte). Aucun tableau de cotisations dans ce
  chapitre : le financement renvoie à `cotisations_sociales/_autres_branches.html#sec-cot-famille`.
  **Restent, par disponibilité :**
  - *lisible au corpus* : la **date d'effet de la loi n° 96-65** (fin de l'article unique à relire,
    JORT n° 60 du 26 juillet 1996, déposé le 30 juillet : 4 août 1996 si l'article ne dit rien) et
    celle de la **loi n° 96-101** (mention de dépôt du JORT n° 94 de 1996 à relever à l'image,
    rectificatif au JORT n° 7 de 1997, p. 114) — le chapitre dit « non établie ici » ; la **loi
    n° 82-71** du 15 août 1982 (JORT n° 55, p. 1737), lue partiellement, sans clé de
    bibliographie : ligne de registre sans ancre ni citation ;
  - *à dépouiller* : les lois modifiant les articles 52, 54 et 61 de la loi n° 60-30 **de 2007 à
    2026** (fiche `r-pf-art61-apres-1988`, couverte jusqu'au 23 juillet 2007) ; un éventuel décret
    de fixation des indemnités familiales du secteur public **postérieur à 1996** (aucune passe
    documentée, pas de fiche) ;
  - *à obtenir* : le décret du 8 juin 1944 et ses modificatifs (hors de la couverture de
    `jort_cache.db`) ;
  - *arabe* : le chapitre arabe garde l'ancien plan et la légende « constants de 1990 » de
    `fig-cnss-allocations-familiales`, dont le module trace désormais des dinars de 2025
    (traduction différée) ;
  - *tableau fait main* : `tbl-pf-ages` (âges limites, art. 54), faute de grandeur à la base des
    tableaux (`backlog-modele.md`).
- **Dépense des allocations familiales, 1990-2004 — fait le 3 octobre 2026** (`#fig-cnss-allocations-familiales`, `#sec-pf-longue-periode`), tirée de la rétrospective financière 1990-2004 de la CNSS (`cnss-retrospective-1990-2004`, exemplaire papier numérisé ; série `cnss-retrospective-ressources-emplois` snapshotée le 3 octobre 2026), déflatée, depuis le 9 octobre 2026, par l'indice du précis en **dinars de 2025** (`scripts/dinars_constants.py` ; 346 MD de 2025 en 1990, 209 en 2004 — avant : IPC des annuaires de l'INS, base 1990). Restent : allocataires, enfants, montant moyen, dépense avant 1990 et après 2004 (TODO du chapitre). **221 valeurs de 1999** (et quelques-unes de 2000) masquées par la reliure restent à lire sur l'original papier (tunisia-data#26) ; en attendant, la figure trace des estimations hachurées ou creuses. Quand le classeur revient : réinjecter dans tunisia-data, relancer `figtools.refresh_cache("cnss-retrospective-ressources-emplois")`, puis relire la note de lecture, qui cite des montants. Depuis le 3 octobre 2026, la figure a trois vues : millions de dinars, % du PIB (PIB du ministère des Finances, série `irpp-ratios`, rupture de base des comptes nationaux marquée en 1997, non corrigée) et % du total des ressources de la CNSS (tableau de l'ensemble, page 78, toutes branches). Depuis le 9 octobre 2026, une quatrième vue donne les millions de dinars de 2025, à part des dinars courants.
- **Onze paliers de l'allocation** entre 1987 et 2018 n'ont aucun fondement textuel publié.
  Les décisions ou circulaires de la direction générale de la promotion sociale et
  les rapports administratifs sont à chercher **hors du JORT**. L'arrêté de 2024
  confirme 180 D à sa publication, pas la date de départ attribuée à 2018 (issue
  openfisca-tunisia #462) : aucune date de palier ne devient certaine par interpolation.
- **Lecture immédiate des aides adjacentes** : arrêtés du 30 septembre 1997 et du
  12 décembre 2003 (personnes âgées), du 1er juin 2006 et du 28 avril 2017
  (personnes handicapées). Les quatre fascicules français sont **locaux et textuels** :
  `Jo08197.pdf`, `Jo1022003.pdf`, `Jo0462006.pdf`, `Jo0422017.pdf`. Celui de 1997
  renvoie au montant servi par un programme administratif : il ne donne pas à lui seul
  une série chiffrée. Le décret n° 2018-626 sur la banque de données est également
  lisible dans `2018/fr/Jo0632018.pdf` ; son contenu restait noté comme inconnu.
- **Lois de finances** : l'extrait français local `PDFs/Lois_de_Finances/Loi_de_Finances_2025.pdf`
  contient l'article 26 sur l'aide aux patients allergiques au gluten : le lire et
  relever sa page avant de conserver la qualification « dérivée » du tableau. La LF
  2026 est au corpus en arabe, pas dans une édition française vérifiée : ses autres
  articles demandent lecture arabe puis confirmation française si celle-ci paraît.
- **Conflit de pagination** des éditions française et arabe de textes de 2024 et postérieurs :
  certains folios restent à établir. La date de la loi n° 2017-47 est tranchée au JORT
  n° 50 de 2017 : 15 juin 2017, publié le 23 juin.
- **OCR ciblé** : décret n° 75-952 (`1975/fr/Jo08775.pdf`, scan local) pour la série
  des indemnités familiales antérieure à 1986. La circulaire n° 42 de 1996,
  **textuelle et déjà locale** dans `1996/fr/Jo09496.pdf` (à partir de la p. 2349),
  peut être lue sans OCR pour établir les règles de gestion. Les arrêtés des quotas
  régionaux des cartes AMG et le décret d'application du fonds contre la perte
  d'emploi de la LF 2025 restent à identifier (`docs/recherches.yml`).
- **Aides occasionnelles de l'AMEN** : le modificatif du 10 juillet 2025 est lu dans
  l'édition arabe du JORT n° 88, pp. 2058-2059 (relu le 9 octobre 2026). Il relève de 50 à
  100 D l'aide de rentrée scolaire, avec effet au 1er septembre 2024, élargit les cas couverts
  et interdit le cumul avec des aides publiques au même titre. C'est la même aide à deux dates :
  le chapitre le dit, et garde un tableau fait main d'une ligne à côté du tableau engendré des
  cinq aides (état de 2022) tant que le palier de 100 D n'est pas versé en amont
  (`backlog-modele.md`). L'édition française reste à obtenir : le fichier local
  `2025/fr/Jo0882025.pdf` est l'édition arabe, octet pour octet.
- **Amen social et aide permanente mis à jour le 9 octobre 2026** (`_non_contributives.qmd`,
  correction bornée, chapitre non converti) :
  - **fait** : tableaux `amen_base`, `amen_supplement_enfant`, `amen_vs_afnc` régénérés (état
    initial au 25 mai 2020, date exécutoire ; palier de 280 D au 1er janvier 2026 ; allocation
    familiale des 6 à 18 ans, 30 D au 9 novembre 2025) ; tableau des plafonds de ressources de
    l'article 5 engendré (`amen_plafonds_ressources`, `tbl-amen-plafonds`) ; arrêté du 5 août
    2026 sur le PNAFN intégré ; trois clés créées, textes lus dans les deux éditions, fascicules
    **locaux et textuels** : `arrete-2026-04-21-transferts` (`2026/fr/Jo0402026.pdf`, p. 786),
    `decret-2025-426-allocation-familiale-6-18` (`2025/fr/Jo1212025.pdf`, p. 2518),
    `arrete-2025-11-03-allocation-familiale-6-18` (`2025/fr/Jo1322025.pdf`, p. 2963) ;
  - **reprise du 9 octobre 2026, d'après `docs/notes/prestations-sociales-lectures-2026-10-09.md`** (réponses D0 à D5, D11 ; six passages,
    rien de réorganisé) : l'allocation des 6 à 18 ans est décrite comme un programme pilote sur
    don depuis 2022 (rapport du ministère pour 2023, UNICEF 2024, Banque mondiale 2026), puis
    instituée par le décret n° 2025-426, qui ne vise que la Constitution ; le supplément de 10 D
    est dit borné aux 6 à 18 ans depuis le 1er février 2022, non supprimé ; la majoration pour
    handicap lourd est dite valoir pour les quatre paliers, avec la divergence « à charge » de
    l'édition arabe ; le seuil de score est dit fixé par aucun texte publié ; les visas de
    l'arrêté du 5 août 2026 (textes de pensions) sont signalés, avec renvoi au livre
    « Retraites ». Trois clés créées en français et en arabe (`mas-amen-social-2023`, sans
    adresse publique vérifiée ; `unicef2024allocations618` ; `banquemondiale2026ppiaf000292`),
    PDF rangés dans `tunisia-data` ; trois fiches de recherche créées
    (`r-amen-smig-regime`, `r-amen-seuil-score-circulaires`, `r-amen-cumul-supplement-6-18`) ;
  - **reste, pour la relecture humaine** : valider la lecture D3 (décompte des alinéas de
    l'article 5, appuyé sur l'article 7 ; décret lisible dans `2020/fr/Jo0452020.pdf`, p. 1093,
    et dans l'édition arabe, p. 1248) avant d'engendrer les plafonds majorés ; dire si l'édition
    arabe fait foi pour la condition « à charge », et sur quel texte ;
  - **reste, pour le documentaliste** (TODO et ancres du chapitre) : relire **à l'image** les
    pages du rapport du ministère pour 2023 sur l'allocation des 6 à 18 ans (PDF 36-38, lues sur
    la seule couche texte arabe : convention du 28 septembre 2022, 191, 188 et 124,6 millions de
    dinars, effectifs de décembre 2023, phrase des 20 D du don et des 10 D du budget) — le PDF
    est local, aucune OCR à lancer ; ce qui a été servi au titre de 2025 (institution au
    1er janvier, montant exécutoire le 9 novembre) ; la règle de cumul du supplément de 10 D et
    de l'allocation de 30 D depuis 2025 (`r-amen-cumul-supplement-6-18`, aucun texte identifié) ;
    le régime du salaire minimum des plafonds (`r-amen-smig-regime`) ; les circulaires du score,
    mai 2022 et octobre 2025, hors *Journal officiel*, **à obtenir**
    (`r-amen-seuil-score-circulaires`) ; les six études citées de seconde main par les pièces
    de la Banque mondiale (§ 1.10 de la note), à récupérer avant toute section d'études ;
  - **reste, pour le terminologue** : la définition de « allocation familiale non
    contributive » au glossaire ne connaît que les moins de six ans ;
  - **non fait ici** (conversion du chapitre, `docs/notes/prestations-sociales-plan-architecte.md`) :
    figures de l'aide permanente, des bénéficiaires et des crédits ; séries du rapport de suivi
    du ministère pour 2023, à instantaner — dont les enfants de 6 à 18 ans allocataires, à tracer en deux
    segments, don puis budget (juillet 2022, décembre 2023, mai 2026 ; § 1.11 de la note de lectures) ;
    rapports extérieurs dépouillés dans la note de lectures, section d'études non écrite.
    → **clos par la conversion ci-dessous** ; la figure des enfants l'est par
    `fig-nc-montee-en-charge` (retouches du 9 octobre 2026).
- **Assistance sociale convertie aux principes de présentation — 9 octobre 2026 (non commité, à
  relire)** (`_non_contributives.qmd`, `#sec-prest-non-contributives`, titre « L'assistance
  sociale : du programme d'aide aux familles nécessiteuses à l'Amen social », chapitre en
  `.domicile-unique`) :
  - **fait** : vue d'ensemble, état du droit en 2026, mise en place (1986-1988), deux réformes
    (2019-2020, 2022 et son étape de 2025), une section par dispositif, détail en vingt-deux
    blocs repliés ; buts de l'article 7 de la loi organique cités ; section administrative
    (`#sec-nc-administration` : allocataires 2018-2023, crédits 2021-2023, enfants 2022-2026,
    indicateurs de suivi 2024-2026, financement extérieur) et section d'études
    (`#sec-nc-etudes` : ciblage simulé sur l'enquête de 2015, incidence CEQ de 2026, coût en part
    du PIB sans base dite, transfert rapporté au salaire minimum, enquête de l'UNICEF) ; deux
    séries du ministère versées au cache (`mas-amen-social-2023-beneficiaires-bruts`,
    `…-credits-bruts`) et deux figures (`fig-nc-beneficiaires`, `fig-nc-credits`) ; figure de
    l'allocation du PNAFN passée en dinars de 2025 et prolongée jusqu'au constat de 2024
    (`figures/assistance.py`, déflateur du volume « Marché du travail » chargé par son chemin) ;
    plafonds de ressources convertis en dinars aux deux régimes du salaire minimum
    (`tbl-nc-plafonds-dinars`, calculé depuis `marche-travail-smig-smag`) ; décrets de
    prorogation des cartes de soins portés au chapitre (`tbl-nc-cartes-prorogations`) ; cinq
    clés créées en français et en arabe (`banquemondiale2021pad4414`,
    `banquemondiale2022pad4815`, `banquemondiale2025isr04716`, `banquemondiale2026isr08116`,
    `banquemondiale2021pret9230tn`), `bct-ra` recopiée du volume « Marché du travail » ;
  - **reste, rédacteur** : prolonger la figure de l'aide permanente par la base du transfert de
    l'Amen social et la renommer `fig-nc-aide-permanente` — il manque une série du cache pour
    `amen_social/allocation_base`, à écrire par `generate_prestations_tables.py`
    (`ecrire_serie_parametres`) ; raccorder `figures/assistance.py` au déflateur partagé quand
    il sera sous `scripts/` ; libellés arabes des trois figures (repli sur le français) ;
    `figures/pnafn.py` n'est plus appelé que par le chapitre arabe, à retirer quand celui-ci
    sera resynchronisé ;
  - **reste, documentaliste — séries à verser à `tunisia-data`** (tableaux faits main
    `tbl-nc-effectifs`, `tbl-nc-enfants`, `tbl-nc-suivi-projet`, `tbl-nc-pib`,
    `tbl-nc-ciblage-simule`, sourcés ligne à ligne ; PDF locaux et textuels) : ménages du
    transfert permanent (2024-2026), enfants de 0 à 5 ans et de 6 à 18 ans allocataires,
    ménages vérifiés par la nouvelle procédure, ménages payés par moyen numérique, budget de
    2021 en dollars, parts du PIB (à ne pas chaîner), couverture par décile (2015), pauvreté
    selon le nombre d'enfants (2021) ; **à relire à l'image avant tout versement** : transfert
    et salaire minimum 1987-2021 (PAD4815, figure 4), couverture de la carte de soins par
    décile (figure 7), répartition par décile de cinq interventions (PAD4414, tableau 6, dont
    la source est une étude UNICEF de 2019) ;
  - **reste, documentaliste — à obtenir** : les six études citées de seconde main (CRES-BAD
    2017, d'où viennent le taux d'exclusion de 53,1 %, les 40 % au premier quintile et l'effet
    de −0,8 point, **non repris au chapitre** faute de méthode dans les documents qui les rapportent ;
    CRES-Banque mondiale 2021 ; *Tunisia Economic Monitor* de l'automne 2025 ; analyse CEQ ;
    rapport annuel de l'Amen social pour 2022 ; UNICEF 2019) ; l'arrêté d'application du
    décret n° 2022-919 ; les conditions du candidat à l'autonomisation économique ; le décret
    gouvernemental n° 2018-626 ; les décrets n° 93-529, n° 94-1738 et n° 99-1372 ; le décompte
    « onze décrets de prorogation sur seize » de la note, non repris faute de lecture des
    quatre décrets de la chaîne de la carte de soins gratuits ;
  - **retouches du 9 octobre 2026 après lecture du rendu (non commité, à relire)** :
    `tbl-nc-rentree-scolaire` refait en trois dates d'effet (25 mai 2020, décembre 2022,
    1^er^ septembre 2024), montant et enfants visés, avec son registre replié
    (`r-nc-rs-2020/2022/2024`, arrêté, article, page) ; deux séries versées au cache
    (`amen-social-effectifs-suivi`, `pnafn-transfert-smig-banque-mondiale`) ; figure de la
    montée en charge (`fig-nc-montee-en-charge`, deux vues : transfert permanent 2010-2026,
    enfants allocataires 2022-2026, familles de sources non reliées, dates de droit et rupture
    de série du 27 mars 2026) — **clôt** « la figure des enfants » et le versement des séries
    d'effectifs ; quinze valeurs annuelles de la Banque mondiale ajoutées à part sur
    `fig-pnafn-allocation`, le texte disant que le pouvoir d'achat de l'aide n'est pas établi
    avant 2009 ; « transferts financiers directs » réservé aux citations de la loi organique
    (art. 11 : « des transferts financiers directs versés chaque mois »), la prose et le
    glossaire disant « transferts monétaires mensuels » ;
    **reste, rédacteur** : engendrer `tbl-nc-effectifs`, `tbl-nc-enfants` et
    `tbl-nc-suivi-projet` depuis `amen-social-effectifs-suivi` ; verser `amen-social-cout-pib`
    et engendrer `tbl-nc-pib` ; libellés arabes de la figure de la montée en charge ;
    **reste, documentaliste** : date exécutoire de l'arrêté du 8 décembre 2022 (dépôt du
    fascicule n° 136 non établi : le chapitre écrit « décembre 2022 ») ; **à trancher** : la
    colonne « Texte » des tableaux engendrés du chapitre (`tbl-aides-ponctuelles`,
    `tbl-amen-base`, `tbl-amen-vs-afnc`…) rend l'intitulé entier de l'arrêté dans chaque
    case — forme commune à tout `generate_prestations_tables.py`, non modifiée ici ;
  - **reste, bibliographe** : treize clés pour les décrets de prorogation des cartes de soins
    (`tbl-nc-cartes-prorogations`, sans citation) ; type CSL de l'accord de prêt n° 9230-TN ;
    adresses des cinq notices à rouvrir (reprises du catalogue de `tunisia-data`) ;
  - **fait le 9 octobre 2026** : part des crédits du ministère dans le PIB, seconde vue de
    `#fig-nc-credits` (`figures/assistance.py`, `vues_credits`) — total 0,56 %, 0,59 % et
    0,68 % du PIB en 2021, 2022 et 2023, transfert mensuel 0,49 %, 0,49 % et 0,58 % ; PIB aux
    prix courants de la série `cnat-pib-nominal`, édition 2021-2025 des comptes de la nation,
    base 2015 seule, années non rétropolées, renvoi à l'annexe du PIB ; crédits affectés, non
    dépenses exécutées. Les 0,6 % (2021) et 0,61 % (2022) de la Banque mondiale pour le seul
    transfert, base non dite, restent à `#sec-nc-etudes-pib`, hors de la figure : écart
    constaté, non expliqué (**reste** : dépenses exécutées, absentes du rapport du ministère ;
    le PIB employé par la Banque mondiale). Si une édition ultérieure des comptes révise le
    PIB de 2021-2023, relire la note de lecture et les deux phrases du chapitre, qui citent
    les parts à la main.

- **Tableau engendré — fait le 3 octobre 2026** : les indemnités familiales du secteur public
  (`tbl-indemnites-familiales-public`) sont désormais le tableau du livre « Retraites », émis
  dans ce livre ; le montant de l'enfant handicapé (1996), sans paramètre, est passé dans la
  ligne « Sources ». Les taux qui financent l'assurance maladie des agents et des pensionnés
  de la CNRPS et le fonds de perte d'emploi de 2025 viennent aussi du livre « Cotisations
  sociales » (`tbl-cnrps-maladie`, `tbl-prevoyance-pensionnes`, `tbl-perte-emploi`) :
  **depuis le 9 octobre 2026, `_autres_risques.qmd` ne les émet plus** et y renvoie par des
  liens entre livres (voir ci-dessous).

- **`_autres_risques.qmd` converti le 9 octobre 2026** (« ruptures au premier plan, détail
  replié » ; fiche `docs/notes/prestations-sociales-plan-architecte.md`, § 3.4 et 4.4, corrigée
  par `prestations-sociales-lectures-2026-10-09.md`, D6 et D9). Un seul fichier, chapitre
  `.domicile-unique` : vue d'ensemble (`#sec-ar-vue-ensemble`, tableaux `tbl-ar-risques` et
  `tbl-ar-reformes`, registre `tbl-ar-textes`), mise en place 1960-1961, quatre réformes
  (1995-1996, 1996, 2007, 2024), état du droit en 2026 (`tbl-ar-etat-2026`), une section par
  risque, longue période (`#sec-ar-longue-periode`, cinq années des comptes de la CNSS et
  liens vers `fig-cnss-assurances-sociales` et `fig-cnss-atmp-pst` du volume des caisses).
  `#sec-perte-emploi` est gardé, la section est titrée d'après l'article premier de la loi
  n° 96-101. Clé `loi95-101` ajoutée aux `references.json` du livre (français et arabe),
  recopiée du livre des cotisations.
  - **Fait** : les trois tableaux de cotisations retirés (voir ci-dessus) ; fiche de recherche
    `r-loi2024-44-application` créée (une passe sur `jort_cache`, index au 2 octobre 2026).
  - **Générateur à nettoyer** (non touché ici) : `scripts/generate_cotisations_tables.py`
    écrit toujours `cnrps_maladie`, `prevoyance_pensionnes` et `perte_emploi` (`.md` et
    `.liens.yml`) dans `precis/*/prestations_sociales/tables/`, où plus rien ne les lit ;
    retirer ces trois destinations et les six fichiers par langue.
  - **Tableaux faits main** (`TODO (rédacteur)` dans le chapitre) : `tbl-ar-etat-2026`,
    `tbl-ar-indemnites`, `tbl-ar-assiette`, `tbl-ar-conges-2024`, `tbl-ar-deces-multiplicateurs`,
    `tbl-ar-atmp-prestations` — aucun paramètre en amont (`backlog-modele.md`) ;
    `tbl-ar-capital-deces-age` — les grandeurs existent sous `retraite/cnrps/capital_deces/`,
    il manque la fonction du générateur.
  - **Dates d'application non établies** (D9, non écrites comme établies) : loi n° 96-101
    (mention de dépôt du JORT n° 94 de 1996 à relever à l'image, fascicule au corpus ;
    rectificatif du JORT n° 7 de 1997, p. 114, non lu) ; loi n° 2024-44 (aucune clause,
    mention de dépôt non relevée) ; décret-loi n° 2024-4, loi n° 2002-32, loi n° 95-101,
    loi n° 2017-47 (à confirmer ou à calculer). L'article final de la loi de finances pour
    2025 n'est pas cité pour la date du 1er janvier 2025.
  - **À relire à l'image** : loi n° 2004-71, art. 1er (couche texte décodée : l'article n'est
    pas cité entre guillemets, le tableau des réformes ne donne que l'intitulé) ; loi
    n° 95-101, alinéa ajouté à l'article 111 (prescription) ; loi n° 60-30, p. 1609-1610
    (art. 76 à 98).
  - **À lire** : article 17 de la loi de finances pour 2025 dans l'édition française (le
    chapitre le donne d'après l'édition arabe) ; loi n° 94-28, art. 39 à 43 et 48 à 53 (taux
    des rentes, non donnés) ; loi n° 2002-24 modifiant la loi n° 96-101 ; décret du 6 avril
    1950 sur la période légale de couches, sans clé.
  - **Non établi** : qui gère en 2026 la réparation des accidents du travail des agents
    publics (loi n° 95-56, art. 5, et loi n° 2004-71, art. 8, donnés côte à côte) ; ce que
    recouvrent les lignes « Capital-décès » et « Indemnité de décès » des comptes de la CNSS ;
    l'absence de texte postérieur modifiant les taux de 1960 et de 1994 (l'état du droit est
    dit « en 2026 », avec un `TODO (documentaliste)`).
  - **Non traités** (D7, D8, D10, D12, D13 du ticket) : en particulier les prestations de
    soins du régime de base (D13) et la relance de `r-lf2025-art17-decret` (D10).
  - **À obtenir** : séries postérieures à 2004 (CNAM pour la maladie, les couches et les
    accidents du travail ; CNRPS pour le capital-décès) et effectifs de bénéficiaires.
  - **Pour le terminologue** : le terme de `g-indemnite-perte-emploi`, « Protection contre la
    perte d'emploi », n'est pas dans la loi n° 96-101.
  - **Hors de ce chapitre** : `index.qmd` nomme encore le chapitre par « la perte d'emploi »
    (plan du volume) ; à accorder avec le nouveau titre.

## Rémunérations publiques

- **Régime indiciaire converti aux principes de présentation — 8 octobre 2026 (non commité, à
  relire).** `_regime_indiciaire.qmd` suit `docs/notes/remunerations-regime-indiciaire-plan-architecte.md` :
  « Vue d'ensemble » (tableau court `tbl-ri-reformes`), champ, construction (état du droit),
  prélèvements, repères historiques (mise en place, ancien système, 1998, 2007, augmentations
  générales 1993-2028), repères budgétaires et statistiques. Classe `.domicile-unique` sur tout
  le chapitre ; onze blocs repliés, huit registres de textes faits main (64 lignes à ancre).
  Les 22 identifiants, les 13 `TODO`, les 16 ancres de glossaire, les 60 clés et les 87 couples
  (clé, localisateur) du départ sont à l'arrivée ; six clés déjà versées entrent par le
  registre des augmentations (`decret2015-462`, `decret2016-1`, `decret2019-209`,
  `decret2019-1133`, `decret2020-767`, `lf-2026`). Restent :
  - **la grille des traitements de base n'est pas montrée** (P8 de la fiche) : le chapitre en
    donne la structure et un seul exemple (inspecteur central, « environ 203 » puis 611 D).
    Tableau attendu `tbl-ri-grille-reperes` (premier et dernier échelon de quelques grades par
    catégorie, 1998 et 2007), à engendrer depuis les annexes des décrets n° 97-1832 et
    n° 2007-268 — **à documenter d'abord** : les annexes ne sont ni dans le chapitre ni dans
    `precis/_seriescache/` ; relever au passage le montant exact de l'exemple ;
  - **la grille depuis le 1er avril 2007** (Q3) : aucun texte postérieur n'est cité, et le
    chapitre ne dit pas sur quel élément de la rémunération les augmentations générales sont
    servies depuis 2016. L'état du droit est daté « au 1er avril 2007 » sans être dit inchangé ;
    aucune recherche n'a été menée, donc aucune fiche `RECHERCHE` — à créer si la recherche
    est faite sans résultat ;
  - **objet et dates d'effet des textes de structure** (Q1, Q4) : intitulés et rubriques des
    décrets n° 97-1832, n° 97-2127, n° 2007-267, n° 2007-268 ; dates d'effet des lois n° 83-112
    et n° 97-83 (tiret au tableau de la vue d'ensemble) ; fascicules de 1997 et de 2007 au
    corpus, **texte lisible** ; celui de 1983 à vérifier ;
  - **article du décret gouvernemental n° 2016-1** (Q0) : il décide si 2016 est une étape
    (rangement actuel, sans ligne au tableau de la vue d'ensemble) ou une rupture ; relever
    aussi ce que dispose l'article 15 de la loi de finances pour 2026, nommé sans contenu ;
  - **deux fiches de recherche créées** (`docs/recherches.yml`) : `r-epa-regime-propre`
    (établissement administratif à régime entièrement propre) et `r-indemnite-residence`
    (indemnité de résidence commune). Une seule passe chacune, **par les titres de
    `jort_cache` seulement**, le 8 octobre 2026 ; plein texte non parcouru, textes de création
    des établissements non lus ;
  - **hypothèse retirée du texte rendu** (P5) : en 2024, la catégorie D passe d'environ 28 400
    à 39 800 agents quand la première unité d'ouvriers recule d'environ 48 900 à 35 400 ; la
    source n'explique ni l'un ni l'autre. Un reclassement d'ouvriers en catégorie D n'est
    qu'une hypothèse, non attribuée : à documenter (texte de reclassement, note de l'INS)
    avant de l'écrire ;
  - **code des collectivités locales** : le texte n'affirme plus qu'il « ne substitue pas un
    régime de rémunération propre » ; il dit que ce point n'est pas établi. Lecture de
    l'édition arabe toujours à faire (voir plus bas) ;
  - **outillage des tableaux d'augmentations** (P4) : registres `tbl-ri-ige-textes` et
    `tbl-ri-augmentations-textes` faits main ; à remplacer par un rendu « registre » de
    `scripts/augmentations.py` (ancres et citations depuis le CSV) et par un rendu « total par
    cycle et par catégorie », en dinars courants et constants, qui prendrait la place des
    grilles à onze et treize colonnes, repliées telles quelles ;
  - **renvoi de la partition en trois tableaux** : elle n'est appuyée que sur l'article 2 bis
    inséré en 2007 (décret n° 2007-268) ; vérifier à l'annexe du décret n° 97-1832 que la
    grille de 1998 a déjà trois tableaux ;
  - **date du 1er février 1959 de `tbl-cnrps-retraite`** : antérieure à la loi n° 59-18
    (5 février 1959), qui n'énonce pas de date d'effet pour son article 5 — constat porté à
    `docs/notes/backlog-modele.md` ;
  - **version arabe** : les attributs `titre` des onze blocs sont à traduire ; rien n'est écrit
    sous `precis/ar/`.
- **Masse salariale, rupture du numérateur en 1996 et 2000 — constat fait le 6 octobre 2026, cause à
  identifier.** La série du ministère des Finances recule de 2 091,0 à 1 993,2 MD en 1996 et
  bondit de 16,1 % en 2000 ; le détail du fonctionnement (moyens des services, interventions
  publiques) n'y commence qu'en 1996. Le FMI (Staff Country Reports n° 97/57 et n° 00/37, lisibles
  dans `tunisia-data/data/raw/banque-mondiale-rapports/`) ne montre aucune baisse. Reste à faire :
  identifier les dépenses reclassées ; verser les deux clés du FMI (FR et AR) et citer le
  recoupement dans `index.qmd`, à part du budgétaire ; marquer 1996 et 2000 sur
  `#fig-masse-salariale-ratios` (colonne `rupture` de la série, côté entrepôt).
- **PIB par base — fait le 6 octobre 2026** (règle : tout PIB dit sa base et s'il est
  rétropolé ; sinon rupture de série). `#fig-masse-salariale-ratios` trace la part du PIB par
  segments (base 1983 en 1990-1996, présumée pour 1990-1991 ; base 1997 rétropolée par l'INS
  en 1997-2001 ; valeurs propres au ministère, base non précisée par la source, en 2002-2004
  et 2025 ; base 1997 en 2005-2009 ; base 2015 de l'INS en 2010-2024, rétropolée pour
  2010-2014), marque les ruptures de 1997, 2002, 2005, 2010 et 2025, et donne à part la part
  dans les dépenses de l'État, seule mesure homogène. Nouvelle `#fig-masse-salariale-reconciliation`
  (2010-2020) : la masse salariale rapportée au PIB de la base 1997 et de la base 2015 sur les
  années publiées dans les deux bases (2010-2017), et les parts du FMI et de la Banque
  mondiale en marques ; le coefficient 1,06 appliqué à toute la série est supprimé. Le texte de
  `index.qmd` dit la base de chaque période ; les parts de 2012-2014 ne sont plus citées
  (elles ont changé dans la série : 12,30 → 11,71 % ; 12,79 → 12,15 % ; 13,03 → 12,35 %).
  Restent :
  - **snapshots à refaire après fusion de tunisia-data.** `masse-salariale-ratios`,
    `masse-salariale-reconciliation` et `pib-courant-recouvrements` (nouvelle dans le cache)
    sont snapshotées depuis la branche **non fusionnée** `fix/masse-salariale-build` de
    tunisia-data, commit `18be659` (PIB de 2023-2024 déjà aligné sur l'édition 2021-2025 :
    14,48 et 13,93 %). Après fusion sur `main` : relancer
    `figtools.refresh_cache("masse-salariale-ratios", "masse-salariale-reconciliation",
    "pib-courant-recouvrements")`, vérifier que les CSV sortent identiques, sinon relire le
    texte et les notes de lecture, qui citent des parts. L'ordre de fusion des deux dépôts
    est à décider par l'humain. `irpp-ratios`, que la même branche modifie, n'est PAS
    resnapshotée ici (fiscalité, retraites, prestations, cotisations, caisses la lisent) ;
  - **conflit prévisible** avec la branche `docs/annexe-pib`, qui snapshote aussi
    `pib-courant-recouvrements` : `catalog.snapshot.yml` se résout en relançant
    `refresh_cache` ; les entrées de bibliographie `ins-changement-base-2015`,
    `ins-pib-base-2015-2010-2020` et `imf-tunisia-art4-2010` sont reprises à l'identique de
    cette branche (fonds commun FR et AR), pour fusionner sans divergence ;
  - **liens morts tant que l'annexe n'est pas fusionnée** : `../annexe-pib.html` (ancres
    `#sec-pib-ruptures`, `#sec-pib-sources`, `#pib-base-2015`), dans `index.qmd` (texte et
    deux notes de lecture) et `_regime_conventionnel.qmd` ;
  - **arabe** : `precis/ar/…/index.qmd` porte encore l'ancien texte et l'ancienne note de
    lecture (« PIB en base 2015 ») sous la figure refaite, et n'a pas la seconde figure,
    jusqu'à la traduction ; les libellés arabes des figures sont dans le module ;
  - **helper à mutualiser** : le bandeau des bases au-dessus du cadre, le repère triangulaire
    à infobulle et le tracé par segments sont écrits deux fois, dans
    `remunerations_publiques/figures/masse_salariale.py` et dans
    `compensation/figures/compensation.py` (branche `docs/compensation-documentation`) : à
    porter dans `figtools` une fois les deux branches fusionnées ;
  - **rapports extérieurs (documentaliste)** : les parts du FMI (17,6 % en 2020) et de la
    Banque mondiale (14,7 % en 2017, 10,7 % en 2010 ; transferts aux entreprises publiques,
    8,9 % en 2013 et 7,5 % en 2014) sont citées sans page ; la base du PIB de la Banque
    mondiale est à relever dans sa revue des dépenses publiques de 2020 (le texte dit « n'est
    pas précisée ici »). Le 14,1 % de 2019 de la série (« Min Fin/presse ») n'est ni tracé ni
    affiché, faute de source. La part de 1997 en base 1983 citée au texte (10,97 %) n'est
    dans aucune figure : elle se recalcule sur `pib-courant-recouvrements` (2 293,5 /
    20 898,0) ;
  - **bibliographie** : la clé `imf-tunisia-art4-2020` désigne le rapport n° 21/44, dont le
    titre imprimé est « 2021 Article IV Consultation » (relevé sur la branche de l'annexe) ;
  - **catalogue de l'entrepôt** : `ins-pib-base-2015-2010-2020` manque aux `sources` de
    `masse-salariale-ratios` (le module l'ajoute à l'affichage) ; ses `caveats` s'adressent
    à qui trace la série (noms de colonnes, journal des corrections) : le module les
    remplace par un texte pour le lecteur (`PROVENANCE_LECTEUR`) ;
  - `_demo_figure_onglets.qmd` (hors livre, lit l'entrepôt directement) : non repris ;
  - **autres volumes non conformes** (figures de rendement fiscal, figures de la CNSS
    1990-2004, retraites, finances locales) : non touchés ici, inventaire sur la branche
    `docs/annexe-pib`.
- **Chapitres à étoffer** : régime conventionnel public, marché contrôlé et statutaire
  autonome ; le régime indiciaire est le plus développé. Ne pas réutiliser les
  longueurs des chapitres mesurées avant la relecture des rémunérations.
- **Chronologies à construire** : indemnité de magistrature (décrets identifiés au JORT) ;
  textes de rémunération des magistrats de l'ordre judiciaire, des forces de sécurité
  intérieure et des douanes, absents du livre.
- **Présentation des trois chapitres courts — fait le 8 octobre 2026** (`_regime_statutaire_autonome`,
  `_regime_conventionnel`, `_regime_marche_controle`) : vue d'ensemble en tête, trame du volume
  conservée, section « Repères historiques » avec tableau des dates, registres repliés à colonne
  « Portée » ; `.domicile-unique` sur `#sec-statutaire-champ`, `#sec-statutaire-remuneration` et
  `#sec-augmentations-ep` seulement. Restent :
  - **clés versées le 8 octobre 2026 (bibliographe)** : lois n° 70-46, n° 2009-47, n° 67-51 et
    n° 2001-65 ; décrets n° 97-2133, n° 97-2134, n° 78-885, n° 2014-12 et n° 2019-1132 ; les huit
    modificatifs du décret n° 79-96 ; arrêté d'agrément de 1975 et avenant n° 5 de 2022 de la
    convention des banques (`docs/notes/biblio-a-rapatrier.md`) ; les mentions du chapitre
    statutaire autonome et du chapitre du marché contrôlé portent l'appel de citation ; **restent**
    le texte arabe de l'arrêté de 1975 (fichier arabe du fascicule tronqué), le décret n° 2019-1132,
    versé mais non cité (aucune mention au chapitre), et le décret gouvernemental n° 2016-742 du
    10 mai 2016 (magistrats, JORT n° 50 du 21 juin 2016, intitulé arabe seul à l'index, adresses
    française et arabe renseignées) : ni lu ni versé, inscrit au `TODO` du chapitre statutaire ;
    les lois n° 70-46 et n° 2009-47 ont leur ligne de registre et leur lien depuis le 8 octobre 2026 ;
  - **décret n° 2026-65 (magistrats, 2026-2028)** : porté au registre de
    `#sec-statutaire-remuneration` par son seul intitulé ; fascicule JORT n° 44 de 2026
    **à lire** pour les montants ;
  - **`index.qmd`** : la liste des corps du régime statutaire autonome (annonce des chapitres
    et tableau des sous-périmètres) omet les agents des douanes, que le chapitre couvre ;
  - **Banque mondiale, transferts aux entreprises publiques (8,9 % et 7,5 % du PIB)** : ni page,
    ni base du PIB, ni méthode de l'évaluation au chapitre ; revue des dépenses publiques de
    2020 à relire ;
  - **sociétés d'assurance — fait le 8 octobre 2026** (`#sec-marche-controle-assurances`, note
    `docs/notes/remunerations-convention-collective-assurances.md`) : champ, classification,
    bas et haut de la grille de 1975 à 2021 face au SMIG, chaîne des quinze avenants, dix-sept
    clés `cc-assurances-*` (FR et AR), fiche `r-cc-assurances-avenant-16`. Restent :
    liste des assureurs à capital public (le rapport sur les entreprises publiques n'en nomme
    aucun ; rapports du Comité général des assurances, de la FTUSA et des participations de
    l'État **à obtenir** ; pas de fiche de recherche) ; **clos par la relecture à l'image du
    8 octobre 2026** (`…-assurances-relecture-2026-10-08.md`) : grille du 1er juin 2014
    (avenant n° 11) trouvée au n° 4 du 13 janvier 2015, édition arabe, p. 151 (clé
    `cc-assurances-avenant11-grille-2015`), hauts de 2018 et 2019 lus, bas de 1990 et de 1991
    corrigés d'un millime ; **reste** : bas du 1er janvier 1989, illisible dans les deux éditions
    (autre source **à obtenir** : recueil de la FTUSA, exemplaire papier), page française de la
    grille de 2014 (fascicule **lisible**, non ouvert) ; grilles entières (28, pages identifiées,
    **lecture à l'image**) pour le versement en paramètres ; protocole du 8 juin 1984,
    probablement non publié ; dates de signature contradictoires au *Journal officiel*
    (convention révisée : 10 novembre 1982 ou 13 avril 1983 ; avenants n° 1, 7 et 9) ;
    « révision du 24 juillet 1997 » visée par cinq arrêtés (fiche `r-cc-assurances-revision-1997`
    proposée par la note, non versée faute d'ancre au chapitre) ; édition de la loi de finances
    pour 2022 du rapport sur les entreprises publiques : clé `minfin-ep-2022` versée le
    8 octobre 2026 (aucun assureur nommé non plus) ; intitulés arabes des
    dix-sept entrées à relever ; articulation avec le décret n° 2026-68 (pas de colonne en
    dinars constants au tableau des assurances : le propriétaire a répondu non, 8 octobre 2026) ;
  - **marché contrôlé** : aucune rupture datée ; les textes des dates de 1967, 1975, 1978, 2001,
    2014 (décret n° 2014-12) et 2022 sont versés à la bibliographie depuis le 8 octobre 2026.
- **Augmentations générales (5 octobre 2026)** : les tranches de l'indemnité de gestion et
  d'exécution de 1993 à 2013 sont lues et relevées (`augmentations/augmentations-ige.csv`,
  § des cycles du régime indiciaire) ; les décrets des entreprises publiques de 1991 à 2026
  sont lus et présentés au régime conventionnel (`#sec-augmentations-ep`). Note :
  `docs/notes/remunerations-accords-salariaux-publics.md`. Restent :
  - décrets n° 90-1001 et 91-803 (IGE, cycle 1990-1992 ?) : fascicules JORT n° 42 de 1990
    et n° 38 de 1991 au corpus local, **scans sans couche texte** : lecture à l'image
    ou OCR ;
  - décrets parallèles des autres corps (ingénieurs, enseignants, santé, greffes…) :
    fascicules au corpus, **texte lisible** à partir de 1996 ; non relevés ;
  - majoration de l'IGE au titre de 2011 — **trouvée le 8 octobre 2026** : décret n° 2011-2281 du
    21 septembre 2011 (JORT n° 73 du 27 septembre 2011, édition arabe, pp. 1961-1962), repéré
    par son intitulé arabe à l'index et **lu à l'image** ; effet au 1er juillet 2011, de 91 D
    (administrateur général) à 27 D (catégorie D). Clé `decret2011-2281` versée (FR, AR), ligne
    au registre `tbl-ri-ige-textes`, fiche `r-ige-2011` résolue. Restent : l'édition française
    du fascicule, **à obtenir** (absente du corpus, 404 sur pist.tn) pour l'intitulé et la
    pagination français ; le versement de 2011 au relevé `augmentations-ige.csv` et à
    `scripts/augmentations.py` (les deux tableaux engendrés ne la portent pas — `TODO
    (modéliste)`, `docs/notes/backlog-modele.md`). Leçon : une recherche par titres français
    manque les notices dont l'index ne porte qu'un intitulé arabe — ajouter `iort_ar` ou un
    motif arabe dans `titres_like` aux fiches du même genre ;
  - montants arrêtés par la commission supérieure pour les entreprises publiques, 1991-2012
    (fiche `r-montants-ep-commission`) : **à obtenir** hors JORT (rapports sur les
    entreprises publiques, communiqués conjoints de 1996 et 1999) ;
  - décrets des entreprises publiques entre 2013 et 2026 (fiche
    `r-augmentations-ep-2013-2025`) : plein texte 2014-2025 **lisible**, non parcouru ;
  - magistrats : le décret n° 2026-65 est porté au régime statutaire autonome par son
    intitulé (8 octobre 2026) ; le décret n° 2019-1132 est versé (clé `decret2019-1132`,
    8 octobre 2026), non encore cité au chapitre ;
  - poids budgétaire par cycle : aucun texte ne le donne.
- **Séries** : effectifs et masse salariale par régime ; dépenses de défense ; effectifs du
  secteur financier public. Substituer des sources tunisiennes officielles aux chiffres du
  FMI et de la Banque mondiale.
- **Lecture immédiate des textes locaux** : le décret n° 2015-2217 sur les dirigeants
  des entreprises publiques est dans `2015/fr/Jo1012015.pdf`, texte extractible ; en
  établir l'article sur les sociétés à majorité publique avant d'étendre la règle aux
  banques. Le Code des collectivités locales est lisible en arabe dans
  `2018/ar/Ja0392018.pdf` ; relever ses dispositions sur les élus et agents sans
  conclure à l'absence d'un régime par une simple recherche de mots. Le décret
  n° 72-230 est dans `1972/fr/Jo02972.pdf`, **scan** à océriser avant d'en qualifier
  le champ. Les fascicules cités sont sous `PDFs/JORT/`.
- **Convention bancaire** : l'arrêté d'agrément de 2014 est textuel en français
  (`2014/fr/Jo0232014.pdf`), mais il indique que la convention annexée est publiée
  **seulement en arabe** ; son fascicule arabe `2014/ar/Ja0232014.pdf` est présent,
  avec une couche texte **en formes Unicode de présentation** : `pdftotext` suivi
  d'une normalisation NFKC rend ses mots recherchables. Lire ensuite ses articles
  et grilles et ceux des avenants : travail faisable localement, mais pas encore
  établi dans le précis. Ne pas lancer d'OCR sur ce fascicule textuel.
- **Vérifications sur source primaire** : la loi n° 85-78 a été lue dans le JORT n° 58
  de 1985 (art. 1-3 et 75) : statuts particuliers approuvés par décret pour son champ
  principal, option transitoire entre statut et convention sectorielle pour certaines
  sociétés à capital partiellement public. Pour les caisses sociales (issue #13), le
  décret présidentiel n° 2022-76 abroge le statut approuvé en 1999. Retrouver les
  textes des deux statuts pour qualifier la grille : le JORT n° 20 de 2022 ne joint
  pas l'annexe annoncée, et le JORT arabe n° 77 de 1999 porte le décret d'approbation
  sans reproduire le statut intégral. **Un OCR de ces fascicules ne produira pas
  l'annexe absente** : la chercher auprès des organismes ou dans un autre recueil.
  Restent aussi le champ des banques publiques et les
  conventions réellement applicables aux entreprises publiques. Les **branches financées par
  les cotisations CNRPS** sont aux articles 8 à 10 de
  la loi n° 85-12, dont le fascicule — JORT n° 76 de 1985 — est un scan : océrisation requise.
- **Deux points clos le 20 septembre.** La chaîne des décrets fixant la liste des employeurs
  soumis à la loi n° 95-56 est vérifiée fascicule par fascicule et citée (n° 95-2487, puis
  2000-908, 2001-1446, 2006-2777, 2012-2586). Et l'**indemnité familiale** ne relève pas de
  la CNRPS : c'est une indemnité de rémunération portée par le budget de l'employeur, ce que
  le livre « Prestations sociales » établissait déjà sans que celui-ci en tire parti.
- **Code des collectivités locales** : voir la lecture locale de l'édition arabe ci-dessus ;
  son édition française n'est pas au corpus.
- **Tableaux de paramètres engendrés — fait le 3 octobre 2026** : le régime indiciaire
  reçoit, depuis le générateur des cotisations, la retenue pour pension de la CNRPS
  (`tbl-cnrps-retraite`) et le taux salarial de la contribution sociale de solidarité
  (`tbl-css-salarie`). Le CSV des augmentations reste fait main (RE-01, RE-02, classés C).

## Cotisations sociales

- **Accidents du travail par activité et taux légal — mis en réserve le 6 octobre 2026**
  (`docs/reserve/atmp-bareme-sinistralite.md`). Les nuages de points ajoutés la veille
  (`fig-atmp-secteurs`) sont **retirés du chapitre** `_accidents_travail.qmd` : une relectrice
  signale que le rattachement des employeurs aux activités (NAT61 à la CNSS) n'est pas fiable,
  ce qui fausse la sinistralité par activité. Module et données conservés, plus rendus. À
  reprendre quand une source publiée établira la classification (passage NAT61 → NAT2009) et
  un tableau de passage par codes d'activité ; conditions détaillées dans la fiche. Constat
  d'origine, conservé pour la reprise : le rapport CNAM
  2023, PDF arabe lisible, porte la fréquence des accidents avec arrêt par
  activité (PDF 15), le nombre d'accidents (PDF 13) et celui des décès
  (PDF 26) pour 2021–2023 ; les séries sont conservées séparément dans
  `tunisia-data`. Dix activités ont un point de l'article 2 du décret
  n° 99-1010 qui leur correspond par le libellé et porte un taux unique ;
  rapprochement éditorial, non correspondance administrative vérifiée.
  Quinze autres rubriques agrègent plusieurs taux, ne recoupent pas les
  intitulés du barème ou n'ont pas de ligne de décès ; établir le passage par les codes AT/MP auprès de la
  CNSS/CNAM avant de les inclure. Pour 2023, la fréquence utilise les
  assujettis de 2022 ; décès par secteur lisibles pour 22 activités, les
  trois absentes n'étant pas interprétées comme nulles. Première vue :
  taux légal en x, fréquence des accidents avec arrêt pour 1 000 travailleurs
  en y ; seconde : accidents mortels pour 1 000 accidents déclarés en y,
  ajustement linéaire et corrélation de Pearson non pondérés par année et sur
  les dix seules activités retenues. Ce second ratio n'est pas un taux de
  mortalité par travailleur. Le barème de 1999
  n'est pas une série de taux effectivement acquittés de 2021 à 2023 :
  aucun modificatif de l'échelle n'est identifié (`r-atmp-echelle-modificatifs`,
  plein texte parcouru le 5 octobre 2026), et la modulation des art. 10 à 27 du
  décret n° 95-538, désormais exposée (`#sec-cot-at-modulation`), peut écarter la
  cotisation due du taux du barème, sans qu'aucune donnée sur sa pratique soit connue.
- **Autres prélèvements sur les salaires — rédigé le 5 octobre 2026** (`_prelevements_salaires.qmd`,
  `#sec-cot-prelevements-salaires`, après `_taux_global.qmd`) : TFP et contribution au FOPROLOS,
  taux en tableau engendré (`tbl-tfp-foprolos`, openfisca-tunisia 0.119, #478) ; les
  changements d'assiette (1987, 2003) sont dans la prose. Note : `docs/notes/cotisations-prelevements-salaires.md`. Ouvert :
  taux de la TFP de 1957 à 1966 (décret du 16 janvier 1957, fascicule ni dans le corpus ni sur
  pist.tn, `r-tfp-decret-1957`) ; assiette de la TFP avant 1989 (décret de 1957, code du travail
  de 1966, art. 364-365 : JORT n° 22/1966 lisible au corpus, à l'image) ; date d'effet de la LF
  2003 ; exclusions handicapés et emploi à l'étranger sans texte (`r-tfp-exclusions-handicapes-etranger`) ;
  exonérations des régimes d'incitation non inventoriées ; décret n° 94-492 (industries
  manufacturières) non lu ; prélèvements sur le fonds de 2011-2013 connus par leurs intitulés
  seulement ; rendement : aucune série — prévisions des tableaux « ت » des LF 2016-2019 à
  relever (LF 2018 lue), réalisations à chercher dans les lois de règlement et les rapports de
  la DGI. **Arabe** : chapitre déclaré en commentaire dans `precis/ar/cotisations_sociales/_quarto.yml`,
  à décommenter dans la même PR de traduction que celle qui retraduit `_taux_global.qmd` et
  `index.qmd`, sans quoi le livre arabe affiche `?@sec-cot-prelevements-salaires`.

- **Découpé en chapitres le 4 octobre 2026** (déplacement seul, aucune valeur changée, ancres
  gardées) : `index.qmd` (« Présentation » : introduction, conventions, présentation générale,
  encadré des caisses), `_assiette.qmd`, `_taux_global.qmd`, partie « Les branches, une à une »
  (`_branches.qmd`, `#sec-cot-branches`) — `_pensions.qmd`, `_maladie.qmd`,
  `_accidents_travail.qmd`, `_autres_branches.qmd` (famille, emploi et fonds spécial,
  complémentaire ; ancre nouvelle `#sec-cot-autres-branches`) —, `_regimes.qmd`, `_bilan.qmd` ;
  annexes `_notations.qmd`, `_textes_modificatifs.qmd`. L'ancre `#sec-cot-annexes`, que rien ne
  visait, a disparu. Les liens des autres livres sont redirigés vers les nouvelles pages, **sauf
  ceux du livre des caisses**, restructuré en parallèle, à corriger après fusion : huit liens de
  `_comptes_regimes.qmd`, `_etat_caisses.qmd` et `_comptes_longue_periode.qmd` visent encore
  `cotisations_sociales/index.html#…` (`sec-cot-taux-unique`, `sec-cot-ventilation` →
  `_taux_global.html` ; `tbl-quote-part-rsna` → `_pensions.html` ;
  `fig-cotisations-branches-1990-2004` ×2 → `_bilan.html` ; `sec-cot-fonds-special`,
  `sec-cot-protection-sociale` → `_autres_branches.html` ; `sec-cot-cnrps-employeur` →
  `_regimes.html`).
- **Arabe — chapitres déclarés** : `precis/ar/cotisations_sociales/_quarto.yml` déclare les
  chapitres du découpage du 4 octobre 2026 (constaté le 5 octobre 2026, le livre arabe rend) ;
  seul `_prelevements_salaires.qmd` y reste en commentaire (voir ci-dessus).

- **Les caisses ont quitté ce livre le 4 octobre 2026** : cadre comptable et budgétaire, et les
  trois figures de la rétrospective CNSS par régime et par branche, dans le livre « Les caisses de
  sécurité sociale » (voir sa section ci-dessous). Ce livre garde le prélèvement, dont
  `#fig-cotisations-branches-1990-2004` et `#fig-cotisations-cnss`.

- **Cotisations par branche, 1990-2004 — fait le 3 octobre 2026** (`#fig-cotisations-branches-1990-2004`, après `#fig-cotisations-cnss`), tirées de la rétrospective financière 1990-2004 de la CNSS (`cnss-retrospective-1990-2004`, exemplaire papier numérisé ; série `cnss-retrospective-ressources-emplois` snapshotée le 3 octobre 2026). Comptes de bilan, non encaissements : écart de −1,13 % à −0,81 % avec la série encaissée en 2000-2004, inexpliqué. Les notes du document datent la réduction de 2 points de la branche familiale par la loi n° 97-4 au 1er octobre 1996, date que la loi n'énonce pas : à confronter à la datation du taux global (`#sec-cot-taux-unique`). **221 valeurs de 1999** (et quelques-unes de 2000) masquées par la reliure restent à lire sur l'original papier (tunisia-data#26) ; en attendant, la figure trace des estimations hachurées ou creuses. Quand le classeur revient : réinjecter dans tunisia-data, relancer `figtools.refresh_cache("cnss-retrospective-ressources-emplois")`, puis relire la note de lecture, qui cite des montants. Depuis le 3 octobre 2026, la figure a trois vues : millions de dinars, % du PIB (PIB du ministère des Finances, série `irpp-ratios`, rupture de base des comptes nationaux marquée en 1997, non corrigée) et % du total des ressources de la CNSS (tableau de l'ensemble, page 78, toutes branches).
- **Accidents du travail (§ sec-cot-at)** : les décrets n° 95-538 et 99-1010 sont lus
  dans les deux éditions (taux, entrée en vigueur au 1er janvier 1995 et au 1er avril
  1999). Les deux échelles sont engendrées, avant et après transfert du point
  (`tables/atmp_1995.md`, `tables/atmp_1999.md`). Reste : le financement sous la loi
  n° 57-73 (texte à obtenir pour ce livre ; clé à verser au fonds commun).
- **Accidents du travail : le constat de la Cour des comptes — rédigé le 8 octobre 2026**
  (`#sec-cot-at-modulation-cour`, et un paragraphe dans `#sec-cot-at-classement`). Source : 32e
  rapport annuel général (février 2021), chapitre « حوادث الشغل والأمراض المهنية », 56 pages lues à
  l'image, réponses du ministère et de la CNAM comprises ; clé `courdescomptes2021-rapport32` ;
  PDF à l'entrepôt (`tunisia-data`, `data/raw/cour-des-comptes/84/rapport32.pdf`, et le chapitre
  seul sous `76/`). Retenus, attribués à la Cour : majoration non appliquée depuis 2009, réductions
  accordées, commission, taux non mis à jour et erreurs de codes. Ouvert :
  - **écartés à dessein** : les réponses et engagements de la CNAM et du ministère, invérifiables ;
    le montant d'indemnités attribué aux 496 entreprises (137,611 MD), supérieur au total que le
    même rapport donne pour le régime (131,311 MD) ; les formules de la synthèse (« أبرز ملاحظات »),
    qui arrondit et regroupe deux constats ;
  - **non rapprochés** : les décomptes d'accidents de la Cour (environ 165 000 déclarations sur
    2015-2019, maladies comprises ; 264 966 sur 2011-2019) et la série de la figure
    `fig-atmp-declares` — périmètres différents (secteur privé seul, déclarations saisies) ;
  - **non repris, hors de ces sections** : prêts de prévention (117 depuis 1995, 9,731 MD), rentes
    (48,327 MD en 2015, 57,518 MD en 2019), indemnités journalières, délais et erreurs de
    liquidation — matière pour le volume des caisses et celui des prestations ;
  - **comité de veille** : composition donnée par la réponse du ministère (avec la CNAM, sans la
    CNSS), nom arabe « لجنة اليقظة لمتابعة تطور حوادث الشغل والأمراض المهنية », circulaire dite en
    cours d'actualisation — non repris dans le texte ; `r-atmp-comite-veille-2001` ;
  - **relu le 8 octobre 2026** par la relectrice du chapitre, et nuancé en conséquence : les
    constats sont rattachés à la période contrôlée (2015-2019) ; la majoration et la réduction
    restent appliquées, rarement, d'après le fichier des employeurs (2010-2023) — précision
    signalée comme telle dans le texte, sans source publiée ; les chiffres détaillés de la Cour
    sur le classement (taux non mis à jour, corrections de codes, montants) sont **retirés du
    texte**, seul le constat général restant ; à reprendre si une source publiée plus récente
    paraît sur le classement des employeurs et la mise à jour des taux.
- **Accidents du travail : CNAM et CNSS, classement des employeurs, sinistres déclarés —
  rédigé le 6 octobre 2026** (`#sec-cot-at-modulation-caisses`,
  `#sec-cot-at-modulation-application`, `#sec-cot-at-classement`, `#sec-cot-at-declares`),
  à la suite d'un retour de lecture. Lus : loi n° 2004-71, art. 5, 8 à 10, 16 et 29, à
  l'image dans les deux éditions ; loi n° 2017-47 ; décret n° 2005-321 en entier (rien sur
  la prévention ni la modulation) ; décrets n° 96-1050 et 2009-2344 (couche texte française,
  non relus à l'image). Deux documents publiés, lus et rapportés comme tels : le Profil
  national de la sécurité et de la santé au travail (ministère des affaires sociales, 2023)
  et La Lettre du CRES n° 8 (janvier 2023). Ouvert :
  - **non établi par un texte** : la caisse qui décide la majoration et la réduction depuis
    2004 ; une commission pour ces décisions (`r-atmp-commission-modulation`) ; la convention
    de recouvrement entre la CNSS et la CNAM (`r-cnam-cnss-convention-recouvrement`) ;
    question posée à la relectrice ;
  - **à lire** : la circulaire n° 20 du ministre des affaires sociales du 19 décembre 2001
    (comité de veille), non identifiée (`r-atmp-comite-veille-2001`) ; les annexes des organigrammes de
    la CNAM (décrets n° 2008-3707 et 2018-747) ; le décret n° 2002-583 ;
  - **rangés le 6 octobre 2026** : les PDF du Profil et de la Lettre du CRES n° 8, dans
    `tunisia-data` (`data/raw/caisses/mas/` et `data/raw/caisses/cres/`), fiches
    `sources/mas-profil-sst-2023.md` et `sources/cres-lettre-8-atmp-2023.md` (tunisia-data#34) ;
    le PDF du ministère a été téléchargé sans vérification du certificat du site ;
  - **deux figures** (`fig-atmp-declares`, `fig-atmp-frequence`, module
    `figures/atmp_sinistres.py`), sur la série `atmp-sinistres-declares-2012-2022-bruts` de
    l'entrepôt (tunisia-data#34, **à fusionner** : le précis n'en porte que l'instantané) ; les
    écarts entre les deux documents pour 2014, 2015 et 2020 sont dits dans le texte et gardés
    dans les données ; reste à raccorder aux statistiques de la CNAM pour 2021-2023 ; les
    intitulés d'indicateurs de l'onglet « Données » ne sont pas traduits en arabe ;
  - **non repris, faute de série** : 209 entreprises bénéficiaires d'une réduction jusqu'en
    2020 et 7 prêts de 2014 à 2019 (Profil, pp. 48-49), cumuls sans source ;
  - **pour le volume des caisses** : recettes, dépenses et résultats du régime de 2018 à 2022
    (Profil, annexe 5, p. 92), avec une incohérence sur les dépenses de 2021 (159,755 MD à
    l'annexe, 222,343 MD au texte p. 28) ; part du régime dans les dépenses de la CNAM de
    2009 à 2019 (Lettre du CRES, figure 1) ; recettes et dépenses de 2007 à 2018 en
    graphique sans valeurs (figure 2) ;
  - **relecteur-ar** : pagination arabe des décrets n° 96-1050 et 2009-2344, et fin du décret
    n° 2005-321, non relevées.
- **Accidents du travail : assiette et modulation — rédigé le 5 octobre 2026**
  (`#sec-cot-at-assiette` : `#sec-cot-at-assiette-principe`, `#sec-cot-at-forfaits`,
  `#sec-cot-at-salaire-comparaison` ; `#sec-cot-at-modulation` : `#sec-cot-at-majoration`,
  `#sec-cot-at-reduction`, `#sec-cot-at-modulation-recours`). Lus à l'image dans les deux
  éditions : loi n° 94-28 (art. 17, 18, 88 à 90), décret n° 95-538 (art. 1 à 29), décrets
  n° 99-1010 et 2000-1439, loi n° 95-101. Trois tableaux **faits main**
  (`tbl-atmp-forfaits`, `tbl-atmp-journees`, `tbl-atmp-modulation`), à engendrer quand les
  forfaits et la modulation seront portés en amont (openfisca-tunisia#471, auquel ajouter
  le décret n° 2000-1439) ; aucun montant en dinars n'est donné. Ouvert :
  - **à relire à l'image** (fascicules français présents au corpus, connus par cette seule édition) :
    loi n° 60-30, art. 42 et 46, rédaction de 1960 (JORT n° 57 de 1960, pp. 1605-1606,
    impression pâle : paraphrasée, non citée) et son édition arabe ; décrets n° 96-341, 2003-1098 et 2008-173 (avantages exclus de
    l'assiette), dont l'édition arabe reste à lire ; le n° 99-1011 est lu dans les deux ;
  - **à lire** (fascicule présent au corpus) : loi n° 88-38 du 6 mai 1988, visée par le
    décret n° 95-538 (JORT n° 33 du 13 mai 1988, p. 735 d'après jort_cache,
    `1988/fr/Jo03388.pdf`) — l'art. 42 entre 1960 et 1995 n'est pas vérifié ;
  - **à calculer** : date exécutoire de la loi n° 95-101 et des décrets n° 96-341,
    2003-1098 et 2008-173 (aucune clause d'effet) ;
  - **à obtenir** : une source administrative (CNSS, CNAM) sur la pratique des forfaits ;
    rien n'établit qu'ils sont appliqués aujourd'hui ;
  - **lectures, non textes** : portée du décret n° 2000-1439 sur l'art. 5 (abrogation
    implicite) ; application à l'AT/MP des décrets d'exclusion (par renvoi seulement) ;
    taux applicable aux forfaits des art. 5 (muet) et 7 (« selon les branches ») ;
  - **relecteur-ar** : termes arabes de l'art. 4 du décret n° 95-538 et de l'art. 18 de la
    loi n° 94-28, transcrits depuis des pages scannées — les divergences sont dites en
    français dans le texte (tonneaux de jauge, pêche au feu, caprins, floriculture,
    malades des hôpitaux psychiatriques), sans citation arabe ;
  - **bibliographe** : clés à créer pour les décrets n° 96-341, 99-1011, 2003-1098 et
    2008-173 ; `loi2004-71` sans `page` ni `container-title` ;
  - **`_assiette.qmd`** : le TODO sur l'art. 42 de la loi n° 60-30 (`#sec-cot-salaire-reel`)
    est en partie levable avec la même matière (rédactions de 1960 et de 1995, décrets
    d'exclusion) ; le décret n° 2000-1439 y a aussi sa place, son forfait valant pour les
    régimes de sécurité sociale ; `tbl-assiettes` n'a pas de ligne AT/MP ;
  - **glossaire — bloquant** : le chapitre ancre sept notions créées sans définition
    (`assiette-cotisations`, `salaire-forfaitaire`, `remuneration-a-la-part`,
    `employes-de-maison`, `louage`, `cotisation-supplementaire`, `maladie-professionnelle`) ;
    `build_glossary.py` s'arrête sur `KeyError: 'definition'` tant que le terminologue ne
    les a pas définies (FR et AR), et le `_glossaire.qmd` du livre n'est pas régénéré :
    neuf liens de glossaire du chapitre restent sans cible (les sept, plus
    `accident-du-travail` et `smag`, que ce livre n'ancrait pas encore) ;
  - **recherches** : fiche `r-atmp-assiette-modificatifs` créée (aucun modificatif des
    art. 3 à 27 autre que les décrets n° 99-1010 et 2000-1439) ; passe de plein texte
    consignée sur `r-atmp-echelle-modificatifs`. Lacunes communes : édition arabe
    1995-2004 sans texte exploitable ; 14 fascicules français de 1995-1998 à océriser ;
    115 fascicules citant la loi n° 94-28 sans le décret, non parcourus un à un.
- **Lecture immédiate** : l'article 4 du décret n° 2007-1406 (`2007/fr/Jo0492007.pdf`,
  source déjà lue pour la maladie) : établir sur pièce ce qu'il change au partage
  employeur/agent. Le décret-loi n° 2024-4 sur les travailleuses agricoles est désormais
  présent dans les deux éditions textuelles du JORT n° 129 de 2024 ; relever taux,
  assiette et dates avant d'affirmer qu'ils sont fixés. Le vieux relevé
  `todo-localisation.md` le classe encore « absent du corpus » : **ce classement est périmé**.
- **OCR ciblé** : la loi n° 65-17 sur les risques couverts par le régime des étudiants
  se trouve au JORT n° 34 de 1965 (`1965/fr/Jo03465.pdf`), scan local. Lire l'article
  pertinent après OCR, au lieu de déduire les branches des seuls décrets de 1992 et 2003.
- **À rechercher/établir** : assiette exacte du régime général, part historique des
  prestations familiales dans le taux global, cotisation maladie des agents publics
  avant 2007 et ventilation des parts résiduelles entre risques ; plusieurs recherches
  négatives ont déjà leur fiche dans `docs/recherches.yml`. Relancer ces fiches plutôt
  que répéter leur conclusion. Pour les modificatifs du décret n° 74-499 après avril
  2026, la fiche `r-dec74-499-modificatifs` est couverte jusqu'au 18 septembre 2026.

- **Tableaux de paramètres engendrés (recension du 2 octobre, lot A) — fait le 3 octobre
  2026** : contribution de l'employeur public à la CNRPS (`tbl-cnrps-employeur`, qui remplace
  le tableau fait main), prévoyance sociale des pensionnés (`tbl-prevoyance-pensionnes`),
  réduction conventionnelle de 1996-2007 (`tbl-reduction-conventionnelle`), classes de
  revenus des régimes à assiette forfaitaire (`tbl-classes-revenu`), assurance maladie des
  agents de la CNRPS (`tbl-cnrps-maladie`), perte d'emploi (`tbl-perte-emploi`). Restent faits main
  les tableaux classés B ou C dans `recension-parametres-en-dur.md` (assiettes, somme des
  trois textes, ventilation, montée en charge AMU, longue période) : ils attendent des PR
  openfisca-tunisia.

## Les caisses de sécurité sociale

Livre créé le 4 octobre 2026 (`precis/fr/caisses/`) ; plan approuvé : architecture A, étapes 2
à 4. Il porte les organismes — histoire, statut, comptes par régime, budget, relations avec
l'État ; les livres « dispositifs » gardent les règles et renvoient ici par l'encadré commun
(`_encadre_caisses.qmd`, engendré par `scripts/generate_encadre_caisses.py`, contrôlé par
`tests/test_encadre_caisses.py`).

- **Découpage en chapitres — fait le 4 octobre 2026** (plan validé par l'humain) : `index.qmd`
  « Présentation » (non numérotée : périmètre `#sec-caisses-perimetre`, carte
  `#tbl-caisses-carte`) ; `_histoire.qmd` « Des caisses du Protectorat aux caisses nationales »
  (`#sec-caisses-panorama`) ; `_statut_cadre.qmd` ; `_comptes_regimes.qmd` (avec la ventilation
  du taux global) ; `_etat_caisses.qmd` ; `_comptes_longue_periode.qmd` (avec « Ce que les textes
  ne disent pas ») ; annexes `_chronologie.qmd` puis glossaire. Ancres inchangées ; liens entrants
  corrigés vers la page de chaque chapitre (cotisations, fiscalité, rémunérations, retraites).
  Mêmes chapitres déclarés dans `precis/ar/caisses/_quarto.yml`.
- **Histoire — rédigée le 4 octobre 2026** (`_histoire.qmd`, note `caisses-histoire.md`) : avant
  1956, d'après Bertrand (*Bulletin économique et social de la Tunisie*, n° 73 et 74 de 1953) et
  les visas des textes de 1956-1961 — Société de prévoyance des fonctionnaires et employés
  tunisiens (pensions, régime de prévoyance de 1951), Caisse de retraite des ouvriers de l'État,
  caisses du semi-public, accidents du travail sans caisse (décret du 15 mars 1921), trois caisses
  de compensation des allocations familiales (décret du 8 juin 1944), mutualité (décret du
  18 février 1954, intitulé seul) ; 1956-1960 lus au JORT — surcompensation (décret du 8 novembre
  1956), Caisse centrale des prestations sociales (loi n° 58-130), Société de prévoyance → Caisse
  nationale de retraites (lois n° 59-18 et 59-19), Caisse de prévoyance sociale (loi n° 59-45,
  **lue** : la tâche précédente est close), CNSS et ce qu'elle reprend (loi n° 60-30, art. 119 à
  131) ; puis la lignée 1960-2004. Restent : **hors corpus** — Journal officiel tunisien antérieur
  à 1956 (ni jort_cache, ni corpus local, ni pist.tn) pour les textes fondateurs de la Société,
  de la caisse des ouvriers de l'État et des caisses d'allocations familiales (fiche
  `r-caisses-protectorat-fondation`), mois du n° 74 du *BEST* ; **à océriser ou relire** — loi
  n° 59-5 (JORT n° 3 de 1959 : le fichier local ne rend rien à l'OCR), loi n° 59-87, décret du
  29 mars 1956 (JORT n° 27 de 1956, lisible à l'image), loi n° 61-9 (fiche `r-ccps-devolution`).
- Le partage du recouvrement de la cotisation maladie après la loi n° 2017-47 reste à reporter
  dans `#tbl-caisses-carte` (texte lu par le livre « Prestations sociales »).
- **Contribution sociale de solidarité — histoire du taux tenue ici** (`#sec-caisses-financeur`),
  corrigée le 4 octobre 2026 d'après `css-verification.md` : un point (loi de finances pour 2018,
  art. 53) ; dispense permanente des seuls salaires et pensions ≤ 5 000 D nets depuis la loi de
  finances pour 2020 (art. 39) ; demi-point pour les revenus dont la déclaration échoit de 2023 à
  2025 (loi de finances pour 2023, art. 22, édition arabe seule, pp. 4062-4063), prorogé à 2026
  (loi de finances pour 2026, art. 87) ; la loi de finances pour 2025 ne touche pas la CSS des
  personnes physiques. Lecture administrative (retenue sur les sommes payées en 2023-2026) dite
  sans citation : notes communes 1/2023 et 1/2026 à verser (bibliographe, source publique à
  vérifier). Reste la date à retenir pour le tableau daté (openfisca-tunisia#474 et #475).
- **Étape 5 du plan, non faite** : chapitres « État et caisses » et « comptes dans la durée » à
  compléter par des séries à construire dans tunisia-data — comptes des organismes de sécurité
  sociale des comptes de la nation (S1314, 2001-2025, rupture de base à documenter), transferts
  et subventions de l'État aux caisses depuis 2016, états financiers de la CNRPS et de la CNSS
  après 2004 ; versements des caisses au budget (tableau A des lois de finances, 1985-2004).
- **Transitoire, à défaire après la première traduction du livre** :
  - `precis/ar/caisses/index.qmd` et ses partiels n'existent qu'après la passe de traduction qui
    suit la fusion ; d'ici là `build.sh`, `verifier.sh` et `translation-sync.yml` sautent le livre
    arabe (« traduction pas encore livrée »). Vérifier ensuite que le livre arabe rend.
  - trois liens symboliques `precis/fr/cotisations_sociales/figures/cnss_{regimes_1990_2004,
    assurances_sociales_1990_2004,atmp_pst_1995_2004}.py` → `../../caisses/figures/` : la
    traduction arabe actuelle du chapitre des cotisations importe encore ces modules. À retirer
    quand elle est retraduite.
  - trois entrées gardées dans les `references.json` ARABES seulement, parce que la traduction
    arabe en place les cite encore : `loi59-45` (cotisations), `loi86-86` (prestations),
    `loi2017-66-lf2018` (rémunérations publiques, doublon de `lf-2018`). À retirer après la
    retraduction de ces chapitres.
  - la traduction arabe orpheline de `_cadre_caisses.qmd` (PR #348) a été supprimée le 4 octobre 2026
    (la traduction du livre des caisses la remplace).
- **Bibliographie** : clés du livre rangées le 4 octobre 2026 — propres au livre dans
  `caisses/references.json`, partagées avec un autre livre dans le fonds commun. Doublons fusionnés
  dans le fonds commun : `loi86-83-lfr1986` → `loi-86-83-lfr-1986`, `loi87-83-lf1988` →
  `loi-87-83-lf-1988`, `loi2017-66-lf2018` → `lf-2018` (tableau `css_salarie` régénéré, seul
  l'identifiant de clé change). Zotero n'a pas encore de collection « Caisses de sécurité sociale » :
  `COLLECTION_TO_BOOK` (`sync_biblio.py`) et `COLLECTIONS` (`push_biblio.py`) la déclarent ; après
  fusion, l'action `ranger` du workflow `biblio-zotero.yml` la crée et y classe les items du volume.

- **Trois figures de la rétrospective CNSS 1990-2004 — fait le 3 octobre 2026**, mêmes vues (MD, % du PIB, % des ressources de la CNSS) : `#fig-cnss-assurances-sociales` (livre des caisses, `#sec-caisses-cnss-assurances-sociales` ; renvoi depuis `#sec-cot-maladie-longue-periode`, branche AS du RSNA, page 13 : forfait Santé publique, participation aux budgets des hôpitaux, compléments facturés par les hôpitaux publics, polycliniques, prestations en espèces, résultat ; colonne 1999 estimée hormis le total des ressources) ; `#fig-cnss-regimes` (livre des caisses, `#sec-caisses-cnss-regimes` ; renvoi depuis `#sec-cot-prive`, page 79 : taux de couverture et résultat de neuf régimes ; aucune valeur estimée ; RSA et non-salariés agricoles structurellement déficitaires, RSAA excédentaire sauf 2001 et 2004, aucune ligne de transfert entre régimes) ; `#fig-cnss-atmp-pst` (livre des caisses, `#sec-caisses-cnss-atmp-pst` ; renvois depuis `#sec-cot-at-longue-periode` et `#sec-cot-protection-sociale`, pages 54 et 56 ; détail AT/MP de 2000 estimé). Restent (TODO des chapitres, textes à obtenir, hors corpus JORT pour l'essentiel) : la base juridique du forfait accordé à la Santé publique, de la participation aux budgets des hôpitaux et de la facturation des compléments de soins à partir de 1996 ; le sens du sigle « C.A.O. » ; le contenu de la ligne « Provision Prest. & Mathématique » du régime AT/MP ; ces séries après 2004 (CNAM pour les AT/MP). Quand le classeur de tunisia-data#26 revient : relire les notes de lecture, qui citent des montants.
- **Cadre comptable et budgétaire des caisses — rédigé le 4 octobre 2026** (d'abord
  `cotisations_sociales/_cadre_caisses.qmd`, déplacé le même jour dans ce livre et découpé en
  `_statut_cadre.qmd`, `_comptes_regimes.qmd`, `_etat_caisses.qmd`, `_comptes_longue_periode.qmd`,
  `_chronologie.qmd` ; ancres `sec-cot-cadre-*` → `sec-caisses-*`, `tbl-cadre-*` → `tbl-caisses-*`), d'après la note
  `cadre-budgetaire-comptable-caisses.md` : statut, budget et contrôle des trois caisses ;
  comptabilité et réserves par régime ; dotations initiales et transferts de points ; concours
  des caisses au budget et financement par l'État (CSS, compte de diversification) ; chronologie
  des textes (`#tbl-caisses-chronologie`) ; silences des textes. Six fiches de recherche versées
  (`r-cnrps-tutelle-1976-1985`, `r-cnrps-organisation-apres-1989`, `r-norme-comptable-securite-sociale`,
  `r-cnam-transfert-reserves`, `r-caisses-placements-obligatoires`, `r-css-arretes-repartition`).
  Lacunes de la note (numérotation L1-L15), état du support contrôlé le 4 octobre 2026 sur le
  corpus local (couche texte des trois premières pages) :
  - **lisible** : loi n° 98-91 (JORT n° 89 de 1998, `1998/fr/Jo08998.pdf`) pour les modificatifs
    des art. 18-33 de la loi n° 60-30 (L2, en partie) ; décret n° 97-565 (JORT n° 27 de 1997)
    et décret n° 2002-2197 (JORT n° 83 de 2002, couche à décoder le cas échéant) (L12) ; arrêtés
    d'approbation des normes comptables de 1999 (n° 27), 2000 (n° 54), 2001 (n° 96), 2003
    (n° 97), 2007 (n° 70), 2008 (n° 10) et 2011 (n° 17) (L7) ; décret n° 2005-910 (JORT n° 26
    de 2005, pp. 844-850), dont le tableau de tutelle est à lire à l'image (L11) ;
  - **OCR** : décret n° 75-775 (JORT n° 72 de 1975) et décret n° 86-454 (n° 25 de 1986) pour la
    tutelle de la CNRPS (L1) ; modificatifs de la loi n° 60-30 antérieurs à 1996 (L2) ; lois de
    finances 1971-1975 et 1991 (n° 86 de 1990) pour les placements en bons d'équipement (L5 ;
    LF 1992 à localiser) ; loi n° 85-72 (n° 56 de 1985) (L13) ; décret n° 87-529 (n° 25 ou 30 de 1987, à départager) (L15) ;
    loi n° 68-8 sur la Cour des comptes (n° 11 de 1968) (L9) ;
  - **à obtenir** (hors JORT) : couverture des déficits agricoles par la trésorerie de la CNSS —
    états financiers, rapports du conseil d'administration, études du CRESS (L10) ; rapport de
    mission complet de la Cour des comptes sur la CNRPS (2006) (L9) ; affectation du produit de
    la majoration de 1975 après 1988, tableaux A des lois de finances 1985-2004 (L6) ;
  - **recherches** : L3, L4, L8 suivent leurs fiches dans `docs/recherches.yml`.
  - **L14 levée** : l'arrêté du 6 janvier 1987 est déjà lu et cité par le livre « Prestations
    sociales » (`arrete-1987-01-06-financement-pnafn`, contribution pour 1986) ; restent les
    arrêtés des années suivantes.
  Séries à construire avant de publier des montants (TODO du fichier) : comptes des organismes
  de sécurité sociale des comptes de la nation ; versements des caisses au budget (tableau A) ;
  transferts de l'État aux caisses depuis 2016, dont les sources restent à verser.

## Manques du précis — revue du 5 octobre 2026

Revue de ce que les sept volumes ne couvrent pas (sujets à établir sur les textes, rien n'est affirmé ici). Ordre de traitement décidé par l'humain : **1 et 2 d'abord** (documentation lancée le 5 octobre 2026), puis 5, 8, et 15 en dernier.

**Prioritaires**

1. **Prélèvements sur salaires autres que les cotisations** : taxe de formation professionnelle (TFP), contribution au FOPROLOS — assiette, taux, redevables, historique ; sans eux, le coin socio-fiscal des cotisations est incomplet. **En cours.**
2. **Salaire minimum et salaires négociés du secteur privé** : histoire du SMIG et du SMAG (montants, régimes 40 h / 48 h, revalorisations, décrets) ; conventions collectives sectorielles et leurs grilles ; accords salariaux périodiques UGTT-UTICA (privé) et UGTT-gouvernement (public). **En cours.**
3. Droit du travail déterminant les revenus : durée du travail, congés payés, heures supplémentaires, indemnités de licenciement, contrats précaires et sous-traitance, travail informel.
4. Politiques actives de l'emploi : programmes de l'ANETI (stages d'insertion, contrats aidés), primes à l'embauche, prises en charge de cotisations patronales ; protection contre la perte d'emploi (aujourd'hui effleurée).
5. La compensation (Caisse générale de compensation : produits de base, carburants, électricité, transport) — **volume IX créé le 6 octobre 2026** (`precis/fr/compensation/`) ; lacunes à la rubrique « La compensation » ci-dessous.

**Fiscalité**

6. Droits d'enregistrement et de timbre ; fiscalité des mutations immobilières.
7. Droits de douane.
8. Dépenses fiscales et régimes d'incitation (code d'incitation aux investissements, loi de 2016, entreprises totalement exportatrices, développement régional) — **chapitre créé le 6 octobre 2026** (`fiscalite/_depenses_fiscales.qmd`) ; lacunes dans la section « Fiscalité » ci-dessus.
9. Fiscalité de l'épargne et du capital : retenues libératoires sur les revenus de capitaux mobiliers, plus-values mobilières, épargne exonérée.
10. Taxes affectées et contributions exceptionnelles (contribution conjoncturelle, contribution au budget de l'État de 2014, FODEC, vignette).

**Social et secteur public**

11. Régimes spéciaux du secteur public (militaires, forces de sécurité, magistrats, membres du gouvernement), recrutement, départs anticipés et plans de départ volontaire.
12. Couverture santé au-delà de la CNAM : filières, ticket modérateur, mutuelles et assurance complémentaire de groupe.
13. Logement social (FOPROLOS, programmes, prêts aidés), en lien avec le foncier.
14. Transferts en nature et aides à l'éducation (bourses, cantines, allocation de rentrée scolaire, handicap).

**Transversal**

15. Synthèse de la redistribution par décile (impôts, cotisations, prestations, subventions), dans l'esprit des études d'incidence de type CEQ (dépôt `ceq-tunisie`).

## Allègement du juridique et de l'administratif — chantier, non urgent (5 octobre 2026)

Ligne éditoriale rappelée par l'humain : le précis vise l'**impact économique, distributif et budgétaire**, l'**évolution sur le temps long** et les **ruptures de réforme** ; on retient d'un texte sa **date, sa valeur et sa source**, sans les détails administratifs sans impact (modalités de déclaration, de recouvrement, procédures). Les chapitres déjà écrits en contiennent beaucoup (par exemple le recouvrement des impôts locaux dans le volume VII). Chantier à mener plus tard, **sans forcément réécrire le texte** : réduire la visibilité de ces sections (encadrés repliés, niveau de titre plus bas) ou les **repousser en annexe** du volume. Une passe par volume, à décider avec l'humain. Les nouveaux chapitres appliquent la règle dès leur rédaction.
## Le marché du travail

### Annexe « Les conventions collectives, branche par branche » (8 octobre 2026, premier jet ; repris le 9 octobre 2026 ; grilles entières le 9 octobre 2026)

`precis/fr/marche_travail/_annexe_conventions.qmd` (`#sec-mt-cc-annexe`), déclarée dans les
`appendices` du `_quarto.yml` français, avant le glossaire. Décision du propriétaire du 8 octobre
2026 (canevas, « Destination »). Décision du propriétaire du 9 octobre 2026 : **l'annexe ne
reproduit plus les grilles** — ni tableaux par case, ni tableaux aux dates repères. Elle garde,
par branche, la création, la description de la grille, la figure en escalier et le registre des
avenants, et renvoie pour chaque grille à sa vue en tableau sur le site de la base législative
(`…/parameters/<nœud de la grille>/table/`). `scripts/generate_conventions_collectives_tables.py`
(appelé par `generate_marche_travail_tables.py`, donc gardé par le contrôle de fraîcheur) parcourt
`marche_travail/conventions_collectives` d'`openfisca-tunisia` sans nommer de branche ni de
grille, et écrit `tables/cc_index.yml`, `tables/cc_<branche>_grilles.liens.yml` (contrôlé par
`scripts/verifier_liens_base_legislative.py`) et une série par grille tracée,
`_seriescache/cc-grille-<branche>-<grille>.csv`. La grille d'une case se déduit des chemins : le
nœud le plus profond commun aux cases de même grandeur et de même unité de la branche (`grilles`).
La création de chaque convention et la suite des avenants viennent des notes, non des paramètres.

**État au 9 octobre 2026, version 0.128 du modèle** (borne `VERSION_MINIMALE` relevée à 0.128) :
trois branches, cinq grilles, toutes tracées — textile horaire (7 lignes × 21 colonnes, 147
cases) et mensuelle (18 × 21, 378) ; bâtiment, personnel occasionnel (9 lignes, puis 10 depuis
2008 ; 11 cases en tout) et personnel
administratif et technique (19 × 11, 209) ; assurances (22 × 14, 308) —, soit 1 053 cases,
29 148 valeurs et **144 cases vides** (illisibles sur le fascicule : 127 dans la grille mensuelle
du textile, 16 dans la grille mensuelle du bâtiment, 1 dans les assurances). L'index ne liste
plus les cases une à une : il porte, par grille, ses comptes, sa période et les fiches de sa case
du bas et de sa case du haut ; la série d'une grille ne porte que ces deux cases.

Règles écrites dans le générateur (fonctions pures, testées dans
`tests/test_conventions_collectives.py`) :

- **le bas et le haut se choisissent par grille, à sa dernière date publiée** (`bas_et_haut`),
  parmi les cases qui y ont une valeur en vigueur : une ligne close avant (l'ouvrier hautement
  qualifié du bâtiment, 2008) ou une case illisible à cette date ne concourt pas ;
- **une colonne sans rang parmi des colonnes numérotées n'est pas un échelon** (`hors_rang`) : le
  bas de la grille mensuelle du textile est l'échelon 1 (confirmation) de la catégorie 1A, non
  la colonne de stage, égale à l'échelon 1 jusqu'en 2007 et plus basse ensuite ;
- **trois espèces de valeur vide** (`etat_grille`), distinguées par la forme de la grille : grille
  non publiée (aucune case n'a de valeur à la date), ligne close (plus aucune date ensuite), case
  vide parce qu'illisible (les autres) ;
- **une grille n'a sa courbe que si elle est courante** (`marque_tracees`) : au moins trois dates
  publiées, et pas de grille de même unité qui commence à sa date de clôture ou après. Sinon
  l'annexe la mentionne, avec sa période et son lien (`autres_grilles`) ;
- **la vue en tableau d'un nœud n'existe sur le site qu'en deçà de 200 cases**
  (`PLAFOND_VUE_TABLEAU`) : l'adresse `…/table/` des trois grandes grilles répond 404. Elles ont
  un lien par ligne (`liens_grille`) — 18, 19 et 22 liens —, rendus en une ligne sous la figure.

Ce qui lui manque :

- **régénérer quand la 0.129 du modèle sera publiée** (openfisca-tunisia, PR n° 490, ouverte le
  9 octobre 2026) : elle ajoute aux assurances deux nœuds frères de `salaire_base` —
  `salaire_base_avant_1993` (1975-1992, clos au 1er juin 1993) et
  `salaire_base_avant_1993_grille_1_de_1990` (une seule date). Le générateur y est prêt, et un
  test en imite la forme : la première sort « antérieure », la seconde « peu de dates », aucune
  ne fournit de bas ni de haut, et `cc.autres_grilles("assurances")` — déjà appelé dans l'annexe —
  les mentionnera avec leur période et leurs liens (un par ligne : 264 cases chacune). À faire
  alors : relever la borne, régénérer, relire le libellé de leurs liens (il vient des
  `short_label` des deux nœuds) et écrire dans la section des assurances ce que sont ces grilles
  (hors indemnité complémentaire provisoire) ; le tableau `@tbl-mt-cc-grilles-hors-series` du
  chapitre pourra alors renvoyer à l'annexe pour les assurances ;
- **les 144 cases vides** : à relire sur un meilleur exemplaire des fascicules — textile mensuel,
  grilles de 1994 (1 case), 1999 (42), 2000 (30), 2002, 2003 et 2004 (18 chacune, l'échelon 18
  des dix-huit lignes) ; bâtiment mensuel, grilles de 1996 (7), 1998 (5), 2001, 2002, 2003 et
  2004 (1 chacune) ; assurances, grille de 1996 (1). Le compte de l'annexe est calculé : il
  baissera à la régénération quand une case sera lue en amont ;
- **la vue en tableau des grandes grilles** : le site de la base législative ne rend pas en un
  tableau un nœud de 200 cases ou plus ; si ce plafond est levé en amont (visualiseur des
  paramètres), `PLAFOND_VUE_TABLEAU` se relève et chaque grille retrouve un lien unique ;
- **une case tracée vide avant la dernière date publiée** : `cc.figure` la refuse par une erreur
  explicite — le composant `figtools.figure_escalier` ne sait ni commencer un trait par une
  valeur vide ni interrompre la vue en dinars constants (il relierait les années de part et
  d'autre). Aucune case tracée n'est dans ce cas (les dix n'ont de vide que le 1er janvier
  2026) ; à traiter dans `figtools` le jour où cela arrive ;
- **deux grilles de même unité sous une même grandeur** ne se distingueraient pas (`grilles`) :
  aucune branche versée n'en a ;
- **les indemnités** (transport, présence, assiduité) : relevées en partie dans les notes, pas
  dans les paramètres ; le générateur les prendra sous un nœud frère de `salaire_base` ;
- **les autres branches** : commerce, industrie hôtelière, mécanique et électricité d'abord
  (canevas, « Par où commencer »). Une branche versée en amont a son index et ses liens à la régénération,
  mais sa section (création, grille, avenants) reste à écrire dans l'annexe ;
- **textile et bâtiment avant 1990** : sentence arbitrale de 1983, avenants n° 2 et n° 4 du textile,
  avenants n° 1, n° 2 et n° 4 du bâtiment — sans clé bibliographique, grilles non établies ;
  fascicules de l'édition française présents au corpus, à ouvrir ; grilles de 1990-1992 hors
  indemnité complémentaire provisoire (données au chapitre, non à l'annexe) ; pages des arrêtés et
  des avenants n° 6 à 18 dans l'édition arabe ;
- **bâtiment, avenant n° 16** : second exemplaire du JORT n° 132 du 2 décembre 2022 à obtenir. Les
  deux grilles entières des 1er décembre 2021, 1er janvier 2023 et 1er janvier 2024 — 220 cases
  par date — sont lues sur la reproduction d'un site tiers, sans lien ; l'annexe le dit pour les
  deux grilles (section, note de lecture et réserve de chaque figure) ;
- **assurances** : application du décret n° 2026-68 à la branche non établie. Les dix-huit clés
  `cc-assurances-*` — dont `cc-assurances-avenant11-grille-2015`, citée au registre
  `#r-cc-assurances-grille-2014` — sont tenues en double, à l'identique, dans les
  `references.json` du marché du travail et des rémunérations publiques (FR et AR) ;
  `tests/test_references_communes.py` contrôle que toute clé commune à ces deux livres y a la
  même notice (9 octobre 2026 : la notice `cc-assurances-avenants-10-11`, corrigée dans le seul
  volume des rémunérations publiques, a été recopiée). D'autres clés communes à d'autres
  volumes divergent, hors du contrôle : `loi86-106-lf1987`, `loi57-73`, `loi-2007-70-lf-2008`,
  `lfc-2012`, `ins-annuaire` ; en arabe aussi `loi59-45` et `loi86-86` — à réconcilier avec le
  bibliographe. La section
  `#sec-marche-controle-assurances` de ce volume, à laquelle l'annexe renvoie pour la chaîne des
  avenants, dit encore la grille de 2014 « annoncée, non imprimée » : correction attendue de la PR
  qui y reporte les relectures ;
- **côté arabe** : l'annexe n'est **pas** déclarée dans `precis/ar/marche_travail/_quarto.yml` —
  à faire à la livraison de sa traduction. L'index et les liens arabes sont engendrés, mentions
  en arabe, mais les noms des branches, des grilles et des cases y restent en français (les
  `short_label` du modèle n'existent qu'en français) : à trancher avec le relecteur de l'arabe,
  comme l'intitulé arabe du renvoi (`INTRO_BASE` de `figures/conventions.py`,
  `cases` de `MOTS` dans le générateur) et les mentions arabes posées le 9 octobre 2026 avec les
  grilles entières (`MOTS` de `figures/conventions.py` : en-têtes des deux tableaux, « سطرًا
  بسطر », « الخانات الفارغة » ; `cases_ligne` du générateur) ;
- **figures** : une figure en escalier par grille tracée, par le composant commun, en dinars
  courants et en dinars de 2025 — cinq figures. Le bas et le haut viennent de l'index. Les
  étiquettes `fig-mt-cc-annexe-textile` et `-batiment`, que cite le chapitre, restent celles des
  grilles horaires ; les grilles mensuelles ont `-textile-mensuelle` et `-batiment-mensuelle`.
  Dans la figure des assurances, les douzième et treizième échelons de l'échelle 21 ne se lisent
  qu'à la vue de la ligne. Une grille tracée sans figure déclarée dans l'annexe fait échouer le
  rendu (`autres_grilles`). Pas de rapport au SMIG dans l'annexe ;
- **prose de l'annexe** (9 octobre 2026) : ni compte ni montant saisi — les nombres de lignes, de
  colonnes, de cases, de dates d'effet et de cases vides sont au tableau `@tbl-cc-annexe-grilles`
  et dans la phrase des cases vides, engendrés depuis l'index ; les montants ne sont que dans
  les figures. Le tableau d'ouverture a une ligne par grille : création de la convention, grille
  et unité, cases tracées. La forme de chaque grille (lignes, colonnes, cases, et la date où
  elle change) est une phrase engendrée (`cc.formes_branche`, d'après `formes` de l'index) : les
  totaux écrits en toutes lettres — sept, dix-sept ou dix-neuf catégories, onze, douze ou
  quatorze échelons, vingt et une échelles — sont retirés des descriptions. Restent à la main
  les noms et les numéros qui désignent (catégories I à IV-2, échelles 1 à 21, treizième et
  quatorzième échelons créés par l'avenant n° 5) et les registres repliés, qui disent ce que
  chaque texte fixe. Les tableaux des avenants du textile et du bâtiment restent
  faits main, avec leur titre de bloc et leurs bornes : à engendrer quand les avenants seront
  versés en amont ;
- **chapitre** (9 octobre 2026) : le tableau replié `@tbl-mt-cc-grilles` (62 grilles, 1974-2026)
  est retiré ; la section `#sec-mt-cc-smig` renvoie à l'annexe pour 1994-2026 et ne garde, replié,
  que `@tbl-mt-cc-grilles-hors-series` — les six grilles que l'annexe ne porte pas (origine de
  1974, 1990-1992 hors indemnité complémentaire provisoire), engendré depuis la série
  `tunisia-data` du salaire d'entrée (`tableau_cc_grilles_hors_series`). Le rapport au SMIG de
  chaque grille, le haut de la grille et les précisions de lecture (date « à titre
  exceptionnel » du 15 juin 2005, date du fascicule n° 81 de 2011 à confirmer) restent à
  l'onglet « Données » de `@fig-mt-cc-salaire-entree` ; la date du 15 juin 2005 est aussi dite
  dans l'annexe. À verser en amont : les grilles de 1974 et de 1990-1992, pour que ce dernier
  tableau rejoigne l'annexe.
- **largeur des tableaux repliés** (mesure du 9 octobre 2026, fenêtre de 1 300 px) : les deux
  tableaux faits main des avenants (`tbl-cc-textile-avenants`, `tbl-cc-btp-avenants`) tiennent
  dans leur bloc — largeurs de colonnes à proportion des dates insécables et classe `.sm` de la
  légende (marges de cellule resserrées), la somme des largeurs minimales dépassant sinon le
  bloc. Reste l'inventaire des 57 branches du chapitre (`tbl-mt-cc-inventaire`), qui dépasse de
  142 px ; aucun dépassement à 1 800 px. À régler dans le thème commun (`precis/legendes.scss`,
  défilement horizontal du bloc replié), ce qui fait rendre tous les livres.
- **figure en escalier, dernière année écrite deux fois** (9 octobre 2026) : corrigé dans
  `figtools.fig_escalier` — une date d'effet au 1er janvier de la dernière année tracée ne
  reçoit plus une seconde graduation. Les figures des taux de TVA et des déductions pour
  charges de famille, sans date d'effet à cette place, sortent à l'identique.

Volume créé le 5 octobre 2026 (branche `docs/marche-travail-volume`), sept chapitres : présentation,
notions, institutions, salaire minimum, conventions collectives, négociations salariales, longue
période. Notes documentaires : `docs/notes/marche-travail-smig-smag.md`,
`-conventions-collectives.md`, `-negociations.md` (partie privée). Le livre arabe est déclaré
(`precis/ar/marche_travail/_quarto.yml`) et sauté tant que la traduction n'est pas livrée.

Huitième chapitre ajouté le 6 octobre 2026 (branche `docs/marche-travail-politiques-emploi`) :
« Les politiques de l'emploi » (`_politiques_emploi.qmd`), placé après la longue période du
salaire minimum, qui clôt le bloc des salaires ; note documentaire
`docs/notes/marche-travail-politiques-emploi.md`. Il porte sa propre longue période : figure des
dotations 1987-2008 (série `bct-programmes-emploi-dotations`, fonction `vues_dotations_emploi` de
`figures/marche_travail.py`), tableaux budgétaires 2011-2025, décomptes administratifs 2009-2013,
rapports de la Banque mondiale et évaluations, en blocs séparés.

Chapitre converti le 7 octobre 2026 (branche `chantier/conversion-politiques-emploi`) selon les
principes « ruptures au premier plan, détail replié » : vue d'ensemble ; mise en place
(1967-1988) ; cinq grandes réformes (1993, 2000, 2009, 2012, 2019 complétée en juin 2023) ; bilan
et état du droit daté de juin 2023 (six programmes) ; quinze sections de programme rangées par
type de soutien, chacune avec son registre replié ; longue période inchangée. Plan :
`docs/notes/marche-travail-politiques-emploi-plan-architecte.md` ; complément documentaire :
`docs/notes/marche-travail-politiques-emploi-objets-des-reformes.md`, dont les vingt corrections
sont appliquées. Le chapitre passe de 10 936 à environ 30 000 mots, dont 9 000 dans vingt et un
blocs repliés.

Chapitre du salaire minimum converti le 8 octobre 2026 (branche
`chantier/conversion-salaire-minimum`) selon les mêmes principes, sans fiche d'architecte : vue
d'ensemble ; mise en place (1961-1974 : minima par zone, institution du SMIG et du SMAG) ; cinq
ruptures dans l'ordre des dates (hausses uniformes de 1977-1980, deux taux horaires en 1981,
intervalles sans hausse, effets rétroactifs, décrets pluriannuels) ; état du droit en 2026
(montants, composition du SMIG). Quatre registres repliés portent les références de loi
(trente lignes) ; les tableaux engendrés du SMIG et du SMAG sont repliés, celui des indemnités
spéciales reste au premier plan. La longue période, d'abord chapitre à part, est devenue la
dernière section du chapitre (`#sec-mt-longue-periode`) ; `_longue_periode.qmd` n'existe plus.
Environ 1 800 mots au premier plan et 1 400 dans six blocs repliés, hors tableaux engendrés et
hors longue période.

Les quatre chapitres courts restants convertis le 8 octobre 2026 (branche
`chantier/conversion-marche-travail-reste`), sans fiche d'architecte et sans matière nouvelle
hors des notes documentaires. Notions : chapitre de définitions, une section par notion qui
définit d'abord ; références laissées sur place (sept appels à des textes de loi, pour
l'essentiel des citations mot pour mot), pas de domicile unique. Institutions, conventions,
négociations : domicile unique au niveau du chapitre, un registre replié par chapitre (quinze,
seize et quatorze lignes, colonne « Portée »). Institutions : code de 1966 et changements de
1968, 1973 et 1996 ; organisations et commissions ; fondement des décrets de 2026. Conventions :
convention cadre de 1973 ; trois étages ; conventions de branche, avec un tableau par période
et, à la conversion, un compte d'« au moins 64 » agréments et une liste repliée des branches de
1974 à 1977, remplacés depuis (voir « Conventions — enrichissement du 8 octobre 2026 »). Négociations : tableau de tête « qui fixe la
hausse », rounds de 1973 à 2023, accords-cadres, hausse fixée par décret en 2026. Une erreur
corrigée au passage : le chapitre des institutions annonçait « quatre » dispositions du code et
en donnait trois.

À faire, avec l'état des sources :

- **Salaire minimum — état du droit au premier plan** : les montants en vigueur ne se lisent que
  dans les tableaux repliés. À engendrer : un tableau court de l'état du droit à des dates repères
  (SMIG des deux régimes et SMAG, dont les paliers de 2026, 2027 et 2028), par `tableau_a_la_date`
  (TODO rédacteur dans `_salaire_minimum.qmd`, `#sec-mt-montants`) ; il demande un snapshot
  nouveau dans `tables/`.
- **Salaire minimum — tableau du SMAG** : la clé `decret2024-420` est versée (8 octobre 2026) ; le
  tableau engendré cite encore ce décret par un lien brut : à faire citer par le générateur.
- **Glossaire — indemnité complémentaire provisoire** : le terme arabe est désormais celui du
  décret n° 81-437 (المنحة الإضافية المؤقتة). La même expression française nomme un élément de
  rémunération publique des décrets de 1982, que les chapitres arabes rendent par
  منحة تكميلية وقتية : deux entrées ou un qualificatif, à trancher avant la reprise de la
  traduction. Terme arabe de l'indemnité de cherté de vie (décret n° 71-164) à fixer par un
  arabophone.
- **Salaire minimum — dates d'effet non établies** : loi n° 66-27, décret n° 73-247, décret
  n° 74-493, loi n° 96-62 et article 15 de la loi de finances pour 2026 figurent aux registres
  sans date d'effet (tiret) ; textes lus, date d'exécution à calculer par le documentaliste.
- **Conventions — enrichissement du 8 octobre 2026** (branche `chantier/conventions-collectives-fond`,
  note `marche-travail-conventions-collectives-fond.md`) : le compte des agréments est corrigé
  (61 agréments de conventions sectorielles dans 56 branches, une 57e connue par ses seuls
  avenants ; borne basse) et sourcé par deux séries de `tunisia-data` ; figure des agréments par
  année (`fig-mt-cc-agrements`) et inventaire engendré des 57 branches (`tbl-mt-cc-inventaire`,
  qui remplace la liste faite main des branches de 1974-1977) ; section nouvelle « Ce que les
  conventions ajoutent au SMIG » (`#sec-mt-cc-smig` : salaire d'entrée du textile et du
  bâtiment-travaux publics, 1974-2026, par segments) ; section « La couverture, d'après
  l'Organisation internationale du travail » (`#sec-mt-cc-couverture`, 2010-2019). Clos : le
  compte « au moins 64 » et les nombres annuels d'avenants sans référence ; l'absence de toute
  source de couverture.
- **Conventions — grilles de 1996 à 2010 et bâtiment après 2019 : clos le 8 octobre 2026.** La
  série du salaire d'entrée est continue de 1994 à 2026 pour le textile (avenants n° 5 à 18) et de
  1996 à 2024 pour le bâtiment (avenants n° 5 à 16) ; note
  `marche-travail-conventions-collectives-grilles-1996-2022.md`. L'avenant n° 16 du bâtiment est lu
  sur une reproduction, par un site tiers, des pages de l'édition arabe : fiche
  `r-btp-avenant-16-grilles` résolue ; le fascicule (n° 132 de 2022) et un second exemplaire
  restent à obtenir. Un avenant postérieur n'est pas identifié : fiche `r-btp-avenant-17`
  (sommaires arabes de 2023-2026 à parcourir).
- **Conventions — grilles restant à établir** : textile, sentence arbitrale de 1983 et avenants
  n° 2 (1989) et n° 4 (1993) ; bâtiment, avenants n° 1, 2, 4 et suite du n° 3 (1991-1992) — scans
  français au corpus, OCR à lancer. Montant de l'indemnité complémentaire provisoire (décrets
  n° 81-437 et n° 82-501, au corpus) pour comparer 1983-1993 au SMIG.
- **Conventions — hauts de grille, pages et points à confirmer : clos le 8 octobre 2026** par la
  relecture à l'image (`marche-travail-conventions-collectives-relecture-2026-10-08.md`) : douze
  hauts de grille lus, six points du textile confirmés sans correction, pages de 1996 à 2004
  confirmées, date d'effet des deux conventions d'origine au 1er juin 1974 (articles 53 et 58).
  **Restent** : la raison de la date d'effet du 15 juin 2005 (texte de l'avenant n° 9 du textile,
  au corpus, en image) ; un rappel éventuel des grilles d'origine depuis le 1er juin 1974 ; le
  régime horaire du textile ; la date du fascicule n° 81 de 2011 (bâtiment) ; l'avenant n° 16 du
  bâtiment sur le fascicule lui-même (n° 132 de 2022, **à obtenir**) ou sur un second exemplaire ;
  les grilles entières des deux branches (seuls le bas et le haut sont établis). Les dix clés des
  avenants de 1996 à 2009 et de 2022 sont versées sans URL (adresses pist.tn de l'édition arabe à
  vérifier ; pist.tn ne sert pas le n° 132 de 2022) ; l'intitulé français des neuf premières est à
  confirmer sur les visas.
- **Conventions — autres branches** : commerce, hôtellerie, mécanique et électricité (conventions
  d'origine en scans français au corpus ; avenants depuis 1996 dans l'édition arabe). Coût et
  fascicules dans la note, § D.
- **Conventions — hausse par décret de 2026** : aucun texte ne publie les grilles issues du décret
  n° 2026-68, ni ne dit comment sa hausse se combine avec la grille du textile déjà fixée au
  1er janvier 2026 ; le chapitre pose les deux faits sans conclure (fiche
  `r-grilles-decret-2026-68` ; à parcourir : édition arabe de 2026, circulaires du ministère des
  affaires sociales).
- **Conventions — couverture** : la série de l'OIT ne précise ni son producteur national ni sa
  méthode (fiche de métadonnées par pays d'ILOSTAT à obtenir) ; aucun nombre de salariés couverts
  par convention sectorielle, par branche (annuaires statistiques du ministère des affaires
  sociales, non ouverts ; la rubrique « conventions » de son site porte sur les conventions
  internationales).
- **Conventions — inventaire** : rattachement des avenants aux branches fait d'après les mots des
  intitulés, à relire ligne à ligne (quatre doubles comptes signalés au tableau) ; avenants de
  1996-2012 et de 2022 à compter sur l'édition arabe ; année du fascicule de la convention des
  constructeurs et concessionnaires de véhicules (n° 14, arrêté du 21 décembre 1983) à contrôler.
- **Conventions — clés manquantes** : seuls les arrêtés d'agrément de 1969, de 1971, du 29 août
  1974 et du 4 février 2025 ont une clé dans `references.json` ; les autres agréments de
  l'inventaire sont donnés par leur fascicule, sans clé (TODO bibliographe dans
  `_conventions.qmd`). Les clés `avenants-1990-textile-btp` et `avenants-2014-textile-btp`
  réunissent chacune deux arrêtés : à scinder, dans `tunisia-data` d'abord (le catalogue les cite
  ainsi). Arrêtés au corpus.
- **Négociations — matière de la note non reprise** : la chronologie des rounds déduite des
  décrets d'augmentation du secteur public (1993-1995 à 2011-2012) et la position de l'UGTT sur
  la fixation par décret de 2026 ne sont pas au chapitre, faute de clés de référence ; le décret
  n° 2018-674 (secteurs non couverts) n'a pas de clé non plus (TODO bibliographe dans
  `_negociations.qmd`).
- **Chapitres annoncés, non écrits** : temps de travail et congés ; rupture du contrat de travail.
  À ajouter au `_quarto.yml` français et arabe à leur rédaction.
- **Politiques de l'emploi — chapitre arabe à déclarer** : `_politiques_emploi.qmd` est déclaré au
  `_quarto.yml` français seulement. À la livraison de la traduction, l'ajouter à la main à
  `precis/ar/marche_travail/_quarto.yml` (en dernier chapitre, après `_negociations.qmd`) et rendre le livre arabe :
  la figure y est déjà bilingue (`figures/` est un lien vers le répertoire français).
- **Politiques de l'emploi — dépense exécutée du Fonds national de l'emploi** : établie pour
  aucune année. Le chapitre ne donne que des dotations (BCT, 1987-2008), des prévisions de lois de
  finances (2011-2020), des dotations de rapports sur le budget (2022, 2024, 2025) et des excédents
  reversés (2016-2018, celui de 2016 sous réserve : intitulé de la colonne de la loi n° 2018-49 à
  confirmer). À obtenir : rapports annuels de performance de la mission (gbo.tn, adresses non
  trouvées), tableaux annexes des lois de règlement (images, au corpus, à dépouiller), Cour des
  comptes. Prévisions du Fonds avant 2011 et depuis 2021 : tableaux des lois de finances au
  corpus, à relire à l'image ; pages des tableaux 2012-2020 connues à une page près. PAP 2024 et
  2025 (édition arabe) récupérés, tableaux à dépouiller.
- **Politiques de l'emploi — bénéficiaires** : années entières 2014 à 2022 absentes (rapports
  annuels de l'ANETI et de l'ONEQ non obtenus ; `emploi.tn` ne répond pas, captures d'archive
  partielles) ; seules des périodes partielles sont données (neuf mois 2016-2017, premier semestre
  2023-2024). Contrats signés et bénéficiaires de 1988 à 2008 : donnés en prose par chaque édition
  du Rapport annuel de la BCT (au dépôt `tunisia-data`, lisibles), non dépouillés. Annuaires de
  l'INS non parcourus.
- **Politiques de l'emploi — études récupérées, non dépouillées** (donc non citées) : ONEQ, suivi
  du SIVP (2009), évaluation du service civil volontaire (2010), évaluation du « PC50 » (2016),
  rapport du premier semestre 2013, bulletin du premier trimestre 2018 ; Banque mondiale,
  *Building Effective Employment Programs…* (2013), *Breaking the Barriers to Youth Inclusion*
  (2014), note « The AMAL Program » (2011). À relever aussi : résultats du contrat de service civil
  et tailles d'échantillon de l'étude ONEQ-OIT de 2023 ; chiffres de Premand et al. (2012), dont
  seuls la méthode et le résultat qualitatif sont écrits. Non obtenue : OCDE (2015), *Investir dans
  la jeunesse : Tunisie*. Les PDF sont dans `tunisia-data/data/raw/emploi/`, répertoire **non
  ignoré par git** : à trancher par l'humain avant tout `git add` dans ce dépôt.
- **Politiques de l'emploi — chiffres de 1981 à 1993 à relire** : subventions, indemnités, durées,
  âges et taux des
  décrets n° 81-1220, 87-1190, 88-715, 88-733 et 93-1049, lus sur des fascicules sans couche texte
  fiable ; le chapitre les donne dans un tableau à part, replié, sous réserve
  (`tbl-mt-pe-montants-1981-1993`), et le dit en clair dans la mise en place et dans les sections
  du contrat emploi-formation et du stage d'initiation. L'objet de ces textes, leurs intitulés et
  leurs abrogations sont établis (lus à l'image, complément du 7 octobre 2026) ; seuls les chiffres
  restent à relire à l'image, au corpus. De même pour les indemnités de FORSATI (décret
  gouvernemental n° 2016-904, colonnes entrelacées ; décret n° 2019-542, art. 26 à 30), laissées
  hors du texte. Les lignes de crédit imputées sur le Fonds par les lois de finances 2022 à 2026
  ne sont connues que par les intitulés des notices : à relire avant d'être écrites (seul l'art. 14
  de la loi de finances pour 2026, qui élargit l'objet du Fonds, est établi et écrit). Jour d'effet
  des deux textes de 1981 toujours non établi (fascicules datés de deux jours). **Clos** : date
  d'effet du décret gouvernemental n° 2019-542 (2 juillet 2019, dérivée du dépôt du 27 juin lu à
  l'édition arabe) ; pages du décret n° 2023-461 (1552-1558) ; fin du contrat emploi-formation
  (déduite, 16 février 2009).
- **Politiques de l'emploi — lacunes ouvertes par la conversion du 7 octobre 2026** (toutes dites
  « non établi ici » dans le chapitre, avec un TODO documentaliste dans la section) :
  - *terme du relais du maintien dans l'emploi* : la mesure du décret n° 2009-1052 finit le 30 juin
    2009 ; l'État la reprend le 1^er^ juillet (loi n° 2009-35, lue) ; pour dater la fin du relais,
    lire la loi n° 2009-82 (JORT n° 1 de 2010) et le décret-loi n° 2011-9 (JORT n° 14 de 2011),
    au corpus, clés versées (`loi2009-82`, `dl2011-9`), non citées tant qu'elles ne sont pas lues ;
    contenu d'origine de la loi n° 2008-79 à lire aussi (sans clé) ;
  - *article 43 d'origine du code d'incitation aux investissements* (loi n° 93-120) : public et
    taux non établis ; une modification de l'article 43 bis entre 1997 et 2004 n'est pas
    recherchée ; à lire au corpus ;
  - *montants du contrat de réinsertion de 2023* : décret n° 2023-461, art. 11 ter à 11 sexies
    (indemnité, avantage de l'entreprise), et articles 31, 41, 43, 44, 45, 48, 49 et 52 récrits :
    couche texte fiable, à relever ;
  - *décret n° 2002-13* (modifie le décret n° 98-868) : seul l'intitulé est connu ; clé
    `decret2002-13` versée, non citée ; fascicule au corpus (JORT n° 4 de 2002), à lire ;
  - *financeur des stages d'initiation et du contrat emploi-formation de 2003 à février 2009* :
    la loi de finances pour 2003 (art. 12) les retire des dépenses du fonds de la formation ;
    aucun texte lu ne dit qui les paie ensuite ; à chercher dans les lois de finances 2003-2009
    (tableaux des comptes spéciaux) et les rapports de la Banque centrale ;
  - *sort de l'article 22 de la loi de finances pour 2005* (contrat de réinsertion dans la vie
    professionnelle) après le décret n° 2009-349 ; contenu des décrets n° 2001-1722, n° 2006-2990
    et n° 72-58, connus par leurs seuls intitulés ; articles 16 et 17 du décret n° 2009-349
    modifiés par le décret n° 2010-87 ; objet de l'article 39 § 2 modifié par le décret n° 2011-98 ;
    art. 22 du décret n° 2019-542 ; plafond de la contribution patronale du contrat d'initiation ;
  - *figure* : frise des réformes (`fig-mt-pe-frise`) non faite (TODO rédacteur dans le chapitre) ;
    le tableau `tbl-mt-pe-reformes` en tient lieu ;
  - *bibliographie* : les entrées `lf-2005` et `lf-2010` du fonds commun portent p. 3440 et
    p. 3919, qui sont les pages d'autres articles (49-50 ; 39-40) ; les registres du chapitre
    donnent la page de chaque article cité (3433, 3434 ; 3914, 3923). Champ de page des deux
    entrées à revoir (bibliographe) ; `dafflon-2021-budget-local` (type non pris en charge)
    interrompt le dry-run Zotero de tout le lot, et `minfin-cnf-2013-forfait` perd sa langue à
    l'aller-retour.
- **Politiques de l'emploi — textes non identifiés** (fiches de `docs/recherches.yml`) : texte
  instituant le FIAP (`r-fiap-texte-fondateur`) ; barème du SIVP entre 1993 et 2009
  (`r-sivp-bareme-1993-2009`) ; arrêtés des chèques de 2012 (`r-d2012-2369-arretes-cheques`) ;
  texte fondateur des chantiers (`r-chantiers-regionaux-texte-fondateur`) ; modificatif du décret
  gouvernemental n° 2019-542 postérieur à juin 2023 (`r-d2019-542-modificatifs-apres-2023`, fiche
  versée le 7 octobre 2026, couverte jusqu'au 6 octobre 2026). Textes connus par leur
  seul intitulé : décret n° 2003-564 (ANETI), décret-loi n° 2022-78, arrêté du 8 août 2017,
  décret n° 2025-459, décrets n° 93-1354, 97-1938, 97-1930, 2001-1722, 2002-13, 2006-2990,
  2007-1237, 72-58 ; loi n° 2008-79. Les décrets n° 94-494 et n° 98-868 sont désormais lus (art. 1
  à 5 et 1 à 4) et cités au registre des prises en charge.
- **Politiques de l'emploi — bibliographie** : pas de clé pour les éditions 1988-1990, 1997 et
  2000 du Rapport annuel de la BCT (la clé générique `bct-ra` les couvre dans la figure), ni pour
  le décret n° 2000-2279, la loi n° 91-4, l'arrêté du 8 août 2017, le décret n° 2025-459, le
  décret n° 2024-182 et l'arrêté conjoint du 16 août 2024 (qui visent le décret de 2019 modifié en
  2023 : non écrits dans le chapitre faute de clé), les décrets n° 2006-2990 et n° 2005-1857, la
  loi n° 2008-79 ;
  `loi88-60-lfc1988` (restructuration des offices en 1988) n'existe qu'au volume « Les caisses » ;
  `loi74-101-lf1975` existe au fonds commun, mais son art. 57 (fonds d'intervention économique)
  n'est pas vérifié.
- **Politiques de l'emploi — tableaux faits main** : `tbl-mt-pe-programmes`,
  `tbl-mt-pe-indemnites` et `tbl-mt-pe-fne-lf` portent un TODO rédacteur (à engendrer une fois les
  barèmes et les prévisions des comptes spéciaux versés en amont). Depuis la conversion, les mêmes
  montants sont écrits à la main en trois lieux (ces tableaux, le registre général
  `tbl-mt-pe-textes`, le registre de chaque programme) : une correction doit les toucher tous. La
  prise en charge par l'État de la contribution patronale (née de la loi n° 97-79, art. 43 bis du
  code d'incitation aux investissements ; récrite par la LF 2005, art. 20 ; reprise par les décrets
  n° 2009-349, 2010-87 et 2012-2369 jusqu'au 31 décembre 2014) n'est traitée dans aucun
  chapitre du volume « Les cotisations sociales » : à y signaler par un renvoi vers
  `#sec-mt-pe-prise-en-charge`.
- **Glossaire des politiques de l'emploi** : dix-neuf notions en `provisoire`, sans définition ;
  « contrat d'initiation » (usage, sigle CIVP) ou « contrat d'insertion » (décret n° 2023-461) à
  trancher par le terminologue.
- **Taux des accords-cadres UGTT-UTICA** (1990-2023) : aucun texte au *Journal officiel* ; fiche
  `r-accords-cadres-ugtt-utica`. À obtenir hors corpus (archives d'*Echaab*, ministère des affaires
  sociales, OIT).
- **Décrets des secteurs non couverts** : 2009-693, 2019-456 et 2026-69 lus ; les autres
  (1989-2023) sont au corpus (couche texte à vérifier pour 1989-1996, OCR probable) ; 2018-674 n'a
  qu'un intitulé arabe en base, 2019-456 n'est pas dans jort_cache.db (lu au fascicule). Le tableau
  `tbl-mt-non-couverts` est fait main (TODO rédacteur) en attendant.
- **Couverture conventionnelle et grilles** : aucune source chiffrée de la part des salariés
  couverts ; aucune grille lue (textile, BTP, commerce, hôtellerie). Avenants agréés lisibles au
  corpus (JORT, couche texte selon l'année).
- **Code du travail de 1966** : fascicules n° 20-22 de 1966 sans couche texte (OCR requis pour
  citer les art. 31-52 mot pour mot) ; rectificatif du n° 27/1966 non lu.
- **Socle du SMAG avant 1974** : arrêté et décret du 30 avril 1956 (JORT n° 35/1956) non lus.
- **Le SMIG, les salaires du secteur privé et les prix** — section réécrite le 8 octobre 2026
  (`#sec-mt-salaires-prive`, dernière section de `_salaire_minimum.qmd`), d'après la note
  `docs/notes/marche-travail-salaires-effectifs-prive.md` et les fiches de `tunisia-data`
  (`docs/salaire-moyen-declare-smig.md`, `docs/cnss-quantiles-salaires-approches.md`,
  `sources/cnss-annuaires.md`). Quatre figures : pouvoir d'achat du salaire moyen et du SMIG
  (`#fig-mt-sp-pouvoir-achat`, trois vues) ; SMIG en % du salaire moyen déclaré, avec les
  éléments de législation (`#fig-mt-sp-smig-salaire`) ; salariés par classe de SMIG de référence
  de la CNSS (`#fig-mt-sp-pyramide`) ; quantiles approchés, par segments (`#fig-mt-sp-quantiles`).
  Tableaux : sources (`#tbl-mt-sp-sources`), rapports interquantiles
  (`#tbl-mt-sp-interquantiles`), deux populations de 2013 (`#tbl-mt-sp-2013`), enquêtes de l'INS
  en bloc replié. Chaque chiffre du texte est contrôlé par `controle_texte()` du module de
  figures. Séries snapshotées le 8 octobre 2026 : `cnss-salaire-moyen-declare-smig`,
  `cnss-pyramide-smig-2000-2018`, `cnss-quantiles-salaires-approches`,
  `cnss-pyramide-trimestres-declares-2013`, `cnss-pyramide-dinars-reperes`,
  `ins-salaires-prive-annuel`, `ins-micro-entreprises-salaries-smig`,
  `ins-ees-salaire-base-permanents-smig`. Clos : le salaire moyen des déclarés quatre trimestres
  de 2013 vient désormais de la série (plus de constante) ; le décret n° 2002-3018 (taxis et
  louages) est cité. Le champ du régime des salariés non agricoles vient de la loi (n° 60-30,
  art. 34, volume des cotisations) : les annuaires de la CNSS ne définissent pas le régime.
  Restent :
  - **type de salaire déclaré** : non précisé par les annuaires ; la définition de l'assiette
    reste à établir sur l'article 42 de la loi n° 60-30 ;
  - **rien après 2018** : aucun annuaire de la CNSS postérieur — à obtenir ;
  - **part des salariés au SMIG** : un seul point (2013, déclarés quatre trimestres) ; pyramide
    de l'édition 2006 à lire à l'image (scan) ; pyramides trimestrielles en SMIG des éditions
    2016 et 2017 lisibles (couche texte), non extraites ;
  - **lignes 2000 et 2001 de l'annuaire 2006** : masquées par le pli du scan — à relire sur
    l'original ;
  - **texte de 1988** qui fait entrer l'indemnité complémentaire provisoire dans l'assiette des
    cotisations, sigle « MIT » de l'annuaire 2006 : non lus, aucune recherche lancée (fiche
    `r-…` à ouvrir) ;
  - **enquêtes** : micro-entreprises 1997, 2002 et 2022 à obtenir ; type de salaire de cette
    enquête non précisé par les rapports lus ; quartiles de l'enquête « Emploi et salaires » à
    lire à l'image ; enquête CRES-BIT de 2011 rangée dans `tunisia-data`, non exploitée ;
  - **bibliographie** : treize clés versées à la main dans `marche_travail/references.json` (FR
    et AR), à remonter dans Zotero ; `cnss-annuaire-2006` et `cnss-annuaire-2018` sans URL ; les
    notes de `cnss-annuaire-2013` et `-2018` ne listent pas encore les pages des pyramides en
    dinars (p. 34-35 ; p. 24) ;
  - **glossaire** : « salaire déclaré », « salarié permanent », « salaire de base »,
    « micro-entreprise », « quantile » sans entrée.
- **Glossaire** : dix notions neuves en `provisoire` — termes arabes à confirmer sur le *Journal
  officiel* arabe (الأجر التعاقدي, الاتفاقية المشتركة الإطارية, المصادقة على الاتفاقية المشتركة,
  المنحة التكميلية الوقتية, الأجر الخام/الصافي, التشغيل غير المنظّم).
- **Séries du salaire minimum** : corrigées par openfisca-tunisia#479 (fusionnée) ; tableaux
  régénérés depuis `master` (0.120). À la publication de la 0.120 sur PyPI : relever
  `VERSION_MINIMALE` dans `scripts/openfisca_tables.py` et engendrer le tableau de l'indemnité de
  cherté de vie (TODO rédacteur dans `_salaire_minimum.qmd`).
- **Catalogue de `ipc-longue-periode`** (tunisia-data) : titre et réserves disent « 1962-2003 »,
  alors que la série va jusqu'en 2023 (annuaire 2019-2023, tableau 13.6).
- **Dinars constants : année de base 2025 — fait le 8 octobre 2026.** `ANNEE_BASE = 2025` dans
  `figures/marche_travail.py` ; `bct-ipc-base2015` snapshotée avec 2025 = 186,3 (Rapport annuel
  2025 de la BCT, tableau 2-1, p. 57). L'indice de l'INS (annuaires, jusqu'en 2023) est prolongé
  pour 2024 et 2025 par la variation de cet indice. Tous les chiffres en dinars constants de
  `_salaire_minimum.qmd` sont recalculés et contrôlés par `controle_texte()`, qui s'arrête si
  l'année de base change sans que le texte suive. Restent :
  - **écart de la source** : 186,3 ÷ 176,8 donne +5,4 %, quand le même rapport imprime 5,3 %
    d'inflation moyenne ; non expliqué, rien n'est corrigé (réserve de la série, onglet
    « Sources » des figures) ;
  - **2025 ne repose que sur un rapport** (colonne `rapports_concordants`) : à recouper à la
    parution de l'annuaire de l'INS qui portera 2024 et 2025 ;
  - **volume « Rémunérations publiques » — accordé le 8 octobre 2026** : il reste en dinars
    constants de 2015 (base de l'indice), et ses deux séries déflatées vont maintenant jusqu'en
    2025 (`#fig-augmentations-reel`, `#fig-salaires-categories-reel`) ; texte, légendes et
    libellés des modules mis d'accord, les bornes des libellés de `salaires_categories.py` étant
    lues dans les séries ;
  - **`prestations_sociales`** : `cnss_allocations_familiales.py` et le module nouveau
    `prestations_familiales.py` sont passés aux dinars de 2025 le 9 octobre 2026, par
    `scripts/dinars_constants.py` (le déflateur de ce volume, remonté dans `scripts/`) ;
    `pnafn.py` garde sa base 1987 et ne lit pas cette série.

## La compensation

Volume IX (`precis/fr/compensation/`), créé le 6 octobre 2026 par redécoupage du chapitre
`_compensation.qmd` du volume « Prestations sociales », puis **réécrit le 6 octobre 2026** sur les
notes `docs/notes/compensation.md` (§ 9 et 10 prévalent), `compensation-avant-1970-et-plans.md`,
`compensation-rupture-2015.md` (sa synthèse fait foi), `compensation-prix-carburants.md` et
`compensation-prix-carburants-1993-2018.md` (la seconde corrige la première). Règle d'exposé :
le budgétaire d'abord, en entonnoir ; les rapports extérieurs et les études d'impact ensuite, à
part, chacun avec sa méthode ; aucun tableau ne mêle deux familles. Huit chapitres depuis l'ajout de `_electricite_gaz.qmd`
(rubriques « Électricité et gaz », « Structure des prix » et « Incidence de l'énergie » des
lacunes ci-dessous) :

- `index.qmd` (`#sec-compensation`) : objet, encadré « Trois familles de chiffres », plan ;
- `_institution.qmd` (`#sec-compensation-caisse`) : avant 1970 (Caisse de compensation du
  Protectorat, péréquation, rupture du 28 septembre 1964, compte 1965-1975), création de
  1970-1971, compte de la Caisse 1984-2011 (charges, recettes propres, dotation, solde ; charges
  par produit ; recettes propres de 1984-1985 ; prêts du Trésor), rupture de 1987, poids de la
  dotation dans les dépenses de l'État ;
- `_reformes.qmd` (`#sec-compensation-reformes`) : tableau 1957-2021, puis 1976, 1984, 1989,
  redevance de 2013-2014, renvoi aux carburants ;
- `_depense.qmd` (`#sec-compensation-longue-periode`) : dépense globale, décomposition par poste
  (tableaux 2003-2011 et 2012-2025 **repliés**, les figures les portent), prévu et réalisé (lois
  de finances ; plans IXe, XIe, 2016-2020 ; VIe en mention) ;
- `_carburants.qmd` (`#sec-compensation-carburants-chapitre`), **nouveau** : circuit ETAP-STIR-STEG
  et prix de cession, subvention directe et totale selon l'audit de 2014, rupture de 2015
  (périmètre élargi, facteurs de la LFC 2015, recettes en regard, impayés de 2016), taxe unique
  de compensation 1964-1981, prix à la pompe 1964-2026 source par source, mécanisme d'ajustement
  2009-2021 et gels, autorité qui fixe et notifie les prix ;
- `_exterieurs.qmd` (`#sec-compensation-sources-exterieures`), **nouveau** : figure de comparaison,
  Banque mondiale 1977 et 1985, FMI 1996 et 2000, FMI 2014 et 2016 (énergie « brute ») ;
- `_incidence.qmd` (`#sec-compensation-incidence`) : l'étude INS-CRES-BAD de 2013, avec sa méthode.

Retiré : la section « La compensation rapportée au PIB » et son tableau des parts publiées
(`tbl-compensation-pib`) — les parts sont celles des figures, calculées dans l'entrepôt ; le
tableau du XIe Plan année par année (`tbl-compensation-plan`) et le tableau du poste des
carburants par entreprise en 2011 (`tbl-compensation-energie-2011`), repris dans des tableaux
plus larges ; la phrase du FMI de 1996 sur 4,2 % et 1,8 % du PIB, qui ne se recoupe pas avec son
propre tableau. Le tableau `tbl-compensation-1971-1984` ne mêle plus les familles : les lignes
de la Banque mondiale sont passées dans `_exterieurs.qmd`.

Neuf fiches dans `docs/recherches.yml` : `r-caisse-compensation-origine`,
`r-centimes-additionnels-art106-1955`, `r-cgc-decret-application-1970`,
`r-cgc-budgetisation-1992-2003` (`_institution.qmd`) ; `r-plans-prevision-compensation`
(`_depense.qmd`) ; `r-separation-hydrocarbures-2014-texte`, `r-arrete-prix-petroliers-1980-12-31`,
`r-prix-pompe-arretes-apres-1993`, `r-carburants-ajustement-apres-2021` (`_carburants.qmd`).
Proposées par les notes et **non versées**, faute d'ancre dans le texte :
`r-operations-compensation-creation`, `r-arrete-1993-10-08-prix-gaz-steg`,
`r-separation-effet-ex-post`, `r-serie-prix-pompe-1993-2017` (largement résolue).

- **Figures** (`precis/fr/compensation/figures/compensation.py`, appelées par `cm.figure(…)`),
  onze, chacune appelée une fois : `fig-compensation-compte-caisse`,
  `fig-compensation-par-produit` et `fig-compensation-recettes-caisse` dans `_institution.qmd` ;
  `fig-compensation-longue-periode`, `fig-compensation-par-poste`,
  `fig-compensation-prevu-realise` et `fig-compensation-prevu-realise-postes` dans
  `_depense.qmd` ; `fig-compensation-carburants-beneficiaires`,
  `fig-compensation-carburants-directe-totale` et `fig-compensation-prix-pompe` dans
  `_carburants.qmd` ; `fig-compensation-sources-exterieures` dans `_exterieurs.qmd`.
  - **Snapshots** : refaits le 6 octobre 2026 depuis `main` de `tunisia-data` (neuf séries
    `compensation-*` et `prix-carburants*`). Les notes de lecture disent la base du PIB d'après
    `segment_pib`, `pib_retropole` et `rupture_pib` (2010-2024 : INS, base 2015, rétropolée
    pour 2010-2014). La rupture de 1987 est déclarée dans le module, la colonne `rupture` de
    l'entrepôt ne la portant pas : à y verser.
  - **Tableaux repliés le 6 octobre 2026** : `tbl-compensation-compte-caisse` et
    `tbl-compensation-besoins-energie`, que des figures portent.
  - **Prix à la pompe en dinars constants** : vue non faite. `ipc-longue-periode` est
    snapshoté, mais c'est un indice raccordé (bases 1962 et 1970), annuel et arrêté à 2023,
    face à des prix datés au jour jusqu'en 2026 : le déflatage demande une règle écrite
    (année d'effet, prolongement 2024-2026) avant d'être tracé.
  - **Non tracé, présent dans les données** : relevés mensuels de l'INS et ajustements déduits
    par le calcul (prix à la pompe) ; lignes de plan en cumul ou en part du PIB et prévisions
    de dotation de 1989 et 2007 (prévu / réalisé) ; prévisions de besoins de financement de
    2012-2013 (carburants) ; dépenses du fonds spécial par produit, 1983-1986.
  - **Annexe sur le PIB** : le texte et les notes des figures renvoient à
    `../annexe-pib.html#sec-pib-ruptures` et `#sec-pib-retropolation` ; l'annexe est sur une autre
    branche, les ancres n'ont pas pu être contrôlées ici.
  - **Arabe** : `precis/ar/compensation/figures` est un lien vers le module français ; ses
    libellés sont bilingues, non relus par un arabophone.
- **Arabe** : `precis/ar/compensation/_quarto.yml` (tenu à la main) porte en commentaire les six
  chapitres, dont `_carburants.qmd` et `_exterieurs.qmd` ; décommenter chaque chapitre quand sa
  traduction est livrée, puis rendre le livre arabe.
- **Bibliographie — clés manquantes, citées en clair dans le texte** (bibliographe) :
  `bct-ra-1987` (dotation de 189 MD, citation sur la loi de finances pour 1987, p. 71) et
  `bct-ra-1997` (dotation de 320 MD, p. 91) ; `decret78-316` (taxe unique à 7,120 D/hl) ;
  `minenergie-opendata-prix-vente-petroliers` (moyennes annuelles 1990-2016, fichier aux
  archives du web, **non versé à l'entrepôt**) ; `ins-bms` (présente dans « Retraites » seulement) ;
  dix articles de presse de la frise 2002-2018 ; loi de finances pour 1981 et pour 1987, loi
  n° 91-98, arrêtés des 11 octobre 1990 et 7 juillet 1992, arrêté du 10 mai 2024 ; loi n° 63-13
  (caisse des transports routiers). La collection Zotero « Compensation » reste à créer.
- **Glossaire — notions à créer** (terminologue) : subvention directe / subvention indirecte ;
  prix de cession (préférentiel) ; séparation des opérations de commercialisation des
  hydrocarbures ; revenus de commercialisation des carburants ; compte de la Caisse (charges,
  recettes propres) ; dotation budgétaire ; taxe unique de compensation sur les produits
  pétroliers ; redevance compensatrice ; centimes additionnels ; prix limite de vente ; structure
  des prix ; arrêté interne ; mécanisme d'ajustement de 2009 ; base caisse ; ETAP, STIR, STEG.
  L'ancre `#g-auto-ciblage` n'est toujours pas employée.
- **Lacunes**, dans l'état que les notes établissent :
  - **Avant 1956** : aucun texte établi dans sa lettre ; décrets de 1943, 1945, 1954, 1955 connus
    par les visas. *Journal officiel tunisien* de 1943-1955 : hors corpus et hors pist.tn, **à
    obtenir** (Gallica à vérifier dans un navigateur). Fiches `r-caisse-compensation-origine` et
    `r-centimes-additionnels-art106-1955`.
  - **1956-1969, chiffres non publiés** : montants des redevances sur les huiles et le sucre
    (1956, 1958), sur l'acier (1967), arrêté du 20 juillet 1965, lois n° 59-66 et n° 63-13,
    tableau F de la loi de finances pour 1970 — fascicules au corpus ou sur pist.tn, connus par
    OCR seul : **à relire à l'image**. Première série de 1957 du Journal officiel : absente du
    corpus local, présente sur pist.tn. Aucune série du compte avant 1970 (deux points : 1965,
    1967).
  - **Dotation du budget à la Caisse, dix années sans valeur** : 1988, 1989, 1990, 2000, 2001,
    2003, 2006, 2008, 2009, 2011 — à chercher au chapitre des finances publiques des rapports de
    la BCT (au corpus, textuels) et dans les lois de règlement. Recettes propres après 1999,
    charges par produit de 1984, 1989-1991 et 1994, prêts et avances du Trésor par année : non
    établis. Loi de finances pour 1987 (intégration des recettes au budget) : à lire au JORT.
  - **Passage de la Caisse hors des fonds spéciaux** : texte non identifié (fiche
    `r-cgc-budgetisation-1992-2003`) ; lois de finances 1993-2003 à ouvrir.
  - **Décret d'application de l'article 3 de la loi n° 70-26** : non identifié (fiche).
  - **Rupture de 2015** : effet constaté de la séparation de 2015 à 2018, subvention indirecte de
    2013 et 2014, bénéficiaires de la ligne en 2013 et après 2016, recettes de commercialisation
    encaissées de 2019 à 2025, acte formalisant la séparation (fiche), arrêté du 8 octobre 1993
    sur le prix du gaz, régularisation des impayés de 2016 : non établis. Rapport de 2014 :
    pages 1-10 et 158-159 seules exploitées. Lois de finances pour 2016 et 2019 : éditions
    françaises absentes du corpus local.
  - **Prix à la pompe** : arrêté du 31 décembre 1980 (fiche) ; **1997-2001 : dates et niveaux des
    ajustements non établis** (moyennes annuelles seules ; les lignes inférées ne sont pas
    publiées) ; laquelle des lignes 2000 et 2001 du ministère est fautive ; tout prix mensuel
    avant novembre 2007 ; ajustements du pétrole lampant et de la bouteille de gaz avant 2008 ;
    moyenne officielle 2017-2018 ; prix de la bouteille de gaz du 18 août 1992 (à relire à
    l'image) ; aucun « arrêté interne » de notification n'a été vu. Tarifs de la taxe unique
    après 1981 : non établis.
  - **Électricité et gaz** (`_electricite_gaz.qmd`, `#sec-compensation-electricite-gaz`), sur
    `compensation-tarifs-electricite-gaz.md`, `compensation-tarifs-1993-2004.md` et
    `compensation-tarifs-mt-ht-gaz.md` — écrit : autorité tarifaire (arrêtés 1970-1990, décision
    du 11 août 1992, décision du 10 août 2000 citée par l'API) ; grilles des ménages 1970-1992
    (Journal officiel), cinq grilles de 1993 à 2003 en deux tableaux (relais officiels ; rapport
    extérieur seul), 2004-2022 (STEG, établies sur ses documents de 2008 à 2022) ; frise
    1992-2006 avec la famille de chaque source ; moyenne et haute tension, gaz en moyenne et
    haute pression, tarifs à postes horaires expliqués ; recette moyenne par kWh donnée comme un
    calcul ; coût et prix de vente (rapport de contrôle 2008-2012 ; Observatoire 2017-2025 ;
    BAD 2000-2004, rapport extérieur) ; rapprochement avec la subvention d'exploitation de la
    STEG. **Restent** : jour d'effet des grilles d'octobre 1993 et de juin 1994 (fiche
    `r-tarifs-electricite-grilles-1993-2003`, passe consignée) ; moyenne et haute tension et gaz
    de 1994 à 2003, établis par les notes et non publiés ; grilles du gaz de 2001 à 2003 ;
    **acte du 10 août 2000 non lu**, actes de 1993, 1994, 2001, 2003 et 2004 non identifiés
    (fiche `r-tarifs-electricite-gaz-apres-1992`, passe consignée) ; contradiction de 2003 (90
    ou 94) et écart de 2005 avec l'INS ; **tarifs du Journal officiel de 1975 à 1990 à relire**
    (moyenne et haute tension, unité de la prime) ; haute tension de septembre 2012, moyenne
    pression de 2012-2013 ; heures des postes avant 2014 ; ventes en haute tension de 2020 ;
    grille basse tension du 1er janvier 2014 (source seconde, non publiée) ; arrêtés de 1961,
    1963, 1976-1981 connus par leur intitulé ; **figure de la facture type**
    (`fig-compensation-facture-electricite`, TODO figures : TVA et surtaxe municipale à
    reconstituer) ; série de la subvention d'exploitation de la STEG non publiée (notes aux
    états financiers à lire) ; décodage des couches texte du JORT des années 2000 à verser à
    `docs/notes/outillage-sources.md`.
  - **Structure des prix des carburants** (`_carburants.qmd`, `#sec-compensation-structure-prix`),
    sur `compensation-archives-energie.md` et `compensation-structure-prix-relue.md` — écrit :
    lecture du tableau de la *Conjoncture énergétique*, 24 structures datées de 2014 à 2022
    (synthèse en clair, deux tableaux repliés), importation et cession en moyenne annuelle
    2016-2025 (écart donné comme un calcul), subvention unitaire prévisionnelle des budgets
    citoyens 2021-2024, déficit de commercialisation 2000-2002, hausses de 2000, aucune en 2001.
    **Restent** : **structure du 1er avril 2018** et numéros de janvier à juin 2018 ; date de la
    baisse d'août 2020 ; droits et marges du 6 février 2021 ; composantes séparées (droit de
    consommation, TVA, chaque marge) ; **montant budgétaire par produit pétrolier** (aucune
    publication officielle) ; **décisions de prix** (aucun « arrêté interne » en ligne ni
    archivé) ; série 1980-2025 du graphique des *Chiffres clés* (non publiée en valeurs) ; jour
    et niveau des ajustements de 1997 à 2000 ; budgets citoyens 2018, 2020 et 2025 ; répartition
    STIR / STEG de la ligne 2022-2025 (rapports sur le budget, sans clé).
  - **Études d'impact** (`_incidence.qmd`), sur `compensation-etudes-incidence-calculs.md` —
    écrit, pour quatre études, les données, le calcul pas à pas, les résultats, les limites et
    les incohérences : INS-CRES-BAD 2013 (répartition 9,2 / 60,5 / 7,5 / 22,8 publiée avec la
    mention que deux classes ne sont pas définies), Banque mondiale 2013 (par produit, par
    quintile, par tête, réforme simulée), document de travail de 2015 (subvention unitaire, par
    quintile, perte, scénarios), document de travail de 2017 (agrégat de toutes les
    subventions). **Restent** : **tableaux d'études à contrôler cellule par cellule** (seuls le
    tableau 1 et les figures 11 et 12 de la note de 2013 sont établis sur le document) ;
    alignement du tableau 18-8 du document de 2017 ; outil de simulation (Araar et Verme, 2012)
    non ouvert ; définition des classes moyenne et aisée (rapport INS-BAD-Banque mondiale de
    2012) ; Banque mondiale n° 47294 (2008), sans clé ; rien sur l'alimentaire après 2010.
  - **Rapports extérieurs** : tableau III-1 de la Banque mondiale 1985 et tableau par produit
    1972-1977 de la revue du Ve Plan : à relire à l'image, aucune valeur publiée ; rétropolation
    de la série « brute » du FMI non détaillée par le rapport ; rapports du FMI de 2015 à 2019
    non exploités.
  - **Lois de règlement** : aucune ouverte.
  - **Textes non relus à l'image** : LF 1971 (art. 48, tableau F), décret n° 70-622, LF 1984
    (art. 87, tableau F ; art. 38 et suivants : seule la référence est retenue), LFC 1989.
  - **Hors texte, faute de source** : opérateurs de la compensation des produits de base,
    bénéficiaires de la compensation du transport, entrées et sorties de produits, produit de la
    redevance de compensation, ciblage et transferts de substitution, événements de janvier 1984.
  - **Redevance de compensation, revenu des personnes physiques** : rédaction de 2013 (assiette,
    plafond de 2 000 D) à relire à l'image ; prorogation des volets bornés à 2014-2015 à établir.

## Citations répétées — suggestion, non engagée (4 octobre 2026)

Une même référence revient parfois à chaque phrase : le code de l'IRPP et de l'IS (`code-irpp-is-1990`) 31 fois dans `fiscalite/_impot_revenu.qmd` ; dans le volume VII en préparation (branche locale), la loi n° 97-11 jusqu'à 28 fois par chapitre et Dafflon et Gilbert 56 fois dans le chapitre des notions. La parenthèse « (loi n° … du …, art. 3) » alourdit la lecture sans rien apporter que le numéro d'article. Suggestion, à décider par l'humain avant toute mise en œuvre :

1. **Source principale déclarée en tête de section** : « Sauf mention contraire, les articles cités dans cette section sont ceux du code … [@clé]. » ; ensuite « (art. 3) » ou « l'article 35 dispose… » en clair, sans citation ; toute autre source reste citée en place. Même chose pour une doctrine suivie de bout en bout (« Les définitions de ce chapitre suivent … », puis « (p. 23) »).
2. **Une citation par paragraphe** plutôt que par phrase quand un texte court tout le paragraphe (`[@clé, art. 1 à 5]`).
3. **Tableaux** : une ligne « Sources » sous le tableau plutôt qu'une citation par cellule.
4. **Contrôle** dans `scripts/verifier.sh` : une même clé citée plus de N fois (N = 4 ?) dans une section est signalée.

Écartés : notes de bas de page (changement de style CSL pour tout le précis) ; suppression des articles (perte d'information). À prévoir côté traduction : les locateurs en clair « (art. 3) », hors citation, devront être protégés comme le sont aujourd'hui ceux des citations (`translate_sync.restore_locators`). Ordre envisagé : volume VII, puis IRPP, caisses, cotisations, un volume par PR.

## Les finances locales

Volume créé le 4 octobre 2026 (`precis/fr/finances_locales/`), d'après le plan
`docs/notes/fiscalite-locale-plan.md`. **Neuf chapitres** depuis le 9 octobre 2026 : le
chapitre « La longue période » est dissous, chaque chapitre porte ses séries. Une entrée par
chapitre ci-dessous, dans l'ordre du volume ; les `TODO` des `.qmd` détaillent chaque lacune.

**État d'ensemble (10 octobre 2026).** Les neuf chapitres sont au format « ruptures au premier
plan, détail replié ». Huit portent le domicile unique des références : histoire (ch. 3) et
compétences (ch. 4), convertis le 10 octobre 2026 ; budgets (ch. 5), impôts sur les immeubles
(ch. 6), impôts sur l'activité (ch. 7), taxes et redevances (ch. 8), transferts (ch. 9),
convertis le 9 octobre 2026. Les notions (ch. 2), resserrées le 9 octobre, n'ont pas de registre
(elles ne citent aucune loi). La présentation (ch. 1) annonce les neuf chapitres sous leurs
titres. Le partage entre les deux chapitres d'institutions : les réformes à l'histoire, l'état
du droit aux compétences ; raccords de fin de chantier faits le 10 octobre 2026 (voir les
entrées des chapitres 3 et 4).
Plans : `finances-locales-impots-plan-architecte.md`,
`finances-locales-transferts-budgets-plan-architecte.md`,
`finances-locales-histoire-competences-notions-plan-architecte.md` ; lectures :
`finances-locales-impots-lectures-2026-10-09.md`,
`finances-locales-transferts-budgets-lectures-2026-10-09.md`,
`finances-locales-institutions-lectures-2026-10-10.md`.

**Ce qui reste pour le volume (10 octobre 2026)** — le détail est dans les entrées ci-dessous :

- **Frises de tête** : faites dans aucun chapitre ; un `TODO (rédacteur)` les attend aux
  chapitres 3, 6, 7 et 8, le tableau des réformes en tient lieu.
- **Tableaux encore faits main**, faute de paramètres datés et sourcés en amont : taxe sur les
  établissements (maximum, taux, montants) et taxe hôtelière au chapitre 7 ; pénalité de retard
  et contribution au fonds de l'habitat au chapitre 6 ; tarifs des taxes et redevances au
  chapitre 8 ; seuils de l'approbation au chapitre 5 ; parts et critères du fonds et des
  subventions au chapitre 9. Seuls les trois barèmes des taxes sur les immeubles sont engendrés.
- **Figure des barèmes des taxes sur les immeubles**, en dinars courants et en dinars de 2025 :
  devenue faisable (séries complètes de 1997 à 2017), non faite.
- **Approbation des délibérations communales, 1975-2018** (lecture du 10 octobre 2026,
  `docs/notes/finances-locales-approbation-1975-2018.md`), portée aux chapitres 3, 4 et 8.
  **Établi** : tarifs approuvés par le gouverneur de 1975 à 1995 (ou le délégué jusqu'en 1985),
  sans approbation propre de 1995 à 2018, sauf la redevance des déchets non ménagers ; budget
  approuvé jusqu'en 2018 ; emprunts approuvés par les ministres jusqu'en 1995, et autorisés
  depuis 1985 par l'art. 66 du code de la comptabilité publique (loi n° 85-47) ; loi organique
  n° 91-24 lue (art. 48 et 90 seuls) ; « 2 - 10 et 12 » = 2, 10 et 12. **Reste, lisible dans le
  corpus (image ou OCR)** : art. 66 d'origine (loi n° 73-81, JORT n° 51 de 1973) et ses
  modificatifs après 1985 (fiche `r-fl-ccp-art66-modificatifs`, terme arabe à jouer, loi
  n° 85-109 à ouvrir) ; décret n° 90-1960, p. 1849-1853 ; décrets n° 76-826, n° 95-1121 et
  n° 58-234 ; loi n° 75-33 hors p. 1058-1060 et durée des baux de l'art. 43, 3e tiret ; loi
  organique n° 2008-57 ; date de dépôt du JORT n° 59 de 1995 (date d'effet de la loi organique
  n° 95-68) ; numéros des art. 43, 44 et 46 après 2006. Le motif du retrait de 1995 n'est dit
  par aucun exposé ni rubrique.
- **Lectures en attente** : décret-loi n° 2026-4, art. 14 à 27, 35 à 48 et 100 à
  131, et art. 57 à 99 à relever pour les budgets ; édition française du code de 2018 et du
  décret-loi de 2026, **à obtenir**.
- **2012** : décrets de dissolution, de nomination et de prorogation à lire ; aucun total pour
  l'année ; rien n'est établi sur ce qui relie les prorogations aux élections de 2018.
- **Constitution de 2014** : numéro spécial du JORT du 10 février 2014 **à obtenir** ; le
  chapitre VII est cité d'après la traduction reproduite par Dafflon et Gilbert.
- **Libellés arabes** : attributs `titre` des blocs repliés des chapitres 2 à 9 à traduire,
  avec les chapitres eux-mêmes ; libellés des figures du 9 octobre non relus.

**Livre arabe.** `precis/ar/finances_locales/` a son `_quarto.yml` et ses références ; il est
sauté au rendu tant que la traduction n'a pas livré `index.qmd`. Les chapitres 3 à 9 y sont
déclarés en commentaire, à décommenter à la livraison de chaque traduction ; la ligne de
`_longue_periode.qmd` en est retirée. Les blocs repliés (attribut `titre`) et les libellés des
figures nouvelles restent à traduire.

### Ce qui traverse le volume

- **Décret-loi n° 2026-4 du 30 septembre 2026, relatif aux conseils municipaux** (JORT n° 96
  de 2026, édition arabe, p. 2058-2074 ; clé `decretloi2026-4`). Il abroge le code des
  collectivités locales de 2018 (art. 139) mais n'entre en vigueur qu'après les prochaines
  élections municipales (art. 136). **État de lecture** : art. 1 à 13, 28 à 34, 57 à 99 et 132
  à 140 lus à l'image (`finances-locales-impots-lectures-2026-10-09.md`, § D.5) ; art. 14 à 27,
  35 à 56 et 100 à 131 parcourus, à lire en suivi. **Écrit au volume** : signalé une fois, comme
  texte publié qui n'est pas en vigueur, au chapitre des taxes (`#sec-fl-moduler-droits`) et à
  celui des budgets (`#sec-fl-budg-etat-du-droit`, ligne `r-fl-budg-2026` : art. 30, 71, 136,
  137 et 139). **Reste** : relever pour le chapitre des budgets les art. 57 à 99 (budget,
  équilibre, emprunt, exécution, comptes), lus mais non relevés ; rien n'est dit au chapitre
  des transferts de l'art. 134 (fonds de 2021 maintenu et renommé) ; le chapitre d'histoire
  le porte depuis le 10 octobre 2026 comme réforme publiée, non entrée en vigueur
  (`#sec-fl-hist-2026` : art. 1, 2, 12, 29, 30, 51, 52, 55, 56, 136, 137 et 139 ; p. 2058 et
  2065 lues à l'image le 10 octobre, art. 14 à 27, 35 à 48 et 100 à 131 à lire) ; celui des
  compétences le donne à l'état du droit comme texte publié non entré en vigueur
  (`#sec-fl-comp-dissolution-2023`, ligne `r-fl-comp-2026` : art. 12, 29, 30, 56, 136 et 139) et
  renvoie à `@sec-fl-hist-2026` pour l'objet du texte et la dissolution ; sort du code de la fiscalité
  locale et du décret de tarifs n° 2016-805 à son entrée en vigueur, que le texte ne règle
  pas. **Corpus** : fascicule arabe lisible (`PDFs/JORT/2026/ar/Ja0962026.pdf`) ; édition
  française **à obtenir** (le fichier « fr » est l'arabe) ; absent de `jort_cache.db`. À
  l'entrée en vigueur, tout ce que le volume dit des conseils élus et du budget communal est à
  récrire.
- **Code des collectivités locales (loi organique n° 2018-29)** : lu dans l'édition arabe du
  JORT n° 39 de 2018 ; édition française **à obtenir** (absente de pist.tn et du corpus, comme
  celle du n° 51 de 2018). Les traductions du volume sont de travail, sans guillemets. Le nom
  français des niveaux (« باب », « قسم ») n'est pas établi.
- **Art. 237 et art. 139 du code de 2018** : tranché le 10 octobre 2026 — l'art. 139 donne aux
  conseils élus de toute collectivité le pouvoir d'arrêter le montant ou le tarif des droits ;
  l'art. 237 en fait une matière du conseil municipal. Les deux références sont justes
  (`finances-locales-institutions-lectures-2026-10-10.md`, § 4) ; `TODO` retirés.
- **Tableaux de paramètres** : trois engendrés au chapitre des impôts sur les immeubles
  (`tbl-fl-tib-taux`, `tbl-fl-tib-prix-reference`, `tbl-fl-tnb-tarif`) ; les autres faits main,
  avec leur `TODO (rédacteur)`. Constats versés à `docs/notes/backlog-modele.md`.
- **Sources des séries** : présentées une fois, `#sec-fl-lp-sources` (ch. 5). Six séries de
  `tunisia-data`, lues par `figtools.series()` dans `precis/_seriescache/`. Les fichiers Banque
  mondiale de 1992 et 1997 sont snapshotés par `scripts/snapshot_finances_locales_bm.py` et
  déclarés par `register_provenance` — à retirer quand `tunisia-data` les déclarera. Les
  réserves du catalogue disent encore « réserve à 18 % jusqu'en 2017, 15 % ensuite » et
  « vraisemblablement fonds total contre quote-part des communes » : à aligner sur le volume
  (les 15 % de 2018-2019 ne sont plus la réserve ; la divergence de 1990 n'est pas tranchée),
  puis snapshot à refaire.
- **Figures** : un seul module, `figures/finances_locales.py` ; chaque source a sa marque, les
  textes placés à leur date d'effet ont un trait rouge distinct des ruptures de série, sans lien
  de cause (`MARQUES_IMMEUBLES`, `MARQUES_ACTIVITE`, `MARQUES_FCCL`, `MARQUES_BUDGETS`). Libellés
  arabes écrits dans le module, non relus par le relecteur-ar pour les deux figures du 9 octobre.
- **Définitions des ratios publiés par la Direction générale des collectivités locales**
  (autonomie, rémunération, recouvrement de la taxe sur les immeubles bâtis, 2008-2019) : non
  publiées avec les séries. Pistes non ouvertes : étude « transferts financiers » de la
  bibliothèque du portail, archives du web de la page des indicateurs. Fiche proposée
  `r-fl-dgct-definitions-ratios`, **non versée** (pas de requête rejouable sur le JORT) : à
  trancher par l'architecte ou le propriétaire. **À obtenir.**
- **Dates dans la prose** : la classe `.insecable` n'agit que dans les tableaux
  (`precis/legendes.scss`) ; une date ou un nombre à espace (« 1 169 MD ») peut encore se
  couper en fin de ligne dans le texte courant — à trancher pour tout le volume.
- **Frise de tête** : faite dans aucun chapitre ; le tableau des réformes en tient lieu.
- **Renvois entre chapitres** : contrôlés le 10 octobre 2026 — tout `@sec-fl-…` vise un titre,
  tout `@tbl-fl-…` ou `@fig-fl-…` une légende, tout lien `(#…)` un identifiant du même fichier ;
  aucun renvoi ne vise l'un des identifiants devenus simples ancres ; seul lien entrant depuis
  un autre volume : la page d'accueil (`precis/fr/index.qmd`).
- **Glossaire** : 40 notions du chapitre des notions, toutes `provisoire` (termes arabes sans
  texte bilingue ; à trancher par un arabophone : « التعديل » pour péréquation, « الرسم » pour
  la taxe, « معلوم الاستعمال » pour la redevance d'utilisation) ; quinze notions d'institutions
  et de budget, dont trois `valide` ; `fonds-commun-collectivites-locales`,
  `reserve-fonds-commun`, `cpscl` (termes du JORT). **Entrées à créer par le terminologue** :
  subvention annuelle du budget de l'État, subvention d'équilibre, fonds d'appui à la
  décentralisation, fonds de coopération des collectivités locales.
- **Références à lire** : Dafflon et Gilbert, PARD 2021 (transferts) et 2022 ; Hammami, Dafflon
  et Gilbert, PARD 2021 (compétences) ; Dafflon, RTF n° 25 (2017) ; Dafflon et Madiès, AFD,
  *Notes et documents* n° 42 (2008), dont le fichier téléchargé n'a que six pages — **à
  obtenir** ; voir `docs/notes/biblio-fiscalite-locale.md`.
- **Questions du plan restées ouvertes** : chapitre propre aux régions ; taxes affectées à des
  fonds hors budgets locaux ; chronologie des textes en annexe (annoncée par la présentation
  jusqu'au 9 octobre 2026, retirée du texte faute d'exister).

### Chapitre 1 — Présentation (`index.qmd`)

Rédigée le 4 octobre 2026, mise à jour le 9 octobre, **mise en accord avec les neuf chapitres
le 10 octobre 2026** : sous les trois mouvements (notions, institutions, ressources), une ligne
par chapitre, avec son titre actuel et ce qu'il donne ; un guide de lecture
(`#sec-fl-guide-lecture`, identifiant nouveau) dit où se lisent les réformes, l'état du droit des
institutions, puis les budgets, impôts, taxes et transferts, et que les longs tableaux de textes
sont dans des blocs repliés ; la section du périmètre, titrée « Le champ du volume »
(`#sec-fl-perimetre` gardé), ne dit plus ce que le volume ne traite pas. La phrase qui prêtait le
même plan à tous les chapitres est retirée : le plan commun n'est dit que des chapitres 5 à 9.

### Chapitre 2 — Les notions (`_notions.qmd`) — resserré le 9 octobre 2026

Rédigé le 4 octobre 2026, resserré le 9 octobre 2026 d'après
`finances-locales-histoire-competences-notions-plan-architecte.md` (§ 2.5, arbitrages A3 et A4) :
définitions, trois tableaux et six formules au premier plan (2 576 mots contre 4 103), les
développements de Dafflon et Gilbert dans cinq blocs repliés, un par section (1 476 mots). Source
unique : Dafflon et Gilbert, AFD 2018 (`dafflon-gilbert-2018`, exemplaire HAL). Aucune valeur
tunisienne, aucune loi citée : ni registre ni domicile unique. La section « Notations » et son
tableau sont supprimés (`sec-fl-notations`, `tbl-fl-notations`, appelés par personne) ; chaque
symbole est défini sous la formule où il sert. Les 21 autres identifiants et les 42 liens de
glossaire sont inchangés.

- **Notation** : deux symboles renommés pour s'aligner sur les chapitres convertis — les
  financements extérieurs de fonctionnement passent de $F$ à $X$ ($F$ est le montant du fonds
  commun au chapitre des transferts), le taux moyen national de $\bar{t}$ à $\bar{\tau}$ ($\tau$
  est le taux dans les chapitres des impôts). Restent à arbitrer pour tout le volume : $B$ (base
  d'imposition ici, moyenne triennale des recettes des taxes sur la propriété bâtie $B_j$ aux
  transferts), $R$ (recettes du nouvel investissement ici, $R_1$ recettes du titre 1 aux
  budgets), $\mu$ (part des communes aux transferts, minimum par mètre carré aux impôts sur
  l'activité).
- **Deux titres de blocs s'écartent du plan** : celui du budget ajoute « et coûts récurrents » ;
  celui de la mesure ne nomme plus le périmètre des recettes propres, resté au premier plan
  parce que le chapitre des budgets y renvoie.
- **Charte européenne de l'autonomie locale** : le chapeau la date de 1986 ; date à vérifier
  (1985 ou 1986) sur Dafflon et Gilbert, p. 17, et sur le texte de la Charte.
- **Glossaire (terminologue)** : douze notions définies au fil du texte sans entrée —
  coopération, solidarité, responsabilité budgétaire, patrimoine administratif, déséquilibres
  locaux, effets de débordement, externalité fiscale, principe de dérivation, autonomie fiscale,
  péréquation verticale et horizontale, subventions d'incitation et correctrices.
- **Lacunes** : notions non définies faute de source lue — épargne brute, dépendance aux
  transferts, fonds commun comme notion générale, établissement public (Dafflon et Madiès 2008,
  **à obtenir**). Aucun exemple chiffré : le chapitre n'en porte pas, et aucune série ne s'y
  prête sans sortir des définitions.
- **Livre arabe** : le chapitre traduit date d'avant le resserrement ; les cinq attributs
  `titre` des blocs sont à traduire.

### Chapitre 3 — Les collectivités locales, de 1957 à 2026 (`_histoire.qmd`) — converti le 10 octobre 2026

Rédigé le 5 octobre 2026 (note `finances-locales-histoire.md`) ; **converti le 10 octobre 2026**
au format « ruptures au premier plan, détail replié », avec domicile unique des références,
d'après la fiche `finances-locales-histoire-competences-notions-plan-architecte.md` et les
lectures `finances-locales-institutions-lectures-2026-10-10.md`, qui la corrigent. Le chapitre
est celui des grandes réformes du volume : tableau de tête de cinq lignes (1957, 1975, 2018,
2023-2025, 2026), une section et un registre replié par réforme ; 1989 et 2011 sont des étapes ;
il ne porte pas d'état du droit (renvoi à `@sec-fl-comp-depuis-2023`). Onze blocs repliés, dix
clés versées en français et en arabe (`decretloi2011-14`, `decret2011-4252`,
`loi-constituante2011-6`, `decret2012-385`, `decret2012-578`, `loi-org85-43`, `loi-org95-68`,
`loi-org2006-48`, `decret-gouv2019-351`, `decret-gouv2020-31`). Cinq identifiants de section ne
sont plus des titres mais des ancres (`sec-fl-hist-1959`, `-1975`, `-1989`, `-2011-2022`,
`-apres-2022`) : ils ne répondent plus à un renvoi `@`.

**Fiches RECHERCHE ancrées au chapitre** : `r-fl-dissolutions-2011` (2011 établi : dix-huit
décrets, 212 conseils en somme de tableaux ; 2012 ouvert), `r-fl-duree-delegation-speciale`
(nouvelle), `r-fl-constitution-2014-numero-special`, `r-fl-conseil-superieur-collectivites`
(nouvelle ; depuis le 10 octobre le constat est dit en entier à `#sec-fl-comp-instances`, où
la fiche a sa seconde ancre, et `#sec-fl-hist-carte` le dit en une proposition avec renvoi), `r-fl-nombre-communes` (déplacée à `#sec-fl-hist-longue-periode`).
`r-fl-elections-municipales-apres-2023` n'est plus ancrée qu'au chapitre des compétences.

**Lacunes**, lisibles dans le corpus sauf mention :

- **raccords du 10 octobre 2026 avec le chapitre des compétences** : la Haute instance des
  finances locales est dite en entier à `#sec-fl-comp-instances` ; ici, une proposition au premier
  plan et deux lignes de registre réduites à la date, au texte et à un renvoi
  (`r-fl-hist-2019-instance`, `-2020-instance`, gardées parce que le premier plan les lie) ; le
  registre de 1985-2008 ne dit plus « non établi » pour l'autorité d'approbation d'avant 1985 ni
  pour l'article 42 de 1975, lus à l'image le 5 octobre (p. 1058) et portés au registre
  `tbl-fl-comp-1975` : il y renvoie. **Tranché le 10 octobre 2026** : l'article 43 de 1985
  réserve aux ministres les paragraphes 2, 10 et 12 (édition arabe), le 9 passant au
  gouverneur ; l'article 42 n'est modifié ni en 1985 ni en 1991 ; le premier plan et le registre
  disent ce qui sort de la liste en 1995 (emprunts, taxes et droits, foires et marchés, dons et
  legs grevés, acquisitions) ; ligne de 1991 portée au registre (`r-fl-hist-1991`), avec son avant →
  après sur le plein temps, depuis la rédaction de 1985 de l'art. 48 ; guillemets retirés des
  lignes de 1995 et de 2006 (couche texte). **À trancher** : la portée de la ligne de 1995,
  laissée à « ajustement » ;
- 2012 : décrets n° 2012-910, 2012-1122, 2012-2007, 2012-2536 à 2012-2538, 2012-2771, 2012-2885,
  2012-2895 et 2012-2943 à lire ; aucun total pour l'année ; décrets de 2012 à 2017 à lire avant
  de dire ce qui relie les prorogations aux élections de 2018 (le chapitre n'en dit rien) ;
- 2011 : doublons de communes entre les dix-huit décrets, nombre de communes existant en 2011 ;
  dispositif de huit décrets de nomination (n° 2011-395, 778, 831, 861, 1138, 1208, 2908, 3293) ;
  le chapitre écrit « dix décrets de nomination » d'après l'énumération du § 1.3 de la note du
  10 octobre, dont le résumé dit « neuf » : **à trancher** ;
- source de la durée d'un an des délégations spéciales : art. 161 du code électoral (JORT n° 30
  de 2009), fascicule sans couche texte utile, **OCR ou lecture à l'image** ;
- loi organique n° 85-43 : date d'adoption à relire dans l'édition française ;
  art. 48 de la loi organique des communes dans sa rédaction de 1975 ; date d'effet de la loi
  organique n° 95-68 ;
  clauses d'effet des lois organiques de 1985 à 2008 ; loi n° 75-38 (intitulé seul, sans clé) ;
- loi municipale de 1957 : clause finale (fascicule du 15 mars 1957 absent du corpus, sur
  pist.tn) ; décrets d'avant 1956, **à obtenir** ;
- numéro spécial du JORT du 10 février 2014 (Constitution), **à obtenir** ; texte arabe de la
  Constitution de 2014 ;
- nombre de communes de 1957 à 2014 ; texte de mise en place du Conseil supérieur des
  collectivités locales ; activité de la Haute instance des finances locales ;
- décret-loi n° 2026-4 : art. 14 à 27, 35 à 48 et 100 à 131, intitulés des titres III et
  suivants, mode de nomination de la commission provisoire de gestion ;
- frise des réformes en tête du chapitre (`TODO (rédacteur)`) ; onze attributs `titre` à
  traduire quand le chapitre le sera.

### Chapitre 4 — Les compétences : qui fait quoi, qui décide (`_competences.qmd`) — converti le 10 octobre 2026

`.domicile-unique`, d'après `finances-locales-histoire-competences-notions-plan-architecte.md`
(§ 2.4 et 3.2). Rédigé le 5 octobre 2026 (note `finances-locales-competences.md`) sous le titre
« Compétences et organisation ». Plan : vue d'ensemble (`tbl-fl-comp-etats`, trois états du
droit) ; avant 2018 (commune de 1975, conseil régional de 1989) ; 2018, trois catégories de
compétences ; qui décide, qui contrôle ; **l'état du droit en octobre 2026**, le seul du volume
(`#sec-fl-comp-depuis-2023`, `tbl-fl-comp-2026`). Douze blocs repliés, tous des registres à
ancres `r-fl-comp-…` (66 lignes). Premier plan : 3 417 mots contre 3 520 (repliés : 3 920) ;
la cible du plan (− 38 %) n'est pas tenue, parce que deux tableaux courts et l'état du droit
entrent au premier plan. Tous les identifiants sont gardés ; `sec-fl-comp-longue-periode`
devient une ancre de la vue d'ensemble. Le décret-loi n° 2026-4 entre au chapitre, comme texte
publié et non entré en vigueur (art. 1, 12, 29, 30, 55, 56, 136 et 139). Fiches :
`r-fl-loi-competences-partagees`, `r-fl-elections-municipales-apres-2023`.

- **Renvois au chapitre d'histoire** : par ses identifiants d'avant conversion
  (`sec-fl-hist-lois-1975`, `-modifications`, `-code-2018`, `-2023-2025`, tous gardés comme titres par
  le plan) ; depuis le 10 octobre 2026, `@sec-fl-hist-2026` pour le décret-loi de 2026, dont la
  ligne de registre ne garde que les art. 12, 29, 30, 56, 136 et 139 (art. 1, 51, 52 et 55 :
  `tbl-fl-hist-2026`) ; l'art. 56 y est traduit comme au chapitre d'histoire (« entrave
  manifeste au fonctionnement des services »).
- **Redite retirée, qui vit à `_histoire.qmd`** : place de la loi de 1975 dans les six lois et
  délégation spéciale au premier plan (`#sec-fl-hist-lois-1975`) ; statut du gouvernorat et
  composition du conseil régional (`#sec-fl-hist-1989`, que le plan fond dans
  `#sec-fl-hist-modifications`) ; récit des décrets-lois de 2023 et
  statut des conseils de 2025 (`#sec-fl-hist-2023-2025`). Les articles correspondants restent
  dans les registres repliés de ce chapitre.
- **Art. 237 et art. 139 ; art. 9 et art. 135 du code de 2018** : tranché par
  `finances-locales-institutions-lectures-2026-10-10.md` (§ 4 et 5) — deux règles compatibles à
  chaque fois, aucune référence à corriger ; les `TODO` sont retirés, ici et à
  `_taxes_redevances.qmd`. **Reste** : `_budgets.qmd` ne cite pas l'art. 9 (obligation
  permanente sur les ressources ordinaires réalisées, programme de maîtrise), que seul le
  registre des organes de ce chapitre porte ; décret d'application de l'art. 9 non cherché.
- **Approbation des délibérations, 1985, 1995 et 2006** : portées le 10 octobre 2026 au registre
  du contrôle des actes (`tbl-fl-comp-controle-articles`, lignes `r-fl-comp-controle-1985`,
  `-1995`, `-2006`), une ligne par loi, avec renvoi au registre du chapitre d'histoire
  (`tbl-fl-hist-modifs-communes`) qui en porte le texte. Complétées le 10 octobre 2026 d'après
  `docs/notes/finances-locales-approbation-1975-2018.md` : avant → après de 1985 et de 1995,
  art. 44 de 1975 et détail de l'art. 43 au registre `tbl-fl-comp-1975`, ligne
  `r-fl-comp-controle-emprunts` (loi n° 85-47, art. 66 du code de la comptabilité publique),
  ligne « Budget, emprunts, taxes et droits » de `tbl-fl-comp-controle` scindée en trois.
  Constat et ancre `r-fl-ccp-art66-modificatifs` sous `#sec-fl-comp-communes-1975` : le maintien
  de l'art. 66 jusqu'en 2018 n'est vérifié que sur les titres de l'index. **États de lecture** :
  n° 85-43, p. 642-643 lues en entier (OCR relu, édition arabe à l'image pour les art. 43 à
  46) ; n° 85-47, OCR, sans guillemets ; n° 95-68 et n° 2006-48, couche texte, sans guillemets
  dans les deux chapitres, **à relire à l'image** avant toute citation ; n° 91-24 lue en entier.
  **Non établi** : l'application de l'art. 44 de la loi organique des communes à l'autorisation
  des emprunts ; la durée des baux approuvés par le délégué en 1975 (art. 43, 3e tiret).
- **Dates d'effet** : loi n° 75-33, exécutoire le 22 mai 1975 (aucune clause ; rectificatif du
  1er août 1975 lu à l'image, sans date d'effet, numéros d'articles à relire) ; loi organique n° 89-11 (p. 220-221), non établie, le registre des
  dates donne sa publication. **Lisible dans le corpus, à l'image.**
- **Instances nationales** : désignation des membres de la Haute instance (décret gouvernemental
  n° 2019-351) et indemnités (n° 2020-31) portées au registre, clés versées dans les deux
  `references.json` ; mise en place du Conseil supérieur non identifiée : constat et ancre
  `r-fl-conseil-superieur-collectivites` posés le 10 octobre 2026 sous `#sec-fl-comp-instances`
  (champ `ou` de la fiche : les deux chapitres) ; activité de la Haute
  instance : rien d'établi.
- **Lacunes** : modificatifs et édition arabe de la loi n° 75-33, et son sort après 2018 ;
  textes de création des agences citées par Dafflon et Gilbert et décret n° 2004-1182 (couche
  texte décalée) ; activité de la Haute instance des finances locales et existence du
  Conseil supérieur ; décret-loi n° 2026-4, art. 14 à 27, 35 à 48 et 100 à 131, à lire pour
  les compétences, les organes et le contrôle (art. 1, 55 et 56 repris de la note du
  10 octobre, § 3) ; qui adopte le budget communal et arrête un tarif depuis le
  14 mars 2023 ; **dépenses par fonction et part dans la dépense publique : aucune série
  identifiée**, à chercher dans les rapports de la Haute instance — **à obtenir**.
- **Tableau de tête** : `tbl-fl-comp-etats` suit le plan, sauf deux cases — la colonne de la loi
  organique des communes couvre 1975-2018, et sa case « qui fixe les droits » dit les deux
  régimes (approbation jusqu'en 1995, aucune approbation propre ensuite) avant le renvoi ; la « supervision du gouverneur » y est sans guillemets (traduction de travail).
- **Livre arabe** : chapitre non traduit ; douze attributs `titre` à traduire.

### Chapitre 5 — Budgets et comptes (`_budgets.qmd`) — converti le 9 octobre 2026

`.domicile-unique`, d'après `finances-locales-transferts-budgets-plan-architecte.md` (§ 3 et 4)
corrigé par les lectures du 9 octobre 2026. Plan : vue d'ensemble ; mise en place de 1975 ;
trois grandes réformes (2007, budgets de 2008 ; 2018, budgets communaux de 2019 ; 2025) ; état
du droit au 18 mars 2025 ; seuil de l'approbation ministérielle ; nomenclature ; comptable et
comptes ; longue période (sources, recettes propres et transferts, autonomie, dépenses, quatre
impôts, comptes de la nation, rapports de la Banque mondiale). Treize blocs repliés, dont dix
registres à ancres `r-fl-budg-…`. **Premier plan resserré le 9 octobre 2026** (retour de
lecture : « plus court, replier le comptable, la procédure, les vérifications ») : de 6 465 à
3 991 mots au premier plan, légendes et notes de lecture des figures comprises (repliés : de
3 927 à 5 619 mots) ; quatorze blocs au lieu de treize, toujours vingt tableaux, dont trois au premier plan au lieu
de cinq (`tbl-fl-budg-reformes`, `tbl-fl-budg-controle`, `tbl-fl-budg-art135`). Passent dans
les blocs, sans perte d'article ni de clé : le détail de l'approbation de 1975 et du recours
de 2018, l'assiette du seuil, le seuil du délégué et l'agrément des investissements,
`tbl-fl-budg-nomenclature` et l'histoire de la nomenclature, le comptable et les comptes,
`tbl-fl-lp-sources`, les exercices non clos, les notations et le calcul des deux ratios
d'autonomie, les écarts du ratio publié, le détail des rapports de la Banque mondiale. Le bloc
des définitions des transferts (`tbl-fl-lp-transferts-definition`) quitte la vue d'ensemble
pour `#sec-fl-lp-ressources` ; un bloc nouveau, sous `#sec-fl-lp-autonomie`, porte le calcul
du dénominateur et les écarts du ratio publié. Les sections « Nomenclature » et « Comptable et comptes » se
réduisent chacune à un paragraphe et un bloc. **Il accueille le chapitre « La longue période », supprimé**
(`_longue_periode.qmd`) : `fig-fl-lp-ressources` en vue d'ensemble ; `fig-fl-lp-autonomie`,
`fig-fl-lp-impots` et `fig-fl-lp-ins` dans sa longue période ; `tbl-fl-lp-sources` replié
sous `#sec-fl-lp-sources`, l'administration d'abord ; `tbl-fl-lp-ecarts` réparti par famille de sources (trois
lignes de l'administration, deux lignes dans `tbl-fl-lp-ecarts-bm`, une phrase sur 2008-2012
dans la section titrée « Selon les rapports de la Banque mondiale », une phrase sur la taxe sur
les immeubles bâtis de 2006-2007 au chapitre 6) ; la table des notations est dissoute, chaque
symbole défini où il sert. Identifiants `fig-fl-lp-…`, `tbl-fl-lp-…`, `sec-fl-lp-…` gardés.
**Deux figures nouvelles** (`figures/finances_locales.py`, sans série ajoutée au cache) :
`fig-fl-budg-depenses` (dépenses des deux titres 2002-2023, service de la dette et emprunt
2002-2012 et 2018-2023) et `fig-fl-budg-remunerations` (rémunérations rapportées aux recettes
du titre I, 2008-2023, et plafond de moitié tracé depuis 2019). **Faits nouveaux** : intitulés
du régime financier du code (édition arabe, traductions de travail) ; date de la loi organique
n° 94-44 (23 mai 1994) ; décret gouvernemental n° 2020-52 du 23 janvier 2020 (modèle de la
nomenclature budgétaire des communes, clé `decret-gouv2020-52`, FR et AR) ; décret-loi
n° 2026-4, signalé une fois. **Fiches** : `r-ccl-2018-nomenclature-art167` **résolue** par le
décret n° 2020-52 (passe du 9 octobre 2026, ancre retirée) ;
`r-lob-cl-seuil-approbation-apres-2017` toujours ouverte (`#sec-fl-budg-seuils`). **Tâches
closes** : la promesse de chiffres « au chapitre de la longue période » ; « en l'état des
textes identifiés, le dernier fixé » (l'état du droit est dit par sa date) ; les dépenses et
le service de la dette, non suivis jusque-là ; la phrase qui traversait trois bases du PIB
sans le dire (récrite base par base, avec renvoi à l'annexe). **Lacunes**, lisibles dans le
corpus sauf mention :
- ce que cherche la loi organique n° 2007-65 : ni rubrique ni exposé ; débats des 12 et
  15 décembre 2007 hors corpus, **à obtenir** (pas de requête rejouable, donc pas de fiche) ;
- modèle annexé au décret n° 2020-52 (édition arabe, p. 368 et suivantes) : **non lu** — il
  donnerait la correspondance entre articles budgétaires et prélèvements du code (figure du
  chapitre 8) et le contenu des articles 6101 et 8002 (chapitre 9) ;
- décrets des missions et programmes (code, art. 156) et du système comptable (art. 191) :
  aucun signalé par la recherche sur les titres du 5 octobre 2026 ; ils ont quitté l'objet de
  la fiche résolue et ne sont portés que par un `TODO` — à chercher au plein texte ;
- vote des budgets communaux depuis la dissolution de 2023 : non établi, **à obtenir**
  (décisions des secrétaires généraux, circulaires) ;
- art. 38-41 de la LF 1980 (lus par océrisation, à relire à l'image) et clause d'effet de
  cette loi ; date de publication du décret n° 75-485 ; arrêté de nomenclature du 6 novembre
  1975 et modèles de l'arrêté du 31 mars 2008 ; texte postérieur au décret n° 75-782 sur
  l'agrément des investissements ;
- code de la comptabilité publique (loi n° 73-81) et loi n° 68-8 sur la Cour des comptes :
  non lus ; l'emprunt avant 2018 (loi n° 75-38, LF 1980, art. 37) n'est pas au chapitre ;
- le plafond de moitié des rémunérations porte sur les prévisions : la figure ne compare que
  des réalisations ; les prévisions des budgets par commune (2018-2023) sont dans
  `tunisia-data` et permettraient le rapport de la règle — **travail de données** ;
- écart entre les agrégats et la somme des budgets par commune sur les dépenses de 2018-2019,
  non expliqué ;
- figure en escalier du seuil : après versement des onze valeurs dans la base de paramètres ;
- les dates d'exécution des lois de finances pour 1982, 1986 et 1992 (2 janvier) ne sont pas
  au registre de ce chapitre, qui ne cite pas ces lois : elles sont à celui des transferts
  (`#r-fl-transf-dates-gestions`).

### Chapitre 6 — Impôts sur les immeubles (`_impots_immeubles.qmd`) — converti le 9 octobre 2026

`.domicile-unique`, d'après `finances-locales-impots-plan-architecte.md` : vue d'ensemble ; mise
en place de 1997 ; deux grandes réformes de perception (2002, 2006-2009) ; état du droit en
2025 ; quatre dispositions (dégrèvement, contribution au fonds de l'habitat, pénalité,
abandons) ; longue période, avec `fig-fl-immeubles-rendement` et
`fig-fl-immeubles-recouvrement` sur le seul budgétaire. Treize blocs repliés, dix registres à
ancres `r-fl-imm-…`. Trois fiches : `r-cfl-prix-reference-1998-2006`,
`r-cfl-prix-reference-tib-apres-2017`, `r-cfl-tarif-tnb-apres-2017`. **Mis à jour le 9 octobre
2026 avec la dissolution de la longue période** : la phrase de l'évaluation de la Banque
mondiale sur 2006-2007 (53,5 puis 28,2 MD) y est écrite, sous son titre ; renvoi à
`@fig-fl-lp-impots` au chapitre des budgets. **Tableaux engendrés le 9 octobre 2026** : les
taux selon les services (`tbl-fl-tib-taux`), le prix de référence du mètre carré couvert
(`tbl-fl-tib-prix-reference`) et le tarif des terrains non bâtis (`tbl-fl-tnb-tarif`) viennent
de `scripts/generate_finances_locales_tables.py`, avec leur onglet « Base législative » ; les
valeurs et les dates d'effet faites main concordaient toutes (37 valeurs). Les registres repliés
des décrets restent écrits dans le chapitre. Restent faits main, faute de paramètres : la
pénalité de retard (`tbl-fl-penalite-retard`) et la contribution au fonds de l'habitat
(`tbl-fl-immeubles-fnah`). **Figures des deux barèmes faites le 10 octobre 2026** : `fig-fl-tib-prix-reference` (quatre
panneaux à axe partagé, un par catégorie) et `fig-fl-tnb-tarif` (un panneau, axe
logarithmique), chacune en dinars courants et en dinars de 2025, placées après leur tableau ;
séries `fl-tib-prix-reference` et `fl-tnb-tarif` émises au cache par le même générateur, module
`figures/baremes.py`. Les niveaux en dinars de 2025 et les hausses de prix cités dans le texte
sont écrits à la main d'après `baremes.reperes()` : à relire si l'indice de 2025 est révisé ou
si l'année de base change. **À reprendre,
d'après les lectures du 9 octobre 2026** (`finances-locales-impots-lectures-2026-10-09.md`), non fait :
- l'état du droit y est dit pour 2025 avec un `TODO` de confirmation, alors que la loi de
  finances pour 2026 est inventoriée (aucun article du code modifié, aucun abandon
  d'arriérés) : titre et section à passer à 2026 ;
- rubriques de la LF 2006 (art. 53, 56, 57) et de la LF 2009 (art. 33), relevées mot pour mot
  par la note : la réforme de 2006-2009 est encore paraphrasée ;
- LF 2002, art. 88 : la note donne 1 % à l'art. 87 et 0,75 % à l'art. 88, taux à relire à
  l'image, page à trancher (4260 ou 4261).

**Lacunes**, lisibles dans le corpus sauf mention : art. 3 du code (six exonérations annoncées,
cinq énumérées) ; pages françaises des art. 72 (LF 2019), 59 (LF 2023), 59 (LF 2024) et 76
(LF 2025) ; condition de l'abandon des pénalités des personnes morales (LF 2024, art. 59) ;
taxe au profit du Fonds national d'amélioration de l'habitat avant 2005 et produit de la
contribution depuis 2005 — **à obtenir** ; décrets de 1902, 1919, 1920 et 1948 — **à obtenir**
pour ceux d'avant 1956 ; arrêtés communaux du prix de référence, **hors corpus** ; portée du
§ 10 de l'art. 59 du décret-loi n° 2022-79 ; explication du produit de 2019 (76 MD).

### Chapitre 7 — Impôts sur l'activité (`_impots_activite.qmd`) — converti le 9 octobre 2026

`.domicile-unique` : vue d'ensemble ; mise en place en deux temps (lois n° 75-39 et 75-34, code
de 1997) ; deux grandes réformes (2012-2013, 2013-2014) avec les rubriques des lois de
finances ; état du droit en 2026 ; cinq dispositions (taxe hôtelière, forfaits, partage,
déclaration, amnisties) ; longue période avec `fig-fl-activite-rendement`. Trois fiches :
`r-cfl-minimum-tcl-apres-2017`, `r-cfl-prix-reference-1998-2006`,
`r-cfl-taxe-hoteliere-modificatifs`. **Mis à jour le 9 octobre 2026** : le `TODO` sur le nom du
fonds de 2021, devenu sans objet, est retiré ; le renvoi à la comparaison des quatre impôts
vise le chapitre des budgets. **Lacunes** : loi n° 75-34, art. 9, année de la date d'effet à
confirmer sur l'édition arabe (**à lire à l'image**) ; plafond de la taxe de 1976 à 1996
(décrets de 1975-1976 et LF 1976, 1980, 1992, non lus) ; unité du maximum dans les décrets
n° 2003-1345 et 2006-3360 ; doctrine administrative sur le chiffre d'affaires brut « local »,
1997-2013, **à obtenir** ; produit de la taxe avant ou après écrêtement au profit du fonds
depuis 2013, et série du montant écrêté, **à obtenir** ; amnisties de 2012, 2019, 2024 et 2025
(objet, années, conditions), loi n° 2006-25, décret-loi n° 2006-1, arrêté de calendrier de
2026 ; pages françaises des art. 37 (LF 2016), 42 (LF 2019), 52 et 57 (LF 2023), 67 et 69
(LF 2024) ; LF 1993, art. 39, et décrets des zones municipales touristiques ; art. 7 initial
du décret-loi n° 2020-33.

### Chapitre 8 — Taxes, redevances et autonomie fiscale (`_taxes_redevances.qmd`) — converti le 9 octobre 2026

`.domicile-unique` : vue d'ensemble ; mise en place de 1997 ; une grande réforme (2018, les
droits et redevances confiés aux conseils élus), les décrets de tarifs de 1998 et 2016 étant
des étapes ; « Qui fixe quoi : l'état du droit en 2026 » ; six sections de prélèvements ;
longue période réduite à un renvoi à la nomenclature du chapitre des budgets
(`@sec-fl-budg-nomenclature`, mis à jour le 9 octobre 2026). Huit blocs repliés, cinq registres
à ancres `r-fl-tax-…`. Fiche ouverte : `r-ccl-2018-decrets-art391` (44 fascicules arabes à
lire à l'image). **Lacunes**, lisibles dans le corpus sauf mention :
- **figure du produit des droits et redevances : non faite** ; il faut d'abord la
  correspondance entre les articles des budgets par commune et les prélèvements du code
  (modèle annexé au décret n° 2020-52, non lu) — travail de données dans `tunisia-data` ;
- annexes des décrets de tarifs : aucune valeur transcrite (annexe française de 1998 rognée,
  édition arabe du JORT n° 59 de 1998 **à lire à l'image** ; annexe de 2016 à transcrire) ;
  six modificatifs du décret de 1998 connus par leur intitulé, sans clé ;
- **avant 1998** (porté le 10 octobre 2026 à `#sec-fl-moduler-droits`) : `tbl-fl-taxes-pouvoir`
  commence en 1975 — deux lignes, 22 mai 1975 et 6 décembre 1990 —, registre
  `tbl-fl-taxes-textes-1975-1995` (loi n° 75-35, art. 11 ; lois organiques n° 75-33, 85-43 et
  95-68 ; décret n° 90-1960) ; l'art. 93 du code reprend l'art. 8 du décret
  n° 90-1960. **Reste, lisible dans le corpus à l'image** : décret n° 90-1960, p. 1849-1853
  (tarifs laissés à la collectivité ; clause d'effet, la date du 6 décembre 1990 étant calculée
  sur les seuls art. 8 à 10) ; décrets n° 76-826, n° 95-1121 et n° 58-234, connus par leur seul
  intitulé ; la case « Contrôle » de 2016 reprend l'exception des déchets non ménagers
  (art. 93 du code, sans modificatif au registre du chapitre) : **à confirmer** ;
- loi n° 2002-76, art. 3 (réduction de moitié pour les cas sociaux après le 1er août 2002) ;
  barème des parkings de la LF 2003, art. 79, à transcrire ; arrêtés du 4 mars 1997 et du
  30 mai 2003 ; antécédents abrogés en 1997 (décrets de 1887 à 1956, **à obtenir** ; loi
  n° 71-41) ;
- qui arrête un tarif communal depuis le décret-loi n° 2023-9 : non établi ; délibérations
  tarifaires de 2019 à 2023 au *Journal officiel des collectivités locales*, **hors corpus**.

### Chapitre 9 — Les transferts de l'État (`_transferts.qmd`) — converti le 9 octobre 2026

`.domicile-unique` : vue d'ensemble ; mise en place de 1975 ; trois grandes réformes (1987,
2001, 2018 avec son second temps de 2021) ; répartition légale 1976-2017 ; état du droit au
14 juillet 2021 ; réserve ; caisse ; longue période. Treize blocs repliés. `fig-fl-lp-fccl` et
`fig-fl-lp-cpscl` y sont montées. Fiches : `r-fccl-repartition-reserve-2014-2017`,
`r-fl-criteres-subventions-apres-2021`, `r-fl-decret-fonds-appui-decentralisation`. **Mis à
jour le 9 octobre 2026 avec la dissolution de la longue période** : ses renvois aux sources et
aux écarts de 1990 visent le chapitre des budgets (`@sec-fl-lp-sources`,
`@tbl-fl-lp-ecarts-bm`). **Lacunes**, lisibles dans le corpus sauf mention :
- décrets de répartition de la réserve de 1993 à 2013 (vingt-deux, connus par leur intitulé) ;
- montant du fonds, LF par LF : **versé de 1976 à 1995 sauf 1979** (série
  `finances-locales-fccl-lois-de-finances`, snapshotée le 9 octobre 2026 et tracée dans
  `fig-fl-lp-fccl` en famille à part, deux segments séparés par la rupture de définition de
  1987 ; grandeur retenue pour 1987-1995 : le total des recettes du fonds, non la seule
  subvention). **Restent** : 1979 (tableau des fonds spéciaux de la loi n° 78-59 non localisé,
  numérisation dégradée — OCR ou relecture à l'image) ; 1996-2017, où le tableau n'imprime plus
  le montant (1996 et 1997 lus, 1998-2010 à vérifier dans le corpus) : à chercher au budget du
  ministère de l'Intérieur par chapitre, aux lois de règlement et aux décrets de répartition ;
  exécution de 1976-1982 aux rapports annuels de la Banque centrale, repérée, non versée. La
  série votée n'a **pas de vue au PIB** : `cnat-pib-nominal` commence en 2001, et avant 1992
  le seul PIB courant du cache (`pib-courant-enchaine`, variante accolée) est d'une base non
  dite ; la base 1983 publiée ne couvre que 1992-1995. La série a vingt et une clés de loi de
  finances au catalogue des données, absentes de la bibliographie du volume : le module de
  figures déclare sa provenance avec une ligne de source unique (**à verser par le
  bibliographe** si l'on veut les citer une à une) ;
- montant annuel des subventions depuis 2018 ; LF 1977-1979 et arrêtés de 1975-1983 ; montants de 1990-1991 au
  profit de la caisse à relire à l'image ; les tableaux des LF de 2022 à 2026 semblent en
  image — **OCR à prévoir** ;
- décret n° 2013-2797 (fonds de coopération) et LF 2013, art. 13-15, sans clé pour le décret ;
  base des proportions de 90 % et 10 % : non dite par la loi ;
- décret du fonds d'appui et modificatif de l'arrêté après le 29 juin 2021 : non identifiés
  (deux fiches ; fascicules sans couche texte à océriser) ;
- ce que cherche la loi n° 2000-60 : débats du 8 juin 2000, **à obtenir** ;
- décrets et arrêtés de la caisse (n° 77-212 … 2016-367, loi n° 2001-56) ;
- subventions d'investissement, programmes d'investissement communal et régionaux, dotation
  exceptionnelle de 2011-2012 : aucune source primaire lue ;
- divergence 82 / 50,8 MD du fonds en 1990 : non tranchée (le JORT donne 80 MD votés) ; le
  rapport de 1997 vaut de 63,5 % à 65,1 % des montants votés en 1990, 1992, 1994 et 1995,
  ordre de grandeur de la part légale des communes (75 % × 86 %) — constat dit au chapitre,
  clé non vérifiée ;
- l'onglet « Sources » de `fig-fl-lp-fccl` reprend les réserves du catalogue des données pour
  `finances-locales-communes-agregats` (« réserve à 18 % jusqu'en 2017, 15 % ensuite ») et
  pour `finances-locales-bm-1985-2012` (« vraisemblablement fonds total contre quote-part des
  communes ») : à accorder, dans le dépôt des données, avec le chapitre, qui dit que la ligne
  de 2018-2019 n'est plus la réserve et ne tranche pas l'écart de 1990 ;
- vue au PIB de `fig-fl-lp-fccl` : le libellé « PIB : base 2015 » chevauche les courbes de
  2012-2014 (antérieur à l'ajout de la série votée) ;
- code des collectivités locales, art. 146-151 et 392 : lus en arabe seulement ;
- contenu des articles 6101 et 8002 des budgets communaux de 2022-2023 au regard des parts de
  90 % et 10 % : non établi (modèle annexé au décret n° 2020-52, non lu).

## Forme des chapitres — le plan type, et où il ne s'applique pas

**Tout chapitre décrivant un dispositif suit le même déroulé** : l'historique d'abord,
jusqu'à la création du dispositif ; sa description, paramètres d'origine compris ;
l'évolution, **une sous-section par grande étape**, chacune portant à la fois l'intention du
texte et le mouvement des paramètres ; enfin la longue période, puis les données. Les
tableaux de synthèse sont groupés en un seul endroit, pour que la consultation reste possible
sans relire le récit.

Ce plan ne s'applique **pas partout**, et c'est un résultat, non une réserve. Il décrit un
dispositif dont la substance *est* un jeu de paramètres datés — un impôt. Pour un régime de
retraite, dont la substance est un jeu de règles qui s'emboîtent, il détruirait de
l'information.

| Chapitre | Forme | À faire |
|---|---|---|
| `_impot_societes.qmd` | conforme | — |
| `_impot_fortune.qmd` | conforme ; s'achève sur une case vide (aucune série de rendement) | traduction arabe à déclarer dans le `_quarto.yml` AR |
| `_droits_consommation.qmd` | historique remonté en tête | la chronologie du périmètre reste un tableau sans récit texte par texte — signalé, non confirmé |
| `_tva.qmd` | **prototype du chantier « ruptures au premier plan »** (7 octobre 2026, à juger) : en bref, mise en place, grandes réformes, bilan des taux et état du droit, dispositifs, longue période | voir l'entrée du chantier en tête de ce fichier ; `@sec-tva-deduction` garde ses données et ses études à leur place ; les données du crédit sont une figure engendrée (`@fig-tva-credit-restitutions`), dont les séries restent à prolonger après 2014 ; le tableau des générations de taux (`@tbl-tva-taux`) et la figure des taux dans le temps (`@fig-tva-taux`) sont engendrés depuis le 7 octobre 2026 ; vue des régimes par catégorie (`@fig-tva-regimes`) et annexe des tableaux annexés au code (`_tva_tableaux.qmd`, non déclarée côté arabe) ajoutées le 7 octobre 2026 |
| `_impot_revenu.qmd` | conforme, à sa manière | rien sur la forme ; restent deux sections à ÉCRIRE, voir plus bas |
| `retraites/_secteur_*.qmd` | **rangés par mécanisme, et c'est bien** | ne pas y appliquer le plan type |
| `_regime_indiciaire.qmd` | **converti le 8 octobre 2026** aux principes « ruptures au premier plan » : trame du volume gardée, vue d'ensemble, registres repliés, domicile unique | voir l'entrée « Rémunérations publiques » ; à relire |

### Ce que `_impot_revenu.qmd` a appris sur les limites du plan type

Ce chapitre devait être réorganisé en trois passes. La première a remonté ses titres d'un
cran — le régime moderne vivait sous un titre nu qui coûtait un niveau à tout ce qu'il
abritait. **La deuxième a été abandonnée après lecture, et c'est un résultat à conserver.**

Le diagnostic initial — « cinq chronologies parallèles à fondre en une colonne par réforme »
— reposait sur cinq titres `## L'évolution de…`, non sur leur contenu. À la lecture, les cinq
ne sont pas comparables : « L'évolution du minimum d'impôt » ne contient AUCUNE prose, c'est
un TODO seul ; « L'évolution des régimes dérogatoires » est une description assortie de deux
TODO ; et « L'évolution de l'assiette », qui pèse 232 des 380 lignes en cause, parcourt les
sept catégories **dans l'ordre de l'article 8**. Cette structure est imposée par la loi, non
choisie : la disperser dans une colonne chronologique y détruirait la même information que le
plan par réforme détruirait dans les retraites.

**La leçon, qui vaut pour toute réorganisation à venir : compter les titres ne diagnostique
rien, il faut lire ce qu'ils portent.** Un chapitre peut sembler mal rangé et suivre en
réalité une structure que la loi lui impose.

Le défaut réel, une fois mesuré, était plus étroit : cinq lois de finances racontées à deux
endroits sans qu'on dise jamais qu'il s'agit d'un seul geste. Il s'est corrigé en AJOUTANT la
couche qui manquait — une section « La longue période », qui rapproche notamment deux
immobilités que les sections par paramètre ne pouvaient pas voir : le barème gelé
vingt-sept exercices et les charges de famille vingt-neuf, à partir des mêmes revenus de
1990. Non en démontant la structure.

Ce qui reste sur ce chapitre ne relève plus de la forme mais du documentaliste.

Pour toute passe qui DÉPLACE de la prose, le **balayage phrase à phrase** de l'original
contre le résultat n'est pas optionnel : sur l'impôt sur les sociétés, deux fois plus court,
il avait rattrapé deux pertes sans citation, donc invisibles au décompte.

## Le PIB et ses changements de base — annexe du site et mise en conformité des volumes (6 octobre 2026)

**Fait.** L'annexe `precis/fr/annexe-pib.qmd` est écrite (page de site, rendue par `build.sh`
comme `a-propos`, liée depuis l'accueil et le pied de page des huit volumes français). Matière :
`docs/notes/annexe-pib.md`. Ancres stables auxquelles les volumes renvoient : `#sec-pib-bases`,
`#sec-pib-ecarts`, `#sec-pib-retropolation`, `#sec-pib-sources`, `#sec-pib-ruptures`,
`#sec-pib-lire`, `#sec-pib-definition`, et par changement de base `#pib-base-1997`,
`#pib-base-2015` (plus `#pib-base-1983`, `#pib-annee-de-prix`, `#pib-series-accolees`,
`#tbl-pib-jonctions`).

**Règle à appliquer partout** : toute grandeur rapportée au PIB nomme la base, dit si le PIB est
recalculé pour le passé ou non, trace les changements de base et renvoie à l'annexe. Modèle à
généraliser : `finances_locales/figures/finances_locales.py` (`_pib`, `_pib_par_base`,
`_ruptures_pib`).

**Inventaire** (note, § 4.2) : 25 emplois du PIB dans six volumes — 4 conformes, 8 partiels,
13 non conformes. À mettre en conformité **dans des PR distinctes, une par volume** ; rien n'a
été touché dans les volumes ici.

- **Fiscalité — 8 emplois non conformes.** Les quatre figures de rendement (`figures/irpp.py`,
  `impot_societes.py`, `tva.py`, `droits_consommation.py`) rapportent les recettes au PIB du
  ministère des Finances sans dire sa base ni tracer ses changements de niveau (1997, 2002, 2005,
  2010) ; la légende de l'impôt sur les sociétés présente l'écart de 5 % de 2012-2014 entre ses
  deux colonnes de PIB sans dire que c'est un écart de base. Quatre phrases chiffrées à reprendre :
  `_impot_revenu.qmd` (« de 1,9 % à plus de 6 % », 1990-2016), `_impot_societes.qmd` (« 1,86 % …
  3,77 % »), `_tva.qmd` (« 6,5 % en 1988, 5,1 % en 1997… » : 1997 est l'année du changement de
  niveau de 9,8 %), `_droits_consommation.qmd` (maximum de 1994 en base 1983 comparé à la suite en
  base 1997).
- **Rémunérations publiques — 5 emplois non conformes.** `fig-masse-salariale-ratios` (et sa
  reprise dans `_demo_figure_onglets.qmd`) annonce un « PIB en base 2015 » alors que 1990-1996
  n'est pas dans cette base, que 2002-2004 ne se rattache à aucune base et que **2012-2014 sont
  en base 1997** : la part publiée vaut 12,30 %, 12,79 % et 13,03 % ; rapportée au PIB en base
  2015 recalculé par l'INS, 11,71 %, 12,15 % et 12,35 % ; le « reflux » de 2014 à 2015 est un
  effet de base. Phrase de `index.qmd` (« 11 à 12 % … 16,1 % en 2020 … ») à reprendre. Figure B
  de `masse_salariale.py` : « base 2010 (×1,06) » — il n'existe pas de PIB nominal « base 2010 »,
  et le coefficient unique est appliqué à 1990-2025 alors qu'il n'est mesuré que sur 2015-2017.
  Citations du FMI (17,6 % en 2020 : PIB en base 1997, établi) et de la Banque mondiale (14,7 %
  en 2017, 10,7 % en 2010 ; `_regime_conventionnel.qmd`, transferts aux entreprises publiques,
  8,9 % en 2013 et 7,5 % en 2014) : dire la base, ou dire qu'elle n'est pas précisée par la
  source (revue des dépenses publiques de 2020 à relire sur ce point).
- **Figures de la CNSS, 1990-2004 — 6 figures partielles, même défaut** : le changement de
  1997 est tracé et dit ; celui de **2002** (valeurs du ministère non rattachées, 2002-2004) ne
  l'est pas.
  - **Caisses** (`_comptes_longue_periode.qmd`) : `fig-cnss-regimes`,
    `fig-cnss-assurances-sociales`, `fig-cnss-atmp-pst`.
  - **Cotisations** (`_bilan.qmd`) : cotisations par branche ; les modules `cnss_*` du volume
    sont des liens symboliques vers ceux des caisses — une même PR pour les deux volumes.
  - **Prestations** (`_prestations_familiales.qmd`) : allocations familiales.
  - **Retraites** (`_secteur_prive.qmd`) : branche des pensions du RSNA.
- **Retraites — 1 groupe partiel** : les deux figures du barème d'actualisation
  (`bareme_actualisation.py`) ; dire les années de la réserve d'avant 1993 (taux de 1970 à cheval
  sur deux séries ; taux de 1983 et 1985 appuyés sur des valeurs de 1983-1984 propres à la Banque
  mondiale).
- **Finances locales — conformes depuis le 9 octobre 2026** : la phrase qui traversait trois bases
  est récrite base par base (`_budgets.qmd`, `#sec-fl-lp-ressources` et `#sec-fl-lp-bm`) ; le
  paragraphe local sur les bases renvoie à l'annexe ; les notes de lecture de
  `fig-fl-lp-ressources`, `fig-fl-lp-impots` et `fig-fl-lp-ins` disent la base par segment. Les
  points de 1985-1991 de `fig-fl-lp-fccl` (chapitre des transferts) restent rapportés au PIB d'un
  rapport de la Banque mondiale de 1992 dont la base n'est pas dite — la note de lecture et le
  tableau des sources le disent. Les montants votés de 1976-1995, ajoutés à cette figure le
  9 octobre 2026, n'y sont tracés qu'en dinars courants, faute de PIB à base dite avant 1992. Les deux figures nouvelles des dépenses et des rémunérations
  n'ont pas de vue au PIB.
- **Marché du travail** : aucun emploi du PIB relevé.

**Figures de l'annexe — fait le 6 octobre 2026.** `#fig-pib-volume` (sous-section
`#pib-croissance-volume`), deux vues : tous les taux de croissance en volume de 1961 à 2025
(comptes tunisiens en ronds de la couleur de leur base, Banque mondiale en croix, taux retenu en
trait, neuf jonctions étiquetées base / année de prix / série / source, 1962-1965 sur fond gris) ;
les deux indices enchaînés, prix courants et volume. `#fig-pib-bases` (sous-section
`#pib-croissance-longue-periode` ; le `TODO (rédacteur)` de `#sec-pib-ecarts` est levé), trois
vues, toutes aux prix courants : niveaux des bases 1983, 1997 et 2015 sur leurs années (tronçons
rétropolés par l'INS distingués) ; croissance calculée à l'intérieur de chaque base, 1962-2025 ;
série accolée et série enchaînée, en indice et en taux, les deux taux faux de 1997 et de 2010
marqués. Module `precis/fr/figures/annexe_pib.py`. La règle 2 de `#sec-pib-ruptures` dit
désormais que la série enchaînée n'est qu'une illustration.

- **Snapshots.** `pib-courant-enchaine`, `pib-croissance-par-base`,
  `pib-courant-recouvrements`, `pib-croissance-volume` et `pib-volume-enchaine`
  (`precis/_seriescache/`) sont pris sur `main` de `tunisia-data` (`b6e412c`, 6 octobre 2026) :
  CSV identiques, octet pour octet, à ceux de l'entrepôt.
- **Câblage d'une figure de page de site.** Le module est dans `precis/fr/figures/` (lien
  symbolique `precis/ar/figures`), les sorties à côté de la page (`precis/<langue>/_fig/`,
  ignoré, et `precis/<langue>/figdata/`, versionné) ; `build.sh` copie ces deux dossiers dans le
  site. `scripts/verifier.sh` ne rend aucune page de site et ne restaure pas
  `precis/<langue>/figdata/` : la page se contrôle par `./build.sh --no-pdf`. Une modification
  du seul module `precis/fr/figures/annexe_pib.py` ne fait rendre aucun livre
  (`verifier_livres.livres_touches`), ce qui est exact — mais rien ne rend alors la page.
- **Ligne « Source » et onglet « Sources ».** Le module remplace, pour l'affichage, le libellé
  des bases, le périmètre et les réserves du catalogue de l'entrepôt par un texte pour le
  lecteur, en français et en arabe (`PROVENANCE_LECTEUR`, comme `masse_salariale.py`) : ni nom
  de colonne, ni consigne de filtrage, ni chemin de fiche dans la page rendue. À relire si le
  catalogue change.
- **Reste à faire, en amont.** Les colonnes `jonction`,
  `source`, `base` et `annee_de_prix` des séries en volume n'existent qu'en français : les
  infobulles de la page arabe les reprendront telles quelles. Divergence de 1962-1965 entre la Banque mondiale et la série des
  Nations unies, et taux de 1970 : à départager sur pièces (rapports annuels de la BCT,
  mémorandums de la Banque mondiale de 1978 et 1985 — `docs/pib-croissance-volume.md` de
  l'entrepôt). Étiquettes à corriger :
  `masse-salariale-ratios` (`base_pib: 2015`), `irpp-ratios` (`pib_cnat_MDT`, 2012-2014),
  `masse-salariale-reconciliation` (« base 2010 »).
- **Bibliographie.** `undata-sna` et `wb-wdi` sont promues au fonds commun
  (`precis/{fr,ar}/references.json`) et retirées de `retraites/references.json` : l'onglet
  « Sources » affiche leur titre et leur lien. `wb-wdi` est reprise à l'identique de la branche
  de la compensation, qui la promeut aussi : à la fusion des deux branches, ne garder qu'une
  entrée. `bct-ra` reste à remonter.
- **Pied de page.** Le lien vers l'annexe est au pied de page des huit volumes de `master` ; le
  neuvième volume (la compensation) arrive par une autre PR : y ajouter le même lien à sa
  fusion.
- **Arabe.** La page arabe n'existe pas encore ; les libellés arabes de la figure sont dans le
  module et sont à relire avec la traduction de la page (« سلسلة مسلسلة » pour la série
  enchaînée, « موصولة دون تصحيح » pour la série accolée, repris du catalogue de l'entrepôt).

**Reste non établi** (note, § 5, L1 à L9) : comptes d'avant la base 1983, date d'entrée en
service de celle-ci et profondeur de son recalcul ; CD de l'édition 2005-2009 ; méthode du
recalcul 2010-2014 et toute série en base 2015 avant 2010 ; base du PIB dans la revue des
dépenses publiques de 2020 ; origine des valeurs 2002-2004 du ministère des Finances ; PIB
définitif en base 1997 pour 2018-2020 ; termes arabes de « rétropolation » et de « changement
de base ». Supports : publications de l'INS et rapports de la BCT, hors *Journal officiel* —
le registre `docs/recherches.yml` ne peut pas les porter sans extension de
`scripts/recherches.py` ; la page porte des `TODO (documentaliste)` à la place d'ancres.

**Arabe** : `precis/ar/annexe-pib.qmd` viendra de la traduction après fusion (`build.sh` saute
la page absente). Ensuite, à la main : ajouter le lien d'annexe au pied de page des huit
`_quarto.yml` arabes et à `precis/ar/index.qmd` s'il n'y est pas ; vérifier que les
identifiants `{#…}` sont restés tels quels. Glossaire : la page ne peut pas ancrer le glossaire
(engendré par livre) ; les notions de la note (§ 8) sont définies dans le texte et restent à
verser par le terminologue quand un volume les emploiera.

## Ce qui traverse les livres

- **Traductions arabes en retard sur leur code (relevé et rattrapage du 3 octobre 2026).**
  Le garde-fou des cellules Python de `translate_sync` signalait dix chapitres arabes dont les
  cellules manquaient ou différaient du français. Neuf sont rattrapés par retraduction complète
  (`translation-sync`, `traduction_complete`) : `retraites/_secteur_prive` et `_secteur_public`
  (#331, #333), les cinq fichiers de `fiscalite` (#334), `remunerations_publiques/index` et
  `_demo_figure_onglets` (#335), `retraites/index` (#336) ; parité, cellules et rendu arabe
  vérifiés, et six intertitres des retraites recollés à la ligne précédente remis en titres.
  Le dixième, `remunerations_publiques/_regime_indiciaire`, a d'abord été rejeté deux fois : les
  cellules `fig-salaire-moyen` et `fig-emploi-public`, dont la `note_lecture` porte des « », ne
  compilaient plus. Côté outil (#338, #339), le code des cellules est désormais masqué avant
  l'envoi : le modèle ne voit que le texte des chaînes, d'un tenant, et le code est réinjecté à
  l'identique. `translate_sync` rétablit aussi les liens relatifs entre livres et la ligne vide
  devant les titres. Les quatre chapitres des rémunérations publiques (`_regime_indiciaire`,
  `_regime_conventionnel`, `_regime_marche_controle`, `_regime_statutaire_autonome`) ont été
  retraduits en entier le 3 octobre (#340) : parité, 10 cellules sur 10, liens et citations
  identiques au français, rendu arabe sans citation non résolue et avec toutes ses figures.
  Les jetons corrigés à la main sur #331, #333 et #343 — clés déformées (`@looi81-6`), renvoi
  traduit (`@tbl-somme-three-texts`), locateurs traduits (« art. 48 إلى 50 »), liens de
  glossaire ajoutés — sont désormais rétablis par `translate_sync` avant le contrôle de parité
  (`restore_citation_keys`, `remove_extra_glossary_links`, `restore_locators` apparié par clé).

- **Zotero** : le rangement a été corrigé le 29 septembre (535 références présentes,
  aucun défaut restant alors). Depuis, deux nouvelles clés du livre « Prestations
  sociales » — `loi2017-47` et `arrete-2025-07-10-appui-occasionnel` — et la clé
  commune `cnss-retrospective-1990-2004` (3 octobre) attendent leur versement **après revue** ; elles sont recensées dans `biblio-a-rapatrier.md`.
  Recontrôler la préservation des URL et notes par langue au diff de la descente.
- **Titres arabes et glossaire** : des notices restent en français dans la bibliographie
  arabe et des notions sont encore à valider (issues #151, #77, #54, #53). Recompter
  avant de réutiliser les totaux anciens de 69 notices et 26 termes.
- **Tableaux engendrés** : la règle est que tout tableau de paramètres vienne des dépôts
  openfisca par un générateur. Retraites et Prestations sociales y dérogent provisoirement.
- **Version arabe** : produite par la CI ; rendre tout livre traduit avant de fusionner
  la PR de traduction. `uv run python scripts/traduction_en_retard.py --detail` ne signale
  **aucun fichier français en avance sur l'arabe** au 3 octobre, après le rattrapage des
  rémunérations publiques (#340).
- **Garde-fou de troncature — CORRIGÉ le 20 septembre.** Il était enveloppé dans
  `if old_target_text:` et ne s'exécutait donc pas en retraduction complète, le mode où la
  troncature est la plus probable. Mesuré sur le vrai script : un chapitre arabe de 175 lignes
  était écrasé par une réponse de 3, la passe sortant en 0. Il se règle désormais sur la
  SOURCE à défaut d'ancienne cible, et trois épreuves lui interdisent de redevenir
  conditionnel.
- **Traduction du gros chapitre des prestations** : les PR #157 et #159 ont montré
  qu'une traduction complète tronquait le chapitre et qu'une mise à jour partielle
  multipliait les écarts de parité. Les nombres de lignes relevés lors de ces PR ne
  décrivent plus le fichier actuel. Examiner la stratégie de découpage ou de
  traduction par sections avant une retraduction complète.

## Suite proposée

**Point d'arrêt du 30 septembre 2026.** Le repère de bonification de l'article 32 est
établi au **5 mai 2019** dans le livre « Retraites », le glossaire et le dossier. Pour
reprendre sans refaire la même recherche :

- **D'abord, les textes locaux déjà lisibles** : loi n° 2009-39 et décret n° 2009-2085
  pour les conditions du départ anticipé public ; puis les autres lectures de la liste
  ci-dessous, un sujet à la fois, en mettant ce backlog à jour avec chaque chapitre.
- **Côté modèle**, comparer le repère de l'article 32 et sa date à l'état publié dans
  `openfisca-tunisia` avant toute correction : la date du **5 mai 2019** ne se déduit
  pas du calendrier des âges de départ au 1er juillet 2019 et au 1er janvier 2020.
  Ne pas régénérer un tableau du précis depuis une correction non publiée du modèle.
- **Chaîne éditoriale en attente** : les deux clés des « Prestations sociales » à verser
  dans Zotero après revue, avec comparaison FR/AR à la descente ; puis les traductions
  arabes en retard, à recontrôler au retour du budget de traduction et à rendre avant
  toute fusion. Les sources du PNAFN et les annexes des statuts des caisses restent à
  obtenir hors du corpus JORT.

1. **Lire ce qui est déjà textuel** : loi n° 2009-39 et décret n° 2009-2085
   (Retraites) ; décret-loi n° 2024-4 (Cotisations) ; décret n° 2018-626 et LF 2025,
   art. 26 (Prestations) ; décrets n° 97-1368 et 2015-1768 (Fiscalité) ; décret
   n° 2015-2217 (Rémunérations). Vérifier chaque article à sa page, pas seulement
   la présence du fascicule.
2. **Océriser par cible**, avec contrôle à l'image : loi n° 65-17 (étudiants), décret
   n° 75-952 (indemnités familiales), code fiscal de 1990 (annexe II) et code TVA
   de 1988. La convention bancaire arabe de 2014 est **extractible après NFKC**,
   sans OCR. Les fascicules sont déjà locaux ; l'OCR ne peut créer une annexe absente.
3. **Chercher hors corpus** : montants/dates PNAFN auprès de l'administration, statuts
   annexés du personnel des caisses, méthode du barème d'actualisation des retraites.
   Les fascicules français non disponibles en ligne des LF 2025/2026 demandent un
   traitement distinct : extrait français local pour 2025, édition arabe pour 2026.
4. **Entretenir la chaîne éditoriale** : après revue des deux références nouvelles,
   les verser dans Zotero et inspecter la descente ; après réouverture du budget de
   traduction, rattraper l'arabe et rendre les livres concernés.

`todo-localisation.md` donne le point de départ pour les numéros et pages, **pas un
décompte actuel de disponibilité** : un fascicule qui y manque peut depuis avoir été
téléchargé (décret-loi n° 2024-4, par exemple), ou un chemin « français » servir
en réalité l'édition arabe.

# Ce qui reste à faire, livre par livre

**Révisé le 25 octobre 2026** (passe de mise en accord avec les fusions du 19 au 23 octobre :
états « non commité », « en cours », « à juger » rapportés à ce qui est sur `master`). Cette note rassemble les chantiers encore visibles dans les
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
Le prototype a été jugé et étendu : les conventions de rédaction (§ 4), la consigne du rédacteur
et le rôle « architecte » sont en place ; les finances locales (9 et 10 octobre), les prestations
sociales (10 octobre), les incitations et dépenses fiscales (11 octobre) sont au format. Les
chapitres écrits depuis (douane, timbre, boissons, épargne, rupture et durée du travail) y sont
nés. Le format n'est pas encore appliqué aux chapitres antérieurs des retraites, des cotisations
et des rémunérations publiques ; la table « Forme des chapitres » en bas de ce fichier dit où il
ne s'applique pas.

**Chapitre de la TVA au format « ruptures au premier plan » — sur `master` depuis le 12 octobre
2026 (dernière retouche le 23 octobre 2026, fusion des clés en doublon, #512).** `_tva.qmd` est réécrit selon
`docs/notes/fiscalite-tva-plan-architecte.md` (§ 2, corrigé par le § 11) et
`docs/notes/fiscalite-tva-objets-des-reformes.md` : en bref ; mise en place 1988-1990 ; quatre
grandes réformes et une clôture « depuis 2018 » ; bilan des taux et état du droit ; huit
sections de dispositif, chacune avec son registre replié ; longue période. Réorganisation sans
perte : les 62 clés, les 163 couples (clé, localisateur), les 38 ancres de glossaire, les
15 identifiants, les 6 TODO et l'ancre RECHERCHE du départ sont tous à l'arrivée. Le texte
passe de 11 000 à 22 300 mots, dont 13 000 au premier plan (8 300 au départ) : seize blocs
repliés (`.chronologie-repliable`, compte du 25 octobre 2026). Reste à faire :

- **trajectoires par opération : tranché le 7 octobre 2026** — le propriétaire garde le tableau
  (`@tbl-tva-trajectoires`, dans `#sec-tva-etat-du-droit`) et la matrice des régimes par
  catégorie ; la section en prose `#sec-tva-trajectoires` est supprimée. Ce qu'elle seule
  portait (contrats maintenus à 6 % en 1996, article 7 en 2017, détail de 2023, reports du
  logement et des médicaments, numéro 48 du tableau A) est en cinq puces sous le tableau, et son
  registre (`tbl-tva-trajectoires-textes`, 19 ancres) est déplacé sous lui, inchangé. « Les
  dispositifs qui aménagent la taxe » n'a plus que deux sous-sections ;
- **frise des réformes : faite le 24 octobre 2026** (`#fig-tva-frise`, « Vue d'ensemble » ;
  `figures/tva.py`, relevé tenu à la main `tva/frise-reformes.csv` avec son manifeste). Jalons : les
  six périodes du chapitre, la naissance de six dispositifs dans le code de 1988 et 15 ruptures
  retenues selon une règle (une par dispositif et par date, lignes jumelles fondues, registre des
  catégories écarté ; règle au manifeste), chacune avec son ancre `r-tva-…`, son texte et son article. Une loi
  à date d'effet non établie (forfaits de 1993 ; le retrait du tableau B de 1996 est daté du 16 juillet 1997 depuis le 24 octobre 2026) : losange creux,
  posée à l'année de la loi ; 2014 (achats en espèces) et 2016 (facture électronique) : cercle
  creux, classement à confirmer. Reste : libellés arabes de la frise (relecteur-ar), étapes et
  ajustements non tracés (ils restent aux registres) ;
- **quatre clés versées le 24 octobre 2026** (`precis/{fr,ar}/fiscalite/references.json`, pièces
  relues ; `docs/notes/biblio-a-rapatrier.md`) : `minfin-plf-2018` (exposés des motifs des art. 28 et 45
  du projet, lus à l'image p. 91-92 et 146-149 ; cité au paragraphe de la réforme de 2016-2018,
  avec les taux des pays voisins que l'exposé donne ; la prévision de 313 MD par an reste non
  écrite : chiffre sans vue d'évolution, `TODO (rédacteur)` maintenu), `dgi-nc-5-2023` (note
  commune n° 5/2023 ; la note préparatoire la nommait `dgelf-nc-2023-05`, la clé suit la forme des
  autres notes communes ; citée p. 1, 2 et 4, avec `dgelf-code-tva-2021`, art. 7, numéro 3, p. 23, pour
  la liste des professions), `rectificatif-lf-1993` (JORT n° 33 du 4 mai 1993, p. 579, lu à l'image en
  français et en arabe ; cité à la ligne de 1993 du registre des forfaits), `minfin-plf-2014`
  (exposé des motifs des art. 34 et 35 du projet, lu à l'image, p. 77 imprimée ; une phrase au
  paragraphe des achats en espèces). Versées dans Zotero (absentes de la liste « à créer » du dry-run du 25 octobre 2026) ;
- **classements à confirmer** : 2014 (achats en espèces) et 2016 (facture électronique) sont
  portés « rupture » dans leurs registres, que le plan donnait pour « possibles » ;
  `tbl-tva-suspension-sectorielle` garde sa forme d'origine, sans colonne « Portée » ;
- **registres bornés à ce que le chapitre établissait** : les lignes que seules les notes
  `fiscalite-tva-reformes.md` et `fiscalite-tva-deductions-documentation.md` connaissent (plan,
  § 5 : colonnes « N2 », « N3 ») ne sont pas versées — retouches des tableaux A, B et C de
  1989 à 1994 (versées le 24 octobre 2026 aux registres des taux, des exonérations et des dates,
  lues à l'image : LF 1989 art. 21 à 25, LF 1991 art. 33 à 36 et 60, LF 1992 art. 35 à 42, LF 1993
  art. 79 à 94, LF 1994 art. 50 à 54, 60 et 61 ; numéros d'alinéas de la LF 1989 relevés dans l'édition du code de 2008 ; LF 1995 art. 76, 81, 82, 84, 86 et 88 et LF 2014 art. 31-33, 64-65 versées le 24 octobre 2026 ; LF 2016 art. 75 § 4 (art. 13 quater, p. 3160), LF 2019 art. 64 et 79, LF 2021 art. 26, LF 2024 art. 39 et 50, LF 2025 art. 59 et LF 2026 art. 46-47 versées), lois de finances pour 1997 (art. 19, texte non retrouvé dans l'extraction), quatre lignes de la restitution, retouches de l'article 9 connues par le seul code
  consolidé. Texte présent au corpus pour la plupart ; lectures à confirmer à l'image avant
  versement ;
- **décret n° 97-1339 du 14 juillet 1997 : trouvé le 24 octobre 2026** (JORT n° 57 du 18 juillet 1997,
  p. 1274, absent de `jort_cache` ; clé `decret-97-1339-tva-carburants`). Il fixe au 16 juillet 1997
  l'entrée en vigueur de l'art. 40 de la LF 1996 (hors électricité basse tension domestique) et le
  taux de 10 % sur l'essence, le gasoil, le fuel-oil domestique et le gaz de pétrole ; écrit aux
  registres des réductions annuelles, des taux et des catégories et à la frise (date établie) ;
- **état du droit des règles de base en 2026** : la grille est établie ; le tableau A et le
  tableau B en vigueur sont donnés en annexe (`_tva_tableaux.qmd`), d'après l'édition du code à
  jour au 1er janvier 2025 et la loi de finances pour 2026 — voir l'entrée « TVA — régimes par
  catégorie et tableaux annexés » ; contenu des art. 46 et 47 de la loi de finances pour 2026 à
  détailler au registre `tbl-tva-taux-perimetre` (relevé en annexe, bloc de la loi de finances
  pour 2026) ;
- **longue période : faite en partie le 24 octobre 2026.** `#fig-tva-rendement` est tracée base par
  base (1983, 1997, 2015, série `pib-courant-par-base`, jamais raccordées ; années à deux points ;
  1988-1991 en base 1983 présumée ; valeurs du ministère non rattachées en losanges ; changements
  de base marqués ; quatre réformes en bandes ; rapport aux dépenses de l'État inchangé) et le
  texte dit la base de chaque pourcentage ; `#fig-tva-indirects` (part de la TVA, des droits de
  douane, des droits de consommation et des autres recettes indirectes, 1986-2025, sans PIB).
  Partage importation/intérieur : fait le 24 octobre 2026 (`#fig-tva-regimes-recettes`, relevé `tva/recettes-tva-par-regime.csv`, prévisions du tableau A des lois de finances 2001-2026 ; 2001-2010 et 2021-2022 lues à l'image, 2023-2026 sur l'édition arabe, 2020 et 2022 imprimées un rang au-dessus de leur libellé) ; réalisations par régime non identifiées. Restent : la taxe rapportée à la consommation privée (série à verser), la décomposition des dépenses fiscales de TVA par forme (plan, § 6.3 et 6.4) ;
- **domicile unique des références étendu à tout le chapitre — sur `master`** (branche
  `chantier/citations-domicile-unique` fusionnée) : `.domicile-unique` sur le titre du chapitre ;
  176 appels juridiques retirés du fil, remplacés par 164 liens `#r-tva-…` vers les lignes de
  registre (142 ancres) ; un registre nouveau pour les clauses de date d'application
  (`tbl-tva-dates-textes`) et la liste des six grilles devenue tableau (`tbl-tva-taux-textes`).
  Restent à juger à la revue :
  ancres des trajectoires posées dans la cellule de date ; `tbl-tva-reformes` sans liens ;
  attributs `titre` et libellés des liens à traduire en arabe ;
- **relecture du propriétaire (7 octobre 2026) — portée sur `master`** : « En bref » devient « Vue d'ensemble » ;
  le mot « cœur » ne paraît plus au chapitre (« règles de base », ou l'élément nommé) ; les renvois
  « traité ailleurs » sont en tête de section ; chaque section de dispositif s'ouvre sur une
  définition de son objet, avant sa place dans la chronologie ;
- **texte principal autosuffisant (7 octobre 2026) — porté sur `master`** : notations T et D définies dans
  chaque section qui les emploie ; règles du fait générateur, de l'option, du pourcentage de
  déduction et de la régularisation dites en clair hors des blocs repliés ; sigles développés et
  notions du glossaire ancrées dans chaque section de niveau 2 ; plus de tournure de lecture
  linéaire. Reste : « DGCPR », cité tel que la source l'écrit, sans développement établi
  (toujours le cas au 25 octobre 2026, section du rapport du FMI de 2013) ;
- **version arabe** : `precis/ar/fiscalite/_tva.qmd` est l'ancienne structure (aucun bloc
  `.chronologie-repliable`, arabe du 4 octobre 2026) ; retraduction complète à la réouverture du
  budget de traduction (décision du 6 octobre 2026, voir « Ce qui traverse les livres »), avec
  les attributs `titre` des seize blocs repliés.

## Vue d'ensemble

| Livre | État du texte | Première lecture faisable |
|---|---|---|
| Fiscalité | Douze chapitres au 23 octobre 2026 : IRPP (section « épargne et capital » du 20 octobre), IS, impôt sur la fortune, contributions conjoncturelles et taxes des fonds spéciaux (23 octobre), patrimoine immobilier, timbre et enregistrement (23 octobre, tableaux faits main), TVA, droits de consommation, droits de douane (23 octobre), régimes d'incitation et dépenses fiscales (format « ruptures au premier plan » depuis le 11 octobre) ; TVA : réformes de 1988 à 2026 rédigées, chapitre au format « ruptures au premier plan » sur `master` depuis le 12 octobre 2026 (restes ci-dessus) ; déduction, crédit et restitution, régime suspensif, déclaration et retenue à la source rédigés le 6 octobre 2026 (`@sec-tva-deduction`), séries budgétaires bornées à 2010-2014 | Boissons alcoolisées rédigées le 23 octobre 2026 (décrets n° 93-2090, 97-1368, 2002-627, 2007-1977, 2013-929, 2015-1768, 2022-545 et lois de finances 2016, 2018, 2021) ; lacunes ci-dessous |
| Retraites | Deux chapitres développés ; coefficients des 31 barèmes relevés | Départs avant l'âge légal (1987, 2009, 2017, 2022-2028) et limite d'âge des magistrats exposés ; lacunes restantes : voir la section Retraites de ce fichier |
| Prestations sociales | Dispositifs décrits ; Amen social à jour au 9 octobre 2026 (280 D, allocation des 6 à 18 ans — pilote sur don depuis 2022, décret de 2025 —, arrêté du 5 août 2026) ; PNAFN historique sans texte pour ses onze dates et montants (fiche `r-pnafn-montants-historiques`, passes du 24 octobre 2026 : trois études rangées dans tunisia-data confirment 7,7 D en 1987, 36,3 en 2000, 56,7 en 2010, 100 D en 2012, 150 D en 2014 ou 2015, 180 D en février 2018 ; la circulaire conjointe du 27 mai 2011 est identifiée, non lue ; aucune source ne date les neuf autres débuts de palier) ; figure `fig-pnafn-allocation` portant le 24 octobre 2026 tous les montants connus, en famille par document, avec la série `pnafn-montants-etudes` et sa fiche `docs/notes/provenance-pnafn-montants-etudes.md` ; figure `fig-nc-beneficiaires` portant toutes les valeurs du tableau des allocataires, série `amen-social-allocataires-tableau` contrôlée par `scripts/verifier_effectifs_tableau.py` ; libellés arabes des deux figures à verser ; volume entier au format « ruptures au premier plan » le 10 octobre 2026 (cinq chapitres ; la matrice des régimes porte aussi l'assistance) ; lectures du 10 octobre 2026 portées (dates d'effet, loi n° 96-101 dans sa rédaction du 7 mars 2002, frontière entre régimes et assistance, aides aux familles d'accueil) | Relecture à l'image des autres textes repris de la couche texte (liste dans la section « Prestations sociales ») ; budgets économiques 2012-2018 et circulaires de montant pour les paliers du PNAFN (non trouvés en ligne ; Wayback hors service le 24 octobre 2026, à rejouer) ; circulaire conjointe n° 12 (Intérieur) et n° 3 (Affaires sociales) du 27 mai 2011 à obtenir ; rédaction en vigueur de l'article 34 de la loi n° 60-30 (champ des salariés non agricoles), lu seulement dans sa rédaction de 1960 |
| Rémunérations publiques | Régime indiciaire développé, trois autres chapitres brefs ; régime de rémunération des dirigeants d'entreprises publiques fusionné le 23 octobre 2026 (#499) | Décret n° 78-885 et circulaire n° 78-45 (scans de 1978-1979 à océriser autrement) |
| Cotisations sociales | Régimes et branches décrits ; échelles AT/MP de 1995 et 1999 engendrées ; plusieurs assiettes et ventilations encore à établir | Article 4 du décret n° 2007-1406 dans le JORT n° 49 de 2007, texte local extractible |
| Caisses de sécurité sociale | Livre créé le 4 octobre 2026 : présentation, histoire (rédigée le 4 octobre), statut-cadre, comptes par régime, état des caisses, comptes de la longue période, chronologie ; rétrospective CNSS 1990-2004 tracée ; statuts annexés du personnel et couverture des déficits agricoles à obtenir hors JORT | Loi n° 98-91 (JORT n° 89 de 1998), fascicule local lisible, pour les modificatifs du statut-cadre |
| Finances locales | Neuf chapitres rédigés ; cinq convertis au format « ruptures au premier plan » le 9 octobre 2026 (budgets, immeubles, activité, taxes, transferts), le chapitre de la longue période fondu dans les autres ; notions resserrées le même jour (cinq blocs repliés) ; histoire et compétences converties le 10 octobre 2026 : les neuf chapitres sont au nouveau format ; présentation mise en accord le même jour | Dispositions finales du code des collectivités locales (loi organique n° 2018-29), édition arabe du JORT n° 39 de 2018, texte local extractible |
| Marché du travail | Volume VIII : institutions, notions, salaire minimum, conventions collectives, négociations, durée du travail et congés (22 octobre 2026), rupture du contrat (20 octobre 2026, tableaux engendrés le 23), politiques de l'emploi, annexe des conventions branche par branche (8-9 octobre 2026 ; grilles tracées depuis le modèle, 193 cases illisibles sur les fascicules) | Décrets n° 81-437 et n° 82-501 (indemnité complémentaire provisoire), fascicules au corpus ; grilles du textile 1983-1993 et du bâtiment 1991-1992 : scans français au corpus, OCR à lancer |
| Compensation | Volume IX, huit chapitres réécrits le 6 octobre 2026 (institution, réformes, dépense, carburants, électricité et gaz, transport, rapports extérieurs, incidence) ; montant versé de la dotation de la Caisse inconnu pour dix années, dont cinq (2003, 2006, 2008, 2009, 2011) ont une ligne budgétaire d'ordre de grandeur (subvention prévue 1987-1994 et ligne 2003-2011 versées le 24 octobre 2026) ; tarifs MT/HT et gaz 1994-2003 versés le 24 octobre 2026, grille d'octobre 1993 non publiée | Lois de règlement 1988 et 1989 (scans à lire à l'image), budget économique, lois de finances complémentaires et tableaux des fonds spéciaux 1995-2010 (dotation) ; décrets de suspension du prélèvement à l'importation (n° 97-2509 à 2007-1199) ; produit annuel des prélèvements ; décret n° 93-1187 et modifications de 2002, 2009 et 2015 du décret n° 91-1391 lus le 24 octobre 2026 |
| Entreprises publiques | **Brouillon** du 11 octobre 2026 : un volume d'un seul chapitre, avec une section « effectifs et masse salariale », français seul ; inscrit à l'accueil le 20 octobre 2026 (partie V) ; séries budgétaires 2016-2024 et 1987-2009 ; quatre flux de clôture du budget pour 2010-2016 (24 octobre 2026) ; ni transferts par entreprise avant 2016, ni encours de la dette garantie, ni série avant 1987 ; forme (volume ou chapitre) à trancher par la revue (note dans la section du volume) | Lois de finances de 2016 à 2024 (articles sur la garantie) ; transferts par entreprise 2010-2015 ; totaux des budgets de 1959-60 à 1985 (voir la section du volume) |
| Santé | Volume X, première rédaction le 12 octobre 2026, français seul : histoire, couverture, hôpital, médecine de ville ; tarifs des malades payants et tarifs réduits de 1998 (23 octobre) ; numérotation des sections corrigée (#511) ; dépenses du département 2018-2023 et comptes de la CNAM 2016-2021 intégrés, comptes 2011-2015 lus à l'image le 15 octobre ; les prestations en espèces restent dans « Prestations sociales » | Statistiques de prestations de la CNAM, lisibles en couche texte dans le corpus ; ventilation de la dépense par prestation à obtenir hors JORT |
| Éducation et formation | Volume XII, première rédaction le 17 octobre 2026, français seul : histoire, scolaire, formation professionnelle, supérieur, aides aux élèves et aux étudiants, dépense (dépense des communes ajoutée le 23 octobre, séries 2022-2023) ; lectures des 18 et 19 octobre fusionnées ; lignes de tableau sans contenu établi retirées et listées en TODO | Arrêtés de montants de bourses 1958-1978, décret n° 80-1001 : lus le 29 octobre 2026 ; arrêté du 20 août 1982 non retrouvé en français (édition arabe à lire) ; § 9 du plan, points 2 et 3, à lire à l'image ; supérieur réordonné par parcours de l'étudiant le 30 octobre 2026 (lois, accès et orientation, établissements, diplômes, formation pratique, textes), contribution des étudiants passée au chapitre des aides (même identifiant) ; TODO sur la langue d'enseignement ajouté |

Les `TODO` des `.qmd` détaillent chaque lacune, y compris celles que ce tableau ne peut pas
résumer. Ici, **lisible** veut dire que le fascicule est présent avec une couche texte
extractible sur les premières pages contrôlées ; vérifier à la page de l'article que les
tableaux ou annexes ne sont pas des images. **OCR** veut dire que le fascicule est présent,
mais que la couche texte testée est vide. Un texte absent du JORT en français peut avoir une
édition arabe ou un extrait français dans `PDFs/Lois_de_Finances/` : les distinguer.

## Fiscalité — cinq impôts ouverts, des lectures et des mécanismes à compléter

- **Droit de timbre et droits d'enregistrement hors mutations : chapitre rédigé le 23 octobre 2026** (`_timbre_enregistrement.qmd`, `#sec-te`, après `_patrimoine_immobilier.qmd` dans le `_quarto.yml` français). Sources : `docs/notes/fiscalite-timbre-enregistrement-documentation.md` (note N), ses deux CSV, `docs/notes/fiscalite-timbre-enregistrement-plan-architecte.md` (plan), `docs/notes/eco-timbre-enregistrement.md` (fiche économiste). Fait : vue d'ensemble à cinq dates ; mise en place (décrets n° 65-222, 68-3, 68-104, LF 1969, loi n° 87-73, LF 1990, code de 1993) ; réformes de 1997 (taxe unique sur les assurances), 2006 (téléphone), 2022 (tickets), 2026 (affectation aux caisses) ; état du droit au 1^er^ janvier 2026 ; dix dispositifs avec registres repliés (`r-te-…`) ; figure `fig-te-rendement` (prévisions du tableau A 2001-2026, réalisations de la Cour des comptes 2018-2023, dinars courants et de 2025), lue dans le relevé tenu à la main `precis/fr/fiscalite/timbre/rendement-timbre-enregistrement.csv` par `figures/timbre_enregistrement.py` ; « Ce qu'en dit l'économie » ; fiche de recherche `r-timbre-decret-1912`. Corrigé dans `_patrimoine_immobilier.qmd` : fonds de commerce en 1987 (18,80 % au tarif de 1969, non 14,60 %), minimum de perception 15 → 20 D en 2012, renvoi `@sec-te-droit-fixe`, décret n° 68-104 cité. Restent ouverts :
  - **lu le 24 octobre 2026** (section « 1977 à 1989 : le droit fixe harmonisé et le timbre relevé par les lois de finances », `#sec-te-1977-1989`, registre `#r-te-ant-1974` à `-1989`, relevé `fiscalite-timbre-enregistrement-textes-lus.csv`) : LF 1974 (art. 26-28), 1975 (art. 32), 1977 (art. 46-47) et loi n° 77-60, LF 1978 (art. 12), 1982 (art. 19, 22-23, 26) et LFC 1982, LF 1983 (art. 43-51), 1985 (art. 36-42), 1986 (art. 29), 1987 (art. 22-23), 1989 (art. 46, 66) ; restes : LF 1980 (art. 37 seul lu), LF 1983 art. 44 et 49 à recouper avec le tarif de 1912, loi n° 83-81 (LFC 1983, art. 14, marchés), taux des fonds de commerce de 1969 à 1987, suppression du droit d'apport proportionnel (loi n° 62-81, art. 8), timbre des effets de 1986 imprimé « 9 % » (lu ‰), clause générale d'effet de chaque loi de finances ; la **taxe unique sur les assurances** existe avant 1997 (LF 1974, art. 29, qui modifie le tarif fixé par le décret n° 69-114 du 29 mars 1969) : corriger l'ordre des réformes du chapitre (« la taxe unique sur les assurances en 1997 ») après lecture du décret n° 69-114 ; **lisible dans le corpus local** : clause générale d'effet de la LF 1990 ; prorogations du 5 % de 1989 à 1992 pour les fonds de commerce ; LF 2001, art. 64 (titre de crédit) ; LF 2005, art. 59 (souscription unifiée), art. 37-40, et LF 2007, art. 17-18 (fusions) ; LF 2011, art. 22-23 (sociétés par actions, date d'effet) ; LF 2018, art. 33 (marchés) ; LF 2022, art. 37, 40, 42 ; LF 2013, art. 49 (carte de séjour, renouvellement de la carte d'identité, visite technique) ; intermédiaires de 1994 à 2012 du timbre des actes (2 → 3 D), des effets et de la carte d'identité ; **écrits le 24 octobre 2026** : LF 1996 art. 48 et LF 1998 art. 84-85 (registre des documents administratifs), paiement du timbre (LF 1998 art. 86-87, LF 2002 art. 76-77, LF 2004 art. 93-97, LF 2020 art. 23, LF 2022 art. 44 ; registre `r-te-mp-`), taxe unique sur les assurances (LF 2001 art. 45, LF 2020 art. 15-16) ; seconde passe : LF 2008 art. 27 (écrit, p. 4360 : le fascicule français a bien une couche texte), LF 1994 art. 57 (déjà au chapitre) et art. 64 (formules de la Marine marchande, écrit), arrêtés du 4 juin 2003, du 2 août 2013, du 4 juillet 2017, du 23 mai 2022, du 16 janvier 2023 et du 6 janvier 2026 (écrits au registre du paiement) ; restent les arrêtés d'application des art. 128 *bis* et 128 *quinquies* (fiche `r-te-arretes-machines-a-timbrer`) et la date de dépôt du JORT n° 55 de 2017 ; tableau A des LF 1970-2000 et totaux de 2002-2007 ; rapports sur les projets de budget 2008, 2013, 2014, 2015 et diaporama LF 2016 (`tunisia-data`) pour le contexte et les sauts de prévision de 2008 et 2015 ;
  - **lecture au fascicule (scan)** : jour de publication des décrets n° 65-222, 68-3 et 68-104 (dates d'effet au mois près) ; réalisations de 2017 (`loireg2018.pdf`, sans couche texte exploitable) ; aucun OCR indispensable ;
  - **à obtenir** : décrets organiques des 19 et 20 avril 1912 et modificatifs de 1957 (Gallica, ancienne série absente du corpus) ; date de dépôt au gouvernorat de Tunis du JORT n° 39/2012 (le chapitre retient le 25 mai 2012, date de la note commune n° 14/2012) ; JORT n° 68/2014 : déposé le 22 août 2014 (mention de dernière page, relevée le 24 octobre 2026), donc 27 août 2014, établi ; édition arabe du tableau A 2021-2022 (permutation probable 18-03 / 18-04) ; décret n° 93-1148 (timbre d'avocat) ; débats du 11 mai 1993 ; régime fiscal des assurances du décret du 27 mars 1947 ;
  - **contexte des réformes** : 1993, 1997, 2006, 2026 (`TODO (documentaliste)` dans le chapitre) ; population couverte de l'état du droit (actes par nature, contrats d'assurance, factures, recharges) ; ligne 13-02 du tableau A (« mutations des biens mobiliers ») à rattacher à un article et à relever 2020-2026 ; sous-total des seuls impôts du tableau A ;
  - **tableaux à engendrer** : tous les tableaux du chapitre sont faits main (`TODO (rédacteur)`) ; droit fixe, minimum de perception, timbre des factures, timbre téléphonique, passeport et taxe unique à verser en amont (voir `docs/notes/backlog-modele.md`), puis figure en escalier du droit fixe et du minimum ;
  - **économiste** : écart entre *Doing Business 2020* (0,400 TND en 2018) et le timbre de 0,600 D au 1^er^ janvier 2018 ;
  - **figures** : frise de tête `fig-te-frise` ; libellés arabes de `figures/timbre_enregistrement.py` à relire (relecteur-ar) ;
  - **livre des caisses — fait le 25 octobre 2026** : phrase et lien dans `../caisses/_etat_caisses.qmd#sec-caisses-financeur` vers `#sec-te-2026` sur l'affectation par la LF 2026, art. 20, § 7, d'une part du timbre (tickets, cahiers des charges, nouveaux tarifs des factures des grandes surfaces et des recharges) au compte « حساب تنويع مصادر الضمان الاجتماعي » ;
  - **arabe** : à la livraison de la traduction, ajouter `_timbre_enregistrement.qmd` au `_quarto.yml` arabe et copier le relevé `timbre/rendement-timbre-enregistrement.csv` (et son manifeste) sous `precis/ar/fiscalite/timbre/` ; clé arabe de l'entrée de glossaire `minimum-perception-enregistrement` à vérifier ; traduction des rubriques arabes citées (LF 2023, LF 2026) dans les `TODO` et les registres ; l'attribut `titre` des blocs repliés à traduire ;
  - **taille** : le fichier compte 16 900 mots (wc, 23/10/2026), sous le seuil d'environ 25 000.

- **Timbre et enregistrement : figures du 24 octobre 2026.** `#fig-te-rendement` a quatre vues : dinars courants ; part des dépenses de l'État (série `denominateurs-depenses-etat-pib`, dépenses hors service de la dette, réalisations du ministère des Finances, 1986-2025, une seule série ; numérateur voté ou réalisé, dénominateur réalisé) ; part du PIB, une courbe par base (1983, 1997, 2015, série `pib-courant-par-base`, sans raccord, valeurs « non rattachées » 2002-2004 et 2025 dans l'onglet Données seulement) ; dinars de 2025 (IPC de l'INS base 1970, seul raccord 2024-2025 par l'indice base 2015 de la BCT). Huit figures en escalier (`figures/timbre_montants.py`, série `timbre-montants-dates`, 78 lignes, 14 grandeurs, courant et dinars de 2025) : droit fixe par page (5 dates), minimum de perception des actes (8) et des jugements par juridiction (6), timbre des factures (6), des effets domiciliés (7) et des autres effets (4), du titre de crédit (4), d'une carte (4) et d'une recharge (5) de téléphone de 5 D, passeport (7) et passeport des étudiants (6), renouvellement de la carte pour perte (4). **Écartés, à trois dates ou moins** : timbre des actes par feuille (3 : 1993, 2013, 2018), timbre de dimension (3 : 1969, 1981-1982, 1986 ; 1965 et 1968 sans jour établi), carte d'identité (3), carte de séjour (3), droit fixe des marchés (3 et fin en 2013), actes de sociétés (2), visite technique (2 datés), débits de boissons (3), services rendus par l'État sans redevance (3 dont une date non établie), renouvellement du passeport pour perte (3). Les montants par dinar ou en pour cent (téléphone depuis 2012, taxe unique, droits proportionnels) sont des taux : seul l'équivalent pour 5 D du téléphone est tracé, calculé. Pages corrigées le 24 octobre 2026 sur fascicule : la page d'un article est le numéro imprimé sur la page du fichier qui porte son texte, non le dernier numéro rencontré dans l'extraction du texte (écart d'un rang constaté pour la loi de finances pour 1997, la loi de finances complémentaire pour 2014, les lois de finances pour 2017 et 2018, et vérifié pour les références ajoutées ce jour) ; corrections de fond : marchés des n° 13 à 15 de l'art. 23 au droit fixe de 10 D dès 1993, tribunal administratif au minimum des jugements (20 D en 1993, 75 D en 2012), marchés à 20 D du 25 mai au 31 décembre 2012.
- **Fiscalité de l'épargne et du capital : rédigée le 20 octobre 2026, section `#sec-irpp-epargne` du chapitre de l'IRPP** (`_impot_revenu.qmd`, décision du propriétaire du 20 octobre 2026 : ni chapitre neuf ni scission). Sources : `docs/notes/fiscalite-epargne-capital.md` (note, § 14 réponses), `docs/notes/fiscalite-epargne-capital-plan-architecte.md` (plan), `docs/notes/eco-epargne-capital.md` (fiche économiste). Vue d'ensemble des taux 1990-2026, mise en place, cinq réformes (1992, 1999, 2004, 2014, 2020-2022), trois registres (intérêts, revenus distribués, plus-values), état du droit au 1^er^ janvier 2026, sept dispositifs (comptes spéciaux, épargne exonérée, assurance-vie, CEA, CEI, fonds, non-résidents), coût des déductions 2017-2023 (`#fig-irpp-epargne-depenses-fiscales`, module `figures/epargne_capital.py`), « Ce qu'en dit l'économie ». `#tbl-epargne` et le plafond de l'assurance-vie ont quitté `#sec-irpp-deductions` pour la section. **Taille : le fichier compte 38 096 mots (wc, 20/10/2026), contre 26 285 avant, au-delà du seuil d'environ 25 000** ; options de scission au § 9 du plan de l'architecte, non appliquées. Restent ouverts :
  - **bibliographe** : pages des art. 30-31 de la LF 2002 (CEA, p. 4253-4254 du JORT n° 104 de 2001) à confirmer à l'image, puis à citer par `lf-2002` ;
  - **à lire au fascicule** (corpus local) : LF 2002, art. 21-28 (OPCVM), connus par la NC 45/2002 ; LF 2003, art. 23 (CEI ; art. 21, 22 et 87 lus), arrêté du 24 avril 2003 ; décret-loi n° 2011-100 ; loi n° 2005-59 (art. 39 *ter*) ; LF 2019, art. 35-4 (lu en arabe, à porter au registre des non-résidents) ; LF 2000, art. 57, et décret n° 2007-1870 ; décrets n° 99-2773 (CEA) et 99-1923 (comptes d'études) ; LF 2007, art. 32 (page 4387 à confirmer à l'image) ;
  - **dates à établir** : année de revenus du plafond de 1 500 D (LF 1992, art. 30), du CEA à 50 000 D (décret-loi n° 2011-28, exécutoire le 25 avril 2011 ; aucune note commune) et de la première déduction CEA (1999) ; règle de date des lois sans clause d'effet (dépôt + 5 ou + 6 jours : `docs/notes/backlog-modele.md`) ; sort des intérêts courus avant le 10 juin 2020 ; modalités de la restitution sous 10 000 D (NC 3/2015 muette) ;
  - **sources** : pages imprimées des rapports annuels de la BCT 1992, 1996, 2000 et 2003 citées pour le contexte (fichiers lus) ; contexte de 2004, 2020 et 2021 ; régime des SICAV ; antécédent 1969-1987 (LF 1983, art. 24 ; LF 1984, art. 24 ; loi n° 87-48) ;
  - **séries** : recettes des retenues non ventilées dans les sources trouvées ; population couverte de l'état du droit (titulaires de CEA, CEI, contrats d'assurance-vie, foyers déclarant des revenus de capitaux) ; encours BCT 2003-2024 à cataloguer dans `tunisia-data` ; figure des plafonds en dinars courants et constants (`scripts/generate_epargne_capital_series.py`, à écrire ; les tableaux de plafonds sont engendrés depuis `scripts/generate_bareme_tables.py`) ; rapports des dépenses fiscales pour 2022 et 2023 ;
  - **régime boursier de la loi n° 99-92 (art. 1-3, IS à 20 % pendant cinq ans)** absent du chapitre de l'IS, qui ne commence qu'en 2010 ;
  - **glossaire** : les onze entrées de la passe 1 (retenue libératoire, retenue définitive, revenus de capitaux mobiliers…) ont une définition vide (passe 2 du terminologue) ; la définition de `retenue-a-la-source` est inexacte pour les retenues libératoires.

- **Figure du taux d'imposition des BIC selon le régime : faite (19 octobre 2026), `#sec-irpp-forfait-taux`.** Dix panneaux (1990 à 2026), chiffres d'affaires en dinars de 2025, forfait, impôt forfaitaire optionnel (1999-2010, 2026) et régime réel à τ = 25 % et 10 %. Séries écrites par `scripts/generate_forfait_bic_series.py` dans `precis/_seriescache/` (`bic-forfait-tarifs`, `bic-minimum-impot`, `bic-hypotheses-benefice`), figure `precis/fr/fiscalite/figures/bic_regimes.py`, calcul testé `tests/test_bic_regimes.py`. Reste :
  - **paramètres du forfait en amont** (openfisca-tunisia#476) : remplacer le générateur par une lecture de l'arbre (TODO modéliste dans la section) ;
  - **3 % de l'art. 44 *ter* (LF 2016, art. 17) : corrigé le 24 octobre 2026.** La note commune n° 27/2016 est au corpus local (`dgi-nc-27-2016`, URL jibaya.tn vérifiée, SHA-256 identique) : le 3 % s'applique à la seule fraction du chiffre d'affaires au-dessus de 10 000 D, en plus du montant fixe (exemples p. 11-12 : 150 + 3 % × 75 500 = 2 415 D ; 75 + 3 % × 60 000 = 1 875 D). Le calcul de la figure comptait 3 % du chiffre entier : il est corrigé (`scripts/bic_regimes.py`, `generate_forfait_bic_series.py`, `tests/test_bic_regimes.py`), la série `bic-forfait-tarifs` régénérée (huit lignes), les deux paragraphes et le tableau des états du droit repris (2026 : option comparée au forfait à 50 000 et 100 000 D, croisements à 80 000 et 86 667 D) ;
  - **plafond d'accès de l'option de 1 500 D (LF 1999, art. 61)** : le texte donne 100 000 D comme seuil de relèvement ; tracé jusqu'à 100 000 D, usage de l'administration à vérifier ;
  - **indice des prix de 2026 non publié** : panneau 2026 au niveau de 2025 ; à reprendre à la publication de l'indice ;
  - **activités et zones** : une courbe par activité en 1990 et 2011-2015, tireté pour les zones communales ; le plafond des services (12 000 D en 1993, 50 000 D en 2011-2015) est un point ; les annexes III (forfait simplifié 1992-1998), assises sur des indices d'emplois et de zones, ne sont pas tracées ;
  - **libellés arabes de la figure** (`bic_regimes.py`, `_L`) à faire relire par le relecteur-ar.

- **Fiscalité locale : aucune entrée à ce jour (demande de l'humain, 4 octobre 2026). Option B retenue le 4 octobre 2026 : un volume VII « Les finances locales » (fiscalité locale, transferts, budgets) ; plan : `docs/notes/fiscalite-locale-plan.md`. TIB, TNB, TCL et taxes du code rédigées dans ce volume le 4 octobre 2026 (voir « Les finances locales » ci-dessous).** Le volume ne traite que des impôts d'État. Il manque un chapitre — ou un volume — sur la fiscalité locale : taxe sur les immeubles bâtis (TIB), taxe sur les terrains non bâtis (TNB), taxe sur les établissements à caractère industriel, commercial ou professionnel (TCL), et leurs textes (code de la fiscalité locale et ses modifications, à relever au JORT). Matière déjà collectée : documents de la réforme fiscale 2013-2014 (`tunisia-data/data/raw/minfinances/reforme_fiscale_2013_2014/`, fiche `sources/minfinances-reforme-fiscale-2013-2014.md`) — synthèse du groupe « fiscalité locale » (CNF août 2013, `2013-08_cnf_rf_5_ar.pdf` : TCL 111 / 93 / 137 MD et TIB 40 / 21 / 30 MD en 2010-2012), présentation de novembre 2013, journée de réflexion d'octobre 2014 sur la décentralisation ; inventaire page par page dans `docs/notes/reforme-fiscale-2013-2014-inventaire.md`. À cadrer : périmètre (impôts des collectivités locales seulement, ou aussi taxes affectées), place dans le précis, lien avec l'impôt foncier de 2014 (chapitre de l'impôt sur la fortune). Doctrine : six textes de B. Dafflon et G. Gilbert (Revue tunisienne de fiscalité, n° 20, 24, 25, 27 ; mélanges *Transparence et droit*, 2021) — deux en accès libre, quatre à obtenir en bibliothèque ou au Centre d'études fiscales de Sfax ; synthèse de référence : Dafflon et Gilbert, *L'économie politique et institutionnelle de la décentralisation en Tunisie*, AFD, 2018 (HAL, CC BY-NC-ND) ; rapports PARD 2021-2022. Inventaire, statut d'accès et ébauches CSL : `docs/notes/biblio-fiscalite-locale.md` ; copies locales hors dépôt : `~/Documents/biblio-precis/fiscalite-locale/`.

- **Présentation (`index.qmd`) : impôts directs et indirects définis et sourcés** (LOB 1967, 1996, 2019 ; tableaux A des LF 2014 et 2021 ; support ENA de S. Zakraoui), textes lus dans le corpus. Reste : relever la page de fin des trois LOB dans l'édition arabe ; dater le support ENA ou lui substituer la doctrine imprimée (`baccouche2008`, `ayadi1996`, à obtenir) ; l'arrêté de nomenclature des recettes (LOB 2019, art. 16) n'est pas identifié.

**Immédiat, avec les sources déjà présentes.** Les décrets n° 97-1368 et 2015-1768 sont
lus et rédigés (23 octobre 2026, section « Les boissons alcoolisées » du chapitre des droits
de consommation) ; lacunes ouvertes : voir « Droits de consommation, boissons : lacunes ».
L'extrait français `PDFs/Lois_de_Finances/Loi_de_Finances_2016.pdf` porte les articles
utilisés de la LF 2016 ; le JORT français n° 128 de 2020 (LF 2021) est aussi au corpus
et a été lu pour l'IRPP. **Ces deux lois ne sont donc plus des textes « absents »** ; ne
pas confondre l'absence en ligne du fascicule français de 2015 avec celle de son extrait
français conservé localement.

**OCR ciblé.** Le texte initial de la TVA au JORT n° 39 de 1988 (`Jo03988.pdf`, p. 827-846)
a été océrisé le 23 octobre 2026 (`docs/notes/ocr-cibles-2026-10-23.md`) ; les tableaux et
chiffres se relèvent encore à l'image avant citation. Le code fiscal du JORT n° 1 de
1990 a été océrisé le 4 octobre 2026 ; ses annexes II et III (forfait) sont relues à l'image
(`docs/notes/fiscalite-regime-forfaitaire.md`).

**TVA — déduction, crédit et suspension (`_tva.qmd`, `@sec-tva-deduction`, rédigé le
6 octobre 2026)** d'après `docs/notes/fiscalite-tva-deductions-documentation.md`. Restent
ouverts, avec l'état des sources :

- **séries budgétaires après 2014 et avant 2010** (24 octobre 2026 : lois de règlement 2018-2022 et rapports de la Cour des comptes locaux sans série de restitutions ; rapports annuels de la DGI 2013-2014 en police non Unicode, à lire à l'image ; recherche web : déclarations ponctuelles seulement ; fiche `r-tva-credit-series-apres-2014`) (stock de crédit, restitutions, retenue à
  la source) : les rapports annuels de la DGI de 2013 et 2014 sont dans `tunisia-data` mais
  leur texte arabe n'est pas exploitable par recherche — **à lire à l'image**, puis chercher
  les millésimes suivants ; lois de règlement, rapports de la Cour des comptes et rapports
  annuels de performance de la mission Finances **non examinés**. Les séries connues
  (2009-2014) sont versées dans `tunisia-data` (`tva-credit-restitutions-sources`) et tracées
  par `@fig-tva-credit-restitutions`, toutes sources côte à côte ; quand la série sera prolongée, élargir les
  axes des vues (bornes fixées dans `figures/tva.py`) et la légende « 2009-2014 » ;
- **dates d'effet** : lois de finances pour 1989 à 1993 : aucune clause spéciale d'application ; dates calculées le 24 octobre 2026 selon la règle d'avant 1993 (un jour franc après la publication du 31 décembre), soit le 2 janvier, comme aux chapitres du timbre et des droits de douane (rubriques de taux, d'exonérations et de catégories ; forfaits de 1990 et de 1993 laissés non établis, leur application dépendant d'un texte d'application ou de l'année de revenus) ; art. 31 et 32 de la loi de finances pour 1994 : lus à l'image le 24 octobre 2026 (JORT n° 100 du 31 décembre 1993, p. 2197), aucune clause propre, application au 1^er^ janvier 1994 par l'art. 77 (« les dispositions de la présente loi sont applicables à compter du 1^er^ janvier 1994 »), écrite au chapitre (`r-tva-declaration-1994`) ; art. 50 (LF 1991), 66 et 68 (LF 1992) et 114 (LF 1993), non repris au chapitre ; loi n° 2007-69 (art. 10 et 11 : lue le 24 octobre 2026 à l'image et par OCR, JORT n° 104 de 2007, p. 4337-4356 — aucune clause d'application pour ces articles, l'art. 31 ne datant que les art. 27 à 29 et l'art. 49 portant la seule formule d'exécution ; fascicule déposé le 31 décembre 2007 (dernière page), exécutoire le 5 janvier 2008, écrit au registre) ; loi de finances complémentaire pour 2014, art. 27 (article 13 *bis* du code) : lu le 24 octobre 2026 (JORT n° 68 du 22 août 2014, p. 2103), aucune clause d'application propre ; fascicule déposé le 22 août 2014 (mention de dernière page), exécutoire le 27 août 2014, écrit au registre ;
- **délai de visa de la restitution entre 1998 et 2001** (relu le 24 octobre 2026 : l'art. 41 de la LF 1998, lu à la lettre, ne porte aucun délai, et la LF 1999 n'en fixe pas non plus (elle relève le taux de restitution à 50 %) ; note commune n° 11/1999 absente du corpus) : l'art. 41 de la LF 1998 récrit
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
l'image), et les
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
aux dates repères est engendré (`tva_taux_dates_reperes.md`) et inséré dans `_tva.qmd`
(`@tbl-tva-taux-reperes`) ; les déductions pour charges de famille de
l'impôt sur le revenu ont les deux (`@tbl-charges-famille-reperes`,
`@fig-irpp-deductions-famille`). Restent :

- *(fait : `tva_taux_dates_reperes.md` est inséré dans `_tva.qmd`, `@tbl-tva-taux-reperes` ; vérifié le 24 octobre 2026)* ;
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
  - **AR** : déclarer `_regimes_incitation.qmd` PUIS `_depenses_fiscales.qmd` dans
    `precis/ar/fiscalite/_quarto.yml` (ligne commentée en place, après
    `_droits_consommation.qmd`), les deux ensemble et seulement quand les deux traductions
    sont livrées : `_depenses_fiscales.qmd` renvoie à des ancres parties dans
    `_regimes_incitation.qmd` (`sec-df-sommes-versees`, `sec-df-etudes`, `tbl-df-bm-cout`,
    `tbl-df-reports`…), qui ne se résolvent pas sans lui ;
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
  - **crédits budgétaires** : crédits de programmes du FOPRODI (1999-2019) et de la prise en
    charge de la contribution patronale (1995-2019), de l'aide aux promoteurs touristiques (2010-2019) et du FONAPRA (2012-2019) relevés le 13 octobre 2026 aux
    tableaux des crédits de programmes des lois de finances initiales, lus à l'image
    (`#sec-df-foprodi` et `#sec-ri-credits-programmes` : deux figures à trois vues depuis le 13 octobre 2026 — millions de dinars, part des dépenses de l'État, part du PIB —, séries `jort-lf-credits-programmes-incitations` et `bct-foprodi-fonapra` de tunisia-data ; `docs/notes/fiscalite-incitations-second-passage-2026-10-13.md`) —
    le tableau « ب » des fonds spéciaux n'était pas le bon. **Restent** : FOPRODI de 1995 à 1998 (pas de ligne au chapitre de
    l'industrie ; autres chapitres non lus) ; loi de finances pour 1994 ; encouragements
    à l'agriculture aux mêmes tableaux (trois séries qui ne s'enchaînent pas) ; FONAPRA 2010-2011 ;
    exécution : les lois de règlement ne nomment aucune de ces lignes (lues le 13 octobre 2026) ;
    à partir de 2020, le tableau n'existe plus (missions et programmes) ; budgets par ministère depuis 2013,
    comptes du Fonds tunisien de l'investissement — **à obtenir** ou à transcrire ;
  - **restes du 13 octobre 2026** : entrée de glossaire « crédits de programmes » — aucune
    définition sourcée (la loi organique du budget n° 2004-42, lue par océrisation, ne la donne
    pas ; loi n° 67-53 à lire à l'image) ; numéros et dates des lois de finances pour 2018, 2019
    et 2020 repris de l'index du *Journal officiel*, à relire au fascicule ; libellés arabes des
    figures `fig-ri-foprodi` et `fig-ri-credits-programmes` à verser
    (`precis/fr/fiscalite/figures/credits_incitations.py`) avant la traduction du chapitre ;
    repli du détail de `#sec-ri-2016-2017` et de `#sec-df-sommes-versees` proposé dans une PR
    brouillon à part, à juger ;
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
  - **rapport annexé au PLF 2026 — non trouvé** : absent, le 11 octobre 2026, de la rubrique
    du portail gbo.tn et de la page « loi de finances » de finances.gov.tn (vues par année
    non parcourues) ; à rechercher. Existence d'un rapport pour les PLF 2019 et 2020 : non
    établie. Les rapports 2022 et 2023 sont dans `tunisia-data` depuis le 6 octobre 2026 ;
    leur partie « dépenses fiscales » (périmètre, exercices, méthode) reste à lire ;
  - **série du coût à reconstruire, avec sa rupture de périmètre** : les rapports 2024 et
    2025 excluent les exonérations des médicaments et des engrais, que le rapport 2021
    compte (274,5 et 249,9 MD en 2019). Les deux CSV traités de `tunisia-data` cousent trois
    rapports sur cinq et portent cette rupture à la couture 2019/2020 ; le périmètre des
    rapports 2022 et 2023 reste à lire. `figures/depenses_fiscales.py` (les huit plus gros
    dispositifs) n'est donc pas appelé. Depuis le 11 octobre 2026, `fig-df-total`
    (`figures/depenses_fiscales_total.py`) publie le total par impôt **rapport par rapport,
    sans chaînage**, en MD, en % des recettes fiscales et en % du PIB (INS, base 2015, non
    rétropolé), les rapports 2022 et 2023 n'y figurant que par leur total d'introduction ;
    les parts sont calculées, et ne coïncident pas toujours avec celles qu'impriment les
    rapports (dénominateurs à établir : voir le TODO de `@sec-df-total`).
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
- **Scission en deux chapitres, au format « ruptures au premier plan » (11 octobre 2026)** :
  `_regimes_incitation.qmd` (nouveau : vue d'ensemble, mise en place 1969-1974, grandes
  réformes, état du droit en 2026, sommes versées et FOPRODI, commerce extérieur, études
  extérieures) et `_depenses_fiscales.qmd` (resserré : la mesure du ministère des Finances).
  Toutes les ancres `sec-df-…`, `tbl-df-…` et `fig-df-…` gardent leur nom ; les sections
  sont à domicile unique (registres `r-ri-…` et `r-df-…`). Quatre relevés versionnés dans
  `precis/fr/fiscalite/incitations/` alimentent les figures du texte (`fig-ri-frise`,
  `fig-ri-prime`, `fig-ri-zones`, `fig-ri-ghazouani`). **Replié le 13 octobre 2026**, sans
  texte supprimé, dans `#sec-ri-2016-2017` (précisions de lecture des deux tableaux) et
  `#sec-df-sommes-versees` (« par domaine », limites du relevé ; l'encadré de lecture reste visible) :
  deux blocs repliés nouveaux. Le repli de `#sec-ri-credits-programmes` est sans objet depuis que
  les tableaux des crédits sont des figures (même jour). Restent :
  - **ce que la loi cherche** : rubrique de l'article 37 de la loi de finances pour 2019
    (fin du régime de l'exportation) et des articles 5 et 6 de la loi n° 2006-80, à relever
    au fascicule (JORT lisibles au corpus, non ouverts pour cela) ;
  - **figures écartées** : sommes versées « un point par rapport » (un à trois points par
    périmètre : le tableau une colonne par rapport suffit) ; carte des délégations de 2017
    (demande un fond de carte des délégations) ; budgétaire et études sur un même graphique
    (périmètres à dire sur la figure) ;
  - **dinars constants** : plafonds des primes et sommes versées en dinars courants
    seulement — le chapitre n'a pas d'année de référence (point à trancher) ;
  - **tableaux faits main** des barèmes des primes (`tbl-df-primes-…`) : à engendrer quand
    les paramètres seront datés en amont.
- **Primes, zones, sommes versées, commerce extérieur par régime (`_regimes_incitation.qmd`
  depuis la scission ; écrit dans `_depenses_fiscales.qmd` le 11 octobre 2026)** sur la note `docs/notes/fiscalite-incitations-primes-zones-2026-10-11.md`
  et les séries `gbo-avantages-financiers-par-rapport`, `bct-foprodi-fonapra` et
  `ins-commerce-exterieur-par-regime` de `tunisia-data` (qui font foi quand elles divergent
  de la note). Écrit : `@sec-df-loi-2019-47` (portée fiscale et financière de la loi
  n° 2019-47) ; `@sec-df-primes-zones` (barème de 2011 → 2017, primes de la loi de 2016,
  carte des zones 1994-2024, barèmes successifs, registre des décrets et listes nominatives
  repliés) ; `@sec-df-sommes-versees` (cinq rapports, une colonne par rapport, 2018-2023) ;
  `@sec-df-foprodi` (crédits votés, 1999-2019, et comptes de la BCT, 2016-2025, sur une même figure) ; `@sec-df-commerce-exterieur` (part du
  régime off shore, 1998-2023, figure). Clos : décret gouvernemental n° 2017-389 et loi
  n° 2019-47, lus. Restent :
  - **que l'annexe n° 2 du décret n° 2017-389 vaille pour l'article 63 du code de l'impôt** :
    établi par aucun texte lu (fiche `r-fisc-art63-decret-zones`) ; chercher la note commune
    de la direction générale des impôts sur les articles 63 et 64 — hors corpus, à obtenir ;
  - **dates d'effet de 1994 et de 1999** : mention de dépôt du JORT n° 21 de 1994 à lire sur
    la page (`1994/fr/Jo02194.pdf`, lisible) ; articles 2 et suivants du décret n° 99-486
    (`1999/fr/Jo02099.pdf`, couche texte à police décalée : à lire à l'image) ;
  - **vingt décrets de retouche des zones et des primes (1995-2009)** et décret n° 2011-3197 :
    intitulés seuls ; **rédactions des articles 23, 25 et 25 bis du code de 1993** entre 2005
    et 2016 (durées de déduction et de prise en charge par catégorie de zones) : non lues ;
  - **sommes versées avant 2016** : aucune série (FOPRODI : rien entre 1992 et 2015 ;
    éditions 1977-1986 du rapport de la BCT à lire à l'image ; Cour des comptes, archives du
    web de l'APII et de l'APIA non ouvertes) ; mise à niveau et primes agricoles avant 2018 :
    néant ;
  - **coût côté CNSS des prises en charge de la contribution patronale** : non établi (les
    rapports comptent des sommes versées ou portées en dette de l'État) ; états financiers et
    rapports d'activité de la CNSS, rapports annuels de performance de la mission Affaires
    sociales — à obtenir ; cause de la chute de la ligne 031106 entre 2018 et 2019 non dite ;
  - **nombre et emploi des entreprises totalement exportatrices** : rien dans `tunisia-data`,
    non cherché en ligne (répertoire national des entreprises de l'INS, APII, FIPA, archives
    du web) ;
  - **définition des régimes « général » et « off shore » par l'INS** : non lue ; ventilation
    par groupement sectoriel du tableau 14.2 non transcrite ; cause de la révision 2004-2005
    du régime off shore non dite par l'annuaire ;
  - **tableaux de barème faits main** (quatre) : à engendrer quand le barème sera versé en
    amont (`docs/notes/backlog-modele.md`) ; **dinars constants** : le chapitre n'a pas
    d'année de référence, les montants sont en dinars courants seulement — à trancher ;
  - **glossaire** : entrées candidates non créées, faute d'arbitrage du terminologue —
    prime de développement régional, FOPRODI, Fonds tunisien de l'investissement (termes
    arabes relevés dans la note, § 3) ; la définition de « zones de développement régional »
    n'est pas retouchée (terme arabe des « zones d'encouragement » de 1994-2016 non relevé) ;
  - **AR** : les onze clés nouvelles de `precis/ar/fiscalite/references.json` gardent leur
    intitulé français (l'index ne porte l'intitulé arabe que pour la loi n° 2019-47).
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

- **Taux marginal et taux moyen des barèmes de l'IRPP et de la CPE — fait le 19 octobre 2026**
  (`fig-cpe-taux`, `fig-irpp-taux-bareme`, `#sec-irpp` ; module `figures/baremes_revenu.py`,
  séries `cpe-bareme` et `irpp-bareme`). Taux moyen du barème seul, en dinars courants ; ni
  plafond de cotisation, ni exemptions, ni minimum d'impôt, ni charges de famille. IRPP année
  par année, 1990-2026, en dinars constants (indice commun du précis, base 2025 ; `fig-irpp-annuel`,
  `tbl-irpp-bareme-annuel`) : **fait le 19 octobre 2026** ; l'indice s'arrête à 2025, 2026 est
  en dinars courants seulement. Restent : le seuil de la tranche à 0 % rapporté au SMIG ; la CSS des
  personnes physiques, dérivée du barème de l'IRPP (voir `taux-moyens-marginaux-baremes.md`) ;
  la version arabe du chapitre, à rendre avant fusion.

- **Le patrimoine immobilier : mutations, plus-values, antécédents fonciers** (17 octobre 2026 ;
  chapitre `precis/fr/fiscalite/_patrimoine_immobilier.qmd`, **rédigé le 17 octobre 2026**, en
  français seulement ; manque n° 6 de la revue du 5 octobre). Notes :
  `fiscalite-patrimoine-immobilier-mutations-plus-values.md`, `…-antecedents-fonciers.md`,
  `…-dates-textes-series.md` ; plan : `fiscalite-patrimoine-immobilier-plan-architecte.md`
  (décisions du propriétaire du 17 octobre 2026 : cinq réformes, 1977, 1990, 1993 avec la loi
  n° 87-73, 2014, 2017 ; antécédents du droit musulman et de la loi foncière). **Écrit** : vue
  d'ensemble ; antécédents (droit musulman et habous d'après les sources secondes, **loi foncière
  du 1er juillet 1885**, JOT n° 134 du 12 juillet 1885, mise à exécution par le décret du 28 juin
  1886, lien avec l'impôt de 1886 à 1892 d'après le rapport Massicault, textes de 1956 à 1965) ;
  tarif de 1969 ; cinq réformes et leurs registres repliés ; état du droit au 1er janvier 2026 ;
  donations et successions, terrains, promoteurs, droit complémentaire ; longue période (sans
  figure) ; rapports et études. **Corrigé dans `_impot_revenu.qmd`** : la ligne de la loi de
  finances pour 2023 du registre (la condition de première cession vient de la loi de finances pour
  2005, art. 60) ; renvoi vers le nouveau chapitre. **Tranché par le propriétaire le 18 octobre 2026** : les
  dix points du § M6 du plan, validés tels qu'appliqués (commentaires `À CONFIRMER` retirés) ;
  la figure des prévisions reste limitée à 2011-2020, l'extension à 1970-1993 et 2021-2022 restant
  à faire si les données se trouvent (TODO de `fig-pi-previsions`) ; section « Ce qu'en dit
  l'économie » resserrée, le détail par étude replié dans « Détail des études citées ». **À
  trancher par le propriétaire** : la coupe de l'histoire de la plus-value dans `_impot_revenu.qmd`
  (décision 2, non faite). **Intégré le 18 octobre 2026** (note
  `fiscalite-patrimoine-immobilier-lectures-2026-10-18.md`) : dates d'effet de la LF 1973
  (31 déc. 1972), de la LF 1975 (2 janv. 1975), de la LF 1989 (loi du 31 décembre 1988, 2 janv.
  1989), de la loi n° 98-73 (dépôt 12 août, 17 août 1998, et art. 12 sur les opérations
  antérieures), de la LFC 2014 (27 août 2014) et de la LFC 2015 (29 août 2015) ; défaut d'origine
  1,25 → 1,40 % en 1969 ; art. 8, § II, de la loi n° 93-53 ; LF 1977, art. 27 (« moins de 5 ans »
  = première tranche, pas de trou à cinq ans) ; assiette du droit complémentaire (valeur globale,
  art. 20 *bis*) ; terrains en 1982-1983 par la LF 1980 (loi n° 79-66, art. 14 et 15, borne au
  1er janvier 1986), ligne ajoutée au registre. **Intégré le 18 octobre 2026** (note
  `successions-bareme-1985-1993.md`) : barème de 1984 complet (mutations par décès seulement),
  abattement de 1975 et sa reprise par le code (art. 51, I), 4 000 D par héritier handicapé
  (art. 51, II), habitation principale limitée à 1 000 m² (art. 53), tableau des abattements
  1975-1998 (`tbl-pi-abattements-successions`) ; constat « aucune modification » étendu aux LF 1992
  et 1993, LFC 1989 et 1991, lois n° 87-71 et 87-73 ; affirmation retirée selon laquelle le code
  remplace pour les donations le barème de 1984 ; art. 26 de la LFC 2015 : la date du 1er janvier
  2016 rattachée à la seule déduction des intérêts (note commune n° 18/2015, p. 1 et 5) ; plus-value :
  majoration de 10 % par année vérifiée dans la LF 1977 (art. 27) et le code de 1990 (art. 28, § IV,
  p. 7). **Reste à lire** (lisible dans le corpus local) : LF 1987, LF 1988 hors art. 32 et LF 1989
  hors pages lues, pour le barème successoral 1984-1993 (`r-bareme-successions-1985-1993`) ; tarif
  des donations de 1975 à 1993 (loi n° 74-101, art. 29 et 31) ; art. 30 de la LF 1975 sur l'édition
  arabe (p. 3221) ; décret n° 68-104 ; contexte des réformes (exposés des
  motifs et débats de 1969, 1977, 1987, 1993, 2017 ; documents de la réforme fiscale 2013-2014).
  **À obtenir** (autre source) : interprétation administrative de la cession après la dixième
  année (LF 1977 et 1981) ; seconde source pour la publication de la LF 1973 au 29 décembre 1972,
  déduite de l'en-tête et d'un décret du même fascicule. **Différé** (décision du propriétaire
  du 18 octobre 2026 : textes de 1885-1957 cités indirectement) : décret du 28 juin 1886 et loi
  du 16 mai 1886 (`r-loi-fonciere-1885-1886`) ; tarif du décret du 19 avril 1912 et textes de
  1948-1965 (`r-enregistrement-protectorat-1912-1954`) ; fascicules de 1957 de l'ancienne série
  (`r-habous-prives-1957-fascicule`) ; texte du taux de 7,25 % et de la réduction voulue en 1892
  (`r-reduction-droits-mutation-1892`) ; décret du 19 mars 1874. **À reprendre (règle du
  propriétaire du 18 octobre 2026, pas de fait inconnu dans le texte)** : la colonne « Ce qui en
  est connu ici » et les cellules « intitulé seul » du tableau des textes fonciers
  (`tbl-pi-textes-fonciers`). **Données** : prévisions du tableau A antérieures à 2020 à lire à l'image
  (OCR non vérifiée) et à verser dans `tunisia-data` avant la figure `fig-pi-previsions` ;
  tableaux A de 2000-2010 et 2023-2026 ; réalisations par article ; nombre d'actes et de cessions.
  **Section « Ce qu'en dit l'économie »** : figure `fig-pi-ipim` ajoutée le 18 octobre 2026
  (indice des prix déclarés de l'immobilier de l'INS, 2015 = 100, terrains, appartements,
  maisons ; méthode révisée T1 2000 - T4 2025 et ancienne méthode T1 2000 - T4 2021 tracées
  séparément ; séries `ins-ipim-trimestriel` et `ins-ipim-trimestriel-methode-anterieure`
  snapshotées le 18 octobre 2026 ; clé `ins-ipim` versée ; module
  `figures/patrimoine_immobilier.py`). Restent : révisions des derniers trimestres et écarts
  entre classeurs (TODO économiste) ; vue déflatée à proposer ; dans `tunisia-data`, réécrire
  les `caveats` du catalogue (« non extraites », « seule l'édition… est retenue »), affichés tels
  quels dans l'onglet « Sources ».
  **Section « Les donations et les successions »** (18 octobre 2026) : figures
  `fig-pi-tarif-successions` (taux marginal en escalier et taux moyen en courbe selon la part
  nette, quatre parentés, états du 1er janvier 1984, du 17 mai 1993 et du 17 août 1998 ; tracée
  depuis le 19 octobre 2026 par le composant commun `scripts/taux_bareme.py`, voir
  `docs/notes/taux-moyens-marginaux-baremes.md`) et
  `fig-pi-abattements-successions` (trois abattements, dinars courants et dinars de 2025, un
  segment par texte en vigueur) ; `tbl-pi-abattements-successions` désormais engendré, avec ses
  colonnes en dinars de 2025 (TODO rédacteur levé). Séries `successions-tarif` et
  `successions-abattements` émises par `scripts/generate_bareme_tables.py` (openfisca-tunisia
  ≥ 0.136). Reste : le mode de liquidation du barème de 1984, qu'aucun texte de 1962 à 1984 ne
  dit (note `docs/notes/successions-liquidation-1969-1984.md`, fiche
  `r-liquidation-successions-1929`) : la figure ne trace que le taux de la tranche pour 1984 ;
  lire le décret du 28 décembre 1929 (Revue algérienne, tunisienne et marocaine de législation,
  1930, Gallica `bpt6k442529z`), puis rétablir la courbe du taux moyen ou ajouter le mode
  « tranche atteinte ».
  Glossaire de la section (18 octobre 2026) : huit notions ancrées et définies, au statut
  `provisoire` — seuil à saut, seuil à changement de taux, regroupement, sous-déclaration, effet
  de verrouillage, capitalisation d'un impôt, perte sèche, incidence fiscale. Restent : termes
  arabes à faire confirmer ; équivalents français de *notch* et *kink* à fixer sur une source
  française de référence.
  **Bibliographe** : clés à créer pour la loi n° 79-27, la loi n° 70-66 (LF 1971), les lois n° 59-131,
  64-28, 74-53 et le DL 61-15, la loi n° 90-17, la loi n° 70-25, les avis du Conseil constitutionnel
  n° 31-2006 et 53-2006 ; notes communes 23/2014 et 28/2002 ; URL pist.tn de `lf-2016`, `lf-2019`,
  `lf-2020` ; compléter les notes de `loi79-66-lf1980` (art. 14 et 15, pp. 3542-3543),
  `loi-93-53-cdet` (art. 3, p. 715 ; art. 8 § II, p. 716), `loi-98-73` (dépôt du 12 août 1998,
  art. 12), `lfc-2014` et `lfc-2015` (dépôts) ; `lfc-1989` (à reprendre de `compensation/references.json`),
  `lfc-1991`, `dgi-nc-15-2016`, `dgi-nc-17-2016` (notices proposées dans
  `successions-bareme-1985-1993.md`, § 9). **Traduction arabe** différée : ajouter le chapitre au `_quarto.yml` arabe à la
  livraison. Fiches de recherche : les quatre ci-dessus, `r-pv-immobiliere-modificatifs-2023` et `r-bareme-successions-1985-1993`.

## Retraites

- **Tableaux et figure engendrés depuis les paramètres (24 octobre 2026)** (`_secteur_public.qmd`) : la retenue
  des députés et la contribution de l'État (`tbl-cnrps-deputes-retenue`, `fig-cnrps-deputes-retenue`, série
  `retraites-deputes-retenue`), les limites d'âge du Tribunal administratif et de la Cour des comptes
  (`tbl-cnrps-magistrats-ta-cc`, sans les colonnes « Portée » et « Membres » du tableau écrit à la main : les fonctions
  visées passent dans la phrase d'introduction) et le seuil du différentiel complémentaire (`tbl-cnrps-differentiel`) ne
  sont plus écrits à la main ; valeurs et dates identiques à celles du chapitre. **Reste à engendrer** dans la même
  section : le tableau des trois régimes spéciaux (`tbl-regimes-speciaux`, règles d'ouverture, de calcul et de jouissance,
  que l'arbre ne porte pas) et les taux du gouvernement et des gouverneurs (nœud `gouvernement_deputes_gouverneurs`
  non chargé, `docs/notes/backlog-modele.md`). **Reste** pour les textes arabes des trois tableaux : relecture de
  « الفارق التكميلي » et des intitulés de colonnes par le relecteur-ar.

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
- **Départs avant l'âge légal hors de la loi n° 85-12 : exposés (24 octobre 2026)** (§ `#sec-cnrps-departs-anticipes` :
  `#sec-cnrps-retraite-anticipee-1987`, `#sec-cnrps-retraite-avant-age-2009`, `#sec-cnrps-retraite-avant-age-2017`,
  programme de 2022 à 2028 dans `#sec-cnrps-reforme-2022` ; notes `docs/notes/retraites-depart-anticipe-2009.md` et
  `docs/notes/regimes-speciaux-recrutement-departs-effectifs-2026-10-23.md`).
  - **Fait** : loi n° 87-7 (art. 1 à 8, JORT n° 18/1987, pp. 363-364) et décret n° 87-337 (art. 1 à 9, pp. 369-370), lus à l'image ;
    loi n° 2017-51 (art. 1 à 7, éd. ar. pp. 2126-2127 ; traduction française « pour information », p. 2303) et décret
    gouvernemental n° 2017-825 (art. 1 à 10, éd. ar. pp. 2380-2381) ; dates d'effet par le dépôt des fascicules (6 juillet et 29 juillet 2017) ;
    décret présidentiel n° 2022-542 et arrêtés annuels de délais 2022-2025 (pp. 1926, 34, 3653, 3784), art. 14 de la loi de
    finances pour 2025 (prolongation jusqu'au 31 décembre 2028, éd. ar. p. 6420) ; sort du compte spécial de 2009 : abrogé par
    l'art. 17, 4), de la loi de finances pour 2025 (éd. ar. p. 6422), solde transféré au fonds d'assurance contre la perte d'emploi
    pour des motifs économiques ; recettes prévues du compte (tableaux « B » 2009-2013) et excédents transférés au budget
    (lois de règlement, gestions 2015-2018) ; page de l'avis n° 27-2009 : non relevée (TODO conservé).
  - **Reste, lisible au corpus ou à océriser** : pourcentages d'affectation de 2009, 2011 et 2012 (fiche
    `r-cnrps-fonds-retraite-avant-age-2009-taux` : les quinze fascicules français sans couche texte ont été océrisés le 24 octobre
    2026, aucun décret de pourcentages ; les sommaires de 362 fascicules arabes (n° 50 de 2009 au n° 103 de 2012) ont été océrisés en arabe le 24 octobre 2026 :
    seul le décret n° 2011-932 ressort ; reste le corps des fascicules arabes de 2009 à 2012 ; les lois de finances 2011, 2012 et le décret-loi n° 2011-56 ne portent que le tableau B) ; dépenses du compte (fiche `r-cnrps-compte-retraite-avant-age-2009-depenses` : annexes des
    lois de règlement) ; relecture à l'image des art. 9 à 13 du décret n° 2022-542 (faite le 24 octobre 2026 sur le fascicule français : art. 9, 11 et 13 précisés au chapitre) ; ligne « 2009-39 » du guide statistique 2000-2010
    et page de la valeur 2 686 du guide 2010-2014 ; rectificatifs du décret n° 82-1030 et de la loi n° 81-6 (scans locaux, pages à identifier).
  - **Reste, à obtenir** : exposé des motifs et débats des chambres (30 juin et 4 juillet 2009 ; 3 mars 1987) ; convention entre
    le ministre des finances et la CNRPS (décret n° 2009-2085, art. 8) et convention du décret n° 2017-825 (art. 8) (fiche
    `r-cnrps-convention-retraite-avant-age-2009` : aucune approbation par décret au JORT, sommaires arabes 2009-2012 compris ; à demander
    à la CNRPS ou au ministère des finances) ; arrêté du
    Premier ministre fixant le contingent de 1987 ; nombre de départs de 2017-2021 et de 2022-2025 ; décision sur la bonification
    et le plafond du taux de liquidation (question de droit non tranchée par les textes).
- **Magistrats de l'ordre judiciaire : limite d'âge (24 octobre 2026)** (`#sec-cnrps-magistrats`) : décret n° 85-614 (JORT n° 32, p. 599),
  loi organique n° 85-79, art. 43 nouveau (JORT n° 59, p. 1024), loi organique n° 88-73 (JORT n° 47, p. 1019), d'après
  `docs/notes/regimes-speciaux-magistrats-2026-10-23.md` ; loi n° 2019-37 relue en entier : aucune disposition propre aux
  magistrats. **Fait le 24 octobre 2026** : limites d'âge du Tribunal administratif
  (décret n° 73-459, JORT n° 37/1973, p. 1532) et de la Cour des comptes (décret n° 74-820, JORT n° 55/1974, p. 1919), lues à l'image,
  65 ans ; loi organique n° 2016-34 (art. 53, 78, 80) ; les lois organiques n° 91-9, 2005-81 et 2012-13 ne touchent pas l'art. 42 de
  la loi n° 67-29. **Reste** : sort du décret n° 85-614 après 1988 (fiche `r-decret-85-614-sort` : plein texte lu de 1997 à 2026, zéro
  occurrence ; fascicules de 1988 à 1996 à océriser) ; texte consolidé de l'art. 42 ; limites d'âge propres éventuelles de la loi organique n° 72-67 et du décret-loi n° 70-6 ;
  pensions des magistrats.
- **Régimes spéciaux (députés, gouvernement, gouverneurs, Constituante) : portés au livre le 24 octobre 2026** (`#sec-cnrps-regimes-speciaux`) :
  LF 1989 art. 75-76 (JORT n° 87/1988, p. 1800, lue à l'image), loi n° 2005-54, loi n° 2015-39 (membres de l'Assemblée constituante, JORT
  n° 79/2015, pp. 2371-2372), décret-loi n° 2011-48 (contribution de l'employeur, +1 point au 1er juillet 2011), LF 2026 art. 102-103
  (nouveaux art. 3 et 5 de la loi n° 85-16, effet au 13 mars 2023, p. 4257 de l'édition arabe), loi n° 83-31 art. 8 à 10 et loi n° 88-16 art. 6
  (lues à l'image) ; loi n° 88-101 (lue à l'image, JORT n° 55/1988, p. 1156) ; chaîne des taux de la retenue et de la contribution de
  l'art. 5 de la loi n° 85-16, 1985-2023 (tableau `tbl-cnrps-deputes-retenue` : loi n° 85-16, loi n° 94-71, LF 2002, loi n° 2007-43, LF 2026).
  **Reste** : application aux députés du relèvement d'un point du décret-loi n° 2011-48 (le texte ne nomme pas la loi n° 85-16) ; LF 1988 art. 60-61 et loi n° 2005-55 (anciens présidents, Premiers ministres,
  présidents des chambres : avantages en nature, relevant plutôt du livre « Rémunérations publiques » où `loi2005-55` existe) ;
  régime des assemblées postérieures à 2014 (aucun texte identifié, fiche
  `r-indemnite-parlementaire-decret`).
  Les rectificatifs du décret n° 82-1030 et de la loi n° 81-6 restent à relire sur les scans locaux après identification exacte
  des pages : un numéro peut avoir des homonymes.
- **RSNA, RTNS et régime public : lacunes de lecture closes le 24 octobre 2026** : date d'effet du décret n° 2002-3018 (dépôt du 30 novembre 2002,
  exécutoire le 5 décembre) ; date d'effet du décret n° 94-1477 (dépôt du 18 juillet 1994, exécutoire le 23 juillet) ; loi n° 88-38, art. 1 à 4
  (ni vieillesse ni retraite) ; décret n° 90-1455, art. 3, 14, 30, 32, 43 et 54 (lus à l'image, ajoutés au tableau des textes) ; art. 30 et 32 relus le 25 octobre 2026 contre les art. 30 et 32 de 1974 (JORT n° 30 de 1974, p. 917) : le tableau des textes ne porte plus qu'une ligne par article (deux lignes en doublon, contraires, retirées) et la section « Les droits dérivés » dit les deux états datés (1974, 1990). Aucune modification postérieure de l'art. 32 n'est identifiée (décrets n° 97-291, 97-1927, 2007-2148 : art. 29, 33, 38, 42, 53) ; décret n° 80-103,
  art. 11 bis (18 mois de cotisations au cours des trois premières années, édition arabe, p. 252) ; décret n° 2026-229 du 2 octobre 2026 (liste
  du décret n° 85-1176, Instance supérieure indépendante pour les élections). Relances des fiches `r-dec74-499-modificatifs`, `r-rsna-age-relevement`,
  `r-dl2024-4-art33` et `r-rsna-bareme-annees-manquantes` jusqu'au JORT n° 97 de 2026 : rien de nouveau (un arrêté conjoint du n° 80 de 2026 cite
  le décret n° 2007-2148 comme dernier modificatif du décret n° 74-499). **Reste** : méthode de calcul du barème d'actualisation, hors du JORT.
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
  | survivants du RSNA | la branche existe ; l'âge de 55 ans du remariage (1990) est **engendré depuis le 25 octobre 2026** ; restent des **règles** — état de 1974 du remariage (suppression à tout âge), plafond de cumul, cumul invalidité/survivant |
  | départs anticipés du RSNA | les durées et les taux sont versés ; les **conditions** de chaque cas ne sont pas des valeurs datées |
  | article 32 de la loi n° 85-12 | repère de 60 → 62 ans exécutoire le 5 mai 2019 ; les autres distinctions entre colonnes restent des règles |

  Les conditions d'âge, d'études et de ressources de la pension d'orphelin restent à la main.

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

- **Aides exceptionnelles de 2020 et aide de 2021 — 14 octobre 2026** (`_non_contributives.qmd`,
  `#sec-nc-aide-2020` nouvelle, `#sec-nc-aide-2021` corrigée ; note
  `docs/notes/prestations-aides-exceptionnelles-covid-2020-2026-10-14.md`) :
  - **fait** : section 2020 (arrêtés conjoints du 10 juillet et du 31 août 2020 lus au fascicule
    français, pages établies page par page : 1515-1517 et 2010-2012 ; tableau du droit par tranche ;
    tableau des versements du rapport annuel de performance 2020 ; rapports de la Banque mondiale à
    part, « deux mois » et « one-time » en regard) ; section 2021 corrigée à l'image du tableau de
    l'art. 2 (JORT n° 75, p. 2071) : six catégories, la première sans condition, cinq conditions pour
    les catégories 2 à 5, une condition de salaire en plus pour la sixième ; procédure des art. 3 à 7 ;
    clés `decret-gouv-2020-475` et `-476` portées dans `@tbl-nc-cartes-prorogations` ; renvoi depuis
    `sante/_couverture.qmd#sec-soins-frontiere` ; fiches `r-covid-2020-decision-avril` et
    `r-covid-2020-ligne-aides-exceptionnelles` créées, passe du 14 octobre 2026 sur `r-amg-cartes-quotas`.
  - **reste, pour le bibliographe** : clés des décrets-lois n° 2020-3 et n° 2020-4 (JORT n° 32,
    p. 767 et 769) et du décret gouvernemental n° 2020-184 (JORT n° 36, p. 884-887 ; l'exclusion des
    bénéficiaires des aides aux familles est à l'**art. 5, p. 886**, lu à l'image, et non à l'art. 4,
    p. 885, comme le dit la note) ; clé de la loi n° 2020-45 (LFR 2020) ; clé du rapport annuel de
    performance 2021 du ministère (crédits de l'aide de 2021).
  - **reste, pour le documentaliste** (questions ouvertes de la note, § 10 c) : texte qui a fixé
    les montants avant les arrêtés de juillet et d'août 2020 (`r-covid-2020-decision-avril`, à
    obtenir : archives du web de pm.gov.tn et social.gov.tn) ; aide de 60 D de Ramadan annoncée pour
    le 4 mai 2020, avant l'effet de l'arrêté du 19 mai 2020 (25 mai), et régime antérieur à 40 D ;
    date du versement sur formulaire (mai ou juin 2020) et du premier paiement (mars ou avril 2020) ;
    unité du « virement (326,805 DT) » du rapport 2020 et texte de la ligne budgétaire
    (`r-covid-2020-ligne-aides-exceptionnelles`, annexes de l'arrêté du 4 mai 2021 à océriser) ;
    nombre de cartes de soins à tarifs réduits en 2020, connu seulement par la Banque mondiale
    (`r-amg-cartes-quotas`) ; édition arabe de l'arrêté du 31 août 2020 à relire à l'image (début
    p. 2249 ou 2250) ; le sigle « P2P » (fiche `r-covid-2020-p2p` proposée par la note, non créée :
    le chapitre n'en a pas besoin).
  - **fait le 24 octobre 2026** : le décret-loi n° 2020-30 du 10 juin 2020 (complément portant les
    pensions à 180 D, art. 1) est exposé au volume « Retraites » (`_secteur_public.qmd`, section « La péréquation cotisée »). Reste :
    prolongation ou relèvement éventuel du seuil de 180 D, conventions de gestion, bénéficiaires et coût.

- **Relecture à l'image du 24 octobre 2026** (`_autres_risques.qmd`, protection des travailleurs ayant cessé leur travail) :
  - *fait* : loi n° 2002-24 (JORT n° 18 du 1er mars 2002, p. 515, art. 1 et 2, sans clause d'effet, dépôt le
    2 mars 2002) ; rectificatif à la loi n° 96-101 (JORT n° 7 du 24 janvier 1997, p. 114) ; décrets
    n° 97-1925 et n° 97-1926 (JORT n° 80 du 7 octobre 1997, p. 1849-1850, articles 1 à 8, sans clause
    d'effet) : texte conforme aux lignes de registre ; **dates d'exécution levées** par les mentions de dépôt
    au siège du gouvernorat de Tunis : n° 80 de 1997 le 9 octobre 1997 (exécution le 14 octobre 1997), n° 34 de
    2002 le 27 avril 2002 (2 mai 2002), n° 31 de 2006 le 19 avril 2006 (24 avril 2006). Les décrets n° 2002-886,
    n° 2002-887 et n° 2006-1025 étaient relus à l'image depuis le 12 octobre.
  - *PNAFN* : fiche `r-pnafn-montants-historiques` ouverte ; le palier de 150 D (2015) est confirmé par le
    projet de loi de finances pour 2018 (presse, 29 octobre 2017) et l'étude CRES-BAD ; l'annonce de 180 D
    date du 13 janvier 2018 sans texte ni date d'effet ; les neuf autres paliers restent sans source. Piste
    non suivie : budgets économiques 2012-2018, circulaires, Wayback Machine sur social.gov.tn.

- **Lectures du 10 octobre 2026 portées dans le volume** (`docs/notes/prestations-sociales-lectures-2026-10-10.md` ;
  quatre chapitres, corrections ciblées, aucun plan changé).
  - *Levé* : les dates d'effet des lois n° 95-101 (10 décembre 1995), du 22 juillet 1996 (4 août 1996),
    n° 96-101 (1er décembre 1996), n° 2002-24 (7 mars 2002), n° 2002-32 (21 mars 2002), n° 2017-47
    (3 juillet 2017), n° 2024-44 (17 août 2024), du décret-loi n° 2024-4 (24 octobre 2024), de l'art. 17 de
    la loi de finances pour 2025 (1er janvier 2025, art. 84) et de la loi n° 82-71 (fourchette du 19 au
    22 août 1982), chacune avec son calcul dans sa ligne de registre ; **la section de la cessation
    d'activité (`#sec-perte-emploi`) dit l'état du droit du 7 mars 2002** (loi n° 2002-24), la rédaction de
    1996 étant l'état antérieur, avec le rectificatif de 1997 et les décrets d'application ; la loi n° 82-71
    (art. 65 ter, clé `loi82-71`) ; la frontière entre régimes et assistance (`#sec-matrice-frontiere`) ;
    le score (source du ministère pour le premier décile, circulaire du 10 mai 2022) ; les rentes de la loi
    n° 94-28 (art. 42 à 53) ; l'art. 2 de la loi n° 95-101 ; l'art. 17 de la loi de finances pour 2025 dans
    son texte français ; les aides catégorielles des lois de finances pour 2025 et 2026 (condition de
    l'art. 81 ajoutée) ; les aides aux familles d'accueil (`#tbl-nc-familles-accueil`, deux séries) ; les
    modalités, les taux et le plafond de 2008 de l'assurance maladie (bloc replié) ; les décrets
    n° 99-1372 (le n° 2018-626 est relu et porté le 23 octobre 2026) ; les conditions du programme d'autonomisation ; le tableau 13 du rapport du
    ministère pour 2023 (il ne se referme pas).
  - *Trouvé en écrivant, hors de la note* : les décrets de 1997 sont modifiés — n° 2002-886 et
    n° 2006-1025 pour le décret n° 97-1925 (aide plafonnée à trois, puis six, puis douze mensualités),
    n° 2002-887 pour le décret n° 97-1926 (articles 1 à 7 remplacés). Lus par le rédacteur sur la couche
    texte du corpus (`2002/fr/Jo0342002.pdf`, police décalée, décodée ; `2006/fr/Jo0312006.pdf`), puis
    **relus à l'image le 12 octobre 2026** : contenu confirmé, registre complété (articles 3 bis et 6 de
    2002, inscription au bureau d'emploi), aucune clause d'effet, aucun modificatif postérieur à 2006 dans
    les intitulés. Dates d'exécution levées le 24 octobre 2026 (voir plus haut).
  - *Reste, lisible au corpus* : relecture à l'image des textes repris de la couche texte (loi n° 94-28 art. 42 à 53, décrets n° 2007-1367,
    n° 2008-756 et n° 2021-318, arrêté du 3 juin 2008, arrêtés des familles d'accueil, décret n° 2022-715
    dont les articles finaux, lois de finances pour 2025 — texte français de jibaya.tn — et pour 2026 —
    arabe) ; art. 34 de la loi
    n° 60-30 ; décrets n° 99-1514, n° 2016-1401, n° 93-529, n° 94-1738, n° 2019-1130, n° 2002-916 ;
    décret n° 75-952 et circulaire n° 42 de 1996 ; décret du 6 avril 1950 ; loi n° 95-56 et gestion des
    accidents du travail du secteur public ; arrêté conjoint du 25 juin 2007 (affections lourdes ou
    chroniques).
  - *Reste, à dépouiller* : révisions du plafond annuel des soins ambulatoires après 2008 ; arrêtés des
    familles d'accueil après 2010 et 2017 ; arrêtés d'application des art. 35, 71 et 81 de la loi de
    finances pour 2026 ; lois de finances de 2007 à 2026 pour les art. 52, 54 et 61 de la loi n° 60-30 ;
    six fiches de recherche ouvertes le 10 octobre 2026 (`r-ar-etat-2026-modificatifs`,
    `r-am-extension-loi2002-32`, `r-amen-carte-arrete-cahier-des-charges`, `r-amen-cumul-af-contributive`,
    `r-loi96-101-extension`, `r-pf-taux-apres-1996`).
  - *Reste, à obtenir* : les circulaires n° 12 du 10 mai 2022 et d'octobre 2025 (ministère des Affaires
    sociales) ; le rapport technique entier CRES-Banque mondiale (le résumé est rangé) ; le décret du
    8 juin 1944 ; l'édition française du JORT n° 149 de 2024 (absente de pist.tn) ; les séries de données
    (CNSS, CNAM, CNRPS, PNAFN, versements de 2025).
  - *Hors de ce volume* : le volume des cotisations nomme encore le fonds de 2025 par la traduction de
    l'arabe (« perte de postes de travail ») ; le texte français dit « Fonds d'assurance contre la perte
    d'emploi pour des motifs économiques ». Les lignes de catalogue de `tunisia-data` pour les cinq
    fichiers du ministère rangés le 10 octobre 2026 sont proposées dans la note (§ 6.3), non écrites.
  - *Tableaux faits main ajoutés* : `tbl-ar-cessation-etats`, `tbl-ar-am-taux`, `tbl-ar-am-plafond`,
    `tbl-nc-familles-accueil` (`backlog-modele.md`).

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
     (`#tbl-matrice-textes`, l'ancienne matrice). **La frontière est établie le 10 octobre 2026** : aucune
     condition de non-affiliation pour le transfert mensuel (loi organique n° 2019-10, décret
     gouvernemental n° 2020-317) ni pour la carte de soins gratuits (décret n° 98-1812 et
     modificatifs de 2004, 2012, 2016, 2020 et 2021) ; condition écrite pour la carte à tarifs
     réduits et pour les ayants droit du support de 2022 ; cumul des deux allocations familiales
     pour une famille pauvre affiliée : règle non identifiée (fiche `r-amen-cumul-af-contributive`).
     **Reste** : l'extension de la loi n° 96-101 aux régimes agricoles et aux contractuels publics
     (fiche `r-loi96-101-extension`) ; l'entrée du régime de la loi n° 2002-32 dans l'assurance
     maladie (fiche `r-am-extension-loi2002-32`) ; l'art. 34 de la loi n° 60-30, non lu ; douze
     notions de glossaire à créer (terminologue). La colonne
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
  - *levé le 10 octobre 2026* : dates d'effet de la loi du 22 juillet 1996 (4 août 1996, à citer
    par sa date : deux lois sont imprimées sous le n° 96-65) et de la loi n° 96-101 (1er décembre
    1996) ; loi n° 82-71 lue à l'image, clé `loi82-71`, ligne de registre `#r-pf-reg-1982`. Seule
    reste « non établie ici » la date d'effet du décret n° 75-952, non lu ;
  - *à dépouiller* : les lois modifiant les articles 52, 54 et 61 de la loi n° 60-30 **de 2007 à
    2026** (fiche `r-pf-art61-apres-1988` ; passe du 10 octobre 2026 sur les intitulés seuls, lois de
    finances non dépouillées) ; un éventuel décret de fixation des indemnités familiales du secteur
    public **postérieur à 1996** (fiche `r-pf-taux-apres-1996`, intitulés seuls) ;
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
- **Aides adjacentes — fait le 10 octobre 2026** : arrêtés du 30 septembre 1997 (deux), du
  12 décembre 2003 et du 24 juin 2010 (personnes âgées), du 1er juin 2006 et du 28 avril 2017
  (personnes handicapées), lus sur la couche texte et portés à `#sec-nc-adjacents` — famille
  d'accueil d'une personne âgée : 90, 100, 150 D ; d'une personne handicapée : 150, 200 D. Les
  deux aides « à la personne » renvoient au montant du programme d'aide aux familles
  nécessiteuses. Reste : arrêtés postérieurs à 2010 et à 2017, relecture à l'image. Le décret
  n° 2018-626 est lu et porté (`#r-nc-li-2018`).
- **Lois de finances — fait le 10 octobre 2026** : art. 26 de la loi de finances pour 2025 (texte
  français, p. 3427) et art. 35, 71, 81, 96 et 110 de la loi de finances pour 2026 (édition arabe,
  la seule : le fichier « français » de pist.tn est l'arabe), portés à
  `#sec-nc-aides-categorielles`. Reste : les arrêtés d'application des articles de 2026.
- **Décret n° 2018-626 et loi de finances pour 2025, art. 26 — clos le 23 octobre 2026**
  (note : `docs/notes/prestations-2018-626-lf2025-art26.md`). Décret relu à l'image (FR p. 2653,
  AR p. 3524) ; décret n° 2014-1526 exécutoire le 19 mai 2014 ; art. 2 du décret de 2018 :
  quatre → six cadres. Aide « gluten » : arrêté du 30 juillet 2025 abrogé par l'arrêté conjoint
  du 14 juillet 2026 (JORT n° 70, pp. 1327-1328, exécutoire le 19 juillet 2026 ; commission
  médicale, registre spécifique, condition de non-couverture pour le *xeroderma pigmentosum*),
  portés à `#sec-nc-aides-categorielles`. Le tableau des montants `#tbl-nc-gluten-montant` est
  engendré depuis le 23 octobre 2026 (`generate_prestations_tables.py`, 0.145) ; le tableau
  `#tbl-nc-aides-categorielles`, qui mêle des aides sans feuille (art. 71, 81, 96 de 2026) à
  des conditions rédigées, reste écrit à la main. Lacunes :
  - **articulation art. 26 (2025) / art. 35 (2026)** : montant servi du 1er janvier au
    19 juillet 2026, survie de l'art. 26, cumul ; aucun texte lu (TODO HTML dans le chapitre) ;
  - **suite de la banque de données après mai 2019** : aucune prolongation ni abrogation du
    décret n° 2014-1526 trouvée dans `jort_cache` (fiche `r-banque-donnees-2014-1526-suite` ;
    miroir iort et plein texte 2018-2020 à parcourir) ; le « scoring » prévu à l'art. 3 du
    décret de 2014 n'est pas rapproché du score de l'Amen social, aucun texte lu ne le fait ;
  - **arrêtés d'application des art. 71 et 81 de la loi de finances pour 2026** : non
    identifiés (fiche `r-lf2026-art71-81-arretes`, fascicules postérieurs au n° 97 à lire) ; le
    décret n° 2026-192 du 27 juillet 2026 (JORT n° 76, AR p. 1600, enfants autistes en jardin
    d'enfants) est un programme distinct, non lu ;
  - **données** : ni effectif de bénéficiaires ni dépense de ces aides (budget du ministère des
    affaires sociales, rapports Amen social 2025 : non cherchés) ;
  - **LF 2025, édition française** : absente de pist.tn ; seule source, la copie locale
    (corpus local, texte arabe concordant sur l'art. 26) ; la notice n'a pas d'URL française ;
  - **LF 2026, art. 35** : relu sur le fascicule arabe (p. 4238) ; relecture à l'image des
    articles 35, 71, 81, 96 et 110 encore à faire.
- **Pagination des textes de 2024 et postérieurs — établie le 10 octobre 2026** et portée aux
  notices : décret-loi n° 2024-4, p. 2897-2902 en français ; loi n° 2024-44, p. 2215-2216 ;
  décret n° 2022-919, p. 3367-3370 ; loi de finances pour 2025, art. 17 p. 3423 du texte français
  (fascicule français absent de pist.tn ; folio arabe à trancher entre 6420-6421 et 6421-6422) ;
  loi de finances pour 2026, art. 35 p. 4238. La date de la loi n° 2017-47 est tranchée au JORT
  n° 50 de 2017 : 15 juin 2017, publié le 23 juin, exécutoire le 3 juillet 2017.
- **Décret n° 75-952** (`1975/fr/Jo08775.pdf`, p. 2884) : océrisé et lu à l'image le
  23 octobre 2026 (`docs/notes/ocr-cibles-2026-10-23.md`) : taux mensuels par enfant au
  1er janvier 1976 relevés ; reste à les verser à la série des indemnités familiales antérieure à 1986. La circulaire n° 42 de 1996,
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
  - **retouches du 9 octobre 2026 après lecture du rendu — sur `master` depuis le 10 octobre 2026 (#429)** :
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
    rectificatif du JORT n° 7 de 1997, p. 114, non lu) ; loi n° 2024-44 (aucune clause ;
    dépôt du 12 août 2024 relevé le 20 octobre 2026 dans les deux éditions : exécutoire le
    17 août 2024 selon la loi n° 93-64, ou le 13 août selon le décret-loi n° 2020-1 ; le
    propriétaire a tranché le 20 octobre 2026 pour le décret-loi n° 2020-1 : **13 août 2024**,
    à reporter à `#r-ar-2024-44` et aux tableaux de `_autres_risques.qmd`, qui écrivent encore
    17 août 2024 ; le chapitre `_temps_travail.qmd` du marché du travail porte déjà le 13 août) ; loi n° 2002-32, loi n° 95-101,
    loi n° 2017-47 (à confirmer ou à calculer) ; décret-loi n° 2024-4 : **24 octobre 2024**
    (décret-loi n° 2020-1), reporté le 23 octobre 2026. L'article final de la loi de finances pour
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

- **Rémunération des dirigeants d'entreprises publiques — rédigée et fusionnée le 23 octobre 2026
  (#499).** Sous-section « Les dirigeants »
  du régime conventionnel public (`#sec-conventionnel-dirigeants`, domicile unique), d'après
  `docs/notes/remunerations-decret-2015-2217.md` et
  `docs/notes/remunerations-publiques-dirigeants-plan-architecte.md` : grille de 2014 à 2015, deux
  modalités, règles autres que le montant, dérogations (décrets gouvernementaux n° 2020-422 et
  2017-1387), registre. Le marché contrôlé garde le décret gouvernemental n° 2015-968 (banques
  publiques, `#sec-marche-controle-dirigeants`). Corrections : intitulé du décret n° 2015-2217
  (« fixant le régime », non « fixant les taux »), exclusion des directeurs généraux des banques
  publiques, retrait du « versant contrôle » du glossaire, renvoi du volume des retraites.
  **Tâche « décret n° 2015-2217 » close.** Restent, avec l'état du texte :
  - **liste de la catégorie exceptionnelle** (art. 2) et **arrêtés de classement** : aucun texte
    identifié dans le corpus ; probablement non publiés, à obtenir auprès de la Présidence du
    gouvernement ou de la direction générale de la tutelle des entreprises publiques (fiche
    `r-decret-2015-2217-application`) ;
  - **décret n° 2006-242 et modificatifs** (n° 2009-188, 2010-24, 2010-215), **décret n° 2009-187** :
    absents de l'index sous ces numéros, probablement non publiés ; date du décret n° 2006-242
    différente selon les visas (2 ou 12 octobre 2006) ; plein texte des fascicules 2006-2010 non
    parcouru (fiche `r-dirigeants-ep-categorie-exceptionnelle-2006-2010`) ;
  - **fait le 24 octobre 2026** : décret n° 90-1855 (JORT n° 75/1990, pp. 1752-1753), modificatifs
    n° 92-1 (JORT n° 4/1992, p. 67) et n° 2006-2564 (JORT n° 80/2006, pp. 3460-3461), décret
    n° 84-865 (JORT n° 46/1984, pp. 1708-1709), modificatifs n° 82-509 (JORT n° 20/1982, p. 695) et
    n° 83-577 (JORT n° 48/1983, p. 1874) du décret n° 78-885 : lus à l'image (OCR au premier plan)
    et versés au chapitre (`#sec-conventionnel-dirigeants-1984-2006`, registre `#r-conventionnel-dirigeants-1982`
    à `-2006`) ; le régime de 1990 a quatre éléments dont une indemnité de gestion, l'exclusivité
    figure déjà en 1984 ;
  - **décret n° 78-885** (JORT n° 68/1978, pp. 2844-2845) et **circulaire n° 78-45** (JORT n° 2/1979,
    pp. 89-91) : le scan (`1978/fr/Jo06878.pdf`, `1979/fr/Jo00279.pdf`) ne rend presque rien à
    l'OCR par défaut ; **OCR à reprendre avec un autre réglage** ; montants de 1978 de l'indemnité de
    représentation et autres éléments à relever ; relation du décret n° 2014-12 au décret n° 90-1855
    à établir ;
  - **circulaire n° 04 du 10 mars 2021** : introuvable en ligne, probablement hors JORT, **à obtenir** ;
  - **liste nominative des « banques publiques »** (décrets n° 2013-4953 et 2015-968) : non établie,
    **à obtenir** (les visas du décret n° 2013-4953 citent les textes d'organisation de la BNA, de
    la BH, de la STB, de la BFPME et de la BTS, entre autres) ;
    régime applicable avant le 15 août 2015 aux directeurs généraux des banques publiques :
    **lisible dans le corpus** (décret n° 90-1855, lu le 24 octobre 2026, qui ne vise pas les banques à part ; reste le décret n° 2014-12 et le texte qui les exceptait avant 2015) ;
  - **dates d'effet** des décrets n° 2014-12, 2017-1387 et 2020-422 : colophon des fascicules,
    **lisible dans le corpus** ;
  - **texte arabe du décret n° 2015-2217** : intitulés et termes relevés, comparaison article par
    article à faire (**lisible dans le corpus**) ;
  - **décrets n° 2023-294 (art. 16) et n° 2017-985 (art. 4 nouveau)** : lus en arabe, clés à verser ;
  - **montants en dinars constants de 2015** : à ajouter quand la date d'effet du décret n° 2014-12
    sera établie ; tableaux faits main (`TODO (rédacteur)` : tableau engendré) ;
  - **séries** : aucune revalorisation des montants de 2015 trouvée jusqu'au 2 octobre 2026
    (constat de recherche) ; **effectifs de dirigeants par catégorie et coût budgétaire** : aucune
    source, **à obtenir** ;
  - **Zotero** : sept notices à verser ou à corriger (`docs/notes/biblio-a-rapatrier.md`).

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
    Banque mondiale (14,7 % en 2017, 10,7 % en 2010) sont citées sans page — les 8,9 % et
    7,5 % de 2013 et 2014 sont rendus au Livre blanc de 2018, p. 12, le 11 octobre 2026 — ;
    la base du PIB de la Banque
    mondiale est à relever dans sa revue des dépenses publiques de 2020 (le texte dit « n'est
    pas précisée ici »). Le 14,1 % de 2019 de la série (« Min Fin/presse ») n'est ni tracé ni
    affiché, faute de source. La part de 1997 en base 1983 citée au texte (10,97 %) n'est
    dans aucune figure : elle se recalcule sur `pib-courant-recouvrements` (2 293,5 /
    20 898,0) ;
  - **bibliographie — fait le 11 octobre 2026** : le titre et le titre court de
    `imf-tunisia-art4-2020` disent désormais « 2021 Article IV Consultation » dans les deux
    langues (page de garde du rapport n° 21/44 ; clé inchangée, année déjà 2021) ;
  - **catalogue de l'entrepôt** : `ins-pib-base-2015-2010-2020` manque aux `sources` de
    `masse-salariale-ratios` (le module l'ajoute à l'affichage) ; ses `caveats` s'adressent
    à qui trace la série (noms de colonnes, journal des corrections) : le module les
    remplace par un texte pour le lecteur (`PROVENANCE_LECTEUR`) ;
  - `_demo_figure_onglets.qmd` (hors livre, lit l'entrepôt directement) : non repris ;
  - **autres volumes non conformes** (figures de rendement fiscal, figures de la CNSS
    1990-2004, retraites, finances locales) : non touchés ici, inventaire sur la branche
    `docs/annexe-pib`.
- **Chapitres à étoffer** : régime conventionnel public et marché contrôlé ; le régime
  indiciaire est le plus développé. Ne pas réutiliser les longueurs des chapitres mesurées
  avant la relecture des rémunérations.
- **Régime statutaire autonome — réorganisé le 23 octobre 2026** (première moitié du plan
  `docs/notes/plan-regimes-speciaux-remuneration.md`, branche `rediger/regimes-speciaux-secteur-public`) :
  vue d'ensemble, mise en place 1967-1972, quatre réformes (1982-1983, 1995, 1997-2000,
  2011-2013), état du droit au 1er janvier 2026, magistrats (indemnité de magistrature
  1985-2028 et niveau calculé en dinars courants et constants), militaires, forces de sécurité
  intérieure, douanes, prélèvements corrigés, « Ce qu'en dit l'économie » ; corrections C1 à C7
  appliquées, C8 en `TODO` ; six fiches de recherche (`r-magistrats-majorations-indemnite`,
  `r-mil-traitement-base-1997`, `r-mil-solde-79-96-1982-1985`, `r-mil-charges-militaires-2011`,
  `r-fsi-indemnites-1992`, `r-douanes-indemnites-1997`). Restent :
  - **section budgétaire** (`#sec-statutaire-budget`) : **refaite le 23 octobre 2026** — crédits
    votés 2011-2026 (tableau repère et registre replié, dinars de 2015, part du total), effectifs
    autorisés 2021-2026, exécution 2022-2023, recrutements prévus 2013-2025, INS par renvoi,
    SIPRI titré « rapports extérieurs ». Restent : figure F2 à la place des tableaux, figures F3
    (SIPRI) et F4 (IISS par la Banque mondiale) après versement des séries dans `tunisia-data` ;
    totaux de la dernière page des tableaux C/ت 2020 et 2022-2026, mission Finances
    (« Douane ») — **lecture à l'image** (tableaux des LF 2020-2026 en image) ; recrutements
    prévus de 2012 (rapport sur le budget actualisé, sans clé) et de 2023 (rapport **à
    obtenir**) ; rapports sur le budget 2015-2021 et 2026 **à obtenir** ; répartition des
    paiements par mission 2018-2021 (Cour des comptes, **lecture à l'image**) ; figure F1 de
    l'indemnité de magistrature après versement de la série ; frise de la vue d'ensemble ;
  - **lisible dans le corpus** : permanence des magistrats depuis 2009 (décrets n° 2009-2826,
    2009-2791, 2009-2792, JORT n° 80 de 2009) ; décrets n° 85-907, 85-908, 93-2453, 93-2581
    (indemnité de magistrature au Tribunal administratif et à la Cour des comptes) ; n° 2006-1379,
    2000-1344, 2019-654 ; concordances de 2000 et 2012 des autres corps de sécurité intérieure ;
    décret gouvernemental n° 2016-512 (douanes) ; lois n° 72-40 et 72-67 (statut des membres
    du Tribunal administratif, C8) ;
  - **OCR ou lecture à l'image** : grilles de 1984 de la Garde nationale, des prisons et de la
    protection civile (n° 84-751, 84-752, 84-754, 84-756) ; statuts de 2006 (n° 2006-1160 à
    2006-1168, édition française en image) ; fascicules de février-mars 1992 (indemnités des
    forces de sécurité intérieure) et de 1982-1985 (solde des militaires) ; décret n° 72-230 ;
    décret n° 88-905 (champ) ;
  - **à obtenir** : édition arabe du décret n° 2019-285 (JORT n° 24 de 2019, 404 sur pist.tn) ;
    nombre de magistrats et effectifs par corps ; contexte des réformes de 1982, 1995, 2011,
    2013 et des majorations des magistrats de 2012-2013 et 2018 (sources de l'époque) ;
  - **hors chapitre, à signaler** : glossaire `solde-militaire` et `magistrat` (terminologue) ;
    livre « Retraites » : décret n° 85-614, loi organique n° 85-79 art. 43, loi organique
    n° 88-73 (fait le 24 octobre 2026, `#sec-cnrps-magistrats`) ; (`index.qmd` et § ventilation par ministère du régime indiciaire corrigés le
    23 octobre 2026) ;
  - **clés à créer (bibliographe)** : lois n° 72-67 ; décrets n° 88-908, 2013-1401, 2012-3552,
    2011-2093, 2011-2094, 2002-323, 2002-1048, 84-751 à 84-756 ;
  - fiche `r-augmentations-ep-2013-2025` : sa couverture omet les décrets des magistrats
    n° 2019-1132, 2020-768 et 2022-798, ces deux derniers absents de `jort_cache` ; à reprendre
    par une passe du documentaliste.
- **Régime indiciaire — corps particuliers et « Recruter et faire partir », 23 octobre 2026**
  (seconde moitié du plan des régimes spéciaux) : diplomates (`#sec-ri-diplomates`),
  enseignants-chercheurs (`#sec-ri-enseignants-chercheurs`), emplois fonctionnels et cabinets
  (`#sec-ri-emplois-fonctionnels`), fiche `#sec-ri-recruter-partir` (statut de 1983, recrutements
  dérogatoires 2011-2025, départs 1987-2028, prime de départ volontaire de 2018) ; champ
  statutaire de l'INS : le texte n'affirme plus l'exclusion des corps. Fiches
  `r-diplomates-indemnite-poste-apres-1998`, `r-loi2020-38-decrets-application`,
  `r-loi2025-18-application`. Restent :
  - **lisible dans le corpus** : modificatifs du décret n° 73-167 de 1985 à 1992 (scans,
    **lecture à l'image**) ; fin du statut diplomatique de 1991 (pp. 1423-1425) ; décret
    n° 76-843 (cabinets) et n° 71-364 (emplois fonctionnels), scans ; textes postérieurs à 2009
    sur les emplois fonctionnels (décret n° 2023-592, intitulé arabe) ; rédaction actuelle des
    art. 17 à 20 de la loi n° 83-112 ; LF 2026 art. 90, 92 et 108 (édition arabe) ;
  - **OCR ou lecture à l'image** : décret n° 85-1405 et majorations de l'indemnité d'encadrement
    et de recherche (niveau non reconstitué ; tranches de 1996 à 2011) ; décret n° 2009-910
    (indemnité spécifique) et sens des montants du décret n° 2013-1470 (tranches ou montants
    successifs) ; recrutements « exceptionnels et temporaires » de 1957-1969 ;
  - **à obtenir** : définition statutaire de la base INSAF de l'INS (militaires, forces de
    sécurité intérieure, magistrats, douaniers) ; nombre de bénéficiaires et coût des départs
    de 2017-2021, 2018 et 2022-2028 (CNRPS, Cour des comptes, revues du FMI) ; budget de la
    mission « Affaires étrangères » et effectif diplomatique ;
  - **clés à créer ou à copier (bibliographe)** : `decret-gouv-2018-904-prime-rentree-universitaire`
    à copier de `education/references.json` dans `remunerations_publiques/references.json`
    (FR et AR) pour écrire la prime de rentrée universitaire ; décrets n° 2019-1129, 2020-550,
    91-1078, 85-1183, 2006-1245, 2023-592, 91-802, 76-843, 2025-459 ; rapport sur le budget
    actualisé 2012 ;
  - **figures** : `figures/emploi_public.py` titre et légende « fonction publique civile »,
    « agents civils » : à aligner sur le texte, qui ne dit plus le champ de l'INS limité aux
    civils ;
  - **taille** : le chapitre approche 20 000 mots ; chapitre propre pour « Recruter et faire
    partir » si le seuil de 25 000 est franchi (plan, § 9).
- **Les fonctions politiques — chapitre créé le 23 octobre 2026** (`_fonctions_politiques.qmd`,
  ajouté au `_quarto.yml` **français** seulement) : parlementaires (1960, 1979, 1989, 2005, ANC
  2012), gouverneurs (1973, 2020), membres du gouvernement, prélèvements. Écrit sans plan
  d'architecte (le plan des régimes spéciaux renvoyait ce plan à une passe séparée). Fiches
  `r-indemnite-parlementaire-decret`, `r-gouverneurs-decret-1991`,
  `r-remuneration-membres-gouvernement`. Restent :
  - **`_quarto.yml` arabe** : ajouter `_fonctions_politiques.qmd` après
    `_regime_statutaire_autonome.qmd` une fois la traduction livrée ;
  - **OCR ou lecture à l'image** : montants de l'indemnité parlementaire de 1967, 1972 et 1975
    (lois n° 67-56, 72-76 ou 72-78, 72-86, 75-80) ; décret n° 83-681 (exonération fiscale) ;
    antécédents des gouverneurs de 1957-1976 ;
  - **lisible dans le corpus** : arrêté du président de l'ANC du 15 août 2012 ; décret
    n° 2015-658 (intitulé arabe) ;
  - **à obtenir** : textes fixant l'indemnité des députés depuis 1989, de l'ARP et des
    assemblées de 2022-2024, la rémunération des membres du gouvernement (fiches ci-dessus) ;
    budget des missions « Assemblée » et « Présidence du gouvernement » ; article de TelQuel
    du 9 septembre 2016 (non lu, à ne pas citer) ;
  - **pour le livre « Retraites »** : LF 1988 art. 60-61 et loi n° 2005-55 (anciens présidents,
    Premiers ministres, présidents des chambres), LF 1989 art. 75-76, loi n° 2015-39.
- **Fiche `r-augmentations-ep-2013-2025`** : aucun décret des entreprises publiques n'a été
  établi par la passe du 23 octobre 2026 ; la fiche n'est pas modifiée (TODO du
  documentaliste, voir ci-dessus).
- **Présentation des trois chapitres courts — fait le 8 octobre 2026** (`_regime_statutaire_autonome`,
  `_regime_conventionnel`, `_regime_marche_controle`) : vue d'ensemble en tête, trame du volume
  conservée, section « Repères historiques » avec tableau des dates, registres repliés à colonne
  « Portée » ; `.domicile-unique` sur deux sections du chapitre statutaire (repris le 23 octobre 2026, voir plus haut) et sur
  `#sec-augmentations-ep` seulement. Restent :
  - **clés versées le 8 octobre 2026 (bibliographe)** : lois n° 70-46, n° 2009-47, n° 67-51 et
    n° 2001-65 ; décrets n° 97-2133, n° 97-2134, n° 78-885, n° 2014-12 et n° 2019-1132 ; les huit
    modificatifs du décret n° 79-96 ; arrêté d'agrément de 1975 et avenant n° 5 de 2022 de la
    convention des banques (`docs/notes/biblio-a-rapatrier.md`) ; les mentions du chapitre
    statutaire autonome et du chapitre du marché contrôlé portent l'appel de citation ; **reste**
    le texte arabe de l'arrêté de 1975 (fichier arabe du fascicule tronqué) — les décrets
    n° 2019-1132 et 2016-742 sont lus et cités au chapitre statutaire depuis le 23 octobre 2026
    (décret gouvernemental n° 2016-742 du
    10 mai 2016, JORT n° 50 du 21 juin 2016) ;
    les lois n° 70-46 et n° 2009-47 ont leur ligne de registre et leur lien depuis le 8 octobre 2026 ;
  - **transferts aux entreprises publiques (8,9 % et 7,5 % du PIB) — attribution corrigée le
    11 octobre 2026** : ces deux parts sont dans le Livre blanc de la Présidence du gouvernement
    de mars 2018 (p. 12), non dans la revue des dépenses publiques de la Banque mondiale, dont
    le texte ne les porte pas ; `_regime_conventionnel.qmd` les rend au Livre blanc
    (`pm-livre-blanc-ep-2018`, versé FR et AR), dit qu'il n'expose ni calcul ni base du PIB, et
    renvoie au volume « Les entreprises publiques » ;
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
  - magistrats : décrets n° 2026-65 et 2019-1132 lus et cités au régime statutaire autonome
    (23 octobre 2026) ;
  - poids budgétaire par cycle : aucun texte ne le donne.
- **Séries** : effectifs et masse salariale par régime ; dépenses de défense ; effectifs du
  secteur financier public. Régime statutaire autonome (plan, § 6) : F1 indemnité de magistrature
  1985-2028 ; F2 crédits de rémunération votés, missions Défense, Intérieur, Justice, 2011-2026 ;
  F3 dépense militaire du SIPRI ; F4 effectifs des forces armées (IISS, Banque mondiale) ; séries à
  verser dans `tunisia-data` ; effectif autorisé par mission 2021-2026 (tableau de l'introduction,
  `tbl-remu-effectifs-autorises`), figure à faire. Substituer des sources tunisiennes officielles aux chiffres du
  FMI et de la Banque mondiale.
- **Lecture immédiate des textes locaux** : le décret n° 2015-2217 est lu et rédigé
  (23 octobre 2026) ; les directeurs généraux des banques publiques en sont exclus et relèvent
  du décret n° 2015-968. Le Code des collectivités locales est lisible en arabe dans
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
  employeur/agent.
- **Travailleuses agricoles (décret-loi n° 2024-4) — lu et porté le 23 octobre 2026**
  (`docs/notes/cotisations-decret-loi-2024-4.md`, JORT n° 129 de 2024, deux éditions au corpus ;
  `todo-localisation.md`, qui le classe « absent du corpus », est périmé). Le décret-loi ne fixe
  ni taux ni assiette de cotisation : `#sec-cot-travailleuses-agricoles` le dit, avec les trois
  cas de prise en charge par l'État (art. 20, 23, 42), l'exemption de l'art. 3 et l'antécédent du
  décret n° 2019-379 ; `#sec-cot-at-travailleuses-agricoles` porte les risques professionnels
  (art. 38-42) ; la matrice `tbl-matrice-branches` est corrigée. Date d'effet : 24 octobre 2024
  (décret-loi n° 2020-1), reportée aux volumes cotisations, retraites et prestations sociales.
  Reste :
  - les décrets d'application (art. 19, 22, 33, 41) : fiches `r-dl2024-4-cotisations` et
    `r-dl2024-4-art33`, couvertes jusqu'au 2 octobre 2026 ; JORT n° 58 de 2026 à lire, jort_cache
    à rafraîchir ;
  - l'articulation avec le décret n° 2019-379 (RTFR) et avec la loi n° 81-6 : aucun article ne la
    règle ; l'application des trois ans à une activité antérieure à l'entrée en vigueur ;
  - folios des dernières pages (p. 2902 FR, 5297 AR) déduits, non lus à l'image ; décret
    gouvernemental n° 2020-724 (transport) non lu ; effectifs affiliés et dépenses du fonds non
    recherchés (budget du ministère des affaires sociales) ;
  - la note `cnss-autres-regimes.md` § 10 dit que les deux éditions concordent sur l'art. 28 :
    inexact (français « inférieure à 60 mois », arabe « n'excède pas 60 mois ») ; à corriger
    dans cette note.
- **Loi n° 65-17** (régime des étudiants, `1965/fr/Jo03465.pdf`, p. 787) : océrisée et lue
  à l'image le 23 octobre 2026 (`docs/notes/ocr-cibles-2026-10-23.md`) ; elle couvre les soins
  et les allocations familiales (art. 4 à 7). À reporter dans le chapitre ; numéro de fascicule
  à trancher (l'en-tête du PDF dit n° 32, la base n° 34).
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

1. **Prélèvements sur salaires autres que les cotisations** : taxe de formation professionnelle (TFP), contribution au FOPROLOS — assiette, taux, redevables, historique ; sans eux, le coin socio-fiscal des cotisations est incomplet. **Fait** : `cotisations_sociales/_prelevements_salaires.qmd` (5 octobre 2026) ; emploi du FOPROLOS au chapitre du logement social des « Prestations sociales » (23 octobre 2026, #506) ; lacunes à la rubrique « Cotisations sociales ».
2. **Salaire minimum et salaires négociés du secteur privé** : histoire du SMIG et du SMAG (montants, régimes 40 h / 48 h, revalorisations, décrets) ; conventions collectives sectorielles et leurs grilles ; accords salariaux périodiques UGTT-UTICA (privé) et UGTT-gouvernement (public). **Fait** : volume VIII « Marché du travail » (`_salaire_minimum.qmd`, `_conventions.qmd`, `_negociations.qmd`, annexe branche par branche) ; lacunes à la rubrique « Le marché du travail ».
3. Droit du travail déterminant les revenus : durée du travail, congés payés, heures supplémentaires, indemnités de licenciement, contrats précaires et sous-traitance, travail informel. **Fait pour l'essentiel** : `marche_travail/_rupture_contrat.qmd` (20 octobre 2026 : préavis, gratification, CDD, essai, licenciement économique, sous-traitance) et `_temps_travail.qmd` (22 octobre 2026 : durée, congés, heures supplémentaires) ; le travail informel n'a pas de section propre (mentions dans les notions et le temps de travail).
4. Politiques actives de l'emploi : programmes de l'ANETI (stages d'insertion, contrats aidés), primes à l'embauche, prises en charge de cotisations patronales ; protection contre la perte d'emploi (aujourd'hui effleurée). **Chapitre `marche_travail/_politiques_emploi.qmd`** ; la protection contre la perte d'emploi est traitée au chapitre de la rupture du contrat.
5. La compensation (Caisse générale de compensation : produits de base, carburants, électricité, transport) — **volume IX créé le 6 octobre 2026** (`precis/fr/compensation/`) ; lacunes à la rubrique « La compensation » ci-dessous.

**Fiscalité**

6. Droits d'enregistrement et de timbre ; fiscalité des mutations immobilières. **Mutations immobilières : chapitre `fiscalite/_patrimoine_immobilier.qmd`. Droit de timbre et droits d'enregistrement hors mutations : chapitre `fiscalite/_timbre_enregistrement.qmd` (`#sec-te`), rédigé le 23 octobre 2026** (mise en place depuis 1965, quatre réformes, état au 1^er^ janvier 2026, dix dispositifs, rendement 2001-2026, économie) ; lacunes dans la section « Fiscalité » ci-dessus.
7. Droits de douane. **Chapitre `fiscalite/_droits_douane.qmd` (`#sec-dd`), rédigé le 23 octobre 2026** (antécédents de 1955, tarifs de 1959 et 1973, réformes de 1987-1988, 1990, 1997, 2018 et 2022, état au 1^er^ janvier 2026, redevance de prestations douanières, droit compensateur provisoire, accords commerciaux, autres prélèvements, code de 2008, rendement 1986-2025, rapports extérieurs, évaluation Ayadi et al., économie) ; lacunes à la rubrique « Lacunes du chapitre droits de douane » ci-dessous.
8. Dépenses fiscales et régimes d'incitation (code d'incitation aux investissements, loi de 2016, entreprises totalement exportatrices, développement régional) — **chapitre créé le 6 octobre 2026, scindé le 11 octobre 2026** (`fiscalite/_regimes_incitation.qmd` et `fiscalite/_depenses_fiscales.qmd`) ; lacunes dans la section « Fiscalité » ci-dessus.
9. Fiscalité de l'épargne et du capital : retenues libératoires sur les revenus de capitaux mobiliers, plus-values mobilières, épargne exonérée. **Rédigée le 20 octobre 2026** comme section `#sec-irpp-epargne` du chapitre de l'IRPP (`fiscalite/_impot_revenu.qmd`), par décision du propriétaire ; lacunes dans la section « Fiscalité » ci-dessus.
10. Taxes affectées et contributions exceptionnelles (contribution conjoncturelle, contribution au budget de l'État de 2014, FODEC, vignette). **Rédigée le 23 octobre 2026** en deux chapitres de la fiscalité, `fiscalite/_contributions_conjoncturelles.qmd` et `fiscalite/_taxes_fonds_speciaux.qmd` ; la vignette n'est pas une taxe affectée et reste à loger dans le chapitre « timbre et enregistrement » (lacunes ci-dessous).

**Lacunes des chapitres « contributions conjoncturelles » et « taxes au profit des fonds spéciaux » (23 octobre 2026)**

Notes : `docs/notes/fiscalite-taxes-affectees.md` (documentation), `plan-fiscalite-taxes-affectees.md`, `eco-taxes-affectees.md`, `eco-contributions-conjoncturelles.md`.

- Contributions conjoncturelles :
  - encaissements de 2017, 2018-2019, 2024-2025 et 2025 : à obtenir (lois de règlement ; rapports d'exécution postérieurs à 2018 absents de `tunisia-data`) ; ceux de 2014 (186 MD) et 2015 (75 MD) sont lus ;
  - tableaux « A » des LF 2016, 2018 et 2020-2026, rubrique « contribution conjoncturelle » : à relever (éditions arabes à lire à l'image) ;
  - contexte des LFC 1991, LFC 2014, LF 2017, LF 2018 et LF 2025 (exposés des motifs, débats) : aucune source lue ;
  - antécédents 1959-1988 (défense nationale, reconductions de la contribution de solidarité, loi n° 85-89, inondations 1983, banques de dépôt 1988) : fascicules au corpus, OCR à demander ;
  - arrêté fixant les cinq mois de 1991 de la contribution des salariés (LFC 1991, art. 3) : à identifier ; décret n° 2012-472 (contribution volontaire de 2012) : intitulé seul, JORT n° 44 de 2012, p. 1334, au corpus ;
  - 2026 : recherche `r-contribution-conjoncturelle-2026` (aucune reconduction trouvée dans la LF 2026) ; fascicules 2026 inconnus de `jort_cache` à parcourir ;
  - population couverte par chaque épisode : aucune source ; montants en dinars constants : à faire ;
  - livre des caisses : la contribution de 1 % de 2019 au profit des caisses (LF 2019, art. 87-88, AR p. 5468, lisible) n'a pas de domicile ; abrogation (LF 2020, art. 39 § 5) à relire.
- Taxes au profit des fonds spéciaux :
  - rubriques des LF 1996, 2000 et 2003 : à lire à l'image ; LF 2003, art. 58-59 (taxe pour la protection de l'environnement) : chiffres à relire à l'image, extensions 2005-2018 et LF 2007, art. 60 (tourisme) à lire ;
  - décret n° 2000-634 (liste des produits du FODEC, lisible au corpus), décrets n° 99-2741, 2008-4111 ; décret n° 2012-435 (édition arabe seule, à l'image) ; décret n° 95-2495 (lisible, pp. 2363-2364) ;
  - textes de 1956, 1958 et 1984 que la taxe de 1995 remplace : OCR à demander ;
  - contexte de la LF 1995 (mise à niveau, accord d'association) : sources de l'époque à lire ;
  - tableaux « B » 2021-2026 ventilés par fonds : à lire à l'image ; réalisations par fonds : lois de règlement, à obtenir ;
  - série « Fonds spéciaux de Trésor » : colonne à créer dans `tunisia-data` (build `irpp`), puis figure par `figtools.series()` ; le tableau actuel est écrit à la main (TODO) ;
  - population couverte : aucune source ; dinars constants et part du PIB (base dite, annexe PIB) : à faire.
- Vignette (taxe de circulation) : recette du budget général ; chapitre « timbre et enregistrement » à lui donner une section (worktree `precis-wt-fiscalite-timbre-enregistrement`) ; décret du 31 mars 1955, art. 19-21, hors corpus (JOT 1955, à obtenir) ; arrêté du 27 mai 1955 ; tarifs 1964-1994 : OCR ; tarif des voitures de 2000 à 2021 non établi (LF 2016, art. 90 : lignes imprimées en tirets) ; LF 2024 (abandon des taxes 2020-2022 : numéro d'article à relever) ; réalisations : à obtenir.
- Fonds sans texte de financement lu (liste du tableau « B » de la LFC 2014, 32 comptes) : fonds de garantie des victimes des accidents de la circulation, de prévention des accidents, de la protection civile, FNAH, promotion des exportations, communications, huile d'olive conditionnée, qualité des dattes, repos biologique, création littéraire, sports et jeunesse, solidarité sociale, autoroutes, comptes des collectivités locales.
- Clés doublons : fondues le 23/10/2026 (correspondances dans `docs/notes/biblio-a-rapatrier.md`, § « Fusion des clés en doublon »). Rapatriement Zotero des clés versées (fiscalité, 23/10/2026) : sur feu vert.

**Lacunes du chapitre droits de douane (23 octobre 2026)**

Notes : `docs/notes/fiscalite-droits-douane-documentation.md` (textes), `fiscalite-droits-douane-chiffres.md` (chiffres), `fiscalite-droits-douane-plan-architecte.md` (plan), `eco-droits-douane.md` (économie), et leurs CSV. Relevés et figures : `precis/fr/fiscalite/douane/`, `figures/droits_douane.py`. Fiches de recherche : `r-douane-legislation-1955`, `r-douane-union-douaniere-protectorat`, `r-douane-tableaux-tarifs`, `r-douane-decrets-demantelement-ue`.

- **Lisible dans le corpus local** :
  - sections douanières des LF 1982, 1983, 1985, 1986 (LF 1971, 1977 et 1981 lues le 30/10/2026) (aménagements du tarif, habilitations, taxe de formalités douanières et son affectation de 40 % à la Caisse générale de compensation) ; clause d'effet de la LF 1984 ;
  - lois n° 61-41 et 62-68 (tarif de 1959) ; décrets n° 79-85 et 79-477 (nomenclature) ; décret n° 69-293 (accord CEE de 1969) et accord de coopération de 1976 ;
  - LF 1990 (suspensions), LF 1992 (art. 45-52, droit compensateur, tableaux « M », « P », « N »), LF 1995, 1996, 2000 à 2003 (bandes de taux de 1994 à 2004) ; minimum de perception après 1988 ;
  - LF 2010, art. 22 ; LF 2011, art. 11 ; LF 2012, art. 16-17 ; lecture complète des sections douanières des LF 2015 à 2017 et 2019 à 2026 ; annexes 2 et 3 de la LF 2016, 1 et 2 de la LF 2018, annexe 1 de la LF 2024 ; tableau de la LF 2019, art. 81 ; LF 2021 (suspensions) ; LF 2022, art. 31 (page), 58 et 70 ; LF 2023, art. 63 (friperie) ; LF 2024, art. 40 ; LF 2025, tableau du lait en poudre (rattachement à l'art. 40) ; pages des LF 2024, art. 44 et 66, et LF 2015, art. 41, à confirmer ;
  - loi n° 2006-72 : date d'effet (dépôt au gouvernorat de Tunis) ;
  - lois n° 98-106 et 99-9, décrets n° 93-695, 94-1745, 2000-477 (sauvegarde, pratiques déloyales) ; décrets de prélèvements agricoles à l'importation (90-1193, 91-1391, 93-1924, 93-2115, 95-1212) ; redevances compensatrices de 1958-1982 ; avis n° 33-2007 et 32-2008 du Conseil constitutionnel ; loi n° 2001-92 ; modificatifs du code de 2008 (LF 2017, art. 56-60 ; LF 2018, art. 31, 35-38 ; décret n° 2024-463) ; décret n° 94-1845 et modificatifs ;
  - lois arabes et d'adhésion connues par leurs intitulés (n° 81-41, 2007-11, 91-1, loi organique n° 2018-6, loi organique n° 2013-39) ; objet de l'amendement de 2025 à l'accord d'association (annexe de la loi organique n° 2025-21) ;
  - tableau A des LF 1970-2000 (prévisions des droits et de la redevance) ; rapports annuels de la BCT 1959-1985 (ligne « droits de douane » ; unité de 1972-1975 à établir).
- **Lues le 30 octobre 2026 : LF 1997, 1998 et 1999** (sections douanières en entier, texte français du corpus, versées aux registres du chapitre ; aucune table de taux dans ces trois lois). Restent : tableau « M » du droit de consommation de la LF 1998 (art. 47) et son rectificatif (JORT n° 13 du 13 février 1998, pp. 324-325) ; objet de l'art. 172 de l'ancien code des douanes, abrogé par la LF 1998, art. 65 (texte du code d'avant 2009 à lire) ; décret n° 99-1785 du 23 août 1999 (équipements ferroviaires, LF 1999, art. 36) et décrets pris sur les habilitations de 1997 à 1999 (intitulés seuls) ; tableau A des trois lois lu à l'image, valeurs en TODO du chapitre, non versées au relevé des rendements ; `_taxes_fonds_speciaux.qmd` ne porte pas la taxe sur les viandes de la LF 1997 (art. 41 et 42, fonds de développement de la compétitivité dans le secteur de l'agriculture et de la pêche) ; pages des LF 1999, art. 32, 33, 34 et 35 corrigées (2504, non 2503) : le paramètre de la redevance d'`openfisca-tunisia` cite encore p. 2503.
- **Lues le 30 octobre 2026 : LF 2013 et LF 2014** (textes français du corpus, JORT n° 1 de 2013 et n° 105 de 2013 ; articles douaniers en entier, versés aux registres du chapitre ; ni table de taux ni habilitation dans les deux lois). Restent : décrets de suspension ou de réduction n° 2012-3410 à 3412 (listes de positions) et n° 2014-2, 3 et 5 (intitulés seuls) ; décret n° 2013-929 (produits des n° 22.03 à 22.08, intitulé seul) ; domicile ailleurs : taxe pour la protection de l'environnement (LF 2013, art. 68-69 ; LF 2014, art. 71) au chapitre des taxes des fonds spéciaux, droit de consommation (LF 2014, art. 70) à son chapitre ; lien du fonds des dépenses spécifiques de la direction générale des douanes (LF 2014, art. 15) avec l'affectation de 10 % de la redevance.
- **Lues le 30 octobre 2026 : LF 1971, 1977 et 1981** (scans du corpus, OCR puis valeurs relues à l'image ; articles douaniers versés aux registres du chapitre : taxe de formalités douanières 1971, 1977, 1981 et redevance compensatrice de 1981, tarif, habilitation de 1981, taxation forfaitaire des petits envois). Restent : tableaux « G » (LF 1977, pp. 3187-3202) et « J » (LF 1981, pp. 3324-3360), non transcrits ; LF 1980 (loi n° 79-66) et lois de finances de 1974 à 1976, 1978 et 1979 ; décret n° 78-315 et compléments (taxe spéciale de compensation) ; décret d'application de l'assurance du transport à l'importation (LF 1981, art. 32) ; dates de publication des fascicules de décembre 1970 et 1980.
- **Lues le 30 octobre 2026 : lois de finances complémentaires 2012, 2013 et 2014** (loi n° 2012-1 et ses modificatives n° 2012-14 et 2012-25, loi n° 2013-51, loi n° 2014-54 ; texte français du corpus, articles en entier). Versés : LFC 2012, art. 19 (abandon des pénalités douanières et de change) et 53 (sacs à urines à 30 %) ; LFC 2014, art. 16 à 18 (espèces non justifiées, contrebande) et 47 (produits importés avant le 1er janvier 2014 ; taxe sur les moteurs usagés ramenée de 3 à 1 D) ; la LFC 2013 n'a aucune mesure douanière. Restent, domicile ailleurs : LFC 2012, art. 53 § 2 (taxe pour la protection de l'environnement) ; LFC 2014, art. 21, 22, 24, 32 à 34, 41 et 42 (TVA et droit de consommation) ; tableau A révisé des trois lois (droits de douane à l'importation, non versé au relevé des rendements). Clés ajoutées : `loi2012-14` et `loi2012-25` (à reporter en arabe).
- **Lues le 30 octobre 2026 : LF 1974, 1975, 1976, 1978, 1979 et 1980** (scans du corpus sans couche de texte ; OCR ciblé puis relecture à l'image). Versés aux registres du chapitre : LF 1975, art. 33 (franchise des ouvriers tunisiens revenus de l'étranger) ; LF 1979, art. 15 (production cinématographique) ; LF 1980, art. 18, 19, 22 à 24 et dispositions spéciales du tableau « G » ; décret n° 77-1114 (pommes de terre et bananes). LF 1974, 1976 et 1978 : aucun article douanier (LF 1976 : recherche par mots dans l'OCR, pages non relues à l'image). Restent : taux du tarif minimum par numéro du tableau « G » de la LF 1980 (pp. 3570-3622) ; lois modificatives de 1973 à 1977 et de 1980 ; décrets d'application ; tableau A de ces six lois (valeurs dans le TODO du chapitre, non versées au relevé des rendements). Clés ajoutées : `lf-1974`, `lf-1975`, `lf-1976`, `lf-1978`, `lf-1979`, `decret77-1114` (à reporter en arabe).
- **Lus le 30 octobre 2026 : décrets de suspension ou de réduction de 2013 et 2014** (texte français du corpus) : décrets n° 2014-2, 2014-3 et 2014-5 du 7 janvier 2014 (JORT n° 2, pp. 44-71, articles) et n° 2012-3410 du 31 décembre 2012 (art. 1 à 31), versés au registre des taux. Lus le 31 octobre 2026 : les annexes 1 et 2 du n° 2014-2 et du n° 2012-3410 (taux de 0, 7, 10, 15 et 27 %, chapitres 1 à 24 sauf 2, 16 et 20 ; annexe 2 de 21 positions à TVA de 12 %), les articles des décrets n° 2012-3411 et 3412 (lignes `r-dd-t-2013-divers` et `r-dd-t-2013-sante`). Restent : la transcription position par position des deux annexes 1 (environ 240 numéros chacune) ; décrets n° 2014-1 et 2014-4 ; décrets n° 2014-4512 à 4514 (JORT n° 105 de 2014) ; décret n° 2013-929 lu au chapitre du droit de consommation (tarifs des alcools). Clés ajoutées : `decret2014-2`, `decret2014-3`, `decret2014-5` (à reporter en arabe).
- **OCR à demander** : aucun indispensable ; un OCR des LF 1982-1986 éviterait la lecture page à page de la taxe de formalités douanières.
- **À obtenir** : *Journal officiel tunisien* de 1955 et textes douaniers du Protectorat, *Bulletin économique et social de la Tunisie* ; fascicules du tarif hors JORT (n° 59-5 de 1959, éditions de 1973 et 1989) et tarif consolidé au 1^er^ janvier 2026 (direction générale des douanes) ; fascicule annexé au JORT n° 49 de 1998 ; notice d'entrée en vigueur de l'accord d'association au JOCE (le 1^er^ mars 1998 n'est écrit qu'en TODO, d'après la page du SEAE) ; textes et dates d'entrée en vigueur des autres accords ; version consolidée du code des douanes ; contexte de 1987-1988, 1990, 1997, 2018 et 2022 (sources de l'époque) ; définition des régimes « général » et « off shore » de l'annuaire de l'INS ; importations 2024-2025 ; réalisations avant 2018 (Cour des comptes, lois de règlement) ; Jbili et Enders (1996), Havrylyshyn (1996) (`biblio-a-rapatrier.md`).
- **Tableaux à engendrer** : redevance, minimum de perception, tables de correspondance, bandes et registres des taux sont faits main ou imprimés depuis un relevé (`TODO (rédacteur)`) ; aucun nœud douane dans l'arbre des paramètres (voir `docs/notes/backlog-modele.md`).
- **Figures** : frise de tête `fig-dd-frise` ; `fig-dd-parts` marque 1988, 1997, 2016, 2018 et la nomenclature de 2020, non 1990 ni 2022 (plan : les cinq grandes réformes) — à trancher.
- **Autres chapitres** : `_contributions_conjoncturelles.qmd`, registre du prélèvement conjoncturel à l'importation (`#r-ccj-1991-importation`) : fin écrite le 24 octobre 2026 (LF 1992 art. 47, prorogation pour 1992 ; LF 1994 art. 71 et 74, incorporation aux droits de douane et abrogation, p. 2202) ; 1993 : prorogé par la LF 1993, art. 118 (déjà au chapitre des droits de douane), reporté au registre le 24 octobre 2026 ; `_depenses_fiscales.qmd`, TODO de la répartition par impôt : droits de douane relevés dans `fiscalite-droits-douane-chiffres.md`, § 8. `index.qmd` mis à jour (carte à sept impôts, renvois vers `@sec-dd`, `@fig-dd-parts`, `@sec-dd-etudes`) ; tableau de voisinage du livre à créer (prélèvements affectés à la Caisse générale de compensation → compensation ; agents des douanes → rémunérations publiques). `_quarto.yml` arabe : ajouter `_droits_douane.qmd` à la livraison de la traduction.
- **Bibliographie** : doublon `lf-1988` / `loi-87-83-lf-1988` (le chapitre cite le second, comme le relevé des tarifs) ; `.gitignore` racine de `tunisia-data` : ajouter `data/raw/droits-douane/`.

**Social et secteur public**

11. Régimes spéciaux du secteur public (militaires, forces de sécurité, magistrats, membres du gouvernement), recrutement, départs anticipés et plans de départ volontaire. **En cours (23 octobre 2026)** : chapitre statutaire autonome réorganisé (magistrats, militaires, forces de sécurité intérieure, douanes) ; section budgétaire refaite, corps particuliers et fiche « Recruter et faire partir » au régime indiciaire, chapitre `_fonctions_politiques` créé (23 octobre 2026) ; restent les figures F1-F4, les lacunes listées au § des rémunérations publiques et le `_quarto.yml` arabe.
12. Couverture santé au-delà de la CNAM : filières, ticket modérateur, mutuelles et assurance complémentaire de groupe — **volume X « La santé » commencé le 12 octobre 2026**, voir le chantier ci-dessous.
13. Logement social (FOPROLOS, programmes, prêts aidés), en lien avec le foncier. **Chapitre rédigé le 23 octobre 2026** dans `prestations_sociales/_logement_social.qmd` (`#sec-logement-social`), à titre provisoire : à migrer vers un livre « Le logement » (partie IV) quand il s'ouvrira ; ancres sans nom de livre (`sec-log-`, `r-log-`), seuls les liens entrants changeront de chemin (cotisations `#sec-cot-foprolos-affectation` et `#sec-cot-prelevements-rendement`, finances locales `#sec-fl-immeubles-fnah`, présentation du livre). Sources : note `docs/notes/logement-social-foprolos-2026-10-23.md`, plan `docs/notes/logement-social-plan-architecte.md`, fiche `docs/notes/eco-logement-social.md`. Fait : mise en place (1957-1977), cinq réformes (1986-1990, 2012, 2016, 2017, 2026), état du droit des prêts en 2026 (tableau fait main), résorption et FNAH, programme spécifique, premier logement, opérateurs et location-vente, régime de 1999, prévisions 2011-2020 et prélèvements 1987-1990 et 2011-2013, suivi du ministère des Finances 2009-2013, estimations d'une étude de 2014, « Ce qu'en dit l'économie » ; cotisations corrigées (premier prélèvement en 1987, prélèvements de 2011-2013 cités, renvois) ; lien depuis les finances locales ; les quinze modificatifs du décret n° 77-965 (1981-2015, dont les scans de 1977 à 2000 lus à l'image) et les décrets de l'AFH (n° 2021-327 et 2023-584) lus et versés, section « 1981-2015 : les prêts du fonds avant la refonte de 2016 », 2016 reclassé « étape — refonte du texte ». Restes :
    - **À trancher** : compter 2007 (public jusqu'à 4,5 SMIG, première aide à l'autofinancement) parmi les grandes réformes, et garder 2016 dans la liste (`tbl-log-reformes`) ; règle de date d'effet des textes postérieurs au 14 avril 2020 (décrets n° 2021-327 et 2023-584 datés du lendemain de la publication, comme le registre) ; tableau `tbl-log-prets-avant-2016` fait main (`TODO (rédacteur)`), à engendrer quand les paramètres antérieurs à 2016 seront versés ; deuxième et troisième tranches (art. 6 et 6 ter) détaillées au registre seulement.
    - **Lisible dans le corpus** : décret n° 2018-749 (fonds de garantie) ; LF 2005, art. 11-17, à harmoniser avec le volume des finances locales ; décrets n° 2007-534 et 2007-535 ; LF 2018, art. 61 ; DL n° 2022-79, art. 16 ; article final de la LF 2025 (date d'effet des art. 25 et 27).
    - **Texte à tester (décalage)** : arrêtés de prix de 2007 et 2009 ; LF 1994 (loi n° 93-125) ; tableaux des LF 1994-2010.
    - **OCR** : décret du 20 décembre 1956 et arrêté du 21 décembre 1956 (FNAH) ; décrets de gestion de 1956 et 1960 ; art. 11 et suivants du décret n° 74-224 ; suite du décret n° 74-33 (art. 13 et suivants) ; reste de la loi n° 58-47 ; lois et décrets de liquidation des sociétés HBM, HLM et de la caisse mutuelle de crédit immobilier (lois n° 58-82, 61-18, 61-29, décret-loi n° 61-7) ; annexe de l'arrêté du 2 mai 1987 pour le secteur privé ; tableaux « fonds spéciaux du Trésor » des LF de 1978 à 1993 (pages à localiser : fascicules de plus de cent pages). Océrisés et versés le 24 octobre 2026 : décret du 23 août 1956, lois n° 60-5, décret-loi n° 63-1, loi n° 66-75 (FNAH) ; lois n° 59-58, 61-57 et 58-47 (art. 1er) (SNIT) ; loi n° 73-24, décrets n° 74-223 et 74-224 (art. 1-10), loi n° 73-21, décret n° 74-33 (art. 1-12) ; loi n° 89-18 ; décret n° 77-926 (entier), n° 92-1818, loi n° 93-78 ; décret n° 87-709, arrêté du 2 mai 1987 (annexe, secteur public) ; arrêté du 5 janvier 1987 (prévisions de 1986). Aucun OCR de l'arabe (langue absente de tesseract).
    - **À obtenir** : convention de gestion du fonds avec la banque issue de la CNEL (la loi n° 89-18 autorise la transformation sans nommer la banque ; la dénomination « Banque de l'Habitat » reste à établir par un texte de la banque) ; réalisations du fonds hors 2009-2013 ; activité de la SNIT, de la SPROLS, de l'AFH, du programme de 1986, du programme spécifique et du premier logement ; budget du programme habitat avant 2026 ; ligne du fonds dans les lois de finances depuis 2021.
    - **Contexte des réformes** (mots de l'époque) : 1977, 1986-1990, 2012, 2016, 2017 (les rubriques des articles de prélèvement sont lues le 24 octobre 2026 ; la LF 2012 initiale est la loi n° 2011-7, JORT n° 1/2012, sans prélèvement ; le décret-loi n° 2011-55 ne touche pas l'ordonnateur du fonds et concerne le fonds de solidarité nationale, supprimé par la LF 2013, art. 12).
    - **Recherches** : les quatre fiches proposées au § 5 de la note sont versées au registre le 24 octobre 2026 (`r-foprolos-convention-gestion`, `r-foprolos-programme-emploi`, `r-psls-arretes-subvention-credit`, `r-foprolos-ligne-lf-2021`) avec leur ancre ; elles sont écrites par `recherches.charger` et `recherches.ecrire`, `scripts/recherches.py` n'ayant pas de sous-commande de création.
    - **Contribution de la loi n° 86-47** (10 % de l'impôt sur les BIC et l'IS, 1986-1988) : à placer dans les taxes affectées de la fiscalité (item 10) ; le chapitre la cite comme ressource du programme de 1986.
    - **Catalogue `tunisia-data`** du PDF des délibérations de l'ARP du 16 novembre 2025 (`arp-2025-11-16-equipement`), à créer par l'humain : ligne prête au § 3.4 de la note.
    - **Figure des prélèvements** (`fig-log-prelevements`, 25 octobre 2026) : lois de finances de 1987 à 2026 lues, série `log-prelevements-fonds` contrôlée par `scripts/verifier_prelevements_fonds.py` ; restent à établir si le fonds est compris dans les transferts globaux de 2004, 2007, 2008 et 2013 (lois de règlement, comptes spéciaux du Trésor), les lois de finances pour 2023 à 2025 dans l'édition française, les lois de finances complémentaires de 1986 et antérieures, et l'effet de l'article 92 de la loi de finances pour 1987 sur les recettes du fonds de 1987 à 1994 (montants versés au budget).
    - **Figure F1** des prévisions et prélèvements : verser la série dans `tunisia-data` avec sa fiche de provenance ; colonnes en dinars constants : faites le 24 octobre 2026 pour les prévisions, les prélèvements, les prêts accordés, la subvention de 2012, 1977 et le premier logement ; reste le tableau des ressources et emplois du ministère (`TODO (rédacteur)`). Lus le 24 octobre 2026 et versés au registre : décrets n° 2017-391, 2019-39 (premier logement), 2013-3289, 2014-4251 et 2015-460 (programme spécifique).
    - **Tableau engendré** des prêts du fonds (`tbl-log-etat-2026`) : paramètres proposés dans `backlog-modele.md`.
    - **Présentation du livre** : tableau de voisinage (§ 4 des conventions) à créer ; forme « monétaire : prêt » retenue pour les prêts dans `tbl-prest-naissances`, à confirmer.
    - **`_quarto.yml` arabe** : ajouter `_logement_social.qmd` quand la traduction sera livrée.
    - **Points à trancher par le propriétaire** (plan § 9) : 2016 rupture ou étape ; 2023 étape ou rupture ; 2011-2013 rattachés à 1987 (retenu) ou à 2012 ; 2017 compté comme réforme.
14. Transferts en nature et aides à l'éducation (bourses, cantines, allocation de rentrée scolaire, handicap).

**Transversal**

15. Synthèse de la redistribution par décile (impôts, cotisations, prestations, subventions), dans l'esprit des études d'incidence de type CEQ (dépôt `ceq-tunisie`).

## La santé — volume X, première rédaction le 12 octobre 2026

`precis/fr/sante/` est un livre nouveau, distinct des « Prestations sociales ». Sa présentation
pose la question des **transferts non monétaires de santé** (publics couverts, prestations
effectivement financées, financeurs, dépense des ménages) ; son premier chapitre
`_couverture.qmd` suit les protections antérieures à 1960, les assurances sociales,
l'assistance médicale, l'assurance maladie de base, les trois modalités de soins et leur
participation financière, puis délimite les couvertures complémentaires. Deux chapitres
nouveaux du 12 octobre, `_hopital.qmd` et `_medecine_ville.qmd`, exposent respectivement
l'échelle des structures publiques, le fonctionnement et les ressources des établissements
publics de santé, les composantes de la rémunération du corps médical des hôpitaux dans
les textes de 1989, puis le conventionnement et le paiement des médecins libéraux. La
fiche de lecture commune est `sante-hopital-ville-lectures-2026-10-12.md`. Les prestations
en espèces de maladie et de maternité restent dans leur volume d'origine ; ses registres
et tableaux des taux et plafonds restent accessibles par renvoi, sans déplacement à ce stade.

**Premières séries de dépense intégrées le 12 octobre** : dépenses du département
« Santé publique » en 2018-2023, gestion et développement, d'après les tableaux
16.8 et 16.10 de deux annuaires INS (source ministère des Finances, PDF locaux
lisibles en couche texte), aussi rapportées aux dépenses de gestion et de
développement de l'État et au PIB nominal INS en base 2015 (2018-2023, non
rétropolé) ; charges techniques et administratives de la CNAM et prestations
décaissées en 2016-2021, d'après ses états financiers, avec distinction entre
charges du compte de résultat et sorties de trésorerie ; les rapports annexés
aux PLF 2020 et 2021 servent de recoupement, prévisions écartées. Comptes de la santé OMS
2018-2023 (dépense courante, financeurs public, privé et extérieur, parts de
la dépense publique et du PIB citées telles que publiées par l'OMS), et
paiements directs des ménages en part des dépenses courantes de santé et en
montant moyen par habitant en dollars courants et en dinars courants (conversion
indicative au taux de change officiel annuel Banque mondiale/FMI), puis en
**dinars de 2025** (IPC annuel de la BCT, base 2015, indice 2025 de 186,3).
Les onglets « Données » des figures budgétaires et des tableaux OMS affichent
les dénominateurs budgétaires et le PIB, ainsi que les taux de change et les
indices employés dans les calculs ; aucune
observation OMS des paiements directs de l'année 2025 n'est disponible. Les familles figurent dans des sections
distinctes, avec leurs unités, financeurs et limites. Calculs,
localisations et réponses des API : `sante-depenses-sources-2026-10-12.md`.
La part dite « ressources extérieures » suit l'**origine étrangère des
transferts à la santé**, qu'ils passent par l'État ou par d'autres circuits ;
la fiche d'indicateur OMS relayée par la Banque mondiale en donne la définition.
Leur ventilation par bailleur, programme et forme de financement reste à
obtenir avant d'expliquer le point haut de 2022.
Les PDF des annuaires étaient déjà catalogués dans `tunisia-data` ; l'API OMS
est accessible en texte. Aucun montant n'est présenté comme un reste à charge
en dinars pour un ménage donné.

**Carte de lecture des chiffres ajoutée à la présentation** : trois plans
explicités avant les séries — dépense courante de santé par financeur (OMS),
comptes du département Santé et de la CNAM, postes partiels de soins suivis
par la caisse —, en **deux schémas distincts et lisibles à la largeur de la page**
(financeurs OMS ; circuits et écritures tunisiens), réalisés en HTML/CSS avec
équivalent textuel dans le livre PDF, puis distinction des charges comptabilisées et des prestations
décaissées. Les paiements directs sont inclus dans le financement privé OMS ;
le budget ministériel inclut le développement hors dépense courante ; la
facturation à la caisse peut être une recette hospitalière, jamais une somme à
ajouter à la charge de la caisse. Des renvois partent de cette carte vers les
figures et tableaux et reviennent des chapitres Couverture et Hôpital. **L'année commune
2021** illustre les quatre niveaux (ministère, CNAM, facturation publique,
paiements directs), sans en additionner les montants ni traiter la part OMS
comme la part d'un compte national tunisien. La ventilation
comptable exhaustive des charges CNAM et la consolidation budgétaire restent
à établir ; les chiffres publiés ne sont pas additionnés en un total inventé.

**Postes de soins de la CNAM identifiés dans sa statistique 2007-2021** :
facturation des hospitalisations et consultations externes dans les EPS et
hôpitaux régionaux, et deux rubriques des cliniques privées (chirurgie,
accouchements). Tableaux en onglets au chapitre Hôpital, sans assimilation au
budget complet des EPS ni à l'ensemble des charges techniques de la caisse.
La fiche `sante-cnam-comptes-2026-10-12.md` donne les montants en milliers et
millions de dinars et le recoupement entre éditions. Les états financiers et
statistiques de prestations sont lisibles en couche texte dans le corpus,
sans OCR. Les comptes 2011-2015, document scanné, ont été **lus à l'image le 15 octobre
2026** (pp. 3 et 4, identités imprimées vérifiées pour les cinq années) et versés dans
`tunisia-data` (série `cnam-comptes-2011-2021`, transcription
`sources/transcriptions/cnam-etats-financiers-2011-2015.csv`) ; la figure
`#fig-sante-cnam-comptes` couvre désormais 2011-2021. Aucune année commune entre
l'édition 2011-2015 et la suivante : la jonction 2015-2016 n'est pas recoupée, et la
baisse des décaissements de 2015 à 2016 reste à expliquer par les notes aux états
financiers, **à obtenir**.
**À lire ou obtenir** pour ventiler la dépense totale : soins ambulatoires,
médicaments, soins dentaires, accidents du travail, indemnités en espèces,
part versée par la caisse aux prestataires et restes à payer, à périmètre
comptable constant.

**Ventilation par régime, lue sans image dans une étude** : *La Lettre du
CRES* n° 8 (Belloussaief, 2023), figure 1 p. 1, donne les parts annuelles de
l'assurance maladie, des assurances sociales et des AT/MP dans les dépenses
CNAM de 2009 à 2019, d'après la CNAM avec calcul de l'auteure. L'étude est
archivée dans `tunisia-data` ; sa méthode n'est pas détaillée. En 2019, le
montant AT/MP de l'étude rapporté aux charges techniques des comptes CNAM
redonne sa part publiée à l'arrondi ; cela ne valide ni les autres années ni
une ventilation exacte en dinars. Présentation **dans une section d'étude
distincte** des montants comptables et du budget, en figure longitudinale
avec valeurs au survol et séries complètes dans les onglets, note
`sante-cnam-comptes-2026-10-12.md`. Les états primaires
ventilés par régime et par prestation restent à obtenir pour reconstituer
les montants exacts ; les chiffres en pourcentage ne sont pas convertis en
montants prétendument observés.

**Trois figures longitudinales dans la présentation** : budget Santé
2018-2023 (vues en MD et en parts du budget et du PIB), comptes CNAM 2011-2021
(compte de résultat puis trésorerie séparés) et parts des trois régimes du
CRES 2009-2019 (étude distincte). Les tableaux de synthèse ont été remplacés
par des courbes à valeurs au survol, sans perdre les données détaillées ou
les sources. Extraction rejouable dans `tunisia-data`,
`scripts/extract_sante_depenses.py` ; trois séries au catalogue et snapshots
`precis/_seriescache/` pour le rendu autonome. L'extracteur rattache les
cinq années de PIB imprimées à leurs années, distinctes des trois années
budgétaires de chaque édition, et retient la révision du PIB 2020 de
l'annuaire le plus récent ; sans ce contrôle l'extraction aurait produit une
part du PIB erronée.

**Résultats du système de santé, 12 octobre** : l'indice OMS des services
essentiels (ODD 3.8.1, série annuelle 2000-2023, échelle 0-100 et quatorze
traceurs) et la difficulté financière due aux paiements directs (ODD 3.8.2,
définition révisée en 2025, six enquêtes 1995-2021) ont chacun leur section,
leur série datée, leur méthode et leurs réserves dans `_couverture.qmd`.
L'indice des services essentiels est montré en figure à survol, avec données
annuelles et provenance en onglets : extraction de la réponse OMS conservée
dans `tunisia-data`, série `oms-couverture-services-tunisie-2000-2023`, puis
snapshot pour le site autonome.
L'ancienne série au seuil de 10 % du budget total du ménage ne se raccorde
pas au seuil de 40 % du budget discrétionnaire. Les valeurs et les fiches OMS
sont lisibles en texte ; aucun OCR demandé. Les documents récurrents à suivre
et les années effectivement disponibles sont inventoriés dans
`sante-indicateurs-sources-2026-10-12.md`. **À lire** : composantes de l'indice
de couverture, tableaux régionaux INS sur les structures et professionnels,
RAP/PAP Santé, rapports de contrôle de la Cour et enquêtes INS 2015/2021 sur
la dépense médicale et les remboursements, avant d'attribuer un changement
observé à une réforme précise ou de le décliner par région.

**Autres angles documentés sur une source CNAM en texte** : répartition des
personnes comptées dans les trois modalités de soins (2008-2021, changement de
définition des affiliés en 2019 ; étudiants et salariés à faibles revenus à part)
et nombre de généralistes et spécialistes conventionnés (2007-2021). Le
chapitre Couverture sépare vue courte, données annuelles et sources ; celui de
la Médecine de ville montre les deux séries sur une figure à **30 infobulles**,
avec les années et les pages dans l'onglet Données, et la provenance dans
l'onglet Sources. La série est extraite dans `tunisia-data` et snapshotée pour
le rendu autonome du précis. Le document local, déjà catalogué dans `tunisia-data`,
est détaillé dans `sante-cnam-filiere-medecins-2026-10-12.md`. **À obtenir** :
consultations réalisées par filière, répartition territoriale des praticiens,
nombre de bénéficiaires après 2013 (2008-2013 publiés par la *Lettre du CRES* n° 5,
`#fig-soins-beneficiaires-cnam`), remboursements par type
de soin et leurs séries postérieures à 2021. Le nombre de conventionnés ne
mesure ni les soins réalisés ni les revenus des médecins.

- **Lisible au corpus** : loi n° 59-45, art. 1 (JORT n° 22 de 1959, p. 368), loi n° 60-30,
  loi n° 87-29, loi n° 2004-71, décrets n° 2007-1366 et 2007-1367, arrêté du 3 juin 2008,
  décret n° 2021-318. Les protections d'entreprise et la prévoyance publique avant 1956
  sont connues par Lucien Bertrand (1953, deux articles lus et récupérés) ; la loi de 1959
  confirme la continuité du régime public de 1951. L'arrêté mutualiste de 1961 a son visa
  lu à l'image, non ses garanties ; le décret de 1954 est connu par ce visa seulement.
- **Relecture à l'image** : décrets n° 2007-1367 et 2021-318 et arrêté du 3 juin 2008,
  repris de leur couche texte ; clause finale de 2021 à confirmer ; révisions postérieures
  des plafonds à chercher. L'arrêté du 25 juin 2007 sur les affections lourdes reste à lire.
- **Hôpital et ville, lus à l'image** : loi n° 91-63 (JORT n° 55 de 1991, pp. 1390-1393),
  décret n° 91-1844 (n° 86 de 1991, pp. 2009-2011), décrets n° 89-296, 89-298 et 89-299
  (n° 17 de 1989, pp. 382-384), arrêté du 6 février 2007 et convention des médecins de
  libre pratique (n° 13 de 2007, pp. 385, 387, 389-397, 400-404, 406). Fascicules
  français présents localement mais **sans couche texte** pour 1989 et 1991 ; les pages
  utiles ont été lues sur les images. La convention de 2007 a une couche texte absente
  pour les pages utiles ; les articles cités ont été lus à l'image. URL FR et AR des
  quatre fascicules vérifiées (`206 application/pdf` le 12 octobre). La lecture décrit
  ces états datés, **pas un état actuel reconstitué** des statuts, primes ou honoraires.
- **Infirmiers, lu à l'image** : décret n° 2000-1690, JORT français n° 59 du 25 juillet
  2000, pp. 1778-1779 pour les art. 1-4, 8 et 11 ; fascicule local lisible à l'image,
  grades et niveaux de rémunération décrits sans valeur isolée. L'URL du JORT arabe
  est `Ja05900.pdf` (vérifiée) et non `Ja0592000.pdf` (404) ; pagination arabe à relever.
- **À lire pour les personnels** : statut hospitalo-universitaire (décret n° 77-732),
  hospitalo-sanitaire (n° 2008-3449) et statuts propres des sages-femmes,
  pharmaciens et personnels techniques ; chaîne des majorations de traitement,
  de la prime de rendement, de non-clientèle et des gardes ; modificatifs du statut
  des infirmiers (2011, 2015, 2024). Les fascicules de 1977 et 2008 sont à vérifier
  au corpus avant reprise ; aucun montant actuel n'est imprimé.
- **À lire pour la ville** : avenants n° 1 à 7 (2007-2012) et suites de la convention
  des médecins, leurs annexes d'honoraires et dates d'effet ; le texte de 2007 renvoie
  les modalités pratiques du parcours de médecin de famille à un avenant, sans en établir
  la mise en œuvre effective. Les fascicules JORT sont repérés par titre dans
  `jort_cache.db` ; leur présence au corpus et leur lisibilité restent à vérifier.
- **À obtenir ou documenter** : textes et statuts déterminant les garanties des mutuelles,
  contrats d'assurance complémentaire de groupe, effectifs et dépenses propres ; comptes
  CNAM, budgets et exécutions hospitaliers, série de l'assistance. Pour le budget
  ministériel, confronter les annuaires INS aux rapports de clôture de la Cour des
  comptes et aux PAP/RAP afin d'établir le stade comptable et les transferts.
  Pour les ménages, lire la méthode des enquêtes INS 2015 et 2021, notamment le
  traitement des remboursements, avant de rapprocher leurs dépenses médicales
  en dinars des paiements directs de l'OMS. Ces deux PDF d'enquête ont une couche
  texte lisible et ont été récupérés temporairement, sans valeurs reprises au
  volume. Aucun état actuel des plafonds ni incidence distributive chiffrée
  n'est publié faute de série établie.
  **Plafond ambulatoire :** le RAP 2021 des Affaires sociales mentionne un
  arrêté du 8 février 2021 modifiant celui du 3 juin 2008 ; `jort_cache.db`
  le localise au JORT n° 14 du 9 février 2021, p. 412. Le fichier local et les
  deux éditions servies sur `pist.tn` sous le numéro 14 contiennent en réalité
  le **numéro 13 du 5 février 2021** (vérifié sur la première page, en texte,
  le 13 octobre 2026). Le numéro 15 est bien le 15. **À obtenir** : le vrai n° 14,
  puis lecture des valeurs et de leur date d'effet ; ne pas traiter les métadonnées
  comme le texte de l'arrêté.
- **Couverture avant 2004, écrite le 14 octobre 2026** (chapitre `_histoire.qmd`, `#sec-soins-histoire`,
  placé en tête du livre et ordonné par périodes le même jour ; `_couverture.qmd`, `#sec-soins-base`, `#sec-soins-assistance` ; note `sante-couverture-avant-2004-2026-10-14.md`).
  Fait : régime de prévoyance de 1951 d'après le *Bulletin économique et social de la Tunisie*
  (Bertrand, n° 71 et 72 ; rubrique « Législation » du n° 52 de 1951) ; réforme de 1972-1973
  (loi n° 72-2, décret n° 73-91, arrêtés du 12 mars 1973, décret n° 74-899) ; assistance
  médicale de 1958 à 1986 (lois n° 58-67, 60-13, 69-2, 81-12, décret n° 69-399, LF 1983
  art. 105, LF 1986 art. 56) ; extensions de la sécurité sociale du secteur privé 1965-2002 ;
  loi n° 91-63 (art. 35-36, 63) et décrets de 1998 ; commission de 1996 (décret n° 96-1018).
  Lus à l'image au corpus (OCR des pages utiles) ; trois fiches nouvelles dans
  `docs/recherches.yml` (`r-sante-prevoyance-1951-texte`, `r-sante-admission-1939`,
  `r-sante-am-preparation-1996-2004`).
  - **À obtenir, hors corpus** : texte du décret du 12 avril 1951 et de ses arrêtés
    (17 juillet 1951, 23 juillet 1952, 10 octobre 1952) ; décret du 23 décembre 1939 sur
    l'admission des malades ; document du IXe Plan (1997-2001) ; décision gouvernementale de
    1996 sur l'assurance maladie, si elle existe.
  - **Lisible au corpus, à lire** : arrêtés d'application de la loi n° 81-12 (livrets, liste
    des longues maladies) ; décrets n° 57-39 et 62-350 (contribution de 1962) — les décrets
    n° 93-529 et 94-1738 sont repris le 15 octobre 2026 (voir ci-dessous) ; texte de la convention de 1973 (forfait annuel, décret n° 74-899) ; branche
    soins du décret n° 95-1166. Les dates d'effet des lois n° 81-6 et du décret n° 82-1360
    sont reprises des notes de leurs clés, non relues ; le tableau des extensions ne date
    donc que par année.
  - **Pages arabes à relever** : art. 105 de la LF 1983 ; titres arabes des lois n° 60-13,
    85-109 et des décrets n° 69-399, 74-899, au fascicule.
  - **Dinars constants** : les plafonds et contributions de 1951-1986 (`#tbl-soins-prevoyance`,
    `#tbl-soins-contributions`) attendent un indice des prix sourcé sur la période.
  - **Fait le 14 octobre 2026, volumes des prestations et des caisses** : la puce « dualité de
    1987 » de `#sec-nc-aide-medicale` est corrigée (1958, 1981, 1987), avec un renvoi à l'histoire
    du volume santé ; `#sec-caisses-cnr-cps` dit le rôle de la Caisse de prévoyance sociale dans
    l'option de 1972-1973 (carnet de soins, convention à forfait annuel).
  - **Fait le 15 octobre 2026, volume des cotisations** : `#sec-cot-pensionnes` donne les valeurs
    des textes avant 2007 — 0,50 % de la pension sous le régime de 1951, 2 % au 1er avril 1973
    (décret n° 73-91, art. 15), retenus par décision de l'auteur ; la série du modèle reste à
    étendre (backlog-modele.md). **À demander** à la relectrice spécialiste : ce qui s'est
    appliqué en pratique de 1973 à 2007 (les rapports de la Banque mondiale de 1993 et 2006
    donnent 1 %, sans texte).
- **Régimes des caisses avant 2004, écrit le 15 octobre 2026** (branche
  `chantier/sante-regimes-avant-2004`, non commité ; note `sante-regimes-avant-2004-2026-10-14.md`).
  - Fait, `_histoire.qmd` : convention CNSS - Santé publique de 1961 et règlement intérieur
    de 1965 (période 1958-1969) ; loi n° 70-34 et décret n° 74-796, CNRPS de 1976, ascendants
    de 1979, soins thermaux et tarifs des actes de 1982 (période retitrée « 1970-1986 »,
    ancre inchangée) ; facultatif de 1988 (colonne ajoutée à `#tbl-soins-prevoyance`, barème
    `#tbl-soins-facultatif-1988`), tarifs de 1993 et contributions de 1994
    (`#tbl-soins-assures-hopital`), régime conventionnel de 1996-1997, enfants à charge de
    1997 ; section nouvelle `#sec-soins-histoire-caisses` (état de 2004, `#tbl-soins-caisses-2004`)
    et sous-section des rapports de la Banque mondiale `#sec-soins-histoire-bm` ; six lignes
    ajoutées à `#tbl-soins-histoire`.
  - Fait, `_couverture.qmd` : `#sec-soins-complementaires` rédigée (contrat de groupe, statuts
    mutualistes de 1961 et 1984, régime conventionnel, médecine du travail), registre
    `r-soins-…`, sous-section `#sec-soins-complementaires-etudes` (Banque mondiale 2006 et 2008,
    thèse de 2015 ; le « 6 à 15 % » n'est repris nulle part).
  - Quatre fiches nouvelles dans `docs/recherches.yml` : `r-cnrps-cotisation-retraites-1973-2007`,
    `r-cnss-polycliniques-fondation`, `r-caisses-soins-lourds-etranger`,
    `r-assurance-groupe-mutuelles-taux`. La passe proposée par la note pour
    `r-sante-am-preparation-1996-2004` (Banque mondiale 2006, p. 62, note 45) reste à verser.
  - **À verser (bibliographe)** : arrêté du 30 mars 1991 (soins thermaux, cité dans la ligne de
    1982 faute de clé) ; lois des mutuelles de corps (n° 77-80, 82-68, 82-69, 89-53, 96-30),
    décret n° 85-847, arrêté du 7 septembre 1993 (Union nationale des sociétés mutualistes) ;
    rectificatif de 1965 au règlement intérieur de la CNSS.
  - **Lisible au corpus, à lire ou à confirmer à l'image** : loi n° 60-30, art. 5 ; règlement intérieur, art. 102-109 ; arrêtés du 30 mars 1991 et du
    17 septembre 1984 ; code des assurances, art. 31-32 ; décrets n° 76-3 et 89-1890
    (organisation de la CNRPS, OCR inexploitable) ; arrêté du 2 avril 1979 (longue maladie) ;
    décret n° 91-487.
  - **À établir** : contenu des statuts types de 1961 et des statuts approuvés (garanties,
    cotisations), séries d'adhérents et de dépenses des mutuelles et des contrats de groupe ;
    taux et plafonds du facultatif après 1988 (le tableau de 2004 renvoie au barème de 1988) ;
    sort du régime conventionnel de 1996-1997 après 2004 ; série du forfait
    annuel des caisses au ministère de la Santé (lois de finances) ; dinars constants des
    plafonds de 1988 et des tarifs de 1993-1994.
  - **À obtenir, hors corpus** : Ladhari (1996, *Recueil de sécurité sociale*) et Essoussi
    (1994, ENA-CERA), notices corrigées le 16 octobre 2026 d'après leurs couvertures, ouvrages
    non consultés (bibliothèque du CRES) ; décret du 18 février 1954.
  - Fait le 16 octobre 2026 (`_histoire.qmd`, `#sec-soins-histoire-1951`) : régimes du personnel
    de l'électricité, du gaz et des transports — retraite et capital-décès (décret du 26 août 1948,
    connu par la loi n° 98-37, art. 1), prévoyance obligatoire (décret du 13 décembre 1951 :
    chirurgie, longue maladie, décès, d'après le *Bulletin économique et social de la Tunisie*
    n° 60, p. 9 et 119), transfert à la CNRPS en 1998. Le « régime de prévoyance de 1948 »
    signalé en relecture est le régime de retraite de 1948. **À obtenir** : texte de la convention
    approuvée le 14 décembre 1951 (J.O.T. du 18 décembre 1951), hors corpus ; fiche
    `r-sante-prevoyance-egt-1951`.
  - **Questions ouvertes à trancher** : ascendants après la loi n° 97-60 (exposé tel quel, sans
    conclusion) ; report de l'ancre `r-cnrps-cotisation-retraites-1973-2007` dans
    `cotisations_sociales/_regimes.qmd` (`#sec-cot-pensionnes`).
- **Séries et études sur l'assurance maladie, écrit le 15 octobre 2026** (branche
  `chantier/sante-series-etudes`, non commité ; note `sante-series-etudes-2026-10-15.md`).
  Toutes les sources sont des PDF à couche texte, lus dans `tunisia-data` (`cres/`,
  `sante-etudes/`, `sante-avant-2004/`) ; aucun OCR demandé.
  - Fait, `_couverture.qmd` : `#sec-sante-cnam-etude` complétée (dépenses CNAM par secteur
    2007 et 2012, *Lettre du CRES* n° 5, recoupement de 2012 avec les états financiers et
    la part maladie du CRES n° 8) ; sous-section `#sec-soins-beneficiaires-cnam`
    (`#tbl-soins-beneficiaires-cnam`, bénéficiaires 2008-2013, et écart des filières de 2013 :
    66,4 % selon la Lettre contre 62,1 % calculé sur la CNAM, sans arbitrage) ; section
    `#sec-soins-comptes-nationaux` (financement de 2004 d'après la RTBC n° 19 ; comptes de la
    santé 2012-2014, `#tbl-soins-comptes-nationaux`, en MD courants et de 2025 ; ratios au PIB
    seulement cités ; tableau 4 de Ben Abdelaziz cité avec son écart de 140 à 350 MD) ;
    section d'études `#sec-soins-etudes-reforme` (thèse de 2015, coefficients en bloc replié ;
    article EMHJ 2022).
  - Trois fiches nouvelles dans `docs/recherches.yml` : `r-sante-conseil-national-am-rapports`
    (passe JORT du 15 octobre : le décret n° 2005-2192, art. 7, prévoit un rapport annuel
    transmis au Premier ministre, sans publication), `r-sante-cnam-rapports-activite`,
    `r-sante-comptes-sante-2012-2014`.
  - Fait le 15 octobre 2026 : `#fig-soins-beneficiaires-cnam`, figure à deux panneaux
    (bénéficiaires 2008-2013 selon le CRES, affiliés 2008-2021 selon la CNAM, chacun avec son
    axe, ruptures de 2010 et 2019 marquées), qui remplace le tableau fait main
    `#tbl-soins-beneficiaires-cnam` ; séries `cnam-beneficiaires-cres-2008-2013` et
    `cnam-affilies-filieres-2008-2021` versées dans `tunisia-data` (PR #68), lues dans les PDF
    à couche texte, la première contrôlée à l'image. Le tableau `#tbl-soins-effectifs-filieres`
    est engendré depuis la seconde série (`depenses_sante.tableau_filieres`), avec des
    chiffres identiques à ceux de l'ancien tableau fait main. Les trois filières du décret
    n° 2007-1367 (art. 2) sont au glossaire, termes arabes lus dans l'édition arabe.
  - **À obtenir (documentaliste)** : rapports du Conseil national de l'assurance maladie
    (2008-2014), rapports d'activité de la CNAM 2007-2014, rapports des comptes de la santé
    2012-2014 ; comptes nationaux de la santé 2004-2005 de l'INSP (Arfa, Souiden, Achour,
    2007) pour confronter les parts de 2004 ; parts 2000-2017 tirées directement de la base
    de l'OMS pour relier 2004, 2012-2014 et 2018-2023 dans une seule méthode (TODO dans
    `#sec-soins-comptes-nationaux`).
  - **Non repris, à juger** : couverture de la population en 2016 (note CRES/UNICEF 2019,
    p. 14 : clé versée, non citée ; les parts publiées ne somment pas à 100 %) ; dépenses CNAM
    par secteur 2007-2010 de la thèse (relais aux totaux incohérents) ; actes ATDSRP 2017.
- **Tarifs des malades payants et tarifs réduits de 1998, écrit le 23 octobre 2026** (branche
  `rediger/sante-chantier-2`, non fusionnée ; note `sante-tarifs-malades-payants-2026-10-23.md`).
  Le décret n° 98-409 fixe les tarifs réduits en pourcentage des tarifs de l'arrêté du
  19 décembre 1996, non en dinars : la case « montants de 1998 » du tableau
  `#tbl-soins-assures-hopital` est remplie par calcul (colonnes 1996 et 1998 ajoutées, formules et
  arrondi de l'art. 22 sous le tableau). **Depuis le 23 octobre 2026, les quatre tableaux de tarifs
  sont engendrés** (`scripts/generate_sante_tables.py`, français seul) et recoupent le fait main,
  sauf la colonne 1998 des consultations de `#tbl-soins-assures-hopital` : pourcentage et ligne nommée
  par l'art. 17, sans montant (1,500 ; 2 ; 3 ; 4,500 D retirés), et la colonne 1996 des consultations
  de l'hôpital régional et de l'établissement universitaire (« 10 ou 14 selon le praticien ») ;
  TODO (documentaliste) dans `_histoire.qmd`, constat dans `backlog-modele.md`. Lus : arrêtés du 19 décembre 1996 (couche texte ; dépôt
  du 30 décembre 1996 lu à l'image, exécutoire le 4 janvier 1997 ; édition arabe lue à l'image,
  pp. 2855-2856), du 17 avril 1998, du 29 janvier 2003 (couche texte décalée de 29 points de code)
  et du 7 juillet 2008 ; arrêté du 25 janvier 1993 lu à l'image (JORT n° 10, pp. 201-202).
  Section nouvelle `#sec-hopital-tarifs-malades-payants` (`_hopital.qmd`, tableaux
  `#tbl-hopital-tarifs-malades-payants`, `#tbl-hopital-lettres-cles`, `#tbl-hopital-forfaits-actes`),
  ligne `#r-hist-1996-tarifs` à `_histoire.qmd`, cinq clés `arrete-…-tarifs` (FR et AR), deux notions
  au glossaire (`malade-payant`, `lettre-cle`), fiche `r-sante-tarifs-malades-payants-apres-2008`
  (cinq arrêtés dans `jort_cache`, aucun après 2008).
  - **À confirmer** : arrondi par excès de l'art. 22 et ligne « maître de conférence » de l'art. 17
    (un texte ou une circulaire d'application) ; dates d'effet des arrêtés de 1993, 1998, 2003 et
    2008 (dépôt des fascicules : 1993 sans mention imprimée, les trois autres non relevés) ; sort des
    forfaits de scanner de 1996 face aux lettres clés S de 2008.
  - **À obtenir** : tarifs de consultation et d'hospitalisation en vigueur après 2008 (aucun arrêté
    identifié ; 5 337 notices de `jort_cache` n'ont qu'un intitulé arabe) ; nomenclature du 25 septembre
    1990 et du 1er juin 2006 (coefficients des actes, hors corpus lu) ; tarifs réduits de 2008
    à 2026 (les modifications du décret n° 98-409 de 1999 à 2021 portent sur les cartes, non sur les
    montants, d'après le volume des prestations sociales) ; dinars constants des tarifs de 1993 à 1998.
  - **Hors périmètre** : numérotation des sections de `sante/` (`check_numerotation.py` : `index.qmd:1`,
    `_histoire.qmd:211`, `_couverture.qmd:102` et `:334`, sections à une seule sous-section), échec
    antérieur à ce chantier.
- **Intégration bilingue** : `_quarto.yml` et `references.json` tenus dans les deux langues ;
  les références arabes de 1987 à 2021 demandent page et, pour celles dont elle manque,
  URL vérifiée ; les URL arabes des fascicules de 1989, 1991 et de la convention de 2007
  ont été vérifiées, mais leurs pages restent à relever. Aucun `.qmd`
  arabe n'est écrit avant la livraison de la traduction ; ajouter alors `index.qmd` et
  les trois chapitres au `_quarto.yml` arabe. Le sommaire général arabe reste à actualiser
  lors de cette livraison. Le futur travail sur l'éducation suivra la même question des
  services et transferts non monétaires ; son livre et ses textes restent à documenter.

## L'éducation et la formation — volume XII, première rédaction le 17 octobre 2026

Première version en français seulement : présentation, histoire, enseignement scolaire, formation professionnelle
initiale, enseignement supérieur, aides aux élèves et aux étudiants, dépense (`precis/fr/education/`). Plan et décisions : `education-plan-2026-10-17.md` (Q1 à Q11, une seule ouverte).
Notes documentaires : `education-histoire`, `education-aides-scolaires`, `education-aides-universitaires`,
`education-depense` (2026-10-17) et leurs fiches `education-recherches-{A,B,C,D}.yml` (fusionnées dans
`recherches.yml`).

- [ ] **Textes lus le 18 octobre 2026 (chapitres 2 et 4), à relire à la revue** : décret n° 96-682 (1996), arrêtés du
  3 avril 2013, du 29 juillet 2019 (deux, édition arabe seule), du 28 avril 2021 et du 30 avril 1994 (trois), arrêtés
  conjoints de 2004 et 2008 sur la contribution aux frais d'examen, arrêté du 9 mai 2008 (commissions des établissements
  privés), décret n° 2008-29 ; loi n° 2008-19 lue en entier ; décrets n° 2012-1232, 2013-1469, 2017-1196 et
  n° 2008-2716 (art. 1 à 23). Lectures du second passage : décret n° 2004-2437 (vie scolaire, à l'image), décret n° 2009-2139 (classification des qualifications), décrets n° 94-1600, 2007-4147 et clause d'abrogation du décret gouvernemental n° 2016-620 (formation professionnelle). Lectures versées dans `education-scolaire`, `education-superieur` et `education-formation-professionnelle`. Troisième passage (branche `chantier/education-v2`) : arrêtés sur les jardins d'enfants (1974, 2001, 2003, 2022), décret n° 2012-827, arrêté de 2014 sur les commissions des établissements privés, série des tarifs de pension et de demi-pension (huit arrêtés de 1967 à 2022, chapitre des aides). Quatrième passage (branche `chantier/education-v3`) : arrêtés de 1956 et 1957 dans la série des tarifs de pension (le fascicule de 1957 récupéré sur pist.tn), art. 60 du décret-loi n° 2021-21, décret n° 2008-2716 en entier, décrets n° 2011-683, 2006-1936 et 2002-2103. Les pages des
  arrêtés de 1994, 2004, 2013 et 2021 de l'index `jort_cache.db` sont décalées d'une page ; le fascicule n° 68 de 2004
  et le n° 86 de 2004 ont une couche de texte décalée (police), le second sans texte après la p. 2955.
- [ ] **Règle de rédaction (18 octobre 2026)** : le texte rendu ne dit plus les incertitudes (« traduction de travail »,
  « seul l'intitulé est connu ici ») ; elles sont des TODO. Les lignes de tableau sans contenu établi ont été retirées
  des chapitres 2, 3, 4, 5 et de l'histoire ; leur liste est dans un TODO de fin de chapitre, à relire pour les
  rétablir. À aligner avec `AGENTS.md`, qui cite encore la formule « seul l'intitulé de ce texte est connu ici ».
- [ ] **Arabophone** : faire relire les traductions de l'arabe (Constitution de 2022, décret-loi n° 2024-2, lois de
  finances 2024 et 2026, arrêtés du 29 juillet 2019, décret gouvernemental n° 2019-656).
- [ ] **Chapitres non commencés** : résultats (scolarisation, examens, abandon) et rapports et études (chap. 7 et 8
  du plan) ; ils attendent les séries du ministère de l'Éducation (taux de scolarisation par âge, abandon) et les
  rapports à obtenir ; « Ce qu'en dit l'économie » par dispositif ; version arabe.
- [ ] **Q8, collectivités : instruite pour les communes le 23 octobre 2026 ; reste les conseils régionaux.**
  Section `#sec-educ-depense-collectivites` du chapitre de la dépense, note `education-collectivites-2026-10-23`.
  Lus : décret gouvernemental n° 2020-52 et son modèle annexé (JORT n° 9 de 2020, édition arabe, pp. 368-397),
  décret n° 2020-439 (ne touche que le principal de la dette), fichiers par commune de la DGCT. Constat : un article
  de dépenses d'interventions dans l'enseignement et la formation (03.303, mêlé à la contribution au centre de
  formation et d'appui à la décentralisation), les revenus des jardins d'enfants (4101, 4201), aucune rubrique pour la
  construction ni l'entretien des écoles ; budgets par article publiés pour 2022 et 2023 seulement (2018-2021 : par
  grande section). Reste : nomenclature des budgets des conseils régionaux (arrêté du 31 mars 2008), nomenclature
  communale antérieure à 2020 (arrêtés de 1975 et de 2008), décret n° 2004-1182 (centre de formation), destination
  des tickets-repas de l'article 3304 (13,8 MD en 2022) ; plein texte du corpus non parcouru. Fiche
  `r-educ-collectivites-depense-education` ouverte. Figure `fig-educ-communes` (parts des articles 3303 et 4101 dans les
  budgets, 2022-2023) engendrée par `figures/fig_educ_communes_donnees.py` depuis les fichiers bruts de la DGCT ; les séries par
  article sont encore à verser au catalogue de `tunisia-data`. Série 2018-2021 impossible : fichiers sans identifiant d'article. Le TODO du livre des finances locales sur l'annexe du décret n° 2020-52
  (`_budgets.qmd`, section de la nomenclature) est en partie levé : le modèle est lu, le contenu des articles 6101
  et 8002 reste à lire ; `decret-gouv2020-439` est dans les références de ce livre (contrôle du 25 octobre 2026).
- [ ] **Textes à lire à l'image** : § 9 du plan, points 2 et 3 (fascicules d'avant 1990 de l'histoire, décrets de
  répartition des crédits, budgets citoyens 2014-2018). Ticket proposé au § 9, à ouvrir par l'humain.
- [ ] **§ 9, point 1 (aides universitaires), lu à l'image le 29 octobre 2026** (branche `educ/textes-aides`, note
  `education-aides-universitaires` § 2.9) : arrêtés de montants de 1958, 1959, 1962, 1963 (deux), 1964, 1965, 1969,
  15 novembre 1971, 1974 et 1978 ; décret n° 63-2 ; décret n° 72-51 ; arrêtés du 28 février 1990 et du 7 avril 1992 ;
  décret n° 80-1001 ; p. 1449 du règlement de 1974 ; avis du Conseil constitutionnel n° D-L 02-2006 (statut des
  offices, ancienne Q7). Versés au chapitre 5 (tableaux du montant, des niveaux, du prêt, de l'étranger et du
  renouvellement ; registres de la bourse et des œuvres). Corrections faites au rendu : engagement de servir dix
  ans et concours sur titres dès 1963 (et non 1971) ; premier prêt chiffré en 1988-1989 (et non 1989-1990). À la
  revue : la baisse de 30 D (premier cycle, 1969) à 25 D (taux général, octobre 1971), corrigée le 18 novembre 1971.
  Restent :
  - arrêté du 20 août 1982 : non retrouvé dans l'édition française de 1982 (sommaires n° 59 à 83 lus à l'image ;
    n° 84 par l'index) ; reste l'édition arabe de 1982 (corpus) et 1983-1987 ; montant en Tunisie non établi entre
    1977 et 1988 ;
  - année universitaire 1960-1961 : les décrets n° 58-189, 59-212, 61-421 et 62-312 (lus le 29 octobre 2026, note
    § 2.9 e ; ligne « attribution sans concours » au registre) écartent le concours pour 1958-1959, 1959-1960,
    1961-1962 et 1962-1963 ; aucun texte pour 1960-1961 (sommaires page 1 des n° 30 à 56 de 1960 lus) ; restent
    les suites de sommaire en page 2, les n° 57 de 1960 à juin 1961 et l'édition arabe (corpus) ; fiche
    `r-bourse-sans-concours-1960` proposée dans la note (§ 9), à inscrire si le texte rendu en parle ;
  - à la revue : le décret n° 85-173 (lu, note § 2.9 e) ne change que le rang du directeur de l'ONOU ; non versé
    au registre des œuvres (ni montant, ni niveau, ni condition) ;
  - décisions de majoration de 1958-1959 et arrêtés du 5 février 1962 (études à l'étranger), visés en 1963 : absents
    de l'index, à chercher ;
  - arrêtés de bourses des écoles du ministère de l'Agriculture (1972, 1973, 1975, 1980) : au corpus ; celui de 1972
    est lu (35 D et 30 D).
- [ ] **Classement des réformes** (rupture, étape) : classement provisoire, avec l'autre lecture écrite
  (2002, 2017, 2008 en formation initiale). LMD = rupture ; 1989 = étape (décision du 17 octobre 2026) ; à
  confirmer à la revue.
- [ ] **Références** : une quinzaine de textes connus par leur seul intitulé n'ont pas de clé
  (`docs/notes/biblio-a-rapatrier.md`, « Clôture du 17/10/2026 ») ; `budget-mesrs-2013-gbo` désigne le fichier
  non-GBO (clé **conservée**, décision de l'inbox du 17 octobre 2026 : citée dans le chapitre et dans une figure, et déjà dans
  Zotero) ; `loi-2009-32-restauration-formation` est au fonds commun en français et, depuis le 25 octobre 2026, en arabe
  (déplacée depuis `precis/ar/fiscalite/references.json`) ; double clé de la loi de finances pour 2019.
- [ ] **Séries** : les 79 relevés de `education-depense-series/` sont au catalogue de `tunisia-data` (onze séries
  `education-*`, 29 octobre 2026) et les figures de la dépense lisent `figtools.series()`. Les réponses de l'API de la
  Banque mondiale (UIS) et le communiqué de l'INS sont retéléchargés dans `data/raw/` de `tunisia-data` (30 octobre 2026) ;
  figure des effectifs F2 (`fig-educ-eleves`, `figures/fig_educ_eleves.py`, 29 octobre 2026) et figure des boursiers F3
  (`fig-educ-boursiers`, `figures/fig_educ_boursiers.py`, série `education-boursiers-bourse-nationale`, 30 octobre 2026) faites.
- [ ] **Recherche exclue de la dépense** (décision du 17 octobre 2026) : fondue dans l'enseignement supérieur en
  gestion en 2002-2004 et depuis 2019 ; réserve de périmètre dite dans le texte, pas d'estimation ; la
  fiche de plan § 4 et la note `education-depense` § 2.4 comptent encore la recherche dans le périmètre et
  sont à mettre à jour.
- [ ] **Coût par élève** : aucun publié (Q9) ; établir la source documentaire des trois coûts moyens de l'exercice
  d'incidence de 2021 avant toute valeur.
- [ ] **Renvois des livres voisins** : « Rémunérations publiques » ne traite aucun corps enseignant, ni la prime de
  rentrée universitaire ; « Caisses » ne dit rien du prêt universitaire des caisses ; « Prestations sociales » :
  figure des boursiers (Q4) et histoire de l'aide de rentrée avant 2020 ; « Entreprises publiques » : une ligne
  de renvoi vers les offices ; « Fiscalité » : exonérations de l'enseignement privé (Q6).
  « Le marché du travail » : la section `sec-mt-pe-fonds-formation` ne traite pas la formation continue des
  salariés, que le chapitre de la formation professionnelle initiale de l'éducation lui renvoie (décision Q1) :
  lacune à combler dans `marche_travail/_politiques_emploi.qmd`.
- [ ] **Infobulles** : une vingtaine de liens du chapitre d'histoire vers les registres du chapitre scolaire
  (`./_scolaire.html#r-educ-h-…`) n'affichent pas l'infobulle de la ligne (elle ne marche que dans la même
  page) ; le lien ouvre bien la ligne. Limite connue du domicile unique entre fichiers.
- [ ] **Chapitres suivants** : scolaire, formation professionnelle initiale, supérieur, résultats (scolarisation,
  examens, abandon), rapports et études ; « Ce qu'en dit l'économie » par dispositif ; version arabe.
- [x] **Chapitre « L'enseignement scolaire » réordonné par parcours de l'élève (30 octobre 2026, branche
  `educ/reorg-scolaire`)** : état du droit, préscolaire, cycles et langues (section neuve `#sec-educ-scolaire-cycles-langues`),
  examens et orientation (sous-section neuve `#sec-educ-scolaire-pilotes`), passages et abandons, privé, cours particuliers et
  vie scolaire, textes. Identifiants et lignes de registre conservés. Reste : le fil historique des langues d'enseignement
  (1958-1995), à placer dans la section neuve quand les textes de 1973 à 1995 seront lus (PR #608).

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

**État au 10 octobre 2026, version 0.129 du modèle** (borne `VERSION_MINIMALE` relevée à 0.129,
publiée le 10 octobre 2026) : trois branches, sept grilles, dont cinq tracées — textile horaire
(7 lignes × 21 colonnes, 147 cases) et mensuelle (18 × 21, 378) ; bâtiment, personnel occasionnel
(9 lignes, puis 10 depuis 2008 ; 11 cases en tout) et personnel administratif et technique
(19 × 11, 209) ; assurances, grilles de 1993 à 2021 (22 × 14, 308) — et deux sans courbe, aux
assurances : grilles de 1975 à 1992 (`salaire_base_avant_1993`, 22 × 12, 264 cases, 6 dates,
motif « antérieure ») et grille n° 1 du 1er juin 1990 (`salaire_base_avant_1993_grille_1_de_1990`,
22 × 12, 264 cases, 1 date, motif « peu de dates »). Soit 1 581 cases, 30 935 valeurs et
**193 cases vides** (illisibles sur le fascicule : 127 dans la grille mensuelle du textile, 16
dans la grille mensuelle du bâtiment, 1 dans les assurances de 1993 à 2021, 49 dans les
assurances de 1975 à 1992). Ces comptes sont ceux de `cc_index.yml`. L'index ne liste
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
  un lien par ligne (`liens_grille`) — 18, 19 et 22 liens, et 22 pour chacune des deux grilles
  des assurances antérieures à 1993 (264 cases) —, rendus en une ligne sous la figure.

Ce qui lui manque :

- **assurances, grilles antérieures au 1er juin 1993 — versées le 10 octobre 2026** (modèle
  0.129, PR n° 490) : section `#sec-mt-cc-annexe-assurances-avant-1993` de l'annexe, sans
  courbe, mentionnées par `cc.autres_grilles` avec leur période et un lien par ligne (22 liens
  par grille, 44 adresses). Restent : **aucune grille entre le 1er janvier 1975 et le 1er janvier
  1983** et le **protocole d'accord du 8 juin 1984** relatif à l'augmentation des salaires, que
  vise l'avenant n° 1 — restent à obtenir (documentaliste ; présence au corpus non vérifiée ; TODO dans l'annexe, sans fiche de `docs/recherches.yml` : aucune recherche
  n'a été menée) ; la série change d'entreprises entre le 1er janvier 1989 (avenant n° 1) et le
  1er juin 1990 (grille n° 2), ce que l'annexe dit sans le mesurer ; deux cases à réserve
  (échelle 16, échelon 12, de 1990 à 1992 : éditions divergentes ; échelle 4, échelon 9, 1975 :
  rectificatif de 1976) ne sont dites que dans la base législative ; le libellé des deux
  grilles vient des `short_label` du modèle, inégaux (« Salaire de base avant le 1er juin
  1993 » ne dit pas « hors indemnité complémentaire provisoire », l'autre le dit ; « 1er » sans
  exposant) — à harmoniser en amont ; le tableau `@tbl-mt-cc-grilles-hors-series` du chapitre
  ne donne que le textile et le bâtiment : l'annexe y renvoie pour eux, et le chapitre peut
  renvoyer à l'annexe pour les assurances ; `index.qmd` du volume dit encore que l'annexe suit
  le bas et le haut « de chaque grille » ; `cc.forme_grille` (une seule date ; dernière forme
  d'une grille sans courbe) n'a pas de test — le module `figures/conventions.py` n'en a aucun ;
- **les 193 cases vides** : à relire sur un meilleur exemplaire des fascicules — textile mensuel,
  grilles de 1994 (1 case), 1999 (42), 2000 (30), 2002, 2003 et 2004 (18 chacune, l'échelon 18
  des dix-huit lignes) ; bâtiment mensuel, grilles de 1996 (7), 1998 (5), 2001, 2002, 2003 et
  2004 (1 chacune) ; assurances, grille de 1996 (1), grilles de 1983 (1) et de 1989 (48, télécopie dégradée que
  reproduisent les deux éditions). Le compte de l'annexe est calculé : il
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
  comme l'en-tête arabe de la quatrième colonne du tableau d'ouverture (« دون منحنى، تواريخ
  المفعول », posé le 10 octobre 2026), l'intitulé arabe du renvoi (`INTRO_BASE` de `figures/conventions.py`,
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
  Établi le 20 octobre 2026 pour la **loi n° 66-27 : 1er mai 1966**, date énoncée par l'art. 1 de
  la loi de promulgation (JORT n° 20 de 1966, p. 716, lu à l'image), à reporter aux registres
  `#r-mt-sm-1966-duree` et `#r-mt-inst-1966-duree`. Établi aussi pour la **loi n° 96-62 : 31 juillet 1996** (dépôt du JORT n° 59 le 26 juillet
  1996, mention de la dernière page, p. 1599, lue à l'image ; loi n° 93-64, art. 2), à reporter à
  `#r-mt-sm-1996-duree` et `#r-mt-sm-1996-134` (note `marche-travail-temps-de-travail.md`, § 13,
  Q1).
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
- **Rupture du contrat de travail — chapitre rédigé le 20 octobre 2026**
  (`_rupture_contrat.qmd`, `#sec-mt-rupture-contrat`, entre `_negociations.qmd` et
  `_politiques_emploi.qmd` au `_quarto.yml` français ; note `docs/notes/marche-travail-rupture-contrat.md`,
  plan `docs/notes/marche-travail-rupture-contrat-plan-architecte.md`, fiche économique
  `docs/notes/eco-rupture-contrat-travail.md`). Chapitre entier `.domicile-unique`, 48 lignes de
  registre ; figures `fig-mt-rc-temporaires` (OIT, points par enquête) et
  `fig-mt-rc-licenciements-economiques` (Banque mondiale 2004) ; figure `fig-mt-rc-contrats-ins`
  engendré depuis la série de l'INS (snapshots du 20 octobre 2026). Restent :
  - *arabe* : ajouter `_rupture_contrat.qmd` à `precis/ar/marche_travail/_quarto.yml` (entre
    `_negociations.qmd` et `_politiques_emploi.qmd`) à la livraison de la traduction ;
  - *tableaux* : `tbl-mt-rc-parametres` est engendré (22/10/2026, versement de la 0.138 ; la
    colonne de 1973 et les cases sans paramètre sont écrites dans
    `scripts/generate_marche_travail_tables.py`) ; son en-tête porte le 24 mai 2025 et le texte
    du chapitre le 28 tant que la PR « Dates d'effet depuis le décret-loi n° 2020-1 » (#482)
    n'est pas fusionnée ; `tbl-mt-rc-etat-du-droit` est engendré depuis le 23/10/2026
    (`mt_rc_etat_du_droit` : préavis, dommages-intérêts, plafond et vice de procédure lus ;
    condition, débiteur, population et articles écrits dans le script). Reste, après la
    publication de la 0.143 : lire la période d'essai de la convention cadre et le délai de
    notification de la rupture (colonne de 1973 et cases « inchangée » de `tbl-mt-rc-parametres`,
    case de la fin d'essai de `tbl-mt-rc-etat-du-droit`) ;
  - *rémunérations publiques* : décret n° 2025-327 (sous-traitance interdite dans le secteur
    public, effet au 22 juin 2025 ; édition arabe seule au corpus, éd. française 404) à exposer
    dans « Les rémunérations dans le secteur public » (décision D6), puis renvoi depuis
    `#sec-mt-rc-sous-traitance` ;
  - *à obtenir* : JORT n° 32/2020 (décret-loi n° 2020-2, connu par iort ; 404 sur pist.tn) ;
    étude BIT de 2019 sur un fonds perte d'emploi (403) ; série des licenciements économiques de
    l'inspection du travail après 2001 ; décrets du Protectorat de 1940, 1943, 1944, 1950
    (*Journal officiel tunisien*, OCR) ; dossier ARP du projet de loi n° 16/2025 et débats de 1994,
    1996, 2025 (contexte des réformes, Q2) ;
  - *à lire* : conventions de branche — préavis, indemnité de licenciement, départ à la retraite,
    diviseur du « jour de salaire » (Q4, Q11 ; scans de `tunisia-data`, lecture à l'image) ;
    loi n° 70-20 (texte local illisible, OCR à refaire, Q8) ; sort de la loi n° 58-139 (Q9) ;
    code des obligations et contrats (Q14) ; rectificatif de la loi n° 92-81 et pied de page du
    JORT n° 52/1992, à relire à l'image (Q6) ;
  - *zones franches* : la loi n° 2001-76 (art. 1er, JORT n° 58/2001, p. 1752, exécutoire le
    26 juillet 2001) renomme les zones « parcs d'activités économiques » ; le sort du contrat à
    durée déterminée présumé (art. 23 de la loi n° 92-81) de 2001 à 2025 est à lire (reste de la
    loi n° 2001-76, textes postérieurs sur les parcs) ; dénomination arabe non lue (édition arabe
    du JORT n° 58/2001 à couche texte encodée, lecture à l'image) ;
  - *glossaire* : « cause réelle et sérieuse », « priorité de réembauchage » et « zone franche
    économique » ancrées le 20 octobre 2026 ; « délai-congé » est un synonyme de `preavis` ;
    restent les notions économiques du § 7 de la fiche économique (protection de l'emploi,
    marché du travail dual…).
- **Temps de travail et congés — chapitre rédigé le 20 octobre 2026** (`_temps_travail.qmd`,
  branche `chantier/temps-de-travail`, déclaré au `_quarto.yml` français après
  `_negociations.qmd`). **Restent** :
  - *arabe* : à la livraison de la traduction, ajouter `_temps_travail.qmd` à la main au
    `_quarto.yml` arabe, après `_negociations.qmd` et avant `_rupture_contrat.qmd` ;
  - *dates du chapitre de la rupture* : corrigées par la PR « Correctifs de dates de la rupture du contrat
    (loi n° 2025-9 au 24 mai 2025, art. 117) » (#482), non fusionnée à la rédaction de cette ligne ;
  - *références* : Chemin et Wasmer 2009 (fiche `eco-temps-de-travail.md`) sans clé ni PDF, non
    citée par la section « Ce qu'en dit l'économie » ;
  - *date dérivée* : loi n° 2021-37 au 30 janvier 2022 (six mois après la publication du
    30 juillet 2021, art. 29), à confirmer ;
  - *textes non identifiés*, fiches versées à `docs/recherches.yml` le 20 octobre 2026 avec leurs
    ancres : `r-mt-duree-40h-decrets`, `r-mt-art107-jours-feries`,
    `r-mt-art121-cotisations-conges`, `r-mt-protectorat-duree-conges` ;
  - *questions ouvertes de la note* (§ 13) : Q4 (jour de la loi n° 91-15, « mars 1991 » écrit),
    Q7 (avenants : non-signataires ; « 7 novembre » depuis 2011), Q9 (contexte d'époque des
    réformes de 1973, 1996 et 2021), Q10 (art. 11 et 28 et clause d'effet de la convention cadre
    agricole), Q11 (textile, art. 22 à 28 sur un meilleur exemplaire, articles exacts du jour
    férié travaillé et du congé de naissance), Q13 (limite de 9 heures par jour après 1996),
    Q14 (art. 94-3 à 94-14 ; article de la loi n° 2025-9 qui récrit l'art. 94-2), Q15 (qui paie
    les sept jours de paternité), Q16 (effectifs de la colonne « population couverte ») ;
  - *séries* : la section des données ne trace que l'INS (trois trimestres de 2019, tableau 6,
    p. 5) ; snapshot `ins-emploi-duree-travail-2019` tiré d'une série de `tunisia-data` non
    encore committée sur `main` ;
  - *tableaux* : paramètres, état du droit, congé et jours fériés sont engendrés (22/10/2026,
    versement de la 0.139) par `scripts/generate_marche_travail_tables.py` ; restent écrits dans
    ce script, faute de paramètre : traitement pendant le congé (convention cadre, art. 30),
    ligne de 1964 des jours fériés (loi n° 63-55, avant la première date de la série), âge
    apprécié, « Population couverte », travail domestique (TODO documentaliste au chapitre).
    Les tableaux `tbl-mt-tt-conventions`, `tbl-mt-tt-conges-familiaux` et `tbl-mt-tt-domestique`
    restent faits main. Après la publication de la 0.144 (travail domestique) : engendrer la
    ligne « Travail domestique » de `tbl-mt-tt-etat-du-droit`, `tbl-mt-tt-domestique` et la
    colonne du travail domestique de `tbl-mt-tt-conges-familiaux` ;
  - *pages* : art. 113, 114, 116 et 119 nouveaux de la loi n° 96-62 à la p. 1584 (corrigé au
    registre) ; art. 2 de l'avenant n° 2 à la p. 229 ; entrée en vigueur de la convention cadre
    au 1er juin 1973 confirmée par l'art. 52, p. 859. La note
    `docs/notes/marche-travail-temps-de-travail.md` est corrigée de même.
- **Temps de travail et congés — matière rassemblée le 20 octobre 2026, avant rédaction** (branche
  `chantier/temps-de-travail`, note `docs/notes/marche-travail-temps-de-travail.md`) : plan
  proposé, paramètres datés (durée, heures supplémentaires, congé annuel, jours fériés, congés
  familiaux et de paternité), antécédents du Protectorat, conventions cadre et textile, séries
  INS et OIT, notions à glossaire, références à créer. Établi et lu à l'image : code de 1966
  (art. 1 et 4 de la loi de promulgation, art. 79 à 124, art. 445), rectificatifs n° 27 et 37 de
  1966, lois n° 63-55, 88-55, 91-15, décret de 1957, décret n° 60-189, convention cadre de 1973
  (art. 24-36) et ses avenants n° 1 (1984), n° 2 (1992) et n° 3 (2004), convention du textile de
  1974 (art. 22-28) ; couche texte : loi n° 96-62, décrets-lois n° 2011-51 et
  2021-11 ; à l'image : décrets-lois n° 2020-1 et 2020-2 (ce dernier touche les art. 92 et 117 :
  récupération en six mois, congé annuel accordé par l'employeur pendant le confinement), lois n° 2021-37 (travail domestique), 2024-44 et 2025-9, convention cadre agricole de
  2015 (édition arabe). **Restent** :
  - *règle de date d'effet depuis le 14 avril 2020* : le décret-loi n° 2020-1 (JORT n° 32 de
    2020, p. 767) rend les textes exécutoires « le lendemain de leur publication dans l'édition
    électronique » et de leur dépôt électronique, « contrairement aux dispositions de la loi
    n° 93-64 ». **Tranché par le propriétaire le 20 octobre 2026** : depuis le 14 avril 2020, le
    lendemain de la publication électronique ; avant, la loi n° 93-64. Reste à l'écrire dans
    `AGENTS.md` (« Dater ») et à reporter aux dates calculées depuis 2020 des autres volumes ;
  - *date de publication de la loi n° 91-15* (JORT n° 17, numéro double « 1er et 5 mars
    1991 », aucune mention de dépôt) ; la loi n° 96-62 est datée du 31 juillet 1996 (§ 13, Q1 ;
    la première version de la note la disait sans date, à tort) ; *avenants de la convention cadre* : date à partir de laquelle ils obligent les
    non-signataires, et application depuis 2011 du « 7 novembre » de la liste de neuf jours
    fériés de l'avenant n° 2 ;
  - *textes non identifiés* (fiches versées le 20 octobre 2026, voir l'entrée du chapitre
    rédigé) : décrets de l'art. 80 (40 heures par branche, 1966-1996) ; arrêté de l'art. 107
    nouveau (jours fériés) ; arrêté de l'art. 121 (cotisations de congés payés à la CNSS) ;
    textes du Protectorat (décret du 4 août 1936 — « 14 août » dans la loi de 1966 —, décrets du
    25 juillet 1946, du 9 mars 1944, du 20 avril 1921), à obtenir (*Journal officiel tunisien*,
    Gallica inaccessible en accès automatisé) ;
  - *contexte des réformes de 1988, 1991 et 1996* : aucune source d'époque lue (débats de la
    Chambre des députés, plans, presse) ;
  - *conventions de branche* : seule celle du textile est relue pour ces articles, sur un
    exemplaire dégradé (art. 27 à relire) ; les autres textes sont au corpus ;
  - *séries* : durée effective du travail seulement en 2019 (OIT, ENPE) et sur trois trimestres
    de 2019 (INS, « sur-emploi ») ; aucune mesure des heures supplémentaires payées ni de la
    répartition entre régimes de 48 et de 40 heures ;
  - *glossaire* : onze notions créées par le terminologue (statut provisoire).
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
  citer les art. 31-52 mot pour mot). Le 20 octobre 2026, OCR des n° 21 et 22 entiers et des
  pp. 716-720 du n° 20 (fichiers de travail, non conservés au dépôt) ; art. 1 et 4 de la loi de
  promulgation, art. 79-124 et 445 lus à l'image. Les rectificatifs du n° 27 (p. 960) et du
  n° 37 (p. 1298) de 1966 sont lus : le second remplace, à l'art. 113, al. 2, « dix-huit à
  vingt et un ans » par « dix-huit à vingt ans ». Art. 31-52 (conventions collectives,
  pp. 720-721) toujours non relus à l'image.
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
- `_transport.qmd` (`#sec-compensation-transport`), **nouveau le 11 octobre 2026**, premier jet à
  relire : voir « Le transport public » ci-dessous.

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
  - **Figure des tarifs de la moyenne tension** (24 octobre 2026) : `fig-compensation-eg-tarifs-mt`
    (`_electricite_gaz.qmd`, `figures/electricite.py`, série versionnée
    `precis/_seriescache/steg-tarifs-moyenne-tension.csv`, 118 lignes, écrite et comparée aux trois
    tableaux par `scripts/serie_tarifs_mt.py`, test `tests/test_serie_tarifs_mt.py`). Une courbe par
    poste, trois familles sans raccord ; le tarif de secours et la prime sont dans l'onglet
    « Données » ; libellés arabes à verser (traduction différée) ; haute tension et gaz non tracés.
  - **Vue en monnaie de 2025** (24 octobre 2026) sur `fig-compensation-eg-tarifs-mt` et
    `fig-compensation-eg-prix-achat-gaz` : valeurs calculées, non observées, avec l'indice
    annuel moyen publié de 2025 pour référence (même année de base que les autres figures en
    dinars constants, `scripts/dinars_constants.py`) ; colonne `valeur_2025` de l'onglet
    « Données ». À actualiser à la publication de l'indice annuel suivant (2026).
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
- **Bibliographie** (bibliographe, état du 24 octobre 2026) : les clés `bct-ra-1987`, `bct-ra-1997`,
  `decret78-316`, `minenergie-opendata-prix-vente-petroliers`, `ins-bms`, `lf-1981`,
  `loi91-98-lf1992` et `loi86-106-lf1987` existent (le précédent état de cette liste était périmé).
  Versées le 24 octobre 2026 (FR et AR, compensation) : `arrete-1990-10-11-cgc`,
  `arrete-1992-07-07-cgc`, `arrete-2024-05-10-redevance-patisseries`, `lfc-2008`, `fipa-2002-06-electricite-aout-2000`,
  `fipa-2003-08-gaz`, et dix-sept décrets de prélèvement (`decret93-1187`, `decret95-851`,
  `decret95-1212`, `decret97-2509`, `decret2002-2227`, `decret2003-2048`, `decret2004-2314`,
  `decret2005-213`, `decret2005-2931`, `decret2006-1`, `decret2006-4`, `decret2006-1835`,
  `decret2007-8`, `decret2007-10`, `decret2007-1199`, `decret2009-2293`, `decret2015-50`). Restent : les articles de
  presse de la frise des prix 2002-2018 (cités en clair dans le tableau, non versés) ; la collection
  Zotero « Compensation », à créer ; la loi de finances pour 2024 (art. 45), fascicule
  n° 144 de 2023 absent du corpus local et de pist.tn.
- **Glossaire** (terminologue, 24 octobre 2026) : toutes les notions listées jusqu'ici existent
  et sont ancrées ; le mécanisme de 2009 est décrit dans `ajustement-automatique-prix-carburants`.
  Dix entrées ajoutées : `tranche-economique`, `tranche-normale`, `fonds-transition-energetique`,
  `homologation-des-prix`, `decision-ministerielle` (`valide`, définitions arabes à relire par un
  arabophone) ; `redevance-compensatrice`, `compte-caisse-compensation`, `dotation-budgetaire`,
  `prix-limite-vente`, `base-caisse` (`provisoire`, terme arabe non attesté, sans définition
  arabe). Restent :
  - termes arabes à relever : éditions arabes de l'arrêté du 5 février 1957 et des arrêtés de
    prix 1964-1993 (corpus, image) ; « dotation » et « compte » de la Caisse dans les rapports
    arabes de la BCT ou du ministère des Finances ;
  - `base-caisse` n'a pas de `source_definition` : le chapitre ne cite aucun texte qui définisse
    la notion ;
  - « tranche économique » : le JORT écrit القسط الاقتصادي en 1984 et الشريحة الاقتصادية dans
    les lois de finances pour 2019 et 2024 ; la seconde est retenue comme terme, à confirmer ;
  - tableau A du décret n° 91-1996 : dans l'édition arabe d'origine (JORT n° 88 de 1991,
    p. 1766, lue à l'image), les carburants sont au n° 7 et l'électricité, l'eau et le gaz au
    n° 8 ; rétablissement du tableau au JORT n° 30 de 1992 non lu ;
  - « taxe due sur les produits énergétiques consommés » : pas d'entrée propre, décrite dans
    `fonds-transition-energetique`.
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
  - **Dotation du budget à la Caisse, dix années sans valeur versée** (1988, 1989, 1990, 2000,
    2001, 2003, 2006, 2008, 2009, 2011), **traitée le 24 octobre 2026** (fiche
    `r-cgc-dotation-annees-manquantes`). Rapports annuels de la BCT 1987-2013 parcourus au texte
    intégral : aucun montant ; archives du web : rien. **Ajouté** (`_institution.qmd`, tableau
    `tbl-compensation-lf-caisse`) : subvention du budget **prévue** par les lois de finances
    initiales 1987-1994, tableaux des fonds spéciaux lus à l'image (188, 188, 188, 300, 272, 255,
    245, 230 MD ; pages dans le tableau) ; crédits d'interventions du ministère du commerce 2000,
    2001, 2002 et 2011 (`tbl-compensation-lf-commerce`), non désignés comme la dotation (251,2 MD
    en 2002 pour 235 MD de dotation) ; 70 MD de 2007 dépensés en 2008. **Complété le 24 octobre
    2026** : lois de règlement des gestions 1990 et 2000 à 2009 lues (fonds spéciaux en un seul
    total, la Caisse n'y est pas nommée) ; ligne « compensation » du budget du ministère du
    commerce (rapports sur les finances publiques) rapprochée de la dotation de la BCT pour 2003,
    2006, 2008, 2009 et 2011 (ordre de grandeur, non montant ; égale en 2004 et 2010, écart en
    2005 et 2007). **Seconde passe** : lois de règlement des gestions 1988 et 1989 lues
    à l'image (totaux des fonds spéciaux seuls : 460,2 et 659,82 MD) ; lois de finances 1995-2011
    balayées : la Caisse n'est nommée qu'en 2011 ; arrêtés des 11 octobre 1990 (302 → 320 MD) et
    7 juillet 1992 (270 → 348 MD) lus ; prêts du Trésor de 95 MD (LF 1981, art. 58) et de 73 MD
    (LF 1992, art. 77) versés ; suppression de la taxe spéciale de compensation à l'importation
    (décret n° 78-315, LF 1981, art. 33) ; crédits du ministère du commerce des LFC 2008 et 2009.
    Tableau III-1 du mémorandum de 1985 versé (`_exterieurs.qmd`) ; prix de la bouteille de
    gaz du 4 août 1992 (3,800 D) lu à l'image ; arrêté du 10 mai 2024 sur les pâtisseries versé.
    **Restent** : montant versé de 1988-1990, 2000, 2001 et, au sens strict, des
    cinq années précédentes (lois de règlement 1988 et 1989 à lire à l'image, budget économique,
    lois de finances complémentaires, tableaux des fonds spéciaux des lois 1995-2010 non
    ouverts). Recettes propres après 1999,
    charges par produit de 1984, 1989-1991 et 1994, prêts et avances du Trésor par année : non
    établis.
  - **Loi de finances pour 1987** : lue le 24 octobre 2026 (loi n° 86-106, JORT n° 78 de 1986,
    art. 91 et 92, p. 1623 ; tableau L, p. 1677). Fait.
  - **Prélèvements à l'importation au profit de la Caisse, 1990-1993** (nouvelle section
    `#sec-compensation-prelevements-importation`) : huit décrets lus à l'image ; ensuite : décret
    n° 93-1187 du 24 mai 1993 et modifications du décret n° 91-1391 (n° 2002-2227, 2009-2293,
    2015-50) : **lus et versés le 24 octobre 2026** (clés `decret93-1187`, `decret2002-2227`,
    `decret2009-2293`, `decret2015-50`, FR et AR) ; **seconde passe** : onze décrets de suspension ou
    de réduction de 1998 à 2007 lus (tableau `tbl-compensation-prelevements-suspensions`) et décrets
    n° 95-851 (bovins, 8 mai 1995) et n° 95-1212 (fruits, 10 juillet 1995), tous deux au profit
    de la Caisse (tableau `tbl-compensation-prelevements-1995`) ; restent les décrets de
    suspension de 1998 à 2002 et d'après 2007, la suite du tarif de 1995 (p. 1534) et le produit
    annuel (fiche `r-prelevements-importation-cgc`). Clés `decret90-1193`,
    `decret90-1194`, `decret91-1391`, `decret92-1340`, `decret93-1605`, `decret93-1924`,
    `decret93-2115`, `decret93-2116` versées (FR et AR, compensation).
  - **La Caisse reste un fonds spécial du Trésor** : elle figure aux tableaux des fonds spéciaux
    de 1987 à 1994 et aux lois de finances pour 2011 et 2012 (sans montant). Aucun texte de
    sortie n'est à chercher ; fiche `r-cgc-budgetisation-1992-2003` : tableaux 1995-2010 à
    ouvrir pour dater la disparition de la subvention du tableau.
  - **Décret d'application de l'article 3 de la loi n° 70-26** : non identifié (fiche).
  - **Rupture de 2015** : effet constaté de la séparation de 2015 à 2018, subvention indirecte de
    2013 et 2014, bénéficiaires de la ligne en 2013 et après 2016, recettes de commercialisation
    encaissées de 2019 à 2025, acte formalisant la séparation (fiche), décision du 8 octobre 1993
    sur le prix du gaz (nature de l'acte non établie ; « arrêté » corrigé le 17 octobre 2026 dans `_carburants.qmd`), régularisation des impayés de 2016 : non établis. Rapport de 2014 :
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
    `compensation-tarifs-electricite-gaz.md`, `compensation-tarifs-1993-2004.md`,
    `compensation-tarifs-mt-ht-gaz.md`, la fiche de plan
    `compensation-electricite-gaz-plan-architecte.md` et la note
    `compensation-electricite-gaz-objets-des-reformes.md` — **converti le 17 octobre 2026 au
    format « ruptures au premier plan, détail replié »** (fusionné le 17 octobre 2026, #453) : vue d'ensemble (tarif des
    ménages en cinq dates) ; mise en place jusqu'en 1982 ; quatre réformes (1984, 1991-1992,
    2014, 2015) et les grilles des ménages en trois blocs repliés ; état du droit au 1er janvier
    2024 (grille de 2022, taxe du Fonds de transition énergétique, homologation des prix) ; gaz
    des ménages ; tarifs des entreprises ; longue période (subvention à la STEG, coût et prix de
    vente). Sections de dispositifs en domicile unique, registres ancrés `r-eg-…`. Tous les
    identifiants, clés et couples de citation du départ sont conservés. **Corrigé** :
    tranche économique de 1984 à **61** millimes (prix unique de 1982 maintenu), non 51 ; la
    réserve sur la première apparition de la tranche est levée (arrêtés de 1980 et de janvier
    1981 lus, sans tranche) ; rupture de 1991-1992 datée du 1er janvier 1992 (loi n° 91-64,
    art. 62) ; tableau A en vigueur celui du décret n° 95-1142 (n° 9) ; décret n° 2015-307 sans
    effet sur la liste ; taxe du Fonds de transition énergétique instituée sur l'électricité par
    la loi de finances pour 2019 (art. 68), portée à 5 millimes par celle pour 2024 (art. 51) ;
    2014 : phrase d'objet du rapport de contrôle (p. 75) et dates divergentes (1er janvier et
    1er juin selon le rapport, 1er mai selon la grille) exposées sans trancher ; prime de la
    moyenne tension en dinars par kW et par mois en 1984. Huit références créées (arrêtés de
    1980 et 1981, loi n° 91-64, décrets n° 95-1142 et 2015-307, loi n° 2015-36, tarif
    interruptible de 2013). **Restent** (lisibles dans le corpus, sauf mention) :
    avis et communications des JORT n° 75 à 86 de 1993 : **lus à l'image le 24 octobre 2026, aucun
    ne porte sur le gaz ou un tarif** (fiches `r-decision-1993-10-08-prix-cession-gaz` et
    `r-tarifs-electricite-gaz-apres-1992`) ; actes
    tarifaires depuis 1992 — 10 août 2000, 5 mars 2013, et ceux d'octobre 1993, juin 1994, août
    2001, avril 2003, mai 2004 et 2014 — non identifiés au JORT (à demander à la STEG si les
    archives restent muettes) ; date d'effet des hausses de 2014 (1er janvier et 1er juin, ou
    1er mai) ; grille basse tension du 1er janvier 2014 et grille résidentielle de mars 2013, à
    obtenir ; éclairage public de 1984 au-delà de 60 kWh (31 dans l'édition française, 51 dans
    l'arabe), non repris ; arrêtés du 16 juin 1977 et du 27 février 1978, décret n° 61-47 et
    arrêtés de 1963 et 1976, connus par leur intitulé (fascicules au corpus) ; décret n° 93-59 et
    rétablissements des annexes du décret n° 91-1996 (JORT 1992, n° 11 et 30), à lire pour la
    version du tableau A de 1991 à 1995 ; date de première facturation de la taxe du Fonds de
    transition énergétique, et aucun décret de taux identifié de 2014 à 2018 ; décret
    gouvernemental remplaçant la liste après la loi n° 2015-36 (fiche
    `r-decret-91-1996-liste-apres-2015`) ; jour d'effet des grilles d'octobre 1993 et de juin
    1994 (fiche `r-tarifs-electricite-grilles-1993-2003`) ; moyenne et haute tension et gaz de
    1994 à 2003 **versés le 24 octobre 2026** (grilles de juin 1994, août 2000, août 2001 et
    avril 2003 ; gaz ; pages des agences publiques et ESMAP relus aux sources) ; restent la
    grille d'octobre 1993 (moyenne et haute tension, gaz), les soir et nuit de la moyenne
    tension en 2001, la formule de la haute pression de 1992 à avril 2000 et la grille « Mai
    2004 » de la FIPA (étude de l'ANER d'avril 2000 lue : prix moyens par niveau de tension
    1996-1998 en graphique sans valeurs, annexes de tarifs absentes) ;
    contradiction de 2003 (90 ou 94) et écart de 2005 avec l'INS ; tarifs du Journal officiel
    de 1975 à 1990 à relire (moyenne et haute tension, unité de la prime de 1975 à 1982) ; haute
    tension de septembre 2012, moyenne pression de 2012-2013 ; heures des postes avant 2014 ;
    ventes en haute tension de 2020 ; **figure de la facture type**
    (`fig-compensation-facture-electricite`, TODO figures : TVA et surtaxe municipale à
    reconstituer) ; subvention d'exploitation de la STEG de 2017 à 2021 (états de résultat des
    rapports annuels, à relire et à verser ; 2006-2016 versée le 17 octobre 2026) ; décodage des couches texte du JORT des années 2000 à verser à
    `docs/notes/outillage-sources.md`. **Faits des notes non repris**, par décision du
    propriétaire (17 octobre 2026), à reprendre éventuellement : partage entre ménages et autres
    abonnés de l'électricité en 2014 (`compensation-tarifs-electricite-gaz.md`, (ii)) ; tarif du
    gaz de 1982 (146 millimes le m³) ; tarif propre des cimentiers en 2016. **À corriger hors du
    chapitre** : `_carburants.qmd` (l. 29, légende de `tbl-compensation-prix-cession`) écrit
    encore « arrêté du ministre de l'Économie nationale du 8 octobre 1993 » ; la nature de
    l'acte n'est pas établie (« قرار » selon le rapport de contrôle). Bibliographe : doublon
    `lf-2019` (Fiscalité) / `loi2018-56-lf2019` (fonds commun) à résoudre. Terminologue : notions
    du § 9 de la note `compensation-electricite-gaz-objets-des-reformes.md` (tranche
    économique, tranche normale, Fonds de transition énergétique, homologation des prix,
    décision ministérielle).
  - **Séries d'achat du gaz et de coût de l'électricité de la STEG** (17 octobre 2026,
    `compensation-electricite-gaz-series-steg.md`, 23 séries de travail hors dépôt) : le prix
    moyen d'achat de la tep gaz est publié par la STEG dans ses états financiers avec notes
    (2013-2023 ; 2007-2013 par le rapport de contrôle de 2014 ; 90,8 DT/tep administré de 1993
    à 2006) ; la valeur FOB du gaz algérien par l'ETAP (2005, 2008-2014), puis le prix
    d'importation de l'Observatoire (2013-2025) ; le coût de revient du kWh pour 1996-1998,
    2000-2004, 2008-2018 et 2022-2025 ; les prélèvements de gaz par source de 2001 à 2024.
    **Rupture** : note 11 des états financiers 2014, p. 23 — depuis 2007 le gaz est enregistré
    à sa valeur économique et la différence figure en subvention d'exploitation, égale au
    « soutien total » du rapport de contrôle de 2014 pour 2007-2013 ; les coûts d'avant et
    d'après 2007 ne se chaînent pas. **Fait le 17 octobre 2026** : quatre séries versées à
    l'entrepôt (`steg-prix-achat-gaz`, `steg-cout-prix-kwh`, `steg-subvention-exploitation`,
    `steg-prelevements-gaz`, fiche `docs/steg-gaz-electricite.md`, transcription relue sur les
    PDF) et quatre figures de longue période dans `#sec-compensation-eg-longue-periode`
    (`fig-compensation-eg-prix-achat-gaz`, `-cout-prix-kwh`, `-subvention`, `-gaz-sources`),
    familles séparées, ruptures de 2007 et de 2015 marquées ; quatorze références versées
    (états financiers 2014-2023, rapports annuels 2005, 2023 et 2024, Mémentos de l'Observatoire
    de 2014 et 2016, étude de l'ANER, rapport d'achèvement de la BAD sur Électricité VII). Les
    tableaux de coût et de prix restent visibles. **Fait aussi le 17 octobre 2026** : la
    facture des combustibles de la STEG (2013-2023, états financiers, onze valeurs relues sur les
    PDF, écart de 2017 consigné) versée à l'entrepôt (`steg-facture-combustibles`) et la figure
    `fig-compensation-eg-gaz-pib` (`#sec-compensation-eg-gaz-achat`) : pont de cette facture en
    points de PIB nominal (base 2015, 2013-2014 rétropolés par l'INS), en trois effets — prix,
    quantité déduite, PIB — sur 2013-2016, 2016-2022, 2022-2023 et 2013-2023 ; décomposition
    logarithmique calculée dans le module de figure, testée. **Reste à faire** pour cette figure :
    la facture comprend le fuel et le gazole, la quantité déduite est le « total des achats de
    gaz » et non du gaz seul (aucune facture du seul gaz n'est publiée) ; les valeurs de 2005,
    2007 et 2008 des rapports annuels (« achats de combustibles », « facture combustible ») ne sont
    pas versées, leurs pages restent à relire ; 2022 et 2023 s'écartent de 0,6 et 1,7 ktep du
    total publié des achats de gaz (cause non dite par les états financiers) ; version arabe de
    la note de lecture et des libellés, à terme. **Reste à faire** : prix d'importation du
    gaz algérien de l'Observatoire (2013-2025, versé, non tracé : figure ultérieure) et valeur FOB
    de l'ETAP (2005, 2008-2014, non versée) ; coût de revient de 2015 par les états financiers
    2015 (lu par reconnaissance de caractères, non relu) ; subvention d'exploitation de 2017 à
    2021 ; coût du combustible au kWh de 2013 à 2023 (calcul à construire et à valider contre
    2008-2012) ; ventilation du gaz algérien entre redevance et achats de 2001 à 2006 ; coût par filière et achats
    d'électricité par fournisseur : aucune série publiée, à demander à la STEG ; fiche
    `r-prix-gaz-commercial-concessions-apres-2000` (décret n° 2000-1027 et ses suites) ;
    états financiers 2024 introuvables ; rapports de l'ETAP de 2006 et 2007 à océriser ou réparer.
  - **Prix du gaz par source de la STEG** (17 octobre 2026, `compensation-electricite-gaz-prix-par-source.md`) :
    le prix publié est un prix moyen FOB des achats algériens contractuels et additionnels réunis (ETAP 2005, 2006,
    2008-2014 et premier semestre 2015 ; rapport de contrôle 2008-2013 ; Observatoire 2013-2025) ; le prix de chaque
    part existe (deux factures mensuelles de la SONATRACH, rapport de 2014, p. 42) mais n'est publié nulle part. Miskar :
    un prix depuis le 8 juin 2022 seulement (466 puis 384 et 387 $/tep, ETAP), le gaz étant vendu par BG/Shell avant. Gaz
    national : prix par champ de l'ETAP 2016-2019 et 2021-2024, **part de l'ETAP** (environ la moitié du prélèvement de la STEG
    sur chaque champ), non le prix du bloc de la figure. Redevance : 90,8 DT/tep jusqu'en 2014, aucun prix ensuite
    (valorisation « au prix international », dû de 115 MDT en 2015, non un prix). **Formule du prix du gaz national** :
    décret-loi n° 85-9, art. 33 (85 % du fuel à haute teneur en soufre) avant mai 2000, décret n° 2000-1027 (80 %) ensuite, et un
    avenant de Miskar du 13 mai 2000 qui applique le prix du code avec effet de mars 2000, jugé irrégulier par le rapport de
    contrôle (105 MD de surcoût de 2000 à 2013). **Restent** : prix de Miskar de 1996 à 2022, prix contractuel et additionnel de la
    SONATRACH, valorisation de la redevance après 2014, rapport de l'ETAP de 2020, états financiers 2024, annexes 11, 19, 20, 38,
    39, 45 et 46 du rapport de 2014 ; demandes à l'ETAP et à la STEG listées dans la note. Aucune figure n'en est tirée pour l'instant.
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

## Les entreprises publiques

Volume X (`precis/fr/entreprises_publiques/`), **brouillon** du 11 octobre 2026 : un seul
chapitre, `_relation_financiere.qmd` (`#sec-ep-relation`), écrit sur la note
`docs/notes/entreprises-publiques-2026-10-11.md` et sur les onze séries versées dans
`tunisia-data` (`sources/entreprises-publiques.md`) ; quand la note et une série divergent, la
série fait foi. La forme — volume ou chapitre d'un autre volume — reste à trancher par la revue
humaine. **Le livre n'existe qu'en français** : pas de dossier `precis/ar/entreprises_publiques/` ;
il est lié depuis la page d'accueil (partie V, depuis le 20 octobre 2026) et inscrit dans `build.sh`, `build_glossary.py` et
`verifier_livres.py`, qui sautent un livre arabe absent.

Plan : vue d'ensemble (`#sec-ep-vue-ensemble`) ; mise en place 1969-1987 ; grandes réformes
(1989, 1994-2001, cessions 1987-2009, rapport annuel de 2019, depuis 2011) et registre des
textes ; état du droit ; transferts du budget ; garanties ; dettes et créances croisées ;
dividendes et versements ; cessions ; longue période ; Livre blanc de 2018 et études
extérieures ; section « Les effectifs et la masse salariale » (`#sec-ep-effectifs`) ajoutée le
11 octobre 2026, avant la longue période. Le tableau de l'encours de la dette garantie
(`tbl-ep-encours`), double de l'onglet « Données » de `fig-ep-encours`, est retiré le 13 octobre
2026.

**Annexe « La liste des entreprises publiques, 1997-2021 »** (`_annexe_liste.qmd`,
`#sec-ep-liste`), écrite le 13 octobre 2026 sur `docs/notes/entreprises-publiques-liste-2026-10-13.md` :
nombre d'entreprises à chaque liste (figure `fig-ep-liste-perimetre`), entrées et sorties liste
après liste, établissements considérés comme entreprises publiques, liste partielle de 1989-1990 ;
tableau complet et registre des décrets repliés. Deux relevés versionnés dans
`precis/fr/entreprises_publiques/listes/` (totaux contrôlés par
`tests/test_listes_entreprises_publiques.py`). Quinze sorties portent l'année et le mode d'une cession, lus au « Recueil des
opérations depuis 1998 » de la Direction générale de la privatisation (série
`privatisation-recueil-operations`, relevé `listes/sorties-recueil-privatisation.csv`).
**Restent** : quinze sorties sans opération au recueil — texte de fusion, de dissolution ou de
cession **à chercher au corpus du Journal officiel** ; listes nominatives des rapports du ministère pour 2022 à 2025 (**lisibles dans le
corpus de tunisia-data**, à feuilleter à l'image) ; identités retenues sur le seul nom (huit cas,
TODO de l'annexe) ; contradiction sur l'Agence tunisienne d'Internet (Cour des comptes, 2008) ;
forme et participation par entreprise ; périmètre d'ensemble avant 1998 (aucune liste publiée) ;
tableau de tutelle après 2010 et classement de l'Office national des postes frontaliers
terrestres (fiches `r-ep-tutelle-modificatifs-apres-2010`, `r-onpft-classement-entreprise-publique`) ;
noms arabes des listes ; libellés arabes de la figure. Dix figures et trente tableaux, tous engendrés depuis les séries sauf quatre
(les réformes ; les deux registres de textes ; les six éditions du rapport). Depuis le
11 octobre 2026 (retouche), chaque figure a trois vues — dinars courants, % des dépenses de
l'État hors service de la dette, % du PIB — et les tableaux de premier plan les mêmes colonnes ;
les dinars constants sont retirés du volume.

Ce qui reste :

- **Chapitre « Restructurer » (`_restructuration.qmd`, `#sec-ep-restructuration`), ouvert le 28 octobre 2026**
  sur la note `docs/notes/restructuration-textes-2026-10-28.md` : fonds de restructuration du capital (1986-2010,
  série 2004-2011 et extinction 2018-2024), reprise des dettes bancaires de 1999, banques publiques 2013-2019,
  Tunisair et sociétés de transport 2014-2019 ; vingt textes lus au registre. **Restent** : réalisation du fonds
  1986-2003 (rapports de clôture absents ; lois de règlement, rapports de la Banque centrale) ; recettes du fonds
  2012-2016 (annexes de recettes non lues ; rapport 2012 à couche texte déformée, **à lire à l'image**) ; traitement
  du prélèvement sur le compte des jetons de présence dans les recettes de 2007, 2008 et 2010 ; prélèvements de
  2004, 2006 et 2011 (fiche `r-ep-fonds-restructuration-prelevements` ; loi n° 2004-87 **lisible dans le corpus**) ;
  tableau « G » de la loi n° 98-111 (**lisible dans le corpus**) ; décret du fonds de modernisation du secteur
  bancaire (fiche `r-ep-fonds-modernisation-bancaire-decret`) ; montants souscrits par banque et emploi des
  133 MD non répartis en 2015 (rapport annexé aux lois de finances, rapports annuels de la STB et de la BH,
  **à obtenir**) ; ligne « assainissement et restructuration » de 2016 (rapport de clôture de 2016, **à lire à
  l'image**) ; pages du rapport de clôture de 2005, citées au fichier ; section « Ce qu'en dit l'économie »
  (recapitalisation bancaire), pas encore écrite.
- **2010-2024 : quatre flux de clôture et l'encours garanti, versés les 24 et 27 octobre 2026** (série
  `cdc-cloture-entreprises-publiques` de `tunisia-data`, prolongée le 27 octobre sur la branche
  `donnees/cdc-cloture-2017-2024` ; section `#sec-ep-lp-cloture`, figure `fig-ep-cdc`, trois tableaux repliés ;
  encours de la Cour superposé à celui du ministère sur `fig-ep-encours` ; cessions 1987-2009 et recettes de
  privatisation du budget 2010-2024 sur une seule figure `fig-ep-cessions`) : versements au budget
  (« transferts des entreprises publiques et profits du Trésor », total et lignes jusqu'en 2019 ; depuis 2020 la
  Cour n'imprime plus de total, la somme des lignes est calculée par le précis et dite telle quelle), principal et
  intérêts de la dette garantie payés par l'État, remboursements de prêts reçus (total jusqu'en 2019, puis prêts
  rétrocédés et prêts du titre II), recettes de privatisation inscrites au budget (aucune ligne de 2017 à 2024),
  encours de la dette garantie en fin de gestion (2018, 2019, 2021-2023 ; rien d'imprimé pour 2020 et 2024),
  d'après les rapports de la Cour des comptes sur la clôture du budget des gestions 2011 à 2016 et 2018 à 2024
  (chacun avec la gestion précédente ; 2010 et 2017 par la colonne de comparaison). **Ce que la série n'est
  pas** : ni transferts du budget aux entreprises (les rapports ventilent par ministère et par nature), ni encours
  avant 2017. **Restent** : transferts
  par entreprise 2010-2015 (le rapport sur les transferts et les garanties commence avec l'édition LF 2020 ;
  rapports annuels de la Banque centrale 2010-2016 et rapport « Finances publiques » du ministère pour 2010
  ouverts le 27 octobre 2026 sans résultat, voir la fiche `r-ep-series-budgetaires-avant-2016` ; lois de
  règlement du Journal officiel non ouvertes) ; rapports de clôture des gestions 2010
  (absent du catalogue de la Cour) et 2017 (au catalogue, sans fichier) ; encours des gestions 2020 et 2024 ;
  dividendes 2023 : libellés pétrolier et non pétrolier inversés entre les rapports 2023 et 2024, non arbitrés ; fonds de restructuration du capital des entreprises à participation publique
  et recapitalisations des banques publiques en réalisation (tableaux des fonds spéciaux de chaque rapport) ;
  intérêts de 2012 à 2014 lus à la couche texte (recoupés d'un rapport à l'autre) ; rapport de l'Unité de suivi
  (Présidence du gouvernement) que cite le Livre blanc, non obtenu (fiche `r-ep-rapport-unite-suivi-2010-2014`).
  PIB : base 2015, rétropolée par l'INS pour 2010-2014, dite sous la figure.
- **2003-2009 : versements au budget ; part de l'État dans le résultat de la Banque centrale, 2002-2010 — versés
  le 27 octobre 2026** (séries `cdc-cloture-entreprises-publiques-2003-2009` et `bct-part-etat-benefices` de
  `tunisia-data`, branche `donnees/cdc-cloture-2003-2009`, fusionnée ; section
  `#sec-ep-versements` du chapitre « Ce que l'État reçoit » (`_recettes.qmd`), figure `fig-ep-versements` de 2003 à
  2024, tableaux repliés `tbl-ep-versements-anciens` et `tbl-ep-bct-parts`). Rapports de clôture des gestions 2005,
  2006, 2007 et 2009 (chacun avec les deux gestions précédentes ; 2008 par le rapport 2009), lus à l'image ; aucune
  révision d'un rapport à l'autre. **Prolongé le 27 octobre 2026 (soir)**, branche `donnees/bct-passe-participations`
  de `tunisia-data` : part de l'État par exercice 2011-2025 (répartition du résultat, rapports 2011-2025, lue à
  l'image), partage budget / Fonds de péréquation des changes des exercices 1999-2001 (rapport 2002, p. 169),
  virements de 2011 (rapport 2011, p. 35, 144, 153) ; `tbl-ep-bct-parts` couvre les exercices 1999 à 2025. Série
  nouvelle `bct-ra-revenus-participations` : ligne « revenus des participations » des recettes non fiscales et
  versement de la Banque centrale, années budgétaires 1983-1988 et 1993-2016 (rapports 1985, 1988, 1995-2006,
  2008-2016, lus à l'image) ; section `#sec-ep-versements-bct`, figure `fig-ep-bct-ra`, tableau replié
  `tbl-ep-bct-ra`. Contre-lecture indépendante du 27 octobre 2026 (`docs/notes/recettes-2003-2009-contre-lecture-2026-10-28.md`,
  corrections appliquées, `tunisia-data` #82) : aucune erreur de lecture ; exercice 2007 lu dans les états financiers de
  la Banque centrale publiés au *Journal officiel* (n° 33 du 22 avril 2008, p. 1294 : part de l'État 435 MD) ; base
  légale de la retenue au profit du Fonds de péréquation des changes (loi n° 2000-98, art. 34), attestée pour 1999-2001
  et 2003 ; 882 MD inscrits au budget de 2011 selon le ministère des Finances aussi (rapport sur les finances publiques
  2011, annexe 5) ; ventilation excédents / bénéfices de la Cour gardée et dite (48,0 et 136,7 MD d'écart au ministère
  en 2008 et 2009) ; registre `tbl-ep-fpc-registre`. **Restent** : (1) écarts entre la part arrêtée par la Banque centrale et la ligne du budget de la
  gestion suivante — 5 MD (exercice 2002), 10,4 (2004-2005), 10 (2006), 10 (2007), 8 MD entre les 882 MDT budgétisés
  selon la Banque centrale et les 874 MD de la Cour pour 2011, +13,7 (exercice 2011, gestion 2012), -15 (2012),
  -10 (2013), -10 (2015) ; l'écart de 36,7 MD de 2008-2010 se décompose en 28,7 MDT de reliquat de l'exercice 2010,
  resté en compte d'ordre fin 2011 et soldé en 2012 (rapports 2011, p. 153 ; 2012, p. 154), et ces 8 MD ; égalité au
  dinar près depuis l'exercice 2016. Lu : chapitre des finances publiques des rapports 2001-2016 (tableaux à l'image) ;
  couches texte 2003-2012 cherchées (« reliquat », « péréquation », « compte d'attente ») ; notes des comptes d'ordre
  au passif des rapports 2011, 2012, 2013 et 2015, à l'image (« autres comptes d'ordre » de 2,1 à 4,9 MDT de fin
  2012 à fin 2015, sans ligne de reliquat ; rapport 2016 en couche texte seulement, 2,8 MDT fin 2016) ; rien d'autre
  que le Fonds de péréquation des changes (1999-2001, 2003). Lois de règlement : recettes par
  titre seulement au *Journal officiel* (loi n° 2010-6, gestion 2007, lue à l'image ; les autres non ouvertes, même
  forme présumée). Pistes : rapports de clôture de la Cour (comptes du Trésor), états financiers de la Banque
  centrale (affectation au Fonds de péréquation après 2003 ; publiés au *Journal officiel* depuis l'exercice 2007,
  sans ligne pour le fonds), comptes généraux de l'administration des finances 2008 et 2009 et rapport du ministère sur
  les finances publiques 2005, **à océriser** (`tunisia-data`, `minfinances/portail_ancien`) ; fiche
  `r-bct-retenue-fpc-2002-2011` ; TODO dans la section ; (2) 811 MD de bénéfices 2008 de la CPG et du GCT gardés hors
  budget selon la Cour : la Banque centrale ne confirme qu'au moins 605 et 211 MD reçus en 2009, et le ministère inscrit
  au budget de 2009 59 MD de la CPG et 225 MD du GCT ; rapport de clôture de la gestion 2010 **à obtenir** (absent du
  catalogue de la Cour) ;
  (3) dans les rapports de clôture 2005-2009 : principal et intérêts de la dette garantie, remboursements de prêts,
  recettes de privatisation, fonds spéciaux — lisibles (couche texte des rapports 2005, 2006 et 2009 propre ;
  rapport 2007 à lire à l'image, couche texte aux chiffres décalés) ; (4) gestions 2008 (sauf la recette des
  transferts, par le rapport 2009) et antérieures à 2003 : aucun rapport de clôture au catalogue de la Cour ;
  (5) « revenus des participations » : écart de 2009 expliqué (803,8 MD dans le rapport 2009, révisé à 788,6 MD,
  montant de la Cour, dans le rapport 2010) ; écart de 109,3 MD en 2011 (1 457,5 contre 1 566,8) non expliqué ;
  rapports 1986, 1987 et 1989 à 1994 de la Banque centrale : couche texte chiffrée, tableau des recettes non
  fiscales à localiser à l'image (pages du chapitre des finances publiques, OCR ou lecture directe) ; rapport 1998,
  p. 184 : « la Banque Centrale de Tunisie dont le bénéfice est revenu de 104 MDT en 1997 à 60 MDT en 1998 »
  (bénéfice ou versement ? non versé) ; rapport 2007 : ligne « excédent + recouvrement prêts », non versée ;
  (6) part de l'État dans le résultat de la Banque centrale avant 1999 : les rapports antérieurs à 2001 n'impriment
  pas les états financiers de la Banque ; versements au budget seulement (1983-1985, 1987-1988, 1999-2004, dans
  `bct-ra-revenus-participations`) ; rapports 1959-1984 à lire pour la même ligne. PIB du ministère des Finances
  (2003-2004 sans base, 2005-2009 base 1997) puis INS base 2015, ruptures marquées sur la figure ; 1983-1985 : PIB
  de la Banque mondiale (bases accolées).
- **Avant 1987, et avant 2016 pour les transferts par entreprise et l'encours de la dette garantie** : rien
  (fiche `r-ep-series-budgetaires-avant-2016`, passe du 24 octobre 2026, résultat partiel). Pistes non
  ouvertes : lois de règlement du Journal officiel, Cour des comptes (dette publique extérieure, 2018), plans
  de développement ; rapports annuels de la Banque centrale ouverts le 27 octobre 2026 pour sa seule part de
  l'État (2002-2010) et, pour les transferts, 2010-2016 avec le rapport « Finances publiques » du ministère pour
  2010 : classement par nature et par ministère, aucun total par bénéficiaire (fiche, passe du 27 octobre 2026).
  Passe du 27 octobre 2026 (soir) sur les rapports annuels 1985-2015 de la Banque centrale : une seule expression
  régulière sur les couches texte (celles de 1985-2000 déchiffrées par décalage de caractères), « subvention,
  transfert, dotation, intervention » près de « entreprises publiques, établissements publics, offices » et d'un
  montant : aucun résultat ; les tableaux à l'image n'ont pas été feuilletés. Piste non lue : ligne « Subventions aux
  établissements publics » avec montants dans les rapports 1976 à 1978 (périmètre à établir : établissements
  administratifs ou entreprises publiques) ; côté recettes, revenus des participations 1983-1985 et 1987-1988 versés
  (`#sec-ep-versements-bct`). Rapports 1986, 1987, 1989-1994 : couche texte illisible, à lire à l'image.
  Le plafond des garanties est lu de 1958-59 à 2015
  (voir le point « Plafond légal » plus bas). Recettes de cession : 1987-2009 (Direction générale de la
  privatisation) et 2010-2016 (clôture) ; rien depuis 2017.
- **Annexes du projet de loi de finances pour 2026** : non obtenues (fiche
  `r-ep-annexes-plf-2026`).
- **Total sans les caisses, la STIR, la STEG et les offices des céréales et de l'huile — fait le
  27 octobre 2026** (chapitre `#sec-ep-transferts`, tableaux `tbl-ep-transferts-reste` et
  `tbl-ep-transferts-compensation` ; série `entreprises-publiques-transferts-par-etablissement`,
  branche `donnees/ep-transferts-par-etablissement` de `tunisia-data`, fiche
  `sources/minfin-transferts-par-etablissement.md`) : tableau 3.1 « par établissement » des éditions
  LF 2021 à LF 2025 lu à l'image, 2018-2023 et loi de finances 2024. STIR + STEG = poste « carburants »
  de la compensation chaque année. **Restent** : 2017 (la traduction française de l'édition LF 2021
  omet le bloc du ministère du Commerce ; original arabe sur gbo.tn, **à obtenir**) ; la subvention du
  transport public, comptée avec les autres concours aux sociétés de transport (tableaux par
  établissement et par nature, **lisibles dans le corpus de tunisia-data**) ; le bénéficiaire de
  l'écart de 191 à 307 MD par an entre le poste « produits de base » et l'Office des céréales et
  l'Office de l'huile ; la nature des transferts à l'Office de l'huile : en partie établie le
  28 octobre 2026 (`#sec-ep-ge-onh` : subvention d'exploitation égale aux transferts en 2022,
  inférieure de 10 à 39 MD de 2018 à 2021 ; approvisionnement en huile végétale subventionnée « pour
  le compte de l'Etat », titre III du budget de l'Office depuis le décret n° 2000-2579) ; la part
  des achats d'huile d'olive reste à établir.
- **Fiches par entreprise : STEG, ETAP et SNCFT versées le 27 octobre 2026** (chapitres
  `_energie.qmd`, sections `#sec-ep-steg` et `#sec-ep-etap`, et `_grandes_entreprises.qmd`, section
  `#sec-ep-sncft` ; séries
  `entreprises-publiques-fiches-entreprises`, `steg-etats-financiers` et `etap-rapports-annuels`
  de `tunisia-data`, branche `donnees/ep-fiches-entreprises`). Éditions LF 2022 (dette par
  créancier, 2018-2020), LF 2024 et LF 2025 (bilan et résultat, 2020-2023), lues à l'image ;
  comptes publiés de la STEG 2013-2023 ; rapports annuels de l'ETAP 2004-2024 (sans 2020 ; 2019
  sans états financiers) ; textes fondateurs lus au corpus local (décret-loi n° 62-8, loi
  n° 72-22, décret du 27 décembre 1956). Tableaux de données mis en figures le 28 octobre 2026
  (`fig-ep-transferts-entreprises`, `fig-ep-resultats-entreprises`, `fig-ep-transferts-revisions`,
  `fig-ep-steg-comptes`, `fig-ep-etap-rapports`, `fig-ep-{steg,etap,sncft}-fiches`) ; les fiches
  imprimées détaillées restent en tableaux repliés (`tbl-ep-*-fiche-a`, `tbl-ep-*-fiche-b`).
  **Reste** :
  - les autres grandes entreprises (Tunisie Télécom, Poste, Office du commerce et SNDP versées le
    29 octobre 2026, `#sec-ep-ge-tt`, `#sec-ep-ge-poste`, `#sec-ep-ge-otc`, `#sec-ep-ge-sndp`) : mêmes trois éditions, pages connues par la série des effectifs ; lisibles dans
    le corpus de `tunisia-data`, à l'image ; leurs textes fondateurs, à chercher dans
    `jort_cache.db` ;
  - SNCFT : loi n° 2005-72 (assainissement financier) lue et portée au registre le 30 octobre 2026
    (`r-ep-sncft-2005`) ; statuts de 1969 (loi n° 69-31, JORT n° 19 de 1969, p. 581-584, dans le corpus local,
    non lus) ; comptes avant 2018 (rapports annuels de la société, à obtenir) ;
  - STEG : bilan avant 2013 (rapports annuels 2006-2016 déjà rangés dans `tunisia-data`,
    `data/raw/minenergie/steg/rapports-annuels/`) ; notes des états financiers de 2022 sur le
    « complément de subvention à recevoir » (p. 27), non dépouillées ;
  - ETAP : redevances et impôts versés à l'État (lignes « impôts et taxes » de chaque état),
    non relevés ;
  - éditions françaises LF 2020 et LF 2021 et édition LF 2023 : comptes dans la prose, non
    versés ; classements par charges de personnel et par produits d'exploitation, non versés ;
  - chapitre « L'énergie » ouvert le 28 octobre 2026 (`_energie.qmd`, `#sec-ep-energie`, sur
    décision de l'humain ; la fiche de la STIR est versée le même jour ; note de chantier, § 10) : les sections
    de la STEG, de l'ETAP et de la STIR y sont déplacées sans changement de texte. La section
    d'ensemble reste dans `_grandes_entreprises.qmd` (ouvre la partie III) ; la SNCFT passe dans
    `_autres_entreprises.qmd` (`#sec-ep-autres-entreprises`).
  - chapitres « Les offices et les monopoles » (`_offices.qmd`, `#sec-ep-offices`) et « L'eau et les communications »
    (`_eau_communications.qmd`, `#sec-ep-eau-communications`) ouverts le 29 octobre 2026, par application de la règle
    de la note de chantier (§ 9, point 3 ; § 12), à confirmer à la revue : Office des céréales, ONH, RNTA et Office
    du commerce d'un côté ; SONEDE, ONAS, Tunisie Télécom et La Poste de l'autre, déplacées sans changement de texte,
    ancres conservées. « Les autres entreprises » garde la CPG et le GCT (`#sec-ep-autres-entreprises`).
  - chapitre « L'industrie » (`_industrie.qmd`, `#sec-ep-industrie`) ouvert le 30 octobre 2026, par la même règle, à
    confirmer à la revue : CPG, GCT, El Fouladh, Ciments de Bizerte, Ciments d'Oum El Kélil, SNCPA et AFI, déplacées sans
    changement de texte, ancres conservées. « Les autres entreprises » garde Tunisie Trade Net
    (`#sec-ep-autres-entreprises`).
- **CTF — section écrite le 29 octobre 2026** (`_energie.qmd`, en fin de chapitre ;
  `#sec-ep-ge-ctf`, figure `fig-ep-ctf-fiches` engendrée par `grandes_entreprises.figure
  ("ctf_fiches")`, tableaux repliés `tbl-ep-ctf-fiche-a` et `-b`, registre `tbl-ep-registre-ctf`).
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-ctf`) :
  LF 2022 p. 62, LF 2024 p. 94, LF 2025 p. 68, lues à l'image à 300 dpi et recoupées avec la
  couche texte ; toutes les identités bouclent ; seule divergence entre éditions, le signe des
  charges financières nettes (LF 2024 négatif, LF 2022 et LF 2025 positif). Lus sur les pages de
  l'édition LF 2021, non versés dans une série : structure du capital (p. 15 : 10,5 MD, État 0 %,
  autres actionnaires publics 98,0 %), besoins de fonds propres de 2018 (p. 152-153, tableau 32),
  rang du résultat de 2018 (p. 28). Pas de figure budget : la CTF n'est pas dans la série des
  transferts par entreprise. Registre lu au corpus local (couche texte) : décrets n° 98-1172
  (tutelle), 89-876 (marchés, lu à l'image), 2005-3396 et 2017-653 (organigrammes), 2006-1002, 2009-3048 et 2018-790 (emplois
  fonctionnels), 2007-1330 (marchés), 2020-183 (tutelle du ministère de l'Énergie), 2020-1061
  (article 22 ter, articles 18 à 22 et 11 bis), arrêté du 18 août 2022 (calendrier des conseils).
  **Reste** :
  - texte de création de la société et garanties de l'État : non identifiés dans `jort_cache.db` ;
    plein texte du corpus 1994-2026, éditions française et arabe, parcouru le 29 octobre 2026
    (seuls les textes du registre, des nominations et des listes générales nomment la société) ; fascicules d'avant 1994 **sans couche texte, à l'image** ;
  - actionnaires publics de la CTF (l'édition LF 2021 ne les nomme pas) et contradiction entre les
    visas de la loi n° 85-78 (capital entièrement public) et les 2,0 % d'autres actionnaires ;
  - statut particulier du personnel (décret n° 99-2643, JORT n° 96 de 1999, p. 2533) : **publié
    en arabe seulement, édition arabe du corpus à lire** ; décrets n° 92-713 et 98-28, qui modifient
    le décret n° 89-876 : **dans le corpus local, à l'image**, non lus ;
  - transferts du budget à la CTF : annexe 8 et tableaux de transferts du rapport, à vérifier ;
  - jours de forage (grandeurs d'activité des fiches) : non relevés ; comptes publiés par la
    société : **à obtenir**.
- **STIR — section écrite le 28 octobre 2026** (`_energie.qmd` depuis l'ouverture du
  chapitre « L'énergie », même jour ; `#sec-ep-ge-stir`, figure `fig-ep-stir-budget` engendrée par `grandes_entreprises.figure
  ("stir_budget")` depuis trois séries du rapport sur les entreprises publiques : transferts
  2017-2022, résultats nets des classements, effectifs et charges de personnel 2016-2023 ; le
  principal de dette garantie payé par l'État 2013-2016, `cdc-cloture-entreprises-publiques`, est
  dit dans le texte avec ses pages et renvoie à `tbl-ep-cdc-garantie`).
  **Fiche du ministère des Finances versée le 28 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-stir`) :
  LF 2022 p. 62, LF 2024 p. 95, LF 2025 p. 70, lues à l'image et recoupées avec la couche texte ;
  figure `fig-ep-stir-fiches` et tableaux `tbl-ep-stir-fiche-a` et `-b`, repliés ; texte : subvention
  d'exploitation, fonds propres et passifs, dette par créancier. Écarts imprimés : dette totale
  de l'édition LF 2022 inférieure de 50,0 MD à la somme des créanciers, les trois années ;
  fonds propres de fin 2020 à −1 282,9 MD (LF 2022) et 171,2 MD (LF 2024) ; renvoi de l'édition
  LF 2024 sur les 624,5 MD de recettes du stock de réserve (2021).
  Registre `tbl-ep-registre-stir`, lu au corpus local : loi n° 60-11 (convention avec l'ANIC,
  p. 1005, image), loi n° 75-81 (rachat des actions du groupe ENI, p. 2852, image ; intitulé daté
  du 20 décembre, formule finale du 30 décembre 1975), décret n° 77-467 (nom, objet, tutelle,
  p. 1279-1281, image), lois n° 2015-9, 2017-12, 2020-10 et décret-loi n° 2023-19 (garanties et
  convention cadre avec la Société internationale islamique de financement du commerce ; 2023 à
  l'édition arabe, p. 764, l'édition française étant absente du corpus et de pist.tn), décret
  gouvernemental n° 2016-1393 (compensation des créances réciproques, 152,0 MD, p. 3797).
  Plein texte du corpus 1994-2026, éditions française et arabe : aucune autre convention de
  garantie au profit de la STIR ; 384 fascicules de 1994-2012 sans couche texte exploitable.
  **Reste** :
  - éditions LF 2020 (p. 88) et LF 2021 (p. 79) : comptes de la STIR dans la prose, non versés
    (même règle que pour les autres entreprises ; **lisibles dans le corpus de `tunisia-data`**) ;
  - fonds propres de fin 2020 : l'écart entre l'édition LF 2022 (−1 282,9 MD) et l'édition
    LF 2024 (171,2 MD) n'est pas expliqué par le rapport ; les comptes publiés de la STIR le
    trancheraient ;
  - comptes publiés par la STIR (rapports annuels, états financiers) : **à obtenir** ;
  - le prêt garanti dont l'État paie le principal de 2013 à 2016 : non identifié ;
  - augmentations de capital de la société tuniso-italienne (loi n° 61-35, décret-loi n° 61-11
    et loi n° 61-44, loi n° 62-29) : **dans le corpus local, à l'image**, non lues ;
  - décrets n° 89-1197 et 91-178 (article 5 du décret n° 77-467, composition du conseil) : lus à
    l'OCR, non versés au registre ; décret n° 99-1304 (organigramme), non lu ;
- **SNDP — section écrite le 29 octobre 2026** (`_energie.qmd`, `#sec-ep-ge-sndp`, après la
  STIR et son TODO ; aucune ligne de la SNDP dans les séries des transferts du budget : figure
  de la fiche seule). **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-sndp`) :
  LF 2022 p. 62 (page du fichier 61, tableau 26, sous la STIR), LF 2024 p. 96 (fichier 97),
  LF 2025 p. 68, lues à l'image à 300 dpi et recoupées avec la couche texte ; figure
  `fig-ep-sndp-fiches` et tableaux `tbl-ep-sndp-fiche-a` et `-b`, repliés. Écarts imprimés
  déclarés : LF 2024, résultat d'exploitation 2020 (−30,6 pour −31,0) ; LF 2025, produits
  d'exploitation 2022 (−0,5) et bilan 2023 provisoire (actifs 1 930 pour 1 709,0 de passifs et
  de fonds propres, +221,0). Écarts entre éditions dits dans le texte : résultat net 2019
  (−5,9 MD dans la fiche LF 2022, +7,9 MD dans le classement LF 2023), effectif 2020 (1 133 en
  LF 2022, 1 151 en LF 2024).
  Registre `tbl-ep-registre-sndp`, lu au corpus local : décrets-lois n° 63-4 (convention avec
  l'AGIP, constitution d'AGIP S.A. Tunis à parité, p. 212, image) et n° 63-5 (75 000 dinars,
  p. 214, image), loi n° 69-20 (425 000 dinars, p. 344, image), décret n° 77-466 (nom, objet,
  tutelle, p. 1277-1279, image), loi n° 82-59 (5 MD, p. 1489, image), décret n° 85-775
  (règlement des consommations de carburants des administrations, p. 813-814, image), décret
  n° 89-1196 (conseil d'administration, p. 1348, image), décret n° 2001-372 (abrogation du
  décret n° 77-466, p. 247, couche décalée décodée), décrets n° 2005-2753 et 2011-719
  (article 52 du code d'incitation aux investissements, GPL à Radès et à Ghannouch). Le rachat
  de 1975 renvoie à la ligne `r-ep-stir-1975` du registre de la STIR (loi n° 75-81).
  Plein texte des fascicules français 1994-2012, couche décalée décodée : aucune garantie de
  l'État au profit de la SNDP ; 7 fascicules sur 1 962 sans couche texte exploitable, non parcourus.
  **Reste** :
  - éditions LF 2020 (p. 91) et LF 2021 (p. 82) : comptes de la SNDP dans la prose, non versés
    (**lisibles dans le corpus de `tunisia-data`**) ; ventes de produits pétroliers des fiches,
    non relevées ;
  - comptes publiés par la SNDP (rapports annuels, états financiers) : **à obtenir** ; ils
    trancheraient le signe du résultat net de 2019 ;
  - lois n° 63-5 et 63-6 (ratification des décrets-lois de 1963, JORT n° 19 de 1963, p. 505),
    décret n° 80-165 (statut du personnel, JORT n° 17 de 1980, p. 849) : **dans le corpus local,
    à l'image**, non lus ; décret n° 99-2645 (statut particulier) : publié en arabe seulement,
    **édition arabe du JORT n° 96 de 1999 à lire** ; organigrammes et emplois fonctionnels
    (n° 2001-370, 2001-371, 2007-448, 2008-3909, 2009-3085, 2021-278), non lus ;
  - garanties : les fascicules d'avant 1994 (sans couche texte) n'ont été parcourus que par
    leurs intitulés ; les éditions arabes et 2013-2026, par le seul cache plein texte.
- **Office des céréales — section écrite le 28 octobre 2026** (`_offices.qmd`,
  `#sec-ep-ge-oc`, avant la SNCFT : l'Office est le deuxième bénéficiaire des transferts après la
  STIR). Figures `fig-ep-oc-budget` (`grandes_entreprises.figure("oc_budget")` : transferts
  2017-2022, résultats nets des classements, effectifs et charges de personnel 2016-2023) et
  `fig-ep-oc-fiches` ; tableaux repliés `tbl-ep-oc-fiche-a` et `-b`. **Fiche du ministère des
  Finances versée le 28 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-office-cereales`) : LF 2022 p. 75, LF 2024 p. 111,
  LF 2025 p. 89, lues à l'image et recoupées avec la couche texte ; identités sans écart à
  déclarer. Écarts entre éditions dits dans le texte : transferts provisoires très révisés (2020 :
  3 MD puis 1 745 et 1 726,5 MD ; 2021 : 213,5 puis 1 687,5 MD) ; comptes de 2022, « réalisés »
  dans les deux éditions, révisés de 3 à 6 % au bilan. Principal de l'emprunt obligataire payé par
  l'État en 2010 et 2011 (15,0 MD par an, Cour des comptes) dit à part. Registre
  `tbl-ep-registre-oc`, lu au corpus local : décret-loi n° 62-10 (création, monopole, subvention
  du compte des importations, p. 371-373, image), décret-loi n° 70-7 (nom, monopole des
  importations et de l'achat à la production, p. 1267, image), loi n° 86-67 (conseil
  d'administration, p. 788, image), loi de finances pour 1997, art. 17 (garantie de 980 MD des
  dettes des offices des céréales et de l'huile envers la BNA, p. 2580), décret n° 2000-2578
  (organisation, tutelle, p. 2907-2909, OCR), décrets-lois n° 2022-64 (garantie BERD, 150,5 M€,
  p. 2711) et 2023-4 (garantie BEI, 150 M€, p. 273 ; mention de dépôt fautive dans l'édition
  française, date de l'édition arabe retenue), décret n° 2023-35 (compensation des créances
  réciproques, 690,9 MD, p. 160-161), décret-loi n° 2025-2 (prix fixés par arrêté conjoint,
  p. 2420). Glossaire : `office-cereales`.
  **Reste** :
  - éditions françaises LF 2020 (p. 107) et LF 2021 (p. 104) : comptes dans la prose, non versés
    (**lisibles dans le corpus de `tunisia-data`**) ; grandeurs d'activité des fiches (ventes et
    achats de céréales) non relevées ;
  - comptes publiés par l'Office (rapports annuels, états financiers) : **à obtenir** ;
  - textes **dans le corpus local, non lus** : loi n° 62-18 (ratification, 1962 n° 27, p. 619),
    décret n° 63-378 (monopole des pommes de terre), arrêté du 27 avril 1964 (visa du contrôleur
    financier), loi n° 70-47, décrets n° 87-102 (conseil) et 87-978 (exercice comptable,
    1987 n° 53, p. 938), décrets de ratification n° 2022-729 et 2023-126, statut du personnel
    (décrets n° 74-4, 2000-2356, 2009-2650, 2013-4706), organigramme (décrets n° 2002-1197 et
    2019-339), loi n° 82-10 (prêt de la BIRD pour le stockage des céréales) ;
  - l'emprunt obligataire dont l'État paie le principal en 2010 et 2011 : texte non identifié ;
  - garanties dans les lois de finances : parcourues en plein texte les lois de finances de type
    « loi » 1993-2026 (édition française) et les lois de finances pour 2022 et 2023 (décrets-lois,
    édition arabe) ; restent les décrets-lois de finances rectificatives, la loi de finances
    rectificative n° 2023-12 et les fascicules sans couche texte ;
- **SONEDE et ONAS — sections écrites le 28 octobre 2026** (`_eau_communications.qmd`,
  `#sec-ep-ge-sonede` et `#sec-ep-ge-onas`, après l'Office des céréales et avant la SNCFT, dans
  l'ordre des transferts de 2022 ; restent dans « Les autres entreprises » : deux entreprises ne
  font pas un chapitre « L'eau », note de chantier, § 10). Figures `fig-ep-{sonede,onas}-budget`
  et `fig-ep-{sonede,onas}-fiches`, tableaux repliés `tbl-ep-{sonede,onas}-fiche-a` et `-b`.
  **Fiches du ministère des Finances versées le 28 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiches-sonede-onas`) :
  SONEDE LF 2022 p. 75, LF 2024 p. 113, LF 2025 p. 88 ; ONAS p. 85, 126 et 103 ; lues à l'image
  (300 dpi) et retrouvées dans la couche texte. SONEDE : bilan de 2022 (LF 2024) et de 2023
  (LF 2025) remplacé par une note ; 2019 de l'édition LF 2022 en comptes non approuvés. Écarts
  imprimés déclarés : ONAS 2018 (charges d'exploitation imprimées négatives), SONEDE 2022 en
  LF 2024 (produits à 0,2 près). Registres `tbl-ep-registre-sonede` (loi n° 68-22, image ; loi
  n° 72-37, image ; décret n° 73-227, image ; loi n° 76-21, image ; loi n° 2019-48, fonds de
  dotation ; lois n° 2018-3, édition arabe, 2021-15, 2021-17, 2021-33 ; arrêté du 28 février 2024 sur le prix de l'eau) et
  `tbl-ep-registre-onas` (loi n° 74-73, image ; décret n° 75-201, image ; loi n° 93-41, image ;
  décret n° 95-1139 ; décret n° 2001-2001, OCR ; décret n° 2002-524, OCR ; loi n° 2004-70, OCR ;
  loi n° 2007-35 ; arrêté du 12 octobre 2022 sur les redevances ; lois n° 2016-2, 2017-22, 2017-32,
  2017-33, 2019-57 et 2019-58, édition arabe, 2023-10, 2024-36). Recherche des garanties et des
  compensations : intitulés français et arabes de `jort_cache.db` (aucune compensation de créances
  pour les deux entreprises). Glossaire : `sonede`, `onas`.
  **Reste** :
  - séries du prix de l'eau par tranche (arrêtés de 1968 à 2022) et des redevances
    d'assainissement (arrêtés de 1982 à 2018) : **dans le corpus local** (texte pour les années
    récentes, image avant 1995), à établir, puis à verser dans `openfisca-tunisia` si le modèle
    doit les porter ;
  - nature des transferts du budget à la SONEDE et à l'ONAS (investissement ou exploitation) :
    le tableau des transferts ne le dit pas ; lois de finances, budget du ministère de
    l'Agriculture et du ministère de l'Environnement ;
  - décret n° 75-492 (perception des redevances par la SONEDE, 1975 n° 52, p. 1596) : **scan peu
    lisible**, connu par le décret n° 2002-524 ; loi n° 2001-14 (modification de la loi n° 93-41) :
    dans le corpus, non lue ;
  - garanties antérieures à 2016-2018 (une vingtaine de textes par entreprise, liste dans les
    commentaires du chapitre) : dans le corpus, non lues ;
  - éditions françaises LF 2020 (SONEDE p. 116, ONAS p. 125) et LF 2021 (p. 109-111 et 118) :
    comptes dans la prose, non versés ; grandeurs d'activité des fiches (eau facturée, redevances,
    raccordements) non relevées ;
  - comptes publiés et contrats-programmes des deux entreprises : **à obtenir**.
- **CPG et GCT — sections écrites le 28 octobre 2026** (`_industrie.qmd`,
  `#sec-ep-ge-cpg` et `#sec-ep-ge-gct`, après l'ONAS et avant la SNCFT ; deux entreprises du
  phosphate ne font pas un chapitre, note de chantier, § 10). Figures `fig-ep-{cpg,gct}-fiches`
  (pas de figure du budget : le tableau des transferts de l'édition LF 2022, p. 105-106, leur donne 0
  de 2018 à 2020), tableaux repliés `tbl-ep-{cpg,gct}-fiche-a` et `-b`. **Fiches du ministère des
  Finances versées le 28 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiches-cpg-gct`) : LF 2022 p. 63 (les deux), LF 2024 p. 97
  (les deux), LF 2025 p. 71 (CPG) et 72 (GCT) ; lues à l'image (300 dpi), chaque ligne retrouvée
  entière dans la couche texte. GCT : exercice 2023 remplacé par une note dans l'édition LF 2025.
  Écarts imprimés déclarés : CPG 2019 (dette totale à 0,32 près), GCT en LF 2022 (montants entiers,
  écarts d'une unité). Lus sur les pages, sans série : contribution aux ressources propres de
  l'État (LF 2022 p. 103 ; LF 2024 p. 151, CPG seule), dettes et créances croisées de fin 2023
  (LF 2025 p. 118-123), part de l'État dans les bénéfices 2021-2023 (CPG, 50 MD, p. 126).
  Registres `tbl-ep-registre-cpg` (décret-loi n° 60-25, image ; loi n° 93-68, image ; loi
  n° 96-31 ; loi n° 2000-13, image ; loi n° 2005-109 ; lois de finances pour 2021, art. 40, et
  pour 2026, art. 40, édition arabe ; loi n° 2026-17) et `tbl-ep-registre-gct` (loi n° 93-79,
  image ; décret n° 97-1840 ; loi n° 99-84, image ; décret n° 2000-2947, image ; lois n° 2009-45,
  2012-15, 2014-2, 2017-17, 2017-18, 2021-30 ; décret-loi n° 2023-20, édition arabe ; lois
  n° 2026-18 et 2026-19). Recherche par les intitulés français et arabes de `jort_cache.db`.
  Glossaire : `cpg`, `gct`.
  **Reste** :
  - CPG : convention de 1897 et textes antérieurs à 1956 (**hors du corpus local**) ; décret
    beylical du 1er janvier 1953 sur les mines (article 87) ; forme juridique, capital et part de
    l'État ; augmentations de capital de 1970 à 1992 et garanties de 1974 à 1990 (**dans le
    corpus, image**, liste dans le commentaire de la section) ;
  - GCT : texte de constitution du Groupe (regroupement de sociétés, dont la SIAPE et la SAEPA)
    **non identifié** par les intitulés ; lois de capital des sociétés du groupe, 1972-1990 (**dans
    le corpus, image**) ;
  - séries à verser dans `tunisia-data` : contribution aux ressources propres de l'État par
    entreprise (tableau 35 de LF 2022, tableau 42 de LF 2024), dettes et créances croisées de fin
    2022 (LF 2024, tableaux 38 et 39) et de fin 2023 au-delà des dix premières ;
  - grandeurs d'activité des fiches (production et ventes en millions de tonnes) non relevées ;
    éditions françaises LF 2020 (CPG p. 78, GCT p. 80) et LF 2021 (p. 89 et 92) non versées ;
  - prêts à l'État pour les lignes ferroviaires du phosphate (lois n° 2024-31, 2025-12, 2026-7) :
    non lus, à rattacher à la SNCFT ou aux transports ;
  - comptes publiés et rapports annuels des deux entreprises : **à obtenir**.
- **El Fouladh — section écrite le 29 octobre 2026** (`_industrie.qmd`,
  `#sec-ep-ge-fouladh`, en fin de chapitre). Figures `fig-ep-fouladh-budget` (transferts du budget
  des éditions LF 2021 à LF 2023 : 10,0 MD en 2019, 150 MD pour 2020 dans l'édition LF 2021 ramenés
  à 0 ensuite) et `fig-ep-fouladh-fiches`, tableaux repliés `tbl-ep-fouladh-fiche-a` et `-b`.
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-elfouladh`) :
  LF 2022 p. 63, LF 2024 p. 92 (tableau 31 ; 2022 « متوقع », prévu), LF 2025 p. 71 ; lue à l'image
  (300 dpi), chaque ligne retrouvée entière dans la couche texte. Écarts imprimés déclarés :
  produits d'exploitation de 2021 et 2022 en LF 2024 (0,2 près). Lus sur les pages, sans série :
  dettes et créances croisées de fin 2023 (LF 2025 p. 118-123). Paiements de dette garantie par
  la Cour des comptes (gestions 2013-2015) repris de la série `cdc-cloture-entreprises-publiques`.
  Registre `tbl-ep-registre-fouladh` (décret-loi n° 62-22 et loi n° 62-59, lois n° 65-42, 72-75
  et 83-77, toutes à l'image ; loi de finances pour 2013, art. 16 ; loi n° 2015-5 ; lois de
  finances pour 2020, art. 50, et pour 2025, art. 61, extraits français du corpus ; décret
  n° 2025-423). Glossaire : `el-fouladh`.
  **Reste** :
  - statuts et acte de constitution (1962), forme juridique, capital actuel et part de l'État :
    non lus ;
  - décrets n° 88-1988 (commission d'achat), 2002-2862 (statut du personnel), 2013-1289
    (organigramme), 2015-1127 (emplois fonctionnels), décret de ratification n° 2015-64, décret
    n° 2003-188 : **dans le corpus** (2002, 2013, 2015 avec couche texte ; 1988 et 2003 à vérifier),
    non lus ;
  - texte instituant la taxe à l'exportation des déchets de fer (270 D la tonne d'après l'édition
    LF 2021, p. 96) : à identifier ;
  - série des transferts : ligne d'El Fouladh de l'édition LF 2024 (p. 155, 0,0) absente de
    `entreprises-publiques-transferts-par-entreprise` ;
  - grandeurs d'activité (production et ventes en tonnes) non versées ; éditions françaises
    LF 2020 (p. 97) et LF 2021 (p. 96) non versées ;
- **Ciments de Bizerte — section écrite le 29 octobre 2026** (`_industrie.qmd`,
  `#sec-ep-ge-cimbiz`, en fin de chapitre). Figures `fig-ep-cimbiz-budget` (transferts de
  0,068 à 0,1 MD de 2018 à 2020, LF 2022 p. 105, LF 2023 p. 200, LF 2024 p. 155) et
  `fig-ep-cimbiz-fiches`, tableaux repliés `tbl-ep-cimbiz-fiche-a` et `-b`. **Fiche du ministère
  des Finances versée le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-cimbiz`) : LF 2022 p. 63, LF 2024 p. 93, LF 2025 p. 69 ;
  lue à l'image (300 dpi), chaque ligne retrouvée entière dans la couche texte. Écart imprimé
  déclaré : charges d'exploitation imprimées négatives dans l'édition LF 2024 ; signe « − »
  imprimé après le nombre dans l'édition LF 2025 (2023), que le script de `tunisia-data` lit
  désormais. Registre `tbl-ep-registre-cimbiz` (arrêtés du 10 octobre 1959 et du 22 août 1974,
  image ; lois n° 75-30 et 76-40, image ; loi n° 2002-91, couche texte décodée). Recherche par
  les intitulés de `jort_cache.db` et en plein texte des fascicules français de 2007 à 2026.
  Glossaire : `ciments-bizerte`. Module de figures : graduations décimales de `_axe_md` quand
  l'axe est court ou la graduation non entière (vaut pour toutes les figures du module).
  **Reste** :
  - textes antérieurs à 1956 (convention du 20 mars 1950, décret du 23 mars 1950, cahier des
    charges du 30 novembre 1950, création de la Société des Ciments Portland de Bizerte) : **hors
    du corpus local** ;
  - loi n° 59-132 (comité de gestion de la Caisse de compensation des ciments), décret-loi de 1973
    sur la taxe compensatrice sur le ciment, décrets d'expropriation (n° 79-310, 88-1756,
    2006-1548), statut du personnel (n° 99-1944), organigramme (n° 2005-1611), emplois
    fonctionnels (n° 2006-396), textes de 2015 et 2023 sur la dépollution du lac de Bizerte :
    **dans le corpus**, non lus ;
  - continuité entre la Société des Ciments Portland de Bizerte (1975) et la société des Ciments
    de Bizerte (1976) : texte à identifier ; part de l'État dans le capital, forme juridique,
    cotation : non établies ; hausse des fonds
    propres de fin 2020 à fin 2021 (30,6 à 85,9 MD) à expliquer ;
  - grandeurs d'activité des fiches (clinker et ciment en tonnes, revenus de LF 2022) non
    relevées ; éditions françaises LF 2020 et LF 2021 non versées ;
- **Les Ciments d'Oum El Kélil — section écrite le 29 octobre 2026** (`_industrie.qmd`,
  `#sec-ep-ge-cimoek`, en fin de chapitre, après le GCT). Figure `fig-ep-cimoek-fiches` (pas de
  figure du budget : les tableaux des transferts lui donnent 0, LF 2022 p. 106 pour 2018-2020 et
  LF 2024 p. 155 pour 2020-2022), tableaux repliés `tbl-ep-cimoek-fiche-a` et `-b`. **Fiches du
  ministère des Finances versées le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-cimoek`, à fusionner avant ce chapitre) : LF 2022 p. 63,
  LF 2024 p. 94, LF 2025 p. 74 ; lues à l'image (300 dpi) et retrouvées dans la couche texte.
  Écarts imprimés déclarés : dette totale de LF 2022 supérieure à la somme des créanciers (22,1 et
  17,7 MD). Cases vides : dette de fin 2020 (LF 2022), total des passifs 2022-2023 (LF 2025). Lus sur
  les pages, sans série : contribution aux ressources propres de l'État (LF 2022 p. 103 ; LF 2024
  p. 152), dettes et créances croisées de fin 2022, nulles (LF 2024 p. 142 et 146), commentaire du
  rapport (LF 2024 p. 101-102 ; LF 2025 p. 87), tutelle (LF 2024 p. 183). Registre
  `tbl-ep-registre-cimoek` : arrêté du 12 septembre 1978 (ligne de 90 kV, image) ; loi
  n° 2000-36 (assainissement financier, couche texte décodée ; dépôt au gouvernorat le 24 mars
  2000). Décret gouvernemental n° 2020-1061 (article 22 ter) : renvoi à `@tbl-ep-22ter`. Recherche
  par les intitulés français et arabes de `jort_cache.db` et le plein texte du miroir iort.
  Glossaire : `cimoek`.
  **Reste** :
  - texte de constitution de la société, forme juridique, capital et part de l'État **non
    identifiés** ; loi n° 79-24 (« Société des Ciments Tunisiens », lue à l'image, JORT n° 31 de
    1979, p. 1300) : ne nomme pas la cimenterie, rattachement à établir ;
  - textes **dans le corpus local, non lus** : décrets n° 99-1739 (statut du personnel), 2009-3047
    (organigramme), 2010-2066 (emplois fonctionnels), arrêté du 17 juin 2015 (conservation des
    documents, intitulé arabe) ;
  - séries à verser dans `tunisia-data` : contribution aux ressources propres et dettes et
    créances croisées (voir l'entrée CPG et GCT) ; grandeurs d'activité des fiches (production de
    ciment et de chaux) non relevées ; classement des résultats d'exploitation négatifs de LF 2025
    (p. 20) non repris ; éditions françaises LF 2020 et LF 2021 non versées ;
  - comptes publiés et rapports annuels de la société : **à obtenir**.
- **SNCPA — section écrite le 29 octobre 2026** (`_industrie.qmd`, `#sec-ep-ge-sncpa`,
  après le GCT). Figures `fig-ep-sncpa-budget` (transferts 2017-2022, résultat net des
  classements, effectif et charges de personnel) et `fig-ep-sncpa-fiches`, tableaux repliés
  `tbl-ep-sncpa-fiche-a` et `-b`. **Fiche du ministère des Finances versée le 29 octobre 2026**
  dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-sncpa`,
  code `sncpa`) : LF 2022 p. 63, LF 2024 p. 93, LF 2025 p. 73 ; lues à l'image (300 dpi) et
  retrouvées dans la couche texte. LF 2025 : bilan de 2022-2023 et résultat de 2023 sous une note,
  seul l'effectif de 2023 imprimé. Écart imprimé déclaré : résultat d'exploitation 2019 (LF 2022).
  Lus sur les pages, sans série nouvelle : dettes envers l'État de fin 2023 (320,0 MD, LF 2025
  p. 118), paiements de dette garantie de la Cour des comptes (série déjà versée, 2012-2018).
  Registre `tbl-ep-registre-sncpa` (décret du 8 janvier 1957, fascicule téléchargé de pist.tn,
  absent du corpus local ; arrêté du 29 juillet 1959 ; lois n° 60-3, 84-19, 85-30, 88-86 ; décret
  n° 80-780 avec l'édition arabe ; tous à l'image ; loi n° 95-86 ; loi de finances pour 2026,
  art. 64, édition arabe). Glossaire : `sncpa`.
  **Reste** :
  - création de la Société nationale tunisienne de cellulose et de la Société tunisienne de papier
    alfa, et leur réunion en SNCPA (entre 1980 et 1984) : textes **non identifiés** par les
    intitulés de `jort_cache.db` ; forme juridique, capital et part de l'État : non lus ;
  - arrêté du 31 janvier 1981 (JORT n° 8, p. 240-245), décret n° 88-283 (JORT n° 18 de 1988,
    p. 383-384), décret n° 2000-2366 (JORT n° 86 de 2000, p. 2606) : **dans le corpus, non lus** ;
  - objet des transferts de l'annexe 9 (9,3 à 35,0 MD) : l'annexe 8, bloc du ministère du
    Commerce, ne donne que 0,061 à 3,555 MD ; Cour des comptes, gestion 2018 : 0 au tableau,
    709 962 dinars dans le texte ;
  - grandeurs d'activité des fiches (production et ventes en tonnes) non relevées ; éditions
    françaises LF 2020 (p. 100) et LF 2021 (p. 99) non versées ; comptes publiés : **à obtenir**.
- **Tunisie Autoroutes et Transtu — sections écrites le 28 octobre 2026** (`_autres_entreprises.qmd`,
  `#sec-ep-ge-autoroutes` et `#sec-ep-ge-transtu`, après l'ONAS et avant la SNCFT, dans l'ordre des
  transferts de 2022 : Tunisie Autoroutes 170,0 MD, Transtu 147,5 MD, SNCFT 129,8 MD). Figures
  `fig-ep-{autoroutes,transtu}-budget` et `fig-ep-{autoroutes,transtu}-fiches`, tableaux repliés
  `tbl-ep-{autoroutes,transtu}-fiche-a` et `-b`. **Fiches du ministère des Finances versées le
  28 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiches-transtu-autoroutes`, à fusionner avant ce chapitre) : Transtu LF 2022 p. 55,
  LF 2024 p. 83, LF 2025 p. 60 ; Tunisie Autoroutes p. 80, 120 et 95 ; lues à l'image (300 dpi) et
  retrouvées dans la couche texte. Transtu : bilan de 2021-2022 (LF 2024) remplacé par une note
  (états financiers 2020-2022 non approuvés), seuls les résultats reportés imprimés en LF 2025 ;
  fonds propres de 2020 (1 110 MD, LF 2024) lus par l'ordre des colonnes de LF 2025, sans total
  pour les contrôler. Tunisie Autoroutes : subvention d'exploitation de 320,2 MD en 2022 (avances
  de l'État pour les échéances de prêts extérieurs de 2021 et 2022, note de LF 2025) ; 2021 retraité.
  Registres `tbl-ep-registre-autoroutes` (décret n° 95-720, concession ; décrets n° 96-2263,
  2003-1118 et 2014-4203, péage Hammam-Lif–M'saken ; loi de finances pour 1999, art. 16-17, et
  pour 2019, art. 10, fonds de développement des autoroutes ; lois n° 99-50, 2002-96, 2006-3,
  2010-57 et 2019-75 (édition arabe), capital ; lois n° 99-47, 2001-40, 2002-72, 2003-4, 2010-5,
  2012-6 et décrets-lois n° 2011-65, 2011-111, garanties ; décret n° 2025-218, prorogation) et
  `tbl-ep-registre-transtu` (décret-loi n° 63-8, image ; loi n° 95-3 ; loi n° 2003-33, image,
  avec l'édition arabe p. 1432 ; décret n° 2003-2407 ; loi n° 2005-73, image ; loi n° 2020-40 ;
  décret-loi n° 2023-13, édition arabe). Glossaire : `tunisie-autoroutes`, `transtu`.
  **Reste** :
  - **chapitre « Les transports » ouvert le 29 octobre 2026** (`_transports.qmd`, `#sec-ep-transports`) : Tunisie Autoroutes, Transtu, SNCFT et Tunisair, déplacées de « Les autres entreprises » sans changement de texte ; ancres conservées. L'ATTT y est ajoutée le 29 octobre 2026 (voir l'entrée ATTT). Reste dans « Les autres entreprises » : Tunisie Autoroutes relève du ministère de l'Équipement (dit dans « La source » du chapitre) ; l'Office de l'aviation civile et des aéroports, la CTN et l'OMMP, au tableau du ministère du Transport, n'ont pas de fiche versée ;
  - **chapitre « Les transports » ouvert le 29 octobre 2026** (`_transports.qmd`, `#sec-ep-transports`) : Tunisie Autoroutes, Transtu, SNCFT et Tunisair, déplacées de « Les autres entreprises » sans changement de texte ; ancres conservées. Reste dans « Les autres entreprises » : Tunisie Autoroutes relève du ministère de l'Équipement (dit dans « La source » du chapitre) ; la CTN et l'OMMP, au tableau du ministère du Transport, n'ont pas de fiche versée ; l'Office de l'aviation civile et des aéroports a sa section depuis le 29 octobre 2026 (entrée ci-dessous) ;
  - **chapitre « Les transports » ouvert le 29 octobre 2026** (`_transports.qmd`, `#sec-ep-transports`) : Tunisie Autoroutes, Transtu, SNCFT et Tunisair, déplacées de « Les autres entreprises » sans changement de texte ; ancres conservées. Reste dans « Les autres entreprises » : Tunisie Autoroutes relève du ministère de l'Équipement (dit dans « La source » du chapitre) ; l'Office de l'aviation civile et des aéroports et la CTN, au tableau du ministère du Transport, n'ont pas de fiche versée ; l'OMMP a la sienne depuis le 29 octobre 2026 (entrée suivante) ;
  - **chapitre « Les transports » ouvert le 29 octobre 2026** (`_transports.qmd`, `#sec-ep-transports`) : Tunisie Autoroutes, Transtu, SNCFT et Tunisair, déplacées de « Les autres entreprises » sans changement de texte ; ancres conservées. Reste dans « Les autres entreprises » : Tunisie Autoroutes relève du ministère de l'Équipement (dit dans « La source » du chapitre) ; l'Office de l'aviation civile et des aéroports et l'OMMP, au tableau du ministère du Transport, n'ont pas de fiche versée ; la CTN a sa section depuis le 29 octobre 2026 (ci-dessous) ;
  - Tunisie Autoroutes : acte de constitution (13 mai 1992 d'après le rapport LF 2020, p. 121) non
    identifié au JORT ; décrets de concession des autres sections (n° 2000-645, 2002-537,
    2004-1073, 2004-1074, 2016-256, 2019-661 à 2019-663) et de péage des autres sections (n° 97-1003,
    2003-1119, 2009-383, 2010-3222, 2014-4201, 2014-4202, 2014-4204, 2019-977, 2019-1066 et ses
    modificatifs de 2020 à 2022) **dans le corpus local, non lus** : une série du péage par
    section reste à établir ; écart entre la dette de LF 2020 (1 707,2 MD envers les bailleurs de
    fonds, 2018) et celle de LF 2022 (325,7 MD) non expliqué ;
  - Transtu : création de la Société du métro léger de Tunis, non identifiée ; lois d'augmentation
    du capital de la SNT (1974-1982), décret n° 2006-433 (concession du domaine public
    ferroviaire), cahier des charges de la loi n° 2003-33 : **dans le corpus local, non lus** ou
    non identifiés ; prise en charge par l'État des dettes envers la SNDP (145,3 MD, 2017) et AGIL :
    texte non identifié ; transferts du rapport sur les entreprises publiques et du rapport sur
    les transferts et les garanties non concordants (2017 : 154,4 contre 287,8 MD) ;
  - éditions françaises LF 2020 et LF 2021 : comptes des deux entreprises dans la prose, non
    versés ; grandeurs d'activité (voyageurs, trafic) non relevées ; comptes publiés des deux
    entreprises : **à obtenir**.
- **Office de la marine marchande et des ports (OMMP) — section écrite le 29 octobre 2026**
  (`_transports.qmd`, `#sec-ep-ge-ommp`, en fin de chapitre). Figure `fig-ep-ommp-fiches` (pas de
  figure du budget : l'Office n'est dans aucun tableau des transferts par entreprise du rapport) ;
  tableaux repliés `tbl-ep-ommp-fiche-a` et `-b`. **Fiche du ministère des Finances versée le
  29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-ommp`, à fusionner avant la PR du précis) : LF 2022 p. 54 (tableau 25 du ministère
  du Transport), LF 2024 p. 83, LF 2025 p. 58 ; lues à l'image et retrouvées dans la couche texte.
  Dette imprimée « 0 » envers chaque créancier (LF 2022) ; bilan non imprimé de 2021 à 2023 (états
  financiers non approuvés) ; écart imprimé déclaré (LF 2025, 2023, résultat d'exploitation −0,8).
  Registre `tbl-ep-registre-ommp` : lois n° 65-2 (image, et son rectificatif), 72-5, 80-34, 83-76,
  84-61 (image) ; décret n° 98-1385 ; loi n° 98-83 ; loi n° 98-109 (date de dépôt lue dans l'édition
  arabe du même numéro) ; décret n° 2000-2407 (police décalée, décodée) ; décret-loi n° 2021-10 et
  décret présidentiel n° 2021-248. `figures/grandes_entreprises.py` : `fig_fiche` fixe l'échelle du
  panneau de la dette quand la dette totale imprimée est nulle chaque année. Glossaire : `ommp`.
  **Reste** :
  - loi n° 91-94 (prêt de la KfW, JORT n° 82 de 1991, **scanné, à lire à l'image**) ; tarifs et
    redevances portuaires (décrets n° 70-588, 82-1386, 88-229, arrêtés de 1982 à 2007), statut du
    personnel (décrets n° 73-383, 99-1731), affiliation à la CNR (décret n° 72-263), conseil
    d'administration (décret n° 72-242), services concédables (décret n° 2002-135), organigramme
    (décret n° 2004-1029), code des ports maritimes (loi n° 99-25), protocoles de 2014 : **dans le
    corpus local, non lus** ;
  - loi n° 80-34 : montant du prêt de la BIRD non imprimé ; date de l'accord (8 février dans
    l'intitulé, 6 février dans l'article, à l'image) ; garantie de l'AFD datée du 3 juin 2021 par le
    décret-loi et du 3 juin 2020 par le décret de ratification : **édition arabe à lire** ;
  - part de l'État dans les bénéfices de l'Office par exercice (seul le cumul 2021-2023, 50 MD,
    est versé) ; transferts éventuels du budget, à chercher dans l'annexe 8 ; grandeurs d'activité
    (marchandises, passagers) non relevées ; éditions françaises LF 2020 et LF 2021 (prose) non
    versées ; régime fiscal propre : aucun texte identifié par les intitulés.
- **CTN — section écrite le 29 octobre 2026** (`_transports.qmd`, `#sec-ep-ge-ctn`, en fin de
  chapitre). Figures `fig-ep-ctn-budget` et `fig-ep-ctn-fiches`, tableaux repliés
  `tbl-ep-ctn-fiche-a` et `-b`, registre `tbl-ep-registre-ctn` (loi n° 59-34, image ; lois n° 75-29,
  77-35, 78-29, 80-87, 83-75, 84-60, capital, image ; décret-loi n° 76-3 et loi n° 76-88, lois
  n° 77-9 et 78-13, emprunts, image ; lois n° 96-72 et 98-27 (image), décret-loi n° 2011-74,
  garanties ; arrêté du 4 avril 2017, redevances portuaires ; loi de finances pour 2024, art. 42,
  édition arabe, suspension de TVA). Glossaire : `ctn`. **Fiche du ministère des Finances versée
  le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-ctn`) : LF 2022 p. 54, LF 2024 p. 82, LF 2025 p. 57 ; bilan non imprimé pour
  2021-2023 (comptes non approuvés) ; écart imprimé des produits de 2022 (LF 2024, 20,0) déclaré.
  **Reste** :
  - effectifs de l'édition LF 2022 (734 ; 698 ; 700) inférieurs d'environ 400 à ceux des autres
    éditions : cause à établir ;
  - capital de 126 MD (rapport LF 2020) pour 18,9 MD de souscriptions de l'État lues (1959-1984) :
    augmentations postérieures à 1984 non identifiées dans jort_cache.db ; statuts de 1959 visés,
    non publiés ;
  - date d'effet de la loi n° 98-27 : mention de dépôt du JORT n° 30 de 1998 à relever dans
    l'édition arabe ;
  - textes **dans le corpus local, non lus** : décrets n° 95-2435, 99-2046, 99-2047, 2000-2903,
    2002-1606, 2015-241, 2018-430 ; arrêtés de 1994, 1995, 2003, 2013 ;
  - prorogation de l'art. 42 de la loi de finances pour 2024 au-delà de 2026 : à vérifier ;
  - éditions françaises LF 2020 (p. 64-66) et LF 2021 : comptes dans la prose, non versés ;
    grandeurs d'activité (passagers, remorques) non relevées ; comptes publiés : **à obtenir**.
- **Tunisair et RNTA — sections écrites le 28 octobre 2026** (`_transports.qmd` pour Tunisair, `_offices.qmd` pour la RNTA`,
  `#sec-ep-ge-tunisair` et `#sec-ep-ge-rnta`, après l'ONAS et avant la SNCFT). La RNTA est la
  Régie nationale des **tabacs et des allumettes** (code `rnta` de toutes les séries, ministère des
  Finances), non une régie des transports. Figures `fig-ep-{tunisair,rnta}-budget` et
  `fig-ep-{tunisair,rnta}-fiches`, tableaux repliés `tbl-ep-{tunisair,rnta}-fiche-a` et `-b`.
  **Fiches du ministère des Finances versées le 28 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiches-tunisair-rnta`) :
  Tunisair LF 2022 p. 54, LF 2024 p. 81, LF 2025 p. 56 ; RNTA p. 50, 73 et 50 ; lues à l'image et
  retrouvées dans la couche texte. Tunisair : bilan non imprimé en LF 2024 et LF 2025 (comptes
  2020-2023 non approuvés), aucun exercice dit réalisé. RNTA : écarts imprimés déclarés (LF 2022 ;
  signes « − » omis en LF 2024 ; fonds propres hors résultat en LF 2025). Registres
  `tbl-ep-registre-tunisair` (lois n° 61-49, 74-70, 76-39, 77-16, 84-59, image ; lois de garantie
  n° 94-48, 94-49, 94-105, 94-106, 95-39, 95-107, 2001-121, 2002-88, 2015-27 à 2015-29 ; décret
  n° 2009-2211) et `tbl-ep-registre-rnta` (loi n° 64-57, image ; loi n° 70-23, image ; loi de
  finances pour 1971, art. 33, image ; loi de finances pour 1983, art. 37 et 38, image, qui abroge
  les exonérations de 1964 ; décret n° 88-67, image ; décret n° 2011-4396, édition arabe, image). Glossaire : `tunisair`, `rnta`.
  **Reste** :
  - dates de dépôt des JORT n° 38 de 1994, n° 104 de 1995 et n° 93 de 2011 (arabe) : **à lire à
    l'image** ;
  - Tunisair : décret du 18 juillet 1957 (JORT n° 59 de 1957, **absent du corpus local**, à
    obtenir) ; statuts, part de l'État au capital, introduction en bourse ; lois de garantie de 1971
    à 1992 (une quinzaine, liste dans le commentaire du chapitre) : **dans le corpus local**,
    scannées pour la plupart ; décrets n° 2015-154 à 2015-156 (édition arabe) ; Tunisair Express
    (textes non identifiés) ; rapport de la Cour des comptes sur la flotte (2018, au catalogue) ;
  - RNTA : loi n° 93-53 (son article de promulgation abroge à nouveau l'article 30 de la loi
    n° 64-57 ; lu à l'OCR, **à relire à l'image**) ; décrets n° 70-291, 74-917, 84-859, 85-1236
    et modificatifs, 2001-2123 ; organigrammes ; textes sur la quote-part des recettes versée au
    budget : **dans le corpus local**, non lus ; objet des transferts du budget de 2020 et 2022
    (annexe 8, bloc du ministère des Finances) ;
  - grandeurs d'activité des fiches (passagers, marchandises ; ventes et production de tabac) non
    relevées ; éditions françaises LF 2020 et LF 2021 : comptes dans la prose, non versés.
- **Agence technique des transports terrestres (ATTT) — section écrite le 29 octobre 2026**
  (`_transports.qmd`, `#sec-ep-ge-attt`, en fin de chapitre, après Tunisair). Figure
  `fig-ep-attt-fiches` (pas de figure du budget : transferts nuls, LF 2022 p. 106, LF 2023 p. 201,
  LF 2024 p. 155), tableaux repliés `tbl-ep-attt-fiche-a` et `-b`. **Fiche du ministère des
  Finances versée le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-attt`, code `attt`) : LF 2022 p. 55, LF 2024 p. 85,
  LF 2025 p. 59, lues à l'image (300 dpi) et retrouvées dans la couche texte. Écarts imprimés
  déclarés : bilans de 2022 (LF 2024, −6,7 MD) et de 2023 (LF 2025, +5,6 MD) déséquilibrés ;
  virgule arabe lue comme décimale (LF 2022). Lus sur les pages, sans série : contribution aux
  ressources propres de l'État (LF 2022 p. 102, LF 2023 p. 197, LF 2024 p. 151), dettes et
  créances croisées (LF 2023 p. 190 et 194, LF 2024 p. 142 et 146, LF 2025 p. 119 et 123).
  Registre `tbl-ep-registre-attt` : loi n° 95-61, décret n° 98-1375, loi n° 98-108, décrets
  n° 99-2048 (image des p. 1751-1752), 2000-166, 2000-2406, 2000-2782 et 2007-704 (fascicules
  français ; couche texte à police décalée décodée pour 1999 et 2000). Glossaire : `attt`.
  L'axe des montants des figures de fiches affiche une décimale pour une graduation non entière
  (`_axe_md`), ce qui ne change que les petits montants.
  **Reste** :
  - date de dépôt du JORT n° 104 de 1998 (loi n° 98-108, et lois n° 98-109 et 98-110 du même
    numéro) : **à lire à l'image** (absente de la couche texte et de la dernière page ;
    édition arabe sans couche texte) ;
  - ce que couvre la « contribution aux ressources propres de l'État » de l'agence (redevances,
    impôts et taxes collectés pour l'État) : **non établi** ; nature des « autres produits »
    d'exploitation, supérieurs aux recettes : états financiers de l'agence **à obtenir** ;
  - régime fiscal après l'abrogation de l'article 9 de la loi n° 95-61, article 38 de la loi de
    finances pour 1978 : **non lus** ; barème des redevances après 2007 : aucun modificatif
    identifié par les intitulés, à chercher en plein texte ;
  - textes **dans le corpus local, non lus** : décrets n° 95-2037, 97-789, 2000-148 et
    modificatifs (2005-1497, 2007-705, 2007-4102, 2021-82), 2002-1672, 2004-2191, 2011-4625
    (édition arabe) ; arrêtés du 8 juin 1999, du 7 septembre 2018 et du 27 mars 2023 ;
  - grandeurs d'activité des fiches (visites techniques, examens du permis, immatriculations)
    et ratio de couverture des charges (LF 2024 p. 165) non relevés.
- **Office de l'aviation civile et des aéroports (OACA) — section écrite le 29 octobre 2026**
  (`_transports.qmd`, `#sec-ep-ge-oaca`, en fin de chapitre, avant le commentaire de la SNCFT).
  Figure `fig-ep-oaca-fiches` (pas de figure budget : transferts nuls de 2018 à 2022), tableaux
  repliés `tbl-ep-oaca-fiche-a` et `-b`, registre `tbl-ep-registre-oaca`. **Fiche du ministère des
  Finances versée le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-oaca`, code `oaca`) : LF 2022 p. 54 (tableau 25), LF 2024
  p. 82, LF 2025 p. 59, lues à l'image (300 dpi) et retrouvées dans la couche texte. Écarts imprimés
  déclarés : dette totale de l'édition LF 2022 supérieure à la somme des créanciers (17,2 ; 18,7 ;
  29,2 MD) ; résultat d'exploitation 2020 à 0,9 près. Édition LF 2024 : subvention d'exploitation
  en case blanche, deux signes « − » absents (résultat après modifications 2020, reportés 2022).
  Registre : lois n° 70-30, 74-19, 77-11, 93-59 et 93-60 (image), décret n° 93-1154 (image, art. 1er
  à 8 et 18 à 28), décret n° 98-1374, loi n° 98-110 (dépôt lu sur l'édition arabe), décrets
  d'exonération des vols intérieurs n° 2001-1400, 2004-572, 2009-371, 2014-2235 et 2020-778, loi
  n° 2004-41, décrets n° 2007-1216 et 2007-1316 (concession TAV), loi n° 2009-51. Glossaire :
  `oaca`. Transferts (LF 2022 p. 106, LF 2024 p. 155), dividendes (LF 2025 p. 125-126), dettes
  envers l'État (LF 2025 p. 118) : lus sur les pages.
  **Reste** :
  - **dans le corpus local, non lus** : loi n° 74-34 (rectificatif, image) ; loi n° 66-79 (Régie
    des ports aériens) ; décrets n° 70-590, 72-264, 74-599, 99-1941, 2000-2926 ; décret n° 93-1154,
    art. 9 à 17, et modificatifs n° 95-1326, 2008-101, 2021-81 ; exonérations propres à des
    aéroports (décrets n° 97-230, 2000-947, 2002-3264, 2005-3239, 2008-3903, 2017-342, 2024-5) ;
    décret n° 2004-1342 et avenants d'Enfidha (n° 2013-1328, 2020-556, 2020-557) ; décret
    n° 2007-1686 ; code de l'aéronautique civile (loi n° 99-58) ;
  - exonération des vols intérieurs après 2023, compensation éventuelle par l'État, régime fiscal
    de l'Office (requête arabe à faire) : non établis ;
  - grandeurs d'activité (passagers, mouvements d'avions, fret) non relevées ; éditions françaises
    LF 2020 et LF 2021 : comptes dans la prose, non versés ; rapports annuels de l'Office : **à
    obtenir** ;
  - tranché le 30 octobre 2026 : décrets n° 98-1374 et 98-1385 (changements de dénomination de
    l'Office des ports aériens et de l'Office des ports nationaux) lus et portés au registre de
    `_annexe_liste.qmd` (`r-epl-1998-noms`), qui ne dit plus que la succession n'est pas établie.
- **Office national de l'huile — section écrite le 28 octobre 2026** (`_offices.qmd`,
  `#sec-ep-ge-onh`, après l'ONAS et avant la SNCFT, comme demandé ; l'intro du chapitre ne dit plus
  que les entreprises sont rangées dans l'ordre des transferts, l'ONH recevant plus que la SONEDE et
  l'ONAS). Figures `fig-ep-onh-budget` et `fig-ep-onh-fiches`, tableaux repliés `tbl-ep-onh-fiche-a`
  et `-b`. **Fiche du ministère des Finances versée le 28 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-onh`, code
  `office_huile`) : LF 2022 p. 75, LF 2024 p. 112, LF 2025 p. 89, lues à l'image (300 dpi) et
  retrouvées dans la couche texte. 2022 provisoire dans les deux éditions, fortement révisé (actifs
  280,0 puis 525,0 MD) ; bilan 2022 de l'édition LF 2024 déséquilibré de 145,0 MD (écart déclaré) ;
  total des passifs 2023 en case vide (LF 2025). Principal de dette garantie payé par l'État 2013-2023
  (Cour des comptes, 70,4 MD) dit à part. Registre `tbl-ep-registre-onh`, lu au corpus local :
  décret-loi n° 62-24 (création, p. 1075-1077, image) ; loi n° 69-51 (dissolution, p. 912, image) ;
  loi de finances pour 1970, art. 35 (reconstitution au 26 juillet 1969, p. 1503, image) ; décret-loi
  n° 70-13 (monopole, p. 1348-1349, image) ; loi n° 94-37 (fin du monopole) ; décret n° 94-1166
  (exportation libre hors quota de l'Union européenne) ; loi de finances pour 1995, art. 90 ; arrêté
  du 8 janvier 1996 ; décret n° 2000-2579 (couche texte décalée, décodée) ; loi n° 2006-52 (prêt
  GSM 102) ; décret n° 2011-4798 (édition arabe, image). Loi de finances pour 1997, art. 17 :
  renvoi au registre de l'Office des céréales. Glossaire : `onh`.
  **Reste** :
  - prêt garanti dont l'État paie le principal de 2013 à 2023 : **non identifié** ;
  - texte de la concession d'approvisionnement en huile végétale subventionnée : **non identifié** ;
  - textes **dans le corpus local, non lus** : loi n° 62-61, décret n° 68-19, loi n° 70-53, décret
    n° 71-337 et ses modificatifs, statut du personnel, organigramme, décret n° 2006-2455, décrets
    sur l'exportation dans le quota de l'Union européenne (2011-2022), arrêté du 4 décembre 2023 ;
  - éditions arabes 2012-2016 du JORT et environ la moitié de 2017-2026 sans couche texte : la
    recherche des garanties et compensations après 2011 n'y a pas porté (**OCR à faire**) ;
  - éditions françaises LF 2020 (p. 110-111) et LF 2021 (p. 106-107) : comptes et activité dans la
    prose, non versés ; grandeurs d'activité des fiches (huile végétale subventionnée en MD et en
    tonnes) non relevées ;
  - comptes publiés et contrat-programme de l'Office : **à obtenir**.
- **Office du commerce de la Tunisie — section écrite le 29 octobre 2026** (`_offices.qmd`,
  `#sec-ep-ge-otc`, en fin de chapitre ; intro et « La source » du chapitre mises à jour). Figures
  `fig-ep-otc-budget` et `fig-ep-otc-fiches`, tableaux repliés `tbl-ep-otc-fiche-a` et `-b`.
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-commerce`, code
  `office_commerce`) : LF 2022 p. 89, LF 2024 p. 130-131, LF 2025 p. 107, lues à l'image (300 dpi) et
  retrouvées dans la couche texte. Édition LF 2024 : colonne 2022 de l'état de résultat qui reproduit
  les variations 2021/2020 (imprimé tel quel, dit dans le texte et les légendes) ; « total des
  passifs » égal au total des actifs (écart déclaré ; la case de 2020 n'est pas tracée). Annexe 8
  (rapport sur les transferts) citée à part de l'annexe 9. Registre `tbl-ep-registre-otc`, lu au corpus
  local : décret-loi n° 62-6 et son rectificatif (image) ; loi n° 67-32 (image) ; loi n° 78-8 (crédit
  Citibank garanti, image) ; arrêté du 30 août 1989 (liste des produits de base, image) ; loi n° 90-1
  (image) ; décret n° 99-227 ; décrets n° 2017-346 (édition arabe) et 2018-178 (zone de Ben Guerdane) ;
  lois de finances pour 2021 (art. 23), 2024 (art. 21), 2025 (art. 35) et 2026 (art. 41), éditions
  arabes pour les trois dernières. Glossaire : `office-commerce`.
  **Reste** :
  - texte qui confie à l'Office l'importation des produits de base avant 1989 et fondement d'une
    exclusivité d'importation (sucre, café, thé) : **non identifié** sous les intitulés de jort_cache ;
    aucun statut de 1970-1971 sous ces intitulés ; recherche à mener dans les lois de finances, les
    textes du commerce extérieur et de la compensation ;
  - textes **dans le corpus local, non lus** : loi n° 62-14 (ratification ; dates de jort_cache
    incohérentes), décrets n° 65-335 et 74-184 et arrêtés de 1974 et 1976 (personnel), décrets
    n° 88-885 et 89-1647 (organisation), n° 99-1920, 2001-719, 2005-2456 ;
  - grandeurs d'activité des fiches (achats et ventes de produits de base) citées, non versées dans
    une série ; éditions françaises LF 2020 et LF 2021 : comptes dans la prose, non versés ;
  - comptes publiés et contrat-programme de l'Office : **à obtenir**.
- **Régie des alcools et Manufacture des tabacs de Kairouan — sections écrites le 29 octobre 2026**
  (`_offices.qmd`, `#sec-ep-ge-ra` et `#sec-ep-ge-mtk`, en fin de chapitre ; intro et « La source » du
  chapitre mises à jour). Figures `fig-ep-ra-budget`, `fig-ep-ra-fiches`, `fig-ep-mtk-budget`,
  `fig-ep-mtk-fiches`, tableaux repliés `tbl-ep-{ra,mtk}-fiche-a` et `-b`. **Fiches du ministère des
  Finances versées le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`,
  branche `donnees/fiche-ra`, codes `regie_alcools` et `mtk`) : LF 2022 p. 50 (les deux), LF 2024 p. 74
  (Régie) et 73 (MTK), LF 2025 p. 49 et 51, lues à l'image (300 dpi) et retrouvées dans la couche texte.
  Écarts déclarés : Régie, LF 2024, « total des passifs » égal au total des actifs (case de 2020 non
  tracée) ; MTK, LF 2024, fonds propres et reportés de 2020 sans le signe « − » ; MTK 2023, bilan à
  0,2 près. Explications des révisions citées d'après la prose de l'édition LF 2025 (p. 52 et 55).
  Registres `tbl-ep-registre-ra` et `tbl-ep-registre-mtk`, lus au corpus local à l'image : loi de
  finances pour 1975 (art. 43 à 46 et 82), décrets n° 75-65 et 88-68 ; loi n° 81-14, décret n° 81-526,
  loi de finances pour 1982 (art. 85), décret-loi n° 2011-108 (couche texte), décret n° 2011-4395
  (édition arabe), loi de finances complémentaire pour 2014 (art. 46). Glossaire : `regie-alcools`, `mtk`.
  **Reste** :
  - textes **dans le corpus local, non lus** : Régie, décrets n° 75-594, 77-503 et 2007-843, arrêtés
    des prix de cession des alcools (dernier : 18 novembre 2025, JORT n° 137, p. 3123) ; MTK, décrets
    n° 82-1168, 85-1568, 87-1199, 89-598, 93-114 et 98-1802, décrets n° 2000-1934 et 2008-2398 (achats
    de tabacs bruts), article 69 de la loi de finances pour 2025 ;
  - **demandent l'OCR ou la lecture à l'image** (fascicules sans couche texte) : décret du 20 novembre
    1927 sur le régime de l'alcool (antérieur au corpus), loi n° 59-113 et décret-loi n° 60-5 ;
  - date de dépôt au gouvernorat du JORT n° 93 de 2011 (décret n° 2011-4395), comme pour la RNTA ;
  - objet des transferts du budget (Régie 2021 ; MTK 2017, 2020, 2022, sans subvention d'exploitation
    sur la fiche) : tableaux par établissement de l'annexe 8 ;
  - grandeurs d'activité (hectolitres vendus ; paquets produits et vendus, colonnes à attribuer) :
    non versées ;
  - comptes publiés des deux établissements : **à obtenir**.
- **Pharmacie centrale de Tunisie — section écrite le 30 octobre 2026** (`_offices.qmd`,
  `#sec-ep-ge-pct`, en fin de chapitre ; intro, « La source » et TODO final du chapitre mis à jour).
  Figures `fig-ep-pct-budget` et `fig-ep-pct-fiches`, tableaux repliés `tbl-ep-pct-fiche-a` et `-b`.
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-pct`, code `pct`) :
  LF 2022 p. 91, LF 2024 p. 133, LF 2025 p. 109, lues à l'image (300 dpi) et retrouvées dans la couche
  texte. Écart déclaré : 2022 (LF 2024), bilan +0,6. Subvention d'exploitation de 2020 : 29,7 (LF 2022),
  case vide et 29,8 aux autres produits (LF 2024) ; charges financières nettes de signes opposés entre
  éditions ; dits dans le texte et les légendes. Prose du rapport citée : LF 2022 p. 92, LF 2024 p. 134
  (avance du Trésor de 199,1 MD pour les vaccins contre la Covid-19), LF 2025 p. 110 (dettes des
  structures sanitaires prises en charge par l'État). Registre `tbl-ep-registre-pct`, lu au corpus local :
  décret-loi n° 61-2 (image), décret n° 87-228 (image), lois n° 90-104 et 90-105 (image), décret
  n° 91-555 (art. 1er à 13, image), arrêtés du 25 octobre 1994, du 4 septembre 1995 et du 25 novembre
  2020 (monopole d'importation), loi n° 2005-75 (vaccins, couche décalée, image), lois de finances pour
  2022 (art. 62), 2025 (art. 34, édition arabe) et 2026 (art. 79, édition arabe). Glossaire :
  `pharmacie-centrale`.
  **Reste** :
  - **renvoi au volume « La santé »** : aucun chapitre ne traite des médicaments ni des achats de la
    Pharmacie centrale au 30 octobre 2026 ; TODO (rédacteur) laissé en tête de section ;
  - 192 MD de la loi de finances complémentaire pour 2021 et 200 MD par an des lois de finances pour
    2022 et 2023 (prise en charge par l'État de dettes des structures sanitaires publiques envers la
    Pharmacie centrale, rapport LF 2025 p. 110) : **lu le 30 octobre 2026**, aucun article ni aucune
    ligne ne les porte — décret-loi n° 2021-3 (articles en couche texte, tableaux A à D océrisés,
    annexe de l'arrêté de répartition, mission de la santé p. 2632, lue à l'image), lois de finances
    pour 2022 et 2023 (couche texte). Hausse de 193,0 MD des « autres dépenses » des programmes 1 à 3
    de la mission de la santé, non rattachée. Fiche `r-ep-pct-dettes-structures-sanitaires` ; reste
    **à obtenir** : documents budgétaires de la mission de la santé et rapport du projet de loi de
    finances complémentaire ; tableaux de la mission de la santé pour 2022 et 2023 **lisibles au
    corpus**, non lus ; prêt du Fonds arabe de 26 MD (2022) : ratification non identifiée ;
  - subventions d'équipement « au profit de la pharmacie centrale » des lois de finances pour 2018 et
    2019 (repérées dans le miroir iort, **lisibles au corpus**, non lues) face à des transferts nuls dans
    le rapport : à rapprocher ;
  - arrêté du 25 novembre 2020 : annexe (p. 2866-2867) **lisible au corpus**, non lue ; décret
    n° 91-555 : suite au-delà de l'article 13 non repérée ;
  - textes **dans le corpus local, non lus** : décret et arrêté du 31 mars 1956, lois n° 58-28 et 58-29,
    arrêté du 18 mars 1958, décret n° 58-149, loi n° 61-24 (ratification), arrêtés de 1963, 1969 et 1981,
    décrets n° 72-233, 76-732, 99-1886, arrêtés de 1977, 1991 (commission d'achat), 2000 et 2020
    (conservation des documents), décret gouvernemental n° 2019-1013 ;
  - volume des ventes (édition française LF 2020, p. 119) non versé ; comptes publiés de
    l'établissement : **à obtenir**.
- **Agence foncière industrielle — section écrite le 29 octobre 2026** (`_industrie.qmd`,
  `#sec-ep-ge-afi`, en fin de chapitre ; intro et « La source » du chapitre mises à jour). Figures
  `fig-ep-afi-budget` et `fig-ep-afi-fiches`, tableaux repliés `tbl-ep-afi-fiche-a` et `-b`.
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-afi`, code `afi`) :
  LF 2022 p. 64, LF 2024 p. 98, LF 2025 p. 72, lues à l'image (300 dpi) et retrouvées dans la couche
  texte. Écart déclaré : 2023 (LF 2025), fonds propres hors résultat de l'exercice (+4,2). Édition
  LF 2024 : note « (1) » sans appel (comptes non approuvés par le conseil), dite dans le texte et la
  légende. Registre `tbl-ep-registre-afi`, lu au corpus local : loi n° 73-21 (image ; fascicule à
  double date, effet en fourchette), loi n° 78-27 (prêt garanti, image), loi n° 87-50 (art. 1er,
  image), loi n° 91-37 (image), loi n° 97-31, loi n° 2000-59 (couche décalée, décodée), loi
  n° 2009-34, décret n° 2013-2272, loi de finances pour 2016 (art. 84, extrait français local),
  décret présidentiel n° 2022-501. Glossaire : `afi`.
  **Reste** :
  - textes **dans le corpus local, non lus** : décret n° 73-598 et ses modificatifs n° 74-85 et
    85-1602 ; suite de la loi n° 87-50 (p. 962) et loi n° 91-38 ; décrets d'organisation n° 92-127,
    98-22 et 2010-3012 ; personnel, organigramme et emplois fonctionnels (décrets n° 77-545,
    98-1174, 98-1175, 2001-2442, 2012-2027, 2013-3109) ; décrets gouvernementaux n° 2016-413, 2016-822
    et 2016-1391 (article 52 bis du code d'incitation aux investissements, **intitulés arabes**) ;
    arrêté du 5 mai 2014 (réserves foncières industrielles) ; décrets d'approbation des ventes au
    dinar symbolique de 2023 à 2026 (n° 2023-613, 2023-614, 2023-659, 2023-660, 2023-771, 2023-772,
    2024-40, 2026-6, 2026-8) ; décret n° 2026-127 (Sidi Thabet) ; article 23, IV, du code des droits
    d'enregistrement et de timbre ;
  - grandeurs d'activité des fiches (surfaces aménagées) : unités incompatibles entre éditions
    (m², « hectare », milliers de m²), non versées ; classements des dettes et créances envers
    l'État (LF 2024 et LF 2025), liquidités placées (LF 2022) et couverture des charges (LF 2024) :
    cités d'après les pages, non versés dans une série ;
  - page exacte de la ligne de l'agence dans les tableaux des transferts par entreprise (LF 2022 à
    LF 2024) : non relevée ; objet des transferts à confirmer dans l'annexe 8 ;
  - comptes publiés et rapports annuels de l'agence : **à obtenir**.
- **Office des terres domaniales — section écrite le 29 octobre 2026** (`_offices.qmd`,
  `#sec-ep-ge-otd`, en fin de chapitre ; intro et « La source » du chapitre mises à jour). Figures
  `fig-ep-otd-budget` et `fig-ep-otd-fiches`, tableaux repliés `tbl-ep-otd-fiche-a` et `-b`.
  **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-otd`, code `otd`) :
  LF 2022 p. 75, LF 2024 p. 112, LF 2025 p. 88, lues à l'image (300 dpi) et retrouvées dans la couche
  texte. Écarts déclarés : bilan de l'édition LF 2024 (trois exercices), produits d'exploitation de
  2019 (LF 2022) et de 2021 (LF 2024, LF 2025) ; LF 2022, 2020 et LF 2025, 2023 sous une note.
  Éditions discordantes sur l'effectif (2018 à 2020) et sur les transferts de 2020 (0,2 puis 8,0 MD) :
  dites dans le texte et les légendes. Registre `tbl-ep-registre-otd`, lu au corpus local, à l'image :
  décret-loi n° 61-15, loi n° 61-58, loi n° 62-2, loi n° 73-26, décret n° 2001-82 et loi n° 2004-17
  (ces deux derniers à couche texte décalée). Commentaires du rapport lus : LF 2021 p. 111-113 (prose
  française), LF 2024 p. 115 et 165. Glossaire : `otd`.
  **Reste** :
  - exercice comptable : année civile en 1961, 1er septembre-31 août en 2001 ; date du changement
    (décrets n° 73-390 et 78-60, **dans le corpus local, sans couche texte, non lus**) et exercice que
    désignent les fiches du ministère, à établir ;
  - effectif : périmètre des chiffres des éditions LF 2022 et LF 2024 (écart de 1 176 agents sur 2020),
    à éclaircir dans les rapports ; objet des transferts de 2020 à 2022 (annexe 8, à lire) ; tableau de
    l'édition LF 2023 p. 198 (3,5 ; 3,9 ; 12,9 MD), nature non établie ;
  - créance abandonnée en 2004 (135,375 MD) : origine non établie ;
  - textes **dans le corpus local, non lus** : décret n° 64-129 (immeubles), n° 73-262 (retraite du
    personnel), n° 73-390, 73-431, 78-60, 78-851, 92-2069 (organisation), n° 75-772 (marchés), statuts
    du personnel et des ouvriers agricoles (n° 74-914 à 99-1855, décret gouvernemental n° 2017-1349),
    n° 2001-2430 et 2001-2431, n° 84-1036 et 2013-2628 (réquisition), lois n° 75-45 et 82-72 (crédits
    où l'emprunteur est l'État), lois n° 70-25 et 72-36 (cession des terres domaniales) ; plein texte
    des lois de finances (garanties, abandons, dotations) non parcouru ;
  - découvert bancaire de l'Office (LF 2024, tableaux 18 et 19, p. 43-44 : 88,9 et 117,5 MD) : non lu à
    l'image, non versé ;
  - grandeurs d'activité des fiches (céréales en quintaux, huile d'olive en tonnes) citées, non versées ;
    éditions françaises LF 2020 et LF 2021 : comptes dans la prose, non versés ;
  - comptes publiés et contrat-programme de l'Office : **à obtenir**.
- **Société tunisienne de banque, Banque de l'habitat, Caisse des prêts et de soutien des
  collectivités locales — sections écrites le 30 octobre 2026** (`_autres_entreprises.qmd`,
  `#sec-ep-ge-stb`, `#sec-ep-ge-bh`, `#sec-ep-ge-cpscl`, en fin de chapitre, à déplacer dans un
  chapitre « Le secteur financier public » ; intro et « La source » mises à jour). Figures
  `fig-ep-stb-fiches`, `fig-ep-bh-budget`, `fig-ep-bh-fiches`, `fig-ep-cpscl-budget`,
  `fig-ep-cpscl-fiches` ; tableaux repliés `tbl-ep-{stb,bh,cpscl}-fiche-a` et `-b` ; nouvelles
  fonctions `fig_banque`, `table_banque`, `tableau_banque_detail` (figures/grandes_entreprises.py),
  à rapprocher de celles qu'écrit en parallèle la branche BNA/BFPME/BTS. **Versés le 29 octobre
  2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-stbbh`) : STB et BH depuis le tableau des banques publiques (LF 2022 p. 39,
  tableau 21 ; LF 2024 p. 53-54, tableau 26 ; LF 2025 p. 29), mise en page `banques` et codes `bq_`
  de la branche BNA/BFPME/BTS ; CPSCL depuis le tableau du secteur quasi financier (LF 2022 p. 44 ;
  LF 2024 p. 63 ; LF 2025 p. 40), codes de la Poste, écarts déclarés (LF 2024, passifs y compris
  fonds propres ; LF 2025, 2023, bilan à 104,2 près). Les recapitalisations de 2013-2015 restent au
  chapitre « Restructurer » (renvoi en tête des sections). Registres lus au corpus local :
  STB — décret du 20 décembre 1956 (océrisation), loi n° 57-15 (image), loi n° 61-64
  (océrisation), décret-loi n° 81-29 (image), loi n° 92-55 (océrisation), loi n° 2012-17 ; BH —
  loi n° 73-24 (océrisation), décret n° 74-224 (art. 1er et 2, océrisation), loi n° 89-18
  (image), loi n° 2007-31, loi n° 2018-8 ; CPSCL — loi n° 2001-56 (couche décalée, décodée), loi
  n° 2015-19 ; la loi n° 75-37 reste au volume des finances locales (renvoi). Glossaire : `stb`,
  `bh` (le terme `cpscl` existait).
  **Reste** :
  - textes **dans le corpus local, non lus** : loi n° 82-6 (ratification du décret-loi n° 81-29) ;
    conventions STB-État de 1959 à 1967 (lois n° 59-57, 59-102, 59-104, 59-144, 61-5, 61-34,
    67-44) ; organigrammes et emplois fonctionnels de la STB (n° 2001-715, 2001-1251, 2007-894)
    et de la BH (n° 2005-965, 2006-1806) ; rectificatif de la loi n° 73-24, décret n° 74-223 et
    modificatifs, suite du décret n° 74-224 et décrets n° 76-271 et 76-1000, loi n° 75-83 (LF
    1976, exonérations de la caisse), lois n° 76-53, 77-63, 79-58, 93-117 (prêts garantis de la
    caisse), n° 92-34, 2002-70, 2003-72, 2009-78 (BH) ; pour la CPSCL, lois n° 97-78, 2003-19,
    2003-39, 2005-53 et décrets du personnel, de l'organigramme et des agences régionales ;
  - **à identifier** : filiation entre la Société tunisienne de banque populaire (décret de 1956) et
    la STB ; acte de constitution de la STB ; texte de la fusion de 2000 avec la BNDT et la BDET ;
    date effective de la transformation de la caisse en BH ;
  - écart entre les 117 MD de garantie mise en jeu (loi n° 2012-17) et les 70,0 MD relevés par la
    Cour des comptes pour 2012 ; écart entre les parts de l'État dans les dividendes de la BH du
    tableau des banques (46,87 MD sur 2021-2023) et le tableau des dividendes (46,7 MD) ;
  - CPSCL : « dette envers les banques » de l'édition LF 2022 à rapprocher de la note de
    l'édition LF 2025 ; objet des subventions d'investissement ; indicateurs d'activité non versés ;
  - montants souscrits en application de la loi n° 2015-31 et part de l'État dans le capital des
    deux banques ; comptes publiés et rapports annuels : **à obtenir**.
- **BNA, BFPME et BTS — sections écrites le 29 octobre 2026** (`_autres_entreprises.qmd`,
  `#sec-ep-ge-bna`, `#sec-ep-ge-bfpme`, `#sec-ep-ge-bts`, en fin de chapitre, à déplacer dans un
  futur chapitre « Le secteur financier public » ; intro et « La source » du chapitre mises à
  jour). Figures `fig-ep-bna-fiches`, `fig-ep-bfpme-budget`, `fig-ep-bfpme-fiches`,
  `fig-ep-bts-fiches` (nouvelle fonction `fig_fiche_banque` et tableau `tableau_fiche_banque`
  dans `figures/grandes_entreprises.py`, bloc délimité ; un agent parallèle a écrit pour la STB et
  la BH des fonctions voisines, `fig_banque` et `tableau_banque_detail` : à unifier à la fusion).
  Tableaux repliés `tbl-ep-<bna|bfpme|bts>-fiche-a` et `-b`. **Tableau des banques publiques versé
  le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-bnabts`, codes `bna`, `bfpme`, `bts`, mise en page « banques publiques », codes
  `bq_` communs avec la STB et la BH) : LF 2022 p. 39 (tableau 21), LF 2024 p. 53-54 (tableau 26),
  LF 2025 p. 30 ; lus à l'image (300 dpi) et retrouvés dans la couche texte. Commentaires du rapport
  lus pour le capital et la part de l'État (LF 2025 p. 34, 36, 37). La recapitalisation de 2013-2019
  reste au chapitre « Restructurer », non répétée. Registres `tbl-ep-registre-bna` (lois n° 59-47 et
  59-107, image ; loi n° 94-30 ; loi de finances pour 2004, art. 49-50 et décret n° 2004-751, couche
  décalée lue à l'image ; loi n° 2009-27 ; loi de finances pour 2026, art. 89, arabe),
  `tbl-ep-registre-bfpme` (lois de finances pour 2005, art. 23, et 2009, art. 15 ; pour 2024, art. 31,
  pour 2025, art. 53, et pour 2026, art. 63, arabe) et `tbl-ep-registre-bts` (loi n° 97-87 ; loi
  n° 2000-45, image ; lois de finances pour 2015, art. 38, pour 2018, art. 12, et pour 2026, art. 70,
  arabe ; loi de finances pour 2016, art. 77 et 78, lue le 30 octobre 2026 dans l'extrait français et
  l'édition arabe, en couche texte). Glossaire : `bna`, `bfpme`, `bts`.
  **Reste** :
  - textes **dans le corpus local, non lus** : loi n° 59-65 et décret n° 64-295 (BNA) ; suite de la
    convention du 1er août 1959 ; décrets d'organigramme et d'emplois fonctionnels des trois banques
    (n° 2001-982, 2003-1541, 2009-40, 2009-1740, 2008-3923, 2009-1741) ; décret n° 2001-886 (BTS) ;
    lois de garantie de prêts rétrocédés (BNA : n° 93-94, 95-79, 99-60, 2002-34 ; BFPME : n° 2006-40,
    2012-5, 2014-53, 2020-24, 2024-39 ; BTS : n° 2001-80) ; loi de finances pour 2024, art. 29 ; pour
    2025, art. 50-51 ; pour 2026, art. 23, 25, 26, 27 ; décret-loi n° 2022-79, art. 18 ;
  - fusion de la BNA et de la Banque nationale de développement agricole (loi n° 83-19 pour la
    seconde) : texte **non identifié** ; statuts de la BFPME (2005) : **à identifier** ;
  - objet des 22,7 MD de transferts à la BFPME en 2022 (LF 2024, tableau 45) ; part de l'État dans
    les dividendes de la BNA à recouper avec les recettes du budget ; ligne de crédits de programmes
    « autofinancement des projets de la BTS » (loi de finances pour 2015, tableau D) à suivre d'année
    en année ;
  - statut de la ligne « juin 2020 » de la BFPME (LF 2022) : « non dit » dans la série des fiches,
    « provisoire » dans celle des effectifs ;
  - comptes publiés et rapports annuels des trois banques : **à obtenir**.
- **Agence foncière d'habitation — section écrite le 29 octobre 2026** (`_autres_entreprises.qmd`,
  `#sec-ep-ge-afh`, en fin de chapitre, à déplacer dans un futur chapitre « L'habitat et
  l'équipement » ; intro, « La source » du chapitre et `index.qmd` mis à jour). Figure
  `fig-ep-afh-fiches` (pas de figure budget : transferts du budget nuls, l'agence n'est pas dans la
  série des transferts par entreprise), tableaux repliés `tbl-ep-afh-fiche-a` et `-b`. **Fiche du
  ministère des Finances versée le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-afh`, code `afh`) : LF 2022 p. 79 (tableau 28 du ministère
  de l'Équipement), LF 2024 p. 119, LF 2025 p. 93, lues à l'image (300 dpi) et retrouvées dans la
  couche texte ; aucun écart d'identité ; « autres passifs courants » de deux définitions (LF 2024 :
  36,9 ; LF 2025 : 491,2 pour 2021). Registre `tbl-ep-registre-afh`, lu au corpus local : loi de
  finances pour 1974, art. 28 (image), décret n° 74-33 (image, art. 1er à 28), loi n° 87-28 (image),
  décret gouvernemental n° 2021-327, décret n° 2023-584, arrêté conjoint du 8 avril 2025 ; création
  par renvoi à la ligne `r-ep-afi-1973`. Glossaire : `afh` passé au statut valide, définition
  réécrite en FR et AR (partagée avec « Les prestations sociales »), clé `decret-gouv2021-327`
  ajoutée au `references.json` du volume. Pages citées sans série : transferts nuls (LF 2022 p. 106,
  LF 2023 p. 201, LF 2024 p. 155), contribution aux ressources propres de l'État (LF 2022 p. 103,
  LF 2023 p. 198, LF 2024 p. 152), dettes et créances croisées (LF 2024 p. 142 et 146, LF 2025
  p. 119 et 123), couverture des charges (LF 2024 p. 165), commentaires (LF 2022 p. 83, LF 2024
  p. 123, LF 2025 p. 98).
  **Reste** :
  - textes **dans le corpus local, non lus** : décrets n° 76-313, 76-781, 86-281, 93-60 (fascicules
    scannés, image) et 2001-986 (couche décalée, lu en passant) modifiant le décret n° 74-33 ; décret
    n° 74-34 (marchés) ; décrets n° 75-585, 99-2745, 76-685, arrêté du 28 mai 1977 (personnel,
    retraite) ; décrets n° 2000-2830, 2000-2831, 2017-1048 (emplois fonctionnels, organigramme) ;
    décrets de zones de préemption, de périmètres d'intervention foncière et de réserves foncières
    (1974-2026, dont **intitulés arabes** seuls de 2011 à 2026) ; loi n° 73-21 relue pour l'AFH ;
  - date d'effet du décret n° 2021-327 : 23 mai 2021 ici (dépôt le 18 mai, plus cinq jours), 19 mai
    2021 au volume « Les prestations sociales » (`r-log-afh-2021`) : **à harmoniser** ;
  - grandeurs d'activité des fiches (chiffre d'affaires de LF 2022, ventes de lots en hectares de
    LF 2024) : non versées ;
  - aucune garantie de l'État à un prêt de l'agence identifiée dans les intitulés de jort_cache.db ;
  - comptes publiés et rapports annuels de l'agence : **à obtenir** ;
  - **pour « Les prestations sociales », chapitre « Le logement social » (`#sec-log-operateurs`)** :
    arrêté de la ministre de l'Équipement et de l'Habitat du 28 janvier 2025, conditions
    d'attribution des lots destinés à l'habitat individuel par l'AFH (JORT n° 11, p. 236, dépôt le
    29 janvier 2025, effet le 3 février 2025 ; lu, couche texte) : une seule demande et un seul lot
    par ménage, classement par ancienneté de la demande (score N/M × 100), actualisation tous les
    trois ans ; et condition sociale de l'arrêté conjoint du 8 avril 2025 (au moins 50 % des lots
    réalisés sur les terrains acquis au prix préférentiel réservés aux ménages dont le revenu brut
    mensuel ne dépasse pas trois fois le salaire minimum), à verser.
- **Société de promotion des logements sociaux — section écrite le 29 octobre 2026**
  (`_autres_entreprises.qmd`, `#sec-ep-ge-sprols`, en fin de chapitre, à déplacer dans un chapitre
  « L'habitat et l'équipement » ; intro, « La source » et TODO final du chapitre mis à jour). Figure
  `fig-ep-sprols-fiches` seule (aucun transfert du budget : 0 imprimé de 2018 à 2022), tableaux
  repliés `tbl-ep-sprols-fiche-a` et `-b`. **Fiche du ministère des Finances versée le 29 octobre
  2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-sprols`, code `sprols`) : LF 2022 p. 79, LF 2024 p. 118, LF 2025 p. 93, lues à
  l'image (300 dpi) et retrouvées dans la couche texte ; aucun écart déclaré ; LF 2022 imprime
  l'exercice 2020 « 200 », sans astérisque. Registre `tbl-ep-registre-sprols`, lu au corpus local :
  loi n° 77-53 (image), décret n° 77-926 (image et OCR de lecture), décret n° 92-1818 (image), loi
  n° 93-78 et son **rectificatif** (JORT n° 91 de 1993, p. 2005, image : l'article 4 nouveau réserve
  le capital à la CNSS, à la CNRPS et à la CAVIS), décret n° 2010-3170, décret n° 2012-1224, décret
  gouvernemental n° 2017-840, décret gouvernemental n° 2020-1034, loi n° 2026-2 ; dates de dépôt
  lues dans la mention de la dernière page de chaque fascicule. Glossaire : `sprols` (existant).
  **Glossaire corrigé** : « 14 février 2026 » → « 18 février 2026 » dans `sprols`, `snit`,
  `location-vente` et `vente-a-temperament` (FR et AR) : dépôt du JORT n° 19 de 2026 le 13 février,
  plus cinq jours (loi n° 93-64), les lois n° 2026-1 et 2026-2 ne portant pas de clause d'effet.
  Même correction dans `prestations_sociales/_logement_social.qmd` (§ des opérateurs, lignes
  `r-log-op-2026-1` et `r-log-op-2026-2`). **À reprendre dans ce chapitre** : registre de la SPROLS
  daté par la publication brute (`r-log-sprols-decret-1977`, `-1992`, `-1993`, `-2017`) ; dates
  d'effet calculées dans `tbl-ep-registre-sprols` (20 novembre 1977, 29 octobre 1992, 29 juillet
  1993, 7 août 2017) ; ligne de 1993 et § des opérateurs (« réservé en 1993 à la CNRPS et à la
  CAVIS ») à corriger par le rectificatif de novembre 1993 (CNSS, CNRPS et CAVIS).
  **Reste** :
  - textes **dans le corpus local, non lus** : décret n° 2005-910 et ses modificatifs antérieurs à
    2010 (tutelle avant 2010) ; arrêté du 17 avril 2006 (conservation des documents) ; décret
    n° 80-1504 (personnel), décrets n° 99-1105 et 2015-539 (organigramme), n° 2000-2576 (statut
    particulier), n° 2007-2983 et 2015-540 (emplois fonctionnels) ; décrets de cession au dinar
    symbolique n° 2016-145, 2016-146, 2019-484 et 2020-917 (intitulés arabes pour les deux
    derniers) ; article 30 de la loi n° 2012-1 ;
  - garanties : aucune identifiée ; bénéficiaire des prêts de l'AFD (lois n° 98-105, 2005-14), du
    Fonds saoudien (loi n° 2013-42) et du don du Qatar (décret n° 2013-1422) à lire ;
  - passifs hors fonds propres (215 à 224 MD) bien supérieurs à la dette de l'édition LF 2022 et aux
    lignes détaillées (52 MD fin 2020) : nature du reste à établir ; dettes et créances envers l'État
    de fin 2021 (LF 2023 : 9,5 et 0,2 MD) et de fin 2022 (LF 2024 : 0,3 et 10,5 MD), inversion
    possible ; contribution aux ressources propres, transferts, couverture des charges : cités
    d'après les pages, non versés dans une série ; annexe 8 : société non trouvée dans la couche
    texte, à vérifier à l'image ;
  - grandeurs d'activité des fiches (chiffre d'affaires, ventes de logements) : non versées ;
- **SNIT — section écrite le 29 octobre 2026** (`_autres_entreprises.qmd`, `#sec-ep-ge-snit`, en fin
  de chapitre, à déplacer dans un chapitre « L'habitat et l'équipement » ; intro et « La source » du
  chapitre mises à jour). Figure `fig-ep-snit-fiches` (pas de figure budgétaire : transferts nuls),
  tableaux repliés `tbl-ep-snit-fiche-a` et `-b`. **Fiche du ministère des Finances versée le
  29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-snit`, code `snit`) : LF 2022 p. 79, LF 2024 p. 119, LF 2025 p. 96, lues à l'image
  (300 dpi) et retrouvées dans la couche texte. Écart déclaré : 2019 (LF 2022), dette totale
  inférieure de 0,3 à la somme des créanciers. Lus sur les pages, cités sans série : transferts nuls
  (LF 2022 p. 106, LF 2023 p. 201, LF 2024 p. 155), contribution aux ressources propres (LF 2022
  p. 103, LF 2023 p. 198, LF 2024 p. 152 : trois séries qui ne concordent pas), dettes et créances
  croisées (LF 2024 p. 142 et 146, LF 2025 p. 118-119 et 122-123 : 89,1 et 90,0 MD de dette envers
  l'État quand la fiche de LF 2022 en donne zéro), couverture des charges (LF 2024 p. 166),
  commentaire (LF 2025 p. 102). Registre `tbl-ep-registre-snit`, lu au corpus local : loi n° 57-19
  et statut (OCR relu à l'image), lois n° 58-47 (image), 59-58 (OCR relu), 61-57 et son rectificatif
  (OCR), 78-28 (OCR), loi de finances pour 1985 (art. 65, OCR ; jort_cache porte bien p. 2961),
  décret n° 92-2235 (OCR, p. 63), décret n° 2025-204, loi de finances pour 2026 (art. 21, édition
  arabe), loi n° 2026-1. Clés `loi57-19` et `loi2026-1` reprises du volume des prestations sociales
  (même texte ; URL française ajoutée à `loi2026-1`). Glossaire : `snit` (entrée existante).
  **Reste** :
  - **date d'effet de la loi n° 2026-1 à corriger hors de ce volume** : dépôt au gouvernorat de
    Tunis le 13 février 2026, effet le 18 février 2026 (cinq jours, jour du dépôt non compté) ; le
    volume des prestations sociales (`_logement_social.qmd`, `r-log-op-2026-1`) et la définition
    `snit` du glossaire portent le 14 février ;
  - textes **dans le corpus local, non lus** : loi n° 57-22 (Compagnie immobilière de Tunisie) ;
    lois n° 59-64 et 59-85 (conventions de 1959) ; décret-loi n° 61-7 et loi n° 61-29 (Caisse
    mutuelle de crédit immobilier) ; arrêtés de 1959 et 1961 (seuil des transactions) ; décrets
    n° 66-389, 67-119, 69-160, 78-642, 79-313, 85-790 (logements, sociétés d'HBM confiées) ;
    personnel et organisation (décret n° 74-866, arrêté du 24 février 1979, décrets n° 2000-2493,
    2009-13, 2010-834, 2010-1322) ; textes de création des sociétés régionales (Nord, Centre, Sud) ;
    décrets d'expropriation (1962-1984) ; autres cessions au dinar symbolique (2019-2026, dont
    n° 2025-205 et 2025-206) ; décret d'application de l'article 21 de la loi de finances pour 2026 ;
  - grandeurs d'activité des fiches (chiffre d'affaires, logements réalisés et vendus) : non
    versées ; la colonne « logements réalisés » de LF 2022 ne recoupe pas celles de LF 2024 ;
- **Agence de réhabilitation et de rénovation urbaine (ARRU) — section écrite le 29 octobre 2026**
  (`_autres_entreprises.qmd`, `#sec-ep-ge-arru`, en fin de chapitre, à déplacer dans un futur
  chapitre « L'habitat et l'équipement » ; intro et « La source » du chapitre mises à jour). Figure
  `fig-ep-arru-fiches` seule (l'agence n'est pas dans la série des transferts par entreprise),
  tableaux repliés `tbl-ep-arru-fiche-a` et `-b`. **Fiche versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-arru`, code
  `arru`) : LF 2022 p. 80, LF 2024 p. 121, LF 2025 p. 96, lues à l'image (300 dpi) et retrouvées
  dans la couche texte ; aucun écart d'identité ; 2023 dit réalisé par l'édition LF 2025. Registre
  `tbl-ep-registre-arru`, lu au corpus local : loi n° 81-69 (image), décret n° 81-1876 (image,
  fascicule à double date, effet en fourchette), loi de finances complémentaire pour 2012
  (art. 27 à 31, extrait français local), décret gouvernemental n° 2019-487. Glossaire : `arru`.
  **Reste** :
  - textes **dans le corpus local, non lus** : décret n° 2002-536 (sans couche texte, image) ;
    décrets n° 84-645, 99-188, 2000-1231, 2001-1401, 2001-1402, 2015-538 ; arrêté du 20 avril
    1985 ; décrets de périmètres d'intervention et d'expropriation ; loi n° 93-53 (effet sur
    l'article 11 de la loi n° 81-69) ; conventions de prêt de l'AFD et de l'UE pour les programmes
    de réhabilitation des quartiers populaires (prêts à l'État ; rôle de l'agence à établir) ;
  - date de dépôt au gouvernorat des JORT n° 39 de 2012 et n° 45-46 de 2019 (dates d'effet données
    « au plus tôt ») : **édition arabe à lire** ;
  - composition du total des passifs (1 630 à 1 776 MD, moins de 350 MD détaillés) et transferts du
    budget à l'agence (tableaux par entreprise, annexe 8) : **à établir** ; grandeurs d'activité
    (projets délégués) citées d'après les pages, non versées ;
  - comptes publiés et rapports annuels de l'agence : **à obtenir**.
- **Société générale d'entreprises de matériel et de travaux (SOGEMT) — section écrite le 29 octobre
  2026** (`_autres_entreprises.qmd`, `#sec-ep-ge-sogemt`, en fin de chapitre, même destination que
  l'ARRU). Figures `fig-ep-sogemt-budget` et `fig-ep-sogemt-fiches`, tableaux repliés
  `tbl-ep-sogemt-fiche-a` et `-b`. **Fiche versée le 29 octobre 2026** (même branche, code
  `sogemt`) : LF 2022 p. 79, LF 2024 p. 118, LF 2025 p. 94 ; écarts déclarés : dette totale de
  l'édition LF 2022 supérieure à la somme des créanciers (44,4 ; 53,8 ; 48,1). Effectifs
  discordants entre éditions (212 agents en 2020 dans l'édition LF 2022, 1 194 dans l'édition
  LF 2024, à charges de personnel égales ; 2021 : 1 062 et 1 194), dits dans le texte et les
  légendes. Registre `tbl-ep-registre-sogemt` : décret n° 2007-1330 (marchés publics), loi de
  finances pour 2024 (art. 43, p. 3478, extrait français local). Glossaire : `sogemt`.
  **Reste** :
  - texte de création, forme juridique, capital et part de l'État : **non identifiés** dans
    jort_cache.db ; lois n° 70-29 (G.E.T., lue) et 71-2 (Société de matériel et de travaux publics,
    corpus local, non lue) : continuité avec la SOGEMT à établir ; décret n° 89-876 et
    modificatifs, décrets n° 2010-90 et 2010-3170 (tutelle) : corpus local, non lus ;
  - effectif juste de 2018 à 2021 : **à établir** (comptes de la société, éditions françaises
    LF 2020 et LF 2021) ; chiffre d'affaires de la colonne d'activité non versé ;
  - date de dépôt au gouvernorat du JORT n° 46 de 2007 : **édition arabe à lire** ;
- **Tunisie Trade Net — section écrite le 29 octobre 2026** (`_autres_entreprises.qmd`,
  `#sec-ep-ge-ttn`, en fin de chapitre ; intro et « La source » du chapitre mises à jour). Figure
  `fig-ep-ttn-fiches` (pas de figure du budget : la société n'est dans aucun tableau des transferts
  versé), tableaux repliés `tbl-ep-ttn-fiche-a` et `-b`. **Fiche du ministère des Finances versée
  le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-ttn`, code `ttn`) : LF 2022 p. 50, LF 2024 p. 74, LF 2025 p. 50, lues à l'image
  (300 dpi) et retrouvées dans la couche texte. Édition LF 2024 : « total des passifs » égal au
  total des actifs (écart déclaré ; la case de 2020 n'est pas tracée, `PASSIFS_AVEC_FONDS_PROPRES`).
  Capital et actionnariat d'après l'édition française LF 2021 (p. 13-14). Registre
  `tbl-ep-registre-ttn`, lu au corpus local : décrets n° 2006-1807, 2006-1808 et 2009-3511.
  Glossaire : `ttn`. Renvoi en tête de section vers « Les droits de douane » (`#sec-dd`).
  **Reste** :
  - rôle de la société dans le système intégré de traitement automatisé des formalités du
    commerce extérieur : **aucun texte lu ne la nomme** ; décret n° 97-2470 (lu, couche texte) et
    arrêté conjoint du 20 avril 2001 (lu, couche décalée décodée) parlent d'un « gestionnaire du
    centre serveur » sans le nommer ; décret n° 2006-2620 (lu) ; texte de création et statuts :
    **non identifiés** dans jort_cache.db (intitulés français et arabes) ;
  - volume « La fiscalité », chapitre « Les droits de douane » : la liasse unique et ses textes
    fiscaux n'y sont pas — loi de finances pour 2000, art. 71 (timbre, lu) et loi de finances pour
    2003, art. 67 (paiement électronique, lu) ; à y verser, pas au volume des entreprises publiques ;
  - schéma et annexe de l'organigramme de 2006 : dans le corpus local, **non lus** ;
  - grandeur d'activité des fiches (dossiers, documents traités) citée en TODO, non versée ;
    édition LF 2023 (p. 86) non versée ; tableaux 32 et 34 de l'édition LF 2021 (p. 152 et 157)
    lus, non versés ; identité des « autres actionnaires publics » : **non établie** ;
  - comptes publiés et rapports annuels de la société : **à obtenir**.
- **Office national des postes — section écrite le 29 octobre 2026** (`_eau_communications.qmd`,
  `#sec-ep-ge-poste`, en fin de chapitre, après le GCT). Figures `fig-ep-poste-budget` et
  `fig-ep-poste-fiches`, tableaux repliés `tbl-ep-poste-fiche-a` et `-b`. Le rapport n'a pas de fiche
  de la Poste dans la suite des fiches d'entreprises : ses comptes sont au tableau des « autres
  entreprises publiques du secteur quasi financier », même mise en page (LF 2022 p. 44, tableau 22 ;
  LF 2024 p. 63, tableau 27 ; LF 2025 p. 40). **Versés le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-poste`, code
  `poste`), lus à l'image (300 dpi) et retrouvés dans la couche texte ; aucun écart d'identité ;
  charges financières nettes de signe opposé entre LF 2024 et LF 2025. Transferts du budget (20 MD
  en 2018, 21 MD en 2020, 11 MD en 2021) lus aux pages par entreprise des éditions LF 2022 (p. 106),
  LF 2023 (p. 200) et LF 2024 (p. 154). Commentaires du rapport lus : LF 2024 p. 64-65, LF 2025
  p. 42. Registre `tbl-ep-registre-poste`, lu au corpus local : loi n° 90-97 (comptes courants
  postaux, p. 1636, image) ; loi n° 98-38 (code de la poste) ; décret n° 98-1305 (création) ; loi
  n° 98-87 (transfert des biens et du personnel) ; loi de finances pour 1999, art. 67 et 68 ;
  décret n° 2003-1536 (couche texte décalée, décodée) ; loi de finances pour 2004, art. 39 à 42
  (couche décalée) ; décret n° 2007-1394 ; loi n° 2007-40 ; décret gouvernemental n° 2016-681.
  Dates de dépôt au gouvernorat lues à l'image sur la dernière page des éditions arabes (1998,
  2003, 2007) et dans l'édition française (2016). Glossaire : `onp`. Dans `grandes_entreprises.py`,
  le panneau « résultat net » de `fig_budget` n'a plus d'échelle quand l'entreprise n'est dans
  aucun classement (cas de la Poste, absente des classements des dix premiers résultats).
  **Reste** :
  - nature du total des passifs (12 à 15 milliards de dinars, dont 647 à 784 MD dans les rubriques
    détaillées) : la fiche ne la dit pas ; états financiers de l'Office : **à obtenir** ;
  - objet des transferts de 2018, 2020 et 2021 (annexe 8, tableaux par établissement, **lisibles
    dans le corpus de `tunisia-data`**) et application à l'Office, depuis 1998, de l'article 8 de la
    loi n° 90-97 (intérêts et rémunération de 1,5 % des avoirs des comptes courants postaux) ;
  - garantie de l'État à des emprunts de l'Office : aucune par les intitulés de `jort_cache.db`
    (français, arabe, FTS) ; plein texte non parcouru ;
  - textes **dans le corpus local, non lus** : décret du 28 août 1956 (Caisse d'épargne nationale
    tunisienne) et ses modificatifs, décrets sur les taux de l'épargne et des comptes courants
    postaux (1967-1988), lois de finances pour 1978, 1987, 1988, 2003 (art. 82), 2015 (art. 43,
    seuil antérieur non lu), 2019 (art. 53 et 54) et 2026 (art. 100), organigramme, statut du
    personnel, emplois fonctionnels, arrêtés de 2004, 2019 et 2021, circulaire de la Banque
    centrale n° 2022-11 ;
  - grandeurs d'activité du tableau (cartes de paiement, comptes et encours de l'épargne postale)
    non versées ; édition LF 2022 absente de la série des effectifs ; éditions françaises LF 2020
    (p. 32) et LF 2021 (p. 42) : comptes dans la prose, non versés.
- **Tunisie Télécom — section écrite le 29 octobre 2026** (`_eau_communications.qmd`,
  `#sec-ep-ge-tt`, en fin de chapitre, après le GCT). Figure `fig-ep-tt-fiches` (pas de figure du
  budget : transferts nuls, LF 2022 p. 106 et LF 2024 p. 155), tableaux repliés
  `tbl-ep-tt-fiche-a` et `-b`. **Fiche du ministère des Finances versée le 29 octobre 2026** dans
  `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche `donnees/fiche-tt`) : LF 2022
  p. 87 (tableau 30, mise en page verticale), LF 2024 p. 128 (tableau 35), LF 2025 p. 105 ; lues à
  l'image (300 dpi), chaque ligne retrouvée entière dans la couche texte. Tous les exercices des
  éditions LF 2024 et LF 2025 dits réalisés. Écarts imprimés déclarés : produits d'exploitation
  supérieurs à recettes + autres produits (60,5 ; 50,7 ; 27,7 ; 30,1 MD, 2020-2023). Lus sur les
  pages, sans série : contribution aux ressources propres de l'État (LF 2022 p. 102 ; LF 2024
  p. 151), dettes et créances croisées de fin 2022 (LF 2024 p. 142 et 146) et de fin 2023 (LF 2025
  p. 118-123), part de l'État dans les bénéfices 2021-2023 (64,6 MD, p. 126). Registre
  `tbl-ep-registre-tt` : lois n° 95-36, 97-67, 98-86, loi de finances pour 1999 (art. 21, 22 et 68),
  lois n° 2002-39, 2002-40, 2002-60, 2002-89, 2003-40, 2004-12, 2004-86, décret n° 2006-398, loi
  n° 2014-48, décret gouvernemental n° 2020-422, décret présidentiel n° 2022-307 (fascicules
  français ; couche texte à police décalée décodée pour certains fascicules de 2002 à 2004). La loi n° 2004-30 et le décret n° 2006-1555 restent
  au registre de `_statut.qmd` (renvoi par `@tbl-ep-registre` et `@tbl-ep-22ter`, les liens
  `#r-` ne traversant pas les fichiers). Acquéreur de 2006 nommé d'après le recueil de la
  Direction générale de la privatisation. Glossaire : `tunisie-telecom`.
  **Reste** :
  - ouverture du capital de 2006 : texte d'autorisation **non identifié** ; part actuelle de
    l'État et cotation éventuelle **non établies** ;
  - redevance sur les télécommunications (15 % du chiffre d'affaires, loi n° 95-36, art. 10) :
    sort après 1999 **non établi** (aucun modificatif trouvé par les intitulés ; le code des
    télécommunications ne la mentionne pas) ;
  - textes **dans le corpus local, non lus** : décrets n° 95-2031 et 2003-1510 (organisation),
    99-2844 et 2010-2989 (statut du personnel), 2000-323 (organigramme), 2001-1248 (emplois
    fonctionnels), 2015-85 (application de la loi n° 2014-48), décrets de ratification
    n° 2002-2063, 2002-3040 et 2003-1554, code des télécommunications et ses modificatifs, loi de
    finances pour 2002, art. 66 à 70 ; licences 3G et 4G (décrets n° 2016-438 et 2017-64,
    **édition arabe**) ; annexe du décret n° 2022-307 (p. 901-945) ;
  - séries à verser dans `tunisia-data` : contribution aux ressources propres, transferts nuls et
    dettes et créances croisées (voir l'entrée CPG et GCT) ; grandeurs d'activité des fiches
    (abonnés, lignes) non relevées ; édition française LF 2021 (p. 130) non versée ;
  - comptes publiés et rapports annuels de la société : **à obtenir**.
- **Sociétés régionales de transport de Sfax et de Bizerte — section écrite le 29 octobre 2026**
  (`_transports.qmd`, `#sec-ep-ge-srt`, en fin de chapitre, avant le TODO de la SNCFT ; une
  section, deux sous-sections `#sec-ep-ge-srt-sfax` et `#sec-ep-ge-srt-bizerte`). Figures
  `fig-ep-srt-{sfax,bizerte}-budget` et `fig-ep-srt-{sfax,bizerte}-fiches`, tableaux repliés
  `tbl-ep-srt-{sfax,bizerte}-fiche-a` et `-b`, tableau `tbl-ep-srt-abandons` (lois d'abandon de
  créances de 1989, 1999 et 2005, en dinars), registres `tbl-ep-registre-srt` (les trois lois,
  communes aux deux sociétés), `tbl-ep-registre-srt-sfax` (décret n° 60-68, décrets n° 63-154 à
  63-158, arrêté du 24 avril 1969, loi n° 74-71, décret n° 2001-663, décret n° 2015-5) et
  `tbl-ep-registre-srt-bizerte` (arrêté du 14 juillet 1973, décret n° 2015-6). Fascicules de 1960
  à 1989 lus à l'image (sans couche texte) ; 1999, 2001 et 2005 dans la couche texte à police
  décalée, décodée ; 2015 dans la couche texte. Loi n° 89-74 : les deuxième et troisième colonnes
  du tableau sont en millimes (la somme redonne le total imprimé). **Fiches du ministère des
  Finances versées le 29 octobre 2026** dans `entreprises-publiques-fiches-entreprises`
  (`tunisia-data`, branche `donnees/fiche-srt`) : LF 2022 p. 55 (les deux sociétés), LF 2024
  p. 84 (Sfax) et 85 (Bizerte), LF 2025 p. 57 et 58. Écarts imprimés déclarés : dette totale de
  l'édition LF 2022 qui ne vaut pas la somme des créanciers (Sfax +13,2 ; +16,3 ; +11,2 ; Bizerte
  −6,4 ; −10,4) ; fonds propres 2020 de Sfax imprimés positifs en LF 2024 (96,4 ; bilan juste
  avec le signe « − », ligne des variations de la page calculée sur +96,4) ; colonne des fonds
  propres de Bizerte en LF 2024 (1,9 ; 1,4 ; 4,7) qui ne boucle pas ; autres produits de Bizerte
  2020-2021 (LF 2024) qui comprennent la subvention. Glossaire : `srt`.
  **Reste** :
  - textes de création et statuts des deux sociétés (sociétés anonymes : statuts hors du
    *Journal officiel*) : **à obtenir** ; société de Bizerte : aucun texte antérieur à 1973
    relevé par les intitulés français de `jort_cache.db` ; intitulés arabes et fascicules de
    1958-1973 à interroger ; société « de transport » de la commune de Sfax en 1960 : à
    identifier ;
  - part de l'État et des communes dans le capital aujourd'hui : **non établie** ;
  - textes **dans le corpus local, non lus** : schéma et annexe du décret n° 2001-663 ; arrêtés du
    25 novembre 2008 (Bizerte), du 19 août 2011 (Sfax) et du 11 octobre 2018 (calendriers de
    conservation des documents) ; décrets de 1963 sur les autres sociétés régionales
    (métadonnées seules) ;
  - grandeurs d'activité des fiches (voyageurs, kilomètres) non relevées ; objet des transferts
    du budget (compensation, subvention d'équilibre) à rapprocher du volume « La compensation »
    et de l'annexe 8.
- **SOTRAPIL — section écrite le 29 octobre 2026** (`_energie.qmd`, `#sec-ep-ge-sotrapil`, en fin
  de chapitre, après la STIR). Figure `fig-ep-sotrapil-fiches` (pas de figure du budget : la
  société n'est dans aucun tableau des transferts des éditions lues), tableaux repliés
  `tbl-ep-sotrapil-fiche-a` et `-b`. **Fiche du ministère des Finances versée le 29 octobre 2026**
  dans `entreprises-publiques-fiches-entreprises` (`tunisia-data`, branche
  `donnees/fiche-sotrapil`) : LF 2022 p. 64 (fichier 63), LF 2024 p. 95 (fichier 96), LF 2025
  p. 69 ; lues à l'image (300 dpi), chaque ligne retrouvée entière dans la couche texte ; toutes
  les identités tiennent, aucun écart déclaré ; tous les exercices des éditions LF 2024 et
  LF 2025 dits réalisés. Lus sur les pages, sans série : prose des éditions LF 2024 (p. 103-104 :
  covid-19 et carburant d'aviation en 2020, gasoil en 2022) et LF 2025 (p. 77) ; structure du
  capital, édition LF 2021 p. 14 (État 0 %, autres publics 52,951 %, autres 47,050 %) ;
  classements des résultats (série `entreprises-publiques-resultats-nets-dix-premieres`). Offre publique de
  vente de 2001 (30,39 %, 9 876 mD) d'après le recueil de la Direction générale de la
  privatisation. Registre `tbl-ep-registre-sotrapil` : décrets n° 2000-2371 (intitulé seul en
  français), 2001-240, 2001-1568 (lus à l'image), 2013-1393, décrets gouvernementaux
  n° 2016-1183 et 2019-38 (réquisitions), décret présidentiel n° 2022-492 (édition arabe) ;
  dates de dépôt lues en dernière page des éditions arabes. Arrêté du 18 août 2022 (calendrier
  des conseils, 2023) renvoyé à `tbl-ep-registre-gouvernance`. Glossaire : `sotrapil`.
  Figure : graduations fractionnaires de l'axe des montants désormais écrites avec leur
  décimale (`_axe_md`, sans effet sur les graduations entières des autres figures).
  **Reste** :
  - textes de création, de transformation (dénominations successives : « Société de stockage
    d'hydrocarbure et de transport par pipe-line » en 1998, « Société de transport d'hydrocarbures
    par pipe-line » en 2016 et 2020, « Société tunisienne de transport par pipes lines » dans
    l'édition LF 2021), d'introduction en Bourse et de concession des deux oléoducs : **non
    identifiés** dans `jort_cache.db` ni dans le plein texte du corpus ; fascicules français de
    1997 à 2001 à couche texte chiffrée (décalage de 29), à décoder ou océriser ;
  - texte arabe du statut du personnel (décret n° 2000-2371, JORT n° 86 de 2000, édition
    arabe) : **dans le corpus local**, non lu ; schémas et annexes des organigrammes de 2001 et
    de 2022, non lus ;
  - régime général : loi n° 82-60 (canalisations d'intérêt public, modifiée par la loi
    n° 95-50) et code des hydrocarbures (art. 75 à 83) : **dans le corpus local**, non lus ;
  - visas des décrets de 2001 et 2022 : loi n° 85-78 (sociétés à capital entièrement public),
    à rapprocher de la structure du capital de l'édition LF 2021 ;
  - grandeurs d'activité (quantités transportées par les deux oléoducs, trois éditions, unités
    à concilier) : non versées ;
  - comptes publiés de la société et communications à la Bourse : **à obtenir**.
- **Statut, tutelle et gouvernance — lus le 27 octobre 2026** (`_statut.qmd`, sections `#sec-ep-2006` et
  `#sec-ep-gouvernance`, registres `tbl-ep-registre` et `tbl-ep-registre-gouvernance`) : lus au corpus local,
  fascicules français (image pour 1985-1993, couche texte ensuite ; décret n° 2023-591 à l'édition arabe, la
  française étant absente du corpus et de pist.tn) — loi n° 85-74 et ses modificatifs n° 87-34 et 88-54 ; loi
  organique n° 2019-41 (art. 111, 164-166 : la Cour des comptes reprend les fautes de gestion au 1er janvier 2020) ;
  loi de finances pour 1993, art. 123, et loi n° 93-124 (régime transitoire de l'article 9 prorogé au 31 décembre
  1993 puis 1994) ; loi n° 96-74 relue (article 22 bis : l'édition française imprime « 12 (bis) », l'édition arabe,
  p. 1940, dit 22 bis) ; décret n° 2002-2197 et décret gouvernemental n° 2016-510 ; loi n° 2004-30 ; loi n° 2006-36 et
  ses quatre décrets d'application (n° 2006-1555, 2009-2965, 2013-4953, 2020-1061 — champs distincts, aucun
  n'abroge l'autre) ; loi n° 2007-33 ; décret gouvernemental n° 2018-618 ; décrets n° 2020-314, 2020-1052, 2022-303
  et arrêté du 18 août 2022 (administrateurs) ; décrets n° 2014-12 et 2015-2217 (rémunération des dirigeants :
  une phrase et un lien vers « Les rémunérations publiques », qui en est le domicile) ; décrets n° 2023-591 et
  2024-86 (audit des recrutements 2011-2021, tout le secteur public : ce ne sont pas les comités d'audit des
  conseils). **Dates d'effet** calculées par la mention de dépôt au gouvernorat de Tunis imprimée en dernière page
  de chaque fascicule (lois n° 93-124, 96-74, 99-38, 2001-33, décrets n° 97-564, 2002-2197, 2004-2265, loi
  n° 2006-36, et tous les textes neufs). **Intégré le 28 octobre 2026** (note
  `docs/notes/statut-textes-non-lus-2026-10-28.md`) : décrets n° 89-378 et 97-565 au registre
  (`r-ep-1989-tutelle`, `r-ep-1997-tutelle`) et en colonnes 1989 et 1997 de `tbl-ep-administrateurs` ; ligne
  `r-ep-2002` réécrite avant (1997) → après (2002), décret n° 2002-2197 relu à l'image contre celui de 1997 (ce
  que 2002 change : mandat renouvelable deux fois, délais d'approbation des contrats-programmes et des budgets,
  nomination par le seul ministre de tutelle, contrôleur d'État observateur, mandataire spécial nommé par le
  Premier ministre, destinataires des documents) ; article 67 de la loi de finances pour 1986 (`r-ep-1986-fautes`) ;
  activité de la Cour de discipline financière 1986-2009 (figure `fig-ep-cdf`, série `cdf-activite` de tunisia-data, branche `donnees/cdf-activite` ; tableaux repliés `tbl-ep-cdf` et `tbl-ep-cdf-detail`,
  vingt et une notices `cdf-rapport-01` à `-21`) ; passes du 27 octobre versées aux fiches
  `r-loi89-9-modificatifs-apres-2006` et `r-epna-liste-modificatifs-apres-2007` ; fiche
  `r-cdf-rapports-apres-2009`. **Restent** : fascicules sans couche texte de 2022 (n° 35, 91) et 2025 (n° 67, 70),
  à lire à l'image ou à océriser pour clore les deux recherches sur la loi n° 89-9 et la liste des établissements ;
  fascicules arabes de 2008 à 2013 (liste) ; texte qui retire l'Agence tunisienne d'Internet de la liste (piste :
  rapport de la Cour des comptes, JORT n° 93 de 2008, p. 3603) ; décrets n° 97-566 et 97-552 (établissements hors
  liste), **lisibles au corpus** (JORT n° 27 de 1997), non lus ; rapports de la Cour de discipline financière
  après 2009 : édition arabe de 2010 à 2016 à océriser ; condamnations touchant une entreprise publique de 1999 à
  2009, à compter arrêt par arrêt ; application du calendrier de 2022 (nominations par concours) non suivie ;
  lois n° 69-50 et 85-72 toujours en fourchette (fascicules datés de plusieurs jours). Notices neuves à verser
  dans Zotero et dans `precis/ar/entreprises_publiques/references.json` : `decret89-378`, `decret97-565`,
  `cdf-rapport-01` à `cdf-rapport-21`. Le décret n° 2014-12 prend
  effet le 25 janvier 2014 (dépôt le 20 janvier) : à reporter dans le registre des « Rémunérations publiques »
  (TODO de `_regime_conventionnel.qmd`).
- **Pages arabes** : la loi n° 89-9 et ses modificatifs n'ont été lus qu'en français ; les
  termes arabes du glossaire viennent des rapports du ministère et du relevé de la Direction
  générale de la privatisation.
- **Plafond des garanties de 2020 — tranché le 11 octobre 2026** : 7 000 MD (loi n° 2020-45 du
  14 décembre 2020, article 10 nouveau de la loi de finances pour 2020, JORT n° 123, p. 2932,
  lue dans le corpus ; fiche `r-garantie-etat-plafond-2020-lfr` résolue). Les 7 500 MD de la
  traduction française du rapport ne sont pas dans la loi. À reporter dans `tunisia-data`, dont
  la série `garanties-etat` garde les deux valeurs et dit le point « non tranché ».
- **Plafond légal de la garantie, 1958-59 à 2015 — fait le 23 octobre 2026**
  (`docs/notes/entreprises-publiques-plafond-garanties-2026-10-23.md`, §§ 1 à 6, section
  `#sec-ep-garanties-plafond-legal`, figure `fig-ep-plafond-legal`, registre `tbl-ep-plafond-registre`
  et `tbl-ep-garanties-commission` repliés ; série `jort-lf-plafond-garanties` de `tunisia-data`, lue par
  `figures/listes.py` depuis le cache du précis le 24 octobre 2026, contrôlée par
  `tests/test_listes_entreprises_publiques.py`). Soixante et une lois et textes lus aux
  fascicules français du corpus : trente-huit de 1958-59 à 1994 (reconnaissance de caractères) ;
  vingt-trois de 1995 à 2015 (couche texte ; polices codées de 1999 à 2004 déchiffrées), dont deux
  relèvements en cours de gestion — loi n° 2002-90 (2002 : de 950 à 1 800 MD) et décret-loi
  n° 2011-56 (2011 : de 1 800 à 4 000 MD). Le plafond est de 950 MD de 1994 à 2010 sauf 1 200 MD en
  2003, puis 1 800, 4 000 et 3 000 MD (2013-2015). Parts du PIB en quatre segments de base (1961-91,
  1992-96, 1997-2009, 2010-15), traits interrompus aux ruptures ; parts des dépenses de l'État de 1986
  à 2015. Arrêté du 3 avril 1993 sur la commission de garantie lu (le chapitre l'attribuait à une
  commission d'instruction : corrigé). **Restent** : gestion 1960 et décret du 29 juin 1957
  (fascicule absent du corpus local, à obtenir sur pist.tn) ; lois de finances complémentaires de
  1969 à 1991 à lire en entier ; garantie propre aux dettes de l'Office des céréales et
  de l'Office national de l'huile (loi de finances pour 1997, art. 17, 980 MD), lue et versée au
  registre de l'Office des céréales (`tbl-ep-registre-oc`) le 28 octobre 2026, pas au chapitre des garanties ;
  article 36 de la loi n° 77-81 (fonds d'amortissement de la garantie de bonne fin) ; acte de la
  commission d'instruction ; prêts du Trésor aux entreprises publiques avant 2016 (article voisin de chaque loi,
  40 MD de 1995 à 2005 et 100 MD de 2013 à 2015, montants vus, pas en série ; la série commence en 2016) ; lois modifiant un budget de capital en cours d'année et réalisation du budget avant 1986
  (fiche `r-ep-budget-etat-1959-1985`) ; PIB de 1959-60 et de 1960 ; libellés arabes de la figure ; alias arabe transitoire `lf-1978` à retirer après la
  retraduction (`docs/notes/biblio-a-rapatrier.md`). **Dénominateurs d'avant 1986 (§ 7 de la note)** : établi le budget ordinaire voté (titre I ;
  recettes ordinaires = crédits des dépenses de gestion ou courantes) de 1959-60 à 1986 (les crédits de
  1959-60 sont effacés à l'image), lu aux fascicules scannés ; relevé `listes/budget-ordinaire-lois-de-finances.csv`,
  vue en part du budget de la figure sur deux segments séparés en 1986 (budget ordinaire voté, puis dépenses
  réalisées hors service de la dette) ; aucun total de l'État (budget d'équipement non lu, contribution du
  budget ordinaire à compter une fois). Notion « budget ordinaire » non versée au glossaire, faute de terme
  arabe attesté par un texte lu. **Versé dans `tunisia-data`** : séries `jort-lf-plafond-garanties` (montant fixé, montant en vigueur à la fin de la gestion, 1958-59 à 2015) et `jort-lf-budget-ordinaire` (1959-60 à 1986) ; le relevé du plafond du livre est retiré, celui du budget ordinaire reste dans le livre pour ses colonnes d'article et de page (la série porte la localisation en une colonne).
- **Second passage de la note** (son § 8) : ventilation par nature de 2023 (écart imprimé de
  23,0 MD) ; encours des prêts rétrocédés (rapport sur la dette publique, pages repérées) ;
  rapports sur la dette publique des éditions LF 2021 et LF 2024 ; rapports
  de la Cour des comptes par entreprise ; OCDE. (Bilan global de la privatisation et opérations
  une à une : faits le 27 octobre 2026, voir le point « Céder ».)
- **Glossaire** : deux entrées neuves, provisoires, sans définition arabe —
  `garantie-etat` (ضمان الدولة) et `participation-publique` (مساهمة عمومية). Non versées,
  faute de terme arabe attesté par un texte lu ou de définition légale : entreprise-mère et
  filiale (1985), action spécifique, commission d'assainissement et de restructuration,
  privatisation (« تخصيص » chez la Direction générale ; la loi dit « restructuration » et
  « cession »), contrat de performance, prêt rétrocédé, document d'orientation, dette
  garantie. Les entrées `contrat-programme`, `controleur-d-etat` et `tutelle` sont définies
  pour les caisses et les collectivités : à élargir aux entreprises publiques (lois n° 85-72
  et n° 89-9).
- **Bibliographie** : trente-huit notices (dont `wb-tunisia-gouvernance-ep-2014`, à verser dans Zotero) dans `entreprises_publiques/references.json`, dont
  douze recopiées d'autres livres (`imf-tunisia-art4-2020`, `wb-tunisia-per-2020`,
  `decret97-564`, `decret2004-2265`, `loi-org-2019-15-lob`, `bct-ra`, `ins-annuaire`…) : à
  promouvoir au fonds commun et à verser dans Zotero (`docs/notes/biblio-a-rapatrier.md`).
- **Effectifs — ce qui reste** : aucun total pour 2021 ni avant 2018 (l'édition LF 2020 ne
  donne qu'une part, l'édition LF 2021 n'a pas le tableau) ; quatre points sur quatre
  périmètres (84, 86, 88, 85 entreprises), jamais une série ; total de 2020 imprimé avec une
  demi-unité et non recoupé par les fiches ; définition de l'« agent » non dite ; sociétés
  régionales de transport autres que Sfax et Bizerte hors des fiches ; statistique publique de
  l'emploi des entreprises publiques non trouvée (enquêtes de l'INS sans ligne propre ; fiches
  sur la Banque centrale et la Cour des comptes sans effectif — rapports eux-mêmes non
  ouverts) ; rapport de l'Unité de suivi, source des 117 416 employés de 2010 que rapporte la
  Banque mondiale (2014), toujours non obtenu. Numéros de page des éditions LF 2022 à LF 2024 :
  ceux de la colonne `page_imprimee` de la série, à contrôler. Dette, subvention d'exploitation
  et total des passifs par entreprise : toujours non versés.
- **Parts calculées dans le module de figures, non dans l'entrepôt** : les dénominateurs
  (dépenses de l'État hors service de la dette, 1986-1987 et depuis 1991 ; PIB par segment de
  base, depuis 1986) sont lus dans la série `compensation-parts`, qui les porte déjà, et les
  parts sont calculées par `figures/entreprises_publiques.py`. À porter dans `tunisia-data`
  (une série « à tracer » par grandeur, comme pour la compensation), puis à relire ici. Les
  dépenses de l'État manquent de 1988 à 1990 : la vue des cessions s'y interrompt. La dépense
  de 2024 employée pour la loi de finances 2024 est celle de la série, dont l'état (réalisé ou
  voté) est à vérifier.
- **Intégration du volume** : livre arabe et `_quarto.yml` arabe, page d'accueil, comptes de
  livres (`AGENTS.md`, README), collection Zotero dans `sync_biblio.py`, libellés arabes des
  figures (`figures/entreprises_publiques.py`, table `LIB`).
- **Budget d'équipement et total de l'État avant 1986 — fait le 24 octobre 2026** (relevé
  `listes/budget-equipement-lois-de-finances.csv` et manifeste, test
  `test_budget_d_equipement_et_total_de_l_etat`, tableau replié `tbl-ep-budget-etat` dans la section du plafond ;
  seize clés de lois neuves dans `entreprises_publiques/references.json`, à promouvoir au fonds commun). Vingt-cinq
  textes lus à l'image, 1961 à 1986 : voies et moyens égaux aux crédits de paiement partout ; total de l'État =
  budget ordinaire + crédits de paiement − contribution du budget ordinaire, **établi par la loi pour 1983 seule**
  (1 753 MD), calculé selon le même mécanisme pour les autres gestions ; vide pour 1962 (montant provisoire
  abrogé), 1962-1964 (montant triennal), 1963 et 1964. Avant 1985 les voies et moyens comprennent les budgets annexes
  (le raccord 1984-1985 n'est pas à périmètre égal). **Restent** : lois modificatives et complémentaires (n° 70-59,
  71-58, 74-76, 84-3, 81-70, 82-27, 83-81) ; gestions 1959-60, 1963, 1964 sans montant annuel ; réalisation avant
  1986 ; reversement du total dans `tunisia-data` (relevé versionné dans le livre pour l'instant) ; la figure du
  plafond garde le budget ordinaire pour dénominateur (le total calculé n'y est pas encore substitué). Correction :
  la contribution du budget ordinaire en 1961 est de 0,6 MD (les 3 MD de la note du 23 octobre sont les emprunts).
- **Gestions 2010-2016, lois de finances 2016-2024** : voir les points « 2010-2016 » et « Plafond légal » ci-dessus ;
  le plafond de 2016 à 2024 vient des annexes du ministère (série `garanties-etat`), les articles des lois de
  finances de 2016 à 2024 restent à lire pour que la série légale rejoigne les annexes.
- **Forme du livre : un volume, à segmenter en quatorze chapitres (27 octobre 2026).** La demande d'une
  segmentation de premier niveau plus fine tranche la question « volume ou chapitre » en faveur du volume ;
  à confirmer par la revue humaine. Le plan, la table de correspondance des sections actuelles, les liens
  entrants à préserver, les sources par chapitre (en série, à portée, à obtenir), les pièges de domicile
  (compensation, caisses, Banque centrale, sociétés confisquées depuis 2011, concessions) et l'ordre de
  remplissage sont dans `docs/notes/chantier-decoupage-entreprises-publiques.md`. La scission est mécanique,
  sans contenu nouveau, et vient après la relecture de la passe sur les années récentes (branche
  `ep/cloture-2017-2024`). Quatre arbitrages attendent l'humain (§ 8 de la note) : chapitres sectoriels ou
  « grandes entreprises » ; domicile des sociétés confisquées ; chapitre « gouvernance » séparé ou fondu ;
  ordre des parties.
- **Plafond légal 2016-2026 et prêts du Trésor — fait le 27 octobre 2026** (branche `donnees/lf-plafond-garanties-2016-2026`
  de tunisia-data ; section `#sec-ep-garanties-plafond-legal` prolongée, registre `tbl-ep-plafond-registre` recopié
  jusqu'en 2026, registre neuf `tbl-ep-prets-tresor-registre`). Articles « garantie de l'État » et « prêts du Trésor »
  des lois de finances pour 2016 à 2026 et des lois rectificatives 2016-2023 lus à l'image : garantie 3 000 MD
  (2016-2018), 4 500 puis 4 790 (2019), 5 000 puis 7 000 (2020), 7 000 (2021-2022), 7 000 puis 8 000 (2023), 8 000
  (2024-2025), 7 000 (2026) ; prêts du Trésor de 100 à 550 MD selon la gestion. La série légale rejoint les annexes
  du ministère (`garanties-etat`) sauf pour la loi de finances initiale de 2023 (7 000 MD, relevée à 8 000 en
  novembre). **Restent** : éditions françaises des JORT n° 104 de 2015, 104 de 2018, 104 de 2019, 141 de 2022,
  144 de 2023 et 149 de 2024, absentes du corpus et de pist.tn (la loi de finances pour 2023 et celle pour 2026 sont
  citées à la page de l'édition arabe) ; prêts du Trésor avant 2016 ; libellés arabes du registre des prêts.
- **Céder (`_cessions.qmd`) — complété le 27 octobre 2026** (branche `ep/cessions-complement` ; tunisia-data,
  branche `donnees/privatisation-modes-operations`). Fait : section `#sec-ep-cessions-modes` (bilan global, 217
  entreprises par mode, 1987-2009, série `privatisation-bilan-global-par-mode`) ; section `#sec-ep-1999`
  (commission et comité technique, décrets n° 97-410 et n° 98-1440 ; liquidation à l'amiable, loi n° 99-38 ;
  liquidateurs, décret n° 2000-2280 — lus dans le corpus, dates d'effet calculées sur la date de dépôt imprimée au
  fascicule) ; section `#sec-ep-cessions-operations` (recueil 1998-2008 par année et nature de l'acte, 162 lignes en
  bloc replié ; séries `privatisation-recueil-par-annee-nature`, `-par-nature`, `-recoupement-annuel`, colonne
  `nature` au recueil) ; une ligne sur les biens confisqués (décret-loi n° 2011-13, art. 1er, lu). **Intégré le
  28 octobre 2026** (note `docs/notes/privatisation-ecarts-archives-2026-10-28.md`) : écarts du recueil avec le
  relevé annuel (1998, 1999, 2008, et 2000-2007) expliqués opération par opération par la liste arabe des
  opérations 1986-2009 (capture du 7 septembre 2012), tableau replié `tbl-ep-cessions-ecarts` ; « 6 noms contre
  5 entreprises » en concession : règle du plus gros montant reconstituée par le précis ; fiche
  `r-ep-privatisation-ecarts-recueil` ; notices neuves `dgpv-operations-1986-2009-ar`, `dgpv-recettes-par-mode`,
  `dgpv-recueil-index-2007` (à verser dans Zotero et dans le `references.json` arabe). **Restent** : total imprimé
  du tourisme et de l'artisanat (3 MD de plus que ses lignes), seul écart non expliqué ; mode retenu par la
  Direction pour l'ONP et la SOCOMENA (non énoncé) ; pistes : version française ou anglaise du recueil PDF aux
  archives du web, pages arabes de 2007 des secteurs transport et services ; pages de la liste arabe à relire à
  l'image avant toute citation à la page ; versement de la liste comme série par opération dans tunisia-data ;
  tableaux I à V des plafonds de rémunération des
  liquidateurs (décret n° 2000-2280, p. 2484-2488, **lisibles dans le corpus**, non transcrits) ; décret n° 89-377
  (composition de 1989) et décret n° 96-1225 (création du comité technique) — **lisibles dans le corpus** ;
  sociétés confisquées : domicile, décret-loi n° 2011-68, cession de 45 MD au rapport de clôture de 2022 ; textes
  de la seconde licence de téléphonie mobile et de l'ouverture du capital de Tunisie Télécom ; cessions depuis
  2009 opération par opération. Clé `dgpv-recueil-operations` du précis = `dgpv-recueil-operations-depuis-1998`
  de tunisia-data (deux noms pour une source). Cinq notices neuves dans `references.json`, à verser dans Zotero :
  `decret97-410`, `decret98-1440`, `decret2000-2280`, `dl2011-13`, `dgpv-bilan-global`.
- **Forme du livre : tranchée le 27 octobre 2026 — volume de six parties.** Le chapitre unique
  `_relation_financiere.qmd` est scindé en neuf chapitres (`_statut`, `_transferts`, `_garanties`, `_recettes`,
  `_cessions`, `_grandes_entreprises`, `_emploi_comptes`, `_longue_periode`, `_etudes`), sans contenu nouveau ;
  plan et décisions dans `docs/notes/chantier-decoupage-entreprises-publiques.md`. Restent : ouvrir
  « Restructurer » et la gouvernance quand ils ont leur matière.
- **Les notions — fait le 27 octobre 2026** (branche `ep/eclatement`, après relecture) : pas de liste dans la
  présentation ; chaque notion est liée au glossaire à sa première occurrence utile dans le chapitre qui la traite
  (`_statut` : entreprise publique, établissement public non administratif, participation publique,
  contrat-programme ; `_garanties` : garantie, prêts du Trésor, prêts rétrocédés ; `_cessions` : cession,
  privatisation, liquidation à l'amiable). Cinq entrées neuves au glossaire, `provisoire`, sans définition arabe :
  `prets-tresor` (قروض الخزينة, édition arabe de la loi organique du budget, couche texte), `prets-retrocedes`
  (القروض المعاد إقراضها, rapports arabes de clôture 2021 et 2024), `liquidation-amiable` (التصفية الرضائية, lue à
  l'image de l'édition arabe de la loi n° 99-38, JORT n° 37 de 1999, p. 848), `privatisation` (التخصيص, relevé
  arabe de la Direction générale de la privatisation), `cession-participations-publiques` (التفويت في المساهمات
  العمومية, assemblée à partir du même relevé). **Restent** : lire l'édition arabe de la loi n° 89-9 (JORT n° 9 de
  1989, **OCR** : la couche texte du corpus est illisible) pour confirmer l'expression de la cession et la
  traduction de « participation publique » ; définitions arabes des cinq entrées et de `garantie-etat` ; la
  définition de `contrat-programme`, écrite pour les caisses, ne dit pas l'usage de la loi de 1985.
- **Sections mixtes éclatées — fait le 27 octobre 2026** (branche `ep/eclatement`), sans fait nouveau. 1989 et
  1994-2001 : le périmètre reste dans `_statut` (`#sec-ep-1989`, `#sec-ep-1994-2001`) ; la cession organisée et
  l'action spécifique passent dans `_cessions` (`#sec-ep-1989-cession`, `#sec-ep-1994-cession`), avec les lignes de
  registre `r-ep-1989` et `r-ep-1994` recopiées. Clôture 2010-2024 : versements au budget dans `_recettes`
  (`#sec-ep-versements-cloture`, `tbl-ep-cdc-recettes`) ; principal garanti remboursé, prêts remboursés et encours
  selon la Cour dans `_garanties` (`#sec-ep-garanties-cloture`, `tbl-ep-cdc-garantie`, `tbl-ep-cdc-autres` réduit
  aux prêts) ; recettes de privatisation dans `_cessions` (puce de `#sec-ep-lp-cessions`, `tbl-ep-cdc-privatisation`)
  ; `_longue_periode` ne garde que `fig-ep-cdc`, ce que les flux montrent de la relation financière, et la
  description des rapports en note de méthode repliée (`tbl-ep-cdc-flux`). Après relecture, les séries des
  sections de clôture passent de la prose aux figures et aux tableaux repliés : figure neuve `fig-ep-cdc-garanties`
  (principal garanti remboursé, prêts remboursés, encours selon la Cour), `fig-ep-versements` et `fig-ep-cessions`
  pour les deux autres. **Restent** :
  pages des rapports de clôture du tableau des prêts (`tbl-ep-cdc-autres`), dont la liste couvre encore aussi les
  pages de la privatisation ; « depuis la gestion 2017 » (introduction de `#sec-ep-lp-cloture`) et « depuis le
  rapport sur la gestion 2018 » (encours) à accorder ; « en trois années » de `#sec-ep-lp-cessions` alors que 2014
  porte 4,3 MD.
- *(historique)* **Forme du livre : volume ou chapitre — décision laissée à la revue.** Éléments : (a) le livre n'a qu'un chapitre
  (`_relation_financiere.qmd`, environ 1 200 lignes) et une annexe ; (b) ses figures, ses séries et son plan
  (mise en place, réformes, état du droit, longue période) sont ceux d'un chapitre de partie V ; (c) le volume
  n'existe qu'en français et n'est pas lié depuis l'accueil comme les autres ; (d) la matière s'est étendue
  (garanties, dettes croisées, dividendes, cessions, effectifs, 2010-2016, budget avant 1986) au point que la
  scission du chapitre selon le critère de `docs/conventions-redaction.md` § 4 est plausible : relation financière,
  garanties et dette garantie, cessions, effectifs. Un volume suppose un livre arabe et un `_quarto.yml` arabe
  tenus à la main ; un chapitre de la partie V évite cette charge mais allonge un volume déjà chargé. Aucune
  décision prise ici.
- **État chiffré des lacunes restantes du volume (24 octobre 2026)** :

  | Lacune | État | Raison |
  |---|---|---|
  | Transferts du budget aux entreprises, par entreprise, 2010-2015 | 0 année sur 6 | rapports de clôture sans ventilation ; annexes d'avant 2020 non ouvertes |
  | Encours de la dette garantie avant 2016 | 0 année sur 6 | la Cour écrit que le compte général ne le porte pas |
  | Rapports de clôture des gestions 2010 et 2017 | 2 sur 15 gestions sans rapport propre | valeurs prises à la colonne de comparaison des rapports 2011 et 2018 |
  | Encours de la dette garantie selon la Cour, 2020 et 2024 | 2 gestions sur 8 depuis 2017 | non imprimé dans le rapport de clôture |
  | Intérêts de la dette garantie 2012-2014 | 3 sur 7 années lues à la couche texte | recoupées d'un rapport à l'autre, non relues à l'image |
  | Page française de la loi de finances pour 2023 et de celle pour 2026 | 2 lois sur 11 citées à l'édition arabe | fascicules français absents du corpus et de pist.tn |
  | Lois modificatives des budgets de capital 1970-1984 | 7 lois non lues | montants du vote initial |
  | Budget de l'État avant 1986 : total calculé | 23 gestions sur 26 (1961 à 1986) ; établi par la loi pour 1983 | sans total : 1962 (provisoire), 1963 et 1964 (triennal 1962-1964) ; 1959-60 sans budget d'équipement |
  | Réalisation du budget avant 1986 | 0 année sur 27 | lois de règlement et rapports de la Banque centrale non ouverts |
  | Recettes de cession depuis 2017 | 0 année | les rapports de clôture 2017-2024 n'ont aucune ligne de privatisation ; la Direction générale de la privatisation s'arrête à 2009 |
  | Fonds de restructuration du capital, recapitalisations en réalisation | 0 année | tableaux des fonds spéciaux non lus |
  | Rapport de l'Unité de suivi 2010-2014 | 1 document | non obtenu (fiche `r-ep-rapport-unite-suivi-2010-2014`) |

### Le transport public (`_transport.qmd`, 11 octobre 2026)

Chapitre nouveau, écrit sur `docs/notes/compensation-transport-2026-10-11.md` et sur les sept
séries versées dans `tunisia-data` (fiche `sources/compensation-transport.md`) ; **quand la note et
une série divergent, la série fait foi**. Premier jet, non relu par l'humain.

- **Plan** : vue d'ensemble (`#sec-compensation-transport-vue`) ; mise en place 1948-1983
  (`-mise-en-place`) ; grandes réformes 1984, 1985, 1987-1995, 2001, 2004, 2017 (`-reformes`, une
  sous-section par date ; `-1987` ajoutée le 13 octobre 2026 sur
  `docs/notes/compensation-transport-second-passage-2026-10-12.md`) ; état du droit en octobre 2026 (`-etat-du-droit`) ; tarifs et
  abonnements (`-tarifs`) ; abonnement scolaire (`-scolaire`) ; gratuités et réductions
  (`-gratuites`) ; longue période (`-longue-periode` : `-tarifs-constants`, `-interventions`,
  `-abonnements-nombre`, `-comptes`) ; Cour des comptes (`-cour`) ; *Livre blanc* de la Banque
  mondiale (`-livre-blanc`) ; incidence (`-incidence`). Six sections `.domicile-unique`, cinq
  registres repliés.
- **Figures** (`precis/fr/compensation/figures/transport.py`, `tr.figure(…)`), huit :
  `fig-compensation-transport-soutien` (quatre vues, dont part de la dépense de compensation et
  part du PIB), `-tarifs-arretes`, `-abonnements-prix`, `-tarifs`, `-interventions` (deux vues),
  `-abonnements-nombre`, `-trafic-tunis`, `-caisse` (trois vues : millions de dinars, part des
  dépenses de l'État, part du PIB ; **restent** : part des dépenses de l'État pour 1984-1985,
  l'entrepôt n'ayant ces dépenses qu'à partir de 1986 ; base du PIB de 1986-1991, présumée). Libellés des figures en français seulement : **libellés
  arabes à verser** dans `_L` avant de déclarer le chapitre au livre arabe.
- **Snapshots** du 11 octobre 2026 : `transport-soutien-par-societe`,
  `transport-abonnements-scolaires`, `transport-transferts-par-entreprise`,
  `jort-transport-tarifs-reperes`, `ins-bms-prix-transport`,
  `bm-livre-blanc-2016-transport-trafic-comptes`,
  `minfin-entreprises-publiques-transport-trafic-comptes` (ce dernier snapshoté, employé par le
  seul tableau `tbl-compensation-transport-comptes`, saisi à la main d'après lui).
- **Dinars de 2025** : `scripts/dinars_constants.py`, une seule convention, dite une fois à la
  section des tarifs — par année, moyenne des montants en vigueur au premier jour de chacun des
  douze mois, années entièrement établies seulement (celle de `figtools.constants_escalier`).
  Les tableaux annuels en dinars de 2025 sont engendrés par `tr.tableau_annuel`.
- **Trois fiches** dans `docs/recherches.yml` : `r-transport-tarifs-apres-2000` et
  `r-transport-decret-manque-a-gagner`, ancrées à l'état du droit ;
  `r-transport-ligne-budgetaire-1995-2002`, ancrée à `#sec-compensation-transport-1987`.
- **Bibliographie** : clés `lf-1985` à `lf-1995` versées le 13 octobre 2026 aux deux
  `references.json` du volume (adresses pist.tn de l'édition française contrôlées le 12 octobre ;
  adresses arabes tirées de l'index, fichiers non ouverts).
- **Arabe** : le chapitre n'est pas déclaré dans `precis/ar/compensation/_quarto.yml` (ligne en
  commentaire) ; à déclarer quand sa traduction sera livrée. D'ici là, `index.qmd`, `_depense.qmd` et `_reformes.qmd`
  nomment le chapitre en clair, sans ancre (`TODO (rédacteur)` : rétablir les renvois).
- **Lacunes**, dans l'état que la note établit :
  - **1985-1994, établi le 12 octobre 2026** (lu à l'image) : prévisions de la caisse de
    compensation et de soutien des transports routiers aux tableaux des fonds spéciaux, retour de
    ses recettes affectées au budget général à la gestion 1987 (loi n° 86-106, art. 92),
    subvention du budget seule de 1988 à 1994, suppression à la gestion 1995 (loi n° 94-127,
    art. 35) — `fig-compensation-transport-caisse` (figure à trois vues depuis le 13 octobre 2026 : millions de dinars, part des dépenses de l'État, part du PIB ; série `jort-lf-caisse-transports-routiers` de tunisia-data). **Restent** : réalisations (lois de règlement lues le 13 octobre 2026 : total de tous les
    fonds seulement, la caisse n'y est pas nommée ; lois de finances complémentaires, au corpus,
    **à lire**) ; composition des recettes de
    1985-1986 (art. 26 de la loi de finances pour 1985, **à lire**) ; pied de page de la loi de finances pour 1989 à confirmer à l'image.
  - **1995-2002** : ligne du budget général qui porte la subvention après la suppression de la
    caisse, non identifiée (fiche `r-transport-ligne-budgetaire-1995-2002` : lois de finances
    et décrets de répartition lus le 13 octobre 2026 pour 1995, 1996, 1997 et 2001, aucun
    libellé ne nomme le transport ; budgets du
    ministère du Transport, **à obtenir** aux archives du web) ; le poste n'est suivi qu'à partir
    de 2003.
  - **Tarifs entre février 2000 et novembre 2007**, et actes des relèvements d'août 2010 et de
    juin 2021 : aucun acte au *Journal officiel* (fiche `r-transport-tarifs-apres-2000` : plein
    texte français des fascicules de 2000-2010 joué le 12 octobre 2026, sans résultat ; restent
    l'édition arabe et les fascicules de 2021, communiqués des sociétés aux archives du web,
    numéros du *Bulletin mensuel de la statistique* antérieurs à novembre 2008, **à obtenir**).
  - **Subvention par société** : avant 2012, budgets du ministère du Transport antérieurs à
    2013, à chercher aux archives du web ; après 2017 au sens strict du poste, budgets de 2018 à
    2026, **à collecter** sur `finances.gov.tn` et `gbo.tn` — seule la colonne « interventions »,
    plus large, est connue pour 2016-2024, et son rapprochement avec le poste n'est fait que
    pour 2016. Éditions LF 2021 et LF 2023 du rapport sur les transferts : rangées ou à
    transcrire.
  - **Décomposition par nature** (scolaire, tarifs réduits, gratuités) : aucune source.
  - **Sociétés régionales** : ni voyageurs, ni recettes, ni couverture des charges ; rapports de
    la Cour des comptes sur six sociétés et éditions arabes du rapport sur les entreprises
    publiques (LF 2022 à LF 2025), **à collecter ou à exploiter**.
  - **SNCFT et métro léger, 1995-2023** (*Annuaire statistique* de l'INS, vingt-deux éditions) :
    repérés, **non versés en série** — sens des colonnes à vérifier édition par édition.
  - **Textes à relire sur les fascicules avant citation littérale** : loi n° 63-13, loi de
    finances pour 1978 (art. 37-38), loi n° 85-77, loi n° 2004-33 (art. 6, 11, 12), décret
    n° 2001-2621 ; clauses d'effet des arrêtés urbains de 1991 et 1992 ; arrêté du 30 septembre
    1989 ; arrêtés tarifaires de 1977 à 1986 ; loi n° 2012-26 et loi n° 2003-33 (intitulés
    seuls) ; arrêtés sur l'accès des personnes handicapées (1982, 1989, 1993).
  - **Pages de l'édition arabe** : relevées pour le seul décret gouvernemental n° 2017-987, dont
    l'édition française manque sur pist.tn (pagination française inconnue) ; toutes les autres
    entrées arabes ont le champ `page` vide.
  - **Décrets d'application de la loi n° 2004-33** (art. 11 et 12) : fiche
    `r-transport-decret-manque-a-gagner` ; montants des forfaits du décret n° 2017-987.
  - **Incidence** : aucune étude ne répartit la subvention du transport par niveau de vie.
  - **Frontière** : apurements de dettes, résultats et endettement des entreprises de transport
    (note, § 7) relèvent d'un texte à venir sur les entreprises publiques.

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
- **Tableaux encore faits main** : contribution au fonds de l'habitat et dégrèvements au
  chapitre 6, forfaits qui comprennent la taxe sur les établissements au chapitre 7 — la base
  de paramètres n'en porte qu'une ligne chacun, leur `TODO (rédacteur)` dit laquelle — ;
  tarifs des taxes et redevances diverses fixés par décret au chapitre 8, non transcrits ;
  seuils de l'approbation au chapitre 5 ; parts et critères du fonds et des subventions au
  chapitre 9. Sont engendrés (11 octobre 2026) : les trois barèmes des taxes sur les
  immeubles et la pénalité de retard ; pour la taxe sur les établissements, le minimum, le
  maximum et les taux par assiette ; les taux et tarifs des chapitres V à VII du code et les
  deux barèmes des parkings. Le tableau de la taxe hôtelière (deux lignes) reste fait main,
  ses valeurs étant versées : la forme commune ne rend pas ses deux lignes de registre.
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
- **population communale et non communale** (`#sec-fl-hist-longue-periode`,
  `fig-fl-hist-population`, 10 octobre 2026 ; module `figures/population.py`, série
  `population-milieu-communal-recensements` versée au cache, six clés `ins-rgph-*` versées en
  français et en arabe). Éditions retenues : tableau 3 du volume 1 du recensement de 2004 pour
  1966-2004, volume 1 du recensement de 2014 pour 2014 (part de 2014 calculée sur ses effectifs,
  égale aux 67,7 % qu'imprime le volume 3) ; 2024 (urbain / rural) tracé à part. Le nombre de
  communes de la figure est la table `COMMUNES` du module, reprise à la main de
  `tbl-fl-hist-communes` : à tenir en accord avec le tableau. Restent :
  - ventilation du recensement de 1956 par milieu : aucune des publications lues ne la
    donne, **à obtenir** ;
  - publications d'origine des recensements de 1966, 1975, 1984 et 1994 (valeurs et définition
    du milieu communal à chaque date) : absentes du portail de l'Institut, **à obtenir** ;
  - nombre de communes aux dates intermédiaires : annexe « Division administrative du pays »
    des annuaires statistiques (nombre de communes par gouvernorat, à des dates de situation),
    fichiers présents dans le dépôt des données, **à lire à l'image** ; complète la fiche
    `r-fl-nombre-communes` ;
  - aucune série à périmètre constant n'est publiée : la part de la hausse due aux créations et
    extensions de communes reste non mesurée ; ventilation communal / non communal de 2024 non
    publiée ;
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
des décrets restent écrits dans le chapitre. **Pénalité de retard engendrée le 11 octobre
2026** : `tbl-fl-penalite-retard` (taux mensuel et plafond du total, cinq dates ; valeurs
faites main identiques) et `fig-fl-penalite-retard` (le taux, en escalier, sans déflateur),
série `fl-tib-penalite-retard` ; le changement de point de départ de 2007, que portait une
colonne du tableau fait main, est passé dans un point de la section et au registre ; page de
l'art. 59 § 7 de la loi de finances pour 2023 portée au registre (édition arabe, p. 4076).
Restent faits main, avec leur motif en `TODO (rédacteur)` : la contribution au fonds de
l'habitat (`tbl-fl-immeubles-fnah`, seul le 4 % de 2005 est versé) et les deux dégrèvements
(`tbl-fl-immeubles-degrevement`, seul le dégrèvement partiel a un taux). **Figures des deux barèmes faites le 10 octobre 2026** : `fig-fl-tib-prix-reference` (quatre
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
(décrets de 1975-1976 et LF 1976, 1980, 1992, non lus) ; édition arabe non lue pour le code
(art. 35 à 45), les lois de finances pour 2013 (art. 13, 14, 23 et 24), pour 2021 (art. 13) et
complémentaire pour 2012 (art. 50), et les trois décrets du maximum (n° 97-435, 2003-1345,
2006-3360) — fascicules **dans le corpus**, couche texte à décoder ou **à lire à l'image** ;
celle de la loi de finances pour 2014 (art. 49) est lisible sur sa couche texte ; libellés
arabes des tableaux engendrés à confronter à ces éditions (chiffre d'affaires brut, produits à
prix homologués, redevables taxés sur leur impôt, maximum et sa suppression) ; doctrine administrative sur le chiffre d'affaires brut « local »,
1997-2013, **à obtenir** ; produit de la taxe avant ou après écrêtement au profit du fonds
depuis 2013, et série du montant écrêté, **à obtenir** ; amnisties de 2012, 2019, 2024 et 2025
(objet, années, conditions), loi n° 2006-25, décret-loi n° 2006-1, arrêté de calendrier de
2026 ; pages françaises des art. 37 (LF 2016), 42 (LF 2019), 52 et 57 (LF 2023), 67 et 69
(LF 2024) ; LF 1993, art. 38 et 39 : date d'effet non établie, édition arabe non relue
(édition française lue à l'image, p. 1670, fascicule **dans le corpus** sans couche texte),
et décrets des zones touristiques municipales (décret n° 94-822 et compléments), non lus ;
décret-loi n° 2020-33 (auto-entrepreneur) : date d'effet et pages à relever, sans clé
bibliographique ; LF 2023, art. 54 § 2 et 3, lus sur la couche texte de l'édition arabe
(p. 4073), **à relire à l'image**. **Corrigé le 11 octobre 2026, d'après les textes lus** :
la part de 50 % affectée au Fonds de protection des zones touristiques ne porte que sur la
taxe hôtelière des hôtels des zones touristiques municipales, et le fonds est ouvert par la
loi de finances pour 1993 (art. 38 et 39, ligne de registre `r-fl-act-hoteliere-fonds-1993`,
clé `lf-1993` versée au livre dans les deux langues), celle de 1997 ne récrivant que le
début du tiret ; l'auto-entrepreneur est dispensé de la taxe de 2020 à 2022, la loi de
finances pour 2023 abrogeant cette dispense (art. 54 § 2) et la contribution unique de 2019
(art. 54 § 3) — `tbl-fl-tcl-forfaits` donne désormais la période de chaque régime, et reste
fait main (seule la part de 20 % est versée). **Mis à jour le 11 octobre 2026** : les tableaux du minimum, du maximum
et des taux sont engendrés (48 + 4 + 6 valeurs comparées aux tableaux faits main, aucun
écart), avec deux figures en escalier (`fig-fl-tcl-minimum`, `fig-fl-tcl-maximum`) ; l'unité
du maximum est établie — le code dit « un maximum qui sera fixé par décret », le décret
n° 97-435 « 50.000 dinars par année », les décrets n° 2003-1345 et 2006-3360 « montant maximum
annuel », aucun ne disant s'il s'entend par redevable ou par établissement ; pages corrigées :
LF 2014, art. 49, p. 3680-3681 ; LF 2021, art. 13, p. 3125-3127 (§ 6, p. 3127).

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
- arrêtés du 4 mars 1997 et du 30 mai 2003 (listes de communes des parkings) ; barème des
  parkings de 2003 dans l'édition arabe (JORT n° 102 de 2002, p. 3510) : deux premiers cas
  lus sur une océrisation, **à relire à l'image** ; antécédents abrogés en 1997 (décrets de
  1887 à 1956, **à obtenir** ; loi n° 71-41) ;
- **engendrés le 11 octobre 2026** : `tbl-fl-taxes-baremes` (chapitres V à VII, en long, chaque
  grandeur avec sa période ; 10 valeurs identiques à celles du tableau fait main),
  `tbl-fl-parkings-1997` et `tbl-fl-parkings-2003` (neuf montants, dont 565 D), et
  `fig-fl-parkings` (communes de plus de 100 000 habitants, dinars courants et dinars de
  2025 ; nombres du texte écrits à la main d'après `baremes.reperes_parkings()`, à relire si
  l'indice de 2025 est révisé). **Corrigé** : la réduction de moitié de la contribution des
  riverains cesse au 1er août 2002, remplacée par un dégrèvement total (tableau, section,
  registres, `tbl-fl-qui-fixe`) ; libellés arabes de ces tableaux et des deux figures composés,
  l'édition arabe des articles n'étant pas relue : **à confronter** ;
- les notes de lecture de `fig-fl-parkings` et de `fig-fl-penalite-retard` (ch. 6) prolongent le
  dernier palier jusqu'en 2026, « aucun texte postérieur n'étant identifié », sans fiche de
  `docs/recherches.yml` : **à ouvrir** (modificatifs de l'art. 90 du code depuis 2003 ; de
  l'art. 19 § I depuis 2023), comme pour les barèmes des taxes sur les immeubles ;
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

- **TVA — écart de la recette à la prévision (`#fig-tva-prevu-realise`, 24 octobre 2026, branche `chantier-tva-ecart`).** Série `tva-ecart-prevision-realise` (2001-2026, `scripts/generate_tva_ecart.py`, test `tests/test_tva_ecart.py`) ; classeur du ministère relevé à la main dans `tva/classeur-tva-lf-lfc.csv` (2013-2026). Restent : (1) prévisions de TVA avant 2001, tableau A des lois de finances 1986-2000 en image, à lire (OCR) ; (2) LF 2012 : 3 929 MD au tableau A contre 4 515,5 MD à la colonne « LF » du bulletin d'exécution de mars 2013, à expliquer ; (3) périmètre de la rubrique « TVA » du classeur (brute ou nette des restitutions) non établi, à contrôler sur une loi de règlement ou un rapport de la Cour des comptes (à obtenir) ; (4) LFC 2011 et 2012 (4 154,0 MD au bulletin pour 2012) absentes du classeur ; (5) réalisé 2026 vide, exercice en cours ; (6) valeurs 2002-2004 et 2025 du PIB non rattachées à une base : écart en % du PIB non tracé.
- **Fiscalité — mis en conformité le 24 octobre 2026 (branche `lacunes-fiscalite`).** Les quatre figures de rendement (impôt sur le revenu, impôt sur les sociétés, TVA, droits de consommation) rapportent l'impôt au PIB de chacune des trois bases (1983, 1997, 2015), jamais raccordées, d'après la série `pib-courant-par-base` ; composant commun `figures/rendement_bases.py` (modèle : `figures/tva.py`), onglet « Données » à une ligne par année et par base. Les phrases chiffrées de `_impot_revenu.qmd`, `_impot_societes.qmd` et `_droits_consommation.qmd` disent la base de chaque pourcentage ; le rapport aux dépenses de l'État et aux recettes fiscales n'en dépend pas. Reste : libellés arabes des légendes (relecteur-ar) et rendu arabe des trois figures.

- **Rémunérations publiques — 5 emplois non conformes.** `fig-masse-salariale-ratios` (et sa
  reprise dans `_demo_figure_onglets.qmd`) annonce un « PIB en base 2015 » alors que 1990-1996
  n'est pas dans cette base, que 2002-2004 ne se rattache à aucune base et que **2012-2014 sont
  en base 1997** : la part publiée vaut 12,30 %, 12,79 % et 13,03 % ; rapportée au PIB en base
  2015 recalculé par l'INS, 11,71 %, 12,15 % et 12,35 % ; le « reflux » de 2014 à 2015 est un
  effet de base. Phrase de `index.qmd` (« 11 à 12 % … 16,1 % en 2020 … ») à reprendre. Figure B
  de `masse_salariale.py` : « base 2010 (×1,06) » — il n'existe pas de PIB nominal « base 2010 »,
  et le coefficient unique est appliqué à 1990-2025 alors qu'il n'est mesuré que sur 2015-2017.
  Citations du FMI (17,6 % en 2020 : PIB en base 1997, établi) et de la Banque mondiale (14,7 %
  en 2017, 10,7 % en 2010) : dire la base, ou dire qu'elle n'est pas précisée par la
  source (revue des dépenses publiques de 2020 à relire sur ce point). Les 8,9 % et 7,5 % de
  2013 et 2014 de `_regime_conventionnel.qmd` sont rendus au Livre blanc de 2018 le 11 octobre
  2026 : base non précisée par la source, et le texte le dit.
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

- **Zotero — à jour le 25 octobre 2026** : la poussée du 25 octobre (neuf lois de finances issues
  de la fusion des doublons, puis rangement) laisse **0 clé absente de Zotero** et 0 à ranger
  (contrôle de rangement, exécution 40222647086 ; détail dans `biblio-a-rapatrier.md`) ; les 72
  clés citées par plusieurs livres mais rattachées à un livre ont été déclassées le même jour
  (exécution 40223425216, 0 échec). Reste la **descente** (exécution 40222650564 : les 24
  `references.json` réécrits, ordre et forme des champs pour l'essentiel), à relire dans sa PR
  propre en contrôlant la préservation des URL et notes par langue.
- **Titres arabes et glossaire** : des notices restent en français dans la bibliographie
  arabe et des notions sont encore à valider (issues #151, #77, #54, #53). Recompter
  avant de réutiliser les totaux anciens de 69 notices et 26 termes.
- **Tableaux engendrés** : la règle est que tout tableau de paramètres vienne des dépôts
  openfisca par un générateur. Retraites et Prestations sociales y dérogent provisoirement.
- **Version arabe** : produite par la CI ; rendre tout livre traduit avant de fusionner
  la PR de traduction. Au 3 octobre 2026, aucun fichier français n'était en avance sur l'arabe
  (#340). **Au 25 octobre 2026, `uv run python scripts/traduction_en_retard.py --detail` compte
  88 fichiers en retard** : les traductions sont différées depuis le 6 octobre 2026 (plafond de
  dépense du traducteur) ; les arabes datent du 4 octobre, et quatre ensembles n'ont jamais été
  traduits (`annexe-pib.qmd`, `retraites/_regard_banque_mondiale.qmd`, les volumes « Santé »,
  « Éducation et formation » et « Entreprises publiques »). Ce n'est pas un blocage du travail en
  français. **Disjoncteur et issue d'état (30 octobre 2026)** : une limite de dépense (plafond
  mensuel du palier gratuit, 402, 429 persistant) ne fait plus rougir `translation-sync` ; le
  passage sort en succès, sans courriel d'échec, et l'issue épinglée « Traductions arabes : état »
  donne le retard par livre, la date de reprise estimée (1er du mois suivant, UTC), le budget
  mensuel appris (moyenne des trois derniers mois où la limite a été atteinte ; 300 000
  caractères tant qu'aucun mois n'a été mesuré, constante `BUDGET_INITIAL` de
  `scripts/etat_traduction.py`) et la consommation du mois. Rattraper par livre, en commençant par ceux dont la
  structure a changé (TVA, prestations sociales, finances locales). **Câblage et pages-relais
  (30 octobre 2026)** : `scripts/arabe_cablage.py` tient les listes de chapitres des `_quarto.yml`
  arabes d'après le français et pose une page-relais (« هذا الفصل لم يُترجم بعد » et lien vers le
  français) pour tout chapitre sans arabe, ainsi que pour les pages générales : plus de 404 arabe,
  `prestations_sociales/_soins.qmd` et `_logement_social.qmd` compris. Le relais compte comme
  « jamais traduit » et sera écrasé par la traduction. Reste : les trois livres sans `_quarto.yml`
  arabe (éducation, entreprises publiques, informel), que le script ne crée pas.
  **Rattrapage par lots (30 octobre 2026)** : lundi et 1er du mois, un livre à la fois
  (`scripts/lot_traduction.py`), borné au budget mensuel appris ; mesure du 30 octobre : 33
  fichiers périmés (1,97 million de caractères) et 84 jamais traduits (4,41 millions), dont les
  quatre ensembles jamais traduits (34 fichiers, 1,79 million). Le délai de résorption s'affiche
  dans l'issue d'état.
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

- **Budget de l'État voté, 1986-2026 : série versée, usage à décider (24 octobre 2026).**
  `tunisia-data`, série `jort-lf-budget-etat` (64 lois de finances initiales et complémentaires,
  ressources, charges, fonds spéciaux, emprunts nets, déficit imprimé depuis 2020 ; fiche
  `sources/jort-lf-budget-etat.md`). Aucun chapitre ni figure ne l'emploie encore : un total voté
  ne se lit qu'avec sa vue d'évolution datée et par régime de présentation (budget général,
  titres I et II, parties, missions : jamais chaînés ; les ressources d'avant 2020 comprennent
  les emprunts bruts et égalent les charges). Usages à instruire, un par un : (1) contexte
  budgétaire de la longue période des chapitres de dispositifs, en lisant les ressources
  ordinaires (`recettes_ordinaires_md`) et non le total ; (2) rapprochement, sur un graphique, des
  lois initiales et complémentaires d'une même année (écart voté) ; (3) fonds spéciaux, à
  rapprocher de la ligne des recettes des fonds spéciaux du ministère (`minfin-fonds-speciaux-tresor`).
  Lacunes : fonds spéciaux de 1986, 1987 et 1989 (loi initiale) ; articles d'emprunts nets de
  quelques lois complémentaires ; clés bibliographiques des lois complémentaires de 2002, 2004,
  2005, 2007, 2008, 2014, 2016, 2019, 2020, 2021, 2022 et 2023 et des deux lois du budget de capital
  de 1986 à verser (colonne `cle` vide) ; fascicule français de la loi de finances pour 2023
  (n° 141 de 2022) absent du corpus local, lue dans l'édition arabe.

## Suite proposée

**Point d'arrêt du 30 septembre 2026.** Le repère de bonification de l'article 32 est
établi au **5 mai 2019** dans le livre « Retraites », le glossaire et le dossier. Pour
reprendre sans refaire la même recherche :

- **D'abord, les textes locaux déjà lisibles** : les lectures de la liste
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

1. **Lire ce qui est déjà textuel** : les textes recensés au 23 octobre 2026 sont lus ; vérifier chaque article à sa page, pas seulement
   la présence du fascicule.
2. **Océriser par cible** — fait le 23 octobre 2026 (`docs/notes/ocr-cibles-2026-10-23.md`) pour
   la loi n° 65-17 (étudiants), le décret n° 75-952 (indemnités familiales), le code fiscal de
   1990 (annexe II) et le code TVA de 1988 ; reste à exploiter les textes dans les chapitres. La convention bancaire arabe de 2014 est **extractible après NFKC**,
   sans OCR. Les fascicules sont déjà locaux ; l'OCR ne peut créer une annexe absente.
3. **Chercher hors corpus** : montants/dates PNAFN auprès de l'administration, statuts
   annexés du personnel des caisses, méthode du barème d'actualisation des retraites.
   Les fascicules français non disponibles en ligne des LF 2025/2026 demandent un
   traitement distinct : extrait français local pour 2025, édition arabe pour 2026.
4. **Entretenir la chaîne éditoriale** : après revue des deux références nouvelles,
   les verser dans Zotero et inspecter la descente ; après réouverture du budget de
   traduction, rattraper l'arabe et rendre les livres concernés.
5. **Très basse priorité — institutions politiques et de contrôle** : le Parlement et la
   Cour des comptes, avec leurs obligations et leurs prérogatives respectives, et un
   inventaire des rapports de la Cour des comptes, au moins le rapport public annuel.
   Proposé le 21 octobre 2026 par un lecteur qui s'attendait à les trouver dans la partie
   « institutions », aujourd'hui limitée aux entreprises publiques. À examiner après les
   livres en cours, avec la partie VI (synthèse).

`todo-localisation.md` donne le point de départ pour les numéros et pages, **pas un
décompte actuel de disponibilité** : un fascicule qui y manque peut depuis avoir été
téléchargé (décret-loi n° 2024-4, par exemple), ou un chemin « français » servir
en réalité l'édition arabe.

### Droits de consommation, boissons : lacunes (23 octobre 2026)

Tâche close : lecture des décrets n° 97-1368 et 2015-1768 et de leurs modificatifs
(2002-627, 2007-1977, 2013-929, 2022-545), section `sec-dc-boissons` du chapitre
`_droits_consommation.qmd`. Plan : `docs/notes/plan-droits-consommation-alcools.md` ;
matière : `docs/notes/fiscalite-decrets-97-1368-2015-1768.md`.

- **Annexe de 2015 et tableau de la loi.** Les lois de finances pour 2016 (art. 44), 2018
  (art. 45) et 2021 (art. 20) portent les lignes 22-03 à 22-08 dans le tableau de la loi
  n° 88-62 : texte lisible dans le corpus (LF 2016 : édition française pp. 3150-3151 et édition arabe p. 3609 ; LF 2018
  pp. 4282-4283 et LF 2021 p. 3130, éditions françaises). Les deux éditions de la LF 2016 diffèrent pour les
  vins mousseux classés (4,000 D français, 24,000 arabe) : l'édition 2019 du code (française, p. 79 et 98, citée au chapitre) donne 24,000 D, mais reprend le tableau consolidé et non le fascicule ; seul un second exemplaire du JORT n° 104 de 2015 en français (absent du corpus local, non servi par pist.tn) trancherait la coquille. Reste à lire la doctrine administrative (notes communes sur
  les art. 44 de la LF 2016 et 45 de la LF 2018) pour savoir si l'annexe du décret de 2015 est
  abrogée, sans objet ou laissée en coexistence. TODO au chapitre.
- **Lois de finances 2022 à 2026.** *(24 octobre 2026 : LF 2022, art. 59 et LF 2023, art. 62 lus et écrits dans « Deux prélèvements propres aux boissons alcoolisées », `#sec-dc-boissons-autres`.)* Rubriques des textes indexés (`jort_cache`) : aucune ne
  porte sur les positions 22-03 à 22-08 ; le tableau consolidé de 2023 (`tbl-dc-en-vigueur`)
  porte les valeurs de 2021. À confronter, ligne à ligne, au texte des lois de finances 2024 à
  2026 (fascicules français de 2023 et 2024 absents du corpus ; éditions arabes présentes).
- **Lois de finances 1998 à 2017.** Plein texte des 31 fascicules à couche texte (fiche
  `r-dc-alcools-lois-de-finances-1998-2017`, 24 octobre 2026) : aucune occurrence des positions 22-03
  à 22-08 dans un article avant la LF 2018 ; la LF 1998, art. 47, vise les voitures de tourisme et
  les motocycles (lu, écrit). *Seconde passe du 24 octobre 2026* : numéros tarifaires à quatre et six chiffres, désignations et éditions arabes 2022-2025 : aucune ligne des positions 22-03 à 22-08 hors LF 2018 ; les modifications du droit de consommation des LF 2023 à 2026 portent sur la position 87-03. Reste : tableaux des LF 2000 à 2004 (couche texte décalée), à relire à l'image. Les valeurs de 1997 à 2015 de ces lignes reposent sur la chaîne des décrets (« sans
  modification » en 2002 et en 2013).
- **Habilitation de l'article 86 (LF 1989).** Elle vise les positions 22-03 et 22-05 à 22-09, sans
  22-04, alors que les décrets de 1993 et de 1997 fixent des tarifs pour Ex 22-04 (vins dans la
  nomenclature actuelle). Piste : la loi de décembre 1988 précède le tarif harmonisé (loi n° 89-113) ;
  le tableau de 1988 emploie l'ancienne numérotation (alcool éthylique en 22-08), où 22-04 désignerait
  les moûts de raisin. À vérifier sur le tarif de 1988, sans conclure.
- **Capsule de 1997.** La date de l'avis aux embouteilleurs (art. 44) est inconnue ; le JORT ne
  la porte pas.
- **Décret n° 93-2090.** Date de dépôt du JORT n° 80 de 1993 non lue ; libellés des lignes lus
  par OCR (colonne gauche à contrôler à l'image).
- **Contexte de 1997.** Le décret n'a pas d'exposé des motifs ; budget de 1997 et IXe plan non
  consultés.
- **Loi de finances 2022, art. 33 et 59 ; loi de finances 2023, art. 62.** *Écrit le 24 octobre
  2026* : redevance sur le commerce à emporter (lois n° 98-14 et 2004-76, LF 2022 art. 59), avance de 5 %
  sur les ventes des producteurs ; TVA du détail (art. 33) au registre des exonérations. Dates d'effet calculées le 24 octobre 2026 sur la date de dépôt relevée à la dernière page des fascicules (1^er^ mars 1998 ; 12 août 2004). Restent : arrêtés du 4 juin 1998 et du 14 décembre 2006 (conditions d'octroi de l'autorisation), non lus.
- **Fascicules scannés 2016-2026.** Recherche du motif 97-1368 sur la couche texte seulement :
  fiche `r-modificatifs-decret-97-1368` (`a_faire`).
- **Tableaux.** `alcools-tarifs` est engendré depuis le 23 octobre 2026
  (`generate_droit_consommation_tables.py`, 0.147 : les 60 cases lues dans les paramètres rendent
  exactement le relevé, cinq colonnes, la date du 1er janvier 2016 vérifiée sans valeur nouvelle ;
  le relevé reste le garde-fou) ; `capsule-fiscale` reste un relevé tenu à la main
  (`tarifs/tarifs-releves-droits-consommation.csv`), sans feuille d'accises.
- **Arabe.** Termes retenus sur l'édition arabe du décret de 1997 (lue à l'image, pp. 1366 et
  1370) : وصل ضمان, سند إعفاء, حسابية المواد ; à faire relire par le relecteur-ar.
- Alias arabes transitoires (23/10/2026) : les clés fondues restent dans `precis/ar/references.json` (note « TRANSITOIRE ») tant que les `.qmd` arabes les citent ; à retirer, clé par clé, après la retraduction du chapitre qui les cite (liste dans `docs/notes/biblio-a-rapatrier.md`, § « Fusion des clés en doublon »).

## Informel (volume XIII, ébauche du 28 octobre 2026)

Note documentaire : `docs/notes/informel-sources-2026-10-28.md` (textes de la CIST de 1993, 2003 et 2023 lus ; estimations classées par objet).

- Écrit : définitions (trois textes), six familles de mesure, estimations par groupe (enquête emploi, solde, valeur ajoutée, macroéconomie, Banque mondiale).
- Thèse de Ben Cheikh (2021) lue (note `docs/notes/informel-these-ben-cheikh-2026-10-28.md`) : série 2005-2018 ajoutée au tableau du solde ; la thèse donne deux valeurs pour 2018 (25,2 % et 26,9 %) sans les départager ; ligne de catalogue de `tunisia-data` à inscrire (fichier rangé, SHA-256 519efb04…b06d).
- Chapitre « La couverture sociale des informels » (`_couverture.qmd`, 28 octobre 2026) écrit d'après la thèse de Ben Cheikh, attribué à l'auteur ; références de loi rapportées par la thèse, à vérifier au JORT dans les volumes « Caisses » et « Cotisations » ; pas de figure (séries de couverture à six points).
- Informel retiré du marché du travail le 28 octobre 2026 (section des notions, plan, renvoi du temps de travail).
- À obtenir : Ben Cheikh et Moisseron 2021 (chapitre payant ; ses valeurs 25,2 % et 25,8 % sont dans la thèse) ; version française de la résolution de 2023 ; FMI DP/2022/011 et Medina-Schneider 2018 (serveur du FMI en 403) ; ITCEQ 2017 ; OCDE ECO WP 1486 ; enquête micro-entreprises postérieure à 2016 ; note INS du 2e trimestre 2020 sans couche texte.
- À lire à l'image : figure 11 du rapport PNUD-OIT (étiquette de 2018) ; tableau 12 de CRES-BAD ; annexe de la 17e CIST.
- À demander : table de passage OIT-INS pour l'écart de 2019 (36,9 % contre 44,9 %).
- Glossaire (28 octobre 2026) : neuf notions versées et ancrées dans le texte ; `emploi-informel` prend le terme arabe de l'INS (العمل غير المنظم), « travail informel » n'en est plus synonyme. Reste : termes arabes non attestés (économie informelle, travail informel, économie non observée, économie souterraine, entreprise individuelle, enquête mixte, méthode du solde, MIMIC) à confirmer sur la version arabe des résolutions de la CIST, non disponible dans le corpus ; version française de la résolution de 2023 à obtenir (définitions du glossaire traduites de l'anglais).
- À inscrire au catalogue de `tunisia-data` : 26 fichiers (lignes dans § 7 de la note).

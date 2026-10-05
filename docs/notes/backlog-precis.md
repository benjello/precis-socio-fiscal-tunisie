# Ce qui reste à faire, livre par livre

**Révisé le 30 septembre 2026.** Cette note rassemble les chantiers encore visibles dans les
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

## Vue d'ensemble

| Livre | État du texte | Première lecture faisable |
|---|---|---|
| Fiscalité | Cinq impôts ouverts (impôt sur la fortune ajouté le 4 octobre 2026) ; TVA : déductions, régime suspensif et obligations encore à rédiger | Décrets n° 97-1368 et 2015-1768 dans les fascicules français locaux, à lire sur pièce |
| Retraites | Deux chapitres développés ; coefficients des 31 barèmes relevés | Loi n° 2009-39 et décret n° 2009-2085 dans les JORT n° 55 et 56 de 2009, textes locaux extractibles |
| Rémunérations publiques | Régime indiciaire développé, trois autres chapitres brefs | Décret n° 2015-2217 dans le JORT n° 101 de 2015, texte local extractible |
| Prestations sociales | Dispositifs décrits ; PNAFN historique sans sources pour ses onze dates et montants | Décret n° 2018-626 dans le JORT n° 63 de 2018 et LF 2025, art. 26, dans l'extrait français local |
| Cotisations sociales | Régimes et branches décrits ; échelles AT/MP de 1995 et 1999 engendrées ; plusieurs assiettes et ventilations encore à établir | Article 4 du décret n° 2007-1406 dans le JORT n° 49 de 2007, texte local extractible |
| Finances locales | Les dix chapitres rédigés : présentation, notions et ressources propres (4 octobre 2026) ; institutions (histoire, compétences, budgets), transferts de l'État et longue période (5 octobre 2026) | Dispositions finales du code des collectivités locales (loi organique n° 2018-29), édition arabe du JORT n° 39 de 2018, texte local extractible |

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

**Rédaction à partir des textes déjà cités, puis vérification des versions.** La TVA
attend encore trois développements : déductions (art. 9-11), régime suspensif et
obligations déclaratives/de facturation (art. 18 et suivants) ; voir les `TODO` de
`precis/fr/fiscalite/_tva.qmd`. Ne pas les confondre avec une simple reprise de forme.

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
- **Séries à construire** : le seuil de la tranche à 0 % et les déductions pour charges de
  famille, rapportés au SMIG et à l'indice des prix, 1990-2026 ; les tarifs successifs de la
  contribution des patentes ; le plafond de déduction des primes d'assurance-vie.
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

- **Découpé en chapitres le 4 octobre 2026** (déplacement seul, aucune valeur changée, ancres
  gardées) : `index.qmd` (« Présentation » : introduction, conventions, présentation générale
  `#sec-prest-presentation`, encadré des caisses), partie « Les prestations contributives »
  (`_contributives.qmd`, `#sec-prest-contributives` : chapeau et ouverture du droit) —
  `_prestations_familiales.qmd` (`#sec-prest-familiales`), `_autres_risques.qmd` (maladie,
  maternité, décès, accidents du travail, perte d'emploi, CNAM ; `#sec-prest-autres-risques`) —,
  `_non_contributives.qmd` (`#sec-prest-non-contributives`), `_matrice.qmd` ; annexe
  `_notations.qmd` (« Les notations du volume »).
- **Arabe — à faire à la livraison de la traduction** : `precis/ar/prestations_sociales/_quarto.yml`
  ne déclare encore que `index.qmd`, à dessein. Y déclarer la partie `_contributives.qmd`, les quatre chapitres et
  l'annexe quand la traduction les livre, puis rendre le livre arabe (mêmes réserves que pour les
  cotisations).
- **Dépense des allocations familiales, 1990-2004 — fait le 3 octobre 2026** (`#fig-cnss-allocations-familiales`, `#sec-pf-longue-periode`), tirée de la rétrospective financière 1990-2004 de la CNSS (`cnss-retrospective-1990-2004`, exemplaire papier numérisé ; série `cnss-retrospective-ressources-emplois` snapshotée le 3 octobre 2026), déflatée par l'IPC des annuaires de l'INS (`ins-annuaire-ipc`). Restent : allocataires, enfants, montant moyen, dépense avant 1990 et après 2004 (TODO du chapitre). **221 valeurs de 1999** (et quelques-unes de 2000) masquées par la reliure restent à lire sur l'original papier (tunisia-data#26) ; en attendant, la figure trace des estimations hachurées ou creuses. Quand le classeur revient : réinjecter dans tunisia-data, relancer `figtools.refresh_cache("cnss-retrospective-ressources-emplois")`, puis relire la note de lecture, qui cite des montants. Depuis le 3 octobre 2026, la figure a trois vues : millions de dinars, % du PIB (PIB du ministère des Finances, série `irpp-ratios`, rupture de base des comptes nationaux marquée en 1997, non corrigée) et % du total des ressources de la CNSS (tableau de l'ensemble, page 78, toutes branches).
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
  l'édition arabe du JORT n° 88, pp. 2058-2059. Il relève de 50 à 100 D l'aide de rentrée
  scolaire, avec effet au 1er septembre 2024, élargit les cas couverts et interdit le cumul
  avec des aides publiques au même titre. L'édition française reste à vérifier.

- **Tableau engendré — fait le 3 octobre 2026** : les indemnités familiales du secteur public
  (`tbl-indemnites-familiales-public`) sont désormais le tableau du livre « Retraites », émis
  dans ce livre ; le montant de l'enfant handicapé (1996), sans paramètre, est passé dans la
  ligne « Sources ». Les taux qui financent l'assurance maladie des agents et des pensionnés
  de la CNRPS et le fonds de perte d'emploi de 2025 viennent aussi du livre « Cotisations
  sociales » (`tbl-cnrps-maladie`, `tbl-prevoyance-pensionnes`, `tbl-perte-emploi`).

## Rémunérations publiques

- **Chapitres à étoffer** : régime conventionnel public, marché contrôlé et statutaire
  autonome ; le régime indiciaire est le plus développé. Ne pas réutiliser les
  longueurs des chapitres mesurées avant la relecture des rémunérations.
- **Chronologies à construire** : indemnité de magistrature (décrets identifiés au JORT) ;
  textes de rémunération des magistrats de l'ordre judiciaire, des forces de sécurité
  intérieure et des douanes, absents du livre.
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
  - majoration de l'IGE au titre de 2011 (fiche `r-ige-2011`) : JORT n° 62, 73 et 90 à 99
    de 2011 **à obtenir** en français (l'arabe n'a pas de couche texte exploitable) ;
  - montants arrêtés par la commission supérieure pour les entreprises publiques, 1991-2012
    (fiche `r-montants-ep-commission`) : **à obtenir** hors JORT (rapports sur les
    entreprises publiques, communiqués conjoints de 1996 et 1999) ;
  - décrets des entreprises publiques entre 2013 et 2026 (fiche
    `r-augmentations-ep-2013-2025`) : plein texte 2014-2025 **lisible**, non parcouru ;
  - magistrats (décrets n° 2019-1132 et 2026-65) : à porter au régime statutaire autonome ;
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
- **Arabe — à faire à la livraison de la traduction** : `precis/ar/cotisations_sociales/_quarto.yml`
  ne déclare encore que `index.qmd`, à dessein (déclarer des fichiers absents casserait le rendu).
  Quand la passe de traduction livre les onze nouveaux fichiers, y déclarer les mêmes chapitres,
  la partie `_branches.qmd` et les annexes, puis rendre le livre arabe. D'ici là, le livre arabe
  sert l'ancien `index.qmd` d'un seul tenant ; si la passe réécrit d'abord `ar/index.qmd` en
  version courte, le contenu des chapitres manquera au livre arabe jusqu'à leur déclaration.
  Les renvois des volumes « Retraites » et « Rémunérations publiques » visent déjà les nouvelles
  pages (`_pensions.html`, `_taux_global.html`, `_regimes.html`, `_matrice.html`…) : leur
  retraduction produira des liens morts dans les livres arabes tant que ces chapitres n'y sont pas
  déclarés. Déclarer les chapitres arabes dans la même passe que ces retraductions.

- **Les caisses ont quitté ce livre le 4 octobre 2026** : cadre comptable et budgétaire, et les
  trois figures de la rétrospective CNSS par régime et par branche, dans le livre « Les caisses de
  sécurité sociale » (voir sa section ci-dessous). Ce livre garde le prélèvement, dont
  `#fig-cotisations-branches-1990-2004` et `#fig-cotisations-cnss`.

- **Cotisations par branche, 1990-2004 — fait le 3 octobre 2026** (`#fig-cotisations-branches-1990-2004`, après `#fig-cotisations-cnss`), tirées de la rétrospective financière 1990-2004 de la CNSS (`cnss-retrospective-1990-2004`, exemplaire papier numérisé ; série `cnss-retrospective-ressources-emplois` snapshotée le 3 octobre 2026). Comptes de bilan, non encaissements : écart de −1,13 % à −0,81 % avec la série encaissée en 2000-2004, inexpliqué. Les notes du document datent la réduction de 2 points de la branche familiale par la loi n° 97-4 au 1er octobre 1996, date que la loi n'énonce pas : à confronter à la datation du taux global (`#sec-cot-taux-unique`). **221 valeurs de 1999** (et quelques-unes de 2000) masquées par la reliure restent à lire sur l'original papier (tunisia-data#26) ; en attendant, la figure trace des estimations hachurées ou creuses. Quand le classeur revient : réinjecter dans tunisia-data, relancer `figtools.refresh_cache("cnss-retrospective-ressources-emplois")`, puis relire la note de lecture, qui cite des montants. Depuis le 3 octobre 2026, la figure a trois vues : millions de dinars, % du PIB (PIB du ministère des Finances, série `irpp-ratios`, rupture de base des comptes nationaux marquée en 1997, non corrigée) et % du total des ressources de la CNSS (tableau de l'ensemble, page 78, toutes branches).
- **Accidents du travail (§ sec-cot-at)** : les décrets n° 95-538 et 99-1010 sont lus
  dans les deux éditions (taux, entrée en vigueur au 1er janvier 1995 et au 1er avril
  1999). Les deux échelles sont engendrées, avant et après transfert du point
  (`tables/atmp_1995.md`, `tables/atmp_1999.md`). Restent : les forfaits des
  articles 4 à 7 et la modulation des articles 10 à 27 (openfisca-tunisia#471), dont
  l'édition arabe des articles 4 à 7 (JORT n° 30 de 1995, pp. 691-692) reste à lire à
  l'image ; le financement sous la loi n° 57-73. La fiche `r-atmp-echelle-modificatifs`
  ne couvre que les intitulés : le plein texte reste à parcourir.
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
5. La compensation (Caisse générale de compensation : produits de base, carburants, électricité, transport) — sources déjà collectées sur l'ancien portail du ministère des Finances (`tunisia-data/sources/minfinances-portail-ancien.md`).

**Fiscalité**

6. Droits d'enregistrement et de timbre ; fiscalité des mutations immobilières.
7. Droits de douane.
8. Dépenses fiscales et régimes d'incitation (code d'incitation aux investissements, loi de 2016, entreprises totalement exportatrices, développement régional) — documents Banque mondiale 2014 collectés.
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

## Citations répétées — suggestion, non engagée (4 octobre 2026)

Une même référence revient parfois à chaque phrase : le code de l'IRPP et de l'IS (`code-irpp-is-1990`) 31 fois dans `fiscalite/_impot_revenu.qmd` ; dans le volume VII en préparation (branche locale), la loi n° 97-11 jusqu'à 28 fois par chapitre et Dafflon et Gilbert 56 fois dans le chapitre des notions. La parenthèse « (loi n° … du …, art. 3) » alourdit la lecture sans rien apporter que le numéro d'article. Suggestion, à décider par l'humain avant toute mise en œuvre :

1. **Source principale déclarée en tête de section** : « Sauf mention contraire, les articles cités dans cette section sont ceux du code … [@clé]. » ; ensuite « (art. 3) » ou « l'article 35 dispose… » en clair, sans citation ; toute autre source reste citée en place. Même chose pour une doctrine suivie de bout en bout (« Les définitions de ce chapitre suivent … », puis « (p. 23) »).
2. **Une citation par paragraphe** plutôt que par phrase quand un texte court tout le paragraphe (`[@clé, art. 1 à 5]`).
3. **Tableaux** : une ligne « Sources » sous le tableau plutôt qu'une citation par cellule.
4. **Contrôle** dans `scripts/verifier.sh` : une même clé citée plus de N fois (N = 4 ?) dans une section est signalée.

Écartés : notes de bas de page (changement de style CSL pour tout le précis) ; suppression des articles (perte d'information). À prévoir côté traduction : les locateurs en clair « (art. 3) », hors citation, devront être protégés comme le sont aujourd'hui ceux des citations (`translate_sync.restore_locators`). Ordre envisagé : volume VII, puis IRPP, caisses, cotisations, un volume par PR.

## Les finances locales

Volume créé le 4 octobre 2026 (`precis/fr/finances_locales/`), d'après le plan
`docs/notes/fiscalite-locale-plan.md` (quatre mouvements, les notions avant le droit). Le
livre arabe a son `_quarto.yml` et ses références ; il est sauté au rendu tant que la
traduction n'a pas livré `index.qmd`.

- **Présentation — rédigée le 4 octobre 2026** (`index.qmd`, `#sec-fl-presentation`) : objet
  du volume, quatre mouvements, frontières avec « La fiscalité » (impôt foncier de 2014, IRPP et
  IS) et avec « Rémunérations publiques ». Les trois chapitres des ressources propres y sont
  renvoyés par `@sec-` ; les chapitres d'institutions, des transferts et de la longue période
  restent annoncés sans renvoi, faute d'exister. La phrase sur la TCL s'appuie désormais sur le
  code de la fiscalité locale (art. 35 et 37), et non plus sur Dafflon et Gilbert.
- **Trois chapitres des ressources propres — rédigés le 4 octobre 2026**, d'après la note
  `docs/notes/finances-locales-impots-locaux.md` (textes lus au JORT, valeurs relues à l'image
  en FR et en AR) : `_impots_immeubles.qmd` (`#sec-fl-immeubles` : TIB et TNB, structure du
  code, barèmes de 1997, 2008 et 2017 en tableaux à onglets, réformes de 1998 à 2025, pénalité
  de retard), `_impots_activite.qmd` (`#sec-fl-activite` : TCL et taxe hôtelière, minimum en
  onglets, maximum jusqu'en 2011, réformes de 2002 à 2024, taux), `_taxes_redevances.qmd`
  (`#sec-fl-taxes` : chapitres V à VIII du code, décret de tarifs n° 2016-805 lu le 4 octobre
  2026 en français, marges laissées aux collectivités, code des collectivités locales,
  art. 137, 139-141, 391-392). Tous les tableaux de paramètres sont faits main et portent le
  TODO de remplacement par un tableau engendré : aucun de ces paramètres n'est dans la base.
  Cinq fiches RECHERCHE versées (`r-cfl-*`) : prix de référence, tarif TNB et minimum TCL
  après 2017 ; décrets intermédiaires 1997-2007 ; modificatifs de la taxe hôtelière.
- **Lacunes des chapitres des ressources** (TODO des `.qmd`), toutes **lisibles dans le
  corpus** sauf mention :
  - code des collectivités locales : date d'entrée en vigueur des dispositions budgétaires
    (dispositions finales, édition arabe du JORT n° 39 de 2018) ; décrets transitoires de
    l'art. 391 (à chercher) ; délibérations tarifaires communales, au *Journal officiel des
    collectivités locales*, **hors corpus** ;
  - portée du § 10 de l'art. 59 du décret-loi n° 2022-79 sur la pénalité de 1,25 % de la TIB
    (texte lu, interprétation à trancher) ;
  - barème des parkings récrit par la LF 2003, art. 79, à transcrire (JORT n° 102 de 2002) ;
  - grilles du décret n° 98-1428 et de ses modificatifs, et du décret n° 2016-805 (lu, non
    transcrit ; l'édition arabe fait foi) ;
  - antécédents abrogés en 1997 (décrets de 1887 à 1956, lois n° 71-41, 75-34 et 75-39) ; les
    fascicules de 1975 sont au corpus, ceux d'avant 1956 restent à obtenir ;
  - art. 39 de la LF 1993 et décrets des zones municipales touristiques ; art. 7 initial du
    décret-loi n° 2020-33 ; art. 7 de la loi organique du budget des collectivités locales ;
  - articles d'amnistie de la LF 2026, de la loi n° 2006-25 et du décret-loi n° 2006-1 ;
  - arrêtés communaux fixant le prix de référence de la TIB, **hors corpus**.
- **Trois chapitres des institutions — rédigés le 5 octobre 2026** (branche
  `docs/finances-locales-institutions`), d'après trois notes documentaires établies sur le JORT :
  `_histoire.qmd` (`#sec-fl-histoire`, note `finances-locales-histoire.md` : loi municipale de
  1957, conseils de gouvernorat de 1957 et 1963, Constitution de 1959 et art. 71 de 2002, lois du
  14 mai 1975, conseils régionaux de 1989, 2011, Constitution de 2014, carte communale, code de
  2018, Constitution de 2022, décrets-lois de 2023, loi organique n° 2025-4) ;
  `_competences.qmd` (`#sec-fl-competences`, note `finances-locales-competences.md` : loi organique
  des communes, loi n° 89-11, catégories de compétences du code, art. 11-28, 234-244, 293-298,
  356-358, instances nationales, contrôle des actes, depuis 2023) ; `_budgets.qmd`
  (`#sec-fl-budgets-comptes`, note `finances-locales-budgets.md` : loi n° 75-35 lue à l'image,
  modifications de 1979 à 1997, refonte de 2007, série des seuils d'approbation de 1975 à 2017
  — décrets n° 77-320, 86-1036 et 89-280 relus à l'image le 5 octobre 2026, effet du décret
  n° 89-280 au 1er janvier 1989 —, code de 2018, art. 126-199 et 383, loi organique n° 2025-4).
  Entrée en vigueur des règles budgétaires du code pour les communes : budgets de 2019, les
  résultats définitifs des municipales ayant été proclamés par les décisions de l'ISIE n° 2018-12
  et suivantes, du 17 mai au 12 juin 2018 (JORT n° 46 à 50 de 2018, lus le 5 octobre 2026). Le
  tableau des seuils est fait main et porte le TODO de remplacement par un tableau engendré.
  Sept fiches RECHERCHE versées : `r-fl-loi-competences-partagees`,
  `r-fl-elections-municipales-apres-2023`, `r-lob-cl-seuil-approbation-apres-2017`,
  `r-ccl-2018-nomenclature-art167`, `r-fl-dissolutions-2011`,
  `r-fl-constitution-2014-numero-special`, `r-fl-nombre-communes`. Quinze notions au glossaire
  (compétences propres, partagées, transférées ; district ; conseil local ; délégation spéciale ;
  instances nationales ; notions budgétaires), dont trois `valide`. Les renvois de `index.qmd`
  vers ces chapitres restent à poser à la réunion des branches.
- **Lacunes des chapitres des institutions** (TODO des `.qmd`), **lisibles dans le corpus** sauf
  mention :
  - lois organiques n° 85-43, 91-24, 95-68 et 2006-48 (modificatifs de la loi organique des
    communes) ; fin du texte et édition arabe de la loi n° 75-33 ; sort de la loi n° 75-33 après
    le code de 2018 ;
  - art. 38-41 de la LF 1980 (lus sur OCR, à relire à l'image) ; date de dépôt du JORT n° 38 de
    1994 (loi organique n° 94-44) ; date de publication du décret n° 75-485 au pied du fascicule ;
  - textes de création des agences nationales citées par Dafflon et Gilbert et décret
    n° 2004-1182 (Centre de formation et d'appui à la décentralisation, couche texte décalée) ;
  - vote des budgets communaux depuis la dissolution de 2023 ;
  - numéro spécial du JORT du 10 février 2014 (Constitution), **à obtenir** (absent de pist.tn
    et de jort_cache) ; texte arabe de la Constitution de 2014 ;
  - nombre des conseils municipaux dissous en 2011-2012 et nombre de communes entre 1957 et 2014 ;
  - code de la comptabilité publique et lois sur la Cour des comptes, non lus.
- **Lacunes des chapitres des ressources levées par ces notes, à reporter à la réunion** :
  l'entrée en vigueur des dispositions budgétaires du code pour les communes (premier point du
  TODO de `_taxes_redevances.qmd`, § « La transition ») est établie au 1er janvier 2019 ; l'art. 7
  de la loi organique du budget est lu (note `finances-locales-budgets.md`, § 1.1 et 1.3). Les
  chapitres 6 à 8 n'ont pas été modifiés.
- **Livre arabe** : les trois chapitres sont déclarés en commentaire dans
  `precis/ar/finances_locales/_quarto.yml`, à décommenter quand la traduction sera livrée.
- **Notions — rédigé le 4 octobre 2026** (`_notions.qmd`, `#sec-fl-notions`) : décentraliser,
  budget local, ressources propres, transferts, mesurer, et tableau des notations. Source
  unique : Dafflon et Gilbert, AFD 2018 (`dafflon-gilbert-2018`), lue dans l'exemplaire HAL
  (p. 11-30, 64-69, 79, 81-86, 150-157, 195-207, 251-252). Les manuscrits de 2013 (encadrés 4-5
  et 4-6, § 5.1) ont été comparés : ils sont repris à l'identique dans le livre, qui seul est
  cité. Aucune valeur tunisienne.
- **Notions non définies faute de source lue** : épargne brute (le livre ne la définit
  qu'en droit tunisien, comme solde du titre I, p. 84) ; dépendance aux transferts ; fonds
  commun, comme notion générale ; établissement public. À sourcer dans Dafflon et Madiès, AFD,
  *Notes et documents* n° 42 (2008) — le fichier téléchargé le 4 octobre 2026 n'en contient que
  six pages, à obtenir en entier — ou à traiter dans les chapitres de droit.
- **Glossaire — 40 notions, toutes `provisoire`** : les termes arabes ne sont mis en regard
  des notions par aucun texte bilingue. Treize figurent, à la lettre ou presque, dans l'édition
  arabe du code des collectivités locales (JORT n° 39 de 2018 ; article en commentaire de
  chaque entrée), dont l'édition française n'est pas identifiée (absente de jort_cache, du
  corpus local et de pist.tn le 4 octobre 2026). Les autres sont proposés sans attestation.
  À trancher par un arabophone : « التعديل » pour péréquation (le code emploie aussi
  « التسوية », et Dafflon et Gilbert rendent l'article 136 de la Constitution de 2014 par
  « régulation et adéquation », p. 205) ; « الرسم » pour la taxe au sens des finances
  publiques ; « معلوم الاستعمال » pour la redevance d'utilisation.
- **Références à lire avant les chapitres suivants** : Dafflon et Gilbert, PARD 2021
  (transferts) et 2022 ; Hammami, Dafflon et Gilbert, PARD 2021 (compétences) ; Dafflon, RTF
  n° 25 (2017) ; voir `docs/notes/biblio-fiscalite-locale.md`.
- **Questions du plan restées ouvertes** : chapitre propre aux régions ; taxes affectées à
  des fonds hors budgets locaux.
- **Transferts de l'État — rédigé le 5 octobre 2026** (`_transferts.qmd`, `#sec-fl-transferts`),
  d'après la note `docs/notes/finances-locales-transferts.md`, close par anticipation : lois
  n° 75-36 et 75-37, LF 1982 (art. 27), 1985 (art. 63), 1986 (art. 68), 1987 (art. 44, 92, 94),
  1988-1991 (prélèvements et reconduction de la réserve), 1990 (tableau « L » : 80 MD), 1992
  (art. 80), décret n° 92-308, loi n° 95-45, loi n° 2000-60, LF 2007 (art. 11), LF 2014 (art. 12)
  lus au fascicule ; tableau de la répartition légale 1976-2017 fait main (TODO de tableau
  engendré). L'ancre des notions passe de `#sec-fl-transferts` à `#sec-fl-notions-transferts`.
  Fiche `r-fccl-repartition-reserve-2014-2017`. **Lacunes, toutes lisibles dans le corpus** :
  - décrets de répartition de la réserve 1993-2013 (vingt-deux, non lus ; les AR postérieurs
    à 2000 sont aussi sur le miroir iort) ; décret n° 92-308 à relire à l'image (océrisation) ;
  - montant du fonds, LF par LF, 1987-2017 (seul 1990 est lu) ; LF 1977-1979 et arrêtés de
    1975-1983 ; clauses d'effet des LF 1982, 1985, 1986 et 1992 ; pages AR de la plupart des
    textes lus ;
  - LF 2018, art. 11 (texte, effet) ; code des collectivités locales (ressources transférées,
    péréquation, art. 392) ; LF 2013 art. 13-15, décret n° 2013-2797, LF 2021 art. 13 :
    seuls leurs intitulés sont cités ;
  - texte fondant la réserve de 15 % des agrégats DGCT de 2018-2019 ;
  - décrets et arrêtés de la CPSCL (77-212 … 2016-367, loi n° 2001-56) ;
  - subventions d'investissement, PIC, PRD, dotation exceptionnelle 2011-2012 : aucune source
    primaire lue ;
  - divergence 82 / 50,8 MD du fonds en 1990 : non tranchée (le JORT donne 80 MD votés).
- **Longue période — rédigé le 5 octobre 2026** (`_longue_periode.qmd`,
  `#sec-fl-longue-periode`) : six figures à onglets (`figures/finances_locales.py`), lues par
  `figtools.series()` sur les séries de tunisia-data snapshotées dans `precis/_seriescache/`
  (communes 2008-2023, CPSCL 2005-2024, INS trois bases, Banque mondiale 1985-2012, PIB des
  comptes de la nation) ; les fichiers Banque mondiale 1992 et 1997, absents du catalogue de
  l'entrepôt sous un identifiant propre, sont snapshotés par
  `scripts/snapshot_finances_locales_bm.py` et déclarés par `register_provenance` — à retirer
  quand tunisia-data les déclarera. Références versées : `dgct-donnees-ouvertes`,
  `cpscl-etats-financiers`, `wb-msip-1992`, `wb-mdp2-1997`, `wb-pforr-pad-2014`,
  `wb-pforr-ta-2014`, décrets n° 2016-600 à 602 ; `ins-cnat-2015` couvre déjà les éditions en
  bases 1983 et 1997 (pas de clé séparée). **Lacunes** : dépenses, investissement et
  endettement des communes non encore suivis (données présentes) ; définitions du ratio
  d'autonomie et du taux de recouvrement de la TIB publiés par la DGCT ; explication de la TIB
  de 2019 (76 MD) ; écart DGCT / somme des communes sur les dépenses 2018-2019.
- **Livre arabe** : `_transferts.qmd` et `_longue_periode.qmd` déclarés en commentaire dans
  `precis/ar/finances_locales/_quarto.yml`. Glossaire : `fonds-commun-collectivites-locales`,
  `reserve-fonds-commun`, `cpscl` (termes arabes du JORT).

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
| `_tva.qmd` | historique sorti de l'attaque | déductions, achats en suspension et obligations restent à écrire sur les articles du code |
| `_impot_revenu.qmd` | conforme, à sa manière | rien sur la forme ; restent deux sections à ÉCRIRE, voir plus bas |
| `retraites/_secteur_*.qmd` | **rangés par mécanisme, et c'est bien** | ne pas y appliquer le plan type |
| `_regime_indiciaire.qmd` | fait le travail sous d'autres noms | ne rien reprendre sur la forme |

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

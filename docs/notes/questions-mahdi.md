# Décisions qui reviennent à Mahdi

Ouvert le 24/11/2026, au fil du plan par opération (`docs/notes/plan-par-operations.md`). Chaque entrée donne la question, les options, la recommandation et ce que l'attente bloque. Quand l'option recommandée est réversible sur une branche, elle est **appliquée par défaut, à confirmer** ; sinon, rien n'est fait.

## M1. Le volume de la fiscalité dans un plan par opération
- **Tranchée par Mahdi le 25/11/2026** : option (b), le volume entier en trois parties (#869).
- **Question** : faut-il scinder le volume (62 sections déplacées selon la mesure) entre D.2, impôts sur les produits (partie II), et D.5, impôts sur le revenu (partie III), ou le garder entier ?
- **Options** :
  - (a) scinder en deux volumes ;
  - (b) garder le volume, avec des parties internes par opération ;
  - (c) garder tel quel.
- **Recommandation** : (b). Le lecteur garde un seul livre de la fiscalité, et la somme par opération reste lisible.
- **Bloque** : la réorganisation de la fiscalité. La proposition sera faite sur une branche à part, non fusionnée.
- **Coût de changer** : (a) déplace 62 sections et crée deux volumes, avec leurs pages-relais arabes ; (b) ne déplace que des titres, à l'intérieur du volume.

## M2. Taxe de formation professionnelle et FOPROLOS (D.29)
- **Question** : ces deux prélèvements doivent-ils quitter le volume des cotisations ?
- **Options** :
  - (a) les déplacer vers les fonds spéciaux du Trésor (fiscalité) ;
  - (b) les déplacer vers un futur chapitre D.29 ;
  - (c) les laisser, avec le bloc « Dans les comptes ».
- **Appliqué par défaut, à confirmer** : (c). Les deux sections portent le bloc et le renvoi au compte, sans déplacement.
- **Bloque** : rien.
- **Coût de changer** : (a) ou (b) déplacent 2 sections et réécrivent leurs renvois par script ; le bloc « Dans les comptes » suit la section sans modification.

## M3. Les 176 sections sans opération
- **Question** : où ranger les sections qui ne se rattachent à aucune opération (temps de travail, rupture du contrat, logement social, offices, redevances…) ?
- **Options** :
  - (a) un « cadre institutionnel » en tête de chaque partie ;
  - (b) une partie 0 commune.
- **Recommandation** : (a).
- **Bloque** : la réorganisation du marché du travail et des entreprises publiques. Une proposition sera faite sur une branche à part, non fusionnée.
- **Coût de changer** : à peu près le même pour les deux options, puisque les 176 sections sont à classer une à une dans les deux cas ; seul diffère l'endroit où on les range.

## M4. Les loyers et redevances (D.45)
- **Question** : faut-il créer un chapitre pour D.45 (2 227,8 MD reçus par les administrations publiques en 2023), qu'aucune section ne traite ?
- **Recommandation** : oui, dans un futur chapitre des revenus de la propriété.
- **Bloque** : la couverture de D.4.

## M5. Les pages de synthèse par institution
- **Question** : où placer les pages de synthèse des institutions (caisses, compensation, entreprises publiques, collectivités) ?
- **Options** :
  - (a) dans le volume actuel de chaque institution ;
  - (b) regroupées dans la partie 0.
- **Recommandation** : (a), qui ne demande aucun déplacement.
- **Bloque** : la scission des 13 chapitres « à cheval ».
- **Coût de changer** : (b) déplace les sections d'institution (69 selon la mesure) et en réécrit les renvois.

## M6. La date de consultation des éditions des comptes de la nation
- **Mise à jour du 25/11/2026** : l'année d'édition est imprimée en couverture (« Edition 2026 » pour 2021-2025) ; seule la date de consultation manque.
- **Question** : aucune liste ne donne la date de consultation des 15 éditions. Faut-il la relever (date de téléchargement des fichiers) ou la laisser vide ?
- **Recommandation** : la laisser vide tant qu'aucune trace n'existe, et la noter à chaque nouveau téléchargement.

## M7. La relecture des bases 1997 et 1983
- **Question** : faut-il poursuivre la relecture page par page des 130 équilibres restants de la base 1997, ou fusionner #152 en l'état (dépôt de données), les écarts restant listés ?
- **Recommandation** : fusionner en l'état, puisque les écarts sont listés et non masqués ; la relecture continuera dans une branche ultérieure.

## M8. Les fusions refusées dans le dépôt de données
- **Question** : #153 (relecture du TOF) et #154 (catalogue) attendent une fusion sur main, que la protection du poste a refusée. Faut-il ajouter la règle `Bash(gh pr merge:*)`, ou fusionner toi-même ?
- **Bloque** : #155 et #156, empilées sur #153.

## M9. La structure de la base des comptes nationaux (dépôt de données)
- **Question** : quel format pour l'accès structuré aux comptes nationaux ?
- **Options** :
  - (a) SQLite reconstruite depuis les CSV ;
  - (b) DuckDB ;
  - (c) une base qui ferait source.
- **Appliqué** : (a), parce que SQLite sert déjà à l'inventaire, sans nouvelle dépendance ; les CSV versionnés restent la source.
- **Coût de changer** : passer à DuckDB ne toucherait que `tunisia_data/cnat/base.py`, les requêtes restant en SQL standard.

## M10. Le raccordement des bases (1983, 1997, 2015)
- **Question** : faut-il raccorder les séries des comptes entre bases ?
- **Options** :
  - (a) publier chaque base séparément, ruptures marquées ;
  - (b) rétropoler par des taux de croissance ;
  - (c) suivre la méthode de l'INS si elle existe (question C3 de l'expert).
- **Appliqué par défaut** : (a), qui n'invente aucune valeur.
- **Coût de changer** : (b) ou (c) ajoutent des valeurs de nature « calculé », avec leur généalogie ; aucune valeur lue n'est modifiée.

## M11. Branchement de l'ouvrage sur la base (clés stables et sources dans le cache)
- **Question** : quand brancher le cache des séries et le registre des postes sur les sources de la base (page, édition, empreinte) ?
- **Recommandation** : après la fusion de #155 et #156 sur main. Le cache est régénéré depuis main, et un tableau qui dépendrait d'une branche non fusionnée serait écrasé.
- **Bloque** : le contrôle bloquant dans verifier.sh (« une valeur citée remonte à une publication enregistrée »).

## M12. Le domicile du compte financier
- **Question** : où domicilier le compte financier (F.1 à F.8) ? Il est aujourd'hui dispersé entre les garanties et les cessions des entreprises publiques et le crédit agricole.
- **Options** :
  - (a) une partie « Financier » du futur plan, avec la monnaie et le crédit du volume cadre ;
  - (b) le volume des entreprises publiques pour l'État actionnaire et prêteur.
- **Appliqué par défaut** : la page « Les comptes des secteurs » porte le tableau par secteur (#870), sans déplacer de section.
- **Coût de changer** : (a) déplace une vingtaine de sections (cessions, garanties, crédit agricole) ; (b) n'en déplace aucune.

## M13. Publications à récupérer (lots B et C)
- **Question** : peut-on télécharger ces publications officielles ? L'inventaire de l'entrepôt (`catalogue.sqlite`) ne les contient pas ; la recherche y a été faite le 25/11/2026.
- **Liste**, avec les titres exacts à confirmer sur les sites :

| Organisme | Publication | Année | Ce qu'elle lève |
|---|---|---|---|
| Banque centrale de Tunisie | balance des paiements annuelle | 1987-2024 | **déjà dans l'entrepôt** (38 fichiers, archives de la BCT) : rien à télécharger |
| CNSS | rapport annuel ou états financiers | 2021-2023 | D.61 et D.62 de la CNSS en 2023 (la série de l'entrepôt s'arrête en 2020) |
| CNRPS | rapport annuel ou états financiers | 2021-2023 | D.61 et D.62 de la CNRPS |
| CNAM | rapport annuel (dépenses de soins) | 2021-2023 | passage des soins à D.631 ; seules les statistiques d'accidents du travail de 2023 sont inventoriées |
| Ministère des Finances | loi de règlement du budget ou résultats définitifs d'exécution | 2023 | recettes douanières et TVA par nature, restitutions (E1, A4) |
| Ministère de l'Intérieur (collectivités locales) | comptes définitifs des collectivités | 2023 | D.73 définitif (la valeur de l'entrepôt est provisoire, au 10/01/2024) |

- **Appliqué par défaut** : rien n'est téléchargé, puisque tout téléchargement demande ton accord.
- **Coût de changer** : une fois l'accord donné, la procédure existante de collecte du dépôt de données (`docs/agents/collecteur-donnees.md`) s'applique.

### Résultat de la collecte du 25/11/2026 (accord de Mahdi du 25/11/2026)
- **Récupéré** sur les sites officiels, avec adresse, date et empreinte dans les listes `sources/*-urls.csv` du dépôt de données :
  - ministère des Finances : rapport semestriel de l'exécution du budget de l'État à fin décembre 2023 (31 pages) et résultats provisoires de l'exécution du budget à fin décembre 2023 ;
  - CNSS : les huit fichiers de la page « La CNSS en chiffres » (états financiers, budget de gestion, recettes, dépenses des régimes, prestations familiales, pensions, annuaire), dont les données s'arrêtent en 2020, avec un budget de gestion jusqu'en 2022.
- **Introuvable sur les sites officiels** :
  - CNSS : comptes et données de 2021 à 2023 (la page est à jour au 29/06/2021) ;
  - CNRPS : rapport d'activité ou états financiers postérieurs à 2018 (le site public ne donne que les rapports d'accès à l'information) ;
  - CNAM : statistiques financières de 2023 (seules les statistiques d'accidents du travail de 2023 sont en ligne, déjà dans l'entrepôt) ;
  - loi de règlement du budget 2023 ;
  - comptes définitifs des collectivités de 2023.
- **Note technique** : les sites de la CNSS et de la CNAM servent un certificat dont la chaîne est incomplète. Le téléchargement a vérifié le certificat avec l'intermédiaire officiel de l'autorité (Sectigo), tiré de l'adresse que le certificat indique ; aucune vérification n'a été désactivée.

## M14. Prolonger la reconstruction en 2021-2023 par le rapport sur les entreprises publiques

L'année de référence est 2020 (dernière année où toutes les sources existent ; année du COVID). Le rapport du ministère des Finances sur les entreprises publiques (éditions LF 2024 et LF 2025) donne les comptes de résultat des trois caisses pour 2020-2023, désormais extraits dans le dépôt de données (`minfin-ep-caisses`), avec leur statut imprimé : 2021-2022 réalisés, 2023 provisoire (CNSS, CNRPS) ou estimation (CNAM). Il donne les recettes (cotisations : celles de la CNSS en 2020 égalent ses propres chiffres, 3 430 MD), mais ni les pensions ni les prestations de soins, fondues dans les charges d'exploitation.

Question : faut-il chiffrer en 2021-2023 les cotisations des trois caisses par cette source, en marquant « rapport du ministère » et le statut, et laisser les pensions et les soins sans montant ces années-là ? Défaut proposé : oui, pour les cotisations seulement, avec l'année 2020 maintenue comme référence.

## M15. La classification économique du budget de l'État vers le SCN

Le budget par nature (rémunérations, moyens, interventions, équipement, prêts) ne descend pas au niveau des opérations du compte de l'État : 15 opérations sur 32, de 172 à 2 046 MD chacune en 2020, restent « à déterminer » (`docs/notes/etat-operations-non-chiffrees-2026-11-25.md`). La table officielle serait la classification économique des charges et des recettes du manuel de statistiques de finances publiques 2014 du FMI, croisée avec la nomenclature budgétaire tunisienne (articles et paragraphes du titre I). Question : récupérer le manuel (site du FMI) et une exécution du budget par article et paragraphe (ministère des Finances), pour établir les correspondances ligne par ligne ? Le téléchargement depuis le site du FMI attend votre accord.

## M16. Le vocabulaire de comptabilité nationale quand le SCN 2008 et l'INS divergent — résolue

**Résolue le 25/11/2026 (19 h 40)** : « terme de l'INS suivi du code SCN, sauf définition différente ». Quand la définition est la même, l'ouvrage écrit le terme imprimé par l'INS suivi du code du SCN, par exemple « impôts courants sur les revenus et le patrimoine (D.5) » ; il n'emploie un autre terme, en disant l'écart, que si l'INS et le SCN désignent deux choses différentes. Nature de chaque écart et preuve : colonnes `nature_ecart` et `preuve` de `docs/conventions/vocabulaire-comptes-nationaux.csv` ; règle écrite dans `docs/conventions/ecrire-dans-le-precis.md`.

La table `docs/conventions/vocabulaire-comptes-nationaux.csv` (53 termes, références au SCN 2008 en français, paragraphe et page) relève 14 termes où l'INS imprime un autre mot que le SCN : excédent d'exploitation ou revenu mixte (INS : « revenu d'exploitation ») ; variations des stocks (« variation de stocks ») ; revenus d'investissements attribués aux assurés (« revenus de la propriété attribués aux assurés ») ; salaires et traitements (« salaires bruts ») ; impôts du type TVA (« TVA non déductible ») ; impôts sur les produits hors TVA et commerce extérieur (« autres impôts sur les produits ») ; autres subventions sur la production (« subventions sur la production ») ; revenus distribués des sociétés (« revenus distribués par les entreprises ») ; impôts courants sur le revenu, le patrimoine, etc. (« impôts courants sur les revenus et le patrimoine », « impôts directs ») ; impôts en capital (« impôts sur le capital ») ; aides à l'investissement (« subventions d'investissement ») ; sociétés financières (« institutions financières ») ; administrations publiques (« administration publique ») ; reste du monde (« extérieur »).

Dans les pages françaises, hors glossaires : « impôts directs » 20 fois, « subventions d'investissement » 16, « revenu d'exploitation » 8, « institutions financières » 4, « salaires bruts » 3, « prestations sociales en espèces » 2, « variation de stocks », « consommation publique », « consommation privée » une fois chacun. Plusieurs sont des termes du budget ou des textes, à garder dans ce sens.

Question : dans le texte de l'ouvrage, faut-il retenir le terme du SCN (en citant entre guillemets le libellé de l'INS quand on reprend un de ses tableaux), ou le terme de l'INS ? Défaut proposé : le SCN dans le texte, l'INS entre guillemets quand il est cité ; les termes du budget et des lois restent tels quels. Rien n'est changé avant votre réponse.

## M17. Les pensions de 2021 à 2023 (D.62 versé par la sécurité sociale) — résolue
- **Constat** : les deux postes de D.62 de S1314, `pensions` (CNSS, série `cnss-pensions-versees`) et `pensions-cnrps` (CNRPS, série `cnrps-regime-general-finances`), s'arrêtent en 2020 : 4 013,6 et 5 849,3 MD, soit 95,5 % du D.62 de S1314 (10 329,3 MD, édition 2020-2024). En 2021-2023, D.62 de S1314 vaut 10 577,5, 11 704,5 et 12 602,5 MD (édition 2021-2025 ; `precis/_seriescache/cnat-secteurs.csv`), sans poste chiffré. La part du montant couverte de S1314 tombe de 85,3 % en 2020 à 48,4 %, 42,4 % et 42,3 % (`precis/fr/compte-couverture-annees.csv`) ; D.62 pèse 36,3 à 37,8 points du compte de S1314 ces trois années.
- **Où l'on a cherché** (25/11/2026) : le rapport sur les entreprises publiques (`minfin-ep-caisses`, LF 2024 et LF 2025) ne porte, pour les caisses, ni pensions ni charges techniques, seulement le total des charges d'exploitation (M14) ; la fiche `sources/cnrps-publications.md` du dépôt de données relève qu'aucun rapport d'activité de la CNRPS postérieur à 2020 n'a été trouvé ; la série `cnss-produits-charges-techniques` note que les charges techniques de la CNSS ne sont plus publiées telles quelles après 2020 ; la collecte du 25/11/2026 (M13) n'a trouvé sur les sites officiels ni comptes de la CNSS de 2021 à 2023 ni rapport de la CNRPS postérieur à 2018. Le dépôt de données n'a que la série calculée `cnrps-taux-equilibre`, dont les dépenses du régime de retraite 2021-2023 (6 517,3 ; 6 699,1 ; 7 383,6 MD) sont des ESTIMATIONS : charges d'exploitation de la caisse entière × part des pensions de 2019-2020 (0,9546). Les rapports annuels de performance du ministère des Affaires sociales 2021-2023, dans le dépôt de données, donnent des ratios charges/produits de la branche pensions, pas des montants (`sources/mas-rap-pap-cnrps.md`).
- **Ce que disent les règles** : la colonne `nature` du registre `precis/fr/postes-comptables.csv` ne porte que « lu » (31 postes) ou rien (7) ; aucun script ni test ne lit cette colonne. L'interdiction d'estimer est écrite, non codée : `scripts/reconstruire_comptes.py` (docstring, l. 14 : « un montant vide (jamais estimé) »), `scripts/reconstruire_secteurs.py` (l. 2 : « rien d'estimé »), `scripts/sommaire_comptes.py` (l. 9 : « Rien n'est estimé ni déplacé ») et `precis/fr/compte-apu.qmd` (l. 31 : « il n'est jamais estimé »).
- **Options** :
  - (a) collecter les rapports annuels 2021-2023 de la CNSS et de la CNRPS (ou leurs états financiers), ou les comptes de la branche pensions du ministère des Affaires sociales, et chiffrer les deux postes par des montants publiés ;
  - (b) laisser D.62 de S1314 sans montant en 2021-2023, comme aujourd'hui (défaut de M14) ;
  - (c) poser un poste « estimé » tiré de `cnrps-taux-equilibre` (et d'une estimation analogue pour la CNSS), ce qui demande une valeur nouvelle de `nature`, une règle écrite qui la permette, un contrôle qui l'exclue de la justesse et un marquage dans les encadrés et les tableaux.
- **Recommandation** : (a), avec (b) tant que la collecte n'a rien donné. (c) mêlerait au compte reconstruit une estimation de l'ouvrage, que toutes les règles écrites excluent, et changerait la couverture de 2021-2023 de plus de 35 points sur la foi d'une part de 2019-2020.
- **Résolue le 25/11/2026 (19 h 39)** : (b), « laisser non chiffrées ». Les pensions de 2021-2023 restent sans montant tant qu'aucune publication des caisses ne les donne ; aucun poste estimé. La collecte (a) reste ouverte (`docs/notes/documents-manquants-annees-anterieures.md`).
- **Bloque** : la couverture de S1314 et la justesse de D.62 en 2021-2023 ; la liste de collecte du 25/11/2026 (`docs/notes/a-collecter-2026-11-25.md`) porte les documents de l'option (a).
- **Coût de changer** : (a) un versement par caisse dans le dépôt de données, puis deux postes de relais dans le registre, comme `cotisations-cnss-2021-2023` ; (c) une modification du registre, des scripts de reconstruction et de leurs tests, et des règles écrites.

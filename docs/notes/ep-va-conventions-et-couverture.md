# EP — valeur ajoutée : convention de mesure et couverture du secteur

**6 novembre 2026.** Après la collecte ciblée des états financiers de six grands EPIC non cotés
(ETAP, La Poste, SONEDE, SNCFT, TRANSTU, Tunisie Autoroutes), cette note fixe **la définition de VA
retenue** et mesure **quelle part de la VA du secteur public productif est désormais adossée à des
états financiers primaires** plutôt qu'estimée.

## 1. Convention de valeur ajoutée

Deux grandeurs normées coexistent, et elles divergent selon le traitement des **subventions
d'exploitation** :

- **VA aux prix de base** (mesure *préférée* du SNA 2008 / Eurostat) : inclut les **subventions sur
  les produits** (compensation d'un prix réglementé sous le coût, au prorata des unités vendues) mais
  **exclut les autres subventions sur la production** (compensations forfaitaires, couverture de
  déficit de service public). C'est aussi, de fait, la VA du **SIG du plan comptable** : `Production −
  Consommations intermédiaires`, les subventions d'exploitation n'étant réintroduites qu'au niveau de
  l'EBE (`EBE = VA + subventions d'exploitation − impôts & taxes − charges de personnel`).
- **VA au coût des facteurs** : = VA aux prix de base + toutes les autres subventions sur la
  production. C'est la mesure qu'affiche le SIG publié par STEG et celle qu'utilisait historiquement
  Eurostat (statistiques structurelles d'entreprises).

**Choix retenu** : la **VA aux prix de base est la grandeur primaire** (comparable entre pays et
conforme au SNA) ; la **VA au coût des facteurs est donnée en complément**. Le critère de partage
n'est pas « subvention dedans/dehors » en bloc, mais la **nature** de la subvention :

| Nature de la subvention | Traitement | EP concernées |
|---|---|---|
| **Sur les produits** (tarif réglementé sous le coût) | reste **dans** la VA prix de base | STEG (élec/gaz), SONEDE (eau) |
| **Service public / déficit** (autre subvention sur la production) | **hors** VA prix de base, visible au coût des facteurs | TRANSTU, SNCFT |
| Aucune subvention notable (marchande) | prix de base = coût des facteurs | Ciments, GCT, CPG, Poste, Tunisie Télécom, SOTRAPIL, Tunisie Autoroutes |
| **Pass-through** (commercialisation part de l'État, hydrocarbures transportés) | *autre problème* : gonfle revenus et achats ; caveat dédié | ETAP, Tunisair, SOTRAPIL (dans une moindre mesure) |

**Conséquence marquante** — TRANSTU : VA au coût des facteurs ≈ 134 MD (2020), mais **VA prix de base
≈ −5 MD** : le transport urbain de Tunis ne dégage quasiment aucune valeur ajoutée marchande propre,
il vit de la compensation de l'État. Le diagnostic de productivité doit le dire.

### Précisions après seconde collecte (6 nov. 2026)
- **SNCFT** : la compensation de service public est désormais **isolée** (tableau « Participation de
  l'État / compensation annuelle » des rapports annuels), 2010-2022 : de 28,3 à 40,8 MD. La **VA prix
  de base** (= VA − compensation) est donc disponible et chute de **84,5 MD (2010) à 9,5 MD (2022)**.
  Exclu de la compensation : le « gros entretien de la voie » (contribution d'infrastructure).
  2020 surestimé (~66 MD de compensation COVID logée dans les autres produits, non retirée) ; 2023
  non isolable.
- **SONEDE** : clarifié — la subvention d'**exploitation** est **minime** (0,04-5 MD) ; le soutien
  passe par la subvention d'**investissement** et la **subvention tarifaire (sur les produits)**, qui
  reste dans la VA prix de base. Donc **VA prix de base ≈ VA coût des facteurs** pour la SONEDE ; les
  « autres produits » exclus en 2015 n'étaient pas une subvention d'exploitation.
- **ONH** (Office National de l'Huile) : rejoint le groupe **exclu par nature** (STIR, Office des
  céréales) — il administre des crédits d'huile subventionnée (≈ 480 MD), ressources propres nulles,
  pas d'états financiers propres.
- Restent au coût des facteurs seulement : **CPG, GCT** (VA « posée » par la synthèse annuelle de
  l'entreprise, composantes et subvention non ventilées).

## 2. VA mesurée — 16 EP, 190 points EP×année sur états financiers primaires

| EP | Plage VA | Points | Nature |
|---|---|---|---|
| SOTRAPIL | 2000-2025 | 26 | marchande |
| Tunisair | 2000-2023 (trou 2001) | 23 | pass-through |
| ETAP | 2004-2024 | 21 | pass-through (caveat) |
| Ciments de Bizerte | 2009-2024 | 16 | marchande |
| SNCFT | 2010-2023 | 14 | service public |
| **El Fouladh** | 2012-2024 | 13 | marchande (sidérurgie) |
| CPG | 2004-2015 | 12 | industrie sous soutien |
| TRANSTU | 2010-2021 | 12 | service public |
| SOTUMAG | 2002-2024 (trous 2003-15) | 11 | marchande |
| STEG | 2014-2023 | 10 | produit |
| La Poste | 2015-2023 | 9 | marchande |
| **TTN** (Tunisie TradeNet) | 2017-2025 (trous 19-21) | 6 | marchande (service IT) |
| SONEDE | 2010-2016 (trous 12-13) | 5 | produit |
| GCT | 2010-2014 | 5 | industrie sous soutien |
| Tunisie Télécom | 2007-2009 | 3 | marchande |
| Tunisie Autoroutes | 2021-2022 | 2 | marchande |

Données et provenance (fichier + page) : `tunisia-data/sources/entreprises-publiques/grandeurs-*.csv`,
`consolidation-provenance.csv` (3 540 lignes, 40 EP, **0 valeur sans source**) et
`va-consolidee-ep-derniere-annee.csv`. Chaque valeur est lue ou calculée depuis un état financier
primaire. Séries continues longues : SOTRAPIL (26 ans), Tunisair (23), ETAP (21), Ciments (16).

## 3. Couverture de la VA du secteur

Sur l'**univers productif** (40 EP non financières, hors banques, caisses sociales et bureaux de
compensation), en prenant pour chaque EP sa **dernière année disponible** :

- **VA mesurée : ≈ 5 770 MD** (16 EP sur états financiers primaires) ;
- VA encore **proxytée** (personnel + résultat d'exploitation, borne basse) pour ~26 autres :
  ≈ 1 640 MD ;
- **⇒ ≈ 78 % de la VA du secteur productif est désormais mesurée** sur états financiers, contre
  **~46 %** avant la collecte (et ces 46 % reposaient encore sur un proxy pour ETAP, Poste, SONEDE…).
  La part reste à 78 % malgré 2 EP et ~90 points EP×année ajoutés : El Fouladh et TTN sont de faible
  VA face à ETAP/STEG ; le gain de la seconde collecte est surtout en **profondeur temporelle**.

**Mise en garde** : ce ratio agrège des années différentes (ETAP 2024, mais Tunisie Télécom 2009,
CPG 2010, GCT 2013 — des pics anciens). Il mesure « quelle part du secteur est adossée à des comptes
réels », pas une VA sectorielle d'une année donnée. Le proxy des 27 restantes est une borne basse
(il ignore dotations et impôts), donc la part mesurée est une **borne haute**.

Reste en proxy, par ordre de poids : OACA (~363), RNTA (~191), ONAS (~152), CTN (~128), OMMP (~121),
Pharmacie Centrale/PCT (~114), SNDP-Agil (~93). Murs confirmés (pas d'EF public) : RNTA, ONAS, OMMP,
OACA — EF primaires existants à la DGPPP mais non publics.

## 4. Backlog (à verser au durable)
1. **SONEDE 2012-2013 et 2017-2024** (site sonede.com.tn en HTTP 500 ; tenter le prospectus
   obligataire SONEDE sur la CMF) et **TRANSTU 2022-2023** (transtu.tn s'arrête à 2021) : états de
   résultat non récupérés — seuls les agrégats MdF (sans VA) versés pour les années récentes.
2. **SNCFT compensation 2023** non isolée ; **SNCFT 2020** VA prix de base surestimée (compensation
   COVID non retirée).
3. **Tunisie Télécom** (2010→), **GCT** (2015→), **STEG** (<2014, EF absents du corpus) : VA
   manquante — le ratio de couverture mélange les années.
4. **VA des EPIC murs** (RNTA, ONAS, OMMP, OACA, ONH) : obtenir les EF primaires auprès de la DGPPP.
5. **TTN 2019-2021** (EF manquants / 2 fichiers corrompus) ; **El Fouladh** effectifs 2012-2016, 2019.
6. **Tunisie Autoroutes** : série antérieure à 2021 (prospectus obligataires CMF) ; VA 2022 retenue
   **hors** l'élément exceptionnel de 324,4 MD (« autres produits », retraitement note 22).
7. **CPG 2006-2010** : valeurs issues d'un doc OCR (recoupées aux valeurs connues, mais à revérifier
   sur source propre) ; **CPG/GCT** : VA « posée », à recalculer depuis un état de résultat détaillé.

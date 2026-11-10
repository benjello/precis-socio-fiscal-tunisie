# Backlog — chantier annexe dette publique

Reports et lacunes du chantier `chantier/annexe-dette-publique`. À fusionner dans
`docs/notes/backlog-precis.md` par le rôle `archiviste-backlog` après relecture (évite les conflits
sur le fichier partagé pendant que d'autres chantiers tournent). Rien n'a été téléchargé dans les
dépôts : les séries ci-dessous sont **à rapatrier et indexer dans `tunisia-data`** avant d'être
engendrées en figures.

## Données à sourcer / rapatrier (lisible = URL publique vérifiée ; à obtenir = non encore récupéré)

### Dette extérieure (publique et garantie, PPG)
- **FAIT (9 nov. 2026)** : échéancier agrégé **et par créancier** rapatrié dans `tunisia-data`
  (`scripts/extract_ids_dette.py`, `build/dette_exterieure.py`, catalogue + fiche), snapshoté au
  cache (`dette-exterieure-echeancier`, `dette-exterieure-echeancier-creanciers`), et engendré en
  deux figures de l'annexe (`#fig-dette-echeancier`, `#fig-dette-echeancier-creanciers`). Clé CSL
  `wb-ids` versée (FR+AR). Reste : conditions moyennes `DT.INR.DPPG`/`DT.MAT.DPPG` non encore
  versées ; limite PPG extérieur seul, en USD, échéancier = dette déjà contractée.
- **Registre nominatif des prêts extérieurs** — JORT, 881 lois/décrets de ratification 1962→2026
  (`docs/notes/dette-registre-jort.csv`). Donne prêteur, objet, date, réf. JORT ; **montant** dans
  le corps (repéré sur échantillon OCR), **taux/maturité absents du JORT**. Non dédoublonné par
  accord (avenants, rectificatifs). Colonne `montant` à extraire des corps (chantier OCR borné).
- **Rapport annuel BCT sur la dette extérieure** (`bct.gov.tn/.../dette2024.pdf`) : taux moyen,
  maturité moyenne, service, structure par devise. À rapatrier + OCR des tableaux.

### Dette intérieure (titres d'État en dinars)
- **Stock vivant à la ligne de titre (BTA/BTCT)** : ISIN, coupon, échéance, encours — Tunisie
  Clearing (courbe des taux, bulletins) et BVMT. **Encours par ligne non tabulé** : à collecter.
- **Adjudications BTA/BTCT** (montant retenu, taux moyen pondéré, maturité) — MdF (DGGDCF) +
  bulletins SVT. Série temporelle **dispersée**, à consolider.
- **Encours agrégé Bons du Trésor** — BCT (indicateurs quotidiens testés le 6 nov. 2026 :
  BTA 36 689,6 MDT ; BTCT 1 645,6 MDT). **Codes de table `PL130xxx` à préciser** pour la série
  longue.
- **Ventilation par instrument** (BTA, BTCT, emprunts nationaux) — annexe 7 au PLF (`gbo.tn`),
  PDF **arabe** : à relever.
- **Registre JORT des emprunts intérieurs** (`docs/notes/dette-interieure-registre-jort.csv`,
  198 lignes 1950→2026, colonne `categorie`). ATTENTION : les « emprunts obligataires » sont
  **surtout corporatifs** (70) — hors dette d'État ; dette d'État = bons d'équipement 63 +
  emprunts nationaux 6 + bons du Trésor 15 (+ 17 intitulés arabes رقاعي à classer) ; zone grise
  rétrocédés 25 / garantis 2.

### Dynamique dette/PIB (soutenabilité) — FAIT en partie (9 nov. 2026)
- **FAIT** : indicateurs MdF rapatriés (`tunisia-data` : `extract_minfinances_indicateurs.py`,
  catalogue `finances-publiques-indicateurs`, fiche), snapshotés au cache ; figures
  `#fig-dette-dynamique` (trajectoire dette/PIB + **décomposition** déficit / effet croissance /
  résidu-change, 1986-2025, sur PIB implicite MdF) ; section `#sec-dette-dynamique` et sous-section
  méthode `#sec-dette-soutenabilite`. Source `minfin-indicateurs-fp` (déjà au précis).
- **FAIT en partie** : charge d'intérêt et solde budgétaire **2021-2024** extraits du PDF d'exécution
  MdF (`extract_minfinances_execution.py`, série `finances-publiques-execution`, clé
  `minfin-resultats-provisoires-2024-12` versée FR+AR) ; figure `#fig-dette-cout` (coût apparent
  r vs croissance g ; solde global = primaire − intérêts). Constat récent : r monte mais reste < g.
- **Reste à sourcer** pour aller plus loin (sources validées dans `dette-soutenabilite-sources.md`) :
  - **série LONGUE de la charge d'intérêt BUDGÉTAIRE** (domestique + extérieure, avant 2021) :
    **SONDÉ le 9 nov. 2026, INTROUVABLE dans l'archive BCT locale**. Le BSF récent (pub 108, n° 235)
    n'a plus de section finances publiques ; le Rapport annuel (pub 109) et le BSF ne portent que
    le **service/intérêts de la dette EXTÉRIEURE** (déjà en main via l'IDS). La charge d'intérêt
    budgétaire est une grandeur MdF : sa série longue demande une **compilation des Résultats
    d'exécution du budget** (plusieurs millésimes) ou une « Statistiques des finances publiques »
    du MdF à localiser. → extension du r−g budgétaire avant 2021 **non faite**, gap documenté.
  - **FAIT en contrepartie** : **coût apparent de la dette EXTÉRIEURE 1971-2025** (intérêts/encours,
    IDS) tracé (`#fig-dette-cout-exterieur`) — montre le coût du stock extérieur (~7 % vers 1980
    → ~2,5 % en 2015-2020), **inférieur** au coût apparent total récent (dette intérieure en dinars
    plus chère ; l'extérieure porte le change).
  - **FAIT (10 nov. 2026) — série LONGUE de la charge d'intérêt et r−g budgétaire long** :
    WDI GFS (`finances-publiques-gfs`, 1972-2012, déclaré par la Tunisie au FMI) **+** extraction
    NATIONALE de 3 bulletins d'exécution MdF (Déc 2017/2020/2024 → `finances-publiques-execution`,
    2012-2024) ; série combinée `finances-publiques-charge-interet` (1972-2024, raccord par segments,
    recoupement 2012 : 1267,6 MdF vs 1272,1 GFS). Figure `#fig-dette-cout` : **r−g sur ~1987-2024**
    (g = PIB enchaîné base-cohérente) + décomposition du solde (primaire/intérêts, 2012-2024).
    Clés `minfin-resultats-provisoires-2020-12` versée. Constat : g > r presque toujours ; r−g
    défavorable en 2002, 2011, 2020 (croissance nominale faible).
  - Reste (profondeur et finesse) : **2005-2007** sans bulletin national (BM seulement, non versé) ;
    bulletins 2019/2021/2022/2023 non rapatriés (valeurs plus récentes d'années déjà couvertes) ;
    clés `minfin-resultats-provisoires-{2019-12,2021-12,2022-12,2023-12}` à créer si exploitées.
    Liste complète des éditions : `docs/notes/dette-execution-bulletins.{md,csv}`.
  - **FAIT (10 nov. 2026) — composition par devise et effet de change** : extraites du rapport
    BCT dette extérieure 2024 (pub 107, tableaux A14 et A15) → séries `dette-exterieure-devises`
    (parts EUR/USD/YEN/KWD/autres, 2020-2024) et `dette-exterieure-effet-change` (variation =
    effet-change + effet-volume, 2020-2024, identité vérifiée). Figures `#fig-dette-devises` et
    `#fig-dette-effet-change`. Clé `bct-dette-exterieure-2024` versée. Fenêtre 2020-2024 ;
    série plus longue = rapports BCT antérieurs (format différent). **Durée de vie moyenne** : pas
    d'indicateur isolé dans le rapport (matrices 2D snapshot A16-A19 seulement) — non tracée ;
  - **dette extérieure par devise, série longue** (avant 2020) : rapports BCT pub 107 1991-2019
    (format différent, à parser au cas par cas) ;
  - **durée de vie moyenne / taux moyen** : à chercher dans un état BCT dédié (table PL235010) ;
  - **FAIT (10 nov. 2026) — liquidité externe** : série `liquidite-externe` (réserves en mois
    d'importation `FI.RES.TOTL.MO` et service de la dette PPG en % des exportations
    `DT.TDS.DPPG.XP.ZS`, 1976-2024 ; données BCT/balance des paiements republiées par la BM,
    recoupées au RA de la BCT). Figure `#fig-dette-liquidite` (2 vues). Creux de réserves ~1 mois
    en 1985, pic ~7 mois en 2020, retour ~4,5.
  - Variante **100 % BCT** des réserves/exportations (table en ligne `PL237010` ou BSF) : possible
    en recoupement, non nécessaire (la série BM est déjà d'origine BCT et plus longue) ;
  - **réserves / exportations** (BCT `PL237010`) pour les ratios de liquidité ;
  - **besoin brut de financement** (déficit + amortissements/PIB) — amortissements à assembler ;
  - **composition par devise et durée de vie moyenne** (rapport BCT dette extérieure, pub 107,
    PDF 1991-2024 à OCR) ;
  - **réserves (jours d'import) et exportations** (BCT `PL237010`) pour les ratios de liquidité ;
  - clés CSL économiques de `eco-soutenabilite-dette.md` (bibliographe) pour citer la méthode.
- **Projectif (DSA : chocs, fan charts, BBF futur)** : à **citer** depuis la DSA du FMI (Article IV),
  jamais refaire avec des paramètres inventés.

### Profondeur historique des figures (demande du propriétaire)
- **FAIT (10 nov. 2026)** : figure longue **valeur du dinar** (prix + change, 1960-2025,
  `change-dinar` + `ipc-longue-periode`) illustrant l'effet différencié inflation/change ;
  **composition par devise étendue 2020-2024 → 2003-2024** (parsing multi-rapports BCT pub 107,
  deux dispositions) ; **effet-change étendu → 2019-2024**.
- **Trou 2013-2018** de la composition par devise : **irréductible proprement** (constat du
  10 nov. 2026). Le résolveur d'archives BCT (`download_bct_archives.py --resolve`) confirme que
  la publication 107 « Dette Extérieure » ne contient que **1991-2012 et 2023-2024** (24 numéros) ;
  Wayback n'a pas non plus `dette2013..2018.pdf`. Le Rapport annuel (pub 109) donne un **récit
  partiel** (euro/dollar/yen, sans le détail KWD/autres) et d'un **périmètre vraisemblablement
  différent** (RA 2015 : euro 40,9 %, dollar 31,2 % ; incompatible avec euro ~58-60 % des rapports
  dette) — non raccordable sans risque. Le trou reste donc **affiché tel quel** dans la figure.
  Piste restante : numéros 2013-2018 éventuellement obtenables directement auprès de la BCT.
  La composition couvre 2003-2012 + 2019-2024.
  Deux périmètres (total vs MLT public et garanti) à ne pas mélanger.
- **Effet-change 2003-2018** : les rapports anciens décomposent la variation par devise (pas
  d'agrégat change/volume) ; la série reste 2019-2024.
- **FAIT (10 nov. 2026) — dette publique intérieur/extérieur LONGUE (2001-2025)** : extraite du
  tableau « Encours de la dette publique » (périmètre budgétaire MdF) des **rapports annuels BCT**
  chaînés (`extract_bct_ra_dette_publique.py`, série `dette-publique-interieur-exterieur`) ; total
  concordant avec la dette MdF (écart médian 0,4 MDT). La figure `#fig-dette-interieure` passe de
  2020-2025 à **2001-2025** (niveaux + parts) : intérieur ~38 % (années 2000) → creux 26 % (2018,
  eurobonds) → > 50 % (2024). La série monétaire `dette-etat-interieur-exterieur` (2020-2025) reste
  au catalogue comme concept distinct, non utilisée par la figure.
  Reste : avant 2001, la forme tabulée n'est pas confirmée (RA 1986-2000 à dépouiller) ;
  recoupement possible avec l'annexe 7 au PLF (arabe). Voir `docs/notes/dette-interieure-exterieure-longue.md`.
- **Source brute RA/BCT (pub 109)** : les PDF des rapports annuels sont déjà dans `tunisia-data`
  (`data/raw/bct-archives/109`, ignoré) ; l'extraction est rejouable.
- **Effet-change avant 2019** : les rapports anciens décomposent la variation **par devise**, non
  en agrégat change/volume — extension < 2019 demande un autre traitement.
- **Figures encore courtes** : dette intérieure/extérieure de l'État (2020-2025, table BCT en ligne ;
  série longue = annexe 7 au PLF, arabe, ou BSF) ; garanties (2016-2023, rapports minfin-dette).

## Limites structurelles (à écrire telles quelles dans l'annexe, pas à combler)
- **Prêt individuel nominatif** (un emprunt extérieur = son taux + sa maturité + son échéancier
  propres) : **non public** (reste interne au DRS/BM et à SIADE/MdF). Maille fine publique =
  créancier × année.
- **Détenteurs de la dette intérieure par ligne** et ventilation fine banques / non-banques /
  non-résidents : **non publics**.

## Notions à ajouter au glossaire (terminologue)
`dette-publique`, `dette-de-l-etat`, `dette-interieure`, `dette-exterieure`, `service-de-la-dette`,
`encours`, `ressources-de-tresorerie` (déjà : `garantie-etat`, `emprunt`, `capacite-emprunt`,
`prets-retrocedes`, `regle-d-or`). BTA/BTCT à définir si cités.

## Références à verser (bibliographe)
- `code-comptabilite-publique-62` (art. 62 CCP, base légale des prêts du Trésor) — texte à localiser
  au JORT, non encore lu.
- `bct-dette-exterieure-<année>` (rapport annuel BCT) — URL à vérifier.
- Clé(s) World Bank International Debt Statistics (jeu de données + millésime).

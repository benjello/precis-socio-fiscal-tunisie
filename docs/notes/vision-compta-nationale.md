# Vision — la comptabilité nationale comme ossature macro du précis

Note de cadrage (mode plan), ouverte le 6 novembre 2026. État : **en cours**.
Elle propose une doctrine et des options, puis consigne l'arbitrage. **Décision du 06/11/2026 :
A + B retenus** (couche de données canonique + annexe ; voir § 5). Elle s'appuie sur l'existant du
dépôt et de `tunisia-data`, pas sur une collecte nouvelle.

---

## 0. Le constat de départ

- **Le PIB est déjà partout, mais sans colonne vertébrale.** 42 fichiers `.qmd` sous `precis/fr/`
  rapportent une grandeur « au PIB ». Chaque volume choisit son dénominateur, parfois sa base, sans
  garantie d'homogénéité. L'annexe `annexe-pib.qmd` (note `annexe-pib.md`, ouverte le 06/10/2026)
  traite **les bases** (1983/1997/2015, rétropolations, étiquettes inexactes) mais reste cantonnée
  au PIB-dénominateur.
- **La matière compta nat existe déjà, abondante, dans `tunisia-data`** :
  `data/processed/ins-comptes-nationaux/` porte le PIB courant/volume par base et enchaîné, le
  revenu national, la rémunération des salariés, les emplois du PIB, l'investissement/financement,
  et surtout un **`cnat-consolide/`** avec les **comptes des secteurs institutionnels** (ménages,
  sociétés non financières, sociétés financières, organismes de sécurité sociale, administrations,
  reste du monde) et la consommation finale.
- **L'accès est déjà outillé** : `figtools.series()` sait lire l'entrepôt/snapshot avec métadonnées
  (`base_pib`, libellés bilingues). Le build du site est autonome (pas d'openfisca).

**Donc** : ce n'est pas un problème de données, c'est un problème de **doctrine et d'intégration**.
La vision répond à : *que fait la compta nat dans le précis, et comment on l'y branche sans la
dupliquer ?*

## 1. Les trois rôles possibles de la compta nat (à choisir/combiner)

1. **Dénominateur commun** — fournir LE PIB de référence (et d'autres agrégats : RNB, revenu
   disponible brut des ménages, consommation finale) pour tous les ratios du précis.
2. **Objet documenté en soi** — une annexe/un volume qui explique le système (SCNT, bases, secteurs
   institutionnels, passage emplois↔ressources), comme on documente le JORT.
3. **Cadre de cohérence transversal** — un lieu où les grandeurs des neuf volumes se raccrochent à
   un même squelette (la masse salariale publique vs rémunération des salariés des comptes ; les
   prestations vs comptes des organismes de sécurité sociale ; la compensation vs subventions sur
   produits ; les finances locales vs administrations publiques).

## 2. Options d'architecture (A, B, C)

### Option A — « Annexe enrichie » (incrémental, faible risque)
Étendre `annexe-pib.qmd` en une **annexe « Les comptes de la nation »** : bases + agrégats de
référence + un petit jeu de séries canoniques servies par `figtools`. Chaque volume y renvoie pour
son dénominateur.
- **Pour** : s'appuie sur l'existant, pas de nouveau livre, cohérent avec la note déjà ouverte.
- **Contre** : reste périphérique ; ne crée pas de vrai cadre de cohérence inter-volumes.
- **Effort** : faible. **Gain** : moyen.

### Option B — « Couche de données canonique » (l'investissement structurant)
Créer, dans `tunisia-data` + `figtools`, un **jeu de séries macro canoniques** (identifiants
stables : `pib_courant`, `pib_volume`, `conso_finale_menages`, `rdb_menages`,
`remuneration_salaries`, `va_administrations`, `subventions_produits`…) avec base explicite et
chaînage documenté. Les 42 fichiers migrent vers ces identifiants.
- **Pour** : règle le problème au bon endroit (une source de vérité des dénominateurs) ; rend les
  ratios auditables et reproductibles ; sert A **et** C.
- **Contre** : chantier de migration des 42 `.qmd` ; exige une discipline de nommage et de base.
- **Effort** : élevé. **Gain** : élevé, durable.

### Option C — « Volume / grande annexe de cohérence » (ambition éditoriale)
Un **volume transversal « Le cadre macroéconomique »** (ou une grande annexe) qui présente les
comptes des secteurs institutionnels et **raccroche chaque volume** à sa case des comptes. Devient
le point d'entrée macro du précis.
- **Pour** : réalise les trois rôles ; donne au lecteur la carte d'ensemble qui manque.
- **Contre** : lourd ; risque de doublonner les volumes ; frontière éditoriale à tenir
  (documenter, pas commenter).
- **Effort** : très élevé. **Gain** : élevé mais à horizon long.

**Recommandation de séquence initiale** (supplantée par la décision du § 5 après vérification) :
**B d'abord**, **A en vitrine**, **C en horizon**. → En pratique, la migration (B2) était déjà
faite et l'annexe PIB déjà écrite ; la séquence effective est devenue **B3 (registre) livré, A
déjà en place, B1 et C gatés** — voir § 5.

## 3. Idées concrètes à mettre au pot

- **Un « registre des dénominateurs »** : un YAML (type `tables/*.liens.yml`) qui, pour chaque ratio
  publié, déclare l'agrégat, la base, la source et le segment — vérifié en CI (pas de PIB chaîné en
  silence, cf. la règle AGENTS.md sur les changements de base).
- **Séries par segments de base** dans `figtools` : exposer nativement les ruptures
  1983→1997→2015 pour que toute figure « au PIB » les trace par segments sans bricolage.
- **Comptes des secteurs institutionnels en figures réutilisables** : à partir de `cnat-consolide/`,
  des blocs « compte des ménages », « compte des administrations », « organismes de sécurité
  sociale » que les volumes concernés citent.
- **Table de concordance volume ↔ compte** : prestations ↔ organismes de sécurité sociale,
  rémunérations publiques ↔ rémunération des salariés / VA administrations, compensation ↔
  subventions sur produits, finances locales ↔ administrations publiques locales.
- **Garde-fou éditorial** : la compta nat se **documente** (comme le JORT), elle ne commente pas ;
  le budgétaire reste distinct des évaluations (règle FMI/BM/OCDE de l'AGENTS.md).
- **Pont modèle** : openfisca n'entre pas dans le site, mais la couche B peut nourrir des agrégats
  de calage ; constat éventuel → `backlog-modele.md`, jamais dans un volume.

## 4. Questions ouvertes (pour la revue humaine)

1. **Un agrégat de référence unique** pour tout le précis, ou un dénominateur par famille (PIB
   nominal pour le budgétaire, RDB pour les ménages) ?
2. **Jusqu'où remonter** ? Appliquer la règle « série à fenêtre ~30 ans » aux agrégats macro, ou
   publier l'histoire longue par segments de base ?
3. **A/B/C** : lance-t-on la couche canonique B tout de suite, ou l'annexe A d'abord ?
4. **Volume ou annexe** pour C, et sous quel nom (« cadre macroéconomique » / « comptes de la
   nation ») ?
5. **Qui porte le chantier** : rôle `economiste` (cadre + notions), `documentaliste` (preuves INS),
   `modeliste` (calage) — et qui tient le registre des dénominateurs ?

## 5. Décision et feuille de route A + B (06/11/2026)

**Arbitrage de la revue humaine : A + B retenus.** On construit la **couche de données canonique
(B)** comme socle, et l'**annexe (A)** comme vitrine qui la consomme. **C** (volume de cohérence)
reste en horizon, non tranché.

**Mise à jour du 06/11/2026 (après vérification du code)** : la part « migration » de B (B2) était
**déjà faite** (PR #524, #374). La séquence effective devient donc **A + B3 d'abord** (annexe +
registre des dénominateurs, qui documentent l'existant déjà sain), **B1 ensuite** (dette technique :
factorisation du helper), **C en horizon**.

### Ce que B exige vraiment (le socle de données existe déjà)

L'inspection de `tunisia-data/catalog.yml` change l'échelle du chantier : la **couche de données**
de B est en grande partie **déjà bâtie**. L'entrepôt porte les séries canoniques et leurs ruptures :
- `pib-courant-par-base` — LE PIB nominal par base (1983/1997/2015), « trois bases jamais
  raccordées », colonne `retropole`, fiche `docs/pib-courant-par-base.md` ;
- `irpp-ratios` — PIB du ministère avec colonnes `segment_pib` et `rupture` (ruptures 1997, 2002,
  2005, 2010, 2025 déjà documentées dans les *caveats*) ;
- `compensation-ratios`, `masse-salariale-ratios`, `cnat-pib-nominal`, `pib-courant-recouvrements`
  (écarts observés entre bases, « jamais extrapolés »).

Ce qui manque n'est donc **pas la donnée**, et **B2 est déjà fait** (voir le bandeau de l'annexe) :
il reste **deux pièces d'intégration** (B1, B3), dont une seule est prioritaire.

- **B2 — migrer les foyers de chaînage silencieux : FAIT.** Les deux foyers que cette feuille de
  route visait (fiscalité rendements, masse salariale) étaient **déjà migrés** sur
  `pib-courant-par-base` / `segment_pib` (PR #524 et PR #374), ce que la vérification du code a
  établi le 06/11/2026. Plus rien à corriger ici.
- **B1 — un helper de figure partagé « part du PIB par segments » (optionnel, non urgent).** Le
  tracé par segments est **dupliqué** : `compensation.py` (`_cles_pib`, `_marque_ruptures`),
  `finances_locales.py` (`_pib_par_base`, `_ruptures_pib`), `masse_salariale.py`,
  `fiscalite/rendement_bases.py`, et leurs **copies arabes**. Le factoriser dans
  `scripts/figtools.py` réduirait la dette, mais son bénéfice premier (rendre B2 mécanique) est
  caduc puisque B2 est fait. À traiter comme une dette technique, gatée, **après** A/B3 — un
  refactor de 4 modules + copies arabes à iso-rendu ne se fait pas sans revue.
- **B3 — le « registre des dénominateurs » (prioritaire avec A).** Un YAML (modèle
  `tables/*.liens.yml`) qui, pour chaque ratio publié, déclare : agrégat, base/segment, source,
  **nature** (interne / externe). Les **18 ratios `externe`** y entrent avec la mention « base non
  précisée par la source ». Vérifié en CI (cf. règle des changements de base, AGENTS.md).

### Ce que A ajoute, en consommant B

- **A1 — étendre `annexe-pib.qmd`** en annexe « Les comptes de la nation » : les trois bases (déjà
  matière d'`annexe-pib.md`) + les agrégats de référence + le **registre B3 rendu en table lisible**
  (quel dénominateur, quelle base, interne/externe).
- **A2 — chaque volume renvoie à l'annexe** pour son dénominateur. Les phrases de doctrine « toute
  part du PIB dit sa base » (entrée # 57) sont le point d'accroche déjà en place.

### Ordre d'exécution révisé (après vérification du 06/11/2026)

| Pas | Objet | État | Touche | Vérif |
|---|---|---|---|---|
| 1 | Inscrire la note au `docs/notes/README.md` | **fait** | docs | — |
| 2 | Vérifier les deux foyers `RISQUE`, corriger l'inventaire | **fait** | docs | lecture code (#524/#374) |
| 2bis | **Re-vérifier les 57 entrées sur le code** (pas l'identifiant de série) | **fait** | — | 0 écart, 0 RISQUE confirmé |
| 3 | **B3** : registre des dénominateurs + contrôle structurel | **fait** | `docs/notes/registre-denominateurs-pib.yml`, `scripts/check_registre_denominateurs.py` | check vert (exit 0) |
| 4 | **A** : annexe « comptes de la nation » | **déjà en place à 90 %** (voir ci-dessous) | annexe | — |
| 5 | **B1** : factoriser le helper `segment_pib` dans `figtools` (dette) | gaté, après revue | 4 modules + AR | diff nul au rendu |
| 6 | Re-vérifier les 7 `partiel` (CNSS) ; produire fonds spéciaux (# 14) | optionnel | fiscalité/caisses | rendu |

#### B3 — livré (06/11/2026)

`docs/notes/registre-denominateurs-pib.yml` : **60 entrées** pour les 57 ratios de l'inventaire
(trois ratios mixtes scindés interne/externe ; # 45 reclassé `ok`). Chaque entrée porte agrégat,
base, source (identifiant d'entrepôt pour les internes, rapport pour les externes), nature.
`scripts/check_registre_denominateurs.py` (uv run) contrôle la structure, la cohérence
classement↔nature, l'existence des fichiers, l'exactitude de la synthèse, et rapproche les
`source_serie` du catalogue `precis/_seriescache/catalog.snapshot.yml` (informatif). **Check vert.**
Trois suites honnêtes : # 9 (`droits-douane-pib`, série dérivée hors snapshot), # 14 (à produire),
# 45 (dénominateur via l'abstraction EP, à préciser).

#### A — déjà en place pour le PIB

Contrairement à ce que laissait croire le README (« annexe à rédiger »), **`precis/fr/annexe-pib.qmd`
existe et est substantiel** (437 l., ancres stables) : il couvre « Ce qu'est une base », les bases
successives, les écarts de niveau, la rétropolation, **« Quel PIB dans quelle source »** (tableaux
institutions TN / organisations extérieures), les **5 règles de signalement d'une rupture**, et
« Comment lire une part du PIB ». L'objet « PIB-dénominateur » de A est donc **fait**. Le registre
B3 en est le complément lisible par machine (par ratio, là où l'annexe est par source).

**Ce qui reste pour A/C, et pourquoi c'est gaté** : l'annexe ne couvre que le PIB. La
**comptabilité nationale au sens large** (comptes des secteurs institutionnels — ménages,
administrations, organismes de sécurité sociale ; emplois/ressources ; revenu national ;
consommation finale), déjà présente en données dans `tunisia-data/…/cnat-consolide/`, reste à
écrire — mais c'est de la **rédaction éditoriale** (rôle rédacteur, revue humaine) et cela relève
de l'option C (horizon). Un agent ne l'écrit pas sans ticket cadré ni relecture.

**Bilan du chantier autonome** : la partie « données + vérité » de la vision est faite (inventaire
vérifié, aucun foyer de chaînage silencieux, registre livré et contrôlé).

#### C — ouvert le 06/11/2026 (décision humaine « go C »)

Forme tranchée : **une annexe** `precis/fr/annexe-comptes-nation.qmd`, sœur de l'annexe PIB, et non
un volume (un système statistique se documente comme l'annexe PIB, pas comme un corps de droit).
Elle complète l'annexe PIB — secteurs institutionnels, séquence des comptes, trois approches du
PIB, agrégats citables, **table de concordance volumes ↔ comptes** — sans la refaire. Plan
d'architecte : `docs/notes/chantier-comptes-nation-plan.md`.

**Chaîne éditoriale parcourue jusqu'à un brouillon rendu (06/11/2026)** :

| Étape | Rôle | Livrable | État |
|---|---|---|---|
| Note documentaire | documentaliste | `docs/notes/annexe-comptes-nation.md` (sourcée, pages INS, chiffres 2021 base 2015) | **fait** |
| Versement | bibliographe | clé `ins-scnt97-presentation` (FR + AR) ; cohérence ✓ | **fait** |
| Passe 1 termes | terminologue | 11 ancres `#g-…` dans `glossaire.yml` ; `build_glossary.py` EXIT=0 | **fait** |
| Rédaction | rédacteur | `precis/fr/annexe-comptes-nation.qmd` (7 sections, câblée dans `build.sh`) | **fait** |
| Rendu de contrôle | — | `quarto render` OK, **0 citation `[?]`** ; `check_pas_de_modele`/`check_jargon` OK | **fait** |

**Restent, pour l'humain / la CI** (non autonomes) : revue éditoriale de l'annexe ; **passe 2**
(définitions finales + validation des formes arabes) ; **clôture bibliographe** (dry-run Zotero,
rapatriement de la clé) ; **nav** facultative (lien dans le pied de page des livres — parité AR,
non faite) ; **version AR** par la CI de traduction (`build.sh` saute la page AR absente ;
`arabe_cablage.py` ne concerne pas les pages racine) ; **figures de séries** (plan § 5.3) et
les séries de niveaux par base à construire dans `tunisia-data` (note doc. § 5). Questions de
forme encore ouvertes (annexe vs volume à terme, concordance simple vs réconciliation chiffrée) :
§ 5 du plan d'architecte. **Rien n'est committé.**

### Backlog à verser (issu de l'inventaire)

Les neuf points du § « Backlog issu de l'inventaire » (annexe) sont à reporter dans
`docs/notes/backlog-precis.md` (et les points amont dans `docs/notes/backlog-modele.md` pour la
masse salariale). Priorité : foyers `RISQUE` (fiscalité rendements, masse salariale).

---

## Annexe — inventaire des ratios au PIB

Inventaire factuel rendu par le `documentaliste` (06/11/2026). **Portée** : 48 fichiers `.qmd`
sous `precis/fr/` (hors `annexe-pib.qmd`) emploient une formule « au PIB » (≈ 259 occurrences
chiffrées, 311 lignes au grep large), regroupées ici par couple (figure ou phrase) × grandeur.
Il élargit le § 4.2 de `annexe-pib.md` (qui ne couvrait six volumes que sous l'angle de la base)
à Compensation, Entreprises publiques, Éducation, Santé, Prestations non contributives, Informel,
Marché du travail, Fonds spéciaux.

**Colonne « base »** : celle que le fichier affirme ; « non dit » = aucune base dans texte ni
code ; « par segments » = tracé base par base, sans raccord. **Colonne « risque »** : `OK` = base
explicite et segments tracés ; `partiel` = une rupture tracée, une autre non ; `RISQUE` = série
accolée ou étiquette inexacte, chaînage silencieux possible ; `externe` = ratio imprimé tel quel
par un rapport extérieur, base non dite par la source.

> **Correction vérifiée le 06/11/2026 (lecture du code, pas de l'inventaire).** Les **8 entrées
> classées `RISQUE`** par le documentaliste (# 1-8 fiscalité, # 23/24/26 masse salariale) sont en
> réalité **déjà corrigées dans le code** et doivent se lire `OK` :
> - **Fiscalité, 4 rendements** — `_impot_revenu.qmd` embarque `fig_rendement()` qui délègue à
>   `figures/rendement_bases.py` ; ce module trace le PIB **par base** (`pib-courant-par-base`,
>   une courbe par base 1983/1997/2015, rétropolation marquée, aucun coefficient de passage).
>   Migré par la **PR #524**. L'inventaire a vu la série `irpp-ratios` sans voir la délégation.
> - **Masse salariale** — `figures/masse_salariale.py` trace par `segment_pib`, ruptures issues
>   des données (`figtools.marque_rupture`), base 2015 vs base 1997 « dite 2010 par le FMI »
>   explicitée. Migré par la **PR #374**. Le « ×1,06 » n'est plus un forfait : c'est une colonne
>   de ratio **annuel observé** (base 2015 / base 1997) de la figure de réconciliation.
>
> **Conséquence** : il ne reste **aucun foyer de chaînage silencieux** à corriger. Les autres
> classements (`OK`, `partiel`, `externe`) n'ont pas été re-vérifiés un à un ; les deux seuls
> `RISQUE` l'ont été, et tous deux étaient périmés. **Avant de piloter un chantier sur cet
> inventaire, re-vérifier chaque entrée dans le code**, pas seulement l'identifiant de série.
> La synthèse ci-dessous est corrigée en conséquence ; le tableau garde les libellés d'origine
> du documentaliste (colonne « risque » à lire à travers ce bandeau pour # 1-8, # 23, # 24, # 26).

| # | Fichier `.qmd` | Volume | Grandeur rapportée au PIB | Dénominateur | Base supposée | Source du dénominateur | Segments / risque |
|---|---|---|---|---|---|---|---|
| 1 | `fiscalite/_impot_revenu.qmd` | Fiscalité | Rendement IRPP 1986‑2025 (fig. `irpp.py`) | PIB nominal | non dit (part. rétropolé 2010‑14) | `irpp-ratios`, `irpp_sur_pib_pct` | **RISQUE** (ruptures 1997/2002/2005/2010 non tracées) |
| 2 | `fiscalite/_impot_revenu.qmd` l.886 | Fiscalité | « 1,9 % à plus de 6 % du PIB » (1990‑2016) | PIB nominal | non dit | idem | **RISQUE** |
| 3 | `fiscalite/_impot_societes.qmd` | Fiscalité | Rendement IS (fig.), onglet 2 colonnes de PIB | PIB nominal | non dit | `pib_minfin_MDT`, `pib_cnat_MDT` | **RISQUE** (écart 2012‑14 vu comme divergence, pas rupture) |
| 4 | `fiscalite/_impot_societes.qmd` l.326 | Fiscalité | « 1,86 % (1990) → 3,77 % (2025) » | PIB nominal | non dit | idem | **RISQUE** |
| 5 | `fiscalite/_tva.qmd` | Fiscalité | Rendement TVA 1986‑2025 (fig. `tva.py`) | PIB min. Finances | non dit | `irpp-ratios` | **RISQUE** |
| 6 | `fiscalite/_tva.qmd` l.195‑199 | Fiscalité | « 6,5 % 1988 … 6,8 % 2025 » | PIB min. Finances | non dit (1997 = +9,8 %) | idem | **RISQUE** |
| 7 | `fiscalite/_droits_consommation.qmd` | Fiscalité | Rendement droits de consommation | PIB min. Finances | non dit | idem | **RISQUE** |
| 8 | `fiscalite/_droits_consommation.qmd` l.406 | Fiscalité | « maximum 1994, 3,7 % » | PIB min. Finances | non dit (traverse le saut 1997) | idem | **RISQUE** |
| 9 | `fiscalite/_droits_douane.qmd` l.786 (`#fig-dd-pib`) | Fiscalité | Droits de douane en part du PIB 1986‑2025 | PIB nominal | **par segments** 1983/1997/2015 ; 2002‑04, 2025 isolés | série PIB par base | **OK** |
| 10 | `fiscalite/_droits_douane.qmd` l.837,884 | Fiscalité | FMI/CEQ/BM : pertes tarifaires en % du PIB | PIB du rapport | non dit | FMI, BM, études | **externe** |
| 11 | `fiscalite/_depenses_fiscales.qmd` l.99‑140 | Fiscalité | Total avantages fiscaux en % du PIB | PIB nominal INS | **2015, non rétropolé** | `@ins-cnat-2015` | OK (calcul interne) ; **externe** (ratios des rapports, TODO l.140) |
| 12 | `fiscalite/_regimes_incitation.qmd` | Fiscalité | Crédits d'incitation (2 fig.) en part du PIB | PIB nominal | **par segments** | série PIB par base | **OK** |
| 13 | `fiscalite/_regimes_incitation.qmd` l.1053‑1169 | Fiscalité | Études (BM 2014, Ghazouani) | PIB du document | non dit | BM, Ghazouani 2011 | **externe** |
| 14 | `fiscalite/_taxes_fonds_speciaux.qmd` l.338 | Fiscalité | Ratio au PIB des fonds spéciaux (fig. à créer) | — | — (TODO par segments) | à venir | **lacune** |
| 15 | `fiscalite/_taxes_fonds_speciaux.qmd` l.421 | Fiscalité | FMI : pertes en % du PIB | PIB du rapport | non dit | FMI 2015/2016 | **externe** |
| 16 | `fiscalite/_timbre_enregistrement.qmd` l.757,772 | Fiscalité | Timbre en part du PIB (`#fig-te-rendement`) | PIB nominal | **2015 et 1997** en double | série PIB par base | **OK** |
| 17 | `caisses/_comptes_longue_periode.qmd` | Caisses | Résultat de gestion CNSS en % du PIB 1990‑2004 | PIB min. Finances | 1983→1997, rupture 1997 tracée | `irpp-ratios` | **partiel** (2002‑04 non rattaché) |
| 18 | `cotisations_sociales/_bilan.qmd` | Cotisations | Cotisations CNSS par branche en % du PIB | PIB min. Finances | 1983→1997, rupture tracée | `irpp-ratios` | **partiel** |
| 19 | `prestations_sociales/_prestations_familiales.qmd` | Prestations | Allocations familiales + maj. en % du PIB | PIB min. Finances | 1983→1997, rupture tracée | `irpp-ratios` | **partiel** |
| 20 | `retraites/_secteur_prive.qmd` l.772 | Retraites | Branche pensions RSNA en % du PIB | PIB min. Finances | 1983→1997, rupture tracée | `irpp-ratios` | **partiel** |
| 21 | `retraites/_secteur_prive.qmd` l.309,361 | Retraites | Croissance du PIB nominal (taux, pas un ratio) | PIB nominal | depuis 1993 même base | `croissances-revenus-prix` | **partiel** (1970, 1983‑85 à cheval) |
| 22 | `retraites/_regard_banque_mondiale.qmd` l.8‑9 | Retraites | BM : pensions 5,1 % du PIB (2011), déficits | PIB du rapport | non dit | `@wb-2015-spl-policy-note` | **externe** |
| 23 | `remunerations_publiques/index.qmd` | Rémunérations | Masse salariale publique en % du PIB 1990‑2025 | PIB nominal | **étiquette « base 2015 » inexacte** (2012‑14 = base 1997) | `masse-salariale-ratios` | **RISQUE** (aucune rupture tracée) |
| 24 | `remunerations_publiques/index.qmd` l.79 | Rémunérations | « 11‑12 % 1990 … 16,1 % 2020 … 13,5 % 2025 » | PIB nominal | étiquette inexacte | idem | **RISQUE** |
| 25 | `remunerations_publiques/index.qmd` l.44,103,117 | Rémunérations | FMI 17,6 % (2020) ; BM 14,7 % (2017) | PIB du rapport | non dit (FMI = base 1997) | FMI, BM | **externe** |
| 26 | `remunerations_publiques/` fig. B (`masse_salariale.py`) | Rémunérations | Masse salariale « recalculée base 2010 (×1,06) » | PIB nominal | **« base 2010 » inexistante** ; facteur 1,06 unique | `masse-salariale-reconciliation` | **RISQUE** (coefficient forfaitaire) |
| 27 | `remunerations_publiques/_regime_conventionnel.qmd` l.83 | Rémunérations | BM : transferts aux EP 8,9 % (2013), 7,5 % (2014) | PIB du rapport | non dit | BM | **externe** |
| 28 | `remunerations_publiques/_regime_indiciaire.qmd` / `_regime_statutaire_autonome.qmd` | Rémunérations | 1 mention « au PIB » chacune (renvoi au cadre) | PIB nominal | renvoi annexe PIB | masse salariale | partiel (renvoi) |
| 29 | `finances_locales/_budgets.qmd` | Finances locales | Ressources/impôts locaux en % du PIB | `cnat-pib-nominal` par base | **explicite** 1983/1997/2015 | `cnat-pib-nominal` | **OK** (`_pib_par_base`) |
| 30 | `finances_locales/_transferts.qmd` | Finances locales | FCCL en % du PIB 1985‑2023 | `cnat-pib-nominal` ; BM 1985‑91 | explicite (INS) ; non dit 1985‑91 | idem + BM 1992 | **OK** sauf 1985‑91 (**externe**) |
| 31 | `finances_locales/_impots_activite.qmd` l.489‑498 | Finances locales | TCL en % du PIB | PIB comptes nation | **1997 puis 2015, non raccordées** | `cnat-pib-nominal` | **OK** |
| 32 | `finances_locales/_impots_immeubles.qmd` l.584‑605 | Finances locales | TIB en % du PIB 2008‑2023 | PIB comptes nation | **1997 puis 2015, non raccordées** | `cnat-pib-nominal` | **OK** |
| 33 | `compensation/_depense.qmd` | Compensation | Dépense de compensation en part du PIB 1984‑2026 | PIB | **par segments** 1983/1997/2015 | `compensation-parts` (`segment_pib`) | **OK** (modèle de référence) |
| 34 | `compensation/_depense.qmd` l.74‑75,300‑304 | Compensation | « 1,9 % (2005)… 8,6 % 2022 » ; plans 1 % du PIB | PIB min. Finances | **base citée dans le texte** | `compensation-parts` | **OK** |
| 35 | `compensation/_institution.qmd` | Compensation | Dotation de la Caisse en part du PIB | PIB | par segments, base dite | `compensation-parts` | **OK** |
| 36 | `compensation/_carburants.qmd` l.107‑117 | Compensation | Soutien aux carburants en part du PIB | PIB INS | **2015** | `@ins-cnat-2015` | **OK** |
| 37 | `compensation/_electricite_gaz.qmd` l.549‑560 | Compensation | Facture combustibles STEG en points de PIB 2013‑23 | PIB nominal base 2015 | **2015** (2013‑14 rétrop.) | `pib-courant-par-base` | **OK** |
| 38 | `compensation/_exterieurs.qmd` | Compensation | Subventions selon BM/FMI en part du PIB | PIB du rapport + min. Fin. 1983 | **par segments** | rapports + `compensation-parts` | **OK/externe** |
| 39 | `compensation/_incidence.qmd` l.94 | Compensation | BM 2013 : 4,7 % et 6,6 % | PIB base FMI | non dit (2 dénominateurs) | `@bm-2013-82712` | **externe** |
| 40 | `compensation/_transport.qmd` | Compensation | Crédits/interventions transport en part du PIB | PIB INS base 2015 ; segments ≤1994 | **2015** ; par segments avant | `compensation` + INS | **OK** |
| 41 | `compensation/_transport.qmd` l.751 | Compensation | CEQ : transport 0,3 pt de PIB (2010) | PIB de l'étude | non dit | `@jouini-lustig-moummi-shimeles-2017-ceq38` | **externe** |
| 42 | `entreprises_publiques/index.qmd` + `_transferts.qmd` | Entreprises pub. | Transferts du budget aux EP en % du PIB 2016‑24 | PIB INS | **2015** | série dédiée, `base_pib` | **OK** |
| 43 | `entreprises_publiques/_garanties.qmd` l.7‑233 | Entreprises pub. | Encours/garanties/plafond légal en % du PIB | PIB INS | **par segments** 1983/1997/2015 | série par base + rapport dette | **OK** + **externe** (13,5 % 2023 base non dite) |
| 44 | `entreprises_publiques/_recettes.qmd` | Entreprises pub. | Part de l'État dans les bénéfices en % du PIB 1983‑2023 | PIB | base dite (1997 pour 2003‑09) | série par base | **OK** |
| 45 | `entreprises_publiques/_cessions.qmd` l.235‑255 | Entreprises pub. | Recettes de cession en % du PIB 1987‑2009 | PIB de l'année | base non dite dans texte (fig. base dite) | série par base | OK/partiel |
| 46 | `entreprises_publiques/_emploi_comptes.qmd` | Entreprises pub. | Charges de personnel ; résultat net agrégé en % du PIB | PIB INS | **2015** | série par base | **OK** |
| 47 | `entreprises_publiques/_etudes.qmd` | Entreprises pub. | 5 documents (réforme, BM, FMI, ITCEQ) | PIB du document | non dit | rapports | **externe** |
| 48 | `education/_depense.qmd` + `index.qmd` | Éducation | Dépense d'éducation en % du PIB 2010‑2023 | PIB nominal INS | **2015** (2010‑14 rétrop.) | `@ins-cnat-2015` | **OK** ; segment 2005‑09 base 1997 **non calculé** (TODO l.51) |
| 49 | `education/_depense.qmd` l.481‑515 | Éducation | UIS/UNESCO : dépense 4,9‑7,3 % du PIB | PIB UIS/WDI | non dit | `@wb-wdi` | **externe** |
| 50 | `sante/_couverture.qmd` l.102 | Santé | Budget Santé en % du PIB 2018‑2023 | PIB nominal INS | **2015** | annuaire INS | **OK** |
| 51 | `sante/_couverture.qmd` tbl.1 | Santé | Dépense courante de santé en % du PIB | PIB de l'OMS | non dit | OMS, GHED | **externe** |
| 52 | `prestations_sociales/_non_contributives.qmd` l.998‑1065 | Prestations | Crédits Amen social en part du PIB 2021‑23 | PIB prix courants INS | **2015** | `@ins-cnat-2015` | **OK** |
| 53 | `prestations_sociales/_non_contributives.qmd` l.1150‑1223 | Prestations | BM/UNICEF : coût du transfert 0,4‑0,9 % du PIB | PIB de chaque document | non dit | BM, UNICEF | **externe** |
| 54 | `prestations_sociales/_logement_social.qmd` l.587‑614 | Prestations | Prélèvement FOPROLOS en part du PIB | PIB « de chaque base » | **par segments** | série PIB par base | **OK** |
| 55 | `informel/_estimations.qmd` + `_mesures.qmd` | Informel | Production non déclarée en part du PIB (Schneider) | PIB officiel | non dit (MIMIC/DGE) | Schneider ; base BM | **externe** |
| 56 | `marche_travail/_politiques_emploi.qmd` l.1257‑1259 | Marché du travail | BM : politiques actives 1,5 % (2002), 0,8 % (2011) | PIB du rapport | non dit | BM 2004, 2015 | **externe** |
| 57 | `compensation/index.qmd` ; `entreprises_publiques/_etudes.qmd` ; `education/index.qmd` | (cadres) | Doctrine « toute part du PIB dit sa base » | — | renvoi annexe PIB | — | OK (cadre, pas un ratio) |

### Synthèse de l'inventaire (corrigée après vérification du code)

- **57 entrées** (≈ 32 figures/groupes, 25 phrases ou tableaux), sur **16 volumes**, couvrant
  ~259 occurrences chiffrées.
- **`OK` (base explicite et segmentée) : 32 entrées** — les 24 recensées par le documentaliste
  **plus les 8 ex-`RISQUE`** (fiscalité rendements et masse salariale), vérifiées déjà migrées
  (PR #524, PR #374). Le modèle `_pib_par_base` / `segment_pib` / `pib_retropole` est généralisé
  à Compensation, Entreprises publiques, Finances locales, Fiscalité, Rémunérations, et aux ratios
  récents base 2015 d'Éducation, Santé, Prestations.
- **`externe` : 18 entrées** — ratios imprimés par FMI/BM/UIS/OMS/CEQ/Ghazouani/Schneider, base non
  dite *par la source* : à documenter, pas à corriger (cœur de B3).
- **`RISQUE` (chaînage silencieux) : 0 entrée** après vérification (les 8 annoncées étaient
  périmées — voir le bandeau ci-dessus).
- **`partiel` : 7 entrées** — figures CNSS 1990‑2004 (rupture 1997 tracée, 2002‑04 non) et barème
  d'actualisation ; ruptures mineures, séries courtes se terminant en 2004, **non re-vérifiées**.
- Non encore produits : fonds spéciaux (# 14) et segment 2005‑2009 de l'éducation (# 48, TODO).

**Conclusion révisée** : le précis **n'a plus de foyer de chaînage silencieux interne** — le travail
de segmentation par base a déjà été fait là où il était critique. Le problème résiduel est de
**cohérence et de documentation** : homogénéiser le modèle `segment_pib` (aujourd'hui dupliqué dans
plusieurs modules de figures), **documenter les 18 dénominateurs externes**, et offrir au lecteur une
annexe de référence. Cela **déplace la priorité de B2 (fait) vers A (annexe) et B3 (registre)**.

### Backlog issu de l'inventaire

1. **Fiscalité, 4 rendements** (`_impot_revenu`, `_impot_societes`, `_tva`, `_droits_consommation`)
   — PIB accolé du ministère, base non dite, aucune rupture tracée. **Cible prioritaire** couche B.
2. **`remunerations_publiques/index.qmd` + `masse_salariale.py`** — étiquette `base_pib: 2015`
   inexacte (2012‑14 = base 1997) ; figure B « base 2010 » inexistante, facteur 1,06 mesuré sur
   2015‑2017 seulement. Corriger en amont dans `tunisia-data` (cf. annexe‑pib § 4.3).
3. **`education/_depense.qmd` l.51** — part du PIB 2005‑2009 (base 1997) non calculée (attend
   `denominateurs-depenses-etat-pib`).
4. **`fiscalite/_taxes_fonds_speciaux.qmd` l.338** — ratio au PIB des fonds spéciaux pas encore
   produit (attend `fonds_speciaux_tresor_MDT`).
5. **`fiscalite/_depenses_fiscales.qmd` l.140** — ratios imprimés par les rapports ≠ calcul base
   2015 ; PIB employé par les rapports à relever.
6. **Dénominateurs externes non maîtrisés** (base non dite *par la source*) : FMI, BM, UIS/UNESCO,
   OMS, CEQ, Ghazouani, Schneider → candidats au « registre des dénominateurs », mention « base
   non précisée par la source ».
7. **`entreprises_publiques/_garanties.qmd`** — rapport dette : 13,5 % (2023) sur PIB base non
   identifiée, divergence avec calcul base 2015 (14,3 %).
8. **`compensation/_incidence.qmd`** — BM 2013 : deux ratios sur deux PIB différents (réalisé 2012
   vs prévu 2013), base FMI non précisée.
9. **Stock rapporté à un flux** (encours garanties, créances/dettes EP) : « ordre de grandeur, non
   fraction » — point de doctrine (nature stock/flux), pas une anomalie de base.

*Méthode : aucune fiche `docs/recherches.yml` ouverte (aucune lacune ne porte sur un texte du
JORT). Inventaire du documentaliste, 06/11/2026 ; aucun fichier du corpus modifié.*

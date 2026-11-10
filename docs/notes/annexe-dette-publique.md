# Matière — Annexe « La dette publique » (chantier annexe-dette)

Note de conception et d'inventaire. Alimente une annexe transversale sur le modèle de
`annexe-budget-etat` et `annexe-pib` : une page de site hors volume
(`precis/fr/annexe-dette-publique.qmd`) qui porte le lieu unique de vérité méthodologique sur la
dette publique, auquel les volumes renvoient par ancre stable. **Aucun chiffre de dette n'est
avancé ici** : on documente la loi, les périmètres et les séries disponibles ; les encours et le
service de la dette restent à sourcer (§ Lacunes).

## 1. Pourquoi une annexe, et pas un volume

Aucun des treize volumes ne « possède » la dette publique. Le service de la dette pèse sur le
budget de l'État (*Fiscalité* pour les ressources, l'annexe budget pour les dépenses) ; les
garanties et les prêts rétrocédés relèvent des *Entreprises publiques* ; les dettes croisées
État / entreprises publiques et banques publiques, du même volume ; la soutenabilité touche tous
les volumes qui rapportent une charge au PIB. La dette est l'agrégat de passif qui relie ces
dispositifs. Comme pour le budget et le PIB, on en fait une **annexe commune** : la méthode et les
définitions vivent là ; les volumes y accrochent une grandeur (plafond de garantie, encours
garanti, service de la dette en % des dépenses) par lien d'ancre.

Conforme à la convention « les volumes documentent la loi, jamais l'agrégat » : le récit de la
dette transversal est hors volume, chaque volume reste sur son dispositif.

## 2. Ce que recouvre « la dette publique » (socle juridique vérifié)

### 2.1 Dette de l'État vs dette publique au sens large
- **Dette de l'État** (dette négociée et contractée par le Trésor) ⊂ **dette publique au sens
  large**, qui ajoute la dette garantie par l'État (entreprises et établissements publics,
  banques publiques) et, selon le périmètre retenu par le ministère des Finances, la dette des
  entreprises publiques. Le document de référence qui porte ces périmètres en Tunisie est le
  **Rapport sur la dette publique** annexé chaque année au projet de loi de finances (annexe n° 7,
  *gbo.tn*), publié **en arabe seulement** (« التقرير حول الدين العمومي ») — clés déjà versées
  `minfin-dette-2022` et `minfin-dette-2025`.
- La **garantie de l'État** est déjà définie au glossaire (`garantie-etat`, source
  `minfin-dette-2025` p. 61 et `loi-org-2019-15-lob` art. 45) : engagement par lequel l'État
  s'oblige à honorer la dette d'un tiers s'il fait défaut ; la loi de finances en fixe le plafond
  annuel. On distingue **garanties accordées dans l'année** (flux) et **encours de dette garantie**
  (stock).

### 2.2 Dette intérieure vs extérieure
- Partition par **résidence du créancier / marché d'émission et devise** : dette **intérieure**
  (marché local, dinar) vs **extérieure** (bailleurs, marchés internationaux, en devises). Le
  piège de change est propre à l'extérieure : un encours en devises se réévalue en dinars avec la
  dépréciation, sans nouvel emprunt. La série `garanties-etat` distingue déjà
  `encours_interieur` / `encours_exterieur` (et `garanties_interieures` / `garanties_exterieures`),
  ce qui donne la maille, mais pour les seules garanties, pas pour la dette de l'État.

### 2.3 Encours (stock) vs service de la dette (flux)
- **Encours** : stock dû à une date (fin d'année). **Service de la dette** : flux annuel =
  **remboursement du principal (amortissement)** + **intérêts (charges d'intérêt)**. La
  distinction est juridiquement portée par la nomenclature budgétaire (ci-dessous) : intérêts et
  principal ne sont pas au même endroit du budget.

### 2.4 Les ressources d'emprunt : ressources de trésorerie, pas recettes du budget
Point de droit central, **déjà établi et cité dans `annexe-budget-etat.qmd`** (§ ressources) —
réutilisable tel quel :
- **Loi organique 2019-15** : les recettes du budget de l'État sont classées en trois parties —
  recettes fiscales, recettes non fiscales, dons [`loi-org-2019-15-lob`, art. 14, p. 396-397].
  L'emprunt **n'y figure pas** : les **ressources d'emprunt sont des ressources de trésorerie**,
  distinctes des recettes du budget [`loi-org-2019-15-lob`, art. 12]. Les dépenses sont classées
  par missions/programmes et, par nature, incluent « opérations financières » et « charges de
  financement » [art. 15]. Structure applicable à partir de la LF 2020.
- **Loi 67-53** (régime antérieur, jusqu'à l'exercice 2019) : les dépenses sont rangées en deux
  **titres**. **Titre I** (budget ordinaire / fonctionnement) = dépenses de gestion **et intérêts
  de la dette** [`loi-67-53-lob`, art. 3]. **Titre II** (développement) = dépenses des plans de
  développement **et remboursement du principal de la dette** [art. 5]. Les ressources suivent la
  partition : recettes ordinaires au titre I ; **recettes exceptionnelles et ressources d'emprunt
  au titre II** [art. 6]. L'emprunt faisait donc partie des **ressources du budget** sous 1967,
  alors qu'il en est **exclu** (trésorerie) sous 2019. Refonte intermédiaire en titres/parties/
  sections par `loi-org-96-103-lob`.
- **Conséquence pour lire une série** : « recettes fiscales, non fiscales, dons, emprunt » recouvre
  **deux régimes** ; la place de l'emprunt bascule de « ressource budgétaire » (1967) à « ressource
  de trésorerie » (2019). Tracer et commenter l'emprunt impose de dire l'époque.

### 2.5 Pourquoi « les dépenses de l'État hors dette » excluent le service de la dette
La série maîtresse de l'annexe budget (`denominateurs-depenses-etat-pib.csv`, colonne
`depenses_etat_hors_dette_MDT`) **exclut le service de la dette** — précisément pour isoler les
dépenses pilotables du poids des emprunts passés et éviter de compter l'amortissement comme une
dépense de politique publique. C'est le miroir exact de l'annexe dette : ce que l'annexe budget
retire (intérêts + principal), l'annexe dette le reprend. À énoncer comme complémentarité, renvoi
croisé `#sec-bud-definitions` ↔ `#sec-dette-service`.

### 2.6 Plafonds votés en loi de finances (prêts du Trésor, garanties)
- **Prêts du Trésor aux établissements publics** : chaque LF fixe le **montant maximal** dans la
  limite duquel le ministre des Finances peut accorder des prêts du Trésor, **en vertu de l'article
  62 du code de la comptabilité publique**. C'est un **plafond légal voté**, NI un montant accordé,
  NI un encours (série `jort-lf-plafond-prets-tresor`, § 3).
- **Garantie de l'État** : chaque LF fixe de même le **plafond de la garantie** (série
  `jort-lf-plafond-garanties`, art. 45 de la LOB 2019 pour le principe).

## 3. Inventaire des séries disponibles (`precis/_seriescache/`)

| Série | Portée exacte | Couverture | Source | Piège |
|---|---|---|---|---|
| `jort-lf-plafond-prets-tresor.csv` | **plafond légal VOTÉ** des prêts du Trésor aux établissements publics (art. 62 CCP), une ligne par fixation + relèvements en cours de gestion | **2016 → 2026** (états antérieurs à 2016 non versés) | lois de finances au JORT (clés `lf-2016`…`lf-2026`), lecture à l'image ; fascicules FR absents du corpus pour 2016/2019/2020/2023/2024/2025 → pages de l'extrait FR ; LF 2026 lue **en arabe seulement** | **maximum autorisé, PAS un montant accordé ni un encours** ; voté ≠ réalisé ; valeurs faibles (100-330 MDT) ; relèvements LFC à ne pas confondre avec la fixation initiale |
| `jort-lf-plafond-garanties.csv` | **plafond légal VOTÉ** de la garantie de l'État (octroi de la garantie du Trésor puis de l'État) | **1958-59 → 2026** | lois de finances au JORT (clés `loi58-45-lf1958`…`lf-2026`) ; 1958-59 imprimé en **francs** (colonne `valeur_imprimee`) | plafond voté, pas l'encours garanti ; rupture d'unité franc→dinar ; LF 2025 ne dit plus « maximum » ; LF 2026 arabe seule ; **ne pas raccorder** à `garanties-etat` (sources et définitions différentes) |
| `garanties-etat.csv` | garanties de l'État : **plafond, garanties accordées (flux), encours de dette garantie (stock, intérieur/extérieur/total)** + volet audit banques publiques | **2016 → juin 2024** | Rapport sur la dette publique (annexe 7, `minfin-dette-2022`/`minfin-dette-2025`) et rapport transferts/garanties (annexe 8, `minfin-transferts-garanties`), lecture à l'image | mélange **flux** (`-S1`, semestre) et **stock** (`-06`, fin juin estimé) : NE PAS TRACER ensemble ; `encours_pct_pib` : base PIB non dite ; divergences entre éditions arabes |
| `entreprises-publiques-dettes-creances-croisees.csv` | dettes des entreprises publiques **envers l'État** et créances **sur l'État**, fin d'année | **2021, 2022, 2023** | Rapport sur les entreprises publiques (annexe 9, `minfin-ep-2025`), échantillon 42 entreprises **hors banques** | échantillon partiel (hors banques, Ciments Oum El Kélil, OTD, CNAM) ; dettes croisées ≠ dette publique ; 3 points seulement |
| `denominateurs-depenses-etat-pib.csv` | dépenses de l'État **hors dette**, RÉALISÉES, + PIB | 1984-2025 (dépenses dès 1986) | ministère des Finances ; PIB WDI/INS | **hors service de la dette par construction** — pivot de complémentarité avec l'annexe dette ; PIB à bases multiples (cf. `annexe-pib`) |
| `bct-ipc-base2015.csv`, `ipc-longue-periode.csv` | IPC (déflateur) | 2015→2025 ; longue→2023 | BCT, INS | pour passer en dinars constants un encours/service nominal ; lacune IPC 2023→2025 (cf. note budget) |

**Fait structurant** : toutes les séries « dette » en cache sont **votées (plafonds)** ou
**partielles (garanties 2016→2024, dettes croisées 2021-2023)**. Il n'existe **aucune série longue
d'encours de la dette publique ni de service de la dette** dans `_seriescache/`. L'annexe ne peut
donc pas, en l'état, tracer la courbe maîtresse « encours de la dette publique / PIB » : c'est la
première lacune à sourcer (§ 7), pas un chiffre à inventer.

## 4. Les pièges méthodologiques (cœur de l'annexe)

1. **Plafond voté ≠ montant accordé ≠ encours.** Les deux séries JORT (prêts, garanties) sont des
   **autorisations maximales**. Ne jamais les lire comme un endettement réalisé.
2. **Stock ≠ flux.** Encours (date) vs service de la dette (année = principal + intérêts). Ne
   jamais additionner ni tracer ensemble (cf. piège `garanties-etat` `-S1`/`-06`).
3. **Intérêts (titre I / fonctionnement) ≠ principal (titre II / développement)** sous la loi de
   1967. Le service de la dette est **éclaté** dans la nomenclature de l'époque ; le reconstituer
   demande d'additionner deux titres. Sous 2019, voir « charges de financement » / « opérations
   financières » (art. 15).
4. **Emprunt : recette budgétaire (1967) → ressource de trésorerie (2019).** Dire l'époque avant
   d'interpréter.
5. **Intérieur / extérieur et change.** Un encours extérieur en devises se réévalue en dinars sans
   emprunt nouveau ; dire la devise et distinguer effet volume / effet change.
6. **Dénominateur PIB.** Toute part au PIB hérite des ruptures de base : renvoi systématique à
   `annexe-pib` (`#sec-pib-bases`, `#sec-pib-ruptures`).
7. **Dette publique ≠ dette de l'État ≠ dettes croisées des entreprises publiques.** Trois
   périmètres distincts ; toute figure dit lequel.
8. **Source arabe seule.** Rapport dette (annexe 7) et EP (annexe 9) publiés en arabe : montants lus
   à l'image, divergences entre éditions possibles ; signaler la lecture.

## 5. Ancres stables proposées (les volumes y renvoient — ne pas renommer, ne pas traduire)

```
#sec-dette-pourquoi       — pourquoi cette annexe
#sec-dette-perimetres     — dette de l'État / publique / garantie ; intérieur / extérieur
#sec-dette-stock-flux     — encours vs service (principal + intérêts)
#sec-dette-tresorerie     — ressources d'emprunt : trésorerie (2019) vs titre II (1967)
#sec-dette-service        — le service de la dette dans le budget (complément annexe budget)
#sec-dette-plafonds       — plafonds votés en LF : prêts du Trésor, garanties
#fig-dette-plafond-prets  — plafond des prêts du Trésor voté en LF (2016-2026)
#fig-dette-plafond-garanties — plafond de la garantie de l'État voté en LF (1959-2026)
#fig-dette-garanties-encours — encours de dette garantie (intérieur/extérieur), 2016-2024
#sec-dette-ep-croisees    — dettes croisées État / entreprises publiques
#sec-dette-sources        — sources et périmètres
#sec-dette-lire           — comment lire une grandeur de dette
```

## 6. Points d'accroche « dette » par volume

| Volume | Grandeur rapportée | Série / source | Ancre annexe |
|---|---|---|---|
| Entreprises publiques | plafond et encours des garanties de l'État | `jort-lf-plafond-garanties`, `garanties-etat` | `#sec-dette-plafonds`, `#fig-dette-garanties-encours` |
| Entreprises publiques | prêts du Trésor, dettes croisées | `jort-lf-plafond-prets-tresor`, `entreprises-publiques-dettes-creances-croisees` | `#fig-dette-plafond-prets`, `#sec-dette-ep-croisees` |
| Fiscalité / Budget | service de la dette vs dépenses hors dette | `denominateurs-depenses-etat-pib` + minfin (à sourcer) | `#sec-dette-service` |
| Tous | encours / PIB (soutenabilité) | **à sourcer** (BCT / minfin) | `#sec-dette-stock-flux` |

## 7. Références candidates (pour le bibliographe)

**Déjà versées, à réutiliser** :
- `loi-org-2019-15-lob` (precis/fr/references.json) — LOB 2019, art. 12 (ressources de trésorerie),
  14 (recettes), 15 (nomenclature), 45 (garanties). URL pist.tn vérifiée.
- `loi-67-53-lob`, `loi-org-96-103-lob` (precis/fr/fiscalite/references.json) — régime des titres
  I/II, emprunt au titre II. URL pist.tn.
- `minfin-dette-2022`, `minfin-dette-2025` — Rapport sur la dette publique (annexe 7 LF), arabe.
- `minfin-transferts-garanties` — Rapport transferts et garanties (annexe 8).
- `minfin-ep-2025` — Rapport sur les entreprises publiques (annexe 9).
- Clés de LF `lf-2016`…`lf-2026`, `loi58-45-lf1958`… (déjà sources des séries plafonds).

**Nouvelles à créer (à confirmer par le bibliographe)** :
- **Code de la comptabilité publique, art. 62** (base légale des prêts du Trésor). Clé proposée
  `code-comptabilite-publique-62` — à sourcer : loi n° 73-81 du 31 décembre 1973 portant promulgation
  du code de la comptabilité publique, JORT (localisateur à établir ; non encore lu).
- **Rapport annuel BCT** (encours et service de la dette, change) — clé `bct-rapport-annuel-<année>`
  à créer une fois l'édition retenue et l'URL vérifiée. **Non encore sourcé.**
- **Rapport annuel sur la dette publique / situation de la dette** du ministère des Finances
  (série longue encours + service) — à localiser sur finances.gov.tn / gbo.tn. **Non encore sourcé.**

## 8. Notions à glossaire (pour le terminologue)

**Déjà présentes** (réutiliser, vérifier suffisance) : `garantie-etat`, `prets-retrocedes`,
`emprunt`, `capacite-emprunt`, `regle-d-or`.

**À ajouter / préciser** (source canonique pressentie) :
- **dette publique** — périmètre large (État + garantie + EP) ; source `minfin-dette-2025`.
- **dette de l'État** — dette contractée par le Trésor ; `minfin-dette-2025`, `loi-org-2019-15-lob`.
- **dette intérieure** / **dette extérieure** — marché/devise ; `minfin-dette-2025`.
- **service de la dette** — principal + intérêts (flux annuel) ; `minfin-dette-2025`,
  `loi-67-53-lob` (titre I intérêts / titre II principal).
- **encours (de la dette)** — stock à une date ; `minfin-dette-2025`.
- **ressources de trésorerie** — `loi-org-2019-15-lob`, art. 12.
- **prêts du Trésor** — art. 62 code de la comptabilité publique ; série `jort-lf-plafond-prets-tresor`.
- (AR, pressenti depuis les intitulés : الدين العمومي ; دين الدولة ; خدمة الدين ; ضمان الدولة —
  à confirmer par le terminologue sur le rapport dette arabe.)

## 9. Lacunes à verser au backlog durable

1. **Série longue d'encours de la dette publique** (État / publique au sens large, intérieur /
   extérieur, en % du PIB) : **absente du cache**. À sourcer (rapport dette annexe 7, rapport
   annuel BCT, ou situation de la dette minfin). Sans elle, pas de figure maîtresse `#fig-dette-encours`.
2. **Série du service de la dette** (principal + intérêts, annuel, longue période) : absente. À
   sourcer minfin/BCT. Nécessaire pour `#sec-dette-service` et le miroir « hors dette ».
3. **Dette extérieure en devises** et **effet change** : aucune série ; à sourcer BCT (rapport
   annuel, balance des paiements).
4. **Plafond des prêts du Trésor avant 2016** : l'article existe dans les LF antérieures mais n'est
   pas versé ; extension `jort-lf-plafond-prets-tresor` vers l'arrière = chantier documentaliste JORT.
5. **Code de la comptabilité publique, art. 62** : cité de mémoire via le périmètre de la série ;
   **texte non encore lu ni localisé au JORT**. À ouvrir et verser comme référence.
6. **Rapport sur la dette publique (annexe 7)** : disponible en **arabe seulement** ; aucune
   traduction française officielle. Les montants `garanties-etat` sont lus à l'image ; une relecture
   systématique des encours de dette de l'État (hors garanties) reste à faire.
7. **IPC 2023→2025** pour déflater un service de la dette nominal : même lacune que l'annexe budget
   (raccord `ipc-longue-periode` / `bct-ipc-base2015`).
8. **Dettes croisées EP / État** limitées à 2021-2023, échantillon hors banques : pas de série
   longue.

## 10. Recherches infructueuses

Aucune fiche `docs/recherches.yml` ouverte dans cette passe : les lacunes ci-dessus sont des
**séries de données à sourcer** (rapports BCT/minfin), non des textes juridiques manquants au JORT.
Deux candidates à ouvrir par le documentaliste au moment du sourçage effectif :
- recherche du **code de la comptabilité publique (art. 62)** au JORT (loi 73-81) — à lancer ;
- recherche d'une **série officielle longue encours/service de la dette** (finances.gov.tn, gbo.tn,
  rapports annuels BCT) — à documenter en fiche si elle n'aboutit pas.

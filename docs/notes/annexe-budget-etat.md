# Matière — Annexe « Le budget de l'État » (chantier evolution-budgets)

Note de conception et d'inventaire. Alimente une annexe transversale sur le modèle de
`annexe-pib` : une page de site (`precis/fr/annexe-budget-etat.qmd`, hors volume) qui porte la
série longue du budget de l'État et le lieu unique de vérité méthodologique auquel les volumes
renvoient par ancre stable.

## 1. Pourquoi une annexe, et pas un volume

Aucun des treize volumes ne « possède » le budget de l'État : les recettes fiscales relèvent de la
*Fiscalité*, les transferts aux entreprises publiques des *Entreprises publiques*, la masse
salariale des *Rémunérations publiques*, la compensation de son volume, les subventions aux caisses
des *Retraites*/*Caisses*, les transferts FCCL des *Finances locales*. Le budget est l'agrégat qui
les relie. Comme pour le PIB, on en fait une **annexe commune** : la méthode et la série maîtresse
vivent là ; les volumes y accrochent une « part du budget » par lien d'ancre.

Conforme à la convention « les volumes documentent la loi, jamais l'agrégat » : le récit budgétaire
transversal est hors volume, et chaque volume reste sur son dispositif.

## 2. Inventaire des séries disponibles (`precis/_seriescache/`)

| Série | Portée exacte | Couverture | Piège |
|---|---|---|---|
| `jort-lf-budget-ordinaire.csv` | **budget ordinaire VOTÉ** (titre I de la LF), sourcé loi par loi au JORT | **1959–1986** | n'est **pas** un total de l'État ; titre I seul (hors investissement, titre II) ; **voté**, pas réalisé ; s'arrête en 1986 |
| `denominateurs-depenses-etat-pib.csv` | **dépenses de l'État hors dette, RÉALISÉES** + PIB | **1984–2025** | réalisé ≠ voté ; hors service de la dette ; PIB à bases multiples (cf. annexe-pib) |
| `recettes-fiscales-composition.csv` | composition des **recettes fiscales** réalisées (IRPP, IS, douanes, TVA, consommation, autres indirects) | **1986–2025** | recettes fiscales seulement (hors non-fiscales, dons, emprunt) ; source minfin |
| `depenses-fiscales-detail.csv` | dépenses fiscales (GBO) | 2017–2023 | « manque à gagner », pas une dépense budgétaire ; tous postes non chiffrés |
| `entreprises-publiques-transferts-budget.csv` | transferts budgétaires aux EP | — | périmètre EP ; cf. volume EP |
| `finances-locales-fccl-lois-de-finances.csv` | dotation FCCL **votée** en LF | — | voté ; part collectivités |
| `compensation-recettes-caisse.csv`, `compensation-carburants-recettes.csv` | compensation | — | caisse de compensation, périmètre propre |
| `education-depense-*`, `ins-budget-sante-2018-2023.csv` | dépenses sectorielles | — | nomenclatures sectorielles, ruptures de champ |

**Le fait structurant** : la série *votée* (1959–1986) et la série *réalisée* (1984–2025) ne se
chaînent pas — définitions différentes (voté/réalisé, titre I/dépenses hors dette). Il y a un
chevauchement 1984–1986 qui sert à montrer l'écart, **pas** à raccorder. Comme pour le PIB, on trace
**par segments** et le pivot du milieu des années 1980 est une **rupture documentée**, pas un
raccord silencieux.

### Lacune à verser au backlog
- La série *votée* titre I s'arrête en 1986. Deux options, à trancher en revue :
  (a) l'étendre vers l'avant par lecture JORT des LF 1987→ (travail documentaliste, lourd) ;
  (b) assumer le pivot voté→réalisé au milieu des années 1980 et ne pas prolonger le voté.
  Recommandation : (b) d'abord — la série réalisée 1984–2025 porte le récit moderne ; le voté
  1959–1986 éclaire la période de construction. (a) reste un chantier ouvert.
- Pas de série longue des **recettes totales** ni du **déficit/dette** en cache : à sourcer si le
  récit « entrées/sorties » doit être bouclé (minfin, BCT).

## 3. Les pièges méthodologiques (cœur de l'annexe)

1. **Voté ≠ réalisé.** La LF vote un budget ; l'exécution en diffère. On ne compare que du
   comparable ; chaque figure dit lequel elle porte.
2. **Titre I ≠ total.** Le budget ordinaire (titre I) exclut l'investissement (titre II). Un
   « total de l'État » agrège les deux + opérations de trésorerie ; la série votée ne le donne pas.
3. **Dénominateur PIB.** Toute part au PIB hérite des ruptures de base : renvoi systématique à
   `annexe-pib` (`#sec-pib-bases`, `#sec-pib-ruptures`). Tracer par segments de base.
4. **Dinars courants vs constants.** Série longue déflatée par l'IPC (`bct-ipc-base2015` via
   `figtools.constants_escalier`) pour l'évolution réelle ; toujours dire l'année de prix.
5. **Rupture de champ 1986.** La bascule voté→réalisé coïncide avec le début des séries minfin ;
   c'est le moment où le récit change de source et de définition.

## 4. Ancres stables proposées (les volumes y renvoient — ne pas renommer, ne pas traduire)

```
#sec-bud-pourquoi        — pourquoi cette annexe
#sec-bud-definitions     — voté/réalisé, titre I/II, total de l'État, recettes/dépenses
#sec-bud-serie-longue    — la série maîtresse (segments)
#fig-bud-courant         — budget en dinars courants, par segments
#fig-bud-constant        — budget en dinars constants (IPC)
#fig-bud-pib             — dépenses de l'État en % du PIB
#sec-bud-recettes        — composition des recettes fiscales
#fig-bud-recettes        — figure composition recettes
#sec-bud-pivot-1986      — la rupture voté→réalisé du milieu des années 1980
#sec-bud-sources         — sources et périmètres
#sec-bud-lire            — comment lire une part du budget
```

## 5. Points d'accroche « part du budget » par volume

Chaque accroche est une phrase + un lien d'ancre, dans la section longue période du dispositif.

| Volume | Grandeur rapportée au budget | Série | Ancre annexe |
|---|---|---|---|
| Fiscalité | rendement IRPP/IS/TVA, part dans les recettes | `recettes-fiscales-composition` | `#sec-bud-recettes` |
| Fiscalité | dépenses fiscales (manque à gagner) vs recettes | `depenses-fiscales-detail` | `#sec-bud-recettes` |
| Entreprises publiques | transferts budgétaires aux EP en % des dépenses | `entreprises-publiques-transferts-budget` | `#fig-bud-pib` |
| Compensation | charge de compensation en % des dépenses/PIB | `compensation-*` | `#fig-bud-pib` |
| Rémunérations publiques | masse salariale en % des dépenses/PIB | denominateurs + minfin masse salariale | `#fig-bud-pib` |
| Finances locales | dotation FCCL en % du budget de l'État | `finances-locales-fccl-lois-de-finances` | `#sec-bud-serie-longue` |
| Retraites / Caisses | subventions d'équilibre aux caisses | (à sourcer) | `#fig-bud-pib` |
| Éducation / Santé | dépense sectorielle en % du budget | `education-depense-*`, `ins-budget-sante` | `#fig-bud-pib` |

## 5bis. Prototype validé (chiffres de contrôle)

Fusion voté + réalisé + IPC long (déflation vers 2015) exécutée — la série tient :

| année | voté titre I (MDT courants) | voté (const. 2015) | dép. réalisées hors dette | % PIB | base PIB |
|---|---|---|---|---|---|
| 1962 | 56,8 | 837 | — | — | — |
| 1970 | 146,5 | 1 640 | — | — | — |
| 1986 | 1 970 | 7 207 | 2 395 | 33,4 | base 1983 présumée |
| 2000 | — | — | 6 638 | 22,6 | base 1997 |
| 2010 | — | — | 14 267 | 21,6 | base 2015 |
| 2020 | — | — | 37 703 | 31,5 | base 2015 |
| 2025 | — | — | 52 495 | 30,4 | non rattachée |

Constats :
- **Le raccord se fait en 1986 seulement** (le réalisé des `denominateurs` ne commence qu'en 1986 ;
  1984–1985 n'y portent que le PIB). En 1986, voté titre I = 1 970 MDT contre réalisé hors dette =
  2 395 MDT : l'écart matérialise « titre I voté < dépenses totales réalisées ». À montrer comme
  **rupture**, jamais comme continuité.
- **Le % PIB n'est pas monotone** (33 % en 1986 → ~22 % en 2000–2010 → ~31 % en 2020–2025) **mais**
  il traverse trois bases PIB (1983 présumée → 1997 → 2015) : toute lecture longue de ce ratio doit
  segmenter par base et renvoyer à `annexe-pib`. Ne pas conclure sur la tendance sans segmenter.
- **Lacune IPC** : `ipc-longue-periode` s'arrête en **2023**, `bct-ipc-base2015` va à 2025. Pour une
  série constante jusqu'à 2025 il faut raccorder les deux IPC (figtools sait déflater par escalier) ;
  sinon la série constante s'arrête à 2023. À verser au backlog.

## 6. Ordre de travail

1. Figure `#fig-bud-courant` / `#fig-bud-constant` à partir de `jort-lf-budget-ordinaire`
   (1959–1986) + `denominateurs` (1984–2025), tracées **par segments**, déflatées via IPC.
2. Figure `#fig-bud-pib` (dépenses hors dette / PIB, par base).
3. Figure `#fig-bud-recettes` (composition, part empilée).
4. Ossature `.qmd` de l'annexe, ancres posées, renvois `annexe-pib`.
5. Accroches dans les volumes (une PR par volume, après validation de l'annexe).

# Concordance des dettes — carte des périmètres de l'annexe « dette publique »

Note **faisant foi** : de quelle dette parle chaque série et chaque figure de l'annexe. À lire
avant d'ajouter une figure, de reprendre un chiffre, ou de comparer deux séries. Le mot « dette
extérieure » recouvre **quatre périmètres** de valeurs différentes — c'est la première source
d'erreur. Valeurs repères à fin 2024 (sauf mention).

`scripts/check_dette_coherence.py` vérifie les invariants de cette note à chaque rendu.

## Famille 1 — Dette publique de l'État (ce que l'État doit)

| Périmètre | Total | Intérieur | Extérieur | Série(s) `id` | Source | Figures |
|---|---:|---:|---:|---|---|---|
| **1a. Budgétaire (MdF)** — *référence du précis* | **135 642** | 73 103 | 62 539 | `finances-publiques-indicateurs` (total, % PIB), `dette-publique-interieur-exterieur` (int/ext, 2000-2025) | ministère des Finances (indicateurs ; RA BCT) | dette/PIB, décomposition, intérieur/extérieur |
| **1b. Monétaire (BCT)** — *financement de l'économie* | 124 635 | 62 098 | 62 537 | `dette-etat-interieur-exterieur` (2020-2025, **non employée par les figures**) | BCT, statistiques monétaires | — |

- **« La dette publique » sans autre précision = 1a (budgétaire).** Son total (135 642, **84,9 % du
  PIB**) concorde entre `finances-publiques-indicateurs` et `dette-publique-interieur-exterieur`
  (écart médian 0,4 MDT) : c'est l'invariant maître.
- 1a et 1b **diffèrent surtout par l'intérieur** (73 103 vs 62 098) : périmètre et valorisation
  distincts. Ne jamais additionner ni comparer terme à terme.

## Famille 2 — Dette extérieure (en devises) — **quatre périmètres, ne pas confondre**

| Périmètre | Niveau 2024 | Série(s) | Unité | Figures |
|---|---:|---|---|---|
| **2a. Ext. publique et garantie (PPG)** | 20 843 M$ (≈ 66 600 MDT) | `dette-exterieure-echeancier`, `-creanciers` | **dollars** | échéancier, créanciers, coût apparent extérieur |
| **2b. Ext. MLT TOTALE (tous secteurs)** | **≈ 80 000 MDT** | `dette-exterieure-devises` (parts), `dette-exterieure-effet-change` (variation) | dinars | composition par devise, effet‑change/volume |
| **2c. Ext. de l'État (budgétaire)** | 62 539 MDT | `dette-publique-interieur-exterieur` (col. extérieur) | dinars | intérieur/extérieur, canaux inflation |
| **2d. Ext. de l'État (monétaire)** | 62 537 MDT | `dette-etat-interieur-exterieur` (col. extérieur) | dinars | — |

- **Règle d'or** : l'**effet‑change et la composition par devise (2b)** portent sur l'encours
  extérieur MLT **de tous les secteurs** (État + banques + entreprises, ≈ 80 000 MDT), **pas** sur
  la dette extérieure de l'État (2c, 62 539). *C'est l'erreur commise lors de la reproduction de
  l'effet‑change : base 62 539 au lieu de ≈ 80 000.* Niveau de 2b = tableau A10 du rapport BCT
  dette extérieure ; **aucune série de niveau n'est encore au cache** (seulement parts et
  variation) — à verser si besoin.
- 2c ≈ 2d ≈ 62 500 (l'État doit la même chose, lu par deux producteurs) ; 2a (PPG, en dollars)
  ajoute la part garantie ; 2b ajoute les autres secteurs.
- **Toujours dire l'unité** : 2a est en **dollars** ; 2b/2c/2d en **dinars**.

## Famille 3 — Charge et service

| Grandeur | Série | Valeur 2024 | Périmètre |
|---|---|---:|---|
| Charge d'intérêt de l'État | `finances-publiques-charge-interet` | 6 284 MDT | administration centrale (GFS avant 2012, MdF ensuite) |
| Solde budgétaire / primaire | `finances-publiques-execution`, `-indicateurs` | — | administration centrale |
| Service ext. PPG (principal+intérêts) | `dette-exterieure-echeancier` | — | PPG, dollars |

## Famille 4 — Garanties et passifs conditionnels (dette **au sens large**)

| Grandeur | Série | Périmètre |
|---|---|---|
| Encours de dette garantie | `garanties-etat` | garantie de l'État (EP, banques) — **pas** une dette directe |
| Plafonds votés (prêts Trésor, garanties) | `jort-lf-plafond-prets-tresor`, `jort-lf-plafond-garanties` | autorisation maximale votée, ni accordé ni encours |
| Dettes croisées État / EP | `entreprises-publiques-dettes-creances-croisees` | périmètre EP, échantillon |

## Famille 5 — Macro de contexte (jamais « la dette »)

`change-dinar` (cours officiel dinar/USD), `ipc-longue-periode` + `bct-ipc-base2015` (prix),
`liquidite-externe` (réserves en mois d'import, service/exportations), `pib-*` (PIB).

## Invariants vérifiés (par `check_dette_coherence.py`)

1. `dette-publique-interieur-exterieur` : intérieur + extérieur = total (chaque année).
2. `dette-etat-interieur-exterieur` : intérieur + extérieur = total.
3. Total budgétaire 1a ≈ `finances-publiques-indicateurs.dette_MDT` (écart < 1 %).
4. `dette-exterieure-effet-change` : variation = effet‑change + effet‑volume.
5. Ordre des périmètres extérieurs : 2c (État budg.) ≤ 2a (PPG, converti) ≤ 2b (MLT total).
6. Parts par devise `dette-exterieure-devises` : somme ≈ 100 %.
7. Toute figure de l'annexe cite une série **existante** au cache, de `perimetre` renseigné.

## Reproduire l'effet‑change : ce qui est possible, ce qui ne l'est pas

L'effet‑change (`dette-exterieure-effet-change`, **reporté par la BCT**, 1999‑2024) se recalcule en
principe : `effet‑change = Σ (encours MLT total × part_devise) × (variation du cours dinar/devise)`.
La **méthode est validée** (reproduction quasi exacte certaines années), mais la reproduction
**exacte au dinar** bute sur trois points, tous vérifiés :
1. **Base d'encours** : c'est l'encours extérieur **MLT total** (tableau A10 du rapport BCT dette,
   versé en série `dette-exterieure-encours-mlt-total`, **2019-2024** : 77 001 → 75 966 MDT, pic
   82 712 en 2022), **pas** la dette extérieure budgétaire (62 539). *Erreur commise puis corrigée ;
   le garde-fou vérifie désormais État budg. ≤ MLT total.* Segment ancien (2013-2018) non versé
   (rapports 107 absents).
2. **Cours = officiels BCT, pas de marché.** Le dinar est administré ; les cours **officiels fin
   d'année** (tableau **A23** du rapport dette) diffèrent des cours de marché (Yahoo) de 1‑2 % par
   devise, ce qui **se cumule** (effet‑change 2024 : −208 avec A23 vs −880 avec cours de marché,
   pour −304 reporté). Les cours A23 ne sont extractibles que des **rapports récents** (2022‑2024) ;
   avant, ils sont en **graphiques**.
3. **« Autres devises » (~9 %)** ≈ **dette FMI en DTS** (`DT.DOD.DIMF.CD`, publié ; ordres de
   grandeur concordants) + reliquat (GBP, mineures) **non public** (interne **SIADE** de la BCT ;
   la Banque mondiale ne renseigne pas `DT.CUR.*` pour la Tunisie).

**Décision** : on **garde la série reportée par la BCT** comme valeur autoritative ; la recomputer à
partir de cours de marché publics introduirait **plus** d'erreur. Le calcul reste une **validation**.

## Séries BCT en ligne (fetch à la main) — ce qu'on peut, ce qu'on ne peut pas

Tables statistiques scrapables (HTTP 200, HTML statique) mais **fenêtre ~2020‑2025 seulement** :
endettement (`PL060010,PL060020`), réserves (`PL237010`), bons du Trésor (`PL203120`), taux
(`PL203105` TMM, `PL203260` directeur), cours de change (`PL203130` du jour, `PL212010` moyennes
annuelles, `PL213010` mensuel). **La profondeur historique et les cours officiels fin d'année ne
sont PAS en ligne** — ils vivent dans les **PDF** (rapport annuel pub 109, rapport dette pub 107,
bulletin BSF pub 108). Tables `tableau_n_ne.jsp` (dette extérieure détaillée, durée de vie moyenne
`PL235010`) chargées en **AJAX** → non scrapables, à prendre dans le PDF.

## Règles d'écriture (pour ne pas se tromper)

- Une figure, un périmètre : **la légende nomme le périmètre** (p. ex. « dette extérieure publique
  et garantie, en dollars » ; « encours extérieur total, tous secteurs »).
- Ne jamais écrire « la dette extérieure » seule : préciser **lequel des quatre**.
- Ne jamais mélanger dollars (2a) et dinars (2b/2c) sur un même axe.
- Avant un calcul qui croise deux séries, vérifier qu'elles sont **du même périmètre** (cf. erreur
  effet‑change).

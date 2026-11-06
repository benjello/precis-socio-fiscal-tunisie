# EP — volet financier (ROE/ROA, ratios bancaires, dettes croisées)

**6 novembre 2026.** Calculé **sans extraction nouvelle**, à partir des `fiches-entreprises` du précis
(`precis/_seriescache/entreprises-publiques-fiches-entreprises.csv`, 8436 l., bilan + résultat par EP,
rapports MdF LF2024/2025, sourcé page). Recoupe exactement nos données (PNB BNA 2018 : précis 553 vs
tunisia-data 553,8). Voir `ep-sources-consolidation.md`.

## ⚠️ Avertissement méthodo : le ROE est trompeur pour les EP à fonds propres impaires
Plusieurs EP ont des **capitaux propres négatifs ou quasi nuls** → le ROE (résultat/fonds propres)
**change de signe et explose** (STEG ROE +289 % en 2021 ; STIR +110 % en 2022 ; GCT +144 % en 2020)
sans aucun sens économique. **On lit le ROA** (résultat/total actif), robuste à ce biais, et l'on
réserve le ROE aux EP à fonds propres positifs.

## ROA — rentabilité réelle des EP non financières (2020-2023, %)
| EP | 2020 | 2021 | 2022 | 2023 | Lecture |
|---|---|---|---|---|---|
| GCT | **−35** | +7 | +2 | — | effondrement 2020 (phosphate), reprise fragile |
| STIR | +2 | 0 | **−64** | **−20** | choc 2022 (prix carburants / compensation) |
| CPG | **−16** | +3 | +18 | +3 | très volatil (phosphate) |
| SNCFT | −4 | −6 | **−10** | — | dégradation continue |
| Office des céréales | −9 | −13 | −13 | **−16** | déficit structurel croissant (compensation) |
| SONEDE | −5 | −1 | −1 | — | déficitaire mais stabilisé |
| STEG | −1 | +23 | −18 | −7 | en dents de scie (subventions) |
| ETAP | −7 | −3 | +5 | +5 | redressement (pétrole) |
| SNDP | −2 | +2 | +3 | +1 | légèrement positif |
| ONAS | ~0 | ~0 | ~0 | ~0 | à l'équilibre comptable |

## Banques — ratios déjà calculés par le précis (2018-2023), recoupés avec nos PNB
| | coeff. exploitation (%) | solvabilité (%) | créances classées / NPL (%) |
|---|---|---|---|
| **BNA** | 48 → **38,5** (amélioration) | 14,7 → 21,4 | 15,6 → **19,4** (dégradation 2023) |
| **STB** | 46 → 39 → **48,9** (re-dégradation) | 10,4 → 13,6 (mince) | 20,7 → 13,5 → 18,1 |
| **BH** | ~39-42 (stable) | 10,5 → 15,4 | 11,4 → **15,9** |
Le **coefficient d'exploitation** (frais / PNB) est **déjà extrait** par le précis → inutile de
l'ajouter au parseur tunisia-data. Nos séries tunisia-data le **prolongent avant 2018** (masse
salariale / PNB depuis 2000), ce que le précis n'a pas.

## Dettes croisées — l'enjeu de politique publique (exercice 2018, MD)
Déjà extrait (`fiches-entreprises`, indicateurs `dette_*`). Révèle le **web d'arriérés** EP ↔ banques ↔
État ↔ caisses ↔ autres EP :
| EP | envers banques | envers autres EP | envers caisses soc. | dette totale |
|---|---|---|---|---|
| **STEG** | **8 277** | 433 | 9 | **11 397** |
| STIR | 602 | **1 062** | 3 | 2 741 |
| Tunisair | 1 076 | 784 | 31 | 1 949 |
| GCT | 499 | 536 | 24 | 1 496 |
| Office des céréales | 1 037 | — | 1 | 1 294 |
| CPG | 87 | 22 | 12 | 172 |
STEG concentre l'essentiel de la dette bancaire du secteur ; STIR et GCT sont surtout endettés
**envers d'autres EP** (arriérés croisés).

## Répartition du travail (consolidée)
- **Volet financier récent (2018-2023)** : **le précis fait foi** — ROE/ROA, ratios bancaires,
  dettes croisées sont déjà extraits et sourcés. Rien à ré-extraire.
- **tunisia-data apporte** : la **VA / productivité** (absente du précis) et le **long terme 2000-2017**
  (banques, Tunisair…) que les rapports MdF ne couvrent pas.
- **À faire (léger)** : brancher nos séries longues (masse sal./PNB, résultat/PNB depuis 2000) en
  amont des ratios bancaires du précis pour une lecture 2000-2023 continue.

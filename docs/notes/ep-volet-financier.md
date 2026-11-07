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

## Volet bancaire longue durée (2000-2024) — extrait par nous des EF (6 nov. 2026)
4 agents (un par banque) ont extrait des états financiers individuels (BVMT, au corpus) :
total_actifs, capitaux_propres, charges_générales_exploitation (CH7), dotations_amortissements (CH8)
→ `data/processed/entreprises-publiques/{bna,stb,bh,bte}_bancaire.csv` (sourcés, scripts reproductibles).
Joints à PNB + frais de personnel + résultat net déjà en base.

**Validation** : coefficient d'exploitation = (frais de personnel + CH7 + CH8) / PNB **= précis au
centième** sur 2018-2023 (BNA 48,0→38,5 ; STB 46,4→48,9 ; BH 41,5→39,5). Les postes lus sont les bons.

**Coefficient d'exploitation (%)** — nouvelle série 2000-2024 (le précis commençait en 2018) :
- BNA : 62 (2000) → 73 (2004) → **39 (2023)** — forte amélioration continue.
- BH : 65 (2003) → **38 (2024)** — la plus efficiente.
- STB : 71 (2002, crise) → 46 (2007-09) → **re-dégradation 49-53 (2023-24)**.
- BTE : 33 (2004) → **99-103 (2022-24)** — coûts > PNB (petite banque, exploitation en perte ;
  résultat net positif via produits de placement, à expliciter).

**ROA (%)** — rentabilité des actifs, robuste (préférée au ROE, distordu par les fonds propres) :
- **Creux 2013** (recapitalisation banques publiques) vif : **STB −1,6 % (−115 MD), BH −3,0 % (−159 MD)** ;
  BNA l'a traversé (+0,2 %). ROE 2013 : STB −101 %, BH −70 % (fonds propres impairs).
- **BNA 2016 : ROA 8,2 %** = aberration (élément exceptionnel, résultat/PNB 205 %) → à vérifier/flaguer.
- BTE : négatif 2014, puis fort (2,3-2,5 % en 2021-2023).

Données brutes et ratios : `data/processed/entreprises-publiques/*_bancaire.csv` + scripts.
Lacunes : BNA 2001/2002 (EF absents du corpus).

## Résultats bancaires vérifiés (re-lecture image, 7 nov. 2026)

Série `entreprises-publiques-ratios-bancaires` reconstruite sur les états financiers **re-lus à
l'image** (après qu'une 1re construction sur couche générée se soit révélée fausse : résultat net mal
lu, frais de personnel reclassés). Chaînage N/N-1 vérifié ; **coefficient d'exploitation concordant au
dixième avec les fiches du ministère des Finances (2018-2023), STB 2020 résolu**. ROA/ROE sur le
résultat **après modifications comptables** (base MdF) ; ROE laissé vide à capitaux propres ≤ 0.

| Banque | Coeff. expl. (%) | ROA (%) | ROE (%) | Lecture |
|---|---|---|---|---|
| **BNA** | 62 (2000) → 40 (2024) | 0,8-1,5 stable | 7-15 | la plus saine, jamais en perte |
| **STB** | 72 (2002) → 39 (2019) → 50 (2025) | −1,6 (2012) → 1,4 (2019) → 0,3 (2023) | −31 (2012) → 15 (2019) → 3,5 (2023) | redressée puis re-faiblit |
| **BH** | 65 (2003) → 38 (2024) | −4,1 (2013) → 1,2 (2019) → 0,5 (2024) | −97 (2013) → 14 (2019) | choc 2013 violent puis redressement |
| **BTE** | 39 (2003) → 102 (2024) | 1,7 → −2,1 (2024) | 5,6 → −82 (2024) | en détresse : frais > PNB, fonds propres impairés |

**Constats.** (1) La crise post-2011 est nette : STB ROE −31 % (2012), BH ROA −4,1 % / ROE −97 %
(2013). (2) Redressement 2014-2019 (coefficient en baisse, ROA/ROE au vert, STB et BH à ~15 % de ROE
en 2019). (3) Tassement 2020-2024 (Covid + provisions). (4) Les trois grandes convergent vers un
coefficient d'exploitation de 38-50 % et un ROA modeste (~0,5-1 %). (5) **BTE** fait exception, en perte
récente, fonds propres impairés — d'où le ROE à −82 % (illustration du biais : on lit le ROA). Tout
sur **2000-2024**, là où le rapport MdF ne couvre que 2018-2023.

# Dette publique « prêt par prêt » — note de faisabilité sourcée

Note documentaire (documentaliste). Objet : peut-on reconstituer la dette **prêt par prêt** —
prêteur, montant, **taux**, **maturité**, **remboursements année par année** ? À quelle maille, de
quelle source, avec quel effort. Rien n'est avancé ici sans source vérifiée ; les valeurs citées
sont datées et renvoient à l'URL qui les rend. Complète la note de cadrage
`annexe-dette-publique.md` (§ 3, qui constatait l'absence de série d'encours ligne-à-ligne).

Vérifications exécutées le 2026-11-06 (SQLite local `jort_cache.db` ; API Banque mondiale en ligne).

---

## 1. Le census JORT des prêts — ce qu'il donne, ce qu'il ne donne pas

**Principe établi** (note de cadrage, confirmé ici) : le recensement exhaustif des **prêts
extérieurs contractés ou garantis par l'État** passe par les **lois d'approbation** (et décrets de
ratification) des accords de prêt publiés au *Journal officiel*. Chaque emprunt extérieur de l'État
suit la voie : accord signé → **loi portant approbation** (ARP) → **décret portant ratification** →
publication au JORT. Le titre identifie prêteur + objet/projet + date de signature.

### 1.1 Requête SQL de référence (rejouable)

Base : `sqlite3 'file:/home/benjello/projets/PDFs-legislation-tunisie/jort_cache.db?immutable=1'`.
Deux flux, réunis et dédoublonnés par `recid` dans `scripts`/`/tmp/build_registre.py` (voir
`docs/notes/dette-registre-jort.csv`) :

**(A) Titres français** — `LIKE` écrit **sans accent** (piège `outillage-sources.md` §1 c :
`LIKE` sensible aux accents, titres majoritairement non accentués dans le corps) :

```sql
SELECT recid,type,numero,jort_annee,jort_numero,pages,date_signature,objet,titre,pdf_fr
FROM textes
WHERE jort_annee BETWEEN 1956 AND 2026
  AND ( titre LIKE '%accord de pr%t%'      OR titre LIKE '%convention de cr%dit%'
     OR titre LIKE '%convention de pr%t%'  OR titre LIKE '%accord de financement%'
     OR titre LIKE '%accord de cr%dit%' );
```
→ **762 textes** (`%pr%t%` / `%cr%dit%` absorbent l'accent de « prêt »/« crédit »).

**(B) Titres arabes seuls** — indispensable : une part des notices n'a qu'un intitulé arabe
qu'aucune requête française n'atteint (`outillage-sources.md` §1 g : 37 % en 2011, 40–80 % de 2015
à 2019). La forme « accord/convention de prêt » s'y lit اتفاق/اتفاقية القرض :

```sql
SELECT ... FROM textes
WHERE jort_annee BETWEEN 1956 AND 2026
  AND titre GLOB '*[؀-ۿ]*'
  AND ( titre LIKE '%اتفاق القرض%'  OR titre LIKE '%اتفاقية القرض%'
     OR titre LIKE '%اتفاقية قرض%'  OR titre LIKE '%اتفاق قرض%'
     OR titre LIKE '%اتفاقية التمويل%' OR titre LIKE '%اتفاق التمويل%' );
```
→ **119 textes supplémentaires** (1 recouvrement avec le flux A), concentrés en 2015-2019 — soit
exactement les années où l'intitulé arabe domine. **Le seul flux français sous-compte donc les
prêts de ces années** : caveat majeur à porter dans l'annexe.

**Total registre : 881 lignes** (762 FR + 120 à intitulé arabe − 1 recouvrement), 1962 → 2026.

### 1.2 Couverture par décennie (registre consolidé)

| Décennie | titres FR | titres AR | total |
|---|---:|---:|---:|
| 1960 | 11 | 0 | 11 |
| 1970 | 85 | 0 | 85 |
| 1980 | 186 | 0 | 186 |
| 1990 | 118 | 0 | 118 |
| 2000 | 172 | 0 | 172 |
| 2010 | 97 | 111 | 208 |
| 2020 (→2026) | 92 | 9 | 101 |
| **Total** | **761** | **120** | **881** |

Note : une ligne = un **texte** ; un même accord génère souvent **deux** textes (loi d'approbation
+ décret de ratification), parfois un **avenant** ultérieur. Le registre n'est donc pas un compte
d'emprunts distincts mais un **recensement de textes** ; le dédoublonnage par accord se ferait sur
(prêteur, date de signature, objet). Prêteur et date de signature sont extraits du titre par
expression régulière quand ils y sont lisibles : **612/761** titres FR portent un prêteur exploité,
**575/761** une date de signature ; vides sinon (pas d'invention). Les titres arabes ne sont pas
parsés (champs laissés vides, titre conservé tel quel).

### 1.3 Ce que le titre NE porte PAS

Le champ `objet` **ne répète que le titre**. Montant, taux, maturité, échéancier **n'y sont pas**.
Reste la question du **corps** du texte au fascicule (§ C ci-dessous).

---

## 2. Banque mondiale — International Debt Statistics (IDS) / Debtor Reporting System (DRS)

Source du **détail par créancier et des flux année par année** pour la **dette extérieure publique
et garantie publiquement (PPG)**. API publique testée pour la Tunisie (`TUN`) le 2026-11-06.

### 2.1 Deux points d'entrée API, tous deux fonctionnels

**(a) Agrégats (source WDI, dimension pays × indicateur × temps)** — URL simple :

```
https://api.worldbank.org/v2/country/TUN/indicator/DT.DOD.DECT.CD?format=json&date=2020:2023
```
Renvoie (vérifié, `lastupdated 2026-10-08`), *External debt stocks, total (current US$)* :
2020 = 41,977 G$ ; 2021 = 43,022 G$ ; 2022 = 41,041 G$ ; **2023 = 42,407 G$**.

**(b) IDS par créancier (source 6, dimension `counterpart-area`)** — c'est le niveau fin.
Les codes `DT.*.DPPG.*` n'existent QUE dans la source 6 ; l'endpoint WDI (a) les refuse (« indicator
not found »). Il faut l'endpoint *sources* :

```
https://api.worldbank.org/v2/sources/6/country/TUN/series/DT.DOD.DPPG.CD/counterpart-area/all/time/all?format=json&per_page=20000
```
Structure de réponse : `d['source']['data']`, chaque point portant les dimensions `Country`,
`Time`, `Series`, **`Counterpart-Area`** (= le créancier). `lastupdated 2026-11-05`.

### 2.2 Ventilation par créancier — elle existe, elle est publique

Encours PPG par **counterpart-area**, année **2023** (série `DT.DOD.DPPG.CD`, URL ci-dessus avec
`time/YR2023`) — **38 créanciers renseignés**, dont :

| Créancier (counterpart-area) | Encours PPG 2023 |
|---|---:|
| World (total) | 22,09 G$ |
| World Bank–IBRD | 4,32 G$ |
| Bondholders (marchés / eurobonds) | 3,89 G$ |
| African Dev. Bank | 2,64 G$ |
| European Investment Bank | 1,46 G$ |
| European Union | 1,22 G$ |
| Germany | 1,13 G$ ; France | 1,07 G$ |
| Saudi Arabia | 0,81 G$ ; Japan | 0,79 G$ |
| Arab Fund for Econ. & Social Dev. (FADES) | 0,77 G$ |
| Islamic Dev. Bank | 0,61 G$ ; African Export-Import Bank | 0,50 G$ |
| … (Kuwait, Italy, EBRD, BADEA, IFAD, OPEC Fund, Qatar, UAE, Libya, Algérie, Chine, etc.) | |

Ces créanciers **recoupent nommément les prêteurs du registre JORT** (AfDB, BIRD, FADES, AFD/France,
BEI, Koweït, Arabie saoudite…) : les deux sources parlent des mêmes bailleurs, à des mailles
différentes.

### 2.3 Flux année par année — tirages, amortissement, intérêts, service, **y compris projetés**

Toutes testées, counterpart `World`, série/temps `all` (valeurs en G$ sauf mention) :

| Indicateur | Libellé | Valeurs récentes (réalisé) | **Projeté** (échéancier futur) |
|---|---|---|---|
| `DT.DIS.DPPG.CD` | Tirages PPG | — | 2028 = 1,37 ; 2033 = 0,04 |
| `DT.AMT.DPPG.CD` | **Remboursement du principal** | 2023 = 2,12 ; 2024 = 2,75 ; 2025 = 2,79 ; 2026 = 3,22 ; 2027 = 2,67 | 2028 = 2,07 … 2033 = 1,53 |
| `DT.INT.DPPG.CD` | **Intérêts** | — | 2028 = 0,41 … 2033 = 0,23 |
| `DT.TDS.DPPG.CD` | Service total (principal+intérêts) | — | 2028 = 2,48 … 2033 = 1,76 |

**Fait décisif** : l'API publie l'**échéancier de remboursement année par année, y compris les
années à venir (2026 → 2033+)** — exactement la « dette année par année » demandée —, et **cette
projection existe aussi par créancier** : testé `DT.AMT.DPPG.CD`, `time/YR2027`, **33 créanciers**
avec amortissement programmé (Bondholders 341,9 M$ ; AfDB 317,9 M$ ; Afreximbank 291,7 M$ ;
BEI 234,8 M$ ; France 215,1 M$ ; IBRD 184,3 M$ ; BID 153,1 M$ ; Allemagne 152,9 M$…).

### 2.4 Conditions moyennes (taux, maturité) — niveau agrégat, par guichet

| Indicateur | Libellé | Valeurs (counterpart World) |
|---|---|---|
| `DT.INR.DPPG` | **Taux d'intérêt moyen des nouveaux engagements (%)** | 2020 = 1,06 ; 2021 = 1,58 ; 2022 = 2,00 ; **2023 = 5,06** ; 2024 = 4,66 ; 2025 = 3,67 |
| `DT.INR.OFFT` / `DT.INR.PRVT` | idem, officiel / privé | disponibles |
| `DT.MAT.DPPG` | **Maturité moyenne des nouveaux engagements (ans)** | 2020 = 18,7 ; 2023 = 15,0 ; **2025 = 28,4** |

Taux et maturité sont donc des **moyennes annuelles des nouveaux engagements** (par guichet
officiel/privé via `.OFFT`/`.PRVT`), **pas** le taux/maturité d'un prêt donné.

### 2.5 Limite dure : créancier/guichet, jamais le prêt individuel

L'IDS dérive du **DRS**, où la Tunisie déclare prêt par prêt (formulaires 1 & 2), mais la Banque
mondiale **ne publie que l'agrégation par créancier et par guichet** (bilatéral/multilatéral/privé,
`OFFT`/`PRVT`/`MLAT`/`BLAT`, et par pays/institution créancière). **Il n'existe PAS de niveau
« prêt » public** dans l'API : la maille fine publique est le **couple (créancier × année ×
indicateur)**, pas l'emprunt nominatif. Le ligne-à-ligne réel reste interne (DRS confidentiel côté
BM ; SIADE côté tunisien).

---

## 3. BCT et ministère des Finances — l'agrégat réalisé, en dinars

Ce que ces sources ajoutent (déjà repéré en cadrage, non ré-téléchargé ici) :
- **BCT** — rapport annuel sur la dette extérieure et tableaux statistiques en ligne : taux moyen
  apparent, maturité moyenne, **service réalisé** en dinars, ventilation par devise et par type de
  créancier. Maille : agrégat / catégorie, pas le prêt.
- **Ministère des Finances** — *Rapport sur la dette publique* (annexe 7 au PLF, en arabe) :
  encours État intérieur/extérieur, service budgété, structure par devise et par taux (fixe/
  variable), **couvre aussi la dette intérieure** (BTA, BTCT, marché local) que l'IDS, limité au PPG
  extérieur, ne voit pas. Clés déjà au projet : `minfin-dette-2022`, `minfin-dette-2025`.

Apport propre : la **dette intérieure** (en dinars, marché local) et la **conversion en dinars** du
service extérieur — absentes de l'IDS (libellé US$, PPG extérieur seulement).

---

## 4. Verdict de faisabilité

**Le « prêt par prêt » nominatif (un emprunt = une ligne avec son taux, sa maturité, son
échéancier) n'est atteignable pour AUCUNE source publique.** Ni le JORT, ni l'IDS/DRS, ni la BCT/
MdF ne publient l'emprunt individuel avec ses conditions financières. Ce qui est réellement
atteignable, par maille :

| Dimension | JORT (registre) | IDS/DRS (BM) | BCT / MdF |
|---|---|---|---|
| **Recensement nominatif des prêts extérieurs** | ✅ titre : prêteur, objet, date, **montant plafond** (voir §C) | ✗ (agrégé par créancier) | ✗ |
| Taux d'un prêt donné | ✗ | ✗ (moyenne annuelle seulement) | ✗ |
| Maturité d'un prêt donné | ✗ | ✗ (moyenne annuelle) | ✗ |
| **Flux par créancier, année par année (dont futur)** | ✗ | ✅ **(counterpart-area)** | partiel |
| Taux / maturité moyens, par guichet | ✗ | ✅ `INR`/`MAT` | ✅ (réalisé, dinars) |
| **Dette intérieure / marché local** | lois d'emprunt intérieur à part | ✗ (PPG extérieur seul) | ✅ |

**Croisement recommandé JORT × IDS** : le **JORT** donne le *catalogue nominatif* des prêts
extérieurs (qui, quand, quel projet, quel montant plafond) ; l'**IDS** donne, pour les **mêmes
créanciers**, les *flux et conditions moyennes année par année*, projetés inclus. En les appariant
**par créancier** (et par millésime de signature), on reconstitue une vue « par bailleur »
quasi-complète de la **dette extérieure PPG** — jamais « par prêt ». Pour la **dette intérieure**
(BTA/BTCT, marché en dinars), seul l'agrégat MdF/BCT existe : **aucun ligne-à-ligne**, et l'IDS ne
la couvre pas.

**Part de la dette réellement « traçable au bailleur, année par année » : la dette extérieure PPG**
(≈ la totalité de l'extérieure de l'État et garantie). **Non traçable finement : la dette intérieure
/ de marché**, qui n'existe qu'en agrégat MdF/BCT.

---

## C. OCR d'un échantillon de lois d'approbation (le JORT suffit-il pour les termes ?)

Échantillon : **Loi 2025-3** (JORT n° 15/2025, p. 310, `Jo0152025.pdf`) et **Loi 2025-7**
(JORT n° 54/2025, p. 1221, `Jo0542025.pdf`). Fascicules FR présents au corpus local
(`PDFs-legislation-tunisie/PDFs/JORT/2025/fr/`), **couche texte exploitable** (`pdftotext -layout`,
30–46 k caractères, français) — pas d'OCR image nécessaire.

- **Loi 2025-3** (BAD, programme CAP-EMPLOIS) — texte intégral de l'acte :
  > « **Article unique** — Est approuvé l'accord de prêt, **annexé à la présente loi**, conclu à
  > Tunis le 10 septembre 2024 entre la République tunisienne et la **Banque africaine de
  > développement** d'un **montant n'excédant pas quatre-vingt-dix millions (90 000 000) d'euros**
  > pour la contribution au financement du programme […] (CAP-EMPLOIS). »
- **Loi 2025-7** (BAD, infrastructures routières III) — même forme :
  > « Article unique — Est approuvé l'accord de prêt, **annexé à la présente loi**, conclu à Tunis
  > le 24 janvier 2025 […] et la Banque africaine de développement, **d'un montant de quatre-vingt
  > millions cent soixante-[…]** ».

**Conclusion** : la loi imprime **prêteur + date de signature + objet + MONTANT (plafond, devise)**
— davantage que le titre, mais **ni taux, ni maturité, ni échéancier**. L'accord est « annexé à la
présente loi » **mais l'annexe n'est pas reproduite au JORT** : le fascicule ne contient que
l'article unique d'approbation (et, plus loin, le décret de ratification, de forme identique). Sur
les deux textes examinés, aucune table de conditions financières ne suit.

→ **Le JORT ne suffit pas pour les termes.** Il fixe le **recensement nominatif + le montant** ;
pour **taux, maturité et remboursements**, il faut la **Banque mondiale (IDS)** — au niveau
créancier, pas prêt. Le registre JORT gagnerait à porter une colonne **`montant`** extraite du
corps (à l'image / couche texte) ; non fait ici (le registre est bâti sur les métadonnées de
titre), à verser au backlog.

---

## Lacunes et reports (à verser au backlog durable)

1. **Dette intérieure / de marché non couverte prêt-par-prêt ni par bailleur** : BTA, BTCT,
   emprunts en dinars — seul l'agrégat MdF/BCT existe. Aucune source publique ligne-à-ligne.
2. **Niveau « prêt » inexistant publiquement** même pour l'extérieur PPG : DRS confidentiel (BM),
   SIADE interne (MdF). Maille fine publique = créancier × année.
3. **Sous-comptage JORT des années à intitulé arabe** (2015-2019 surtout) corrigé ici par le flux
   arabe (+119 textes), mais à **rejouer périodiquement** (notices arabes récentes) et à **compléter
   par terme arabe** dans une éventuelle fiche `recherches.yml` dédiée (`iort_ar`).
4. **Montant non extrait au registre** : présent dans le corps de la loi (OCR/couche texte), absent
   des colonnes actuelles (bâties sur le titre). Enrichissement possible, non fait.
5. **Dédoublonnage par accord non fait** : le registre compte des **textes** (loi + décret +
   avenants), pas des emprunts distincts.
6. **À rapatrier dans `tunisia-data`** (signalé, non téléchargé — garde-fou) :
   - Extraction IDS Tunisie par créancier (séries `DT.DOD/DIS/AMT/INT/TDS.DPPG.*` et `.OFFT/.PRVT`,
     `DT.INR.*`, `DT.MAT.DPPG`), via
     `https://api.worldbank.org/v2/sources/6/country/TUN/series/<série>/counterpart-area/all/time/all?format=json` ;
   - Rapport annuel BCT sur la dette extérieure (`bct.gov.tn`) et tableaux statistiques en ligne ;
   - *Rapport sur la dette publique* MdF annexe 7 au PLF (clés `minfin-dette-2022/2025` déjà
     référencées) pour le volet intérieur et la conversion dinar.

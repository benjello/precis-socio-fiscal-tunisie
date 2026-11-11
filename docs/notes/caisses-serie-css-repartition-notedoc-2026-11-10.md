# Série (4) — Produit de la CSS et sa répartition entre caisses (`css-repartition`) : note documentaire

> Note documentaire (rôle documentaliste), 10 novembre 2026. Instruit la série (4) du § 3 de
> `cadre-budgetaire-comptable-caisses.md` : `css-repartition` — « produit de la CSS et répartition
> entre caisses (arrêtés du compte de diversification, annexes budgétaires) — à condition de
> retrouver les arrêtés ». Traite la lacune **L8** de la note de cadre et la fiche de recherche
> **`r-css-arretes-repartition`**. Rien n'a été téléchargé, versionné ni modifié : le matériau
> chiffré est déjà dans l'entrepôt `tunisia-data` ; les textes sont lus au corpus JORT local et sur
> `pist.tn`. Aucun fichier du précis, de `tunisia-data`, de `glossaire.yml`, de `backlog-precis.md`
> ni de `docs/recherches.yml` n'a été touché.
>
> **Niveaux d'attestation** (convention des notes sœurs) : **[T]** texte lu au fascicule (image ou
> couche texte) ; **[M]** seul l'intitulé (`jort_cache`) est connu ; **[S]** source secondaire
> (rapport, annexe budgétaire, publication) ; **[D]** déduction de la note. URL `pist.tn` et
> `finances.gov.tn` vérifiées le 10 novembre 2026 (`curl -k -r 0-1200` : 206, `application/pdf`).

---

## 1. Verdict de couverture (résumé)

**Deux grandeurs, deux verdicts opposés.**

1. **La répartition de la CSS n'est régie par aucun arrêté retrouvé.** La base légale
   (décret-loi n° 2021-21, art. 12 § 3) renvoie les *critères de répartition* du compte de
   diversification à « un arrêté du ministre chargé de la sécurité sociale » (قرار). **Cet arrêté
   n'est pas identifié** : absent de `jort_cache` (index à jour au 29 octobre 2026, ≥ 1 000 textes
   par an pour 2022-2026) et absent du corpus JORT local (712 fascicules arabes 2022-2026 balayés
   au plein texte, un seul sans couche texte). La seule occurrence de « حساب تنويع مصادر الضمان
   الاجتماعي » dans tout le corpus 2022-2026 est dans les **deux lois** elles-mêmes (création en
   LF 2022, nouvelles recettes en LF 2026) — **jamais** dans un arrêté. Je **juge** (sans l'avoir
   lu) qu'il s'agit probablement d'une **décision administrative non publiée au JORT**, comme c'est
   l'usage pour les critères de gestion interne d'un compte spécial du Trésor ; mais je ne peux pas
   l'affirmer : l'absence de l'index et du corpus ne prouve pas l'inexistence.

2. **Le produit de la CSS n'est chiffrable, année par année, que pour la *part CNRPS*.** Les
   annexes budgétaires (rapport sur les entreprises publiques annexé aux lois de finances — dit
   « annexe 9 »), la fiche de jumelage UE et les RAP/PAP du ministère des Affaires sociales
   donnent la CSS **attribuée à la CNRPS** : **200 (2018), 450 (2019), 460 (2020), 500 (2021),
   195 (2022), 420 (2023)** millions de dinars **[S]**. Le **produit total** de la CSS et les
   **parts CNSS et CNAM** ne sont isolés dans aucune source lue : c'est la lacune de fond de la
   série. La ligne consolidée existe *de iure* (recettes du compte spécial, tableau B des recettes
   des comptes spéciaux du Trésor annexé aux lois de finances depuis 2020) mais n'est pas encore
   extraite au catalogue `tunisia-data`.

**Conséquence pour la série.** `css-repartition` n'est, en l'état des sources retrouvées, **pas
une série de répartition** (CNSS / CNRPS / CNAM) : c'est une **série à une seule branche connue**
(CNRPS, 2018-2023) plus un **total à retrouver**. La construire comme répartition supposerait soit
l'arrêté (introuvable), soit les recettes du compte spécial croisées aux versements à chaque caisse
(tableau B des LF + états financiers des trois caisses). La règle « longue et homogène d'abord »
impose ici de **laisser le trou honnête** : publier la part CNRPS sourcée, et marquer CNSS, CNAM et
total comme non chiffrés, plutôt que de répartir le produit par une clé reconstruite.

---

## 2. La répartition : base légale et recherche de l'arrêté

### 2.a Base légale (texte lu)

**Décret-loi n° 2021-21 du 28 décembre 2021 (LF 2022), art. 12.** JORT n° 119 du 28 décembre 2021,
**FR p. 3081-3082** (édition française vérifiée : <https://www.pist.tn/jort/2021/2021F/Jo1192021.pdf>,
206/`application/pdf`), AR p. 3081 (<https://www.pist.tn/jort/2021/2021A/Ja1192021.pdf>). Clé
`lf-2022`. **[T]** (lu sur la couche texte FR et AR).

> Art. 12 — 1) Est ouvert dans les écritures du Trésorier général de la Tunisie un compte spécial
> du trésor intitulé « compte de diversification des sources de sécurité sociale » pour financer les
> caisses de sécurité sociale. Le ministre chargé de la sécurité sociale est l'ordonnateur de ce
> compte. Les dépenses de ce compte ont un caractère estimatif.
> 2) Les ressources du « compte de diversification des sources de sécurité sociale » proviennent des
> recettes de la contribution sociale de solidarité instituée par les dispositions de l'article 53
> de la loi n° 2017-66 du 18 décembre 2017 […] ; d'autres recettes peuvent être affectées au profit
> de ce compte.
> **3) Les critères de répartition des recettes du « compte de diversification des sources de
> sécurité sociale » entre les caisses de sécurité sociale sont fixés par arrêté du ministre chargé
> de la sécurité sociale.**

AR du § 3 : « تضبط معايير توزيع عائدات "حساب تنويع مصادر الضمان الاجتماعي" على صناديق الضمان
الاجتماعي بمقتضى **قرار** من الوزير المكلّف بالضمان الاجتماعي. » Le mot est **قرار** : « arrêté »
*ou* « décision », indistinctement — ce qui ouvre la possibilité d'une décision non publiée.

### 2.b Recherche de l'arrêté (ce qui a été fait, et ce qu'il reste)

**`jort_cache.db`** (`~/projets/PDFs-legislation-tunisie/jort_cache.db`, `MAX(date_publication)` =
2026-10-29 ; 79 790 notices ; 682 à 1 410 textes/an de 2022 à 2026) :

- `titre LIKE '%تنويع%' OR objet LIKE '%تنويع%'` → **2 notices seulement** : loi n° 2019-78 (LF 2020)
  art. 54 (« تنويع مصادر التمويل » — sans rapport : emprunt) et décret-loi n° 2021-21 (LF 2022)
  art. 12 (création du compte). Aucun arrêté.
- `titre LIKE '%diversification%'` → le seul texte français est un décret de don (2020-999), sans
  rapport.
- Arrêtés du ministre des affaires sociales 2022-2026 (`type LIKE '%rr%'`, ministère des affaires
  sociales) : conventions collectives, concours, barèmes d'actualisation des salaires, prix du
  pain/transport — **aucun** « critères de répartition » ou « صناديق الضمان » / « توزيع ».
- `titre LIKE '%توزيع%' AND (…صندوق… OR …الضمان… OR …الصناديق…)` depuis 2021 → aucun.
- La seule notice liée au numéro « 2021-21 » et au couple affaires sociales/finances (recid 165037,
  arrêté du 18 février 2022) porte sur l'**indemnité exceptionnelle de l'art. 61**, pas sur la
  répartition. **[M]**

**Corpus JORT local** (`PDFs/JORT/20{22,23,24,25,26}/`) : balayage plein texte (`pdfgrep` /
`pdftotext`) des fascicules arabes **et** français 2022-2026. Hits « تنويع » : `Ja0582022`,
`Ja0802022`, `Ja1452024`, `Ja0352025` (tous = « tنويع » dans d'autres contextes : programmes,
formation), et **`Ja1482025`** (LF 2026). Hits « تنويع مصادر الضمان الاجتماعي » : **uniquement
`Ja1482025`** (LF 2026, art. 20). Côté FR, « diversification des sources » → **zéro** fascicule
2022-2026. **Lacune de couverture** : un seul fascicule arabe sans couche texte dans l'intervalle
(`Ja0922022`, n° 92/2022, 194 caractères extraits) ; il n'a pas été océrisé.

**Conclusion documentaire.** Aucun arrêté de répartition de la CSS/du compte de diversification
entre caisses n'est publié au JORT dans la fenêtre couverte (création du compte le 28/12/2021 →
29/10/2026). Trois lectures possibles, que je **ne tranche pas** faute de pièce :
(i) la décision existe mais **n'est pas publiée au JORT** (hypothèse la plus probable, cf. le mot
قرار et l'usage des comptes spéciaux) ; (ii) la répartition se fait **sans acte réglementaire
distinct**, par les inscriptions budgétaires annuelles (annexe 9, cf. § 3) ; (iii) l'arrêté a été
publié dans le seul fascicule non lu (`Ja0922022`) — à écarter ou confirmer par OCR.

---

## 3. Le produit de la CSS : ce qui est chiffrable

### 3.a Part attribuée à la CNRPS, 2018-2023 (annexes budgétaires + jumelage + RAP) **[S]**

| Année | CSS CNRPS (MD) | Attestation | Sources concordantes |
|---|---|---|---|
| 2018 | **200** | [S] | rapport sur les entreprises publiques annexé à la LF 2022 (« annexe 9 », AR) ; fiche de jumelage UE p. 25 ; états financiers CNRPS ; annexe 9 des LF 2020-2024 |
| 2019 | **450** | [S] | idem ; jumelage UE p. 25 ; états financiers CNRPS |
| 2020 | **460** | [S] | trois éditions de l'annexe 9 + jumelage (460) ; **variante 450** dans le RAP 2020 p. 39 (« crédits de l'ordre de 450 M.D imputés au budget de l'État pour 2020 au titre de la CSS ») ; **500** en renvoi du RAP 2021 p. 26 |
| 2021 | **500** | [S] | note de l'annexe 9 (LF 2023) ; = 835 − 335 (annexe 9, LF 2024) |
| 2022 | **195** | [S] | annexe 9 la plus récente |
| 2023 | **420** | [S] | annexe 9 (LF 2024/2025) |

Source dérivée : `tunisia-data`, `data/processed/caisses/cnrps_ratios_charges_produits.csv`
(fiche `sources/mas-rap-pap-cnrps.md`) ; PDF au catalogue `sources/cnrps-tutelle-urls.csv`
(non versionnés). Règle de reconstitution déjà fixée par cette fiche : « la valeur du tableau de
l'annexe 9 la plus récente fait foi ». **Cumul 2018-2022** imprimé par le RAP 2022 (p. 28) :
**2 150 MD** (contre 1 805 MD pour la somme des valeurs annuelles retenues : écart non levé par la
fiche, liste d'années fautive « 2018-2019-2020-2022-2022 » dans la source).

**Fiche de jumelage UE** (`data/raw/caisses/minfin/renforcement_regime_retraite.pdf`, p. 25,
« Soldes financiers du Régime de retraite CNRPS ») : ligne « CSS * » = 200 / 450 / 460 pour
2018 / 2019 / 2020, ajoutée **après** le solde pension (le régime ne la compte pas dans ses
recettes). **[S]**, lu à l'image le 10 novembre 2026.

**États financiers CNRPS** (fiche `sources/cnrps-etats-financiers.md`) : « Ni la contribution
sociale de solidarité (200, 450 et 460 millions de dinars en 2018, 2019 et 2020) […] ne figurent
dans les recettes du régime : le rapport 2020 (p. 25) les ajoute après le résultat net. » **[S]**

**Mise en garde de périmètre** (fiche `sources/minfin-transferts-cnrps.md`) : la CSS passe, depuis
2022, par le compte spécial « تنويع مصادر الضمان الاجتماعي » ; **ne pas l'additionner** aux
transferts budgétaires de l'annexe 8 (risque de double compte) ; avant 2022, elle a pu transiter
par les crédits d'intervention du budget.

### 3.b Produit total et parts CNSS / CNAM : non isolés (lacune)

Aucune source lue ne donne le **produit total** de la CSS ni les parts **CNSS** et **CNAM**. Les
chiffres ci-dessus ne sont que la branche CNRPS. La ligne consolidée doit se chercher dans :
- le **tableau B des recettes des comptes spéciaux du Trésor** annexé aux lois de finances (depuis la
  LF 2020 ; le compte de diversification y a une ligne de recettes = produit de la CSS budgété, puis
  réalisé en loi de règlement). Le catalogue `tunisia-data` (`sources/jort-lf-budget-etat.md`,
  `data/processed/jort/budget_etat_lois_de_finances_1986_2026.csv`) n'agrège que le total des CST
  (`cst_md`), **sans** ligne par compte : à extraire. **[D]**
- le **rapport de la Cour des comptes** (rapport annuel général, chapitre « comptes spéciaux du
  Trésor » ou mission sur les caisses) ;
- l'**INS** : l'annuaire statistique et les comptes de la nation portent une ligne « Compte de
  diversification des sources de financement de la sécurité sociale » (cf.
  `sources/ins-annuaires-statistiques.md`, 2019-2023), à relever ;
- les **rapports du FMI** (Selected Issues, Article IV) : pistes non épuisées.

### 3.c Développement LF 2026 : le compte cesse d'être alimenté par la seule CSS **[T]**

**Loi n° 2025-17 du 12 décembre 2025 (LF 2026), art. 20** (« تعزيز موارد تمويل الصناديق الاجتماعية »
— renforcement des ressources de financement des caisses sociales), § 7 : ajoute à l'art. 12 § 2 du
décret-loi n° 2021-21 de **nouvelles recettes affectées** au compte de diversification. JORT n° 148
du 12 décembre 2025, **AR p. 4234-4235** (<https://www.pist.tn/jort/2025/2025A/Ja1482025.pdf>, 206 ;
pas d'édition FR — l'URL `2025F/Jo1482025.pdf` sert le fascicule arabe). **[T]**, lu à l'image /
couche texte. Sont « ترصد لفائدة حساب تنويع مصادر الضمان الاجتماعي » :
- 50 % du droit d'enregistrement sur les donations d'immeubles entre ascendants/descendants et
  entre époux (art. 26 § 2 de la loi n° 80-88, LF 1981) ;
- 50 % du droit sur les tickets de vente (art. 117-I-10 du CDET) ;
- 50 % du droit de timbre sur les cahiers des charges (art. 117-II-10 bis) ;
- 20 % du droit sur les voyages aériens et maritimes internationaux (art. 81 de la loi n° 2015-53) ;
- 20 % de la taxe de séjour dans les établissements touristiques (art. 49, LF 2018) ;
- 20 % de la redevance sur boîtes de nuit, cabarets et clubs (art. 63, LF 2013) ;
- le **produit du relèvement** du droit de timbre sur les factures (art. 117-I-6 bis du CDET) et du
  droit sur les jeux et concours en ligne.

Conséquence pour la série : **à partir de 2026, les recettes du compte ne sont plus égales au
produit de la CSS** — le compte est « diversifié » au sens propre. Une série du *produit de la CSS*
et une série des *recettes du compte* divergent donc dès 2026 : à distinguer impérativement (note de
concordance de périmètres recommandée si les deux sont publiées).

---

## 4. Références candidates (CSL-JSON, à valider par le bibliographe)

Déjà présentes (à vérifier / compléter) :
- **`lf-2022`** (décret-loi n° 2021-21) : s'assurer que l'entrée porte l'URL FR
  `https://www.pist.tn/jort/2021/2021F/Jo1192021.pdf`, JORT n° 119 du 28/12/2021, et **art. 12 aux
  pp. 3081-3082** (édition française vérifiée le 10/11/2026).
- **`lf-2018`** (loi n° 2017-66, art. 53 — institution de la CSS) : déjà en références.
- **`lf-2026`** (loi n° 2025-17, art. 20 — nouvelles recettes du compte) : vérifier la pagination
  (le volet « recettes affectées » est AR pp. 4234-4235).

À créer (ébauches) :

```json
[
  {"id": "minfin-rapport-ep-2022", "type": "report",
   "title": "Rapport sur les entreprises publiques annexé au projet de loi de finances pour l'année 2022 (annexe n° 9)",
   "title-short": "Annexe 9 — entreprises publiques, LF 2022",
   "publisher": "République tunisienne, ministère des Finances", "issued": {"date-parts": [[2021]]},
   "URL": "http://www.finances.gov.tn/sites/default/files/2022-02/ANNEXE_09.pdf", "language": "ar",
   "note": "Section CNRPS (p. 48 ar) ; ligne CSS attribuée à la CNRPS. Fichier tunisia-data data/raw/caisses/minfin/annexe9_2022.pdf (MD5 a8f5a80f85352072ec20fcf878c06dbb)."},
  {"id": "ue-jumelage-retraite-2021", "type": "report",
   "title": "Renforcement du régime de retraite et sa gouvernance — fiche de jumelage TN 18 ENI SO 01 21",
   "publisher": "Union européenne, Programme d'appui institutionnel à la transition tunisienne (PAITT)",
   "issued": {"date-parts": [[2021, 11, 25]]},
   "URL": "https://um.fi/documents/385176/0/Renforcement+du+r%C3%A9gime+de+retraite+et+sa+gouvernance.pdf",
   "note": "Annexe III, p. 25 : soldes financiers CNRPS, ligne CSS 200/450/460 (2018-2020). tunisia-data data/raw/caisses/minfin/renforcement_regime_retraite.pdf (MD5 60ebd8ca9efcae59884ebbf76c8fb16d)."},
  {"id": "mas-rap-cnrps-2022", "type": "report",
   "title": "Rapport annuel de performance 2022 — mission Affaires sociales, programme Sécurité sociale",
   "publisher": "République tunisienne, ministère des Affaires sociales", "issued": {"date-parts": [[2023]]},
   "language": "ar",
   "note": "p. 28 : cumul CSS 2018-2022 = 2 150 MD. Via gbo.tn ; copie tunisia-data data/raw/caisses/mas/rap_2022_ar.pdf."}
]
```

(Les deux premières sources sont **déjà collectées et cataloguées** dans `tunisia-data` —
`sources/cnrps-tutelle-urls.csv`, `sources/ue-jumelage-retraite-2021.md`,
`sources/minfin-rapport-ep-*` / `sources/mas-rap-pap-cnrps.md` ; rien à retélécharger.)

---

## 5. Notions à glossaire (à vérifier, ne pas écrire ici)

- **Contribution sociale de solidarité (CSS)** — « المساهمة الاجتماعية التضامنية » : majoration de
  l'IRPP/IS instituée au profit des caisses sociales (loi n° 2017-66, art. 53). Source canonique :
  `lf-2018`. (Déjà traitée par la note `css-verification.md` ; signaler le renvoi.)
- **Compte de diversification des sources de sécurité sociale** — « حساب تنويع مصادر الضمان
  الاجتماعي » : compte spécial du Trésor ouvert par le décret-loi n° 2021-21, art. 12, alimenté par
  la CSS (puis, dès 2026, par d'autres droits affectés), ordonnateur = ministre chargé de la
  sécurité sociale. Source canonique : `lf-2022`, art. 12.

---

## 6. Lacunes (reports pour le backlog durable)

| # | Lacune | Statut | Piste |
|---|---|---|---|
| L8-a | **Arrêté/décision de répartition de la CSS entre caisses** (décret-loi n° 2021-21, art. 12 § 3) | **non identifié** ; absent de `jort_cache` (≤ 29/10/2026) et du corpus 2022-2026 | probablement non publié au JORT (قرار = décision de gestion) ; demander au ministère des Affaires sociales / à la Trésorerie générale ; OCR du fascicule `Ja0922022` (seul sans couche texte 2022-2026) ; fiche `r-css-arretes-repartition` (voir § 7) |
| L8-b | **Produit total de la CSS, année par année** (2018→) | **non isolé** ; seule la part CNRPS est chiffrée | extraire la ligne « compte de diversification » du **tableau B** (recettes des comptes spéciaux du Trésor) des LF 2022-2026 et des lois de règlement ; Cour des comptes ; INS (annuaire / comptes de la nation, ligne « compte de diversification ») |
| L8-c | **Parts CNSS et CNAM** de la CSS | **inconnues** | états financiers CNSS et CNAM 2018→ (la CSS ajoutée après résultat net, comme à la CNRPS) ; annexes 9 des LF ; à défaut, non chiffrables → trou honnête |
| L8-d | **Divergence CSS ≠ recettes du compte à partir de 2026** (LF 2026, art. 20) | **documentée (texte lu)**, non chiffrée | une fois le total connu, tenir deux séries distinctes (produit CSS / recettes du compte) et une note de concordance |
| L8-e | Fascicule `Ja0922022` (n° 92/2022) sans couche texte | **OCR à prévoir** | seule zone non couverte du balayage 2022-2026 |

---

## 7. Fiche de recherche `r-css-arretes-repartition` — mise à jour proposée (NON appliquée)

Je n'ai **pas** lancé `scripts/recherches.py` (qui réécrirait `docs/recherches.yml`). Ce que la
fiche existante devrait porter, après la présente passe :

- **objet** (inchangé) : arrêtés du ministre chargé de la sécurité sociale fixant les critères de
  répartition entre caisses des recettes du « compte de diversification des sources de sécurité
  sociale » (décret-loi n° 2021-21, art. 12).
- **requetes.titres_like** à ajouter (le FTS arabe de `jort_cache` est peu fiable, remove_diacritics
  sur l'arabe) : `'%تنويع مصادر%'`, `'%توزيع%الضمان الاجتماعي%'`, `'%صناديق الضمان%'`,
  `'%معايير توزيع%'`.
- **requetes.iort_ar** (obligatoire, période post-2011) : termes `تنويع مصادر الضمان الاجتماعي`,
  `توزيع عائدات`, `قرار من الوزير المكلّف بالضمان الاجتماعي`.
- **nouvelle passe** à consigner :
  - `date: 2026-11-10`, `role: documentaliste`, `sources: [jort_cache, corpus_local]` ;
  - `couverture` : « `jort_cache` (index au 29/10/2026) — `LIKE '%تنويع%'` sur titre et objet : 2
    notices (LF 2020 art. 54, LF 2022 art. 12), aucun arrêté ; arrêtés affaires sociales 2022-2026
    passés en revue, aucun "critères de répartition / صناديق الضمان". Corpus JORT local 2022-2026
    (712 fascicules AR + FR) balayé au plein texte : "تنويع مصادر الضمان الاجتماعي" n'apparaît que
    dans la LF 2022 (création, art. 12) et la LF 2026 (art. 20, nouvelles recettes) — jamais dans un
    arrêté. Non couvert : fascicule AR `Ja0922022` (sans couche texte) ; éditions FR manquantes sur
    pist.tn ; iort_ar non interrogé. » ;
  - `couvert_jusqu_au: 2026-10-29` ; `resultat: aucun`.
- **a_faire** : (1) OCR de `Ja0922022` ; (2) interroger `iort_ar` et le miroir iort ; (3) à défaut de
  publication, demande écrite au ministère des Affaires sociales / à la TGT ; (4) **découpler**
  l'objet : ouvrir une piste distincte pour le *produit total* de la CSS (tableau B des CST), qui
  n'est pas une recherche de texte réglementaire mais d'annexe budgétaire.

---

## 8. Où j'ai jugé plutôt que lu

- **« Arrêté probablement non publié au JORT »** (§ 1, § 2.b, L8-a) : **jugement**, fondé sur le mot
  قرار (décision) et l'usage des comptes spéciaux, non sur un document. L'absence de l'index et du
  corpus ne prouve pas l'inexistence.
- **« La ligne consolidée existe de iure dans le tableau B des CST »** (§ 3.b) : **déduction** du
  mécanisme budgétaire (un compte spécial a nécessairement une ligne de recettes), non vérifiée sur
  les fascicules — le tableau B n'a pas été ouvert dans cette passe.
- **Variantes 2020 de la CSS CNRPS (450 / 460 / 500)** : rapportées telles que la fiche
  `tunisia-data` les a relevées ; je n'ai pas rouvert les RAP pour les réarbitrer.
- **Pages de l'annexe 9 LF 2022 (p. 48 ar)** : le repère de section CNRPS est lu ; le tableau
  chiffré lui-même est en arabe mis en page (couche texte brouillée) — les valeurs retenues viennent
  du CSV `tunisia-data` et de la fiche de jumelage, non d'une relecture image de l'annexe 9.

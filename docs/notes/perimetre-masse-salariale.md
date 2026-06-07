# Note documentaire — Poids agrégé de la masse salariale publique tunisienne

> Matière sourcée pour le TODO « masse salariale agrégée » de la section A.2
> « Le périmètre du secteur public » (`precis/fr/remunerations_publiques/index.qmd`),
> ticket #6. Produite par l'agent documentaliste.

**Avertissement méthodologique.** WebFetch et le téléchargement direct des PDF étant
bloqués dans l'environnement de recherche, le texte intégral des rapports FMI/Banque
mondiale n'a pas pu être lu. Les chiffres ci-dessous proviennent de recherches web
restreintes aux domaines primaires (imf.org, worldbank.org) croisées avec la presse.
**Avant publication, revérifier les figures-clés (17,6 % ; 14,7 % ; effectifs) sur les
PDF sources** (références en section II).

## I. Faits sourcés

### A. Masse salariale en % du PIB (attention au périmètre et au dénominateur)

| Chiffre | Année | Périmètre | Source primaire |
|---|---|---|---|
| **17,6 % du PIB** | 2020 | administration centrale (civil service salary bill) | FMI, *Tunisia: 2020 Article IV Consultation*, publié fév. 2021 |
| **14,7 % du PIB** | 2017 | administration centrale et régionale (hors collectivités locales et entreprises publiques) | Banque mondiale, *Public Expenditure Review* 2020 |
| **+4 pts de PIB depuis 2010** | 2010→2017 | administration centrale (≈10,7 % → 14,7 %) | Banque mondiale, PER 2020 |
| 14,4 % du PIB | 2017/18 (prév.) | fonction publique | FMI cité par presse (à confirmer) |
| 14,1 % du PIB | 2016 | fonction publique | presse (à confirmer) |
| ≈10 % du PIB | 2010 | fonction publique | presse (à confirmer) |

Citation FMI (2020 Article IV, publié fév. 2021) : « *Additional hiring (about 40 percent
of which was in the health sector, including to fight the pandemic) pushed the civil
service salary bill to 17.6 percent of GDP, among the highest in the world.* »

### B. Masse salariale en % des recettes / dépenses de l'État

- **> 60 % des recettes** et **≈ 50 % des dépenses** (≈2017-2018) — Banque mondiale, PER 2020 :
  « *The government wage bill in Tunisia is among the highest in the world, taking up more
  than 60 percent of government revenues and 50 percent of expenditures, thereby crowding
  out needed investment and social spending.* »

### C. Périmètre du « wage bill » Banque mondiale (point décisif pour la section)

L'agrégat BM (PER 2020) **couvre l'administration centrale et régionale mais exclut** :
- collectivités locales : ≈ **30 000** agents ;
- entreprises publiques : ≈ **190 000** agents.

→ Illustration directe de l'écart fonction publique / emploi public / secteur public :
le 14,7 %/PIB est un périmètre administration centrale, pas le secteur public consolidé.

### D. Effectifs

| Effectif | Année | Périmètre | Source |
|---|---|---|---|
| 435 487 | 2010 | fonction publique | presse citant données officielles (à confirmer) |
| 642 918 | 2017 | fonction publique | presse citant données officielles (à confirmer) |
| ≈ 650 000 | 2021 | fonction publique | presse |
| ≈ 687 000 | 2026 | fonction publique (annonce budgétaire) | presse seule |
| + ≈30 000 (collectivités) ; +≈190 000 (entreprises publiques) | ~2017 | hors FP stricte | Banque mondiale, PER 2020 |

Hausse FP 2010→2017 : ≈ **+47 %** (≈ +207 000), cohérent avec le +4 pts de PIB.

### E. Dynamique et comparaison internationale

- Trajectoire administration centrale : ≈10,7 % (2010) → 14,7 % (2017) → 17,6 % (2020,
  effet recrutements + Covid). FMI et BM qualifient ce niveau de « among the highest in
  the world ».
- Engagement d'ajustement auprès du FMI : retour vers ≈15 % du PIB en 2022.
- Tendance récente (presse / projet de budget, **non primaire**) : 13,9 % (2024),
  14,1 % (prév. 2025), 13,4 % (prév. 2026) ; enveloppe 2026 ≈ 25 267 MDT.

## II. Références candidates (CSL-JSON) — absentes de references.json

```json
[
  {
    "id": "imf-tunisia-art4-2020",
    "type": "report",
    "title": "Tunisia: 2020 Article IV Consultation — Press Release; Staff Report; and Statement by the Executive Director for Tunisia",
    "note": "citation-key: imf-tunisia-art4-2020 | IMF Country Report, publié février 2021. Source du 17,6 % du PIB (2020) et de « among the highest in the world ». Numéro (probable CR 21/44) à confirmer sur le PDF.",
    "publisher": "Fonds monétaire international",
    "publisher-place": "Washington, D.C.",
    "URL": "https://www.imf.org/-/media/files/publications/cr/2021/english/1tunea2021001.pdf",
    "issued": { "date-parts": [[2021, 2]] }
  },
  {
    "id": "wb-tunisia-per-2020",
    "type": "report",
    "title": "Tunisia Public Expenditure Review: A New Pact for the Transition — Modernizing the State for Better and Fairer Public Spending (Overview Report)",
    "note": "citation-key: wb-tunisia-per-2020 | Source des 14,7 % du PIB (2017), +4 pts depuis 2010, >60 % des recettes / 50 % des dépenses, et du périmètre (exclut ~30 000 collectivités et ~190 000 entreprises publiques).",
    "publisher": "Banque mondiale",
    "publisher-place": "Washington, D.C.",
    "URL": "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/225051591252911165",
    "issued": { "date-parts": [[2020]] }
  }
]
```

## III. Lacunes (TODO de vérification)

1. **Texte intégral non lu** (WebFetch/curl bloqués) → confirmer tous les chiffres sur les PDF FMI/BM.
2. **Numéro exact du rapport FMI** : probablement *IMF Country Report No. 21/44* (à confirmer ; ne pas confondre avec CR 20/103).
3. **Réconcilier 17,6 % vs 16 % (2020)** et **14,1 % vs 14,7 % (2016/2017)** : écarts de périmètre (FP vs administration centrale) ou réalisé vs prévision — trancher sur source, ne pas moyenner.
4. **Effectifs** (435 487 / 642 918) : ancrer sur un document primaire (Présidence du gouvernement / ministère des Finances / INS).
5. **Source primaire tunisienne en dinars et % du budget** (« Résultats de l'exécution du budget » du ministère des Finances) non localisée — source FR à privilégier.
6. **Comparaison internationale chiffrée** absente (seulement la formule qualitative) — extraire un classement du PER 2020 / Article IV.
7. **Secteur public consolidé** : aucun agrégat masse salariale incluant entreprises publiques + collectivités + sécurité sociale trouvé ; seul l'agrégat administration centrale est documenté.

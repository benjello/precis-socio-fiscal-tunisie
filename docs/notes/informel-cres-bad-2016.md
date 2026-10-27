# Note documentaire : l'étude CRES-BAD de 2016 sur la protection sociale et l'économie informelle

Étude retrouvée le 27 octobre 2026 sur le site du CRES. Archivée dans `tunisia-data`
(`data/raw/caisses/cres/cres_bad_2016_protection_sociale_economie_informelle.pdf`, 94 pages,
couche texte native, SHA-256 `cf8ded41a04d37e0d1014777d1318af9468f0d99a38f3aac1201120a02443161`) ;
fiche de provenance : `tunisia-data/sources/cres-bad-2016-protection-sociale-informel.md`.

## Ce que c'est

- Titre : *Protection sociale et économie informelle en Tunisie : défis de la transition vers
  l'économie formelle*, CRES et Banque africaine de développement, mai 2016.
- Auteurs : Jacques Charmes (IRD, consultant) et Nidhal Ben Cheikh (CRES), sous la supervision de la
  BAD. Lancement le 23 mai 2016.
- URL : http://www.cres.tn/uploads/tx_wdbiblio/Secteur_informel_Tunisie.pdf
- Plan : 2. déploiement de la protection sociale (p. 22) ; 3. analyse exploratoire de l'économie
  informelle, concepts et mesures (p. 34) ; 4. l'emploi informel de 2005 à 2015 (p. 54) ; 5.
  conclusions et recommandations (p. 73) ; annexes 1 à 4 (p. 76-86).

## Ce que le précis peut en tirer

- **Définition** : emploi informel mesuré par l'absence de cotisation à la sécurité sociale
  (définition internationale de 2003) ; l'avertissement (p. 9) distingue emploi dans le secteur
  informel, emploi informel et économie illégale. À rapprocher de la résolution de la CIST de 2023
  citée au volume du marché du travail (`oit-cist21-2023-informel`).
- **Série** : tableau 12, p. 64, emploi informel total, salarié et non salarié, 2005-2015 (1 001 355
  en 2005, 34 % ; 1 092 640 en 2015, 32 %, provisoire). Le texte (p. 61) donne 32,2 % et 1 092 000.
  Source du tableau : calculs de N. Ben Cheikh d'après le DWH du CRES et les enquêtes emploi de
  l'INS.
- **Couverture** : tableau 15 (taux de couverture sociale effective 2005-2015) ; tableau 16 (manque à
  gagner de la CNSS en 2014 selon des scénarios de formalisation).
- **Désaccord à documenter** : Ben Cheikh et Moisseron (2021) estiment l'emploi informel à 25,2 % ;
  la Banque mondiale (2020) à 45 %. Définition, enquête et année à comparer avant de les mettre côte
  à côte.

## Référence candidate (CSL-JSON)

```json
{
  "id": "charmes-bencheikh2016-informel",
  "type": "report",
  "title": "Protection sociale et économie informelle en Tunisie : défis de la transition vers l'économie formelle",
  "title-short": "Protection sociale et économie informelle en Tunisie",
  "author": [
    {"family": "Charmes", "given": "Jacques"},
    {"family": "Ben Cheikh", "given": "Nidhal"}
  ],
  "publisher": "Centre de recherches et d'études sociales (CRES) ; Banque africaine de développement",
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2016, 5]]},
  "number-of-pages": "94",
  "URL": "http://www.cres.tn/uploads/tx_wdbiblio/Secteur_informel_Tunisie.pdf",
  "accessed": {"date-parts": [[2026, 10, 27]]},
  "language": "fr",
  "note": "citation-key: charmes-bencheikh2016-informel\nTableau 12 p. 64 (emploi informel 2005-2015) ; définition p. 9 ; copie archivée dans tunisia-data (data/raw/caisses/cres/, SHA-256 cf8ded41a04d37e0d1014777d1318af9468f0d99a38f3aac1201120a02443161). Chiffres de 2015 provisoires."
}
```

À verser dans Zotero avant toute citation dans un chapitre (la clé ci-dessus est celle de
`references.json`).

## À faire

- Lire à l'image le tableau 12 et les tableaux 15 et 16 avant tout versement en série.
- Corriger la mention « CRES, étude sur le secteur informel, 2016 » du chapitre des prestations non
  contributives (`_non_contributives.qmd`, liste des études) : l'étude est maintenant en main ; la
  référence sera `charmes-bencheikh2016-informel`.
- Demander à N. Ben Cheikh son document interne CRES de 2014, cité en source d'un tableau de l'étude, sur la couverture sociale par régime (voir
  message du 27/10/2026).

# Bourse nationale : montants 1982 et seuils de revenu 1986-2005, lecture de l'édition arabe du JORT

*documentaliste — 2026-11-10 — chantier densification « L'éducation et la formation »*

Objet : solder deux fiches RECHERCHE (`docs/recherches.yml`) par l'édition **arabe** du JORT,
jamais lue jusqu'ici pour ces deux objets :
- `r-bourse-montants-1982` — arrêté du 20 août 1982 fixant les montants mensuels de la bourse
  nationale d'études supérieures (1er et 2e cycles) et de la bourse de spécialisation ;
- `r-bourse-seuils-revenu-1986-2005` — seuils annuels de revenu des parents pour la bourse
  nationale et le prêt universitaire (décret n° 86-688 art. 4 ; arrêté du 28 juillet 1986 art. 3).

## Méthode d'océrisation

- Corpus local `PDFs/JORT/<année>/ar/` (édition arabe), nommage `Ja<NNN><aa>.pdf` (et `Ja<NNN><aaaa>.pdf`
  à partir de ~2000).
- Rendu `pdftoppm -r 120` des pages de **sommaire** (pages 1 à 3 de chaque fascicule), OCR
  `tesseract -l ara --psm 6` avec `OMP_THREAD_LIMIT=1` (≈ 4 s/page), parallélisé 8 voies.
- Texte OCR mis en cache puis criblé pour : `منح`, `منحة`, `المنح`, `المنحة الوطنية`,
  `المنح القومية`, `التعليم العالي`, `دخل`, `مداخيل`, `سقف`, `القرض الجامعي`.
- **Valeurs chiffrées et visas lus à l'image** (pas sur l'OCR, qui abîme les chiffres).

## Fascicules océrisés

| Lot | Fascicules arabes | Pages OCR |
|---|---|---|
| 1982 après le 20 août | n° 56 à 84 (29 fasc.) | sommaires p. 1-3 |
| 1983 | n° 1 à 86 (86 fasc.) | sommaires p. 1-3 |
| 1984 | n° 1 à 79 (79 fasc.) | sommaires p. 1-3 |
| 1985 | n° 1 à 91 (91 fasc.) | sommaires p. 1-3 |
| 1986 | n° 1 à 78 (78 fasc.) | sommaires p. 1-3 ; **n° 44 pages 1-24** (arrêté du 28 juillet 1986) |
| 1987 | n° 1 à 91 (91 fasc.) | sommaires p. 1-3 |
| Témoins « rentrée » 1988 | n° 55 à 69 | sommaires p. 1-3 |
| Témoins « rentrée » 1993 | n° 61 à 78 | sommaires p. 1-3 |
| Témoins « rentrée » 1999 | n° 66 à 83 | sommaires p. 1-3 |
| Témoins « rentrée » 2004 | n° 66 à 83 | sommaires p. 1-3 |
| 1990 (vérification seuil) | n° 55 pages 1-56 (partiel), **p. 1169 lue à l'image** | arrêté du 21 août 1990 |

Total : 454 fascicules 1982-1987 + 69 fascicules « rentrée » témoins + vérifications ciblées.

## Faits sourcés

### 1. Arrêté du 20 août 1982 (montants) — introuvable au JORT, mais titre arabe reconstitué

- **Aucun** arrêté fixant les montants mensuels de la bourse nationale ne paraît dans l'édition
  arabe de 1982 (n° 56-84, après le 20 août) ni de 1983 à 1987. Toutes les occurrences de `منحة`
  dans ces sommaires sont des **indemnités de fonction** : `منحة التكاليف البيداغوجية` (indemnité
  pédagogique), `منحة كيلومترية` (indemnité kilométrique), `منحة القضاء` (indemnité judiciaire),
  `منحة المركز` (indemnité de poste), `منحة السكن` (indemnité de logement), etc. — jamais une
  bourse d'études. *(Source : OCR des sommaires, édition arabe, corpus local.)*
- L'édition française postérieure au 20 août 1982 avait déjà été couverte (passes des 17 et
  29 octobre 2026) ; l'arabe 1982-1987 l'est désormais. **L'arrêté du 20 août 1982 n'a pas paru
  au JORT** (ni fr ni ar) sur la période — il n'a vraisemblablement jamais été publié au Journal
  officiel.
- **Nouveau** : son titre arabe exact est reconstitué par un visa de l'arrêté du 23 août 1990
  (JORT n° 55 de 1990, p. 1169, lu à l'image) :
  « القرار المؤرخ في 20 اوت 1982 المتعلق بضبط المقادير الشهرية للمنحة القومية للدراسات العليا
  للمرحلة الاولى والثانية والمنحة القومية للتخصص » — soit « arrêté du 20 août 1982 relatif à la
  fixation des **montants mensuels de la bourse nationale d'études supérieures des 1er et 2e
  cycles et de la bourse nationale de spécialisation** ». Ce visa confirme l'existence de l'acte
  mais ne livre ni son contenu ni son lieu de publication.

### 2. Arrêté du 28 juillet 1986 (mécanisme du seuil) — lu à l'image

- **قرار من وزير التعليم العالي والبحث العلمي مؤرخ في 28 جويلية 1986 يتعلق بضبط تراتيب اسناد
  المنح القومية للدراسات العليا والقروض الجامعية**, JORT **n° 44 de 1986, p. 869** (publié
  8-12 août 1986), lu à l'image (fascicule arabe `Ja04486.pdf`, pages 13-14).
- **Art. 3 (الفصل 3)** : la bourse nationale (1er et 2e cycles) et le prêt universitaire ne sont
  accordés que si le **revenu annuel net imposable des parents** ne dépasse pas « مقدارا يحدد
  سنويا بقرار من وزير التعليم العالي والبحث العلمي » — **un montant fixé chaque année par arrêté
  (قرار) du ministre** —, après abattement des charges sociales fixées à **100 D par enfant à
  charge non étudiant**, et pour les enfants étudiants ne bénéficiant ni d'une bourse ni d'une
  réduction d'impôt : **200 D pour le 1er enfant étudiant, 300 D pour le 2e, 400 D pour le 3e**.
- **Art. 4** : bourse/prêt accordés pour **dix mois**, prorogeables à 11 ou 12 mois sur arrêté.
- **Art. 5** : prorogation possible pour les étudiants appelés à des stages obligatoires non
  rémunérés intégrés au cursus.
- Conséquence : le seuil annuel est bien un **arrêté (قرار)** — qui devrait donc paraître au JORT,
  et non une simple « décision » interne.

### 3. Seuils annuels 1986-2005 — un seul publié au JORT : 1990-1991

- Index `jort_cache` 1988-2005, titres français **et** arabes (`bourse`, `المنح`, `دخل`,
  `مداخيل`, `سقف`, `revenus annuels`, `seuil`, `plafond`) : **un seul** arrêté de seuil de revenu
  des parents pour la bourse/le prêt sur toute la période — celui de 1990-1991.
- Sommaires arabes des fascicules de rentrée (15 août-15 octobre) des années témoins **1988, 1993,
  1999 et 2004** : **aucun** arrêté de seuil ni de montants de bourse nationale. Les occurrences de
  `دخل` y sont toutes `الضريبة على دخل` (impôt sur le revenu), `تدخل` (intervention) ou `مدخل`
  (entrée) — aucun seuil de bourse.
- **Donnée positive lue à l'image** — seuil 1990-1991 :
  **قرار من وزير التربية والتعليم العالي والبحث العلمي مؤرخ في 21 اوت 1990 يتعلق بضبط مقدار
  المداخيل السنوية لاولياء المترشحين للحصول على منحة قومية او قرض جامعي بعنوان السنة الجامعية
  1990-1991**, JORT **n° 55 de 1990, p. 1169** (publié 28-31 août 1990), **fascicule arabe
  `Ja05590.pdf`, p. 1169 lue à l'image**. Article unique :
  - **1 450 D** (« ألف وأربعمائة وخمسون دينارا », écrit `1.450`) pour la **bourse nationale**
    (المنحة القومية) ;
  - **4 200 D** (écrit `4.200`) pour le **prêt universitaire** (القرض الجامعي) ;
  - ces montants s'entendent du revenu annuel net imposable des parents, **après les abattements
    de l'art. 3 de l'arrêté du 28 juillet 1986**. Daté du 21 août 1990.
- Conclusion : hormis **1990-1991**, les seuils annuels 1986-87 à 2004-05 **ne paraissent pas au
  JORT**. En pratique le ministère a fixé ces seuils par des décisions non publiées au Journal
  officiel — à chercher **hors JORT** (rapports annuels et guides du ministère de l'Enseignement
  supérieur, offices des œuvres universitaires), comme l'oriente le `a_faire` de la fiche.

## Références candidates

Entrée CSL-JSON à créer (donnée nouvelle, utile au tableau des seuils du chapitre) :

```json
{
  "id": "arrete-1990-08-21-seuil-revenus-bourse",
  "citation-key": "arrete-1990-08-21-seuil-revenus-bourse",
  "type": "legislation",
  "title": "Arrêté du ministre de l'éducation, de l'enseignement supérieur et de la recherche scientifique du 21 août 1990 fixant le seuil des revenus annuels des parents des candidats pour l'obtention d'une bourse nationale ou d'un prêt universitaire au titre de l'année universitaire 1990-1991",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "55",
  "page": "1169",
  "issued": {"date-parts": [[1990, 8, 21]]},
  "jurisdiction": "Tunisie",
  "language": "ar",
  "note": "Publié au JORT n° 55 des 28-31 août 1990. Article unique : seuil de revenu annuel net imposable des parents fixé à 1 450 D pour la bourse nationale et 4 200 D pour le prêt universitaire, après abattements de l'art. 3 de l'arrêté du 28 juillet 1986. Lu à l'image, édition arabe (fascicule Ja05590.pdf, p. 1169)."
}
```

Références déjà présumées présentes au corpus (confirmées / précisées ici) :
- **Arrêté du 28 juillet 1986** (`المنح القومية للدراسات العليا والقروض الجامعية`), JORT n° 44 de
  1986, p. 869 — mécanisme du seuil (art. 3) et durée (art. 4) relus à l'image.
- **Arrêté du 20 août 1982** (montants mensuels) — titre arabe reconstitué par visa ; **texte
  toujours introuvable**, donc pas d'entrée exploitable.

## Notions à glossaire

*(Pas de modification de `precis/glossaire.yml` — réservé à un autre chantier.)* Pour mémoire, les
notions déjà présentes et confirmées : **bourse nationale** (`المنحة القومية` / `المنحة الوطنية`),
**prêt universitaire** (`القرض الجامعي`), **bourse de spécialisation** (`المنحة القومية للتخصص`),
**seuil de revenu des parents** (`مقدار المداخيل السنوية الصافية الخاضعة للضريبة لاولياء المترشحين`).

## Lacunes et reports

- **Arrêté du 20 août 1982** : introuvable au JORT (fr et ar, 1982-1990). Son contenu (montants
  mensuels 1982) reste **non sourcé**. Pistes non suivies : archives du ministère de
  l'Enseignement supérieur / des œuvres universitaires ; rapports de planification de l'époque.
- **Seuils annuels 1986-87 à 2004-05** (hors 1990-1991) : non publiés au JORT. À chercher hors
  Journal officiel (rapports/guides ministériels, offices des œuvres universitaires).
- OCR **exhaustif** 1988-2005 non fait (spot-check 4 années + index `jort_cache` complet) : le
  risque d'un seuil publié dans un fascicule non échantillonné est faible (l'index `jort_cache`
  couvre toute la période), mais non nul.
- Édition **française** 1983-1987 non relue page à page (jort_cache seulement) ; l'arabe 1983-1987
  étant négatif, cette relecture n'est pas prioritaire.

## Recherches infructueuses — passes consignées ce jour

- `r-bourse-montants-1982` : passe du 2026-11-10, résultat **aucun**, couvert jusqu'au 1987-12-31
  (édition arabe 1982 n° 56-84 et 1983-1987 en entier).
- `r-bourse-seuils-revenu-1986-2005` : passe du 2026-11-10, résultat **aucun**, couvert jusqu'au
  2006-01-17 (index jort_cache fr+ar 1988-2005 ; témoins arabes 1988/1993/1999/2004 ; mécanisme
  de l'arrêté de 1986 lu à l'image ; seul seuil JORT = 1990-1991, dont la valeur est désormais
  relevée).

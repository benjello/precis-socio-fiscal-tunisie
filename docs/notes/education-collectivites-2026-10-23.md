# Éducation : la dépense des communes (Q8), note documentaire du 23 octobre 2026

Question Q8 du plan (`education-plan-2026-10-17.md`) : les budgets des communes et des conseils
régionaux isolent-ils une dépense d'éducation ? Fiche `r-educ-collectivites-depense-education`.
Plan du chapitre inchangé : une section s'ajoute au chapitre de la dépense, pas de nouveau chapitre.

## 1. Textes lus

- **Décret gouvernemental n° 2020-52 du 23 janvier 2020**, modèle annexé de la nomenclature
  budgétaire des communes. JORT n° 9 du 31 janvier 2020, édition arabe, couche texte du PDF local
  (`PDFs-legislation-tunisie/PDFs/JORT/2020/ar/Ja0092020.pdf`), pp. 368 à 397 ; pp. 392 et 393
  vérifiées sur l'image. Pagination : p. 368 = page 8 du PDF, d'où la correspondance
  page imprimée = page du fichier + 360.
- **Décret gouvernemental n° 2020-439 du 14 juillet 2020**, JORT n° 71 du 22 juillet 2020,
  édition française pp. 1575-1576 : il remplace seulement les lignes de la quatrième partie du
  titre II (remboursement du principal de la dette). Aucune rubrique d'éducation.

## 2. Ce que la nomenclature de 2020 isole (édition arabe du modèle)

Dépenses de gestion, troisième rubrique (القسم الثالث) « interventions publiques » :

| Article | Intitulé arabe | Paragraphes | Page |
|---|---|---|---|
| 03.303 | تدخلات في ميدان التعليم والتكوين | 4 : contribution au Centre de formation et d'appui à la décentralisation ; 20 : transport des élèves pauvres ; 21 : prix scolaires ; 99 : autres interventions | 393 |
| 03.304 | المساهمة لفائدة الودادية بعنوان خدمة تذاكر الأكل | aucun | 393 |
| 03.305 | تدخلات في ميادين الثقافة والشباب والطفولة | 2 livre et lecture ; 3 théâtre ; 5 musique ; 6 manifestations ; 10 jeunes ; 11 enfance ; 12 associations sportives ; 99 autres | 393-394 |

L'article 03.304 est la contribution de la commune à l'amicale (association) pour un service de
tickets-repas. Le modèle n'en nomme pas les bénéficiaires : il n'est pas classé dans l'éducation.

Recettes : article 4101 « revenus des jardins d'enfants » (مداخيل رياض الأطفال), p. 376 ;
article 4201 « revenus de la concession des jardins d'enfants », p. 377.

Dépenses, titre II (développement) : aucune rubrique de construction, de grosses réparations ni
d'équipement des écoles. Les jardins d'enfants figurent comme un paragraphe de l'article de
construction des équipements collectifs de culture, de jeunesse, de sport et d'enfance
(« بناء رياض الأطفال وتهيئتها », p. 397), avec les bibliothèques, les maisons des jeunes et les
installations sportives. L'entretien des bâtiments communaux est classé dans les dépenses de gestion, deuxième rubrique
« moyens des services » (article « الاعتناء بالبنايات »), sans distinction d'usage.

## 3. Ce que les budgets publiés donnent (DGCT, données ouvertes)

Fichiers par commune, 350 communes, au niveau de l'article, **2022 et 2023 seulement**
(`tunisia-data/data/raw/finances_locales/dgct_portail/` : `Budget2022_Depenses-1.xlsx`,
`Budget2022_Recettes-1.xlsx`, `Data_Depenses_2023_10-01-2024.xlsx`,
`Data_Recettes_2023_10-01-2024.xlsx`). Les fichiers de 2018 à 2021 s'arrêtent à la section
(gestion, intérêts, développement, principal) : aucun identifiant d'article. Le niveau du
paragraphe (par exemple le 20, transport des élèves pauvres) n'est publié dans aucun fichier.
2022 est une exécution définitive ; 2023 une situation provisoire au 10 janvier 2024
(fiche `finances-locales-communes.md` de `tunisia-data`).

Contrôle fait : sur 5 330 réalisations non nulles de 2022, 152 ont la même valeur (au millime)
et la même commune qu'en 2020, des montants fixes (indemnités, annuités) ; la série de 2022 n'est
pas une copie de 2020. Les dépenses du titre I recalculées (1 145,1 MD en 2022, 1 082,1 MD en 2023)
égalent celles que donne le chapitre « Budgets et comptes » du livre des finances locales.

| Grandeur | 2022 | 2023, provisoire |
|---|---:|---:|
| Article 3303 (dépenses), prévision définitive, MD | 2,46 | 2,45 |
| Article 3303, réalisation, MD | 1,015 | 0,639 |
| Communes dont la réalisation est positive | 160 | 101 |
| Article 3303, part des dépenses du titre I | 0,09 % | 0,06 % |
| Article 4101 (recettes des jardins d'enfants), réalisation, MD | 1,102 | 1,130 |
| Communes dont la réalisation est positive (4101) | 29 | 29 |
| Article 4201 (concession), réalisation, MD | 0,006 | 0,006 |

L'article 3303 mêle le paragraphe 4 (formation des agents locaux, qui n'est pas de l'éducation) et
les paragraphes 20, 21 et 99 : sa réalisation est un majorant de la dépense d'éducation des
communes qu'il porte. L'article 3304 (13,8 MD en 2022, 13,1 MD en 2023, tickets-repas) est exclu.

## 4. Autres textes

- Code des collectivités locales (loi organique n° 2018-29), art. 243 (compétences partagées :
  entretien des écoles de base) et 244 : déjà cités dans le chapitre, voir le livre des finances
  locales, `_competences.qmd`.
- Loi n° 58-118, art. 30 : dépenses obligatoires des communes pour l'enseignement, déjà cité.

## 5. Lacunes (TODO, rien dans le texte rendu)

- Nomenclature des budgets des conseils régionaux (arrêté du 31 mars 2008, modèle des conseils
  régionaux) : non lue. Les conseils régionaux n'ont pas de budget par article dans les fichiers
  de la DGCT lus.
- Nomenclature communale antérieure à 2020 (loi n° 75-35, arrêté du 6 novembre 1975, arrêté du
  31 mars 2008) : non lue ; savoir si les articles 3303 et 4101 existaient avant 2020.
- Article-level 2018-2021 : non publié ; reconstitution par rang de ligne non tentée.
- Les 57 séries de dépense et ces séries par article doivent entrer au catalogue de
  `tunisia-data` (processed) : l'étape revient au dépôt de données.
- Dépense des communes pour les écoles (entretien courant, petites réparations) : rangée sous
  l'article des bâtiments communaux ; aucune source publiée ne la sépare.

## 6. Références candidates

Déjà présentes dans `precis/fr/finances_locales/references.json`, à copier dans le volume :
`decret-gouv2020-52` et `dgct-donnees-ouvertes`. À créer : `decret-gouv2020-439`
(URL FR : `https://www.pist.tn/jort/2020/2020F/Jo0712020.pdf`, champ `pdf_fr` de la notice 147652).
Dans le fonds commun : `loi-org-2018-29-ccl`. Le volume est en français seul : pas de
`precis/ar/education/references.json`.

## 7. Notions à glossaire

« Nomenclature budgétaire » (AR : تبويب الميزانية, intitulé du décret n° 2020-52, édition arabe).
Termes déjà au glossaire : `interventions-publiques`, `competences-partagees`, `jardin-d-enfants`,
`depenses-de-gestion`.

## 8. Recherche

Fiche `r-educ-collectivites-depense-education` : passe du 2026-10-23 (lecture des deux décrets et
des fichiers de la DGCT) ; reste ouverte pour la nomenclature des conseils régionaux, la
nomenclature communale antérieure à 2020 et le plein texte.

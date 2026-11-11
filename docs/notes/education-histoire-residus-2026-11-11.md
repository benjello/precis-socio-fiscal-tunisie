# Éducation — résidus documentaires de l'histoire (2026-11-11)

Documentaliste. Cinq lookups indépendants soldés sur l'édition arabe du JORT (corpus
local `PDFs/JORT/<année>/ar|fr/`, OCR tesseract ara/fra + relecture à l'image) et
`jort_cache.db` (indexé jusqu'au 29 octobre 2026). Aucun `.qmd`, `glossaire.yml` ni
backlog modifié. Deux fiches `docs/recherches.yml` ouvertes, une passe ajoutée.

> **Garde-fou terminologue.** Les termes arabes ci-dessous sont lus **à l'image** sur le
> texte officiel. Trois des six candidats du glossaire sont **à corriger** (recteur, IPST,
> homologation) ; trois sont **confirmés** (DUT, cycles, contrat de formation et de
> recherche). Le terminologue promeut (`statut: provisoire → valide`) ou corrige.

---

## Lookup 1 — Six termes arabes de glossaire

Bloc « terme → arabe confirmé (source) / à corriger (motif) » pour le terminologue :

| id glossaire | FR | candidat actuel | arabe attesté | source (vue à l'image) | verdict |
|---|---|---|---|---|---|
| `recteur-universite` | Recteur d'université | مدير الجامعة | **رئيس الجامعة** | décret 60-98, titre II et art. 3 (JORT 1960 n° 16 ar, p. 426-429) ; loi 86-80 art. 5 et 10 (JORT 1986 n° 44 ar) | **À CORRIGER** |
| `diplome-universitaire-technologie` | DUT | الشهادة الجامعية للتكنولوجيا | **الشهادة الجامعية للتكنولوجيا** | décret 2004-2722, titre + art. 3 (JORT 2004 n° 104 ar, p. 3421-3423) | **CONFIRMÉ** |
| `cycles-court-moyen-long` | Cycles court/moyen/long | المراحل القصيرة والمتوسّطة والطويلة | **ثلاث مراحل للتكوين : قصيرة ومتوسّطة وطويلة** | loi 76-65, art. 7 (JORT 1976 n° 46 ar, p. 1644-1645) | **CONFIRMÉ** |
| `contrat-formation-recherche` | Contrat de formation et de recherche | عقد التكوين والبحث | **عقود تكوين وبحث / عقود التكوين والبحث** | loi 2000-67, art. 5 et 6 nouveaux (JORT 2000 n° 57 ar, p. 1739-1741) | **CONFIRMÉ** |
| `ipst` | Institut de promotion supérieure du travail | معهد النهوض بالعمل | **معهد الترقية العليا للشغل** (plur. معاهد الترقية العليا للشغل) | loi 93-12, art. 3 (JORT 1993 n° 14 ar, p. 257) | **À CORRIGER** |
| `homologation-certificats-diplomes` | Homologation des certificats et diplômes | المصادقة على الشهائد والدبلومات | **التنظير** (الباب الثالث : تنظير شهائد ومؤهّلات التكوين المهني) | décret 94-1397, chap. III, art. 4-10 (JORT 1994 n° 52 ar, p. 1142-1143) ; confirmé repris par décret 2009-2139 (JORT 2009 n° 57 ar) | **À CORRIGER** |

Détails et citations exactes :

- **Recteur → رئيس الجامعة.** Le candidat *مدير الجامعة* n'est **pas attesté**. Décret
  60-98 (1960), titre II : « العنوان الثاني — رئيس الجامعة ونائبه والكاتب العام للجامعة »,
  art. 3 « يدير الجامعة التونسية رئيس يقع تعيينه بمقتضى أمر » ; côté FR, chapitre « Du
  Recteur », art. 3-10 (« Chaque université est dirigée par un recteur »). Loi 86-80
  (1986) art. 5 FR « Chaque université est dirigée par un recteur » = ar « يدير كل جامعة
  رئيس… », art. 10 « يمثّل رئيس الجامعة… الجامعة » (« Le recteur, assisté des doyens… »).
  **Alerte de concordance** : l'arabe emploie رئيس الجامعة de 1960 à aujourd'hui, pour le
  « recteur » (1960-2000) **comme** pour le « président d'université » (loi 2000-67,
  entrée `president-universite`, déjà `valide` avec رئيس الجامعة). La distinction
  recteur/président n'existe **qu'en français** : en arabe il n'y a pas de terme
  distinct. Le terminologue doit soit garder رئيس الجامعة pour les deux (avec note de
  désambiguïsation FR), soit laisser `recteur-universite` sans forme arabe propre. Le
  candidat مدير الجامعة est à retirer.
- **DUT → الشهادة الجامعية للتكنولوجيا.** Décret 2004-2722, titre I « في الإطار العام
  لنظام الدراسة في الشهادة الجامعية للتكنولوجيا », art. 3 « تُمنح الشهادة الجامعية
  للتكنولوجيا من قبل مؤسسات… ». Conforme au candidat. **Prêt à passer `valide`.**
- **Cycles court/moyen/long → مراحل التكوين القصيرة/المتوسّطة/الطويلة.** Loi 76-65 art. 7
  « يمكن أن يشتمل التعليم العالي على ثلاث مراحل للتكوين : قصيرة ومتوسّطة وطويلة حسب غاية
  كلّ شعبة وأهدافها مع إمكانية الارتقاء من مرحلة إلى أخرى ». Conforme au candidat
  (مراحل = cycles, قصيرة/متوسّطة/طويلة = court/moyen/long). **Prêt à passer `valide`.**
- **Contrat de formation et de recherche → عقد التكوين والبحث.** Loi 2000-67 art. 5
  nouveau « …موضوع عقود تكوين وبحث تُبرَم بين الدولة من جهة والجامعات من جهة أخرى », forme
  définie عقود التكوين والبحث à l'art. 6 nouveau et au tableau des ressources. Conforme
  au candidat. **Prêt à passer `valide`.** (La loi 2008-19 reprend le dispositif ; non
  réouverte, la forme 2000 fait foi.)
- **IPST → معهد الترقية العليا للشغل.** Le candidat *معهد النهوض بالعمل* n'est **pas
  attesté**. Loi 93-12 art. 3 : « يتمّ التكوين خاصة داخل مؤسسات فرعية تابعة لهذا المركز
  أُطلق عليها اسم "معاهد الترقية العليا للشغل" ويُضبط تنظيمها وسيرها بمقتضى أمر. »
  (« promotion supérieure du travail » = الترقية العليا للشغل). À corriger. NB : l'entrée
  voisine `cnfcpp` (statut `valide`) contient elle aussi « في معاهد النهوض بالعمل » dans
  sa définition arabe — **à revoir** par le terminologue pour cohérence.
- **Homologation → التنظير.** Le candidat *المصادقة على الشهائد والدبلومات* n'est **pas
  attesté**. Décret 94-1397, « الباب الثالث — تنظير شهائد ومؤهّلات التكوين المهني »,
  art. 4 « توجَّه مطالب تنظير شهائد ومؤهّلات التكوين المهني… », art. 6 « يُصدر الوزير…
  قرارات التنظير… وذلك لمدة خمس سنوات » (les « cinq ans » de la définition FR). Le terme
  التنظير est repris tel quel par le décret 2009-2139 (visa : « …شروط تنظير شهائد
  ومؤهّلات التكوين المهني »). À corriger. La racine « homologation = تنظير » est propre à
  la formation professionnelle tunisienne (≠ معادلة « équivalence », ≠ مصادقة
  « approbation »).

---

## Lookup 2 — Prorogation de l'unité de gestion par objectifs (décret 2016-1100) : **TRANCHÉ**

Le texte qui proroge l'unité de la réforme de l'enseignement supérieur est le
**décret n° 2023-12 du 23 janvier 2023** (أمر عدد 12 لسنة 2023 مؤرخ في 23 جانفي 2023),
**JORT n° 9 du 27 janvier 2023, p. 250**, « portant prorogation du délai de l'unité de
gestion par objectifs pour l'exécution du projet de la réforme de l'enseignement supérieur
en vue de l'appui à l'employabilité des diplômés de l'enseignement supérieur ».

- **Article premier** (lu à l'image, FR) : « Les délais de réalisation des missions de
  l'unité… sont prorogés **du 2 septembre 2022 jusqu'au 31 décembre 2024** », en deux
  étapes : étape d'exécution des activités principales prorogée jusqu'au 31 décembre 2023 ;
  étape de clôture d'un (1) an à compter de la fin de la première étape.
- Visa explicite du décret gouvernemental n° 2016-1100 du 25 août 2016 (création de l'unité).

**Le « décret 2023-12 » du ticket n'était donc pas une erreur de fond** : il existe bien un
décret n° 2023-12 qui proroge l'unité. La confusion vient de l'**homonymie de numéro** : il
y a DEUX textes « 2023-12 » — ce décret (23 janvier 2023) ET la **loi n° 2023-12 du
23 novembre 2023, loi de finances rectificative pour 2023** (JORT 2023 n° 136, p. 3128).
Citer « décret n° 2023-12 du 23 janvier 2023 » (jamais « loi n° 2023-12 ») lève l'ambiguïté.

Candidats du ticket **écartés** (aucun ne concerne l'unité de l'enseignement supérieur) :
- **décret présidentiel n° 2022-683 du 3 août 2022** : modifie le décret gouvernemental
  n° 2016-**1151** (unité du réseau routier classé, cofinancé BAD) — autre unité.
- **décret n° 2025-200 du 15 avril 2025** (JORT 2025 n° 46, p. 924) : proroge l'unité du
  projet de soutien de l'**enseignement primaire** financé par le FADES, créée par le
  décret gouvernemental n° 2019-493 — autre unité.

**Référence candidate CSL-JSON à créer :**
```json
{
  "id": "decret2023-12-prorogation-ges",
  "citation-key": "decret2023-12",
  "type": "legislation",
  "title": "Décret n° 2023-12 du 23 janvier 2023, portant prorogation du délai de l'unité de gestion par objectifs pour l'exécution du projet de la réforme de l'enseignement supérieur en vue de l'appui à l'employabilité des diplômés de l'enseignement supérieur",
  "issued": {"date-parts": [[2023, 1, 23]]},
  "authority": "République tunisienne",
  "container-title": "Journal officiel de la République tunisienne",
  "issue": "9",
  "page": "250",
  "language": "fr"
}
```
NB : clé `decret2023-12` à ne pas confondre si une entrée existe déjà pour la loi de
finances rectificative ; employer une clé distincte (p. ex. `decret2023-12-ges`).

---

## Lookup 3 — Doublon du décret n° 60-98 (JORT n° 24, p. 693) : **TRANCHÉ**

La notice n° 24 du 13 mai 1960, p. 693, est un **rectificatif** (pas une republication, pas
un changement de date). Intitulé jort_cache : « Décret n° 60-98 du 31 Mars 1960, portant
création et organisation de l'université de Tunis (**rectificatif** au J.O.R.T. n° 16 du
31 mars 1960) ». Texte lu à l'image (JORT 1960 n° 24 fr, p. 693) :

> « Rectificatif au J.O.R.T. … du 31 mars 1960 — Page 437, 2ᵉ colonne. ARTICLE 12. Au lieu
> de : *Les trois premières catégories de membres du Conseil de l'Université forment la
> section permanente du Conseil*, lire : *Les quatre premières catégories de membres du
> Conseil de l'Université forment la section permanente du Conseil.* »

- Le rectificatif **ne touche que l'art. 12** (section permanente du conseil :
  « trois » → « quatre » premières catégories). La **date du décret reste le 31 mars 1960**.
- **Citation canonique inchangée** : JORT n° 16 du 31 mars 1960, p. 426-429 (recid 107031),
  avec mention du rectificatif (JORT n° 24 du 13 mai 1960, p. 693, recid 106960) pour l'art. 12.
- Petite discordance de pagination à signaler : le rectificatif renvoie à la « page 437 »,
  alors que `jort_cache` donne au décret les pages 426-429 ; l'art. 12 se lit en p. 437 du
  même fascicule n° 16 (l'intervalle du cache est probablement sous-estimé). Sans incidence
  sur la date.

---

## Lookup 4 — Décrets d'application de la loi n° 2008-10 : **NON IDENTIFIÉS → 2 fiches ouvertes**

Articles de la loi (JORT 2008 n° 14, p. 683-688), lus à l'image FR+AR :
- **Art. 38** : « L'organisation, les modalités de fonctionnement et le régime
  disciplinaire des établissements publics de formation professionnelle sont fixés **par
  décret** » (ar : « يُضبط تنظيم مؤسسات التكوين المهني العمومية… »).
- **Art. 55** : « Les conditions d'attribution de l'habilitation et de la classification
  aux établissements de formation professionnelle sont fixées **par arrêté** du ministre »
  (ar : « تُضبط شروط إسناد **التأهيل والتصنيف** إلى مؤسسات التكوين »). C'est bien l'arrêté
  « habilitation/classification » qui prend le relais du chap. III (« تنظير ») du décret
  94-1397 — cf. lookup 1, homologation.
- **Art. 57** : commission « nationale d'évaluation et d'assurance qualité dans la
  formation professionnelle », composition et fonctionnement fixés **par décret** (ar :
  l'instance est nommée « **الهيئة الوطنية لتقييم التكوين المهني وضمان الجودة** »).

**Recherche jort_cache (indexé au 29 octobre 2026), FTS + LIKE FR et AR : aucun des trois
textes d'application identifié.** Voisins écartés : décret n° 2013-4450 (modifie le décret
n° 2006-1545, création d'un établissement nommé) ; arrêtés « liste des établissements
publics habilités aux cycles d'adaptation professionnelle » (2009, 2011, 2013). Miroir iort
et plein texte des fascicules non parcourus.

**Fiches ouvertes dans `docs/recherches.yml`** (passe datée du 11 novembre 2026,
`couvert_jusqu_au: 2026-10-29`, `resultat: aucun`) :
- `r-educ-fp-2008-art38-etablissements-publics` (décret, art. 38) ;
- `r-educ-fp-2008-art57-commission-evaluation` (décret, art. 57).

> **À FAIRE RÉDACTEUR (handoff).** Je ne touche pas aux `.qmd` : les deux fiches sont pour
> l'instant **orphelines** (`recherches.py verifier` les signale). Le rédacteur doit poser,
> dans `precis/fr/education/_formation_professionnelle.qmd` (section `#sec-educ-fp-lois`),
> les ancres `<!-- RECHERCHE r-educ-fp-2008-art38-etablissements-publics : … -->` et
> `<!-- RECHERCHE r-educ-fp-2008-art57-commission-evaluation : … -->` pour rendre le
> registre cohérent.

**Lacune non fichée (art. 55) :** l'arrêté « habilitation et classification » (التأهيل
والتصنيف) remplaçant le chap. III du décret 94-1397 n'est pas non plus identifié ; non fiché
ici (hors des deux fiches demandées), à verser au besoin par le rédacteur (proche de la
fiche existante `r-educ-fp-cahier-charges-prive-2008`).

---

## Lookup 5 — Tutelle des kouttabs : **TOUJOURS INTROUVABLE, candidats écartés**

Les deux décrets du ticket concernent un **autre objet** (lu à l'image FR, JORT 2015 n° 4) :
- **décret n° 88-1962 du 6 décembre 1988** (JORT 1988 n° 83, p. 1706) et
- **décret n° 2014-4567 du 31 décembre 2014** (JORT 2015 n° 4, p. 93)

fixent la composition et le fonctionnement de la **« commission des livres coraniques »**
(لجنة الكتب القرآنية, contrôle des exemplaires du Coran / مصاحف), **créée par la loi
n° 88-97 du 18 août 1988** — avis des ministres de l'économie/finances et des affaires
religieuses. **Rien à voir avec la tutelle des kouttabs (écoles coraniques).** Écartés.

Aucun texte transférant la tutelle des kouttabs au ministère des affaires religieuses n'est
identifié dans `jort_cache` (FTS/LIKE : kouttab, كتاتيب, الكتاب القرآني, الكتب القرآنية, au
29 octobre 2026). L'indice contraire (arrêté 2007 « Premier ministère ») tient.
**Fiche `r-educ-kouttabs-tutelle-affaires-religieuses` : passe du 11 novembre 2026 ajoutée**
(résultat : aucun). Reste à parcourir : miroir iort et plein texte des fascicules.

---

## Références candidates (CSL-JSON)

Déjà présentes dans les `references.json` (vérifier la clé) : `decret60-98`, `loi86-80`,
`loi76-65`, `loi2000-67`, `loi2008-19`, `loi93-12`, `decret94-1397`, `decret2009-2139`,
`decret2004-2722` (toutes citées par le glossaire).

À créer :
- `decret2023-12` — décret n° 2023-12 du 23 janvier 2023 (prorogation unité ES), supra.
- (optionnel) `decret2014-4567` et `decret88-1962` — commission des livres coraniques, si
  l'on veut documenter l'écartement dans le précis ; sinon inutile (hors sujet kouttabs).

## Notions à glossaire (pour le terminologue)

Rien à créer : les six entrées existent déjà. Actions : **corriger** l'arabe de
`recteur-universite` (→ رئيس الجامعة, avec note de désambiguïsation vs `president-universite`),
`ipst` (→ معهد الترقية العليا للشغل) et `homologation-certificats-diplomes` (→ التنظير) ;
**promouvoir `valide`** `diplome-universitaire-technologie`, `cycles-court-moyen-long` et
`contrat-formation-recherche` (arabe confirmé). Revoir la définition arabe de `cnfcpp`
(contient « معاهد النهوض بالعمل », à aligner sur معاهد الترقية العليا للشغل).

## Lacunes

- Décret art. 38, décret art. 57 et arrêté art. 55 de la loi 2008-10 : non identifiés
  (fiches ouvertes pour les deux décrets ; arrêté art. 55 non fiché).
- Tutelle des kouttabs : non identifiée (fiche relancée).
- Miroir iort et plein texte des fascicules : non parcourus pour les lookups 4 et 5.

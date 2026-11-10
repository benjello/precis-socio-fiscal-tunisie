# Exécuté budgétaire par mission — extraction des RAP, lot A (collecte gbo.tn du 2026-11-10)

Ticket : construire la série de l'exécuté par mission (crédits **engagés** et **payés**, en
**milliers de dinars, أد**) à partir de la section « تنفيذ ميزانية المهمة » des rapports annuels de
performance (RAP) du lot `~/projets/tunisia-data/data/raw/gbo-recup-2026-11-10/` (98 PDF,
index `sources/gbo-recuperation-2026-11-10.csv`).

Résultat : **66 couples (mission, année de gestion)** extraits dans
`docs/notes/budget-missions-execute-lotA.csv`. Chaque ligne porte le fichier source (chemin
dans l'entrepôt tunisia-data) et la page PDF. Famille de chiffres : **budgétaire — exécution
constatée dans les RAP des ministères** (ni LF votée, ni règlement définitif de la Cour des
comptes).

## Méthode

1. `pdftotext -layout` sur les 98 PDF ; repérage de la section « تنفيذ ميزانية المهمة » (ou
   « تنفيذ ميزانية الوزارة » avant 2020) et du total mission (المجموع / المجموع العام /
   مجموع الميزانية).
2. Quand plusieurs fichiers couvrent la même gestion (versions AR/FR, rééditions), une seule
   version retenue (la plus lisible), l'autre citée en contrôle dans la note.
3. L'année de gestion vérifiée sur la page de titre : elle correspond partout à la colonne
   `annee_nom_fichier` de l'index, **sauf** `tourisme/2022-02_rap tourisme version
   francaise...pdf` (indexé 2022, en réalité gestion 2020 — non utilisé, doublon FR).
4. Trois contrôles systématiques : (a) taux imprimé ≈ réalisé/prévu et montant = prévu −
   réalisé (arithmétique interne du tableau) ; (b) plausibilité inter-annuelle par mission ;
   (c) ordre de grandeur vs la LF votée 2021-2023 (`precis/_seriescache/budget-missions-vote.csv`).

## Structures rencontrées

- **2017-2019 (ancienne nomenclature, loi organique 1967)** : exécution en **crédits de
  paiement seulement** (نفقات التصرف / التنمية / صناديق الخزينة). La colonne `engage_milliers`
  est vide pour ces années (sauf néant) — ce n'est pas une lacune d'extraction.
- **2020-2023 (LOB 2019)** : tableaux par nature et par programmes avec lignes اعتمادات
  التعهد / اعتمادات الدفع ; le total mission est généralement « hors ressources propres des
  établissements » et parfois hors subvention d'un fonds du trésor (culture : hors fonds
  7 000 أد en 2021-2022, y compris en 2020 — signalé en note).
- Libellés du total : المجموع, المجموع العام, مجموع الميزانية, مجموع المهمة, اجملموع العام
  (ligatures), Total / Total général (versions FR).
- Éducation seul porte la phrase-type « بلغت جملة الإنجازات X أد تعهدا و Y أد دفعا » (sonde du
  ticket) ; emploi-formation 2020-2023 en a une variante.

## PDF à texte corrompu (polices à cmap cassé) et traitement

Le texte extrait de plusieurs PDF rend les chiffres brouillés (runs inversés ou permutés :
« 0202 » pour 2020, « 8102 » pour 2018). Traitement : lecture du **rendu image** de la page
(pdftoppm 300 dpi) ou OCR tesseract-ara, puis validation arithmétique (somme des lignes,
écart, taux). Fichiers concernés et résolus ainsi :
- `culture/2021-03_RAP 2018 AFFAIRES CULTURELLES.pdf` (OCR p.7) ;
- `culture/2022-11_...2021 (النسخة الثالثة).pdf` (image p.8) ;
- `education/2021-03_RAP 2018 EDUCATION.pdf` (image p.6) ;
- `justice/2021-03_RAP_JUSTICE_2018.pdf` (tableaux en images ; image p.12) ;
- `affaires-sociales/2021-10_RAP 2020 affaires sociales.pdf` et
  `femme-famille/2024-07_RAP2023...pdf` : texte arabe illisible mais colonnes numériques
  arithmétiquement cohérentes — gardées telles quelles.

## Anomalies de source (incohérences internes des RAP, consignées dans le CSV)

- **Éducation 2021** : la phrase des crédits LFC diffère entre les deux versions AR
  (8 462 873 vs 6 781 643 أد de crédits de paiement) et les taux imprimés (95,75/99,88) ne
  se recalculent pas ; le **réalisé** (6 758 655 / 6 715 571) est identique dans les deux
  versions et est retenu.
- **Enseignement supérieur 2023** : p.9, le tableau 1 (par nature) porte des totaux à chiffres
  transposés (2 748 148 / 2 615 061) ; le tableau 2 (par programmes : 2 148 748 / 2 061 615)
  est cohérent avec le texte et la somme des programmes — retenu.
- **Enseignement supérieur 2020** : le fichier `2021-09_RAP 2020 MESRS.pdf` présente comme
  tableau « mission » ce qui est en fait le programme enseignement supérieur seul
  (1 320 232 / 1 203 457) ; le vrai total mission (1 999 507 / 1 789 068) vient de
  `2021-09_RAP MESRS232020.pdf` et de la version FR.
- **Jeunesse-sport** : totaux divergents entre tableau par nature et tableau par programmes en
  2018 (633 101 vs 571 796) et 2020 (engagements 942 023 vs 919 173) ; écart arithmétique de
  10 000 sur la ligne engagements 2023 ; en-têtes d'années erronés (2021, 2023). Valeurs par
  nature retenues, divergences en note.
- **Tourisme 2020** : lignes engagements = paiements au total (110 696) — engagements douteux.
  **Tourisme 2023** : nature (107 246) vs programmes (106 964, confirmé par le texte) — retenu
  programmes.
- **Présidence du gouvernement 2020** : totaux d'engagements incohérents entre tableaux
  (49 414 / 90 641) — engagements non retenus, paiements seuls (224 571,354).
- **Culture 2021** : ligne engagements du tableau source intrinsèquement incohérente (montant
  et taux ne collent pas) ; **culture 2022** : taux paiements imprimé 97,5 % ≠ calculé 95,5 %.
- **Femme-famille 2020** : texte 169 720 vs tableau 169 200.
- **Affaires religieuses 2019 (FR)** : tableau par nature embrouillé (colonne réalisations
  décalée) ; total pris au tableau par programmes (125 643).

## Contrôles (b) et (c)

- Vs LF votée 2021-2023 (`budget-missions-vote.csv`, MDT) : tous les payés sont entre 85 % et
  115 % du voté, **sauf tourisme** (65 % en 2021, 68 % en 2022, 61 % en 2023) — ce n'est pas
  une erreur d'extraction : les taux d'exécution imprimés (65,4 / 77,6 / 60,7 %) confirment la
  sous-exécution (interventions et fonds du trésor non décaissés), et **affaires sociales
  2021** (2 234,9 vs 1 955 votés) — crédits complémentaires CNRPS (+85 MDT) notés par le RAP.
- Inter-annuel : pic affaires sociales 2020 (2 677,9 contre 1 777,1 en 2019 et 2 234,9 en
  2021) = aides exceptionnelles COVID ; creux éducation 2018 (4 945,2 contre 5 162,3 en 2017
  cité par le RAP 2018 et 5 699,0 en 2019) — tel qu'imprimé ; le reste évolue sans saut > ×1,3.

## Reports / lacunes

- **Couples absents du lot A** (aucun RAP collecté, pas un échec d'extraction) :
  affaires-étrangères 2017 et **2021** ; affaires-religieuses **2020** et **2022** ;
  affaires-sociales 2017, 2018, **2022**, **2023** ; culture 2017 et **2023** ; éducation
  2017 ; enseignement-supérieur 2017 ; femme-famille 2017, 2018 ; jeunesse-sport 2017 ;
  justice 2016 et antérieurs ; présidence-gouvernement 2017-2019 ; tourisme 2017 ; finances :
  seul 2020 présent. → à chercher lors d'une prochaine passe de collecte gbo.tn/ministères
  (certains existent peut-être sur les sites ministériels ou dans les projets annuels de
  performance joints aux PLF).
- **Engagements non disponibles** avant la gestion 2020 (nomenclature) et non retenus pour
  présidence-gouvernement 2020 (source incohérente) ; tourisme 2020 douteux.
- Taux imprimés non recalculables pour éducation 2021 (voir anomalies).
- Les deux fichiers en échec HTTP 404 de l'index de collecte ne concernent pas ce lot
  (statut `echec` dans `sources/gbo-recuperation-2026-11-10.csv`).

*Extraction du 2026-11-10 (documentaliste). Outils : pdftotext -layout, pdftoppm + lecture
d'image, tesseract (ara), scripts jetables (non conservés) ; aucune valeur sans source
fichier + page.*

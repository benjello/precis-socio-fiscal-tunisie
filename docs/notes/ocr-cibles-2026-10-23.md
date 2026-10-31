# OCR ciblé du 23 octobre 2026 : quatre cibles du point 2 du backlog

Procédure : repérage par `jort_cache.db` (fascicule, pages imprimées), calage de la page
imprimée sur la page du PDF par OCR à 100 dpi de quelques pages, puis OCR à 300 dpi
(`tesseract -l fra --psm 4`, au premier plan, une page à la fois) des seules pages utiles ;
contrôle par rendu PNG de la page et lecture de l'image. Aucun processus laissé en fin de tâche.

Rangement du texte extrait : `~/projets/tunisia-data/data/raw/jort-ocr/` (hors git : non ajouté
au dépôt `tunisia-data`, fichiers non suivis). Un fichier `.txt` par cible, un marqueur
`=== PDF page N ===` par page. Corpus source : `~/projets/PDFs-legislation-tunisie/PDFs/JORT/`.

Constat général : l'OCR est utilisable pour le texte courant et pour des tableaux simples sur
fond propre ; il abîme les tableaux à filets (chiffres de l'annexe du décret de 1975 : « 42 go »
pour 4 D, 600). Toute valeur se relève à l'image.

| Cible | Fichier local | Pages utiles (imprimées / PDF) | Texte extrait |
|---|---|---|---|
| Loi n° 65-17 du 28 juin 1965 | `1965/fr/Jo03465.pdf` | p. 787 / PDF 3 (OCR de PDF 2 à 5) | `jort-1965-n32-pdf2-5_loi-65-17.txt` |
| Décret n° 75-952 du 30 décembre 1975 | `1975/fr/Jo08775.pdf` | p. 2884 / PDF 34 | `jort-1975-n87-pdf34_decret-75-952.txt` |
| Code de l'IRPP et de l'IS (loi n° 89-114), JORT n° 1 de 1990 | `1990/fr/Jo00190.pdf` | p. 3-21 / PDF 3-21 (annexe II p. 18) | `jort-1990-n01-pdf3-21_code-irpp-is.txt` |
| Code de la TVA (loi n° 88-61), JORT n° 39 de 1988 | `1988/fr/Jo03988.pdf` | p. 827-846 / PDF 7-26 (PDF = page imprimée − 820) | `jort-1988-n39-pdf7-26_code-tva.txt` |

## 1. Loi n° 65-17 (étudiants) : réussie

- Texte complet en une page (787, colonne de droite de la page, après la loi n° 65-16), dix
  articles, lu à l'image sur toute la page. L'OCR (colonnes entrelacées par moments) est
  correct sur les articles ; lecture à l'image pour tout chiffre ou citation.
- Ce que le texte permet (lu à l'image) : titre « étendant les régimes de sécurité sociale
  aux étudiants » ; art. 1 : extension des régimes de la loi n° 60-30 du 14 décembre 1960 ; art. 2 :
  assujettissement obligatoire des étudiants tunisiens inscrits dans l'enseignement supérieur
  non assurés sociaux eux-mêmes ni ayants droit, étrangers sous réserve de réciprocité ;
  art. 3 : limite d'âge de 28 ans révolus (reculée du temps passé sous les drapeaux ou
  en maladie/maternité) ; art. 4 : soins en cas de consultation ou d'hospitalisation et allocations
  familiales ; art. 5 : immatriculation à la CNSS, carte d'assuré social étudiant et carnet de
  soins familial ; art. 6 : allocations familiales de l'étudiant père de famille, 7 D, 875 par
  trimestre et par enfant, quatre premiers enfants ; art. 7 : soins pour le conjoint et les enfants ;
  art. 9 : cotisation forfaitaire fixée par décret et subvention de la CNSS ; art. 10 : compte
  spécial. Les branches couvertes se lisent donc dans la loi : soins et allocations familiales.
- Anomalie de numérotation : l'en-tête du PDF porte « N° 32 », 25-29 juin 1965 ; `jort_cache.db`
  et `todo-localisation.md` disent n° 34. À trancher avant toute citation du numéro de fascicule
  (la page 787 et la date sont, elles, établies).
- Autre notice de la base : « 65-17 », décret du 19 janvier 1965 (JORT n° 3, p. 48) : homonyme,
  sans rapport.

## 2. Décret n° 75-952 (indemnités familiales) : réussie

- Décret complet sur la page 2884 (colonne de gauche à partir du ministère « Premier Ministère »,
  colonne de droite pour l'article 2), PDF 34 ; PDF 35 (p. 2885) lu : il porte un autre décret
  (n° 75-937).
- Texte lu à l'image : art. 1 : le tableau « A » (indemnités familiales) de l'article 31 du
  décret du 30 juin 1956 est modifié ; fonctionnaires titulaires, agents temporaires et
  contractuels ; mariés sans enfant : néant ; par enfant à charge, taux mensuels : 1er enfant
  4 D, 600 ; 2e 3 D, 800 ; 3e 3 D, 300 ; 4e 2 D, 700. Art. 2 : effet au 1er janvier 1976.
  Visas : loi n° 68-12, décret du 30 juin 1956, loi de finances n° 65-46 (art. 24), décret
  n° 72-358.
- Qualité de l'OCR : mauvaise sur le tableau (valeurs illisibles), correcte sur les visas.
- Ce que le texte permet : le palier de 1976 de la série des indemnités familiales (une seule
  catégorie, quatre taux), à poser avec la date d'effet 1er janvier 1976 énoncée par le texte.

## 3. Code de l'IRPP et de l'IS de 1990, annexe II : réussie

- Pages 3 à 21 océrisées ; annexe II (impôt forfaitaire légal) en page 18, lue à l'image.
  Le texte OCR de la page 18 reprend les barèmes sans erreur sur les lignes comparées ; l'en-tête
  est lu « ANNEXE I » par l'OCR alors que l'image porte « ANNEXE II ».
- Contenu de l'annexe (image) : 1) prestations de services, chiffre d'affaires par tranches de
  1.000 D (millimes) jusqu'à 20.000 D ; impôt en dinars, deux colonnes (consommation sur
  place : 0 à 500 ; autres prestations : 0 à 600 jusqu'à 15.000) ; 2) autres opérations,
  tranches de 2.000 D jusqu'à 30.000 D ; impôt de 0 à 700. Concorde avec la note
  `docs/notes/fiscalite-regime-forfaitaire.md` (article 44 § IV en p. 9 ; annexes III en p. 19-20).
- Le texte complet des pages 3 à 21 est maintenant interrogeable (grep) ; chaque chiffre cité
  reste à relever à l'image.
- Exploité le 31 octobre 2026 dans `_impot_revenu.qmd` : annexes I (p. 17), II (p. 18) et III-1 à III-3 (p. 19-20) lues à l'image et reproduites en tableaux, article 42 (p. 8) en section `#sec-irpp-train-de-vie`.

## 4. Code de la TVA de 1988 : réussie pour le texte, annexes lues par sondage

- Pages 827 à 846 (loi n° 88-61 du 2 juin 1988, JORT n° 39 du 10 juin 1988) océrisées en
  entier : articles du code, puis tableaux A (exonérations), B (taux de 6 %, p. 836) et C
  (taux de 29 %, p. 836-837), puis listes de produits par numéros de nomenclature (suite jusqu'à
  la p. 846).
- Contrôle à l'image : p. 844 (liste de produits : numéros N.T. et désignations) lue ; l'OCR la
  restitue à quelques coupures de ligne près (« 85 - % » pour « 85 - 06 », phrases coupées).
  Les taux (6 %, 17 %, 29 %) et les articles se lisent dans le texte, à relever à l'image avant
  citation chiffrée ; les numéros de nomenclature de l'OCR ne sont pas fiables.
- Ce que le texte permet : repérer les articles et tableaux d'origine (assiette, taux de 6 %,
  17 % et 29 %, exonérations) ; la comparaison article par article avec les modificatifs reste
  à faire à l'image.
- Limite : l'OCR n'a pas créé d'annexe absente ; seules les p. 827-846 de la loi sont lues.
  Les pages 822-826 (loi n° 88-60) et 847-857 du fascicule ne sont pas océrisées.

## 5. Convention bancaire arabe de 2014

Non traitée ici : extraction par `pdftotext` puis normalisation NFKC, sans OCR (point 2 du backlog).

## Limites

- Les images lues sont les pages 3 (1965), 34 et 35 (1975), 18 (1990), 24 (1988) ; les autres
  pages ne sont contrôlées que par la qualité du texte extrait.
- Le fichier 1965 est à vérifier pour le numéro de fascicule (32 ou 34).

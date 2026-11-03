# Loi n° 2009-40 : lecture de l'édition arabe par OCR ciblé — note documentaire, 3 novembre 2026

Rôle : documentaliste. Objet : lecture, à partir de l'édition arabe du JORT, des articles 2 à 4 de la
loi n° 2009-40 (compte spécial de financement de la mise à la retraite avant l'âge légal), sans
océriser les 362 fascicules arabes de 2009 à 2012. Aucun chapitre n'est modifié.

## 1. De quel texte s'agit-il

Le « 2009-40 » a deux sens dans le dépôt. La base JORT (`jort_search`, numéro « 2009-40 ») répond :

| Texte | Ce que c'est | Publication |
|---|---|---|
| **Loi n° 2009-40 du 8 juillet 2009** | loi de finances complémentaire pour 2009. Elle ouvre, aux articles 2 à 4 de son dernier chapitre, le compte spécial qui paie les pensions des agents mis à la retraite avant l'âge légal (loi n° 2009-39) | JORT n° 55 du 10 juillet 2009 ; p. 1822-1843 (français), p. 2367-2389 (arabe) |
| Décret n° 2009-40 du 5 janvier 2009 | organigramme de la Banque de financement des petites et moyennes entreprises (BFPME) | JORT n° 5 du 16 janvier 2009 ; p. 190 (français), p. 200 (arabe) |

La demande visait la loi (c'est elle que touche l'entrée « 362 fascicules arabes » du backlog et de
`taches-legislation-par-date.md`). La ligne 4608 du backlog, elle, cite le **décret** (liste des
organigrammes de banques publiques « dans le corpus local, non lus »). Les deux sont traités ici ;
ils n'ont aucun lien entre eux.

## 2. Méthode

- Fascicule arabe : `PDFs/JORT/2009/ar/Ja0552009.pdf` (88 pages). Sa couche de texte existe mais
  est un codage de police illisible (suite de signes sans mots arabes) : elle ne sert à rien.
- Le sommaire (PDF p. 1) a été océrisé : loi n° 2009-40 à la p. 2367. Les pages 4 à 14 du PDF ont
  été océrisées pour trouver les articles (PDF p. 8 = p. 2368 imprimée ; PDF p. 14 = p. 2374).
  Soit 11 pages sur les 88 du fascicule, et 1 fascicule sur 362.
- `tesseract -l ara --psm 4`, 300 dpi. Données de langue : `ara.traineddata` déjà présent dans le
  dossier `tessdata` du corpus (rien n'a été téléchargé, rien n'est ajouté au dépôt).
- Chaque valeur citée ci-dessous a été contrôlée sur l'image de la page, pas sur l'OCR seul.

## 3. Ce que le texte apporte

**Page 2368 (arabe) : articles 2 à 4 du chapitre « Création d'un compte spécial au Trésor »**
(intitulé arabe : « إحداث حساب خاص في الخزينة »).

- Art. 2 : le Trésorier général ouvre dans ses écritures un **compte spécial** du Trésor intitulé
  « compte de financement des mesures exceptionnelles de mise à la retraite » ; le ministre chargé
  des Affaires sociales ordonne les dépenses ; elles sont évaluatives.
- Art. 3 : le compte est financé par un pourcentage du produit de l'augmentation spécifique sur le
  tabac et les allumettes, un pourcentage du produit du droit sur les jeux joués par SMS,
  téléphone ou serveur vocal, et les autres ressources que la législation permet de lui affecter.
  **Les deux pourcentages sont fixés par décret** (« أمر »). Le texte ne les donne pas.
- Art. 4 : les ressources paient les pensions des agents mis à la retraite avant l'âge légal, les
  cotisations sociales dues au titre de la loi n° 2009-39, et toute dépense née de ces mesures.

**Même page, haut de page** : fin de l'article 3 (nouveau, dépenses des comptes spéciaux du Trésor :
11e partie, 718 800 000 dinars ; 4e section 2 550 000 000), article 4 (nouveau, crédits de
programmes 3 425 623 000), article 5 (nouveau, crédits d'engagement de développement
4 350 000 000, par parties : 1 708 825 000 + 1 108 569 000 + 415 860 000 + 1 116 746 000).

**Page 2374 (arabe), tableau « ب » (prévisions de recettes des comptes spéciaux du Trésor pour
2009)** : « compte de financement des mesures exceptionnelles de mise à la retraite », 20 000 000
dinars, total du tableau 718 800 000 dinars, ministère des Affaires sociales, de la Solidarité et des
Tunisiens à l'étranger. Même ligne et mêmes chiffres que le tableau « B » de l'édition française
(p. 1828-1829).

### Écart de vocabulaire entre les deux éditions

L'édition française dit « fonds spécial du Trésor » (« Fonds de financement des mesures
exceptionnelles de mise à la retraite ») à l'article 2. L'édition arabe dit « compte spécial »
(« حساب ») dans le titre, la première phrase et le tableau, mais « le fonds » (« الصندوق ») dans les
deux phrases suivantes de l'article 2. L'objet, l'ordonnateur et les ressources sont identiques. Le
chapitre du précis peut garder « compte » (c'est le mot du tableau, dans les deux éditions : « Compte
de financement… » en français, « حساب » en arabe).

### Ce que le texte n'apporte pas

- Aucun pourcentage. Les décrets de pourcentages pour 2009, 2011 et 2012 ne sont pas dans la loi.
  La lecture de ces 11 pages ne les fait pas apparaître.
- Pas de texte arabe différent du français sur le fond : l'édition arabe confirme l'édition
  française, qui était déjà lisible en couche de texte (JORT n° 55 français, p. 1822 et 1828).

## 4. Décret n° 2009-40 (BFPME)

Lu dans l'édition française (couche de texte) et à l'image de l'édition arabe (PDF p. 16, p. 200).

- Quatre articles. Art. 1er : l'organigramme est fixé conformément à un schéma et à une annexe
  joints au décret. Art. 2 : il s'applique sur la base de fiches de poste ; les nominations aux
  emplois fonctionnels suivent l'article 10 bis de la loi n° 96-74. Art. 3 : la banque établit un
  manuel de procédures. Art. 4 : exécution (Premier ministre, ministre des Finances).
- Visas : loi n° 89-9, code des sociétés commerciales, loi n° 2001-65 sur les établissements de
  crédit, arrêté du ministre des Finances du 28 février 2005 (agrément de la BFPME comme banque).
- **Le schéma et l'annexe ne sont pas imprimés** : ni sur la page 190 française, ni sur la page 200
  arabe, ni sur la page suivante (autre texte). L'organigramme lui-même (postes, rattachements)
  reste donc illisible dans le JORT. Une demande à l'administration serait nécessaire ; elle
  n'est pas faite (règle : seulement ce qui est en ligne).

## 5. Ce qui reste illisible ou non fait

- Le corps des 361 autres fascicules arabes de 2009 à 2012 n'est pas océrisé : la recherche des
  décrets de pourcentages (2009, 2011, 2012) reste ouverte. Seuls les sommaires l'ont été (24
  octobre 2026). Piste : lire le sommaire de chaque fascicule, ne passer à l'image que pour les
  lignes « أمر ... يتعلق بضبط نسبة ... » ou « ... الإحالة على التقاعد », au lieu de tout océriser.
- Tableaux « ت », « ث », « ج » de la loi (crédits par ministère) : non lus, hors objet.
- Organigramme de la BFPME (schéma, annexe) : non publié au JORT.

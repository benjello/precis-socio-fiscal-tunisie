# Relevé — diplômés de l'enseignement supérieur, 2001-02 à 2022-23

*Documentaliste, 10 novembre 2026. Reconstitution complète du relevé annoncé par
`docs/notes/education-superieur-2026-10-17.md`, § 9 (le fichier `serie_diplomes_superieur.csv`
n'avait jamais été construit). Répond au TODO de `precis/fr/education/_superieur.qmd` (ligne ~111).*

**Couverture : 22 années sur 22.** Le trou 2012-13 est comblé (61 376, deux sources concordantes),
la colonne des étudiantes de 2003-04 existe et a été relue à l'image, les colonnes ambiguës de
2001-02 et 2002-03 ont été relues à l'image, et le pic de 2009-10 est expliqué et décomposé.

## 1. Le relevé

Source première : INS, *Annuaire statistique de la Tunisie*. Chaque édition (glissante sur cinq
ans) ne publie le tableau des diplômés **que pour sa dernière année universitaire** : une édition
par année, sans recouvrement. PDF lus dans `tunisia-data`,
`data/raw/ins-publications/annuaire-statistique/<édition>.pdf` (couche texte complète, 22 éditions ;
fiche `sources/ins-annuaires-statistiques.md`). Pages imprimées vérifiées sur la couche texte
(libellé de pied de page), et à l'image pour les lignes marquées « image ».

| Année univ. | Diplômés | dont étudiantes | Édition de l'annuaire | Tableau | Page (impr. = PDF sauf mention) | État |
|---|---:|---:|---|---|---|---|
| 2001-02 | 28 565 | 15 120 | 1998-2002 | 3.21 | p. 76 (PDF 70) | texte + **relu à l'image** |
| 2002-03 | 34 254 | 18 309 | 1999-2003 | 3.21 | p. 76 (PDF 70) | texte + **relu à l'image** |
| 2003-04 | 40 321 | 19 949 | 2000-2004 | 3.20 | p. 76 (PDF 70) | texte + **relu à l'image** |
| 2004-05 | 49 811 | 28 243 | 2001-2005 | 3.20 | p. 76 (PDF 70) | texte |
| 2005-06 | 56 559 | 33 352 | 2002-2006 | 3.20 | p. 76 (PDF 70) | texte |
| 2006-07 | 58 598 | 35 660 | 2003-2007 | 3.1.20 | p. 74 | texte |
| 2007-08 | 60 613 | 37 138 | 2004-2008 | 3.1.20 | p. 74 | texte |
| 2008-09 | 65 630 | 41 064 | 2005-2009 | 2.1.20 | p. 66 | texte |
| 2009-10 | 86 035 | 53 718 | 2006-2010 | 2.1.20 | p. 66 | texte |
| 2010-11 | 74 133 | 48 531 | 2007-2011 | 2.1.20 | p. 68 | texte |
| 2011-12 | 68 880 | 45 525 | 2008-2012 | 2.1.20 | p. 68 | texte |
| 2012-13 | 61 376 | 41 390 | **édition 2009-2013 jamais mise en ligne** — INS, *Tunisie en chiffres 2013-2014*, tabl. 2.4, p. 12 (total, **relu à l'image**) ; MESRS, *… en chiffres 2013-2014*, tabl. 1.4 p. 15 et 1.6 p. 16 (étudiantes) | — | — | texte (TEC : corpus local ; MESRS : en ligne, vérifié le 10 nov. 2026) |
| 2013-14 | 61 287 | 41 073 | 2010-2014 | 2.1.19 | p. 61 | texte |
| 2014-15 | 58 748 | 39 093 | 2011-2015 | 2.1.19 | p. 61 | texte |
| 2015-16 | 57 923 | 39 606 | 2012-2016 | 2.1.19 | p. 61 | texte |
| 2016-17 | 54 418 | 36 841 | 2013-2017 | 2.1.19 | p. 61 | texte |
| 2017-18 | 50 307 | 34 671 | 2014-2018 | 2.1.19 | p. 61 | texte |
| 2018-19 | 51 988 | 36 284 | 2015-2019 | 2.1.19 | p. 61 | texte |
| 2019-20 | 49 713 | 35 060 | 2016-2020 | 2.1.19 | p. 61 | texte |
| 2020-21 | 51 409 | 35 935 | 2017-2021 | 2.1.19 | p. 61 | texte |
| 2021-22 | 55 670 | 38 948 | 2018-2022 | 2.1.19 | p. 61 | texte |
| 2022-23 | 51 580 | 36 096 | 2019-2023 | 2.1.19 | p. 61 | texte (déjà relu à l'image le 17 oct. 2026) |

Intitulés exacts des tableaux : « Effectifs des étudiants et diplômés de fin d'études par secteur
et par genre » (éditions 1998-2002 et 1999-2003) ; « Effectif des étudiants diplômés de fin
d'études (AAAA-AAAA) par filières et par genre » (depuis l'édition 2000-2004). Source citée par
l'INS : ministère de l'Enseignement supérieur et de la Recherche scientifique. Note de détail :
l'index de l'édition 2003-2007 annonce « 3.1.21 » mais l'en-tête du tableau porte « 3.1.20 » ;
le relevé suit l'en-tête.

## 2. Ce qui est compté — et les coutures de définition

**Périmètre constant depuis 2003-04** : diplômés de fin d'année universitaire du **secteur public**
(établissements du MESRS *et* des départements en cotutelle — santé, agriculture, jeunesse et
sports…), **tous diplômes confondus** (1er diplôme : licences, maîtrise, ingénieur, médecine ;
2e diplôme : mastères, doctorats, agrégation, révision comptable). Preuve par recoupement exact :
MESRS, *… en chiffres 2013-2014*, p. 15, tabl. 1.4 : 2012-13 = 51 534 admis au 1er diplôme
+ 9 842 au 2e = 61 376, le total INS. **Le secteur privé est exclu** : le même document (tabl. 2.1,
p. 17) compte à part 4 045 diplômés du privé en 2012-13.

**Couture 2002-03 → 2003-04.** Les deux premières éditions (1998-2002, 1999-2003) publient un
tableau différent : *candidats admis à la session de juin* (2002 : 28 565 admis sur 32 215
candidats inscrits ; 2003 : 34 254 sur 38 476), ventilé par **secteur** de formation et non par
filière. La relecture à l'image confirme les colonnes (admis à gauche, inscrits à droite, l'arabe
الناجحون/المترشحون concordant ; coquille d'en-tête français de l'édition 1999-2003, « juin-02 »
pour juin 2003, l'arabe disant 2003). Ce décompte « admis en juin » peut omettre la session
d'octobre : la marche de +6 067 entre 2002-03 et 2003-04 mêle croissance réelle et changement de
définition. **À signaler dans la figure** (note de rupture), sans tenter de raccord.

**2012-13 (le trou comblé).** L'édition 2009-2013 de l'annuaire n'a jamais été mise en ligne
(constat de la fiche tunisia-data, reconfirmé le 10 nov. 2026 : `anunaire-2013.pdf` et
`annuaire-2013.pdf` → 404 ; page `/en/publication/statistical-yearbook-tunisia-2009-2013` → 404).
La valeur vient de deux sources de la même famille (chiffres MESRS) :
- total 61 376 : INS, *Tunisie en chiffres 2013-2014*, tabl. 2.4, p. 12 (corpus local
  `tunisia-data/data/raw/ins-publications/tunisie-en-chiffres/2013-2014.pdf`, relu à l'image) —
  tableau triennal 2011-12/2012-13/2013-14 dont les deux années voisines recoupent exactement
  l'annuaire (68 880 et 61 287) ;
- dont étudiantes 41 390 = 34 717 (1er diplôme) + 6 673 (2e diplôme) : MESRS,
  *L'enseignement supérieur, la recherche scientifique et les TIC en chiffres, année universitaire
  2013-2014*, tabl. 1.4 (p. 15) et 1.6 (p. 16) — valeurs exactes, pas une estimation.
  Contre-épreuve de la méthode sur 2011-12 : l'édition MESRS 2012-2013 donne 38 494 filles au 1er
  diplôme + 65,5 % de 10 733 au 2e ≈ 45 524, contre 45 525 à l'annuaire (écart 1).
Ce n'est donc **pas une approximation** mais un changement de support au sein de la même famille ;
la case « édition de l'annuaire » reste honnêtement vide. Si l'édition papier 2009-2013 refait
surface (BNT, INS), son tableau 2.1.19/2.1.20 remplacera ce montage.

**Le pic de 2009-10 : vérifié et décomposé.** L'annuaire 2006-2010 (tabl. 2.1.20, p. 66) ne
ventile que par filière ; la définition ne change pas cette année-là. L'explication est dans
INS, *Tunisie en chiffres 2012*, tabl. 2.4, p. 12 (relu à l'image), qui ventile par type de
diplôme :

| Type de diplôme | 2009-10 | 2010-11 | 2011-12 | 2012-13* | 2013-14* |
|---|---:|---:|---:|---:|---:|
| Licence fondamentale | 17 899 | 19 925 | 16 031 | 15 915 | 16 511 |
| Licence appliquée | 17 290 | 29 845 | 32 130 | 28 729 | 25 371 |
| Techniciens supérieurs | 8 333 | 18 | 3 | – | – |
| Techniciens sup. paramédicaux | 2 975 | 2 790 | 2 713 | – | – |
| **Maîtrise** | **26 076** | 6 509 | 467 | 4 | – |
| Ingénierie et architecture | 4 157 | 4 252 | 4 611 | 5 199 | 5 473 |
| Professions médicales | 1 137 | 1 454 | 1 502 | 1 510 | 1 529 |
| Autres diplômes | 8 168 | 9 340 | 11 423 | 10 019 | 12 403 |
| **Total** | **86 035** | **74 133** | **68 880** | **61 376** | **61 287** |

\* colonnes de l'édition 2013-2014 du même abrégé (tabl. 2.4, p. 12).

Le pic est bien la **sortie conjointe des dernières grandes cohortes de l'ancien régime
(26 076 maîtrises + 8 333 techniciens supérieurs) et des premières grosses cohortes LMD
(35 189 licences)** — l'hypothèse du § 9 de la note du 17 octobre est confirmée et chiffrée.
En 2010-11 la maîtrise tombe à 6 509, en 2011-12 à 467. La figure devra l'annoter ainsi, plutôt
que de laisser lire une expansion réelle de 31 % suivie d'un effondrement.

## 3. Références candidates (CSL)

**Existante, à réutiliser** : `ins-annuaire-statistique` (`precis/fr/references.json`), entrée
générique couvrant les 22 éditions. Complément à verser dans sa note par le bibliographe : tableau
des diplômés de fin d'études aux pages 76 (éditions 1998-2002 à 2002-2006), 74 (2003-2007 et
2004-2008), 66 (2005-2009 et 2006-2010), 68 (2007-2011 et 2008-2012), 61 (depuis 2010-2014) ;
l'édition 2009-2013 n'existe pas en ligne. (L'autre entrée `ins-annuaire`, restreinte à l'indice
des prix, n'est pas le bon support.)

**À créer** (aucune entrée « Tunisie en chiffres » ni MESRS « en chiffres » dans
`precis/fr/references.json` ni `precis/fr/education/references.json`) :

```json
{
  "id": "ins-tunisie-en-chiffres-diplomes",
  "type": "report",
  "title": "Tunisie en chiffres (éditions 2012 et 2013-2014)",
  "title-short": "INS, Tunisie en chiffres",
  "author": [{"literal": "Institut national de la statistique"}],
  "publisher": "Institut national de la statistique",
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2014]]},
  "URL": "https://www.ins.tn/publication/tunisie-en-chiffres-2013-2014",
  "note": "citation-key: ins-tunisie-en-chiffres-diplomes\nAbrégé statistique annuel de l'INS. Tableau 2.4, « Répartition des diplômés de l'enseignement supérieur » par type de diplôme, p. 12 des deux éditions (lues à l'image le 10 novembre 2026) : édition 2012 pour 2009-10, 2010-11, 2011-12 ; édition 2013-2014 pour 2011-12, 2012-13, 2013-14 — seule source INS en ligne pour 2012-13 (61 376), l'édition 2009-2013 de l'annuaire n'ayant jamais été mise en ligne. Source citée : MESRS. Fichiers : dépôt tunisia-data, data/raw/ins-publications/tunisie-en-chiffres/2012.pdf et 2013-2014.pdf (catalogue sources/ins-publications-urls.csv). Note documentaire : docs/notes/education-releve-diplomes-superieur-2026-11-10.md."
}
```

```json
{
  "id": "mesrs-chiffres2013-2014",
  "type": "report",
  "title": "L'enseignement supérieur, la recherche scientifique et les technologies de l'information et de la communication en chiffres — année universitaire 2013-2014",
  "title-short": "MESRS, en chiffres 2013-2014",
  "author": [{"literal": "Ministère de l'Enseignement supérieur, de la Recherche scientifique et des TIC, Bureau des études, de la planification et de la programmation"}],
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2014]]},
  "URL": "https://www.mes.tn/image.php?id=4106",
  "note": "citation-key: mesrs-chiffres2013-2014\nPlaquette statistique annuelle du ministère, 20 pages. Diplômés 2012-13 du secteur public : tabl. 1.4, p. 15 (1er diplôme : 51 534 admis dont 34 717 filles, par type de diplôme et tutelle) et tabl. 1.6, p. 16 (récapitulatif : 1er diplôme 51 534 dont 34 717 ; 2e diplôme 9 842 dont 6 673) — total 61 376, exactement le chiffre INS. Diplômés du privé à part : tabl. 2.1-2.2, p. 17 (4 045 dont 1 723 filles). URL vérifiée le 10 novembre 2026 (HTTP 200 application/pdf, 353 101 octets, SHA-256 ca3d5928af5a9d60e1b2957745b1e2a295879058a944a9756eb4ded69b584385). À rapatrier dans tunisia-data. Note documentaire : docs/notes/education-releve-diplomes-superieur-2026-11-10.md."
}
```

```json
{
  "id": "mesrs-chiffres2012-2013",
  "type": "report",
  "title": "L'enseignement supérieur et la recherche scientifique en chiffres — année universitaire 2012-2013",
  "title-short": "MESRS, en chiffres 2012-2013",
  "author": [{"literal": "Ministère de l'Enseignement supérieur et de la Recherche scientifique, Bureau des études, de la planification et de la programmation"}],
  "publisher-place": "Tunis",
  "issued": {"date-parts": [[2013]]},
  "URL": "https://www.mes.tn/image.php?id=3140",
  "note": "citation-key: mesrs-chiffres2012-2013\nPlaquette statistique annuelle du ministère, 20 pages. Diplômés 2011-12 du secteur public : 1er diplôme 58 147 admis dont 38 494 filles (tabl. 1.1, p. 15) ; 2e diplôme 10 733, 65,5 % de femmes (tabl. 1.2, p. 15) — total 68 880, le chiffre INS, contre-épreuve de la composition 1er + 2e diplômes. C'est la publication « en chiffres » demandée par la note education-superieur-2026-10-17.md, § 9 et § 11 (contient aussi effectifs du privé et personnel). URL vérifiée le 10 novembre 2026 (HTTP 200 application/pdf, 438 265 octets, SHA-256 f10debbbff627e7ccf8b0ad2e4f26e3a8c1aac43d85bc9c9211f6fa6459c143e). À rapatrier dans tunisia-data. Note documentaire : docs/notes/education-releve-diplomes-superieur-2026-11-10.md."
}
```

## 4. Notions à glossaire

- **diplômés de fin d'études** (المتخرجون في نهاية السنة الجامعية, intitulé bilingue des tableaux
  INS) : à ne verser que si la figure l'emploie ; source canonique pressentie :
  `ins-annuaire-statistique`.
- **maîtrise** et **licence (LMD)** : déjà traités par le chantier du supérieur (décrets n° 93-2333
  et 2008-3123) ; rien à ajouter ici.

## 5. Lacunes

- **Dont étudiantes 2012-13 (41 390)** : seule valeur de la colonne qui ne vient pas d'un tableau
  INS mais de la somme de deux cases exactes du MESRS (34 717 + 6 673). À dire en note de la série
  au catalogue ; remplaçable par le tableau de l'édition 2009-2013 de l'annuaire si elle refait
  surface en papier.
- **Édition 2009-2013 de l'annuaire** : jamais mise en ligne (INS 404 sous quatre orthographes ;
  page anglaise 404 ; Wayback CDX sur `files-ftp3/files/publication/pdf/` : aucun fichier
  `*annuaire*2013*`). La passe Wayback sur l'ancien domaine `ins.nat.tn` n'a **pas pu être faite**
  (Internet Archive « temporarily offline » le 10 nov. 2026) : à rejouer. Pas de fiche
  `docs/recherches.yml` : ce registre vise les textes attendus au JORT, et l'enjeu résiduel est
  faible (toutes les valeurs sont acquises) ; le reliquat est porté au backlog (§ 7).
- **Diplômés du secteur privé** : hors série (exclus des tableaux INS). Points connus : 4 045 en
  2012-13 (MESRS 2013-2014, p. 17). La série privée complète demanderait les éditions successives
  de la plaquette MESRS — demande déjà ouverte au § 11 de la note du 17 octobre.
- **Décomposition par type de diplôme avant 2009-10** : non cherchée au-delà des deux abrégés lus
  (le pic est documenté ; les éditions 2004-2011 de *Tunisie en chiffres*, au corpus, l'auraient
  peut-être pour 2007-2009).

## 6. Recherches infructueuses

Aucune fiche `docs/recherches.yml` ouverte ni à ouvrir (voir § 5 : l'objet manquant n'est pas un
texte JORT et toutes les valeurs de la série sont sourcées). La fiche de source
`tunisia-data/sources/ins-annuaires-statistiques.md` documente déjà l'absence de l'édition
2009-2013 ; le constat y est reconfirmé (10 nov. 2026) — ligne à ajouter côté tunisia-data
(lecture seule ici).

## 7. Marche restante

1. **Rapatrier dans `tunisia-data`** (agent data ; lecture seule ici) : les deux plaquettes MESRS
   (`mes.tn/image.php?id=4106` et `id=3140`, empreintes SHA-256 au § 3) sous
   `data/raw/mesrs-en-chiffres/`, avec catalogue `sources/mesrs-en-chiffres-urls.csv` ; recenser au
   passage les autres éditions (`image.php?id=5119`, `id=5138`, `id=5429` vues en recherche web, et
   la page des statistiques du site) pour la série du privé. Ajouter à la fiche
   `ins-annuaires-statistiques.md` : l'index des tableaux de diplômés (pages du § 1) et le constat
   Wayback ; rejouer la passe `ins.nat.tn` quand l'Internet Archive répondra.
2. **Verser la série au catalogue `tunisia-data`** (comme les onze séries `education-*` du
   29 octobre 2026) : 22 lignes, colonnes année, total, étudiantes, source, page ; deux notes de
   définition (couture 2002-03/2003-04 ; 2012-13 hors annuaire).
3. **Figure** `fig-educ-superieur-diplomes` (rédacteur) : annoter le pic 2009-10 (sortie conjointe
   maîtrises + licences LMD, § 2) et la couture de 2003-04 ; lever le TODO de `_superieur.qmd`.
4. **Bibliographe** : créer les trois entrées du § 3, compléter la note de
   `ins-annuaire-statistique`.

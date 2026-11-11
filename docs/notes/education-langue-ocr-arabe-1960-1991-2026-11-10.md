# OCR édition arabe du JORT (1960-1971, 1982-1985, 1990-1991) — langue d'enseignement

Date : 2026-11-10 · rôle : documentaliste · branche : chantier/education-densification

## Objet

Solder la lacune laissée par la première passe d'océrisation (qui couvrait
1958-1959, 1972-1981, 1986-1989) en étendant l'OCR des **pages 1 et 2** de
l'édition **arabe** du Journal officiel aux années non couvertes — **1960-1971,
1982-1985, 1990-1991** — pour y chercher les arrêtés/décisions fixant programmes
et horaire du primaire (répartition arabe/français, langue du calcul) et tout
texte sur le statut du français au baccalauréat.

## Méthode

- Fascicules : `/home/benjello/projets/PDFs-legislation-tunisie/PDFs/JORT/<année>/ar/Ja*.pdf`.
- **1228 fascicules** océrisés : 1960 (60), 1961 (59), 1962 (64), 1963 (60),
  1964 (66), 1965 (66), 1966 (55), 1967 (55), 1968 (55), 1969 (57), 1970 (58),
  1971 (57), 1982 (84), 1983 (86), 1984 (79), 1985 (91), 1990 (86), 1991 (90).
- Rendu `pdftoppm -r 200 -gray` des pages 1-2, `tesseract -l ara --oem 1` (LSTM).
- Termes cherchés : الباكالوريا، البكالوريا، الابتدائية، انتهاء الدروس،
  ختم الدروس، توقيت، توزيع الأوقات، البرامج، تعريب، اللغة الفرنسية،
  اللغة العربية، الرياضيات، قرار وزير التربية القومية، البرامج الرسمية.
- Tout candidat a été relu à l'image (OCR arabe bruité).

## Résultat : couverture étendue, aucun texte-cible

Aucun arrêté ni décision fixant les **programmes ou l'horaire du primaire** des
élèves ; aucun texte de 1978 sur la **langue du calcul** ; aucun texte retirant
au français le caractère d'épreuve obligatoire du baccalauréat.

Les occurrences des termes sont des faux positifs de contexte :

- **الابتدائية** → presque toujours « المحكمة الابتدائية » (tribunal de première
  instance) dans nominations et concours, non « المدرسة الابتدائية » (école
  primaire).
- **توقيت** → durée hebdomadaire de travail des **personnels** (توقيت العمل
  الأسبوعي) : amendements des décrets n° 126/1973, n° 709/1986, n° 726/1988
  (p. ex. JORT 1982/061, 1990/042, 1991/021) — pas l'horaire des élèves.
- **البرامج** → programmes d'examens du supérieur (licence/CAPES en droit, 1960 ;
  maîtrises en sciences, 1990) ou « programmes » budgétaires (loi de finances,
  1991/023).
- **تعريب / اللغة الفرنسية / اللغة العربية** → épreuves de **traduction** de
  concours administratifs, p. ex. concours de secrétaires municipaux
  (JORT 1964/031, p. 556).

Seul texte relatif au primaire reparu : **arrêté du 25 mai 1963** sur le
certificat de fin d'études primaires (JORT 1963/027) — déjà au registre
(dates/pages dans les passes antérieures de la fiche).

## Références candidates (témoins incidents, hors fenêtres des fiches)

Textes sur le baccalauréat de l'enseignement secondaire repérés en 1991 (hors
période des fiches, notés pour la lignée issue de l'arrêté du 27 août 1988 ;
aucun ne touche au statut du français) :

- **Arrêté du ministre de l'éducation et des sciences du 23 mars 1991** modifiant
  l'arrêté du 27 août 1988 relatif à l'examen du baccalauréat de l'enseignement
  secondaire — JORT n° 24 de 1991 (fascicule arabe `Ja02491.pdf`, sommaire p. 1).
- **Rectificatif (إصلاح غلط)** du même arrêté — JORT n° 30 de 1991 (`Ja03091.pdf`,
  sommaire p. 1).

## Lacunes et suites (hors JORT)

Le texte fixant les programmes/horaires du primaire n'est pas au Journal
officiel sur toute la fenêtre 1958-1992 (pages 1-2). Reste à chercher **hors
JORT** : les programmes et horaires officiels publiés par le ministère
(**Centre national pédagogique**, bulletins du ministère), que le règlement
scolaire du 25 janvier 1964 (art. 9) désigne comme « programmes et horaires
d'enseignement officiels ». a_faire résiduel laissé en ce sens dans
`docs/recherches.yml` (fiche r-educ-horaires-primaire-1958-1992).

Non couvert : le **corps** des fascicules au-delà de la page 2.

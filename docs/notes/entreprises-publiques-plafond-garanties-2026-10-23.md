# Entreprises publiques : le plafond de la garantie de l'État, 1958-59 à 1994 (23 octobre 2026)

Note documentaire du chantier « série légale du plafond des garanties ». Elle complète
`docs/notes/entreprises-publiques-2026-10-11.md`, § 1.2 (plafond 2016-2024, annexes du
ministère des Finances) : la présente note donne le plafond fixé par la loi, avant 2016.

## 1. Méthode

- Notices : `jort_cache.db`, titres « octroi de la garantie de l'Etat », 1956-1996. Le champ
  `pages` de la notice d'un article de loi de finances est la page où l'article est imprimé
  (contrôlé sur l'en-tête ou le pied de page de chaque fascicule, ou sur les pages voisines
  du même fascicule, trente-huit cas).
- Lecture : fascicules français du corpus local (`PDFs/JORT/<année>/fr/`), scannés, sans texte.
  Reconnaissance de caractères (Tesseract, français, 170 dpi) sur la page de l'article, relue à
  l'image pour les gestions 1966, 1975 et 1979 (reconnaissance illisible) et pour 1963, 1969 et
  1985 (numéros d'article mal reconnus). Gestion 1985 : le numéro imprimé est peu lisible
  (« 51 » ou « 54 ») ; 54 d'après la suite des articles 53 et 55.
- Le relevé versionné est `precis/fr/entreprises_publiques/listes/plafond-garanties-lois-de-finances.csv`
  (manifeste `.csv.yml`, test `tests/test_listes_entreprises_publiques.py`).

## 2. Faits sourcés

Formule de l'article : « Le montant total dans la limite duquel le ministre [des Finances, du
Plan et des Finances, secrétaire d'État …] est autorisé à accorder la garantie du Trésor (puis,
dans la loi de finances pour 1984 et les suivantes : de l'État) en vertu des textes et
conventions en vigueur est fixé pour la gestion N à … ». Montants en millions de dinars (MD).

| Gestion | Montant (MD) | Loi, article, page |
|---|---|---|
| 1958-59 | 7 milliards de francs | loi n° 58-45, art. 30, p. 325 |
| 1959-60 | 12 | loi n° 59-42, art. 12, p. 281 |
| 1961 | 12 | loi n° 60-38, art. 15, p. 1711 |
| 1962 | 12 | loi n° 61-65, art. 11, p. 1808 |
| 1963 à 1966 | 16 | lois n° 62-82 (art. 12, p. 1658), 63-58 (art. 44, p. 1877), 64-59 (art. 14, p. 1569), 65-46 (art. 25, p. 1719) |
| 1967 | 20 | loi n° 66-79, art. 21, p. 1788 |
| 1968 à 1973 | 25 | lois n° 67-57 (art. 23), 68-41 (art. 16), 69-64 (art. 19), 70-66 (art. 29), 71-59 (art. 7), 72-87 (art. 11) |
| 1974 | 25, puis 50 | loi n° 73-82, art. 40, p. 2285 ; loi n° 74-75 du 3 août 1974, art. 8, p. 1747 : « porté pour la gestion 1974 de vingt-cinq millions de dinars à cinquante millions de dinars » |
| 1975, 1976 | 50 | lois n° 74-101 (art. 35, p. 2917), 75-83 (art. 16, p. 2853) |
| 1977 à 1987 | 200 | lois n° 76-115 (art. 50) à 86-106 (art. 68) |
| 1988 | 200, puis 300 | loi n° 87-83, art. 20 ; loi n° 88-145, art. 18 (p. 1794) : 300 « pour l'année 1988 et l'année 1989 » |
| 1989 à 1991 | 300 | lois n° 88-145, 89-115 (art. 20, p. 2146), 90-111 (art. 20, p. 2050) |
| 1992 | 250, puis 530 | loi n° 91-98, art. 20, p. 2083 ; loi n° 92-122, art. 21, p. 1669, rubrique « Régularisation de la garantie de l'Etat pour la gestion 1992 » |
| 1993 | 500, puis 900 | loi n° 92-122, art. 20 ; loi n° 93-111 du 8 novembre 1993, article unique, p. 1900 |
| 1994 | 950 | loi n° 93-125, art. 18, p. 2195 |

Le détail article par article et page par page est dans le relevé CSV.

- **Commission de garantie.** Arrêté du ministre des finances du 3 avril 1993 (JORT n° 28 des
  13-16 avril 1993, p. 507) : l'octroi de la garantie est subordonné au paiement d'une
  commission sur le montant du crédit garanti, 0,5 % pour une institution financière, 1,5 %
  pour une institution non financière (art. 2), versée au « fonds d'amortissement de la
  garantie de bonne fin donnée par le trésor » au plus tard à la date de la première utilisation
  du crédit (art. 3), avec débit d'office du compte de l'emprunteur (art. 4). Il vise l'article 36
  de la loi n° 77-81. **Correction du chapitre** : il disait que cet arrêté institue une
  commission de garantie qui instruit les demandes ; l'arrêté fixe la commission due par
  l'emprunteur. Le rapport du ministère des Finances (édition LF 2020, p. 38) renvoie à cet
  arrêté pour la « commission de garantie » (transcription du 11 octobre 2026, § 1.2) : rien ne
  montre qu'une commission d'instruction des demandes existe ; le passage est à relire.
- La loi de finances pour 1979 (loi n° 78-59, art. 44, p. 3778) supprime le « fonds de
  péréquation de change 1964 » et verse ses excédents au fonds spécial du Trésor intitulé
  « Fonds d'amortissement de la garantie de bonne fin donnée par le Trésor ».

## 3. Références

Seize notices neuves (FR et AR, fonds commun), plus `loi66-79-lf1967` promue du volume « Les cotisations sociales » au fonds commun : `loi58-45-lf1958`, `loi59-42-lf1959`,
`loi60-38-lf1961`, `loi61-65-lf1962`, `loi62-82-lf1963`, `loi63-58-lf1964`, `loi64-59-lf1965`,
`loi65-46-lf1966`, `loi67-57-lf1968`, `loi71-59-lf1972`, `loi73-82-lf1974`,
`loi74-75-lfc1974`, `loi75-83-lf1976`, `loi77-81-lf1978`, `loi78-59-lf1979`,
`loi93-111-garantie-1993`, plus `arrete1993-04-03-commission-garantie`. Les autres lois sont
déjà au fonds commun (`lf-1969`, `lf-1970`, `lf-1971`, `lf-1973`, `lf-1977`, `lf-1981`,
`lf-1983` à `lf-1986`, `lf-1990` à `lf-1994`, `loi74-101-lf1975`, `loi79-66-lf1980`,
`loi81-100-lf1982`, `loi86-106-lf1987`, `loi-87-83-lf-1988`, `loi-88-145-lf-1989`). Adresses
pist.tn tirées de `jort_cache.db` (`pdf_fr`, `pdf_ar` du même enregistrement), non rejouées en
ligne. Le volume n'a pas de livre arabe : seul le fonds commun arabe est versé.

## 4. Notions à glossaire

`garantie-etat` existe ; définition complétée (plafond fixé par la loi de finances depuis
1958-59 au moins). Non versées, faute de terme arabe attesté : commission de garantie, fonds
d'amortissement de la garantie de bonne fin.

## 5. Lacunes et recherches

- Fiche `r-ep-plafond-garantie-1995-2015` : plafond de 1995 à 2015 (l'index de `jort_cache` ne
  détaille plus les articles ; fascicules du corpus local à lire) ; gestion 1960 (aucune notice) ;
  décret du 29 juin 1957 (budget ordinaire 1957-58, JORT n° 52, `1957F/Jo15257.pdf`, absent du
  corpus local) ; lois de finances complémentaires de 1969 à 1991 non lues en entier.
- Article 36 de la loi n° 77-81 non lu.
- Parts du plafond (ajoutées le 23 octobre 2026) : PIB de l'année de la gestion de 1961 à 1994
  (Banque mondiale sans base dite jusqu'en 1991, INS en base 1983 de 1992 à 1994, deux segments,
  rupture en 1992 sans conversion) ; dépenses de l'État hors service de la dette, réalisation,
  de 1986 à 1994 (série `denominateurs-depenses-etat-pib`). Aucune dépense de l'État avant 1986
  dans l'entrepôt : totaux des budgets des lois de finances de 1959-60 à 1985 à lire ; aucun PIB
  pour 1959-60.
- Prêts du Trésor aux entreprises publiques (article voisin de chaque loi, code de la
  comptabilité publique, art. 62) : montants vus (1974-75 : 14 puis 20 MD ; 1979 : 20 MD ;
  1992 : 20 MD ; 1994 : 40 MD), non relevés en série.

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
- Le relevé est versé dans `tunisia-data` (série `jort-lf-plafond-garanties`, cache `precis/_seriescache/jort-lf-plafond-garanties.csv`) ; le fichier `listes/plafond-garanties-lois-de-finances.csv` du livre est retiré le 24 octobre 2026
  (test `tests/test_listes_entreprises_publiques.py`).

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

## 6. Plafond de 1995 à 2015 (ajouté le 23 octobre 2026)

**Méthode.** Fascicules français du corpus local (`PDFs/JORT/<année>/fr/`) : couche texte, lue par
`pdftotext`. Les fascicules de 1999 à 2004 (et celui du 1er novembre 2002) ont une police codée :
chaque caractère est décalé de 29 rangs, le texte se déchiffre en ajoutant 29 au code. Numéro de page
relevé sur le pied de page de la page qui porte l'article ; page 2876 (gestion 2003) contrôlée à
l'image. Les lois de finances complémentaires sont cherchées par « limite duquel » dans le texte ; pour
2002, 2004 et 2006 (autre codage), par reconnaissance de caractères.

| Gestion | Montant (MD) | Loi, article, page |
|---|---|---|
| 1995 | 950 | loi n° 94-127, art. 13, p. 2042 |
| 1996 | 950 | loi n° 95-109, art. 13, p. 2369 (le texte écrit « législation en vigueur », et non plus « textes et conventions en vigueur ») |
| 1997 | 950 | loi n° 96-113, art. 16, p. 2579 |
| 1998 | 950 | loi n° 97-88, art. 16, p. 2436 |
| 1999 | 950 | loi n° 98-111, art. 11, p. 2501 |
| 2000 | 950 | loi n° 99-101, art. 11, p. 2740 |
| 2001 | 950 | loi n° 2000-98, art. 11, p. 3172 |
| 2002 | 950, puis 1 800 | loi n° 2001-123, art. 11, p. 4252 ; loi n° 2002-90 du 29 octobre 2002, art. unique, p. 2535 (JORT n° 89) : « est porté de 950.000.000 dinars à 1.800.000.000 dinars » |
| 2003 | 1 200 | loi n° 2002-101, art. 11, p. 2876 |
| 2004 | 950 | loi n° 2003-80, art. 11, p. 3722 |
| 2005 à 2010 | 950 | lois n° 2004-90 (art. 9, p. 3433), 2005-106 (p. 3597), 2006-85 (p. 4381), 2007-70 (p. 4358), 2008-77 (p. 4275), 2009-71 (p. 3912) |
| 2011 | 1 800, puis 4 000 | loi n° 2010-58, art. 9, p. 3462 ; décret-loi n° 2011-56 du 25 juin 2011, art. 1er (art. 9 nouveau), p. 1013 (JORT n° 47) |
| 2012 | 4 000 | loi n° 2011-7, art. 9, p. 5 |
| 2013 | 3 000 | loi n° 2012-27, art. 9, p. 5 : garantie « pour la conclusion des prêts ou émissions des soukouks islamiques » |
| 2014, 2015 | 3 000 | lois n° 2013-54 (art. 9, p. 3668) et 2014-59 (art. 9, p. 3463), même libellé |

**Constats.**

- Loi n° 2012-1 du 16 mai 2012 (loi de finances complémentaire pour 2012, art. 1er, p. 921) : « article 9
  (nouveau) » au même montant de 4 000 MD pour 2012. Aucun montant ne change : pas de ligne dans le relevé.
- Loi de finances pour 1997, art. 17, p. 2580 : « nonobstant » l'article 16, la garantie de l'État est
  accordée dans la limite de 980 000 000 dinars aux dettes de l'Office des céréales et de l'Office
  national de l'huile envers la Banque nationale agricole au 31 décembre 1996, consolidées sur douze ans
  sans intérêts et rachetées par la Banque centrale. Garantie distincte, hors du plafond de l'article 16 :
  non versée dans la série.
- Lois de finances complémentaires sans modification du plafond (aucune occurrence de « limite duquel »
  ou de « garantie de l'État » dans le texte) : n° 2005-103, 2007-64, 2008-76, 2009-40, 2013-51, 2014-54 ;
  par reconnaissance de caractères : n° 2002-100 (modifie les articles 1, 2, 5, 6 et 7 de la loi n° 2001-123),
  2004-87, 2006-70 (modifie la loi n° 2001-123, autres articles). Pas de loi de finances complémentaire
  indexée pour 2015.
- Décrets-lois et décrets de 2001 à 2002 « portant octroi de la garantie de l'État pour la couverture des
  conséquences de la responsabilité civile du fait des risques de guerre » dans le transport aérien :
  garantie propre, sans montant plafond annuel, hors série.

**À reporter dans `tunisia-data`** : la série du plafond légal (gestion, montant fixé, montant en vigueur
à la fin de la gestion), 1959-60 à 2015, série `jort-lf-plafond-garanties` de `tunisia-data`.

**Références.** Nouvelle notice : `loi2002-90-garantie-2002` (FR et AR, fonds commun). `lf-1998`
(loi n° 97-88) promue du volume « Fiscalité » au fonds commun, FR et AR. Les autres lois sont déjà au
fonds commun (`lf-1995` à `lf-2015`, `loi2001-123-lf2002`, `loi-2007-70-lf-2008`,
`dl-2011-56-lfc-2011`) : leur note porte maintenant l'article et la page du plafond.

**Lacunes.** Gestion 1960, décret du 29 juin 1957 et lois de finances complémentaires de 1969 à 1991
(fiche `r-ep-plafond-garantie-1995-2015`) ; lois de finances de 2016 à 2024 (le plafond de 2016 à 2024
vient des annexes du ministère des Finances ; seule la loi de 2020 est lue).

## 7. Dénominateurs d'avant 1986 : le budget ordinaire voté (ajouté le 23 octobre 2026)

**Question.** Parts du plafond dans le budget de l'État avant 1986 : « aucun dénominateur » dans
l'entrepôt (dépenses de l'État hors service de la dette, réalisation, depuis 1986 seulement).

**Lu.** Les articles 1 à 4 de chaque loi de finances de 1959-60 et de 1961 à 1986 (fascicules
français scannés, reconnaissance de caractères à 250 dpi, deux colonnes séparées, puis relecture de
l'image) : article 1er, recettes ordinaires du budget de l'État (tableau « A ») ; article 3 (ou 6),
montant maximum des crédits des dépenses de gestion (1961-1967) ou courantes (depuis 1968). **Les
deux montants sont égaux chaque année** : l'égalité contrôle la lecture. Relevé versionné :
`listes/budget-ordinaire-lois-de-finances.csv` (manifeste `.csv.yml`, test
`test_budget_ordinaire_vote_recettes_et_credits_egaux`).

| Gestion | MD | Gestion | MD | Gestion | MD |
|---|---|---|---|---|---|
| 1959-60 | 48,6 (recettes) | 1970 | 146,5 | 1980 | 751,6 |
| 1961 | 55,8 | 1971 | 154,0 | 1981 | 938,0 |
| 1962 | 56,8 | 1972 | 175,0 | 1982 | 1 168,0 |
| 1963 | 59,95 | 1973 | 208,1 | 1983 | 1 420,0 |
| 1964 | 68,3 | 1974 | 247,2 | 1984 | 1 544,0 |
| 1965 | 86,0 | 1975 | 344,6 | 1985 | 1 885,0 |
| 1966 | 100,5 | 1976 | 385,5 | 1986 | 1 970,0 |
| 1967 | 108,1 | 1977 | 441,5 | | |
| 1968 | 124,0 | 1978 | 541,2 | | |
| 1969 | 131,35 | 1979 | 625,1 | | |

**Ce que le montant est — et n'est pas.** Un montant voté du seul budget ordinaire (titre I). Les voies et
moyens du budget d'équipement comprennent une « contribution du budget ordinaire » (0,6 MD en 1961, art. 23
de la loi n° 60-38) : la somme des deux budgets compterait deux fois cette contribution, et la structure du
budget d'équipement (puis de développement : crédits d'engagement, crédits de paiement, reconstruction,
voies et moyens) change d'une loi à l'autre. Aucun total de l'État n'est donc établi ; le budget
d'équipement n'est pas compris. La loi de finances pour 1983 (loi n° 82-91, art. 1er et 2, p. 2876) fixe
en outre un budget général de 1 753 MD, dont 954 MD de dépenses courantes et 799 MD de dépenses
d'investissement (crédits de paiement) ; l'année suivante, la loi revient au seul budget ordinaire :
ce total de 1983 n'a pas de voisin et n'est pas versé. Le dénominateur de 1986 à 2015 (dépenses de
l'État hors service de la dette, réalisation) est un autre concept : la ligne de 1986 porte les deux
(plafond de 200 MD : 10,2 % du budget ordinaire voté de 1 970 MD, 8,4 % des dépenses réalisées de
2 395 MD), les séries ne sont pas chaînées, la figure les sépare par un trait vertical.

**Pages.** Page de l'article : en-tête du fascicule (décalage page imprimée moins page du fichier lu sur
les en-têtes voisins) ; pour 1985 (loi n° 84-84), la double page numérisée porte l'article 1er page 2950
et l'article 3 sur la moitié droite (2951).

**Lecture à l'image** pour 1962, 1963, 1964, 1967, 1968, 1969 (la reconnaissance de caractères donnait
131,85 au lieu de 131,35), 1975 (scan à basse résolution), 1976, 1978 à 1986 ; reconnaissance de caractères
concordante entre les articles 1er et 3 pour les autres gestions. Dans la loi de finances pour 1959-60
(loi n° 59-42), les recettes (48,6 MD, art. 1er) sont lues, le chiffre des crédits (art. 3) est effacé :
seule la recette est versée. Loi de finances pour 1979 (loi n° 78-59) : recettes lues à basse résolution.

**À reporter dans `tunisia-data`** : la série « budget ordinaire voté, 1959-60 à 1986 » (recettes =
crédits), avec sa définition ci-dessus ; **non versée ici**.

**Non lus (fiche `r-ep-budget-etat-1959-1985`).** Budgets d'équipement et de développement de 1961 à 1985 ;
réalisation du budget avant 1986 (lois de règlement, rapports de la Banque centrale) ; budget ordinaire de
1958-59 (loi n° 58-45, en francs, budget fixé par décret du 29 juin 1957) ; gestion 1960 ; crédits de
1959-60.

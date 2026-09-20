# Où sont les textes que les consignes demandent de lire

Recensement produit le 20 septembre 2026 par un balayage des commentaires `TODO` des
chapitres. Pour chaque texte nommé par son numéro, on donne son fascicule d'après
`jort_cache.db` et **l'état de ce fascicule dans le corpus local** — ce qui décide du coût
de la lecture, et que la consigne elle-même ne dit jamais.

Quatre avertissements, tous rencontrés en établissant ce tableau :

- **un fascicule « texte » peut porter un tableau en image.** Vérifié sur les arrêtés du
  barème d'actualisation de 1997 et 2024 : entre l'annonce du barème et l'article 2, la
  couche texte ne contient que des en-têtes courants. L'état ci-dessous qualifie le
  fascicule, pas chacune de ses pages ;
- **« texte décalé »** signifie que `pdftotext` rend du charabia qui se relit en ajoutant 29
  à chaque code (`docs/notes/outillage-sources.md`, § 5). Ne pas le prendre pour un scan ;
- **le cache porte des homonymes** : plusieurs textes sous un même numéro, parfois dans le
  même fascicule. Rencontré sur les numéros 95-2487, 83-112 et 2004-167. Toujours vérifier
  la page avant de citer ;
- **une absence ici ne prouve rien** : elle dit que le corpus local ne l'a pas, non que le
  texte n'existe pas. `pist.tn` répond.

## texte — lisible directement — 34

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 2007-2148 | 2007 n°69 | 3070-3071 | `retraites/_secteur_prive.qmd:123` |
| n° 2007-70 | 2007 n°104 | 4357-4358 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2009-2085 | 2009 n°56 | 1919-1920 | `retraites/_secteur_public.qmd:206` |
| n° 2009-349 | 2009 n°12 | 0477-0482 | `prestations_sociales/index.qmd:52` |
| n° 2010-58 | 2010 n°102 | 3460-3462 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2010-58 | 2010 n°5 | 0170-0172 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2011-16 | 2011 n°21 | 0381 | `prestations_sociales/index.qmd:52` |
| n° 2014-54 | 2014 n°6 | 0173-0174 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2014-54 | 2014 n°68 | 2183-2232 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2015-462 | 2015 n°51 | — | `remunerations_publiques/_regime_indiciaire.qmd:318` |
| n° 2017-47 | 2017 n°27 | 1214 | `prestations_sociales/index.qmd:714` |
| n° 2017-47 | 2017 n°50 | 2244 | `prestations_sociales/index.qmd:714` |
| n° 2017-66 | 2017 n°101 | — | `fiscalite/_impot_revenu.qmd:526` |
| n° 2017-66 | 2017 n°37 | 1691 | `fiscalite/_impot_revenu.qmd:526` |
| n° 2017-66 | 2017 n°5 | — | `fiscalite/_impot_revenu.qmd:526` |
| n° 2018-56 | 2018 n°6 | 0208 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2018-56 | 2022 n°108 | 2723-2727 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2018-56 | 2022 n°26 | 0666-0667 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2019-37 | 2019 n°35 | 1312-1315 | `retraites/_secteur_public.qmd:85` |
| n° 2025-17 | 2025 n°2 | 0050-0051 | `fiscalite/_impot_revenu.qmd:512` |
| n° 94-1429 | 1994 n°52 | 1141-1142 | `retraites/_secteur_prive.qmd:154` |
| n° 95-105 | 1995 n°101 | 2308 | `retraites/_secteur_public.qmd:169` |
| n° 95-538 | 1995 n°30 | 0690-0693 | `cotisations_sociales/index.qmd:84` |
| n° 95-56 | 1995 n°53 | 1419-1424 | `remunerations_publiques/_regime_indiciaire.qmd:176` |
| n° 96-101 | 1996 n°7 | 0114 | `prestations_sociales/index.qmd:707` |
| n° 96-101 | 1996 n°94 | 2319-2320 | `prestations_sociales/index.qmd:707` |
| n° 97-1832 | 1997 n°76 | 1771-1780 | `remunerations_publiques/_regime_indiciaire.qmd:130` |
| n° 97-88 | 1997 n°104 | 2435-2436 | `fiscalite/_impot_revenu.qmd:578` |
| n° 97-88 | 1997 n°13 | 0324-0325 | `fiscalite/_impot_revenu.qmd:578` |
| n° 97-88 | 1998 n°91 | 2248-2249 | `fiscalite/_impot_revenu.qmd:578` |
| n° 98-111 | 1998 n°104 | 2500-2501 | `fiscalite/_impot_revenu.qmd:578` |
| n° 98-1981 | 1998 n°83 | 2067-2069 | `retraites/index.qmd:257` |
| n° 98-37 | 1998 n°43 | 1170 | `retraites/_secteur_public.qmd:93` |
| n° 99-101 | 1999 n°8 | 0141-0142 | `prestations_sociales/index.qmd:52` |

## texte décalé — lisible après décodage — 18

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 2001-123 | 2001 n°104 | 4251-4252 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2001-123 | 2001 n°30 | 0942 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2001-123 | 2002 n°78 | 2282 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2002-101 | 2002 n°102 | 2875-2876 | `fiscalite/_impot_revenu.qmd:120` |
| n° 2002-101 | 2002 n°7 | 0196 | `fiscalite/_impot_revenu.qmd:120` |
| n° 2002-104 | 2002 n°106 | 3187-3190 | `retraites/_secteur_prive.qmd:452` |
| n° 2002-104 | 2002 n°9 | 0182 | `retraites/_secteur_prive.qmd:452` |
| n° 2002-32 | 2002 n°22 | 0603-0606 | `prestations_sociales/index.qmd:707` |
| n° 2002-32 | 2002 n°5 | 0106 | `prestations_sociales/index.qmd:707` |
| n° 2002-32 | 2002 n°63 | 1765-1766 | `prestations_sociales/index.qmd:707` |
| n° 2002-61 | 2002 n°57 | 1584-1585 | `retraites/_secteur_public.qmd:85` |
| n° 2003-1128 | 2003 n°42 | 1679-1681 | `retraites/index.qmd:224` |
| n° 2003-1656 | 2003 n°65 | 2483-2484 | `retraites/_secteur_public.qmd:85` |
| n° 2003-80 | 2003 n°104 | 3721-3722 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2003-80 | 2003 n°4 | 0134 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2003-80 | 2004 n°36 | 1212 | `fiscalite/_impot_revenu.qmd:578` |
| n° 2003-894 | 2003 n°34 | 1291-1294 | `retraites/_secteur_prive.qmd:452` |
| n° 99-101 | 1999 n°105 | 2739-2740 | `prestations_sociales/index.qmd:52` |

## scan — océrisation requise — 54

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 59-18 | 1959 n°5 | 0057-0059 | `retraites/_secteur_public.qmd:40` |
| n° 59-18 | 1959 n°8 | 0093-0100 | `retraites/_secteur_public.qmd:40` |
| n° 60-30 | 1960 n°47 | 1292 | `cotisations_sociales/index.qmd:84` |
| n° 60-30 | 1960 n°57 | 1602-1613 | `cotisations_sociales/index.qmd:84` |
| n° 60-30 | 1960 n°8 | 0208 | `cotisations_sociales/index.qmd:84` |
| n° 60-30 | 1961 n°33 | 1107 | `cotisations_sociales/index.qmd:84` |
| n° 60-33 | 1960 n°57 | 1616 | `retraites/index.qmd:32` |
| n° 60-33 | 1960 n°8 | 0213-0214 | `retraites/index.qmd:32` |
| n° 65-17 | 1965 n°3 | 0048 | `cotisations_sociales/index.qmd:365` |
| n° 65-17 | 1965 n°34 | 0787 | `cotisations_sociales/index.qmd:365` |
| n° 72-230 | 1972 n°29 | 0995-1003 | `remunerations_publiques/_regime_statutaire_autonome.qmd:96` |
| n° 74-499 | 1974 n°30 | 0915-0919 | `cotisations_sociales/index.qmd:204` |
| n° 74-499 | 1974 n°39 | 1252 | `cotisations_sociales/index.qmd:204` |
| n° 75-83 | 1975 n°5 | 0169 | `retraites/index.qmd:32` |
| n° 75-83 | 1975 n°7 | 0225 | `retraites/index.qmd:32` |
| n° 75-83 | 1975 n°87 | 2852-2853 | `retraites/index.qmd:32` |
| n° 75-952 | 1975 n°87 | 2884 | `prestations_sociales/index.qmd:200` |
| n° 79-96 | 1979 n°5 | 0199-0201 | `remunerations_publiques/_regime_statutaire_autonome.qmd:41` |
| n° 81-188 | 1981 n°10 | 0319-0320 | `retraites/_secteur_prive.qmd:244` |
| n° 81-6 | 1981 n°26 | 0844 | `cotisations_sociales/index.qmd:84` |
| n° 81-6 | 1981 n°55 | 2036 | `cotisations_sociales/index.qmd:84` |
| n° 81-6 | 1981 n°9 | 0265-0273 | `cotisations_sociales/index.qmd:84` |
| n° 82-1030 | 1982 n°51 | 1605-1607 | `retraites/_secteur_prive.qmd:87` |
| n° 82-1030 | 1982 n°66 | 2197 | `retraites/_secteur_prive.qmd:87` |
| n° 83-112 | 1983 n°12 | 0435-0436 | `remunerations_publiques/_regime_statutaire_autonome.qmd:90` |
| n° 83-112 | 1983 n°82 | 3214-3225 | `remunerations_publiques/_regime_statutaire_autonome.qmd:90` |
| n° 83-31 | 1983 n°23 | 0808-0809 | `retraites/_secteur_public.qmd:458` |
| n° 85-1025 | 1985 n°62 | 1095 | `retraites/_secteur_public.qmd:93` |
| n° 85-109 | 1985 n°91 | 1730-1731 | `fiscalite/_impot_revenu.qmd:84` |
| n° 85-109 | 1986 n°13 | 0316 | `fiscalite/_impot_revenu.qmd:84` |
| n° 85-12 | 1985 n°20 | 0359-0365 | `remunerations_publiques/_regime_indiciaire.qmd:176` |
| n° 85-12 | 1985 n°70 | 1319 | `remunerations_publiques/_regime_indiciaire.qmd:176` |
| n° 85-12 | 1985 n°76 | 1472-1473 | `remunerations_publiques/_regime_indiciaire.qmd:176` |
| n° 85-16 | 1985 n°21 | 0375-0377 | `retraites/_secteur_public.qmd:458` |
| n° 85-16 | 1985 n°73 | 1401-1402 | `retraites/_secteur_public.qmd:458` |
| n° 86-438 | 1986 n°25 | 0504 | `prestations_sociales/index.qmd:52` |
| n° 86-47 | 1986 n°35 | 0683 | `prestations_sociales/index.qmd:52` |
| n° 87-337 | 1987 n°18 | 0369-0370 | `retraites/_secteur_public.qmd:206` |
| n° 88-145 | 1988 n°11 | 0203 | `retraites/_secteur_public.qmd:458` |
| n° 88-145 | 1988 n°87 | 1793 | `retraites/_secteur_public.qmd:458` |
| n° 88-145 | 1989 n°32 | 0808 | `retraites/_secteur_public.qmd:458` |
| n° 88-145 | 1990 n°9 | 0168-0170 | `retraites/_secteur_public.qmd:458` |
| n° 88-16 | 1988 n°20 | 0427 | `retraites/_secteur_public.qmd:458` |
| n° 88-16 | 1988 n°4 | 0058-0059 | `retraites/_secteur_public.qmd:458` |
| n° 88-40 | 1988 n°33 | 0735-0736 | `retraites/index.qmd:202` |
| n° 89-114 | 1989 n°1 | 0003-0021 | `fiscalite/_impot_revenu.qmd:137` |
| n° 89-114 | 1989 n°88 | 2142-2144 | `fiscalite/_impot_revenu.qmd:137` |
| n° 90-111 | 1990 n°13 | 0281-0282 | `fiscalite/_droits_consommation.qmd:187` |
| n° 90-111 | 1990 n°86 | 2049-2050 | `fiscalite/_droits_consommation.qmd:187` |
| n° 90-1455 | 1990 n°60 | 1358 | `retraites/_secteur_prive.qmd:154` |
| n° 91-604 | 1991 n°32 | 1008 | `retraites/_secteur_prive.qmd:444` |
| n° 91-98 | 1991 n°90 | 2082-2083 | `fiscalite/_impot_revenu.qmd:578` |
| n° 92-24 | 1992 n°17 | 0314-0325 | `remunerations_publiques/_regime_marche_controle.qmd:37` |
| n° 93-308 | 1993 n°13 | 0246-0247 | `prestations_sociales/index.qmd:773` |

## absent du corpus — 6

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 2018-56 | 2018 n°104 | — | `fiscalite/_impot_revenu.qmd:496` |
| n° 2018-56 | 2020 n°91 | 1979-1981 | `fiscalite/_impot_revenu.qmd:496` |
| n° 2024-4 | 2024 n°129 | 5293-5293 | `prestations_sociales/index.qmd:714` |
| n° 2025-17 | 2025 n°148 | 4231-4231 | `fiscalite/_impot_revenu.qmd:512` |
| n° 2025-17 | 2025 n°155 | 3654-3654 | `fiscalite/_impot_revenu.qmd:512` |
| n° 83-112 | 2022 n°123 | 3031-3033 | `remunerations_publiques/_regime_statutaire_autonome.qmd:90` |

## illisible — 1

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 2019-37 | 2019 n°23 | — | `retraites/_secteur_public.qmd:85` |

## inconnu du cache — 1

| Texte | Fascicule | Pages | Consigne |
|---|---|---|---|
| n° 2022-79 | — | — | `fiscalite/_impot_revenu.qmd:526` |

## Ce que le tableau dit

Les consignes nomment **66 textes distincts**. Un même numéro pouvant renvoyer à plusieurs
fascicules — le cache porte des homonymes, et certains textes sont republiés —, le recensement
compte **114 fascicules** :

- **34** — texte — lisible directement
- **18** — texte décalé — lisible après décodage
- **54** — scan — océrisation requise
- **6** — absent du corpus
- **1** — illisible
- **1** — inconnu du cache

**Cinquante-deux fascicules se lisent aujourd'hui** — les deux premières catégories —, sans
autre outil que `pdftotext` et, le cas échéant, le décodage du décalage. Ce sont eux qu'il
faut prendre d'abord. Cinquante-quatre demandent une océrisation, et six un téléchargement
sur `pist.tn`.

Ce tableau ne dit pas ce que chaque consigne demande, seulement ce qu'il en coûte de
l'instruire. Il se régénère en rejouant le balayage ; il n'a pas vocation à être tenu à la
main.

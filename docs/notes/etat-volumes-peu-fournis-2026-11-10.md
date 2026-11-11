# État des lieux des volumes les moins fournis — 10 novembre 2026

Dépouillement du 10 novembre 2026 (quatre passes de lecture : `.qmd`, `TODO`/`RECHERCHE`,
notes de `docs/notes/`, backlog). Volumes examinés : santé, caisses, cotisations sociales,
éducation — les moins fournis après exclusion de l'informel (exploration abandonnée sur
décision du propriétaire ; l'informel n'est d'ailleurs pas un livre selon la doctrine du
17 octobre 2026, mais une colonne « population couverte », un chapitre du marché du travail
et un chapitre de la synthèse).

Cette note est un **instantané d'orientation**, pas un backlog : les reports détaillés sont
déjà consignés dans `docs/notes/backlog-precis.md` et `backlog-modele.md` (vérifié lors du
dépouillement) ; les deux corrections de backlog constatées sont listées en fin de note.

## Diagnostic transversal

Les quatre volumes sont *structurellement* mûrs (charpente complète, format « ruptures au
premier plan » là où il s'applique). Le goulot n'est plus la rédaction mais :

1. **la donnée** — séries à construire ou à obtenir (caisses post-2004, résultats scolaires,
   honoraires de ville, séries ATFP) ;
2. **des lectures ciblées** — éditions arabes, fascicules sans couche texte à océriser ;
3. deux lacunes de forme récurrentes : la section « Ce qu'en dit l'économie » manque
   (caisses, cotisations, en partie santé) et des glossaires pauvres (santé : 3 termes).

| Volume | Goulot principal | Première action (rôle) |
|---|---|---|
| Santé | `_medecine_ville` et `_histoire` squelettiques | documentaliste (avenants convention 2007-2012) ; gain rapide : terminologue |
| Caisses | rien de consolidé après 2004 | documentaliste : les 4 séries de `cadre-budgetaire-comptable-caisses.md` § 3 |
| Cotisations | 3 tableaux AT/MP faits main | modeliste : openfisca-tunisia#471 |
| Éducation | bourses 1982 non lues ; chapitre « résultats » absent | documentaliste : édition arabe 1982-1987 |

## La santé (~16 600 mots, FR seul)

**Maturité.** `index` complet pour son rôle ; `_couverture` (8 768 mots) quasi complet —
budget Santé 2018-2023, comptes CNAM 2011-2021, ventilation CRES, comptes OMS, études de la
réforme de 2004 ; `_hopital` (4 924 mots) partiel — cadre de 1991, tarifs malades payants
1996/1998, facturation CNAM 2007-2021, mais **aucun montant de rémunération** ;
`_medecine_ville` (1 671 mots) squelette — convention de 2007 et conventionnés, sans
honoraires ni avenants ni longue période ; `_histoire` (643 mots) squelette ; `_glossaire` :
3 termes (**porté à 14 notions le 10 novembre au soir**, worktree `precis-wt-sante` ; termes
arabes `provisoire`, à faire attester).

**Matière rassemblée non versée.** ~8 termes de glossaire prêts
(`sante-series-etudes-2026-10-15.md` § 10 : APCI, DTS, filières, dépense catastrophique,
résultat technique, bénéficiaire) ; extraction OMS GHED 2000-2023 préparée (§ 9) pour relier
2004 / 2012-2014 / 2018-2023 en une seule méthode (TODO `_couverture` l. 467) ; les notes
avant-2004 (`sante-couverture-avant-2004`, `sante-regimes-avant-2004`, 164 Ko) peuvent
nourrir `_histoire` (le gros alimente « Prestations sociales »).

**Prochaines étapes.** 1. terminologue : glossaire (gain immédiat). 2. documentaliste :
avenants n° 1-7 (2007-2012) de la convention de ville, honoraires des annexes, dates
d'effet, puis figure de longue période. 3. documentaliste : extraction GHED. 4.
documentaliste/architecte : `_histoire` (politique sanitaire avant 1991, couverture avant
2008). 5. documentaliste : budgets exécutés des EPS, grilles salariales (décret n° 97-1832,
à lire) et statuts paramédicaux. 6. économiste : « Ce qu'en dit l'économie » (incidence,
dépense catastrophique).

## Les caisses de sécurité sociale (~16 800 mots)

**Maturité.** Six chapitres + deux annexes, tous mûrs sur le périmètre juridique ;
`_histoire` très mûr (Protectorat → CNAM, Bertrand 1953 + textes 1956-1961 lus à l'image).
Limite : `_comptes_longue_periode` ne tient que **1990-2004** (CNSS) ; rien de consolidé
après 2004, CNRPS limité à 2015-2018. `_etat_caisses` réclame des séries datées (4 TODO,
2 RECHERCHE). Pas de section « Ce qu'en dit l'économie ».

**Matière rassemblée non versée.** `cadre-budgetaire-comptable-caisses.md` § 3 : quatre
séries à construire (comptes des organismes de sécurité sociale INS 2001-2025 ; versements
du tableau A aux caisses 1985-2004 ; prolongation CNSS post-2004 ; répartition de la CSS) ;
§ 5 : notices CSL à créer. `css-verification.md` : notes communes DGELF 1/2023, 1/2026,
28/2019 à verser. Montants Bertrand 1951-52 et chiffres BM/Vittas retenus faute de série
datée.

**Prochaines étapes.** 1. documentaliste : construire les quatre séries (le plus fort
rendement — débloque la longue période des trois caisses). 2. documentaliste/OCR : solder
les RECHERCHE (tutelle CNRPS 1976-1985, organisation CNRPS post-1989, arrêté du transfert
des réserves CNAM, placements obligatoires et levée de 1991, arrêtés de répartition CSS,
norme comptable sectorielle — fascicules < 1996 sans couche texte). 3. économiste : dossier
puis section (gouvernance, placements, compensation entre régimes). 4. bibliographe : notes
communes DGELF et sources des transferts État → CNRPS. 5. rédacteur : compléter
`_etat_caisses` et la longue période une fois les séries prêtes. 6. humain/architecte :
retours de lectrices (place des parties II/V, titres).

## Les cotisations sociales (~34 000 mots)

**Maturité.** Volume mûr, réorganisé par branche le 4 octobre 2026. Solides : `_pensions`,
`_regimes`, `_bilan`, `_accidents_travail` (8 913 mots, le plus développé). Minces :
`_maladie` (1 505 mots) et surtout `_autres_branches` (1 276 mots : famille + emploi +
complémentaire). **Arabe : les dix chapitres et annexes sont déclarés et le livre rend** —
le backlog l. 1806 est périmé sur ce point.

**Matière rassemblée non versée.** Statistiques CNAM 2021-2023 (AT/MP) à l'entrepôt, à
raccorder aux figures `fig-atmp-declares`/`fig-atmp-frequence` ; série
`atmp-sinistres-declares-2012-2022` (tunisia-data#34) à fusionner ; 221 valeurs CNSS 1999
masquées par la reliure (tunisia-data#26) ; fiche en réserve
`docs/reserve/atmp-bareme-sinistralite.md` (attente d'un passage NAT61→NAT2009 publié).

**Prochaines étapes.** 1. modeliste (openfisca-tunisia#471) : salaires forfaitaires AT/MP
(décret n° 95-538 art. 4-7, décret n° 2000-1439) et modulation (art. 10-27) pour remplacer
les trois tableaux faits main. 2. modeliste : cotisation de prévoyance sur pension CNRPS dès
1973 (décret n° 73-91 art. 15, 2 %) et non 2007 ; art. 5 du décret n° 2007-1406 au tableau
`cnrps_maladie`. 3. documentaliste : ventilations et assiettes manquantes (part des
prestations familiales dans le taux global d'origine, assiette du régime général avant 1995
et art. 89 de la loi n° 81-6, maladie des agents publics avant 2007, régime étudiants
1965-1992). 4. bibliographe : clés `loi57-73`, `decret-96-1797`,
`cnss-annuaires-statistiques` à mettre au fonds commun. 5. rédacteur : étoffer
`_autres_branches` ; trancher le TODO `_pensions` l. 87. 6. économiste : « Ce qu'en dit
l'économie » (coin social, effets emploi) — absente du volume.

## L'éducation et la formation (~74 500 mots, FR seul)

**Maturité.** Sept chapitres au format « ruptures au premier plan » : histoire, scolaire
(17 000 mots) et dépense complets ; supérieur quasi complet (réordonné par parcours le
30 octobre) ; aides riche (21 900 mots) mais bourses lacunaires ; **formation
professionnelle partiel** (4 400 mots, aucune série, aucune figure). Deux chapitres du plan
non commencés : « résultats » (scolarisation, examens, abandon) et « rapports et études /
Ce qu'en dit l'économie ». ~45 TODO et ~40 ancres RECHERCHE ouverts.

**Ce qui bloque.** Arrêté du 20 août 1982 (montants des bourses) jamais retrouvé en
français — édition arabe 1982-1987 à lire ; seuils de revenu 1986-2005 et montants
post-2017 inconnus ; langue d'enseignement : trois fiches RECHERCHE ouvertes, sommaires
arabes 1960-1971 / 1982-1985 / 1990-1991 à océriser ; séries du ministère à obtenir pour le
chapitre « résultats ».

**Matière rassemblée non versée.** 79 relevés `education-depense-series/` catalogués dans
`tunisia-data` ; ~~`serie_diplomes_superieur.csv` (INS 2003-2023) prête pour
`fig-educ-superieur-diplomes`~~ — **correction du 10 novembre au soir : ce fichier n'a jamais
existé** ; le relevé a été reconstitué depuis les annuaires INS le même jour (22/22 années,
`docs/notes/education-releve-diplomes-superieur-2026-11-10.md`, worktree
`precis-wt-education`) ; séries des communes par article pas encore au catalogue ;
conseils régionaux non traités (modèles d'arrêtés 1975/2008 en édition spéciale arabe).

**Prochaines étapes.** 1. documentaliste : édition arabe 1982-1987 (bourses — déblocage
central du chapitre aides). 2. documentaliste : OCR des sommaires arabes (langue
d'enseignement) ; programmes du Centre national pédagogique. 3. documentaliste : séries du
ministère pour « résultats ». 4. architecte puis rédacteur : chapitre « résultats » quand
les séries seront là ; formation professionnelle après obtention des séries ATFP. 5.
bibliographe : ~15 clés manquantes ; promotion de `loi2024-18`. 6. terminologue : « vie
scolaire », « conseil d'établissement », « conseil pédagogique », « cellule de médiation ».
7. relecteur-ar : traductions des textes cités à relire sur l'édition arabe. 8. économiste :
« Ce qu'en dit l'économie » (incidence CEQ 2021 déjà en séries).

**Traduction arabe : pas mûr.** Deux chapitres manquent, lignes de tableaux en TODO,
classement des ruptures provisoire. Attendre la stabilisation structurelle.

## Corrections de backlog constatées (pour l'archiviste-backlog)

- `backlog-precis.md` l. ~1818 (huit liens du livre des caisses visant
  `cotisations_sociales/index.html#…`) : **déjà corrigé dans les sources** — les `.qmd` des
  caisses pointent vers `_taux_global.html`, `_pensions.html`, `_bilan.html`,
  `_autres_branches.html`, `_regimes.html` ; seuls `public/` et `.quarto/_freeze/` (artefacts
  de build) gardent les anciennes adresses. Le report peut être clos, à l'exception de
  `caisses/index.qmd` l. 11 → `cotisations_sociales/index.html#sec-cot-perimetre`, cible
  légitime (page d'accueil du livre des cotisations).
- `backlog-precis.md` l. ~1806 (chapitre `_prelevements_salaires` « déclaré en commentaire »
  dans `precis/ar/cotisations_sociales/_quarto.yml`) : **périmé** — le `_quarto.yml` arabe
  déclare les dix chapitres et annexes, livre rendu.

# Ce qui reste à faire, livre par livre

État au 12 septembre 2026. Cette note rassemble ce que disent les issues ouvertes, les
commentaires `<!-- TODO (rôle) : … -->` des chapitres et les notes de travail. Elle ne
remplace ni les unes ni les autres : elle sert à voir l'ensemble, et à décider par quoi
continuer.

Les constats portant sur le modèle de microsimulation ont leur propre fichier,
`backlog-modele.md`. Les références à verser ou à corriger dans Zotero sont dans
`biblio-a-rapatrier.md`.

## Vue d'ensemble

| Livre | Écrit (lignes) | TODO | État |
|---|---:|---:|---|
| Retraites | 1 042 | 55 | rédigé sur le *Journal officiel*, tableaux de paramètres provisoires |
| Prestations sociales | 780 | 12 | rédigé, plusieurs séries sans fondement publié |
| Fiscalité | 580 | 22 | **trois sections promises sont vides** |
| Rémunérations publiques | 593 | 34 | un chapitre abouti, trois chapitres brefs |
| Cotisations sociales | 463 | 3 | le plus complet |

## Fiscalité — le plus en retard

Le portail promet « le système fiscal tunisien » ; seul l'impôt sur le revenu est traité.

- **Sections vides** : impôt sur les sociétés, taxe sur la valeur ajoutée, droits de
  consommation. Elles ne portent qu'un « TODO: détailler ».
- **Sections à écrire dans l'IRPP** : le minimum d'impôt (art. 44 § II) et la contribution
  au budget de l'État ; le régime forfaitaire depuis 1990, avec ses seuils et ses tarifs.
- **Séries à construire** : le seuil de la tranche à 0 % et les déductions pour charges de
  famille, rapportés au SMIG et à l'indice des prix, 1990-2026 ; les tarifs successifs de la
  contribution des patentes ; le plafond de déduction des primes d'assurance-vie.
- **Lectures** : barèmes régionaux d'évaluation forfaitaire agricole ; véhicule d'origine du
  taux de 60 % de l'article 12 bis ; notes communes de la DGI sur la réforme de 2025 ;
  articles 56 et 91 de la loi de finances 2026, lus en arabe, à confirmer en français.
- **Ton** : exposer en regard au moins deux lectures attribuées de la dérive du barème.

## Retraites

- **Lectures restantes** (39) : rectificatifs des décrets n° 82-1030 et de la loi n° 81-6 ;
  arrêtés annuels du barème d'actualisation, de 1994 à 2024 ; série du SMAG journalier ;
  règlement du régime complémentaire du 18 novembre 1978 ; articles propres du RTNS, du
  RACI et du RTTE ; textes de départ anticipé du régime agricole.
- **Question ouverte** : comment les pensions du régime non agricole ont été liquidées entre
  le 23 septembre 1990 et le 30 juin 1994, la règle de 1990 laissant l'article 19 inchangé.
  À chercher dans les circulaires et les rapports de la CNSS.
- **Treize tableaux de paramètres** sont écrits à la main et attendent d'être engendrés,
  après la fusion des PR qui datent et sourcent les paramètres en amont.
- **Régimes spéciaux** : le décret-loi n° 2011-48 relève aussi la contribution de
  l'employeur pour les membres du gouvernement et les gouverneurs ; le chapitre ne le dit pas.

## Prestations sociales

- **Onze paliers de l'allocation** entre 1987 et 2018 n'ont aucun fondement textuel publié.
  Pistes non explorées : circulaires de la direction générale de la promotion sociale.
- **Montants non relevés** : aides aux personnes âgées (arrêtés de 1997 et 2003) et aux
  personnes handicapées (arrêtés de 2006 et 2017), soit deux séries entières.
- **Fascicules manquants** : lois de finances 2025 et 2026 en édition française.
- **Deux conflits de source** à trancher sur pièce, dont la date de la loi n° 2017-47.
- **Indemnités familiales** : décret n° 75-952 et circulaire n° 42 de 1996 à lire pour
  compléter la série en amont de 1986.

## Rémunérations publiques

- **Chapitres à étoffer** : régime statutaire autonome (83 lignes), conventionnel public
  (63) et marché contrôlé (62), contre 234 pour le régime indiciaire.
- **Chronologies à construire** : indemnité de magistrature (décrets identifiés au JORT) ;
  textes de rémunération des magistrats de l'ordre judiciaire, des forces de sécurité
  intérieure et des douanes, absents du livre ; tranches de l'indemnité de gestion et
  d'exécution de 1996 à 2012.
- **Séries** : effectifs et masse salariale par régime ; dépenses de défense ; effectifs du
  secteur financier public. Substituer des sources tunisiennes officielles aux chiffres du
  FMI et de la Banque mondiale.
- **Vérifications sur source primaire** : statut du personnel des caisses sociales (issue
  #13), champ des banques publiques, existence d'une convention-cadre des entreprises
  publiques, branches financées par les cotisations CNRPS.

## Cotisations sociales

- Modificatifs du décret n° 74-499 publiés après avril 2026.
- Loi n° 65-17 du 28 juin 1965, pour les branches couvertes par le régime des étudiants.

## Ce qui traverse les cinq livres

- **Zotero** : la synchronisation est bloquée tant que le rangement des clés remontées dans
  la bibliographie partagée n'est pas tranché ; sinon elles reviendront en doublon dans les
  fichiers de livre (issue #17, détail dans `biblio-a-rapatrier.md`).
- **Titres arabes** : 69 entrées bibliographiques portent encore un titre français.
- **Glossaire arabe** : 26 termes à valider (issues #151, #77, #54, #53).
- **Tableaux engendrés** : la règle est que tout tableau de paramètres vienne des dépôts
  openfisca par un générateur. Retraites et Prestations sociales y dérogent provisoirement.
- **Version arabe** : produite par la CI ; rendre l'arabe en local avant de fusionner la PR
  de traduction.

## Suite proposée

1. Terminer la série en cours sur les retraites : rejouer et fusionner les PR du modèle,
   publier, puis remplacer les treize tableaux faits main.
2. Débloquer Zotero, qui conditionne toute la tenue de la bibliographie.
3. Ouvrir le chantier de la fiscalité, seul livre dont des sections promises sont vides.
4. Étoffer les trois chapitres brefs des rémunérations publiques.

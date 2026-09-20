# Ce qui reste à faire, livre par livre

État au **20 septembre 2026**, version v1.26.0. Cette note rassemble ce que disent les
issues ouvertes, les commentaires `<!-- TODO (rôle) : … -->` des chapitres et les notes de
travail. Elle ne remplace ni les unes ni les autres : elle sert à voir l'ensemble, et à
décider par quoi continuer.

**Une note périmée est pire qu'absente** : elle envoie vers des chantiers clos. Celle-ci
l'était de huit jours le 20 septembre, et annonçait trois impôts « pas commencés » alors
qu'ils étaient écrits. La règle qui en découle : **toute branche qui ajoute ou réorganise un
chapitre met à jour la vue d'ensemble dans le même commit.**

Les constats portant sur le modèle de microsimulation ont leur propre fichier,
`backlog-modele.md`. Les références à verser ou à corriger dans Zotero sont dans
`biblio-a-rapatrier.md`. **Où trouver chaque texte que les consignes demandent de lire, et
ce qu'il en coûte de l'ouvrir** : `todo-localisation.md`.

## Vue d'ensemble

| Livre | Écrit (lignes) | TODO | État |
|---|---:|---:|---|
| Fiscalité | 1 300 | 26 | **les quatre impôts sont écrits** ; l'impôt sur le revenu reste à réorganiser |
| Retraites | 1 201 | 40 | rédigé sur le *Journal officiel*, tableaux de paramètres provisoires |
| Rémunérations publiques | 751 | 33 | un chapitre abouti, trois chapitres brefs |
| Prestations sociales | 708 | 12 | rédigé, plusieurs séries sans fondement publié |
| Cotisations sociales | 401 | 3 | le plus complet |

Les 114 `TODO` ne sont pas un arriéré de négligence. **Cinquante-six d'entre eux demandent
explicitement de lire ou de vérifier un texte** — ils marquent un endroit où le précis refuse
d'affirmer ce qu'il n'a pas vu. Les autres sont des sections à écrire, des séries à
construire, des questions à trancher. Le compte baissera parce qu'on aura lu, ou il ne
baissera pas. Une passe de tri menée le 20 septembre sur les vingt-sept consignes de la fiscalité n'en
a trouvé **aucune** déjà satisfaite : il n'y a pas de stock de consignes closes à supprimer.

## Fiscalité — les quatre impôts sont écrits

Le livre porte désormais **1 300 lignes et 484 citations**, réparties sur quatre chapitres :
impôt sur le revenu (596 lignes), droits de consommation (351), impôt sur les sociétés (329)
et taxe sur la valeur ajoutée (185). Les trois derniers ont été ouverts entre le 16 et le
20 septembre ; le portail ne promet plus rien qu'il ne tienne.

Ce qui reste porte sur la FORME d'un chapitre et sur des lectures, non sur des sections
absentes.

- **Réorganiser `_impot_revenu.qmd`** — le seul chapitre encore rangé par paramètre plutôt
  que par réforme. Voir « Forme des chapitres » plus bas ; c'est le plus gros chantier
  ouvert du livre.
- **Sections à écrire dans l'IRPP** : le minimum d'impôt (art. 44 § II) et la contribution
  au budget de l'État ; le régime forfaitaire depuis 1990, avec ses seuils et ses tarifs.
- **Séries à construire** : le seuil de la tranche à 0 % et les déductions pour charges de
  famille, rapportés au SMIG et à l'indice des prix, 1990-2026 ; les tarifs successifs de la
  contribution des patentes ; le plafond de déduction des primes d'assurance-vie.
- **Lectures** : barèmes régionaux d'évaluation forfaitaire agricole ; véhicule d'origine du
  taux de 60 % de l'article 12 bis ; notes communes de la DGI sur la réforme de 2025 ;
  articles 56 et 91 de la loi de finances 2026, lus en arabe, à confirmer en français.
- **Ton** : exposer en regard au moins deux lectures attribuées de la dérive du barème.
- **Reste du côté du glossaire** : un seul arbitrage, entre « revenu annuel net » (au
  glossaire) et « revenu net global » (proposé par la note documentaire sur l'article 8,
  alinéa 1er) — une notion ou deux ? Les vingt autres notions que la consigne réclamait
  existent, et l'annexe est déclarée dans les `_quarto.yml` des deux langues.
- **Reste du côté de la bibliographie** : deux textes cités en prose sans clé — loi
  n° 2001-123 (LF 2002) et loi n° 2007-70 (LF 2008) — et le versement Zotero des vingt clés
  de la sous-section sur l'assiette, qui restent provisoires tant qu'il n'est pas fait.

## Retraites

- **Lectures restantes** : rectificatifs des décrets n° 82-1030 et de la loi n° 81-6 ;
  série du SMAG journalier ; règlement du régime complémentaire du 18 novembre 1978 ;
  articles propres du RACI et du RTTE ; textes de départ anticipé du régime agricole.
- **Barème d'actualisation — chronologie faite, coefficients à relever.** Les vingt-huit
  arrêtés ont leur clé dans les deux langues, et le chapitre donne leur rythme : signature en
  février, effet rétroactif au 1er janvier, une ligne ajoutée par an, et **aucun arrêté pour
  2016, 2017 ni 2019**. Les COEFFICIENTS ne sont pas publiés : ils doivent être relus à
  l'image. Deux pièges consignés dans la consigne du chapitre — un fascicule textuel dont le
  tableau est une image (1997, 2024), et deux sérialisations du tableau dont l'une, appariée
  au jugé, produit des séries fausses mais plausibles.
- **Travailleurs non salariés — fait.** Âge, stage, taux, plancher et versement unique sont
  lus sur le décret n° 95-1166, sa chaîne modificative entière avec eux. L'article 30 a changé
  de nature en 2002 : la revalorisation, d'abord suspendue à un arrêté, est devenue
  automatique.
- **Question ouverte, et la voie du *Journal officiel* y est ÉPUISÉE** : comment les pensions
  du régime non agricole ont été liquidées entre le 23 septembre 1990 et le 30 juin 1994.
  Vérifié le 20 septembre : aucun texte entre ces dates ne vise le décret n° 74-499 hors celui
  de 1994, lequel ne porte aucune clause de régularisation — sa seule rétroactivité vise la
  quote-part de cotisations. Restent les circulaires et rapports de la CNSS, l'avis non publié
  du Tribunal administratif, la doctrine et la jurisprudence ; aucun n'est au corpus local.
  **Cette question se résoudra hors du *Journal officiel*, ou pas du tout.**
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

- **Chapitres à étoffer** : régime conventionnel public (63 lignes), marché contrôlé (62) et
  statutaire autonome (99), contre 474 pour le régime indiciaire.
- **Chronologies à construire** : indemnité de magistrature (décrets identifiés au JORT) ;
  textes de rémunération des magistrats de l'ordre judiciaire, des forces de sécurité
  intérieure et des douanes, absents du livre ; tranches de l'indemnité de gestion et
  d'exécution de 1996 à 2012.
- **Séries** : effectifs et masse salariale par régime ; dépenses de défense ; effectifs du
  secteur financier public. Substituer des sources tunisiennes officielles aux chiffres du
  FMI et de la Banque mondiale.
- **Vérifications sur source primaire** : statut du personnel des caisses sociales (issue
  #13), champ des banques publiques, existence d'une convention-cadre des entreprises
  publiques. Les **branches financées par les cotisations CNRPS** sont aux articles 8 à 10 de
  la loi n° 85-12, dont le fascicule — JORT n° 76 de 1985 — est un scan : océrisation requise.
- **Deux points clos le 20 septembre.** La chaîne des décrets fixant la liste des employeurs
  soumis à la loi n° 95-56 est vérifiée fascicule par fascicule et citée (n° 95-2487, puis
  2000-908, 2001-1446, 2006-2777, 2012-2586). Et l'**indemnité familiale** ne relève pas de
  la CNRPS : c'est une indemnité de rémunération portée par le budget de l'employeur, ce que
  le livre « Prestations sociales » établissait déjà sans que celui-ci en tire parti.
- **Code des collectivités locales** : l'édition française du JORT n° 39 de 2018 est absente
  du corpus, l'arabe y est et s'extrait. Attention, l'absence d'un régime de rémunération
  propre NE PEUT PAS être confirmée par une recherche par mots-clés : le code porte seize
  « مرتب », quatorze « تأجير » et onze « منحة », probablement au titre des élus. À lire.

## Cotisations sociales

- Modificatifs du décret n° 74-499 publiés après avril 2026.
- Loi n° 65-17 du 28 juin 1965, pour les branches couvertes par le régime des étudiants.

## Forme des chapitres — le plan type, et où il ne s'applique pas

**Tout chapitre décrivant un dispositif suit le même déroulé** : l'historique d'abord,
jusqu'à la création du dispositif ; sa description, paramètres d'origine compris ;
l'évolution, **une sous-section par grande étape**, chacune portant à la fois l'intention du
texte et le mouvement des paramètres ; enfin la longue période, puis les données. Les
tableaux de synthèse sont groupés en un seul endroit, pour que la consultation reste possible
sans relire le récit.

Ce plan ne s'applique **pas partout**, et c'est un résultat, non une réserve. Il décrit un
dispositif dont la substance *est* un jeu de paramètres datés — un impôt. Pour un régime de
retraite, dont la substance est un jeu de règles qui s'emboîtent, il détruirait de
l'information.

| Chapitre | Forme | À faire |
|---|---|---|
| `_impot_societes.qmd` | conforme | — |
| `_droits_consommation.qmd` | historique remonté en tête | la chronologie du périmètre reste un tableau sans récit texte par texte — signalé, non confirmé |
| `_tva.qmd` | historique sorti de l'attaque | — |
| `_impot_revenu.qmd` | **non conforme** | évolution rangée en cinq chronologies parallèles ; tout niché d'un cran de trop ; rendement en `###` au lieu de `##` ; pas de synthèse de longue période |
| `retraites/_secteur_*.qmd` | **rangés par mécanisme, et c'est bien** | ne pas y appliquer le plan type |
| `_regime_indiciaire.qmd` | fait le travail sous d'autres noms | ne rien reprendre sur la forme |

La réorganisation de `_impot_revenu.qmd` se mène en trois passes : les niveaux de titre
d'abord, dont le diff se vérifie seul ; la colonne chronologique ensuite ; la description et
la longue période enfin. Sur 596 lignes et 109 citations, le **balayage phrase à phrase** de
l'original contre le résultat n'est pas optionnel : sur un chapitre deux fois plus court, il
avait rattrapé deux pertes sans citation, donc invisibles au décompte.

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
- **Plafond de dépense Gemini atteint, et non relevé avant le mois prochain.** Onze fichiers
  français sont en avance sur leur arabe ; `scripts/traduction_en_retard.py` dit lesquels.
  Aucune relance n'y changera rien : ce n'est pas un débit, c'est un plafond. Depuis le
  20 septembre, la passe s'arrête au premier refus — un appel, pas onze — et, quand le
  plafond explique TOUT, elle finit au vert avec un avis plutôt qu'en rouge. Au 1er octobre,
  un `workflow_dispatch` sans argument rattrapera l'ensemble.
- **Garde-fou de troncature — CORRIGÉ le 20 septembre.** Il était enveloppé dans
  `if old_target_text:` et ne s'exécutait donc pas en retraduction complète, le mode où la
  troncature est la plus probable. Mesuré sur le vrai script : un chapitre arabe de 175 lignes
  était écrasé par une réponse de 3, la passe sortant en 0. Il se règle désormais sur la
  SOURCE à défaut d'ancienne cible, et trois épreuves lui interdisent de redevenir
  conditionnel.
- **`prestations_sociales/index.qmd` résiste aux deux modes de traduction** : 780 lignes,
  171 clés de citation, 9 cellules de code — le chapitre le plus lourd du corpus. Mise à jour :
  13 divergences de parité avant, 68 après (PR #157, fermée). Retraduction complète : 102 lignes
  sur 780 (PR #159, fermée). L'arabe est resté à son meilleur état connu, 636 lignes et
  13 divergences. Ne pas relancer en l'état : découper le fichier ou traduire par sections.

## Suite proposée

1. **Réorganiser `_impot_revenu.qmd`**, en trois passes (voir « Forme des chapitres »).
   C'est le dernier chapitre de la fiscalité qui ne suit pas le plan type.
2. **Au 1er octobre, rattraper la traduction** : `workflow_dispatch` sans argument, puis
   relecture arabe. Onze fichiers, dont le chapitre entier de l'impôt sur les sociétés.
3. **Terminer la série en cours sur les retraites** : rejouer et fusionner les PR du modèle,
   publier, puis remplacer les treize tableaux faits main.
4. **Débloquer Zotero**, qui conditionne toute la tenue de la bibliographie.
5. **Étoffer les trois chapitres brefs des rémunérations publiques**.

Pour toute consigne qui demande de lire un texte, commencer par `todo-localisation.md` : sur
les cent-quatorze fascicules recensés, **cinquante-deux se lisent aujourd'hui**, cinquante-
quatre demandent une océrisation et six un téléchargement. Ce sont les cinquante-deux qu'il
faut prendre d'abord.

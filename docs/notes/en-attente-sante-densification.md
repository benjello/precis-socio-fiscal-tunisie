# En attente — chantier santé « densification » (relais, 10 novembre 2026)

Relais durable du chantier `chantier/sante-densification`. Point d'arrêt : rédaction des quatre
chapitres faite et vérifiée (rendu FR+AR vert, 0 citation [?]), passe 2 terminologue et clôture
bibliographe lancées. **Rien de ce qui suit ne doit vivre seulement dans la conversation.** Les
lignes « Backlog » ci-dessous sont à appliquer par `archiviste-backlog` après fusion (elles ne sont
pas écrites dans `docs/notes/backlog-precis.md`, convention des chantiers parallèles).

## Différé à la demande du propriétaire (10 nov. 2026) : l'économiste

La section « Ce qu'en dit l'économie » du volume santé (incidence de la réforme de 2004, dépense
catastrophique, accès aux soins) est **différée** (« on verra plus tard »). La matière est **déjà
rassemblée et conservée** ; ne pas la refaire :

- **Études déjà intégrées au chapitre** `_couverture.qmd` (section des études de la réforme) : thèse
  Safa Ismail (Paris-Dauphine, 2015, `@ismail-2015-these`) ; article Ismail & Zaouali 2022
  (`@ismail-zaouali2022-reforme`) ; notes CRES (`@cres2015-lettre7-socles`,
  `@blel-chahed2014-depenses-cnam`) ; synthèse des comptes de la santé 2012-2014
  (`@benabdelaziz2018-financement`).
- **Notes documentaires** : `sante-series-etudes-2026-10-15.md` (séries et études),
  `sante-cnam-comptes-2026-10-12.md`, `sante-couverture-avant-2004-2026-10-14.md`,
  `sante-regimes-avant-2004-2026-10-14.md`.
- **Notion de glossaire prête** : `depense-catastrophique` (versée), `apci`, etc.

Au lancement de l'économiste : partir de ces sources, distinguer le budgétaire des évaluations,
donner la méthode de chaque étude (qui, quelles données, quel périmètre, quel calcul).

## Backlog du chantier (points fermés + lacunes) — pour `archiviste-backlog`

**Fermés le 10 nov. 2026 (rédigés) :**
- `_histoire.qmd` : politique sanitaire avant 1991 (section « Organiser, équiper et former… ») et
  population couverte avant 2008, d'après `sante-histoire-politique-sanitaire-pre1991-2026-11-10.md`.
- `_couverture.qmd` : série GHED 2000-2023 (`#fig-soins-financement-ghed`), remplacement du TODO
  l. 467 (raccordement 2004/2012-14/2018-23), ancre `#g-resultat-technique`.
- `_hopital.qmd` : grille 97-1832 (valeurs au 1ᵉʳ janvier 1998), composantes de rémunération par
  corps, financement des EPS.
- `_medecine_ville.qmd` : convention 2007 et avenants 1-7, honoraires datés, parcours de médecin de
  famille (modalités non datables → fiche `r-sante-medecin-famille-modalites`).

**Lacunes ouvertes :**
- Histoire : plans Ier-Xe (primaires hors corpus), MSP « 50 ans d'indépendance », série de lits
  avant 1991, première carte sanitaire ; séries CNRPS et AMG par année avant 2008 ; assurés avant
  2000 ; clé CSL dédiée à « La CNSS en chiffres » (TODO bibliographe dans le `.qmd`).
- Médecine de ville : avenant n° 7 publié sans annexe ; avenant n° 8 absent de `jort_cache` (FR) ;
  édition arabe 2008-2013 et avenant n° 9 (2020) non parcourus.
- Hôpital : grilles successives non constituées (décrets 2007-267/268 cités, non lus) ; statuts
  2000-1688/89, 2015-56/57, décret 93-1725 non lus (TODO) ; budgets exécutés d'EPS à obtenir (Cour
  des comptes, RAP/PAP).
- GHED : 10/19 indicateurs écartés ; raccordement 2004 limité (périmètres différents).
- Glossaire AR : 24 entrées santé `provisoire` → confirmation arabophone/JORT AR ; l'arrêté du
  25 juin 2007 (éd. AR) validerait `apci`.
- Bibliographe : paginations AR des avenants/décrets « à relever » ; clé à créer pour *actes 2017,
  diapositives Ben Abbès* (atteste l'AR des filières).

## Contrôle non exécutable en local (à rejouer par la CI)

`scripts/verifier_liens_base_legislative.py` (liens « Base législative » des tableaux openfisca)
interroge le réseau (`parameters.tn.tax-benefit.org`) et part en timeout dans l'environnement de
rédaction. Il ne porte sur aucun fichier de ce chantier. Tous les autres contrôles passent.

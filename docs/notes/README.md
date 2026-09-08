# Index des notes de travail

Ces notes ne se valent pas. Elles relèvent de quatre espèces, dont **deux seulement doivent
être tenues à jour**. Avant de reprendre une note comme référence, vérifier ici son état.

| État | Signification |
|---|---|
| **vivante** | doit rester juste ; se périme, à revérifier avant de s'y fier |
| **close** | dossier de preuve, figé ; se lit, ne se maintient pas |
| **en cours** | boîte aux lettres qui attend une action et se vide |
| **périmée** | conservée pour trace ; **ne fait plus foi**, voir le renvoi |

## Méthode — vivantes

| Note | Objet | État |
|---|---|---|
| [`outillage-sources.md`](outillage-sources.md) | Recettes et pièges vérifiés : `jort_cache.db`, miroir iort.tn, pist.tn, océrisation, chaîne de rendu. **À lire avant toute recherche documentaire, et à citer dans les briefs d'agents.** | vivante — vérifiée le 08/09/2026 |
| [`prestations-sociales-plan.md`](prestations-sociales-plan.md) | Plan du livre « Prestations sociales » : structure contributif / non contributif, périmètre, déroulé. | vivante |

## Boîtes aux lettres — en cours

| Note | Objet | État |
|---|---|---|
| [`biblio-a-rapatrier.md`](biblio-a-rapatrier.md) | Références à remonter dans Zotero, source canonique. **Tant qu'elles n'y sont pas, `sync_biblio.py` les écrasera.** | en cours — 30 clés en attente |

## Dossiers documentaires — closes

Matière première constituée sur le JORT, avec ses preuves. Se consultent, ne se maintiennent pas.

| Note | Objet | État |
|---|---|---|
| [`fiscalite-irpp-bloc-a-documentation.md`](fiscalite-irpp-bloc-a-documentation.md) | Barème de l'IRPP 1989-2026 : stabilité 1990-2016 attestée, absence de « simplification de 1991 ». | close — 09/2026 |
| [`fiscalite-irpp-assiette-abattements.md`](fiscalite-irpp-assiette-abattements.md) | Assiette par catégorie de revenus, abattements, déductions communes, plafonnement. Porte la **règle de conversion en années de revenus**. | close — 09/2026 |
| [`prestations-contributif.md`](prestations-contributif.md) | Prestations contributives non-retraite ; matrice régime × prestation. | close — 09/2026 |
| [`prestations-assistance.md`](prestations-assistance.md) | PNAFN, aide médicale, AMEN social, allocations non contributives. | close — 09/2026 |
| [`b1-regime-indiciaire-consolidation.md`](b1-regime-indiciaire-consolidation.md) | Régime indiciaire de la fonction publique. | close — 08/2026 |
| [`b2-regime-statutaire-autonome.md`](b2-regime-statutaire-autonome.md) | Corps à statut spécial. | close — 06/2026 |
| [`b3-regime-conventionnel-public.md`](b3-regime-conventionnel-public.md) | Entreprises publiques non financières. | close — 06/2026 |
| [`b4-regime-marche-controle.md`](b4-regime-marche-controle.md) | Entreprises publiques financières. | close — 06/2026 |
| [`ins-fonction-publique-analyse.md`](ins-fonction-publique-analyse.md) | Rapport INS 2010-2021 sur les agents publics. | close — 08/2026 |
| [`perimetre-masse-salariale.md`](perimetre-masse-salariale.md) | Périmètre de la masse salariale publique. | close — 06/2026 |
| [`revue-ajouts-docx-remunerations.md`](revue-ajouts-docx-remunerations.md) | Revue d'un document de l'auteur et suivi d'application. | close — 08/2026 |

## Périmées — ne font plus foi

| Note | Pourquoi | Où regarder |
|---|---|---|
| [`fiscalite-irpp-besoins-documentation.md`](fiscalite-irpp-besoins-documentation.md) | C'était la **commande** passée au documentaliste. Ses questions ont reçu réponse ; elle contient des hypothèses depuis infirmées, dont une pagination erronée. | `fiscalite-irpp-bloc-a-documentation.md` |
| [`fiscalite-irpp-baremes-par-annee.md`](fiscalite-irpp-baremes-par-annee.md) | Tableau de travail bâti sur les paramètres openfisca **avant** dépouillement du JORT. Trois avertissements successifs ont dû y être ajoutés. | `fiscalite-irpp-bloc-a-documentation.md` |

## Ce qui n'a pas sa place ici

Le contenu publié va dans `precis/`. Les valeurs datées vont dans les paramètres
`openfisca-tunisia`, avec leurs métadonnées `reference` — c'est de là que les tableaux du précis
sont générés, pas de ces notes.

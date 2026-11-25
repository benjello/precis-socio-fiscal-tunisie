# RFC 0001 — Le plan de l'ouvrage

- **Statut** : brouillon, ouvert aux relecteurs.
- **Date** : 25/11/2026.
- **Clôture** : date laissée à Mahdi.
- **Annexes engendrées** par `scripts/rfc_plans.py` sur `integration/option-d` :
  - [plan A, par les comptes](plan-a-comptes.md) ;
  - [plan B, thématique](plan-b-thematique.md) ;
  - [correspondance section par section](correspondance-plans.csv).

## 1. Objet et contexte

L'ouvrage documente, texte par texte, les politiques publiques de la Tunisie : impôts, cotisations, prestations, retraites, rémunérations, compensation, finances locales, et désormais les branches de la production. Il est bilingue, libre et en ligne. Il s'adresse à deux lecteurs :
- le citoyen ou le praticien, qui cherche un dispositif : « les retraites », « la TVA », « les allocations familiales » ;
- l'économiste, qui veut remonter de ce dispositif à son effet sur les grands agrégats.

L'ouvrage poursuit un but de long terme : pouvoir **reconstruire la comptabilité nationale** à partir des éléments qu'il décrit et documente. Chaque dispositif y est rattaché à une case des comptes : opération, secteur qui verse, secteur qui reçoit. Un encadré « Dans les comptes » compare le montant de l'ouvrage au chiffre de l'INS, et l'écart est publié. Un pilote existe pour les administrations publiques (le [compte reconstruit](../../precis/fr/compte-apu.qmd)), étendu aux autres secteurs ([les comptes des secteurs](../../precis/fr/compte-secteurs.qmd)).

Deux plans de l'ouvrage sont possibles :
- un **plan par les comptes** (A), qui suit la séquence des comptes nationaux ;
- un **plan thématique** (B), qui suit les questions du lecteur.

Les deux plans sont décrits en détail, jusqu'aux parties qui n'existent pas encore. **On demande aux relecteurs** de choisir le plan de la table des matières, de dire où ranger les cas difficiles et de désigner les parties manquantes prioritaires (questions numérotées au § 6). Aucun déplacement n'est fait tant que la RFC n'est pas close.

## 2. Plan A : par les comptes

Les parties sont les comptes de la séquence du SCN 2008 :
- production ;
- exploitation ;
- affectation des revenus primaires ;
- distribution secondaire ;
- redistribution en nature ;
- utilisation du revenu ;
- capital ;
- compte financier ;
- reste du monde ;
- équilibre des produits ;
- synthèse.

Les chapitres sont les opérations, avec leur code et leur libellé ; les sections sont les dispositifs. La somme des sections d'un chapitre donnerait l'opération, et la somme des chapitres le compte.

L'[annexe A](plan-a-comptes.md) détaille chaque chapitre :
- le montant 2023 de l'opération, tiré des comptes des secteurs de l'INS (éd. 2021-2025) ;
- sa part du compte ;
- son mode de reconstruction possible (loi, source administrative, méthode statistique, à déterminer) ;
- les postes du registre et les sections de l'ouvrage qui s'y rattachent, avec leur statut.

**Totaux, sur 52 chapitres d'opération et propositions** :

| Statut | Chapitres |
|---|--:|
| existe | 20 |
| ébauche | 3 |
| inexistant | 29 |

Parties qu'un ouvrage complet devrait avoir et qui n'existent pas, données comme propositions, sans contenu :
- le compte de redistribution en nature (D.63, publié par l'INS dans un tableau à part) ;
- l'équilibre des produits (TRE) ;
- les soldes et agrégats (B.5, B.6, B.7) ;
- les comptes de patrimoine (l'INS ne publie que des comptes de flux) ;
- les comptes régionaux.

## 3. Plan B : thématique en sept parties

1. Le cadre.
2. La production.
3. L'emploi et les revenus.
4. Les prélèvements.
5. La protection sociale et les services publics.
6. La consommation, l'investissement et les échanges.
7. Les finances publiques et la vue d'ensemble.

Les volumes restent entiers, avec leurs chapitres. L'[annexe B](plan-b-thematique.md) donne chaque chapitre et son statut, ainsi que les volumes proposés qui n'existent pas.

**Totaux, sur 188 entrées** :

| Statut | Entrées |
|---|--:|
| existe | 128 |
| ébauche | 43 |
| à rédiger | 7 |
| inexistant (propositions) | 10 |

Les propositions de volumes inexistants sont : les services (commerce, tourisme, télécommunications), le secteur financier, les revenus des indépendants, les revenus du capital, le chômage (par renvoi), la pauvreté et les niveaux de vie, la monnaie et le crédit, le patrimoine public. Le budget de l'État, la dette et les comptes reconstruits existent déjà comme pages générales.

Six cas sont discutés :

| Volume | Options | Proposition |
|---|---|---|
| Rémunérations dans le secteur public | partie 3 (revenus du travail) ou partie 7 (finances publiques) | partie 3, avec un renvoi depuis la partie 7 |
| Compensation | partie 5 (protection sociale) ou partie 2 (prix administrés de l'énergie) | partie 5, avec des renvois depuis l'énergie |
| Caisses de sécurité sociale | partie 4 (avec les cotisations) ou partie 5 (avec les prestations) | partie 5 |
| Environnement | partie 2 ou partie 5 (services publics : assainissement, déchets) | partie 5 |
| Entreprises publiques | volume entier en partie 2 ; ou scindé : statut et relation financière avec l'État en partie 7, activité par branche en partie 2 | à scinder, plus tard (34 sections, 31 renvois) |
| Transport et services | partie 2, dans un ensemble « services » à créer | partie 2 |

## 4. Correspondance et coût

La [table de correspondance](correspondance-plans.csv) donne, pour chacune des 979 sections existantes (volumes et pages générales), sa place dans le plan A et dans le plan B. Dans le plan A :
- 255 sections restent « à déterminer » ;
- 274 relèvent du cadre institutionnel, pages générales comprises.

| | Plan A | Plan B |
|---|--:|--:|
| Sections qui changent de volume | 314 | 0 (34 si l'on scinde les entreprises publiques) |
| Chapitres à scinder | 13 | 0 |
| Renvois touchés | 461 | 0 (31) |
| Fichiers arabes concernés | 42 | 0 |

Ce que chaque plan apporte, et à qui :
- **Plan A** : la somme des sections donne les comptes ; les cases vides se voient dans la table des matières elle-même. Il sert l'économiste et le comptable national, mais déroute le lecteur qui cherche un dispositif.
- **Plan B** : le lecteur trouve « les retraites » là où il les cherche, et presque rien ne bouge. Les comptes restent une couche de lecture : les encadrés « Dans les comptes » et les comptes reconstruits.

## 5. Voie mixte

Une voie mixte : un plan pour la table des matières, l'autre comme **sommaire engendré**. On peut aussi engendrer un troisième sommaire **par situation de vie** : famille, études, travail, chômage, maladie, retraite, pauvreté, logement.
- Le sommaire « par les comptes » s'engendre déjà depuis le registre des postes (`precis/fr/postes-comptables.csv`) ; il suffit d'y ajouter une ligne par section domicile.
- Le sommaire thématique demande une table `precis/fr/parties.yml` (volume → partie, ordre).
- Le sommaire par situation de vie demande une table `sections-situations.csv` (section → situations), saisie à la main.

Les encadrés « Dans les comptes » et les blocs de passage déjà en place valent pour les trois sommaires.

## 6. Questions aux relecteurs

1. **Table des matières** : (a) plan A, par les comptes ; (b) plan B, thématique ; (c) voie mixte : plan B pour la table des matières, plan A comme sommaire engendré ; (d) autre.
2. **Rémunérations publiques** : (a) emploi et revenus ; (b) finances publiques.
3. **Compensation** : (a) protection sociale ; (b) production (énergie).
4. **Caisses de sécurité sociale** : (a) prélèvements ; (b) protection sociale.
5. **Environnement** : (a) production ; (b) services publics.
6. **Entreprises publiques** : (a) volume entier ; (b) scindé entre statut (finances publiques) et activité (branches).
7. **Parties manquantes prioritaires** (trois au plus) : services ; secteur financier ; monnaie et crédit ; revenus des indépendants ; revenus du capital ; pauvreté et niveaux de vie ; redistribution en nature ; équilibre des produits ; comptes régionaux ; patrimoine.
8. **Niveau de détail comptable** dans les chapitres : (a) un encadré « Dans les comptes » par dispositif ; (b) en plus, un tableau « qui verse à qui » par chapitre ; (c) en plus, le passage chiffré du budget aux comptes.
9. **Sommaire par situation de vie** : (a) oui ; (b) non.
10. **Titres** : les titres des sept parties du plan B conviennent-ils ? Proposez-en d'autres le cas échéant.

## 7. Comment répondre

On propose d'ouvrir **un fil de discussion par question** sur le dépôt, numéroté comme au § 6, et de clore à une date que fixera Mahdi. Rien n'est ouvert ni publié tant qu'il n'en a pas décidé le lieu. En attendant, les remarques se font en commentaire de la demande de fusion de cette RFC.

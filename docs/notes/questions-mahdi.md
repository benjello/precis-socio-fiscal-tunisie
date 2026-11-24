# Décisions qui reviennent à Mahdi

Ouvert le 24/11/2026, au fil du plan par opération (`docs/notes/plan-par-operations.md`). Chaque entrée donne la question, les options, la recommandation et ce que l'attente bloque. Quand l'option recommandée est réversible sur une branche, elle est **appliquée par défaut, à confirmer** ; sinon, rien n'est fait.

## M1. Le volume de la fiscalité dans un plan par opération
- **Question** : faut-il scinder le volume (62 sections déplacées selon la mesure) entre D.2, impôts sur les produits (partie II), et D.5, impôts sur le revenu (partie III), ou le garder entier ?
- **Options** :
  - (a) scinder en deux volumes ;
  - (b) garder le volume, avec des parties internes par opération ;
  - (c) garder tel quel.
- **Recommandation** : (b). Le lecteur garde un seul livre de la fiscalité, et la somme par opération reste lisible.
- **Bloque** : la réorganisation de la fiscalité. La proposition sera faite sur une branche à part, non fusionnée.

## M2. Taxe de formation professionnelle et FOPROLOS (D.29)
- **Question** : ces deux prélèvements doivent-ils quitter le volume des cotisations ?
- **Options** :
  - (a) les déplacer vers les fonds spéciaux du Trésor (fiscalité) ;
  - (b) les déplacer vers un futur chapitre D.29 ;
  - (c) les laisser, avec le bloc « Dans les comptes ».
- **Appliqué par défaut, à confirmer** : (c). Les deux sections portent le bloc et le renvoi au compte, sans déplacement.
- **Bloque** : rien.

## M3. Les 176 sections sans opération
- **Question** : où ranger les sections qui ne se rattachent à aucune opération (temps de travail, rupture du contrat, logement social, offices, redevances…) ?
- **Options** :
  - (a) un « cadre institutionnel » en tête de chaque partie ;
  - (b) une partie 0 commune.
- **Recommandation** : (a).
- **Bloque** : la réorganisation du marché du travail et des entreprises publiques. Une proposition sera faite sur une branche à part, non fusionnée.

## M4. Les loyers et redevances (D.45)
- **Question** : faut-il créer un chapitre pour D.45 (2 227,8 MD reçus par les administrations publiques en 2023), qu'aucune section ne traite ?
- **Recommandation** : oui, dans un futur chapitre des revenus de la propriété.
- **Bloque** : la couverture de D.4.

## M5. Les pages de synthèse par institution
- **Question** : où placer les pages de synthèse des institutions (caisses, compensation, entreprises publiques, collectivités) ?
- **Options** :
  - (a) dans le volume actuel de chaque institution ;
  - (b) regroupées dans la partie 0.
- **Recommandation** : (a), qui ne demande aucun déplacement.
- **Bloque** : la scission des 13 chapitres « à cheval ».

## M6. La date de consultation des éditions des comptes de la nation
- **Question** : aucune liste ne donne la date de consultation des 15 éditions. Faut-il la relever (date de téléchargement des fichiers) ou la laisser vide ?
- **Recommandation** : la laisser vide tant qu'aucune trace n'existe, et la noter à chaque nouveau téléchargement.

## M7. La relecture des bases 1997 et 1983
- **Question** : faut-il poursuivre la relecture page par page des 130 équilibres restants de la base 1997, ou fusionner #152 en l'état (dépôt de données), les écarts restant listés ?
- **Recommandation** : fusionner en l'état, puisque les écarts sont listés et non masqués ; la relecture continuera dans une branche ultérieure.

## M8. Les fusions refusées dans le dépôt de données
- **Question** : #153 (relecture du TOF) et #154 (catalogue) attendent une fusion sur main, que la protection du poste a refusée. Faut-il ajouter la règle `Bash(gh pr merge:*)`, ou fusionner toi-même ?
- **Bloque** : #155 et #156, empilées sur #153.

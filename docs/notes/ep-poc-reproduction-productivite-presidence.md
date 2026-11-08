# POC — reproduire les chiffres du rapport présidentiel (Unité de Suivi) à partir de nos sources

**Date :** 6 novembre 2026. **Statut :** preuve de concept, **non terminée** côté productivité.
**But :** vérifier qu'on **reproduit** les chiffres du rapport de la Présidence (Livre blanc 2018 / Unité de suivi du système de productivité) **à partir de nos sources publiques** (états financiers déposés), pour (a) valider la chaîne données et (b) préparer la **productivité** (valeur ajoutée, VA/agent).

## 1. Revenus 2014 — reproduits exactement (chaîne données validée)
Cible = rapport présidentiel (« 16 premières EP, revenus 2014 »). Source = états financiers publics 2014.

| Entreprise | Présidence | Nos sources publiques 2014 | Écart |
|---|---|---|---|
| STEG | 3 736 | 3 736 001 807 DT = **3 736,0 MD** | 0 (exact) |
| Tunisair | 1 149,6 | 1 149 607 KDT = **1 149,6 MD** (individuel) | 0 (exact) |
| ETAP | 2 152,7 | états financiers : « revenus 2014 **2153 MDT** » | ≈ 0 |
| STB | 499,7 | TOTAL PRODUITS D'EXPLOITATION BANCAIRE = **499 697 KDT** | 0 (exact) |
| BNA | 596,8 | TOTAL PRODUITS D'EXPLOITATION BANCAIRE = **596 755 KDT** | 0 (exact) |
| **STIR** | 4 495,7 | **—** (pas d'états financiers publics) | **lacune** |

- Pour les **banques**, le « revenus » de la Présidence = **total des produits d'exploitation bancaire** (pas le PNB).
- **STIR** : ne publie pas d'états financiers (pas cotée). Seule donnée secondaire trouvée (un PFE) : CA 2014 ≈ 3 478 MD, **très loin** des 4 495,7 MD du rapport — probablement CA (ventes) vs « revenus » incluant la compensation carburants, ou erreur. **Non recoupable** : pour les EP qui ne publient pas, le rapport présidentiel est la **seule** source, et il n'est même pas vérifiable. Lacune consignée, **jamais** inventée.

## 2. Valeur ajoutée — méthode validée, pas généralisée
- POC : **Tunisair 2022 consolidé** (par nature) → **VA ≈ 331 MD** < masse salariale **347 MD** → **EBE négatif**.
- Confirme : la VA se calcule en **production − consommations intermédiaires** (≠ coût salarial de la fonction publique) ; mais, les EP étant déficitaires, **salaires ≥ VA** et l'EBE est négatif.

## 3. Ce qui reste (le cœur « productivité », NON FAIT)
1. Généraliser **revenus → VA (production − CI)** et **VA/agent** sur l'ensemble des EP dont on a les états financiers.
2. **Reproduire le tableau de productivité** du rapport présidentiel (et le vérifier ligne par ligne).
3. **Étendre aux exercices récents** (le rapport s'arrête à 2014).
4. **Combler STIR** : états financiers via la **Cour des comptes** (qui l'audite) ou demande directe.

## Garde-fous
- **Un sourçage par chiffre** ; un chiffre non lu reste non écrit ; une lacune (STIR) est **consignée, jamais interpolée**.
- Sources : corpus `tunisia-data` (`data/raw/entreprises-publiques/bvmt-etats-financiers/`, `minenergie/steg/etats-financiers/`), rapports annuels ETAP.

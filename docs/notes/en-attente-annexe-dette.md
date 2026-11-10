# Chantier annexe dette publique — CLOS

Chantier `chantier/annexe-dette-publique` **terminé, fusionné et déployé** (10 nov. 2026) :

- **Précis** : PR #785 (annexe + chaîne de données + garde-fou + glossaire) puis #787 (correctif
  jargon), fusionnées sur `master`.
- **Données** : `tunisia-data` PR #140 (extracteurs, catalogue, index des tableaux BCT, playbook de
  recherche de données) fusionnée sur `main`.
- **En ligne** : `https://benjello.github.io/precis-socio-fiscal-tunisie/fr/annexe-dette-publique.html`
  (vérifié : correctif jargon présent, figure composition par devise avec estimation hachurée présente).

Ce qu'il livre : annexe `precis/fr/annexe-dette-publique.qmd` (~13 sections, 12 figures), chaîne
**données → `tunisia-data` → cache → figures**, garde-fou `scripts/check_dette_coherence.py` intégré
à `verifier.sh`, carte des périmètres `docs/notes/dette-concordance.md`, 13 termes de glossaire
bilingues (statut `provisoire`), règle « séries longues homogènes / approximation sourcée » dans la
fiche documentaliste.

**Les restes ouverts** (données à sourcer, objectif pub 107 2013-2022, confirmations arabes, question
architecte sur le glossaire des annexes racine, sources économiques à verser) sont dans
**`docs/notes/backlog-dette.md`** — plus rien ne vit uniquement dans cette note de session.

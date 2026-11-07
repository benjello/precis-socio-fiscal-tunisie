# Annexe globale des sources de données — design

**Note de design du 5 novembre 2026** (agent Plan). Objectif : une **annexe globale « sources de
données »**, commune à tout le précis, à laquelle **chaque livre renvoie**. Portée : les **supports
de données CHIFFRÉES** (rapports, publications statistiques, annexes chiffrées de lois de finances si
on en tire des chiffres, bases FMI/BM/OCDE…). **Exclure le texte législatif pur** (JORT) : il reste
en bibliographie. Impératif : **traçable et facile à mettre à jour** — une source se met à jour en un
seul endroit, et on sait quels chiffres/livres en dépendent.

## Où vit le registre : ne rien dupliquer, recomposer une vue
Trois couches existantes :
- **`precis/fr/references.json`** — identité publique (items CSL : `id`, `type`, `title`, `URL`,
  `author/publisher`, `note`). Le champ **`type`** tranche : `dataset`/`report`/`webpage` = support
  chiffré candidat ; **`type == legislation` = JORT, exclu**.
- **`tunisia-data/catalog.yml`** — spine de traçabilité par série (`sources` [clés],
  `fetch`/`build`/`raw`/`output`, `unite`, `perimetre`, `caveats`, `fiche`, `licences`). D'où se
  lisent la cadence/fraîcheur et le « comment rafraîchir » (module `fetch`).
- **`tunisia-data/sources/*.md`** — prose de provenance (date de consultation, pièges).
La clé de citation est l'entité-source unique ; l'annexe est une **projection engendrée**.

## Organisation : THÉMATIQUE — par type de source, puis par source
L'annexe est structurée en deux niveaux : **une sous-section par type (famille) de source**, et à
l'intérieur, **une entrée par source**. Familles pressenties (à ajuster) : *Rapports du ministère des
Finances* (rapport EP, dette publique, transferts et garanties…) ; *Annexes chiffrées des lois de
finances* ; *Publications statistiques* (INS — comptes de la nation…) ; *États financiers
d'entreprises* (Bourse/CMF, Registre national) ; *Cour des comptes* (clôture du budget) ; *Caisses
sociales* (CNSS, CNAM, CNRPS) ; *Banque centrale (BCT)* ; *Bases internationales* (FMI, Banque
mondiale, OCDE, BAD).

La **famille** d'une source est un champ à poser une fois et au même endroit que le reste (de
préférence dans `catalog.yml`, ou une petite table `producteur → famille` tenue à un seul endroit),
jamais recopiée. L'ordre des familles est fixe (le plus officiel/central d'abord) ; l'ordre interne
par producteur puis titre.

## Modèle d'une entrée (tous champs dérivés)
`famille` (titre de sous-section), `cle` (ancre `#src-<cle>`), `producteur`, `titre`, `acces` (URL
publique), `couvre` (perimetre), `periode`, `unite`, `reserves` (caveats), `cadence/fraicheur`,
`rafraichir` (module `fetch`/portail — **en commentaire de code, pas en clair**), `livres_dependants`
(index inverse).

## Génération et placement
Réutiliser le patron de **`precis/fr/annexe-pib.qmd`** (page commune aux volumes, ancres stables,
matière dans `docs/notes/`). Créer **`precis/fr/annexe-sources.qmd`** (+ `precis/ar/…`), engendrée par
un script type `scripts/`, sur le modèle de `figtools.source_details` (`scripts/figtools.py:427`).
Algorithme : (a) scanner tous les `precis/fr/**/figdata/*.csv.yml`, collecter l'union des clés
`sources` ; (b) résoudre dans `references.json`, **écarter `type: legislation`** ; (c) enrichir via
`catalog.yml`/fiche, dont la **famille** ; (d) **grouper par famille**, puis émettre une sous-section
par famille et une entrée par clé. **Noms de CSV : jamais dans le texte publié**
(au plus en commentaire de code).

## Renvois et traçabilité
Chaque annexe de livre et chaque onglet « 🔗 Sources » de figure (`figtools.source_details`) pointe
vers `#src-<cle>` au lieu de re-détailler. **Index inverse** clé-source → {livres, figures}, engendré
depuis les manifestes figdata ; une source changée → annexe et index régénérés. Signalé (non
auto-corrigé) : une clé citée dans un figdata absente de `references.json`, ou de `type` inattendu.

## Étapes (segmentables)
1. Script scanner + filtre `type != legislation` (lecture seule, inventaire).
2. Générateur `annexe-sources.qmd` FR, ancres `#src-<cle>`.
3. Brancher l'onglet Sources de `figtools` sur les ancres.
4. Migrer un livre pilote (fiscalité) : remplacer ses descriptions par renvois ; valider.
5. Dérouler livre par livre, puis AR.

Pièges : ne pas dupliquer `references.json`/`catalog.yml` ; ne jamais réexposer les noms CSV ;
exclure strictement le JORT ; plusieurs `references.json` par livre (cf. en-tête d'`annexe-pib.qmd`).

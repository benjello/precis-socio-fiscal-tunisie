# En attente — relais de session du 11 novembre 2026

Point d'arrêt de la session d'orchestration des 10-11 novembre 2026 (exploration des volumes
peu fournis, plans des nouveaux livres, densification santé/caisses/éducation, livre transport,
openfisca 0.163, release 1.30.0). Tout ce qui suit attend le propriétaire ou une reprise.

## À relire puis committer (dépôt principal, non suivi)

- `docs/notes/chantier-architecture-2026-11.md` — note de doctrine (niveau « section »,
  partie I, fiscalité en quatre volumes) ; décisions déjà consignées dedans : agriculture en
  partie IV pour l'instant (11/11), environnement = tutelle du ministère + l'eau (10/11 soir).
- `docs/notes/agriculture-plan-livre.md`, `environnement-plan-livre.md` (le plan transport,
  enrichi par son chantier, est déjà sur master).
- `docs/notes/etat-volumes-peu-fournis-2026-11-10.md` (corrigée : série diplômés, glossaire santé).
- `docs/notes/openfisca-ticket-hygiene-yamllint.md` — brouillon de ticket openfisca (quatre
  fichiers YAML non conformes sur master), à ouvrir sur accord.
- `.gitignore` — six pages racine (comment-lire, parcours-atmp, etc.).
- La présente note.

## Chantiers ouverts

- **Agriculture** (`precis-wt-agriculture`) : dégelé le 11 novembre (« fusionne tout ») ;
  master fusionné, conflits résolus par structure, poussé ; **bloquant : 107 citations non
  résolues** (versement bibliographe manquant) — session relancée dessus ; PR et mise en
  ligne quand `verifier.sh agriculture` rend 0 citation non résolue. Partie IV actée pour
  l'instant ; frontière eau d'irrigation à confirmer.
- **Éducation** : FAIT — PR #804 fusionnée le 11 novembre par sa session ; worktree, branche
  et onglet nettoyés.
- **Environnement** : FAIT — PR #803 fusionnée le 11 novembre (feu vert donné), livre en
  ligne ; worktree, branche et onglet nettoyés. Reste au backlog : clés CSL « Environnement »
  à rapatrier dans Zotero ; frontière eau d'irrigation à confirmer.

## Release et CI

- **Release 1.31.0 : FAITE** (11 novembre, CHANGELOG complété à la main — transport #796 et
  caisses #798 ajoutés). La release suivante portera l'environnement (#803).
- **Leçon durable** : les commits `NEW:`/`FIX:`/`IMPROVE:` (convention interne) sont
  invisibles pour release-please, qui lit `feat:`/`fix:`/`docs:`. Remèdes possibles :
  configurer release-please pour les types internes, ou titrer les PR en conventionnel
  (la fusion merge conserve les commits de branche). À trancher.

## Reports éditoriaux (déjà routés, rappel)

- **relecteur-ar** : libellés arabes des tableaux AT/MP engendrés ; 8 termes AR `provisoire`
  du glossaire santé (dont deux traductions par analogie) ; textes AT/MP à relire à l'image.
- **économiste** : « Ce qu'en dit l'économie » manquante aux volumes caisses et cotisations ;
  santé différée (`docs/notes/en-attente-sante-densification.md`).
- **documentaliste** : caisses — comptes par régime post-2004 (lacune de fond), soldes CNSS
  2005-2008/2011/2014, composition S1314 ; éducation — bourses 1982 (édition arabe), OCR des
  sommaires arabes, séries du ministère pour le chapitre « résultats ».
- **rédacteur** : montants en dinars des assiettes forfaitaires AT/MP (TODO au chapitre) ;
  cosmétique `formate_taux` (« 0,8 % » vs « 0,80 % » du décret).

## Fait et fusionné (pour mémoire, 10-11 novembre)

Précis : #794 santé, #795+#797 éducation, #796 transport (livre en ligne), #798+#801 caisses
(longue période, quatre séries), #799 tableaux AT/MP, release v1.30.0 (CHANGELOG complété à la
main). Openfisca : #523-#525 fusionnées, 0.163 sur PyPI, issue #471 fermée, exigence de revue
retirée de la protection de master. Worktrees et branches des chantiers clos supprimés.

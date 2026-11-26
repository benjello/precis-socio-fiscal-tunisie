# Déplacer une section ou un chapitre d'un volume à un autre

Procédure pour les déplacements de la restructuration (voir `precis/fr/principes-structure.qmd`).
Le français seul se déplace : l'arabe suit par la CI.

1. **Plan d'abord.** Le déplacement figure dans un plan validé par le propriétaire (règle « plan
   avant exécution ») ; on ne déplace que vers un volume qui existe.
2. **Repérer ce qui pointe vers la section** :
   `grep -rn '#<ancre>' precis/fr --include=*.qmd` et
   `grep -rn '_<chapitre>.html' precis/fr --include=*.qmd`.
3. **Déplacer le texte en gardant l'ancre** (`{#sec-…}`) : les liens depuis les autres volumes ne
   changent que de chemin, pas d'identifiant. Un chapitre entier garde son nom de fichier.
4. **Emporter ce dont le texte dépend** :
   - clés citées : les copier dans le `references.json` du volume d'arrivée, en français et en
     arabe (ces fichiers se tiennent à la main dans les deux langues) ;
   - figures : le script sous `figures/` et ses données sous `figdata/` ;
   - tableaux engendrés : déplacer l'appel au générateur, jamais le fichier sous `tables/` ;
   - inclusions (`{{< include >}}`) et notions du glossaire propres au volume.
5. **Laisser un renvoi** dans le volume de départ : une ou deux phrases et un lien relatif
   `../<volume>/_<chapitre>.html#<ancre>` (règle « un volume à cheval reste entier, les autres
   parties y renvoient »).
6. **Câbler les chapitres** : listes `chapters` des `_quarto.yml` français, puis
   `uv run python scripts/arabe_cablage.py` (jamais de `.qmd` écrit sous `precis/ar/`).
7. **Remplacer les liens en masse** quand ils sont nombreux :
   `uv run python scripts/remplacer.py '<motif>' '<remplacement>' 'precis/fr/**/*.qmd'`, relire la
   liste des occurrences, puis relancer avec `--appliquer`.
8. **Vérifier** : `scripts/verifier.sh <volume-départ> <volume-arrivée>` ; il contrôle les liens
   entre volumes (`scripts/verifier_liens_entre_volumes.py`) et rend les deux volumes.
9. **Mettre à jour la correspondance** avec la séquence des comptes
   (`scripts/generate_correspondance_comptes.py`) si la section change de domicile.

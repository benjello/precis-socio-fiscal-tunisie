# Créer un volume

Un volume neuf naît en français ; sa traduction vient plus tard, par la CI.

1. **Instruction** : note de plan sous `docs/notes/<volume>-plan-livre.md` (domicile dans la
   séquence des comptes, chapitres, sources tunisiennes disponibles), validée avant tout `.qmd`.
2. **Montage** : copier `precis/fr/environnement/_quarto.yml` (volume récent, en français seul) et
   changer `title`, `repo-subdir` et la liste `chapters` ; créer `index.qmd` et un
   `references.json` vide (`{"items": []}`).
3. **Enregistrer le volume** là où les volumes sont énumérés :
   - `build.sh`, tableau `BOOKS` ;
   - `scripts/build_glossary.py`, liste des livres ;
   - `scripts/verifier_livres.py`, `LIVRES` ;
   - `precis/fr/index.qmd`, liste des volumes, avec la mention « n'existe pour l'instant qu'en
     français » tant que la traduction n'est pas livrée ;
   - `scripts/generate_correspondance_comptes.py`, `RATTACHEMENT`, pour les opérations qu'il porte.
4. **Glossaire** : `uv run python scripts/build_glossary.py` engendre `_glossaire.qmd` et les
   infobulles ; ne pas les écrire.
5. **Vérifier** : `scripts/verifier.sh <volume>`, puis ouvrir le rendu.
6. **Arabe** : ne rien créer sous `precis/ar/` ; voir `docs/conventions/traduction-arabe.md`.

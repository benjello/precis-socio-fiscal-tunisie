# ADR — Architecture données / figures / traçabilité

Statut : **acté** (2026-06-09).

## Décision
Tout chiffre et toute figure du précis sont **régénérables** depuis une source canonique,
et **tracés** via une clé de citation unique pilotée par **Zotero du précis**.

## Frontière (deux couches)
| | `tunisia-data` (entrepôt) | `precis` (publication) |
|---|---|---|
| Contenu | **tout le raw** + fetchers + **séries** (processed, indexées) | **figures + figdata + site**, par livre |
| Forme | **paquet Python `tunisia_data`** (pas de submodule) | dépend du paquet (chemin éditable) |
| API | `load(id)`, `meta(id)`, CLI `trace/uses/validate` | chunks Quarto appelant le paquet |
| Index | `catalog.yml` | `figdata/*.csv.yml` (provenance) |

Le raw n'est pas forcément commité (volumineux) mais **toujours régénérable** (fetcher +
catalogue d'URLs). Les **figures ne sont jamais à la racine** : elles vivent dans
`precis/fr/<livre>/figures/`, leur data téléchargeable dans `precis/fr/<livre>/figdata/`.

## Chaîne de traçabilité
```
Source canonique ─tunisia_data─► SÉRIE (catalog.yml, sourcée)
                                   └─precis/<livre>/figures─► FIGDATA (sourcé) ─► FIGURE ─► SITE
```
- `catalog.yml` lie chaque série à ses **clés de citation Zotero**, son fetch, son build, sa sortie, ses caveats.
- `figdata/<fig>.csv` porte un **en-tête de provenance** (séries, clés `@…`, fiches, hypothèses, date) + un sidecar `.yml` → téléchargeable et **citable seul**.
- `precis/scripts/figtools.py` génère la ligne « Source » et l'en-tête **depuis `meta()`** — jamais à la main.

## Citations
**Tout passe par Zotero du précis** : sources de données = entrées CSL `dataset` ;
législation (décrets) = `legislation.bib` via JORT. `sync_biblio.py` les rapatrie. Les clés
référencées dans `catalog.yml` qui n'existent pas encore dans Zotero sont signalées au
bibliographe (inbox `docs/notes/biblio-a-rapatrier.md`).

## Insertion d'une figure dans un livre (chunk Quarto)
```{python}
#| label: fig-masse-salariale
#| fig-cap: "Poids de la masse salariale publique, 1990-2025."
#| echo: false
import sys; sys.path.insert(0, ".")
from figures import masse_salariale as ms
ms.prepare(generated="{{< meta date >}}")   # écrit figdata/ sourcés
ms.fig_A()
```
Puis le bouton de téléchargement (le site sert le figdata sourcé, pas le raw) :
```python
from figtools import download_button
download_button("figdata/fig_A_masse_salariale.csv")
```

## Build / CI — autonomie de diffusion (décidé 2026-06-09)
Le build du site est **autonome** : il ne dépend pas du repo privé `tunisia-data`.
- Accès aux séries via **une seule couche**, `scripts/figtools.py` :
  `series(id)` / `meta(id)` utilisent l'entrepôt s'il est importable (dev local),
  sinon retombent sur un **snapshot versionné** `precis/_seriescache/` (un CSV par
  série + `catalog.snapshot.yml` pour la provenance). Les modules figures n'importent
  **jamais** `tunisia_data` directement.
- `tunisia-data` n'est **pas** déclaré dans le pyproject du précis (une source path
  épinglée dans `uv.lock` ferait échouer `uv sync` en CI, repo privé absent — vérifié).
- Régénération du snapshot (étape « produire »), avec l'entrepôt présent :
  `uv pip install -e ../tunisia-data` puis
  `PYTHONPATH=scripts uv run python -c "import figtools; figtools.refresh_cache(*ids)"`,
  enfin commit de `precis/_seriescache/`. À refaire quand une série change.
- `tunisia-data` (entrepôt) : `make data` (fetch+build), `tunisia-data validate`.
- CI/Pages (`deploy.yml`) : `uv sync` (cœur, sans entrepôt) → `build.sh` rend le site
  depuis le snapshot. Les PNG de figures sont régénérés au render (non committés).

## Conséquences
- Le précis ne contient **pas** de données brutes ; il **produit** ses figures depuis le paquet.
- Un fichier téléchargé reste sourcé et reproductible. La base/le périmètre sont toujours
  affichés (tirés de la provenance) — évite les faux écarts (cf. base PIB 2010/2015).

#!/usr/bin/env bash
# build.sh — Convert and render all Quarto précis and assemble local site.
#
# Usage:
#   ./build.sh            # full build (HTML + PDF) — le PDF est le défaut
#   ./build.sh --no-pdf   # skip PDF rendering
#   ./build.sh --list-units          # liste JSON des livres (un par langue et par livre)
#   ./build.sh --only fr/informel    # rend UN livre (ni pages générales, ni assemblage)
#   ./build.sh --only fr/informel --pdf-only   # le PDF de ce livre seulement
#   ./build.sh --assemble            # pages générales + assemblage, sans rendre de livre
#   ./build.sh --help     # affiche l'aide
#
# Attention : une option inconnue sort en code 2. Si vous appelez ce script
# dans un pipeline (« ./build.sh | tail »), le code de retour du pipeline est
# celui de la dernière commande : utilisez « set -o pipefail » ou testez
# "${PIPESTATUS[0]}" pour ne pas masquer l'échec.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRECIS_DIR="$ROOT_DIR/precis"
LOCAL_SITE="$ROOT_DIR/local_site"

LANGUAGES=(fr ar)
BOOKS=(prestations_sociales retraites fiscalite remunerations_publiques cotisations_sociales caisses finances_locales marche_travail compensation entreprises_publiques sante education transport informel)
# Pages générales du site, posées directement sous precis/<langue>/ et rendues une à une.
PAGES=(index comment-lire comment-constitue a-propos principes-structure annexe-pib annexe-budget-etat annexe-dette-publique annexe-sources annexe-comptes-nation index-institutions parcours-atmp correspondance-instruments)

DO_PDF=true
ONLY_UNIT=""
PDF_ONLY=false
ASSEMBLE_ONLY=false
LIST_UNITS=false

usage() {
  cat <<'USAGE'
build.sh — rend tous les précis Quarto et assemble le site local.

Usage :
  ./build.sh            build complet (HTML + PDF)
  ./build.sh --no-pdf   rend le HTML seul, sans PDF
  ./build.sh --list-units          liste JSON {"include":[…]} des livres à rendre
  ./build.sh --only fr/informel    rend UN livre, sans pages générales ni assemblage
  ./build.sh --only fr/informel --pdf-only   le PDF de ce livre seulement (échec toléré)
  ./build.sh --assemble            pages générales et assemblage, sans rendre de livre
  ./build.sh --help     affiche cette aide

Le workflow `.github/workflows/rendre.yml` rend un livre par job (`--only`) puis assemble
le site (`--assemble`) : les livres se rendent en parallèle et un livre inchangé n'est pas
rendu de nouveau.

Le PDF est produit PAR DÉFAUT ; il n'existe pas d'option « --pdf ».

Sortie : local_site/ à la racine du dépôt.
Prévisualisation : cd local_site && uv run python -m http.server 8765

Codes de retour :
  0  succès
  1  au moins un livre n'a pas pu être rendu
  2  option invalide
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-pdf)     DO_PDF=false ;;
    --list-units) LIST_UNITS=true ;;
    --assemble)   ASSEMBLE_ONLY=true ;;
    --pdf-only)   PDF_ONLY=true ;;
    --only)
      shift
      if [[ $# -eq 0 || "$1" != */* ]]; then
        echo "build.sh : --only attend « langue/livre » (par ex. fr/informel)." >&2
        exit 2
      fi
      ONLY_UNIT="$1" ;;
    --help|-h)    usage; exit 0 ;;
    *)
      echo "build.sh : option inconnue « $1 »." >&2
      echo >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

# Un livre arabe dont `index.qmd` manque n'est pas encore traduit : il n'est ni rendu ni listé.
unit_exists() {
  local lang="$1" book="$2"
  [[ -d "$PRECIS_DIR/$lang/$book" ]] || return 1
  if [[ "$lang" == "ar" && ! -f "$PRECIS_DIR/$lang/$book/index.qmd" ]]; then
    return 1
  fi
  return 0
}

if $PDF_ONLY && [[ -z "$ONLY_UNIT" ]]; then
  echo "build.sh : --pdf-only s'emploie avec --only." >&2
  exit 2
fi

if [[ -n "$ONLY_UNIT" ]] && ! unit_exists "${ONLY_UNIT%%/*}" "${ONLY_UNIT#*/}"; then
  echo "build.sh : « $ONLY_UNIT » n'est pas un livre à rendre (voir --list-units)." >&2
  exit 2
fi

if $LIST_UNITS; then
  sep=""
  printf '{"include":['
  for lang in "${LANGUAGES[@]}"; do
    for book in "${BOOKS[@]}"; do
      if unit_exists "$lang" "$book"; then
        printf '%s{"unite":"%s/%s","lang":"%s","book":"%s"}' "$sep" "$lang" "$book" "$lang" "$book"
        sep=","
      fi
    done
  done
  printf ']}\n'
  exit 0
fi

# ── Python / Quarto environment ────────────────────────────────────────────────
if [[ -z "${QUARTO_PYTHON:-}" ]]; then
  VENV_PYTHON="$ROOT_DIR/.venv/bin/python3"
  if [[ -x "$VENV_PYTHON" ]]; then
    export QUARTO_PYTHON="$VENV_PYTHON"
    echo "[build] Using QUARTO_PYTHON=$QUARTO_PYTHON"
  else
    echo "[build] Warning: .venv not found; Jupyter notebooks may fail."
  fi
fi

if [[ -z "$ONLY_UNIT" ]]; then
  rm -rf "$LOCAL_SITE"
  mkdir -p "$LOCAL_SITE"
fi

# ── Step 0: Regenerate the bilingual glossary from precis/glossaire.yml ─────────
if [[ -f "$ROOT_DIR/precis/glossaire.yml" ]]; then
  echo "[build] Regenerating bilingual glossary..."
  if (cd "$ROOT_DIR" && uv run python scripts/build_glossary.py); then
    echo "[build] ✓ Glossary regenerated"
  else
    echo "[build] ⚠ Glossary generation failed; using committed files."
  fi
fi

# ── Step 1: Render each language and book ──────────────────────────────────────
FAILED_BOOKS=()

for lang in "${LANGUAGES[@]}"; do
  echo ""
  echo "════════════════════════════════════════"
  echo " Processing Language: $lang"
  echo "════════════════════════════════════════"

  LANG_DIR="$PRECIS_DIR/$lang"
  if [[ ! -d "$LANG_DIR" ]]; then
    echo "[build] Skipping language $lang: directory not found."
    continue
  fi

  # ── Render the general pages for the language ─────────────────────────────
  # Une page générale NEUVE n'a pas encore d'arabe, pour la même raison qu'un livre neuf
  # (voir plus bas) : on saute la page arabe absente, en le disant. L'accueil, lui, existe
  # dans les deux langues — son absence reste une erreur.
  for page in "${PAGES[@]}"; do
    [[ -n "$ONLY_UNIT" ]] && break  # un seul livre demandé : pas de pages générales
    if [[ "$page" != "index" && "$lang" == "ar" && ! -f "$LANG_DIR/$page.qmd" ]]; then
      echo "[build] ⚠ $page ($lang) : traduction pas encore livrée — page sautée."
      continue
    fi
    echo "[build] Rendering page $page for $lang..."
    if (cd "$LANG_DIR" && uv run quarto render "$page.qmd" --to html); then
      echo "[build] ✓ Page $page rendered for $lang"
    else
      echo "[build] ✗ Page $page FAILED for $lang"
      FAILED_BOOKS+=("$lang/$page")
    fi
  done

  # ── Render each book ──────────────────────────────────────────────────────
  for book in "${BOOKS[@]}"; do
    BOOK_DIR="$LANG_DIR/$book"
    $ASSEMBLE_ONLY && continue  # les `public/` sont déjà rendus
    if [[ -n "$ONLY_UNIT" && "$ONLY_UNIT" != "$lang/$book" ]]; then
      continue
    fi
    echo ""
    echo "── $lang / $book ──────────────────────────────"

    if [[ ! -d "$BOOK_DIR" ]]; then
      echo "[build] Skipping $book ($lang): directory not found."
      continue
    fi

    # Un livre NEUF n'a pas encore d'arabe : son `index.qmd` arabe n'est produit que par
    # la traduction automatique, qui ne part qu'après la fusion sur master, et aucun
    # agent n'écrit de `.qmd` sous `precis/ar/`. Le `_quarto.yml` arabe, tenu à la main,
    # existe déjà. On saute donc le livre arabe dont `index.qmd` manque, en le disant :
    # ce cas, et lui seul — un CHAPITRE déclaré mais absent reste une erreur de rendu.
    if [[ "$lang" == "ar" && ! -f "$BOOK_DIR/index.qmd" ]]; then
      echo "[build] ⚠ $book ($lang) : traduction pas encore livrée (index.qmd absent) — livre sauté."
      continue
    fi

    if $PDF_ONLY; then
      # Le PDF d'un livre se rend à part du HTML (le site ne l'attend pas) : un échec est dit
      # et toléré, le livre garde alors le PDF du site en ligne.
      echo "[build] Rendering $book ($lang) (PDF seul)..."
      if (cd "$BOOK_DIR" && uv run quarto render --to pdf); then
        echo "[build] ✓ $book PDF rendered"
      else
        echo "[build] ⚠ $book: PDF failed — le PDF du site en ligne reste en place"
      fi
    elif $DO_PDF; then
      echo "[build] Rendering $book ($lang) (HTML + PDF)..."
      if (cd "$BOOK_DIR" && uv run quarto render); then
        echo "[build] ✓ $book rendered (HTML + PDF)"
      else
        if [[ -f "$BOOK_DIR/public/index.html" ]]; then
          echo "[build] ⚠ $book: PDF failed, HTML OK — deploying HTML only"
        else
          echo "[build] ✗ $book: HTML render FAILED"
          FAILED_BOOKS+=("$lang/$book")
          continue
        fi
      fi
    else
      if (cd "$BOOK_DIR" && uv run quarto render --to html); then
        echo "[build] ✓ $book rendered (HTML only)"
      else
        echo "[build] ✗ $book FAILED"
        FAILED_BOOKS+=("$lang/$book")
      fi
    fi
  done

  # Un seul livre rendu : son PDF est rangé dans `public/`, d'où l'assemblage le reprend
  # (le workflow n'emporte que ce dossier).
  if [[ -n "$ONLY_UNIT" ]]; then
    ubook="${ONLY_UNIT#*/}"
    if [[ "${ONLY_UNIT%%/*}" == "$lang" && -f "$LANG_DIR/$ubook/$ubook.pdf" && ! -f "$LANG_DIR/$ubook/public/$ubook.pdf" ]]; then
      cp "$LANG_DIR/$ubook/$ubook.pdf" "$LANG_DIR/$ubook/public/$ubook.pdf"
    fi
    continue
  fi

  # ── Assemble local site for this language ─────────────────────────────────
  mkdir -p "$LOCAL_SITE/$lang"

  # General pages
  for page in "${PAGES[@]}"; do
    if [[ -f "$LANG_DIR/$page.html" ]]; then
      cp "$LANG_DIR/$page.html" "$LOCAL_SITE/$lang/$page.html"
    fi
    if [[ -d "$LANG_DIR/${page}_files" ]]; then
      cp -r "$LANG_DIR/${page}_files" "$LOCAL_SITE/$lang/${page}_files"
    fi
  done

  # Figures des pages générales (annexe sur le PIB) : `figtools.figure_tabs` écrit ses images
  # dans `_fig/` et ses données téléchargeables dans `figdata/`, à côté de la page — comme
  # dans un livre, où Quarto les copie lui-même dans `public/`. Une page isolée n'a pas de
  # projet Quarto : on les copie ici, sans quoi l'image et le lien de téléchargement
  # pointeraient dans le vide.
  for dossier in _fig figdata; do
    if [[ -d "$LANG_DIR/$dossier" ]]; then
      cp -r "$LANG_DIR/$dossier" "$LOCAL_SITE/$lang/$dossier"
    fi
  done

  # Each book
  for book in "${BOOKS[@]}"; do
    SRC="$LANG_DIR/$book/public"
    DEST="$LOCAL_SITE/$lang/$book"
    if [[ -d "$SRC" ]]; then
      rm -rf "$DEST"
      mkdir -p "$DEST"
      cp -r "$SRC/." "$DEST"
      
      # Check for PDF
      if [[ -f "$SRC/$book.pdf" ]]; then
        cp "$SRC/$book.pdf" "$DEST/$book.pdf"
      elif [[ -f "$LANG_DIR/$book/$book.pdf" ]]; then
        cp "$LANG_DIR/$book/$book.pdf" "$DEST/$book.pdf"
      fi
    fi
  done
done

# Optional root index redirect
if [[ -n "$ONLY_UNIT" ]]; then
  if [[ ${#FAILED_BOOKS[@]} -gt 0 ]]; then
    echo "[build] ✗ Failed builds: ${FAILED_BOOKS[*]}"
    exit 1
  fi
  echo "[build] ✓ $ONLY_UNIT rendered."
  exit 0
fi
cat <<EOF > "$LOCAL_SITE/index.html"
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=fr/index.html">
  <title>Redirection...</title>
</head>
<body>
  <p>Redirection vers la <a href="fr/index.html">version française</a>...</p>
</body>
</html>
EOF

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════"
echo " Build complete"
echo "════════════════════════════════════════"

if [[ ${#FAILED_BOOKS[@]} -gt 0 ]]; then
  echo "[build] ✗ Failed builds: ${FAILED_BOOKS[*]}"
  exit 1
fi

echo "[build] ✓ All books rendered successfully."
echo ""
echo "Local site: $LOCAL_SITE"
echo "To preview: cd $LOCAL_SITE && uv run python -m http.server 8765"

#!/usr/bin/env bash
# build.sh — Convert and render all Quarto précis and assemble local site.
#
# Usage:
#   ./build.sh            # full build (HTML + PDF) — le PDF est le défaut
#   ./build.sh --no-pdf   # skip PDF rendering
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
BOOKS=(prestations_sociales retraites fiscalite remunerations_publiques cotisations_sociales caisses finances_locales marche_travail)
# Pages générales du site, posées directement sous precis/<langue>/ et rendues une à une.
PAGES=(index a-propos)

DO_PDF=true

usage() {
  cat <<'USAGE'
build.sh — rend tous les précis Quarto et assemble le site local.

Usage :
  ./build.sh            build complet (HTML + PDF)
  ./build.sh --no-pdf   rend le HTML seul, sans PDF
  ./build.sh --help     affiche cette aide

Le PDF est produit PAR DÉFAUT ; il n'existe pas d'option « --pdf ».

Sortie : local_site/ à la racine du dépôt.
Prévisualisation : cd local_site && uv run python -m http.server 8765

Codes de retour :
  0  succès
  1  au moins un livre n'a pas pu être rendu
  2  option invalide
USAGE
}

for arg in "$@"; do
  case "$arg" in
    --no-pdf)     DO_PDF=false ;;
    --help|-h)    usage; exit 0 ;;
    *)
      echo "build.sh : option inconnue « $arg »." >&2
      echo >&2
      usage >&2
      exit 2
      ;;
  esac
done

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

rm -rf "$LOCAL_SITE"
mkdir -p "$LOCAL_SITE"

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

    if $DO_PDF; then
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

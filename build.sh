#!/usr/bin/env bash
# build.sh — Convert and render all Quarto précis and assemble local site.
#
# Usage:
#   ./build.sh            # full build (HTML + PDF)
#   ./build.sh --no-pdf   # skip PDF rendering

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRECIS_DIR="$ROOT_DIR/precis"
LOCAL_SITE="$ROOT_DIR/local_site"

LANGUAGES=(fr ar)
BOOKS=(prestations_sociales retraites)

DO_PDF=true

for arg in "$@"; do
  case "$arg" in
    --no-pdf)     DO_PDF=false ;;
    *)            echo "Unknown option: $arg"; exit 2 ;;
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

  # ── Render landing page for the language ──────────────────────────────────
  echo "[build] Rendering landing page for $lang..."
  if (cd "$LANG_DIR" && uv run quarto render index.qmd --to html); then
    echo "[build] ✓ Landing page rendered for $lang"
  else
    echo "[build] ✗ Landing page FAILED for $lang"
    FAILED_BOOKS+=("$lang/index")
  fi

  # ── Render each book ──────────────────────────────────────────────────────
  for book in "${BOOKS[@]}"; do
    BOOK_DIR="$LANG_DIR/$book"
    echo ""
    echo "── $lang / $book ──────────────────────────────"

    if [[ ! -d "$BOOK_DIR" ]]; then
      echo "[build] Skipping $book ($lang): directory not found."
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

  # Landing page
  if [[ -f "$LANG_DIR/index.html" ]]; then
    cp "$LANG_DIR/index.html" "$LOCAL_SITE/$lang/index.html"
  fi
  if [[ -d "$LANG_DIR/index_files" ]]; then
    cp -r "$LANG_DIR/index_files" "$LOCAL_SITE/$lang/index_files"
  fi

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

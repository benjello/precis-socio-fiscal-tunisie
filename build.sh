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

# ── Step 1: Render each book (HTML + optionally PDF) ──────────────────────────
echo ""
echo "════════════════════════════════════════"
echo " Step 1: Rendering books"
echo "════════════════════════════════════════"

FAILED_BOOKS=()

for book in "${BOOKS[@]}"; do
  BOOK_DIR="$PRECIS_DIR/$book"
  echo ""
  echo "── $book ──────────────────────────────"

  if [[ ! -d "$BOOK_DIR" ]]; then
    echo "[build] Skipping $book: directory not found."
    continue
  fi

  if $DO_PDF; then
    # Render HTML + PDF
    echo "[build] Rendering $book (HTML + PDF)..."
    if (cd "$BOOK_DIR" && uv run quarto render); then
      echo "[build] ✓ $book rendered (HTML + PDF)"
    else
      if [[ -f "$BOOK_DIR/public/index.html" ]]; then
        echo "[build] ⚠ $book: PDF failed, HTML OK — deploying HTML only"
      else
        echo "[build] ✗ $book: HTML render FAILED"
        FAILED_BOOKS+=("$book")
        continue
      fi
    fi
  else
    if (cd "$BOOK_DIR" && uv run quarto render --to html); then
      echo "[build] ✓ $book rendered (HTML only)"
    else
      echo "[build] ✗ $book FAILED"
      FAILED_BOOKS+=("$book")
    fi
  fi
done

# ── Step 2: Render landing page ────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════"
echo " Step 2: Rendering landing page"
echo "════════════════════════════════════════"
(cd "$PRECIS_DIR" && uv run quarto render index.qmd --to html)
echo "[build] ✓ Landing page rendered"

# ── Step 3: Assemble local site ────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════"
echo " Step 3: Assembling local site → $LOCAL_SITE"
echo "════════════════════════════════════════"

mkdir -p "$LOCAL_SITE"

# Landing page
cp "$PRECIS_DIR/index.html" "$LOCAL_SITE/index.html"
if [[ -d "$PRECIS_DIR/index_files" ]]; then
  cp -r "$PRECIS_DIR/index_files" "$LOCAL_SITE/index_files"
fi
echo "[build] Copied landing page → local_site/index.html"

# Each book
for book in "${BOOKS[@]}"; do
  SRC="$PRECIS_DIR/$book/public"
  DEST="$LOCAL_SITE/$book"
  if [[ -d "$SRC" ]]; then
    rm -rf "$DEST"
    mkdir -p "$DEST"
    cp -r "$SRC/." "$DEST"
    
    # Check for PDF
    if [[ -f "$SRC/$book.pdf" ]]; then
      cp "$SRC/$book.pdf" "$DEST/$book.pdf"
      echo "[build] Copied PDF $book.pdf → local_site/$book/$book.pdf"
    elif [[ -f "$PRECIS_DIR/$book/$book.pdf" ]]; then
      cp "$PRECIS_DIR/$book/$book.pdf" "$DEST/$book.pdf"
      echo "[build] Copied PDF $book.pdf from root → local_site/$book/$book.pdf"
    fi
    echo "[build] Copied $book → local_site/$book"
  else
    echo "[build] Skipping $book: public/ not found."
  fi
done

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════"
echo " Build complete"
echo "════════════════════════════════════════"

if [[ ${#FAILED_BOOKS[@]} -gt 0 ]]; then
  echo "[build] ✗ Failed books: ${FAILED_BOOKS[*]}"
  exit 1
fi

echo "[build] ✓ All books rendered successfully."
echo ""
echo "Local site: $LOCAL_SITE"
echo "To preview: cd $LOCAL_SITE && uv run python -m http.server 8765"

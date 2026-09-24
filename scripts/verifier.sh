#!/usr/bin/env bash
# verifier.sh — enchaîne les contrôles du précis en UN bilan compact.
#
# Usage :
#   scripts/verifier.sh [--sans-reseau] [livre…]
#
# Sans livre en argument, les livres rendus sont déduits de ce qui a changé :
# `git diff --name-only origin/master...HEAD`, le reste de l'arbre de travail
# (indexé ou non) et les fichiers non suivis. Un fichier partagé (`figtools.py`,
# `precis/glossaire.yml`, `precis/_seriescache/`, un fichier posé au niveau de
# la langue plutôt que du livre) fait rendre les CINQ livres — voir
# `scripts/verifier_livres.py::livres_touches`.
#
# --sans-reseau saute la vérification des liens de la base législative (le seul
# contrôle qui appelle le réseau).
#
# Sortie : 0 si tout passe, 1 dès qu'une étape échoue. Le détail de chaque étape
# va dans un fichier journal (chemin affiché en fin d'exécution) ; ce que la
# commande imprime elle-même se limite à une ligne par étape.
set -uo pipefail
# Pas de `set -e` : chaque étape est lancée séparément et son code de retour
# consigné, pour que l'échec d'une étape n'empêche pas les suivantes de tourner
# et d'apparaître dans le bilan.

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

LOG="$(mktemp -t verifier-precis.XXXXXX.log)"
echo "Journal détaillé : $LOG" >&2

SANS_RESEAU=false
LIVRES_ARG=()
for arg in "$@"; do
  case "$arg" in
    --sans-reseau) SANS_RESEAU=true ;;
    --help|-h)
      sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *) LIVRES_ARG+=("$arg") ;;
  esac
done

ECHECS=0
etape() {
  # etape <intitulé> -- <commande...>
  local intitule="$1"; shift
  {
    echo "══════ $intitule ══════"
    echo "+ $*"
  } >>"$LOG"
  if "$@" >>"$LOG" 2>&1; then
    printf 'OK      %s\n' "$intitule"
    return 0
  else
    local code=$?
    printf 'ÉCHEC   %s (voir %s)\n' "$intitule" "$LOG"
    ECHECS=$((ECHECS + 1))
    return "$code"
  fi
}

# ── 1. Glossaire : régénération, verrou de synchro sur le CONTENU produit ──────
# Comparer au commité (comme verifier-conventions.yml, qui tourne APRÈS commit)
# rapporterait ÉCHEC pour la situation même où verifier.sh sert : un agent qui
# vient de régénérer un glossaire à jour, pas encore commité. On compare donc
# l'empreinte des fichiers engendrés AVANT et APRÈS l'appel : un écart dit
# seulement qu'ils viennent de changer, pas que quelque chose est cassé.
GLOSSAIRE_CIBLES=(precis/*/*/_glossaire.qmd translation_glossary.generated.md)
AVANT=$(sha256sum "${GLOSSAIRE_CIBLES[@]}" 2>/dev/null)
if uv run python scripts/build_glossary.py >>"$LOG" 2>&1; then
  APRES=$(sha256sum "${GLOSSAIRE_CIBLES[@]}" 2>/dev/null)
  if [ "$AVANT" = "$APRES" ]; then
    printf 'OK      Glossaire régénéré, inchangé\n'
  else
    printf 'OK      Glossaire régénéré — annexes modifiées, à commiter\n'
  fi
else
  printf 'ÉCHEC   build_glossary.py (voir %s)\n' "$LOG"
  ECHECS=$((ECHECS + 1))
fi

# ── 2-4. Contrôles de contenu, sans réseau ─────────────────────────────────────
etape "Le précis ne parle pas du modèle" uv run python scripts/check_pas_de_modele.py
etape "Le précis ne parle pas du dépouillement" uv run python scripts/check_jargon_depouillement.py
etape "Chaque recherche infructueuse a sa fiche" uv run python scripts/recherches.py verifier
etape "Les sous-agents Claude Code sont à jour" uv run python scripts/sync_agents.py --verifier

# ── 5. Liens de la base législative (réseau) ───────────────────────────────────
if $SANS_RESEAU; then
  printf 'SAUTÉ   Liens de la base législative (--sans-reseau)\n'
else
  etape "Liens de la base législative" uv run python scripts/verifier_liens_base_legislative.py
fi

# ── 6. Tests ────────────────────────────────────────────────────────────────────
etape "Tests (pytest)" uv run pytest -q tests

# ── 7. Livres à rendre ──────────────────────────────────────────────────────────
if [ "${#LIVRES_ARG[@]}" -gt 0 ]; then
  LIVRES=("${LIVRES_ARG[@]}")
else
  FICHIERS_DIFF="$( { git diff --name-only "origin/master...HEAD" 2>/dev/null; \
                       git diff --name-only HEAD 2>/dev/null; \
                       git diff --name-only --cached 2>/dev/null; \
                       git ls-files -o --exclude-standard 2>/dev/null; } | sort -u)"
  mapfile -t LIVRES < <(printf '%s\n' "$FICHIERS_DIFF" | uv run python scripts/verifier_livres.py livres-touches)
fi

if [ "${#LIVRES[@]}" -eq 0 ]; then
  printf 'OK      Rendu HTML : rien à rendre (aucun livre touché)\n'
else
  echo "══════ Rendu HTML (${LIVRES[*]}) ══════" >>"$LOG"
  QUARTO_PYTHON="$ROOT_DIR/.venv/bin/python3"
  export QUARTO_PYTHON
  RENDU_OK=true
  TOTAL_CITATIONS=0
  TOTAL_AROBASES=0
  for livre in "${LIVRES[@]}"; do
    for langue in fr ar; do
      BOOK_DIR="$ROOT_DIR/precis/$langue/$livre"
      [ -d "$BOOK_DIR" ] || continue
      echo "-- $langue/$livre --" >>"$LOG"
      if ! (cd "$BOOK_DIR" && uv run quarto render --to html) >>"$LOG" 2>&1; then
        printf 'ÉCHEC   Rendu %s/%s (voir %s)\n' "$langue" "$livre" "$LOG"
        ECHECS=$((ECHECS + 1))
        RENDU_OK=false
        continue
      fi
      PUBLIC_DIR="$BOOK_DIR/public"
      [ -d "$PUBLIC_DIR" ] || continue
      while IFS= read -r -d '' page; do
        n_citations=$(uv run python scripts/verifier_livres.py citations < "$page")
        n_arobases=$(uv run python scripts/verifier_livres.py arobases < "$page")
        TOTAL_CITATIONS=$((TOTAL_CITATIONS + n_citations))
        TOTAL_AROBASES=$((TOTAL_AROBASES + n_arobases))
        if [ "$n_citations" -gt 0 ] || [ "$n_arobases" -gt 0 ]; then
          echo "   $page : $n_citations citation(s) non résolue(s), $n_arobases « ?@ »" >>"$LOG"
        fi
      done < <(find "$PUBLIC_DIR" -name '*.html' -not -path '*/site_libs/*' -print0)
    done
  done
  if $RENDU_OK && [ "$TOTAL_CITATIONS" -eq 0 ] && [ "$TOTAL_AROBASES" -eq 0 ]; then
    printf 'OK      Rendu HTML (%s) : 0 citation non résolue, 0 « ?@ »\n' "${LIVRES[*]}"
  elif $RENDU_OK; then
    printf 'ÉCHEC   Rendu HTML (%s) : %d citation(s) non résolue(s), %d « ?@ » (voir %s)\n' \
      "${LIVRES[*]}" "$TOTAL_CITATIONS" "$TOTAL_AROBASES" "$LOG"
    ECHECS=$((ECHECS + 1))
  fi

  # ── 8. Restaurer les figdata dont seule la date de génération a changé ──────
  # Le pathspec DOIT porter le `/*` final : sans lui, un pathspec à glob (« * »)
  # ne descend pas dans le dossier qu'il nomme — contrairement à un pathspec SANS
  # glob, où nommer un dossier inclut tout son contenu. `precis/*/*/figdata` ne
  # matche donc RIEN ; seul `precis/*/*/figdata/*` matche les fichiers eux-mêmes.
  # Vérifié à la main le 24/09/2026 (voir le rapport de la tâche).
  mapfile -t FICHIERS_FIGDATA < <(git diff --name-only -- 'precis/*/*/figdata/*')
  RESTAURES=0
  if [ "${#FICHIERS_FIGDATA[@]}" -gt 0 ]; then
    # Un CSV et son sidecar .yml forment une PAIRE (voir
    # verifier_livres.figdata_a_restaurer) : on ne restaure l'un sans l'autre que
    # si l'un des deux n'a pas changé du tout. La décision se prend donc sur le
    # GROUPE, dans un objet JSON {chemin: diff}, jamais fichier par fichier.
    DIFFS_JSON=$(uv run python - "${FICHIERS_FIGDATA[@]}" <<'PY'
import json
import subprocess
import sys

diffs = {}
for chemin in sys.argv[1:]:
    diffs[chemin] = subprocess.run(
        ["git", "diff", "-U0", "--", chemin], capture_output=True, text=True
    ).stdout
print(json.dumps(diffs))
PY
)
    mapfile -t A_RESTAURER < <(echo "$DIFFS_JSON" | uv run python scripts/verifier_livres.py figdata-a-restaurer)
    for fichier in "${A_RESTAURER[@]}"; do
      [ -n "$fichier" ] || continue
      git checkout -- "$fichier"
      RESTAURES=$((RESTAURES + 1))
    done
  fi
  if [ "$RESTAURES" -gt 0 ]; then
    printf 'OK      Figdata restaurées (%d fichier(s) dont seule la date avait changé)\n' "$RESTAURES"
  fi
fi

echo "" >>"$LOG"
if [ "$ECHECS" -eq 0 ]; then
  echo "Bilan : tout est passé."
  exit 0
else
  echo "Bilan : $ECHECS étape(s) en échec. Journal : $LOG"
  exit 1
fi

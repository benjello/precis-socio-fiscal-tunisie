#!/usr/bin/env bash
# verifier.sh — enchaîne les contrôles du précis en UN bilan compact.
#
# Usage :
#   scripts/verifier.sh [--sans-reseau] [--complet] [livre…]
#
# Par défaut, quand les seuls fichiers modifiés d'un livre sont des chapitres
# `.qmd` posés à sa racine, seuls ces chapitres sont rendus (quelques dizaines de
# secondes au lieu de plusieurs minutes) ; tout autre fichier du livre ou un
# fichier partagé impose le rendu complet (`verifier_livres.py::chapitres_touches`).
# Si un chapitre rendu seul montre un renvoi cassé, le livre est rendu en entier
# avant de conclure. --complet rend toujours les livres entiers ; nommer des
# livres en argument a le même effet.
#
# Sans livre en argument, les livres rendus sont déduits de ce qui a changé :
# `git diff --name-only origin/master...HEAD`, le reste de l'arbre de travail
# (indexé ou non) et les fichiers non suivis. Un fichier partagé (`figtools.py`,
# `precis/glossaire.yml`, `precis/_seriescache/`, un fichier posé au niveau de
# la langue plutôt que du livre) fait rendre TOUS les livres — voir
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
COMPLET=false
LIVRES_ARG=()
for arg in "$@"; do
  case "$arg" in
    --sans-reseau) SANS_RESEAU=true ;;
    --complet|--all) COMPLET=true ;;
    --help|-h)
      sed -n '2,28p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *) LIVRES_ARG+=("$arg") ;;
  esac
done

ECHECS=0
avertir() {
  # avertir <intitulé> -- <commande...> : consigne et affiche la dernière ligne, sans compter d'échec
  local intitule="$1"; shift
  { echo "══════ $intitule ══════"; echo "+ $*"; } >>"$LOG"
  local sortie
  sortie=$("$@" 2>&1); echo "$sortie" >>"$LOG"
  printf 'AVERT   %s : %s\n' "$intitule" "$(printf '%s\n' "$sortie" | tail -1)"
}

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
GLOSSAIRE_CIBLES=(precis/*/*/_glossaire.qmd precis/*/*/_glossaire.infobulles.html translation_glossary.generated.md)
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
etape "Les séries de dette sont cohérentes (périmètres)" uv run python scripts/check_dette_coherence.py
etape "Le dépôt public ne parle pas de la sauvegarde" uv run python scripts/check_pas_d_infra.py
etape "Le précis ne parle pas du dépouillement" uv run python scripts/check_jargon_depouillement.py
etape "La numérotation se lit sans trou" uv run python scripts/check_numerotation.py
etape "Chaque recherche infructueuse a sa fiche" uv run python scripts/recherches.py verifier
etape "Les références de loi ont leur ligne de registre" uv run python scripts/check_domicile_references.py
etape "Les manifestes de relevés sont lisibles et cohérents" uv run python scripts/check_manifestes.py
etape "Les copies locales annoncées sont dans les manifestes de tunisia-data" uv run python scripts/check_copies_locales.py
etape "Les sous-agents Claude Code sont à jour" uv run python scripts/sync_agents.py --verifier
etape "Le compte reconstruit des administrations publiques est cohérent" uv run python scripts/reconstruire_comptes.py --verifier
etape "Les résidus du compte reconstruit sont à jour" uv run python scripts/expliquer_residus.py --verifier
etape "Les comptes des secteurs reconstruits sont à jour" uv run python scripts/reconstruire_secteurs.py --verifier
etape "Le sommaire par les comptes est à jour" uv run python scripts/sommaire_comptes.py --verifier
avertir "Vocabulaire de comptabilité nationale (avertissement)" uv run python scripts/check_vocabulaire_comptes.py --detail
etape "Les liens entre volumes mènent à une page et une ancre (fr)" uv run python scripts/verifier_liens_entre_volumes.py --langue fr
etape "Les liens entre volumes mènent à une page et une ancre (ar)" uv run python scripts/verifier_liens_entre_volumes.py --langue ar

# ── 5. Liens de la base législative (réseau) ───────────────────────────────────
if $SANS_RESEAU; then
  printf 'SAUTÉ   Liens de la base législative (--sans-reseau)\n'
else
  etape "Liens de la base législative" uv run python scripts/verifier_liens_base_legislative.py
fi

# ── 6. Tests ────────────────────────────────────────────────────────────────────
etape "Tests (pytest)" uv run pytest -q tests

# Rendre seulement quelques chapitres d'un livre (mode par défaut).
rendre_chapitres() {
  local dir="$1"; shift
  local ch
  for ch in "$@"; do
    (cd "$dir" && uv run quarto render "$ch" --to html) >>"$LOG" 2>&1 || return 1
  done
}

# Compter citations non résolues, « ?@ » et renvois cassés dans les pages
# rendues : toutes les pages du livre, ou celles des chapitres nommés.
# Imprime « citations arobases renvois ».
compter_pages() {
  local dir="$1"; shift
  local public="$dir/public" page nc na nr c=0 a=0 r=0
  local pages=()
  if [ "$#" -gt 0 ]; then
    local ch
    for ch in "$@"; do pages+=("$public/${ch%.qmd}.html"); done
  else
    mapfile -d '' pages < <(find "$public" -name '*.html' -not -path '*/site_libs/*' -print0 2>/dev/null)
  fi
  for page in "${pages[@]}"; do
    [ -f "$page" ] || continue
    nc=$(uv run python scripts/verifier_livres.py citations < "$page")
    na=$(uv run python scripts/verifier_livres.py arobases < "$page")
    nr=$(uv run python scripts/verifier_livres.py renvois < "$page")
    c=$((c + nc)); a=$((a + na)); r=$((r + nr))
    if [ "$nc" -gt 0 ] || [ "$na" -gt 0 ] || [ "$nr" -gt 0 ]; then
      echo "   $page : $nc citation(s) non résolue(s), $na « ?@ », $nr renvoi(s) « ?tbl-/?fig-/?sec- »" >>"$LOG"
    fi
  done
  echo "$c $a $r"
}

# ── 7. Livres à rendre ──────────────────────────────────────────────────────────
# Les chemins modifiés servent aussi aux pages générales (§ 9) et au nettoyage (§ 10) : on les
# relève même quand les livres sont nommés en argument.
FICHIERS_DIFF="$( { git diff --name-only "origin/master...HEAD" 2>/dev/null; \
                     git diff --name-only HEAD 2>/dev/null; \
                     git diff --name-only --cached 2>/dev/null; \
                     git ls-files -o --exclude-standard 2>/dev/null; } | sort -u)"
if [ "${#LIVRES_ARG[@]}" -gt 0 ]; then
  LIVRES=("${LIVRES_ARG[@]}")
  COMPLET=true
else
  mapfile -t LIVRES < <(printf '%s\n' "$FICHIERS_DIFF" | uv run python scripts/verifier_livres.py livres-touches)
fi

# Relevé des figdata AVANT tout rendu : le nettoyage final (§ 9) ne touche qu'à ce que le rendu a
# changé dans un fichier jusque-là propre.
mapfile -t FIGDATA_MODIFIES_AVANT < <(git diff --name-only -- 'precis/*/*/figdata/*')
mapfile -t FIGDATA_NON_SUIVIS_AVANT < <(git ls-files -o --exclude-standard -- 'precis/*/*/figdata/*')

if [ "${#LIVRES[@]}" -eq 0 ]; then
  printf 'OK      Rendu HTML : rien à rendre (aucun livre touché)\n'
else
  echo "══════ Rendu HTML (${LIVRES[*]}) ══════" >>"$LOG"
  QUARTO_PYTHON="$ROOT_DIR/.venv/bin/python3"
  export QUARTO_PYTHON
  RENDU_OK=true
  TOTAL_CITATIONS=0
  TOTAL_AROBASES=0
  TOTAL_RENVOIS=0
  for livre in "${LIVRES[@]}"; do
    for langue in fr ar; do
      BOOK_DIR="$ROOT_DIR/precis/$langue/$livre"
      [ -d "$BOOK_DIR" ] || continue
      # Livre neuf : l'arabe n'arrive qu'avec la traduction post-fusion (voir build.sh).
      if [ "$langue" = ar ] && [ ! -f "$BOOK_DIR/index.qmd" ]; then
        printf 'SAUTÉ   Rendu ar/%s : traduction pas encore livrée (index.qmd absent)\n' "$livre"
        continue
      fi
      echo "-- $langue/$livre --" >>"$LOG"
      CHAPITRES=()
      MODE=TOUT
      if ! $COMPLET; then
        SORTIE=$(printf '%s\n' "$FICHIERS_DIFF" | uv run python scripts/verifier_livres.py chapitres "$langue" "$livre")
        if [ "$SORTIE" != TOUT ]; then
          MODE=CHAPITRES
          mapfile -t CHAPITRES < <(printf '%s\n' "$SORTIE" | sed '/^$/d')
        fi
      fi
      if [ "$MODE" = CHAPITRES ] && [ "${#CHAPITRES[@]}" -eq 0 ]; then
        echo "   rien à rendre dans cette langue" >>"$LOG"
        continue
      fi
      if [ "$MODE" = CHAPITRES ]; then
        printf 'INFO    Rendu %s/%s : chapitres seuls (%s)\n' "$langue" "$livre" "${CHAPITRES[*]}"
        if ! rendre_chapitres "$BOOK_DIR" "${CHAPITRES[@]}"; then
          MODE=TOUT
        else
          read -r c a r < <(compter_pages "$BOOK_DIR" "${CHAPITRES[@]}")
          if [ $((c + a + r)) -gt 0 ]; then
            echo "   défaut en mode chapitres : rendu complet du livre avant de conclure" >>"$LOG"
            MODE=TOUT
          fi
        fi
      fi
      if [ "$MODE" = TOUT ]; then
        if ! (cd "$BOOK_DIR" && uv run quarto render --to html) >>"$LOG" 2>&1; then
          printf 'ÉCHEC   Rendu %s/%s (voir %s)\n' "$langue" "$livre" "$LOG"
          ECHECS=$((ECHECS + 1))
          RENDU_OK=false
          continue
        fi
        read -r c a r < <(compter_pages "$BOOK_DIR")
      fi
      TOTAL_CITATIONS=$((TOTAL_CITATIONS + c))
      TOTAL_AROBASES=$((TOTAL_AROBASES + a))
      TOTAL_RENVOIS=$((TOTAL_RENVOIS + r))
    done
  done
  if $RENDU_OK && [ "$TOTAL_CITATIONS" -eq 0 ] && [ "$TOTAL_AROBASES" -eq 0 ] && [ "$TOTAL_RENVOIS" -eq 0 ]; then
    printf 'OK      Rendu HTML (%s) : 0 citation non résolue, 0 « ?@ », 0 renvoi cassé\n' "${LIVRES[*]}"
  elif $RENDU_OK; then
    printf 'ÉCHEC   Rendu HTML (%s) : %d citation(s) non résolue(s), %d « ?@ », %d renvoi(s) cassé(s) (voir %s)\n' \
      "${LIVRES[*]}" "$TOTAL_CITATIONS" "$TOTAL_AROBASES" "$TOTAL_RENVOIS" "$LOG"
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

# ── 9. Pages générales touchées (accueil, principes, annexes…) ─────────────────
mapfile -t PAGES_TOUCHEES < <(printf '%s\n' "$FICHIERS_DIFF" | uv run python scripts/verifier_livres.py pages-touchees)
if [ "${#PAGES_TOUCHEES[@]}" -gt 0 ]; then
  echo "══════ Rendu des pages générales (${PAGES_TOUCHEES[*]}) ══════" >>"$LOG"
  PC=0; PA=0; PR=0; PAGES_OK=true
  for lp in "${PAGES_TOUCHEES[@]}"; do
    langue="${lp%%/*}"; page="${lp#*/}"
    if ! (cd "$ROOT_DIR/precis/$langue" && uv run quarto render "$page.qmd" --to html) >>"$LOG" 2>&1; then
      printf 'ÉCHEC   Rendu de la page %s (voir %s)\n' "$lp" "$LOG"; ECHECS=$((ECHECS + 1)); PAGES_OK=false; continue
    fi
    html="$ROOT_DIR/precis/$langue/$page.html"
    nc=$(uv run python scripts/verifier_livres.py citations < "$html")
    na=$(uv run python scripts/verifier_livres.py arobases < "$html")
    nr=$(uv run python scripts/verifier_livres.py renvois < "$html")
    PC=$((PC + nc)); PA=$((PA + na)); PR=$((PR + nr))
    [ $((nc + na + nr)) -gt 0 ] && echo "   $html : $nc citation(s), $na « ?@ », $nr renvoi(s)" >>"$LOG"
  done
  if $PAGES_OK && [ $((PC + PA + PR)) -eq 0 ]; then
    printf 'OK      Rendu des pages générales (%s) : 0 citation non résolue, 0 « ?@ », 0 renvoi cassé\n' "${PAGES_TOUCHEES[*]}"
  elif $PAGES_OK; then
    printf 'ÉCHEC   Rendu des pages générales (%s) : %d citation(s), %d « ?@ », %d renvoi(s) (voir %s)\n' \
      "${PAGES_TOUCHEES[*]}" "$PC" "$PA" "$PR" "$LOG"
    ECHECS=$((ECHECS + 1))
  fi
fi

# ── 10. Nettoyer ce que le rendu a réécrit hors du sujet vérifié ─────────────────
# Seuls les figdata PROPRES avant le rendu, dans un livre dont aucune source n'a changé, sont
# restaurés (modifiés) ou supprimés (créés) : ils n'ont été rendus qu'à cause d'un fichier partagé.
# La liste est écrite au journal ; rien d'autre n'est touché.
mapfile -t FIGDATA_MODIFIES_APRES < <(git diff --name-only -- 'precis/*/*/figdata/*')
mapfile -t FIGDATA_NON_SUIVIS_APRES < <(git ls-files -o --exclude-standard -- 'precis/*/*/figdata/*')
NETTOYAGE=$(uv run python - "$FICHIERS_DIFF" \
  "$(printf '%s\n' "${FIGDATA_MODIFIES_AVANT[@]}")" "$(printf '%s\n' "${FIGDATA_MODIFIES_APRES[@]}")" \
  "$(printf '%s\n' "${FIGDATA_NON_SUIVIS_AVANT[@]}")" "$(printf '%s\n' "${FIGDATA_NON_SUIVIS_APRES[@]}")" <<'PY' | uv run python scripts/verifier_livres.py nettoyage
import json, sys
l = lambda s: [x for x in s.splitlines() if x.strip()]
print(json.dumps({"fichiers_diff": l(sys.argv[1]), "avant_modifies": l(sys.argv[2]),
                  "apres_modifies": l(sys.argv[3]), "avant_non_suivis": l(sys.argv[4]),
                  "apres_non_suivis": l(sys.argv[5])}))
PY
)
mapfile -t A_RESTAURER_RENDU < <(printf '%s' "$NETTOYAGE" | uv run python -c 'import json,sys; print("\n".join(json.load(sys.stdin)["restaurer"]))')
mapfile -t A_SUPPRIMER_RENDU < <(printf '%s' "$NETTOYAGE" | uv run python -c 'import json,sys; print("\n".join(json.load(sys.stdin)["supprimer"]))')
N_R=0; N_S=0
for f in "${A_RESTAURER_RENDU[@]}"; do [ -n "$f" ] && git checkout -- "$f" && echo "   restauré : $f" >>"$LOG" && N_R=$((N_R + 1)); done
for f in "${A_SUPPRIMER_RENDU[@]}"; do [ -n "$f" ] && [ -f "$f" ] && rm -- "$f" && echo "   supprimé : $f" >>"$LOG" && N_S=$((N_S + 1)); done
if [ $((N_R + N_S)) -gt 0 ]; then
  printf 'OK      Rendu nettoyé : %d figdata restauré(s), %d figdata créé(s) supprimé(s), hors des livres modifiés (liste au journal)\n' "$N_R" "$N_S"
fi

echo "" >>"$LOG"
if [ "$ECHECS" -eq 0 ]; then
  echo "Bilan : tout est passé."
  exit 0
else
  echo "Bilan : $ECHECS étape(s) en échec. Journal : $LOG"
  exit 1
fi

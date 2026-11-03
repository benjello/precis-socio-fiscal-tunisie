#!/usr/bin/env bash
# Remet les livres rendus par `rendre.yml` à leur place avant l'assemblage du site.
#
#   scripts/placer_livres.sh DOSSIER [--pdf-en-ligne]
#
# DOSSIER contient les artefacts : `public-<langue>-<livre>/` (le `public/` HTML d'un livre) et
# `pdf-<langue>-<livre>/` (son PDF). Chacun est posé sous precis/<langue>/<livre>/public/.
# Avec --pdf-en-ligne, un livre sans PDF neuf reprend celui du site en ligne : le déploiement
# est total (GitHub Pages remplace tout le site), et un livre ne perd pas son PDF le temps que
# le nouveau soit rendu, ni quand son rendu échoue.
set -euo pipefail
shopt -s nullglob

DIR="${1:?usage : placer_livres.sh DOSSIER [--pdf-en-ligne]}"

for d in "$DIR"/public-*; do
  n="${d#"$DIR"/public-}"; lang="${n%%-*}"; book="${n#*-}"
  mkdir -p "precis/$lang/$book/public"
  cp -r "$d"/. "precis/$lang/$book/public/"
done

for d in "$DIR"/pdf-*; do
  n="${d#"$DIR"/pdf-}"; lang="${n%%-*}"; book="${n#*-}"
  mkdir -p "precis/$lang/$book/public"
  for f in "$d"/*.pdf; do cp "$f" "precis/$lang/$book/public/"; done
done

if [[ "${2:-}" == "--pdf-en-ligne" ]]; then
  repo="${GITHUB_REPOSITORY:-benjello/precis-socio-fiscal-tunisie}"
  base="https://${repo%%/*}.github.io/${repo#*/}"
  anciens=()
  for pub in precis/*/*/public; do
    book="$(basename "$(dirname "$pub")")"; lang="$(basename "$(dirname "$(dirname "$pub")")")"
    [[ -f "$pub/index.html" ]] || continue
    [[ -n "$(find "$pub" -maxdepth 1 -name '*.pdf' -print -quit)" ]] && continue
    # Le nom du PDF est celui que le livre annonce dans sa page d'accueil (titre du livre).
    nom="$(grep -o 'href="\./[^"]*\.pdf"' "$pub/index.html" | head -1 | sed 's|href="\./||; s|"$||')"
    [[ -n "$nom" ]] || continue
    url="$base/$lang/$book/$(python3 -c 'import sys,urllib.parse as u; print(u.quote(sys.argv[1]))' "$nom")"
    if curl -fsSL --retry 2 -o "$pub/$nom" "$url"; then
      anciens+=("$lang/$book")
      # Le PDF vient de la version précédente du site : le lien le dit, en infobulle, jusqu'au
      # second déploiement (qui repart des pages sans cette mention).
      find "$pub" -name '*.html' -print0 | xargs -0 sed -i \
        "s|href=\"./$nom\" title=\"Download PDF\"|href=\"./$nom\" title=\"PDF de la version précédente : mise à jour en cours\"|g"
      echo "[placer] PDF repris du site en ligne : $lang/$book"
    else
      rm -f "$pub/$nom"
      echo "[placer] pas de PDF en ligne pour $lang/$book"
    fi
  done
  if [[ -n "${GITHUB_STEP_SUMMARY:-}" && ${#anciens[@]} -gt 0 ]]; then
    {
      echo "## PDF de la version précédente (mise à jour en cours)"
      echo
      printf -- '- %s\n' "${anciens[@]}"
    } >> "$GITHUB_STEP_SUMMARY"
  fi
fi

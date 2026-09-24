"""Fonctions pures de `scripts/verifier.sh` : quels livres rendre, et ce qu'on compte
dans leur rendu.

Isolées ici pour rester testables sans dépôt ni rendu réel — `verifier.sh` les
appelle en ligne de commande (voir le bloc CLI en bas de fichier), et les tests
les appellent directement.
"""
from __future__ import annotations

import json
import re
import sys

LIVRES = ("cotisations_sociales", "fiscalite", "prestations_sociales",
          "remunerations_publiques", "retraites")

# Un fichier sous ces préfixes touche potentiellement TOUS les livres : les
# modules Python que les figures importent (`from figures import …` mis à part —
# chaque livre a les siennes), le thème partagé, le glossaire source, son cache
# de séries, ou un fichier partagé posé au niveau de la langue plutôt que du
# livre (`precis/fr/references.json`, `precis/fr/precis.csl`…), à distinguer
# d'un fichier DANS un livre (`precis/fr/retraites/references.json`).
#
# Liste des modules établie le 24/09/2026 par
# `grep -rhoE '^(from|import) [a-zA-Z_.]+' precis/fr/*/*.qmd precis/fr/*/figures/*.py`,
# filtrée aux seuls modules internes à `scripts/` : `figtools`, `openfisca_tables`,
# `augmentations`, `tarifs`. À revérifier si un livre commence à importer autre
# chose.
PREFIXES_PARTAGES = (
    "scripts/figtools.py",
    "scripts/openfisca_tables.py",
    "scripts/augmentations.py",
    "scripts/tarifs.py",
    "precis/glossaire.yml",
    "precis/legendes.scss",
    "precis/_seriescache/",
)

RE_FICHIER_DE_LIVRE = re.compile(r"^precis/(?:fr|ar)/([^/]+)/")
RE_FICHIER_DE_LANGUE = re.compile(r"^precis/(?:fr|ar)/[^/]+\.[^/]+$")


def livres_touches(fichiers: list[str]) -> list[str]:
    """Les livres à rendre, déduits des chemins modifiés.

    Un fichier posé directement sous `precis/<langue>/` (pas dans un sous-dossier
    de livre) ou sous l'un des préfixes partagés fait rendre les CINQ livres :
    une bibliographie ou une feuille de style communes, par exemple, ne
    « appartiennent » à aucun livre en particulier.
    """
    touches: set[str] = set()
    for f in fichiers:
        f = f.strip()
        if not f:
            continue
        if f.startswith(PREFIXES_PARTAGES) or RE_FICHIER_DE_LANGUE.match(f):
            return sorted(LIVRES)
        m = RE_FICHIER_DE_LIVRE.match(f)
        if m and m.group(1) in LIVRES:
            touches.add(m.group(1))
    return sorted(touches)


def compter_citations_non_resolues(html: str) -> int:
    """Citations `[@clé]` que citeproc n'a pas résolues.

    Rendues `<strong>clé?</strong>` (constaté empiriquement le 24/09/2026, en
    injectant une citation vers une clé inexistante dans un rendu réel). La
    légende volontaire des prestations sociales, « **?** la question n'est pas
    tranchée… », rend `<strong>?</strong>` — le même motif, mais SANS rien avant
    le point d'interrogation. `[^<]+` (un ou plus, pas `*`) exclut donc ce seul
    cas légitime sans liste d'exceptions ad hoc.
    """
    return len(re.findall(r"<strong>[^<]+\?</strong>", html))


def compter_arobases_cassees(html: str) -> int:
    """`?@` littéral : une référence `[@clé]` mal formée, jamais reconnue comme
    citation par Pandoc, et donc restée telle quelle dans le texte rendu.

    N'appelle ceci QUE sur les pages du livre, jamais sur `site_libs/` : la
    bibliothèque JS de Quarto contient elle-même la sous-chaîne `?@` dans un
    motif d'échappement d'URL (constaté dans `anchor.min.js`), sans rapport
    avec une citation.
    """
    return html.count("?@")


_LIGNE_DATE_SEULE = re.compile(
    r"^[+-](?:# Figure-data du précis socio-fiscal tunisien — généré le "
    r"\d{4}-\d{2}-\d{2}|generated: \d{4}-\d{2}-\d{2})\s*$"
)


def figdata_seule_date_a_change(diff_unifie: str) -> bool:
    """Vrai si un `git diff -U0` sur UN fichier ne touche QUE la ligne de date.

    Compare les lignes `+`/`-` (hors `+++`/`---`/`@@`) à la forme attendue de la
    ligne de date, dans le CSV (`# Figure-data … généré le AAAA-MM-JJ`) et dans
    son sidecar (`generated: AAAA-MM-JJ`). Un diff vide (fichier inchangé) rend
    True : rien à restaurer, mais rien d'anormal non plus.
    """
    lignes_changees = [
        l for l in diff_unifie.splitlines()
        if (l.startswith("+") or l.startswith("-"))
        and not l.startswith("+++") and not l.startswith("---")
    ]
    return all(_LIGNE_DATE_SEULE.match(l) for l in lignes_changees)


def figdata_a_restaurer(diffs: dict[str, str]) -> list[str]:
    """Les chemins à restaurer par `git checkout --`, parmi des figdata modifiés.

    `diffs` associe chaque chemin modifié (CSV ou sidecar `.yml`) à son
    `git diff -U0`. Un CSV et son sidecar forment une PAIRE : on ne restaure les
    deux que si NI L'UN NI L'AUTRE ne change ailleurs que sur sa date. Restaurer
    un seul des deux romprait leur cohérence — une légende ajoutée, par exemple,
    change la ligne de date du CSV (qui porte la légende) mais laisse le sidecar
    inchangé à part sa propre date (il ne connaît pas de champ note) : le CSV
    porte alors un vrai changement de contenu, jamais « seulement sa date ».
    """
    groupes: dict[str, list[str]] = {}
    for chemin in diffs:
        base = chemin[:-len(".yml")] if chemin.endswith(".yml") else chemin
        groupes.setdefault(base, []).append(chemin)
    a_restaurer: list[str] = []
    for membres in groupes.values():
        if all(figdata_seule_date_a_change(diffs[m]) for m in membres):
            a_restaurer.extend(membres)
    return a_restaurer


def _cli(argv: list[str]) -> int:
    if not argv:
        print("usage: verifier_livres.py livres-touches|citations|arobases|figdata-date-seule",
              file=sys.stderr)
        return 2
    commande, reste = argv[0], argv[1:]
    entree = sys.stdin.read()
    if commande == "livres-touches":
        fichiers = [l for l in entree.splitlines() if l.strip()]
        print("\n".join(livres_touches(fichiers)))
        return 0
    if commande == "citations":
        print(compter_citations_non_resolues(entree))
        return 0
    if commande == "arobases":
        print(compter_arobases_cassees(entree))
        return 0
    if commande == "figdata-date-seule":
        return 0 if figdata_seule_date_a_change(entree) else 1
    if commande == "figdata-a-restaurer":
        # entrée : JSON {chemin: diff}, un par ligne de stdin serait fragile (les
        # diffs contiennent des sauts de ligne) — un objet JSON unique, donc.
        diffs = json.loads(entree) if entree.strip() else {}
        print("\n".join(figdata_a_restaurer(diffs)))
        return 0
    print(f"commande inconnue : {commande}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli(sys.argv[1:]))

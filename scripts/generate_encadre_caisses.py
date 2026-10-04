"""Engendre l'encadré « Les caisses de sécurité sociale » des livres « dispositifs ».

Les livres « Cotisations sociales », « Prestations sociales » et « Retraites » présentaient
chacun les caisses à leur manière, et aucun ne le faisait en entier. L'encadré est écrit ICI,
une seule fois : un paragraphe commun — quelles caisses, depuis quand, pour qui —, une ligne
propre à chaque livre — qui y collecte et qui y paie —, et le renvoi au livre « Les caisses
de sécurité sociale », qui fait foi sur leur statut, leurs comptes et leur budget.

Le texte est écrit dans chaque livre sous `precis/fr/<livre>/_encadre_caisses.qmd`, que
l'index du livre inclut. Ce n'est pas un partiel partagé hors des livres : la traduction
automatique traduit les `.qmd` de chaque livre, et un fichier posé hors de leurs dossiers
n'aurait pas d'homologue arabe à côté de l'index arabe qui l'inclut.

    uv run python scripts/generate_encadre_caisses.py             # écrit les trois partiels
    uv run python scripts/generate_encadre_caisses.py --verifier  # 1 si un partiel a dérivé

`tests/test_encadre_caisses.py` lance la vérification : `scripts/verifier.sh` et la CI
attrapent donc une retouche faite à la main dans un partiel.

Les clés citées doivent exister dans la bibliographie de chaque livre qui reçoit l'encadré,
en français ET en arabe (`references.json` du livre ou fonds commun de la langue).
"""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
NOM = "_encadre_caisses.qmd"

ENTETE = (
    "<!-- Fichier engendré par scripts/generate_encadre_caisses.py, depuis une source unique "
    "commune aux livres « Cotisations sociales », « Prestations sociales » et « Retraites » : "
    "ne pas l'éditer ici, éditer le script et le relancer. -->\n"
)

COMMUN = (
    "Trois caisses publiques gèrent aujourd'hui la sécurité sociale. La "
    "[Caisse nationale de sécurité sociale](#g-cnss) (CNSS), instituée en 1960 [@loi60-30], "
    "gère les régimes du secteur privé, salariés et non-salariés. La "
    "[Caisse nationale de retraite et de prévoyance sociale](#g-cnrps) (CNRPS) est formée par "
    "la loi de finances pour 1976, à partir de deux caisses créées en 1959, et couvre les "
    "agents publics [@loi75-83, art. 28]. La [Caisse nationale d'assurance maladie](#g-cnam) "
    "(CNAM), créée en 2004, gère l'assurance maladie des deux secteurs et la réparation des "
    "accidents du travail [@loi2004-71, art. 7 et 8]. De 1976 à 1994, une quatrième caisse, "
    "la [CAVIS](#g-cavis), a géré les pensions du secteur privé dans le cadre de la CNSS "
    "[@decret76-981, art. 1 et 2 ; @decret94-1477, art. 1 et 2]."
)

PROPRE = {
    "cotisations_sociales": (
        "**Dans ce livre**, les cotisations des régimes du secteur privé sont recouvrées par la "
        "CNSS, celles du secteur public par la CNRPS. La cotisation d'assurance maladie "
        "instituée en 2004 est perçue par ces deux caisses, qui la reversent à la CNAM, selon "
        "la rédaction initiale de la loi n° 2004-71 [@loi2004-71, art. 16]."
    ),
    "prestations_sociales": (
        "**Dans ce livre**, les prestations contributives sont servies par la caisse du régime "
        "de l'assuré — la CNSS au secteur privé, la CNRPS au secteur public — et, pour les "
        "soins, les indemnités de maladie et de couches et la réparation des accidents du "
        "travail, par la CNAM [@loi2004-71, art. 8]. Les prestations non contributives "
        "relèvent du ministère des affaires sociales et du budget de l'État "
        "[@loi-amen-social-2019 ; @decret-gouv-2020-317-amen, art. 29]."
    ),
    "retraites": (
        "**Dans ce livre**, les pensions du secteur public sont servies par la CNRPS, celles "
        "du secteur privé par la CNSS. De 1976 à 1994, la CAVIS les gérait pour le compte de "
        "celle-ci ; le régime de pensions des Tunisiens à l'étranger lui était délégué "
        "[@decret89-107, art. 2], et les employeurs adhéraient auprès d'elle au régime "
        "complémentaire [@arrete-1978-11-18-retraite-complementaire, règlement, art. 3-4]."
    ),
}

RENVOI = (
    "Leur lignée, leur statut, la séparation de leurs comptes par régime, leur budget, et ce "
    "que l'État en attend ou y apporte sont exposés dans le livre "
    "[« Les caisses de sécurité sociale »](../caisses/index.html)."
)


def texte(livre: str) -> str:
    """Le partiel d'un livre : en-tête, puis l'encadré."""
    return (
        f"{ENTETE}\n"
        '::: {.callout-note title="Les caisses de sécurité sociale"}\n'
        f"{COMMUN}\n\n{PROPRE[livre]}\n\n{RENVOI}\n"
        ":::\n"
    )


def chemin(livre: str) -> Path:
    return RACINE / "precis" / "fr" / livre / NOM


def derives() -> list[str]:
    """Les partiels absents ou différents de ce que le script écrirait."""
    return [livre for livre in PROPRE
            if not chemin(livre).is_file()
            or chemin(livre).read_text(encoding="utf-8") != texte(livre)]


def main(argv: list[str]) -> int:
    if "--verifier" in argv:
        ecarts = derives()
        for livre in ecarts:
            print(f"✗ {chemin(livre).relative_to(RACINE)} : à régénérer "
                  "(uv run python scripts/generate_encadre_caisses.py)")
        return 1 if ecarts else 0
    for livre in PROPRE:
        chemin(livre).write_text(texte(livre), encoding="utf-8")
        print(f"✓ {chemin(livre).relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

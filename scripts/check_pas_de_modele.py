"""Le précis documente la loi, jamais le modèle : ce contrôle le vérifie.

Voir `docs/conventions-redaction.md`, § 1. `openfisca-tunisia` ne se mentionne pas dans le
texte RENDU du précis — ni son nom, ni « le modèle », ni « les paramètres du modèle ». Ce
qu'on constate à son sujet va dans un `<!-- TODO (rôle) : … -->`, dans une *issue*, ou dans
`docs/notes/backlog-modele.md`.

Le contrôle ne regarde donc que ce que le lecteur voit. Sont exclus :

- les blocs ```{python}``` — ils importent le module qui engendre les tableaux, et ne sont
  pas rendus (`echo: false`) ;
- les commentaires HTML `<!-- … -->` — c'est précisément la destination prévue ;
- l'annexe `_glossaire.qmd`, engendrée par `build_glossary.py`.

Le mot « modèle » a par ailleurs des emplois parfaitement légitimes en droit — « le modèle
français de carrière », « le modèle de score de l'AMEN », « le modèle de la déclaration ».
On ne signale donc `modèle` que lorsqu'il désigne l'outil : précédé d'un article défini et
suivi ou précédé d'un mot du champ technique.

    uv run python scripts/check_pas_de_modele.py [chemins...]

Sans argument, contrôle tous les `.qmd` des deux langues. Sortie 1 si une mention subsiste.

Sur l'ARABE, seul le nom du dépôt est contrôlé : les collocations françaises n'y ont pas
d'équivalent mécanique, et « النموذج » veut aussi bien dire « le formulaire ». Ce n'est pas
une lacune grave — l'arabe est engendré depuis le français par la passe de traduction, de
sorte qu'un français propre donne un arabe propre. Le nom, lui, traverse la traduction tel
quel : c'est justement le cas qu'il faut attraper.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).parent.parent

# Le nom du dépôt, sous toutes ses graphies, est interdit sans condition.
NOM = re.compile(r"openfisca", re.I)

# Le mot « modèle » a des emplois parfaitement légitimes en droit — « le modèle français
# de carrière », « le modèle de score de l'AMEN », « le modèle de la déclaration ». Vouloir
# les distinguer de l'outil par la grammaire produit surtout des faux positifs : la première
# version de ce contrôle signalait les trois. On s'en tient donc à des COLLOCATIONS sans
# ambiguïté, quitte à laisser passer une tournure inédite — qu'une relecture attrapera, et
# qu'on ajoutera ici. Mieux vaut un contrôle qu'on croit qu'un contrôle qui crie.
COLLOCATIONS = [
    r"param[éè]tr\w*\s+(?:du|de\s+ce)\s+modèle",
    r"(?:le|ce)\s+modèle\s+(?:porte|applique|date|calcule|retient|ignore|connaît|encode)",
    r"que\s+porte\s+(?:le|ce)\s+modèle",
    r"(?:dans|selon|d'après|pour)\s+(?:le|ce)\s+modèle\b",
    r"(?:opéré|retenue?|portée?|encodée?)\s+par\s+(?:le|ce)\s+modèle",
    r"(?:du|au)\s+modèle\s+(?:de\s+microsimulation|socio-fiscal)",
    r"modèle\s+de\s+microsimulation",
]
# Deux emplois légitimes se glissent dans ces collocations — « dans le modèle français »,
# « du modèle de score » — et sont écartés par ce garde.
LEGITIME = r"(?!\s*(?:français|de\s+score|de\s+\*?scoring|de\s+la\s+déclaration))"
MODELE = re.compile("|".join(f"(?:{c}){LEGITIME}" for c in COLLOCATIONS), re.I)


def lignes_rendues(chemin: Path):
    """Numérote les lignes que le lecteur voit — hors blocs de code et commentaires."""
    dans_code = dans_commentaire = False
    for numero, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if ligne.lstrip().startswith("```"):
            dans_code = not dans_code
            continue
        if dans_code:
            continue
        if "<!--" in ligne:
            dans_commentaire = True
        fin = "-->" in ligne
        if dans_commentaire:
            if fin:
                dans_commentaire = False
            continue
        yield numero, ligne


def controle(chemin: Path) -> list[tuple[int, str, str]]:
    fautes = []
    for numero, ligne in lignes_rendues(chemin):
        for motif, quoi in ((NOM, "le nom du modèle"), (MODELE, "« le modèle »")):
            trouve = motif.search(ligne)
            if trouve:
                fautes.append((numero, quoi, trouve.group(0)))
                break
    return fautes


def main(argv: list[str]) -> int:
    if argv:
        fichiers = [Path(a) for a in argv]
    else:
        fichiers = sorted(
            f for f in (RACINE / "precis").rglob("*.qmd")
            if not f.name.startswith("_glossaire") and "/public/" not in f.as_posix()
        )

    total = 0
    for chemin in fichiers:
        for numero, quoi, extrait in controle(chemin):
            rel = chemin.relative_to(RACINE) if chemin.is_absolute() else chemin
            print(f"{rel}:{numero} : {quoi} dans le texte rendu — « {extrait} »")
            total += 1

    if total:
        print()
        print(f"{total} mention(s) du modèle dans le texte rendu.")
        print("Le précis documente la loi, pas le modèle : voir docs/conventions-redaction.md.")
        print("Destination d'un constat sur le modèle : un commentaire <!-- TODO (rôle) : … -->,")
        print("une issue sur openfisca-tunisia, ou docs/notes/backlog-modele.md.")
        return 1

    print(f"{len(fichiers)} fichier(s) contrôlé(s) : aucune mention du modèle dans le texte rendu.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

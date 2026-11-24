"""Modules de figures du livre « Les entreprises publiques », partagés avec ce livre.

Le chapitre « Les entreprises publiques de l'énergie » vient de ce livre-là ; ses figures sont
tracées par les mêmes modules que celles des autres entreprises publiques. Le dossier de ce
livre est ajouté au chemin d'import : le paquet `figures`, sans `__init__.py`, est un paquet
d'espace de noms et réunit alors les deux dossiers `figures/` — il n'y a qu'une source :

    from figures.ep import grandes_entreprises as ge
    from figures.ep import cotees as ct

Les modules lisent leurs données par des chemins relatifs à leur propre fichier ; les figdata
qu'ils écrivent vont dans le dossier du livre qui rend, ici `energie/figdata`.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

_LIVRE_EP = str(Path(__file__).resolve().parents[2] / "entreprises_publiques")
if _LIVRE_EP not in sys.path:
    sys.path.append(_LIVRE_EP)

grandes_entreprises = importlib.import_module("figures.grandes_entreprises")
cotees = importlib.import_module("figures.cotees")

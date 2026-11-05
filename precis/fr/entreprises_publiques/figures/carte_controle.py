"""Totaux de la carte de contrôle des entreprises publiques (annexe « Qui contrôle quoi »).

    from figures import carte_controle as cc
    cc.totaux()        # un paragraphe asis : combien de relations, de contrôleurs, hors liste

D'OÙ VIENNENT LES DONNÉES. Du relevé versionné de la carte de contrôle (un `.csv` du dossier
`listes`, avec son manifeste `.csv.yml`), engendré par `scripts/carte_controle.py`. La carte
réunit en une table les relations « contrôleur -> entité contrôlée » déjà documentées ailleurs :
périmètres de consolidation des groupes bancaires et de Tunisair, participations publiques dans
les sociétés cotées, portefeuille de l'ETAP, lignes nommées de la STEG, filiales de la STAR.
Chaque ligne garde sa clé de source ; les totaux sont comptés ici sur la carte.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

RELEVE = Path(__file__).resolve().parent.parent / "listes" / "carte-controle"


def _lire() -> pd.DataFrame:
    return pd.read_csv(f"{RELEVE}.csv", dtype=str, keep_default_na=False)


def _sources() -> list[str]:
    import yaml

    manifeste = yaml.safe_load(Path(f"{RELEVE}.csv.yml").read_text(encoding="utf-8"))
    return list(manifeste["sources"])


def comptes() -> dict[str, int]:
    """Nombres comptés sur la carte."""
    df = _lire()
    hors = df.loc[df["controlee_dans_liste_officielle"] == "non", "controlee"]
    return {
        "relations": len(df),
        "controleurs": df["controleur"].nunique(),
        "controlees": df["controlee"].nunique(),
        "controlees_hors_liste": hors.nunique(),
    }


def totaux() -> None:
    """Imprime, en asis, le paragraphe des totaux de la carte, avec sa ligne de source."""
    c = comptes()
    source = f"Source : {', '.join('@' + k for k in _sources())}."
    print(
        f"**La carte de contrôle réunit {c['relations']} relations de contrôle ou de "
        f"participation : {c['controleurs']} entités en contrôlent ou en détiennent "
        f"{c['controlees']} autres, dont {c['controlees_hors_liste']} ne figurent pas dans la "
        f"liste officielle des entreprises publiques — c'est le périmètre réel, bien plus large "
        f"que la liste.** "
        + source
    )


if __name__ == "__main__":
    print(comptes())

"""Les dinars constants du précis : un indice des prix et une année de base, partagés.

Un seul indice et une seule année de base pour toutes les figures en dinars constants des
volumes qui l'emploient — « Le marché du travail » (salaire minimum, salaires déclarés,
grilles des conventions collectives), « Prestations sociales » (prestations familiales) :

  - `ipc-longue-periode` : l'indice des prix à la consommation, base 100 en 1970, 1962-2023 ;
  - `bct-ipc-base2015` : l'indice en base 2015 que relaie la Banque centrale, dont la
    variation prolonge le premier au-delà de sa dernière année.

Dinars constants : montant × IPC(ANNEE_BASE) / IPC(année). Pour un montant fixé par un texte,
le montant de l'année est la moyenne des montants en vigueur au premier jour de chacun des
douze mois (`figtools.moyenne_annuelle_escalier`). Le module ne lit que `figtools.series()`.

Un module de figures l'importe par `import dinars_constants` — `scripts/` est sur le chemin
de tout chapitre. Celui du marché du travail le réexporte sous son ancien nom
(`precis/fr/marche_travail/figures/deflateur.py`).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figtools  # noqa: E402

SERIE_IPC = "ipc-longue-periode"
SERIE_IPC_RECENT = "bct-ipc-base2015"
# Les séries à citer dans l'onglet « Sources » d'une figure en dinars constants.
SERIES_IPC = (SERIE_IPC, SERIE_IPC_RECENT)
# Année des dinars constants : la dernière dont l'indice des prix est publié, jamais une année
# à venir.
ANNEE_BASE = 2025


def ipc() -> dict[int, float]:
    """Indice des prix, base 1970 ; prolongé au-delà de sa dernière année par la variation de
    l'indice en base 2015 que relaie la Banque centrale."""
    indice = {int(r.annee): float(r.indice_base1970)
              for r in figtools.series(SERIE_IPC).itertuples()}
    recent = {int(r.annee): float(r.valeur)
              for r in figtools.series(SERIE_IPC_RECENT).itertuples()}
    fin = max(indice)
    for annee in sorted(a for a in recent if a > fin and fin in recent):
        indice[annee] = indice[fin] * recent[annee] / recent[fin]
    return indice


def en_dinars_constants(montant: float, annee: int, indice: dict[int, float] | None = None,
                        base: int = ANNEE_BASE) -> float:
    """Un montant de l'année `annee` en dinars de l'année de base."""
    indice = indice or ipc()
    return montant * indice[base] / indice[annee]

"""Le déflateur du volume « Le marché du travail » : indice des prix et année des dinars constants.

Un seul indice et une seule année de base pour toutes les figures du volume en dinars
constants — le salaire minimum, les salaires déclarés, les grilles des conventions
collectives :

  - `ipc-longue-periode` : l'indice des prix à la consommation, base 100 en 1970, 1962-2023 ;
  - `bct-ipc-base2015` : l'indice en base 2015 que relaie la Banque centrale, dont la
    variation prolonge le premier au-delà de sa dernière année.

Dinars constants : montant × IPC(ANNEE_BASE) / IPC(année). Le module ne lit que
`figtools.series()`.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
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

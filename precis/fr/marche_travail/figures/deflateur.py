"""Le déflateur du volume « Le marché du travail » : indice des prix et année des dinars constants.

L'indice et l'année de base sont ceux du précis, partagés avec les autres volumes :
`scripts/dinars_constants.py` les définit, ce module les réexporte sous les noms que les
figures du volume emploient.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
from dinars_constants import (  # noqa: E402, F401
    ANNEE_BASE, SERIE_IPC, SERIE_IPC_RECENT, SERIES_IPC, ipc,
)

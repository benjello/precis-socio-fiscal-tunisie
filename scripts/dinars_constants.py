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


# --- le dernier mois publié : « monnaie de 2026 » ---------------------------------------------
#
# L'indice annuel moyen de 2026 n'existe pas avant la fin de l'année. Une valeur « de 2026 » est
# donc ramenée au dernier indice MENSUEL publié, jamais à une moyenne annuelle ni à une
# prévision : le coefficient d'une année est
#
#     indice du dernier mois publié / indice annuel moyen de cette année.
#
# L'indice du dernier mois est en base 2015 (bulletin mensuel de la statistique de l'INS) ; l'indice
# annuel est celui du reste du module (base 1970 jusqu'en 2023, prolongé par la variation de l'indice
# en base 2015). Le raccord se fait sur 2025, dont l'indice annuel en base 2015 (186,3) est aussi la
# « moyenne mensuelle » du bulletin : le coefficient de l'année 2025 est le rapport des indices de
# base 2015 du dernier mois et de 2025 ; celui d'une autre année s'en déduit par l'indice annuel du
# module. Le montant ainsi obtenu est un calcul, jamais une observation.

SERIE_IPC_MENSUEL = "ins-ipc-mensuel-base2015"


def dernier_indice_mensuel() -> tuple[str, float, float]:
    """(mois, indice du mois en base 2015, moyenne mensuelle de 2025 en base 2015) du dernier
    mois publié de la série `ins-ipc-mensuel-base2015`."""
    d = figtools.series(SERIE_IPC_MENSUEL)
    mensuel = d[d["nature"] == "indice mensuel"].sort_values("periode")
    dernier = mensuel.iloc[-1]
    annuel = float(d[d["periode"].astype(str) == "2025"]["indice_base2015"].iloc[0])
    return str(dernier["periode"]), float(dernier["indice_base2015"]), annuel


def coefficient_dernier_mois(annee: int, indice: dict[int, float] | None = None) -> float:
    """Coefficient qui ramène un montant de l'année `annee` à la monnaie du dernier mois publié."""
    indice = indice or ipc()
    _mois, dernier, annuel_2025 = dernier_indice_mensuel()
    return indice[2025] * dernier / annuel_2025 / indice[annee]

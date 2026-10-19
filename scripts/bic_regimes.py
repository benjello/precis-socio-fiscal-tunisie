"""Impôt des bénéfices industriels et commerciaux selon le régime : calcul pur, testé.

Composant des figures du chapitre « Impôt sur le revenu » (section du régime forfaitaire).
Il compare, pour un chiffre d'affaires donné, trois façons d'être imposé :

  - le RÉGIME FORFAITAIRE : un impôt lu sur le chiffre d'affaires seul. Ce n'est PAS un
    barème par tranche (`taux_bareme.montant_du`) : l'annexe II du code (1990-2010) fixe un
    MONTANT FORFAITAIRE pour la tranche où tombe le chiffre d'affaires, sans fraction par
    tranche ; les articles 44 *ter* (depuis 2011) fixent un taux avec plancher, puis un montant
    fixe jusqu'à 10 000 D et un taux au-delà ;
  - l'IMPÔT FORFAITAIRE OPTIONNEL : un montant fixe (1 500 D de 1999 à 2010 ; 4 000 ou 5 000 D
    selon la classe depuis 2026) ;
  - le RÉGIME RÉEL : le barème de l'impôt sur le revenu appliqué au bénéfice, sans que l'impôt
    descende sous le minimum d'impôt assis sur le chiffre d'affaires (art. 44 § II). Le bénéfice
    est une HYPOTHÈSE : une fraction `tau` du chiffre d'affaires.

Un forfait est une liste de MORCEAUX `(bas, haut, montant, taux, plancher)` : pour un chiffre
d'affaires `ca` tel que `bas < ca <= haut` (comme les tableaux du précis : « 3 000 à 6 000 »,
la tranche s'ouvre à 3 000,001), l'impôt est `montant` si `taux` est vide, sinon
`max(plancher, taux × ca)`. Au-delà du dernier `haut`, le régime n'est plus ouvert :
`None`, jamais 0.

Un minimum d'impôt est `(forme, taux, montant)` :
  - « plafonne » (1990-2005) : `min(taux × ca, montant)` — le texte dit que le minimum « ne peut
    excéder » le montant ;
  - « plancher » (depuis 2006) : `max(taux × ca, montant)`, exigible même sans chiffre d'affaires.

Le module ne lit que `figtools.series()` (séries de `precis/_seriescache/`, écrites par
`scripts/generate_forfait_bic_series.py`) ; il ne contient aucune valeur de droit.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import taux_bareme  # noqa: E402

Morceau = tuple[float, float, float | None, float | None, float | None]


def _vide(v) -> bool:
    return v is None or (isinstance(v, float) and math.isnan(v))


def impot_forfait(morceaux: list[Morceau], ca: float) -> float | None:
    """Impôt du forfait pour le chiffre d'affaires `ca` ; `None` hors du champ du régime."""
    if ca <= 0:
        return None
    for bas, haut, montant, taux, plancher in morceaux:
        if bas < ca <= haut:
            if _vide(taux):
                return float(montant)
            return max(0.0 if _vide(plancher) else float(plancher), float(taux) * ca)
    return None


def plafond(morceaux: list[Morceau]) -> float:
    """Chiffre d'affaires maximal du régime."""
    return max(haut for _bas, haut, *_r in morceaux)


def minimum_impot(forme: str, taux: float, montant: float, ca: float) -> float:
    """Minimum d'impôt de l'article 44 § II pour le chiffre d'affaires `ca`."""
    if forme == "plafonne":
        return min(taux * ca, montant)
    if forme == "plancher":
        return max(taux * ca, montant)
    raise ValueError(f"forme de minimum inconnue : {forme!r}")


def impot_reel(bareme: taux_bareme.Bareme, minimum: tuple[str, float, float], ca: float,
               tau: float) -> float:
    """Impôt du régime réel : barème sur le bénéfice `tau × ca`, jamais sous le minimum."""
    forme, t, m = minimum
    return max(taux_bareme.montant_du(bareme, tau * ca), minimum_impot(forme, t, m, ca))


# ------------------------------------------------------------------------------ lecture


def morceaux_a_l_etat(d, etat: int, regime: str, activite: str, zone: str) -> list[Morceau]:
    """Morceaux de la série `bic-forfait-tarifs` pour un état, un régime, une activité, une zone."""
    sous = d[(d["etat"] == etat) & (d["regime"] == regime) & (d["activite"] == activite)
             & (d["zone"].fillna("") == zone)].sort_values("bas")
    return [(float(r.bas), float(r.haut),
             None if _vide(r.montant) else float(r.montant),
             None if _vide(r.taux) else float(r.taux),
             None if _vide(r.plancher) else float(r.plancher)) for r in sous.itertuples()]


def variantes_a_l_etat(d, etat: int) -> list[tuple[str, str, str]]:
    """(régime, activité, zone) présents à l'état `etat`, dans l'ordre de la série."""
    sous = d[d["etat"] == etat]
    vues = []
    for r in sous.itertuples():
        cle = (r.regime, r.activite, "" if _vide(r.zone) else r.zone)
        if cle not in vues:
            vues.append(cle)
    return vues


def minimum_a_l_annee(d, annee: int) -> tuple[str, float, float]:
    """Minimum d'impôt en vigueur pour `annee` : dernière ligne d'effet au plus égal à `annee`."""
    sous = d[d["annee_effet"] <= annee].sort_values("annee_effet")
    if sous.empty:
        raise ValueError(f"aucun minimum d'impôt en {annee}")
    r = sous.iloc[-1]
    return (r["forme"], float(r["taux"]), float(r["montant"]))

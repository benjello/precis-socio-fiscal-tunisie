#!/usr/bin/env python3
"""Garde-fou de cohérence des séries de dette de l'annexe « dette publique ».

Vérifie les invariants de `docs/notes/dette-concordance.md` à partir des séries snapshotées
(`precis/_seriescache/`) et des citations de figures de `precis/fr/annexe-dette-publique.qmd`.
Sort en échec (code 1) au premier invariant rompu : c'est le contrôle qui aurait attrapé l'erreur
de base d'encours de l'effet-change (dette extérieure budgétaire 62 539 au lieu de l'encours MLT
total ≈ 80 000).

Usage : uv run python scripts/check_dette_coherence.py
À intégrer à scripts/verifier.sh.
"""

import csv
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
QMD = RACINE / "precis" / "fr" / "annexe-dette-publique.qmd"
TOL_IDENTITE = 2.0       # MDT, pour les identités int+ext=total et variation=change+volume
TOL_TOTAL_PCT = 3.0      # %, écart toléré entre total budgétaire et dette_MDT (révisions RA vs MdF)
MARGE_ORDRE = 1.20       # le PPG (converti au change moyen) peut sous-estimer : marge large

erreurs = []


def _lire(sid):
    f = CACHE / f"{sid}.csv"
    if not f.exists():
        erreurs.append(f"série absente du cache : {sid}")
        return []
    return list(csv.DictReader(f.open(encoding="utf-8")))


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def check_identite(sid, a, b, total, nom):
    for r in _lire(sid):
        va, vb, vt = _num(r.get(a)), _num(r.get(b)), _num(r.get(total))
        if None in (va, vb, vt):
            continue
        if abs((va + vb) - vt) > TOL_IDENTITE:
            erreurs.append(f"{nom} ({sid}, {r.get('annee')}): {a}+{b}={va+vb:.1f} ≠ {total}={vt:.1f}")


def check_total_vs_mdf():
    mdf = {int(r["annee"]): _num(r["dette_MDT"]) for r in _lire("finances-publiques-indicateurs")
           if r.get("annee", "").isdigit()}
    for r in _lire("dette-publique-interieur-exterieur"):
        an = r.get("annee", "")
        if not an.isdigit():
            continue
        tot, ref = _num(r.get("total_MDT")), mdf.get(int(an))
        if None in (tot, ref) or ref == 0:
            continue
        if abs(tot - ref) / ref * 100 > TOL_TOTAL_PCT:
            erreurs.append(f"total budgétaire ({an}): {tot:.0f} MDT ≠ dette_MDT MdF {ref:.0f} "
                           f"({abs(tot-ref)/ref*100:.1f} % > {TOL_TOTAL_PCT} %)")


def check_ordre_exterieur():
    """État budgétaire extérieur ≤ PPG (converti en dinars) : le PPG ajoute la part garantie."""
    chg = {int(r["annee"]): _num(r["dinar_par_usd"]) for r in _lire("change-dinar")
           if r.get("annee", "").isdigit()}
    ppg = {int(r["annee"]): _num(r["encours_MUSD"]) for r in _lire("dette-exterieure-echeancier")
           if r.get("annee", "").isdigit()}
    for r in _lire("dette-publique-interieur-exterieur"):
        an = r.get("annee", "")
        if not an.isdigit() or int(an) not in ppg or int(an) not in chg:
            continue
        etat_ext = _num(r.get("exterieur_MDT"))
        ppg_mdt = ppg[int(an)] * chg[int(an)]        # MUSD × dinar/USD = MDT
        if etat_ext and ppg_mdt and etat_ext > ppg_mdt * MARGE_ORDRE:
            erreurs.append(f"ordre extérieur ({an}): État budg. {etat_ext:.0f} > PPG converti "
                           f"{ppg_mdt:.0f} MDT — périmètres incohérents ?")


def check_ordre_mlt_total():
    """Dette extérieure de l'État (budgétaire) ≤ encours MLT total tous secteurs (même devise, MDT).
    Invariant fort : le périmètre le plus large contient le plus étroit."""
    mlt = {int(r["annee"]): _num(r["encours_mlt_total_MDT"])
           for r in _lire("dette-exterieure-encours-mlt-total") if r.get("annee", "").isdigit()}
    for r in _lire("dette-publique-interieur-exterieur"):
        an = r.get("annee", "")
        if not an.isdigit() or int(an) not in mlt:
            continue
        etat_ext = _num(r.get("exterieur_MDT"))
        if etat_ext and etat_ext > mlt[int(an)] * 1.01:
            erreurs.append(f"ordre MLT ({an}): État ext. budg. {etat_ext:.0f} > encours MLT total "
                           f"{mlt[int(an)]:.0f} MDT — le total tous secteurs doit être le plus large")


def check_overlap_mlt_ra():
    """Approximation RA (encours MLT 2013-2019) vs A10 : écart borné au recouvrement (≤ 3 %).
    Matérialise la règle 'une approximation doit quantifier son écart'."""
    a10 = {int(r["annee"]): _num(r["encours_mlt_total_MDT"])
           for r in _lire("dette-exterieure-encours-mlt-total") if r.get("annee", "").isdigit()}
    for r in _lire("dette-exterieure-encours-mlt-ra"):
        an = r.get("annee", "")
        if not an.isdigit() or int(an) not in a10:
            continue
        ra = _num(r.get("encours_mlt_ra_MDT"))
        ref = a10[int(an)]
        if ra and ref and abs(ra - ref) / ref > 0.03:
            erreurs.append(f"overlap MLT RA/A10 ({an}): RA {ra:.0f} vs A10 {ref:.0f} "
                           f"= {abs(ra-ref)/ref*100:.1f} % — approximation RA hors de la marge (3 %)")


def check_devises_somme():
    cols = ["eur_pct", "usd_pct", "yen_pct", "kwd_pct", "autres_pct"]
    for sid in ("dette-exterieure-devises", "dette-exterieure-devises-ra"):
        for r in _lire(sid):
            s = sum(_num(r.get(c)) or 0 for c in cols)
            if not (99 <= s <= 101):
                erreurs.append(f"parts par devise [{sid}] ({r.get('annee')}): somme {s:.1f} ≠ 100")


def check_figures_citent_series():
    if not QMD.exists():
        erreurs.append("annexe introuvable : " + str(QMD))
        return
    texte = QMD.read_text(encoding="utf-8")
    snapshot = {p.stem for p in CACHE.glob("*.csv")}
    cites = set()
    for bloc in re.findall(r"figure_tabs\((.*?)slug\s*=", texte, re.S):
        cites |= set(re.findall(r'"([a-z][a-z0-9-]+)"', bloc))
    for sid in sorted(cites):
        if sid not in snapshot:
            erreurs.append(f"figure cite une série absente du cache : {sid}")


def main():
    check_identite("dette-publique-interieur-exterieur", "interieur_MDT", "exterieur_MDT",
                   "total_MDT", "identité int+ext=total (budgétaire)")
    check_identite("dette-etat-interieur-exterieur", "etat_interieur_MDT", "etat_exterieur_MDT",
                   "etat_total_MDT", "identité int+ext=total (monétaire)")
    check_identite("dette-exterieure-effet-change", "effet_change_MDT", "effet_volume_MDT",
                   "variation_MDT", "identité effet-change+volume=variation")
    check_total_vs_mdf()
    check_ordre_exterieur()
    check_ordre_mlt_total()
    check_overlap_mlt_ra()
    check_devises_somme()
    check_figures_citent_series()

    if erreurs:
        print(f"check_dette_coherence : {len(erreurs)} invariant(s) ROMPU(S)")
        for e in erreurs:
            print("  ✗", e)
        return 1
    print("check_dette_coherence : tous les invariants de dette-concordance.md sont vérifiés.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

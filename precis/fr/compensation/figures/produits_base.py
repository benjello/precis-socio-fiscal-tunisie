"""Figures des prix du chapitre « Les produits de base » (volume « La compensation »).

    from figures import produits_base as pb
    pb.figure("campagne", caption=…, note_lecture=…)   # prix de campagne des céréales, 1970-2026
    pb.figure("reduit", caption=…, note_lecture=…)     # prix réduit du blé aux minoteries, 1974-1991
    pb.figure("pain", caption=…, note_lecture=…)       # prix du pain au kilo et poids, 1975-2026
    pb.figure("derives", caption=…, note_lecture=…)    # farines, semoule, pâtes, couscous, 1975-1991
    pb.figure("sucre_huile_lait", caption=…, note_lecture=…)
    pb.regle_deflation()                               # la règle, pour la note de lecture

D'OÙ VIENNENT LES DONNÉES.

  - Les prix des céréales (prix de base à la production, prix d'intervention de l'orge, prix
    normal et prix réduit de rétrocession) : la série longue `compensation-cereales-parametres`
    de `_seriescache/`, lue par `figtools.series()` — une ligne par (grandeur, date d'effet),
    avec le texte et son lien ; une ligne sans valeur clôt la grandeur. Elle est émise par
    `scripts/generate_compensation_tables.py`, avec les tableaux `tables/cereales_*.md` et la
    liste des liens « Base législative » (`<série>.liens.fr.yml`). Ne pas l'éditer à la main.
  - Les prix au public des dérivés, du sucre, de l'huile et du lait : le relevé tenu à la main
    `precis/fr/compensation/releves/prix-produits-base.csv` (manifeste `.csv.yml`), une ligne
    par (série, date d'effet), valeur courante, poids du pain, texte. Une ligne sans valeur
    marque une date où la valeur cesse d'être établie : le trait s'arrête là.

La provenance des deux est déclarée ici (`register_provenance`), avec les seules clés de
citation présentes dans la bibliographie du livre. L'indice des prix vient de
`dinars_constants` (donc de `figtools.series()`).

RÈGLES.

  - **Dinars courants et dinars de l'année de base** (`dinars_constants.ANNEE_BASE`), deux vues
    de chaque figure. Un prix daté se ramène par la moyenne des valeurs en vigueur au premier
    de chaque mois de l'année (escalier), une année incomplète restant vide. Aucune année
    au-delà de l'indice.
  - **Les familles ne se raccordent pas** : le prix d'intervention de l'orge (depuis le
    6 septembre 1993) n'est pas relié à son prix de base ; une valeur d'un rapport de la Banque
    centrale est en marque creuse ou en pointillé, jamais confondue avec une valeur fixée par
    un texte.
  - **Les ruptures** ont un trait vertical et un triangle porteur d'une infobulle.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.ticker import FuncFormatter, MultipleLocator  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

RELEVES = Path(__file__).resolve().parents[1] / "releves"
CEREALES = "compensation-cereales-parametres"
PRIX = "compensation-prix-produits-base"
BASE = dinars_constants.ANNEE_BASE

BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN = (
    "#0969da", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#57606a", "#9a6700")

PRODUITS = {"ble_dur": ("Blé dur", BLEU), "ble_tendre": ("Blé tendre", ORANGE),
            "orge": ("Orge", VERT)}
SERIES = {
    "pain_gros": ("Gros pain", BLEU),
    "pain_petit": ("Petit pain, puis baguette (1991)", ORANGE),
    "farine": ("Farine panifiable", BRUN),
    "farine_ps7": ("Farine PS-7", GRIS),
    "semoule": ("Semoule", BLEU),
    "pates": ("Pâtes alimentaires", VERT),
    "couscous": ("Couscous", VIOLET),
    "sucre": ("Sucre en poudre", BLEU),
    "huile": ("Huile mélangée, puis huile de graines (1991)", VERT),
    "lait_uht": ("Lait régénéré, UHT", BLEU),
    "lait_pasteurise": ("Lait régénéré, pasteurisé", ORANGE),
}
UNITE = {"pain_gros": "millimes la pièce", "pain_petit": "millimes la pièce",
         "farine": "millimes le kilo", "farine_ps7": "millimes le kilo",
         "semoule": "millimes le kilo",
         "pates": "millimes le kilo", "couscous": "millimes le kilo",
         "sucre": "millimes le kilo", "huile": "millimes le litre",
         "lait_uht": "millimes le litre", "lait_pasteurise": "millimes le litre"}


def _nb(v: float, dec: int = 0) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _x(date_iso: str) -> float:
    return figtools.abscisse_date(str(date_iso)[:10])


def _ipc() -> dict[int, float]:
    return dinars_constants.ipc()


def _coeff(annee: int) -> float | None:
    i = _ipc()
    return i[BASE] / i[annee] if annee in i else None


def regle_deflation() -> str:
    """La règle de déflation, pour la note de lecture et l'onglet « Sources »."""
    i = _ipc()
    fin = max(a for a in i if a <= BASE)
    annee = ("la valeur d'une année est la moyenne des prix en vigueur au premier jour de "
             "chacun des douze mois, ramenée par l'indice annuel moyen de cette année ; une "
             "année dont un mois n'a pas de prix établi n'a pas de point")
    return (f"Dinars de {BASE} : valeurs calculées, non observées. Le coefficient d'une année est "
            f"l'indice des prix à la consommation de {BASE} divisé par celui de l'année "
            "(moyennes annuelles) ; " + annee + ". L'indice est la série longue base 100 en "
            "1970 : jusqu'en 1975, l'indice du coût de la vie que publie la Banque centrale (base "
            "1962, raccordée en 1970), d'un périmètre différent de celui de l'INS ; de 1976 à 2023, "
            "l'indice des prix à la consommation familiale de l'INS ; prolongé en 2024 et 2025 par la "
            "variation de l'indice en base 2015 que relaie la Banque centrale (indice de "
            f"{fin} : {_nb(i[fin], 1)} en base 1970, par ce raccord). Aucune valeur n'est "
            f"ramenée au-delà de {fin}.")


# --- lecture des données ---------------------------------------------------------------------

# Les grandeurs de la série des céréales : clé -> (libellé, couleur, style de trait).
POINTILLE, TIRETS = (0, (1, 1.5)), (0, (4, 2))
CEREALES_COURBES = {
    "ble_dur_prix_base": ("Blé dur, prix de base à la production", BLEU, "-"),
    "ble_tendre_prix_base": ("Blé tendre, prix de base à la production", ORANGE, "-"),
    "orge_prix_base": ("Orge, prix de base à la production", VERT, "-"),
    "orge_prix_intervention": ("Orge, prix d'intervention", VERT, POINTILLE),
    "ble_dur_prix_normal": ("Blé dur, prix normal de rétrocession", BLEU, TIRETS),
    "ble_tendre_prix_normal": ("Blé tendre, prix normal de rétrocession", ORANGE, TIRETS),
    "orge_prix_normal": ("Orge, prix normal de rétrocession", VERT, TIRETS),
    "ble_dur_prix_reduit": ("Blé dur, prix réduit de rétrocession", BLEU, "-"),
    "ble_tendre_prix_reduit": ("Blé tendre, prix réduit de rétrocession", ORANGE, "-"),
}
CAMPAGNE_CLES = [k for k in CEREALES_COURBES if not k.endswith("_reduit")]
REDUIT_CLES = ["ble_dur_prix_reduit", "ble_tendre_prix_reduit",
               "ble_dur_prix_normal", "ble_tendre_prix_normal"]
# Dates d'effet où le prix normal de rétrocession change de composition : son trait s'y
# interrompt.
COUPURES_NORMAL = ("1993-09-06", "2008-06-16")


def _cereales(cles) -> dict:
    """{clé: [(date, valeur ou None, état, texte, lien)]}, lu dans la série engendrée."""
    return figtools.serie_escalier(CEREALES, cles)


def _cles_cereales(lignes: dict) -> list[str]:
    """Les clés de citation des textes de la série, parmi celles de la bibliographie du livre.

    Le numéro du texte (« n° 70-261 ») donne `decret70-261` ou `decret70-261-oc` ;
    l'arrêté conjoint de 2026 a sa clé propre."""
    import re

    connues, cles = figtools._ref_index(), []
    for lg in lignes.values():
        for _d, _v, _e, texte, _l in lg:
            m = re.search(r"n°\s*(\d{2,4}-\d+)", texte or "")
            candidats = ([f"decret{m.group(1)}", f"decret{m.group(1)}-oc"] if m
                         else ["arrete2026-07-24-oc"] if "24 juillet 2026" in (texte or "")
                         else [])
            for c in candidats:
                if c in connues and c not in cles:
                    cles.append(c)
    return cles


def _prix() -> pd.DataFrame:
    d = pd.read_csv(RELEVES / "prix-produits-base.csv", dtype=str, keep_default_na=False)
    d["rang"] = d["rang"].astype(int)
    d["annee"] = d["annee"].astype(int)
    return d.sort_values(["serie", "rang"]).reset_index(drop=True)


def _cles(d: pd.DataFrame) -> list[str]:
    return list(dict.fromkeys(c for c in d["cle"] if c))


def _declarer(cles_cereales=None, cles_prix=None) -> None:
    connues = figtools._ref_index()
    if cles_cereales is not None:
        figtools.register_provenance(
            CEREALES, titre="Prix des céréales fixés par les textes de campagne, 1970-2026",
            sources=[k for k in cles_cereales if k in connues],
            unite="dinars courants le quintal",
            perimetre=("prix de base à la production du blé dur, du blé tendre et de l'orge, "
                       "prix d'intervention de l'orge, prix normal et prix réduit de "
                       "rétrocession, à la date d'effet de chaque décret de campagne, puis de "
                       "l'arrêté conjoint de la récolte 2026"),
            caveats=regle_deflation())
    if cles_prix is not None:
        figtools.register_provenance(
            PRIX, titre="Prix administrés des produits de base, 1974-2020",
            sources=[k for k in cles_prix if k in connues],
            unite="millimes ou dinars courants (colonne « Unité »)",
            perimetre=("prix de vente au public fixés par décret ou par arrêté, poids du pain ; "
                       "trois valeurs tirées des rapports de la Banque centrale ; prix de la "
                       "farine et de la semoule rendus au chef-lieu de délégation ou à la "
                       "fabrique (1975, 1979), dans les données, non tracés"),
            caveats=regle_deflation())


# --- outils de tracé -------------------------------------------------------------------------

def _repere(ax, x: float, texte: str) -> None:
    ax.axvline(x, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
    p, = ax.plot([x], [1], marker=7, ms=6, color=GRIS, clip_on=False, zorder=5,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _cadre(ax, ylabel: str, pas_x: int = 5) -> None:
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    _axe_x(ax, pas_x)


def _axe_x(ax, pas: int = 5) -> None:
    """Graduations entières des années."""
    ax.xaxis.set_major_locator(MultipleLocator(pas))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}"))


def _legende(ax, poignees, ncol=2, y=-0.14) -> None:
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


def _marches(s: pd.DataFrame, par_kilo: bool = False):
    """Les marches d'une série datée : [(x, valeur ou None, pointillé, ligne)], et les points
    isolés d'un rapport (valeur sans date, en tête de série).

    Une ligne sans date d'effet et avec valeur (rapport de la Banque centrale) ouvre une marche
    en pointillé au 1er janvier de l'année suivante, l'année elle-même restant vide ; en tête de
    série, c'est un prix antérieur, montré par une marque creuse à la date de la ligne suivante.
    Une ligne sans valeur interrompt le trait à sa date (ou au 1er janvier de son année).
    Une ligne « poids seul » (poids du pain, sans prix) ou « autre stade » (prix rendu au
    chef-lieu de délégation ou à la fabrique, non au public) n'est pas tracée : elle reste dans
    les données.
    """
    marches, isoles = [], []
    lignes = [r for r in s.itertuples(index=False)
              if r.statut not in ("poids seul", "autre stade")]
    for i, r in enumerate(lignes):
        v = None
        if r.valeur:
            v = float(r.valeur)
            if par_kilo:
                v = v * 1000 / float(r.poids_g)
        if r.date_effet:
            marches.append((_x(r.date_effet), v, False, r))
        elif v is not None and i == 0:
            suivante = lignes[1]
            isoles.append((_x(suivante.date_effet), v, r))
        elif v is not None:
            marches.append((float(r.annee), None, False, r))
            marches.append((float(r.annee + 1), v, True, r))
        else:
            marches.append((float(r.annee), None, False, r))
    return marches, isoles


def _valeur_au(marches, x: float):
    retenue = (None, False)
    for xm, v, poin, _ in marches:
        if xm <= x + 1e-9:
            retenue = (v, poin)
    return retenue


def _annuel(marches) -> dict[int, tuple[float, bool]]:
    """{année: (moyenne au premier de chaque mois, issue d'un rapport)} ; année incomplète omise."""
    if not marches:
        return {}
    debut, fin = int(marches[0][0]), int(marches[-1][0])
    sortie = {}
    for a in range(debut, fin + 1):
        mois = [_valeur_au(marches, a + (m - 1) / 12) for m in range(1, 13)]
        if any(v is None for v, _ in mois) or a > max(_ipc()):
            continue
        sortie[a] = (sum(v for v, _ in mois) / 12, any(p for _, p in mois))
    return sortie


def _trace_marches(ax, marches, isoles, couleur, nom, unite, fmt=lambda v: _nb(v)) -> None:
    for (x0, v, poin, r), (x1, *_rest) in zip(marches, marches[1:]):
        if v is None:
            continue
        ax.plot([x0, x1], [v, v], color=couleur, lw=2 if not poin else 1.4,
                ls=(0, (3, 2)) if poin else "-", solid_capstyle="butt", zorder=3)
        p, = ax.plot([x0], [v], "o", ms=4.5, color=couleur, mfc="white" if poin else couleur,
                     zorder=4)
        quand = r.date_effet or f"{r.annee}, date non établie"
        figtools.infobulle(p, f"{quand} · {nom} : {fmt(v)} {unite} ({r.texte})")
    for x, v, r in isoles:
        p, = ax.plot([x - 0.08], [v], "o", ms=5, color=couleur, mfc="white", zorder=4)
        figtools.infobulle(p, f"avant le {marches[0][3].date_effet} · {nom} : {fmt(v)} {unite} "
                              f"({r.texte})")


def _trace_annuel(ax, annuel, couleur, nom, unite, fmt=lambda v: _nb(v)) -> None:
    annees = sorted(annuel)
    xs, ys = [], []
    for a in annees:
        v = annuel[a][0] * _coeff(a)
        if xs and a != xs[-1] + 1:
            ax.plot(xs, ys, color=couleur, lw=1.4, zorder=3)
            xs, ys = [], []
        xs.append(a); ys.append(v)
    if xs:
        ax.plot(xs, ys, color=couleur, lw=1.4, zorder=3)
    for a in annees:
        moy, rapport = annuel[a]
        v = moy * _coeff(a)
        p, = ax.plot([a], [v], "o", ms=4.5, color=couleur, mfc="white" if rapport else couleur,
                     zorder=4)
        figtools.infobulle(p, f"{a} · {nom} : {fmt(v)} {unite} de {BASE}, valeur calculée "
                              f"(moyenne de l'année {fmt(moy)} × {_nb(_coeff(a), 3)})")


def _table_prix(series: list[str], par_kilo: tuple[str, ...] = ()) -> pd.DataFrame:
    """Données : les lignes des textes, puis les moyennes annuelles (calculées)."""
    d = _prix()
    lignes = []
    for s in series:
        sd = d[d["serie"] == s]
        unite = UNITE[s] if s not in par_kilo else "millimes le kilo"
        for r in sd.itertuples(index=False):
            v = r.valeur and float(r.valeur)
            vk = v * 1000 / float(r.poids_g) if (v and s in par_kilo) else v
            lignes.append({
                "Série": SERIES[s][0], "Ligne": "valeur du texte",
                "Date d'effet": r.date_effet or "non établie", "Année": r.annee,
                "Règle de date": r.regle_date, "Valeur courante": vk if vk != "" else None,
                "Unité": unite, "Poids (g)": r.poids_g or None,
                "Prix de la pièce (millimes)": (v if s in par_kilo and v else None),
                f"Coefficient de {BASE} (calculé)": None,
                f"Valeur de {BASE} (calculée)": None,
                "Texte": r.texte, "Statut": r.statut, "Remarque": r.remarque})
        marches, _ = _marches(sd, par_kilo=s in par_kilo)
        for a, (moy, rapport) in sorted(_annuel(marches).items()):
            lignes.append({
                "Série": SERIES[s][0], "Ligne": "moyenne annuelle (calculée)",
                "Date d'effet": "", "Année": a, "Règle de date": "",
                "Valeur courante": round(moy, 3), "Unité": unite, "Poids (g)": None,
                "Prix de la pièce (millimes)": None,
                f"Coefficient de {BASE} (calculé)": round(_coeff(a), 4),
                f"Valeur de {BASE} (calculée)": round(moy * _coeff(a), 1),
                "Texte": "", "Statut": "rapport BCT" if rapport else "", "Remarque": ""})
    return pd.DataFrame(lignes)


# --- 1 et 2. Les prix des céréales, en escalier ----------------------------------------------

def _segments(lignes, fin: float):
    """Les marches d'une grandeur : [(x0, x1, valeur, ligne)], valeur None exclue.

    Une marche court de sa date d'effet à la suivante ; la dernière, jusqu'à `fin`."""
    xs = [_x(lg[0]) for lg in lignes] + [fin]
    return [(x0, x1, lg[1], lg) for lg, x0, x1 in zip(lignes, xs, xs[1:]) if lg[1] is not None]


def _trace_escalier(ax, lignes, couleur, ls, nom, fin: float, coupures=()) -> None:
    """Escalier : marches horizontales, raccordées par un trait vertical sauf aux `coupures`.

    Un point plein à chaque changement de valeur, un point creux à une reprise sans
    changement ; chacun porte une infobulle (date, valeur, texte)."""
    segs = _segments(lignes, fin)
    for (x0, x1, v, lg), suivant in zip(segs, segs[1:] + [None]):
        ax.plot([x0, x1], [v, v], color=couleur, ls=ls, lw=1.6, solid_capstyle="butt", zorder=3)
        if suivant and abs(suivant[0] - x1) < 1e-9 and suivant[3][0] not in coupures:
            ax.plot([x1, x1], [v, suivant[2]], color=couleur, ls=ls, lw=1.0, zorder=3)
        creux = lg[2] == "reprise"
        p, = ax.plot([x0], [v], "o", ms=3.2, color=couleur, mfc="white" if creux else couleur,
                     zorder=4)
        figtools.infobulle(p, f"{lg[0]} · {nom} : {_nb(v, 3)} D le quintal ({lg[3]})")


def _annuel_cereales(lignes, fin: str | None = None) -> dict[int, float]:
    """{année: moyenne des prix en vigueur au premier de chaque mois}, années de l'indice.

    `fin` (date ISO) : la grandeur n'est lue que jusqu'à la veille de cette date ; une année
    qu'elle coupe n'a pas de point."""
    if not lignes:
        return {}
    debut, fin_ipc = int(lignes[0][0][:4]), max(_ipc())
    if fin:
        lignes = [lg for lg in lignes if lg[0] < fin] + [(fin, None, "suppression", "", "")]
    sortie = {}
    for a in range(debut, fin_ipc + 1):
        m = figtools.moyenne_annuelle_escalier(lignes, a)
        if m is not None:
            sortie[a] = m
    return sortie


def _trace_annuel_cereales(ax, annuel, couleur, ls, nom, coupures=()) -> None:
    annees_coupure = {int(c[:4]) for c in coupures}
    xs, ys = [], []
    for a in sorted(annuel):
        v = annuel[a] * _coeff(a)
        if xs and (a != xs[-1] + 1 or a in annees_coupure):
            ax.plot(xs, ys, color=couleur, ls=ls, lw=1.6, zorder=3)
            xs, ys = [], []
        xs.append(a); ys.append(v)
        p, = ax.plot([a], [v], "o", ms=3.2, color=couleur, zorder=4)
        figtools.infobulle(p, f"{a} · {nom} : {_nb(v, 1)} D de {BASE} le quintal, valeur "
                              f"calculée (moyenne de l'année {_nb(annuel[a], 3)} D × "
                              f"{_nb(_coeff(a), 3)})")
    if xs:
        ax.plot(xs, ys, color=couleur, ls=ls, lw=1.6, zorder=3)


def _table_cereales(lignes: dict, cles, fin: str | None = None) -> pd.DataFrame:
    """Données : les lignes des textes, puis les moyennes annuelles (calculées)."""
    rangs = []
    for cle in cles:
        nom = CEREALES_COURBES[cle][0]
        for date, v, etat, texte, lien in lignes.get(cle, []):
            rangs.append({"Grandeur": nom, "Ligne": "valeur du texte", "Date d'effet": date,
                          "Année": int(date[:4]), "Dinars courants le quintal": v,
                          f"Coefficient de {BASE} (calculé)": None,
                          f"Dinars de {BASE} le quintal (calculés)": None,
                          "Texte": texte, "Lien": lien,
                          "Remarque": {"suppression": "fin de la grandeur",
                                       "reprise": "valeur reprise sans changement"}.get(etat, "")})
        for a, m in sorted(_annuel_cereales(lignes.get(cle, []), fin).items()):
            rangs.append({"Grandeur": nom, "Ligne": "moyenne annuelle (calculée)",
                          "Date d'effet": "", "Année": a,
                          "Dinars courants le quintal": round(m, 3),
                          f"Coefficient de {BASE} (calculé)": round(_coeff(a), 4),
                          f"Dinars de {BASE} le quintal (calculés)": round(m * _coeff(a), 2),
                          "Texte": "", "Lien": "", "Remarque": ""})
    return pd.DataFrame(rangs)


RUPTURES_CAMPAGNE = (
    ("1993-09-06", "6 septembre 1993, décret de la récolte 1992 : « La commercialisation de "
                   "l'orge est libre » (décret n° 93-1721, art. 1er) ; l'orge n'a plus qu'un "
                   "prix d'intervention. Le prix normal de rétrocession comprend désormais une "
                   "prime forfaitaire, 0,100 D au fonds d'équipement et les primes de "
                   "magasinage."),
    ("2008-06-16", "16 juin 2008, décret de la récolte 2008 : le prix normal de rétrocession "
                   "comprend la prime exceptionnelle de prompte livraison (décret n° 2008-2081, "
                   "art. 8 c)."),
)


def _poignees_cereales(cles):
    return [Line2D([0], [0], color=CEREALES_COURBES[k][1], ls=CEREALES_COURBES[k][2], lw=1.8,
                   label=figtools.fig_text(CEREALES_COURBES[k][0])) for k in cles]


def fig_campagne(constants: bool = False):
    figtools.apply_lang_font()
    lignes = _cereales(CAMPAGNE_CLES)
    fig, ax = plt.subplots(figsize=(9.5, 6.0))
    fin_ipc = max(_ipc())
    for cle in CAMPAGNE_CLES:
        nom, couleur, ls = CEREALES_COURBES[cle]
        coupures = COUPURES_NORMAL if cle.endswith("_prix_normal") else ()
        if constants:
            _trace_annuel_cereales(ax, _annuel_cereales(lignes.get(cle, [])), couleur, ls, nom,
                                   coupures)
        else:
            _trace_escalier(ax, lignes.get(cle, []), couleur, ls, nom, 2027.0, coupures)
    for date, texte in RUPTURES_CAMPAGNE:
        _repere(ax, _x(date), texte)
    if constants:
        _cadre(ax, f"Dinars de {BASE} le quintal (calculés)")
        ax.set_xlim(1970, fin_ipc + 1)
        ax.set_ylim(0, None)
    else:
        _cadre(ax, "Dinars courants le quintal (échelle logarithmique)")
        ax.set_yscale("log")
        ax.set_yticks([2, 5, 10, 20, 50, 100, 200])
        ax.set_xlim(1970, 2027)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v)))
    ax.set_xlabel(figtools.fig_text("Année"))
    poignees = _poignees_cereales(CAMPAGNE_CLES)
    poignees.append(Line2D([0], [0], marker=7, color=GRIS, ls="none", ms=6,
                           label=figtools.fig_text("rupture de série (infobulle sur le triangle)")))
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _figure_campagne():
    lignes = _cereales(CAMPAGNE_CLES)
    vues = [("Dinars courants", fig_campagne()),
            (f"Dinars de {BASE} (calculés)", fig_campagne(constants=True))]
    _declarer(cles_cereales=_cles_cereales(lignes))
    return (vues, _table_cereales(lignes, CAMPAGNE_CLES),
            (CEREALES, *dinars_constants.SERIES_IPC), "fig_compensation_pb_prix_campagne")


# Le prix réduit court de la récolte 1974 au décret de la récolte 1990 (4 juillet 1991), qui
# le renvoie à un acte du ministre ; le prix normal n'est tracé qu'en regard, sur la même
# période.
FIN_REDUIT = "1991-07-04"


def _lignes_reduit() -> dict:
    lignes = _cereales(REDUIT_CLES)
    for cle in ("ble_dur_prix_normal", "ble_tendre_prix_normal"):
        lignes[cle] = [lg for lg in lignes.get(cle, []) if "1974-01-01" <= lg[0] < FIN_REDUIT]
    return lignes


def fig_reduit(constants: bool = False):
    figtools.apply_lang_font()
    lignes = _lignes_reduit()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for cle in REDUIT_CLES:
        nom, couleur, ls = CEREALES_COURBES[cle]
        if constants:
            _trace_annuel_cereales(ax, _annuel_cereales(lignes[cle], FIN_REDUIT), couleur, ls,
                                   nom)
        else:
            _trace_escalier(ax, lignes[cle], couleur, ls, nom, _x(FIN_REDUIT))
    _repere(ax, _x("1983-12-28") if not constants else 1984,
            "28 décembre 1983 : prix réduits relevés à 15,600 et 13,000 D le quintal (décret "
            "n° 83-1274) ; retour aux prix antérieurs le 1er mars 1984 (décret n° 84-150)")
    _cadre(ax, f"Dinars de {BASE} le quintal (calculés)" if constants
           else "Dinars courants le quintal")
    ax.set_xlim(1973.5, 1992)
    ax.set_ylim(0, None)
    _axe_x(ax, 2)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 1 if v % 1 else 0)))
    ax.set_xlabel(figtools.fig_text("Année"))
    _legende(ax, _poignees_cereales(REDUIT_CLES), ncol=2)
    fig.tight_layout()
    return fig


def _figure_reduit():
    lignes = _lignes_reduit()
    _declarer(cles_cereales=_cles_cereales(lignes))
    vues = [("Dinars courants", fig_reduit()),
            (f"Dinars de {BASE} (calculés)", fig_reduit(constants=True))]
    return (vues, _table_cereales(lignes, REDUIT_CLES, FIN_REDUIT),
            (CEREALES, *dinars_constants.SERIES_IPC), "fig_compensation_pb_prix_reduit")


# --- 3. Pain : prix au kilo et poids ---------------------------------------------------------

def fig_pain(constants: bool = False):
    figtools.apply_lang_font()
    d = _prix()
    fig, (ax, axp) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=False,
                                  gridspec_kw={"height_ratios": [3, 1.3]})
    for serie in ("pain_gros", "pain_petit"):
        nom, couleur = SERIES[serie]
        s = d[d["serie"] == serie]
        marches, isoles = _marches(s, par_kilo=True)
        if constants:
            _trace_annuel(ax, _annuel(marches), couleur, nom, "millimes le kilo")
        else:
            _trace_marches(ax, marches, isoles, couleur, nom, "millimes le kilo")
        # Poids : un point à chaque texte qui le fixe ou le change ; le trait court jusqu'à
        # la fin de 2026, le poids de 2020 étant celui de l'arrêté en vigueur.
        p = s[(s["poids_g"] != "") & s["statut"].isin(["texte", "poids seul"])]
        p = p[[True] + [a != b for a, b in zip(p["poids_g"].iloc[1:], p["poids_g"].iloc[:-1])]]
        xs = [_x(r.date_effet) for r in p.itertuples(index=False)] + [2027.0]
        for (x0, r), x1 in zip(zip(xs, p.itertuples(index=False)), xs[1:]):
            w = float(r.poids_g)
            axp.plot([x0, x1], [w, w], color=couleur, lw=2, solid_capstyle="butt")
            q, = axp.plot([x0], [w], "o", ms=4, color=couleur, zorder=4)
            figtools.infobulle(q, f"{r.date_effet} · {nom} : {_nb(w)} g ({r.texte})")
            axp.annotate(f"{_nb(w)} g", xy=(x0, w), xytext=(2, 4), textcoords="offset points",
                         fontsize=7, color=couleur)
    _cadre(ax, f"Millimes de {BASE} le kilo (calculés)" if constants
           else "Millimes courants le kilo")
    ax.set_xlim(1974.5, 1993)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v)))
    poignees = [Line2D([0], [0], color=SERIES[s][1], lw=2, marker="o", ms=4,
                       label=figtools.fig_text(SERIES[s][0])) for s in ("pain_gros", "pain_petit")]
    poignees.append(Line2D([0], [0], color=GRIS, lw=1.4, ls=(0, (3, 2)), marker="o", mfc="white",
                           ms=4, label=figtools.fig_text("Rapport de la Banque centrale")))
    _legende(ax, poignees, ncol=3, y=-0.08)
    _axe_x(ax, 2)
    _cadre(axp, "Poids (g)")
    axp.set_xlim(1974.5, 2027.5)
    axp.set_ylim(150, 760)
    axp.set_xlabel(figtools.fig_text("Année"))
    fig.tight_layout()
    return fig


def _figure_pain():
    series = ["pain_gros", "pain_petit"]
    table = _table_prix(series, par_kilo=tuple(series))
    d = _prix()
    _declarer(cles_prix=_cles(d[d["serie"].isin(series)]))
    vues = [("Millimes courants", fig_pain()),
            (f"Millimes de {BASE} (calculés)", fig_pain(constants=True))]
    return vues, table, (PRIX, *dinars_constants.SERIES_IPC), "fig_compensation_pb_prix_pain"


# --- 4. Dérivés des céréales -----------------------------------------------------------------

def _fig_multi(series, xlim, ylabel_unite, constants):
    figtools.apply_lang_font()
    d = _prix()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for serie in series:
        nom, couleur = SERIES[serie]
        marches, isoles = _marches(d[d["serie"] == serie])
        if constants:
            _trace_annuel(ax, _annuel(marches), couleur, nom, ylabel_unite)
        else:
            _trace_marches(ax, marches, isoles, couleur, nom, ylabel_unite)
    _cadre(ax, (f"{ylabel_unite.capitalize().replace('Millimes', 'Millimes de ' + str(BASE))} "
                "(calculés)") if constants else f"{ylabel_unite.capitalize()}, courants")
    ax.set_xlim(*xlim)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v)))
    ax.set_xlabel(figtools.fig_text("Année"))
    poignees = [Line2D([0], [0], color=SERIES[s][1], lw=2, marker="o", ms=4,
                       label=figtools.fig_text(SERIES[s][0])) for s in series]
    _legende(ax, poignees, ncol=min(len(series), 3))
    fig.tight_layout()
    return fig


def _figure_derives():
    series = ["farine", "farine_ps7", "semoule", "pates", "couscous"]
    d = _prix()
    _declarer(cles_prix=_cles(d[d["serie"].isin(series)]))
    vues = [("Millimes courants", _fig_multi(series, (1974.5, 1992.5), "millimes le kilo", False)),
            (f"Millimes de {BASE} (calculés)",
             _fig_multi(series, (1974.5, 1992.5), "millimes le kilo", True))]
    return (vues, _table_prix(series), (PRIX, *dinars_constants.SERIES_IPC),
            "fig_compensation_pb_prix_derives")


# --- 5. Sucre, huile, lait -------------------------------------------------------------------

PANNEAUX_SHL = (("Sucre en poudre (millimes le kilo)", ("sucre",), "millimes le kilo"),
                ("Huile mélangée, vrac (millimes le litre)", ("huile",), "millimes le litre"),
                ("Lait régénéré, 1 l (millimes le litre)", ("lait_uht", "lait_pasteurise"),
                 "millimes le litre"))


def fig_sucre_huile_lait(constants: bool = False):
    figtools.apply_lang_font()
    d = _prix()
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.4), sharex=True)
    for ax, (titre, series, unite) in zip(axes, PANNEAUX_SHL):
        for serie in series:
            nom, couleur = SERIES[serie]
            marches, isoles = _marches(d[d["serie"] == serie])
            if constants:
                _trace_annuel(ax, _annuel(marches), couleur, nom, unite)
            else:
                _trace_marches(ax, marches, isoles, couleur, nom, unite)
        ax.set_title(figtools.fig_text(titre), fontsize=8.5)
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_ylim(0, None)
        ax.set_xlim(1973.5, 1992.5)
        _axe_x(ax, 5)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v)))
        if len(series) > 1:
            ax.legend(handles=[Line2D([0], [0], color=SERIES[s][1], lw=2,
                                      label=figtools.fig_text(SERIES[s][0].split(", ")[1]))
                               for s in series], fontsize=7, frameon=False, loc="lower right")
    axes[0].set_ylabel(figtools.fig_text(f"Millimes de {BASE} (calculés)" if constants
                                         else "Millimes courants"))
    fig.tight_layout()
    return fig


def _figure_sucre_huile_lait():
    series = ["sucre", "huile", "lait_uht", "lait_pasteurise"]
    d = _prix()
    _declarer(cles_prix=_cles(d[d["serie"].isin(series)]))
    vues = [("Millimes courants", fig_sucre_huile_lait()),
            (f"Millimes de {BASE} (calculés)", fig_sucre_huile_lait(constants=True))]
    return (vues, _table_prix(series), (PRIX, *dinars_constants.SERIES_IPC),
            "fig_compensation_pb_prix_sucre_huile_lait")


FIGURES = {"campagne": _figure_campagne, "reduit": _figure_reduit, "pain": _figure_pain,
           "derives": _figure_derives, "sucre_huile_lait": _figure_sucre_huile_lait}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, series_ids, slug = FIGURES[nom]()
    figtools.figure_tabs(vues, table, *series_ids, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")

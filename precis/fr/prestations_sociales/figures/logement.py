"""Figure « prélèvements des lois de finances sur les ressources du fonds de promotion du
logement pour les salariés, 1987-2026 ».

    from figures import logement as fig_log
    fig_log.vues_prelevements()
    fig_log.table_prelevements()

D'OÙ VIENNENT LES DONNÉES. La série `log-prelevements-fonds` du cache du précis donne, pour
chaque année de 1987 à 2026, ce que les lois de finances de l'année (initiale et
complémentaires) disent du fonds :

  - `prelevement` : un montant lu, par bénéficiaire (article, page, édition) ;
  - `aucun` : la loi de finances de l'année a été lue et ne contient aucune disposition de
    ce type : la valeur est 0, avec la loi et l'édition lues ;
  - `transfert_global` : une loi de finances complémentaire transfère au budget de l'État
    des recettes de l'ensemble des fonds spéciaux du Trésor, sans désigner le fonds : le
    montant est celui de l'ensemble, la part du fonds n'est pas connue ; il n'est jamais
    ajouté aux barres ;
  - une année absente de la série est une année non lue : case vide, jamais zéro.

LES DÉNOMINATEURS. Deux vues rapportent les prélèvements à une grandeur de l'année, sans
jamais déflater :

  - « part des dépenses de l'État » : les réalisations de dépenses de l'État hors service de
    la dette, du ministère des Finances (série `denominateurs-depenses-etat-pib`, 1986-2025) ;
  - « part du PIB » : le PIB aux prix courants de chacune des trois bases des comptes
    nationaux (1983, 1997, 2015), série `pib-courant-par-base` (annexe du site sur le PIB).
    Chaque base est une barre distincte, aucun coefficient de passage n'est calculé et une
    année publiée dans deux bases porte deux barres. Avant 1992, aucune base n'est connue :
    le PIB du ministère des Finances est dit « base 1983 présumée ».
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "log-prelevements-fonds"
SERIE_DEPENSES = "denominateurs-depenses-etat-pib"
SERIE_PIB = "pib-courant-par-base"
SERIES_DEN = (SERIE_DEPENSES, SERIE_PIB)

BLEU, ORANGE, VERT, VIOLET = "#08519c", "#bc4c00", "#1a7f37", "#8250df"
GRIS, ROUGE = "#57606a", "#cf222e"
_BENEF = {
    "programme national de résorption des logements rudimentaires": BLEU,
    "Fonds national d'amélioration de l'habitat": ORANGE,
    "Compte national de solidarité sociale": VERT,
    "Budget de l'État (titre I)": VIOLET,
}
_BASES = {1983: ("#1a7f37", "base 1983"), 1997: ("#8250df", "base 1997"),
          2015: ("#0969da", "base 2015")}
DEBUT, FIN = 1987, 2026
INTEGRATION = (1987, 1994)  # liste de l'article 92 de la loi n° 86-106, jusqu'à la LF 1995

SOURCES = [
    "loi86-106-lf1987", "loi-87-83-lf-1988", "loi88-145-lf1989", "loi-89-115-lf-1990",
    "lf-1991", "lfc-1991", "lf-1992", "lf-1993", "lf-1994", "lf-1995", "lf-1996", "lf-1997",
    "lf-1998", "lf-1999", "lf-2000", "lf-2001", "lfc-2002", "lf-2003", "lfc-2004", "lf-2005",
    "lfc-2005", "lf-2006", "lfc-2007", "lfc-2008", "lf-2009", "lfc-2009", "lf-2010",
    "dl-2011-56-lfc-2011", "lfc-2012", "lf-2013", "lfc-2013", "lf-2014", "lfc-2014", "lf-2015",
    "lfc-2015", "lf-2016", "lfc-2016", "lf-2017", "lfc-2017", "lf-2018", "lfc-2018",
    "loi2018-56-lf2019", "lfc-2019", "lf-2020", "lf-2021", "lfr-2021", "dl2021-21-lf2022",
    "lfr-2022", "lf-2023", "lfc-2023", "lf-2024", "lf-2025", "lf-2026"]

figtools.register_provenance(
    SERIE,
    titre="Ce que les lois de finances disent des ressources du fonds de promotion du logement "
          "pour les salariés, 1987-2026 : prélèvements lus, années lues sans prélèvement, "
          "transferts globaux",
    titre_ar="ما تقوله قوانين المالية عن موارد صندوق النهوض بالمساكن للأجراء، 1987-2026",
    sources=SOURCES,
    unite="millions de dinars courants",
    unite_ar="بملايين الدنانير الجارية",
    perimetre=("lois de finances initiales et complémentaires de 1987 à 2026 : une ligne par "
               "année et par bénéficiaire pour un prélèvement, une ligne par année pour une "
               "année lue sans prélèvement ou pour un transfert global"),
    perimetre_ar="قوانين المالية الأصلية والتكميلية من 1987 إلى 2026",
    caveats=("Montants fixés par les textes, non les sommes effectivement prélevées. Une année "
             "marquée « aucun prélèvement » est une année dont la loi de finances (et la loi de "
             "finances complémentaire, s'il y en a une) a été lue et ne contient aucune "
             "disposition de ce type ; une année sans marque n'est pas lue. Les années 1991 à "
             "1994 sont lues sur l'image des fascicules, les autres sur leur texte ; 2023 à "
             "2025 dans l'édition arabe. Un transfert global de l'ensemble des fonds spéciaux "
             "du Trésor n'est pas un montant du fonds."),
    caveats_ar="المبالغ هي المحددة في النصوص وليست المبالغ المقتطعة فعليا.",
)

_L = {
    "titre": {"fr": "Prélèvements sur les ressources du fonds, 1987-2026",
              "ar": "الاقتطاعات من موارد الصندوق، 1987-2026"},
    "v_md": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "v_dep": {"fr": "Part des dépenses de l'État", "ar": "حصة نفقات الدولة"},
    "v_pib": {"fr": "Part du PIB", "ar": "حصة الناتج المحلي الإجمالي"},
    "y_md": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_dep": {"fr": "En % des dépenses de l'État hors service de la dette",
              "ar": "% من نفقات الدولة دون خدمة الدين"},
    "y_pib": {"fr": "En % du PIB de la base", "ar": "% من ناتج الأساس"},
    "x": {"fr": "Année", "ar": "السنة"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _serie():
    return figtools.series(SERIE)


def _vide(valeur) -> bool:
    return str(valeur) in ("nan", "", "None")


def _depenses() -> dict[int, float]:
    d = figtools.series(SERIE_DEPENSES)
    d = d[d["depenses_etat_hors_dette_MDT"].notna()]
    return {int(a): float(v) for a, v in zip(d["annee"], d["depenses_etat_hors_dette_MDT"])}


def _pib() -> dict[int, list[dict]]:
    """Par année, une entrée par base du PIB : la base, son état (présumée, non rattachée)."""
    d = figtools.series(SERIE_PIB)
    sortie: dict[int, list[dict]] = {}
    for r in d.itertuples(index=False):
        base = str(r.base)
        num = next((b for b in (1983, 1997, 2015) if str(b) in base), None)
        sortie.setdefault(int(r.annee), []).append({
            "base": num, "presumee": "présumée" in base, "minfin": base.startswith("non rattachée"),
            "pib": float(r.pib_MD), "retropole": str(r.retropole)})
    return sortie


def _totaux() -> dict[int, float]:
    d = _serie()
    d = d[d["statut"] == "prelevement"]
    sortie: dict[int, float] = {}
    for a, v in zip(d["annee"], d["part_MD"]):
        sortie[int(a)] = sortie.get(int(a), 0.0) + float(v)
    return sortie


def _etiquette_base(e: dict) -> str:
    if e["minfin"]:
        return "PIB du ministère des Finances, non rattaché à une base"
    if e["presumee"]:
        return "base 1983 présumée"
    return f"base {e['base']}" + (" (PIB recalculé par l'INS)" if e["retropole"] == "oui" else "")


def _decor(ax, ft):
    ax.axvspan(INTEGRATION[0] - 0.5, INTEGRATION[1] + 0.5, color="#8b949e", alpha=0.12, lw=0,
               zorder=0)
    ax.set_xlim(DEBUT - 1, FIN + 1)
    ax.set_xticks(range(DEBUT, FIN + 1, 3))
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.grid(True, axis="y", alpha=0.3)


def _marques_zero(ax, ft):
    """Année lue sans prélèvement : un point à zéro ; transfert global : un triangle."""
    d = _serie()
    for r in d[d["statut"] == "aucun"].itertuples(index=False):
        p, = ax.plot([r.annee], [0], "o", ms=4, color="#8c959f", zorder=6, clip_on=False)
        figtools.infobulle(p, f"{r.annee} · aucun prélèvement : {r.texte} ({r.edition})")
    for r in d[d["statut"] == "transfert_global"].itertuples(index=False):
        p, = ax.plot([r.annee], [0.035], "^", ms=7, mfc="white", mec=ROUGE, mew=1.4, zorder=7,
                     transform=ax.get_xaxis_transform(), clip_on=False)
        figtools.infobulle(p, f"{r.annee} · {r.texte}, {r.article} : {_nb(r.montant_MD)} MD "
                              f"pour l'ensemble des fonds spéciaux du Trésor ; part du fonds "
                              f"non identifiée")


def _legende(ax, ft, handles, bas=-0.14):
    handles = handles + [
        Line2D([], [], marker="o", ls="none", ms=4, color="#8c959f",
               label=ft("année lue, aucun prélèvement (zéro)")),
        Line2D([], [], marker="^", ls="none", ms=7, mfc="white", mec=ROUGE, mew=1.4,
               label=ft("transfert global de tous les fonds spéciaux, part du fonds inconnue")),
        Patch(facecolor="#8b949e", alpha=0.25,
              label=ft("1987-1994 : recettes du fonds versées au budget de l'État"))]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, bas), ncol=1,
              fontsize=7.8, frameon=False)


def _vue_empilee(mesure: str):
    """`md` : millions de dinars ; `dep` : part des dépenses de l'État."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _serie()
    d = d[d["statut"] == "prelevement"]
    dep = _depenses()
    fig, ax = plt.subplots(figsize=(10, 6.2))
    bas: dict[int, float] = {}
    for benef, couleur in _BENEF.items():
        for r in d[d["beneficiaire"] == benef].itertuples(index=False):
            a = int(r.annee)
            v = float(r.part_MD) if mesure == "md" else 100 * float(r.part_MD) / dep[a]
            b = ax.bar([a], [v], bottom=[bas.get(a, 0.0)], width=0.72, color=couleur,
                       edgecolor="white", lw=0.4, zorder=3)
            texte = f"{a} · {benef} : {_nb(float(r.part_MD))} MD"
            if mesure == "dep":
                texte += (f", soit {_nb(v, 2)} % des {_nb(dep[a], 0)} MD de dépenses de l'État "
                          f"hors service de la dette")
            figtools.infobulle(b[0], texte + f" ({r.texte}, {r.article})")
            bas[a] = bas.get(a, 0.0) + v
    for a, total in bas.items():
        ax.annotate(_nb(total, 0 if mesure == "md" else 2), (a, total),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=8,
                    color="#24292f")
    _decor(ax, ft)
    ax.set_ylim(0, max(bas.values()) * 1.18)
    ax.set_ylabel(ft(_lab("y_md" if mesure == "md" else "y_dep")))
    ax.set_title(ft(_lab("titre")))
    _marques_zero(ax, ft)
    poignees = [Patch(color=c, label=ft(b)) for b, c in _BENEF.items()
                if (d["beneficiaire"] == b).any()]
    _legende(ax, ft, poignees)
    fig.tight_layout()
    return fig


def _vue_pib():
    """Part du PIB : une barre par base du PIB, jamais raccordées."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    totaux = _totaux()
    pib = _pib()
    fig, ax = plt.subplots(figsize=(10, 6.2))
    ymax = 0.0
    larg = 0.3
    for a, total in sorted(totaux.items()):
        entrees = sorted(pib.get(a, []), key=lambda e: (e["base"] or 9999, e["minfin"]))
        n = len(entrees)
        for i, e in enumerate(entrees):
            x = a + (i - (n - 1) / 2) * larg
            v = 100 * total / e["pib"]
            ymax = max(ymax, v)
            if e["minfin"]:
                couleur, hach = "#8c959f", "///"
            else:
                couleur = _BASES[e["base"]][0]
                hach = "///" if e["presumee"] else None
            b = ax.bar([x], [v], width=larg, color=couleur, hatch=hach, edgecolor="white",
                       alpha=0.55 if e["presumee"] else 1.0, lw=0.4, zorder=3)
            figtools.infobulle(b[0], f"{a} · {_etiquette_base(e)} : {_nb(total)} MD sur un PIB "
                                     f"de {_nb(e['pib'], 0)} MD, soit {_nb(v, 3)} % du PIB")
            ax.annotate(_nb(v, 3), (x, v), textcoords="offset points", xytext=(0, 3),
                        ha="center", va="bottom", rotation=90, fontsize=6.5, color="#24292f")
    _decor(ax, ft)
    for annee, base in ((1997, 1997), (2010, 2015)):
        figtools.marque_rupture(ax, annee)
        ax.annotate(ft(f"PIB : base {base}"), xy=(annee - 0.5, 0),
                    xycoords=("data", "axes fraction"), xytext=(-4, 4),
                    textcoords="offset points", ha="right", va="bottom", fontsize=7, color=GRIS)
    ax.set_ylim(0, ymax * 1.3)
    ax.set_ylabel(ft(_lab("y_pib")))
    ax.set_title(ft(_lab("titre")))
    _marques_zero(ax, ft)
    poignees = [Patch(color=c, label=ft(f"{n}, PIB publié")) for _, (c, n) in _BASES.items()]
    poignees.append(Patch(color=_BASES[1983][0], alpha=0.55, hatch="///",
                          label=ft("base 1983 présumée (aucune base connue avant 1992)")))
    poignees.append(Patch(color="#8c959f", hatch="///",
                          label=ft("PIB du ministère des Finances, non rattaché à une base")))
    _legende(ax, ft, poignees)
    fig.tight_layout()
    return fig


def vues_prelevements():
    return [(_lab("v_md"), _vue_empilee("md")),
            (_lab("v_dep"), _vue_empilee("dep")),
            (_lab("v_pib"), _vue_pib())]


def fig_prelevements(mesure: str = "md"):
    return _vue_pib() if mesure == "pib" else _vue_empilee(mesure)


STATUTS = {"prelevement": "Prélèvement lu", "aucun": "Aucun prélèvement : loi lue",
           "transfert_global": "Transfert global de tous les fonds spéciaux (part du fonds inconnue)"}
COL_BASES = {1983: "% du PIB, base 1983 (présumée avant 1992)", 1997: "% du PIB, base 1997",
             2015: "% du PIB, base 2015"}
COL_MINFIN = "% du PIB du ministère, base non rattachée"


def table_prelevements():
    """Onglet Données : toutes les lignes de la série, avec les parts calculées."""
    import pandas as pd
    d = _serie()
    dep = _depenses()
    pib = _pib()
    lignes = []
    for r in d.itertuples(index=False):
        a = int(r.annee)
        part = None if _vide(r.part_MD) else float(r.part_MD)
        ligne = {
            "Année": a,
            "Statut": STATUTS[r.statut],
            "Bénéficiaire": "" if _vide(r.beneficiaire) else r.beneficiaire,
            "Montant (MD courants)": part,
            "Montant global d'un transfert (MD courants)":
                float(r.montant_MD) if r.statut == "transfert_global" else None,
            "% des dépenses de l'État hors service de la dette":
                None if part is None or a not in dep else round(100 * part / dep[a], 3)}
        for base, nom in COL_BASES.items():
            e = [x for x in pib.get(a, []) if x["base"] == base and not x["minfin"]]
            ligne[nom] = None if not e or part is None else round(100 * part / e[0]["pib"], 3)
        e = [x for x in pib.get(a, []) if x["minfin"]]
        ligne[COL_MINFIN] = None if not e or part is None else round(100 * part / e[0]["pib"], 3)
        ligne.update({
            "Texte lu": r.texte, "Article": "" if _vide(r.article) else r.article,
            "Pages du Journal officiel": "" if _vide(r.page) else str(r.page),
            "Édition": r.edition, "Source": r.source,
            "Remarque": "" if _vide(r.remarque) else r.remarque})
        lignes.append(ligne)
    return pd.DataFrame(lignes)

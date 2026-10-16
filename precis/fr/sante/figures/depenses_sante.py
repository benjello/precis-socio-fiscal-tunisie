"""Trois séries longitudinales, de périmètre et de source distincts.

Les figures ne lisent que figtools.series() (entrepôt ou snapshots du précis).
Budget ministériel, comptes de la CNAM et étude du CRES restent des figures
séparées ; les charges et les décaissements de la CNAM ont des vues distinctes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402


BUDGET = "ins-budget-sante-2018-2023"
CNAM = "cnam-comptes-2011-2021"
CRES = "cnam-parts-regimes-cres-2009-2019"
BENEFICIAIRES = "cnam-beneficiaires-cres-2008-2013"
AFFILIES = "cnam-affilies-filieres-2008-2021"
BLEU, VERT, ORANGE, GRIS = "#08519c", "#1a7f37", "#b45100", "#657487"

_L = {
    "annee": {"fr": "Année", "ar": "السنة"},
    "md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "part": {"fr": "Part (%)", "ar": "الحصة (%)"},
    "gestion": {"fr": "Gestion", "ar": "التصرف"},
    "developpement": {"fr": "Développement", "ar": "التنمية"},
    "total": {"fr": "Total du département Santé", "ar": "جملة نفقات وزارة الصحة"},
    "budget": {"fr": "Part des dépenses comparables de l'État", "ar": "الحصة من نفقات الدولة المماثلة"},
    "pib": {"fr": "Part du PIB (base 2015)", "ar": "الحصة من الناتج المحلي الإجمالي (أساس 2015)"},
    "techniques": {"fr": "Charges techniques", "ar": "الأعباء الفنية"},
    "administratives": {"fr": "Charges administratives", "ar": "الأعباء الإدارية"},
    "decaissees": {"fr": "Prestations décaissées", "ar": "المنافع المدفوعة نقدا"},
    "page": {"fr": "Page", "ar": "الصفحة"},
    "maladie": {"fr": "Assurance maladie", "ar": "التأمين على المرض"},
    "sociales": {"fr": "Assurances sociales", "ar": "التأمينات الاجتماعية"},
    "atmp": {"fr": "Accidents du travail et maladies professionnelles", "ar": "حوادث الشغل والأمراض المهنية"},
    "vue_budget_md": {"fr": "Montants (MD)", "ar": "المبالغ (مليون دينار)"},
    "vue_budget_parts": {"fr": "Parts du budget et du PIB", "ar": "الحصص من الميزانية والناتج"},
    "vue_cnam_resultat": {"fr": "Compte de résultat", "ar": "قائمة النتائج"},
    "vue_cnam_tresorerie": {"fr": "Trésorerie", "ar": "الخزينة"},
    "millions": {"fr": "millions", "ar": "مليون"},
    "millions_pers": {"fr": "Millions de personnes", "ar": "ملايين الأشخاص"},
    "beneficiaires": {"fr": "Bénéficiaires : affiliés et ayants droit (note du CRES)",
                      "ar": "المنتفعون: المضمونون وأولو الحق (مذكرة مركز البحوث والدراسات الاجتماعية)"},
    "affilies_total": {"fr": "Affiliés de la CNAM, total général",
                       "ar": "المضمونون لدى الكنام، المجموع العام"},
    "affilies_trois": {"fr": "Affiliés des trois filières de soins",
                       "ar": "المضمونون في منظومات العلاج الثلاث"},
    "rupture_2010": {"fr": "2010 : étudiants inscrits", "ar": "2010: الطلبة المرسمون"},
    "rupture_2019": {"fr": "2019 : affiliés ouvrant droit", "ar": "2019: المضمونون المنتفعون بالحق"},
}


def _lab(cle: str) -> str:
    return _L[cle][figtools.lang()]


def _serie(ident: str, debut: int, fin: int):
    d = figtools.series(ident).sort_values("annee")
    assert d.annee.tolist() == list(range(debut, fin + 1))
    return d


def _nb(valeur: float, dec: int = 1) -> str:
    return f"{valeur:,.{dec}f}".replace(",", " ").replace(".", ",")


def _courbe(ax, annees, valeurs, couleur: str, cle: str, unite: str,
            marqueur: str = "o", dec: int = 1):
    libelle = _lab(cle)
    ax.plot(annees, valeurs, color=couleur, lw=2, marker=marqueur, ms=4,
            label=figtools.fig_text(libelle))
    for annee, valeur in zip(annees, valeurs):
        (point,) = ax.plot([int(annee)], [float(valeur)], marker=marqueur,
                           ls="none", ms=14, color=couleur, alpha=0.01, zorder=5)
        figtools.infobulle(point, f"{int(annee)} · {libelle} : {_nb(float(valeur), dec)} {unite}")


def _habille(ax, annees, ylabel: str, ymin: float | None = 0):
    ax.set_xticks(annees)
    if ymin is not None:
        ax.set_ylim(bottom=ymin)
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d7dce2", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)


def vues_budget():
    figtools.apply_lang_font()
    d = _serie(BUDGET, 2018, 2023)
    annees = d.annee.tolist()
    fig1, ax = plt.subplots(figsize=(9.3, 4.8))
    for col, couleur, cle, marqueur in (
        ("gestion_sante_milliers", BLEU, "gestion", "o"),
        ("developpement_sante_milliers", VERT, "developpement", "s"),
    ):
        _courbe(ax, annees, d[col] / 1000, couleur, cle, "MD", marqueur)
    _courbe(ax, annees, d.sante_md, ORANGE, "total", "MD", "^", 1)
    _habille(ax, annees, _lab("md"))
    ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper left")
    fig1.tight_layout()

    fig2, ax = plt.subplots(figsize=(9.3, 4.8))
    _courbe(ax, annees, d.part_budget_pct, BLEU, "budget", "%", "o", 2)
    _courbe(ax, annees, d.part_pib_pct, ORANGE, "pib", "%", "s", 2)
    _habille(ax, annees, _lab("part"))
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig2.tight_layout()
    return [(_lab("vue_budget_md"), fig1), (_lab("vue_budget_parts"), fig2)]


def table_budget():
    d = _serie(BUDGET, 2018, 2023).copy()
    return d.rename(columns={
        "annee": _lab("annee"), "gestion_sante_milliers": "Gestion Santé (milliers D)",
        "developpement_sante_milliers": "Développement Santé (milliers D)",
        "gestion_etat_milliers": "Gestion État (milliers D)",
        "developpement_etat_milliers": "Développement État (milliers D)",
        "pib_base2015_md": "PIB base 2015 (MD)", "sante_md": "Total Santé (MD)",
        "budget_comparable_md": "Budget comparable (MD)",
        "part_budget_pct": "Santé / budget (%)", "part_pib_pct": "Santé / PIB (%)",
        "edition": "Édition dépenses",
    })


def vues_cnam():
    figtools.apply_lang_font()
    d = _serie(CNAM, 2011, 2021)
    annees = d.annee.tolist()
    fig1, (haut, bas) = plt.subplots(2, 1, figsize=(9.3, 6), sharex=True)
    _courbe(haut, annees, d.charges_techniques_milliers / 1000,
            BLEU, "techniques", "MD")
    _courbe(bas, annees, d.charges_administratives_milliers / 1000,
            ORANGE, "administratives", "MD")
    _habille(haut, annees, _lab("md"), None)
    _habille(bas, annees, _lab("md"), None)
    haut.legend(frameon=False, fontsize=9, loc="upper left")
    bas.legend(frameon=False, fontsize=9, loc="upper left")
    fig1.tight_layout()

    fig2, ax = plt.subplots(figsize=(9.3, 4.8))
    _courbe(ax, annees, d.prestations_decaissees_milliers / 1000,
            VERT, "decaissees", "MD")
    _habille(ax, annees, _lab("md"), None)
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    fig2.tight_layout()
    return [(_lab("vue_cnam_resultat"), fig1), (_lab("vue_cnam_tresorerie"), fig2)]


def _edition_cnam(fichier: str) -> str:
    """Exercices couverts par l'édition, d'après le nom du fichier source."""
    m = re.search(r"(\d{4})[-_](\d{4})", fichier)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    m = re.search(r"_(\d{2})_(\d{2})", fichier)
    assert m, fichier
    return f"20{m.group(1)}-20{m.group(2)}"


def table_cnam():
    d = _serie(CNAM, 2011, 2021).copy()
    d["edition"] = d["edition"].map(_edition_cnam)
    return d.rename(columns={
        "annee": _lab("annee"),
        "charges_techniques_milliers": "Charges techniques (milliers D)",
        "charges_administratives_milliers": "Charges administratives (milliers D)",
        "prestations_decaissees_milliers": "Prestations décaissées (milliers D)",
        "edition": "Édition des comptes",
    })


def fig_cres():
    figtools.apply_lang_font()
    d = _serie(CRES, 2009, 2019)
    annees = d.annee.tolist()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.3, 6.1), sharex=True)
    _courbe(haut, annees, d.assurance_maladie_pct, BLEU, "maladie", "%")
    _courbe(bas, annees, d.assurances_sociales_pct, VERT, "sociales", "%", "s")
    _courbe(bas, annees, d.atmp_pct, ORANGE, "atmp", "%", "^")
    _habille(haut, sorted(set(annees[::2] + [2019])), _lab("part"), None)
    _habille(bas, sorted(set(annees[::2] + [2019])), _lab("part"), 0)
    haut.set_ylim(85, 95)
    bas.set_ylim(0, 12)
    haut.legend(frameon=False, fontsize=9, loc="upper left")
    bas.legend(frameon=False, fontsize=8, loc="upper left", ncol=2)
    fig.tight_layout()
    return fig


def table_cres():
    return _serie(CRES, 2009, 2019).rename(columns={
        "annee": _lab("annee"), "assurance_maladie_pct": f"{_lab('maladie')} (%)",
        "assurances_sociales_pct": f"{_lab('sociales')} (%)",
        "atmp_pct": f"{_lab('atmp')} (%)", "page": _lab("page"),
    })


def fig_effectifs():
    """Deux panneaux sans axe vertical commun : bénéficiaires (CRES), puis affiliés (CNAM)."""
    figtools.apply_lang_font()
    b = _serie(BENEFICIAIRES, 2008, 2013)
    a = _serie(AFFILIES, 2008, 2021)
    annees = a.annee.tolist()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.3, 6.4), sharex=True)
    _courbe(haut, b.annee.tolist(), b.beneficiaires_millions, BLEU, "beneficiaires",
            _lab("millions"), dec=3)
    _courbe(bas, annees, a.total_general / 1e6, ORANGE, "affilies_total", _lab("millions"), dec=3)
    _courbe(bas, annees, a.total_trois_filieres / 1e6, VERT, "affilies_trois", _lab("millions"),
            "s", dec=3)
    # Axes partant de zéro, d'échelles distinctes : deux unités, aucune comparaison de niveau.
    _habille(haut, annees, _lab("millions_pers"))
    _habille(bas, annees, _lab("millions_pers"))
    haut.set_ylim(0, 8)
    bas.set_ylim(0, 4.5)
    for annee, cle in ((2010, "rupture_2010"), (2019, "rupture_2019")):
        bas.axvline(annee - 0.5, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
        bas.text(annee - 0.4, 0.15, figtools.fig_text(_lab(cle)), fontsize=8,
                 color=GRIS, va="bottom")
    haut.legend(frameon=False, fontsize=9, loc="lower right")
    bas.legend(frameon=False, fontsize=9, loc="upper left")
    bas.tick_params(axis="x", labelsize=8)
    fig.tight_layout()
    return fig


def table_effectifs():
    b = _serie(BENEFICIAIRES, 2008, 2013)[["annee", "beneficiaires_millions"]]
    a = _serie(AFFILIES, 2008, 2021).drop(columns="page")
    d = a.merge(b, on="annee", how="left")
    d = d[["annee", "beneficiaires_millions", "total_general", "total_trois_filieres",
           "filiere_publique", "filiere_privee", "systeme_remboursement",
           "faibles_revenus", "etudiants"]]
    # Années sans bénéficiaires publiés : case vide, et non « NaN », dans l'onglet Données.
    d["beneficiaires_millions"] = d["beneficiaires_millions"].astype(object).where(
        d["beneficiaires_millions"].notna(), "")
    return d.rename(columns={
        "annee": _lab("annee"),
        "beneficiaires_millions": "Bénéficiaires, CRES (millions)",
        "total_general": "Affiliés CNAM, total général",
        "total_trois_filieres": "Affiliés des trois filières",
        "filiere_publique": "Filière publique",
        "filiere_privee": "Filière privée",
        "systeme_remboursement": "Système de remboursement",
        "faibles_revenus": "Salariés à faibles revenus",
        "etudiants": "Étudiants",
    })


def tableau_filieres(annees: tuple[int, ...] | None = None, detail: bool = False) -> str:
    """Tableau Markdown des affiliés par filière, tiré de la série de la CNAM."""
    a = _serie(AFFILIES, 2008, 2021)
    if annees is not None:
        a = a[a.annee.isin(annees)]
    colonnes = [("filiere_publique", "Filière publique"), ("filiere_privee", "Filière privée"),
                ("systeme_remboursement", "Remboursement")]
    if detail:
        colonnes += [("total_trois_filieres", "Total trois modalités"),
                     ("faibles_revenus", "Salariés à faibles revenus"),
                     ("etudiants", "Étudiants"), ("total_general", "Total général CNAM")]
    else:
        colonnes.append(("total_trois_filieres", "Ensemble des trois modalités"))
    lignes = ["| Année | " + " | ".join(t for _, t in colonnes) + " |",
              "|---|" + "---:|" * len(colonnes)]
    for _, r in a.iterrows():
        lignes.append(f"| {int(r.annee)} | "
                      + " | ".join(_nb(float(r[c]), 0) for c, _ in colonnes) + " |")
    return "\n".join(lignes) + "\n"

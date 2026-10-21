"""Figure « coût des déductions liées à l'épargne » du chapitre de l'impôt sur le revenu.

BUDGÉTAIRE, RIEN D'AUTRE : les montants sont ceux des rapports sur les dépenses fiscales
annexés aux projets de loi de finances pour 2021, 2024 et 2025 (série
`depenses-fiscales-detail`, déjà au cache du précis). Aucune étude extérieure n'y entre.

UNE MARQUE PAR RAPPORT, AUCUN CHAÎNAGE. Les rapports se chevauchent et se révisent :
pour l'exercice 2022, le CEA vaut 13,71 MD dans le rapport pour 2024 et 36,43 MD dans le
rapport pour 2025 ; l'assurance-vie 15,96 et 44,30 MD. Chaque rapport a donc sa marque,
et les points d'un même rapport sont seuls reliés entre eux.

MESURES RETENUES (codes du rapport) : dépôts en comptes épargne en actions (111103909),
primes d'assurance-vie (111103901), dépôts en comptes épargne pour l'investissement
(111103912), plus-value de cession d'actions et de parts sociales (111103809). Les intérêts
des comptes spéciaux d'épargne (111103904) sont « non valorisés » dans les trois rapports ;
l'assurance-vie l'est dans le rapport pour 2021 (exercices 2017-2019).

Le domaine « Intérêts dépôts et épargne » du rapport pour 2021 (26,64 / 30,23 / 2,70 MD)
est exactement la somme CEA + CEI : ce ne sont pas des intérêts exonérés.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

SERIE = "depenses-fiscales-detail"

MESURES = [
    (111103909, {"fr": "Dépôts en comptes épargne en actions",
                 "ar": "الإيداعات في حسابات الادخار في الأسهم"}),
    (111103901, {"fr": "Primes d'assurance-vie",
                 "ar": "أقساط التأمين على الحياة"}),
    (111103912, {"fr": "Dépôts en comptes épargne pour l'investissement",
                 "ar": "الإيداعات في حسابات الادخار من أجل الاستثمار"}),
    (111103809, {"fr": "Plus-value de cession d'actions et de parts sociales",
                 "ar": "القيمة الزائدة من التفويت في الأسهم والحصص الاجتماعية"}),
]
RAPPORTS = [
    ("LF2021", "o", "#0969da", {"fr": "rapport pour 2021", "ar": "تقرير 2021"}),
    ("LF2024", "s", "#bf8700", {"fr": "rapport pour 2024", "ar": "تقرير 2024"}),
    ("LF2025", "D", "#8250df", {"fr": "rapport pour 2025", "ar": "تقرير 2025"}),
]

_L = {
    "y": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "titre": {"fr": "Coût des déductions liées à l'épargne, par rapport, exercices 2017-2023",
              "ar": "كلفة الطرح المرتبط بالادخار، حسب التقرير، السنوات 2017-2023"},
    "nv": {"fr": "non valorisé", "ar": "غير مقيّم"},
    "mesure": {"fr": "Mesure", "ar": "الإجراء"},
    "code": {"fr": "Code du rapport", "ar": "رمز التقرير"},
    "rapport": {"fr": "Rapport annexé au projet de loi de finances pour",
                "ar": "التقرير الملحق بمشروع قانون المالية لسنة"},
    "exercice": {"fr": "Exercice", "ar": "السنة"},
    "montant": {"fr": "Coût (millions de dinars courants)",
                "ar": "الكلفة (ملايين الدنانير الجارية)"},
}


def _t(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _nb(v: float, dec: int = 2) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _donnees() -> pd.DataFrame:
    d = figtools.series(SERIE)
    d = d[d["code"].isin([c for c, _ in MESURES])].copy()
    return d[["rapport", "code", "annee", "montant_MDT", "valorise"]].sort_values(
        ["code", "rapport", "annee"]).reset_index(drop=True)


def table() -> pd.DataFrame:
    d = _donnees()
    noms = {c: n.get(figtools.lang(), n["fr"]) for c, n in MESURES}
    return pd.DataFrame({
        _t("mesure"): [noms[c] for c in d["code"]],
        _t("code"): d["code"],
        _t("rapport"): d["rapport"].str.replace("LF", "").astype(int),
        _t("exercice"): d["annee"],
        _t("montant"): [round(v, 3) if ok else _t("nv")
                        for v, ok in zip(d["montant_MDT"], d["valorise"])],
    })


def fig():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.6), sharex=True)
    for ax, (code, nom) in zip(axes.flat, MESURES):
        bloc = d[(d["code"] == code) & d["valorise"] & d["montant_MDT"].notna()]
        for rapport, marque, couleur, libelle in RAPPORTS:
            r = bloc[bloc["rapport"] == rapport].sort_values("annee")
            if r.empty:
                continue
            ligne, = ax.plot(r["annee"], r["montant_MDT"], marker=marque, color=couleur,
                             lw=1.2, ms=6, label=ft(libelle.get(figtools.lang(), libelle["fr"])))
            for x, y in zip(r["annee"], r["montant_MDT"]):
                pt, = ax.plot([x], [y], marker=marque, color=couleur, ms=6, ls="")
                figtools.infobulle(pt, f"{nom['fr']} · exercice {x}, "
                                       f"{libelle['fr']} : {_nb(y, 3)} MD")
        ax.set_title(ft(nom.get(figtools.lang(), nom["fr"])), fontsize=9.5)
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_ylim(bottom=0)
        ax.set_xticks(range(2017, 2024))
        ax.tick_params(labelsize=8)
        for cote in ("top", "right"):
            ax.spines[cote].set_visible(False)
    for ax in axes[:, 0]:
        ax.set_ylabel(ft(_t("y")), fontsize=8.5)
    poignees, libelles = axes.flat[0].get_legend_handles_labels()
    fig.legend(poignees, libelles, loc="lower center", ncol=3, frameon=False, fontsize=8.5)
    fig.suptitle(ft(_t("titre")), fontsize=11)
    fig.tight_layout(rect=(0, 0.06, 1, 0.96))
    return fig

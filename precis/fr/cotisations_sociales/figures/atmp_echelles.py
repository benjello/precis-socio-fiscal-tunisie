"""Les deux échelles des taux d'accidents du travail : 1995 et 1999, classe par classe.

    from figures import atmp_echelles as ae
    ae.fig_echelles()     # pour chaque classe de 1995, son taux et ceux des secteurs de 1999
    ae.table_echelles()

D'OÙ VIENNENT LES DONNÉES. La série `atmp-echelles-1995-1999` est émise hors du build par
`scripts/generate_cotisations_tables.py` dans `precis/_seriescache/`, depuis les paramètres
des décrets n° 95-538 et 99-1010 ; ce module ne lit que `figtools.series()` (#165).

CE QUI EST TRACÉ, ET CE QUI NE L'EST PAS.
  - Les taux sont ceux de l'article 2, après transfert du point du régime général : les
    taux des employeurs affiliés à la CNSS. Ceux de l'article premier sont dans les tableaux.
  - Une ligne par classe de 1995. Les classes subdivisées (agro-alimentaire, papier,
    industries mécaniques, chimie) ont plusieurs taux : la ligne en montre la fourchette.
  - En regard, les secteurs de 1999 que la classe rejoint à l'évidence — libellé identique,
    ou éclatement en sous-secteurs qui en reprennent les termes. Cette correspondance est un
    choix de lecture, et non un texte : elle est écrite et justifiée dans le générateur
    (`CORRESPONDANCE_ATMP`). Une classe sans équivalent évident n'a pas de marque de 1999.
  - La dernière ligne regroupe les secteurs de 1999 qu'aucune classe de 1995 ne rejoint.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "atmp-echelles-1995-1999"

# Couleurs du précis (voir `retraites/figures/bareme_planchers.py`), paire validée pour les
# daltonismes ; la forme double la couleur : rond creux pour 1995, plein pour 1999.
BLEU, ORANGE, GRIS = "#08519c", "#bc4c00", "#6e7781"

figtools.register_provenance(
    SERIE,
    titre=("Taux de cotisation au régime de réparation des accidents du travail et des maladies "
           "professionnelles après transfert du point du régime général : échelle de 1995 et "
           "échelle de 1999, classe par classe"),
    titre_ar=("نسب الاشتراكات في نظام التعويض عن حوادث الشغل والأمراض المهنية بعد تحويل نقطة "
              "النظام العام: جدول 1995 وجدول 1999، صنفًا صنفًا"),
    sources=["decret95-538", "decret99-1010"],
    unite="taux des salaires",
    unite_ar="نسبة من الأجور",
    perimetre=("employeurs affiliés à la CNSS ; échelle du décret n° 95-538 (article 2) du "
               "1er janvier 1995 au 31 mars 1999, échelle du décret n° 99-1010 (article 2 "
               "nouveau du décret n° 95-538) depuis le 1er avril 1999"),
    perimetre_ar=("الأعراف المنخرطون بالصندوق الوطني للضمان الاجتماعي؛ جدول الأمر عدد 538 لسنة "
                  "1995 (الفصل 2) من غرّة جانفي 1995 إلى 31 مارس 1999، وجدول الأمر عدد 1010 "
                  "لسنة 1999 منذ غرّة أفريل 1999"),
    caveats=("La correspondance entre classes de 1995 et secteurs de 1999 n'est donnée par aucun "
             "texte : seuls les cas évidents sont retenus."),
    caveats_ar="لا يحدّد أيّ نصّ التقابل بين أصناف 1995 وقطاعات 1999: لم تُعتمد إلاّ الحالات الواضحة.",
)

_L = {
    "lg_1995": {"fr": "1995 (décret n° 95-538)", "ar": "1995 (الأمر عدد 538)"},
    "lg_1999": {"fr": "depuis 1999 (décret n° 99-1010)", "ar": "منذ 1999 (الأمر عدد 1010)"},
    "axe": {"fr": "taux de cotisation après transfert du point (% des salaires)",
            "ar": "نسبة الاشتراك بعد تحويل النقطة (% من الأجور)"},
    "sans": {"fr": "pas d'équivalent évident en 1999", "ar": "لا مقابل واضحًا في 1999"},
    "n_secteurs": {"fr": "{n} secteurs", "ar": "{n} قطاعًا"},
    "col_classe": {"fr": "Classe de 1995", "ar": "صنف 1995"},
    "col_1995": {"fr": "Taux 1995 (%)", "ar": "نسبة 1995 (%)"},
    "col_1999": {"fr": "Taux depuis 1999 (%)", "ar": "النسبة منذ 1999 (%)"},
    "col_points": {"fr": "Points de 1999", "ar": "أعداد 1999"},
    "ib_1995": {"fr": "1995 — {taux} %", "ar": "1995 — {taux} %"},
    "ib_1999": {"fr": "Depuis 1999 — {taux} %", "ar": "منذ 1999 — {taux} %"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _pct(v: float) -> str:
    return f"{100 * v:.2f}".rstrip("0").rstrip(".").replace(".", ",")


def _fourchette(valeurs) -> str:
    bas, haut = min(valeurs), max(valeurs)
    return _pct(bas) if bas == haut else f"{_pct(bas)} – {_pct(haut)}"


def _lignes():
    """[(libellé, taux de 1995, taux de 1999, points de 1999, détail)], dans l'ordre de 1995.

    `détail` : {(échelle, taux): [« numéro libellé » de chaque classe ou secteur à ce taux]},
    qui nourrit les infobulles.
    """
    df = figtools.series(SERIE)
    col = "libelle_ar" if figtools.lang() == "ar" else "libelle_fr"
    sortie = []
    # Les numéros (« 6 », « 3-1 ») sont des libellés : le CSV les rendrait en nombres.
    for colonne in ("numero_1995", "point", "point_fr", "point_ar"):
        df[colonne] = df[colonne].map(lambda v: "" if v != v else str(v).removesuffix(".0"))
    for _rang, g in df.groupby("ligne", sort=True):
        numero, libelle = g["numero_1995"].iloc[0], g[col].iloc[0]
        if numero:
            libelle = f"{numero}. {libelle}"
        t95 = g.loc[g["echelle"].astype(str) == "1995", "taux"].tolist()
        g99 = g[g["echelle"].astype(str) == "1999"]
        detail = {}
        nom = "point_ar" if figtools.lang() == "ar" else "point_fr"
        for _i, r in g.iterrows():
            detail.setdefault((str(r["echelle"]), r["taux"]), []).append(
                f"{r['point']} {r[nom]}".strip())
        sortie.append((libelle, t95, g99["taux"].tolist(), g99["point"].astype(str).tolist(), detail))
    return sortie


def table_echelles():
    import pandas as pd
    lignes = []
    for libelle, t95, t99, points, _d in _lignes():
        lignes.append({_lab("col_classe"): libelle,
                       _lab("col_1995"): _fourchette(t95) if t95 else "",
                       _lab("col_1999"): _fourchette(t99) if t99 else "",
                       _lab("col_points"): ", ".join(points)})
    return pd.DataFrame(lignes)


def _cible(ax, x: float, y: float, texte: str) -> None:
    """Cible de survol invisible, deux fois plus large que la marque : un rond de 7 points
    est difficile à viser."""
    (m,) = ax.plot([x], [y], "o", ms=15, color=GRIS, alpha=0.0, zorder=5)
    figtools.infobulle(m, texte)


def _sous_lignes(noms: list[str], classe: str) -> list[str]:
    """Les sous-classes de 1995 à ce taux ; rien quand la ligne est la classe elle-même."""
    return [n for n in noms if n and not classe.endswith(n.split(" ", 1)[-1])]


def fig_echelles():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    lignes = _lignes()
    n = len(lignes)
    fig, ax = plt.subplots(figsize=(9.5, 0.42 * n + 1.4))
    for i, (libelle, t95, t99, _points, detail) in enumerate(lignes):
        y = n - 1 - i
        if i % 2 == 0:
            ax.axhspan(y - 0.5, y + 0.5, color="#f3f4f6", zorder=0, lw=0)
        if t95:
            ax.plot([100 * min(t95), 100 * max(t95)], [y + 0.14] * 2, "-", color=ORANGE, lw=2,
                    zorder=2, solid_capstyle="round")
            for v in sorted(set(t95)):
                ax.plot([100 * v], [y + 0.14], "o", mfc="white", mec=ORANGE, mew=1.6, ms=7, zorder=3)
                _cible(ax, 100 * v, y + 0.14, "\n".join([libelle, _lab("ib_1995").format(taux=_pct(v))]
                                                 + _sous_lignes(detail[("1995", v)], libelle)))
        if t99:
            ax.plot([100 * min(t99), 100 * max(t99)], [y - 0.14] * 2, "-", color=BLEU, lw=2,
                    zorder=2, solid_capstyle="round")
            for v in sorted(set(t99)):
                ax.plot([100 * v], [y - 0.14], "o", color=BLEU, mec="white", mew=1, ms=7, zorder=3)
                _cible(ax, 100 * v, y - 0.14, "\n".join([_lab("ib_1999").format(taux=_pct(v))]
                                                 + detail[("1999", v)]))
        if t95 and not t99:
            ax.annotate(ft(_lab("sans")), (100 * max(t95), y + 0.14), xytext=(8, -3),
                        textcoords="offset points", fontsize=7.5, color=GRIS, va="center")
        if t99 and not t95:
            ax.annotate(ft(_lab("n_secteurs").format(n=len(t99))), (100 * max(t99), y - 0.14),
                        xytext=(8, -3), textcoords="offset points", fontsize=7.5, color=GRIS,
                        va="center")
    ax.set_yticks(range(n))
    ax.set_yticklabels([ft(l[0]) for l in reversed(lignes)], fontsize=8.5)
    ax.set_ylim(-0.6, n - 0.4)
    ax.set_xlim(0, None)
    ax.set_xlabel(ft(_lab("axe")), fontsize=9, color="#3d444d")
    ax.xaxis.grid(True, color="#d8dee4", lw=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=8.5, colors="#3d444d")
    for cote in ("top", "right", "left"):
        ax.spines[cote].set_visible(False)
    ax.spines["bottom"].set_color("#8c959f")
    ax.legend(handles=[
        Line2D([], [], color=ORANGE, marker="o", mfc="white", mew=1.6, lw=2, label=ft(_lab("lg_1995"))),
        Line2D([], [], color=BLEU, marker="o", mec="white", lw=2, label=ft(_lab("lg_1999"))),
    ], loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=8.5, frameon=False)
    fig.tight_layout()
    return fig

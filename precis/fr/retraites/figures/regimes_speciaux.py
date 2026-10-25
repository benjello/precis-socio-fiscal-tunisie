"""Figure des régimes spéciaux du secteur public : la retenue des députés et la contribution
de l'État, 1985-2026.

    from figures import regimes_speciaux as rs
    rs.figure_deputes(caption="…")   # fig-cnrps-deputes-retenue

D'OÙ VIENNENT LES DONNÉES. Une série longue de `precis/_seriescache/`, lue par
`figtools.series()` — une ligne par grandeur et par date d'effet, avec le texte et son lien
au Journal officiel —, émise hors du build par `scripts/generate_retraites_tables.py` :

  - `retraites-deputes-retenue` : la retenue pour pension sur l'indemnité parlementaire
    permanente et la contribution de l'État prélevée sur le budget de la chambre, taux de
    l'article 5 de la loi n° 85-16, à chaque date d'effet.

CE QUI EST TRACÉ. Deux grandeurs en escalier, sur un même axe en pour cent de l'indemnité :
une valeur vaut de sa date d'effet à la veille de la suivante ; le dernier palier, celui du
13 mars 2023, court jusqu'à la fin de `FIN`. Les deux taux s'appliquent à la même assiette ;
la série commence à la loi du 8 mars 1985, sans état antérieur versé.

LA PHRASE DE LECTURE est calculée sur la série : `reperes()` rend les nombres qu'elle cite.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "retraites-deputes-retenue"
FIN = 2026  # dernière année tracée : les taux du 13 mars 2023 valent encore
BLEU, ORANGE = "#08519c", "#bc4c00"

MOTS = {
    "fr": {
        "retenue": "Retenue sur l'indemnité du député",
        "contribution": "Contribution de l'État",
        "axe": "Taux, en % des indemnités parlementaires permanentes",
        "titre": ("Retenue pour pension des députés et contribution de l'État : taux de "
                  "l'article 5 de la loi n° 85-16 à chaque date d'effet, 1985-2026"),
        "unite": "part des indemnités parlementaires permanentes, en pour cent",
        "perimetre": ("la retenue à la charge du député et la contribution de l'État prélevée "
                      "sur le budget de la chambre des députés, à chaque date d'effet de "
                      "1985 à 2023"),
        "reserve": ("la série commence à la loi n° 85-16 ; le dernier palier, celui du 13 mars "
                    "2023, est prolongé jusqu'en {fin}"),
        "lecture": ("**Les deux taux montent par paliers, sans jamais baisser.** La retenue "
                    "passe de {r0} % en {a0} à {r1} % depuis le {d1}, la contribution de "
                    "l'État de {c0} % à {c1} %. La contribution reste supérieure à la "
                    "retenue : de {e0} points en {a0} à {e1} points depuis le {d1}."),
    },
    "ar": {
        "retenue": "الاقتطاع من منحة النائب",
        "contribution": "مساهمة الدولة",
        "axe": "النسبة، % من المنح البرلمانية القارة",
        "titre": ("الاقتطاع للجراية من منحة النواب ومساهمة الدولة: نسب الفصل 5 من القانون "
                  "عدد 85-16 عند كل تاريخ نفاذ، 1985-2026"),
        "unite": "حصة من المنح البرلمانية القارة، بالمائة",
        "perimetre": ("الاقتطاع على كاهل النائب ومساهمة الدولة المقتطعة من ميزانية مجلس "
                      "النواب، عند كل تاريخ نفاذ من 1985 إلى 2023"),
        "reserve": ("تبدأ السلسلة بالقانون عدد 85-16؛ والمرحلة الأخيرة، المؤرخة في 13 مارس "
                    "2023، ممدّدة إلى {fin}"),
        "lecture": ("**ترتفع النسبتان على مراحل دون أن تنخفضا.** ينتقل الاقتطاع من {r0} % "
                    "سنة {a0} إلى {r1} % منذ {d1}، ومساهمة الدولة من {c0} % إلى {c1} %. "
                    "وتظل المساهمة أعلى من الاقتطاع: بفارق {e0} نقاط سنة {a0} و{e1} نقطة "
                    "منذ {d1}."),
    },
}

# Dates et mots du texte de lecture, propres à chaque langue.
DATE_FIN = {"fr": "13 mars 2023", "ar": "13 مارس 2023"}


def _m(cle: str, **champs) -> str:
    return MOTS[figtools.lang()][cle].format(**champs)


figtools.register_provenance(
    SERIE, sources=["loi85-16", "loi94-71", "loi2001-123-lf2002", "loi2007-43", "lf-2026"],
    titre=MOTS["fr"]["titre"], titre_ar=MOTS["ar"]["titre"],
    unite=MOTS["fr"]["unite"], unite_ar=MOTS["ar"]["unite"],
    perimetre=MOTS["fr"]["perimetre"], perimetre_ar=MOTS["ar"]["perimetre"],
    caveats=MOTS["fr"]["reserve"].format(fin=FIN),
    caveats_ar=MOTS["ar"]["reserve"].format(fin=FIN))


def courbes() -> dict:
    """{clé de la série: (libellé, couleur)}."""
    return {"retenue": (_m("retenue"), BLEU), "contribution_etat": (_m("contribution"), ORANGE)}


def reperes() -> dict:
    """Premier et dernier taux de chaque grandeur, en pour cent, et leurs dates."""
    etats = figtools.serie_escalier(SERIE, courbes(), echelle=100)
    sortie = {}
    for cle, serie in etats.items():
        sortie[cle] = {"premier": serie[0][1], "dernier": serie[-1][1],
                       "debut": serie[0][0], "fin": serie[-1][0]}
    return sortie


def _nombre(v: float) -> str:
    return f"{v:g}".replace(".", ",")


def lecture() -> str:
    r = reperes()
    ret, con = r["retenue"], r["contribution_etat"]
    return _m("lecture", r0=_nombre(ret["premier"]), r1=_nombre(ret["dernier"]),
              c0=_nombre(con["premier"]), c1=_nombre(con["dernier"]),
              a0=ret["debut"][:4], d1=DATE_FIN[figtools.lang()],
              e0=_nombre(round(con["premier"] - ret["premier"], 4)),
              e1=_nombre(round(con["dernier"] - ret["dernier"], 4)))


# Les paliers de 2003 à 2009 se touchent : seules les marches qui ouvrent ou ferment une
# séquence sont étiquetées, les autres gardent leur valeur à l'infobulle (`format_infobulle`).
ETIQUETEES = {10, 11, 11.5, 13.2, 13.25, 15, 16.2, 16.7, 19.5, 20.5}
GRADUATIONS = ("1985-03-17", "1994-07-01", "2002-07-01", "2009-07-01", "2023-03-13")


def figure_deputes(caption: str) -> None:
    """`fig-cnrps-deputes-retenue` : les deux taux en escalier, une famille par grandeur."""
    dates = {d for serie in figtools.serie_escalier(SERIE, courbes()).values()
             for d, *_ in serie}
    figtools.figure_escalier(
        SERIE, courbes(), slug="fig_cnrps_deputes_retenue", caption=caption, fin=FIN,
        echelle=100, ylabel=_m("axe"), ylim=(0, 24),
        format_valeur=lambda v: _nombre(v) + " %" if round(v, 4) in ETIQUETEES else "",
        format_infobulle=lambda v: _nombre(v) + " %",
        etiquettes_x={d: (d[:4] if d in GRADUATIONS else "") for d in dates},
        note_lecture=lecture(), nominal=False)

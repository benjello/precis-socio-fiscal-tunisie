"""Figures des barèmes en dinars des impôts locaux — les deux taxes sur les immeubles
(chapitre « Les impôts sur les immeubles ») et la taxe sur les établissements (chapitre « Les
impôts sur l'activité ») —, chacune en deux vues : dinars courants, dinars constants.

    from figures import baremes
    baremes.figure_prix_reference()   # fig-fl-tib-prix-reference
    baremes.figure_tarif()            # fig-fl-tnb-tarif
    baremes.figure_minimum_tcl()      # fig-fl-tcl-minimum
    baremes.figure_maximum_tcl()      # fig-fl-tcl-maximum

D'OÙ VIENNENT LES DONNÉES. Quatre séries longues de `precis/_seriescache/`, lues par
`figtools.series()` — une ligne par grandeur et par date d'effet, avec le texte et son lien
au Journal officiel —, émises hors du build par `scripts/generate_finances_locales_tables.py` :

  - `fl-tib-prix-reference` : minimum et maximum du prix de référence du mètre carré
    couvert, pour chacune des quatre catégories de superficie ;
  - `fl-tnb-tarif` : tarif au mètre carré des terrains non bâtis, par zone de densité ;
  - `fl-tcl-minimum` : taxe par mètre carré de référence du minimum de la taxe sur les
    établissements, seize grandeurs (quatre catégories d'immeuble, quatre taux de la taxe
    sur les immeubles bâtis) ;
  - `fl-tcl-maximum` : maximum de la taxe sur les établissements, close par une valeur vide
    à la date de sa suppression.

L'indice des prix et l'année des dinars constants sont ceux du précis
(`scripts/dinars_constants.py`).

CE QUI EST TRACÉ.

  - DINARS COURANTS : en escalier. Une valeur vaut de sa date d'effet à la veille de la
    suivante ; le dernier palier court jusqu'à la fin de `FIN`, les barèmes de 2017 étant
    tenus pour ceux en vigueur (voir la section « L'état du droit » du chapitre).
  - DINARS CONSTANTS : un point par année, par `figtools.constants_escalier` — moyenne des
    montants en vigueur au premier jour de chacun des douze mois × indice de l'année de base
    ÷ indice de l'année. Pas de point pour une année non couverte sur douze mois (1997, les
    premiers décrets prenant effet le 13 mars) ni pour une année dont l'indice n'est pas
    publié. Entre deux décrets la courbe descend au rythme des prix ; un relèvement la
    remonte d'un coup.
  - LES TROIS DÉCRETS sont marqués d'un trait pointillé à leur date d'effet, dans les deux vues.

LA FORME. Le prix de référence a huit grandeurs, et les fourchettes de deux catégories
voisines se touchent (150 et 151 D en 1997) puis se chevauchent depuis 2017 : sur un seul
panneau, les bandes se confondent. La figure a donc quatre panneaux aux axes partagés, deux
par rang — à 1 300 px de fenêtre la figure n'a que 700 px —, un par catégorie : le maximum en trait plein, le minimum en tirets, la fourchette en aplat.
Le tarif a trois grandeurs, dans un rapport de un à dix : un panneau, à axe logarithmique,
où une même baisse en pourcentage a la même hauteur dans les trois zones.
Le minimum de la taxe sur les établissements a seize grandeurs, qui suivent toutes le même
mouvement : la figure n'en trace que quatre, les quatre catégories d'immeuble au taux de
8 % (`TAUX_TRACE`), sur un panneau à axe linéaire ; les douze autres sont au tableau du
chapitre. Le maximum n'a qu'une grandeur ; son dernier palier s'arrête à la date de sa
suppression, marquée d'une croix, et n'est pas prolongé.

LES PHRASES DE LECTURE (`lecture_prix`, `lecture_tarif`, `lecture_minimum_tcl`,
`lecture_maximum_tcl`) sont calculées sur les points que
les figures tracent ; `reperes()` rend les mêmes nombres pour qui veut les relire.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, NullFormatter

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

SERIE_PRIX = "fl-tib-prix-reference"
SERIE_TARIF = "fl-tnb-tarif"
SERIE_MINIMUM = "fl-tcl-minimum"
SERIE_MAXIMUM = "fl-tcl-maximum"
TAUX_TRACE = 8  # taux de la taxe sur les immeubles bâtis dont la figure du minimum trace les montants
FIN = 2026  # dernière année tracée en dinars courants : les barèmes de 2017 valent encore
BASE = dinars_constants.ANNEE_BASE

BLEU, ORANGE, VERT, VIOLET, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#8250df", "#57606a"
CATEGORIES = ((1, BLEU), (2, VERT), (3, ORANGE), (4, VIOLET))
ZONES = (("haute", BLEU), ("moyenne", VERT), ("basse", ORANGE))

# Libellés : ceux des tableaux du chapitre (`tbl-fl-tib-prix-reference`, `tbl-fl-tnb-tarif`) ;
# les bornes de superficie des catégories sont celles de l'article 4 du code.
MOTS = {
    "fr": {
        "cat_1": "Catégorie 1 : jusqu'à 100 m²", "cat_2": "Catégorie 2 : de 100 à 200 m²",
        "cat_3": "Catégorie 3 : de 200 à 400 m²", "cat_4": "Catégorie 4 : plus de 400 m²",
        "minimum": "minimum", "maximum": "maximum", "borne": "{categorie} — {borne}",
        "fourchette": "fourchette dans laquelle la collectivité fixe son prix",
        "decret": "date d'effet d'un décret", "texte": "date d'effet d'un texte",
        "haute": "Zone de haute densité", "moyenne": "Zone de moyenne densité",
        "basse": "Zone de basse densité",
        "prix": "Prix de référence du mètre carré couvert", "tarif": "Tarif au mètre carré",
        "courant": "dinars par m²", "courant_long": "dinars courants par m²",
        "constant": "dinars de {base} par m²", "axe": "{grandeur}\n({unite})",
        "moyenne_an": "{grandeur}, moyenne de l'année ({unite})",
        "reel": "{grandeur} ({unite})", "grandeur": "Grandeur",
        "ipc": "Indice des prix à la consommation (base 100 en 1970)",
        "x_effet": "Date d'effet", "x_annee": "Année", "d": "D",
        "titre_prix": ("Taxe sur les immeubles bâtis : minimum et maximum du prix de référence "
                       "du mètre carré couvert fixés par décret, par catégorie, à chaque date "
                       "d'effet, 1997-2017"),
        "titre_tarif": ("Taxe sur les terrains non bâtis : tarif au mètre carré fixé par "
                        "décret, par zone, à chaque date d'effet, 1997-2017"),
        "unite": "dinars courants par mètre carré",
        "perimetre_prix": ("les trois décrets identifiés, à leur date d'effet (13 mars 1997, "
                           "1er janvier 2008, 1er janvier 2017) ; quatre catégories de "
                           "superficie couverte"),
        "perimetre_tarif": ("les trois décrets identifiés, à leur date d'effet (13 mars 1997, "
                            "1er janvier 2008, 1er janvier 2017) ; trois zones du plan "
                            "d'aménagement urbain"),
        "reserve": ("aucun décret n'est identifié entre ceux de 1997 et ceux de 2007, ni "
                    "depuis ceux de 2017 : le dernier palier est prolongé jusqu'en {fin}"),
        "tcl_cat_1": "Catégorie 1 : usage administratif, commercial ou non commercial",
        "tcl_cat_2": "Catégorie 2 : structure légère, usage industriel",
        "tcl_cat_3": "Catégorie 3 : béton solide, usage industriel",
        "tcl_cat_4": "Catégorie 4 : usage industriel, plus de 5 000 m²",
        "au_taux": "{categorie} — taux de {taux} %",
        "minimum_tcl": "Taxe par mètre carré de référence, au taux de {taux} %",
        "maximum_tcl": "Maximum de la taxe", "maximum_court": "Maximum de la taxe",
        "supprime": "maximum supprimé", "suppression": "suppression du maximum",
        "courant_an": "dinars par an", "courant_an_long": "dinars courants par an",
        "constant_an": "dinars de {base} par an",
        "titre_minimum": ("Taxe sur les établissements : taxe par mètre carré de référence "
                          "du minimum fixée par décret, par catégorie d'immeuble et par taux "
                          "de la taxe sur les immeubles bâtis, à chaque date d'effet, 1997-2017"),
        "titre_maximum": ("Taxe sur les établissements : maximum de la taxe fixé par décret, "
                          "à chaque date d'effet, de 1997 à sa suppression en 2012"),
        "unite_an": "dinars courants par an",
        "perimetre_minimum": ("les trois décrets identifiés, à leur date d'effet (13 mars "
                              "1997, 1er janvier 2008, 1er janvier 2017) ; quatre catégories "
                              "d'immeuble, quatre taux de la taxe sur les immeubles bâtis"),
        "perimetre_maximum": ("les trois décrets, à leur date d'effet (13 mars 1997, 26 juin "
                              "2003, 1er janvier 2007), et la loi de finances complémentaire "
                              "pour 2012, qui supprime le maximum à partir du 1er janvier 2012"),
        "reserve_maximum": ("aucun maximum n'est fixé du 1er janvier au 12 mars 1997 ; les "
                            "plafonds antérieurs à 1997, fixés en application de la loi de "
                            "1975, ne sont pas dans la série"),
    },
    "ar": {
        "cat_1": "الصنف 1: إلى 100 م²", "cat_2": "الصنف 2: من 100 إلى 200 م²",
        "cat_3": "الصنف 3: من 200 إلى 400 م²", "cat_4": "الصنف 4: أكثر من 400 م²",
        "minimum": "الحد الأدنى", "maximum": "الحد الأقصى", "borne": "{categorie} — {borne}",
        "fourchette": "المجال الذي تضبط فيه الجماعة المحلية ثمنها",
        "decret": "تاريخ نفاذ أمر", "texte": "تاريخ نفاذ نص",
        "haute": "منطقة ذات كثافة عمرانية مرتفعة", "moyenne": "منطقة ذات كثافة عمرانية متوسطة",
        "basse": "منطقة ذات كثافة عمرانية منخفضة",
        "prix": "الثمن المرجعي للمتر المربع المبني", "tarif": "المبلغ للمتر المربع",
        "courant": "دينار للمتر المربع", "courant_long": "دينار جارٍ للمتر المربع",
        "constant": "دينار سنة {base} للمتر المربع", "axe": "{grandeur}\n({unite})",
        "moyenne_an": "{grandeur}، المعدّل السنوي ({unite})",
        "reel": "{grandeur} ({unite})", "grandeur": "المقدار",
        "ipc": "الرقم القياسي لأسعار الاستهلاك (أساس 100 سنة 1970)",
        "x_effet": "تاريخ النفاذ", "x_annee": "السنة", "d": "د",
        "titre_prix": ("المعلوم على العقارات المبنية: الحد الأدنى والحد الأقصى للثمن المرجعي "
                       "للمتر المربع المبني المضبوطان بأمر، حسب الصنف، في كلّ تاريخ نفاذ، "
                       "1997-2017"),
        "titre_tarif": ("المعلوم على الأراضي غير المبنية: المبلغ للمتر المربع المضبوط بأمر، "
                        "حسب المنطقة، في كلّ تاريخ نفاذ، 1997-2017"),
        "unite": "دينار جارٍ للمتر المربع",
        "perimetre_prix": ("الأوامر الثلاثة المحدَّدة، في تاريخ نفاذها (13 مارس 1997، "
                           "1 جانفي 2008، 1 جانفي 2017)؛ أربعة أصناف من المساحة المغطاة"),
        "perimetre_tarif": ("الأوامر الثلاثة المحدَّدة، في تاريخ نفاذها (13 مارس 1997، "
                            "1 جانفي 2008، 1 جانفي 2017)؛ ثلاث مناطق من مثال التهيئة العمرانية"),
        "reserve": ("لم يُحدَّد أيّ أمر بين أوامر 1997 وأوامر 2007، ولا بعد أوامر 2017: "
                    "تُمدَّد الدرجة الأخيرة إلى سنة {fin}"),
        "tcl_cat_1": "الصنف 1: استعمال إداري أو نشاط تجاري أو غير تجاري",
        "tcl_cat_2": "الصنف 2: متانة خفيفة، نشاط صناعي",
        "tcl_cat_3": "الصنف 3: عقار متين، نشاط صناعي",
        "tcl_cat_4": "الصنف 4: نشاط صناعي، أكثر من 5000 م²",
        "au_taux": "{categorie} — نسبة {taux} %",
        "minimum_tcl": "المعلوم بالمتر المربع المرجعي، بنسبة {taux} %",
        "maximum_tcl": "الحد الأقصى للمعلوم", "maximum_court": "الحد الأقصى للمعلوم",
        "supprime": "حُذف الحد الأقصى", "suppression": "حذف الحد الأقصى",
        "courant_an": "دينار في السنة", "courant_an_long": "دينار جارٍ في السنة",
        "constant_an": "دينار سنة {base} في السنة",
        "titre_minimum": ("المعلوم على المؤسسات: المعلوم بالمتر المربع المرجعي للحد الأدنى "
                          "المضبوط بأمر، حسب صنف العقار ونسبة المعلوم على العقارات المبنية، "
                          "في كلّ تاريخ نفاذ، 1997-2017"),
        "titre_maximum": ("المعلوم على المؤسسات: الحد الأقصى للمعلوم المضبوط بأمر، في كلّ "
                          "تاريخ نفاذ، من 1997 إلى حذفه سنة 2012"),
        "unite_an": "دينار جارٍ في السنة",
        "perimetre_minimum": ("الأوامر الثلاثة المحدَّدة، في تاريخ نفاذها (13 مارس 1997، "
                              "1 جانفي 2008، 1 جانفي 2017)؛ أربعة أصناف من العقارات وأربع "
                              "نسب للمعلوم على العقارات المبنية"),
        "perimetre_maximum": ("الأوامر الثلاثة، في تاريخ نفاذها (13 مارس 1997، 26 جوان 2003، "
                              "1 جانفي 2007)، وقانون المالية التكميلي لسنة 2012 الذي يحذف "
                              "الحد الأقصى ابتداء من 1 جانفي 2012"),
        "reserve_maximum": ("لم يُضبط أيّ حد أقصى من 1 جانفي إلى 12 مارس 1997؛ والحدود القصوى "
                            "السابقة لسنة 1997، المضبوطة تطبيقًا لقانون 1975، ليست في السلسلة"),
    },
}


def _m(cle: str, **champs) -> str:
    return MOTS[figtools.lang()][cle].format(**champs)


for _serie, _sources, _genre in (
        (SERIE_PRIX, ["decret97-431", "decret2007-1185", "decret2017-397"], "prix"),
        (SERIE_TARIF, ["decret97-432", "decret2007-1186", "decret2017-396"], "tarif")):
    figtools.register_provenance(
        _serie, sources=_sources,
        titre=MOTS["fr"][f"titre_{_genre}"], titre_ar=MOTS["ar"][f"titre_{_genre}"],
        unite=MOTS["fr"]["unite"], unite_ar=MOTS["ar"]["unite"],
        perimetre=MOTS["fr"][f"perimetre_{_genre}"],
        perimetre_ar=MOTS["ar"][f"perimetre_{_genre}"],
        caveats=MOTS["fr"]["reserve"].format(fin=FIN),
        caveats_ar=MOTS["ar"]["reserve"].format(fin=FIN))


for _serie, _sources, _genre, _unite, _reserve in (
        (SERIE_MINIMUM, ["decret97-433", "decret2007-1187", "decret2017-395"], "minimum",
         "unite", "reserve"),
        (SERIE_MAXIMUM, ["decret97-435", "decret2003-1345", "decret2006-3360", "lfc-2012"],
         "maximum", "unite_an", "reserve_maximum")):
    figtools.register_provenance(
        _serie, sources=_sources,
        titre=MOTS["fr"][f"titre_{_genre}"], titre_ar=MOTS["ar"][f"titre_{_genre}"],
        unite=MOTS["fr"][_unite], unite_ar=MOTS["ar"][_unite],
        perimetre=MOTS["fr"][f"perimetre_{_genre}"],
        perimetre_ar=MOTS["ar"][f"perimetre_{_genre}"],
        caveats=MOTS["fr"][_reserve].format(fin=FIN),
        caveats_ar=MOTS["ar"][_reserve].format(fin=FIN))


# --- les grandeurs ---------------------------------------------------------------------

def courbes_prix() -> dict:
    """{clé de la série: (libellé, couleur)}, minimum puis maximum de chaque catégorie."""
    return {f"categorie_{n}_{borne}": (_m("borne", categorie=_m(f"cat_{n}"), borne=_m(borne)),
                                       couleur)
            for n, couleur in CATEGORIES for borne in ("minimum", "maximum")}


def courbes_tarif() -> dict:
    return {zone: (_m(zone), couleur) for zone, couleur in ZONES}


def courbes_minimum() -> dict:
    """Les quatre catégories d'immeuble, au taux `TAUX_TRACE` de la taxe sur les immeubles bâtis."""
    return {f"categorie_{n}_taux_{TAUX_TRACE}": (_m(f"tcl_cat_{n}"), couleur)
            for n, couleur in CATEGORIES}


def courbes_maximum() -> dict:
    return {"maximum": (_m("maximum_court"), BLEU)}


def _nombre(valeur: float, decimales: int) -> str:
    """« 1 056 », « 0,385 » : espace insécable des milliers, virgule décimale."""
    return f"{valeur:,.{decimales}f}".replace(",", " ").replace(".", ",")


def _constants(serie: str, courbes: dict) -> dict:
    """{clé: {année: montant en dinars de l'année de base}}, sur les points tracés."""
    lignes, _base = figtools.constants_escalier(serie, courbes, base=BASE,
                                                ipc=dinars_constants.ipc())
    sortie: dict = {cle: {} for cle in courbes}
    for cle, annee, _moyenne, _indice, reel in lignes:
        sortie[cle][annee] = reel
    return sortie


def _dates(etats: dict) -> list[str]:
    return sorted({date for serie in etats.values() for date, *_ in serie})


# --- le tracé ---------------------------------------------------------------------------

def _marques(ax, dates: list[str]) -> None:
    for date in dates:
        ax.axvline(figtools.abscisse_date(date), color=GRIS, lw=0.8, ls=(0, (1, 2.5)), zorder=1)


def _poignee_decret(cle: str = "decret") -> Line2D:
    return Line2D([], [], color=GRIS, lw=0.8, ls=(0, (1, 2.5)),
                  label=figtools.fig_text(_m(cle)))


def _escalier(ax, lignes, couleur, libelle, fmt, *, tirets=False, dessous=False,
              etiquettes=True) -> None:
    """Une grandeur en escalier : paliers, contremarches, point et valeur à chaque date."""
    style = dict(color=couleur, lw=1.4 if tirets else 2.2, ls=(0, (4, 2)) if tirets else "-",
                 solid_capstyle="butt", dash_capstyle="butt", zorder=3)
    for i, (date, v, etat, texte, _lien) in enumerate(lignes):
        x = figtools.abscisse_date(date)
        if v is None:  # suppression : le palier précédent s'arrête ici, une croix le dit
            if i:
                croix, = ax.plot([x], [lignes[i - 1][1]], "x", color=couleur, ms=8, mew=2,
                                 zorder=4)
                figtools.infobulle(croix, f"{date} · {libelle} : {_m('supprime')} · {texte}")
                ax.annotate(figtools.fig_text(_m("supprime")), xy=(x, lignes[i - 1][1]),
                            xytext=(-6, -8), textcoords="offset points", ha="right",
                            va="top", fontsize=8.5, color=couleur, zorder=5)
            continue
        x_suivant = figtools.abscisse_date(lignes[i + 1][0]) if i + 1 < len(lignes) else FIN + 1
        ax.plot([x, x_suivant], [v, v], **style)
        if i + 1 < len(lignes) and lignes[i + 1][1] not in (None, v):
            ax.plot([x_suivant, x_suivant], [v, lignes[i + 1][1]], color=couleur, lw=1, zorder=3)
        point, = ax.plot([x], [v], "o", color=couleur, ms=4, zorder=4,
                         mfc="white" if etat == "reprise" else couleur)
        figtools.infobulle(point, f"{date} · {libelle} : {fmt(v)} · {texte}")
        if etiquettes and etat != "reprise":
            ax.annotate(fmt(v), xy=(x, v), xytext=(3, -4 if dessous else 4),
                        textcoords="offset points", ha="left",
                        va="top" if dessous else "bottom", fontsize=8.5,
                        fontweight="normal" if tirets else "bold", color=couleur, zorder=5)


def _annuelle(ax, points: dict, couleur, libelle, fmt, *, tirets=False, dessous=False,
              reperes=()) -> None:
    """Une grandeur en dinars constants : un point par année, les années repères chiffrées."""
    annees = sorted(points)
    ax.plot(annees, [points[a] for a in annees], color=couleur, lw=1.3 if tirets else 2,
            ls=(0, (4, 2)) if tirets else "-", zorder=3)
    for a in annees:
        point, = ax.plot([a], [points[a]], "o", color=couleur, ms=2.6, zorder=4)
        figtools.infobulle(point, f"{a} · {libelle} : {fmt(points[a])}")
    for a in reperes:
        if a in points:
            # La courbe descend : la place libre est en haut à droite, et en bas à gauche.
            ax.annotate(fmt(points[a]), xy=(a, points[a]),
                        xytext=(-3, -3) if dessous else (3, 3),
                        textcoords="offset points", ha="right" if dessous else "left",
                        va="top" if dessous else "bottom", fontsize=8.5,
                        fontweight="normal" if tirets else "bold", color=couleur, zorder=5)


def _axe_x(ax, dates: list[str], fin: int, debut: float, bout: float, xlabel: str) -> None:
    positions = [figtools.abscisse_date(d) for d in dates] + [fin]
    ax.set_xticks(positions)
    ax.set_xticklabels([d[:4] for d in dates] + [str(fin)], fontsize=8.5)
    ax.set_xlim(debut, bout)
    ax.set_xlabel(figtools.fig_text(xlabel), fontsize=9)


def _vues_prix() -> list:
    ft = figtools.fig_text
    courbes = courbes_prix()
    etats = figtools.serie_escalier(SERIE_PRIX, courbes)
    reels = _constants(SERIE_PRIX, courbes)
    dates = _dates(etats)
    fmt = lambda v: _nombre(v, 0)  # noqa: E731
    reperes = (min(min(r) for r in reels.values()), *(int(d[:4]) for d in dates[1:]), BASE)
    vues = []
    for constante in (False, True):
        fig, grille = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(9.5, 7.4))
        axes = list(grille.flat)
        for ax, (n, couleur) in zip(axes, CATEGORIES):
            bas, haut = f"categorie_{n}_minimum", f"categorie_{n}_maximum"
            if constante:
                annees = sorted(reels[haut])
                ax.fill_between(annees, [reels[bas][a] for a in annees],
                                [reels[haut][a] for a in annees], color=couleur, alpha=0.16,
                                lw=0, zorder=2)
                _annuelle(ax, reels[bas], couleur, courbes[bas][0], fmt, tirets=True,
                          dessous=True, reperes=reperes)
                _annuelle(ax, reels[haut], couleur, courbes[haut][0], fmt, reperes=reperes)
                _axe_x(ax, dates, BASE, 1995.2, BASE + 2.6, _m("x_annee"))
            else:
                xs = [figtools.abscisse_date(d) for d, *_ in etats[haut]] + [FIN + 1]
                ax.fill_between(xs, [v for _d, v, *_ in etats[bas]] + [etats[bas][-1][1]],
                                [v for _d, v, *_ in etats[haut]] + [etats[haut][-1][1]],
                                step="post", color=couleur, alpha=0.16, lw=0, zorder=2)
                _escalier(ax, etats[bas], couleur, courbes[bas][0], fmt, tirets=True,
                          dessous=True)
                _escalier(ax, etats[haut], couleur, courbes[haut][0], fmt)
                _axe_x(ax, dates, FIN, 1996.2, FIN + 1.6, _m("x_effet"))
            _marques(ax, dates)
            ax.set_title(ft(_m(f"cat_{n}")), fontsize=10, color=couleur, fontweight="bold")
            if ax in axes[:2]:
                ax.set_xlabel("")
            ax.grid(True, axis="y", alpha=0.3)
            ax.tick_params(axis="y", labelsize=8)
        sommet = max(max(reels[c].values()) if constante else max(v for _d, v, *_ in etats[c])
                     for c in courbes)
        axes[0].set_ylim(0, 1.09 * sommet)  # axe partagé : les quatre panneaux se comparent
        axes[0].yaxis.set_major_formatter(FuncFormatter(lambda y, _p: _nombre(y, 0)))
        unite = _m("constant", base=BASE) if constante else _m("courant")
        fig.supylabel(ft(_m("axe", grandeur=_m("prix"), unite=unite)), fontsize=10)
        poignees = [
            Line2D([], [], color=GRIS, lw=2.2, label=ft(_m("maximum"))),
            Line2D([], [], color=GRIS, lw=1.4, ls=(0, (4, 2)), label=ft(_m("minimum"))),
            Patch(color=GRIS, alpha=0.16, lw=0, label=ft(_m("fourchette"))),
            _poignee_decret()]
        fig.legend(handles=poignees, loc="lower center", ncol=2, fontsize=8.5, frameon=False)
        fig.tight_layout(rect=(0, 0.07, 1, 1))
        vues.append(fig)
    return vues


def _vues_tarif() -> list:
    ft = figtools.fig_text
    courbes = courbes_tarif()
    etats = figtools.serie_escalier(SERIE_TARIF, courbes)
    reels = _constants(SERIE_TARIF, courbes)
    dates = _dates(etats)
    fmt = lambda v: _nombre(v, 3)  # noqa: E731
    reperes = (min(min(r) for r in reels.values()), *(int(d[:4]) for d in dates[1:]), BASE)
    vues = []
    for constante in (False, True):
        fig, ax = plt.subplots(figsize=(9.5, 5.4))
        for zone, couleur in ZONES:
            if constante:
                _annuelle(ax, reels[zone], couleur, courbes[zone][0], fmt, reperes=reperes)
            else:
                _escalier(ax, etats[zone], couleur, courbes[zone][0], fmt)
        _marques(ax, dates)
        ax.set_yscale("log")
        ax.set_ylim(0.025, 1.5 if constante else 0.55)
        ax.set_yticks([0.05, 0.1, 0.2, 0.5, 1] if constante else [0.05, 0.1, 0.2, 0.5])
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: f"{y:g}".replace(".", ",")))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.grid(True, axis="y", alpha=0.3)
        if constante:
            _axe_x(ax, dates, BASE, 1996.2, BASE + 2.2, _m("x_annee"))
        else:
            _axe_x(ax, dates, FIN, 1996.2, FIN + 1.6, _m("x_effet"))
        unite = _m("constant", base=BASE) if constante else _m("courant")
        ax.set_ylabel(ft(_m("axe", grandeur=_m("tarif"), unite=unite)))
        poignees = [Line2D([], [], color=couleur, lw=2.2, marker="o", ms=4,
                           label=ft(courbes[zone][0])) for zone, couleur in ZONES]
        ax.legend(handles=poignees + [_poignee_decret()], loc="upper center",
                  bbox_to_anchor=(0.5, -0.13), ncol=4, fontsize=8, frameon=False)
        fig.tight_layout()
        vues.append(fig)
    return vues


def _vues_minimum() -> list:
    ft = figtools.fig_text
    courbes = courbes_minimum()
    etats = figtools.serie_escalier(SERIE_MINIMUM, courbes)
    reels = _constants(SERIE_MINIMUM, courbes)
    dates = _dates(etats)
    fmt = lambda v: _nombre(v, 3)  # noqa: E731
    reperes = (min(min(r) for r in reels.values()), *(int(d[:4]) for d in dates[1:]), BASE)
    vues = []
    for constante in (False, True):
        fig, ax = plt.subplots(figsize=(9.5, 5.8))
        for cle, (libelle, couleur) in courbes.items():
            if constante:
                _annuelle(ax, reels[cle], couleur, libelle, fmt, reperes=reperes)
            else:
                _escalier(ax, etats[cle], couleur, libelle, fmt)
        _marques(ax, dates)
        sommet = max(max(reels[c].values()) if constante else max(v for _d, v, *_ in etats[c])
                     for c in courbes)
        ax.set_ylim(0, 1.12 * sommet)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: _nombre(y, 1)))
        ax.grid(True, axis="y", alpha=0.3)
        if constante:
            _axe_x(ax, dates, BASE, 1996.2, BASE + 2.2, _m("x_annee"))
        else:
            _axe_x(ax, dates, FIN, 1996.2, FIN + 1.6, _m("x_effet"))
        unite = _m("constant", base=BASE) if constante else _m("courant")
        ax.set_ylabel(ft(_m("axe", grandeur=_m("minimum_tcl", taux=TAUX_TRACE), unite=unite)))
        poignees = [Line2D([], [], color=couleur, lw=2.2, marker="o", ms=4, label=ft(libelle))
                    for libelle, couleur in courbes.values()]
        ax.legend(handles=poignees + [_poignee_decret()], loc="upper center",
                  bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8, frameon=False)
        fig.tight_layout()
        vues.append(fig)
    return vues


def _annees_maximum(etats: list, points: dict) -> list[tuple[int, int]]:
    """Pour chaque relèvement, (dernière année pleine avant, première année pleine depuis)."""
    return [(int(d[:4]) - 1, int(d[:4]) if d[5:] == "01-01" else int(d[:4]) + 1)
            for d, v, etat, *_ in etats if etat == "changement"]


def _vues_maximum() -> list:
    ft = figtools.fig_text
    courbes = courbes_maximum()
    etats = figtools.serie_escalier(SERIE_MAXIMUM, courbes)["maximum"]
    reels = _constants(SERIE_MAXIMUM, courbes)["maximum"]
    dates = [d for d, *_ in etats]
    libelle, couleur = courbes["maximum"]
    fmt = lambda v: _nombre(v, 0)  # noqa: E731
    reperes = (min(reels), max(reels), *(a for paire in _annees_maximum(etats, reels)
                                         for a in paire))
    vues = []
    for constante in (False, True):
        fig, ax = plt.subplots(figsize=(9.5, 5.0))
        if constante:
            _annuelle(ax, reels, couleur, libelle, fmt, reperes=reperes)
        else:
            _escalier(ax, etats, couleur, libelle, fmt)
        _marques(ax, dates)
        sommet = max(reels.values()) if constante else max(v for _d, v, *_ in etats if v)
        ax.set_ylim(0, 1.15 * sommet)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: _nombre(y, 0)))
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_xticks([figtools.abscisse_date(d) for d in dates])
        ax.set_xticklabels([d[:4] for d in dates], fontsize=8.5)
        ax.set_xlim(1996.2, int(dates[-1][:4]) + 1.6)
        ax.set_xlabel(ft(_m("x_annee" if constante else "x_effet")), fontsize=9)
        unite = _m("constant_an", base=BASE) if constante else _m("courant_an")
        ax.set_ylabel(ft(_m("axe", grandeur=_m("maximum_tcl"), unite=unite)))
        poignees = [Line2D([], [], color=couleur, lw=2.2, marker="o", ms=4, label=ft(libelle)),
                    _poignee_decret("texte")]
        if not constante:
            poignees.insert(1, Line2D([], [], color=couleur, lw=0, marker="x", ms=7, mew=2,
                                      label=ft(_m("suppression"))))
        ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=3,
                  fontsize=8, frameon=False)
        fig.tight_layout()
        vues.append(fig)
    return vues


# --- les nombres du texte ---------------------------------------------------------------

def reperes() -> dict:
    """Les nombres que le chapitre cite, calculés sur les points des figures.

    `prix` et `tarif` : {clé: {année: dinars de l'année de base}} ; `annees` : la première
    année couverte sur douze mois, l'année de chaque relèvement, la veille de chacun, l'année
    de base ; `prix_hausse` : hausse de l'indice des prix, en %, entre les années moyennes
    de deux dates d'effet consécutives, puis de la dernière à l'année de base.
    """
    indice = dinars_constants.ipc()
    prix = _constants(SERIE_PRIX, courbes_prix())
    tarif = _constants(SERIE_TARIF, courbes_tarif())
    effets = [int(d[:4]) for d in _dates(figtools.serie_escalier(SERIE_TARIF, courbes_tarif()))]
    bornes = effets + [BASE]
    return {
        "prix": prix, "tarif": tarif,
        "annees": sorted({min(prix["categorie_4_maximum"]), BASE,
                          *(a for e in effets[1:] for a in (e - 1, e))}),
        "prix_hausse": {(a, b): 100 * (indice[b] / indice[a] - 1)
                        for a, b in zip(bornes, bornes[1:])},
    }


LECTURES = {
    "fr": {
        "commune": (
            "Chaque trait pointillé marque la date d'effet d'un décret : 13 mars 1997, "
            "1^er^ janvier 2008, 1^er^ janvier 2017. En dinars courants, une valeur vaut de sa "
            "date d'effet à la veille de la suivante, et le palier de 2017 est prolongé "
            "jusqu'en {fin}, aucun décret postérieur n'étant identifié. En dinars de {base}, "
            "chaque point est la moyenne des montants en vigueur dans l'année, multipliée par "
            "l'indice des prix à la consommation de {base} et divisée par celui de l'année ; "
            "la série commence en {a0}, première année couverte sur douze mois. Entre deux "
            "décrets, la courbe descend au rythme des prix ; un relèvement la remonte d'un coup."),
        "prix": (
            " Chaque panneau est une catégorie : le maximum en trait plein, le minimum en "
            "tirets, et entre les deux la fourchette dans laquelle la collectivité fixe son "
            "prix ; un point creux marque un décret qui reprend la valeur sans la changer. Le "
            "maximum de la quatrième catégorie vaut, en dinars de {base} par mètre carré, "
            "{p0} en {a0}, {p1v} en {a1v} puis {p1} en {a1}, {p2v} en {a2v} puis {p2} en "
            "{a2}, et {pfin} en {base}."),
        "tarif": (
            " L'axe vertical est logarithmique : une même baisse en pourcentage y a la même "
            "hauteur dans les trois zones. Le tarif de la zone de haute densité vaut, en "
            "dinars de {base} par mètre carré, {p0} en {a0}, {p1v} en {a1v} puis {p1} en "
            "{a1}, {p2v} en {a2v} puis {p2} en {a2}, et {pfin} en {base}."),
        "minimum": (
            " Les quatre courbes sont les quatre catégories d'immeuble, au taux de {taux} % "
            "de la taxe sur les immeubles bâtis ; les montants des trois autres taux sont au "
            "tableau. Le montant de la première catégorie vaut, en dinars de {base} par mètre "
            "carré, {p0} en {a0}, {p1v} en {a1v} puis {p1} en {a1}, {p2v} en {a2v} puis {p2} "
            "en {a2}, et {pfin} en {base}."),
        "maximum": (
            "Chaque trait pointillé marque une date d'effet : 13 mars 1997, 26 juin 2003 et "
            "1^er^ janvier 2007 pour les trois décrets, 1^er^ janvier 2012 pour la loi qui "
            "supprime le maximum. En dinars courants, une valeur vaut de sa date d'effet à la "
            "veille de la suivante ; la croix marque la fin du dernier palier, à la "
            "suppression. En dinars de {base}, chaque point est la moyenne des montants en "
            "vigueur au premier jour de chacun des douze mois de l'année, multipliée par "
            "l'indice des prix à la consommation de {base} et divisée par celui de l'année ; "
            "la série va de {a0}, première année couverte sur douze mois, à {afin}, dernière "
            "année où le maximum s'applique. Le maximum vaut, en dinars de {base} par an, "
            "{p0} en {a0}, {suite}, et {pfin} en {afin}."),
        "maximum_etape": "{pv} en {av} puis {p} en {a}",
    },
    "ar": {
        "commune": (
            "كلّ خطّ منقّط يبيّن تاريخ نفاذ أمر: 13 مارس 1997، 1 جانفي 2008، 1 جانفي 2017. "
            "بالدينار الجاري، تسري القيمة من تاريخ نفاذها إلى اليوم السابق لتاريخ نفاذ القيمة "
            "الموالية، وتُمدَّد درجة 2017 إلى سنة {fin} لعدم تحديد أيّ أمر لاحق. بدينار سنة "
            "{base}، كلّ نقطة هي معدّل المبالغ الجاري بها العمل خلال السنة، مضروبًا في الرقم "
            "القياسي لأسعار الاستهلاك لسنة {base} ومقسومًا على رقم السنة؛ تبدأ السلسلة سنة "
            "{a0}، أوّل سنة مغطّاة على اثني عشر شهرًا. بين أمرين ينخفض المنحنى بوتيرة الأسعار، "
            "ثمّ يرفعه كلّ ترفيع دفعة واحدة."),
        "prix": (
            " كلّ لوحة صنف: الحد الأقصى بخطّ متّصل، والحد الأدنى بخطّ متقطّع، وبينهما المجال "
            "الذي تضبط فيه الجماعة المحلية ثمنها؛ النقطة المجوّفة تبيّن أمرًا يُبقي القيمة دون "
            "تغيير. يبلغ الحد الأقصى للصنف الرابع، بدينار سنة {base} للمتر المربع، {p0} سنة "
            "{a0}، و{p1v} سنة {a1v} ثمّ {p1} سنة {a1}، و{p2v} سنة {a2v} ثمّ {p2} سنة {a2}، "
            "و{pfin} سنة {base}."),
        "tarif": (
            " المحور العمودي لوغاريتمي: الانخفاض بالنسبة المئوية نفسها له الارتفاع نفسه في "
            "المناطق الثلاث. يبلغ مبلغ المنطقة ذات الكثافة العمرانية المرتفعة، بدينار سنة "
            "{base} للمتر المربع، {p0} سنة {a0}، و{p1v} سنة {a1v} ثمّ {p1} سنة {a1}، و{p2v} "
            "سنة {a2v} ثمّ {p2} سنة {a2}، و{pfin} سنة {base}."),
        "minimum": (
            " المنحنيات الأربعة هي أصناف العقارات الأربعة، بنسبة {taux} % للمعلوم على "
            "العقارات المبنية؛ ومبالغ النسب الثلاث الأخرى في الجدول. يبلغ مبلغ الصنف الأوّل، "
            "بدينار سنة {base} للمتر المربع، {p0} سنة {a0}، و{p1v} سنة {a1v} ثمّ {p1} سنة "
            "{a1}، و{p2v} سنة {a2v} ثمّ {p2} سنة {a2}، و{pfin} سنة {base}."),
        "maximum": (
            "كلّ خطّ منقّط يبيّن تاريخ نفاذ: 13 مارس 1997 و26 جوان 2003 و1 جانفي 2007 "
            "للأوامر الثلاثة، و1 جانفي 2012 للقانون الذي يحذف الحد الأقصى. بالدينار الجاري، "
            "تسري القيمة من تاريخ نفاذها إلى اليوم السابق لتاريخ نفاذ القيمة الموالية؛ "
            "والعلامة × تبيّن نهاية الدرجة الأخيرة عند الحذف. بدينار سنة {base}، كلّ نقطة هي "
            "معدّل المبالغ الجاري بها العمل في اليوم الأوّل من كلّ شهر من أشهر السنة الاثني "
            "عشر، مضروبًا في الرقم القياسي لأسعار الاستهلاك لسنة {base} ومقسومًا على رقم "
            "السنة؛ تمتدّ السلسلة من سنة {a0}، أوّل سنة مغطّاة على اثني عشر شهرًا، إلى سنة "
            "{afin}، آخر سنة يُطبَّق فيها الحد الأقصى. يبلغ الحد الأقصى، بدينار سنة {base} في "
            "السنة، {p0} سنة {a0}، و{suite}، و{pfin} سنة {afin}."),
        "maximum_etape": "{pv} سنة {av} ثمّ {p} سنة {a}",
    },
}


def _lecture(genre: str, points: dict, decimales: int, **autres) -> str:
    a0, a1v, a1, a2v, a2, _base = reperes()["annees"]
    textes = LECTURES[figtools.lang()]
    n = lambda a: _nombre(points[a], decimales)  # noqa: E731
    champs = dict(base=BASE, fin=FIN, a0=a0, a1v=a1v, a1=a1, a2v=a2v, a2=a2, p0=n(a0),
                  p1v=n(a1v), p1=n(a1), p2v=n(a2v), p2=n(a2), pfin=n(BASE))
    return (textes["commune"] + textes[genre]).format(**champs, **autres)


def lecture_prix() -> str:
    return _lecture("prix", reperes()["prix"]["categorie_4_maximum"], 0)


def lecture_tarif() -> str:
    return _lecture("tarif", reperes()["tarif"]["haute"], 3)


def reperes_tcl() -> dict:
    """Les nombres du chapitre des impôts sur l'activité, sur les points des deux figures.

    `minimum` : {clé: {année: dinars de l'année de base par mètre carré}} ; `maximum` :
    {année: dinars de l'année de base par an} ; `etapes` : pour chaque relèvement du
    maximum, (dernière année pleine avant, première année pleine depuis).
    """
    etats = figtools.serie_escalier(SERIE_MAXIMUM, courbes_maximum())["maximum"]
    maximum = _constants(SERIE_MAXIMUM, courbes_maximum())["maximum"]
    return {"minimum": _constants(SERIE_MINIMUM, courbes_minimum()), "maximum": maximum,
            "etapes": _annees_maximum(etats, maximum)}


def lecture_minimum_tcl() -> str:
    points = reperes_tcl()["minimum"][f"categorie_1_taux_{TAUX_TRACE}"]
    return _lecture("minimum", points, 3, taux=TAUX_TRACE)


def lecture_maximum_tcl() -> str:
    r = reperes_tcl()
    points, textes = r["maximum"], LECTURES[figtools.lang()]
    n = lambda a: _nombre(points[a], 0)  # noqa: E731
    separateur = "، و" if figtools.lang() == "ar" else ", "
    suite = separateur.join(textes["maximum_etape"].format(pv=n(av), av=av, p=n(a), a=a)
                            for av, a in r["etapes"])
    a0, afin = min(points), max(points)
    return textes["maximum"].format(base=BASE, a0=a0, afin=afin, p0=n(a0), pfin=n(afin),
                                    suite=suite)


# --- les deux figures -------------------------------------------------------------------

def _figure(serie: str, courbes: dict, vues: list, genre: str, slug: str, caption: str,
            lecture: str, decimales: int, unites: tuple[str, str] = ("courant_long", "constant"),
            **champs) -> None:
    """`unites` : clés de `MOTS` des unités courante et constante ; `champs` complète le
    libellé de la grandeur (le taux tracé, pour le minimum de la taxe sur les établissements)."""
    grandeur = _m(genre, **champs)
    libelles = {
        "parametre": _m("grandeur"),
        "moyenne": _m("moyenne_an", grandeur=grandeur, unite=_m(unites[0])),
        "ipc": _m("ipc"),
        "reel": _m("reel", grandeur=grandeur, unite=_m(unites[1], base=BASE)),
    }
    table = figtools.table_escalier_constants(
        serie, courbes, base=BASE, ipc=dinars_constants.ipc(), libelles=libelles,
        decimales=decimales)
    figtools.figure_tabs(
        [(figtools.t("esc_courants"), vues[0]),
         (figtools.t("esc_constants").format(base=BASE), vues[1])],
        table, serie, *dinars_constants.SERIES_IPC, slug=slug, caption=caption,
        note_lecture=lecture, nominal=False)


def figure_prix_reference(caption: str) -> None:
    """`fig-fl-tib-prix-reference` : à appeler dans un chunk `#| output: asis` étiqueté."""
    _figure(SERIE_PRIX, courbes_prix(), _vues_prix(), "prix", "fig_fl_tib_prix_reference",
            caption, lecture_prix(), 1)


def figure_tarif(caption: str) -> None:
    """`fig-fl-tnb-tarif` : à appeler dans un chunk `#| output: asis` étiqueté."""
    _figure(SERIE_TARIF, courbes_tarif(), _vues_tarif(), "tarif", "fig_fl_tnb_tarif",
            caption, lecture_tarif(), 3)


def figure_minimum_tcl(caption: str) -> None:
    """`fig-fl-tcl-minimum` : à appeler dans un chunk `#| output: asis` étiqueté."""
    _figure(SERIE_MINIMUM, courbes_minimum(), _vues_minimum(), "minimum_tcl",
            "fig_fl_tcl_minimum", caption, lecture_minimum_tcl(), 3, taux=TAUX_TRACE)


def figure_maximum_tcl(caption: str) -> None:
    """`fig-fl-tcl-maximum` : à appeler dans un chunk `#| output: asis` étiqueté."""
    _figure(SERIE_MAXIMUM, courbes_maximum(), _vues_maximum(), "maximum_tcl",
            "fig_fl_tcl_maximum", caption, lecture_maximum_tcl(), 1,
            unites=("courant_an_long", "constant_an"))

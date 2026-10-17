"""Figures du chapitre « L'électricité et le gaz » (volume « La compensation »), longue période.

    from figures import electricite as el
    el.figure("prix_achat_gaz", caption=…, note_lecture=…)
    el.figure("cout_prix_kwh", caption=…, note_lecture=…)
    el.figure("subvention", caption=…, note_lecture=…)
    el.figure("gaz_sources", caption=…, note_lecture=…)

D'OÙ VIENNENT LES DONNÉES. Quatre séries de `tunisia-data`, lues par `figtools.series()` — donc
depuis le snapshot `precis/_seriescache/` quand l'entrepôt est absent :

  - `steg-prix-achat-gaz` : prix d'achat de la tonne équivalent pétrole de gaz, en dinars
    courants — prix de cession administré, prix moyen d'achat du rapport de contrôle de 2014,
    prix moyen d'achat des états financiers de la STEG ; la famille de l'Observatoire (prix
    d'importation du gaz algérien) est dans la série et n'est pas tracée ici ;
  - `steg-cout-prix-kwh` : coût de revient et prix de vente moyen hors taxes du kilowattheure,
    en millimes courants, par famille de source ;
  - `steg-subvention-exploitation` : subvention d'exploitation de la STEG, 2006-2016, soutien
    direct et indirect du rapport de contrôle de 2014 ;
  - `steg-prelevements-gaz` : gaz prélevé par la STEG, par source, 2001-2024, en ktep.

RÈGLES (les mêmes que `compensation.py` et `transport.py`).

  - **Aucune famille n'est raccordée à une autre** : une famille a sa couleur, sa marque et son
    trait ; une année manquante interrompt le trait ; une année sans valeur reste vide.
  - **Les ruptures viennent des données** (colonnes `rupture` et `rupture_annee`) : un trait
    vertical et un repère triangulaire dont l'infobulle porte le texte complet.
  - **Une valeur par ligne retenue** : la ligne `retenu = non` (coût de 2016 calculé) n'est pas
    tracée ; elle reste dans l'onglet « Données ».
  - **Dinars et millimes courants, aucun PIB.**
  - **La ligne « Source » ne cite que les clés des lignes tracées.**

Les libellés sont en français ; les libellés arabes restent à verser.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

PRIX = "steg-prix-achat-gaz"
KWH = "steg-cout-prix-kwh"
SUBV = "steg-subvention-exploitation"
GAZ = "steg-prelevements-gaz"

BLEU, BLEU_CLAIR, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN, NOIR, ROSE, TEAL = (
    "#0969da", "#80b3f0", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#8c959f", "#9a6700",
    "#24292f", "#bf3989", "#1b7c83")
GRIS_FONCE = "#57606a"


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _v(v: float) -> str:
    """Valeur sans décimale inutile : 0, 339, 804,4."""
    return _nb(v, 0 if float(v) == round(float(v)) else 1)


def _legende(ax, poignees, ncol=2, y=-0.14):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


def _cadre(ax, ylabel: str, xlabel: str | None = "Année"):
    ax.set_ylabel(ylabel)
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)


def _cles(*dfs) -> list[str]:
    """Clés de citation des lignes tracées, dans l'ordre où elles apparaissent."""
    vues: dict[str, None] = {}
    for d in dfs:
        for x in d["cle"]:
            for c in str(x).split(" ; "):
                if c:
                    vues[c] = None
    return list(vues)


def _repere(ax, annee, texte):
    """Trait vertical de rupture et petit triangle en haut du trait, porteur de l'infobulle."""
    figtools.marque_rupture(ax, annee)
    p, = ax.plot([annee - 0.5], [1], marker=7, ms=6, color=GRIS_FONCE, clip_on=False, zorder=4,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _segments(annees, valeurs):
    """Coupe en suites d'années consécutives : une année manquante interrompt le trait."""
    suites, cour = [], []
    for a, v in zip(annees, valeurs):
        if cour and a != cour[-1][0] + 1:
            suites.append(cour)
            cour = []
        cour.append((a, v))
    if cour:
        suites.append(cour)
    return suites


def _trace_famille(ax, d, valeur, couleur, marque, ls="-", creux=False, texte=None, lw=1.5):
    """Trace une famille : le trait, puis chaque point séparément (une infobulle par point)."""
    d = d.sort_values("annee")
    for suite in _segments(d["annee"].tolist(), d[valeur].tolist()):
        if len(suite) > 1:
            ax.plot([a for a, _ in suite], [v for _, v in suite], color=couleur, ls=ls, lw=lw,
                    zorder=2)
    for r in d.itertuples(index=False):
        p, = ax.plot([r.annee], [getattr(r, valeur)], marker=marque, ms=5, color=couleur,
                     mfc="white" if creux else couleur, mew=1.2, ls="none", zorder=3)
        if texte:
            figtools.infobulle(p, texte(r))


# --- provenance montrée au lecteur ---------------------------------------------------------

PROVENANCE = {
    PRIX: dict(
        perimetre=("prix de cession administré du gaz à la STEG (90,8 dinars la tonne équivalent "
                   "pétrole, 1993-2014) ; prix moyen d'achat de la tep du rapport de contrôle du "
                   "21 juillet 2014 (2007-2013, p. 72) ; prix moyen annuel d'achat de la tep de "
                   "gaz des états financiers de la STEG, exercices 2013 à 2023"),
        caveats=("Trois séries qui ne se raccordent pas. Le prix de cession est un prix "
                 "administré, constant, non un prix d'achat. Le prix moyen de la STEG porte sur "
                 "toutes les sources de gaz et son numérateur comprend le fuel et le gazole. "
                 "Ruptures : 2007 (la STEG comptabilise le gaz à sa valeur économique) et 2015 "
                 "(fin du prix de cession). Aucune valeur avant 1993 ni après 2023. Dinars "
                 "courants.")),
    KWH: dict(
        perimetre=("coût de revient et prix de vente moyen hors taxes du kilowattheure, toutes "
                   "tensions confondues, par famille de source : ESMAP (prix 1994-1999), ANER "
                   "(coût 1996-1998, lu sur un graphique), Banque africaine de développement "
                   "(2000-2010), rapport de contrôle de 2014 (2008-2012), états financiers de la "
                   "STEG puis Observatoire national de l'énergie (2013-2018), Observatoire "
                   "(2019-2025)"),
        caveats=("Les sources ne se raccordent pas. Rupture de 2007 : jusqu'en 2006 le gaz est "
                 "au prix administré, ensuite à sa valeur économique. Aucun coût de revient pour "
                 "1999, 2005-2007 et 2019-2021, aucune valeur reconstituée. Les valeurs de l'ANER "
                 "sont lues sur un graphique, à un millime près. De 2013 à 2018 les états "
                 "financiers de la STEG et l'Observatoire ont la même origine. Les données de "
                 "2022 à 2025 sont dites provisoires avant audit. Millimes courants.")),
    SUBV: dict(
        perimetre=("« subvention d'exploitation » de l'état de résultat de la STEG, 2006-2016 ; "
                   "soutien direct, indirect et total à la STEG du rapport de contrôle du 21 "
                   "juillet 2014 (2007-2013) ; ventilation des états financiers de 2014 (2013 et "
                   "2014)"),
        caveats=("La subvention d'exploitation des comptes n'est pas la ligne budgétaire : jusqu'en "
                 "2014 elle comprend la subvention indirecte, c'est-à-dire le gaz valorisé à sa "
                 "valeur économique. Elle égale le soutien total du rapport de contrôle, à "
                 "l'arrondi imprimé près. Rupture de 2015. Aucune valeur après 2016. Dinars "
                 "courants.")),
    GAZ: dict(
        perimetre=("tableau « prélèvements de gaz » de chaque rapport annuel de la STEG, 2001-2024 : "
                   "gaz algérien (redevance consommée, achats contractuels et additionnels), "
                   "champ de Miskar, autres champs nationaux, total"),
        caveats=("Le total égale la somme des parties chaque année. De 2001 à 2006 les tableaux ne "
                 "séparent pas la redevance des achats de gaz algérien. Le « total des achats "
                 "gaz » de 2019-2024 vient d'un autre tableau et n'est pas le total des "
                 "prélèvements. Quantités en ktep, pouvoir calorifique supérieur.")),
}
_ORIGINE: dict[str, dict] = {}


def _declarer(series_id: str, cles=None) -> None:
    """Provenance montrée au lecteur : clés restreintes à celles que la figure emploie et
    présentes dans la bibliographie du livre ; périmètre et réserves réécrits pour lui."""
    if series_id not in _ORIGINE:
        _ORIGINE[series_id] = dict(figtools.meta(series_id))
    origine = _ORIGINE[series_id]
    connues = figtools._ref_index()
    cles = list(origine.get("sources", [])) if cles is None else list(dict.fromkeys(cles))
    champs = {k: v for k, v in origine.items() if k != "id" and not k.endswith("_ar")}
    champs["sources"] = [k for k in cles if k in connues]
    champs.update(PROVENANCE.get(series_id, {}))
    figtools.register_provenance(series_id, **champs)


# --- 1. Le prix d'achat de la tonne équivalent pétrole de gaz --------------------------------

FAM_PRIX = (
    ("prix_de_cession", "Prix de cession administré, 1993-2014 (rapport de contrôle de 2014)",
     BLEU, "s", "-"),
    ("rapport_de_controle_2014", "Prix moyen d'achat de la tep, rapport de contrôle de 2014, "
     "2007-2013", ORANGE, "o", "--"),
    ("etats_financiers_steg", "Prix moyen d'achat de la tep de gaz, états financiers de la STEG, "
     "2013-2023", VERT, "^", "-"),
)


def fig_prix_achat_gaz():
    figtools.apply_lang_font()
    d = figtools.series(PRIX)
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    for fam, etiquette, couleur, marque, ls in FAM_PRIX:
        df = d[d["famille"] == fam]
        _trace_famille(
            ax, df, "valeur", couleur, marque, ls=ls,
            texte=lambda r, e=etiquette: f"{r.annee} · {e} : {_nb(r.valeur)} dinars par tep "
                                         f"({r.source}, {r.page})")
        if fam != "prix_de_cession":
            etiq = {"rapport_de_controle_2014": ((0, (0, 7)), (-1, (-3, 8, "right"))),
                    "etats_financiers_steg": ((0, (7, -14, "left")), (-1, (-6, -13, "right")))}
            for i, (dx, dy, *ha) in ((i, (o[0], o[1], *o[2:])) for i, o in etiq[fam]):
                r = df.iloc[i]
                ax.annotate(_v(r["valeur"]), xy=(r["annee"], r["valeur"]), xytext=(dx, dy),
                            textcoords="offset points", ha=ha[0] if ha else "center",
                            fontsize=7, color=couleur)
    haut = d[d["famille"] == "etats_financiers_steg"].sort_values("valeur").iloc[-1]
    ax.annotate(_v(haut["valeur"]), xy=(haut["annee"], haut["valeur"]), xytext=(0, 7),
                textcoords="offset points", ha="center", fontsize=7, color=VERT)
    ax.annotate("90,8", xy=(2003, 90.8), xytext=(0, 7), textcoords="offset points", ha="center",
                fontsize=7.5, color=BLEU)
    for r in d[d["rupture"].fillna("") != ""].itertuples(index=False):
        _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    _cadre(ax, "Dinars courants par tonne équivalent pétrole")
    ax.set_xlim(1992.3, 2023.7)
    ax.set_xticks(range(1993, 2024, 2))
    ax.set_ylim(0, 1650)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=c, marker=m, ls=ls, lw=1.5, ms=5,
                       label=figtools.fig_text(e)) for _, e, c, m, ls in FAM_PRIX]
    poignees.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                           label="rupture de série (infobulle sur le triangle)"))
    _legende(ax, poignees, ncol=1, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_prix_achat_gaz():
    d = figtools.series(PRIX)
    d = d[d["famille"] != "observatoire_import_gaz_algerien"].sort_values(["famille", "annee"])
    noms = {f: e.split(",")[0] for f, e, *_ in FAM_PRIX}
    noms = {"prix_de_cession": "prix de cession administré",
            "rapport_de_controle_2014": "prix moyen d'achat, rapport de contrôle de 2014",
            "etats_financiers_steg": "prix moyen d'achat, états financiers de la STEG"}
    table = d[["famille", "annee", "valeur", "etat", "source", "page", "lecture", "rupture"]].copy()
    table["famille"] = table["famille"].map(noms)
    table.columns = ["Famille", "Année", "Dinars courants par tep", "État", "Source", "Page",
                     "Lecture", "Rupture"]
    return ([(None, fig_prix_achat_gaz())], table.reset_index(drop=True),
            {PRIX: _cles(d)}, "fig_compensation_eg_prix_achat_gaz")


# --- 2. Le coût de revient et le prix de vente moyen du kilowattheure ------------------------

FAM_KWH = (
    ("esmap", "ESMAP, 1994-1999 (prix seul)", GRIS, "v"),
    ("aner", "ANER, 1996-1998 (coût lu sur graphique)", BRUN, "D"),
    ("bad_electricite_vi", "BAD, Électricité VI, 2000-2004", VIOLET, "s"),
    ("bad_electricite_vii", "BAD, Électricité VII, 2005-2007 (prix seul)", ROSE, "P"),
    ("cgf_2014", "Rapport de contrôle de 2014, 2008-2012", ORANGE, "o"),
    ("steg_observatoire_2013_2018", "États financiers de la STEG puis Observatoire, 2013-2018",
     BLEU, "^"),
    ("observatoire_2019_2021", "Observatoire, 2019-2021 (prix seul)", TEAL, "<"),
    ("observatoire_2022_2025", "Observatoire, 2022-2025 (provisoire avant audit)", VERT, ">"),
)
SANS_COUT = ((1998.5, 1999.5), (2004.5, 2007.5), (2018.5, 2021.5))


def _kwh_retenu():
    d = figtools.series(KWH)
    return d[d["retenu"] == "oui"]


def fig_cout_prix_kwh():
    figtools.apply_lang_font()
    d = _kwh_retenu()
    fig, (axc, axp) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True, sharey=True)
    for ax, grandeur, titre in ((axc, "cout_de_revient", "Coût de revient"),
                                (axp, "prix_de_vente_moyen", "Prix de vente moyen, hors taxes")):
        for fam, etiquette, couleur, marque in FAM_KWH:
            df = d[(d["famille"] == fam) & (d["grandeur"] == grandeur)]
            if fam == "bad_electricite_vii":
                df = df[df["annee"] <= 2007]
            if df.empty:
                continue
            _trace_famille(
                ax, df, "valeur", couleur, marque,
                texte=lambda r, e=etiquette, t=titre: (
                    f"{r.annee} · {t.lower()} · {e} : {_nb(r.valeur)} millimes par kWh "
                    f"({r.source}, {r.page} ; {r.etat})"))
        ax.set_title(figtools.fig_text(titre), fontsize=9, loc="left")
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_ylabel("Millimes courants par kWh")
        for r in d[(d["rupture"].fillna("") != "")].head(1).itertuples(index=False):
            figtools.marque_rupture(ax, int(r.rupture_annee))
            if ax is axc:
                _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    for a0, a1 in SANS_COUT:
        axc.axvspan(a0, a1, color="#d0d7de", alpha=0.55, lw=0, zorder=0)
        axc.annotate("aucun coût publié", xy=((a0 + a1) / 2, 250), ha="center", va="center",
                     rotation=90, fontsize=6.5, color=GRIS_FONCE)
    axp.set_xlabel("Année")
    axp.set_xlim(1993.3, 2025.7)
    axp.set_xticks(range(1994, 2026, 2))
    axp.set_ylim(0, 520)
    poignees = [Line2D([0], [0], color=c, marker=m, ls="-", lw=1.5, ms=5,
                       label=figtools.fig_text(e)) for _, e, c, m in FAM_KWH]
    poignees.append(Patch(facecolor="#d0d7de", label="années sans coût de revient publié"))
    poignees.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                           label="rupture de série (infobulle sur le triangle)"))
    _legende(axp, poignees, ncol=2, y=-0.22)
    fig.tight_layout()
    return fig


def _figure_cout_prix_kwh():
    d = figtools.series(KWH)
    noms = {f: e for f, e, *_ in FAM_KWH}
    gr = {"cout_de_revient": "coût de revient", "prix_de_vente_moyen": "prix de vente moyen",
          "cout_combustibles": "coût : combustibles", "cout_personnel": "coût : personnel",
          "cout_charges_financieres_assurances": "coût : charges financières et assurances",
          "cout_amortissements": "coût : amortissements", "cout_divers": "coût : divers"}
    table = d.sort_values(["famille", "annee", "grandeur"]).copy()
    table["tracee"] = [("non" if r.retenu != "oui" or (r.famille == "bad_electricite_vii"
                                                       and r.annee > 2007)
                        or r.grandeur.startswith("cout_") and r.grandeur != "cout_de_revient"
                        else "oui") for r in table.itertuples(index=False)]
    table["famille"] = table["famille"].map(noms)
    table["grandeur"] = table["grandeur"].map(gr)
    table = table[["famille", "annee", "grandeur", "valeur", "etat", "tracee", "source", "page",
                   "lecture", "rupture", "remarque"]]
    table.columns = ["Famille", "Année", "Grandeur", "Millimes courants par kWh", "État",
                     "Tracée", "Source", "Page", "Lecture", "Rupture", "Remarque"]
    return ([(None, fig_cout_prix_kwh())], table.reset_index(drop=True),
            {KWH: _cles(d)}, "fig_compensation_eg_cout_prix_kwh")


# --- 3. La subvention d'exploitation de la STEG ----------------------------------------------

def fig_subvention():
    figtools.apply_lang_font()
    d = figtools.series(SUBV)
    comptes = d[d["grandeur"] == "subvention_exploitation"].sort_values("annee")
    cg = d[d["famille"] == "rapport_de_controle_2014"].pivot(index="annee", columns="grandeur",
                                                             values="valeur")
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    for a, v in cg.iterrows():
        barre = ax.bar([a], [v["soutien_direct"]], width=0.62, color=BLEU, hatch="//",
                       edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien direct (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_direct'])} millions de dinars")
        barre = ax.bar([a], [v["soutien_indirect"]], bottom=[v["soutien_direct"]], width=0.62,
                       color=ORANGE, edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien indirect (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_indirect'])} millions de dinars")
    ax.plot(comptes["annee"], comptes["valeur"], color=NOIR, lw=1.2, zorder=3)
    for r in comptes.itertuples(index=False):
        p, = ax.plot([r.annee], [r.valeur], marker="o", ms=6, color=NOIR, ls="none", zorder=4)
        figtools.infobulle(p, f"{r.annee} · subvention d'exploitation des comptes de la STEG : "
                              f"{_nb(r.valeur)} millions de dinars ({r.source}, {r.page})")
        ax.annotate(_v(r.valeur), xy=(r.annee, r.valeur), xytext=(0, 7),
                    textcoords="offset points", ha="center", fontsize=7)
    for r in comptes[comptes["rupture"].fillna("") != ""].itertuples(index=False):
        _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    _cadre(ax, "Millions de dinars courants")
    ax.set_xticks(range(2006, 2017))
    ax.set_xlim(2005.4, 2016.6)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.08)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [
        Patch(facecolor=BLEU, hatch="//", edgecolor="white",
              label="soutien direct (rapport de contrôle de 2014)"),
        Patch(facecolor=ORANGE, label="soutien indirect (rapport de contrôle de 2014)"),
        Line2D([0], [0], color=NOIR, marker="o", ms=6, lw=1.2,
               label="subvention d'exploitation des comptes de la STEG"),
        Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
               label="rupture de série (infobulle sur le triangle)")], ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_subvention():
    d = figtools.series(SUBV)
    noms = {"comptes_steg": "comptes de la STEG",
            "rapport_de_controle_2014": "rapport de contrôle de 2014",
            "etats_financiers_2014": "états financiers de 2014"}
    gr = {"subvention_exploitation": "subvention d'exploitation", "soutien_direct": "soutien direct",
          "soutien_indirect": "soutien indirect", "soutien_total": "soutien total",
          "subvention_directe": "subvention directe reçue",
          "subvention_indirecte": "subvention indirecte sur l'achat du gaz algérien"}
    table = d.sort_values(["famille", "grandeur", "annee"]).copy()
    table["tracee"] = ["non" if r.famille == "etats_financiers_2014" or r.grandeur == "soutien_total"
                       else "oui" for r in table.itertuples(index=False)]
    table["famille"] = table["famille"].map(noms)
    table["grandeur"] = table["grandeur"].map(gr)
    table = table[["famille", "annee", "grandeur", "valeur", "etat", "tracee", "source", "page",
                   "lecture", "rupture", "remarque"]]
    table.columns = ["Famille", "Année", "Grandeur", "Millions de dinars courants", "État",
                     "Tracée", "Source", "Page", "Lecture", "Rupture", "Remarque"]
    return ([(None, fig_subvention())], table.reset_index(drop=True),
            {SUBV: _cles(d)}, "fig_compensation_eg_subvention")


# --- 4. Le gaz prélevé par la STEG, par source -----------------------------------------------

PARTIES_GAZ = (
    ("gaz_algerien_non_ventile", "Gaz algérien, redevance et achats non distingués (2001-2006)",
     GRIS, "\\\\"),
    ("redevance_consommee", "Redevance consommée sur le gaz algérien en transit", BRUN, ""),
    ("achats_contractuels", "Achats contractuels de gaz algérien", BLEU, ""),
    ("achats_additionnels", "Achats additionnels de gaz algérien", BLEU_CLAIR, "//"),
    ("miskar", "Gaz du champ de Miskar", VERT, ""),
    ("autres_gaz_national", "Autres champs nationaux", VIOLET, ""),
)


def fig_gaz_sources():
    figtools.apply_lang_font()
    d = figtools.series(GAZ)
    annees = sorted(int(a) for a in d["annee"].unique())
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for a in annees:
        da = d[d["annee"] == a].set_index("source_gaz")
        total = float(da.loc["total_preleve", "valeur"])
        bas = 0.0
        for cle, etiquette, couleur, hachure in PARTIES_GAZ:
            if cle not in da.index:
                continue
            v = float(da.loc[cle, "valeur"])
            if v > 0:
                barre = ax.bar([a], [v], bottom=bas, width=0.74, color=couleur, hatch=hachure,
                               edgecolor="white", zorder=2)
                figtools.infobulle(barre[0], f"{a} · {etiquette} : {_nb(v, 0)} ktep "
                                             f"({da.loc[cle, 'source']}, {da.loc[cle, 'page']})")
            bas += v
        if bas != total:
            raise ValueError(f"gaz prélevé {a} : somme des parties {bas} ≠ total {total}")
        ax.annotate(_nb(total, 0), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                    ha="center", va="bottom", fontsize=6.5)
    _cadre(ax, "Milliers de tonnes équivalent pétrole (ktep, PCS)")
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], rotation=90, fontsize=7.5)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.06)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(e))
                  for _, e, c, h in PARTIES_GAZ], ncol=2, y=-0.2)
    fig.tight_layout()
    return fig


def _figure_gaz_sources():
    d = figtools.series(GAZ)
    noms = {c: e for c, e, *_ in PARTIES_GAZ}
    noms.update({"total_preleve": "total des prélèvements (égal à la somme des parties)",
                 "total_des_achats_gaz": "total des achats de gaz (autre tableau, hors somme)"})
    ordre = {c: i for i, c in enumerate(list(noms))}
    table = d.assign(_o=d["source_gaz"].map(ordre)).sort_values(["annee", "_o"]).copy()
    table["source_gaz"] = table["source_gaz"].map(noms)
    table = table[["annee", "source_gaz", "valeur", "etat", "detail", "source", "page", "lecture",
                   "remarque"]]
    table.columns = ["Année", "Source du gaz", "ktep (PCS)", "État", "Lignes réunies", "Source",
                     "Page", "Lecture", "Remarque"]
    return ([(None, fig_gaz_sources())], table.reset_index(drop=True),
            {GAZ: _cles(d)}, "fig_compensation_eg_gaz_sources")


# --- registre ---------------------------------------------------------------------------------

FIGURES = {
    "prix_achat_gaz": _figure_prix_achat_gaz,
    "cout_prix_kwh": _figure_cout_prix_kwh,
    "subvention": _figure_subvention,
    "gaz_sources": _figure_gaz_sources,
}
NON_MONETAIRES = {"gaz_sources"}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        _declarer(sid, liste)
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nom not in NON_MONETAIRES)
    plt.close("all")

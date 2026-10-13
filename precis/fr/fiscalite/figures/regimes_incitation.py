"""Figures du chapitre « Les régimes d'incitation à l'investissement » du livre *Fiscalité*.

D'OÙ VIENNENT LES DONNÉES. De quatre relevés versionnés DANS le livre, à côté du chapitre
(`incitations/*.csv`, chacun avec son manifeste `.csv.yml`) : ils reprennent, sans rien y
ajouter, les tableaux du chapitre — ce que fixent les lois et les décrets cités, et le
tableau d'une étude. Ce n'est pas une statistique de l'entrepôt : les figures les lisent
directement, comme `remunerations_publiques/figures/augmentations.py` lit le sien.

QUATRE FIGURES, AUCUN RACCORD.
  - `frise` : une bande par régime, 1969-2026, et, dessous, l'imposition des bénéfices tirés
    de l'exportation. Seuls les taux qu'un texte fixe sont tracés ; une exonération de dix
    ans ou une déduction de 50 % n'est pas convertie en taux, elle est écrite.
  - `zones` : délégations classées par groupe. Les listes de 1994 et de 1999 classent des
    gouvernorats entiers et ne se comptent pas en délégations : pas de barre, un texte.
  - `prime` : taux et plafond de la prime de développement régional, en escalier depuis le
    25 février 2008. Les barèmes de 1994 et de 1999, dont la date d'effet n'est pas
    établie, sont des points isolés.
  - `ghazouani` : ÉTUDE EXTÉRIEURE, tracée seule ; jamais superposée au budgétaire.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
RELEVES = HERE.parent / "incitations"

FRISE = "regimes-incitation-frise"
TAUX = "benefices-exportes-taux"
ZONES = "zones-developpement-regional-delegations"
PRIME = "prime-developpement-regional-bareme"
GHAZOUANI = "ghazouani-2011-cout-incitations"

BLEU, ORANGE, VERT, GRIS, VIOLET = "#0969da", "#bc4c00", "#1a7f37", "#57606a", "#8250df"
FIN = 2026  # année de l'état du droit exposé au chapitre


def _sources(nom: str) -> list[str]:
    import yaml
    return list(yaml.safe_load((RELEVES / f"{nom}.csv.yml").read_text(encoding="utf-8"))["sources"])


def _lire(nom: str) -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{nom}.csv")


figtools.register_provenance(
    FRISE, titre="Régimes d'incitation à l'investissement : règles et périodes, 1969-2026",
    sources=_sources("regimes-frise"), unite="années (bornes des périodes)",
    perimetre=("régimes suivis au chapitre : code de 1969, exportation, marché intérieur, "
               "développement régional, agriculture et pêche, entreprises nouvelles, primes"),
    caveats=("Bornes en années, pour le tracé : les dates d'effet exactes sont au chapitre. Le "
             "texte qui met fin à la loi de 1972 et à celle de 1974 n'est pas identifié : leurs "
             "bandes s'arrêtent au code de 1993, et le tracé le signale."))
figtools.register_provenance(
    TAUX, titre="Imposition des bénéfices tirés de l'exportation, 1972-2026",
    sources=_sources("benefices-exportes-taux"), unite="% des bénéfices",
    perimetre="taux fixés par les textes ; échéances votées puis reportées",
    caveats=("Seuls les taux qu'un texte fixe sont tracés. L'exonération de dix ans suivie d'un "
             "taux réduit (1972) et la déduction totale suivie d'une déduction de 50 % (1993) "
             "dépendent de l'âge de l'entreprise : elles sont écrites, non converties en taux."))
figtools.register_provenance(
    ZONES, titre="Zones de développement régional en nombre de délégations, 1994-2024",
    sources=_sources("zones-delegations"), unite="délégations",
    perimetre="industrie, artisanat et services ; zones touristiques non comptées",
    caveats=("Nombres comptés sur les listes des décrets, qui ne publient aucun décompte. Les "
             "listes de 1994 et de 1999 classent des gouvernorats entiers : elles ne se comptent "
             "pas en délégations, et leurs dates d'effet ne sont pas établies."))
figtools.register_provenance(
    PRIME, titre="Prime de développement régional : taux et plafonds, 1994-2017",
    sources=_sources("prime-developpement-regional"),
    unite="% du coût de l'investissement ; millions de dinars courants",
    perimetre="industries manufacturières et services éligibles",
    caveats=("Dates d'effet des barèmes de 1994 et de 1999 non établies : points isolés. "
             "L'assiette change de nom d'un barème à l'autre ; les taux ne portent pas "
             "nécessairement sur la même base. Plafonds en dinars courants."))
figtools.register_provenance(
    GHAZOUANI, titre="Incitations du code de 1993 selon Ghazouani (2011), 1994-2007",
    sources=_sources("ghazouani-2011-cout-incitations"),
    unite="% du PIB, des recettes fiscales, des dépenses de gestion et de développement",
    perimetre=("étude extérieure : incitations fiscales et financières du code d'incitations "
               "aux investissements, tableau 1, p. 7"),
    caveats=("L'étude ne dit ni comment le coût de chaque incitation est chiffré, ni la base du "
             "PIB employé. Les années 2004 et 2005 n'y sont pas commentées."))


def _nb(v, dec=0) -> str:
    s = f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s


def _cadre(ax):
    ax.grid(True, axis="y", alpha=0.3)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)


# --- 1. La frise des régimes ---------------------------------------------------------------

PISTES = ["Code des investissements de 1969", "Marché intérieur (industries manufacturières)",
          "Exportation", "Développement régional", "Agriculture et pêche",
          "Entreprises nouvelles", "Primes versées par le budget",
          "Droits acquis du code de 1993"]
COULEURS = dict(zip(PISTES, [GRIS, GRIS, BLEU, VERT, "#9a6700", VIOLET, ORANGE, GRIS]))
# (année, libellé, alignement du libellé par rapport au trait, décalage vertical en points)
RUPTURES = [(1972, "1972\nrégime de\nl'exportation", "left", 0),
            (1994, "1993\ncode\nd'incitations", "left", 0),
            (2014, "2014\nexportation\nimposée", "right", 0),
            (2017, "2017\ncode abrogé", "right", 30),
            (2019, "2019\nfin du régime\nde l'exportation", "left", 0)]


def table_frise() -> pd.DataFrame:
    f = _lire("regimes-frise")
    a = pd.DataFrame({"Régime": f["piste"], "Règle": f["libelle"], "Début": f["debut"].astype(str),
                      "Fin": f["fin"].astype(str), "État": f["etat"], "Taux (%)": "",
                      "Texte": f["texte"], "Article": f["localisateur"]})
    t = _lire("benefices-exportes-taux")
    b = pd.DataFrame({"Régime": "Imposition des bénéfices tirés de l'exportation",
                      "Règle": t["regle"], "Début": t["date_effet"],
                      "Fin": t["date_fin"].fillna(""), "État": t["etat"],
                      "Taux (%)": [("" if pd.isna(v) else _nb(v, 1 if v % 1 else 0))
                                   for v in t["taux_pct"]],
                      "Texte": t["texte"], "Article": t["localisateur"]})
    return pd.concat([a, b], ignore_index=True)


def fig_frise():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    f = _lire("regimes-frise")
    fig, (ax, bas) = plt.subplots(2, 1, figsize=(10.5, 7.4), sharex=True,
                                  gridspec_kw={"height_ratios": [3.3, 1.5], "hspace": 0.08})
    for i, piste in enumerate(PISTES):
        y = len(PISTES) - 1 - i
        for k, r in enumerate(f[f["piste"] == piste].itertuples()):
            style = dict(facecolor=COULEURS[piste], alpha=0.85 if k % 2 == 0 else 0.6,
                         edgecolor="white", lw=1)
            if r.etat == "droits acquis":
                style.update(alpha=0.35, hatch="///", edgecolor=COULEURS[piste])
            if r.etat == "fin non établie":
                style.update(alpha=0.45)
            barre = ax.barh([y], [r.fin + 1 - r.debut], left=[r.debut], height=0.62, **style)
            figtools.infobulle(barre[0], f"{piste} · {r.debut}-{r.fin} · {r.libelle} "
                                         f"({r.etat})")
            large = r.fin + 1 - r.debut
            if large >= 9:
                ax.text(r.debut + 0.3, y, ft(r.etiquette), va="center", ha="left", fontsize=6.6,
                        color="white" if style["alpha"] > 0.5 else "#1f2328", clip_on=True)
            else:
                ax.annotate(ft(r.etiquette), xy=(r.fin + 1, y), xytext=(3, 0),
                            textcoords="offset points", va="center", ha="left", fontsize=6.6,
                            color="#1f2328") if r.fin >= FIN - 6 and r.debut >= 2014 else None
            if r.etat == "fin non établie":
                ax.annotate(ft("fin non établie"), xy=(r.fin + 1, y - 0.31), xytext=(-2, -1),
                            textcoords="offset points", va="top", ha="right", fontsize=5.8,
                            color=GRIS, style="italic")
    ax.set_yticks(range(len(PISTES)))
    ax.set_yticklabels([ft(p) for p in reversed(PISTES)], fontsize=7.6)
    ax.set_ylim(-0.6, len(PISTES) + 1.3)
    for annee, texte, cote, haut in RUPTURES:
        for a in (ax, bas):
            a.axvline(annee, color=GRIS, ls=(0, (2, 2)), lw=0.9, zorder=0)
        ax.annotate(ft(texte), xy=(annee, len(PISTES) - 0.45),
                    xytext=(2 if cote == "left" else -2, haut), textcoords="offset points",
                    ha=cote, va="bottom", fontsize=6.4, color=GRIS)
    for cote in ("top", "right", "left"):
        ax.spines[cote].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title(ft("Les régimes d'incitation à l'investissement, 1969-2026"), fontsize=10)

    # Bas : imposition des bénéfices tirés de l'exportation.
    t = _lire("benefices-exportes-taux")
    for r in t[t["etat"] == "règle sans taux unique"].itertuples():
        d0, d1 = figtools.abscisse_date(r.date_effet), figtools.abscisse_date(r.date_fin) + 1 / 365
        zone = bas.axvspan(d0, d1, color=BLEU, alpha=0.10, lw=0)
        figtools.infobulle(zone, r.regle)
        mots = ("exonération dix ans,\npuis taux de 10 %\n(aucun taux unique)" if d0 < 1990
                else "déduction totale dix ans,\npuis de 50 %\n(aucun taux unique)")
        bas.text((d0 + d1) / 2, 12.5, ft(mots), ha="center", va="center", fontsize=6.8,
                 color="#1f2328")
    applique = t[t["etat"] == "appliqué"].iloc[0]
    x0, x1 = figtools.abscisse_date(applique.date_effet), figtools.abscisse_date("2021-01-01")
    trait, = bas.plot([x0, x1], [10, 10], color=BLEU, lw=2.4, solid_capstyle="butt")
    figtools.infobulle(trait, applique.regle)
    dc = t[t["etat"] == "droit commun"].sort_values("date_effet")
    xs = [figtools.abscisse_date(d) for d in dc["date_effet"]] + [FIN + 1]
    ys = list(dc["taux_pct"])
    bas.step(xs, ys + [ys[-1]], where="post", color=GRIS, lw=2, ls=(0, (4, 2)))
    for x, v in zip(xs, ys):
        bas.annotate(ft(f"{_nb(v)} %"), xy=(x, v), xytext=(3, 3), textcoords="offset points",
                     fontsize=7, color=GRIS)
    bas.annotate(ft("10 %"), xy=(x0, 10), xytext=(3, 3), textcoords="offset points", fontsize=7,
                 color=BLEU)
    for r in t[t["etat"] == "voté puis reporté"].itertuples():
        p, = bas.plot([figtools.abscisse_date(r.date_effet)], [r.taux_pct], marker="o", ms=5.5,
                      mfc="white", mec=BLEU, ls="")
        figtools.infobulle(p, r.regle)
    for r in t[t["etat"] == "voté puis abrogé"].itertuples():
        p, = bas.plot([figtools.abscisse_date(r.date_effet)], [r.taux_pct], marker="D", ms=5,
                      mfc="white", mec=ORANGE, ls="")
        figtools.infobulle(p, r.regle)
    bas.set_ylim(0, 25)
    bas.set_xlim(1968, FIN + 1.5)
    bas.set_xticks(list(range(1970, 2030, 5)))
    bas.set_ylabel(ft("Imposition des bénéfices\ntirés de l'exportation (%)"), fontsize=7.6)
    _cadre(bas)
    bas.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.4, label=ft("taux appliqué aux bénéfices de l'exportation")),
        Line2D([], [], marker="o", mfc="white", mec=BLEU, ls="", ms=5.5,
               label=ft("échéance votée, puis reportée (2008, 2011, 2012, 2013)")),
        Line2D([], [], color=GRIS, lw=2, ls=(0, (4, 2)),
               label=ft("taux de droit commun de l'impôt sur les sociétés, après la fin du régime")),
        Line2D([], [], marker="D", mfc="white", mec=ORANGE, ls="", ms=5,
               label=ft("palier de 13,5 % voté pour 2021, abrogé avant de s'appliquer")),
        Patch(facecolor=BLEU, alpha=0.10, label=ft("règle écrite, sans taux unique")),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=7.2, frameon=False)
    fig.subplots_adjust(left=0.24, right=0.985, top=0.95, bottom=0.14)
    return fig


# --- 2. Les délégations classées par groupe ------------------------------------------------

RANGS = [("moins aidée", "#9ecae1", "catégorie la moins aidée"),
         ("intermédiaire", "#3182bd", "catégorie intermédiaire"),
         ("plus aidée", "#08519c", "catégorie la plus aidée")]


def table_zones() -> pd.DataFrame:
    z = _lire("zones-delegations")
    return pd.DataFrame({
        "Année": z["annee"], "Date d'effet": z["date_effet"].fillna("non établie"),
        "Rang": z["rang"], "Catégorie": z["categorie"],
        "Délégations": [("" if pd.isna(v) else int(v)) for v in z["delegations"]],
        "Gouvernorats": [("" if pd.isna(v) else int(v)) for v in z["gouvernorats"]],
        "Liste dénombrable en délégations": z["denombrable"],
        "Texte": z["texte"], "Article": z["localisateur"]})


def fig_zones():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    z = _lire("zones-delegations")
    annees = sorted(z["annee"].unique())
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for i, a in enumerate(annees):
        za = z[z["annee"] == a]
        if (za["denombrable"] == "non").any():
            texte = "\n".join(c.replace(" : ", " :\n").replace(" et ", "\net ")
                              for c in za["categorie"])
            ax.text(i, 6, ft(texte + "\n\n(liste non dénombrable\nen délégations ;\n"
                                     "date d'effet non établie)"),
                    ha="center", va="bottom", fontsize=6.6, color=GRIS,
                    bbox=dict(facecolor="#f6f8fa", edgecolor="#d0d7de", boxstyle="round,pad=0.4"))
            continue
        bas_ = 0
        for rang, couleur, _ in RANGS:
            l = za[za["rang"] == rang]
            if l.empty:
                continue
            n = int(l["delegations"].iloc[0])
            barre = ax.bar([i], [n], bottom=bas_, width=0.62, color=couleur, edgecolor="white")
            figtools.infobulle(barre[0], f"{a} · {l['categorie'].iloc[0]} : {n} délégations")
            ax.text(i, bas_ + n / 2, ft(f"{l['categorie'].iloc[0]}\n{n}"), ha="center",
                    va="center", fontsize=7, color="white" if rang != "moins aidée" else "#1f2328")
            bas_ += n
        ax.text(i, bas_ + 2, ft(f"{bas_} délégations"), ha="center", va="bottom", fontsize=7.6)
    ax.set_xticks(range(len(annees)))
    ax.set_xticklabels([str(a) for a in annees])
    ax.set_xlim(-0.6, len(annees) - 0.4)
    ax.set_ylim(0, 170)
    ax.set_ylabel(ft("Délégations classées"))
    ax.set_title(ft("Zones de développement régional : délégations classées, par catégorie"),
                 fontsize=10)
    _cadre(ax)
    ax.legend(handles=[Patch(facecolor=c, label=ft(t)) for _, c, t in RANGS],
              loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=3, fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


# --- 3. La prime de développement régional, en escalier ------------------------------------

def table_prime() -> pd.DataFrame:
    p = _lire("prime-developpement-regional")
    return pd.DataFrame({
        "Année": p["annee"], "Date d'effet": p["date_effet"].fillna("non établie"),
        "Rang": p["rang"], "Catégorie de zones": p["categorie"],
        "Prime (% du coût)": p["taux_pct"],
        "Plafond (millions de dinars courants)": [("" if pd.isna(v) else v)
                                                  for v in p["plafond_md"]],
        "Texte": p["texte"], "Article": p["localisateur"]})


def fig_prime(grandeur: str = "taux_pct"):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    p = _lire("prime-developpement-regional")
    dates = p[p["date_effet"].notna()]
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    unite = " %" if grandeur == "taux_pct" else " MD"
    dec = 0 if grandeur == "taux_pct" else 2
    for rang, couleur, libelle in RANGS:
        d = dates[(dates["rang"] == rang) & dates[grandeur].notna()].sort_values("date_effet")
        xs = [figtools.abscisse_date(x) for x in d["date_effet"]]
        ys = list(d[grandeur])
        fin = FIN + 1 if rang != "intermédiaire" else figtools.abscisse_date("2017-01-01")
        ax.step(xs + [fin], ys + [ys[-1]], where="post", color=couleur, lw=2.2, label=ft(libelle))
        if rang == "intermédiaire":
            ax.plot([fin], [ys[-1]], marker="o", mfc="white", mec=couleur, ms=6, ls="")
            ax.annotate(ft("réunie au\ndeuxième groupe"), xy=(fin, ys[-1]), xytext=(5, -3),
                        textcoords="offset points", fontsize=6.6, color=GRIS, va="top")
        precedent = None
        for x, v, cat in zip(xs, ys, d["categorie"]):
            if v != precedent:
                ax.annotate(ft(f"{_nb(v, dec if v % 1 else 0)}{unite}"), xy=(x, v), xytext=(3, 3),
                            textcoords="offset points", fontsize=7, color="#1f2328")
            precedent = v
    isoles = p[p["date_effet"].isna() & p[grandeur].notna()]
    for r in isoles.itertuples():
        couleur = dict((a, b) for a, b, _ in RANGS)[r.rang]
        pt, = ax.plot([r.annee], [getattr(r, grandeur)], marker="s", mfc="white", mec=couleur,
                      ms=6, ls="")
        figtools.infobulle(pt, f"{r.annee} · {r.categorie} : {_nb(getattr(r, grandeur))}{unite} "
                               "(date d'effet non établie)")
        ax.annotate(ft(f"{_nb(getattr(r, grandeur))}{unite}"), xy=(r.annee, getattr(r, grandeur)),
                    xytext=(5, -3), textcoords="offset points", fontsize=7, color=GRIS)
    for date, texte in (("2008-02-25", "25 février 2008"), ("2011-05-19", "19 mai 2011"),
                        ("2017-01-01", "1er janvier 2017")):
        ax.axvline(figtools.abscisse_date(date), color=GRIS, ls=(0, (2, 2)), lw=0.8, zorder=0)
        ax.annotate(ft(texte), xy=(figtools.abscisse_date(date), 1),
                    xycoords=("data", "axes fraction"), xytext=(3, -3),
                    textcoords="offset points", fontsize=6.6, color=GRIS, va="top")
    ax.set_xlim(1993, FIN + 1.2)
    ax.set_ylim(0, 36 if grandeur == "taux_pct" else 3.5)
    ax.set_ylabel(ft("Prime, en % du coût de l'investissement" if grandeur == "taux_pct"
                     else "Plafond de la prime (millions de dinars courants)"))
    _cadre(ax)
    poignees = [Line2D([], [], color=c, lw=2.2, label=ft(t)) for _, c, t in RANGS]
    if len(isoles):
        poignees.append(Line2D([], [], marker="s", mfc="white", mec=GRIS, ls="", ms=6,
                               label=ft("barèmes de 1994 et de 1999 : date d'effet non établie")))
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=2,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_prime():
    return [("Taux de la prime", fig_prime("taux_pct")),
            ("Plafond de la prime", fig_prime("plafond_md"))]


# --- 4. L'étude de Ghazouani (2011) : étude extérieure, tracée seule -----------------------

def table_ghazouani() -> pd.DataFrame:
    g = _lire("ghazouani-2011-cout-incitations")
    return g.rename(columns={
        "annee": "Année", "pct_pib": "% du PIB (base non précisée par la source)",
        "pct_recettes_fiscales": "% des recettes fiscales",
        "pct_depenses_gestion_developpement": "% des dépenses de gestion et de développement"})


def fig_ghazouani():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _lire("ghazouani-2011-cout-incitations")
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for col, couleur, marque, libelle in (
            ("pct_recettes_fiscales", ORANGE, "s", "en % des recettes fiscales"),
            ("pct_depenses_gestion_developpement", VERT, "^",
             "en % des dépenses de gestion et de développement de l'État"),
            ("pct_pib", BLEU, "o", "en % du PIB (base non précisée par l'étude)")):
        ax.plot(g["annee"], g[col], marque + "-", color=couleur, lw=1.9, ms=4, label=ft(libelle))
    ax.set_ylim(0, 14)
    ax.set_xticks(list(g["annee"]))
    ax.set_ylabel(ft("En %"))
    ax.set_title(ft("Étude extérieure — incitations du code de 1993 selon Ghazouani (2011)"),
                 fontsize=10)
    _cadre(ax)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=1, fontsize=8, frameon=False)
    fig.tight_layout()
    return fig

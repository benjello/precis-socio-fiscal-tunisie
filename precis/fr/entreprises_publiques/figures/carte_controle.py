"""Totaux et figures de la carte de contrôle des entreprises publiques (annexe « Qui contrôle quoi »).

    from figures import carte_controle as cc
    cc.totaux()                         # un paragraphe asis : relations, contrôleurs, hors liste
    cc.graphe(caption=…)                # (a) la « toile » : contrôleurs au centre, entités autour
    cc.barres_controleurs(caption=…)    # (b) nombre d'entités contrôlées par contrôleur
    cc.repartition_secteurs(caption=…)  # (c) répartition des entités contrôlées par secteur

D'OÙ VIENNENT LES DONNÉES. Du relevé versionné de la carte de contrôle (un `.csv` du dossier
`listes`, avec son manifeste `.csv.yml`), engendré par `scripts/carte_controle.py`. La carte
réunit en une table les relations « contrôleur -> entité contrôlée » déjà documentées ailleurs :
périmètres de consolidation des groupes bancaires et de Tunisair, participations publiques dans
les sociétés cotées, portefeuille de l'ETAP, lignes nommées de la STEG, filiales de la STAR.
Chaque ligne garde sa clé de source ; totaux et figures sont comptés ici sur la carte.

La colonne `secteur` du relevé est une LECTURE conservatrice du nom et du périmètre (règle dans le
docstring de `scripts/carte_controle.py`) ; les figures la reprennent telle quelle, sans y ajouter
aucun poids économique. Les trois figures sont sourcées sur le relevé, comme les totaux.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

RELEVE = Path(__file__).resolve().parent.parent / "listes" / "carte-controle"
CARTE = "carte-controle"  # identifiant de provenance du relevé (register_provenance)

# Couleur par secteur. « non classé » reste gris : une absence de lecture, non un secteur.
COULEURS = {
    "banque": "#0969da",
    "SICAV/OPCVM": "#8250df",
    "SICAR/capital-investissement": "#bf3989",
    "leasing": "#2da44e",
    "assurance": "#e16f24",
    "recouvrement": "#cf222e",
    "immobilier": "#7d4e00",
    "énergie-pétrole": "#1b7c83",
    "industrie": "#768390",
    "services": "#d4a72c",
    "non classé": "#c9d1d9",
}
ORDRE_SECTEURS = list(COULEURS)


def _lire() -> pd.DataFrame:
    return pd.read_csv(f"{RELEVE}.csv", dtype=str, keep_default_na=False)


def _sources() -> list[str]:
    import yaml

    manifeste = yaml.safe_load(Path(f"{RELEVE}.csv.yml").read_text(encoding="utf-8"))
    return list(manifeste["sources"])


figtools.register_provenance(
    CARTE,
    titre="Carte de contrôle des entreprises publiques : qui contrôle quoi, au-delà de la liste "
          "officielle",
    sources=_sources(),
    unite="relations de contrôle ou de participation",
    perimetre="relations « contrôleur -> entité contrôlée » déjà documentées ailleurs dans le "
              "précis, réunies en une table : périmètres de consolidation des groupes bancaires et "
              "de Tunisair, participations publiques dans les sociétés cotées, portefeuille de "
              "l'ETAP, lignes nommées de la STEG, filiales de la STAR",
    caveats="Le secteur est une lecture conservatrice du nom et du périmètre, « non classé » au "
            "moindre doute ; ce n'est pas un poids économique. Le capital et le chiffre d'affaires "
            "de chaque entité contrôlée ne sont pas disponibles uniformément : ils ne sont pas "
            "portés ici. Le relevé n'est pas exhaustif (portefeuille non nominatif de la STEG, "
            "offices sans périmètre consolidé) : le périmètre réel est un plancher.",
    source_ligne="d'après la carte de contrôle des entreprises publiques (états financiers "
                 "consolidés, portefeuilles de participations et listes d'actionnaires de la "
                 "Bourse de Tunis réunis en un relevé sourcé)",
)


# --- comptes --------------------------------------------------------------------------------

def comptes() -> dict[str, int]:
    """Nombres comptés sur la carte."""
    df = _lire()
    hors = df.loc[df["controlee_dans_liste_officielle"] == "non", "controlee"]
    return {
        "relations": len(df),
        "controleurs": df["controleur"].nunique(),
        "controlees": df["controlee"].nunique(),
        "controlees_hors_liste": hors.nunique(),
    }


def _entites_par_controleur(df: pd.DataFrame) -> pd.Series:
    """Nombre d'entités contrôlées (distinctes) par contrôleur, décroissant."""
    s = df.groupby("controleur")["controlee"].nunique().sort_values(ascending=False)
    return s


def _entites_par_secteur(df: pd.DataFrame) -> pd.Series:
    """Nombre d'entités contrôlées DISTINCTES par secteur, dans l'ordre fixé des secteurs."""
    distinct = df.drop_duplicates("controlee")
    s = distinct.groupby("secteur")["controlee"].count()
    return s.reindex([x for x in ORDRE_SECTEURS if x in s.index])


def table_controleurs() -> pd.DataFrame:
    df = _lire()
    s = _entites_par_controleur(df)
    off = df.drop_duplicates("controleur").set_index("controleur")[
        "controleur_dans_liste_officielle"]
    return pd.DataFrame({
        "contrôleur": s.index,
        "entités contrôlées": s.values,
        "contrôleur dans la liste officielle": [off.get(c, "") for c in s.index],
    })


def table_secteurs() -> pd.DataFrame:
    df = _lire()
    s = _entites_par_secteur(df)
    return pd.DataFrame({"secteur": s.index, "entités contrôlées (distinctes)": s.values})


def table_relations() -> pd.DataFrame:
    """Le relevé lui-même, remis dans un ordre lisible : c'est le figdata du graphe."""
    df = _lire()[["controleur", "controlee", "secteur", "part_interet_pct",
                  "controlee_dans_liste_officielle", "source"]]
    return df.sort_values(["controleur", "secteur", "controlee"]).reset_index(drop=True)


# --- figures --------------------------------------------------------------------------------

def _legende_secteurs(ax, presents: list[str]) -> None:
    poignees = [Line2D([], [], marker="o", ls="", ms=7, color=COULEURS[s],
                       label=figtools.fig_text(s)) for s in ORDRE_SECTEURS if s in presents]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.02),
              ncol=3, fontsize=7.5, frameon=False, handletextpad=0.3, columnspacing=1.2)


def fig_graphe():
    """La « toile » : contrôleurs disposés en couronne, leurs entités contrôlées autour d'eux.

    CHOIX DE LISIBILITÉ. 130 arêtes d'un bloc seraient illisibles. On ne coupe aucune relation :
    chaque contrôleur reçoit une tranche d'angle proportionnelle à son nombre d'arêtes ; ses
    entités sont semées dans cette tranche, sur une à trois couronnes selon leur nombre, reliées
    au contrôleur par un trait fin. Seuls les CONTRÔLEURS sont étiquetés (les entités sont trop
    nombreuses) ; la couleur des points dit le secteur. L'État figure parmi les contrôleurs : il
    détient en direct huit grandes entreprises publiques.
    """
    figtools.apply_lang_font()
    df = _lire()
    aretes = list(df[["controleur", "controlee", "secteur"]].itertuples(index=False, name=None))
    ordre = list(_entites_par_controleur(df).index)  # gros contrôleurs d'abord
    par_ctrl = {c: [(e, s) for cc_, e, s in aretes if cc_ == c] for c in ordre}

    # Tranche d'angle PROPORTIONNELLE au nombre d'arêtes, mais avec un plancher : sans lui, les
    # contrôleurs à une seule filiale se tasseraient en un paquet d'étiquettes illisibles.
    poids = {c: max(len(par_ctrl[c]), 3) for c in ordre}
    total = sum(poids.values())
    gap = math.radians(3)  # écart entre deux tranches
    dispo = 2 * math.pi - gap * len(ordre)
    R_ctrl = 1.0
    fig, ax = plt.subplots(figsize=(10.5, 10.5))

    angle = math.pi / 2  # on part du haut, sens horaire
    presents = set()
    for c in ordre:
        enfants = par_ctrl[c]
        span = dispo * poids[c] / total
        a0 = angle - gap / 2 - span
        a1 = angle - gap / 2
        centre = (a0 + a1) / 2
        xc, yc = R_ctrl * math.cos(centre), R_ctrl * math.sin(centre)
        etat = (c == "État")
        # entités : colonnes le long de l'angle, 1 à 3 couronnes en rayon
        n = len(enfants)
        rangs = 1 if n <= 7 else (2 if n <= 18 else 3)
        cols = math.ceil(n / rangs)
        for i, (e, s) in enumerate(enfants):
            col, rang = i % cols, i // cols
            if cols == 1:
                a = centre
            else:
                a = a0 + (a1 - a0) * (col + 0.5) / cols
            r = 1.6 + rang * 0.42
            x, y = r * math.cos(a), r * math.sin(a)
            ax.plot([xc, x], [yc, y], "-", color="#d0d7de", lw=0.5, zorder=1)
            couleur = COULEURS.get(s, COULEURS["non classé"])
            ax.plot([x], [y], "o", ms=6, color=couleur, mec="white", mew=0.5, zorder=3)
            presents.add(s)
        # nœud contrôleur
        ax.plot([xc], [yc], "s", ms=12 if etat else 9,
                color="#24292f" if etat else "#57606a", zorder=4)
        # étiquette, posée vers l'intérieur
        lab_r = R_ctrl - 0.16
        lx, ly = lab_r * math.cos(centre), lab_r * math.sin(centre)
        droite = math.cos(centre) >= 0
        ax.annotate(f"{c} ({len(enfants)})", xy=(lx, ly),
                    ha="left" if droite else "right", va="center",
                    fontsize=9 if etat else 8,
                    fontweight="bold" if etat else "normal", color="#24292f")
        angle -= span + gap

    lim = 2.7
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")
    _legende_secteurs(ax, list(presents))
    fig.tight_layout()
    return fig


def _positions_toile(df: pd.DataFrame):
    """Calcule, comme la version matplotlib, les coordonnées de la toile.

    Rend (noeuds_ctrl, noeuds_ent, aretes) où :
      - noeuds_ctrl : liste de dicts {nom, x, y, n, etat}
      - noeuds_ent  : liste de dicts {controlee, controleur, secteur, part, source, x, y}
        (un point par RELATION, comme la figure statique : une entité tenue par deux
        contrôleurs apparaît deux fois, chacune sourcée)
      - aretes      : liste de (x0, y0, x1, y1) du contrôleur vers l'entité
    Positionnement IDENTIQUE à fig_graphe (contrôleurs en couronne, entités en périphérie).
    """
    rel = df[["controleur", "controlee", "secteur", "part_interet_pct", "source"]]
    lignes = list(rel.itertuples(index=False, name=None))
    ordre = list(_entites_par_controleur(df).index)  # gros contrôleurs d'abord
    par_ctrl = {c: [(e, s, p, src) for cc_, e, s, p, src in lignes if cc_ == c] for c in ordre}

    poids = {c: max(len(par_ctrl[c]), 3) for c in ordre}
    total = sum(poids.values())
    gap = math.radians(3)
    dispo = 2 * math.pi - gap * len(ordre)
    R_ctrl = 1.0

    noeuds_ctrl, noeuds_ent, aretes = [], [], []
    angle = math.pi / 2  # du haut, sens horaire
    for c in ordre:
        enfants = par_ctrl[c]
        span = dispo * poids[c] / total
        a0 = angle - gap / 2 - span
        a1 = angle - gap / 2
        centre = (a0 + a1) / 2
        xc, yc = R_ctrl * math.cos(centre), R_ctrl * math.sin(centre)
        etat = (c == "État")
        n = len(enfants)
        rangs = 1 if n <= 7 else (2 if n <= 18 else 3)
        cols = math.ceil(n / rangs)
        for i, (e, s, p, src) in enumerate(enfants):
            col, rang = i % cols, i // cols
            a = centre if cols == 1 else a0 + (a1 - a0) * (col + 0.5) / cols
            r = 1.6 + rang * 0.42
            x, y = r * math.cos(a), r * math.sin(a)
            aretes.append((xc, yc, x, y))
            noeuds_ent.append({"controlee": e, "controleur": c, "secteur": s,
                               "part": p, "source": src, "x": x, "y": y})
        noeuds_ctrl.append({"nom": c, "x": xc, "y": yc, "n": n, "etat": etat})
        angle -= span + gap
    return noeuds_ctrl, noeuds_ent, aretes


def fig_graphe_plotly():
    """La même toile, en Plotly : survol, zoom/pan, et clic-légende pour filtrer un secteur.

    Positions reprises telles quelles de la version matplotlib (`_positions_toile`). Chaque
    secteur est une trace : cliquer sa pastille dans la légende le masque/affiche (filtre
    natif Plotly). Le survol d'une entité donne nom, secteur, part %, contrôleur et source ;
    l'État est mis en avant parmi les contrôleurs.
    """
    import plotly.graph_objects as go

    df = _lire()
    noeuds_ctrl, noeuds_ent, aretes = _positions_toile(df)
    fig = go.Figure()

    # Arêtes, en un seul trait fin gris derrière tout le reste.
    ex, ey = [], []
    for x0, y0, x1, y1 in aretes:
        ex += [x0, x1, None]
        ey += [y0, y1, None]
    fig.add_trace(go.Scatter(
        x=ex, y=ey, mode="lines", line=dict(color="#d0d7de", width=0.5),
        hoverinfo="skip", showlegend=False, name="relations"))

    # Entités groupées par secteur -> une trace par secteur = filtre clic-légende.
    presents = [s for s in ORDRE_SECTEURS if s in {n["secteur"] for n in noeuds_ent}]
    for s in presents:
        pts = [n for n in noeuds_ent if n["secteur"] == s]
        textes = []
        for n in pts:
            part = f"{n['part']} %" if str(n["part"]).strip() else "non imprimée"
            textes.append(
                f"<b>{n['controlee']}</b><br>secteur : {figtools.fig_text(s)}"
                f"<br>part : {part}<br>contrôleur : {n['controleur']}"
                f"<br>source : {n['source']}")
        fig.add_trace(go.Scatter(
            x=[n["x"] for n in pts], y=[n["y"] for n in pts], mode="markers",
            name=figtools.fig_text(s), legendgroup=s,
            marker=dict(size=9, color=COULEURS.get(s, COULEURS["non classé"]),
                        line=dict(color="white", width=0.8)),
            customdata=textes, hovertemplate="%{customdata}<extra></extra>"))

    # Contrôleurs : carrés. L'État en trace distincte, plus gros et plus sombre.
    for etat, nom_trace, couleur, taille in (
            (False, "contrôleur", "#57606a", 13), (True, "État", "#24292f", 17)):
        pts = [c for c in noeuds_ctrl if c["etat"] == etat]
        if not pts:
            continue
        fig.add_trace(go.Scatter(
            x=[c["x"] for c in pts], y=[c["y"] for c in pts], mode="markers",
            name=nom_trace, legendgroup="_controleurs",
            marker=dict(size=taille, color=couleur, symbol="square",
                        line=dict(color="white", width=0.8)),
            customdata=[f"<b>{c['nom']}</b><br>contrôleur<br>{c['n']} entités tenues"
                        for c in pts],
            hovertemplate="%{customdata}<extra></extra>"))

    # Étiquettes des contrôleurs, posées vers l'intérieur (comme la statique).
    for c in noeuds_ctrl:
        ang = math.atan2(c["y"], c["x"])
        lab_r = 1.0 - 0.16
        lx, ly = lab_r * math.cos(ang), lab_r * math.sin(ang)
        droite = math.cos(ang) >= 0
        fig.add_annotation(
            x=lx, y=ly, text=f"<b>{c['nom']}</b> ({c['n']})" if c["etat"]
            else f"{c['nom']} ({c['n']})",
            showarrow=False, xanchor="left" if droite else "right", yanchor="middle",
            font=dict(size=11 if c["etat"] else 9, color="#24292f"))

    lim = 2.7
    fig.update_layout(
        title=dict(text="La toile du contrôle public — survolez un point, cliquez un secteur "
                        "dans la légende pour le filtrer", font=dict(size=13), x=0.5),
        showlegend=True, legend=dict(title="secteur / rôle", font=dict(size=10),
                                     orientation="v", x=1.02, y=1),
        hovermode="closest", plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=10, r=10, t=50, b=10), height=760)
    fig.update_xaxes(visible=False, range=[-lim, lim])
    fig.update_yaxes(visible=False, range=[-lim, lim], scaleanchor="x", scaleratio=1)
    return fig


def fig_barres_controleurs():
    """Barres horizontales : nombre d'entités contrôlées par contrôleur."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    df = _lire()
    s = _entites_par_controleur(df)
    off = df.drop_duplicates("controleur").set_index("controleur")[
        "controleur_dans_liste_officielle"]
    couleurs = ["#0969da" if off.get(c) == "oui" else "#bc4c00" for c in s.index]
    fig, ax = plt.subplots(figsize=(9, 5.4))
    y = range(len(s))
    ax.barh(list(y), s.values, color=couleurs, zorder=2)
    ax.set_yticks(list(y))
    ax.set_yticklabels(s.index, fontsize=8.5)
    ax.invert_yaxis()
    for i, v in enumerate(s.values):
        ax.annotate(str(int(v)), xy=(v, i), xytext=(3, 0), textcoords="offset points",
                    va="center", fontsize=8)
    ax.set_xlabel(ft("Nombre d'entités contrôlées ou détenues"))
    ax.grid(axis="x", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(handles=[
        Line2D([], [], marker="s", ls="", ms=9, color="#0969da",
               label=ft("contrôleur de la liste officielle des entreprises publiques")),
        Line2D([], [], marker="s", ls="", ms=9, color="#bc4c00",
               label=ft("contrôleur hors liste (État, CDC, filiales…)")),
    ], loc="lower right", fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def fig_barres_secteurs():
    """Barres horizontales : entités contrôlées distinctes par secteur."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    s = _entites_par_secteur(_lire()).sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(9, 5.2))
    y = range(len(s))
    ax.barh(list(y), s.values, color=[COULEURS[k] for k in s.index], zorder=2)
    ax.set_yticks(list(y))
    ax.set_yticklabels([ft(k) for k in s.index], fontsize=8.5)
    for i, v in enumerate(s.values):
        ax.annotate(str(int(v)), xy=(v, i), xytext=(3, 0), textcoords="offset points",
                    va="center", fontsize=8)
    ax.set_xlabel(ft("Nombre d'entités contrôlées distinctes"))
    ax.grid(axis="x", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    fig.tight_layout()
    return fig


# --- émetteurs (chunks Quarto `output: asis`, étiquetés `fig-…`) ----------------------------

def graphe(caption: str, note_lecture: str | None = None) -> None:
    figtools.figure_tabs(fig_graphe(), table_relations(), CARTE,
                         slug="fig_ep_carte_graphe", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def graphe_interactif(caption: str, note_lecture: str | None = None) -> None:
    """La toile en onglets Graphique/Données/Sources, Graphique = Plotly en HTML.

    Même figure numérotée que `graphe` (même `slug`, même figdata sourcé) : le Graphique
    porte la toile interactive en HTML et, hors HTML (PDF), l'image statique matplotlib en
    repli. Les onglets Données et Sources sont identiques à ceux de la figure statique.
    """
    from itables import to_html_datatable

    slug = "fig_ep_carte_graphe"
    df_rel = table_relations()
    csv_path = Path("figdata") / f"{slug}.csv"
    figtools.write_figdata(df_rel, csv_path, CARTE, note=caption)

    # Graphique : Plotly (HTML) + repli PNG statique (hors HTML).
    html = fig_graphe_plotly().to_html(
        include_plotlyjs="cdn", full_html=False,
        config={"displayModeBar": True, "responsive": True, "locale": "fr"},
        div_id="fig-ep-carte-graphe-plotly")
    png_dir = Path("_fig")
    png_dir.mkdir(parents=True, exist_ok=True)
    png_path = png_dir / f"{slug}.png"
    mfig = fig_graphe()
    mfig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close(mfig)
    alt = caption.replace('"', "&quot;")
    graphique = (
        '::: {.content-visible when-format="html"}\n\n```{=html}\n'
        f'{html}\n```\n\n:::\n\n'
        '::: {.content-hidden when-format="html"}\n\n'
        f'![]({png_path}){{fig-alt="{alt}"}}\n\n:::')

    table = to_html_datatable(
        df_rel, buttons=["csvHtml5", "excelHtml5"], scrollY="420px", scrollX=True,
        scrollCollapse=True, paging=False, classes="display compact nowrap", connected=True)
    src = figtools.bloc_source(CARTE, nominal=False)
    dl = figtools.download_button(str(csv_path))
    details = figtools.source_details(CARTE)
    lecture = ""
    if note_lecture:
        lecture = (f'\n::: {{.callout-note appearance="simple" icon=true '
                   f'title="{figtools.t("how_to_read")}"}}\n{note_lecture}\n:::\n')
    print(
        f"::: {{.panel-tabset}}\n\n## {figtools.t('tab_graph')}\n\n{graphique}\n\n{src}\n"
        f"{lecture}\n## {figtools.t('tab_data')}\n\n{dl}\n\n{table}\n\n"
        f"## {figtools.t('tab_src')}\n\n::: {{.figure-sources-detail}}\n{details}\n:::\n\n:::\n\n"
        f"{caption}\n")
    plt.close("all")


def barres_controleurs(caption: str, note_lecture: str | None = None) -> None:
    figtools.figure_tabs(fig_barres_controleurs(), table_controleurs(), CARTE,
                         slug="fig_ep_carte_controleurs", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def repartition_secteurs(caption: str, note_lecture: str | None = None) -> None:
    figtools.figure_tabs(fig_barres_secteurs(), table_secteurs(), CARTE,
                         slug="fig_ep_carte_secteurs", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def totaux() -> None:
    """Imprime, en asis, le paragraphe des totaux de la carte, avec sa ligne de source."""
    c = comptes()
    source = f"Source : {', '.join('@' + k for k in _sources())}."
    print(
        f"**La carte de contrôle réunit {c['relations']} relations de contrôle ou de "
        f"participation : {c['controleurs']} entités en contrôlent ou en détiennent "
        f"{c['controlees']} autres, dont {c['controlees_hors_liste']} ne figurent pas dans la "
        f"liste officielle des entreprises publiques — c'est le périmètre réel, bien plus large "
        f"que la liste.** "
        + source
    )


if __name__ == "__main__":
    print(comptes())

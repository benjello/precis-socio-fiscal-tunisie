"""Deux exemples préparés après la réunion avec l'équipe SOEs : ce que le volume pourrait offrir, sans y figurer.

    uv run python scripts/exemples_reunion_soes.py

Écrit dans `docs/exemples-soes/` :
  tableau-de-bord-portefeuille.md / .csv / .png               le tableau de bord du portefeuille (pour le suivi des entreprises publiques)
  fiche-en-bref-steg.md / .png                                  une fiche opérationnelle par entreprise (ici la STEG)
Tout vient des relevés du volume (`figdata/fig_ep_*_fiches.csv`, `figdata/fig_ep_*_fiches.csv` seulement) : rien n'est saisi.
Les PDF sont produits par pandoc et Chromium (feuille de style `style.css`).
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

LIVRE = Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques"
SORTIE = Path(__file__).resolve().parent.parent / "docs/exemples-soes"
RESULTAT = {
    "Résultat net",
    "Produits d'exploitation",
    "Résultat d'exploitation",
    "Charges d'exploitation",
}
BILAN = {
    "Total des actifs",
    "Total des passifs, hors fonds propres",
    "Fonds propres",
    "Immobilisations nettes",
}
EDITIONS = {"LF 2022": 0, "LF 2024": 1, "LF 2025": 2}
EXERCICES = list(range(2018, 2024))


def fiches() -> dict[str, pd.DataFrame]:
    out = {}
    for chemin in sorted((LIVRE / "figdata").glob("fig_ep_*_fiches.csv")):
        sigle = re.match(r"fig_ep_(.+)_fiches\.csv", chemin.name).group(1)
        d = pd.read_csv(chemin, comment="#")
        d["rang"] = d["Édition"].map(EDITIONS)
        out[sigle] = d
    return out


def derniere_edition(d: pd.DataFrame, grandeur: str) -> pd.DataFrame:
    """Pour chaque exercice, la valeur de la dernière édition qui la donne."""
    g = d[(d["Grandeur"] == grandeur) & d["Valeur"].notna()].sort_values("rang")
    return g.groupby("Exercice").tail(1).set_index("Exercice")


def registre() -> dict[str, str]:
    with (LIVRE / "listes/entreprises-publiques-registre.csv").open(
        encoding="utf-8", newline=""
    ) as source:
        return {
            r["sigle"].lower().replace(" ", "-"): r["exercices_etats_financiers"]
            for r in csv.DictReader(source)
        }


def panel() -> pd.DataFrame:
    """Une ligne par entreprise et exercice : produits, résultat net, subvention d'exploitation, passifs (dernière édition qui les donne)."""
    lignes = []
    repli = {
        "Résultat net": ["Résultat net", "Résultat net avant modifications comptables"]
    }
    for sigle, d in fiches().items():
        for x in EXERCICES:
            ligne = {"entreprise": sigle.upper().replace("-", " "), "exercice": x}
            for cle, grandeur in (
                ("produits", "Produits d'exploitation"),
                ("resultat", "Résultat net"),
                ("subvention", "Subvention d'exploitation"),
                ("passifs", "Total des passifs, hors fonds propres"),
            ):
                serie = derniere_edition(d, repli.get(grandeur, [grandeur])[0])[
                    "Valeur"
                ]
                for autre in repli.get(grandeur, [])[1:]:
                    serie = serie.combine_first(derniere_edition(d, autre)["Valeur"])
                ligne[cle] = serie.get(x, np.nan)
            lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_de_bord() -> None:
    """Le portefeuille d'un coup d'œil : résultat net cumulé, bénéficiaires et déficitaires, subventions, et les dix plus grandes entreprises."""
    p = panel()
    fmt = lambda v, e=0: (
        "–"
        if pd.isna(v)
        else f"{v:,.{e}f}".replace(",", " ").replace(".", ",").replace("-", "−")
    )  # noqa: E731
    annuel = []
    for x in EXERCICES:
        c = p[(p["exercice"] == x) & p["resultat"].notna()]
        annuel.append(
            {
                "exercice": x,
                "n": len(c),
                "benef": c.loc[c["resultat"] > 0, "resultat"].sum(),
                "deficit": c.loc[c["resultat"] < 0, "resultat"].sum(),
                "nb_perte": int((c["resultat"] < 0).sum()),
                "net": c["resultat"].sum(),
                "subv": p.loc[p["exercice"] == x, "subvention"].sum(),
                "n_subv": int(p.loc[p["exercice"] == x, "subvention"].notna().sum()),
                "produits": p.loc[p["exercice"] == x, "produits"].sum(),
            }
        )
    a = pd.DataFrame(annuel).set_index("exercice")
    a.to_csv(SORTIE / "tableau-de-bord-portefeuille.csv", encoding="utf-8")
    dernier = 2022
    top = p[p["exercice"] == dernier].sort_values("produits", ascending=False).head(10)
    fig, (g1, g2, g3) = plt.subplots(1, 3, figsize=(10, 3.4))
    g1.bar(EXERCICES, a["benef"], color="#1a7f37", label="entreprises bénéficiaires")
    g1.bar(EXERCICES, a["deficit"], color="#cf222e", label="entreprises déficitaires")
    g1.plot(EXERCICES, a["net"], "k-o", ms=3, lw=1, label="résultat net cumulé")
    g1.axhline(0, color="#57606a", lw=0.8)
    g1.set_title("Résultat net des fiches (MD)", fontsize=8, loc="left")
    g1.legend(fontsize=6, frameon=False, loc="lower left")
    g2.plot(
        EXERCICES,
        a["subv"],
        "-o",
        color="#0969da",
        ms=3,
        label="subvention d'exploitation",
    )
    g2.plot(
        EXERCICES,
        a["produits"],
        "-o",
        color="#8250df",
        ms=3,
        label="produits d'exploitation",
    )
    g2.set_title("Subventions et produits (MD)", fontsize=8, loc="left")
    g2.legend(fontsize=6, frameon=False)
    g3.barh(
        top["entreprise"][::-1],
        top["resultat"][::-1],
        color=["#1a7f37" if v > 0 else "#cf222e" for v in top["resultat"][::-1]],
    )
    g3.axvline(0, color="#57606a", lw=0.8)
    g3.set_title(
        f"Résultat net {dernier}, dix plus gros produits (MD)", fontsize=8, loc="left"
    )
    for ax in (g1, g2, g3):
        ax.tick_params(labelsize=7)
        ax.grid(axis="y" if ax is not g3 else "x", color="#d0d7de", lw=0.5)
        for cote in ("top", "right"):
            ax.spines[cote].set_visible(False)
    for ax in (g1, g2):
        ax.set_xticks(EXERCICES)
    fig.tight_layout()
    fig.savefig(SORTIE / "tableau-de-bord-portefeuille.png", dpi=170)
    plt.close(fig)
    nb = len(fiches())
    t = [
        "# Tableau de bord du portefeuille des entreprises publiques, 2018-2023",
        "",
        f"*Exemple préparé après la réunion du 3 novembre 2026 ; il n'est pas dans le volume. Il est engendré par `scripts/exemples_reunion_soes.py` à partir des {nb} fiches d'entreprises du rapport du ministère des Finances annexé aux projets de loi de finances (éditions LF 2022, LF 2024 et LF 2025 : chaque exercice est lu dans la dernière édition qui le donne). Rien n'est saisi à la main.*",
        "",
        "## En un coup d'œil",
        "",
        "![](tableau-de-bord-portefeuille.png){ width=100% }",
        "",
        "| Exercice | " + " | ".join(str(x) for x in EXERCICES) + " |",
        "|---|" + "---|" * len(EXERCICES),
        "| Entreprises avec résultat net | "
        + " | ".join(fmt(a.loc[x, "n"]) for x in EXERCICES)
        + " |",
        "| dont en perte | "
        + " | ".join(fmt(a.loc[x, "nb_perte"]) for x in EXERCICES)
        + " |",
        "| Résultat net cumulé (MD) | "
        + " | ".join(fmt(a.loc[x, "net"]) for x in EXERCICES)
        + " |",
        "| Bénéfices cumulés (MD) | "
        + " | ".join(fmt(a.loc[x, "benef"]) for x in EXERCICES)
        + " |",
        "| Pertes cumulées (MD) | "
        + " | ".join(fmt(a.loc[x, "deficit"]) for x in EXERCICES)
        + " |",
        "| Subvention d'exploitation (MD) | "
        + " | ".join(fmt(a.loc[x, "subv"]) for x in EXERCICES)
        + " |",
        "| Entreprises avec subvention renseignée | "
        + " | ".join(fmt(a.loc[x, "n_subv"]) for x in EXERCICES)
        + " |",
        "| Produits d'exploitation (MD) | "
        + " | ".join(fmt(a.loc[x, "produits"]) for x in EXERCICES)
        + " |",
        "",
        f"## Zoom : les dix plus grandes entreprises par produits d'exploitation en {dernier}",
        "",
        "| Entreprise | Produits d'exploitation (MD) | Résultat net (MD) | Subvention d'exploitation (MD) | Total des passifs hors fonds propres (MD) |",
        "|---|---|---|---|---|",
    ]
    for _, r in top.iterrows():
        t.append(
            f"| {r['entreprise']} | {fmt(r['produits'])} | {fmt(r['resultat'])} | {fmt(r['subvention'])} | {fmt(r['passifs'])} |"
        )
    t += [""] + bloc_etat() + bloc_cotees()
    t += [
        "## Comment le lire",
        "",
        "- Les totaux additionnent les entreprises dont la fiche donne la grandeur cet exercice-là : le nombre d'entreprises est en tête de chaque colonne, parce qu'il change d'un exercice à l'autre (les éditions successives n'ont pas le même périmètre).",
        "- Un total est une somme de chiffres que chaque entreprise publie dans son périmètre, non un résultat consolidé de l'État : des échanges entre entreprises (transferts, créances croisées) peuvent s'y compter deux fois.",
        "- La subvention d'exploitation est une ligne comptable de l'entreprise ; elle ne se confond pas avec les transferts du budget.",
        "- Les derniers exercices de chaque édition sont souvent provisoires.",
        "- Aucune projection : ce sont les chiffres imprimés dans les rapports, avec leur édition.",
    ]
    (SORTIE / "tableau-de-bord-portefeuille.md").write_text(
        "\n".join(t) + "\n", encoding="utf-8"
    )


def fiche(sigle: str, titre: str, identite: dict[str, str]) -> None:
    d = fiches()[sigle]

    repli = {
        "Résultat net": ["Résultat net", "Résultat net avant modifications comptables"],
        "Fonds propres": ["Fonds propres", "Fonds propres avant affectation"],
    }

    def serie(g):
        base = derniere_edition(d, repli.get(g, [g])[0])["Valeur"]
        for autre in repli.get(g, [])[1:]:
            base = base.combine_first(derniere_edition(d, autre)["Valeur"])
        return base

    grandeurs = [
        "Produits d'exploitation",
        "Résultat net",
        "Subvention d'exploitation",
        "Fonds propres",
        "Dette totale",
        "dont État",
        "Effectif (agents)",
    ]
    tab = pd.DataFrame({g: serie(g) for g in grandeurs}).reindex(EXERCICES)
    editions = derniere_edition(d, "Produits d'exploitation")["Édition"].reindex(
        EXERCICES
    )
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.4, 2.9))
    a.bar(
        [x - 0.2 for x in EXERCICES],
        tab["Résultat net"],
        0.4,
        color="#cf222e",
        label="Résultat net",
    )
    a.bar(
        [x + 0.2 for x in EXERCICES],
        tab["Subvention d'exploitation"],
        0.4,
        color="#0969da",
        label="Subvention d'exploitation",
    )
    a.axhline(0, color="#57606a", lw=0.8)
    a.set_title(
        "Résultat net et subvention d'exploitation (MD)", fontsize=8, loc="left"
    )
    a.legend(fontsize=6.5, frameon=False)
    b.plot(
        EXERCICES,
        tab["Dette totale"],
        "-o",
        color="#8250df",
        ms=3,
        label="Dette totale",
    )
    b.plot(
        EXERCICES,
        tab["Fonds propres"],
        "-o",
        color="#1a7f37",
        ms=3,
        label="Fonds propres",
    )
    b.plot(
        EXERCICES,
        tab["dont État"],
        "-o",
        color="#bf8700",
        ms=3,
        label="dont dette envers l'État",
    )
    b.axhline(0, color="#57606a", lw=0.8)
    b.set_title("Dette et fonds propres (MD)", fontsize=8, loc="left")
    b.legend(fontsize=6.5, frameon=False)
    for axe in (a, b):
        axe.set_xticks(EXERCICES)
        axe.tick_params(labelsize=7)
        axe.grid(axis="y", color="#d0d7de", lw=0.5)
        for cote in ("top", "right"):
            axe.spines[cote].set_visible(False)
    fig.tight_layout()
    fig.savefig(SORTIE / f"fiche-en-bref-{sigle}.png", dpi=170)
    plt.close(fig)
    fmt = lambda v, e=1: (
        "–"
        if pd.isna(v)
        else f"{v:,.{e}f}".replace(",", " ").replace(".", ",").replace("-", "−")
    )
    lignes = (
        [
            f"# {titre} : fiche en bref",
            "",
            "*Exemple préparé après la réunion du 3 novembre 2026 ; il n'est pas dans le volume. Les chiffres viennent des fiches du rapport du ministère des Finances (dernière édition qui donne chaque exercice) ; l'identité, du Registre national des entreprises.*",
            "",
            "## Identité",
            "",
        ]
        + [f"- **{k}** : {v}" for k, v in identite.items()]
        + [
            "",
            "## Les chiffres, 2018-2023 (millions de dinars courants)",
            "",
            "| Exercice | " + " | ".join(str(x) for x in EXERCICES) + " |",
            "|---|" + "---|" * len(EXERCICES),
        ]
    )
    for g, e in [
        ("Produits d'exploitation", 1),
        ("Résultat net", 1),
        ("Subvention d'exploitation", 1),
        ("Fonds propres", 1),
        ("Dette totale", 1),
        ("dont État", 1),
        ("Effectif (agents)", 0),
    ]:
        nom = {
            "dont État": "dont dette envers l'État",
            "Total des passifs, hors fonds propres": "Total des passifs hors fonds propres",
        }.get(g, g)
        lignes.append(
            f"| {nom} | " + " | ".join(fmt(tab.loc[x, g], e) for x in EXERCICES) + " |"
        )
    lignes.append(
        "| Édition du ministère | "
        + " | ".join(str(editions.get(x, "–")) for x in EXERCICES)
        + " |"
    )
    ratio = tab["Subvention d'exploitation"] / tab["Produits d'exploitation"] * 100
    vides = {
        g: [str(x) for x in EXERCICES if pd.isna(tab.loc[x, g])] for g in tab.columns
    }
    manquants = []
    par_annees: dict[tuple[str, ...], list[str]] = {}
    for g, v in vides.items():
        if v:
            par_annees.setdefault(tuple(v), []).append(g)
    for annees, noms in par_annees.items():
        editions_ok = sorted(
            {
                e
                for g in noms
                for e in d[(d["Grandeur"] == g) & d["Valeur"].notna()][
                    "Édition"
                ].unique()
            }
        )
        autres = d[
            ~d["Édition"].isin(editions_ok)
            & d["Valeur"].notna()
            & d["Grandeur"].str.contains("emprunts|dette", case=False)
        ]
        ailleurs = ""
        if not autres.empty:
            quoi = sorted(autres["Grandeur"].unique())
            ailleurs = (
                " Les autres éditions impriment d'autres lignes sous un autre code ("
                + ", ".join(quoi)
                + ") : elles ne se raccordent pas et ne sont pas additionnées ici."
            )
        manquants.append(
            f"- **« – » pour {' et '.join(noms)}, exercices {', '.join(annees)}** : "
            f"la grandeur n'est imprimée que dans l'édition {', '.join(editions_ok) or 'aucune'}.{ailleurs}"
        )
    lignes += [
        "",
        "![](fiche-en-bref-" + sigle + ".png){ width=95% }",
        "",
        "## Lectures",
        "",
        "- **Subvention d'exploitation rapportée aux produits d'exploitation** : "
        + ", ".join(
            f"{x} : {fmt(ratio[x], 1)} %" for x in EXERCICES if not pd.isna(ratio[x])
        )
        + " (calcul du script, non imprimé dans le rapport).",
        f"- **Fonds propres** de {fmt(tab['Fonds propres'].dropna().iloc[0])} MD en {tab['Fonds propres'].dropna().index[0]} à {fmt(tab['Fonds propres'].dropna().iloc[-1])} MD en {tab['Fonds propres'].dropna().index[-1]}.",
        f"- **Dette totale** de {fmt(tab['Dette totale'].dropna().iloc[0])} MD en {tab['Dette totale'].dropna().index[0]} à {fmt(tab['Dette totale'].dropna().iloc[-1])} MD en {tab['Dette totale'].dropna().index[-1]}, dont {fmt(tab['dont État'].dropna().iloc[-1])} MD envers l'État en {tab['dont État'].dropna().index[-1]}.",
        "",
        "## Limites",
        "",
        "- Les éditions ne se raccordent pas : un exercice est lu dans la dernière édition qui le donne ; l'édition est indiquée sous chaque colonne.",
        "- Les derniers exercices de chaque édition sont souvent provisoires ; le statut est dans les séries du volume.",
        "- La subvention d'exploitation est une ligne comptable de l'entreprise : elle ne se confond pas avec les transferts du budget.",
        *manquants,
    ]
    (SORTIE / f"fiche-en-bref-{sigle}.md").write_text(
        "\n".join(lignes) + "\n", encoding="utf-8"
    )


def bloc_etat() -> list[str]:
    """La relation financière avec l'État, 2016-2024 : transferts, dette garantie, créances et dettes croisées, part dans les bénéfices."""
    with (LIVRE / "figdata/fig_ep_ensemble.csv").open(
        encoding="utf-8", newline=""
    ) as f:
        d = pd.read_csv(f, comment="#")
    d.columns = [
        "grandeur",
        "annee",
        "md",
        "etat",
        "edition",
        "pct_depenses",
        "pct_pib",
        "base",
    ]
    d = d[d["annee"].astype(str).str.fullmatch(r"\d{4}")].copy()
    d["annee"] = d["annee"].astype(int)
    series = {
        "Transferts du budget": "#0969da",
        "Encours de la dette garantie": "#bc4c00",
        "Créances des entreprises sur l'État": "#1a7f37",
        "Dettes des entreprises envers l'État": "#8250df",
    }
    fig, ax = plt.subplots(figsize=(9, 4))
    for nom, couleur in series.items():
        x = d[d["grandeur"] == nom]
        ax.plot(x["annee"], x["md"] / 1000, marker="o", color=couleur, label=nom)
    ax.set_ylabel("milliards de dinars courants")
    ax.set_title(
        "Relation financière entre l'État et les entreprises publiques, 2016-2024",
        fontsize=10,
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    fig.savefig(SORTIE / "tableau-de-bord-etat.png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    annees = sorted(d["annee"].unique())
    lignes = [
        "## La relation financière avec l'État",
        "",
        "Quatre grandeurs que le précis reprend du rapport du ministère des Finances et des lois de finances, en milliards de dinars courants.",
        "",
        "![](tableau-de-bord-etat.png){ width=95% }",
        "",
        "| Grandeur | " + " | ".join(str(a) for a in annees) + " |",
        "|---|" + "---|" * len(annees),
    ]
    for nom in [*series, "Part de l'État dans les bénéfices"]:
        x = d[d["grandeur"] == nom].set_index("annee")
        unite = 1 if nom.startswith("Part") else 1000
        lignes.append(
            f"| {nom}{' (MD)' if unite == 1 else ''} | "
            + " | ".join(
                f"{x.loc[a, 'md'] / unite:,.1f}".replace(",", " ").replace(".", ",")
                if a in x.index
                else "–"
                for a in annees
            )
            + " |"
        )
    pib = d[d["grandeur"] == "Transferts du budget"].set_index("annee")["pct_pib"]
    lignes += [
        "",
        f"Les transferts du budget font {str(pib.loc[2017]).replace('.', ',')} % du PIB en 2017 et {str(pib.loc[2023]).replace('.', ',')} % en 2023 ; "
        "ce total contient les caisses de sécurité sociale, la compensation et les établissements d'enseignement : il n'est pas le coût des entreprises publiques. "
        "Les créances et les dettes croisées ne sont données que depuis 2021. 2024 : loi de finances pour les transferts ; l'encours de la dette garantie n'est estimé qu'à fin juin 2024 (21,5 milliards) et n'est pas repris ici.",
        "",
    ]
    return lignes


def _liste(nom: str) -> list[dict[str, str]]:
    with (LIVRE / "listes" / f"{nom}.csv").open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _md(valeur: str | float, decimales: int = 1) -> str:
    """Dinars en millions de dinars, à la française ; « – » si le relevé est vide."""
    if valeur in ("", None):
        return "–"
    return (
        f"{float(valeur) / 1e6:,.{decimales}f}".replace(",", " ")
        .replace(".", ",")
        .replace("-", "−")
    )


def bloc_cotees() -> list[str]:
    """Les sociétés cotées où l'État est actionnaire direct : sa part, le dernier résultat net, son dividende."""
    etat = {
        r["societe"]: r
        for r in _liste("societes-cotees-participations")
        if r["detenteur"] == "État"
    }
    derniers: dict[str, dict[str, str]] = {}
    for r in _liste("societes-cotees-resultats"):
        if r["resultat_net_dt"] and (
            r["societe"] not in derniers
            or r["exercice"] > derniers[r["societe"]]["exercice"]
        ):
            derniers[r["societe"]] = r
    lignes = [
        "## Les sociétés cotées où l'État est actionnaire direct",
        "",
        "D'après les pages de la Bourse de Tunis (actionnaires, résultat net et dividende de l'assemblée la plus récente).",
        "",
        "| Société | Part de l'État (%) | Dernier exercice | Résultat net (MD) | Dividende revenant à l'État (MD) |",
        "|---|---|---|---|---|",
    ]
    for societe, r in sorted(etat.items(), key=lambda kv: -float(kv[1]["part_pct"])):
        d = derniers.get(societe)
        lignes.append(
            f"| {societe} | {r['part_pct'].replace('.', ',')} | {d['exercice'] if d else '–'} | "
            f"{_md(d['resultat_net_dt']) if d else '–'} | {_md(d['dividende_etat_dt']) if d else '–'} |"
        )
    lignes += [
        "",
        "Les sociétés dont la page ne donne pas de résultat net ou de dividende sont marquées « – ». "
        "Les actionnaires de moins de 5 % ne sont pas nommés par la Bourse.",
        "",
    ]
    return lignes


def fiche_cotee(sigle: str, titre: str, groupe: str) -> None:
    """Fiche « en bref » d'une société cotée : actionnaires, capital, résultats, périmètre, commissaires aux comptes, délai."""
    nom = sigle.upper()
    parts = [
        r
        for r in _liste("societes-cotees-participations")
        if r["societe"].upper() == nom
    ]
    capital = [r for r in _liste("societes-cotees-capital") if r["banque"] == nom]
    resultats = sorted(
        (r for r in _liste("societes-cotees-resultats") if r["societe"] == nom),
        key=lambda r: r["exercice"],
    )
    perimetre = [
        r
        for r in _liste("groupes-bancaires-perimetre")
        if r["groupe"] == nom and r["methode"] != "mère"
    ]
    opinions = [r for r in _liste("opinions-cac") if r["groupe"] == nom]
    delais = [
        r
        for r in _liste("delais-publication")
        if r["societe"] == sigle and r["nature"] == "individuel"
    ]
    entites: dict[str, int] = {}
    for r in perimetre:
        entites[r["exercice"]] = entites.get(r["exercice"], 0) + 1
    motifs: dict[str, int] = {}
    for r in opinions:
        motifs[r["exercice"]] = motifs.get(r["exercice"], 0) + 1
    lignes = [
        f"# {titre} : en bref",
        "",
        "Fiche produite par un script à partir des relevés du volume ; elle n'est pas dans le volume.",
        "",
        "## Actionnaires et capital",
        "",
        "| Détenteur | Part du capital (%) |",
        "|---|---|",
        *[f"| {r['detenteur']} | {r['part_pct'].replace('.', ',')} |" for r in parts],
        "",
        f"Capital : {_md(capital[-1]['capital_dt'], 3)} MD depuis le {capital[-1]['date']} "
        f"({len(capital)} opérations relevées depuis {capital[0]['date'][:4]}).",
        "",
        "## Résultat net et dividende",
        "",
        "| Exercice | Résultat net (MD) | Dividende par action (DT) | Dividende revenant à l'État (MD) |",
        "|---|---|---|---|",
        *[
            f"| {r['exercice']} | {_md(r['resultat_net_dt'])} | {r['dividende_par_action_dt'].replace('.', ',') or '–'} | {_md(r['dividende_etat_dt'])} |"
            for r in resultats
        ],
        "",
        "## Le groupe : entités consolidées",
        "",
        "| Exercice | " + " | ".join(sorted(entites)) + " |",
        "|---|" + "---|" * len(entites),
        "| Entités, mère non comprise | "
        + " | ".join(str(entites[x]) for x in sorted(entites))
        + " |",
        "",
        "## Opinion des commissaires aux comptes",
        "",
        f"Opinion avec réserves dans les {len(motifs)} exercices lus ({min(motifs)} à {max(motifs)}). Le délai de publication se compte en jours après le 31 décembre.",
        "",
        "| Exercice | " + " | ".join(sorted(motifs)) + " |",
        "|---|" + "---|" * len(motifs),
        "| Motifs de réserve | "
        + " | ".join(str(motifs[x]) for x in sorted(motifs))
        + " |",
        "| Délai de publication (jours) | "
        + " | ".join(
            next((r["jours"] for r in delais if r["exercice"] == x), "–")
            for x in sorted(motifs)
        )
        + " |",
        "",
        f"![](fiche-en-bref-{sigle}.png){{ width=72% }}",
        "",
        "## Limites",
        "",
        "- Les actionnaires de moins de 5 % ne sont pas nommés par la Bourse.",
        "- Le périmètre est celui que la banque imprime ; un exercice absent du relevé n'est pas comblé.",
        "- Le thème d'un motif est un classement du relevé, non un jugement du rapport.",
        "- Les sources de chaque chiffre sont dans le volume (section de la banque, partie III).",
    ]
    (SORTIE / f"fiche-en-bref-{sigle}.md").write_text(
        "\n".join(lignes) + "\n", encoding="utf-8"
    )
    import sys

    sys.path.insert(0, str(LIVRE))
    from figures import cotees as ct

    fig = ct.fig_cac(nom, sigle)
    fig.savefig(SORTIE / f"fiche-en-bref-{sigle}.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


PREMIER_JET = "**Premier jet : toute suggestion est la bienvenue.**"


def marquer_premier_jet(nom: str) -> None:
    """Ajoute la mention « premier jet » sous le titre du document, une seule fois."""
    chemin = SORTIE / f"{nom}.md"
    lignes = chemin.read_text(encoding="utf-8").split("\n")
    if PREMIER_JET in lignes:
        return
    i = next(k for k, l in enumerate(lignes) if l.startswith("# "))
    chemin.write_text(
        "\n".join([*lignes[: i + 1], "", PREMIER_JET, *lignes[i + 1 :]]),
        encoding="utf-8",
    )


def pdf(nom: str) -> None:
    """Markdown -> HTML (pandoc, feuille `style.css`) -> PDF (Chromium sans interface)."""
    import subprocess

    html = SORTIE / f".{nom}.html"
    subprocess.run(
        [
            "pandoc",
            f"{nom}.md",
            "-s",
            "--metadata",
            "title= ",
            "--metadata",
            f"pagetitle={nom}",
            "-c",
            "style.css",
            "--embed-resources",
            "-o",
            html.name,
        ],
        cwd=SORTIE,
        check=True,
    )
    subprocess.run(
        [
            "chromium-browser",
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={SORTIE / (nom + '.pdf')}",
            f"file://{html}",
        ],
        check=True,
        capture_output=True,
    )
    html.unlink()


def main() -> int:
    SORTIE.mkdir(parents=True, exist_ok=True)
    tableau_de_bord()
    fiche(
        "steg",
        "Société tunisienne de l'électricité et du gaz (STEG)",
        {
            "Forme au Registre": "établissement public, actif",
            "Identifiant du Registre": "0005910D",
            "États financiers déposés au Registre": "2024 (6 documents listés)",
        },
    )
    fiche_cotee("stb", "Société tunisienne de banque (STB)", "STB")
    for nom in (
        "tableau-de-bord-portefeuille",
        "fiche-en-bref-steg",
        "fiche-en-bref-stb",
    ):
        marquer_premier_jet(nom)
        pdf(nom)
    print("écrit dans", SORTIE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Tableau et figure du chapitre « Les sociétés cotées » (volume « Les entreprises publiques »).

    from figures import cotees as ct
    ct.tableau_participations(caption=…)          # qui détient quoi, détenteur par détenteur
    ct.figure_resultats(caption=…, note_lecture=…)  # résultat net et dividende de l'État
    ct.tableau_resultats(caption=…)               # résultat net et dividendes des sociétés où l'État est actionnaire
    ct.tableau_perimetres(caption=…)              # les entités consolidées par la STB, la BH et la BNA
    ct.tableau_registre(caption=…)                # l'identité des entreprises publiques au Registre national (annexe)
    ct.figure_capital(caption=…, note_lecture=…)  # le capital de la STB, de la BH et de la BNA

D'OÙ VIENNENT LES DONNÉES. Des relevés versionnés DANS le livre (`listes/*.csv`, chacun avec son manifeste `.csv.yml`) :
`societes-cotees-*.csv`, engendrés par `scripts/bvmt_societes_cotees.py livre` à partir des pages
publiques de la Bourse de Tunis, et `entreprises-publiques-registre.csv`, engendré par
`scripts/rne_registre_releve.py` à partir du portail public du Registre national des entreprises.
Rien n'est lu de l'entrepôt `tunisia-data` à la construction.

RÈGLES.

  - **Les détenteurs publics sont une liste fermée** (voir le script) : un nom n'est pas tenu
    pour public d'après sa seule apparence.
  - **La Bourse ne nomme que les actionnaires de plus de 5 %** : un détenteur public sous ce
    seuil est absent du tableau, et les parts du tableau ne s'additionnent pas à 100 %.
  - **La figure trace ce que la page imprime** : une ligne dont le capital est inférieur à celui
    de la ligne précédente n'est pas tracée.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

RELEVES = Path(__file__).resolve().parent.parent / "listes"
PARTICIPATIONS = "societes-cotees-participations"
CAPITAL = "societes-cotees-capital"
RESULTATS = "societes-cotees-resultats"
REGISTRE = "entreprises-publiques-registre"
PERIMETRE = "groupes-bancaires-perimetre"
ENGAGEMENTS_BNA = "bna-engagements-entreprises-publiques"
# Un nom d'entité change d'un rapport à l'autre (« S.T.C VERITAS » et « S.T.C.V VERITAS ») : la clé les réunit.
ALIAS_ENTITES = {"STCVERITAS": "STCVVERITAS", "GENERALEDESVENTES": "GENERALEDEVENTE", "ELMEDINA": "SPIMADINA", "ZIED": "ZIEDSARL",
                 "TIS": "TUNISIEINFORMATIQUESERVICES", "TUNISIENNEDEREASSURANCE": "TUNISRE", "TUNISIERE": "TUNISRE", "SICAFPARTICIPATIONSBNA": "SICAFPARTICIPATIONS", "SPBSICAFPARTICIPATIONS": "SICAFPARTICIPATIONS",
                 # BH : noms d'avant 2019 (rapport de 2017) rapprochés des noms d'après ; BH Bank, BH Assurances et la SICAV BH-Capitalisation sont attestés par un acte ou par les rapports, Modern Leasing par un projet de résolutions, les suivants par les pourcentages d'intérêt (voir le commentaire TODO de la section de la BH)
                 "BANQUEDELHABITAT": "BHBANK", "ASSURANCESALIM": "BHASSURANCES", "MODERNLEASING": "BHLEASING", "SICAVBHPLACEMENT": "SICAVBHCAPITALISATION",
                 "SICAVBHOBLIGATOIRE": "SICAVBHOBLIGATAIRE", "SICAFBHEPARGNEINVESTISSEMENT": "BHSICAF", "GENERALRECOUVREMENT": "BHRECOUVREMENT", "SIMSICAR": "BHEQUITY",
                 "SOPIVEL": "BHIMMO", "STIMEC": "BHPRINT"}
# Tunisair : « SEVENAIR » (2009) est rapproché de « TUNISAIR EXPRESS » (2010 à 2022) par le pourcentage (88,73 %) et l'activité ; TUNINTER (2006, 83,37 %) reste à part
ALIAS_ENTITES.update({"SEVENAIR": "TUNISAIREXPRESS"})
RAPPORTS = {"STB": "bvmt-ra-stb-2021", "BH": "bvmt-ra-bh-2021", "BNA": "bvmt-ra-bna-2021"}
PAGES_RAPPORT = {"STB": "p. 96-97", "BH": "p. 240", "BNA": "p. 127"}
COULEURS = {"STB": "#0969da", "BH": "#bc4c00", "BNA": "#1a7f37"}


def _lire(nom: str) -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{nom}.csv", dtype=str, keep_default_na=False)


def _sources(nom: str) -> list[str]:
    import yaml
    manifeste = yaml.safe_load((RELEVES / f"{nom}.csv.yml").read_text(encoding="utf-8"))
    return list(manifeste["sources"])


figtools.register_provenance(
    CAPITAL, titre="Capital de la STB, de la BH et de la BNA, depuis leur constitution",
    sources=_sources(CAPITAL), unite="dinars courants",
    perimetre=("historique du capital imprimé sur la page de chaque banque à la Bourse de "
               "Tunis : date de la décision de l'assemblée, nature de l'opération, "
               "augmentation et capital après l'opération"),
    caveats=("La page imprime ses chiffres tels quels : une ligne de la BH (6 juin 1995) donne "
             "un capital inférieur à celui de la ligne précédente et n'est pas tracée. Les "
             "dates sont celles de l'assemblée, non de la libération du capital."))


figtools.register_provenance(
    RESULTATS, titre="Résultat net et dividende des sociétés cotées où l'État est actionnaire",
    sources=_sources(RESULTATS), unite="millions de dinars courants",
    perimetre=("encadré « Indicateurs et ratios clés » de la page de chaque société à la Bourse de "
               "Tunis : résultat net (part du groupe pour les sociétés qui publient des comptes "
               "consolidés) et dividende par action, exercices 2022 à 2025 quand la page les donne"),
    caveats=("Le dividende revenant à l'État est CALCULÉ : dividende par action de l'exercice N, "
             "multiplié par les actions de l'État à l'assemblée de l'année N+1 ; il n'est calculé "
             "que dans ce cas et n'est pas une recette du budget. Une case vide est une valeur "
             "que la page n'imprime pas, non un zéro."))


figtools.register_provenance(
    PERIMETRE, titre="Périmètre de consolidation de la STB, de la BH et de la BNA",
    sources=_sources(PERIMETRE), unite="% d'intérêt",
    perimetre=("entités consolidées par chaque banque, exercice par exercice, d'après les rapports annuels "
               "(Bourse de Tunis, Internet Archive) : méthode, pourcentage de contrôle et d'intérêt"),
    caveats=("Le pourcentage d'intérêt est la part du capital détenue directement et indirectement par le groupe, "
             "non la part directe de la banque. Un exercice sans rapport lu (2019 pour la STB) n'a pas de colonne. "
             "La méthode n'est pas donnée pour 2020 et 2021 (STB)."))


figtools.register_provenance(
    "opinions-cac", titre="Opinion des commissaires aux comptes et motifs de réserve",
    sources=_sources("opinions-cac"), unite="motifs",
    perimetre=("rapport général des commissaires aux comptes de chaque rapport annuel lu : opinion et motifs de réserve, "
               "rangés par thème ; délai de publication d'après la date que la Bourse de Tunis porte à la publication"),
    caveats=("Le thème d'un motif est un classement fixé dans le relevé (colonne themes), non un jugement du rapport ; "
             "un exercice sans rapport lu n'a pas de case. Le délai de publication est celui de la mise en ligne sur la "
             "Bourse, non celui de l'assemblée."))


figtools.register_provenance(
    ENGAGEMENTS_BNA, titre="Engagements de la BNA envers les entreprises publiques",
    sources=_sources(ENGAGEMENTS_BNA), unite="milliers de dinars",
    perimetre=("tableau de la note « Engagements des entreprises publiques » des états financiers individuels de la BNA, "
               "2016 à 2024 : engagements, garanties de l'État, autres garanties, agios réservés et provisions, pour le total "
               "des entreprises publiques et pour l'Office des céréales et quelques entités nommées"),
    caveats=("Les entités nommées changent d'un exercice à l'autre (STIR et Tunisair jusqu'en 2020, puis ETAP, OCT et Transtu) : "
             "l'ensemble « autres entités nommées » n'est pas constant. Une somme n'est pas un total consolidé de l'État. "
             "Chaque exercice vient de l'état de cet exercice ; 2016, qui vient de l'état de 2017, ne donne que les engagements."))


def _md(entete: list[str], lignes: list[list[str]], caption: str, tbl_id: str, gauche: tuple[int, ...] = ()) -> None:
    out = ["| " + " | ".join(entete) + " |",
           "|---|" + "|".join("---" if i + 1 in gauche else ":-:" for i in range(len(entete) - 1)) + "|"]
    out += ["| " + " | ".join(ligne) + " |" for ligne in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def _pct(valeur: str) -> str:
    return valeur.replace(".", ",")


def tableau_participations(caption: str, tbl_id: str = "tbl-ep-cotees-participations") -> None:
    """Une ligne par participation, regroupées par détenteur ; le détenteur n'est écrit qu'une fois."""
    d = _lire(PARTICIPATIONS)
    lignes, precedent = [], None
    for _, r in d.iterrows():
        detenteur = f"**{r['detenteur']}**" if r["detenteur"] != precedent else ""
        precedent = r["detenteur"]
        lignes.append([detenteur, r["societe"], _pct(r["part_pct"]), r["assemblee"],
                       f"[@bvmt-{r['page']}]"])
    _md(["Détenteur", "Société cotée", "Part du capital (%)", "Assemblée", "Source"],
        lignes, caption, tbl_id)


def _md_dt(valeur: str, mille: float = 1e6, chiffres: int = 1) -> str:
    """Dinars → millions de dinars, virgule décimale ; vide si le relevé est vide."""
    if valeur == "":
        return "–"
    return f"{float(valeur) / mille:,.{chiffres}f}".replace(",", " ").replace(".", ",")


def tableau_resultats(caption: str, tbl_id: str = "tbl-ep-cotees-resultats") -> None:
    """Résultat net et dividende par action par exercice, et dividende revenant à l'État."""
    d = _lire(RESULTATS)
    lignes = []
    precedent = None
    for _, r in d.iterrows():
        societe = f"**{r['societe']}**" if r["societe"] != precedent else ""
        precedent = r["societe"]
        dividende = r["dividende_par_action_dt"].replace(".", ",") or "–"
        lignes.append([societe, r["exercice"], _md_dt(r["resultat_net_dt"]), dividende,
                       _md_dt(r["dividende_etat_dt"]), f"[@bvmt-{r['page']}]"])
    _md(["Société", "Exercice", "Résultat net (MD)", "Dividende par action (D)",
         "Dividende revenant à l'État (MD)", "Source"], lignes, caption, tbl_id)


def tableau_perimetres(caption: str, tbl_id: str = "tbl-ep-cotees-perimetres") -> None:
    """Les entités consolidées par la STB, la BH et la BNA : méthode, contrôle, intérêt."""
    d = _lire(PERIMETRE)
    d = d[(d["exercice"] == "2021") & d["groupe"].isin(PAGES_RAPPORT)]  # les banques seules : les autres groupes ont leur propre section
    lignes, precedent = [], None
    for _, r in d.iterrows():
        groupe = f"**{r['groupe']}**" if r["groupe"] != precedent else ""
        precedent = r["groupe"]
        controle = _pct(r["controle_pct"]) if r["controle_pct"] else "–"
        lignes.append([groupe, r["entite"], r["methode"] or "–", controle, _pct(r["interet_pct"]),
                       f"[@{r['source']}, {PAGES_RAPPORT[r['groupe']]}]"])
    _md(["Groupe", "Entité consolidée", "Méthode", "Contrôle (%)", "Intérêt (%)", "Source"],
        lignes, caption, tbl_id)


def _cle_entite(nom: str) -> str:
    """Clé de rapprochement d'un nom d'entité d'un rapport à l'autre : le texte entre guillemets quand il y en a,
    sans « Société »/« STE » initial, sans parenthèses, en majuscules sans accents ni ponctuation."""
    import re
    import unicodedata
    nom = re.sub(r"\(.*?\)|\b[Ee][Xx]\b.*", "", nom)
    guillemets = re.search(r"\u00ab\s*(.+?)\s*\u00bb|[\"\u201c]\s*(.+?)\s*[\"\u201d]", nom)
    texte = (guillemets.group(1) or guillemets.group(2)) if guillemets else nom
    brut = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().upper()
    if not guillemets:
        brut = re.sub(r"^(SOCIETE|STE)\s+", "", brut.strip())
    cle = re.sub(r"[^A-Z0-9]", "", brut)
    return ALIAS_ENTITES.get(cle, cle)


def tableau_evolution(groupe: str, caption: str, tbl_id: str) -> None:
    """Les entités d'un groupe, exercice par exercice : pourcentage d'intérêt (à défaut de contrôle),
    « (ME) » pour la mise en équivalence, « – » quand l'entité n'est pas consolidée cet exercice-là."""
    d = _lire(PERIMETRE)
    d = d[(d["groupe"] == groupe) & (d["methode"] != "mère")]
    exercices = sorted(d["exercice"].unique())
    entites: dict[str, dict] = {}
    for _, r in d.sort_values("exercice").iterrows():
        e = entites.setdefault(_cle_entite(r["entite"]), {"nom": r["entite"], "premier": r["exercice"], "val": {}})
        e["nom"] = r["entite"]
        valeur = _pct(r["interet_pct"] or r["controle_pct"])
        e["val"][r["exercice"]] = valeur + (" (ME)" if r["methode"] == "mise en équivalence" else "")
    lignes = [[e["nom"].replace("’", "'")] + [e["val"].get(x, "–") for x in exercices]
              for e in sorted(entites.values(), key=lambda e: (e["premier"], e["nom"]))]
    lignes.append(["**Nombre d'entités**"] + [str(sum(1 for e in entites.values() if x in e["val"])) for x in exercices])
    _md(["Entité"] + exercices, lignes, caption, tbl_id)


def _matrice(groupe: str):
    """Entités × exercices : (noms, exercices, valeurs d'intérêt, indicateurs de mise en équivalence)."""
    d = _lire(PERIMETRE)
    d = d[(d["groupe"] == groupe) & (d["methode"] != "mère")]
    exercices = sorted(d["exercice"].unique())
    entites: dict[str, dict] = {}
    for _, r in d.sort_values("exercice").iterrows():
        e = entites.setdefault(_cle_entite(r["entite"]), {"nom": r["entite"], "premier": r["exercice"], "val": {}, "me": set()})
        e["nom"] = r["entite"]
        e["val"][r["exercice"]] = float(r["interet_pct"] or r["controle_pct"])
        if r["methode"] == "mise en équivalence":
            e["me"].add(r["exercice"])
    liste = sorted(entites.values(), key=lambda e: (e["premier"], e["nom"]))
    return liste, exercices


def fig_evolution(groupe: str, etiquette: str = "Pourcentage d'intérêt"):
    import numpy as np
    figtools.apply_lang_font()
    ft = figtools.fig_text
    liste, lus = _matrice(groupe)
    # une année sans rapport lu reste une colonne vide quand elle est seule ; un long trou n'a pas de colonnes
    exercices = []
    for a in lus:
        if exercices and int(a) - int(exercices[-1]) == 2:
            exercices.append(str(int(a) - 1))
        exercices.append(a)
    valeurs = np.array([[e["val"].get(x, np.nan) for x in exercices] for e in liste])
    fig, ax = plt.subplots(figsize=(9.5, 0.28 * len(liste) + 1.8))
    image = ax.imshow(valeurs, aspect="auto", cmap="Blues", vmin=0, vmax=100)
    for i, e in enumerate(liste):
        for j, x in enumerate(exercices):
            if x in e["val"]:
                marque = "ME" if x in e["me"] else f"{e['val'][x]:.0f}"
                ax.text(j, i, marque, ha="center", va="center", fontsize=6.5,
                        color="white" if e["val"][x] > 60 else "#24292f")
    ax.set_xticks(range(len(exercices)), exercices, fontsize=8)
    ax.set_yticks(range(len(liste)), [e["nom"].replace("’", "'")[:38] for e in liste], fontsize=7)
    ax.xaxis.tick_top()
    nombres = [int(np.sum(~np.isnan(valeurs[:, j]))) for j in range(len(exercices))]
    ax.set_xlabel(ft("Nombre d'entités consolidées : " + " · ".join(f"{x} : {n}" for x, n in zip(exercices, nombres) if n)),
                  fontsize=7)
    for cote in ("top", "right", "left", "bottom"):
        ax.spines[cote].set_visible(False)
    ax.tick_params(length=0)
    fig.colorbar(image, ax=ax, fraction=0.025, pad=0.02, label=ft(etiquette))
    fig.tight_layout()
    return fig


def table_evolution(groupe: str):
    liste, exercices = _matrice(groupe)
    lignes = [{"entite": e["nom"], "exercice": x, "interet_ou_controle_pct": v,
               "methode": "mise en équivalence" if x in e["me"] else "intégration globale ou non précisée"}
              for e in liste for x, v in sorted(e["val"].items())]
    return pd.DataFrame(lignes)


def figure_evolution(groupe: str, caption: str, note_lecture: str | None = None, etiquette: str = "Pourcentage d'intérêt") -> None:
    figtools.figure_tabs(fig_evolution(groupe, etiquette), table_evolution(groupe), PERIMETRE,
                         slug=f"fig_ep_cotees_evolution_{groupe.lower()}", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def tableau_opinions(groupe: str, caption: str, tbl_id: str) -> None:
    """Opinion des commissaires aux comptes par exercice, avec chaque motif de réserve et sa page."""
    d = _lire("opinions-cac")
    d = d[d["groupe"] == groupe]
    lignes, precedent = [], None
    for _, r in d.iterrows():
        exercice = f"**{r['exercice']}**" if r["exercice"] != precedent else ""
        opinion = r["opinion"] if r["exercice"] != precedent else ""
        precedent = r["exercice"]
        lignes.append([exercice, opinion, r["motif"], f"[@{r['source']}, p. {r['page_pdf']}]"])
    _md(["Exercice", "Opinion", "Motif de la réserve", "Source"], lignes, caption, tbl_id, gauche=(2,))


THEMES_CAC = {
    "suspens": "Comptes de suspens et soldes figés",
    "hors_bilan": "Engagements hors bilan non exhaustifs",
    "garanties": "Garanties reçues",
    "si": "Système d'information, multidevises",
    "provisions": "Provisions, risques antérieurs",
    "notation": "Notation ou états financiers des relations",
    "ecarts": "Écarts avec la base de gestion ou la BCT",
    "immobilisations": "Inventaire des immobilisations",
    "fonds_social": "« Réserves pour fonds social »",
    "avocats": "Confirmations des avocats",
    "retraites": "Indemnités de départ à la retraite",
    "fonds_etat": "Fonds budgétaires de l'État",
    "produits": "Produits identifiés par client",
    # STAR (assureur) : thèmes propres, tracés seulement pour le groupe STAR
    "star_provisions_techniques": "Provisions techniques insuffisantes",
    "star_ecarts_comptes": "Écarts comptables, primes",
    "star_exercices_anterieurs": "Exercices antérieurs dans le résultat",
    "tunisair_tiers": "Clients, fournisseurs, comptes d'attente",
    "tunisair_provisions": "Provisions et risques non constatés",
    "tunisair_flotte": "Flotte : avions, moteurs, maintenance",
    "tunisair_fonds_social": "Fonds social et paie",
    "tunisair_redevances": "Redevances aéroportuaires collectées",
    "tunisair_banques": "Rapprochements bancaires, caisses",
    "tunisair_immobilisations": "Inventaire des immobilisations",
    "tunisair_informatique": "Système d'information, prestations d'AISA",
    "tunisair_filiales": "Comptes réciproques avec les filiales",
    "tunisair_oaca": "Dettes et concessions envers l'OACA",
    "tunisair_stocks": "Stocks techniques",
    "tunisair_hors_bilan": "Engagements hors bilan (Tunisair)",
    "tunisair_limitations": "Limitation des travaux",
    "tunisair_presentation": "Présentation des états financiers",
    "sotumag_chambres_froides": "Chambres froides louées comme boxes d'emballage (SOTUMAG)",
    "sotumag_pharmacies": "Pharmacies et laboratoires conventionnés (SOTUMAG)",
    "tt_immeubles": "Immeubles apportés, situation juridique",
    "tt_clients": "Comptabilité clients, encaissements non identifiés",
    "tt_charges": "Rattachement des charges, factures fournisseurs",
    "tt_passifs_abonnes": "Avances sur consommation, redevances d'avance",
    "tt_prepaye": "Chiffre d'affaires prépayé, ajustement préalable",
    "tt_confirmations": "Confirmations de soldes non reçues",
}


def fig_cac(groupe: str, societe: str, delais_ecartes: tuple[int, ...] = ()):
    """Trois vues sur les mêmes exercices : thèmes de réserve (carte), nombre de motifs (barres), délai de publication (courbe).

    Une société sans ligne dans `delais-publication.csv` (elle n'a pas de page à la Bourse) n'a pas de courbe des délais : deux vues.
    """
    import numpy as np
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _lire("opinions-cac")
    d = d[d["groupe"] == groupe]
    delais = _lire("delais-publication")
    # un délai nul est la date de clôture que la Bourse porte faute de date de publication : il n'est pas tracé
    delais = delais[(delais["societe"] == societe) & (delais["nature"] == "individuel") & (delais["jours"].astype(int) > 0)]
    delais = delais[~delais["exercice"].astype(int).isin(delais_ecartes)]  # dates de la Bourse sans valeur (BTE)
    lus = sorted(int(x) for x in d["exercice"].unique())
    fin = max(lus + [int(x) for x in delais["exercice"]])
    exercices = list(range(min(lus) - 1, fin + 1))  # un exercice avant le premier rapport lu, jusqu'au dernier délai connu
    delais = delais[delais["exercice"].astype(int) >= exercices[0]]
    utilises = {t for ligne in d.loc[~d["opinion"].str.startswith("sans"), "themes"] for t in ligne.split(";")}
    themes = [t for t in THEMES_CAC if t in utilises]  # une ligne par thème que le groupe porte : pas de ligne vide
    if not themes:  # groupe sans aucune réserve : les thèmes communs, en cases blanches
        themes = [t for t in THEMES_CAC if not t.startswith(("star_", "tunisair_", "cimbiz_", "sotumag_", "tunisre_", "bte_", "tt_"))]
    carte = np.full((len(themes), len(exercices)), np.nan)
    nombres = np.zeros(len(exercices))
    for _, r in d.iterrows():
        j = exercices.index(int(r["exercice"]))
        if r["opinion"].startswith("sans"):  # exercice lu, sans réserve : case blanche, zéro motif
            continue
        nombres[j] += 1
        for t in r["themes"].split(";"):
            carte[themes.index(t), j] = 1
    # sans délai de publication (société sans page de la Bourse), la figure s'arrête au nombre de motifs
    avec_delais = not delais.empty
    if avec_delais:
        fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(9.5, 8), sharex=True, gridspec_kw={"height_ratios": [3.2, 1, 1.3], "hspace": 0.12})
    else:
        fig, (a1, a2) = plt.subplots(2, 1, figsize=(9.5, 6), sharex=True, gridspec_kw={"height_ratios": [3.2, 1], "hspace": 0.12})
        a3 = None
    # 1. thèmes : une case par thème et exercice ; gris : exercice sans rapport lu
    for j, x in enumerate(exercices):
        if x not in lus:
            a1.add_patch(plt.Rectangle((j - 0.5, -0.5), 1, len(themes), color="#eaeef2", lw=0, zorder=0))
    a1.imshow(np.ma.masked_invalid(carte), aspect="auto", cmap="Reds", vmin=0, vmax=1.6, extent=(-0.5, len(exercices) - 0.5, len(themes) - 0.5, -0.5), zorder=1)
    a1.set_yticks(range(len(themes)), [ft(THEMES_CAC[t]) for t in themes], fontsize=8)
    a1.set_title(ft("Thèmes des réserves (gris : exercice sans rapport lu)"), fontsize=9, loc="left")
    for j in range(len(exercices)):
        for i in range(len(themes)):
            if not np.isnan(carte[i, j]):
                figtools.infobulle(a1.plot([j], [i], "s", color="none")[0], f"{exercices[j]} · {THEMES_CAC[themes[i]]}")
    # 2. nombre de motifs
    a2.bar(range(len(exercices)), nombres, color="#cf222e", width=0.6)
    for j, n in enumerate(nombres):
        if n:
            a2.text(j, n + 0.1, f"{int(n)}", ha="center", fontsize=8)
    a2.set_ylim(0, max(nombres.max() + 1.5, 4))
    a2.set_title(ft("Nombre de motifs de réserve"), fontsize=9, loc="left")
    # 3. délai de publication
    if avec_delais:
        pts = sorted((int(r["exercice"]), int(r["jours"])) for _, r in delais.iterrows())
        if pts:
            a3.plot([exercices.index(x) for x, _ in pts], [j for _, j in pts], "-o", color="#0969da", ms=4)
            for x, jours in pts:
                a3.annotate(str(jours), (exercices.index(x), jours), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=7)
        a3.set_title(ft("Délai de publication des états financiers annuels individuels (jours après le 31 décembre)"), fontsize=9, loc="left")
        a3.set_ylim(0, max([j for _, j in pts] + [100]) * 1.2)
    (a3 if avec_delais else a2).set_xticks(range(len(exercices)), [str(x) for x in exercices], fontsize=8)
    for axe in tuple(a for a in (a1, a2, a3) if a is not None):
        axe.grid(axis="y", color="#d0d7de", lw=0.5)
        for cote in ("top", "right"):
            axe.spines[cote].set_visible(False)
    return fig


def figure_cac(groupe: str, societe: str, caption: str, note_lecture: str | None = None,
               delais_ecartes: tuple[int, ...] = ()) -> None:
    d = _lire("opinions-cac")
    figtools.figure_tabs(fig_cac(groupe, societe, delais_ecartes), d[d["groupe"] == groupe], "opinions-cac",
                         slug=f"fig_ep_cotees_cac_{societe}", caption=caption, note_lecture=note_lecture, nominal=False)
    plt.close("all")


def _fr(valeur: float, decimales: int = 1) -> str:
    return f"{valeur:,.{decimales}f}".replace(",", " ").replace(".", ",").replace("-", "−")


def _engagements_bna() -> "pd.DataFrame":
    """Une ligne par exercice : engagements (MD) du total, de l'Office des céréales, des autres entités nommées, et le reste."""
    d = _lire(ENGAGEMENTS_BNA)
    d = d[d["valeur_kdt"] != ""].copy()
    d["valeur"] = d["valeur_kdt"].astype(float) / 1000
    lignes = {}
    for exercice, g in d.groupby("exercice"):
        eng = g[g["grandeur"] == "engagements"]
        total = eng[eng["entite"] == "Total des entreprises publiques"]["valeur"].sum()
        oc = eng[eng["entite"] == "Office des céréales"]["valeur"].sum()
        autres = eng[~eng["entite"].isin(["Total des entreprises publiques", "Office des céréales"])]["valeur"].sum()
        gar = g[(g["grandeur"] == "garanties de l'État") & (g["entite"] == "Total des entreprises publiques")]["valeur"].sum()
        lignes[int(exercice)] = {"total": total, "oc": oc, "autres": autres, "reste": total - oc - autres, "garanties": gar}
    return pd.DataFrame(lignes).T.sort_index()


def fig_engagements_bna():
    """Engagements de la BNA envers les entreprises publiques (barres empilées) et part garantie par l'État (courbe)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    e = _engagements_bna()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 6.5), sharex=True, gridspec_kw={"height_ratios": [3, 1.4], "hspace": 0.12})
    x = list(range(len(e)))
    fond = [0.0] * len(e)
    for cle, nom, couleur in (("oc", "Office des céréales", "#cf222e"), ("autres", "Autres entités nommées par la note", "#0969da"),
                              ("reste", "Reste des entreprises publiques", "#8c959f")):
        a1.bar(x, e[cle], bottom=fond, color=couleur, width=0.65, label=ft(nom))
        fond = [f + v for f, v in zip(fond, e[cle])]
    for i, total in enumerate(e["total"]):
        a1.text(i, total + 80, _fr(total, 0), ha="center", fontsize=8)
    a1.set_ylabel(ft("millions de dinars courants"))
    a1.legend(fontsize=8, loc="upper left", frameon=False)
    a1.set_title(ft("Engagements de la BNA envers les entreprises publiques (fin d'exercice)"), fontsize=10, loc="left")
    a1.grid(axis="y", alpha=0.3)
    part = (e["garanties"] / e["total"] * 100).where(e["garanties"] > 0)
    a2.plot(x, part, marker="o", color="#1a7f37")
    for i, v in enumerate(part):
        if v == v:
            a2.text(i, v + 5, f"{v:.0f} %", ha="center", fontsize=8)
    a2.set_ylim(0, 115)
    a2.set_ylabel(ft("garanties de l'État, % des engagements"), fontsize=8)
    a2.set_xticks(x, [str(i) for i in e.index], fontsize=8)
    a2.grid(axis="y", alpha=0.3)
    return fig


def figure_engagements_bna(caption: str, note_lecture: str | None = None) -> None:
    d = _lire(ENGAGEMENTS_BNA)
    figtools.figure_tabs(fig_engagements_bna(), d, ENGAGEMENTS_BNA, slug="fig_ep_bna_engagements",
                         caption=caption, note_lecture=note_lecture, nominal=False)
    plt.close("all")


def tableau_engagements_bna(caption: str, tbl_id: str = "tbl-ep-bna-engagements") -> None:
    """Total et Office des céréales : engagements, garanties de l'État, autres garanties, agios réservés, provisions (MD)."""
    d = _lire(ENGAGEMENTS_BNA)
    d = d[d["valeur_kdt"] != ""].copy()
    d["valeur"] = d["valeur_kdt"].astype(float) / 1000
    exercices = sorted(d["exercice"].unique())
    lignes = []
    for entite, court in (("Total des entreprises publiques", "Total"), ("Office des céréales", "Office des céréales")):
        for grandeur in ("engagements", "garanties de l'État", "autres garanties", "agios et intérêts réservés", "provisions"):
            x = d[(d["entite"] == entite) & (d["grandeur"] == grandeur)].set_index("exercice")["valeur"]
            if x.empty:
                continue
            lignes.append([f"{court} : {grandeur}"] + [_fr(x[e]) if e in x.index else "–" for e in exercices])
    _md(["Grandeur (MD)"] + exercices, lignes, caption, tbl_id)


def tableau_registre(caption: str, tbl_id: str = "tbl-ep-registre-entreprises") -> None:
    """Une ligne par entreprise : identifiant, forme, état, états financiers déposés."""
    d = _lire(REGISTRE)
    lignes = []
    for _, r in d.iterrows():
        exercices = r["exercices_etats_financiers"].replace(" ", ", ") or "aucun"
        lignes.append([r["entreprise"], r["id_unique"], r["forme_juridique"].replace(
            "Etablissement", "Établissement"), r["etat_registre"].replace("Non Actif", "non actif"
            ).replace("Actif", "actif"), exercices, r["documents"]])
    _md(["Entreprise", "Identifiant", "Forme au Registre", "État", "États financiers déposés",
         "Documents listés"], lignes, caption, tbl_id)


COULEURS_SOCIETES = {"BNA": "#1a7f37", "STB": "#0969da", "BH": "#bc4c00", "STAR": "#8250df",
                     "SOTUMAG": "#57606a", "Ciments de Bizerte": "#cf222e", "Tunisair": "#bf8700"}


def donnees_resultats() -> pd.DataFrame:
    d = _lire(RESULTATS)
    for colonne in ("resultat_net_dt", "dividende_etat_dt", "dividende_par_action_dt"):
        d[colonne] = pd.to_numeric(d[colonne], errors="coerce")
    d["resultat_net_md"] = d["resultat_net_dt"] / 1e6
    d["dividende_etat_md"] = d["dividende_etat_dt"] / 1e6
    d["exercice"] = d["exercice"].astype(int)
    return d


def fig_resultats():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_resultats()
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 4.8), gridspec_kw={"width_ratios": [2.1, 1]})
    ax.axhline(0, color="#57606a", lw=0.8, zorder=1)
    for societe, groupe in d.groupby("societe"):
        couleur = COULEURS_SOCIETES[societe]
        ax.plot(groupe["exercice"], groupe["resultat_net_md"], "-", color=couleur, lw=1.8, zorder=2)
        points, = ax.plot(groupe["exercice"], groupe["resultat_net_md"], "o", color=couleur, ms=5,
                          zorder=3, label=societe)
        for _, r in groupe.iterrows():
            figtools.infobulle(points, f"{societe} · exercice {r['exercice']} · résultat net "
                                      f"{r['resultat_net_md']:.1f} MD")
    ax.set_xticks(sorted(d["exercice"].unique()))
    ax.set_ylabel(ft("Résultat net (millions de dinars)"))
    ax.set_xlabel(ft("Exercice"))
    ax.set_title(ft("Résultat net"), fontsize=10, loc="left")
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=4, fontsize=8, frameon=False)
    calcule = d.dropna(subset=["dividende_etat_md"]).sort_values("dividende_etat_md")
    etiquettes = [f"{r['societe']}\n{r['exercice']}" for _, r in calcule.iterrows()]
    barres = bx.barh(etiquettes, calcule["dividende_etat_md"],
                     color=[COULEURS_SOCIETES[s] for s in calcule["societe"]], zorder=2)
    for barre, (_, r) in zip(barres, calcule.iterrows()):
        bx.text(barre.get_width() + 0.5, barre.get_y() + barre.get_height() / 2,
                f"{r['dividende_etat_md']:.1f}".replace(".", ","), va="center", fontsize=8)
        figtools.infobulle(barre, f"{r['societe']} · exercice {r['exercice']} · dividende par action "
                                  f"{r['dividende_par_action_dt']:.3g} D × {int(r['actions_etat']):,} actions "
                                  f"de l'État = {r['dividende_etat_md']:.1f} MD".replace(",", " "))
    bx.set_xlim(0, calcule["dividende_etat_md"].max() * 1.18)
    bx.set_xlabel(ft("Dividende calculé (millions de dinars)"), fontsize=8.5)
    bx.set_title(ft("Dividende de l'État"), fontsize=10, loc="left")
    bx.grid(axis="x", color="#d0d7de", lw=0.6)
    bx.set_axisbelow(True)
    for axe in (ax, bx):
        for cote in ("top", "right"):
            axe.spines[cote].set_visible(False)
    fig.tight_layout()
    return fig


def table_resultats() -> pd.DataFrame:
    d = donnees_resultats()
    return d[["societe", "exercice", "resultat_net_dt", "dividende_par_action_dt", "actions_etat",
              "assemblee", "dividende_etat_dt"]]


def figure_resultats(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure des résultats et dividendes en onglets (chunk `output: asis`, `fig-…`)."""
    figtools.figure_tabs(fig_resultats(), table_resultats(), RESULTATS,
                         slug="fig_ep_cotees_resultats", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def donnees_capital() -> pd.DataFrame:
    d = _lire(CAPITAL)
    d["date"] = pd.to_datetime(d["date"])
    d["capital_md"] = d["capital_dt"].astype(float) / 1e6
    d = d.sort_values(["banque", "date"], kind="stable")
    garde = []
    for _, groupe in d.groupby("banque"):
        precedent = 0.0
        for idx, r in groupe.iterrows():
            if r["capital_md"] >= precedent:
                garde.append(idx)
                precedent = r["capital_md"]
    return d.loc[garde]


def fig_capital():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_capital()
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.axvspan(pd.Timestamp("2013-01-01"), pd.Timestamp("2015-12-31"), color="#d0d7de",
               alpha=0.5, lw=0, zorder=0)
    for banque, groupe in d.groupby("banque"):
        groupe = groupe.drop_duplicates("date", keep="last")
        ax.step(groupe["date"], groupe["capital_md"], where="post", color=COULEURS[banque],
                lw=1.8, zorder=2, label=banque)
        points, = ax.plot(groupe["date"], groupe["capital_md"], "o", color=COULEURS[banque],
                          ms=4, zorder=3)
        for _, r in groupe.iterrows():
            figtools.infobulle(points, f"{banque} · {r['date']:%d/%m/%Y} · {r['operation']} : "
                                      f"capital {r['capital_md']:.1f} MD")
    ax.set_ylabel(ft("Capital (millions de dinars)"))
    ax.set_xlabel(ft("Date de la décision de l'assemblée"))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(loc="upper left", frameon=False)
    ax.annotate(ft("lois de 2013 à 2015"), xy=(pd.Timestamp("2012-10-01"), ax.get_ylim()[1] * 0.97),
                ha="right", va="top", fontsize=8, color="#57606a")
    fig.tight_layout()
    return fig


def table_capital() -> pd.DataFrame:
    d = donnees_capital()
    return d[["banque", "date", "operation", "augmentation_dt", "capital_dt"]].assign(
        date=d["date"].dt.strftime("%Y-%m-%d"))


def figure_capital(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure du capital en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    figtools.figure_tabs(fig_capital(), table_capital(), CAPITAL,
                         slug="fig_ep_cotees_capital", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")

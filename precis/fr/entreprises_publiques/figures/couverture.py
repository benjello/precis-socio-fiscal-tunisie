"""Matrice de couverture des données et indicateurs de l'annexe « La couverture des
données » (volume « Les entreprises publiques »).

    from figures import couverture as cv
    cv.tableau_matrice(caption=…)       # une ligne par entreprise, une colonne par source
    cv.tableau_par_exercice(caption=…)  # nombre d'entreprises couvertes, par exercice et par source
    cv.tableau_par_type(caption=…)      # couverture par type d'entreprise

D'OÙ VIENNENT LES DONNÉES. De la table de correspondance versionnée `listes/couverture-sources.csv`
(un nom d'entreprise, ses clés de jointure dans chaque source) ET des fichiers de données eux-mêmes :

  - **fiche du ministère des Finances**, par édition : `figdata/fig_ep_<cle_fiches>_fiches.csv`
    (colonne `Édition` : LF 2022, LF 2024, LF 2025) ;
  - **états financiers du Registre national** : `listes/entreprises-publiques-registre.csv`
    (colonne `exercices_etats_financiers`) ;
  - **rapport annuel ou d'activité** et **états financiers de la Bourse ou du CMF** :
    `listes/inventaire-rapports-*.csv` (colonne `nature`) ;
  - **page de la Bourse de Tunis** : présence d'une page cotée (`slug_bourse`) ;
  - **engagements et garanties de l'État, détail par entreprise** :
    `listes/bna-engagements-entreprises-publiques.csv` (états financiers individuels de la BNA).

RÈGLES (le précis l'exige).

  - **Aucune donnée fabriquée.** La couverture d'une case est LUE dans les fichiers ci-dessus ;
    la table de correspondance ne fait que rattacher les noms. Rien n'est saisi à la main.
  - **« – » est une absence constatée** (source cherchée, non trouvée), non un oubli ; une case
    vide signale que la source n'a pas été interrogée pour cette entreprise (reportée dans la
    colonne « source possible, non obtenue »).
  - **La dette croisée n'est publiée qu'en agrégat** (État, grand secteur) : aucune source du
    volume ne la ventile entreprise par entreprise, d'où « – » dans toute la colonne.
  - **Les garanties par entreprise ne viennent que des états de la BNA**, qui ne nomment qu'une
    poignée de débiteurs : « – » ailleurs ne veut pas dire sans garantie, mais sans détail dans
    une source par entreprise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))

RELEVES = Path(__file__).resolve().parent.parent / "listes"
FIGDATA = Path(__file__).resolve().parent.parent / "figdata"
CORRESP = "couverture-sources"
REGISTRE = "entreprises-publiques-registre"
BNA = "bna-engagements-entreprises-publiques"

EDITIONS = ["LF 2022", "LF 2024", "LF 2025"]
CATEGORIES = [("banque", "Banques"), ("etablissement", "Établissements publics"),
              ("societe", "Sociétés anonymes")]
# Fenêtre des exercices pour l'indicateur par année (les fiches couvrent 2018-2023, le Registre
# 2019-2025, les rapports remontent plus loin ; on retient la fenêtre commune la plus parlante).
EXERCICES = list(range(2016, 2025))


def _lire(nom: str) -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{nom}.csv", dtype=str, keep_default_na=False)


def _annees(texte) -> list[int]:
    """Les millésimes (quatre chiffres) trouvés dans une chaîne, triés, sans doublon."""
    if texte is None:
        return []
    return sorted({int(a) for a in re.findall(r"(?:19|20)\d{2}", str(texte))})


def _compacte(annees: list[int]) -> str:
    """« 2018–2021, 2023 » à partir d'une liste d'années triées."""
    if not annees:
        return ""
    bouts = []
    debut = prec = annees[0]
    for a in annees[1:]:
        if a == prec + 1:
            prec = a
            continue
        bouts.append((debut, prec))
        debut = prec = a
    bouts.append((debut, prec))
    return ", ".join(str(d) if d == f else f"{d}\u2013{f}" for d, f in bouts)


# --- lecture des sources, keyée par les clés de la table de correspondance -----------------------

def _fiches(cle: str) -> dict:
    """Pour une fiche : éditions présentes et exercices couverts, lus dans le figdata."""
    chemin = FIGDATA / f"fig_ep_{cle}_fiches.csv"
    d = pd.read_csv(chemin, dtype=str, keep_default_na=False, comment="#")
    editions = [e for e in EDITIONS if e in set(d["Édition"])]
    return {"editions": editions, "exercices": _annees(" ".join(d["Exercice"]))}


def _registre() -> dict:
    """sigle -> liste des exercices d'états financiers déposés (vide si aucun)."""
    d = _lire(REGISTRE)
    return {r["sigle"]: _annees(r["exercices_etats_financiers"]) for _, r in d.iterrows()}


_RAP = re.compile(r"rapport", re.I)
_EF = re.compile(r"(tats.financ|etats.financ|etats_financ|information_ago|r[ée]f[ée]rence)", re.I)
_SANS = re.compile(r"sans rapport des commiss", re.I)


def _inventaire() -> dict:
    """sigle -> {rapports: [années], ef_bourse: [années], interroge: bool}. Un `nature` valant
    « aucun » marque une source cherchée et non trouvée (interroge=True, listes vides)."""
    acc: dict[str, dict] = {}
    for fichier in sorted(RELEVES.glob("inventaire-rapports-*.csv")):
        d = pd.read_csv(fichier, dtype=str, keep_default_na=False)
        for _, r in d.iterrows():
            sigle = r["sigle"]
            nat = r["nature"]
            e = acc.setdefault(sigle, {"rapports": set(), "ef_bourse": set(), "interroge": False})
            e["interroge"] = True
            annee = _annees(r["exercice"])
            if _RAP.search(nat) and not _SANS.search(nat):
                e["rapports"].update(annee)
            elif _EF.search(nat):
                e["ef_bourse"].update(annee)
    return {s: {"rapports": sorted(v["rapports"]), "ef_bourse": sorted(v["ef_bourse"]),
                "interroge": v["interroge"]} for s, v in acc.items()}


def _bna() -> dict:
    """entité -> liste des exercices où la BNA chiffre au moins un engagement."""
    d = _lire(BNA)
    d = d[d["valeur_kdt"] != ""]
    out: dict[str, set] = {}
    for _, r in d.iterrows():
        out.setdefault(r["entite"], set()).add(int(r["exercice"]))
    return {k: sorted(v) for k, v in out.items()}


def _couverture() -> pd.DataFrame:
    """Une ligne par entreprise, enrichie de ce que chaque source donne (listes d'années ou
    marqueurs). Tout est lu dans les fichiers ; rien n'est saisi."""
    corr = _lire(CORRESP)
    corr["rang"] = corr["rang"].astype(int)
    reg, inv, bna = _registre(), _inventaire(), _bna()
    lignes = []
    for _, r in corr.sort_values("rang").iterrows():
        info = {"entreprise": r["entreprise"], "categorie": r["categorie"],
                "non_obtenue": r["non_obtenue"]}
        # Fiche du ministère
        if r["cle_fiches"]:
            f = _fiches(r["cle_fiches"])
            info["fiche_editions"] = f["editions"]
            info["fiche_exercices"] = f["exercices"]
        else:
            info["fiche_editions"] = []
            info["fiche_exercices"] = []
        # États financiers du Registre
        info["registre"] = r["sigle_registre"] != ""
        info["rne_exercices"] = reg.get(r["sigle_registre"], []) if r["sigle_registre"] else []
        # Rapports et états financiers de la Bourse / CMF
        e = inv.get(r["sigle_rapports"], {"rapports": [], "ef_bourse": [], "interroge": False})
        info["inventaire"] = e["interroge"] if r["sigle_rapports"] else False
        info["rapports"] = e["rapports"]
        info["ef_bourse"] = e["ef_bourse"]
        # Page de la Bourse
        info["bourse_page"] = r["slug_bourse"] != ""
        # Garanties par entreprise (BNA)
        info["bna"] = r["cle_bna"] != ""
        info["garanties"] = bna.get(r["cle_bna"], []) if r["cle_bna"] else []
        lignes.append(info)
    return pd.DataFrame(lignes)


# --- rendu markdown ------------------------------------------------------------------------------

def _md(entete: list[str], lignes: list[list[str]], caption: str, tbl_id: str,
        gauche: tuple[int, ...] = (1,)) -> None:
    aligns = "|".join("---" if i + 1 in gauche else ":-:" for i in range(len(entete) - 1))
    out = ["| " + " | ".join(entete) + " |", "|---|" + aligns + "|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def _cell_fiche(info) -> str:
    if info["fiche_editions"]:
        return "·".join(e.replace("LF ", "") for e in info["fiche_editions"])
    return "–"


def _cell_rne(info) -> str:
    if info["rne_exercices"]:
        return _compacte(info["rne_exercices"])
    return "–" if info["registre"] else ""


def _cell_rapport(info) -> str:
    if info["rapports"]:
        return _compacte(info["rapports"])
    return "–" if info["inventaire"] else ""


def _cell_bourse(info) -> str:
    if info["ef_bourse"]:
        return _compacte(info["ef_bourse"])
    return "page" if info["bourse_page"] else "–"


def _cell_garanties(info) -> str:
    if info["garanties"]:
        return _compacte(info["garanties"])
    return "–"


def tableau_matrice(caption: str, tbl_id: str = "tbl-ep-couverture-matrice") -> None:
    """Une ligne par entreprise, une colonne par type de source, groupée par type d'entreprise."""
    d = _couverture()
    entete = ["Entreprise", "Fiche min. (éditions)", "États fin. (Registre)",
              "Rapport annuel", "Bourse / CMF", "Garanties (BNA)", "Dette croisée",
              "Source possible, non obtenue"]
    lignes = []
    for cat, titre in CATEGORIES:
        g = d[d["categorie"] == cat]
        lignes.append([f"**{titre}** ({len(g)})"] + [""] * (len(entete) - 1))
        for _, info in g.iterrows():
            lignes.append([info["entreprise"], _cell_fiche(info), _cell_rne(info),
                           _cell_rapport(info), _cell_bourse(info), _cell_garanties(info),
                           "–", info["non_obtenue"]])
    _md(entete, lignes, caption, tbl_id, gauche=(1, 8))


def tableau_par_exercice(caption: str, tbl_id: str = "tbl-ep-couverture-exercice") -> None:
    """Nombre d'entreprises couvertes par chaque source, exercice par exercice."""
    d = _couverture()
    lignes = []
    sources = [("Fiche du ministère", "fiche_exercices"),
               ("États financiers (Registre)", "rne_exercices"),
               ("Rapport annuel", "rapports"),
               ("États financiers (Bourse / CMF)", "ef_bourse")]
    for libelle, col in sources:
        cells = [str(int(d[col].apply(lambda xs: e in xs).sum())) for e in EXERCICES]
        lignes.append([libelle] + [c if c != "0" else "–" for c in cells])
    _md(["Source"] + [str(e) for e in EXERCICES], lignes, caption, tbl_id)


def tableau_par_type(caption: str, tbl_id: str = "tbl-ep-couverture-type") -> None:
    """Couverture par type d'entreprise : nombre d'entreprises ayant chaque source."""
    d = _couverture()
    lignes = []
    def compte(g, pred):
        return int(sum(1 for _, i in g.iterrows() if pred(i)))
    for cat, titre in CATEGORIES:
        g = d[d["categorie"] == cat]
        n = len(g)
        lignes.append([titre, str(n),
                       str(compte(g, lambda i: bool(i["fiche_editions"]))),
                       str(compte(g, lambda i: bool(i["rne_exercices"]))),
                       str(compte(g, lambda i: bool(i["rapports"]))),
                       str(compte(g, lambda i: bool(i["ef_bourse"]) or i["bourse_page"])),
                       str(compte(g, lambda i: bool(i["garanties"])))])
    g = d
    lignes.append(["**Ensemble**", f"**{len(g)}**",
                   f"**{compte(g, lambda i: bool(i['fiche_editions']))}**",
                   f"**{compte(g, lambda i: bool(i['rne_exercices']))}**",
                   f"**{compte(g, lambda i: bool(i['rapports']))}**",
                   f"**{compte(g, lambda i: bool(i['ef_bourse']) or i['bourse_page'])}**",
                   f"**{compte(g, lambda i: bool(i['garanties']))}**"])
    _md(["Type d'entreprise", "Entreprises", "Fiche min.", "États fin. (Registre)",
         "Rapport annuel", "Bourse / CMF", "Garanties (BNA)"], lignes, caption, tbl_id)

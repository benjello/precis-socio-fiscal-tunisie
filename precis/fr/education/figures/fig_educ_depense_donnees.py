"""Données des figures du chapitre « La dépense d'éducation » : copie sourcée des séries.

Copie, ligne à ligne, les séries d'éducation du catalogue de `tunisia-data`, lues par
`figtools.series()` (entrepôt s'il est installé, sinon snapshot `precis/_seriescache/`) — une
ligne par valeur avec sa source et sa page, la colonne `serie` nommant le relevé d'origine de la
note documentaire — dans les figdata `figdata/fig_educ_depense_*.csv` du livre, avec leur
en-tête de provenance et leur sidecar `.csv.yml`. Aucune valeur n'est saisie à la main ; seules s'ajoutent les conversions en
dinars de 2023 par l'indice `ipc-longue-periode` du catalogue, et les deux parts, recalculées
HORS RECHERCHE (décision du 17 octobre 2026 : la recherche scientifique n'entre ni dans les
totaux ni dans les ratios ; ses lignes identifiables sont copiées « hors total »). Les parts
de la note, qui comprennent la recherche, ne servent plus que de contrôle de la copie. Les chunks du chapitre ne lancent PAS ce script : ils lisent les figdata qu'il a
écrits (`fig_educ_depense.py`). Le relancer après une correction des séries (dans
`tunisia-data`, puis `figtools.refresh_cache()`) :

    uv run python precis/fr/education/figures/fig_educ_depense_donnees.py [tableaux.md]

L'argument facultatif reçoit les tableaux Markdown des blocs repliés du chapitre.
"""
import io
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import figtools  # noqa: E402

OUT = ROOT / "precis/fr/education/figdata"
DATE = "2026-10-29"
FICHE = "docs/notes/education-depense-2026-10-17.md, sources/education-depense-series.md"
# Séries d'éducation du catalogue lues ici ; la colonne `serie` nomme le relevé de la note.
SERIES = ("education-depense-ministeres", "education-depense-nature", "education-depense-parts-calcul",
          "education-depense-programmes", "education-personnels-fonction-publique",
          "education-effectifs-annuaire", "education-depense-menages", "education-uis-depense")
_RELEVES: dict[str, pd.DataFrame] = {}

ipc = pd.read_csv(ROOT / "precis/_seriescache/ipc-longue-periode.csv").set_index("annee")["indice_base1970"]
IPC23 = ipc[2023]
# PIB nominal (millions de dinars) de la série dont la note tire sa part du PIB
DENOM = pd.read_csv(ROOT / "precis/_seriescache/denominateurs-depenses-etat-pib.csv").set_index("annee")
HORS_TOTAL = "hors total (recherche)"


def _releves() -> dict[str, pd.DataFrame]:
    """{relevé: lignes}, toutes séries du catalogue confondues, chargé une fois."""
    if not _RELEVES:
        for sid in SERIES:
            for nom, d in figtools.series(sid).groupby("serie", sort=False):
                _RELEVES[nom] = d.drop(columns="serie")
    return _RELEVES


def lire(nom):
    """Lignes d'un relevé, avec les types qu'aurait son fichier lu seul. Une série du catalogue
    mêle des relevés aux colonnes de types différents : une colonne d'entiers y devient flottante
    dès qu'un autre relevé porte une décimale ou une case vide. On la rend entière quand, pour ce
    relevé, toutes ses valeurs le sont ; puis un aller-retour CSV refait l'inférence des types."""
    d = _releves()[nom].reset_index(drop=True).copy()
    for c in d.columns:
        col = d[c]
        if col.dtype == float and col.notna().all() and (col == col.round()).all():
            d[c] = col.astype("int64")
    return pd.read_csv(io.StringIO(d.to_csv(index=False)))


def existe(nom):
    return nom in _releves()


def edition(s):
    m = re.search(r"Annuaire statistique de la Tunisie (\d{4}-\d{4})", s)
    return m.group(1) if m else ""


def libelle(s):
    m = re.search(r"ligne « ([^»]+?) »", s)
    return m.group(1).strip() if m else ""


def stade(s):
    reprise = " ; colonne reprise de l'édition 2013-2017" if "reprises telles quelles" in s else ""
    if "antépénultième" in s:
        return "réalisation présumée" + reprise
    if "avant-dernière" in s:
        return "avant-dernière année de l'édition" + reprise
    if "plus récente" in s:
        return "provisoire (dernière année de l'édition)" + reprise
    return ""


def ecrire(slug, df, sources, caveats, note, series=()):
    caveats = list(caveats)
    head = [
        f"# Figure-data du précis socio-fiscal tunisien — généré le {DATE}",
        f"# séries (tunisia_data) : {', '.join(series)}",
        f"# sources (citation) : {', '.join('@' + k for k in sources)}",
        f"# fiches : {FICHE}",
        f"# méthode/hypothèses : {'. '.join(caveats)}",
        f"# note : {note}",
    ]
    (OUT / f"{slug}.csv").write_text("\n".join(head) + "\n" + df.to_csv(index=False), encoding="utf-8")
    side = "series: [{}]\nsources: [{}]\nfiches: [{}]\ncaveats: [{}]\ngenerated: {}\n".format(
        ", ".join(series), ", ".join(sources), FICHE, ". ".join(caveats), DATE)
    (OUT / f"{slug}.csv.yml").write_text(side, encoding="utf-8")


def nb(v, dec=0):
    if pd.isna(v):
        return ""
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")



def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    md = []

    # ---------------------------------------------------------------- 1. ministères (long)
    MIN = [("education", "Éducation"), ("enseignement-superieur", "Enseignement supérieur"),
           ("recherche-scientifique", "Recherche scientifique"),
           ("formation-professionnelle", "Formation professionnelle"), ("emploi", "Emploi")]
    rows = []
    for titre, tab in (("gestion", "16.8"), ("developpement", "16.10")):
        for cle, nom in MIN:
            d = lire(f"{titre}-{cle}")
            for r in d.itertuples():
                rows.append({
                    "Année": int(r.annee), "Ministère": nom, "Libellé imprimé": libelle(r.source),
                    "Périmètre": HORS_TOTAL if cle == "recherche-scientifique" else "",
                    "Titre": "gestion" if titre == "gestion" else "développement",
                    "Montant (milliers D courants)": int(r.valeur),
                    "Montant (milliers D de 2023)": round(r.valeur * IPC23 / ipc[int(r.annee)]),
                    "Stade": stade(r.source), "Édition": edition(r.source),
                    "Tableau": tab, "Page": int(r.page), "Source": r.source})
    mins = pd.DataFrame(rows).sort_values(["Titre", "Ministère", "Année"], ascending=[False, True, True])
    ecrire("fig_educ_depense_ministeres", mins, ["ins-annuaire-statistique", "bct-ra", "ins-annuaire"], [
        "INS, Annuaire statistique de la Tunisie, chapitre 16, tableaux 16.8 (gestion hors intérêts) et 16.10 "
        "(développement hors principal de la dette), source citée : ministère des Finances",
        "pour chaque année, édition la plus récente qui la contient ; stade lu dans la position de l'année "
        "dans l'édition (troisième année ou plus ancienne : réalisation ; dernière : provisoire)",
        "ruptures de périmètre : formation professionnelle comprise dans l'Éducation de 2002 à 2008 et "
        "dans l'Emploi en gestion de 2014 à 2019 ; recherche comprise dans l'Enseignement supérieur "
        "en 2002-2004 et, en gestion, depuis 2019, sans être déduite ; pas de ligne propre de la recherche "
        "de 1997 à 2001 ; développement : changement de périmètre entre 2008 et "
        "2009, deux segments jamais chaînés ; 2017 provisoire, au-dessus du réalisé 2018",
        "lignes de la recherche scientifique (2005-2023) : hors total ; la recherche n'entre dans "
        "aucun total ni aucune part du chapitre, elle n'est pas tracée sur la figure",
        "dinars de 2023 : indice des prix ipc-longue-periode (base 1970), rapport de l'indice 2023 à "
        "celui de l'année"],
        "Dépense de l'État par ministère, gestion et développement, 1997-2023, en milliers de dinars "
        "courants et de 2023", series=["education-depense-ministeres", "ipc-longue-periode"])

    # tableau replié : large
    w = mins.pivot_table(index="Année", columns=["Ministère", "Titre"],
                         values="Montant (milliers D courants)", aggfunc="first")
    g = mins[mins.Titre == "gestion"].groupby("Année").first()
    dv = mins[mins.Titre == "développement"].groupby("Année").first()
    ed = lire("gestion-education")
    cols = [("Éducation", "gestion"), ("Éducation", "développement"),
            ("Enseignement supérieur", "gestion"), ("Enseignement supérieur", "développement"),
            ("Recherche scientifique", "gestion"), ("Recherche scientifique", "développement"),
            ("Formation professionnelle", "gestion"), ("Formation professionnelle", "développement"),
            ("Emploi", "gestion"), ("Emploi", "développement")]
    md.append("## Tableau ministères\n")
    md.append("| Année | Éducation<br>G | Éducation<br>D | Ens. sup.<br>G | Ens. sup.<br>D | Recherche<br>G, hors total | "
              "Recherche<br>D, hors total | Form. prof.<br>G | Form. prof.<br>D | Emploi<br>G | Emploi<br>D | Stade | Édition<br>(p. G / p. D) |")
    md.append("|---|" + "---:|" * 10 + "---|---|")
    for r in ed.itertuples():
        a = int(r.annee)
        vals = []
        for c in cols:
            v = w.loc[a].get(c) if c in w.columns else None
            tiret = (c == ("Formation professionnelle", "gestion") and 2014 <= a <= 2019) or \
                    (c == ("Recherche scientifique", "gestion") and a >= 2019)
            vals.append(nb(v) if v is not None and not pd.isna(v) else ("« - »" if tiret else ""))
        pd_ = int(lire("developpement-education").set_index("annee").loc[a, "page"])
        md.append(f"| {a} | " + " | ".join(vals) + f" | {stade(r.source)} | {edition(r.source)} ({int(r.page)} / {pd_}) |")

    # ---------------------------------------------------------------- 2. parts
    ge, de = lire("gestion-education").set_index("annee"), lire("developpement-education").set_index("annee")
    gs, ds = lire("gestion-enseignement-superieur").set_index("annee"), lire("developpement-enseignement-superieur").set_index("annee")
    gr, dr = lire("gestion-recherche-scientifique").set_index("annee"), lire("developpement-recherche-scientifique").set_index("annee")
    eg, edv = lire("etat-gestion-hors-interets").set_index("annee"), lire("etat-developpement-hors-principal").set_index("annee")
    pe = lire("calcul-part-education-superieur-depenses-etat").set_index("annee")
    pp = lire("calcul-part-education-superieur-pib").set_index("annee")
    rows = []
    for a in range(2009, 2024):
        grv = gr.valeur.get(a)
        den = eg.valeur[a] + edv.valeur[a]
        pib = DENOM.pib_MDT[a] * 1000 if a >= 2010 else None   # milliers de dinars ; 2009 en base 1997, non retenu
        # contrôle de la copie : l'ancien numérateur (recherche comprise) redonne les parts de la note
        ancien = ge.valeur[a] + de.valeur[a] + gs.valeur[a] + ds.valeur[a] + (grv if grv is not None else 0) + dr.valeur[a]
        assert abs(round(100 * ancien / den, 2) - pe.valeur[a]) < 0.011, (a, ancien, pe.valeur[a])
        if pib is not None:
            assert abs(round(100 * ancien / pib, 2) - pp.valeur[a]) < 0.011, (a, ancien, pp.valeur[a])
        # numérateur du chapitre : Éducation + Enseignement supérieur, la recherche hors total
        num = ge.valeur[a] + de.valeur[a] + gs.valeur[a] + ds.valeur[a]
        rows.append({
            "Année": a,
            "Éducation, gestion (milliers D)": int(ge.valeur[a]), "Éducation, développement (milliers D)": int(de.valeur[a]),
            "Ens. supérieur, gestion (milliers D)": int(gs.valeur[a]), "Ens. supérieur, développement (milliers D)": int(ds.valeur[a]),
            "Numérateur (milliers D)": int(num),
            "Périmètre du numérateur": ("hors recherche" if grv is not None else
                                        "recherche de gestion comprise dans l'Ens. supérieur, non isolable ; "
                                        "recherche de développement hors total"),
            "Recherche, gestion, hors total (milliers D)": "" if grv is None else int(grv),
            "Recherche, développement, hors total (milliers D)": int(dr.valeur[a]),
            "État, gestion hors intérêts (milliers D)": int(eg.valeur[a]),
            "État, développement hors principal (milliers D)": int(edv.valeur[a]),
            "Part des dépenses de l'État (%)": round(100 * num / den, 2),
            "PIB nominal (millions D)": "" if pib is None else DENOM.pib_MDT[a],
            "Part du PIB (%)": "" if pib is None else round(100 * num / pib, 2),
            "Base du PIB": pp.unite.get(a, "").replace("% du PIB aux prix courants, ", "") if a in pp.index else "",
            "Stade": stade(ge.source[a]), "Édition": edition(ge.source[a]),
            "Page gestion": int(ge.page[a]), "Page développement": int(de.page[a]),
        })
    parts = pd.DataFrame(rows)
    ecrire("fig_educ_depense_parts", parts, ["ins-annuaire-statistique", "ins-cnat-2015", "minfin-indicateurs-fp"], [
        "numérateur : gestion et développement de l'Éducation et de l'Enseignement supérieur (tableaux 16.8 "
        "et 16.10 de l'Annuaire statistique) ; recherche scientifique exclue ; formation professionnelle exclue",
        "réserve de périmètre : depuis 2019, la recherche n'a plus de ligne de gestion et se trouve comprise "
        "dans la gestion de l'Enseignement supérieur ; elle n'en est pas déduite, faute de source qui l'isole ; "
        "la série change donc de périmètre entre 2018 et 2019, et les deux segments ne sont pas reliés",
        "lignes de la recherche identifiables (gestion 2009-2018, développement 2009-2023) : copiées hors "
        "total, jamais ajoutées au numérateur",
        "part de l'État : dénominateur = dépenses de gestion hors intérêts + dépenses de développement hors "
        "principal, lues aux mêmes pages ; commence en 2009 (rupture du développement entre 2008 et 2009)",
        "part du PIB : PIB nominal de la série denominateurs-depenses-etat-pib (INS, base 2015, années "
        "2010-2014 rétropolées par l'INS) ; le segment antérieur, en base 1997, n'est pas calculé",
        "contrôle : le numérateur de la note documentaire (recherche comprise) redonne ses deux parts à "
        "0,01 point près ; les parts publiées ici sont recalculées hors recherche",
        "2017 provisoire (dernière année de l'édition 2013-2017, reprise par les éditions suivantes) : la "
        "baisse de 2017 à 2018 tient au stade du chiffre"],
        "Part de l'Éducation et de l'Enseignement supérieur, hors recherche, dans les dépenses de l'État "
        "(2009-2023) et dans le PIB en base 2015 (2010-2023)", series=["education-depense-ministeres", "education-depense-parts-calcul",
                                 "denominateurs-depenses-etat-pib"])

    # ---------------------------------------------------------------- 3. nature
    NAT = [("remunerations", "Rémunérations"), ("biens-et-services", "Biens et services"), ("autres-depenses", "Autres dépenses")]
    rows = []
    for cle, nom in MIN[:4]:
        for nc, nn in NAT:
            if not existe(f"nature-{cle}-{nc}"):
                continue
            d = lire(f"nature-{cle}-{nc}")
            for r in d.itertuples():
                rows.append({"Année": int(r.annee), "Ministère": nom, "Libellé imprimé": libelle(r.source),
                             "Périmètre": HORS_TOTAL if cle == "recherche-scientifique" else "",
                             "Nature": nn, "Montant (milliers D courants)": int(r.valeur),
                             "Édition": edition(r.source), "Page": int(r.page), "Source": r.source})
    nat = pd.DataFrame(rows)
    tot = nat.groupby(["Année", "Ministère"])["Montant (milliers D courants)"].agg(["sum", "count"])
    def part(r):
        s, c = tot.loc[(r["Année"], r["Ministère"])]
        return round(100 * r["Montant (milliers D courants)"] / s, 2) if c == 3 else ""
    nat.insert(6, "Part des trois natures (%)", nat.apply(part, axis=1))
    nat = nat.sort_values(["Ministère", "Nature", "Année"])
    ecrire("fig_educ_depense_nature", nat, ["ins-annuaire-statistique", "mineducation-pap-2014"], [
        "INS, Annuaire statistique de la Tunisie, tableau 16.9 « Dépenses du titre I par catégorie et "
        "département » : seule l'année la plus récente de chaque édition y figure, chiffre provisoire",
        "part = montant ÷ somme des trois natures de la même ligne du tableau 16.9 (non ÷ la gestion du "
        "tableau 16.8, d'un autre stade) ; pas de part en 2001, année à quatre colonnes",
        "Éducation : ligne « Education et Formation » de 2003 à 2010 (formation professionnelle comprise) ; "
        "Enseignement supérieur : recherche comprise en 2003 et 2004 (libellé « et recherche scientifique ») ; "
        "en 2006, 2009, 2020, 2022 et 2023, la part de la recherche dans l'Enseignement supérieur n'est pas "
        "établie ; aucune déduction",
        "lignes de la recherche scientifique (2005-2017) : hors total, non tracées",
        "biens et services = moyens des services ; autres dépenses = interventions publiques (PAP 2014)",
        "sauts sans commentaire de la source : autres dépenses de l'Éducation 2016-2017, biens et services "
        "2017-2020 ; reclassements possibles, non confirmés ; années absentes : 2002, 2013, 2018, 2019, 2021"],
        "Dépense de gestion par nature et par ministère, 2001-2023, en milliers de dinars courants et en "
        "parts des trois natures", series=["education-depense-nature"])

    md.append("\n## Tableau nature (Éducation, ES)\n")
    for mn in ["Éducation", "Enseignement supérieur", "Recherche scientifique", "Formation professionnelle"]:
        sub = nat[nat.Ministère == mn]
        md.append(f"\n### {mn}\n")
        md.append("| Année | Libellé imprimé | Rémunérations | Biens et services | Autres dépenses | Édition (p.) |")
        md.append("|---|---|---:|---:|---:|---|")
        for a, grp in sub.groupby("Année"):
            v = {r["Nature"]: r["Montant (milliers D courants)"] for _, r in grp.iterrows()}
            r0 = grp.iloc[0]
            md.append(f"| {a} | « {r0['Libellé imprimé']} » | {nb(v.get('Rémunérations', float('nan')))} | "
                      f"{nb(v.get('Biens et services', float('nan')))} | {nb(v.get('Autres dépenses', float('nan')))} | "
                      f"{r0['Édition']} ({r0['Page']}) |")

    # ---------------------------------------------------------------- 4. enseignants + rémunérations
    rows = []
    for cle, nom in (("enseignants-public-premier-cycle-base", "Enseignants du public, premier cycle de l'enseignement de base"),
                     ("enseignants-public-second-cycle-base-secondaire", "Enseignants du public, second cycle de la base et secondaire"),
                     ("enseignants-public-superieur", "Enseignants du public, enseignement supérieur")):
        d = lire(cle)
        for r in d.itertuples():
            rows.append({"Série": nom, "Période": r.annee, "Valeur": int(r.valeur), "Unité": "enseignants",
                         "Valeur en milliers D de 2023": "", "Édition": edition(r.source), "Page": int(r.page),
                         "Source": r.source})
    for cle, nom in (("nature-education-remunerations", "Rémunérations, ministère de l'Éducation"),
                     ("nature-enseignement-superieur-remunerations", "Rémunérations, ministère de l'Enseignement supérieur")):
        d = lire(cle)
        for r in d.itertuples():
            rows.append({"Série": nom, "Période": str(int(r.annee)), "Valeur": int(r.valeur),
                         "Unité": "milliers de dinars courants",
                         "Valeur en milliers D de 2023": round(r.valeur * IPC23 / ipc[int(r.annee)]),
                         "Édition": edition(r.source), "Page": int(r.page), "Source": r.source})
    # agents de la fonction publique du ministère (INS, base INSAF) : annexes annuelles jusqu'en
    # 2017, rapport d'août 2026 depuis 2018 (l'édition la plus récente pour 2018-2020, où les
    # deux se recouvrent ; l'écart est contrôlé ici et dit dans les réserves)
    agents = {}
    for cle, nom in (("education", "Éducation"), ("enseignement-superieur", "Enseignement supérieur")):
        ann = lire(f"personnels-ins-agents-{cle}-annexes-2010-2020").set_index("annee")
        rec = lire(f"personnels-ins-agents-{cle}-2018-2025").set_index("annee")
        for a in sorted(set(ann.index) & set(rec.index)):
            ecart = int(rec.valeur[a]) - int(ann.valeur[a])
            assert abs(ecart) <= 100, (nom, a, ecart)   # Éducation : 0 ou 1 ; supérieur : 80 ou 81
        serie = {}
        for a, r in ann.iterrows():
            if a < 2018:
                serie[int(a)] = (int(r.valeur), f"2010-2021, annexe {a}", "", r.source, "agents (effectif de l'année)")
        for a, r in rec.iterrows():
            serie[int(a)] = (int(r.valeur), "2018-2025 (août 2026)", str(int(r.page)), r.source, "agents (décembre)")
        agents[nom] = serie
        for a, (v, ed, p, src, u) in sorted(serie.items()):
            rows.append({"Série": f"Agents de la fonction publique, ministère de l'{nom}",
                         "Période": str(a), "Valeur": v, "Unité": u,
                         "Valeur en milliers D de 2023": "", "Édition": ed, "Page": p, "Source": src})
    # rémunération par agent : tableau 16.9 ÷ agents du même ministère, la même année ;
    # Éducation 2010 exclue (le tableau 16.9 y comprend la formation professionnelle)
    for cle, nom in (("nature-education-remunerations", "Éducation"),
                     ("nature-enseignement-superieur-remunerations", "Enseignement supérieur")):
        for r in lire(cle).itertuples():
            a = int(r.annee)
            if a not in agents[nom] or (nom == "Éducation" and a == 2010):
                continue
            n, ed_ag = agents[nom][a][:2]
            courant = r.valeur / n                       # milliers de D par agent
            rows.append({"Série": f"Rémunération par agent, ministère de l'{nom}",
                         "Période": str(a), "Valeur": round(courant, 2),
                         "Unité": "milliers de dinars courants par agent et par an",
                         "Valeur en milliers D de 2023": round(courant * IPC23 / ipc[a], 2),
                         "Édition": f"Annuaire {edition(r.source)} ; agents {ed_ag}", "Page": "",
                         "Source": "calcul du précis : colonne « Rémunération » du tableau 16.9 de l'Annuaire "
                                   "statistique (même année) divisée par les agents de la fonction publique "
                                   "du ministère (INS, base INSAF), lignes de ce tableau"})
    ens = pd.DataFrame(rows)
    ens["Valeur"] = pd.Series([r["Valeur"] for r in rows], dtype=object)   # entiers restent entiers
    ecrire("fig_educ_depense_enseignants", ens, ["ins-annuaire-statistique", "ins-fonction-publique-2021",
                                                  "ins-fonction-publique-2025", "bct-ra", "ins-annuaire"], [
        "effectifs : INS, Annuaire statistique, chapitre « Enseignement et culture », tableau des données "
        "générales de l'enseignement (sources citées : ministères de l'Éducation et de l'Enseignement "
        "supérieur) ; enseignants du public ; une valeur par année scolaire, dans l'édition la plus récente "
        "qui la contient ; révisions entre éditions (second cycle 2009-2010 ; supérieur 2018-2019 à 2020-2021)",
        "rémunérations : colonne « Rémunération » du tableau 16.9, masse salariale de tout le ministère, non "
        "des seuls enseignants ; année la plus récente de chaque édition, chiffre provisoire ; Éducation "
        "2003-2010 avec la formation professionnelle",
        "agents : agents de la fonction publique du ministère, base INSAF (INS) ; annexes annuelles de "
        "l'édition 2010-2021 (effectif de l'année) jusqu'en 2017, rapport d'août 2026 (effectif de décembre) "
        "depuis 2018 ; pour 2018-2020, "
        "où les deux se recouvrent, le rapport d'août 2026 est retenu : il concorde à une unité près pour "
        "l'Éducation et dépasse les annexes de 80 à 81 agents pour l'Enseignement supérieur ; pas de ligne "
        "propre à la formation professionnelle",
        "rémunération par agent : rémunérations du tableau 16.9 divisées par les agents du même ministère "
        "la même année, seulement les années où les deux existent (ni 2013, 2018, 2019, 2021) ; Éducation "
        "2010 exclue, le tableau 16.9 y comprenant la formation professionnelle ; ni rémunération "
        "d'enseignant ni équivalent temps plein",
        "dinars de 2023 : indice des prix ipc-longue-periode (base 1970)"],
        "Enseignants du public par cycle (1995-1996 à 2023-2024), rémunérations des ministères "
        "(2001-2023), agents des ministères (2010-2025) et rémunération par agent (2010-2023)",
        series=["education-effectifs-annuaire", "education-depense-nature",
                "education-personnels-fonction-publique", "ipc-longue-periode"])

    md.append("\n## Tableau enseignants\n")
    e1, e2, e3 = (lire(k).set_index("annee") for k in ("enseignants-public-premier-cycle-base",
                  "enseignants-public-second-cycle-base-secondaire", "enseignants-public-superieur"))
    md.append("| Année scolaire | Premier cycle<br>de la base | Second cycle<br>et secondaire | Supérieur | Édition (p.) |")
    md.append("|---|---:|---:|---:|---|")
    for a in e1.index:
        md.append(f"| {a} | {nb(e1.valeur[a])} | {nb(e2.valeur[a])} | {nb(e3.valeur[a])} | {edition(e1.source[a])} ({int(e1.page[a])}) |")

    # ---------------------------------------------------------------- 5. UIS
    rows = []
    for cle, ind in (("rapport-uis-depense-education-pct-pib", "SE.XPD.TOTL.GD.ZS"),
                     ("rapport-uis-depense-education-pct-depenses-publiques", "SE.XPD.TOTL.GB.ZS"),
                     ("rapport-uis-depense-par-eleve-primaire-pct-pib-hab", "SE.XPD.PRIM.PC.ZS"),
                     ("rapport-uis-depense-par-eleve-secondaire-pct-pib-hab", "SE.XPD.SECO.PC.ZS"),
                     ("rapport-uis-depense-par-etudiant-superieur-pct-pib-hab", "SE.XPD.TERT.PC.ZS")):
        d = lire(cle)
        for r in d.itertuples():
            rows.append({"Famille": "rapport extérieur (UNESCO-UIS, par la Banque mondiale)", "Indicateur": ind,
                         "Année": int(r.annee), "Valeur": round(r.valeur, 2), "Unité": r.unite,
                         "Page": "", "Source": r.source})
    for col, ind, unite in (("Part du PIB (%)", "part du PIB (base 2015)",
                             "% du PIB aux prix courants, base 2015 (2010-2014 rétropolés par l'INS)"),
                            ("Part des dépenses de l'État (%)", "part des dépenses de l'État",
                             "% des dépenses de gestion et de développement de l'État hors dette")):
        for a, v in zip(parts["Année"], parts[col]):
            if v == "":
                continue
            rows.append({"Famille": "budgétaire (Annuaire statistique de l'INS ; Éducation et Enseignement supérieur, hors recherche)",
                         "Indicateur": ind, "Année": int(a), "Valeur": v, "Unité": unite,
                         "Page": "voir la part budgétaire de l'Éducation et de l'Enseignement supérieur",
                         "Source": "calcul du précis, part budgétaire de l'Éducation et de l'Enseignement supérieur (recherche hors total ; "
                                   "comprise dans la gestion de l'Enseignement supérieur depuis 2019, non isolable)"})
    uis = pd.DataFrame(rows)
    ecrire("fig_educ_depense_uis", uis, ["wb-wdi", "ins-annuaire-statistique"], [
        "UNESCO-UIS par les World Development Indicators de la Banque mondiale (API consultée le "
        "17 octobre 2026, mise à jour du 8 octobre 2026) : dépense des administrations publiques "
        "(centrales, régionales, locales), courante, en capital et en transferts, y compris les transferts "
        "reçus de l'étranger ; base du PIB non précisée par la source",
        "zéros de SE.XPD.TOTL.GB.ZS pour 1981-1986, 1990 et 1991 (absence de donnée) exclus",
        "valeurs UIS arrondies au centième",
        "la part budgétaire superposée est celle de l'Éducation et "
        "Enseignement supérieur, recherche hors total (comprise dans la gestion du supérieur depuis 2019, "
        "non isolable), PIB en base 2015 (2010-2014 rétropolés par l'INS) ; périmètres différents, familles distinctes"],
        "Dépense publique d'éducation selon l'UNESCO-UIS, en part du PIB et des dépenses publiques, et "
        "par élève en part du PIB par habitant, avec la part budgétaire superposée",
        series=["education-uis-depense", "education-depense-ministeres"])

    md.append("\n## Programmes\n")
    for cle, nom in (("programme-education-primaire", "P1 primaire"), ("programme-education-preparatoire-secondaire", "P2 prep-sec"),
                     ("programme-education-pilotage", "P3 pilotage"), ("programme-esrs-enseignement-superieur", "ES P1"),
                     ("programme-esrs-recherche-scientifique", "ES P2"), ("programme-esrs-services-universitaires", "ES P3"),
                     ("programme-esrs-pilotage", "ES P4"), ("programme-fpe-formation-professionnelle", "FPE")):
        d = lire(cle)
        md.append(f"| {nom} | " + " | ".join(f"{nb(r.valeur)} | {nb(r.valeur * IPC23 / ipc[int(r.annee)])}" for r in d.itertuples()) + f" | p. {d.page.iloc[0]} |")
    md.append("\n## Ménages\n")
    a = lire("menages-depense-education-par-personne"); b = lire("menages-coefficient-budgetaire-education")
    for r, q in zip(a.itertuples(), b.itertuples()):
        md.append(f"| {r.annee} | {nb(r.valeur)} | {nb(r.valeur * IPC23 / ipc[int(r.annee)])} | {nb(q.valeur, 1)} % |")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text("\n".join(md) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

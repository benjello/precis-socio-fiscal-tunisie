"""Recoupe le périmètre de consolidation d'un groupe bancaire avec les participations de ses comptes
INDIVIDUELS, et contrôle que ses comptes CONSOLIDÉS bouclent (règles de somme).

Deux questions, deux outils (voir docs/notes/bh-filiales-renommage… et le rapport produit ici) :
  - « les chiffres sont-ils bien recopiés ? »  -> règles de somme sur le bilan et le résultat consolidés
    (actif = passif + minoritaires + capitaux propres ; cascade du résultat). Une somme qui casse = une
    ligne mal lue.
  - « a-t-on toutes les filiales ? »           -> recoupement du périmètre consolidé avec la liste des
    participations des comptes individuels de la mère, et test du seuil de 50 % : une société détenue à
    plus de 50 % absente du périmètre est un trou, à moins qu'elle ne soit provisionnée (sinistrée, exclue).

    uv run python scripts/recoupement_perimetre_participations.py           # STB, écrit le rapport et le relevé
    uv run python scripts/recoupement_perimetre_participations.py --check   # vérifie que les sommes bouclent (tests)

Écrit dans docs/exemples-soes/ :
  recoupement-perimetre-stb.md                 rapport lisible (comptes consolidés, contrôles de somme, recoupement)
  recoupement-perimetre-participations.csv     le relevé (une ligne par participation : part, consolidée ?, verdict)

Les PDF (comptes individuels et consolidés) sont sous tunisia-data/data/raw/entreprises-publiques/
bvmt-etats-financiers/<banque>/, hors git. Rien n'est saisi à la main : tout est lu au PDF.
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-etats-financiers"
)
PERIMETRE = RACINE / "precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv"
SORTIE = RACINE / "docs/exemples-soes"

# (groupe, exercice, fichier individuel, fichier consolidé, lecteur des participations)
DOCUMENTS = [
    ("STB", 2019, "stb/2019_individuel.pdf", "stb/2019_consolide.pdf", "stb"),
    ("BH", 2016, "bh-bank/2016_individuel.pdf", "bh-bank/2016_consolide.pdf", "bh"),
    ("BH", 2021, "bh-bank/2021_individuel.pdf", "bh-bank/2021_consolide.pdf", "bh"),
    ("BNA", 2020, "bna/2020_individuel.pdf", "bna/2020_consolide.pdf", "bna"),
    ("BNA", 2021, "bna/2021_individuel.pdf", "bna/2021_consolide.pdf", "bna"),
]

# Noms des participations (comptes individuels) rapprochés des entités du périmètre consolidé,
# quand la clé normalisée ne suffit pas (abréviations, variantes orthographiques). L'alias s'applique
# aux deux côtés (participation ET périmètre), donc il suffit de ramener les deux formes à une clé commune.
ALIAS = {
    "LAGENERALEDEVENTE": "LAGENERALEDESVENTES",            # STB : « DE VENTE » vs « DES VENTES »
    "SIFIB": "BHINVEST",                                   # BH : « Société SIFIB » renommée « BH Invest » (cf. conventions « BH Invest (Ex SIFIB) »)
    "SICAVBHOBLIGATAIRE": "SICAVBHOBLIGATOIRE",            # BH : « Obligataire » (individuel) vs « Obligatoire » (périmètre 2016/2017)
    "ASSURANCESSALIM": "ASSURANCESALIM",                   # BH : « Assurances SALIM » (individuel) vs « Assurance SALIM » (périmètre)
    "GENERALEDESVENTES": "GENERALEDEVENTE",                # BNA : « GENERALE DES VENTES » (individuel) vs « GENERALE DE VENTE » (périmètre)
}


def texte(chemin: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(chemin), "-"], capture_output=True, text=True, check=True
    ).stdout


def cle(nom: str) -> str:
    """Clé de rapprochement : contenu entre guillemets s'il y en a, sinon le nom sans « Société/STE » ni
    article « L' » en tête, en majuscules, sans accents ni ponctuation. Les apostrophes (droite et courbe)
    sont remplacées par une espace AVANT la réduction en ASCII, pour que « L’IMMOBILIERE » ne colle pas."""
    guillemets = re.search(r"[«\"“]\s*(.+?)\s*[»\"”]", nom)
    texte_ = re.sub(r"[’'`]", " ", guillemets.group(1) if guillemets else nom)
    brut = unicodedata.normalize("NFKD", texte_).encode("ascii", "ignore").decode().upper().strip()
    if not guillemets:
        brut = re.sub(r"^(SOCIETE|STE)\b\s*", "", brut)
        brut = re.sub(r"^L\s+", "", brut)
    k = re.sub(r"[^A-Z0-9]", "", brut)
    return ALIAS.get(k, k)


def entier(valeur: str) -> int:
    """« 11 406 843 » -> 11406843 ; « (891) » -> -891."""
    v = valeur.strip().replace(" ", "")
    negatif = v.startswith("(") and v.endswith(")")
    v = v.strip("()")
    return -int(v) if negatif else int(v)


def ligne_chiffree(contenu: str, libelle: str) -> int | None:
    """Premier nombre de colonne (exercice N) de la ligne qui COMMENCE par `libelle`. Les montants sont en
    format français (espace = séparateur de milliers), et selon les PDF les deux colonnes (N, N-1) ne sont
    séparées que par une seule espace : un nombre se lit donc « 1-3 chiffres puis des groupes de 3 », ce qui
    évite de coller N et N-1. On écarte un code de note (« 6.14 », ou « 12 » isolé devant ≥ 2 colonnes) et
    les renvois (« (*) »)."""
    nombre = re.compile(r"\(?-?\d{1,3}(?: \d{3})*\)?")
    for ligne in contenu.splitlines():
        depouille = ligne.strip()
        if not depouille.startswith(libelle):
            continue
        reste = re.sub(r"\d{1,2}\.\d{1,2}", " ", depouille[len(libelle):])  # codes de note « 6.14 »
        jetons = [m.group() for m in nombre.finditer(reste) if re.search(r"\d", m.group())]
        if len(jetons) > 2 and re.fullmatch(r"\d{1,2}", jetons[0]):  # code de note « 12 » en tête
            jetons = jetons[1:]
        if jetons:
            return entier(jetons[0])
    return None


# --- Lecteurs des participations (comptes individuels) ------------------------------------------


def participations_stb(contenu: str) -> list[dict]:
    """Note « liste des principales entreprises filiales » : secteur, nom, % détenu par la STB,
    valeurs brute/provision/nette. Une filiale dont la valeur nette est nulle est provisionnée à 100 %."""
    debut = contenu.lower().find("principales entreprises filiales")
    if debut < 0:
        return []
    fin = contenu.find("Les résultats et les capitaux propres", debut)
    fenetre = contenu[debut : fin if fin > debut else debut + 2600]
    motif = re.compile(r"^ *(.+?)\s{2,}(\d{1,3}[ .,]\d{2})\s*%\s+(.+)$")
    res, secteur = [], ""
    for ligne in fenetre.splitlines():
        depouille = ligne.strip()
        if depouille.isupper() and "%" not in depouille and not re.search(r"\d", depouille):
            secteur = depouille.replace("SECTEUR ", "").title()
            continue
        trouve = motif.match(ligne)
        if not trouve:
            continue
        nom = " ".join(trouve.group(1).split())
        pct = float(trouve.group(2).replace(" ", ".").replace(",", "."))
        nombres = [
            entier(x) for x in re.split(r"\s{2,}", trouve.group(3).strip()) if re.fullmatch(r"[\d ]+", x)
        ]
        brute = nombres[0] if nombres else None
        net = nombres[-1] if len(nombres) >= 2 else None
        res.append({"secteur": secteur, "entite": nom, "pct": pct, "brute": brute, "net": net})
    return res


def pourcentages_filiales_bh(contenu: str) -> dict[str, float]:
    """% de détention lus dans la note « Liste des entreprises filiales » (présente en 2016 et 2017),
    indexés par clé de rapprochement. Les lignes dont le % est reporté sur une ligne de continuation
    (adresse) ne sont pas captées : sans conséquence, ces filiales figurent au périmètre consolidé."""
    debut = contenu.lower().find("liste des entreprises filiales")
    if debut < 0:
        return {}
    pcts = {}
    for ligne in contenu[debut : debut + 3500].splitlines():
        m = re.match(r"^(\S.*?)\s{2,}.*?(\d{1,3}[.,]\d{2})\s*%", ligne)
        if m:
            pcts[cle(" ".join(m.group(1).split()))] = float(m.group(2).replace(",", "."))
    return pcts


def participations_bh(contenu: str) -> list[dict]:
    """Note « participations dans les parties liées » : nom puis colonnes Brut/Prov/Net de l'exercice N
    (puis N-1). Le % de détention, quand il existe, est lu dans la note « Liste des entreprises filiales »
    (2016/2017 seulement ; absente à partir de 2021). Valeur nette nulle et brute positive = provisionnée à 100 %."""
    debut = contenu.lower().find("participations dans les parties liées")
    if debut < 0:
        return []
    fin = contenu.find("Total", debut + 60)
    fenetre = contenu[debut : fin if fin > debut else debut + 2000]
    pcts = pourcentages_filiales_bh(contenu)
    res = []
    for ligne in fenetre.splitlines():
        m = re.match(r"^(\S.*?)\s{2,}(.+)$", ligne.rstrip())
        if not m:
            continue
        nom = " ".join(m.group(1).split())
        if nom.lower().startswith(("total", "participations")):
            continue
        nums = []
        for jeton in re.split(r"\s{2,}", m.group(2).strip()):
            j = jeton.strip()
            if j in {"-", "–", "—"}:
                nums.append(0)
            elif re.fullmatch(r"\(?-?[\d ]+\)?", j):
                nums.append(entier(j))
            else:
                nums = None
                break
        if not nums or len(nums) < 3:
            continue
        res.append({"secteur": "", "entite": nom, "pct": pcts.get(cle(nom)),
                    "brute": nums[0], "net": nums[2]})
    return res


def participations_bna(contenu: str) -> list[dict]:
    """Note « portefeuille titres d'investissement » : chaque participation avec son % de détention puis
    des colonnes chiffrées (brute N-1, acquisitions, cessions, brute N, provisions, nette N). Valeur nette
    nulle et brute positive = provisionnée à 100 %. Les lignes de sous-total (sans %) sont ignorées."""
    ancre = re.search(r"portefeuille titres d.investissement se détaill", contenu, re.I)
    if not ancre:
        return []
    debut = ancre.start()
    fin = contenu.find("Les résultats et les capitaux propres", debut)
    fenetre = contenu[debut : fin if fin > debut else debut + 6000]
    motif = re.compile(r"^ *(\S.*?)\s{2,}(\d{1,3}(?:[ .,]\d{1,2})?)\s*%\s+(.+)$")
    res = []
    for ligne in fenetre.splitlines():
        trouve = motif.match(ligne)
        if not trouve:
            continue
        nom = " ".join(trouve.group(1).split())
        pct = float(trouve.group(2).replace(" ", ".").replace(",", "."))
        nums = []
        for jeton in re.split(r"\s{2,}", trouve.group(3).strip()):
            j = jeton.strip()
            if j in {"-", "–", "—", ""}:
                nums.append(0)
            elif re.fullmatch(r"\(?-?[\d ]+\)?", j):
                nums.append(entier(j))
        if not nums:
            continue
        res.append({"secteur": "", "entite": nom, "pct": pct, "brute": nums[0], "net": nums[-1]})
    return res


LECTEURS = {"stb": participations_stb, "bh": participations_bh, "bna": participations_bna}


# --- Recoupement et contrôles de somme ----------------------------------------------------------


def perimetre_consolide(groupe: str, exercice: int) -> dict[str, dict]:
    """Entités du périmètre consolidé (hors mère) pour un exercice, indexées par clé de rapprochement."""
    out = {}
    with PERIMETRE.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["groupe"] == groupe and r["exercice"] == str(exercice) and r["methode"] != "mère":
                out[cle(r["entite"])] = r
    return out


def recouper(parts: list[dict], perim: dict[str, dict]) -> list[dict]:
    """Verdict par participation. Le test du seuil de 50 % ne vaut que si la filiale n'est pas provisionnée."""
    lignes = []
    for p in parts:
        entree = perim.get(cle(p["entite"]))
        pct = p["pct"]
        provisionnee = p["net"] == 0 and (p["brute"] or 0) > 0
        if entree:
            verdict = f"consolidée ({entree['methode']})"
        elif pct is not None and pct <= 50:
            # détenue à 50 % ou moins : pas vocation à être consolidée. La provision éventuelle touche sa
            # valeur, pas le périmètre : c'est un placement minoritaire, jamais un trou.
            verdict = "détenue ≤ 50 % et non consolidée"
        elif provisionnee:
            prefixe = "détenue > 50 % mais " if (pct or 0) > 50 else ""
            verdict = f"{prefixe}exclue (participation provisionnée à 100 %)"
        elif pct is None:
            verdict = "part non renseignée et ABSENTE du périmètre — à vérifier"
        else:
            verdict = "détenue > 50 % et ABSENTE du périmètre — à expliquer"
        lignes.append({**p, "consolidee": bool(entree),
                       "methode": entree["methode"] if entree else "",
                       "provisionnee": provisionnee, "verdict": verdict})
    return lignes


def controles_somme(cons: str) -> list[tuple[str, int, int]]:
    """Règles de somme sur le bilan et le résultat consolidés. Rend (intitulé, calcul, imprimé). Les
    intitulés varient d'une banque à l'autre (STB, BH, BNA) : on essaie plusieurs libellés par grandeur.
    Les minoritaires du résultat étant tantôt imprimés positifs (STB), tantôt négatifs (BNA), on prend
    leur valeur absolue : part du groupe = résultat net − |minoritaires|."""
    def g(*libelles):
        for lib in libelles:
            v = ligne_chiffree(cons, lib)
            if v is not None:
                return v
        return None
    verifs = []
    actifs, passifs = g("Total des actifs"), g("Total des passifs")
    minos = g("Intérêts Minoritaires", "IM - Intérêts Minoritaires")
    cp = g("Total des Capitaux propres")
    cp_passifs = g("Total des capitaux propres et passifs")
    if None not in (passifs, minos, cp, cp_passifs):
        verifs.append(("Passifs + minoritaires + capitaux propres = total", passifs + minos + cp, cp_passifs))
    if None not in (actifs, cp_passifs):
        verifs.append(("Total actifs = total capitaux propres et passifs", actifs, cp_passifs))
    res_ex = g("Résultat net de l'exercice")
    mino_res = g("Intérêts minoritaires dans le résultat", "Intérêts minoritaires")
    part_groupe = g("Résultat Net consolidé part du groupe", "Résultat net de l'exercice, Part du groupe")
    if None not in (res_ex, mino_res, part_groupe):
        verifs.append(("Résultat net − minoritaires = part du groupe", res_ex - abs(mino_res), part_groupe))
    return verifs


# --- Rapport ------------------------------------------------------------------------------------


def md(n: int | None) -> str:
    return "—" if n is None else f"{n/1000:,.1f}".replace(",", " ").replace(".", ",")


def rapport(groupe: str, exercice: int, cons: str, lignes: list[dict],
            verifs: list[tuple[str, int, int]], perim: dict[str, dict]) -> str:
    def g(*libelles):
        for lib in libelles:
            v = ligne_chiffree(cons, lib)
            if v is not None:
                return v
        return None
    L = [f"# Recoupement du périmètre de consolidation — {groupe}, {exercice}", "",
         "Document produit par `scripts/recoupement_perimetre_participations.py` (rien saisi à la main ; "
         "tout est lu aux PDF des comptes individuels et consolidés de la banque, conservés hors git). "
         "Il répond à deux questions distinctes.", ""]

    res_net = md(g("Résultat net de l'exercice"))
    part_grp = md(g("Résultat Net consolidé part du groupe", "Résultat net de l'exercice, Part du groupe"))
    L += ["## 1. Les chiffres consolidés sont-ils cohérents ? (règles de somme)", "",
          "Un bilan consolidé doit s'équilibrer ; le résultat doit se décomposer. Une somme qui casse "
          "trahit une ligne mal lue. En millions de dinars :", "",
          "| Grandeur | Valeur |", "|---|---:|",
          f"| Total des actifs | {md(g('Total des actifs'))} |",
          f"| Produit net bancaire | {md(g('Produit Net Bancaire', 'Total Produit net bancaire'))} |",
          f"| Résultat net de l'exercice | {res_net} |",
          f"| dont intérêts minoritaires | {md(g('Intérêts minoritaires dans le résultat', 'Intérêts minoritaires'))} |",
          f"| **Résultat net consolidé part du groupe** | **{part_grp}** |",
          ""]
    L += ["| Règle de somme | Calcul | Imprimé | |", "|---|---:|---:|:--|"]
    for intitule, calc, imprime in verifs:
        ok = "✅" if calc == imprime else f"❌ écart {calc - imprime:+,}"
        L.append(f"| {intitule} | {calc:,} | {imprime:,} | {ok} |".replace(",", " "))
    tout_ok = all(c == i for _, c, i in verifs)
    L += ["", f"**{'Toutes les règles bouclent' if tout_ok else 'Une règle casse'} : l'extraction est "
          f"{'fidèle au PDF' if tout_ok else 'à revoir'}.** Ces règles valident la *recopie*, non la "
          "sincérité des comptes (travail des commissaires aux comptes).", ""]

    L += ["## 2. A-t-on toutes les filiales ? (recoupement + seuil de 50 %)", "",
          "On confronte le périmètre consolidé à la liste des participations des comptes **individuels** "
          "de la mère. Toute société détenue à plus de 50 % doit être consolidée — sauf exclusion motivée "
          "(filiale sinistrée, provisionnée à 100 %, en liquidation).", "",
          "| Participation (comptes individuels) | Secteur | Part mère | Au périmètre consolidé ? | Verdict |",
          "|---|---|---:|:--|:--|"]
    # On ne détaille que l'essentiel : entités consolidées, détentions > 50 % et parts non renseignées.
    # Les placements minoritaires (≤ 50 %) non consolidés, normaux, sont résumés en une ligne.
    saillantes = [x for x in lignes if x["consolidee"] or (x["pct"] or 0) > 50 or x["pct"] is None]
    mineures = [x for x in lignes if x not in saillantes]
    for x in sorted(saillantes, key=lambda x: (not x["consolidee"], -(x["pct"] or 0))):
        coche = "oui — " + x["methode"] if x["consolidee"] else "**non**"
        part = "n.d." if x["pct"] is None else f"{x['pct']:.2f} %"
        L.append(f"| {x['entite']} | {x['secteur']} | {part} | {coche} | {x['verdict']} |")
    if mineures:
        prov = sum(x["provisionnee"] for x in mineures)
        L.append(f"| *(+ {len(mineures)} participations minoritaires ≤ 50 %, non consolidées — normal, "
                 f"dont {prov} provisionnées à 100 %)* | | | | |")
    manquantes = [x for x in lignes if not x["consolidee"] and (x["pct"] or 0) > 50]
    L += ["", f"**Bilan : {len(lignes)} participations listées, "
          f"{sum(x['consolidee'] for x in lignes)} au périmètre consolidé, "
          f"{len(manquantes)} détenue(s) à plus de 50 % hors périmètre.**"]
    for x in manquantes:
        L.append(f"- {x['entite']} ({x['pct']:.2f} %) : {x['verdict']}.")
    non_rens = [x for x in lignes if not x["consolidee"] and x["pct"] is None and not x["provisionnee"]]
    for x in non_rens:
        L.append(f"- {x['entite']} : {x['verdict']} (% de détention non publié dans la note individuelle).")
    L += ["", "## Ce qu'on en retient", "",
          "La règle de somme (partie 1) ne prouve jamais la complétude : un bilan boucle même s'il manque "
          "une filiale. La complétude se prouve par le recoupement (partie 2). Ici il exhibe des sociétés "
          "contrôlées par l'État qui n'apparaissent **ni** au périmètre consolidé **ni**, a fortiori, dans "
          "la liste des entreprises publiques du ministère. **L'information requise pour chaque groupe : la "
          "note des participations des comptes individuels (part détenue) et la note d'exclusion du "
          "périmètre (motif).** Sans elles, on ne peut pas affirmer tenir toutes les entités contrôlées.", ""]
    return "\n".join(L)


def main(arguments: list[str]) -> int:
    verifier = "--check" in arguments
    SORTIE.mkdir(parents=True, exist_ok=True)
    relevé = []
    souci = 0
    for groupe, exercice, f_ind, f_cons, lecteur in DOCUMENTS:
        ind, cons = texte(DONNEES / f_ind), texte(DONNEES / f_cons)
        parts = LECTEURS[lecteur](ind)
        perim = perimetre_consolide(groupe, exercice)
        lignes = recouper(parts, perim)
        verifs = controles_somme(cons)
        for intitule, calc, imprime in verifs:
            if calc != imprime:
                souci += 1
                print(f"{groupe} {exercice} — SOMME FAUSSE : {intitule} ({calc} ≠ {imprime})", file=sys.stderr)
        if not verifier:
            (SORTIE / f"recoupement-perimetre-{groupe.lower()}.md").write_text(
                rapport(groupe, exercice, cons, lignes, verifs, perim), encoding="utf-8")
        for x in lignes:
            relevé.append({"groupe": groupe, "exercice": exercice, "entite": x["entite"],
                           "secteur": x["secteur"],
                           "part_mere_pct": "" if x["pct"] is None else f"{x['pct']:.2f}",
                           "valeur_nette_provisionnee": "oui" if x["provisionnee"] else "non",
                           "consolidee": "oui" if x["consolidee"] else "non",
                           "methode": x["methode"], "verdict": x["verdict"]})
    if not verifier:
        with (SORTIE / "recoupement-perimetre-participations.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(relevé[0].keys()))
            w.writeheader()
            w.writerows(relevé)
        print(f"Écrit : {len(DOCUMENTS)} rapport(s) et {len(relevé)} lignes de relevé dans {SORTIE}")
    return 1 if souci else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

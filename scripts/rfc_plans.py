"""Engendre les deux plans détaillés de la RFC 0001 et leur table de correspondance.

    uv run python scripts/rfc_plans.py
Sorties : docs/rfc/plan-a-comptes.md, docs/rfc/plan-b-thematique.md, docs/rfc/correspondance-plans.csv.

Statut d'une entrée, établi sur les fichiers de l'ouvrage, jamais supposé :
  existe     — le fichier de la section ou du chapitre existe et ne porte pas de marque d'ébauche ;
  ébauche    — il porte « ébauche », « BROUILLON » ou n'a pas de section de niveau 2 ;
  à rédiger  — la section porte « À rédiger » ;
  inexistant — aucune section de l'ouvrage n'y répond (proposition de la RFC).
Montants : comptes des secteurs de l'INS (cache `cnat-secteurs`), dernière édition, dernière année définitive.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rfc_tables as T  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
FR = RACINE / "precis" / "fr"
CACHE = RACINE / "precis" / "_seriescache"
RFC = RACINE / "docs" / "rfc"
TITRE2 = re.compile(r"^##\s+(.*?)\s*(?:\{#([^}\s]+)[^}]*\})?\s*$")
EBAUCHE = re.compile(r"ébauche|BROUILLON", re.I)

PARTIES_A = [
    ("A1", "Le compte de production", ["Compte de production", "Production ou Compte extérieur Biens & Services"]),
    ("A2", "Le compte d'exploitation", ["Compte d'exploitation"]),
    ("A3", "Le compte d'affectation des revenus primaires", ["Compte d'affectation des revenus primaires"]),
    ("A4", "Le compte de distribution secondaire du revenu", ["Compte de distribution secondaire du revenu"]),
    ("A5", "Le compte de redistribution du revenu en nature", []),
    ("A6", "Le compte d'utilisation du revenu", ["Compte d'utilisation du revenu disponible"]),
    ("A7", "Le compte de capital", ["Compte de capital"]),
    ("A8", "Le compte financier", ["Compte financier"]),
    ("A9", "Le reste du monde", ["Compte extérieur Biens & Services"]),
    ("A10", "L'équilibre des produits (tableau ressources-emplois)", []),
    ("A11", "La synthèse et les agrégats", []),
]
PROPOSITIONS_A = {
    "A5": [("D.63", "Transferts sociaux en nature", "publié dans un tableau à part des comptes des secteurs (éd. 2021-2025, p. 114) : 15 104,2 MD en 2023, dont 14 604,2 versés par les administrations publiques")],
    "A10": [("TRE", "Ressources et emplois par produit (production, importations, marges, impôts, consommations intermédiaires, emplois finals)", "tableau publié ; extrait dans le dépôt de données")],
    "A11": [("B.1*g", "Produit intérieur brut", "annexe sur le PIB"), ("B.5", "Solde des revenus primaires et revenu national", "à rédiger"),
            ("B.6/B.7", "Revenu disponible brut et ajusté", "à rédiger"), ("—", "Comptes de patrimoine", "l'INS ne publie que des comptes de patrimoine financiers (base 2015, vol. B de l'édition 2015-2020), pas de comptes de patrimoine non financiers (annexe des comptes de la nation)"),
            ("—", "Comptes régionaux", "proposition")],
}
PARTIES_B = [
    ("B1", "Le cadre", ["cadre"], ["Les acteurs (institutions)", "Mode d'emploi des comptes"]),
    ("B2", "La production", ["agriculture", "industrie", "energie", "logement", "transport", "entreprises_publiques"],
     ["Les services (commerce, tourisme, télécommunications)", "Le secteur financier"]),
    ("B3", "L'emploi et les revenus", ["marche_travail", "remunerations_publiques", "informel"], ["Les revenus des indépendants", "Les revenus du capital"]),
    ("B4", "Les prélèvements", ["fiscalite", "cotisations_sociales"], []),
    ("B5", "La protection sociale et les services publics", ["prestations_sociales", "retraites", "caisses", "sante", "education", "compensation", "environnement"],
     ["Le chômage (par renvoi au marché du travail)", "La pauvreté et les niveaux de vie"]),
    ("B6", "La consommation, l'investissement et les échanges", ["consommation", "investissement", "echanges"], []),
    ("B7", "Les finances publiques et la vue d'ensemble", ["finances_locales", "synthese"],
     ["Le budget de l'État (annexe existante)", "La dette publique (annexe existante)", "La monnaie et le crédit", "Le patrimoine public", "Les comptes reconstruits (pages existantes)"]),
]
CAS_B = {"remunerations_publiques": "cas discuté : revenus du travail ou finances publiques", "compensation": "cas discuté : protection sociale ou production",
         "caisses": "cas discuté : prélèvements ou protection sociale", "environnement": "cas discuté : production ou services publics",
         "entreprises_publiques": "cas discuté : à scinder (statut et relation financière en B7, activité par branche en B2)",
         "transport": "rangé avec les services"}


def lire(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def chapitres(v: str) -> list[str]:
    q = FR / v / "_quarto.yml"
    return [f for f in re.findall(r"([_a-z0-9-]+)\.qmd", lire(q)) if f not in ("_glossaire", "_references")]


def sections(qmd: Path) -> list[tuple[str, str, str]]:
    """(titre, ancre, statut) des sections de niveau 2 d'un chapitre."""
    t = lire(qmd)
    out, code, cur = [], False, None
    for l in t.splitlines():
        if l.startswith("```"):
            code = not code
        m = None if code else TITRE2.match(l)
        if m:
            cur = [m.group(1), m.group(2) or "", "existe"]
            out.append(cur)
        elif cur and re.match(r"^À rédiger", l.strip()):
            cur[2] = "à rédiger"
    if EBAUCHE.search(t[:3000]):
        for s in out:
            s[2] = "ébauche" if s[2] == "existe" else s[2]
    return [tuple(s) for s in out]


def statut_chapitre(qmd: Path) -> str:
    t = lire(qmd)
    if not t:
        return "inexistant"
    if EBAUCHE.search(t[:3000]) or not any(TITRE2.match(l) for l in t.splitlines()):
        return "ébauche"
    return "à rédiger" if re.search(r"^À rédiger", t, re.M) else "existe"


def op_de_section(v: str, f: str, titre: str) -> str:
    op = (T.INDEX.get(v) if f == "index" else T.CHAPITRES.get((v, f))) or "à déterminer"
    if op == T.S:
        op = next((o for m, o in T.SECTIONS if re.search(m, titre, re.I)), "à déterminer")
    return op


def mode(op: str) -> str:
    for ops, s, c, m, j in T.REGLES:
        if op in ops and (s is None or s == "apu" or (isinstance(s, tuple) and "apu" in s)):
            return m
    return T.AD


def fr(v) -> str:
    return f"{v:,.1f}".replace(",", " ").replace(".", ",")


def main() -> int:
    vols = [v.parent.name for v in sorted(FR.glob("*/_quarto.yml"))]
    toutes = []  # (volume, chapitre, titre, ancre, statut, opération)
    for v in vols:
        for f in chapitres(v):
            q = FR / v / f"{f}.qmd"
            for titre, ancre, st in sections(q) or [(f, "", statut_chapitre(q))]:
                toutes.append((v, f, titre, ancre, st, op_de_section(v, f, titre)))
    for q in sorted(FR.glob("*.qmd")):  # pages générales (annexes, comptes reconstruits)
        for titre, ancre, st in sections(q):
            toutes.append((q.stem, "", titre, ancre, st, "transversal"))
    postes = list(csv.DictReader((FR / "postes-comptables.csv").open(encoding="utf-8")))
    cache = [l for l in csv.DictReader((CACHE / "cnat-secteurs.csv").open(encoding="utf-8")) if str(l["base"]) == "2015"]
    defin = [l for l in cache if l["statut_annee"] == "definitif"]
    ed = max(l["edition"] for l in defin)
    an = max(int(l["annee"]) for l in defin if l["edition"] == ed)
    lig = [l for l in cache if l["edition"] == ed and int(l["annee"]) == an and l["sous_ligne"] == "0"]
    # opérations par compte : montant des secteurs résidents (emplois, sinon ressources) et part du compte
    ops = defaultdict(lambda: {"emplois": 0.0, "ressources": 0.0, "lib": "", "code": ""})
    for l in lig:
        if l["secteur"] in ("snf", "sf", "apu", "menages") and l["code_scn2008"]:
            k = (l["compte"], l["code_scn2008"], l["operation"])
            ops[k][l["cote"]] += float(l["valeur"])
            ops[k]["lib"] = ops[k]["lib"] or l["libelle_ins"]
            ops[k]["code"] = l["code_scn2008"]
    # Une opération par (compte, code) : la plus grande ; les autres du même code sont ses composantes (« dont »).
    partie_de = {c: pid for pid, _, comptes in PARTIES_A for c in comptes}
    groupes = defaultdict(list)
    for k, x in ops.items():
        groupes[(partie_de.get(k[0], k[0]), k[1])].append((k, x))
    dont = {}
    for g, ls in groupes.items():
        ls.sort(key=lambda kx: -max(abs(kx[1]["emplois"]), abs(kx[1]["ressources"])))
        for k, x in ls[1:]:
            ops.pop(k)
            for c in ("emplois", "ressources"):
                if k[2] == ls[0][0][2]:
                    ops[ls[0][0]][c] += x[c]
        dont[ls[0][0]] = [x["lib"] for k, x in ls[1:]]
    lignes_a, stat_a = [], Counter()
    out = [f"# Plan A : par les comptes (engendré par `scripts/rfc_plans.py`)\n",
           f"Montants : comptes des secteurs de l'INS, éd. {ed}, année {an} (dernière année définitive), somme des quatre secteurs résidents, en millions de dinars courants. "
           "Part : part de l'opération dans le total du même compte et du même côté. Mode : mode de reconstruction possible pour les administrations publiques. "
           "Couverture : postes du registre de l'ouvrage (dont chiffrés). Les soldes (B.) sont rangés en A11. Une sous-opération (D.11, D.12…) n'est sommée que pour les secteurs qui l'impriment en ligne principale : son montant peut ne couvrir qu'une partie des secteurs.\n"]
    for pid, ptitre, comptes in PARTIES_A:
        out.append(f"\n## {pid}. {ptitre}\n")
        if pid == "A8":
            out.append("Les opérations financières par instrument (F.1 à F.8) viennent du tableau des opérations financières, extrait ; "
                       "l'ouvrage n'a qu'un tableau par secteur ([les comptes des secteurs](../../precis/fr/compte-secteurs.qmd)).\n")
        tot = defaultdict(float)
        sel = [(k, x) for k, x in ops.items() if k[0] in comptes and not k[1].startswith("B.")]
        codes = {k[1] for k, x in sel}
        for k, x in sel:  # dénominateur : opérations de premier rang (aucun code parent présent)
            if any(c != k[1] and k[1].startswith(c) for c in codes):
                continue
            for c in ("emplois", "ressources"):
                tot[c] += abs(x[c])
        for k, x in sorted(sel, key=lambda kv: kv[0][1]):
            c = "emplois" if x["emplois"] else "ressources"
            montant = x[c]
            part = 100 * abs(montant) / tot[c] if tot[c] else 0
            code = x["code"]
            pst = [p for p in postes if p["operation"] == k[2]]
            chif = sum(1 for p in pst if p["montant_reference"])
            secs = [s for s in toutes if s[5] == code or (s[5] == "P.51" and code == "P.51g")]
            domiciles = {(p["volume"], p["chapitre"], p["ancre"]) for p in pst}
            secs += [s for s in toutes if (s[0], s[1], s[3]) in domiciles and s not in secs]
            st = "existe" if any(s[4] == "existe" for s in secs) else ("ébauche" if secs else "inexistant")
            stat_a[st] += 1
            out.append(f"### {code} {x['lib']} — {fr(montant)} MD ({c}), {fr(part)} % du compte ; mode : {mode(k[2])} ; "
                       f"postes : {len(pst)} (dont {chif} chiffrés) ; statut : **{st}**\n")
            if dont.get(k):
                out.append("- dont : " + " ; ".join(dont[k]))
            for v, f, titre, ancre, s_st, _ in secs[:12]:
                lien = f"../../precis/fr/{v}/{f}.qmd" if f else f"../../precis/fr/{v}.qmd"
                out.append(f"- [{titre}]({lien}) ({v}) — {s_st}")
            if len(secs) > 12:
                out.append(f"- … et {len(secs) - 12} autres sections")
            if not secs:
                out.append("- aucune section de l'ouvrage (à créer)")
            lignes_a.append((code, k[2]))
            out.append("")
        for code, lib, note in PROPOSITIONS_A.get(pid, []):
            stat_a["inexistant" if "proposition" in note or "à rédiger" in note else "existe"] += 1
            out.append(f"### {code} {lib} — {note}\n")
    (RFC / "plan-a-comptes.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    # Plan B
    out, stat_b = ["# Plan B : thématique en sept parties (engendré par `scripts/rfc_plans.py`)\n",
                   "Chaque volume garde ses chapitres ; le statut d'un chapitre est lu dans son fichier. Les propositions marquées « inexistant » n'ont aucun fichier dans l'ouvrage.\n"], Counter()
    for pid, ptitre, vs, props in PARTIES_B:
        out.append(f"\n## {pid}. {ptitre}\n")
        for v in vs:
            chs = chapitres(v)
            out.append(f"### Volume « {v} »{' — ' + CAS_B[v] if v in CAS_B else ''}\n")
            for f in chs:
                st = statut_chapitre(FR / v / f"{f}.qmd")
                stat_b[st] += 1
                t = re.search(r"^#\s+(.*?)\s*(\{|$)", lire(FR / v / f"{f}.qmd"), re.M)
                out.append(f"- [{t.group(1) if t else f}](../../precis/fr/{v}/{f}.qmd) — {st}")
            out.append("")
        for p in props:
            st = "existe" if "existante" in p else "inexistant"
            stat_b[st] += 1
            out.append(f"### {p} — **{st}** (proposition)\n")
    (RFC / "plan-b-thematique.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    # Correspondance
    part_b = {v: f"{pid} {pt}" for pid, pt, vs, _ in PARTIES_B for v in vs}
    part_a = {}
    for pid, ptitre, comptes in PARTIES_A:
        for k, x in ops.items():
            if k[0] in comptes:
                part_a.setdefault(x["code"], f"{pid} {ptitre}")
    part_a.update({"D.63": "A5 Le compte de redistribution du revenu en nature", "F": "A8 Le compte financier",
                   "P.6/P.7": "A9 Le reste du monde", "P.51": "A7 Le compte de capital"})
    with (RFC / "correspondance-plans.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["volume", "chapitre", "section", "ancre", "statut", "operation", "plan_a", "plan_b"])
        for v, f, titre, ancre, st, op in toutes:
            pa = part_a.get(op) or ("A1 Le compte de production (par branche)" if op.startswith("branche:") else
                                    "cadre institutionnel" if op in ("cadre", "institution", "transversal") else "à déterminer")
            w.writerow([v, f, titre, ancre, st, op, pa, part_b.get(v, "")])
    print(f"plan A : {dict(stat_a)} ; plan B : {dict(stat_b)} ; sections : {len(toutes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

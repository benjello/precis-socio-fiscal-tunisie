"""Tient l'issue unique « Traductions arabes : état » à jour.

    uv run python scripts/etat_traduction.py corps      # imprime le texte de l'issue
    uv run python scripts/etat_traduction.py publier    # crée ou met à jour l'issue (gh)

Appelé par `translation-sync.yml` à la fin de chaque passage, succès ou non. Aucun appel au
modèle. Le texte se construit sans réseau (fonctions pures, testées) ; seul `publier` parle
à GitHub, par `gh`.

L'ISSUE. Une seule, retrouvée par un marqueur HTML caché dans son corps, jamais recréée en
double, jamais fermée ni rouverte : on met son corps à jour. Elle est épinglée.

LE BUDGET. Le palier gratuit de Gemini plafonne par mois, pour un montant inconnu qui peut
changer. On ne le code donc pas : on l'APPREND. Chaque mois, on cumule les caractères traduits
avec succès ; le mois où la limite dure est atteinte, ce cumul est une mesure du plafond. Le
budget estimé du mois est la moyenne des trois dernières mesures (`BUDGET_INITIAL` à défaut).
L'historique vit dans un commentaire HTML du corps de l'issue (`donnees-traduction`), au même
endroit que l'état : pas de fichier à pousser sur une branche protégée.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

MARQUEUR = "<!-- etat-traduction-arabe -->"
TITRE = "Traductions arabes : état"
DONNEES_RE = re.compile(r"<!-- donnees-traduction: (\{.*?\}) -->", re.S)

# Budget mensuel supposé tant qu'aucun plafond n'a été observé, en caractères de source
# française traduits. Valeur prudente, sans mesure : la première limite dure atteinte la
# remplace. Pour la régler à la main, modifier cette constante ou, mieux, laisser faire.
BUDGET_INITIAL = 300_000
MOIS_MOYENNES = 3
# Part du budget que le passage planifié peut dépenser ; le reste est la marge des
# traductions déclenchées par les fusions sur `master`.
PART_PLANIFIEE = 0.75

A_JOUR = "a_jour"
EN_COURS = "en_cours"
SUSPENDUE = "suspendue"
ECHEC = "echec"

LIBELLES = {
    A_JOUR: "à jour",
    EN_COURS: "en cours",
    SUSPENDUE: "suspendue : plafond mensuel atteint",
    ECHEC: "en échec (autre cause qu'une limite de dépense)",
}
NATURES = {
    "plafond_mensuel": "le message de l'API parle d'un plafond de dépense mensuel",
    "credit_prepaye": "refus 402 : crédits prépayés épuisés (le palier gratuit mensuel "
                      "n'explique pas ce message à lui seul)",
    "quota_persistant": "429 qui ne cède pas après tous les réessais (cause non établie : "
                        "plafond ou limite de débit)",
    "limite_inconnue": "mention de facturation (cause exacte non établie)",
}


def fmt(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def marqueur() -> str:
    return MARQUEUR


def mois_de(maintenant: datetime) -> str:
    return maintenant.strftime("%Y-%m")


def renouvellement_estime(maintenant: datetime) -> datetime:
    """1er du mois suivant, 00h00 UTC. Estimation : le fournisseur ne publie pas l'heure."""
    if maintenant.month == 12:
        return datetime(maintenant.year + 1, 1, 1, tzinfo=timezone.utc)
    return datetime(maintenant.year, maintenant.month + 1, 1, tzinfo=timezone.utc)


def trouver_issue(issues: list[dict]) -> dict | None:
    """L'issue portant le marqueur (la plus ancienne si, par accident, il y en a plusieurs)."""
    portent = [i for i in issues if MARQUEUR in (i.get("body") or "")]
    return min(portent, key=lambda i: i["number"]) if portent else None


def lire_donnees(corps: str | None) -> dict:
    """Données persistantes cachées dans le corps ; vides si absentes ou illisibles."""
    vide = {"historique": {}, "etat": None}
    if not corps:
        return vide
    m = DONNEES_RE.search(corps)
    if not m:
        return vide
    try:
        d = json.loads(m.group(1))
    except ValueError:
        return vide
    d.setdefault("historique", {})
    d.setdefault("etat", None)
    return d


def enregistrer_passage(donnees: dict, bilan: dict | None, maintenant: datetime) -> dict:
    """Ajoute le passage à l'historique mensuel. `bilan` est None si rien n'a été tenté."""
    d = json.loads(json.dumps(donnees))
    if not bilan:
        return d
    mois = d["historique"].setdefault(mois_de(maintenant),
                                      {"caracteres": 0, "limite_atteinte": False})
    mois["caracteres"] += int(bilan.get("caracteres") or 0)
    if bilan.get("etat") == SUSPENDUE:
        mois["limite_atteinte"] = True
        mois["nature"] = bilan.get("nature")
    d["etat_passage"] = bilan.get("etat")
    d["dernier_lot"] = {
        "date": maintenant.strftime("%Y-%m-%d %H:%M UTC"),
        "traduits": bilan.get("traduits") or [],
        "non_traduits": bilan.get("non_traduits") or [],
        "caracteres": int(bilan.get("caracteres") or 0),
    }
    return d


def budget_estime(historique: dict, mois_courant: str) -> tuple[int, bool]:
    """(budget en caractères, mesuré ?). Moyenne des dernières mesures des mois ÉCOULÉS.

    Une mesure est un mois où la limite dure a été atteinte : le cumul de ce mois-là est
    ce que le palier a laissé passer. Un mois sans limite ne mesure rien (on n'a pas
    atteint le plafond), sauf pour dire que le budget est au moins ce cumul.
    """
    mesures = [(m, v["caracteres"]) for m, v in sorted(historique.items())
               if v.get("limite_atteinte") and v.get("caracteres") and m < mois_courant]
    if not mesures:
        # Mois courant déjà plafonné : à défaut de mois écoulé, il fait foi lui-même.
        courant = historique.get(mois_courant)
        if courant and courant.get("limite_atteinte") and courant.get("caracteres"):
            return int(courant["caracteres"]), True
        return BUDGET_INITIAL, False
    derniers = [c for _m, c in mesures[-MOIS_MOYENNES:]]
    return int(sum(derniers) / len(derniers)), True


def consommation(historique: dict, mois_courant: str) -> int:
    return int(historique.get(mois_courant, {}).get("caracteres", 0))


def mois_pour_resorber(caracteres_en_retard: int, budget: int) -> int:
    """Nombre de mois pour résorber le retard au rythme planifié (au moins 1 s'il y en a)."""
    if caracteres_en_retard <= 0:
        return 0
    rythme = max(1, int(budget * PART_PLANIFIEE))
    return math.ceil(caracteres_en_retard / rythme)


def determiner_etat(nb_retard: int, etat_passage: str | None, etat_precedent: str | None) -> str:
    if nb_retard == 0:
        return A_JOUR
    if etat_passage:
        return etat_passage if etat_passage in (SUSPENDUE, ECHEC) else EN_COURS
    # Aucun passage tenté (rien à traduire, ou événement sans lot) : on garde le dernier
    # constat, qui ne se lève que par un passage réussi.
    return etat_precedent if etat_precedent in (SUSPENDUE, ECHEC) else EN_COURS


def livre_de(chemin: str) -> str:
    parties = chemin.split("/")
    return parties[2] if len(parties) > 3 else "(racine)"


def par_livre(retard: list[dict]) -> dict[str, list[dict]]:
    livres: dict[str, list[dict]] = {}
    for r in retard:
        livres.setdefault(livre_de(r["fichier"]), []).append(r)
    return dict(sorted(livres.items()))


def collecter_retard(racine: Path = RACINE) -> list[dict]:
    """Fichiers en retard, avec leur taille (lecture du dépôt local, sans réseau)."""
    import traduction_en_retard as tr
    sortie = []
    for fr, d_fr, d_ar in tr.en_retard():
        try:
            taille = len(fr.read_text(encoding="utf-8"))
        except OSError:
            taille = 0
        sortie.append({"fichier": str(fr.relative_to(racine)), "caracteres": taille,
                       "jamais": d_ar is None})
    return sortie


def phrase_etat(etat: str, nature: str | None, maintenant: datetime) -> str:
    if etat != SUSPENDUE:
        return LIBELLES[etat]
    quand = renouvellement_estime(maintenant).strftime("%Y-%m-%d")
    base = (f"suspendue : plafond mensuel atteint ; reprise attendue au renouvellement "
            f"mensuel (estimé au {quand}, 00h UTC ; estimation, si le renouvellement n'a "
            "pas lieu le 1er)")
    if nature in NATURES:
        base += f". Ce que l'on sait : {NATURES[nature]}"
    return base


def construire_corps(retard: list[dict], maintenant: datetime, donnees: dict,
                     prs_en_attente: list[dict] | None = None,
                     prochain_lot: list[str] | None = None,
                     nature: str | None = None) -> str:
    """Texte complet de l'issue. `donnees` porte déjà le passage en cours."""
    etat = determiner_etat(len(retard), donnees.get("etat_passage"), donnees.get("etat"))
    donnees = {k: v for k, v in donnees.items() if k != "etat_passage"}
    donnees["etat"] = etat
    mois = mois_de(maintenant)
    hist = donnees.get("historique", {})
    budget, mesure = budget_estime(hist, mois)
    conso = consommation(hist, mois)
    total = sum(r["caracteres"] for r in retard)
    nature = nature or hist.get(mois, {}).get("nature")

    l = [MARQUEUR, "", "Issue tenue par `translation-sync.yml` (`scripts/etat_traduction.py`) : "
         "elle se met à jour, ne se ferme pas, ne se commente pas.", ""]
    l.append(f"**État : {phrase_etat(etat, nature, maintenant)}**")
    l.append(f"Dernier passage : {maintenant.strftime('%Y-%m-%d %H:%M UTC')}")
    l.append("")
    if not retard:
        l.append("Retard : **aucun**. Tous les fichiers français ont une traduction arabe "
                 "au moins aussi récente.")
    else:
        jamais = [r for r in retard if r["jamais"]]
        l.append(f"Retard : **{len(retard)} fichier(s)** français plus récents que leur "
                 f"arabe, dont {len(jamais)} jamais traduit(s) ; environ {fmt(total)} "
                 "caractères à envoyer.")
        l.append("")
        l.append("| Livre | En retard | Jamais traduits | Caractères |")
        l.append("|---|---:|---:|---:|")
        for livre, items in par_livre(retard).items():
            c = sum(i["caracteres"] for i in items)
            n = sum(1 for i in items if i["jamais"])
            l.append(f"| {livre} | {len(items)} | {n} | {fmt(c)} |")
        l.append("")
        l.append("<details><summary>Liste des fichiers</summary>\n")
        for livre, items in par_livre(retard).items():
            l.append(f"**{livre}**\n")
            for i in items:
                l.append(f"- `{i['fichier']}`{' (jamais traduit)' if i['jamais'] else ''}")
            l.append("")
        l.append("</details>")
    l.append("")
    l.append("### Budget")
    origine = "moyenne des mois où la limite a été atteinte" if mesure else \
        "valeur initiale, aucune mesure encore"
    l.append(f"- Budget estimé du mois : {fmt(budget)} caractères ({origine}).")
    l.append(f"- Consommé ce mois ({mois}) : {fmt(conso)} caractères.")
    if retard:
        m = mois_pour_resorber(total, budget)
        l.append(f"- Résorption du retard au rythme planifié ({int(PART_PLANIFIEE * 100)} % "
                 f"du budget, le reste pour les fusions) : environ {m} mois.")
    lot = donnees.get("dernier_lot")
    l.append("")
    l.append("### Dernier lot")
    if lot:
        l.append(f"{lot['date']} : {len(lot['traduits'])} fichier(s) traduit(s), "
                 f"{len(lot['non_traduits'])} non traduit(s), {fmt(lot['caracteres'])} "
                 "caractères.")
        for f in lot["traduits"][:30]:
            l.append(f"- `{f}`")
    else:
        l.append("Aucun lot traité depuis la création de cette issue.")
    if prochain_lot:
        l.append("")
        l.append("### Prochain lot")
        for f in prochain_lot:
            l.append(f"- `{f}`")
    if prs_en_attente:
        l.append("")
        l.append("### PR de traduction ouvertes")
        for p in prs_en_attente:
            l.append(f"- #{p['number']} {p.get('title', '')} : "
                     f"{p.get('sort', 'relecture et fusion à faire à la main')}")
    l.append("")
    l.append(f"<!-- donnees-traduction: {json.dumps(donnees, ensure_ascii=False)} -->")
    corps = "\n".join(l) + "\n"
    return corps[:60000]


# ---------- partie réseau (gh), non testée par les tests unitaires ----------

def _gh(*args: str, entree: str | None = None) -> str:
    r = subprocess.run(["gh", *args], capture_output=True, text=True, input=entree)
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} : {r.stderr.strip()}")
    return r.stdout


def publier(corps: str) -> str:
    issues = json.loads(_gh("issue", "list", "--state", "all", "--limit", "300",
                            "--json", "number,body,state"))
    existante = trouver_issue(issues)
    chemin = RACINE / "etat_traduction_corps.md"
    chemin.write_text(corps, encoding="utf-8")
    try:
        if existante:
            _gh("issue", "edit", str(existante["number"]), "--body-file", str(chemin))
            return f"issue #{existante['number']} mise à jour"
        url = _gh("issue", "create", "--title", TITRE, "--body-file", str(chemin)).strip()
        numero = url.rstrip("/").split("/")[-1]
        try:
            _gh("issue", "pin", numero)
        except RuntimeError as e:
            print(f"Épinglage impossible (à faire à la main) : {e}")
        return f"issue #{numero} créée"
    finally:
        chemin.unlink(missing_ok=True)


def prs_en_attente() -> list[dict]:
    """PR de traduction ouvertes : numéro, titre et sort (fusion automatique en attente ou non)."""
    try:
        prs = json.loads(_gh("pr", "list", "--state", "open", "--limit", "100", "--json",
                             "number,title,headRefName,autoMergeRequest"))
    except (RuntimeError, ValueError, OSError):
        return []
    sortie = []
    for p in prs:
        if not p["headRefName"].startswith("auto-translate/"):
            continue
        sort = ("fusion automatique activée, en attente des contrôles obligatoires"
                if p.get("autoMergeRequest") else "relecture et fusion à faire à la main")
        sortie.append({"number": p["number"], "title": p["title"], "sort": sort})
    return sortie


def issue_courante() -> dict | None:
    try:
        issues = json.loads(_gh("issue", "list", "--state", "all", "--limit", "300",
                                "--json", "number,body,state"))
    except (RuntimeError, ValueError, OSError):
        return None
    return trouver_issue(issues)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("action", choices=["corps", "publier"])
    ap.add_argument("--bilan", help="JSON écrit par translate_sync (TRADUCTION_BILAN)")
    ap.add_argument("--prochain-lot", default="", help="fichiers du prochain lot, séparés par des espaces")
    ap.add_argument("--prs", help="JSON : liste de PR de traduction en attente")
    ap.add_argument("--corps-precedent", help="fichier : corps de l'issue existante (tests, hors ligne)")
    args = ap.parse_args()

    maintenant = datetime.now(timezone.utc)
    bilan = None
    if args.bilan and Path(args.bilan).exists():
        bilan = json.loads(Path(args.bilan).read_text(encoding="utf-8"))

    if args.corps_precedent:
        precedent = Path(args.corps_precedent).read_text(encoding="utf-8")
    elif args.action == "publier":
        iss = issue_courante()
        precedent = (iss or {}).get("body")
    else:
        precedent = None
    donnees = enregistrer_passage(lire_donnees(precedent), bilan, maintenant)
    prs = json.loads(args.prs) if args.prs else (
        prs_en_attente() if args.action == "publier" else None)
    corps = construire_corps(collecter_retard(), maintenant, donnees, prs,
                             args.prochain_lot.split() or None,
                             (bilan or {}).get("nature"))
    if args.action == "corps":
        print(corps)
        return 0
    print(publier(corps))
    resume = os.environ.get("GITHUB_STEP_SUMMARY")
    if resume:
        etat = lire_donnees(corps)["etat"]
        with open(resume, "a", encoding="utf-8") as f:
            f.write("### Traductions arabes : état\n\n"
                    + ("Traduction suspendue : plafond mensuel atteint ; reprise attendue "
                       "au renouvellement mensuel.\n" if etat == SUSPENDUE
                       else f"État : {LIBELLES[etat]}.\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

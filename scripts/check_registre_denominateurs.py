#!/usr/bin/env python3
"""Registre des dénominateurs au PIB : contrôle de cohérence structurelle.

Le registre `docs/notes/registre-denominateurs-pib.yml` relie chaque ratio « au PIB » publié
dans le précis à son dénominateur (agrégat, base, source), et dit s'il est produit par le précis
(interne) ou imprimé tel quel par un rapport extérieur (externe). Première brique de la vision
compta-nat (option B3).

Ce contrôle vérifie, sans juger le contenu éditorial :

1. chaque entrée porte les champs obligatoires de sa `nature` :
   - interne (hors `a_produire`/`cadre`) : `agregat`, `base`, `source_serie` ;
   - externe : `source_rapport`, `base` ;
2. `classement` et `nature` appartiennent aux vocabulaires admis, et sont cohérents
   (un `externe` a `nature: externe`, et réciproquement) ;
3. `base` appartient au vocabulaire admis ;
4. chaque `fichier` cité existe sur le disque ;
5. la `synthese` du bloc `meta` est exacte (recompte par classement) ;
6. INFORMATIF (n'échoue pas) : pour les internes, `source_serie` qui ressemble à un identifiant
   d'entrepôt (sans espace) est rapproché du catalogue `precis/_seriescache/catalog.snapshot.yml` ;
   les identifiants absents, et les `source_serie` encore « à préciser », sont listés comme suite
   à donner.

Usage : uv run python scripts/check_registre_denominateurs.py [registre.yml]
Sans argument : docs/notes/registre-denominateurs-pib.yml. Sort en 1 s'il trouve une erreur
structurelle (pas pour les simples avertissements informatifs).
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "docs/notes/registre-denominateurs-pib.yml"
SNAPSHOT = RACINE / "precis/_seriescache/catalog.snapshot.yml"

CLASSEMENTS = {"ok", "partiel", "externe", "a_produire", "cadre"}
NATURES = {"interne", "externe"}
BASES = {
    "par_segments", "2015", "1997", "1983", "1983/1997", "1997/2015",
    "non_dit", "non_precisee_par_la_source", "a_produire", "mixte", "renvoi",
}
# ressemble à un identifiant d'entrepôt : minuscules, chiffres et tirets, pas d'espace
RE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)+$")


def _ids_catalogue() -> set[str]:
    if not SNAPSHOT.exists():
        return set()
    ids = set()
    for ligne in SNAPSHOT.read_text(encoding="utf-8").splitlines():
        m = re.match(r"- id:\s*(\S+)", ligne)
        if m:
            ids.add(m.group(1))
    return ids


def main() -> int:
    chemin = Path(sys.argv[1]) if len(sys.argv) > 1 else REGISTRE
    if not chemin.exists():
        print(f"ERREUR : registre introuvable : {chemin}")
        return 1

    doc = yaml.safe_load(chemin.read_text(encoding="utf-8"))
    entrees = doc.get("entrees") or []
    if not entrees:
        print("ERREUR : aucune entrée dans le registre.")
        return 1

    erreurs: list[str] = []
    avertissements: list[str] = []
    vus_id: set = set()
    compte = Counter()

    for e in entrees:
        eid = e.get("id", "?")
        ref = f"entrée {eid}"
        if eid in vus_id:
            erreurs.append(f"{ref} : identifiant en double.")
        vus_id.add(eid)

        classement = e.get("classement")
        nature = e.get("nature")
        base = e.get("base")

        if classement not in CLASSEMENTS:
            erreurs.append(f"{ref} : classement « {classement} » hors vocabulaire {sorted(CLASSEMENTS)}.")
        else:
            compte[classement] += 1
        if nature not in NATURES:
            erreurs.append(f"{ref} : nature « {nature} » hors vocabulaire {sorted(NATURES)}.")

        # cohérence classement ↔ nature
        if classement == "externe" and nature != "externe":
            erreurs.append(f"{ref} : classement externe mais nature « {nature} ».")
        if nature == "externe" and classement != "externe":
            erreurs.append(f"{ref} : nature externe mais classement « {classement} ».")

        # base
        if base not in BASES:
            erreurs.append(f"{ref} : base « {base} » hors vocabulaire {sorted(BASES)}.")

        # champs obligatoires par nature
        if nature == "externe":
            if not e.get("source_rapport"):
                erreurs.append(f"{ref} : entrée externe sans source_rapport.")
        elif nature == "interne":
            if classement not in {"a_produire", "cadre"}:
                for champ in ("agregat", "base", "source_serie"):
                    if not e.get(champ):
                        erreurs.append(f"{ref} : entrée interne sans {champ}.")

        # fichiers existent
        fichiers = e.get("fichier")
        if not fichiers:
            erreurs.append(f"{ref} : aucun fichier.")
        else:
            if isinstance(fichiers, str):
                fichiers = [fichiers]
            for f in fichiers:
                if not (RACINE / f).exists():
                    erreurs.append(f"{ref} : fichier absent : {f}")

        # INFORMATIF : source_serie vs catalogue
        ss = e.get("source_serie")
        if nature == "interne" and isinstance(ss, str) and ss not in ("—", ""):
            if ss.startswith("à préciser"):
                avertissements.append(f"{ref} : source_serie à préciser ({ss}).")
            elif RE_ID.match(ss) and ss not in _ids_catalogue():
                avertissements.append(
                    f"{ref} : source_serie « {ss} » absente du snapshot "
                    "(série dérivée ou à régénérer ?).")

    # synthèse annoncée
    annonce = (doc.get("meta") or {}).get("synthese") or {}
    for k, v in annonce.items():
        if compte.get(k, 0) != v:
            erreurs.append(
                f"meta.synthese.{k} annonce {v}, le registre en compte {compte.get(k, 0)}.")

    # rapport
    print(f"Registre : {chemin.relative_to(RACINE)}")
    print(f"  {len(entrees)} entrées — " + ", ".join(f"{k}={compte[k]}" for k in sorted(compte)))
    if avertissements:
        print(f"  {len(avertissements)} suite(s) à donner (informatif) :")
        for a in avertissements:
            print(f"    · {a}")
    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) structurelle(s) :")
        for e in erreurs:
            print(f"  ✗ {e}")
        return 1
    print("  structure : OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

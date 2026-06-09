"""Outils partagés de figures pour le précis (traçabilité + téléchargement sourcé).

Frontière : les **séries** viennent du paquet `tunisia_data` (entrepôt) ; ici on
prépare le **jeu de données de la figure** (figdata), on écrit sa provenance, et on
fournit la ligne « Source » et le lien de téléchargement. Les figures elles-mêmes
sont définies **par livre** (`precis/fr/<livre>/figures/`), jamais à la racine.

La provenance (sources/clés de citation, unité, périmètre, base, caveats) est tirée
de `tunisia_data.meta(series_id)` — jamais saisie à la main.
"""
from __future__ import annotations

import datetime as _dt
from pathlib import Path

import pandas as pd
import tunisia_data as td


def _meta(series_id: str) -> dict:
    return td.meta(series_id)


def source_line(*series_ids: str) -> str:
    """Ligne « Source » d'une figure, assemblée depuis la provenance des séries."""
    keys, bases, perims = [], set(), set()
    for sid in series_ids:
        m = _meta(sid)
        keys += [f"@{k}" for k in m.get("sources", [])]
        if m.get("base_pib"):
            bases.add(str(m["base_pib"]))
        if m.get("perimetre"):
            perims.add(m["perimetre"])
    parts = ["Source : " + ", ".join(dict.fromkeys(keys))]
    if bases:
        parts.append("PIB base " + "/".join(sorted(bases)))
    parts.append("nominal (prix courants)")
    return " — ".join(parts)


def write_figdata(df: pd.DataFrame, out_csv: Path, *series_ids: str,
                  note: str | None = None, generated: str | None = None) -> Path:
    """Écrit le figdata téléchargeable, avec en-tête de provenance commenté + sidecar .yml.

    `generated` : date ISO passée explicitement (Quarto/CI) — pas de Date.now() implicite.
    """
    out_csv = Path(out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    keys = []
    fiches = []
    caveats = []
    for sid in series_ids:
        m = _meta(sid)
        keys += m.get("sources", [])
        if m.get("fiche"):
            fiches.append(m["fiche"])
        if m.get("caveats"):
            caveats.append(m["caveats"])
    stamp = generated or _dt.date.today().isoformat()
    header = [
        f"# Figure-data du précis socio-fiscal tunisien — généré le {stamp}",
        f"# séries (tunisia_data) : {', '.join(series_ids)}",
        f"# sources (citation) : {', '.join('@'+k for k in dict.fromkeys(keys))}",
        f"# fiches : {', '.join(fiches)}",
        f"# méthode/hypothèses : {', '.join(caveats)}",
    ]
    if note:
        header.append(f"# note : {note}")
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        f.write("\n".join(header) + "\n")
        df.to_csv(f, index=False)
    # sidecar yaml (lisible machine)
    side = out_csv.with_suffix(out_csv.suffix + ".yml")
    side.write_text(
        "series: [{}]\nsources: [{}]\nfiches: [{}]\ncaveats: [{}]\ngenerated: {}\n".format(
            ", ".join(series_ids), ", ".join(dict.fromkeys(keys)),
            ", ".join(fiches), ", ".join(caveats), stamp),
        encoding="utf-8")
    return out_csv


def download_button(figdata_csv: str, label: str = "Télécharger les données (sourcées)") -> str:
    """Markdown du lien de téléchargement (le site sert le figdata sourcé, pas le raw)."""
    return f"[⬇️ {label}]({figdata_csv}){{download=\"\"}}"

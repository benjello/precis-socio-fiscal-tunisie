"""Outils partagés de figures pour le précis (traçabilité + téléchargement sourcé).

Frontière : les **séries** viennent du paquet `tunisia_data` (entrepôt) ; ici on
prépare le **jeu de données de la figure** (figdata), on écrit sa provenance, et on
fournit la ligne « Source » et le lien de téléchargement. Les figures elles-mêmes
sont définies **par livre** (`precis/fr/<livre>/figures/`), jamais à la racine.

La provenance (sources/clés de citation, unité, périmètre, base, caveats) est tirée
de `tunisia_data.meta(series_id)` — jamais saisie à la main.

Autonomie de build (diffusion GitHub Pages)
-------------------------------------------
Le rendu du site **ne dépend pas** de la présence de l'entrepôt `tunisia_data`.
`series()` et `meta()` utilisent l'entrepôt s'il est importable (dev local), sinon
ils retombent sur un **snapshot versionné dans le précis** (`precis/_seriescache/` :
un CSV par série + `catalog.snapshot.yml` pour la provenance). Le snapshot est
régénéré depuis l'entrepôt par `refresh_cache(*series_ids)` (étape « produire »),
puis committé. Ainsi le build CI/Pages reste reproductible sans le repo privé.
"""
from __future__ import annotations

import datetime as _dt
import functools
from pathlib import Path

import pandas as pd

# Cache versionné sous precis/ (jamais à la racine du repo) : autonomie de build.
_CACHE = Path(__file__).resolve().parent.parent / "precis" / "_seriescache"


# --- i18n : la langue du livre est déduite du cwd au render (precis/<lang>/...) ---
def lang() -> str:
    """Langue du livre en cours de rendu, déduite du chemin de travail."""
    p = Path.cwd().as_posix()
    if "/ar/" in p or p.endswith("/ar"):
        return "ar"
    return "fr"


# Chrome d'interface généré par Python (jamais vu par le pipeline de traduction).
# Le texte des figures (titres/axes/légendes/en-têtes) est, lui, dans chaque module.
_UI = {
    "tab_graph":  {"fr": "📈 Graphique",  "ar": "📈 الرسم البياني"},
    "tab_data":   {"fr": "📊 Données",    "ar": "📊 البيانات"},
    "tab_src":    {"fr": "🔗 Sources",    "ar": "🔗 المصادر"},
    "source":     {"fr": "Source",        "ar": "المصدر"},
    "nominal":    {"fr": "valeurs courantes (nominal)", "ar": "قيم جارية (اسمية)"},
    "pib_base":   {"fr": "PIB base",      "ar": "الناتج المحلي الإجمالي، أساس"},
    "consult":    {"fr": "consulter la série en ligne ↗",
                   "ar": "الاطّلاع على السلسلة عبر الإنترنت ↗"},
    "perimetre":  {"fr": "périmètre",     "ar": "النطاق"},
    "unite":      {"fr": "unité",         "ar": "الوحدة"},
    "reserves":   {"fr": "Réserves",      "ar": "تحفّظات"},
    "download":   {"fr": "Télécharger les données (sourcées)",
                   "ar": "تنزيل البيانات (مع مصادرها)"},
    "how_to_read": {"fr": "Comment lire cette figure",
                    "ar": "كيف نقرأ هذا الرسم البياني"},
}


def t(key: str) -> str:
    """Traduit une chaîne de chrome d'interface selon la langue courante."""
    return _UI[key].get(lang(), _UI[key]["fr"])


# --- arabe dans matplotlib : police OFL embarquée + shaping RTL ---------------
@functools.lru_cache(maxsize=1)
def _register_ar_font() -> str:
    """Enregistre la police arabe embarquée (indépendance CI) ; retourne son nom."""
    from matplotlib import font_manager
    fp = Path(__file__).resolve().parent / "fonts" / "NotoNaskhArabic-Regular.ttf"
    font_manager.fontManager.addfont(str(fp))
    return font_manager.FontProperties(fname=str(fp)).get_name()


def apply_lang_font() -> None:
    """Configure la police des figures pour le livre courant (arabe si lang=ar).

    Police arabe + repli DejaVu Sans pour les chiffres/symboles latins.
    À appeler une fois en tête de chaque fonction de figure.
    """
    if lang() != "ar":
        return
    import matplotlib as mpl
    name = _register_ar_font()
    mpl.rcParams["font.family"] = [name, "DejaVu Sans"]


def fig_text(s: str) -> str:
    """Met en forme une chaîne pour matplotlib (shaping + RTL en arabe, sinon identité)."""
    if lang() != "ar":
        return s
    import arabic_reshaper
    from bidi.algorithm import get_display
    return get_display(arabic_reshaper.reshape(s))


def _td():
    """Retourne le module `tunisia_data` s'il est installé, sinon None."""
    try:
        import tunisia_data as td
        return td
    except Exception:
        return None


@functools.lru_cache(maxsize=1)
def _snapshot() -> dict:
    """Provenance snapshotée {id: entrée} lue depuis le cache du précis."""
    f = _CACHE / "catalog.snapshot.yml"
    if not f.exists():
        return {}
    import yaml
    return {e["id"]: e for e in (yaml.safe_load(f.read_text(encoding="utf-8")) or [])}


def meta(series_id: str) -> dict:
    """Provenance d'une série : entrepôt si présent, sinon snapshot du précis."""
    td = _td()
    if td is not None:
        try:
            return td.meta(series_id)
        except Exception:
            pass
    snap = _snapshot()
    if series_id in snap:
        return snap[series_id]
    raise KeyError(f"série inconnue: {series_id!r} (ni entrepôt, ni snapshot)")


def series(series_id: str) -> pd.DataFrame:
    """Données d'une série : entrepôt si présent, sinon CSV snapshoté du précis."""
    td = _td()
    if td is not None:
        try:
            return td.load(series_id)
        except Exception:
            pass
    p = _CACHE / f"{series_id}.csv"
    if p.exists():
        return pd.read_csv(p)
    raise FileNotFoundError(
        f"série {series_id!r} absente du cache {p} — lancer figtools.refresh_cache()")


def refresh_cache(*series_ids: str) -> None:
    """Snapshote séries + provenance depuis l'entrepôt vers le cache du précis.

    À lancer en dev (entrepôt présent) puis committer `_seriescache/`. Fusionne
    avec le snapshot existant pour ne pas perdre les séries des autres livres.
    """
    td = _td()
    if td is None:
        raise RuntimeError("tunisia_data requis pour rafraîchir le cache des séries")
    import yaml
    _CACHE.mkdir(parents=True, exist_ok=True)
    snap_path = _CACHE / "catalog.snapshot.yml"
    existing = {}
    if snap_path.exists():
        existing = {e["id"]: e for e in (yaml.safe_load(snap_path.read_text("utf-8")) or [])}
    for sid in series_ids:
        td.load(sid).to_csv(_CACHE / f"{sid}.csv", index=False)
        existing[sid] = td.meta(sid)
    snap_path.write_text(
        yaml.safe_dump(list(existing.values()), allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    _snapshot.cache_clear()


def _meta(series_id: str) -> dict:
    return meta(series_id)


def source_line(*series_ids: str) -> str:
    """Ligne « Source » d'une figure, assemblée depuis la provenance des séries."""
    keys, bases, units = [], set(), set()
    for sid in series_ids:
        m = _meta(sid)
        keys += [f"@{k}" for k in m.get("sources", [])]
        if m.get("base_pib"):
            bases.add(str(m["base_pib"]))
        if m.get("unite"):
            units.add(str(m["unite"]).lower())
    parts = [f"{t('source')} : " + ", ".join(dict.fromkeys(keys))]
    if bases:
        parts.append(f"{t('pib_base')} " + "/".join(sorted(bases)))
    # mention « prix courants » seulement pour les séries monétaires (pas les effectifs)
    monetaire = any(k in u for u in units
                    for k in ("dinar", "pib", "dépense", "depense", "%", "budget"))
    if monetaire:
        parts.append(t("nominal"))
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
    # un shortcode Quarto non résolu (passé tel quel depuis un chunk) → date du jour
    if not generated or "{{" in generated:
        generated = _dt.date.today().isoformat()
    stamp = generated
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


def download_button(figdata_csv: str, label: str | None = None) -> str:
    """Markdown du lien de téléchargement (le site sert le figdata sourcé, pas le raw)."""
    return f"[⬇️ {label or t('download')}]({figdata_csv}){{download=\"\"}}"


# --- traçabilité détaillée des sources ---------------------------------------

@functools.lru_cache(maxsize=1)
def _ref_index() -> dict:
    """Index {clé: entrée CSL} des references.json visibles depuis le cwd.

    Lit `references.json` du livre (cwd) puis ceux des dossiers parents
    (`../references.json` = bibliographie commune). Sert à enrichir la
    provenance : titre lisible et URL web de la source d'origine.
    """
    import json
    idx: dict = {}
    seen = set()
    for base in (Path.cwd(), *Path.cwd().parents):
        rj = base / "references.json"
        if rj in seen or not rj.exists():
            continue
        seen.add(rj)
        try:
            items = json.loads(rj.read_text(encoding="utf-8")).get("items", [])
        except (ValueError, OSError):
            continue
        for e in items:
            idx.setdefault(e.get("id"), e)  # le plus proche (livre) prime
        if base == Path.cwd().anchor:
            break
    return idx


def source_details(*series_ids: str) -> str:
    """Bloc Markdown « Sources & traçabilité » : tout ce qui permet de remonter
    de la figure jusqu'au fichier brut récupéré sur le web.

    Pour chaque série : titre + clé de citation, **lien web** vers la source
    d'origine (references.json), fiche de provenance, fichiers raw de l'entrepôt
    `tunisia-data`, périmètre, unité, base PIB, hypothèses/caveats.
    """
    def mf(m, key, default=None):
        """Champ de provenance localisé : `<key>_<lang>` si présent, sinon `<key>`."""
        return m.get(f"{key}_{lang()}") or m.get(key, default)

    refs = _ref_index()
    blocks = []
    for sid in series_ids:
        m = _meta(sid)
        lines = [f"**{mf(m, 'titre', sid)}**\n"]
        for key in m.get("sources", []):
            ref = refs.get(key, {})
            titre = ref.get("title", key)
            url = ref.get("URL")  # lien public vers la série/l'enquête (site producteur)
            cite = f"[@{key}]"
            if url:
                lines.append(f"- {cite} — {titre} · [{t('consult')}]({url})")
            else:
                lines.append(f"- {cite} — {titre}")
        meta_bits = []
        if mf(m, "perimetre"):
            meta_bits.append(f"*{t('perimetre')}* : {mf(m, 'perimetre')}")
        if mf(m, "unite"):
            meta_bits.append(f"*{t('unite')}* : {mf(m, 'unite')}")
        if m.get("base_pib"):
            meta_bits.append(f"*{t('pib_base')}* : {m['base_pib']}")
        if meta_bits:
            lines.append("- " + " · ".join(meta_bits))
        cav = mf(m, "caveats")
        if cav and not str(cav).endswith(".md"):  # pas de chemin local de fiche
            lines.append(f"- ⚠️ *{t('reserves')}* : {cav}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def figure_tabs(fig, df: pd.DataFrame, *series_ids: str, slug: str,
                caption: str = "", note_lecture: str | None = None,
                fig_id: str | None = None, figdata_dir: str = "figdata",
                png_dir: str = "_fig", scroll_y: str = "420px",
                generated: str | None = None) -> None:
    """Composant générique : figure en **onglets** Graphique / Données / Sources.

    À appeler dans un chunk Quarto `#| output: asis`. Produit :
      - onglet « Graphique » : figure **numérotée** (crossref Quarto « Figure N : … »),
        ligne « Source » courte, et — si fournie — une **note de lecture** ;
      - onglet « Données » : table **itables** scrollable + export CSV/Excel
        + téléchargement du **figdata sourcé** ;
      - onglet « Sources » : provenance détaillée (citation, **lien web** vers la
        source d'origine, fiche, fichiers bruts, périmètre, réserves).

    `fig`          : figure matplotlib (déjà rendue).
    `df`           : données de la figure (deviennent le figdata téléchargeable).
    `series_ids`   : id(s) de série `tunisia_data` (provenance/citation).
    `slug`         : identifiant de fichier (png + csv).
    `caption`      : **titre** de la figure (légende numérotée par Quarto).
    `note_lecture` : texte « Comment lire cette figure » (callout). Optionnel.
    `fig_id`       : ancre de référence croisée (défaut `fig-<slug>`).
    """
    from itables import to_html_datatable

    fig_id = fig_id or f"fig-{slug.replace('_', '-')}"
    png = Path(png_dir)
    png.mkdir(parents=True, exist_ok=True)
    png_path = png / f"{slug}.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")

    csv_path = Path(figdata_dir) / f"{slug}.csv"
    write_figdata(df, csv_path, *series_ids, note=caption, generated=generated)

    table = to_html_datatable(
        df, buttons=["csvHtml5", "excelHtml5"], scrollY=scroll_y, scrollX=True,
        scrollCollapse=True, paging=False, classes="display compact nowrap",
        connected=True)  # charge DataTables depuis le CDN (figure autoportante)

    src = source_line(*series_ids)
    dl = download_button(str(csv_path))
    details = source_details(*series_ids)
    lecture = ""
    if note_lecture:
        lecture = (f'\n::: {{.callout-note appearance="simple" '
                   f'icon=true title="{t("how_to_read")}"}}\n'
                   f'{note_lecture}\n:::\n')
    print(f"""::: {{.panel-tabset}}

## {t('tab_graph')}

![{caption}]({png_path}){{#{fig_id} fig-alt="{caption}"}}

::: {{.figure-source}}
{src}
:::
{lecture}
## {t('tab_data')}

{dl}

{table}

## {t('tab_src')}

::: {{.figure-sources-detail}}
{details}
:::

:::
""")

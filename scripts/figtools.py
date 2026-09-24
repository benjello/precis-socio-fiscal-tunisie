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
from typing import TYPE_CHECKING

# `pandas` n'est PAS importé à l'exécution, à dessein — comme `matplotlib`,
# `arabic_reshaper`, `itables` et `tunisia_data` plus bas, il l'est dans la seule
# fonction qui s'en sert, `series()`.
#
# Sans cela le module entier est inimportable sans pandas, et les fonctions purement
# textuelles qu'il porte — `date_deja_inscrite` — deviennent intestables : le job de
# tests n'installe aucune dépendance, précisément pour qu'un test qui réclame un
# paquet signale qu'il teste autre chose que ce qu'il annonce.
#
# La garde ci-dessous lie tout de même `pd` pour les annotations. `from __future__
# import annotations` suffirait à l'exécution, les annotations n'étant alors jamais
# évaluées ; mais le nom resterait non lié pour les vérificateurs de types et pour
# tout ce qui appelle `typing.get_type_hints()`.
if TYPE_CHECKING:  # pragma: no cover - jamais vrai à l'exécution
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
    "tab_base":   {"fr": "⚖️ Base législative", "ar": "⚖️ القاعدة التشريعية"},
    "base_intro": {"fr": "Chaque grandeur de la figure, avec toutes ses valeurs datées et "
                         "leurs références :",
                   "ar": "كلّ مقدار في الرسم البياني، بجميع قيمه المؤرّخة ومراجعها:"},
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


# Provenance déclarée par un module de figure, pour les séries qui ne viennent PAS de
# l'entrepôt. Le précis a deux origines de données : `tunisia-data` pour les statistiques
# publiées, et les paramètres d'`openfisca-tunisia` pour le droit codé. Les secondes n'ont
# pas de place dans le catalogue de l'entrepôt — ce ne sont pas des observations — mais
# elles doivent être sourcées comme les autres.
_DECLAREES: dict[str, dict] = {}


def register_provenance(series_id: str, **champs) -> None:
    """Déclare la provenance d'une série locale (paramètres openfisca, notamment).

    Mêmes champs que le catalogue de l'entrepôt : `titre`, `sources` (clés de citation),
    `unite`, `perimetre`, `caveats`, et leurs variantes `_ar`.
    """
    _DECLAREES[series_id] = {"id": series_id, **champs}


def meta(series_id: str) -> dict:
    """Provenance d'une série : déclaration locale, sinon entrepôt, sinon snapshot."""
    if series_id in _DECLAREES:
        return _DECLAREES[series_id]
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
    """Données d'une série : entrepôt si présent, sinon CSV snapshoté du précis.

    Vaut pour les DEUX origines du précis. Les séries de `tunisia-data` sont snapshotées
    par `refresh_cache()` ; celles qui viennent des paramètres d'openfisca — du droit codé,
    non des observations — sont snapshotées par les générateurs de tableaux, qui lisent
    déjà ces paramètres. Dans les deux cas le build ne voit qu'un CSV versionné, et une
    figure n'a jamais à lire une source vive (#165).

    `register_provenance` reste le moyen de déclarer la provenance d'une série absente du
    catalogue de l'entrepôt ; il ne dit rien de l'endroit où vivent ses données.
    """
    td = _td()
    if td is not None:
        try:
            return td.load(series_id)
        except Exception:
            pass
    p = _CACHE / f"{series_id}.csv"
    if p.exists():
        import pandas as pd  # import différé : voir l'en-tête du module

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


def date_deja_inscrite(ancien_texte: str | None, entete_sans_date: list[str],
                       corps: str) -> str | None:
    """Rend la date du figdata existant si RIEN d'autre n'a changé, sinon `None`.

    Fonction pure : elle reçoit le texte déjà écrit, et ne lit aucun fichier.

    `None` — donc une date neuve — dès que le fichier est absent, que sa provenance
    diffère (séries, sources, fiches, réserves, note) ou que ses données diffèrent.
    La date ne survit qu'à un rendu strictement identique.
    """
    if not ancien_texte:
        return None
    lignes = ancien_texte.split("\n")
    entete = []
    for ligne in lignes:
        if not ligne.startswith("#"):
            break
        entete.append(ligne)
    if not entete:
        return None
    if entete[1:] != entete_sans_date:
        return None
    if "\n".join(lignes[len(entete):]) != corps:
        return None
    date = entete[0].rsplit(" ", 1)[-1].strip()
    # Une date doit ressembler à une date. Sur un en-tête tronqué, `rsplit` rend le mot
    # qui précède : « … généré le » donne « le », valeur non vide qui serait réécrite
    # telle quelle dans le fichier — l'en-tête de provenance afficherait « généré le le ».
    # Vérifier la forme couvre du même coup l'en-tête corrompu.
    try:
        _dt.date.fromisoformat(date)
    except ValueError:
        return None
    return date


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
    # Deux séries peuvent partager la même fiche de source : c'est le cas dès qu'une figure
    # joint un montant et son dénominateur, tirés du même classeur du ministère. Les clés de
    # citation étaient déjà dédoublonnées ; les fiches et les réserves ne l'étaient pas, et
    # l'en-tête de provenance répétait alors deux fois le même fichier — dans un CSV publié
    # et téléchargeable, où il tient lieu de source.
    fiches = list(dict.fromkeys(fiches))
    caveats = list(dict.fromkeys(caveats))
    # un shortcode Quarto non résolu (passé tel quel depuis un chunk) → date du jour
    if not generated or "{{" in generated:
        generated = _dt.date.today().isoformat()
    entete_sans_date = [
        f"# séries (tunisia_data) : {', '.join(series_ids)}",
        f"# sources (citation) : {', '.join('@'+k for k in dict.fromkeys(keys))}",
        f"# fiches : {', '.join(fiches)}",
        f"# méthode/hypothèses : {', '.join(caveats)}",
    ]
    if note:
        entete_sans_date.append(f"# note : {note}")
    corps = df.to_csv(index=False)
    # Un rendu qui ne change ni les données ni la provenance ne doit pas redater le
    # fichier : sinon chaque `quarto render` salit le dépôt d'une vingtaine de figdata
    # dont SEULE la date bouge, qu'il faut ensuite restaurer à la main avant tout
    # commit. Le 16/09/2026, quatre restaurations en une matinée.
    #
    # La date n'est conservée que si l'en-tête HORS date est lui aussi inchangé. Une
    # légende, une source ou une réserve modifiée doit redater : à défaut, l'en-tête
    # de provenance — qui tient lieu de source dans un CSV publié et téléchargeable —
    # mentirait sur la date de ce qu'il décrit.
    try:
        ancien = out_csv.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        ancien = None
    stamp = date_deja_inscrite(ancien, entete_sans_date, corps) or generated
    header = [f"# Figure-data du précis socio-fiscal tunisien — généré le {stamp}"]
    header += entete_sans_date
    nouveau_csv = "\n".join(header) + "\n" + corps
    # `date_deja_inscrite` rend déjà l'ancienne date quand le contenu (hors date) n'a
    # pas changé, ce qui suffit à ce que le CSV réécrit soit OCTET POUR OCTET identique
    # à l'existant. Mais réécrire quand même touche le fichier : mtime modifié, et
    # certains outils (rsync, un `make` qui dépend des horodatages) le voient comme
    # changé alors que git ne le verrait pas. On compare donc le contenu produit à
    # l'existant et on n'écrit que s'il diffère — ni le CSV, ni son sidecar.
    if ancien != nouveau_csv:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            f.write(nouveau_csv)
    # sidecar yaml (lisible machine)
    side = out_csv.with_suffix(out_csv.suffix + ".yml")
    nouveau_side = "series: [{}]\nsources: [{}]\nfiches: [{}]\ncaveats: [{}]\ngenerated: {}\n".format(
        ", ".join(series_ids), ", ".join(dict.fromkeys(keys)),
        ", ".join(fiches), ", ".join(caveats), stamp)
    try:
        ancien_side = side.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        ancien_side = None
    if ancien_side != nouveau_side:
        side.write_text(nouveau_side, encoding="utf-8")
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


def base_legislative(*series_ids: str) -> str:
    """Liste Markdown des liens « Base législative » des séries, vide s'il n'y en a pas.

    Une série tirée du droit codé — et non d'une statistique publiée — est émise dans
    `_seriescache/` par un générateur de tableaux, qui écrit à côté d'elle la liste des
    grandeurs qu'il a lues : `<série>.liens.<langue>.yml`, même schéma que les
    `tables/<nom>.liens.yml` (`libelle`, `parametre`, `url`). Les liens sont donc
    engendrés, jamais écrits à la main ; on ne fait ici que les lire — le build du site
    n'importe pas le générateur.
    """
    import yaml

    vus, items = set(), []
    for sid in series_ids:
        f = _CACHE / f"{sid}.liens.{lang()}.yml"
        if not f.exists():
            continue
        for e in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            if e["url"] not in vus:
                vus.add(e["url"])
                items.append(f"- [{e['libelle']}]({e['url']})")
    if not items:
        return ""
    return f"{t('base_intro')}\n\n" + "\n".join(items)


def figure_tabs(fig, df: pd.DataFrame, *series_ids: str, slug: str,
                caption: str = "", note_lecture: str | None = None,
                fig_id: str | None = None, figdata_dir: str = "figdata",
                png_dir: str = "_fig", scroll_y: str = "420px",
                generated: str | None = None) -> None:
    """Composant générique : figure en **onglets** Graphique / Données / Sources.

    À appeler dans un chunk Quarto `#| output: asis`, **étiqueté** `#| label: fig-…`,
    dont c'est la dernière instruction. Produit :
      - onglet « Graphique » : l'image, la ligne « Source » courte, et — si fournie —
        une **note de lecture** ;
      - onglet « Données » : table **itables** scrollable + export CSV/Excel
        + téléchargement du **figdata sourcé** ;
      - onglet « Sources » : provenance détaillée (citation, **lien web** vers la
        source d'origine, fiche, fichiers bruts, périmètre, réserves) ;
      - onglet « Base législative », si une série tracée vient du droit codé : un lien
        par grandeur, lu dans `_seriescache/<série>.liens.<langue>.yml` (voir
        `base_legislative`).

    UNE SEULE FIGURE NUMÉROTÉE, CELLE DU CHUNK. L'étiquette du chunk fait de toute sa
    sortie — les onglets — une figure Quarto, et c'est elle que vise `@fig-…`. Sa légende
    est le DERNIER PARAGRAPHE de la sortie : Quarto la prend pour titre (« Figure N — … »).
    L'option `#| fig-cap:` n'est, elle, pas lue sur une sortie `asis` : la légende affichée
    est `caption`. L'image ne porte donc ni identifiant ni légende — elle en portait,
    et Quarto en faisait une sous-figure « (a) … » dans une figure à la légende vide.

    `fig`          : figure matplotlib (déjà rendue).
    `df`           : données de la figure (deviennent le figdata téléchargeable).
    `series_ids`   : id(s) de série `tunisia_data` (provenance/citation).
    `slug`         : identifiant de fichier (png + csv).
    `caption`      : **titre** de la figure (légende numérotée par Quarto).
    `note_lecture` : texte « Comment lire cette figure » (callout). Optionnel.
    `fig_id`       : pour un chunk NON étiqueté seulement — la sortie est alors enveloppée
                     dans sa propre figure `::: {#fig_id}`. Ne jamais le combiner avec
                     `#| label:` : on retomberait sur la figure dans la figure.
    """
    from itables import to_html_datatable

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
    base = base_legislative(*series_ids)
    onglet_base = f"## {t('tab_base')}\n\n{base}\n\n" if base else ""
    alt = caption.replace('"', "&quot;")
    sortie = f"""::: {{.panel-tabset}}

## {t('tab_graph')}

![]({png_path}){{fig-alt="{alt}"}}

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

{onglet_base}:::

{caption}
"""
    if fig_id:
        sortie = f"::: {{#{fig_id}}}\n\n{sortie}\n:::\n"
    print(sortie)

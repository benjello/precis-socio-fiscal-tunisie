"""Figure « partage de la valeur ajoutée » (part des salaires), annexe des comptes de la nation.

Sur le modèle de Cotis (2009) et d'Askenazy, Cette & Sylvain : la part des salaires dans la
valeur ajoutée des **sociétés non financières** (SNF) est l'indicateur de référence, car il
exclut le **revenu mixte** des entreprises individuelles (logé chez les ménages), qui mêle
rémunération du travail indépendant et profit. On la compare à la part « naïve » des salaires
dans le PIB de l'économie entière, nettement plus basse pour cette raison.

Données (entrepôt `tunisia-data`, snapshotées dans le précis) :
  - `cnat-approche-revenus-secteurs` : VA et rémunération des salariés par secteur ;
  - `cnat-approche-revenus` : rémunération et PIB de l'économie entière.

Tracé PAR SEGMENTS DE BASE (base 1997 jusqu'en 2014, base 2015 à partir de 2015) : les niveaux
ne se comparent pas d'une base à l'autre, un trait vertical marque le changement de base.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import figtools

SERIE_SECTEURS = "cnat-approche-revenus-secteurs"
SERIE_TOTAL = "cnat-approche-revenus"
SERIE_UNDATA = "cnat-approche-revenus-undata"  # économie entière, prolonge avant 2005
RUPTURES = (1997, 2015)  # changements de base sur la ligne longue

BLEU, VERT = "#0969da", "#1a7f37"

_L = {
    "y": {"fr": "Part des salaires (en %)", "ar": "حصة الأجور (%)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "snf": {"fr": "dans la VA des sociétés non financières",
            "ar": "من القيمة المضافة للشركات غير المالية"},
    "pib": {"fr": "dans le PIB (économie entière)", "ar": "من الناتج المحلي الإجمالي (كامل الاقتصاد)"},
    "rupt": {"fr": "changement de base (1997 → 2015)", "ar": "تغيير الأساس (1997 ← 2015)"},
    "ib_snf": {"fr": "{a} · SNF : {v} % de la VA (base {b})",
               "ar": "{a} · الشركات غير المالية: {v} % من القيمة المضافة (الأساس {b})"},
    "ib_pib": {"fr": "{a} · économie entière : {v} % du PIB (base {b})",
               "ar": "{a} · كامل الاقتصاد: {v} % من الناتج (الأساس {b})"},
}


def _ft(key, **kw):
    e = _L[key]
    s = e.get(figtools.lang(), e["fr"])
    return figtools.fig_text(s.format(**kw)) if kw else figtools.fig_text(s)


def _segments(points):
    """points : liste (annee, valeur, base) triée ; renvoie les segments par base continue."""
    segs, cur = [], []
    for a, v, b in points:
        if cur and (b != cur[-1][2]):
            segs.append(cur); cur = []
        cur.append((a, v, b))
    if cur:
        segs.append(cur)
    return segs


def _base_snf(annee: int) -> str:
    """SNF : base 1983 (2001-2004, seule disponible), 1997 (2005-2014), 2015 (≥ 2015)."""
    return "1983" if annee <= 2004 else ("1997" if annee <= 2014 else "2015")


def _serie_snf():
    """Part des salaires dans la VA des SNF, 2001-2025, par segments de base.

    2001-2004 : comptes sectoriels des éditions base 1983 ; 2005+ : approche des revenus
    par secteur (bases 1997 puis 2015). Au raccord 2005, les deux bases coïncident (~46 %).
    """
    d = figtools.series(SERIE_SECTEURS)
    d = d[d["secteur"] == "snf"].copy()
    d["annee"] = d["annee"].astype(int)
    d = d[d.apply(lambda r: str(r["base"]) == _base_snf(int(r["annee"])), axis=1)]
    return [(int(r.annee), float(r.part_remuneration_va), str(r.base))
            for r in d.sort_values("annee").itertuples()]


def _base_de(annee: int) -> str:
    """Un an, une base : économie entière segmentée 1983 / 1997 / 2015."""
    return "1983" if annee <= 1996 else ("1997" if annee <= 2014 else "2015")


def _serie_pib():
    """Part des salaires dans le PIB (économie entière), 1992-2025, par segments de base.

    INS (`cnat-approche-revenus`) où disponible (2005+), ONU (`cnat-approche-revenus-undata`,
    comptes INS transmis aux Nations unies) pour prolonger avant 2005.
    """
    ins, und = figtools.series(SERIE_TOTAL).copy(), figtools.series(SERIE_UNDATA).copy()
    val = {}
    for d, src in ((und, "onu"), (ins, "ins")):  # ins écrase onu sur le recouvrement
        d["annee"] = d["annee"].astype(int)
        for r in d.itertuples():
            a, b = int(r.annee), str(r.base)
            if b == _base_de(a):
                val[a] = (float(r.part_remuneration_pib), b)
    return [(a, v, b) for a, (v, b) in sorted(val.items())]


def figure():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for pts, couleur, lab, ibk in ((_serie_snf(), BLEU, "snf", "ib_snf"),
                                   (_serie_pib(), VERT, "pib", "ib_pib")):
        first = True
        for seg in _segments(pts):
            xs = [a for a, _, _ in seg]
            ys = [v for _, v, _ in seg]
            ax.plot(xs, ys, "-o", color=couleur, ms=3.5, lw=1.6,
                    label=_ft(lab) if first else None)
            first = False
            for a, v, b in seg:
                p, = ax.plot([a], [v], "o", color=couleur, ms=3.5)
                figtools.infobulle(p, _ft(ibk, a=a, v=f"{v:.1f}".replace(".", ","), b=b))
    for an in RUPTURES:
        figtools.marque_rupture(ax, an, _ft("rupt") if an == RUPTURES[0] else None)
    ax.set_ylabel(_ft("y"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.set_ylim(30, 65)
    ax.grid(True, axis="y", lw=0.4, alpha=0.5)
    ax.legend(fontsize=8, loc="lower right", frameon=False)
    fig.tight_layout()
    return fig


def table():
    """Données de la figure : part des salaires SNF et PIB, et taux de marge SNF, par base."""
    import pandas as pd
    snf = {a: (v, b) for a, v, b in _serie_snf()}
    lignes = []
    for a, v, b in _serie_pib():  # économie entière, 1992-2025
        s = snf.get(a)
        lignes.append({"annee": a, "base": b,
                       "part_salaires_pib_pct": round(v, 1),
                       "part_salaires_snf_pct": round(s[0], 1) if s else None,
                       "taux_marge_snf_pct": round(100 - s[0], 1) if s else None})
    return pd.DataFrame(lignes)


# =====================================================================================
# Figures compl\u00e9mentaires du partage de la valeur ajout\u00e9e (calculs \u00e9tendus)
# =====================================================================================

SECTEURS_LABELS = {
    "snf": {"fr": "Soci\u00e9t\u00e9s non financi\u00e8res", "ar": "\u0634\u0631\u0643\u0627\u062a \u063a\u064a\u0631 \u0645\u0627\u0644\u064a\u0629"},
    "sf": {"fr": "Soci\u00e9t\u00e9s financi\u00e8res", "ar": "\u0634\u0631\u0643\u0627\u062a \u0645\u0627\u0644\u064a\u0629"},
    "apu": {"fr": "Administrations publiques", "ar": "\u0625\u062f\u0627\u0631\u0627\u062a \u0639\u0645\u0648\u0645\u064a\u0629"},
    "menages": {"fr": "M\u00e9nages (y.c. entrepreneurs individuels)", "ar": "\u0623\u0633\u0631"},
}
SECTEURS_COULEURS = {"snf": "#0969da", "sf": "#8250df", "apu": "#d1242f", "menages": "#1a7f37"}


def _eco_3parts():
    """\u00c9conomie enti\u00e8re, 3 parts (travail, capital, imp\u00f4ts nets) en % du PIB, 1992-2025, par base.
    INS (\u2265 2005) compl\u00e9t\u00e9 par l'ONU (1992-2004). Renvoie [(annee, travail, capital, impots, base)]."""
    ins = figtools.series(SERIE_TOTAL).copy()
    und = figtools.series(SERIE_UNDATA).copy()
    val = {}
    for d, src in ((und, "onu"), (ins, "ins")):
        d["annee"] = d["annee"].astype(int)
        for r in d.itertuples():
            a, b = int(r.annee), str(r.base)
            if b != _base_de(a):
                continue
            trav = float(r.part_remuneration_pib)
            capi = float(r.part_revenu_exploitation_pib)
            val[a] = (trav, capi, round(100 - trav - capi, 2), b)
    return [(a, *v) for a, v in sorted(val.items())]


def figure_distribution():
    """Distribution fonctionnelle du revenu de l'\u00e9conomie enti\u00e8re, en aires empil\u00e9es par base."""
    pts = _eco_3parts()
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    etq = [("travail", 0, "#0969da"), ("capital", 1, "#d1242f"), ("impots", 2, "#8a8a8a")]
    lab = {"travail": {"fr": "Travail (r\u00e9mun\u00e9ration des salari\u00e9s)", "ar": "\u0627\u0644\u0639\u0645\u0644"},
           "capital": {"fr": "Capital (exc\u00e9dent + revenu mixte)", "ar": "\u0631\u0623\u0633 \u0627\u0644\u0645\u0627\u0644"},
           "impots": {"fr": "Imp\u00f4ts nets sur la production", "ar": "\u0636\u0631\u0627\u0626\u0628 \u0635\u0627\u0641\u064a\u0629"}}
    # segments par base continue
    segs, cur = [], []
    for row in pts:
        b = row[4]
        if cur and b != cur[-1][4]:
            segs.append(cur); cur = []
        cur.append(row)
    if cur:
        segs.append(cur)
    first = True
    for seg in segs:
        xs = [r[0] for r in seg]
        trav = [r[1] for r in seg]; capi = [r[2] for r in seg]; imp = [r[3] for r in seg]
        etqs = ([figtools.fig_text(lab[k]["fr"] if figtools.lang() == "fr" else lab[k]["ar"])
                 for k in ("travail", "capital", "impots")] if first else ["_nolegend_"] * 3)
        ax.stackplot(xs, trav, capi, imp,
                     colors=["#0969da", "#d1242f", "#8a8a8a"], alpha=0.85, labels=etqs)
        first = False
    for an in RUPTURES:
        figtools.marque_rupture(ax, an, None)
    ax.set_ylim(0, 100)
    ax.set_xlim(min(r[0] for r in pts), max(r[0] for r in pts))
    ax.set_ylabel(figtools.fig_text("En % du PIB" if figtools.lang() == "fr" else "% \u0645\u0646 \u0627\u0644\u0646\u0627\u062a\u062c"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.legend(fontsize=8, loc="center left", frameon=False)
    fig.tight_layout()
    return fig


def table_distribution():
    import pandas as pd
    return pd.DataFrame([{"annee": a, "base": b,
                          "part_travail_pct": round(t, 1), "part_capital_pct": round(c, 1),
                          "part_impots_nets_pct": round(i, 1)}
                         for a, t, c, i, b in _eco_3parts()])


def _base_snf_bis(a):  # alias local (\u00e9vite d'exposer _base_snf au module de test)
    return _base_snf(a)


def figure_secteurs():
    """Part des salaires dans la VA de chaque secteur institutionnel, 2001-2025, par base."""
    d = figtools.series(SERIE_SECTEURS).copy()
    d["annee"] = d["annee"].astype(int)
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    for sec, coul in SECTEURS_COULEURS.items():
        sub = d[d["secteur"] == sec]
        # un an, une base : SNF suit _base_snf ; autres secteurs 1997 (\u22642014) / 2015 (\u22652015)
        pts = []
        for r in sub.itertuples():
            a, b = int(r.annee), str(r.base)
            bref = _base_snf(a) if sec == "snf" else ("1997" if a <= 2014 else "2015")
            if b == bref:
                pts.append((a, float(r.part_remuneration_va), b))
        pts.sort()
        segs, cur = [], []
        for p in pts:
            if cur and p[2] != cur[-1][2]:
                segs.append(cur); cur = []
            cur.append(p)
        if cur:
            segs.append(cur)
        first = True
        lab = SECTEURS_LABELS[sec]["fr"] if figtools.lang() == "fr" else SECTEURS_LABELS[sec]["ar"]
        for seg in segs:
            ax.plot([p[0] for p in seg], [p[1] for p in seg], "-o", color=coul, ms=3, lw=1.5,
                    label=figtools.fig_text(lab) if first else None)
            first = False
    for an in RUPTURES:
        figtools.marque_rupture(ax, an, None)
    ax.set_ylim(0, 100)
    ax.set_ylabel(figtools.fig_text("Part des salaires dans la VA du secteur (%)"
                                    if figtools.lang() == "fr" else "\u062d\u0635\u0629 \u0627\u0644\u0623\u062c\u0648\u0631 (%)"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.grid(True, axis="y", lw=0.4, alpha=0.5)
    ax.legend(fontsize=7.5, loc="center left", frameon=False)
    fig.tight_layout()
    return fig


def table_secteurs():
    import pandas as pd
    d = figtools.series(SERIE_SECTEURS).copy()
    d["annee"] = d["annee"].astype(int)
    rows = []
    for r in d.sort_values(["annee", "secteur"]).itertuples():
        rows.append({"annee": int(r.annee), "base": str(r.base), "secteur": r.secteur,
                     "part_salaires_va_pct": round(float(r.part_remuneration_va), 1)})
    return pd.DataFrame(rows)


def _revenu_mixte_menages():
    """Revenu mixte des m\u00e9nages (leur revenu d'exploitation) en % du PIB, par base.
    C'est l'ordre de grandeur du capital 'contamin\u00e9' de travail ind\u00e9pendant qui s\u00e9pare la
    mesure \u00e9conomie enti\u00e8re de la mesure SNF."""
    sec = figtools.series(SERIE_SECTEURS).copy(); sec["annee"] = sec["annee"].astype(int)
    tot = figtools.series(SERIE_TOTAL).copy(); tot["annee"] = tot["annee"].astype(int)
    pib = {(int(r.annee), str(r.base)): float(r.pib_approche_revenus) for r in tot.itertuples()}
    out = []
    for r in sec[sec["secteur"] == "menages"].itertuples():
        a, b = int(r.annee), str(r.base)
        if (a, b) in pib:
            out.append((a, round(100 * float(r.revenu_exploitation) / pib[(a, b)], 2), b))
    out.sort()
    return out


def figure_revenu_mixte():
    pts = _revenu_mixte_menages()
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    segs, cur = [], []
    for p in pts:
        if cur and p[2] != cur[-1][2]:
            segs.append(cur); cur = []
        cur.append(p)
    if cur:
        segs.append(cur)
    for seg in segs:
        ax.plot([p[0] for p in seg], [p[1] for p in seg], "-o", color="#1a7f37", ms=3.5, lw=1.6)
    for an in RUPTURES:
        figtools.marque_rupture(ax, an, None)
    ax.set_ylabel(figtools.fig_text("Revenu mixte des m\u00e9nages (% du PIB)"
                                    if figtools.lang() == "fr" else "\u0627\u0644\u062f\u062e\u0644 \u0627\u0644\u0645\u062e\u062a\u0644\u0637 (% \u0645\u0646 \u0627\u0644\u0646\u0627\u062a\u062c)"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.grid(True, axis="y", lw=0.4, alpha=0.5)
    fig.tight_layout()
    return fig


def table_revenu_mixte():
    import pandas as pd
    return pd.DataFrame([{"annee": a, "base": b, "revenu_mixte_menages_pct_pib": v}
                         for a, v, b in _revenu_mixte_menages()])


# =====================================================================================
# Contracyclicité : part du travail vs croissance du PIB
# =====================================================================================

def _croissance_pib():
    """Croissance du PIB en volume, une valeur par année (base la plus récente qui la porte)."""
    g = figtools.series("pib-croissance-volume").copy()
    g["annee"] = g["annee"].astype(int)
    cr = {}
    for b in ("1983", "1997", "2015"):  # 2015 écrase (prioritaire)
        for r in g[g["base"].astype(str).str.contains(b, na=False)].itertuples():
            try:
                cr[int(r.annee)] = float(r.croissance_volume_pct)
            except (ValueError, TypeError):
                pass
    return cr


def _points_cyclicite():
    t = table.__wrapped__() if hasattr(table, "__wrapped__") else table()
    lp = {int(r.annee): r.part_salaires_pib_pct for r in t.itertuples()}
    ls = {int(r.annee): r.part_salaires_snf_pct for r in t.itertuples()
          if r.part_salaires_snf_pct == r.part_salaires_snf_pct}
    cr = _croissance_pib()
    pts = []
    for y in sorted(set(lp) & set(cr)):
        if y - 1 in lp and y in cr:
            dpib = lp[y] - lp[y - 1]
            dsnf = (ls[y] - ls[y - 1]) if (y in ls and y - 1 in ls) else None
            pts.append((y, cr[y], round(dpib, 2), round(dsnf, 2) if dsnf is not None else None))
    return pts


def figure_cyclicite():
    """Nuage : croissance du PIB (x) vs variation annuelle de la part des salaires (y)."""
    pts = _points_cyclicite()
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    xs = [c for _, c, _, _ in pts]
    ye = [d for _, _, d, _ in pts]
    ax.scatter(xs, ye, s=28, color="#1a7f37", zorder=3,
               label=figtools.fig_text("Δ part des salaires, économie entière"
                                        if figtools.lang() == "fr" else "Δ حصة الأجور، كامل الاقتصاد"))
    # droite de régression simple
    n = len(xs); mx = sum(xs) / n; my = sum(ye) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ye)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    xr = [min(xs), max(xs)]
    ax.plot(xr, [a + b * x for x in xr], "--", color="#57606a", lw=1.2)
    # repères d'années marquantes
    for y, c, d, _ in pts:
        if y in (2011, 2020, 2021):
            ax.annotate(str(y), (c, d), textcoords="offset points", xytext=(5, 4),
                        fontsize=8, color="#d1242f")
            ax.plot([c], [d], "o", ms=7, mfc="none", mec="#d1242f", zorder=4)
    ax.axhline(0, color="#ccc", lw=0.7)
    ax.axvline(0, color="#ccc", lw=0.7)
    ax.set_xlabel(figtools.fig_text("Croissance du PIB en volume (%)"
                                    if figtools.lang() == "fr" else "نمو الناتج بالحجم (%)"), fontsize=9)
    ax.set_ylabel(figtools.fig_text("Variation de la part des salaires (points)"
                                    if figtools.lang() == "fr" else "تغيّر حصة الأجور (نقاط)"), fontsize=9)
    ax.grid(True, lw=0.3, alpha=0.4)
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    fig.tight_layout()
    return fig


def table_cyclicite():
    import pandas as pd
    return pd.DataFrame([{"annee": y, "croissance_pib_volume_pct": c,
                          "var_part_salaires_pib_pts": d, "var_part_salaires_snf_pts": s}
                         for y, c, d, s in _points_cyclicite()])


def _composition_va():
    """Part de la VA de chaque secteur dans le PIB, par base (segments). Renvoie
    {secteur: [(annee, part, base)]}."""
    sec = figtools.series(SERIE_SECTEURS).copy(); sec["annee"] = sec["annee"].astype(int)
    tot = figtools.series(SERIE_TOTAL).copy(); tot["annee"] = tot["annee"].astype(int)
    pib = {(int(r.annee), str(r.base)): float(r.pib_approche_revenus) for r in tot.itertuples()}
    out = {s: [] for s in ("snf", "sf", "apu", "menages")}
    for r in sec.itertuples():
        a, b = int(r.annee), str(r.base)
        bref = "1997" if a <= 2014 else "2015"
        if b == bref and (a, b) in pib:
            out[r.secteur].append((a, round(100 * float(r.valeur_ajoutee) / pib[(a, b)], 2), b))
    for s in out:
        out[s].sort()
    return out


def figure_composition():
    """Aires empilées : part de la VA de chaque secteur dans le PIB, 2005-2025."""
    comp = _composition_va()
    ordre = ["snf", "menages", "apu", "sf"]
    coul = {"snf": "#0969da", "menages": "#1a7f37", "apu": "#d1242f", "sf": "#8250df"}
    annees = sorted({a for s in comp for a, _, _ in comp[s]})
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    # construire des segments continus par base (rupture 2015)
    for seg_an in ([a for a in annees if a <= 2014], [a for a in annees if a >= 2015]):
        if not seg_an:
            continue
        data = {}
        for s in ordre:
            d = dict((a, v) for a, v, _ in comp[s])
            data[s] = [d.get(a, float("nan")) for a in seg_an]
        ax.stackplot(seg_an, *[data[s] for s in ordre], colors=[coul[s] for s in ordre], alpha=0.85,
                     labels=[figtools.fig_text(SECTEURS_LABELS[s]["fr"] if figtools.lang() == "fr"
                                               else SECTEURS_LABELS[s]["ar"]) for s in ordre]
                     if seg_an[0] <= 2014 else ["_nolegend_"] * 4)
    figtools.marque_rupture(ax, 2015, None)
    ax.set_ylim(0, 100)
    ax.set_ylabel(figtools.fig_text("Part dans le PIB (%)" if figtools.lang() == "fr"
                                    else "الحصة من الناتج (%)"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.legend(fontsize=8, loc="upper center", ncol=2, frameon=False)
    fig.tight_layout()
    return fig


def table_composition():
    import pandas as pd
    comp = _composition_va()
    rows = {}
    for s, pts in comp.items():
        for a, v, b in pts:
            rows.setdefault((a, b), {})[s] = v
    return pd.DataFrame([{"annee": a, "base": b, **{f"part_va_{s}_pct": d.get(s) for s in
                          ("snf", "sf", "apu", "menages")}} for (a, b), d in sorted(rows.items())])


def figure_remuneration_excedent():
    """Rémunération vs excédent des SNF, indexés à 100 au début de chaque base — montre la
    divergence post-2011 (la rémunération s'écarte de l'excédent)."""
    sec = figtools.series(SERIE_SECTEURS).copy(); sec["annee"] = sec["annee"].astype(int)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    first = True
    for b, deb in (("1997", 2005), ("2015", 2015)):
        rows = sorted((int(r.annee), float(r.remuneration_salaries), float(r.revenu_exploitation))
                      for r in sec.itertuples() if r.secteur == "snf" and str(r.base) == b)
        if not rows:
            continue
        r0 = next(x for x in rows if x[0] == deb)
        xs = [y for y, _, _ in rows]
        rem = [100 * rm / r0[1] for _, rm, _ in rows]
        ebe = [100 * e / r0[2] for _, _, e in rows]
        ax.plot(xs, rem, "-o", color="#0969da", ms=3, lw=1.6,
                label=figtools.fig_text("Rémunération des salariés (SNF)" if figtools.lang() == "fr"
                                        else "تعويضات الأجراء (الشركات غير المالية)") if first else None)
        ax.plot(xs, ebe, "-s", color="#d1242f", ms=3, lw=1.6,
                label=figtools.fig_text("Excédent brut d'exploitation (SNF)" if figtools.lang() == "fr"
                                        else "فائض الاستغلال (الشركات غير المالية)") if first else None)
        first = False
    for an in RUPTURES:
        figtools.marque_rupture(ax, an, None)
    ax.set_ylabel(figtools.fig_text("Indice (début de base = 100)" if figtools.lang() == "fr"
                                    else "مؤشر (بداية الأساس = 100)"), fontsize=9)
    ax.set_xlabel(_ft("x"), fontsize=9)
    ax.grid(True, axis="y", lw=0.4, alpha=0.5)
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout()
    return fig

# Droits de douane : blocs prêts à coller dans `_droits_douane.qmd`

Fichier de travail du rédacteur des données et figures, 23 octobre 2026. Chaque bloc est à
coller tel quel ; les chemins supposent le chapitre dans `precis/fr/fiscalite/` (comme
`_timbre_enregistrement.qmd`). Les relevés sont dans `precis/fr/fiscalite/douane/`, le module
de figures dans `figures/droits_douane.py`, le contrôle dans
`scripts/verifier_figures_droits_douane.py`.

## Figures

Cadre commun : `import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")`,
`from figures import droits_douane as fig_dd`, `import figtools`. Les `slug` ne se heurtent à
aucun `figdata` existant. `register_provenance` est déjà appelé à l'import du module.

````markdown
```{python}
#| label: fig-dd-parts
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
from figures import droits_douane as fig_dd
import figtools
figtools.figure_tabs(
    fig_dd.fig_parts(), fig_dd.table_parts(), *fig_dd.SERIES_PARTS,
    slug="fig_dd_parts",
    caption=("Part de la rubrique « droits de douane », redevances de prestations douanières "
             "comprises, dans les recettes fiscales et dans les dépenses de l'État hors "
             "service de la dette, 1986-2025, en %"),
    note_lecture=(
        "La rubrique est celle du ministère des Finances ; elle comprend la redevance de "
        "prestations douanières. Les dépenses sont des réalisations, hors service de la "
        "dette. Les traits verticaux marquent l'entrée en vigueur du tarif de la loi de "
        "finances pour 1988, du calendrier de l'accord d'association avec l'Union "
        "européenne (1997), de la réduction des taux des chapitres 25 à 97 (2016, trait "
        "plein) et des relèvements de taux (2018). Le trait violet marque la nouvelle "
        "nomenclature du tableau A des lois de finances (2020) : la rubrique du ministère "
        "n'est pas interrompue."))
```

```{python}
#| label: fig-dd-pib
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
from figures import droits_douane as fig_dd
import figtools
figtools.figure_tabs(
    fig_dd.fig_pib(), fig_dd.table_pib(), *fig_dd.SERIES_PIB,
    slug="fig_dd_pib",
    caption=("Part de la rubrique « droits de douane », redevances de prestations douanières "
             "comprises, dans le PIB, par segment de base du PIB, 1986-2025, en % du PIB"),
    note_lecture=(
        "Le PIB n'est jamais chaîné d'une base à l'autre : chaque segment porte sa base, "
        "inscrite au-dessus du cadre, et un trait vertical marque chaque rupture (1997, "
        "2002, 2005, 2010, 2025 ; voir l'[annexe sur le PIB](../annexe-pib.html#sec-pib-ruptures)). "
        "Trait plein : base du PIB établie ; tirets : base 1983 présumée (1986-1991) ; "
        "pointillés et cercles creux, « n. r. » au-dessus du cadre : valeur propre au "
        "ministère des Finances, rattachée à aucune base (2002-2004 et 2025). « Rétropolée » "
        "désigne des valeurs que l'INS a recalculées à la base suivante."))
```

```{python}
#| label: fig-dd-rendement
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
from figures import droits_douane as fig_dd
import figtools
figtools.figure_tabs(
    fig_dd.fig_rendement(), fig_dd.table_rendement(), *fig_dd.SERIES_REND,
    slug="fig_dd_rendement",
    caption=("Droits de douane à l'importation et redevance de prestations douanières : "
             "prévisions des lois de finances, 2001-2026, et réalisations de la Cour des "
             "comptes, 2018-2024, en millions de dinars courants et en millions de dinars "
             "de 2025"),
    note_lecture=(
        "Le trait relie les prévisions du tableau A des lois de finances initiales ; le "
        "cercle creux est la réalisation publiée par la Cour des comptes. La redevance "
        "additionne l'importation et l'exportation : articles 21-02 et 21-03 jusqu'en 2019, "
        "article 17-02 depuis 2020 pour les prévisions, et les deux lignes que la Cour "
        "garde distinctes pour les réalisations. Le trait vertical marque la nouvelle "
        "nomenclature du tableau A (2020) : 17-01 reprend 21-01 et 17-02 fond 21-02 et "
        "21-03, de sorte que les courbes ne sont pas interrompues. Dinars de 2025 : indice "
        "des prix commun du précis, sans 2026."))
```

```{python}
#| label: fig-dd-perception
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
from figures import droits_douane as fig_dd
import figtools
figtools.figure_tabs(
    fig_dd.fig_perception(), fig_dd.table_perception(), *fig_dd.SERIES_PERC,
    slug="fig_dd_perception",
    caption=("Taux de perception implicite (rubrique « droits de douane », redevances "
             "comprises, rapportée aux importations) et moyennes simples des taux du tarif "
             "publiées par le GATT et l'OMC, 1987-2025, en %"),
    note_lecture=(
        "Le numérateur du taux de perception est la rubrique du ministère des Finances, qui "
        "comprend les redevances de prestations douanières ; le « régime général » rapporte "
        "cette rubrique entière aux seules importations de ce régime. Dénominateur : "
        "importations CAF de la Banque centrale (marqueurs creux, 1988-1997), puis de l'INS "
        "(annuaire, tableau 14.2, depuis 1998). Le trait vertical coupe les séries entre 2003 "
        "et 2004 : les années antérieures ne sont imprimées dans aucune édition de l'annuaire "
        "postérieure à la révision du régime off shore. Les losanges sont les moyennes "
        "simples des taux du tarif données par le GATT (1987-1989) et l'OMC (1994, "
        "2005-2016, 2025), chacune avec sa définition : 2014 n'est pas notifié, la valeur "
        "de 2025 est calculée à neuf chiffres comme celle de 2016, et celle de 2006 est "
        "telle que l'OMC l'imprime. Une moyenne simple se calcule sur les lignes du tarif, "
        "le taux de perception rapporte les recettes aux importations."))
```
````

Données de la figure `fig-dd-rendement` : 92 lignes (une par article imprimé) ; elle sert
aussi de relevé à citer dans le texte (prévisions : tableau A de chaque loi de finances ;
réalisations : Cour des comptes). Le relevé comprend les clés `lf-2001` à `lf-2026`,
`cdc-loireg-2019` à `cdc-loireg-2022`, `cdc-rapport-budget-2023`, `cdc-rapport-budget-2024`.

## Tableaux

`tarifs.imprime` imprime le corps ; la légende et la ligne de sources restent dans le `.qmd`.
Chaque ligne porte déjà sa citation (colonne « Texte et article »). Placer au-dessus des
quatre premiers : `<!-- TODO (rédacteur) : remplacer par un tableau engendré depuis les
paramètres -->` (redevance, correspondances, bandes, minimum de perception ; ligne
`backlog-modele.md` à ouvrir : série à fenêtre, aucun nœud douane dans le modèle).

````markdown
: Redevance de prestations douanières, 1988-2024 : assiette, taux et minimum de perception {#tbl-dd-redevance}

```{python}
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import tarifs
tarifs.imprime("douane/tarifs-releves-droits-douane.csv", "redevance")
```

: Tables de correspondance des taux du tarif, 1987, 1988 et 1994 : taux avant, taux après {#tbl-dd-correspondances}

```{python}
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import tarifs
tarifs.imprime("douane/tarifs-releves-droits-douane.csv", "correspondances")
```

: Étapes du tarif, 2004-2022 : taux remplacés, par texte et par champ {#tbl-dd-bandes}

```{python}
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import tarifs
tarifs.imprime("douane/tarifs-releves-droits-douane.csv", "bandes")
```

: Calendrier de démantèlement des droits à l'importation des produits originaires de la Communauté, accord d'association, article 11 : part du droit de base, par annexe {#tbl-dd-calendrier-ue}

```{python}
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import tarifs
tarifs.imprime("douane/tarifs-releves-droits-douane.csv", "calendrier-ue")
```

: Minimum de perception du tarif minimum *ad valorem* à l'importation, 1987 et 1988 {#tbl-dd-minimum}

```{python}
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import tarifs
tarifs.imprime("douane/tarifs-releves-droits-douane.csv", "minimum-perception")
```
````

Lignes de sources et réserves à écrire sous les tableaux, d'après le manifeste
`douane/tarifs-releves-droits-douane.csv.yml` :

- `tbl-dd-calendrier-ue` : @accord-association-ue-tunisie-1995, art. 11, § 2 et 3, pp. L 97/5-6.
  Annexes désignées par leur numéro seul (listes de codes de la nomenclature combinée sans
  intitulé dans l'accord) ; annexe 5 : « taux de base » dans le texte ; annexe 6 hors calendrier
  (art. 12) ; droit de base : droit effectivement appliqué à l'égard de la Communauté au
  1er janvier 1995 (§ 5). Seule correspondance lue avec l'année civile : la loi de finances
  pour 1997, art. 21, fait du 1er janvier 1997 le début de la deuxième année du calendrier.
  Aucune année civile en en-tête.
- `tbl-dd-correspondances` : les trois tables ne se chaînent pas ; la table de 1994 exclut les
  taux consolidés au GATT (art. 71, § 2) ; la table de 1987 exclut les produits du tableau « M ».
  Taux le plus élevé après transposition : 45 % (1987), 43 % (1988), 43 % (1994).
- `tbl-dd-bandes` : les seuls articles qui transposent un taux en un autre ; les articles 42 et
  43 de la LF 2016 (taux fixés sans taux antérieur) et l'article 81 de la LF 2019 (motocycles)
  n'y figurent pas ; aucune ligne ne donne l'état complet du tarif ; tarif « à deux taux » de
  2016 exact pour les seuls chapitres 25 à 97, sous réserve des annexes 2 et 3.

## Points à trancher ou à vérifier (hors rendu)

Voir le rapport de la tâche : écarts avec les notes, valeurs douteuses, lacunes.

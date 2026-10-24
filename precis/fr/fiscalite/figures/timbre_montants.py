"""Les montants du timbre et de l'enregistrement qui changent plus de trois fois, en escalier.

D'OÙ VIENNENT LES DONNÉES. De la série `timbre-montants-dates` (`precis/_seriescache/`),
une ligne par grandeur et par date d'effet : parametre, date_effet, valeur (dinars), unite,
famille, source (clé de citation du texte qui fixe le montant), ligne_du_registre (ancre du
registre du chapitre qui le porte), remarque. Les valeurs et les dates sont celles du chapitre
et de ses registres ; rien n'y est ajouté.

LE CHOIX DES GRANDEURS. Une grandeur est tracée quand son montant a plus de trois dates d'effet
dans le chapitre (au moins quatre). Les autres restent aux tableaux : timbre des actes par
feuille (3 dates, 1993-2018), timbre de dimension (3 dates, 1969-1986), carte d'identité
(3 dates), carte de séjour (3 dates), actes de sociétés (2 dates), visite technique (2 dates).
Les montants par dinar ou en pour cent (téléphone depuis 2012, taxe unique, droits
proportionnels) sont des taux : seul leur équivalent en dinars pour une recharge de 5 D est
tracé, calculé et dit tel dans la série.

DEUX VUES. Dinars courants, en escalier par date d'effet ; dinars de 2025, un point par année :
le montant moyen de l'année (moyenne des douze mois, un montant daté en cours d'année pèse au
prorata des mois) multiplié par l'indice des prix de 2025 et divisé par celui de l'année
(`scripts/dinars_constants.py`, indice des prix à la consommation de l'INS, base 1970 = 100).
La première année déflatée est 1970 : l'indice de la base 1962, raccordé à la base 1970 pour
1962-1969, n'intervient pas. Les indices de 2024 et 2025 prolongent celui de 2023 par la variation
de l'indice en base 2015 que relaie la Banque centrale : c'est le seul raccord, dit sous chaque
figure.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402

SERIE = "timbre-montants-dates"
BASE = dinars_constants.ANNEE_BASE
FIN = 2026

figtools.register_provenance(
    SERIE,
    titre=("Montants du timbre et de l'enregistrement à plus de trois dates d'effet, "
           "1969-2026 : droit fixe, minimum de perception, timbres des factures, des effets, "
           "du titre de crédit et du téléphone, passeport, renouvellement de la carte"),
    sources=["loi-93-53-cdet", "lf-1969", "lf-1977", "loi81-100-lf1982", "lf-1983",
             "loi85-109-lf1986", "loi-89-115-lf-1990", "lf-1997", "lf-1999", "lf-2001",
             "lf-2003", "lf-2004", "lf-2005", "lf-2006", "lfc-2012", "lf-2013", "lfc-2014",
             "lf-2017", "lf-2018", "dl2021-21-lf2022", "lf-2023", "lf-2026"],
    unite="dinars courants",
    perimetre=("quatorze grandeurs, une ligne par date d'effet : droit fixe par page ; minimum "
               "de perception des actes et des jugements par juridiction ; timbre des "
               "factures, des effets domiciliés et des autres effets, du titre de crédit ; "
               "timbre d'une carte et d'une recharge de 5 D ; passeport, passeport des "
               "étudiants ; renouvellement de la carte pour perte"),
    caveats=("Les montants sont ceux des textes, lus dans les registres du chapitre ; les "
             "dates sans clause d'effet sont celles où le texte devient exécutoire. Le 25 mai "
             "2012 est la date retenue par l'administration fiscale pour la loi de finances "
             "complémentaire. Le timbre du téléphone depuis 2012 est un taux par dinar : "
             "l'équivalent pour 5 D est un calcul, distingué dans la colonne famille. Avant le "
             "6 500 D du passeport de 1983, la date du montant de 6,500 D n'est pas établie."),
)

_METHODE = (
    "Dinars de {base} : chaque montant est la moyenne des douze mois de l'année, multipliée par "
    "l'indice des prix à la consommation de {base} et divisée par celui de l'année (INS, base "
    "1970 = 100, moyenne annuelle). Les indices de 2024 et 2025 prolongent celui de 2023 par la "
    "variation de l'indice en base 2015 que relaie la Banque centrale : c'est le seul raccord de "
    "la période. La première année déflatée est la première année pleine du montant. La vue "
    "s'arrête en {base}, dernier indice publié.")

BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS = ("#0969da", "#bc4c00", "#1a7f37", "#8250df",
                                           "#d1242f", "#57606a")


def _d(v: float) -> str:
    """Un montant en dinars, trois décimales si la valeur est inférieure à 1 D."""
    if v >= 1:
        t = f"{v:g}"
    else:
        t = f"{v:.3f}"
    return t.replace(".", ",") + " D"


FIGURES = {
    "droit-fixe": dict(
        courbes={"droit_fixe_page": ("Droit fixe d'enregistrement par page", BLEU)},
        slug="fig_te_droit_fixe", fin=FIN, log=False,
        caption=("Droit fixe d'enregistrement par page, à chaque date d'effet, 1993-2026, en "
                 "dinars courants et en dinars de 2025"),
        note=("Le droit fixe est celui de l'article 23 du code pour la plupart des actes ; "
              "les actes sans tarif ont eu un tarif propre de 5 puis de 10 D de 1993 à 2004. "
              "Avant 1993, le droit fixe est un montant par acte, qui varie selon l'acte "
              "(tableau 1969-1993)."),
        ylabel="Droit fixe par page, en dinars courants",
        yc="Droit fixe par page, en dinars de {base}", dec=1),
    "minimum": dict(
        courbes={"minimum_actes": ("Minimum de perception, actes et mutations", BLEU),
                 "minimum_jug_cantonaux": ("Jugements des tribunaux cantonaux", ORANGE),
                 "minimum_jug_premiere_instance": ("Jugements de première instance", VERT),
                 "minimum_jug_appel_cassation": ("Arrêts d'appel et de cassation, tribunal administratif", VIOLET)},
        slug="fig_te_minimum", fin=FIN, log=True, ncol=2,
        caption=("Minimum de perception des droits d'enregistrement, des actes et des jugements "
                 "par juridiction, 1969-2026, en dinars courants et en dinars de 2025"),
        note=("Les minima des jugements se distinguent par juridiction de 1977 à 2016 ; "
              "en 2017, un minimum unique de 40 D remplace tous les minima. Le tribunal "
              "administratif est rangé avec les arrêts d'appel et de cassation dès le code de "
              "1993. L'échelle verticale est logarithmique."),
        ylabel="Minimum de perception, en dinars courants (échelle logarithmique)",
        yc="Minimum de perception, en dinars de {base} (échelle logarithmique)", dec=2),
    "factures": dict(
        courbes={"factures": ("Timbre des quittances, puis des factures", BLEU)},
        slug="fig_te_factures", fin=FIN, log=False,
        caption=("Timbre des quittances, puis des factures, à chaque date d'effet, 1993-2026, "
                 "en dinars courants et en dinars de 2025"),
        note=("Le montant est celui d'une facture ordinaire ; les factures de téléphonie, les "
              "tickets de caisse (0,100 D en 2022) et les factures des grandes surfaces "
              "(1,500 ou 2 D en 2026) ont un timbre propre, au registre."),
        ylabel="Timbre par facture, en dinars courants",
        yc="Timbre par facture, en dinars de {base}", dec=3),
    "effets": dict(
        courbes={"effets_domicilies": ("Effets domiciliés", BLEU),
                 "autres_effets": ("Autres effets", ORANGE)},
        slug="fig_te_effets", fin=FIN, log=True,
        caption=("Timbre des effets de commerce, effets domiciliés et autres effets, à chaque "
                 "date d'effet, 1969-2026, en dinars courants et en dinars de 2025"),
        note=("Avant 1990, le timbre des effets autres que domiciliés est proportionnel à leur "
              "montant, en pour mille : il n'est pas tracé. De 1990 à 1992, les effets "
              "domiciliés restent à 0,100 D. L'échelle verticale est logarithmique."),
        ylabel="Timbre par effet, en dinars courants (échelle logarithmique)",
        yc="Timbre par effet, en dinars de {base} (échelle logarithmique)", dec=3),
    "titre-credit": dict(
        courbes={"titre_de_credit": ("Titre de crédit", BLEU)},
        slug="fig_te_titre_credit", fin=FIN, log=False,
        caption=("Timbre du titre de crédit, à chaque date d'effet, 2001-2026, en dinars "
                 "courants et en dinars de 2025"),
        note=("Le timbre du titre de crédit naît au 1^er^ janvier 2001 (loi de finances pour 2001, "
              "art. 64)."),
        ylabel="Timbre du titre de crédit, en dinars courants",
        yc="Timbre du titre de crédit, en dinars de {base}", dec=2),
    "telephone": dict(
        courbes={"telephone_carte_5d": ("Carte de recharge de 5 D", BLEU),
                 "telephone_recharge_5d": ("Recharge de 5 D sans carte", ORANGE)},
        slug="fig_te_telephone", fin=FIN, log=False,
        caption=("Timbre d'une carte ou d'une recharge de téléphone de 5 D, à chaque date "
                 "d'effet, 2006-2026, en dinars courants et en dinars de 2025"),
        note=("Depuis le 25 mai 2012, le timbre des cartes de 5 D au plus est un taux par "
              "dinar (0,080, 0,100 puis 0,140 D) : le montant tracé est l'équivalent pour 5 D, "
              "soit le taux multiplié par 5, calculé ici ; le timbre des recharges sans carte "
              "est de 0,400 puis 0,500 D par tranche de 5 D, puis un taux par dinar depuis 2018, "
              "avec 0,100 D de plus par recharge de 5 D ou plus en 2026."),
        ylabel="Timbre pour 5 D de recharge, en dinars courants",
        yc="Timbre pour 5 D de recharge, en dinars de {base}", dec=3),
    "passeport": dict(
        courbes={"passeport": ("Passeport", BLEU),
                 "passeport_etudiants": ("Passeport des étudiants", ORANGE)},
        slug="fig_te_passeport", fin=FIN, log=True,
        caption=("Timbre du passeport et du passeport des étudiants, à chaque date d'effet, "
                 "1969-2026, en dinars courants et en dinars de 2025"),
        note=("Avant le 2 janvier 1983, le passeport coûtait 6,500 D et celui des étudiants "
              "2 D, à des dates que les textes lus n'établissent pas : la courbe saute de 3,750 "
              "à 10 D en 1983. L'échelle verticale est logarithmique."),
        ylabel="Timbre du passeport, en dinars courants (échelle logarithmique)",
        yc="Timbre du passeport, en dinars de {base} (échelle logarithmique)", dec=2),
    "carte-perte": dict(
        courbes={"renouvellement_carte_perte": ("Renouvellement de la carte pour perte", BLEU)},
        slug="fig_te_carte_perte", fin=FIN, log=False,
        caption=("Timbre du renouvellement de la carte d'identité ou de séjour pour perte ou "
                 "destruction, à chaque date d'effet, 1993-2026, en dinars courants et en "
                 "dinars de 2025"),
        note=("Le montant de 2014 est celui du « renouvellement de la carte d'identité » du "
              "tableau de l'article 117."),
        ylabel="Timbre du renouvellement, en dinars courants",
        yc="Timbre du renouvellement, en dinars de {base}", dec=2),
}


def figure(nom: str, generated: str | None = None) -> None:
    f = FIGURES[nom]
    figtools.figure_escalier(
        SERIE, f["courbes"], slug=f["slug"], caption=f["caption"],
        note_lecture=f["note"] + " " + _METHODE.format(base=BASE),
        generated=generated, fin=f["fin"], constants=True, base=BASE,
        ipc=dinars_constants.ipc(), series_ipc=dinars_constants.SERIES_IPC,
        decimales_constants=f["dec"], ylabel=f["ylabel"], ylabel_constants=f["yc"],
        format_valeur=_d, log=f["log"], **({"ncol": f["ncol"]} if "ncol" in f else {}))

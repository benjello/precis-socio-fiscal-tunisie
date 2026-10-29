"""Aides aux élèves et aux étudiants : montants du droit en dinars courants et en dinars de 2023.

Chaque ligne est un montant fixé par un texte (clé de citation et article dans la colonne
`texte`), ou un crédit prévu par un document budgétaire (clé et page). Le montant en dinars de
2023 est le montant courant multiplié par le rapport de l'indice des prix à la consommation de
2023 à celui de l'année d'effet ; pour une année scolaire ou universitaire, l'année d'effet est
celle où elle commence. L'indice est celui du précis (`scripts/dinars_constants.py` :
`ipc-longue-periode`, base 100 en 1970, qui reprend les annuaires statistiques de l'INS à partir
de 1976) ; l'année de base est 2023, celle que la fiche de plan du livre retient, et non
`dinars_constants.ANNEE_BASE`. Aucun montant antérieur à 1976 n'est converti.

Usage : uv run python precis/fr/education/figures/fig_educ_aides_dinars_constants.py
Écrit `figdata/fig_educ_aides_dinars_constants.csv` et son sidecar `.yml`, que les tableaux
de `_aides.qmd` reprennent. Le module n'est pas appelé au rendu.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parents[3] / "scripts"))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402

ANNEE_BASE = 2023
SERIE_LOCALE = "educ-aides-montants-du-droit"

# (tableau, grandeur, date d'effet telle que le texte la donne, année de l'indice,
#  montant courant, unité, texte)
LIGNES = [
    # Droits d'inscription, d'assurance et de bibliothèque (par élève et par an)
    ("droits", "collège et lycée", "septembre 1992", 1992, 2.5, "D", "decret-92-1185-droits-inscription, art. 1 et 3, p. 816"),
    ("droits", "collège et lycée", "septembre 1997", 1997, 5.0, "D", "decret-97-1355-droits-inscription, art. 1 et 2, p. 1345"),
    ("droits", "primaire", "2010", 2010, 2.0, "D", "decret-2010-1928-droits-inscription, art. 1, p. 2247"),
    ("droits", "collège et lycée", "2010", 2010, 5.0, "D", "decret-2010-1928-droits-inscription, art. 1, p. 2247"),
    ("droits", "primaire", "année scolaire 2019-2020", 2019, 4.0, "D", "decret-gouv-2019-898-droits-inscription, art. 1 et 2, p. 3620-3621 (édition arabe)"),
    ("droits", "collège et lycée", "année scolaire 2019-2020", 2019, 8.6, "D", "decret-gouv-2019-898-droits-inscription, art. 1 et 2, p. 3620-3621 (édition arabe)"),
    # Crédits d'intervention du ministère de l'Éducation (prévisions, MD)
    ("cantines", "bourses scolaires et de formation", "2013", 2013, 7.394, "MD", "budget-men-2013, p. 29"),
    ("cantines", "cantines des écoles primaires", "2013", 2013, 14.560, "MD", "budget-men-2013, p. 29"),
    ("cantines", "aides scolaires", "2013", 2013, 1.020, "MD", "budget-men-2013, p. 29"),
    ("cantines", "total des interventions", "2013", 2013, 35.285, "MD", "budget-men-2013, p. 29"),
    ("cantines", "bourses scolaires et de formation", "2014", 2014, 7.394, "MD", "budget-men-2014, p. 32"),
    ("cantines", "cantines des écoles primaires", "2014", 2014, 24.000, "MD", "budget-men-2014, p. 32"),
    ("cantines", "aides scolaires", "2014", 2014, 1.020, "MD", "budget-men-2014, p. 32"),
    ("cantines", "total des interventions", "2014", 2014, 44.725, "MD", "budget-men-2014, p. 32"),
    ("cantines", "bourses scolaires et de formation", "2015", 2015, 7.394, "MD", "budget-men-2015, p. 31"),
    ("cantines", "cantines des écoles primaires", "2015", 2015, 24.000, "MD", "budget-men-2015, p. 31"),
    ("cantines", "aides scolaires", "2015", 2015, 1.020, "MD", "budget-men-2015, p. 31"),
    ("cantines", "total des interventions", "2015", 2015, 44.725, "MD", "budget-men-2015, p. 31"),
    ("cantines", "bourses scolaires et de formation", "2016", 2016, 7.394, "MD", "budget-men-2016, p. 30"),
    ("cantines", "cantines des écoles primaires", "2016", 2016, 24.000, "MD", "budget-men-2016, p. 30"),
    ("cantines", "aides scolaires", "2016", 2016, 2.002, "MD", "budget-men-2016, p. 30"),
    ("cantines", "total des interventions", "2016", 2016, 44.725, "MD", "budget-men-2016, p. 30"),
    ("cantines", "bourses scolaires et de formation", "2017", 2017, 0.872, "MD", "budget-men-2017, p. 30"),
    ("cantines", "cantines des écoles primaires", "2017", 2017, 24.000, "MD", "budget-men-2017, p. 30"),
    ("cantines", "aides scolaires", "2017", 2017, 2.252, "MD", "budget-men-2017, p. 30"),
    ("cantines", "total des interventions", "2017", 2017, 38.753, "MD", "budget-men-2017, p. 30"),
    # Budget prévisionnel de l'office des services scolaires (annexe des lois de finances, MD)
    ("office", "subvention de l'État", "2017", 2017, 36.550, "MD", "lf-2017, annexe, p. 4283 (édition arabe)"),
    ("office", "ressources propres", "2017", 2017, 5.616, "MD", "lf-2017, annexe, p. 4283 (édition arabe)"),
    ("office", "total", "2017", 2017, 42.166, "MD", "lf-2017, annexe, p. 4283 (édition arabe)"),
    ("office", "subvention de l'État", "2019", 2019, 71.973, "MD", "loi2018-56-lf2019, annexe, p. 5616 (édition arabe)"),
    ("office", "ressources propres", "2019", 2019, 5.600, "MD", "loi2018-56-lf2019, annexe, p. 5616 (édition arabe)"),
    ("office", "total", "2019", 2019, 77.573, "MD", "loi2018-56-lf2019, annexe, p. 5616 (édition arabe)"),
    ("office", "subvention de l'État", "2020", 2020, 69.981, "MD", "lf-2020, annexe, p. 4783 (édition arabe)"),
    ("office", "ressources propres", "2020", 2020, 5.600, "MD", "lf-2020, annexe, p. 4783 (édition arabe)"),
    ("office", "total", "2020", 2020, 75.581, "MD", "lf-2020, annexe, p. 4783 (édition arabe)"),
    # Bourse nationale en Tunisie, montant mensuel
    ("bourse", "premier niveau", "1er janvier 1988", 1988, 40, "D/mois", "arrete-1988-03-31-bourses-montants, art. 1 et 2, p. 548-549"),
    ("bourse", "troisième cycle", "1er janvier 1988", 1988, 70, "D/mois", "arrete-1988-03-31-bourses-montants, art. 1, p. 548-549"),
    ("bourse", "premier niveau", "année universitaire 1991-1992", 1991, 40, "D/mois", "arrete-1992-03-07-bourses-montants, art. 1, p. 360"),
    ("bourse", "spécialisation", "année universitaire 1991-1992", 1991, 70, "D/mois", "arrete-1992-03-07-bourses-montants, art. 1, p. 360"),
    ("bourse", "études doctorales", "année universitaire 1991-1992", 1991, 140, "D/mois", "arrete-1992-03-07-bourses-montants, art. 1, p. 360"),
    ("bourse", "premier niveau", "année universitaire 1997-1998", 1997, 50, "D/mois", "arrete-1997-08-18-bourses-montants, art. 1, p. 1614-1615"),
    ("bourse", "spécialisation", "année universitaire 1997-1998", 1997, 70, "D/mois", "arrete-1997-08-18-bourses-montants, art. 1, p. 1614-1615"),
    ("bourse", "études doctorales", "année universitaire 1997-1998", 1997, 140, "D/mois", "arrete-1997-08-18-bourses-montants, art. 1, p. 1614-1615"),
    ("bourse", "premier niveau", "année universitaire 2011-2012", 2011, 60, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1 et 3, p. 2566-2567"),
    ("bourse", "second niveau", "année universitaire 2011-2012", 2011, 80, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1, p. 2566-2567"),
    ("bourse", "mastère, 1re année", "année universitaire 2011-2012", 2011, 100, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1, p. 2566-2567"),
    ("bourse", "mastère, 2e année", "année universitaire 2011-2012", 2011, 140, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1, p. 2566-2567"),
    ("bourse", "études doctorales", "année universitaire 2011-2012", 2011, 250, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1, p. 2566-2567"),
    ("bourse", "premier niveau", "année universitaire 2015-2016", 2015, 80, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "second niveau", "année universitaire 2015-2016", 2015, 110, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 1re année", "année universitaire 2015-2016", 2015, 120, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 2e année", "année universitaire 2015-2016", 2015, 160, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "études doctorales", "année universitaire 2015-2016", 2015, 250, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "premier niveau", "année universitaire 2016-2017", 2016, 100, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "second niveau", "année universitaire 2016-2017", 2016, 130, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 1re année", "année universitaire 2016-2017", 2016, 140, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 2e année", "année universitaire 2016-2017", 2016, 180, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "études doctorales", "année universitaire 2016-2017", 2016, 250, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "premier niveau", "année universitaire 2017-2018", 2017, 120, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "second niveau", "année universitaire 2017-2018", 2017, 160, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 1re année", "année universitaire 2017-2018", 2017, 160, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "mastère, 2e année", "année universitaire 2017-2018", 2017, 200, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "études doctorales", "année universitaire 2017-2018", 2017, 250, "D/mois", "arrete-2015-12-04-bourses-montants, art. 1, p. 2936"),
    ("bourse", "bourse d'intégration universitaire", "année universitaire 2018-2019", 2018, 500, "D, une fois", "arrete-2018-12-04-bourse-integration, art. 4 et 5, p. 4250"),
    ("bourse", "ENS et polytechnique, 3e année", "année universitaire 2011-2012", 2011, 150, "D/mois", "arrete-2012-10-09-bourses-montants, art. 1, p. 2566-2567"),
    # Plafond de revenu des parents (bourse de premier niveau), D par an
    ("plafond", "bourse", "année universitaire 1990-1991", 1990, 1450, "D/an", "arrete-1990-08-21-seuil-revenus, art. unique, p. 1148"),
    ("plafond", "prêt", "année universitaire 1990-1991", 1990, 4200, "D/an", "arrete-1990-08-21-seuil-revenus, art. unique, p. 1148"),
    ("plafond", "bourse, 1er et 2e cycles", "année universitaire 2005-2006", 2005, 2619, "D/an", "arrete-2006-01-06-seuil, p. 200"),
    ("plafond", "bourse, 1er et 2e cycles", "année universitaire 2006-2007", 2006, 2691, "D/an", "arrete-2006-06-08-seuil, p. 1617"),
    ("plafond", "bourse, 1er et 2e cycles", "année universitaire 2007-2008", 2007, 2775, "D/an", "arrete-2007-06-11-seuil, p. 2069"),
    ("plafond", "bourse, 1er et 2e cycles", "année universitaire 2008-2009", 2008, 2878, "D/an", "arrete-2008-07-07-seuil, p. 2080"),
    ("plafond", "bourse, 1er et 2e cycles", "année universitaire 2009-2010", 2009, 3022, "D/an", "arrete-2009-10-05-seuil, p. 3108"),
    # Le plafond SMIG des régimes de 2009 et de 2012, en dinars : douze fois le SMIG mensuel en
    # vigueur au premier jour de l'année universitaire (série marche-travail-smig-smag), pour les
    # deux régimes horaires, les arrêtés ne disant pas lequel s'applique.
    ("plafond", "SMIG annuel, régime de 48 heures", "1er septembre 2009", 2009, "smig_48h_mensuel@2009-09-01", "D/an", "arrete-2009-10-26-bourses-prets, art. 4, p. 3304-3308 ; SMIG : marche-travail-smig-smag"),
    ("plafond", "SMIG annuel, régime de 40 heures", "1er septembre 2009", 2009, "smig_40h_mensuel@2009-09-01", "D/an", "arrete-2009-10-26-bourses-prets, art. 4, p. 3304-3308 ; SMIG : marche-travail-smig-smag"),
    ("plafond", "SMIG annuel, régime de 48 heures", "année universitaire 2011-2012", 2011, "smig_48h_mensuel@2011-09-01", "D/an", "arrete-2012-10-09-bourses-conditions, art. 4 nouveau, p. 2563-2566 ; SMIG : marche-travail-smig-smag"),
    ("plafond", "SMIG annuel, régime de 40 heures", "année universitaire 2011-2012", 2011, "smig_40h_mensuel@2011-09-01", "D/an", "arrete-2012-10-09-bourses-conditions, art. 4 nouveau, p. 2563-2566 ; SMIG : marche-travail-smig-smag"),
    # Prêt universitaire de l'État en Tunisie, montant annuel à 100 %
    ("pret", "premier niveau", "année universitaire 1988-1989", 1988, 400, "D/an", "arrete-1990-02-28-prets-montants, art. 1 et 3, p. 360"),
    ("pret", "troisième cycle", "année universitaire 1988-1989", 1988, 700, "D/an", "arrete-1990-02-28-prets-montants, art. 1 et 3, p. 360"),
    ("pret", "premier niveau", "année universitaire 1989-1990", 1989, 400, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("pret", "troisième cycle", "année universitaire 1989-1990", 1989, 700, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("pret", "premier niveau", "année universitaire 1991-1992", 1991, 400, "D/an", "arrete-1992-03-17-prets-montants, p. 399"),
    ("pret", "spécialisation", "année universitaire 1991-1992", 1991, 700, "D/an", "arrete-1992-03-17-prets-montants, p. 399"),
    ("pret", "études doctorales", "année universitaire 1991-1992", 1991, 1400, "D/an", "arrete-1992-03-17-prets-montants, p. 399"),
    ("pret", "premier niveau", "année universitaire 1997-1998", 1997, 500, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("pret", "spécialisation", "année universitaire 1997-1998", 1997, 700, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("pret", "études doctorales", "année universitaire 1997-1998", 1997, 1400, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("pret", "révision comptable", "1er octobre 2010", 2010, 700, "D/an", "arrete-2010-11-24-prets-montants, art. 2 et 7, p. 3248"),
    ("pret", "mastère, doctorat", "1er octobre 2010", 2010, 1400, "D/an", "arrete-2010-11-24-prets-montants, art. 2 et 7, p. 3248"),
    ("pret", "enfants des personnels", "1er octobre 2010", 2010, 500, "D/an", "arrete-2010-11-24-prets-montants, art. 3 et 7, p. 3248"),
    ("pret", "premier niveau", "1er octobre 2011", 2011, 600, "D/an", "arrete-2012-10-09-prets-montants, art. 2, p. 2567"),
    ("pret", "second niveau", "1er octobre 2011", 2011, 800, "D/an", "arrete-2012-10-09-prets-montants, art. 2, p. 2567"),
    ("pret", "mastère, 1re année", "1er octobre 2011", 2011, 1000, "D/an", "arrete-2012-10-09-prets-montants, art. 2, p. 2567"),
    ("pret", "mastère, 2e année", "1er octobre 2011", 2011, 1400, "D/an", "arrete-2012-10-09-prets-montants, art. 2, p. 2567"),
    # Prêt universitaire de l'État à l'étranger, montant annuel à 100 %
    ("etranger", "bourse, Angleterre, Allemagne, Belgique, Canada, Italie, Suisse, États-Unis", "1er octobre 1977", 1977, 72.5, "D/mois", "arrete-1978-01-05-bourses-montants, art. 1 et 3, p. 106-107"),
    ("etranger", "bourse, France", "1er octobre 1977", 1977, 70, "D/mois", "arrete-1978-01-05-bourses-montants, art. 1 et 3, p. 106-107"),
    ("etranger", "bourse, pays arabes du Moyen-Orient, Europe de l'Est et autres pays", "1er octobre 1977", 1977, 60, "D/mois", "arrete-1978-01-05-bourses-montants, art. 1 et 3, p. 106-107"),
    ("etranger", "prêt, Europe de l'Ouest", "année universitaire 1988-1989", 1988, 1200, "D/an", "arrete-1990-02-28-prets-montants, art. 1 et 3, p. 360"),
    ("etranger", "prêt, États-Unis, Canada", "année universitaire 1988-1989", 1988, 2200, "D/an", "arrete-1990-02-28-prets-montants, art. 1 et 3, p. 360"),
    ("etranger", "prêt, Europe de l'Est, Maghreb, Machrek, pays africains", "année universitaire 1988-1989", 1988, 600, "D/an", "arrete-1990-02-28-prets-montants, art. 1 et 3, p. 360"),
    ("etranger", "prêt, Europe de l'Ouest", "année universitaire 1989-1990", 1989, 1500, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("etranger", "prêt, États-Unis, Canada", "année universitaire 1989-1990", 1989, 3000, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("etranger", "prêt, Maghreb et Machrek", "année universitaire 1989-1990", 1989, 600, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("etranger", "prêt, Europe de l'Est", "année universitaire 1989-1990", 1989, 600, "D/an", "arrete-1990-04-17-prets-montants, art. 1, p. 542-543"),
    ("etranger", "prêt, Europe de l'Ouest", "année universitaire 1997-1998", 1997, 1500, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("etranger", "prêt, États-Unis, Canada", "année universitaire 1997-1998", 1997, 3000, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("etranger", "prêt, Maghreb et Machrek", "année universitaire 1997-1998", 1997, 600, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("etranger", "prêt, Europe de l'Est et Chine", "année universitaire 1997-1998", 1997, 600, "D/an", "arrete-1997-08-18-prets-montants, p. 1615"),
    ("etranger", "prêt, pays arabes et africains", "1er octobre 2010", 2010, 1200, "D/an", "arrete-2010-11-24-prets-montants, art. 4 et 7, p. 3248"),
    ("etranger", "prêt, Russie, Chine, Turquie, Asie centrale", "1er octobre 2010", 2010, 1200, "D/an", "arrete-2010-11-24-prets-montants, art. 4 et 7, p. 3248"),
    ("etranger", "prêt, Union européenne et Suisse", "1er octobre 2010", 2010, 2500, "D/an", "arrete-2010-11-24-prets-montants, art. 4 et 7, p. 3248"),
    ("etranger", "prêt, États-Unis et Canada", "1er octobre 2010", 2010, 4500, "D/an", "arrete-2010-11-24-prets-montants, art. 4 et 7, p. 3248"),
    ("etranger", "prêt, Union du Maghreb arabe", "année universitaire 2018-2019", 2018, 3000, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "prêt, Japon, Chine, Corée du Sud, Inde", "année universitaire 2018-2019", 2018, 4000, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "prêt, autres pays asiatiques, Russie, Turquie", "année universitaire 2018-2019", 2018, 3000, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "prêt, Canada, États-Unis, France, Allemagne", "année universitaire 2018-2019", 2018, 6000, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "prêt, autres pays européens", "année universitaire 2018-2019", 2018, 5000, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "prêt, reste du monde", "année universitaire 2018-2019", 2018, 2500, "D/an", "arrete-2019-02-18-prets-etranger, art. 1 et 2, p. 448"),
    ("etranger", "bourse en RFA", "1990", 1990, 230, "D/mois", "arrêté du 23 août 1990, JORT n° 55 de 1990 (sans clé)"),
    ("etranger", "bourse des enfants des familles résidentes à l'étranger, études en Tunisie", "novembre 1997", 1997, 100, "D/mois", "arrete-1997-11-04-bourse-tre, art. 1, p. 2037-2038"),
    # Œuvres universitaires
    ("oeuvres", "bourse au boursier non hébergé", "année universitaire 1992-1993", 1992, 20, "D/mois", "arrete-1992-08-20-bourse-supplementaire, art. 2, p. 1135-1136"),
    ("oeuvres", "bourse d'hébergement", "2 février 2016", 2016, 30, "D/mois", "arrete-2016-01-18-hebergement, art. 6, p. 266-268"),
    ("oeuvres", "contribution au lit", "2 février 2016", 2016, 10, "D/mois", "arrete-2016-01-18-hebergement, art. 9, p. 266-268"),
    ("oeuvres", "contribution au repas", "2 février 2016", 2016, 0.2, "D/repas", "arrete-2016-01-18-restauration, art. 4, p. 268-269"),
    # Crédits des bourses en Tunisie, ministère de l'Enseignement supérieur (prévisions, MD)
    ("credits", "bourses en Tunisie, prévision 2013", "2013", 2013, 97.8, "MD", "budget-mesrs-2013-gbo, p. 57"),
    ("credits", "bourses en Tunisie, prévision 2014", "2014", 2014, 103.6, "MD", "budget-mesrs-2014-gbo, page du fichier 92"),
    ("credits", "bourses en Tunisie, prévision 2015", "2015", 2015, 100.0, "MD", "budget-mesrs-2015, page du fichier 102"),
    ("credits", "bourses en Tunisie, prévision 2016", "2016", 2016, 110.0, "MD", "budget-mesrs-2016, page du fichier 100"),
    ("credits", "bourses en Tunisie, prévision 2017", "2017", 2017, 130.0, "MD", "budget-mesrs-2017, p. 91"),
    ("credits", "bourses en Tunisie, colonne « ق . م 2012 »", "2012", 2012, 86.0, "MD", "budget-mesrs-2013-gbo, p. 57"),
    ("credits", "bourses en Tunisie, colonne « ق . م 2013 »", "2013", 2013, 97.8, "MD", "budget-mesrs-2014-gbo, page du fichier 92"),
    ("credits", "bourses en Tunisie, colonne « ق . م 2014 »", "2014", 2014, 103.6, "MD", "budget-mesrs-2015, page du fichier 102"),
    ("credits", "bourses en Tunisie, colonne « ق . م 2015 »", "2015", 2015, 110.0, "MD", "budget-mesrs-2016, page du fichier 100"),
    ("credits", "bourses en Tunisie, colonne « ق . م 2016 »", "2016", 2016, 110.0, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Nord, colonne « ق . م 2016 »", "2016", 2016, 2.660, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Nord, prévision 2017", "2017", 2017, 3.122, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Centre, colonne « ق . م 2016 »", "2016", 2016, 4.600, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Centre, prévision 2017", "2017", 2017, 3.882, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Sud, colonne « ق . م 2016 »", "2016", 2016, 3.740, "MD", "budget-mesrs-2017, p. 91"),
    ("offices", "subvention de gestion, office du Sud, prévision 2017", "2017", 2017, 3.977, "MD", "budget-mesrs-2017, p. 91"),
]


def table() -> pd.DataFrame:
    ipc = dinars_constants.ipc()
    smig = figtools.series("marche-travail-smig-smag").sort_values("date")
    lignes = []
    for tableau, grandeur, date, annee, montant, unite, texte in LIGNES:
        if isinstance(montant, str):  # « colonne@date » : 12 × SMIG mensuel en vigueur à la date
            colonne, jour = montant.split("@")
            montant = round(12 * float(smig[smig.date <= jour].iloc[-1][colonne]), 3)
        assert annee >= 1976, (grandeur, annee)
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append({
            "tableau": tableau, "grandeur": grandeur, "date_effet": date,
            "annee_indice": annee, "montant_courant": montant, "unite": unite,
            "ipc_annee": ipc[annee], "ipc_2023": ipc[ANNEE_BASE],
            "montant_dinars_2023": round(montant * coef, 3), "texte": texte,
        })
    return pd.DataFrame(lignes)


def main() -> None:
    figtools.register_provenance(
        "marche-travail-smig-smag",
        titre="Salaire minimum interprofessionnel garanti, à chaque date d'effet",
        sources=[],
        caveats=("Montants du SMIG exposés au livre « Le marché du travail », tableau du SMIG "
                 "(precis/fr/marche_travail/_salaire_minimum.qmd, @tbl-mt-smig), avec leurs décrets."),
    )
    figtools.register_provenance(
        SERIE_LOCALE,
        titre="Aides aux élèves et aux étudiants : montants fixés par les textes et crédits prévus",
        sources=[],
        caveats=("Montants relevés dans les textes et documents budgétaires cités ligne par ligne "
                 "(colonne texte : clé de citation, article ou page). Montant en dinars de 2023 = "
                 "montant courant × IPC 2023 / IPC de l'année d'effet ; pour une année scolaire ou "
                 "universitaire, l'année où elle commence. Aucun montant antérieur à 1976 n'est converti."),
    )
    d = table()
    figtools.write_figdata(d, ICI.parent / "figdata" / "fig_educ_aides_dinars_constants.csv",
                           SERIE_LOCALE, *dinars_constants.SERIES_IPC,
                           "marche-travail-smig-smag")
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(d[["tableau", "grandeur", "date_effet", "montant_courant", "montant_dinars_2023"]])


if __name__ == "__main__":
    main()

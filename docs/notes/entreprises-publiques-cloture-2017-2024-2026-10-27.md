# Entreprises publiques : les années récentes, premier passage (27 octobre 2026)

Consigne du 27 octobre 2026 : l'ossature du volume est la longue période, flux par flux ; on remplit
d'abord les années récentes et l'on remonte ensuite vers le passé. Deux séries sont étendues ou créées
dans `tunisia-data`, lues par le volume X depuis son snapshot.

## 1. Clôture du budget, gestions 2017 à 2024 (Cour des comptes)

- Série `cdc-cloture-entreprises-publiques` prolongée de 2016 à 2024 (branche `donnees/cdc-cloture-2017-2024`,
  commit `b2d82e2`), sept rapports de clôture (gestions 2018 à 2024), la gestion 2017 par la colonne de
  comparaison du rapport 2018 (le rapport de 2017 est au catalogue de la Cour sans fichier). Fiche :
  `sources/cdc-cloture-entreprises-publiques.md` de tunisia-data.
- Rupture de nomenclature en 2020 : plus de total « transferts des entreprises publiques et profits du
  Trésor » ; sous-totaux imprimés (dividendes ; excédents et Banque centrale) et lignes de profits du Trésor.
  Le précis trace la somme des lignes imprimées, dite telle quelle (parenthèses dans le tableau, trait sur la
  figure). Pour 2019, les trois lignes de profits du Trésor de l'annexe du rapport 2020 somment les « autres
  profits du Trésor » du rapport 2019 : c'est le recoupement qui autorise la lecture continue.
- Remboursements de prêts : plus de total depuis 2020 ; prêts rétrocédés classés parmi les ressources
  d'emprunt ; prêts du titre II sous un libellé sans « entreprises publiques ».
- Recettes de privatisation : aucune ligne dans les tableaux de recettes de 2017 à 2024 ; la série porte une
  ligne vide par gestion, le précis une bande grise, jamais un zéro.
- Grandeur nouvelle : encours de la dette garantie en fin de gestion, imprimé depuis le rapport 2018 d'après
  le ministère des Finances (2018, 2019, 2021-2023 ; rien pour 2020 et 2024). Identique à l'encours du
  rapport sur la dette publique, sauf fin 2018 (16 471 MD dans le rapport 2018, 16 713,4 dans le suivant).
- Divergence gardée : dividendes 2023, libellés pétrolier et non pétrolier inversés entre les rapports 2023
  et 2024 ; sous-total identique.

## 2. Plafonds légaux de la garantie et des prêts du Trésor, lois de finances 2016 à 2026

- Série `jort-lf-plafond-garanties` prolongée de 2015 à 2026 et série nouvelle `jort-lf-plafond-prets-tresor`
  (2016-2026), branche `donnees/lf-plafond-garanties-2016-2026`, commits `b81dca7` et `ba8e6d8`. Articles lus à
  l'image : lois de finances pour 2016 à 2026 et lois rectificatives ou complémentaires 2016-2023.
- Garantie : 3 000 MD (2016-2018) ; 4 500 MD puis 4 790 (2019, loi n° 2019-77) ; 5 000 puis 7 000 (2020, loi
  n° 2020-45) ; 7 000 (2021-2022) ; 7 000 puis 8 000 (2023, loi n° 2023-12) ; 8 000 (2024-2025) ; 7 000
  (2026). La série légale rejoint les annexes du ministère sauf pour la loi initiale de 2023.
- Prêts du Trésor : 100 MD (2016-2018, relevés à 125 par les lois complémentaires de 2016 et 2017) ; 125
  (2019-2021, 550 en 2020 par la rectificative, 175 en 2021) ; 500 (2022) ; 325 puis 200 (2023) ; 200
  (2024) ; 330 (2025) ; 200 (2026). Série incomplète : états antérieurs à 2016 non versés.
- Pages : édition française quand le fascicule ou l'extrait au pied de page du Journal officiel existe ;
  édition arabe pour la loi de finances pour 2023 et celle pour 2026, dit dans le registre. Les éditions
  françaises des JORT n° 104 de 2015, 104 de 2018, 104 de 2019, 141 de 2022, 144 de 2023 et 149 de 2024
  sont absentes du corpus et répondent 404 sur pist.tn.
- La note de lecture de chaque ligne est dans une colonne `lecture` de la transcription, non rendue ; la
  colonne `remarque` rendue ne porte que l'éditorial.

## 3. Ce que le volume change

- Section `#sec-ep-garanties-plafond-legal` : titre 1958-2026, plafond des prêts du Trésor, registre
  `tbl-ep-plafond-registre` recopié jusqu'en 2026 (test d'identité), registre neuf `tbl-ep-prets-tresor-registre`,
  figure `fig-ep-plafond-legal` prolongée.
- Section `#sec-ep-lp-cloture` : gestions 2010 à 2024, figure et tableaux à quinze gestions.
- Figure `fig-ep-encours` : encours de la Cour en losanges ; figure `fig-ep-cessions` : 1987-2009 (Direction
  générale de la privatisation) et 2010-2024 (budget), sans chaînage.
- Présentation : tableau de voisinage à la place de « Ce que d'autres volumes traitent ».
- Sept notices `cdc-cloture-2018` à `cdc-cloture-2024` dans `entreprises_publiques/references.json`.

## 4. Prochaines marches vers le passé

1. Rapports annuels de la Banque centrale (1959-1986 et 2015-2025 déjà rangés dans tunisia-data) : transferts
   aux entreprises publiques et revenus de participations avant 2016.
2. Rapports de clôture des gestions 2005 à 2009 (catalogue de la Cour : 2005, 2006, 2007, 2009 téléchargés).
3. Fonds de restructuration du capital des entreprises publiques (loi de finances pour 1986, art. 13 de celle
   pour 2003) : recettes et dépenses dans les tableaux des fonds spéciaux des rapports de clôture.
4. Recapitalisation des banques publiques (lois de finances pour 2014 et 2015, art. 14 à 16).

# Plan : les boissons alcoolisées dans le chapitre « Les droits de consommation »

Fiche de l'architecte, 23 octobre 2026. Matière : `docs/notes/fiscalite-decrets-97-1368-2015-1768.md`,
complétée par la lecture des lois de finances pour 2016 (art. 44, 92), 2018 (art. 45, 67) et
2021 (art. 20, 42). Chapitre : `precis/fr/fiscalite/_droits_consommation.qmd`.

## Constat qui commande le plan

L'annexe du décret gouvernemental n° 2015-1768 n'est plus le tarif des positions 22-03 à
22-08 : le tableau de la loi n° 88-62 porte ces lignes depuis le 1er janvier 2016 (LF 2016,
mêmes valeurs que l'annexe de 2015), puis les vermouths et les spiritueux à 100 % (LF 2018),
puis la bière à 0,024 D/cl et les vins à 2,4 D/l (LF 2021). Le tableau consolidé de 2023 du
chapitre (`tbl-dc-en-vigueur`) porte ces valeurs. Un « état du droit » qui s'arrêterait
à 2015 serait faux.

## Place et forme

Une section de deuxième niveau, `## Les boissons alcoolisées : un régime fiscal fixé par décret`,
placée après « Qui peut modifier le tableau » et avant « L'articulation avec la taxe sur la valeur
ajoutée ». Le paragraphe de « Qui peut modifier le tableau » garde l'habilitation de l'article 86
et renvoie à cette section en tête.

## Ruptures (deux) et une reprise par la loi

1. **4 août 1997 : un code complet par décret.** Le décret n° 97-1368 réunit droit de
   consommation, TVA propre, capsule fiscale sur les vins, obligations des producteurs et
   circulation, et abroge le décret n° 93-2090. Tarif par récipient pour la bière et les vins.
2. **24 novembre 2015 : un tarif au volume, une annexe unique.** Bière au centilitre, vin en
   bouteille au litre, spiritueux à un taux uniforme ; fin de la distinction classés / non classés
   pour les spiritueux.
3. **1er janvier 2016 : la loi reprend le tarif (étape).** Le tableau de la loi, refondu en entier,
   porte les lignes 22-03 à 22-08 aux valeurs de l'annexe de 2015 ; les révisions de 2018 et de 2021
   passent par la loi de finances. La capsule reste fixée par décret. Le tableau de 1988 portait déjà
   des lignes de boissons : il n'y a pas là de rupture.

## Étapes et ajustements (dans le tableau daté et le bloc replié)

2002 (TVA 18 %, affectations), 2007 (capsule doublée, part affectée 75 %), 2013 (annexes
refondues, taux de TVA de 29 % supprimé du décret), 2018 (vermouths et spiritueux de 50 à 100 %),
2021 (bière, vins), 2022 (capsule doublée).

## Ordre de la section

1. Phrase d'objet et état à une date (depuis le 1er janvier 2021).
2. Trois points : 1997, 2015 et 2016, capsule.
3. Vue d'ensemble : tableau daté des tarifs (`alcools-tarifs`), tableau de la capsule
   (`capsule-fiscale`), tous deux issus de `tarifs/tarifs-releves-droits-consommation.csv`.
4. Bloc replié « textes du régime, 1993-2022 » : colonne « Portée », avant → après.
5. Bloc replié « obligations, circulation et contrôle » : par article, sans montants isolés.

## Frontière cœur / secondaire

Cœur : le tarif et ses changements de nature. Secondaire : capsule, entrepôt, circulation,
contrôle ; ils vont dans le bloc replié, sans section propre.

## Ce qui reste hors du texte (TODO)

- Textes de loi de finances postérieurs à 2021 et antérieurs à 2023 non dépouillés un à un ;
  vérification des lois de finances 2022 à 2026 sur le tableau consolidé le plus récent.
- Rapport entre l'annexe de 2015 et le tableau de la loi : les textes lus ne règlent pas le sort
  de l'annexe.
- Habilitation de l'article 86 (positions 22-03 et 22-05 à 22-09) : 22-04 n'y figure pas, alors que le
  décret de 1997 y fixe des tarifs ; piste : nomenclature antérieure au tarif harmonisé (22-04 =
  moûts de raisin), à vérifier.
- Date d'application de la capsule de 1997 (avis aux embouteilleurs, article 44).
- Contexte de 1997 : le décret n'a pas d'exposé des motifs.
- Lignes du décret n° 93-2090 lues par OCR : libellés à contrôler à l'image.

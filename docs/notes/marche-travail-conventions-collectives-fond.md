# Les conventions collectives sectorielles du secteur privé — passe documentaire de fond

> Note du documentaliste, 8 octobre 2026. Elle prolonge `docs/notes/marche-travail-conventions-collectives.md`
> (5 octobre 2026) sans la refaire, et ne rédige pas le chapitre. Priorité retenue : l'économique —
> niveaux de salaire, évolution, rapport au SMIG — avant le juridique.
>
> **Niveaux de preuve employés dans les tableaux** — « image » : chiffre lu sur la page rendue en
> image ; « texte » : chiffre tiré de la couche texte du PDF (éditions arabes de 2011 à 2014, dont
> les chiffres sortent en clair alors que les lettres sont mal encodées), titre et date de la grille
> contrôlés à l'image ; « texte FR » : couche texte de l'édition française ; « notice » : métadonnée
> de `jort_cache.db` seule. Aucune valeur de cette note ne vient d'un fichier de seconde main.
>
> Outils de cette passe (scratchpad, non versionnés) : `scratchpad/cc/inv.py` (inventaire),
> `branches.py` (rattachement par branche), `scan2.py` (plein texte français), `nums.py`
> (repérage des pages de grille par leurs chiffres), `crop.sh` (rendu et recadrage des pages).

## 0. Trois constats qui commandent tout le reste

1. **Depuis le 24 juillet 1996, l'édition française du *Journal officiel* ne publie plus le texte
   des avenants ni leurs grilles.** JORT n° 60 du 26 juillet 1996, p. 1606 (texte FR) : « Arrêtés
   du ministre des affaires sociales du 24 juillet 1996, portant agréments d'avenants à quarante
   conventions collectives nationales. (Les arrêtés et avenants sont publiés dans l'édition
   originale arabe). » Même mention au n° 48 du 15 juin 1999, p. 947 (« vingt conventions »).
   De 2002 à 2012 l'édition française ne porte qu'un avis collectif par fascicule (« avenants à
   certaines conventions collectives ») ; à partir de 2013 elle publie de nouveau un arrêté par
   branche, avec la liste complète des avenants antérieurs dans ses visas, mais renvoie les
   grilles à l'arabe — JORT n° 49 du 16 avril 2024, p. 1257 (texte FR), note (1) : « L'avenant à
   la présente convention est publié uniquement en langue arabe. »
   Nuance vérifiée : la bascule n'est pas nette en 1996 — le n° 86 du 25 octobre 1996 publie
   encore en français, texte et grilles, les avenants n° 5 du bâtiment, de la boulangerie et du
   pétrole (pp. 2141-2160, texte FR et image).
   Conséquence : **de 1974 à 1994 (et pour quelques branches jusqu'en octobre 1996) les grilles se lisent en français** (fascicules scannés, sans
   couche texte avant 1994) ; **depuis 1996 elles ne se lisent que dans l'édition arabe**, où les
   tableaux sont des images (2016 →), du texte mal encodé mais aux chiffres lisibles (2011-2014),
   ou des pages entièrement en image (1996-2009 : constat fait sur le seul n° 97 de 2002 ; les n° 60/1996 et 48/1999 arabes sont des scans, couche texte vide).
2. **Le texte des conventions d'origine est indexé à part** dans `jort_cache.db`, sous le type
   « Convention » (et non « Arrêté ») : l'arrêté d'agrément paraît d'abord, seul, sur une page ; le
   texte de la convention, avec ses grilles, paraît quelques semaines plus tard. Textile : arrêté
   au n° 55 du 30 août 1974, p. 1936 ; texte au n° 76 du 10 décembre 1974, pp. 2715-2733.
   Bâtiment : arrêté au n° 18 du 14 mars 1975, p. 504 ; texte au n° 20 du 25 mars 1975,
   pp. 557-571. La note du 5 octobre ne comptait que les arrêtés.
3. **Les grilles changent de périmètre en 1994.** De 1981-1982 à avril 1994, elles n'incluent pas
   l'indemnité complémentaire provisoire des décrets n° 81-437 du 7 avril 1981 et n° 82-501 du
   16 mars 1982 (nota bene de chaque grille de 1990, image) ; l'avenant n° 5 du textile (12 août
   1994) l'« intègre à compter du 1er mai 1994 dans les salaires de base » (JORT n° 78 du
   4 octobre 1994, p. 1637, texte FR). Toute série longue porte donc une rupture au 1er mai 1994,
   et les grilles de 1983 à 1993 ne se comparent pas directement au SMIG (§ B.4).

## Corrections à la note du 5 octobre 2026

- « Au moins 64 » agréments : le chiffre est exact pour la requête d'alors ; il se précise en
  66 notices, 61 agréments de conventions sectorielles, 56 branches agréées (§ A.2).
- Les pics annuels (45, 53, 44) comptaient toutes les notices ; avenants seuls : 43, 51, 40 (§ A.5).
- Banques : l'agrément du 24 décembre 1975 (n° 87/1975, p. 2898) est **confirmé** par sa notice.
- « Avenant » = الملحق التعديلي et « agrément » = المصادقة sont désormais lus au journal.
- La lacune « aucune source chiffrée de couverture » est levée pour l'OIT (§ C).
- `data/conventions_collectives/` ne contient ni le textile ni le bâtiment : rien n'en est repris.

## A. L'inventaire

### A.1 Requêtes (rejouables) et couverture

Base : `jort_cache.db`, dernière publication indexée le 2 octobre 2026.

```sql
-- R1 : toutes les notices du champ (titres français ET titres arabes seuls) → 611 lignes
select * from textes where jort_annee between 1956 and 2026 and (
  lower(titre) like '%convention collective%' or lower(titre) like '%conventions collectives%'
  or titre like '%مشتركة القطاعية%' or titre like '%تفاقية المشتركة%' or titre like '%تفاقية مشتركة%'
  or titre like '%تفاقيات المشتركة%' or titre like '%الاتفاقية الاطارية%'
  or titre like '%الإتفاقية الإطارية%' or titre like '%الاتفاقية الإطارية%');
-- R2 : textes des conventions publiés à part
select * from textes where type like 'Conv%' and titre like '%collective%';
```

Classement de R1 (script `inv.py`) : **512 notices d'avenant** (353 à titre français, 159 à titre
arabe seul — motif `avenant` ou `ملحق`) ; **65 notices d'agrément ou d'approbation de convention**
(63 françaises, 2 arabes), **plus une que R1 manque** — l'agrément du 24 décembre 1975 de la
« convention nationale des banques et des établissements financiers » (n° 87/1975, p. 2898),
dont le titre ne porte pas le mot « collective » ; contrôle `lower(titre) like '%convention
nationale%'` sans « collective », arrêtés seuls : deux lignes, celle-ci et un rectificatif
d'avenant (presse, 1994). Soit **66** ; 34 autres (commission consultative, décrets de majoration des secteurs
non couverts, extensions de champ, rectificatifs). Seconde voie : `textes_fts match '"convention
collective"'` rend 537 lignes, soit moins que R1 (les titres arabes lui échappent). Requête de
contrôle `match '(agrement OR approbation) AND convention AND (collective OR sectorielle)'`,
titres sans « convention collective » ni « avenant » : dix lignes, toutes des « conventions
sectorielles » de l'assurance maladie avec les professions de santé (2007, 2016, 2020, 2021),
hors champ. Aucun agrément de convention collective n'échappe donc à R1 parmi les titres indexés.

Plein texte (seconde source, script `scan2.py`) : cache `~/.cache/precis-recherches` des fascicules
français, 1994-2026 (les fascicules de 1981 à 1993 n'ont pas de couche texte ; ceux de 1999 à 2005
ont la couche à police décalée, décodée avant recherche). Motif : « Arrêté du ministre des affaires
sociales du …, portant agrément | approbation de l'avenant n° N à la convention collective … »,
lignes recollées, arrêtés datés de l'année du fascicule ou de la précédente (pour écarter les visas).

### A.2 Le total, et pourquoi c'est une borne basse

- **66 notices d'agrément.** La requête du 5 octobre, rejouée, rend bien 64 lignes : les 63 à
  titre français de R1 et l'agrément des banques de 1975 (que R1 manque, ci-dessus) ; elle
  ignorait les deux notices à titre arabe, qui ne sont ni l'une ni l'autre une convention
  sectorielle. Sur ces 66 : la convention cadre de 1973 ; la convention cadre du
  secteur agricole (arrêté du 17 novembre 2015, n° 94/2015, notice à titre arabe, intitulé français
  lu au plein texte : « convention cadre dans le secteur de l'agriculture ») ; un décret présidentiel de 2017 sans
  rapport (convention cadre de financement, faux positif) ; un rectificatif (plastique, n° 13 du
  22 février 1977) ; un arrêté modificatif (hôtellerie, 6 octobre 1976). Restent **61 agréments de
  conventions sectorielles**, qui se ramènent à **57 lignes de branche** dans le tableau A.3 :
  **56 branches ayant au moins un agrément**, et **une sans notice d'agrément** (jardins
  d'enfants et crèches, connue par ses seuls avenants). Quatre branches ont plusieurs agréments
  successifs (salines 1971 et 1976 ; ports et docks 1975 et 1993 ; assurances 1975 et 1983 ;
  banques 1975, 1983 et 2014).
- En raisonnant par **branche vivante** : la convention de 1969 des hôtels-restaurants-cafés est
  relayée par celles de l'industrie hôtelière (1975) et des cafés-bars-restaurants (1977) ; celle de
  la mécanique générale et de l'électricité (1974) par l'électricité-électronique (1999) et la
  mécanique générale-stations de vente de carburant (2000). On obtient **54 à 55 conventions
  sectorielles distinctes en vigueur**, ce que recoupe un document extérieur : « 56 collective
  agreements […], 54 sectorial agreements and 2 global/framework agreements » (Belgacem et Vacher,
  2023, annexe ; rapport extérieur, cité pour le seul recoupement).
- **Borne basse**, pour trois raisons mesurées :
  1. une convention au moins n'a pas de notice d'agrément (jardins d'enfants et crèches : avenant
     n° 3 agréé le 14 octobre 2011, n° 81/2011) ; et un titre qui s'écarte de la formule usuelle
     échappe à la requête (banques, 1975 : « convention nationale ») ;
  2. les **avenants de 1996 à 2012 ne sont pas indexés un par un** : l'édition française ne publie
     qu'un avis collectif. Mesure sur le textile : les visas de l'avenant n° 18 énumèrent dix-sept
     étapes (sentence arbitrale de 1983, avenants n° 2 à 17) ; `jort_cache` n'en connaît que onze
     — manquent les n° 6 (1996), 7 (1999), 8 (2002), 9 (2006), 10 (2009) et 17 (2022) ;
  3. des fascicules entiers sont inconnus de la base ou absents du corpus (n° 132 de 2022 : voir
     § D).

### A.3 Tableau par branche

Colonnes tirées des notices (dates au format de la base ; **la date de notice n'est pas le pied de
page du fascicule**, à contrôler avant citation). « Notices d'avenant » : nombre de notices de
`jort_cache` rattachées à la branche par mots-clés ; « n° repérés » : numéros d'avenant distincts
vus dans les notices ou au plein texte français. État de lecture : voir A.4.

| Branche | Arrêté(s) d'agrément (date ; JORT n°, date de notice, p.) | Texte de la convention (JORT, p.) | Notices d'avenant | N° d'avenant repérés (max) | Dernier arrêté d'avenant repéré |
|---|---|---|---:|---|---|
| Hôtels, restaurants, cafés, débits de boissons (1969) | 1969-07-02 (n° 25/1969, 1969-07-01, pp. 817-825) | — | 0 | — | — |
| Salines de Tunisie | 1971-06-23 (n° 28/1971, 1971-06-29, p. 829) ; 1976-09-29 (n° 59/1976, 1976-10-05, pp. 2343-2357) | — | 8 | max 16 ; 8 numéros distincts | 2018-12-03 ; plein texte FR : 2022 |
| Construction métallique | 1974-08-29 (n° 55/1974, 1974-08-30, p. 1936) | n° 72/1974, 1974-11-26, pp. 2582-2595 | 10 | max 16 ; 10 numéros distincts | 2018-12-03 ; plein texte FR : 2022 |
| Textile | 1974-08-29 (n° 55/1974, 1974-08-30, p. 1936) | n° 76/1974, 1974-12-10, pp. 2715-2733 | 11 | max 18 ; 12 numéros distincts | 2024-04-08 |
| Mécanique générale et électricité (1974) | 1974-08-29 (n° 55/1974, 1974-08-30, p. 1937) | n° 2/1975, 1975-01-10, pp. 61-77 | 5 | max 4 ; 3 numéros distincts | 1993-11-16 |
| Imprimerie, reliure, transformation du carton et du papier | 1974-08-29 (n° 55/1974, 1974-08-30, p. 1937) | n° 69/1974, 1974-11-15, pp. 2462-2468 | 11 | max 16 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Pâtes alimentaires et couscous | 1975-03-12 (n° 18/1975, 1975-03-14, p. 503) | n° 24/1975, 1975-04-08, pp. 683-689 | 10 | max 16 ; 10 numéros distincts | 2019-07-24 ; plein texte FR : 2022 |
| Boissons gazeuses non alcoolisées | 1975-03-12 (n° 18/1975, 1975-03-14, p. 503) | n° 29/1975, 1975-04-29, pp. 861-870 | 10 | max 16 ; 10 numéros distincts | 2019-02-18 ; plein texte FR : 2022 |
| Torréfaction | 1975-03-12 (n° 18/1975, 1975-03-14, p. 503) | n° 25/1975, 1975-04-15, pp. 727-735 | 8 | max 15 ; 9 numéros distincts | 2017-08-14 ; plein texte FR : 2022 |
| Bâtiment et travaux publics | 1975-03-12 (n° 18/1975, 1975-03-14, p. 504) | n° 20/1975, 1975-03-25, pp. 557-571 | 12 | max 16 ; 11 numéros distincts | 2022-11-25 |
| Pétrole (commerce et distribution) | 1975-03-12 (n° 18/1975, 1975-03-14, p. 504) | n° 21/1975, 1975-03-28, pp. 586-595 | 13 | max 15 ; 14 numéros distincts | 2023-04-10 |
| Cuirs et peaux | 1975-03-29 (n° 24/1975, 1975-04-08, p. 683) | n° 33/1975, 1975-05-16, pp. 1028-1039 | 9 | max 16 ; 10 numéros distincts | 2019-01-11 ; plein texte FR : 2022 |
| Ports et docks | 1975-06-19 (n° 43/1975, 1975-06-24, p. 1355) ; 1993-11-16 (n° 90/1993, 1993-11-26, pp. 1991-1998) | n° 57/1975, 1975-08-26, pp. 1821-1827 | 8 | max 6 ; 3 numéros distincts | 1999-09-15 |
| Industries des matériaux de construction | 1975-06-19 (n° 43/1975, 1975-06-24, pp. 1355-1356) | n° 58/1975, 1975-09-02, pp. 1853-1862 | 10 | max 16 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Industrie laitière | 1975-06-19 (n° 43/1975, 1975-06-24, p. 1356) | n° 55/1975, 1975-08-15, pp. 1723-1734 | 11 | max 16 ; 10 numéros distincts | 2019-05-28 ; plein texte FR : 2022 |
| Industries et commerce des boissons alcoolisées | 1975-06-19 (n° 43/1975, 1975-06-24, p. 1356) | n° 66/1975, 1975-10-07, pp. 2146-2156 | 12 | max 16 ; 10 numéros distincts | 2018-12-17 ; plein texte FR : 2022 |
| Bonneterie et confection | 1975-06-19 (n° 43/1975, 1975-06-24, p. 1356) | n° 51/1975, 1975-07-22, pp. 1553-1565 | 11 | max 18 ; 12 numéros distincts | 2024-04-08 |
| Confiserie, biscuiterie, chocolaterie, pâtisserie | 1975-06-19 (n° 43/1975, 1975-06-24, pp. 1356-1357) | n° 47/1975, 1975-07-08, pp. 1454-1464 | 10 | max 16 ; 10 numéros distincts | 2018-12-17 ; plein texte FR : 2022 |
| Chaussure et articles chaussants | 1975-07-17 (n° 50/1975, 1975-07-18, pp. 1537-1538) | n° 62/1975, 1975-09-19, pp. 1995-2015 | 9 | max 16 ; 10 numéros distincts | 2019-01-11 ; plein texte FR : 2022 |
| Industrie hôtelière / hôtels classés touristiques | 1975-07-17 (n° 50/1975, 1975-07-18, p. 1538) ; 1976-10-06 (n° 61/1976, 1976-10-15, p. 2427) | n° 56/1975, 1975-08-22, pp. 1762-1787 | 11 | max 18 ; 11 numéros distincts | 2024-09-17 |
| Conserves et semi-conserves alimentaires | 1975-07-17 (n° 50/1975, 1975-07-18, p. 1538) | n° 59/1975, 1975-09-05, pp. 1894-1904 | 10 | max 15 ; 9 numéros distincts | 2019-07-24 |
| Savonneries, raffineries, huile de grignons | 1975-08-04 (n° 55/1975, 1975-08-15, p. 1723) | n° 58/1975, 1975-09-02, pp. 1863-1869 | 11 | max 16 ; 10 numéros distincts | 2023-04-11 |
| Fabrication de peinture | 1975-11-20 (n° 78/1975, 1975-11-25, p. 2523) | n° 84/1975, 1975-12-19, pp. 2747-2757 | 10 | max 16 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Minoterie | 1975-11-20 (n° 78/1975, 1975-11-25, p. 2523) | — | 10 | max 16 ; 10 numéros distincts | 2019-07-24 ; plein texte FR : 2022 |
| Explosifs | 1975-11-20 (n° 78/1975, 1975-11-25, p. 2523) | n° 86/1975, 1975-12-26, pp. 2820-2830 | 9 | max 16 ; 8 numéros distincts | 2025-03-14 |
| Entreprises de presse | 1975-11-20 (n° 78/1975, 1975-11-25, p. 2524) | — | 11 | max 16 ; 10 numéros distincts | 2022-11-30 |
| Fonderie, métallurgie, construction mécanique | 1975-12-11 (n° 83/1975, 1975-12-16, p. 2699) | n° 5/1976, 1976-01-20, pp. 190-203 | 10 | max 16 ; 10 numéros distincts | 2019-01-21 ; plein texte FR : 2022 |
| Assurances | 1975-12-24 (n° 87/1975, 1975-12-30, pp. 2898-2899) ; 1983-08-23 (n° 74/1983, 1983-11-15, pp. 2935-2947) | n° 7/1976, 1976-01-30, pp. 270-279 | 9 | max 15 ; 9 numéros distincts | 2023-12-12 |
| Commerce des matériaux de construction, bois, produits sidérurgiques | 1975-12-24 (n° 87/1975, 1975-12-30, p. 2899) | n° 4/1976, 1976-01-16, pp. 135-146 | 10 | max 15 ; 9 numéros distincts | 2019-01-11 |
| Banques et établissements financiers | 1975-12-24 (n° 87/1975, 1975-12-30, p. 2898 — ajouté à la main, titre « convention nationale ») ; 1983-08-23 (n° 71/1983, 1983-11-04, pp. 2827-2845) ; 2014-02-17 (n° 23/2014, 2014-03-21, p. 718) | n° 6/1976, 1976-01-27, pp. 226-237 | 9 | max 5 ; 5 numéros distincts | 2022-11-17 |
| Boulangerie | 1976-07-12 (n° 47/1976, 1976-07-16, pp. 1739-1748) | — | 11 | max 16 ; 11 numéros distincts | 2017-07-03 ; plein texte FR : 2022 |
| Commerce de gros, demi-gros et détail | 1976-07-23 (n° 49/1976, 1976-07-30, pp. 1859-1872) | — | 11 | max 16 ; 10 numéros distincts | 2023-03-03 |
| Pharmacies d'officine | 1976-09-29 (n° 60/1976, 1976-10-08, pp. 2386-2393) | — | 12 | max 17 ; 11 numéros distincts | 2025-04-16 |
| Transformation du plastique | 1976-11-11 (n° 80/1976, 1976-12-21, pp. 3070-3082) ; rectificatif n° 13/1977, 1977-02-22, p. 474 | — | 10 | max 16 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Teintureries et blanchisseries | 1976-11-11 (n° 81/1976, 1976-12-24, pp. 3104-3115) | — | 10 | max 16 ; 9 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Produits d'entretien et insecticides | 1977-06-06 (n° 40/1977, 1977-06-10, pp. 1509-1522) | — | 10 | max 16 ; 10 numéros distincts | 2018-12-17 ; plein texte FR : 2022 |
| Produits de toilette et parfumerie | 1977-06-15 (n° 43/1977, 1977-06-21, pp. 1657-1670) | — | 11 | max 16 ; 9 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Cafés, bars, restaurants | 1977-07-27 (n° 59/1977, 1977-09-09, pp. 2378-2379) | n° 63/1977, 1977-09-30, pp. 2547-2567 | 7 | max 9 ; 6 numéros distincts | 2009-11-09 |
| Bois, meuble et liège | 1977-09-07 (n° 59/1977, 1977-09-09, p. 2379) | — | 10 | max 16 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Salles de projection cinématographique | 1977-07-27 (n° 59/1977, 1977-09-09, p. 2379) | — | 6 | max 7 ; 5 numéros distincts | 2003-04-01 |
| Constructeurs et concessionnaires de véhicules automobiles | 1983-12-21 (n° 14/1983, 1984-02-28, pp. 459-476) | — | 9 | max 15 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Loueurs de véhicules | 1985-02-18 (n° 22/1985, 1985-03-19, pp. 405-417) | — | 6 | max 12 ; 5 numéros distincts | 2019-05-28 |
| Répartiteurs de médicaments | 1985-02-05 (n° 34/1985, 1985-04-30, pp. 650-661) | — | 3 | max 3 ; 3 numéros distincts | 1993-08-02 |
| Transformation du verre et miroiterie | 1985-09-07 (n° 69/1985, 1985-10-04, pp. 1303-1313) | — | 9 | max 15 ; 10 numéros distincts | 2018-12-03 ; plein texte FR : 2022 |
| Enseignement privé | 1987-05-05 (n° 57/1987, 1987-08-18, pp. 983-1001) | — | 7 | max 12 ; 7 numéros distincts | 2016-05-25 |
| Concessionnaires de matériel agricole et de génie civil | 1987-05-05 (n° 62/1987, 1987-09-08, pp. 1074-1088) | — | 9 | max 15 ; 10 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Gardiennage, sécurité, transport de fonds | 1989-07-27 (n° 58/1989, 1989-08-29, pp. 1299-1311) | — | 4 | max 8 ; 4 numéros distincts | 2023-12-12 |
| Cliniques privées | 1997-02-04 (n° 14/1997, 1997-02-18, pp. 235-243) | — | 6 | max 9 ; 6 numéros distincts | 2018-02-02 ; plein texte FR : 2019 |
| Transport routier de marchandises | 1997-02-04 (n° 14/1997, 1997-02-18, pp. 244-254) | — | 4 | max 9 ; 5 numéros distincts | 2018-02-23 |
| Agences de voyages | 1997-05-15 (n° 41/1997, 1997-05-23, pp. 912-921) | — | 5 | max 12 ; 7 numéros distincts | 2018-11-30 ; plein texte FR : 2025 |
| Électricité et électronique (1999) | 1999-09-15 (n° 78/1999, 1999-09-28, pp. 1781-1805) | — | 7 | max 10 ; 8 numéros distincts | 2018-11-30 ; plein texte FR : 2022 |
| Mécanique générale et stations de vente de carburant (2000) | 2000-02-09 (n° 14/2000, 2000-02-18, pp. 472-490) | — | 7 | max 10 ; 7 numéros distincts | 2023-04-10 |
| Jardins d'enfants et crèches | — (aucune notice d'agrément) | — | 2 | max 3 ; 2 numéros distincts | 2011-10-14 |
| Associations de personnes handicapées | 2013-01-04 (n° 12/2013, 2013-02-08, p. 548) | — | 2 | max 3 ; 3 numéros distincts | 2019-06-26 ; plein texte FR : 2022 |
| Clercs d'avocats | 2014-09-11 (n° 77/2014, 2014-09-23, p. 2521) | — | 0 | — | — |
| Gestion des déchets solides et liquides | 2014-11-21 (n° 97/2014, 2014-12-02, p. 3165) | — | 3 | max 4 ; 4 numéros distincts | 2023-03-21 ; plein texte FR : 2025 |
| Grands, moyens et petits espaces commerciaux | 2025-02-04 (n° 15/2025, 2025-02-05, p. 312) | — | 0 | — | — |

Hors tableau : convention collective cadre (arrêté du 29 mai 1973, n° 21/1973, pp. 852-859 ;
avenants repérés par notice : n° 13/1985, n° 12/1993 « avenant n° 2 », n° 38/2004 « avenant
n° 3 ») ; convention cadre du secteur agricole (2015, ci-dessus) ; « convention cadre des
journalistes tunisiens » (arrêté du 30 avril 2019, n° 36/2019, plein texte FR, non rattachée).
47 notices d'avenant ne sont rattachées à aucune branche : ce sont les avis collectifs de
1996-2012 et les avenants à la convention cadre.

Le rattachement est fait par mots-clés (script `branches.py`) et n'a pas été relu ligne à ligne :
le nombre de notices par branche est indicatif, le numéro maximal d'avenant est fiable (il est lu
dans le titre).

### A.4 Lisibilité au corpus, par époque (vaut pour toutes les branches)

| Époque | Où est la grille | État au corpus local | Ce qu'il faut pour lire |
|---|---|---|---|
| 1974-1977, conventions d'origine | édition française, notices de type « Convention » | fascicules présents, **scans sans couche texte** | repérage par OCR (une minute par fascicule), lecture à l'image |
| 1983-1993, avenants n° 1 à 4 | édition française | scans sans couche texte | idem ; grilles pivotées de 90° |
| 1994, avenant n° 5 (textile, confection) | édition française | couche texte pour l'arrêté, **grilles en image** | lecture à l'image |
| 1996-2009, avenants n° 5/6 à 9/10 | **édition arabe seule** | fascicules présents, **pages entièrement en image** (2002 vérifié), couche texte inexploitable | lecture de l'arabe à l'image pour trouver la page, puis lecture de la grille |
| 2011-2014 | édition arabe seule | couche texte aux lettres mal encodées mais **chiffres en clair** | repérage par les chiffres (`nums.py`), contrôle du titre à l'image |
| 2016-2025 | édition arabe seule | texte de l'avenant en couche texte correcte, **grilles en image** | repérage par le texte, lecture de la grille à l'image |

### A.5 Série annuelle des arrêtés d'agrément d'avenants

Deux mesures, à ne pas additionner. Colonne 2 : notices de `jort_cache` classées « avenant »
(requête R1), par année du fascicule. Colonne 5 : arrêtés individuels repérés au plein texte de
l'édition française (1994 →). Les années absentes du tableau n'ont aucune notice ni aucun arrêté
repéré ; cela ne prouve pas qu'aucun avenant n'a paru (2020 et 2021 : aucun avenant de convention
*collective* au plein texte français, les seuls textes repérés concernant les conventions de
l'assurance maladie avec les professions de santé, hors champ).

| Année | Notices `jort_cache` (total) | dont titre français | dont titre arabe seul | Arrêtés individuels au plein texte FR (1994 →) | Remarque |
|---|---:|---:|---:|---:|---|
| 1974 | 1 | 1 | 0 | n. d. |  |
| 1978 | 1 | 1 | 0 | n. d. |  |
| 1981 | 1 | 1 | 0 | n. d. |  |
| 1983 | 35 | 35 | 0 | n. d. |  |
| 1985 | 2 | 2 | 0 | n. d. |  |
| 1989 | 43 | 43 | 0 | n. d. |  |
| 1990 | 39 | 39 | 0 | n. d. |  |
| 1991 | 6 | 6 | 0 | n. d. |  |
| 1993 | 51 | 51 | 0 | n. d. |  |
| 1994 | 3 | 3 | 0 | 3 |  |
| 1996 | 11 | 11 | 0 | 5 | 1 avis collectif : « quarante conventions » (n° 60) |
| 1997 | 1 | 1 | 0 | 1 |  |
| 1999 | 9 | 9 | 0 | 1 | 1 avis collectif : « vingt conventions » (n° 48) |
| 2000 | 1 | 1 | 0 | 1 |  |
| 2002 | 9 | 9 | 0 | 1 | avis collectifs aux n° 97 à 101 |
| 2003 | 2 | 2 | 0 | 2 |  |
| 2004 | 1 | 1 | 0 | 2 |  |
| 2006 | 10 | 10 | 0 | 1 | avis collectifs aux n° 6, 7, 8, 13 |
| 2007 | 1 | 1 | 0 | 1 |  |
| 2009 | 14 | 14 | 0 | 5 | avis collectifs aux n° 16, 39, 45, 60 |
| 2011 | 38 | 0 | 38 | 0 | avis collectifs aux n° 78, 80, 81, 88 |
| 2012 | 2 | 2 | 0 | 0 | avis collectifs aux n° 23, 40 |
| 2013 | 40 | 40 | 0 | 41 |  |
| 2014 | 36 | 36 | 0 | 23 |  |
| 2015 | 9 | 8 | 1 | 15 |  |
| 2016 | 42 | 5 | 37 | 39 |  |
| 2017 | 42 | 3 | 39 | 39 |  |
| 2018 | 28 | 1 | 27 | 6 |  |
| 2019 | 20 | 3 | 17 | 19 |  |
| 2022 | 4 | 4 | 0 | 35 |  |
| 2023 | 5 | 5 | 0 | 5 | dont un arrêté que le journal date par coquille du « 11 avril 1023 » (savonneries, n° 38), rétabli à la main |
| 2024 | 3 | 3 | 0 | 3 |  |
| 2025 | 2 | 2 | 0 | 4 |  |

Lecture : les vagues suivent les rounds — 1983, 1989-1990, 1993, 1996, 1999, 2002, 2006, 2009,
2011, 2013-2014, 2016-2017, 2018-2019, 2022. **De 1996 à 2012 la colonne des notices sous-compte**
(avis collectifs : « quarante conventions » en 1996, « vingt » le 9 juin 1999) ; pour ces années
le nombre exact d'avenants ne s'obtient que sur l'édition arabe. 2022 : 4 notices mais 35 arrêtés
au plein texte — la base n'a pas indexé la vague de 2022. Écart avec les pics de la note du
5 octobre (45 en 1989, 53 en 1993, 44 en 2013) : ils comptaient toutes les notices contenant
« convention collective », agréments et décrets compris ; les avenants seuls donnent 43, 51 et 40.

## B. Les grilles du textile et du bâtiment-travaux publics

### B.1 La chaîne des textes

**Textile** — chaîne complète, lue dans les visas de l'arrêté du 8 avril 2024 (JORT n° 49 du
16 avril 2024, p. 1257, texte FR) et dans le préambule de l'avenant n° 18 (édition arabe du même
numéro, pp. 3503-3504, texte) :

| Étape | Signature | Arrêté | Publication (numéro et date tels que cités par l'avenant n° 18) |
|---|---|---|---|
| Convention | 26 juill. 1974 | 29 août 1974 | n° 76 des 10 et 12 déc. 1974 (FR pp. 2715-2733) |
| Extension du champ | — | 5 mai 1976 | n° 31/1976, p. 1048 (notice) |
| Sentence arbitrale (chaussure, textile, confection, bonneterie) | 27 juin 1983 | 27 juin 1983 | n° 57 des 30 août et 2 sept. 1983 |
| Avenant n° 2 | 22 févr. 1989 | 22 mars 1989 | n° 21 du 24 mars 1989 (FR pp. 524-528, notice) |
| n° 3 | 14 juill. 1990 | 16 août 1990 | n° 54 des 21 et 24 août 1990 (FR pp. 1102-1109) |
| n° 4 | 12 août 1993 | 7 sept. 1993 | n° 70 du 17 sept. 1993 (FR pp. 1518-1525, notice) |
| n° 5 | 12 août 1994 | 22 sept. 1994 | n° 78 du 4 oct. 1994 (FR pp. 1637-1641) |
| n° 6 | 23 juill. 1996 | 24 juill. 1996 | n° 60 du 26 juill. 1996 (arabe seul) |
| n° 7 | 28 mai 1999 | 9 juin 1999 | n° 48 du 15 juin 1999 (arabe seul) |
| n° 8 | 14 nov. 2002 | 25 nov. 2002 | n° 97 du 29 nov. 2002 (arabe seul) |
| n° 9 | 29 déc. 2005 | 17 janv. 2006 | n° 7 du 24 janv. 2006 (arabe seul) |
| n° 10 | 28 janv. 2009 | 17 févr. 2009 | n° 16 du 24 févr. 2009 (arabe seul) |
| n° 11 | 23 sept. 2011 | 11 oct. 2011 | n° 78 du 14 oct. 2011 (arabe seul) |
| n° 12 | 29 janv. 2013 | 19 févr. 2013 | n° 16 du 22 févr. 2013 |
| n° 13 | 2 oct. 2014 | 17 oct. 2014 | n° 90 du 7 nov. 2014 |
| n° 14 | 22 mars 2016 | 8 avr. 2016 | n° 30 du 12 avr. 2016 |
| n° 15 | 18 juill. 2017 | 14 août 2017 | n° 66 du 18 août 2017 |
| n° 16 | 27 déc. 2018 | 21 janv. 2019 | n° 11 du 5 févr. 2019 |
| n° 17 | 12 mai 2022 | 23 juin 2022 | n° 71 du 24 juin 2022 |
| n° 18 | 29 févr. 2024 | 8 avr. 2024 | n° 49 du 16 avr. 2024 |

Il n'existe pas d'« avenant n° 1 » du textile : la sentence arbitrale de 1983 en tient lieu.
L'édition arabe cite l'avenant n° 3 au « n° 55 des 28 et 31 août 1990 », l'édition française de
1994 au « n° 54 des 21 et 24 août 1990 » : c'est le n° 54 qui porte le texte français (vu à
l'image, pied de page « 21-24 août 1990, N° 54 »).

**Bâtiment et travaux publics** — chaîne lue dans le préambule de l'avenant n° 15 (édition arabe
du n° 4 du 11 janvier 2019, p. 118, texte ; numéros et dates de publication tels qu'il les cite)
et recoupée par les notices :

| Étape | Signature | Arrêté | Publication |
|---|---|---|---|
| Convention | 16 janv. 1975 | 12 mars 1975 | arrêté n° 18 du 14 mars 1975, p. 504 ; texte n° 20 du 25 mars 1975 (FR pp. 557-571) ; rectificatif n° 28 du 25 avr. 1975, p. 824 (notice) |
| Avenant n° 1 | 8 mars 1983 | 14 avr. 1983 | arrêté n° 30/1983, p. 1044 (notice) ; texte n° 38 du 20 mai 1983 |
| n° 2 | 12 juill. 1989 | 10 août 1989 | n° 58 du 29 août 1989 (FR pp. 1312-1313, notice) |
| n° 3 | 14 juill. 1990 | 16 août 1990 | n° 54 des 21 et 24 août 1990 (FR pp. 1095-1101) |
| n° 4 | 12 août 1993 | 7 sept. 1993 | n° 69 du 14 sept. 1993 (FR pp. 1491-1497, notice) |
| n° 5 | 24 sept. 1996 | 16 oct. 1996 | n° 86 du 25 oct. 1996 (**FR pp. 2148-2152, texte et grilles en français**) |
| n° 6 | 28 mai 1999 | n. r. | n° 48 du 15 juin 1999 (arabe seul) |
| n° 7 | 14 nov. 2002 | n. r. | n° 98 du 3 déc. 2002 (arabe seul) |
| n° 8 | 29 déc. 2005 | n. r. | n° 7 du 24 janv. 2006 (arabe seul) |
| n° 9 | 28 janv. 2009 | n. r. | n° 16 du 24 févr. 2009 (arabe seul) |
| n° 10 | 5 oct. 2011 | 14 oct. 2011 | n° 81 du 25 oct. 2011 (arabe seul) |
| n° 11 | 25 févr. 2013 | 8 mars 2013 | n° 22 du 15 mars 2013 (FR p. 985) |
| n° 12 | 10 oct. 2014 | 27 oct. 2014 | n° 90 du 7 nov. 2014 (FR pp. 2982-2983) |
| n° 13 | 13 avr. 2016 | 2 mai 2016 | n° 37 du 6 mai 2016 (FR pp. 1460-1461) |
| n° 14 | 11 juill. 2017 | 30 août 2017 | n° 72 du 8 sept. 2017 |
| n° 15 | 26 nov. 2018 | 17 déc. 2018 | n° 4 du 11 janv. 2019 |
| n° 16 | n. r. | 25 nov. 2022 | n° 132 du 2 déc. 2022, p. 3387 — **notice seule : fascicule absent du corpus et de pist.tn** (§ D) |

« n. r. » : non relevé. Aucun avenant n° 17 n'est repéré (notices jusqu'au 2 octobre 2026 ;
plein texte français 2023-2026, « bâtiment et des travaux publics », lignes recollées) : ce
silence ne prouve pas qu'il n'existe pas.

### B.2 Structure des grilles

- **Textile.** Deux grilles par date : *agents payés à l'heure* (personnel d'exécution, catégories
  I, II, III-1 à III-3, IV-1 et IV-2 ; échelons 0 « confirmation » — الترسيم — à 16 en 1974, à 20
  depuis 2011 au moins) et *agents payés au mois* (catégories 1 à 17). Le bas de grille est la
  **catégorie I, échelon 0**, en dinars par heure. Régime horaire : la grille horaire n'en porte
  pas ; la grille mensuelle de 2024 donne 595,401 D pour la catégorie 1 en période de stage, soit
  environ 209 fois le taux horaire d'entrée — cohérent avec le régime de 48 heures (208 heures
  par mois), sans que le texte lu le dise. **Régime à confirmer** sur l'article de la convention
  relatif à la durée du travail.
- **Bâtiment.** Grille n° 1 du *personnel occasionnel* (العملة العرضيين), un salaire horaire par
  catégorie, sans échelon : manœuvre ordinaire (1), manœuvre spécialisé (2), aide-ouvrier (3),
  ouvrier qualifié de 1re et de 2e catégorie (4, 5), ouvrier hautement qualifié I et II (6), chef
  d'équipe à trois degrés (7). Grille n° 2 du *personnel administratif et technique à traitement
  mensuel*, 19 catégories, 11 échelons, « base : 48 heures/semaine » (1975, image). Le bas de
  grille est le **manœuvre ordinaire**, en dinars par heure ; en 1975 la catégorie 1, échelon 1,
  de la grille mensuelle vaut 27,040 D, soit exactement le SMIG mensuel du régime de 48 heures.
- Depuis 1994, chaque grille porte la mention que les salaires « comprennent l'indemnité
  complémentaire provisoire » des décrets n° 81-437 et n° 82-501.

### B.3 Textile : salaire horaire de base, catégorie I échelon 0, et haut de la grille d'exécution

Dinars par heure. « Haut » = catégorie IV-2, échelon 0. SMIG : régime de 48 heures, taux horaire
en vigueur à la date d'effet (dernière ligne antérieure ou égale de
`precis/_seriescache/marche-travail-smig-smag.csv`).

| Date d'effet | Bas (I-0) | Haut (IV-2, éch. 0) | Hausse du bas | SMIG 48 h (depuis le) | Bas / SMIG | Source (JORT) | Lecture |
|---|---:|---:|---:|---:|---:|---|---|
| conv. 1974 (date d'effet non relevée) | 0,130 | 0,250 | — | 0,130 (1er juin 1974) | 1,00 | n° 76, 10 déc. 1974, p. 2729 (FR) | image |
| 1er mai 1990 | 0,431 * | 0,589 * | — | 0,577 | n. c. | n° 54, 21-24 août 1990, p. 1104 (FR) | image |
| 1er mai 1991 | 0,479 * | 0,671 * | +11,1 % | 0,577 | n. c. | id., p. 1106 | image |
| 1er mai 1992 | 0,527 * | 0,753 * | +10,0 % | 0,639 | n. c. | id., p. 1108 | image |
| 1er mai 1994 | 0,749 | 1,005 | rupture | 0,697 (1er août 1993) | 1,07 | n° 78, 4 oct. 1994, p. 1638 (FR) | image |
| 1er mai 1995 | 0,787 | 1,053 | +5,1 % | 0,741 | 1,06 | id., p. 1640 | image |
| *1996-2010 : avenants n° 6 à 10, non lus* | | | | | | | |
| 1er mai 2011 | 1,533 | 2,192 | — | 1,375 | 1,11 | n° 78, 14 oct. 2011, éd. arabe p. 2194 | texte ; branche et page à l'image ; **date d'effet lue à faible résolution, à confirmer** (recoupée par celle du bâtiment, même round) |
| 1er mai 2012 | 1,625 | 2,323 | +6,0 % | 1,375 | 1,18 | n° 16, 22 févr. 2013, éd. arabe p. 845 | texte ; titre et date à l'image |
| 1er mai 2014 | 1,722 | 2,462 | +6,0 % | 1,538 | 1,12 | n° 90, 7 nov. 2014, éd. arabe p. 3100 | texte |
| 1er sept. 2015 | 1,826 | n. l. | +6,0 % | 1,625 | 1,12 | n° 30, 12 avr. 2016, éd. arabe p. 1320 | image |
| 1er août 2016 | 1,935 | 2,767 | +6,0 % | 1,717 | 1,13 | n° 66, 18 août 2017, éd. arabe p. 2681 | image |
| 1er janv. 2018 | 2,051 | 2,933 | +6,0 % | 1,717 | 1,19 | id., p. 2683 | image |
| 1er janv. 2019 | 2,195 | 3,138 | +7,0 % | 1,820 | 1,21 | n° 11, 5 févr. 2019, éd. arabe p. 387 | image |
| 1er janv. 2020 | 2,348 | 3,358 | +7,0 % | 1,938 | 1,21 | id., p. 389 | image |
| 1er sept. 2021 | 2,501 | 3,576 | +6,5 % | 2,064 | 1,21 | n° 71, 24 juin 2022, éd. arabe p. 2150 | image |
| 1er mai 2022 | 2,676 | 3,826 | +7,0 % | 2,064 | 1,30 | id., p. 2152 | image |
| 1er janv. 2024 | 2,850 | 4,075 | +6,5 % | 2,208 | 1,29 | n° 49, 16 avr. 2024, éd. arabe p. 3507 | image |
| 1er janv. 2025 | 3,035 | 4,340 | +6,5 % | 2,540 | 1,19 | id., p. 3509 | image |
| 1er janv. 2026 | 3,248 | 4,644 | +7,0 % | 2,667 | 1,22 | id., p. 3511 | image |

\* Hors indemnité complémentaire provisoire (décrets n° 81-437 et n° 82-501) : non comparable au
SMIG de la série, d'où « n. c. ». Les pages arabes de 2019 et 2017 sont déduites du pied de page
de la dernière page de texte de l'avenant (p. 386 et p. 2680) ; à contrôler à l'image avant
citation. Les montages de 2015-2020 ont été lus à résolution réduite : les hausses successives
(6,0 ; 6,0 ; 7,0 ; 7,0 ; 6,5 ; 7,0 ; 6,5 %) recoupent la lecture, sans la remplacer.

Autres lectures utiles : grille mensuelle du textile au 1er janvier 2024, catégorie 1 (1 أ),
période de stage 595,401 D, échelon 1 604,366 D (n° 49/2024, éd. arabe p. 3508, image). Grille
horaire de 1974, catégorie I : 0,130 (confirmation) à 0,208 D (échelon 16, 29 ans d'ancienneté) ;
IV-2 : 0,250 à 0,400 D. Avenant n° 18 : chaque passage d'échelon vaut 1 % du salaire de l'échelon
quitté (article 12, texte arabe, p. 3505).

**Indemnités forfaitaires du textile** (dinars par mois ; couche texte de l'édition arabe).
Pour 2024-2026 l'attribution des montants est lue en clair ; pour 2016-2022 les colonnes du texte
sont entrelacées et l'attribution est établie **par continuité** avec 2024 — à contrôler à l'image.
Indice à l'appui, qui ne vaut pas lecture : chaque série monte du même pas que la grille (6,0 %
en 2018, 7,0 % en 2019 et 2020, 6,5 % en 2021, 7,0 % en 2022).

| Date d'effet | Présence | Transport, exécution et maîtrise | Transport, cadres | Assiduité | Source (éd. arabe) |
|---|---:|---:|---:|---:|---|
| 1er mai 2014 | n. l. | 29 + 5 | 29 + 10 | n. l. | n° 90/2014, p. 3099 |
| 1er sept. 2015 | 5,080 | 39 + 5 | 39 + 10 | n. l. | n° 30/2016, pp. 1318-1319 |
| 1er août 2016 | 5,384 | 46,640 | 51,940 | 9,540 | n° 66/2017, pp. 2679-2680 |
| 1er janv. 2018 | 5,707 | 49,438 | 55,050 | 10,112 | id. |
| 1er janv. 2019 | 6,106 | 52,899 | 58,904 | 10,820 | n° 11/2019, pp. 385-386 |
| 1er janv. 2020 | 6,534 | 56,602 | 63,027 | 11,577 | id. |
| 1er sept. 2021 | 6,959 | 60,281 | 67,123 | 12,330 | n° 71/2022, pp. 2148-2149 |
| 1er mai 2022 | 7,446 | 64,500 | 71,822 | n. l. | id. |
| 1er janv. 2024 | 7,930 | 68,693 | 76,491 | 14,050 | n° 49/2024, p. 3505 |
| 1er janv. 2025 | 8,445 | 73,158 | 81,462 | 14,964 | id. |
| 1er janv. 2026 | 9,036 | 78,279 | 87,165 | 16,011 | id. |

L'indemnité de transport inclut les montants du décret n° 82-503 du 16 mars 1982 (5 D pour
l'exécution et la maîtrise, 10 D pour les cadres) ; la prime d'assiduité inclut les 6 D de la
sentence arbitrale de 1983 et n'est pas due au-delà d'une absence injustifiée par mois ;
l'indemnité de présence inclut l'« indemnité de demi-journée » du décret du 8 janvier 1948
(avenant n° 18, article 49 nouveau, p. 3505, texte). Aucune indemnité de panier n'apparaît dans
les avenants du textile lus. Au 1er janvier 2024, présence, transport et assiduité font
90,673 D par mois pour un agent d'exécution, soit environ 15 % du salaire mensuel d'entrée
(595,401 D) — calcul de cette note.

### B.4 Bâtiment et travaux publics : salaire horaire du personnel occasionnel

Dinars par heure. « Haut » = chef d'équipe, 3e degré.

| Date d'effet | Manœuvre ordinaire | Chef d'équipe 3e degré | Hausse du bas | SMIG 48 h (depuis le) | Bas / SMIG | Source (JORT) | Lecture |
|---|---:|---:|---:|---:|---:|---|---|
| conv. 1975 (date d'effet non relevée) | 0,140 | 0,315 | — | 0,130 (1er juin 1974) | 1,08 | n° 20, 25 mars 1975, p. 570 (FR) | image |
| 1er mai 1990 | 0,441 * | 0,661 * | — | 0,577 | n. c. | n° 54, 21-24 août 1990, p. 1096 (FR) | image |
| *1991-1995 : avenants n° 3 (suite) et n° 4, non lus* | | | | | | | |
| 1er mai 1996 | 0,862 | 1,285 | rupture | 0,770 | 1,12 | n° 86, 25 oct. 1996, p. 2150 (FR) | image |
| 1er mai 1997 | 0,906 | 1,358 | +5,1 % | 0,780 (9 sept. 1996) | 1,16 | id., p. 2151 | image |
| 1er mai 1998 | 0,950 | 1,431 | +4,9 % | 0,819 (7 nov. 1997) | 1,16 | id., p. 2152 | image |
| *1999-2010 : avenants n° 6 à 9, non lus (édition arabe)* | | | | | | | |
| 1er mai 2011 | 1,588 | 2,685 | — | 1,375 | 1,15 | n° 81, 25 oct. 2011 (date de notice), éd. arabe p. 2442 | image |
| 1er mai 2012 | 1,683 | 2,846 | +6,0 % | 1,375 | 1,22 | n° 22, 15 mars 2013, éd. arabe p. 1043 | texte ; titre et date à l'image |
| 1er mai 2014 | 1,784 | 3,017 | +6,0 % | 1,538 | 1,16 | n° 90, 7 nov. 2014, éd. arabe p. 3120 | texte |
| 1er sept. 2015 | 1,891 | 3,198 | +6,0 % | 1,625 | 1,16 | n° 37, 6 mai 2016, éd. arabe p. 1703 | image |
| 1er août 2016 | 2,004 | 3,390 | +6,0 % | 1,717 | 1,17 | n° 72, 8 sept. 2017, éd. arabe p. 3034 | image |
| 1er mai 2017 | 2,125 | 3,593 | +6,0 % | 1,717 | 1,24 | id., p. 3035 | image |
| 1er mai 2018 | 2,263 | 3,827 | +6,5 % | 1,820 | 1,24 | n° 4, 11 janv. 2019, éd. arabe p. 121 | image |
| 1er mai 2019 | 2,410 | 4,076 | +6,5 % | 1,938 | 1,24 | id., p. 122 | image |
| *2020 → : avenant n° 16 (2022) non lu, fascicule introuvable* | | | | | | | |

\* Hors indemnité complémentaire provisoire. Grille mensuelle : catégorie 1, échelon 1, 27,040 D
en 1975 (p. 570, image) ; 363,988 D au 1er mai 2014 (n° 90/2014, éd. arabe p. 3120, texte).
Annexe V de 1975 : chauffeurs, 0,200 à 0,300 D l'heure selon le tonnage. Indemnité journalière
relevée par OCR dans l'avenant n° 3 de 1990 (1,115 D par jour au 1er mai 1990, 1,230 D au
1er mai 1991, p. 1095) : **nature non lue**, à relire à l'image.

Indemnités mensuelles du bâtiment relevées dans la couche texte arabe, **nature non établie**
(colonnes entrelacées ; vraisemblablement transport pour la plus élevée, présence pour l'autre) :
1er août 2016 : 62,010 et 5,384 D ; 1er mai 2017 : 65,730 et 5,707 D (n° 72/2017, pp. 3032-3033) ;
1er mai 2018 : 70,002 et 6,078 D ; 1er mai 2019 : 74,553 et 6,473 D (n° 4/2019, pp. 118-119).
À relire à l'image avant tout usage.

### B.5 Ce que montre le rapport au SMIG (constat)

- **À l'origine, le bas de grille est le SMIG ou presque** : textile 1974, 0,130 D pour un SMIG de
  0,130 D (rapport 1,00) ; bâtiment 1975, 0,140 D (1,08), et la catégorie 1 de la grille
  mensuelle vaut exactement le SMIG mensuel de 48 heures (27,040 D).
- **En 1994-1998**, premières dates où grille et SMIG sont de nouveau comparables : 1,06 à 1,07
  pour le textile (1994, 1995), 1,12 à 1,16 pour le bâtiment (1996 à 1998).
- **De 2011 à 2026** le rapport est toujours supérieur à 1 : textile entre 1,11 et 1,30,
  bâtiment entre 1,15 et 1,24 (jusqu'en 2019). Le bâtiment est au-dessus du textile de quatre
  points à chaque date commune (2011, 2012, 2014, 2015, 2016).
- Le rapport **monte en escalier entre deux relèvements du SMIG et retombe à chacun** : les
  avenants relèvent la grille de 6 à 7 % par an, le SMIG l'est par à-coups. Textile : 1,21 en
  septembre 2021, 1,30 en mai 2022 (SMIG inchangé depuis octobre 2020), 1,19 en janvier 2025 (SMIG
  porté à 2,540 D), 1,22 en janvier 2026.
- Sur 2011-2026 le bas de la grille du textile est multiplié par 2,12 (1,533 → 3,248 D), le SMIG
  horaire de 48 heures par 1,94 (1,375 → 2,667 D).
- Recoupement extérieur, à ne pas mêler à ces chiffres : « starting salaries in collective
  agreements, are on average 25 percent higher than the minimum wage (OECD, 2015) » (Belgacem et
  Vacher, 2023, annexe 2). L'étude de l'OCDE d'origine n'a pas été récupérée.

Limites : (i) le rapport compare des **salaires de base** ; les indemnités de la convention
(§ B.3) s'ajoutent au salaire conventionnel, et le SMIG a ses propres accessoires ; (ii) le régime
horaire du textile reste à confirmer ; (iii) les grilles de 1983-1993 excluent l'indemnité
complémentaire provisoire : pour les comparer, il faut le montant de cette indemnité (décrets
n° 81-437 et n° 82-501, non lus ici) et savoir si la série du SMIG l'inclut à ces dates.

### B.6 La hausse par décret de 2026 appliquée à ces deux grilles

Décret n° 2026-68 du 30 avril 2026 (JORT n° 44 du 30 avril 2026, pp. 838-839, texte FR) :
- art. 1 : hausse annuelle de 5 % des salaires de base et des indemnités de transport et de
  présence, « au titre des années 2026, 2027 et 2028, à compter du 1er janvier 2026 » ; pour 2026
  elle « s'applique sur les salaires de base et pour tous les échelons inclus dans les dernières
  grilles des salaires annexées aux conventions collectives sectorielles » ; pour 2027 et 2028,
  sur les salaires et indemnités « majorées au titre de l'année qui précède » ;
- art. 3 : elle bénéficie aussi aux travailleurs payés au-dessus des grilles ;
- art. 4 : en sont exclus « les travailleurs des entreprises ayant octroyé au cours de la même
  année, des augmentations générales des salaires égales ou supérieures ».

**Aucun texte ne publie les grilles qui en résultent** : aucun arrêté d'agrément d'avenant n'est
repéré en 2026 (notices jusqu'au 2 octobre 2026 ; plein texte français des n° 1 à 97, où seul le
n° 44 répond à « grille des salaires »). Les grilles de 2026 à 2028 sont donc à calculer par
l'employeur.

Application aux deux branches, telle que les textes la laissent lire, sans interprétation :
- **Textile** : la convention porte déjà une grille au 1er janvier 2026 (avenant n° 18, tableaux
  n° 5 et 6 : 3,248 D, soit +7,0 % sur 2025), et des indemnités au 1er janvier 2026 (présence
  9,036 D, transport 78,279 D : +7,0 %). Le décret ne dit pas si « les dernières grilles » sont
  celles de 2025 ou celle de 2026, ni comment sa hausse se combine avec une hausse conventionnelle
  déjà fixée pour la même année ; l'article 4 vise les hausses d'entreprise. Arithmétique seule :
  5 % sur la grille de 2025 donneraient 3,187 D, moins que les 3,248 D conventionnels ; 5 % sur
  celle de 2026 donneraient 3,410 D. **Point à faire trancher** (circulaire du ministère des
  affaires sociales, non cherchée), à ne pas écrire dans le chapitre comme un état du droit.
- **Bâtiment** : la dernière grille lue est celle du 1er mai 2019 ; la « dernière grille » au
  sens du décret est celle de l'avenant n° 16 (2022), non lue. Aucune valeur de 2026 ne peut être
  donnée.

## C. La couverture

### C.1 Ce qui est trouvé : la série de l'OIT

**Famille : rapport extérieur** (organisation internationale), sur fichiers administratifs
nationaux. Indicateur ILOSTAT « Collective bargaining coverage rate (%) », code
`ILR_CBCT_NOC_RT`, Tunisie, annuel :

| 2010 | 2011 | 2012 | 2013 | 2014 | 2016 | 2017 | 2018 | 2019 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 54,9 | 55,1 | 57,7 | 56,2 | 56,9 | 64,3 | 61,5 | 62,4 | 62,9 |

- Définition (libellé de l'indicateur) : nombre de salariés dont la rémunération ou les conditions
  d'emploi sont déterminées par une ou plusieurs conventions collectives, en pourcentage du nombre
  total de salariés ; note de source de chaque ligne : « Reference group coverage: Employees ».
- Source déclarée : « ADM - Other administrative records and related sources ». **L'administration
  productrice n'est pas nommée, le numérateur et le dénominateur ne sont pas publiés** dans le flux
  lu ; 2015 manque ; la série s'arrête en 2019 ; le saut de 2014 à 2016 (56,9 → 64,3) n'est pas
  expliqué. La méthode nationale reste donc à établir (fiche de métadonnées par pays d'ILOSTAT,
  non obtenue).
- Le taux porte sur **l'ensemble des salariés** (périmètre public/privé non précisé par la
  source) et, selon la définition générale de l'indicateur, sur toute convention (sectorielle ou
  d'établissement) : ce n'est pas la part des salariés du
  privé couverts par une convention *sectorielle*.
- Adresses, vérifiées le 8 octobre 2026 (réponse 200, contenu lu) :
  `https://sdmx.ilo.org/rest/data/ILO,DF_ILR_CBCT_NOC_RT/TUN..?format=csv` (neuf lignes) et
  `https://rplumber.ilo.org/data/indicator/?id=ILR_CBCT_NOC_RT_A&ref_area=TUN&format=.csv&type=label`
  (mêmes valeurs ; un navigateur ou un en-tête `User-Agent` est nécessaire). Extrait conservé :
  `data/raw/oit/ilostat/ilostat_cbct_tun.csv` de `tunisia-data` (hors git, à cataloguer), SHA-256
  `4e3325c198261f92916c39708f5b7270fd5b8a5c5178d3b952aa112f51781ef1` — **à ranger dans
  `tunisia-data`** (`data/raw/ilostat/`, ligne à `sources/ilostat-urls.csv`), ce que cette passe,
  tenue de ne modifier aucun dépôt, n'a pas fait.
- Même base, taux de syndicalisation (`ILR_TUMT_NOC_RT`), Tunisie : 20,4 % (2011), 27,2 % (2016),
  36,8 % (2017), 36,6 % (2018), 38,1 % (2019) ; source « ADM », sans autre précision.

### C.2 Rapports extérieurs qui donnent un chiffre (une ligne chacun, non instruits)

- Belgacem et Vacher, « Why is Tunisia's unemployment so high? Evidence from policy factors »,
  version préliminaire de juillet 2023 (auteurs du FMI, mention « please do not quote »), annexe 2,
  p. 30 du PDF : « Collective agreements apply to 57 percent of the total number of employees
  (ILOSTAT, 2014) » — c'est le 56,9 ci-dessus ; le salaire minimum ne s'appliquerait qu'aux
  secteurs sans convention, « 15 percent of the labor force, MDICI estimates, 2015 » (estimation
  du ministère du développement, **de seconde main, source d'origine non retrouvée**). PDF
  récupéré (`data/raw/emploi/etudes/belgacem-vacher-2023.pdf` de `tunisia-data` (hors git, à cataloguer), SHA-256
  `4e8618a8b5b78d8ba1e4b9d533cdb7a15f15f82bdf513d266a4be57ad6a6d300`), à ranger
  dans `tunisia-data` s'il est cité.

### C.3 Ce qui n'est pas trouvé, et où il a été cherché

- **Producteur national de la série de l'OIT** : non établi. Recherche en ligne « ILOSTAT
  industrial relations data sources Tunisia » : la description générale de la base
  (`https://ilostat.ilo.org/methods/concepts-and-definitions/description-industrial-relations-data`)
  dit que les sources sont des registres administratifs tenus par les syndicats ou les ministères
  du travail, questionnaire annuel d'ILOSTAT et enquêtes d'experts nationaux, sans fiche propre à
  la Tunisie dans les résultats obtenus.
- **Ministère des affaires sociales** (nombre de salariés couverts par convention sectorielle,
  par branche) : l'index des archives du web (`web.archive.org/cdx`, `social.gov.tn*`, filtre
  « convention | negociation | statisti ») rend une rubrique `social.gov.tn/conventions`
  (captures de 2022 à 2025, en français, arabe et anglais, avec un filtre `?service=`) ; **son
  contenu n'a pas pu être lu** (l'outil de lecture refuse web.archive.org ; l'interface
  `archive.org/wayback/available` a répondu 429). À ouvrir dans un navigateur : c'est
  vraisemblablement la liste des conventions, non une mesure d'effectifs. Annuaires statistiques
  du ministère : non cherchés.
  Le corpus local (`data/conventions_collectives/`, `data/ugtt/`) n'en contient pas.
- **INS** : non cherché en ligne ; `tunisia-data` n'a aucune série de couverture (constat de la
  note du 5 octobre, non refait).
- Page de profil par pays d'ILOSTAT (`https://ilostat.ilo.org/data/country-profiles/tun/`) :
  réponse 403 aux deux essais (outil de lecture et `curl`) ; les données ont été obtenues par les
  deux interfaces de programmation ci-dessus.
- Effectifs salariés par branche (dénominateur d'un poids par convention) : non cherchés.

## D. Lacunes et coût

| Ce qui manque | Nature | Coût estimé |
|---|---|---|
| Textile, sentence de 1983 (n° 57/1983) et avenants n° 2 (n° 21/1989) et n° 4 (n° 70/1993) ; bâtiment, avenants n° 1 (texte au n° 38 du 20 mai 1983), n° 2 (n° 58/1989), n° 3 pour 1991-1992 (n° 54/1990, pages 1097 et suivantes), n° 4 (n° 69/1993) | fichiers au corpus, scans français | faible : par fascicule, un repérage par OCR (une à deux minutes au premier plan) et une ou deux lectures à l'image ; six fascicules |
| Montant de l'indemnité complémentaire provisoire (décrets n° 81-437 et n° 82-501), pour raccorder 1983-1993 à la suite | fichiers au corpus (scans de 1981 et 1982) | faible : deux décrets |
| Avenants n° 6 à 10 du textile (n° 60/1996, 48/1999, 97/2002, 7/2006, 16/2009) et n° 6 à 9 du bâtiment (n° 48/1999, 98/2002, 7/2006, 16/2009) | fichiers au corpus, édition arabe en image | **moyen à élevé** : il faut lire l'arabe à l'image pour trouver l'avenant dans des fascicules de 60 à 320 pages (sommaire, puis pages), soit trois à cinq lectures par avenant ; neuf avenants dans six fascicules. Les éditions arabes des n° 60/1996 et n° 48/1999 sont des PDF valides (scans « Acrobat 4.0 Scan », 14 et 10 Mo), sans couche texte. Un OCR arabe n'est pas disponible (seuls `fra`, `eng` installés) |
| Bâtiment, avenant n° 16 (arrêté du 25 nov. 2022, n° 132 du 2 déc. 2022) | **fascicule absent du corpus local dans les deux éditions, et réponse 404 de pist.tn** aux adresses `2022F/Jo1322022.pdf` et `2022A/Ja1322022.pdf` (deux essais le 8 octobre 2026 ; le n° 131 répond 200) ; seconde voie : aucun des 141 fascicules arabes de 2022 du corpus ne porte l'avenant | à obtenir : autre miroir (iort.gov.tn, portail de la législation), ou copie de l'UGTT ; tant qu'il manque, la série du bâtiment s'arrête au 1er mai 2019 |
| Bâtiment, existence d'un avenant n° 17 (2024-2025) | non repéré par deux voies (notices, plein texte français) | à confirmer sur les sommaires arabes de 2024-2025 |
| Régime horaire du textile ; date d'effet des conventions de 1974 et 1975 ; nature des indemnités du bâtiment | fichiers au corpus | faible : relire les articles de durée du travail et d'entrée en vigueur (scans de 1974 et 1975), deux pages de texte arabe de 2017 et 2019 à l'image |
| Méthode nationale de la série de couverture de l'OIT ; chiffre du ministère par branche | non publié dans les sources lues | recherche en ligne ciblée (métadonnées ILOSTAT, archives du site du ministère) |
| Grilles résultant du décret n° 2026-68 | **publiées nulle part** à ce jour | — |

**Étendre B à trois branches** (mécanique-électricité, commerce, hôtellerie). Les outils existent ;
l'ordre de grandeur constaté sur textile et bâtiment est d'une lecture à l'image par date de grille
pour 2015-2025 et d'une extraction de texte pour 2011-2014.
- *Commerce de gros, demi-gros et détail* : convention au n° 49 du 30 juillet 1976, pp. 1859-1872
  (texte et grille dans le même fascicule) ; avenants jusqu'au n° 16 (arrêté du 3 mars 2023,
  n° 23/2023). Coût comparable au textile : une quinzaine de lectures pour l'origine et 2011-2023.
- *Hôtellerie (hôtels classés touristiques)* : convention au n° 56 du 22 août 1975, pp. 1762-1787 ;
  avenants jusqu'au n° 18 (arrêté du 16 septembre 2024, n° 115/2024). Même coût ; grille
  vraisemblablement plus large (26 pages de convention), à vérifier.
- *Mécanique-électricité* : **la branche se scinde** — convention de 1974 (n° 2 du 10 janvier 1975,
  pp. 61-77), puis électricité et électronique (n° 78 du 28 septembre 1999, pp. 1781-1805) et
  mécanique générale et stations de vente de carburant (n° 14 du 18 février 2000, pp. 472-490),
  dont les textes fondateurs sont en français avec couche texte décalée (décodable). Deux séries
  après 1999, avenants jusqu'au n° 10 ; coût d'environ une fois et demie celui du textile. Le
  fichier `data/conventions_collectives/mecanique_electricite/grille_salaires_1974.yaml` donne une
  grille de 1974 **non relue au journal dans cette passe** : à vérifier contre le n° 2/1975 avant
  tout usage.
- Dans les trois cas, 1996-2009 reste au coût « moyen à élevé » ci-dessus.

## E. Vue d'évolution proposée pour le chapitre

**Figure** (une, à deux panneaux partageant l'axe du temps, 1974-2026) :
- panneau haut, dinars par heure, échelle logarithmique : SMIG horaire du régime de 48 heures en
  escalier (série existante) ; salaire de base d'entrée du textile (catégorie I, échelon 0) et du
  bâtiment (manœuvre ordinaire), en escalier, un palier par date d'effet ;
- panneau bas : rapport salaire d'entrée / SMIG, ligne de référence à 1 ;
- **segments, pas de ligne continue** : 1974-1975 (points d'origine) ; 1990-1992 en trait
  distinct et hors du panneau bas (grilles hors indemnité complémentaire provisoire) ; 1994-1998 ;
  2011 → ; les intervalles non lus (1996-2010 ; bâtiment après 2019) restent **vides**, sans
  interpolation ;
- ruptures à marquer : 1er mai 1994 (intégration de l'indemnité complémentaire provisoire) ;
  1996 (grilles publiées en arabe seulement — rupture de source, non de droit) ; 1er janvier 2026
  (hausse par décret).

**Tableau court** (dates repères, une ligne par date) : 1974-1975, 1994, 2011, 2014, 2019, 2022,
2024, 2026 — SMIG horaire, bas de grille du textile, bas de grille du bâtiment, les deux rapports.
Le tableau complet des § B.3 et B.4 va dans le bloc replié, avec sa colonne de source.

**Second tableau possible, replié** : indemnités du textile (présence, transport, assiduité),
2014-2026, une fois l'attribution de 2016-2022 contrôlée à l'image.

Données : les séries de cette note sont à verser dans `tunisia-data` (une ligne par branche, date
d'effet, catégorie, valeur, unité, source, niveau de lecture) avant toute figure, puisqu'un module
de figure lit l'entrepôt.

## Recherches infructueuses — fiches proposées (non versées)

```yaml
- id: r-btp-avenant-16-grilles
  objet: texte et grilles de l'avenant n° 16 à la convention collective sectorielle du bâtiment et des travaux publics (arrêté du 25 novembre 2022), et tout avenant postérieur
  ou: [docs/notes/marche-travail-conventions-collectives.md]
  requetes:
    titres_like: ['%avenant%batiment et des travaux publics%', '%avenant%bâtiment et des travaux publics%', '%للبناء والأشغال%']
    plein_texte: ['bâtiment et des travaux publics']
    depuis: 2019-01-11
  passes:
  - date: 2026-10-08
    role: documentaliste
    sources: [jort_cache, corpus_local, pist]
    couverture: 'notice trouvée (JORT n° 132 du 2 décembre 2022, p. 3387) mais fascicule absent du corpus local en français et en arabe, et réponse 404 de pist.tn aux adresses 2022F/Jo1322022.pdf et 2022A/Ja1322022.pdf ; plein texte français 2023-2026 (n° 1 à 97 de 2026) sans avenant n° 17 ; cache texte des 141 fascicules arabes de 2022, motif normalisé « عدد 16 للاتفاقية المشتركة القطاعية للبناء والأشغال » : aucun ; miroir iort (data/iort/textes/md) : aucun fichier ne porte « للبناء والأشغال » (il n''indexe pas les arrêtés d''avenant) ; sommaires arabes de 2023-2026 non lus'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun

- id: r-grilles-decret-2026-68
  objet: texte publiant les grilles de salaires des conventions sectorielles résultant du décret n° 2026-68 (5 % par an, 2026-2028), ou circulaire d'application disant comment la hausse se combine avec une grille conventionnelle déjà fixée pour 2026
  ou: [docs/notes/marche-travail-conventions-collectives.md]
  requetes:
    titres_like: ['%avenant%convention collective%']
    plein_texte: ['grilles des salaires', 'avenant n°']
    depuis: 2026-04-30
  passes:
  - date: 2026-10-08
    role: documentaliste
    sources: [jort_cache, corpus_local]
    couverture: 'notices de jort_cache jusqu''au 2 octobre 2026 ; plein texte français des fascicules de 2026 présents au cache (90 sur 94 ; le n° 96 français est le fichier arabe) ; édition arabe de 2026 non parcourue ; circulaires du ministère des affaires sociales non cherchées'
    couvert_jusqu_au: 2026-10-02
    resultat: aucun
```

(`ou` pointe provisoirement vers la note : aucune ancre n'existe dans un `.qmd`. La fiche
`r-accords-cadres-ugtt-utica` proposée le 5 octobre reste valable ; cette passe ne l'a pas
relancée.)

## Références candidates

Aucune de ces clés n'existe dans `precis/fr/marche_travail/references.json` (non vérifié fichier
ouvert dans cette passe : à contrôler par le bibliographe). Adresses pist.tn, édition française,
toutes vérifiées le 8 octobre 2026 (réponse 200, `application/pdf`) ; **le contenu français n'a
été ouvert que pour les fascicules marqués d'un astérisque** — pour les autres, la pagination
française de l'arrêté est celle de la notice ou du plein texte, et les grilles sont dans l'édition
arabe aux pages indiquées en B.

```json
[
 {"id":"convention-textile-1974","type":"legislation","title":"Convention collective nationale du textile, signée le 26 juillet 1974, agréée par arrêté du ministre des affaires sociales du 29 août 1974","issued":{"date-parts":[[1974,7,26]]},"container-title":"Journal officiel de la République tunisienne","issue":"76","page":"2715-2733","URL":"https://www.pist.tn/jort/1974/1974F/Jo07674.pdf","note":"* Grille horaire du personnel d'exécution p. 2729. Arrêté d'agrément : JORT n° 55 du 30 août 1974, p. 1936. Rectificatif de la grille mensuelle : JORT n° 25 du 15 avril 1975, p. 736 (notice)."},
 {"id":"convention-btp-1975","type":"legislation","title":"Convention collective nationale du bâtiment et des travaux publics, agréée par arrêté du ministre des affaires sociales du 12 mars 1975","issued":{"date-parts":[[1975,3,12]]},"container-title":"Journal officiel de la République tunisienne","issue":"20","page":"557-571","URL":"https://www.pist.tn/jort/1975/1975F/Jo02075.pdf","note":"* Annexes III (personnel occasionnel) et IV (personnel à traitement mensuel) p. 570. Date de signature non relevée. Rectificatif : JORT n° 28 du 25 avril 1975, p. 824 (notice)."},
 {"id":"avenants-1990-textile-btp","type":"legislation","title":"Arrêtés du ministre des affaires sociales du 16 août 1990, portant agrément de l'avenant n° 3 à la convention collective nationale du bâtiment et des travaux publics et de l'avenant n° 3 à la convention collective nationale du textile","issued":{"date-parts":[[1990,8,16]]},"container-title":"Journal officiel de la République tunisienne","issue":"54","page":"1095-1109","URL":"https://www.pist.tn/jort/1990/1990F/Jo05490.pdf","note":"* Deux arrêtés distincts (pp. 1095-1101 et 1102-1109) : à scinder en deux entrées si les deux sont cités. Intitulés à relever à l'image."},
 {"id":"avenant5-textile-1994","type":"legislation","title":"Arrêté du ministre des affaires sociales du 22 septembre 1994, portant agrément de l'avenant n° 5 à la convention collective nationale du textile","issued":{"date-parts":[[1994,9,22]]},"container-title":"Journal officiel de la République tunisienne","issue":"78","page":"1637-1641","URL":"https://www.pist.tn/jort/1994/1994F/Jo07894.pdf","note":"* Intègre l'indemnité complémentaire provisoire aux salaires de base à compter du 1er mai 1994."},
 {"id":"avenant5-btp-1996","type":"legislation","title":"Arrêté du ministre des affaires sociales du 16 octobre 1996, portant agrément de l'avenant n° 5 à la convention collective nationale du bâtiment et des travaux publics","issued":{"date-parts":[[1996,10,16]]},"container-title":"Journal officiel de la République tunisienne","issue":"86","page":"2148-2152","URL":"https://www.pist.tn/jort/1996/1996F/Jo08696.pdf","note":"* Avenant signé le 24 septembre 1996 ; grilles n° 1 à 6 pp. 2150-2152 (1er mai 1996, 1997, 1998). Adresse vérifiée (200, application/pdf)."},
 {"id":"arretes-1996-07-24-avenants-quarante-conventions","type":"legislation","title":"Arrêtés du ministre des affaires sociales du 24 juillet 1996, portant agréments d'avenants à quarante conventions collectives nationales","issued":{"date-parts":[[1996,7,24]]},"container-title":"Journal officiel de la République tunisienne","issue":"60","page":"1606","URL":"https://www.pist.tn/jort/1996/1996F/Jo06096.pdf","note":"* Première mention « Les arrêtés et avenants sont publiés dans l'édition originale arabe »."},
 {"id":"avenant11-textile-2011","type":"legislation","title":"Arrêté du ministre des affaires sociales du 11 octobre 2011, portant agrément de l'avenant n° 11 à la convention collective sectorielle du textile","issued":{"date-parts":[[2011,10,11]]},"container-title":"Journal officiel de la République tunisienne","issue":"78","URL":"https://www.pist.tn/jort/2011/2011F/Jo0782011.pdf","note":"Édition française : avis collectif p. 2170 (plein texte). Grille dans l'édition arabe, p. 2194. Intitulé français reconstitué d'après les visas de 2024."},
 {"id":"avenant10-btp-2011","type":"legislation","title":"Arrêté du ministre des affaires sociales du 14 octobre 2011, portant agrément de l'avenant n° 10 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2011,10,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"81","URL":"https://www.pist.tn/jort/2011/2011F/Jo0812011.pdf","note":"Grille dans l'édition arabe, p. 2442. Intitulé français reconstitué ; page française non relevée."},
 {"id":"avenant12-textile-2013","type":"legislation","title":"Arrêté du ministre des affaires sociales du 19 février 2013, portant agrément de l'avenant n° 12 à la convention collective sectorielle du textile","issued":{"date-parts":[[2013,2,19]]},"container-title":"Journal officiel de la République tunisienne","issue":"16","page":"777","URL":"https://www.pist.tn/jort/2013/2013F/Jo0162013.pdf","note":"Grille dans l'édition arabe, p. 845."},
 {"id":"avenant11-btp-2013","type":"legislation","title":"Arrêté du ministre des affaires sociales du 8 mars 2013, portant agrément de l'avenant n° 11 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2013,3,8]]},"container-title":"Journal officiel de la République tunisienne","issue":"22","page":"985","URL":"https://www.pist.tn/jort/2013/2013F/Jo0222013.pdf","note":"Grille dans l'édition arabe, p. 1043."},
 {"id":"avenants-2014-textile-btp","type":"legislation","title":"Arrêtés du ministre des affaires sociales des 17 et 27 octobre 2014, portant agrément de l'avenant n° 13 à la convention collective sectorielle du textile et de l'avenant n° 12 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2014,10,17]]},"container-title":"Journal officiel de la République tunisienne","issue":"90","page":"2978-2983","URL":"https://www.pist.tn/jort/2014/2014F/Jo0902014.pdf","note":"Deux arrêtés (pp. 2978-2979 et 2982-2983, notices) : à scinder. Grilles dans l'édition arabe, pp. 3100 et 3120."},
 {"id":"avenant14-textile-2016","type":"legislation","title":"Arrêté du ministre des affaires sociales du 8 avril 2016, portant agrément de l'avenant n° 14 à la convention collective sectorielle du textile","issued":{"date-parts":[[2016,4,8]]},"container-title":"Journal officiel de la République tunisienne","issue":"30","page":"1207","URL":"https://www.pist.tn/jort/2016/2016F/Jo0302016.pdf","note":"Page française relevée au plein texte (pied de page), à contrôler. Avenant et grille dans l'édition arabe, pp. 1317-1320."},
 {"id":"avenant13-btp-2016","type":"legislation","title":"Arrêté du ministre des affaires sociales du 2 mai 2016, portant agrément de l'avenant n° 13 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2016,5,2]]},"container-title":"Journal officiel de la République tunisienne","issue":"37","page":"1460-1461","URL":"https://www.pist.tn/jort/2016/2016F/Jo0372016.pdf","note":"Grille dans l'édition arabe, p. 1703."},
 {"id":"avenant15-textile-2017","type":"legislation","title":"Arrêté du ministre des affaires sociales du 14 août 2017, portant agrément de l'avenant n° 15 à la convention collective sectorielle du textile","issued":{"date-parts":[[2017,8,14]]},"container-title":"Journal officiel de la République tunisienne","issue":"66","page":"2667","URL":"https://www.pist.tn/jort/2017/2017F/Jo0662017.pdf","note":"Page française relevée au plein texte (pied de page), à contrôler. Avenant dans l'édition arabe, pp. 2679-2680 ; grilles aux pages suivantes."},
 {"id":"avenant14-btp-2017","type":"legislation","title":"Arrêté du ministre des affaires sociales du 30 août 2017, portant agrément de l'avenant n° 14 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2017,8,30]]},"container-title":"Journal officiel de la République tunisienne","issue":"72","URL":"https://www.pist.tn/jort/2017/2017F/Jo0722017.pdf","note":"Page française non établie (le pied de page relevé au plein texte, 3093, est douteux). Grilles dans l'édition arabe, pp. 3034-3035."},
 {"id":"avenant15-btp-2018","type":"legislation","title":"Arrêté du ministre des affaires sociales du 17 décembre 2018, portant agrément de l'avenant n° 15 à la convention collective sectorielle du bâtiment et des travaux publics","issued":{"date-parts":[[2018,12,17]]},"container-title":"Journal officiel de la République tunisienne","issue":"4","page":"91","URL":"https://www.pist.tn/jort/2019/2019F/Jo0042019.pdf","note":"JORT du 11 janvier 2019. Page française relevée au plein texte, à contrôler. Grilles dans l'édition arabe, pp. 121-122."},
 {"id":"avenant16-textile-2019","type":"legislation","title":"Arrêté du ministre des affaires sociales du 21 janvier 2019, portant agrément de l'avenant n° 16 à la convention collective sectorielle du textile","issued":{"date-parts":[[2019,1,21]]},"container-title":"Journal officiel de la République tunisienne","issue":"11","page":"320","URL":"https://www.pist.tn/jort/2019/2019F/Jo0112019.pdf","note":"JORT du 5 février 2019. Page française relevée au plein texte, à contrôler. Avenant dans l'édition arabe, pp. 385-386 ; grilles aux pages suivantes."},
 {"id":"avenant17-textile-2022","type":"legislation","title":"Arrêté du ministre des affaires sociales du 23 juin 2022, portant agrément de l'avenant n° 17 à la convention collective sectorielle du textile","issued":{"date-parts":[[2022,6,23]]},"container-title":"Journal officiel de la République tunisienne","issue":"71","page":"2002","URL":"https://www.pist.tn/jort/2022/2022F/Jo0712022.pdf","note":"Absent de jort_cache. Page française relevée au plein texte, à contrôler. Avenant et grilles dans l'édition arabe, pp. 2148-2153."},
 {"id":"avenant18-textile-2024","type":"legislation","title":"Arrêté du ministre des affaires sociales du 8 avril 2024, portant agrément de l'avenant n° 18 à la convention collective sectorielle du textile","issued":{"date-parts":[[2024,4,8]]},"container-title":"Journal officiel de la République tunisienne","issue":"49","page":"1257","URL":"https://www.pist.tn/jort/2024/2024F/Jo0492024.pdf","note":"* Avenant signé le 29 février 2024, « publié uniquement en langue arabe » : édition arabe du même numéro, pp. 3503-3512 (grilles pp. 3507-3512)."},
 {"id":"oit-ilostat-couverture-negociation-collective","type":"dataset","title":"Collective bargaining coverage rate (%) — Annual (ILR_CBCT_NOC_RT_A), Tunisia","author":[{"literal":"Organisation internationale du Travail, ILOSTAT"}],"accessed":{"date-parts":[[2026,10,8]]},"URL":"https://sdmx.ilo.org/rest/data/ILO,DF_ILR_CBCT_NOC_RT/TUN..?format=csv","note":"2010-2014 et 2016-2019. Source déclarée : fichiers administratifs. Date d'édition de la base non relevée."},
 {"id":"belgacem-vacher-2023-unemployment","type":"report","title":"Why is Tunisia's unemployment so high? Evidence from policy factors","author":[{"family":"Belgacem","given":"Aymen"},{"family":"Vacher","given":"Jérôme"}],"issued":{"date-parts":[[2023,7]]},"URL":"https://thedocs.worldbank.org/en/doc/4c3928355c0c5808cd1e5c0bb6645ff9-0280032023/original/Draft-WP-Tunisia-unemployment-rate-AB-JV-July-2023-WB-conference.pdf","note":"Version préliminaire portant la mention « Please do not quote or circulate » : chercher la version publiée avant de citer. Rapport extérieur ; ne sert ici qu'au recoupement."}
]
```
`decret2026-68`, `decret73-247`, `arrete-1973-05-29-convention-cadre` : ébauches dans la note du
5 octobre, inchangées. Côté arabe : adresses `A/Ja` (celle du n° 49 de 2024 vérifiée), intitulés
arabes à relever au fascicule.

## Notions à glossaire

| FR | AR | Source canonique pressentie | État |
|---|---|---|---|
| convention collective sectorielle | الاتفاقية المشتركة القطاعية | intitulés des avenants, éd. arabe (n° 49/2024, p. 3503) | existant, provisoire : à confirmer |
| convention collective nationale (intitulé jusqu'en 2002) | الاتفاقية المشتركة القومية | préambule de l'avenant n° 18, même page ; bascule « nationale » → « sectorielle » entre les avenants n° 8 (2002) et n° 9 (2006) | à ajouter comme variante |
| avenant | الملحق التعديلي | id. | **confirmé au journal** (la note du 5 octobre le tenait de l'UGTT) |
| agrément (d'une convention, d'un avenant) | المصادقة | « يتعلق بالمصادقة على الملحق التعديلي », titres arabes 2011-2019 | **confirmé** ; noter que le français dit tantôt « agrément », tantôt « approbation » |
| grille des salaires | جدول الأجور ; شبكات الأجور | « جدول الأجور عدد 1 » (titres des grilles) ; « شبكات الأجور » (avenant n° 18, art. 12) | à ajouter |
| salaire de base | الأجر الأساسي | à relever (non vu en clair dans les pages lues) | à vérifier |
| échelon ; catégorie ; sous-catégorie | الدرجة ; الصنف ; الصنف الفرعي | en-têtes des grilles du textile (image) | à ajouter |
| confirmation (échelon 0), titularisation | الترسيم | grille du textile, 1974 (FR) et 2024 (AR) | à ajouter |
| personnel occasionnel (bâtiment) | العملة العرضيون | titre de la grille n° 1 du bâtiment | à ajouter |
| agents payés à l'heure ; agents payés au mois | الأعوان الخالصون بالساعة ; الأعوان الخالصون بالشهر | titres des grilles du textile, 2014 | à ajouter |
| indemnité de présence | منحة الحضور | avenant n° 18, art. 49 nouveau | à ajouter |
| indemnité de transport | منحة النقل | id. | à ajouter |
| prime d'assiduité | منحة التشجيع على المواظبة | id. | à ajouter (intitulé français à confirmer sur un avenant français antérieur à 1996) |
| indemnité complémentaire provisoire | المنحة التكميلية المؤقتة | nota bene des grilles (FR 1994 ; AR 2014 →) ; décrets n° 81-437 et n° 82-501 | à ajouter |
| sentence arbitrale | القرار التحكيمي | visas de 2024 | à ajouter |
| taux de couverture de la négociation collective | — | ILOSTAT (libellé anglais) | terme d'étude, à ne pas arabiser sans source |

# Volume VII « Les finances locales » : plan

**Option B retenue par l'humain le 4 octobre 2026** : un septième volume, distinct de « La
fiscalité ». Il traite ensemble la fiscalité locale, les transferts de l'État et les budgets des
collectivités, parce que ces trois éléments ne se comprennent que l'un par l'autre. Rien n'est
rédigé : ce plan cadre le travail. Aucune date, aucun texte, aucune valeur n'y est donné comme
établi ; ce qui est marqué « à établir » doit être lu au JORT ou dans une source vérifiée avant
d'entrer dans le précis.

## 1. Principes

- **Frontières avec les autres volumes.**
  - « La fiscalité » garde les impôts d'État ; l'impôt foncier de 2014, assis sur la TIB et la TNB,
    reste au chapitre de l'impôt sur la fortune, avec un renvoi croisé.
  - La TCL est assise sur le chiffre d'affaires : le volume renvoie au chapitre de l'IRPP et à celui
    de l'IS pour les assiettes communes.
  - Les rémunérations du personnel des collectivités relèvent, s'il y a lieu, du volume
    « Rémunérations dans le secteur public ».
- **Conventions des volumes** : chapitres à plat, numérotés par Quarto, sans partie ; l'introduction
  annonce les regroupements (`scripts/check_numerotation.py`). Plan type de chaque dispositif :
  origines → institution → réformes, une à une → longue période et données.
- **Termes** : les notions passent au glossaire bilingue ; termes arabes relevés dans l'édition arabe
  des textes (règle « impôt » de `docs/agents/terminologue.md` : l'impôt garde le nom de son texte).

## 2. Chapitres

| # | Chapitre | Contenu | Sources de départ |
|---|---|---|---|
| 1 | **Présentation** | Ce que sont les collectivités locales (communes, régions, conseils de gouvernorat, selon les textes successifs) ; carte « collectivité × ressources × compétences » ; plan du volume ; frontières avec les autres volumes | AFD 2018, ch. 2 |
| 2 | **Histoire des collectivités et de leurs finances** | Municipalités beylicales et coloniales ; organisation après l'indépendance ; textes fondateurs des communes et des conseils régionaux ; Constitution de 2014 (chapitre du pouvoir local) et code des collectivités locales ; textes postérieurs — tous à établir au JORT | AFD 2018, ch. 2 et 7 ; doctrine (Dafflon et Gilbert) ; JORT |
| 3 | **Compétences et organisation** | Ce que font les collectivités, par délégation ou par dévolution ; agences et organismes publics ; ce que cela coûte | AFD 2018, ch. 4 ; Hammami, Dafflon et Gilbert, PARD 2021 ; note DGCL 2016 |
| 4 | **Budgets et comptes** | Nomenclature, procédure budgétaire, règles d'équilibre, endettement ; tutelle et contrôle | AFD 2018, ch. 3 ; Dafflon, RTF n° 20 (2013) ; Dafflon, « Le budget local » (2021) |
| 5 | **Les impôts sur les immeubles** | Taxe sur les immeubles bâtis (TIB) et taxe sur les terrains non bâtis (TNB) : assiette, prix de référence, taux, exonérations, recouvrement ; réforme par réforme | Code de la fiscalité locale et modificatifs (à établir au JORT) ; manuscrit 2013, ch. 4 ; AFD 2018, ch. 5 ; références foncières en cours de vérification |
| 6 | **Les impôts sur l'activité** | Taxe sur les établissements à caractère industriel, commercial ou professionnel (TCL) : assiette sur le chiffre d'affaires, taux minimaux ; taxe hôtelière ; autres impôts (spectacles, etc.) | Idem ; CNF 2013, groupe « fiscalité locale » |
| 7 | **Taxes, redevances et autonomie fiscale** | Taxes locales (permis de bâtir, etc.) ; redevances et paiements des usagers ; ce que les collectivités peuvent moduler (taux, fourchettes, tarifs) et ce que l'État fixe ; classification des ressources | AFD 2018, ch. 5 ; Dafflon, RTF n° 25 (2017) ; Dafflon et Gilbert, RTF n° 24 (2017) |
| 8 | **Les transferts de l'État** | Fonds commun des collectivités locales (quote-part, critères de répartition) ; transferts sur crédits des ministères ; transferts exceptionnels ; réformes des dotations depuis 2014 ; subventions d'investissement, CPSCL, lien prêt-subvention ; programmes régionaux | AFD 2018, ch. 6 ; manuscrit 2013, ch. 5 ; PARD 2021 et 2022 ; Gilbert, *Transparence et droit* (péréquation) |
| 9 | **La longue période** | Ressources propres et transferts ; rendement de chaque impôt local ; dépenses et investissement ; endettement ; en séries datées, par type de collectivité si les sources le permettent | Voir § 3 |
| A | Annexe : chronologie des textes | — | — |
| B | Annexe : glossaire | — | — |

Les chapitres 5 à 7 suivent la classification du code de la fiscalité locale (impôts, taxes,
redevances), à vérifier sur le code lui-même. Le chapitre 2 se dédouble si la matière d'avant 1956
le justifie.

## 3. Données à construire (tunisia-data)

| Série | Sources à exploiter | État |
|---|---|---|
| Ressources des collectivités : propres / transferts / emprunt | manuscrit 2013, ch. 5 (2010-2012) ; AFD 2018, § 3.7 et 6.7 ; lois de règlement ; CPSCL | à chercher au-delà de 2012 |
| Rendement de la TIB, de la TNB, de la TCL | CNF août 2013 (2010-2012) ; Dafflon, RTF n° 25, annexe (recettes communales 2010-2016, à vérifier sur l'imprimé) ; ancien portail du ministère (collecte en cours) | à reconstituer |
| Quote-part et répartition du FCCL | manuscrit 2013, tableau 5-10 (2006-2012) ; lois de finances | à reconstituer |
| Prêts et subventions de la CPSCL | rapports annuels de la CPSCL (à chercher) | à chercher |
| Prix à la consommation (déflateur) | INS, déjà dans tunisia-data | disponible |

Chaque série reconstruite reçoit sa fiche de provenance, source par source, dans tunisia-data.

## 4. Étapes

1. **Documentation**, chapitre par chapitre : notes documentaires (`docs/notes/finances-locales-*.md`),
   textes lus au JORT, fiches `RECHERCHE` pour ce qui reste introuvable. D'abord le code de la
   fiscalité locale et ses modificatifs (chapitres 5 à 7), puis les textes du FCCL et de la CPSCL
   (chapitre 8), enfin l'histoire (chapitre 2).
2. **Données** : séries du § 3 dans tunisia-data, avec leurs fiches de provenance.
3. **Création du volume** : `precis/fr/finances_locales/`, `build.sh`, CI, page d'accueil (volume VII),
   `_quarto.yml` arabe à la main, collection Zotero, AGENTS.md (sept volumes). Le livre arabe est sauté
   tant que sa traduction n'est pas livrée.
4. **Rédaction**, un chapitre par PR, en commençant par les chapitres 5 et 6 (les plus sourcés),
   puis 8, 4, 3, 2, et la présentation en dernier.
5. **Traduction** à la fin de chaque lot.

## 5. Sources déjà repérées

- **Doctrine** : `docs/notes/biblio-fiscalite-locale.md` — six textes de B. Dafflon et G. Gilbert
  (deux en accès libre) ; leur livre AFD 2018, synthèse de référence, dont les chapitres 2 à 7
  recoupent ce plan ; rapports PARD 2021-2022 ; manuscrits des chapitres 4 et 5 de 2013, hors dépôt
  (`~/Documents/biblio-precis/fiscalite-locale/`), à citer de préférence par leur version publiée.
- **Foncier** : références en cours de vérification
  (`~/Documents/biblio-precis/fiscalite-locale/foncier/`).
- **Ministère des Finances** : documents de la réforme fiscale 2013-2014
  (`docs/notes/reforme-fiscale-2013-2014-inventaire.md`) et collecte en cours sur l'ancien portail.

## 6. Questions ouvertes

- Faut-il un chapitre propre pour les régions et les conseils de gouvernorat, ou les traiter avec
  les communes ?
- Les taxes affectées à des fonds (hors budgets locaux) entrent-elles dans le périmètre ?
- Le titre du volume : « Les finances locales », ou « Les collectivités locales et leurs finances » ?

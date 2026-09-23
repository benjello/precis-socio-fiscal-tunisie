# RSNA : avant 1974, l'état du décret n° 74-499 à l'origine, et les réformes du cœur du régime

> Note **documentaire**, rédigée le 23 septembre 2026 sur la branche `feat/retraites-cnss-rsna`.
> Elle n'écrit pas de prose de précis. Elle n'a modifié aucun `.qmd`, aucun `references.json` ni
> aucun paramètre.
>
> Objet : préparer la réorganisation de la partie « régime des salariés non agricoles » de
> `precis/fr/retraites/_secteur_prive.qmd` sur le modèle du chapitre CNRPS : § « Avant 1985 »,
> « Le régime de la loi n° 85-12 », « Les réformes du cœur du régime ». Elle reprend la forme de
> `cnrps-avant-1985.md`.
>
> Elle **corrige quatre affirmations du chapitre actuel** (§ 6), sur le texte.

## Conventions

**Trois niveaux d'attestation** : **[T]** texte lu au fascicule (à l'image, ou couche texte relue) ;
**[M]** métadonnées `jort_cache.db` seules ; **[D]** dérivé d'un rapprochement ou d'une convention.

**Dates d'entrée en vigueur** (AGENTS.md). Quand le texte énonce une date d'effet, on la reprend.
Sans clause d'effet, on applique deux règles :
- avant 1993, le texte est exécutoire **un jour franc après la publication** (art. 3 nouveau du
  décret du 27 janvier 1883, dans sa rédaction du décret du 13 septembre 1956) ;
- depuis 1993, il est exécutoire **cinq jours après le dépôt au siège du gouvernorat de Tunis**
  (loi n° 93-64, art. 2). La date de dépôt n'est pas connue ici : la date exécutoire reste donc à
  calculer.

Quand un fascicule porte plusieurs dates, la date de publication utilisée est celle de
`jort_cache`. Elle est signalée comme telle, parce que la base diverge parfois du pied de page
(outillage-sources § 3 bis).

**Lecture.** Les fascicules de 1960 à 1988 n'ont pas de couche texte. Ils ont été rendus avec
`pdftoppm` à 250-300 dpi, puis découpés par colonne et lus à l'image ; `tesseract -l fra` n'a servi
qu'au repérage. Deux chiffres illisibles au fascicule français de 1974 ont été tranchés sur
l'**édition arabe** (Ja03074.pdf) : l'article 2 (600 heures) et l'article 44 (8 mois). Le
fascicule n° 46 de 2003 a une police décalée, décodée selon la méthode de outillage-sources § 5.
Les autres fascicules postérieurs à 1994 ont une couche texte. Les images de travail se trouvent
dans `scratchpad/rsna-doc/`, hors dépôt.

**URL.** Le motif est `https://www.pist.tn/jort/<aaaa>/<aaaa>{F|A}/{Jo|Ja}<nnn><aa|aaaa>.pdf`.
Toutes les URL citées ci-dessous ont été contrôlées le 23 septembre 2026 avec `curl -k`, qui a
renvoyé `200 application/pdf` et une taille plausible.

---

## 1. Les textes lus

| Texte | Objet | Signature | JORT (éd. fr.) | Pages fr. | Effet | Niv. |
|---|---|---|---|---|---|---|
| **Loi n° 60-30** | Organisation des régimes de sécurité sociale | 1960-12-14 | n° 57, fasc. 13-16 déc. 1960 | 1602-1613 | **art. 130** : **1er avril 1961**, sauf art. 1 à 33, 119, 124 à 126 et 129, qui sont d'application immédiate | **[T]** art. 130-131 lus à l'image ; art. 2 à 5, 68-69, 119-121 confirmés à l'image le 23 sept. 2026 (§ 10) ; art. 1, 122-126 par OCR non confirmé à l'image |
| **Loi n° 60-33** | Institue le régime de pensions d'invalidité, de vieillesse et de survie et le régime d'allocation de vieillesse et de survie dans le secteur non agricole | 1960-12-14 | n° 57, même fascicule | 1616 | non énoncée | **[T]** (art. 1-4 lus à l'image ; art. 5 confirmé à l'image le 23 sept. 2026, § 10) |
| **Décret n° 71-452** | Prestations *minima* de vieillesse, d'invalidité et de survie, servies à titre transitoire | 1971-12-17 | n° 56 du 21 déc. 1971 | 1700-1702 | **art. 24 : 1er janvier 1972** | **[T]** (intégral) |
| **Décret n° 74-499** | Régime de pensions de vieillesse, d'invalidité et de survivants, secteur non agricole | 1974-04-27 | n° 30, fasc. 30 avril - 3/4 mai 1974 | 915-919 | **art. 64 : 1er janvier 1974** | **[T]** (art. 1-64) |
| Décret n° 74-499, édition arabe | idem | — | Ja n° 30/1974 | vers 1008-1013 (art. 44 à 48 : p. 1012) | — | **[T]** (art. 1-2, 17-31, 43-48) |
| **Arrêté du 4 juillet 1975** | Âge de la retraite des mineurs | 1975-07-04 | n° 47/1975 | 1454 | **art. 2 : 1er janvier 1974** | **[T]** (lu à l'image) |
| **Décret n° 76-981** | Organise la CAVIS ; fusion avec les régimes conventionnels | 1976-11-19 | n° 72 du 23 nov. 1976 | 2867-2869 | non énoncée : exécutoire le **25 novembre 1976** **[D]** | **[T]** art. 25 lu à l'image ; art. 1-3, 23-24, 26-27 par OCR non confirmé à l'image |
| **Décret n° 81-188** | Remplace les art. 21 b), 22 al. 1, 29, 33 et 34 ; complète l'art. 31 | 1981-02-14 | n° 10 du 17 fév. 1981 | 319-320 | non énoncée : exécutoire le **19 février 1981** **[D]** | **[T]** (art. 1er à 34 et art. 2 — art. 31, 2e alinéa — lus à l'image ; § 10) |
| Décret n° 81-187 | Art. 53, 53 bis, 53 ter | 1981-02-14 | n° 10 du 17 fév. 1981 | 319 | art. 3 : 1er mai 1980 (d'après le chapitre) | **[T]** (art. 1) |
| **Décret n° 82-1030** | Art. 15 bis, 17, 22, 39-43, 45, 55 | 1982-07-15 | n° 51, fasc. 20-23 juil. 1982 | 1605-1607 | non énoncée : exécutoire le 22 juillet 1982 (calcul du chapitre, repris) | **[T]** (art. 1-5) |
| **Rectificatif au décret n° 82-1030** | Art. 17, al. 3 | — | n° 66, fasc. 19-22 oct. 1982 | **2197** | — | **[T]** |
| Décret n° 88-1137 | Art. 5 b) : quote-part 4,25/20e | 1988-06-11 | n° 43 du 24 juin 1988 | 942 | art. 2 : 1er janvier 1988 | **[T]** |
| **Décret n° 94-1477** | Abroge le décret n° 76-981 ; transfère les régimes à la CNSS | 1994-07-04 | n° 55 du 15 juil. 1994 | 1193 | non énoncée (règle de 1993) | **[T]** (intégral) |
| Décret n° 97-555 | Art. 9 : taux de cotisation | 1997-03-31 | n° 27 du 4 avril 1997 | 553 | non énoncée | **[T]** |
| Décret n° 2003-1212 | Art. 5 b) : quote-part 7,25/20e | 2003-06-02 | n° 46 du 10 juin 2003 | 1834-1835 | art. 2 : 1er janvier 2003 | **[T]** (texte décodé) |
| **Décret n° 2007-2148** | Art. 15 bis a) et c), 15 ter, 17 § 3, 33, 42, 47 | 2007-08-21 | n° 69 du 28 août 2007 | 3070-3071 | non énoncée (règle de 1993) | **[T]** (intégral) |
| **Arrêté du 11 septembre 2015** | Âge de la retraite des agents mineurs | 2015-09-11 | n° 75 du 18 sept. 2015 | 2234-2235 | non énoncée | **[T]** (art. 1-2) |
| **Arrêté du 22 mai 2023** | Âge de la retraite dans l'assainissement et les déchets | 2023-05-22 | n° 55 du 26 mai 2023 | 1413 | non énoncée | **[T]** (intégral) |

URL (fr / ar), toutes vérifiées :

| Texte | Français | Arabe |
|---|---|---|
| Lois n° 60-30 et 60-33 | `1960/1960F/Jo05760.pdf` | `1960/1960A/Ja05760.pdf` |
| Décret n° 71-452 | `1971/1971F/Jo05671.pdf` | `1971/1971A/Ja05671.pdf` |
| Décret n° 74-499 | `1974/1974F/Jo03074.pdf` | `1974/1974A/Ja03074.pdf` |
| Rectificatif au décret n° 74-499 | `1974/1974F/Jo03974.pdf` | — |
| Arrêté du 4 juillet 1975 | `1975/1975F/Jo04775.pdf` | `1975/1975A/Ja04775.pdf` |
| Décret n° 76-981 | `1976/1976F/Jo07276.pdf` | `1976/1976A/Ja07276.pdf` |
| Rectificatif au décret n° 82-1030 | `1982/1982F/Jo06682.pdf` | `1982/1982A/Ja06682.pdf` |
| Décret n° 94-1477 | `1994/1994F/Jo05594.pdf` | `1994/1994A/Ja05594.pdf` |
| Arrêté du 11 septembre 2015 | `2015/2015F/Jo0752015.pdf` | `2015/2015A/Ja0752015.pdf` |
| Arrêté du 22 mai 2023 | `2023/2023F/Jo0552023.pdf` | `2023/2023A/Ja0552023.pdf` |

Préfixe commun : `https://www.pist.tn/jort/`. Pour les URL arabes de 1960, 1971, 1976, 1982 et
2015, seule l'existence du fichier est vérifiée : la pagination arabe n'en a pas été relevée.

---

## 2. Avant 1974

### 2.1 La loi n° 60-30 ne couvre pas la vieillesse

**Art. 2 [T]** : l'organisation de la sécurité sociale assure aux salariés « un régime de
prestations familiales et un régime d'assurances sociales ». **Art. 68 [T]** : les assurances
sociales comprennent « des indemnités en espèces, en cas de maladie, de maternité ou de décès » et
« l'octroi des soins ». **La vieillesse n'y figure pas.**

La loi règle toutefois les régimes conventionnels :
- **art. 5, 4° [T]** : la Caisse nationale peut « gérer, selon des conventions particulières
  approuvées […], des régimes conventionnels de retraite ou d'entr'aide sociale » ;
- **art. 119 [T]** : les organismes qui couvrent les risques « maladie, décès, maternité et
  vieillesse » doivent déclarer leurs régimes dans les six mois ;
- **art. 120 [T]** : les assurances sociales légales excluent « à due concurrence » les régimes
  conventionnels, qui continuent à assurer la différence à titre complémentaire ;
- **art. 121 [T]** : les organismes dispensés d'affiliation servent eux-mêmes les prestations.

**Art. 130 [T]**, lu à l'image : « La présente loi entre en vigueur le 1er avril 1961, sauf en ce
qui concerne les dispositions prévues par les articles 1 à 33, 119, 124 à 126 et 129, qui sont
d'application immédiate. » Le 1er avril 1961 est la date à partir de laquelle les décrets de 1971
et de 1974 comptent les périodes de cotisation.

### 2.2 La loi n° 60-33, loi-cadre de la vieillesse

**Art. 1 [T]** : « Il est institué, au profit des travailleurs salariés visés à l'article 34 de la
loi n° 60-30 […], un régime de pensions d'invalidité, de vieillesse et de survie, et un régime
d'allocation de vieillesse et de survie. »

- **Art. 2** : la gestion est confiée à la CNSS ; les titres I et III de la loi n° 60-30
  s'appliquent ; les cotisations, à la charge des travailleurs et des employeurs, ont un taux et
  une répartition fixés par décret.
- **Art. 3** : « Les conditions d'ouverture des droits à pension ou à allocation, le mode de calcul
  de ces prestations, ainsi que leur montant, seront déterminés par décret », sur proposition d'une
  commission tripartite (État, employeurs, travailleurs).
- **Art. 4** : contrôle technique et financier des organismes non publics qui couvrent ces risques.
- **Art. 5** : « Un décret prévoira dans quelle mesure ou sous quelle forme les régimes
  conventionnels […] pourront continuer à exister, en dehors du régime général et, en cas de fusion
  totale, les conditions et les modalités de cette fusion. »

**La loi ne fixe donc aucun paramètre.** Âge, stage, taux et montant sont renvoyés au décret. Ce
renvoi explique qu'aucun régime ne fonctionne de 1961 à 1971, et que toutes les réformes du RSNA,
jusqu'à aujourd'hui, se fassent **par décret**. Le décret n° 74-499 s'ouvre sur « En application de
la loi n° 60-33 » (art. 1er) ; son visa cite les propositions de la commission tripartite de
l'article 3.

> La note de la clé `loi60-33` dans `references.json` porte « Métadonnées seules ; texte non lu ».
> Ce n'est plus exact : le texte est lu (**[T]**).

Un arrêté du 29 mars 1961 fixe la composition de la commission consultative (JORT n° 12/1961,
p. 446). Seul son intitulé est connu (**[M]**) ; le décret n° 71-452 le vise.

### 2.3 Le décret n° 71-452 du 17 décembre 1971, premier régime servi

**Le chapitre et la note de la clé `decret74-499` le numérotent « 71-432 ». C'est une erreur :
c'est le décret n° 71-452.** Le numéro 452 est lu dans l'intitulé du décret de 1971 (JORT n° 56,
p. 1700), dans le visa du décret n° 74-499 et dans ses articles 58 et 63. `jort_cache` ne connaît
aucun décret n° 71-432 relatif aux pensions.

C'est un régime **transitoire de prestations *minima*, forfaitaires**, et non encore un régime
contributif proportionnel. **Art. 1 [T]** : « En attendant la mise en application, dans un délai
maximum de deux ans, du régime de pension […] institué par la loi n° 60-33 […], il sera servi, à
titre transitoire, par la CNSS, aux assurés sociaux du secteur non agricole […] des prestations
minima de vieillesse, d'invalidité ou de survie. »

| Règle | Décret n° 71-452 (1er janvier 1972) | Article |
|---|---|---|
| Trimestre validé | période de cotisation effective depuis le 1er avril 1961, pour un salaire trimestriel au moins égal aux **deux tiers** de la rémunération d'un « manœuvre ordinaire du bâtiment et des travaux publics » occupé **600 heures** | art. 2 |
| Périodes assimilées | incapacité temporaire indemnisée (accident du travail) ; rente d'incapacité permanente d'au moins **40 %** ; indemnités journalières de maladie, de longue maladie ou de maternité | art. 2 |
| Âge | **60 ans** | art. 3 a) |
| Stage | **120 mois** de cotisations | art. 3 b) |
| Cessation | pas d'activité assujettie aux assurances sociales | art. 3 c) |
| Stage transitoire | **80 mois** depuis le 1er avril 1961, majorés de **8 mois** par an à partir du 1er janvier 1973 jusqu'à 120 mois | art. 4 |
| **Montant** | forfait annuel égal à **60 %** de la rémunération légale globale d'un manœuvre du BTP occupé **2 400 heures** par an, arrondi au demi-dinar supérieur. Il n'y a **ni salaire de référence, ni taux croissant avec la durée** | art. 5 |
| Invalidité | incapacité **absolue**, présumée permanente, d'origine non professionnelle ; moins de 60 ans ; stage de **60 mois**, dont 6 au cours des 12 mois précédant la première constatation ; montant égal à celui de l'art. 5 ; conversion en vieillesse à 60 ans | art. 6-10 |
| Veuve | **50 %** ; conditions : **45 ans** ou invalidité, à charge du défunt, mariage depuis **2 ans** (sauf enfant) ; suppression au remariage | art. 11-12 |
| Orphelin | **20 %**, porté à **30 %** pour l'orphelin de père et de mère ; cumul des survivants limité à la prestation de l'assuré | art. 13 |
| Cumul vieillesse et survivant | interdit, seule la plus élevée est servie | art. 16 |
| Régimes conventionnels | cumul autorisé avec leurs prestations | art. 21 |
| Entreprises dispensées (art. 121 de la loi n° 60-30) | servent les *minima*, sauf régime plus favorable | art. 22 |
| Financement | excédents annuels de la CNSS pendant la période transitoire, puis cotisations des employeurs et des salariés | art. 20 |
| Effet | **1er janvier 1972** | art. 24 |

### 2.4 Le passage de 1971 à 1974

Le **décret n° 74-499, art. 58 [T]** : « Les prestations allouées sur le fondement du décret
n° 71-452 […] feront l'objet sans effet rétroactif, d'une nouvelle liquidation suivant les
modalités de calcul prévues par le présent décret. » Cette nouvelle liquidation ne doit pas porter
atteinte aux droits acquis. L'**art. 63 [T]** abroge le décret n° 71-452.

Les deux stages transitoires se raccordent exactement **[D]** : 80 mois au 1er janvier 1972, plus
8 mois au 1er janvier 1973, plus 8 mois au 1er janvier 1974, donnent **96 mois**, le chiffre de
l'art. 44 du décret n° 74-499 (§ 3.2). On atteint 120 mois au 1er janvier 1977.

### 2.5 Les régimes conventionnels et la CAVIS

| Date | Texte | Ce qui se passe | Niv. |
|---|---|---|---|
| 1er janv. 1974 | décret n° 74-499, **art. 59-62** (section 9) | « à titre provisoire et jusqu'à l'intervention des mesures […] de survie ou de fusion des régimes conventionnels, prévus par l'article 5 de la loi n° 60-33 », des règles de coordination s'appliquent. L'introduction du régime légal n'éteint pas les régimes conventionnels gérés en **contrat groupe** dont les avantages sont « au moins équivalents » et assortis du minimum de l'art. 45 (art. 60). Employeurs et salariés disposent d'un **droit d'option** de trois mois pour rester au régime conventionnel, avec dispense de la cotisation légale ; à défaut, ils adhèrent de façon irrévocable au régime légal (art. 61-62). Si le contrat groupe est résilié, la CNSS reprend les droits acquis et les pensions en cours (art. 62 b) | **[T]** |
| 25 nov. 1976 | **décret n° 76-981**, art. 1-2 | « La fusion du régime légal de pensions […] institué […] par le décret n° 74-499 […] avec les régimes conventionnels du même ordre est réalisée en application de l'article 5 de la loi n° 60-33. » La gestion du régime unique est confiée à une caisse autonome créée dans le cadre de la CNSS : la **CAVIS**, seule chargée du régime légal, habilitée aussi à gérer des régimes conventionnels à titre principal ou complémentaire | **[T]** |
| idem | décret n° 76-981, **art. 25** | **abroge les art. 59 à 62 du décret n° 74-499**. Les organismes qui gèrent des régimes conventionnels faisant « double emploi » avec le régime légal **transfèrent à la CAVIS** les dossiers et l'actif, réserves comprises. Les dossiers qui dépassent le régime légal passent à la CAVIS « à titre de régime complémentaire ». Les droits acquis sont intégralement maintenus : ceux du conventionnel sont reconvertis en droits du régime légal et, le cas échéant, du régime complémentaire | **[T]** |
| idem | décret n° 76-981, **art. 24** | la CNSS assure pour le compte de la CAVIS le recouvrement, le contrôle et le service des prestations | **[T]** |
| 1978 | décret n° 78-962 (JORT n° 76/1978, p. 3184-3185 ; rectificatif n° 1/1979, p. 38) | modifie le décret n° 76-981 | **[M]** |
| 1979 | décret n° 79-536, art. 1 (art. 45 al. 2) | pension minimale étendue aux pensions des « régimes conventionnels antérieurs au décret n° 76-981 » (d'après le chapitre) | — |
| 1er mai 1980 | décret n° 81-187, **art. 53 ter** | la revalorisation automatique s'applique aux « régimes conventionnels […] transférés à la CAVIS dans le cadre de la fusion prévue par l'article 25 du décret n° 76-981 » | **[T]** |
| 1989 | décret n° 89-268 (JORT n° 12/1989, p. 270-271) | complète le décret n° 76-981 | **[M]** |
| 1994 | **décret n° 94-1477** | le JORT l'imprime sous l'intitulé « *Projet de* décret n° 94-1477 ». **Art. 1** : abroge le décret n° 76-981. **Art. 2** : transfère à la **CNSS** « tous les régimes légaux d'assurance vieillesse invalidité et survie ainsi que les régimes de retraite conventionnels faisant double emploi » avec le décret n° 74-499, passif, actif et réserves compris. **Art. 3** : la CNSS gère les régimes de la loi n° 81-6 et des décrets n° 74-499, 82-1359, 82-1360 et 89-107. **Art. 4** : elle peut gérer des régimes conventionnels, principaux ou complémentaires, fixés par arrêté. **Art. 5** : les droits acquis sont maintenus et reconvertis. Il n'a pas de clause d'effet | **[T]** |

**En résumé : la CAVIS a existé de la fin de 1976 à 1994.** Le texte en fait une « caisse
autonome créée dans le cadre de la Caisse nationale de sécurité sociale » (art. 1) ; qu'elle n'ait
pas eu de personnalité distincte est une inférence **[D]**, que le texte ne dit pas. La date exacte de sa
disparition dépend du dépôt du JORT n° 55/1994 au gouvernorat de Tunis, qui n'est pas établi.

---

## 3. Le décret n° 74-499 à son entrée en vigueur (1er janvier 1974), d'un seul tenant

Toutes les références de cette section renvoient au JORT n° 30/1974, p. 915-919, lu à l'image
**[T]**.

### 3.1 Champ, validation, financement

- **Art. 1** : pris « en application de la loi n° 60-33 » ; il fixe le taux des cotisations et les
  conditions d'ouverture des droits.
- **Art. 2** : un trimestre compte depuis le 1er avril 1961 si le salaire du trimestre atteint au
  moins les **deux tiers** de la rémunération d'un bénéficiaire du SMIG occupé **600 heures**. Le
  chiffre est illisible au fascicule français (500 ou 600) ; il est net dans l'édition arabe
  (« 600 ساعة ») et c'est celui du décret de 1971. En 1971, la référence était le manœuvre du BTP ;
  en 1974, c'est le SMIG.
- Périodes assimilées : a) incapacité temporaire au titre des accidents du travail ; b) rente
  d'incapacité permanente d'au moins **66,66 %** (40 % en 1971) ; c) indemnités journalières de
  maladie, de longue maladie ou de maternité ; d) périodes de pension d'invalidité.
- **Art. 3** : validation des périodes non déclarées depuis le 1er avril 1961, contre versement des
  cotisations arriérées.
- **Art. 4** : extension ultérieure, par décret, aux travailleurs indépendants.
- **Art. 5 b)** : quote-part de **1,25/20e** de la masse des cotisations de la loi n° 60-30.
- **Art. 9** : cotisation de **3,75 %** (2,5 % à la charge de l'employeur, 1,25 % à celle du
  travailleur) sur les gains de l'art. 42 de la loi n° 60-30. Ce point relève du livre
  « Cotisations sociales ».
- **Art. 8** : période d'équilibre initiale de dix ans. **Art. 13** : analyse actuarielle tous les
  cinq ans au moins.

### 3.2 Âge et stage

- **Art. 14** : l'acquisition du droit oblige à mettre fin à la relation de travail. L'accord des
  parties, homologué par l'inspection du travail, peut différer l'acquisition du droit.
- **Art. 15** : a) **60 ans** ; b) **120 mois** de cotisations effectives ou assimilées ; c) aucune
  activité assujettie. L'âge peut être **réduit à 55 ans** pour les travaux pénibles ou insalubres,
  par arrêté du ministre des affaires sociales (§ 5).
- **Art. 16** : pour ceux qui bénéficient de cette dérogation, les périodes cotisées à 55 ans sont
  majorées des **deux tiers** du nombre de mois restant à courir jusqu'à 60 ans. Si l'assuré
  continue à travailler après 55 ans, le point de départ de la majoration est reporté.
- **Art. 44 (transitoire)** : sont réputés remplir le stage ceux qui justifient de **96 mois**
  depuis le 1er avril 1961. Cette durée est « majorée de **8** mois d'année en année, dès le
  premier janvier 1975 », jusqu'à 120 mois. **Le chapitre dit « six mois » : c'est faux (§ 6,
  écart 2).**

### 3.3 La formule

**Art. 17** : « Le taux de la pension de vieillesse est fixé à **40 %** du salaire moyen de
référence […] lorsque se trouve réalisée la condition de 120 mois de cotisation. Toute fraction de
cotisation supérieure à 120 mois ouvre droit **par période de 12 mois** de cotisation
supplémentaire à une majoration égale à **2 %** […] sans que le montant total de la pension puisse
excéder un maximum de **80 %** dudit salaire. » Le taux est confirmé par l'édition arabe.

**Art. 18** : la pension se calcule sur les salaires soumis à cotisation des **trois ou cinq
dernières années** précédant l'âge d'ouverture du droit, la plus avantageuse des deux périodes
étant retenue. Ces salaires ne comptent, pour chaque année, que « dans la limite de **six fois le
SMIG** rapporté à une durée d'occupation annuelle de **2 400 heures** ».

**Art. 19** : on prend les 36 ou 60 mois écoulés à la date du 1er janvier de l'année où l'assuré
remplit la condition d'âge, ou cesse son activité. Le salaire mensuel moyen vaut 1/36 ou 1/60 du
total, augmenté des salaires moyens ayant servi aux prestations des périodes assimilées.

Formule **[D]**, qui transcrit les articles 17 à 19 :

$$P = \min\big(40\,\% + 2\,\%\cdot\lfloor (m-120)/12 \rfloor,\ 80\,\%\big)\cdot \bar S, \quad m \ge 120$$

où $\bar S$ est le salaire moyen de 36 ou 60 mois, chaque année étant plafonnée à 6 × SMIG ×
2 400 h. Par le calcul, le taux atteint 80 % à 360 mois. La majoration se compte par tranches
entières de 12 mois ; le trimestre n'apparaît qu'en 1982.

### 3.4 Planchers et carrières courtes

**Art. 45 al. 1** : « Le taux annuel des pensions de vieillesse ou d'invalidité ne peut être
inférieur aux **2/3 du SMIG** rapporté à une durée d'occupation annuelle de 2400 heures. »
L'alinéa 2 écarte ce plancher pour l'allocation de vieillesse.

L'**allocation de vieillesse** (section 6, art. 39 à 43) :
- elle est ouverte à qui a l'âge et a cessé son activité sans remplir le stage (art. 39, dont le
  renvoi à l'« article 16 » est corrigé en « 15 » par le rectificatif) ;
- il faut **60 mois** effectifs au moins (art. 40) ;
- c'est un **capital** égal à une mensualité de la pension théorique par période de six mois
  (art. 41) ;
- elle se prescrit par un an (art. 42) ;
- elle peut être convertie en **rente viagère** au tarif de l'arrêté du 17 avril 1958 (art. 43).

En deçà de 60 mois, le texte de 1974 ne prévoit rien.

### 3.5 Revalorisation

**Art. 53** : « Le montant des pensions en cours de paiement sera révisé en cas de hausse sensible
du niveau général des salaires. La date et les modalités de cette révision sont déterminées par
décret. » Aucune indexation automatique.

### 3.6 Droits dérivés (art. 29 à 38)

| Règle | 1974 | Article |
|---|---|---|
| Bénéficiaires | la veuve d'un pensionné de vieillesse ou d'invalidité, ou d'un assuré qui remplit le stage de vieillesse ou d'invalidité ; le veuf invalide | art. 29 |
| Antériorité du mariage | mariage contracté « antérieurement à la réalisation de l'éventualité » | art. 30 |
| Taux | **50 %** de la pension ; partage égal entre les veuves | art. 31 |
| Remariage | suppression au premier jour du trimestre civil suivant | art. 32 |
| Orphelin mineur, limite d'âge | 16 ans ; 21 ans pour l'enseignement du second degré ou supérieur, technique ou professionnel ; sans limite en cas d'infirmité | art. 33 |
| Orphelin, taux | **20 %** ; **30 %** pour l'orphelin de père et de mère (le chiffre est à la limite de la lisibilité, voir le callout du chapitre) | art. 34 |
| Plafond | le total des pensions de veuves et d'orphelins ne dépasse pas la pension de référence du mari ; les pensions d'orphelins sont réduites temporairement | art. 38 |
| Cumul avec l'invalidité | interdit, seule la plus élevée est servie | art. 52 |

Comparaison avec 1971 **[D]** : la condition d'âge de la veuve (45 ans) et la condition de mariage
depuis deux ans disparaissent en 1974.

### 3.7 Invalidité (art. 20 à 28)

- **Art. 20** : l'invalidité est d'origine non professionnelle et réduit **des deux tiers** au moins
  la capacité de travail ou de gain. En 1971, il fallait une incapacité absolue.
- **Art. 21** : a) ne pas avoir l'âge de la vieillesse ; b) « un stage au moins égal à **60 mois**
  de cotisations **dont 6 au cours des 12 mois** précédant la première constatation ». Pas de
  stage en cas d'accident non professionnel si l'immatriculation est antérieure.
- **Art. 22** : **40 %** du salaire moyen de référence avec 60 mois de cotisation (al. 1), plus
  « par période de 12 mois de cotisation supplémentaire [au-delà de 120 mois] une majoration égale
  à **2 %** […] maximum de **80 %** » (al. 2). **Le chapitre omet cet alinéa 2 de 1974.**
- **Art. 23** : bonification de 20 % pour l'assistance d'une tierce personne.
- **Art. 24** : conversion en pension de vieillesse, bonification conservée.
- **Art. 25** : contrôle annuel ; pas de révision après 55 ans.
- **Art. 28** : cumul avec une rente d'accident du travail : réduction de la moitié de la rente,
  dans la limite de la moitié de la pension.

### 3.8 Liquidation et service

- **Art. 46 al. 1** : la demande est présentée « dans le délai d'**un an** à partir du jour où le
  bénéficiaire a atteint l'âge […] et a cessé son activité », a été déclaré invalide ou est décédé.
  Une demande tardive fait perdre les arrérages antérieurs. **Cela ferme le TODO du chapitre sur
  l'ancienne rédaction de l'art. 46** : le délai passe d'un an à cinq ans avec le décret n° 96-326.
- **Art. 47 al. 1** : jouissance au 1er jour du mois qui suit la cessation d'activité, la
  reconnaissance de l'invalidité ou le décès.
- **Art. 49** : condition de résidence, levée par convention de réciprocité.
- **Art. 50** : pension temporaire de 80 % à l'épouse et aux enfants en cas d'abandon de famille.
- **Art. 54** : soins gratuits. **Art. 55** : allocations familiales maintenues.

### 3.9 Contrôle des affirmations du chapitre sur 1974

| Affirmation du chapitre | Verdict |
|---|---|
| 60 ans, 120 mois, cessation d'activité (art. 15) | exact |
| 55 ans pour les travaux pénibles, stage majoré des 2/3 (art. 15-16) | exact |
| Stage transitoire de 96 mois « majoré de six mois par an » (art. 44) | **faux : 8 mois** (§ 6, écart 2) |
| 40 % + 2 % par 12 mois, plafond de 80 % (art. 17) | exact |
| 3 ou 5 dernières années, 6 × SMIG × 2 400 h (art. 18-19) | exact |
| 2/3 du SMIG (art. 45) | exact |
| Allocation en capital, 60 mois (art. 39-43) | exact |
| Révision discrétionnaire (art. 53) | exact |
| Réversion de 50 %, orphelin à 20/30 %, âges 16/21 (art. 31, 33, 34) | exact |
| Invalidité à 40 % en 1974 | exact, mais l'al. 2 (majoration de 2 %/an, plafond de 80 %) est omis |
| Abroge le « décret n° 71-432 » | **faux : 71-452** (§ 6, écart 1) |

---

## 4. Les réformes du cœur du régime (formule et âge)

### 4.1 Recensement exhaustif des modificatifs du décret n° 74-499, 1974-2026

Le recensement a été fait par **trois voies** dans `jort_cache.db` (78 953 textes, dernière
publication indexée : **10 avril 2026**) :

1. `LIKE` sans accents sur `titre` : « 74-499 », « vieillesse,invalidite », « pension(s) de
   vieillesse », « secteur non agricole », « securite sociale » ;
2. FTS `"74-499" OR "74 499"`, puis `(retraite OR pension OR vieillesse) AND (securite OR sociale
   OR prive OR CNSS)` et `(age OR retraite OR admission) AND (…)` après 2007 ;
3. `LIKE` sur les intitulés arabes après 2007 (« التقاعد », « الشيخوخة », « الضمان الاجتماعي »,
   « 499 … 1974 ») ; liste de tous les décrets du ministère des affaires sociales de 2023 à 2026.

Seize textes modifient le décret n° 74-499. **Trois d'entre eux manquent au tableau
`tbl-rsna-textes` du chapitre** : 88-1137, 97-555 et 2003-1212. Tous trois ne touchent qu'au
financement :

| Texte | Effet | Article | Avant → après | Livre |
|---|---|---|---|---|
| 79-536 | 1er janv. 1979 | 45 al. 2 ; 54 ; 55 al. 1 | voir chapitre | Retraites |
| 81-187 | 1er mai 1980 | 53, 53 bis, 53 ter | révision par décret → revalorisation automatique à chaque hausse du SMIG | Retraites (**cœur**) |
| 81-188 | 19 févr. 1981 **[D]** | 21 b) ; 22 al. 1 ; 29 ; 31 al. 2 ; 33 ; 34 | voir 4.2 | Retraites |
| 82-1030 + rectificatif | 22 juil. 1982 | 15 bis ; 17 al. 2-3 ; 22 al. 2 ; 39-43 ; 45 al. 1 ; 55 | voir 4.2 | Retraites (**cœur**) |
| **88-1137** | **1er janv. 1988** (art. 2) | 5 b) | 1,25/20e (ou palier intermédiaire non lu) → **4,25/20e** | Cotisations |
| 90-1455 | 23 sept. 1990 | 3, 14, 18, 30, 32, 43, 54 | fenêtre de 3/5 ans → 10 ans | Retraites (**cœur**) |
| 94-1429 | 1er juil. 1994 et suivants | 5 b), 9, 18, 19 | 10 ans → 5/7/10 ans, 1994-1996 | Retraites (**cœur**) et Cotisations |
| 96-326 | règle de 1993 | 46 al. 1 | délai de demande : **1 an → 5 ans** | Retraites |
| 97-291 | règle de 1993 | 29, 38, 53 al. 4 ; abroge 52 | voir chapitre | Retraites |
| **97-555** | règle de 1993 (JORT du 4 avril 1997) | 9 | → **5,25 %**, dont **2,50 %** à la charge des employeurs et **2,75 %** à celle des travailleurs | Cotisations |
| 97-1927 | 1er mai 1997 | 33 | voir chapitre | Retraites |
| 2001-779 | 1er janv. 2001 | 53 | majoration en somme → en pourcentage | Retraites (**cœur**) |
| **2003-1212** | **1er janv. 2003** (art. 2) | 5 b) | → **7,25/20e** | Cotisations |
| 2007-2148 | règle de 1993 (JORT du 28 août 2007) | 15 bis a) et c) ; 15 ter ; 17 § 3 ; 33 ; 42 ; 47 | voir 4.2 | Retraites (**cœur**) |

Sur 97-555 : le chapitre écrit que le décret n° 94-1429 fixe le taux de l'art. 9 à 5,75 % et fait
monter la part salariale à 3,25 % en 1997. Le décret n° 97-555, du 31 mars 1997, **abroge et
remplace** cet article 9 par 5,25 %, dont 2,75 % à la charge des travailleurs. **À confronter dans
le livre « Cotisations sociales »** avant d'écrire la série.

### 4.2 Contrôle des réformes déjà citées par le chapitre

**Décret n° 81-188 [T]** (p. 320, art. 1-3).
- **Art. 21 b) (nouveau)** : « avoir accompli un stage au moins égal à 60 mois de cotisations ».
  **La condition « dont 6 au cours des 12 mois » disparaît.** Le chapitre dit l'inverse : il
  présente les 6 mois sur 12 comme l'apport de 1981, alors qu'ils étaient dans le texte de 1974
  (§ 6, écart 3).
- **Art. 22 al. 1** : invalidité portée de **40 à 50 %**. Exact.
- **Art. 29 (nouveau)** : la veuve d'un pensionné de vieillesse, ou d'un assuré qui remplit le
  stage de vieillesse, a droit à la réversion ; le veuf invalide aussi. Le même droit est ouvert à
  la veuve d'un pensionné d'invalidité, ou d'un assuré décédé **avant l'âge normal de la
  retraite** qui remplissait les conditions de l'art. 21. Cela ferme le TODO « art. 29 ».
- **Art. 33 (nouveau)** : les âges de 1974 (16 ans, 21 ans, sans limite) sont repris. Le droit est
  étendu aux orphelins d'un pensionné d'invalidité ou d'un assuré décédé avant l'âge normal qui
  remplissait l'art. 21. Cela ferme le TODO « art. 33 de 1981 ».
- **Art. 34** : orphelin à **30 %** dans tous les cas. Exact.
- **Art. 31 al. 2** : réversion jusqu'à **75 %**. Exact.
- **Art. 3** : clause d'exécution, sans date d'effet.

**Décret n° 82-1030 [T]** (p. 1605-1606).
- Art. 1 (art. 15 bis) : les quatre cas, la jouissance à 50 ans, les 360 mois et les 180 mois sont
  exacts.
- Art. 4 (art. 17 al. 2 et 22 al. 2) : 0,5 % par trimestre, plafond de 80 % ; pour l'invalidité,
  au-delà de 180 mois. Exact.
- Art. 3 (section 6) : pension proportionnelle et versement unique en deçà de 60 mois. Exact.
- Art. 5 (art. 45 al. 1 : 2/3 et 1/2 du SMIG ; art. 55). Exact.
- **Art. 17 al. 3 : voir le rectificatif ci-dessous.**

**Rectificatif au décret n° 82-1030 [T]** (JORT n° 66, 19-22 octobre 1982, p. 2197), lu à
l'image : « Article 17, alinéa 3 (nouveau) : à la dernière ligne. Au lieu de : *lors du départ à la
retraite et l'âge de 60 ans.* Lire : *lors du départ à la retraite et l'âge normal de celle-ci.* »
**Le rectificatif ne porte que sur ce point.** Cela lève la réserve du callout du chapitre, mais
contredit le chapitre sur le rôle de 2007 (§ 6, écart 4).

**Décret n° 2007-2148 [T]** (p. 3070-3071).
- **Art. 1** : abroge le tiret c) de l'art. 15 bis.
- **Art. 2** : remplace l'art. 15 bis a), l'art. 17 § 3, et les art. 33, 42 et 47.
- **Art. 3** : ajoute l'art. 15 ter : droit « sans condition d'âge avec jouissance différée de la
  pension jusqu'à l'âge de **cinquante cinq ans** » pour convenance personnelle, avec 360 mois.
- **Art. 17 § 3 (nouveau)** : réduction de 0,5 % par trimestre « entre leur âge lors du départ à la
  retraite et l'âge normal de celle-ci », pour les départs de l'art. 15 ter. **La seule différence
  avec 1982 rectifié est le renvoi, de l'art. 15 bis c) à l'art. 15 ter.**
- **Art. 15 bis a) (nouveau)** : licenciement pour raisons économiques, sans possibilité de
  reprendre une activité assujettie, après la période d'inscription au bureau de l'emploi.
  L'article renvoie à « l'âge visée à l'article 15 ». Le licenciement doit être approuvé par la
  commission de contrôle des licenciements (art. 21 du code du travail), avec une inscription de
  **6 mois** sans offre de travail. **La substance de 1982 est inchangée ; la rédaction est
  reformulée.** Cela ferme le TODO « tiret a) ».
- **Art. 47 (nouveau)** : la jouissance court « à partir du premier jour du mois qui suit celui au
  cours duquel l'assuré ait rempli les conditions d'ouverture du droit ». En 1974, c'était le mois
  qui suit **la cessation d'activité**, la reconnaissance de l'invalidité ou le décès. Cela ferme le
  TODO « art. 47 ».
- Art. 33 et 42 : conformes au chapitre.

Les décrets n° **90-1455, 94-1429, 96-326, 97-1927 et 2001-779** n'ont pas été rouverts ici ; le décret n° **97-291** l'a été le 23 septembre 2026 (§ 10).
Le chapitre en expose la teneur « lu au texte » ; rien dans les textes lus pour cette note ne la
contredit.

### 4.3 Après 1996 : aucun relèvement de l'âge légal

- **Aucun texte publié au JORT ne modifie l'âge légal de 60 ans, le taux de 40 % + 0,5 % par
  trimestre, le salaire de référence ni le minimum depuis 2007.** Les trois voies du § 4.1 ne
  donnent **aucun modificatif du décret n° 74-499 après le décret n° 2007-2148**, jusqu'au
  10 avril 2026 (**[M]**, contrôlé par trois requêtes indépendantes).
- La **loi n° 2019-37** ne vaut que pour le secteur public. Le directeur général de la sécurité
  sociale l'a dit publiquement ([Babnet](https://www.babnet.net/cadredetail-182848.asp), presse).
- **Un projet de décret a été annoncé, jamais trouvé publié** (presse uniquement, à ne pas citer
  comme droit) :
  - décembre 2023 : un relèvement à 62 ans, **optionnel** et soumis à l'accord de l'employeur, est
    annoncé ([Réalités, 5 déc. 2023](https://realites.com.tn/fr/la-retraite-a-62-ans-dans-le-secteur-prive-ce-que-lon-sait/)) ;
  - mai 2024 : le ministre des affaires sociales annonce la parution « dans les tous prochains
    jours » d'un décret « portant prolongement de l'âge de la retraite dans le secteur privé »,
    avec prolongation possible jusqu'à 65 ans sur accord de l'employeur et « effet rétroactif, à
    compter de janvier 2024 » ([Webdo, 2 mai 2024](https://www.webdo.tn/fr/actualite/national/tunisie-la-retraite-a-62-ans-dans-le-secteur-prive-un-decret-bientot-publie/213913/)) ;
  - le même projet porterait de 50 à 55 ans l'âge minimum de départ pour raisons économiques ou
    techniques (d'après le résumé d'un moteur de recherche, source primaire non ouverte) ;
  - le 11 novembre 2025, l'âge légal du privé reste présenté comme 60 ans ([Business News](https://businessnews.com.tn/2025/11/11/age-duree-de-service-regime-laamouri-detaille-les-regles-de-depart-a-la-retraite-dans-les-secteurs-public-et-prive/1372142/)).
- **Les seules règles d'âge prises après 1996 sont des arrêtés d'application de l'art. 15**, qui
  abaissent l'âge à 55 ans pour certaines catégories (§ 5).
- **Programme de départ anticipé 2022-2024** (LF 2022, art. 14, prolongé par la LF 2025, art. 14) :
  il vise la fonction publique. Rien, dans les intitulés, ne l'étend au RSNA.

### 4.4 Liste proposée des réformes du « cœur du régime »

Le critère est celui du chapitre CNRPS : âge, conditions de départ, formule et coût de la
revalorisation.

| Année | Texte | Ce qui change dans le cœur | Date d'effet |
|---|---|---|---|
| 1980-1981 | **81-187** | revalorisation automatique indexée sur le SMIG, en montant (art. 53) | 1er mai 1980 (art. 3) |
| 1982 | **82-1030** + rectificatif | départs anticipés (15 bis) ; majoration de 2 %/an → 0,5 %/trimestre ; **décote de 0,5 %/trimestre jusqu'à « l'âge normal »** ; pension proportionnelle au lieu du capital ; deux minima (2/3 et 1/2 du SMIG) | 22 juillet 1982 **[D]** |
| 1990 | **90-1455** | fenêtre de référence de 3/5 ans → 10 ans, salaires actualisés | 23 septembre 1990 **[D]** |
| 1994-1996 | **94-1429** | fenêtre de 5, 7 puis 10 ans ; moyenne sur 60, 84 puis 120 mois ; limite de 6 × SMIG « régime 48 heures » ; hausse parallèle de la cotisation | 1er juillet 1994, 1995, 1996 (calendrier de l'article) |
| 2001 | **2001-779** | revalorisation en pourcentage de la hausse du SMIG | 1er janvier 2001 (art. 2) |
| 2007 | **2007-2148** | convenance personnelle : jouissance de 50 → **55 ans** (15 ter) ; jouissance au mois qui suit l'ouverture du droit (art. 47) | règle de 1993, JORT du 28 août 2007 |

Réformes **périphériques** (droits dérivés, invalidité, procédure) : 79-536, 81-188, 96-326,
97-291 et 97-1927. **Financement** : 88-1137, 97-555, 2003-1212 et l'art. 9 de 94-1429.
**Pas de réforme de l'âge légal ni du taux** : c'est le trait saillant à opposer au secteur public.

---

## 5. Les catégories à 55 ans (art. 15 al. 2) — TODO du chapitre, partiellement fermé

| Arrêté | Catégorie | Condition | Effet | Niv. |
|---|---|---|---|---|
| **4 juillet 1975** (JORT n° 47/1975, p. 1454) | « L'âge de la retraite tel qu'il est prévu aux articles 14 et 15 du décret […] n° 74-499 […] est fixé à **55 ans** pour les mineurs » | — | **art. 2 : « à compter du 1er janvier 1974 »** (rétroactif) | **[T]** (lu à l'image) |
| **11 septembre 2015** (JORT n° 75/2015, p. 2234-2235) | « agents mineurs » en rapport direct avec l'activité minière, en application des art. 15 et 16 : **55 ans** | **5 ans** dans les mines, carrières ou laveries, ou **10 ans** dans les services techniques qui les fréquentent ; cadres supérieurs techniques exclus ; liste annexée | non énoncé | **[T]** (art. 1-2) |
| **22 mai 2023** (JORT n° 55/2023, p. 1413) | agents des entreprises affiliées à la CNSS dans l'assainissement, le nettoyage des voies, les ordures et les déchets solides et liquides : **55 ans** | **10 ans** de service ; personnel des sièges sociaux exclu ; liste annexée ; l'employeur porte le poste et l'ancienneté sur la fiche de carrière, la CNSS vérifie | non énoncé | **[T]** |

À ne pas confondre avec le décret n° 85-1177 (tâches pénibles et insalubres des ouvriers de l'État,
art. 27 de la loi n° 85-12), modifié par le décret gouvernemental n° 2021-474. Il concerne la
CNRPS, non la CNSS.

---

## 6. Écarts avec le chapitre actuel, à corriger par le rédacteur

1. **« décret n° 71-432 » → « décret n° 71-452 »** : ligne 38 du chapitre, et note de la clé
   `decret74-499` dans `precis/fr/references.json` (et `ar`). Le chiffre est lu quatre fois au
   fascicule.
2. **Art. 44 : le stage transitoire est majoré de 8 mois par an, et non de six.** Le chiffre est net
   dans l'édition arabe (« 8 اشهر », p. 1012) et cohérent avec le décret de 1971 (80 + 8 + 8 = 96).
   Le fascicule français est ambigu. Par le calcul, on atteint 120 mois au 1er janvier 1977.
3. **Décret n° 81-188, art. 21 b)** : il **supprime** la condition « dont 6 au cours des 12 mois »,
   présente en 1974. Le texte de 1981 est lu à l'image (p. 320) : « avoir accompli un stage au
   moins égal à 60 mois de cotisations. » Il faut corriger le tableau `tbl-rsna-textes` (ligne 47) et le § « L'invalidité »
   (ligne 327).
4. **Décote « jusqu'à l'âge normal » : elle date du rectificatif de 1982, non de 2007.** Il faut
   corriger :
   - la ligne 70 du tableau `tbl-rsna-textes` ;
   - les lignes « c) Convenance personnelle, de 1982 à 2007 » et « depuis 2007 » du tableau
     `tbl-rsna-anticipes` ;
   - le callout « Un rectificatif reste à confronter » : le rectificatif est désormais lu, et il ne
     change que ce point.

   En 2007, seul le renvoi change (15 bis c) → 15 ter).
5. Invalidité de 1974 : ajouter l'**al. 2 de l'art. 22** (+2 % par 12 mois au-delà de 120 mois,
   plafond de 80 %), que 82-1030 remplace par +0,5 % par trimestre au-delà de 180 mois.
6. La phrase « aucun modificatif du décret postérieur au décret n° 2007-2148 n'a été retrouvé
   jusqu'en avril 2026 » est **confirmée** par trois voies. Il faut ajouter au tableau les trois
   modificatifs financiers omis (88-1137, 97-555, 2003-1212), ou dire qu'ils relèvent des
   cotisations.
7. Plusieurs TODO sont fermés par cette note :
   - art. 29 et 33 (81-188) : § 4.2 ;
   - tiret a) de l'art. 15 bis et art. 47 (2007-2148) : § 4.2 ;
   - ancienne rédaction de l'art. 46 al. 1 (un an) : § 3.8 ;
   - arrêté des travaux pénibles : § 5, partiellement.

   Restent ouverts : les art. 3, 14, 30 et 54 de 90-1455 ; les art. 48 al. 3 et 55 de 82-1030.
8. La note de la clé `loi60-33` porte « texte non lu » : ce n'est plus exact.

---

## 7. Références

### 7.1 Clés existantes (à citer telles quelles)

`loi60-30`, `loi60-33`, `decret74-499`, `decret79-510`, `decret79-536`, `decret81-187`,
`decret81-188`, `decret82-1030`, `decret88-1137`, `decret90-1455`, `decret94-1429`,
`decret96-326`, `decret97-291`, `decret97-555`, `decret97-1927`, `decret2001-779`,
`decret2003-1212`, `decret2007-2148`, `decret89-107`, `decret95-1166`,
`arrete-1978-11-18-retraite-complementaire`, et les `arrete-AAAA-MM-JJ-bareme-actualisation`.
`loi88-38` n'existe que dans les bibliographies du livre « Prestations sociales ».

À corriger dans les notes existantes : `decret74-499` (71-432 → 71-452 ; le rectificatif du
n° 39/1974 est lu par le chapitre, alors que la note dit « non lu ») et `loi60-33` (texte lu).

### 7.2 Entrées à créer (CSL-JSON, sur le gabarit de `precis/fr/references.json`)

```json
[
 {"id": "decret71-452", "type": "legislation",
  "title": "Décret n° 71-452 du 17 décembre 1971, portant attribution de prestations de vieillesse, d'invalidité et de survie",
  "title-short": "Décret n° 71-452 du 17 décembre 1971",
  "container-title": "Journal officiel de la République tunisienne", "issue": "56", "page": "1700-1702",
  "issued": {"date-parts": [[1971, 12, 17]]},
  "URL": "https://www.pist.tn/jort/1971/1971F/Jo05671.pdf",
  "note": "citation-key: decret71-452\nJORT n° 56 du 21 décembre 1971, pp. 1700-1702. Prestations minima transitoires servies par la CNSS en attendant le régime de la loi n° 60-33 (art. 1). 60 ans, 120 mois (art. 3) ; stage transitoire de 80 mois + 8 mois/an dès 1973 (art. 4) ; forfait de 60 % de la rémunération d'un manœuvre du BTP à 2 400 h (art. 5) ; veuve 50 %, orphelin 20/30 % (art. 12-13). Art. 24 : effet au 1er janvier 1972. Abrogé par le décret n° 74-499, art. 63. Lu à l'image."},
 {"id": "decret76-981", "type": "legislation",
  "title": "Décret n° 76-981 du 19 novembre 1976, organisant la caisse d'assurance vieillesse, invalidité et survivants",
  "title-short": "Décret n° 76-981 du 19 novembre 1976",
  "container-title": "Journal officiel de la République tunisienne", "issue": "72", "page": "2867-2869",
  "issued": {"date-parts": [[1976, 11, 19]]},
  "URL": "https://www.pist.tn/jort/1976/1976F/Jo07276.pdf",
  "note": "citation-key: decret76-981\nJORT n° 72 du 23 novembre 1976. Art. 1 : fusion du régime légal (décret n° 74-499) avec les régimes conventionnels, en application de l'art. 5 de la loi n° 60-33 ; création de la CAVIS. Art. 25 : abroge les art. 59 à 62 du décret n° 74-499 ; transfert des régimes conventionnels. Sans clause d'effet : exécutoire le 25 novembre 1976. Abrogé par le décret n° 94-1477. Art. 25 lu à l'image ; art. 1-2 par OCR, à confirmer à l'image."},
 {"id": "decret94-1477", "type": "legislation",
  "title": "Décret n° 94-1477 du 4 juillet 1994, abrogeant le décret n° 76-981 du 19 novembre 1976 organisant la caisse d'assurance vieillesse, invalidité et survie",
  "title-short": "Décret n° 94-1477 du 4 juillet 1994",
  "container-title": "Journal officiel de la République tunisienne", "issue": "55", "page": "1193",
  "issued": {"date-parts": [[1994, 7, 4]]},
  "URL": "https://www.pist.tn/jort/1994/1994F/Jo05594.pdf",
  "note": "citation-key: decret94-1477\nJORT n° 55 du 15 juillet 1994, p. 1193 (imprimé « Projet de décret »). Art. 1 : abroge le décret n° 76-981. Art. 2 : transfert à la CNSS des régimes légaux et conventionnels. Art. 3 : la CNSS gère les régimes des textes 81-6, 74-499, 82-1359, 82-1360, 89-107. Sans clause d'effet (règle de la loi n° 93-64). Couche texte."},
 {"id": "decret82-1030-rect", "type": "legislation",
  "title": "Rectificatif au décret n° 82-1030 du 15 juillet 1982, modifiant le décret n° 74-499 du 27 avril 1974",
  "container-title": "Journal officiel de la République tunisienne", "issue": "66", "page": "2197",
  "issued": {"date-parts": [[1982, 10, 19]]},
  "URL": "https://www.pist.tn/jort/1982/1982F/Jo06682.pdf",
  "note": "citation-key: decret82-1030-rect\nJORT n° 66, fascicule 19-22 octobre 1982, p. 2197. Art. 17 al. 3 : « l'âge de 60 ans » → « l'âge normal de celle-ci ». Lu à l'image."},
 {"id": "arrete-1975-07-04-age-mineurs", "type": "legislation",
  "title": "Arrêté du ministre des affaires sociales du 4 juillet 1975, fixant l'âge d'admission à la retraite pour les mineurs",
  "container-title": "Journal officiel de la République tunisienne", "issue": "47", "page": "1454",
  "issued": {"date-parts": [[1975, 7, 4]]},
  "URL": "https://www.pist.tn/jort/1975/1975F/Jo04775.pdf",
  "note": "citation-key: arrete-1975-07-04-age-mineurs\nArt. 1 : 55 ans pour les mineurs (art. 15 du décret n° 74-499). Art. 2 : effet au 1er janvier 1974. Lu à l'image."},
 {"id": "arrete-2015-09-11-age-mineurs", "type": "legislation",
  "title": "Arrêté du ministre des affaires sociales du 11 septembre 2015, fixant l'âge d'admission à la retraite pour les agents mineurs",
  "container-title": "Journal officiel de la République tunisienne", "issue": "75", "page": "2234-2235",
  "issued": {"date-parts": [[2015, 9, 11]]},
  "URL": "https://www.pist.tn/jort/2015/2015F/Jo0752015.pdf",
  "note": "citation-key: arrete-2015-09-11-age-mineurs\nJORT n° 75 du 18 septembre 2015. Art. 1 : 55 ans, 5 ans dans les mines ou 10 ans dans les services techniques ; application des art. 15 et 16 du décret n° 74-499. Couche texte."},
 {"id": "arrete-2023-05-22-age-assainissement", "type": "legislation",
  "title": "Arrêté du ministre des affaires sociales du 22 mai 2023, fixant l'âge d'admission à la retraite pour les agents travaillant dans les entreprises affiliées à la caisse nationale de sécurité sociale exerçant dans le domaine de l'assainissement, le nettoyage des voies, le traitement des ordures, la collecte, le transport, le traitement des déchets solides et liquides",
  "container-title": "Journal officiel de la République tunisienne", "issue": "55", "page": "1413",
  "issued": {"date-parts": [[2023, 5, 22]]},
  "URL": "https://www.pist.tn/jort/2023/2023F/Jo0552023.pdf",
  "note": "citation-key: arrete-2023-05-22-age-assainissement\nJORT n° 55 du 26 mai 2023. Art. 1 : 55 ans après 10 ans de service (art. 15 du décret n° 74-499). Couche texte."}
]
```

Facultatives, si le texte les cite : `decret78-962` et `decret89-268` (modificatifs de la CAVIS,
dont seul l'intitulé est connu). Pour chacune, il faut une entrée miroir dans
`precis/ar/references.json` avec l'URL `…A/Ja…`, et un signalement dans
`docs/notes/biblio-a-rapatrier.md`, faute de quoi le prochain `sync_biblio` écrasera les ajouts.

## 8. Notions à porter au glossaire

| Terme FR | Arabe (tel que lu en 1974, à valider par le terminologue) | Source canonique | État |
|---|---|---|---|
| Caisse d'assurance vieillesse, invalidité et survivants (CAVIS) | صندوق التأمين على الشيخوخة والعجز والباقين على قيد الحياة *(non lu : à relever dans Ja07276)* | décret n° 76-981, art. 1 | **à créer** (`cavis`) |
| Régime conventionnel (de retraite) | نظام تعاقدي | loi n° 60-33, art. 5 ; décret n° 74-499, art. 59-62 | à créer ; ne pas confondre avec `regime-conventionnel-public` |
| Contrat groupe | عقد جماعي *(à vérifier)* | décret n° 74-499, art. 60 et 62 | à créer, ou à définir dans l'entrée précédente |
| Prestation *minima* de vieillesse (1972-1973) | — | décret n° 71-452, art. 1 et 5 | facultatif |
| Allocation de vieillesse (RSNA, en capital) | منحة الشيخوخة | décret n° 74-499, art. 39-43 | l'entrée existe (`allocation-de-vieillesse`, définie sur la loi n° 85-12, art. 42) : ajouter le sens RSNA de 1974 |
| Stage (de cotisation) | التربص | décret n° 74-499, art. 15 b) | existe (`stage-cotisation`) |
| Salaire moyen de référence | الاجر المتوسط المعتمد / معدل الاجر المرجوع اليه | art. 17-19 | existe |
| Âge normal de la retraite | السن العادية للتقاعد *(à vérifier)* | rectificatif du décret n° 82-1030 ; décret n° 2007-2148, art. 17 § 3 | à envisager |

## 9. Lacunes (TODO, rien n'a été inventé)

- **Date exécutoire** des décrets n° 94-1477, 96-326, 97-291, 97-555 et 2007-2148 et des arrêtés
  de 2015 et 2023 : elle dépend de la date de dépôt au gouvernorat de Tunis, qui n'est pas connue.
- **Loi n° 60-33** : fascicule n° 57 à dates multiples (13-16 décembre 1960). `jort_cache` donne
  une publication au 13 décembre, veille de la signature. La date exécutoire n'est pas tranchée.
- **Décrets n° 78-962 et 89-268** (modificatifs de la CAVIS) : leur intitulé seul est connu.
- **Loi n° 88-38** (6 mai 1988, modifie la loi n° 60-30), visée par 94-1477 et 97-555. D'après la
  note de la clé existante `loi88-38` (livre « Prestations sociales », lu à l'image), son art. 1er
  réécrit les art. 52 et 61 (allocations familiales) et son art. 5 fixe l'entrée en vigueur au
  1er janvier 1989. Rien n'indique qu'elle touche la vieillesse. Ses art. 2 à 4 ne sont pas décrits
  dans cette note : à relire (JORT n° 33/1988, p. 735) avant d'écrire que la loi n° 60-30 ne couvre
  pas la vieillesse après 1988.
- **Régimes conventionnels avant 1974** : aucune liste nominative des caisses ou contrats groupes
  n'a été trouvée au JORT. La déclaration de l'art. 119 de la loi n° 60-30 n'a pas été publiée
  sous un intitulé repérable.
- **Arrêté du 29 mars 1961** (commission consultative) : seul son intitulé est connu.
- **Pagination arabe** du décret n° 74-499 : établie seulement pour les art. 44 à 48 (p. 1012) ; à
  compléter pour citer l'édition arabe.
- **Le projet de décret de 2023-2024 sur l'âge (62 ans optionnel)** : texte, numéro et sort
  inconnus. `jort_cache` s'arrête au 10 avril 2026 ; **d'avril à septembre 2026, contrôler
  directement pist.tn** avant d'écrire que l'âge légal du RSNA est toujours de 60 ans.
- **Arrêtés de l'art. 15 postérieurs à 1975 et antérieurs à 2015** : aucun n'est trouvé par les
  requêtes « penibles », « insalubres » et « admission a la retraite ». L'arrêté de 2015 ne vise
  que celui de 1975, ce qui plaide pour l'absence d'arrêté intermédiaire **[D]**, sans le prouver.
- Les affirmations du chapitre sur **90-1455, 94-1429, 96-326, 97-1927 et 2001-779** (97-291 : voir § 10) n'ont
  pas été relues pour cette note.

---

## 10. Vérification ciblée du 23 septembre 2026

Demandée par le bibliographe sur cinq points du chapitre. Tout ce qui suit est lu **à l'image**,
sur les fascicules du corpus local (`PDFs-legislation-tunisie/PDFs/JORT/<année>/fr/`), rendus par
`pdftoppm` à 250 dpi et découpés par colonne. Seul le fascicule de 1997 a une couche texte ; elle a
été relue contre l'image.

### 10.1 Décret n° 97-291 du 3 février 1997 — JORT n° 13 du 14 février 1997, p. 203-204

Fascicule `1997/fr/Jo01397.pdf` (« traduction française pour information »), p. 203 (colonne de
droite, lue à l'image) et p. 204 (art. 3, couche texte seule). Le visa cite « le décret n° 95-326 du 1er mars 1996 » : coquille du
fascicule pour 96-326.

- **Art. 1er** : « Les articles 29, 38 et 53 alinéa 4 du décret n° 74-499 du 27 avril 1974 susvisé
  sont abrogés et remplacés par les dispositions suivantes : »
  - « **Article 29 (nouveau).** — Le conjoint survivant d'un bénéficiaire d'une pension de vieillesse
    ou d'un assuré, remplissant au moment de son décès la condition de stage requise pour
    l'ouverture du droit à pension de vieillesse, bénéficie d'une pension de survivant. / Le même
    droit est reconnu au conjoint survivant d'un bénéficiaire d'une pension d'invalidité ou d'un
    assuré, décédé avant l'âge normal de mise à la retraite qui, au moment de son décès,
    remplissait les conditions prévues à l'article 21 pour prétendre à une pension d'invalidité. »
    La mention distincte du « veuf invalide » (1974, 1981) disparaît.
  - « **Article 38 (nouveau).** — En aucun cas le moment [sic] cumulé des pensions de conjoint
    survivant et d'orphelins ne doit excéder le montant de la pension dont bénéficiait ou aurait pu
    bénéficier le défunt. Il est procédé, le cas échéant, à une réduction temporaire des pensions
    d'orphelins. »
  - « **Article 53 alinéa 4 (nouveau).** — Pour le calcul des majorations des pensions de conjoint
    survivant et des orphelins, il sera tenu compte du taux de la pension de vieillesse ou
    d'invalidité dont bénéficiait ou aurait dû bénéficier le défunt au moment de son décès ainsi
    que du taux de réversion. »
- **Art. 2** : « Les dispositions de l'article 52 du décret n° 74-499 du 27 avril 1974 susvisé sont
  abrogées. »
- **Art. 3** : exécution. Aucune clause d'effet.

**Comparaison avec l'alinéa 4 antérieur.** L'article 53 de 1974 n'a qu'un alinéa (« Le montant des
pensions en cours de paiement sera revisé en cas de hausse sensible du niveau général des salaires.
La date et les modalités de cette révision sont déterminées par décret. », JORT n° 30/1974,
p. 918). L'alinéa 4 vient du **décret n° 81-187, art. 1er** (JORT n° 10/1981, p. 319, colonne de
droite) : « Pour le calcul des majorations des pensions des veuves et des orphelins il sera tenu
compte du taux de la pension de vieillesse ou d'invalidité dont bénéficiait ou aurait dû bénéficier
le défunt au moment de son décès ainsi que du taux de réversion. » Le texte de 1997 n'en diffère que
par « de conjoint survivant » au lieu de « des veuves ». **La phrase du chapitre est confirmée** ; sa
rédaction a été précisée (l'alinéa 4 est réécrit en entier, avec cette seule substitution).

**Article 52 abrogé** — rédaction de 1974 (JORT n° 30/1974, p. 918) : « Le cumul d'une pension
d'invalidité et d'une pension de survivants est interdit. Dans ce cas, seule la pension la plus
élevée est servie. » **La phrase du chapitre (abrogation par l'art. 2) est confirmée.**

### 10.2 Décret n° 74-499 — JORT n° 30/1974

Fascicule `1974/fr/Jo03074.pdf`.

- **p. 916, colonne de droite** : art. 8 (« Il est déterminé sur la base d'une étude actuarielle
  par rapport à une période d'équilibre préétablie. La période d'équilibre initiale est de dix
  années à compter de la date d'entrée en vigueur du régime. Elle peut être modifiée
  ultérieurement, conformément à l'évolution technique du régime sans toutefois que sa durée
  puisse être inférieure à cinq années. ») ; art. 10 (« La réserve technique du régime est
  constituée par la différence entre les recettes et les dépenses du régime, telles qu'elles sont
  visées aux articles 5 et 6 ci-dessus. La réserve initiale est constituée par un transfert des
  autres régimes gérés par la Caisse Nationale de Sécurité Sociale d'un montant de 15 millions de
  dinars. ») ; art. 11 (« Les fonds de la réserve technique doivent être placés, soit à moyen
  terme, soit à long terme, selon un plan financier établi par le Conseil d'Administration. […] ») ;
  art. 12 (comptabilité séparée) ; art. 13 (« La Caisse Nationale de Sécurité Sociale doit
  effectuer au moins une fois tous les cinq ans une analyse actuarielle et financière du régime. /
  Si l'analyse prévue à l'alinéa précédent révèle un danger de déséquilibre financier du régime,
  le taux de cotisation est réajusté. »). **Confirmé.**
- **p. 917, colonne de droite, bas** : art. 35 (« Les pensions d'orphelins allouées en vertu des
  dispositions de la présente section sont collectives et réduites au fur et à mesure que chaque
  orphelin cesse de remplir les conditions requises pour en bénéficier ou vient soit à occuper un
  emploi salarié, soit à contracter mariage, soit à décéder. »).
- **p. 918, colonne de gauche, haut** : art. 36 (« La pension due au titre d'un orphelin est
  suspendue aussi longtemps que le bénéficiaire est pris en charge par une institution publique ou
  privée bénéficiant de l'aide de l'Etat. »). **Confirmé** ; le locator « art. 35-36 » est juste
  (les deux articles sont à cheval sur p. 917-918).

### 10.3 Décret n° 81-188 — JORT n° 10 du 17 février 1981, p. 319-320

Fascicule `1981/fr/Jo01081.pdf`, p. 320.

- **Art. 1er** : « Les dispositions des articles 21 b), 22 1er alinéa, 29, 33 et 34 du décret
  sus-visé n° 74-499 du 27 avril 1974 sont abrogées et remplacées par les dispositions
  suivantes : » ; art. 34 (nouveau) : 30 % « du montant de la pension de vieillesse ou d'invalidité
  dont bénéficiait ou aurait dû bénéficier le défunt au moment de son décès ».
- **Art. 2** : « L'article 31 du décret sus-visé n° 74-499 du 27 avril 1974 est complété comme
  suit : / Art. 31. (2e alinéa nouveau et complémentaire). — Ce taux est majoré à concurence de 75 %
  de la pension de vieillesse ou d'invalidité dont bénéficiait ou aurait dû bénéficier le défunt
  au moment de son décès, à condition qu'il n'y ait pas d'enfant bénéficiaire, ou que le total de la
  pension de veuve et d'orphelin ne dépasse pas le montant de la pension de l'assuré. En cas de
  dépassement la pension d'orphelin et [sic] réduite d'autant. »
- **Le partage art. 1 / art. 2 est confirmé** : la réversion à 75 % relève de l'art. 2 (un seul
  alinéa ajouté à l'art. 31 ; il n'y a pas d'« al. 3 » distinct).

### 10.4 Loi n° 60-30 — JORT n° 57, 13-16 décembre 1960

Fascicule `1960/fr/Jo05760.pdf`.

- **p. 1602, colonne de gauche** : art. 2 (« Cette organisation assure, en faveur des travailleurs
  salariés, dans le cadre des prescriptions fixées par la présente loi, le service des prestations
  définies par un régime de prestations familiales et un régime d'assurances sociales. ») ; art. 5
  (« La Caisse Nationale est l'organisme de gestion des régimes visés à l'article 2 ci-dessus. […]
  est habilitée : […] 4° à gérer, selon des conventions particulières approuvées par le Secrétaire
  d'Etat à la Santé Publique et aux Affaires Sociales, après avis des Secrétaires d'Etat
  intéressés, des régimes conventionnels de retraite ou d'entr'aide sociale. »).
- **p. 1608, colonne de gauche** : titre II, chapitre II « Les assurances sociales », art. 68
  (« Les assurances sociales comprennent : 1° des indemnités en espèces, en cas de maladie, de
  maternité ou de décès, dont le service est assuré par la Caisse Nationale; 2° l'octroi des soins,
  en cas de consultations ou d'hospitalisation […] »).
- **p. 1612, colonne de gauche** : art. 119 (« Sous peine de retrait d'agrément, les organismes de
  toutes sortes assurant, sous quelque forme que ce soit, la couverture des risques maladie,
  décès, maternité et vieillesse, doivent adresser […] dans les six mois à dater de la
  promulgation de la présente loi, une déclaration comportant toutes indications sur les régimes
  qu'ils gèrent. ») ; art. 120 (« Les régimes d'assurances sociales, définis dans le titre II,
  chapitre II de la présente loi, excluent à due concurrence les régimes conventionnels assurant
  la couverture des mêmes risques. Toutefois, les régimes conventionnels doivent continuer à
  assurer, à titre complémentaire, la différence entre les avantages accordés par le régime légal
  et ceux qu'ils accordaient. »).
- **Les passages cités par le chapitre sont confirmés.**

### 10.5 Loi n° 60-33 — même fascicule, p. 1616

Art. 5 confirmé à l'image (colonne de droite) : « Un décret prévoira dans quelle mesure ou sous
quelle forme les régimes conventionnels, assurant la couverture des mêmes risques, pourront
continuer à exister, en dehors du régime général et, en cas de fusion totale, les conditions et
les modalités de cette fusion. » Suit la formule d'exécution, sans clause d'effet. Le TODO de
`index.qmd` est réécrit en conséquence : reste ouverte la date d'entrée en vigueur (pas de clause ;
fascicule daté 13-16 décembre 1960, date de publication à trancher avant d'appliquer la règle du
jour franc).

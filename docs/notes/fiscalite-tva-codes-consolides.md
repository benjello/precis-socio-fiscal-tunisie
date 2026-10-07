# Code de la TVA — éditions consolidées antérieures à 2019 retrouvées en ligne

> Note documentaire, 7 octobre 2026. Suite du § 6.2 de `fiscalite-tva-tableaux-produits.md` :
> chercher, dans les archives du web et les sites publics, des états consolidés du code de la taxe
> sur la valeur ajoutée antérieurs à la refonte des tableaux de 2016, pour épargner la lecture
> d'environ 150 articles de lois de finances. Aucune administration n'a été sollicitée.
>
> **Rangement.** Les fichiers sont dans
> `~/projets/tunisia-data/data/raw/minfinances/codes_tva/`, dossier désormais ignoré par git
> (vérifié par `git check-ignore`). Le catalogue
> `sources/minfinances-codes-tva-urls.csv` reste à créer (matière au § 6 et aux manifestes).
>
> **Seconde passe (§ 8)** : sites officiels, tous formats — six états officiels en arabe retrouvés.

## 1. Ce qui est trouvé, en une phrase par pièce

Première passe : aucune édition officielle antérieure à 2016 (la seconde passe, § 8, en retrouve six états en arabe, de 2006 à 2008, sur le site documentaire du ministère). Sont retrouvés en première passe : deux
consolidations **privées** en PDF (janvier 2008 et janvier 2014), une consolidation privée en
pages HTML dont les archives du web gardent les états de 2002 à 2010, et deux éditions officielles
de l'Imprimerie officielle (2016 et 2017) qui, bien que postérieures à la refonte, **impriment
encore un tableau C complet, numéros du tarif compris** — dans sa rédaction de 1991 augmentée de
l'ajout de 2004 ; que les retraits de 1992 à 1998 y soient portés n'est pas établi (§ 3).

## 2. Tableau des éditions

Les années des noms de fichiers suivent la consigne de nommage ; la colonne « date portée » dit ce
que le document affirme lui-même, et rien d'autre.

| Fichier (dans `codes_tva/`) | Titre et éditeur | Date portée par le document | Langue, pages | Tableaux | Couche texte | Origine → archive | Octets, SHA-256 |
|---|---|---|---|---|---|---|---|
| `code_tva_2008_fr.pdf` | « Livre 3. Code de la TVA » ; ni auteur ni éditeur dans le fichier ; servi par le site du cabinet « Best Management » (bm.com.tn) | **aucune** date d'édition. Métadonnées PDF : créé le 10 janvier 2008. Loi la plus récente citée en note : n° 2007-70 (LF 2008) | FR, 38 p. | **A, B, B bis** (p. 21-34), notes de bas de page par numéro (article et loi) ; tableau A : n° 1 à 50 retrouvés dans la couche texte sauf le n° 20, non repéré par le balayage (à voir à l'œil) ; tableau B : n° 1 à 12 du § I sauf le n° 6, non repéré (même réserve). **C absent** (supprimé ; l'article 7 en garde la mention entre crochets) | oui (PDF protégé contre la copie, `pdftotext` le lit) | `http://www.bm.com.tn/ckeditor/files/code_tva.pdf` → `https://web.archive.org/web/20161023112429id_/http://www.bm.com.tn:80/ckeditor/files/code_tva.pdf` (copie d'archive identique octet pour octet) | 167 789 ; `458fed58bdfd432cd3d6dd3de22c86b94e4a750907202f28d5bbdf8d5abf3015` |
| `code_tva_2014_fr.pdf` | Recueil des codes fiscaux (IRPP-IS, TVA et droit de consommation, enregistrement et timbre, droits et procédures fiscaux, fiscalité locale) ; page de garde : « SEFAC — Société d'Études, de Formation, d'Assistance & de Conseil » ; servi par bm.com.tn sous le nom `les_codes_definitifs_2014.pdf` | **aucune** mention « à jour au ». Métadonnées PDF : créé le 24 janvier 2014. Loi la plus récente citée dans la partie TVA : n° 2013-54 (LF 2014) | FR, 364 p. ; tableau A à partir de la p. 160, tableau B bis à partir de la p. 177 (pagination imprimée, bornes à relire) | **A entier** (n° 1 à 50 tous retrouvés dans la couche texte, avec les bis ; pages imprimées 160 à 179 continues, la p. 180 non repérée par le balayage), **B et B bis** présents (numéros non énumérés un à un), notes par numéro ; les numéros abrogés restent visibles (« 7 bis – Abrogé Art 64 LF 2013-54 »). **C absent** | oui, propre | `http://www.bm.com.tn/ckeditor/files/les_codes_definitifs_2014.pdf` → `https://web.archive.org/web/20181008125535id_/http://www.bm.com.tn:80/ckeditor/files/les_codes_definitifs_2014.pdf` (identique octet pour octet) | 1 770 955 ; `e7a199bb824c1850aa4fbff48cf3a401b4ffa2f4661ffa8cf90772a3009e4c22` |
| `code_tva_2016_fr.pdf` | « Code de la taxe sur la valeur ajoutée, loi relative au droit de consommation, leurs textes d'application et textes connexes — 2016 », Publications de l'Imprimerie officielle de la République tunisienne | « Edition revue et corrigée le 29 février 2016 » | FR, 542 p. | A nouveau, B nouveau, B bis nouveau (état après la LF 2016) ; **tableau C en entier, avec les numéros du tarif** (p. 53-75 environ ; 210 lignes à numéro de tarif comptées dans la couche texte), sous la note : « Modifié en vertu de l'article 43 LF 91-98 […] et supprimé en vertu de l'article 13 de la loi n° 2006-80 » ; dernière entrée notée « Ajouté par art. 71 de la L.F. n° 2004-90 » | oui | `http://chaexpert.com/documents/2016%20-%20CODE%20TVA%202016.pdf` → capture Wayback `20230610154921` (non comparée octet pour octet) | 2 142 282 ; `77203067f2832760bc9da4e63317382925857fdef841affd8b407da3b48c8bfb` |
| `code_tva_2017_fr.pdf` | même titre, « 2017 », Imprimerie officielle | « Edition revue et corrigée le 15 mars 2017 » | FR, 471 p. | tableaux nouveaux (état après la LF 2017) ; tableau C reproduit lui aussi (en-tête et premières lignes vus, étendue non comptée) | oui | `http://www.legislation.tn/sites/default/files/codes/TVA.pdf` → `https://web.archive.org/web/20181220234514id_/http://www.legislation.tn:80/sites/default/files/codes/TVA.pdf` (fichier pris à cette adresse d'archive). Même fichier, à la taille près, sur `chaexpert.com/documents/CODE%20TVA.pdf` et `africa-laws.org` | 3 826 418 ; `517ae10acf6174da4df8e369d1cf7fe4fc057f425669d652d292c7a8f2097060` |
| `jurisite_html/` (113 fichiers `.htm` + `MANIFESTE.csv`) | « Code de la TVA », site privé Jurisite Tunisie (jurisitetunisie.com), pages `tva1000A1` à `A5` (tableau A), `tva1000B`, `tva1000Bbis`, `tva1000C1` à `C5`, `tva1000` (sommaire), `tva1040` (article sur les taux) | **aucune** date d'édition dans le texte (la ligne « dernière modification de cette page » est produite par script et vide à l'archive). Seule date sûre : l'horodatage de capture | FR, HTML | A, B, B bis, C en entier ; notes par numéro (loi, sans article) ; **C sans les numéros du tarif** (libellés seuls) | HTML (cp1252) | `http://www.jurisitetunisie.com/tunisie/codes/tva/<page>.htm` → `https://web.archive.org/web/<horodatage>id_/…` ; une ligne par fichier dans `MANIFESTE.csv` (adresse, horodatage, taille, SHA-256) | 1,2 Mo au total |

Hors fenêtre, non rangés (relevés pour mémoire) : édition arabe 2018 de l'Imprimerie officielle
(`legislation.tn/sites/default/files/codes/TVAArabe.pdf`, capture `20180713172411`, 477 p.,
3 106 609 octets, SHA-256 `6340e06f…199ec5`) ; édition 2017 du ministère
(`finances.gov.tn/sites/default/files/CODE%20TVA%202017%20FR.pdf`, capture `20200905014226`, non
ouverte) ; éditions 2018, 2020 et 2022 sur chaexpert.com ; édition 2020 sur droit-afrique.com
(`uploads/Tunisie-Code-2020-tva.pdf`) ; édition 2024 sur alliance-tunisie.com.

### États successifs de la consolidation Jurisite

Pour chaque page, captures retenues : la première, puis la dernière avant la fin de 2002, 2004,
2006, 2008, 2010, 2012, 2014, 2015, 2016 et 2017. La « loi la plus récente citée » borne par le bas
l'actualité de la page ; elle ne dit pas que toutes les lois antérieures y sont portées.

| Page | Captures (de — à, nombre) | Loi la plus récente citée, par capture |
|---|---|---|
| A1 (n° 1 à 9) | 2002-06 — 2026, 93 | 2002 et 2004 : 99-101 ; 2006 : 2004-90 ; 2008 et après : 2007-70 |
| A2 (n° 10 à 19) | 2002-04 — 2026, 80 | 2002 : 2000-98 ; 2004-2006 : 2003-80 ; 2008 et après : 2007-70 |
| A3 | 2002-07 — 2026, 82 | 2002-2006 : 98-111 ; 2008 et après : 2007-70 |
| A4 | 2002-09 — 2026, 78 | 2002 : 2001-123 ; 2004-2008 : 2003-80 ; 2010 et après : 2008-77 |
| A5 | 2002-05 — 2017, 55 | 2001-123 à toutes les dates |
| B | 2002-06 — 2026, 110 | 2002-2006 : 99-101 ; 2008 : 2006-80 ; 2010 et après : 2009-71 |
| B bis | 2003-02 — 2026, 140 | 2003 : 2001-123 ; 2004 : 2003-80 ; 2006 : 2005-106 ; 2008 et après : 2006-80 |
| C1 à C5 | 2002 — 2016 (39 à 70 par page) | note d'en-tête : art. 43 de la LF 91-98 ; C5, à partir de 2006 : art. 71 de la loi 2004-90 |

Constat : **le site n'est plus tenu à jour après la LF 2010** (loi n° 2009-71) ; aucune loi de
2010 à 2015 n'y est citée, et les captures de 2012 à 2017 ont la même longueur de texte et citent
les mêmes lois que celles de 2010 (textes non comparés mot à mot). Il ne donne donc pas l'état de fin 2015. Les pages du tableau C restent en ligne après 2007
sans mention de la suppression.

## 3. Ce que chaque pièce permet de reconstituer

- **État des tableaux A, B et B bis au 1er janvier 2014** (`code_tva_2014_fr.pdf`) : c'est la pièce
  maîtresse. Chaque numéro porte en note l'article et la loi qui l'ont ajouté, modifié ou abrogé.
  Dans les pages des tableaux, 89 couples article-loi distincts sont relevés par expression
  régulière, sur 29 lois de 1988 à 2013 (88-145, 89-115, 90-111, 91-98, 92-122, 93-125, 94-127,
  95-109, 97-88, 98-111, 99-70, 99-101, 2000-98, 2001-123, 2002-103, 2003-80, 2005-106, 2006-80,
  2006-85, 2007-69, 2007-70, 2008-77, 2009-32, 2009-71, décret-loi 2011-56, 2011-7, LFC 2012-8,
  2012-27, 2013-54) — décompte de travail, à refaire à la main avant usage.
  Contrôle fait contre la note des tableaux, sur deux numéros seulement et pour l'état de janvier
  2014 : le n° 3 y est « l'importation des peaux brutes » et le n° 10 « l'exploitation des
  douches », comme le suppose la lecture de l'article 31 § 1 de la LF 2016 (lacune 2). Trois lois
  séparent cet état de la LF 2016 ; la liste complète des numéros abrogés par l'article 31 § 1
  n'a pas été rapprochée de la numérotation de 2014 — c'est le premier contrôle à faire. Le n° 6 y
  est « les affaires à caractère philanthropique effectuées par les associations », note :
  « Modifié Art. 55 LF Comp 2012-8 » (lacune 4, à lire).
- **État des mêmes tableaux après la LF 2008** (`code_tva_2008_fr.pdf`) : même appareil de notes,
  rédigées en toutes lettres (« Numéro ajouté par l'article 49 de la loi n° 2007-70… »). Sert de
  point de contrôle intermédiaire. Pour la lacune 11, relevé dans les pages des tableaux
  seulement : la loi n° 2007-70 (LF 2008) y est citée par ses articles **17** (modification, avec
  l'art. 23 de la loi 88-145), **21** (modification) et **39** (ajout) dans les deux PDF, et par
  son article 58 (ajout) dans celui de 2014 — les articles 17 et 21 sont donc ceux que les deux
  consolidations privées donnent, ce qui n'est pas une lecture du *Journal officiel*. La loi
  n° 2011-7 (LF 2012) y est citée par ses articles **37** (ajout) et **47** (modification), sans
  paragraphe : le « § 7 » de l'article 37 n'est ni confirmé ni contredit.
- **États vers 2002, 2004, 2006, 2008 et 2010** (`jurisite_html/`) : cinq photographies de A, B et
  B bis, dont trois **avant** la suppression du tableau C et le passage de 10 à 12 %. Elles
  permettent de voir le libellé d'un numéro avant sa modification de 2003 à 2009, ce que les deux
  PDF, qui ne donnent que la dernière rédaction, ne permettent pas.
- **Tableau C à sa suppression** (`code_tva_2016_fr.pdf`, p. 53-75 ; `jurisite_html/tva1000C*`) :
  l'édition officielle de 2016 l'imprime avec les numéros du tarif ; Jurisite en donne les libellés
  à partir de 2002. C'est la matière de la lacune 1 et un contrôle de la transcription de 1988
  (lacune 10). **Réserve** : 210 lignes à numéro de tarif, soit à peu près le volume du tableau de
  1988 ; il n'est pas établi que les retraits de 1989 à 1998 (lessives, tableaux « M bis » et « L »)
  y soient portés. Le mot « lessives » est absent des pages Jurisite, ce qui va dans le sens du
  retrait de 1989, sans plus. À rapprocher ligne à ligne de la transcription de 1988 avant d'écrire
  quoi que ce soit sur la composition finale. Épreuve simple : prendre deux ou trois numéros du
  tarif dans les listes de retrait de la LF 1995 ou de la LF 1996 (couche texte locale) et les
  chercher dans le tableau C de l'édition 2016.
- **États après les LF 2016 et 2017** (`code_tva_2016_fr.pdf`, `code_tva_2017_fr.pdf`) : les deux
  photographies qui manquaient entre la refonte et l'édition 2019 déjà sur disque.

Nature des sources : les deux PDF de 2008 et 2014 et les pages Jurisite sont des consolidations
privées. Elles servent d'**index et de contrôle**, pas de source citable d'un état du droit : chaque
changement se cite sur son article au *Journal officiel*.

## 4. Périodes qui restent sans édition

- **1988-2001** : aucune édition, officielle ou privée. Les états intermédiaires de cette période
  ne sont connus que par les notes des consolidations ultérieures (qui nomment l'article) ; un
  numéro créé puis abrogé avant 2002 peut n'avoir laissé aucune trace.
- **2011-2013** : pas de photographie propre, mais l'édition de janvier 2014 en porte les notes.
- **2014-2015** (LFC 2014, LF 2015, LFC 2015) : aucune édition entre janvier 2014 et la refonte.
  L'état de fin 2015 s'obtient en rejouant ces trois lois sur l'état de 2014.
- **Tableau C entre 1989 et 2001** : aucun état intermédiaire.
- En arabe : rien en première passe avant 2018 ; la seconde passe (§ 8) retrouve six états
  officiels de décembre 2006 à avril 2008. Rien en arabe de 2009 à 2017.

## 5. Requêtes faites et couverture (rejouables)

Faites le 7 octobre 2026. La Wayback Machine a répondu plusieurs fois « 504 » ou « Temporarily
Offline » pendant la séance : une requête marquée « échec » n'est pas une absence.

| Requête | Résultat |
|---|---|
| CDX `url=<domaine>&matchType=domain&filter=mimetype:application/pdf&collapse=urlkey&limit=60000`, filtré sur « tva », « valeur », « taxe », « code » | impots.finances.gov.tn (1 225 PDF) : formulaires et notes communes, aucun code ; finances.gov.tn (4 681) : « CODE TVA 2017 FR.pdf » seul ; portail.finances.gov.tn (429) : code d'incitation et comptabilité publique, pas de TVA ; jibaya.tn (101) : édition 2023 ; profiscal.com (323) : cours et exercices de TVA de 2003-2004, pas de code ; cnudst.rnrt.tn (1 753), investintunisia.tn (209), tunisieindustrie.nat.tn (1 532), e-justice.tn (1 270), douane.gov.tn (3 448) : rien sur la TVA ; droit-afrique.com (4 623) : édition 2020 seule ; jurisitetunisie.com (323) : extraits de lois de finances ; legislation.tn (18 152) : `codes/TVA.pdf` et `codes/TVAArabe.pdf` ; legislation-securite.tn (739) : rien |
| même requête sur iort.gov.tn | **échec** (504), puis une seule ligne à la relance (une page de constitution) : couverture non établie, à rejouer |
| CDX avec `filter=original:.*(?i)(tva\|valeur\|codes?).*` sur cinq domaines | **requête mal formée** (zéro ligne partout) : ne vaut pas recherche |
| CDX de toutes les captures de `legislation.tn/sites/default/files/codes/TVA.pdf` et `TVAArabe.pdf` | deux captures chacune (2018-2019 ; 2018-2020), une seule empreinte par fichier : pas de version antérieure archivée à cette adresse |
| CDX `url=jurisitetunisie.com/tunisie/codes/tva*` puis captures de chaque page | 14 pages, 39 à 140 captures chacune (§ 2) |
| CDX `url=impots.finances.gov.tn/documentation*` | 666 adresses ; `impots_fr/tva_fr_1…16.htm` (2006-2007) ouvert : guide de présentation, pas le texte du code ni les tableaux |
| CDX `url=chaexpert.com/documents/*` (PDF) | éditions officielles 2016, 2017, 2018, 2020, 2022 de la TVA ; pour d'autres codes des éditions 2006 et 2009, aucune de la TVA avant 2016 |
| CDX `url=bm.com.tn/ckeditor/files/*` | `code_tva.pdf`, `les_codes_definitifs_2014.pdf`, `code_irpp_is_2011.pdf` |
| Recherche web : « Code de la taxe sur la valeur ajoutée » Tunisie « Imprimerie Officielle » 2011/2012/2014/2015 « Tableau A » ; « code de la TVA » pdf « édition 2009/2010/2012/2014 » « tableau C » | chaexpert.com, africa-laws.org, bm.com.tn, alliance-tunisie.com, infirst.tn ; aucune édition officielle antérieure à 2016 |
| archive.org `advancedsearch` : (« taxe sur la valeur ajoutée » OR TVA) AND (Tunisie OR tunisien) ; puis sur le titre | zéro notice |
| Catalogue HathiTrust : « taxe sur la valeur ajoutée » Tunisie | réponse non exploitable (page non analysée) : **non concluant** |
| Sur disque : `find` sur `*tva*`, `*taxe*valeur*`, `*code*` dans `PDFs-legislation-tunisie` et `tunisia-data/data/raw` | rien d'autre que les éditions 2019, 2021, 2023, 2025 déjà connues |

Non faits, faute de temps : Gallica ; recherche en arabe (« مجلة الأداء على القيمة المضافة ») ; les
autres sites de cabinets qui reprennent les éditions de l'Imprimerie officielle ; les pages
`_instances/L….html` de Jurisite, qui pourraient reproduire des articles de lois de finances.

## 6. Catalogue à créer dans `tunisia-data` (matière, non écrite)

`sources/minfinances-codes-tva-urls.csv` : une ligne par fichier du § 2 (adresse d'origine, adresse
d'archive, date de collecte 2026-10-07, octets, SHA-256) ; pour les pages HTML, reprendre
`data/raw/minfinances/codes_tva/jurisite_html/MANIFESTE.csv`. Et une ligne
`data/raw/minfinances/codes_tva/` au `.gitignore`.

## 7. Effet sur le coût du registre complet

Les quelque 150 lectures ne disparaissent pas : elles changent de nature.

- **Le repérage est acquis pour A, B et B bis de 1988 à 2013.** Les notes de l'édition de 2014
  nomment l'article de chaque changement encore visible : environ 90 couples article-loi. Les
  périodes 1988-1994, 1995-2002 et 2003-2013 du plan (§ 6.2 de la note des tableaux, environ 120
  articles) passent de la **découverte** à la **vérification ciblée** : ouvrir l'article nommé,
  relever la page, la rédaction antérieure et la date d'effet. La recherche plein texte muette de
  2003 à 2007 (lacune 11) n'a plus à être refaite.
- **Ce qui ne demande plus de lecture pour établir un état** : l'état consolidé au 1er janvier
  2014, celui d'après la LF 2008, et les cinq photographies de 2002 à 2010. La reconstitution de
  l'état de fin 2015 « en rejouant les lois de 1989 à 2015 » se réduit à rejouer trois lois sur
  l'état de 2014.
- **Lectures qui restent entières** : (a) LFC 2014, LF 2015 et LFC 2015 ; (b) l'histoire du
  tableau C de 1989 à 2001 — listes « M », « M bis », « P », « L », à l'image —, l'édition 2016
  ne donnant qu'un tableau dont l'actualité reste à éprouver ; (c) les numéros créés et abrogés avant 2002, invisibles dans toutes
  les pièces ; (d) les 28 articles de 2016 à 2026, déjà repérés, que les éditions 2016 et 2017
  permettent de contrôler ; (e) les décrets de l'article 8, hors tableaux.
- **Ordre de grandeur, non mesuré** : sur 25 à 35 heures estimées pour A, B et B bis, la part de
  repérage et de reconstitution d'états tombe ; restent la vérification article par article des
  quelque 90 renvois et les trois lois de 2014-2015. Les 8 à 12 heures du tableau C ne baissent
  que si le rapprochement de l'édition 2016 avec la transcription de 1988 montre que les retraits
  y sont portés.

**Après la seconde passe (§ 8).** Le ministère des finances a bien mis le code en ligne, et les
archives en gardent six états officiels en arabe, de décembre 2006 à avril 2008, tableau C compris
pour le premier. La colonne 2008 se contrôle donc sur une source officielle ; la colonne 2014 reste
sur un recueil privé ; l'histoire du tableau C a désormais son plan de lecture officiel (neuf lois,
seize articles) et son état final. Aucune édition française officielle antérieure à 2016 n'est
archivée : les adresses où elle se trouvait sont au § 8.3.

Aucune fiche de `docs/recherches.yml` n'est proposée : il ne s'agit pas d'un texte attendu au
*Journal officiel*, mais d'éditions ; les requêtes ci-dessus tiennent lieu de trace rejouable.

## 8. Seconde passe — les sites officiels, tous formats

Faite le 7 octobre 2026, de 18 h 20 à 19 h environ. Question posée : le ministère des finances
a-t-il mis en ligne le code, et les archives du web l'ont-elles gardé ? Réponse : **oui, en arabe,
pour 2006-2008** ; en français, le ministère le publiait à la même adresse mais la page n'a jamais
été archivée.

### 8.1 Ce qui est trouvé : le recueil « TVA et droit de consommation » du site documentaire du ministère

Le ministère des finances a tenu de 2006 à 2016 un « Site documentaire du ministère des finances —
Documentation fiscale » (`documentation.finances.gov.tn`, puis
`documentations.finances.gov.tn/dgelf`), dont le menu porte « Recueils des textes fiscaux : IRPP et
IS ; TVA et DC ; droits d'enregistrement et de timbre ; droits et procédures fiscaux ; fiscalité
locale ; incitations aux investissements ; textes non incorporés aux codes ; conventions de non
double imposition ; notes communes ». Le portail du ministère y renvoyait depuis sa rubrique
« cadre légal — fiscalité » (`portail.finances.gov.tn/cadrelegal.php?dom=FISC`, capture de 2008).

La version **arabe** du recueil « TVA et DC » (une seule page HTML d'environ 1 Mo, code, tableaux,
loi sur le droit de consommation et textes d'application) est archivée 21 fois, du 15 décembre 2006
au 20 avril 2008, en **six états distincts** (empreintes différentes). Ils sont rangés dans
`codes_tva/docfiscale_minfinances_html/` avec un `MANIFESTE.csv`.

| Fichier `tva_dc_ar_<horodatage>.htm` | Octets | Tableaux | Ce que l'état porte (relevé dans le texte) |
|---|---|---|---|
| `20061215202319` | 1 069 356 | A, B, B bis, **C** | Taux de 29 % et de 10 % ; aucune mention de la loi n° 2006-80. **Tableau C entier, avec les numéros du tarif** (environ 220 lignes à numéro), précédé de la liste des textes qui l'ont modifié (ci-dessous) |
| `20070216012243` | 1 115 775 | A, B, B bis ; C retiré | Loi n° 2006-80 et LF 2007 (loi n° 2006-85) portées ; taux de 12 % |
| `20070410152704` | 1 112 094 | idem | même contenu de lois citées que le précédent (non comparé mot à mot) |
| `20070510231003` | 1 137 275 | idem | idem ; mise en page différente |
| `20071213043909` | 1 041 434 | idem | idem |
| `20080420131808` | 1 032 547 | A, B, B bis ; C retiré | **LF 2008 portée au moins en partie** : dans les tableaux, deux notes la citent — « ajouté par l'article 39 de la LF 2008 » (n° 9 bis du tableau A) et « modifié par l'article 21 de la LF 2008 » ; le n° 9 du tableau A diffère de l'état de décembre 2007. L'article 17, que les recueils privés donnent aussi, n'est pas retrouvé sous la mention « LF 2008 » ; l'article 58 de la loi n° 2007-70 est cité, hors tableaux, dans la liste des textes du droit de consommation |

Rubriques, pour les six : éditeur — ministère des finances (site documentaire, documentation
fiscale) ; date portée par le document — **aucune**, seul l'horodatage de capture est sûr ; langue —
arabe ; couche texte — HTML en UTF-8, sans caractère de remplacement dans le premier état ; tableau
A — numéros 1 à 50 tous présents avec les bis dans l'état de 2006 (les n° 17 à 19 y sont écrits
« 1 7 », « 1 8 », « 1 9 », vus dans le texte) ; tableau B — § I n° 1 à 12 et § II repérés ; tableau B bis repéré ; notes entre
parenthèses par numéro, avec l'article et la loi (48 lignes annotées dans le tableau A de 2006).
Adresse d'origine : `http://documentation.finances.gov.tn/ar/documentation/Explore/article.asp?affTout=yes&id=2` ;
adresses d'archive et SHA-256 au manifeste.

**La liste officielle des textes ayant modifié le tableau C**, telle que l'état du 15 décembre 2006
la donne en tête du tableau (transcrite de l'arabe, à relire) : LF 1989 (loi n° 88-145), art. 25 et
26 ; LF 1991 (loi n° 90-111), art. 35 et 36 ; LF 1992 (loi n° 91-98), art. 37, 38 et 43 ; LF 1993
(loi n° 92-122), art. 83, 84, 94 et 119 ; LF 1994 (loi n° 93-125), art. 51 ; LF 1995 (loi
n° 94-127), art. 86 ; LF 1998 (loi n° 97-88), art. 27 ; LF 2000 (loi n° 99-101), art. 48 ; LF 2005
(loi n° 2004-90), art. 71. C'est le plan de lecture de l'histoire du tableau C. Elle ne nomme ni la
LF 1996 ni les tableaux « M bis », « P » et « L » : à rapprocher de la note des tableaux, qui les
tient pour des listes de retrait : écart à instruire, non tranché ici.

**Rapprochement fait avec le tableau C de l'édition 2016** (numéros du tarif extraits des deux
couches texte, ordre des deux groupes de chiffres neutralisé parce que l'arabe l'inverse) : 212
lignes à numéro dans l'état officiel de décembre 2006, 211 dans l'édition 2016 ; 209 positions
distinctes de part et d'autre, dont **206 communes**. Les trois écarts de chaque côté (02-27,
66-02 et 66-03 d'un côté ; 02-07, 91-11 et 91-13 de l'autre) ont l'allure de coquilles et restent à
lire. L'édition 2016 réimprime donc, à trois lignes près, la consolidation que le ministère
publiait en décembre 2006. Cela ne prouve pas que cette consolidation porte tous les retraits de
1989 à 2000 : le volume reste proche de celui de 1988 (un peu plus de 210 lignes), et l'épreuve du
§ 3 — chercher des numéros retirés par une loi donnée — reste à faire, désormais sur une source
officielle.

Autre acquis : **provenance officielle de l'édition 2016**. Le fichier `code_tva_2016_fr.pdf`, pris
en première passe sur un site de cabinet, est octet pour octet celui que servait
`legislation.tn/en/codes-en-vigueur/96__fr` le 13 août 2016 (même SHA-256, `77203067…48c8bfb`) :
`https://web.archive.org/web/20160813024016id_/http://www.legislation.tn:80/en/codes-en-vigueur/96__fr`.

### 8.2 Verdict site par site

| Site | Verdict | Preuve |
|---|---|---|
| `documentation.finances.gov.tn` (2006-2012), version arabe | **Oui** : six états, décembre 2006 à avril 2008, A, B, B bis, et C dans le premier ; téléchargés | § 8.1 |
| `documentation.finances.gov.tn`, version française (2006-2008) | **Indéterminé** : le site publiait le recueil, la page n'est pas archivée | Le portail y renvoie en 2008 ; le service d'archives répond 404 pour l'adresse, et n'a de la page française que 30 captures en erreur 500 de l'adresse sans paramètre |
| `documentation.finances.gov.tn` et `documentations.finances.gov.tn/dgelf` (2009-2016, version PHP) | **Indéterminé** | Menu « TVA et DC » archivé en 2009, 2012, 2013, 2015 ; le contenu, chargé par formulaire dans un cadre, n'est archivé à aucune date |
| `www.impots.finances.gov.tn` (2003-2018) | **Non**, le site ne publiait pas le code | Rubrique « Documentation » ouverte dans l'archive (`documentation.htm`, septembre 2003 ; `docutxt.htm`, février 2004 ; `doc_fisc_fr.htm`, décembre 2005), adresses listées jusqu'en 2016 : fiches de présentation par impôt (`impots_fr/tva_fr_1…16.htm`), notes communes en PDF, formulaires ; aucun code. 6 207 adresses archivées ; seuls fichiers d'archive : deux `.zip` de schémas de la liasse fiscale |
| `portail.finances.gov.tn` (2008-2016) | **Non** pour le code de la TVA ; renvoi vers le site documentaire | Rubrique « cadre légal — fiscalité » de 2008 : sept liens, tous vers `documentation.finances.gov.tn`. Seuls le code d'incitation aux investissements, le code des assurances et le code de la comptabilité publique y sont en PDF |
| `www.finances.gov.tn` (2012-2016) | **Non** | Catégorie de téléchargements « Fiscalité » (2013, 2014, 2015) : « Différents impôts », « Télédéclaration », « Dépôt sur support magnétique », « Contrôle fiscal », « Téléliquidation » ; pas de code. Premier code en PDF : « CODE TVA 2017 FR » |
| `mfdi.gov.tn` | **Non couvert** | Quatre réponses vides du service d'archives |
| `www.iort.gov.tn` (Imprimerie officielle, 2009-2019) | **Indéterminé** | Le site avait des rubriques « CodesJuridiques » (3 396 adresses archivées), « PageModificationsCodes », « CodesJuridiquesRecueils », « CodesJuridiquesAbroge » ; c'est une application à session : toutes les captures ouvertes sont des messages de déconnexion de moins de 1 Ko, aucune ne porte de contenu. Un seul PDF archivé sur le domaine (la Constitution) |
| `www.legislation.tn` (2013-2020) | **Indéterminé avant 2016** ; oui à partir de 2016 | Le code de la TVA figure dans la liste « codes en vigueur » dès la capture du 28 décembre 2013 (identifiant 96). Premières captures du code : PDF le 13 août 2016 (édition 2016), pages par article à partir du 7 juillet 2016 ; rien avant |
| `douane.gov.tn`, `cepex.nat.tn`, `tunisieindustrie.nat.tn`, `investintunisia.tn`, `e-justice.tn`, `cnudst.rnrt.tn` | **Non** | Aucune adresse archivée ne porte le code ; douane : pages de présentation du tarif à partir de 2018 seulement. `apii.tn` : réponses vides, non couvert |
| `jurisitetunisie.com/tunisie/codes/_instances/` | sans objet | 17 pages de lois, dont L1988-0145 et L2001-0123 ; non ouvertes |

### 8.3 Adresses mortes, utiles si l'on écrit un jour à l'administration

- `http://documentation.finances.gov.tn/documentation/Explore/article.asp?affTout=yes&id=1460` —
  recueil « TVA et droit de consommation » en français, 2006-2008. L'identifiant est établi par le
  libellé du lien dans la rubrique du portail (capture de 2008) : « 1. Recueil du code de la Taxe
  sur la Valeur Ajoutée et du droit de consommation ».
- `http://documentation.finances.gov.tn/cadre_principal_documentation.php?root=TVA et DC` et
  `http://documentations.finances.gov.tn/dgelf/cadre_principal_documentation.php?root=TVA et DC`
  (et `…_ar.php?root=TVA+et+DC&rooot_ar=2`) — le même recueil, version de 2009 à 2016.
- `http://www.legislation.tn/fr/codes-en-vigueur/96__fr` et `…/96__ar` — le PDF du code servi par le
  portail legislation.tn ; le code figure dans la liste du portail dès décembre 2013, mais ce qui
  était servi à ces adresses avant août 2016 n'est pas connu.
- `http://www.iort.gov.tn/WD120AWP/WD120Awp.exe/CONNECT/SITEIORT`, rubriques « Codes juridiques »
  et « Modifications des codes ».

### 8.4 Ce que cela change pour les colonnes 2008 et 2014 de la vue par catégories

- **Colonne 2008** : elle peut désormais se contrôler sur une source **officielle**, l'état du
  20 avril 2008 du recueil du ministère, qui porte la LF 2008 au moins pour ses articles 21 et 39
  (l'article 17 reste à y retrouver). Il est en arabe : le contrôle porte
  sur la présence, le numéro et le régime de chaque opération, non sur la lettre des libellés
  français, qui restent ceux du recueil privé. L'état du 15 décembre 2006 offre en plus une colonne
  officielle « fin 2006 », la dernière avec le tableau C et le taux de 10 %.
- **Colonne 2014** : rien d'officiel n'est retrouvé entre avril 2008 et février 2016 ; elle reste
  lue sur le recueil privé de janvier 2014.
- **Tableau C** : la réserve du § 3 demeure, mais change d'objet. Le ministère publie en décembre
  2006 un tableau C consolidé avec la liste de ses modifications, et l'édition 2016 le reprend à
  trois lignes près (§ 8.1) ; il reste à vérifier que les retraits y sont portés et à le rapprocher
  de la transcription de 1988.

### 8.5 Requêtes de la seconde passe (rejouables)

| Requête | Résultat |
|---|---|
| CDX `url=<domaine>&matchType=domain&collapse=urlkey&filter=statuscode:200&limit=150000`, sans filtre de type | impots.finances.gov.tn : 6 207 ; finances.gov.tn (tous sous-domaines) : 41 581 ; portail.finances.gov.tn : 13 695 ; mfdi.gov.tn : vide quatre fois ; iort.gov.tn et legislation.tn : **tronqués à 150 000**, repris par requêtes ciblées |
| Recherche dans ces listes de « code », « tva », « taxe », « legis », « textes », « tableau », « annexe », « majall », « adaa », « fiscal » | révèle les sous-domaines `documentation`, `documentations`, `doc-fiscale` (2017 et après) ; aucun fichier bureautique ou archive de code |
| CDX `url=documentation.finances.gov.tn&matchType=domain`, toutes captures | 1 325 lignes ; 199 captures de `article.asp` en 200, 88 en 500 |
| Pages ouvertes dans l'archive : index et menu du site documentaire (2006, 2009, 2012, 2015) ; `impots…/documentation/documentation.htm`, `docutxt.htm`, `doc_fisc_fr.htm` (2003-2005) ; `portail…/cadrelegal.php?dom=FISC` (2008) ; `www.finances.gov.tn/index.php?option=com_jdownloads&view=viewcategory&catid=12` (2013, 2014, 2015) ; `legislation.tn/fr/recherche/codes-en-vigueur` (2013, 2016) ; deux pages « CodesJuridiques » de l'IORT (2010) | § 8.2 |
| CDX iort.gov.tn, filtres `original:.*[Cc][Oo][Dd][Ee].*` (4 262), `.*[Tt][Vv][Aa].*` (74, faux positifs d'identifiants de session), hors HTML et images (83) | aucune page de plus de 3 Ko, aucun PDF de code |
| CDX legislation.tn : préfixe `sites/default/files/codes/` (445 captures, 2014-2026 ; TVA à partir de 2018) ; filtre `codes` (734) ; filtre `affich-code.*(valeur\|__96\|taxe)` (5 872 ; TVA : 31 en 2016, rien avant) | § 8.2 |
| CDX douane, apii, cepex, tunisieindustrie, investintunisia, e-justice, cnudst, filtre « tva, code, tarif, fisc, taxe, recueil » | rien d'utile ; apii.tn vide trois fois |
| Recherche web en arabe : « مجلة الأداء على القيمة المضافة » avec « المطبعة الرسمية » et « منشورات المطبعة الرسمية للجمهورية التونسية », années 2009 à 2015 | éditions 2025 (jibaya.tn) et pages actuelles de legislation.tn, 9anoun.tn, diwan.tn ; aucune édition arabe antérieure à 2016 |

Non faits : les autres services d'archives (archive.today, Common Crawl) pour l'adresse française
`id=1460` ; les recueils voisins du même site (`id=7`, `id=9`, archivés en arabe et non identifiés) ;
la lecture à l'œil des six états arabes. Le recueil `id=9` est celui des notes communes (vu) ;
`id=7`, d'après le menu, celui des textes non incorporés aux codes.

Anciens noms de domaine du ministère : les pages d'accueil archivées (impots, 2003 et 2004 ;
portail, 2008 ; `www.finances.gov.tn`, une seule capture rendue pour 2006 et 2012) ne renvoient
qu'aux hôtes déjà couverts, plus `amendes.finances.tn`. Première capture par hôte :
`www.impots.finances.gov.tn` en septembre 2003, `documentation.finances.gov.tn` en janvier 2006,
`www.finances.gov.tn` en novembre 2007, `www.portail.finances.gov.tn` en février 2008. Rien n'est
donc archivé du ministère avant septembre 2003 sous ces noms ; le domaine `finances.tn` et un
éventuel hébergement antérieur (pages ministérielles du portail du gouvernement) ne sont pas
couverts.

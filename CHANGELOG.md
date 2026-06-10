# Changelog

## [1.3.1](https://github.com/benjello/precis-socio-fiscal-tunisie/compare/v1.3.0...v1.3.1) (2026-06-10)


### 🐛 Corrections de bugs

* **ar:** libellés d'interface Quarto en arabe (TOC, éditer, signaler) ([e7b1233](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/e7b123346e45f83cf55d3437089cd5ad95abc12f))
* **ar:** mise en page RTL du livre arabe (titres et texte alignés à droite) ([bfb54e5](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/bfb54e572e6819f00675508ed7c823449ec73eea))
* **biblio:** titres arabes pour les références juridiques (references.json AR) ([410c10d](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/410c10dbe37c9fe34ef94e35833d4877a4ef02c1))
* **ci:** translation-sync ne propage que FR→AR (même en PR) ([ef51b3b](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/ef51b3b877ee2997cad57136f96be5ac952fc3bc))

## [1.3.0](https://github.com/benjello/precis-socio-fiscal-tunisie/compare/v1.2.0...v1.3.0) (2026-06-10)


### ✨ Nouveautés

* add public sector remuneration précis (fr + ar) ([ef86710](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/ef867104a1215e087ec0d4e62526281867a4b185))
* alphabetical sorting of FR/AR glossaries ([a8084ca](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/a8084ca2bddc51326af935d9c826a9bd52ae95c2))
* architecture donnees/figures - paquet tunisia_data + figures par livre ([2ce8fc5](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/2ce8fc5331b8551b49bfcc139218666f816a8bc2))
* **ar:** figure structure par catégorie statutaire (chunk arabe + figdata) ([cd82b9f](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/cd82b9f29c0aba51febd954e2dbd55b083816009))
* bilingual glossary from single source + translation-pipeline bijection ([cd9e479](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/cd9e479bd7870dbad71f2cd4a9c914e583ff65ef))
* composant generique figure a onglets (Graphique / Donnees exportable) ([bf20486](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/bf20486f3f47c5752b57b4f46fb6463233a1c851))
* glossary sync lock + optional canonical sources ([66466c0](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/66466c0d6ff525e4890d1bf8f7df62db151a9422))
* **i18n:** figures/tableaux/chrome traduits (AR) + biblio AR + liens corrigés ([736d1a2](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/736d1a25fc990cad4a97baa8e6153636e465dc89))
* **i18n:** onglet Sources entièrement traduit en arabe (provenance bilingue) ([1e83519](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/1e83519c9568734dedcad4576dc17633141b9719))
* Phase 0 editorial agent system (documentaliste, redacteur, terminologue) + /rediger ([a04405b](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/a04405b09134f3dc143952c911373a7138cab8f4))
* **remunerations:** figure structure par catégorie statutaire (INS tab8) ([3af26ff](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/3af26ffce9e9818fb496afcb7ae26be6da7eee16))
* **remunerations:** figures sourcées (effectifs FP, masse salariale) + biblio + build autonome ([308bbd0](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/308bbd0f5eebef74cb43e84dc3ec66450689ce15))
* **remunerations:** rédige B.1 — chapitre régime indiciaire ([#8](https://github.com/benjello/precis-socio-fiscal-tunisie/issues/8)) ([6fc489c](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/6fc489ca3c593cc3230890070e7f4240a01705a6))
* **remunerations:** régime indiciaire — champ d'application par sous-secteur (État/CL/EPA) ([3c9145d](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/3c9145de6adaedc2e499b0ec44956ddb10074755))


### 🐛 Corrections de bugs

* **ar:** câble les chapitres de régime dans le livre AR + coupe la boucle de rétro-traduction ([e00d102](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/e00d1026a1280288a5cd250f9edc1d0d67ffc526))
* **ar:** rend les figures disponibles au livre arabe (build Pages) ([4e6e49c](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/4e6e49c90dc8dec7ce9b057b8054dd33e9ff9841))
* **biblio:** liens législatifs cassés -&gt; PDF officiels JORT ([858dafe](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/858dafe761b075c270f8cdf561d62894b0bb9ea9))
* **biblio:** références AR pointent vers le JORT arabe (pdf_ar) sur pist.tn ([84b94b2](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/84b94b26effbc3d6e9942ca67f5ececa6fbdc186))
* **ci:** retry avec backoff sur 503/429 dans translate_sync ([31dee33](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/31dee338e25c7eb4208535d84eda27e6715cf842))


### 📝 Documentation

* **biblio:** signale au bibliographe les cles dataset (sources de donnees) a creer dans Zotero ([5488e9d](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/5488e9df06b73e2b58dd384cdf747c551ce01f55))
* fold per-regime history/budget repères into chapter intros (fr) ([a13cbcb](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/a13cbcbb9047a93427ceb00bc7ee49ab429abf6c))
* fold rémunération structure into régimes section (fr) ([fbc740d](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/fbc740da3ef77e3e12884219f1cec748965de75d))
* implement intro (perimeter funnel) and regime chapter trame (fr) ([bf83424](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/bf834242145aa4df5e6009e3357ad55afea83437))
* move history and wage-bill into intro as transversal themes (fr) ([438d284](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/438d2846739964a35ff28ee800a03cd4977e4f83))
* **notes:** sourced note on aggregate public wage bill for A.2 ([#6](https://github.com/benjello/precis-socio-fiscal-tunisie/issues/6)) ([d0b50cf](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/d0b50cff873077656e8cbd637274ffdeff3f26a5))
* **precis:** consolide A.5 — annonce des régimes de rémunération ([#7](https://github.com/benjello/precis-socio-fiscal-tunisie/issues/7)) ([4b52ced](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/4b52ced9bfe7b28af1ecc6972618b1fd90af8b59))
* **precis:** précise la nature juridique des EP non financières (A.5) ([9a48842](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/9a48842621e0e915ca2ab36500810d4136fff75f))
* split précis into introduction and per-regime chapters (fr) ([9f31861](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/9f31861774c1e797ce33f6f550b5b94b4050a6fb))
* write intro and section outline for public remuneration précis (fr) ([860ef52](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/860ef5239a931d7f11dc2b53fdb44f088cd0caa9))

## [1.2.0](https://github.com/benjello/precis-socio-fiscal-tunisie/compare/v1.1.0...v1.2.0) (2026-04-28)


### ✨ Nouveautés

* add Zotero bibliography sync with CSL-JSON fallback ([f3bd49c](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/f3bd49c09bb33e747ccad3991e947d5149825016))
* Zotero bibliography with citation keys, URL checks, and proper citations ([2034bdc](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/2034bdca19e674c384943e19affba34cac89febb))


### 🐛 Corrections de bugs

* add fiscalite to build and restore landing page links ([13138e4](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/13138e46e50155ec3534bc2f941f202dd01ad31e))

## [1.1.0](https://github.com/benjello/precis-socio-fiscal-tunisie/compare/v1.0.0...v1.1.0) (2026-04-27)


### ✨ Nouveautés

* add fiscalité précis skeleton and fix CI translation pipeline ([8e48713](https://github.com/benjello/precis-socio-fiscal-tunisie/commit/8e48713e32322972e118f9b28dec12a14fc241c2))

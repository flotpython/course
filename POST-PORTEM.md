<!--- -*- coding: utf-8 -*- --->

Plateforme
=======

* Prévoir des mécanismes plus conviviaux pour échanger le code (miniprojets) - étudier un mini-github

* montrer dans une vidéo comment publier du code
  * l'icone '010010' dans la barre de menu
  * Control-K
  * les back quotes `x`
  * 4 espaces
  * parler aussi de la possibilité de publier les notebooks (liens statiques)
  * et donc du point précédent (un site pour exposer le code ?)

* peut-on faire du peer-review sur des miniprojets ?


Général
=======

* classes new-style
  * trop de décalage dans le temps entre le cours semaine 5
     et celui de la semaine 7

* équilibre cours
   * la semaine 2 est très chargée
   * les libellés des différentes semaines sont imprécis

* équilibre cours - suite
  * essayer de parler de plus de librairies standard

* exercices sans doute trop difficiles en moyenne
   on observe un taux de 1 succès pour 3 échecs dans les stats

* les quelques séquences qui ont 2 vidéos : des gens sont arrivés à
   rater la deuxième; il suffirait de reprendre un peu la présentation
   pour rendre ça + explicite (un message AVANT la première vidéo).

* alléger data/ as far as possible

* la mise à disposition au format html
   * il faut penser aux accessoires (surtout media/ et peut-être
   data/ - sachant que dans data/ on a les cities*.json qui prennent
   dans les 140 Mb à eux tous seuls)
   * ce serait bien si les cellules pouvaient être évaluées avant de
     générer le html - mais ça semble peut-être un peu dur à faire

* minor: bisect the repo to find out about this
   "nous dirons plus tard que les variables référencent le même objet" thing
   when was it written, by whom, did valerie let this pass ?

W1
===

 * installation sur windows
   * donner un peu plus d'indications a propos du PATH
   * idem peut-être pour le shebang sur windows

W2
===

 * Le quiz sur les listes et la copie avec `3 * [[0]]` est assez foireux
   il faudrait le supprimer ou le récrire avec un exemple plus
   pertinent - c'est-à-dire sans le `*`

 * W2S8 - l'exercice 'affichage' donne un résultat discutable pour Ted Mosby,
   * le dernier champ étant vide on pourrait s'attendre à afficher ??
   * d'ailleurs la mise en page sur la plateforme pourrait être améliorée,
     comme de toutes façons on se retrouve avec 2 lignes par input
     autant ne pas abréger c'est inutile et confusant

 * le quiz sur le formattage des strings, et "dans du code nouveau"
   a suscité pas mal d'émoi, il faudrait préciser mieux l'histoire
   des `%` qu'on ne compte pas comme corrects.

W3
===

 * W3S2 - dans le quiz on propose une option qui est `'marc' in annuaire and annuaire['marc']`
   quelqu'un remarque que ceci renvoie False au lieu de None
   il faudrait mettre ça en contexte

 * W3S6 dans le notebook la section sur le short-circuit est foireuse,
   il faudrait des trucs + simples comme tout simplement
   True and 0/0
   False and 0/0
   qui est bcp + clair à comprendre - plutot que ces pop() qui sont confusants

 * W3S2 l'exo sur les bateaux (abbreviated et extended et les dictionnaires)
   semble être trop raide pour certains
   j'ai rangé dans la branche 'exo' une version 2.0 de cet exercice
   qui se décline en deux versions basique et intermédiaire

W4
===

 * W4S8 dans doubler_premier il faudrait au moins une fonction
   non-associative - la fonction distance est en fait associative ! Du
   coup les gens utilisent reduce et trouvent un résultat légèrement différent.

W7
===
 * le complément sur les décorateurs : plutoôt que de rediriger vers
   https://wiki.python.org/moin/PythonDecoratorLibrary#Singleton à la
   fin, ce serait mieux de le refaire en le commentant; rien que
   d'utiliser des noms un peu moins space ça va rendre le tout déjà beaucoup + lisible.


Exos
===

* shipdict.py - il faudrait enlever les doublons (même mesure dans 2
  fichiers) - voir bateaux "ENFORCER" et le "SANTA CRUZ" d'après un
  post étudiant

* prévenir + clairement la toute première fois qu'on fait un exo sur
  les bateaux qu'il peut y avoir des bateaux de même nom


Notebooks et process
====================
 * un bouton pour faire kernel_restart + clear_all_cells + run_all_cells serait très appréciable
 * un bouton pour faire clear_all_cells + remove_empty_cells serait très appréciable
 * avoir git mieux intégré à IPython serait cool
 * un outil dans IPython pour gérer les annotations (notebookname et version)
 * comprendre les signatures entre mac et windows
 * revoir l'utilisation de RawNbConvert
   * a. dans l'état, on n'utilise que le rendu html dans le notebook qui est plutôt sympa
   * b. il y a d'autres voies pour rendre la même chose (genre 'code' avec les 4 espaces en markdown)
   * avec a. on a un html sympa, mais tous les nbconvert sont pourris (on ne peut pas lancer latex par exemple)
   * avec b. c'est mieux pour les exports mais c'est dommage de perdre le rendu
   * j'ai essayé plusieurs voies pour essayer d'obtenir le même rendu
   avec un autre type que RawNbConvert mais sans succès. par exemple
   si je mets moi-meme un `<pre>` avec un `style=` dans un markdown,
   le style ne passe pas très bien (apparemment certains flags css passent et d'autres non...)
   * trouver un autre rendu permettrait d'éditer du pdf plus fidele.
 * produire les PDFs localement et du coup produire des bundle (tar ou
   zip) par semaine

 * ce serait bien si on pouvait lier les notebooks entre eux (mettre des URLs de l'un vers l'autre)
   * apparemment c'est possible déjà sauf que MH ne m'a pas passé la recette magique.
   * dans tous les cas il faudrait dans ce cas garder le libellé de la référence (Semaine x Séquence y)
   * XXX: à bien y réfléchir, c'est très casse gueule car ça rend le
     notebook dépendant du 'run' FUN, c'est sûrement une idée à la
     noix en fait.

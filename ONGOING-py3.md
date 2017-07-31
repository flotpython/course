# missing

* f-strings
* `pathlib`

* check all hrefs to python docs in section /2/ -> /3.5/
* remove most calls to `from __future__ import print_function`

## compréhensions

`w2-s7-c2-comprehension-de-liste` et `w4-s4-c1-comprehensions-imbriquees` ont un overlap non vide, les compréhensions imbriquées.

## `w3-s8-c4-iterateurs-et-performances`

A besoin d'être repris

* on peut garder l'idée d'introduire les différentes méthodes de benchmarking
* ajouter d'ailleurs les magics jupyter `%timeit` ou `%%timeit`
* mais il faudra à cous sûr séparer ça de l'histoire des itérateurs qui sera forcément abordé ailleurs/avant ?

On pourra découper en deux notebooks distincts:

* `w3-s8-c4-performances`
  * pure python: `time.time()` et le module `timeit`
  * https://docs.python.org/3.5/library/timeit.html
  * ipython: `%time` et `%timeit`
  * http://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-time

* `w3-s8-c4bis-iterateurs`
  * pas très sûr si ça a encore du sens de toutes façons..

## `w3-s8-c5-iterable-vs-iterateur`

* J'ai écrit au départ ce notebook parce qu'Arnaud avait beaucoup mélangé itérable et itérateur dans la vidéo
* on n'aura pas forcément besoin de le préserver

## `w4-s1-c2-utilitaires-sur-fichiers`

* ceci est presque entièrement obsolète, il faut faire la promo de `pathlib` en indiquant que c'est standard à partir de 3.4 (et dispo sur pypi pour les versions précédentes)

## `w4-s6-c2-exception-unboundlocalerror`

* faut-il introduire `nonlocal` ?

## `w4-s8-c1-passage-arguments`

* très vague
  * ne fait pas la différence entre paramètre et argument,
  * ne détaille pas comment les associations sont faites
* p.r. à python3, manque
  * le fait que l'on peut mettre un * avant des paramètres nommés
* envisager de le couper en deux ?

## `w5-s1-c2-fonctions-globals-et-locals`

* je mentionne les f-strings, qui ne sont décrits nulle part encore
* je donne un petit exemple avec les f-strings

## `w5-s3-c1-import-as`

* il semble qu'il y a ici des redites par rapport à des choses vues en semaine 3 (`import as`)

## `w5-s6-c2-surcharge-operateurs-2`

* 2ème tiers: on introduit `__getattr__` en suggérant que c'est la seule façon de customiser `obj.attribute`; selon ce qu'on décide de faire par rapport aux `__get__`, `__getattribute__`, et autres, il faudra rectifier ça...

## `w5-s8-c1-espaces-de-nommage`

Le complément avancé dans ce notebook ne me paraît pas forcément très utile, et de plus je ne sais pas dire s'il est toujours réellement courant; cette histoire de `global` et `nonlocal` ne m'inspire pas vraiment de toutes les façons..

# mini-projets

## `diskusage`

* pourrait constructivement utiliser `pathlib` plutôt que ces vieux trucs

## `crawler`

* laissé en python2

# commentaires généraux

## CLASSES

* il manque cruellement un complément sur les properties
* je supprime entièrement `w5-s5-c2-classes-new-style.ipynb` qui n'est plus pertinent en python3.


## Type hints
* un impact sans doute sur le ou les compléments `w5-s5-c3-heritage-multiple` et/ou `w5-s5-c4-heritage-typage`


## divers

* renommer `w5-s6-e2-classes` en `w5-s6-e2-classes-shipdict` ?
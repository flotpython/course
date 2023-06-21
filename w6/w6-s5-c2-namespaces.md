---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
nbhosting:
  title: Espaces de nommage
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Espaces de nommage

+++

## Complément - niveau basique

+++

Nous venons de voir les règles pour l'affectation (ou l'assignation) et le référencement des variables et des attributs ; en particulier, on doit faire une distinction entre les attributs et les variables.

+++

* Les attributs sont résolus de manière **dynamique**, c'est-à-dire au moment de l'exécution (*run-time*) ;
* alors que la liaison des variables est par contre **statique** (*compile-time*) et **lexicale**, en ce sens qu'elle se base uniquement sur les imbrications de code.

+++

Vous voyez donc que la différence entre attributs et variables est fondamentale. Dans ce complément, nous allons reprendre et résumer les différentes règles qui régissent l'affectation et le référencement des attributs et des variables.

+++

##### Attributs

+++

Un attribut est un symbole `x` utilisé dans la notation `obj.x` où `obj` est l'objet qui définit l'espace de nommage sur lequel `x` existe. 

L'**affectation** (explicite ou implicite) d'un attribut `x` sur un objet `obj` va créer (ou altérer) un symbole `x` **directement** dans l'espace de nommage de `obj`, symbole qui va référencer l'objet affecté, typiquement l'objet à droite du signe `=`

```{code-cell} ipython3
class MaClasse:
    pass

# affectation explicite
MaClasse.x = 10 

# le symbole x est défini dans l'espace de nommage de MaClasse
'x' in MaClasse.__dict__
```

Le **référencement** (la lecture) d'un attribut va chercher cet attribut **le long de l'arbre d'héritage** en commençant par l'instance, puis la classe qui a créé l'instance, puis les super-classes et suivant la MRO (voir le complément sur l'héritage multiple).

+++

##### Variables

+++

Une variable est un symbole qui n'est pas précédé de la notation `obj.` et l'affectation d'une variable rend cette variable locale au bloc de code dans lequel elle est définie, un bloc de code pouvant être :

* une fonction, dans ce cas la variable est locale à la fonction ;
* une classe, dans ce cas la variable est locale à la classe ;
* un module, dans ce cas la variable est locale au module, on dit également que la variable est globale.
 
Une variable référencée est toujours cherchée suivant la règle LEGB :

* localement au bloc de code dans lequel elle est référencée ;
* puis dans les blocs de code des **fonctions ou méthodes** englobantes, s'il y en a, de la plus proche à la plus eloignée ;
* puis dans le bloc de code du module.
 
Si la variable n'est toujours pas trouvée, elle est cherchée dans le module `builtins` et si elle n'est toujours pas trouvée, une exception est levée.

Par exemple :

```{code-cell} ipython3
var = 'dans le module'

class A:
    var = 'dans la classe A'
    def f(self):
        var = 'dans la fonction f'
        class B:
            print(var)
        B()
A().f()
```

##### En résumé

+++

Dans la vidéo et dans ce complément basique, on a couvert tous les cas standards, et même si python est un langage plutôt mieux fait, avec moins de cas particuliers que d'autres langages, il a également ses cas étranges entre raisons historiques et bugs qui ne seront jamais corrigés (parce que ça casserait plus de choses que ça n'en réparerait). Pour éviter de tomber dans ces cas spéciaux, c'est simple, vous n'avez qu'à suivre ces règles :

* ne jamais affecter dans un bloc de code local une variable de même nom qu'une variable globale ;
* éviter d'utiliser les directives `global` et `nonlocal`, et les réserver pour du code avancé comme les décorateurs et les métaclasses ;
* et lorsque vous devez vraiment les utiliser, toujours mettre les directives `global` et `nonlocal` comme premières instructions du bloc de code où elle s'appliquent.
 
Si vous ne suivez pas ces règles, vous risquez de tomber dans un cas particulier que nous détaillons ci-dessous dans la partie avancée.

+++

## Complément - niveau avancé

+++

##### La documentation officielle est fausse

+++

Oui, vous avez bien lu, la documentation officielle est fausse sur un point subtil. Regardons le [modèle d'exécution](https://docs.python.org/3/reference/executionmodel.html), on trouve la phrase suivante "If a name binding operation occurs anywhere within a code block, all uses of the name within the block are treated as references to the current block." qui est fausse, il faut lire "If a name binding operation occurs anywhere within a code block **of a function**, all uses of the name within the block are treated as references to the current block." 

En effet, les classes se comportent différemment des fonctions :

```{code-cell} ipython3
x = "x du module"
class A():
    print("dans classe A: " + x)
    x = "x dans A"
    print("dans classe A: " + x)
    del x
    print("dans classe A: " + x)
```

Alors pourquoi si c'est une mauvaise idée de mélanger variables globales et locales de même nom dans une fonction, c'est possible dans une classe ?

Cela vient de la manière dont sont implémentés les espaces de nommage. Normalement, un objet a pour espace de nommage un dictionnaire qui s'appelle `__dict__`. D'un côté un dictionnaire est un objet python qui offre beaucoup de flexibilité, mais d'un autre côté, il induit un petit surcoût pour chaque recherche d'éléments. Comme les fonctions sont des objets qui par définition peuvent être appelés très souvent, il a été décidé de mettre toutes les variables locales à la fonction dans un objet écrit en C qui n'est pas dynamique (on ne peut pas ajouter des éléments à l'exécution), mais qui est un peu plus rapide qu'un dictionnaire lors de l'accès aux variables. Mais pour faire cela, il faut déterminer la portée de la variable dans la phase de précompilation. Donc si le précompilateur trouve une affectation (explicite ou implicite) dans une fonction, il considère la variable comme locale pour tout le bloc de code. Donc si on référence une variable définie comme étant locale avant une affectation dans la fonction, on ne va pas la chercher globalement, on a une erreur `UnboundLocalError`.

Cette optimisation n'a pas été faite pour les classes, parce que dans l'évaluation du compromis souplesse contre efficacité pour les classes, c'est la souplesse, donc le dictionnaire qui a gagné.

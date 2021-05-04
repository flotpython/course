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
notebookname: "H\xE9ritage"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Héritage

+++

## Complément - niveau basique

+++

La notion d'héritage, qui fait partie intégrante de la Programmation Orientée Objet, permet principalement de maximiser la **réutilisabilité**. 

Nous avons vu dans la vidéo les mécanismes d'héritage *in abstracto*. Pour résumer très brièvement, on recherche un attribut (pour notre propos, disons une méthode) à partir d'une instance en cherchant :

* d'abord dans l'instance elle-même ;
* puis dans la classe de l'instance ;
* puis dans les super-classes de la classe.

+++

L'objet de ce complément est de vous donner, d'un point de vue plus appliqué, des idées de ce que l'on peut faire ou non avec ce mécanisme. Le sujet étant assez rabâché par ailleurs, nous nous concentrerons sur deux points :

* les pratiques de base utilisées pour la conception de classes, et notamment pour bien distinguer **héritage** et **composition** ;
* nous verrons ensuite, sur des **exemples extraits de code réel**, comment ces mécanismes permettent en effet de contribuer à la réutilisabilité du code.

+++

### Plusieurs formes d'héritage

+++

Une méthode héritée peut être rangée dans une de ces trois catégories :

* *implicite* : si la classe fille ne définit pas du tout la méthode ;
* *redéfinie* : si on récrit la méthode entièrement ;
* *modifiée* : si on récrit la méthode dans la classe fille, mais en utilisant le code de la classe mère.

+++

Commençons par illustrer tout ceci sur un petit exemple :

```{code-cell} ipython3
# Une classe mère
class Fleur:
    def implicite(self):
        print('Fleur.implicite')
    def redefinie(self):
        print('Fleur.redéfinie')
    def modifiee(self):
        print('Fleur.modifiée')

# Une classe fille
class Rose(Fleur):
    # on ne définit pas implicite
    # on rédéfinit complètement redefinie
    def redefinie(self):
        print('Rose.redefinie')
    # on change un peu le comportement de modifiee
    def modifiee(self):
        Fleur.modifiee(self)
        print('Rose.modifiee apres Fleur')
```

On peut à présent créer une instance de Rose et appeler sur cette instance les trois méthodes.

```{code-cell} ipython3
# fille est une instance de Rose
fille = Rose()

fille.implicite()
```

```{code-cell} ipython3
fille.redefinie()
```

S'agissant des deux premières méthodes, le comportement qu'on observe est simplement la conséquence de l'algorithme de recherche d'attributs : `implicite` est trouvée dans la classe Fleur et `redefinie` est trouvée dans la classe Rose.

```{code-cell} ipython3
fille.modifiee()
```

Pour la troisième méthode, attardons-nous un peu car on voit ici comment *combiner* facilement le code de la classe mère avec du code spécifique à la classe fille, en appelant explicitement la méthode de la classe mère lorsqu'on fait :

```python
Fleur.modifiee(self)
```

+++

##### La fonction *built-in* `super()`

+++

Signalons à ce sujet, pour être exhaustif, l'existence de la [fonction *built-in* `super()`](https://docs.python.org/3/library/functions.html#super) qui permet de réaliser la même chose sans nommer explicitement la classe mère, comme on le fait ici :

```{code-cell} ipython3
# Une version allégée de la classe fille, qui utilise super()
class Rose(Fleur):
    def modifiee(self):
        super().modifiee()
        print('Rose.modifiee apres Fleur')
```

```{code-cell} ipython3
fille = Rose()

fille.modifiee()
```

On peut envisager d'utiliser `super()` dans du code très abstrait où on ne sait pas déterminer statiquement le nom de la classe dont il est question. Mais, c'est une question de goût évidemment, je recommande personnellement la première forme, où on qualifie la méthode avec le nom de la classe mère qu'on souhaite utiliser. En effet, assez souvent :

* on sait déterminer le nom de la classe dont il est question ;
* ou alors on veut mélanger plusieurs méthodes héritées (via l'héritage multiple, dont on va parler dans un prochain complément) et dans ce cas `super()` ne peut rien pour nous.

+++

### Héritage *vs* Composition

+++

Dans le domaine de la conception orientée objet, on fait la différence entre deux constructions, l'héritage et la composition, qui à une analyse superficielle peuvent paraître procurer des résultats similaires, mais qu'il est important de bien distinguer. 

Voyons d'abord en quoi consiste la composition et pourquoi le résultat est voisin :

```{code-cell} ipython3
# Une classe avec qui on n'aura pas de relation d'héritage
class Tige:
    def implicite(self):
        print('Tige.implicite')
    def redefinie(self):
        print('Tige.redefinie')
    def modifiee(self):
        print('Tige.modifiee')

# on n'hérite pas
# mais on fait ce qu'on appelle une composition
# avec la classe Tige
class Rose:
    # mais pour chaque objet de la classe Rose
    # on va créer un objet de la classe Tige
    # et le conserver dans un champ
    def __init__(self):
        self.externe = Tige()

    # le reste est presque comme tout à l'heure
    # sauf qu'il faut definir implicite
    def implicite(self):
        self.externe.implicite()
        
    # on redéfinit complètement redefinie
    def redefinie(self):
        print('Rose.redefinie')
        
    def modifiee(self):
        self.externe.modifiee()
        print('Rose.modifiee apres Tige')
```

```{code-cell} ipython3
# on obtient ici exactement le même comportement 
# pour les trois sortes de méthodes
fille = Rose()

fille.implicite()
fille.redefinie()
fille.modifiee()
```

##### Comment choisir ?

+++

Alors, quand faut-il utiliser l'héritage et quand faut-il utiliser la composition ?  
On arrive ici à la limite de notre cours, il s'agit plus de conception que de codage à proprement parler, mais pour donner une réponse très courte à cette question :

* on utilise l'héritage lorsqu'un objet de la sous-classe **est aussi un** objet de la super-classe (une rose est aussi une fleur) ;
* on utilise la composition lorsqu'un objet de la sous-classe **a une relation avec** un objet de la super-classe (une rose possède une tige, mais c'est un autre objet).

+++

## Complément - niveau intermédiaire

+++

### Des exemples de code

+++

Sans transition, dans cette section un peu plus prospective, nous vous avons signalé quelques morceaux de code de la bibliothèque standard qui utilisent l'héritage. Sans aller nécessairement jusqu'à la lecture de ces codes, il nous a semblé intéressant de commenter spécifiquement l'usage qui est fait de l'héritage dans ces bibliothèques.

+++

##### Le module `calendar`

+++

On trouve dans la bibliothèque standard [le module `calendar`](https://docs.python.org/3/library/calendar.html). 
Ce module expose deux classes `TextCalendar` et `HTMLCalendar`. Sans entrer du tout dans le détail, ces deux classes permettent d'imprimer dans des formats différents le même type d'informations.

Le point ici est que les concepteurs ont choisi un graphe d'héritage comme ceci :

```python
    Calendar
    |-- TextCalendar
    |-- HTMLCalendar
```

qui permet de grouper le code concernant la logique dans la classe `Calendar`, puis dans les deux sous-classes d'implémenter le type de sortie qui va bien. 

C'est l'utilisateur qui choisit la classe qui lui convient le mieux, et de cette manière, le maximum de code est partagé entre les deux classes ; et de plus si vous avez besoin d'une sortie au format, disons PDF, vous pouvez envisager d'hériter de `Calendar` et de n'implémenter que la partie spécifique au format PDF.

C'est un peu le niveau élémentaire de l'héritage.

+++

##### Le module `SocketServer`

+++

Toujours dans la bibliothèque standard, le [module `SocketServer`](https://docs.python.org/3/library/socketserver.html) fait un usage beaucoup plus sophistiqué de l'héritage.

Le module propose une hiérarchie de classes comme ceci :

+++

```python
    +------------+
    | BaseServer |
    +------------+
          |
          v
    +-----------+        +------------------+
    | TCPServer |------->| UnixStreamServer |
    +-----------+        +------------------+
          |
          v
    +-----------+        +--------------------+
    | UDPServer |------->| UnixDatagramServer |
    +-----------+        +--------------------+
```

+++

Ici encore notre propos n'est pas d'entrer dans les détails, mais d'observer le fait que les différents *niveaux d'intelligence* sont ajoutés les uns aux les autres au fur et à mesure que l'on descend le graphe d'héritage.

Cette hiérarchie est par ailleurs étendue par le [module `http.server`](https://docs.python.org/3/library/http.server.html) et notamment au travers de la classe [`HTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer) qui hérite de `TCPServer`.

+++

Pour revenir au module `SocketServer`, j'attire votre attention dans [la page d'exemples](https://docs.python.org/3/library/socketserver.html#examples) sur
[cet exemple en particuler](https://docs.python.org/3/library/socketserver.html#asynchronous-mixins), 
où on crée une classe de serveurs multi-threads - la classe `ThreadedTCPServer` -
par simple héritage multiple entre `ThreadingMixIn` et `TCPServer`.
La notion de `Mixin` est [décrite dans cette page Wikipédia](http://en.wikipedia.org/wiki/Mixin)
dans laquelle vous pouvez accéder directement [à la section consacrée à Python](http://en.wikipedia.org/wiki/Mixin#In_Python).

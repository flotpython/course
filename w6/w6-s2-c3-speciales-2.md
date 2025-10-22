---
jupytext:
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
  title: Surcharge op. (2)
---

# Méthodes spéciales (2/3)

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau avancé

+++

Nous poursuivons dans ce complément la sélection de méthodes spéciales entreprise en première partie.

+++

***

+++

### `__contains__`, `__len__`, `__getitem__` et apparentés

+++

La méthode `__contains__` permet de donner un sens à :

```python
item in objet
```

Sans grande surprise, elle prend en argument un objet et un item, et doit renvoyer un booléen. Nous l'illustrons ci-dessous avec la classe `DualQueue`.

+++

La méthode `__len__` est utilisée par la fonction *built-in* `len` pour retourner la longueur d'un objet.

+++

##### La classe `DualQueue`

+++

Nous allons illustrer ceci avec un exemple de classe, un peu artificiel, qui implémente une queue de type FIFO. Les objets sont d'abord admis dans la file d'entrée (`add_input`), puis déplacés dans la file de sortie (`move_input_to_output`), et enfin sortis (`emit_output`).

Clairement, cet exemple est à but uniquement pédagogique ; on veut montrer comment une implémentation qui repose sur deux listes séparées peut donner l'illusion d'une continuité, et se présenter comme un container unique. De plus cette implémentation ne fait aucun contrôle pour ne pas obscurcir le code.

```{code-cell} ipython3
class DualQueue:
    """Une double file d'attente FIFO"""

    def __init__(self):
        "constructeur, sans argument"
        self.inputs = []
        self.outputs = []

    def __repr__ (self):
        "affichage"
        return f"<DualQueue, inputs={self.inputs}, outputs={self.outputs}>"

    # la partie qui nous intéresse ici
    def __contains__(self, item):
        "appartenance d'un objet à la queue"
        return item in self.inputs or item in self.outputs
    
    def __len__(self):
        "longueur de la queue"
        return len(self.inputs) + len(self.outputs)        

    # l'interface publique de la classe
    # le plus simple possible et sans aucun contrôle
    def add_input(self, item):
        "faire entrer un objet dans la queue d'entrée"
        self.inputs.insert(0, item)
        
    def move_input_to_output (self):
        """
        l'objet le plus ancien de la queue d'entrée
        est promu dans la queue de sortie
        """
        self.outputs.insert(0, self.inputs.pop())
        
    def emit_output (self):
        "l'objet le plus ancien de la queue de sortie est émis"
        return self.outputs.pop()
```

```{code-cell} ipython3
# on construit une instance pour nos essais
queue = DualQueue()
queue.add_input('zero')
queue.add_input('un')
queue.move_input_to_output()
queue.move_input_to_output()
queue.add_input('deux')
queue.add_input('trois')

print(queue)
```

##### Longueur et appartenance

+++

Avec cette première version de la classe `DualQueue` on peut utiliser `len` et le test d'appartenance :

```{code-cell} ipython3
print(f'len() = {len(queue)}')

print(f"deux appartient-il ? {'deux' in queue}")
print(f"1 appartient-il ? {1 in queue}")
```

##### Accès séquentiel (accès par un index entier)

+++

Lorsqu'on a la notion de longueur de l'objet avec  `__len__`, il peut être opportun -  quoique cela n'est pas imposé par le langage, comme on vient de le voir - de proposer également un accès indexé par un entier pour pouvoir faire :

```python
queue[1]
```

**Pour ne pas répéter tout le code de la classe**, nous allons étendre `DualQueue` ; pour cela nous définissons une fonction, que nous affectons ensuite à `DualQueue.__getitem__`, comme nous avons déjà eu l'occasion de le faire :

```{code-cell} ipython3
# une première version de DualQueue.__getitem__
# pour uniquement l'accès par index

# on définit une fonction
def dual_queue_getitem (self, index):
    "redéfinit l'accès [] séquentiel"

    # on vérifie que l'index a un sens
    if not (0 <= index < len(self)):
        raise IndexError(f"Mauvais indice {index} pour DualQueue")
    # on décide que l'index 0 correspond à l'élément le plus ancien
    # ce qui oblige à une petite gymnastique
    li = len(self.inputs)
    lo = len(self.outputs)
    if index < lo:
        return self.outputs[lo - index - 1]
    else:
        return self.inputs[li - (index-lo) - 1]

# et on affecte cette fonction à l'intérieur de la classe
DualQueue.__getitem__ = dual_queue_getitem
```

À présent, on peut **accéder** aux objets de la queue **séquentiellement** :

```{code-cell} ipython3
print(queue[0])
```

ce qui lève la même exception qu'avec une vraie liste si on utilise un mauvais index :

```{code-cell} ipython3
try:
    print(queue[5])
except IndexError as e:
    print('ERREUR',e)
```

##### Amélioration : accès par slice

+++

Si on veut aussi supporter l'accès par slice comme ceci :

```python
queue[1:3]
```

il nous faut modifier la méthode `__getitem__`.

+++

Le second argument de `__getitem__` correspond naturellement au contenu des crochets `[]`, on utilise donc `isinstance` pour écrire un code qui s'adapte au type d'indexation, comme ceci :

```{code-cell} ipython3
# une deuxième version de DualQueue.__getitem__
# pour l'accès par index et/ou par slice

def dual_queue_getitem (self, key):
    "redéfinit l'accès par [] pour entiers, slices, et autres"

    # l'accès par slice queue[1:3] 
    # nous donne pour key un objet de type slice
    if isinstance(key, slice):
        # key.indices donne les indices qui vont bien
        return [self[index] for index in range(*key.indices(len(self)))]

    # queue[3] nous donne pour key un entier
    elif isinstance(key, int):
        index = key
        # on vérifie que l'index a un sens
        if index < 0 or index >= len(self):
            raise IndexError(f"Mauvais indice {index} pour DualQueue")
        # on décide que l'index 0 correspond à l'élément le plus ancien
        # ce qui oblige à une petite gymnastique
        li = len(self.inputs)
        lo = len(self.outputs)
        if index < lo:
            return self.outputs[lo-index-1]
        else:
            return self.inputs[li-(index-lo)-1]
    # queue ['foo'] n'a pas de sens pour nous
    else:
        raise KeyError(f"[] avec type non reconnu {key}")

# et on affecte cette fonction à l'intérieur de la classe
DualQueue.__getitem__ = dual_queue_getitem
```

Maintenant on peut accéder par slice :

```{code-cell} ipython3
queue[1:3]
```

Et on reçoit bien une exception si on essaie d'accéder par clé :

```{code-cell} ipython3
try:
    queue['key']
except KeyError as e:
    print(f"OOPS: {type(e).__name__}: {e}")
```

##### L'objet est itérable (même sans avoir `__iter__`)

+++

Avec seulement `__getitem__`, on peut **faire une boucle** sur l'objet queue. On l'a mentionné rapidement dans la séquence sur les itérateurs, mais la **méthode `__iter__` n'est pas la seule façon** de rendre un objet itérable :

```{code-cell} ipython3
# grâce à __getitem__ on a rendu les 
# objets de type DualQueue itérables
for item in queue:
   print(item)
```

##### On peut faire un test sur l'objet

+++

De manière similaire, même sans la méthode `__bool__`, cette classe sait **faire des tests de manière correcte** grâce uniquement à la méthode `__len__` :

```{code-cell} ipython3
# un test fait directement sur la queue
if queue:
    print(f"La queue {queue} est considérée comme True")
```

```{code-cell} ipython3
# le même test sur une queue vide
empty = DualQueue()

# maintenant le test est négatif (notez bien le *not* ici)
if not empty:
    print(f"La queue {empty} est considérée comme False")
```

***

+++

### `__call__` et les *callables*

+++

Le langage introduit de manière similaire la notion de ***callable*** - littéralement, qui peut être appelé.
L'idée est très simple, on cherche à donner un sens à un fragment de code du genre de :

+++

```python
# on crée une instance
objet = Classe(arguments)
```

et c'est l'objet (Attention : **l'objet, pas la classe**) qu'on utilise comme une fonction

```python
objet(arg1, arg2)
```

+++

Le protocole ici est très simple ; cette dernière ligne a un sens en Python dès lors que :

 * `objet` possède une méthode `__call__` ;
 * et que celle-ci peut être envoyée à `objet` avec les arguments `arg1, arg2` ;
 * et c'est ce résultat qui sera alors retourné par `objet(arg1, arg2)` :

+++

```python
objet(arg1, arg2) ⟺ objet.__call__(arg1, arg2)
```

+++

Voyons cela sur un exemple :

```{code-cell} ipython3
class PlusClosure:
    """Une classe callable qui permet de faire un peu comme la 
    fonction built-in sum mais en ajoutant une valeur initiale"""
    def __init__(self, initial):
        self.initial = initial
    def __call__(self, *args):
        return self.initial + sum(args)
    
# on crée une instance avec une valeur initiale 2 pour la somme
plus2 = PlusClosure (2)
```

```{code-cell} ipython3
# on peut maintenant utiliser cet objet 
# comme une fonction qui fait sum(*arg)+2
plus2()
```

```{code-cell} ipython3
plus2(1)
```

```{code-cell} ipython3
plus2(1, 2)
```

Pour ceux qui connaissent, nous avons choisi à dessein un exemple qui s'apparente à [une clôture](http://en.wikipedia.org/wiki/Closure_%28computer_programming%29). Nous reviendrons sur cette notion de *callable* lorsque nous verrons les décorateurs en semaine 9.

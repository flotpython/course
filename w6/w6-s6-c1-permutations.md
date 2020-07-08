---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## Complément - niveau avancé

+++

### Implémenter un itérateur de permutations

+++

Dans ce complément nous allons nous amuser à implémenter une fonctionnalité qui est déjà disponible dans le module `itertools`.

+++

##### C'est quoi déjà les permutations ?

+++

En guise de rappel, l'ensemble des permutations d'un ensemble fini correspond à toutes les façons d'ordonner ses éléments ; si l'ensemble est de cardinal $n$, il possède $n!$ permutations : on a $n$ façons de choisir le premier élément, $n-1$ façons de choisir le second, etc.

+++

Un itérateur sur les permutations est disponible au travers du module standard `itertools`. Cependant il nous a semblé intéressant de vous montrer comment nous pourrions écrire nous-mêmes cette fonctionnalité, de manière relativement simple.

+++

Pour illustrer le concept, voici à quoi ressemblent les 6 permutations d'un ensemble à trois éléments :

```{code-cell}
from itertools import permutations
```

```{code-cell}
set = {1, 2, 3}

for p in permutations(set):
    print(p)
```

##### Une implémentation

+++

Voici une implémentation possible pour un itérateur de permutations :

```{code-cell}
class Permutations:
    """
    Un itérateur qui énumère les permutations de n
    sous la forme d'une liste d'indices commençant à 0
    """
    def __init__(self, n):
        # le constructeur bien sûr ne fait (presque) rien
        self.n = n
        # au fur et à mesure des itérations
        # le compteur va aller de 0 à n-1
        # puis retour à 0 et comme ça en boucle sans fin
        self.counter = 0
        # on se contente d'allouer un iterateur de rang n-1
        # si bien qu'une fois qu'on a fini de construire
        # l'objet d'ordre n on a n objets Permutations en tout
        if n >= 2:
            self.subiterator = Permutations(n-1)

    # pour satisfaire le protocole d'itération
    def __iter__(self):
        return self

    # c'est ici bien sûr que se fait tout le travail
    def __next__(self):
        # pour n == 1
        # le travail est très simple
        if self.n == 1:
            # on doit renvoyer une fois la liste [0]
            # car les indices commencent à 0
            if self.counter == 0: 
                self.counter += 1
                return [0]
            # et ensuite c'est terminé
            else:
                raise StopIteration

        # pour n >= 2
        # lorsque counter est nul,
        # on traite la permutation d'ordre n-1 suivante
        # si next() lève StopIteration on n'a qu'à laisser passer
        # car en effet c'est qu'on a terminé
        if self.counter == 0:
            self.subsequence = next(self.subiterator)
        #
        # on insère alors n-1 (car les indices commencent à 0)
        # successivement dans la sous-sequence
        #
        # naivement on écrirait
        # result = self.subsequence[0:self.counter] \
        #    + [self.n - 1] \
        #    + self.subsequence[self.counter:self.n-1]
        # mais c'est mettre le nombre le plus élevé en premier
        # et donc à itérer les permutations dans le mauvais ordre,
        # en commençant par la fin
        #
        # donc on fait plutôt une symétrie
        # pour insérer en commençant par la fin
        cutter = self.n-1 - self.counter
        result = self.subsequence[0:cutter] + [self.n - 1] \
                 + self.subsequence[cutter:self.n-1]
        # 
        # on n'oublie pas de maintenir le compteur et de
        # le remettre à zéro tous les n tours
        self.counter = (self.counter+1) % self.n
        return result

    # la longeur de cet itérateur est connue
    def __len__(self):
        import math
        return math.factorial(self.n)
```

Ce qu'on a essayé d'expliquer dans les commentaires, c'est qu'on procède en fin de compte par récurrence. Un objet `Permutations` de rang `n` possède un sous-itérateur de rang `n-1` qu'on crée dans le constructeur. Ensuite l'objet de rang `n` va faire successivement (c'est-à-dire à chaque appel de `next()`) :

* appel *0* :
  * demander à son sous-itérateur une permutation de rang `n-1` (en lui envoyant `next`),
  * la stocker dans l'objet de rang `n`, ce sera utilisé par les *n* premier appels,
  * et construire une liste de taille `n` en insérant `n-1` à la fin de la séquence de taille `n-1`,  


* appel *1* :
  * insérer `n-1` dans la même séquence de rang `n-1` mais cette fois 1 cran avant la fin,


* ...


* appel *n-1* :
  * insérer `n-1` au début de la séquence de rang `n-1`,


* appel *n* :
  * refaire `next()` sur le sous-itérateur pour traiter une nouvelle sous-séquence,
  * la stocker dans l'objet de rang `n`, comme à l'appel *0*, pour ce bloc de n appels,
  * et construire la permutation en insérant *n-1* à la fin, comme à l'appel 0,


* ...

+++

On voit donc le caractère cyclique d'ordre *n* qui est matérialisé par `counter`, que l'on incrémente à chaque boucle mais modulo *n* - notez d'ailleurs que pour ce genre de comportement on dispose aussi de `itertools.cycle` comme on le verra dans une deuxième version, mais pour l'instant j'ai préféré ne pas l'utiliser pour ne pas tout embrouiller ;) 

La terminaison se gère très simplement, car une fois que l'on a traité toutes les séquences d'ordre *n-1* eh bien on a fini, on n'a même pas besoin de lever StopIteration explicitement, sauf bien sûr dans le cas *n=1*.

Le seul point un peu délicat, si on veut avoir les permutations dans le "bon" ordre, consiste à commencer à insérer `n-1` par la droite (la fin de la sous-séquence).

+++

##### Discussion

+++

Il existe certainement des tas d'autres façons de faire bien entendu. Le point important ici, et qui donne toute sa puissance à la notion d'itérateur, c'est **qu'à aucun moment on ne construit** une liste ou une séquence quelconque de **n! termes**. 

C'est une erreur fréquente chez les débutants que de calculer une telle liste dans le constructeur, mais procéder de cette façon c'est aller exactement à l'opposé de ce pourquoi les itérateurs ont été conçus ; au contraire, on veut éviter à tout prix le coût d'une telle construction.

On peut le voir sur un code qui n'utiliserait que les 20 premières valeurs de l'itérateur, vous constatez que ce code est immédiat :

```{code-cell}
def show_first_items(iterable, nb_items):
    """
    montre les <nb_items> premiers items de iterable
    """
    print(f"Il y a {len(iterable)} items dans l'itérable")
    for i, item in enumerate(iterable):
        print(item)
        if i >= nb_items:
            print('....')
            break
```

```{code-cell}
show_first_items(Permutations(12), 20)
```

Ce tableau vous montre par ailleurs sous un autre angle comment fonctionne l'algorithme, si vous observez le `11` qui balaie en diagonale les 12 premières lignes, puis les 12 suivantes, etc..

+++

##### Ultimes améliorations

+++

Dernières remarques, sur des améliorations possibles - mais tout à fait optionnelles :

* le lecteur attentif aura remarqué qu'au lieu d'un entier `counter` on aurait pu profitablement utiliser une instance de `itertools.cycle`, ce qui aurait eu l'avantage d'être plus clair sur le propos de ce compteur ;
* aussi dans le même mouvement, au lieu de se livrer à la gymnastique qui calcule `cutter` à partir de `counter`, on pourrait dès le départ créer dans le cycle les bonnes valeurs en commençant à `n-1`.

+++

C'est ce qu'on a fait dans cette deuxième version ; après avoir enlevé la logorrhée de commentaires ça redevient presque lisible ;)

```{code-cell}
import itertools

class Permutations2:
    """
    Un itérateur qui énumère les permutations de n
    sous la forme d'une liste d'indices commençant à 0
    """
    def __init__(self, n):
        self.n = n
        # on commence à insérer à la fin 
        self.cycle = itertools.cycle(list(range(n))[::-1])
        if n >= 2:
            self.subiterator = Permutations2(n-1)
        # pour savoir quand terminer le cas n==1
        if n == 1:
            self.done = False

    def __iter__(self):
        return self

    def __next__(self):
        cutter = next(self.cycle)

        # quand n==1 on a toujours la même valeur 0
        if self.n == 1:
            if not self.done:
                self.done = True
                return [0]
            else:
                raise StopIteration

        # au début de chaque séquence de n appels
        # il faut appeler une nouvelle sous-séquence
        if cutter == self.n-1:
            self.subsequence = next(self.subiterator)
        # dans laquelle on insére n-1
        return self.subsequence[0:cutter] + [self.n-1] \
                 + self.subsequence[cutter:self.n-1]

    # la longeur de cet itérateur est connue
    def __len__(self):
        import math
        return math.factorial(self.n)
```

```{code-cell}
show_first_items(Permutations2(5), 20)
```

***
***

+++

Il me semble intéressant de montrer une autre façon, plus simple, d'écrire un itérateur de permutations, à base cette fois de générateurs; c'est un tout petit peu une digression par rapport au cours qui est sur la conception d'itérateurs et d'itérables. Ça va nous permettre surtout de réviser la notion de `yield from`.

+++

On commence par une version très rustique qui fait des impressions :

```{code-cell}
# pour simplifier ici on suppose que l'entrée est une vraie liste
# que l'on va ainsi pouvoir modifier par effets de bord
def gen_perm1(subject, k=0):
    if k == len(subject):
        # cette version hyper rustique se contente de faire une impression
        print(subject)
    else:
        for i in range(k, len(subject)):
            # on échange 
            subject[k], subject[i] = subject[i], subject[k]
            gen_perm1(subject, k+1)
            # on remet comme c'était pour le prochain échange
            subject[k], subject[i] = subject[i], subject[k]
```

```{code-cell}
gen_perm1(['a', 'b', 'c', 'd'])
```

Très bien, mais on ne veut pas imprimer, on veut itérer. On pourrait se dire, il me suffit de remplacer `print` par `yield`. Essayons cela :

```{code-cell}
# pour simplifier ici on suppose que l'entrée est une vraie liste
# que l'on va ainsi pouvoir modifier par effets de bord
def gen_perm2(subject, k=0):
    if k == len(subject):
        # cette version hyper rustique se contente de faire une impression
        yield subject
    else:
        for i in range(k, len(subject)):
            # on échange 
            subject[k], subject[i] = subject[i], subject[k]
            gen_perm2(subject, k+1)
            # on remet comme c'était pour le prochain échange
            subject[k], subject[i] = subject[i], subject[k]
```

```{code-cell}
for perm in gen_perm2(['a', 'b', 'c', 'd']):
    print(perm)
```

On est exactement dans le cas où il nous faut utiliser `yield from`. En effet lorsqu'on appelle `gen_perm(subject, k+1)` ici, ce qu'on obtient en retour c'est maintenant un objet générateur. Pour faire ce qu'on cherche à faire il nous faut bien utiliser cet objet générateur, et pour cela on utilise `yield from`.

```{code-cell}
# pour simplifier ici on suppose que l'entrée est une vraie liste
# que l'on va ainsi pouvoir modifier par effets de bord
def gen_perm3(subject, k=0):
    if k == len(subject):
        # cette version hyper rustique se contente de faire une impression
        yield subject
    else:
        for i in range(k, len(subject)):
            # on échange 
            subject[k], subject[i] = subject[i], subject[k]
            yield from gen_perm3(subject, k+1)
            # on remet comme c'était pour le prochain échange
            subject[k], subject[i] = subject[i], subject[k]
```

```{code-cell}
for perm in gen_perm3(['a', 'b', 'c', 'd']):
    print(perm)
```

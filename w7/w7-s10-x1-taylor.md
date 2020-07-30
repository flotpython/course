---
jupytext:
  cell_metadata_filter: all
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: 'Exercice: taylor'
version: '3.0'
---

# Le théorème de Taylor illustré

+++

## exercice : niveau avancé

+++

En guise d'application de ce qu'on a vu jusqu'ici, je vous invite à réaliser une visualisation
du théorème de Taylor; je vous renvoie à votre cours d'analyse, [ou à wikipedia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Taylor) pour une présentation détaillée de ce théorème, mais ce que nous en retenons se résume à ceci.


On peut approximer une fonction "suffisamment régulière" - disons $C^\infty$ pour fixer les idées - par un polynôme d'ordre $n$, dont les coefficients dépendent uniquement des $n$ dérivées successives au voisinage d'un point :

$$f_n(x) = \sum_{i=0}^{n}\frac{f^{(i)}(0).x^i}{i!}$$

Sans perte de généralité nous avons ici fixé le point de référence comme étant égal à 0, il suffit de translater $f$ par changement de variable pour se ramener à ce cas-là.

Le théorème de Taylor nous dit que la suite de fonctions $(f_n)$ converge vers $f$.

+++

On pourrait penser - c'était mon cas la première fois que j'ai entendu parler de ce théorème - que l'approximation est valable **au voisinage de 0** seulement; si on pense en particulier à **sinus**, on peut accepter l'idée que ça va nous donner une période autour de 0 peut-être.

En fait, c'est réellement bluffant de voir que ça marche vraiment incroyablement bien et loin.

+++

## mon implémentation

+++

Je commence par vous montrer **seulement le résultat** de l'implémentation que j'ai faite.

Pour calculer les dérivées successives j'utilise la librairie `autograd`.

Ce code est relativement générique, vous pouvez visualiser l'approximation de Taylor avec une fonction que vous passez en paramètre - qui doit avoir tout de même la bonne propriété d'être vectorisée, et d'utiliser la couche `numpy` exposée par `autograd` :

```{code-cell}
# to compute derivatives
import autograd
import autograd.numpy as np
```

Sinon pour les autres dépendances, j'ai utilisé les `ipywidgets` et `bokeh`

```{code-cell}
from math import factorial

from ipywidgets import interact, IntSlider, Layout
```

```{code-cell}
from bokeh.plotting import figure, show
from bokeh.io import push_notebook, output_notebook

output_notebook()
```

### la classe `Taylor`

+++

J'ai défini une classe `Taylor`, je ne vous montre pas encore le code, je vais vous inviter à en écrire une vous même; nous allons voir tout de suite comment l'utiliser, mais pour la voir fonctionner il vous faut l'évaluer :

+++

<span style='background-color: #9EBC9E; padding:5px;'>↓↓↓↓↓ ↓↓↓↓↓ assurez-vous de **bien évaluer la cellule cachée** ici ↓↓↓↓↓ ↓↓↓↓↓</span>

```{code-cell}
:hide_input: true

# @BEG@ name=taylor
class Taylor:
    """
    provides an animated view of Taylor approximation
    where one can change the degree interactively
        
    derivatives are computed on X=0, translate as needed
    """
    def __init__(self, function, domain):
        """
        initialized from
        
        Parameters:
          function: an autograd-friendly vectorized function
          domain: the X domain (typically a linspace)
        """
        self.function = function
        self.domain = domain
        self.regular_y = function(self.domain)
        
    def display(self, y_range):
        """
        create initial drawing with degree=0
        
        Parameters:
          y_range: there is a need to display all degrees with a fixed 
            range on the y-axis for smooth transitions; 
            pass this as a (ymin, ymax) tuple
        """
        x_range = (self.domain[0], self.domain[-1])
        self.figure = figure(title=self.function.__name__,
                             x_range=x_range, y_range=y_range)
        # each of the 2 curves is a bokeh line object
        self.line_exact = self.figure.line(
            self.domain, self.regular_y, color='green')
        self.line_approx = self.figure.line(
            self.domain, self._approximated(0), color='red', line_width=2)
        # that's what allows for smooth updates down the road
        self.handle = show(self.figure, notebook_handle=True)
# @END@

# @BEG@ name=taylor continued=true
        
    def _approximated(self, degree):
        """
        Computes and returns the Y array, the images of the domain
        through Taylor approximation
        
        Parameters:
          degree: the degree for Taylor approximation
        """
        # initialize with a constant f(0)
        # 0 * self.domain allows to create an array
        # with the right length
        result = 0 * self.domain + self.function(0.)
        # f'
        derivative = autograd.grad(self.function)
        for n in range(1, degree+1):
            # the term in f(n)(x)/n!
            result += derivative(0.)/factorial(n) * self.domain**n
            # higher-orders derivatives
            derivative = autograd.grad(derivative)
        return result

    def _update(self, degree):
        # update the second curve only, of course
        self.line_approx.data_source.data['y'] = self._approximated(degree)
        push_notebook(handle=self.handle)
        
    def interact(self, degree_widget):
        """
        displays a widget for interatively modifying degree
        
        Parameters:
          degree_widget: a ipywidget, typically an IntSlider
            styled at your convenience
        """
        interact(lambda degree: self._update(degree), degree=degree_widget)
# @END@
```

<span style='background-color: #9EBC9E; padding:5px;'>↑↑↑↑↑ ↑↑↑↑↑ assurez-vous de **bien évaluer la cellule cachée** ici ↑↑↑↑↑ ↑↑↑↑↑</span>

```{code-cell}
# check the code was properly loaded
help(Taylor)
```

### sinus

+++

Ma classe `Taylor` s'utilise comme ceci : d'abord on crée une instance à partir d'une fonction
et d'un domaine, i.e. l'intervalle des X qui nous intéresse.

```{code-cell}
# between -4π and 4π
DOMAIN = np.linspace(-4*np.pi, 4*np.pi, 250)

# an instance
sinus_animator = Taylor(np.sin, DOMAIN)
```

**Remarquez bien** qu'ici la fonction que je passe au constructeur est **en réalité `autograd.numpy.sin`** et non pas `numpy.sin`, vu la façon dont on a défini notre symbole `np` lors des imports (et ça ne marcherait pas du tout avec `numpy.sin`).

+++

Ensuite on crée un `ipywidget` qui va nous permettre de choisir le degré $n$; dans le cas de sinus, qui est impaire, les degrés intéressants sont impairs (vous pouvez vérifier que les coefficients de Taylor pairs sont nuls lorsque $f$ est impaire).

```{code-cell}
# the widget to select a degree
sinus_widget = IntSlider(
   min=1, max=33, step=2,        # sinus being odd we skip even degrees
   layout=Layout(width='100%'))  # more convenient with the whole page width
```

Pour lancer l'interaction, on n'a plus qu'à :

* afficher le diagramme avec la méthode `display()`; on a besoin pour cela de préciser les bornes en Y, qui resteront constantes au cours de l'animation (sinon la visualisation est vilaine)

puis lancer l'interaction en passant en paramètre le widget qui choisit le degré, ce qui donne :

```{code-cell}
# fixed limits in Y
sinus_animator.display((-1.5, 1.5))

sinus_animator.interact(sinus_widget)
```

### cosinus

+++

La même chose avec cosinus nous donnerait ceci :

```{code-cell}
# allows to select a degree
sinus_widget = IntSlider(
   min=0, max=34, step=2,      # only even degrees
   layout=Layout(width='100%'))

### ready to go
sinus_animator = Taylor(np.cos, DOMAIN)
sinus_animator.display((-1.5, 1.5))
sinus_animator.interact(sinus_widget)
```

### exponentielle

```{code-cell}
# allows to select a degree
exp_widget = IntSlider(min=0, max=17,
   layout=Layout(width='100%'))

### ready to go
exp_animator = Taylor(np.exp, np.linspace(-5, 10, 200))
exp_animator.display((-15_000, 25000))
exp_animator.interact(exp_widget)
```

## quelques indices

+++

### affichage

+++

Ici j'ai utilisé `bokeh`, mais on peut tout à fait arriver à quelque chose de similaire avec `matplotlib` sans aucun doute

+++

### conception

+++

Ma classe `Taylor` s'inspire très exactement de la technique décrite dans le Complément #6 "Autres bibliothèques de visualisation", et notamment la classe `Animation`, modulo quelques renommages.

+++

### calcule de dérivées avec `autograd`

+++

La seule fonction que j'ai utilisée de la bibliothèque `autograd` est `grad` :

```{code-cell}
from autograd import grad
```

```{code-cell}
# dans le cas de sinus par exemple
# les dérivées successives en 0 se retrouvent comme ceci
f = np.sin  # à nouveau cette fonction est autograd.numpy.sin
f(0.)
```

```{code-cell}
:cell_style: split

# ordre 1
f1 = grad(f)
f1(0.)
```

```{code-cell}
:cell_style: split

# ordre 2
f2 = grad(f1)
f2(0.)
```

## votre implémentation

+++

Je vous invite à écrire votre propre implémentation, qui se comporte en gros comme notre classe `Taylor`.

Vous pouvez naturellement simplifier autant que vous le souhaitez, ou modifier la signature comme vous le sentez (pensez alors à modifier aussi la cellule de test).

À titre indicatif ma classe `Taylor` fait environ 30 lignes de code utile, i.e. sans compter les lignes blanches, les docstrings et les commentaires.

```{code-cell}
# à vous de jouer

class MyTaylor:
    def __init__(self, function, domain):
        ...
    def display(self, y_range):
        # là on veut créer le dessin original, c'est à dire
        # la figure, la courbe de f qui ne chagera plus,
        # et la courbe approchée avec disons n=0 (donc y=f(0))
        ...
    def _update(self, n):
        # modifier la courbe approximative avec Taylor à l'ordre n
        # je vous recommande de créer cette méthode privée
        # pour pouvoir l'appeler dans interact()
        ...
    def interact(self, widget):
        # là clairement il va y avoir un appel à 
        # interact() de ipywidgets
        print("inactive for now")
```

```{code-cell}
# testing MyTaylor on cosinus

sinus_widget = IntSlider(
   min=0, max=34, step=2,      # only even degrees
   layout=Layout(width='100%'))

### ready to go
sinus_animator = MyTaylor(np.cos, DOMAIN)
sinus_animator.display((-1.5, 1.5))
sinus_animator.interact(sinus_widget)
```

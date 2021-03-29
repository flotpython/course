---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: 'App: Fourier (K3D + bokeh)'
---

# Application à la transformée de Fourier

+++

## Complément - niveau avancé

+++

On va appliquer ce qu'on a appris jusqu'ici, au cas de la transformée de Fourier.

Mon angle c'est d'essayer de vous faire intuiter à quoi correspond cette fameuse formule, dans le cas d'une fonction périodique en tous cas, et pourquoi dans ce cas-là on trouve un résultat non nul seulement sur les fréquences harmoniques de la fonction de base.

En guise de bonus, on va en profiter pour représenter aussi la fonction complexe en 3D, c'est surtout un prétexte pour faire au moins un exemple avec `k3d`, qui est très efficace, et qui à mon humble avis gagne à être connue.

+++

Mais commençons par importer ce qui va nous servir.

```{code-cell}
import numpy as np
# mostly we use bokeh in here, but the first glimpse is made with mpl
import matplotlib.pyplot as plt
%matplotlib notebook
```

```{code-cell}
from bokeh.plotting import figure, show
from bokeh.io import push_notebook, output_notebook

output_notebook()
```

```{code-cell}
# install with - unsurprisingly (from the terminal)
# pip install ipywidgets

from ipywidgets import interact, fixed
from ipywidgets import SelectionSlider, IntSlider
```

```{code-cell}
# ditto w/
# pip install k3d

import k3d
from k3d.plot import Plot
```

## Une fonction périodique

+++

On considère donc une fonction périodique, comme celle-ci :

```{code-cell}
# a vectorized function is required here

def my_periodic_2pi(t): 
    '2sin(x) + sin(2x) - 3/2 sin(3x) + 2'
    return 2*np.sin(t) + np.sin(2*t) - 1.5*np.sin(3*t) + 2
```

Pour un aperçu, on la plotte rapidement avec matplotlib

```{code-cell}
def plot_functions(domain, title, *functions):
    plt.figure(figsize=(4, 2))
    for function in functions:
        plt.plot(domain, function(domain))
    # notice how to retrieve the function's docstring
    plt.title(title)
    plt.show()

# period is 2 pi, let us plot between 0 and 15 with a .001 step
plot_functions(np.linspace(-1, 15, 200), "period = 2π", my_periodic_2pi)
```

### changement d'échelle

+++

Comme on le voit, la période est de 2π, évidemment;  
pour nous simplifier la vie nous allons changer l'échelle des x, pour travailler avec une période entière, ce sera plus facile pour faire les calculs mentalement;  
je choisis arbitrairement une période = 2 :

```{code-cell}
# this one has a period of 2
def my_periodic(t):
    "addition of 3 sinus - period = 2"
    return my_periodic_2pi(t*np.pi)
```

```{code-cell}
D1 = np.linspace(0, 6, 200)

plot_functions(D1, "now period=2", my_periodic)
```

### les morceaux

En ignorant la constante additive 2, on sait donc que notre fonction d'entrée est la superposition des 3 fonctions

```{code-cell}
def H1(t):
    "fundamental"
    return 2*np.sin(t*np.pi)
def H2(t):
    "fundamental"
    return np.sin(2*t*np.pi)
def H3(t):
    "fundamental"
    return -1.5*np.sin(3*t*np.pi)

plot_functions(D1, "the 3 pieces", H1, H2, H3)
```

La transformée de Fourier permet de retrouver ces 3 morceaux, donc par contruction de `my_periodic` on doit retrouver :

* la fondamentale (bleu): period = 2, frequency = 1/2
* l'harmonique de 2nd ordre(orange): period = 1, frequency = 1
* l'harmonique de 3eme ordre (vert):  period = 2/3, frequency = 3/2

+++

### les plages de fréquence

+++

Du coup on va avoir envie de s'intéresser à plusieurs plages de fréquence :

```{code-cell}
from ipywidgets import FloatSlider, Dropdown, Layout
# for building sliders
full_width = Layout(width='100%')

# la fréquence fondamentale
FUNDAMENTAL = 1/2

# un widget à large spectre, pour choisir une fréquence entre 1/4 et 3
def full_spectrum():
    return FloatSlider(min=0.25, max=3., step=0.01,
                       layout=full_width,
                       value=FUNDAMENTAL,
                      )

# quand on voudra faire un zoom autour d'une fréquence précise
def closeup_around(freq):
    return FloatSlider(min=freq * 0.98, max=freq * 1.02,
                       # 400 steps 
                       step = freq/10_000,
                       layout=full_width,
                       value=FUNDAMENTAL,
                       readout_format='.4f',
                      )
```

## La formule de fourier

+++

Je rappelle la formule magique, la transformée de Fourier de $f$ est la fonction $F$ qui associe à une fréquence $\phi$ la valeur :

$F: \phi \rightarrow \int_{-\infty}^{\infty}f(t)e^{2i\pi\phi t}dt$

+++

Pour un $\phi$ donné, il s'agit donc de calculer l'intégrale sur $\mathbb{R}$ de la fonction complexe

$F_{\phi}(t) = f(t)e^{2i\pi\phi t}$

On va commencer par représenter cette courbe en 3D :
* sur l'axe des x, on représente le temps $t$
* et sur les axes y et z, on représente les partie réelle et imaginaire de $F_{\phi}(t)$

+++

## représentation 3D

+++

Voici une classe permettant de visualiser la courbe de $F_{\phi}$ en 3D.  
En plus de la courbe, on matérialise par une ligne rouge l'emplacement du barycentre de la distribution complexe (plus de détails plus bas).

+++

Une différence par rapport à ce qu'on avait pu voir avec `bokeh`, c'est qu'ici la librairie `k3d` expose une classe `Plot`, qui peut s'afficher directement dans le notebook; du coup il semble raisonnable ici d'hériter de cette classe; sinon l'idée générale est la même.

Vous avez sans doute déjà remarqué que chaque librairie de visualisation s'attend à recevoir les données d'entrée sous un format spécifique - ce qui a tendance à rendre l'utilisation de toutes ces techniques un peu fastidieuse parfois..

En tous cas notez que de manière opportuniste, la méthode centrale ici, à savoir `compute_dots_and_center()`, retourne ses données sous un format qui est propice pour `k3d` - qui aime les tableaux de `shape` $(n, 3)$, d'où l'appel à `np.stack()`.

```{code-cell}
class FourierAnimator3D(Plot):
    
    DOTS_PER_UNIT = 50

    def __init__(self, function, phi, 
                 domain=10, **kwds):
        self.function = function
        self.phi = phi
        self.domain = domain
        # pass along named parameters, like e.g. height
        super().__init__(**kwds)
        
        # returns the format expected by k3d line
        dots, center = self.compute_dots_and_center()
        # create line and add in plot
        self.line = k3d.line(dots)
        self += self.line
        # the line that materializes the barycenter 
        self.center_line = k3d.line(center, color=0xff0000, width=0.5)
        self += self.center_line

    def update(self, phi):
        self.phi = phi
        new_dots, new_center = self.compute_dots_and_center()
        self.line.vertices = new_dots
        self.center_line.vertices = new_center

    def compute_dots_and_center(self):
        """
        returns an array of shape (nb_points, 3) suitable for k3d.line
        """
        nb_points = self.DOTS_PER_UNIT * self.domain
        t, dt = np.linspace(0, self.domain, nb_points, retstep=True)
        # a complex value
        rotating = self.function(t) * np.exp(2j * np.pi * self.phi * t)
        x = t
        y = np.real(rotating)
        z = np.imag(rotating)
        # the format expected by k3d line
        dots = np.stack([x, y, z], axis=1)
        # compute barycenter - as a complex average
        center_complex = np.sum(rotating) / nb_points
        # the format expected by k3d points
        # here 1 point at each end of the cylinder
        center = np.array([(0, center_complex.real, center_complex.imag),
                           (self.domain, center_complex.real, center_complex.imag)])
        return dots, center
    
    def interact(self, phi_widget):
        interact(lambda phi: self.update(phi), phi=phi_widget)
```

```{code-cell}
a3d = FourierAnimator3D(my_periodic, phi=1.)
display(a3d)
a3d.interact(full_spectrum())
```

### calculer et visualiser l'intégrale : le barycentre

+++

Rappelez-vous que :
* on commence par fixer $\phi$;  
  et $\phi$ correspond à la vitesse de rotation de la courbe de $f$ autour de l'axe y=z=0

Et là vous vous dites, c'est bien joli mais comment je calcule l'intégrale de cette fonction complexe ?

En fait c'est assez simple à faire mentalement, et ça le truc crucial à comprendre, c'est que cette intégrale se déduit du barycentre de la courbe qu'on observe si on se met "au bout" de l'axe du temps et qu'on observe le signal tourner.

Intuitivement, pour évaluer l'intégrale d'une fonction usuelle, on peut estimer la moyenne de $f$ entre les bornes, on n'a plus qu'à multiplier par la longueur du segment.

De la même façon, le barycentre de ce dessin - à nouveau quand on regarde le long de l'axe du temps - donne une bonne indication de la valeur de l'intégrale; bien sûr, pour obtenir les coordonnées du barycentre il faut normaliser (diviser par la longeur du segment, comme pour la moyenne en dimension 1); aussi si on a N points dans notre échantillon :

$$
\begin{array} {rcl}
\int_a^bF_{\phi}(t)dt & \approx & \sum rotating[i]*dt \\
& \approx & \sum \frac{rotating[i]*(b-a)}{N} \\
\end{array}
$$

et du coup le barycentre, qui est obtenu (souvenez-vous le cas de la dimension 1) en divisant cette valeur par la longueur du domaine $(b-a)$ s'obtient par notre unique ligne de code

        center_complex = np.sum(rotating) / nb_points


On peut essayer de faire le calcul mentalement, mais c'est parfois délicat; d'une part on ne voit pas la différence entre les points où $f$ est positive ou négative; d'autre part il faut noter que ça ne marche bien en fait que parce la vitesse de rotation est uniforme.  
En tous cas le **barycentre dans la visualisation** donne, lui, une **indication fiable** de la valeur de l'intégrale.

+++

Ce qu'on observe sur cette première visualisation, - on va le voir encore mieux en 2D - c'est que le barycentre est souvent nul, sauf au voisinage des fameuse fréquences de $f$ - ouf, ça marche !

+++

## animation en 2D

+++

Il ne nous reste plus qu'à représenter la même chose, mais cette fois en 2D en regardant le long de l'axe des x;
la logique est la même, sauf pour le format de retour de `compute_dots_and_center`, qui est adapté pour `bokeh` :

```{code-cell}
DEFAULT_RANGE = (-6, 6)
DEFAULT_DOMAIN = 100

class FourierAnimator2D:
    
    DOTS_PER_UNIT = 50

    def __init__(self, function, phi, domain=DEFAULT_DOMAIN, **kwds):
        self.function = function
        self.phi = phi
        self.domain = domain
        
    def compute_dots_and_center(self):
        """
        returns X, Y for the curve in 2D 
        and xc, yc the coordinates of the (bary)center
        """
        nb_points = self.DOTS_PER_UNIT * self.domain
        t, dt = np.linspace(0, self.domain, nb_points, retstep=True)
        # a complex value
        rotating = self.function(t) * np.exp(2j * np.pi * self.phi * t)
        X = np.real(rotating)
        Y = np.imag(rotating)
        # compute barycenter - as a complex average
        center_complex = np.sum(rotating) / nb_points
        return X, Y, center_complex.real, center_complex.imag
    
    def display(self, x_range=DEFAULT_RANGE, y_range=DEFAULT_RANGE):
        self.figure = figure(
            title=self.function.__name__,
            x_range=x_range, y_range=y_range)
        
        X, Y, xc, yc = self.compute_dots_and_center()
        
        self.courbe = self.figure.line(X, Y, color='blue', line_width = 1)
        self.center = self.figure.circle([xc], [yc], size=5, color="red")
        self.handle = show(self.figure, notebook_handle=True)
        
    def update(self, phi):
        self.phi = phi

        X, Y, xc, yc = self.compute_dots_and_center()
        self.courbe.data_source.data['x'] = X
        self.courbe.data_source.data['y'] = Y
        self.center.data_source.data['x'] = [xc]
        self.center.data_source.data['y'] = [yc]
        push_notebook(handle=self.handle)

    def interact(self, phi_widget):
        interact(lambda phi: self.update(phi), phi=phi_widget)
```

```{code-cell}
a2d = FourierAnimator2D(my_periodic, FUNDAMENTAL)
a2d.display()
a2d.interact(full_spectrum())
```

On peut même zoomer autour des fréquences critiques :

```{code-cell}
a2d.interact(closeup_around(FUNDAMENTAL))
```

### Discussion

+++

Vous observez la forte discontinuité de $F$ qui vaut 0 presque partout; vous pouvez comprendre que lorsque la fréquence $\phi$ n'est pas en résonance avec celle de $f$, le dessin qu'on obtient est presque parfaitement centré sur (0, 0) et que donc le barycentre est nul.

En mode zoom autour de la fondamentale, on observe mieux la mise en résonance; par contre cette visualisation peut donner l'illusion que $F$ est continue, ce n'est pas le cas, c'est un artefact lié à la longueur finie de notre domaine. 

On a choisi pour la 2D un domaine par défaut qui est [0..100], ce qui fait donc 50 périodes.  
C'est pour cela qu'on a l'illusion qu'au voisinage d'une fréquence sensible, le barycentre s'écarte petit à petit; en fait ce n'est pas le cas, c'est réellement une fonction discontinue, mais pour le voir il faut faire le calcul sur un domaine plus long; lorsque vous choisissez par exemple $\phi=0.501$, vous voyez seulement les 50 premiers pas de la figure qui commencent à diverger; vous pouvez imaginer qu'en augmentant le domaine, on verra une décroissance plus rapide.

Par contre ce sont les vitesses de calcul qui vont commencer à nous limiter :

```{code-cell}
# la discontinuité est plus forte qu'on ne pourrait le penser
# mais pour le vois il faut augmenter le domaine
# et donc les calculs sont plus lents
a2dzoom = FourierAnimator2D(my_periodic, FUNDAMENTAL, domain=500)
a2dzoom.display()
a2dzoom.interact(closeup_around(FUNDAMENTAL))
```

## voir aussi

Une vidéo de 3BlueBrown, sur le même sujet; bon ses animations sont autrement plus sophistiquées :-)

mais ici au moins on les a faites nous-mêmes ;)

https://www.youtube.com/watch?v=spUNpyF58BY

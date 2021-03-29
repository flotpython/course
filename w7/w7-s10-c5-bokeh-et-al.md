---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
notebookname: Autres librairies
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Autres bibliothèques de visualisation

+++

## Complément - niveau basique

+++

Pour conclure cette séquence sur les outils de visualisation, nous allons très rapidement évoquer des alternatives à la bibliothèque `matplotlib`, sachant que le domaine est en pleine expansion.

+++

### Le poids du passé

+++

On a vu que `matplotlib` est un outil relativement complet. Toutefois, on peut lui reprocher deux défauts majeurs.

* D'une part, `matplotlib` a choisi d'offrir une interface aussi proche que possible de ce qui existait préalablement en MatLab. C'est un choix tout à fait judicieux dans l'optique d'attirer la communauté MatLab à des outils open source basés sur Python et numpy. Mais en contrepartie, cela implique d'adopter tels quels des choix de conception.

* Et notamment, en suivant cette approche on hérite d'un modèle mental qui est plus orienté vers la sortie vers du papier que vers la création de documents interactifs.

+++

Ceci, ajouté à l'explosion du domaine de l'analyse et de la visualisation de données, explique la largeur de l'offre en matière de bibliothèques de visualisation alternatives.

Dans ce complément nous allons explorer notamment quelques techniques qui permettent de faire des visualisations interactives; c'est-à-dire où l'on peut modifier la visualisation en fonction de paramètres, réglables facilement. 

C'est quelque chose qui demande **un peu de soin** car, si on utilise `interact()` brutalement, on obtient **des visualisations qui "*flashent*"**, car à chaque changement du contexte on recalcule toute une image, plutôt que de modifier l'image précédente. Ça semble un détail, mais l'oeil est très sensible à ce type d'artefact, et à l'expérience ce détail a plus d'impact qu'on ne pense.

+++

### `bokeh`

+++

Commençons par signaler notamment la bibliothèque [`bokeh`](https://bokeh.pydata.org/en/latest/), qui est développée principalement par Anaconda, dans un modèle open source.

`bokeh` présente quelques bonnes propriétés qui nous semblent mériter d'être signalées.

+++

Pour commencer cette bibliothèque utilise une architecture qui permet de *penser la visualisation comme quelque chose d'interactif* (disons une page html), et non pas de figé comme lorsqu'on pense en termes de feuille de papier. Notamment elle permet de faire collaborer du code Python avec du code JavaScript, qui offre immédiatement des possibilités bien plus pertinentes lorsqu'il s'agit de créer des interactions utilisateur qui soient attractives et efficaces. Signalons en passant, à cet égard, qu'elle utilise [la librairie JavaScript `d3.js`](https://d3js.org/), qui est devenu un standard de fait plus ou moins incontournable dans le domaine de la visualisation.

En tout état de cause, elle offre une interface de programmation qui tient compte d'environnements comme les notebooks, ce qui peut s'avérer un atout précieux si vous utilisez massivement ce support, comme on va le voir, précisément, dans ce notebook.

+++

Il peut aussi être intéressant de savoir que `bokeh` offre des possibilités natives de [visualisation de graphes](https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html) et de [ données géographiques](https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html#).

+++

Par contre à ce stade du développement, la visualisation en 3D n'est sans doute pas le point fort de `bokeh`. C'est une option qui reste possible (voir [par exemple ceci](https://github.com/bokeh/bokeh/tree/master/examples/app/surface3d)), mais cela est pour l'instant considéré comme une extension de la librairie, et donc n'est accessible qu'au prix de l'écriture de code javascript.

+++

Pour une présentation plus complète, je vous renvoie à [la documentation utilisateur](https://bokeh.pydata.org/en/latest/docs/user_guide.html).

+++

### `bokeh` dans les notebooks

+++

Nous allons rapidement illustrer ici comment `bokeh` s'interface avec l'environnement des notebooks pour créer une visualisation interactive. Vous remarquerez que dans le code qui suit, on n'a **pas eu besoin de mentionner** de *magic* ipython, comme lorsqu'on avait du faire dans le complément sur les notebooks interactifs :

```python
%matplotlib notebook
```

```{code-cell}
import numpy as np
```

```{code-cell}
# l'attirail de notebooks interactifs
from ipywidgets import interact, fixed, FloatSlider, Dropdown
```

```{code-cell}
# les imports pour bokeh
from bokeh.plotting import figure, show
# dans la rubrique entrée-sortie, on trouve
# les outils pour produire du html
#  (le mode par défaut)
# ou pour interactig avec un notebook
from bokeh.io import push_notebook, output_notebook
```

```{code-cell}
# c'est cette déclaration qui remplace
# si on veut la magic  '%matplotlib notebook'
output_notebook()
```

*****

```{code-cell}
# on crée un objet figure
figure1 = figure(
    title="fonctions trigonométriques",
    plot_height=300, plot_width=600,
    # c'est là notamment qu'on précise
    # l'intervalle en y
    y_range=(-5, 5),
)
```

```{code-cell}
# on initialise la figure en créant
# un objet courbe
x = np.linspace(0, 2*np.pi, 2000)
y = np.sin(x)
courbe_trigo = figure1.line(x, y, color="#2222aa", line_width=3)
```

```{code-cell}
# la fonction de mise à jour, qui sera connectée
# à interact
def update_trigo(function, frequency=1,
                 amplitude=1, phase=0,
                 # l'objet handle correspond
                 # à une figure à mettre à jour
                 *, handle):
    # c'est ici qu'on modifie les données
    # utilisées pour produire la courbe
    courbe_trigo.data_source.data['y'] = \
       amplitude * function(frequency * x + phase)
    # et c'est ici qu'on provoque la mise à jour
    push_notebook(handle=handle)
```

```{code-cell}
# au moment où on matérialise l'objet figure
# on récupère une `handle` qui lui correspond
handle1 = show(figure1, notebook_handle=True)
```

```{code-cell}
# maintenant on peut créer un interacteur
interact(update_trigo, 
         # on peut définir les options sont des tuples (label, valeur)
         # et ici nos valeurs sont des fonctions
         function=Dropdown(options =(("sinus", np.sin),
                                     ("cosinus", np.cos),
                                     ("tangeante", np.tan))),
         frequency=(1,20),
         amplitude=[0.5, 1, 3, 5],
         phase=(0, 2*np.pi, 0.05),
         handle=fixed(handle1),
        );
```

## Complément : niveau intermédiaire

+++

### Une classe pour ce genre d'usages

+++

En termes de conception, notre approche jusqu'ici est améliorable.  
En effet par construction, nous devons partager des données entre l'initialisation et la mise à jour - cf. les variables globales comme `handle1` - et c'est, comme toujours, une pratique qu'on cherche à éviter.

Voici une approche qui va réaliser exactement la même fonction, mais basée sur une classe; on va tirer profit de l'instance pour ranger proprement toutes les données.

```{code-cell}
# première version d'une classe d'animation

class Animation:

    # la fonction doit être vectorisée
    def display(self, function, title, *,
               y_range=(-5, 5), height=300, width=600):
        self.figure = figure(
            title=title, y_range=y_range,
            plot_height=height, plot_width=width)
        self.x = np.linspace(0, 2*np.pi, 200)
        y = function(self.x)
        self.courbe = self.figure.line(self.x, y, color="#2222aa", line_width=3)
        self.handle = show(self.figure, notebook_handle=True)
        
    # on passe directement la fonction en paramètre
    def update(self, function, frequency, amplitude, phase):
        new_y = amplitude * function(frequency * self.x + phase)
        self.courbe.data_source.data['y'] = new_y
        push_notebook(handle=self.handle)
     
    def interact(self):
        # interact nous impose de passer une simple fonction
        # pour passer 'self' à cette fonction on crée une cloture
        def closure(function, frequency, amplitude, phase):
            self.update(function, frequency, amplitude, phase)
        interact(closure,
                 function = Dropdown(
                     options=(('sinus', np.sin), ('cosinus', np.cos), ('tangeante', np.tan))),
                 frequency=(1, 20),
                 amplitude=[0.5, 1, 3, 5],
                 phase=(0, 2*np.pi, 0.05),
                )
```

```{code-cell}
a1 = Animation()
a1.display(np.sin, "fonctions trigonométriques")
```

```{code-cell}
a1.interact()
```

**Remarque**

Je vous recommande cette pratique car, à nouveau, cela permet d'éviter les variables globales qui sont **toujours** une mauvaise idée; tous les morceaux interdépendants sont regroupés, ainsi on limite la possibilité de casser le code en ne modifiant qu'un morceau; la classe matérialise les interdépendances entre les objets `figure`, `handle` et `courbe`; remarquez qu'en fait on n'a pas strictement besoin de `self.figure` comme attribut de l'instance.

+++

*****

+++ {"slideshow": {"slide_type": "slide"}}

### Exemple : distribution uniforme

+++

Voyons un deuxième exemple avec `bokeh`. Vous pouvez prendre ceci comme un exercice, et le faire de votre côté avant de lire la suite du notebook.

+++

On veut ici écrire un outil qui déplace et déforme une distribution de points; on part d'une distribution de N points calculée aléatoirement une bonne fois au début dans le cercle unité; grâce aux réglages on pourra déformer ce nuage de points, qui va devenir une ellipse, grâce aux réglages suivants :

* `dx` et `dy`, les coordonnées du centre de l'ellipse,
* `rx` et `ry` les rayons en x et en y de l'ellipse,
* et enfin `alpha` l'angle de rotation de l'ellipse.

+++

****

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# petit utilitaire pour calculer la distribution
# uniforme de départ
def uniform_distribution(N):
    # on tire au hasard un rho et un rayon
    rhos = 2 * np.pi * np.random.sample(N)
    rads = np.random.sample(N)
    # il faut prendre la racine carrée du rayon
    # sinon ce n'est pas uniforme dans le plan
    circle_x = np.sqrt(rads) * np.cos(rhos)
    circle_y = np.sqrt(rads) * np.sin(rhos)
    return circle_x, circle_y
```

```{code-cell}
# regardons ça rapidement,  - avec matplotlib
# pour vérifier que la répartition est bien homogène
import matplotlib.pyplot as plt
```

```{code-cell}
plt.figure(figsize=(4, 4))
X, Y = uniform_distribution(2000)
plt.scatter(X, Y, marker='.', s=1, color='red');
```

#### un peu de variété

```{code-cell}
# et aussi: pour que ce soit plus joli 
# et surtout plus facile à suivre visuellement
# je tire au hasard des couleurs
# et des tailles pour les points
def enhanced_uniform_distribution(N):
    # on calcule la distribution initiale
    # (celle-ci est vraiment uniforme)
    # dans le cercle de rayon 1
    x, y = uniform_distribution(N)

    # le rouge entre 50 et 250
    reds = 50 + 200 * np.random.random(size=N)
    # le vert entre 30 et 250
    greens = 30 + 220 * np.random.random(size=N)
    # la mise en forme des couleurs
    # le bleu est constant à 150
    colors = [
        f"#{int(red):02x}{int(green):02x}{150:02x}"
        for red, green in zip(reds, greens)
    ]

    # les rayons des points; entre 0.05 et 0.25
    radii = 0.05 + np.random.random(size=N) * .20
    
    return x, y, colors, radii
```

```{code-cell}
# c'est ici qu'on commence à faire du bokeh

# j'applique la technique qu'on vient de voir
# en créant une classe 
# pour éviter les variables globales

class AnimatedDistribution:

    def __init__(self, N):
        self.N = N

        
    def show(self):
        # les choix des bornes sont très arbitraires
        # dans une version plus élaborée tous ces détails pourraient
        # être passés en paramètre au constructeur
        self.figure = figure(
            title="distribution pseudo-uniforme",
            plot_height=300, plot_width=300,
            x_range=(-10, 10),
            y_range=(-10, 10),
        )
        
        # on range x0 et y0 dans des attributs de l'instance
        # pour pouvoir faire les mises à jour
        self.x0, self.y0, colors, radii = enhanced_uniform_distribution(self.N)
        
        # le paquets de cercles
        self.cloud = self.figure.circle(
            self.x0, self.y0, 
            radius = radii,
            fill_color=colors, fill_alpha=0.6,
            line_color=None, line_width=.1,
        )
        
        # et enfin la poignée qui, à nouveau, sera nécessaire
        # pour les mises à jour
        self.handle = show(self.figure, notebook_handle=True)

    def update(self, rx, ry, dx, dy, alpha):
        # on recalcule les x et y
        # à partir des valeurs initiales
        s, c = np.sin(alpha), np.cos(alpha)
        x = dx + c * rx * self.x0 - s * ry * self.y0
        y = dy + s * rx * self.x0 + c * ry * self.y0
        self.cloud.data_source.data['x'] = x
        self.cloud.data_source.data['y'] = y
        push_notebook(handle=self.handle)        
        
    def interact(self):
        def closure(rx, ry, dx, dy, alpha):
            self.update(rx, ry, dx, dy, alpha)
        interact(closure,
            rx=FloatSlider(min=.5, max=8,
                           step=.1, value=1.),
            ry=FloatSlider(min=.5, max=8,
                           step=.1, value=1.),
            dx=(-3, +3, .2),
            dy=(-3, +3, .2),
            alpha=FloatSlider(min=0., max=np.pi,
                              step=.05, value=0.))
```

```{code-cell}
:cell_style: split

dist = AnimatedDistribution(1000)
dist.show()
```

```{code-cell}
:cell_style: split

# pour déformer / déplacer
dist.interact()
```

+++ {"cell_style": "split"}

le point étant ici de montrer que toutes les modifications sont lisses, sans l'effet de *flickering* qu'on obtiendrait en redessinant toute l'image à chaque fois

+++

***
***
***

+++

### Autres bibliothèques

+++

Pour terminer cette digression sur les solutions alternatives à `matplotlib`, j'aimerais vous signaler enfin rapidement quelques autres options disponibles actuellement.

+++

Comme on l'a dit en introduction, l'offre dans ce domaine est pléthorique, aussi si vous avez un témoignage à apporter sur une expérience que vous avez eue dans ce domaine, nous serons ravis de vous voir la partager dans le forum du cours.

+++

#### plotly

+++

[la bibliothèque `plotly`](https://plot.ly/).

Cette bibliothèque est disponible en open source, et l'offre commerciale de plotly est tournée vers le conseil autour de cette technologie. Comme pour `bokeh`, elle est conçue comme un hybride entre Python et JavaScript, au dessus de `d3.js`. En réalité, elle présente même la particularité d'offrir une API unique disponible depuis Python, JavaScript, et R.

+++

#### mpld3

+++

https://mpld3.github.io/

Je n'ai pas d'expérience à partager avec cette librairie, mais sur la papier l'approche semble prometteuse, puisqu'il s'agit (aussi) de conciler matplotlib [avec `d3.js`](d3js.org).

+++

#### k3d

+++

J'ai utilisé récemment [la librairie k3d](https://github.com/K3D-tools/K3D-jupyter/) et j'ai trouvé le résultat assez bluffant pour les visualisations 3d. C'est un outil assez spartiate en termes [de documentation](https://k3d-jupyter.org/), mais très performant. 

Cette librairie se prête bien à la technique d'interactions que nous avons développée dans ce notebook. On en verra un autre exemple dans un prochain notebook.

+++

## Complément - niveau avancé (voire oiseux)

+++

Simplement pour finir, j'aimerais revenir sur notre classe `Animation`.

On pourrait même considérer qu'une instance de notre classe `Animation` **est** une figure, et donc envisager de la faire hériter d'une classe `bokeh.figure`; sauf qu'en fait `bokeh.figure` n'est pas une classe mais une fonction (une *factory*, c'est-à-dire une fonction qui contruit des instances) :

```{code-cell}
# l'objet bokeh.figure est une factory, est pas une classe
# comme on le devine grâce aux minuscules
type(figure)
```

```{code-cell}
# la classe c'est celle-ci:
type(figure())
```

```{code-cell}
# qu'on peut importer comme ceci
from bokeh.plotting import Figure

type(figure()) is Figure
```

**Exercice (niveau avancé)** : 

vous semble-t-il possible de récrire la classe `Animation` comme une classe qui hérite cette fois de `Figure`; quels seraient les bénéfices de cette approche ?

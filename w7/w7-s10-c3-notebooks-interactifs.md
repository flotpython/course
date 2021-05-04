---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
notebookname: Notebooks interactifs
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Notebooks interactifs

+++

## Complément - niveau basique

+++

Pour conclure cette série sur les outils de visualisation, nous allons voir quelques fonctionnalités disponibles uniquement dans l'environnement des notebooks, et qui offrent des possibilités supplémentaires par rapport aux visualisations que l'on a vues jusqu'à maintenant.

+++

### installation

+++

Pour exécuter ou créer un notebook depuis votre ordinateur, il vous faut installer Jupyter, ce que se fait bien sûr depuis le terminal :
```bash
pip install jupyter
```

En 2020 il existe deux versions de l'interface Jupyter dites *classic* et *lab*, la seconde étant plus puissante en termes d'UI; pour installer le tout, faire plutôt

```bash
pip install jupyterlab
```

Pour lancer un serveur jupyter, faire selon le mode choisi
```bash
jupyter notebook
# ou
jupyter lab
```

+++

### Contenus

+++

Pour le contenu des notebooks :

* une cellule est marquée comme étant soit du code, soit du texte(markdown);
* pour les cellules de markdown, on peut très simplement :
  * insérer des formules mathématiques, en insérant un fragment de $\LaTeX$ entre deux simples `$`, comme $\forall x\in\mathbb{R}$, ou encore  
  sur une ligne séparée en entourant entre deux doubles dollars `$$`, comme 
  $$\forall \epsilon>0, \exists\alpha>0, \forall x, |x-x_0| < \epsilon \implies |f(x)-f(x_0|<\epsilon$$

  * et bien sûr [toute la panoplie des effets markdown](https://daringfireball.net/projects/markdown/syntax), quoi qu'il faut se méfier car tout cela n'est pas très bien standardisé actuellement.
* un notebook choisit son *kernel* (en clair son langage); le mot Jupyter vient de Julia + Python + R, et aujourd'hui il y a moyen de faire tourner presque tous les langages, même `bash` et `C++` (mais en mode interprété bien sûr)

+++

### Courbes

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

Comme on l'a déjà vu plein de fois, la bonne façon de créer un graphique matplotlib c'est avec la formule magique suivante :

```{code-cell} ipython3
# ça c'est pour choisir la sortie 'notebook' 
%matplotlib notebook

# et ça c'est pour dire 'interactive on'
# pour éviter de devoir plt.show() tout le temps
plt.ion()
```

Avec ces réglages - enfin surtout le premier - il y a pas mal de possibilités qui sont très pratiques :

* pour commencer on peut changer la taille de la courbe en cliquant sur le petit coin visible en bas à droite de la figure ![](media/matplotlib-resize.png)
* les courbes apparaissent avec un barre d'outils en dessous; entraînez-vous à utiliser par exemple **l'outil de zoom**, pour agrandir et vous déplacer dans la courbe ![](media/matplotlib-navigate.png)

+++

À titre d'exercice, sur cette courbe le nombre d'or correspond à une des racines du polynôme, à vous de trouver sa valeur avec une précision de

```{code-cell} ipython3
plt.figure(figsize=(2, 2))
X = np.linspace(-2, 2)
ZERO = X * 0
def golden(x):
    return x**2 - x - 1
plt.plot(X, golden(X));
plt.plot(X, ZERO);
```

Voici à quoi je suis arrivé de mon côté (je ne dis pas que c'est forcément la méthode la plus rapide pour trouver le nombre d'or ;-):  
Mais tous les outils de visualisation décents vons proposer des mécanismes analogues, soyez-y attentifs car ça fait parfois gagner beaucoup de temps.


<img src="media/matplotlib-zoomed.png" width=600px>

+++

### Exemple de notebook interactif

+++

Je vous signale enfin un [exemple de notebook publié par la célèbre revue *Nature*](http://www.nature.com/news/ipython-interactive-demo-7.21492), qui pourra vous donner une idée de ce qu'il est possible de faire avec un notebook interactif. Interactif dans le sens où on peut faire varier les paramètres d'une expérience et voir l'impact du changement se refléter immédiatement sur la visualisation.

Comme il n'est malheureusement plus actif en ligne semble-t-il, 
je vous invite à le faire marcher localement à partir [de la version sur github ici](https://github.com/jupyter/nature-demo).

+++

## Complément - niveau intermédiaire

+++

### Une visualisation interactive simple : `interact`

+++

Pour refaire de notre coté quelque chose d'analogue, nous allons commencer par animer la fonction sinus, avec un bouton pour régler la fréquence. Pour cela nous allons utiliser la fonction `interact` ; à nouveau c'est un utilitaire qui fait partie de l'écosystème des notebooks, et plus précisément du module `ipywidgets` :

```{code-cell} ipython3
# dans cette partie on a besoin de 
# revenir dans un mode plus usuel
%matplotlib inline
```

```{code-cell} ipython3
from ipywidgets import interact
```

+++ {"slideshow": {"slide_type": "-"}}

Dans un premier temps, j'écris une fonction qui prend en paramètre la fréquence, et qui dessine la fonction sinus sur un intervalle fixe de 0. à $4\pi$ :

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
def sinus(freq):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*X)
    plt.plot(X, Y)
```

```{code-cell} ipython3
:cell_style: split

sinus(1)
```

```{code-cell} ipython3
:cell_style: split

sinus(0.5)
```

Maintenant, plutôt que de tracer individuellement les courbes une à une, j'utilise `interact` qui va m'afficher une réglette pour changer le paramètre `freq`. Ça se présente comme ceci :

```{code-cell} ipython3
# je change maintenant la taille des visualisations
plt.rcParams["figure.figsize"] = (12, 4)
```

```{code-cell} ipython3
interact(sinus, freq=(0.5, 10., 0.25));
```

+++ {"slideshow": {"slide_type": "slide"}}

### Mécanisme d'`interact`

+++

La fonction `interact` s'attend à recevoir :

* en premier argument : une fonction `f` ;
* et ensuite autant d'arguments nommés supplémentaires que de paramètres attendus par `f`.

Comme dans mon cas la fonction `sinus` attend un paramètre nommé `freq`, le deuxième argument de `interact` lui est passé aussi avec le nom `freq`.

+++

### Les objets `Slider`

+++

Chacun des arguments à `interact` (en plus de la fonction) correspond à un objet de type `Slider` (dans la ménagerie de `ipywidget`). Ici en passant juste le tuple `(0.5, 10., 0.25)` j'utilise un raccourci pour dire que je veux pouvoir régler le paramètre `freq` sur une plage allant de `0.5` à `10` avec un pas de `0.25`.

+++

Mon premier exemple avec `interact` est en réalité équivalent à ceci :

```{code-cell} ipython3
from ipywidgets import FloatSlider
```

```{code-cell} ipython3
# exactement équivalent à la version ci-dessus
interact(sinus, freq=FloatSlider(min=0.5, max=10., step=0.25));
```

Mais en utilisant la forme bavarde, je peux choisir davantage d'options, comme notamment :

* mettre `continuous_update = False` ; l'effet de ce réglage, c'est que l'on met à jour la figure seulement lorsque je lâche la réglette ; c'est utile lorsque les calculs sont un peu lents, comme ici avec l'infrastructure notebook qui est à distance ;
* mettre `value=1.` pour choisir la valeur initiale :

```{code-cell} ipython3
# exactement équivalent à la version ci-dessus
# sauf qu'on ne redessine que lorsque la réglette
# est relâchée
interact(sinus, freq=FloatSlider(min=0.5, max=10., 
                                 step=0.25, value=1.,
                                 continuous_update=False));
```

### Plusieurs paramètres

+++

Voyons tout de suite un exemple avec deux paramètres, je vais écrire maintenant une fonction qui me permet de changer aussi la phase :

```{code-cell} ipython3
def sinus2(freq, phase):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*(X+phase))
    plt.plot(X, Y)
```

Et donc maintenant je passe à `interact` un troisième paramètre :

```{code-cell} ipython3
interact(sinus2,
         freq=FloatSlider(min=0.5, max=10., step=0.5,
                          continuous_update=False),
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6, 
                           continuous_update=False),
        );
```

+++ {"slideshow": {"slide_type": "slide"}}

### Bouche-trou : `fixed`

+++

Si j'ai une fonction qui prend plus de paramètres que je ne veux montrer de réglettes, je peux fixer un des paramètres  par exemple comme ceci :

```{code-cell} ipython3
from ipywidgets import fixed
```

```{code-cell} ipython3
# avec une fonction à deux argument,
# je peux en fixer un, et n'avoir qu'une réglette
# pour fixer celui qui est libre
interact(sinus2, freq=fixed(1.),
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6),
        );
```

+++ {"slideshow": {"slide_type": "slide"}}

## Widgets

+++

Il existe toute une famille de widgets, dont `FloatSlider` est l'exemple le plus courant, mais vous pouvez aussi :

* créer des radio bouton pour entrer un paramètre booléen ;
* ou une saisie de texte pour entre un paramètre de type `str` ;
* ou une liste à choix multiples…

Bref, vous pouvez créer une mini interface-utilisateur avec des objets graphiques simples choisis dans une palette assez complète pour ce type d'application.

Voyez [les détails complets sur `readthedocs.io`](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# de même qu'un tuple était ci-dessus un raccourci pour un FloatSlider
# une liste ou un dictionnaire est transformé(e) en un Dropdown
interact(sinus, freq={'rapide': 10., 'moyenne': 1., 'lente': 0.1});
```

+++ {"slideshow": {"slide_type": "slide"}}

Voyez la [liste complète des widgets ici](http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html).

+++

### Dashboards

+++

Lorsqu'on a besoin de faire une interface un peu plus soignée, on peut créer sa propre disposition de boutons et autres réglages.

+++

Voici un exemple de dashboard, uniquement pour vous donner une meilleure idée, qui pour changer agit sur une visualisation réalisée avec plot.ly plutôt que matplotlib :

```{code-cell} ipython3
import plotly
plotly.__version__
```

```{code-cell} ipython3
# on importe la bibliothèque plot.ly
import chart_studio.plotly as py
import plotly.graph_objs as go
```

```{code-cell} ipython3
# il est impératif d'utiliser plot.ly en mode 'offline' 
# pour in mode interactif, 
# car sinon les affichages sont beaucoup trop lents
import plotly.offline as pyoff

pyoff.init_notebook_mode()
```

```{code-cell} ipython3
# les widgets pour construire le tableau de bord
from ipywidgets import (interactive_output,
                        IntSlider, Dropdown, Layout, HBox, VBox, Text)
from IPython.display import display
```

```{code-cell} ipython3
# une fonction sinus à 4 réglages
# qu'on réalise pour changer avec plot.ly
# et non pas avec matplotlib
def sinus4(freq, phase, amplitude, domain):

    X = np.linspace(0., domain*np.pi, 500)
    Y = amplitude * np.sin(freq*(X+phase))

    data = [ go.Scatter(x=X, y=Y, mode='lines', name='sinus') ]
    # je fixe l'amplitude à 10 pour que les animations
    # soient plus parlantes
    layout = go.Layout(
        yaxis = {'range' : [-10, 10]},
        title="Exemple de graphique interactif avec dashboard",
        height=500,
        width=500,
    )
    figure = go.Figure(data=data, layout=layout)
    pyoff.iplot(figure)
```

```{code-cell} ipython3
:cell_style: center

def my_dashboard():
    """
    create and display a dashboard
    return a dictionary name->widget suitable for interactive_output
    """
    # dashboard pieces as widgets
    l_75 = Layout(width='75%')
    l_50 = Layout(width='50%')
    l_25 = Layout(width='25%')

    w_freq = Dropdown(options=list(range(1, 10)),
                      value = 1,
                      description = "fréquence",
                      layout=l_50)
    w_phase = FloatSlider(min=0., max = 2*np.pi, step=np.pi/12,
                          description="phase",
                          value=0., layout=l_75)
    w_amplitude = Dropdown(options={"micro" : .1,
                                    "mini" : .5,
                                    "normal" : 1.,
                                    "grand" : 3.,
                                    "énorme" : 10.},
                           value = 3.,
                           description = "amplitude",
                           layout = l_25)
    w_domain = IntSlider(min=1, max=10, description="dom. n * π", layout=l_50)

    # make up a dashboard
    dashboard = VBox([HBox([w_amplitude, w_phase]),
                      HBox([w_domain, w_freq]),
                     ])
    display(dashboard)
    return dict(freq=w_freq, phase=w_phase,
                amplitude=w_amplitude, domain=w_domain)
```

*****
Avec tout ceci en place on peut montrer un dialogue interactif pour changer tous les paramètres de sinus4.

```{code-cell} ipython3
# interactively call sinus4
# attention il reste un bug:
# au tout début rien ne s'affiche,
# il faut faire bouger au moins un réglage
interactive_output(sinus4, my_dashboard())
```

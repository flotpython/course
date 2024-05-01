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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
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
nbhosting:
  title: Notebooks interactifs
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
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

Pour exécuter ou créer un notebook depuis votre ordinateur, il vous faut installer Jupyter, ce qui se fait bien sûr depuis le terminal :
```bash
pip install jupyter
```

En 2023 on recommande l'interface Jupyter dite *lab*:

Pour le lancer, tapez dans le terminal:
```bash
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
# ça c'est pour choisir la sortie 'interactive'
# nécessite un `pip install ipympl`
%matplotlib ipympl
```

**À noter**  
* il y a eu pas mal de changements dans cette zone de l'écosystème, notamment en 2023 avec la déprécation du notebook dit "classic"
  du coup le code de ce notebook est assez fragile, n'hésitez pas à chercher de votre coté sur google si vous rencontrez des soucis
* si vous voulez **changer de *driver*** de sortie pour matplotlib  
  (c'est-à-dire si par exemple vous avez executé `%matplotlib inline` et qu'ensuite vous voulez changer et utiliser `%matplotlib ipympl`)  
  il vous faudra alors ***redémarrer votre kernel***
* aussi, pour utiliser le driver *ipympl* il est nécessaire d'installer `pip install ipympl`

+++

Avec le driver *ipympl*, il y a pas mal de possibilités qui sont très pratiques :

+++

* pour commencer on peut changer la taille de la courbe en cliquant sur le petit coin visible en bas à droite de la figure

![](media/matplotlib-resize.png)

+++

* les courbes apparaissent avec un barre d'outils en dessous; entraînez-vous à utiliser par exemple **l'outil de zoom**, pour agrandir et vous déplacer dans la courbe

![](media/matplotlib-navigate.png)

+++

À titre d'exercice, sur cette courbe le nombre d'or correspond à une des racines du polynôme, à vous de trouver sa valeur avec une précision de $10^{-6}$

```{code-cell} ipython3
plt.figure(figsize=(8, 3))
X = np.linspace(-2, 2)
ZERO = X * 0
def golden(x):
    return x**2 - x - 1
plt.plot(X, golden(X));
plt.plot(X, ZERO);
```

Voici à quoi je suis arrivé de mon côté (je ne dis pas que c'est forcément la méthode la plus rapide pour trouver le nombre d'or ;-).  
Mais tous les outils de visualisation décents vont proposer des mécanismes analogues, soyez-y attentifs car ça fait parfois gagner beaucoup de temps.

![](media/matplotlib-zoomed.png)

+++

### Exemple de notebook interactif

+++

Je vous signale enfin un [exemple de notebook publié par la célèbre revue *Nature*](http://www.nature.com/news/ipython-interactive-demo-7.21492), qui pourra vous donner une idée de ce qu'il est possible de faire avec un notebook interactif. Interactif dans le sens où on peut faire varier les paramètres d'une expérience et voir l'impact du changement se refléter immédiatement sur la visualisation.

**Mise à jour**: comme il n'est **malheureusement plus actif** en ligne semble-t-il, 
je vous invite à le faire marcher localement à partir [de la version sur github ici](https://github.com/jupyter/nature-demo).

+++

## Complément - niveau intermédiaire

+++

### Une visualisation interactive simple : `interact`

+++

Pour refaire de notre coté quelque chose d'analogue, nous allons écrire une sorte d'oscilloscope virtuel, c'est-à-dire animer la fonction sinus, avec un bouton pour régler la fréquence.  
Pour cela nous allons utiliser la fonction `interact`; c'est un utilitaire qui fait partie de l'écosystème des notebooks, et plus précisément du module `ipywidgets`.

**Note:**
avec le mode `%matplotlib inline` le code est légèrement plus simple, mais pour rester cohérent, nous montrons ici comment faire ce genre de choses avec le mode `%matplotlib ipympl`

```{code-cell} ipython3
from ipywidgets import interact
```

Nous expliquerons tout cela un peu plus loin, mais voici comment on pourrait s'y prendre.

```{code-cell} ipython3
# créer une figure - et trouver les axes
# on le fait une seule fois - et donc pas dans la fonction sinus 
fig, ax = plt.subplots()

# cette fonction va être appelée sans arrêt
# son job est de nettoyer la courbe précédente
# et d'afficher la nouvelle pour freq
def sinus(freq):
    # le domaine en X
    X = np.linspace(0., 4*np.pi, 200)
    # les Y
    Y = np.sin(freq*X)

    # nettoyer la ligne précédente
    for line in ax.lines:
        line.remove()
    # dessiner la courbe pour freq
    # (on précise une couleur, sinon mpl en choisit 
    # une au hasard à chaque fois, c'est vilain..)
    ax.plot(X, Y, color='DarkBlue')

# et maintenant le morceau de bravoure
# on affiche un "slider" - une réglette - qui réappelle 'sinus' 
# à chaque changement de la valeur de 'freq'

interact(sinus, freq=(0.5, 10., 0.25));

# voyez comment vous pouvez choisir 'freq' avec la réglette
```

+++ {"slideshow": {"slide_type": "slide"}}

### Mécanisme d'`interact`

+++

Le mécanisme général, c'est que la fonction `interact` s'attend à recevoir :

* en premier argument : une fonction `f` ;
* et ensuite autant d'arguments nommés supplémentaires que de paramètres attendus par `f`.

Comme dans mon cas la fonction `sinus` attend un paramètre nommé `freq`, le deuxième argument de `interact` lui est passé aussi avec le nom `freq`; c'est pourquoi à la fin on appelle:

    interact(sinus, freq=...)

+++

### Les objets `Slider`

+++

Chacun des arguments à `interact` - en plus de la fonction - correspond à un objet de type `Slider` (dans la ménagerie de `ipywidgets`). Ici en passant juste le tuple `(0.5, 10., 0.25)` j'utilise un raccourci pour dire que je veux pouvoir régler le paramètre `freq` sur une plage allant de `0.5` à `10` avec un pas de `0.25`.

+++

Mon premier exemple avec `interact` est en réalité équivalent à ceci :

```{code-cell} ipython3
from ipywidgets import FloatSlider
```

```{code-cell} ipython3
# exactement équivalent à la version ci-dessus

# je recrée une nouvelle figure, sinon la réglette
# irait modifier .. la figure ci-dessus
fig, ax = plt.subplots()

interact(sinus, freq=FloatSlider(min=0.5, max=10., step=0.25));
```

Mais en utilisant la forme bavarde, je peux choisir davantage d'options, comme notamment :

* mettre `continuous_update = False` ; l'effet de ce réglage, c'est que l'on met à jour la figure seulement lorsque je lâche la réglette ; c'est utile lorsque les calculs sont un peu lents, comme ici avec l'infrastructure notebook qui est à distance ;
* mettre `value=1.` pour choisir la valeur initiale :

```{code-cell} ipython3
fig, ax = plt.subplots()

# exactement équivalent à la version ci-dessus
# sauf qu'on ne redessine que lorsque la réglette
# est relâchée
interact(sinus, freq=FloatSlider(min=0.5, max=10., 
                                 step=0.25, value=1.,
                                 continuous_update=False));
```

### Plusieurs paramètres

+++

Voyons tout de suite un exemple avec deux paramètres, je vais écrire maintenant une fonction qui me permet de changer aussi la phase.  
Et donc maintenant:

- la fonction prend 2 paramètres - c'est pourquoi je l'appelle `sinus2`
- et je passe à `interact` un troisième paramètre, qui est la réglette pour choisir le second paramètre `phase`

```{code-cell} ipython3
fig, ax = plt.subplots()

def sinus2(freq, phase):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*(X+phase))
    
    for line in ax.lines:
        line.remove()
    ax.plot(X, Y, color='DarkGreen')

interact(sinus2, 
         freq=FloatSlider(min=0.5, max=10., step=0.5),
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6));
```

+++ {"slideshow": {"slide_type": "slide"}}

### Bouche-trou : `fixed`

+++

Si j'ai une fonction qui prend plus de paramètres que je ne veux montrer de réglettes, je peux fixer un des paramètres en utilisant l'utilitaire `fixed`; c'est comme si on créait une réglette avec une valeur fixe, du coup on n'a même pas besoin de montrer cette réglette.

Pour illustrer ce point on va utiliser `sinus2` et reproduire le comportement qu'on avait avec `sinus`:

```{code-cell} ipython3
from ipywidgets import fixed
```

```{code-cell} ipython3
fig, ax = plt.subplots()

interact(sinus2, 
         # le premier paramètre de sinus2 est toujours 1
         freq=fixed(1),
         # et on peut régler le second paramètre uniquement
         phase=FloatSlider(min=0., max=2*np.pi, step=np.pi/6));
```

+++ {"slideshow": {"slide_type": "slide"}}

### Widgets

+++

Sachez qu'il existe toute une famille de widgets, dont `FloatSlider` est l'exemple le plus courant, mais vous pouvez aussi :

* créer un radio bouton pour entrer un paramètre booléen ;
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
fig, ax = plt.subplots()
interact(sinus, freq={'rapide': 10., 'moyenne': 1., 'lente': 0.1});
```

+++ {"slideshow": {"slide_type": "slide"}}

Voyez la [liste complète des widgets ici](http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html).

+++

### Forme avec décorateur

Signalons enfin, et pour finir, qu'il est possible également d'utiliser `interact` comme un décorateur, qui donne une forme un tout petit peu plus concise; voici comment on récrirait alors notre tout premier exemple:

```{code-cell} ipython3
fig, ax = plt.subplots()

@interact(freq=(0.5, 10., 0.25))
def sinus(freq):
    X = np.linspace(0., 4*np.pi, 200)
    Y = np.sin(freq*X)

    # nettoyer la ligne précédente
    for line in ax.lines:
        line.remove()
    # dessiner la courbe pour freq
    # (on précise une couleur, sinon mpl en choisit 
    # une au hasard à chaque fois, c'est vilain..)
    ax.plot(X, Y, color='DarkBlue')
```

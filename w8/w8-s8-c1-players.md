---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
notebookname: 'Un exemple: players'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# `asyncio`  - un exemple un peu plus réaliste

+++

## Complément - niveau avancé

+++

Pour des raisons techniques, il n'est pas possible de mettre en ligne un notebook pour les activités liées au réseau, qui sont pourtant clairement dans le coeur de cible de la bibliothèque - souvenez-vous que ce paradigme de programmation a été développé au départ par les projets comme tornado, qui se préoccupe de services Web.

+++

Aussi, pour illustrer les possibilités offertes par `asyncio` sur un exemple un peu plus significatif que ceux qui utilisent `asyncio.sleep`, nous allons écrire le début d'une petite architecture de jeu.

Il s'agit pour nous principalement d'illustrer les capacités de `asyncio` en matière de gestion de sous-processus, car c'est quelque chose que l'on peut déployer dans le contexte des notebooks.

+++

Nous allons procéder en deux temps. Dans ce premier notebook nous allons écrire un petit programme Python qui s'appelle `players.py`. C'est une brique de base dans notre architecture, dans le second notebook on écrira un programme qui lance (sous la forme de sous-processus) plusieurs instances de `players.py`.

+++

### Le programme `players.py`

+++

Mais dans l'immédiat, voyons ce que fait `players.py`. On veut modéliser le comportement de plusieurs joueurs.

Chaque joueur a un comportement hyper basique, il émet simplement à des intervalles aléatoires un événement du type :

> je suis le joueur John et je vais dans la direction Nord

Chaque joueur a un nom, et une fréquence moyenne, et un nombre de cycles.

Par ailleurs pour être un peu vraisemblable, il y a quatre directions `N`, `S`, `E` et `W`, mais que l'on n'utilisera pas vraiment dans la suite.

+++

<a href="data/players.py">Voyez ici le code de `players.py`</a>

+++

Comme vous le voyez, dans ce premier exemple nous n'utilisons à nouveau que `asyncio.sleep` pour modéliser chaque joueur, dont la logique peut être illustrée simplement comme ceci (où la ligne horizontale représente le temps) :

+++

![](media/player.png)

+++

### configurations prédéfinies

Pour éviter de nous noyer dans des configurations compliquées, on a embarqué dans `players` plusieurs (4) configurations prédéfinies - voyez la globale `predefined`.

+++

Dans tous les cas **chacune de ces configurations crée deux joueurs**.

```{code-cell}
# par exemple la config. prédéfinie # 1 
# ressemble à ceci
from data.players import predefined

for predef, players in predefined.items():
     print(f"predefined {predef}: {players}")
```

Ce qui signifie qu'avec la config. #1, on génére 3 événements pour `john`, et 7 pour `mary`; et la durée entre les événements de `john` est tirée au hasard entre 0 et 0.8s.

+++

La logique des deux joueurs est simplement juxtaposée, ou si on préfère superposée, par `asyncio.gather`, ce qui fait que la sortie de `players.py` ressemble à ceci :

+++

![](media/players.png)

```{code-cell}
:cell_style: split

# je peux lancer un sous-processus
# depuis le notebook
# ici la config #1
!data/players.py
```

```{code-cell}
:cell_style: split

# ou une autre configuration
!data/players.py 2
```

Nous allons voir dans le notebook suivant comment on peut orchestrer plusieurs instances du programme `players.py`, et prolonger cette logique de juxtaposition / mélange des sorties, mais cette fois au niveau de plusieurs processus.

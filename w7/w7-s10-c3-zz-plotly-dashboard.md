---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
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
  title: Un dashboard
---

# Un dashboard, avec un peu de plotly pour changer

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau avancé

```{code-cell} ipython3
import numpy as np
```

### Dashboards

+++

Lorsqu'on a besoin de faire une interface un peu plus soignée, on peut créer sa propre disposition de boutons et autres réglages.

+++

Voici un exemple de dashboard, uniquement pour vous donner une meilleure idée, qui pour changer agit sur une visualisation réalisée **avec la librairie `plot.ly`** plutôt que matplotlib :

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
# pour un mode interactif, 
# car sinon les affichages sont beaucoup trop lents
import plotly.offline as pyoff

pyoff.init_notebook_mode()
```

Cette fois-ci notre prétexte sera d'afficher une fonction sinus qui prend cette fois 4 paramètres:

```{code-cell} ipython3
# les widgets pour construire le tableau de bord
from ipywidgets import (interactive_output,
                        FloatSlider, IntSlider, Dropdown, Layout, HBox, VBox, Text)
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
        height=400,
        width=750,
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
    w_domain = IntSlider(min=1, max=10, description="dom. n * π", value=2, layout=l_50)

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

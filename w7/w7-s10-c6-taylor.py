# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     cell_metadata_json: true
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: 'Application: Taylor'
#   version: '1.0'
# ---

# %% [markdown]
# # Le théorème de Taylor illustré

# %% [markdown]
# ## Exercice : niveau avancé

# %%
from math import factorial

from ipywidgets import interact, IntSlider, Layout

# to compute derivatives
import autograd
import autograd.numpy as np

# %%
from bokeh.plotting import figure, show
from bokeh.io import push_notebook, output_notebook

output_notebook()


# %% {"hide_input": true}
class Taylor:
    """
    provides an animated view of Taylor approximation
    one can change the degree interactively
    built from a vectorized function and the X (linspace) domain
    derivatives are computed on X=0, translate as needed
    """
    def __init__(self, function, domain):
        self.function = function
        self.domain = domain
        self.regular_y = function(self.domain)
        
    # we need to set a fixed y_range for smooth transitions
    def create(self, y_range):
        x_range = (self.domain[0], self.domain[-1])
        self.figure = figure(title=self.function.__name__,
                             x_range=x_range, y_range=y_range)
        self.line_exact = self.figure.line(
            self.domain, self.regular_y, color='green')
        self.line_approx = self.figure.line(
            self.domain, self.approximated(0), color='red', line_width=2)
        self.handle = show(self.figure, notebook_handle=True)
        
    def approximated(self, degree):
        # degree 0
        result = (0*self.domain + 1) * self.function(0.)
        derivative = autograd.grad(self.function)
        for n in range(1, degree+1):
            # the term in f(n)(x)/n!
            result += derivative(0.)/factorial(n) * self.domain**n
            derivative = autograd.grad(derivative)
        return result

    def update(self, degree):
        self.line_approx.data_source.data['y'] = self.approximated(degree)
        push_notebook(handle=self.handle)
        
    def interact(self, degree_widget):
        interact(lambda degree: self.update(degree), degree=degree_widget)


# %% [markdown]
# ### sinus

# %% {"scrolled": false}
# between -4π and 4π
DOMAIN = np.linspace(-4*np.pi, 4*np.pi, 250)

# fixed limits in Y
Y_RANGE = (-1.5, 1.5)

# select a degree
widget = IntSlider(
   min=1, max=33, step=2,      # sinus being odd we skip even degrees
   layout=Layout(width='100%'))

### ready to go
interactor = Taylor(np.sin, DOMAIN)
interactor.create(Y_RANGE)
interactor.interact(widget)

# %% [markdown]
# ### cosinus

# %% {"scrolled": false}
# allows to select a degree
widget2 = IntSlider(
   min=0, max=34, step=2,      # sinus being odd we skip even degrees
   layout=Layout(width='100%'))

### ready to go
interactor = Taylor(np.cos, DOMAIN)
interactor.create(Y_RANGE)
interactor.interact(widget2)

# %% [markdown]
# ### exponential

# %% {"scrolled": false}
# allows to select a degree
widget3 = IntSlider(min=0, max=11,
   layout=Layout(width='100%'))

### ready to go
interactor = Taylor(np.exp, np.linspace(-4, 4, 200))
interactor.create((-10, 60))
interactor.interact(widget3)

# %% [markdown]
# ****
# ****
# à finir de rédiger
# ****
# ****

# %%
import math
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# on va prendre pour commencer la fonction sinus, disons entre -π et π
#
# on applique ici le théorème de Taylor en $x_0 = 0$, à titre d'exercice vous pouvez le modifier pour pouvoir spécifier un autre point de référence
#

# %%
# prenons un domaine entre -π et π
borne = np.pi

X = np.linspace(-borne, borne)

# %%
# on la dessine 
Y = np.sin(X)
plt.plot(X, Y);


# %% [markdown]
# Le théorème de Taylor nous permet d'approximer cette fonction par une série de polynômes.  
# on va montrer ce que ça donne dans le cas de sinus en 0, selon le nombre de termes que l'on prend dans la série, le résultat est assez impressionnant.

# %% [markdown]
# ## approche naïve

# %% [markdown]
# ### ordre 1

# %% [markdown]
# pour commencer on se définit une fonction qui dessine sur la même figure deux fonctions - l'originale et l'approximation  
# on suppose les deux fonctions définies sur le même domaine  
#
# il y a une petite subtilité avec l'axe des y; si on ne précise rien à matplotlib, lorsqu'on dessine deux fonctions, il va calculer les valeurs maximales prises par l'une ou l'autre des fonctions, et s'en servir pour déterminer l'échelle des y; avec des polynômes de degré élevé, les approximations loin du 0 divergent fortement, aussi il est utile de fixer l'échelle en y. 

# %%
# le défaut pour l'échelle en y est adapté pour sinus / cosinus
def plot_2_functions(X, Y, Y_approx, ymin=-2, ymax=2):
    # on fixe la taille de la figure
    plt.figure(figsize=(12, 8))
    # et aussi les bornes en Y 
    plt.ylim(ymin, ymax)
    # maintenant on peut plotter les deux fonctions
    plt.plot(X, Y)
    plt.plot(X, Y_approx)


# %%
# la formule de Taylor à l'ordre 1 assimile sin(x) à x

Y1 = X
plot_2_functions(X, Y, Y1)

# %% [markdown]
# ### ordre 3

# %% [markdown]
# comme *sin* est impaire, les dérivées d'ordre pair de *sin* sont nulles, on passe donc à l'ordre 3
#
# pour calculer l'ordre 3 on ajoute à l'ordre 1 le terme $-\frac{x^3}{6}$
#

# %%
Y3 = Y1 - X**3 / 6
plot_2_functions(X, Y, Y3)


# %% [markdown]
# ça commence à coller..

# %% [markdown]
# ## ordres supérieurs

# %% [markdown]
# pour passer à des ordres plus grands, on va automatiser un peu plus  
# pour cela on écrit une fonction qui calcule le terme de Taylor d'ordre n  
#
# en entrée de cette fonction on a besoin :
#
# * comme toujours du domaine X
# * et des dérivées successives de la fonction - ici sinus - en 0  
# * et de l'ordre où on veut s'arrêter

# %%
def taylor(X, derivatives, n):
    """
    Parameters:
      X: le domaine 
      derivatives: les dérivées successives en 0; i.e. 
        derivatives[0] = f(0), 
        derivatives[1] = f'(0), 
        etc..
      n: ordre de l'approximation
    """
    result = np.zeros(len(X))
    for k, derivative in zip(range(n+1), derivatives):
        result = result + (derivative * (X**k) / math.factorial(k))
    return result                   


# %% [markdown]
# **remarque 1**  
# plutôt que de passer en troisième paramètre l'ordre où on veut s'arrêter, 
# on pourrait bien sûr passer en second paramètre un itérable fini; 
# on préfère procéder comme ceci, car comme on va le voir, il est possible
# pour les dérivées successives d'utiliser un itérateur infini, qui sera du coup
# toujours le même quel que soit l'ordre auquel on s'intéresse.

# %% [markdown]
# **remarque 2**  
#
# dans une première version j'avais écrit ceci
#
# ```python
#         result += (derivative * (X**k) / math.factorial(k))
# ```
#
# il se trouve que cette cette façon d'écrire les choses a soulevé des problèmes de conversions entre types de données, par ex. avec sinus à partir de l'ordre 21
#
# en effet lorsqu'on essaie de faire le calcul à l'ordre 21, on calcule à un moment $21!$ qui ne "tient plus" dans un entier 64 bits; avec les types de base de Python (`int` et `float`) cela ne poserait pas de problème particulier, mais ici avec numpy, c'est un souci...

# %%
# à partir de 21, le factoriel ne tient plus sur un entier de 64 bits

from math import factorial

factorial(19) <= 2**64 <= factorial(21)

# %% [markdown]
# ### rappel sur les itérateurs

# %% [markdown]
# dans le cas de *sin*, les dérivées successives en 0 sont cycliques et valent

# %%
# ordre
# 0   1   2   3   4   5   6   7 ...
# dérivée
# 0   1   0  -1   0   1   0  -1 ...

# %%
# et pour itérer sur un patron cyclique, en Python on utilise itertools.cycle
import itertools

def sinus_derivatives():
    return itertools.cycle( (0, 1, 0, -1) )


# %% {"cell_style": "center", "slideshow": {"slide_type": "notes"}}
iterator = sinus_derivatives()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# %% [markdown]
# il faut juste faire attention toutefois à bien utiliser à chaque fois un itérateur tout neuf :

# %% {"cell_style": "split"}
# ici on va continuer la boucle à -1
for i in iterator:
    print(i)
    break

# %% {"cell_style": "split"}
# comme ça c'est OK
for i in sinus_derivatives():
    print(i)
    break

# %% [markdown]
# ### ordre 5

# %%
# on peut maintenant afficher n'importe quel ordre
plot_2_functions(X, Y, taylor(X, sinus_derivatives(), 5))

# %% [markdown]
# c'est effectivement de mieux en mieux

# %% [markdown]
# ***

# %% [markdown]
# ## agrandissons le  domaine

# %% [markdown]
# avec ceci en place, on peut maintenant voir l'approximation de Taylor de *sin* à n'importe quel ordre ;
#
# pour mieux voir ce que ça donne nous allons élargir le domaine d'observation

# %%
big_borne = 4 * math.pi
BIGX = np.linspace(-big_borne, big_borne, 200)
BIGY = np.sin(BIGX)

# %%
# c'est très étonnant comme ça fonctionne bien
plot_2_functions(BIGX, BIGY, taylor(BIGX, sinus_derivatives(), 7))

# %%
plot_2_functions(BIGX, BIGY, taylor(BIGX, sinus_derivatives(), 11))

# %%
plot_2_functions(BIGX, BIGY, taylor(BIGX, sinus_derivatives(), 19))

# %% [markdown]
# ## une version interactive

# %% [markdown]
# pour éviter d'encombrer l'écran de dessins, on peut créer une micro UI pour faire bouger le paramètre 'n'

# %%
from ipywidgets import interact, IntSlider, Layout

# commodité
full_width = Layout(width='100%')


# %%
def interactive_sinus_taylor(n):
    plot_2_functions(BIGX, BIGY, taylor(BIGX, sinus_derivatives(), n))


# %%
# utilisez la réglette pour changer l'ordre
# apparemment à l'ordre 21 les choses se compliquent
interact(interactive_sinus_taylor, n=IntSlider(3, min=1, max=33, step=2, layout=full_width));


# %% [markdown]
# ## exponentielle

# %% [markdown]
# on a tout ce qui est nécessaire pour étudier une autre fonction; prenons le cas de $e^x$

# %%
def exp_derivatives():
    return itertools.repeat(1)


# %%
# le domaine
EXP_MAX_X = 10
EXP_MIN_X = -5


def interactive_exponential_taylor(min_x, max_x, max_degree):
    
    # un peu de place en haut et en bas
    max_y = np.exp(max_x) * 1.2
    min_y = -max_y/5

    EXPX = np.linspace(min_x, max_x)
    EXPY = np.exp(EXPX)

    def interactive_exp_taylor(n):
        plot_2_functions(EXPX, EXPY, taylor(EXPX, exp_derivatives(), n),
                         ymin=min_y, ymax=max_y)

   
    interact(interactive_exp_taylor,
             n=IntSlider(1, min=1, max=max_degree, layout=full_width));

# %%
# entre -4 et 4
# à l'ordre 8 c'est déjà très correct
interactive_exponential_taylor(-4, 4, 11)

# %%
# agrandissons le domaine
interactive_exponential_taylor(-5, 10, 17)

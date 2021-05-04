---
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
notebookname: TimeSeries
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Séries temporelles en `pandas`

+++

## Complément - niveau intermédiaire

+++

### Parsing des dates et gestion des erreurs

+++

Lorsqu'il y a des erreurs de parsing des dates, pandas offre la possibilité de lancer une exception, ou de produire un objet `NaT` pour *Not a Time* qui se manipule ensuite comme un `NaN`.

```{code-cell} ipython3
import pandas as pd
date = '100/06/2018' # cette date ne peut pas être parsée

try:
    pd.to_datetime(date) # comportement pas défaut qui lance une exception
except ValueError as e:
    print(e)
```

```{code-cell} ipython3
# retourne l'input en cas d'erreur
pd.to_datetime(date, errors='ignore')
```

```{code-cell} ipython3
# retourne NaT en cas d'erreur
pd.to_datetime(date, errors='coerce')
```

```{code-cell} ipython3
# la dernière date n'est pas valide
d = pd.to_datetime(['jun 2018', '10/12/1980',
                    '25 january 2000', '100 june 1900'], 
                   errors='coerce')
print(d)
```

```{code-cell} ipython3
# on peut utiliser les méthodes pour les NaN directement sur un NaT
d.fillna(pd.to_datetime('10 june 1980'))
```

### Pour aller plus loin

+++

Vous trouverez de nombreux exemples [dans la documentation officielle de pandas](https://pandas.pydata.org/pandas-docs/stable/timeseries.html)

+++

## Conclusion

+++

Ce notebook clôt notre survol de `numpy` et `pandas`. C'est un sujet vaste que nous avons déjà largement dégrossi. Pour aller plus loin vous avez évidemment la documentation officielle de `numpy` et `pandas` :

* [reference numpy](https://docs.scipy.org/doc/numpy-1.13.0/reference/)
* [reference pandas](http://pandas.pydata.org/pandas-docs/stable/index.html)

+++

Mais vous avez aussi l'excellent livre de Jake VanderPlas "Python Data Science Handbook" qui est entièrement disponible sous forme de notebooks en ligne :

<https://github.com/jakevdp/PythonDataScienceHandbook>

Il s'agit d'un très beau travail (c'est rare) utilisant les dernières versions de Python, `pandas` and `numpy` (c'est encore plus rare), fait par un physicien qui fait de la data science et qui a contribué au développement de nombreux modules de data science en Python.

Je vous conseille par ailleurs, pour ceux qui sont à l'aise en anglais, [une série de 10 vidéos sur YouTube](https://www.youtube.com/watch?v=_ZEWDGpM-vM) publiées par le même Jake VanderPlas, où il étudie un jeu de données du début (chargement des données) à la fin (classification).

+++

Pour finir, si vous voulez faire de la data science, il y a un livre incontournable : "An Introduction de Statistical Learning" de G. James, D. Witten, T. Hastie, R. Tibshirani. Ce livre utilise R, mais vous pouvez facilement l'appliquer en utilisant `pandas`.

Les auteurs mettent à disposition gratuitement le PDF du livre ici :

<http://www-bcf.usc.edu/~gareth/ISL/>

+++

N'oubliez pas, si ces ressources vous sont utiles, d'acheter ces livres pour supporter ces auteurs. Les ressources de grande qualité sont rares, elles demandent un travail énorme à produire, elles doivent être encouragées et recompensées.

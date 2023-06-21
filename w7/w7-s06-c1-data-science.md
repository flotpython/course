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
notebookname: Data Science
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La data science en général
## et en Python en particulier

+++

## Complément - niveau intermédiaire

+++

### Qu'est-ce qu'un data scientist ?

+++

J'aimerais commencer cette séquence par quelques réflexions générales sur ce qu'on appelle data science. Ce mot valise, récemment devenu à la mode, et que tout le monde veut ajouter à son CV, est un domaine qui regroupe tous les champs de l'analyse scientifique des données. Cela demande donc, pour être fait sérieusement, de maîtriser :

1. un large champ de connaissances scientifiques, notamment des notions de statistiques appliquées ;
2. les données que vous manipulez ;
3. un langage de programmation pour automatiser les traitements.

+++

#### Statistiques appliquées

+++

Pour illustrer le premier point, pour quelque chose d'aussi simple qu'une moyenne, il est déjà possible de faire des erreurs. Quel intérêt de considérer une moyenne d'une distribution bimodale ?

Par exemple, j'ai deux groupes de personnes et je veux savoir lequel a le plus de chance de gagner à une épreuve de tir à la corde. L'âge moyen de mon groupe A est de 55 ans, l'âge moyen de mon groupe B est de 30 ans. Il me semble alors pouvoir affirmer que le groupe B a plus de chances de gagner. Seulement, dans le groupe B il y a 10 enfants de 5 ans et 10 personnes de 55 ans et dans le groupe A j'ai une population homogène de 20 personnes ayant 55 ans. Finalement, ça sera sans doute le groupe A qui va gagner.

Quelle erreur ai-je faite ? J'ai utilisé un outil statistique qui n'était pas adapté à l'analyse de mes groupes de personnes. Cette erreur peut vous paraître stupide, mais ces erreurs peuvent être très subtiles voire extrêmement difficiles à identifier.

+++

#### Connaissance des données

+++

C'est une des parties les plus importantes, mais largement sous estimées : analyser des données sur lesquelles on n'a pas d'expertise est une aberration. Le risque principal est d'ignorer l'existence d'un facteur caché, ou de supposer à tort l'indépendance des données (sachant que nombre d'outils statistiques ne fonctionnent que sur des données indépendantes). Sans rentrer plus dans le détail, je vous conseille de lire cet article de [David Louapre sur le paradoxe de Simpson](https://sciencetonnante.wordpress.com/2013/04/29/le-paradoxe-de-simpson/) et [la vidéo associée](https://www.youtube.com/watch?v=vs_Zzf_vL2I), pour vous donner l'intuition que travailler sur des données qu'on ne maîtrise pas peut conduire à d'importantes erreurs d'interprétation.

+++

#### Maîtrise d'un langage de programmation

+++

Comme vous l'avez sans doute compris, le succès grandissant de la data science est dû à la démocratisation d'outils informatiques comme R, ou la suite d'outils disponibles dans Python, dont nous abordons certains aspects cette semaine.

Il y a ici cependant de nouveau des difficultés. Comme nous allons le voir il est très facile de faire des erreurs qui seront totalement silencieuses, par conséquent, vous obtiendrez presque toujours un résultat, mais totalement faux. Sans une profonde compréhension des mécanismes et des implémentations, vous avez la garantie de faire n'importe quoi.

Vous le voyez, je ne suis pas très encourageant, pour faire de la data science vous devrez maîtriser la bases des outils statistiques, comprendre les données que vous manipulez et maîtriser parfaitement les outils que vous utilisez. Beaucoup de gens pensent qu'en faisant un peu de R ou de Python on peut s'affirmer data scientist, c'est faux, et si vous êtes, par exemple, journaliste ou économiste et que vos résultats ont un impact politique, vous avez une vraie responsabilité et vos erreurs peuvent avoir d'importantes conséquences.

+++

### Présentation de `pandas`

+++

`numpy` est l'outil qui permet de manipuler des tableaux en Python, et `pandas` est l'outil qui permet d'ajouter des index à ces tableaux. Par conséquent, `pandas` repose entièrement sur `numpy` et toutes les données que vous manipulez en `pandas` sont des tableaux `numpy`.

`pandas` est un projet qui évolue régulièrement, on vous recommande donc d'utiliser au moins `pandas` dans sa version 0.21. Voici les versions que l'on utilise ici.

```{code-cell} ipython3
import numpy as np
print(f"numpy version {np.__version__}")

import pandas as pd
print(f"pandas version {pd.__version__}")
```

Il est important de comprendre que le monde de la data science en Python suit un autre paradigme que Python. Là où Python favorise la clarté, la simplicité et l'uniformité, `numpy` and `pandas` favorisent l'efficacité. La conséquence est une augmentation de la complexité et une moins bonne uniformité. Aussi, personne ne joue le rôle de BDFL dans la communauté data science comme le fait Guido van Rossum pour Python. Nous entrons donc largement dans une autre philosophie que celle de Python.

+++

#### Les structures de données en `pandas`

+++

Il y a deux structures de données principales en `pandas`, la classe `Series` et la classe `DataFrame`. Une `Series` est un tableau à une dimension où chaque élément est indexé avec essentiellement un autre array (souvent de chaînes de caractères), et une `DataFrame` est un tableau à deux dimensions où les lignes et les colonnes sont indexées. La clef ici est de comprendre que l'intérêt de `pandas` est de pouvoir manipuler les tableaux `numpy` qui sont indexés, et le travail de `pandas` est de rendre les opérations sur ces index très efficaces.

+++

Vous pouvez bien sûr vous demander à quoi cela sert, alors regardons un petit exemple. Nous allons revenir sur les notions utilisées dans cet exemple, notre but ici est de vous montrer l'utilité de `pandas` sur un exemple.

```{code-cell} ipython3
# seaborn est un module pour dessiner des courbes qui améliore
# sensiblement matplotlib, mais ça n'est pas ce qui nous intéresse ici.
# seaborn vient avec quelques jeux de données sur lesquels on peut jouer.
import seaborn as sns

# chargeons un jeu de données qui représente des pourboires
tips = sns.load_dataset('tips')
```

`load_dataset` retourne une `DataFrame`.

```{code-cell} ipython3
type(tips)
```

Regardons maintenant à quoi ressemble une `DataFrame` :

```{code-cell} ipython3
# voici à quoi ressemblent ces données. On a la note totale (total_bill),
# le pourboire (tip), le sexe de la personne qui a donné le pourboire,
# si la personne est fumeur ou non fumeur (smoker), le jour du repas,
# le moment du repas (time) et le nombre de personnes à table (size)
tips.head()
```

On voit donc un exemple de `DataFrame` qui représente des données indexées, à la fois par des labels sur les colonnes, et par un rang entier sur les lignes. C'est l'utilisation de ces index qui va nous permettre de faire des requêtes expressives sur ces données.

```{code-cell} ipython3
# commençons par une rapide description statistique de ces données
tips.describe()
```

```{code-cell} ipython3
# prenons la moyenne par sexe
tips.groupby('sex').mean()
```

```{code-cell} ipython3
# et maintenant la moyenne par jour
tips.groupby('day').mean()
```

```{code-cell} ipython3
# et pour finir la moyenne par moment du repas
tips.groupby('time').mean()
```

Vous voyez qu'en quelques requêtes simples et intuitives (nous reviendrons bien sûr sur ces notions) on peut grâce à la notion d'index, obtenir des informations précieuses sur nos données. Vous voyez qu'en l'occurrence, travailler directement sur le tableau `numpy` aurait été beaucoup moins aisé.

+++

### Conclusion

+++

Nous avons vu que la data science est une discipline complexe qui demande de nombreuses compétences. Une de ces compétences est la maîtrise d'un langage de programmation, et à cet égard la suite data science de Python qui se base sur `numpy` et `pandas` offre une solution très performante.

+++

Il nous reste une dernière question à aborder : R ou la suite data science de Python ?

Notre préférence va bien évidemment à la suite data science de Python parce qu'elle bénéficie de toute la puissance de Python. R est un langage dédié à la statistique qui n'offre pas la puissance d'un langage générique comme Python. Mais dans le contexte de la data science, R et la suite data science de Python sont deux excellentes solutions. À très grosse maille, la syntaxe de R est plus complexe que celle de Python, par contre, R est très utilisé par les statisticiens, il peut donc avoir une implémentation d'un nouvel algorithme de l'état de l'art plus rapidement que la suite data science de Python.

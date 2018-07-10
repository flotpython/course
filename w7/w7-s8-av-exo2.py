# pour cet exemple, je vais prendre un jeux de données qui est publiquement
# disponible dans le projet seaborn. seaborn est une librairie graphique spécilisée
# pour certaines représentations statisques. Je ne vais pas utiliser ici seaborn
# pour faire de la représentation, mais uniquement pour accéder à ce jeux de données.

import pandas as pd
import numpy as np

import seaborn as sns
ti = sns.load_dataset('titanic').loc[:,['survived', 'sex', 'class']]

# regardons cette DataFrame

ti.head()
ti.shape

# pour cette expression-ci, je présume que tu vas décortiquer un peu
# le fait que par exemple ti.loc[:, 'survived']
# est un objet 'Series' qui représente la colonne 'survived'
ti.loc[:, 'survived']

ti.loc[:, 'survived'].mean()

# Regardons maintenant le taux de survie pour la première classe

ti.loc[ti.loc[:, 'class'] == 'First', 'survived'].mean()

# je peux évidemment faire le même calcul pour chacune
# des deux autres classes, mais il serait beaucoup plus commode de pouvoir
# regrouper automatiquement tous les passegers de la même classe.

# c'est exacetement ce que permet groupby.
ti.groupby('class').mean()

[[pour moi il y a un coté magique ici; comment en partant de trois colonnes
survived, sex et class, et en groupant pas class, on arrive à une moyenne sur
survived; où est-ce qu'on dit qu'on se débarrasse de sex ??; j'imagine que c'est
peut-être parce que 'sex' n'est pas numérique ?? ça mérite sans doute d'être
explicité...]]

# et je pourrai même faire un regroupement par class et sex de la manière
# suivante
ti.groupby(['class', 'sex']).mean()

# en résumé, groupby permet de regrouper des lignes en fonction en
# certaines colonnes et ensuite permet d'appliquer une fonction, à chaque
# groupe.

# Cependant, on voit dans l'exemple précédent, que si l'on fait un
# regroupement sur plusieurs colonnes, on obtient un multiindex.

[[1. c'est pas hyper clair pour moi qu'on a un multi-index !]]

[[2. plus généralement sur groupby:
  j'ai essayé de regarder le résultat de
  ti.groupby['class']
  sans lui appliquer mean()
  ça renvoie un objet pandas.core.groupby.groupby.DataFrameGroupBy
  qu'on ne peut pas afficher

  du coup je ne suis pas très sûr de ce qu'on peut faire au juste sur cet objet
  à part mean(); est-ce que tu en parles ? dit autrement, ce serait bien d'aider
  l'apprenant à voir (comment on utilise / ce qu'on peut faire sur) un object
  groupby en plus de mean()

 PS. après avoir lu le complément, je vois qu'on y aborde des trucs comme
 g.groups et g.get_group('First')
 ce serait bien que dans la vidéo tu renvoies au complément en disant quelque chose comme:

"on creusera dans le complément les différentes opérations qu'on peut faire directement sur un object 'groupby' "
 ]]


# C'est tout à fait correct, mais pas le plus agréable à manipuler.
# Il serait beaucoup mieux dans cet exemple d'avoir une DataFrame
# qui contiennent comme index les classe, comme column le sex
# et comme valeur le nombre moyen de survivant.

# C'est exactement ce que permet pivot_table qui
# peut-être vue comme une généralisation de groupby sur 2 dimensions.
# revenons à notre exemple du titanic

ti.pivot_table('survived', index='class', columns='sex', aggfunc=np.mean)

[[le complément fournit déjà un exemple de ça; je remarque qu'il ne creuse pas vraiment beaucoup par rapport à ceci, mais bon ça n'est sans doute pas très grave:) ]]

#5m30

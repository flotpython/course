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

# Nous avons déjà vu que je peux accéder à la colonne survived 
# de la manière suivante 
ti.loc[:, 'survived']

# et calculer une moyenne sur cette colonne avec
ti.loc[:, 'survived'].mean()

# Regardons maintenant le taux de survie pour la première classe

ti.loc[ti.loc[:, 'class'] == 'First', 'survived'].mean()

# je peux évidemment faire le même calcul pour chacune
# des deux autres classes, mais il serait beaucoup plus commode de pouvoir
# regrouper automatiquement tous les passegers de la même classe.

# c'est exactement ce que permet groupby.
ti.groupby('class').mean()

# vous noterez que la colonne sex a disparue. groupby a un concept
# qui s'appelle *nuisance colonne*. Si une opération ne peux pas être appliquée
# à une colonne (et calculer une moyenne sur la colonne sex n'aurait pas de sens), 
# cette colonne est automatiquement écartée du résultat

# Il est important de comprendre que groupby me retourne un nouvel objet

ti.groupby('class')

# qui permet d'accéder aux différents groupes et d'appliquer une opération d'aggregation, 
# de filtrage ou de transformation à chaque groupe. On creusera dans le complément les
# différentes opérations qu'on peut  faire directement sur un object groupby

# je pourrais maintenant faire un regroupement par class et sex de la manière
# suivante
tig = ti.groupby(['class', 'sex']).mean()
tig

# Cependant, on voit dans l'exemple précédent, que si l'on fait un
# regroupement sur plusieurs colonnes, on obtient un multiindex.
tig.index

# C'est tout à fait correct, mais pas le plus agréable à manipuler.
# Il serait beaucoup mieux dans cet exemple d'avoir une DataFrame
# qui contiennent comme index les classe, comme column le sex
# et comme valeur le nombre moyen de survivant.

# C'est exactement ce que permet pivot_table qui
# peut-être vue comme une généralisation de groupby sur 2 dimensions.
# revenons à notre exemple du titanic

ti.pivot_table('survived', index='class', columns='sex', aggfunc=np.mean)

#7m30

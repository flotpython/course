# pour cet exemple, je vais prendre un jeux de données qui est publiquement 
# disponible dans le projet seaborn. seaborn est une librairie graphique spécilisée
# pour certaines représentations statisques. Je ne vais pas utiliser ici seaborn
# pour faire de la représentation, mais uniquement pour accéder à ce jeux de données. 

import seaborn as sns
import pandas as pd
import numpy as np
ti = sns.load_dataset('titanic').loc[:,['survived', 'sex', 'class']]

# regardons cette DataFrame

ti.head()
ti.shape
ti.loc[:,'survived'].mean()

# Regardons maintenant le taux de survie pour la première classe

ti.loc[ti.loc[:, 'class']=='First','survived'].mean()

# je peux évidemment faire le même calcul pour chacune 
# des deux autres classes, mais il serait beaucoup plus commode de pouvoir
# regrouper automatiquement tous les passegers de la même classe. 

# c'est exacetement ce que permet groupby.
ti.groupby('class').mean()

# et je pourrai même faire un regroupement par class et sex de la manière
# suivante
ti.groupby(['class', 'sex']).mean()

# en résumé, groupby permet de regrouper des lignes en fonction en 
# certaines colonnes et ensuite permet d'appliquer une fonction, à chaque
# groupe. 

# Cependant, on voit dans l'exemple précédent, que si l'on fait un 
# regroupement sur plusieurs colonnes, on obtient un multiindex. 
# C'est tout à fait correct, mais pas le plus agréable à manipuler. 
# Il serait beaucoup mieux dans cet exemple d'avoir une DataFrame
# qui contiennent comme index les classe, comme column le sex
# et comme valeur le nombre moyen de survivant. 

# C'est exactement ce que permet pivot_table qui 
# peut-être vue comme une généralisation de groupby sur 2 dimensions. 
# revenons à notre exemple du titanic

ti.pivot_table('survived', index='class', columns='sex', aggfunc=np.mean)

#5m30
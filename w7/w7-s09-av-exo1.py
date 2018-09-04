# numpy a  types pour gérer le dates datetime64 et un type pour
# gérer les intervals de temps timedelta64.

# ces deux objets sont codés sur 64 bits avec un codage très malin. On spécifie
# notre résolution maximum et l'objet va automatiquement trouver le plus grande
# nombre de date possibles à coder sur 64 bits avec la résolution souhaitée.

# Par exemple avec une résolution de la ns, on peut coder toutes les dates
# de 1678 à 2262. C'est cette résolution qui est la plus courrente. Si on a besoin
# d'intervals beaucoup plus larges, on peut prendre la résolution de la ms qui permet
# de couvrir 600 millions d'années.

# Pour créer un objet datetime64, il faut lui fournir une date dans le format
# ISO8601. Regardons un exemple
import numpy as np
import pandas as pd
np.datetime64('2018-06-30')

 # on peut également spécifier une heure
np.datetime64('2018-06-30 08:35:23')

# et on peut fixer la granularité ainsi
np.datetime64('2018-06-30 08:35:23', 'ns')

# un timedelta64 est obtenu, par exemple, lorsque l'on fait la différence
# de deux datetime64
np.datetime64('2018-06-30 08:35:23') - np.datetime64('2017-06-30 18:33:20')

#3m00

# Pandas propose trois nouveaux types qui se basent sur datetime64 et timedelta64.
# Ces types sont Timestamp pour représenter une date, Period pour représenter une date
# et une durée associée (par exemple, une semaine à partir du 1er juillet 2018), et
# Timedelta pour représenter un interval de temps.

# Ces nouveaux types ont deux avantage majeurs par rapport aux types
# numpy: ils supportent un parsing de dates beaucoup plus flexible et
# ils peuvent être dans des index

# Dans la suite, nous ne parlerons que du type Timestamp et de sont index
# associé DatetimeIndex. Notez le choix des noms un peu malheureux, on aurait
# préféré avec un TimestampIndex

# Il y a en pandas une fonction magique to_datetime qui prend soit une date dans un format
# quelconque et produit un objet Timestamp, soit une séquence de dates et produit
# un index DatetimeIndex. Regardons cela

pd.to_datetime('10 june 1973 8h30')

pd.to_datetime(['10 june 1973', '22-June-1973']) # avec des formats hétérogènes

#5m00

# on peut également utiliser date_range pour créer un index, par exemple
index = pd.date_range('1 jan 2018', periods=1000, freq='D')
# pour créer mile dates à partir du 1 janvier 2018 avec une fréquence
# d'un jour. Notons que les fréquences peuvent etre quelconque, regardons
# cet exemple. On utilise t pour les minutes, parce que m est déjà utilisé pour les mois
index = pd.date_range('2018-01-01', periods=1000, freq='43h36t') # t or min

# regardons maintenant un exemple de Series avec un index DatetimeIndex
s = pd.Series(np.random.randint(100, size=1000), index=index)

# les Séries permette une indéxation intélligente
s.loc['2018'] # me retourne toutes les entrées en 2018
s.loc['dec 2018'] # me retourne toutes les entrées en décembre 2018

# et je peux évidemment faire du slicing en utilisant le même principe
s.loc['2018-12': '2019-01-25']

#8m20

# et pour finir, essayons la méthode resample qui permet de rééchantillonner une
# Series avec un DatetimeIndex. Cette méthode est similaire à groupby dans l'esprit,
# le resample retourne un resampler object qui permet d'accéder aux groupes
# rééchantillonés et d'appliquer une opération à ces groupes. Regardons cela

s.resample('M').mean()

# resample est une méthode très puissante, par exemple, je peux rééchantilloné 
# avec une fréquence de la semaine qui démarre le mercredi et calculer la somme
# de chaque groupe.

s.resample('W-WED').sum()

# la méthode resample vient avec beaucoup d'exemples que je vous
# recommande de consulter

s.resample?

#9m40

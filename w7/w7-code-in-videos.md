
# w7s1. Présentation générale
-------------

> Ouvrir un notebook (par ex. dans la page de complément ci-après)

> ou bien aller sur l'url https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb

> attendre d'avoir la page jupyter et faire File -> New Notebook -> Python 3



	# Vidéo
	import numpy as np
	import pandas as pd
	import seaborn as sns

> Exécuter la cellule par Shift-Entrée

> Insérer une cellule après avec b (une fois la cellule bleue avec esc)
> ou bien avant avec a 

	L = list(range(1000))

	a = np.array(L)

	%timeit [x**2 for x in L]

	%timeit [x**2 for x in a]

	%timeit a**2

	tit = sns.load_dataset('titanic')

	tit.head()

	t = tit.pivot_table('survived',
                        aggfunc = np.mean,
                        index = 'class',
                        columns = 'sex')

	 t.plot(kind='bar')


# w7s2. Numpy : le type ndarray
-------------

> Ouvrir un notebook
> ou bien un interpréteur python si vous avez installé numpy

	import numpy as np

> Exécuter la cellule par Shift-Entrée puis a pour insérer une cellule avant

	np.ones(shape=3)

	np.ones(shape=(2, 2))

	np.ones(shape=(2, 2, 3))

	a = np.ones((2, 2))
	a

	np.sctypes

	a = np.array([1, 100, 110], dtype=np.int8)

	a

	a.dtype

	a.itemsize

	a.nbytes

	np.array([1, 45, 128], dtype=np.int8)

	np.array([1, 45, 129], dtype=np.int8)

	a = np.array([1, 2, np.nan])
	a.dtype

	a = np.array([1, 2, np.nan], dtype= np.int32)

	np.sctypes['others']

	a = np.array(['spam', 'bean'], dtype=np.str)
	a

	a = np.array(['spam', 'beans'], dtype=np.str)
	a

	a = np.array(['spam', 'beans'], dtype=(np.str, 2))
	a

	np.sctypes['others']


# w7s3. Numpy : slicing, reshaping et indexation avancée
-------------

> Ouvrir un notebook

	import numpy as np

	a = np.random.randint(1, 10, size=(3, 3))
	a

	a[1:, 2:]

	b = a[1:, :2]
	b

	a[1, 1] = 35
	a

	b

	a = np.random.randint(1, 10, size=(4, 4))
	a

	b = a.reshape(8, 2)
	b

	mars = np.random.randint(-5, 20, size=31)
	mars

	mars > 0

	mars == 0

	np.sum(mars > 0)

	np.any(mars == 20)

	np.all(mars > 0)

	jours_mars = np.arange(1, mars.size + 1, dtype=np.int8)
	jours_mars

	np.sum((mars > 10) & (jours_mars >= 15))

	mars[mars > 10]

	mars[(mars > 10) & (jours_mars >= 15)]

	moy = np.mean(mars[mars > 0])
	mars[mars < 0] = moy
	mars

	countries = np.array(['fr', 'us', 'jp'])
	countries[[0, 0, 1, 2, 0]]


# w7s4. Numpy : vectorisation
-------------

> Ouvrir un notebook

	import numpy as np

	a = np.arange(1000)

	%timeit [x**2 + 2*x - 1 for x in a]

	%timeit a**2 + 2*a - 1

	a = np.arange(1, 1_000_000, dtype=np.float64)
	%timeit -r 1 -n 1 np.sqrt(a)

	%timeit -r 1 -n 1 np.sqrt(a, out=a)

	a

	a[:5]

	a = np.arange(1, 10).reshape(3, 3)
	a

	np.sum(a)

	np.sum(a, axis=0)

	np.sum(a, axis=1)

	a = np.arange(1, 10, dtype=np.float64).reshape(3, 3)
	a

	a[1, 1] = np.nan
	a

	np.mean(a)

	np.nanmean(a)

	np.nanmax(a)


# w7s5. Numpy : broadcasting
-------------

> Ouvrir un notebook

	import numpy as np

	a = np.array([1, 2, 3])
	b = np.array([5, 5, 5])
	a * b

	c = np.array([5])
	a * c

	a * 5

	a = np.array([1, 2, 3]).reshape(1, 3)
	b = np.ones((3, 3))

	a.shape

	b.shape

	a * b

	a = np.array([1, 2, 3]).reshape(3, 1)
	b = np.ones((3, 3))

	a.shape

	b.shape

	a = np.array([1, 2, 3]).reshape(3, 1)
	b = np.array([4, 5]).reshape(1, 2)

	a.shape

	b.shape

	a * b


# w7s6. Pandas : introduction aux series et aux index
-------------

> Ouvrir un notebook
> ou bien un interpréteur python si vous avez installé pandas

	import pandas as pd

	s = pd.Series([20, 30, 40, 50], index=['eve', 'bill', 'liz', 'bob'])
	s

	s.values

	s.index

	s.loc['eve']

	s['eve']

	s.loc['eve':'liz']

	s = pd.Series([20, 30, 40, 50], index=['eve', 'liz', 'bill', 'bob'])
	s.loc['eve':'liz']

	animaux = ['chien', 'chat', 'chat', 'chien', 'poissson']
	proprio = ['eve',   'bob',  'eve',  'bill',  'liz']

	s = pd.Series(animaux, index=proprio)
	s

	s = s.sort_index()
	s.loc['eve':'liz']

	s

	s.iloc[0]

	s.iloc[4]

	s.iloc[1:3]

	s.loc[s =='chien']

	s.loc[(s =='chien') | (s == 'poisson')]

	s.loc[(s =='chien') | (s == 'poisson')] = 'autre'
	s

	s1 = pd.Series([1, 2, 3], index=list('abc'))
	s2 = pd.Series([5, 6, 7], index=list('acd'))
	s1

	s2

	s1 + s2

	s1.add(s2, fill_value=50)


# w7s7. Pandas : le type DataFrame
-------------

> Ouvrir un notebook

	import numpy as np
	import pandas as pd

	prenoms = ['liz', 'bob', 'bill', 'eve']
	age = pd.Series([25, 30, 35, 40], index = prenoms)
	taille = pd.Series([160, 175, 170, 180], index = prenoms)
	sexe = pd.Series(list('fhhf'), index = prenoms)

	df = pd.DataFrame({'age': age, 'taille': taille, 'sexe': sexe})

	df

	df.index

	df.columns

	df.values

	df.head(2)

	df.tail(2)

	df.describe()

	df.loc['liz']

	df.loc['liz', 'age']

	df.loc[:,'taille']

	df.loc[df.loc[:,'age']<32 ]

	df

	df = df.reset_index()
	df

	df = df.rename(columns={'index': 'prenom'})
	df

	df = df.set_index('age')
	df

	# Réinitialisation de df
	df = pd.DataFrame({'age': age, 'taille': taille, 'sexe': sexe})
	df

	df = (df.reset_index()
	        .rename(columns={'index': 'nom'})
	        .set_index('age'))
	df

	df1 = pd.DataFrame(np.ones((2, 2)), index=list('ab'), columns=list('xy'))
	df1

	df2 = pd.DataFrame(np.ones((2, 2)), index=list('ac'), columns=list('xz'))
	df2

	df1 + df2

	df1.add(df2, fill_value=0)

	df = df1.add(df2, fill_value=0)
	df

	df.fillna(-1)

	df.dropna()


# w7s8. Pandas : opérations avancées
-------------

> Ouvrir un notebook

	import numpy as np
	import pandas as pd

	df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
	                   columns=list('ab'), index=list('xy'))
	df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
	                   columns=list('ab'), index=list('zt'))
	 
	df1

	df2

	pd.concat([df1, df2])

	df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
	                   columns=list('ab'), index=list('xy'))
	df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
	                   columns=list('cd'), index=list('xy'))

	df1

	df2

	pd.concat([df1, df2], axis=1)

	df1 = pd.DataFrame({'personnel': ['Bob', 'Lisa', 'Sue'],
	                   'groupe': ['SAF', 'R&D', 'RH']})
	df2 = pd.DataFrame({'personnel': ['Lisa', 'Bob', 'Sue'],
	                    'date embauche': [2004, 2008, 2014]})

	print(df1)
	print(df2)

	pd.merge(df1, df2)

	import seaborn as sns

	ti = sns.load_dataset('titanic').loc[:,['survived', 'sex', 'class']]

	ti.head()

	ti.shape

	ti.loc[:, 'survived'].mean()

	ti.loc[ti.loc[:, 'class']=='First', 'survived'].mean()

	ti.loc[ti.loc[:, 'class']=='Second', 'survived'].mean()

	ti.groupby('class')

	ti.groupby('class').mean()

	g = ti.groupby(['class', 'sex']).mean()

	g

	g.index

	ti

	ti.pivot_table('survived', aggfunc=np.mean,
	               index='class', columns='sex')
	 


# w7s9. Pandas : gestion des dates et des séries temporelles
-------------

> Ouvrir un notebook

	import numpy as np
	import pandas as pd

	np.datetime64('2018-06-30')

	np.datetime64('2018-06-30 08:35:23')

	np.datetime64('2018-06-30 08:35:23', 'ns')

	np.datetime64('2018-06-30 08:35:23') - np.datetime64('2018-06-20 08:37:23')

	pd.to_datetime('10 june 1973 8h30')

	pd.to_datetime(['10 june 1973 8h30', '22-JUNE-1973'])

	index = pd.date_range('1 jan 2018', periods=1000, freq='D')

	index

	index = pd.date_range('1 jan 2018', periods=1000, freq='43h36min')

	index = pd.date_range('1 jan 2018', periods=1000, freq='43h36t')

	index

	s = pd.Series(np.random.randint(100, size=1000), index=index)

	s

	s['2018']

	s['dec2018']

	s['dec 2018':'3 jan 2019']

	s.resample('M').mean()

	s.resample('W-WED').mean()

	s.resample?
		 		 

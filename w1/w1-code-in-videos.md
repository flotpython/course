
# w1s3. Interpréteur et IDLE
-------------

	20 * 30
	a = 10
	print(a)
	def polynome(x):
		return 2*x**2 + 4*x + 10
	polynome(10)
	polynom(10)
	import math
	dir(math)
	help(math.ceil)

> Faire : *File → New file* ou Control-N

	# un commentaire
	def factoriel(n):
	    """ le factoriel """
	    if n <= 1:
	        return 1
	    else:
	        return n * factoriel(n-1)
> Faire : *File → save as* `factoriel.py`

	polynome(10)
	factoriel(10)

> dans le programme factoriel.py, rajouter :

	print(factoriel(100))
> dans un terminal (cmd pour windows) :

	python -V
	python factoriel.py
	ipython
	?

	def fibonacci(n):
	     return 1 if n <=1 else fibonacci(n-1) + fibonacci(n-2)
	fibonacci(10)
	import math
	math.ceil?
	math.ceil(10)

# w1s6. Les types numériques
-------------

	1
	i = 1
	type(i)
	1 + 3
	1 * 5
	i = i + 5
	print(i)
	i = 393213216546546546546546546546565654654654231546654645654654
	i * i
	i ** 5
	f = 4.3
	c = 4 + 5j
	c
	i + f
	i + f + c
	int(4.3)
	float(4)
	complex(4.0)
	1 + 4
	1 - 4
	3 * 5
	3 / 6
	3 // 6
	3 % 6
	abs(-4)
	True
	False
	1 < 2
	1 > 5



# w9s1. Méthodes statiques et de classe
-------------

> Prendre l’éditeur IDLE et faire nouveau fichier
 
	class Phrase:
	    nb_i = 0
	    def __init__(self):
	        Phrase.nb_i += 1

> Faire Save As "w9s1 Vidéo.py" puis F5

	Phrase()

	Phrase()

	Phrase.nb_i

> Reprendre sous IDLE le fichier python et ajouter

	    def num():
	        return Phrase.nb_i

> Faire Ctl-s puis F5

	Phrase()

	Phrase()

	Phrase.num()

	Phrase.num

	p = Phrase()
	p.num()

	p.num

> Reprendre sous IDLE le fichier python et ajouter

	    @staticmethod

> Faire Ctl-s puis F5

	p = Phrase()
	Phrase.num()

	p.num()

> Reprendre sous IDLE le fichier python et ajouter

	class PhraseSansCasse(Phrase):
	    pass

> Faire Ctl-s puis F5

	p = Phrase()
	Phrase.num()

	PhraseSansCasse.num()

> Reprendre sous IDLE le fichier python et ajouter à la classe PhraseSansCasse

	    @staticmethod
	    def num():
	        return f"PhraseSansCasse {Phrase.nb_i}"

> Faire Ctl-s puis F5

	p = Phrase()
	Phrase.num()

	PhraseSansCasse.num()


> Reprendre sous IDLE le fichier python et ajouter à la classe PhraseSansCasse

	    nb_i = 0
	    def __init__(self):
	        PhraseSansCasse.nb_i += 1

> Dans la classe Phrase, remplacer par:

	    @classmethod
	    def num(cls):
	        return cls.nb_i

> Et dans la classe PhraseSansCasse:

	    @classmethod
	    def num(cls):
	        return f"PhraseSansCasse {Phrase.nb_i}"

> Faire Ctl-s puis F5

	p = Phrase()
	Phrase()

	p_no = PhraseSansCasse()
	p.num()

	Phrase.num()

	Phrase.num

	p.num

	p_no.num()

	PhraseSansCasse.num()

# w9s2. Les décorateurs
-------------

> Prendre l’éditeur IDLE et faire nouveau fichier
 
	class NbAppels:
	    def __init__(self, f):
	        self.appels = 0
	        self.f = f
	    def __call__(self, *t, **d):
	        self.appels += 1
	        s = f"{self.f.__name__} : {self.appels}"
	        print(s)
	        return self.f(*t, **d)

	@NbAppels
	def f(a, b):
	    print(a, b)

> Faire Save As "w9s2 Vidéo.py" puis F5

	f(1, 2)

	f(3, 'a')

	@NbAppels
	def g(a, b, c):
	    print(a, b, c)
	    
	g(1, 2, 3)


# w9s3. Les clôtures de fonctions
-------------

> Prendre l’éditeur IDLE et faire nouveau fichier

	def plus_n(y):
	    def incremente(x):
	        return x + y
	    return incremente

> Faire Save As "w9s3 Vidéo.py" puis F5

	plus3 = plus_n(3)
	plus3(10)

	plus3.__closure__

	plus3.__closure__[0].cell_contents


> Reprendre l’éditeur IDLE et prendre un nouveau fichier (ou pas)

	import time
	def timer(f):
	    def wrapper(*args, **dargs):
	        start = time.time()
	        res = f(*args, **dargs)
	        print('{:.2} s'.format(time.time() - start))
	        return res
	    return wrapper

	@timer
	def sum_poly5(n):
	    return sum(x**5 for x in range(n))

> Faire Ctl-s puis F5

	sum_poly5(1_000_000)


> Reprendre l’éditeur IDLE et prendre un nouveau fichier (ou pas)

	def trace_call(f):
	    called = 0
	    def wrapper(*args, **dargs):
	        nonlocal called
	        called += 1
	        print(f'{called} appels de {f.__name__}')
	        return f(*args, **dargs)
	    return wrapper

	@trace_call
	def my_func():
	    pass

> Faire Ctl-s puis F5

	my_func()
	my_func()


> Reprendre l’éditeur IDLE et prendre un nouveau fichier (ou pas)

	def trace_call(f):
	    def wrapper(*args, **dargs):
	        wrapper.called += 1
	        print(f'{wrapper.called} appels de {f.__name__}')
	        return f(*args, **dargs)
	    wrapper.called = 0
	    return wrapper

	@trace_call
	def my_func():
	    pass

> Faire Ctl-s puis F5

	my_func()
	my_func()

> Reprendre la fonction my_func et ajouter

	    'documentation pour my_func'

> Faire Ctl-s puis F5

	help(my_func)
  
> Reprendre le fichier et ajouter

    from functools import wraps

> Ajouter à la foncton trace_call

	    @wraps(f)

> Faire Ctl-s puis F5

	help(my_func)
  
# w9s4. Les métaclasses
-------------

> Prendre une console python

	class C:
	    pass

	t = C.__bases__
	t

	t[0].__bases__

	object.__bases__

	int.__bases__

	dict.__bases__

	str.__bases__

	i = C()
	type(i)

	type(C)

	type(1)

	type(int)

	class C:
	    pass

	class D(C):
	    pass

	type(object)

	type(C)

	type(D)


> Prendre l’éditeur IDLE

	class LowerAttrMetaclass(type):
	    def __new__(cls, clsname, bases, dct):
	        lowercase_attr = {}
	        for name, val in dct.items():
	            if not name.startswith('__'):
	                lowercase_attr[name.lower()] = val
	            lowercase_attr[name] = val
	        bases = (BaseOfAll,)
	        return type.__new__(cls, clsname, bases, lowercase_attr)

	class BaseOfAll:
	    def common_func(self):
	        return "in commun_func"
	    
	class C(metaclass=LowerAttrMetaclass):
	    def funC_bAd_CAP(self):
	        return "in func_bad_cap"

> Faire Ctl-s puis F5

	c = C()
	c.func_bad_cap()

	c.common_func()


# w9s5. Property et descripteurs
-------------

> Prendre l’éditeur IDLE 

	class Maison:
	    def __init__(self, t):
	        self._temperature = t
	        
	    def get_temperature(self):
	        return self._temperature
	    
	    def set_temperature(self, t):
	        if 5 < t and t < 25:
	            self._temperature = t
	            return
	        raise TemperatureError()
	        
	class TemperatureError(Exception):
	    pass

> Faire Ctl-s puis F5

	m = Maison(18)
	print(m.get_temperature())

	m.set_temperature(22)
	print(m.get_temperature())

	m.set_temperature(28)

> Reprendre l’éditeur IDLE et ajouter à la classe Maison:

	    temperature = property(get_temperature, set_temperature)

> Faire Ctl-s puis F5

	m = Maison(18)
	m.temperature

	m.temperature = 22
	m.temperature

	m.temperature = 28

> Reprendre l’éditeur IDLE

	class Temperature:
	    def __get__(self, inst, insttype):
	        return inst._temperature
	    
	    def __set__(self, inst, t):
	        if 5 < t and t < 25:
	            inst_temperature = t
	            return
	        raise TemperatureError()
	        
	class TemperatureError(Exception):
	    pass

	class Maison:
	    def __init__(self, t):
	        self.temperature = t

	    temperature = Temperature()
	    

> Faire Ctl-s puis F5

	m = Maison(18)
	m.temperature

	m.temperature = 22
	m.temperature

	m.temperature = 28


# w9s6.  Protocole d'accès aux attributs
-------------

> Prendre l’éditeur IDLE 

	class Temperature:
	    def __get__(self, inst, insttype):
	    	print("desc __get__")
	        return inst._temperature
	    
	    def __set__(self, inst, t):
	    	print("desc __set__ {t}")
	        inst_temperature = t
	        
	class Maison:
	    def __init__(self, t):
	        self.temperature = t

		def __getattribute__(self, a):
		    print("__getattribute__ : {a}")
		    return object.__getattribute__(self, a)

		def __setattr__(self, a, v):
		    print("__setatt__ : {a} - {v}")
		    return object.__setattr__(self, a, v)

		temperature = Temperature()

> Faire Ctl-s puis F5

	m = Maison(18)

	m.temp

> Taper tab pour la complétion

	m.temperature

	m.temperature = 22

	m.x

	m.x = 10

	m.x

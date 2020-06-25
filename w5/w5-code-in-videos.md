 
# w5s1. Itérable, itérateur, itération 
-------------

    s = {1, 2, 3, 'a'} 
    for i in s: 
        print(i) 
    [x for x in s if type(x) is int] 
    s 
    it = iter(s) 
    it 
    next(it) 
    next(it) 
    next(it) 
    next(it) 
    next(it) 
     
    a = [1, 2] 
    b = [3, 4] 
    iter(a) 
    z = zip(a, b) 
    z 
    z is iter(z) 
    [i for i in z] 
    [i for i in z] 
    next(z) 
    z = zip(a, b) 
    [i for i in z] 
 
# w5s2. Objet fonction, fonction lambda, map et filter 
-------------
 
    lambda x: x**2 - 1 
    carre = lambda x: x**2 - 1
    carre(1)

> Prendre l'éditeur de IDLE (ou pas :))

    def image(f): 
        for x in range(10): 
            print(f"{f(x)}: {x}") 
> Faire Control-s puis F5 

    image 
    image(lambda x: x**2 - 1)

> Reprendre l'éditeur

    def carre(x): 
        return x**2 - 1 
> Faire Control-s puis F5

    image 
    carre 
    image(carre) 
     
    m = map(carre, range(10)) 
    m
    list(m) 
    filter(lambda x: x%2 == 0, range(10)) 
    f = filter(lambda x: x%2 == 0, range(10)) 
    list(f)
 
# w5s3. Compréhension des listes, sets et dictionnaires    
-------------

    prenoms = ['ana', 'eve', 'ALICE', 'Anne', 'bob'] 
    prenoms 
    a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')] 
    a_prenoms 
    prenoms.extend(prenoms) 
    prenoms 
    a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')] 
    a_prenoms 
    set(a_prenoms) 
    prenoms 
    a_prenoms = {p.lower() for p in prenoms if p.lower().startswith('a')} 
    a_prenoms 
    ages = [('ana', 20), ('EVE', 30), ('bob', 40)] 
    ages = dict(ages) 
    ages 
    ages_fix = {p.lower():a for p, a in ages.items()} 
    ages_fix 
    ages_fix = {p.lower():a for p, a in ages.items() if a < 40} 
    ages_fix 
 
# w5s4. Expressions et fonctions génératrices  
-------------

## Vidéo 1

    carre = [x**2 for x in range(1000)]
    sum(carre)
    carre = (x**2 for x in range(1000))
    carre
    sum(carre)
    sum(carre)
    next(carre)
    carre = (x**2 for x in range(1000))
    sum(carre)
    gen_carre = (x**2 for x in range(1_000))
    palin = (x for x in gen_carre if str(x) == str(x)[::-1])
    palin
    list(palin)
     
## Vidéo 2

> Prendre l'éditeur IDLE 

    def gen(): 
        yield 10 
> Faire Control-s puis F5

    gen 
    gen() 
    g = gen() 
    next(g) 
    next(g) 
> Prendre l'éditeur IDLE

    def gen(x): 
        yield x 
        x = x + 1 
        yield x 
> Faire Control-s puis F5

    g = gen(10) 
    g 
    next(g) 
    next(g) 
    next(g) 
> Prendre l'éditeur IDLE

    def carre(a, b): 
        for i in range(a, b): 
            yield i ** 2 
> Faire Control-s puis F5

    c = carre(1, 10) 
    list(c) 
> Prendre l'éditeur IDLE

    def palin(it): 
        for i in it: 
            if (isinstance(i, (str, int)) and 
                str(i) == str(i)[::-1]): 
                yield i 
> Faire Control-s puis F5

    p = palin([121, 10, 12321, 'abc', 'abba']) 
    list(p) 
    list(palin(x**2 for x in range(1000))) 
 
# w5s5. Modules et espaces de nommage   
-------------

> Prendre l'éditeur IDLE

    x = 1 
    def f(): 
        print(x) 
> Faire: *File → save as* `spam.py`

> Faire de nouveau Control-n

    import spam 
    x = 2 
    def f(): 
        print(x) 
     
    f() 
    spam.f() 
    print(spam.x) 
> Faire: *File → save as* `egg.py`

> Ouvrir une invite de commande (cmd) sous windows ou bash sous unix, puis taper :

    python egg.py 
 
# w5s6. Processus d'importation des modules 
-------------

    import os 
    print(os) 
    os.environ['PYTHONPATH'] 
    import sys 
    sys.path 
 
# w5s7. Importation des modules et des espaces de nommage 
-------------

> Prendre l'éditeur IDLE, ouvrir le fichier spam.py

    x = 1 
> Faire Control-s

> Ouvrir le fichier egg.py

    import spam 
    x = 2 
> Faire Control-s puis F5

> Ouvrir une invite de commande (cmd) sous windows ou bash sous unix, puis taper :

    python egg.py 
> Pour voir l'espace de nommage de ces modules, dans la console python, après avoir fait F5 sur un module,  utiliser les instructions

    vars() # ou globals() 
    vars(spam) 
    dir(spam) 
> Ajouter dans egg.py:

    print(x) 
    print(spam.x) 
> Faire Control-s puis F5

> Ajouter dans egg.py:

    spam.x = 3 
> Faire Control-s puis F5

    spam.y = 4 
    print(spam.y) 
> Faire Control-s puis F5

> Reprendre le fichier egg.py:

    from spam import x 
    print(x) 
    x = 3 
    print(x) 
> Faire Control-s puis F5

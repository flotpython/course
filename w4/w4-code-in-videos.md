
# w4s1. Fonction
-------------

    def f(a, b, c):
        print(a, b, c)

    g = f
    f(1, 2, 3)
    g(1, 2, 3)

    def add_1(a):
        a.append(1)

    L = []
    add_1(L)
    L
    help(list.sort)
    add_1(L[:])

    def add_1(a):
        a = a[:]
        a.append(1)
        return a
    L
    add_1(L)
    L
    L = add_1(L)
    L

    def f(a):
        func(a)

    f
    func
    f(1)
    def func(a):
        return a
    func
    f(1)

    def my_add(a, b):
        print(f"{a} et {b}")
        return a + b

    my_add(1, 2)
    my_add(4.3, 2.3)
    my_add('spam', 'good')

# w4s2. Test if/elif/else et opérateurs booléens
-------------

    s = input("Quelle est votre question\n")
    if s.startswith('bonjour'):
        print("bonjour, comment allez-vous?")
    elif "bien" in s:
        print("c'est super !")
    elif "bye" in s:
        print("Au revoir !")
    else:
        print("mais encore...")
> Faire : File -> save as pour sauver le programme  dans jeu.py par ex. puis F5

# w4s3. Vidéo - Boucle while
-------------

> Faire : File -> New file ou ctl-N

    a = list(range(1, 10))
    while a:
        a.pop()
        print(a)
> Faire : File -> save as w4s3.py puis F5

> Dans le programme «w4s3.py», rajouter: 

    if len(a) == 5:
        continue
> Faire Ctl-s puis F5

> Dans le programme «w4s3.py», remplacer continue par: 

        break
> Faire Ctl-s puis F5

> Reprendre «w4s3.py», ou en prendre un nouveau par ctl-n: 

    while True:
        s = input('Quelle est votre question ?\n')
        if 'aucune' in s:
            break
> Faire Ctl-s puis F5

    bonjour
    rien
    aucune

> Reprendre le programme jeu.py

    s = input("Quelle est votre question\n")
    while True:
        if s.startswith('bonjour'):
            print("bonjour, comment allez-vous?")
        elif "bien" in s:
            print("c'est super !")
        elif "bye" in s:
            print("Au revoir !")
            break
        else:
            print("mais encore...")
        s = input()
> Faire Ctl-s puis F5

    bonjour
    bien
    ça va
    bye

# w4s4. Vidéo - Portée des variables - règle LEGB
-------------

    a, b, c = 1, 1, 1
    def g():
         b, c = 2, 4
         b = b + 10
         def h():
             c = 5
             print(a, b, c)
         h()
    g()
    print(a, b, c)
    import builtins
    dir(builtins)
    print(1)
    print = 10
    print(1)
    x = 1
    print = builtins.print
    print(1)

# w4s5. Vidéo - Modification de la portée avec global et nonlocal
-------------

> Faire: File -> New file ou ctl-N

    a = 'a globale'
    def f():
        a = 'a dans f'
        print(a)
> Faire: File -> save as w4s5.py  puis F5

    print(a)
    f()
    print(a)

> Rajouter la ligne (sous def f()

    global a
> Ctl-s puis F5

    print(a)
    f()
    print(a)

    a = 10

    def f():
        global a
        a = a + 10
> Ctl-s puis F5

    print(a)
    f()
    print(a)

> Modifier la fonction

    note = 10

    def add_10(n):
        return n + 10
> Ctl-s puis F5

    note = add_10(note)
    note

> Modifier la fonction

    a = 'a globale'

    def f():
        a = 'a de f'
        def g():
            a = 'a de g'
            print(a)
        g()
        print(a)

    f()
    print(a)
> Ctl-s puis F5

> Rajouter dans g() la ligne:

        nonlocal a
> Ctl-s puis F5

# w4s6. Vidéo - Passage des arguments et appel de fonctions
-------------

> Faire: File -> New file ou ctl-N

    def agenda(nom, prenom, tel):
        return {'nom': nom, 'prenom': prenom,
                'tel': tel}
> Faire: File -> save as w4s6.py puis F5

    agenda('idle', 'eric', '07070707')
    agenda(tel='070707707', nom='idle', prenom='eric')
> Faire: File -> save as w4s6.py puis F5

> Dans la fonction rajouter après tel

    ='?'
> Ctl-s puis F5

    agenda('idle', 'eric')
    agenda('idle', 'eric', '07070707')

> Reprendre le programme ou bien prendre un nouveau

    def f(*t):
        print(t)
> Faire Ctl-s puis F5

    f()
    f(1)
    f(1, 2, 3, 4)

    def f(**d):
        print(d)
> Faire Ctl-s puis F5

    f()
    f(nom='idle', prenom='eric')
    print(1)
    print(1, 2, 3, 4)

> Reprendre le programme ou bien prendre un nouveau

    def f(a, b):
        print(a, b)
> Faire Ctl-s puis F5

    L = [1, 2]
    f(L[0], L[1])
    f(*L)
    d ={'a': 1, 'b': 2}
    f(**d)
    print(1, 2, sep=';', end='FIN')
    pp = {'sep':';', 'end':'FIN'}
    print(1, 2, **pp)

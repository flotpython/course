
# w2s2. Les chaînes de caractères
-------------

## Vidéo 1

    'spam'
    "spam"
    s = 'spam'
    str?
    dir(str)
    'un mooc sur python'.title()
    s = "le poulet c'est bon"
    s.replace('poulet', 'spam')
    s
    '123'.isdecimal()
    n = 'sonia'
    age = 30
    "{} {}".format(n, age)
    "{} a {} ans".format(n, age)
    f"{n} a {age} ans"

## Vidéo 2

    "noël, été"
    "\u03a6"
    "\u0556"
    s = "un noël en été"
    print(s)
    s.encode('utf8')
    en = s.encode('utf8')
    en
    en.decode('utf8')
    s.encode('latin1')

# w2s3. Les séquences
-------------

    s = 'egg, bacon'
    s[0]
    s[9]
    len(s)
    'egg' in s
    'egg' not in s
    s 
    s + ', and beans'
    s.index('g')
    s.count('g')
    min(s)
    max(s)
    'x'*30 
    s = 'egg, bacon'
    s[0:3]
    s[5:10]
    s[:3]
    s[5:]
    s[:]
    s[0:10:2]
    s[::2]
    s[:8:3]
    s[2::3]
    s[100]
    s[5:100]
    s[100:200]
    s[-10:-7]
    s[:-3]
    s[::-1]
    s[2:0:-1]
    s[2::-1]

# w2s4. Les listes
-------------

    a = []
    type(a)
    i = 4
    a = [i, 'spam', 3.2, True]
    a
    a[0]
    a[0] = 6
    a
    a[0] = a[0] + 10
    a
    a[1:3]
    a[1:3] = [1, 2, 3]
    a
    a[1:3] = []
    a
    del a[1:2]
    a
    dir(list)
    list.append?
    help(list.append)
    a
    a.append('18')
    a
    a.extend([1, 2, 3])
    a
    a = [1, 5, 3, 1, 7, 9, 2]
    a.sort()
    a
    a = a.sort()
    a
    s = 'spam egg beans'
    a = s.split()
    a
    a[0] = a[0].upper()
    a
    " ".join(a)

# w2s6. Introduction aux tests if et à la syntaxe
-------------

    print(1**2)
    print(2**2)
    print(3**2)
    for i in range(10):
        print(i**2)
    for i in ['a', 3.5, True]:
        print(i)
    a = [1, 2, 5, 8, 9]
    for i in a:
        print(i**2)
    b = [3.6, 18, 12, 25]
    for i in b:
        print(i**2)
    def carre(a):
        for i in a:
            print(i**2)
    carre(a)
    carre(b)
    def carre(a):
        L = []
        for i in a:
            L.append(i**2)
        return L
    carre(b)
    b = carre(b)
    b

# w2s7. Introduction aux compréhensions des listes
-------------

    a = [1, 4, 18, 29, 13]
    import math
    b = []
    for i in a:
        b.append(math.log(i))
    b
    b = [math.log(i) for i in a]
    b
    a.append(-1)
    a
    b = [math.log(i) for i in a if i > 0]
    b
    prenom = ['Alice', 'evE', 'sonia', 'BOB']
    prenom
    prenom = [p.lower() for p in prenom]
    prenom

# w2s8. Introduction aux modules
-------------

    import random
    print(random)
    dir(random)
    help(random)
    dir(random)
    random.randint? ou help(random.randint)
    random.randint(1, 100)

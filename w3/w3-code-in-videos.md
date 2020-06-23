
# w3s1. Les fichiers
-------------

## Vidéo 1

    f = open(r'C:\temp\spam.txt', 'w', encoding= 'utf8')
    for i in range(100):
        f.write(f"ligne {i+1}\n")
    f.close()
    !type C:\temp\spam.txt
    f = open(r'C:\temp\spam.txt', 'r', encoding= 'utf8')
    f2 = open(r'C:\temp\spam2.txt', 'w', encoding= 'utf8')
    for line in f:
        line = line.split()
        line[0] = line[0].upper()
        f2.write(",".join(line) + "\n")
    f.close()
    f2.close()
    !type C:\temp\spam.txt
    !type C:\temp\spam2.txt

## Vidéo 2

    with open(r'C:\temp\spam.txt', 'r', encoding= 'utf8') as f:
    for line in f:
            print(line)
    with open(r'C:\temp\spam.bin', 'bw') as f:
        for i in range(100):
            f.write(b'\x3d')

# w3s2. Les tuples
-------------

    t = ()
    type(t)
    t = (4,)
    t
    t = (True, 3.4, 18)
    t
    t = True, 3.4, 18
    t
    3.4 in t
    t[1]
    t[:2]
    a = list(t)
    a
    a[0] = False
    t = tuple(a)
    t
    (a, b) = [3, 4]
    a
    b
    a, b = 3, 4
    a
    b
    a = list(range(10))
    a
    x, *y = a
    x
    y
    *x, y = a
    x
    y

# w3s3. Tables de hash
-------------

    %timeit 'x' in range(100)
    %timeit 'x' in range(10_000)
    %timeit 'x' in range(1_000_000)

    t = [1, 2]
    t[0]
    t = [18, 35]
    t['alice']

# w3s4. Les dictionnaires
-------------

    age = {}
    type(age)
    age = {'ana':35, 'eve':30, 'bob':38}
    age['ana']
    a = [('ana', 35), ('eve', 30), ('bob', 38)]
    age = dict(a)
    age['bob']
    age['bob'] = 45
    age
    del age['bob']
    age
    len(age)
    'ana' in age
    'bob' in age
    age.keys()
    age.values()
    age.items()
    k = age.keys()
    k
    age['bob'] = 25
    k
    'ana' in k
    'bill' in k
    for k, v in age.items():
        print(f"{k} {v}")
    for k in age:
        print(k)

# w3s5: Les ensembles
-------------

    s = set()
    type(s)
    s = {1, 2, 3, 'a', True}
    a = [1, 2, 4, 1, 18, 30, 4, 1]
    set(a)
    len(s)
    1 in s
    'b' in s
    s.add('alice')
    s
    s.update([1, 2, 3, 4, 5, 6, 7])
    s
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    s1 - s2
    s1 | s2
    s1 & s2

    a = [0]
    s = set(a)

    %timeit -n 50 0 in a
    %timeit -n 50 0 in s

# w3s6. Les exceptions
-------------

    def div(a, b) :
        print(a/b)
    div(1, 2)
    div(1, 0)

    def div(a, b) :
        try:
            print(a/b)
        except ZeroDivisionError:
            print("attention, division par 0")
    print("Continuons")


    def div(a, b) :
        try:
            print(a/b)
        except ZeroDivisionError:
            print("attention, division par 0")
        except TypeError:
            print("il faut des int")
        print("Continuons")

    def div(a, b) :
        print(a / b)

# w3s7. Les références partagées
-------------

    a = 3
    b = a
    a = 'spam'
    a = [1, 2]
    b = a
    a[0] = 'spam'
    a = [1, 2]
    b = a[:]
    a[0] = 'spam'

    a = [1, [2]]
    b = a[:]
    a[0] = 'spam'
    a[1][0] = 'spam'

    a = [1, [2]]
    import copy
    b = copy.deepcopy(a)
    a[1][0] = 'spam'

# w3s8. Introduction aux classes
-------------

> Faire : *File → New file* ou Control-N

    class C:
        pass
    C()
    c1 = C()
    c2 = C()
    class Phrase:
          def __init__(self, phrase):
          self.mots = phrase.split()
> Faire : *File → save as* `w3s8.py` puis F5

    p = Phrase('je fais un mooc sur python')
    p.mots

    def upper(self):
        self.mots = [m.upper() for m in self.mots]
> Faire Control-s puis F5

    p = Phrase('je fais un mooc sur python')
    p.mots
    p.upper()
    p.mots

    def __str__(self):
        return "\n".join(self.mots)
>Faire Control-s puis F5

    
    p = Phrase('je fais un mooc sur python')
    print(p)

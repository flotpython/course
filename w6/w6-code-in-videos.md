
# w6s1. Classes, instances et méthodes
-------------

> Faire : *File → New file* ou Control-N

    class Phrase:
        ma_phrase = 'je fais un mooc sur python'
> Faire : *File → save as* `Phrase.py` puis F5

    Phrase
    p = Phrase()
    p
    Phrase.__dict__
    vars(Phrase)
    vars(p)
    p.ma_phrase
    Phrase.ma_phrase
    Phrase.mots = Phrase.ma_phrase.split()
    Phrase.mots
    vars(p)
    p.mots
    vars(Phrase)
    vars(p)

> Reprendre `Phrase.py`

    s = 'je fais un mooc sur python'
    class Phrase:
        def initia(self, ma_phrase):
            self.ma_phrase = ma_phrase

> Faire Control-s puis F5

    p = Phrase()
    p.initia(s)
    vars(p)
    Phrase.initia
    p.initia
    p.initia(s)
    Phrase.initia(p, s)

# w6s2. Méthodes spéciales
-------------

> Reprendre `Phrase.py` et ajouter dans la classe `Phrase`:

        def nb_lettres(self):
            return len(self.ma_phrase)

> Faire Control-s puis F5

    p = Phrase()

> Reprendre Phrase.py et remplacer dans la classe Phrase le nom initia par:

    __init__

> Faire Control-s puis F5

    p = Phrase('je fais un mooc sur python')
    p.ma_phrase
    
> Reprendre Phrase.py et dans la méthode `__init__`

            self.mots = ma_phrase.split()

> puis dans la classe Phrase :

        def __len__(self):
            return len(self.mots)

> Faire Control-s puis F5

    p = Phrase('je fais un mooc sur python')
    len(p)
    'mooc' in p

> Reprendre `Phrase.py` et dans la classe `Phrase`:

        def __contains__(self, mot):
             return mot in self.mots

> Faire Control-s puis F5

    p = Phrase('je fais un mooc sur python')
    len(p)
    'moon' in p
    'mooc' in p
    print(p)

> Reprendre `Phrase.py` et dans la classe `Phrase`:

        def __str__(self):
            return "\n".join(self.mots)

> Faire Control-s puis F5

    p = Phrase('je fais un mooc sur python')
    len(p)
    'mooc' in p
    print(p)

# w6s3. Héritage
-------------

> Reprendre `Phrase.py` et modifier `s`:

    s = 'Je fais un MOOC sur Python'

> et après la classe `Phrase`:

    class PhraseSansCasse(Phrase):
        pass

> Faire Control-s puis F5

    p_no = PhraseSansCasse(s)
    isinstance(p_no, Phrase)
    isinstance(p_no, PhraseSansCasse)
    p_no

> Rajouter dans la classe `PhraseSansCasse`:

        def __init__(self, ma_phrase):
            Phrase.__init__(self, ma_phrase)
            self.mots_lower = {m.lower() for m
                               in self.mots}

> Faire Control-s puis F5

    p_no = PhraseSansCasse(s)
    p_no.mots_lower

> Rajouter dans  la classe PhraseSansCasse:

        def __contains__(self, mot):
            return mot.lower() in self.mots_lower

> Faire Control-s puis F5

    p_no = PhraseSansCasse(s)
    'Mooc' in p_no
    p = Phrase(s)
    p_no = PhraseSansCasse(s)
    'mooc' in p
    'mooc' in p_no
    p.nb_lettres()
    p_no.nb_lettres()

# w6s4. Héritage multiple et ordre de résolution des attributs
-------------

    class C:
        pass
    c = C()
    c.__class__
    C.__bases__
    print(c)
    print(C)
    C.mro()

    class SuperA:
        pass
    class SuperB:
        pass
    class C(SuperA, SuperB):
        pass
    C.mro()
    class C(SuperB, SuperA):
        pass
    C.mro()

    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    D.mro()

# w6s5. Variables et attributs
-------------

> Reprendre spam.py

    # fichier spam.py
    a = 1

    def f():
        a = 2

    class C():
        a = 3
    f()
    ins = C()
    print(a)
> Faire Control-s puis F5

    # fichier spam.py
    a = 1
    class C:
        a = 2
        def f(self):
            print(a)
            print(C.a)
            
    ins = C()
    ins.f()
        
> Faire Control-s puis F5

    # fichier spam.py
    a = 1
    class A:
        a = 2
        class B:
            def f(self):
                print(a)
            
    ins = A.B()
    ins.f()
    
# w6s6. Conception d'itérateurs
-------------

> Reprendre Phrase.py

        def __iter__(self):
            return self

        def __next__(self):
            if not self.mots:
                raise StopIteration
            return self.mots.pop(0)

> Faire Control-s puis F5

    p = Phrase(s)
    [m for m in p]
    [m for m in p]
    next(p)
> Dans la méthode \__iter__

            return IterPhrase(self.mots)

> Une nouvelle classe

    class IterPhrase:
        def __init__(self, mots):
            self.mots = mots[:]

        def __iter__(self):
            return self
        
        def __next__(self):
            if not self.mots:
                raise StopIteration
            return self.mots.pop(0)

> Faire Control-s puis F5

    p = Phrase(s)
    [m for m in p]
    [m for m in p]
    iter(p)
    iter(p)
> Dans la méthode \__iter__

            for m in self.mots:
                yield m

> Faire Control-s puis F5

    p = Phrase(s)
    [m for m in p]
    [m for m in p]
    
# w6s7. Conception d'exceptions généralisées
-------------

> Reprendre Phrase.py

    class PhraseVideError(Exception):
        pass


> Dans la méthode \__init__ de la classe Phrase:

            if not ma_phrase:
                raise PhraseVideError()


> Faire Control-s puis F5

    p = Phrase(s)
    p.mots
    p = Phrase('')

> Dans la méthode \__init__ de la classe Phrase:

                raise PhraseVideError('phrase vide', 18)


> Faire Control-s puis F5

    p = Phrase('')

> Ajouter dans Phrase.py

    try:
        Phrase('')
    except PhraseVideError as e:
        print(e.args)


> Faire Control-s puis F5

# w6s8. Conception de context manager
-------------

    import time
    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self
        
        def __exit__(self, *args):
            duree = time.time() - self.start
            print(f"{duree}s")
            return False

        def __str__(self):
            duree = time.time() - self.start
            return f"intermédiaire: {duree}s"
            
    with Timer() as t:
        sum(x for x in range(10_000_000))
        print(t)
        sum(x**2 for x in range(10_000_000))


> Faire Control-s puis F5

> Ajouter après print(t)

        1/0


> Faire Control-s puis F5

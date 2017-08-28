# -*- coding: utf-8 -*-

## Commençons par créer une variable globale et une fonction
a = 'a globale'

def f():
    a = 'a dans f'
    print(a)

print(a)
f()
print(a)

## La variable a est définie locale et globalement, ce sont donc deux
## variable différentes. Lorsque je fais a = 'locale' dans le
## fonction, je crée une nouvelle variable locale a qui n'a pas de
## rapport avec la variable globale a.

## Pour modifier la variable globale il faut déclarer a comme variable
## globale dans le fonction. On fait cela avec l'instruction global

a = 'a global'

def f():
    global a              # nouvelle ligne
    a = 'a dans f'
    print(a)

print(a)
## je référence a que je trouve globalement
f()
## j'exécute la fonction f qui déclare la variable a comme globale. La
## variable locale a n'est pas créée dans la fonction et toute
## affectation de a sera maintenant considérée comme si elle était
## faite en dehors de toute fonction directement sur la variable
## globale a.

## print(a) cherche a suivant la règle LEGB. a n'est pas défini
## localement (parce que déclarée comme global), il n'y a pas de
## fonctions englobantes, elle est déclarée globalement et au moment
## de l'appel de print(a), la variable globale référence la chaîne 'locale'

print(a)

## comme la variable globale a été modifiée dans la fonction, cela
## afficher 'a dans f'

## Vous remarquez que global peut sembler très pratique pour modifier
## les variables globales depuis une fonction. Cependant, c'est en
## général une très mauvaise idée parce que cela nuit à la clareté du
## code et donc à sa qualité et facilité de maintenance. Regardons
## l'exemple suivant.

a = 10
def f():
    global a
    a = a + 10

f()

## que fait l'appel à f(), f déclare une variable a globale et lui
## ajoute 10. Ce code qui ne fait que 5 lignes peut vous sembler à peu
## prêt acceptable. Il est cependant mauvais. En effet, on référence
## la variable globale 10 de manière implicite (avec la règle LEGB) et
## on modifie la variable globale avec l'instruction global.

## Dans du bon code, on doit rendre toutes les opérations explicites,
## ça réduit la documentation nécessaire et surtout ça enlève tout
## doute sur l'intention du développeur et donc ça facilite la
## recherche de bug. Dans l'exemple précédent, est-ce que le
## développeur avait rééllement l'intention de modifier la variable
## global.

## Comment bien écrire le code ci-dessus, de la manière suivante en
## rendant tout explicite.

note = 10           # je donne un bon nom de variable
def add_10(n):      # ma fonction a un nom explicite et prend un argument
    return n + 10   # je retourne le résultat du calcul

note = add_10(note) # j'affecte le résultat à la variable
                    # explicitement.

## Croyez moi, il n'y a rien de pire a maintenir et débuguer qu'un
## code qui utilise un grand nombre de variable globale.  En résumé,
## on ne peut que vous décourager d'utiliser global, sauf si vous avez
## une très bonne raison qui est très bien documentée de le faire.

################################## 5m00s ######################

## Regardons maintenant nonlocal. Commençons par un exemple

a = 'a global'
def f():
    a = 'a de f'
    def g():
        a = 'a de g'
        print(a)
    g()
    print(a)
f()
print(a)

>>>
a de g
a de f
a global

## j'ai une variable a globale, une variable a locale à f et une
## variable a locale à g. Le print dans le bloc de code de g va
## afficher 'a de g', le print dans le bloc de code de f va afficher
## 'a de f' et le print en dehors de fonction va afficher 'a global'.
## Si je veux modifier la variable global dans f, je peux ajouter un
## 'global a' dans f et si je veux modifier la variable globale a dans
## g, je peux ajouter un 'global a' dans g.

## Mais comment modifier la variable locale de f depuis la fonction g,
## en utilisant nonlocal.  Regardons cela

a = 'a global'
def f():
    a = 'a de f'
    def g():
        nonlocal a               # nouvelle ligne
        a = 'a de g'
        print(a)
    g()
    print(a)
f()
print(a)

>>>
a de g
a de g
a global


## nonlocal a quelques restrictions, notamment nonlocal ne peut pas
## être utilisé pour modifier une variable global, donc une variable
## nonlocal doit obligatoirement être définie dans une fonction
## englobante. Une variable ne peut pas être à la fois dans l'entête
## d'une fonction et définie nonlocal dans cette fonction.

## nonlocal favorise comme global les modifications implicite, mais
## elle trouve quelques usages importants dans des concepts avancés
## comme les décorateurs que nous aborderons dans une prochaine vidéo. 

################################### 8m00 #######################

# -*- coding: utf-8 -*-

## Je rappelle que l'on définit une fonction avec le mot clef
## def suivi du nom de la fonction, d'une liste quelconque
## d'arguments entre parenthèses, séparés par des virgules
## suivi de : et d'un bloc d'instruction indenté de 4 caractères
## vers la droite.

def f(a, b, c):
    print(a, b, c)

f(1, 2, 3)

## En Python tout est un objet. Une fonction est donc un objet
## et le nom de la fonction n'est qu'une variable référençant
## l'objet fonction. On peut donc renomer une fonction simplement
## en affectant l'objet à une nouvelle variable

g = f
g(1, 2, 3)

############################# 1m00s ##########################

## Comme en Python tout est un objet, on a un surcoût mémoire pour
## tout. Il faut donc minimiser les créations d'objets et Python est
## très efficace pour cela. En particulier, en Python, on ne duplique
## jamais les objets (sauf à faire explicitement une copie). Les
## arguments que l'on passe à une fonction sont donc toujours des
## références vers les objets (et jamais une copie d'objet). Les
## passages d'arguments aux fonctions créent donc des références
## partagées vers les objets. On a vu que lorsque l'objet est
## immuable, les références partagées ne pose aucun problème, mais
## lorsque l'objet est mutable, il faut faire attention aux effets de
## bord.

L = []

def add_1(a): # fonction a effet de bord, bien le documenter, montrer list.sort?
    a.append(1)

print(L)
add_1(L)
print(L)

L = [1, 2]
add_1(L[:]) # par contre, pas de retour de la fonction, donc aucun effet. 

## une référence vers la liste L a été passé à la fonction add_1, la
## fonction a modifié en place la liste, donc en sortie de la fonction
## la liste reste modifiée.

################################ 1m45s (cumul: 2m45s) ################


## On peut donner une valeur de retour à notre fonction
## avec l'instruction return. Cette valeur de retour
## peut être assignée à une variable lors de l'appel
## de la fonction. S'il n'y a pas de return, la fonction
## retourne None.

print add_1(L)

def add_1(a):
	a = a[:]
    a.append(1)
    return a

L = add_1(L)
print(L)

## Return peut appaître n'importe ou dans une fonction et
## il peut même y avoir plusieurs return. Cependant, le
## premier return rencontré lors de l'exécution du code de
## la fonction sortira immédiatement de la fonction.

def f(a, b, c):
    if b > 10:
        return a
    else:
        return c

print(f(1, 11, 2))

################################ 1m45s (cumul: 4m30s) ################

## il y a un autre point important que je voudrais aborder dans cette
## introduction générale aux fonctions. Lorsque le code d'une fonction
## est évalué, c'est-à-dire lorsque l'on tape un retour chariot dans
## l'interpréteur Python après la définition d'une fonction, ou
## lorsque l'on exécute un fichier .py contenant une fonction, l'objet
## fonction est créé, mais le code dans le corps de la fonction n'est
## pas evalué. Ce code ne sera évalué qu'à l'appel de la
## fonction. Cela permet à une fonction d'utiliser du code non encore
## implémenté au moment de la définition de la fonction, mais
## implémenté plus tard.  regardons un exemple.

def f(a):
    g(a)

print(f) # on a bien un objet fonction
#f(1)   # mais on a une exception lors de l'appel puisque func
        # n'existe pas encore. 

def g(a):
    print(a)

f(1)

################################ 1m30s (cumul: 6m00s) ################

## Pour finir, je vais vous parler de polymorphisme qui
## représente un concept tout simple.

## Une fonction est polymorphe lorsqu'elle accepte en argument
## des objets de n'importe quel type. En Python, le typage est
## dynamique, donc toutes les fonctions sont naturellement
## polymorphes. Regardons un exemple

def my_add(a, b):
    print(f"j'ajoute{a} et {b}")
    return a + b

my_add(1, 2)
my_add(1.5, 2.3)
my_add('spam', 'good')
my_add([1], [2])

################################ 2m00s (cumul: 8m00s) ################

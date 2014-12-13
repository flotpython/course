# -*- coding: utf-8 -*-

## prenons un problème simple, je veux afficher la liste des entiers
## de 1 à 10 et de leur carré.
print 1, 1**2
print 2, 2**2
print 3, 3**2

## on se rend vite compte que l'on fait 10 fois la même tache avec
## une petite variation, la valeur de x. Les boucles for existe justement
## pour factoriser ce type de taches. Regardons comme on écrit une boucle for

for x in range(1,11):
    print x, x**2
print "on est sorti de la boucle"
## La boucle for utilise (comment souvent en Python), une notation
## simple et intuitive. On commence une boucle for par l'instruction
## for puis, on spécifie une variable (x dans notre cas), l'instruction
## in, et une séquence. On fini la ligne avec un : ce qui veut
## dire que l'on va avoir un nouveau bloc d'instruction décalé
## de 4 caractères vers la droite par rapport au for.
## La boucle for va répéter le bloc d'instruction autant fois qu'il
## y a d'éléments dans la séquence. À la premiere exécution du bloc
## d'instruction, la variable x référence le premier élément de la séquence
## et à chaque nouvelle répétition du bloc d'instruction x référencera
## l'élément suivant dans la séquence jusq'au dernier élément de la séquence. 
## Lorsqu'il n'y a plus d'élément dans la séquence on sort de la boucle
## for, c'est-à dire que l'on continu avec le bloc de code aligné avec
## la boucle for.

## comme un boucle for fonctionne sur toutes les séquences, on peut
## faire une boucle for sur un chaîne de caractères par exemple
for i in 'spam':
    print i + ' ',
    
print
## ou sur une liste d'éléments quelconques.
L = [1, 'spam', 3.2, True]
for i in L:
    print i

#2 minutes 50 secondes

## regardons maintenant un autre problème. Je veux a différents moments
## de mon programme faire une opération, par exemple, afficher
## sur la sortie standard tous les éléments d'une liste et leur carré.

L1 = [1, 4, 6, 7, 10, 11, 30, 50]
for x in L1:
    print x, x**2

L2 = [3.4, 11, 22, 150.435, 18]
for x in L2:
    print x, x**2

## on voit que grace à la boucle for, je peux factoriser mon code, mais
## que malgré tout je répète deux fois exactement la même boucle for.
## Un moyen de factoriser encore plus ce code est d'utiliser ce que l'on
## appelle une fonction. Regardons comment on écrit une fonction

def f(L):
    for x in L:
        print x, x**2

## une fonction commence avec l'instruction def, on donne ensuite un nom
## à la fonction (f ici). puis en met entre paranthèses l'argument de la
## fonction (L dans notre cas) et on finit une fois encore par un :
## qui signal un nouveau bloc d'instruction qui doit être indenté de 4
## caractère vers la droite par rapport au premier caractere du la
## permière ligne de la fonction, donc le d du def. On appelle de bloc
## d'instructions le corps de la fonction. 
## Le principe d'une fonction est que le bloc d'instruction dans la fonction
## (c'est-à-dire indenté de 4 caractères vers la droite) est exécuté
## à chaque appel de la fonction avec l'argument passé au moment de la
## fonction. C'est très facile d'appeler une fonction et de lui passer un
## argument, il suffit de taper le nom de la fonction suivi de l'argument
## entre parenthèses.

f(L1)
f(L2)

# 6 minutes ##

## Une caractéristique importante des fonctions est sa valeur de retour.
## En effet, une fonction retourne toujours un objet. Par défaut
## elle retourne l'objet None qui est un objet vide, sans valeur,
## mais on peut définir un autre objet retourné avec l'instruction
## return.

## la valeur de retour d'une fonction peut-être affecté à une variable
## de la manière suivante

r = f(L1) ## c'est None qui est retourné.
print r

def f(L):
    for x in L:
        print x, x**2
    return 'fin du calcul'

##

r = f(L1)
print s

# 7 mintes 10 secondes

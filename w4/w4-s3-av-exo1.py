# -*- coding: utf-8 -*-

## L'instruction while évalue un test qui peut s'écrire
## exactement comme un test dans un if. Ce test peut-être
## par exemple le résultat d'une comparaison, d'un retour
## fonction, d'un opérateur de test booléen (and, or, not)
## ou directement un type built-in qui vaut faux lorsque
## c'est 0, None, ou un objet vide (liste vide, set vide)
## et True dans tous les autres cas. 

## Tant que le test est vrai, le while répète le
## bloc d'instruction sous le while, lorsque le
## test est faux, on sort du while. 

## commençons par créer une liste de 9 entiers allant de 1 à 9. On
## utilise pour cela range(1, 10) qui retourne un objet de type range,
## puis pour obtenir une liste on caste cet objet dans list()

a = list(range(1, 10))

while a:
    a.pop()
    print(a)

## while accepte les instructions break, pour sortir du while, et
## continue, pour remonter directement à l'évaluation du test.
## Regardons cela

a = list(range(1, 10))
while a:   
    a.pop()
    if len(a) == 5:
        continue
    print(a)

## on voit que le continue est remonté directement en haut du while
## sans exécuter le print. remplaçons le continue par un break


a = list(range(1, 10))
while a:   
    a.pop()
    if len(a) == 5:
        break
    print(a)
    
## on voit maintenant que l'on est directement sorti du while lorsque
## la liste avait 5 éléments

## Un usage fréquent du while est le suivant. On fait une boucle
## infinie avec un while True et on sort de cette boucle avec un break
## sous une certaine condition. La raison de cette construction est de
## parcourir un bloc d'instruction autant de fois de que nécessaire
## alors que l'on ne connait pas au départ le nombre de
## répétition. C'est un usage fréquent, par exemple, lorsque l'on a un
## programme qui répond à des entrées utilisateur.
    
while True:
    s = input('Quelle est votre question\n')
    if 'aucune' in s:
        break
    #answer(s) # fonction pour le traitement de la reponse


## Pour finit, reprenons notre exemple d'intelligence artificiel de la
## vidéo sur Les tests if/elif/else et les opérateurs booléens et
## adaptons notre while

###################### PAUSE ########################################
####################### RECOPIER LE CODE SUIVANT DANS IDLE ###########
s = input("Quelle est votre question\n")
if s.startswith('bonjour'):
    print("bonjour, comment allez vous ?")
elif "bien" in s:
    print("c'est super !")
elif "bye" in s:
    print("Au revoir !")
else:
    print("mais encore...")
######################################################################
####################### RESUME SUR IDLE ############################

## voici le code que l'on avait, n'hésitez pas à faire une pause sur
## la vidéo si vous voulez un peu de temps pour le taper. 

s = input("Quelle est votre question\n")  ## new 
while True:
    if s.startswith('bonjour'):
        print("bonjour, comment allez vous ?")
    elif "bien" in s:
        print("c'est super !")
    elif "bye" in s:
        print("Au revoir !")
        break                               ## new
    else:
        print("mais encore...")
    s = input()                             ## new


>>> bonjour
>>> je vais bien
>>> je fais un mooc sur Python
>>> c'est pratique un while
>>> bye

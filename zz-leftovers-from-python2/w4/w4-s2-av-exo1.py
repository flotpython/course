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

L = range(10)

while L.pop():
    print L

## Notons que le while, comme la boucle for, accepte
## les instructions break, pour sortir du while, et
## continue, pour remonter directement à l'évaluation
## du test. 

## Un usage fréquent du while est le suivant. On fait
## une boucle infinie avec un while True et on sort
## de cette boucle avec un break sous une certaine
## condition. C'est un usage fréquent lorsque l'on a
## un programme qui répond à des entrées utilisateur. 
    
while True:
    s = raw_input('Quelle est votre question ?\n')
    if 'aucune' in s:
        break
    #answer(s) # fonction pour le traitement de la reponse

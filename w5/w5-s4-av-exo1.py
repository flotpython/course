# -*- coding: utf-8 -*-

## prenons un exemple de compréhension de liste

carre = [x**2 for x in range(1000)]

## carre référence bien une liste

print(carre)

## je peux maintenant calculer la somme de tous les éléments de la
## liste avec la fonction built-in sum

sum(carre)

## Mais on voit bien ici que la création de la liste intermédiaire
## carre a pour unique but de permettre à sum() de parcourir les
## carrés des entiers de 0 à 999. Un itérateur serait ici serait
## suffisant. Regardons alors le cas d'une expression
## génératrice. Pour créer une expression génératrice, je n'ai qu'à
## remplacer les crochets par des parenthèses

gen_carre = (x**2 for x in range(1000))

## Cette expression génératrice va calculer à la volée les carrés de x
## lorsque x parcours range(1000). C'est un itérateur que je ne peux
## donc parcourir qu'une seule fois, mais l'avantage est que je ne
## crée à aucune moment une liste temporaire. Notons également que
## comme range() ne crée pas de liste, cette expression génératrice ne
## crée aucune structure de donnée temporaire. 

sum(gen_carre) # affiche 285332833500

sum(gen_carre) # affiche 0

## en effet l'itérateur est consommé et retourne maintenant stop
## itération

next(gen_carre)

## notons que comme un générateur ne fait aucun calcul tant qu'il
## n'est pas parcouru, le coût de création d'un nouveau générateur est
## très faible.

## On peut évidement réutiliser notre expression dans une autre
## expression et ainsi chainer des expressions génératrices sans
## jamais créer de structure de données temporaire. Cherchons les
## palindromes des tous les nombres carrés, c'est-à-dire les nombre
## qui peuvent se lire de gauche à droite ou de droite à gauche comme
## 121

gen_carre = (x**2 for x in range(1000))
palin = (x for x in gen_carre if str(x) == str(x)[::-1])

## pour afficher le résultat, je peux mettre ce résultat dans une
## liste, on voit donc ici que je ne crée ma liste qu'au dernier
## moment, uniquement lorsque j'en ai besoin. 
list(palin)


## En résumé, les expressions génératrices permettent de transformer
## les compréhensions de listes en itérateur. L'avantage est qu'il n'y
## a plus de création de listes temporaires et donc plus de limite
## dues à la mémoire, sur le nombre d'opérations que vous pouvez
## faire.

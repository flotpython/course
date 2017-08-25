# -*- coding: utf-8 -*-

################## Utiliser IDLE ##################

## prenons un problème simple, je veux afficher la liste des carrés
## des entiers allant de 0 à 10
print(0**2)
print(1**2)
print(2**2)
print(3**2)

## on se rend vite compte que l'on fait 10 fois la même tache avec une
## petite variation, la valeur de x. Les boucles for existe justement
## pour factoriser ce type de taches. Regardons comme on écrit une
## boucle for

for i in range(11):
    print(i**2)

## La boucle for utilise (comment souvent en Python), une notation
## simple et intuitive. On commence une boucle for par l'instruction
## for puis, on spécifie une variable (x dans notre cas),
## l'instruction in, et un itérable. Un itérable est un objet que l'on
## peut parcourir avec un boucle for. En particulier les séquence et
## [[TP: le résultat de ?]] la fonction range() sont itérable. On fini la ligne avec un : ce
## qui veut dire que l'on va avoir un nouveau bloc d'instruction
## décalé de 4 caractères vers la droite par rapport au for.  La
## boucle for va répéter le bloc d'instruction autant fois qu'il y a
## d'éléments dans la séquence. À la premiere exécution du bloc
## d'instruction, la variable x référence le premier élément de la
## séquence et à chaque nouvelle répétition du bloc d'instruction x
## référencera l'élément suivant dans la séquence jusqu'au dernier
## élément de la séquence.  Lorsqu'il n'y a plus d'élément dans la
## séquence on sort de la boucle for, c'est-à dire que l'on continu
## avec le bloc de code aligné avec la boucle for.

## comme une boucle for fonctionne sur toutes les séquences, on peut
## faire une boucle for sur un chaîne de caractères par exemple
[[TP: ça sert à quoi l'espace ici, ça se voit pas à l'écran, si ?]]
for i in 'spam':
    print(i + ' ')
    

## ou sur une liste d'éléments quelconques.
truc = [1, 'spam', 3.2, True]
for i in truc:
    print(i)

#2 minutes 50 secondes

## regardons maintenant un autre problème. Je veux a différents
## moments de mon programme faire une opération, par exemple, afficher
## sur la sortie standard les carrés de tous tous les éléments d'une
## liste

data_1 = [1, 4, 6, 7, 10, 11, 30, 50]
for i in data1:
    print(i**2)

data_2 = [3.4, 11, 22, 150.435, 18]
for i in data_2:
    print(i**2)

## on voit que grace à la boucle for, je peux factoriser mon code, mais
## que malgré tout je répète deux fois exactement la même boucle for.
## Un moyen de factoriser encore plus ce code est d'utiliser ce que l'on
## appelle une fonction. Regardons comment on écrit une fonction

def carre(data):
    for i in data:
        print(i**2)

## une fonction commence avec l'instruction def, on donne ensuite un
## nom à la fonction (ici carre). puis en met entre paranthèses le ou les arguments
## de la fonction (ici un seul argument data) et on finit une fois encore par
## un : qui signal un nouveau bloc d'instruction qui doit être indenté
## de 4 caractère vers la droite par rapport au mot-clé def. On appelle le
## bloc d'instructions le corps de la fonction.  Le principe d'une
## fonction est que le bloc d'instruction dans la fonction
## (c'est-à-dire indenté de 4 caractères vers la droite) est exécuté à
## chaque appel de la fonction avec l'argument passé au moment de
## l'appel.  C'est très facile d'appeler une fonction et de lui passer
## un argument, il suffit de taper le nom de la fonction suivi de
## l'argument entre parenthèses.

carre(data_1)
carre(data_2)

# 6 minutes ##

## Une caractéristique importante des fonctions est sa valeur de retour.
## En effet, une fonction retourne toujours un objet. Par défaut
## elle retourne l'objet None qui est un objet vide, sans valeur,
## mais on peut définir un autre objet retourné avec l'instruction
## return.

## la valeur de retour d'une fonction peut-être affecté à une variable
## de la manière suivante

result = carre(data_1) ## comme carre ne contient pas de return, c'est None qui est retourné.
print(result)

[[TP: je propose de faire un peu moins neuneu, car on a déjà tout le bagage pour faire ça comme il faut
  ce qui permettrait de placer une tirade sur le fait que print ne nous sert que
  a des fins pedagogiques mais que le vrai code n'utilise pratiquement jamais print,
  et qu'il vaut bcp mieux pour une fonction retourner une valeur que d'imprimer des trucs 
  et en plus ça fera une transition pour la vidéo qui vient juste après
]]

def carre(data):
    resultat = []
    for i in data:
        resultat.append(i**2)
    return resultat

##

result = carre(data_1)
print(result)

# 7 mintes 10 secondes

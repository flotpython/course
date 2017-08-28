# -*- coding: utf-8 -*-

## Nous avons déjà vu la déclaration de paramètres ordonnées

def agenda(nom, prenom, tel):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## et l'appel de fonction avec le passage d'arguments
## ordonnés.

d = agenda('idle', 'eric', '0720202020')
print(d)

## Il y a cependant une limitation avec cet appel : on doit connaître
## l'ordre des paramètres. Lorsqu'il y a beaucoup de paramètres et que
## leur nom est bien choisi il est plus facile de se souvenir du nom
## des paramètres que de leur ordre. C'est pourquoi, il est possible
## d'appeler une fonction en plaçant les arguments dans un ordre
## quelconque du moments qu'on les nomme avec le nom du paramètres
## correspondant

d = agenda(tel='0720202020', nom='idle', prenom='eric')

## Même s'il est possible de mélanger des arguments ordonnés et des
## arguments nommés lors de l'appel, c'est rarement pertinent de le
## faire. En effet, soit on connait l'ordre des paramètres et dans ce
## cas on utilise des arguments ordonnés lors de l'appel. Soit on ne
## connait pas l'ordre alors on utilise des arguments nommés. Si on
## les mélanges cela peut conduire à des erreurs subtiles que nous
## détaillerons dans les compléments.

## Si l'on revient à notre déclaration de fonction, on pourrait
## vouloir créer une entrée dans l'agenda sans donner un
## téléphone. C'est ce que l'on appelle un argument optionnel. Le
## moyen le plus simple est d'utiliser les paramètres par
## défaut. Regardons un exemple

def agenda(nom, prenom, tel='na'):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## si on ne founit pas l'argument lors de l'appel, c'est
## la valeur par défaut du paramètre qui est utilisée.
print(agenda('idle', 'eric'))

## sinon c'est l'argument que l'on passe. 
print(agenda('idle', 'eric', '0720202020'))

## lorsque dans la déclaration de notre fonction on a des paramètres
## ordonnés et des paramètres par défaut, il faut toujours mettre les
## paramètres ordonnés en premier et les paramètres par défaut
## après. On ne peut pas les mélanger.

## Nous avons donc vu deux manières de déclarer les paramètres d'une
## fonction : paramètres ordonnés et paramètres par défaut; et deux
## manières d'appeler une fonction, arguments ordonnés et arguments
## nommés.



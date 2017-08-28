# -*- coding: utf-8 -*-

## Nous avons déjà vu la déclaration d'arguments ordonnées

def agenda(nom, prenom, tel):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## et l'appel de fonction avec le passage d'arguments
## ordonnés.

d = agenda('idle', 'eric', '0720202020')
print(d)

## Il y a cependant une limitation avec cet appel : on doit connaître
## l'ordre des arguments. Lorsqu'il y a beaucoup d'arguments et que le
## nom des arguments est bien choisi il est plus facile de se souvenir
## du nom des arguments que de leur ordre. C'est pourquoi, il est
## possible d'appeler une fonction en plaçant les arguments dans un
## ordre quelconque du moments qu'on les nomme

d = agenda(tel='0720202020', nom='idle', prenom='eric')

## Même s'il est possible de mélanger des arguments ordonnés et des
## arguments nommés lors de l'appel, c'est rarement pertinent de le
## faire. En effet, soit on connait l'ordre des arguments et dans ce
## cas on utilise des arguments ordonnés lors de l'appel. Soit on ne
## connait pas l'ordre alors on utilise des arguments nommés. Si on
## les mélanges cela peut conduire à des erreurs subtiles que nous
## détaillerons dans les compléments.

## Si l'on revient à notre déclaration de fonction, on pourrait
## vouloir créer une entrée dans l'agenda sans donner un
## téléphone. C'est ce que l'on appelle un argument optionnel. Le
## moyen le plus simple est d'utiliser les arguments par
## défaut. Regardons un exemple

def agenda(nom, prenom, tel='na'):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## si on ne founit pas l'argument lors de l'appel, c'est
## l'argument par défaut qui est utilisé.
print(agenda('idle', 'eric'))

##sinon c'est l'argument que l'on passe. 
print(agenda('idle', 'eric', '0720202020'))

## lorsque dans la déclaration de notre fonction on a des
## arguments ordonnés et des arguments par défaut,
## il faut toujours mettre les arguments ordonnés en premier
## et les arguments par défaut après. On ne peut pas les
## mélanger. 

## Nous avons donc vu deux manières de déclarer les arguments d'une
## fonction : arguments ordonnés et arguments par défaut; et deux
## manières d'appeler une fonction, arguments ordonnés et arguments
## nommés.



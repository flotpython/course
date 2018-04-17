# -*- coding: utf-8 -*-

## On peut écrire des listes, tuples, set et dictionnaires
## sur plusieurs lignes. Lorsque les éléments sont séparés
## par des virgules, on a l'habitude le mettre une virgule
## en fin de ligne plutôt qu'en début. On aligne chaque
## premier élément de la ligne pour la lisibilité, les espaces
## ne sont pas pris en compte. 

print [1,
       2]

print (1,
       2) 

print {1,
       2}

print {'a': 1,
       'b': 2}

print (1 + 2 + 3 +
       4)

## par contre pour les chaînes de caractères, on doit
## mettre un backslash en fin de ligne et tous les caractères
## ajoutés en début de ligne seront pris en compte dans
## la chaîne. 

print 'une grande\
 phrase'

# xxx comme la fois précédente, perso je ne mettrais pas l'exemple des strings
# 1. les strings multilignes sont beaucoup mieux avec des """
# 2. c'est plus utile je pense de montrer un appel de fonction - il n'y en a pas ci-dessus

    monobjet.mamethode (le_premier_argument,
                        on_doit_appeler_une_fonction (x,y,z),
                        le_dernier_argument)

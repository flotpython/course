# vidéo 2.2 Les chaînes de caractères 1/2

À 5:05, les f-string sont introduites depuis Python 3.6 (en non Python 3.5)

# vidéo 3.2 Les tuples

À 5:48, y référence une liste (et non un tuple)

# vidéo 3.4 Les dictionnaires

À 4:20, je dis que les dictionnaires ne sont par ordonnés. En Python 3.6, 
on avait par effet de bord de l'implémentation la préservation de l'ordre d'insertion des clefs. 
En Python 3.7, cette préservation de l'ordre d'insertion des clefs des dictionnaires est devenue
officielle https://mail.python.org/pipermail/python-dev/2017-December/151283.html

# vidéo 3.5 Les ensembles

À 1:34 je stocke dans un set True et 1. Or True est égal à l'entier 1 (True == 1), par conséquent on n'aura
dans le set au final que l'entier 1 et plus True. C'est ce que l'on peut vérifier à 2:55. 
Il s'agit d'un comportement normal, mais qui sans cette explication pourrait entrainer un peu de confusion. 


# vidéo 6.5 Variables et attributs

De 4:00 à 5:00, je fais plusieurs lapsus entre liaison et référence. La liaison est le mécanisme qui 
lie une variable à un bloc de code, la référence est le mécanisme qui associe une variable 
à un objet. Dans le premier exemple, x=1 va à la fois permettre à la variable x de référencer l'objet 1, mais
également de lier la variable x au bloc de code dans lequel elle est déclarée. 

# vidéo 7.4 numpy: vectorisation

À  3:50 je fais un lapsus et dis 82 ms au lieu de  5 ms

# vidéo 7.9 pandas: gestion des dates et des séries temporelles
À 0:55 la granularité de la nanoseconde permet d'encoder toutes les dates de 1678 à 2262

# vidéo 9.4 Les métaclasses

De 5:40 à 6:20 je dis que type est la super classe de toutes les classes, c'est un lapsus. type est
la métaclasse de toutes les classes. 

# vidéo 9.5 property et descripteurs

À 5:00 lorsque je crée une property, on pourrait à ce moment (et c'est en général ce que l'on veut)
modifier __init__ avec self.temperature = t (et non self._temperature = t) ainsi, on bénéficie 
à la création de l'instance du mécanisme de validation de la property. 
Donc à 5:50, __init__ peut bien avoir un attibut temperature (sans le underscore), mais pas
get_temperature et set_temperature. 

# vidéo 9.6 Protocole d'accès aux attributs

À 5:30 à 5:40 je vais un lapsus, je dis set_temperature au lieu de __setattr__
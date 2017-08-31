# -*- coding: utf-8 -*-

## Commençons par regarder le comportement d'un itérable.
## Prenons une liste de 3 éléments

a = [1, 2, 3]

## la liste est un type built-in qui est itérable. vérifions le

iter(a)

## retourne un nouvel objet list_iterator

## Évidemment, je peux manipuler l'itérateur de list et le parcourir,
## même si en pratique on ne le fait jamais, puisque c'est le
## mécanisme d'itération qui gère les itérateurs pour nous

## Mais lorsqu'on n'a pas un objet itérable, mais uniquement un
## itérateur, on doit être conscient qu'on ne peut le parcourir qu'une
## seule fois.

## Dans quel cas, on a uniquement un itérateur ? C'est comme on vient
## de le dire le cas des fichiers. En effet, lorsque vous ouvrez un
## fichier, ça ne crée par un objet qui contient toutes les lignes de
## votre fichier, mais uniquement un itérateur capable de parcourir
## ligne par ligne le fichier stocké sur le disque dur. Par
## conséquent, comme un objet fichier est un itérateur, il ne peut
## parcourir le fichier qu'un seule fois, mais il ne crée aucune
## structure de donnée temporaire qui pourrait être très couteuse en
## mémoire et longue à créer si le fichier est grand. 

## Un autre exemple est la fonction built-in zip qui combine deux
## listes ensemble. 

a = [1, 2]
b = [3, 4]
z = zip(a, b)

## z est bien un itérateur que l'on ne peut parcourir qu'une seule
## fois.
z is iter(z)

[i for i in z]

## on obtient bien la combinaison des deux listes

[i for i in z]

## on n'obtient rien parce que zip() retourne un itérateur et que
## l'itérateur z a été consommé

## évidemment, si vous avez besoin d'un itérable plutôt que d'un
## itérateur (c'est très rare) vous pouvez passer l'itérateur au
## constructeur d'un itérable comme une liste ou un set. Mais
## attention, en Python on préfère toujours travailler avec des
## itérateurs plutôt que des itérables quand c'est possible. 

z = zip(a, b)

l = list(z)

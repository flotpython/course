# -*- coding: iso-8859-15 -*-

## Pour ouvrir un fichier on utilise la fonction built-in open.
## Attention, le nom de cette fonction peut-être trompeur.
## La fonction open ne permet pas seulement d'ouvrir un
## fichier qui existe déjà, mais elle permet aussi de créer
## un nouveau fichier. En fait, le rôle exact de la fonction
## open est déterminé par ce que l'on appel le mode d'ouverture.

## Regardons, maintenant comment créer un fichier, écrire
## dedans sur chaque ligne un nombre et son carré

f = open('C:\Temp\spam.txt', 'w')

## le mode w ouvre le fichier en écriture et efface le
## contenu précédent. Attention w est une chaîne de caractères

## on ne peut écrire dans un fichier que des chaînes de
## caractères, en d'autres termes write s'attend a recevoir un string
## on utilise donc format; remarquez bien la fin de ligne qui s'écrit "\n"
for i in range(100):
    line = "{} {}\n".format(i,i**2)
    f.write(line)

f.close()

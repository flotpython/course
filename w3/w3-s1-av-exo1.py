# -*- coding: utf-8 -*-

################# FICHIER TEXTE ###################### (6m00)

## Je vous rappelle que lorsque nous avons parlé des chaînes de
## caractères en Python, je vous ai dit qu'il fallait maitriser votre
## encodage à chaque lecture ou écriture. On se rend bien compte que
## s'il fallait encoder les chaines de caractères à la main pour les
## écrire dans un fichier et les décoder pour les lire, l'ecriture et
## la lecture des fichiers seraient peu commode. Heureusement, l'objet
## fichier gère toutes ces opérations pour nous, nous n'avons qu'à lui
## donner l'encodage à utiliser.

## Pour ouvrir un fichier on utilise la fonction built-in open.
## Attention, le nom de cette fonction peut-être trompeur.  La
## fonction open ne permet pas seulement d'ouvrir un fichier qui
## existe déjà, mais elle permet aussi de créer un nouveau fichier. En
## fait, le rôle exact de la fonction open est déterminé par ce que
## l'on appel le mode d'ouverture.  il y a deux modes principaux, le
## mode r pour lire le fichier et le mode w pour écrire dans le
## fichier.

## Regardons, maintenant comment justement créer un fichier

f = open(r'C:\tmp\spam.txt', 'w', encoding='utf8') # expliquer chaque
                                                   # argument
                                                   #
                                                   # raw string
                                                   # w est une str
                                                   # encoding est str

## Si je ne donne pas le paramêtre encoding, l'encodage utilisé sera
## celui du système de fichiers de mon ordinateur. Ça veut donc dire
## que l'encodage dépendra de la machine que vous utilisez, ce qui est
## toujours une mauvaise idée. Je vous le répète, il faut maitriser
## votre encodage en utilisant toujours utf8 sauf si on a une bonne
## raison de faire autrement.

for i in range(100):
    f.write(f"ligne {i+1}\n")  # écrit la chaine line dans le fichier 

## il faut ensuite obligatoirement fermer le fichier avec un close()

f.close()

## regardons le fichier créé
!type c:\tmp\spam.txt # dans ipython uniquement sous linux utiliser
                      # less ou cat


## Vous remarquez qu'une fois le fichier ouvert, on ne s'est plus
## préoccupé de l'encodage. Python a automatiquement
## encodé nos chaînes de caractères en utf8 avant de les écrire,
## et l'opération inverse sera faite lors de la lecture.

## Regardons maintenant, comment lire le fichier, le modifier et
## réécrire dans un autre fichier

f = open(r"C:\tmp\spam.txt", 'r', encoding='utf8')
f2 = open(r"C:\tmp\spam2.txt", 'w', encoding='utf8')

## les objets fichiers sont itérable, ça veut dire qu'on peut les
## parcourir dans une boucle for, chaque tour de la boucle retourne
## une nouvelle ligne de fichier. Regarder comme il est facile
## d'ouvrir un fichier, de la parcourir, de changer une colonne
## et de changer le format. 
for line in f:
    l = line.split()
    l[0] = l[0].upper()
    f2.write(",".join(l)+'\n') # attention au \n

f.close()
f2.close()

!type c:\tmp\spam.txt
!type c:\tmp\spam2.txt

## une dernière subtilité sur laquelle nous reviendrons lorsque nous
## parlerons des itérateurs, un fichier ne peut être parcouru qu'une
## seule fois dans une boucle for. Pour le parcourir de nouveau du
## début, le plus simple est de le fermer puis le reouvrir. 

## nous verrons dans la suite de cette vidéo pourquoi on doit fermer
## les fichiers avec close, comment remplacer close avec un contexte
## manager et comment ouvrir des fichiers binaires.




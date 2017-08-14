# -*- coding: utf-8 -*-

####################### CONTEXT MANAGER ############### (1m30)

## lorsque l'on ouvre un fichier dans un context manager, le fichier
## sera automatiquement fermé en sortie du context manager, même si le
## programme crash en cours d'exécution. Regardons cela

with open(r"c:\tmp\spam.txt", "r", encoding="utf8") as f: # expliquer
                                                          # la syntaxe
    for line in f:
        print(line)


## Dès que l'on sort du bloc de code sous le contexte manager, le
## fichier est automatiquement fermé même si le programme plante en
## cours d'exécution dans le bloc de code du context manager. C'est le
## mécanisme de fermeture des fichiers le plus robuste et c'est celui
## qu'il faut utiliser dans votre code.



####################### FICHIER BINAIRE ############### (2m45)

## Pour conclure sur les fichier, j'aimerai parler des fichiers
## binaires. En effet, pour le moment, nous n'avons parlé que de
## l'écriture d'un fichier en mode texte. Seulement tous les fichiers
## ne sont pas des fichiers text, un grand nombre de fichiers est
## binaire et dans ce cas un décodage automatique en utilisant un
## encodage pour du texte comme UTF8 n'aurait pas sens. Il faut donc
## être capable d'ouvrir un fichier binaire sans appliquer d'encodage.
## En Python c'est très simple, il suffit d'ajouter un b devant le
## mode d'ouverture du fichier. Comme le fichier est ouvert en mode
## binaire et qu'aucun encodage n'est appliqué, on ne peut lire ou
## écrire que des chaîne de type bytes. Regardons un exemple.


with open(r'C:\tmp\spam.bin', 'bw') as f:# pas d'encodage
    for i in range(100):
        line = b"\x3d"  # \x3d est le signe =. attention au b devant la
                        # chaine pour forcer le type bytes
        f.write(line)  # écrit la chaine line dans le fichier 

## Pour résumer, lorsqu'un fichier est ouvert en mode texte, on doit
## controller l'encodage et on peut lire ou écrire directement des
## chaines de type str. Quand le fichier est ouvert en mode binaire,
## il n'y a pas d'encodage et on lit ou écrit directement des chaines
## de type bytes.


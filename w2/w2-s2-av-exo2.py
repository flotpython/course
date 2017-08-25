# -*- coding: utf-8 -*-


###################### UNICODE ############################### 2m40

## NOTE AL: mettre le terminal avec la font par défault Lucida Console

## Parlons maintenant du support d'unicode en Python. Les chaînes de
## caractères supportent nativement unicode. Ça veut dire qu'une
## chaîne de caractère en Python peut supporter tous les caractères
## disponible en unicode.  Pour entrer un caractère unicode, soit vous
## le tapez directement sur votre clavier, si ce caractère est
## supporté par votre clavier, soit vous utilisez sont code
## unicode. Regardons cela,

"noël, été"
"\u03a6"    # Phi majuscule
"\u0556"    # lettre arménienne Fé

## vous remarqué que vous voyez un carré à la place de la lettre. Que
## ce passe-t-il ? Les chaînes de caractères Python supporte tous les
## caractères Unicode, le problème ne vient donc pas de là. 

## Le problème vient du non support de ce caractère par la police de
## caractères que l'on utilise. Quand il n'y a pas un glyphe
## correspondant au caractère, un caractère par défaut est affiché,
## ici un rectangle. La solution est de trouver une autre police qui
## définie ce caractère. [Aller dans propriété, Police, choisir "deja
## vu sans mono"]

"\u0556"

## Il n'y a malheureusement pas de police qui supporte tous les
## caractères unicode, donc si vous voulez afficher des caractères qui
## ne sont pas disponible dans votre langue, vous devrez vous assurer
## que vous avez une police qui supporte ces caractères. 

########################################################## 3m15


## Revenons maintenant à la notion de codage et décodage. Jusqu'à
## maintenant, on n'a travaillé que sur du texte que l'on entrait nous
## même sur la ligne de commande. Par défaut, Python s'attend à
## recevoir du texte en UTF-8, on n'a donc pas à gérer le
## codage. Mais, en pratique, dès que l'on lit ou écrit du texte il
## faut gérer ce codage. Par exemple, lorsque l'on écrit dans une base
## de donnée, il faut écrire avec l'encodage supporté par cette base
## (qui ne sera peut-être pas UTF-8), ou lorsque l'on reçoit des
## données par internet, il faudra les décoder en utilisant le même
## encodage que celui utilisé par l'expéditeur.

## Python permet de facilement gérer ces étapes de codage (qui est le
## passage de texte à binaire) et décodage (qui est l'opération
## inverse).  Le texte est géré en Python par le type str qui supporte
## nativement unicode. Le binaire est géré par le type bytes qui
## stocke les données sans aucun décodage. Évidement, Python founit
## toutes les méthodes pour passer de l'un à l'autre, c'est-à-dire
## pour coder des str et décoder des bytes. Regardons cela.



## créons une chaine de caractères

s = "un noël en été"

## codons cette chaine de caractère en UTF-8 pour obtenir des bytes

en = s.encode('utf8')
[[TP: pourquoi pas l'appeler b pour bytes comme s pour str, tant qu'à faire court
      ou alors appeler les deux variables text et bin respectivement]]
[AL: b n'est pas bien adapté ici, parce qu'il peut y avoir confusion
 entre le b de b"text encode" et le nom de variable. bin est un
 built-in, ça ne va pas non plus]]
 
 
 
 
 ## cette nouvelle chaine de caractère est de type bytes, on remarque
 ## le petit b devant qui permet de faire la différence avec un chaine
 ## de type str
 
 ## cette chaine étant encodée elle est prête à être écrite ou envoyée.
 ## Lorsqu'on lira de nouveau cette chaine, il faudra la décoder
 
 en.decode('utf8')
 
 ## peut bien évidement encoder s dans un autre encodage, il faudra
 ## alors la décoder avec le même encodage
 
 en = s.encode('latin1')
 en.decode('latin1')
 
 ## Une difficulté avec l'encodage est que si on ne le gère pas, Python
 ## va utiliser un encodage par défaut. Ça ne posera aucun problème
 ## tant que vous gardez toutes vos données sur votre ordinateur parce
 ## que vous écrirez et vous lirez avec le même encodage par défaut. Ça
 ## fonctionnera même probablement si vous échangez des données avec des
 ## personnes utilisant le même sytème dans la même langue (par
 ## exemple, Windows 10 en français). Mais dès que vous commencerez à
 ## échanger des données avec des système utilisant d'autres encodages
 ## par défaut vous allez rencontrer des problèmes.
 
 

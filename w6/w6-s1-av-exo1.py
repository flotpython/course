# -*- coding: utf-8 -*-

## Commençons par créer une classe. Une classe est créée avec l'instruction
## class suivi du nom de la classe, puis d'un bloc d'instructions.
## Comme pour une fonction, le nom de la classe est une variable
## qui pointe vers l'objet classe qui est créé.

[[TP; je sais que je suis casse-couille, mais a ce point je dirais bien une petite phrase qui dit que c'est un exemple qui est conçu pour être simple mais qui n'est pas réaliste]]

class Phrase:
    ma_phrase = "je fais un mooc sur python"

print(Phrase)

## Créons maintenant une instance de la classe Phrase
p = Phrase()

print(p)

## En Python, chaque classe et chaque instance a son propre espace de
## nommage.  on accède à l'espace de nommage des objets avec
## l'attribut __dict__ ou de manière équivallente avec la fonction
## built-in vars(), l'espace de nommage est représenté comme un
## dictionnaire

print(Phrase.__dict__)
print(vars(Phrase))

## Notons que toutes les variables commençant et finissant par des
## double tirets bas sont des variables définies par le langage. On ne
## doit donc jamais créer de nouvelles variables utilisant cette
## notation. [[TP ici c'est un attribut, pas une variable]]

## Notons également que l'espace de nommage d'une classe est un
## dictionnaire un peu particulier, un dictproxy, qui est en lecture
## seule. Les classes utilisent un dictproxy pour des raisons
## d'optimisation et de stabilité. Par contre, comme nous allons le
## voir dans quelques instants, ça n'empêche pas les classe d'être
## des objets mutables.

## Regardons maintenant l'espace de nommage de l'instance, on voit
## qu'il est vide

print(vars(p))

## La relation d'héritage permet à une instance d'accéder
## automatiquement à l'espace de nommage de sa classe si un attribut
## n'est pas trouvé localement.  

print(Phrase.ma_phrase)
print(p.ma_phrase)

## L'attribut ma_phrase n'est pas trouvé dans l'espace de nommage de
## l'instance, mais il est trouvé dans celui de la classe.

# COUPE 3m00s

## Les classes et les instances sont des objets mutables, on peut donc
## modifier ou ajouter des attributs après création de l'objet. La
## recherche d'attributs (on dit également résolution d'attributs)
## étant faite sur les espaces de nommage actuels, elle prendra en
## compte toutes les modifications sur ces espaces au moment de la
## recherche.

## Regardons cela

Phrase.mots = Phrase.ma_phrase.split()

print(Phrase.mots)

## l'attribut mots à été ajouté dans la classe, mais pas dans
## l'instance. Comme la recherche d'attributs est dynamique,
## l'attribut mots cherché depuis l'instance sera automatiquement
## trouvé dans la classe Phrase.
print(p.mots)


## évidemment, si mots est définie dans l'instance p, c'est cet
## attribut qui sera retournée

p.mots = 'autres mots'

print(p.mots)
print(Phrase.mots)

print(vars(p))
print(vars(Phrase))

# COUPE 5m00s

## On a vu que la classe fournit un espace de nommage accessible à
## toutes les instances, mais que les instances sont des objets qui
## ont leur propre espace de nommage et qui peut évoluer indépendamment
## de celui de la classe.

## Cependant, il nous manque toujours un notion importante pour
## manipuler les instances, c'est la notion de méthode. Une méthode
## est une fonction qui est définit dans une classe. Elle a cependant
## une particularité, lorsque vous appelez une méthode depuis une
## instance, une référence de l'instance est automatiquement passée à
## cette méthode. Ça permet ainsi d'avoir des méthodes définies dans
## une classe qui peuvent travailler sur les attributs, c'est-à-dire
## l'espace de nommage, de l'instance. 

## Regardons un exemple. Plutôt que d'avoir la même phrase pour toutes
## les instances, je vais créer une méthode dans la classe qui va
## initialiser mon instance avec une phrase.

[[TP: j'aime bien l'idée de ce plan, mais je suggère qu'on utilise justement pas init, mais un nom qui n'a rien a voir, pour éviter de créer de la confusion; je sais pas moi, initialisation, creation, n'importe..], ou comme il faut un truc court, foo carrément]]

class Phrase:
    def init(self, ma_phrase):  #self est un nom de variable, ça n'est
                                #pas un mot clef
        self.ma_phrase = ma_phrase

## le premier argument de la méthode va recevoir une référence de
## l'instance qui appelle la méthode. Traditionnellement, on appelle
## cet argument self.
        
p = Phrase()
p.init("je fais un mooc sur python")


# COUPE 7m10s

## Comment fait Python pour automatiquement passer l'instance à init
## comme premier argument. Lorsqu'on appelle la méthode directement
## depuis la classe, c'est une fonction classique à laquelle il faut
## passer deux arguments

Phrase.init

## Mais, lorsqu'on appelle une méthode sur une instance, Python va
## transformer cette fonction en une méthode bound. Ça veut dire que
## lors de l'appel, l'interpréteur va toujours appeler la même
## fonction init, mais il va automatiquement passer l'instance comme
## premier argument.

p.init

## donc

p.init("python")

## va être équivalent à 

Phrase.init(p, "python")

# 8m30

# -*- coding: utf-8 -*-

## reprenons la classe Phrase que vous avions dans une précédente vidéo

[[ditto - foo vs init]]
class Phrase:
    def init(self, ma_phrase):  #self est un nom de variable, ça n'est
                                #pas un mot clef
        self.ma_phrase = ma_phrase

## la première méthode spéciale que vous allons voir est la méthode
## __init__() qui est ce qu'on appelle l'initialisateur de
## l'instance. Cette méthode est automatiquement appellée après la
## création de l'instance pour l'initialiser. Lorsque l'on appelle une
## classe, on peut passer des arguments entre les paranthèses qui
## seront automatiquement passée à __init__(). Regardons cela


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase

p = Phrase("je fais un mooc sur python")

## l'attribut ma_phrase a bien été créé dans l'instance par
## l'initialisateur
vars(p)
print(p.ma_phrase)

## Notons qu'il arrive d'appeler __init__ le constructeur de la
## classe, mais c'est un terme impropre puisque techniquement
## l'objet instance est créé avant l'appel d'__init__.

# COUPE 2m00s

## Regardons maintenant d'autres méthodes spéciales
## courantes. Supposons que je veuille que ma classe phrase me
## permette de travailler sur les mots de la phrase. Il faut pour cela
## découper la phrase en mot. Si ensuite je veux connaitre le nombre
## de mots, j'aimerai simplement appeler len() sur mon
## instance. Regardons comment implémenter cela


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()  # new

    def __len__(self):                 # new
        return len(self.mots)          # new  (doit retourner un entier)
    
p = Phrase("je fais un mooc sur python")

len(p)

## COUPE 4m00

## Supposons maintenant que je veuille faire un test d'appartenance
## qui vérifie si un mot est dans la phrase, je peux implémenter cela
## avec __contains__


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):     # new (doit retourner un bool)
        return mot in self.mots      # new

[[TP: ce qui me gêne là dedans c'est que c'est mot pour mot l'exemple de w3-s8...; je trouve rétrospectivement que w3-s8 ça devrait plutôt parler méthode 'normale' plutôt que méthodes spéciales; je l'édite dans ce sens]]
    
p = Phrase("je fais un mooc sur python")

'python' in p

## COUPE 5m20s

## Pour finir, si je vais un print sur mon instance, je n'ai pas
## l'affichage des mots dans mon instance.

print(p)

## Je peux remédier à cela en implémentant la méthode spéciale
## __str__()


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):                             
        return mot in self.mots

    def __str__(self):               # new (doit retourner une str)
        return "\n".join(self.mots)  # new
    
p = Phrase("je fais un mooc sur python")

print(p)

# 6m30

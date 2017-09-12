# -*- coding: utf-8 -*-

## reprenons notre classe Phrase de la précédente vidéo, n'hésiter à
## mettre cette vidéo en pause pour retrouver ou taper le code de
## cette classe
    
class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):                             
        return mot in self.mots
    
    def __str__(self):               
        return "\n".join(self.mots)

## et ajoutons une méthode nb_lettres qui compte le nombre de lettre
## dans la phrase. 

    def nb_lettres(self):
        return len(self.ma_phrase)
    

## J'aimerais maintenant faire une nouvelle classe qui se comporte
## comme une classe Phrase, mais qui ne prend pas en compte la casse
## des mots dans le test d'appartenance. Faire une classe qui se
## comporte presque comme une autre classe, c'est exactement le but de
## l'héritage. Commençons à créer cette classe.

class PhraseSansCasse(Phrase):
    pass

## j'ai donc une classe PhraseSansCasse qui hérite de tous les attributs
## de la classe Phrase. L'héritage entre classes fonctionne comme
## l'héritage entre instance et classe. Lorsque je cherche un attribut
## dans l'espace de nommage de la classe, si je ne le trouve pas, je
## vais le chercher dans l'espace de nommage de sa super classe.

## Ça veut dire que si je crée une instance de
## PhraseSansCasse elle va être initialisée avec le __init__ de Phrase,
## ou si je fais un print sur cette instance, elle va utiliser la
## méthode __str__ de Phrase. 

p_no = PhraseSansCasse("nouvelle phrase")
## je peux vérifier que p_no est bien une instance de Phrase avec
## isinstance()

isinstance(p_no, Phrase)

print(p_no)

# 2m00s


## Évidemment cette classe PhraseSansCasse ne définissant aucun argument
## elle a exactement le même comportement que Phrase, elle n'apporte
## rien. Il faut donc ajouter ou surcharger des méthodes. La notion de
## surcharge est très importante.

## Comme la recherche d'attribut remonte le long de l'arbre
## d'héritage, si un attribut de même nom est défini à deux endroits
## dans l'arbre d'héritage, c'est le premièr (le plus bas dans
## l'arbre) qui sera utilisé. Le fait de définir un tel attribut en
## dessous d'un autre, dans une sous classe, s'appelle une surcharge.

## Commençons par surcharger la méthode __init__. Quand on surcharge
## une méthode, la méthode de la super classe n'est pas appelée. Si on
## veut tout même l'appeler, il faut le faire explicitement. C'est en
## général ce que l'on veut faire avec __init__

class PhraseSansCasse(Phrase):
    def __init__(self, ma_phrase):
        Phrase.__init__(self, ma_phrase)  # je commence par appeler
                                          # __init__ de Phrase
        self.mots_lower = set(m.lower()    
                              for m in self.mots)  # je crée un
                                                   # attribut
                                                   # mots_lower
                                                   
## et je surcharge __contains__ pour faire un test d'appartenance sans
## prendre en compte la casse
    def __contains__(self, mot):                             
        return mot.lower() in self.mots_lower


## et je peux évidemment créer une nouvelle méthode spécifique à cette
## classe
    def nb_upper(self):
        return len([m for m in self.mots if m.isupper()])

s = "je fais un MOOC sur Python"
p = Phrase(s)
p_no = PhraseSansCasse(s)
    
'mooc' in p
'mooc' in p_no
p_no.nb_upper()

#6m30s

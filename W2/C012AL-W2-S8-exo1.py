# -*- coding: iso-8859-15 -*-

## il existe deux manières totalement équivalentes de créer
## une chaîne de caractères. Soit on met la chaîne que l'on
## veut créer entre apostrophes ou entre guillemets

s1 = 'spam'
s2 = "spam"

print s1, s2

print s1 == s2

## l'intérêt d'avoir deux notations est que, si dans la
## chaîne on veut avoir un guillement ou une apostrophe,
## on peut l'écrire en utilisant l'autre notation pour
## ne pas avoit d'ambiguïté

s1 = "l'herbe"
s2 = 'un guillemet : "'

print s1, s2

## Il est possible d'écrire dans une chaîne de caractères
## des caractères spéciaux qui sont toujours précédés
## d'une barre oblique inversée que l'on appelle backslash

print '\' \" \\ \n spam'

## mais supposons que l'on ait une chaîne de caractères
## qui contienne beaucoup de backslash qui ne représente
## pas de caractères spéciaux. C'est le cas notamment
## des chemins des fichiers sous Windows.

nom = 'c:\temp\test\f.py'
print nom

## on a deux solutions à ce problèmes; soit on double
## tous les backslash, mais c'est fastidieux et sujet
## à erreur, soit on utilise une "raw string", c'est-à-dire
## une chaîne de caractères qui n'interprête plus aucun
## backslash comme caractère spécial.

nom = 'c:\\temp\\test\\f.py'
print nom

nom = r'c:\temp\test\f.py'
print nom

## il exite un dernier type de notation, en plus de l'apostrophe
## et du guillemet, pour créer une chaîne de caractères,
## c'est la triple apostrophe ou le triple guillemet.
## l'intéret de cette notation est que les retours chariots
## sont automatiquement transformé en \n. C'est très pratique
## pour écrire par exemple de l'aide ou de la documentation.

s = """
Usage : fft(n)
        calcule la fft de n
"""
s
print s

## comme les chaînes de caractères sont immuables, on ne peut
## pas les modifier en place, par contre, il existe de
## nombreuses fonctions qui retournent une nouvelle chaîne
## modifiée. Regardons quelques-unes des ces fonctions.

s = "le spam, c'est bon"
s = s.upper()
print s
s = s.lower()
print s
s = s.replace('spam', 'poulet')
print s

## il y a ensuite deux fonctions très importantes qui
## permettent de passer d'une chaîne de caractère à une liste
## et vice versa. Comme la liste est un type mutable 
## il est naturel pour travailler sur une chaîne de caractères
## de la transformer en liste. Regardons un example.

string = 'marc 35 175'
liste = string.split()
print liste
liste[1] += 'ans'  
liste[-1] += 'cm'  
print liste
string = '; '.join(liste)
print string
liste = string.split('; ')
print liste


# -*- coding: iso-8859-15 -*-

def multi_tri (listes):
    "trie toutes les sous-listes"
    for liste in listes:
        liste.sort()
    return listes

def multi_tri_reverse (listes, reverses):
    """tries toutes les sous listes, dans une direction
    precisee par le second argument"""
    for liste, reverse in zip(listes, reverses):
        liste.sort(reverse=reverse)
    return listes

def afficher_racines (p):
    "affiche les racines p-iemes de l'unite"
    for n in range(p):
        print "racine d'indice",n,"=", e**((2*pi*1j*n)/3)
        # ou pour la variante
        #print "valeur pour n=",n,n*(n+1)/2

def liste_racines (p):
    "retourne la liste des racines p-iemes de l'unite"
    resultat = []
    for n in range(p):
        resultat.append(e**((2*pi*1j*n)/3))
        # ou pour la variante
        #resultat.append(n*(n+1)/2)
    return resultat

def produit_scalaire (X,Y):
    """retourne le produit scalaire de deux listes de même taille"""
    # la dimension
    n = len(X)
    # initialisation du resultat
    scalaire = 0
    # on calcule la somme de tous les xi*yi
    for i in range (n):
        scalaire += X[i] * Y[i]
    # ne pas oublier
    return scalaire


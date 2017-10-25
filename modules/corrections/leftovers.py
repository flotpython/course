# -*- coding: utf-8 -*-
# from w2s7_for.py

### ####################
### # restes de l'itération 1 - trop abscons
### # @BEG@ week=2 sequence=7 name=liste_racines
### from math import e, pi
### 
### def liste_racines(p):
###     "retourne la liste des racines p-ièmes de l'unité"
###     # une simple compréhension fait l'affaire
###     # souvenez vous que 1j c'est notre 'i' complexe
###     return [e**((2j*pi*n)/p) for n in range(p)]
### 
### # Il est tout à fait possible aussi de construire les racines pas à pas
### # C'est un peu moins élégant mais ça fonctionne très bien aussi
### def liste_racines_bis(p):
###     "retourne la liste des racines p-ièmes de l'unité"
###     # on va construire le résultat petit à petit
###     # en partant d'une liste vide
###     resultat = []
###     # pour chaque n dans {0 .. p-1}
###     for n in range(p):
###         # on ajoute dans le résultat la racine d'ordre n
###         resultat.append(e**((2j*pi*n)/p))
###     # et on retourne le résultat
###     return resultat
### # @END@
### 
### inputs_liste_racines = [Args(2), Args(3), Args(4)] 
### 
### exo_liste_racines = ExerciceFunction(
###     liste_racines,
###     inputs_liste_racines,
###     layout_args=(18, 30, 30))



# from w2s8_strings

# left over from iteration 1

### # @BEG@ week=2 sequence=8 name=affichage
### # un élève a remarqué très justement que ce code ne fait pas
### # exactement ce qui est demandé, en ce sens qu'avec
### # l'entrée correspondant à Ted Mosby on obtient A:><
### # je préfère toutefois publier le code qui est en
### # service pour la correction en ligne, et vous laisse
### # le soin de l'améliorer si vous le souhaitez
### def affichage(s):
###     # pour ignorer les espaces et les tabulations 
###     # le plus simple est de les enlever
###     s=s.replace(' ', '').replace('\t','')
###     # la liste des mots séparés par une virgule 
###     # nous est donnée par un simple appel à split
###     mots = s.split(',')
###     # si on n'a même pas deux mots, on retourne None
###     if len(mots) < 2:
###         return None
###     # maintenant qu'on sait qu'on a deux mots
###     # on peut extraire le prénom et le nom
###     prenom = mots.pop(0)
###     nom = mots.pop(0)
###     # on veut afficher "??" si l'âge est inconnu
###     age = "??"
###     # mais si l'âge est précisé dans la ligne
###     if len(mots) >= 2:
###         # alors on le prend
###         age = mots.pop(1)
###     # il ne reste plus qu'à formater
###     return "N:>{}< P:>{}< A:>{}<".format(nom, prenom, age)
### # @END@
### 
### inputs_affichage = [
###     Args("Joseph, Dupont"),
###     Args("Jules , Durand, G123, 21"),
###     Args("Jean"), 
###     Args("Ted, Mosby, F321, "),
###     Args(" Jacques , Martin, L119, \t24 ,"),
###     Args("Sheldon, Cooper ,"),
###     Args("\t Sam, Does\t, F321, 23"),
### ]
### 
### exo_affichage = ExerciceFunction(
###     affichage, inputs_affichage,
###     layout_args=(40, 40, 40),
###     exemple_how_many=4)


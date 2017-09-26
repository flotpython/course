# -*- autofill-mode:true; fill-column: 40 -*-

La dernière fois nous avons vu comment utiliser python, ipython et IDLE sur votre ordinateur.
 
Aujourd'hui je vais vous montrer rapidement comment utiliser les
notebooks. Alors tout d'abord, par rapport à ce qu'on a vu la dernière
fois, j'insiste bien sur le fait que tout ce que nous allons faire
aujourd'hui utilise des ressources python qui sont distantes,
c'est-à-dire hébergées dans la plateforme fun. 

**Vous pouvez utiliser
tout ceci même si vous n'avez pas encore installé python sur votre
ordinateur. Vous pourriez par exemple utiliser une tablette.**

> ouvrir chrome 

Nous allons d'abord parcourir ensemble le complément de cette vidéo, pour
voir les mécanismes de base, et ensuite je vous montrerai un exercice,
pour vous montrer comment vous pouvez faire votre propre correction.

Si je prends le premier notebook

Vous pouvez d'abord voir que le document est découpé en cellules. Si
je clique ici, je sélectionne la première cellule.

Vous pouvez passer d'une cellule à l'autre en utilisant **cette petite
flêche** ici; 

> descendre jusqu'à **Shift Enter**

Pour ceux qui comme moi sont plus clavier que souris, vous pouvez
utiliser le raccourci **Majuscule-Entrée**, qui fait la même chose. 

Tant que vous êtes dans une cellule de texte on a l'impression qu'on ne
fait qu'avancer dans le document, mais sur une cellule de code comme
ici

> s'arrêter sur la première expression

quand j'avance vous voyez qu'il se passe quelque chose de plus, le
fragment de code se fait évaluer et le browser me **montre le résultat**.

Remarquez la ligne Out[] qui nous donne le résultat, c'est un peu
comme avec l'interpréteur interactif qu'on a vu la dernière fois.

Ce code, vous pouvez le modifier 

> descendre et s'arrêter sur la cellule avec la **racine carrée**

```
sqrt(25)
``` 

Montrer qu'il faut **remonter**, modifier le code, et refaire le triangle ou shift-enter]]

> remontrer le champ *Out*

Vous n'êtes pas obligés d'exécuter les cellules de code dans l'ordre,
mais faites attention quand même; pour vous y retrouver  on vous
montre dans la bulle "Out" l'ordre des évaluations 

> montrer que ça s'incrémente

Vous pouvez repartir d'un interpréteur vierge (donc comme quand on
fait F5 sous IDLE) avec le menu ***Kernel -> Restart*** 

------------
Une chose importante: votre notebook naturellement est une
**copie** de celui rédigé par les enseignants (une copie qui est faite au niveau
du serveur web, pas sur votre machine évidemment, vous avez bien
compris que toute cette mécanique fonctionne intégralement sur le
serveur, et n'utilise pas votre installation python à vous) 

Si par hasard vous défigurez votre notebook vous pouvez revenir à
cette version 'enseignants' avec le menu ***File -> Reset to Origin***

------------
Je vous signale aussi la possibilité de télécharger le contenu du
notebook au format python, ***File -> Download as -> python***

------
Et aussi, qui peut être pratique pour échanger entre vous, la
possibilité de créer un snapshot en lecture seule ***File -> Share
static version***;
vous obtenez comme ça une adresse URL que vous
pouvez poster sur le forum pour que d'autres puissent lire votre code.

-------------
Je vous montre à présent rapidement un des tous premiers exercices.

Passer à l'exercice exo-if

La mécanique est très simple, vous lisez l'énoncé, vous écrivez votre
code, vous l'évaluez, et vous pouvez ensuite utiliser une cellule en
dessous pour vérifier votre code

> Remplir avec du code faux

Montrer comment se présente le résultat

> corriger et mettre du code juste

recommencer

---

J'espère que cette rapide présentation vous clarifie les idées
concernant l'utilisation des notebooks, que nous allons massivement
utiliser dans ce cours.

À bientôt

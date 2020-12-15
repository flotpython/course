---
jupytext:
  cell_metadata_filter: all
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: 'exercice: nombres premiers'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Exercice - niveau avancé

+++

## itérateurs et générateurs

**Tous les exercices** de ce notebook vous demandent d'écrire
des fonctions qui **construisent des itérateurs**.

```{code-cell}
import itertools
```

## 1. Nombres premiers

+++

On vous demande d'écrire un générateur qui énumère les nombres premiers.

Naturellement il existe de nombreuses biliothèques pour cela, mais on vous demande ici d'écrire votre propre algorithme, même s'il est naïf.

```{code-cell}
from corrections.gen_primes import exo_primes
exo_primes.example()
```

Le générateur ne s'arrête donc jamais, c'est un générateur infini comme `itertools.count()`. 
Le système de correction automatique est capable d'extraire certaines parties du flux du générateur, avec une convention voisine de `range()` et/ou du *slicing*.

Ainsi par exemple le deuxième jeu de test, sous-titré `1 → 5 / 2`, va retenir les éléments énumérés par le générateur aux itérations *1, 3 et 5* - en commençant bien sûr à compter à 0.

+++

**NOTES**

* Évidemment, il vous faut retourner un itérateur, et la correction automatique vérifiera ce point.
* Notez aussi que, lorsqu'on cherche à déterminer si $n$ est entier, on a nécessairement déjà fait ce travail sur tous les entiers plus petits que $n$. Il est donc tentant, et fortement recommandé, de profiter de cette information pour accélérer l'algorithme.
* Si votre algorithme est très lent ou faux, vous pouvez *perdre* le *kernel* (en français noyau), c'est-à-dire qu'il calcule pendant très longtemps (ou pour toujours) ; dans ces cas-là, la marge gauche indique `In [*]:` et l'étoile n'est jamais remplacée par un chiffre.
  Il vous **faut alors interrompre** votre kernel ; pour cela utilisez le menu *Kernel* qui a des options pour interrompre ou redémarrer le kernel courant ; les raccourcis clavier `i i` et `0 0` permettent aussi d'interrompre et redémarrer le noyau.

```{code-cell}
# à vous de jouer

def primes():
    # vous DEVEZ retourner un itérateur
    # bien sûr count() n'est pas une bonne réponse...
    return itertools.count()
```

```{code-cell}
# pour corriger votre code
exo_primes.correction(primes)
```

##### zone de debug

```{code-cell}
# à toutes fins utiles

MAX = 10

iterator = primes()

for index, prime in enumerate(itertools.islice(iterator, MAX)):
    print(f"{index} -> {prime}")
```

***
***
***

+++

## 2. Les carrés des nombres premiers

+++

On veut à présent énumérer les carrés des nombres premiers

**NOTE** il y a au moins deux façons triviales de parvenir au résultat.

```{code-cell}
from corrections.gen_primes import exo_prime_squares
exo_prime_squares.example() 
```

```{code-cell}
# à vous

def prime_squares():
    ...
```

```{code-cell}
exo_prime_squares.correction(prime_squares)
```

***
***
***

+++

## 3. Combinaisons d'itérateurs

+++

On vous demande d'écrire un itérateur qui énumère des couples :

* en première position, on veut trouver les nombres premiers, mais avec un décalage :  
  les **cinq premiers tuples** contiennent `1`, puis le sixième contient 2, et à partir de là les nombres premiers ;
* en deuxième position, les carrés des nombres premiers, sans décalage :

+++

**NOTE**  
Il peut être tentant de créer deux instances de l'itérateur `primes()` ; toutefois c'est cet objet qui demande le plus de temps de calcul, aussi on vous suggère de réfléchir, en option, à une solution qui ne crée qu'un seul exemplaire de cet itérateur.

```{code-cell}
from corrections.gen_primes import exo_prime_legos
exo_prime_legos.example()
```

```{code-cell}
# à vous de jouer

def prime_legos():
    ...
```

```{code-cell}
exo_prime_legos.correction(prime_legos)
```

***
***
***

+++

## 4. Les $n$-ièmes nombres premiers, avec $n$ premier

+++

On vous demande d'implémenter un itérateur qui renvoie les $n$-ièmes nombres premiers, mais seulement pour $n$ premier.

Ainsi comme `primes()` retourne la suite 

| indice | premier |
|--------|---------|
| 0 | 2 |
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |
| 4 | 11|
| 5 | 13|
| 6 | 17|
| 7 | 19|

on veut que `prime_th_primes` retourne la suite

| indice | premier |
|--------|---------|
| 0 | 5 |
| 1 | 7 |
| 2 | 13|
| 3 | 19|

```{code-cell}
# ce qui est illustré sur cet exemple calculé, qui va un peu plus loin

from corrections.gen_primes import exo_prime_th_primes
exo_prime_th_primes.example()
```

```{code-cell}
# À vous de jouer

def prime_th_primes():
    # souvenez-vous que vous devez retourner un itérateur
    return itertools.count()
```

```{code-cell}
# pour corriger votre code
exo_prime_th_primes.correction(prime_th_primes)
```

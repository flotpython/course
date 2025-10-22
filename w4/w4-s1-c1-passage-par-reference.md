---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
nbhosting:
  title: "Passage par r\xE9f\xE9rence"
---

# Passage d'arguments par référence

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

Entre le code qui appelle une fonction et le code de la fonction elle-même

```{code-cell} ipython3
def ma_fonction(dans_fonction):
    print(dans_fonction)
    
dans_appelant = ["texte"]
ma_fonction(dans_appelant)
```

on peut se demander quelle est exactement la nature de la relation entre l'appelant et l'appelé, c'est-à-dire ici `dans_appelant` et `dans_fonction`. 

C'est l'objet de ce complément.

+++

### Passage par valeur - passage par référence

+++

Si vous avez appris d'autres langages de programmation comme C ou C++, on a pu vous parler de deux modes de passage de paramètres :

 * par valeur : cela signifie qu'on communique à la fonction, non pas l'entité dans l'appelant, mais seulement **sa valeur** ; en clair, **une copie** ;
 * par référence : cela signifie qu'on passe à la fonction une **référence** à l'argument dans l'appelant, donc essentiellement les deux codes **partagent** la même mémoire.

+++

### Python fait du passage par référence

+++

Certains langages comme Pascal - et C++ si on veut - proposent ces deux modes. En Python, tous les passages de paramètres se font **par référence**.

```{code-cell} ipython3
# chargeons la magie pour pythontutor
%load_ext ipythontutor
```

```{code-cell} ipython3
%%ipythontutor curInstr=4
def ma_fonction(dans_fonction):
    print(dans_fonction)
    
dans_appelant = ["texte"]
ma_fonction(dans_appelant)
```

Ce qui signifie qu'on peut voir le code ci-dessus comme étant - pour simplifier - équivalent à ceci :

```{code-cell} ipython3
dans_appelant = ["texte"]

# ma_fonction (dans_appelant)
# → on entre dans la fonction
dans_fonction = dans_appelant
print(dans_fonction)
```

On peut le voir encore d'une autre façon en instrumentant le code comme ceci -- on rappelle que la fonction built-in `id` retourne l'adresse mémoire d'un objet :

```{code-cell} ipython3
def ma_fonction(dans_fonction):
    print('dans ma_fonction', dans_fonction , id(dans_fonction))
    
dans_appelant = ["texte"]
print('dans appelant   ', dans_appelant, id(dans_appelant))
ma_fonction(dans_appelant)
```

### Des références partagées

+++

On voit donc que l'appel de fonction crée des références partagées, exactement comme l'affectation, et que tout ce que nous avons vu au sujet des références partagées s'applique exactement à l'identique :

```{code-cell} ipython3
# on ne peut pas modifier un immuable dans une fonction
def increment(n):
    n += 1

compteur = 10
increment(compteur)
print(compteur)
```

```{code-cell} ipython3
# on peut par contre ajouter dans une liste
def insert(liste, valeur):
    liste.append(valeur)
    
liste = ["un"]
insert(liste, "texte")
print(liste)
```

Pour cette raison, il est important de bien préciser, quand vous documentez une fonction, si elle fait des effets de bord sur ses arguments (c'est-à-dire qu'elle modifie ses arguments), ou si elle produit une copie. Rappelez-vous par exemple le cas de la méthode `sort` sur les listes, et de la fonction de commodité `sorted`, que nous avions vues en semaine 2.

De cette façon, on saura s'il faut ou non copier l'argument avant de le passer à votre fonction.

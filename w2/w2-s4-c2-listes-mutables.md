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
  title: Mutables / immuables
---

# Objets mutables et objets immuables

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### Les chaînes sont des objets immuables

+++

Voici un exemple d'un fragment de code qui illustre le caractère immuable des chaînes de caractères. Nous l'exécutons sous [pythontutor](pythontutor.com), afin de bien illustrer les relations entre variables et objets.

```{code-cell} ipython3
# il vous faut charger cette cellule
# pour pouvoir utiliser les suivantes
%load_ext ipythontutor
```

**Note** : une fois que vous avez évalué la cellule avec `%%ipythontutor`, vous devez cliquer sur le bouton `Next` pour voir pas à pas le comportement du programme.

+++

Le scénario est très simple, on crée deux variables `s1` et `s2` vers le même objet `'abc'`, puis on fait une opération `+=` sur la variable `s1`.

Comme l'objet est une chaîne, il est donc immuable, on ne **peut pas modifier l'objet** directement ; pour obtenir l'effet recherché (à savoir que `s1` s'allonge de `'def'`), Python **crée un deuxième objet**, comme on le voit bien sous pythontutor :

```{code-cell} ipython3
%%ipythontutor heapPrimitives=true
# deux variables vers le même objet
s1 = 'abc'
s2 = s1
# on essaie de modifier l'objet
s1 += 'def'
# pensez à cliquer sur `Next`
```

```{code-cell} ipython3
# à se stade avec des chaines on observe
s1 = 'abc'
s2 = s1
s1 += 'def'
print(s1)
print(s2)
```

### Les listes sont des objets mutables

+++

Voici ce qu'on obtient par contraste pour le même scénario mais qui cette fois utilise des listes, qui sont des objets mutables :

```{code-cell} ipython3
%%ipythontutor heapPrimitives=true ratio=0.8
# deux variables vers le même objet
liste1 = ['a', 'b', 'c']
liste2 = liste1
# on modifie l'objet
liste1 += ['d', 'e', 'f']
# pensez à cliquer sur `Next`
```

```{code-cell} ipython3
# alors qu'avec les listes on observe
liste1 = ['a', 'b', 'c']
liste2 = liste1
# on modifie l'objet
liste1 += ['d', 'e', 'f']
print(liste1)
print(liste2)
```

### Conclusion

+++

Ce comportement n'est pas propre à l'usage de l'opérateur `+=`, les objets mutables et immuables ont par essence un comportement différent, il est très important d'avoir ceci présent à l'esprit.

Nous aurons notamment l'occasion d'approfondir cela dans la séquence consacrée aux références partagées, en semaine 3.

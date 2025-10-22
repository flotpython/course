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
  title: break et continue
---

# Les instructions `break` et `continue`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### `break` et `continue`

+++

En guise de rappel de ces deux notions que nous avons déjà rencontrées dans la séquence consacrée aux boucles `while` la semaine passée, python propose deux instructions très pratiques permettant de contrôler l'exécution à l'intérieur des boucles de répétition, et ceci s'applique indifféremment aux boucles `for` ou `while` :

 * `continue` : pour abandonner l'itération courante, et passer à la suivante, en **restant dans la boucle** ;
 * `break` : pour abandonner **complètement** la boucle.
 
Voici un exemple simple d'utilisation de ces deux instructions :

```{code-cell} ipython3
for entier in range(1000):
    # on ignore les nombres non multiples de 10
    if entier % 10 != 0:
        continue
    print(f"on traite l'entier {entier}")
    # on s'arrête à 50
    if entier >= 50:
        break
print("on est sorti de la boucle")
```

Pour aller plus loin, vous pouvez lire [cette documentation](https://docs.python.org/3/tutorial/controlflow.html?highlight=break#break-and-continue-statements-and-else-clauses-on-loops).

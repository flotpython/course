---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
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
  title: "Puissance enti\xE8re"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Mise à la puissance

+++

## Exercice - niveau intermédiaire

On vous demande d'écrire une fonction qui met un objet x à la puissance entière n.

Le paramètre `x` doit pouvoir être multiplié par lui même, et le paramètre `n` est un entier `>=1` (pas la peine de vérifier).

+++

Naturellement on s'interdit d'utiliser l'opérateur prédéfini `**`; notamment notre algorithme doit pouvoir s'appliquer à tous les types d'objet qui supportent la multiplication.

Pour optimiser les calculs, on va utiliser un algorithme qui permet d'effectuer un nombre de multiplications en $O(log_2(n))$. 

Pour cela remarquez par exemple que le fait de mettre un nombre au carré nécessite seulement une multiplication ;  

Ce qui signifie que la décomposition de n en binaire donne une formule pour $x^n$ qui met en jeu de l'ordre de $2*log_2{n}$ multiplications.

Ainsi par exemple :

* si n = 21, c'est-à-dire en base 2 `010101`, alors

$ n = 2 * 2 * (2*2 + 1) + 1 $  

$ x^{21} = (((x.x)^2*x)^2)^2 . x $ soit 6 multiplications


* si n = 42, c'est-à-dire en base 2 `101010`, alors

$ n = 2 * (2 * 2 * (2*2 + 1) + 1) $  

$ x^{42} = ((((x.x)^2*x)^2)^2 . x)^2$ soit 7 multiplications

```{code-cell} ipython3
from corrections.exo_power import exo_power
exo_power.example()
```

**Commentaires**

* on rappelle que `1j` désigne le nombre complexe $i$ ;
* le jeu de données de test contient des objets (la classe `Number`) pour lesquels l'opérateur `**` ne fonctionne pas ;
* le système de correction automatique n'est pas en mesure de vérifier la complexité de votre algorithme, mais sachez que les données de test mettent en jeu des exposants jusqu'à $2^{128}$ ;

**Indice**

* on peut être tenté d'écrire une boucle `while` sur la variable $n$, mais pour commencer une formulation récursive est une approche qui peut sembler beaucoup plus commode à implémenter.

```{code-cell} ipython3
# à vous de jouer
def power(x, n):
    "<votre code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_power.correction(power)
```

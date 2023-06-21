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
  title: "Flottants extr\xEAmes"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Estimer le plus petit (grand) flottant

+++

## Exercice - niveau basique

+++

### Le plus petit flottant

+++

En corollaire de la discussion sur la précision des flottants, il faut savoir que le système de codage en mémoire impose aussi une limite. Les réels très petits, ou très grands, ne peuvent plus être représentés de cette manière.

C'est notamment très gênant si vous implémentez un logiciel probabiliste, comme des graphes de Markov, où les probabilités d'occurrence de séquences très longues tendent très rapidement vers des valeurs extrêmement petites.

+++

Le but de cet exercice est d'estimer la valeur du plus petit flottant qui peut être représenté comme un flottant. Pour vous aider, voici deux valeurs :

```{code-cell} ipython3
10**-320
```

```{code-cell} ipython3
10**-330
```

Comme on le voit, $10^{-320}$ est correctement imprimé, alors que $10^{-330}$ est, de manière erronée, rapporté comme étant nul.

+++

**Notes :**

* À ce stade du cours, pour estimer le plus petit flottant, procédez simplement par approximations successives.

* Sans utiliser de boucle, la précision que vous pourrez obtenir n'est que fonction de votre patience, ne dépassez pas 4 à 5 itérations successives :)

* Il est par contre pertinent d'utiliser une approche rationnelle pour déterminer l'itération suivante (par opposition à une approche "au petit bonheur"). Pour ceux qui ne connaissent pas, nous vous recommandons de vous documenter sur l'algorithme de [**dichotomie**](https://fr.wikipedia.org/wiki/Recherche_dichotomique).

```{code-cell} ipython3
10**-325
```

Voici quelques cellules de code vides ; vous pouvez en créer d'autres si nécessaire, le plus simple étant de taper `Alt+Enter`, ou d'utiliser le menu _"Insert -> Insert Cell Below"_

```{code-cell} ipython3
# vos essais successifs ici
```

```{code-cell} ipython3
.24*10**-323
```

### Le plus grand flottant

+++

La même limitation s'applique sur les grands nombres. Toutefois, cela est un peu moins évident, car comme toujours il faut faire attention aux types :

```{code-cell} ipython3
10**450
```

Ce qui passe très bien car j'ai utilisé un `int` pour l'exposant. Dans ce premier cas Python calcule le résultat comme un `int`, qui est un type qui n'a pas de limitation de précision (Python utilise intelligemment autant de bits que nécessaire pour ce genre de calculs).

Par contre, si j'essaie de faire le même calcul avec un exposant flottant, Python essaie cette fois de faire son calcul avec un flottant, et là on obtient une erreur :

```{code-cell} ipython3
:latex:skip-eval: true

10**450.0
```

On peut d'ailleurs remarquer que le comportement ici n'est pas extrêmement cohérent, car avec les petits nombres Python nous a silencieusement transformé $10^{-330}$ en $0$, alors que pour les grands nombres, il lève une exception (nous verrons les exceptions plus tard, mais vous pouvez dès maintenant remarquer que le comportement est différent dans les deux cas).

+++

Quoi qu'il en soit, la limite pour les grands nombres se situe entre les deux valeurs $10^{300}$ et $10^{310}$. On vous demande à nouveau d'estimer comme ci-dessus une valeur approchée du plus grand nombre qu'il soit possible de représenter comme un flottant.

```{code-cell} ipython3
10**300.
```

```{code-cell} ipython3
:latex:skip-eval: true

10**310.
```

```{code-cell} ipython3
# vos essais successifs ici
```

## Complément - niveau avancé

+++

En fait, on peut accéder à ces valeurs minimales et maximales pour les flottants comme ceci

```{code-cell} ipython3
import sys
print(sys.float_info)
```

Et notamment, [comme expliqué ici](https://docs.python.org/3/library/sys.html#sys.float_info).

```{code-cell} ipython3
print("Flottant minimum", sys.float_info.min)
print("Flottant maximum", sys.float_info.max)
```

**Sauf que** vous devez avoir trouvé un maximum voisin de cette valeur, mais le minimum observé expérimentalement ne correspond pas bien à cette valeur.

Pour ceux que cela intéresse, l'explication à cette apparente contradiction réside dans l'utilisation de [nombres dénormaux](http://en.wikipedia.org/wiki/Denormal%5Fnumber).

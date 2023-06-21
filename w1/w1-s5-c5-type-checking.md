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
  title: type-checking
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Typages statique et dynamique

+++

## Complément - niveau intermédiaire

+++

Parmi les langages typés, on distingue les langages à typage statique et ceux à typage dynamique. Ce notebook tente d'éclaircir ces notions pour ceux qui n'y sont pas familiers.

+++

### Typage statique

+++

À une extrémité du spectre, on trouve les langages compilés, dits à typage statique, comme par exemple C ou C++.

En C on écrira, par exemple, une version simpliste de la fonction factoriel comme ceci :

+++

```C
int factoriel(int n) {
    int result = 1;
    for (int loop = 1; loop <= n; loop++)
        result *= loop;
    return result;
}
```

+++

Comme vous pouvez le voir - ou le deviner - toutes les **variables** utilisées ici (comme par exemple `n`, `result` et `loop`) sont typées :

* on doit appeler `factoriel` avec un argument `n` qui doit être un entier (`int` est le nom du type entier) ;
* les variables internes `result` et `loop` sont de type entier ;
* `factoriel` retourne une valeur de type entier.

+++

Ces informations de type ont essentiellement trois fonctions :

* en premier lieu, elles sont nécessaires au compilateur. En C si le programmeur ne précisait pas que `result` est de type entier, le compilateur n'aurait pas suffisamment d'éléments pour générer le code assembleur correspondant ;
* en contrepartie, le programmeur a un contrôle très fin de l'usage qu'il fait de la mémoire et du matériel. Il peut choisir d'utiliser un entier sur 32 ou 64 bits, signé ou pas, ou construire avec `struct` et `union` un arrangement de ses données ;
* enfin, et surtout, ces informations de type permettent de faire un contrôle *a priori* de la validité du programme, par exemple, si à un autre endroit dans le code on trouve :

+++

```C
#include <stdio.h>

int main(int argc, char *argv[]) {
    /* le premier argument de la ligne de commande est argv[1] */
    char *input = argv[1];
    /* calculer son factoriel et afficher le résultat */
    printf("Factoriel (%s) = %d\n", input, factoriel(input));
    /*                                               ^^^^^

     * ici on appelle factoriel avec une entrée de type 'chaîne de caractères' */
}
```

+++

alors le compilateur va remarquer qu'on essaie d'appeler `factoriel` avec comme argument `input` qui, pour faire simple, est une chaîne de caractères et comme `factoriel` s'attend à recevoir un entier, ce programme n'a aucune chance de compiler.

On parle alors de **typage statique**, en ce sens que chaque **variable** a exactement un type qui est défini par le programmeur une bonne fois pour toutes.

+++

C'est ce qu'on appelle le **contrôle de type**, ou *type-checking* en anglais. Si on ignore le point sur le contrôle fin de la mémoire, qui n'est pas crucial à notre sujet, ce modèle de contrôle de type présente&nbsp;:

* l'**inconvénient** de demander davantage au programmeur (je fais abstraction, à ce stade et pour simplifier, de [langages à inférence de types](https://en.wikipedia.org/wiki/Type_inference) comme ML et Haskell) ;
* et l'**avantage** de permettre un contrôle étendu, et surtout précoce (avant même de l'exécuter), de la bonne correction du programme.

+++

Cela étant dit, le typage statique en C n'empêche pas le programmeur débutant d'essayer d'écrire dans la mémoire à partir d'un pointeur `NULL` - et le programme de s'interrompre brutalement. Il faut être conscient des limites du typage statique.

+++

### Typage dynamique

+++

À l'autre bout du spectre, on trouve des langages comme, eh bien, Python.

+++

Pour comprendre cette notion de typage dynamique, regardons la fonction suivante `somme`.

```{code-cell} ipython3
def somme(*largs):
    "retourne la somme de tous ses arguments"
    if not largs:
        return 0
    result = largs[0]
    for i in range(1, len(largs)):
        result += largs[i]
    return result
```

Naturellement, vous n'êtes pas à ce stade en mesure de comprendre le fonctionnement intime de la fonction. Mais vous pouvez tout de même l'utiliser :

```{code-cell} ipython3
somme(12, 14, 300)
```

```{code-cell} ipython3
liste1 = ['a', 'b', 'c']
liste2 = [0, 20, 30]
liste3 = ['spam', 'eggs']
somme(liste1, liste2, liste3)
```

Vous pouvez donc constater que `somme` peut fonctionner avec des objets de types
différents: on peut lui passer des nombres, ou lui passer des listes. En fait,
telle qu'elle est écrite, elle va fonctionner s'il est possible de faire `+`
entre ses arguments. Ainsi, par exemple, on pourrait même faire :

```{code-cell} ipython3
# Python sait faire + entre deux chaînes de caractères
somme('abc', 'def')
```

Mais par contre on ne pourrait pas faire

```{code-cell} ipython3
:latex:hidden-code-instead: "try:\n    somme(12, [1, 2, 3])\nexcept:\n    print('OOPS')"

# ceci va déclencher une exception à l'exécution
somme(12, [1, 2, 3])
```

Il est utile de remarquer que le typage de Python, qui existe bel et bien comme on le verra, est qualifié de dynamique parce que le type est attaché **à un objet** et non à la variable qui le référence. On aura bien entendu l'occasion d'approfondir tout ça dans le cours.

+++

En Python, on fait souvent référence au typage sous l'appellation *duck typing*, de manière imagée :

> If it looks like a duck and quacks like a duck, it's a duck.

+++

On voit qu'on se trouve dans une situation très différente de celle du programmeur C/C++, en ce sens que&nbsp;:

* à l'écriture du programme, il n'y aucun des surcoûts qu'on trouve avec C ou C++ en matière de définition de type ;
* aucun contrôle de type n'est effectué *a priori* par le langage au moment de la définition de la fonction `somme` ;
* par contre au moment de l'exécution, s'il s'avère qu'on tente de faire une somme entre deux types qui ne peuvent pas être additionnés, comme ci-dessus avec un entier et une liste, le programme ne pourra pas se dérouler correctement.

+++

Il y a deux points de vue vis-à-vis de la question du typage.

Les gens habitués au *typage statique* se plaignent du typage dynamique en disant qu'on peut écrire des programmes faux et qu'on s'en rend compte trop tard - à l'exécution.

À l'inverse les gens habitués au *typage dynamique* font valoir que le typage statique est très partiel, par exemple, en C si on essaie d'écrire dans un pointeur `NULL`, le système d'exploitation ne le permet pas et le programme sort tout aussi brutalement.

+++

Bref, selon le point de vue, le typage dynamique est vécu comme un inconvénient (pas assez de bonnes propriétés détectées par le langage) ou comme un avantage (pas besoin de passer du temps à déclarer le type des variables, ni à faire des conversions pour satisfaire le compilateur). 

Vous remarquerez cependant à l'usage, qu'en matière de vitesse de développement, les inconvénients du typage dynamique sont très largement compensés par ses avantages.

+++

### *Type hints*

+++

Signalons enfin que depuis python-3.5, il est **possible** d'ajouter des annotations de type, pour expliciter les suppositions qui sont faites par le programmeur pour le bon fonctionnement du code.

Nous aurons là encore l'occasion de détailler ce point dans le cours, signalons simplement que ces annotations sont totalement optionnelles, et que même lorsqu'elles sont présentes elles ne sont pas utilisées à l'exécution par l'interpréteur. L'idée est plutôt de permettre à des outils externes, [comme  par exemple `mypy`](http://www.mypy-lang.org), d'effectuer des contrôles plus poussés concernant la correction du programme.

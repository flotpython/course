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
  title: "Fichiers syst\xE8mes"
---

# Fichiers systèmes

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau avancé

+++

Dans ce complément, nous allons voir comment un programme Python interagit avec ce qu'il est convenu d'appeler le système d'entrées-sorties standard du système d'exploitation.

+++

### Introduction

+++

Dans un ordinateur, le système d'exploitation (Windows, Linux, macOS, etc.) comprend un noyau (*kernel*) qui est un logiciel qui a l'exclusivité  pour interagir physiquement avec le matériel (processeur(s), mémoire, disque(s), périphériques, etc.) ; il offre aux programmes utilisateur (*userspace*) des abstractions pour interagir avec ce matériel.

La notion de fichier, telle qu'on l'a vue dans la vidéo, correspond à une de ces abstractions ; elle repose principalement sur les quatre opérations élémentaires suivantes :

 * `open` ;
 * `close` ;
 * `read` ;
 * `write`.

+++

Parmi les autres conventions d'interaction entre le système (pour être précis : le [*shell*](http://fr.wikipedia.org/wiki/Interface_système)) et une application, il y a les notions de :

 * entrée standard (*standard input*, en abrégé `stdin`) ;
 * sortie standard (*standard output*, en abrégé `stdout`) ;
 * erreur standard (*standard error*, en abrégé `stderr`).

Ceci est principalement pertinent dans le contexte d'un terminal. L'idée c'est que l'on a envie de pouvoir [*rediriger* les entrées-sorties](http://en.wikipedia.org/wiki/Redirection_%28computing%29) d'un programme sans avoir à le modifier. De la sorte, on peut également *chaîner* des traitements [à l'aide de *pipes*](http://en.wikipedia.org/wiki/Redirection_%28computing%29#Piping), sans avoir besoin de sauver les résultats intermédiaires sur disque.

+++

Ainsi par exemple lorsque l'on écrit :

```bash
$ monprogramme < fichier_entree > fichier_sortie
```

Les deux fichiers en question sont ouverts par le *shell*, et passés à `monprogramme` - que celui-ci soit écrit en C, en Python ou en Java - sous la forme des fichiers `stdin` et `stdout` respectivement, et donc **déjà ouverts**.

+++

### Le module `sys`

+++

L'interpréteur Python vous expose ces trois fichiers sous la forme d'attributs du module `sys` :

```{code-cell} ipython3
import sys
for channel in (sys.stdin, sys.stdout, sys.stderr):
    print(channel)
```

Dans le contexte du notebook vous pouvez constater que les deux flux de sortie sont implémentés comme des classes spécifiques à IPython. Si vous exécutez ce code localement dans votre ordinateur vous allez sans doute obtenir quelque chose comme :

```python
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
```

+++

On n'a pas extrêmement souvent besoin d'utiliser ces variables en règle générale, mais elles peuvent s'avérer utiles dans des contextes spécifiques.

Par exemple, l'instruction `print` écrit dans `sys.stdout` (c'est-à-dire la sortie standard). Et comme `sys.stdout` est une variable (plus exactement `stdout` est un attribut dans le module référencé par la variable `sys`) et qu'elle référence un objet fichier, on peut lui faire référencer un autre objet fichier et ainsi rediriger depuis notre programme toutes les sorties, qui sinon iraient sur le terminal, vers un fichier de notre choix :

```{code-cell} ipython3
# ici je fais exprès de ne pas utiliser un `with`
# car très souvent les deux redirections apparaissent
# dans des fonctions différentes
import sys
# on ouvre le fichier destination
autre_stdout = open('ma_sortie.txt', 'w', encoding='utf-8')
# on garde un lien vers le fichier sortie standard
# pour le réinstaller plus tard si besoin.
tmp = sys.stdout
print('sur le terminal')

# première redirection
sys.stdout = autre_stdout
print('dans le fichier')

# on remet comme c'était au début
sys.stdout = tmp
# et alors pour être propre on n'oublie pas de fermer
autre_stdout.close()
print('de nouveau sur le terminal')
```

```{code-cell} ipython3
# et en effet, dans le fichier on a bien
with open("ma_sortie.txt", encoding='utf-8') as check:
    print(check.read())
```

---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: Exos regexps
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Expressions régulières

+++

Nous vous proposons dans ce notebook quelques exercices sur les expressions régulières. Faisons quelques remarques avant de commencer :

* nous nous concentrons sur l'écriture de l'expression régulière en elle-même, et pas sur l'utilisation de la bibliothèque ;
* en particulier, tous les exercices font appel à `re.match` entre votre *regexp* et une liste de chaînes d'entrée qui servent de jeux de test.

+++

##### Liens utiles

+++

Pour travailler sur ces exercices, il pourra être profitable d'avoir sous la main :

* la [documentation officielle](https://docs.python.org/3/library/re.html#regular-expression-syntax) ;
* et <https://regex101.com/> (par exemple) qui permet de mettre au point de manière interactive, et donc d'avoir un retour presque immédiat, pour accélérer la mise au point.

+++

## Exercice - niveau intermédiaire (1)

+++

##### Identificateurs Python

On vous demande d'écrire une expression régulière qui décrit les noms de variable en Python. Pour cet exercice on se concentre sur les caractères ASCII. On exclut donc les noms de variables qui pourraient contenir des caractères exotiques comme les caractères accentués ou autres lettres grecques.

Il s'agit donc de reconnaître toutes les chaînes qui commencent par une lettre ou un `_`, suivi de lettres, chiffres ou `_`.

```{code-cell} ipython3
# quelques exemples de résultat attendus
from corrections.regexp_pythonid import exo_pythonid
exo_pythonid.example()
```

```{code-cell} ipython3
# à vous de jouer: écrivez ici
# sous forme de chaîne votre expression régulière

regexp_pythonid = r"votre_regexp"
```

```{code-cell} ipython3
# évaluez cette cellule pour valider votre code
exo_pythonid.correction(regexp_pythonid)
```

## Exercice - niveau intermédiaire (2)

+++

##### Lignes avec nom et prénom

On veut reconnaître dans un fichier toutes les lignes qui contiennent un nom et un prénom.

```{code-cell} ipython3
from corrections.regexp_agenda import exo_agenda
exo_agenda.example()
```

Plus précisément, on cherche les chaînes qui :

* commencent par une suite - possiblement vide - de caractères alphanumériques (vous pouvez utiliser `\w`) ou tiret haut (`-`) qui constitue le prénom ;
* contiennent ensuite comme séparateur le caractère 'deux-points' `:` ;
* contiennent ensuite une suite - cette fois jamais vide - de caractères alphanumériques ou tiret haut, qui constitue le nom ;
* et enfin contiennent un deuxième caractère `:` mais optionnellement seulement.

+++

On vous demande de construire une expression régulière qui définit les deux groupes `nom` et `prenom`, et qui rejette les lignes qui ne satisfont pas ces critères. 

Dans la correction - et ce sera pareil pour tous les exercices de regexp où on demande des groupes - la correction affiche **uniquement les groupes demandés**; ici on va vous montrer les groupes `nom` et `prenom`; vous avez parfaitement le droit d'utiliser des groupes supplémentaires, nommés ou pas d'ailleurs, dans votre propre regexp.

```{code-cell} ipython3
# entrez votre regexp ici
# il faudra la faire terminer par \Z
# regardez ce qui se passe si vous ne le faites pas

regexp_agenda = r"votre regexp\Z"
```

```{code-cell} ipython3
# évaluez cette cellule pour valider votre code
exo_agenda.correction(regexp_agenda)
```

## Exercice - niveau intermédiaire (3)

+++

##### Numéros de téléphone

Cette fois on veut reconnaître des numéros de téléphone français, qui peuvent être :

* soit au format contenant 10 chiffres dont le premier est un `0` ;
* soit un format international commençant par `+33` suivie de 9 chiffres.

Dans tous les cas on veut trouver dans le groupe `number` les 9 chiffres vraiment significatifs, comme ceci :

```{code-cell} ipython3
from corrections.regexp_phone import exo_phone
exo_phone.example()
```

```{code-cell} ipython3
# votre regexp
# à nouveau il faut terminer la regexp par \Z
regexp_phone = r"votre regexp\Z"
```

```{code-cell} ipython3
# évaluez cette cellule pour valider votre code
exo_phone.correction(regexp_phone)
```

## Exercice - niveau avancé

+++

Vu comment sont conçus les exercices, vous ne pouvez pas passer à `re.compile` un drapeau comme `re.IGNORECASE` ou autre ; sachez cependant que vous pouvez ***embarquer* ces drapeaux dans la *regexp*** elle-même ; par exemple pour rendre la regexp insensible à la casse de caractères, au lieu d'appeler `re.compile` avec le flag `re.I`, vous pouvez utiliser `(?i)` comme ceci :

```{code-cell} ipython3
import re
```

```{code-cell} ipython3
# on peut embarquer les flags comme IGNORECASE
# directement dans la regexp
# c'est équivalent de faire ceci

re_obj = re.compile("abc", flags=re.IGNORECASE)
re_obj.match("ABC").group(0)
```

```{code-cell} ipython3
# ou cela

re.match("(?i)abc","ABC").group(0)
```

```{code-cell} ipython3
:tags: [raises-exception]

# les flags comme (?i) doivent apparaître
# en premier dans la regexp
re.match("abc(?i)","ABC").group(0)
```

Pour plus de précisions sur ce trait, que nous avons laissé de côté dans le complément pour ne pas trop l'alourdir, voyez [la documentation sur les expressions régulières](https://docs.python.org/3/library/re.html#regular-expression-syntax) et cherchez la première occurrence de `iLmsux`.

+++

### Décortiquer une URL

+++

On vous demande d'écrire une expression régulière qui permette d'analyser des URLs.

Voici les conventions que nous avons adoptées pour l'exercice :

* la chaîne contient les parties suivantes :
  * `<protocol>://<location>/<path>` ;
* l'URL commence par le nom d'un protocole qui doit être parmi `http`, `https`, `ftp`, `ssh` ;
* le nom du protocole peut contenir de manière indifférente des minuscules ou des majuscules ;
* ensuite doit venir la séquence `://` ;
* ensuite on va trouver une chaîne `<location>` qui contient :
  * potentiellement un nom d'utilisateur, et s'il est présent, potentiellement un mot de passe ;
  * obligatoirement un nom de `hostname` ;
  * potentiellement un numéro de port ;
* lorsque les 4 parties sont présentes dans `<location>`, cela se présente comme ceci :
  * `<location> = <user>:<password>@<hostname>:<port>` ;
* si l'on note entre crochets les parties optionnelles, cela donne :
  * `<location> = [<user>[:<password>]@]<hostname>[:<port>]` ;
* le champ `<user>` ne peut contenir que des caractères alphanumériques ; si le `@` est présent le champ `<user>` ne peut pas être vide ;
* le champ `<password>` peut contenir tout sauf un `:` et de même, si le `:` est présent le champ `<password>` ne peut pas être vide ;
* le champ `<hostname>` peut contenir une suite non-vide de caractères alphanumériques, underscores, ou `.` ;
* le champ `<port>` ne contient que des chiffres, et il est non vide si le `:` est spécifié ;
* le champ `<path>` peut être vide.

Enfin, vous devez définir les groupes `proto`, `user`, `password`, `hostname`, `port` et `path` qui sont utilisés pour vérifier votre résultat. Dans la case `Résultat attendu`, vous trouverez soit `None` si la regexp ne filtre pas l'intégralité de l'entrée, ou bien une liste ordonnée de tuples qui donnent la valeur de ces groupes ; vous n'avez rien à faire pour construire ces tuples, c'est l'exercice qui s'en occupe.

```{code-cell} ipython3
# exemples du résultat attendu
from corrections.regexp_url import exo_url
exo_url.example()
```

```{code-cell} ipython3
# n'hésitez pas à construire votre regexp petit à petit

regexp_url = "votre_regexp"
```

```{code-cell} ipython3
exo_url.correction(regexp_url)
```

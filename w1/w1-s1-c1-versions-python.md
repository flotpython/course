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
  title: Versions de python
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Versions de Python

+++

### Version de référence : Python-3.6

+++

Comme on l'indique dans la vidéo, la version de Python qui a servi de **référence pour le MOOC est la version 3.6**, c'est notamment avec cette version que l'on a tourné les vidéos.

+++

### Versions plus anciennes

+++

Certaines précautions sont à prendre si vous utilisez une version plus ancienne :

+++

##### Python-3.5

+++

Si vous préférez utiliser python-3.5, la différence la plus visible pour vous apparaitra avec les *f-strings* :

```{code-cell} ipython3
age = 10

# un exemple de f-string
f"Jean a {age} ans"
```

Cette construction - que nous utilisons très fréquemment - n'a été introduite qu'en Python-3.6, aussi si vous utilisez Python-3.5 vous verrez ceci&nbsp;:
```python
>>> age = 10
>>> f"Jean a {age} ans"
  File "<stdin>", line 1
    f"Jean a {age} ans"
                      ^
SyntaxError: invalid syntax
```

+++

Dans ce cas vous devrez remplacer ce code avec la méthode `format` - que nous verrons en Semaine 2 avec les chaines de caractères - et dans le cas présent il faudrait remplacer par ceci&nbsp;:

```{code-cell} ipython3
age = 10

"Jean a {} ans".format(age)
```

Comme ces f-strings sont très présents dans le cours, il est recommandé d'utiliser au moins python-3.6.

+++

##### Python-3.4

+++

La remarque vaut donc *a fortiori* pour python-3.4 qui, en outre, ne vous permettra pas de suivre la semaine 8 sur la programmation asynchrone, car les mots-clés `async` et `await` ont été introduits seulement dans Python-3.5.

+++

### Version utilisée dans les notebooks / versions plus récentes

+++

Tout le cours doit pouvoir s'exécuter tel quel avec une version plus récente de Python.

Cela dit, certains compléments illustrent des nouveautés apparues après la 3.6, comme les *dataclasses* qui sont apparues avec python-3.7, et que nous verrons en semaine 6. 

Dans tous les cas, nous **signalons systématiquement** les notebooks qui nécessitent une version plus récente que 3.6.

+++

Voici enfin, à toutes fins utiles, un premier fragment de code Python qui affiche la version de Python utilisée dans tous les notebooks de ce cours.

Nous reviendrons en détail sur l'utilisation des notebooks dans une prochaine séquence, dans l'immédiat pour exécuter ce code vous pouvez :

* désigner avec la souris la cellule de code ; vous verrez alors apparaître une petite flèche à côté du mot `In `, en cliquant cette flèche vous exécutez le code ;
* une autre méthode consiste à sélectionner la cellule de code avec la souris ; une fois que c'est fait vous pouvez cliquer sur le bouton `>| Run` dans la barre de menu (bleue claire) du notebook.

```{code-cell} ipython3
# ce premier fragment de code affiche des détails sur la
# version de python qui exécute tous les notebooks du cours
import sys
print(sys.version_info)
```

Pas de panique si vous n'y arrivez pas, nous consacrerons très bientôt une séquence entière à l'utilisation des notebooks :)

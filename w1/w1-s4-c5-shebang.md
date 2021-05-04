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
notebookname: '#!/usr/bin/env python'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La ligne *shebang*

+++

```bash
#!/usr/bin/env python3
```

+++

## Complément - niveau avancé

+++

Ce complément est uniquement valable pour macOS et Linux.

+++

### Le besoin

+++

Nous avons vu dans la vidéo que, pour lancer un programme Python, on fait depuis le terminal :

+++

```bash
$ python3 mon_module.py
```

+++

Lorsqu'il s'agit d'un programme que l'on utilise fréquemment, on n'est pas forcément dans le répertoire où se trouve le programme Python. Aussi, dans ce cas, on peut utiliser un chemin "absolu", c'est-à-dire à partir de la racine des noms de fichiers, comme par exemple :

+++

```bash
$ python3 /le/chemin/jusqu/a/mon_module.py
```

+++

Sauf que c'est assez malcommode, et cela devient vite pénible à la longue.

+++

### La solution

+++

Sur Linux et macOS, il existe une astuce utile pour simplifier cela. Voyons comment s'y prendre, avec par exemple le programme `fibonacci.py` que vous pouvez [télécharger ici](data/fibonacci.py) (nous avons vu ce code en détail dans les deux compléments précédents). Commencez par sauver ce code sur votre ordinateur dans un fichier qui s'appelle, bien entendu, `fibonacci.py`.

+++

On commence par éditer le tout début du fichier pour lui ajouter une **première ligne** :

+++

```python
#!/usr/bin/env python3

## La suite de Fibonacci (Suite)
...etc...
```

+++

Cette première ligne s'appelle un [Shebang](http://en.wikipedia.org/wiki/Shebang_%28Unix%29) dans le jargon Unix. Unix stipule que le Shebang doit être en **première position** dans le fichier.

+++

Ensuite on rajoute au fichier, depuis le terminal, le caractère exécutable comme ceci :

+++

```bash
$ pwd
/le/chemin/jusqu/a/
```

+++

```bash
$ chmod +x fibonacci.py
```

+++

À partir de là, vous pouvez utiliser le fichier `fibonacci.py` comme une commande, sans avoir à mentionner `python3`, qui sera invoqué au travers du shebang :

+++

```bash
$ /le/chemin/jusqu/a/fibonacci.py 20
fibonacci(20) = 10946
```

+++

Et donc vous pouvez aussi le déplacer dans un répertoire qui est dans votre variable `PATH`; de cette façon vous les rendez ainsi accessible à partir n'importe quel répertoire en faisant simplement :

+++

```bash
$ export PATH=/le/chemin/jusqu/a:$PATH
```

+++

```bash
$ cd /tmp
$ fibonacci.py 20
fibonacci(20) = 10946
```

+++

**Remarque&nbsp;:** tout ceci fonctionne très bien tant que votre point d'entrée - ici `fibonacci.py` - n'utilise que des modules standards. Dans le cas où le point d'entrée vient avec au moins un module, il est également nécessaire d'installer ces modules quelque part, et d'indiquer au point d'entrée comment les trouver, nous y reviendrons dans la semaine où nous parlerons des modules.

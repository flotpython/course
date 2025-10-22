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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
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

### Version utilisée dans les notebooks / versions plus récentes

+++

Cela dit, les compléments ont été mis à jour au fur et à mesure, le cours est donc totalement pertinent même en 2025, où les notebooks utilisent à présent Python-3.13 (voir ci-dessous)

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

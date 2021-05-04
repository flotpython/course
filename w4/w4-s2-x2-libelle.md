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
notebookname: "Les cha\xEEnes"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Expression conditionnelle

+++

## Exercice - niveau basique

+++

### Analyse et mise en forme

Un fichier contient, dans chaque ligne, des informations (champs) séparées par des virgules. Les espaces et tabulations présentes dans la ligne ne sont pas significatives et doivent être ignorées. 

Dans cet exercice de niveau basique, on suppose que chaque ligne a exactement 3 champs, qui représentent respectivement le prénom, le nom, et le rang d'une personne dans un classement. Une fois les espaces et tabulations ignorées, on ne fait pas de vérification sur le contenu des 3 champs. 

On vous demande d'écrire la fonction `libelle`, qui sera appelée pour chaque ligne du fichier. Cette fonction:

* prend en argument une ligne (chaîne de caractères)
* retourne une chaîne de caractères mise en forme (voir plus bas)
* ou bien retourne `None` si la ligne n'a pas pu être analysée, parce qu'elle ne vérifie pas les hypothèses ci-dessus (c'est notamment le cas si on ne trouve pas exactement les 3 champs)

+++

La mise en forme consiste à retourner 
 
```python
Nom.Prenom (message)
```

le *message* étant lui-même le *rang* mis en forme pour afficher '1er', '2nd' ou '*n*-ème' selon le cas. Voici quelques exemples

```{code-cell} ipython3
# voici quelques exemples de ce qui est attendu
from corrections.exo_libelle import exo_libelle
exo_libelle.example()
```

```{code-cell} ipython3
# écrivez votre code ici
def libelle(ligne):
    "<votre_code>"
```

```{code-cell} ipython3
# pour le vérifier
exo_libelle.correction(libelle)
```

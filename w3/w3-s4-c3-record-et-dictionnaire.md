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
  title: record et dict
---

# Gérer des enregistrements

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

### Implémenter un enregistrement comme un dictionnaire

+++

Il nous faut faire le lien entre dictionnaire Python et la notion d'enregistrement, c'est-à-dire une donnée composite qui contient plusieurs champs. (À cette notion correspond, selon les langages, ce qu'on appelle un `struct` ou un `record`.)

Imaginons qu'on veuille manipuler un ensemble de données concernant des personnes ; chaque personne est supposée avoir un nom, un âge et une adresse mail.

Il est possible, et assez fréquent, d'utiliser le dictionnaire comme support pour modéliser ces données comme ceci :

```{code-cell} ipython3
personnes = [
    {'nom': 'Pierre',  'age': 25, 'email': 'pierre@example.com'},
    {'nom': 'Paul',    'age': 18, 'email': 'paul@example.com'},
    {'nom': 'Jacques', 'age': 52, 'email': 'jacques@example.com'},
]
```

Bon, très bien, nous avons nos données, il est facile de les utiliser.

Par exemple, pour l'anniversaire de Pierre on fera :

```{code-cell} ipython3
personnes[0]['age'] += 1
```

Ce qui nous donne :

```{code-cell} ipython3
for personne in personnes:
    print(10*"=")
    for info, valeur in personne.items():
        print(f"{info} -> {valeur}")
```

### Un dictionnaire pour indexer les enregistrements

+++

Cela dit, il est bien clair que cette façon de faire n'est pas très pratique ; pour marquer l'anniversaire de Pierre on ne sait bien entendu pas que son enregistrement est le premier dans la liste. C'est pourquoi il est plus adapté, pour modéliser ces informations, d'utiliser non pas une liste, mais à nouveau… un dictionnaire.

Si on imagine qu'on a commencé par lire ces données séquentiellement dans un fichier, et qu'on a calculé l'objet `personnes` comme la liste qu'on a vue ci-dessus, alors il est possible de construire un index de ces dictionnaires, (un dictionnaire de dictionnaires, donc).

C'est-à-dire, en anticipant un peu sur la construction de dictionnaires par compréhension :

```{code-cell} ipython3
# on crée un index permettant de retrouver rapidement
# une personne dans la liste
index_par_nom = {personne['nom']: personne for personne in personnes}
index_par_nom
```

```{code-cell} ipython3
# du coup pour accéder à l'enregistrement pour Pierre
index_par_nom['Pierre']
```

Attardons-nous un tout petit peu ; nous avons construit un dictionnaire par compréhension, en créant autant d'entrées que de personnes. Nous aborderons en détail la notion de compréhension de sets et de dictionnaires en semaine 5, donc si cette notation vous paraît étrange pour le moment, pas d'inquiétude.

Le résultat est donc un dictionnaire qu'on peut afficher comme ceci :

```{code-cell} ipython3
for nom, record in index_par_nom.items():
    print(f"Nom : {nom} -> enregistrement : {record}")
```

Dans cet exemple, le premier niveau de dictionnaire permet de trouver rapidement un objet à partir d'un nom ; dans le second niveau au contraire on utilise le dictionnaire pour implémenter un enregistrement, à la façon d'un `struct` en C.

+++

### Techniques similaires

+++

Notons enfin qu'il existe aussi, en Python, un autre mécanisme qui peut être utilisé pour gérer ce genre d'objets composites, ce sont les classes que nous verrons en semaine 6, et qui permettent de définir de nouveaux `types` plutôt que, comme nous l'avons fait ici, d'utiliser un type prédéfini. Dans ce sens, l'utilisation d'une classe permet davantage de souplesse, au prix de davantage d'effort.

+++

## Complément - niveau avancé

+++

#### La même idée, mais avec une classe `Personne`

+++

Je vais donner ici une implémentation du code ci-dessus, qui utilise une classe pour modéliser les personnes. Naturellement je n'entre pas dans les détails, que l'on verra en semaine 6, mais j'espère vous donner un aperçu des classes dans un usage réaliste, et vous montrer les avantages de cette approche.

+++

Pour commencer je définis la classe `Personne`, qui va me servir à modéliser chaque personne :

```{code-cell} ipython3
class Personne:

    # le constructeur - vous ignorez le paramètre self,
    # on pourra construire une personne à partir de
    # 3 paramètres
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    # je définis cette méthode pour avoir
    # quelque chose de lisible quand je print()
    def __repr__(self):
        return f"{self.nom} ({self.age} ans) sur {self.email}"
```

Pour construire ma liste de personnes, je fais alors :

```{code-cell} ipython3
personnes2 = [
    Personne('Pierre',  25, 'pierre@example.com'),
    Personne('Paul',    18, 'paul@example.com'),
    Personne('Jacques', 52, 'jacques@example.com'),
]
```

Si je regarde un élément de la liste j'obtiens :

```{code-cell} ipython3
personnes2[0]
```

Je peux indexer tout ceci comme tout à l'heure, si j'ai besoin d'un accès rapide :

```{code-cell} ipython3
# je dois utiliser cette fois personne.nom et non plus personne['nom']
index2 = {personne.nom : personne for personne in personnes2}
```

Le principe ici est exactement identique à ce qu'on a fait avec le dictionnaire de dictionnaires, mais on a construit un dictionnaire d'instances.

Et de cette façon :

```{code-cell} ipython3
print(index2['Pierre'])
```

Rendez-vous en semaine 6 pour approfondir la notion de classes et d'instances.

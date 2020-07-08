---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Enregistrements et instances

+++

## Complément - niveau basique

+++

### Un enregistrement implémenté comme une instance de classe

+++

Nous reprenons ici la discussion commencée en semaine 3, où nous avions vu comment implémenter un enregistrement comme un dictionnaire. Un enregistrement est l'équivalent, selon les langages, de *struct* ou *record*.

+++

Notre exemple était celui des personnes, et nous avions alors écrit quelque chose comme :

```{code-cell}
pierre = {'nom': 'pierre', 'age': 25, 'email': 'pierre@foo.com'}
print(pierre)
```

Cette fois-ci nous allons implémenter la même abstraction, mais avec une classe `Personne` comme ceci :

```{code-cell}
class Personne:
    """Une personne possède un nom, un âge et une adresse e-mail"""
    
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        
    def __repr__(self):
        # comme nous avons la chance de disposer de python-3.6
        # utilisons un f-string
        return f"<<{self.nom}, {self.age} ans, email:{self.email}>>"
```

Le code de cette classe devrait être limpide à présent ; voyons comment on l'utiliserait - en guise de rappel sur le passage d'arguments aux fonctions :

```{code-cell}
personnes = [

    # on se fie à l'ordre des arguments dans le créateur
    Personne('pierre', 25, 'pierre@foo.com'),

    # ou bien on peut être explicite
    Personne(nom='paul', age=18, email='paul@bar.com'),

    # ou bien on mélange
    Personne('jacques', 52, email='jacques@cool.com'),
]
for personne in personnes:
    print(personne)
```

### Un dictionnaire pour indexer les enregistrements

+++

Nous pouvons appliquer exactement la même technique d'indexation qu'avec les dictionnaires :

```{code-cell}
# on crée un index pour pouvoir rechercher efficacement
# une personne par son nom
index_par_nom = {personne.nom: personne for personne in personnes}
```

De façon à pouvoir facilement localiser une personne :

```{code-cell}
pierre = index_par_nom['pierre']
print(pierre)
```

### Encapsulation

+++

Pour marquer l'anniversaire d'une personne, nous pourrions faire :

```{code-cell}
pierre.age += 1
pierre
```

À ce stade, surtout si vous venez de C++ ou de Java, vous devriez vous dire que ça ne va pas du tout !

En effet, on a parlé dans le complément précédent des mérites de l'encapsulation, et vous vous dites que là, la classe n'est pas du tout encapsulée car le code utilisateur a besoin de connaître l'implémentation.

+++

En réalité, avec les classes python on a la possibilité, grâce aux *properties*, de conserver ce style de programmation qui a l'avantage d'être très simple, tout en préservant une bonne encapsulation, comme on va le voir dans le prochain complément.

+++

## Complément - niveau intermédiaire

+++

Illustrons maintenant qu'en Python on peut ajouter des méthodes à une classe *à la volée* - c'est-à-dire en dehors de l'instruction `class`.

Pour cela on tire simplement profit du fait que **les méthodes sont implémentées comme des attributs de l'objet classe**.

+++

Ainsi, on peut étendre l'objet `classe` lui-même dynamiquement :

```{code-cell}
# pour une implémentation réelle voyez la bibliothèque smtplib
# https://docs.python.org/3/library/smtplib.html

def sendmail(self, subject, body):
    "Envoie un mail à la personne"
    print(f"To: {self.email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    
Personne.sendmail = sendmail
```

Ce code commence par définir une fonction en utilisant `def` et la signature de la méthode. La fonction accepte un premier argument `self` ; exactement comme si on avait défini la méthode dans l'instruction `class`. 

Ensuite, il suffit d'affecter la fonction ainsi définie à **l'attribut `sendmail`** de l'objet classe.

Vous voyez que c'est très simple, et à présent la classe a connaissance de cette méthode exactement comme si on l'avait définie dans la clause `class`, comme le montre l'aide :

```{code-cell}
help(Personne)
```

Et on peut à présent utiliser cette méthode :

```{code-cell}
pierre.sendmail("Coucou", "Salut ça va ?")
```

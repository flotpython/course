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
notebookname: Conditions
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout, Jean-Michel Heras</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Instruction match (1/2)

+++

## Complément - niveau basique

+++

Une instruction switch/case ou match/case est une instruction qui évalue une expression par rapport à un cas et qui exécute ensuite du code. Il s'agit d'une méthode par laquelle les langages de programmation peuvent contrôler le déroulement du programme, en fonction de la satisfaction d'une ou plusieurs conditions.

La version 3.10 de python introduit une nouvelle fonctionnalité permetant de contrôler plus facilement le flux de vos programmes en exécutant certaines parties du code si des conditions (ou cas) sont remplies.

Python va au-delà d'une simple instruction case et offre un contrôle flexible de la correspondance.

`match`, `case` ne sont pas des mots réservés du langage. Ils ne sont reconnus comme mots-clés que lorsqu'ils font partie d'une instruction match ou d'un bloc case. Ils peuvent être utilisés dans tous les autres contextes comme noms de variables ou d'arguments.

+++

### Un premier exemple basique

+++

Le distributeur de boissons chaudes.

 * On commande une boisson en tapant le chiffre correspondant sur le pavé numérique de la machine.
 * Contrairement à un **swicth/case** classique, on ne met pas de **break** après chaque cas. De la même manière que le **if**, une fois qu'on a obtenu un résultat vrai, on sort de l'expression conditionnelle sans évaluer les autres conditions. On s'arrête dès qu'on peut. Pour optimiser le traitement, on met dans l'ordre des plus fréquentes demandes.
 * Si aucun des cas ne correspond, on utilise *l'attape-tout '_' l'underscore* pour evaluer ce cas.
 * Si on n'utilise pas '_' et qu'il n'y a pas de correspondance **match** ne fait rien.

```{code-cell} ipython3
def choix1(boisson):
    match boisson:
        case 1:
            #faire_cafe()
            print("Votre café est prêt !")
        case 2:
            #faire_cappuccino()
            print("Votre cappuccino est prêt !")
        case 3:
            #faire_the()
            print("Votre thé est prêt !")
        case 4:
            #faire_chocolat()
            print("Votre chocolat est prêt !")
        case _:
            print("Boisson inconnue !")
```

```{code-cell} ipython3
choix1(3)
```

La même chose avec un `if`.

```{code-cell} ipython3
def choix2(boisson):
    if boisson == 1:
        #faire_cafe()
        print("Votre café est prêt !")
    elif boisson == 2:
        #faire_cappuccino()
        print("Votre cappuccino est prêt !")
    elif boisson == 3:
        #faire_the()
        print("Votre thé est prêt !")
    elif boisson == 4:
        #faire_chocolat()
        print("Votre chocolat est prêt !")
    else:
        print("Boisson inconnue !")
```

```{code-cell} ipython3
choix2(2)
```

Jusque là, à part un peu plus de lisibilité, ça n'apporte pas grand chose. Mais cela va devenir interessant.
Que faire s'il s'agit de cas différents, mais la façon dont nous les traitons doit être la même.

+++

### L'or en barre ou le pipe '|'

+++

On combine en un seul cas avec le ou '|', les cas dont la réponse est similaire.

```{code-cell} ipython3
def c_pas_faux(mot):
    """Voir Kaamelott, épisode La botte secrète"""
    match mot:
        case "paradoxale"|"dichotomie":
            print("Ouais, c'est pas faux !")
        case "insipide"|"péremptoire":
            print("Non, j'connais pas c'mot la !")
        case _:
            print("Chante sloubi !")
```

```{code-cell} ipython3
c_pas_faux("paradoxale")
c_pas_faux("dichotomie")
c_pas_faux("insipide")
c_pas_faux("python")
```

### Qu'est-ce que match peut évaluer ?

+++

* **Les nombres:**
    * Entiers signés ou non: 4, -4, +4.
    * Flottants signés ou non: 3.14, +1.2, -2.3
    * Complexes: 2j, 2 + 3j, 2 - 3j *Attention, x+y ou x-y autorisé seulement pour les complexes !*

```{code-cell} ipython3
def match_number(my_var):
    match my_var:
        case 8|-8:
            print(type(my_var))
        case 3.14|-3.14:
            print(type(my_var))
        case 2j|2+3j|2-3j:
            print(type(my_var))
        case _:
            print("Pas un nombre")
```

```{code-cell} ipython3
lit_list = [8, -8, 3.14, -3.14, 2j, 2+3j, 2-3j]
for item in lit_list:
    match_number(item)
```

* **Les booléens:**
    * `True`, `False`, `None` *Attention 0 ne renvoie pas `False` et diffèrent de 0 ne renvoie pas `True`!*

```{code-cell} ipython3
def match_bool(my_var):
    match my_var:
        case True:
            print(True)
        case False:
            print(False)
        case None:
            print(None)
        case _:
            print("Pas un booléen.")

def say(something):
    "Fonction qui ne renvoie rien"
    print(something)
```

```{code-cell} ipython3
# la fonction say ne renvoie rien, result == None
result = say("Hello")
# 0 ne renvoie pas False et diffèrent de 0 ne renvoie pas True
bool_list = [True, False, None, 0, 1, bool(-10),bool(0), bool(1), result]

for item in bool_list:
    match_bool(item)
```

* **Les Chaines:**
    * Simples quotes: 'Une chaine'
    * Doubles quotes: "Un autre chaine"
    * Triples quotes: """Encore une""", '''ou celle la'''
    * Les raws strings: r"raw chaine"
    * Les binarys strings: b'binary'

*Les `fstrings` ne sont pas prises en charge.*

```{code-cell} ipython3
:cell_style: split

def match_string(my_var):
    match my_var:
        case 'simple quotes'|"double quotes"|"""triple quotes""":
            print(type(my_var))
        case b"binary":
            print(type(my_var))
        case r"raw string":
            print(type(my_var))
        case _:
            print("autre")
```

```{code-cell} ipython3
:cell_style: split

string_list = ['simple quotes', "double quotes", """triple quotes""", b"binary", r"raw string"]
for item in string_list:
    match_string(item)
```

* Des tuples, des listes.

```{code-cell} ipython3
def odd_even(a, b):
    match(bool(a%2), bool(b%2)):
        case (False, False):
            print("a pair, b pair")
        case (False, True):
            print("a pair, b impair")
        case (True, True):
            print("a impair, b impair")   
        case (True, False):
            print("a impair, b pair")
        case _:
            print("Pas évaluable")
```

```{code-cell} ipython3
odd_even(1, 2)
```

```{code-cell} ipython3
def action(player_input):
    match(player_input.split()):
        case ["go", "north"]: # ou ("go", "north")
            print("ok")
        case _:
            print("commande inconnue")
```

```{code-cell} ipython3
action("go north")
```

**Valider un terme avec une sous-séquence.**

+++

Ici, `sucre` peut prendre n'importe quelle valeur.

```{code-cell} ipython3
def choix(boisson):
    match boisson:
        case(1, sucre):
            print(f"Un café {sucre}.")
        
choix((1, "peu sucré"))
```

Là, on verifie que c'est bien ce qu'on attends avec `as`.

```{code-cell} ipython3
def choix(boisson):
    match boisson:
        # Valide uniquement si dans la séquence.
        case (1, ("non sucré"|"peu sucré"|"sucré"|"très sucré") as sucre):
            print(f"Un café {sucre}.")
        # Peu importe les deux premiers éléments, il y en a plus de deux.
        case (_, _, *args):
            print("argument inconnu ou trop d'arguments.")
        case _:
            print("Autre cas")
            
choix((1, "peu sucré"))
choix((1, "sucré", 8))
choix((1))
```

### Pour en savoir plus

+++

[PEP 634](https://peps.python.org/pep-0634/) specification
[PEP 636](https://peps.python.org/pep-0636/) tutorial

+++

Rendez-vous en semaine 6 pour une seconde partie.

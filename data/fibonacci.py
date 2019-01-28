# La suite de Fibonacci (version pour terminal)

from argparse import ArgumentParser

def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux premières valeurs de n, on peut renvoyer n
    if n <= 1:
        return n
    # sinon on initialise f1 pour n-1 et f2 pour n-2
    f2, f1 = 0, 1
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
#        print(i, f2, f1)
    # le résultat est dans f1
    return f1

# à nouveau : ceci n'est pas conçu pour être exécuté dans le notebook !
parser = ArgumentParser()
parser.add_argument(dest="entier", type=int,
                    help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier

# Nous pouvons à présent afficher le résultat :
print(f"fibonacci({entier}) = {fibonacci(entier)}")


# Vous pouvez donc à présent exécuter ce script
# avec simplement l'interpréteur Python comme ceci :
# 
# $ python3 fibonacci.py 56
# 
# (et sans taper le signe $ qui indique simplement le prompt du terminal)

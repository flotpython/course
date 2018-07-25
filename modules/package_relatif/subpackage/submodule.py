
# notez ici la présence des deux points pour remonter
from ..random import alea as imported

print(f"On charge {__name__}")

def alea():
    return f"<<{imported()}>>"

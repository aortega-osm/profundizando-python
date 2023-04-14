# Manejo de valores infinitos
import math
from decimal import Decimal
print("----------------------------------------------------------------------")
# Constructor float
infinitos_positivos = float("3412343454313431")
print(f"Infinito:{infinitos_positivos}")
print(f"Es infinito:{math.isinf(infinitos_positivos)}")

infinitos_negativo = float("-inf")
print(f"infinito:{infinitos_negativo}")
print(f"Es infinito:{math.isinf(infinitos_negativo)}")

print("----------------------------------------------------------------------")
# Modulo math
infinitos_positivos = math.inf
print(f"Numero:{infinitos_positivos}")
print(math.isinf(infinitos_positivos))

infinitos_negativo = math.inf
print(f"Numero:{infinitos_negativo}")
print(math.isinf(infinitos_negativo))

print("----------------------------------------------------------------------")
# Modulo Decimal

infinitos_positivos = Decimal ("Infinity")
print(f"Numero:{infinitos_positivos}")
print(math.isinf(infinitos_positivos))

infinitos_negativo = Decimal ("Infinity")
print(f"Numero:{infinitos_negativo}")
print(math.isinf(infinitos_negativo))

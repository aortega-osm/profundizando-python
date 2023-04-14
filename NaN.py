import  math
from decimal import Decimal
# Nan no es un numero
# Nan no es sensible a mayusculas o minisculas
# Nan es un tipo de dato numerico indefinido

a = float("Nan")
print(f"Es un numero:{math.isnan(a)}")

a = Decimal("NaN")

a = float("Nan")
print(f"Es un numero:{math.isnan(a)}")

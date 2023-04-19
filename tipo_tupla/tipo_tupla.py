# profundizando tuplas
# declarar variables
a,b="Hola","Adios"

# swap intercambio
a,b = b,a

# Regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos),max(elementos)

min,max=minmax([1,2,3,4,5])
print(min,max)

# Regresa la suma de una tupla
resultado = sum((1,2,3,4,5))
print(resultado)
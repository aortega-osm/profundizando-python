# Expresion generadora(es un generador anonimo)
multiplicacion = (valor*valor for valor in range(5))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# Tambien se puede pasar una expresion generadora a una funcion(sin parentesis)
import math
suma= sum(valor*valor for valor in range(5))
print(f"Resultado suma:{suma}")

# Tambien podemos usar una lista o cualquier otro iterador
lista=["Mario","Andres"]
generador=(valor for valor in lista)
print(next(generador))
print(next(generador))

# Los generadores son mas utiles si queremos recuperar miles o millones de elementos de una lista
# Crear una cadena a partir de un gerenador creado a partir de una lista}
lista=["Karla","Maria",20]
contador = 0
def incrementar():
        global contador
        contador +=1
        return contador
# La primera para el yielf, la segunda es el for entre parenteisis
generador = (f"{incrementar()}.{nombre}" for nombre in lista)
lista=list(generador)
print(lista)
cadena= "---".join(lista)
print(cadena)

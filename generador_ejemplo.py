def generador_numeros():
    for numero in range(1,6):
        yield numero
        print("Se reaunuda la ejecucion")

# utilizamos el generador
generador=generador_numeros()
print(f"Objeto generador:{generador}")
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f"Numero producido:{valor}")
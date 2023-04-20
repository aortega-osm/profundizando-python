# generador
# es una funcion especial,retorna una secuencia de valores
# suspende la ejecucion de la funcion yield(producir)(no se usar return)
def generador():
    yield 1
    print("Se reaunuda la ejecucion")
    yield 2
    print("Se reaunuda la ejecucion")
    yield 3
# consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) saltara error por ausencia de valores

# Consumiendo los valores con un ciclo for
# gen=generador()
# for valor in generador():
#     print(f"Numero generado:{valor}")
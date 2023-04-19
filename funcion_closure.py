# Funcion closure es una funcion que encapsula a otra, o se podria decir que es una funcion que define a otra
# ademas la regresa, la funcion anidada puede acceder a las variables locales definifas
# en la funcion principal o externa

# Funcion principal
# def operacion(a,b):
#     # 1definimos una funcion anidada
#     def sumar():
#         return a + b
#     # 2retornar la funcion}
#     return sumar
# Funcion principal
def operacion(a,b):
    # 1.Definimos una funcion lambda anidada y la retornamos
    return lambda : a + b

mi_funcion_closure = operacion(2, 4)
print(f"Resultado:{mi_funcion_closure()}")

# Llamar la funcion regresada al vuelo
print(f"Resultado de la funcion closure:{operacion(2,3)()}")


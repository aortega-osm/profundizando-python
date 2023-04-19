# Funcion lambda es una funcion anonima y pequeñas(una linea de codigo)
# No es posible asignar una funcion a una variable
# mi_funcion =def sumar(a,b): return a+b

# con una funcion lambda(anonima,sin nombre y una linea)
# no se necesita parentesis para los parametros
# no se necesita usar return pero si una expresio valida
# mi_funcion_lambda = lambda a,b: a + b
# resultado=mi_funcion_lambda(3,4)
# print(resultado)
# # Funcion lambda que no recibe argumentos(debe regresar una expresion
# mi_funcion_lambda = lambda :"Sin argumento"
# print(f"Funcion lambda:{mi_funcion_lambda()}")
#
# # funcion lambda con parametros por default
# mi_funcion_lambda = lambda a=2 , b=3:a+b
# print(f"Funcion con parametro fijos:{mi_funcion_lambda()}")

# # Funcion lambda con argumentos variables *args y **kwargs
# mi_funcion_lambda = lambda *args,**kwargs: len(args)+len(kwargs)
# print(f"Funcion con argumentos:{mi_funcion_lambda(1,2,3,4,a=4,b=5)}")
#
# # Funciones lambda con argumentos,argumentos variables y valores por default)
# mi_funcion_lambda= lambda a,b,c=9, *args,**kwargs:a-b+c+len(args)+len(kwargs)
# print(f"Funcion con argumentos por default:{mi_funcion_lambda(15,2,3, 4,5,6, d=31,e=43)}")
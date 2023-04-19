# Decoradores nos vas a permitir expandir una funcionalidad
# Es una funcion que recibe una funcion y recibe otra funcion
# Funcion decorador(a)
# Funcion a decorar(b)
# Funcion decorada(c)

def funcion_decorador_a(Funcion_a_decorar_b):
    def funcion_decorada_c():
        print("Antes de ejecutar")
        Funcion_a_decorar_b()
        print("Despues de ejecutar")
    return funcion_decorada_c()

@funcion_decorador_a
def mostrar_mensaje():
        print("Hola desde funcion mostrar mensaje")

print("--------------------------")

@funcion_decorador_a
def imprimir():
    print("Hola desde funcion imprimir")


# Decoradores nos vas a permitir expandir una funcionalidad
# Es una funcion que recibe una funcion y otorga otra funcion
# Funcion decorador(a)
# Funcion a decorar(b)
# Funcion decorada(c)

def decorador_a(decorar_b):
    def decorada_c():
        print("Antes de ejecutar")
        decorar_b()
        print("Despues de ejecutar")
    return decorada_c()

@decorador_a
def mostrar_mensaje():
        print("Hola desde funcion mostrar mensaje")

print("--------------------------")

@decorador_a
def imprimir():
    print("Hola desde funcion imprimir")



# Mas de funciones anidades y alcance de variables

def funcion_externa():
    var_local_externa="Variable local externa"

    def funcion_anidada():
        var_local_anidada="Variable local anidada"

        nonlocal var_local_externa
        var_local_externa = "Nuevo valor variable local externa"

    funcion_anidada()
    print(f"Valor variable local externa:{var_local_externa}")
    # no es posible acceder
    # print(f"Valor variable local externa:{var_local_anidada}")
    # Nonlocal indica el uso de una variable que no sera local sino del ambiente que sea originario
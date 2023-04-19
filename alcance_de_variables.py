# alcance de variables en ingles scope
# es el tiiempo de vida o los lugares que se puede usar una variable
# Si definimos una variable fuera de un codigo sera global
var_global ="Variable global"

def imprimir():
    # si queremos modificar una variable debemos especificar que tipo es antes de modificarlo
    global var_global
    # Acceder a una variable global
    print(f"Variable global:{var_global}")
    # definicion de variable local(tambien se puede usar dentro de funciones anidadas
    var_local="Variable local"
    print(f"Variable local:{var_local}")
    var_global="Nuevo valor global"

    def funcion_anidada():
        print(f"Variable local dentro de la funcion anidada:{var_local}")

#No es posible acceder una variable local fuera del bloque


# profundizando en diccionario

# los diccionarios guardan un orden a diferencia de un set
diccionario={"Nombre":"Juan","Apellido":"SANCHEZ","Edad":23}
print(diccionario)

# los dic son mutables pero las llaves deben ser inmutables
diccionario = {(1,2):"Valor1"}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario["Departamento"] = "Sistemas"
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario(si ya existe se remplaza)
diccionario ["Nombre"]="Juan"
print(diccionario)

# Recuperar un valor indicando una llave
# print(diccionario("Nombre"))
# Si no se encuentra la llave lanza una excepcion

# metodo get recupera la llave y si no existe no lanza excepcion
# ademas podemos regresar un valor en caso de que no exista
# print(diccionario.get("Nombre","No se encontro la llave"))
# print(diccionario)
# # setdefault si modifica el diccionario, ademas se agrega un valor por default
# nombre=diccionario.setdefault("Nombre","Valor por default")
# print(nombre)

# imprimir con pprint
from pprint import pprint as pp

# help(pp)
pp(diccionario)


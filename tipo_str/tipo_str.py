import math
from mi_clase import Miclase

# profundizando en el tipo str
# concanetacion automica en python
# # no concaneta una variable

# variable= "adios"
# mensaje= "hola","Mundo," + variable
# mensaje += 'Marea' 'alta'
# print(mensaje)



# Como solicitar ayuda en python
# help(str)
# solicitar ayuda en un metodo especifico
# help(str.join)
# Solicitar ayuda sobre un modulo
# help(math)



# Como solictar ayuda sobre tu clase y ver la documentacion
# help(Miclase)
# print(Miclase.__doc__)
# print(Miclase.mi_metodo.__doc__)
# print(Miclase.__init__.__doc__)
# usando doc vemos la primera documentacion y si especificamos veremos la documentacion especifica
# print(type(Miclase.mi_metodo))
# print(Miclase.mi_metodo)
#  Pa saber el tipo y el la ubicacion del objeto


#Los str son inmutables
# help(str.capatilize)
# mensaje1="hola"
# mensajeBonito=mensaje1.capitalize()
# print(f"Mensaje1:{mensaje1},id:{id(mensaje1)}")
# print(f"Mensaje2:{mensajeBonito},id:{id(mensajeBonito)}")
# mensaje1 += ",adios"
# print(f"Mensaje1:{mensaje1},id:{id(mensaje1)}")



# Metodo join para cadenas
# tupla="hola","mundo","python"
# mensaje= "".join(tupla)
# print(mensaje)
#
# lista_cursos= "Python","Java","Angular"
# mensaje="".join(lista_cursos)
# print(mensaje)
#
# cadena="Holamundo"
# mensaje = ".".join(cadena)
# print(mensaje)
#
# diccionario = {"Nombre":"juan", "apellido":"perez"}
# llaves = ",".join(diccionario.keys())
# valores = ",".join(diccionario.values())
# print(f"llaves:{llaves}")
# print(f"valores:{valores}")



#  Metodo split
# cursos = "Java Python Angular Spring Excel"
# lista_cursos = cursos.split()
# print(f"LISTA CURSO:{lista_cursos}")

# cursosSeparadosComa = "Java, Python, Excel, Angular"
# lista_cursos = cursosSeparadosComa.split(", ",2)
# El 2 en lista_cursos representa el max split(la cantidad de veces que se va a usar el metodo split
# print(f"Lista curso:{lista_cursos}")
# print(len(lista_cursos))



# dar formato a un str

# nombre = "juan"
# edad = 20
# mensaje_con_formato = "Mi nombre es %s y tengo %s años"%(nombre,edad)
# print(mensaje_con_formato)
#
# persona =("Maria","Sanchez",5000.00)
# mensaje_con_formato = "Hola %s %s , tu sueldo es de %s"%(persona)
# print(mensaje_con_formato)
#
# nombre = "juan"
# edad = 20
# sueldo = 3000
# mensaje_con_formato = "Nombre {} Edad {} Sueldo {}".format(nombre,edad,sueldo)
#


#  otra manera de hacerlo es asignando indices
# mensaje_con_formato = "Nombre {0} Edad {1{ Sueldo{2}".format(nombre,edad,sueldo)
# mensaje = "Nombre {n} edad{e} sueldo {s:.2f}",format(n=nombre,e=edad,s=sueldo)



# aqui haremos uso de un diccionario para remplazar los valores
# diccionario ={"nombre":"Ivan","edad":34,"sueldo":5000}
# mensaje = 'Nombre {persona[nombre]} Edad:{persona[edad]} Sueldo:{persona[sueldo]}'.format(persona=diccionario)
# print(mensaje)


# metodo print
# sep= representa lo que se colocara en la separacion
# print(nombre,edad,sueldo,sep=", ")

# multiplicando str (listas,tuplas,cadenas
# resultado = 5 * "Hola"
# print(f"Resultado:{resultado}")
# # multiplicando tuplas
# resultado = 5 * ("Hola",10)
# print(f"Resltado:{resultado}")
# # multiplicando listas
# resultado = 10 *[0]
# print(f"Resultado:{resultado}")


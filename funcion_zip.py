# print(dir(__builtins__))
# # help(zip)
# numeros = (1,2,3)
# letras = ['a','b','c','d']
# indentificadores = 321, 322, 323, 324, 325
# conjunto = {6,4,0,9,8,15,10}
# mezcla = zip(numeros, letras, indentificadores, conjunto)
# # print(mezcla)
# print(list(mezcla))
# # print(tuple(zip(numeros, letras)))
# # print(type(mezcla))
#
# # iterar en paralelo
# for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
#     print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')
#
# nueva_lista = []
# for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
#     nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
# print(nueva_lista)
#
# # unzip
# mezcla=[(1,"a"),(2,"b"),(3,"c")]
# numeros,letras = zip(*mezcla)
# print(numeros,letras)

# ordenamiento usando zip
# letras= ["c","a","b"]
# numeros= [3,42,2,34]
# mezcla= zip(letras,numeros)
# print(tuple(mezcla))
# # ordenar por letra
# print(sorted(zip(letras,numeros)))
# print(sorted(zip(numeros,letras)))

# Crear un diccionario con zip y dos iterables
# llaves = ["Nombre","Apellido","Edad"]
# valores = ("Mario","Sanchez",34)
# dic=dict(zip(llaves,valores))
# print(dic)

# Actualizar un elemento de un diccionario
# llave=["Edad"]
# valor_nuevo=[23]
# dic.update(zip(llave,valor_nuevo))
# print(dic)

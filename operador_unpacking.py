# # desempaquetar
# numeros =[1,2,3]
# print(numeros)
# print(*numeros)
# print(*numeros,sep="-")
#
# # desempaquetando al momento de pasar un parametro a una funcion

# def sumar (a,b,c):
#     print(f"Resultado suma:{a + b +c}")
#
# sumar(*numeros)

# Extraer algunas partes de una lista
# lista=list(range(7))
# print(lista)
# a, *b, c, d = lista
# print(b)
#
# # Unir listas
# lista1=[1,2,3]
# lista2=[4,5,6]
# lista3=[lista1 + lista2]
# print(f"Lista de listas:{lista3}")
# lista3 = [*lista1 , *lista2]
# print(lista3)
#
# # Unir diccionarios
# dic1= {"a":12,"b":34 ,"c":32}
# dic2= {"d":32,"e":41}
# dic3 = {**dic1,**dic2}
# print(dic3)
#
# # Construir una lista a partir de una cadena
#
# cadena=[*"Holamundo"]
# print(cadena)
# print(*cadena,sep="-")


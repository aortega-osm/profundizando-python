# ejemplo atributos publicos,protegidos,privados
#
# class miClase:
#     def __init__(self,publico,protegido,privado):
#         self.publico=publico
#         self._protegido=protegido
#         self.__privado=privado
#
# objecto =miClase("Valor publico","Valor protegido","Valor privado")
# # acceso al atributo publico
# print(objecto.publico)
# # modificar el valor publico
# objecto.publico = "Nuevo valor publico"
# print(objecto.publico)
#
# # Acceso al valor protegido
# # solo dentro de la misma clase o clases hijas
# print(objecto._protegido)
# # modificar atributo protegido
# objecto._protegido="Nuevo valor protegido"
# print(objecto._protegido)
#
# # Acceso al valor privado
# # print(objecto.__privado)
# # Pero,convierte:objeto._clase__atributo_privado
# print(objecto._miClase__privado)
# # Modificar valor privado
# objecto._miClase__privado = "Nuevo valor privado"
# print(objecto._miClase__privado)

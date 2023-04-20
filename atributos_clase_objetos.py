class Persona:
    contador_persona= 0
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


#Mostrar los atributos de un objeto
persona1= Persona("Juan","Perez")
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_persona)
# Accediendo al atributo de clase pero no es posible modificarlo con el objeto,sino con la clase
persona1.contador_persona = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_persona)#Atributo clase
print(persona1.contador_persona)#Atributo del objeto 1

# 2 objeto
persona2=Persona("Karla","Gomez")
print(persona2.__dict__)
print(persona2.contador_persona)

# Todos los atributos de clase que se comparten con los objetos creados de dicha clase
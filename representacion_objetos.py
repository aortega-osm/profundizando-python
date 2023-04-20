# Representacion de objetos(str,repr,format)
print(dir(object))
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    # repr mas enfocado a los programadores
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre:{self.nombre},Apellido:{self.apellido}),"


    #str es mas para el usuario final y otros sistemas
    #la implementacion por default llama al metodo repr

    def __str__(self):
        return f"{self.__class__.__name__}:{self.nombre} {self.apellido}"
    # Format su implementacion por default
    # se manda a llamar al usar f-string,
    def __format__(self, format_spec):
        return f"{self.__class__.__name__} con nombre:{self.nombre} y apellido{self.apellido}"


persona1=Persona("Juan","Perez")
# repr(!r)
print(f"Mi objeto 1:{persona1!r}")
# str(default)
print(persona1)
# format
print(f"{persona1}")


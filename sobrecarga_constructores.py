# simulacion de sobrecarga de constructores en python
# otras formas de crear objetos
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    @classmethod
    def crear_persona(cls):
        return cls()

    @classmethod
    def crear_persona_valores(cls,nombre,apellido):
        return cls(nombre,apellido)

persona1=Persona("JUan","Mario")
persona_vacia = Persona.crear_persona()
persona_valores=Persona.crear_persona_valores("Andrea","Torres")

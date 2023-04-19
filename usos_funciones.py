# las funciones en python son ciudadanos de primera clase
# First class citizens
# eso quiere decir que una función puede ser asignada a una variable, puede ser utilizada como argumento para otra función,
# o inclusive puede ser retornada.

# definimos la funcion
def sumar( a,b):
    return a + b

# 1.Asigar una funcion a una variable (no se usan parentesis)
mi_funcion = sumar

# verificar el tipo de variable
print(type(mi_funcion))
# LLamamos la funcion a traves de la variable
resultado=mi_funcion(4,6)
print(resultado)

# 2 Funcion como argumento
def operacion(a,b,sumar_arg):
    print(f"Suma: {sumar_arg(a,b)}")
operacion(7,3,sumar)

# 3.Podemos retornar una funcion
def retornar_funcion():
    return sumar
mi_funcion_retornada=retornar_funcion()
print({mi_funcion_retornada(1,4)})

 # Funciones Anidadas
# Las funciones anidadas son funciones que se encuentras definidas dentro de otra funciones
def calculadora(a, b, operacion='sumar'):
    # 1. Definir Función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # 2. Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(2, 2, operacion='sumar')
calculadora(400, 300, operacion='restar')
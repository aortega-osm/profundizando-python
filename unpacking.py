variable=1,2,3
valor1,valor2,valor3=variable
print(valor2)

def regresa_datos():
    return 1,2,3
valor1,*valor_restantes= regresa_datos()
print(valor_restantes)
print(valor1)

hora="16:45".partition(":")
hora,separador,minutos=hora
print(f"hora:{hora},minutos:{minutos})")
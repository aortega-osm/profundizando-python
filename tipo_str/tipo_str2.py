# profundizando tipo str

# caracteres de escape
# resultado = "hoLA/" Mundo"
# print(f"Resultado:{resultado}")

# resultado = "Se va a eliminar el punto.\b\b\b"
# print(f"Resultado:{resultado}")

# caracteres en byte
# caracterees_bytes = b"Holamundo"
# print(caracterees_bytes)
#
# mensaje = b"Universidad python"
# print(mensaje[0])
#
# listaCaracteres= mensaje.split()
# print(listaCaracteres)

# convertir de str a bytes y viceversa
# str= "Programacion en python"
# print("Frase original:",str)
# bytes = str.encode("UTF-8")
# print(f"Bytes codificados:{bytes}")
# # convertir de bytes a str
# str2= bytes.decode()
# print(f"string decodificado:{str2}")
# print(str == str2)

# Algunos metodos mas del tipo str

# Contar veces ocurrencias de una cadena
# print("No veces que aparece Universidad:",mensaje.count("Universidad"))

# Convertir en mayusculas la cadena
# (mensaje.upper())

# Convertir en minisculas la cadena
# (mensaje.lower())

# para saber si existe un mensaje podriasmor preguntar
# print("Existe python en el texto:","python".lower() in contenido.lower())

# startswith inicia con
# print("inicia con:",mensaje.startswith("En GlobalMentoring.com.mx"))

# esto es para comprobar si es verdad que termina o empieza de cierta manera
# endswith termina con
# print("termina con:",mensaje.endswith("GlobalMentoring.com.mx"))

# islower funciona para saber si todos los caracteres estan en minisculas mientras que isupper para sabier si estan en mayusculas
# print(mensaje.islower)

# alinear cadenas
# center- centrar una cadena
titulo="Maria"
# print(len(titulo)
# print(titulo.center(50,"-"))
# print(titulo.center(len(titulo)+10,"-"))----esta es la mejor forma que va a centrar de mejor manera sin causar error

# Alinear a la izquierda
# print(titulo.ljust(50,"-"))
# print(titulo.ljust(len(titulo)+10,"-"))

# Alinear a la derecha
# print(titulo.rjust(50,"-"))
# print(titulo.rjust(len(titulo)+10,"-"))

# Remplazar contenido de un str
print(titulo.replace("a","-"))

# eliminar caracteres al inicio hy al final de un str
titulo2="***Maria***"
print("Cadena original:",titulo2)
titulo2 =titulo2.strip
# se le puede asignar un solo lado usando el lstrip o rstrip
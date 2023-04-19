# Profundizar en set
# Un set es una coleccion de elementos unicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto={[1,2],[3,4]}
conjunto={"Juan",True,14.4}
print(conjunto)
# conjunto={} genera un dict vacio

# generar set vacio
conjunto=set()

# Mutable
conjunto.add("Mario")
print(conjunto)
# Contiene valores unicos
conjunto.add("Mario")
print(conjunto)
# Crear un set a partir de un iterable
conjunto=set([3,4,54,3])
print(conjunto)

# Agregar mas elemeentos incluso otro set
conjunto2={100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,3,2,1])
print(conjunto)

conjunto_copia = conjunto.copy()
print(conjunto_copia)

# Verificar igualdad
# if conjunto_copia == conjunto:
#     print("Son iguales")
# else:
#     print("No son iguales")
# otra forma de verificar
# print(f"Son iguales?:{conjunto_copia == conjunto}")
# print(f"Son iguales en referencia?:{conjunto_copia is conjunto}")

# Operaciones de conjuntos con set
# Personas con distintas caracteristicas
pelo_negro= {"Juan","Laura","Maria"}
pelo_rubio= {"Lorenzo","Laura","Marco"}
ojos_cafe= {"Karla","Laura"}
menores_30= {"Juan","Karla","Maria","Laura"}

# Todos con ojos cage y pelo rubio(union),(es conmutativa)
print(ojos_cafe.union(pelo_rubio))

# intersection te muestra el elementos en comun solo las personas pelo rubio y ojos cafe
print(ojos_cafe.intersection(pelo_rubio))

# difference para saber los elementos de u una variable
print(pelo_negro.difference(ojos_cafe))

# Symmetric Difference pelo negro y ojos cafe no ambas (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set esta contenido en otro(subset)
# revisemos si los elementos del primer set estan TODOS contenidos en el segundo
print(ojos_cafe.issubset(menores_30))

# Preguntar si un set contiene a otro set(superset)
# Revisar si los elementos del primer set estan contenidos en el segundo
print(ojos_cafe.issuperset(pelo_negro))
# Preguntar si son completamentes diferentes(disjoint)
print(ojos_cafe.isdisjoint(pelo_negro))
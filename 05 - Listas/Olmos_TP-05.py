#----------------------------------------Ejercicio 1----------------------------------------
# Creamos la lista
lista = []
for i in range(1,100):
    if i % 4 == 0:
        lista.append(i)
# Imprimimos (aunque no se nos pide específicamente)
print(lista)

#----------------------------------------Ejercicio 2----------------------------------------
# Creamos una lista cualquiera
lista = [1, 2, 3, 4, 5]
# Pedimos mostrar el elemento "-2" ya que al utilizar el número negativo accedemos al penúltimo
# elemento, sin necesidad de saber exactamente la longitud de la lista
print(lista[-2])

#----------------------------------------Ejercicio 3----------------------------------------
# Creamos la lista vacía
lista = []
# Agregamos las palabras
lista.append("Hola")
lista.append("como")
lista.append("estas?")
# Imprimimos la lista resultante
print(lista)

#----------------------------------------Ejercicio 4----------------------------------------
# Creamos la lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos los valores
animales[1] = "loro"
animales[-1] = "oso"

# Imprimimos la lista para ver las modificaciones
print(animales)

#----------------------------------------Ejercicio 5----------------------------------------
# El programa que se nos presenta es el siguiente:
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
# Su funcionamiento es simple, primero se crea la lista de números, luego se elimina el valor 
# más grande de esta y finalmente se imprime la lista resultante

#----------------------------------------Ejercicio 6----------------------------------------
# Creamos la lista con la función range casteado a tipo lista
numeros = list(range(10,31,5))

# Imprimimos por pantalla los 2 primeros elementos
print(f"Primer elemento: {numeros[0]}")
print(f"Segundo elemento: {numeros[1]}")

#----------------------------------------Ejercicio 7----------------------------------------
# Creamos la lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos los valores del medio
autos[1] = "vento"
autos[2] = "t-cross"

#----------------------------------------Ejercicio 8----------------------------------------
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.
# Creamos la lista vacía
dobles = []

# Añadimos directamente los valores que se nos piden
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)

# Imprimimos la lista resultante
print(dobles)

#----------------------------------------Ejercicio 9----------------------------------------
# Generamos la lista que se nos da como base
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")

# Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# Imprimimos el resultado
print
print(f"Lista final: {compras}")

#----------------------------------------Ejercicio 10----------------------------------------
# Creamos una lista base
lista_anidada = [0, 0, [0, 0, 0], 0]

# Reemplazamos cada valor con lo que nos piden
lista_anidada[0] = 15
lista_anidada[1] = True
lista_anidada[2][0] = 25.5
lista_anidada[2][1] = 57.9
lista_anidada[2][2] = 30.6
lista_anidada[3] = False

# Imprimimos
print(lista_anidada)


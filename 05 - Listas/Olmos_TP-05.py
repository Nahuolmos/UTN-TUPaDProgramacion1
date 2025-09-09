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

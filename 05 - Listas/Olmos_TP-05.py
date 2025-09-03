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


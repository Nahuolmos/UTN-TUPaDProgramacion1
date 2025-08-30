#----------------------------------------Ejercicio 1----------------------------------------
# Creamos un bucle for ya que sabemos cuantas veces tiene que repetirse la instrucción y el límite
# lo fijamos en 101 para que el 100 esté incluido.
for i in range(101):
    print(i)

#----------------------------------------Ejercicio 2----------------------------------------
# Pedimos al usuario que ingrese un numero entero, pero lo guardamos como cadena para poder contar
# sus "dígitos" (que serían los caracteres)
num : str =input("Ingrese un número entero: ")

# Creamos una variable contador que guarda la cantidad de dígitos y lo mostramos (aunque sería más fácil utilizar la funcion len())
cont = 0
while cont < len(num):
    cont += 1
print(f"Cantidad de caracteres: {cont}")

#----------------------------------------Ejercicio 3----------------------------------------
# Pedimos al usuario que ingrese los valores minimos y maximos del intervalo
num_min : int = int(input("Ingrese el valor mínimo del intervalo: "))
num_max : int = int(input("Ingrese el valor máximo del intervalo: "))

# Mostramos el resultado
print(f"Los número del intervalo ({num_min}, {num_max}) son: ")
for i in range((num_min+1), num_max):
    print(i)

#----------------------------------------Ejercicio 4----------------------------------------
# Creamos el bucle while ya que no sabemos cuántos numeros ingresasaría el usuario
bandera = True
suma = 0
while bandera == True:
    num : int = int(input("Ingrese un número o 0 para terminar la secuencia: "))
    suma += num
    # definimos la condición para finalizar el bucle
    if num == 0:
        print(f"Secuencia finalizada")
        bandera = False
print(f"Suma total: {suma}")

#----------------------------------------Ejercicio 5----------------------------------------
# Importamos la libreria random para poder generar el número aleatorio
import random
num_azar = random.randint(0,9)

# Creamos el bucle para que el usuario intente adivinar (asumiendo que solamente ingrese enteros)
bandera = True
respuesta = 0
intentos = 0
while bandera == True:
    if intentos == 0:
        respuesta : int = int(input("Intenta adivinar el número secreto: "))
        intentos += 1
    elif intentos > 0 and respuesta != num_azar:
        respuesta : int = int(input("Casi! Intenta de nuevo: "))
        intentos += 1
    if respuesta == num_azar:
        print(f"Adivinaste! en {intentos} intentos")
        bandera = False

#----------------------------------------Ejercicio 6----------------------------------------
# Podríamos definir la condicion directamente en el paso en la funcion range poniendo en -2 
# pero definimos la condicion dentro de un if por si queremos cambiar la condición que sea más fácil
for i in range(100, 0, -1):
    if i%2 == 0:
        print(i)

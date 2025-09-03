#----------------------------------------Ejercicio 1----------------------------------------
# Creamos un bucle for ya que sabemos cuantas veces tiene que repetirse la instrucción y el límite
# lo fijamos en 101 para que el 100 esté incluido.
for i in range(101):
    print(i)

#----------------------------------------Ejercicio 2----------------------------------------
# Pedimos al usuario que ingrese un numero entero y validamos que lo sea
bandera : bool = True
while bandera:
    numero = input("Ingrese un número entero: ")
    # Validamos que no sea una cadena de caracteres
    if not numero.isalpha():
        contador : int = 0
        # Ignoramos el signo si es un número negativo
        for i in numero:
            if i != "-":
                contador += 1
        # Imprimimos el resultado
        print(f"La longitud de {numero} es: {contador}")
        bandera = False
    else:
        print("Valor inválido")
        print()

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

#----------------------------------------Ejercicio 7----------------------------------------
# Pedimos al usuario que ingrese el máximo del intervalo
num_max : int = int(input("Ingrese el límite de la sucesión: "))
suma = 0
for i in range(0,num_max):
    suma += i
print(f"La suma total es: {suma}")

#----------------------------------------Ejercicio 8----------------------------------------
# Pedimos al usuario que ingrese los números e inicializamos las variables para clasificarlos
pares : int = 0
impares : int = 0
pos : int = 0
negs : int = 0
for i in range (0,10):
    num : int = int(input("Ingrese un número entero: "))
    # clasificamos
    if num%2 == 0:
        pares += 1
    if num%2 != 0:
        impares += 1
    if num > 0:
        pos += 1
    elif num < 0:
        negs += 1
    else:
        continue
# Mostramos el conteo total
print(f"Números pares ingresados: {pares}")
print(f"Números impares ingresados: {impares}")
print(f"Números positivos ingresados: {pos}")
print(f"Números negativos ingresados: {negs}")

#----------------------------------------Ejercicio 9----------------------------------------
# Definimos en una sola linea la cantidad máxima de números que se le van a pedir al usuario
cant_nums = 100
# Creamos el bucle que pediría los números e inicializamos variables
num : int = 0
suma = 0
for i in range (0, cant_nums):
    num : int = int(input("Ingresa un número entero: "))
    suma += num
media = suma/cant_nums
print(f"La media de los valores ingresados es: {media}")

#----------------------------------------Ejercicio 10----------------------------------------
# Pedimos al usuario un número entero
num = int(input("Ingresa un número: "))

invertido = 0
# Mientras el número no sea 0, vamos sacando de a un dígito
while num > 0:
    # Guardamos el último dígito
    digito = num % 10
    # Lo agregamos al número invertido
    invertido = invertido * 10 + digito
     # Eliminamos el último dígito del número original
    num = num // 10

print(f"Número invertido: {invertido}")
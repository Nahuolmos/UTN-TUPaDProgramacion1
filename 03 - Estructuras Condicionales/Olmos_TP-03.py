#----------------------------------------Ejercicio 1----------------------------------------#----------------------------------------Ejercicio 1----------------------------------------
# Solicitamos edad al usuario y lo guardamos en la variable "edad"
edad : int = int(input("Ingrese su edad: "))

# Creamos una variable mayor_de_edad por si en algún momento llegara a cambiar (como de 21 a 18)
mayor_de_edad = 18

if edad >= mayor_de_edad:
    print("Es mayor de edad")
elif edad > 0 and edad < mayor_de_edad:
    print("Es menor de edad")
else:
    print("Valor inválido")

#----------------------------------------Ejercicio 2----------------------------------------
# Solicitamos la nota al usuario y lo guardamos en la variable "nota"
nota : float = float(input("Ingrese su nota: "))

# Creamos una variable nota_aprobacion por si en algún momento queremos cambiarla
nota_aprobacion = 6
# Fijamos la calificacion maxima que se pueda obtener para no cargar valores incorrectos
nota_maxima = 10

if nota >= nota_aprobacion and nota <= nota_maxima:
    print("Aprobado")
elif nota > 0 and nota < nota_aprobacion:
    print("Desaprobado")
else:
    print("Valor inválido")

#----------------------------------------Ejercicio 3----------------------------------------
#Solicitamos ingresar numeros al usuario y lo guardamos en la variable num
#De tipo entero para poder evaluar si es par
num : int = int(input("Ingrese un número par: "))

if num%2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
#----------------------------------------Ejercicio 4----------------------------------------
# Solicitamos edad al usuario y lo guardamos en la variable "edad"
edad : int = int(input("Ingrese su edad: "))

#Clasificamos al usuario
if edad > 0 and edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente") 
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
elif edad >= 30:
    print("Categoría: Adulto/a")

#----------------------------------------Ejercicio 5----------------------------------------
# Solicitamos al usuario que ingrese una contraseña
password : str = input("Ingrese su contraseña (8 a 14 caracteres): ")

# Verificamos si la longitud de la contraseña es correcta
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#----------------------------------------Ejercicio 6----------------------------------------
# Importamos mode, median y mean desde la libreria statistics
from statistics import mode, median, mean
# Importamos la libreria random
import random
# Creamos nuestra lista de números aleatorios
nums_aleatorios = [random.randint(1, 100) for i in range(50)]

# Definimos media, mediana y moda
media = mean(nums_aleatorios)
mediana = median(nums_aleatorios)
try:
    moda = mode(nums_aleatorios)
except:
    # En caso de que no haya una moda clara (Recomendación de chatGPT)
    moda = None

# Definimos el sesgo
if moda is not None:
    if media > mediana > moda:
        print("Sesgo positivo (hacia la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (hacia la izquierda)")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("Sin sesgo claro según los criterios dados")
else:
    print("No se puede determinar el sesgo por falta de moda clara")

#----------------------------------------Ejercicio 7----------------------------------------
# Solicitamos al usuario que ingrese una frase o palabra
texto : str = input("Ingrese una frase o palabra: ")

# Verificamos si la última letra es una vocal (mayúscula o minúscula)
# Utilizamos la funcion lower() para hacer más fácil la verificación
# sin importar si el usuario ingreso en mayúsculas o minúsculas
if texto[-1].lower() in "aeiou":
    # Si termina en vocal, añadimos un signo de exclamación
    texto += "!"

# Imprimimos el resultado
print(texto)

#----------------------------------------Ejercicio 8----------------------------------------
# Solicitamos el nombre al usuario y lo guardamos en la variable "nombre"
nombre : str = input("Ingrese su nombre: ")

# Solicitamos la opción que quiera al usuario y lo guardamos en la variable "opcion"
print("Elija una opción para transformar su nombre:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra mayúscula")
opcion : int = int(input("Ingrese 1, 2 o 3: "))

# Transformamos el nombre según la opción y lo guardamos en la variable "resultado"
if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = "Opción inválida"

print("Resultado:", resultado)

#----------------------------------------Ejercicio 9----------------------------------------
# Solicitamos al usuario que ingrese la magnitud del terremoto para clasificarlo
magnitud : float = float(input("Ingrese la magnitud del terremoto: "))
# Creamos los parámetros de clasificación y los imprimimos por pantalla
if magnitud > 0 and magnitud < 3:
    print("Categoría: Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Categoría: Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Categoría: Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Categoría: Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Categoría: Muy Fuerte")
elif magnitud >= 7:
    print("Categoría: Extremo")
else:
    print("Opción Inválida")

#----------------------------------------Ejercicio 10---------------------------------------
# Solicitamos al usuario que ingrese su hemisferio (Norte o Sur) 
# y lo guardamos en la variable "hemisferio" en mayúscula
hemisferio : str = input("Ingrese su hemisferio (N/S): ").upper()
# Solicitamos al usuario que ingrese el día y el mes actual
mes : str = int(input("Mes(1-12): "))
dia : str = int(input("Día(1-31): "))
# Determinamos en que estación se encuentra el usuario según hemisferio y fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        print("Estación: Invierno")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Opción inválida"

print("La estación actual es:", estacion)

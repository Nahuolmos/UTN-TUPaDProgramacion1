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
password = input("Ingrese su contraseña (8 a 14 caracteres): ")

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

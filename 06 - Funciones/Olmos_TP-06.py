#----------------------------------------Ejercicio 1----------------------------------------
# Creamos la función y la nombramos
def imprimir_hola_mundo():
    print("Hola Mundo!")
# Llamamos a la función
imprimir_hola_mundo()
#----------------------------------------Ejercicio 2----------------------------------------
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)
#----------------------------------------Ejercicio 3----------------------------------------
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola! Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad : int = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#----------------------------------------Ejercicio 4----------------------------------------
from math import pi
def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio : float = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es: ", calcular_area_circulo(radio))
print("El perímetro del círculo es: ", calcular_perimetro_circulo(radio))
#----------------------------------------Ejercicio 5----------------------------------------
def segundos_a_horas(segundos):
    return segundos/60

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Su equivalente en horas es: ", segundos_a_horas(segundos))

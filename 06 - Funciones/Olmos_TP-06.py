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
#----------------------------------------Ejercicio 6----------------------------------------
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero}x{i} = {numero*i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)
#----------------------------------------Ejercicio 7----------------------------------------
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b 
    else: 
        print("No se puede dividir por cero")

    return (suma, resta, multiplicacion, division)

a : float = float(input("Ingrese el primer número: "))
b : float = float(input("Ingrese el segundo número: "))

resultados : tuple = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
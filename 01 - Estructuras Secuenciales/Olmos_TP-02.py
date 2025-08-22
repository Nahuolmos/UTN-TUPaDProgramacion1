import math

# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre: str = input("Ingrese su nombre: ")
print(f"¡Hola {nombre}!")

# Ejercicio 3
nombre: str = input("Ingrese su nombre: ")
apellido: str = input("Ingrese su apellido: ")
edad: int = int(input("Ingrese su edad: "))
residencia: str = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
radio: float = float(input("Ingrese el radio del círculo: "))
area: float = math.pi * radio**2
perimetro: float = 2 * math.pi * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5
segundos: int = int(input("Ingrese la cantidad de segundos: "))
horas: float = segundos/3600
print(f"{segundos}s equivalen a {horas}h")

# Ejercicio 6
numero: int = int(input("Ingrese un numero entero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Ejercicio 7
num1: int = int(input("Ingresá el primer número entero (distinto de 0): "))
num2: int = int(input("Ingresá el segundo número entero (distinto de 0): "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Ejercicio 8
peso: float = float(input("Ingrese su peso en kg: "))
altura: float = float(input("Ingrese su altura en metros: "))
IMC = peso / (altura**2)
print(f"Su índice de masa corporal es: {IMC}")

# Ejercicio 9
grados: float = float(input("Ingrese la temperatura en C°: "))
fahrenheit = 9/5 * grados + 32
print(f"La equivalencia en F° es: {fahrenheit}F")

# Ejercicio 10
num1: float = float(input("Ingresá el primer número: "))  # Se espera un número
num2: float = float(input("Ingresá el segundo número: ")) # Se espera un número
num3: float = float(input("Ingresá el tercer número: "))  # Se espera un número
promedio: float = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")

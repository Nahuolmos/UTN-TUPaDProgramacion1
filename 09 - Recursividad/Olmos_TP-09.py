#----------------------------------------Ejercicio 1----------------------------------------
def fact(x):
    return 1 if x == 1 or x == 0 else x * fact(x - 1)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print([fact(i) for i in range(int(num) + 1)])

#----------------------------------------Ejercicio 2----------------------------------------
def fib(x):
    return 0 if x == 0 else 1 if x == 1 else fib(x - 1) + fib(x - 2)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print([fib(i) for i in range(int(num) + 1)])

#----------------------------------------Ejercicio 3----------------------------------------
def pot(a, b):
    return 1 if b == 0 else a * pot(a, b - 1)

num1 = input("Ingrese un número natural: ")
while not num1.isdigit():
    num1 = input("Ingrese un número válido por favor: ")

num2 = input("Ingrese otro número natural: ")
while not num2.isdigit():
    num2 = input("Ingrese un número válido por favor: ")

print(f"el resultado de hacer {num1} elevado a la {num2} es {pot(int(num1), int(num2))}.")

#----------------------------------------Ejercicio 4----------------------------------------
def a_binario(x):
    if x == 0:
        return ""
    else:
        resto = str(x % 2)
        return a_binario(x // 2) + resto

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(a_binario(int(num)))
#----------------------------------------Ejercicio 5----------------------------------------
def es_palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        if palabra[0] != palabra[len(palabra) - 1]:
            return False
        else:
            return es_palindromo(palabra[1:len(palabra) - 1])

palabra = input("Por favor, ingrese una palabra sin espacios ni tildes: ")
while " " in palabra or "´" in palabra:
    palabra = input("Ingrese una palabra válida: ")

print(es_palindromo(palabra))

#----------------------------------------Ejercicio 6----------------------------------------
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        nu = n % 10
        return nu + suma_digitos(n // 10)

num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(suma_digitos(int(num)))

#----------------------------------------Ejercicio 7----------------------------------------
def suma_todos(n):
    if n == 0:
        return 0
    else:
        return n + suma_todos(n - 1)
    
num = input("Ingrese un número natural: ")
while not num.isdigit():
    num = input("Ingrese un número válido por favor: ")

print(suma_todos(int(num)))

#----------------------------------------Ejercicio 8----------------------------------------
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            valor = 1
        else:
            valor = 0
        return valor + contar_digito(numero // 10, digito)
    
num1 = input("Ingrese un número natural: ")
while not num1.isdigit():
    num1 = input("Ingrese un número válido por favor: ")

num2 = input("Ingrese un dígito del 0 al 9: ")
while not num2.isdigit() or len(num2) != 1:
    num2 = input("Ingrese un dígito válido por favor: ")

print(contar_digito(int(num1), int(num2)))
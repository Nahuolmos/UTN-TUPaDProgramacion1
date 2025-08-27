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
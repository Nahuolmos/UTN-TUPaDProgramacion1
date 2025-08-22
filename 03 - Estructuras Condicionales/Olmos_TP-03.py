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
    

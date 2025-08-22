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

#----------------------------------------Ejercicio 1----------------------------------------
# Creamos el diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Agregamos lo que se nos pide
# Naranja = 1200 
# Manzana = 1500
# Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#----------------------------------------Ejercicio 2----------------------------------------
# Actualizamos precios de las frutas del diccionario anterior
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#----------------------------------------Ejercicio 3----------------------------------------
# Recuperamos en una lissta las keys de nuestro diccionario para ver solo las frutas sin precios
precios_frutas.keys()

#----------------------------------------Ejercicio 4----------------------------------------
# Creacion del diccionario contactos
contactos = {}
for i in range(1,6):
    contactos[input("Ingrese el nombre del contacto: ")] = int(input("Ingrese el número telefónico: "))
    print()

# Consulta dentro del diccionario
def buscar_por_nombre(nombre_a_buscar):
    if nombre_a_buscar in contactos:
        print("El número es: ", contactos[nombre_a_buscar])
    else:
        print("No se encontró el contacto buscado")

nombre_a_buscar = input("Ingrese el nombre del contacto a buscar: ")
buscar_por_nombre(nombre_a_buscar)

#----------------------------------------Ejercicio 5----------------------------------------
# Solicitamos una frase al usuario
frase = input("Ingresa una frase: ")
# Separa la frase en palabras
palabras = frase.split()
# Devolver las palabras únicas usando un set
palabras_unicas = set(palabras)
# Crea un diccionario con la cantidad de veces que aparece cada palabra
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
# Muestra los resultados
print("Palabras únicas:")
print(palabras_unicas)
print("Frecuencia de cada palabra:")
print(frecuencias)

#----------------------------------------Ejercicio 6----------------------------------------
alumnos = {}
can_alumnos : int = 3
for i in range(can_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

#----------------------------------------Ejercicio 7----------------------------------------
# Cada número representaría a un estudiante
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


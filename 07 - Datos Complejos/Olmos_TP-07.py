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

#----------------------------------------Ejercicio 8----------------------------------------
dict = {"leche": 10, "huevos": 30, "manteca": 15, "galletas": 20, "tortitas": 12}
bandera = True

while bandera:
    print("Opciones: ")
    print("|1. Consultar stock de un producto")
    print("|2. Modificar stock de un producto")
    print("|3. Agregar producto y stock")
    print("|4. Salir")
    consulta = input("> ")
    while consulta not in ("1", "2", "3", "4"):
        consulta = input("Por favor, ingrese un comando válido: 1, 2 ó 3: ")

    if consulta == "1":
        producto = input("¿De qué producto desea consultar el stock?: ")
        while producto.lower() not in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto de la lista: ")
        print(f"Hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    elif consulta == "2":
        producto = input("¿De qué producto desea actualizar el stock?: ")
        while producto.lower() not in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto de la lista: ")
        unidades = input(f"¿Cuántas unidades de {producto} hay en stock?: ")
        while not unidades.isdigit():
            unidades = input("Ingrese una cantidad válida: ")
        dict[producto.lower()] = unidades
        print(f"Ahora hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    elif consulta == "3":
        producto = input("¿Qué producto desea agregar al stock?: ")
        while producto.lower() in dict:
            producto = input(f"Los productos con stock son {list(dict.keys())}. Ingrese un producto que no esté en la lista para agregar: ")
        unidades = input(f"¿Cuántas unidades de {producto} hay en stock?: ")
        while not unidades.isdigit():
            unidades = input("Ingrese una cantidad válida: ")
        dict[producto.lower()] = unidades
        print(f"Ahora hay {dict[producto.lower()]} unidades del producto {producto} en stock.")

    else:
        bandera = False
        print("¡Adiós!")

#----------------------------------------Ejercicio 9----------------------------------------
agenda = {("sábado", "20:00"): "casamiento", ("sábado", "10:00"): "partido", ("lunes", "8:00"): "examen"}

dias_y_horas = list(agenda.keys())
print(f"Tienes actividades el {dias_y_horas[0][0]} a las {dias_y_horas[0][1]}, el {dias_y_horas[1][0]} a las {dias_y_horas[1][1]} y el {dias_y_horas[2][0]} a las {dias_y_horas[2][1]}.")
dia = input("¿Qué actividad desea consultar? Ingrese día: ")
hora = input("Ingrese hora (ejemplo: 20:00): ")
dia_y_hora = (dia.lower(), hora)
if dia_y_hora not in agenda:
    print("No tienes actividades ese día a esa hora.")
else:
    print(f"Tienes {agenda[dia_y_hora]} ese día a esa hora.")

#----------------------------------------Ejercicio 10----------------------------------------
original = {"Argentina": "CABA", "Chile": "Santiago", "Bután": "Timbu"}
invertido = {}

paises = list(original.keys())
capitales = list(original.values())

for i in range(len(paises)):
    invertido[capitales[i]] = paises[i]

print(invertido)
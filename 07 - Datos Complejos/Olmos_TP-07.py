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
#----------------------------------------Ejercicio 1----------------------------------------
with open("productos.txt", "w") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.write("manzana,1000,20\n")
    archivo.write("banana,2000,30\n")
    archivo.write("uva,1500,40\n")

#----------------------------------------Ejercicio 2----------------------------------------
with open("productos.txt", "r") as archivo:
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")

    print(f"Producto: {primera_linea[0].title()} | Precio: ${primera_linea[1]} | Cantidad: {primera_linea[2]}")
    print(f"Producto: {segunda_linea[0].title()} | Precio: ${segunda_linea[1]} | Cantidad: {segunda_linea[2]}")
    print(f"Producto: {tercera_linea[0].title()} | Precio: ${tercera_linea[1]} | Cantidad: {tercera_linea[2]}")

#----------------------------------------Ejercicio 3----------------------------------------
with open("productos.txt", "r+") as archivo:
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")

    print(f"Producto: {primera_linea[0].title()} | Precio: ${primera_linea[1]} | Cantidad: {primera_linea[2]}")
    print(f"Producto: {segunda_linea[0].title()} | Precio: ${segunda_linea[1]} | Cantidad: {segunda_linea[2]}")
    print(f"Producto: {tercera_linea[0].title()} | Precio: ${tercera_linea[1]} | Cantidad: {tercera_linea[2]}")

    nuevo_producto = input("Ingrese un nuevo producto para ingresar a la lista: ")
    while nuevo_producto == "" or nuevo_producto.lower() in (primera_linea[0], segunda_linea[0], tercera_linea[0]):
        nuevo_producto = input("Ese producto ya está en la lista. Ingrese otro producto: ")
    
    precio_n_p = input("Ingrese el precio del producto a añadir a la lista: ")
    while precio_n_p == "" or not precio_n_p.isdigit():
        precio_n_p = input("Por favor, ingrese un valor válido: ")
    
    cantidad_n_p = input("Ingrese la cantidad del producto a añadir a la lista: ")
    while cantidad_n_p == "" or not cantidad_n_p.isdigit():
        cantidad_n_p = input("Por favor, ingrese un valor válido: ")
    
    archivo.write(f"{nuevo_producto.lower()},{int(precio_n_p)},{int(cantidad_n_p)}\n")

#----------------------------------------Ejercicio 4----------------------------------------
with open("productos.txt", "r") as archivo:
    productos = [0, 1, 2, 3]
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")
    cuarta_linea = archivo.readline().strip().split(",")

    productos[0] = {"Producto" : primera_linea[0], "Precio" : primera_linea[1], "Cantidad" : primera_linea[2]}
    productos[1] = {"Producto" : segunda_linea[0], "Precio" : segunda_linea[1], "Cantidad" : segunda_linea[2]}
    productos[2] = {"Producto" : tercera_linea[0], "Precio" : tercera_linea[1], "Cantidad" : tercera_linea[2]}
    productos[3] = {"Producto" : cuarta_linea[0], "Precio" : cuarta_linea[1], "Cantidad" : cuarta_linea[2]}

    print(productos)

#----------------------------------------Ejercicio 5----------------------------------------
with open("productos.txt", "r") as archivo:
    productos = [0, 1, 2, 3]
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")
    cuarta_linea = archivo.readline().strip().split(",")

    productos[0] = {"Producto" : primera_linea[0], "Precio" : primera_linea[1], "Cantidad" : primera_linea[2]}
    productos[1] = {"Producto" : segunda_linea[0], "Precio" : segunda_linea[1], "Cantidad" : segunda_linea[2]}
    productos[2] = {"Producto" : tercera_linea[0], "Precio" : tercera_linea[1], "Cantidad" : tercera_linea[2]}
    productos[3] = {"Producto" : cuarta_linea[0], "Precio" : cuarta_linea[1], "Cantidad" : cuarta_linea[2]}

    bandera = False
    busqueda = input("Por favor, ingrese el nombre de un producto que desea chequear: ")
    while busqueda == "":
        busqueda = input("Por favor, ingrese el nombre de un producto válido: ")
    
    for i in range(len(productos)):
        if busqueda == productos[i]["Producto"]:
            print(f"Producto: {productos[i]["Producto"].title()} | Precio: ${productos[i]["Precio"]} | Cantidad: {productos[i]["Cantidad"]}")
            bandera = True
        
    if bandera == False:
        print(f"El producto {busqueda} no se encuentra en la lista de productos.")

#----------------------------------------Ejercicio 6----------------------------------------
with open("productos.txt", "r") as archivo:
    productos = [0, 1, 2, 3]
    encabezado = archivo.readline().strip()
    primera_linea = archivo.readline().strip().split(",")
    segunda_linea = archivo.readline().strip().split(",")
    tercera_linea = archivo.readline().strip().split(",")
    cuarta_linea = archivo.readline().strip().split(",")

    productos[0] = {"Producto" : primera_linea[0], "Precio" : primera_linea[1], "Cantidad" : primera_linea[2]}
    productos[1] = {"Producto" : segunda_linea[0], "Precio" : segunda_linea[1], "Cantidad" : segunda_linea[2]}
    productos[2] = {"Producto" : tercera_linea[0], "Precio" : tercera_linea[1], "Cantidad" : tercera_linea[2]}
    productos[3] = {"Producto" : cuarta_linea[0], "Precio" : cuarta_linea[1], "Cantidad" : cuarta_linea[2]}

with open("productos.txt", "r") as archivo:

    productos_lista = []
    for i in range(len(productos)):
        productos_lista.append(f"{productos[i]["Producto"]},{productos[i]["Precio"]},{productos[i]["Cantidad"]}\n") 
    
    decision = input("¿Desea agregar un producto a la lista? S/N: ")
    while decision.lower() not in ("s", "n"):
        decision = input("Por favor, ingrese una opción válida. S/N:")
    
    while decision.lower() == "s":
        n_p = input("Ingrese el nombre del producto a agregar: ")
        while n_p == "" or n_p.lower() in [productos_lista[i].split(",")[0] for i in range(len(productos_lista))]:
            n_p = input("Es posible que el producto ingresado ya exista en la lista. Intente con otro: ")
        
        p_p = input("Ingrese el precio del producto a ingresar: ")
        while p_p == "" or not p_p.isdigit():
            p_p = input("Ingrese un valor válido para el precio: ")
        
        c_p = input("Ingrese la cantidad de unidades del producto a ingresar: ")
        while c_p == "" or not c_p.isdigit():
            c_p = input("Ingrese un valor válido para la cantidad de unidades: ")
        
        productos_lista.append(f"{n_p},{p_p},{c_p}\n")

        decision = input("¿Desea agregar otro producto? S/N: ")
        while decision.lower() not in ("s", "n"):
            decision = input("Por favor, ingrese una opción válida. S/N:")
        
    print("¡Adiós!")

with open("productos.txt", "w") as archivo:
    archivo.write("producto,precio,cantidad\n")
    archivo.writelines(productos_lista)
inventario = []

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por ID")
    print("5. Calcular Valor Total del Inventario")
    print("6. Salir")

def agregar_producto():
    idProducto = int(input("Ingrese el ID del producto: "))
    nombreProducto = input("Ingrese el nombre del producto: ")
    cantidadProducto = int(input("Ingrese la cantidad del producto: "))
    precioProducto = float(input("Ingrese el precio del producto: "))
    
    producto = {
        "id": id_producto,
        "nombre": nombre_producto,
        "cantidad": cantidad_producto,
        "precio": precio_producto
    }
    inventario.append(producto)
    print("Producto agregado con éxito.")

def eliminar_producto():
    idProducto = int(input("Ingrese el ID del producto a eliminar: "))
    for producto in inventario:
        if producto["id"] == id_producto:
            inventario.remove(producto)
            print("Producto eliminado con éxito.")
            return
    print("No se encontró ningún producto con ese ID.")

def actualizar_producto():
    idProducto = int(input("Ingrese el ID del producto a actualizar: "))
    for producto in inventario:
        if producto["id"] == id_producto:
            nombreProducto = input("Ingrese el nuevo nombre del producto: ")
            cantidadProducto = int(input("Ingrese la nueva cantidad del producto: "))
            precioProducto = float(input("Ingrese el nuevo precio del producto: "))
            producto["nombre"] = nombre_producto
            producto["cantidad"] = cantidad_producto
            producto["precio"] = precio_producto
            print("Producto actualizado con éxito.")
            return
    print("No se encontró ningún producto con ese ID.")

def buscarProductoPorId():
    idProducto = int(input("Ingrese el ID del producto a buscar: "))
    for producto in inventario:
        if producto["id"] == id_producto:
            print("ID:", producto["id"])
            print("Nombre:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])
            print("Precio:", producto["precio"])
            return
    print("No se encontró ningún producto con ese ID.")

def calcular_valor_total():
    total = sum(producto["cantidad"] * producto["precio"] for producto in inventario)
    print("El valor total del inventario es:", total)

# Menú principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        buscar_producto_por_id()
    elif opcion == "5":
        calcular_valor_total()
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

from tabulate import tabulate
from datetime import datetime
from clases.cliente import ClienteRegular, ClienteVIP, ClienteCorporativo
from clases.producto import Producto
from clases.carrito import Carrito, ItemCarrito
from clases.compra import Compra
from utils.file_operations import cargar_clientes, cargar_productos, guardar_clientes, guardar_productos, \
    guardar_compra, cargar_compras


def mostrar_menu(menu):
    headers = ["Opción", "Descripción"]
    table = [[key, value] for key, value in menu.items()]
    print(tabulate(table, headers, tablefmt="grid"))


def obtener_datos_comunes():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    return nombre, apellido, email, telefono


def agregar_cliente(clientes):
    tipo_cliente_menu = {
        "1": "Cliente Regular",
        "2": "Cliente VIP",
        "3": "Cliente Corporativo"
    }
    print("\nTipos de Cliente")
    mostrar_menu(tipo_cliente_menu)
    tipo_cliente = input("Seleccione el tipo de cliente: ")

    nombre, apellido, email, telefono = obtener_datos_comunes()

    if tipo_cliente == '1':
        frecuencia_compra = input("Frecuencia de Compra (veces por mes): ")
        cliente = ClienteRegular(nombre, apellido, email, telefono, frecuencia_compra)
    elif tipo_cliente == '2':
        descuento = input("Descuento (%): ")
        puntos = input("Puntos: ")
        cliente = ClienteVIP(nombre, apellido, email, telefono, descuento, puntos)
    elif tipo_cliente == '3':
        empresa = input("Empresa: ")
        descuento_corporativo = input("Descuento Corporativo (%): ")
        cliente = ClienteCorporativo(nombre, apellido, email, telefono, empresa, descuento_corporativo)
    else:
        print("Tipo de cliente no válido.")
        return

    clientes.append(cliente)
    print("Cliente agregado exitosamente.")
    guardar_clientes(clientes)


def mostrar_clientes(clientes):
    headers = ["#", "Nombre", "Apellido", "Email", "Teléfono", "Detalles"]
    table = []
    for i, cliente in enumerate(clientes):
        if isinstance(cliente, ClienteRegular):
            detalles = f"Frecuencia de Compra: {cliente.frecuencia_compra} veces por mes"
        elif isinstance(cliente, ClienteVIP):
            detalles = f"Descuento: {cliente.descuento}%, Puntos: {cliente.puntos}"
        elif isinstance(cliente, ClienteCorporativo):
            detalles = f"Empresa: {cliente.empresa}, Descuento Corporativo: {cliente.descuento_corporativo}%"
        else:
            detalles = ""
        table.append([i + 1, cliente.nombre, cliente.apellido, cliente.email, cliente.telefono, detalles])
    print(tabulate(table, headers, tablefmt="grid"))


def modificar_cliente(clientes):
    mostrar_clientes(clientes)
    try:
        indice_cliente = int(input("Ingrese el número del cliente a modificar: ")) - 1
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de cliente no válido.")
        return
    cliente = clientes[indice_cliente]
    print(f"Modificando cliente: {cliente}")
    nombre, apellido, email, telefono = obtener_datos_comunes()
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.email = email
    cliente.telefono = telefono
    guardar_clientes(clientes)
    print("Cliente modificado exitosamente.")


def eliminar_cliente(clientes):
    mostrar_clientes(clientes)
    try:
        indice_cliente = int(input("Ingrese el número del cliente a eliminar: ")) - 1
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de cliente no válido.")
        return
    clientes.pop(indice_cliente)
    guardar_clientes(clientes)
    print("Cliente eliminado exitosamente.")


def agregar_producto(productos):
    nombre_producto = input("Nombre del Producto: ")
    try:
        precio_producto = float(input("Precio del Producto: "))
    except ValueError:
        print("Precio inválido. Intente nuevamente.")
        return
    producto = Producto(nombre_producto, precio_producto)
    productos.append(producto)
    print("Producto agregado exitosamente.")
    guardar_productos(productos)


def mostrar_productos(productos):
    headers = ["#", "Nombre", "Precio"]
    table = [[i + 1, producto.nombre, f"${producto.precio:.2f}"] for i, producto in enumerate(productos)]
    print(tabulate(table, headers, tablefmt="grid"))


def modificar_producto(productos):
    mostrar_productos(productos)
    try:
        indice_producto = int(input("Ingrese el número del producto a modificar: ")) - 1
        if indice_producto < 0 or indice_producto >= len(productos):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de producto no válido.")
        return
    producto = productos[indice_producto]
    print(f"Modificando producto: {producto}")
    nombre_producto = input("Nuevo nombre del producto: ")
    try:
        precio_producto = float(input("Nuevo precio del producto: "))
    except ValueError:
        print("Precio inválido. Intente nuevamente.")
        return
    producto.nombre = nombre_producto
    producto.precio = precio_producto
    guardar_productos(productos)
    print("Producto modificado exitosamente.")


def eliminar_producto(productos):
    mostrar_productos(productos)
    try:
        indice_producto = int(input("Ingrese el número del producto a eliminar: ")) - 1
        if indice_producto < 0 or indice_producto >= len(productos):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de producto no válido.")
        return
    productos.pop(indice_producto)
    guardar_productos(productos)
    print("Producto eliminado exitosamente.")


def agregar_al_carrito(productos, carrito):
    print("\nSeleccione un Producto")
    mostrar_productos(productos)
    try:
        indice_producto = int(input("Ingrese el número del producto: ")) - 1
        if indice_producto < 0 or indice_producto >= len(productos):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de producto no válido.")
        return
    producto = productos[indice_producto]
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print("Cantidad inválida. Intente nuevamente.")
        return
    carrito.agregar_item(producto, cantidad)
    print(f"{producto.nombre} agregado al carrito.")


def registrar_compra(clientes, productos):
    if not clientes:
        print("No hay clientes registrados.")
        return
    if not productos:
        print("No hay productos registrados.")
        return

    print("\nSeleccione un Cliente")
    mostrar_clientes(clientes)
    try:
        indice_cliente = int(input("Ingrese el número del cliente: ")) - 1
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de cliente no válido.")
        return
    cliente = clientes[indice_cliente]

    carrito = Carrito()
    while True:
        agregar_al_carrito(productos, carrito)
        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    if carrito.items:
        compra = Compra(indice_cliente, carrito, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        guardar_compra(compra)
        print(f"\nRecibo de Compra:\n{compra}\n")
        print(f"Compra registrada para {cliente.nombre}.")
    else:
        print("Carrito vacío. No se registró ninguna compra.")


def mostrar_compras(clientes):
    compras = cargar_compras()
    if not clientes:
        print("No hay clientes registrados.")
        return
    if not compras:
        print("No hay compras registradas.")
        return

    print("\nSeleccione un Cliente")
    mostrar_clientes(clientes)
    try:
        indice_cliente = int(input("Ingrese el número del cliente: ")) - 1
        if indice_cliente < 0 or indice_cliente >= len(clientes):
            raise IndexError
    except (ValueError, IndexError):
        print("Índice de cliente no válido.")
        return
    cliente = clientes[indice_cliente]

    headers = ["Carrito", "Fecha"]
    table = [[compra.carrito, compra.fecha] for compra in compras if compra.cliente_id == indice_cliente]
    print(f"Compras de {cliente.nombre}:")
    print(tabulate(table, headers, tablefmt="grid"))


def menu_principal(clientes, productos):
    menu = {
        "1": "Cliente",
        "2": "Administrador",
        "3": "Salir"
    }
    while True:
        print("\nMenú Principal")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            menu_cliente(clientes, productos)
        elif opcion == '2':
            menu_administrador(clientes, productos)
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


def menu_cliente(clientes, productos):
    menu = {
        "1": "Realizar Compra",
        "2": "Mostrar Compras",
        "3": "Volver al Menú Principal"
    }
    while True:
        print("\nMenú Cliente")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            registrar_compra(clientes, productos)
        elif opcion == '2':
            mostrar_compras(clientes)
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


def menu_administrador(clientes, productos):
    menu = {
        "1": "Agregar Cliente",
        "2": "Modificar Cliente",
        "3": "Eliminar Cliente",
        "4": "Agregar Producto",
        "5": "Modificar Producto",
        "6": "Eliminar Producto",
        "7": "Mostrar Clientes",
        "8": "Mostrar Productos",
        "9": "Volver al Menú Principal"
    }
    while True:
        print("\nMenú Administrador")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            modificar_cliente(clientes)
        elif opcion == '3':
            eliminar_cliente(clientes)
        elif opcion == '4':
            agregar_producto(productos)
        elif opcion == '5':
            modificar_producto(productos)
        elif opcion == '6':
            eliminar_producto(productos)
        elif opcion == '7':
            mostrar_clientes(clientes)
        elif opcion == '8':
            mostrar_productos(productos)
        elif opcion == '9':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

from clases.producto import Producto
from utils.file_operations import guardar_productos, cargar_productos
from tabulate import tabulate


def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    # Check if the product already exists
    for producto in productos:
        if producto.nombre == nombre:
            print("El producto ya existe. Por favor, elija otro nombre.")
            return
    try:
        precio_producto = float(input("Precio del Producto: "))
    except ValueError:
        print("Precio inválido. Intente nuevamente.")
        return

    descripcion = input("Descripción del producto: ")

    try:
        cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("Cantidad inválida. Intente nuevamente.")
        return

    producto = Producto(nombre, descripcion, precio_producto, cantidad)
    productos.append(producto)
    print("Producto agregado exitosamente.")
    guardar_productos(productos)


def mostrar_productos(productos):
    headers = ["#", "Nombre", "Descripción", "Precio", "Cantidad"]
    table = []
    for i, producto in enumerate(productos):
        table.append([i + 1, producto.nombre, producto.descripcion, producto.precio, producto.cantidad])
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
    print(f"Modificando producto: {producto.nombre}")
    producto.nombre = input("Nombre del producto: ")
    producto.descripcion = input("Descripción del producto: ")
    try:
        producto.precio = float(input("Precio del producto: "))
        producto.cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("Precio o  Cantidad no válido.")
        return
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

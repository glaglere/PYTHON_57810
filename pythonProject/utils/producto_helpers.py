from clases.producto import Producto
from utils.file_operations import guardar_productos
from utils.menu_helpers import mostrar_menu
from tabulate import tabulate


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

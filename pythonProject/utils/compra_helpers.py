from datetime import datetime
from tabulate import tabulate

from clases.carrito import Carrito
from clases.compra import Compra
from utils.cliente_helpers import mostrar_clientes
from utils.file_operations import guardar_compra, cargar_compras
from utils.menu_helpers import mostrar_menu
from utils.producto_helpers import mostrar_productos

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

def mostrar_compras(cliente):
    compras = cargar_compras()
    if not compras:
        print("No hay compras registradas.")
        return

    headers = ["Carrito", "Fecha"]
    table = [[compra.carrito, compra.fecha] for compra in compras if compra.cliente_id == cliente]
    print(f"Compras de {cliente.nombre}:")
    print(tabulate(table, headers, tablefmt="grid"))

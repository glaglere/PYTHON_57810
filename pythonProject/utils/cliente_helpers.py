from tabulate import tabulate

from utils.file_operations import guardar_clientes
from utils.menu_helpers import mostrar_menu
from clases.cliente import ClienteRegular, ClienteVIP, ClienteCorporativo

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

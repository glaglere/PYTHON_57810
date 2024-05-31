import bcrypt
# import stdiomask
from tabulate import tabulate

from clases.cliente import ClienteRegular, ClienteVIP, ClienteCorporativo
from utils.file_operations import guardar_clientes
from utils.menu_helpers import mostrar_menu


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
    username = input("Nombre de usuario: ")

    # Check if the username or email already exists
    for cliente in clientes:
        if cliente.username == username:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
            return
        if cliente.email == email:
            print("El email ya está registrado. Por favor, use otro email.")
            return

    # password = stdiomask.getpass(prompt="Contraseña: ")
    # confirmar_password = stdiomask.getpass(prompt="Confirmar contraseña: ")

    password = input("Contraseña: ")
    confirmar_password = input("Confirmar contraseña: ")

    if password != confirmar_password:
        print("Las contraseñas no coinciden. Intente nuevamente.")
        return

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    if tipo_cliente == '1':
        frecuencia_compra = input("Frecuencia de Compra (veces por mes): ")
        cliente = ClienteRegular(nombre, apellido, email, telefono, username, password_hash, frecuencia_compra)
    elif tipo_cliente == '2':
        descuento = input("Descuento (%): ")
        puntos = input("Puntos: ")
        cliente = ClienteVIP(nombre, apellido, email, telefono, username, password_hash, descuento, puntos)
    elif tipo_cliente == '3':
        empresa = input("Empresa: ")
        descuento_corporativo = input("Descuento Corporativo (%): ")
        cliente = ClienteCorporativo(nombre, apellido, email, telefono, username, password_hash, empresa,
                                     descuento_corporativo)
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


def registrar_cliente(clientes):
    print("Registro de nuevo cliente")
    agregar_cliente(clientes)


def iniciar_sesion(clientes):
    print("Inicio de sesión")
    username = input("Nombre de usuario: ")
    # password = stdiomask.getpass(prompt="Contraseña: ")
    password = input(prompt="Contraseña: ")

    for cliente in clientes:
        if cliente.username == username and bcrypt.checkpw(password.encode('utf-8'), cliente.password.encode('utf-8')):
            print(f"Bienvenido, {cliente.nombre} {cliente.apellido}!")
            return cliente

    print("Usuario o contraseña incorrectos.")
    return None


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

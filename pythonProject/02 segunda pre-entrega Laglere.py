import json
from tabulate import tabulate
from datetime import datetime


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def to_dict(self):
        return {"nombre": self.nombre, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["nombre"], data["precio"])

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"


class Compra:
    def __init__(self, producto, fecha):
        self.producto = producto
        self.fecha = fecha

    def to_dict(self):
        return {"producto": self.producto.to_dict(), "fecha": self.fecha}

    @staticmethod
    def from_dict(data):
        producto = Producto.from_dict(data["producto"])
        return Compra(producto, data["fecha"])

    def __str__(self):
        return f"{self.producto.nombre} - ${self.producto.precio:.2f} (Fecha: {self.fecha})"


class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.compras = []

    def registrar_compra(self, producto):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        compra = Compra(producto, fecha)
        self.compras.append(compra)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "compras": [compra.to_dict() for compra in self.compras]
        }

    @staticmethod
    def from_dict(data):
        cliente = Cliente(data["nombre"], data["apellido"], data["email"], data["telefono"])
        cliente.compras = [Compra.from_dict(compra) for compra in data["compras"]]
        return cliente

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"


class ClienteRegular(Cliente):
    def __init__(self, nombre, apellido, email, telefono, frecuencia_compra):
        super().__init__(nombre, apellido, email, telefono)
        self.frecuencia_compra = frecuencia_compra

    def to_dict(self):
        data = super().to_dict()
        data["frecuencia_compra"] = self.frecuencia_compra
        data["tipo"] = "ClienteRegular"
        return data

    @staticmethod
    def from_dict(data):
        cliente = ClienteRegular(data["nombre"], data["apellido"], data["email"], data["telefono"],
                                 data["frecuencia_compra"])
        cliente.compras = [Compra.from_dict(compra) for compra in data["compras"]]
        return cliente

    def __str__(self):
        return f"{super().__str__()}, Frecuencia de Compra: {self.frecuencia_compra} veces por mes"


class ClienteVIP(Cliente):
    def __init__(self, nombre, apellido, email, telefono, descuento, puntos):
        super().__init__(nombre, apellido, email, telefono)
        self.descuento = descuento
        self.puntos = puntos

    def to_dict(self):
        data = super().to_dict()
        data["descuento"] = self.descuento
        data["puntos"] = self.puntos
        data["tipo"] = "ClienteVIP"
        return data

    @staticmethod
    def from_dict(data):
        cliente = ClienteVIP(data["nombre"], data["apellido"], data["email"], data["telefono"], data["descuento"],
                             data["puntos"])
        cliente.compras = [Compra.from_dict(compra) for compra in data["compras"]]
        return cliente

    def __str__(self):
        return f"{super().__str__()}, Descuento: {self.descuento}%, Puntos: {self.puntos}"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, apellido, email, telefono, empresa, descuento_corporativo):
        super().__init__(nombre, apellido, email, telefono)
        self.empresa = empresa
        self.descuento_corporativo = descuento_corporativo

    def to_dict(self):
        data = super().to_dict()
        data["empresa"] = self.empresa
        data["descuento_corporativo"] = self.descuento_corporativo
        data["tipo"] = "ClienteCorporativo"
        return data

    @staticmethod
    def from_dict(data):
        cliente = ClienteCorporativo(data["nombre"], data["apellido"], data["email"], data["telefono"], data["empresa"],
                                     data["descuento_corporativo"])
        cliente.compras = [Compra.from_dict(compra) for compra in data["compras"]]
        return cliente

    def __str__(self):
        return f"{super().__str__()}, Empresa: {self.empresa}, Descuento Corporativo: {self.descuento_corporativo}%"


# Función auxiliar para recolectar datos comunes
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


def agregar_producto(productos):
    nombre_producto = input("Nombre del Producto: ")
    precio_producto = float(input("Precio del Producto: "))
    producto = Producto(nombre_producto, precio_producto)
    productos.append(producto)
    print("Producto agregado exitosamente.")
    guardar_productos(productos)


def mostrar_productos(productos):
    headers = ["Nombre", "Precio"]
    table = [[producto.nombre, f"${producto.precio:.2f}"] for producto in productos]
    print(tabulate(table, headers, tablefmt="grid"))


def registrar_compra(clientes, productos):
    if not clientes:
        print("No hay clientes registrados.")
        return
    if not productos:
        print("No hay productos registrados.")
        return

    print("\nSeleccione un Cliente")
    mostrar_clientes(clientes)
    indice_cliente = int(input("Ingrese el número del cliente: ")) - 1
    if indice_cliente < 0 or indice_cliente >= len(clientes):
        print("Índice de cliente no válido.")
        return
    cliente = clientes[indice_cliente]

    print("\nSeleccione un Producto")
    mostrar_productos(productos)
    nombre_producto = input("Nombre del Producto: ")
    producto = next((p for p in productos if p.nombre == nombre_producto), None)
    if producto:
        cliente.registrar_compra(producto)
        print(f"Compra registrada: {cliente.nombre} ha comprado {producto.nombre}")
        guardar_clientes(clientes)
    else:
        print("Producto no encontrado.")


def mostrar_compras(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return

    print("\nSeleccione un Cliente")
    mostrar_clientes(clientes)
    indice_cliente = int(input("Ingrese el número del cliente: ")) - 1
    if indice_cliente < 0 or indice_cliente >= len(clientes):
        print("Índice de cliente no válido.")
        return
    cliente = clientes[indice_cliente]

    headers = ["Nombre del Producto", "Precio", "Fecha"]
    table = [[compra.producto.nombre, f"${compra.producto.precio:.2f}", compra.fecha] for compra in cliente.compras]
    print(f"Compras de {cliente.nombre}:")
    print(tabulate(table, headers, tablefmt="grid"))


def mostrar_menu(menu):
    headers = ["Opción", "Descripción"]
    table = [[key, value] for key, value in menu.items()]
    print(tabulate(table, headers, tablefmt="grid"))


def guardar_clientes(clientes):
    with open('clientes.json', 'w') as file:
        json.dump([cliente.to_dict() for cliente in clientes], file, indent=4)


def cargar_clientes():
    try:
        with open('clientes.json', 'r') as file:
            clientes_data = json.load(file)
            clientes = []
            for data in clientes_data:
                if data["tipo"] == "ClienteRegular":
                    clientes.append(ClienteRegular.from_dict(data))
                elif data["tipo"] == "ClienteVIP":
                    clientes.append(ClienteVIP.from_dict(data))
                elif data["tipo"] == "ClienteCorporativo":
                    clientes.append(ClienteCorporativo.from_dict(data))
            return clientes
    except FileNotFoundError:
        return []


def guardar_productos(productos):
    with open('productos.json', 'w') as file:
        json.dump([producto.to_dict() for producto in productos], file, indent=4)


def cargar_productos():
    try:
        with open('productos.json', 'r') as file:
            productos_data = json.load(file)
            return [Producto.from_dict(data) for data in productos_data]
    except FileNotFoundError:
        return []


def main():
    clientes = cargar_clientes()
    productos = cargar_productos()

    menu = {
        "1": "Agregar Cliente",
        "2": "Mostrar Clientes",
        "3": "Agregar Producto",
        "4": "Mostrar Productos",
        "5": "Registrar Compra",
        "6": "Mostrar Compras de Cliente",
        "7": "Salir"
    }

    while True:
        print("\nMenú Principal")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            mostrar_clientes(clientes)
        elif opcion == '3':
            agregar_producto(productos)
        elif opcion == '4':
            mostrar_productos(productos)
        elif opcion == '5':
            registrar_compra(clientes, productos)
        elif opcion == '6':
            mostrar_compras(clientes)
        elif opcion == '7':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()

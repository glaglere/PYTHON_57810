from tabulate import tabulate


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"


class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.compras = []

    def registrar_compra(self, producto):
        self.compras.append(producto)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"


class ClienteRegular(Cliente):
    def __init__(self, nombre, apellido, email, telefono, frecuencia_compra):
        super().__init__(nombre, apellido, email, telefono)
        self.frecuencia_compra = frecuencia_compra

    def __str__(self):
        return f"{super().__str__()}, Frecuencia de Compra: {self.frecuencia_compra} veces por mes"


class ClienteVIP(Cliente):
    def __init__(self, nombre, apellido, email, telefono, descuento, puntos):
        super().__init__(nombre, apellido, email, telefono)
        self.descuento = descuento
        self.puntos = puntos

    def __str__(self):
        return f"{super().__str__()}, Descuento: {self.descuento}%, Puntos: {self.puntos}"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, apellido, email, telefono, empresa, descuento_corporativo):
        super().__init__(nombre, apellido, email, telefono)
        self.empresa = empresa
        self.descuento_corporativo = descuento_corporativo

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
    print("\n1. Cliente Regular")
    print("2. Cliente VIP")
    print("3. Cliente Corporativo")
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


def mostrar_clientes(clientes):
    headers = ["Nombre", "Apellido", "Email", "Teléfono", "Detalles"]
    table = []
    for cliente in clientes:
        if isinstance(cliente, ClienteRegular):
            detalles = f"Frecuencia de Compra: {cliente.frecuencia_compra} veces por mes"
        elif isinstance(cliente, ClienteVIP):
            detalles = f"Descuento: {cliente.descuento}%, Puntos: {cliente.puntos}"
        elif isinstance(cliente, ClienteCorporativo):
            detalles = f"Empresa: {cliente.empresa}, Descuento Corporativo: {cliente.descuento_corporativo}%"
        else:
            detalles = ""
        table.append([cliente.nombre, cliente.apellido, cliente.email, cliente.telefono, detalles])
    print(tabulate(table, headers, tablefmt="grid"))


def agregar_producto(productos):
    nombre_producto = input("Nombre del Producto: ")
    precio_producto = float(input("Precio del Producto: "))
    producto = Producto(nombre_producto, precio_producto)
    productos.append(producto)
    print("Producto agregado exitosamente.")


def mostrar_productos(productos):
    headers = ["Nombre", "Precio"]
    table = [[producto.nombre, f"${producto.precio:.2f}"] for producto in productos]
    print(tabulate(table, headers, tablefmt="grid"))


def registrar_compra(clientes, productos):
    email_cliente = input("Email del Cliente: ")
    nombre_producto = input("Nombre del Producto: ")
    cliente = next((c for c in clientes if c.email == email_cliente), None)
    producto = next((p for p in productos if p.nombre == nombre_producto), None)
    if cliente and producto:
        cliente.registrar_compra(producto)
        print(f"Compra registrada: {cliente.nombre} ha comprado {producto.nombre}")
    else:
        print("Cliente o producto no encontrado.")


def mostrar_compras(clientes):
    email_cliente = input("Email del Cliente: ")
    cliente = next((c for c in clientes if c.email == email_cliente), None)
    if cliente:
        headers = ["Nombre del Producto", "Precio"]
        table = [[compra.nombre, f"${compra.precio:.2f}"] for compra in cliente.compras]
        print(f"Compras de {cliente.nombre}:")
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print("Cliente no encontrado.")


def main():
    clientes = []
    productos = []

    while True:
        print("\nMenú Principal")
        print(tabulate(
            [["1. Agregar Cliente"], ["2. Mostrar Clientes"], ["3. Agregar Producto"], ["4. Mostrar Productos"],
             ["5. Registrar Compra"], ["6. Mostrar Compras de Cliente"], ["7. Salir"]], tablefmt="grid"))

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

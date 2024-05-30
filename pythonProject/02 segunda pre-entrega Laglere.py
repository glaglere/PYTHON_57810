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


def main():
    clientes = []
    productos = []

    while True:
        print("\n1. Agregar Cliente Regular")
        print("2. Agregar Cliente VIP")
        print("3. Agregar Cliente Corporativo")
        print("4. Mostrar Clientes")
        print("5. Agregar Producto")
        print("6. Mostrar Productos")
        print("7. Registrar Compra")
        print("8. Mostrar Compras de Cliente")
        print("9. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            nombre, apellido, email, telefono = obtener_datos_comunes()
            frecuencia_compra = input("Frecuencia de Compra (veces por mes): ")
            cliente = ClienteRegular(nombre, apellido, email, telefono, frecuencia_compra)
            clientes.append(cliente)
        elif opcion == '2':
            nombre, apellido, email, telefono = obtener_datos_comunes()
            descuento = input("Descuento (%): ")
            puntos = input("Puntos: ")
            cliente = ClienteVIP(nombre, apellido, email, telefono, descuento, puntos)
            clientes.append(cliente)
        elif opcion == '3':
            nombre, apellido, email, telefono = obtener_datos_comunes()
            empresa = input("Empresa: ")
            descuento_corporativo = input("Descuento Corporativo (%): ")
            cliente = ClienteCorporativo(nombre, apellido, email, telefono, empresa, descuento_corporativo)
            clientes.append(cliente)
        elif opcion == '4':
            for cliente in clientes:
                print(cliente)
        elif opcion == '5':
            nombre_producto = input("Nombre del Producto: ")
            precio_producto = float(input("Precio del Producto: "))
            producto = Producto(nombre_producto, precio_producto)
            productos.append(producto)
        elif opcion == '6':
            for producto in productos:
                print(producto)
        elif opcion == '7':
            email_cliente = input("Email del Cliente: ")
            nombre_producto = input("Nombre del Producto: ")
            cliente = next((c for c in clientes if c.email == email_cliente), None)
            producto = next((p for p in productos if p.nombre == nombre_producto), None)
            if cliente and producto:
                cliente.registrar_compra(producto)
                print(f"Compra registrada: {cliente.nombre} ha comprado {producto.nombre}")
            else:
                print("Cliente o producto no encontrado.")
        elif opcion == '8':
            email_cliente = input("Email del Cliente: ")
            cliente = next((c for c in clientes if c.email == email_cliente), None)
            if cliente:
                print(f"Compras de {cliente.nombre}:")
                for compra in cliente.compras:
                    print(compra)
            else:
                print("Cliente no encontrado.")
        elif opcion == '9':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()

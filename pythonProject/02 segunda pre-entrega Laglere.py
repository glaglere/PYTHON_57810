class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

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

    while True:
        print("\n1. Agregar Cliente Regular")
        print("2. Agregar Cliente VIP")
        print("3. Agregar Cliente Corporativo")
        print("4. Mostrar Clientes")
        print("5. Salir")

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
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()

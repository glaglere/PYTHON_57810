class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cliente1 = Cliente("Ginette", "Laglere","glaglere@gmail.com","099-123456")
    print(cliente1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

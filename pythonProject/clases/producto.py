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

# from .producto.py import Producto
from clases.producto import Producto


class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def to_dict(self):
        return {"producto": self.producto.to_dict(), "cantidad": self.cantidad}

    @staticmethod
    def from_dict(data):
        producto = Producto.from_dict(data["producto"])
        return ItemCarrito(producto, data["cantidad"])

    def __str__(self):
        return f"{self.producto.nombre} - ${self.producto.precio:.2f} x {self.cantidad}"


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        self.items.append(ItemCarrito(producto, cantidad))

    def vaciar_carrito(self):
        self.items = []

    def total(self):
        return sum(item.producto.precio * item.cantidad for item in self.items)

    def to_dict(self):
        return {"items": [item.to_dict() for item in self.items]}

    @staticmethod
    def from_dict(data):
        carrito = Carrito()
        carrito.items = [ItemCarrito.from_dict(item) for item in data["items"]]
        return carrito

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

from .carrito import Carrito

class Compra:
    def __init__(self, cliente_id, carrito, fecha):
        self.cliente_id = cliente_id
        self.carrito = carrito
        self.fecha = fecha

    def to_dict(self):
        return {"cliente_id": self.cliente_id, "carrito": self.carrito.to_dict(), "fecha": self.fecha}

    @staticmethod
    def from_dict(data):
        carrito = Carrito.from_dict(data["carrito"])
        return Compra(data["cliente_id"], carrito, data["fecha"])

    def __str__(self):
        recibo = []
        recibo.append(f"Fecha: {self.fecha}")
        recibo.append(f"Cliente ID: {self.cliente_id}")
        recibo.append("-" * 40)
        recibo.append("{:<20} {:<10} {:<10}".format("Producto", "Cantidad", "Precio"))
        recibo.append("-" * 40)
        for item in self.carrito.items:
            recibo.append("{:<20} {:<10} ${:<10.2f}".format(item.producto.nombre, item.cantidad, item.producto.precio * item.cantidad))
        recibo.append("-" * 40)
        recibo.append("{:<20} {:<10} ${:<10.2f}".format("Total a pagar", "", self.carrito.total()))
        return "\n".join(recibo)

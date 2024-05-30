from tabulate import tabulate
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
        # Datos de la cabecera del recibo
        cabecera = [
            ["Fecha:", self.fecha],
            ["Cliente ID:", self.cliente_id]
        ]

        # Crear tabla de productos con columnas adicionales
        productos = [[item.producto.nombre, item.cantidad, f"${item.producto.precio:.2f}",
                      f"${item.producto.precio * item.cantidad:.2f}"] for item in self.carrito.items]

        # Calcular total general
        total_general = self.carrito.total()

        # Formatear las tablas usando tabulate
        recibo = tabulate(cabecera, tablefmt="plain")
        recibo += "\n" + "-" * 40
        recibo += "\n" + tabulate(productos, headers=["Producto", "Cantidad", "Precio Unitario", "Total"],
                                  tablefmt="plain")
        recibo += "\n" + "-" * 40
        recibo += f"\n{'Total a pagar':<30} ${total_general:.2f}"

        return recibo

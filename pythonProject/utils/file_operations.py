import json
from clases.cliente import ClienteRegular, ClienteVIP, ClienteCorporativo
from clases.producto import Producto
from clases.compra import Compra


import json
from clases.cliente import ClienteRegular, ClienteVIP, ClienteCorporativo, Cliente

def guardar_clientes(clientes):
    with open('clientes.json', 'w', encoding='utf-8') as file:
        json.dump([cliente.to_dict() for cliente in clientes], file, indent=4, ensure_ascii=False)

def cargar_clientes():
    try:
        with open('clientes.json', 'r', encoding='utf-8') as file:
            clientes_data = json.load(file)
            clientes = []
            for data in clientes_data:
                if data["tipo"] == "ClienteRegular":
                    clientes.append(ClienteRegular.from_dict(data))
                elif data["tipo"] == "ClienteVIP":
                    clientes.append(ClienteVIP.from_dict(data))
                elif data["tipo"] == "ClienteCorporativo":
                    clientes.append(ClienteCorporativo.from_dict(data))
                else:
                    clientes.append(Cliente.from_dict(data))  # Fallback to base Cliente if type is not recognized
            return clientes
    except FileNotFoundError:
        return []


def guardar_productos(productos):
    with open('productos.json', 'w', encoding='utf-8') as file:
        json.dump([producto.to_dict() for producto in productos], file, indent=4, ensure_ascii=False)


def cargar_productos():
    try:
        with open('productos.json', 'r', encoding='utf-8') as file:
            productos_data = json.load(file)
            return [Producto.from_dict(data) for data in productos_data]
    except FileNotFoundError:
        return []


def guardar_compra(compra):
    try:
        compras = cargar_compras()
    except FileNotFoundError:
        compras = []
    compras.append(compra)
    with open('compras.json', 'w', encoding='utf-8') as file:
        json.dump([comp.to_dict() for comp in compras], file, indent=4, ensure_ascii=False)


def cargar_compras():
    try:
        with open('compras.json', 'r', encoding='utf-8') as file:
            compras_data = json.load(file)
            return [Compra.from_dict(data) for data in compras_data]
    except FileNotFoundError:
        return []

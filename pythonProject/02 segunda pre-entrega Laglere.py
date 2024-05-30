from utils.file_operations import cargar_clientes, cargar_productos
from utils.menu_principal import menu_principal

if __name__ == "__main__":
    clientes = cargar_clientes()
    productos = cargar_productos()
    menu_principal(clientes, productos)

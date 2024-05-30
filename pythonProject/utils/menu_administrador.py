from utils.menu_helpers import mostrar_menu
from utils.cliente_helpers import agregar_cliente, modificar_cliente, eliminar_cliente, mostrar_clientes
from utils.producto_helpers import agregar_producto, modificar_producto, eliminar_producto, mostrar_productos

def menu_administrador(clientes, productos):
    menu = {
        "1": "Agregar Cliente",
        "2": "Modificar Cliente",
        "3": "Eliminar Cliente",
        "4": "Agregar Producto",
        "5": "Modificar Producto",
        "6": "Eliminar Producto",
        "7": "Mostrar Clientes",
        "8": "Mostrar Productos",
        "9": "Volver al Menú Principal"
    }
    while True:
        print("\nMenú Administrador")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            modificar_cliente(clientes)
        elif opcion == '3':
            eliminar_cliente(clientes)
        elif opcion == '4':
            agregar_producto(productos)
        elif opcion == '5':
            modificar_producto(productos)
        elif opcion == '6':
            eliminar_producto(productos)
        elif opcion == '7':
            mostrar_clientes(clientes)
        elif opcion == '8':
            mostrar_productos(productos)
        elif opcion == '9':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

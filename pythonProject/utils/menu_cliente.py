from utils.menu_helpers import mostrar_menu
from utils.compra_helpers import registrar_compra, mostrar_compras

def menu_cliente(clientes, productos):
    menu = {
        "1": "Realizar Compra",
        "2": "Mostrar Compras",
        "3": "Volver al Menú Principal"
    }
    while True:
        print("\nMenú Cliente")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            registrar_compra(clientes, productos)
        elif opcion == '2':
            mostrar_compras(clientes)
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

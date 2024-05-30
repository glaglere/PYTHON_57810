from utils.menu_cliente import menu_cliente
from utils.menu_administrador import menu_administrador
from utils.menu_helpers import mostrar_menu

def menu_principal(clientes, productos):
    menu = {
        "1": "Cliente",
        "2": "Administrador",
        "3": "Salir"
    }
    while True:
        print("\nMenú Principal")
        mostrar_menu(menu)

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            menu_cliente(clientes, productos)
        elif opcion == '2':
            menu_administrador(clientes, productos)
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

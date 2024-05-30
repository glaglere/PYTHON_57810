from utils.menu_helpers import mostrar_menu
from utils.compra_helpers import registrar_compra, mostrar_compras
from utils.cliente_helpers import registrar_cliente, iniciar_sesion

def menu_cliente(clientes, productos):
    cliente_actual = None

    while True:
        if cliente_actual:
            menu = {
                "1": "Realizar Compra",
                "2": "Mostrar Compras",
                "3": "Cerrar Sesión"
            }
            print(f"\nMenú Cliente - {cliente_actual.nombre}")
        else:
            menu = {
                "1": "Registrarse",
                "2": "Iniciar Sesión",
                "3": "Volver al Menú Principal"
            }
            print("\nMenú Cliente")

        mostrar_menu(menu)
        opcion = input("\nSeleccione una opción: ")

        if cliente_actual:
            if opcion == '1':
                registrar_compra(clientes, productos)  # Ensure to pass the list of clients
            elif opcion == '2':
                mostrar_compras(cliente_actual)  # Here, it can pass the actual client
            elif opcion == '3':
                cliente_actual = None
                print("Sesión cerrada. Volviendo al menú anterior...")
            else:
                print("Opción no válida, por favor intente nuevamente.")
        else:
            if opcion == '1':
                registrar_cliente(clientes)
            elif opcion == '2':
                cliente_actual = iniciar_sesion(clientes)
            elif opcion == '3':
                break
            else:
                print("Opción no válida, por favor intente nuevamente.")

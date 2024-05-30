from tabulate import tabulate

def mostrar_menu(menu):
    headers = ["Opción", "Descripción"]
    table = [[key, value] for key, value in menu.items()]
    print(tabulate(table, headers, tablefmt="grid"))

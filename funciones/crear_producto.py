from ui.ventana import ventana

def crear_registro()->none:
    """Funcion para crear un nuevo registro en el inventario"""

    #Inicializacio de variables 
    nombre:str = ''
    stock:int = 0

    ventana(["Sistema de inventario",
             "",
             "CREAR NUEVO REGISTRO"])

    while not nombre or nombre.isspace():
        """ validacio del nombre del producto"""

        nombre = input("Nombre del producto: ")

        if nombre.isdigit():
            print("El nombre no puede ser un numero")
            nombre = None
        elif not nombre or nombre.isspace():
            print("El nombre no puede estar vacio")
            nombre = None

    while not stock:
        """ validacio del stock del producto"""
        
        stock = input("stock del producto: ")

        if not stock.isdigit():
            print("El stock debe ser un numero")
            stock = None
            continue

        stock = int(stock)

        if stock < 0:
            print("El stock debe ser numero mayor a cero")
            stock = None        



    input("PRODUCTO CREADO!!!!! \nPresione cualquier tecla para continuar...")


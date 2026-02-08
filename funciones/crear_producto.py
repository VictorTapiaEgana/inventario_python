from ui.ventana import ventana
from funciones.inventario import guardar_inventario

def crear_registro()->none:
    """Funcion para crear un nuevo registro en el inventario"""
    
    #Inicializacio de variables 
    nombre:str = ''
    stock:int = 0
    descr:str = ''
    valor:int = 0
    
    menu = (
            {"texto":"Sistema de inventario","align":"center"},
            {"texto":"", "align":"center"},
            {"texto":"CREAR NUEVO REGISTRO", "align":"center"}
    )
    ventana(menu)

    while not nombre or nombre.isspace():
        """ Validacio del nombre del producto """

        nombre = input("Nombre del producto o 's' para salir: ")

        if nombre.lower() == 's':
            return
        
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

    while not descr or descr.isspace():
        """ validacio del descripcion del producto"""

        descr = input("Descripcion del producto: ")

        if descr.isdigit():
            print("La descripcion no puede ser un numero")
            descr = None
        elif not descr or descr.isspace():
            print("La descripcion no puede estar vacia")
            descr = None

    while not valor:
        """ validacio del valor del producto"""
        
        valor = input("Valor del producto: ")

        if not valor.isdigit():
            print("El valor debe ser un numero")
            valor = None
            continue

        valor = int(valor)

        if valor < 0:
            print("El valor debe ser numero mayor a cero")
            valor = None        

    producto_nuevo  = {
        "nombre":nombre,
        "stock":stock,        
        "precio":valor,
        "descripcion":descr
    }
    
    guardar_inventario(producto_nuevo)

    input("PRODUCTO CREADO!!!!! \nPresione cualquier tecla para continuar...")


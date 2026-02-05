from ui.ventana import ventana

def crear_registro()->none:

    nombre:str = ''

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




    input("PRODUCTO CREADO!!!!! \nPresione cualquier tecla para continuar...")


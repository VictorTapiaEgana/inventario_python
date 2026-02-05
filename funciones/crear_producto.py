from ui.ventana import ventana

def crear_registro()->none:

    ventana(["Sistema de inventario",
             "",
             "CREAR NUEVO REGISTRO"])

    nombre = input("Nombre del producto: ")

from funciones.crear_producto import crear_registro
from ui.ventana import ventana

def seleccionar_menu(opcion, menu_items)->bool:    
    # Check if option is available
    if opcion == 2:  # Eliminar option
        for item in menu_items:
            if "2-. Eliminar un Registro" in item["texto"]:
                if not item.get("disponible", True):
                    print("❌ Opción no disponible en este momento")
                    return True
    
    match opcion:
        case 1:
            crear_registro()
            return  True
        case 2:
            print("ELIMINAR")
            return  True
        case 3:
            print("VER")
            return  True
        case _:           
           return  False

def main()->none:
    # VARIABLES GLOBALES
    entrada: bool = True
    """ Valida si se selecciono una opcion valida del menu inicial"""
    
    inventario:list[dict[str,str | int]] = [] 
    """
    Estructura del inventario
    [
       {
           "nombre": "Producto 1",
           "stock": 10,
           "precio": 100,
           "descripcion":"Este es un producto "
       },
       {
           "nombre": "Producto 2",
           "stock": 20,
           "precio": 200,
           "descripcion":"Este es otro producto"
       }
    ]
    """
    while entrada == True:   

        menu = (
            {"texto": "Sistema de Inventario", "align": "center"},
            {"texto": "Opciones", "align": "center"},
            {"texto": "1-. Nuevo Registro", "align": "left"},
            {"texto": "2-. Eliminar un Registro", "align": "left"},
            {"texto": "3-. Ver Registros", "align": "left"},
            {"texto": "4-. SALIR [x]", "align": "left"},
            {"texto": "", "align": "center"}
        )        
        ventana(menu)
            


        opcion = int(input("Ingrese el numero de una opcion:")) 
        entrada = seleccionar_menu(opcion)
        
        
if __name__ == "__main__" : 
    main()
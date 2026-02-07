from funciones.crear_producto import crear_registro
from ui.ventana import ventana
from tkinter import *
from funciones.inventario import cargar_inventario

def seleccionar_menu(opcion)->bool:        
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
        case 4:           
            print("Saliendo...\nAplicacion CERRADA!!!!")
            return  False
        case _:                       
            return  True

def main()->none:
    #********************* VARIABLES GLOBALES******************
    #Valida si se selecciono una opcion valida del menu inicial
    entrada: bool = True
    inventario:list[dict[str,str | int]] = cargar_inventario()
    #**********************************************************
    
    
    

    print(inventario)
    
    

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

        opcion = input("Ingrese una opcion VALIDA:")

        if opcion.isdigit():
            opcion = int(opcion)
            entrada = seleccionar_menu(opcion)
        else:            
            continue
        
        
if __name__ == "__main__" : 
    main()
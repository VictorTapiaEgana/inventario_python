import json

def cargar_inventario():
    """
        Carga el inventario desde el archivo de texto.
        Retorna una lista de productos.
    """
    
    try:
        with open("datos/inventario.txt", 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def guardar_inventario(producto_nuevo):
    """
        Guarda el inventario en el archivo de texto.
    """

    inventario = cargar_inventario()
    inventario.append(producto_nuevo)

    try:
        with open("datos/inventario.txt", 'w') as f:
            json.dump(inventario, f, indent=4)        
    except Exception as e:
        print(f"Error al guardar el inventario \nReintente nuevamente. {e}")
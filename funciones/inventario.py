import json

def cargar_inventario()->list[dict[str,str | int]]:
    """
        Carga el inventario desde el archivo de texto.
        Retorna una lista de productos.
    """
    
    try:
        with open("datos/inventario.txt", 'r',encoding='utf-8') as archivo:

            datos = json.load(archivo)
            #agregamos el indice como id a cada producto
            for inice, producto in enumerate(datos):
                producto['id'] = inice + 1

            return datos

    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def guardar_inventario(producto_nuevo)->None:
    """
        Guarda el inventario en el archivo de texto.
    """
    inventario:list[dict[str,str | int]] = cargar_inventario()    
    # inventario = cargar_inventario()
    inventario.append(producto_nuevo)

    try:

        with open("datos/inventario.txt", 'w',encoding='utf-8') as archivo:
            json.dump(inventario, archivo, indent=4)        

    except Exception as e:

        print(f"Error al guardar el inventario \nReintente nuevamente. {e}")

def eiminar_por_id(inventario)->None:
    """
        Elimina un producto por su id.
    """
    with open("datos/inventario.txt", "w", encoding="utf-8") as f:
        lista_limpia = []
        for producto in inventario:

            p_limpio = {
                "nombre": producto.get('nombre'),
                "descripcion": producto.get('descripcion'),
                "precio": producto.get('precio'),
                "stock": producto.get('stock')
            }

            lista_limpia.append(p_limpio)
        
        try:
            with open("datos/inventario.txt", "w", encoding="utf-8") as f:
               
                json.dump(lista_limpia, f, indent=4, ensure_ascii=False)
            

        except Exception as e:

            print(f"Error al escribir el archivo: {e}")
    
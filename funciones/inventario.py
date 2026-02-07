def cargar_inventario():
    """
    Carga el inventario desde el archivo de texto.
    Retorna una lista de productos.
    
    Estructura del inventario
    [
       {
           "nombre": "Producto 1",
           "stock": 10,
           "precio": 100,
           "descripcion":"Este es un producto ",
           "valor": 1000
       },
       {
           "nombre": "Producto 2",
           "stock": 20,
           "precio": 200,
           "descripcion":"Este es otro producto",
           "valor" : 4000
       }
    ]

    """
    
    try:
        with open("datos/inventario.txt", 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return [] 
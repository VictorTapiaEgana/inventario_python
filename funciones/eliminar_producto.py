from tabulate import tabulate
from ui.ventana import ventana
from funciones.inventario import cargar_inventario
from funciones.inventario import eiminar_por_id

def eliminar_producto():
        
    menu = (
        {"texto":"Sistema de inventario","align":"center"},
        {"texto":"", "align":"center"},
        {"texto":"ELIMINAR PRODUCTO", "align":"center"}
    )
    ventana(menu)

    print("SELECCIONE EL ID DEL PRODUCTO A ELIMINAR".center(79))  

    inventario = cargar_inventario()    
    
    # ORDENAR LOS CAMPOS DE LA TABLA
    inventario_ordenado = []

    for productos in inventario:
        
        producto_ordenado ={
            'ID': productos['id'],
            'NOMBRE': productos['nombre'],
            # 'DESCRIPCION': productos['descripcion'],
            # 'PRECIO': f"$ {productos['precio']}",
            'STOCK': productos['stock']
        }

        inventario_ordenado.append(producto_ordenado)
    
    # print(tabulate(inventario_ordenado, headers="keys", tablefmt="grid", maxcolwidths=[None, 25, 25, None, None]))
    tabla_texto = tabulate(inventario_ordenado, headers="keys", tablefmt="grid", maxcolwidths=[None, 25, 25, None, None])
    tabla_centrada = "\n".join(linea.center(79) for linea in tabla_texto.split("\n"))

    print(tabla_centrada)

    id_producto=0

    while not id_producto:
        """ Validacio del Id edecuado """
        
        id_producto = input("\nIngrese el ID del producto a eliminar o 's' para salir: ")

        if id_producto.lower() == "s":
            print("Saliendo...")
            return
        
        if not id_producto.isdigit():
            print("El valor debe ser un numero")
            id_producto = None
            continue

        id_producto = int(id_producto)

        if id_producto < 0 or id_producto > len(inventario):
            print("El valor debe ser numero mayor a cero y menor al numero de productos")
            id_producto = None

    #Se elimina el producto del inventario
    inventario.pop(id_producto - 1)

    eiminar_por_id(inventario)    


    input("PRODUCTO ELIMINADO!!!! \nPresione cualquier tecla para continuar...")
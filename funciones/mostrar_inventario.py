
from funciones.inventario import cargar_inventario
from ui.ventana import ventana
from tabulate import tabulate

def mostrar_inventario():

    menu = (
        {"texto":"Sistema de inventario","align":"center"},
        {"texto":"", "align":"center"},
        {"texto":"DETALLE DE INVENTARIO", "align":"center"}
    )
    ventana(menu)
    inventario = cargar_inventario()
    
    # ORDENAR LOS CAMPOS DE LA TABLA
    inventario_ordenado = []

    for productos in inventario:
        
        producto_ordenado ={
            'ID': productos['id'],
            'NOMBRE': productos['nombre'],
            'DESCRIPCION': productos['descripcion'],
            'PRECIO': f"$ {productos['precio']}",
            'STOCK': productos['stock']
        }

        inventario_ordenado.append(producto_ordenado)
    

    tabla_texto = tabulate(inventario_ordenado, headers="keys", tablefmt="grid", maxcolwidths=[None, 25, 25, None, None])
    tabla_centrada = "\n".join(linea.center(79) for linea in tabla_texto.split("\n"))

    print(tabla_centrada)
    input("\nPresione cualquier tecla para volver la Menu Principal . . . .")
    
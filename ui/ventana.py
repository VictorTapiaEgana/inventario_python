import os

def ventana(menu:dict[str,str])->none():
    
    #Ancho maximo de la ventana
    ancho:int = 79

    #limpia la consola
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"╔{'═' * (ancho-2)}╗")

    for linea in menu:
        contenido = linea['texto']
        alineacion = linea['align']

        if alineacion == 'center':
            print(f"║ {str(contenido.center(ancho-4))} ║")
        else:
            print(f"║ {str(contenido.ljust(ancho-4))} ║")

    print(f"╚{'═' * (ancho-2)}╝")
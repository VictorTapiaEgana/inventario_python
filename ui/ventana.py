import os

def ventana(contenido:int , ancho=79)->none():

    #Limipia la consola , antes de ejecutar la ventana
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"╔{'═' * (ancho-2)}╗")

    for palabra in contenido:    
        print(f"║ {palabra.center(ancho-4)} ║")

    print(f"╚{'═' * (ancho-2)}╝")
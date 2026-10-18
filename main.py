from PIL import Image
import numpy as np
from gameboy import filtroGameBoy
from filtroCRT import filtroCRT
from insertar_pantalla import insertar_en_pantalla

ruta_gameboy: str = "materiales/gameboy.png" 
ruta_gameboy_mascara: str = "materiales/gameboy_mascara.png"
ruta_tv: str = "materiales/tv.png"
ruta_mascara_tv: str = "materiales/tv_mascara.png"

def main() -> None:

    """La función solicita al usuario la ruta de la imagen, luego le pregunta qué tipo
     de pantalla quiere (gameboy o crt) y la ruta de salida. Valida que la imágen exista, 
     que la pantalla sea alguna con las cuales trabaja el programa y que el desplazamiento
     sea un entero positivo. Finalmente, aplica el filtro, insertala imágen resultante en la 
    pantalla correspondiente y guardala imágen en la ruta de salida ingresada por el usuario.
    """

    ruta: str = input ("Ingrese la ruta de la imagen: ")
    try:
        imagen: Image.Image = Image.open(ruta)

    except FileNotFoundError:
        print ("No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
        return 

    pantalla: str = input("Seleccione la pantalla (gameboy/crt): ")
    if pantalla != "gameboy" and pantalla != "crt":
        print ("Pantalla inválida. Las opciones son 'gameboy' o 'crt'.")
        return 

    #Desplazamiento sólo para crt
    desplazamiento: int = 3
    if pantalla == "crt":
        texto: str = input ("Ingrese el desplazamiento de canales (default=3): ")
        if texto != "":
            try:
                desplazamiento = int(texto)

            except ValueError:
                print ("El desplazamiento debe ser un número entero positivo.")
                return

            if desplazamiento <= 0:
                print ("El desplazamiento debe ser un número entero positivo.")
                return

    ruta_salida: str = input ("Seleccione la ruta para guardar la imágen procesada: ")

    if pantalla == "gameboy":
        foto_filtro: np.array = filtroGameBoy(imagen)
        final: np.array = insertar_en_pantalla(foto_filtro, ruta_gameboy, ruta_gameboy_mascara)
    else:
        foto_filtro = filtroCRT(imagen, desplazamiento)
        final = insertar_en_pantalla(foto_filtro, ruta_tv, ruta_mascara_tv)

    Image.fromarray(final).save(ruta_salida)
    print ()
    print (f"Imagen guardada en {ruta_salida}")

if __name__ == "__main__":
    main()
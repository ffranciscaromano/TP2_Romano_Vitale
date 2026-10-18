from PIL import Image
import numpy as np

def insertar_en_pantalla (foto_filtro: np.array, ruta_foto: str, ruta_mascara: str):

    """ Ésta función ajusta el tamaño original de la imágen ingresada 
    al tamaño del tipo de pantalla seleccionada por el usuario. """

    foto: np.array = np.array (Image.open(ruta_foto))
    mascara: np.array = np.array (Image.open(ruta_mascara))

    alto: int = mascara.shape [0]
    ancho: int = mascara.shape [1]

    y1: int = alto
    y2: int = -1
    x1: int = ancho
    x2: int = -1

    for y in range(alto):
        for x in range(ancho):
            if mascara[y, x] == 255:
                if y < y1:
                    y1 = y

                if y > y2:
                    y2 = y

                if x < x1:
                    x1 = x
                
                if x > x2:
                    x2 = x

    #Estiro la imagen 
    ancho_pantalla: int = x2 - x1 + 1
    alto_pantalla: int = y2 - y1 + 1
    img_estirada: np.array = Image.fromarray(foto_filtro).resize((ancho_pantalla, alto_pantalla))
    
    resultado: np.array = foto.copy()
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if mascara[y, x] == 255:
                resultado[y, x] = img_estirada [y - y1, x - x1]

    return resultado
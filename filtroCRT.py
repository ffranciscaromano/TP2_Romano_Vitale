
from PIL import Image
import numpy as np


def filtroCRT(imagen:Image.Image, desplazamiento: int = 3) -> np.ndarray:

    """La función recibe la imágen y el desplazamiento como parámetros, ambos 
    ingresados por el usuario. Luego, aplica el filtro CRT en la imágen solicitada 
    de la siguiente forma: primero, redimensiona la imágen a 320x240; después, desplaza
    los canales rojo (hacia la izquierda) y azul (hacia la derecha) según lo que 
    solicitó el usuario (3 por default en caso de no ingresar nada), y oscurece las 
    filas pares para simular las scanlines. 
    
    Parámetros de entrada:
        - imagen: imágen ya abierta con Image.com (Image.Image)
        - desplazamiento: cantidad de píxeles de desplazamiento (por default 3)

    Parametros de salida:
        - Matriz numpy uint8 de forma (240, 320, 3) con la imágen filtrada con el 
        filtro CRT
    """

    #resize y convertir en números
    imagen = imagen.resize((320, 240))
    matriz: np.ndarray = np.array(imagen)
    resultado: np.ndarray = matriz.copy()


    #desplazamineto
    ROJO: int = 0
    VERDE: int = 1 
    AZUL: int = 2

    alto: int = matriz.shape[0]
    ancho: int = matriz.shape[1]

    for y in range(alto):

        for x in range(ancho):
            if x - desplazamiento >= 0: 
                resultado[y, x, ROJO] = matriz[y, x - desplazamiento, ROJO]
            if x + desplazamiento < ancho:
                resultado[y, x, AZUL] = matriz[y, x + desplazamiento, AZUL]

    #scanlines
    for y in range(0, alto, 2):
        for x in range(ancho):
            for color in range(3):
                resultado[y, x, color] = round(int(resultado[y, x, color]) * 0.5)

    return resultado 
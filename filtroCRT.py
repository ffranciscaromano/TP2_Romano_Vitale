
from PIL import Image
import numpy as np


def filtroCRT(imagen:Image.Image, desplazamiento: int = 3) -> np.array:

    """ La función recibe la imágen y el despalzamineto, ambos 
    ingresados por el usuario. Primero reacomoda el tamaño 
    de la imágen para que sea del tamaño del tele, luego la 
    convierte en matriz para trabajar con ella. Luego desplazamos los píxeles
    dado el número ingresado por el usuario, sino esta configurado para 
    que el desplazamiento sea 3, de no poner ningún valor. Y el detalle que 
    destaca al CRT son sus líneas claras/oscuras horizontales. 
    La función devuelve """

    #resize y convertir en números
    imagen = imagen.convert("RGB").resize((320, 240))
    matriz: np.array = np.array(imagen)
    resultado: np.array = matriz.copy()


    #desplazamineto
    ROJO: int = 0
    VERDE: int = 1 
    AZUL: int = 2

    alto: int = matriz.shape[0]
    ancho: int = matriz.shape[1]

    for x in range(ancho):

        for y in range(alto):

            if x - desplazamiento >= 0: 
                resultado[y, x, ROJO] = matriz[y, x - desplazamiento, ROJO]
            if x + desplazamiento < ancho:
                resultado[y, x, AZUL] = resultado[y, x + desplazamiento, AZUL]

    #scanlines
    for y in range(0, alto, 2):
        for x in range(ancho):
            for color in range(3):
                resultado[y, x, color] = round(resultado[y,x, color]* 0.5)


    return resultado 
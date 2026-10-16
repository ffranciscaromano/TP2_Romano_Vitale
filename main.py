import PIL
from PIL import Image
import numpy as np

def filtroGameBoy(imagen):
    GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
    
    BAYER_4 = [
        [ 0,  8,  2, 10],
        [12,  4, 14,  6],
        [ 3, 11,  1,  9],
        [15,  7, 13,  5],
        ]
    
    imagen = imagen.resize((160,144))
    matriz_pixeles = np.array(imagen)

    alto = matriz_pixeles.shape[0]
    ancho = matriz_pixeles.shape [1]
    paso = 64
    
    matriz_salida = np.zeros ((alto, ancho, 3), dtype = np.uint8)
    
    for y in range (alto):
        for x in range (ancho):
            r = int (matriz_pixeles[y, x, 0])
            g = int (matriz_pixeles[y, x, 1])
            b = int (matriz_pixeles [y, x, 2])
            brillo = (r + g + b) / 3

            ajuste = ( ((BAYER_4[y % 4][x % 4] + 0.5)/16) - 0.5 ) * paso
            brillo = brillo + ajuste

            indice = int (brillo // paso)
            indice = max (0, min(3, indice)) #asegura que nunca sea > 0, <3

            matriz_salida [y, x] = GAMEBOY[indice]

    return matriz_salida

imagen_abierta = Image.open("materiales/statue_of_liberty.jpg")

resultado = filtroGameBoy(imagen_abierta)
Image.fromarray (resultado).save("probando_gameboy.jpg")
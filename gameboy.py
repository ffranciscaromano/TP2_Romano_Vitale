from PIL import Image
import numpy as np

GAMEBOY: list = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
    
BAYER_4: list = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
    ]
    
def filtroGameBoy(imagen: Image.Image) -> np.array:
    
    """La función aplica el filtro gameboy a la imágen ingresada.  
    El filtro lo aplica de la siguiente forma: redimensiona la imágen a 160x144,
    calcula el brillo de cada píxel a partir del promedio de sus canales RGB, 
    le suma el ajuste de dithering ordenado (matriz de Bayer 4x4) y lo lleva a 
    uno de los 4 tonos de la paleta GAMEBOY
    
    Parámetros de entrada:
        - imagen: imágen ya abierta con Image.open (Image.Image)
    
    Parámetros de salida:
        - Matriz numpy uint8 de forma (144, 160, 3) con la imagen ya
            filtrada con gameboy    
    """

    imagen = imagen.resize((160,144)) #(ancho, alto) 
    matriz_pixeles: np.array = np.array(imagen)

    alto: int = matriz_pixeles.shape[0]
    ancho: int = matriz_pixeles.shape [1]
    paso: int = 64
    
    matriz_salida: np.array = np.zeros ((alto, ancho, 3), dtype = np.uint8)
    
    for y in range (alto):
        for x in range (ancho):
            r: int = int (matriz_pixeles[y, x, 0])
            g: int = int (matriz_pixeles[y, x, 1])
            b: int = int (matriz_pixeles [y, x, 2])
            brillo: float = (r + g + b) / 3

            ajuste: float = ( ((BAYER_4[y % 4][x % 4] + 0.5)/16) - 0.5 ) * paso
            brillo = brillo + ajuste

            indice: int = int (brillo // paso)
            indice = max (0, min(3, indice)) #asegura que nunca sea > 0, <3

            matriz_salida [y, x] = GAMEBOY[indice]

    return matriz_salida
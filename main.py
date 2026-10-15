import PIL
from PIL import Image
import numpy as np

"""FALTA PEDIR IMÁGEN AL USUARIO.... Image.open"""
imagen = Image.open("materiales/statue_of_liberty.jpg") #o lo que pida el usuario"

def filtroGameBoy(imagen):
    imagen = imagen.resize ((160,144))
    matriz_pixeles = np.array (imagen)

    GAMEBOY = [(15, 56, 15), (48, 98, 48), (139, 172, 15), (155, 188, 15)]
    paso = 64
    
    alto = matriz_pixeles.shape[0]
    ancho = matriz_pixeles.shape [1]

    for y in range (alto):
        for x in range (ancho):
            r = int (matriz_pixeles[y, x, 0])
            g = int (matriz_pixeles[y, x, 1])
            b = int (matriz_pixeles [y, x, 2])
            brillo = (r + g + b)/3
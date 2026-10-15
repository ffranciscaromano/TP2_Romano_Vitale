import PIL
from PIL import Image
import numpy as np

"""FALTA PEDIR IMÁGEN AL USUARIO.... Image.open"""
imagen = Image.open("TP2_Romano_Vitale\img\statue_of_liberty.jpg") #o lo que pida el usuario"

def filtroGameBoy(imagen):
    imagen = imagen.resize ((160,144))
    matriz_pixeles = np.array (imagen)
    return matriz_pixeles

matriz = filtroGameBoy (imagen)

print (matriz.shape)
print (matriz[0,0])
print ("HOLA")
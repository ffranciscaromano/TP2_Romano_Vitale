"""hacer import de las fotos con el filtro"""
from PIL import Image
import numpy as np

def insertar_en_pantalla (foto_filtro, ruta_foto, ruta_mascara):
    foto = np.array (Image.open(ruta_foto))
    mascara = np.array (Image.open(ruta_mascara))

    #.shape() te dice qué dimensiones tiene el array (o sea, la matriz)
    alto = mascara.shape [0]
    ancho = mascara.shape [1]

    y1 = alto
    y2 = -1
    x1 = ancho
    x2 = -1

    for y in range (alto):
        for x in range (ancho):
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
    ancho_pantalla = x2 - x1 + 1
    alto_pantalla = y2 - y1 + 1
    img_estirada = Image.fromarray(foto_filtro).resize((ancho_pantalla, alto_pantalla)) #lo pongo del tamaño de la mascara
    img_estirada = np.array (img_estirada)

    #.copy() copia la foto tal cual así trabajo con una copia y no la og
    resultado = foto.copy()
    for y in range (y1, y2 + 1):
        for x in range (x1, x2 + 1):
            if mascara[y, x] == 255:
                resultado[y, x] = img_estirada [y - y1, x - x1]

    return resultado

#PRUEBO CON GAMEBOY QUE YA ESTÁ HECHO   

from gameboy import filtroGameBoy

foto_filtro = filtroGameBoy (Image.open("materiales/statue_of_liberty.jpg"))
final = insertar_en_pantalla(foto_filtro, "materiales/gameboy.png", "materiales/gameboy_mascara.png")
Image.fromarray(final).save("prueba_pantalla.png")
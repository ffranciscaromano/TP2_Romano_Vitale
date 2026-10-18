# TP2_Romano_Vitale

El trabajo es un programa que permite al usuario ingresar una imagen para luego poder poder aplicarle filtros y simular como se vería esa imagen en un Game Boy o en un televisor viejo. 


## integrantes
Isabella Tina Vitale 
Franscisca Romano

## archivos utilizados 
main.py : es el código principal del trabajo, en donde se llaman a los otros archivos para ejecutar efectivamente el programa
gameboy.py : es el filtro game boy, que modifica a cuatro tonos de verde con dithering
filtroCRT.py : es el filtro del televisor, que corre los colores azul y rojo, y trabaja las scanlines
insertar_pantalla.py : pega la nueva imagen dentro de la pantalla de cada respectivo aparato

## como usarlo 
- ingresar ruta de guardado de donde está él archivo con la imágen a modificar
- seleccionar gameboy o crt
- seleccionar donde querés guardar la nueva imágen
- el programa crea un archivo y guarda la imagen en su respectivo archivo seleccionado

## validaciones
 tira error si: 
 - no se encuentra la imagen ingresada por el usuario
 - la pantalla elegida no es gameboy ni crt 
 - el deplazamiento ingresado no es un número entero y positivo
 
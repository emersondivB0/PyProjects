from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write("Comienzo de archivo")
    archivo.close()

def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt','r')
        #texto = archivo.read()
        texto = archivo.readlines()
        archivo.close()
        print(texto)
    else:
        print('No existe el archivo')




def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')
        archivo.write('\nHola Juán')
        archivo.close()
    else:
        print('No existe el archivo')


def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'Hola locos\n'
        archivo.write('\nHola Juán')
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        print(texto)
    else:
        print('No existe el archivo')

#escribir_archivo()
#leer_archivo()
#agregar_datos()
modificar_datos()
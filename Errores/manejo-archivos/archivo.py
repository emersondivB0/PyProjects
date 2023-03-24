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
#escribir_archivo()
leer_archivo()
from io import open

def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write("Comienzo de archivo")
    archivo.close()
    
escribir_archivo()
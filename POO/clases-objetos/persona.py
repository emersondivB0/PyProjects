class Persona():
    #si definimos un constructor no hay que estar declarando atributos ni asignando valores uno a uno

    #nombre =None
    #edad = None
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    # una función dentro de una clase se denomina método
    def mostrar_datos(self):
        print('Edad: ', self.edad)
        print('Nombre: ', self.nombre)
#si quiero que el print de un objet0 me devuelva su estado y no su posición de memoria
# debo declarar el método str
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'

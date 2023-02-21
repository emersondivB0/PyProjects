class Persona:
    #si defino los atributos con doble piso, se declaran privados
    #__nombre = None
    #__edad = None

    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def _metodo_privado(self):
        print("Soy un mérodo privado")

    def getName(self):
        return self.__nombre

    def setName(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.__nombre} \nEdad: {self.__edad}"

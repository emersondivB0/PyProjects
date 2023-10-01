class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def moverse(self):
        print('Ando caminando')
        
class Atleta(Persona):
    def moverse(self):
        print('Ando corriendo')
        
class Ciclista(Persona):
    def moverse(self):
        print('Ando moviéndome en mi bicicleta')
        
        
"""
Este es el concepto de polimorfismo, modificar métodos, usando el mismo nombre, pero con funcionalidad distinta para cada subclase
"""
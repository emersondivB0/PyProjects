"""Así se lanza un error directamente sin try
"""
class OperadorExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def dividir(a,b):
    if b == 0:
        #raise ZeroDivisionError("Error: no se puede dividir entre 0")
        raise OperadorExcepcion("Error: no se puede dividir entre 0")
    else:
        return a/b

dividir(4,0)
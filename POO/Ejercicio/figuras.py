class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        Figura.__init__(self, nombre)
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2*self.base) + (2*self.altura)
    
    def __str__(self):
        return Figura.__str__(self) + f"\nArea: {self.base} \nAltura: {self.altura}"
        
    
class Circulo(Figura):
    def __init__(self, nombre, radio):
        Figura.__init__(self, nombre)
        self.radio = radio
        
    def area(self):
        return (3.14 * self.radio * self.radio)
    
    def perimetro(self):
        return (2 * 3.14 * self.radio)
    
    def __str__(self):
        return Figura.__str__(self) + f"\nRadio: {self.radio}"
    
def probar_figura(objeto):
    print(objeto)
    print(f"Area: {objeto.area()} \nPerimetro: {objeto.perimetro(): .2f}")
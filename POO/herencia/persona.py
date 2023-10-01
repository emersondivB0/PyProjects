"""Definiremos la clase principal o clase padre, y crearemos clases secundarias o hijas que heredarán atributos y/o métodos del padre

    Returns:
        class Persona: clase principal
"""
class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def detalle_persona(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad}")
        
    def __str__(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"
    
"""Para definir una clase hija o secundaria, se de coloca entre paréntesis la clase desde la cual se quiere heredar.

En este caso se creará ua clase que herede todos los métodos y atributos de Persona
"""
class Cliente(Persona):
    pass

"""
Ahora se creará una clase Empleado
"""

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        #heredo el constructor de la clase Persona
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def detalle_empleado(self):
        super().detalle_persona()
        print("Sueldo: ", self.sueldo)
        
    def __str__(self):
        return super().__str__() + f"\nSueldo: {self.sueldo}"

"""
Ahora vamos a heredar sin la función super(), directamente con la clase Persona
"""
class Ejecutivo(Persona):
    def __init__(self,nombre,edad,sueldo,cargo):
        #heredo el constructor de la clase Persona
        #super().__init__(nombre, edad)
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo
        self.cargo = cargo
        
    def detalle_empleado(self):
        #super().detalle_persona()
        Persona.detalle_persona(self)
        print(f"Sueldo:  {self.sueldo} \nCargo: {self.cargo}")
        
    def __str__(self):
        #return super().__str__() + f"\nSueldo: {self.sueldo} \nCargo: {self.cargo}"
        return Persona.__str__(self) + f"\nSueldo: {self.sueldo} \nCargo: {self.cargo}"
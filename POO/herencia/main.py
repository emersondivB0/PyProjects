from persona import Cliente, Empleado, Ejecutivo

cliente1 = Cliente("Andrés", 33)
cliente1.detalle_persona()

cliente2 = Cliente("Pedro", 27)
print(cliente2)

empleado1 = Empleado("Anna", 28, 1500)
empleado2 = Empleado("Juana", 35, 1800)

empleado1.detalle_empleado()
empleado2.detalle_persona()
print(empleado2)

ejecutivo1 = Ejecutivo("Gus", 23, 2500, "Vicepresidente")

print(ejecutivo1)
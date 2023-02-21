from sys import argv

if len(argv) == 4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])
    
    print(f"Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}")
    print()
    print("Nombre: {} \nEdad: {} \nAltura: {}".format(nombre, edad, altura))
    print()
    print("Nombre: {n} \nEdad: {e} \nAltura: {a}".format(n = nombre, a = altura, e = edad))


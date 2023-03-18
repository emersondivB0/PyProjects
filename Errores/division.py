divi = 0
try:
    a = int(input("Ingrese el Dividendo: "))
    b = int(input("Ingrese el Divisor: "))

    divi = a / b
except ValueError:
    print("Ingrese sólo números enteros.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
except Exception as error:
    print("Ha ocurrido un error no previsto:", type(error).__name__)

print("La división es: ", divi)
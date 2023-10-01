import math
import matplotlib.pyplot as plt

def bessel_j0(x):
    return math.cos(x)

def bessel_j1(x):
    return (math.sin(x))/x

# Genera valores de x
x = [i/10 for i in range(1,100)]

# Calcula las funciones de Bessel de orden 0 y 1
J0 = [bessel_j0(xi) for xi in x]
J1 = [bessel_j1(xi) for xi in x]

# Grafica las funciones de Bessel
plt.plot(x, J0, label='J0')
plt.plot(x, J1, label='J1')

# Configura el gráfico
plt.title('Funciones de Bessel')
plt.xlabel('x')
plt.ylabel('J(n)')
plt.legend()

# Guarda la imagen como un archivo PNG
plt.savefig('Ejemplo.png')
plt.show()


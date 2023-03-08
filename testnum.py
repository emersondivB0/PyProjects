"""
Prueba genérica de numpy y matplotlib
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 21})
ax = plt.gca()

ax2 = ax.twinx()
for i in range(10):
    ax.bar(i, np.random.randint(1000))

plt.ylabel('Datos')
plt.savefig("Ejemplo1.jpg")

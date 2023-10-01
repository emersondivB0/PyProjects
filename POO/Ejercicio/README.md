Crear un módulo figuras.py, y dentro crea clases como Figura, Rectangulo, Circulo y la función probar_figura.

Crear una clase Figura, con atributo nombre. Crear también el constructor de la clase y los métodos necesarios área y el perímetro con instrucción pass.

Crear otra clase Rectángulo que herede de la clase Figura, con atributos base y altura. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.

Crear otra clase Circulo que herede de la clase Figura, con atributo radio. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.

Crear una función probar_figura donde reciba un objeto para probar diferentes figuras como rectángulo o circulo. Y imprima el estado del objeto y como también el área y perímetro.

Crear un módulo principal main.py, luego importa desde el modulo figuras las clases Rectángulo, Circulo y la función probar_figura.

Crear la función principal que puede ser main() y el punto de entrada de la aplicación de Python y llama a ejecutar la función main().

Dentro de la función main() crea un sistema que tenga un bucle infinito y también tenga un menú de navegación donde las opciones sean 1-Rectangurlo 2-Circulo 4-Salir

En la opción 1 pide al usuario que ingrese base y altura del rectángulo y crea un objeto de rectángulo y ese objeto envía al funcion probar_figura()

En la opción 2 pide al usuario que ingrese el radio del circulo y crea un objeto de circulo y ese objeto envía al función probar_figura()

En la opción 3 termina el bucle infinito y se cierra el programa.

Ejemplo de la salida Final:

   

λ python main.py
 
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
 
        1 - Rectangurlo
        2 - Circulo
        3 - Salir
        Ingrese una Opcion: 1
Ingrese Base:4
Ingrese Altura: 3
Rectangulo[base:4.0 altura:3.0]
Area:  12.0
Perimetro:  14.0
 
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
 
        1 - Rectangurlo
        2 - Circulo
        3 - Salir
        Ingrese una Opcion: 2
Ingrese Radio:5
Circulo[radio:5.0]
Area:  78.53981633974483
Perimetro:  31.41592653589793
 
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
 
        1 - Rectangurlo
        2 - Circulo
        3 - Salir
        Ingrese una Opcion: 8
Opción incorrecta
 
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
 
        1 - Rectangurlo
        2 - Circulo
        3 - Salir
        Ingrese una Opcion: 3
Cerrando sistema
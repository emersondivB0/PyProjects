Generador de contraseñas seguras: 

Crea un programa que genere contraseñas seguras para los usuarios.
El programa debe utilizar expresiones regulares
para validar la complejidad de las contraseñas y
almacenarlas en una base de datos. Esto te
permitirá utilizar tus habilidades en programación
orientada a objetos, manejo de bases de datos y
expresiones regulares

Pasos a seguir:

1.- Define las características que deben cumplir las contraseñas seguras: longitud mínima, caracteres permitidos, complejidad, etc. La idea es que las contraseñas sean lo suficientemente complejas para que sean difíciles de adivinar o hackear, pero también fáciles de recordar para el usuario.

2.- Crea una clase para generar las contraseñas. Esta clase podría tener un método que reciba como parámetros la longitud mínima y los caracteres permitidos, y que genere una contraseña aleatoria que cumpla con esas características.

3.- Utiliza expresiones regulares para validar la complejidad de las contraseñas. Por ejemplo, puedes asegurarte de que la contraseña contenga al menos una letra mayúscula, una letra minúscula, un número y un carácter especial. Si la contraseña no cumple con estas características, puedes mostrar un mensaje de error al usuario y pedirle que vuelva a intentar.

Punto 3: Utiliza expresiones regulares para validar la comlejidad de las contraseñas
Las expresiones regulares son patrones de búsqueda que permiten buscar y validar texto. En este caso, podemos utilizarexpresiones regulares para validar que las contraseñas generadas sean lo suficientemente complejas.

Por ejemplo, podemos crear una expresión regular que valideque la contraseña tenga al menos 8 caracteres, una letra m
ayúscula, una letra minúscula, un número y un carácter especial. Una posible expresión regular sería la siguiente:

>>:  ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;'?/><,.\[\]\\|]).{8,}$

Esta expresión regular contiene las siguientes partes:

^ y $: indican el inicio y el final de la cadena de texto, respectivamente.
(?=.*\d): busca un dígito en la cadena de texto.
(?=.*[a-z]): busca una letra minúscula en la cadena de texto.
(?=.*[A-Z]): busca una letra mayúscula en la cadena de texto.
(?=.*[!@#$%^&*()_+}{":;'?/><,.\[\]\\|]): busca un carácter especial en la cadena de texto.
.{8,}: busca cualquier carácter en la cadena de texto, con una longitud mínima de 8 caracteres.

Para validar que una contraseña cumple con esta expresión regular, podemos utilizar la función match() de Python. Si la contraseña cumple con la expresión regular, la función devolverá un objeto Match, que indica que la contraseña es válida. Si la contraseña no cumple con la expresión regular, la función devolverá None, lo que indica que la contraseña no es válida.




4.- Conecta tu programa a una base de datos para almacenar las contraseñas generadas. Puedes crear una tabla para almacenar las contraseñas junto con el nombre de usuario y otros detalles relevantes. Asegúrate de encriptar las contraseñas antes de almacenarlas en la base de datos para proteger la privacidad del usuario.

Punto 4: Conecta tu programa a una base de datos para almacenar las contraseñas generadas
Para almacenar las contraseñas generadas en una base de datos, podemos utilizar un sistema de gestión de bases de datos (DBMS, por sus siglas en inglés) como MySQL, PostgreSQL, SQLite, etc.

Para conectarnos a la base de datos desde Python, podemos utilizar un paquete como mysql-connector-python o psycopg2 (para MySQL y PostgreSQL, respectivamente). Estos paquetes permiten conectarnos a la base de datos y realizar consultas SQL para almacenar y recuperar datos.

Para almacenar las contraseñas generadas en la base de datos, podemos crear una tabla en la base de datos que contenga los siguientes campos:

id: un identificador único para cada registro.
username: el nombre de usuario asociado a la contraseña.
password: la contraseña generada.
created_at: la fecha y hora en que se generó la contraseña

Para insertar un registro en la tabla, podemos utilizar una consulta SQL como la siguiente:

import mysql.connector

# Conectamos a la base de datos
cnx = mysql.connector.connect(user='usuario', password='contraseña',
                              host='localhost', database='basedatos')
cursor = cnx.cursor()

# Generamos la contraseña
password = generar_password()

# Insertamos el...


5.- Implementa una interfaz de usuario para que el usuario pueda solicitar una contraseña segura. Puedes hacer esto a través de una interfaz gráfica o de línea de comandos.

6.- Prueba tu programa para asegurarte de que las contraseñas generadas sean realmente seguras y que se almacenen correctamente en la base de datos.

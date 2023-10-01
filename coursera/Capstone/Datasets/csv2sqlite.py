import sqlite3
import csv

#Abrimos el archivo CSV
f=open('C:UsersAdminDesktopPosiciones.csv','r') 
#Omitimos la linea de encabezado
next(f, None)
reader = csv.reader(f, delimiter=';')

#Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect('Posiciones.db')
cur = sql.cursor()

#Creamos la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS posiciones
            (posicion int, nombre text, equipo text, tiempo text)''')

#Llenamos la BD con los datos del CSV
for row in reader:
    cur.execute("INSERT INTO posiciones VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

#Muestro las filas guardadas en la tabla
for row in cur.execute('SELECT * FROM posiciones'):
    print(row)

#Cerramos el archivo y la conexion a la bd
f.close()
sql.commit()
sql.close()
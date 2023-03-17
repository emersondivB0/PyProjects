import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Conexión a la base de datos
cnx = mysql.connector.connect(host="%",
                              user="emerson",
                              password="database",
                              database="todo_list_py")


# Funciones para manejar las tareas
def agregar_tarea(descripcion, fecha_vencimiento):
    try:
        fecha_vencimiento = datetime.strptime(fecha_vencimiento,
                                              "%d/%m/%Y").date()
    except ValueError:
        return "Formato de fecha incorrecto (DD/MM/AAAA)"
    cursor = cnx.cursor()
    query = "INSERT INTO tareas (descripcion, fecha_vencimiento) VALUES (%s, %s)"
    values = (descripcion, fecha_vencimiento)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()


def mostrar_tareas():
    cursor = cnx.cursor()
    query = "SELECT id, descripcion, fecha_vencimiento, completada FROM tareas"
    cursor.execute(query)
    tareas = cursor.fetchall()
    for tarea in tareas:
        print(
            f"{tarea[0]} - {tarea[1]} - {tarea[2].strftime('%d/%m/%Y')} - {tarea[3]}"
        )
    cursor.close()


def actualizar_tarea(tarea_id, completada):
    cursor = cnx.cursor()
    query = "UPDATE tareas SET completada = %s WHERE id = %s"
    values = (completada, tarea_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()


def eliminar_tarea(tarea_id):
    cursor = cnx.cursor()
    query = "DELETE FROM tareas WHERE id = %s"
    values = (tarea_id, )
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()

"""
Interfaz gráfica
"""


# Conexión a la base de datos
cnx = mysql.connector.connect(host="tu_host",
                              user="tu_usuario",
                              password="tu_contraseña",
                              database="tu_base_de_datos")


# Funciones para manejar las tareas
def agregar_tarea():
    descripcion = entry_descripcion.get()
    fecha_vencimiento = entry_fecha_vencimiento.get()
    try:
        fecha_vencimiento = datetime.strptime(fecha_vencimiento,
                                              "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Error",
                             "Formato de fecha incorrecto (DD/MM/AAAA)")
        return
    cursor = cnx.cursor()
    query = "INSERT INTO tareas (descripcion, fecha_vencimiento) VALUES (%s, %s)"
    values = (descripcion, fecha_vencimiento)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    messagebox.showinfo("Éxito", "La tarea ha sido agregada exitosamente.")
    entry_descripcion.delete(0, tk.END)
    entry_fecha_vencimiento.delete(0, tk.END)


def mostrar_tareas():
    cursor = cnx.cursor()
    query = "SELECT id, descripcion, fecha_vencimiento, completada FROM tareas"
    cursor.execute(query)
    tareas = cursor.fetchall()
    tarea_text = ""
    for tarea in tareas:
        tarea_text += f"{tarea[0]} - {tarea[1]} - {tarea[2].strftime('%d/%m/%Y')} - {'Completada' if tarea[3] else 'En progreso'}\n"
    if tarea_text == "":
        tarea_text = "No hay tareas para mostrar."
    messagebox.showinfo("Tareas", tarea_text)
    cursor.close()


def actualizar_tarea():
    tarea_id = entry_tarea_id.get()
    completada = checkbutton_completada.get()
    cursor = cnx.cursor()
    query = "UPDATE tareas SET completada = %s WHERE id = %s"
    values = (completada, tarea_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    messagebox.showinfo("Éxito", "La tarea ha sido actualizada exitosamente.")
    entry_tarea_id.delete(0, tk.END)
    checkbutton_completada.set(False)


def eliminar_tarea():
    tarea_id = entry_tarea_id.get()
    cursor = cnx.cursor()
    query = "DELETE FROM tareas WHERE id = %s"
    values = (tarea_id, )
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    messagebox.showinfo("Éxito", "La tarea ha sido eliminada exitosamente.")
    entry_tarea_id.delete(0, tk.END)
    checkbutton_completada.set(False)


# Creación de la ventana principal
root = tk.Tk()
root.title("Sistema de gestión de tareas")
root.geometry("500x300")

# Labels y Entry para agregar tarea
label_descripcion = tk.Label(root, text="Descripción:")
label_descripcion.grid(row=0, column=0)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=0, column=1)
label_fecha_vencimiento = tk.Label(root,
                                   text="Fecha de vencimiento (DD/MM/AAAA):")
label_fecha_vencimiento.grid(row=1, column=0)
entry_fecha_vencimiento = tk.Entry(root)
entry_fecha_vencimiento.grid(row=1, column=1)

button_agregar_tarea = tk.Button(root,
                                 text="Agregar tarea",
                                 command=agregar_tarea)
button_agregar_tarea.grid(row=2, column=0)

# Labels y Entry para actualizar y eliminar tarea
label_tarea_id = tk.Label(root, text="ID de tarea:")
label_tarea_id.grid(row=3, column=0)
entry_tarea_id = tk.Entry(root)
entry_tarea_id.grid(row=3, column=1)
label_completada = tk.Label(root, text="Completada:")
label_completada.grid(row=4, column=0)
checkbutton_completada = tk.BooleanVar()
checkbutton_completada.set(False)
checkbutton = tk.Checkbutton(root, variable=checkbutton_completada)
checkbutton.grid(row=4, column=1)
button_actualizar_tarea = tk.Button(root,
                                    text="Actualizar tarea",
                                    command=actualizar_tarea)
button_actualizar_tarea.grid(row=5, column=0)
button_eliminar_tarea = tk.Button(root,
                                  text="Eliminar tarea",
                                  command=eliminar_tarea)
button_eliminar_tarea.grid(row=5, column=1)

# Botón para mostrar tareas
button_mostrar_tareas = tk.Button(root,
                                  text="Mostrar tareas",
                                  command=mostrar_tareas)
button_mostrar_tareas.grid(row=6, column=0, columnspan=2)

root.mainloop()

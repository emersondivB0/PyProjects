import tkinter as tk
from tkinter import messagebox
import sqlite3


class ToDoList:

    def __init__(self):
        self.conn = sqlite3.connect('tareas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT NOT NULL,
                fecha DATE NOT NULL
            );
        ''')
        self.conn.commit()

        self.ventana = tk.Tk()
        self.ventana.title("To-Do List")

        # Crear lista de tareas
        self.lista_tareas = tk.Listbox(self.ventana, width=50)
        self.lista_tareas.grid(row=0, column=1, padx=5, pady=5)

        # Crear botones
        boton_agregar = tk.Button(self.ventana,
                                  text="Agregar tarea",
                                  command=self.agregar_tarea)
        boton_agregar.grid(row=1, column=0, padx=5, pady=5)

        boton_eliminar = tk.Button(self.ventana,
                                   text="Eliminar tarea",
                                   command=self.eliminar_tarea)
        boton_eliminar.grid(row=2, column=0, padx=5, pady=5)

        boton_actualizar = tk.Button(self.ventana,
                                     text="Actualizar tarea",
                                     command=self.actualizar_tarea)
        boton_actualizar.grid(row=3, column=0, padx=5, pady=5)

        # Conectar a la base de datos
        self.conexion = sqlite3.connect("tareas.db")
        self.cursor = self.conexion.cursor()

        # Cargar tareas desde la base de datos
        self.cargar_tareas()

        self.ventana.mainloop()

    def cargar_tareas(self):
        """self.lista_tareas.delete(0, tk.END)
        #filas = self.cursor.fetchall()
        tareas = self.cursor.execute('SELECT * FROM tareas').fetchall()
        for tarea in tareas:
            tarea_str = f"{tarea[1]} ({tarea[2]})"
            self.lista_tareas.insert(tk.END, tarea_str) """
        # Limpiar la lista de tareas

        self.lista_tareas.delete(0, tk.END)

        # Cargar tareas desde la base de datos
        self.cursor.execute("SELECT * FROM tareas")
        tareas = self.cursor.fetchall()

        # Mostrar tareas en la lista
        for tarea in tareas:
            descripcion = tarea[1]
            fecha = tarea[2]
            self.lista_tareas.insert(tk.END, f"{descripcion} - {fecha}")



    def agregar_tarea(self):
        """descripcion = self.input_descripcion.get()
        fecha = self.input_fecha.get()
        if descripcion != "" and fecha != "":
            self.cursor.execute(
                'INSERT INTO tareas (descripcion, fecha) VALUES (?, ?)',
                [descripcion, fecha])
            self.conn.commit()
            self.input_descripcion.delete(0, tk.END)
            self.input_fecha.delete(0, tk.END)
            self.cargar_tareas()
        else:
            messagebox.showerror(
                "Error", "La descripción y la fecha no pueden estar vacías")"""
        # Obtener descripción de la tarea y la fecha

        descripcion = self.entrada_tarea.get().strip()
        fecha = self.entrada_fecha.get().strip()

        # Agregar tarea a la base de datos
        self.cursor.execute(
        "INSERT INTO tareas (descripcion, fecha) VALUES (?, ?)", (descripcion, fecha))
        self.conexion.commit()

        # Limpiar las entradas de texto
        self.entrada_tarea.delete(0, tk.END)
        self.entrada_fecha.delete(0, tk.END)

        # Actualizar la lista de tareas
        self.cargar_tareas()

    def actualizar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            descripcion = self.input_descripcion.get()
            fecha = self.input_fecha.get()
            if descripcion != "" and fecha != "":
                tarea_id = self.cursor.execute('SELECT id FROM tareas ORDER BY id DESC LIMIT 1').fetchone()[0]
                self.cursor.execute('UPDATE tareas SET descripcion = ?, fecha = ? WHERE id = ?', [descripcion, fecha, tarea_id])
                self.conn.commit()
                self.input_descripcion.delete(0, tk.END)
                self.input_fecha.delete(0, tk.END)
                self.cargar_tareas()
            else:
                messagebox.showerror("Error", "La descripción y la fecha no pueden estar vacías")
        else:
            messagebox.showerror("Error", "Debe seleccionar una tarea para actualizar")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_seleccionada = self.lista_tareas.get(seleccion[0])
            tarea_descripcion = tarea_seleccionada.split(" (")[0]
            tarea_id = self.cursor.execute('SELECT id FROM tareas WHERE descripcion = ?', [tarea_descripcion]).fetchone()[0]
            self.cursor.execute('DELETE FROM tareas WHERE id = ?', [tarea_id])
            self.conn.commit()
            self.input_descripcion.delete(0, tk.END)
            self.input_fecha.delete(0, tk.END)
            self.cargar_tareas()
        else:
            messagebox.showerror("Error", "Debe seleccionar una tarea para eliminar")

ToDoList()

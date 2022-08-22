import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from DataHandler import DataHandler
from FileParser import FileParser
from tkinter import ttk

dataHandler = DataHandler()
fileParser = FileParser()


def handle_courses():

    if dataHandler.all_courses:
        courses_window = tk.Toplevel()
        cv = tk.Canvas(courses_window, height=HEIGHT, width=900)
        cv.pack()
        table = ttk.Treeview(courses_window, height=20)
        table.place(x=10, y=10)
        table['columns'] = ('code', 'name', 'pre_requisites', 'is_required', 'semester', 'points', 'status')
        cell_size = 120
        table.column('#0', width=0, stretch=False)
        table.column('code', anchor=tk.CENTER, width=cell_size)
        table.column('name', anchor=tk.CENTER, width=cell_size)
        table.column('pre_requisites', anchor=tk.CENTER, width=cell_size)
        table.column('is_required', anchor=tk.CENTER, width=cell_size)
        table.column('semester', anchor=tk.CENTER, width=cell_size)
        table.column('points', anchor=tk.CENTER, width=cell_size)
        table.column('status', anchor=tk.CENTER, width=cell_size)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading('code', text='Código', anchor=tk.CENTER)
        table.heading('name', text='Nombre', anchor=tk.CENTER)
        table.heading('pre_requisites', text='Pre-Requisitos', anchor=tk.CENTER)
        table.heading('is_required', text='Es Obligatorio', anchor=tk.CENTER)
        table.heading('semester', text='Semestre', anchor=tk.CENTER)
        table.heading('points', text='Puntos', anchor=tk.CENTER)
        table.heading('status', text='Estado', anchor=tk.CENTER)

        for index, course in enumerate(dataHandler.all_courses):
            pre_requisites = ''
            for requisite in course.prerequisites:
                pre_requisites + requisite.code + ','
            table.insert(parent='',
                         index='end',
                         text='',
                         values=(course.code,
                                 course.name,
                                 pre_requisites,
                                 course.is_required,
                                 course.semester,
                                 course.points,
                                 course.status))

    else:
        messagebox.showinfo(message='Debe cargar un archivo primero', title='Error')


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("LFP Files", ".lfp")])
    print('Filepath: ', filepath)
    fileParser.file_location = filepath
    parsed_data = fileParser.parse_file()
    if len(parsed_data.errors) > 0:
        messagebox.showinfo('El archivo contiene errores')
    else:
        dataHandler.all_courses = parsed_data.data


HEIGHT = 400
WIDTH = 600

ws = tk.Tk()
ws.title("Práctica 1")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()
tk.Label(ws, text="Nombre del curso. Lab Lenguajes Formales y de Programación").place(x=80, y=100)
tk.Label(ws, text="Nombre del Estudiante: Carlos Rolando Barrera Rodríguez").place(x=80, y=130)
tk.Label(ws, text="Carné del Estudiante: 201403796").place(x=80, y=60)

tk.Button(ws,
          text="Cargar Archivo",
          bg="#82CC6C",
          fg="black",
          highlightbackground="#82CC6C",
          highlightthickness=1,
          borderwidth=0.2,
          relief="groove",
          width=20,
          command=lambda: open_file()).place(x=80, y=190)
tk.Button(ws,
          text="Gestionar Cursos",
          bg="#82CC6C",
          fg="black",
          highlightbackground="#82CC6C",
          highlightthickness=1,
          borderwidth=0.2,
          width=20,
          relief="groove",
          command=lambda: handle_courses()).place(x=80, y=230)

tk.Button(ws,
          text="Conteo de créditos",
          bg="#82CC6C",
          fg="black",
          highlightbackground="#82CC6C",
          highlightthickness=1,
          borderwidth=0.2,
          relief="groove",
          width=20,
          command=lambda: handle_courses()).place(x=80, y=270)

tk.Button(ws,
          text="Salir",
          bg="#82CC6C",
          fg="black",
          highlightbackground="#82CC6C",
          highlightthickness=1,
          borderwidth=0.2,
          relief="groove",
          width=20,
          command=lambda: exit()).place(x=80, y=310)

# button.pack()

ws.mainloop()

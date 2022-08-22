import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from DataHandler import DataHandler
from FileParser import FileParser
from tkinter import ttk
from Prerequisite import Prerequisite
from Course import Course

dataHandler = DataHandler()
fileParser = FileParser()


def handle_courses():
    if dataHandler.all_courses:
        courses_window = tk.Toplevel()
        cv = tk.Canvas(courses_window, height=HEIGHT+100, width=900)
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

        tk.Button(cv,
                  text="Agregar",
                  bg="#82CC6C",
                  fg="black",
                  highlightbackground="#82CC6C",
                  highlightthickness=1,
                  borderwidth=0.2,
                  relief="groove",
                  width=20,
                  command=lambda: create_course()).place(x=10, y=400)
        tk.Button(cv,
                  text="Editar",
                  bg="#82CC6C",
                  fg="black",
                  highlightbackground="#82CC6C",
                  highlightthickness=1,
                  borderwidth=0.2,
                  relief="groove",
                  width=20,
                  command=lambda: create_course()).place(x=200, y=400)

        tk.Button(cv,
                  text="Borrar",
                  bg="#82CC6C",
                  fg="black",
                  highlightbackground="#82CC6C",
                  highlightthickness=1,
                  borderwidth=0.2,
                  relief="groove",
                  width=20,
                  command=lambda: delete_course()).place(x=390, y=400)

        for index, course in enumerate(dataHandler.all_courses):
            pre_requisites = ''
            for requisite in course.prerequisites:
                pre_requisites = pre_requisites + requisite.code + ','
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


def delete_course():
    delete_course_window = tk.Toplevel()
    cv = tk.Canvas(delete_course_window, height=HEIGHT + 100, width=900)
    cv.pack()

    tk.Label(cv, text="Codigo").place(x=80, y=10)
    code_entry = ttk.Entry(cv)
    code_entry.place(x=80, y=30)
    tk.Button(cv,
              text="Guardar",
              bg="#82CC6C",
              fg="black",
              highlightbackground="#82CC6C",
              highlightthickness=1,
              borderwidth=0.2,
              relief="groove",
              width=20,
              command=lambda: del_course(Course(code=code_entry.get()))).place(x=80, y=60)


def del_course(code):
    dataHandler.delete_course(code)


def create_course():
    create_course_window = tk.Toplevel()
    cv = tk.Canvas(create_course_window, height=HEIGHT + 100, width=900)
    cv.pack()

    tk.Label(cv, text="Codigo").place(x=80, y=10)
    code_entry = ttk.Entry(cv)
    code_entry.place(x=80, y=30)

    tk.Label(cv, text="Nombre:").place(x=80, y=70)
    name_entry = ttk.Entry(cv)
    name_entry.place(x=80, y=100)

    tk.Label(cv, text="Pre-Requisito:").place(x=80, y=130)
    pre_requisite_entry = ttk.Entry(cv)
    pre_requisite_entry.place(x=80, y=160)

    tk.Label(cv, text="Semestre:").place(x=80, y=190)
    semester_entry = ttk.Entry(cv)
    semester_entry.place(x=80, y=220)

    tk.Label(cv, text="Opcionalidad:").place(x=80, y=250)
    is_required_entry = ttk.Entry(cv)
    is_required_entry.place(x=80, y=280)

    tk.Label(cv, text="Créditos:").place(x=80, y=310)
    credits_entry = ttk.Entry(cv)
    credits_entry.place(x=80, y=340)

    tk.Label(cv, text="Estado:").place(x=80, y=370)
    status_entry = ttk.Entry(cv)
    status_entry.place(x=80, y=400)

    tk.Button(cv,
              text="Guardar",
              bg="#82CC6C",
              fg="black",
              highlightbackground="#82CC6C",
              highlightthickness=1,
              borderwidth=0.2,
              relief="groove",
              width=20,
              command=lambda: save_course(
                  code_entry.get(),
                  name_entry.get(),
                  pre_requisite_entry.get(),
                  semester_entry.get(),
                  is_required_entry.get(),
                  credits_entry.get(),
                  status_entry.get())).place(x=80, y=450)


def save_course(code, name, pre_requisites, semester, is_required, points, status):
    pre_requisites_parsed = pre_requisites.rstrip("\n").split(";")
    pre_requisites_list = []
    for pre in pre_requisites_parsed:
        pre_requisites_list.append(Prerequisite(pre))

    new_course = Course(code=code, name=name, prerequisites=pre_requisites_list, semester=semester, is_required=is_required, points=points, status=status)
    dataHandler.add_single_course(new_course=new_course)


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("LFP Files", ".lfp")])
    print('Filepath: ', filepath)
    fileParser.file_location = filepath
    parsed_data = fileParser.parse_file()
    if len(parsed_data.errors) > 0:
        messagebox.showinfo('El archivo contiene errores')
    else:
        dataHandler.all_courses = parsed_data.data


def open_calculation():
    if dataHandler.all_courses:
        calculations_window = tk.Toplevel()
        cv = tk.Canvas(calculations_window, height=HEIGHT+100, width=900)
        cv.pack()
        tk.Label(cv, text="Créditos aprobados: " + str(dataHandler.sum_approved_credits())).place(x=80, y=100)
        tk.Label(cv, text="Créditos cursando: " + str(dataHandler.count_current_courses_credits())).place(x=80, y=130)
        tk.Label(cv, text="Créditos pendientes: " + str(dataHandler.count_pending_courses_credits())).place(x=80, y=160)

        tk.Label(cv, text="Créditos hasta el semestre:").place(x=80, y=200)
        entry = ttk.Entry(cv)
        entry.place(x=80, y=230)
        tk.Button(cv,
                  text="Calcular",
                  bg="#82CC6C",
                  fg="black",
                  highlightbackground="#82CC6C",
                  highlightthickness=1,
                  borderwidth=0.2,
                  relief="groove",
                  width=20,
                  command=lambda: show_credits_until_semester(entry.get())).place(x=80, y=260)

        tk.Label(cv, text="Créditos del semestre:").place(x=80, y=300)
        entry2 = ttk.Entry(cv)
        entry2.place(x=80, y=330)
        tk.Button(cv,
                  text="Calcular",
                  bg="#82CC6C",
                  fg="black",
                  highlightbackground="#82CC6C",
                  highlightthickness=1,
                  borderwidth=0.2,
                  relief="groove",
                  width=20,
                  command=lambda: show_semester_credits(entry2.get())).place(x=80, y=360)

    else:
        messagebox.showinfo(message='Debe cargar un archivo primero', title='Error')


def show_credits_until_semester(semester):
    if not semester.isnumeric():
        messagebox.showinfo(message='Debe ingresar un valor numérico de semestre', title='Error')
    elif int(semester) > 10:
        messagebox.showinfo(message='No puede ingresar un semestre mayor a 10', title='Error')
    else:
        messagebox.showinfo(message='Los créditos hasta el semestre ' +
                                    str(semester) + ' es: ' +
                                    str(dataHandler.sum_credits(int(semester))), title='Error')


def show_semester_credits(semester_number):
    if not semester_number.isnumeric():
        messagebox.showinfo(message='Debe ingresar un valor numérico de semestre', title='Error')
    elif int(semester_number) > 10:
        messagebox.showinfo(message='No puede ingresar un semestre mayor a 10', title='Error')
    else:
        data_result = dataHandler.get_semester_data(int(semester_number))
        messagebox.showinfo(message='Total Créditos Aprobados: ' +
                                    str(data_result.approved) +
                                    ', Total créditos asignados: ' +
                                    str(data_result.coursing) +
                                    ', Total pendientes: ' +
                                    str(data_result.pending), title='Error')


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
          command=lambda: open_calculation()).place(x=80, y=270)

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

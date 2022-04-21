# Bibliotecas necesarias
from cgi import test
from tkinter import *
from tkcalendar import Calendar  
from datetime import *
from tkinter import font as tkfont

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        #removed slant="italic"
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        # El contenedor permite apilar varios frames uno sobre otro, entonces el que queremos que sea visible será mostrado sobre los demás.
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PCalendario, PClase, PAgregarAsistente, PClientes, PAgregarCliente, PModificarCliente):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Se ponen todos los frames uno sobre otro dejando al visible al tope.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PCalendario")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Frame del calendario
class PCalendario(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes",
                            command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)
        #btn_calendario.grid(row=0, column=0, sticky="nw")
        #btn_clientes.grid(row=0, column=1, sticky="nw")
        #frm_buttons.grid(row=0, column=0, sticky="nw")

        frm_calendario = Frame(self)
        label = Label(frm_calendario, text="Calendario", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #label.grid(row=1, column=0, sticky="ew")

        #Calendario
        cal = Calendar(frm_calendario, selectmode = 'day',
                       year = datetime.now().year, month = datetime.now().month,
                       day = datetime.now().day, font = "Arial 15")
        cal.pack()
        #cal.grid(row=2, column=0)

        btn_clase = Button(frm_calendario, text="Revisar Clase", command=lambda: controller.show_frame("PClase"))
        btn_clase.pack(pady=15)

        frm_calendario.pack()
        #frm_calendario.grid(row=2, column=0, sticky="ew")

#Frame de las Clases
class PClase(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes", command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)

        #Información de la Clase
        frm_clase = Frame(self)
        label = Label(frm_clase, text="Clase de la Fecha ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        datos = ["Cliente", 
                "Cliente", 
                "Cliente",
                "Cliente",
                "Cliente"]

        for idx, text in enumerate(datos):
            entradas = Label(frm_clase, text = "#" + str(idx+1) + " - " + text, relief=RAISED)
            entradas.pack(pady=5)
        frm_clase.pack()

        #Botones de opciones
        frm_clase_botones = Frame(self)
        btn_agregar = Button(frm_clase_botones, text = "Agregar Asistente", command=lambda: controller.show_frame("PAgregarAsistente"))
        btn_remover = Button(frm_clase_botones, text = "Remover Asistente")
        btn_regresar = Button(frm_clase_botones, text="Regresar a Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_agregar.pack(padx=5, pady=15, side=LEFT)
        btn_remover.pack(padx=5, pady=15, side=LEFT)
        btn_regresar.pack(padx=5, pady=15, side=LEFT)
        frm_clase_botones.pack()

#Frame para agregar asistentes a la clase
class PAgregarAsistente(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones Principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes", command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)

        #Ingreso del asistente
        frm_agregar = Frame(self)
        label = Label(frm_agregar, text="Agregar Cliente Asistente", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        nombre = Label(frm_agregar, text="Nombre de Asistente:")
        nombre.pack(side=LEFT)
        entry = Entry(frm_agregar, width=30)
        entry.pack(side=LEFT)
        btn_agregar = Button(frm_agregar, text="Agregar")
        btn_agregar.pack(side=LEFT)
        frm_agregar.pack()

        #Botón de regreso
        frm_regreso = Frame(self)
        btn_regresar = Button(frm_regreso, text="Regresar",
                           command=lambda: controller.show_frame("PClase"))
        btn_regresar.pack(pady=15)
        frm_regreso.pack()

#Frame para mostrar clientes registrados. Quiero usar .json para registrar los clientes y las clases pero no creo que completaré esto a tiempo
class PClientes(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones Principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", 
                            command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes",
                            command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)
        #btn_calendario.grid(row=0, column=0, sticky="nw")
        #btn_clientes.grid(row=0, column=1, sticky="nw")
        #frm_buttons.grid(row=0, column=0, sticky="nw")
        
        #Datos de Clientes
        frm_clientes_datos = Label(self)
        label = Label(frm_clientes_datos, text="Clientes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #label.grid(row=1, column=0, sticky="ew")

        datos = ["Nombre: Cliente \nPago por Clase: 14\nNúmero de Clases: 10", 
                "Nombre: Cliente \nPago por Clase: 11\nNúmero de Clases: 8", 
                "Nombre: Cliente \nPago por Clase: 13\nNúmero de Clases: 15",
                "Nombre: Cliente \nPago por Clase: 9\nNúmero de Clases: 18",
                "Nombre: Cliente \nPago por Clase: 11\nNúmero de Clases: 12"]

        for idx, text in enumerate(datos):
            entradas = Label(frm_clientes_datos, text = "#" + str(idx+1) + " - " + text, relief=RAISED)
            entradas.pack(pady=5)
        frm_clientes_datos.pack()

        #Botones de opcioes
        frm_clientes_botones = Frame(self)
        btn_agregar = Button(frm_clientes_botones, text = "Agregar Cliente", command=lambda: controller.show_frame("PAgregarCliente"))
        btn_modificar = Button(frm_clientes_botones, text = "Modificar Cliente", command=lambda: controller.show_frame("PModificarCliente"))
        btn_borrar = Button(frm_clientes_botones, text = "Eliminar Cliente")
        btn_regresar = Button(frm_clientes_botones, text="Regresar a calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_agregar.pack(padx=5, pady=15, side=LEFT)
        btn_modificar.pack(padx=5, pady=15, side=LEFT)
        btn_borrar.pack(padx=5, pady=15, side=LEFT)
        btn_regresar.pack(padx=5, pady=15, side=LEFT)
        frm_clientes_botones.pack()

#Frame para agregar clientes
class PAgregarCliente(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones Principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes", command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)

        #Entrar datos
        frm_agregar_cliente = Frame(self, relief=RAISED, bd=3)
        label = Label(frm_agregar_cliente, text="Agregar Cliente", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        datos = ["Nombre:", 
                "Pago por Clase:", 
                "Número de Clases:"]

        for idx, text in enumerate(datos):
            frm = Frame(frm_agregar_cliente)
            datos = Label(frm, text = text)
            datos.pack(side=LEFT)
            entrada = Entry(frm, width=30)
            entrada.pack(side=LEFT)
            frm.pack()
        frm_agregar_cliente.pack()

        #Botones de opciones
        frm_botones = Frame(self)
        btn_agregar = Button(frm_botones, text="Agregar")
        btn_agregar.pack(side=LEFT, pady=15)
        btn_regresar = Button(frm_botones, text="Regresar", command=lambda: controller.show_frame("PClientes"))
        btn_regresar.pack(side=LEFT, pady=15)
        frm_botones.pack()

#Frame para modificar clientes
class PModificarCliente(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #Botones Principales
        frm_buttons = Frame(self, relief=RAISED)
        btn_calendario = Button(frm_buttons, text = "Calendario", command=lambda: controller.show_frame("PCalendario"))
        btn_clientes = Button(frm_buttons, text="Clientes", command=lambda: controller.show_frame("PClientes"))
        btn_calendario.pack(side=LEFT)
        btn_clientes.pack(side=LEFT)
        frm_buttons.pack(fill=BOTH)

        #Entrar datos para modificar
        frm_agregar_cliente = Frame(self, relief=RAISED, bd=3)
        label = Label(frm_agregar_cliente, text="Modificar Cliente", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        datos = ["Nombre:", 
                "Pago por Clase:", 
                "Número de Clases:"]

        for idx, text in enumerate(datos):
            frm = Frame(frm_agregar_cliente)
            datos = Label(frm, text = text)
            datos.pack(side=LEFT)
            entrada = Entry(frm, width=30)
            entrada.pack(side=LEFT)
            frm.pack()
        frm_agregar_cliente.pack()

        #Botones de opciones
        frm_botones = Frame(self)
        btn_agregar = Button(frm_botones, text="Actualizar")
        btn_agregar.pack(side=LEFT, pady=15)
        btn_regresar = Button(frm_botones, text="Regresar", command=lambda: controller.show_frame("PClientes"))
        btn_regresar.pack(side=LEFT, pady=15)
        frm_botones.pack()

#Iniciar aplicación
if __name__ == "__main__":
    app = SampleApp()
    app.title("Calendario para Actividad en Equilibrio")
    #app.geometry("800x400")
    app.mainloop()
from tkinter import *

class Ventana:
    def __init__(self):
        # Crear la instancia de Tk dentro del constructor
        self.aplicacion = Tk()

    def ventana_inicio(self):
        # Tamaño de la ventana
        self.aplicacion.geometry('1300x630+0+0')
        # No maximiza la pestaña
        self.aplicacion.resizable(0, 0)
        # Titulo de ventana
        self.aplicacion.title("CodeWiseAI")
        # Color de ventana
        self.aplicacion.config(bg='gray')

    def menu_ventana(self):
        # Crear la barra de menú
        menubar = Menu(self.aplicacion)

        # Variables para los check buttons
        self.markdown_var = IntVar()
        self.comentar_var = IntVar()
        self.buenas_practicas_var = IntVar()
        self.analisis_clase_var = IntVar()

        # Función que se llama cuando se cambia el estado de los check buttons
        def toggle_check(var, label):
            if var.get() == 1:
                print(f"{label} activado")
                menubar.entryconfig(label, foreground="green")  # Cambiar color a verde si está activado
            else:
                print(f"{label} desactivado")
                menubar.entryconfig(label, foreground="black")  # Volver al color original

        # Agregar los check buttons directamente a la barra de menú
        menubar.add_checkbutton(label="Markdown", variable=self.markdown_var,
                                command=lambda: toggle_check(self.markdown_var, "Markdown"),
                                foreground="black", selectcolor="green")  # Color cuando está seleccionado
        menubar.add_checkbutton(label="Comentar Código", variable=self.comentar_var,
                                command=lambda: toggle_check(self.comentar_var, "Comentar Código"),
                                foreground="black", selectcolor="green")  # Color cuando está seleccionado
        menubar.add_checkbutton(label="Buenas Prácticas", variable=self.buenas_practicas_var,
                                command=lambda: toggle_check(self.buenas_practicas_var, "Buenas Prácticas"),
                                foreground="black", selectcolor="green")  # Color cuando está seleccionado
        menubar.add_checkbutton(label="Análisis de Clase", variable=self.analisis_clase_var,
                                command=lambda: toggle_check(self.analisis_clase_var, "Análisis de Clase"),
                                foreground="black", selectcolor="green")  # Color cuando está seleccionado

        # Mostrar la barra de menú
        self.aplicacion.config(menu=menubar)

    def iniciar_aplicacion(self):
        # Ejecutar el mainloop después de configurar la ventana y el menú
        self.aplicacion.mainloop()

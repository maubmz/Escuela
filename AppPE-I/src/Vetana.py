from tkinter import *

# Inicio de la ventana
aplicacion = Tk()

def vetana_incio():
    # Tamaño de la ventana
    aplicacion.geometry('1300x630+0+0')
    # No maximiza la pestaña
    aplicacion.resizable(0, 0)
    # Titulo de ventana
    aplicacion.title("CodeWiseAI")
    # Color de ventana
    aplicacion.config(bg='gray')
    # Evita que cierre la pestaña
    aplicacion.mainloop()

def componentes_ventana():
    panel_inferior = Frame(aplicacion, bd=1, relief=FLAT)
    panel_inferior.pack(side=TOP)

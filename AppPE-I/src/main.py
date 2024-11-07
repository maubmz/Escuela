import customtkinter as ctk

from src.interfaz.Vetana import InterfazApp


# Clase Main que crea la ventana y ejecuta la interfaz
def main():
    root = ctk.CTk()  # Usar CTk en lugar de Tk
    InterfazApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
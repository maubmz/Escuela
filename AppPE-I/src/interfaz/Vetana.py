import customtkinter as ctk


class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeWiseAI")
        self.root.geometry("1500x900")  # Tamaño inicial de la ventana
        self.root.config(bg="lightgray")  # Aseguramos que el fondo de la ventana es gris

        # Crear un panel superior
        panel_superior = ctk.CTkFrame(self.root, fg_color="black")
        panel_superior.pack(side="top", fill="x")

        # Crear el label "ApiKey"
        self.label_apikey = ctk.CTkLabel(panel_superior, text="ApiKey", font=("Arial", 16))
        self.label_apikey.pack(side="left", padx=10, pady=10)

        # Crear el campo de entrada (entry) para la ApiKey
        self.entrada_superior = ctk.CTkEntry(panel_superior, width=800, font=("Arial", 16))
        self.entrada_superior.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # Crear los botones
        self.boton_markdown = ctk.CTkButton(panel_superior, text="Markdown", width=100, height=40, corner_radius=10,
                                            fg_color="gray", hover_color="lightgray",
                                            command=lambda: self.toggle_button_color(self.boton_markdown, "Markdown"))
        self.boton_markdown.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.boton_comentar_codigo = ctk.CTkButton(panel_superior, text="Comentar\nCódigo", width=100, height=40,
                                                   corner_radius=10, fg_color="gray", hover_color="lightgray",
                                                   command=lambda: self.toggle_button_color(self.boton_comentar_codigo,
                                                                                            "Comentar código"))
        self.boton_comentar_codigo.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.boton_buenas_practicas = ctk.CTkButton(panel_superior, text="Buenas\nPrácticas", width=100, height=40,
                                                    corner_radius=10, fg_color="gray", hover_color="lightgray",
                                                    command=lambda: self.toggle_button_color(
                                                        self.boton_buenas_practicas, "Buenas prácticas"))
        self.boton_buenas_practicas.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.boton_analisis_clase = ctk.CTkButton(panel_superior, text="Análisis de\nClase", width=100, height=40,
                                                  corner_radius=10, fg_color="gray", hover_color="lightgray",
                                                  command=lambda: self.toggle_button_color(self.boton_analisis_clase,
                                                                                           "Análisis de clase"))
        self.boton_analisis_clase.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # Crear un panel inferior
        panel_inferior = ctk.CTkFrame(self.root, fg_color="black")
        panel_inferior.pack(side="bottom", fill="x")

        # Cambiar a CTkTextbox para que sea un campo de texto multilinea
        self.entrada_inferior = ctk.CTkTextbox(panel_inferior, width=2000, height=50, corner_radius=10,
                                               font=("Arial", 16))
        self.entrada_inferior.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # Asociar la tecla "Enter" al campo de entrada para que también envíe el texto
        self.entrada_inferior.bind("<Return>", lambda event: self.mostrar_texto())

    # Función para capturar el texto
    def mostrar_texto(self):
        texto = self.entrada_inferior.get("1.0", "end-1c")  # Captura todo el texto desde la primera línea
        print(f"Texto ingresado: {texto}")

    # Función para cambiar el color del botón y mostrar el mensaje
    def toggle_button_color(self, button, nombre_opcion):
        current_color = button.cget("fg_color")  # Obtiene el color actual
        if current_color == "gray":
            new_color = "green"
            print(f"{nombre_opcion} seleccionado")
        else:
            new_color = "gray"
            print(f"{nombre_opcion} deseleccionado")

        button.configure(fg_color=new_color)  # Actualiza el color del botón

    # Funciones que se ejecutarán cuando se seleccionen las opciones (ya no son necesarias)
    def opcion_markdown(self):
        pass

    def opcion_comentar_codigo(self):
        pass

    def opcion_buenas_practicas(self):
        pass

    def opcion_analisis_clase(self):
        pass


# Clase Main que crea la ventana y ejecuta la interfaz
def main():
    root = ctk.CTk()  # Usar CTk en lugar de Tk
    app = InterfazApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import customtkinter as ctk
from src.openAi.Metodo_OpenAI import mensaje_sistema_ayuda, MetodoOpenAI


class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeWiseAI")
        self.root.geometry("1500x900")  # Tamaño inicial de la ventana
        self.root.config(bg="lightgray")  # Aseguramos que el fondo de la ventana es gris
        self.boton_state = []
        self.open_ai = None

        # Crear un panel superior
        panel_superior = ctk.CTkFrame(self.root, fg_color="black")
        panel_superior.pack(side="top", fill="x")

        # Crear el label "ApiKey"
        self.label_apikey = ctk.CTkLabel(panel_superior, text="ApiKey", font=("Arial", 16))
        self.label_apikey.pack(side="left", padx=10, pady=10)

        # Crear el campo de entrada (entry) para la ApiKey
        self.entrada_superior = ctk.CTkEntry(panel_superior, width=800, font=("Arial", 16))
        self.entrada_superior.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # Asociar la tecla "Enter" y "Shift+Enter" al campo ApiKey para capturar el texto
        self.entrada_superior.bind("<Return>", self.procesar_apikey)
        self.entrada_superior.bind("<Shift-Return>", self.procesar_apikey)

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

        # Crear un panel central
        panel_central = ctk.CTkFrame(self.root, fg_color="gray")
        panel_central.pack(side="top", fill="both", expand=True)  # Expande para llenar el espacio disponible

        # Importar ScrollableFrame de customtkinter
        self.scrollable_frame_central = ctk.CTkScrollableFrame(panel_central, width=800, height=600)
        self.scrollable_frame_central.pack(side="top", fill="both", expand=True)

        # Crear un panel inferior
        panel_inferior = ctk.CTkFrame(self.root, fg_color="black")
        panel_inferior.pack(side="bottom", fill="x")

        # Cambiar a CTkTextbox para que sea un campo de texto multilinea
        self.entrada_inferior = ctk.CTkTextbox(panel_inferior, width=2000, height=50, corner_radius=10,
                                               font=("Arial", 16))
        self.entrada_inferior.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # Asociar la tecla "Enter" al campo de entrada para que también envíe el texto
        self.entrada_inferior.bind("<Return>", self.procesar_texto_usuario)


    # Función para capturar el texto solo cuando se presiona Enter (sin Shift)
    def procesar_texto_usuario(self, event):
        # Verificar si se presionó la tecla "Enter"
        if event.keysym == "Return":
            if event.state & 0x0001:  # Si se presionó Shift+Enter
                return  # No hacer nada, solo permite el salto de línea
            else:  # Si solo se presionó Enter
                texto = self.entrada_inferior.get("1.0", "end-1c")  # Captura todo el texto desde la primera línea
                print(f"Texto ingresado: {texto}")
                self.entrada_inferior.delete("1.0", "end")  # Limpiar el campo de texto
                return "break"  # Evita el salto de línea con Enter solo

    # Función para procesar el texto ingresado en ApiKey
    def procesar_apikey(self, event):

        # Captura el texto cuando se presiona Enter o Shift+Enter
        apikey = self.entrada_superior.get()  # Obtener el texto de ApiKey
        print(f"ApiKey ingresada: {apikey}")

        # Llama al método para actualizar la API Key en Metodo_OpenAI
        self.open_ai = MetodoOpenAI(apikey)

        # Evitar la acción predeterminada de salto de línea en el campo ApiKey
        return "break"

    # Función para cambiar el color del botón y guardar texto del boton
    def toggle_button_color(self, button, nombre_opcion):
        current_color = button.cget("fg_color")  # Obtiene el color actual
        if current_color == "gray":
            new_color = "green"
            # print(f"{nombre_opcion} seleccionado")
            self.boton_state.append(nombre_opcion)
        else:
            new_color = "gray"
            # print(f"{nombre_opcion} deseleccionado")
            self.boton_state.remove(nombre_opcion)

        button.configure(fg_color=new_color)  # Actualiza el color del botón
        print(self.boton_state)

    # Método para imprimir mensajes en el panel central con el rol del mensaje
    def imprimir_mensaje_panel_central(self, mensaje, rol):
        if rol == "usuario":
            # prefijo = "Usuario: "
            color_fondo = "#E0E0E0"  # Color de fondo para la burbuja del usuario
            color_texto = "black"
        elif rol == "sistema":
            # prefijo = "Sistema: "
            color_fondo = "#0078D4"  # Color de fondo para la burbuja del sistema
            color_texto = "white"

        # Crear un marco que actúe como la burbuja del mensaje
        burbuja_frame = ctk.CTkFrame(self.scrollable_frame_central, fg_color=color_fondo)

        # Crear el mensaje dentro de la burbuja
        mensaje_label = ctk.CTkLabel(burbuja_frame, text= mensaje,
                                     font=("Arial", 14), text_color=color_texto, anchor="w")

        # Empaquetar el mensaje dentro del marco
        mensaje_label.pack(padx=10, pady=5, fill="x")

        # Empaquetar la burbuja en el panel central con alineación hacia la izquierda
        burbuja_frame.pack(anchor="w", padx=10, pady=5, fill="x")

    # Método para usar mensaje_sistema_ayuda
    def generar_mensaje_ayuda(self, codigo_usuario):
        mensaje = mensaje_sistema_ayuda(self.boton_state, codigo_usuario)
        # Llamamos a OpenAI para generar la ayuda
        respuesta = self.open_ai.metodo_openai(mensaje)

        respuesta_text = respuesta.content
        print(respuesta_text)

        # En lugar de imprimir en la consola, usamos el método para mostrar en el panel central
        self.imprimir_mensaje_panel_central(respuesta_text, "sistema")

    def procesar_texto_usuario(self, event):
        if event.keysym == "Return":
            if event.state & 0x0001:  # Si se presionó Shift+Enter
                return  # Permite el salto de línea
            else:  # Si solo se presionó Enter
                # Captura la ApiKey de entrada_superior
                apikey = self.entrada_superior.get()

                # Verifica si la ApiKey está vacía
                if not apikey:
                    print("Por favor, ingresa una ApiKey.")
                    return "break"

                # Actualiza self.open_ai con la ApiKey
                self.open_ai = MetodoOpenAI(apikey)

                # Captura el texto de entrada_inferior
                texto = self.entrada_inferior.get("1.0", "end-1c")

                # Imprime el mensaje en el panel central
                self.imprimir_mensaje_panel_central(texto, "usuario")

                # Limpia el campo de texto
                self.entrada_inferior.delete("1.0", "end")

                # Llama a generar_mensaje_ayuda con el texto
                self.generar_mensaje_ayuda(texto)

                return "break"  # Evita el salto de línea con Enter solo


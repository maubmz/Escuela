import openai
from openai import OpenAI

from src.mensajes.mensajes_asistencia import *


class MetodoOpenAI:
    def __init__(self, apikey):
        openai.api_key = apikey
        self.client = openai

    # Método donde se utiliza OpenAI y se genera un mensaje con ayudas externas
    def metodo_openai(self, sistema_ayuda: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # Asegúrate de usar un modelo válido
            messages=[
                {"role": "system", "content": peticion_sistema},
                {"role": "user", "content": user_generar},
                {"role": "assistant", "content": asistente_mensajes},
                {"role": "system", "content": sistema_ayuda},
            ],
        )
        return completion.choices[0].message


# Mensaje donde mediante unos textos que recibe como parametro y codigo del usuario genera un mensaje para enviar a la API de OpenAI
def mensaje_sistema_ayuda(estado_botones, respuesta_usuario):
    instrucciones = []

    if "Markdown" in estado_botones:
        instrucciones.append("realizar el archivo markdown")
    if "Comentar código" in estado_botones:
        instrucciones.append("comentar el código")
    if "Buenas prácticas" in estado_botones:
        instrucciones.append("darme buenas prácticas")
    if "Análisis de clase" in estado_botones:
        instrucciones.append("analizar el código")

    if instrucciones:
        # Combina todas las instrucciones en un solo mensaje
        mensaje_ayuda = f"Necesito que me ayudes a {', '.join(instrucciones)} del código siguiente:\n {respuesta_usuario}"
    else:
        # Caso cuando no se selecciona ninguna opción
        mensaje_ayuda = "El usuario no eligió ninguna opción, pero puede que haya enviado un mensaje. Envia un mensaje indicando que no eligió ninguna opción."

    return mensaje_ayuda



import openai


openai.api_key = ""

# Metodo para generar el mensaje de bienvenida
def generador_mensaje_inicio():
    pass

def generar_mensaje():
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content": "mensaje de inicio"},
            {"role": "system", "content": "mensaje de inicio"}
        ]
    )
    return response.choices[0].message.content


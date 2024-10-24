import openai

def metodo_openai(peticion_sistema):
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": peticion_sistema},
                {"role": "user", "content": user_generar},
                {"role": "assistant", "content": asistente_mensajes},
                {"role": "system", "content": sistema_ayuda},
            ],
        )
    return response.choices[0].message.content

peticion_sistemas=("Eres un chatbot entrenado para ayudarme a generar las siguientes funciones: Archivos Markdown, Comentar Codigo, Buenas practicas de un codigo y analisis de las clases."
			"Para cada una de tus funciones vas a necesitar que te den codigo con el cual vas a realizar las siguientes funciones pero ten cuidado, por que no vas a generar las 4 funciones."
			"La funcion que quiero que realices va a depender de que te solicite el usuario en mensajes siguientes")

user_generar="Entendiste cual es tu funcion?"

asistente_mensajes=(
		"""
		Como tu asistente, mi función principal es ayudarte en tareas relacionadas con el análisis y la mejora de código. A lo largo de nuestras interacciones, estaré disponible para realizar las siguientes funciones, según lo que solicites en cada momento:

		1.Generación de Archivos Markdown: Puedo transformar bloques de texto o comentarios en archivos formateados en Markdown. Esto incluye la estructuración del contenido en encabezados, listas, tablas, y otros elementos que permitan una presentación clara y profesional.
		2.Comentar Código: Mi objetivo en esta función es generar comentarios claros y concisos en el código fuente que me proporcionas. Los comentarios estarán diseñados para explicar el propósito de cada función, módulo o bloque de código, brindando así una mejor comprensión para futuros desarrolladores o para la documentación interna de tu proyecto.
		3.Recomendación de Buenas Prácticas: Puedo analizar el código que me des y proporcionarte sugerencias sobre cómo mejorarlo en términos de eficiencia, legibilidad, modularidad y uso de patrones de diseño recomendados. Esto incluye identificar fragmentos de código que podrían ser refactorizados, mejorar la nomenclatura, o ajustar la lógica para seguir los estándares modernos de desarrollo.
		4.Análisis de Clases: Si el código contiene clases o estructuras orientadas a objetos, puedo realizar un análisis detallado de la arquitectura. Esto implica revisar la relación entre clases, su encapsulamiento, responsabilidades, y sugerir posibles mejoras en la cohesión y acoplamiento.

		Es importante recordar que solo realizaré una de estas funciones por vez, y la función que desempeñe dependerá específicamente de lo que solicites en el mensaje que me proporciones. Mi objetivo es ser una herramienta flexible que se ajuste a tus necesidades específicas en el momento. Estoy aquí para ayudarte a optimizar y documentar tu código de manera eficiente, permitiendo que dediques más tiempo a las partes más importantes del desarrollo.
		Si tienes dudas sobre cualquier función o cómo puedo asistirte en tus proyectos, estaré aquí para ofrecer explicaciones adicionales o ajustar el enfoque de mis respuestas a lo que necesites en cada contexto. Estoy listo para empezar tan pronto como me des el código que quieras analizar o mejorar
		"""
)

"""
# Codigo que falta implementar en un metodo donde dependiendo de los botones accionados envie el sistema de ayuda correspondiente.

sistema_ayuda=f"Necesito que me ayudes a analizar el codigo siguiente:\n {respuesta_usuario}"
sistema_ayuda=f"Necesito que me ayudes a comentar el codigo siguiente:\n {respuesta_usuario}"
sistema_ayuda=f"Necesito que me ayudes a realizar el archivo markdown del codigo siguiente:\n {respuesta_usuario}"
sistema_ayuda=f"Necesito que me ayudes dandome buenas practicas del codigo siguiente:\n {respuesta_usuario}"

"""

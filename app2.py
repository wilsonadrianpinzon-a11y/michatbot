from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

# Simula el almacenamiento temporal de la adivinanza actual (en memoria)
# Solo se reinicia si se apaga el servidor
ultima_adivinanza = {"pregunta": "", "respuesta": ""}

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').lower().strip()
    resp = MessagingResponse()
    msg = resp.message()

    global ultima_adivinanza

    if "hola" in incoming_msg:
        msg.body("¡Hola! ¿Quieres que te cuente un chiste, trabalenguas o una adivinanza?")
    
    elif "chiste" in incoming_msg:
        chistes = [
            "¿Por qué el libro de matemáticas está triste? Porque tiene muchos problemas.",
            "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.",
            "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro."
        ]
        msg.body(random.choice(chistes))

    elif "adivinanza" in incoming_msg:
        adivinanzas = [
            ("Blanca por dentro, verde por fuera. ¿Qué es?", ["pera", "la pera"]),
            ("Vuelo sin alas, lloro sin ojos. ¿Qué soy?", ["nube", "una nube"]),
            ("Oro parece, plata no es, el que no lo adivine, bien tonto es.", ["plátano", "banana"])
        ]
        pregunta, respuestas = random.choice(adivinanzas)
        ultima_adivinanza["pregunta"] = pregunta
        ultima_adivinanza["respuesta"] = respuestas
        msg.body(pregunta)

    elif ultima_adivinanza["pregunta"]:
        # Validar si la respuesta es correcta
        if incoming_msg in ultima_adivinanza["respuesta"]:
            msg.body("¡Correcto! Muy bien.")
        else:
            msg.body("Mmm... no es correcto. Intenta de nuevo o escribe 'adivinanza' para otra.")
        # Limpiar la adivinanza para evitar repetir
        ultima_adivinanza = {"pregunta": "", "respuesta": ""}

    elif "trabalenguas" in incoming_msg:
        trabalenguas = [
            "Pepe Pecas pica papas con un pico, con un pico Pepe Pecas pica papas.",
            "Tres tristes tigres tragan trigo en un trigal.",
            "El cielo está encapotado, ¿quién lo desencapotará?"
        ]
        msg.body(random.choice(trabalenguas))

    else:
        msg.body("No entendí eso. Prueba diciendo 'hola', 'chiste', 'trabalenguas' o 'adivinanza'.")

    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False

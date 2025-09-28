from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)


@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hola" in incoming_msg:
        msg.body("¡Hola! ¿Quieres que te cuente sobre el medio ambiente?")
    elif "si" in incoming_msg:
        msg.body("el medio ambiente son los factores fisicos, quimicos y biologicos que rodean y afectan a los seres vivos en la tierra. quieres que hable sobre sus componentes, su importancia, los problemas ambientales o las acciones para protegerlo?")
    elif "sus componentes" in incoming_msg:
        msg.body("los componentes del medio ambiente son: 1. el aire que respiramos que puede estar contaminado por gases y particulas. 2. agua:Rios, lagos y oceanos que son esenciales para la vida. 3. suelo:sustenta a las plantas y es habitad de muchos organismos. 4.Flora y fauna que habitan en el planeta. 5. el clima que afecta la vida en la tierra")
    elif "su importancia" in incoming_msg:
        msg.body("la importancia del medio ambiente radica en ser un soporte de la vida, pues este proporciona los recursos necesarios para la supervivencia de los seres vivos como lo pueden ser el agua, alimentos y minerales. un medio ambiente saludable es esencial para la supervivencia de todas las especies incluyendo al humano")
    elif "los problemas ambientales" in incoming_msg:
        msg.body("los problemas ambientales son: 1.contaminacion: la contaminacion de suelos, agua y suelo son un problema grave que afecta la salud del ambiente. 2. cambio climatico: el cambio climatico es un problema que afecta a toda la vida en la tierra. 3.la deforestacion es un problema que afecta la supervivencia de especies y la salud del ecosistema")
    elif "acciones para protegerlo" in incoming_msg:
        msg.body("conservar el agua y reducir su consumo para protefer este recurso, proteger la biodiversidad y los ecosistemas para mantener la salud del planeta, reducir emiciones de gases efecto invernadero para mitigar el cambio climatico")
    else:
        msg.body("lo siento, no puedo ayudarte con eso.")



    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


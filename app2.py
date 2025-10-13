from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hola" in incoming_msg:
        msg.body("¡Hola! ¿Quieres que te cuente sobre el medio ambiente?")
    elif "si" in incoming_msg:
        msg.body(
            "El medio ambiente son los factores físicos, químicos y biológicos que rodean y afectan a los seres vivos en la Tierra.\n\n"
            "Puedo hablarte de él enfocándome en:\n"
            "1: Importancia\n"
            "2: Componentes\n"
            "3: Problemas ambientales\n"
            "4: Acciones de protección"
        )
    elif "1:importancia" in incoming_msg:
        msg.body("El medio ambiente es fundamental porque de él depende la vida en la Tierra. Nos proporciona los recursos naturales que necesitamos, como el agua, el aire, los alimentos y los materiales para construir y producir energía. Además, regula el clima, purifica el aire y el agua, y mantiene el equilibrio de los ecosistemas.")
    elif "2:componentes" in incoming_msg:
        msg.body(
            "Los componentes del medio ambiente son:\n"
            "1: Aire\n"
            "2: Agua\n"
            "3: Suelo\n"
            "4: Flora y fauna\n"
            "5: Clima\n\n"
            "Por favor, hazme saber si quieres que profundice en alguno de ellos."
        )
    elif "1:aire" in incoming_msg:
        msg.body("El aire es esencial para mantener un equilibrio natural y permitir la vida en el planeta. Cumple funciones vitales, como proporcionar oxígeno para la respiración de los seres vivos, dióxido de carbono para la fotosíntesis de las plantas y nitrógeno para el crecimiento de los organismos. Además, el aire ayuda a regular el clima, distribuir el calor solar y transportar la humedad.")
    elif "2:agua" in incoming_msg:
        msg.body("El agua es un componente fundamental del medio ambiente y uno de los recursos más importantes para la vida. Cubre la mayor parte del planeta y se encuentra en los ríos, mares, nubes, glaciares y en los seres vivos. Es esencial porque permite la hidratación, la alimentación, la agricultura, la industria y el equilibrio de los ecosistemas. Además regula la temperatura del planeta.")
    elif "3:suelo" in incoming_msg:
        msg.body("El suelo es la base donde crecen las plantas, que a su vez sostienen la vida de muchos seres vivos. Está formado por minerales, materia orgánica, agua, aire y microorganismos. Su importancia radica en que permite la producción de alimentos, regula el ciclo del agua, almacena nutrientes y sostiene ecosistemas terrestres. Además, el suelo actúa como un filtro natural que limpia el agua de lluvia y ayuda a mantener el equilibrio del planeta.")
    elif "4:flora y fauna" in incoming_msg:
        msg.body("Estos son seres vivos que habitan la tierra. La flora está formada por todas las plantas, árboles, arbustos y algas, que producen oxígeno y se alimentan a sí mismas por medio de la fotosíntesis, además de servir de refugio y alimento para muchas especies. La fauna incluye a todos los animales, desde los más pequeños hasta los más grandes, que contribuyen al equilibrio natural de diversas formas como la polinización, la dispersión de semillas y las cadenas alimenticias. Ambas son fundamentales para mantener un equilibrio ecológico.")
    elif "5:clima" in incoming_msg:
        msg.body("El clima es un conjunto de condiciones del tiempo que se repiten en un lugar a lo largo de los años, como la temperatura, la humedad, las lluvias, el viento y la presión. Es muy importante porque influye en la forma de vida de las personas, animales y plantas, determinando qué especies pueden habitar en cada región. También afecta actividades humanas como la agricultura y la ganadería, además de ayudar a mantener el equilibrio natural del planeta.")
    elif "3:problemas ambientales" in incoming_msg:
        msg.body(
            "Los problemas ambientales son alteraciones que dañan la naturaleza.\n"
            "Si gustas, puedo hablarte sobre:\n"
            "1: Contaminación\n"
            "2: Cambio climático\n"
            "3: Deforestación"
        )
    elif "1:contaminacion" in incoming_msg:
        msg.body("La contaminación es la presencia de sustancias o ruidos que alteran y dañan el medio ambiente. Afecta el aire cuando se liberan gases tóxicos por fábricas y vehículos; el agua cuando se arrojan desechos o productos químicos a ríos y mares; y el suelo cuando se acumulan basuras, pesticidas o residuos industriales. También existe la contaminación auditiva, causada por ruidos fuertes de tráfico, maquinaria o música a alto volumen que perjudican la salud y bienestar de las personas.")
    elif "2:cambio climatico" in incoming_msg:
        msg.body("El cambio climático es la variación global del clima provocada principalmente por la actividad humana. Se debe al aumento de gases que atrapan el calor como el dióxido de carbono y hacen que la temperatura del planeta suba. Esto causa fenómenos como el derretimiento de los polos, el aumento del nivel del mar, las sequías, las inundaciones y los cambios en los ecosistemas. Sus efectos afectan la agricultura, la salud, la biodiversidad y la vida de millones de personas.")
    elif "3:deforestacion" in incoming_msg:
        msg.body("La deforestación es la eliminación o destrucción de bosques y selvas, generalmente por actividades humanas como la agricultura, la ganadería, la tala indiscriminada y la expansión urbana. Este problema ambiental provoca la pérdida de hábitats para muchas especies, contribuye al cambio climático al reducir la cantidad de árboles que absorben el dióxido de carbono y causa la erosión del suelo y la disminución del agua.")
    elif "4:acciones de proteccion" in incoming_msg:
        msg.body("Las acciones de protección ambiental son todas aquellas prácticas que buscan cuidar y conservar la naturaleza. Entre ellas están reducir, reutilizar y reciclar los materiales para disminuir los residuos; ahorrar agua y energía; plantar árboles y proteger los bosques; usar medios de transporte sostenibles como la bicicleta o transporte público; y evitar la contaminación del aire, agua y suelo. También es importante educar y crear conciencia ambiental. Cada pequeña acción contribuye al bienestar del planeta y de las futuras generaciones.")
    elif "no" in incoming_msg:
        msg.body("Es una pena que no quieras saber sobre el medio ambiente, escríbeme de nuevo cuando estés interesado.")
    else:
        msg.body("Lo siento, no puedo ayudarte.")

    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


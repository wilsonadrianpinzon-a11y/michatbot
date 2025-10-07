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
        msg.body("el medio ambiente son los factores fisicos, quimicos y biologicos que rodean y afectan a los seres vivos en la tierra.  Puedo hablarte de el enfocandome en: 1:importancia    2:componentes    3:problemas ambientales    4:acciones de proteccion")
    elif "1:importancia" in incoming_msg:
        msg.body("El medio ambiente es fundamental por que de él depende la vida en la Tierra. Nos proporciona los recursos naturales que necesitamos, como el agua, el aire, los alimentos y los materiales para contruir y producir energia. Además, regula el clima, purifica el aire y el agua, de igual forma mantiene el quilibrio de los ecosistemas.")
    elif "2:componentes" in incoming_msg:
        msg.body("los componentes del medio ambiente son: 1:aire    2:agua    3:suelo    4:flora y fauna    5:clima.   por favor hazme saber si quieres que profundice en alguno de ellos.")
    elif "1:aire" in incoming_msg:
        msg.body("el aire es esencial para mantener un equilirio natural y permitir la vida en el planeta. Cumple funciones vitales, como proporcionar oxigeno para la respiracion de los seres vivos, dioxido de carbono para la fotosintesis de las plantas y nitrogenó para el crecimiento de los organismos. Además el aire ayuda a regular el clima, distribuir el calor solar y transportar la humedad.")
    elif "2:agua" in incoming_msg:
        msg.body("el agua es un componente fundamental del medio ambiente y uno de los recursos mas importantes para la vida. Cubre la mayor parte del planeta y se encuentra en los rios,mares,nubes,glaciares y en los seres vivos. Es esencial porque permite la hidratacion, la alimentacion, la agricultura, la industria y el equilibrio de los ecosistemas ademas regula la temperatura del planeta")
    elif "3:suelo" in incoming_msg:
        msg.body("el suelo es la base donde crecen las plantas, que a su vez sostienen la vida de muchos seres vivos. Esta formado por minerales, materia organica, agua, aire y microorganismos. Su importancia radica en que permite la produccion de alimentos, regula el ciclo del agua, almacena nutrientes y sostiene ecosistemas terrestres. Ademas el suelo actua como un filtro natural que limpia el agua de lluvia y ayuda a mantener el equilibrio del planeta")
    elif "4:flora y fauna" in incoming_msg:
        msg.body("estos son seres vivos que habitan la tierra. La flora esta formada por todas las plantas, arboles, arbustos, y algas, que producen oxigeno y se alimentan a si mismas por medio de la fotosintesis, ademas de servir de refugio y alimento para muchas especies. La fauna incluye a todos los animales desde los mas pequeños asta los mas grandes que contribuyen al equilibrio natural de diversas formas como lo puede ser la polinizacion, la dispercion de semillas y las cadenas alimenticias. ambas son fundamentales para mantener un equilibrio ecologico.")
    elif "5:clima" in incoming_msg:
        msg.body("el clima es un conjunto de condiciones del tiempo que se repiten en un lugar a lo largo de los años, como la temperatura, la humedad, las lluvias, el viento y la presión. Es muy importante porque influye en la forma de vida de las personas, animales y plantas, determinando que especies puede avitar en cada región. Tambien afecta actividades humanas como la agricultura y la ganaderia ademas de ayudar a mantener el equilibrio natural del planeta.")
    elif "3:problemas ambientales" in incoming_msg:
        msg.body("los problemas ambientales son alteraciones que dañan la naturaleza. Si gustas puedo hablarte sobre:     1:contaminacion    2:cambio climatico    3:deforestacion")
    elif "1:contaminacion" in incoming_msg:
        msg.body("la contaminacion es la presencia de sustancias o ruidos que alteran y dañan el medio ambiente. Afecta el aire cuando se liberan gases toxicos por fabricas y vehículos; el agua cuando se arrojan desechos o productos quimicos a rios y mares; y el suelo cuando se acumulan basuras, pesticidas o residuos industriales. Tambien existe la contaminacion auditiva, causada por ruidos fuertes de trafico, maquinaria o musica a alto volumen que perjudican la salud y bienestar de las personas.")
    elif "2:cambio climatico" in incoming_msg:
        msg.body("el cambio climatico es la variacion global del clima provocada principalmente por la actividad humana. Se debe al aumento de gases que atrapan el calor como el dioxido de carbono y hacen que la temperatura del planeta suba. Esto causa fenomenos como el derritimiento de los polos, el aumento del nivel del mar, las sequias, las inundaciones y los cambios en los ecosistemas. Sus efectos afectan la agricultura, la salud, la biodiversidad y la vida de millones de personas.")
    elif "3:deforestacion" in incoming_msg:
        msg.body("la deforestacion es la eliminacion o destruccion de bosques y selvas, generalmente por actividades humanas como la agricultura, la ganaderia, la tala indiscriminada y la expansión urbana. Este problema ambiental provoca la perdida de habitats para muchas especies, contribuye al cambio climatico al reducir la cantidad de arboles que absorven el dioxido de carbono y causa la erosíon del suelo y la disminucion del agua.")
    elif "4:acciones de proteccion" in incoming_msg:
        msg.body("las acciones de proteccion ambiental son todas aquellas practicas que buscan cuidar y conservar la naturaleza. Entre ellas estan reducir, reutilizar y reciclar los materiales para disminuir los resuidos; ahorrar agua y energia; plantar arboles y proteger los bosques; usar medios de transporte sostenibles como la bicicleta o transporte publico; y evitar la contaminacion del aire,agua y suelo. Tambien es importante educar y crear conciensia ambientarl. Cada pequeña accion contribuye al bienestar del planeta y de las futuras generaciones")
    elif "no" in incoming_msg:
        msg.body("es una pena que no quieras saber sobre el medio ambiente, escribeme denuevo cuando estes interesado")
    else:
        msg.body("lo siento, no puedo ayudarte")



    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

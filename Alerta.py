import urequests

url = "https://maker.ifttt.com/trigger/AlimentadorVacio/with/key/bOqOmrWh2aQdFdPBOw3MUI"

class CorreoElectronico:
    def __init__(self):
        print("")

    def alertEmpty (self, date):
        respuesta = urequests.get(url)
        #respuesta = urequests.get(url+"&field1="+str(random.randint(20,35))+"&field2="+str(random.randint(40,80)))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close()
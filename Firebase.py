import ufirebase as firebase

firebase.setURL("https://ifupbd-default-rtdb.firebaseio.com/")

class BaseDatos:
    def __init__(self):
        print("")

    def getFechaAnterior (self):
          firebase.get("Alimentador/FechaIni", "dato", bg=0)          
          return firebase.dato
    
    def setFechaActual (self,now):
          firebase.put("Alimentador/", {"FechaIni": now}, bg=0)
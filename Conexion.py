import network, time, urequests

class Wifi:
    def __init__(self):
        print("")

    def conectaWifi (self,red, password):
          global miRed
          miRed = network.WLAN(network.STA_IF)     
          if not miRed.isconnected():              #Si no está conectado…
              miRed.active(True)                   #activa la interface
              miRed.connect(red, password)         #Intenta conectar con la red
              print('Conectando a la red', red +"…")
              timeout = time.time ()
              while not miRed.isconnected():           #Mientras no se conecte..
                  if (time.ticks_diff (time.time (), timeout) > 10):
                      return False
          return True
    

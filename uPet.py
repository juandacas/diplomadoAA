#import network, time, urequests
from utime import sleep, mktime, localtime
from machine import Pin, ADC, PWM, RTC
from hcsr04 import HCSR04
from Conexion import Wifi
from Funciones import Proximidad, map, actualDate, diferenciaTiempo
from Firebase import BaseDatos
from Alerta import CorreoElectronico

servo = PWM(Pin(15), freq=50)
#--------------------------- [Conexion WiFi]---------------------------------------
wf = Wifi()
bd = BaseDatos()
ce = CorreoElectronico()
wf.conectaWifi("FAMILIA CASTRILLON RUIZ", "1070943923") #Conexion wifi

tem = 0
env = 0

while True:
    dif = diferenciaTiempo(actualDate(),bd.getFechaAnterior())
    print (actualDate())
    print (bd.getFechaAnterior())
    contenedor = Proximidad(5,18)    
    
    if contenedor > 10 and dif > 7200 and env == 0:
        print("Alerta de contener vacio")
        ce.alertEmpty(actualDate())
        env = 1
    
    dis = Proximidad(2,4) 
    if dis < 15 and dif > 7200:        
        comida = Proximidad(19,21)
        print(comida)
        if comida > 7:            
            m = map(180)#Compuerta abierta
            servo.duty(m)
            sleep(2)
            n = map(90)#Compuerta cerrada
            servo.duty(n)
            bd.setFechaActual(actualDate())
            tem = 1
            env = 0
        else:
            print("El plato contiene comida")
    else:
        print("Recientemente se sirvio, no debe servirse aún")
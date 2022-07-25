#import network, time, urequests
from utime import sleep, mktime, localtime
from machine import Pin, ADC, PWM, RTC
from hcsr04 import HCSR04
from Conexion import Wifi
from Funciones import Proximidad, map, actualDate, diferenciaTiempo
from Firebase import BaseDatos

servo = PWM(Pin(15), freq=50)
#--------------------------- [Conexion WiFi]---------------------------------------
wf = Wifi()
bd = BaseDatos()
wf.conectaWifi("FAMILIA CASTRILLON RUIZ", "1070943923") #Conexion wifi

tem = 0

while True:
    dif = diferenciaTiempo(actualDate(),bd.getFechaAnterior())
    print (actualDate())
    print (bd.getFechaAnterior())
    contenedor = Proximidad(5,18)    
    
    if contenedor > 10:
        print("Alerta para llenar el contenedor")
    
    dis = Proximidad(2,4)   
    #print(dis)
    #sleep(1)
    #712082211
    if dis < 15 and dif > 7200:        
        comida = Proximidad(19,21)
        print(comida)
        if comida < 10:            
            m = map(180)#Compuerta abierta
            servo.duty(m)
            sleep(2)
            n = map(90)#Compuerta cerrada
            servo.duty(n)
            bd.setFechaActual(actualDate())
            tem = 1
        else:
            print("El plato contiene comida")
    else:
        print("Recientente se sirvio, no debe servirse aún")
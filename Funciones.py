from Conexion import Wifi
from utime import sleep, mktime, localtime
from machine import Pin, ADC, PWM, RTC
from hcsr04 import HCSR04

#--------------------------- [Ultrasonido]---------------------------------------
def Proximidad(trigger,echo):
    sensor = HCSR04(trigger_pin=trigger,echo_pin=echo)
    dis = sensor.distance_cm()
    return dis

#--------------------------- [Servo]---------------------------------------
def map(x):
    return int((x - 0) * (125 - 25) / (180 - 0) + 25)

#--------------------------- [Tiempo]---------------------------------------
def actualDate():
    lt = localtime()
    now = mktime(lt)
    return now
    
#--------------------------- [Diferencias Tiempo]---------------------------------------
def diferenciaTiempo(ahora, antes):    
    return ahora-antes
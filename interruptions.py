# version interruption
import time 
from machine import Pin

bt1_ON_OFF = Pin(5, Pin.IN, Pin.PULL_UP)
etat_commande_bt1 = 0

led = Pin('LED', Pin.OUT) #sortie lampe
led.off()

bt2_ON_OFF = Pin(6, Pin.IN, Pin.PULL_UP)
etat_commande_bt2 = 0

start = time.ticks_ms()  

def programme_interruption_bt1(pin):
    global etat_commande_bt1
    global start
    delta = time.ticks_diff(time.ticks_ms(), start) # Antirebond
    if delta > 150 : 
        start = time.ticks_ms()    
        if etat_commande_bt1 :
            etat_commande_bt1 = 0
            led.off()
            print('OFF-bt1')
        else :
            etat_commande_bt1 = 1
            led.on()
            print('ON-bt1')
        

def programme_interruption_bt2(pin):
    global etat_commande_bt2
    global start
    delta = time.ticks_diff(time.ticks_ms(), start) # Antirebond
    if delta > 150 : 
        start = time.ticks_ms()    
        if etat_commande_bt2 :
            etat_commande_bt2 = 0
            print('OFF-bt2')
        else :
            etat_commande_bt2 = 1
            print('ON-bt2')


bt1_ON_OFF.irq(trigger=Pin.IRQ_RISING, handler=programme_interruption_bt1)
bt2_ON_OFF.irq(trigger=Pin.IRQ_RISING, handler=programme_interruption_bt2)


while True :
    time.sleep(100)       # sleep for 100 seconds
